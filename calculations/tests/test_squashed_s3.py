"""Checks for calculations/squashed_s3.py (validation against known spectra and
the de Vries block statements of calculations/squashed_s3_verdict.md)."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import squashed_s3 as q  # noqa: E402


def test_round_sphere_spectra():
    assert q.check_round_spectra(jmax=2.0)


def test_berger_matches_henkel_lauret():
    assert q.check_berger_against_hl(a=1.7, b=0.8, kmax=4)
    assert q.check_berger_against_hl(a=0.6, b=1.3, kmax=4)


def test_weitzenboeck_identity_triaxial():
    assert q.check_weitzenboeck(s=(1.3, 0.7, 1.1), jmax=1.5)


def test_gain_hessian_gives_devries_on_round_radius_two():
    for j in (0.5, 1.0, 1.5):
        J = j * (j + 1)
        spec = q.gain_spectrum(j, (2.0, 2.0, 2.0))
        xp, xm = q.devries_x(J)
        assert np.isclose(spec, xp, atol=1e-9).any() and np.isclose(spec, xm, atol=1e-9).any()
        others = spec[~(np.isclose(spec, xp, atol=1e-9) | np.isclose(spec, xm, atol=1e-9))]
        assert np.allclose(others, 0.0, atol=1e-9)  # coexact 1-forms are zero modes


def test_labels_survive_only_on_mean_axis_family():
    # W level: lambda = tr(c)/4 for any left-invariant metric
    for c in ((1, 1, 1), (0.8, 1.2, 1.0), (1, 1, 1.5)):
        s = tuple(2 / np.sqrt(ck) for ck in c)
        lw = q.scalar_modes(0.5, s)[0]
        lz = np.sort(q.scalar_modes(1.0, s)[0])
        assert np.allclose(lw, sum(c) / 4)
        assert np.allclose(lz, np.sort([sum(c) - ck for ck in c]))
    # Berger (two equal c): ratio 3/8 only at the round point
    for c3 in (0.5, 0.9, 1.1, 1.5):
        s = (2.0, 2.0, 2 / np.sqrt(c3))
        lw = q.scalar_modes(0.5, s)[0][0]
        lz = q.scalar_modes(1.0, s)[0]
        assert not np.isclose(lw / lz, 0.375).any()


def test_curvature_expectation_is_constant_on_round_sphere():
    for j in (0.5, 1.0, 1.5):
        rhos = [r for _, r in q.curvature_expectation(j, (1.0, 1.0, 1.0))]
        assert np.allclose(rhos, 2.0)
