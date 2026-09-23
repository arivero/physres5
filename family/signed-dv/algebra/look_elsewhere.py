"""
Look-elsewhere / Bayesian chance-probability analysis for the algebraic
identity

    m_h^2 / M_Z^2 = (15*sqrt(19) + 33*sqrt(3) + 5*sqrt(57) + 81) / 128
                  = 1.88508...

agreeing with the PDG value m_h^2/M_Z^2 = 125.20^2 / 91.1876^2 at the
10^-5 level.

This script does NOT redo the physics. It answers a single question:

    Given a "natural" family of closed-form expressions of comparable
    algebraic complexity, how many of them land within 10^-5 of the
    target value?

Three families are scanned:

    Family A   (the "narrow" family, tied to the dV construction):
               F(a,b,c,d) = (a*sqrt(19) + b*sqrt(3) + c*sqrt(57) + d)/128
               with a,b,c,d integers in [-100, 100].
               This is the *advertised* combinatorial pool that produces
               the observed identity.

    Family B   (the "generic radical-triple" family):
               F(a,b,c,d; p,q,r) = (a*sqrt(p) + b*sqrt(q) + c*sqrt(r) + d)/D
               with (p,q,r) any unordered triple drawn from
               {1,2,3,5,7,11,13,17,19,57}, D in {64, 128, 256}, and
               a,b,c,d in [-100, 100].
               This is the LEE-corrected pool: it accounts for the fact
               that a referee will say "you chose those radicals after
               seeing the answer".

    Family C   (the dV-deterministic family, zero free parameters):
               Once the dV quadratic, the (3/8) ratio, and the slot
               assignment are fixed, there is *no* tuning. The
               combinatorial weight is 1.

Outputs are written both to stdout and (as a clean markdown table) to
``look_elsewhere_results.md`` alongside this file.
"""

from __future__ import annotations

import math
import os
import time
from dataclasses import dataclass
from typing import Iterable

import numpy as np


# ---------------------------------------------------------------------------
# Target
# ---------------------------------------------------------------------------

M_H_PDG = 125.20      # GeV (PDG central value, m_h pole)
M_Z_PDG = 91.1876     # GeV (PDG central value, M_Z pole)
TARGET = (M_H_PDG / M_Z_PDG) ** 2          # 1.88508...

TOL = 1.0e-5  # absolute tolerance on the dimensionless ratio


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def count_matches_fixed_radicals(
    radicals: tuple[int, int, int],
    denom: int,
    coeff_range: range,
) -> tuple[int, int, list[tuple[int, int, int, int, float]]]:
    """Count integer tuples (a,b,c,d) in coeff_range^4 such that

        |(a*sqrt(p) + b*sqrt(q) + c*sqrt(r) + d)/denom  -  TARGET| < TOL

    Returns (n_matches, n_total, examples) where examples is at most a
    short list of (a,b,c,d,value) tuples for sanity-checking.
    """
    p, q, r = radicals
    sp = math.sqrt(p)
    sq = math.sqrt(q)
    sr = math.sqrt(r)

    coeffs = np.array(list(coeff_range), dtype=np.float64)
    # We vectorise as: target_d = denom*TARGET - a*sp - b*sq - c*sr
    # and check if any integer d in coeff_range matches within denom*TOL.
    n_match = 0
    examples: list[tuple[int, int, int, int, float]] = []
    d_min, d_max = coeff_range.start, coeff_range.stop - 1
    target_scaled = denom * TARGET
    tol_scaled = denom * TOL

    # 3-deep loop over (a,b,c), vectorised over c.
    for a in coeffs:
        for b in coeffs:
            # vector over c
            partial = a * sp + b * sq + coeffs * sr
            d_wanted = target_scaled - partial          # shape (Nc,)
            # closest integer in [d_min, d_max]
            d_int = np.rint(d_wanted).astype(np.int64)
            in_range = (d_int >= d_min) & (d_int <= d_max)
            err = np.abs(d_wanted - d_int)
            ok = in_range & (err < tol_scaled)
            n_ok = int(ok.sum())
            if n_ok:
                n_match += n_ok
                if len(examples) < 8:
                    idx = np.where(ok)[0]
                    for j in idx[: 8 - len(examples)]:
                        c_val = int(coeffs[j])
                        d_val = int(d_int[j])
                        val = (a * sp + b * sq + c_val * sr + d_val) / denom
                        examples.append((int(a), int(b), c_val, d_val, val))
    n_total = len(coeffs) ** 4
    return n_match, n_total, examples


def all_unordered_triples(pool: Iterable[int]) -> list[tuple[int, int, int]]:
    pool = sorted(set(pool))
    out: list[tuple[int, int, int]] = []
    n = len(pool)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                out.append((pool[i], pool[j], pool[k]))
    return out


# ---------------------------------------------------------------------------
# Family A — the narrow, advertised family
# ---------------------------------------------------------------------------

@dataclass
class FamilyResult:
    name: str
    n_match: int
    n_total: int
    p_chance: float
    examples: list[tuple[int, int, int, int, float]]
    notes: str = ""


def family_A(coeff_range: range) -> FamilyResult:
    n_match, n_total, ex = count_matches_fixed_radicals(
        radicals=(19, 3, 57), denom=128, coeff_range=coeff_range
    )
    return FamilyResult(
        name="A: (a√19 + b√3 + c√57 + d)/128",
        n_match=n_match,
        n_total=n_total,
        p_chance=n_match / n_total,
        examples=ex,
        notes="Radicals and denominator fixed by the dV construction.",
    )


# ---------------------------------------------------------------------------
# Family B — generic radical-triple sweep (the LEE-corrected pool)
# ---------------------------------------------------------------------------

def family_B(
    radical_pool: list[int],
    denominators: list[int],
    coeff_range: range,
) -> FamilyResult:
    triples = all_unordered_triples(radical_pool)
    n_match_total = 0
    n_total_total = 0
    examples: list[tuple[int, int, int, int, float]] = []
    per_config: list[tuple[tuple[int, int, int], int, int, int]] = []

    for trip in triples:
        for D in denominators:
            n_match, n_total, ex = count_matches_fixed_radicals(
                radicals=trip, denom=D, coeff_range=coeff_range
            )
            n_match_total += n_match
            n_total_total += n_total
            per_config.append((trip, D, n_match, n_total))
            if n_match and len(examples) < 12:
                for e in ex[: 12 - len(examples)]:
                    examples.append(e)

    notes_lines = [
        f"Pool of radicals: {radical_pool}",
        f"Denominators: {denominators}",
        f"#(unordered triples) = {len(triples)}",
        f"#(triple, denom) configs = {len(per_config)}",
    ]
    # Append a short per-config hit list
    hits = [pc for pc in per_config if pc[2] > 0]
    notes_lines.append(f"#(configs with at least one hit) = {len(hits)}")
    return FamilyResult(
        name="B: generic radical-triple sweep",
        n_match=n_match_total,
        n_total=n_total_total,
        p_chance=n_match_total / n_total_total,
        examples=examples,
        notes="\n".join(notes_lines),
    )


# ---------------------------------------------------------------------------
# Family C — the deterministic dV-only construction (no free parameters)
# ---------------------------------------------------------------------------

def family_C() -> FamilyResult:
    # Verify the identity numerically.
    val = (
        15 * math.sqrt(19)
        + 33 * math.sqrt(3)
        + 5 * math.sqrt(57)
        + 81
    ) / 128.0
    return FamilyResult(
        name="C: deterministic dV construction",
        n_match=1,
        n_total=1,
        p_chance=1.0,
        examples=[(15, 33, 5, 81, val)],
        notes=(
            "Zero free parameters once the dV quadratic, the slot "
            "assignment {M_Z^2,M_W^2,-m_h^2,-v^2/2}, and the (3/8)σ_3 "
            "ansatz are accepted. Combinatorial weight = 1."
        ),
    )


# ---------------------------------------------------------------------------
# Bayesian framing
# ---------------------------------------------------------------------------

def bayes_factor(
    p_match_given_dv: float,
    p_match_given_random: float,
) -> float:
    """Bayes factor K = P(data|H_dV) / P(data|H_random)."""
    if p_match_given_random <= 0:
        return float("inf")
    return p_match_given_dv / p_match_given_random


# ---------------------------------------------------------------------------
# Markdown writer
# ---------------------------------------------------------------------------

def write_markdown(
    out_path: str,
    famA: FamilyResult,
    famB: FamilyResult,
    famC: FamilyResult,
    elapsed: float,
    coeff_range: range,
) -> None:
    lo, hi = coeff_range.start, coeff_range.stop - 1
    K = bayes_factor(famC.p_chance, famB.p_chance)

    with open(out_path, "w") as f:
        f.write("# Look-elsewhere / chance-probability analysis\n\n")
        f.write(
            "Target ratio: "
            f"$m_h^2/M_Z^2 = (125.20/91.1876)^2 = {TARGET:.8f}$, "
            f"tolerance $10^{{-5}}$.\n\n"
        )
        f.write(
            "All families count integer-coefficient closed forms of the "
            f"shape $(a\\sqrt p + b\\sqrt q + c\\sqrt r + d)/D$ with "
            f"$a,b,c,d \\in [{lo},{hi}]$.\n\n"
        )

        f.write("## Summary table\n\n")
        f.write(
            "| Family | #matches | #candidates | p_chance | comment |\n"
        )
        f.write(
            "|---|---:|---:|---:|---|\n"
        )
        for fam in (famA, famB, famC):
            short_note = fam.notes.split("\n")[0]
            f.write(
                f"| {fam.name} | {fam.n_match:,} | {fam.n_total:,} | "
                f"{fam.p_chance:.3e} | {short_note} |\n"
            )
        f.write("\n")

        f.write("## Bayesian framing\n\n")
        f.write(
            "Let $H_{\\rm dV}$ be the hypothesis that the dV-Casimir "
            "construction is the correct algebraic skeleton, and "
            "$H_{\\rm rand}$ the null hypothesis that the identity is "
            "a numerical coincidence drawn from the generic pool of "
            "comparable closed forms.\n\n"
        )
        f.write(
            f"- $P(\\text{{match}}\\,|\\,H_{{\\rm dV}}) = "
            f"{famC.p_chance:.3e}$  (the construction predicts the "
            "identity with no tuning)\n"
        )
        f.write(
            f"- $P(\\text{{match}}\\,|\\,H_{{\\rm rand}}) = "
            f"{famB.p_chance:.3e}$  (generic radical-triple pool, "
            "Family B)\n"
        )
        f.write(
            "- Bayes factor "
            f"$K = P(\\text{{match}}\\,|\\,H_{{\\rm dV}}) / "
            f"P(\\text{{match}}\\,|\\,H_{{\\rm rand}}) "
            f"\\approx {K:.3e}$\n\n"
        )

        f.write("## Per-family details\n\n")
        for fam in (famA, famB, famC):
            f.write(f"### {fam.name}\n\n")
            f.write(f"- matches within $10^{{-5}}$: {fam.n_match:,}\n")
            f.write(f"- total candidates: {fam.n_total:,}\n")
            f.write(f"- chance probability: {fam.p_chance:.6e}\n")
            if fam.notes:
                f.write("- notes:\n\n")
                for line in fam.notes.split("\n"):
                    f.write(f"    - {line}\n")
            if fam.examples:
                f.write("\n  Sample matches (a, b, c, d → value):\n\n")
                for a, b, c, d, v in fam.examples[:8]:
                    f.write(
                        f"    - ({a:+d}, {b:+d}, {c:+d}, {d:+d}) "
                        f"→ {v:.8f}\n"
                    )
            f.write("\n")

        f.write("## Bottom line\n\n")
        p = famB.p_chance
        if p > 1e-3:
            verdict = (
                "**unsurprising** — a generic closed form of comparable "
                "complexity hits the target with probability "
                f"$\\sim {p:.2e}$, well above the $10^{{-3}}$ threshold."
            )
        elif p < 1e-5:
            verdict = (
                "**significant** — a generic closed form of comparable "
                "complexity hits the target with probability "
                f"$\\sim {p:.2e}$, below the $10^{{-5}}$ threshold."
            )
        else:
            verdict = (
                "**borderline** — a generic closed form of comparable "
                "complexity hits the target with probability "
                f"$\\sim {p:.2e}$, between $10^{{-5}}$ and $10^{{-3}}$. "
                "Marginal evidence that the identity is more than "
                "numerology."
            )
        f.write(verdict + "\n\n")
        f.write(
            "Important caveat: this is the *post-LEE* chance probability "
            "if one allows the analyst to scan radical triples, "
            "denominators, and coefficients. The dV construction "
            "itself has no such freedom — once accepted, its "
            "combinatorial weight is 1 (Family C). The Bayes factor "
            "above quantifies the asymmetry.\n\n"
        )
        f.write(
            f"Total wall time: {elapsed:.1f} s.\n"
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    # The full -100..100 sweep would be 201^4 ≈ 1.6e9 candidates per
    # (triple,denom) configuration, times ~660 configurations in
    # Family B → ~1e12 evaluations.  We use a tighter range that still
    # contains the dV coefficients {15, 33, 5, 81} comfortably.  -50..50
    # has 101^4 ≈ 1.04e8 per config and is fully tractable.
    #
    # The chance probability is reported as a *density*
    # (n_match / n_total), so the conclusion is independent of the box
    # size as long as the box is much wider than the typical scale of
    # the coefficients and the density has converged.
    coeff_range = range(-50, 51)

    print(f"Target m_h^2/M_Z^2 = {TARGET:.10f}")
    print(f"Tolerance         = {TOL}")
    print(f"Coefficient box   = [{coeff_range.start}, "
          f"{coeff_range.stop - 1}]^4 "
          f"= {len(list(coeff_range))**4:,} per (triple, denom)")
    print()

    t0 = time.time()

    print("Scanning Family A (fixed radicals √19,√3,√57; D=128)...")
    famA = family_A(coeff_range)
    print(f"  matches: {famA.n_match:,} / {famA.n_total:,} "
          f"=> p = {famA.p_chance:.3e}")
    print()

    radical_pool = [1, 2, 3, 5, 7, 11, 13, 17, 19, 57]
    denominators = [64, 128, 256]
    print(f"Scanning Family B (radical pool {radical_pool}, "
          f"denominators {denominators})...")
    famB = family_B(radical_pool, denominators, coeff_range)
    print(f"  matches: {famB.n_match:,} / {famB.n_total:,} "
          f"=> p = {famB.p_chance:.3e}")
    print()

    famC = family_C()
    print(f"Family C (deterministic dV): p = {famC.p_chance}")
    print()

    elapsed = time.time() - t0

    K = bayes_factor(famC.p_chance, famB.p_chance)
    print("Bayes factor (dV vs random numerology) K = "
          f"{K:.3e}")
    print()

    out_path = os.path.join(
        os.path.dirname(__file__), "look_elsewhere_results.md"
    )
    write_markdown(out_path, famA, famB, famC, elapsed, coeff_range)
    print(f"Wrote {out_path}")
    print(f"Wall time: {elapsed:.1f} s")


if __name__ == "__main__":
    main()
