# Milestone 1 `q_j` oscillator coefficient lock -- 2026-05-25

## Aim

After the connected/1PI Wilson test, the finite branch reduces to the local
`q_j` oscillator.  This note asks which coefficient relation the oscillator
must satisfy.

## General local oscillator

Use a canonically normalized image-channel field

```tex
Q_j\in{\rm Im}\,A_j.
```

The most general single-pole quadratic form with the same tensor structure is

```tex
S_j^{(2)}
=\langle p_j,Bp_j\rangle
+\langle Q_j,(B+\alpha\mu^2A_jA_j^\dagger)Q_j\rangle
-\gamma\mu^2\langle Q_j,A_jp_j\rangle
-\gamma\mu^2\langle A_jp_j,Q_j\rangle,
```

with positive `alpha` and real `gamma`.  Eliminating `Q_j` gives

```tex
\Gamma_j(B)
=B-\gamma^2\mu^4
A_j^\dagger(B+\alpha\mu^2A_jA_j^\dagger)^{-1}A_j.
```

On `Im A_j`,

```tex
\Gamma_j(B)
=B-{\gamma^2\mu^4J_j\over B+\alpha\mu^2J_j}.
```

Set the physical common scale by

```tex
\mu_{\rm eff}^2=\alpha\mu^2,
\qquad
X={B\over\mu_{\rm eff}^2}.
```

The pole equation is then

```tex
X={r^2J_j\over X+J_j},
\qquad
r={\gamma\over\alpha}.
```

Thus a generic local oscillator leaves a dimensionless residue ratio `r`.
The de Vries pole requires

```tex
r=1,
\qquad \hbox{equivalently}\qquad \gamma=\alpha.
```

A common positive value of `alpha=gamma` only changes the common scale
`\mu_{\rm eff}`; it does not change the W/Z ratio.

## Single-square completion

The local current-displacement square

```tex
\alpha\mu^2\|A_j^\dagger Q_j-p_j\|^2
-\alpha\mu^2\|p_j\|^2
```

expands to

```tex
\alpha\mu^2\langle Q_j,A_jA_j^\dagger Q_j\rangle
-\alpha\mu^2\langle Q_j,A_jp_j\rangle
-\alpha\mu^2\langle A_jp_j,Q_j\rangle.
```

Therefore a single-square local completion forces

```tex
\gamma=\alpha.
```

It supplies the coefficient lock required by the de Vries pole after the common
scale is renamed.

## Noncanonical kinetic normalization

If the original field has kinetic coefficient `Z_q>0`,

```tex
\langle q_j,Z_qBq_j\rangle
+c_m\mu^2\langle q_j,A_jA_j^\dagger q_j\rangle
-c_g\mu^2\langle q_j,A_jp_j\rangle
-c_g\mu^2\langle A_jp_j,q_j\rangle,
```

then the canonical field `Q_j=Z_q^{1/2}q_j` gives

```tex
\alpha={c_m\over Z_q},
\qquad
\gamma={c_g\over Z_q^{1/2}}.
```

The de Vries condition is

```tex
{c_g\over Z_q^{1/2}}={c_m\over Z_q}.
```

Equivalently,

```tex
c_m=c_g Z_q^{1/2}.
```

This is the field-normalization invariant form of the coefficient lock.

## Decision

The finite branch now has a concrete local pass condition:

```text
the D10 boundary action must generate q_j through one current-displacement
square, or through another mechanism that enforces gamma=alpha.
```

If the boundary dynamics generate a generic oscillator with `gamma/alpha != 1`,
the weak-angle relation is shifted.  If they generate the single-square
completion, Milestone 1 reduces to proving that this `q_j` is the first
positive image-current pole and that competing poles are heavier or projected
out.
