# Iteration 1 verdict: gauge/Stueckelberg protection of the coefficient lock

**Verdict: UNFORCED-WITH-BOUNDARY (cross-confirmed: codex GPT-5.5 constructor
+ Fable-5 adversary, independent; all algebra verified in
`calc/iter1_gauge_lock.py` and `calc/iter1_adversary_checks.py`).**

Question as registered (`notes/LOG.md`, iteration 1): does 4D gauge
invariance + locality + single scale + the fixed channel content force
`Γ_P(B) = B − μ⁴C/(B+μ²C)` (one-square, r = 1, no surviving contact)?

Raw arm outputs: `loop/OUT-codex-iter1.txt`, `loop/OUT-claude-iter1.md`.

## Answer: no — and the failure is a structured pincer, not a shrug

1. **Static lock exists but bites the wrong way (DERIVED).** With strict
   channel content — fields (p, Q) only, Q a 4D vector in Im A_j,
   δQ = nA∂λ for any n (the only covariant laws; Hom is one-dimensional) —
   the unique invariant static structure is the displacement-square family,
   and every local gauge-invariant quadratic action gives
   `Γ_P(B) = B·R(B)`: the open channel stays massless (Theorem A; the
   adversary's general proof via the invariant variable D = Q − nAp, my
   claims 7/check 3/check 9 confirm for all Z_p, Z_Q, Z_m/η, κ, n, any
   channel count and sign structure). The de Vries kernel has
   `Γ_P(0) = −(γ²/α)μ² ≠ 0`: **not gauge-realizable in strict content.**
   The de Vries form is the invariant square minus its own contact, and the
   subtraction is not a local invariant (codex: removing the contact forces
   a = b = d = 0). Locked-theory spectrum: {0, κμ²(1+C)} — a Gram/PSD
   system. This re-derives the old PSD no-go inside the class instead of
   assuming the block shape.
2. **With the mandatory compensator, invariance is toothless (DERIVED).**
   A massive open channel requires the Goldstone π (Schwinger-mechanism
   pole; Theorem A). Once π exists, Stueckelberg completion makes ANY
   quadratic massive-vector action gauge-invariant (Ruegg–Ruiz-Altaba), and
   the adversary exhibits the five-parameter invariant deformation family
   (r = γ/α, m₀, s, η, Z₁) whose pole polynomial is `X² + CX − r²C`
   (check 4) — a continuous invariant family through the de Vries point.
3. **Pincer ⇒ UNFORCED.** Without π: de Vries forbidden. With π: everything
   allowed. In neither branch does gauge symmetry select r = 1.
4. **Sugawara control (as pre-registered):** every statement is equivariant
   under A → cA, C → c²C. The analysis locks nothing about the map; map
   selection (zero-mode vs L0 weighting) stays a separate question.

## Cross-checked side results (all verified)

- **Lorentz-type dichotomy (adversary).** Vector Q supplies the C-tracking
  resolvent but no C-independent static piece; scalar Q supplies a Proca
  contact but no resolvent; 2-form Q gives portal sandwiches f(C)·C with
  the wrong C-tracking. The kernel needs vector-Q exchange AND a scalar
  compensator simultaneously — the inherited channel content was incomplete
  for its own target, and the 4D transcription of the gap-equation
  realizations (Lorentz types of the channels) is an ASSUMED embedding.
- **Resolvent necessity (adversary, check 7).** `X+(C)` is irrational over
  R(C) (C(C+4) squarefree), so no local polynomial/rational-in-C kernel can
  produce `X+(C)` as an identity in C. Any mechanism matching de Vries
  identically in the Casimir must contain the resolvent denominator. The
  Feshbach/gap shape is necessary, not merely sufficient. (A two-point fit
  at C = 3/4, 2 by a rational kernel is over-determination, not forcing.)
- **Frame-scoped PSD statement (orchestrator, claim 8).** In the
  Q-transforming frame (all mixing from the displacement square), even the
  π-extension cannot reach the de Vries polynomial: matching would need
  μ₁² = −κ(C+1)/(κC+1) < 0. Dissolved in the inert-Q frame (the adversary's
  family has independent invariant mixing ⟨Q, AP⟩). Recorded so neither
  over-claim survives: the PSD obstruction is frame-scoped; the deformation
  freedom is general.
- **De-certification extended.** The prior run's "conditional gauge pass"
  was internal-SU(2) covariance only; Theorem A shows it was never a 4D
  gauge pass. The de-certified "κ = 1 from canonical norm" stays dead: r is
  rescaling-invariant (adversary task 1d).

## The named boundary (what would exclude the deformations)

Dynamical conditions, not symmetry (adversary §1.5; codex's Ward proposal
in its narrow gauge-Ward form is refuted by transversality — gauge Ward
identities constrain only the longitudinal kernel; the viable versions are
spectral/current-algebra statements):

- **B1 — induced-gap / no-CDD:** `μ²H_QQ = H_QP·H_PQ` on Im A_j (with
  H_PQ = μ²A† this gives H_QQ = μ²C and r = 1). Spectral form: the
  closed-channel pole has residue R = μ²·ν₀, channel-universally — the
  closed channel has no intrinsic gap; everything is portal-induced.
  Weinberg-compositeness/no-CDD class, applied to the CLOSED channel
  (distinct from the open-channel Z = 0 killed at admission).
- **B2 — portal minimality:** s = η = 0; spectral form: Σ(B) obeys an
  unsubtracted dispersion relation (no contact) with single current vertex.
- **B3 — channel-universal kinetic normalization** (Z per channel equal):
  a standing framework assumption — the same-radius/single-μ postulate (the
  orbit form's r_½ = r₁, ledger entry (c3)) in field language. Flagged, not
  derived.

KSRF anchor: B1 has the shape of KSRF II (m_V² ∝ g²·scale²), which in QCD
follows from current-algebra saturation + vector dominance and is known to
be dynamical, not symmetry-derived. The question whether a finite internal
sector makes a KSRF-class statement exact is iteration 2.

## Ledger effect

Candidate (d), strike 1: UNFORCED-WITH-BOUNDARY. The sub-class
"local invariant gauge-field Lagrangian forces de Vries" is KILLED by
derivation. Strike 2 (iteration 2) targets the boundary itself: derive
B1+B2 from a non-ad-hoc dynamical principle or show each candidate
principle fails/smuggles. If strike 2 also returns
UNFORCED-WITH-BOUNDARY, candidate (d) retires per the two-strike rule.
