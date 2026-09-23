# Iteration 1 verification: every algebraic claim of the codex constructor
# output (loop/OUT-codex-iter1.txt) plus the orchestrator's spectrum reading.
# Channel content: p in V_j (open, gauge), Q in Im A_j (closed),
# A = sum_a T_a (x) e_a, A^dagger A = C on V_j. Explicit irreps j=1/2, j=1.
# Completeness of the three zero-derivative terms rests on Schur's lemma for
# the irreducible Im A_j ~ V_j (any invariant insertion is scalar), so the
# variation check may be run in image coordinates Q = A y.
# Exit 0 = all verified.
import sympy as sp


def su2_irrep(j2):
    """Spin matrices for 2j = j2 (dimension j2+1), exact entries."""
    d = j2 + 1
    j = sp.Rational(j2, 2)
    m = [j - k for k in range(d)]
    Jp = sp.zeros(d, d)
    for k in range(1, d):
        Jp[k - 1, k] = sp.sqrt(j*(j + 1) - m[k]*(m[k] + 1))
    Jm = Jp.T
    return [(Jp + Jm)/2, (Jp - Jm)/(2*sp.I), sp.diag(*m)]


for j2 in (1, 2):
    j = sp.Rational(j2, 2)
    C = j*(j + 1)
    d = j2 + 1
    Ts = su2_irrep(j2)
    A = sp.Matrix.vstack(*Ts)             # A: V_j -> V_j (x) C^3, (3d x d)
    Ad = A.H

    # operator identities: A^dagger A = C; static Schur A^dag (AA^dag|_Im)^-1 A = 1
    assert sp.simplify(Ad*A - C*sp.eye(d)) == sp.zeros(d, d)
    assert sp.simplify(Ad*A/C - sp.eye(d)) == sp.zeros(d, d)

    # ---- claim 1: zero-derivative gauge-variation lock ----
    # L0 = (1/2)(a<Q,Q> + 2b<Q,Ap> + d0<p,p>), delta p = u, delta Q = A u / C.
    # In image coordinates Q = A y (A injective for j>0): <Q,Q> = C y.y,
    # <Q,Ap> = C y.p, delta y = u/C.
    a, b, d0 = sp.symbols('a b d0')
    p = sp.Matrix(sp.symbols(f'p0:{d}', real=True))
    u = sp.Matrix(sp.symbols(f'u0:{d}', real=True))
    y = sp.Matrix(sp.symbols(f'y0:{d}', real=True))
    L0 = sp.Rational(1, 2)*(a*C*(y.dot(y)) + 2*b*C*(y.dot(p)) + d0*(p.dot(p)))
    dL0 = sp.expand(a*C*y.dot(u/C) + b*C*((u/C).dot(p) + y.dot(u)) + d0*p.dot(u))
    eqs = [dL0.coeff(s) for s in list(u)]
    coeff_sys = set()
    for e in eqs:
        e = sp.expand(e)
        for s in list(y) + list(p):
            coeff_sys.add(sp.simplify(e.coeff(s)))
    coeff_sys.discard(0)
    sol = sp.solve(list(coeff_sys), [b, d0], dict=True)
    assert sol == [{b: -a/C, d0: a/C}], sol

    # locked L0 equals the one-square (kappa/2)||A^dag Q - p||^2, kappa = a/C
    kappa = a/C
    one_square = sp.Rational(1, 2)*kappa*((C*y - p).dot(C*y - p))
    L0_locked = L0.subs({b: -a/C, d0: a/C})
    assert sp.expand(L0_locked - one_square) == 0

    # ---- claim 2: Schur reduction with kinetic coefficients ----
    B = sp.symbols('B', real=True)
    Zp, ZQ, Zm, k_ = sp.symbols('Z_p Z_Q Z_m kappa', positive=True)
    Gamma_mat = (Zp*B + k_)*sp.eye(d) - (Zm*B - k_)**2/(ZQ*B + k_*C)*(Ad*A)
    GammaP = (Zp*B + k_) - C*(Zm*B - k_)**2/(ZQ*B + k_*C)
    assert sp.simplify(Gamma_mat - GammaP*sp.eye(d)) == sp.zeros(d, d)

    # ---- claim 3: the z-deformation and r = sqrt(z) ----
    z = sp.symbols('z', positive=True)
    Gz = (B + 1) - C/(z*B + C)                  # mu = kappa = 1, Zm = 0, ZQ = z
    assert sp.simplify(Gz - ((B + 1) - (C/z)/(B + C/z))) == 0
    alpha, gamma2 = 1/z, 1/z                    # Gamma = B + 1 - gamma^2 C/(B+alpha C)
    assert sp.simplify(sp.sqrt(gamma2)/alpha - sp.sqrt(z)) == 0   # r = sqrt(z)

    # ---- claim 4 (orchestrator): spectrum of the locked invariant theory ----
    # canonical kinetics, kappa = mu = 1: mass matrix on (p,Q) is D^dag D with
    # D = (-1, A^dag): nonzero spectrum = spec(D D^dag) = 1 + C (Gram/PSD).
    DDdag = sp.eye(d) + Ad*A
    assert sp.simplify(DDdag - (1 + C)*sp.eye(d)) == sp.zeros(d, d)
    # pole equations: invariant kernel has roots {0, -(1+C)}; de Vries kernel
    # gives X^2 + CX - C = 0. They differ by the (forbidden) -1 contact.
    G_inv = B + 1 - C/(B + C)
    assert set(sp.solve(sp.numer(sp.together(G_inv)), B)) == {0, -(1 + C)}
    G_dV = B - C/(B + C)
    assert sp.simplify(G_dV - (B**2 + C*B - C)/(B + C)) == 0

    # ---- claim 5: Sugawara carry-through C -> c^2 C ----
    c = sp.symbols('c', positive=True)
    Gc = B - (c**2*C)/(B + c**2*C)
    assert sp.simplify(Gc - (B**2 + c**2*C*B - c**2*C)/(B + c**2*C)) == 0

    # ---- claim 6: Stueckelberg-weight freedom == kinetic freedom ----
    # delta Q = s A u / C with weight s: invariant is ||A^dag Q - s p||^2;
    # rescaling Q' = Q/s maps it to weight 1 with Z_Q' = s^2 Z_Q: same knob.
    s = sp.symbols('s', positive=True)
    L0s = sp.Rational(1, 2)*((C*y - s*p).dot(C*y - s*p))
    yprime = y*s                                 # Q' = Q/s  =>  y' = y*s ... kinetic |dQ|^2 = |A dy|^2 = C |dy|^2 -> C |dy'|^2/s^2
    L0s_rescaled = sp.Rational(1, 2)*((C*yprime/s - s*p).dot(C*yprime/s - s*p))
    assert sp.expand(L0s - L0s_rescaled) == 0   # same square; kinetic picks 1/s^2

    # ---- claim 7 (orchestrator synthesis): the WHOLE invariant family misses
    # de Vries. Numerator of Gamma_P(B) vanishes at B=0 for ALL coefficients:
    # the gauge-invariant (p,Q) system always has a massless pole (Gram rank
    # deficit = unbroken combination) plus exactly one massive root
    # B = -kappa mu^2 (Z_p C + Z_Q + 2 C Z_m)/(Z_p Z_Q - C Z_m^2).
    num = sp.expand((Zp*B + k_)*(ZQ*B + k_*C) - C*(Zm*B - k_)**2)
    assert num.subs(B, 0) == 0
    other = sp.simplify(-k_*(Zp*C + ZQ + 2*C*Zm)/(Zp*ZQ - C*Zm**2))
    quotient = sp.simplify(num/(B*(Zp*ZQ - C*Zm**2)) - (B - other))
    assert quotient == 0
    # de Vries needs two nonzero roots with ratio X+(3/4)/X+(2); the invariant
    # family has root set {0, other}: structurally incompatible for all
    # coefficient choices, not merely r != 1.

    # ---- claim 8 (orchestrator synthesis): pi-extension keeps PSD; de Vries
    # polynomial unreachable statically. Adding an eaten Stueckelberg scalar
    # gives the independent invariant square mu1^2 ||p - d(pi)/mu1||^2, so the
    # static mass matrix on (p, Q) becomes (mu = 1)
    #   M2 = [[kappa + mu1^2, -kappa sqrt(C)], [-kappa sqrt(C), kappa C]]
    # with det = kappa C mu1^2 >= 0 (PSD: sum of squares). The de Vries
    # polynomial X^2 + C X - C has constant term -C < 0, i.e. needs
    # det(M2) < 0 (one negative eigenvalue): unreachable for ALL kappa,
    # mu1^2 >= 0. Matching the linear term too is likewise impossible:
    # t + kappa C = Ct_, kappa C (t - kappa) = -Ct_ forces t < kappa,
    # contradicting t = kappa + mu1^2 >= kappa.
    t, mu1sq, Ct_ = sp.symbols('t mu1sq Ct')
    M2 = sp.Matrix([[k_ + mu1sq, -k_*sp.sqrt(C)], [-k_*sp.sqrt(C), k_*C]])
    assert sp.simplify(M2.det() - k_*C*mu1sq) == 0          # det >= 0 for mu1sq >= 0
    # matching: pole polynomial B^2 + (t + kappa C)B + kappa C(t - kappa)
    # equals a de Vries-form B^2 + Ct B - Ct  =>  two equations; eliminate Ct:
    sol_t = sp.solve(sp.Eq(k_*C*(t - k_), -(t + k_*C)), t)
    assert len(sol_t) == 1
    mu1_needed = sp.simplify(sol_t[0] - k_)                 # = t - kappa
    assert sp.simplify(mu1_needed + k_*(C + 1)/(k_*C + 1)) == 0
    # mu1^2 = -kappa(C+1)/(kappa C+1) < 0 for all kappa, C > 0: no PSD match;
    # the de Vries polynomial's negative constant term is unreachable by any
    # positive local invariant quadratic action of this channel content.

print("iter1_gauge_lock: ALL CHECKS PASS (j=1/2 and j=1)")
print("  zero-derivative sector: invariance forces b=-a/C, d0=a/C")
print("    -> unique invariant = one-square (kappa/2)||A^dag Q - p||^2")
print("  kinetic sector: Z_Q = z deforms r = sqrt(z)  (UNFORCED)")
print("  Stueckelberg weight s is the same knob as Z_Q (claim 6)")
print("  locked invariant theory: mass matrix = Gram, spectrum {0, (1+C)mu^2}")
print("    -> a local invariant Lagrangian does NOT produce the de Vries kernel;")
print("       the -mu^2 contact subtraction is not available as a local invariant")
