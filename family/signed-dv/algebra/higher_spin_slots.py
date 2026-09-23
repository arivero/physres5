#!/usr/bin/env python3
"""Higher-spin signed-root slots of the dV quadratic.

For each spin s, the roots are
    x_{s,pm} = ( -C_s pm sqrt(C_s (C_s+4)) ) / 2,  with C_s = s(s+1).

Using the same Mcal that fixes M_Z = Mcal sqrt(x_{1,+}), tabulate the
masses for s = 0, 1/2, 1, 3/2, 2, 5/2, 3 and compare against known SM
mass scales (M_Z, M_W, m_h, v/sqrt(2), m_t, m_b, m_tau, top Yukawa).

Question: do the s = 3/2, 2, ... slots correspond to any known particle
masses, or are they empty?
"""

import sympy as sp

sqrt = sp.sqrt
N = sp.N

MZ = sp.Rational(911876, 10000)
x1p = sqrt(3) - 1
Mcal = MZ / sqrt(x1p)

spins = [
    sp.Rational(0), sp.Rational(1, 2), sp.Rational(1),
    sp.Rational(3, 2), sp.Rational(2), sp.Rational(5, 2), sp.Rational(3)
]

print('Mcal =', N(Mcal, 12), 'GeV')
print()
print(f"{'s':>4s} {'C_s':>10s}   {'x_+':>14s}   {'x_-':>14s}   "
      f"{'M_+ (GeV)':>14s}  {'M_- = sqrt(-x_-)*Mcal (GeV)':>30s}")
print('-' * 100)
for s in spins:
    C = s * (s + 1)
    if C == 0:
        xp = xm = sp.Integer(0)
    else:
        xp = (-C + sqrt(C*(C+4)))/2
        xm = (-C - sqrt(C*(C+4)))/2
    Mp = sqrt(xp) * Mcal if xp >= 0 else sp.nan
    Mm = sqrt(-xm) * Mcal if xm <= 0 else sp.nan
    print(f"{str(s):>4s} {str(C):>10s}   {str(N(xp,10)):>14s}   {str(N(xm,10)):>14s}   "
          f"{str(N(Mp,10)):>14s}  {str(N(Mm,10)):>14s}")

# Reference SM masses (GeV)
print()
print('Reference SM masses (PDG 2024-ish):')
refs = {
    'M_Z': 91.1876,
    'M_W (PDG average)': 80.369,
    'm_h': 125.20,
    'v/sqrt(2)': 174.10358,
    'm_t (pole)': 172.69,
    'm_t (MS-bar)': 162.5,
    'm_b (pole, ish)': 4.78,
    'm_tau': 1.77686,
    '2 v/sqrt(2) = v': 246.219651,
}
for k, val in refs.items():
    print(f'  {k:25s} {val:>10.4f} GeV')

# Try to identify near-coincidences with the higher-spin slots
print()
print('Near-coincidences search (slot vs SM particle, |M-M_SM|<5 GeV):')
sm_masses = [
    ('M_Z', 91.1876),
    ('M_W', 80.369),
    ('m_h', 125.20),
    ('v/sqrt2', 174.10358),
    ('m_t pole', 172.69),
]
for s in spins:
    C = s * (s + 1)
    if C == 0:
        continue
    xp = (-C + sqrt(C*(C+4)))/2
    xm = (-C - sqrt(C*(C+4)))/2
    Mp = float(sqrt(xp) * Mcal)
    Mm = float(sqrt(-xm) * Mcal)
    for name, mval in sm_masses:
        if abs(Mp - mval) < 5:
            print(f'  s={s}: M_+ = {Mp:.4f} GeV close to {name} ({mval}); diff = {Mp-mval:+.4f}')
        if abs(Mm - mval) < 5:
            print(f'  s={s}: M_- = {Mm:.4f} GeV close to {name} ({mval}); diff = {Mm-mval:+.4f}')

print()
print('Conclusion:')
print('- Only s = 1 and s = 1/2 slots produce near-coincidences with')
print('  known electroweak scales.  Higher-spin slots (s = 3/2, 2, ...)')
print('  do not match any known particle masses within ~5 GeV.')
print('- This reinforces that the dV structure is electroweak-specific:')
print('  it picks out the spin-1 (gauge) and spin-1/2 (fermion / doublet')
print('  Higgs) slots only.  No "tower" interpretation is supported.')
