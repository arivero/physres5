# Stress Tests

These checks are written from the standpoint of a skeptical field-theory
referee.  They separate what is consistent from what is not derived.

## Gauge Invariance

The proposed correction

```text
Delta M_-^2 = kappa (M_Z^2-M_W^2) sigma_3
```

is not itself a gauge-invariant operator until the negative-sector fields are
specified.  A gauge-invariant EFT could contain a custodial-breaking operator
that becomes this mass matrix after electroweak symmetry breaking, but the
fields carrying the `sigma_3` label must be part of the Lagrangian.

Conclusion: gauge invariance is recoverable only after adding a genuine
negative-sector multiplet or interpreting the formula as a post-EWSB mass
matching rule.

## Custodial Symmetry

The factor

```text
M_Z^2-M_W^2 = g'^2 v^2/4
```

has the correct custodial behavior: it vanishes for `g' -> 0`.  This is the
strongest mainstream feature of the proposal.

The original quadratic does not contain `g'` or a custodial-breaking spurion.
Its W/Z split is produced by assigning different spin Casimirs, `C_1` and
`C_1/2`, not by turning on hypercharge.

Conclusion: the correction has a custodial limit; the parent root equation does
not unless a new parameter is introduced.

## Scheme Dependence

`M_Z`, `M_W`, and `m_H` are pole-like experimental inputs.  `v` inferred from
`G_F` includes electroweak radiative corrections in precision fits, while the
simple relation `v=(sqrt(2)G_F)^(-1/2)` is a low-energy convention.  A real EFT
matching calculation must specify pole, on-shell, or running parameters.

Conclusion: the numerical comparison is meaningful as a phenomenological
on-shell relation, but not yet as a renormalization-scheme-independent
prediction.

## Pole vs Running Masses

The algebra uses pole-mass-normalized values.  A Wilson coefficient matched in a
UV theory would usually be computed in a running scheme at a matching scale and
then evolved.  The equality to `3/8` would not generally be invariant under this
procedure unless protected by symmetry.

Conclusion: an exact coefficient claim requires a scheme statement.  None is
present in the current construction.

## Higgs Potential Interpretation

In the Standard Model,

```text
V(H) = -mu^2 H^\dagger H + lambda (H^\dagger H)^2,
m_h^2 = 2 lambda v^2.
```

There is one tachyonic parameter `-mu^2`, not two negative roots.  The proposed
`H_0` can be viewed as a bare tachyonic scale, but `F_0` has no independent SM
Higgs-potential role.

Conclusion: the negative-root sector is not the SM Higgs potential.  It is an
extra spectral ansatz.

## Relation to G_F

The scale

```text
v/sqrt(2) = 1/sqrt(2 sqrt(2) G_F)
```

is a vacuum scale derived from muon decay.  It is not a particle mass.  Matching
`M_F` to `v/sqrt(2)` is therefore a comparison between a spectral mass parameter
and an electroweak vev-derived scale.

Conclusion: the comparison is numerically interesting but needs a Lagrangian
definition of `F` to become a physical mass prediction.

## Actual Custodial Limit of the Parent Equation

A minimal engineered parent is

```text
C_s(chi_Y) = C_0 + chi_Y (C_s^phys - C_0).
```

At `chi_Y=0`, all positive roots are degenerate.  At `chi_Y=1`, the
de Broglie-de Vries values are recovered.  This works algebraically, but `C_0`
and the interpolation are arbitrary.

Conclusion: a custodial-degenerate parent exists only as an added deformation,
not as a consequence of the original quadratic.

## Final Stress-Test Judgment

The proposal passes the spurion-shape test and the trace-preservation test.  It
fails the derivation test at two points:

1. no mainstream Lagrangian supplies the two-state negative-root projector;
2. no mainstream matching calculation fixes `kappa = C_F/C_A = 3/8`.

The result should be described as symmetry-motivated and phenomenological, not
derived.

## Sister-Project Stress Addendum

The sister project added three useful discriminants:

1. A one-parameter parent equation can make the positive roots degenerate only
   by collapsing them to zero.  A non-singular custodial parent needs an added
   `C_*` and a chosen interpolation.
2. The de Vries positive branch factorizes as
   `cos^2(theta_W)^dV = (3/8) F_dyn`; exposing the bare `3/8` would require
   removing the de Broglie dynamical factor, not merely taking a custodial
   limit.
3. The effective de Broglie coupling identity
   `alpha_eff^2(s)=beta_s^2 C_2(s)` is exact, but it is not a Lagrangian
   matching relation.

These are consistent with the final assessment: the algebra is structured and
nontrivial, but the field-theory embedding remains an ansatz.
