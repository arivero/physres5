#!/usr/bin/env python3
"""Verify the exact signed de Broglie--de Vries identities.

Run:
    python algebra/verify_signed_roots.py
"""

import sympy as sp

sqrt = sp.sqrt
N = sp.N

# Inputs
MZ = sp.Rational(911876, 10000)  # 91.1876 GeV
GF = sp.Float("1.1663787e-5")
mh = sp.Float("125.20")

# Casimirs
C1 = sp.Rational(2, 1)
Ch = sp.Rational(3, 4)
CF_over_CA = sp.simplify(Ch / C1)

# Roots
x1p = sqrt(3) - 1
x1m = -(sqrt(3) + 1)
xhp = (sqrt(57) - 3) / 8
xhm = -(sqrt(57) + 3) / 8

print("=== Exact root checks ===")
checks = [
    ("s=1 sum", sp.simplify(x1p + x1m), -C1),
    ("s=1 product", sp.simplify(x1p * x1m), -C1),
    ("s=1/2 sum", sp.simplify(xhp + xhm), -Ch),
    ("s=1/2 product", sp.simplify(xhp * xhm), -Ch),
]
for name, value, expected in checks:
    print(f"{name:18s}: {value}  expected {expected}  ok={sp.simplify(value-expected)==0}")

trace_ratio = sp.simplify((xhp + xhm) / (x1p + x1m))
det_ratio = sp.simplify((xhp * xhm) / (x1p * x1m))
pos_ratio = sp.simplify(xhp / x1p)

print("\n=== Ratios ===")
print("C_F/C_A     =", CF_over_CA)
print("trace ratio =", trace_ratio)
print("det ratio   =", det_ratio)
print("MW^2/MZ^2   =", pos_ratio, "=", N(pos_ratio, 15))
print("sin^2 dV    =", sp.simplify(1 - pos_ratio), "=", N(1 - pos_ratio, 15))

# Masses
Mcal = sp.simplify(MZ / sp.sqrt(x1p))
MW0 = sp.simplify(Mcal * sp.sqrt(xhp))
MH0 = sp.simplify(Mcal * sp.sqrt(-xhm))
MF0 = sp.simplify(Mcal * sp.sqrt(-x1m))

print("\n=== Mass slots, MZ=91.1876 GeV ===")
print("Mcal =", N(Mcal, 15))
print("MW0  =", N(MW0, 15))
print("MH0  =", N(MH0, 15))
print("MF0  =", N(MF0, 15))

# Custodial correction
gap = sp.simplify(MZ**2 - MW0**2)
eps = sp.simplify(CF_over_CA * gap)
MHcorr = sp.sqrt(MH0**2 + eps)
MFcorr = sp.sqrt(MF0**2 - eps)

v = 1 / sp.sqrt(sp.sqrt(2) * GF)
vF = v / sp.sqrt(2)

print("\n=== Custodial/Casimir correction ===")
print("MZ^2 - MW0^2        =", N(gap, 15))
print("(3/8)(MZ^2-MW0^2)   =", N(eps, 15))
print("MH corrected         =", N(MHcorr, 15))
print("MF corrected         =", N(MFcorr, 15))
print("v/sqrt(2)            =", N(vF, 15))
print("MFcorr - v/sqrt(2)   =", N(MFcorr - vF, 15))

DeltaH = mh**2 - MH0**2
DeltaF = vF**2 - MF0**2
Delta_trl = (DeltaH - DeltaF) / 2

print("\n=== Physical deltas, using mh=125.20 GeV ===")
print("DeltaH               =", N(DeltaH, 15))
print("DeltaF               =", N(DeltaF, 15))
print("DeltaH + DeltaF      =", N(DeltaH + DeltaF, 15))
print("Delta_traceless      =", N(Delta_trl, 15))
print("DeltaH/gap           =", N(DeltaH / gap, 15))
print("-DeltaF/gap          =", N(-DeltaF / gap, 15))
print("Delta_traceless/gap  =", N(Delta_trl / gap, 15))

# Exact corrected mass-square ratios
MHcorr_ratio = sp.simplify((MH0**2 + eps) / MZ**2)
MFcorr_ratio = sp.simplify((MF0**2 - eps) / MZ**2)
print("\n=== Exact corrected ratios ===")
print("MHcorr^2/MZ^2 =", MHcorr_ratio)
print("MFcorr^2/MZ^2 =", MFcorr_ratio)
