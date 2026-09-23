# D5 Lens Weinberg EM Compatibility Criterion

Date: 2026-06-01.

Status: electroweak compatibility constraint from the D5 lens endpoint.  It is retained as a
non-De-Vries constraint compatible with experiment.

## Purpose

The D5 endpoint

```text
S^1 -> M_5(n)=S(O(n)) -> CP^2,
M_5(n) ~= S^5/Z_n
```

is a good place to test electroweak global compatibility.  The lens quotient changes the allowed
circle phases, flat characters, and line-bundle holonomies.  That can constrain how the
unbroken electromagnetic circle sits inside

```text
SU(2)_W x U(1)_Y
```

and how Weinberg's Kaluza-Klein inertia prescription reads the hypercharge generator.

The lens quotient by itself does not set a weak angle.  It can fix the charge lattice and the
period of the `U(1)` generator that enters the inertia calculation.  The angle then comes from
the resulting ratio of normalized inertias.

## Local Source Anchors

The local Weinberg source states that KK gauge couplings are computed from root-mean-square
circumferences or inertias of internal Killing directions.  In the notation of the project:

```text
1/g_X^2 = internal inertia of the Killing direction X.
```

The Hilo synthesis records the raw `CP^2` inertia outcome:

```text
g'/g = 1/sqrt(3),
sin^2(theta_W)=1/4.
```

That number is a rigidity test, not the desired De Vries value.  A lens repair has to change the
hypercharge generator normalization, its allowed period, or the relevant inertia ratio from the
same global geometry.

The Standard Model global-form source records:

```text
G_SM = (SU(3)_C x SU(2)_W x U(1)_Y)/Gamma,
Gamma subset Z_6,
Gamma = 1, Z_2, Z_3, or Z_6.
```

Therefore a D5 `Z_5` lens deck group cannot be directly identified with the Standard Model
center quotient.  It can still act as a Spin^c boundary holonomy, a hypercharge-line datum, or a
finite endpoint character.

## Electromagnetic Compatibility Test

Use the electroweak generator convention

```text
Q_EM = T_3 + Y/2.
```

The Higgs vacuum has to be neutral under `Q_EM`.  On the D5 endpoint, the same generator also
has to exponentiate to a well-defined circle action on the lens quotient and on all coefficient
modules:

```text
exp(2 pi i Q_EM) acts trivially on physical fields,
deck Z_n action preserves the Higgs and matter boundary conditions,
flat characters respect the chosen hypercharge period.
```

In practice this becomes a congruence problem:

```text
Hopf fibre charge + Spin^c line charge + electroweak Y charge
```

has to be integral modulo the deck group and compatible with the global form of `G_SM`.

## Weinberg-Angle Calculation To Run

Let the reduced gauge kinetic terms be

```text
L_kin =
  - (1/4) f_2 F_W^2
  - (1/4) f_Y F_Y^2.
```

Then

```text
g^2=1/f_2,
g'^2=1/f_Y,
sin^2(theta_W)=f_2/(f_2+f_Y).
```

The D5 lens quotient can affect the calculation through:

```text
period of the hypercharge circle,
allowed unit of Y after quotienting,
rms circumference of the fibre generator,
flat-character sector retained at the endpoint,
global gauge-group quotient Gamma.
```

The calculation has to output `f_2` and `f_Y` from normalized generators and the D5/D6/D7 metric
data.  Choosing `n` after the desired angle is known counts as a fit.

## Relation To The Current D5 n=5 Diagnostic

The active D5 diagnostic uses

```text
M_5(5)=S^5/Z_5,
chi_{1,3}(ell)=zeta^ell+zeta^(3 ell),
```

as a balanced finite boundary character in the standard odd spin, flat-twisted round lens
representative.

That `Z_5` has a different job from the Standard Model `Gamma subset Z_6`.  A viable model has
to state one of the following:

```text
Z_5 is only a D5 Spin^c/eta boundary datum, separate from the SM global quotient;
or a map from the D5 boundary character to hypercharge is computed without identifying Z_5
   with Gamma;
or the n=5 branch is deleted from electroweak global-form use.
```

The first option is currently safest: keep `n=5` for the D5 diagnostic and use a separate
electroweak global quotient when computing line operators and `Q_EM`.

## Proargument

The constructive role of the lens quotient is:

```text
D5 lens endpoint
  -> finite phase and flat-character lattice,

Spin^c/hypercharge line
  -> quantized Y periods,

electromagnetic survivor
  -> compatibility congruence for Q_EM,

Weinberg inertia
  -> coupling ratio after generator periods are fixed.
```

This can turn the lens space into a real electroweak constraint.  It is especially valuable if
the same endpoint data also selects the balanced D5 character and preserves the custodial
`rho=1` branch.

## Counterargument

The quotient cannot carry the whole weak-angle explanation by itself.  A finite deck group gives
charge-period data, while the angle depends on kinetic normalization.  A model that keeps the
inertia ratio free has no prediction.  A model that identifies `Z_5` with the Standard Model
center quotient conflicts with the allowed `Gamma subset Z_6` list.

The lens endpoint also cannot replace the De Vries source calculation.  It may constrain
hypercharge, endpoint holonomy, and line operators; it does not compute the retained signed
Hessian.

## Repair Tests

For any D5 lens explanation of the weak angle, record:

```text
n_lens and its geometric role,
Gamma_SM in (SU(3) x SU(2) x U(1))/Gamma_SM,
normalization and period of Y,
definition of Q_EM and proof that the Higgs vacuum is neutral,
flat characters on M_5(n_lens),
Weinberg inertias f_2 and f_Y,
predicted sin^2(theta_W),
line-operator and anomaly/global-form compatibility.
```

Keep the result only if the same geometry fixes the generator periods and the inertia ratio.
If it only supplies a charge lattice, retain it as an electroweak global-form constraint rather
than as an angle prediction.

## Effect On The Active Search

This note keeps a useful non-De-Vries constraint: the D5 lens endpoint can restrict hypercharge
periods and electromagnetic compatibility.  The De Vries route remains unchanged.  The signed
source still has to compute the named operator, response kinetic norm, and relative-gain
Hessian coefficient.
