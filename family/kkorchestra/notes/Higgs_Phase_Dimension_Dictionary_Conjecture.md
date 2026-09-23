# Higgs Phase Dimension Dictionary Conjecture

Date: 2026-06-01.

Status: conjectural non-DeVries phase dictionary for the KK Higgs branch.

## Purpose

The proposed dictionary relates the Higgs potential phase to the low-dimensional and
CP2/Aloff-Wallach ladders:

```text
D3 / D7: symmetric carrier with four equal-mass scalar components,
D2 / D6: selected broken/axis branch,
D1 / D5: phase or boundary limit after the radial variable decouples.
```

This note records the idea as a testable branch-selection picture.  It does not supply a De Vries
spectral relation.

## D3 Prototype

Start with a single electroweak doublet

```text
H in C^2 ~= R^4.
```

### Symmetric branch

If

```text
V(H)=m^2 H^dagger H + lambda (H^dagger H)^2 + ...,
m^2>0,
```

then

```text
<H>=0,
Hess_H V=m^2 Id_{R^4}.
```

The four real scalar components are degenerate.  There is no vacuum radius and no electroweak
mass relation.

### Finite broken branch

If

```text
m^2<0,
lambda>0,
```

then

```text
|H|=v/sqrt(2),
v^2=-m^2/lambda.
```

The fixed-radius vacuum orbit is

```text
S^3 subset C^2.
```

The Hopf quotient gives

```text
S^1 -> S^3 -> CP^1 ~= S^2.
```

Thus the D2 object is naturally the projective/axis data after quotienting the phase of the
finite-radius broken branch.  The scalar spectrum has one radial mode and three Goldstone
directions before gauge fixing.

### Phase-only or boundary limit

The D1 circle can arise from a phase-only limit.  In field-theory language, the clean limit is
usually radial decoupling:

```text
m_h^2=2 lambda v^2 -> infinity with v fixed,
```

so only angular/phase data remain at low energy.  Sending `v` itself to infinity decouples the
broken vector and scalar masses as well; that limit can define an asymptotic boundary or
projective description, but finite-energy observables need rescaling.

## D7/D6/D5 CP2/Aloff-Wallach Version

The D7 carrier contains the horizontal four-block

```text
m_3 ~= C^2 ~= R^4
```

inside

```text
SO(3) -> X_{1,1} -> CP^2.
```

### D7 symmetric carrier

If the D7 or D6/D7 effective potential returns

```text
m_3,eff^2>0,
```

then

```text
<H>=0,
Hess_H V=m_3,eff^2 Id_{m_3}.
```

The four `m_3` scalars are degenerate by `U(2)` equivariance.  The branch contains visible scalar
doublet interactions, but no vacuum radius and no `rho=1` mass test.

### D6 selected broken or axis branch

The D6 flag phase

```text
S^2 -> Y_6=SU(3)/T^2 -> CP^2
```

can encode axis/projective data in the same way that `CP^1` records a line in the D3 prototype.
It can also host branch or defect terms from

```text
CP^2 -> S^4,
branch locus RP^2.
```

For the conjecture, the D6 role is to compute or mediate the sign change

```text
m_3,eff^2<0,
<Phi_0>=0,
```

and to preserve the isotropic metric on `m_3`.  Under those outputs, the D6 phase selects the
finite broken doublet branch and the ordinary custodial result

```text
rho=1.
```

### D5 phase or boundary limit

The D5 endpoint

```text
M_5(n)=S(O(n)) -> CP^2
```

is a circle-bundle object.  It is naturally read as phase, boundary, flat-character, or eta data.
The analogy with the D1 phase-only limit is:

```text
radial/amplitude data decouple,
circle or endpoint character remains.
```

A literal `v -> infinity` limit gives a decoupling regime rather than an ordinary finite-energy
Higgs phase.  A smoother low-energy limit keeps the angular/boundary data while the radial mode
is heavy or removed by boundary conditions.

## Testable Content

The conjecture becomes useful only after a source action calculates:

```text
m_3,eff^2 on D7 and D6,
lambda_3,
<Phi_0>,
the D6 branch/defect correction to m_3,eff^2,
the D5 boundary or flat-character limit,
the fate of W/Z masses under any large-v or radial-decoupling limit.
```

The branch classification is:

```text
m_3,eff^2>0:
  symmetric D7/D3 doublet, four equal-mass real scalars.

m_3,eff^2<0 and <Phi_0>=0:
  selected D6/D2 broken/projective branch, one radial scalar plus three Goldstone directions.

radial decoupling or boundary limit:
  D5/D1 phase data, eta/flat-character data, or low-energy angular sector.
```

## Dual Limit: Vacuum To Zero

There is a complementary reading of the dimension change:

```text
v finite:
  radius fixed or projective/axis data selected.

v -> 0:
  the amplitude coordinate is released,
  the symmetric carrier reappears,
  the system grows the direction lost by fixing the radius or quotient data.
```

In the D3 prototype, the finite broken branch uses the fixed-radius orbit

```text
|H|=v/sqrt(2),
S^3 subset C^2.
```

As `v` tends to zero, the orbit collapses as a vacuum manifold, but the quadratic fluctuation
space around the origin is the full linear doublet space

```text
C^2 ~= R^4.
```

Thus the symmetric phase can be read as the restoration of the amplitude direction in field
space, even though the vacuum set itself is the origin.

In the CP2/Aloff-Wallach ladder, the analogous statement is:

```text
D6/D2:
  selected finite branch, axis/projective data, or quotient description.

D7/D3:
  restored carrier with the full m_3 doublet fluctuation block.
```

This gives a useful slogan for the branch tests:

```text
v -> 0 restores the extra carrier direction,
radial decoupling or boundary projection leads toward the D5/D1 phase data.
```

The source action still decides which limit exists.  A positive `m_3,eff^2` gives the symmetric
origin; a negative `m_3,eff^2` gives a finite radius; a radial-decoupling or boundary limit gives
the phase/endpoint description.

## De Vries Separation

This phase dictionary supplies constraints on the bosonic branch and on which KK limit is being
used.  It does not compute the De Vries retained-response data:

```text
P,
mu_r,
alpha,
beta,
gamma(u)^2,
sigma_r^can.
```

The De Vries route can use the dictionary only after the source action fixes the branch and the
normalization data.
