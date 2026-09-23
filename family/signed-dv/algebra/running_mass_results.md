# Renormalization-scheme dependence and the v/sqrt(2) tension

## Setup

The dV closed-form construction predicts
M_F^(corrected) = 174.175 GeV, and identifies this with v/sqrt(2).
The Fermi-extracted value is v_bare/sqrt(2) = 174.10358 GeV
(v_bare = (sqrt(2) G_F)^(-1/2) = 246.2197 GeV).
The discrepancy is 0.04% in v, equivalently 25 GeV^2 at the v^2/2 level.
The target vev is v_target = sqrt(2) * 174.175 = 246.3206 GeV.

## (a) Can scheme dependence explain the 25 GeV^2?

**Numerically yes; structurally no.** One-loop on-shell (Sirlin 1980):
    Delta r = Delta alpha - (c_W^2/s_W^2) Delta rho + Delta r_rem
            ~ 0.066 - 0.033 + 0.010 ~= 0.036-0.044.
The natural radiative shift of v^2/2 is Delta r * v_bare^2/2 ~ 1100-1330 GeV^2.
The 25 GeV^2 tension is ~**1.9%** of that scale.

But the canonical schemes differ from v_bare in the wrong direction or
by the wrong magnitude:

| Scheme               | v (GeV) | v - v_target (GeV) |
|----------------------|---------|--------------------|
| v_bare (G_F)         | 246.220 | -0.101 (undershoot)|
| v_pole = v_bare sqrt(1-Delta r) | 240.770 | -5.550 (wrong way) |
| v_MSbar(m_t) lit.    | ~247.0  | +0.679 (overshoot) |

The dV deficit sits inside the radiative band but at no canonical landmark.

## (b) Natural vev definition that lands on M_F^(corrected) exactly?

A top-Yukawa tadpole shift M_F^2 = (v^2/2)(1 + Tr(Y Y^dag)/(16 pi^2))
gives 174.65 GeV (overshoots by ~190 GeV^2 vs. required 25).
sqrt(sum m_f^2/3) = 99.7 GeV (off by 1.75x). m_t/sqrt(2) = 122.1 GeV.
**No off-the-shelf SM definition** hits 174.175 GeV to 10^-5; the
closest is v_bare/sqrt(2) at 0.04%.

## (c) Cleanest honest framing

- The dV M_F slot agrees with v_bare/sqrt(2) at 4 x 10^-4 - ~10x worse
  than the m_h match (10^-5), ~5x worse than M_W (~0.4 sigma).
- The 25 GeV^2 residual is ~2% of the Delta r scale and ~13% of the
  leading top tadpole - the size of a *missing* O(alpha) electroweak
  correction not captured by the tree-level (3/8)(M_Z^2 - M_W^2) shift.
- Report as: "M_F = v_bare/sqrt(2) at 10^-4, residue consistent with
  a one-loop EW correction of Sirlin type, not yet derived from the
  dV ansatz." Not as an exact identity.

## Bottom line (100 words)

Scheme dependence neither rescues the match nor kills the
construction. The 25 GeV^2 residual is ~2% of the canonical Delta r
window (~1300 GeV^2) and ~13% of the top-tadpole scale, so it sits
comfortably inside the natural one-loop EW band - but no standard
scheme (G_F, on-shell, MS-bar at M_Z or m_t) hits 174.175 GeV to
the precision the m_h match achieves (10^-5). The honest claim is
"M_F = v_bare/sqrt(2) to 4 x 10^-4, residue of canonical one-loop EW
size" - a *one-loop-precision* match, not an exact identity.
