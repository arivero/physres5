# Milestone 6 extra-mode mass-gap table -- 2026-05-25

## Question

Milestone 6 requires absence of unwanted light modes on the same branch used for
the W/Z relation.  This note tests the auxiliary image complement, the rotor
tower, the mixed Hom candidate, and generic string/brane excitations.

## Finite image-channel complement

The finite image operator uses

```tex
A_j:V_j\to V_j\otimes{\bf R}^3,
\qquad
A_j^\dagger A_j=J_j{\bf 1}_{V_j}.
```

For `j>0`, `A_j` is injective and

```tex
V_j\otimes{\bf R}^3={\rm Im}\,A_j\oplus({\rm Im}\,A_j)^\perp .
```

On `Im A_j`,

```tex
A_jA_j^\dagger=J_j.
```

On the orthogonal complement,

```tex
A_j^\dagger q_\perp=0,
\qquad
A_jA_j^\dagger q_\perp=0.
```

Thus an unconstrained image field with quadratic operator

```tex
B+\mu^2A_jA_j^\dagger
```

has complement denominator `B`.  The complement is massless, not heavy.  Its
dimension is

```tex
\dim({\rm Im}\,A_j)^\perp=2\dim V_j.
```

The finite branch therefore needs an actual projection

```tex
q_j=P_jq_j,
\qquad
P_j={1\over J_j}A_jA_j^\dagger,
```

or a derived complement mass.  The current D8/Payen source package has not
derived either one.

## Mixed Hom candidate

The mixed Hom field

```tex
y_j\in H^0(CP1,{\rm Hom}(O(0),O(2j)))=V_j
```

maps isometrically to the image:

```tex
Q_j={1\over\sqrt{J_j}}A_jy_j\in{\rm Im}\,A_j.
```

This removes the `({\rm Im}A_j)^\perp` complement from the finite field
content.  However, the current source package does not derive the one-square
Hom action or coefficient lock.  Thus Hom removes the complement problem only
on the same branch that remains compatible rather than predictive.

## Rotor tower

The second-order rotor branch has Peter-Weyl sectors

```tex
j=0,{1\over2},1,{3\over2},2,\ldots .
```

With the de Vries pole and the scale fixed by `M_Z=91.1880 GeV`, the first
states are:

| `j` | `J=j(j+1)` | `M_j` GeV |
|---:|---:|---:|
| `1/2` | `0.75` | `80.3748` |
| `1` | `2` | `91.1880` |
| `3/2` | `3.75` | `96.5388` |
| `2` | `6` | `99.5795` |
| `5/2` | `8.75` | `101.4539` |
| `3` | `12` | `102.6807` |

The higher states are not decoupled.  The tower accumulates below the
large-`j` limit

```tex
M_\infty={M_Z\over\sqrt{X_+(2)}}=106.57{\rm GeV}.
```

Therefore the rotor branch is a light-tower branch, not a finite W/Z branch.

## String and brane oscillator modes

The current article does not compute the open-string oscillator scale,
brane-displacement Hessian, or compactification KK spectrum.  No derived
inequality places those modes above the weak boundary scale.  They remain
uncontrolled for Milestone 6.

## Mass-gap table

| Sector | Current mass statement | Verdict |
|---|---|---|
| finite image field restricted to `Im A_j` | desired denominator `B+mu^2J_j` | algebraic pass |
| unprojected `V_j tensor R^3` complement | denominator `B` on `({\rm Im}A_j)^\perp` | fails |
| added `M_perp` complement | would gap complement if derived and positive | not in current action |
| mixed Hom `y_j` | no image complement, but coefficient lock not derived | compatible only |
| rotor branch | light tower beginning at `96.54 GeV` after Z scaling | finite-branch fail |
| string/brane/KK excitations | no scale inequality computed | not passed |

## Decision

Milestone 6 fails the extra-light-mode check for the current action.  The
finite image branch is safe only if the field is really an `Im A_j` field, as
in the mixed Hom candidate, or if a complement mass is derived.  The written
D8/Payen/RR package does not supply that derivation.  The rotor branch keeps a
light tower and therefore cannot be used as a finite W/Z prediction.
