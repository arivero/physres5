# AGENTS.md — DeVries String manuscript workspace

## Working mode

Work as a research assistant for a speculative high-energy-physics manuscript. Preserve precision. State assumptions, equations, consequences, and tests. Do not inflate conjectures into derivations. The goal is a coherent manuscript, up to 50 pages, whose open calculations are explicit enough that a referee can see what follows and what remains.

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

- Focus on electroweak structure; Casimir language is a construction and historical clue, not the final physics by itself.
- Treat the DeVries relation as kinematical unless a dynamical derivation is supplied.
- String, brane, Kaluza-Klein, and G2 material should enter as possible mechanisms for the kinematical spectrum and its branch structure.
- Do not claim generations arise exactly from compactification topology. The working flavor caveat is: generation structure may be associated with an SO(32)-flavor interpretation and may or may not be compatible with compactification topology.
- Use pole masses when comparing W and Z. Distinguish pole masses from on-shell/Breit-Wigner inputs and from running parameters.
- The allowed electroweak deformation is the broken-to-unbroken vacuum ray. Do not introduce independent limits in which only W or only Z is made massless unless the manuscript is explicitly analyzing why those limits are outside the construction.
- Explain why the construction assigns the W comparison to \(J=3/4\) and the Z comparison to \(J=2\). If the derivation is absent, state it as the central open analytical calculation.
- The negative branch is an analytical object. Its relation to the Higgs/order-parameter scale is conjectural until derived.

## Style

Use affirmative exposition. Prefer equations, explicit assumptions, derived consequences, and falsifiable tests. Avoid filler numerics. Avoid decorative prose. Avoid habitual contrast formulas such as “this is X, not Y” unless the negative statement prevents a concrete error.

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
- Add BibTeX entries to `manuscript/references.bib` before citing new papers.
- For each manuscript section, add a short “status” comment in the corresponding `.tex` file: derived, cited, conjectural, or open.

## Done definition

A task is done when the edited files compile or pass tests, the relevant section contains no hidden uncited factual claims, and `OPEN_ISSUES.md` has been updated with any remaining analytical gap.
