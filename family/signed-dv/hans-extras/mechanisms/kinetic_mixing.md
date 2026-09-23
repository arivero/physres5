# Hidden-`U(1)` kinetic mixing

## Motivation

The paired D-term boundary model needs an effective charge `q_S=3/8`, which is
not on the ordinary Standard Model, minimal-`SU(5)`, or custodial `T_R^3+X`
charge lattices.  A standard way to generate nonstandard effective charges is
kinetic mixing between two Abelian gauge fields.

The classic reference is Holdom, "Two U(1)'s and epsilon charge shifts,"
Phys. Lett. B 166, 196--198 (1986), doi:10.1016/0370-2693(86)91377-8.

## Effective charge

After diagonalizing kinetic terms, a hidden-sector field can acquire an
effective hypercharge-like coupling of the schematic form

```text
q_eff = q_0 + epsilon (g_X/g_Y) q_X.
```

The scan in `algebra/kinetic_mixing_charge_shift.py` gives:

```text
q_0=0,   q_X=1: epsilon = 3/(8 (g_X/g_Y))
q_0=1/3, q_X=1: epsilon = 1/(24 (g_X/g_Y))
q_0=1/2, q_X=1: epsilon = -1/(8 (g_X/g_Y))
```

Thus kinetic mixing can engineer `q_eff=3/8`.

## Why it does not derive the correction

The price is a new continuous parameter `epsilon`, plus a hidden gauge coupling
and hidden charge normalization.  Unless a UV compactification computes exactly
the required mixing, the `3/8` is still chosen by matching.

This route also shifts the problem away from custodial `SU(2)`: the coefficient
comes from Abelian mixing data, not from the `SU(2)` Casimir ratio `C_F/C_A`.

## Status

Kinetic mixing is mainstream and relevant to string/D-brane UV model building,
but in this project it is a **phenomenological engineering route**, not a
derivation.
