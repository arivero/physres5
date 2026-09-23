#!/usr/bin/env python3
"""Compare the positive-branch de Vries weak angle with on-shell inputs."""

from __future__ import annotations

from dataclasses import dataclass
import math
import sympy as sp


@dataclass(frozen=True)
class InputSet:
    label: str
    m_z: float
    m_w: float


def main() -> None:
    sqrt = sp.sqrt
    x_z = sqrt(3) - 1
    x_w = (sqrt(57) - 3) / 8
    sin2_dv = sp.simplify(1 - x_w / x_z)

    inputs = [
        InputSet("project_root_prediction", 91.1876, 80.3744430708),
        InputSet("PDG_2024_summary", 91.1880, 80.3692),
        InputSet("PDGLive_2026_accessed_2026_05_14", 91.1879, 80.3692),
    ]

    print("Positive-branch weak-angle comparison")
    print("-------------------------------------")
    print(f"sin^2(theta)_deVries exact = {sp.sstr(sin2_dv)}")
    sin2_dv_float = float(sin2_dv.evalf(16))
    print(f"sin^2(theta)_deVries = {sin2_dv_float:.12f}")
    print()

    for item in inputs:
        sin2 = 1.0 - (item.m_w**2 / item.m_z**2)
        print(item.label)
        print(f"  M_Z = {item.m_z:.7f} GeV, M_W = {item.m_w:.10f} GeV")
        print(f"  sin^2(theta)_OS = {sin2:.12f}")
        print(f"  OS - deVries = {sin2 - sin2_dv_float:+.12e}")
        print(f"  implied M_W from deVries at this M_Z = {item.m_z * math.sqrt(float(x_w / x_z)):.10f} GeV")
        print()

    print("Conclusion")
    print("----------")
    print(
        "The positive branch fixes an on-shell weak angle near 0.22310.  "
        "Using current W and Z pole inputs gives a nearby but distinct value.  "
        "This does not affect the exact signed-root algebra, but it reinforces "
        "that the construction is an on-shell phenomenological relation rather "
        "than a replacement for the electroweak fit."
    )


if __name__ == "__main__":
    main()
