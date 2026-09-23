# Loop and threshold normalization test

## Target size

At tree level in the electroweak theory,

```text
M_Z^2 - M_W^2 = g'^2 v^2 / 4.
```

The proposed negative-sector shift is therefore

```text
epsilon = (3/8)(M_Z^2-M_W^2)
        = (3/32) g'^2 v^2.
```

This is a tree-size hypercharge correction.  It is not loop-size unless a heavy
threshold or strong-sector factor compensates the `16 pi^2` suppression.

## One-loop self-energy estimate

For a perturbative one-loop correction of the schematic form

```text
delta m^2 = A g'^2 C v^2/(16 pi^2),
```

the coefficient relative to the vector splitting is

```text
kappa = delta m^2/(M_Z^2-M_W^2) = A C/(4 pi^2).
```

The required dimensionless finite coefficient is:

```text
C = C_F = 3/4:          A = 2 pi^2  = 19.739...
C = (T_R^3)^2 = 1/4:    A = 6 pi^2  = 59.217...
```

These are too large for an ordinary weakly coupled one-loop self-energy with
`A = O(1)`.  They are possible only as shorthand for a heavy threshold, strong
dynamics, or a tuned matching coefficient.

## Quadratic heavy threshold

For a threshold of the form

```text
delta m^2 = g'^2 C M^2/(16 pi^2)
```

with unit finite coefficient, the target size requires

```text
C = C_F = 3/4:          M/v = sqrt(2 pi^2)  = 4.443...
C = (T_R^3)^2 = 1/4:    M/v = sqrt(6 pi^2)  = 7.695...
```

Numerically this means a threshold near `1.09 TeV` for the full Casimir
normalization or near `1.89 TeV` for the single-generator normalization.  This
is a plausible scale for new physics, but the coefficient and sign remain
model-dependent.  It also introduces a naturalness-sensitive quadratic
threshold rather than a protected prediction.

## D-term cross-check

A tree-level Abelian D term

```text
V_D = g'^2/2 (q_H |H|^2 + q_S |S|^2)^2
```

gives

```text
delta m_S^2 = g'^2 q_H q_S v^2/2,
kappa = delta m_S^2/(M_Z^2-M_W^2) = 2 q_H q_S.
```

With the SM Higgs hypercharge convention `q_H=1/2`, this gives `kappa=q_S`.
The target coefficient would therefore require `q_S=3/8`.

This is not a derivation of `C_F/C_A`; it is a charge assignment.  A pair of
states with charges `+3/8` and `-3/8` could produce a traceless split at tree
level, but it would introduce exotic hypercharged negative-sector fields and
would not leave an electroweak-singlet Fermi-vacuum interpretation intact
without additional structure.

## Status

Ordinary one-loop hypercharge self-energies are too small.  D terms or heavy
thresholds can be made tree-size, but their coefficients are charges or Wilson
coefficients.  This cycle therefore does not produce a mainstream derivation;
it narrows the viable route to a specific UV threshold calculation.
