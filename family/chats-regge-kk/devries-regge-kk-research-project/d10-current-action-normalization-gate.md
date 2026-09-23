# D10 Current Action Normalization Gate

## Purpose

This note sharpens the D10 action requirement for the de Vries block:
the current interface must realize the Schur Hessian with canonical
coefficient

```tex
a=1.
```

The target lives in the Type IIA frame:

```text
M4 x CP2 x CP1
```

with RR `C1` flux from the `M^{pqr}` circle and an added
brane/current/branch interface carrying the weak `SU(2)` current data.

## Current Sector

Use an affine `SU(2)_2` current sector as the finite weak interface.
The level fixes the allowed integrable sectors:

```tex
j=0,{1\over2},1.
```

The zero modes act on each primary space as:

```tex
J^a_0|_{V_j}=T_a^{(j)}.
```

Use the standard finite-dimensional generator normalization:

```tex
[T_a,T_b]=i\epsilon_{abc}T_c,
\qquad
\sum_{a=1}^3T_aT_a=j(j+1){\bf 1}_{V_j}.
```

Choose an orthonormal current-vector basis:

```tex
\langle e_a,e_b\rangle=\delta_{ab}.
```

Then:

```tex
A_j=\sum_{a=1}^3T_a^{(j)}\otimes e_a
```

satisfies:

```tex
A_j^\dagger A_j=j(j+1){\bf 1}_{V_j}.
```

This is the action-normalization meaning of the canonical current map.

## Source-To-Action Normalization Calculation

The Regge/WZW source fixes two separate pieces of data.

First, the affine `SU(2)_k` source gives the admissible finite set:

```tex
j=0,{1\over2},\ldots,{k\over2}.
```

At:

```tex
k=2,
```

this gives:

```tex
j=0,{1\over2},1.
```

Second, the same source gives the conformal weight:

```tex
\Delta_j={j(j+1)\over k+2}.
```

Thus the WZW level selects the de Vries weak-label set. It also places
the zero-mode Casimir inside the worldsheet Hamiltonian with scale
factor:

```tex
{1\over k+2}={1\over4}.
```

For the three retained sectors:

| `j` | `J=j(j+1)` | `Delta_j=J/4` | `4 Delta_j` |
|---:|---:|---:|---:|
| `0` | `0` | `0` | `0` |
| `1/2` | `3/4` | `3/16` | `3/4` |
| `1` | `2` | `1/2` | `2` |

The de Vries Schur block uses the zero-mode Casimir:

```tex
J=j(j+1),
```

so a D10 mass operator built directly from `L_0` must include the
target-space conversion factor:

```tex
k+2=4.
```

Equivalently, the interface may use the holonomy/current zero-mode
metric directly:

```tex
\langle e_a,e_b\rangle=\delta_{ab},
\qquad
\sum_aT_aT_a=J.
```

Status:

```text
SU(2)_2 fixes the allowed j-set.
The zero-mode metric gives the algebraic unit map.
The target-space action must still derive the conversion from WZW
normalization or holonomy metric to the physical mass operator.
```

## Current Metric Scale Lemma

Let the target-space current-vector metric on the retained `SU(2)`
orbit be:

```tex
\langle e_a,e_b\rangle_{\rm cur}
=
\kappa_{\rm cur}\,\delta_{ab}.
```

With:

```tex
A_j^{(\kappa)}
=
\sum_{a=1}^3 T_a^{(j)}\otimes e_a,
```

the adjoint is computed with the same current metric, so:

```tex
\left(A_j^{(\kappa)}\right)^\dagger A_j^{(\kappa)}
=
\kappa_{\rm cur}\,j(j+1){\bf 1}_{V_j}.
```

For a unit vector `t in V_j`, define the image unit vector:

```tex
n_j
=
{1\over\sqrt{\kappa_{\rm cur}J}}A_j^{(\kappa)}t,
\qquad
J=j(j+1).
```

Then the one-current image block becomes:

```tex
\begin{pmatrix}
0&\sqrt{\kappa_{\rm cur}}\sqrt J\\
\sqrt{\kappa_{\rm cur}}\sqrt J&-\kappa_{\rm cur}J
\end{pmatrix}
=
\begin{pmatrix}
0&c\sqrt J\\
c\sqrt J&-c^2J
\end{pmatrix},
\qquad
c=\sqrt{\kappa_{\rm cur}}.
```

Consequences:

1. a single current metric automatically keeps the Regge-compatible
   locus `b=a^2`;
2. exact de Vries equivalence is the metric condition

```tex
\kappa_{\rm cur}=1;
```

3. the WZW source data give `Delta_j=J/(k+2)`, so at `k=2` the
   target-space mass conversion must multiply the conformal weight by
   four to reach the same unit `J`.

The next D10 calculation is therefore concrete:

```text
derive kappa_cur=1 from the brane/current/holonomy metric, or compute
its value and propagate c=sqrt(kappa_cur) through the weak-angle and
mass-pole formulas.
```

## Scale-Normalization Separation

The boundary Wilson route introduces a dimensionful fluctuation scale:

```tex
A_\tau=\mu\,\xi^aT_a.
```

This `\mu` multiplies the whole projected mass operator:

```tex
\Pi_j{\cal K}_{D10,*}\Pi_j
=
\mu_*^2
\begin{pmatrix}
0&c\sqrt J\\
c\sqrt J&-c^2J
\end{pmatrix}.
```

The physical compactification scale and the local boundary scale enter
through `\mu_*`. The ratio data are controlled by the dimensionless
current metric:

```tex
c=\sqrt{\kappa_{\rm cur}}.
```

Thus `\mu_*` fixes the common mass scale, while `\kappa_{\rm cur}`
fixes the pole equation:

```tex
X^2+c^2JX-c^2J=0.
```

The coefficient gate cannot be absorbed into the physical scale because
the off-diagonal and diagonal entries scale as:

```tex
c\sqrt J,
\qquad
c^2J.
```

The pass condition is therefore:

```tex
\hbox{D10 boundary/current metric on }{\rm Im}\,A_j
=
\hbox{Borel-Weil invariant metric on }V_j
```

in the orthonormal frame where the Payen boundary charge is:

```tex
R(A_\tau)=\mu\,\xi^aT_a^{(j)}.
```

Then:

```tex
\kappa_{\rm cur}=1,
\qquad
c=1,
```

and the same `\mu_*` remains available as the physical mass scale
selected by the D10 vacuum.

## L0 Route Versus Zero-Mode Route

The WZW source gives the conformal weight:

```tex
\Delta_j={J\over k+2},
\qquad
J=j(j+1).
```

If the D10 mass operator used the conformal-weight normalization as the
Schur operator norm, it would give:

```tex
A_{L0,j}^\dagger A_{L0,j}
=
{J\over k+2}{\bf 1}_{V_j}.
```

The projected block would be:

```tex
\begin{pmatrix}
0&{1\over\sqrt{k+2}}\sqrt J\\
{1\over\sqrt{k+2}}\sqrt J&-{1\over k+2}J
\end{pmatrix}.
```

At the Regge-selected level:

```tex
k=2,
\qquad
c_{L0}={1\over2}.
```

This is a Regge-compatible block on the locus `b=a^2`, with coefficient
`a=1/2`. The exact de Vries block requires the D10 target-space
interface to use:

```tex
A_j
=
\sqrt{k+2}\,A_{L0,j},
```

or equivalently to use the zero-mode/holonomy metric directly:

```tex
A_j^\dagger A_j=J{\bf 1}_{V_j}.
```

Numerical control:

```tex
c=1
\quad\Rightarrow\quad
\tan^2\theta_{\rm pole}=0.2871691363429838,
```

while:

```tex
c={1\over2}
\quad\Rightarrow\quad
\tan^2\theta_{\rm pole}=0.4314539065631521.
```

Therefore the direct `L0` coefficient is a rejected route for exact
de Vries equivalence. It remains useful as the Regge/current control
normalization that the D10 action must lift.

Status:

```text
WZW L0 normalization gives the finite spin set and a controlled
Regge-compatible block with c=1/2 at k=2.
Exact de Vries requires the D10 interface metric to lift this to the
zero-mode/holonomy normalization c=1.
```

## Zero-Mode Charge Route

The affine current algebra has:

```tex
[J_m^a,J_n^b]
=
f^{ab}{}_cJ_{m+n}^c
+km\delta_{m+n}d^{ab}.
```

Set:

```tex
m=n=0.
```

The central term vanishes and the zero modes obey the finite algebra:

```tex
[J_0^a,J_0^b]
=
f^{ab}{}_cJ_0^c.
```

On the integrable primary module `L_j`, the zero modes act as the
ordinary spin-`j` representation:

```tex
J_0^a|_{L_j}=T_a^{(j)}.
```

With the invariant representation metric:

```tex
\sum_aJ_0^aJ_0^a
=
\sum_aT_a^{(j)}T_a^{(j)}
=
J{\bf 1}_{V_j}.
```

Therefore the zero-mode charge route gives:

```tex
\kappa_{\rm cur}=1
```

algebraically. The D10 structure then reads:

```text
Regge/WZW supplies the finite j-set through SU(2)_2.
The target-space D10 interface uses the current zero modes or the
equivalent holonomy differential for the mass operator.
```

Remaining action-placement gate:

```text
derive from the D10 brane/current/holonomy sector that the quadratic
fluctuation operator couples to J_0^a, with Sugawara L0 retained as the
worldsheet selection/control channel.
```

## Boundary Chan-Paton Placement Route

Payen's boundary action for Chan-Paton factors supplies a source-backed
open-string placement for the zero-mode route. Attach a group-valued
endpoint variable:

```tex
g(\tau)\in G
```

to the string boundary. Coupling to an external Yang-Mills field uses:

```tex
S_{\partial\Sigma}
=
\int_{\partial\Sigma}
d\tau\,
\kappa\!\left(
-ig^{-1}(\partial_\tau+iA_\tau)g
\right).
```

The boundary pullback is:

```tex
A_\tau
=
A_\mu(X(\bar\sigma(\tau)))
{\partial X^\mu(\bar\sigma(\tau))\over\partial\sigma^\alpha}
{\partial\bar\sigma^\alpha\over\partial\tau}.
```

Canonical quantization gives a finite-dimensional Hilbert space
carrying an irreducible representation `R` of `G`, and the boundary
charges act as representation generators. The boundary path integral
gives:

```tex
\operatorname{Tr}\,
T_{\partial\Sigma}
\exp\left(
i\int_{\partial\Sigma}d\tau\,R(A_\tau)
\right).
```

Project specialization:

```tex
G=SU(2),
\qquad
R=V_j=H^0(CP1,O(2j)),
\qquad
j=0,{1\over2},1.
```

Then:

```tex
R(A_\tau)
=
A_\tau^aT_a^{(j)},
\qquad
\sum_aT_a^{(j)}T_a^{(j)}
=
j(j+1){\bf 1}_{V_j}.
```

This is precisely the zero-mode/holonomy route:

```tex
A_j=\sum_aT_a^{(j)}\otimes e_a,
\qquad
A_j^\dagger A_j=J{\bf 1}_{V_j}.
```

### Wilson-Loop Expansion

Set the boundary gauge fluctuation in an orthonormal current frame:

```tex
A_\tau=\mu\,\xi^a(\tau)T_a.
```

The boundary Wilson operator is:

```tex
W[\xi]
=
\operatorname{Tr}\,
T_{\partial\Sigma}
\exp\left(
i\mu\int_{\partial\Sigma}d\tau\,\xi^a(\tau)T_a
\right).
```

The first variation inserts the zero-mode charge:

```tex
{\delta W\over\delta\xi^a(\tau)}\bigg|_{\xi=0}
\propto
T_a.
```

Therefore a boundary fluctuation `n=n^a e_a` couples to a state
`t in V_j` through:

```tex
A_j^\dagger n
=
\sum_an^aT_a^{(j)}t.
```

Equivalently:

```tex
A_jt
=
\sum_aT_a^{(j)}t\otimes e_a.
```

The second variation supplies the invariant charge-bilinear tensor:

```tex
{\delta^2 W\over\delta\xi^a(\tau_1)\delta\xi^b(\tau_2)}
\bigg|_{\xi=0}
\propto
T_{\partial\Sigma}\left(T_aT_b\right).
```

Contracting this bilinear with the boundary image field gives:

```tex
\left\|A_j^\dagger n\right\|^2
=
\langle n,A_jA_j^\dagger n\rangle.
```

Thus the Payen boundary placement supplies both tensors needed by the
Schur block:

```tex
A_j,
\qquad
A_jA_j^\dagger.
```

Open action gate:

```text
derive the local boundary current-current completion with coefficient
-mu^2 ||A_j^dagger n||^2 from the D10 brane, branch-defect, DBI/WZ,
gauge-fixing, or boundary-RG sector.
```

### Auxiliary Schur Completion

The local sign and coefficient can be generated by one positive
auxiliary boundary field:

```tex
y\in V_j.
```

Take:

```tex
S_{\rm aux}^{(2)}
=
\mu^2
\left[
\langle t,t\rangle
+\langle y,y\rangle
+\langle y,t-A_j^\dagger n\rangle
+\langle t-A_j^\dagger n,y\rangle
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

This is exactly the image-sector Schur block. The new D10 placement
gate is:

```text
derive the auxiliary field y and the equal local coefficients from the
brane/open-boundary/branch action.
```

Status:

```text
source-backed open-string boundary placement exists for the zero-mode
charge route and for the tensors A_j and A_j A_j^dagger. The D10-specific
gate is to identify the brane, branch-defect, or open-string boundary in
the selected CP2 x CP1/flag background and to derive the auxiliary
Schur-completion field y with the equal local coefficients.
```

The Atiyah-Manton reading supplies the same first-order object. Holonomy
of an `SU(2)` connection along the relevant circle-like direction gives:

```tex
U(\gamma)=P\exp\left(-\int_\gamma A\right),
\qquad
\delta U_j\simeq-\sum_a\xi^aT_a^{(j)}.
```

The infinitesimal holonomy differential is:

```tex
Q_T=\sum_aT_a^{(j)}\otimes e_a.
```

With the same orthonormal orbit metric:

```tex
Q_T^\dagger Q_T=J.
```

Therefore the D10 normalization problem has a precise form:

```text
show that the branch/current/brane interface uses the orthonormal
holonomy metric, or show that its coefficient is c and propagate c
through the electroweak calculation.
```

## Quadratic Interface Action

Let:

```tex
t\in V_j,
\qquad
n\in W_j=V_j\otimes{\mathbb R}^3.
```

Use the image projector:

```tex
P_j={1\over J}A_jA_j^\dagger,
\qquad
J=j(j+1),
\qquad
j>0.
```

The canonical quadratic interface term is:

```tex
S_{\rm int}^{(2)}
=
\mu^2
\left[
\langle t,A_j^\dagger P_jn\rangle
+
\langle P_jn,A_jt\rangle
-
\langle P_jn,A_jA_j^\dagger P_jn\rangle
\right]
+
\mu^2M_\perp^2
\langle n,(1-P_j)n\rangle.
```

Here:

```tex
M_\perp^2>0.
```

The first bracket is the de Vries image block. The second term is the
orthogonal auxiliary gap.

On:

```tex
V_j\oplus{\rm Im}\,A_j,
```

the Hessian is:

```tex
{\cal H}_j
=
\begin{pmatrix}
0&A_j^\dagger\\
A_j&-A_jA_j^\dagger
\end{pmatrix}.
```

For:

```tex
n_j={1\over\sqrt J}A_jt,
\qquad
\langle t,t\rangle=1,
```

the projected block is:

```tex
\begin{pmatrix}
0&\sqrt J\\
\sqrt J&-J
\end{pmatrix}.
```

Thus the action has:

```tex
a=1.
```

## Normalization Audit

If the interface current is rescaled:

```tex
A_j\mapsto cA_j,
```

the projected block becomes:

```tex
\begin{pmatrix}
0&c\sqrt J\\
c\sqrt J&-c^2J
\end{pmatrix}.
```

So:

```tex
a=c,
\qquad
b=c^2.
```

The Regge-compatible locus survives as:

```tex
b=a^2.
```

The exact de Vries point requires the brane/current normalization:

```tex
c=1.
```

Therefore the open physical question is concrete:

```text
does the retained RR/Chern/current interface give the unit current map,
or does it produce a dimensionless factor c?
```

## Relation To The Type IIA Background

The Type IIA background supplies:

```tex
CP2\times CP1,
\qquad
C_1,
\qquad
F_2\sim p\,\omega_{CP2}+q\,\omega_{CP1}.
```

The fundamental closed-string NSNS sigma model supplies the Regge tower.
The RR/Chern data and the `O(n)` sectors require an additional interface
channel:

```text
brane current, equivariant current, branch defect, or open-string
boundary current.
```

The current-normalization gate demands that this channel identify its
current metric with the Borel-Weil metric on:

```tex
H^0(CP1,O(2j)).
```

In that case the zero-mode map has the canonical coefficient:

```tex
a=1.
```

## KK Gauge-Metric Formula For `kappa_cur`

The same geometric normalization used for the Weinberg coupling test
can measure the current metric. Let `K_a` be the three internal Killing
fields or interface vector fields generating the retained weak
`SU(2)` action on the normalized D10 space:

```tex
\widehat K_6=CP2\times CP1
\quad{\rm or}\quad
F_{1,2}(C^3).
```

Define the normalized D10 metric matrix:

```tex
{\cal G}^{(2)}_{ab}
=
{1\over{\rm Vol}(\widehat K_6)}
\int_{\widehat K_6}
d^6y\,\sqrt{\widehat g}\,
\widehat g_{mn}K_a^mK_b^n.
```

On the CP2-symmetric weak line this must reduce to:

```tex
{\cal G}^{(2)}_{ab}=L_2^2\,\delta_{ab}.
```

The canonically normalized current frame is:

```tex
e_a={K_a\over L_2}.
```

The Payen boundary coupling in that frame is:

```tex
R(A_\tau)
=
\mu\,\xi^aT_a^{(j)},
\qquad
\langle e_a,e_b\rangle=\delta_{ab}.
```

Therefore:

```tex
A_j=\sum_aT_a^{(j)}\otimes e_a,
\qquad
A_j^\dagger A_j=J{\bf 1}_{V_j}.
```

In this KK frame:

```tex
\kappa_{\rm cur}=1.
```

The physical length `L_2` remains in the gauge coupling:

```tex
g_2={2\pi\sqrt{16\pi G}\over L_2},
```

and the common mass scale remains in:

```tex
\mu_*.
```

Thus the DeVries operator normalization and the Weinberg coupling
normalization are compatible when the boundary Schur image channel uses
the same orthonormal weak frame that defines `L_2`.

Open calculation:

```text
compute G_ab^(2) for the selected normalized CP2 x CP1 or flag metric,
then verify that the boundary image channel uses e_a=K_a/L_2 and
report any separate current metric as kappa_cur.
```

### CP1 Control Integral

On a round `CP1 ~= S2` weak factor with radius `R_w`, use the standard
rotation Killing fields:

```tex
K_a=x\times e_a,
\qquad
{x^2}=R_w^2.
```

Their pointwise norms are:

```tex
|K_a|^2=R_w^2-x_a^2.
```

The sphere average gives:

```tex
\langle x_ax_b\rangle={R_w^2\over3}\delta_{ab}.
```

Hence:

```tex
{1\over{\rm Vol}(CP1)}
\int_{CP1}
\sqrt g\,g(K_a,K_b)
=
{2\over3}R_w^2\delta_{ab}.
```

In this rotation convention:

```tex
L_2^2={2\over3}R_w^2,
\qquad
e_a={K_a\over L_2},
\qquad
\langle e_a,e_b\rangle=\delta_{ab}.
```

Status: CP1 control calculation. The selected flag/product metric must
now fix the convention relating `R_w^2` to the `lambda` coordinate and
to the Weinberg length `L_2`.

### Bailin-Love/Weinberg Length Split

Weinberg's rule gives:

```tex
g^2={4\pi^2\kappa^2\over L^2},
\qquad
\kappa^2=16\pi G.
```

Bailin-Love equation (42) gives the weak-isospin coupling on `M^{pqr}`:

```tex
g_2^2
=
3\kappa^2
\left(2b^{-2}+q^2c^{-2}\right)^{-1}.
```

Therefore the Weinberg length inherited from the `M^{pqr}` parent is:

```tex
L_{2,{\rm BL}}^2
=
{4\pi^2\over3}
\left(2b^{-2}+q^2c^{-2}\right).
```

With the Bailin-Love Einstein metric parameters:

```tex
b=\gamma\sqrt{2\beta},
\qquad
c=q\gamma,
```

this becomes:

```tex
L_{2,{\rm BL}}^2
=
{4\pi^2\over3\gamma^2}
{1+\beta\over\beta}.
```

The two terms have different D10 meanings:

```tex
L_{2,{\rm horiz}}^2
=
{4\pi^2\over3\gamma^2}{1\over\beta},
\qquad
L_{2,{\rm vert}}^2
=
{4\pi^2\over3\gamma^2}.
```

`L_{2,horiz}` is the weak-orbit length visible in the CP1 metric
average. `L_{2,vert}` is the vertical connection contribution from the
parent `M^{pqr}` circle, seen in D10 through the RR/current interface.

The source connection is visible in the Bailin-Love fiber square:

```tex
c^{-2}
\left[
D dz^3+\sqrt3pK_8+qK_3
\right]^2.
```

The weak component is `qK_3`, hence its contribution to the invariant
weak-current norm is `q^2c^-2`. In Weinberg length units:

```tex
L_{2,conn}^2
=
{4\pi^2\over3}q^2c^{-2}
=
{4\pi^2\over3\gamma^2}
=
L_{2,vert}^2.
```

For the selected labels:

```tex
\beta=0.328481702082924367895293909852,
```

so:

```tex
{L_{2,{\rm horiz}}^2\over L_{2,{\rm BL}}^2}
=
0.7527390090748721,
\qquad
{L_{2,{\rm vert}}^2\over L_{2,{\rm BL}}^2}
=
0.24726099092512785.
```

Equivalently:

```tex
L_{2,{\rm BL}}^2=(1+\beta)L_{2,{\rm horiz}}^2.
```

Open gate: derive the D10 RR/current sector that supplies the vertical
term while preserving the unit projected Schur metric `kappa_cur=1`.

### Selected One-Shape Application

Use the one-shape product metric convention:

```tex
ds^2_{K6}(\ell)
=
\ell^2
\left[
ds^2_{CP2}
+\lambda\,ds^2_{CP1}
+\cdots
\right].
```

Let the reference `CP1` metric have radius `R_0`. Then:

```tex
R_w^2(\ell,\lambda)=\ell^2\lambda R_0^2.
```

The weak current length is therefore:

```tex
L_{2,{\rm horiz}}^2(\ell,\lambda)
=
{2\over3}\ell^2\lambda R_0^2.
```

Equivalently, for the normalized geometry:

```tex
\widehat L_{2,{\rm horiz}}^2(\lambda)
=
{2\over3}\lambda R_0^2,
\qquad
L_{2,{\rm horiz}}(\ell,\lambda)
=
\ell\,\widehat L_{2,{\rm horiz}}(\lambda).
```

At the selected shape:

```tex
\lambda_*=\lambda_{\rm BL}=0.514554893751227,
```

the CP1 control factor is:

```tex
\sqrt{2\lambda_{\rm BL}/3}=0.5856932608747956.
```

Using the selected electroweak output as the total Bailin-Love/Weinberg
length:

```tex
{L_{2,{\rm BL}}\over\sqrt G}=69.038577890768138,
```

the horizontal CP1 component is:

```tex
{L_{2,{\rm horiz}}\over\sqrt G}
=
{L_{2,{\rm BL}}\over\sqrt{1+\beta}\sqrt G}
=
59.898238170777375.
```

Using the horizontal CP1 metric average gives:

```tex
{\ell_*R_0\over\sqrt G}
=
102.2689557351453.
```

Status: algebraic consistency check. The value of `R_0` is a metric
normalization convention; the D10 vacuum must still determine `ell_*`
through `rho_*=c_\rho ell_*^2`.

The same relation can be written without `ell`. For:

```tex
{\rm Vol}(\widehat K_6)=\lambda V_{4,0}V_{2,0},
\qquad
c_\rho(\lambda)=(\lambda V_{4,0}V_{2,0})^{1/3},
```

one has:

```tex
{(L_{2,{\rm horiz}}/\sqrt G)^2\over\rho}
=
{2\over3}{\lambda R_0^2\over c_\rho(\lambda)}.
```

At the selected point this gives:

```tex
{(L_{2,{\rm horiz}}/\sqrt G)^2\over\rho_*}
=
379.12087511550334.
```

The total parent length gives the previous value:

```tex
{(L_{2,{\rm BL}}/\sqrt G)^2\over\rho_*}
=
503.65514546861164.
```

In the KLT coframe convention:

```tex
V_e=\int e^{123456},
\qquad
J=-a e^{12}+b e^{34}-c e^{56},
\qquad
d^2=abc.
```

The volume form follows from:

```tex
{1\over6}J^3=abc\,e^{123456},
```

so:

```tex
{\rm Vol}(\widehat K_6)=abc\,V_e.
```

On:

```tex
a=b=A,
\qquad
c=\lambda A,
```

the normalized choice `A=1` gives:

```tex
c_\rho(\lambda)=(\lambda V_e)^{1/3}.
```

The selected one-scale equation is then:

```tex
{R_0^2\over V_e^{1/3}}
=
885.6208147862705.
```

Using the full parent length as the CP1 metric term gives the control
value:

```tex
{R_0^2\over V_e^{1/3}}
=
1176.531047427331.
```

The flag-ring period control gives:

```tex
h=e^{12}+e^{34},
\qquad
\eta_{\rm harm}
=
-{1\over2}e^{12}
+{1\over2}e^{34}
+e^{56},
```

so:

```tex
h^2\eta_{\rm harm}=2e^{123456}.
```

With:

```tex
\int h^2\eta=1,
```

this would set:

```tex
V_e={1\over2}.
```

If the weak fiber period also sets `4\pi R_0^2=1`, the control value is:

```tex
{R_0^2\over V_e^{1/3}}
=
0.10026133149814978.
```

The selected output therefore contains a large conversion between
period-normalized cohomology representatives and the Weinberg generator
length convention.

Thus the weak-current metric, alpha scale, and one-scale volume
normalization meet in one dimensionless equation.

## Relation To D9 Parameters

The same interface must preserve the Q-neutral `O(1)` component:

```tex
Q\eta_0=0.
```

It also has to transport or compute the surviving norm:

```tex
L_Q.
```

So a completed action must connect three numbers through one sector:

```tex
a=1,
\qquad
{r\over n},
\qquad
{L_Q\over\sqrt G}.
```

This is the current action-level form of the selector problem.

## Current Gate Split

The normalization problem now separates into three tests:

1. representation charge test:

```tex
\sum_aT_a^{(j)}T_a^{(j)}
=
j(j+1){\bf 1}_{V_j}.
```

Status: algebra-from-source from affine zero modes and the Payen
endpoint representation route.

2. physical current metric test:

```tex
\mathcal G^{(2)}_{ab}
=
L_2^2\delta_{ab},
\qquad
e_a={K_a\over L_2},
\qquad
\langle e_a,e_b\rangle_{\rm D10}=\delta_{ab}
```

on the image channel used by the mass operator.

Status: formula gate; compute the KK integral and prove that the
boundary image channel uses this orthonormal frame.

3. local Schur coefficient test:

```tex
S_{\rm eff}^{(2)}
=
\mu_*^2
\left[
\langle t,A_j^\dagger n\rangle
+\langle n,A_jt\rangle
-\langle n,A_jA_j^\dagger n\rangle
\right].
```

Status: open gate; derive the auxiliary `y` and equal coefficients from
the same boundary sector.

## Pass/Fail Gate

Pass requires:

1. identify the D10 brane/current/branch sector carrying `SU(2)_2`;
2. prove that the zero modes on `O(0)`, `O(1)`, and `O(2)` are
   canonically normalized as `T_a`;
3. derive the image-channel term `-A_jA_j^\dagger` from the same
   current metric;
4. compute the current metric scale and show `kappa_cur=1`;
5. give a positive gap to `Ker A_j^\dagger`;
6. preserve `Q\eta_0=0`;
7. compute or constrain `r/n`, `rho_*`, and `L_Q`.

Current status: canonical normalization is formulated as a precise
action gate. The representation charge test is fixed by the
zero-mode/Payen route. The physical current metric test and local Schur
coefficient test remain open.
