#!/usr/bin/env python3
"""Precision decomposition of the negative-sector correction.

We split the dV correction
    Delta_H = m_h^2 - M_H^(0)^2
    Delta_F = (v^2/2) - M_F^(0)^2
into a traceless sigma_3 part and a residual trace part:
    Delta_H = eps_t + eps_s
    Delta_F = -eps_t + eps_s
where eps_t = (Delta_H - Delta_F)/2 is the traceless coefficient and
eps_s = (Delta_H + Delta_F)/2 is the residual trace.

If the proposed correction (3/8)(M_Z^2 - M_W^2) sigma_3 were exact,
eps_t/(M_Z^2 - M_W^2) would equal 3/8 = 0.375 and eps_s would vanish.
"""

import sympy as sp

sqrt = sp.sqrt
N = sp.N

# Inputs
MZ = sp.Rational(911876, 10000)
mh = sp.Float("125.20")
GF = sp.Float("1.1663787e-5")

x1p = sqrt(3) - 1
x1m = -(sqrt(3) + 1)
xhp = (sqrt(57) - 3)/8
xhm = -(sqrt(57) + 3)/8
Mcal = MZ / sqrt(x1p)
MW0 = Mcal * sqrt(xhp)
MH0 = Mcal * sqrt(-xhm)
MF0 = Mcal * sqrt(-x1m)

v = 1 / sqrt(sqrt(2) * GF)
vF2 = v**2 / 2

gap = MZ**2 - MW0**2

DeltaH = mh**2 - MH0**2
DeltaF = vF2 - MF0**2

eps_t = (DeltaH - DeltaF) / 2     # traceless part
eps_s = (DeltaH + DeltaF) / 2     # residual trace part

print('=== Inputs ===')
print(f'M_Z          = {N(MZ, 12)} GeV')
print(f'M_W0 (dV)    = {N(MW0, 12)} GeV')
print(f'M_H0 (dV)    = {N(MH0, 12)} GeV')
print(f'M_F0 (dV)    = {N(MF0, 12)} GeV')
print(f'm_h          = {mh} GeV  (PDG 2024 input)')
print(f'v/sqrt(2)    = {N(v/sqrt(2), 12)} GeV  (from G_F)')

print()
print('=== Deltas ===')
print(f'Delta_H = m_h^2 - M_H0^2         = {N(DeltaH, 8)} GeV^2')
print(f'Delta_F = v^2/2 - M_F0^2         = {N(DeltaF, 8)} GeV^2')
print(f'Delta_H + Delta_F                = {N(DeltaH+DeltaF, 8)} GeV^2')
print(f'M_Z^2 - M_W0^2                    = {N(gap, 8)} GeV^2')

print()
print('=== Decomposition into traceless + trace ===')
print(f'eps_t (traceless, sigma_3)        = {N(eps_t, 8)} GeV^2')
print(f'eps_s (trace, identity)           = {N(eps_s, 8)} GeV^2')
print(f'eps_t / (M_Z^2 - M_W^2)           = {N(eps_t/gap, 10)}')
print(f'eps_s / (M_Z^2 - M_W^2)           = {N(eps_s/gap, 10)}')
print(f'3/8 (target)                      = {N(sp.Rational(3,8), 10)}')

print()
print('=== Departure from (3/8)*sigma_3 ===')
dev = eps_t/gap - sp.Rational(3, 8)
print(f'Departure of eps_t coefficient from 3/8: {N(dev, 6)}')
print(f'eps_t = (3/8) * gap * (1 + delta) with delta = {N(dev/sp.Rational(3,8), 6)}')

# Express eps_s as a fraction of eps_t
print(f'eps_s / eps_t                     = {N(eps_s/eps_t, 6)}')

print()
print('=== Implications ===')
print(' * The dominant correction is indeed traceless and very close to')
print('   (3/8)(M_Z^2 - M_W^2): coefficient 0.3818 vs target 0.3750.')
print(' * The departure is ~1.8% of the target, suggesting either a')
print('   higher-order custodial-breaking correction or a small additional')
print('   common-mode shift.')
print(' * The residual trace eps_s ~ -12 GeV^2 is small (~1.7% of eps_t)')
print('   and could be a real physical effect (a singlet/common-mode')
print('   shift in the negative sector).')
print(' * Plausibly the correct phenomenological ansatz is:')
print('       Delta M_-^2 = (3/8)(M_Z^2 - M_W^2) sigma_3 + eps_s * 1,')
print('   with eps_s a separate (much smaller) custodial-symmetric shift.')

# Try the alternative ansatz: (M_Z^2 - M_W^2) sigma_3 with coefficient
# chosen to match m_h exactly (i.e. fit eps_t to Delta_H), and predict
# Delta_F from that.
ct_fit = DeltaH / gap
print()
print('=== Alternative: fit coefficient to m_h, predict v/sqrt(2) shift ===')
print(f'fit coefficient (from Delta_H)    = {N(ct_fit, 10)}')
print(f'predicted (-eps_t)                = {N(-ct_fit*gap, 8)} GeV^2')
print(f'observed   Delta_F                = {N(DeltaF, 8)} GeV^2')
print(f'discrepancy                       = {N(-ct_fit*gap - DeltaF, 8)} GeV^2')
print('Note: fitting eps_t to Delta_H gives coefficient 0.375 (= 3/8) to 4 digits!')
print('-> The m_h match is essentially exact under (3/8)*sigma_3.')
print('-> The v/sqrt(2) match has a ~25 GeV^2 surplus on the M_F side.')

# Print a cleanly formatted scoreboard
print()
print('=== Match scoreboard (mass-squared level, in GeV^2) ===')
print(f' slot       target           dV (corr)         absolute err   rel err')
print(f' M_Z^2     {float(MZ**2):>12.4f}     {float(MZ**2):>12.4f}     {0:>12.4f}    {0:>+.2e}')
print(f' M_W^2     {(80.379**2):>12.4f}     {float(MW0**2):>12.4f}     {(float(MW0**2)-80.379**2):>12.4f}    {(float(MW0**2)/80.379**2-1):>+.2e}')
print(f' m_h^2     {float(mh**2):>12.4f}     {float(MH0**2 + sp.Rational(3,8)*gap):>12.4f}     {(float(MH0**2 + sp.Rational(3,8)*gap)-float(mh**2)):>12.4f}    {(float(MH0**2 + sp.Rational(3,8)*gap)/float(mh**2)-1):>+.2e}')
print(f' v^2/2     {float(vF2):>12.4f}     {float(MF0**2 - sp.Rational(3,8)*gap):>12.4f}     {(float(MF0**2 - sp.Rational(3,8)*gap)-float(vF2)):>12.4f}    {(float(MF0**2 - sp.Rational(3,8)*gap)/float(vF2)-1):>+.2e}')
