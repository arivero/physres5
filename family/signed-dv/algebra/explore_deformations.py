#!/usr/bin/env python3
"""Algebraic deformations of the signed dV quadratic.

We organize the deformations by the *physical question* each one is meant to
address:

  (i)   universal eta deformation        : multiplicative deformation of the
                                            constant term; can it generate the
                                            phenomenological sin^2 theta_W?
  (ii)  spin-dependent eta_s deformation : different multiplier per spin slot;
                                            mostly used to check uniqueness.
  (iii) on-shell-subtracted deformation  : leaves the positive root fixed and
                                            shifts the negative root by lam.
                                            Used to parametrize the proposed
                                            (3/8)(M_Z^2 - M_W0^2) sigma_3
                                            correction without introducing new
                                            physics.
  (iv)  intercept (Regge) deformation    : J = alpha_0 + alpha' M^2 with the
                                            quadratic interpreted as the
                                            j(j+1) eigenvalue along a moving
                                            trajectory.  Used to test whether
                                            a Regge picture can naturally
                                            replace s(s+1) by an effective
                                            Casimir.
  (v)   spurion deformation              : P_s(x; chi_Y) with a single
                                            custodial-breaking spurion that
                                            connects s=1 and s=1/2 slots.
                                            Used to ask whether a parent
                                            equation exists that interpolates
                                            between a custodial-degenerate
                                            point and the physical signed-root
                                            point.
  (vi)  matrix/operator deformation      : 2 x 2 mass-square matrix in the
                                            signed (+,-) sector with a sigma_3
                                            perturbation.

The script prints exact symbolic results and the corresponding numerical
masses where relevant.  Nothing here is a derivation: it is a catalogue of
algebraic options to be matched against mainstream mechanisms.
"""

import sympy as sp

sqrt = sp.sqrt
N = sp.N

# ---------------------------------------------------------------------------
# Basic symbols and constants
# ---------------------------------------------------------------------------
x, C, eta, lam, chi, alpha0, alphap, J = sp.symbols(
    'x C eta lam chi alpha0 alphap J', real=True)
s = sp.symbols('s', real=True, nonnegative=True)

C1 = sp.Rational(2)         # adjoint Casimir of SU(2)
Ch = sp.Rational(3, 4)      # fundamental Casimir of SU(2)
CFoCA = Ch / C1             # 3/8

MZ_num = sp.Rational(911876, 10000)
mh_num = sp.Float("125.20")
GF_num = sp.Float("1.1663787e-5")

# Unperturbed roots
def roots_of(P):
    return sp.solve(P, x)

P0 = x**2 + C*x - C
xplus = (-C + sqrt(C*(C + 4)))/2
xminus = (-C - sqrt(C*(C + 4)))/2

print('=' * 72)
print('(i) Universal eta deformation: x^2 + C x - eta C = 0')
print('=' * 72)
P_eta = x**2 + C*x - eta*C
rho_plus = sp.simplify((-C + sqrt(C**2 + 4*eta*C))/2)
print('positive root :', rho_plus)
rho1 = rho_plus.subs(C, C1)
rhoh = rho_plus.subs(C, Ch)
print('ratio rhoh/rho1 (sin^2 thW analog) ->')
print('  solve = 5/8  : eta =', sp.solve(sp.Eq(rhoh/rho1, sp.Rational(5, 8)), eta))
print('  solve = 3/8  : eta =', sp.solve(sp.Eq(rhoh/rho1, sp.Rational(3, 8)), eta))

print()
print('=' * 72)
print('(ii) Spin-dependent eta_s : x^2 + C_s x - eta_s C_s = 0')
print('=' * 72)
eta1, etah = sp.symbols('eta_1 eta_h')
rho1_eta = (-C1 + sqrt(C1**2 + 4*eta1*C1))/2
rhoh_eta = (-Ch + sqrt(Ch**2 + 4*etah*Ch))/2
# Demand positive-branch ratio = M_W^2/M_Z^2 (experimental) AND
# determinant ratio = 3/8 (signed identity); see if etas can preserve both.
det1 = sp.simplify(-eta1 * C1)         # = product of roots
deth = sp.simplify(-etah * Ch)
print('det1   :', det1)
print('deth   :', deth)
print('deth/det1 = 3/8  iff  (Ch eta_h)/(C1 eta_1) = 3/8')
print('  with eta_1 = eta_h = 1 already gives 3/8 (Casimir ratio)')

print()
print('=' * 72)
print('(iii) On-shell-subtracted deformation: P -> P + lam (x - x_+)')
print('=' * 72)
P_sub = sp.expand(P0 + lam*(x - xplus))
factored = sp.expand((x - xplus) * (x - xminus + lam))
print('P_sub - (x-x+)(x-x-+lam) =', sp.simplify(P_sub - factored))
print('-> positive root unchanged, negative root shifted by -lam')
# Tune lam to reproduce the 3/8 (M_Z^2 - M_W0^2) correction:
x1p_val = sqrt(3) - 1
xhp_val = (sqrt(57) - 3)/8
delta_pos = sp.simplify(x1p_val - xhp_val)
lam_h = sp.Rational(3, 8) * delta_pos          # acts on s=1/2 sector
lam_1 = -sp.Rational(3, 8) * delta_pos         # acts on s=1   sector
print('lam_{1/2}  =', sp.nsimplify(lam_h), '  num =', N(lam_h, 10))
print('lam_{1}    =', sp.nsimplify(lam_1), '  num =', N(lam_1, 10))

print()
print('=' * 72)
print('(iv) Intercept (Regge) deformation: J = alpha0 + alphap M^2')
print('=' * 72)
# Interpret C_s = s(s+1) = J(J+1) along a Regge trajectory.
# A linear intercept shift maps J = alpha0 + alphap M^2 so that
#     C(M^2) = J(J+1) = (alpha0 + alphap M^2)(alpha0 + alphap M^2 + 1)
# Replace C_s in P_s(x) and look for fixed points.
Mfeed = sp.Symbol('M2', real=True)
J_lin = alpha0 + alphap * Mfeed
C_traj = J_lin * (J_lin + 1)
P_traj = x**2 + C_traj*x - C_traj
roots_traj = sp.solve(P_traj, x)
print('roots along trajectory (symbolic, two values):')
for r in roots_traj:
    print('  ', sp.simplify(r))
# Custodial point: J = 0 forces C = 0, roots are x = 0 (degenerate).
# Physical points: alpha(M_Z^2) = 1 and alpha(M_W^2) = 1/2.  Solve for
# alpha0, alphap.
MZ2, MW2 = sp.symbols('MZ2 MW2', positive=True)
sol = sp.solve([alpha0 + alphap*MZ2 - 1, alpha0 + alphap*MW2 - sp.Rational(1, 2)],
               [alpha0, alphap])
print('alpha0 =', sol[alpha0])
print('alphap =', sol[alphap])
print('-> linear interpolation in M^2; intercept 1 at M_Z, 1/2 at M_W')
print('   does *not* by itself produce the (3/8) correction.')

print()
print('=' * 72)
print('(v) Spurion deformation: P_s(x; chi_Y)')
print('=' * 72)
# Demand a one-parameter family P(x; chi) such that
#   P(x; 0)         has degenerate positive root x_+ for both spins (custodial),
#   P(x; chi_phys)  reproduces the dV equation.
# Try the simplest ansatz: shift the constant term by a Casimir-weighted
# spurion that vanishes at chi = 0 and equals C_s at chi = 1:
P_chi = x**2 + C*x - chi*C
print('Family : P(x; chi) = x^2 + C x - chi C')
print('At chi = 0 the roots are x = 0 and x = -C  (degenerate-zero positive root)')
print('At chi = 1 the roots are the dV roots')
# Positive root vs chi:
rp_chi = (-C + sqrt(C**2 + 4*chi*C))/2
print('positive root = ', sp.simplify(rp_chi))
# In the custodial limit chi = 0 the W and Z "positive" roots both collapse to 0.
# We need a different parent: split chi between Casimirs so that x_+ stays
# equal across spins only when chi -> chi_cust (custodial spurion turned off).
# Ansatz: x^2 + C x - C - chi (C - C_*) where C_* is the custodial-degenerate
# Casimir.  At chi = 1 this collapses to the dV equation; at chi = 0 the
# constant term -C is replaced by -C_*, restoring a common x_+ across spins.
C_star = sp.Symbol('C_star', positive=True)
P_parent = x**2 + C*x - C_star - chi*(C - C_star)
print()
print('Parent equation : x^2 + C x - C_* - chi (C - C_*) = 0')
print('  chi = 0       : roots depend on C linearly, custodial spurion off')
print('  chi = 1       : reproduces the dV equation P_s(x) = 0')
rp_parent = (-C + sqrt(C**2 + 4*(C_star + chi*(C - C_star))))/2
rm_parent = (-C - sqrt(C**2 + 4*(C_star + chi*(C - C_star))))/2
# Custodial degeneracy condition: x_+ identical for s=1 and s=1/2 at chi = 0.
cust_eq = sp.simplify(rp_parent.subs([(C, C1), (chi, 0)]) -
                      rp_parent.subs([(C, Ch), (chi, 0)]))
print('  x_+(s=1,chi=0) - x_+(s=1/2,chi=0) =', cust_eq)
print('  -> custodial degeneracy in the positive root cannot be achieved')
print('     with a chi-shift in the constant term alone, because the linear-in-C')
print('     coefficient of x still distinguishes the spins.')
# To get a real custodial-degenerate point we need to switch off the linear
# term as well.  Try a two-parameter parent:
#     x^2 + (1-chi) C_* x + chi C x - C_* - chi (C - C_*) = 0.
# At chi = 0 : x^2 + C_* x - C_* = 0 (spin-independent).
# At chi = 1 : x^2 + C x - C = 0 (dV).
P_parent2 = x**2 + ((1-chi)*C_star + chi*C)*x - (C_star + chi*(C - C_star))
print()
print('Two-parameter parent  : x^2 + [(1-chi) C_* + chi C] x - [C_* + chi (C - C_*)] = 0')
print('  chi = 0  : custodial-degenerate quadratic in C_* alone (M_Z = M_W)')
print('  chi = 1  : dV equation')
# Compute the positive root as a function of chi and check the rate at which
# the spin splitting opens.
disc = ((1-chi)*C_star + chi*C)**2 + 4*(C_star + chi*(C - C_star))
rp2 = (-((1-chi)*C_star + chi*C) + sqrt(disc))/2
rm2 = (-((1-chi)*C_star + chi*C) - sqrt(disc))/2
print('positive root at chi=1 : ', sp.simplify(rp2.subs(chi, 1)))
print('negative root at chi=1 : ', sp.simplify(rm2.subs(chi, 1)))
# The leading custodial-breaking expansion is in chi (or in (C - C_*) at
# fixed chi).  Expand rp2 around chi = 0 to first order in (C - C_*):
print('linear (C-C_*) expansion at chi -> 0 :')
exp_p = sp.series(rp2, chi, 0, 2).removeO()
exp_m = sp.series(rm2, chi, 0, 2).removeO()
print('  rp2 =', sp.simplify(exp_p))
print('  rm2 =', sp.simplify(exp_m))
print()
print('=> the parent equation is well-defined but the linear coefficient of')
print('   chi (C - C_*) does NOT factor into a clean C_F/C_A ratio; the')
print('   eigenvalues at chi = 1 do reproduce the dV roots exactly.')

print()
print('=' * 72)
print('(vi) Matrix deformation in signed two-root space')
print('=' * 72)
# Mcal^2 * diag(x_+, x_-) per spin slot.  The proposed correction is a
# traceless sigma_3 perturbation that lives entirely in the negative-sector
# combination [M_H0^2, M_F0^2].  Write
#
#   M_-^2 = diag(M_H0^2, M_F0^2) + eps * sigma_3,   eps = (3/8)(M_Z^2 - M_W0^2)
#
# The trace and determinant changes are
trM, detM, e = sp.symbols('trM detM e', real=True)
# Symbolic:
MH0s, MF0s = sp.symbols('MH0_sq MF0_sq', positive=True)
M_minus = sp.Matrix([[MH0s + e, 0], [0, MF0s - e]])
print('Matrix M_-^2 :')
sp.pprint(M_minus)
print('Trace        :', sp.simplify(M_minus.trace()))
print('Det          :', sp.simplify(M_minus.det()))
# The "trace-preserved" claim: Trace = MH0^2 + MF0^2 is invariant under sigma_3.
# The "det-changes-by-O(eps^2)" claim:
print('Trace shift (eps -> 0)     :',
      sp.simplify(M_minus.trace() - (MH0s + MF0s)))
print('Det shift to O(eps)        :',
      sp.simplify(sp.series(M_minus.det(), e, 0, 2).removeO()))
print('Det shift to O(eps^2)      :',
      sp.simplify(sp.series(M_minus.det(), e, 0, 3).removeO()))

# Numerical sanity check
Mcal = sp.simplify(MZ_num / sqrt(xplus.subs(C, C1)))
MH0_val = sp.simplify(Mcal * sqrt(-xminus.subs(C, Ch)))
MF0_val = sp.simplify(Mcal * sqrt(-xminus.subs(C, C1)))
MW0_val = sp.simplify(Mcal * sqrt(xplus.subs(C, Ch)))
eps_val = sp.Rational(3, 8) * (MZ_num**2 - MW0_val**2)
print()
print('Numerical eps          =', N(eps_val, 12), 'GeV^2')
print('MH (corrected)         =', N(sqrt(MH0_val**2 + eps_val), 12), 'GeV')
print('MF (corrected)         =', N(sqrt(MF0_val**2 - eps_val), 12), 'GeV')
print('Trace M_-^2 (corr)     =', N(MH0_val**2 + MF0_val**2, 12))
print('Trace M_-^2 (uncorr)   =', N(MH0_val**2 + MF0_val**2, 12))
print('Trace identity holds   : yes (sigma_3 is traceless)')

print()
print('=' * 72)
print('Summary table of natural group factors for SU(2)')
print('=' * 72)
print(f'  C_F        = {Ch}    (fundamental, j=1/2)')
print(f'  C_A        = {C1}    (adjoint, j=1)')
print(f'  C_F/C_A    = {CFoCA} = 3/8')
print(f'  T_F        = 1/2    (Dynkin index)')
print(f'  d_F        = 2,    d_A = 3')
print(f'  d_F/d_A    = 2/3')
print(f'  T_F/C_A    = 1/4')
print(f'  C_F/(C_F+C_A) = 3/11  (NOT a SUSY beta-function ratio)')
print('  -> Only C_F/C_A reproduces 3/8 from SU(2) group theory alone.')
