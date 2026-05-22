# AGENTS.md — DeVries String manuscript workspace

## Working mode

Work as a research assistant for a speculative high-energy-physics manuscript. Preserve precision. State assumptions, equations, consequences, and tests. Keep conjectures labeled as conjectures. The goal is a coherent Physical Review D manuscript, at least 60 pages in the long target version, whose open calculations are explicit enough that a referee can see what follows and what remains.

Active phase: conceptual manuscript development. Prioritize source reading, section architecture, physical interpretation, explicit assumptions, open analytical obligations, referee/advisor critique cycles, and Lean-style notes. Verification for this phase is LaTeX compilation with `make manuscript`. Leave numerical scripts, numerical sanity checks, and `make numbers` for a user-approved calculation phase.

## Core construction

Use

\[
Q(J)=\mu^2\begin{pmatrix}0&\sqrt J\\ \sqrt J&-J\end{pmatrix},
\qquad
x^2+Jx-J=0,
\qquad
J=s(s+1),
\]

with

\[
x_+(J)=\frac{\sqrt{J^2+4J}-J}{2},\qquad
x_-(J)=-\frac{\sqrt{J^2+4J}+J}{2}.
\]

The electroweak target is

\[
\sin^2\theta_{dV}=1-\frac{x_+(3/4)}{x_+(2)},
\qquad
\sin^2\theta_{\rm pole}=1-\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2}.
\]

Interpret this first as a pole-spectrum statement. Treat running weak mixing angles, MS-bar parameters, and Breit-Wigner conventions as separate schemes that must be related explicitly.

## Project constraints

- Focus on electroweak structure; Casimir language is a construction and historical clue. The final physics must come from electroweak, string, brane, Kaluza-Klein, or \(G_2\) mechanisms.
- Treat the DeVries relation as kinematical unless a dynamical derivation is supplied.
- String, brane, Kaluza-Klein, and G2 material should enter as possible mechanisms for the kinematical spectrum and its branch structure.
- Do not claim generations arise exactly from compactification topology. The working flavor caveat is: generation structure may be associated with an SO(32)-flavor interpretation and may or may not be compatible with compactification topology.
- Use pole masses when comparing W and Z. Distinguish pole masses from on-shell/Breit-Wigner inputs and from running parameters.
- The allowed electroweak deformation is the broken-to-unbroken vacuum ray. Do not introduce independent limits in which only W or only Z is made massless unless the manuscript is explicitly analyzing why those limits are outside the construction.
- Explain why the construction assigns the W comparison to \(J=3/4\) and the Z comparison to \(J=2\). If the derivation is absent, state it as the central open analytical calculation.
- The negative branch is an analytical object. Its relation to the Higgs/order-parameter scale is conjectural until derived.

## Style

Use affirmative exposition. Prefer equations, explicit assumptions, derived consequences, and falsifiable tests. Avoid filler numerics. Avoid decorative prose.
Do not use rhetorical contrast formulas. Avoid phrases such as “not X, but Y,” “X, not Y,” “not merely X,” “rather than,” and close variants — the canonical example is the Bond formula “shaken, not stirred.” This pattern is heavy in pretraining (it saturates referee reports and review prose), so it recurs across models and must be suppressed per sentence. Correct technical errors directly. Avoid adjectival positioning where an equation, assumption, consequence, or test can do the work.
Use Lean-style notes in `notes/lean/` when useful to trigger expert review. These notes are not compiled; they record obligations, assumptions, and open derivations.

Progress discipline: avoid fake work. Each work block should leave manuscript text, source inventory, conceptual notes, review records, or explicit open issues in a better state.
After each completed referee/advisor/implementation loop, compile the manuscript,
run the relevant prose scans, and commit the loop as a checkpoint.
Each substantial loop also uses a lightweight editor subagent, configured below
GPT-5.5, to flag banned contrast formulas, journalistic language, adjectival
positioning, and prose outside Physical Review D style. Store the editor report
in `reviews/`, resolve alerts, then run the prose scans.
Each substantial loop also includes a small recall pass: choose at least one
random bibliography or source-inventory entry and one random local note or
Lean-style note, inspect them, and record any equation, test, source-fragment
gap, or issue-ledger consequence.

## Repository commands

Run from repository root:

```bash
make numbers       # numerical DeVries spectrum and EW comparison
make test          # Python tests and project sanity checks
make manuscript    # compile manuscript/main.tex
make clean         # remove generated LaTeX artifacts
```

## Source discipline

- Use `context/source_inventory.md` before writing literature claims.
- Use `references/pdfs/` only as primary local source material.
- Treat `pdftotext` output as an access aid for PDFs. Keep the PDFs as source objects, because diagrams, plots, equation layout, and embedded images can be lost in text extraction.
- For mathematical content in PDFs, inspect the PDF view directly and transcribe formulas deliberately. Mark such formulas as agent-read transcriptions when they rely on visual reading.
- Add BibTeX entries to `manuscript/references.bib` before citing new papers.
- For each manuscript section, add a short “status” comment in the corresponding `.tex` file: derived, cited, conjectural, or open.

## Done definition

A task is done when the edited files compile or pass tests, the relevant section contains no hidden uncited factual claims, and `OPEN_ISSUES.md` has been updated with any remaining analytical gap.
REMEMBER TO CLOSE AND REMOVE ISSUES THAT HAVE REACHED THE SUCCESS CRITERIUM, AND COMMIT ===============
