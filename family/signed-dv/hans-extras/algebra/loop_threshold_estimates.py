#!/usr/bin/env python3
"""Loop, threshold, and D-term size estimates for the 3/8 correction."""

from __future__ import annotations

import math
from dataclasses import dataclass


KAPPA_TARGET = 3.0 / 8.0
C_F = 3.0 / 4.0
T3_SQUARED_F = 1.0 / 4.0
V_GEV = 246.21965


@dataclass(frozen=True)
class LoopEstimate:
    label: str
    group_factor: float

    @property
    def kappa_for_unit_loop_coefficient(self) -> float:
        # delta m^2 = A * g'^2 * C * v^2 / (16 pi^2)
        # M_Z^2 - M_W^2 = g'^2 v^2 / 4
        # kappa = delta/gap = A C/(4 pi^2)
        return self.group_factor / (4.0 * math.pi**2)

    @property
    def coefficient_needed(self) -> float:
        return KAPPA_TARGET / self.kappa_for_unit_loop_coefficient

    @property
    def heavy_mass_over_v_for_unit_coefficient(self) -> float:
        # delta m^2 = g'^2 C M^2/(16 pi^2), target = (3/32)g'^2 v^2.
        # M^2/v^2 = (3/32)(16 pi^2)/C.
        return math.sqrt((3.0 / 32.0) * (16.0 * math.pi**2) / self.group_factor)


def main() -> None:
    estimates = [
        LoopEstimate("full fundamental Casimir C_F=3/4", C_F),
        LoopEstimate("single hypercharge generator (T^3)^2=1/4", T3_SQUARED_F),
    ]

    print("Target normalization")
    print("--------------------")
    print("M_Z^2 - M_W^2 = g'^2 v^2 / 4")
    print("epsilon_target = (3/8)(M_Z^2-M_W^2) = (3/32) g'^2 v^2")
    print(f"kappa_target = {KAPPA_TARGET:.12f}")
    print(f"epsilon_target/(g'^2 v^2) = {3.0/32.0:.12f}")
    print()

    print("Perturbative one-loop estimate")
    print("------------------------------")
    print("Assume delta m^2 = A g'^2 C v^2/(16 pi^2).")
    for item in estimates:
        print()
        print(item.label)
        print(f"  kappa(A=1) = {item.kappa_for_unit_loop_coefficient:.12f}")
        print(f"  A needed for kappa=3/8 = {item.coefficient_needed:.12f}")
    print()

    print("Quadratic heavy-threshold scale estimate")
    print("----------------------------------------")
    print("Assume delta m^2 = g'^2 C M^2/(16 pi^2) with unit finite coefficient.")
    for item in estimates:
        ratio = item.heavy_mass_over_v_for_unit_coefficient
        print()
        print(item.label)
        print(f"  M/v needed = {ratio:.12f}")
        print(f"  M needed for v={V_GEV:.5f} GeV = {ratio * V_GEV:.6f} GeV")
    print()

    print("Tree-level U(1) D-term cross-check")
    print("----------------------------------")
    print("For V_D = g'^2/2 (q_H |H|^2 + q_S |S|^2)^2,")
    print("delta m_S^2 = g'^2 q_H q_S v^2/2 and kappa = 2 q_H q_S.")
    print("With q_H=1/2, kappa=q_S.")
    print(f"q_S needed for kappa=3/8: {KAPPA_TARGET:.12f}")
    print(
        "This is a charge assignment or matching coefficient, not the SU(2) "
        "Casimir ratio.  A pair with opposite q_S could give a traceless split, "
        "but the charge magnitude is put in by hand."
    )


if __name__ == "__main__":
    main()
