# Milestone 6 source branch decision -- 2026-05-25

## Question

The replacement-source equation isolates the minimal lower-charge target

```tex
Q_{\rm new}=-h_Q^2
```

on the balanced opposite-lift endpoint branch.  This note decides whether to
accept that repair inside the present compactification route.

## Options

### Keep the current D8/O8 package

This fails.  Endpoint data, closed `H`, bare K-theory absorption, and the tested
product O4/O6 package do not cancel the lower Bianchi classes.

### Add a standalone anti-D4

A defect on

```tex
M_4\times S^1_Q
```

localized at a point of the `CP2` carrier has the right cohomology class.  It
would cancel the minimal residual charge on the balanced endpoint branch.

It is not a completion of the current route.  It adds a new localized source
with positive tension, an open-string sector, and backreaction not used in the
boundary-current action.  The scalar potential coefficient `B_loc`, the local
mode spectrum, and the backreacted geometry would have to be recomputed from
the enlarged source system.  The de Vries-compatible vacuum data would then no
longer be data of the current D8/O8 compactification.

### Add an O4-only image source

An `O4^-` component has the right charge normalization in the doubled type I'
convention.  The required support is

```tex
{pt}_{CP2}\times S^1_Q.
```

The standard product involutions tested on `CP2 x CP1` do not produce that
support alone.  Holomorphic projective involutions produce an O4 component and
an O6 component; standard complex conjugation gives O6-type support after the
`CP1` fixed circle is included.  An O4-only option therefore requires a
different orientifold or topology.

### Use the product O4/O6 package

This is the natural product-involution enlargement, but it fails the endpoint
lattice.  For `k` identical packages,

```tex
Q_{O4/O6}=-4k h_Q-kh_Q^2.
```

D6 cancellation forces `k` to be a multiple of four, while the balanced
endpoint D4 coefficient is `1 mod 8`.  Unequal endpoint stacks give the
equation `4M^2-3=4M`, which has no integer solution.

### Add generic D6-bearing sources

Any such repair is a new source sector.  It must supply the full vector

```tex
Q_{\rm new}=-16M h_Q-(4M^2-3)h_Q^2
```

on an unequal endpoint branch, or a compatible vector on a changed balanced
branch.  This changes the Bianchi table, localized tension, open sectors, and
potential coefficients.  No such source is selected by the present D10
boundary-current action.

## Decision

The current D8/O8 compactification route is closed as a global proof branch.
The minimal cohomological repair exists as a charge target, but accepting it
requires changing the source content or topology and recomputing the vacuum,
mode spectrum, and backreaction.  Thus the current route remains a coherent
compatibility framework and not a compactification that forces the de Vries
relation.

Any revived source branch must start as a new compactification ansatz with its
own source table, not as a patch to the current D8/O8 package.
