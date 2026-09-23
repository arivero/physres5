# Connes Finite Hessian And Schur Comparison

## Purpose

This auxiliary calculation compares three quadratic objects that use the same
Q-neutral Higgs vector:

```tex
\Phi_0=v_F\eta_0,
\qquad
Q\eta_0=0,
\qquad
\eta_0\in H^0(CP1,O(1)).
```

The objects are:

1. the finite Higgs-potential Hessian;
2. the electroweak gauge-boson Hessian;
3. the D10/current Schur Hessian that gives the de Vries block.

## Local Finite Potential

Use the local spectral-action form after auxiliary-field elimination:

```tex
V_F(\Phi)=\lambda_F\left(\langle\Phi,\Phi\rangle-v_F^2\right)^2.
```

Let:

```tex
\Phi=v_F\eta_0+\delta\Phi,
\qquad
\langle\eta_0,\eta_0\rangle=1.
```

Define the canonical radial coordinate:

```tex
h=\sqrt2\,{\rm Re}\,\langle\eta_0,\delta\Phi\rangle .
```

Then, to quadratic order:

```tex
V_F^{(2)}
=
2\lambda_Fv_F^2 h^2
=
{1\over2}m_H^2h^2,
\qquad
m_H^2=4\lambda_Fv_F^2.
```

The angular directions orthogonal to the radial mode are Goldstone directions
before gauge fixing. Thus the local finite potential has a positive radial
eigenvalue and angular zero modes at the selected vacuum.

Signature audit:

```text
finite Higgs-potential Hessian: positive radial block plus zero modes
```

## Gauge Hessian

The same vacuum vector gives the ordinary electroweak mass matrix through:

```tex
K_{ab}^{\rm gauge}
=
v_F^2\,g_ag_b\,
\langle T_a\eta_0,T_b\eta_0\rangle .
```

With:

```tex
T_3\eta_0=-{1\over2}\eta_0,
\qquad
Y\eta_0={1\over2}\eta_0,
```

the protected generator is:

```tex
Q=T_3+Y,
\qquad
Q\eta_0=0.
```

This yields:

```tex
M_W^2={g_2^2v_{\rm EW}^2\over4},
\qquad
M_Z^2={(g_2^2+g_Y^2)v_{\rm EW}^2\over4},
\qquad
M_\gamma^2=0,
\qquad
v_{\rm EW}=\sqrt2\,|v_F|.
```

This Hessian is the ordinary broken-gauge-sector mass matrix. It uses the
finite Connes sheet scale as its vacuum input.

## Schur Interface Hessian

The de Vries block uses an extra image/current variable:

```tex
n\in{\rm Im}\,A_j,
\qquad
A_j=\sum_aT_a^{(j)}\otimes e_a,
\qquad
A_j^\dagger A_j=J{\bf 1},
\qquad
J=j(j+1).
```

The dimensionless interface quadratic form is:

```tex
S_{\rm Schur}^{(2)}
=
\langle\delta\phi,A_j^\dagger n\rangle
+
\langle n,A_j\delta\phi\rangle
-
\langle n,A_jA_j^\dagger n\rangle .
```

On the normalized source/image basis:

```tex
t_j\in V_j,
\qquad
n_j={1\over\sqrt J}A_jt_j,
```

the matrix is:

```tex
{\cal H}_j
=
\begin{pmatrix}
0&\sqrt J\\
\sqrt J&-J
\end{pmatrix}.
```

For the Connes Higgs doublet:

```tex
j={1\over2},
\qquad
J={3\over4},
```

so:

```tex
{\cal H}_{1/2}
=
\begin{pmatrix}
0&\sqrt3/2\\
\sqrt3/2&-3/4
\end{pmatrix}.
```

Signature audit:

```tex
\det{\cal H}_j=-J,
\qquad
{\rm tr}\,{\cal H}_j=-J.
```

For `J>0`, the Schur interface Hessian is indefinite. Direct identification
with the finite Higgs-potential Hessian is rejected by signature.

## Relation Between The Three Objects

The finite Higgs potential supplies:

```text
radial scalar mass M_H
Goldstone directions for the broken gauge generators
finite sheet-distance scale ell_H=1/|v_F|
```

The gauge Hessian supplies:

```text
W/Z/photon masses from the Q-neutral vacuum vector
```

The Schur interface Hessian supplies:

```text
the de Vries branch operator on V_j plus Im A_j
```

They are related through the same vacuum vector and the same weak orbit:

```tex
\eta_0
\quad\longmapsto\quad
A_{1/2}\eta_0
\quad\longmapsto\quad
J_{\rm branch}={3\over4}.
```

The equality demanded by the project is therefore a common-vacuum and
common-normalization condition:

```tex
P_{1/2}{\cal M}^2P_{1/2}
=
\mu_*^2{\cal H}_{1/2},
```

where:

```tex
{\cal M}^2=Z^{-1}K
```

is computed from the full D10/finite scalar system.

## KK Coupling Pattern

A minimal coupled scalar potential has the form:

```tex
V_{\rm eff}
=
V_{\rm KK}(\rho,\lambda,\theta_H)
+
V_F(v_F)
+
V_{\rm int}(\rho,\lambda,\theta_H,v_F,n).
```

The stationary point satisfies:

```tex
\partial_\rho V_{\rm eff}=0,
\qquad
\partial_\lambda V_{\rm eff}=0,
\qquad
\partial_{\theta_H}V_{\rm eff}=0,
\qquad
\partial_{v_F}V_{\rm eff}=0.
```

The Hessian has block form:

```tex
K=
\begin{pmatrix}
K_{\rm KK}&K_{\rm mix}\\
K_{\rm mix}^\dagger&K_F
\end{pmatrix}.
```

The bridge requires `K_mix` and the image/current sector to project to the
Schur form above. With all mixed entries set to zero, the Connes sheet scale
and KK shape scale become independent stationarity problems.

## Current Status

Closed calculation:

```text
finite local potential gives radial mass and Goldstone zeros
gauge Hessian gives W/Z/photon masses from Q eta_0=0
Schur interface Hessian has determinant -J and trace -J
direct finite-potential to Schur identification rejected by signature
```

Open calculation:

```text
derive V_int and K_mix from the selected D10 boundary/current action
derive mu_* and a=1 in the same normalization as ell_H and rho_*
embed the finite edge in the full determinant-one KO6 lift
```
