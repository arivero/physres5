# Uniqueness of the S³ realization of the de Vries block (2026-09-23)

Companion to `squashed_s3_verdict.md`, result 5. Checked by
`calculations/tests/test_s3_uniqueness.py`.

## Setting

Round S³ of radius R. Two fields, a scalar f ∈ Ω⁰ and a 1-form ω ∈ Ω¹, with
canonical (L²) kinetic terms. The mass functional M is any SO(4)-invariant
local quadratic form on Ω⁰ ⊕ Ω¹, with any number of derivatives, parity-even
or parity-odd.

**Reduction.** Scalar harmonics of level j (ℓ = 2j) span the (j, j)
representation of SU(2)_L × SU(2)_R. Ω¹ contains (j, j) exactly once, as the
exact forms dY; coexact 1-forms lie in representations (a, b) with
|a − b| = 1. By Schur's lemma, on each level M reduces to

    [[P(J), √λ b(J)], [√λ b(J), S(J)]]   on (Y, dY/√λ),

with λ = νJ, ν = 4/R², J = j(j+1), and P, S, b real polynomials (locality).
Coexact forms decouple from f.

## Results

**U1 (the tower).** Suppose the positive mass-squared eigenvalue on every
level j = ½, 1, 3/2, … equals μ²x₊(j(j+1)), with x² + Jx − J = 0. Then
{P, S} = {0, −μ²J} and b² = μ⁴/ν, so on the exact sector

    M = μ² [ ‖f‖² − ‖f − (R/2) δω‖² ]    or its mirror    μ² [ ‖ω‖² − ‖ω − (R/2) df‖² ],

up to ω → −ω. The negative branch x₋ follows; it is not an extra input.

*Proof.* The positive root is X₊ = (T + √D)/2 with T = P + S and
D = (P − S)² + 4νJb². Put q = −μ²J − T. Matching at infinitely many J gives
q·√(J² + 4J) equal to a polynomial at infinitely many points. J(J + 4) is not
the square of a rational function, so q ≡ 0. Hence T = −μ²J and
D = μ⁴(J² + 4J), which reduce to S² + μ²JS + νJb² = μ⁴J. Four steps close it:
- if deg S ≥ 2, the leading term of S² has no partner to cancel it;
- the J⁰ term forces S(0) = 0;
- b² = [μ⁴ − (s₁² + μ²s₁)J]/ν must be the square of a polynomial, which
  forces s₁ ∈ {0, −μ²} and b constant;
- P = −μ²J − S then follows.

**U2 (physical levels only).** Suppose M has at most two derivatives. Require
the photon level j = 0 to be massless, and the W (j = ½) and Z (j = 1) blocks
to carry the full de Vries spectrum (both roots). Then the same two solutions
follow, and nothing else. Without the photon condition a one-parameter family
survives: p₀ = −s₀ = ±(√6/2)√(p₁(μ² + p₁)), s₁ = −μ² − p₁. The massless photon
is what makes the minimal construction unique.

## Meaning

Every coefficient of M is fixed, apart from the overall mass unit μ² and the
choice of which field plays the order-parameter channel. The relation
b² = μ⁴/ν says the gain length is c = R/2, and (R/2)²Δ₀ is the SU(2) Casimir
C₂ on functions. So the gain is written with the su(2) generators in their
standard normalization, the same normalization that makes the labels
j(j+1) with half-integer j.

A coupling g in front of the generators gives x² + Jx − g²J = 0. Requiring
Casimir-texture spectra, with no de Vries target, leaves exactly one free
number, g (dvFable's r, kkorchestra's scale condition). The observed value
corresponds to g = 1.

The construction is therefore unique within its class, and it states the
remaining open question in one line: why the order parameter couples to the
isometry current with unit strength.
