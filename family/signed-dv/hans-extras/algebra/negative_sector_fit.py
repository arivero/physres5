#!/usr/bin/env python3
"""Fit the physical negative-sector shifts to trace/traceless components."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


sqrt = sp.sqrt
xZ = sqrt(3) - 1
xW = (sqrt(57) - 3) / 8
xH0_abs = (sqrt(57) + 3) / 8
xF0_abs = sqrt(3) + 1


@dataclass(frozen=True)
class InputCase:
    label: str
    mz: str
    mh: str
    gf: str


CASES = [
    InputCase("project_statement", "91.1876", "125.20", "1.1663788e-5"),
    InputCase("PDG_2024_summary", "91.1880", "125.20", "1.1663788e-5"),
    InputCase("PDGLive_2026_accessed_2026_05_14", "91.1879", "125.13", "1.1663787e-5"),
]


def v_over_sqrt2(gf: sp.Float) -> sp.Expr:
    v = 1 / sp.sqrt(sp.sqrt(2) * gf)
    return v / sp.sqrt(2)


def analyze(case: InputCase) -> dict[str, sp.Expr]:
    mz = sp.Float(case.mz)
    mh_phys = sp.Float(case.mh)
    gf = sp.Float(case.gf)
    scale = mz / sqrt(xZ)

    mw0 = scale * sqrt(xW)
    mh0 = scale * sqrt(xH0_abs)
    mf0 = scale * sqrt(xF0_abs)
    mf_phys = v_over_sqrt2(gf)

    gap = mz**2 - mw0**2
    target_eps = sp.Rational(3, 8) * gap

    delta_h = mh_phys**2 - mh0**2
    delta_f = mf_phys**2 - mf0**2
    trace_shift = delta_h + delta_f
    traceless_eps_fit = (delta_h - delta_f) / 2

    return {
        "MZ": mz,
        "MH_phys": mh_phys,
        "MF_phys": mf_phys,
        "MW0": mw0,
        "MH0": mh0,
        "MF0": mf0,
        "gap": gap,
        "target_eps": target_eps,
        "delta_H": delta_h,
        "delta_F": delta_f,
        "kappa_H": delta_h / gap,
        "kappa_F": -delta_f / gap,
        "kappa_traceless": traceless_eps_fit / gap,
        "trace_shift": trace_shift,
        "trace_shift_over_gap": trace_shift / gap,
        "H_residual_at_3_8": delta_h - target_eps,
        "F_residual_at_3_8": delta_f + target_eps,
    }


def main() -> None:
    print("Negative-sector physical fit")
    print("----------------------------")
    for case in CASES:
        row = analyze(case)
        print()
        print(case.label)
        print(f"  inputs: M_Z={case.mz} GeV, m_H={case.mh} GeV, G_F={case.gf} GeV^-2")
        print(f"  M_W0={row['MW0'].evalf(12)} GeV, M_H0={row['MH0'].evalf(12)} GeV, M_F0={row['MF0'].evalf(12)} GeV")
        print(f"  M_F physical=v/sqrt(2)={row['MF_phys'].evalf(12)} GeV")
        print(f"  gap=M_Z^2-M_W0^2={row['gap'].evalf(12)} GeV^2")
        print(f"  target eps=(3/8)gap={row['target_eps'].evalf(12)} GeV^2")
        print(f"  delta_H={row['delta_H'].evalf(12)} GeV^2,  delta_F={row['delta_F'].evalf(12)} GeV^2")
        print(f"  kappa_H=delta_H/gap={row['kappa_H'].evalf(10)}")
        print(f"  kappa_F=-delta_F/gap={row['kappa_F'].evalf(10)}")
        print(f"  kappa_traceless=(delta_H-delta_F)/(2 gap)={row['kappa_traceless'].evalf(10)}")
        print(f"  trace_shift=(delta_H+delta_F)={row['trace_shift'].evalf(12)} GeV^2")
        print(f"  trace_shift/gap={row['trace_shift_over_gap'].evalf(10)}")
        print(f"  residuals at 3/8: H={row['H_residual_at_3_8'].evalf(10)} GeV^2, F={row['F_residual_at_3_8'].evalf(10)} GeV^2")

    print()
    print("Conclusion")
    print("  The Higgs shift alone is very close to 3/8 for the historical")
    print("  m_H=125.20 input.  The Fermi/vev shift prefers a larger coefficient")
    print("  near 0.388.  The traceless best-fit coefficient is near, but not")
    print("  exactly, 3/8; the trace leak is small but not zero.")


if __name__ == "__main__":
    main()
