#!/usr/bin/env python3
"""Symbolic tests of simple deformations of P_s(x).

This is not a statistical scan.  It records which algebraic deformations can
preserve the positive branch while moving only the negative branch, and which
ones require an explicit projector or tuned on-shell subtraction.
"""

from __future__ import annotations

import sympy as sp


x, eta, chi, C0 = sp.symbols("x eta chi C0")
sqrt = sp.sqrt
C_A = sp.Rational(2)
C_F = sp.Rational(3, 4)
k = sp.Rational(3, 8)

xZ = sqrt(3) - 1
xFm = -(sqrt(3) + 1)
xW = (sqrt(57) - 3) / 8
xHm = -(sqrt(57) + 3) / 8
Delta = sp.radsimp(k * (xZ - xW))


def dx_dC(root: sp.Expr, C: sp.Expr) -> sp.Expr:
    return sp.radsimp((1 - root) / (2 * root + C))


def first_order_shift(root: sp.Expr, other: sp.Expr, perturbation: sp.Expr) -> sp.Expr:
    """For P=(x-root)(x-other), return first-order root shift from dP."""
    return sp.radsimp(-perturbation.subs(x, root) / (root - other))


def main() -> None:
    print("Target signed negative-root shifts")
    print(f"  epsilon_H signed = {-Delta}")
    print(f"  epsilon_F signed = {Delta}")
    print()

    print("1. Universal C -> C + eta deformation")
    print("   P = x^2 + (C+eta)x - (C+eta)")
    for label, C, rp, rm in [
        ("adjoint/s=1", C_A, xZ, xFm),
        ("fundamental/s=1/2", C_F, xW, xHm),
    ]:
        print(f"   {label}:")
        print(f"     d x_+ / d eta = {dx_dC(rp, C)}")
        print(f"     d x_- / d eta = {dx_dC(rm, C)}")
    print("   Verdict: any nonzero eta moves the positive branch.")
    print()

    print("2. Spin-dependent eta_s deformation")
    print("   P_s = x^2 + (C_s+eta_s)x - (C_s+eta_s)")
    print("   Verdict: eta_s can tune a negative shift only by also moving x_{s,+};")
    print("   imposing exact preservation of x_{s,+} forces eta_s = 0.")
    print()

    print("3. On-shell-subtracted deformation")
    lam = sp.symbols("lambda")
    P_sub = sp.expand((x - xW) * (x - xHm) + lam * (x - xW))
    print("   P -> P + lambda_s (x - x_{s,+})")
    print(f"   Example s=1/2 factorization: {sp.factor(P_sub)}")
    print("   Roots are x_{s,+} and x_{s,-}-lambda_s exactly.")
    print(f"   To shift H signed root by -Delta choose lambda_H = {Delta}.")
    print(f"   To shift F signed root by +Delta choose lambda_F = {-Delta}.")
    print("   Verdict: algebraically exact, but lambda_s is a Wilson coefficient.")
    print()

    print("4. General linear spurion dP = chi(a_s x + b_s)")
    a, b = sp.symbols("a b")
    dP = a * x + b
    pos_shift = first_order_shift(xW, xHm, dP)
    print(f"   First-order positive-root shift for s=1/2: {pos_shift}")
    print("   Setting b_s = -a_s x_{s,+} preserves x_{s,+}; this reduces to")
    print("   the on-shell-subtracted deformation and moves x_- by -chi a_s.")
    print("   Verdict: custodial spurion symmetry allows the form, not the coefficient.")
    print()

    print("5. Regge-intercept deformation")
    print("   If J = alpha_0 + alpha' M^2, an intercept shift gives")
    print("   delta M^2 = -delta alpha_0/alpha' for all states on that trajectory.")
    print("   Preserving only the positive roots requires branch-dependent intercepts")
    print("   or a projector onto the negative-root sector.")
    print()

    print("6. Two-parameter parent with a custodial limit")
    C_phys = {"A": C_A, "F": C_F}
    C_parent_A = C0 + chi * (C_phys["A"] - C0)
    C_parent_F = C0 + chi * (C_phys["F"] - C0)
    print("   C_s(chi) = C0 + chi(C_s^phys - C0)")
    print(f"   C_A(chi) = {C_parent_A}")
    print(f"   C_F(chi) = {C_parent_F}")
    print("   At chi=0 the positive roots are degenerate for any C0>0;")
    print("   at chi=1 the de Broglie-de Vries Casimirs are recovered.")
    print("   Verdict: a custodial limit can be engineered, but C0 and the")
    print("   interpolation are arbitrary and are not implied by SU(2) representation theory.")
    print()

    print("7. Matrix/operator deformation in signed-root space")
    print("   A projector P_- times sigma_3 gives exactly")
    print("   diag(0,0,-Delta,+Delta) on (W,Z,H_signed,F_signed).")
    print("   Verdict: mathematically clean; a field-theory derivation must explain")
    print("   why such a projector exists and why its Wilson coefficient is C_F/C_A.")


if __name__ == "__main__":
    main()
