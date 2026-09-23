# Electroweak Quantized Manton De Vries Small Run

Date: 2026-06-01.

Status: source-admission run for the question whether quantizing Manton's
`S^2` CSDR model naturally supplies a De Vries source operator.  The answer
recorded here is negative for the ordinary one-loop or fuzzy-Manton reading,
with a precise repair path.

## Question

Manton's `G_2` branch already supplies a motivated electroweak baseline:

```text
g'/g = 1/sqrt(3),
sin^2(theta_W)=1/4,
lambda/g^2=1/6,
m_H=m_Z.
```

Source status: cited from the Manton `S^2` CSDR source and recorded in
[Electroweak_Manton_G2_Common_Source_Baseline.md](Electroweak_Manton_G2_Common_Source_Baseline.md).

The small run asks whether a quantized version of that same source can also
play the De Vries role: a named operator whose second variation produces the
retained signed response block, rather than a bare spin-Casimir shortcut.

## Expansion Block: Manton Tree Source

Variables and domain:

```text
M_6            = M_4 x S^2_R,
G              = G_2 in the focused branch,
R_iso          = SO(3) acting on S^2,
H_EW           = SU(2)_L x U(1)_Y after the CSDR centralizer,
g_6            six-dimensional Yang-Mills coupling,
j,j'           four-dimensional weak and hypercharge couplings in Manton's notation,
H              retained electroweak Higgs doublet,
theta_M        Manton weak angle,
K              invariant bilinear form on Lie(G_2).
```

Action:

```text
S_6 =
  - (1/(4 g_6^2)) int_{M_4 x S^2_R} sqrt(G_6) K(F_MN,F^MN).
```

Reduction and readout:

```text
spherical-symmetry constraints:
  L_X A = D W_X for X in Lie(SO(3)),

canonical four-dimensional branch:
  j'/j = 1/sqrt(3),
  theta_M = 30 degrees,
  lambda_M/j^2 = 1/(8 cos^2 theta_M) = 1/6,
  m_H=m_Z.
```

Normalization:

```text
lambda_M is in the Standard-Model convention
V(H)=m_H^2 H^dagger H + lambda_M (H^dagger H)^2.
```

Residuals:

```text
modern pole Higgs residual in the G_2 branch:
  m_H,model - m_H,PDG ~= 92.802359 GeV - 125.20 GeV.

source-scale quartic residual at the CP2 weak-angle crossing:
  c_obs(Q_CP2)-1/6 ~= 0.036021441,
  c_obs=lambda(Q)/g(Q)^2.
```

Use status: source-derived tree baseline and obstruction.  The tree relation
cannot be used as a modern Higgs prediction without a sourced quantum,
threshold, or dual-scale repair.

## Expansion Block: Ordinary Quantized Manton

Variables and operators:

```text
A_bar,H_bar          Manton background with a constant Higgs branch value,
xi                   bosonic and ghost fluctuations around the CSDR background,
L_KK(H_bar)          gauge-fixed fluctuation operator on M_4 x S^2_R,
mu_ren               renormalization scale,
Gamma_1(H_bar)       one-loop effective action after integrating nonzero KK modes.
```

Operator family:

```text
L_KK(H_bar) xi =
  Delta_A xi + ad(H_bar)^2 xi + curvature/isotropy terms + gauge-fixing terms.
```

Formal one-loop readout:

```text
Gamma_1(H_bar) =
  (1/2) Str log(L_KK(H_bar)/mu_ren^2) + counterterms.
```

For a local effective potential this gives the schematic threshold package

```text
V_eff(H) =
  V_Manton(H)
  + (1/(64 pi^2)) Str M_i(H)^4 log(M_i(H)^2/mu_ren^2)
  + counterterms,

Delta c_KK =
  Delta(lambda/g^2),
Delta f_2, Delta f_Y =
  gauge kinetic threshold corrections.
```

Spectral readout needed for admission:

```text
full KK spectrum on S^2_R,
G_2 representation multiplicities,
ghost subtraction,
gauge-fixing convention,
counterterm prescription,
matching scale map,
finite threshold residuals.
```

Use status: admissible electroweak threshold target.  The determinant has a
named operator family, but the spectrum and counterterms have not been
computed in this workspace.

## Numerical Diagnostic

Local SMDR data and the Manton/Wilking dual-scale note give:

```text
at Q_CP2 ~= 3628.270640400 GeV:
  gp/g ~= 1/sqrt(3),
  c_obs = lambda/g^2 ~= 0.202688108,
  c_obs - 1/6 ~= 0.036021441.

at Q_E = 5 Q_CP2 ~= 18141.353202 GeV:
  g ~= 0.624373124717,
  gp ~= 0.368446956693,
  gp/g ~= 0.590107008305,
  lambda ~= 0.065040925343,
  c_obs ~= 0.166839280785,
  c_obs - 1/6 ~= 0.000172614118.
```

The scale relation behind the second comparison is:

```text
rho_W = 5,
Q_c16/Q_CP2 ~= 4.965621132398,
rho_W/(Q_c16/Q_CP2)-1 ~= 0.006923377093.
```

Source status: diagnostics from the local running data and
[Electroweak_MantonG2_Wilking_DualScale_Test.md](Electroweak_MantonG2_Wilking_DualScale_Test.md).
The near agreement receives no model score until a source derives the
CP2-to-Manton scale map and the quantum threshold package.

## Expansion Block: De Vries Admission Test

The current De Vries discipline requires a retained two-variable source:

```text
q               source-side branch variable,
p               retained response variable,
P               named response map,
L_unpatched(q)  unpatched operator family,
L_patched(q,p)  patched operator family with retained response,
Gamma_rel       log Det L_patched(q,p) - log Det L_unpatched(q).
```

The required second variation has the form

```text
delta^2 Gamma_rel|(0,0)
  -> signed retained block with mixed q-p term and p-p image term,

schematic target:
  [ 0          P^dagger ]
  [ P       - P P^dagger ],
```

up to the source-fixed response metric and sign convention.  The representation
readout must then enter through a named operator:

```text
K_r^can = gamma^2 mu_r + sigma_r^can,
```

where `mu_r` is evaluated only after the operator, domain, representation, and
trace convention have been derived.  A bare `SU(2)` Casimir is rejected as a
premise.

Comparison with ordinary quantized Manton:

```text
ordinary Manton determinant:
  variables: H_bar and KK fluctuations xi,
  readout: Delta m_H^2, Delta lambda, Delta f_i,
  missing: retained response variable p,
  missing: response map P with p-p term P P^dagger,
  missing: relative patched/unpatched branch operator pair.

De Vries source:
  variables: q,p retained simultaneously,
  readout: mixed source-response Hessian and retained image stiffness,
  required: source-fixed response norm and residual terms.
```

Use status: ordinary quantized Manton does not currently admit a De Vries
source.  The determinant can repair the electroweak Higgs quartic, but it does
not produce the required retained signed response Hessian.

## Fuzzy Manton Check

A fuzzy version replaces the internal sphere by a finite matrix algebra:

```text
S^2_R -> S^2_N,
functions -> Mat_N,
internal Laplacian -> [J_a,[J_a,.]],
finite spectrum -> l(l+1) blocks with representation multiplicities.
```

Source status: compatible with published fuzzy-CSDR mechanisms catalogued in
[Electroweak_Fuzzy_CSDR_Source_Audit.md](Electroweak_Fuzzy_CSDR_Source_Audit.md).

The finite matrix trace can in principle compute thresholds:

```text
Gamma_N(H) = (1/2) Str log L_N(H),
Delta c_N  = Delta(lambda/g^2),
Delta f_i,N = finite gauge-kinetic thresholds.
```

De Vries status:

```text
finite SU(2) Casimirs l(l+1) appear naturally,
but l(l+1) alone is not a De Vries source;
promotion requires a finite relative operator pair
  L_N,patched(q,p), L_N,unpatched(q)
whose second variation retains the q,p response block.
```

Use status: fuzzy Manton remains an admissible threshold and finite-source
search.  It does not reveal De Vries in the small run.

## Constructive Route

The non-ad-hoc way to keep quantized Manton alive is:

```text
1. Quantize the Manton G_2 CSDR background with a fixed gauge and ghost system.
2. Compute the S^2 KK or fuzzy-S^2_N spectrum as a source calculation.
3. Extract Delta lambda, Delta f_2, Delta f_Y, and mass residuals.
4. Test whether the Wilking quotient 5 derives a physical scale map.
5. Compare the resulting thresholds to m_H=m_Z and c_obs-1/6 residuals.
```

The De Vries repair path is stricter:

```text
1. Identify a source-side branch variable q and an independent retained response p.
2. Define patched and unpatched Manton operator families.
3. Compute Gamma_rel as a determinant ratio.
4. Derive the mixed q-p and p-p Hessian block.
5. Only then evaluate any representation multiplier mu_r.
```

## Objections

1. The ordinary one-loop Manton determinant is a one-field Higgs-background
   effective action, so it naturally produces thresholds rather than a retained
   response Hessian.

2. The presence of `SU(2)` harmonics on `S^2` does not meet the De Vries source
   rule.  Harmonic Casimirs need an operator, trace, response metric, and
   residual calculation before use.

3. The Manton `m_H=m_Z` tree relation remains a hard obstruction.  A quantum
   repair must compute the correction; it cannot drop the relation while
   retaining only `lambda/g^2=1/6`.

4. The Wilking fivefold scale relation is motivated, but the current workspace
   has no source action or duality deriving the physical map from
   CP2/Aloff-Wallach data to Manton's `M_4 x S^2` compactification.

## Repair Criteria

Quantized Manton may enter the active electroweak reduction only after it
supplies:

```text
named fluctuation operator L_KK or finite L_N,
complete spectrum and multiplicities,
ghost and gauge-fixing convention,
renormalization prescription,
Delta lambda and Delta f_i in the same normalization as the gauge angle,
scale map and residuals fixed before comparison.
```

Quantized Manton may enter the De Vries ledger only after it supplies:

```text
retained variables q,p,
patched/unpatched operator pair,
Gamma_rel determinant ratio,
second variation with mixed q-p and p-p image-stiffness terms,
canonical response metric,
neutral multiplier mu_r computed from that operator package.
```

## Verdict

Small-run verdict:

```text
ordinary quantized Manton:
  admissible as electroweak threshold programme,
  no admitted De Vries source found.

fuzzy Manton:
  admissible as finite-threshold programme,
  no admitted De Vries source found.

relative patched Manton determinant:
  possible repair path,
  no current source construction in the workspace.
```

Current ledger action: retain quantized Manton as a threshold/source target and
do not use De Vries from Manton in the active electroweak reduction.
