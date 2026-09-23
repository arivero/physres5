# Milestone 1 Wilson-contact residue calculation -- 2026-05-25

## Setup

Let

```tex
A_j:V_j\to V_j\otimes{\bf R}^3,
\qquad
A_jp=\sum_a T_a^{(j)}p\otimes e_a,
\qquad
A_j^\dagger A_j=J_j{\bf 1}_{V_j}.
```

For `j>0`, `A_j` is injective and the image projector is

```tex
P_j={1\over J_j}A_jA_j^\dagger.
```

On `Im A_j`,

```tex
A_jA_j^\dagger=J_j{\bf 1}_{\operatorname{Im}A_j}.
```

The desired static part of the finite image-channel action is

```tex
S_{\rm stat}
=\mu^2J_j\|q_j\|^2
-\mu^2\langle q_j,A_jp_j\rangle
-\mu^2\langle A_jp_j,q_j\rangle,
\qquad q_j\in\operatorname{Im}A_j.
```

## Contact fixed by completing the square

Completing the square in the image metric gives

```tex
S_{\rm stat}
=\mu^2J_j\left\|q_j-{A_jp_j\over J_j}\right\|^2
-\mu^2\|p_j\|^2.
```

Equivalently,

```tex
\mu^2\|A_j^\dagger q_j-p_j\|^2
=S_{\rm stat}+\mu^2\|p_j\|^2.
```

Therefore the finite image-channel kernel requires the open-channel contact

```tex
C_{\rm req}=-\mu^2{\bf 1}_{V_j}.
```

This condition is independent of `j`.

## Raw Wilson second variation

In the orthonormal current frame used for the canonical current metric,

```tex
{\delta^2W_j\over\delta\xi^a\delta\xi^b}\bigg|_{\xi=0}
\sim -\mu^2T_a^{(j)}T_b^{(j)}.
```

Contracting with `delta^{ab}` gives

```tex
C_{\rm Wilson}
=-\mu^2\sum_aT_a^{(j)}T_a^{(j)}
=-\mu^2A_j^\dagger A_j
=-\mu^2J_j{\bf 1}_{V_j}.
```

The image projection does not change this coefficient:

```tex
A_j^\dagger P_j A_j
=A_j^\dagger A_j
=J_j{\bf 1}_{V_j}.
```

Thus the bare Wilson second variation has residue

```tex
\kappa_j=J_j,
```

not the unit residue required by the finite Feshbach pole.

## Inverse image metric residue

The unit contact is obtained by inserting the inverse image metric on
`Im A_j`:

```tex
-\mu^2A_j^\dagger
\left(A_jA_j^\dagger|_{\operatorname{Im}A_j}\right)^{-1}
A_j
=-\mu^2{1\over J_j}A_j^\dagger A_j
=-\mu^2{\bf 1}_{V_j}.
```

The inverse image metric can arise as the static Schur complement of a retained
local image oscillator.  It does not have to be inserted as a microscopic
nonlocal operator if the `q_j` field is present.  Ordinary Wilson Taylor
expansion plus projection gives a shifted kernel only when the raw `T_aT_b`
term is also used as a direct 1PI `p_j` contact.

## Shifted kernel without the inverse image metric

With Wilson residue `kappa_j=J_j`, the finite image-channel kernel is

```tex
\Gamma_j(B)
=B+\mu^2(1-J_j)
-{\mu^4J_j\over B+\mu^2J_j}.
```

The pole equation in `X=B/\mu^2` becomes

```tex
X+1-J_j-{J_j\over X+J_j}=0.
```

This is not the de Vries fixed-point equation except at accidental values of
`J_j`.

For the two weak slots:

```tex
J_{1/2}=3/4:\qquad
X+{1\over4}-{3/4\over X+3/4}=0,
```

```tex
J_1=2:\qquad
X-1-{2\over X+2}=0.
```

Thus the raw Wilson contact changes both W and Z slots and cannot be absorbed
into one common scale.

## Decision

The finite image-channel branch now has a sharper status:

- the required contact is fixed algebraically as `-\mu^2`;
- the raw Wilson second variation gives `-\mu^2J_j`;
- projection to `Im A_j` does not remove the factor `J_j`;
- an inverse image metric gives the required unit residue;
- that inverse is the static propagator of the retained `q_j` field.

Therefore the ordinary Wilson contact does not by itself derive the finite
Feshbach kernel.  The branch remains viable only if the retained-field 1PI
boundary action has the `q_j` oscillator and does not also add the raw Wilson
`T_aT_b` term as a direct `p_j` contact.
