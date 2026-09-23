# Boundary Hessian and Schur-Complement Derivation

Date: 2026-06-01.

Status: action-level algebra for the boundary Calderon/DtN part of the active D5/D6/D7
programme.

## Aim

The boundary operator programme needs more than the spectral statement

```text
P^*P|_j = x0 C_2(j) + sigma_j.
```

It also needs the quadratic action to place the same operator in the linear and quadratic
entries of the signed Hessian.  This note records the finite-dimensional normal form and the
test for the De Vries coefficient.

## Algebraic Normal Form

Let `P:E_j -> F_j` be the retained boundary, branch, or vertical operator on one `SU(2)` sector.
Assume a singular-vector pair

```text
P u_j = s_j v_j,
P^* v_j = s_j u_j,
s_j^2 = J_j = x0 C_2(j) + sigma_j.
```

The reduced boundary Hessian has the form

```text
H_{alpha,beta}(P) =
  [ 0            alpha P^* ]
  [ alpha P   - beta P P^* ].
```

On the span of `(u_j,v_j)`, its eigenvalue equation is

```text
lambda^2 + beta J_j lambda - alpha^2 J_j = 0.
```

If the off-diagonal operator is normalized as

```text
P_norm = alpha P,
P_norm^* P_norm = alpha^2 J_j,
```

then

```text
H_{alpha,beta}(P) =
  [ 0              P_norm^* ]
  [ P_norm    - c P_norm P_norm^* ],

c = beta/alpha^2.
```

Thus the De Vries value `c=1` means

```text
beta = alpha^2
```

after the same field normalization has been used in both entries.  The remaining overall factor
in the action scales all eigenvalues and belongs to the physical mass scale, not to `c`.

## Positive and Negative Branches

For the normalized block

```text
H_c(P_norm) =
  [ 0              P_norm^* ]
  [ P_norm    - c P_norm P_norm^* ],
```

write

```text
K_j = P_norm^*P_norm|_j = alpha^2 J_j.
```

The eigenvalue equation is

```text
lambda^2 + c K_j lambda - K_j = 0.
```

The positive root `a_j` and the negative-root magnitude `b_j` obey different rational forms:

```text
a_j^2/(1 - c a_j) = K_j,
b_j^2/(1 + c b_j) = K_j.
```

Therefore the commonly used expression

```text
x_j^2/(c x_j + 1) = K_j
```

is the negative-root magnitude equation.  The positive vector-mass branch uses the denominator
`1-c a_j`.  Any comparison between the W/Z positive roots and the Higgs/vacuum negative roots
need this branch convention stated explicitly.

For the De Vries normalization `c=1` and unshifted `K_j=J_j=j(j+1)`,

```text
a_j = (sqrt(J_j^2 + 4J_j) - J_j)/2,
b_j = (sqrt(J_j^2 + 4J_j) + J_j)/2.
```

## Schur-Complement Reading

The same equation can be read as an eigenvalue-dependent Schur complement.  For `lambda` away
from `-cK_j`, the second row gives

```text
v_j = (lambda + c P P^*)^(-1) P u_j.
```

Substitution into the first row gives

```text
P^*(lambda + c P P^*)^(-1) P u_j = lambda u_j.
```

On the singular-vector pair this becomes

```text
J_j/(lambda + c J_j) = lambda
```

before off-diagonal normalization, or the same equation with `J_j` replaced by `K_j` after
normalization.  The rational root therefore arises from eliminating the auxiliary boundary
amplitude, while the square-root data enters through `P^*P`.

## Boundary Action Test

A concrete boundary action should identify the two fields whose Hessian is
`H_{alpha,beta}(P)`.  A schematic quadratic boundary functional is

```text
S_boundary^(2)(q,p) =
  tau/2 [
    2 alpha Re <p, P q>
    - beta <p, P P^* p>
  ]
  + tau/2 <q, A_0 q>
  + local counterterms.
```

The simplest De Vries sector takes `A_0=0` after projecting to the retained patching variables.
More generally, a nonzero `A_0` shifts the characteristic equation and is recorded as part
of `sigma_j` or as a separate failure of the normal form.

The coefficient test is:

```text
alpha_j = alpha       independent of j,
beta_j = beta         independent of j,
c = beta/alpha^2,
K_j = alpha^2 [x0 C_2(j) + sigma_j].
```

The golden-rule comparison survives only if the same action yields sector-independent `alpha`,
`beta`, and the residual sector dependence in `sigma_j` is controlled.

## Application To Boundary/DtN Data

For a product collar,

```text
D = c(nu)(partial_u + A_Sigma),
P_boundary = |A_Sigma|_ren.
```

For a scalar Laplace model, the on-shell DtN action is instead the direct order-one boundary
form

```text
S_on-shell = (tau/2) <q, P_boundary q>.
```

This direct term can stabilize boundary modes but does not produce the signed Hessian.  The
signed-Hessian use of `P_boundary` requires a second boundary/interface variable and the
`H_{alpha,beta}` block below.

The action-level test becomes

```text
P_boundary^*P_boundary|_j = x0 C_2(j) + sigma_j,
H_{alpha,beta}(P_boundary) from S_boundary^(2),
c = beta/alpha^2.
```

The exact values of `alpha` and `beta` can depend on:

```text
tau_boundary,
collar length and metric scale,
normalization of boundary fields,
flat character chi,
sheet-exchange lift G_B,
choice of APS/Calderon projection,
local boundary counterterms.
```

These data are fixed once for the `j=1/2` and `j=1` sectors.

## Application To D5, D6, And D7

For the D5 endpoint:

```text
Sigma = M_5(5),
chi = chi_{1,3},
P = |A_{5,chi}|_ren.
```

The same flat lift must enter the eta invariant, the Calderon projector, and the Hessian
coefficients `alpha,beta`.

For the D6 branch link:

```text
Sigma = N_B,
P = |A_{N_B,n,r,G}|_ren.
```

The sheet-exchange lift `G_B` can affect both `sigma_j` and the mixed term coefficient `alpha`.
The branch-cover construction contributes to the golden-rule relation only if this dependence is
sector-independent or constrained by the branch symmetry.

For the D7 cylinder:

```text
P = Lambda_T,
Lambda_T|_j = sqrt(K_j) coth(T sqrt(K_j)).
```

Finite length shifts `K_j` by a nonlinear sector-dependent correction unless the restoration
limit suppresses it or the correction is retained explicitly in `sigma_j`.

## Objections And Repairs

1. The signed Hessian is indefinite.

   The De Vries block has one positive and one negative branch on each nonzero singular pair.
   A Euclidean positive-definite boundary energy cannot use this block as its full stability
   matrix.  The repair is to interpret `H_c` as a signed second-variation block for patching,
   constraint elimination, or Lorentzian/quadratic fluctuation variables, while the final
   physical vacuum still passes the full positive-Hessian tests in the bosonic potential.
   The positive-source separation is recorded in
   `notes/Positive_Local_Source_Relative_Gain_Audit.md`.

2. The coefficient `c` can change under field rescaling.

   Independent rescalings of `q` and `p` alter `alpha` and `beta`.  The repair is to fix the
   kinetic normalization of both boundary fields before reading off `c`.  Once kinetic terms are
   canonical, `c=beta/alpha^2` becomes a meaningful dimensionless test.

3. Boundary counterterms can manufacture `c=1`.

   A local counterterm may tune `beta`.  The repair is to allow only counterterms derived from
   the same D5 filling, branch defect, Calderon projection, or higher-dimensional action.  A
   free counterterm weakens the geometric claim to a fit.

4. The branch equation can be mixed up.

   The relation `x^2/(c x+1)=K_j` belongs to the negative-root magnitude.  The positive branch
   uses `x^2/(1-cx)=K_j`.  Repairs and comparisons state which branch supplies W/Z data and
   which branch supplies scalar-instability or vacuum data.

5. The boundary spectrum may spoil the Casimir law.

   Curvature, torsion, holonomy, flat characters, finite cylinders, and non-product collars can
   produce large sector-dependent `sigma_j`.  The repair is to compute these terms in the same
   convention as the action coefficients.

## Failure Criteria

The boundary-Hessian route fails as a geometric derivation if any of the following occurs:

```text
alpha_{1/2} != alpha_1 after canonical normalization,
beta_{1/2} != beta_1 after canonical normalization,
beta/alpha^2 has no reason to equal 1 or a controlled universal c,
sigma_1 - sigma_{1/2} is comparable to x0[C_2(1)-C_2(1/2)],
APS and Calderon data require incompatible flat-character conventions,
positive-root and negative-root assignments are interchanged without changing the rational formula.
```

## Minimal Success Statement

A successful boundary derivation should produce:

```text
P^*P|_{1/2} = x0 (3/4) + sigma_{1/2},
P^*P|_1     = x0 (2)   + sigma_1,
alpha_{1/2}=alpha_1,
beta_{1/2}=beta_1,
c=beta/alpha^2,
```

with the D5 character, D6 branch lift, and D7 restoration convention fixed before comparison.
The special De Vries value is the additional condition

```text
beta=alpha^2.
```

The unscaled Casimir normal form also requires the scale condition
`alpha^2 x0=1`; see `notes/Scale_Absorption_Criterion_For_DeVries.md`.

The product-collar scalar calculation that separates direct DtN energy from interface-Hessian
use is recorded in `notes/Product_Collar_DtN_Normalization_Test.md`.
The calibrated mismatch-gain test for deriving `beta=alpha^2` is recorded in
`notes/Affine_Mismatch_Ward_Calibration_Test.md`.
The audit deleting positive local boundary or defect potentials as retained signed Hessian
sources is recorded in `notes/Positive_Local_Source_Relative_Gain_Audit.md`.
