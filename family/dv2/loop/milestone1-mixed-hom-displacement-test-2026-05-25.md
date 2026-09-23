# Milestone 1 mixed Hom displacement test -- 2026-05-25

## Question

The current-displacement square test left one narrow finite-branch obstruction:
the boundary theory needs a field

```tex
Q_j\in{\rm Im}\,A_j\subset V_j\otimes{\bf R}^3
```

with local norm

```tex
\alpha\mu^2\|A_j^\dagger Q_j-p_j\|^2
-\alpha\mu^2\|p_j\|^2 .
```

The prior D8/Chan-Paton note contains a candidate mixed boundary-changing
sector

```tex
H^0(CP^1,{\rm Hom}({\cal O}(0),{\cal O}(2j)))
=H^0(CP^1,{\cal O}(2j))
=V_j .
```

This note tests whether that mixed Hom zero mode can be the missing image
displacement.

## Rank and metric test

For `j>0`, the current map is

```tex
A_j:V_j\to V_j\otimes{\bf R}^3,
\qquad
A_j^\dagger A_j=J_j{\bf 1}_{V_j},
\qquad
J_j=j(j+1)>0 .
```

Hence

```tex
U_j={1\over \sqrt{J_j}}A_j:V_j\to{\rm Im}\,A_j
```

is an isometry:

```tex
U_j^\dagger U_j={\bf 1}_{V_j},
\qquad
U_jU_j^\dagger=P_j={1\over J_j}A_jA_j^\dagger .
```

Therefore a mixed Hom mode

```tex
y_j\in V_j
```

does supply an image-bundle field after the canonical change of variables

```tex
Q_j=U_jy_j={1\over\sqrt{J_j}}A_jy_j .
```

The displacement seen by the open channel becomes

```tex
A_j^\dagger Q_j
=A_j^\dagger {A_jy_j\over\sqrt{J_j}}
=\sqrt{J_j}\,y_j .
```

Thus the desired square is equivalent to the Hom-sector square

```tex
\alpha\mu^2\|\sqrt{J_j}\,y_j-p_j\|^2
-\alpha\mu^2\|p_j\|^2 .
```

This is a real improvement over the bare normal-displacement test: the mixed
Hom sector has the right rank and becomes an `Im A_j` field through the
unitary map `A_j/sqrt(J_j)`.

For `j=0`, `A_0=0` and there is no image channel.  The construction above is
only for `j>0`; photon protection requires the `j=0` Hom constant to decouple
or enter only through terms proportional to `J_0`.

## Coefficient test

The mixed-sector field content alone does not fix the quadratic action.  The
most general local one-pole Hom-mode action with this tensor structure is

```tex
S_y^{(2)}
=\langle p_j,Bp_j\rangle
+Z_y\langle y_j,By_j\rangle
+c_m\mu^2J_j\langle y_j,y_j\rangle
-c_g\mu^2\sqrt{J_j}
 (\langle y_j,p_j\rangle+\langle p_j,y_j\rangle),
```

with `Z_y>0`.  Eliminating `y_j` gives

```tex
\Gamma_j(B)
=B-{c_g^2\mu^4J_j\over Z_yB+c_m\mu^2J_j}.
```

After setting

```tex
\mu_{\rm eff}^2={c_m\over Z_y}\mu^2,
\qquad
X={B\over\mu_{\rm eff}^2},
```

the pole equation is

```tex
X={r^2J_j\over X+J_j},
\qquad
r={c_g\sqrt{Z_y}\over c_m}.
```

The de Vries slice requires

```tex
r=1,
\qquad
c_m=c_g\sqrt{Z_y}.
```

If `y_j` is canonically normalized, this reduces to `c_m=c_g`.  The single
Hom displacement square above enforces this condition.  A generic mixed
Chan-Paton quadratic form does not.

## Decision

The mixed Hom sector passes the field-content test:

```text
y_j in H^0(CP1,Hom(O(0),O(2j))) = V_j
```

is equivalent, for `j>0`, to an image displacement

```text
Q_j = A_j y_j / sqrt(J_j) in Im A_j.
```

It does not by itself pass the action test.  The zero-mode statement gives the
right finite vector bundle, but it does not derive the local norm

```tex
\|\sqrt{J_j}\,y_j-p_j\|^2
```

or the coefficient lock `c_m=c_g sqrt(Z_y)`.

Therefore the finite branch is still not a proof of de Vries.  Its strongest
local route is now sharper:

```text
derive the mixed Hom boundary-changing mode as a DBI/Stueckelberg displacement
whose quadratic action is one local norm, with the current frame normalized by
the full D10 metric.
```

If that one-square Hom action is derived, the finite branch gets the required
`Im A_j` displacement and the residue lock.  If the mixed-sector action has
independent `Z_y,c_m,c_g`, the weak-angle relation is shifted by `r` and the
D10 construction remains compatible rather than predictive.
