# Alpha_EM Prediction And Historical Status

## Short Answer

Yes, in principle:

```text
if the compactification/vacuum fixes the absolute Q normalization,
then alpha_EM is predicted.
```

Status: the 1980s `M^{pqr}` literature left that job open. It mostly
computed classical compactification-scale coupling ratios and then found
that the source matches failed under their assumptions.

## What Was Published

The relevant pieces were published:

- Weinberg gave the rms-circumference prescription for gauge couplings
  from compact extra dimensions.
- Bailin and Love applied that logic to the `M^{pqr}` family and
  computed coupling-constant ratios.
- Ezawa and Koh tested D=11 `SU(3) x SU(2) x U(1)` couplings against
  strong/electroweak expectations and reported a severe mismatch.

So the suspicious fact is that physicists published the right type of
machinery and the program still stalled.

The gap is the realistic electroweak vacuum.

## Ratios Versus Alpha

Bailin-Love mainly gives ratios such as:

```tex
{g_Y^2\over g_2^2}.
```

That is enough to test a weak angle. It is insufficient for predicting:

```tex
\alpha_{\rm EM}={e^2\over4\pi}.
```

For alpha, the absolute generator norm is needed.

Using Weinberg normalization:

```tex
g_2={C\over L_2},
\qquad
g_Y={C\over L_Y},
\qquad
C=2\pi\sqrt{16\pi G}.
```

After electroweak breaking:

```tex
e={g_2g_Y\over \sqrt{g_2^2+g_Y^2}},
```

so:

```tex
{1\over e^2}
={1\over g_2^2}+{1\over g_Y^2}
={L_2^2+L_Y^2\over C^2}.
```

Therefore:

```tex
\alpha_{\rm EM}
={16\pi^2G\over L_2^2+L_Y^2}.
```

Equivalently:

```tex
L_Q^2=L_2^2+L_Y^2.
```

This is why alpha becomes predictable when the vacuum fixes the
absolute size of the `Q` generator beyond the ratio `L_Y/L_2`.

## Role Of The Electroweak Vacuum

An electroweak vacuum would have to supply:

```tex
SU(2)_L\times U(1)_Y \to U(1)_Q,
```

with:

```tex
Q=T_3+Y,
\qquad
M_\gamma=0.
```

It must also fix:

```tex
L_2,\qquad L_Y,\qquad L_Q,
```

or their string-current analogues.

For the source `M^{pqr}` parent, the `T_3,Y` mixed norm vanishes by the
orthogonality argument in
[mpqr-cartan-orthogonality.md](mpqr-cartan-orthogonality.md), so:

```tex
L_Q^2=L_2^2+L_Y^2.
```

That simplifies the parent alpha gate while leaving the absolute
scale.

The Higgs vev `v` sets:

```tex
M_W={g_2v\over2},
\qquad
M_Z={\sqrt{g_2^2+g_Y^2}\,v\over2},
```

The electromagnetic coupling comes from the normalized surviving
generator, and the Higgs mass comes from radial curvature of the same
vacuum sector:

```tex
M_H^2={1\over Z_H}
{\partial^2 V_{\rm eff}\over\partial h^2}\bigg|_*.
```

So the project needs:

```text
vacuum/interface -> generator norms and Q
+ finite-direction minimum and curvature -> v and M_H
+ branch quotient -> W/Z mass ratio.
```

## Why This Was Not Already The Standard Model

There are several hard reasons.

### 1. The Source Ratios Were Insufficient

Bailin and Love explicitly state that satisfactory agreement, even at
the approximate level they considered, required `r > 1` for `M^{pqr}`
with both `p` and `q` nonzero; in their classification context this
makes the manifold non-simply connected.

That remains compatible with the present project, because global
quotients and flat sectors are now part of the candidate mechanism. It
also explains why the classical model stalled.

### 2. The Labels Remain Unselected

The present scan shows many close weak-angle hits because:

```tex
{g_Y^2\over g_2^2}=F(q/p){p^2n^2\over r^2}.
```

The integers `p,q,r,n` give too much freedom unless another principle
selects them.

This is why [mpqr-k6-selector-gates.md](mpqr-k6-selector-gates.md)
is now central.

### 3. Chirality And Fermions Are Hard

The D=11 KK setting can give `SU(3) x SU(2) x U(1)`-like gauge data,
while a realistic chiral fermion spectrum is a separate obstruction.

Any branch, lens, defect, or current-sector trick must be tested against
that problem.

### 4. No Electroweak Breaking Layer

The Freund-Rubin `M^{pqr}` parent is an unbroken gauge compactification.
It lacks:

```tex
v,\quad M_H,\quad M_W,\quad M_Z,\quad U(1)_Q.
```

Those require the lower-dimensional interface or vacuum.

### 5. Running And Thresholds Matter

The compactification calculation gives high-scale bare or effective
couplings. The measured electromagnetic coupling depends on the
renormalization scale and threshold corrections.

A serious comparison must specify:

```text
compactification scale -> running -> electroweak or infrared scale.
```

## What Would Count As A Real Prediction

A real prediction would require all of:

1. Select `p,q,r,n` from geometry or string/current consistency.
2. Compute `L_2` and `L_Y` with their absolute normalization.
3. Construct the breaking/interface sector selecting exact `Q`.
4. Compute `L_Q^2=L_2^2+L_Y^2` or the corrected non-diagonal norm.
5. Run the resulting couplings to the comparison scale.
6. Produce `M_W`, `M_Z`, `M_H`, `v`, and `alpha_EM` from the same
   vacuum data.

Until then, the correct status is:

```text
published classical coupling-ratio machinery,
pre-Standard-Model-vacuum.
```

## Project Consequence

The promising part is that the old machinery computes the right kind of
objects.

The missing part is mechanism:

```text
branched/projective K6 selector
+ D10 Regge/current interface
+ D9 Q normalization
+ electroweak vacuum.
```

If those are built, alpha can be predicted. Without them, the weak-angle
matches remain adjustable ratios.
