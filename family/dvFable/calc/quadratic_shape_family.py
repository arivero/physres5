# The (c1, c2)-quadratic family X^2 + c1 X - c2 = 0: occurrences and the
# de Vries diagonal. Verifies the normalizations behind
# notes/2026-06-11-quadratic-shape-inventory.md. Exit 0 = all verified.
import sympy as sp

X, C, c1, c2, K = sp.symbols('X C c_1 c_2 K', real=True)
l, d, lam, Delta, m2L2, M2, m, s = sp.symbols(
    'l d lambda Delta m2L2 M2 m s', positive=True)

# 1. The iteration-1/2 two-channel family IS the (c1,c2) quadratic:
#    X^2 + (delta + lam C) X - gamma^2 C = 0  ->  c1, c2 arbitrary nonneg;
#    de Vries = the diagonal c1 = c2 = C (the retired g^2/alpha = 1 closure).
delta, gam = sp.symbols('delta gamma', nonnegative=True)
fam = X**2 + (delta + lam*C)*X - gam**2*C
assert sp.expand(fam.subs({delta: 0, lam: 1, gam: 1}) - (X**2 + C*X - C)) == 0

# 2. Sphere-harmonic inversion: lambda = l(l + d - 1) on S^d
#    <=> l^2 + (d-1) l - lambda = 0: c1 = d-1, c2 = lambda.
sphere = sp.expand(l*(l + d - 1) - lam)
assert sp.expand(sphere - (l**2 + (d - 1)*l - lam)) == 0

# 3. AdS_{d+1}/CFT_d scalar mass-dimension relation: Delta(Delta - d) = m^2 L^2
#    <=> Delta^2 - d Delta - m^2L^2 = 0: same family, c1 = -d, c2 = m^2 L^2.
ads = sp.expand(Delta*(Delta - d) - m2L2)
assert sp.expand(ads - (Delta**2 - d*Delta - m2L2)) == 0

# 4. Corpus Poincare-Casimir form (conversation 14):
#    M^4 - M^2 C2 + C1 C2 = 0, C1 = m^2, C2 = -m^2 s(s+1).
#    Normalizing X = M^2/C1, K = C2/C1: the polynomial becomes
#    X^2 - K X + K = 0 -- the SAME K in both slots AUTOMATICALLY:
#    the diagonal is built into the product structure of the constant term.
C1s, C2s = sp.symbols('C1 C2')
poin = M2**2 - M2*C2s + C1s*C2s
norm = sp.expand(poin.subs({M2: X*C1s, C2s: K*C1s})/C1s**2)
assert sp.expand(norm - (X**2 - K*X + K)) == 0
#    With C1 = m^2, C2 = -m^2 s(s+1): K = -s(s+1) -> X^2 + s(s+1)X - s(s+1):
assert sp.expand(norm.subs(K, -s*(s + 1))
                 - (X**2 + s*(s + 1)*X - s*(s + 1))) == 0

# 5. The de Vries family in (c1,c2)-language is the diagonal line c1 = c2:
#    equivalently "constant term = minus the linear coefficient" -- one
#    condition on a two-parameter family. The forcing question = what
#    dynamics pins the diagonal; the Poincare form only repackages it
#    (why is the constant term the PRODUCT C1*C2 and not independent?).
gen = X**2 + c1*X - c2
assert sp.expand(gen.subs({c1: C, c2: C}) - (X**2 + C*X - C)) == 0

print("quadratic_shape_family: ALL CHECKS PASS")
print("  family X^2 + c1 X - c2: two-channel (iter 1-2), sphere-harmonic")
print("  inversion (c1 = d-1, c2 = lambda), AdS mass-dimension (c1 = -d,")
print("  c2 = m^2L^2), Poincare-Casimir corpus form (auto-diagonal via the")
print("  C1*C2 product constant term). De Vries content = the diagonal c1=c2.")
