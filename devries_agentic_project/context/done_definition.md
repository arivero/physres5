# Completion criteria for the 50-page manuscript

A complete manuscript satisfies these checks.

## Structural checks

- 35–50 manuscript pages in REVTeX preprint format.
- Abstract states the observable, the construction, and the open dynamical question.
- Introduction distinguishes derivation, coincidence, conjecture, and program.
- Main text contains no hidden dependence on unpublished conversation context.
- Appendices contain all algebra and numerical checks needed to reproduce the central number.

## Analytical checks

- The quadratic secular equation is derived from stated assumptions.
- The positive-root ratio is computed symbolically and numerically.
- Pole-mass scheme is stated with conversion formulas.
- W/Z assignment is either derived or isolated as the central conjecture.
- Negative branch is analyzed without overclaiming.
- The string/brane/KK/G2 section contains concrete mechanisms or constraints.
- Flavor/generation claims respect the SO(32)-flavor caveat.

## Validation checks

- `make test` passes.
- `make manuscript` passes.
- `calculations/devries_spectrum.py` reproduces the central number.
- Bibliography keys used in LaTeX are present in `manuscript/references.bib`.
- `OPEN_ISSUES.md` reflects remaining gaps.
