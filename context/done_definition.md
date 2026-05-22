# Completion criteria for the long PRD manuscript

A complete manuscript satisfies these checks.

## Structural checks

- At least 60 manuscript pages in REVTeX PRD preprint format for the long target.
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
- The string/brane/KK/G2 sections show strong command of string theory and Kaluza-Klein mechanisms, including compactification spectra, boundary data, endpoint sectors, and the role of singularities.
- Flavor/generation claims respect the SO(32)-flavor caveat.

## Validation checks

- `make test` passes.
- `make manuscript` passes.
- `calculations/devries_spectrum.py` reproduces the central number.
- Bibliography keys used in LaTeX are present in `manuscript/references.bib`.
- `OPEN_ISSUES.md` reflects remaining gaps.
