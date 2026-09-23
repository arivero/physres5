# Regge Evidence Memo

## Verdict

Verdict for a direct de Vries-Regge identification: `rejected`.

Verdict for Regge as a moduli selector: `partial pass`.

The source-backed Regge object is a string trajectory:

```tex
J=\alpha_0+\alpha' t
```

with possible string-loop and background corrections. The de Vries
quadratic is a finite internal two-channel block. The useful connection
is therefore:

```text
Regge/string tower in D10
+ finite internal SU(2) current block
+ D9 electroweak boundary.
```

The operational selector supplied by the Regge leg is:

```text
D10 interface must contain an SU(2)_2 current sector, or an equivalent
finite current algebra, whose retained spins are j=0,1/2,1.
```

Open gate: derive the `M^{pqr}` labels and the absolute normalization
from that same current/brane/flux sector.

## Sources Read

### S-Regge-1

L. A. Pando Zayas, J. Sonnenschein, and D. Vaman,
`Regge Trajectories Revisited in the Gauge/String Correspondence`,
arXiv:hep-th/0311190.

Local file:

```text
references/regge-string/pando-zayas-sonnenschein-vaman-2004-regge-trajectories-revisited.pdf
```

Use in this memo: definition of Regge trajectory, open/closed spinning
string trajectories, and corrected string trajectory in confining
backgrounds.

### S-Regge-2

P. Bouwknegt, A. W. W. Ludwig, and K. Schoutens,
`Spinon basis for higher level SU(2) WZW models`,
arXiv:hep-th/9412108.

Local file:

```text
references/regge-string/bouwknegt-schoutens-ludwig-1995-spinon-basis-su2-wzw.pdf
```

Use in this memo: affine `SU(2)_k` current algebra, integrable module
range, and conformal dimension:

```tex
\Delta(j)={j(j+1)\over k+2}.
```

## Regge Source Facts

Pando Zayas-Sonnenschein-Vaman state the Chew-Frautschi form as:

```tex
J=\alpha_0+\alpha' t.
```

For a classical open spinning string in flat space, their equation
(2.4) gives:

```tex
J=\alpha' E^2=\alpha' t.
```

For a classical closed spinning string in flat space, their equation
(2.7) gives:

```tex
J={\alpha'\over2}E^2.
```

For a closed spinning string in a confining supergravity background,
their equation (2.30) gives:

```tex
J={\alpha'_{\rm eff}\over2}t.
```

Their abstract summarizes the corrected trajectory as:

```tex
J\equiv\alpha(t)=\alpha_0+\alpha' t+\beta\sqrt t.
```

Their equation (5.22) gives the same square-root structure in energy
language:

```tex
J={1\over2}\alpha'_{\rm eff}E^2
-\alpha'_{\rm eff}z_0E
{+}{1\over2}\alpha'_{\rm eff}z_0^2.
```

Source-backed conclusion:

```text
Regge theory supplies a string trajectory and intercept data. It does
not supply the de Vries two-root internal block as a standalone
trajectory.
```

Status: direct de Vries-Regge identity rejected.

## SU(2)_k Source Facts

Bouwknegt-Ludwig-Schoutens define the affine `su(2)` current algebra at
level `k` in their equation (2.1):

```tex
[J_m^a,J_n^b]
=
f^{ab}{}_cJ_{m+n}^c
+km\delta_{m+n}d^{ab}.
```

They state that the integrable highest weight modules are labelled by:

```tex
j=0,{1\over2},1,\ldots,{k\over2}.
```

They give the conformal dimension in equation (2.5):

```tex
\Delta(j)={j(j+1)\over k+2}.
```

Setting `m=n=0` in the affine current algebra removes the central term:

```tex
[J_0^a,J_0^b]
=
f^{ab}{}_cJ_0^c.
```

Thus the zero modes are the ordinary finite `SU(2)` generators on each
spin-`j` primary module:

```tex
J_0^a|_{L_j}=T_a^{(j)},
\qquad
\sum_aT_a^{(j)}T_a^{(j)}
=
j(j+1){\bf 1}_{V_j}.
```

At:

```tex
k=2,
```

the allowed set is:

```tex
j=0,{1\over2},1.
```

This is exactly the finite set needed by the de Vries weak slots:

```text
photon slot, W slot, Z slot.
```

Source-backed conclusion:

```text
SU(2)_2 is the preferred Regge/current selector for the D10 interface.
```

Status: source-backed finite current-algebra filter.

Normalization consequence:

```tex
\Delta_j={J\over k+2}
\quad\Rightarrow\quad
c_{L0}={1\over\sqrt{k+2}}.
```

At `k=2`, direct conformal-weight normalization gives:

```tex
c_{L0}={1\over2}.
```

Using the Regge-compatible block:

```tex
Q_J(c)
=
\begin{pmatrix}
0&c\sqrt J\\
c\sqrt J&-c^2J
\end{pmatrix},
```

the direct `L0` coefficient gives:

```tex
\tan^2\theta_{\rm pole}(c=1/2)
=
0.4314539065631521.
```

Thus the Regge/WZW leg selects the finite set and supplies a controlled
Regge-compatible normalization. Exact de Vries requires the D10
interface to use the zero-mode/holonomy metric, equivalently:

```tex
A_j=\sqrt{k+2}\,A_{L0,j},
\qquad
A_j^\dagger A_j=J{\bf 1}_{V_j}.
```

The zero-mode algebra supplies this unit Casimir. The remaining D10
gate is action placement: the target-space mass operator has to couple
to `J_0^a` or the equivalent holonomy differential.

## Operational Selector

Apply this selector before arithmetic fitting of `M^{pqr}` labels.

### Selector R1: D10 Current Sector

Admissible D10 interfaces must contain:

```tex
SU(2)_2
```

or a source-backed equivalent current sector with retained spins:

```tex
j=0,{1\over2},1.
```

Candidates with a generic infinite `S^3` harmonic tower receive lower
priority unless a projection derives the same finite set.

### Selector R2: Casimir Normalization

The current zero modes must act on the retained sectors as:

```tex
A_j=\sum_{a=1}^3T_a^{(j)}\otimes e_a,
\qquad
A_j^\dagger A_j=j(j+1){\bf 1}_{V_j}.
```

The same inner product must be used in the Schur block and in the D9
coupling-normalization calculation.

### Selector R3: Regge-Compatible Block

For a two-channel internal block:

```tex
Q_J(a,b)
=
\mu^2
\begin{pmatrix}
0&a\sqrt J\\
a\sqrt J&-bJ
\end{pmatrix},
```

Regge priority selects:

```tex
b=a^2.
```

Exact de Vries selects the stronger condition:

```tex
a=1.
```

Status: algebraic selector. Open gate: derive `a=1` from the D10
current/brane normalization.

### Selector R4: Label Selection

The `M^{pqr}` label selector must be compatible with the same current
sector. The current arithmetic target:

```tex
p:q:r:n=12:14:91:1
```

passes the numerical weak-angle test. It remains a target until
`q/p`, `r/n`, and `rho_*` are derived from the Regge/current interface,
flux data, or vacuum extremum.

## Run Against The Current Candidate

| Item | Result | Status |
|---|---|---|
| `K7=M^{pqr}` D11 parent | Compatible with the D11 source-backed KK parent. | source-backed via KK memo |
| `K6=CP2 x CP1` | Compatible with a D10 string/current interface because `CP1` carries `SU(2)` line-bundle sectors. | source-backed plus algebra-from-source |
| `O(0),O(1),O(2)` | Matches the required `j=0,1/2,1` set. | algebra-from-source |
| `SU(2)_2` current layer | Regge selector picks it as the preferred finite current sector. | source-backed filter, construction open |
| `A_j` Schur block | Algebra matches the Regge-compatible `b=a^2` locus. | internal-conjecture normal form |
| `a=1` | Required for exact de Vries. | open gate |
| `p:q:r:n=12:14:91:1` | Fits weak-angle target. | internal-conjecture selector target |
| `rho_*=9.463469757` | Required alpha scale for that target. | open vacuum gate |

## Selector Consequences

1. The Regge leg keeps the D10 layer load-bearing.
2. The preferred D10 object is a string/current interface with
   `SU(2)_2` content.
3. The `CP1` line-bundle weak sector survives the Regge filter.
4. The arithmetic selector files remain target-generation notes until
   the `SU(2)_2` current or a linked brane/flux sector derives their
   integers.
5. The closure calculation is:

```tex
\Pi_j{\cal D}_{K6}\Pi_j
=
\mu^2
\begin{pmatrix}
0&\sqrt{j(j+1)}\\
\sqrt{j(j+1)}&-j(j+1)
\end{pmatrix}
```

with the same normalization that gives:

```tex
{L_Q\over\sqrt G}=146.16396265602495.
```

## Current Verdict For The Goal

The Regge evidence supports the current constructive branch:

```text
M^{pqr} D11 parent
-> Type IIA / current D10 interface on CP2 x CP1
-> SU(2)_2-compatible weak sector over CP1
-> D9 Q boundary.
```

The Regge evidence also sharpens the main open gate:

```text
derive the SU(2)_2 current normalization, M^{pqr} label selector,
and D9 alpha normalization from one interface/vacuum sector.
```

Goal status: candidate structure found; electroweak parameters are
mapped as functions of selected data; production of the data remains
open.
