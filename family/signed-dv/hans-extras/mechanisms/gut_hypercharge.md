# GUT hypercharge normalization

## Temptation

The number `3/8` also appears in grand unification.  In minimal `SU(5)`, the
properly normalized hypercharge generator gives

```text
sin^2(theta_W) = 3/8
```

at the unification scale when the `SU(2)` and normalized `U(1)` gauge couplings
are equal.  This makes it tempting to identify the de Broglie-de Vries
coefficient with GUT hypercharge normalization.

## Calculation

In the fundamental of `SU(5)`,

```text
Y = diag(-1/3,-1/3,-1/3,1/2,1/2),
Tr_5(Y^2) = 5/6.
```

The canonically normalized generator is

```text
T_Y = sqrt(3/5) Y,
Tr_5(T_Y^2)=1/2.
```

Thus

```text
g'^2 = (3/5) g_1^2.
```

At unification, `g_1=g_2`, so

```text
sin^2(theta_W) = g'^2/(g_2^2+g'^2)
               = (3/5)/(1+3/5)
               = 3/8.
```

The proposed mass correction instead uses

```text
epsilon = (C_F/C_A)(M_Z^2-M_W^2)
        = (3/8)(g'^2 v^2/4),
```

where

```text
C_F/C_A = (3/4)/2.
```

These are numerically equal but structurally different:

```text
GUT weak-angle value:      (3/5)/(1+3/5)
SU(2) Casimir ratio:      (3/4)/2
```

## Why it does not derive the correction

GUT normalization fixes how the low-energy hypercharge coupling is embedded
into a unified gauge coupling.  It does not create a two-state negative-root
sector, a `sigma_3` projector, or a finite scalar threshold of size
`(3/8)(M_Z^2-M_W^2)`.

Moreover, the unification value is a high-scale boundary condition.  After
renormalization-group running, the weak-scale on-shell value of the weak mixing
angle is not `3/8`.  The signed-root construction uses weak-scale pole inputs,
so importing a high-scale boundary value would mix schemes and scales unless a
complete running and matching calculation is supplied.

## Status

GUT hypercharge normalization is a useful warning against over-interpreting the
number `3/8`: the same rational can arise from unrelated group-theory
quotients.  It does not provide the desired mainstream derivation.
