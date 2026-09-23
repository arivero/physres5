"""LRSM mock-up: Casimir lock on BOTH SU(2)_L and SU(2)_R, with U(1)_Y
emerging from the broken SU(2)_R x U(1)_{B-L} subgroup.

EXPLICITLY EXPLORATORY -- this script is *not* folded into the v4
paper. It is here to test the user hypothesis: "spin 1/2 -> SU(2),
spin 1 -> U(1) or to where U(1) comes from", interpreted in the
strong sense as "the Casimir-locked j=1 channel on SU(2)_R provides
the substrate from which U(1)_Y emerges".

Setup (left-right symmetric model, LRSM):
  Gauge group:    G_LR = SU(2)_L x SU(2)_R x U(1)_{B-L}
  Hypercharge:    Y = T^3_R + (B-L)/2
  Higgs sector:   bidoublet Phi (2_L, 2_R, 0)
                  + right-triplet Delta_R (1_L, 3_R, 2)
                  (and optionally Delta_L (3_L, 1_R, 2))

Symmetry breaking pattern:
  Stage I  (high scale v_R):  G_LR -> SU(2)_L x U(1)_Y  via <Delta_R>
  Stage II (low scale v_L):   SU(2)_L x U(1)_Y -> U(1)_em  via <Phi>
  After Stage I: g' is determined by g_R, g_BL via
                 1/g'^2 = 1/g_R^2 + 1/g_BL^2.

Casimir-lock extension:
  Apply the same Casimir-locked seed structure to BOTH SU(2)_L and
  SU(2)_R sectors:
    SU(2)_L:  doublet (j=1/2), triplet (j=1)  with seed scale m_0^L = 106.57 GeV
    SU(2)_R:  doublet (j=1/2), triplet (j=1)  with seed scale m_0^R = ?

  Phase-D condition for each sector:
    m_chi_R^2 = y |eps| C_2(R)
  with possibly distinct y, eps for L and R sectors.

The right-triplet Delta_R gets a Casimir-locked mass; its tachyonic
eigenvalue triggers the SU(2)_R x U(1)_{B-L} -> U(1)_Y breaking at
scale v_R.

What this script does:
  1. Documents the gauge structure and breaking pattern.
  2. Computes the Casimir-locked spectrum at the SU(2)_R scale,
     given an assumed m_0^R.
  3. Checks the LRSM relation 1/g'^2 = 1/g_R^2 + 1/g_BL^2 against
     our model's g' = 0.349 prediction. With the parity assumption
     g_R = g_L = g, this fixes g_BL (the U(1)_{B-L} coupling).
  4. Identifies the heavy W_R, Z_R masses and compares to LHC
     direct-search bounds.
  5. Asks: does the Casimir lock predict m_0^R, or is it a free
     scale?
  6. Documents what's gained and what's lost relative to the
     low-energy Casimir-locked SU(2)_L x U(1)_Y model of v4.
"""

from __future__ import annotations

import math
import sys


# --- Inputs (low-energy, from the v4 model) ---
MW_PDG = 80.3692
MZ_PDG = 91.188
G_L    = 0.6529                          # SU(2)_L coupling (predicted in v4)
GP     = 0.349                           # U(1)_Y coupling (predicted in v4)
SIN2W  = 0.22310                         # Casimir-locked algebraic value
LAM_2P = (math.sqrt(57) - 3) / 8.0       # 0.5687
LAM_2M = -(math.sqrt(57) + 3) / 8.0      # -1.3187
LAM_3P = math.sqrt(3) - 1.0              # 0.7321
LAM_3M = -(math.sqrt(3) + 1.0)           # -2.7321

m0_L   = MW_PDG / math.sqrt(LAM_2P)      # 106.5705 GeV (from M_W anchor)


def main() -> int:
    print("=" * 78)
    print("LRSM Casimir-locked extension MOCK -- analysis only, NOT in paper")
    print("=" * 78)

    print("""
[1] GAUGE STRUCTURE

  G_LR = SU(2)_L x SU(2)_R x U(1)_{B-L}
       --(stage I, v_R)-->  SU(2)_L x U(1)_Y
       --(stage II, v_L)--> U(1)_em

  Hypercharge:  Y = T^3_R + (B-L)/2

  Casimir-locked seeds (mock proposal):
    SU(2)_L: doublet H^L_(2_L,1_R), triplet T^L_(3_L,1_R) (Y=0)
             seed scale m_0^L = 106.57 GeV (anchored by M_W)
    SU(2)_R: doublet H^R_(1_L,2_R), triplet T^R_(1_L,3_R) (B-L=2)
             seed scale m_0^R = ? (TBD)
    Bidoublet Phi (2_L, 2_R, 0): standard LRSM ingredient, mediates
             the EWSB to U(1)_em at low scale.
""")

    print("[2] STAGE I: SU(2)_R x U(1)_{B-L} -> U(1)_Y  via <Delta_R>")
    print()
    print("  The right-triplet Delta_R = T^R has a Casimir-locked seed mass;")
    print("  its tachyonic eigenvalue sets v_R via the standard SM-like")
    print("  Higgs mechanism, mirrored from the SU(2)_L sector:")
    print()
    print("    M(W_R^+/-)  = g_R v_R / 2")
    print("    M(Z_R)      = sqrt(g_R^2 + g_BL^2 (R-charge)^2) v_R / 2")
    print()
    print("  Standard LRSM relation between low-energy g' and (g_R, g_BL):")
    print("    1/g'^2 = 1/g_R^2 + 1/g_BL^2")
    print()
    g_R = G_L  # parity assumption
    print(f"  Parity: g_R = g_L = g = {g_R:.4f}")
    print(f"  Solve for g_BL given g' = {GP}:")
    g_BL_sq = 1.0 / (1.0/GP**2 - 1.0/g_R**2)
    g_BL = math.sqrt(g_BL_sq)
    print(f"    1/g_BL^2 = 1/g'^2 - 1/g_R^2 = {1.0/GP**2:.4f} - {1.0/g_R**2:.4f} = {1.0/g_BL_sq:.4f}")
    print(f"    g_BL     = {g_BL:.4f}")
    print()
    print(f"  Interpretation: g_BL is a NEW input not constrained by SU(2)")
    print(f"  Casimir lock (U(1)_{{B-L}} is abelian, no Casimir).")
    print(f"  In Casimir-locked LRSM, g_BL is genuinely a free parameter")
    print(f"  unless tied to additional UV structure.")

    print("""
[3] STAGE II: SU(2)_L x U(1)_Y -> U(1)_em  via bidoublet <Phi>

  This is exactly the v4 paper's Casimir-locked EWSB on the doublet's
  tachyonic eigenvalue, but now the doublet mixes with the SU(2)_R
  doublet via the bidoublet structure. The bidoublet has two neutral
  components <h_1^0> = v_L1, <h_2^0> = v_L2; their combination gives
  the SM v.

  Standard relations (with v_R^2 >> v_L^2):
    M_W^2 = g^2 (v_L1^2 + v_L2^2) / 4
    M_Z^2 = (g^2 + g'^2)(v_L1^2 + v_L2^2)/4 + (corrections at order v_L^2/v_R^2)

  Our v4 prediction M_W = 80.37 GeV holds at leading order in v_L/v_R.
""")

    print("[4] CASIMIR-LOCKED PREDICTIONS FOR THE NEW STATES")
    print()
    print("  The SU(2)_R sector has the same Casimir-locked seed structure:")
    print(f"    M(W_R) = m_0^R * sqrt(lambda_+(2)) = m_0^R * {math.sqrt(LAM_2P):.4f}")
    print(f"    M(Z_R) = m_0^R * sqrt(lambda_+(3)) = m_0^R * {math.sqrt(LAM_3P):.4f}")
    print()
    print("  Predicted ratio:")
    print(f"    M(W_R) / M(Z_R) = sqrt(lambda_+(2)/lambda_+(3)) = {math.sqrt(LAM_2P/LAM_3P):.4f}")
    print(f"    => M(W_R) / M(Z_R) = {math.sqrt(LAM_2P/LAM_3P):.4f}  (independent of m_0^R)")
    print()
    print("  This is the SAME ratio M_W^L / M_Z^L = 0.881 we get from the")
    print("  SU(2)_L sector. The Casimir lock predicts identical W/Z ratios")
    print("  in the L and R sectors -- a TESTABLE prediction.")

    print("""
[5] LHC bounds on m_0^R

  Direct LHC searches set roughly M(W_R) > 4-6 TeV (ATLAS, CMS
  searches in pp -> W_R -> tb, jj). With M(W_R) = m_0^R * sqrt(lambda_+(2)):
""")
    for MWR_min_TeV in (4.0, 6.0, 10.0):
        m0R = MWR_min_TeV * 1000 / math.sqrt(LAM_2P)
        MZR = m0R * math.sqrt(LAM_3P)
        print(f"    M(W_R) > {MWR_min_TeV} TeV  =>  m_0^R > {m0R:.0f} GeV  =>  M(Z_R) > {MZR:.0f} GeV")

    print("""
[6] DOES THE CASIMIR LOCK FIX m_0^R FROM THE LOW-ENERGY THEORY?

  Without additional UV input, NO. m_0^L = 106.57 GeV is anchored by
  M_W. m_0^R is a free scale that must be set by the SU(2)_R sector's
  own dynamics. Possible relations:

  (a) Parity: m_0^R = m_0^L  =>  M(W_R) = M_W = 80 GeV  (EXCLUDED by LHC).
      So strict parity at the seed level is RULED OUT.

  (b) Casimir-extended ratio: m_0^R / m_0^L = some Casimir ratio.
      No obvious candidate from SU(2) representation theory alone.

  (c) Independent dynamics: m_0^R is a free TeV-scale parameter.
      Then the LRSM extension introduces a NEW SCALE not predicted by
      the original Casimir lock.

  (d) Tied to the U(1)_{B-L} coupling g_BL = 0.41 (mock estimate above).
      Could in principle be motivated by a higher-rank UV embedding
      (SO(10), Pati-Salam) that ties the SU(2) and U(1) scales.

[7] TESTABLE PREDICTIONS (assuming m_0^R = some TeV-scale value)

  * M(W_R) / M(Z_R) = 0.881 (same ratio as M_W/M_Z; testable at LHC/FCC).
  * Existence of a heavy "Higgs-bare-like" state at m_0^R * sqrt(|lam_-(2)|)
    = 1.523 m_0^R (analogous to m_h_bare in the L sector).
  * Existence of a heavy "176-GeV-like" state at m_0^R * sqrt(|lam_-(3)|)
    = 1.653 m_0^R (analogous to v/sqrt(2) state in the L sector).

  For m_0^R = 5 TeV (compatible with current bounds):
""")
    m0R_test = 5000.0
    print(f"    m_0^R = {m0R_test} GeV")
    print(f"    M(W_R)            = {m0R_test * math.sqrt(LAM_2P):.0f} GeV  ~ 3.8 TeV (just below current bounds)")
    print(f"    M(Z_R)            = {m0R_test * math.sqrt(LAM_3P):.0f} GeV  ~ 4.3 TeV")
    print(f"    M(h^R_bare)       = {m0R_test * math.sqrt(abs(LAM_2M)):.0f} GeV  ~ 5.7 TeV")
    print(f"    M(176-analog)     = {m0R_test * math.sqrt(abs(LAM_3M)):.0f} GeV  ~ 8.3 TeV")

    print("""
[8] WHAT IS GAINED, WHAT IS LOST

  GAINED (relative to v4):
    + U(1)_Y has a UV ORIGIN (residual of SU(2)_R x U(1)_{B-L} after
      Casimir-locked Delta_R triplet acquires VEV at m_0^R).
    + The ratio M(W_R)/M(Z_R) = 0.881 is a parameter-free PREDICTION
      independent of m_0^R, mirroring the low-energy M_W/M_Z ratio.
    + A complete UV embedding into LRSM is a known framework
      (Pati-Salam, SO(10), etc.).

  LOST:
    - One new scale m_0^R is introduced; not predicted by the Casimir
      lock (parity fails phenomenologically).
    - U(1)_{B-L} coupling g_BL ~ 0.41 is a NEW free parameter (no
      Casimir for abelian groups). The clean v4 prediction
      sin^2(theta_W) = 1 - lambda_+(2)/lambda_+(3) becomes a
      CONSTRAINT relating m_0^R, g_BL, and v_R, no longer parameter-free.
    - The bidoublet quartic structure adds further free parameters
      to the scalar potential.
    - The LRSM extension TRADES one free input (g' in v4) for two
      free inputs (m_0^R, g_BL). Net parameter count INCREASES.

[9] VERDICT ON THE USER HYPOTHESIS

  "U(1)_Y comes from where the j=1 channel lives in the gauge sector"

  In the LRSM extension: U(1)_Y is the residual of SU(2)_R x U(1)_{B-L}
  after the j=1 (triplet) Casimir-locked Delta_R acquires a VEV. So
  yes, the j=1 channel of SU(2)_R IS structurally what U(1)_Y comes
  from.

  However, the price of this structural identification is HIGHER total
  parameter count, not LOWER:
    v4 model:  m_0, Delta  -> M_W, M_Z, m_h, v/sqrt(2)
                              + free inputs: g, g', G_F (or 2 of them)
                              -> total: 2 model params + 2 free inputs

    LRSM mock: m_0^L, m_0^R, Delta, g_BL  -> M_W, M_Z, M(W_R), M(Z_R),
                                              m_h, v, ...
                              + free inputs: g, G_F (1 fewer than v4)
                              -> total: 4 model params + 1 free input

  So the LRSM extension makes the U(1)_Y origin EXPLICIT but at the
  cost of adding 2 new model parameters (m_0^R, g_BL) for the gain
  of removing 1 free input (g'). NET: +1 parameter.

  CONCLUSION: the hypothesis "U(1)_Y from SU(2)_R Casimir lock" is
  STRUCTURALLY consistent and PREDICTS a heavy-state spectrum
  (W_R, Z_R, etc.) with the same Casimir-locked mass ratio as the
  low-energy sector. But it does NOT economize on parameters; it
  introduces a new scale m_0^R that the Casimir lock does not
  determine.

  For the v4 paper, the LRSM extension is best presented as a
  natural future direction, NOT as an in-line proposal. The
  predicted heavy-W_R/Z_R mass ratio = 0.881 is a clean falsifiable
  signature for any future LRSM realisation of the model.
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
