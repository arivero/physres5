# Hosotani Single-Coupling Gate

Date: 2026-05-26

## Purpose

Turn the gauge-Higgs steering rule into a local D10 calculation for the
single-coupling Schur premise.

Source anchors: Manton 1979, Hosotani 1983, and Hosotani-Mabe 2005 as recorded
in `literature-search.md`.

## Steering Expansion

Use a three-layer separation for each candidate Hosotani realization.

H1 holonomy algebra:

```tex
U_H={\cal P}\exp\left(
i\mu_\Gamma\int_{\gamma_H}\theta_H\,\omega_H\,n_H^aT_a^{(j)}
\right)
```

has to yield the pair

```tex
\delta U_H=i\mu_\Gamma n_H^aT_a^{(j)}\delta\theta_H,
\qquad
\delta^2U_H=-\mu_\Gamma^2n_H^an_H^bT_a^{(j)}T_b^{(j)}
\,\delta\theta_H^2.
```

H2 localized normalization:

```tex
(f_H^2)_{ab}
=
{1\over g_{10}^2}\int_{\Gamma_{\rm EW}}d\nu_\Gamma\,
G_\Gamma^{ss}e_a(s)e_b(s)
+(f_\partial^2)_{ab}
```

sets the four-dimensional field `varphi_H=f_H theta_H`, the holonomy scale
`mu_Gamma/f_H`, and the charge period `w_H`.

H3 scalar vacuum:

```tex
V_H(\theta_H)=\sum_{m\ge1}c_m\cos(mw_H\theta_H),
\qquad
\sum_{m\ge1}mw_Hc_m\sin(mw_H\theta_{H,*})=0,
```

has to give a finite value satisfying

```tex
|f_H\theta_{H,*}|=|v_F|={v_{\rm EW}\over\sqrt2}.
```

Every candidate row should record

```tex
(\gamma_H,\omega_H,n_H^a,(f_H^2)_{ab},w_H,\mu_\Gamma,c_m)
```

and the comparison with the Schur scale

```tex
\mu_*^2={M_Z^2\over X_+(2)}.
```

The full local scale comparison is:

```tex
\mu_{\Gamma,{\rm Schur}}^2
=\mu_*^2
={g_2^2+g_Y^2\over2X_+(2)}f_H^2\theta_{H,*}^2,
\qquad
\chi_H=
{2X_+(2)\mu_{\Gamma,{\rm Schur}}^2
\over
(g_2^2+g_Y^2)f_H^2\theta_{H,*}^2}
=1.
```

For the point-projector metric `f_H^2=Q f_Gamma^2/4`, this becomes:

```tex
\mu_{\Gamma,{\rm Schur}}^2
=
{Q(g_2^2+g_Y^2)\over8X_+(2)}
f_\Gamma^2\theta_{H,*}^2.
```

## Holonomy Tensor Algebra

Let `gamma_H` be a retained weak or boundary-current cycle.  Write the
canonically normalized Wilson-line fluctuation as

```tex
U_H(\xi)
=
{\cal P}\exp\left(
i\mu_\Gamma\int_{\gamma_H}\xi^a e_a\,T_a^{(j)}
\right),
```

with `e_a` the same current frame used in

```tex
A_j=\sum_aT_a^{(j)}\otimes e_a.
```

At the selected background,

```tex
{\partial U_H\over\partial \xi^a}\bigg|_0
=
i\mu_\Gamma T_a^{(j)},
\qquad
{\partial^2 U_H\over\partial \xi^a\partial\xi^b}\bigg|_0
=
-\mu_\Gamma^2 T_a^{(j)}T_b^{(j)}.
```

Contracting with an image-channel field `n=n^a e_a` gives

```tex
A_j^\dagger n
=
\sum_a n^aT_a^{(j)},
\qquad
\|A_j^\dagger n\|^2
=
\langle n,A_jA_j^\dagger n\rangle .
```

Therefore one Wilson expansion supplies

```tex
\alpha_{\rm mix}=\mu_\Gamma,
\qquad
\beta_{\rm diag}=\mu_\Gamma^2,
\qquad
\beta_{\rm diag}/\alpha_{\rm mix}^2=1.
```

After the common physical factor is removed, the Schur coefficient condition
is reached.

## Pure Q-Circle Test

For the electromagnetic stabilizer cycle,

```tex
U_Q(\theta)=\exp(i\theta Q),
\qquad Q\eta_0=0.
```

Thus

```tex
{\partial U_Q\eta_0\over\partial\theta}\bigg|_0=0,
\qquad
{\partial^2 U_Q\eta_0\over\partial\theta^2}\bigg|_0=0.
```

The pure `S1_Q` holonomy supplies photon protection and zero Schur insertion
on the neutral finite section.  The Hosotani scalar has to live on a retained
transverse weak/current cycle or on a Chan-Paton boundary-complex cycle whose
image projects to the `e_a` frame.

## Candidate Cycle Data

The D10 calculation has to choose `gamma_H` from:

- the weak `CP1`/flag fibre before the `Q` projection;
- a Chan-Paton endpoint loop with `SU(2)` representation `V_j`;
- a boundary-complex cycle coupled to the neutral line `L_N`;
- a mixed RR/current cycle whose pullback enters `theta_Gamma^a`.

The same choice has to provide:

```tex
Q\eta_0=0,
\qquad
A_j^\dagger A_j=j(j+1),
\qquad
\beta_{\rm diag}/\alpha_{\rm mix}^2=1,
```

and a finite periodic potential

```tex
V_H(\theta_H)=\sum_m c_m\cos(m\theta_H)
```

with a stationary value compatible with the Connes sheet length

```tex
\ell_H=\sqrt2/v_{\rm EW}.
```

## Local D10 Data

The concrete Hosotani pass is the five-tuple

```tex
(\gamma_H,\omega_H,n_H^a,(f_H^2)_{ab},w_H).
```

Here `omega_H` is a one-form or endpoint profile normalized by

```tex
\int_{\gamma_H}\omega_H=1,
```

and `n_H^a e_a` is the current-frame direction retained by the scalar mode.
Near `Gamma_EW`, use the local ansatz

```tex
A_{\rm int}|_\Gamma
=
A_{\rm int}^{(0)}
+\theta_H(x)\,\omega_H\,n_H^aT_a^{(j)}.
```

The kinetic matrix is

```tex
(f_H^2)_{ab}
=
{1\over g_{10}^2}
\int_{\Gamma_{\rm EW}}d\nu_\Gamma\,
G_\Gamma^{ss}\,e_a(s)e_b(s)
+(f_{\partial}^2)_{ab}.
```

Pass condition on the Schur channel:

```tex
(f_H^2)_{ab}=f_H^2\delta_{ab}
```

up to the common multiplier removed by canonical normalization.  A
non-diagonal kinetic matrix can pass when its eigenframe also gives

```tex
A_j^\dagger A_j=J.
```

The period is charge-lattice data.  If the coupled spectrum has integer
charges `w_s` on `gamma_H`, set

```tex
w_H=\gcd\{w_s\},
\qquad
\theta_H\sim\theta_H+{2\pi\over w_H}.
```

The neutral vector `eta_0` represents the unitary-gauge component.  The full
cycle assignment still has to carry the electroweak doublet before the
`Q`-neutral projection.

## Point-Projector Current Metric

The point-evaluation filtration on `H^0(CP1,O(Q))` gives a concrete local
current-frame test.  With `J_Q=Q/2`, highest vector `|0>=|J_Q,J_Q>`,
rank-one projector `P_p=|0><0|`, and `K_p=1-P_p`, define

```tex
G_{ab}^{(p)}
=
{\rm Re}\,\langle0|T_aK_pT_b|0\rangle .
```

Using

```tex
T_1={1\over2}(T_++T_-),
\qquad
T_2={1\over2i}(T_+-T_-),
\qquad
T_-|0\rangle=\sqrt Q\,|J_Q,J_Q-1\rangle,
```

gives

```tex
G_{ab}^{(p)}
=
{Q\over4}
{\rm diag}(1,1,0).
```

Thus the boundary point selects the two weak directions transverse to the
stabilizer and gives an equal transverse metric.  The D10 density supplies the
common scale, and canonical normalization preserves
`beta_diag/alpha_mix^2=1`.

Writing the common localized density factor as `f_Gamma^2` gives:

```tex
f_{H,\perp}^2=f_\Gamma^2{Q\over4},
\qquad
f_{H,\perp}={\sqrt Q\over2}f_\Gamma.
```

For holonomy scale `mu_Gamma`, the normalized coefficients are:

```tex
\alpha_{\rm mix}={2\mu_\Gamma\over\sqrt Q f_\Gamma},
\qquad
\beta_{\rm diag}={4\mu_\Gamma^2\over Q f_\Gamma^2},
\qquad
{\beta_{\rm diag}\over\alpha_{\rm mix}^2}=1.
```

## Canonical Normalization Map

Write the localized quadratic action for the Wilson variable as

```tex
S_{\Gamma,H}^{(2)}
=
\int_{M_4}{1\over 2} f_H^2(\partial_\mu\theta_H)^2
+
Z_\Gamma\left[
\alpha_{\rm mix}\,{\rm Re}\langle a,A_j\phi\rangle
-
\beta_{\rm diag}\langle\phi,A_j^\dagger A_j\phi\rangle
\right].
```

The D10 calculation has to express

```tex
f_H^2
=
{1\over g_{10}^2}\int_{\Gamma_{\rm EW}}
d\nu_\Gamma\,|e_H|^2
\quad{\rm plus\ localized\ boundary\ terms},
```

and then set the canonically normalized field through

```tex
\varphi_H=f_H\,\theta_H,
\qquad
\phi=\varphi_H\,\eta_0 .
```

The same normalization has to appear in the linear and quadratic Wilson
insertions.  A successful calculation therefore produces

```tex
\alpha_{\rm mix}={\mu_\Gamma\over f_H},
\qquad
\beta_{\rm diag}={\mu_\Gamma^2\over f_H^2},
\qquad
{\beta_{\rm diag}\over\alpha_{\rm mix}^2}=1.
```

Coefficient-level version of the single-coupling Schur premise.

## Periodicity And Potential

The Wilson variable is angular:

```tex
\theta_H\sim\theta_H+{2\pi\over w_H}.
```

The localized sector should therefore give a Fourier potential

```tex
V_H(\theta_H)
=
\sum_{m\geq 1}c_m\cos(m w_H\theta_H)
```

with stationary equation

```tex
\sum_{m\geq 1}m w_H c_m\sin(m w_H\theta_H)=0.
```

For the minimal two-harmonic test, set `x=w_H theta_H` and

```tex
V_H=c_1\cos x+c_2\cos(2x).
```

The interior stationary branch is:

```tex
\cos x_*=-{c_1\over4c_2},
\qquad c_2>0,
\qquad |c_1|<4c_2.
```

Matching the finite-sheet value gives:

```tex
x_*={w_H v_{\rm EW}\over\sqrt2 f_H},
\qquad
{c_1\over c_2}=-4\cos\left({w_H v_{\rm EW}\over\sqrt2 f_H}\right).
```

The canonical curvature is:

```tex
m_\theta^2
=
{1\over f_H^2}\partial_{\theta_H}^2V_H|_*
=
{4w_H^2c_2\over f_H^2}\sin^2x_*.
```

The full-curvature specialization `m_theta^2=M_H^2` gives:

```tex
c_2={M_H^2f_H^2\over4w_H^2\sin^2x_*},
\qquad
c_1=-{M_H^2f_H^2\over w_H^2}{\cos x_*\over\sin^2x_*}.
```

With `M_H^2=2 lambda_F v_EW^2`:

```tex
c_2={\lambda_Fv_{\rm EW}^2f_H^2\over2w_H^2\sin^2x_*},
\qquad
c_1=-{2\lambda_Fv_{\rm EW}^2f_H^2\over w_H^2}
{\cos x_*\over\sin^2x_*}.
```

Eliminating `f_H` through

```tex
f_H={w_Hv_{\rm EW}\over\sqrt2 x_*}
```

gives:

```tex
{c_2\over v_{\rm EW}^4}
=
{\lambda_F\over4x_*^2\sin^2x_*},
\qquad
{c_1\over v_{\rm EW}^4}
=
-{\lambda_F\cos x_*\over x_*^2\sin^2x_*}.
```

Thus the local spectrum ratio gives:

```tex
x_*=\arccos\left(-{c_1\over4c_2}\right),
\qquad
f_H={w_Hv_{\rm EW}\over\sqrt2 x_*}.
```

The standard massless charge-one tower over one circle has:

```tex
c_m^{(1)}={A_1\over m^5},
\qquad
{c_1\over c_2}=32.
```

The interior minimum requires:

```tex
\left|{c_1\over c_2}\right|<4.
```

Thus the local spectrum must include additional charged sectors, massive
thresholds, or localized boundary terms.  For charge-one amplitude `A1` and
charge-two amplitude `A2` at the fundamental period:

```tex
c_1=A_1,
\qquad
c_2={A_1\over32}+A_2,
\qquad
{A_2\over A_1}=-{1\over4\cos x_*}-{1\over32}.
```

The two minimum branches are:

```tex
A_1>0:\quad {A_2\over A_1}>{7\over32},
\qquad {\pi\over2}<x_*<\pi,
```

and

```tex
A_1<0:\quad {A_2\over A_1}<-{9\over32},
\qquad 0<x_*<{\pi\over2}.
```

For a general massless charge spectrum, let `A_r` be the total signed
amplitude of charge `r`.  Then

```tex
V_H(x)=\sum_{r\ge1}A_r\sum_{m\ge1}{\cos(mrx)\over m^5}
=\sum_{n\ge1}c_n\cos(nx),
```

with

```tex
c_n={1\over n^5}\sum_{r|n}r^5A_r.
```

The first coefficients are:

```tex
c_1=A_1,\qquad
c_2={A_1\over32}+A_2,\qquad
c_3={A_1\over243}+A_3,\qquad
c_4={A_1\over1024}+{A_2\over32}+A_4.
```

The two-harmonic calculation is a controlled truncation when higher
coefficients are small against `|c_1|+|c_2|`.

## Borel-Weil Charge-Parity Test

Use integer current charge `q=2m` on

```tex
H^0(\CP^1,\mathcal O(n))\simeq V_{n/2}.
```

The charge set is

```tex
q=-n,-n+2,\ldots,n-2,n.
```

The first relevant sectors are:

```tex
\mathcal O(1): |q|=1,\qquad
\mathcal O(2): |q|=2,\qquad
\mathcal O(7): |q|=1,3,5,7.
```

Consequences:

- `O(1)` is the physical doublet source for `A_1`.
- `O(7)` is the weak-period stack; it has zero `A_2` and produces odd
  higher harmonics through `A_3`, `A_5`, and `A_7`.
- `O(2) ~= Sym^2 O(1)` is the minimal Borel-Weil source for `A_2`.

The minimal localized spectrum for the two-harmonic Hosotani potential is
therefore

```tex
A_1 \ {\rm from}\ \mathcal O(1),
\qquad
A_2 \ {\rm from}\ \mathcal O(2),
```

with sign windows

```tex
A_1>0:\quad A_2>{7\over32}A_1,
\qquad
A_1<0:\quad A_2<-{9\over32}A_1.
```

The same line-square sector that carries the `j=1` Schur anchor supplies the
second Fourier harmonic.

## Signed Supertrace Amplitudes

For localized towers coupled to `gamma_H`, record integral current charge
`q_alpha`, one-loop sign `sigma_alpha`, degeneracy `d_alpha`, and positive
threshold weight `tau_alpha`.  With common loop factor `C_H>0`,

```tex
A_r=
{\cal C}_H
\sum_{\alpha:\ |q_\alpha|=r}
\sigma_\alpha d_\alpha\tau_\alpha.
```

For the minimal Borel-Weil pair `O(1) + O(2)`, define

```tex
S_1=
\sum_{\alpha\in O(1),\ |q_\alpha|=1}
\sigma_\alpha d_\alpha\tau_\alpha,
\qquad
S_2=
\sum_{\alpha\in O(2),\ |q_\alpha|=2}
\sigma_\alpha d_\alpha\tau_\alpha.
```

Then

```tex
{A_2\over A_1}={S_2\over S_1}.
```

The finite Hosotani minimum requires

```tex
S_1>0:\quad {S_2\over S_1}>{7\over32},
\qquad
S_1<0:\quad {S_2\over S_1}<-{9\over32}.
```

A same-sign charged-weight pass has `S_2=S_1`, hence `A_2=A_1`.  It gives

```tex
c_1=A_1,\qquad c_2={33\over32}A_1,\qquad
{c_1\over c_2}={32\over33},
```

so

```tex
\cos x_*=-{8\over33},
\qquad
x_*=1.815660181000518\ldots,
\qquad
{f_H\over v_{\rm EW}}
=0.389448856446748\ldots\, w_H.
```

The full-curvature coefficient target becomes

```tex
{c_2\over v_{\rm EW}^4}
=0.080570282164285\ldots\,\lambda_F,
\qquad
{c_1\over v_{\rm EW}^4}
=0.078128758462337\ldots\,\lambda_F.
```

Next calculation: derive `S_1` and `S_2` from the localized `Gamma_EW`
boundary spectrum.

## Charge-Conjugate Pair Reduction

If the localized real structure pairs `+r` with `-r` and preserves the
threshold weight, the signed charge supertrace reduces to

```tex
S_r=2\sigma_r d_r\tau_r.
```

For `O(1)`, the charged pair is `q=+-1`.  For `O(2)`, the charge-two pair is
`q=+-2`; the middle `q=0` state is independent of `theta_H`.  Therefore

```tex
{S_2\over S_1}
=
{\sigma_2 d_2\tau_2\over \sigma_1d_1\tau_1}
=:\chi_{12}.
```

The equal-weight pass is `chi_12=1`.  The general finite-minimum pass is

```tex
\sigma_1d_1\tau_1>0:\quad \chi_{12}>{7\over32},
\qquad
\sigma_1d_1\tau_1<0:\quad \chi_{12}<-{9\over32}.
```

Thus the concrete D10 target is common signed oscillator degeneracy and
common threshold weight for the charge-one and charge-two endpoint pairs.

## Threshold-Resolved Harmonics

The threshold weight carries a wrapping label.  For a flat local circle pass,
set

```tex
z_r=M_rL_H,
\qquad
F(z)=e^{-z}\left(1+z+{z^2\over3}\right),
\qquad
\tau_{r,m}=F(mz_r).
```

With signed base pair weights

```tex
D_r={\cal C}_H\,2\sigma_rd_r,
\qquad
\chi_{12}^{(0)}={D_2\over D_1},
```

the first two Fourier coefficients are

```tex
c_1=D_1F(z_1),
\qquad
c_2={D_1\over32}F(2z_1)+D_2F(z_2).
```

Thus

```tex
{c_2\over c_1}
=
{F(2z_1)\over32F(z_1)}
+\chi_{12}^{(0)}{F(z_2)\over F(z_1)}.
```

For a chosen stationary angle,

```tex
\chi_{12}^{(0)}
=
{F(z_1)\over F(z_2)}
\left[
-{1\over4\cos x_*}
-{F(2z_1)\over32F(z_1)}
\right].
```

The equal signed-base pass gives

```tex
\cos x_*=
-{1\over4\left(F(2z_1)/(32F(z_1))+F(z_2)/F(z_1)\right)}.
```

At `z_1=z_2=0`, this returns `cos x_*=-8/33`.

The threshold function is monotone:

```tex
F'(z)=-{1\over3}e^{-z}z(1+z)\le0.
```

For equal signed-base weights `D_2=D_1` with `D_1>0`, the finite-minimum
domain is

```tex
F(z_2)>{1\over4}F(z_1)-{1\over32}F(2z_1).
```

For `z_1=0`,

```tex
F(z_2)>{7\over32},
\qquad
z_2<3.773046018411012\ldots.
```

For common thresholds `z_2=z_1`, the pass condition holds along the whole ray:

```tex
1+{F(2z_1)\over32F(z_1)}>{1\over4}.
```

## Holomorphic Zero-Mode Pass

The Borel-Weil sectors are Dolbeault kernels:

```tex
H^0(\CP^1,\mathcal O(n))=\ker\bar\partial_{\mathcal O(n)}
\qquad (n\ge0).
```

The charge pair `q=+-1` in `O(1)` and the charge pair `q=+-2` in `O(2)`
therefore sit in zero eigenvalue sectors of their holomorphic boundary
complexes:

```tex
z_1=z_2=0,
\qquad
F(z_1)=F(z_2)=F(2z_1)=1.
```

The `q=0` middle state of `O(2)` is independent of `theta_H`.  With common
signed oscillator data,

```tex
\sigma_2d_2=\sigma_1d_1,
```

the first two coefficients are

```tex
c_1=D_1,\qquad c_2={33\over32}D_1,
\qquad {c_1\over c_2}={32\over33}.
```

The stationary point is

```tex
\cos x_*=-{8\over33},
\qquad
{f_H\over v_{\rm EW}}=0.389448856446748\ldots\,w_H.
```

Remaining computation: derive the common signed oscillator data from the
localized `Gamma_EW` boundary action.

## Common Boundary-Complex Multiplicity

With homogeneous coordinates `[u:v]` on `CP1`, the charged bases are:

```tex
H^0(\CP^1,O(1)): \quad u\ (q=+1),\quad v\ (q=-1),
```

and

```tex
H^0(\CP^1,O(2)):
\quad u^2\ (q=+2),\quad uv\ (q=0),\quad v^2\ (q=-2).
```

Each charged pair has one positive-charge and one negative-charge complex
mode.  The `uv` mode is neutral for the Wilson angle.

For a common localized boundary complex `B_Gamma` whose oscillator operator
acts with the same sign and degeneracy on `(u,v)` and `(u^2,v^2)`,

```tex
\sigma_2=\sigma_1,\qquad d_2=d_1,\qquad D_2=D_1.
```

Combining this multiplicity equality with the holomorphic zero-mode pass
gives `c1/c2=32/33`.

## Charged-Projector Trace Form

Let `P_1^chi` project onto `span{u,v}` in `O(1)`, and let `P_2^chi` project
onto `span{u^2,v^2}` in `O(2)`.  Then

```tex
{\rm Tr}\,P_1^\chi={\rm Tr}\,P_2^\chi=2,
\qquad
P_2^\chi=1-|uv\rangle\langle uv|.
```

For a common localized charged oscillator block

```tex
{\cal B}_\Gamma^\chi=B_0\otimes P_r^\chi,
```

the signed base weights are

```tex
D_r={\cal C}_H\,\sigma\,{\rm Tr}_{P_r^\chi}{\bf 1}
=2{\cal C}_H\sigma.
```

Therefore

```tex
D_2=D_1,
\qquad
V_H(x)=D_1\cos x+{33\over32}D_1\cos(2x).
```

This projector normal form is the local boundary-action test for the
Hosotani spectrum pass.

## Equivariant Dolbeault Character Pass

For the `S1` action generated by `x=w_H theta_H`, the equivariant Dolbeault
index is

```tex
{\rm Ind}_{S^1}\bar\partial_{O(n)}(x)
=
\sum_{k=0}^{n}\exp(i(n-2k)x),
\qquad n\ge0,
```

since `H^1(CP1,O(n))=0`.  Thus

```tex
I_1(x)=2\cos x,
\qquad
I_2(x)=1+2\cos(2x).
```

The `1` in `I_2` is the Wilson-neutral `uv` mode.  The charged character
coefficients for `O(1)` and `O(2)` match.  If the localized endpoint
determinant supplies the same sign and density on the two Dolbeault zero-mode
sectors, then

```tex
A_1=A_2,\qquad
c_1=A_1,\qquad
c_2={A_1\over32}+A_2={33\over32}A_1.
```

Equivalently, after absorbing the common charged-pair factor into `D`,

```tex
V_{\rm BW}(x)
=
D\sum_{m\ge1}{\cos(mx)+\cos(2mx)\over m^5},
```

so

```tex
c_1=D,\qquad
c_2={33\over32}D.
```

Hence

```tex
{c_1\over c_2}={32\over33},
\qquad
\cos x_*=-{8\over33}.
```

The two-harmonic truncation gives that value.  The full massless character has

```tex
{\rm Im}\,{\rm Li}_4(e^{ix})
+2{\rm Im}\,{\rm Li}_4(e^{2ix})=0,
```

with interior solution

```tex
x_{\rm full}=1.837672606049940\ldots,
\qquad
{f_H\over v_{\rm EW}}
=
0.384783872197163\ldots\,w_H.
```

At that root,

```tex
K_{\rm full}
=
-{\rm Re}\,{\rm Li}_3(e^{ix_{\rm full}})
-4{\rm Re}\,{\rm Li}_3(e^{2ix_{\rm full}})
=
3.557941701817797\ldots .
```

Matching `m_theta^2=M_H^2=2 lambda_F v_EW^2` gives

```tex
{D\over v_{\rm EW}^4}
=
{\lambda_F\over x_{\rm full}^2K_{\rm full}}
=
0.083227124394645\ldots\,\lambda_F.
```

The common endpoint sign and density are now the localized
`Gamma_EW` boundary-action target.

## Common-Threshold Flow

For common threshold `z` on the two Dolbeault charged pairs,

```tex
V_z(x)
=
D\sum_{m\ge1}F(mz){\cos(mx)+\cos(2mx)\over m^5}.
```

The stationary equation is

```tex
\sum_{m\ge1}F(mz){\sin(mx)+2\sin(2mx)\over m^4}=0.
```

Representative values:

| `z` | `x_z` | `f_H/(w_H v_EW)` | `D/(lambda_F v_EW^4)` |
|---:|---:|---:|---:|
| `0` | `1.837672606` | `0.384783872` | `0.083227124` |
| `1` | `1.834541900` | `0.385440519` | `0.095760631` |
| `2` | `1.829406205` | `0.386522566` | `0.138316512` |
| `3` | `1.826105448` | `0.387221221` | `0.231213593` |

As `z` grows, the root tends to

```tex
x_\infty=\arccos(-1/4)=1.823476581936975\ldots,
\qquad
f_H/v_{\rm EW}=0.387779469279188\ldots\,w_H.
```

The angle is stable across the common-threshold family; the determinant
amplitude `D` absorbs the threshold suppression.

## Localized Determinant Amplitude Target

After CP2 and boundary zero-mode reduction, write the signed charged endpoint
supertrace after canonical normalization as

```tex
{\cal N}_\Gamma^\chi={\rm Str}_\chi \zeta_\alpha,
```

where `zeta_alpha` is dimensionless and may include threshold factors.  For a
tower with quadratic density `Z_alpha`,

```tex
{1\over2}{\rm Tr}\log[Z_\alpha\Delta_\alpha(x)]
=
{1\over2}{\rm Tr}\log\Delta_\alpha(x)
+
{1\over2}{\rm Tr}\log Z_\alpha.
```

The last term is independent of the Wilson angle and is absorbed into the
vacuum constant.  Thus the angle-dependent determinant uses the canonical
signed supertrace.  The DBI/open-boundary density enters `f_H^2` and the
threshold parameters.  The five-dimensional circle determinant has form

```tex
D={3\over4\pi^2}{{\cal N}_\Gamma^\chi\over L_H^4}.
```

The numerical coefficient follows from Schwinger parameterization and Poisson
resummation of

```tex
{1\over2}\sum_{n\in{\mathbb Z}}\int {d^4p_E\over(2\pi)^4}
\log\left[p_E^2+\left({2\pi n+x\over L_H}\right)^2\right].
```

The tower sign is included in `N_Gamma^chi`.

For the full massless character, matching `M_H^2=2 lambda_F v_EW^2` gives

```tex
{3\over4\pi^2}{{\cal N}_\Gamma^\chi\over L_H^4v_{\rm EW}^4}
=
0.083227124394645\ldots\,\lambda_F.
```

Equivalently,

```tex
{{\cal N}_\Gamma^\chi\over L_H^4v_{\rm EW}^4}
=
1.095225057620535\ldots\,\lambda_F.
```

For common threshold `z`, replace the right side by the corresponding
threshold-flow table value.  The scalar amplitude equation for the localized
`Gamma_EW` determinant is now explicit.

## Loop-Length Metric Bridge

Let `s` be arclength on `gamma_H`, with total length `L_H`, and use

```tex
\omega_H={ds\over L_H},
\qquad
\int_{\gamma_H}\omega_H=1.
```

Then

```tex
\int_{\gamma_H}|\omega_H|^2ds={1\over L_H}.
```

Writing `Z_Gamma,H` for the remaining localized CP2, endpoint, and current
density,

```tex
f_H^2={Z_{\Gamma,H}\over L_H}.
```

The finite-sheet condition gives

```tex
f_H\theta_{H,*}={v_{\rm EW}\over\sqrt2},
\qquad
x_*=w_H\theta_{H,*},
```

hence

```tex
L_H={2x_*^2Z_{\Gamma,H}\over w_H^2v_{\rm EW}^2}.
```

For the full massless-character root, the determinant target becomes

```tex
{{\cal N}_\Gamma^\chi w_H^8v_{\rm EW}^4
\over
16x_*^8Z_{\Gamma,H}^4}
=
1.095225057620535\ldots\,\lambda_F.
```

The localized Hosotani calculation is now reduced to the pair
`(N_Gamma^chi,Z_Gamma,H)`.

## Point-Projector Metric Consequence

The point-projector current metric on the weak transverse channel gives

```tex
f_H^2={Q\over4}f_\Gamma^2.
```

Combining it with the full massless-character root gives

```tex
{f_H\over v_{\rm EW}}
=
{w_H\over\sqrt2\,x_{\rm full}}
=
0.384783872197163\ldots\,w_H.
```

Hence

```tex
{f_\Gamma\over v_{\rm EW}}
=
{2\over\sqrt Q}\,0.384783872197163\ldots\,w_H
=
{\sqrt2\over\sqrt Q\,x_{\rm full}}\,w_H.
```

For `Q=7`,

```tex
{f_\Gamma\over v_{\rm EW}}
=
0.290869266954901\ldots\,w_H.
```

The loop metric and projector metric meet through

```tex
{Z_{\Gamma,H}\over L_H}
=
{Q\over4}f_\Gamma^2.
```

Equivalently,

```tex
{{\cal N}_\Gamma^\chi\over Z_{\Gamma,H}^4}
=
{2279.126786313921\ldots\over w_H^8v_{\rm EW}^4}\,\lambda_F
```

at the full massless-character root.  The localized boundary calculation has
three quantities to extract from one action:
`N_Gamma^chi`, `Z_Gamma,H`, and `f_Gamma^2`.

## DBI Kinetic Coefficient Map

The localized Yang-Mills term induced by the D8-like action is

```tex
S_{\rm YM}^{\Gamma}
=
-{T_8(2\pi\alpha')^2\over4}
\int_{\Gamma_{\rm EW}}
e^{-\phi}\sqrt{\gamma_\Gamma}\,
{\rm tr}_{\rm end}(F_{MN}F^{MN}).
```

For the Wilson ansatz

```tex
A_s(x,y)=\theta_H(x)\omega_{H,s}(y)n_H^aT_a,
\qquad
F_{\mu s}=(\partial_\mu\theta_H)\omega_{H,s}n_H^aT_a,
```

the four-dimensional kinetic coefficient is

```tex
f_H^2
=
T_8(2\pi\alpha')^2
\int_{\Gamma_{\rm EW,int}}
e^{-\phi}\sqrt{\gamma_\Gamma}\,
g^{ss}\omega_{H,s}\omega_{H,s}\,
{\cal T}_H,
```

with

```tex
{\cal T}_H=
{\rm tr}_{\rm end}(n_H^aT_a\,n_H^bT_b)\Pi_{ab}^{\rm Schur}.
```

For `omega_H=ds/L_H` and uniform transverse density,

```tex
Z_{\Gamma,H}
=
T_8(2\pi\alpha')^2
\int_{\CP^2}
e^{-\phi}\sqrt{\gamma_\perp}\,
{\cal T}_H,
\qquad
f_H^2={Z_{\Gamma,H}\over L_H}.
```

The canonical determinant factor is

```tex
{\cal N}_\Gamma^\chi
=
\sum_{\alpha\in\ker{\cal B}_\Gamma^\chi}
\sigma_\alpha d_\alpha\tau_\alpha.
```

In the equal-amplitude Borel-Weil pass,

```tex
{\cal N}_{\Gamma,1}^\chi
=
{\cal N}_{\Gamma,2}^\chi
=
{\cal N}_\Gamma^\chi.
```

The total charged supertrace over `O(1) op O(2)` is

```tex
{\cal N}_{\Gamma,tot}^\chi=2{\cal N}_\Gamma^\chi.
```

The scalar-curvature target uses the per-pair amplitude
`N_Gamma^chi`, multiplying `cos(mx)+cos(2mx)` with a common coefficient.

The shared localized calculation is the equality of current frame, endpoint
trace convention, and threshold operator in the DBI kinetic integral and the
charged-kernel supertrace.

## Endpoint Trace Evaluation

Let `Z_Gamma,0` be the DBI density with the endpoint trace stripped to unit
weak-current normalization:

```tex
Z_{\Gamma,0}
=
T_8(2\pi\alpha')^2
\int_{\CP^2}
e^{-\phi}\sqrt{\gamma_\perp}\,{\cal Z}_{\rm end}.
```

The point-projector endpoint trace gives

```tex
G_{ab}^{(p)}
=
{\rm Re}\,\langle0|T_aK_pT_b|0\rangle
=
{Q\over4}{\rm diag}(1,1,0)_{ab}.
```

For a unit transverse weak direction,

```tex
Z_{\Gamma,H}={Q\over4}Z_{\Gamma,0},
\qquad
f_\Gamma^2={Z_{\Gamma,0}\over L_H}.
```

For `Q=7`,

```tex
Z_{\Gamma,H}={7\over4}Z_{\Gamma,0}.
```

The base-density form of the target is

```tex
{{\cal N}_\Gamma^\chi\over Z_{\Gamma,0}^4}
=
{21375.716460702053\ldots\over w_H^8v_{\rm EW}^4}\,\lambda_F.
```

Thus the active calculation reduces to `Z_Gamma,0` from the DBI integral and
`N_Gamma^chi` from the canonical charged kernel.

## Zero-Threshold Kernel Count

For `M_Gamma^chi=0`, the charged kernels are

```tex
H^0(CP1,O(1))^chi=span{u,v},        q=+-1,
H^0(CP1,O(2))^chi=span{u^2,v^2},    q=+-2.
```

The neutral `uv` state is constant in the Wilson angle.  Each charged pair
has rank two.  With common oscillator multiplicity `d_chi` and common
Dolbeault index sign `sigma_chi`,

```tex
N_{Gamma,1}^chi=2 sigma_chi d_chi,
\qquad
N_{Gamma,2}^chi=2 sigma_chi d_chi.
```

Thus the per-pair convention gives

```tex
N_Gamma^chi=2 sigma_chi d_chi.
```

The Higgs-curvature match has `D>0` for `lambda_F>0`, so the zero-threshold
trial requires

```tex
sigma_chi d_chi>0.
```

For the minimal even endpoint determinant,

```tex
d_chi=1,\qquad sigma_chi=+1,\qquad N_Gamma^chi=2.
```

The base-density target becomes

```tex
{Z_{\Gamma,0}\over v_{\rm EW}}
=
\left(
{2\over21375.716460702053\ldots\,\lambda_F}
\right)^{1/4}
w_H^2.
```

## Operational Steering Addendum

Each candidate Hosotani row should now be written as a coefficient ledger:

```tex
(\gamma_H,\omega_H,n_H^a,w_H,\mu_\Gamma,
 Z_{\Gamma,0},Z_{\Gamma,H},L_H,
 {\cal B}_\Gamma^\chi,M_\Gamma^\chi,
 \sigma_\chi,d_1,d_2,z_1,z_2,
 {\cal N}_{\Gamma,1}^\chi,{\cal N}_{\Gamma,2}^\chi).
```

The row passes the local tensor test through the Wilson expansion

```tex
\delta U_H=i\mu_\Gamma T_a^{(j)}\delta\xi^a,
\qquad
\delta^2U_H=-\mu_\Gamma^2T_a^{(j)}T_b^{(j)}
\delta\xi^a\delta\xi^b,
```

and through the canonical ratio

```tex
{\beta_{\rm diag}\over\alpha_{\rm mix}^2}=1.
```

The row passes the metric test through

```tex
f_H^2={Z_{\Gamma,H}\over L_H},
\qquad
Z_{\Gamma,H}={Q\over4}Z_{\Gamma,0},
```

using the point-projector trace on the weak transverse directions.  The
dimension count is then

```tex
[Z_{\Gamma,0}]=L^{-1},
\qquad
[f_H^2]=L^{-2},
\qquad
[{\cal N}_\Gamma^\chi]=1.
```

The row passes the charged-kernel test when the localized boundary complex
has common charged blocks

```tex
{\cal B}_\Gamma^\chi
=B_0\otimes(P_1^\chi\oplus P_2^\chi)+M_\Gamma^\chi,
```

with

```tex
P_1^\chi=span\{u,v\},
\qquad
P_2^\chi=span\{u^2,v^2\}.
```

The neutral `uv` mode is absent from the angle-dependent determinant.  The
threshold condition is

```tex
d_1F(z_1)=d_2F(z_2),
\qquad
F(z)=e^{-z}\left(1+z+{z^2\over3}\right).
```

A common threshold block gives

```tex
d_1=d_2=1,\qquad z_1=z_2=z,
\qquad
{\cal N}_\Gamma^\chi=2\sigma_\chi F(z).
```

Positive Higgs curvature selects

```tex
\sigma_\chi=+1.
```

The final density comparison for a common threshold is

```tex
{Z_{\Gamma,0}\over v_{\rm EW}}
=
\left(
{2F(z)\over21375.716460702053\ldots\,\lambda_F}
\right)^{1/4}w_H^2.
```

The calculation therefore has three concrete outputs:

```tex
Z_{\Gamma,0},
\qquad
z,
\qquad
w_H.
```

Together with the sign of the endpoint determinant, these outputs decide the
Hosotani realization.

## Common Boundary-Complex Threshold Lemma

Let

```tex
{\cal H}_\chi=P_1^\chi\oplus P_2^\chi,
\qquad
\dim P_1^\chi=\dim P_2^\chi=2,
```

where

```tex
P_1^\chi=span\{u,v\},
\qquad
P_2^\chi=span\{u^2,v^2\}.
```

Assume the localized charged boundary operator factorizes on a common
oscillator space `E_chi`:

```tex
{\cal B}_\Gamma^\chi
=
{\cal B}_0\otimes{\bf 1}_{{\cal H}_\chi}
+
{\cal M}_0\otimes{\bf 1}_{{\cal H}_\chi},
```

with

```tex
{\cal M}_0^\dagger{\cal M}_0=M^2{\bf 1}_{E_\chi},
\qquad
{\rm Str}_{E_\chi}{\bf 1}=\sigma_\chi d_\chi.
```

The Wilson angle acts on the charged pair in `P_r^chi` through

```tex
e^{irx},\qquad e^{-irx}.
```

The angle-dependent supertrace over the pair is therefore

```tex
2\sigma_\chi d_\chi F(ML_H)\cos(rx).
```

Thus

```tex
{\cal N}_{\Gamma,r}^\chi
=
2\sigma_\chi d_\chi F(z),
\qquad r=1,2,
```

so the equal-amplitude condition follows from a degree-blind charged boundary
oscillator block.  A splitting term

```tex
\Delta{\cal M}^\chi
=
\Delta_1P_1^\chi+\Delta_2P_2^\chi
```

changes the condition to

```tex
d_1F(z_1)=d_2F(z_2).
```

The next local source check is the degree-dependence of
`M_Gamma^chi` in the D8/open-boundary action.

## Dolbeault-Protected Degree-Blindness

A concrete source for degree-blindness is the product boundary complex

```tex
{\cal D}_\Gamma^\chi
=
\left(
\bar\partial_{O(1)}^\chi
\oplus
\bar\partial_{O(2)}^\chi
\right)\otimes{\bf 1}_{E_\chi}
+
{\bf 1}\otimes{\cal D}_{E,\chi}.
```

On the product zero-mode reduction,

```tex
({\cal D}_\Gamma^\chi)^\dagger{\cal D}_\Gamma^\chi
=
\Delta_{\bar\partial,\chi}\otimes{\bf 1}_{E_\chi}
+
{\bf 1}\otimes\Delta_{E,\chi}.
```

For `n>=0`,

```tex
H^0(CP1,O(n))=\ker\bar\partial_{O(n)},
\qquad
H^1(CP1,O(n))=0.
```

Thus `Delta_dbar,chi` vanishes on

```tex
P_1^\chi=span\{u,v\},
\qquad
P_2^\chi=span\{u^2,v^2\}.
```

The charged-pair threshold spectrum is the spectrum of `Delta_E,chi` in both
sectors.  If the common oscillator block has one relevant eigenvalue `M^2`
with signed multiplicity `sigma_chi d_chi`, then

```tex
z_1=z_2=ML_H,\qquad d_1=d_2=d_\chi,
```

and

```tex
{\cal N}_{\Gamma,1}^\chi
=
{\cal N}_{\Gamma,2}^\chi
=
2\sigma_\chi d_\chi F(ML_H).
```

Degree-dependent rough-Laplacian, Casimir, or curvature terms are the local
splitting sources to compute in the D8/open-boundary action.

## Splitting-Source Audit

After the Dolbeault reduction, parameterize a degree-dependent threshold by

```tex
M_r^2
=
M_E^2
+ alpha_B n_r
+ alpha_C j_r(j_r+1)
+ alpha_R,
```

where

```tex
n_r=r,\qquad j_r={r\over2}.
```

Thus

```tex
M_1^2=M_E^2+alpha_B+{3\over4}alpha_C+alpha_R,
```

and

```tex
M_2^2=M_E^2+2alpha_B+2alpha_C+alpha_R.
```

The splitting is

```tex
M_2^2-M_1^2=alpha_B+{5\over4}alpha_C.
```

The common-threshold condition is

```tex
alpha_B+{5\over4}alpha_C=0.
```

The Dolbeault-protected pass has

```tex
alpha_B=0,\qquad alpha_C=0,
```

with `alpha_R` absorbed into the common oscillator threshold.  The
D8/open-boundary action must decide whether the CP1 part is a Dolbeault index
complex or a degree-dependent kinetic Laplacian.

## Minimal Density Factors

For the minimal positive endpoint determinant,

```tex
{\cal N}_\Gamma^\chi=2F(z),
```

the base-density equation is

```tex
{Z_{\Gamma,0}\over v_{\rm EW}}
=
C_0 F(z)^{1/4}\lambda_F^{-1/4}w_H^2,
\qquad
C_0=
\left({2\over21375.716460702053\ldots}\right)^{1/4}.
```

The numerical constant is

```tex
C_0=0.0983506713707568\ldots .
```

Representative common-threshold values:

| `z` | `F(z)` | `F(z)^(1/4)` | `C0 F(z)^(1/4)` |
|---:|---:|---:|---:|
| `0` | `1.000000000000000` | `1.000000000000000` | `0.0983506713707568` |
| `1` | `0.858385362733366` | `0.962543965999241` | `0.0946668452798963` |
| `2` | `0.586452894025322` | `0.875101208197768` | `0.0860667913436109` |
| `3` | `0.348509478575048` | `0.768340363218516` | `0.0755667905637921` |
| `4` | `0.189261601850253` | `0.659577189613153` | `0.0648698594192906` |

The numerical scale remains a localized density target; `lambda_F` and `w_H`
remain symbolic at this stage.

## Charge-Period Audit

In the integer current-charge convention,

```tex
O(1): q=+-1,\qquad O(2): q=0,+-2.
```

The angle-dependent charged set is

```tex
|q|=1,2,
```

so

```tex
w_H=gcd(1,2)=1.
```

The `Q=7` endpoint stack has odd charges

```tex
|q|=1,3,5,7,
```

and also gives `w_H=1` in the same current-charge normalization.  Therefore
the minimal Hosotani density target uses

```tex
{Z_{\Gamma,0}\over v_{\rm EW}}
=C_0F(z)^{1/4}\lambda_F^{-1/4}.
```

A quotient or lift of the endpoint charge lattice changes this by the explicit
factor `w_H^2`.

## Source Status For The Dolbeault Pass

Local source support currently splits as follows:

- Payen supports the endpoint Wilson representation route
  `endpoint group variable -> V_j -> Wilson-loop charge insertion`.
- D-brane WZ notes support Chan-Paton charge data and spin-c boundary
  bookkeeping.
- Katz-Sharpe and Zabzine support the boundary-complex pattern
  `open string BRST/cohomology -> Ext/Dolbeault zero modes -> charged
  endpoint spectrum` for B-type or generalized-complex brane settings.
- The D8 Dolbeault product complex
  `D_Gamma^chi=(dbar_O(1)^chi op dbar_O(2)^chi) otimes 1 + 1 otimes D_E`
  still requires a Type-IIA/D8 realization or direct derivation from the
  localized D8/open-boundary action.

Thus the Dolbeault-protected threshold has source support as a
boundary-cohomology pattern and remains a D8 realization criterion.

## D8 Realization Routes

The source-to-`Gamma_EW` bridge has three concrete routes.

1. Generalized-complex brane route: Katz-Sharpe supplies the large-radius
   B-brane Ext/cohomology model, and Zabzine supplies the generalized-complex
   BRST language.  Target: a Type-IIA-compatible generalized cycle whose
   open-string BRST complex reduces to
   `dbar_O(1)^chi op dbar_O(2)^chi` on the weak line-bundle factor.
2. Spin-c boundary route: the Freed-Witten completion on the D8-like carrier
   already forces spin-c data.  Target: a boundary Dirac operator whose
   chiral reduction on the weak projective line is the Dolbeault complex.
3. Endpoint-cohomology route: before the `Q`-neutral collapse, the
   Chan-Paton endpoint Hilbert space carries
   `H0(CP1,O(1)) op H0(CP1,O(2))`.  The D8 action supplies the common
   oscillator block `E_chi`, and the weak line-bundle factor supplies the
   cohomology projectors `P_1^chi` and `P_2^chi`.

The endpoint-cohomology route is closest to the current boundary-complex
calculation.  Select it as the active Hosotani route.

The working charged Hilbert space is

```tex
{\cal H}_{\Gamma,\chi}
=
\left(
H^0(CP1,O(1))^\chi
\oplus
H^0(CP1,O(2))^\chi
\right)\otimes E_\chi.
```

The localized operator target is

```tex
{\cal D}_{\Gamma,\chi}
=
\Pi_\chi
\left(
1\otimes{\cal D}_{E,\chi}
+
{\cal D}_{split}
\right)
\Pi_\chi,
\qquad
\Pi_\chi=P_1^\chi\oplus P_2^\chi.
```

The pass condition is

```tex
{\cal D}_{split}=0
```

on the charged cohomology, equivalently

```tex
alpha_B=0,\qquad alpha_C=0.
```

Failure modes are explicit:

```tex
{\cal D}_{split}
=
alpha_B N_line
+
alpha_C C_2
+
alpha_parity Pi_O8.
```

The next local derivation is the coefficient extraction of
`alpha_B`, `alpha_C`, and `alpha_parity` from the D8/O8 endpoint action.

## Orientifold-Parity Reduction

The existing D8/O8 endpoint reality test gives

```tex
V_j^* \simeq V_j
```

for the retained `SU(2)` representations.  The `j=1/2` doublet is pseudoreal
and the `j=1` triplet is real; both charged source sectors survive the
orientifold endpoint test.  At the charged-pair rank level,

```tex
dim P_1^chi=dim P_2^chi=2
```

is preserved.  Therefore orientifold survival alone contributes

```tex
alpha_parity=0
```

to the threshold splitting operator.  The real versus pseudoreal distinction
belongs in `sigma_chi` or in a sourced endpoint multiplicity `d_chi`.  The
remaining threshold-splitting coefficients are `alpha_B` and `alpha_C`.

## Coefficient-Extraction Worksheet

Each Hosotani candidate gets a six-row coefficient record.  The record is
usable when every entry comes from the same localized `Gamma_EW` action.

### H0 Data Row

Record

```tex
(\gamma_H,\omega_H,n_H^a,w_H,\mu_\Gamma),
\qquad
\int_{\gamma_H}\omega_H=1,
\qquad
x=w_H\theta_H.
```

Also record the coupled charge set

```tex
{\cal Q}_H=\{|q_\alpha|\},
\qquad
w_H=\gcd{\cal Q}_H
```

in the integer current-charge convention.

### H1 Tensor Row

Expand the Wilson operator in the same current frame used by `A_j`:

```tex
U_H(\xi)=
{\cal P}\exp\left(
i\mu_\Gamma\int_{\gamma_H}\xi^a e_aT_a^{(j)}
\right).
```

The row records

```tex
\alpha_{\rm mix}={\mu_\Gamma\over f_H},
\qquad
\beta_{\rm diag}={\mu_\Gamma^2\over f_H^2},
\qquad
R_{\rm tensor}=
{\beta_{\rm diag}\over \alpha_{\rm mix}^2}.
```

Pass value:

```tex
R_{\rm tensor}=1.
```

Pure `S1_Q` rows fail as scalar rows because `Q eta0=0` gives zero first and
second insertions on the neutral section.

### H2 Kinetic Row

Compute

```tex
Z_{\Gamma,H}
=
T_8(2\pi\alpha')^2
\int_{\Gamma_{\rm EW,int}}
e^{-\phi}\sqrt{\gamma_\Gamma}\,
g^{ss}\omega_{H,s}\omega_{H,s}\,
{\cal T}_H .
```

For the point-projector endpoint metric,

```tex
{\cal T}_{H,\perp}={Q\over4},
\qquad
R_{\rm metric}={4Z_{\Gamma,H}\over QZ_{\Gamma,0}}.
```

Pass value:

```tex
R_{\rm metric}=1.
```

If the endpoint trace gives another metric `G_ab`, diagonalize `G_ab` and
evaluate `A_j^\dagger A_j` in that eigenframe.

### H3 Determinant Row

For a charge-`r` tower with threshold

```tex
z_r=M_rL_H,
```

define the wrapping weight

```tex
F_m(z_r)=\exp(-mz_r)\left(1+mz_r+{m^2z_r^2\over3}\right).
```

With bare signed endpoint density

```tex
A_r^0=C_H\sigma_r d_r,
```

the Wilson potential coefficients are

```tex
V_H(x)=\sum_{n\ge1}c_n\cos(nx),
\qquad
c_n={1\over n^5}\sum_{r|n}r^5A_r^0F_{n/r}(z_r).
```

The fundamental two-charge shape check is

```tex
\sigma_1d_1F_1(z_1)=\sigma_2d_2F_1(z_2).
```

For the common positive endpoint pair this reduces to

```tex
d_1F(z_1)=d_2F(z_2).
```

### H4 Splitting Row

After the endpoint cohomology reduction, write

```tex
{\cal D}_{\rm split}
=
\alpha_BN_{\rm line}
+\alpha_CC_2
+\alpha_{\rm parity}\Pi_{\rm O8}.
```

The current orientifold-parity result gives

```tex
\alpha_{\rm parity}=0.
```

Two sourced routes remain:

```tex
\bar\partial{\rm\ kernel\ route:}\quad
\alpha_B=\alpha_C=0,
```

because the Dolbeault eigenvalue on `H0(CP1,O(n))` is zero for `n>=0`; and

```tex
{\rm rough\ Laplacian\ route:}\quad
\alpha_B+{5\over4}\alpha_C=0
```

as the required relation for equal charge-one and charge-two threshold
weights.  The coefficient extraction has to identify which operator the
D8/O8 endpoint action uses.

### Bochner Split Decision

Use the local curvature convention

```tex
i\Lambda F_{\mathcal O(1)}=\kappa_B>0,
\qquad
i\Lambda F_{\mathcal O(n)}=n\kappa_B.
```

For zero-forms valued in `O(n)`, the Kähler identity gives

```tex
2\Delta_{\bar\partial,n}
=
\nabla_n^\dagger\nabla_n
-i\Lambda F_{\mathcal O(n)}.
```

On a holomorphic section

```tex
s\in H^0(CP1,O(n)),
\qquad
\Delta_{\bar\partial,n}s=0,
```

so a rough kinetic determinant gives

```tex
\nabla_n^\dagger\nabla_n s=n\kappa_Bs.
```

Therefore the rough-Laplacian endpoint row has

```tex
\alpha_B=\kappa_B,\qquad \alpha_C=0,
```

and

```tex
M_2^2-M_1^2=\kappa_B.
```

This row splits the `O(1)` and `O(2)` thresholds.  A pure representation
Casimir threshold has

```tex
\alpha_B=0,\qquad \alpha_C=\kappa_C,
\qquad
M_2^2-M_1^2={5\over4}\kappa_C.
```

Thus a pass row comes from either the cohomological determinant

```tex
\alpha_B=\alpha_C=0
```

or a sourced mixed operator satisfying

```tex
\alpha_C=-{4\over5}\alpha_B.
```

The current endpoint-cohomology route selects the first option as the active
target.

### Threshold Row Table

| row | coefficients | threshold result | verdict |
|---|---:|---:|---|
| cohomological determinant | `alpha_B=0`, `alpha_C=0` | `M_2^2-M_1^2=0` | pass |
| rough CP1 kinetic term | `alpha_B=kappa_B`, `alpha_C=0` | `M_2^2-M_1^2=kappa_B` | rejected row |
| pure representation Casimir | `alpha_B=0`, `alpha_C=kappa_C` | `M_2^2-M_1^2=5kappa_C/4` | rejected row |
| sourced mixed operator | `alpha_C=-4alpha_B/5` | `M_2^2-M_1^2=0` | pass after source derivation |

### Threshold Monotonicity Lemma

For

```tex
F(z)=\exp(-z)\left(1+z+{z^2\over3}\right),
```

one has

```tex
F'(z)=-{1\over3}\exp(-z)z(1+z).
```

Hence `F` decreases for `z>0`.  With equal endpoint multiplicities,

```tex
M_2^2>M_1^2
\quad\Longrightarrow\quad
z_2>z_1
\quad\Longrightarrow\quad
F(z_2)<F(z_1).
```

Thus a positive rough or pure-Casimir split fails the equal-amplitude
Borel-Weil condition.  Unequal multiplicity can compensate algebraically
through `d_2/d_1=F(z_1)/F(z_2)`, and then the multiplicity ratio has to be
sourced by the D8/O8 endpoint action.

### Payen/Borel-Weil Endpoint Implication

In the Payen endpoint route, the boundary variable quantizes to a finite
representation `V_j`.  The Borel-Weil identification

```tex
V_j\simeq H^0(CP1,O(2j))
```

uses `CP1` as the representation phase space.  The endpoint contribution is a
finite Wilson trace over `V_j`; the line-bundle degree supplies the character,
charge set, and multiplicity data.  A CP1 rough kinetic Hamiltonian is an
extra endpoint operator and must be sourced separately.

Consequently the current endpoint-Hilbert route naturally lands on the
cohomological determinant row

```tex
alpha_B=alpha_C=0.
```

Rows with `alpha_B` or `alpha_C` activated require an explicit extra
Hamiltonian in the localized D8/O8 action.

### Payen Trace Normalization

Payen's discretized boundary path integral uses

```tex
\int N_R\,Dg\,R(g)v_\kappa v_\kappa^\dagger R^\dagger(g)
=
{\bf 1}_{V_R}.
```

Boundary insertions then reduce to

```tex
{\rm Tr}_{V_R}\,T_{\partial\Sigma}\prod_s\lambda_s.
```

With an external Yang-Mills field the same construction gives

```tex
{\rm Tr}_{V_R}\,
T_{\partial\Sigma}
\exp\left(i\int_{\partial\Sigma}d\tau\,R(A_\tau(\tau))\right).
```

The endpoint Wilson determinant therefore uses the ordinary finite
representation trace.  The final trace coefficient has no dimension divisor.
For the charged projectors,

```tex
{\rm Tr}_{P_1^\chi}{\bf 1}=2,
\qquad
{\rm Tr}_{P_2^\chi}{\bf 1}=2,
```

so the source-backed endpoint trace gives

```tex
d_1=d_2=d_\chi
```

before oscillator thresholds.  The remaining determinant input is the common
oscillator sign and multiplicity `sigma_chi d_chi`.

### Finite Trace Factor Separation

The determinant and kinetic rows use the same localized measure with two
different finite traces already evaluated.  The Wilson determinant row uses

```tex
{\rm Tr}_{P_r^\chi}{\bf 1}=2,\qquad r=1,2,
```

and the kinetic row uses the point-projector metric

```tex
G_{ab}^{(p)}
=
{\rm Re}\,\langle0|T_a(1-|0\rangle\langle0|)T_b|0\rangle
=
{Q\over4}{\rm diag}(1,1,0)_{ab}.
```

Thus the shared-density calculation concerns

```tex
d\nu_\Gamma
=
T_8(2\pi\alpha')^2e^{-\phi}\sqrt{\gamma_\Gamma}
W_\Gamma\,d^5\sigma,
```

with finite factors

```tex
{\cal N}_\Gamma^\chi=2\sigma_\chi d_\chi F(z),
\qquad
Z_{\Gamma,H}={Q\over4}Z_{\Gamma,0}.
```

For `Q=7`, these finite factors are `2` and `7/4`.

### Density-Normalized Determinant

Use the same localized measure to define the charged kernel Hilbert space:

```tex
\psi_\alpha\in
L^2(\Gamma_EW,int,d\nu_\Gamma)\otimes E_\chi,
\qquad
\int_{\Gamma_EW,int}d\nu_\Gamma |\psi_\alpha|^2=1.
```

The angle-dependent determinant coefficient is then the finite supertrace

```tex
{\cal N}_\Gamma^\chi
=
\sum_{\alpha\in\ker{\cal B}_\Gamma^\chi}
\sigma_\alpha d_\alpha\tau_\alpha.
```

Thus `dnu_Gamma` fixes the kernel normalization and the kinetic scale

```tex
Z_{\Gamma,0}=\int d\nu_\Gamma |\eta_0|^2,
\qquad
Z_{\Gamma,H}={Q\over4}Z_{\Gamma,0},
```

The Wilson amplitude is the finite trace over normalized kernels.  For
the minimal positive endpoint row,

```tex
{\cal N}_\Gamma^\chi=2F(z),
```

and the full-character target reads

```tex
{Z_{\Gamma,0}\over v_{\rm EW}}
=
w_H^2
\left(
{2F(z)\over21375.716460702053\ldots\,\lambda_F}
\right)^{1/4}.
```

Since `F'(z)=-exp(-z)z(1+z)/3`, every minimal positive endpoint realization
obeys the density window

```tex
0<
{Z_{\Gamma,0}\over w_H^2v_{\rm EW}}
\leq
C_0\lambda_F^{-1/4},
\qquad
C_0=
\left({2\over21375.716460702053\ldots}\right)^{1/4}
=0.0983506713707568\ldots .
```

Equivalently, the localized D8/O8 calculation passes the row exactly when

```tex
0<
{21375.716460702053\ldots\,\lambda_F\over2w_H^8}
\left({Z_{\Gamma,0}\over v_{\rm EW}}\right)^4
\leq1.
```

Define the left-hand side as

```tex
\Xi_\Gamma
=
{21375.716460702053\ldots\,\lambda_F\over2w_H^8}
\left({Z_{\Gamma,0}\over v_{\rm EW}}\right)^4.
```

Then `Xi_Gamma=1` gives `z=0`, and `0<Xi_Gamma<1` gives a unique `z>0`
through

```tex
e^{-z}\left(1+z+{z^2\over3}\right)=\Xi_\Gamma.
```

Values `Xi_Gamma>1` reject the minimal positive endpoint row and require
additional localized spectrum data.

Equivalently,

```tex
R_\Gamma
=
\Xi_\Gamma^{1/4}
=
{Z_{\Gamma,0}\over C_0\lambda_F^{-1/4}w_H^2v_{\rm EW}}
=
F(z)^{1/4}.
```

Representative inversion values:

| `R_Gamma` | `Xi_Gamma` | `z` |
|---:|---:|---:|
| `1.00` | `1.000000000000` | `0.000000000000` |
| `0.95` | `0.814506250000` | `1.172323217914` |
| `0.90` | `0.656100000000` | `1.747032087191` |
| `0.80` | `0.409600000000` | `2.710609395385` |
| `0.70` | `0.240100000000` | `3.624198934761` |
| `0.50` | `0.062500000000` | `5.612362993294` |
| `0.25` | `0.003906250000` | `9.192117816916` |

### Determinant Sign Placement

Payen quantization fixes the ordinary trace and the equality

```tex
d_1=d_2=d_\chi.
```

The sign `sigma_chi` belongs to the quadratic fluctuation determinant on the
common oscillator block `E_chi`.  In the project convention

```tex
D={3\over4\pi^2}{{\cal N}_\Gamma^\chi\over L_H^4},
\qquad
{\cal N}_\Gamma^\chi=2\sigma_\chi d_\chi F(z).
```

The Higgs curvature target has `D>0`.  Since `d_chi>0` and `F(z)>0`, the
minimal endpoint determinant uses

```tex
sigma_chi=+1.
```

Thus Payen supplies trace multiplicity, and the D8/O8 fluctuation operator
supplies the sign.

### H5 Finite-Triple Row

The Wilson scalar has to carry the electroweak doublet edge before the
`Q`-neutral projection.  The finite-triple row records:

```tex
{\rm KO6\ signs},\qquad
\mu_{ij}\ {\rm Poincare\ matrix},\qquad
{\rm determinant\mbox{-}one\ hypercharge\ lift},\qquad
Q\eta_0=0.
```

The stationary value and curvature checks are

```tex
|f_H\theta_{H,*}|={v_{\rm EW}\over\sqrt2},
\qquad
{1\over f_H^2}\partial_{\theta_H}^2V_H|_*=M_H^2
```

after projection to the Standard-Model-like scalar.

Concrete local finite-edge entries come from the KO6 four-summand lift

```tex
H_{rq}^-\longrightarrow H_{wq}^+.
```

The abelian charge equations are

```tex
Y(H_{rq})=y_r-y_q=0,
\qquad
Y(H_{wq})=y_w-y_q={1\over2}.
```

With the weak-summand convention `y_w=0`, they give

```tex
y_r=y_q=-{1\over2}.
```

The neutral Higgs component has

```tex
T_3\eta_0=-{1\over2}\eta_0,
\qquad
Y\eta_0={1\over2}\eta_0,
\qquad
Q\eta_0=0.
```

In integer hypercharge `y=6Y`, the target edge has

```tex
y(H_{wq})=3,
```

matching the `Z6 -> Z3` endpoint quotient convention.  Thus the H5 row has a
local photon-protection pass; the full finite-triple row still has to evaluate
the complete Poincare/unimodular fermion lift.

### Row Verdict

A row passes the Schur/Hosotani requirement when

```tex
R_{\rm tensor}=1,\qquad
R_{\rm metric}=1,\qquad
\alpha_B=\alpha_C=\alpha_{\rm parity}=0,
\qquad
w_H=1,
```

or when a sourced rough-Laplacian relation enforces

```tex
\alpha_B+{5\over4}\alpha_C=0
```

and the determinant row still gives the same finite Wilson minimum.

## Threshold-Operator Criterion

Let `z_r=M_r L_H` for the charged pair of absolute charge `r`, with

```tex
F(z)=exp(-z)(1+z+z^2/3).
```

Then

```tex
N_{Gamma,1}^chi=2 sigma_chi d_1 F(z_1),
\qquad
N_{Gamma,2}^chi=2 sigma_chi d_2 F(z_2).
```

The equal-amplitude Borel-Weil shape requires

```tex
d_1F(z_1)=d_2F(z_2).
```

The minimal common-threshold pass has

```tex
d_1=d_2=1,\qquad z_1=z_2=z,
```

and therefore

```tex
N_Gamma^chi=2 sigma_chi F(z).
```

Positive Higgs curvature selects `sigma_chi=+1`, giving

```tex
{Z_{\Gamma,0}\over v_{\rm EW}}
=
\left(
{2F(z)\over21375.716460702053\ldots\,\lambda_F}
\right)^{1/4}
w_H^2.
```

The finite electroweak value enters through

```tex
|v_F|={1\over\ell_H},
\qquad
\ell_H={\sqrt2\over v_{\rm EW}},
```

so the calculation has to map the stationary Wilson angle to the Connes sheet
scalar normalization:

```tex
|f_H\theta_{H,*}|=|v_F|={v_{\rm EW}\over\sqrt2}.
```

## Finite-Triple Compatibility

The Hosotani scalar should be checked against the finite spectral triple data:

- KO dimension 6 grading and real-structure signs;
- Poincare-duality multiplicity matrix;
- determinant-one hypercharge lift;
- survival of the `Q` projection on the neutral vacuum component;
- compatibility of the scalar Hessian with the Connes sheet length.

These checks decide whether the Wilson scalar can carry the finite Higgs
coordinate used in the D10 potential.

## Rejected Realization Rows

Record a failed row if the calculation gives:

- a curvature-shifted tensor in the Schur channel;
- an independent second operator beyond `A_j^\dagger A_j`;
- a current frame distinct from the frame that gives `A_j^\dagger A_j=J`;
- scalar support on pure `S1_Q`;
- a finite-sheet scalar incompatible with the KO6/Poincare-duality data.

## Localized Extraction Worksheet

Start from the D8/O8 quadratic expansion on `Gamma_EW`:

```tex
S_Gamma^(2)
=
{1\over2}\int d\nu_\Gamma
\left[
(K_H)_{ab}\partial_\mu\theta_H^a\partial^\mu\theta_H^b
+2\mu_\Gamma\xi^a\langle t,T_a y\rangle_\Gamma
+\mu_\Gamma^2\xi^a\xi^b\langle T_a y,T_b y\rangle_\Gamma
\right]
+{1\over2}{\rm Str}_\chi\log D_{\Gamma,\chi}(\theta_H).
```

Read the coefficients in a fixed order:

```tex
d\nu_\Gamma
\longrightarrow
Z_{\Gamma,0}
\longrightarrow
Z_{\Gamma,H}
\longrightarrow
\mu_\Gamma
\longrightarrow
(\sigma_\chi,d_\chi,z_\chi)
\longrightarrow
\theta_{H,*}.
```

The common-density pass is

```tex
d\nu_\Gamma^{\rm kin}
=
d\nu_\Gamma^{\rm source}
=
d\nu_\Gamma^{\rm det}.
```

With

```tex
f_H^2={Z_{\Gamma,H}\over L_H},
\qquad
x=w_H\theta_H,
```

canonical normalization gives

```tex
\alpha_{\rm mix}={\mu_\Gamma\over f_H},
\qquad
\beta_{\rm diag}={\mu_\Gamma^2\over f_H^2},
\qquad
R_{\rm tensor}=1.
```

In the point-projector convention,

```tex
Z_{\Gamma,H}={Q\over4}Z_{\Gamma,0},
\qquad
\alpha_{\rm mix}={2\mu_\Gamma\over\sqrt Q f_\Gamma},
\qquad
\beta_{\rm diag}={4\mu_\Gamma^2\over Q f_\Gamma^2}.
```

Decision rows:

```tex
(\alpha_B,\alpha_C)=(0,0)
\quad{\rm cohomological\ endpoint\ determinant},
```

```tex
(\alpha_B,\alpha_C)=(\kappa_B,0)
\quad{\rm rough\ CP^1\ endpoint\ Hamiltonian},
```

```tex
(\alpha_B,\alpha_C)=(0,\kappa_C)
\quad{\rm pure\ Casimir\ threshold}.
```

The active row is the cohomological endpoint determinant.  A sourced mixed row
has to derive

```tex
\alpha_C=-{4\over5}\alpha_B
```

from the localized D8/O8 action.

## Next Calculation

Compute `gamma_H`, `mu_Gamma`, and the Wilson-line kinetic coefficient from
the localized `Gamma_EW` action.  The same data must match the boundary Hodge
matrix used for `L_Q`, `L_2`, and the neutral-line norm.
