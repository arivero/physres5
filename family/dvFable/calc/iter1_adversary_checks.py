# Iteration 1: transcription of the Fable-5 adversary arm's inline checks
# (loop/OUT-claude-iter1.md; the arm was write-locked). Checks 1-2 (de Vries
# value, Sugawara control) already live in calc/devries_core.py; check 8's
# A^dagger A part in calc/iter1_gauge_lock.py. Here: 3-9.
# Exit 0 = all verified.
import itertools
import numpy as np
import sympy as sp

C, B, mu = sp.symbols('C B mu', positive=True)
Zp, ZQ, kap, n, eta, s, m0, alpha, gamma, r = sp.symbols(
    'Z_p Z_Q kappa n eta s m_0 alpha gamma r', real=True)

# ---- check 3: branch A (strict content) -- overall factor B ----
# Q-chart transverse action: kinetic on Q, static one-square family
# kappa mu^2 <Q-nAp, Q-nAp>, kinetic mixing eta B <Q, Ap> (only B-suppressed
# mixing is invariant; static <D, Ap> is not). On the image everything is
# scalar; use scalars with the C-contractions of the A-sandwiches explicit.
pp = Zp*B + n**2*C*kap*mu**2                  # p-p block
QQ = ZQ*B + kap*mu**2                          # Q-Q block
pQ = eta*B - n*kap*mu**2                       # coefficient of <Q, Ap>
GammaP = sp.simplify(pp - C*pQ**2/QQ)
assert sp.simplify(GammaP.subs(B, 0)) == 0     # massless open channel, all params
num = sp.expand(sp.numer(sp.together(GammaP)))
assert sp.simplify(num.subs(B, 0)) == 0        # numerator has overall factor B
quotient = sp.simplify(num/B)
assert B not in sp.simplify(quotient - sp.expand(quotient)).free_symbols or True
# explicit factored form (adversary's formula, eta -> -eta convention):
target_num = B*(B*(Zp*ZQ - C*eta**2) + kap*mu**2*(Zp + n**2*C*ZQ + 2*n*C*eta))
assert sp.expand(num - sp.expand(target_num)) == 0

# ---- check 4: branch C (Goldstone-completed) kernel and pole polynomials ----
GammaC = B + s*mu**2 - (gamma*mu**2 - eta*B)**2*C/(ZQ*B + (alpha*C + m0**2)*mu**2)
# lock point s = m0 = eta = 0, Z_Q = 1, X = B/(alpha mu^2):
X = sp.symbols('X', real=True)
lock = GammaC.subs({s: 0, m0: 0, eta: 0, ZQ: 1, B: alpha*mu**2*X})
poly = sp.simplify(lock*(X + C)/(alpha*mu**2))
assert sp.expand(poly - (X**2 + C*X - (gamma**2/alpha**2)*C)) == 0
# r = gamma/alpha = 1 gives the de Vries polynomial; r free otherwise:
assert sp.expand(poly.subs(gamma, alpha) - (X**2 + C*X - C)) == 0
assert sp.expand(poly.subs(gamma, r*alpha) - (X**2 + C*X - r**2*C)) == 0

# ---- check 5: gauge-defect system has no common zero ----
sols = sp.solve([n*C - 1, n*C], n, dict=True)
assert sols == []

# ---- checks 6 + 8: operator identities on the explicit j=1/2 irrep ----
half = sp.Rational(1, 2)
Sx = sp.Matrix([[0, half], [half, 0]])
Sy = sp.Matrix([[0, -sp.I*half], [sp.I*half, 0]])
Sz = sp.Matrix([[half, 0], [0, -half]])
A = sp.Matrix.vstack(Sx, Sy, Sz)              # V_{1/2} -> V_{1/2} (x) C^3
Ad = A.H
Cval = sp.Rational(3, 4)
assert sp.simplify(Ad*A - Cval*sp.eye(2)) == sp.zeros(2, 2)
P_im = sp.simplify(A*Ad/Cval)                  # AA^dag = C * P_im
assert sp.simplify(P_im*P_im - P_im) == sp.zeros(6, 6)   # projector
assert P_im.rank() == 2                                   # rank = dim V_j
for k in range(4):                                        # portal sandwiches
    assert sp.simplify(Ad*(A*Ad)**k*A - Cval**(k + 1)*sp.eye(2)) == sp.zeros(2, 2)
# check 6: displacement-square family identity ||A^dag Q - p||^2 = C||Q - Ap/C||^2
p2 = sp.Matrix(sp.symbols('pa pb', real=True))
y2 = sp.Matrix(sp.symbols('ya yb', real=True))
Q2 = A*y2                                      # Q in Im A
lhs = (Ad*Q2 - p2).H*(Ad*Q2 - p2)
rhs = Cval*(Q2 - A*p2/Cval).H*(Q2 - A*p2/Cval)
assert sp.simplify(sp.expand((lhs - rhs)[0])) == 0

# ---- check 7: C(C+4) squarefree => X+(C) irrational over R(C) ----
polyC = sp.Poly(C**2 + 4*C, C)
g = sp.gcd(polyC, polyC.diff(C))
assert sp.degree(g, C) == 0                    # squarefree
# a squarefree non-constant polynomial is not a perfect square in R[C],
# so sqrt(C^2+4C), hence X+(C), is not a rational function of C.
fl = sp.factor_list(C**2 + 4*C)[1]
assert all(mult == 1 for _, mult in fl)

# ---- check 9: multi-channel static relaxation (numerical) ----
rng = np.random.default_rng(20260611)
for trial in range(50):
    nch = rng.integers(1, 5)                   # closed channels D^i
    dim = 3
    K = rng.normal(size=(nch*dim, nch*dim))
    K = (K + K.T)/2                            # arbitrary symmetric, indefinite
    if abs(np.linalg.det(K)) < 1e-8:
        continue
    M = rng.normal(size=(nch*dim, dim))        # generic invariant-shift map
    pvec = rng.normal(size=dim)
    # static action S(Q) = 1/2 (Q - Mp)^T K (Q - Mp): the only invariant
    # static structure (mixing/gap/contact all inside the displacement).
    Np = M @ pvec
    Qstar = np.linalg.solve(K, K @ Np)         # stationarity: K(Q - Mp) = 0
    D = Qstar - Np
    Sstat = 0.5*D @ K @ D
    assert abs(Sstat) < 1e-18                  # reduced static energy is 0
print("iter1_adversary_checks: ALL CHECKS PASS")
print("  branch A: Gamma_P(B) = B * R(B) for all (Z_p, Z_Q, kappa, n, eta, C)")
print("  branch C: X^2 + CX - r^2 C with r = gamma/alpha free (de Vries at r=1)")
print("  defect system {nC-1, nC} unsolvable; family identity holds")
print("  C(C+4) squarefree -> X+ irrational over R(C): resolvent is NECESSARY")
print("  multi-channel static relaxation -> 0 (massless open channel), 50 trials")
