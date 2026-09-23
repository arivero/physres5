# M^{pqr} Weak-Angle Scan

## Purpose

This note tests whether the source-backed Bailin-Love coupling-ratio
formulas for `M^{pqr}` can hit the de Vries weak-angle target.

This is a filter on the D=11 parent. Model status requires an
independent selector and vacuum gate.

## Source Equations

Bailin and Love compute coupling-constant ratios for the seven-dimensional
`M^{pqr}` manifolds with nonzero `p`, `q`, and `r`.

For `p q != 0`, their Einstein metric parameter `beta` is the unique
positive root in:

```tex
0 < \beta < {1\over 2}
```

of:

```tex
4\beta^3
-6\beta^2
+\left({9\over4}+{q^2\over p^2}\right)\beta
-{1\over2}{q^2\over p^2}
=0.
```

Their ratio formulas are:

```tex
{g_3^2\over g_2^2}
=
{2(3-4\beta)^2(1+\beta)\over 9(2-3\beta)},
```

and:

```tex
{g_1^2\over g_3^2}
=
{27p^2n^2(2-3\beta)\over 4(1-2\beta)r^2},
```

where `n` is the integer entering their weak-hypercharge quantization.

Therefore:

```tex
{g_1^2\over g_2^2}
=
{3\over2}{p^2n^2\over r^2}
{(3-4\beta)^2(1+\beta)\over 1-2\beta}.
```

In this note `g_1` is read as the unbroken hypercharge coupling `g_Y`.

## De Vries Target

The de Vries weak-angle target recorded in
[charge-normalization-gate.md](charge-normalization-gate.md) is:

```tex
\sin^2\theta_{\rm dV}=0.2231013223008662,
```

```tex
\cos^2\theta_{\rm dV}=0.7768986776991338.
```

So:

```tex
\tan^2\theta_{\rm dV}
={g_Y^2\over g_2^2}
=0.2871691363429836.
```

## Sanity Check

The canonical `p=q=r=n=1` point gives:

```tex
\beta={1\over4},
```

```tex
{g_Y^2\over g_2^2}=15.
```

This is far from the de Vries target. Direct `M111` is therefore a
control case and fails the endpoint test.

## Scan Method

For each integer `p,q,n`, solve the cubic for `beta`, compute the
continuous value of `r` that would hit the de Vries target, and then
test nearby integer `r`.

The scan below imposed:

```text
1 <= p,q <= 80
1 <= n <= 6
1 <= r <= 1000
gcd(p,q,r)=1
```

The `gcd` condition is the standard "no common divisor" condition on
the `M^{pqr}` labels. It permits `p` and `q` to share a factor when
`r` removes the common divisor across the full triple.

## Best Hits In The Unselected Scan

| Relative error in `g_Y^2/g_2^2` | `p` | `q` | `r` | `n` | `beta` | `g_Y^2/g_2^2` | `g_3^2/g_2^2` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| `1.859e-07` | 39 | 45 | 883 | 3 | 0.323085485 | 0.287169189736 | 0.831814702 |
| `1.925e-07` | 43 | 70 | 411 | 1 | 0.434796905 | 0.287169081074 | 0.728640784 |
| `5.780e-07` | 51 | 64 | 803 | 2 | 0.361366231 | 0.287168970351 | 0.798205714 |
| `1.176e-06` | 19 | 60 | 339 | 1 | 0.486446976 | 0.287169474179 | 0.678999420 |
| `1.971e-06` | 32 | 13 | 883 | 4 | 0.037591919 | 0.287169702310 | 0.992129166 |
| `2.703e-06` | 12 | 14 | 91 | 1 | 0.328481702 | 0.287169912626 | 0.827218731 |
| `1.062e-05` | 22 | 22 | 159 | 1 | 0.250000000 | 0.287172184645 | 0.888888889 |
| `4.729e-04` | 2 | 4 | 23 | 1 | 0.461608107 | 0.287304931641 | 0.702595478 |

The low-denominator point:

```text
p:q:r:n = 12:14:91:1
```

is the most useful short-list entry because it matches at relative
error `2.7e-6` with `n=1` and moderate `r`.

The equivalent ratio:

```text
p:q = 6:7
```

is now supported by the D10 flag selector package recorded in
[d10-flag-discrete-selector-check.md](d10-flag-discrete-selector-check.md).
The support chain is:

```text
Z6 global form -> P=6
Regge weak unit O(1) -> Q=7
flag cubic -> r=Q(P+Q)=91
branch/spin-c lift -> p=2P, q=2Q
minimal hypercharge period -> n=1.
```

Status: strongest discrete selector candidate. The D10 action still
must derive the carrier, normalization, and lift.

## Interpretation

The unselected scan proves a narrow algebraic fact:

```text
The Bailin-Love M^{pqr} coupling-ratio formulas can approximate the
de Vries weak-angle target very closely.
```

Model status requires an independent selector.

The reason is simple: the integer `r` and the hypercharge integer `n`
give enough freedom that close rational approximations are expected.
Without an independent rule selecting `p,q,r,n`, the match is a fit.

Therefore the selection problem becomes the real KK problem:

```text
What geometric or string-frame rule selects the p:q ratio and the
circle/global quotient data?
```

## Consequence For The Branched K6 Route

The branched/projective clue is useful if it selects or
constrains the `M^{pqr}` integers.

The working possibility is:

```text
D11 parent:
  M^{pqr} supplies the unbroken SU(3) x SU(2) x U(1) coupling arena.

D10 interface:
  a projective/branched K6 reduction selects a circle or quotient,
  replacing the round S4/Hopf picture by CP2/RP2 branch data.

D9 endpoint:
  the surviving U(1)_Q generator has Weinberg rms normalization.
```

If the branched K6 interface fails to select `p,q,r,n`, the weak-angle
scan remains numerology.

## Regge Priority

Many `M^{pqr}` labels can approximate the weak-angle target. The project
objective says to prioritize Regge compatibility when moduli are
non-unique.

Apply this ranking:

1. Prefer labels admitting a legal D10 string/current interface.
2. Prefer interfaces preserving `j=1/2` and `j=1` in the same controlled
   field or current sector.
3. Prefer a two-channel operator on the Regge-compatible locus
   `a^2=b`.
4. Then rank by numerical closeness to `tan^2(theta_dV)`.

This makes the best numerical hit subordinate to the Regge/D10 selector.

## Current Verdict

`M^{pqr}` remains the best source-backed D=11 parent. Direct coupling
matching is non-unique.

The current best route is:

```text
M^{pqr} parent
-> branched/projective K6 selector
-> D10 string/current interface
-> D9 Q and alpha boundary.
```

The next gate is to derive the selector before any further integer scan.
