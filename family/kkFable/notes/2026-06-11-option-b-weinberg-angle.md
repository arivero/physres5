# N3 — The Weinberg angle under Option B

Date: 2026-06-11.

**VERDICT: C5's prediction sin²θ_W = 1/4 is DEAD under Option B, twice over.
Strictly: with no dynamical U(1)_Y on X_{1,1} (N2 §4) there is no g_Y and no
θ_W at all. Counterfactually (granting a dynamical Y normalized on the base
block, e.g. on a repaired carrier): sin²θ_W = x1/(x1 + k_Y·x2) =
(1+t)/((1+t)+k_Y), a continuous function of the free Wilking modulus t for
every fixed normalization k_Y — a free modulus, not a prediction. Hand
re-derivation below; reproduces R5(c) without computer algebra.**

Conventions: N0. Inputs: N1 (dictionary), N2 (Y status), T2 (metric blocks),
T3 (inertia rule), R5(c).

## 1. The strict statement

θ_W is defined by tan θ_W = g_Y/g_2 between two dynamical couplings. N2 §4:
on X_{1,1} under Option B there is no massless hypercharge boson, hence no
g_Y. The observable θ_W does not exist in the reduced theory; "predicting" it
is vacuous. This is the primary verdict; §2–§4 treat the standard
counterfactual so that the comparison with Option A's 1/4 is quantitative.

## 2. Counterfactual setup: the KK coupling rule, by hand

Expansion block.
- Variables/domain: invariant metric family on X_{1,1} (T2):
  g_t = x1·(−B)|_{m_0} ⊕ x2·(−B)|_{m_3}, B = Killing form, x1 = fibre scale,
  x2 = base scale, t := x1/x2 − 1. Gauge fields from Killing vectors K_a.
- Rule (Weinberg 1983 / T3, cited): after KK reduction the 4D gauge kinetic
  term for the isometry direction a is (1/g_a²) ∝ I_a = ∫_X g(K_a, K_a) dvol
  (the "inertia" of that Killing vector).
- Weak factor: the right-SO(3) Killing vectors are vertical (N1 §2: they
  generate the fibre orbits), so g(K,K) picks up the m_0 block only:
  pointwise g(K,K) = x1·(−B)(k,k) for the corresponding k ∈ so(3) ⊂ vertical
  frame. Hence 1/g_2² = c·x1 with c a t-independent constant (volume
  normalization common to all factors).
- Hypothetical hypercharge: any Y realized along the base/H8 structure (the
  flux line; or the fibre circle after an M^{p,q,r}-type repair, whose norm
  is set by the base-block geometry it is fibred over) has its inertia carried
  by the m_3 block: 1/g_Y² = c·k_Y·x2, with k_Y the group-theory
  normalization of the Y generator (the analogue of Option A's k_Y = 3),
  fixed once a matter convention is fixed — but t-independent.
- Status: derived (the only input beyond linear algebra is the cited inertia
  rule).

## 3. The angle

  g_Y²/g_2² = (1/x2)·(1/k_Y) / (1/x1) = x1/(k_Y·x2)

  sin²θ_W = g_Y²/(g_2² + g_Y²) = x1/(x1 + k_Y·x2) = (1+t)/((1+t) + k_Y).

Spot values (k_Y = 1): t = −3/5 (squashed Einstein) → 2/7 ≈ 0.286; t = 0
(normal homogeneous) → 1/2; t = +1 (3-Sasakian) → 2/3. Monotone increasing in
t: d/dt [(1+t)/(1+t+k_Y)] = k_Y/(1+t+k_Y)² > 0. Every value in (0,1) is
attained as t ranges over the metric family for any fixed k_Y > 0. These
match R5(c)'s sweep (its k_Y = 1 column: 0.2857, 0.5, 0.6667 — agreement to
the displayed digits).

## 4. Why no choice of k_Y restores rigidity

Schur's lemma fixes ratios of invariant quadratic forms only **within one
simple factor**: on a simple g, the invariant-form space is one-dimensional,
so I(T₃)/I(Y) is metric-independent when both T₃ and Y sit inside that one
factor — Option A's situation (both inside the electroweak SU(3); ratio
Tr T₃²/Tr Q² = 1/4 on the lepton triplet, rep-independent). On the semisimple
su(3) ⊕ so(3), the invariant-form space is two-dimensional (one scale per
ideal): x1 and x2 are independent. Option B puts T₃ in one ideal and Y's
normalization in the other; their ratio x1/x2 is the free shape modulus t
that no group theory constrains. Fixing k_Y rescales the curve, never
collapses it: the t-derivative above is strictly positive for every k_Y.
The two Einstein points (t = +1, −3/5) pin t only by a curvature condition —
a vacuum-selection assumption, not gauge group theory; and even then the
value depends on the unproven k_Y. This is the C5 cross-factor caveat
(Established, T3d) doing its decisive work — and it is Weinberg's own 1983
caveat: the coupling ratio persists only while both generators live in one
simple factor.

## 5. The trade, quantitatively

| | Option A | Option B (X_{1,1}) |
|---|---|---|
| colour | absent | present (base SU(3)_c) |
| dynamical Y | yes (λ_8 inside EW SU(3)) | **no** (N2 §4) |
| tree sin²θ_W | 1/4, rigid (Schur, k_Y = 3) | undefined; counterfactually (1+t)/((1+t)+k_Y), free |

Whether the De Vries scale-free 0.2231 — Option A's preferred sharp number
(wastebook C7) — survives Option B is settled in N5 (it does not; its EW slot
assignment fails). So Option B on X_{1,1} retains **no** sharp electroweak
number from either mechanism.

## 6. Counterargument pass

1. *"A dynamical principle (e.g. Einstein condition) selects t, restoring a
   prediction."* Then the prediction is conditional on (a) the selection
   principle, (b) the k_Y convention, and (c) a dynamical Y existing at all —
   (c) already fails on this carrier (N2). At best a two-assumption
   conditional value, qualitatively weaker than Option A's
   metric-independent 1/4. Recorded, not adopted.
2. *"Maybe Y's inertia also sits on the fibre block, cancelling t."* Y
   commutes with the weak SO(3) (it must, to survive EW breaking as part of
   U(1)_EM); a vertical realization would place it inside the fibre isometry,
   where the only Cartan is already T₃ (N1 §4) — then Y ∝ T₃, which fails on
   the matter spectrum (doublet members would have equal electric charge).
   So a hypothetical Y is necessarily base-normalized, and the cross-factor
   freedom stands.
3. *"Rep-dependence: Option A's 1/4 needed the lepton-triplet choice; maybe
   a clever Option-B multiplet fixes the ratio."* Traces over a multiplet fix
   k_Y (the analogue of 3), never x1/x2 — the modulus is metric freedom, not
   representation freedom. No multiplet choice touches t.

## 7. Kill criteria

- Exhibiting an SU(3)×SO(3)-invariant identity forcing x1/x2 (would
  contradict the two-ideal Schur count; none can exist).
- A derivation making k_Y AND t both dynamical from one source — that is the
  named repair route (Einstein-point selection + matter embedding), which
  would re-open this note as a conditional-prediction note on a repaired
  carrier.

## Sources

- archive/verification_20260531/T2.md (metric family, t).
- archive/verification_20260531/T3.md (inertia rule; Schur rigidity; the
  free cross-factor ratio g_cust²/g_EW² = 1/(1+t), here re-labelled).
- archive/verification_20260531/R5.md part (c) (prior sympy sweep; numerical
  agreement noted in §3).
- docs/Weinberg_Charges_From_Extra_Dimensions_1983.md (coupling-from-inertia
  rule and the simple-factor caveat).
