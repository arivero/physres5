---
name: analytic-gap-solver
description: Attack one of the open analytical calculations in the DeVries String project and produce a derivation or precise obstruction.
---

# Analytical gap solver

Use this skill for open issues O1-O7.

## Workflow

1. Identify the open issue in `OPEN_ISSUES.md`.
2. Write assumptions explicitly.
3. Derive symbolically as far as possible.
4. If the derivation fails, state the missing assumption.
5. Update `calculations/*.md`, the relevant manuscript section, and `OPEN_ISSUES.md`.
6. Run tests and compile.

## Output

Create `reviews/analytic_gap_<issue>.md`.
