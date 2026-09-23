#!/usr/bin/env python3
"""Paired exotic-scalar D-term model for a traceless hypercharge split."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    q_h, q_s, gp, v = sp.symbols("q_h q_s gprime v", positive=True)
    gap = gp**2 * v**2 / 4

    delta_plus = gp**2 * q_h * q_s * v**2 / 2
    delta_minus = -delta_plus
    kappa = sp.simplify(delta_plus / gap)
    q_needed = sp.solve(sp.Eq(kappa.subs(q_h, sp.Rational(1, 2)), sp.Rational(3, 8)), q_s)[0]

    print("Paired scalar D-term model")
    print("--------------------------")
    print("V_D = g'^2/2 (q_H |H|^2 + q_S |S_+|^2 - q_S |S_-|^2)^2")
    print(f"delta m_+^2 = {sp.sstr(delta_plus)}")
    print(f"delta m_-^2 = {sp.sstr(delta_minus)}")
    print(f"trace shift = {sp.sstr(sp.simplify(delta_plus + delta_minus))}")
    print(f"kappa = delta m_+^2/(M_Z^2-M_W^2) = {sp.sstr(kappa)}")
    print(f"With q_H=1/2, kappa = {sp.sstr(kappa.subs(q_h, sp.Rational(1, 2)))}")
    print(f"q_S needed for kappa=3/8: {sp.sstr(q_needed)}")
    print()

    print("Anomaly and charge comments")
    print("---------------------------")
    print("Scalars do not generate gauge anomalies.")
    print("A vectorlike chiral-fermion pair with Y=+q_S and -q_S also cancels")
    print("U(1)_Y^3 and gravitational-U(1)_Y anomalies.")
    print("For SU(2)_L singlet scalars, electric charges are Q=Y=+/-3/8.")
    print("For SU(2)_L doublets, component charges are Y+/-1/2:")
    print(f"  Y=+3/8 doublet: Q = {sp.Rational(3, 8)+sp.Rational(1, 2)}, {sp.Rational(3, 8)-sp.Rational(1, 2)}")
    print(f"  Y=-3/8 doublet: Q = {-sp.Rational(3, 8)+sp.Rational(1, 2)}, {-sp.Rational(3, 8)-sp.Rational(1, 2)}")
    print()

    print("Conclusion")
    print("----------")
    print(
        "This is a genuine Lagrangian way to get a traceless split proportional "
        "to M_Z^2-M_W^2, but the coefficient is q_S.  Setting q_S=3/8 is a "
        "hypercharge assignment, not a derivation from C_F/C_A."
    )


if __name__ == "__main__":
    main()
