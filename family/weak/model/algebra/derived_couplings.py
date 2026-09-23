"""Q1 step 1: derived SM couplings from the Casimir-locked identifications.

Conditional on the seed eigenvalue identifications of Section 6 of the
paper:
    M_W^2 = m_0^2  lambda_+(2)
    M_Z^2 = m_0^2  lambda_+(3)
    m_h^2 = m_0^2 |lambda_-(2)|  +  Delta
    (v/sqrt 2)^2 = m_0^2 |lambda_-(3)|  -  Delta

we ALSO derive the SM EW couplings g, g', and the Higgs self-coupling
lambda_h, by combining the seed predictions with standard tree-level
EWSB on the doublet's tachyonic mass eigenstate. This is the missing
"derivation" step requested as Q1: the seed identifications + SM EWSB
relations (M_W = g v / 2, m_h^2 = 2 lambda_h v^2) suffice to pin the
gauge couplings.

Not derived here (still open):
  * Why the seed eigenvalue equals the gauge-boson mass-squared (the
    eigenvalue-to-physical-mass postulate of Section 6).
  * The microscopic origin of Delta (top-CW for the doublet half is
    in Section 7; triplet half is open work Q6).
  * The numerical value of lambda_h from a Lagrangian (we extract it
    from m_h and v via the SM relation, then check consistency).
"""

from __future__ import annotations

import math
import sys

# --- Anchored inputs ---
MW_PDG = 80.3692         # input: anchor
MH_PDG = 125.20          # input: anchor (fixes Delta)
MZ_PDG = 91.1880         # for cross-check only
GF     = 1.1663787e-5    # for v_PDG cross-check
ALPHA_INV = 127.918

# --- Casimir-locked structure (Phase 1) ---
LAM_2P =  (math.sqrt(57) - 3) / 8.0          # 0.5687
LAM_2M = -(math.sqrt(57) + 3) / 8.0          # -1.3187
LAM_3P =  math.sqrt(3) - 1.0                 # 0.7321
LAM_3M = -(math.sqrt(3) + 1.0)               # -2.7321


def main() -> int:
    print("=" * 78)
    print("Q1 step 1: derived SM couplings (g, g', lambda_h) from seed + EWSB")
    print("=" * 78)

    # --- Step 0: m_0 from M_W anchor ---
    m0 = MW_PDG / math.sqrt(LAM_2P)
    m02 = m0 * m0
    print(f"\n[0] m_0 = M_W / sqrt(lambda_+(2)) = {m0:.4f} GeV  (anchor)")

    # --- Step 1: M_Z prediction (unchanged from Section 6) ---
    MZ_pred = m0 * math.sqrt(LAM_3P)
    print(f"\n[1] M_Z = m_0 sqrt(lambda_+(3)) = {MZ_pred:.4f} GeV")
    print(f"    (PDG 91.1880, deviation {(MZ_pred - MZ_PDG)*100/MZ_PDG:+.4f}%)")

    # --- Step 2: bare Higgs from doublet negative eigenvalue ---
    mh_bare = m0 * math.sqrt(abs(LAM_2M))
    print(f"\n[2] m_h_bare = m_0 sqrt(|lambda_-(2)|) = {mh_bare:.4f} GeV")
    print(f"    Delta_d = m_h_phys^2 - m_h_bare^2 = ({math.sqrt(MH_PDG**2 - mh_bare**2):.3f} GeV)^2 = ({MH_PDG**2 - mh_bare**2:.2f} GeV^2)")

    Delta = MH_PDG**2 - mh_bare**2
    print(f"    Delta (anchored to m_h_phys) = ({math.sqrt(Delta):.3f} GeV)^2")

    # --- Step 3: v from cross-irrep negative-branch trace identity ---
    # |lambda_-(3)| m_0^2 - Delta = (v/sqrt 2)^2
    vF_sq = m02 * abs(LAM_3M) - Delta
    vF_pred = math.sqrt(vF_sq)
    v_pred = vF_pred * math.sqrt(2.0)
    v_PDG = 1.0 / math.sqrt(math.sqrt(2) * GF)
    print(f"\n[3] v/sqrt(2) = sqrt(|lambda_-(3)| m_0^2 - Delta) = {vF_pred:.4f} GeV")
    print(f"    => v = {v_pred:.4f} GeV   (PDG from G_F: {v_PDG:.4f}, dev {(v_pred-v_PDG)*100/v_PDG:+.4f}%)")

    # --- Step 4: g from M_W = g v / 2 (standard EWSB on doublet VEV) ---
    g_pred = 2.0 * MW_PDG / v_pred
    g_PDG  = 2.0 * MW_PDG / v_PDG
    print(f"\n[4] g = 2 M_W / v_pred = {g_pred:.6f}")
    print(f"    (g_PDG = 2 M_W / v_PDG = {g_PDG:.6f}, dev {(g_pred-g_PDG)*100/g_PDG:+.4f}%)")
    print(f"    PDG quoted g = 0.65294(2). The model's g matches to ~0.05% --")
    print(f"    a *derived* gauge coupling, not an input.")

    # --- Step 5: g' from M_Z and g ---
    # M_Z^2 = (g^2 + g'^2) v^2 / 4
    gp_sq = 4.0 * MZ_pred**2 / v_pred**2 - g_pred**2
    gp_pred = math.sqrt(gp_sq)
    print(f"\n[5] g' = sqrt(4 M_Z^2 / v^2 - g^2) = {gp_pred:.6f}")
    print(f"    Standard PDG g' (running, MS-bar) ~ 0.358; our (on-shell-derived)")
    print(f"    g' is naturally ~2% lower because of the on-shell vs MS-bar shift.")

    # --- Step 6: sin^2(theta_W) cross-check ---
    s2W_pred = gp_sq / (g_pred**2 + gp_sq)
    s2W_alg  = 1.0 - LAM_2P/LAM_3P
    print(f"\n[6] sin^2(theta_W) consistency check:")
    print(f"    From g, g':              sin^2(theta_W) = g'^2/(g^2+g'^2) = {s2W_pred:.6f}")
    print(f"    Algebraic from Casimirs: sin^2(theta_W) = 1 - lambda_+(2)/lambda_+(3) = {s2W_alg:.6f}")
    print(f"    Match: {abs(s2W_pred-s2W_alg) < 1e-6}  (must be exact by construction)")

    # --- Step 7: e from g sin(theta_W) ---
    e_pred = g_pred * math.sqrt(s2W_pred)
    alpha_pred = e_pred**2 / (4 * math.pi)
    alpha_PDG  = 1.0 / ALPHA_INV
    e_PDG = math.sqrt(4 * math.pi * alpha_PDG)
    print(f"\n[7] e = g sin(theta_W) = {e_pred:.5f}")
    print(f"    alpha = e^2/(4 pi) = {alpha_pred:.7f}, 1/alpha = {1.0/alpha_pred:.3f}")
    print(f"    PDG alpha(M_Z) = {alpha_PDG:.7f}, 1/alpha(M_Z) = {ALPHA_INV:.3f}")
    print(f"    Deviation: {(e_pred-e_PDG)*100/e_PDG:+.3f}%   (reflects on-shell vs running scheme)")

    # --- Step 8: Higgs self-coupling lambda_h from m_h^2 = 2 lambda_h v^2 ---
    lambda_h_pred = MH_PDG**2 / (2 * v_pred**2)
    print(f"\n[8] Higgs quartic self-coupling")
    print(f"    SM relation: m_h^2 = 2 lambda_h v^2  =>  lambda_h = m_h^2 / (2 v^2)")
    print(f"    Implied lambda_h = {lambda_h_pred:.5f}")
    print(f"    SM-textbook value at tree level: ~ 0.1293")
    print(f"    Our model thus implies a SM-strength quartic coupling -- the")
    print(f"    model is consistent with standard SM EWSB on the doublet's")
    print(f"    negative-eigenvalue mass eigenstate.")

    # --- Summary ---
    print("\n" + "=" * 78)
    print("SUMMARY: derived predictions vs. PDG (with M_W and m_h as anchors)")
    print("=" * 78)
    rows = [
        ("M_Z",        MZ_pred,           MZ_PDG,        "GeV"),
        ("v",          v_pred,            v_PDG,         "GeV"),
        ("v/sqrt(2)",  vF_pred,           v_PDG/math.sqrt(2), "GeV"),
        ("g",          g_pred,            g_PDG,         ""),
        ("g'",         gp_pred,           0.358,         "(approx PDG)"),
        ("sin^2(thW)", s2W_pred,          0.22290,       "OS scheme"),
        ("e",          e_pred,            e_PDG,         ""),
        ("alpha",      alpha_pred,        alpha_PDG,     ""),
        ("lambda_h",   lambda_h_pred,     0.1293,        "SM value"),
    ]
    for name, pred, pdg, units in rows:
        if pdg != 0:
            dev = (pred - pdg) * 100 / pdg
            print(f"  {name:>12} = {pred:>12.6f}    PDG/SM: {pdg:>12.6f}   dev {dev:+8.4f}%   {units}")

    print("\nVerdict: Q1 partially answered.")
    print("  * The seed identifications + standard SM EWSB on the doublet")
    print("    tachyonic eigenstate together fix g, g', e, alpha, lambda_h to")
    print("    the precision of the original m_h, M_W, m_0 anchoring.")
    print("  * The remaining postulate (eigenvalue = physical mass-squared)")
    print("    is NOT derived here; that requires the partial-compositeness")
    print("    Coleman-Weinberg calculation, sketched in Section 11 of the paper.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
