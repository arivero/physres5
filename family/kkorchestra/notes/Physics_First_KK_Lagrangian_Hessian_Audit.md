# Physics-First KK Lagrangian Hessian Audit

Date: 2026-06-01.

Status: source-action audit for the no-priori De Vries goal.

## Question

Start from the reduced KK Lagrangian, choose a vacuum, and compute the quadratic physics.  Does
the ordinary KK/geometric-Higgs source action produce the retained signed Hessian needed for a
De Vries comparison?

## Reduced Lagrangian

The relevant four-dimensional zero-mode action has the form

```text
L_4 =
  -1/4 Z_ab(q) F^a F^b
  -1/2 G_IJ(q) D_mu q^I D^mu q^J
  - V(q)
  + ...
```

with

```text
D_mu q^I = partial_mu q^I - A^a_mu (T_a q)^I.
```

At a vacuum `q_0`, write

```text
q=q_0+eta.
```

The covariant kinetic term expands to

```text
D_mu q^I =
  partial_mu eta^I
  - A^a_mu (T_a q_0)^I
  - A^a_mu (T_a eta)^I
  + ...
```

The vector mass matrix is therefore

```text
(M_A^2)_ab = G_IJ(q_0) (T_a q_0)^I (T_b q_0)^J.
```

The scalar Hessian is

```text
(M_eta^2)_IJ = partial_I partial_J V(q_0)
```

plus gauge-fixing and Goldstone mixing terms in the usual Higgs description.

## Computed Structure

The ordinary source action gives:

```text
vector mass matrix:    positive semidefinite norm on T_a q_0,
scalar Hessian:        second derivative of V at q_0,
Goldstone mixing:      A_mu partial^mu eta before gauge fixing,
gauge kinetic matrix:  internal inertia Z_ab(q_0).
```

After unitary gauge or an equivalent gauge fixing, the physical quadratic Lagrangian contains
ordinary masses and scalar Hessian eigenvalues.  It does not contain a retained two-field
indefinite block

```text
[ 0       P^dagger ]
[ P      -P P^dagger ].
```

Writing such a block after the ordinary KK vacuum expansion inserts a new interface variable and
a new response stiffness not present in the computed source action.

## Source-Term Classification

| Source term | Vacuum Hessian output | De Vries status | Retained physics |
|---|---|---|---|
| Einstein-Hilbert compact curvature | Radion and inner-metric shape potential `V_grav(phi,u)`; graviphoton masses only from retained non-invariant metric data. | No signed retained block. | Shape-stability constraints; exact Killing fields give massless vectors. |
| Geometric modulus kinetic term | `G_IJ(q_0)(T_a q_0)^I(T_b q_0)^J`. | No De Vries block. | Ordinary Higgs/Stueckelberg vector masses. |
| Yang-Mills gauge-Higgs sector | CSDR/YM scalar potential from internal `F_ab F^ab`; vector masses from a chosen scalar vacuum. | No De Vries block from the ordinary Hessian. | Possible `m_3` doublet branch and `rho=1`. |
| Stueckelberg or phase locking | Rank-one abelian mass matrix. | Deleted as De Vries source. | Diagonal survivor and one massive abelian vector. |
| Direct DtN/boundary energy | Positive boundary stiffness `<q,P q>`. | Deleted as signed-Hessian source. | Boundary stabilization and mass shifts. |
| Green boundary form | Mixed pairing. | Deleted as standalone route. | Mixed boundary input for another source action. |
| Interface action with retained response `p` | Unknown until a physical source term computes `p`, its kinetic norm, and `M`. | Open only as a new source-action calculation. | Could be tested after writing the actual Lagrangian term. |

## Deletion

The ordinary KK/geometric-Higgs vacuum Hessian route leaves active De Vries derivations.

Reason:

```text
ordinary KK source action
  -> positive vector mass matrix + scalar Hessian,
  -> no retained response variable p,
  -> no computed p-p entry M=P P^dagger,
  -> no signed two-field De Vries block.
```

An active De Vries route therefore needs a physical interface, boundary, defect, or finite trace
term with a retained response variable.  That term becomes the source action under test.  It
cannot be appended as a preferred Hessian shape.

## Constraints Kept

The audit preserves non-De Vries constraints produced by the physics:

```text
single m_3 doublet vacuum
  -> kappa_c = kappa_n
  -> rho=1.
```

The vertical triplet condition also remains:

```text
<Phi_0>=0,
m_0,eff^2 + lambda_03 v^2/2 > 0.
```

These are compatible with electroweak precision physics and do not depend on De Vries.

The D7 gravitational shape calculation remains a model constraint:

```text
a=2       stable for pure normalized curvature at fixed seven-volume,
a=2/5     unstable for the same pure term and needs extra stabilizing contributions.
```

This constraint affects compactification stability, not the De Vries comparison.

## Next Physics Calculation

The remaining active De Vries search has only one physics-first form:

```text
write an actual interface/boundary/defect/finite trace term in L_4,
identify its retained fields q,p,
compute its quadratic Hessian at the vacuum,
read alpha, beta, M, response kinetic norm, and sigma_r,
delete the branch if the output differs from the required source-action ledger.
```

No theorem depending on the desired De Vries block should be developed before that source term is
written and expanded.

The audit separating positive local energies from signed relative or constraint sources is
recorded in `notes/Positive_Local_Source_Relative_Gain_Audit.md`.
