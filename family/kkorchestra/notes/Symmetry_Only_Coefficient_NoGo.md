# Symmetry-Only Coefficient No-Go

Date: 2026-06-01.

Status: deletion note for the De Vries coefficient route based on branch symmetry alone.

## Purpose

The active De Vries goal asks for a relation from symmetry and Kaluza-Klein moduli without
inserting the desired Hessian coefficient.  The branch notes have a strong partial result:
unitary sheet exchange gives a canonical graph/anti-graph splitting, and an affine matching
symmetry can make the residual mismatch depend on

```text
r = q - P^dagger p.
```

Those facts do not by themselves calculate the signed two-field Hessian coefficient.  The
coefficient requires a source-action observable, not branch symmetry alone.

## Minimal Variables

Let

```text
q in E
p in F
h = P^dagger p in E
```

where `q` is the anti-graph mismatch and `h` is the correction supplied by the retained
response.  Suppose the branch Hilbert norm and the operator `P` have been computed.
Write the most general quadratic expression built from the mismatch norm and an independent
response-image stiffness as

```text
S(q,p) =
  (1/2) [
    tau_m ||q - P^dagger p||^2
    + tau_q ||q||^2
    + tau_h ||P^dagger p||^2
  ].
```

An affine shift

```text
q -> q + zeta,
P^dagger p -> P^dagger p + zeta
```

removes the independent `tau_q` term from the mismatch energy, but it allows

```text
tau_h ||P^dagger p||^2
```

unless another source principle forbids it.

## Calculation

The positive mismatch energy has Hessian entries

```text
q-q entry:  tau_m
q-p entry: -tau_m P^dagger
p-p entry:  tau_m P P^dagger
```

after projecting to the retained image sector.  It therefore has a nonzero `q-q` entry.
The signed De Vries-type block uses no such diagonal entry.

Subtracting the unpatched baseline gives the calibrated gain

```text
Delta S(q,p) = S(q,0) - S(q,p).
```

If `tau_q=0`, the quadratic part is

```text
Delta S(q,p)
  = tau_m Re <q,P^dagger p>
    - (1/2)(tau_m + tau_h) ||P^dagger p||^2.
```

In the standard Hessian notation,

```text
alpha = tau_m,
beta  = tau_m + tau_h,
c     = beta/alpha^2
      = (tau_m + tau_h)/tau_m^2
```

after canonical kinetic normalization of `q` and `p`.

Therefore branch symmetry and affine mismatch symmetry do not compute `c=1`.  They compute the
allowed variables.  The value follows only after the same source action fixes

```text
tau_h = 0
```

and fixes the calibrated baseline coefficient in canonical variables.

## Moduli Compatibility

Let `u` denote a radion, branch radius, collar length, Wilking squash, flat character, or
endpoint holonomy.  Symmetry can at most make

```text
c(u) = (tau_m(u) + tau_h(u))/tau_m(u)^2
```

sector-independent.  It does not force

```text
c(u_*) = 1
```

at the comparison point.  A constant but uncomputed `c` remains a parameter.

The spectral part has a separate quotient test:

```text
K_r^can(u) = gamma(u)^2 mu_r + sigma_r^can(u).
```

Thus even a valid coefficient calculation still needs the map-scale calculation.  The two tests
cannot be collapsed into one assumption.

## Deletion

Delete the following route as a standalone De Vries derivation:

```text
unitary branch splitting
  + affine mismatch symmetry
  -> c=1.
```

The correct status is narrower:

```text
unitary branch splitting
  + affine mismatch symmetry
  -> canonical q and q-P^dagger p variables.
```

The coefficient row remains open only for a source-action calculation that derives the
calibrated gain observable with no independent response-image stiffness.

## Proargument For The Remaining Route

The strongest surviving chain is:

```text
unitary sheet exchange
  -> canonical anti-graph norm,

affine matching symmetry
  -> mismatch energy depends on q-P^dagger p,

source observable equals calibrated improvement
  -> Delta S = S(q,0)-S(q,p),

same trace norm supplies both terms
  -> tau_h=0 after canonical normalization,

retained response field is not eliminated
  -> signed two-field Hessian keeps the computed multiplier.
```

If a branch, Calderon, or finite trace action computes every arrow above, then the coefficient
calculation becomes action-derived rather than inserted.

## Counterargument

The remaining route can fail in several direct ways.

```text
the physical action is the positive mismatch energy S(q,p), not Delta S,
the source action contains an independent tau_h term,
the baseline S(q,0) has a different norm from the patched mismatch,
p is eliminated before reading the Hessian,
canonical kinetic normalization changes tau_m or tau_h by sector,
local boundary terms alter p-p stiffness,
sigma_r^can is not controlled.
```

Any one of these outputs deletes the coefficient claim from the active derivation.  Compatible
bosonic constraints, such as branch selection, response-sector deletion, or custodial `rho=1`,
can still be retained.

## Repair Tests

For the next branch-interface calculation, record:

```text
S_source(q,p) before baseline subtraction,
whether q and P^dagger p occur only as q-P^dagger p,
the precise baseline used to form Delta S,
tau_m and tau_h after canonical kinetic normalization,
m(u), gamma(u)^2, sigma_r^can(u),
whether p remains retained in the Hessian.
```

Accept the coefficient calculation only if the source gives

```text
tau_h=0,
c=1,
```

with the same canonical normalization used in the map-scale quotient.  Otherwise retain a
general `c` or delete the branch from De Vries use.
