# Attempt to derive v = √2·M₋(J=2)

**Goal.** Decide whether the identification `v = √2·M₋(J=2)` — on which the α
prediction rests — is derivable, partial, or assumption-only.

**Verdict: PARTIAL.** Not derived from first principles, but it reduces exactly
to a cleaner primitive that removes the √2 and the negative branch from the α
chain.

## Algebra

Root invariant of `x² + Jx − J = 0`:  `x₊(J)·x₋(J) = −J`, so
```
|x₋(2)| = 2 / x₊(2).
```
With `M_V = μ√x₊` and `M₋(J) = μ√|x₋(J)|`, the assumption `v = √2·M₋(2)` gives
`v² = 2μ²|x₋(2)| = 4μ²/x₊(2)`, i.e.
```
v = 2μ / √x₊(2).
```
Then `g = 2M_W/v = 2μ√x₊(3/4) / (2μ/√x₊(2))`, and μ cancels:

```
  g²  = x₊(3/4) · x₊(2)              # SU(2) coupling² = product of positive roots
  g'² = x₊(2) · (x₊(2) − x₊(3/4))
  e²  = x₊(3/4) · (x₊(2) − x₊(3/4))  # = g²g'²/(g²+g'²), standard 1/e²=1/g²+1/g'²
  g²+g'² = x₊(2)²
  1/α = 4π / e² = 135.29
```
All verified numerically (see `devries_spectrum.py`); the reduced primitive
`g² = x₊(3/4)·x₊(2)` and `v = √2·M₋(2)` are the *same* statement via the
invariant.

## What this means

The electroweak couplings rest on **two** assignments, both of the form
"positive-branch eigenvalues fix couplings":

1. **Angle (positive branch):** `M_W²/M_Z² = x₊(3/4)/x₊(2)` → `sin²θ = 0.2231`.
2. **Scale (this note):** `g² = x₊(3/4)·x₊(2)`  ⟺  `v = √2·M₋(2)`  ⟺  `μ² = v·M_Z/2`.

Given both, the whole coupling sector is fixed, and
```
1/α = 4π / [ x₊(3/4)·(x₊(2) − x₊(3/4)) ] = 135.29.
```

## Honest status

- The reduction is exact and is a genuine simplification: the `√2`, the negative
  branch, and the top-Yukawa detour are not needed to *state* the assumption —
  `g² = x₊(3/4)·x₊(2)` suffices.
- It is still an **assumption**: a cross-slot relation (one eigenvalue from each
  J block) with no first-principles derivation yet.
- Its physical reading is `v = √2·M₋(2)`, i.e. the J=2 negative branch is the
  top-Yukawa scale with `y_t ≈ 1` (`m_t = y_t v/√2`). This reading is what ties
  the assumption to the order-parameter / top sector.

## Open

Derive `g² = x₊(3/4)·x₊(2)` (or equivalently `μ² = v·M_Z/2`) from a dynamical
or geometric principle. Until then it is the paper's second stated assumption.
