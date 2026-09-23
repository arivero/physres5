# Iteration 3 verdict: does the single GHU trace force the de Vries point?

**Verdict: KILLED at class level (cross-confirmed: codex GPT-5.5
constructor UNFORCED/NO-GO + Fable-5 adversary REFUTED/MIS-POSED, fully
consistent; all algebra verified in `calc/iter3_checks.py`). Class killed:
tree-level quadratic reduction of a single trace-normalized Yang–Mills
term of a compact group, on ANY internal background (any space, flux,
condensate, level set, host group). Candidate (h) closes after one
iteration because the kill is a derivation, not a search failure.**

Question as registered (`notes/LOG.md`, iteration 3); raw arm outputs
`loop/OUT-codex-iter3.txt`, `loop/OUT-claude-iter3.md`.

## The theorem (the adversary's general form; the constructor's
## observation is the two-mode special case)

For every internal background, the transverse-vector kernel of the single
trace is

    K_T(B) = B·1 + D†D,   D = internal background covariant derivative —

a Gram structure (the vector–scalar cross term is purely longitudinal;
the one indefinite term in the trace, the Nielsen–Olesen ⟨F^bg,[a,a]⟩
coupling, touches scalars only). Consequences, each verified:

1. **Static Schur ≥ 0**: any retained/eliminated mode split gives
   Γ_P(0) ≥ 0; the de Vries kernel needs Γ_P(0) = −μ².
2. **Gram cone**: the static compression obeys γ²C ≤ s(αC + m₀²); s = 0
   forces γ = 0 (the commutator that mixes IS the open channel's contact —
   vertex without seagull is impossible). The de Vries point
   (s = m₀ = 0, γ = α = 1) violates the cone maximally (det = −C).
3. **No resolvent at all**: diagonalizing D†D, the pure-YM transverse
   sector is a direct sum ⊕(B + λ_i); the trace's kernel is
   basis-removable while the de Vries resolvent is not (X₊ ∉ R(C)).

"Locking and landing come apart": the coefficients ARE trace-locked (the
(h) intuition was right — no continuous modulus survives within one
internal factor), and the locked point is the Manton/Gram class, not de
Vries. **Forced to the wrong place** — stronger than UNFORCED.

## Cross-checked specifics

- **Minimal sector**: no 4D vector closed channel (internal components are
  scalars); a massless internally-charged open channel is a contradiction
  (massless ⇔ ker D ⇔ internal singlet ⇔ empty portal) — so the family
  coordinates r and map weight are undefined there (mis-posed). Landing:
  seagull Gram mass M² = g²v²·C per channel (SU(3) adjoint ad-Casimir
  spectrum {2 ×3, 3/4 ×4, 0 ×1} verified); ratio class 0.375 vs de Vries
  0.7769; angle class = rational embedding-trace numbers (Manton's table:
  SU(3) 3/4, O(5) 1/2, G₂ 1/4; Fairlie charge-one 1/4). This locates the
  recorded Lim–Maru–Hasegawa data point at the γ = 0 stratum.
- **First KK level** (constructor): the p–Q mixing vanishes by mode
  orthogonality (∫u_n = 0; Killing frames divergence-free) — γ = 0 with
  m₀² = λ₁/(μ²R²); consistent with the general theorem.
- **EYM escape dispatched**: the recorded universal KK 2×2 needs the
  Einstein–Hilbert term (second term — outside (h)) and fails anyway
  (trace > 0 vs −C; PSD det ≥ 0 vs −C).
- **Map-slot split** (bears on ledger (a)): the trace puts the algebraic
  Casimir in the vertex/seagull slots (A†A = C — the GHU asset survives)
  but the spectral Laplacian in the gap slot: S² without flux has no
  j = 1/2 channel; S² with monopole flux q shifts the map to ℓ(ℓ+1) − q²
  (j = 1/2 gap = 1/2, not 3/4; map-sensitivity controls 0.2968/0.3170);
  S³ gives the unshifted 4C but is dimensionally excluded (D = 11 vs the
  chirality-forced D = 10) and its symmetric background sits at a maximum
  of the trace's own potential (V″(1/2) = −6) — vacuum selection is
  one-loop Hosotani, not the tree trace. Sugawara/L0 is not rescued.
- **Corrigendum** (recorded here; `PRIOR-AGENT.md` is read-only): its line
  "Manton/Fairlie 1979: sin² = 1/4" conflates rows — 1/4 is the G₂/Fairlie
  value; Manton's SU(3) value is 3/4. Nothing load-bearing changes (the
  crux there was mass-ratio vs coupling-ratio, intact).

## Named escapes (all outside (h)'s admission premise)

E1 loop/self-consistent dynamics (Hosotani vacuum selection; gap-equation
evaluation at the pole) — the retired (d)-closure in geometric clothes;
any revival must derive g²/α = 1 from the loop dynamics, fresh admission.
E2 gravity-sector mixing (second term; fails anyway). E3 brane/localized
terms (per-term freedom returns). E4 noncompact groups (ghosts).

Deep ASSUMED flag (adversary): the identification of the channel label j
with an internal-space quantum number. If j is NOT geometric, the
geometric route never had anything to say — which redirects attention to
the readings where j is a mechanical/spin label: the orbit candidate (c).

## Ledger effect

(h) KILLED (one iteration; derivation-grade). Killed forcing classes so
far: 4D gauge symmetry (iter 1), spectral/self-consistency kinematics
(iter 2), single-trace geometric reduction (iter 3), HS realizations and
open-channel Z = 0 (by inheritance/admission). Remaining live LOCK
candidates: (c) orbit Lagrangian [next, iteration 4], (e) exact duality
[quick name-or-drop check], unadmitted E1 and Bracken–Green-class
characteristic identities. Remaining non-lock legs: (a) map selection
[now informed by the slot-split finding], (g) assignment.
