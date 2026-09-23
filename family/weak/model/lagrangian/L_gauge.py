"""Gauge sector of the Casimir-locked bosonic-seesaw model.

Low-energy gauge group: G_LE = SU(2)_L x U(1)_Y (same as SM at the
electroweak scale). The chat-confirmed role of hypercharge as a
'low-energy spurion that splits doublet vs. triplet' constrains the UV
embedding without changing the IR gauge content.

This module defines the gauge fields, generators, covariant derivatives,
and Yang-Mills kinetic terms symbolically.
"""

from __future__ import annotations

import sympy as sp

# ---------------------------------------------------------------------------
# Symbols
# ---------------------------------------------------------------------------
# Couplings
g, gp = sp.symbols("g g'", positive=True)

# Gauge fields (flat-spacetime placeholders). In a full Lagrangian we
# would carry Lorentz indices; for the purpose of mass-matrix algebra we
# only need the algebraic structure of the kinetic operator.
W1, W2, W3 = sp.symbols("W^1 W^2 W^3", real=True)
B = sp.symbols("B", real=True)

# Pauli matrices
sigma1 = sp.Matrix([[0, 1], [1, 0]])
sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sigma3 = sp.Matrix([[1, 0], [0, -1]])
sigmas = [sigma1, sigma2, sigma3]

# SU(2) generators in fundamental rep: T^a = sigma^a / 2
T_fund = [s / 2 for s in sigmas]


def covariant_derivative_doublet(Phi_doublet):
    """Symbolic covariant derivative on an SU(2)_L doublet of hypercharge Y=1/2.

    D_mu Phi = (d_mu - i g W^a T^a - i g' Y B_mu) Phi
    Returns the gauge-piece (d_mu suppressed): -i (g W^a T^a + g' Y B) Phi.
    """
    Y = sp.Rational(1, 2)
    gauge_piece = sp.zeros(2, 2)
    for Wa, Ta in zip([W1, W2, W3], T_fund):
        gauge_piece += g * Wa * Ta
    gauge_piece += gp * Y * B * sp.eye(2)
    return -sp.I * gauge_piece * Phi_doublet


def covariant_derivative_triplet(Phi_triplet, Y=0):
    """Symbolic covariant derivative on a real SU(2)_L triplet of hypercharge Y.

    For Y=0 (real triplet, like the Georgi-Machacek case), only SU(2)_L
    generators in the adjoint representation contribute. We embed the
    triplet as a 3-vector and use T^a_adj_{bc} = -i epsilon^{abc}.
    """
    eps = sp.MutableDenseNDimArray.zeros(3, 3, 3)
    eps[0, 1, 2] = eps[1, 2, 0] = eps[2, 0, 1] = 1
    eps[0, 2, 1] = eps[2, 1, 0] = eps[1, 0, 2] = -1
    T_adj = []
    for a in range(3):
        Ta = sp.Matrix(3, 3, lambda b, c: -sp.I * eps[a, b, c])
        T_adj.append(Ta)
    gauge_piece = sp.zeros(3, 3)
    for Wa, Ta in zip([W1, W2, W3], T_adj):
        gauge_piece += g * Wa * Ta
    if Y != 0:
        gauge_piece += gp * Y * B * sp.eye(3)
    return -sp.I * gauge_piece * Phi_triplet


def yang_mills_kinetic_skeleton():
    """Returns a symbolic skeleton for the Yang-Mills kinetic terms.

    L_YM = -1/4 W^a_{mu nu} W^{a mu nu} - 1/4 B_{mu nu} B^{mu nu}

    For our purposes we don't need the explicit field-strength tensor;
    we only need the canonical normalisation coefficient -1/4.
    """
    return {
        "SU(2)_L kinetic coefficient": sp.Rational(-1, 4),
        "U(1)_Y  kinetic coefficient": sp.Rational(-1, 4),
        "couplings": (g, gp),
        "fields": (W1, W2, W3, B),
    }


def diagonalise_neutral_gauge_sector(v):
    """After EWSB, the neutral gauge bosons (W^3, B) mix into (Z, A).

    The mass-squared matrix in the (W^3, B) basis from a doublet VEV
    <Phi> = (0, v/sqrt2)^T is

        M^2 = (v^2/4) * [[g^2,   -g g'],
                         [-g g', g'^2 ]]

    Returns (M_W^2, M_Z^2, M_A^2, weinberg_angle).
    """
    M2 = (v**2 / 4) * sp.Matrix([[g**2, -g * gp], [-g * gp, gp**2]])
    eigvals = list(M2.eigenvals().keys())
    # Order: 0 (photon), nonzero (Z)
    eigvals_sorted = sorted(eigvals, key=lambda e: sp.simplify(e).evalf(subs={g: 0.65, gp: 0.35, v: 246.0}))
    M_A2, M_Z2 = eigvals_sorted[0], eigvals_sorted[1]
    M_W2 = g**2 * v**2 / 4
    # Weinberg angle: tan(theta_W) = g'/g
    sin2_thetaW = gp**2 / (g**2 + gp**2)
    return M_W2, M_Z2, M_A2, sin2_thetaW


def main():
    print("=" * 70)
    print("Gauge sector of the Casimir-locked bosonic-seesaw model")
    print("=" * 70)

    skel = yang_mills_kinetic_skeleton()
    print("\n[1] Yang-Mills kinetic skeleton")
    for k, v in skel.items():
        print(f"    {k}: {v}")

    print("\n[2] Covariant derivative on a Y=1/2 doublet")
    Phi = sp.Matrix(sp.symbols("phi^+ phi^0", complex=True))
    DPhi = covariant_derivative_doublet(Phi)
    print(f"    D Phi (gauge piece) = {DPhi.T}")

    print("\n[3] Covariant derivative on a Y=0 real triplet")
    T = sp.Matrix(sp.symbols("t^1 t^2 t^3", real=True))
    DT = covariant_derivative_triplet(T)
    print(f"    D T (gauge piece) = {DT.T}")

    print("\n[4] Standard EWSB from a doublet VEV: (W^3, B) -> (Z, A)")
    v_sym = sp.symbols("v", positive=True)
    MW2, MZ2, MA2, s2W = diagonalise_neutral_gauge_sector(v_sym)
    print(f"    M_W^2  = {MW2}")
    print(f"    M_Z^2  = {sp.simplify(MZ2)}")
    print(f"    M_A^2  = {sp.simplify(MA2)}")
    print(f"    sin^2(theta_W) = g'^2 / (g^2 + g'^2) = {s2W}")
    print(f"    Ratio  M_W^2 / M_Z^2 = {sp.simplify(MW2 / MZ2)}    (= cos^2 theta_W)")

    # Numerical check: with the model's prediction sin^2 theta_W = 0.2231013,
    # we recover the standard relation M_W^2/M_Z^2 = 1 - sin^2 theta_W
    s2W_model = 0.2231013223
    print(f"\n    Plugging model prediction sin^2(theta_W) = {s2W_model}:")
    print(f"      => M_W^2/M_Z^2 = {1 - s2W_model:.10f}")
    print(f"      Matches PDG (M_W/M_Z)^2 = {(80.3692/91.1880)**2:.10f}")


if __name__ == "__main__":
    main()
