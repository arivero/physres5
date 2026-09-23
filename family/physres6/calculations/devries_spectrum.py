#!/usr/bin/env python3
"""DeVries two-branch spectrum and the parameter-free electroweak couplings.

Central result of the physres6 note:

  * positive branch  -> weak mixing angle  sin^2(theta) = 1 - x+(3/4)/x+(2)
  * negative branch  -> order parameter;   v = sqrt(2) * M-(J=2)
  * because M_W and v both scale with the single scale mu, the SU(2) coupling
    g = 2 M_W / v is mu-INDEPENDENT, so alpha = g^2 sin^2(theta)/(4 pi) is a
    pure number.

Only bare computed numbers are printed.  Reference/measured values are labelled
`ref` and are NOT outputs of the construction.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt


@dataclass(frozen=True)
class BranchValues:
    J: float
    x_plus: float
    x_minus: float


def roots_from_J(J: float) -> BranchValues:
    if J <= 0:
        raise ValueError("J must be positive")
    disc = sqrt(J * J + 4.0 * J)
    return BranchValues(J=J, x_plus=(disc - J) / 2.0, x_minus=-(disc + J) / 2.0)


def J_from_spin(s: float) -> float:
    if s <= 0:
        raise ValueError("spin label s must be positive")
    return s * (s + 1.0)


# --- dimensionless construction outputs (no scale, no measured input) ---------

def sin2_devries() -> float:
    w = roots_from_J(J_from_spin(0.5)).x_plus
    z = roots_from_J(J_from_spin(1.0)).x_plus
    return 1.0 - w / z


def g_squared() -> float:
    """SU(2) coupling^2 under v = sqrt(2) M-(J=2); mu cancels.

    g^2 = 4 M_W^2 / v^2 = 4 mu^2 x+(3/4) / (2 mu^2 |x-(2)|) = 2 x+(3/4)/|x-(2)|.
    """
    xp34 = roots_from_J(J_from_spin(0.5)).x_plus
    xm2 = roots_from_J(J_from_spin(1.0)).x_minus
    return 2.0 * xp34 / abs(xm2)


def inv_alpha_devries() -> float:
    return 4.0 * pi / (g_squared() * sin2_devries())


# --- scale-dependent spectrum (one scale mu, fixed by one mass) ---------------

def mu_from_mz(mz: float) -> float:
    return mz / sqrt(roots_from_J(J_from_spin(1.0)).x_plus)


def spectrum_from_mz(mz: float) -> dict[str, float]:
    mu = mu_from_mz(mz)
    w = roots_from_J(J_from_spin(0.5))
    z = roots_from_J(J_from_spin(1.0))
    Mminus2 = mu * sqrt(abs(z.x_minus))
    return {
        "mu": mu,
        "M_W (+,3/4)": mu * sqrt(w.x_plus),
        "M_Z (+,2)": mu * sqrt(z.x_plus),
        "M_-(3/4)": mu * sqrt(abs(w.x_minus)),
        "M_-(2)": Mminus2,
        "v = sqrt2*M_-(2)": sqrt(2.0) * Mminus2,
    }


def main() -> None:
    ref = {  # measured / reference, NOT construction outputs
        "M_Z": 91.1880, "M_W": 80.3692, "M_h": 125.20, "M_t": 172.57,
        "v": 246.22, "1/alpha(0)": 137.036, "1/alpha(MZ)": 127.95,
    }

    print("# dimensionless (no scale, no measured input)")
    print(f"sin2_theta = {sin2_devries():.6f}")
    print(f"g          = {sqrt(g_squared()):.6f}")
    print(f"1/alpha    = {inv_alpha_devries():.4f}")
    print()
    print("# spectrum with mu fixed by M_Z (ref values in parentheses)")
    s = spectrum_from_mz(ref["M_Z"])
    labels = {
        "mu": None, "M_W (+,3/4)": ref["M_W"], "M_Z (+,2)": ref["M_Z"],
        "M_-(3/4)": ref["M_h"], "M_-(2)": ref["M_t"], "v = sqrt2*M_-(2)": ref["v"],
    }
    for k, r in labels.items():
        tag = "" if r is None else f"   (ref {r})"
        print(f"{k:>18} = {s[k]:8.3f}{tag}")
    print()
    print("# higher positive-branch slots (parameter-free given mu)")
    mu = s["mu"]
    for spin, note in [(1.5, "~95 GeV diphoton excess; identity open (chiral 4/3?)"),
                       (2.0, None)]:
        M = mu * sqrt(roots_from_J(J_from_spin(spin)).x_plus)
        tag = "" if note is None else f"   ({note})"
        print(f"     M_+(s={spin}) = {M:8.3f}{tag}")


if __name__ == "__main__":
    main()
