# Milestone 1 mixed Hom local-action source test -- 2026-05-25

## Question

The mixed Hom displacement test found the right finite field content:

```tex
y_j\in H^0(CP^1,{\rm Hom}({\cal O}(0),{\cal O}(2j)))=V_j,
\qquad
Q_j={1\over\sqrt{J_j}}A_jy_j\in{\rm Im}\,A_j .
```

This note tests whether the current source package derives the required local
one-square action

```tex
\alpha\mu^2\|\sqrt{J_j}y_j-p_j\|^2
-\alpha\mu^2\|p_j\|^2 .
```

## Payen endpoint action

The Payen boundary action attaches a group-valued endpoint variable `g(tau)` to
the open-string boundary.  Its coupling to an external Yang-Mills field is
first order on the boundary.  Quantization gives a representation `V_j`, and
the boundary path integral gives the Wilson loop

```tex
{\rm Tr}_{V_j}\,P_{\partial\Sigma}
\exp\left(i\int_{\partial\Sigma}A_\tau^aT_a^{(j)}d\tau\right).
```

Its first variation inserts `T_a`; its second variation inserts the ordered
charge product `T_aT_b`.  This is enough to produce the current tensor

```tex
A_j=\sum_aT_a^{(j)}\otimes e_a
```

and the connected current response.  It does not introduce a propagating
mixed Hom field `y_j`, a second-order kinetic term for `y_j`, or a potential
whose quadratic part is `||sqrt(J_j)y_j-p_j||^2`.

Decision: Payen supplies the representation and Wilson tensors, not the
one-square Hom displacement action.

## D8 DBI and WZ source terms

The D8-like source package has two different roles.

The DBI term can generate local norms for geometric brane displacements and
worldvolume fields.  The WZ term fixes RR charges through the Chan-Paton Chern
character and curvature correction.  These terms support the D8 carrier and the
mixed Chan-Paton bundle data, but the current written action contains no
quadratic term that identifies the mixed Hom zero mode with the mismatch
`sqrt(J_j)y_j-p_j`.

A standard covariant kinetic term for a mixed boundary-changing field has the
form

```tex
Z_y\langle D y_j,D y_j\rangle+m_y^2\langle y_j,y_j\rangle+\cdots .
```

Around `y_j=0`, this gives no algebraic `p_j-y_j` mixing.  Around a nonzero
`y_j` background, the gauge-boson mass is a Gram/Higgs term depending on the
chosen background vector; it is not the Feshbach denominator
`B+\mu^2J_j` with numerator `\mu^4J_j`.

Decision: the current DBI/WZ source package supplies the right kind of local
norm in other variables, but not the Hom square needed here.

## Generic local action check

If the mixed Hom sector is retained with the most general local quadratic form

```tex
S_y^{(2)}
=\langle p_j,Bp_j\rangle
+Z_y\langle y_j,By_j\rangle
+c_m\mu^2J_j\langle y_j,y_j\rangle
-c_g\mu^2\sqrt{J_j}
(\langle y_j,p_j\rangle+\langle p_j,y_j\rangle),
```

then elimination gives

```tex
\Gamma_j(B)
=B-{c_g^2\mu^4J_j\over Z_yB+c_m\mu^2J_j},
\qquad
r={c_g\sqrt{Z_y}\over c_m}.
```

The de Vries relation is recovered only at

```tex
c_m=c_g\sqrt{Z_y}.
```

The Payen endpoint source, D8 DBI term, and D8 WZ term do not impose this
relation in the current action.

## Decision

The mixed Hom candidate passes the bundle test but fails as a derivation from
the current source package.  The current D10 boundary action can be made
compatible with de Vries by adding the Hom one-square action, but it does not
force that action.

Milestone 1 therefore has the following current verdict:

```text
finite D10 boundary branch: compatible, not predictive, unless a new local
open-string field theory input derives the Hom one-square action.
```

This closes the current Hom source test.  The next non-dependent milestone work
is the D8/RR full-current placement required by Milestone 3.
