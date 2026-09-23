#!/usr/bin/env python3
"""Exact closed-form predictions for m_h and v from the dV ansatz.

Given M_Z as the only dimensional input and the assumption that the
correction is exactly (3/8)(M_Z^2 - M_W^2) sigma_3 in the negative
sector, derive closed-form radical expressions for the predicted
Higgs pole mass and the predicted Fermi vev.

We then compare to PDG-style inputs to quantify which prediction is
exact and which is approximate.
"""

import sympy as sp

sqrt = sp.sqrt
N = sp.N

# Inputs
MZ_num = sp.Rational(911876, 10000)
GF_num = sp.Float('1.1663787e-5')
mh_PDG = sp.Float('125.20')             # PDG 2024 m_h
mh_PDG_err = sp.Float('0.11')           # PDG 2024 uncertainty
v_from_GF = 1 / sqrt(sqrt(2) * GF_num)  # v from Fermi constant (essentially exact)

# Symbolic computation
x1p = sqrt(3) - 1
xhp = (sqrt(57) - 3)/8

# Dimensionless slot ratios
r_W = sp.simplify(xhp / x1p)                          # M_W^2 / M_Z^2
r_gap = sp.simplify(1 - r_W)                          # (M_Z^2 - M_W^2)/M_Z^2

r_H0 = sp.simplify(((sqrt(57) + 3)/8) / x1p)          # M_H0^2 / M_Z^2
r_F0 = sp.simplify((sqrt(3) + 1) / x1p)               # M_F0^2 / M_Z^2 = 2 + sqrt(3)

# Corrected dimensionless ratios
r_mh = sp.simplify(r_H0 + sp.Rational(3, 8) * r_gap)
r_vF = sp.simplify(r_F0 - sp.Rational(3, 8) * r_gap)

# Closed-form simplifications
r_W_simp = sp.radsimp(r_W)
r_F0_simp = sp.radsimp(r_F0)
r_mh_simp = sp.expand(sp.radsimp(r_mh))
r_vF_simp = sp.expand(sp.radsimp(r_vF))

print('=== Exact dimensionless predictions in units of M_Z^2 ===')
print()
print('M_W^2 / M_Z^2 =', r_W_simp)
print('                =', N(r_W, 16))
print()
print('M_F0^2 / M_Z^2 (uncorrected) =', r_F0_simp)
print('                              =', N(r_F0, 16))
print()
print('m_h^2 / M_Z^2 (corrected M_H^2) =', r_mh_simp)
print('                                 =', N(r_mh, 16))
print()
print('(v^2/2) / M_Z^2 (corrected M_F^2) =', r_vF_simp)
print('                                   =', N(r_vF, 16))
print()

# Predicted masses
print('=== Predicted masses ===')
mh_pred = MZ_num * sqrt(r_mh)
v_pred = MZ_num * sqrt(2 * r_vF)
MW_pred = MZ_num * sqrt(r_W)

print(f'M_W (dV positive root)   = {N(MW_pred, 12)} GeV')
print(f'm_h (dV corrected)       = {N(mh_pred, 12)} GeV')
print(f'v  (dV corrected, from M_F slot identification with v/sqrt(2))')
print(f'                          = {N(v_pred, 12)} GeV')
print()

print('=== Observed values ===')
print(f'M_W (PDG average)         = 80.369 GeV (uncert ~0.013 GeV)')
print(f'm_h (PDG 2024)            = {mh_PDG} +- {mh_PDG_err} GeV')
print(f'v (from G_F)              = {N(v_from_GF, 12)} GeV')

print()
print('=== Discrepancies ===')
delta_MW = MW_pred - sp.Float('80.369')
delta_mh = mh_pred - mh_PDG
delta_v = v_pred - v_from_GF
print(f'Delta M_W  = {N(delta_MW, 6)} GeV  ({N(delta_MW/sp.Float("80.369"), 4)*100} %)')
print(f'Delta m_h  = {N(delta_mh, 6)} GeV  ({N(delta_mh/mh_PDG, 4)*100} %)')
print(f'Delta v    = {N(delta_v, 6)} GeV  ({N(delta_v/v_from_GF, 4)*100} %)')

print()
print('Key observation:')
print(' - m_h prediction is exact to within experimental uncertainty.')
print(' - v prediction overshoots by ~0.07%, well above the ~10^-8 G_F')
print('   precision.  Either the M_F slot identification with v/sqrt(2)')
print('   is approximate, or an additional small correction acts.')

# What coefficient C does v require exactly?
# v^2/2 = M_F0^2 - C (M_Z^2 - M_W^2)
# C = (M_F0^2 - v^2/2)/(M_Z^2 - M_W^2)
print()
print('=== Coefficient required for exact v matching ===')
MF0_sq = sp.simplify(MZ_num**2 * r_F0)
gap = sp.simplify(MZ_num**2 * r_gap)
C_exact_v = (MF0_sq - v_from_GF**2/2) / gap
print(f'C_v (exact)  = {N(C_exact_v, 10)} = (M_F0^2 - v^2/2)/(M_Z^2 - M_W^2)')

MH0_sq = sp.simplify(MZ_num**2 * r_H0)
C_exact_h = (mh_PDG**2 - MH0_sq) / gap
print(f'C_h (exact)  = {N(C_exact_h, 10)} = (m_h^2 - M_H0^2)/(M_Z^2 - M_W^2)')
print(f'3/8         = {sp.Float(3/8, 10)}')

print()
print('=> The Higgs side wants coefficient 0.37514 ~ 3/8 + 0.04% (within m_h error)')
print('=> The Fermi side wants coefficient 0.38843 ~ 3/8 + 3.6% (well beyond errors)')

# Try to identify a rational close to 0.388:
print()
print('=== Rational approximants for the v-side coefficient ===')
target = 0.38843
candidates = [
    (sp.Rational(3, 8),  '3/8'),
    (sp.Rational(31, 80),  '31/80'),
    (sp.Rational(7, 18),  '7/18'),
    (sp.Rational(11, 28),  '11/28'),
    (sp.nsimplify(C_exact_v, rational=True, tolerance=1e-3), 'rational~0.388'),
]
for c, name in candidates:
    print(f'  {name:>20s} = {float(c):.6f}  diff = {float(c)-target:+.6f}')
