# Paper normalization plan

## Purpose

The current 62-page reference draft preserves the conceptual work, source trail, theorem targets, and review scaffolding.  The next editorial phase should turn that reference draft into a journal-shaped paper.  The main task is to move workshop language out of the manuscript body and present the argument as physics: definitions, assumptions, constructions, consequences, and open theorem targets.

Reference commit:

```text
5943f77 Reference 62-page PRD draft
```

## Diagnosis

The draft reads partly like a conversation because the manuscript body contains research-process language.  Examples of material to relocate or rewrite:

- section-status paragraphs;
- referee-facing checklists and decision ledgers;
- phrases such as current draft, next calculation, next pass, route passes, and decision tree;
- internal score or planning language;
- tables whose purpose is project management and whose content belongs outside
  exposition.

These elements are useful for the workspace.  They should live in appendices, review notes, Lean notes, or planning files.  The main paper should speak in the voice of a Physical Review D article.

## Rewrite Rules

1. Rewrite the main text around claims:
   \[
   \hbox{definition}\to\hbox{assumption}\to\hbox{construction}\to
   \hbox{consequence}\to\hbox{open theorem}.
   \]
2. Replace project-management phrases with paper-level statements.
3. Keep theorem targets in Appendix D and cite them from the body only where they clarify a claim.
4. Keep one compact route-comparison table in the body; move detailed working ledgers to an appendix or review note.
5. Convert Sec. IX into a conclusion/status section in journal tone.
6. Preserve the conceptual framing: pole placement, radical placement, ordered \(J\)-assignment, negative branch as scalar-functional target, and route competition among endpoint, interval, and \(G_2\) mechanisms.
7. Preserve source discipline: every factual literature claim in the normalized text must trace to `context/source_inventory.md` or `context/concept_claims_matrix.md`.

## Section-Level Tasks

| Section | Normalization action |
|---|---|
| Abstract | Keep the clue status and central theorem target; remove process language. |
| Introduction | Present motivation, placement burden, and paper map in journal prose. |
| Secs. II--IV | Keep algebra, pole scheme, and electroweak assignment formal. |
| Sec. V | Present the negative branch as a scalar-functional problem, with route details shortened. |
| Secs. VI--VI.G | Recast endpoint, interval, and \(G_2\) routes as candidate mechanisms. |
| Sec. IX | Turn claim hierarchy and referee tests into a concise status/conclusion section. |
| Appendix D | Hold theorem targets, acceptance criteria, and detailed proof obligations. |

## Review-Loop Rule

Every substantial rewrite loop must call three subagents before implementation:

1. **Referee A subagent, GPT-5.5.** Skeptical PRD referee focused on correctness, scheme discipline, and overclaiming.
2. **Referee B subagent, GPT-5.5.** Independent PRD referee focused on string/Kaluza--Klein/\(G_2\) depth, source control, and manuscript structure.
3. **Advisor subagent, GPT-5.5.** Research advisor focused on conceptual synthesis, new mechanisms, and high-risk improvements.

Record their outputs in `reviews/` before editing.  Then implement revisions that improve derivational clarity, source traceability, or paper-like exposition.
Each loop after Loop 48 must also satisfy a closure-output gate: issue closure,
route rejection, failed derivation record with a narrower next target, or a
source-backed theorem entry with acceptance and rejection equations.  Repeated
target polishing fails the normalization plan.

## Acceptance Criteria

- `make manuscript` succeeds.
- The compiled paper remains at or above 60 REVTeX PRD preprint pages unless the user approves a shorter journal target.
- Main-body prose reads as a paper, while review/process material lives in appendices or repo notes.
- `OPEN_ISSUES.md`, `context/concept_claims_matrix.md`, and Lean notes reflect any remaining analytical gaps.
