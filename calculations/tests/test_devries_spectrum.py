from math import isclose

from calculations.devries_spectrum import J_from_spin, roots_from_J, sin2_devries, mw_from_mz


def test_J_values():
    assert isclose(J_from_spin(0.5), 0.75)
    assert isclose(J_from_spin(1.0), 2.0)


def test_branch_product():
    for J in (0.75, 2.0, 10.0):
        r = roots_from_J(J)
        assert isclose(r.x_plus * r.x_minus, -J, rel_tol=1e-14)
        assert isclose(r.x_plus + r.x_minus, -J, rel_tol=1e-14)


def test_devries_number():
    assert isclose(sin2_devries(), 0.22310132, rel_tol=0, abs_tol=5e-9)


def test_mw_from_mz_seed():
    assert isclose(mw_from_mz(91.1880), 80.3748, rel_tol=0, abs_tol=5e-4)
