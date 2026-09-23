#!/usr/bin/env python3
"""Compare the signed-root prediction under historical and current inputs."""

from __future__ import annotations

import sympy as sp


sqrt = sp.sqrt
xZ = sqrt(3) - 1
xW = (sqrt(57) - 3) / 8
xH = (5 * sqrt(57) + 24 * sqrt(3) + 9) / 64
xF = (40 * sqrt(3) + 3 * sqrt(57) + 79) / 64

MZ_INPUTS = {
    "project_statement": sp.Float("91.1876"),
    "PDG_2024_summary": sp.Float("91.1880"),
    "PDGLive_2026_accessed_2026_05_14": sp.Float("91.1879"),
}

GF_INPUTS = {
    "PDG_value_used_in_project": sp.Float("1.1663788e-5"),
    "NIST_CODATA_2022": sp.Float("1.1663787e-5"),
}


def masses_from_mz(mz: sp.Float) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    scale = mz / sqrt(xZ)
    return scale * sqrt(xW), scale * sqrt(xH), scale * sqrt(xF)


def v_over_sqrt2(gf: sp.Float) -> sp.Expr:
    v = 1 / sqrt(sqrt(2) * gf)
    return v / sqrt(2)


def main() -> None:
    print("Masses from signed-root formula")
    print("label,M_Z,M_W0,M_H,M_F")
    for label, mz in MZ_INPUTS.items():
        mw, mh, mf = masses_from_mz(mz)
        print(f"{label},{mz:.7f},{mw.evalf(12)},{mh.evalf(12)},{mf.evalf(12)}")

    print()
    print("Fermi scale comparison")
    print("label,G_F,v/sqrt(2)")
    for label, gf in GF_INPUTS.items():
        print(f"{label},{gf:.8e},{v_over_sqrt2(gf).evalf(12)}")

    print()
    print("Current PDGLive comparison, accessed 2026-05-14")
    print("PDGLive M_W = 80.3625 +/- 0.0077 GeV")
    print("PDGLive M_Z = 91.1879 +/- 0.0020 GeV")
    print("PDGLive m_H = 125.13 +/- 0.11 GeV")
    mw, mh, mf = masses_from_mz(MZ_INPUTS["PDGLive_2026_accessed_2026_05_14"])
    print(f"signed-root M_W0 - PDGLive M_W = {(mw - sp.Float('80.3625')).evalf(8)} GeV")
    print(f"signed-root M_H  - PDGLive m_H = {(mh - sp.Float('125.13')).evalf(8)} GeV")
    print(f"signed-root M_F  - v/sqrt(2), CODATA 2022 = {(mf - v_over_sqrt2(GF_INPUTS['NIST_CODATA_2022'])).evalf(8)} GeV")


if __name__ == "__main__":
    main()
