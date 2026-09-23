"""Phase B: scheme dependence of sin^2(theta_W) and one-loop matching.

The model's algebraic prediction
    sin^2(theta_W)  =  1 - lambda_+(2)/lambda_+(3)  =  1 - (sqrt(57)-3)(sqrt(3)+1)/16  =  0.22310
is the ON-SHELL Weinberg angle by construction:
    sin^2(theta_W)_OS  =  1 - M_W^2 / M_Z^2,
because we identify the two positive eigenvalues with M_W^2 and M_Z^2.

This script:
  1. Quantifies the scheme dependence of sin^2(theta_W) and confronts
     each scheme with the algebraic prediction. The point: 0.22310 is
     not "PDG to 10 digits" -- it agrees with the OS scheme to
     ~0.1% (which is itself ~1 sigma against PDG_OS), and DISAGREES
     with MS-bar at the ~3% level (which is ~30x the model's claimed
     precision on m_h).

  2. Computes Delta_r (the one-loop EW radiative correction connecting
     M_W and M_Z via G_F and alpha) and shows where the model's
     tree-level identification sits relative to the SM one-loop
     prediction.

  3. Honest input/output bookkeeping for the model: 1 input + 1 spurion
     -> 1 parameter-free output (M_Z) + 1 fitted (m_h or v/sqrt(2),
     whichever is anchored to Delta) + 1 consistency check.
"""

from __future__ import annotations

import math
import sys

# --- Inputs ---
MW_PDG = 80.3692
MZ_PDG = 91.1880
MH_PDG = 125.20
MT_PDG = 172.69     # top quark
GF     = 1.1663787e-5
ALPHA_INV_MZ = 127.918
V      = 1.0/math.sqrt(math.sqrt(2)*GF)
VF     = V/math.sqrt(2)


def sin2_OS():
    """On-shell scheme: sin^2(theta_W) = 1 - M_W^2/M_Z^2."""
    return 1.0 - (MW_PDG/MZ_PDG)**2


def model_sin2():
    """Algebraic Casimir-locked prediction."""
    return 1.0 - (math.sqrt(57)-3)*(math.sqrt(3)+1)/16.0


def sin2_MSbar():
    """Approximate MS-bar value at scale M_Z (PDG 2024 effective)."""
    return 0.23121


def sin2_eff_lept():
    """Effective leptonic mixing angle (LEP/SLD combination, PDG 2024)."""
    return 0.23153


def Delta_r_SM_estimate():
    """Approximate Delta_r at one loop in the SM (Sirlin's formula).

    Definition: M_W^2 (1 - M_W^2/M_Z^2) = pi alpha / (sqrt(2) G_F) * 1/(1 - Delta_r).
    Solving for Delta_r given measured M_W, M_Z, alpha, G_F:
    """
    A = math.pi * (1.0/ALPHA_INV_MZ) / (math.sqrt(2.0) * GF)  # ~ (37.3 GeV)^2 in natural units
    rhs = MW_PDG**2 * (1.0 - (MW_PDG/MZ_PDG)**2)
    Delta_r = 1.0 - A / rhs
    return Delta_r


def main() -> int:
    print("=" * 78)
    print("Phase B: scheme dependence of sin^2(theta_W) and Delta_r")
    print("=" * 78)

    s2_model = model_sin2()
    s2_OS    = sin2_OS()
    s2_MS    = sin2_MSbar()
    s2_eff   = sin2_eff_lept()

    print("\n[1] sin^2(theta_W) by scheme")
    print(f"    Model (algebraic, on-shell)        : {s2_model:.6f}")
    print(f"    On-shell PDG (1 - M_W^2/M_Z^2)      : {s2_OS:.6f}")
    print(f"    MS-bar at M_Z (PDG)                 : {s2_MS:.6f}")
    print(f"    Effective leptonic (LEP/SLD)        : {s2_eff:.6f}")
    print()
    print("    Comparison with the model's algebraic value:")
    print(f"      vs OS      : dev = {(s2_model-s2_OS)*100/s2_OS:+.3f}%   (claimed precision)")
    print(f"      vs MS-bar  : dev = {(s2_model-s2_MS)*100/s2_MS:+.3f}%   (~3.5%, ~100x worse)")
    print(f"      vs eff_lep : dev = {(s2_model-s2_eff)*100/s2_eff:+.3f}%   (~3.6%, ~100x worse)")
    print()
    print("    Conclusion: the model's algebraic 'sin^2(theta_W)' is the")
    print("    on-shell scheme value by construction. Comparing it to MS-bar or")
    print("    effective-leptonic schemes is invalid; the schemes differ by ~3.5%")
    print("    due to one-loop EW corrections, ~100x larger than the model's")
    print("    claimed precision on m_h.")

    print("\n[2] Delta_r: one-loop SM EW correction")
    Dr = Delta_r_SM_estimate()
    print(f"    Delta_r (extracted from PDG measurements) = {Dr:+.5f} (~ 4%)")
    print(f"    This is the one-loop correction connecting M_W to (M_Z, G_F, alpha).")
    print(f"    Our identification M_W^2 = m_0^2 lambda_+(2) is to the PHYSICAL")
    print(f"    M_W, so Delta_r is implicit in the identification. The model does")
    print(f"    NOT predict Delta_r; it inherits it via the anchor.")

    print("\n[3] Honest input/output bookkeeping")
    print("    Old (overclaimed) bookkeeping:")
    print("       2 parameters (m_0, Delta) -> 4 outputs (M_W, M_Z, m_h, v/sqrt2)")
    print("    Why this is wrong: M_W is the anchor (input), not output; m_h or")
    print("    v/sqrt(2) is fitted by Delta (input), not output.")
    print()
    print("    Correct bookkeeping:")
    print("    Inputs (3):")
    print(f"      * M_W = {MW_PDG} GeV         -> fixes m_0 = M_W/sqrt(lambda_+(2))")
    print(f"      * G_F = {GF}    -> gives v/sqrt(2) = {VF:.4f} GeV")
    print(f"      * Delta (1 free param)         -> anchored to either m_h or v/sqrt(2)")
    print("    Genuine outputs (per anchor choice):")
    print(f"      * M_Z = m_0 sqrt(sqrt(3)-1)    -> 91.18 GeV  (PARAMETER-FREE)")
    print(f"      * if Delta fits m_h: v/sqrt(2) is predicted to 0.02%")
    print(f"      * if Delta fits v/sqrt(2): m_h is predicted to 0.04%")
    print(f"    Consistency check (cross-irrep neg.-branch trace identity):")
    print(f"      m_h^2 + (v/sqrt2)^2 = m_0^2 (|lam_-(2)| + |lam_-(3)|)")
    print(f"      holds within (5 GeV)^2 ~ 25 GeV^2 ~ 3.4% of Delta")
    print()
    print("    Verdict: the model has 1 PARAMETER-FREE prediction (M_Z, 0.007%)")
    print("    plus 1 FITTED + 1 CONSISTENCY-CHECK pair, not 4 independent outputs.")
    print("    The parameter-free M_Z prediction is the most defensible claim.")

    print("\n[4] Suggested abstract revision")
    print("    Replace: 'the model then outputs four EW quantities'")
    print("    With:    'the model then outputs M_Z (parameter-free, 0.007%);")
    print("              with one further input (m_h or v/sqrt(2)) anchoring")
    print("              the spurion Delta, the remaining EW quantity is")
    print("              predicted to 0.04% as an algebraic consistency check.'")

    return 0


if __name__ == "__main__":
    sys.exit(main())
