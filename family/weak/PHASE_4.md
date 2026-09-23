# PHASE 4 — Fermion sector extension (charged leptons)

Status: completed in Phase 4 of 7.
Inputs read: `/home/codexssh/weak/SEED.md`, `/home/codexssh/weak/PHASE_1.md`,
`/home/codexssh/weak/PHASE_2.md`, `/home/codexssh/weak/PHASE_3.md`,
`/home/codexssh/.claude/projects/-home-codexssh-weak/memory/MEMORY.md`.

Scope: extend the Casimir-locked seed to the charged-lepton sector under two
distinct hypotheses (parallel-seed Hypothesis A and Koide-coupled circulant
Hypothesis B), with full algebra; predict {m_e, m_mu, m_tau} numerically;
compare to PDG; quote sigma-deviations; identify which (if any) hits <5% on
all three masses.

PDG inputs (charged-lepton pole masses, 2024):
- m_e   = 0.5109989461 MeV, sigma_e   = 3.1e-9 MeV.
- m_mu  = 105.6583755  MeV, sigma_mu  = 2.3e-6 MeV.
- m_tau = 1776.86      MeV, sigma_tau = 0.12   MeV.

A note on the Koide ratio convention (the task statement has the ratio
inverted): Q := (m_e + m_mu + m_tau) / (sqrt(m_e)+sqrt(m_mu)+sqrt(m_tau))^2 is
the form that equals 2/3 (PDG value: Q = 0.66666051, deviation from 2/3 of
-6.16e-6, ~6 ppm). We use this convention throughout. Geometrically, Koide =
2/3 is the statement cos(theta) = 1/sqrt(2) where theta is the angle between
the sqrt-mass vector (sqrt(m_e), sqrt(m_mu), sqrt(m_tau)) and the (1,1,1)
direction in R^3.

---

## 1. Hypothesis A — parallel construction

### 1.1 Algebra

For each charged fermion f in {e, mu, tau}, postulate
```
                              [  0           sqrt(C2_f)  ]
   M_f^2  =  m_f0^2  *        [                          ]
                              [  sqrt(C2_f)  -C2_f        ]
```
with the same shape as the Phase-1 doublet/triplet seed (a=b=1).
Eigenvalues:
```
   lambda_pm = m_f0^2 * ( -C2_f  ±  sqrt(C2_f^2 + 4 C2_f) ) / 2.
```
Explicitly:
```
   lambda_+  = m_f0^2 * (sqrt(C2_f (C2_f + 4)) - C2_f) / 2     (positive, bounded)
   |lambda_-| = m_f0^2 * (sqrt(C2_f (C2_f + 4)) + C2_f) / 2    (positive, unbounded above)
```
Asymptotics:
- C2 -> 0:    lambda_+ ~ m_f0^2 * sqrt(C2);          |lambda_-| ~ m_f0^2 * sqrt(C2).
- C2 -> oo:   lambda_+ -> m_f0^2  (saturates at 1 in m_f0^2 units);
              |lambda_-| ~ m_f0^2 * C2 (linear, unbounded).

Carrying forward the previous (killed) Phase-4 run's observation: lambda_+/m_f0^2
saturates at 1 as C2 -> oo. This is rigorous from the closed form above.

We now test the four sub-options.

### 1.2 Sub-option A.1 — common m_f0, SU(2) reps, POSITIVE branch (lambda_+)

SU(2) irreps of dimension n have C2(n) = (n^2 - 1)/4. The map n -> lambda_+/m_f0^2:

| n   |  C2     |  lambda_+ / m_f0^2  |
|-----|---------|---------------------|
|  2  |  3/4    |  0.5687293          |
|  3  |  2      |  0.7320508          |
|  4  |  15/4   |  0.8204823          |
|  5  |  6      |  0.8729833          |
| 10  |  24.75  |  0.9625644          |
| 100 |  2499.75|  0.9996004          |
| oo  |  oo     |  -> 1               |

With common m_f0, the achievable mass-squared range is
[0.5687 m_f0^2, m_f0^2] -- spanning only a factor 1.758 in m^2 (1.326 in m).
Required experimental span:
- (m_tau / m_e)^2  = 1.21e7,
- (m_mu / m_e)^2   = 4.27e4.

These exceed the maximum achievable span (1.76) by 6.9e6 and 2.4e4 respectively.

Best A.1 attempt (n_e = 2, n_mu = 3, n_tau very large): with m_f0 = m_tau =
1776.86 MeV,
- m_e  pred = 1340.0 MeV (off by 2.6e5 %, sigma = +4.3e11),
- m_mu pred = 1520.3 MeV (off by 1.3e3 %, sigma = +6.2e8),
- m_tau pred = 1776.86 MeV (anchored exact).

**Verdict A.1: catastrophic failure**, by a factor ~6e6 in mass-squared span.
This is the saturation finding inherited from the killed Phase-4 run and is now
rigorously established from the closed-form lambda_+ = (sqrt(C2(C2+4)) - C2)/2.

### 1.3 Sub-option A.2 — common m_f0, reps of a DIFFERENT compact simple group

The required C2 spread to span (m_tau/m_e)^2 with lambda_+ ranging from
saturation (~1) down to ~ (m_e/m_tau)^2 ~ 1.21e-7 needs a smallest C2 of order
~ 1.5e-14 (using lambda_+ ~ sqrt(C2) for small C2, so C2 ~ lambda_+^2).

Minimum non-trivial Casimirs in fundamental reps of standard compact simple groups:
- SU(2) fund:    C2 = 3/4         (lambda_+ = 0.569)
- SU(3) fund:    C2 = 4/3         (lambda_+ = 0.667)
- SU(N) fund:    C2 = (N^2-1)/(2N) -> N/2 (grows with N)
- SO(N) vector:  C2 = (N-1)/2     (similar scale)
- G2 fund (7):   C2 = 2           (lambda_+ = 0.732)
- F4 fund (26):  C2 ~ 6           (lambda_+ ~ 0.873)
- E8 (smallest, 248): C2 = 30     (lambda_+ ~ 0.969)

All compact simple Lie groups have minimum non-trivial C2 of order 1 -- nowhere
near 1e-14. There is **no compact simple Lie group** whose fundamental rep
delivers lambda_+ small enough to fit m_e/m_tau on the saturating branch.

**Verdict A.2: impossible.** The saturation pathology of lambda_+ at large C2,
combined with the universal O(1) lower bound on minimum C2 in compact simple
Lie group irreps, makes the lepton mass span unreachable on the positive branch
for *any* compact simple group, not just SU(2).

### 1.4 Sub-option A.3 — generation-dependent m_f0,g + SU(2) reps

Six free parameters (m_f0,e; m_f0,mu; m_f0,tau; n_e, n_mu, n_tau) for three
data points. Trivially fits any masses without predictive content.

Minimal 1-parameter sub-case worth checking: m_f0,g = M * x^g with g = 0, 1, 2
and same SU(2) rep for all three (so lambda_+ factor cancels in ratios).
Then m_g = M * x^g (times constant). This requires a geometric progression
m_e : m_mu : m_tau = 1 : x : x^2:
- m_mu / m_e = 206.77,
- predicted m_tau = m_mu * (m_mu/m_e) = 21846.8 MeV,
- PDG m_tau = 1776.86 MeV.

Predicted m_tau is **12.3x** too large (off by +1130%); equivalently
(m_mu/m_e)^2 = 42753 vs (m_tau/m_mu) = 16.8, mismatch factor 2542.

**Verdict A.3: trivially fits with 6 DOF, no predictive content; the simplest
1-parameter "geometric" sub-case fails by a factor ~12 on m_tau.**

### 1.5 Sub-option A.4 — common m_f0, SU(2) reps, NEGATIVE branch (|lambda_-|)

|lambda_-| = (sqrt(C2(C2+4)) + C2)/2 ~ C2 for large C2 -- *unbounded*. So in
principle, common m_f0 + a SU(2) rep choice on the negative branch *can*
produce any mass span.

Grid search (n_e in {2,3,4,5}, n_mu and n_tau chosen to minimize residuals):
the best fit is

| n   | C2          | |lambda_-|    |
|-----|-------------|---------------|
| 4   | 3.75        | 4.5705        |
| 884 | 195363.75   | 195364.75     |
| 14867 | 55256922  | 55256923      |

with m_f0 = 0.239034 MeV.

Predictions:
- m_e_pred  = 0.51102351 MeV  (PDG 0.5109989, **+0.0048%**, **+7.9e3 sigma**)
- m_mu_pred = 105.65327 MeV   (PDG 105.65838, **-0.0048%**, **-2.2e3 sigma**)
- m_tau_pred = 1776.86 MeV    (anchored)

The relative errors are *within 5%* (indeed within 0.01%), but only because
SU(2) irreps come in integer dimensions -- the integer discretization gives
fractional residuals ~ 1/(2 n^2) ~ 1e-9 for n=14867 in the |lambda_-| value
itself, which translates to ~1e-5 in the predicted mass once one fits via the
ratio. So the residual is set by integer-discretization, not by the model
matching reality.

However, this comes at a phenomenological cost that makes A.4 *physically*
unviable:

1. **Absurd representation dimensions**: n_mu = 884 and n_tau = 14867 are
   ~3 and ~4 orders of magnitude above any rep that appears in 4D SU(2)_W
   gauge theory consistently with asymptotic freedom and unitarity bounds.

2. **Catastrophic gauge running**: SU(2)_W with a fermion in dim-n rep
   contributes T(R) = n(n^2-1)/12 to the gauge beta function. For n_tau =
   14867, T(R) ~ 2.7e11. The Landau pole would sit essentially at the EW
   scale; the SU(2)_W gauge coupling is non-perturbatively strong.

3. **Direct production**: charged-lepton-like states in such reps have ~n
   electroweak charge multiplets and would have been observed at colliders.

4. **No selection rule**: Phase 2's Rule (A) ("two lowest non-trivial SU(2)
   irreps") which gave {2,3} for the gauge sector becomes (4, 884, 14867)
   here -- a completely unrelated, fine-tuned triple.

**Verdict A.4: numerically achieves <5% on all three masses, but only at the
price of unphysical SU(2)_W reps with dim ~10^4. The fit is parametric, not
predictive: the integer choices (n_e, n_mu, n_tau) are tuned to data with no
selection rule, and three integers tuned to three masses is just a re-skin of
three Yukawa couplings.**

### 1.6 Summary of Hypothesis A

| Sub-option | Setup                                                      | Max frac err on {m_e, m_mu, m_tau}    | Verdict                                              |
|------------|------------------------------------------------------------|---------------------------------------|------------------------------------------------------|
| A.1        | common m_f0, SU(2) reps, lambda_+ (saturating branch)      | +2.6e5 % (m_e)                        | catastrophic failure (saturation, ratio bounded 1.76)|
| A.2        | common m_f0, other group reps, lambda_+ (saturating branch)| same: no group has C2_min < O(0.1)    | impossible                                           |
| A.3        | gen-dep m_f0,g + SU(2) reps (6 DOF)                        | 0 (trivial fit) / +1130% (1-param)    | trivial / minimal sub-case fails                     |
| A.4        | common m_f0, SU(2) reps, |lambda_-| (unbounded branch)     | +0.005% (within 5%) but n_tau ~ 1e4   | numerically passes but reps unphysical               |

---

## 2. Hypothesis B — Koide-coupled circulant

### 2.1 Construction

A general circulant in three complex parameters (c_0, c_1, c_2):
```
  C(c_0, c_1, c_2)  =  [[c_0, c_1, c_2],
                        [c_2, c_0, c_1],
                        [c_1, c_2, c_0]].
```
Eigenvalues (closed form, omega = exp(2 pi i / 3)):
```
   lambda_k = c_0 + c_1 omega^k + c_2 omega^{2k},  k = 0, 1, 2.
```
For three eigenvalues all real (required to identify with sqrt(m_e), sqrt(m_mu),
sqrt(m_tau)), the circulant must be Hermitian: c_2 = conj(c_1). Then with
c_0 = a real and c_1 = r exp(i phi) (so c_2 = r exp(-i phi)),
```
   lambda_k = a + 2 r cos(phi + 2 pi k / 3),   k = 0, 1, 2.
```

This is *exactly* the Foot-Krolikowski-Brannen geometric form of Koide's 1981
ansatz: the three sqrt-masses are the three points obtained by rotating a
fixed vector by 0, 120, 240 deg in a plane around a common center; the center
lies on the (1,1,1) axis in R^3.

### 2.2 Koide as a constraint on (a, r)

Identify lambda_k <-> sqrt(m_k). Compute:
```
   sum_k lambda_k   = 3 a                          (the (1,1,1) projection)
   sum_k lambda_k^2 = 3 a^2 + 6 r^2                (uses sum cos^2 = 3/2, sum cos = 0)
```
So
```
   sum_i sqrt(m_i)  =  3 a
   sum_i  m_i       =  3 a^2 + 6 r^2
```
and the Koide ratio is
```
   Q  =  sum m_i  /  (sum sqrt m_i)^2  =  (3 a^2 + 6 r^2) / (9 a^2)
                                       =  (1 + 2 r^2 / a^2) / 3.
```
**Koide Q = 2/3   <=>   r^2 = a^2 / 2   <=>   r = a / sqrt(2).**

This is the unique constraint Koide imposes on (a, r); the phase phi is free
and parameterizes the mass spread.

Geometric interpretation: r/a = 1/sqrt(2) is exactly cos(45 deg) = 1/sqrt(2),
i.e. the sqrt-mass vector lies on a cone of half-angle 45 deg around (1,1,1)
in R^3. This is Foot's geometric Koide.

### 2.3 Numerical prediction

Step 1 -- fix a from PDG (uses the sum of sqrt-masses, ~Tr-of-circulant data):
```
   a = (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau)) / 3
     = (0.7148419 + 10.2790260 + 42.1528172) / 3
     = 17.7155617 sqrt(MeV).
```

Step 2 -- impose Koide (the constraint of Hypothesis B):
```
   r = a / sqrt(2) = 12.5267938 sqrt(MeV).
```

Step 3 -- fix phi by anchoring one eigenvalue. Choose lambda_0 = sqrt(m_tau):
```
   cos(phi) = (sqrt(m_tau) - a) / (2 r) = 0.9753994
   phi = 12.7352 deg.
```

Step 4 -- predict lambda_1, lambda_2 (i.e. sqrt(m_mu), sqrt(m_e)):
```
   lambda_1 + lambda_2 = 3 a - sqrt(m_tau) = 10.9938679 sqrt(MeV)   (exact)
   lambda_1 * lambda_2 = (3 a^2 - 6 a sqrt(m_tau) + 2 m_tau) / 2 = 7.3391857 MeV
   => lambda_+ = 10.2799348 sqrt(MeV)  ->  m_mu_pred = 105.6770600 MeV
   => lambda_- =  0.7139331 sqrt(MeV)  ->  m_e_pred  =   0.5097005 MeV
```

### 2.4 Comparison to PDG and sigma-deviations

| State    | Predicted (MeV)   | PDG (MeV)         | Rel. err   | sigma deviation     |
|----------|-------------------|-------------------|------------|---------------------|
| m_e      | 0.50970047        | 0.51099895        | -0.2541%   | -4.2e5 sigma        |
| m_mu     | 105.67706         | 105.65838         | +0.01768%  | +8.1e3 sigma        |
| m_tau    | 1776.86 (anchor)  | 1776.86           | 0%         | 0 (anchored)        |

All three predictions are within 5% (indeed within 0.3%). The non-zero residual
arises entirely from the fact that Koide Q = 2/3 is satisfied by PDG only to
~6 ppm rather than exactly. Specifically, the predicted m_e is too small by
0.254%, exactly tracking the deviation (Q_PDG - 2/3) when propagated through
the 1-parameter Koide constraint.

The sigma deviations are enormous (1e4-1e5) because PDG charged-lepton masses
are measured to ridiculous precision (~10^-9 fractional uncertainty for m_e),
while Koide Q = 2/3 holds only to ~10^-5. Hypothesis B is therefore *not*
consistent with PDG at the experimental-sigma level -- it is consistent only
at the few-parts-per-thousand relative-error level. (The same is true of any
exact Koide ansatz; an O(alpha_em) RG correction is needed for sigma-level
agreement, well beyond Phase 4's scope.)

### 2.5 Group-theoretic origin of the 3x3

The Hermitian circulant
```
   [[a,    b,     conj(b)],
    [conj(b), a,    b    ],
    [b,    conj(b), a    ]]
```
is the most general Hermitian operator on a 3-dim space that commutes with
the cyclic-permutation operator P (the generator of Z_3 in its regular
representation). Three identifications:

1. **Z_3 = cyclic flavour symmetry**: the matrix is fixed by Z_3 acting by
   cyclic permutation of the three generations. This is the smallest discrete
   group whose regular representation has 3 distinct 1-dim irreps (omega^0,
   omega^1, omega^2) which label the three eigenvalues.

2. **S_3 = Weyl group of SU(3)**: Z_3 is the A_3 = cyclic subgroup of S_3.
   Promoting to full S_3 flips b <-> conj(b), which permutes lambda_1 <-> lambda_2
   (i.e. exchanges m_mu <-> m_e if those are the two non-tau eigenvalues).
   S_3 is the Weyl group of SU(3), so Hypothesis B has a natural embedding
   into an SU(3)_F flavour symmetry broken to its Z_3 center.

3. **Foot/Brannen/Koide geometric form**: the three sqrt-masses lie on a
   circle in the (1,1,1)^perp plane, equilaterally spaced. r is the
   circumradius (sqrt-mass scale of the spread); a is the center offset
   along (1,1,1); Koide Q = 2/3 forces the cone half-angle to 45 deg.

So Hypothesis B is naturally interpreted as: the charged-lepton sqrt-mass
matrix has a residual Z_3 (cyclic flavour) symmetry, with Koide Q = 2/3
emerging as the constraint that the matrix is "maximally chiral" -- the
sqrt-mass vector makes a 45 deg angle with the symmetric (1,1,1) direction.

### 2.6 Verdict on Hypothesis B

| Mass     | Within 5%? |  Mechanism                                     |
|----------|-----------|------------------------------------------------|
| m_e      |  yes (0.25%) | Koide constraint + anchor                  |
| m_mu     |  yes (0.02%) | Koide constraint + anchor                  |
| m_tau    |  yes (anchor) | Anchor (Tr-class spurion)                  |

**Hypothesis B passes the 5% criterion on all three masses.**

The residual O(10^-3) on m_e is the propagated ~10^-5 deviation of PDG-Koide
from exact 2/3, magnified by the small-eigenvalue sensitivity to a, r choice.
A natural Phase 5 refinement is to allow r/a to deviate from 1/sqrt(2) by
O(alpha_em / pi) ~ 10^-3 (one-loop QED running), which would absorb the
residual.

---

## 3. Side-by-side summary

| Sub-option | m_e rel.err | m_mu rel.err | m_tau rel.err | All <5% ? | Predictive (no free param tuned to data)? |
|------------|-------------|--------------|---------------|-----------|-------------------------------------------|
| A.1 (lam_+ saturated, SU(2)) | +2.6e5 %  | +1.3e3 %  | 0 (anchor)    | NO        | No -- catastrophic                         |
| A.2 (other compact group)    | impossible | impossible | impossible    | NO        | No -- forbidden by group theory            |
| A.3 1-param geometric        | -          | -          | +1130%        | NO        | Yes (1 param), but fails                   |
| A.3 generic (6 DOF)          | 0          | 0          | 0             | trivial   | No -- 6 params, 3 data                     |
| A.4 (|lam_-|, SU(2))         | +0.005%    | -0.005%    | 0 (anchor)    | yes*      | No -- 3 integer reps tuned, no rule        |
| **B (Hermitian Z_3 circulant + Koide)** | **-0.254%** | **+0.018%** | **0 (anchor)** | **YES**   | **YES (1 free param phi; Q=2/3 imposed; a from Tr)** |

\* A.4 numerically passes but requires SU(2)_W reps of dim 884, 14867 -- physically excluded.

---

## 4. Conclusion

Among the five examined extensions of the Casimir-locked seed to the charged-
lepton sector:

- **Hypothesis A.1, A.2 catastrophically fail** because the upper eigenvalue
  lambda_+ of the 2x2 Casimir seed saturates at m_f0^2 (saturation is rigorous
  from the closed form). Common m_f0 + SU(2) reps cannot span more than a
  factor 1.76 in m^2; common m_f0 + reps of any other compact simple group
  cannot do better, because every compact simple Lie group has minimum
  non-trivial C2 of order 1.

- **Hypothesis A.3 with 6 free parameters trivially fits but has no
  predictive content**; its 1-parameter geometric sub-case (m_f0,g = M x^g,
  same rep) fails on m_tau by +1130%.

- **Hypothesis A.4 (negative branch, common m_f0) numerically achieves <5%
  on all three masses** -- but only with SU(2)_W reps of dim {4, 884, 14867},
  which are not consistent with phenomenology (Landau pole at the EW scale,
  no selection rule, three integers tuned to three data points). It is a
  re-skin of three Yukawa couplings, not a derivation.

- **Hypothesis B (Hermitian Z_3 circulant with Koide constraint r = a/sqrt(2))
  achieves <5% on all three masses with only one free parameter (phi),
  the other two (a, r) being fixed by the trace-class data sum_i sqrt(m_i)
  and by the Koide constraint Q = 2/3 respectively**. Residual error
  (0.254% on m_e, 0.018% on m_mu) is set entirely by the ~6 ppm deviation
  of PDG Koide from exact 2/3, propagated through the smallest eigenvalue's
  sensitivity to the (a, r) choice.

**Hypothesis B is the unique sub-option that achieves <5% on all three
charged-lepton masses with a non-trivial group-theoretic motivation
(Z_3 cyclic-flavour symmetry = cyclic subgroup of the SU(3)_F Weyl group =
Foot/Brannen geometric Koide).** It is logically independent from the
Phase-1-3 Casimir-locked 2x2 seed -- the connection is structural (both
are Hermitian matrices fixed by group-theoretic constraints; eigenvalues =
"Casimir-like" invariants of the constraining group) rather than dynamical.

---

## 5. Open issues handed to downstream phases

- **Phase 5 (RG matching)**: the residual O(10^-3) deviation of Hypothesis B
  on m_e is the right size for a one-loop QED correction to Koide
  (delta Q / Q ~ alpha_em / pi ~ 2.3e-3). Phase 5 should check whether
  running the Koide constraint from a UV scale (~m_0 ~ 106 GeV or higher)
  to the electron mass scale via QED + QCD predicts r/a = 1/sqrt(2) at
  some natural matching scale.

- **Phase 6 (quark sector)**: try Hypothesis B on the quark sector. The
  up-type Koide Q_u = (m_u + m_c + m_t)/(sqrt(m_u)+sqrt(m_c)+sqrt(m_t))^2
  is far from 2/3 (Q_u ~ 0.27); the down-type is closer (Q_d ~ 0.52).
  Neither is exact 2/3, so the Z_3 circulant + Koide doesn't apply
  directly. A possible extension is a generation-dependent r/a (still one
  parameter per sector, plus phi).

- **Phase 7 (sBootstrap / SO(32) connection)**: the Hermitian Z_3 circulant
  is naturally embedded in SU(3)_F, which itself is a subgroup of the
  SO(32) string spectrum decomposition mentioned in the seed. The
  Z_3 = cyclic part of S_3 = Weyl(SU(3)) link is suggestive but not
  derivative; this should be made precise in Phase 7.

- **Cross-phase**: the {2, 3} of Phase 2 (rule A: two lowest non-trivial
  SU(2) irreps) and the Z_3 of Phase 4 are independent group-theoretic
  inputs. A unified picture would derive both from a single parent
  algebraic structure -- candidate parents: the lowest two reps of the
  Z_3 quotient of SU(3) flavour, or a Z_3-graded extension of SU(2)_W.
  Speculative; deferred.
