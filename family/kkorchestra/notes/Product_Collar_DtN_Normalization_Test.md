# Product-Collar DtN Normalization Test

Date: 2026-06-01.

Status: local model calculation for the Boundary Calderon / DtN programme.

## Aim

The boundary programme uses an order-one operator `P_boundary` satisfying

```text
P_boundary^*P_boundary|_j = x0 C_2(j) + sigma_j.
```

A product-collar scalar model shows which part comes from ordinary Dirichlet-to-Neumann theory
and which part still needs an auxiliary boundary/interface Hessian.

## Half-Cylinder Scalar Model

Let

```text
L = -partial_u^2 + Q,
Q e_j = kappa_j^2 e_j,
kappa_j^2 = x0 C_2(j).
```

On the half-cylinder `u>=0`, the decaying solution with boundary value `f_j e_j` is

```text
u_j(u)=e^(-kappa_j u) f_j e_j.
```

For the bulk action

```text
S_bulk[u] =
  tau/2 int_0^infty [
    ||partial_u u||^2 + <u,Q u>
  ] du,
```

the on-shell value is

```text
S_on-shell(f_j)=tau/2 kappa_j |f_j|^2.
```

Thus the Dirichlet-to-Neumann operator is

```text
Lambda_infty|_j = kappa_j = sqrt(x0 C_2(j)).
```

The scalar DtN action supplies the order-one quadratic form

```text
S_on-shell = tau/2 <f, Lambda_infty f>.
```

It does not by itself supply the signed Hessian

```text
[ 0       P^* ]
[ P   -c P P^* ].
```

The DtN operator can serve as `P`, with `P^*P=Q`, but the mixed field and the quadratic
`P P^*` entry must come from additional boundary/interface variables or constraints.

## Finite Cylinder

On `[0,T]` with Dirichlet condition at `u=T`, the solution is

```text
u_j(u)=sinh(kappa_j(T-u))/sinh(kappa_j T) f_j e_j.
```

The DtN eigenvalue at `u=0` is

```text
Lambda_T^D|_j = kappa_j coth(T kappa_j).
```

If this finite-cylinder DtN operator is used as `P`, then

```text
P^*P|_j
  = kappa_j^2 coth^2(T kappa_j)
  = x0 C_2(j) + sigma_j^D(T),

sigma_j^D(T)
  = x0 C_2(j) [coth^2(T sqrt(x0 C_2(j))) - 1].
```

The correction remains sector-dependent unless `T sqrt(x0 C_2(j))` is large in every compared
sector.

For a Neumann condition at `u=T`, the solution gives

```text
Lambda_T^N|_j = kappa_j tanh(T kappa_j),

sigma_j^N(T)
  = x0 C_2(j) [tanh^2(T sqrt(x0 C_2(j))) - 1].
```

The Neumann finite-cylinder correction is negative and the zero-mode limit is singular for the
square-root interpretation:

```text
Lambda_T^N|_{kappa=0}=0,
Lambda_T^D|_{kappa->0}=1/T.
```

## Consequence For `c`

The product-collar DtN calculation fixes the spectral operator:

```text
P = Lambda,
P^*P = Lambda^2.
```

It does not fix the signed-Hessian coefficients

```text
alpha,
beta,
c=beta/alpha^2.
```

A boundary/interface action must add or derive a second boundary variable `p` and a quadratic
form of the type

```text
S_boundary^(2)(q,p) =
  tau/2 [
    2 alpha Re <p, P q>
    - beta <p, P P^* p>
  ]
  + ...
```

The De Vries value requires `beta=alpha^2` after canonical normalization.  Ordinary scalar DtN
gives no such equality by itself.

## Two Acceptable Uses Of DtN

1. Direct DtN boundary energy.

   Use the on-shell action

   ```text
   S_on-shell = tau/2 <q, Lambda q>.
   ```

   This contributes an order-one positive boundary stiffness to the bosonic potential.  It can
   stabilize or shift boundary modes, but it does not produce the signed-Hessian root equation.

2. DtN as a first-order building block.

   Use

   ```text
   P=Lambda,
   P^*P=Lambda^2.
   ```

   Then place `P` inside an interface Hessian with a second boundary variable.  This can produce
   the De Vries rational roots if the same action supplies sector-independent `alpha,beta` and
   the needed normalization.

## Product-Collar Test For The Project

For each candidate boundary `Sigma`, the first controlled calculation should report:

```text
Q|_j = x0 C_2(j) + q_j^lower,
Lambda|_j = sqrt(Q|_j) + lower order,
P^*P|_j = Lambda^2|_j,
sigma_j = P^*P|_j - x0 C_2(j),
```

then separately report:

```text
Does the boundary/interface action contain p?
What are alpha and beta after canonical normalization?
Is beta=alpha^2 forced, selected, or tuned?
```

## Objections And Repairs

1. Direct DtN energy has the wrong order for the signed block.

   The direct energy is `<q,Lambda q>`, while the diagonal entry in the signed Hessian uses
   `P P^*`.  The repair is to distinguish boundary stabilization from the De Vries Hessian.

2. Finite collars create sector-dependent shifts.

   The corrections `coth^2(T kappa_j)-1` or `tanh^2(T kappa_j)-1` generally differ between
   `j=1/2` and `j=1`.  The repair is to take a controlled long-collar limit or retain these
   corrections in `sigma_j`.

3. Zero modes need separate treatment.

   For `j=0`, the Neumann finite-cylinder DtN operator vanishes, while the Dirichlet finite
   cylinder gives `1/T`.  The repair is to exclude the zero sector from the golden-rule
   comparison or track it as a boundary mass term rather than a Casimir square root.

## Minimal Conclusion

The product-collar test supports the use of DtN as a source of square-root Casimir data:

```text
Lambda^2|_j = x0 C_2(j)
```

in the half-cylinder model.  It also shows that `c=1` cannot be inferred from ordinary DtN
alone.  The signed Hessian requires a separate boundary/interface variable and an action-level
normalization test.
