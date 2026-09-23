# Core identities of the de Vries relation: the three equivalent forms
# (quadratic / gap fixed point / relativistic orbit), the exact W/Z values,
# the weak angle, and the residue bound that kills the Z=0 compositeness
# candidate (ledger b'). Every claim asserted; exit 0 = all verified.
import sympy as sp

C = sp.symbols('C', positive=True)
Xp = (-C + sp.sqrt(C**2 + 4*C)) / 2

# 1. Xp solves the quadratic X^2 + C X - C = 0
assert sp.simplify(Xp**2 + C*Xp - C) == 0

# 2. Gap form: X = C/(X+C) at X = Xp
assert sp.simplify(C/(Xp + C) - Xp) == 0

# 3. Bounds 0 < Xp < 1 (orbit reading needs Xp < 1): Xp<1 iff C^2+4C < (C+2)^2
assert sp.simplify(sp.expand((C + 2)**2 - (C**2 + 4*C))) == 4

# 4. Orbit form: X = beta^2 with beta^2*gamma = sqrt(C), gamma = 1/sqrt(1-X)
#    i.e. C = X^2/(1-X) at X = Xp
assert sp.simplify(Xp**2/(1 - Xp) - C) == 0

# 5. Exact W/Z values
XW = Xp.subs(C, sp.Rational(3, 4))
XZ = Xp.subs(C, 2)
assert sp.simplify(XW - (sp.sqrt(57) - 3)/8) == 0
assert sp.simplify(XZ - (sp.sqrt(3) - 1)) == 0

sin2 = sp.simplify(1 - XW/XZ)
sin2_num = sp.N(sin2, 30)
assert abs(float(sin2_num) - 0.2231013223008662) < 1e-15
ratio_dV = sp.sqrt(1 - sin2)          # m_W/m_Z predicted
ratio_num = sp.N(ratio_dV, 30)

# 6. Monotonicity of Xp(C) (used by the uniqueness re-score): dXp/dC > 0
dXp = sp.diff(Xp, C)
# dXp = (-1 + (C+2)/sqrt(C^2+4C))/2 > 0 iff (C+2)^2 > C^2+4C, true by (3)
assert sp.simplify(dXp - (sp.Rational(-1, 2) + (C + 2)/(2*sp.sqrt(C**2 + 4*C)))) == 0

# 7. Ledger candidate (b') fast kill: rank-one single-pole resolvent residue.
#    Dressed pole residue Z satisfies Z^{-1} = 1 + C/(Xp+C)^2 > 1 strictly,
#    so Z in (0,1); Z -> 0 needs Xp+C -> 0, impossible for C>0. The Weinberg
#    Z=0 compositeness condition is inconsistent with this spectral shape.
Zinv = 1 + C/(Xp + C)**2
ZW = float(1/sp.N(Zinv.subs(C, sp.Rational(3, 4))))
ZZ = float(1/sp.N(Zinv.subs(C, 2)))
assert 0 < ZW < 1 and 0 < ZZ < 1

# 8. Sugawara control identity: map weighted by c gives X^2 + c^2 C X - c^2 C = 0,
#    whose positive root is Xp(c^2 C) ... NOT of the form needed: check the
#    actual control number used in the prior run: c = 1/2 (Delta = J/4):
#    sin^2_control = 1 - Xp(3/16)/Xp(1/2)
sin2_sug = float(sp.N(1 - Xp.subs(C, sp.Rational(3, 16))/Xp.subs(C, sp.Rational(1, 2)), 20))
assert abs(sin2_sug - 0.301410) < 5e-7   # the failed-control value in the record

print("devries_core: ALL CHECKS PASS")
print("  X_W = (sqrt57-3)/8 =", sp.N(XW, 25))
print("  X_Z = sqrt3-1      =", sp.N(XZ, 25))
print("  sin^2 theta_dV     =", sin2_num)
print("  (m_W/m_Z)_dV       =", ratio_num)
print("  residues Z_W, Z_Z  =", round(ZW, 6), round(ZZ, 6), "(both in (0,1); Z=0 impossible)")
print("  Sugawara control   = sin^2 =", sin2_sug, "(fails vs ~0.223)")
