# Scale Absorption Criterion For De Vries

Date: 2026-06-01.

Status: algebraic criterion separating the De Vries Hessian coefficient from the Casimir scale
normalization.

## Purpose

The common-scale note shows that round `SO(3)` symmetry gives

```text
P^dagger P|_j = x0 C_2(j)
```

but does not set `x0=1`.  The boundary-Hessian note also has an off-diagonal coefficient
`alpha`.  The relevant root parameter after canonical field normalization is the product

```text
K_j = alpha^2 x0 C_2(j),
```

not `x0` alone.  Therefore the unscaled De Vries normal form requires two separate action-level
equalities:

```text
beta = alpha^2,
alpha^2 x0 = 1.
```

## Setup

Let `P_0:E_j->F_j` denote a normalized vertical-gradient or boundary operator with

```text
P_0^dagger P_0|_j = C_2(j).
```

Let the geometric metric and trace normalization produce

```text
P = sqrt(x0) P_0.
```

A general retained two-field Hessian in canonical field variables has the form

```text
H_{alpha,beta}(P) =
  [ 0            alpha P^dagger ]
  [ alpha P   - beta P P^dagger ].
```

On a singular-vector pair for `P_0`, with

```text
P_0 u_j = sqrt(C_2(j)) v_j,
```

the matrix becomes

```text
H_j =
  [ 0                         alpha sqrt(x0 C_2(j)) ]
  [ alpha sqrt(x0 C_2(j))    -beta x0 C_2(j)        ].
```

Its eigenvalue equation is

```text
lambda^2 + beta x0 C_2(j) lambda - alpha^2 x0 C_2(j)=0.
```

After defining

```text
K_j = alpha^2 x0 C_2(j),
c = beta/alpha^2,
```

the equation has the standard signed-Hessian form

```text
lambda^2 + c K_j lambda - K_j=0.
```

## Two Conditions

The condition

```text
c=1
```

is equivalent to

```text
beta=alpha^2.
```

It fixes the relative coefficient between the linear sewing term and the quadratic response
stiffness.  It does not fix the scale of `K_j`.

The unscaled Casimir root condition

```text
K_j=C_2(j)
```

is equivalent to

```text
alpha^2 x0=1.
```

Thus a valid unscaled De Vries derivation needs

```text
beta=alpha^2,
alpha^2 x0=1,
sigma_j controlled.
```

The first equality concerns the Hessian shape; the second concerns metric/action scale matching.

## When Scale Absorption Works

An action may absorb the geometric scale if its mixed coefficient depends on the same moduli:

```text
alpha(u)=x0(u)^(-1/2).
```

Then

```text
K_j=C_2(j).
```

For `c=1`, the same action must also give

```text
beta(u)=alpha(u)^2=x0(u)^(-1).
```

This pattern has a natural interpretation: the Green-form or finite trace coefficient uses the
inverse physical adjoint length, while the geometric operator uses the physical adjoint length.
The two factors cancel after canonical normalization.

The orthogonal mismatch action with a normalized operator gives another route:

```text
P=P_0,
alpha=1,
beta=1.
```

Then both required equalities hold directly.  For a physical operator `P=sqrt(x0)P_0`, the same
orthogonal mismatch action gives `alpha=1`, `beta=1`, and therefore leaves `K_j=x0 C_2(j)`.

## Counterargument Pass

Three common repairs fail unless the canonical kinetic norms are stated.

1. Rescaling `P` by hand changes `K_j`; it does not prove `alpha^2 x0=1`.
2. Rescaling `p` can move the factor between `x0`, `alpha`, and `beta`; after canonical kinetic
   normalization the combination `alpha^2 x0` returns.
3. Choosing units can remove an overall mass dimension, but the nonlinear ratio
   `x(2 alpha^2 x0)/x(3 alpha^2 x0/4)` still depends on the dimensionless product
   `alpha^2 x0`.

Hence the scale cannot be treated as harmless unless the compared observable cancels it or the
same action derives the cancellation.

## Proargument Pass

The strongest current route becomes:

```text
branch SO(3) symmetry
  -> round adjoint response metric
  -> P^dagger P|_j=x0 C_2(j),

Green/trace normalization
  -> alpha=x0^(-1/2),

pullback stiffness from the same mismatch functional
  -> beta=x0^(-1),

therefore
  c=beta/alpha^2=1,
  K_j=alpha^2 x0 C_2(j)=C_2(j).
```

This route would derive both the De Vries Hessian shape and the unscaled Casimir input from one
metric/action normalization.  It supplies a sharper target for the branch-interface calculation
than merely asking for `x0=1`.

A concrete implementation through a common retained-response kinetic factor is recorded in
`notes/Common_Response_Kinetic_Scale_Cancellation.md`.
The same issue can be stated as a quotient test `x0/m`; see
`notes/Map_Scale_Versus_Response_Metric_Scale.md`.

## Repair Tests

For each D5, D6, or D7 candidate, record after canonical field normalization:

```text
P_0^dagger P_0|_j=C_2(j),
P=sqrt(x0)P_0,
alpha,
beta,
K_j=alpha^2 x0 C_2(j)+sigma_j,
c=beta/alpha^2.
```

Accept the unscaled De Vries source only if

```text
alpha_{1/2}=alpha_1,
beta_{1/2}=beta_1,
alpha^2 x0=1,
beta=alpha^2,
sigma_1-sigma_{1/2} controlled.
```

If only `beta=alpha^2` holds, then the result has the scaled form

```text
lambda^2 + x0 C_2(j) lambda - x0 C_2(j)=0
```

up to the off-diagonal normalization.  A produced document must not quote the unscaled De Vries
number from that weaker result.
