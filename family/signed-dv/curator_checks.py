#!/usr/bin/env python3
"""Curator checks for physres5/family/signed-dv/SUMMARY.md.

Recomputes the numbers that SUMMARY.md cites beyond what the two source
projects print:

  1. exact identities (Vieta, F_dyn factorization, rapidity form);
  2. the Pauli-form matrix of draft/fused_manuscript.tex, eq. (pauli);
  3. Table 1 of the fused manuscript (ratio x M_Z);
  4. the FCC-ee "N sigma" figures quoted in README / EXECUTIVE_SUMMARY /
     the manuscript conclusion;
  5. which Higgs-mass input the manuscript's derived numbers use;
  6. the sign of the spurion rule, eq. (spurion);
  7. the kappa needed per negative slot, anchored on the Breit-Wigner M_Z
     used by the projects and on the complex-pole M_Z used by physres5;
  8. the alpha-endpoint arithmetic for the (s=1,-) <-> v/sqrt(2) reading;
  9. a recount of look_elsewhere.py Families A and B with an exact
     integer-window count, at the original 1e-5 window, at the dV formula's
     own residual, and at the 1-sigma experimental window on m_H^2/M_Z^2.

Run: python3 curator_checks.py   (numpy, scipy, sympy; about 20 s; writes nothing)
"""

from __future__ import annotations

import math

import numpy as np
import sympy as sp
from scipy.optimize import least_squares

# ---------------------------------------------------------------------------
# Inputs (GeV).  Breit-Wigner (running-width) masses unless marked "pole".
# ---------------------------------------------------------------------------
MW_PDG24, dMW_PDG24 = 80.3692, 0.0133
MZ_PDG24, dMZ_PDG24 = 91.1880, 0.0020
MH_PDG24, dMH_PDG24 = 125.20, 0.11
MH_NOTEOPUS, dMH_NOTEOPUS = 125.25, 0.17      # value used by the noteOpus spine
MW_LIVE26, dMW_LIVE26 = 80.3625, 0.0077
MZ_LIVE26 = 91.1879
MH_LIVE26 = 125.13
MW_ATLAS24 = 80.3665                          # "ATLAS central" quoted in README
MZ_PROJECT = 91.1876                          # anchor used by the project scripts
MZ_POLE_PHYSRES5 = 91.1538                    # physres5 Sec. 3 complex-pole M_Z
MW_POLE_PHYSRES5 = 80.3407                    # physres5 Sec. 3 complex-pole M_W
GF = 1.1663788e-5                             # GeV^-2
VR2 = 1.0 / math.sqrt(2.0 * math.sqrt(2.0) * GF)   # v/sqrt(2) = 174.10358


def xp(J: float) -> float:
    return (math.sqrt(J * J + 4 * J) - J) / 2


def xm(J: float) -> float:
    return -(math.sqrt(J * J + 4 * J) + J) / 2


XW, XZ, XH, XF = xp(0.75), xp(2.0), xm(0.75), xm(2.0)
GAP = XZ - XW                                 # (M_Z^2 - M_W0^2)/mu^2
DV_MH_RATIO = (15 * math.sqrt(19) + 33 * math.sqrt(3) + 5 * math.sqrt(57) + 81) / 128


def header(title: str) -> None:
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


def exact_identities() -> None:
    header("1. Exact identities")
    J, x = sp.symbols("J x", positive=True)
    xps = (sp.sqrt(J**2 + 4 * J) - J) / 2
    xms = -(sp.sqrt(J**2 + 4 * J) + J) / 2
    print("x+ + x- + J           =", sp.simplify(xps + xms + J))
    print("x+ * x- + J           =", sp.simplify(sp.expand(xps * xms) + J))
    print("x- + x+/(1 - x+)      =", sp.simplify(xms + xps / (1 - xps)))
    fdyn = (sp.sqrt(1 + 4 / sp.Rational(3, 4)) - 1) / (sp.sqrt(1 + sp.Integer(4) / 2) - 1)
    lhs = xps.subs(J, sp.Rational(3, 4)) / xps.subs(J, 2)
    print("cos2_dV - (3/8) F_dyn =", sp.nsimplify(sp.simplify(lhs - sp.Rational(3, 8) * fdyn)))
    print(f"sin2_dV = {1 - XW / XZ:.8f};  M_W/M_Z = {math.sqrt(XW / XZ):.6f}")
    print("signed trace ratio    =", sp.nsimplify((XW + XH) / (XZ + XF)),
          "; determinant ratio =", sp.nsimplify((XW * XH) / (XZ * XF)))


def pauli_form() -> None:
    header("2. Fused manuscript eq. (pauli): M^2 = s+ C1C2 + s- 1 + (1-sz)/2 C2")
    m, J, lam = sp.symbols("m J lambda", positive=True)
    c1, c2 = m**2, -m**2 * J
    printed = sp.Matrix([[0, c1 * c2], [1, c2]])
    print("char. poly of printed matrix :", sp.expand(printed.charpoly(lam).as_expr()))
    print("quartic M^4 - M^2 C2 + C1 C2 :", sp.expand(lam**2 - c2 * lam + c1 * c2))
    q = sp.Matrix([[0, sp.sqrt(J)], [sp.sqrt(J), -J]])
    print("physres5 Q(J) (units mu^2)   :", sp.expand(q.charpoly(lam).as_expr()))


def table_one() -> None:
    header("3. Fused manuscript Table 1 (ratio x M_Z, M_Z = 91.1880)")
    printed = {"(1/2,+)": 80.3724, "(1,-)": 176.1602, "(1/2,-)": 122.3879}
    ratios = {"(1/2,+)": math.sqrt(XW / XZ), "(1,-)": math.sqrt(-XF / XZ),
              "(1/2,-)": math.sqrt(-XH / XZ)}
    for slot, r in ratios.items():
        val = r * MZ_PDG24
        print(f"{slot:8s} ratio={r:.6f}  ratio*M_Z={val:.4f}  printed={printed[slot]:.4f}"
              f"  diff={1000 * (printed[slot] - val):+.1f} MeV")


def fcc_ee() -> None:
    header("4. Offset of the dV M_W from reference central values")
    for mz in (MZ_PROJECT, MZ_PDG24):
        mw = mz * math.sqrt(XW / XZ)
        for ref, name in ((MW_ATLAS24, "ATLAS 2024"), (MW_PDG24, "PDG 2024"),
                          (MW_LIVE26, "PDG-Live 2026")):
            d = 1000 * (mw - ref)
            print(f"M_Z={mz}: M_W(dV)={mw:.4f}  vs {name:13s} {ref}: {d:5.2f} MeV"
                  f" = {d:4.1f} sigma at 1 MeV, {2 * d:4.1f} sigma at 0.5 MeV")


def fit_m_beta(mh: float, dmh: float, mw: float, dmw: float, mz: float) -> tuple[float, float, float]:
    obs = np.array([mw, mz, VR2, mh])
    err = np.array([dmw, dMZ_PDG24, 0.0015, dmh])

    def model(p: np.ndarray) -> np.ndarray:
        m, b = p
        return np.array([m * math.sqrt(XW), m * math.sqrt(XZ),
                         m * math.sqrt(-XF - b), m * math.sqrt(-XH + b)])

    res = least_squares(lambda p: (model(p) - obs) / err, x0=[106.5, 0.06])
    return float(res.x[0]), float(res.x[1]), float(np.sum(res.fun**2))


def higgs_input_dependence() -> None:
    header("5. Derived numbers versus the Higgs-mass input")
    m_gauge = math.sqrt((MW_PDG24 / math.sqrt(XW)) * (MZ_PDG24 / math.sqrt(XZ)))
    m_fit = 106.578
    pred_trace = (-XH - XF) * m_fit**2
    for mh, dmh, lab in ((MH_NOTEOPUS, dMH_NOTEOPUS, "125.25(17) noteOpus"),
                         (MH_PDG24, dMH_PDG24, "125.20(11) PDG 2024"),
                         (MH_LIVE26, dMH_PDG24, "125.13(11) PDG-Live 2026")):
        obs_trace = VR2**2 + mh**2
        slot = mh / math.sqrt(-XH)
        resid = mh**2 - (-XH) * m_fit**2
        print(f"m_H={lab:24s}: m_H-slot scale={slot:.3f}+-{dmh / math.sqrt(-XH):.3f}"
              f"  trace mismatch={100 * (pred_trace - obs_trace) / obs_trace:.4f}%"
              f"  delta(m_H^2)={resid:+.1f} GeV^2")
    print(f"(m_gauge from PDG 2024 W and Z = {m_gauge:.4f} GeV; trace uses m = {m_fit})")
    for mh, dmh, mw, dmw, mz, lab in (
            (MH_NOTEOPUS, dMH_NOTEOPUS, MW_PDG24, dMW_PDG24, MZ_PDG24, "noteOpus m_H"),
            (MH_PDG24, dMH_PDG24, MW_PDG24, dMW_PDG24, MZ_PDG24, "PDG 2024"),
            (MH_LIVE26, dMH_PDG24, MW_LIVE26, dMW_LIVE26, MZ_LIVE26, "PDG-Live 2026")):
        m, b, chi2 = fit_m_beta(mh, dmh, mw, dmw, mz)
        print(f"(m, beta) refit, {lab:13s}: m={m:.4f} beta={b:.5f} chi2={chi2:.2f} for 2 dof")


def spurion_sign() -> None:
    header("6. Spurion rule M^2_{s,-} -> M^2_{s,-} + (-1)^(2s+1) beta m^2 (m=106.578, beta=0.0634)")
    m, beta = 106.578, 0.0634
    for s, x, table in ((0.5, XH, 125.30), (1.0, XF, 174.10)):
        sign = (-1) ** int(2 * s + 1)
        signed_rule = m * math.sqrt(-(x + sign * beta))
        magnitude_rule = m * math.sqrt(-x + sign * beta)
        print(f"s={s}: rule on signed M^2 -> {signed_rule:.2f} GeV;"
              f" rule on |M^2| -> {magnitude_rule:.2f} GeV; Table 2 prints {table}")


def kappa_by_anchor() -> None:
    header("7. kappa per negative slot, Breit-Wigner versus complex-pole M_Z anchor")
    for mz, mw, lab in ((MZ_LIVE26, MW_PDG24, "Breit-Wigner 91.1879"),
                        (MZ_POLE_PHYSRES5, MW_POLE_PHYSRES5, "complex pole 91.1538")):
        mu2 = mz**2 / XZ
        gap = GAP * mu2
        mh_k = math.sqrt((-XH + 0.375 * GAP) * mu2)
        mf_k = math.sqrt((-XF - 0.375 * GAP) * mu2)
        mw_dv = mz * math.sqrt(XW / XZ)
        print(f"anchor {lab}: mu={math.sqrt(mu2):.4f}; M_W(dV)={mw_dv:.4f} vs {mw}"
              f" ({1000 * (mw_dv - mw):+.1f} MeV)")
        print(f"   kappa=3/8 gives M_H={mh_k:.3f}, M_F={mf_k:.3f}"
              f" (v/sqrt2={VR2:.4f}, diff {1000 * (mf_k - VR2):+.1f} MeV)")
        for mh in (MH_PDG24, MH_LIVE26):
            k_h = (mh**2 + XH * mu2) / gap
            dk_h = 2 * mh * dMH_PDG24 / gap
            k_f = (-XF * mu2 - VR2**2) / gap
            trace = VR2**2 + mh**2 - (-XH - XF) * mu2
            print(f"   m_H={mh}: kappa_H={k_h:.4f}+-{dk_h:.4f}  kappa_F={k_f:.4f}"
                  f"  sum-rule residual={trace:+.1f} GeV^2 = {trace / (2 * mh * dMH_PDG24):+.2f} sigma(m_H^2)")


def alpha_endpoint() -> None:
    header("8. alpha endpoint: (s=1,-) <-> v/sqrt2 with M_W^2 = g^2 v^2/4")
    s2 = 1 - XW / XZ
    g2_bare = 2 * XW / (-XF)
    g2_corr = 2 * XW / (-XF - 0.375 * GAP)
    s2_os = 1 - MW_PDG24**2 / MZ_PDG24**2
    alpha_gmu = math.sqrt(2) * GF * MW_PDG24**2 * s2_os / math.pi
    print(f"1/alpha, uncorrected slot     = {4 * math.pi / (g2_bare * s2):.3f}")
    print(f"1/alpha, kappa = 3/8 slot     = {4 * math.pi / (g2_corr * s2):.3f}")
    print(f"1/alpha_Gmu (PDG 2024 W, Z)   = {1 / alpha_gmu:.3f}")


# ---------------------------------------------------------------------------
# 9. Look-elsewhere recount
# ---------------------------------------------------------------------------
COEFFS = np.arange(-50, 51, dtype=np.float64)


def count_window(radicals: tuple[int, int, int], denom: int, target: float, tol: float) -> int:
    """Count integer (a,b,c,d) in [-50,50]^4 with |(a sp + b sq + c sr + d)/D - T| <= tol."""
    sp_, sq_, sr_ = (math.sqrt(r) for r in radicals)
    bb, cc = np.meshgrid(COEFFS, COEFFS, indexing="ij")
    base = bb * sq_ + cc * sr_
    n = 0
    for a in COEFFS:
        partial = a * sp_ + base
        lo = np.maximum(np.ceil(denom * (target - tol) - partial), -50)
        hi = np.minimum(np.floor(denom * (target + tol) - partial), 50)
        n += int(np.clip(hi - lo + 1, 0, None).sum())
    return n


def unordered_triples(pool: list[int]) -> list[tuple[int, int, int]]:
    pool = sorted(set(pool))
    return [(pool[i], pool[j], pool[k]) for i in range(len(pool))
            for j in range(i, len(pool)) for k in range(j, len(pool))]


def lee_recount() -> None:
    header("9. look_elsewhere.py Families A and B, exact integer-window recount")
    target = (MH_PDG24 / MZ_PROJECT) ** 2
    residual = abs(DV_MH_RATIO - target)
    one_sigma = 2 * target * dMH_PDG24 / MH_PDG24
    print(f"target (125.20/91.1876)^2 = {target:.8f}; dV closed form = {DV_MH_RATIO:.8f};"
          f" |dV - target| = {residual:.2e}")
    n_box = 101**4
    triples = unordered_triples([1, 2, 3, 5, 7, 11, 13, 17, 19, 57])
    for tol, lab in ((1.0e-5, "original window 1e-5"),
                     (residual, "window = dV residual"),
                     (one_sigma, "window = 1 sigma of m_H^2/M_Z^2")):
        n_a = count_window((19, 3, 57), 128, target, tol)
        n_b = sum(count_window(t, d, target, tol) for t in triples for d in (64, 128, 256))
        print(f"{lab:32s} tol={tol:.3e}: A = {n_a / n_box:.3e}   B = {n_b / (n_box * 660):.3e}"
              f"   (1/B = {n_box * 660 / n_b:.2e})")


def main() -> None:
    exact_identities()
    pauli_form()
    table_one()
    fcc_ee()
    higgs_input_dependence()
    spurion_sign()
    kappa_by_anchor()
    alpha_endpoint()
    lee_recount()


if __name__ == "__main__":
    main()
