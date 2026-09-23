# PRL companion to `claudeFinal.tex`

Submission-ready draft of a Physical Review Letters companion to the long
paper in `../devries-regge-kk-research-project/claudeFinal.tex`.

## Files

- `main.tex` — the Letter. Compiles to 4 pages, the PRL limit.
- `supplemental.tex` — Supplemental Material. Compiles to 6 pages.
- `main.pdf`, `supplemental.pdf` — built artifacts (`pdflatex` ×2 each).

## What is claimed

The on-shell weak mixing angle and the W/Z mass ratio are the spectrum
of a 2×2 matrix with no continuous parameter, evaluated at the SU(2)
Casimirs of j=1/2 and j=1. The matrix is forced by four axioms
(Theorem 1). The half-integer label is the Peter–Weyl fingerprint of an
internal SU(2). The off-diagonal √J is the algebraic Casimir delivered
by gauge–Higgs unification on CP¹. The negative diagonal −J is the
single-portal Schur completion of the same operator (Proposition 1).
The Weitzenböck-shifted alternative gives 0.267 rather than 0.2231, so
the bare-Casimir normalization is rigid. A neutral spin-zero state
near 96.5 GeV is a direct prediction of the same operator.

## What is *not* claimed

- The integer labels (12,14,91,1) play **no role** in any derivation.
  The Bailin–Love four-tuple family is dense around the target
  (138/12/2 hits within 10⁻³/10⁻⁴/10⁻⁵ in a modest scan), so any
  integer match is overdetermined. Sec. VIII of the supplemental
  records the scan as an explicit warning.
- The absolute α and the absolute electroweak scale μ are not
  predicted. μ is fixed to 106.6 GeV by anchoring to M_Z.
- The Hosotani-potential coefficient β is not computed; the conditional
  derivation gives c = β/α² = 1 from the single-portal hypothesis, and
  the absolute magnitude is the open computation flagged in Sec. XI of
  the supplemental.

## Differences from `claudeFinal.tex`

- **Tighter scope.** PRL is operator-first and parameter-free. The full
  Hodge–de Rham curl construction, the dimensional-ladder essay, and
  the M^{pqr} integer-fit critique are condensed to a paragraph each
  and pushed to the supplemental where appropriate.
- **The codex track abandoned.** The labels (12,14,91,1), the period
  rule r = Q(P+Q) = 91, the ρ\* = 9.463 vacuum target, and the
  α_geom⁻¹ = 135.288 derivation route are removed from the load-bearing
  argument. The IIA realization on M₄ × CP² × CP¹ is kept as the
  geometric host for the operator (Sec. V of the supplemental), with
  the Q-boundary carrier, Z₆→Z₃ descent, and the finite Higgs sheet of
  Connes–Lott. These are realization data, not derivation steps.
- **Predictions promoted.** sin²θ_W = 0.22310 (with custodial ρ = 1),
  the 96.5 GeV neutral scalar, and the negative-branch identification
  of v_EW, m_H, m_t are stated as the falsifiable content. The
  Weitzenböck dichotomy 0.223 vs 0.267 is the explicit rigidity test.

## Style rules (from `AGENT.md`)

- Physics prose only in typeset text. Status, methodology, and
  open-gate commentary live in `%` comments.
- No copulative adversatives in typeset text ("X, not Y" forms).
- The de Vries number 0.2231 is an output, never an input.
- D = 10 is the physical rung; D = 11 is the controlled
  linearization limit; D = 9 is the vector-like residue.
- No assistant-voice section headers.

## Build

```
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode supplemental.tex
pdflatex -interaction=nonstopmode supplemental.tex
```

Both compile clean (zero undefined references, zero citation warnings).
