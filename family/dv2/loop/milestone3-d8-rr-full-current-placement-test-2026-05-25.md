# Milestone 3 D8/RR full-current placement test -- 2026-05-25

## Question

Milestone 3 found two current metrics:

```tex
L_{2,BL}^2=L_{2,horiz}^2+L_{2,vert}^2
=(1+\beta)L_{2,horiz}^2 .
```

The de Vries branch needs the boundary image channel to use the full
Bailin-Love/Weinberg current frame, not only the horizontal `CP1` frame.  This
note tests whether the current D8/RR source package derives that placement.

## Metric consequence

If the boundary image channel uses the full current frame,

```tex
e_a={K_{a,full}\over L_{2,BL}},
\qquad
A_j^\dagger A_j=J_j,
```

then

```tex
\kappa_{\rm cur}=1.
```

If it uses only the horizontal `CP1` current while the gauge coupling uses the
full Bailin-Love length, then

```tex
\kappa_h={L_{2,horiz}^2\over L_{2,BL}^2}
={1\over1+\beta}
=0.7527390090748721 .
```

With `c=sqrt(kappa_h)=0.8676053302480755`, the current-metric-deformed pole

```tex
X^2+c^2JX-c^2J=0
```

gives

```tex
\sin^2\theta_W=0.24226537471822063.
```

So the horizontal-only placement does not reproduce the de Vries number.

## Payen endpoint source

The Payen boundary action couples the endpoint representation to the pullback
of an external Yang-Mills field:

```tex
R(A_\tau)=A_\tau^aT_a^{(j)} .
```

After the external connection is expressed in an orthonormal frame, the endpoint
charges give

```tex
\sum_aT_a^{(j)}T_a^{(j)}=J_j .
```

This proves the unit Casimir for whichever current frame is inserted.  It does
not decide whether the inserted connection is the horizontal `CP1` gauge field
or the full Bailin-Love current that includes the vertical parent-circle/RR
piece.

Decision: Payen fixes the representation tensor, not the full-current
placement.

## D8 WZ source

The D8-like WZ term has the schematic form

```tex
S_{WZ}=\mu_8\int_{W9} C\wedge{\rm ch}(E_Q)
\sqrt{\widehat A(TW9)/\widehat A(NW9)} .
```

It couples the D8 carrier to RR potentials and Chan-Paton Chern character data.
This is enough to tie the boundary carrier to the RR/Chern package and to the
spin-c charge accounting.

It does not by itself add the vertical length `L_{2,vert}` to the endpoint
current metric.  A topological WZ coupling fixes RR charge; it is not the
boundary kinetic norm that defines the orthonormal current frame in
`A_j^\dagger A_j`.

Decision: the current WZ skeleton supports the RR placement of the D8 carrier,
but it does not derive the full-current image metric.

## Result

The full-current branch is algebraically coherent:

```tex
K_{a,full}\quad\Longrightarrow\quad \kappa_{\rm cur}=1 .
```

The current D8/Payen/RR source package does not derive the premise that the
boundary image channel uses `K_{a,full}`.  With only the visible horizontal
`CP1` current, Milestone 3 gives the shifted weak angle above and fails the
de Vries test.

Current verdict:

```text
kappa_cur=1 is a full-current branch condition, not a derived consequence of
the written D8/RR boundary action.
```

To pass Milestone 3, the D10 action must add a source-backed mechanism that
identifies the endpoint current with the full parent current before reduction,
or an equivalent RR/current boundary kinetic term whose norm is `L_{2,BL}`.
