# The (c₁, c₂)-quadratic family: where X² + c₁X − c₂ = 0 occurs, and what is de Vries-specific

**Verdict line: REFERENCE / T3-ACCOUNTING (user-prompted, 2026-06-11).
The form is cheap; the de Vries content is one condition — the diagonal
c₁ = c₂ — which is the same dimensionless closure retired in iteration 2.**
Script: `calc/quadratic_shape_family.py` (all checks pass).

Prompted by the user (2026-06-11): "X² + CX − C = 0 is a very common
equation … with arbitrary C₁ C₂ … I remember it in topology equations of
string theory or perhaps KK." The recollection is correct, and both
likely anchors are in this project's own record:

1. **KK spectroscopy, literally named c₁, c₂** (`PRIOR-AGENT.md:49`): the
   universal KK/Freund–Rubin vector mass matrix
   `[[L + c₁m², dm√L], [dm√L, L + c₂m²]]`, L ≥ 0 a Hodge eigenvalue —
   its characteristic polynomial is a quadratic of this family with
   geometry-supplied coefficients (and the recorded no-go: its locked
   entries cannot reach the de Vries point for L ≥ 0).
2. **Poincaré-Casimir form, literally named C₁, C₂** (corpus,
   `14-string-theory-and-orbits…md:343`): `M⁴ − M²C₂ + C₁C₂ = 0` with
   C₁ = m², C₂ = −m²s(s+1). Normalizing (X = M²/C₁, K = C₂/C₁) this is
   X² − KX + K = 0 — **the diagonal is automatic** in this form because
   the constant term is the product C₁C₂. The forcing question is only
   repackaged: why is the constant term the product (and not an
   independent C₃)? That is the orbit derivation's job, not an identity.

Standard zoo, same family (verified normalizations in the script):

- Sphere-harmonic inversion: λ = l(l + d − 1) on S^d ⇔
  l² + (d−1)l − λ = 0 (c₁ = d−1, c₂ = λ).
- AdS_{d+1} mass-dimension relation: Δ(Δ − d) = m²L² ⇔
  Δ² − dΔ − m²L² = 0 (c₁ = −d, c₂ = m²L²; spin-s variants shift the
  coefficients). Liouville/Kac-type weight equations: same family.
- The iterations-1/2 two-channel family itself:
  X² + (δ + λC)X − γ²C = 0 — arbitrary nonnegative (c₁, c₂).

## What this means for the program (both directions)

- **For T3 (coincidence accounting):** the functional FORM is ubiquitous —
  any resolvent/eigenvalue-inversion mechanism produces some member of
  the (c₁, c₂) family. The de Vries-specific content is exactly ONE
  condition: the diagonal c₁ = c₂ (= C, with the zero-mode map and the
  root choice). The look-elsewhere class for "a natural mechanism
  produces a quadratic of this family" is large; the prior probability
  of the diagonal within the family is the honest object to price. This
  goes into the pre-registered T3 hypothesis-class enumeration as its
  own axis: form (cheap) × diagonal (the actual claim).
- **For T1 (forcing):** the AdS relation shows geometry CAN lock both
  coefficients of the family (d by dimension, m²L² by the field's mass) —
  what is never automatic is the diagonal. This restates iterations 1–2:
  the diagonal IS the retired closure g²/α = 1 ⇔ Σ_j(0) = μ²
  channel-universally. Iteration 3 (candidate (h)) asks whether the
  single GHU trace pins it.
- **Possible future candidate (NOT admitted yet, admission check
  pending):** Lie-algebra characteristic identities (Bracken–Green/
  King-class) produce polynomials in operator matrices whose
  coefficients are Casimir polynomials — check whether any standard
  characteristic identity has the C₁C₂ product-constant-term structure
  forced (which would make the corpus Poincaré form a theorem of some
  operator identity rather than an ansatz). One literature pass before
  admission; do not open without it.
