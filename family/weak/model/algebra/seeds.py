"""Casimir-locked bosonic-seesaw seed matrices.

Defines the doublet (R=2) and triplet/adjoint (R=3) seed mass-squared
matrices and reproduces every numerical claim of the source transcript:

  - 2x2 seed matrix M^2_R/m_0^2 = [[0, sqrt(C_2(R))], [sqrt(C_2(R)), -C_2(R)]]
  - Doublet eigenvalues: m_0^2 * (-3 +/- sqrt(57))/8
  - Triplet eigenvalues: m_0^2 * (-1 +/- sqrt(3))
  - Gauge sector: M_W^2 / M_Z^2 = lambda_{2,+} / lambda_{3,+}
                   -> sin^2(theta_W) and m_0 ~ 106.58 GeV
  - Higgs sector: m_h^2 + v^2/2 = m_0^2 * |Tr(negative branch)|
                   -> m_h ~ 125.3 GeV
"""

from __future__ import annotations

import sympy as sp

# Rational/symbolic constants
sqrt3 = sp.sqrt(3)
sqrt57 = sp.sqrt(57)


def C2(R: int) -> sp.Rational:
    """SU(2) quadratic Casimir for the irrep of dimension R = 2j+1."""
    j = sp.Rational(R - 1, 2)
    return j * (j + 1)


def seed_matrix(R: int, m0sq: sp.Symbol) -> sp.Matrix:
    """The Casimir-locked 2x2 seed matrix for SU(2) irrep R."""
    c = C2(R)
    t = sp.sqrt(c)
    return m0sq * sp.Matrix([[0, t], [t, -c]])


def seed_eigenvalues(R: int, m0sq: sp.Symbol):
    """Closed-form eigenvalues of the seed matrix in units of m0^2.

    Returns (lambda_plus, lambda_minus) as exact SymPy expressions.
    """
    M = seed_matrix(R, m0sq)
    # Solve characteristic polynomial: det(M - lambda I) = 0
    lam = sp.symbols("lambda", real=True)
    char = sp.expand(sp.det(M - lam * sp.eye(M.shape[0])))
    roots = sp.solve(char, lam)
    # Order: positive first, negative second
    roots_sorted = sorted(roots, key=lambda r: sp.simplify(r).evalf())
    return roots_sorted[1], roots_sorted[0]


def main():
    m0sq = sp.symbols("m0^2", positive=True)
    print("=" * 70)
    print("Casimir-locked bosonic-seesaw: algebraic verification")
    print("=" * 70)

    # --- Casimirs ----------------------------------------------------------
    print("\n[1] SU(2) Casimirs")
    print(f"    C_2(R=2 doublet)  = {C2(2)}    (= 3/4, j=1/2)")
    print(f"    C_2(R=3 triplet)  = {C2(3)}    (= 2,   j=1)")
    assert C2(2) == sp.Rational(3, 4)
    assert C2(3) == 2

    # --- Seed matrices -----------------------------------------------------
    print("\n[2] Seed matrices  M^2_R / m_0^2")
    M2 = seed_matrix(2, 1)
    M3 = seed_matrix(3, 1)
    print(f"    R=2:  {sp.pretty(M2, use_unicode=False).splitlines()}")
    print(f"    R=3:  {sp.pretty(M3, use_unicode=False).splitlines()}")

    # --- Characteristic polynomials ---------------------------------------
    print("\n[3] Characteristic polynomials (in lambda = eigenvalue / m_0^2)")
    lam = sp.symbols("lambda", real=True)
    char2 = sp.expand(sp.det(M2 - lam * sp.eye(2)))
    char3 = sp.expand(sp.det(M3 - lam * sp.eye(2)))
    # det(M - lam I) for 2x2 = lam^2 - tr(M) lam + det(M); we want
    # lam^2 + (Cas) lam - Cas, which is the chat convention (sign flipped on lam).
    # The chat writes char as lam^2 + 3/4 lam - 3/4 = 0, equivalent to ours up to overall sign.
    print(f"    R=2 (det form):  {char2} = 0    (chat eq: lambda^2 + 3/4 lambda - 3/4 = 0)")
    print(f"    R=3 (det form):  {char3} = 0    (chat eq: lambda^2 + 2 lambda - 2 = 0)")
    # Both forms are equivalent (multiply chat eq by 1, or our by -1; same roots).
    assert sp.expand(char2 - (lam**2 + sp.Rational(3, 4) * lam - sp.Rational(3, 4))) == 0
    assert sp.expand(char3 - (lam**2 + 2 * lam - 2)) == 0

    # --- Eigenvalues -------------------------------------------------------
    print("\n[4] Eigenvalues (units of m_0^2)")
    l2p, l2m = seed_eigenvalues(2, 1)
    l3p, l3m = seed_eigenvalues(3, 1)
    l2p_target = (sqrt57 - 3) / 8
    l2m_target = -(sqrt57 + 3) / 8
    l3p_target = sqrt3 - 1
    l3m_target = -(sqrt3 + 1)
    print(f"    lambda_{{2,+}} = {sp.simplify(l2p)}    (chat: (sqrt(57)-3)/8 ~ {float(l2p_target):.6f})")
    print(f"    lambda_{{2,-}} = {sp.simplify(l2m)}    (chat: -(sqrt(57)+3)/8 ~ {float(l2m_target):.6f})")
    print(f"    lambda_{{3,+}} = {sp.simplify(l3p)}             (chat: sqrt(3)-1 ~ {float(l3p_target):.6f})")
    print(f"    lambda_{{3,-}} = {sp.simplify(l3m)}            (chat: -(sqrt(3)+1) ~ {float(l3m_target):.6f})")
    assert sp.simplify(l2p - l2p_target) == 0
    assert sp.simplify(l2m - l2m_target) == 0
    assert sp.simplify(l3p - l3p_target) == 0
    assert sp.simplify(l3m - l3m_target) == 0

    # --- Gauge sector: M_W^2 / M_Z^2 --------------------------------------
    print("\n[5] Gauge sector: ratio of POSITIVE eigenvalues")
    ratio = sp.simplify(l2p / l3p)
    ratio_clean = sp.nsimplify(ratio, rational=False)
    print(f"    lambda_{{2,+}} / lambda_{{3,+}} = {ratio_clean}")
    print(f"                              ~ {float(ratio):.10f}")

    sin2_theta_w = sp.simplify(1 - ratio)
    print(f"    sin^2(theta_W) = 1 - ratio = {float(sin2_theta_w):.10f}")
    print(f"                    chat value:  0.2231013223")
    assert abs(float(sin2_theta_w) - 0.2231013223) < 1e-9

    # --- m_0 from M_Z ------------------------------------------------------
    print("\n[6] Derive m_0 from measured M_Z")
    MZ_pdg = 91.1880  # GeV (PDG 2024)
    MW_pdg = 80.3692  # GeV (PDG 2024)
    Mh_pdg = 125.20  # GeV (PDG 2024)
    GF = 1.1663787e-5  # Fermi constant in GeV^-2
    v_pdg = 1.0 / sp.sqrt(sp.sqrt(2) * GF)  # 246.2196 GeV
    print(f"    PDG: M_Z = {MZ_pdg}, M_W = {MW_pdg}, M_h = {Mh_pdg}, v = {float(v_pdg):.4f} GeV")

    # M_Z^2 = m_0^2 * lambda_{3,+}, so m_0 = M_Z / sqrt(lambda_{3,+})
    m0_pred = MZ_pdg / float(sp.sqrt(l3p_target))
    print(f"    m_0 = M_Z / sqrt(sqrt(3)-1) = {m0_pred:.4f} GeV    (chat: 106.58)")
    assert abs(m0_pred - 106.58) < 0.01

    # M_W from doublet eigenvalue
    MW_pred = m0_pred * float(sp.sqrt(l2p_target))
    print(f"    M_W (predicted) = m_0 * sqrt((sqrt(57)-3)/8) = {MW_pred:.4f} GeV    (PDG: {MW_pdg})")
    assert abs(MW_pred - MW_pdg) / MW_pdg < 0.001  # < 0.1% deviation

    # --- Higgs sector: trace identity --------------------------------------
    print("\n[7] Higgs sector: protected negative trace")
    neg_trace = sp.simplify(-(l2m_target + l3m_target))
    neg_trace_simplified = sp.nsimplify(neg_trace, rational=False)
    print(f"    |trace_neg| = (sqrt(57)+3)/8 + (sqrt(3)+1)")
    print(f"                = {neg_trace_simplified}")
    print(f"                ~ {float(neg_trace):.6f}")

    # m_h^2 + v^2/2 = m_0^2 * |trace_neg|
    rhs = m0_pred**2 * float(neg_trace)
    v2_over_2 = float(v_pdg) ** 2 / 2
    mh2_pred = rhs - v2_over_2
    mh_pred = mh2_pred**0.5
    print(f"\n    m_0^2 * |trace_neg| = {rhs:.3f} GeV^2")
    print(f"    v^2/2               = {v2_over_2:.3f} GeV^2")
    print(f"    m_h^2 = m_0^2 |trace_neg| - v^2/2 = {mh2_pred:.3f} GeV^2")
    print(f"    m_h   = {mh_pred:.4f} GeV    (chat: 125.3, PDG: {Mh_pdg})")
    assert abs(mh_pred - 125.3) < 0.1

    # --- Negative-branch antisymmetric splitting (chat sec. 9) ------------
    print("\n[8] Chat sec. 9: small antisymmetric residual")
    # Raw negative magnitudes (in units of m_0^2):
    a = float(-l2m_target)  # (sqrt(57)+3)/8
    b = float(-l3m_target)  # sqrt(3)+1
    print(f"    Raw negative magnitudes:")
    print(f"      a = (sqrt(57)+3)/8 ~ {a:.6f}")
    print(f"      b = (sqrt(3)+1)    ~ {b:.6f}")
    # Trace is preserved; chat says shift Delta ~ 700 GeV^2 / m_0^2
    Delta_GeV2 = 700.0  # chat: Delta ~ 700 GeV^2
    delta_in_units = Delta_GeV2 / m0_pred**2
    print(f"    Trace-preserving antisymmetric shift: Delta ~ {Delta_GeV2} GeV^2")
    print(f"    => sqrt(Delta) ~ {Delta_GeV2**0.5:.2f} GeV    (chat: 26.5)")

    # --- Summary -----------------------------------------------------------
    print("\n" + "=" * 70)
    print("SUMMARY OF PREDICTIONS")
    print("=" * 70)
    print(f"  m_0 (internal seed)  = {m0_pred:.4f} GeV")
    print(f"  sin^2(theta_W)       = {float(sin2_theta_w):.10f}")
    print(f"  M_W (predicted)      = {MW_pred:.4f} GeV  vs PDG {MW_pdg}")
    print(f"  M_Z (input)          = {MZ_pdg} GeV")
    print(f"  m_h (predicted)      = {mh_pred:.4f} GeV  vs PDG {Mh_pdg}")
    print(f"  v (input)            = {float(v_pdg):.4f} GeV")
    print()
    print("All chat-claimed numerical results reproduced within < 0.1%.")


if __name__ == "__main__":
    main()
