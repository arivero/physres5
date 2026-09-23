# Milestone 5 neutral scalar Hessian rank test -- 2026-05-25

## Question

Milestone 5 asks whether the scalar part of the D10 boundary action fixes the
de Vries scalar targets

```tex
v_Q^2=\mu_B(\rho,\tau)^2(1+\sqrt3),
\qquad
\lambda_H={3+\sqrt{57}\over32(1+\sqrt3)}.
```

Equivalently, with

```tex
J_v=1+\sqrt3,
\qquad
J_H={3+\sqrt{57}\over8},
```

the radial scalar mass target is

```tex
M_H^2=J_H\mu_B^2.
```

## One-field radial Hessian

Use a canonically normalized radial field `h` and write the most general
renormalizable local radial potential in the neutral boundary sector as

```tex
V_h(h)=a(\rho,\tau)h^2+b(\rho,\tau)h^4+V_0(\rho,\tau),
\qquad b>0.
```

At a nonzero stationary point,

```tex
h_0^2=-{a\over2b}.
```

The radial Hessian is

```tex
M_h^2=V_h''(h_0)=8b h_0^2=-4a.
```

The selector normalization used in the article is

```tex
h_0^2=v_{\rm EW}^2=2v_Q^2.
```

If the `v_Q` selector is imposed, then

```tex
h_0^2=2J_v\mu_B^2.
```

The Hessian becomes

```tex
{M_h^2\over\mu_B^2}=16bJ_v.
```

In the equivalent notation

```tex
V_h={\lambda_H\over4}(h^2-2v_Q^2)^2,
```

one has `b=lambda_H/4` and therefore

```tex
M_h^2=4\lambda_Hv_Q^2=2\lambda_Hv_{\rm EW}^2.
```

The de Vries scalar target is recovered by setting

```tex
\lambda_H={J_H\over4J_v}.
```

Thus the written scalar potential is internally consistent:

```tex
4\lambda_HJ_v=J_H.
```

Numerically,

```tex
J_v=2.732050807568877,
\qquad
J_H=1.3187293044088437,
\qquad
\lambda_H=0.12067210653215474.
```

## Rank of the scalar data

The one-field Hessian supplies two scalar observables, `h_0^2` and `M_h^2`.
The local potential supplies two independent functions, `a(\rho,\tau)` and
`b(\rho,\tau)`.  Therefore the pair

```tex
h_0^2=2J_v\mu_B^2,
\qquad
M_h^2=J_H\mu_B^2
```

is a two-equation target for two scalar coefficients unless the action computes
`a` and `b`.

The same conclusion holds after adding neutral mixing fields.  Let
`\Phi^A=(h,\phi^i)` be the neutral scalar variables.  At a stationary point,
the physical masses are the eigenvalues of the symmetric Hessian

```tex
H_{AB}={\partial^2 V\over\partial\Phi^A\partial\Phi^B}.
```

Requiring one eigenvalue to equal `J_H mu_B^2` is one spectral constraint on
the entries of `H_{AB}`.  Positivity restricts signs, but it does not select
the square-root number `J_H`.

## Negative branch status

The constants are the absolute values of the negative root of the same
quadratic used by the weak-angle slice:

```tex
|X_-(2)|=1+\sqrt3=J_v,
\qquad
|X_-(3/4)|={3+\sqrt{57}\over8}=J_H.
```

This is an algebraic extension of the de Vries pattern.  A scalar Hessian
would make it dynamical only if the D10 boundary action produced the same
fixed-point quadratic for the neutral radial mode.  The present scalar action
is a standard local Higgs potential with free mass and quartic coefficients, so
the negative-branch values are compatible targets rather than forced Hessian
eigenvalues.

## Decision

Milestone 5 fails as an induced scalar selector in the present route.  The
written potential reproduces the scalar numbers when its coefficients are set
to the negative-branch targets, but the neutral boundary scalar Hessian has
enough coefficient freedom to fit those values.  The D10 action would need a
new fixed-point or Schur mechanism in the scalar sector to turn
`J_v,J_H,lambda_H` into predictions.
