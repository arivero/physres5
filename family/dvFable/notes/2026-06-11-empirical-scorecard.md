# Empirical scorecard freeze (G1.0)

**Verdict: SOLVED (freeze recorded). Inputs frozen until a terminal state;
no mid-loop PDG chasing.**
Script: `calc/scorecard_2026.py` (all checks pass). Core identities and exact
values: `calc/devries_core.py`.

## Frozen target

De Vries value: `sin²θ_dV = 0.223101322300866…`, `(m_W/m_Z)_dV = 0.881418560…`.

On-shell experimental targets and pulls (datum recorded in
`loop-history/milestone7-phenomenology-execution-2026-05-25.md`; widths
Γ_Z = 2.4955, Γ_W = 2.085 for the convention shift):

| datum | convention | sin²θ_on-shell | pull of dV |
|---|---|---|---|
| PDG-live 2026 masses (80.3625(77), 91.1880(20)) | Breit–Wigner | 0.223339(153) | **+1.56σ** |
| same | pole (m − Γ²/2m) | 0.223280(153) | +1.17σ |
| CMS 2026 W (80.3602(99)) + PDG Z | Breit–Wigner | 0.223383(194) | +1.45σ |
| PDG direct-ratio entry (0.88136(15)) | as published | 0.223205(264) | +0.39σ |

**Primary datum (frozen): PDG-live 2026 separate masses, Breit–Wigner
convention — sin²_target = 0.223339(153), pull +1.56σ.** Rationale: best
precision and provenance; BW is the PDG-quoted convention. The pole-convention
value (+1.17σ) and the direct-ratio entry (+0.39σ) are recorded as the
robustness band: **the de Vries pull today is 0.4–1.6σ, not the historical
0.42σ** (that number was scored against the superseded 0.22321(26) datum and
is no longer quotable).

## What there is to explain

Relative deviation vs the primary datum: 1.1·10⁻³ → the relation matches
**~3 significant digits** of the on-shell weak angle (not 4). Any T1 claim
inherits this calibration; the look-elsewhere accounting (T3) prices a
±0.0002-wide window around 0.2232.

Pre-commitment (from `GOALS.md`): if a future frozen datum sits ≥3σ from the
tree-level relation, a T1 claim must carry a stated scheme story, or the
framing converts to T3.

## Re-score of the inherited uniqueness claim

"(1/2, 1) is the unique half-integer pair within 3σ (j ≤ 4)" — re-scored
against the frozen primary datum: **holds** (next-nearest pair is >3σ away by
a wide margin; see script output), but the pair's own pull is now 1.56σ (BW) /
1.17σ (pole), and the claim remains a bounded enumeration over one functional
form — it enters T3 accounting as one cell of the hypothesis-class table, not
as evidence of forcing.

## Killed at admission (recorded here because the kill is numerical)

Ledger candidate (b′), Weinberg-compositeness `Z = 0` for the single-pole
rank-one resolvent: the dressed pole residue obeys `Z⁻¹ = 1 + C/(X₊+C)² > 1`
strictly (`Z_W = 0.699`, `Z_Z = 0.789`), and `Z → 0` would need `X₊+C → 0`,
impossible for `C > 0`. `calc/devries_core.py` §7. A continuum/multi-pole
variant would be a different spectral shape — and then the rational de Vries
form is no longer the pole equation — so any revival needs fresh admission.
