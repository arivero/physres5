# Electroweak Parameter Reduction: Source-Disciplined Status Report

Date: 2026-06-01.

Status: produced report for the current electroweak-sector reduction programme.
The report records a candidate tree-level reduction, admitted published
baselines, obstructions, and source-completion criteria.  It does not claim a
completed new electroweak theory.

## Abstract

The target is a non-ad-hoc reduction of the Standard Model electroweak
gauge-Higgs input set

```text
{g_2, g_Y, v, lambda_H}
```

to a smaller source-level set.  The current candidate reduces the source-scale
tree-level continuous set to

```text
{g_*, v, lambda_3}
```

under two source assumptions:

```text
g_2=g_*,
g_Y=g_*/sqrt(3),
sin^2(theta_W)=1/4,
m_W/m_Z=sqrt(3)/2,
rho=1.
```

Source status: the weak-angle relation is a cited/known CP2-Weinberg inertia
normalization; the vector mass and `rho=1` relations are derived here and in
the supporting notes from the one-doublet `m_3` mass matrix.  The possible
original contribution is the source-disciplined synthesis, not the numerical
relations themselves.

The principal current result is restrictive.  Full continuous flag CSDR on
`SU(3)/T^2` with parent `SU(3)_W` cannot directly source the active
electroweak `U(2)_W` carrier:

```text
C_{SU(3)_W}(T^2)=T^2.
```

The admitted carrier comes instead from the one-circle endpoint:

```text
C_{SU(3)_W}(U(1)_8)=U(2)_W.
```

Source status: derived in
[../notes/Electroweak_CSDR_Centralizer_Embedding_Obstruction.md](../notes/Electroweak_CSDR_Centralizer_Embedding_Obstruction.md).
The one-circle endpoint CSDR route then derives the group and charged branch,
but raw `R=U(1)_8` equivariance also leaves zero-charge `m_0` intertwiners.
Thus the endpoint route still needs a source projection or positive mass for
`Phi_0`, plus the endpoint potential variations and trace normalization.

## Scope And Criterion

The scope is the electroweak gauge-Higgs sector:

```text
SU(2)_L x U(1)_Y,
g_2,g_Y,
H in C^2,
V(H)=m_H^2 H^dagger H + lambda_H(H^dagger H)^2,
rho and electromagnetic survivor conditions.
```

QCD, full Yukawa matrices, CKM, PMNS, and colour-sector family structure remain
outside the reduction claim unless a finite module or source action later feeds
them into the electroweak kinetic trace or Higgs potential.

A parameter counts as reduced only when a named geometry, CSDR action,
spectral action, boundary problem, finite trace, current algebra, or published
mechanism fixes it before comparison with data.  Residual numerical agreement
without such a source receives no score.

## Candidate Carrier

Use the CP2/Aloff-Wallach geometric carrier:

```text
SO(3) -> X_{1,1}=SU(3)/U(1)_{1,1} -> CP^2,
Y_6=SU(3)/T^2,
m=m_0 direct_sum m_3,
m_3 ~= C^2 ~= R^4.
```

Source status: cited geometric carrier and local representation setup; the
`S^5 x S^2` endpoint remains the Standard-Model-shaped diagnostic priority for
endpoint checks.

Use the one-circle electroweak gauge carrier:

```text
G_W=SU(3)_W,
U(1)_8={diag(z,z,z^(-2))},
C_{SU(3)_W}(U(1)_8)=U(2)_W.
```

Source status: derived from the one-circle centralizer calculation.

The adjoint split is

```text
su(3)_W=(3_0 direct_sum 1_0) direct_sum (2_(+3) direct_sum 2_(-3)).
```

The matched tangent block is

```text
(m_3)_C = 2_(+3) direct_sum 2_(-3),
Y_SM=q_8/6,
H in 2_(+3),        Y_SM(H)=1/2.
```

Source status: derived representation carrier.  A one-light-doublet spectrum
is conditional on the source keeping one real `m_3` block and projecting or
stabilizing extra scalar branches.

## Expansion Anchor: Gauge And Mass Readout

Variables and normalization:

```text
H                 retained complex doublet,
K_H               scalar kinetic metric on m_3,
g_2,g_Y           canonically normalized electroweak couplings,
Y_SM              q_8/6,
<H>               (0,v/sqrt(2)).
```

Covariant derivative:

```text
D_mu H =
  partial_mu H
  - i g_2 W_mu^a sigma_a H/2
  - i g_Y B_mu Y_SM(H) H.
```

Vector masses:

```text
m_W^2 = g_2^2 v^2/4,
m_Z^2 = (g_2^2+g_Y^2)v^2/4,
cos^2(theta_W)=g_2^2/(g_2^2+g_Y^2),
rho=m_W^2/(m_Z^2 cos^2(theta_W))=1.
```

Source status: derived here from the standard one-doublet mass matrix, with
the additional source condition that `K_H` is scalar on the real irreducible
`m_3` block.

The source-scale gauge relation is

```text
g_2=g_*,
g_Y=g_*/sqrt(3),
sin^2(theta_W)=1/4,
m_W/m_Z=sqrt(3)/2.
```

Source status: the coupling relation is cited/known CP2-Weinberg inertia, not
the canonical adjoint `SU(3)_W` trace.  Direct adjoint `SU(3)_W` gives a
different normalization unless a source trace derives the required excess.

Residuals:

```text
Delta f_2, Delta f_Y       thresholds and running corrections,
Delta K_m3                 anisotropy from defects or endpoints,
Delta V_0                  triplet tadpoles and m_0-m_3 mixing,
Delta rho                  precision correction if K_H is not scalar.
```

Use status: active residuals, not fitted inputs.

## CSDR Findings

The downloaded CSDR source gives the centralizer and scalar-intertwiner rule:

```text
H=C_G(R_G),
F_ib=f_ib^c phi_c - [phi_i,phi_b]=0,
F_ij=f_ij^k phi_k - [phi_i,phi_j]=0.
```

Source status: cited from the CSDR consistency source digested in
[../docs/Chatzistavrakidis_Manousselis_Prezas_Zoupanos_CSDR_Consistency_arXiv_0708_3222.md](../docs/Chatzistavrakidis_Manousselis_Prezas_Zoupanos_CSDR_Consistency_arXiv_0708_3222.md).

Full flag obstruction:

```text
S/R=SU(3)/T^2,
G=SU(3)_W,
R_G=T^2 maximal in SU(3)_W,
H=C_{SU(3)_W}(T^2)=T^2.
```

Source status: derived from the cited CSDR rule and `su(3)` root-space algebra.
It rejects the shortcut from full `SU(3)/T^2` CSDR to `U(2)_W`.

One-circle endpoint admission:

```text
S/R=SU(3)/U(1)_8,
H=C_{SU(3)_W}(U(1)_8)=U(2)_W,
m_C=m_0,C direct_sum m_3,+ direct_sum m_3,-,
Phi_3,+ in Hom_R(m_3,+,g_+),
Phi_3,- in Hom_R(m_3,-,g_-),
Phi_0 in Hom_R(m_0,C,u(2)_C).
```

Source status: derived in
[../notes/Electroweak_OneCircle_CSDR_Endpoint_Admission_Test.md](../notes/Electroweak_OneCircle_CSDR_Endpoint_Admission_Test.md).
The endpoint route admits the weak group and charged doublet representation,
but leaves scalar-spectrum obligations.

Endpoint action target:

```text
S_YM =
  - (1/(4g_D^2)) int_{M_4 x SU(3)/U(1)_8}
      sqrt(-G) Tr(F_MN F^MN),

V_YM(Phi) =
  (1/(4g_D^2)) int_K sqrt(g_K) g^(ac)g^(bd)
    Tr(F_ab(Phi)F_cd(Phi)).
```

Required source readouts:

```text
K_H,
m_3^2,
lambda_3,
m_0,eff^2,
linear triplet portal and Delta rho residual,
f_2,f_Y in the same normalization.
```

Use status: target for future derivation.  These quantities must not be
inserted as fitted constants in a reduced-model claim.

## Published Baselines And Ledger Status

| Branch | Source status | Tree readout | Current use |
| --- | --- | --- | --- |
| Manton `S^2` CSDR, `G_2` subcase | Published source baseline. | `sin^2(theta_W)=1/4`, `lambda/g^2=1/6`, `m_H=m_Z`. | Clean control and obstruction; modern Higgs mass rejects the uncorrected branch. |
| Six-dimensional `SU(3)` gauge-Higgs | Published gauge-Higgs source. | `tan(theta_W)=sqrt(3)`, `lambda=g^2/2`, `m_H=2m_W`. | Quartic-source baseline; weak angle and Higgs mass fail. |
| MSSM D-term | Published supersymmetric source. | `lambda_SM=(g^2+g'^2)cos^2(2 beta)/8 + Delta_lambda_thr`. | Authentic quartic source, but generic MSSM adds soft-sector inputs unless a source derives them. |
| Connes/Pati-Salam spectral action | Published finite-geometry source. | Unified subcase gives `g_Y/g_2=sqrt(3/5)`, `sin^2=3/8`. | High-quality obstruction; CP2 repair needs a source-derived non-unified trace/matching condition. |
| Heterotic current levels | Published string-current mechanism. | `g_Y/g_2=sqrt(k_2/k_Y)`; CP2 target needs `k_Y/k_2=3`. | Authentic target; downloaded published set has no admitted `k_Y=3` derivation with SM charges and thresholds. |
| Fuzzy-CSDR | Published finite-matrix source framework. | Centralizer gauge group and `F_ab F^ab` potential. | Admitted framework; no current source computes `f_Y/f_2=3` or `lambda_3`. |
| 331 near-IR boundary | Published electroweak extension. | `sin^2(theta_W)=t_X^2/(1+4t_X^2)`, CP2 value only as `t_X -> infinity`. | Authentic boundary motivation; finite model adds coupling and heavy-sector data. |
| Diagonal `SU(3)` TeV module | Published diagonal matching mechanism. | Large auxiliary-coupling limit gives `sin^2(theta_W)=1/4`. | Benchmark; finite auxiliary couplings and scalar bridge sectors add inputs. |
| Quantized Manton | One-loop or fuzzy quantization of Manton's CSDR source. | Determinant target `Gamma_1(H)=(1/2)Str log L_KK(H)` for thresholds. | Admitted threshold target; no De Vries source found without a retained two-variable relative operator. |

The score ledger is
[../notes/Electroweak_Model_Score_Ledger.md](../notes/Electroweak_Model_Score_Ledger.md).
All published baselines remain in the ledger as controls or source targets, not
as hidden support for fitted constants.

## Experimental Diagnostics

At pole level the tree relation

```text
m_W/m_Z=sqrt(3)/2
```

is far from the current PDG-style pole ratio recorded in the local running
digest.  The local score ledger records a difference of about `-102 sigma`
using the ratio error.

Source status: experimental diagnostic from
[../notes/Electroweak_Model_Score_Ledger.md](../notes/Electroweak_Model_Score_Ledger.md)
and [../docs/SMDR_Local_Running_Data_PDG2025.md](../docs/SMDR_Local_Running_Data_PDG2025.md).
It does not invalidate a source-scale relation by itself; it requires a running
and threshold map before comparison.

The local SMDR diagnostics also record:

```text
g'/g=1/sqrt(3) crossing: near a few TeV,
MSSM large-tan beta D-term quartic crossing: near 16.7 TeV,
Manton G_2 lambda/g^2=1/6 crossing: near 18 TeV.
```

Use status: diagnostics only.  The Wilking stationary-ratio quotient `5` is a
motivated scale-map target, but no common action currently derives the map from
CP2/Aloff-Wallach data to a D-term or Manton source.

## Quantized Manton Check

The small quantized-Manton run is recorded in
[../notes/Electroweak_Quantized_Manton_DeVries_Small_Run.md](../notes/Electroweak_Quantized_Manton_DeVries_Small_Run.md).

Ordinary quantization starts from a gauge-fixed fluctuation operator around the
Manton background:

```text
L_KK(H) xi =
  Delta_A xi + ad(H)^2 xi + curvature/isotropy terms + gauge-fixing terms,

Gamma_1(H) =
  (1/2) Str log(L_KK(H)/mu_ren^2) + counterterms.
```

Source status: target for future derivation.  With the full spectrum,
ghost subtraction, counterterms, and matching scale fixed, this determinant
could compute

```text
Delta lambda,
Delta f_2,
Delta f_Y,
Delta m_H^2.
```

The De Vries admission test requires more structure:

```text
q,p,
P,
L_patched(q,p),
L_unpatched(q),
Gamma_rel=log Det L_patched(q,p)-log Det L_unpatched(q),
delta^2 Gamma_rel with mixed q-p and p-p image-stiffness terms.
```

Use status: ordinary one-loop or fuzzy Manton supplies no retained response
variable `p`, no response map `P`, and no patched/unpatched relative operator
pair in the current workspace.  Therefore De Vries receives no support from
Manton in the active electroweak reduction.  Quantized Manton remains an
admissible threshold programme for repairing `m_H=m_Z` and testing the
Manton/Wilking residual near `Q_E=5Q_CP2`.

## Constructive Route

The least ad-hoc route now has the following sequence:

```text
1. Use the one-circle endpoint SU(3)/U(1)_8 to derive U(2)_W.
2. Use the charged root-space intertwiners to obtain the m_3 doublet carrier.
3. Compute the endpoint CSDR/YM potential from F_ab F^ab.
4. Prove one light real m_3 block and control Phi_0.
5. Derive f_2,f_Y,K_H in the same source normalization.
6. Derive lambda_3/g_*^2 and m_3^2 before comparison.
7. Add only source-derived running and threshold residuals.
```

The route is motivated by symmetry and source action data:

```text
centralizer condition,
root-space charge matching,
homogeneous carrier,
CSDR/YM curvature-square action,
Schur metric on the real m_3 block.
```

## Objections And Constraints

1. Full flag CSDR does not produce the active carrier with parent `SU(3)_W`.
   It gives `T^2`, not `U(2)_W`.

2. The one-circle endpoint does not isolate the low-energy scalar spectrum.
   Raw `R=U(1)_8` equivariance leaves `Phi_0` in the zero-charge sector.

3. The CP2 weak-angle relation is not the canonical adjoint `SU(3)_W` trace.
   Pure adjoint `SU(3)_W` has the wrong trace factor for the CP2 target.

4. The Higgs quartic remains unreduced.  Published CSDR/YM and gauge-Higgs
   quartics are authentic baselines, but their coefficients currently miss the
   CP2 running diagnostics or bring extra source data.

5. MSSM D-terms provide an authentic quartic source, but generic MSSM increases
   the electroweak parameter inventory unless the soft matrix, beta, spectrum,
   thresholds, and scale map are source-derived.

## Repair Criteria

An electroweak branch may be promoted only after it supplies:

```text
displayed source action or finite trace,
embedded isotropy and centralizer readout,
full scalar-intertwiner decomposition,
canonical gauge and scalar kinetic normalizations,
second variation for m_3^2 and triplet stability,
fourth variation for lambda_3,
source-derived absence, mass, parity, or residual calculation for Phi_0,
running and threshold map fixed before data comparison.
```

Delete or quarantine any branch that:

```text
uses full SU(3)/T^2 CSDR with parent SU(3)_W as a direct U(2)_W source,
sets the hypercharge trace to the CP2 target after comparison,
inserts a rational quartic coefficient without a source action,
projects out Phi_0 without a source equation,
counts MSSM D-terms as a full reduction while leaving soft data free,
uses near-residual numerical agreement as a source.
```

## Current Conclusion

The current programme has a credible non-ad-hoc carrier but not a completed
new electroweak model.

Admitted:

```text
one-circle endpoint centralizer U(2)_W,
charged m_3 doublet representation,
tree-level rho=1 from a scalar metric on one real m_3 block,
published source baselines for CSDR, gauge-Higgs, MSSM D-terms, Connes,
heterotic current levels, fuzzy CSDR, and near-IR diagonal/331 mechanisms.
```

Conditional:

```text
source-scale CP2 weak-angle synthesis with the adjoint SU(3)_W carrier,
one-light-doublet spectrum,
Higgs quartic reduction,
Higgs scale reduction,
threshold and running residuals.
```

The next decisive calculation is the endpoint CSDR/YM potential and trace
package for `SU(3)/U(1)_8` with parent `SU(3)_W`.  It must compute

```text
f_2, f_Y, K_H, m_3^2, lambda_3, m_0,eff^2, Delta rho
```

in one normalization.  Until that calculation succeeds, the best honest
status is a source-disciplined candidate reducing the tree-level gauge-coupling
count and custodial stiffness, with the Higgs potential still open.
