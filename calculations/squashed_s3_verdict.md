# Squashed S³ and the de Vries block: verdict (2026-09-23)

**Question** (physres6 `OPUS_IDEAS.md` #1; `family/physres6/calculations/squashed_s3_attempt.md`).
Can a squashed (Berger) three-sphere, possibly with a Wilson line, produce
Q(J) = μ²[[0, √J], [√J, −J]] at s = ½ and s = 1 with a single μ, with the −J
entry coming from the curvature term 2q(R)?

**Success criterion, fixed before computing.** The full block at both levels,
from a natural operator, with no parameter tuned to the data. Reproducing
cos²θ alone by tuning one geometric parameter counts as a fit.

**Method.** `calculations/squashed_s3.py` builds d, δ and the Hodge Laplacians
Δ_p exactly on SU(2) with an arbitrary left-invariant metric, block by block
in the Peter–Weyl decomposition; the Ricci tensor (Milnor); and the Bochner
Laplacian computed separately from the Levi-Civita connection. Validation:
- round S³: Δ₀ = ℓ(ℓ+2), exact 1-forms ℓ(ℓ+2), coexact (ℓ+1)², with the
  standard multiplicities;
- Berger spheres: Δ₁ agrees with Henkel–Lauret (arXiv:2605.05406) Theorem 4.1
  for k ≤ 5. For k = 0 the code agrees with their eq. (4.9) and with a hand
  computation; the k = 0 line of their eq. (4.1), as extracted from the PDF,
  lists the multiplicities the other way;
- Weitzenböck: Δ₁ = ∇*∇ + Ric holds to 10⁻⁹ on a triaxial metric.

`calculations/tests/test_squashed_s3.py` runs these checks and the results below.

## Results

1. **Where √J and the zero entry come from.** d sends a scalar harmonic Y to
   dY with ‖dY‖² = λ‖Y‖². On the round S³ of radius 2, λ = j(j+1) exactly,
   half-integer j included (ℓ = 2j), with no Weitzenböck or Kostant shift:
   the scalar Laplacian of the bi-invariant metric is the Casimir. The block
   pairs a 0-form with an exact 1-form. The Hodge and Bochner Laplacians are
   block-diagonal in form degree, so the Henkel–Lauret cross term, which mixes
   the frame components of a single 1-form, plays no part in it. This corrects
   the reading in physres6's note.

2. **Curvature cannot supply −J.** On the exact mode dY, an operator
   α∇*∇ + βRic + γ has diagonal entry α(λ − ρ) + βρ + γ, where
   ρ = ⟨dY, Ric dY⟩/‖dY‖² is a weighted average of the principal Ricci
   curvatures, so it lies between the smallest and the largest of them at every
   level. On the round sphere ρ = 2/R² for every mode,
   so −J at two levels forces α < 0, a wrong-sign Laplacian on exact forms,
   together with (β − α)ρ + γ = 0: the curvature must cancel, and the whole −J
   is the negative Laplacian term. On a triaxial metric a pure curvature term
   can be tuned to −J at the W and Z levels (β = −46.9, γ = 20.3 for
   c = (0.8, 1.2, 1.0)); it then gives −5.58 and +3.27 at j = 3/2, where −3.40
   and −4.10 are needed.

3. **Squashing supplies nothing.** Write c_k = 4/s_k². For every left-invariant
   metric the j = ½ modes have λ_W = tr(c)/4 and the three j = 1 modes have
   λ = tr(c) − c_k. The Casimir ratio 3/8 holds for the axis-k mode exactly
   when c_k = tr(c)/3. On Berger spheres this happens only at the round point,
   for every choice of W in j = ½ and Z in j = 1. Triaxial metrics with one c_k
   at the mean keep (3/4, 2) for W and one Z mode and split the other two j = 1
   modes symmetrically.

4. **Wilson lines.** S³ is simply connected and carries no Wilson-line phase.
   On a quotient S³/Γ a flat connection selects which modes survive (the
   Γ-equivariant part of the left multiplicity, or the allowed U(1)_R weights m
   for Γ ⊂ U(1)_R) and leaves every eigenvalue unchanged. S³ and its lens
   quotients have no continuous Hosotani modulus.

5. **The one exact realization.** The relative-gain Hessian
   H = [[0, cδ], [cd, −c²dδ]] on Ω⁰ ⊕ Ω¹ has, on each scalar harmonic,
   eigenvalues solving x² + c²λx − c²λ = 0. On the round sphere with c = R/2
   this is the de Vries equation at every level (checked at j = ½, 1, 3/2).
   H is the Hessian of the gain ½‖f‖² − ½‖f − c δω‖² (kkorchestra's relative
   gain with P† = δ). Coexact 1-forms are zero modes of H; a term +½c′²‖dω‖²
   gives them positive masses and leaves the exact block untouched. The
   family's one free number (dvFable's r = γ/α, kkorchestra's α²x₀ = 1) becomes
   the ratio 2c/R = 1 between the length in the gain functional and the radius.
   Within SO(4)-invariant local functionals this realization is unique up to
   the mirror exchange of the two channels (`s3_uniqueness.md`).

6. **Squashing as custodial breaking (an illustration, a fit).** With W at
   (j, m) = (½, ±½) and Z at (1, 0), Berger squashing moves only the W level:
   L_W = ½ + 1/(4t²), L_Z = 2. sin²θ runs from 0.2055 at t = 0.9 to 0.2370 at
   t = 1.1, and t = 1.0013 reproduces the PDG-Live 2026 pole value 0.2233064.
   One parameter fitted to one number carries no evidential weight.

## Verdict

The squashed-S³ route as posed in physres6 is closed: curvature and Wilson
lines cannot produce the −J entry, and squashing only moves the round-sphere
labels away from (3/4, 2). What survives is a precise statement for the
manuscript: on the round S³ the de Vries block is the Hessian of the relative
gain ½‖f‖² − ½‖f − (R/2)δω‖², with the Casimir labels supplied by scalar
harmonics and no shift. A derivation must now explain two things, the
wrong-sign exact-form term and the scale c = R/2.

## Open physics in this realization

- **Multiplicities.** Scalar harmonics come in (j, j) of SU(2)_L × SU(2)_R. With
  electric charge Q = 2m for the Hopf U(1)_R, the assignment γ ↔ (0, 0),
  W± ↔ (½, ±½), Z ↔ (1, 0) has the right charges, but the W level is an SU(2)_L
  doublet, the Z level a triplet, and the charge-±2 modes (1, ±1) are
  degenerate with the Z on the round sphere. A projection has to remove the
  extra copies; this is the tower problem dv2 and marathon describe.
- **Kinetic terms.** The eigenvalues are masses only if f and ω carry equal,
  canonical four-dimensional kinetic terms (condition B3 in `family/IDEAS.md`).
