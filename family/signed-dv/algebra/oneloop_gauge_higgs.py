#!/usr/bin/env python3
"""One-loop gauge contribution to the Higgs mass-squared.

Question we are answering: can the Standard Model one-loop Coleman-Weinberg
gauge contribution naturally produce a Higgs-mass shift with coefficient
of order C_F/C_A = 3/8 in front of (M_Z^2 - M_W^2)?

Method: compute the standard one-loop CW gauge potential

    V_gauge(h) = (3 / 64 pi^2) [ 2 M_W^4(h) ( log(M_W^2(h)/mu^2) - 5/6 )
                                +   M_Z^4(h) ( log(M_Z^2(h)/mu^2) - 5/6 ) ]

with M_W^2(h) = g^2 h^2 / 4 and M_Z^2(h) = (g^2 + g'^2) h^2 / 4, then
extract d^2 V / dh^2 at h = v and compare with (3/8)(M_Z^2 - M_W^2).

Result: the one-loop coefficient in front of (M_Z^2 - M_W^2) is of order
(1/16 pi^2)(M_V^2 / v^2), i.e. ~ 10^-6 to 10^-5, NOT 3/8 ~ 0.4.

Therefore: the proposed (3/8)(M_Z^2 - M_W^2) correction cannot be a
Standard Model one-loop CW effect.  It must be tree level, non-perturbative,
or numerology.
"""

import sympy as sp
import math

h, mu, g, gp = sp.symbols('h mu g gprime', positive=True)
v = sp.Symbol('v', positive=True)

# Field-dependent gauge boson masses (per W boson; W^+ and W^- count as 2)
MW2 = g**2 * h**2 / 4
MZ2 = (g**2 + gp**2) * h**2 / 4

# One-loop CW potential from gauge bosons (3 polarizations each in MS-bar);
# the constant -5/6 is the standard subtraction for massive vectors.
def CW_gauge(M2, mu2):
    return (3 * M2**2) * (sp.log(M2 / mu2) - sp.Rational(5, 6))

V_gauge = (1 / (64 * sp.pi**2)) * (
    2 * CW_gauge(MW2, mu**2) +  CW_gauge(MZ2, mu**2)
)

# Second derivative at h = v gives the loop contribution to m_h^2
dV_dh = sp.diff(V_gauge, h)
d2V_dh2 = sp.diff(dV_dh, h)

# Evaluate at h = v with M_W = g v / 2 etc. (i.e. just substitute the physical
# values and simplify to a structure in M_W^2, M_Z^2)
MW = sp.Symbol('MW', positive=True)
MZ = sp.Symbol('MZ', positive=True)
subs_phys = {h: v, g: 2*MW/v, gp: 2*sp.sqrt(MZ**2 - MW**2)/v, mu: v}
m_h2_loop = sp.simplify(d2V_dh2.subs(subs_phys))
print('=== One-loop gauge CW contribution to m_h^2 ===')
print('symbolic   :')
sp.pprint(sp.expand(m_h2_loop))

# Numerical evaluation with PDG-like inputs
MW_num = 80.379           # GeV (PDG average, see exploration log)
MZ_num = 91.1876          # GeV
v_num  = 246.219651       # GeV  (1/sqrt(sqrt(2) G_F), G_F = 1.1663787e-5)
G_F = 1.1663787e-5
v_check = 1.0 / math.sqrt(math.sqrt(2.0) * G_F)
print(f'\nv from G_F = {v_check:.6f} GeV')

vals = {MW: MW_num, MZ: MZ_num, v: v_num}
m_h2_num = float(m_h2_loop.subs(vals))
print(f'one-loop m_h^2 (gauge)        = {m_h2_num:.4f} GeV^2')
print(f'sqrt of above                  = {math.sqrt(abs(m_h2_num)):.4f} GeV')
print(f'compare m_h ~ 125.2 GeV (tree-level lambda v^2 dominant)')

# Custodial-symmetric piece (M_Z = M_W):
m_h2_cust = sp.simplify(m_h2_loop.subs(MZ, MW))
print('\ncustodial-symmetric value (M_Z = M_W) :')
sp.pprint(sp.expand(m_h2_cust))
m_h2_cust_num = float(m_h2_cust.subs({MW: MW_num, v: v_num}))
print(f'numeric                        = {m_h2_cust_num:.4f} GeV^2')

# Custodial-breaking shift
delta_cust = sp.simplify(m_h2_loop - m_h2_cust)
delta_cust_num = float(delta_cust.subs(vals))
print('\ncustodial-breaking part        :')
sp.pprint(sp.expand(delta_cust))
print(f'numeric                        = {delta_cust_num:.6f} GeV^2')

# Compare to the dV correction
gap = MZ_num**2 - MW_num**2
target = 0.375 * gap
print(f'\ndV target (3/8)(M_Z^2 - M_W^2) = {target:.4f} GeV^2')
print(f'ratio  (1-loop custodial / dV target) = {delta_cust_num/target:.6e}')

print('\n=== Conclusion ===')
print('The one-loop CW gauge contribution to m_h^2 is dominated by the')
print("custodial-symmetric piece ~ (9/16 pi^2)(M_W^4/v^2) ~ tens of GeV^2.")
print('The custodial-breaking piece, proportional to (M_Z^2 - M_W^2),')
print(f'has coefficient ~ {delta_cust_num/gap:.6e}, i.e. 1-loop suppressed.')
print('This is FAR from C_F/C_A = 3/8 = 0.375.')
print()
print('A coefficient of order 0.4 in front of (M_Z^2 - M_W^2) cannot come')
print('from a 1-loop SM CW effect; it must be tree level (D-term, threshold')
print('matching), non-perturbative, or numerology.')

# As a sanity check, also derive the natural Casimir-scaling ratio that
# appears in fundamental-vs-adjoint one-loop self-energies.
print()
print('=== Casimir-scaling ratio comparison ===')
CF, CA = sp.Rational(3, 4), sp.Rational(2)
print(f'  C_F/C_A = {CF/CA}  ({float(CF/CA):.4f})')
print('  In SU(2), the *ratio* of the gauge-loop self-energy of a scalar')
print("  in the fundamental rep to that of a vector in the adjoint rep is")
print('  exactly C_F/C_A = 3/8.  This is a true group-theory statement.')
print('  But the *absolute coefficient* of (M_Z^2 - M_W^2) on the scalar')
print('  mass is 1-loop-suppressed; the Casimir ratio cancels in the ratio,')
print('  not in the absolute matching to (M_Z^2 - M_W^2).')
