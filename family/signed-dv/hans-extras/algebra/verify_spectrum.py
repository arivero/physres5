#!/usr/bin/env python3
"""Exact checks for the signed de Broglie-de Vries spectrum.

The script keeps the algebra exact in SymPy and only evaluates numerically at
the end.  It is intentionally small enough to audit by eye.
"""

from __future__ import annotations

import sympy as sp


def casimir(s: sp.Rational) -> sp.Expr:
    return sp.simplify(s * (s + 1))


def roots_for_spin(s: sp.Rational) -> tuple[sp.Expr, sp.Expr]:
    C = casimir(s)
    x = sp.symbols("x")
    roots = sp.solve(x**2 + C * x - C, x)
    roots = sorted([sp.radsimp(r) for r in roots], key=lambda r: float(r))
    return roots[1], roots[0]


def main() -> None:
    sqrt = sp.sqrt
    sA = sp.Rational(1, 1)
    sF = sp.Rational(1, 2)
    CA = casimir(sA)
    CF = casimir(sF)
    k = sp.simplify(CF / CA)

    xZ, xFminus = roots_for_spin(sA)
    xW, xHminus = roots_for_spin(sF)

    expected = {
        "x_1,+": sqrt(3) - 1,
        "x_1,-": -(sqrt(3) + 1),
        "x_1/2,+": (sqrt(57) - 3) / 8,
        "x_1/2,-": -(sqrt(57) + 3) / 8,
    }

    assert sp.simplify(xZ - expected["x_1,+"]) == 0
    assert sp.simplify(xFminus - expected["x_1,-"]) == 0
    assert sp.simplify(xW - expected["x_1/2,+"]) == 0
    assert sp.simplify(xHminus - expected["x_1/2,-"]) == 0

    trace_ratio = sp.simplify((xW + xHminus) / (xZ + xFminus))
    det_ratio = sp.simplify((xW * (-xHminus)) / (xZ * (-xFminus)))
    assert trace_ratio == k
    assert det_ratio == k

    sin2_positive = sp.radsimp(1 - xW / xZ)
    cos2_positive = sp.radsimp(xW / xZ)

    delta = sp.simplify(k * (xZ - xW))
    xH0_abs = -xHminus
    xF0_abs = -xFminus
    xH_corr_abs = sp.radsimp(xH0_abs + delta)
    xF_corr_abs = sp.radsimp(xF0_abs - delta)

    assert sp.simplify(xH_corr_abs - (5 * sqrt(57) + 24 * sqrt(3) + 9) / 64) == 0
    assert sp.simplify(xF_corr_abs - (40 * sqrt(3) + 3 * sqrt(57) + 79) / 64) == 0
    assert sp.simplify((xH_corr_abs + xF_corr_abs) - (xH0_abs + xF0_abs)) == 0

    MH_ratio = sp.radsimp(xH_corr_abs / xZ)
    MF_ratio = sp.radsimp(xF_corr_abs / xZ)

    # The historical de Broglie-de Vries comparison uses this fixed M_Z input.
    MZ = sp.Float("91.1876")
    Mcal = MZ / sp.sqrt(xZ)
    MW0 = Mcal * sp.sqrt(xW)
    MH0 = Mcal * sp.sqrt(xH0_abs)
    MF0 = Mcal * sp.sqrt(xF0_abs)
    MH = Mcal * sp.sqrt(xH_corr_abs)
    MF = Mcal * sp.sqrt(xF_corr_abs)

    GF = sp.Float("1.1663788e-5")
    v_over_sqrt2 = 1 / sp.sqrt(2 * sp.sqrt(2) * GF)

    print("Casimirs")
    print(f"  C_A = {CA}")
    print(f"  C_F = {CF}")
    print(f"  C_F/C_A = {k}")
    print()
    print("Exact roots")
    for name, value in expected.items():
        print(f"  {name} = {value}")
    print()
    print("Exact identities")
    print(f"  trace ratio      = {trace_ratio}")
    print(f"  determinant ratio= {det_ratio}")
    print(f"  sin^2 theta_W,+  = {sin2_positive}")
    print(f"  cos^2 theta_W,+  = {cos2_positive}")
    print()
    print("Corrected negative-sector exact forms")
    print(f"  delta/Mcal^2 = {sp.radsimp(delta)}")
    print(f"  M_H^2/Mcal^2 = {xH_corr_abs}")
    print(f"  M_F^2/Mcal^2 = {xF_corr_abs}")
    print(f"  M_H^2/M_Z^2  = {MH_ratio}")
    print(f"  M_F^2/M_Z^2  = {MF_ratio}")
    print()
    print("Numerics for M_Z = 91.1876 GeV")
    print(f"  Mcal = {Mcal.evalf(12)} GeV")
    print(f"  M_W0 = {MW0.evalf(12)} GeV")
    print(f"  M_H0 = {MH0.evalf(12)} GeV")
    print(f"  M_F0 = {MF0.evalf(12)} GeV")
    print(f"  M_H  = {MH.evalf(12)} GeV")
    print(f"  M_F  = {MF.evalf(12)} GeV")
    print(f"  v/sqrt(2) from G_F=1.1663788e-5 = {v_over_sqrt2.evalf(12)} GeV")


if __name__ == "__main__":
    main()
