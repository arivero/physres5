#!/usr/bin/env python3
"""Hidden-U(1) kinetic-mixing charge shift needed for an effective 3/8."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    target = sp.Rational(3, 8)
    eps, ratio, qx, q0 = sp.symbols("epsilon r q_X q_0", nonzero=True)
    q_eff = q0 + eps * ratio * qx

    print("Hidden-U(1) kinetic-mixing charge shift")
    print("---------------------------------------")
    print("Effective charge model: q_eff = q_0 + epsilon (g_X/g_Y) q_X")
    print(f"Target q_eff = {sp.sstr(target)}")
    print()

    examples = [
        ("neutral visible charge, unit dark charge", sp.Rational(0), sp.Rational(1)),
        ("nearest lower SM-lattice charge 1/3", sp.Rational(1, 3), sp.Rational(1)),
        ("nearest upper SM-lattice charge 1/2", sp.Rational(1, 2), sp.Rational(1)),
    ]

    for label, q0_value, qx_value in examples:
        needed = sp.solve(
            sp.Eq(q_eff.subs({q0: q0_value, qx: qx_value}), target),
            eps,
        )[0]
        print(label)
        print(f"  q_0={sp.sstr(q0_value)}, q_X={sp.sstr(qx_value)}")
        print(f"  epsilon needed = {sp.sstr(needed)}")
        print(f"  for g_X/g_Y=1: epsilon = {sp.sstr(needed.subs(ratio, 1))}")
        print()

    print("Conclusion")
    print("----------")
    print(
        "Kinetic mixing can generate an effective 3/8 charge, but only by "
        "choosing a continuous mixing parameter and charge normalization.  "
        "It evades the lattice obstruction by adding a new parameter; it does "
        "not derive C_F/C_A."
    )


if __name__ == "__main__":
    main()
