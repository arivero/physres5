# Projection Gain Spectral Obstruction

Date: 2026-06-01.

Status: research note.  Algebraic test of whether an orthogonal projection principle can force
the De Vries signed Hessian coefficient while preserving the `C_2(j)` spectrum.

## Purpose

The branch mismatch proposal uses

```text
S_gain(q,p) = (tau/2) [ ||q||^2 - ||q-P^dagger p||^2 ],
```

which has Hessian

```text
H(P) =
  [ 0       P^dagger ]
  [ P     -P P^dagger ].
```

This gives the De Vries coefficient `c=1` if `p` remains a retained interface variable.  The
test below checks what happens when `p` is instead eliminated as the orthogonal best-fit
projection.

## Setup

Let

```text
P:E -> F
```

be a bounded finite-dimensional model for the retained branch, boundary, or vertical operator.
Let `q in E` be the mismatch coordinate and `p in F` the patching amplitude.  On a singular pair

```text
P u_j = s_j v_j,
P^dagger v_j = s_j u_j,
K_j=s_j^2.
```

For the normalized vertical-gradient candidate,

```text
K_j=C_2(j)
```

after generator and metric normalizations have been fixed.

## Uneliminated Signed Hessian

Keeping `p` as an independent variable gives the quadratic form

```text
Q(q,p) = 2 Re <P q,p> - <P^dagger p,P^dagger p>.
```

In the singular pair basis `(u_j,v_j)`, the Hessian matrix is

```text
H_j =
  [ 0      s_j ]
  [ s_j   -s_j^2 ].
```

The eigenvalue equation is

```text
lambda^2 + K_j lambda - K_j = 0.
```

The De Vries square-root branches therefore require the uneliminated two-field Hessian.  The
singular value `s_j` appears once in the mixed entry and twice in the lower diagonal entry.

## Literal Orthogonal Projection

Now minimize the mismatch over `p`:

```text
min_p ||q-P^dagger p||^2.
```

The normal equation is

```text
P P^dagger p = P q.
```

For closed range, the best-fit patch is

```text
P^dagger p_* = Pi_R q,
R=range(P^dagger),
```

where `Pi_R` is the orthogonal projector onto `R`.  Substituting gives

```text
S_proj(q)
  = (tau/2) [ ||q||^2 - ||q-Pi_R q||^2 ]
  = (tau/2) ||Pi_R q||^2.
```

The effective Hessian on `q` is therefore

```text
Pi_R,
```

with eigenvalues `0` and `1`.  The singular values `s_j` disappear.  On any nonzero singular
sector in `range(P^dagger)`, the result is the same projector eigenvalue, independent of
`C_2(j)`.

Thus literal orthogonal projection is an obstruction for De Vries roots.  It fixes a coefficient
by projection geometry but erases the spectral data needed for the W/Z ratio.

## Alternative With A Unit Diagonal

A different first-order action

```text
Q_unit(q,p) = 2 Re <P q,p> - ||p||^2
```

does preserve `P^dagger P` after eliminating `p`:

```text
p_*=P q,
Q_unit(q,p_*) = ||P q||^2.
```

The uneliminated Hessian in the singular pair is

```text
H_unit,j =
  [ 0      s_j ]
  [ s_j   -1 ],
```

with characteristic equation

```text
lambda^2 + lambda - K_j = 0.
```

This keeps the Casimir in the reduced `q` action but changes the De Vries Hessian.  The lower
diagonal entry is independent of `K_j`, so the root equation differs from
`lambda^2+K_j lambda-K_j=0`.

## Three-Way Tension

The algebra exposes three distinct constructions:

```text
1. Orthogonal best-fit projection:
   eliminates p, fixes the coefficient, loses K_j.

2. Unit auxiliary variable:
   eliminates p, keeps K_j in the q-action, gives lambda^2+lambda-K_j=0.

3. De Vries signed Hessian:
   keeps p as an interface variable, gives lambda^2+K_j lambda-K_j=0.
```

The third construction is the only one with the De Vries root equation.  It cannot be justified
by literal minimization of `||q-P^dagger p||^2` before the Hessian spectrum is read.

## Consequence For The Branch Programme

The branch graph/anti-graph splitting still matters.  It supplies a canonical mismatch coordinate
`q` and a natural Hilbert norm.  The projection calculation, however, cannot be the full
explanation for the De Vries spectrum.

The remaining viable interpretation is:

```text
q = anti-graph mismatch coordinate,
p = independent branch/interface response variable,
P = normalized vertical-gradient or boundary square-root operator,
H(P) = second variation before p is eliminated.
```

The retained response must also pass a kinetic-normalization test.  The lower diagonal term may
come from the pullback stiffness `||P^dagger p||^2`, while the kinetic norm of `p` must not be
the same sector-dependent image norm.  Otherwise canonical normalization erases the singular
values.  See `notes/Retained_Response_Pullback_Stiffness_Criterion.md`.

The coefficient `c=1` then needs a principle that fixes the uneliminated two-field action, rather
than a principle that projects `p` away.  Possible sources:

```text
first-order parent action,
symplectic or Green-form boundary pairing,
Calderon relative graph norm with both variables retained,
finite trace action with two retained finite directions,
Ward identity fixing the lower diagonal coefficient.
```

## Moduli Compatibility

If `P(u)^dagger P(u)|_j=x0(u) C_2(j)+sigma_j(u)`, the uneliminated De Vries block has

```text
lambda^2 + K_j(u) lambda - K_j(u)=0,
K_j(u)=x0(u) C_2(j)+sigma_j(u).
```

The projection-reduced action has no `K_j(u)` dependence on the nonzero range.  Therefore
projection reduction cannot test or preserve KK-moduli compatibility of the De Vries ratio.

## Objections And Repairs

Objection 1: an actual boundary theory may integrate out auxiliary fields.

Repair: distinguish physical integration from the spectral Hessian used for the De Vries
comparison.  If the physical reduced theory integrates out `p`, the De Vries block must be read
as an unreduced fluctuation matrix, not as the final one-field effective action.

Objection 2: a weighted projection might retain singular values.

Repair: write the weight explicitly.  A `PP^dagger` weight gives the De Vries lower diagonal only
when `p` is retained.  Eliminating `p` with that weight still gives a projector on the relevant
range.

Objection 3: the branch mismatch action may contain additional local terms.

Repair: include them as `A_0`, `sigma_j`, or independent coefficients.  Free local terms weaken
the symmetry derivation unless a Ward identity, Calderon construction, or trace action fixes
them.

## Current Criterion

A projection-based De Vries derivation must satisfy:

```text
P is named and normalized before comparison,
P^dagger P|_j = x0 C_2(j)+sigma_j is derived,
p remains a retained interface variable in the Hessian,
the lower diagonal term is -P P^dagger rather than -I,
the coefficient of -P P^dagger is fixed by the action,
moduli do not introduce uncontrolled x0 or sigma_j.
```

If the derivation instead eliminates `p` by ordinary orthogonal projection, it reaches a projector
wall for the De Vries spectrum.
