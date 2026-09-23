"""Scalar sector of the Casimir-locked bosonic-seesaw model.

Field content (chat sec. 1-2):
    For each SU(2)_L irrep R in {2, 3}, two scalars in the
    elementary/composite basis:

        Phi^d_e  Phi^d_c   (R = 2, doublet,  Y = 1/2)
        Phi^t_e  Phi^t_c   (R = 3, triplet,  Y = 0)

The Casimir-locked seed potential reads, in matrix notation,

    V_seed = m_0^2 * sum_R  [Phi^R_e^dag, Phi^R_c^dag] M^2_R/m_0^2 [Phi^R_e, Phi^R_c]^T

with the chat's Casimir-locked block

    M^2_R / m_0^2 = [[ 0,        sqrt(C2(R)) ],
                     [ sqrt(C2(R)), -C2(R)   ]].

Diagonalisation produces 2 real masses per irrep; the negative eigenvalue
in the doublet channel triggers EWSB through the standard Higgs mechanism
on the corresponding mass eigenstate.
"""

from __future__ import annotations

import sympy as sp

import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from algebra.seeds import C2, seed_matrix, seed_eigenvalues  # noqa: E402

# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------
m0sq = sp.symbols("m_0^2", positive=True)


def seed_potential_block(R: int):
    """Quadratic Casimir-locked potential block for irrep R.

    Returns (V_block, basis_fields) where V_block is the symbolic mass
    Lagrangian density and basis_fields are the (e, c) doublet/triplet
    components.
    """
    # Treat Phi_e, Phi_c as effective scalar magnitudes. The full Lorentz
    # / SU(2) structure factorises in the quadratic mass term.
    if R == 2:
        Phi_e = sp.Matrix(sp.symbols("Phi^d_e+ Phi^d_e0", complex=True))
        Phi_c = sp.Matrix(sp.symbols("Phi^d_c+ Phi^d_c0", complex=True))
    elif R == 3:
        Phi_e = sp.Matrix(sp.symbols("Phi^t_e1 Phi^t_e2 Phi^t_e3", real=True))
        Phi_c = sp.Matrix(sp.symbols("Phi^t_c1 Phi^t_c2 Phi^t_c3", real=True))
    else:
        raise ValueError("Only R = 2, 3 implemented (chat scope).")

    M2 = seed_matrix(R, m0sq)
    # Quadratic form: [|Phi_e|^2, conj]^T M^2 [|Phi_c|^2, ...]
    # We summarise as the (Phi_e, Phi_c) -> M^2 (Phi_e, Phi_c)^T mass matrix:
    return M2, (Phi_e, Phi_c)


def diagonalise_seed(R: int):
    """Diagonalise the seed for irrep R; return (lambda+, lambda-, U)."""
    M2 = seed_matrix(R, m0sq)
    P, D = M2.diagonalize()
    eigs = [D[i, i] for i in range(D.shape[0])]
    eigs_sorted = sorted(eigs, key=lambda e: float(sp.simplify(e / m0sq)))
    lam_minus, lam_plus = eigs_sorted[0], eigs_sorted[1]
    return lam_plus, lam_minus, P


def scalar_kinetic_terms_skeleton():
    """Canonical scalar kinetic terms (sigma factor):

        L_kin = sum_R sum_alpha=e,c (D_mu Phi^R_alpha)^dag (D^mu Phi^R_alpha)

    Returns the structure as a dict for downstream FeynRules export.
    """
    return {
        "doublet pair":  ["(D Phi^d_e)^dag (D Phi^d_e)", "(D Phi^d_c)^dag (D Phi^d_c)"],
        "triplet pair":  ["(1/2)(D Phi^t_e)^a (D Phi^t_e)^a", "(1/2)(D Phi^t_c)^a (D Phi^t_c)^a"],
    }


def quartic_potential_minimal():
    """Minimal quartic potential preserving the doublet-only-VEV pattern.

    V_quartic = lambda_d (Phi^d_-^dag Phi^d_-)^2  +  lambda_t (Phi^t_-)^2 (Phi^t_-)^2
              + lambda_dt (Phi^d_-^dag Phi^d_-) (Phi^t_- . Phi^t_-)

    where Phi^X_- denotes the negative-mass eigenstate after diagonalising
    the seed; only Phi^d_- gets a VEV. The triplet portal lambda_dt must
    be small enough that <Phi^t_-> < a few GeV (rho-parameter).
    """
    lam_d, lam_t, lam_dt = sp.symbols("lambda_d lambda_t lambda_{dt}", positive=True)
    return {
        "lambda_d":  lam_d,
        "lambda_t":  lam_t,
        "lambda_dt": lam_dt,
        "constraint": "lambda_dt small => <Phi^t_-> << v, preserving rho ~ 1",
    }


def main():
    print("=" * 70)
    print("Scalar sector of the Casimir-locked bosonic-seesaw model")
    print("=" * 70)

    print("\n[1] Elementary/composite seed pairs")
    M2_d, (Phi_de, Phi_dc) = seed_potential_block(2)
    M2_t, (Phi_te, Phi_tc) = seed_potential_block(3)
    print(f"    Doublet (R=2):  components {[str(x) for x in Phi_de]}, {[str(x) for x in Phi_dc]}")
    print(f"    Triplet (R=3):  components {[str(x) for x in Phi_te]}, {[str(x) for x in Phi_tc]}")

    print("\n[2] Casimir-locked seed mass matrices  M^2_R")
    print(f"    R=2:  {sp.pretty(M2_d, use_unicode=False).splitlines()}")
    print(f"    R=3:  {sp.pretty(M2_t, use_unicode=False).splitlines()}")

    print("\n[3] Diagonalisation of each block")
    for R in (2, 3):
        lp, lm, U = diagonalise_seed(R)
        c = C2(R)
        print(f"    R={R}: C_2 = {c}")
        print(f"      lambda_+ = {sp.simplify(lp)}")
        print(f"      lambda_- = {sp.simplify(lm)}")
        print(f"      mixing matrix U =")
        for row in sp.simplify(U).tolist():
            print(f"        {row}")

    print("\n[4] Minimal quartic potential")
    quartic = quartic_potential_minimal()
    for k, v in quartic.items():
        print(f"    {k}: {v}")

    print("\n[5] Kinetic-term skeleton (for FeynRules export)")
    skel = scalar_kinetic_terms_skeleton()
    for k, v in skel.items():
        print(f"    {k}: {v}")

    print("\n[6] EWSB pattern")
    print("    The negative eigenvalue of the doublet block is tachyonic.")
    print("    The corresponding mass eigenstate Phi^d_- acquires a VEV")
    print("    <Phi^d_-> = (0, v/sqrt(2))^T,  v = 246.22 GeV.")
    print("    Custodial symmetry of the doublet sector preserves rho ~ 1")
    print("    provided the triplet VEV is suppressed: <Phi^t_-> << v.")


if __name__ == "__main__":
    main()
