# dvFable — fixed goals, terminal standards, and reasoning protocol

Fixed 2026-06-11. Normative for every session of this run. Read after
`AGENTS.md`; supersedes `loop-history/long-term-devries-research-plan.md`
(kept as archive). The startup sequence in `AGENTS.md` still applies.

## The object

The de Vries electroweak relation. With `X+(C)` the positive root of
`X² + C X − C = 0` and `C = j(j+1)`:

    sin²θ_W = 1 − X+(3/4)/X+(2) = 0.2231013223…   (j_W = 1/2, j_Z = 1)

Equivalence decision (recorded once, ends the orbit-vs-gap framing question):
the orbit form `X+ = β²` with `β²γ = √C`, the gap form `X = C/(X+C)`, and the
quadratic `X² + CX − C = 0` are the same equation (verified in
`calc/devries_core.py`). The charter's "orbit-loophole question" is therefore
form-independent. The gap form is the live formulation; orbit quantization
survives as ledger candidate (c), not as a separate question.

## Goal tree

### G0 — terminal goal

Decide whether the relation has a physical origin or is a coincidence, and
document the result at Phys-Rev-D standard. Three admissible terminal states,
each with a pre-registered standard. Nothing else terminates the project.

**T1 — FORCED (origin found).** A principle qualifies only if all five hold:

1. No-de-Vries test: the principle is statable and motivated without
   reference to the measured weak angle.
2. The coefficient lock is a theorem, both halves: the shape lock `r = γ/α = 1`
   (coupling vs closed-channel gap) and the map normalization
   (`A†A = C·1` from the algebra, no level shift, no free residue).
3. The channel assignment `γ: j=0, W: j=1/2, Z: j=1` is an output.
4. The principle explains why the Sugawara control fails (a principle equally
   compatible with the `L0` normalization would "derive" `sin² = 0.3014` and
   is dead on arrival).
5. It survives a dedicated adversarial iteration (roles swapped) and yields at
   least one consequence it was not built to fit.

T1 closes G1 by itself; geometric embedding (G2) is conditional on T1, not a
part of its standard.

**T2 — NO-GO (impossibility).** Only an unrestricted impossibility
(Galois/Arrow class) qualifies, adversarially checked by the other arm and
literature-checked. A class-restricted no-go never terminates anything: it is
filed UNFORCED-WITH-BOUNDARY with its named class boundary plus the escape
direction, and triggers a candidate-or-retire decision at the next planning
step (CORRECTION rule of `PRIOR-AGENT.md`).

**T3 — QUANTIFIED COINCIDENCE.** Admissible only when all of:

1. The candidate ledger is frozen under the admission rule (below), and every
   entry is terminal (KILLED, or retired after two consecutive
   UNFORCED-WITH-BOUNDARY verdicts).
2. Two consecutive planning reviews admit no new candidate (this
   operationalizes dv2's "same verdict re-confirmed twice, no new
   sub-question").
3. A quantitative look-elsewhere / over-determination accounting exists,
   built from a pre-registered hypothesis-class enumeration (function form,
   root choice, (j_W, j_Z) pair, `C = j(j+1)` vs alternatives, scheme/datum
   choice), scored against the frozen empirical scorecard.

### G1 — gating task (charter-fixed; current; nothing builds on top of it)

Close the forcing question: is there a principle that forces the de Vries
form for the electroweak vectors, with the lock and assignment as outputs?

- **G1.0 Empirical scorecard freeze** (one session, no loop). Decide the
  datum (PDG-live 2026 separate masses vs the direct-ratio entry), the mass
  convention (Breit–Wigner vs pole), propagate errors, state the pull and the
  effective digits N_eff to explain, and re-score the inherited claim
  "(1/2, 1) is the unique half-integer pair within 3σ for j ≤ 4" against the
  frozen data. Scope is the tree-level on-shell target only — no running, no
  thresholds, no m_H (G2 material). Inputs are then frozen; re-scored only at
  terminal close. Pre-commitment: if the frozen datum sits ≥3σ from the
  tree-level relation, any T1 claim must carry a stated scheme story, or the
  framing converts to T3.
- **G1.1 Forcing-candidates ledger** (one session). Admission rule — a
  candidate enters only if (a) its principle is statable without the measured
  angle, (b) it has a kill-test executable in ≤1 iteration, (c) it is not a
  rephrasing or an additional realization of an existing entry. The ledger is
  a ledger of forcing principles: realizations of `X = C/(X+C)` score zero
  and are logged as drift.
- **G1.2 The loop** (protocol below) on the sharpest sub-question, one per
  iteration, until G1 closes in a T1/T2/T3 shape.

### G2 — conditional on T1: geometric/UV embedding

Forced geometry only: D=10, K6 minimal cosets (`CP² × CP¹` class), internal
SU(2), gauge-Higgs normalization. The D8/O8 on `CP²×CP¹` package is closed by
the 2026-05-25 source-balance no-go; any revived branch must be a new
compactification ansatz, never a source patch. Selection rule and
normalization must be outputs. Then scheme/threshold phenomenology. The
tower-branch `j=3/2` state at 96.54 GeV vs the CMS 95.4 GeV diphoton excess
(2.9σ local / 1.3σ global) is a branch discriminator only — mutually
exclusive with the finite `SU(2)_2` branch, never a confirmation channel, and
any pre-T1 work on it is drift.

### G3 — the write-up

The paper for whichever terminal state closes. Typeset = derived; meta and
not-yet-derived live in `%` comments only. The originality ledger must
separate (1) the 2005 de Vries/Rivero lore, (2) dv2-run derivations,
(3) dvFable derivations.

User directive (2026-06-12, standing): when the research is definitely
done — a terminal state, not before — condense the results into a LaTeX
paper that is complete but written for a human physicist reader. No
internal scaffolding may appear in the text: no ledger labels
((a)–(h), B1–B3, E1–E4), no iteration numbers, no verdict vocabulary
(FORCED/UNFORCED-WITH-BOUNDARY/…), no goal/plan/objective language. Every
result is stated as physics (definitions, propositions, derivations,
controls as cross-checks), with the run's bookkeeping translated into
ordinary prose and the notes/calc record cited only as supplementary
material. Theorems carry their assumptions inline, not by reference to
loop state.

## Anti-goals (standing; violating one is drift, log it)

- Relitigating the PSD/2×2-block no-go, in either direction.
- Integer scans / numerological fits (`M^{pqr}` trap). Re-scoring an inherited
  look-elsewhere claim against frozen data is T3 accounting, not a scan.
- Reviving the D8/O8/`CP²×CP¹` source package.
- Direct Sugawara `L0` normalization (failed control, `sin² = 0.3014`);
  horizontal-only current metric (failed control, `sin² = 0.2423`).
- New realizations of `X = C/(X+C)`; new formalism (fields, geometry, TeX
  apparatus) inside G1; article building before a terminal state (the
  2026-05-25 session's three in-loop LaTeX articles were displacement
  activity — named as such).
- Pre-T1 diphoton/phenomenology work; corpus numerology (α ≈ 135.3,
  Higgs/top/Z pole relations, μ ≈ √(v·M_Z/2)) — excluded pre-T1, re-enter
  only as T3 over-determination data.
- Mid-loop PDG chasing (inputs frozen at G1.0).

## De-certified prior claims (do not cite as settled)

1. LOOP-LOG iteration 1: "opus's open κ knob RESOLVED by codex variational
   form: κ=1 fixed by canonical ½X² norm." De-certified: the ½X²
   normalization of an auxiliary order parameter with no kinetic term is a
   convention; the same knob re-opened as `r = γ/α` in
   `loop-history/milestone1-q-oscillator-coefficient-lock-2026-05-25.md`.
   The lock is field-normalization-invariant and remains the open core.
2. "(1/2, 1) is the unique half-integer pair within 3σ (j ≤ 4)": a bounded
   scan scored against the superseded 0.42σ datum. Re-score at G1.0.

## The loop (G1.2 protocol)

Per iteration:

1. One sub-question, with the decision rule pre-registered in the prompt
   before dispatch (what result settles it which way).
2. Dispatch BOTH arms in background with the full context inlined
   (codex sandbox cannot reliably read local files; web search works):
   - codex arm: GPT-5.5 xhigh via
     `codex exec -s read-only --skip-git-repo-check - < loop/PROMPT-… > loop/OUT-… 2>&1`
   - Claude arm: a general-purpose background agent (Fable 5).
   Roles are asymmetric — constructor vs adversary — and swap every
   iteration. Both arms online-verify state of the art and originality.
3. On completion: cross-check; resolve any disagreement by explicit
   calculation in `calc/`; every algebraic claim in the verdict gets a script
   that asserts and exits 0.
4. Verdict vocabulary is closed: **FORCED / UNFORCED-WITH-BOUNDARY / KILLED /
   RE-SCOPED**. "Open/conditional/plausible" is inadmissible. Two consecutive
   UNFORCED-WITH-BOUNDARY verdicts retire the candidate (boundary recorded),
   not the project.
5. Record: distilled verdict note in `notes/` (dated, verdict line on top),
   raw arm outputs in `loop/`, one entry in `notes/LOG.md`. Then formulate
   the next sub-question.

Budgets: ≤2 iterations per ledger candidate (construct, then adversarial
confirm/refute); any FORCED claim needs a third iteration with swapped roles
plus both controls (Sugawara; Casimir-vs-dimension) before T1 is declared.
Every statement in a verdict carries DERIVED or ASSUMED status; an ASSUMED
statement may not be consumed by the next iteration's question — it must
first be the target.

## Where things go (extends AGENTS.md)

- `GOALS.md` — this file (normative).
- `notes/LOG.md` — the dvFable loop log, one entry per iteration/session step.
- `loop/` — dispatch prompts and raw arm outputs (`PROMPT-…`, `OUT-…`).
- `notes/`, `calc/` — as in AGENTS.md. Never write through a symlink.
