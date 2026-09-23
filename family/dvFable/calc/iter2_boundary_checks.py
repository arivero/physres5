# Iteration 2 verification: the codex adversary arm's algebra
# (loop/OUT-codex-iter2.txt): HLS/KSRF bookkeeping, the CDD counterexample,
# the bootstrap homogeneity, and the spectral reformulation B1 <=> Sigma(0)
# = mu^2 channel-universally. Exit 0 = all verified.
import sympy as sp

B, C, mu = sp.symbols('B C mu', positive=True)

# ---- 1. HLS/KSRF bookkeeping ----
# m_rho^2 = a g^2 F^2, g_rhopipi = (a/2) g, g_rho = a g F^2.
a, g, F = sp.symbols('a g F', positive=True)
m_rho2 = a*g**2*F**2
g_rpp = (a/2)*g
g_rho = a*g*F**2
# KSRF I: g_rho = 2 F^2 g_rhopipi -- holds for every a (Ward theorem):
assert sp.simplify(g_rho - 2*F**2*g_rpp) == 0
# KSRF II: m_rho^2 = 2 F^2 g_rhopipi^2 -- forces a = 2 (VMD input):
sol = sp.solve(sp.Eq(m_rho2, 2*F**2*g_rpp**2), a)
assert sol == [2]

# ---- 2. CDD counterexample: positive, unsubtracted, violates B1 ----
gam = sp.symbols('gamma', positive=True)
lam, delta = sp.symbols('lambda delta', nonnegative=True)
Sigma = gam**2*mu**4*C/(B + delta*mu**2 + lam*mu**2*C)
# unsubtracted: Sigma -> 0 as B -> oo; single positive pole; residue and
# position independent data:
assert sp.limit(Sigma, B, sp.oo) == 0
R = gam**2*mu**4*C
nu0 = delta*mu**2 + lam*mu**2*C
# B1 (R = mu^2 nu0) as an identity in C forces delta = 0, lambda = gamma^2:
match = sp.Poly(sp.expand(R - mu**2*nu0), C)
coeffs = match.coeffs()   # [mu^4(gamma^2-lambda), -mu^4 delta] (degree order)
solset = sp.solve(coeffs, [lam, delta], dict=True)
assert solset == [{lam: gam**2, delta: 0}]
# pole equation of the counterexample: X^2 + (delta + lam C)X - gam^2 C = 0
X = sp.symbols('X', real=True)
Gcdd = X - gam**2*C/(X + delta + lam*C)
assert sp.simplify(Gcdd*(X + delta + lam*C)
                   - (X**2 + (delta + lam*C)*X - gam**2*C)) == 0

# ---- 3. Bootstrap homogeneity: hs = (w-1) g^2 ----
h, w, s_ = sp.symbols('h w s', positive=True)
KP0 = s_ + g**2/h                       # open static kernel (units mu^2)
closure = sp.Eq(h, w*g**2/KP0)          # H_QQ = w H_QP K_P(0)^-1 H_PQ
reduced = sp.simplify(sp.expand((h*KP0 - w*g**2)))
assert sp.expand(reduced - (h*s_ + g**2 - w*g**2)) == 0
# at w = 1, s = 0 the equation is 0 = 0: every h > 0 is a fixed point
assert reduced.subs({w: 1, s_: 0}) == 0
# with a bare kernel k mu^2 instead: h = w g^2/k -- normalization inserted
k = sp.symbols('k', positive=True)
assert sp.solve(sp.Eq(h, w*g**2/k), h) == [w*g**2/k]

# ---- 4. Spectral reformulation: B1 <=> Sigma_j(0) = mu^2 for all j ----
Sigma_dV = mu**4*C/(B + mu**2*C)
assert sp.simplify(Sigma_dV.subs(B, 0) - mu**2) == 0          # channel-blind
# and for the general single-pole Sigma = R/(B+nu0):
Rs, nus = sp.symbols('R nu0', positive=True)
Sigma_gen = Rs/(B + nus)
assert sp.simplify(sp.solve(sp.Eq(Sigma_gen.subs(B, 0), mu**2), Rs)[0]
                   - mu**2*nus) == 0                          # Sigma(0)=mu^2 <=> R=mu^2 nu0

print("iter2_boundary_checks: ALL CHECKS PASS")
print("  KSRF I holds for every a; KSRF II <=> a = 2 (VMD input)")
print("  CDD counterexample: positive+unsubtracted, B1 fails unless")
print("    delta = 0, lambda = gamma^2 -- no-CDD is a choice, not a theorem")
print("  bootstrap closure is homogeneous: h s = (w-1) g^2; at w=1,s=0")
print("    every h is a fixed point (h = 1 inserted, not derived)")
print("  B1 <=> Sigma_j(0) = mu^2 channel-universally (static seed mass)")
