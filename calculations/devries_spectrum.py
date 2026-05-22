#!/usr/bin/env python3
"""Compute the DeVries positive/negative branch numbers used in the manuscript."""
from __future__ import annotations

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class BranchValues:
    J: float
    x_plus: float
    x_minus: float


def roots_from_J(J: float) -> BranchValues:
    if J <= 0:
        raise ValueError("J must be positive")
    disc = sqrt(J * J + 4.0 * J)
    return BranchValues(J=J, x_plus=(disc - J) / 2.0, x_minus=-(disc + J) / 2.0)


def J_from_spin(s: float) -> float:
    if s <= 0:
        raise ValueError("spin label s must be positive")
    return s * (s + 1.0)


def sin2_devries() -> float:
    w = roots_from_J(J_from_spin(0.5)).x_plus
    z = roots_from_J(J_from_spin(1.0)).x_plus
    return 1.0 - w / z


def mw_from_mz(mz: float) -> float:
    return mz * sqrt(1.0 - sin2_devries())


def main() -> None:
    vals = {
        "J_W=s(s+1), s=1/2": roots_from_J(J_from_spin(0.5)),
        "J_Z=s(s+1), s=1": roots_from_J(J_from_spin(1.0)),
    }
    for label, v in vals.items():
        print(f"{label}: J={v.J:.12g}, x_plus={v.x_plus:.12g}, x_minus={v.x_minus:.12g}")
    sdv = sin2_devries()
    print(f"sin^2(theta_dV) = {sdv:.12f}")
    print(f"M_W from M_Z=91.1880 GeV = {mw_from_mz(91.1880):.6f} GeV")


if __name__ == "__main__":
    main()
