# Electroweak Manton G2 Common-Source Baseline

Date: 2026-06-01.

Status: published common-source baseline and modern obstruction; no active-model promotion.

## Purpose

Manton's `S^2` CSDR reduction has one subcase that deserves separate treatment for the active
electroweak goal.  The `G_2` rank-two branch derives, from one six-dimensional Yang-Mills source,

```text
sin^2 theta_W = 1/4,
lambda/g^2 = 1/6,
m_H = m_Z.
```

It supplies the cleanest published common-source control currently in the ledger: the weak angle
and quartic come from one action and a group choice rather than from separate numerical inputs.

Use status: keep the `G_2` branch as a benchmark for what a non-ad-hoc electroweak reduction
should look like structurally.  It is not the current model because the same source predicts the
wrong modern Higgs and pole mass ratios unless a further source-derived threshold or running map
is supplied.

## Source Anchor

Main branch note:
[Electroweak_Manton_S2_CSDR_Branch_Test.md](Electroweak_Manton_S2_CSDR_Branch_Test.md).

Source transcription:
[docs/Manton_Fermions_and_Parity_Violation_in_Dimensional_Reduction_1979.md](../docs/Manton_Fermions_and_Parity_Violation_in_Dimensional_Reduction_1979.md).

Running-data source:
[docs/SMDR_Local_Running_Data_PDG2025.md](../docs/SMDR_Local_Running_Data_PDG2025.md).

Source status:

```text
cited from Manton source package:
  six-dimensional Yang-Mills on M_4 x S^2,
  SO(3)-symmetric reduction,
  rank-two group angle choices,
  m_H=m_Z relation.

derived here:
  lambda/g^2=1/(8 cos^2 theta_W),
  G_2 subcase lambda/g^2=1/6,
  pole and local-SMDR residual diagnostics.
```

## Expansion Block

Variables and domains:

```text
M_6       = M_4 x S^2_R,
G         = G_2,
g_6       six-dimensional Yang-Mills coupling,
R         sphere radius,
j         four-dimensional SU(2)_L coupling after reduction,
j_prime   four-dimensional U(1) coupling after reduction,
theta_W   group root angle selected by the CSDR embedding,
H         Higgs doublet from internal connection components,
v         Higgs vacuum scale,
lambda_M  quartic coefficient in V(H).
```

Source action:

```text
S_6 =
  - (1/(4 g_6^2)) int_{M_4 x S^2_R} sqrt(G_6) K(F_MN,F^MN).
```

CSDR rule:

```text
SO(3)-symmetric gauge field on S^2
  -> four-dimensional SU(2)_L x U(1)_Y gauge fields
  -> one Higgs doublet from internal components
  -> scalar potential from F_ab F^ab.
```

Manton rank-two readout:

```text
theta_W(G_2) = 30 degrees,
j_prime/j = tan(theta_W) = 1/sqrt(3),
sin^2 theta_W = 1/4.
```

Mass and quartic readout:

```text
m_W = j v/2,
m_Z = m_W/cos(theta_W),
m_H = m_Z,
m_H^2 = 2 lambda_M v^2.
```

Therefore

```text
lambda_M/j^2
  = m_H^2/(2v^2 j^2)
  = (m_W^2/cos^2 theta_W)/(2v^2 j^2)
  = 1/(8 cos^2 theta_W).
```

For `theta_W=30 degrees`,

```text
cos^2 theta_W = 3/4,
lambda_M/j^2 = 1/6,
m_H/m_W = 1/cos(theta_W) = 2/sqrt(3).
```

Variational status:

```text
first variation:
  dV/d(H^dagger H)=0 fixes v from the source mass and quartic,

second variation:
  d^2V/dh^2 at the vacuum gives m_H^2=2 lambda_M v^2,

normalization:
  j,j_prime,H are canonically normalized after integrating S^2.
```

Residual terms needed for promotion:

```text
Delta_run       running from the CSDR scale to the comparison scale,
Delta_thr       threshold correction to lambda and gauge couplings,
Delta_radius    source relation fixing R without fitting a compactification tower,
Delta_fermion   fermion embedding, anomaly, and parity-violation residuals,
Delta_gravity   consistency of an electroweak-scale S^2 radius with the parent setting.
```

Use status: the equations above form a source-derived tree model.  Residual terms are absent in
the current package.

## Modern Residuals

Pole diagnostics from the score ledger:

```text
m_W = 80.3692 GeV,
m_Z = 91.1880 GeV,
m_H = 125.20 GeV.
```

The `G_2` branch predicts, when normalized by the modern `W` mass,

```text
m_W/m_Z = sqrt(3)/2 ~= 0.866025404,
m_H = m_Z = 2 m_W/sqrt(3) ~= 92.802359 GeV,
Delta m_H ~= -32.397641 GeV.
```

The pole ratio residual is

```text
Delta(m_W/m_Z) ~= -0.015335,
```

about `-102 sigma` using the current ratio uncertainty recorded in the score ledger.

Local SMDR diagnostics:

```text
at Q_CP2 ~= 3628.270640400 GeV:
  gp/g ~= 1/sqrt(3),
  c_obs = lambda/g^2 ~= 0.202688108,
  c_G2 = 1/6 ~= 0.166666667,
  c_obs-c_G2 ~= 0.036021441.
```

Interpolating the local SMDR table for `c_obs=1/6` gives the diagnostic point

```text
Q_c16 ~= 18016.617366029 GeV,
gp/g ~= 0.590051876,
gp/g - 1/sqrt(3) ~= 0.012701607,
sin^2 theta_W ~= 0.258248948.
```

Use status: the two source relations do not meet at one local SMDR scale.  The `c=1/6` crossing
is close to the D-term/Wilking quartic diagnostics, but closeness is not a source.

## Proargument Pass

The `G_2` subcase has the right kind of explanation:

```text
choose source action  -> six-dimensional Yang-Mills,
choose group          -> G_2 rank-two embedding,
reduce by CSDR        -> SU(2)_L x U(1)_Y plus Higgs doublet,
read weak angle       -> theta_W=30 degrees,
read quartic          -> lambda/j^2=1/6,
read custodial masses -> m_H=m_Z and rho=1 in the bosonic tree sector.
```

It reduces the bosonic electroweak tree sector to a coupling and the sphere radius, and all three
dimensionless relations are source outputs.

## Counterargument Pass

The same rigidity prevents immediate use as the active model:

```text
m_H=m_Z is far below the observed Higgs mass,
the pole weak-angle prediction misses the measured m_W/m_Z ratio,
the local SMDR scale satisfying gp/g=1/sqrt(3) has c_obs larger than 1/6,
the local SMDR scale satisfying c_obs=1/6 has gp/g larger than 1/sqrt(3),
fermions and anomaly data are not completed,
the electroweak-scale sphere radius requires a parent interpretation.
```

Any repair that changes `m_H=m_Z`, shifts `theta_W`, or changes `lambda/j^2` must come from a
source-derived threshold, boundary term, or running map.

## Kill Or Repair Criteria

Delete the `G_2` branch from an active model claim, while retaining it as a baseline, if:

```text
m_H=m_Z is ignored,
the `1/6` quartic is combined with CP2 running data at a different scale without a source map,
the Higgs quartic threshold is fitted,
the group angle is treated as continuously adjustable,
the compactification radius is chosen from the electroweak scale with no parent explanation.
```

Repair requires:

```text
a source-derived threshold or running map correcting m_H=m_Z,
a source-derived dual-scale map between Q_CP2 and Q_c16,
fermion embedding and anomaly checks,
a parent interpretation of the S^2 radius,
and preservation of the common-action origin of theta_W and lambda.
```
