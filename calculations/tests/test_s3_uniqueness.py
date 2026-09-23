"""Symbolic checks for calculations/s3_uniqueness.md."""
import pytest

sp = pytest.importorskip("sympy")


def _u2_system(with_photon: bool):
    J, mu2 = sp.symbols("J mu2", positive=True)
    p0, p1, s0, s1, B = sp.symbols("p0 p1 s0 s1 B", real=True)  # B = nu * b^2
    P, S = p0 + p1 * J, s0 + s1 * J
    eqs = [sp.Eq(p0, 0)] if with_photon else []
    for Jv in (sp.Rational(3, 4), 2):
        eqs.append(sp.Eq((P + S).subs(J, Jv), -mu2 * Jv))
        eqs.append(sp.Eq((P * S - B * J).subs(J, Jv), -mu2 ** 2 * Jv))
    unknowns = [p0, p1, s0, s1, B] if with_photon else [p0, s0, s1, B]
    return sp.solve(eqs, unknowns, dict=True), (p0, p1, s0, s1, B, mu2)


def test_u2_photon_makes_the_two_level_construction_unique():
    sols, (p0, p1, s0, s1, B, mu2) = _u2_system(with_photon=True)
    found = {(s[p0], s[p1], s[s0], s[s1], s[B]) for s in sols}
    assert found == {(0, 0, 0, -mu2, mu2 ** 2), (0, -mu2, 0, 0, mu2 ** 2)}


def test_u2_without_photon_leaves_a_family():
    sols, (p0, p1, s0, s1, B, mu2) = _u2_system(with_photon=False)
    assert sols and all(p1 not in s for s in sols)  # p1 stays free
    assert any(s[p0].has(p1) for s in sols)


def test_u1_lemma_low_degree():
    J, nu, mu2 = sp.symbols("J nu mu2", positive=True)
    c = sp.symbols("c0:4", real=True)
    d = sp.symbols("d0:2", real=True)
    S = sum(ci * J ** i for i, ci in enumerate(c))
    b = d[0] + d[1] * J
    poly = sp.Poly(sp.expand(S ** 2 + mu2 * J * S + nu * J * b ** 2 - mu2 ** 2 * J), J)
    sols = sp.solve(poly.coeffs(), list(c) + list(d), dict=True)
    shapes = {(sp.simplify(s[c[0]]), sp.simplify(s[c[1]]), s[c[2]], s[c[3]], s[d[1]]) for s in sols}
    assert shapes == {(0, 0, 0, 0, 0), (0, -mu2, 0, 0, 0)}
    assert all(sp.simplify(s[d[0]] ** 2 - mu2 ** 2 / nu) == 0 for s in sols)
