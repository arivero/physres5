"""End-to-end EWSB derivation for the Casimir-locked bosonic seesaw.

Pipeline:
    1. Take the Casimir-locked seed eigenvalues (from algebra/seeds.py).
    2. Identify the gauge-sector ratio  M_W^2/M_Z^2 = lambda_{2,+} / lambda_{3,+}.
    3. Use measured M_Z and v as inputs to fix m_0.
    4. Predict M_W and m_h.
    5. Compare to PDG 2024 measurements.

Exit code 0 iff every prediction matches PDG to better than 0.5%.
"""

from __future__ import annotations

import sys

import sympy as sp

from seeds import seed_eigenvalues  # noqa: E402

# ---------------------------------------------------------------------------
# PDG 2024 inputs
# ---------------------------------------------------------------------------
MZ_PDG = 91.1880    # GeV
MW_PDG = 80.3692    # GeV
MH_PDG = 125.20     # GeV
GF     = 1.1663787e-5  # GeV^-2

V_VEV  = float(1.0 / sp.sqrt(sp.sqrt(2) * GF))  # 246.2196 GeV

# ---------------------------------------------------------------------------
# Tolerances
# ---------------------------------------------------------------------------
TOL_MW = 0.005   # 0.5%
TOL_MH = 0.005   # 0.5%


def main() -> int:
    print("=" * 70)
    print("EWSB end-to-end check (Phase 3)")
    print("=" * 70)

    # --- Symbolic eigenvalues (per unit m_0^2) ------------------------------
    m0sq = sp.symbols("m_0^2", positive=True)
    l2p, l2m = seed_eigenvalues(2, m0sq)  # doublet +, -
    l3p, l3m = seed_eigenvalues(3, m0sq)  # triplet +, -

    # Strip m_0^2 factor for the per-unit-m_0^2 numbers
    l2p_unit = sp.simplify(l2p / m0sq)
    l3p_unit = sp.simplify(l3p / m0sq)
    l2m_unit = sp.simplify(l2m / m0sq)
    l3m_unit = sp.simplify(l3m / m0sq)

    print("\nSeed eigenvalues (units of m_0^2):")
    print(f"  doublet: lambda_+ = {l2p_unit}    -> {float(l2p_unit):.6f}")
    print(f"           lambda_- = {l2m_unit}    -> {float(l2m_unit):.6f}")
    print(f"  triplet: lambda_+ = {l3p_unit}    -> {float(l3p_unit):.6f}")
    print(f"           lambda_- = {l3m_unit}    -> {float(l3m_unit):.6f}")

    # --- Gauge-sector identification ---------------------------------------
    # The chat identifies M_Z^2 = m_0^2 * lambda_{3,+}  and  M_W^2 = m_0^2 * lambda_{2,+}.
    print("\nGauge-sector identification (chat sec. 7):")
    print("  M_Z^2 = m_0^2 * lambda_{3,+}")
    print("  M_W^2 = m_0^2 * lambda_{2,+}")

    m0_pred = MZ_PDG / float(sp.sqrt(l3p_unit))
    MW_pred = m0_pred * float(sp.sqrt(l2p_unit))
    s2W_pred = 1.0 - float(l2p_unit / l3p_unit)

    print(f"\n  Inputs:  M_Z (PDG)  = {MZ_PDG} GeV")
    print(f"           v   (G_F)  = {V_VEV:.4f} GeV")
    print(f"  Solve:   m_0        = {m0_pred:.4f} GeV")
    print(f"  Predict: M_W        = {MW_pred:.4f} GeV  (PDG: {MW_PDG})")
    print(f"  Predict: sin^2(thW) = {s2W_pred:.10f}")

    # --- Higgs identification ---------------------------------------------
    # The chat identifies  m_h^2 + v^2/2  =  m_0^2 * |lambda_{2,-} + lambda_{3,-}|.
    print("\nHiggs-sector identification (chat sec. 8):")
    print("  m_h^2 + v^2/2 = m_0^2 * |lambda_{2,-} + lambda_{3,-}|")

    neg_trace_unit = -float(l2m_unit + l3m_unit)
    rhs = m0_pred**2 * neg_trace_unit
    mh2_pred = rhs - 0.5 * V_VEV**2
    mh_pred = mh2_pred**0.5

    print(f"\n  |trace_neg| = {neg_trace_unit:.6f}")
    print(f"  m_0^2 * |trace_neg| = {rhs:.3f} GeV^2")
    print(f"  v^2/2               = {0.5 * V_VEV**2:.3f} GeV^2")
    print(f"  m_h^2               = {mh2_pred:.3f} GeV^2")
    print(f"  m_h (predicted)     = {mh_pred:.4f} GeV  (PDG: {MH_PDG})")

    # --- Tolerance check ---------------------------------------------------
    dev_MW = abs(MW_pred - MW_PDG) / MW_PDG
    dev_MH = abs(mh_pred - MH_PDG) / MH_PDG

    print("\n" + "=" * 70)
    print("VERIFICATION")
    print("=" * 70)
    print(f"  M_W deviation from PDG: {dev_MW * 100:.3f}%   (tolerance {TOL_MW * 100:.1f}%)")
    print(f"  m_h deviation from PDG: {dev_MH * 100:.3f}%   (tolerance {TOL_MH * 100:.1f}%)")

    ok = dev_MW < TOL_MW and dev_MH < TOL_MH
    if ok:
        print("\n  ALL PREDICTIONS PASS.")
        return 0
    else:
        print("\n  AT LEAST ONE PREDICTION OUT OF TOLERANCE.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
