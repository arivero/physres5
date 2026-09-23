# D10 Boundary Schur de Vries Block

## Purpose

This note gives the minimal action-level mechanism that produces the
de Vries two-channel block after projection to a fixed `SU(2)` sector.

It uses one first-order interface operator:

```tex
A_j,
```

and one auxiliary/normal channel. The central rule is:

```text
the same operator that gives the tangent-normal mixing also gives the
normal-channel quadratic term.
```

That rule is what fixes the Regge-compatible relation:

```tex
b=a^2.
```

The exact de Vries point is the canonical normalization:

```tex
a=1.
```

## Setup

Let:

```tex
V_j
```

be the `SU(2)` representation sector produced by the D10 `CP1`
line-bundle interface:

```tex
V_j \simeq H^0(CP1,O(2j)).
```

Let `A_j` be a first-order current, boundary, or brane-interface map
such that:

```tex
A_j^\dagger A_j=C_2(j)\,{\bf 1}_{V_j},
```

with:

```tex
C_2(j)=J=j(j+1).
```

For a normalized tangent mode:

```tex
|t_j\rangle\in V_j,
\qquad
\langle t_j,t_j\rangle=1,
```

define the normalized normal/auxiliary mode:

```tex
|n_j\rangle={1\over\sqrt J}A_j|t_j\rangle,
\qquad
J>0.
```

Then:

```tex
\langle n_j,n_j\rangle=1,
```

and:

```tex
\langle n_j,A_jt_j\rangle=\sqrt J.
```

The `j=0` sector is special: `J=0`, the mixing vanishes, and it is the
photon/zero slot.

## Minimal Quadratic Form

Use the dimensionless quadratic interface Hessian:

```tex
{\cal H}_j(a)
=
\begin{pmatrix}
0 & aA_j^\dagger\\
aA_j & -a^2 A_jA_j^\dagger
\end{pmatrix}.
```

Here `a` is the remaining interface normalization. Project to the
two-dimensional subspace:

```tex
{\rm span}\{|t_j\rangle,|n_j\rangle\}.
```

The projected matrix is:

```tex
\Pi_j{\cal H}_j(a)\Pi_j
=
\begin{pmatrix}
0&a\sqrt J\\
a\sqrt J&-a^2J
\end{pmatrix}.
```

Therefore:

```tex
b=a^2.
```

This is the Regge-priority locus already identified in
[moduli-space-triage.md](moduli-space-triage.md).

If the interface normalization is canonical:

```tex
a=1,
```

then:

```tex
\Pi_j{\cal H}_j(1)\Pi_j
=
\begin{pmatrix}
0&\sqrt J\\
\sqrt J&-J
\end{pmatrix}.
```

This is the de Vries block.

## Schur-Complement Form

At spectral parameter `lambda`, the determinant condition is:

```tex
\det
\begin{pmatrix}
-\lambda&a\sqrt J\\
a\sqrt J&-a^2J-\lambda
\end{pmatrix}
=0.
```

Equivalently:

```tex
\lambda
=
{a^2J\over a^2J+\lambda}.
```

For `a=1`:

```tex
\lambda={J\over J+\lambda},
```

so:

```tex
\lambda^2+J\lambda-J=0.
```

This is the one-pole boundary resolvent form already identified in
[k6-operator-derivation.md](k6-operator-derivation.md).

## Why This Is Better Than Inserting -J

The negative diagonal is tied to the operator:

```tex
-A_jA_j^\dagger.
```

Thus the trace and determinant are controlled by the same first-order
operator that controls the off-diagonal term.

The open-string boundary route supplies the tensor structure. The
boundary Wilson expansion gives the zero-mode charge insertion:

```tex
{\delta W\over\delta\xi^a}\bigg|_{\xi=0}
\propto T_a,
```

and the charge-bilinear insertion:

```tex
{\delta^2 W\over\delta\xi^a\delta\xi^b}\bigg|_{\xi=0}
\propto T_{\partial\Sigma}(T_aT_b).
```

With boundary fluctuation `A_tau=mu xi^a T_a`, the first two tensors carry

```tex
i\mu T_a,
\qquad
-\mu^2T_aT_b.
```

Thus a rescaling `A_j -> a A_j` sends the image bilinear to
`a^2 A_jA_j^dagger`. The Payen exponential fixes the tensor relation:

```tex
b=a^2.
```

In the orthonormal current frame, after factoring out the common physical
scale `mu_*^2`, the dimensionless boundary tensor has `a=1`.

After contraction with the image field `n=n^a e_a`, the bilinear is:

```tex
\left\|A_j^\dagger n\right\|^2
=
\langle n,A_jA_j^\dagger n\rangle.
```

Status: the source-backed boundary action supplies `A_j`, the image tensor,
and the coefficient relation `b=a^2`. Requirement: derive the local
off-shell completion and the physical scale:

```tex
-\mu^2\langle n,A_jA_j^\dagger n\rangle.
```

## Local Auxiliary Completion

The required sign has a precise Schur-complement realization. Introduce
one local auxiliary boundary field:

```tex
y\in V_j.
```

Use the quadratic local form:

```tex
S_{\rm loc}^{(2)}
=
\mu^2
\left[
\langle t,t\rangle
+\langle y,y\rangle
+\langle y,t-A_j^\dagger n\rangle
+\langle t-A_j^\dagger n,y\rangle
\right].
```

Completing the square gives:

```tex
S_{\rm loc}^{(2)}
=
\mu^2
\left[
\langle y+t-A_j^\dagger n,\,
y+t-A_j^\dagger n\rangle
+\langle t,t\rangle
-\langle t-A_j^\dagger n,\,
t-A_j^\dagger n\rangle
\right].
```

Eliminating `y` gives:

```tex
S_{\rm eff}^{(2)}
=
\mu^2
\left[
\langle t,A_j^\dagger n\rangle
+\langle n,A_jt\rangle
-\langle n,A_jA_j^\dagger n\rangle
\right].
```

Thus the de Vries image term is a standard local Schur complement from
a positive auxiliary channel. The canonical coefficient requires the
same `mu^2` multiplying:

```tex
\langle y,y\rangle,
\qquad
\langle y,t-A_j^\dagger n\rangle+\hbox{h.c.},
\qquad
\langle t,t\rangle.
```

Open D10 gate:

```text
identify y as a boundary, brane, branch-defect, BRST, or finite
auxiliary field and derive the equal local coefficients from the
selected D10 action.
```

## D8/Chan-Paton Origin Candidate For y

The D8-like boundary candidate carries Chan-Paton data on:

```tex
\Gamma_{\rm EW}=M_4\times CP2\times S^1_Q.
```

Before the D9 projection, the weak line sectors are:

```tex
O(0),
\qquad
O(2j),
\qquad
j=0,{1\over2},1.
```

The mixed boundary-changing sector between these two Chan-Paton lines
has zero-mode space:

```tex
H^0(CP1,{\rm Hom}(O(0),O(2j)))
=
H^0(CP1,O(2j))
=
V_j.
```

This is the correct representation space for:

```tex
y\in V_j.
```

The Payen boundary action supplies the finite representation and the
Wilson-loop tensors:

```tex
A_j,
\qquad
A_jA_j^\dagger.
```

The D8 WZ skeleton supplies the same boundary sector as a RR source:

```tex
S_{\rm WZ}
=
\mu_8
\int_{\Gamma_{\rm EW}}
C\wedge{\rm ch}(E_Q)
\sqrt{{\hat A(T\Gamma_{\rm EW})\over\hat A(N\Gamma_{\rm EW})}}.
```

The CP2 spin-c completion shifts the boundary WZ curvature by:

```tex
6h_Q\mapsto 6h_Q+{x\over2},
\qquad
x=(2m+1)h_Q.
```

For `m=0`, the doubled determinant class is:

```tex
13h_Q=(P+Q)h_Q.
```

This changes the RR charge/tadpole vector, while the CP1
boundary-changing zero-mode space remains:

```tex
H^0(CP1,{\rm Hom}(O(0),O(2j)))=V_j.
```

Status:

```text
source-backed open-string/Chan-Paton placement plus internal-conjecture
auxiliary identification. The remaining derivation is the local
off-shell boundary action whose quadratic completion gives y with the
same coefficient as the Wilson-loop A_j coupling.
```

If the interface normalization changes:

```tex
A_j\to aA_j,
```

then both entries change coherently:

```tex
\sqrt J\to a\sqrt J,
\qquad
J\to a^2J.
```

This gives the one-operator coefficient relation:

```tex
a^2=b,
```

## Relation To The CP1 Line-Bundle Interface

The current D10 weak Hilbert space is:

```tex
H^0(CP1,O(0))
\oplus
H^0(CP1,O(1))
\oplus
H^0(CP1,O(2)).
```

This gives:

```tex
j=0,{1\over2},1.
```

The block above acts at fixed `j`. It therefore gives:

```tex
j=0:
\quad
\begin{pmatrix}
0&0\\
0&0
\end{pmatrix},
```

```tex
j={1\over2}:
\quad
\begin{pmatrix}
0&\sqrt{3/4}\\
\sqrt{3/4}&-3/4
\end{pmatrix},
```

and:

```tex
j=1:
\quad
\begin{pmatrix}
0&\sqrt2\\
\sqrt2&-2
\end{pmatrix}.
```

These are the photon, `W`, and `Z` de Vries slots in the internal
interface interpretation.

## Physical Interpretation

The normal channel is an auxiliary/order-parameter/interface channel
before the D9 boundary condition is imposed.

Possible realizations of `A_j`:

- a boundary supercharge in the brane/current sector;
- a Dirac or Dolbeault operator on the `CP1` line-bundle sector;
- a current-algebra zero mode whose square is the `SU(2)` Casimir;
- a Schur complement from integrating out a brane-localized auxiliary
  multiplet.

A ranked operator comparison is recorded in
[d10-aj-operator-candidates.md](d10-aj-operator-candidates.md). The
current working choice is:

```tex
A_j=\sum_{a=1}^3T_a^{(j)}\otimes e_a,
```

with:

```tex
A_j^\dagger A_j=j(j+1){\bf 1}_{V_j}.
```

The action-level realization gate is recorded in
[d10-current-schur-action-gate.md](d10-current-schur-action-gate.md).
It makes explicit that the two-channel block lives on:

```tex
V_j\oplus{\rm Im}\,A_j,
```

with a separate decoupling gate for `Ker A_j^\dagger`.

## Pass/Fail Gate

Pass requires:

1. Identify the concrete D10 operator `A_j`.
2. Prove:

```tex
A_j^\dagger A_j=j(j+1)
```

on `O(0)`, `O(1)`, and `O(2)` sectors.

3. Show the normal channel quadratic term is:

```tex
-A_jA_j^\dagger,
```

as an action-level term tied to the same operator.

4. Show the interface normalization is canonical:

```tex
a=1.
```

5. Keep the `O(1)` boundary-changing field `Q`-neutral.
6. Compute `r/n`, `rho_*`, and `L_Q` from the same brane/current/flux
   data.

Fail if:

- the off-diagonal and negative diagonal have independent coefficients;
- the block is inserted after selecting the states;
- the normal channel lacks stabilization or boundary interpretation;
- `a=1` is chosen by convention after comparing to the de Vries number.

## Current Verdict

This note closes the algebraic shape of the de Vries block:

```text
one first-order operator + its own auxiliary Schur term
  -> b=a^2,
canonical normalization
  -> a=b=1.
```

Open physical-model gates: derive `A_j`, its normalization, `r/n`,
`rho_*`, and the surviving `Q` coupling from the selected D10
brane/current/flux interface.
