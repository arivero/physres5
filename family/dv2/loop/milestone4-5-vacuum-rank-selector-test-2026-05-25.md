# Milestones 4/5 vacuum rank and selector test -- 2026-05-25

## Question

Milestone 4 asks whether the bulk potential selects the `rho,tau` point.
Milestone 5 asks whether the selector potential supplies more than compatible
algebraic targets.  This note tests both at the level of stationarity.

## Selector derivative decoupling

Write the selector terms schematically as

```tex
V_{\rm sel}
=C_{\rm cur}S_{\rm cur}^2+C_vS_v^2+C_HS_H^2,
```

where

```tex
S_{\rm cur}=\kappa_{\rm cur}-1,
\qquad
S_v=v_Q^2-\mu_B(\rho,\tau)^2J_v,
\qquad
S_H=\lambda_H-\lambda_{\rm dV}.
```

On the selector branch,

```tex
S_{\rm cur}=S_v=S_H=0.
```

Therefore

```tex
\partial_\rho V_{\rm sel}
=\sum_i(\partial_\rho C_i)S_i^2+2\sum_iC_iS_i\partial_\rho S_i=0,
```

and the same holds for `\partial_\tau V_{\rm sel}`.  Thus the squared selector
terms do not select `rho,tau` once their own algebraic equations are imposed.
The `rho,tau` selection is entirely a bulk coefficient problem.

## Rank of the bulk stationarity equations

For fixed `rho` and `tau`, the two equations

```tex
\partial_\rho V_{\rm bulk}=0,
\qquad
\partial_\tau V_{\rm bulk}=0
```

are two linear constraints on

```tex
B_R,B_H,B_0,B_2,B_4,B_6,B_{\rm loc}.
```

The coefficient matrix has rank two for generic `rho,tau`, so the stationary
target leaves a five-dimensional coefficient family even before `tau` is
selected.

There is also a direct two-term fit illustrating the freedom.  Set

```tex
B_H=B_0=B_2=B_6=0.
```

The `rho` equation is solved by

```tex
B_4=B_R\tau^2.
```

The `tau` equation then gives

```tex
B_{\rm loc}=-{2\over3}B_R\tau\rho^{-2}.
```

At the de Vries-compatible target

```tex
\rho_*=9.463469757158872,
```

this is

```tex
B_{\rm loc}=-0.007444027070759169\,B_R\tau.
```

Thus the target can be made stationary by a coefficient balance without using
the de Vries data as an output of the geometry.

## Impact of Milestone 6

Milestone 6 now gives a source-balance no-go for the current D8/O8 package.
Consequently `B_{\rm loc}` cannot be treated as a free valid coefficient for
that package: the localized source data do not satisfy the global Bianchi
system.

Even before this consistency failure, the rank test shows that the scaling
potential alone does not predict `rho_*`.  After the consistency failure, the
localized coefficient itself belongs to a source package that fails globally.

## Selector verdict

The full-current Milestone 3 branch removes `kappa_cur` from the minimal
selector variables.  The remaining written selector conditions are

```tex
v_Q^2=\mu_B(\rho,\tau)^2(1+\sqrt3),
\qquad
\lambda_H=\lambda_{\rm dV}.
```

They are algebraic targets supplied by the written potential.  The current
action does not compute `mu_B(rho,tau)`, the neutral scalar potential, or the
radial Hessian coefficient.

## Decision

Milestone 4 fails as a prediction in the current route.  The bulk equations are
a coefficient-balance system with too many free inputs, and the localized
coefficient is attached to a source package that fails Milestone 6.

Milestone 5 also fails as an induced selector.  On the selector branch the
squared selector terms do not affect `rho,tau`, and the written action does not
compute the `v_Q` or `lambda_H` coefficients.

The current D10 construction therefore remains a compatibility framework for
the vacuum/scalar slice, not a vacuum derivation of the de Vries data.
