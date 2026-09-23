#!/usr/bin/env python3
"""Check the relation between SU(5) hypercharge normalization and 3/8."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    y = sp.diag(
        -sp.Rational(1, 3),
        -sp.Rational(1, 3),
        -sp.Rational(1, 3),
        sp.Rational(1, 2),
        sp.Rational(1, 2),
    )
    tr_y2 = sp.trace(y * y)
    norm_sq = sp.Rational(1, 2) / tr_y2
    gprime_over_g1_sq = norm_sq
    sin2_unified = sp.simplify(gprime_over_g1_sq / (1 + gprime_over_g1_sq))

    cf_over_ca = sp.Rational(3, 4) / 2
    target_in_g1_units = sp.simplify(cf_over_ca * gprime_over_g1_sq / 4)

    print("SU(5) hypercharge normalization")
    print("--------------------------------")
    print("Y = diag(-1/3,-1/3,-1/3,1/2,1/2)")
    print(f"Tr_5(Y^2) = {sp.sstr(tr_y2)}")
    print(f"T_Y = sqrt({sp.sstr(norm_sq)}) Y gives Tr_5(T_Y^2)=1/2")
    print(f"g'^2/g_1^2 = {sp.sstr(gprime_over_g1_sq)}")
    print(f"sin^2(theta_W) at g_1=g_2 = {sp.sstr(sin2_unified)}")
    print()

    print("Comparison with the proposed correction")
    print("---------------------------------------")
    print(f"C_F/C_A for SU(2) = {sp.sstr(cf_over_ca)}")
    print(
        "epsilon = (C_F/C_A)(M_Z^2-M_W^2) "
        "= (3/8)(g'^2 v^2/4)"
    )
    print(
        "In SU(5)-normalized hypercharge units this is "
        f"epsilon = {sp.sstr(target_in_g1_units)} g_1^2 v^2"
    )
    print()
    print("Conclusion")
    print("----------")
    print(
        "The SU(5) value sin^2(theta_W)=3/8 is numerically identical to "
        "C_F/C_A for SU(2), but it is a different group-theory quotient: "
        "(3/5)/(1+3/5), not (3/4)/2.  It fixes a high-scale coupling "
        "normalization, not a low-energy negative-sector mass threshold."
    )


if __name__ == "__main__":
    main()
