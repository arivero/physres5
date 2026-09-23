# Iteration 4 verification: the codex adversary arm's algebra
# (loop/OUT-codex-iter4.txt) on the orbit candidate (c): the weight family,
# the general weight identity, proper-clock bookkeeping, orbit data, and
# the same-radius force obstruction. Exit 0 = all verified.
import sympy as sp

C, k, X = sp.symbols('C k X', positive=True)
Xp = (-C + sp.sqrt(C**2 + 4*C))/2


def sin2(xw, xz):
    return 1 - xw/xz


# ---- 1. the pre-registered weight family ----
# weight 1: gamma beta^2 = sqrt(C)  <=>  X^2 + CX - C = 0
xw, xz = Xp.subs(C, sp.Rational(3, 4)), Xp.subs(C, 2)
assert abs(float(sp.N(sin2(xw, xz), 15)) - 0.223101322300866) < 1e-13
# gamma-weight (proper clock): gamma^2 beta^2 = sqrt(C) <=> X/(1-X) = sqrt(C)
xg = lambda c: sp.sqrt(c)/(1 + sp.sqrt(c))
v = float(sp.N(sin2(xg(sp.Rational(3, 4)), xg(2)), 12))
assert abs(v - 0.207729) < 5e-7
# zitter factor 2: gamma beta^2 = 2 sqrt(C) <=> X^2 + 4CX - 4C = 0
Xp4 = (-4*C + sp.sqrt(16*C**2 + 16*C))/2
v = float(sp.N(sin2(Xp4.subs(C, sp.Rational(3, 4)), Xp4.subs(C, 2)), 12))
assert abs(v - 0.119793) < 5e-7
# r = lambda_C: gamma beta = sqrt(C) <=> X = C/(1+C)
xr = lambda c: c/(1 + c)
v = float(sp.N(sin2(xr(sp.Rational(3, 4)), xr(2)), 12))
assert abs(v - 0.357143) < 5e-7

# ---- 2. general weight identity: T = k h/(m0 c^2) => gamma beta^2 = sqrt(C)/k ----
# T = 2 pi r/(beta c) = k h/(m0 c^2)  =>  r = k beta hbar/(m0 c)
# L = gamma m0 beta c r = k gamma beta^2 hbar = sqrt(C) hbar
beta, gamma_ = sp.symbols('beta gamma', positive=True)
L_over_hbar = k*gamma_*beta**2
assert sp.simplify(sp.solve(sp.Eq(L_over_hbar, sp.sqrt(C)),
                            gamma_)[0] - sp.sqrt(C)/(k*beta**2)) == 0

# ---- 3. proper-clock bookkeeping: one tick per orbit => gamma-weight ----
# d phi = (m0 c^2/hbar) d tau; per lab orbit: Delta phi = (m0c^2/hbar) T_lab/gamma
# = 2 pi  =>  T_lab = gamma h/(m0 c^2). De Vries (T_lab = h/m0c^2) gives
# proper phase 2 pi / gamma per orbit (frame-inconsistent as a tick rule).
T_lab, m0c2_over_h = sp.symbols('T_lab nu0', positive=True)
phase = 2*sp.pi*m0c2_over_h*T_lab/gamma_
sol = sp.solve(sp.Eq(phase, 2*sp.pi), T_lab)[0]
assert sp.simplify(sol - gamma_/m0c2_over_h) == 0

# ---- 4. de Vries member orbit data ----
rows = {sp.Rational(1, 2): (0.568729, 0.754143, 1.5227, 0.5227),
        sp.Integer(1): (0.732051, 0.855600, 1.9319, 0.9319)}
for j, (x_ref, b_ref, g_ref, K_ref) in rows.items():
    Cj = j*(j + 1)
    x = float(sp.N(Xp.subs(C, Cj), 12))
    b = x**0.5
    g = (1 - x)**(-0.5)
    # the arm's table is 6-figure rounded with a last-digit slip in beta_1/2
    # (true 0.7541415 vs quoted 0.754143): tolerance 5e-6, immaterial.
    assert abs(x - x_ref) < 5e-7 and abs(b - b_ref) < 5e-6
    assert abs(g - g_ref) < 5e-5 and abs(g - 1 - K_ref) < 5e-5
    # r/lambda_bar_C = beta (weight 1) and F = gamma beta m0^2c^3/hbar:
    F = g*b
    assert abs(F - {sp.Rational(1, 2): 1.148, sp.Integer(1): 1.653}[j]) < 2e-3

# ---- 5. same-radius force obstruction ----
# At common r, L = gamma m beta c r = sqrt(C) hbar gives gamma m beta =
# sqrt(C) hbar/(c r); the centripetal force F = gamma m beta^2 c^2/r =
# sqrt(C) beta hbar c / r^2: channel-dependent through sqrt(C) beta.
# A channel-blind central potential supplies ONE F at r: contradiction.
r_ = sp.symbols('r', positive=True)
F_chan = sp.sqrt(C)*sp.sqrt(Xp)/r_**2          # in units hbar c, beta = sqrt(Xp)
ratio = sp.simplify(F_chan.subs(C, 2)/F_chan.subs(C, sp.Rational(3, 4)))
assert abs(float(sp.N(ratio, 10)) - 1.8527) < 5e-4   # != 1: no single V(r)

print("iter4_orbit_checks: ALL CHECKS PASS")
print("  weight family: 0.223101 / 0.207729 / 0.119793 / 0.357143")
print("  T = k h/(m0c^2)  =>  gamma beta^2 = sqrt(C)/k (weight = the lock)")
print("  invariant one-tick-per-orbit clock => gamma-weight (0.2077), NOT")
print("  de Vries; the weight-1 member mixes rest-frame period into lab time")
print("  same-radius: required force ratio Z/W = 1.853 -> no channel-blind V(r)")
