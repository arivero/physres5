# Branch duality: x → −J/x

The two DeVries roots are exchanged by the involution
```
x  ↦  −J/x
```
because `x₊ x₋ = −J`, so `x₋ = −J/x₊`. The quadratic `f(x)=x²+Jx−J` transforms as
```
f(−J/x) = (−J/x²) · f(x),
```
so the root set is invariant and the map swaps `x₊ ↔ x₋`. Verified against the
known roots: `J=2`, `−2/0.73205 = −2.73205 = x₋(2)`; `J=3/4`,
`−0.75/0.56873 = −1.31873 = x₋(3/4)`.

## In masses

With `M² = μ²x`,
```
M²  ↦  −μ⁴J / M²,        i.e.   M²₊ ↔ M²₋ = −μ⁴J / M²₊
```
consistent with `M²₊ M²₋ = −μ⁴J`. This is an inversion through the scale
`(μ⁴J)^{1/2}`: it exchanges the light gauge branch (`M²₊ < μ²`) with the
heavy/tachyonic order-parameter branch. There is no real fixed point
(`M⁴ = −μ⁴J`), so the duality genuinely swaps the two sectors rather than fixing
one.

Tied to the reciprocal invariant `1/M²₊ + 1/M²₋ = 1/μ²` (see
`reciprocal_invariant.md`): the duality `M² → −μ⁴J/M²` and the constant
inverse-trace are the two faces of `tr = det = −J`.

## Reading (connects to the "duality" raised in discussion)

The construction carries a built-in inversion duality between its gauge and
order-parameter branches — a UV/IR-type exchange of a light and a heavy sector.
This is the candidate object for the duality discussed in the PF threads, and it
sits naturally in the dual-resonance (1968–71) heritage, where s–t channel
duality and Regge structure are primary and the string scale is hadronic
(`α' ∼ (1 GeV)^{-2}`). Under that reading the IR (~1 GeV) value of α is the
coupling read at the string's original hadronic scale, not at the Planck or
electroweak scale.

## Open
- Identify `x → −J/x` with a specific known duality (s–t, open–closed, or
  strong–weak).
- Connect the ~1 GeV scale of α to the hadronic string slope `α'` quantitatively
  (the Regge tower spacing `1/α'` vs the intercept scale `μ`).
- A dual-resonance / Veneziano-era reference is needed; the current bibliography
  is modern KK/string only.

## Brane reading (D0 / space-filling), corrected 2026-05-22

The rotating-brane law uses the SPIN as axis, `M ~ spin^{p/(p+1)}`. The DeVries
label `s` is the spin; `J=s(s+1)` is the Casimir. Verified asymptotics (vs `s`):
`M_+ → μ` (bounded) and `M_- ∝ s` (since `|x_-| → J = s(s+1)`, so
`M_-^2 ∝ s(s+1)`):
- positive branch = `p=0` point / D0 (`M ~ const`);
- negative branch = `p→∞` space-filling brane (`M ~ spin`).

A fundamental string would give `M ~ spin^{1/2}` (`M_-/√s → const`); here
`M_-/√s` grows, so it is NOT a string. (An earlier version of this note read
`M_-^2 ∝ J` as "string/D1" — that used the Casimir `J` as the axis instead of the
spin `s`, the error the user caught. Against the spin, the negative branch is
space-filling, as the original prTalks plot said.) The inversion `x → −J/x`
exchanges D0 (point, all-Dirichlet) and the space-filling brane (all-Neumann) —
the full-T-duality pair. The conventional *linear* Regge tower (`M²∝spin`) is
distinct; it comes from the separate oscillator `n`, not from the sector label.
