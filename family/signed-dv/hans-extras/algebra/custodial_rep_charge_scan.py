#!/usr/bin/env python3
"""Scan custodial SU(2)_R charges Y = T_R^3 + X for Y=3/8."""

from __future__ import annotations

import sympy as sp


def magnetic_weights(j: sp.Rational) -> list[sp.Rational]:
    two_j = int(2 * j)
    return [sp.Rational(-two_j + 2 * k, 2) for k in range(two_j + 1)]


def main() -> None:
    target = sp.Rational(3, 8)
    x_unit = sp.Rational(1, 6)
    print("Custodial SU(2)_R + X charge scan")
    print("----------------------------------")
    print("Hypercharge embedding: Y = T_R^3 + X")
    print(f"Target Y = {sp.sstr(target)}")
    print(f"Assumed ordinary X lattice unit = {sp.sstr(x_unit)}")
    print()

    hits = []
    for two_j in range(0, 9):
        j = sp.Rational(two_j, 2)
        for m in magnetic_weights(j):
            x_needed = sp.simplify(target - m)
            on_lattice = (x_needed / x_unit).is_integer
            if on_lattice:
                hits.append((j, m, x_needed))
            print(
                f"j_R={sp.sstr(j):>3}, T_R^3={sp.sstr(m):>4}: "
                f"X_needed={sp.sstr(x_needed):>6}, "
                f"on 1/6 lattice={on_lattice}"
            )

    print()
    if hits:
        print("Hits:")
        for j, m, x in hits:
            print(f"  j_R={sp.sstr(j)}, T_R^3={sp.sstr(m)}, X={sp.sstr(x)}")
    else:
        print("No hits through j_R=4.")
    print()

    print("Reason")
    print("------")
    print("T_R^3 weights are integer or half-integer.  Subtracting them from")
    print("3/8 leaves a number whose ratio to 1/6 is a quarter-integer, not")
    print("an integer.  Thus ordinary X quantization does not produce Y=3/8.")


if __name__ == "__main__":
    main()
