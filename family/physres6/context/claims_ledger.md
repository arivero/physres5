# Claims ledger — physres6

Every quantitative sentence in `main.tex` maps to a row here. Tags:
**D** derived (exact algebra) · **A** assigned (stated hypothesis) ·
**C** coincidence (consequence agreeing with data at stated %) · **R** cited.

| # | claim | value | tag | source / note |
|---|---|---|---|---|
| 1 | branch eigenvalues `x±(J)=(−J±√(J²+4J))/2` | — | D | algebra |
| 2 | `x₊(3/4)`, `x₊(2)` | 0.568729, 0.732051 | D | `make numbers` |
| 3 | `sin²θ = 1 − x₊(3/4)/x₊(2)` | 0.223101 | D | algebra |
| 4 | on-shell `1 − M_W²/M_Z²` | 0.22320 | R | PDG masses (#12,13) |
| 5 | #3 vs #4 agreement | 0.04% | C | — |
| 6 | distinct angle definitions (eff `0.23155`, MSbar `0.23129`) | — | R | MartinRobertson2025; PDG |
| 7 | invariant `x₊(J)x₋(J) = −J`, so `|x₋(J)|=J/x₊(J)` | — | D | algebra |
| 8 | assignment A1: positive branch → `(J_W,J_Z)=(3/4,2)` for `(s=1/2,1)` | — | A | not derived; physres5 O1 |
| 9 | assignment A2: `v = √2·M₋(2)` ⟺ `g² = x₊(3/4)·x₊(2)` | — | A | not derived; reduced primitive; physres5 O17 |
| 10 | reading of A2: `m_t = y_t v/√2`, `y_t ≈ 1` | — | A/R | top-Yukawa; PDG m_t |
| 11 | `g² = x₊(3/4)·x₊(2)` (μ cancels) | 0.416339 | D | given A2 |
| 12 | `1/α = 4π/[x₊(3/4)(x₊(2)−x₊(3/4))]` | 135.29 | D | given A2 |
| 13 | `1/α(0)` | 137.035999 | R | PDG 2025 |
| 14 | `1/α(M_Z)` | 127.955 | R | PDG 2025 |
| 15 | #12 lies in the IR, far from #14; ≈ running α near ~1 GeV | — | C | running α; hadronic-VP caveat |
| 16 | `μ` from `M_Z` | 106.578 GeV | D | given M_Z |
| 17 | `M_W` (construction) | 80.375 | D | =μ√x₊(3/4) |
| 18 | `M₋(3/4)` vs `M_h=125.20` | 122.39 (−2.2%) | C | PDG M_h |
| 19 | `M₋(2)` vs `m_t=172.57` | 176.16 (+2.1%) | C | PDG m_t |
| 20 | `v=√2 M₋(2)` vs `246.22` | 249.13 (+1.2%) | C | PDG v |
| 21 | forward: `M₊(s=3/2)=μ√x₊(15/4)` | 96.54 GeV | D | given μ |
| 22 | #21 vs ~95.4 GeV diphoton excess | ~1% | C | CMS/ATLAS Run 2 |
| 23 | identity of #21 open (gauge slots exhausted; chiral 4/3 candidate) | — | A | physres5 O18 |
| 24 | golden lineage: `x²+Ax−A`, golden at `A=1`, DeVries `A=s(s+1)` | — | D | algebra |
| 25 | Regge completion `M²_{n,j,±}=μ²x_{j,±}+n/α'`, `J=n+j` | — | A | dynamical hook; physres5 O4 |

## Reference values used (PDG 2025 unless noted)
M_Z = 91.1880(20); M_W = 80.3692(133); M_h = 125.20(11); m_t = 172.57(29);
v = 246.22 (from G_F); 1/α(0) = 137.035999177(21); 1/α(M_Z) = 127.955(10).

## Honesty summary
- Genuinely predicted (parameter-free): #3 (sin²θ), #12 (1/α), #21 (96.5 GeV).
- Rests on two assignments: #8 (A1) and #9 (A2). Neither derived.
- Few-percent consequences: #18–#20.
- Open / not in this Letter: dynamical origin (#25), scale-placement of α (#15),
  identity of the s=3/2 state (#23). These are the physres5 long-version program.
