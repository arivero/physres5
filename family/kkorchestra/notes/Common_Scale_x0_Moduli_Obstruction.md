# Common Scale x0 Moduli Obstruction

Date: 2026-06-01.

Status: scale-normalization obstruction and repair test for the De Vries symmetry programme.

## Purpose

The current vertical-gradient route can derive

```text
P^dagger P|_j = x0(u) C_2(j)
```

from an `SO(3)`-round response metric and a named Casimir operator.  Round symmetry controls
anisotropy but leaves a common scale.  A produced De Vries number would become ad hoc again if
the project silently replaced `x0(u)` by `1`.

## Metric Scaling

Let `T_i` be an `su(2)` basis normalized by

```text
[T_i,T_l]=epsilon_{ilr} T_r,
<T_i,T_l>_K = delta_{il}.
```

Let the physical adjoint metric at moduli point `u` be

```text
h_u(T_i,T_l)=R_A(u)^2 delta_{il}.
```

The physical orthonormal frame is

```text
E_i=R_A(u)^(-1) T_i.
```

If the vertical-gradient operator differentiates along physical orthonormal directions, then

```text
P(u) psi = gamma(u) sum_i J_i psi tensor E_i,
P(u)^dagger P(u)|_j = gamma(u)^2 R_A(u)^(-2) C_2(j).
```

Thus

```text
x0(u)=gamma(u)^2/R_A(u)^2.
```

Here `gamma(u)` represents the boundary/interface action coefficient after canonical field
normalization.  The round metric condition gives a scalar `R_A(u)^2`; it does not set the
dimensionless combination `gamma(u)^2/R_A(u)^2`.

## Effect On The Signed Hessian

For the retained two-field Hessian

```text
H_j =
  [ 0                 sqrt(K_j) ]
  [ sqrt(K_j)        -K_j       ],
K_j=x0 C_2(j),
```

the negative-root magnitude `x_j` satisfies

```text
x_j^2/(x_j+1)=K_j.
```

For the two diagnostic sectors,

```text
K_{1/2}=3 x0/4,
K_1=2 x0.
```

The root ratio depends on `x0`:

```text
x(K) = (K + sqrt(K^2+4K))/2,
R(x0)=x(2x0)/x(3x0/4).
```

The limiting values differ:

```text
x0 -> 0:       R(x0) -> sqrt(8/3),
x0 -> infinity: R(x0) -> 8/3.
```

Therefore a common scale cannot be ignored in the De Vries comparison unless the observable
being compared cancels it or the same action fixes its value.

## Relation To Gravity And Stabilization

The gravity notes decompose the compact metric into radion and shape variables:

```text
D6: u=epsilon^2=x_v/x_h,
D7: u=a=x_1/x_2.
```

The bosonic potential has the schematic form

```text
V_total =
  V_grav + V_YM + V_defect + V_boundary + V_Calderon
  + V_KK-sf + V_flux + V_higher.
```

The same terms that stabilize the radion, squashing, branch defect, and boundary data can change
`R_A(u)`, `gamma(u)`, or both.  The custodial condition `rho=1` constrains equality of weak
stiffnesses in the `m_3` block; it does not by itself determine the scale in the vertical
Casimir-response block.

## Proargument Pass

A symmetry-compatible route to `x0=1` remains possible if the model supplies a canonical
normalization tying the three ingredients together:

```text
Lie-algebra basis normalized by the same Killing form used in the action,
adjoint response frame normalized by the branch trace metric,
boundary/interface coefficient gamma(u) fixed by the Green form or finite trace action,
radion and branch moduli stabilized at a point where gamma(u)^2=R_A(u)^2.
```

Under those hypotheses, the vertical-gradient source becomes

```text
P^dagger P|_j=C_2(j)
```

after canonical field normalization, and the signed Hessian has the unscaled De Vries normal
form.

## Counterargument Pass

Roundness alone leaves the following one-parameter freedom:

```text
h_u -> lambda^2 h_u,
gamma(u) fixed
```

which changes

```text
x0 -> lambda^(-2) x0.
```

Alternatively,

```text
gamma(u) -> lambda gamma(u),
h_u fixed
```

changes

```text
x0 -> lambda^2 x0.
```

Both transformations preserve `SO(3)` covariance and keep `P^dagger P` proportional to
`C_2(j)`.  They change the De Vries root ratio.  Hence `SO(3)` symmetry, Schur's lemma, and
custodial `rho=1` do not determine the final number.

## Repair Tests

Any future produced claim using the unscaled De Vries value should give one of these data:

```text
an action-level derivation of gamma(u)^2/R_A(u)^2=1,
a physical observable in which x0 cancels,
a fitted or measured x0 stated as an input rather than a prediction,
a controlled sigma_j calculation showing a different normalization target.
```

For the D6 branch programme, compute in the same convention:

```text
R_A(u) from the SO(3) adjoint trace metric,
gamma(u) from the Green-form or finite trace coefficient,
u_* from partial_u V_total=0,
x0(u_*)=gamma(u_*)^2/R_A(u_*)^2.
```

Accept the unscaled De Vries source only if that final line gives `1` without tuning.  Otherwise
retain

```text
P^dagger P|_j=x0 C_2(j)+sigma_j
```

and compare scaled roots.

The related absorption criterion, where the mixed coefficient `alpha` can compensate the geometric
scale, is recorded in `notes/Scale_Absorption_Criterion_For_DeVries.md`.
The response-kinetic implementation of that compensation is recorded in
`notes/Common_Response_Kinetic_Scale_Cancellation.md`.
