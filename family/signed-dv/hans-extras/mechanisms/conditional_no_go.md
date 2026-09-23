# Conditional no-go statement

This is not a mathematical theorem about all possible UV completions.  It is a
field-theory no-go statement under the mainstream assumptions used throughout
the project.

## Assumptions

1. The low-energy electroweak theory has the Standard Model gauge group and
   the usual Higgs hypercharge normalization.
2. Custodial breaking is organized by the hypercharge spurion that gauges the
   single generator `T_R^3`.
3. New negative-sector fields, if present, are ordinary low-energy fields with
   charges or Wilson coefficients fixed by the Lagrangian.
4. The positive W/Z pole branch is held fixed by using pole masses as inputs.
5. No exotic charge lattice, hidden confinement sector, or specially tuned
   threshold coefficient is introduced solely to reproduce `3/8`.

## Claim

Under these assumptions, a mainstream custodial EFT can justify

```text
Delta M_-^2 = kappa (M_Z^2-M_W^2) sigma_3
```

as the leading trace-preserving hypercharge/custodial-breaking ansatz for an
assumed two-state negative sector.  It cannot predict

```text
kappa = C_F/C_A = 3/8
```

without an additional matching assumption.

## Reason

The electroweak vector splitting is

```text
M_Z^2 - M_W^2 = g'^2 v^2/4.
```

The spurion responsible for this splitting is the gauged generator `T_R^3`.
At order `g'^2`, group factors available directly from that spurion are
single-generator factors such as

```text
(T_R^3)^2 = 1/4       in a fundamental,
Tr_F[(T^3)^2]/Tr_adj[(T^3)^2] = 1/4.
```

The target coefficient uses the full `SU(2)` Casimir ratio

```text
C_F/C_A = (3/4)/2 = 3/8,
```

which sums over all three custodial generators.  That sum is incompatible with
using a single-generator spurion as the source of custodial breaking unless a
UV threshold calculation supplies an extra coefficient.

## Boundary cases

The minimal negative-sector EFT realizes the operator with

```text
c_Y = 3/16.
```

The paired D-term model realizes the operator with

```text
q_S = 3/8.
```

Both are valid ways to write a Lagrangian or EFT, but neither predicts the
coefficient.  The second option also requires exotic hypercharge outside the
ordinary `1/6` Standard Model/minimal-`SU(5)` lattice.

## Conclusion

The signed de Broglie-de Vries correction is best classified as:

```text
exact algebra + symmetry-motivated operator + phenomenological coefficient.
```

It is not a derived mainstream custodial field-theory prediction under the
assumptions above.
