# family/: curated sibling projects

physres5 is the umbrella repository for the de Vries–Rivero electroweak
relation sin²θ = 1 − x₊(3/4)/x₊(2) = 0.22310132. Between May and July 2026
about fifteen local workspaces explored the same relation. This folder
keeps their lasting work in one place: each subfolder holds verbatim copies
of project-authored papers, notes and scripts, plus a `SUMMARY.md` written
during curation on 2026-09-23.

**Start with [`IDEAS.md`](IDEAS.md).** It merges the results of all ten
folders, lists each idea once with every project that found it, and opens
with five concrete actions for the manuscript.

## Contents

| Folder | Source (local, 2026-09-23) | Git | What it holds | Canonical document | Verdict |
|---|---|---|---|---|---|
| [`chats-regge-kk/`](chats-regge-kk/SUMMARY.md) | `~/chats/devries-regge-kk-research-project`, `~/chats/prl-devries-electroweak` | none | Claude and Codex tracks from a ChatGPT corpus; claim ledger; gate notes | `claudeFinal.tex` (48 pp), `codexVersion.tex` (80 pp), PRL letter + supplement | conditional construction of A1; its physical readings were withdrawn by dv2 and dvFable |
| [`dv2/`](dv2/SUMMARY.md) | `~/dv2` | local only | clean restart, seven milestones, D10 boundary-current route | `paper/d10-new-advances-2026-05-25.tex` (13 pp) | parked: scoped no-prediction theorem |
| [`dvFable/`](dvFable/SUMMARY.md) | `~/dvFable` | local only | pre-registered forcing tests with scripts | none (no terminal state reached) | every candidate principle leaves r = γ/α free |
| [`physres6/`](physres6/SUMMARY.md) | `~/physres6` | local only | PRL spin-off: KK moduli fix sin²θ and α | `manuscript/main.tex` (3 pp) | major revision; α follows from the scale tie |
| [`marathon/`](marathon/SUMMARY.md) | `~/marathon` | none | hand-derived synthesis paper | `main.tex` (14 pp) | exact algebra verified; significance left to a trials audit |
| [`kkorchestra/`](kkorchestra/SUMMARY.md) | `~/kkorchestra` | none | CP²/Aloff–Wallach KK programme | NCG translation (26 pp), custodial lecture (8 pp) | labels get a geometric home; the matrix stays underived |
| [`kkFable/`](kkFable/SUMMARY.md) | `~/kkFable` | local only | Option-B re-derivation on X_{1,1} | `out/OPTIONB_X11_DIDACTIC.tex` (14 pp) | Option B dead; electroweak alternation on the ladder |
| [`signed-dv/`](signed-dv/SUMMARY.md) | `~/signed-dv-custodial-project`, `~/hans` | local only | signed roots and the κ = 3/8 correction | `draft/fused_manuscript.tex` (16 pp, EPJ Plus) | GO from internal critic, unsubmitted; κ an ansatz |
| [`golden/`](golden/SUMMARY.md) | `~/golden2`, `~/golden` | local only | quantized quartic, superstrings and KK | `golden2/quartic_strings_kk.md` (40 pp) | referee: "Mathematical interest: LOW" |
| [`weak/`](weak/SUMMARY.md) | `~/weak` | local only | Casimir-locked seesaw as a particle model | `PAPER.tex` (6 pp) | ansatz; strongest list of failed field-theory routes |

None of the sibling repositories has a remote; this folder is their only
off-machine copy. A complete local snapshot of all of them (git histories,
chats, third-party PDFs, run outputs) was taken on 2026-09-23 into
`~/physres5lineage/`, which stays off GitHub.

## Lineage

```
ChatGPT corpus ──► chats-regge-kk ──► dv2 ──► dvFable
                        │                        ▲ cross-import
kkorchestra ──► kkFable ─────────────────────────┘

physres5 ──► physres6 ──► marathon (synthesis; also draws on golden and signed-dv)
hans ⇄ signed-dv (same prompt, same night; merged manuscript in signed-dv)
weak (2026-05-16) ─► golden, golden2 (2026-05-26, same matrix and scale)
```

The sources stay in place and depend on each other: dvFable symlinks dv2,
kkFable symlinks kkorchestra, and kkorchestra reads PDFs from
`~/physres6/references/` by absolute path.

## Curation rules

- Copied files are byte-identical to their sources and keep the source's
  relative layout; links to files that were left out dangle.
- Left in the sources: raw chat and conversation transcripts, third-party
  PDFs and transcriptions (cited by arXiv id in each `SUMMARY.md`), agent
  PROMPT/OUT logs (their verdicts are summarized), `OPUS_IDEAS.md` files
  (folded into the summaries and `IDEAS.md`), and build files.
- `SUMMARY.md` files use the physres5 tags A1–A3 and the Appendix D targets;
  each lists what was copied and what was left out.
- Curator checks added during curation are marked as such, for example
  `signed-dv/curator_checks.py` (checks C1–C9) and the cross-checks in the
  physres6, marathon and kkorchestra summaries.

## De-duplication (2026-09-23)

- Removed during de-duplication: the pandoc PDF of kkorchestra's status report
  (its Markdown source carries the same text); kkFable's `OPUS_IDEAS.md`; the
  PDF of golden, the companion of golden2; the PDF of weak's 15-page
  `model/paper/main.tex`, the companion of `PAPER.tex`. Companions keep
  their source for the sections the summaries cite.
- Results that several projects found independently are merged in
  `IDEAS.md`; the per-project summaries keep their own statements.
- Duplicates kept on purpose: `physres6/manuscript/macros.tex` and
  `references.bib` (needed for a standalone build), and the small
  per-project scripts that recompute x±(J), which their own check runners
  call. The canonical implementation is `calculations/devries_spectrum.py`
  at the repository root.

Projects that only cite the relation (dualsm, phys3, phys4, koide-formula,
pdghist, physres1) stay outside this folder.
