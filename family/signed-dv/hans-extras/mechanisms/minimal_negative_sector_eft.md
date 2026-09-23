# Minimal Negative-Sector EFT

## Question

What is the cleanest mainstream low-energy operator that could reproduce

```text
Delta M_-^2 = (3/8)(M_Z^2-M_W^2) sigma_3
```

without pretending that the Standard Model already contains the two signed
negative roots?

## Minimal Lagrangian Ansatz

Introduce a real two-component negative-sector field

```text
Psi_- = (psi_H, psi_F)^T
```

and take it to be an electroweak singlet for the minimal test.  The lowest
gauge-invariant scalar operator with explicit hypercharge-spurion dependence is

```text
V_eff contains 1/2 Psi_-^T [
  m_-^2 1 + c_Y g'^2 (H^\dagger H) sigma_3
] Psi_-.
```

After electroweak symmetry breaking, with `<H^\dagger H> = v^2/2`,

```text
Delta M_-^2 = c_Y g'^2 v^2/2 sigma_3.
```

Since

```text
M_Z^2 - M_W^2 = g'^2 v^2/4,
```

the desired correction fixes

```text
c_Y = 3/16.
```

This is a perfectly legal EFT matching relation.  It is not a group-theory
prediction.

## Why This Is the Best Possible EFT Ansatz

It satisfies the requested structural conditions:

1. It vanishes for `g' -> 0`.
2. It is explicitly proportional to the hypercharge/custodial-breaking spurion.
3. It acts only on the negative sector because `Psi_-` was added for that
   purpose.
4. It leaves W/Z pole inputs untouched at tree level.
5. It is trace-preserving because `tr sigma_3 = 0`.

The fifth requested condition fails: the coefficient is `c_Y = 3/16` in this
operator normalization, or equivalently `kappa = 3/8` in the mass formula.  It
is a Wilson coefficient.

## Why Group Theory Does Not Fix `c_Y`

The relevant one-generator quantities are

```text
(T_R^3)^2 on a doublet = 1/4
T_F/C_A = (1/2)/2 = 1/4
Y_H^2/2 = 1/8
```

depending on normalization and whether one is discussing a trace, a component
eigenvalue, or a D-term coefficient.  The target coefficient of `g'^2 v^2` is

```text
(3/8)(1/4) = 3/32.
```

This is `3/4` of the MSSM-like hypercharge D-term coefficient `1/8`, and it is
not selected by a standard single-generator trace.

## Referee Assessment

This is the cleanest mainstream embedding found so far.  It should be described
as an EFT parameterization:

```text
allowed: yes
derived: no
status: symmetry-motivated phenomenological ansatz
```

A skeptical referee would ask what `Psi_-` is physically and why the Wilson
coefficient is `3/16`.  Without a UV matching calculation, those are assumptions.
