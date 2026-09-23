# Milestone 1 rotor stress test -- 2026-05-25

## Question

Can the boundary rotor candidate supply all of the following at once?

1. diagonal gap `mu^2 j(j+1)`;
2. image channel `q_j in Im A_j`;
3. mixing `mu^2 A_j`;
4. finite `j=0,1/2,1` spectrum;
5. no extra light tower.

## What the second-order rotor gives

For a group-valued boundary field `h(tau) in SU(2)`, the kinetic action

```tex
S_{\rm rot}
={I\over2}\int d\tau\,
\langle h^{-1}D_\tau h,h^{-1}D_\tau h\rangle
```

has Hamiltonian

```tex
H_{\rm rot}={1\over2I}\sum_aR_aR_a.
```

On a spin-`j` sector,

```tex
H_{\rm rot}={J_j\over2I},
\qquad
J_j=j(j+1).
```

Thus the desired diagonal gap follows if

```tex
{1\over2I}=\mu^2.
```

This is a real positive-Casimir mechanism.  It is not the WZW conformal-weight
normalization.

## What it does not give by itself

The same rotor has a Peter-Weyl spectrum:

```tex
L^2(SU(2))=\bigoplus_{j\in{1\over2}Z_{\ge0}}V_j\otimes V_j^*.
```

Therefore it does not exclude `j=3/2` or higher sectors.  It supports the tower
branch, not the finite `SU(2)_2` branch.

It also does not by itself identify the oscillator field with

```tex
Im A_j\subset V_j\otimes R^3.
```

The rotor Hilbert space carries left and right representation labels.  The
Feshbach image channel needs a projected current-vector field:

```tex
q_j=P_j q_j,
\qquad
P_j={1\over J_j}A_jA_j^\dagger.
```

That projection must be supplied by the D8 boundary/current coupling.

Finally, minimal coupling in `D_tau h` produces current couplings and contact
terms.  It does not automatically give the Feshbach vertex

```tex
-\mu^2\langle q_j,A_jp_j\rangle+{\rm h.c.}
```

with no additional contact term in the open channel.

## Finite-branch conflict

The finite branch wants an `SU(2)_2` integrable current sector:

```tex
j=0,{1\over2},1.
```

But direct use of the affine conformal weight gives

```tex
\Delta_j={J_j\over k+2}={J_j\over4}.
```

That is the wrong gap normalization for the de Vries mass equation.  The
finite branch therefore needs an extra conversion:

```tex
{\rm finite}\ SU(2)_2\ {\rm label}
\quad+\quad
{\rm target-space\ zero-mode\ Casimir\ gap}.
```

The current notes supply the zero-mode Casimir algebra, but they do not yet
derive the dynamical conversion from the finite current sector to the rotor
gap.

## Branch decision

The simple second-order rotor passes the Casimir-gap test and fails the
finite-spectrum test.

The finite `SU(2)_2` selector passes the finite-spectrum test and fails the
gap test if one uses `L0` directly.

Thus the project has two possible Milestone 1/2 branches:

1. `rotor tower`: natural `mu^2J_j` gap, possible `j=3/2` state, no finite-set
   prediction;
2. `finite current`: finite photon/W/Z set, no `j=3/2`, but needs a D10
   mechanism converting the current label to the zero-mode Casimir gap.

## Consequence

Milestone 1 cannot be closed by saying "boundary rotor" alone.  A passing local
D10 action must do one of two things:

- project the rotor tower to `j<=1` while preserving the `mu^2J_j` gap; or
- start from the finite `SU(2)_2` sector and derive a target-space zero-mode
  mass operator rather than the conformal-weight operator.

The second option is better aligned with the finite W/Z prediction.  The first
option is the one that keeps the `96.54 GeV` diphoton branch.

Finite-operator update:
`loop/milestone1-finite-zero-mode-image-operator-2026-05-25.md` implements the
second option algebraically.  It keeps the `SU(2)_2` finite set and defines the
closed-channel Hamiltonian as `mu^2 A_jA_j^dagger` on `Im A_j`.  On that image,
`A_jA_j^dagger=J_j`, so the Feshbach denominator is `B+mu^2J_j` without adding
a Peter-Weyl rotor tower.
