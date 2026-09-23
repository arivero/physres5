#!/usr/bin/env python3
"""Match the proposed correction to a minimal negative-sector EFT operator.

This script asks a narrow question:

    If we add the cleanest gauge-invariant scalar mass operator whose
    coefficient is explicitly proportional to the hypercharge spurion g'^2,
    what Wilson coefficient is required to reproduce the 3/8 correction?

The answer is useful because it separates "allowed by EFT" from "derived by
group theory".  The matching coefficient is not fixed.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    kappa = sp.Rational(3, 8)
    gp, v, c_y = sp.symbols("gprime v c_Y", positive=True)

    vector_gap = gp**2 * v**2 / 4
    target_delta = sp.simplify(kappa * vector_gap)

    # Convention:
    #   V_eff contains 1/2 Psi^T [c_Y g'^2 (H^\dag H) sigma_3] Psi.
    # At <H^\dag H> = v^2/2, the mass-square splitting is
    #   Delta = c_Y g'^2 v^2/2.
    eft_delta = c_y * gp**2 * v**2 / 2
    c_solution = sp.solve(sp.Eq(eft_delta, target_delta), c_y)[0]

    # Compare to common one-generator normalizations.
    single_generator_eigenvalue = sp.Rational(1, 4)  # (T_R^3)^2 on a doublet
    dynkin_over_adjoint = sp.Rational(1, 4)          # T_F/C_A = (1/2)/2
    hypercharge_dterm = sp.Rational(1, 8)            # Y_H^2/2 for Y_H=1/2
    target_gprime_v_coeff = sp.simplify(target_delta / (gp**2 * v**2))

    print("Minimal negative-sector EFT matching")
    print("------------------------------------")
    print("Operator convention:")
    print("  V_eff contains 1/2 Psi^T [c_Y g'^2 (H^dag H) sigma_3] Psi")
    print("  <H^dag H> = v^2/2")
    print()
    print(f"M_Z^2 - M_W^2 = {vector_gap}")
    print(f"target Delta  = {target_delta}")
    print(f"EFT Delta     = {eft_delta}")
    print(f"required c_Y  = {c_solution}")
    print()
    print("One-generator / D-term comparison")
    print(f"  target coefficient of g'^2 v^2      = {target_gprime_v_coeff}")
    print(f"  (T_R^3)^2 on a doublet              = {single_generator_eigenvalue}")
    print(f"  T_F/C_A                             = {dynkin_over_adjoint}")
    print(f"  hypercharge D-term Y_H^2/2          = {hypercharge_dterm}")
    print(f"  target / hypercharge-D coefficient  = {sp.simplify(target_gprime_v_coeff / hypercharge_dterm)}")
    print()
    print("Conclusion")
    print("  The operator is gauge-invariant if Psi is an electroweak singlet")
    print("  or if it is embedded consistently in a larger scalar sector.")
    print("  Matching requires c_Y = 3/16.  That is a Wilson coefficient,")
    print("  not a value fixed by the SM gauge group or by custodial symmetry.")


if __name__ == "__main__":
    main()
