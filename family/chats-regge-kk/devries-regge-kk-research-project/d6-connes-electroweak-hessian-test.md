# D6 Connes Electroweak Hessian Test

## Purpose

This note tests the D6 Connes two-sheet Higgs picture against the
electroweak and current-Schur gates.

Use the D6 base:

```tex
X_6=M_4\times CP1.
```

Use the finite-direction field already fixed in
[d6-connes-o1-distance-calculation.md](d6-connes-o1-distance-calculation.md):

```tex
\Phi:O(0)\to O(1).
```

The test has four parts:

1. verify that the selected `O(1)` vector is `Q`-neutral;
2. compute the `SU(2)` Casimir on that vector;
3. compute the charged broken-vacuum orbit norm from G29;
4. compare the ordinary electroweak mass Hessian with the `j=1/2`
   current-Schur block.

## Q-Neutral Doublet Vector

Use a doublet basis:

```tex
\eta_+=
\begin{pmatrix}
1\\0
\end{pmatrix},
\qquad
\eta_0=
\begin{pmatrix}
0\\1
\end{pmatrix}.
```

The generator conventions are:

```tex
T_a={\sigma_a\over2},
\qquad
Y={1\over2},
\qquad
Q=T_3+Y.
```

The neutral vector satisfies:

```tex
T_3\eta_0=-{1\over2}\eta_0,
\qquad
Y\eta_0={1\over2}\eta_0,
```

so:

```tex
Q\eta_0=0.
```

Therefore a vacuum:

```tex
\Phi_0=v_F\eta_0
```

preserves the photon gate:

```tex
U(1)_Q.
```

## SU(2) Casimir On The Neutral Vector

The generator action on `eta_0` is:

```tex
T_1\eta_0={1\over2}\eta_+,
```

```tex
T_2\eta_0=-{i\over2}\eta_+,
```

```tex
T_3\eta_0=-{1\over2}\eta_0.
```

Hence:

```tex
\sum_{a=1}^3\|T_a\eta_0\|^2
=
\left\langle \eta_0,\sum_{a=1}^3T_aT_a\,\eta_0\right\rangle
=
{3\over4}.
```

This closes the `j=1/2` branch-Casimir match:

```tex
J=j(j+1)={3\over4}.
```

The current-Schur operator in
[d10-current-schur-action-gate.md](d10-current-schur-action-gate.md)
therefore has the branch-Casimir size in the Connes `O(1)` neutral
sector.

## G29 Charged-Orbit Stop-Check

The physical charged weak orbit uses:

```tex
T_+=T_1+iT_2
=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
```

With the standard broken vacuum:

```tex
H_0={v\over\sqrt2}\eta_0
=
\begin{pmatrix}
0\\
v/\sqrt2
\end{pmatrix},
```

the charged orbit is:

```tex
T_+H_0=
\begin{pmatrix}
v/\sqrt2\\
0
\end{pmatrix}.
```

Thus:

```tex
{\|T_+H_0\|^2\over\|H_0\|^2}=1.
```

The component generators give:

```tex
{\|T_1H_0\|^2\over\|H_0\|^2}
=
{\|T_2H_0\|^2\over\|H_0\|^2}
=
{\|T_3H_0\|^2\over\|H_0\|^2}
={1\over4},
```

and their sum is the doublet Casimir:

```tex
{1\over4}+{1\over4}+{1\over4}={3\over4}.
```

Verdict:

```tex
J_{\rm branch}(1/2)={3\over4},
\qquad
N_W={\|T_+H_0\|^2\over\|H_0\|^2}=1.
```

The `j=1/2` de Vries block is therefore a branch/Casimir datum. The
physical `W` pole needs the G1-G3 branch-quotient or magnetic-dual
interface that maps `X_+(1/2)` into the charged vector pole while the
ordinary electroweak Higgs orbit keeps `N_W=1`.

## Electroweak Gauge Hessian

Take:

```tex
D_\mu\Phi
=
\partial_\mu\Phi
-i g_2 W^a_\mu T_a\Phi
-i g_Y B_\mu Y\Phi.
```

At the constant vacuum:

```tex
\Phi_0=v_F\eta_0,
```

the quadratic gauge term is:

```tex
\|D_\mu\Phi_0\|^2
=
{|v_F|^2\over4}
\left[
g_2^2\left((W^1_\mu)^2+(W^2_\mu)^2\right)
+\left(-g_2W^3_\mu+g_YB_\mu\right)^2
\right].
```

The massless photon direction is:

```tex
A_\mu
=
{g_YW^3_\mu+g_2B_\mu\over\sqrt{g_2^2+g_Y^2}}.
```

The massive neutral direction is:

```tex
Z_\mu
=
{g_2W^3_\mu-g_YB_\mu\over\sqrt{g_2^2+g_Y^2}}.
```

Using the standard electroweak convention:

```tex
v_{\rm EW}=\sqrt2\,|v_F|,
```

the masses are:

```tex
M_W^2={g_2^2v_{\rm EW}^2\over4},
\qquad
M_Z^2={(g_2^2+g_Y^2)v_{\rm EW}^2\over4},
\qquad
M_\gamma^2=0.
```

Therefore:

```tex
{M_W^2\over M_Z^2}
=
{g_2^2\over g_2^2+g_Y^2}.
```

## Relation To Sheet Distance

The finite-distance calculation uses:

```tex
d_{\rm sheet}={1\over\|\Phi_0\|}.
```

With:

```tex
\Phi_0=v_F\eta_0,
\qquad
\|\eta_0\|=1,
```

this gives:

```tex
\ell_H={1\over |v_F|}
={\sqrt2\over v_{\rm EW}}.
```

Thus the Connes two-sheet vacuum size is the inverse electroweak scale,
up to the stated VEV convention.

The joint scale gate is recorded in
[vacuum-scale-selector-gate.md](vacuum-scale-selector-gate.md). In that
gate the same vacuum problem carries both variables:

```tex
V_{\rm eff}=V_{\rm eff}(\rho,v_F),
\qquad
\ell_H={1\over |v_F|}.
```

Here `rho_*` is the absolute alpha-scale target and `v_F` is the
finite-direction amplitude that sets the two-sheet distance.

## Current-Schur Comparison

The Connes/electroweak calculation closes:

```tex
Q\eta_0=0,
\qquad
\sum_a\|T_a\eta_0\|^2={3\over4},
\qquad
M_\gamma^2=0.
```

The current-Schur block at `j=1/2` is:

```tex
\begin{pmatrix}
0&\sqrt{3/4}\\
\sqrt{3/4}&-3/4
\end{pmatrix}.
```

The shared algebraic datum is the `SU(2)` Casimir:

```tex
J={3\over4}.
```

The G29 stop-check separates this branch datum from the physical charged
Higgs-orbit norm:

```tex
J_{\rm branch}={3\over4},
\qquad
N_W=1.
```

Open interface requirement: derive the branch-quotient or dual magnetic
map that carries `J_branch=3/4` into the physical `W` pole while
preserving the standard Higgs Hessian above.

Open gate: derive the finite-direction Hessian whose normalized
two-channel form is the current-Schur block with canonical coefficient:

```tex
a=1.
```

The D6 bridge form of this gate is recorded in
[d6-connes-schur-interface-gate.md](d6-connes-schur-interface-gate.md).
It identifies the needed image/current variable as:

```tex
n\in{\rm Im}\,A_{1/2}.
```

Open gate: derive `g_Y/g_2`, `L_Q`, and the absolute vacuum size from
the `M^{pqr}` selector, current level, flux data, or the vacuum
extremum.

## Status

Status: electroweak Hessian test added.

Closed algebra:

- the `O(1)` neutral vector protects `Q`;
- the `SU(2)` branch Casimir gives `J_branch=3/4`;
- the charged broken-vacuum orbit gives `N_W=1`;
- the Connes vacuum gives `ell_H=sqrt(2)/v_EW`;
- the ordinary Higgs kinetic term gives the standard `W`, `Z`, and
  photon mass pattern.

Remaining gates:

- finite-direction potential;
- normalized two-channel Hessian with `a=1`;
- D10 source of the current-Schur block;
- D9 `Q` norm and alpha calculation;
- relation between `ell_H`, `rho_*`, and `r/n`.
