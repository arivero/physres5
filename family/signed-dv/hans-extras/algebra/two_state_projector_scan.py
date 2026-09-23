#!/usr/bin/env python3
"""Two-state negative-sector projector checks.

The proposed correction is a traceless two-state perturbation,

    Delta M_-^2 = epsilon sigma_3,
    epsilon = (3/8)(M_Z^2 - M_W^2).

This script records two elementary obstructions to deriving it from only
custodial/hypercharge symmetry:

1. Any real traceless 2 x 2 perturbation can be diagonalized to sigma_3.
   The sigma_3 form is therefore not physical unless the root basis has an
   independently fixed meaning.
2. Hypercharge gauges a single SU(2)_R generator T_R^3.  At order g'^2 the
   single-generator invariant contains (T_R^3)^2, not the full SU(2) Casimir
   C_F = sum_a T^a T^a.  For a fundamental doublet this gives 1/4 rather than
   3/4 before any UV matching coefficient is introduced.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    a, b, c, theta = sp.symbols("a b c theta", real=True)

    one = sp.eye(2)
    sigma1 = sp.Matrix([[0, 1], [1, 0]])
    sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma3 = sp.Matrix([[1, 0], [0, -1]])

    perturbation = a * one + b * sigma3 + c * sigma1
    eigs = perturbation.eigenvals()

    rotation = sp.Matrix(
        [
            [sp.cos(theta), -sp.sin(theta)],
            [sp.sin(theta), sp.cos(theta)],
        ]
    )
    rotated_sigma3 = sp.simplify(rotation * sigma3 * rotation.T)

    t1 = sigma1 / 2
    t2 = sigma2 / 2
    t3 = sigma3 / 2
    cf_operator = sp.simplify(t1 * t1 + t2 * t2 + t3 * t3)
    t3_squared = sp.simplify(t3 * t3)

    # Spin-1 adjoint generators in the Cartesian basis:
    # (T^a_adj)_{bc} = -i epsilon_{abc}.
    t3_adj = sp.Matrix([[0, -sp.I, 0], [sp.I, 0, 0], [0, 0, 0]])
    t3_adj_sq = sp.simplify(t3_adj * t3_adj)

    print("Two-state perturbation")
    print("----------------------")
    print("Delta =")
    sp.print_latex(perturbation)
    print("eigenvalues:")
    for val, mult in eigs.items():
        print(f"  {sp.sstr(val)}  multiplicity {mult}")
    print(f"trace(Delta) = {sp.sstr(sp.trace(perturbation))}")
    print("trace preservation requires a = 0")
    print()

    print("Rotation of sigma_3")
    print("-------------------")
    print("R(theta) sigma_3 R(theta)^T =")
    print(sp.sstr(rotated_sigma3))
    print(
        "This spans cos(2 theta) sigma_3 + sin(2 theta) sigma_1, "
        "so a sigma_3 form is a mass-basis convention unless another "
        "structure fixes theta."
    )
    print()

    print("SU(2) generator normalizations")
    print("------------------------------")
    print(f"sum_a T_F^a T_F^a = {sp.sstr(cf_operator)}")
    print(f"C_F = {sp.sstr(cf_operator[0, 0])}")
    print(f"(T_F^3)^2 = {sp.sstr(t3_squared)}")
    print(f"(T_F^3)^2 / C_A = {sp.sstr(sp.Rational(1, 4) / 2)}")
    print(f"C_F / C_A = {sp.sstr(sp.Rational(3, 4) / 2)}")
    print(f"Tr_F[(T^3)^2] = {sp.sstr(sp.trace(t3_squared))}")
    print(f"T_adj^3 squared = {sp.sstr(t3_adj_sq)}")
    print(f"Tr_adj[(T^3)^2] = {sp.sstr(sp.trace(t3_adj_sq))}")
    print(
        "Single-generator trace ratio Tr_F[(T^3)^2]/Tr_adj[(T^3)^2] = "
        f"{sp.sstr(sp.trace(t3_squared) / sp.trace(t3_adj_sq))}"
    )
    print()
    print("Conclusion")
    print("----------")
    print(
        "The factor 3/8 is the full-fundamental/full-adjoint Casimir ratio. "
        "A hypercharge spurion by itself supplies only the selected generator "
        "T_R^3.  A UV model must therefore explain why the full C_F is restored "
        "in a custodial-breaking effect that otherwise knows about only T_R^3."
    )


if __name__ == "__main__":
    main()
