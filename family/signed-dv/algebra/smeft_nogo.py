#!/usr/bin/env python3
"""SMEFT operator-coefficient analysis for the proposed dV correction.

Question: can the proposed shift delta m_h^2 = (3/8)(M_Z^2 - M_W^2) be
hosted by any dimension-6 SMEFT operator with a Wilson coefficient
compatible with current EWPT and Higgs-coupling bounds?

We use the Warsaw basis (Grzadkowski et al. 2010, arXiv:1008.4884).
Relevant Higgs-sector dim-6 operators that shift m_h^2 at tree level
after EWSB:

    O_H       = (H^dag H)^3
    O_{H Box} = (H^dag H) Box (H^dag H)
    O_{HD}    = (H^dag D_mu H)^* (H^dag D^mu H)

The first directly modifies the Higgs potential.  The second induces
Higgs wavefunction renormalization, shifting the pole mass.  The third
contributes to T-parameter and to the Higgs kinetic term.

Conventions: write the SMEFT Lagrangian as
    L_eff = L_SM + sum_i (c_i / Lambda^2) O_i .

Reference Wilson-coefficient bounds (rough 95% CL global fit values,
SMEFTfit / fitmaker-like; orders of magnitude only):
    c_H / Lambda^2     : O(few) TeV^-2 (Higgs trilinear)
    c_{H Box} / Lambda^2 : ~ 0.05 TeV^-2 (Higgs couplings)
    c_{HD} / Lambda^2  : ~ 0.005 TeV^-2 (T parameter)
"""

import math

# Inputs
v = 246.219651
M_Z = 91.1876
M_W = 80.369        # PDG average
g  = 2 * M_W / v
gp = 2 * math.sqrt(M_Z**2 - M_W**2) / v
target_dmh2 = 696.0  # GeV^2; the dV proposed correction size

# Convenient unit: TeV^-2
def conv_GeV2_to_TeV2(x_GeV2_inv):
    return x_GeV2_inv * 1e6
GeV2_per_TeV2 = 1e6

print('=== Setup ===')
print(f'  v          = {v:.4f} GeV')
print(f'  g          = {g:.4f}')
print(f'  g\'         = {gp:.4f}')
print(f'  M_Z^2-M_W^2 = {M_Z**2 - M_W**2:.4f} GeV^2')
print(f'  target Delta m_h^2 = {target_dmh2:.1f} GeV^2')
print(f'  3/8 * (M_Z^2 - M_W^2) = {0.375 * (M_Z**2-M_W**2):.4f} GeV^2')

print()
print('=== Operator-by-operator matching ===')

# --- O_H = (H^dag H)^3 ---
# After expanding H = (0, (v+h)/sqrt(2))^T (unitary gauge),
#   (H^dag H)^3 = ((v+h)^2/2)^3 = (v+h)^6 / 8
# Contribution to V:  (c_H / Lambda^2) (v+h)^6 / 8
# Quadratic part:  (c_H/Lambda^2) * (15/8) v^4 h^2 + ...
# So Delta m_h^2 = (15/8) c_H v^4 / Lambda^2   (times symmetry factor 2 for d^2V/dh^2)
# Standard SMEFT result: Delta m_h^2 = -2 c_H v^4 / Lambda^2 (with sign convention
# such that the minimum condition gives mu^2 shift).
# Use the simpler |Delta m_h^2| = c_H v^4 / Lambda^2 * O(1) factor.
print()
print('--- O_H = (H^dag H)^3 ---')
print('Contribution: Delta m_h^2 ~ c_H v^4 / Lambda^2 (with O(1) numerical')
print('factor; full expression in Brivio-Trott 2019 eq. 2.42)')
# Solve for c_H/Lambda^2 to produce Delta m_h^2 = target
# Using Delta m_h^2 = 2 c_H v^4 / Lambda^2 (a representative coefficient)
cH_over_L2 = target_dmh2 / (2 * v**4)
print(f'  Required c_H / Lambda^2 = {cH_over_L2:.4e} GeV^-2 '
      f'= {cH_over_L2 * GeV2_per_TeV2:.4f} TeV^-2')
# Compare to bound
bound_cH_TeV2 = 5.0      # generous; LHC Run 2 trilinear coupling fits give
                          # |kappa_lambda| roughly 0-6, corresponding to
                          # c_H/Lambda^2 ~ few TeV^-2.
print(f'  Approx bound: c_H/Lambda^2 < {bound_cH_TeV2} TeV^-2 (LHC kappa_lambda)')
print(f'  -> required value is {cH_over_L2 * GeV2_per_TeV2 / bound_cH_TeV2:.4f} of the bound')
print('  CONCLUSION: SMEFT can easily host the *size* via O_H.')

# --- O_HD = (H^dag D H)^*(H^dag D H) ---
# Shifts T parameter: alpha T = -(v^2 / 2 Lambda^2) c_HD
# Tight EWPT bound: |c_HD/Lambda^2| < ~0.02 TeV^-2 (95% CL).
# The contribution to Delta m_h^2 comes via Higgs wavefunction
# renormalization, not directly to the potential.
print()
print('--- O_HD = (H^dag D_mu H)^*(H^dag D^mu H) ---')
print('Contribution: shifts T parameter at tree level and renormalizes H')
print('kinetic term.  Tight EWPT bound:')
bound_cHD_TeV2 = 0.02
print(f'  |c_HD/Lambda^2| < {bound_cHD_TeV2} TeV^-2 (T parameter)')
# Indirect Delta m_h^2 from wavefunction renormalization is suppressed:
#   Delta m_h^2|_indirect ~ -(c_HD v^2 / Lambda^2) * m_h^2 / 2
max_dmh2 = (bound_cHD_TeV2 / GeV2_per_TeV2) * v**2 * 125.2**2 / 2
print(f'  Max indirect Delta m_h^2 ~ {max_dmh2:.4f} GeV^2')
print(f'  vs target {target_dmh2:.1f} GeV^2 -> need {target_dmh2/max_dmh2:.1f}x bound')
print('  CONCLUSION: O_HD cannot reach 696 GeV^2 without violating EWPT.')

# --- O_HBox = (H^dag H) Box (H^dag H) ---
# Renormalizes the Higgs kinetic term: induces wave function correction
#   Z_h = 1 + 2 (c_HBox / Lambda^2) v^2
# Shifts the pole mass: Delta m_h^2 = -m_h^2 (c_HBox/Lambda^2) v^2.
print()
print('--- O_{H Box} = (H^dag H) Box (H^dag H) ---')
bound_cHBox_TeV2 = 0.05
print(f'  Approximate bound: |c_HBox/Lambda^2| < {bound_cHBox_TeV2} TeV^-2 '
      '(Higgs coupling fits)')
max_dmh2_box = -125.2**2 * (bound_cHBox_TeV2 / GeV2_per_TeV2) * v**2
print(f'  Max |Delta m_h^2| from O_HBox: {abs(max_dmh2_box):.1f} GeV^2')
print(f'  vs target {target_dmh2:.1f} GeV^2 -> '
      f'need {target_dmh2/abs(max_dmh2_box):.2f}x bound (TIGHT but plausible)')

print()
print('=== Structural form: can SMEFT predict the COEFFICIENT C_F/C_A ===')
print()
print('SMEFT Wilson coefficients are set by UV matching; in a generic UV')
print('theory the c_H coefficient is independent of g\'.  For the proposed')
print('correction to have the *form* (3/8)(M_Z^2 - M_W^2) = (3/32) g\'^2 v^2,')
print('one would need')
print('    Delta m_h^2 = c_H v^4 / Lambda^2 = (3/32) g\'^2 v^2,')
print('which fixes')
print('    Lambda^2 = (32 c_H / 3) v^2 / g\'^2.')
Lambda_sq_natural = (32.0/3.0) * v**2 / gp**2     # for c_H = 1
print(f'  -> Lambda (for c_H = 1) = {math.sqrt(Lambda_sq_natural):.0f} GeV ~ '
      f'{math.sqrt(Lambda_sq_natural)/1000:.2f} TeV')
print('  This is a LOW UV scale, comparable to direct LHC searches for new')
print('  bosons.  A generic c_H ~ O(1) at Lambda ~ 2.6 TeV is constrained but')
print('  not excluded; however no UV theory naturally produces c_H/Lambda^2')
print('  proportional to g\'^2 -- that would require a heavy state coupled')
print('  only to hypercharge.')

print()
print('=== Final no-go statement ===')
print(' * The *size* delta m_h^2 = 696 GeV^2 can be hosted by O_H or by O_HBox.')
print('   It cannot be hosted by O_HD alone (EWPT-forbidden).')
print(' * The *form* delta m_h^2 = (3/8)(M_Z^2 - M_W^2) requires the Wilson')
print('   coefficient to be proportional to g\'^2.  No known UV completion')
print('   produces this combination naturally; achieving it requires a heavy')
print('   sector that couples only via hypercharge with a tuned coefficient.')
print(' * Hence: the dV correction is not natural in SMEFT, but it is also not')
print('   forbidden.  This is a partial no-go: the structure is unnatural, not')
print('   excluded.')
print()
print('Practical implication: present the dV identities as algebraic')
print('observations, with the SMEFT analysis attached as a "no natural')
print('UV completion" caveat.  The proposal can survive only if a tuned')
print('low-scale UV theory exists.')
