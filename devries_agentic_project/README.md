# DeVries String agentic manuscript project

This repository is a Codex-ready research workspace for turning the current DeVries String paper into a complete manuscript of up to 50 pages.  It is organized so that Codex can work in parallel on analytical calculations, source audits, manuscript expansion, LaTeX compilation, and referee-style criticism, while GPT-5.5 Pro is used as the high-level conceptual reviewer.

## Immediate objective

Produce a self-contained manuscript that makes the following construction precise:

\[
Q(J)=\mu^2\begin{pmatrix}0&\sqrt J\\ \sqrt J&-J\end{pmatrix},
\qquad
x^2+Jx-J=0,
\qquad J=s(s+1),
\]

with positive branch

\[
x_+(J)=\frac{\sqrt{J^2+4J}-J}{2},
\]

and electroweak comparison

\[
\sin^2\theta_{dV}=1-\frac{x_+(3/4)}{x_+(2)}=0.22310132\ldots.
\]

The manuscript must explain the observable target as a pole-spectrum statement,

\[
\sin^2\theta_{\rm pole}=1-\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2},
\]

then identify which claims are derived, which claims are numerical coincidences, which claims are conjectural, and which analytical calculations remain.

## Repository layout

- `AGENTS.md` — durable Codex instructions. Keep this concise; task-specific detail lives elsewhere.
- `.codex/config.toml.example` — optional local Codex profile template.
- `.codex-plugin/` and `skills/` — reusable Codex skills for manuscript work.
- `manuscript/` — REVTeX source, sections, macros, figures, and bibliography.
- `calculations/` — analytical notes, numerical checks, and tests.
- `codex_tasks/` — task packets to paste into Codex Cloud or assign to separate Codex agents.
- `prompts/` — prompts for Codex, GPT-5.5 Pro, referee review, and chapter work.
- `context/` — project memory, source inventory, style rules, and completion criteria.
- `references/pdfs/` — source PDFs copied from the sandbox.
- `scripts/` — build, test, context-pack, and project sanity scripts.

## Local quick start

```bash
cd devries_agentic_project
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pytest pyyaml
make test
make manuscript
```

The LaTeX build uses `latexmk` and `pdflatex`. The calculation tests use standard Python plus `pytest`.

## Codex use

Start with a planning pass:

```bash
codex --cd . --ask-for-approval on-request "Read AGENTS.md and codex_tasks/T00_bootstrap_repo.md. Produce an execution plan before editing."
```

For Codex Cloud, push this repository to GitHub, connect the repository in Codex web, then create separate tasks using the files in `codex_tasks/`. The file `CODEX_CLOUD.md` gives the cloud execution order.

## Manuscript work rule

Every nontrivial statement in the manuscript must be one of:

1. derived from equations written in the manuscript;
2. supported by a cited source in `references.bib` and `context/source_inventory.md`;
3. explicitly labeled as conjecture, programmatic interpretation, or open calculation.

## First run checklist

```bash
make inventory
make numbers
make manuscript
make test
```

Then run the Codex task sequence in `codex_tasks/T00_bootstrap_repo.md` through `T09_50_page_expand_compile.md`.
