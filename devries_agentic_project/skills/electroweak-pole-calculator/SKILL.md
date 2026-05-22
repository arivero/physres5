---
name: electroweak-pole-calculator
description: Compute and audit DeVries electroweak pole-mass comparisons and uncertainty-sensitive numerical checks.
---

# Electroweak pole calculator

Use this skill for W/Z mass-ratio calculations and scheme checks.

## Workflow

1. Run `make numbers`.
2. Inspect `data/pdg_ew_inputs.yaml`.
3. Use `calculations/devries_spectrum.py` for the central number.
4. Keep pole, on-shell/Breit-Wigner, MS-bar, and effective weak angles distinct.
5. Update tests when seed values change.

## Output

Create or update `reviews/electroweak_numbers_report.md`.
