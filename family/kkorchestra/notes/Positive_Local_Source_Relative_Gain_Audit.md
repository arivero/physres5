# Positive Local Source Relative Gain Audit

Date: 2026-06-01.

Status: source-action audit for positive boundary, defect, and local interface energies.

## Purpose

The active De Vries route keeps a retained response variable `p` and asks for the signed block

```text
H(P) =
  [ 0       P^dagger ]
  [ P     -P P^dagger ].
```

A positive local boundary or defect potential cannot supply this block as its full stable-vacuum
Hessian.  The route survives only if the block is a signed constraint, a relative-gain
observable, a Lorentzian quadratic form, or an unreduced saddle block whose stability is restored
by other fields or by later reduction.

## Singular Pair Calculation

Let

```text
P u_r = s_r v_r,
P^dagger v_r = s_r u_r,
s_r^2 = K_r.
```

On the span of `(u_r,v_r)`, the retained block is

```text
H_r =
  [ 0      s_r ]
  [ s_r   -K_r ].
```

Its determinant is

```text
det H_r = -s_r^2.
```

For every nonzero retained sector, `det H_r<0`.  Hence the block has one positive and one
negative eigenvalue.  A positive semidefinite Euclidean energy cannot have this matrix as its
complete Hessian at a stable vacuum.

## Positive Mismatch Energy

A local mismatch energy has the schematic form

```text
E_pos(q,p) =
  (tau/2) ||q - P^dagger p||^2
  + (tau_h/2) ||P^dagger p||^2
  + lower-order positive terms.
```

Expansion gives a positive `q-q` entry.  The resulting Hessian is a stabilization matrix, not
the retained signed block.  If `p` is minimized, the output is a Schur complement or projector
on the mismatch space.  The singular value information can collapse in that reduction.

Deletion:

```text
positive local mismatch energy -> De Vries retained Hessian.
```

The positive energy can still supply boundary stiffness, defect stabilization, branch selection,
and moduli constraints.

## Relative Gain

The signed block appears from the difference

```text
Delta E(q,p) = E_pos(q,0) - E_pos(q,p)
```

when the same norm is used and no independent response-image term is added.  For

```text
E_pos(q,p) = (tau/2)||q-P^dagger p||^2,
```

the relative quadratic form is

```text
Delta E(q,p)
  = tau Re <q,P^dagger p>
    - (tau/2)||P^dagger p||^2.
```

This gives the signed coefficient shape after the overall scale and kinetic normalizations are
handled.  The source question is no longer positivity.  The source question is whether the
physical theory computes `Delta E` as a legitimate unreduced action, constraint, response
functional, or measured improvement.

## General Local Source

Let a local source have three coefficients:

```text
S(q,p) =
  (tau_m/2)||q-P^dagger p||^2
  + (tau_h/2)||P^dagger p||^2
  + (tau_q/2)||q||^2.
```

The relative construction removes the `q-q` entry only when the unpatched baseline uses the same
norm and coefficient.  The `p-p` coefficient after relative subtraction is controlled by

```text
1 + tau_h/tau_m
```

up to kinetic normalization.  A local positive source permits `tau_h`, so positivity alone cannot
fix the De Vries coefficient.

## Proargument For A Surviving Source

The surviving source-action route is narrow:

```text
source computes a relative gain or signed constraint,
p remains retained in the Hessian,
same source gives the image stiffness ||P^dagger p||^2,
separate response kinetic norm is common across sectors,
tau_h is absent or fixed by the same source,
full physical vacuum has a positive stability matrix after all fields are included.
```

This route treats the retained block as an intermediate signed structure, not as the full
positive boundary potential.

## Counterargument

The route fails under any of the following outputs:

```text
the action is a positive Euclidean potential in q,p,
the relative sign is inserted only to remove the q-q term,
p is minimized before the spectrum is read,
the same image norm canonicalizes p,
local counterterms add tau_h,
the full stability problem has no positive completion,
the moduli quotient x0/m remains uncomputed.
```

Any such output deletes the source as a De Vries derivation.  Retain any independent bosonic
constraint that the positive source computes.

## Non-De Vries Constraints To Keep

Positive local boundary or defect energies remain useful for:

```text
stabilizing branch mismatch,
selecting determinant-compatible flat lifts,
fixing branch sign or holonomy,
adding positive mass to response complements,
supporting compactification stability,
preserving the orthodox rho=1 m_3 branch when the triplet vacuum is absent.
```

These outputs do not rely on the retained signed Hessian.

## Ledger Outcome

Delete the standalone route:

```text
positive local boundary/defect potential -> retained De Vries block.
```

Keep the narrow route:

```text
signed relative source or constraint
  + retained p
  + separate common response kinetic norm
  + computed operator multiplier and shifts
  + independent stability completion
  -> candidate retained-response Hessian.
```

## Repair Tests

For any local source proposal, record:

```text
whether the source is positive energy, Lorentzian action, constraint, or relative gain,
the variables q and p before any elimination,
the full Hessian in q,p,
the stability completion if the q,p block is indefinite,
the coefficient tau_h,
the kinetic norm of p,
the operator multiplier and shifts,
the moduli quotient x0/m.
```

Accept the source only if the signed block is computed by the source and the positive physical
stability problem is separately accounted for.
