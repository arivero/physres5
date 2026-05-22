# T03 — Pole-mass scheme and electroweak inputs

## Goal

Make the numerical comparison scheme-safe.

## Instructions

1. Read `calculations/electroweak_pole_scheme.md`.
2. Expand `manuscript/sections/03_pole_observable.tex`.
3. Define the pole observable and distinguish it from MS-bar and effective weak angles.
4. Add a table of seed values with explicit `source-audit pending` status if current source verification is incomplete.
5. Add formulas for pole/Breit-Wigner conversion if source-supported.
6. Update `calculations/devries_spectrum.py` only if the source audit changes seed values.
7. Run `make manuscript` and `make test`.

## Done when

The section states the exact mass convention and all numerical claims are sourced or labeled as project seeds.
