#!/usr/bin/env python3
"""M_W tension and anchor-choice analysis.

(a) Check whether the dV positive-root M_W prediction is consistent with
    PDG average vs the CDF 2022 measurement.

(b) Re-anchor the dV construction by M_W rather than M_Z, and check whether
    the m_h prediction is anchor-independent.

(c) Verify the closed-form identity for m_h^2 / M_Z^2.
"""

import sympy as sp
import math

sqrt = sp.sqrt
N = sp.N

# Closed-form dV ratios (from previous cycles)
r_W_dV   = (sqrt(57) - 3) / 8 / (sqrt(3) - 1)              # M_W^2 / M_Z^2
r_W_dV   = sp.simplify(r_W_dV)
r_F0_dV  = (sqrt(3) + 1) / (sqrt(3) - 1)                   # M_F0^2 / M_Z^2 = 2+sqrt(3)
r_H0_dV  = ((sqrt(57) + 3) / 8) / (sqrt(3) - 1)
r_W_dV_num = float(r_W_dV)
r_F0_num   = float(r_F0_dV)
r_H0_num   = float(r_H0_dV)

# (a) M_W tension
print('=== (a) M_W comparison ===')
M_Z = 91.1876
MW_dV_pred = M_Z * math.sqrt(r_W_dV_num)
MW_PDG = 80.369
MW_PDG_err = 0.013
MW_CDF = 80.4335
MW_CDF_err = 0.0094
print(f'  dV positive root prediction: M_W = {MW_dV_pred:.6f} GeV')
print(f'  PDG average:                M_W = {MW_PDG} +- {MW_PDG_err} GeV')
print(f'  CDF 2022:                   M_W = {MW_CDF} +- {MW_CDF_err} GeV')
print(f'  dV - PDG = {MW_dV_pred - MW_PDG:+.4f} GeV ({(MW_dV_pred-MW_PDG)/MW_PDG_err:+.2f} sigma)')
print(f'  dV - CDF = {MW_dV_pred - MW_CDF:+.4f} GeV ({(MW_dV_pred-MW_CDF)/MW_CDF_err:+.2f} sigma)')
print()
print('  Conclusion: dV positive root is consistent with PDG within 1 sigma')
print('  but in ~6 sigma tension with CDF.  If CDF is correct, the dV')
print('  positive root prediction is falsified at 5+ sigma.')

# (b) Re-anchor by M_W^pole and re-derive
print()
print('=== (b) Re-anchor by M_W rather than M_Z ===')
# Anchor: Mcal^2 x_{1/2,+} = M_W^2 (PDG)
# Then M_Z^2 = Mcal^2 x_{1,+} = M_W^2 / r_W_dV
print('Using anchor M_W = 80.369 GeV (PDG):')
Mcal_W_anchor_sq = MW_PDG**2 / float((sqrt(57)-3)/8)
Mcal_W_anchor = math.sqrt(Mcal_W_anchor_sq)
print(f'  Mcal (from M_W anchor) = {Mcal_W_anchor:.4f} GeV')
MZ_W_anchor = math.sqrt(Mcal_W_anchor_sq * float(sqrt(3)-1))
print(f'  predicted M_Z          = {MZ_W_anchor:.6f} GeV')
print(f'  PDG M_Z                = {M_Z} GeV')
print(f'  diff                   = {MZ_W_anchor - M_Z:+.4f} GeV')

# m_h prediction from M_W anchor:
MH0_W_sq = Mcal_W_anchor_sq * float((sqrt(57)+3)/8)
gap_W = MZ_W_anchor**2 - MW_PDG**2
mh_W_anchor_sq = MH0_W_sq + 0.375 * gap_W
mh_W_anchor = math.sqrt(mh_W_anchor_sq)
print(f'  predicted m_h (3/8 corr) = {mh_W_anchor:.4f} GeV')
print(f'  PDG m_h                  = 125.20 +- 0.11 GeV')
print(f'  diff                     = {mh_W_anchor - 125.20:+.4f} GeV')

# Anchor by m_h instead.
# m_h^2 = Mcal^2 * [ -x_{1/2,-} + (3/8)(x_{1,+} - x_{1/2,+}) ]
print()
print('Using anchor m_h = 125.20 GeV (PDG):')
xhm_val = float(-(sqrt(57)+3)/8)
delta_x = float((sqrt(3)-1) - (sqrt(57)-3)/8)
r_mh_in_Mcal = (-xhm_val) + 0.375 * delta_x
Mcal_h_anchor_sq = 125.20**2 / r_mh_in_Mcal
MZ_h_anchor = math.sqrt(Mcal_h_anchor_sq * float(sqrt(3)-1))
MW_h_anchor = math.sqrt(Mcal_h_anchor_sq * float((sqrt(57)-3)/8))
print(f'  Mcal (from m_h anchor) = {math.sqrt(Mcal_h_anchor_sq):.4f} GeV')
print(f'  predicted M_Z          = {MZ_h_anchor:.6f} GeV  (PDG: 91.1876)')
print(f'  predicted M_W          = {MW_h_anchor:.6f} GeV  (PDG: 80.369)')
print(f'  diff M_Z               = {MZ_h_anchor - M_Z:+.4f} GeV')
print(f'  diff M_W               = {MW_h_anchor - MW_PDG:+.4f} GeV')
print('  -> m_h anchor reproduces M_Z and M_W to similar precision.  The')
print('     fit is consistent regardless of which observable we anchor on,')
print('     reinforcing the post-dictive character (no observable is')
print('     dynamically privileged).')

# (c) Verify the closed-form m_h formula symbolically
print()
print('=== (c) Symbolic verification of m_h^2/M_Z^2 closed form ===')
r_mh_direct = sp.simplify(((sqrt(57)+3)/8)/(sqrt(3)-1)
                          + sp.Rational(3,8) * (1 - (sqrt(57)-3)/8/(sqrt(3)-1)))
print('  derived formula:', sp.expand(r_mh_direct))
target = (15*sqrt(19) + 33*sqrt(3) + 5*sqrt(57) + 81)/128
print('  target          :', sp.expand(target))
print('  difference      :', sp.simplify(r_mh_direct - target))
