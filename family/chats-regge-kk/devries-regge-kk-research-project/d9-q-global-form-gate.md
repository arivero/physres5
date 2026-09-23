# D9 Q Global-Form Gate

## Purpose

The D9 endpoint must protect the photon as an exact zero mode. The
local Lie-algebra statement is:

```tex
Q=T_3+Y.
```

The global-form and line-operator statement is that the D10 interface
transports the Standard-Model diagonal quotient from the unbroken parent
to the electromagnetic endpoint.

## UV Global Form

Use integer hypercharge:

```tex
y=6Y.
```

The maximal Standard-Model global form is:

```tex
G_{\rm SM}
=
{SU(3)_c\times SU(2)_L\times U(1)_y\over Z_6}.
```

The diagonal generator can be represented as:

```tex
\zeta_6=
\left(
\omega_3,\,
-1,\,
e^{i\pi/3}
\right),
\qquad
\omega_3=e^{2\pi i/3}.
```

It acts trivially on the usual integer-hypercharge charge lattice:

| field type | `SU(3)` triality | `SU(2)` parity | `y=6Y` |
|---|---:|---:|---:|
| `q_L` | `1` | `1` | `1` |
| `u_R` | `1` | `0` | `4` |
| `d_R` | `1` | `0` | `-2` |
| `l_L` | `0` | `1` | `-3` |
| `e_R` | `0` | `0` | `-6` |
| Higgs-like doublet | `0` | `1` | `3` |

The lens/global-form clue must involve color, weak, and hypercharge
together. The full `Z_6` is a diagonal Standard-Model quotient.

## D9 Endpoint

After the interface/breaking layer selects:

```tex
Q=T_3+Y,
```

use integer electromagnetic charge:

```tex
q_3=3Q.
```

The D9 endpoint should have global form:

```tex
G_{D9}
=
{SU(3)_c\times U(1)_Q\over Z_3}.
```

A generator can be written as:

```tex
\zeta_3=
\left(
\omega_3,\,
e^{2\pi i/3}
\right),
```

where the `U(1)_Q` factor acts on the integer charge `q_3`.

This identifies the color center with an electromagnetic rotation. It
is what makes fractional quark charges compatible with color
confinement and integer color-singlet charges.

## Descent Of The Diagonal Quotient

For a surviving state with color triality:

```tex
t\in Z_3,
```

weak weight:

```tex
T_3=m,
```

and integer hypercharge:

```tex
y=6Y,
```

the UV generator acts by:

```tex
\zeta_6:
\qquad
\omega_3^t\,
\exp(i2\pi m)\,
\exp(i\pi y/3).
```

Since:

```tex
\exp(i\pi y/3)=\exp(i2\pi Y),
```

the electroweak part is:

```tex
\exp(i2\pi(m+Y))
=
\exp(i2\pi Q).
```

With:

```tex
q_3=3Q,
```

this is:

```tex
\exp(i2\pi q_3/3).
```

Therefore the image of the UV diagonal generator on the D9 endpoint is:

```tex
\zeta_6\mapsto
\zeta_3=(\omega_3,\exp(i2\pi/3)).
```

The cube is trivial on the D9 charge lattice:

```tex
\zeta_3^3=(1,\exp(i2\pi))=1.
```

Thus the residual global form is:

```tex
G_{D9}
=
{SU(3)_c\times U(1)_Q\over Z_3}.
```

Status:

```text
algebra-from-source charge-lattice descent. The D10 source of the UV
diagonal quotient remains a brane/current/line-operator gate.
```

## Photon Protection

The boundary/interface must implement:

```tex
SU(2)_L\times U(1)_Y
\to
U(1)_Q,
```

with:

```tex
Q=T_3+Y
```

preserved.

A Higgs-like doublet has:

```tex
T={1\over2},
\qquad
y=3,
\qquad
Y={1\over2}.
```

Its neutral component has:

```tex
T_3=-{1\over2},
\qquad
Q=0.
```

Therefore the photon gate requires the condensing or boundary-changing
datum to be neutral under `Q` and charged under the orthogonal
electroweak direction.

This is the global-form version of:

```tex
M_\gamma=0.
```

The Connes two-sheet calculation in
[d6-connes-o1-distance-calculation.md](d6-connes-o1-distance-calculation.md)
implements this boundary datum as:

```tex
\Phi:O(0)\to O(1),
\qquad
Q\Phi_0=0,
```

with sheet distance:

```tex
d_{\rm sheet}={1\over\|\Phi_0\|}.
```

The electroweak Hessian test in
[d6-connes-electroweak-hessian-test.md](d6-connes-electroweak-hessian-test.md)
adds:

```tex
Q\eta_0=0,
\qquad
M_\gamma^2=0,
\qquad
{M_W^2\over M_Z^2}={g_2^2\over g_2^2+g_Y^2}.
```

The effective D10-to-D9 carrier projection is recorded in
[k6-to-k5-q-collapse-map.md](k6-to-k5-q-collapse-map.md):

```tex
\Pi_Q:\ CP2\times CP1\to CP2\times S^1_Q.
```

## Connection To M^{pqr}

The source-backed D10 reduction gives:

```tex
S^1_Z\to M^{pqr}\to CP2\times CP1,
```

with retained Chern data:

```tex
c_1(S^1_Z)\sim p x+q y.
```

The current low-complexity control point has:

```tex
p:q=6:7,
```

so:

```tex
c_1(S^1_Z)\sim 6x+7y.
```

Modulo the Standard-Model `Z_6` datum:

```tex
6x+7y\equiv y\pmod 6.
```

This is a useful congruence hint: the weak/projective part is
unit-valued mod `6`, matching the `L(6,1)` flat-sector pattern.

Status: the control point is compatible with the global-form/lens clue
at the congruence level.

The period integer:

```tex
r=91
```

also satisfies:

```tex
r\equiv1\pmod6.
```

Open gate: derive the full line/operator lattice from the
RR/brane/current sector.

## Relation To Lens-Space Flat Sectors

The lens-space note showed that `L(6,1)` flat sectors can preserve:

```tex
T={1\over2}
```

and:

```tex
T=1
```

when the flat-sector character cancels the Hopf weight.

The D10 `CP1` line-bundle version is recorded in
[d10-cp1-line-bundle-interface.md](d10-cp1-line-bundle-interface.md):
`O(1)` carries `j=1/2`, `O(2)` carries `j=1`, and the control point
`q=7=1 mod 6` makes the retained `M^{pqr}` line a unit weak charge
modulo the same `Z_6` datum.

This note gives the complementary global-form requirement:

```text
the same Z6 datum must be the diagonal Standard-Model quotient.
```

So the D10 interface must combine:

- `M^{pqr}` RR/Chern data;
- `Z_6` line-operator or flat-sector data;
- an exact `Q`-neutral boundary/condensate;
- the D9 `Z_3` color-electromagnetic quotient.

## Pass/Fail Gate

Pass requires:

1. Build the UV charge lattice with integer `y=6Y`.
2. Gauge or identify the diagonal `Z_6` generated by `zeta_6`.
3. Show that the D10 interface preserves the required `T=1/2` and
   `T=1` sectors.
4. Show that the breaking datum is `Q`-neutral.
5. Derive the D9 global form:

```tex
{SU(3)_c\times U(1)_Q\over Z_3}.
```

6. Compute `L_Q/sqrt(G)` or the equivalent current/brane
   normalization.

Fail conditions:

- `Q` lacks boundary-condition protection;
- `L(6,1)` lacks coupling to color and hypercharge;
- the `Z_6` quotient projects out the required `T=1/2` channel;
- the congruences `p:q=6:7` and `r=91=1 mod 6` are treated as a
  prediction before a line/operator derivation;
- alpha is fit after the quotient.

## Current Verdict

The D9 endpoint is now constrained as:

```text
D11 parent:  SU(3)c x SU(2)L x U(1)Y with Z6 global form.
D10 bridge:  Type IIA on CP2 x CP1 plus RR/Chern and flat/current data.
D9 endpoint: exact (SU(3)c x U(1)Q)/Z3 with alpha from Q normalization.
```

This is a sharper target for the remaining interface construction.

## Selected-Package Check

The selected endpoint check is recorded in
[d10-selected-q-boundary-check.md](d10-selected-q-boundary-check.md).
For:

```tex
P:Q=6:7,
\qquad
(p,q,r,n)=(12,14,91,1),
```

it verifies:

```tex
Q\eta_0=0,
\qquad
M_\gamma=0,
```

and:

```tex
G_{D9}
=
{SU(3)_c\times U(1)_Q\over Z_3}.
```

It also records the selected alpha carrier:

```tex
{L_Q\over\sqrt G}=146.163962656024950.
```

Status: selected kinematic endpoint. The line/operator derivation and
finite/scalar vacuum remain open.
