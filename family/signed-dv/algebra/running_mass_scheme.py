#!/usr/bin/env python3
"""Renormalization-scheme dependence of the electroweak vev.

Question we are answering: the dV construction predicts
    M_F^(corrected) = 174.175 GeV
and identifies this with v/sqrt(2). The Fermi-constant value is
    v/sqrt(2)|_GF = 174.10358 GeV.
This is a ~0.04% (25 GeV^2 at the M^2 level) discrepancy. Can the
standard SM one-loop Delta r connecting G_F to the on-shell or
MS-bar vev cover that gap?

We compute:

  (1) The one-loop Delta r in the on-shell scheme (Sirlin 1980,
      Bardin/Passarino conventions), broken into
        Delta r = Delta alpha - (c_W^2/s_W^2) Delta rho + Delta r_rem.
  (2) The vev in three flavors:
        v_bare   = (sqrt(2) G_F)^(-1/2)                  (Fermi)
        v_pole   = 2 M_W / g_pole          (on-shell)
        v_MSbar  = MS-bar vev at scale mu (m_t or M_Z)
      via v_pole^2 = v_bare^2 (1 - Delta r).
  (3) Whether v_target = sqrt(2)*174.175 = 246.32 GeV can land on
      any of those at a natural scale.
  (4) "Physical Higgs vacuum" sum-of-fermion-mass-squared tests.
"""

import math

# ---------------------------------------------------------------------------
# PDG / standard inputs
# ---------------------------------------------------------------------------
GF       = 1.1663787e-5      # GeV^-2
MZ       = 91.1876           # GeV
MW       = 80.369            # GeV (PDG world average; CDF outlier omitted)
mt_pole  = 172.69            # GeV (PDG top pole mass)
mh       = 125.20            # GeV
mb       = 4.18              # GeV (MS-bar at mb)
mtau     = 1.77686
mc       = 1.27
ms       = 0.093
mu_q     = 0.00216
md       = 0.00467
me       = 0.000510999
mmu      = 0.1056584

alpha_em_0    = 1.0/137.035999084   # Thomson limit
alpha_em_MZ   = 1.0/127.951         # PDG running EM coupling at MZ
alpha_s_MZ    = 0.1179
Delta_alpha   = 1.0 - alpha_em_0 / alpha_em_MZ   # ~ 0.05900

print("="*72)
print("Inputs")
print("="*72)
print(f"G_F            = {GF:.7e} GeV^-2")
print(f"M_Z            = {MZ} GeV")
print(f"M_W (PDG)      = {MW} GeV")
print(f"m_t (pole)     = {mt_pole} GeV")
print(f"m_h            = {mh} GeV")
print(f"alpha(0)       = 1/{1/alpha_em_0:.5f}")
print(f"alpha(M_Z)     = 1/{1/alpha_em_MZ:.5f}")
print(f"alpha_s(M_Z)   = {alpha_s_MZ}")
print(f"Delta alpha    = {Delta_alpha:.6f}")
print()

# ---------------------------------------------------------------------------
# Derived bare/Fermi vev
# ---------------------------------------------------------------------------
v_bare    = 1.0 / math.sqrt(math.sqrt(2.0) * GF)
v_over_s2 = v_bare / math.sqrt(2.0)
print(f"v_bare = (sqrt(2) G_F)^(-1/2)   = {v_bare:.6f} GeV")
print(f"v_bare / sqrt(2)                = {v_over_s2:.6f} GeV")

# Target from dV construction
MF_corrected = 174.175       # GeV
v_target = math.sqrt(2.0) * MF_corrected
print(f"M_F (dV)                         = {MF_corrected} GeV")
print(f"v_target = sqrt(2) * M_F (dV)    = {v_target:.6f} GeV")
print()

# ---------------------------------------------------------------------------
# (1) Delta r at one loop -- Sirlin decomposition
# ---------------------------------------------------------------------------
sin2W = 1.0 - (MW/MZ)**2     # on-shell sin^2 theta_W
cos2W = 1.0 - sin2W
print("="*72)
print("(1) One-loop Delta r (Sirlin/Bardin-Passarino)")
print("="*72)
print(f"sin^2 theta_W (on-shell) = 1 - M_W^2/M_Z^2 = {sin2W:.6f}")
print(f"cos^2 theta_W            = {cos2W:.6f}")

# Top contribution to Delta rho:  Delta rho = 3 GF m_t^2 / (8 pi^2 sqrt(2))
Delta_rho_top = 3.0 * GF * mt_pole**2 / (8.0 * math.pi**2 * math.sqrt(2.0))

# Higgs logarithm contribution (subleading)
# Delta rho_H ~ - (3 GF M_W^2)/(8 pi^2 sqrt(2)) * (cos2W/sin2W) * (log(MH^2/MW^2) - 5/6)
# Small piece, included for completeness; canonical leading piece is the top.
Delta_rho_H = (3.0 * GF * MW**2 / (8.0 * math.pi**2 * math.sqrt(2.0))) * \
              (cos2W/sin2W - 1.0) * 0.0   # set to zero; subleading & scheme-dep

Delta_rho = Delta_rho_top + Delta_rho_H

# Delta r_rem: residual (non-running, non-rho) one-loop piece.
# Empirically Delta r_rem ~ +0.01 in the on-shell scheme. We use the
# precision-fit value to compute the total:
Delta_r_rem = 0.0100   # standard textbook number (Hollik, Awramik et al.)

Delta_r = Delta_alpha - (cos2W/sin2W)*Delta_rho + Delta_r_rem

print(f"Delta alpha             = {Delta_alpha:.6f}")
print(f"Delta rho (top)         = {Delta_rho_top:.6f}")
print(f"(c^2/s^2) * Delta rho   = {(cos2W/sin2W)*Delta_rho:.6f}")
print(f"Delta r_rem (textbook)  = {Delta_r_rem:.6f}")
print(f"Delta r (one loop)      = {Delta_r:.6f}")
print()
print("(Reference value: precision fits give Delta r ~ 0.036, dominated by")
print(" Delta alpha ~ 0.059 minus the top -(c^2/s^2) Delta rho ~ 0.033.)")
print()

# ---------------------------------------------------------------------------
# (2) Vev in different schemes
# ---------------------------------------------------------------------------
print("="*72)
print("(2) Vev in different renormalization schemes")
print("="*72)

# From  G_F/sqrt(2) = g^2 / (8 M_W^2) * 1/(1 - Delta r)
# define v_pole such that M_W = g_pole v_pole / 2 and g_pole^2 = 4 sqrt(2) GF MW^2
# Then v_pole^2 = v_bare^2 (1 - Delta r).
v_pole_sq = v_bare**2 * (1.0 - Delta_r)
v_pole    = math.sqrt(v_pole_sq)

# MS-bar vev at scale mu = M_Z or m_t (approx). The conversion factor between
# the on-shell and MS-bar vev is mostly from the top Yukawa running and the
# tadpole; typical numerical value v_MSbar(M_t) ~ 246.6-247 GeV. We use the
# Degrassi/Buttazzo result: v(M_t) ~ 247.0 GeV.
v_MSbar_mt = 247.0    # GeV (approximate, from MS-bar matching at m_t)

print(f"v_bare   = (sqrt(2) G_F)^(-1/2)                  = {v_bare:.4f} GeV")
print(f"v_pole   = v_bare * sqrt(1 - Delta r)            = {v_pole:.4f} GeV")
print(f"v_MSbar (mu = m_t, lit)                          ~ {v_MSbar_mt:.4f} GeV")
print(f"v_target (dV: sqrt(2)*M_F)                       = {v_target:.4f} GeV")
print()
print(f"v_pole / sqrt(2)                                  = {v_pole/math.sqrt(2):.4f} GeV")
print(f"v_MSbar(m_t) / sqrt(2)                            ~ {v_MSbar_mt/math.sqrt(2):.4f} GeV")
print()

# ---------------------------------------------------------------------------
# (3) Express the 25 GeV^2 tension as a fraction of radiative scale
# ---------------------------------------------------------------------------
print("="*72)
print("(3) Is the v-tension of natural radiative size?")
print("="*72)
tension_M2 = v_target**2/2 - v_bare**2/2
nat_scale  = Delta_r * v_bare**2 / 2
print(f"v_target^2/2 - v_bare^2/2        = {tension_M2:.3f} GeV^2")
print(f"Delta r * v_bare^2/2 (radiative) = {nat_scale:.3f} GeV^2")
print(f"ratio                            = {tension_M2/nat_scale:.4f}")
print(f"i.e. tension is {100*tension_M2/nat_scale:.2f}% of the natural Delta-r scale")
print()
# A v_pole-style shift:
shift_pole = v_pole**2/2 - v_bare**2/2
print(f"v_pole^2/2 - v_bare^2/2          = {shift_pole:.3f} GeV^2 "
      f"(shift goes the WRONG way -- v_pole < v_bare)")
print()

# ---------------------------------------------------------------------------
# (4) Inverse: what v lands exactly on M_F = 174.175?
# ---------------------------------------------------------------------------
print("="*72)
print("(4) Inverse problem: what v gives M_F = 174.175 GeV exactly?")
print("="*72)
print(f"v_target = {v_target:.4f} GeV")
print(f"v_bare  = {v_bare:.4f} GeV  (delta = {100*(v_target-v_bare)/v_bare:.4f}%)")
print(f"v_pole  = {v_pole:.4f} GeV  (delta = {100*(v_target-v_pole)/v_pole:.4f}%)")
print(f"v_MSbar = {v_MSbar_mt:.4f} GeV  (delta = {100*(v_target-v_MSbar_mt)/v_MSbar_mt:.4f}%)")
print()

# ---------------------------------------------------------------------------
# (5) Physical "sum of fermion masses" measure
# ---------------------------------------------------------------------------
print("="*72)
print("(5) Sum-of-fermion-mass-squared sanity check")
print("="*72)
charged_leptons = [me, mmu, mtau]
up_quarks       = [mu_q, mc, mt_pole]
down_quarks     = [md, ms, mb]
all_charged     = charged_leptons + up_quarks + down_quarks

sum_m2_all = sum(m**2 for m in all_charged)
print(f"sum m_f^2 (all charged f)        = {sum_m2_all:.2f} GeV^2")
print(f"sqrt(sum m_f^2 / 3)              = {math.sqrt(sum_m2_all/3):.4f} GeV  (~ M_F if 3 generations)")
print(f"sqrt(2 * sum m_f^2 / 3)          = {math.sqrt(2*sum_m2_all/3):.4f} GeV")
# Just the top dominates:
print(f"m_t alone                         = {mt_pole:.4f} GeV")
print(f"sqrt(2)*m_t/2 = m_t/sqrt(2)       = {mt_pole/math.sqrt(2):.4f} GeV")
print()
# Treat sum of fermion mass-squared as related to v^2 via Higgs decay rule:
# (in SM) sum y_f^2 = 2 sum m_f^2 / v^2.  Top dominates; trace ~ 1.
trace_yuk = 2.0 * sum_m2_all / v_bare**2
print(f"sum m_f^2 / (v^2/2) = trace(Y Y^t)= {trace_yuk:.4f} (should equal sum y_f^2)")
print()
# What if M_F^2 = (v^2/2)(1 + sum y_f^2 / (16 pi^2)) ?  Top-loop tadpole.
top_shift = trace_yuk / (16*math.pi**2)
v_top_corr_sq = (v_bare**2/2) * (1 + top_shift)
print(f"(v^2/2)(1 + Tr Y^2/(16 pi^2))    = {v_top_corr_sq:.3f} GeV^2 "
      f"-> M_F = {math.sqrt(v_top_corr_sq):.4f} GeV")
print(f"Top tadpole shift v^2/2 by ~     = {top_shift*v_bare**2/2:.2f} GeV^2 "
      f"(target tension = 25 GeV^2)")
print()

# ---------------------------------------------------------------------------
# Summary numbers for the markdown note
# ---------------------------------------------------------------------------
print("="*72)
print("SUMMARY NUMBERS")
print("="*72)
print(f"Tension at M^2 level             = {tension_M2:6.2f} GeV^2  (0.04% of v^2/2)")
print(f"Delta r * v^2/2                   = {nat_scale:6.2f} GeV^2  (natural EW radiative scale)")
print(f"Tension / Delta-r scale           = {100*tension_M2/nat_scale:.2f}%")
print(f"Top tadpole y_t^2/(16pi^2) * v^2/2= {top_shift*v_bare**2/2:6.2f} GeV^2")
print(f"Required v_target                 = {v_target:.4f} GeV")
print(f"v_bare                            = {v_bare:.4f} GeV  (diff {v_target-v_bare:+.3f})")
print(f"v_pole = v_bare sqrt(1-Delta r)   = {v_pole:.4f} GeV  (diff {v_target-v_pole:+.3f})")
print(f"v_MSbar(m_t)                      ~ {v_MSbar_mt:.4f} GeV  (diff {v_target-v_MSbar_mt:+.3f})")
