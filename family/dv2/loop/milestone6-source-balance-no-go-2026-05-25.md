# Milestone 6 source-balance no-go -- 2026-05-25

## Scope

This note consolidates the source-balance tests for the current D8/O8 boundary
route.  It does not exclude all possible compactifications.  It tests the
package actually used in the D10 boundary construction:

- D8/O8 type I' endpoints on `M4 x CP2 x S1_Q`;
- total D8 stack `N_L+N_R=32`, with `N_i in {0,16,32}`;
- spin-c endpoint lifts `M_i=2m_i+13 in 2Z+1`;
- closed `H` on the selected product or flag topology, with no NS5 source;
- ordinary rational WZ/K-theory charge detection on torsion-free even
  cohomology;
- the product O4/O6 involution package tested in the O4 notes;
- no additional anti-D4, D6, NS5, or unrelated defect source.

## Endpoint-only obstruction

The endpoint lower sources are

```tex
Q_6={N_LM_L+N_RM_R\over2}h_Q
```

and

```tex
Q_4=
\left[
{(2M_L^2-1)N_L+(2M_R^2-1)N_R\over16}-1
\right]h_Q^2 .
```

If the endpoint stack is unequal, then

```tex
Q_6=16M_i h_Q,
```

which cannot vanish because `M_i` is odd.

If the endpoint stack is balanced, then

```tex
Q_6=8(M_L+M_R)h_Q.
```

D6 cancellation forces `M_R=-M_L`.  The D4 source becomes

```tex
Q_4=(4M_L^2-3)h_Q^2.
```

For odd `M_L`, this is at least `h_Q^2`, and never zero.

## Flux and K-theory routes

The selected product and flag spaces have only even cohomology:

```tex
H^3=H^5=0.
```

With no NS5 source, closed `H` has no cohomology class, so `HF_0` and `HF_2`
cannot cancel the lower D8/O8 sources.

The same spaces have torsion-free even cohomology, so the rational Chern
character detects the nonzero `h_Q` and `h_Q^2` lower entries.  A bare
K-theory identification cannot set this rational lower vector to zero.

## Product O4/O6 route

The tested holomorphic product involution contributes

```tex
Q_{O4/O6}=-4k h_Q-kh_Q^2
```

for `k` identical packages.  D6 cancellation requires

```tex
Q_6^{D8}=4k h_Q.
```

For all allowed endpoint distributions, `Q_6^{D8}` lies in `16Z h_Q`, so `k`
must be a multiple of four.

In the balanced endpoint case the D4 coefficient is

```tex
2M_L^2+2M_R^2-3.
```

For odd `M_L,M_R`, this is `1 mod 8`, while `k` is `0 mod 4`.  The D4 equation
cannot hold.

In an unequal endpoint case, D6 cancellation gives `k=4M_i`.  The D4 equation
would be

```tex
4M_i^2-3=4M_i,
```

which has no integer solution.

Therefore the product O4/O6 route cannot close the source table.

## Decision

Within the scoped D8/O8 boundary package, Milestone 6 fails at global source
balance.  The local checks still pass, but the Bianchi/tadpole system has no
solution using the endpoint data, closed `H`, bare K-theory absorption, or the
tested product O4/O6 enlargement.

To pass Milestone 6, the project would have to add a different localized source
mechanism and recompute the source table, potential coefficients, and
backreaction.  Without that enlargement, the D10 boundary-current construction
is a compatibility framework rather than a global compactification proof.
