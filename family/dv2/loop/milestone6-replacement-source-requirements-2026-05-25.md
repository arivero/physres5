# Milestone 6 replacement source requirements -- 2026-05-25

## Question

The current D8/O8 package fails source balance.  This note records the algebraic
requirements for any replacement lower-source sector, without assuming a
particular object supplies it.

## General equation

Use the endpoint variables

```tex
N_L+N_R=32,
\qquad
N_i\in\{0,16,32\},
\qquad
M_i\in2{\bf Z}+1.
```

The D8/O8 lower vector is

```tex
Q_6^{\rm end}={N_LM_L+N_RM_R\over2}h_Q,
```

and

```tex
Q_4^{\rm end}
=\left[
{(2M_L^2-1)N_L+(2M_R^2-1)N_R\over16}-1
\right]h_Q^2.
```

Let an added lower-source sector have no D8 charge and contribute

```tex
Q_{\rm new}=\alpha h_Q+\beta h_Q^2.
```

The lower Bianchi equations are

```tex
\alpha=-{N_LM_L+N_RM_R\over2},
```

and

```tex
\beta=
-\left[
{(2M_L^2-1)N_L+(2M_R^2-1)N_R\over16}-1
\right].
```

This is the replacement-source target.

## Endpoint lattice forms

For an unequal endpoint stack, the lower endpoint vector is

```tex
Q_{\rm end}=16M h_Q+(4M^2-3)h_Q^2,
\qquad M\in2{\bf Z}+1.
```

Thus the replacement must be

```tex
Q_{\rm new}=-16M h_Q-(4M^2-3)h_Q^2.
```

For a balanced endpoint stack,

```tex
Q_{\rm end}=8(M_L+M_R)h_Q+(2M_L^2+2M_R^2-3)h_Q^2.
```

Since `M_L+M_R` is even, the D6 entry lies in `16Z h_Q`.

The smallest D6-free target occurs at

```tex
M_R=-M_L,\qquad M_L=\pm1,
```

and is

```tex
Q_{\rm new}=-h_Q^2.
```

Every source replacement that keeps the current endpoint topology must reduce
to one of these charge equations.

## Consequences

1. A pure negative D4 source `-h_Q^2` is the minimal cohomological repair.  It
   requires the balanced opposite-lift endpoint choice.  It is not present in
   the current D8/O8 package.

2. Any replacement with a D6 component must have D6 charge in the endpoint
   lattice `16Z h_Q`, unless additional non-endpoint D6 sources are also
   introduced.

3. The tested O4/O6 package has

```tex
Q_{O4/O6}=-4k h_Q-kh_Q^2.
```

Its D6 entry is compatible with the endpoint lattice only when `k` is a
multiple of four.  Then its D4 entry is also a multiple of four, while the
balanced endpoint D4 coefficient is `1 mod 8`.  Thus this package cannot be
the minimal repair.

4. A standalone anti-D4 or an O4-only image source would match the minimal
   cohomology equation, but it changes the localized tension, open sector,
   backreaction, and scalar potential coefficients.  It is a new compactification
   input, not a consequence of the current source package.

## Decision

Milestone 6 can pass only after a replacement source sector supplies one of the
charge vectors above and the enlarged system is recomputed.  The minimal charge
target is `-h_Q^2`; the current product orientifold route supplies it only with
an O6 companion that fails the endpoint congruences.  Therefore the present
D8/O8 route has no source-balance completion without changing the source
content or topology.
