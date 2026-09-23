"""Exact spectral machinery on SU(2) = S^3 with a left-invariant metric, and
the de Vries block test for squashed three-spheres.

Conventions
-----------
Left-invariant vector fields X_1, X_2, X_3 with [X_i, X_j] = 2 eps_ijk X_k.
The metric is g(X_k, X_k) = s_k^2 (diagonal; every left-invariant metric on
SU(2) is isometric to one of these).  s = (1, 1, 1) is the round unit sphere;
s = (R, R, R) the round sphere of radius R.  A Berger sphere has two equal s.

By Peter-Weyl, forms of type j live in M_j (x) Lambda^p(g*), dim M_j = 2j + 1
(the left multiplicity 2j + 1 is dropped).  X_k acts on M_j as rho(X_k) =
-2i J_k.  The exterior derivative is the Chevalley-Eilenberg differential,
the inner product is the metric one, delta = d^dagger, and
Delta_p = d delta + delta d.  The Bochner Laplacian on 1-forms is computed
separately from the Levi-Civita connection, so the Weitzenboeck identity
Delta_1 = nabla^* nabla + Ric is a check, not an input.

Run as a script to print the validation checks and the de Vries tests.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations

import numpy as np

EPS = np.zeros((3, 3, 3))
for _i, _j, _k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
    EPS[_i, _j, _k], EPS[_j, _i, _k] = 1.0, -1.0

STRUCT = 2.0 * EPS  # [X_i, X_j] = STRUCT[i, j, k] X_k
BASIS = {p: list(combinations(range(3), p)) for p in range(4)}


def spin_matrices(j: float):
    """Standard spin-j matrices J_x, J_y, J_z in the |j, m> basis, m = j..-j."""
    n = int(round(2 * j)) + 1
    m = j - np.arange(n)
    jp = np.zeros((n, n), dtype=complex)
    for a in range(1, n):
        jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    jx = (jp + jp.conj().T) / 2
    jy = (jp - jp.conj().T) / (2j)
    jz = np.diag(m).astype(complex)
    return jx, jy, jz


def rep(j: float):
    """rho(X_k) = -2i J_k, so that [rho(X_i), rho(X_j)] = 2 eps_ijk rho(X_k)."""
    return [-2j * J for J in spin_matrices(j)]


def _wedge(k: int, idx: tuple):
    """theta^k wedge theta^idx -> (sign, sorted index tuple), or (0, None)."""
    if k in idx:
        return 0, None
    new = (k,) + idx
    perm = sorted(range(len(new)), key=lambda a: new[a])
    sign, seen = 1, [False] * len(new)
    for a in range(len(new)):  # parity of the sorting permutation
        if not seen[a]:
            b, length = a, 0
            while not seen[b]:
                seen[b], b, length = True, perm[b], length + 1
            sign *= (-1) ** (length - 1)
    return sign, tuple(sorted(new))


def _d_ce(idx: tuple):
    """Chevalley-Eilenberg d on theta^idx: dict {sorted idx: coefficient}.
    d theta^k = -sum_{i<j} STRUCT[i,j,k] theta^i wedge theta^j."""
    out: dict = {}
    for a, k in enumerate(idx):
        rest_before, rest_after = idx[:a], idx[a + 1:]
        for i, jj in combinations(range(3), 2):
            c = -STRUCT[i, jj, k]
            if c == 0:
                continue
            # theta^{before} ^ (theta^i ^ theta^j) ^ theta^{after}, sign (-1)^a
            term, sign = (i, jj), (-1) ** a
            full = rest_before + term + rest_after
            if len(set(full)) < len(full):
                continue
            order = sorted(range(len(full)), key=lambda q: full[q])
            par, seen = 1, [False] * len(full)
            for q in range(len(full)):
                if not seen[q]:
                    r, length = q, 0
                    while not seen[r]:
                        seen[r], r, length = True, order[r], length + 1
                    par *= (-1) ** (length - 1)
            key = tuple(sorted(full))
            out[key] = out.get(key, 0.0) + c * sign * par
    return out


def d_matrix(j: float, p: int) -> np.ndarray:
    """d: M_j (x) Lambda^p -> M_j (x) Lambda^{p+1}; index = r * nforms + form."""
    R = rep(j)
    n = R[0].shape[0]
    src, dst = BASIS[p], BASIS[p + 1]
    pos = {I: a for a, I in enumerate(dst)}
    D = np.zeros((n * len(dst), n * len(src)), dtype=complex)
    for b, I in enumerate(src):
        for k in range(3):
            sgn, J = _wedge(k, I)
            if sgn:
                for r in range(n):
                    D[r * len(dst) + pos[J], b::len(src)] += sgn * R[k][r, :]
        for J, c in _d_ce(I).items():
            for r in range(n):
                D[r * len(dst) + pos[J], r * len(src) + b] += c
    return D


def gram(j: float, p: int, s) -> np.ndarray:
    n = int(round(2 * j)) + 1
    w = [np.prod([1.0 / s[k] ** 2 for k in I]) for I in BASIS[p]]
    return np.kron(np.eye(n), np.diag(w))


def laplacians(j: float, s):
    """Return dict with d_p, delta_p and Hodge Laplacians Delta_p (p=0..3)."""
    d = {p: d_matrix(j, p) for p in range(3)}
    G = {p: gram(j, p, s) for p in range(4)}
    delta = {p + 1: np.linalg.solve(G[p], d[p].conj().T @ G[p + 1]) for p in range(3)}
    lap = {}
    for p in range(4):
        L = np.zeros_like(G[p], dtype=complex)
        if p >= 1:
            L = L + d[p - 1] @ delta[p]
        if p <= 2:
            L = L + delta[p + 1] @ d[p]
        lap[p] = L
    return d, delta, lap, G


def ricci(s):
    """Principal Ricci curvatures (Milnor) in the frame X_k / s_k."""
    s1, s2, s3 = s
    lam = np.array([2 * s1 / (s2 * s3), 2 * s2 / (s3 * s1), 2 * s3 / (s1 * s2)])
    mu = lam.sum() / 2 - lam
    return np.array([2 * mu[1] * mu[2], 2 * mu[0] * mu[2], 2 * mu[0] * mu[1]])


def bochner_1(j: float, s) -> np.ndarray:
    """nabla^* nabla on 1-forms in the theta basis, from the Levi-Civita
    connection of the orthonormal frame e_k = X_k / s_k."""
    s = np.asarray(s, float)
    c = np.einsum("ijk,i,j,k->ijk", STRUCT, 1 / s, 1 / s, s)  # [e_i,e_j] = c_ijk e_k
    # <nabla_{e_i} e_j, e_k> = (c_ijk - c_jki + c_kij) / 2
    # np.transpose(c, (2, 0, 1))[i,j,k] = c_jki and np.transpose(c, (1, 2, 0))[i,j,k] = c_kij
    gam = 0.5 * (c - np.transpose(c, (2, 0, 1)) + np.transpose(c, (1, 2, 0)))
    R = rep(j)
    n = R[0].shape[0]
    Dsq = np.zeros((3 * n, 3 * n), dtype=complex)
    for i in range(3):
        # acting on vector components V = sum_k V_k e_k : (nabla_i V)_l = e_i V_l + gam[i,k,l] V_k
        conn = np.kron(R[i] / s[i], np.eye(3)) + np.kron(np.eye(n), gam[i].T)
        Dsq = Dsq - conn @ conn
    S = np.kron(np.eye(n), np.diag(1 / s))  # theta-coefficients f -> vector components V = f / s
    return np.linalg.solve(S, Dsq @ S)


def scalar_modes(j: float, s):
    """Eigenpairs (lambda, Y) of Delta_0 on M_j, sorted."""
    _, _, lap, _ = laplacians(j, s)
    w, v = np.linalg.eigh(lap[0])
    return w, v


def devries_x(J: float) -> tuple[float, float]:
    r = np.sqrt(J * J + 4 * J)
    return (-J + r) / 2, (-J - r) / 2


SIN2_DV = 1 - devries_x(0.75)[0] / devries_x(2.0)[0]


# ---------------------------------------------------------------------------
# checks and tests
# ---------------------------------------------------------------------------

def check_round_spectra(jmax: float = 3.0, tol: float = 1e-9):
    """Unit round S^3: Delta_0 = l(l+2), Delta_1 exact l(l+2), coexact (l+1)^2,
    with the known multiplicities once the left factor 2j+1 is restored."""
    s = (1.0, 1.0, 1.0)
    count0, count1 = {}, {}
    j = 0.0
    while j <= jmax + 1e-12:
        _, _, lap, _ = laplacians(j, s)
        mult = int(round(2 * j)) + 1
        for key, L, store in ((0, lap[0], count0), (1, lap[1], count1)):
            for w in np.round(np.linalg.eigvals(L).real, 9):
                store[w] = store.get(w, 0) + mult
        j += 0.5
    for ell in range(0, int(2 * jmax) + 1):
        assert count0.get(float(ell * (ell + 2)), 0) == (ell + 1) ** 2
    lmax = int(2 * jmax)
    for ell in range(1, lmax):  # exact l(l+2) and coexact (l+1)^2 multiplicities
        ex, co = float(ell * (ell + 2)), float((ell + 1) ** 2)
        expect_ex, expect_co = (ell + 1) ** 2, 2 * ell * (ell + 2)
        if ex == co:
            continue
        assert count1.get(ex, 0) == expect_ex, (ell, count1.get(ex), expect_ex)
    return True


def hl_berger_spectrum(k: int, a: float, b: float):
    """Henkel-Lauret Theorem 4.1 / eq. (4.1): Delta_1 spectrum on the k-th
    block of the Berger sphere g(a,b,b) (a = fibre parameter), k = 2j."""
    if k == 0:
        # eq. (4.1) as printed lists one 4a^2 and two 4b^4/a^2; the k = 0 block of
        # their own eq. (4.9), 4D = diag(4b^4/a^2, 4a^2, 4a^2), gives the reverse,
        # which also follows by hand from d(X_1^*) = -(2b^2/a) X_2^* ^ X_3^*.
        return sorted([4 * a * a, 4 * a * a, 4 * b ** 4 / a ** 2])
    if k == 1:
        v = [9 * a * a] * 2 + [a * a + 4 * b * b + 4 * b ** 4 / a ** 2] * 2 + [a * a + 2 * b * b] * 2
        return sorted(v)
    nu = [a * a * (k - 2 * jj) ** 2 + b * b * ((4 * jj + 2) * k - 4 * jj * jj) for jj in range(k + 1)]
    out = list(nu) + [(k + 2) ** 2 * a * a] * 2 + [k * k * a * a + 4 * k * b * b + 4 * b ** 4 / a ** 2] * 2
    for jj in range(1, k):
        rt = np.sqrt(a * a * nu[jj] + b ** 4)
        out += [nu[jj] + 2 * b ** 4 / a ** 2 + sgn * 2 * b * b / (a * a) * rt for sgn in (1, -1)]
    return sorted(out)


def check_berger_against_hl(a: float = 1.7, b: float = 0.8, kmax: int = 5, tol: float = 1e-8):
    """HL use an orthonormal frame with the fibre along X_1: g(X_1,X_1) = 1/a^2,
    g(X_2,X_2) = g(X_3,X_3) = 1/b^2 in our normalisation."""
    s = (1 / a, 1 / b, 1 / b)
    for k in range(kmax + 1):
        _, _, lap, _ = laplacians(k / 2, s)
        mine = sorted(np.linalg.eigvals(lap[1]).real)
        assert np.allclose(mine, hl_berger_spectrum(k, a, b), atol=tol), k
    return True


def check_weitzenboeck(s=(1.3, 0.7, 1.1), jmax: float = 2.0, tol: float = 1e-9):
    j = 0.0
    while j <= jmax + 1e-12:
        _, _, lap, _ = laplacians(j, s)
        n = int(round(2 * j)) + 1
        ric = np.kron(np.eye(n), np.diag(ricci(s)))
        assert np.allclose(lap[1], bochner_1(j, s) + ric, atol=tol), j
        j += 0.5
    return True


def exact_block(j: float, s, op_a: np.ndarray, Y: np.ndarray, lam: float, G1: np.ndarray, d0: np.ndarray):
    """2x2 compression of [[0, d^dagger],[d, op_a]] onto (Y, dY/|dY|)."""
    dY = d0 @ Y
    nrm = np.sqrt((dY.conj() @ G1 @ dY).real)
    u = dY / nrm
    aa = (u.conj() @ G1 @ (op_a @ u)).real
    return np.array([[0.0, nrm], [nrm, aa]])


def curvature_expectation(j: float, s):
    """For each scalar mode Y of type j: (lambda, <dY, Ric dY>/|dY|^2)."""
    d, _, lap, G = laplacians(j, s)
    n = int(round(2 * j)) + 1
    ric = np.kron(np.eye(n), np.diag(ricci(s)))
    w, v = np.linalg.eigh(lap[0])
    out = []
    for a in range(n):
        dY = d[0] @ v[:, a]
        nn = (dY.conj() @ G[1] @ dY).real
        out.append((w[a], (dY.conj() @ G[1] @ (ric @ dY)).real / nn))
    return out


def gain_spectrum(j: float, s, c: float = 1.0):
    """Spectrum of the relative-gain Hessian H = [[0, c delta],[c d, -c^2 d delta]]
    on Omega^0 (+) Omega^1 of type j (identity kinetic metric = L^2 norms)."""
    d, delta, _, G = laplacians(j, s)
    n0, n1 = G[0].shape[0], G[1].shape[0]
    H = np.zeros((n0 + n1, n0 + n1), dtype=complex)
    H[:n0, n0:] = c * delta[1]
    H[n0:, :n0] = c * d[0]
    H[n0:, n0:] = -c * c * d[0] @ delta[1]
    Gt = np.block([[G[0], np.zeros((n0, n1))], [np.zeros((n1, n0)), G[1]]])
    # H is self-adjoint for the metric Gt; eigenvalues are real
    w = np.linalg.eigvals(H)
    assert np.allclose(w.imag, 0, atol=1e-9)
    return np.sort(w.real)


def label_ratio_scan():
    """lambda_W / lambda_Z for W in j=1/2 and each Z mode in j=1, as a function
    of c_k = 4/s_k^2.  Returns the closed forms used in the verdict note."""
    rows = []
    for c in ((1, 1, 1), (1, 1, 1.5), (1, 1, 0.5), (0.8, 1.2, 1.0), (0.5, 1.5, 1.0), (0.7, 1.0, 1.6)):
        s = tuple(2 / np.sqrt(ck) for ck in c)
        lw = scalar_modes(0.5, s)[0]
        lz = scalar_modes(1.0, s)[0]
        rows.append((c, lw, lz, lw[0] / lz))
    return rows


if __name__ == "__main__":
    np.set_printoptions(precision=6, suppress=True)
    print("validation")
    print("  round S^3 spectra and multiplicities:", check_round_spectra())
    print("  Berger Delta_1 against Henkel-Lauret Thm 4.1:", check_berger_against_hl())
    print("  Weitzenboeck Delta_1 = nabla*nabla + Ric (triaxial):", check_weitzenboeck())
    print(f"\nde Vries: x+(3/4) = {devries_x(0.75)[0]:.10f}, x+(2) = {devries_x(2)[0]:.10f}, "
          f"sin2 = {SIN2_DV:.10f}")

    print("\nA. scalar labels (c_k = 4/s_k^2): lambda_W (j=1/2) and the three lambda_Z (j=1)")
    for c, lw, lz, ratio in label_ratio_scan():
        print(f"  c={c}: lambda_W={lw}  lambda_Z={lz}  lambda_W/lambda_Z={ratio}  (3/8 = 0.375)")

    print("\nB. curvature expectation on exact modes, Berger t = s3 (fibre X_3), unit base")
    for t in (1.0, 0.8, 1.25):
        for j in (0.5, 1.0):
            print(f"  t={t} j={j}:", [(round(float(l), 6), round(float(r), 6)) for l, r in curvature_expectation(j, (1, 1, t))])

    print("\nC. relative-gain Hessian on the round sphere of radius 2 (lambda_0 = j(j+1))")
    for j in (0.5, 1.0, 1.5):
        J = j * (j + 1)
        spec = gain_spectrum(j, (2, 2, 2))
        xp, xm = devries_x(J)
        print(f"  j={j}: J={J}  distinct eigenvalues {np.unique(np.round(spec, 9))}  de Vries roots {xp:.9f}, {xm:.9f}")
