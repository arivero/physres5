# Two-state negative-sector projector

## Question

Can a mainstream two-state scalar sector make the negative-root correction

```text
Delta M_-^2 = epsilon sigma_3,
epsilon = (3/8)(M_Z^2 - M_W^2),
```

a physical consequence rather than a chosen basis?

## Minimal two-state algebra

For two real negative-sector modes `Psi_- = (psi_1, psi_2)`, the most general
real symmetric leading perturbation is

```text
Delta = a 1 + b sigma_3 + c sigma_1 .
```

The eigenvalue shifts are

```text
delta m^2 = a +/- sqrt(b^2+c^2).
```

Trace preservation imposes `a = 0`.  With `a=0`, any nonzero traceless
perturbation can be rotated into a diagonal `sigma_3` form.  Therefore the
appearance of `sigma_3` is not itself a derived physical statement unless an
independent structure fixes the basis in which the two signed roots are
identified with the Higgs-like and Fermi-like negative modes.

## Hypercharge spurion obstruction

In custodial language hypercharge gauges the single generator `T_R^3`, not the
full `SU(2)_R`.  For a fundamental doublet,

```text
sum_a T_F^a T_F^a = C_F 1 = (3/4) 1,
(T_F^3)^2 = (1/4) 1.
```

The proposed coefficient uses

```text
C_F / C_A = (3/4)/2 = 3/8.
```

But a leading `g'^2` custodial-breaking spurion built only from the gauged
generator naturally contains `(T_R^3)^2`, which gives `1/4` in the fundamental,
not `3/4`.  Relative to an adjoint normalization this points to `1/8` or to a
trace ratio `Tr_F[(T^3)^2]/Tr_adj[(T^3)^2] = 1/4`, depending on convention, not
to `3/8`.

## What would be needed

A successful mainstream derivation needs more than a generic two-state sector.
It must provide all of the following:

1. A Lagrangian reason for the negative-root basis, so that `sigma_3` is not
   just the diagonal basis of an arbitrary traceless matrix.
2. A symmetry that suppresses the identity perturbation `a 1`, producing an
   approximately trace-preserving correction.
3. A UV or matching reason why a single-generator hypercharge effect is
   normalized by the full fundamental Casimir `C_F`, rather than by
   `(T_R^3)^2`.

The first two conditions can be engineered with exchange symmetries or doubled
fields.  The third is the hard part.  It is not supplied by custodial symmetry
alone.

## Status

This route is **phenomenological unless supplemented by a UV matching
calculation**.  It makes the matrix structure plausible, but it also sharpens
the central obstruction: `3/8` is a full Casimir ratio, whereas hypercharge is a
single-generator spurion.
