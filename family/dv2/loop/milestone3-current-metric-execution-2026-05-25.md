# Milestone 3 current-metric execution -- 2026-05-25

## Milestone question

Milestone 3 asks whether the full D10 carrier computes the same current metric
for both:

- the weak gauge coupling;
- the boundary image map in the Feshbach/Schur channel.

If these are the same metric, then `kappa_cur=1` is not a tunable parameter.

## KK metric calculation

Let `K_a` be the weak current generators and define

```tex
G_{ab}^{(2)}
= {1\over Vol(\widehat K_6)}
\int_{\widehat K_6}\sqrt g\,g(K_a,K_b).
```

On the `SU(2)`-symmetric weak line,

```tex
G_{ab}^{(2)}=L_2^2\delta_{ab}.
```

The normalized current frame is

```tex
e_a={K_a\over L_2},
\qquad
\langle e_a,e_b\rangle=\delta_{ab}.
```

Therefore the boundary image map

```tex
A_jp=\sum_aT_a^{(j)}p\otimes e_a
```

satisfies

```tex
A_j^\dagger A_j
=\sum_aT_a^{(j)}T_a^{(j)}
=j(j+1).
```

This part of the calculation passes: once the boundary channel uses the same
orthonormal current frame as the KK gauge metric, `kappa_cur=1`.

## Round `CP1` control

For a round weak `CP1 ~= S2` with radius `R_w`,

```tex
{1\over Vol(CP1)}
\int_{CP1}\sqrt g\,g(K_a,K_b)
={2\over3}R_w^2\delta_{ab}.
```

Thus

```tex
L_{2,horiz}^2={2\over3}R_w^2.
```

For a one-shape product metric

```tex
ds^2_{K6}=\ell^2(ds^2_{CP2}+\lambda ds^2_{CP1}+\cdots),
```

this gives

```tex
L_{2,horiz}^2={2\over3}\ell^2\lambda R_0^2.
```

## Bailin-Love split

Bailin-Love gives the weak-isospin coupling in the parent as

```tex
g_2^2
=3\kappa^2(2b^{-2}+q^2c^{-2})^{-1}.
```

Using Weinberg's length convention,

```tex
g_2^2={4\pi^2\kappa^2\over L_2^2},
```

the inherited total weak length is

```tex
L_{2,BL}^2
={4\pi^2\over3}(2b^{-2}+q^2c^{-2}).
```

With

```tex
b=\gamma\sqrt{2\beta},
\qquad
c=q\gamma,
```

this becomes

```tex
L_{2,BL}^2
={4\pi^2\over3\gamma^2}{1+\beta\over\beta}.
```

Split it as

```tex
L_{2,horiz}^2={4\pi^2\over3\gamma^2}{1\over\beta},
\qquad
L_{2,vert}^2={4\pi^2\over3\gamma^2}.
```

Thus

```tex
L_{2,BL}^2=(1+\beta)L_{2,horiz}^2.
```

For the selected parent value

```tex
\beta=0.328481702082924367895293909852,
```

one has

```tex
{L_{2,horiz}^2\over L_{2,BL}^2}=0.7527390090748721,
\qquad
{L_{2,vert}^2\over L_{2,BL}^2}=0.24726099092512785.
```

## Current-metric consequence

There are two possibilities.

### Full-current boundary coupling

If the D8 endpoint/current channel couples to the full current generator whose
metric length is `L_{2,BL}`, then

```tex
e_a={K_{a,full}\over L_{2,BL}},
\qquad
A_j^\dagger A_j=J_j.
```

In that case

```tex
kappa_cur=1.
```

The vertical RR/current contribution changes the gauge coupling through the
total length.  It does not deform the normalized current Casimir.

### Horizontal-only boundary coupling

If the boundary image channel sees only the horizontal `CP1` current while the
weak gauge coupling uses the total Bailin-Love length, then the image metric is

```tex
\kappa_{h}
={L_{2,horiz}^2\over L_{2,BL}^2}
={1\over 1+\beta}
=0.7527390090748721.
```

The corresponding pole parameter is

```tex
c=\sqrt{\kappa_h}=0.8676053302480755.
```

In the current-metric deformation

```tex
X^2+c^2JX-c^2J=0,
```

this gives

```tex
\sin^2\theta_W=0.24226537471822063.
```

This is not the de Vries value.  Thus a horizontal-only boundary image channel
fails Milestone 3.

## Execution decision

Milestone 3 has a sharp outcome:

```text
The current metric passes only if the D8 boundary image channel couples to the
full Bailin-Love/Weinberg weak current, including the vertical RR/current
piece.
```

On that branch, `kappa_cur=1` follows from normalization and should be removed
from the physical moduli list.  On the horizontal-only branch, the computed
factor is `kappa_cur=0.7527390090748721`, which misses the de Vries weak
angle.

## New dependency

Milestone 3 therefore feeds back into Milestone 1 and Milestone 6:

- Milestone 1 must derive the boundary-current oscillator using the full
  current generator, not only the `CP1` horizontal current.
- Milestone 6 must check that the D8/RR Wess-Zumino and boundary coupling
  actually place the vertical current piece in the endpoint image channel.

This does not revive Milestone 2 as a blocker.  The representation assignment
can remain deferred; the metric test applies to any spin `j`.
