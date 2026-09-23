# D10 Current Schur Action Gate

## Purpose

This note writes the next action-level gate for the working operator:

```tex
A_j=\sum_{a=1}^3T_a^{(j)}\otimes e_a.
```

The algebraic identity is already fixed:

```tex
A_j^\dagger A_j=j(j+1){\bf 1}_{V_j}.
```

The current task is to realize the Schur Hessian with canonical
coefficient:

```tex
a=1.
```

## Current-Algebra Normalization

Use an `SU(2)_2` current sector in the D10 interface. The zero modes act
on a primary sector `V_j` as ordinary `SU(2)` generators:

```tex
J^a_0|_{V_j}=T_a^{(j)}.
```

The allowed integrable sectors at level `k=2` are:

```tex
j=0,{1\over2},1.
```

With the standard generator normalization:

```tex
[T_a,T_b]=i\epsilon_{abc}T_c,
\qquad
\sum_aT_aT_a=j(j+1){\bf 1}_{V_j}.
```

This gives the working map:

```tex
A_j:V_j\to W_j,
\qquad
W_j=V_j\otimes{\mathbb R}^3,
```

```tex
A_j|t\rangle=\sum_aT_a^{(j)}|t\rangle\otimes e_a.
```

## Image Projection

For `j>0`, `A_j` is injective because:

```tex
A_j^\dagger A_j=j(j+1){\bf 1}_{V_j}.
```

Thus:

```tex
{\rm dim}\,{\rm Im}\,A_j={\rm dim}\,V_j.
```

The de Vries two-channel block is the projection to:

```tex
V_j\oplus{\rm Im}\,A_j.
```

Define the projector on the auxiliary image:

```tex
P_j={1\over J}A_jA_j^\dagger,
\qquad
J=j(j+1),
\qquad
j>0.
```

Then:

```tex
P_j^2=P_j,
\qquad
P_jW_j={\rm Im}\,A_j.
```

The `j=0` sector is handled as the zero/massless slot:

```tex
J=0,
\qquad
A_0=0.
```

## Quadratic Boundary/Current Hessian

Let:

```tex
t\in V_j,
\qquad
n\in{\rm Im}\,A_j.
```

The dimensionless quadratic interface form is:

```tex
S_j^{(2)}
=
\left\langle t,A_j^\dagger n\right\rangle
+
\left\langle n,A_jt\right\rangle
-
\left\langle n,A_jA_j^\dagger n\right\rangle .
```

Equivalently, on `V_j \oplus Im A_j`, the Hessian is:

```tex
{\cal H}_j
=
\begin{pmatrix}
0&A_j^\dagger\\
A_j&-A_jA_j^\dagger
\end{pmatrix}.
```

For a normalized vector:

```tex
\langle t,t\rangle=1,
```

define:

```tex
n={1\over\sqrt J}A_jt.
```

Then:

```tex
\langle n,n\rangle=1,
```

and:

```tex
\langle n,A_jt\rangle=\sqrt J,
\qquad
\langle n,A_jA_j^\dagger n\rangle=J.
```

The projected matrix is:

```tex
\begin{pmatrix}
0&\sqrt J\\
\sqrt J&-J
\end{pmatrix}.
```

This is the de Vries block.

## Projected KK Mode Proof Object

The D10 mode proof can be stated as one projected operator identity.
Let:

```tex
{\cal H}_{\rm weak}
=
H^0(CP1,O(0))
\oplus
H^0(CP1,O(1))
\oplus
H^0(CP1,O(2))
=
V_0\oplus V_{1/2}\oplus V_1.
```

For each:

```tex
j=0,{1\over2},1,
\qquad
J_j=j(j+1),
```

the selected D10 stationary point must give:

```tex
\Pi_j{\cal K}_{D10,*}\Pi_j
=
\mu_*^2{\cal H}_j
=
\mu_*^2
\begin{pmatrix}
0&A_j^\dagger\\
A_j&-A_jA_j^\dagger
\end{pmatrix}
\bigg|_{V_j\oplus{\rm Im}A_j}.
```

Using:

```tex
A_j^\dagger A_j=J_j{\bf 1}_{V_j},
```

this is equivalent to:

```tex
\Pi_j{\cal K}_{D10,*}\Pi_j
=
\mu_*^2
\begin{pmatrix}
0&\sqrt{J_j}\\
\sqrt{J_j}&-J_j
\end{pmatrix}.
```

The secular equation for the dimensionless pole variable `X` is:

```tex
\det
\left[
\begin{pmatrix}
0&\sqrt J\\
\sqrt J&-J
\end{pmatrix}
-X{\bf 1}
\right]
=0,
```

so:

```tex
X^2+JX-J=0,
```

with positive branch:

```tex
X_+(J)={-J+\sqrt{J^2+4J}\over2}.
```

The three weak sectors then give:

```tex
M_\gamma^2=\mu_*^2X_+(0)=0,
```

```tex
M_W^2=\mu_*^2X_+(3/4),
\qquad
M_Z^2=\mu_*^2X_+(2).
```

Thus:

```tex
\tan^2\theta_{\rm pole}
=
{1-X_+(3/4)/X_+(2)\over X_+(3/4)/X_+(2)}
=
0.2871691363429836.
```

This is the workspace proof object for equivalence to the de Vries
hint. The proof is physical when the same D10 stationary point also
fixes:

```tex
\lambda_*=\lambda_{\rm BL},
\qquad
\rho_*,
\qquad
Q\eta_0=0,
\qquad
v_{\rm EW},M_H.
```

## Equivalence Pass Rule

Status: algebra-from-source at the projected-operator level;
physical compactification proof open.

A D10 candidate passes the de Vries equivalence gate when the following
data are produced by one selected D10 stationary point:

1. the weak sectors are `V_0`, `V_{1/2}`, and `V_1`;
2. the current/holonomy map satisfies

```tex
A_j^\dagger A_j=j(j+1){\bf 1}_{V_j};
```

3. the projected fluctuation operator is

```tex
\Pi_j{\cal K}_{D10,*}\Pi_j
=
\mu_*^2
\begin{pmatrix}
0&\sqrt{j(j+1)}\\
\sqrt{j(j+1)}&-j(j+1)
\end{pmatrix};
```

4. the pole interpretation assigns `j=0` to the photon slot, `j=1/2`
   to the `W` slot, and `j=1` to the `Z` slot;
5. the same vacuum fixes the scale and scalar data needed for
   `alpha_EM`, `v_EW`, and `M_H`.

Under these conditions the secular equation and pole weak angle are
read from the D10 operator itself:

```tex
X^2+j(j+1)X-j(j+1)=0,
\qquad
\tan^2\theta_{\rm pole}=0.2871691363429836.
```

## Current-Metric Deformation Test

Let the retained current metric be:

```tex
\langle e_a,e_b\rangle_{\rm cur}
=
\kappa_{\rm cur}\delta_{ab},
\qquad
c=\sqrt{\kappa_{\rm cur}}.
```

The projected block becomes:

```tex
{\cal H}_j(c)
=
\begin{pmatrix}
0&c\sqrt J\\
c\sqrt J&-c^2J
\end{pmatrix}.
```

The corresponding pole equation is:

```tex
X^2+c^2JX-c^2J=0.
```

Thus exact de Vries equivalence is the concrete current-metric
condition:

```tex
\kappa_{\rm cur}=1.
```

The `SU(2)_2` Regge/WZW layer supplies the finite spin set. The D10
target-space KK mode operator must use the zero-mode or holonomy
metric on that finite set to reach the unit current metric.

## Orthogonal Auxiliary Directions

The full auxiliary space is:

```tex
W_j={\rm Im}\,A_j\oplus{\rm Ker}\,A_j^\dagger.
```

The Schur block controls the image part. The orthogonal part requires a
separate decoupling term:

```tex
S_{\perp}^{(2)}
=
M_\perp^2
\left\langle n_\perp,(1-P_j)n_\perp\right\rangle,
\qquad
M_\perp^2>0.
```

Open gate: derive this decoupling from the same boundary/current sector
or show that the auxiliary field is defined directly on `Im A_j`.

## D10 Action Interpretation

The candidate D10 interface action has the schematic form:

```tex
S_{\rm D10}
=
S_{\rm IIA}[CP2\times CP1,C_1]
+
S_{\rm str/Regge}
+
S_{\rm current}
+
S_{\rm aux}.
```

The current sector supplies:

```tex
J_0^a|_{V_j}=T_a^{(j)}.
```

The auxiliary sector supplies the image field:

```tex
n_a\in{\rm Im}\,A_j\subset V_j\otimes{\mathbb R}^3.
```

The required quadratic piece is:

```tex
S_{\rm current+aux}^{(2)}
=
\mu^2
\left[
\left\langle t,A_j^\dagger n\right\rangle
+
\left\langle n,A_jt\right\rangle
-
\left\langle n,A_jA_j^\dagger n\right\rangle
\right]
+
S_\perp^{(2)}.
```

The coefficient is canonical when the current zero-mode generators have
the same normalization as the `SU(2)` Casimir used in the Borel-Weil
sector.

The normalization audit is recorded in
[d10-current-action-normalization-gate.md](d10-current-action-normalization-gate.md).
There a current rescaling:

```tex
A_j\mapsto cA_j
```

gives:

```tex
a=c,
\qquad
b=c^2.
```

Thus exact de Vries requires the retained D10 brane/current interface
to enforce:

```tex
c=1.
```

The normalization note refines this as a current-metric condition:

```tex
c=\sqrt{\kappa_{\rm cur}},
\qquad
\kappa_{\rm cur}=1.
```

This is the single coefficient left by the action-level operator
calculation.

## Relation To Regge Priority

The same `SU(2)_2` current sector supplies:

```tex
j=0,{1\over2},1,
```

and:

```tex
A_j^\dagger A_j=j(j+1){\bf 1}_{V_j}.
```

Therefore the D10 Regge layer and the de Vries weak-label selector use
one current algebra. This keeps the moduli priority on:

```tex
b=a^2,
```

with the canonical point:

```tex
a=1.
```

## Relation To The D9 Q Gate

The D9 endpoint requires:

```tex
Q=T_3+Y.
```

The boundary-changing sector is:

```tex
O(1),
\qquad
j={1\over2}.
```

The action gate is:

```text
the component selected from O(1) must be Q-neutral, and the same
boundary/current data must compute the surviving Q norm.
```

This ties the de Vries operator gate to the alpha gate.

The secondary Connes-format gate is recorded in
[d6-connes-higgs-distance-gate.md](d6-connes-higgs-distance-gate.md).
There the same `O(1)` Q-neutral datum is tested as a finite-direction
connection whose vacuum value controls the sheet distance over
`M4 x CP1`.

The explicit finite-distance calculation is recorded in
[d6-connes-o1-distance-calculation.md](d6-connes-o1-distance-calculation.md).
It uses:

```tex
\Phi:O(0)\to O(1),
\qquad
d_{\rm sheet}={1\over\|\Phi\|}.
```

The D6 image-channel bridge is recorded in
[d6-connes-schur-interface-gate.md](d6-connes-schur-interface-gate.md).
It writes the `j=1/2` Connes/current Hessian on:

```tex
V_{1/2}\oplus{\rm Im}\,A_{1/2}.
```

## Pass/Fail Gate

Pass requires:

1. identify the D10 current algebra or brane current carrying
   `SU(2)_2`;
2. show that its zero modes act as `T_a^{(j)}` on the CP1 Borel-Weil
   sectors;
3. define the auxiliary field on `Im A_j` or derive a positive
   decoupling term on `Ker A_j^\dagger`;
4. derive the quadratic form:

```tex
\begin{pmatrix}
0&A_j^\dagger\\
A_j&-A_jA_j^\dagger
\end{pmatrix};
```

5. fix the coefficient to `a=1`;
6. preserve the `Q`-neutral `O(1)` component;
7. use the same sector to compute `r/n`, `rho_*`, or the replacement
   current normalization.

## Current Status

Status: the algebraic action gate is explicit.

Closed algebra:

```tex
A_j^\dagger A_j=j(j+1){\bf 1}_{V_j}
\quad\Rightarrow\quad
{\cal H}_j|_{V_j\oplus{\rm Im}A_j}
=
\begin{pmatrix}
0&\sqrt J\\
\sqrt J&-J
\end{pmatrix}.
```

Open physics gates:

- D10 origin of the current sector;
- brane/current normalization enforcing `kappa_cur=1`;
- treatment of `Ker A_j^\dagger`;
- D9 `Q` preservation and alpha normalization.
