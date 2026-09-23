# Attempt (1): deriving Q(J) on (squashed) S³ = SU(2)

**Verdict: PARTIAL — a real advance, not a closure.** The natural internal space
is identified, the operator *form* is grounded in published math, two of three
entries are derived, and the third (`−J`) is now precisely located rather than
merely "open."

## What is now derived

1. **The internal space is S³ = SU(2).** Its quadratic Casimir is `j(j+1) = J`
   natively (the DeVries label `s` = SU(2) spin), and its isometry
   `SU(2)×SU(2)` supplies the gauge structure. S² is ruled out: it is symmetric,
   giving a pure Casimir with no room for the negative diagonal.

2. **The operator form matches Henkel–Lauret Lemma 2.1.** The 1-form Laplacian on
   SU(2) on each isotypical block is
   ```
   Δ₁ = −[(C_g − C_k)⊗Id  +  Σ 2 dϱ(Xᵢ)⊗∇_Xᵢ]  +  2 q(R),
   ```
   i.e. a **Casimir diagonal**, a **connection cross-term** (off-diagonal, the
   `√J` mixing — exact 1-form `dφ` with `‖dφ‖²=J‖φ‖²`), and a **curvature term**
   `2q(R)`. The `[[0,√J],[√J,·]]` shape is therefore the genuine shape of the
   SU(2) 1-form Laplacian. `√J` and the zero gauge entry are grounded.

## The obstruction the math forces (and the honest open piece)

The Hodge Laplacian is non-negative: on coexact 1-forms `Δ₁ = Curl²`
(Henkel–Lauret Prop 5.1). But `Q(J)=[[0,√J],[√J,−J]]` has `det = −J < 0`, hence a
**negative eigenvalue**. So `Q(J)` is *not* the Hodge Laplacian. The negative
(tachyonic, order-parameter) entry must come from the curvature/Weitzenböck term
`2q(R)` — equivalently from the Bochner operator `∇*∇ = Δ_Hodge − Ric`, which
*can* be negative on modes of a squashed (Berger) sphere (the standard
squashed-sphere instabilities).

**Open:** that this curvature/Bochner contribution equals exactly `−J·μ²` at each
level (and uniformly at the `s=1/2,1` levels giving `(3/4,2)`) is **not**
derived. The Berger eigenvalues available (`a²+2b²`, `4b⁴/a²`, `4a²`, …) do not
obviously yield `−j(j+1)` per level, and a uniform `−J` likely needs the
Hosotani / Wilson-line (Coleman–Weinberg) potential rather than tree-level
squashing alone.

## Net

Progress: "which 6-manifold + where does `−J` come from" → **S³=SU(2)** (Casimir
native), operator **form grounded** (Lemma 2.1), `√J` and `0` **derived**, and
`−J` **located** in the curvature/Bochner term plus a Wilson-line potential. The
remaining computation is the *value* `−J` at the matched levels — the genuine
open derivation, now sharply posed.
