# dvFable loop log

Run started 2026-06-11. Protocol: `GOALS.md` (normative, fixed this date).
One entry per iteration / session step. Raw arm outputs in `loop/`.

## Iteration 0 — goals fixed, scorecard frozen, ledger opened (2026-06-11)

- `GOALS.md` written: goal tree (G0/T1/T2/T3 with pre-registered standards,
  G1 gating, G2 conditional, G3), anti-goals, de-certifications, loop
  protocol (two arms, constructor/adversary, swapped per iteration; verdict
  vocabulary FORCED / UNFORCED-WITH-BOUNDARY / KILLED / RE-SCOPED).
- Equivalence decision recorded (AGENTS.md + ledger): orbit `X+ = β²`, gap
  `X = C/(X+C)`, quadratic `X²+CX−C = 0` are one equation
  (`calc/devries_core.py` §§2–4); gap form is the live formulation.
- De-certified: LOOP-LOG iter-1 "κ RESOLVED by canonical ½X² norm" (a
  convention; knob re-opens as r = γ/α); "(½,1) unique (j≤4)" as originally
  scored (superseded datum).
- G1.0 scorecard frozen (`calc/scorecard_2026.py`,
  `notes/2026-06-11-empirical-scorecard.md`): de Vries pull is 0.4–1.6σ
  depending on datum/convention; primary = PDG-live 2026 BW masses,
  0.223339(153), pull +1.56σ; ~3 matched digits. The historical 0.42σ is no
  longer quotable. Uniqueness re-score: (½,1) still unique within 3σ (j≤4).
- G1.1 ledger opened (`notes/2026-06-11-forcing-candidates-ledger.md`):
  entries (d) gauge/Stueckelberg lock [RUNNING, iter 1], (a) map selection
  [QUEUED, iter 2], (b) HS potential origin [QUEUED], (b′) Z=0 compositeness
  [KILLED at admission — Z⁻¹ = 1 + C/(X₊+C)² > 1, `calc/devries_core.py` §7],
  (c) orbit quantization [QUEUED; archival kill-test first], (e) composite/
  dual [QUEUED, demoted], (g) global-form assignment [QUEUED].

## Iteration 1 — dispatched 2026-06-11 (candidate d)

Question (registered): does 4D gauge invariance + locality + single scale +
the fixed channel content (open gauge vector p, closed Q ∈ Im A_j,
A†A = C·1) force `Γ_P(B) = B − μ⁴C/(B+μ²C)` (one-square, r = 1, no surviving
contact), or does a local invariant deformation with r ≠ 1 / shifted
denominator exist? Decision rule pre-registered in the prompts: FORCED
(term-by-term proof + Sugawara control showing map non-selection) vs
UNFORCED-WITH-BOUNDARY (explicit deformation + minimal excluding structure
named). "Open/conditional" inadmissible.

- codex arm (GPT-5.5 xhigh, CONSTRUCTOR): `loop/PROMPT-iter1-codex.txt` →
  `loop/OUT-codex-iter1.txt` (background).
- Claude arm (Fable 5, ADVERSARY): prompt copy
  `loop/PROMPT-iter1-claude-adversary.txt` → output to be saved as
  `loop/OUT-claude-iter1.md` on completion.
- Cross-check on completion; all algebra re-verified in `calc/` before any
  verdict is recorded.

Interim (codex arm returned, all its algebra verified in
`calc/iter1_gauge_lock.py`, j=1/2 and j=1):

- codex decision: UNFORCED-WITH-BOUNDARY. Positive sub-lock: with the
  Stueckelberg law δQ = C⁻¹A∂ε, the zero-derivative invariant sector is
  one-dimensional — gauge invariance forces the one-square
  `(κμ²/2)||A†Q − p||²` (b = −a/C, d = a/C), killing independent
  gap/mixing/contact ratios. Evasion: kinetic normalization Z_Q = z gives
  r = √z (and the Stueckelberg weight s is the same knob — verified).
- Orchestrator synthesis (verified, claims 7–8, pending adversary
  cross-check): the invariant family is structurally unable to reach the de
  Vries kernel at all — num Γ_P(0) = 0 identically (massless pole + one
  massive Gram pole for every Z_p, Z_Q, Z_m, κ), and the π-extended static
  mass sector is PSD (det = κCμ₁² ≥ 0) while the de Vries polynomial
  X² + CX − C needs constant term −C < 0: the would-be matching forces
  μ₁² = −κ(C+1)/(κC+1) < 0. So the local-invariant-Lagrangian sub-class is
  KILLED by derivation (the old PSD no-go re-derived inside the class, not
  assumed), and the de Vries kernel exists only as the contact-subtracted,
  energy-dependent correlator kernel — the subtraction is not a local
  invariant. Boundary named: unsubtracted spectral representation
  (superconvergence kills the contact) + current-algebra Ward normalization
  of residue/weight (Weinberg-sum-rule-class conditions).
- Sugawara control: the whole family carries C → c²C; the principle locks
  nothing about the map (as pre-registered).

VERDICT (iteration 1, cross-confirmed): **UNFORCED-WITH-BOUNDARY.**
Both arms returned independently; adversary output saved to
`loop/OUT-claude-iter1.md`; its nine inline checks transcribed to
`calc/iter1_adversary_checks.py` (all pass). Distilled verdict + side
results (Theorem A massless-pincer, resolvent necessity from X+ ∉ R(C),
Lorentz-type dichotomy, frame-scoped PSD statement, extended
de-certifications) → `notes/2026-06-11-iter1-gauge-lock-verdict.md`.
Boundary named: B1 induced-gap/no-CDD (μ²H_QQ = H_QP H_PQ ⇔ R = μ²ν₀),
B2 portal minimality (unsubtracted Σ, single vertex), B3 channel-universal
kinetics (ASSUMED; = orbit (c3)). Ledger candidate (d): strike 1 of 2.

## Iteration 2 — dispatched 2026-06-11 (candidate d, strike 2; roles swapped)

Question (registered): derive B1+B2 from a defined, non-ad-hoc dynamical
principle, or show every candidate principle fails or smuggles the
condition. Candidate principles named in the prompts: (1) KSRF-class
current-algebra saturation made exact by the finite internal sector;
(2) no-CDD/compositeness of the closed channel as a theorem of a defined
bound-state dynamics (portal-generated Q); (3) mutual-induction/bootstrap
fixed point (H_QQ generated as the static Schur complement of the open
channel through the same portal). Controls pre-registered: the principle
must lock coefficients GIVEN the map and must NOT rescue the Sugawara
c = 1/2 map's failed value; B3 stays flagged as assumed. Decision rule:
FORCED-AT-BOUNDARY / UNFORCED-WITH-BOUNDARY (→ candidate (d) retires on
the two-strike rule) / KILLED.

- Claude arm (Fable 5, CONSTRUCTOR this time): background agent; prompt
  copy `loop/PROMPT-iter2-claude-constructor.txt` → output to be saved as
  `loop/OUT-claude-iter2.md`.
- codex arm (GPT-5.5 xhigh, ADVERSARY this time):
  `loop/PROMPT-iter2-codex.txt` → `loop/OUT-codex-iter2.txt` (background).

Interim (codex adversary returned; verification pending constructor):

- codex: no route derives B1+B2. (1) KSRF SMUGGLES — HLS algebra: KSRF I
  (g_ρ = 2F_π²g_ρππ) holds for every a (the Ward low-energy theorem,
  Harada–Kugo–Yamawaki); KSRF II (m_ρ² = 2F_π²g_ρππ²) forces a = 2 =
  one-pole-saturation/VMD, a dynamical input; a finite zero-mode sector
  supplies "one retained state", not "no CDD/contact". (2) no-CDD FAILS:
  Σ = γ²μ⁴C/(B + m₀² + λμ²C) is positive, unsubtracted, causal, violates
  B1 unless δ = 0, λ = γ² — m₀ ≠ 0 consistent ⇒ no-CDD is a choice.
  (3) bootstrap FAILS: closure H_QQ = w·H_QP K_P(0)⁻¹ H_PQ gives
  hs = (w−1)g² — homogeneous: at w = 1, s = 0 EVERY h > 0 is a fixed point;
  h = 1 is inserted, not derived. No analyticity/unitarity/asymptotics
  theorem ties residue to pole position (that tie IS the CDD ambiguity).
- Orchestrator note: clean spectral reformulation of the lock —
  B1 ⇔ Σ_j(0) = μ² channel-universally (de Vries: Σ(0) = μ⁴C/μ²C = μ² for
  all C; the Casimir enters only the dispersion, the static seed mass is
  channel-blind). Candidate phrasing for any future forcing principle.
- codex next-question proposal: a microscopic finite-sector Hamiltonian
  whose Ward identities give Σ_j(0) = μ², s = η = 0, and forbid m₀ — "if
  not, B1+B2 remain postulates."

VERDICT (iteration 2): **UNFORCED-WITH-BOUNDARY (second strike) — candidate
(d) RETIRED.** Constructor arm: the Claude agent failed 3× on
infrastructure (2× API-529, 1× session token limit — user restored tokens
afterwards); the codex-constructor hedge returned UNFORCED-WITH-BOUNDARY,
agreeing with the codex adversary: all three routes leave the single
dimensionless closure g²/α = 1 free. PROTOCOL DEVIATION recorded: iteration
2 is single-family (GPT-5.5 both seats); mitigations: independent runs +
all algebra Claude-verified in `calc/iter2_boundary_checks.py` + the
iteration-1 Fable-5 adversary had already characterized the boundary
cross-family. Retry prompts disclosed the homogeneity/KSRF hazards
(bar-raise, disclosed). Distilled verdict →
`notes/2026-06-11-iter2-boundary-verdict.md`. Ledger: (d) RETIRED;
(b) KILLED BY INHERITANCE (same closure, check 4); (h) admitted.

## Iteration 3 — dispatched 2026-06-11 (candidate h: GHU single-trace normalization)

Question (registered): reduce the single higher-D Yang–Mills kinetic term
`−(1/4g_D²)F_MN F^MN` on the internal SU(2) zero-mode sector (GHU frame:
portal = algebraic current T_a, A†A = C given; the internal gauge
components supply Q and the Goldstone π) and compute the 4D transverse
quadratic (p, Q, π) system's family coordinates `(r = γ/α, s, η, Z_Q, m₀,
map weight)` from the one trace. DECIDE: FORCED-AT-GHU — the single-trace
reduction lands at the de Vries point (r = 1, s = η = m₀ = 0, zero-mode
map) for a forced-geometry reason; controls: the same reduction must
locate the recorded standard-GHU data point (Lim–Maru–Hasegawa: Goldstone
+ separate scalar, no Schur block) in the family, must NOT rescue the
Sugawara/L0 weighting, and must show the Casimir (not 2j+1) trace; OR
UNFORCED — name the modulus/ratio carrying the residual freedom (e.g.
internal metric moduli, radius ratios, level normalization) and state
which forced ingredient, if any, could fix it. SCOPE: zero-mode quadratic
level; no global compactification claims; D8/O8 stays closed; the de Vries
number is never input.

- codex arm (GPT-5.5 xhigh, CONSTRUCTOR): `loop/PROMPT-iter3-codex.txt` →
  `loop/OUT-codex-iter3.txt` (background).
- Claude arm (Fable 5, ADVERSARY): prompt copy
  `loop/PROMPT-iter3-claude-adversary.txt` → output saved as
  `loop/OUT-claude-iter3.md` on completion.

VERDICT (iteration 3, cross-confirmed): **KILLED at class level —
candidate (h) closes in one iteration (derivation-grade kill).** Both
arms converged (constructor: UNFORCED/NO-GO, minimal sector γ = 0
Manton/Gram landing, first-KK mixing vanishes by orthogonality, proposed
the general Gram theorem; adversary: proved it — K_T(B) = B + D†D for
every background ⇒ static Schur ≥ 0, Gram cone γ²C ≤ s(αC+m₀²), direct
sum/no resolvent — REFUTED + MIS-POSED, "forced to the wrong place").
All algebra verified in `calc/iter3_checks.py` (incl. SU(3) ad-Casimir
{2×3, 3/4×4, 0×1}, monopole-shifted map C − q² with controls
0.2968/0.3170, S³ 4C + V″(1/2) = −6, EYM 2×2 trace/det double
obstruction). Corrigendum recorded: Manton SU(3) sin² = 3/4 (1/4 is
G₂/Fairlie). Distilled verdict → `notes/2026-06-12-iter3-ghu-verdict.md`.
Side note (user-prompted, same night): the (c₁,c₂)-quadratic shape
inventory → `notes/2026-06-11-quadratic-shape-inventory.md` +
`calc/quadratic_shape_family.py` (form is cheap; the de Vries content is
the diagonal c₁ = c₂ = the retired closure; possible future candidate:
Bracken–Green characteristic identities, admission pending a literature
pass).

## Iteration 4 — dispatched 2026-06-12 (candidate c: orbit Lagrangian; roles swapped)

Question (registered): the 2005 de Vries construction derives β²γ = √C
from three inputs — (c1) de Broglie/Landé–Pauli angular-momentum rule
L = γm₀βc·r = √(j(j+1))ħ, (c2) the period condition T_r = h/(m₀c²)
(orbit period = Compton period; eliminates the radius — the lock in orbit
clothes), (c3) same-radius matching across channels (= B3/single-μ).
QUESTION: exhibit a defined Lagrangian/action system (relativistic rotor,
two-body bound state, string segment/flux tube, rotating loop —
constructor's choice, defined class) in which (c2) — and with it the full
relation β²γ = √C — is an equation of motion, constraint, or quantization
theorem rather than an input; or show each Lagrangian class needs (c2)
imposed by hand (UNFORCED-WITH-BOUNDARY, name the minimal structure).
Pairing classification mandatory, no scans: the dynamics must select
among {γβ = √C, γβ² = √C} × {L = j, √(j(j+1)), j+½} rather than have the
de Vries pairing picked by hand. Controls: a valid mechanism must not
equally produce the alternative pairings (scope statement required);
state where j(j+1) arises (angular-momentum operator vs dimension);
ASSUMED list mandatory ((c3)/B3, the channel set {½,1}, the EW matching
M_j ∝ β_j). The de Vries number is never input.

- Claude arm (Fable 5, CONSTRUCTOR): background agent; prompt copy
  `loop/PROMPT-iter4-claude-constructor.txt` → output saved as
  `loop/OUT-claude-iter4.md`.
- codex arm (GPT-5.5 xhigh, ADVERSARY): `loop/PROMPT-iter4-codex.txt` →
  `loop/OUT-codex-iter4.txt` (background).

User directive recorded in `GOALS.md` G3 (2026-06-12): at terminal close,
condense everything into a LaTeX paper, complete but human-readable — no
ledger labels, iteration numbers, verdict vocabulary, or plan language in
the typeset text.

Interim (codex adversary returned; verified in `calc/iter4_orbit_checks.py`;
constructor pending):

Cross-import (user-directed, 2026-06-12, while iteration 4 runs):
`~/kkFable` notes + didactic paper spied read-only →
`notes/2026-06-12-kkfable-cross-import.md`. Five imports: (1) the sister
run's two open postulates (c = 1, bare-Casimir map) ARE this program's
lock and map — the open cores coincide; (2) new ledger candidate (i),
the Hessian/variational formulation (kkFable "Deliverable 4": first-order
D_patch whose second variation is the signed block with c = 1 forced) —
admitted, QUEUED; (3) spin^c Dirac-square fact (C_G − C_K + |ρ|², not bare
j(j+1)) corroborates the iteration-3 slot split → ledger (a); (4)
carrier-level assignment obstruction (j = ½ slot coloured; inverted
assignment cos² > 1) → ledger (g); (5) angle landscape on the carrier
(strictly undefined, or a free Wilking modulus (1+t)/((1+t)+k_Y)) → T3
table; plus the didactic tex as the G3 style template.

- codex verdict: UNFORCED-WITH-BOUNDARY + candidate KILL of the orbit
  reading as a derivation. Weight table confirmed (0.223101 / 0.207729 /
  0.119793 / 0.357143; general identity T = k·h/(m₀c²) ⇒ γβ² = √C/k — the
  weight IS the lock). Frame bookkeeping: an invariant one-tick-per-orbit
  worldline clock gives the γ-weighted member (0.2077); the de Vries
  weight-1 member uses the rest-frame Compton period as a lab coordinate
  period (proper phase 2π/γ per orbit — not a covariant tick rule).
  De Broglie phase harmony on a closed orbit gives ∮p·dq = nh
  (L-quantization), not the period condition. Zitter models (Barut–Zanghi,
  Hestenes, Rivas): frequency 2mc²/ħ ⇒ the 0.1198 member — FAILS.
  Nambu–Goto rigid rotation ⇒ Regge J = E²/(2πσ) — wrong family;
  generalized profiles smuggle. Central-force rotor: single V(r)
  interpolation = smuggle; WITH same-radius imposed the required force is
  channel-dependent (ratio 1.853) — no channel-blind potential.
  Half-integer ORBITAL L at j = 1/2 forbidden by single-valuedness —
  candidate kill: the orbit reading may only ever be a mnemonic for the
  gap form. ASSUMED flags: channel set by hand; M ∝ β needs same-radius +
  channel-blind scale; composite-W identification reopens iteration-1
  content. No indexed publication derives the period condition from an
  action. Last-digit slip in its β table noted (immaterial).
