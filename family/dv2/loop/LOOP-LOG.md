# dv2 loop log

Run started 2026-05-25 ~12:43 CEST. STOP target: **14:00 CEST**.
Solo continuation after Claude token stop: **until 14:30 CEST**.
Protocol: AGENT.md "The loop" — one sub-question/iteration, dispatch to BOTH
codex (GPT-5.5 xhigh) and opus, cross-check, integrate, next question.
Governing rule: DEFAULT TO CONSTRUCTION (no-go only if Galois/Arrow-class).

## Iteration 1 — dispatched 12:43
Sub-question: Construct a unitary, positive-definite dynamical mechanism (gap /
Schwinger-Dyson / composite-dual self-energy) whose self-consistent pole obeys
X = C/(X+C) with C = j(j+1) the internal SU(2) Casimir (j_W=1/2, j_Z=1).
Derive the fixed point from a defined Lagrangian/self-energy; show where C enters.

- opus (a91645e9bfdfca5ec): DONE → loop/OUT-opus-iter1.md
  Constructed rainbow/NJL gap eq  Σ = Cμ⁴/(Σ+Cμ²) ⇒ X = C/(X+C). Casimir does
  double duty (vertex numerator C; internal-line Casimir mass denominator Cμ²).
  Reproduces sin²θ_W=0.223101 EXACTLY given residue/coefficient = 1. Missing
  ingredient pinned to one residue-normalization constant κ (= old "a=1" gate).
- codex (bjx7y8sja, bypass mode): DONE → loop/OUT-codex-iter1.txt. Gave TWO
  realizations: (1) rank-one Feshbach/Friedrichs two-channel H_eff=μ⁴C/(E−μ²C),
  pole at E=−M² ⇒ X=C/(X+C), positive residue Z⁻¹>0, KL density
  ρ=μ⁴Cδ(ν−μ²C)≥0; (2) large-N Stueckelberg saddle of V=½X²−C log(X+C),
  dV/dX=0 ⇒ X=C/(X+C). Same assignment (γ:0,W:½,Z:1) via ½⊗½=0⊕1 + Z₂-center.
- VERDICT (iter1): CROSS-CONFIRMED CONSTRUCTION. Two models, three realizations
  (NJL bubble / Feshbach two-channel / large-N saddle) → X=C/(X+C) with no approximation,
  unitary & positive (positive residue, KL ρ≥0, ghost-free Stueckelberg), C=j(j+1)
  as Casimir numerator + resolvent shift; de Vries number is OUTPUT. opus's open
  κ knob RESOLVED by codex variational form: κ=1 fixed by canonical ½X² norm.
  Verified numerically: roots, saddle, and that (½,1) is the UNIQUE half-integer
  pair (j≤4) within 3σ. Integrated into paper §"A one-Casimir resolvent gap".
- REMAINING OPEN (both converge): local anomaly-safe 4D UV completion forcing
  (a) canonical V_j + single-pole spectral density, (b) the Z₂-center selection
  rule W:½,Z:1,γ:0. → iteration 2.

## Iteration 2 — dispatched 12:55
Sub-question: construct the local 4D unitary dynamics whose center/selection rule
FORCES W∈j=½, Z∈j=1, γ∈j=0 (so C_W=¾, C_Z=2 are outputs), with the canonically
normalized one-Casimir resolvent action / single-pole spectral density; or show
the assignment is unforced (a fit). Build on the iter-1 cross-confirmed result.
- codex: loop/OUT-codex-iter2.txt (bypass mode)
- opus:  background agent
- verdict: PENDING / not usable yet. The codex transcript mostly re-ran the
  iteration-1 Feshbach construction and did not solve the selection-rule prompt;
  opus is unavailable while Claude is out of tokens.

## Solo audit — 13:01 CEST
Goal: rescue the loop state and narrow iteration 2 to a checkable gate.

- Source-backed selection fact: `SU(2)_k` WZW integrable modules have
  `j=0,1/2,...,k/2`; at `k=2` this gives `{0,1/2,1}`. This can remove
  higher `j` channels inside that current sector.
- Normalization split: direct Sugawara/`L0` gives `Delta_j=J/(k+2)=J/4`, so a
  mass operator built directly from `L0` has the wrong coefficient for de Vries.
  Exact de Vries needs the target-space current zero modes / holonomy metric.
- Zero-mode normalization: setting `m=n=0` in the affine current algebra removes
  the central term, so `J_0^a` act as ordinary `SU(2)` generators and
  `sum_a J_0^a J_0^a = j(j+1)` on `V_j`. Thus the unit Casimir coefficient is
  algebraically available if the physical mass operator couples to zero modes.
- Boundary placement route: Payen's Chan-Paton boundary action supplies a
  source-backed way to quantize endpoint variables into finite `SU(2)` irreps;
  Wilson-loop variations insert `T_a` and `T_aT_b`, giving the tensor structure
  `A_j^\dagger A_j=J`.
- Remaining gate: derive from a local 4D/D10 parent that the massive-vector
  self-energy uses this zero-mode/boundary operator, with the single-pole
  spectral density and the local coefficient/sign. Without that action
  placement, `SU(2)_2` is only a finite selector, not a full derivation.

## Iteration 3 — next sharp question
Construct the boundary/current parent action. Starting from an `SU(2)_2`
current sector plus Payen-style endpoint variables in `V_j`, derive the local
quadratic interface operator or Feshbach closed channel whose elimination gives
`rho_j(nu)=mu^4 J delta(nu-mu^2 J)` and coefficient `kappa_cur=1`. Show whether
the photon is the `j=0` singlet, `W` the fundamental endpoint `j=1/2`, and `Z`
the lowest neutral bilinear/adjoint `j=1` as consequences of the same boundary
rule, not as labels chosen after the fact.
- solo codex: loop/OUT-solo-iter3.md
- VERDICT (solo, not cross-confirmed): boundary-channel construction closes the
  algebraic selector/normalization gate conditionally on action placement.
  `SU(2)_2` removes higher `j`; current zero modes give
  `A_j^\dagger A_j=J` with no `1/(k+2)` factor; a positive two-channel
  Feshbach kernel gives `rho_j(nu)=mu^4 J delta(nu-mu^2 J)`. Direct Sugawara
  `L0` remains a failed control (`sin^2=0.301410`, `tan^2=0.431454`).
- REMAINING OPEN: derive the concrete 4D/D10 boundary/interface action whose
  physical vector two-point function uses that zero-mode kernel, including the
  local sign/coefficient and the electroweak charge embedding of endpoint
  `j=1/2` versus neutral bilinear `j=1`.

## Solo D10 brane/symmetry note — 13:11 CEST
User objective: show D10 KK as a symmetry of the superstring action and compare
the D0 brane with the space-filling brane in the same KK space.

- Added `prior-work/d10-superstring-kk-brane-symmetry.md`.
- Result: D10 KK is formulated as target-space symmetry data of the Type IIA
  string background on `M4 x CP2 x CP1`: internal vector fields preserving
  `G,B,Phi` and RR data give worldsheet Noether symmetries; localized
  parameters become KK gauge connections via
  `dy^m -> dy^m + K_a^m A_mu^a dx^mu`.
- D0 comparison: D0 couples electrically to `C1`, and in the M-circle reduction
  its charge is `P_psi`, the KK momentum along `S1_Z`. It tests the RR period
  and `F2=dC1` class but does not supply the weak current selector.
- Space-filling comparison: a literal all-Neumann D9 is the ten-dimensional
  control object but belongs to Type IIB/type-I parity. The active Type IIA
  object is D8-like, `W9=M4 x CP2 x S1_Q`, codimension one in `K6`, source for
  a Romans-mass/domain-wall channel, and a candidate host for Chan-Paton/current
  zero modes.
- Remaining gate: derive the D8-like boundary action and source/tadpole
  coefficients from the same D10 parent, then connect it to the Feshbach/current
  kernel in `loop/OUT-solo-iter3.md`.

## LaTeX article build — 13:17 CEST
User objective extended: build a LaTeX article on the D10 KK symmetry / D0 /
space-filling brane comparison.

- Added `paper/d10-kk-branes.tex`.
- Built `paper/d10-kk-branes.pdf` (5 pages).
- Article structure:
  1. D10 background `M4 x K6`, `K6=CP2 x CP1`, with M-circle/RR one-form data.
  2. KK symmetry as worldsheet/target symmetry of the superstring action:
     `delta y^m=epsilon^a K_a^m`, background invariance, and KK connection
     `dy^m -> dy^m+K_a^m A_mu^a dx^mu`.
  3. D0 as the electric `C1` probe / M-circle momentum.
  4. Space-filling side: all-Neumann D9 as control, active Type IIA object as
     D8-like `W9=M4 x CP2 x S1_Q`.
  5. WZ/spin-c/Romans source skeleton and comparison table.
- Verification: `pdflatex` run twice; no undefined references, no LaTeX
  warnings, no overfull boxes.

## LaTeX article rebuild with IR/UV probes — 13:21 CEST
User objective extended: add that IR strings see color times electromagnetism,
while UV probes resolve unbroken D11 as a Witten growing-dimension limit.

- Rebuilt `paper/d10-kk-branes.tex` and `paper/d10-kk-branes.pdf` (6 pages).
- Added section `IR and UV probe regimes`:
  - `E << Lambda_9->10`: effective carrier `M4 x CP2 x S1_Q`, visible
    `G_IR=(SU(3)c x U(1)Q)/Z3`.
  - `Lambda_9->10 << E << Lambda_10->11`: active Type IIA D10
    string/current interface on `M4 x CP2 x CP1`.
  - `E >> Lambda_10->11`: UV parent `M4 x M^{12,14,91}` with unbroken
    `SU(3)c x SU(2)L x U(1)Y`.
- Added Witten interpretation: `R11=g_s ell_s`; as `g_s` grows, `R11` grows,
  the D0 tower becomes KK momentum, and the ten-dimensional description is
  replaced by an eleven-dimensional one.
- Verification: `pdflatex` run twice; no warnings/errors, no undefined refs,
  no overfull boxes, and no forbidden-word hits in the article source.

## LaTeX article proof/example upgrade — 13:29 CEST
User objective extended: every section should contain graduate-level examples,
and the arguments should be proved in the main text or an appendix.

- Rebuilt `paper/d10-kk-branes.tex` and `paper/d10-kk-branes.pdf` (10 pages).
- Added theorem/example structure:
  - 8 main sections each have a proposition plus a worked example.
  - Appendix `Proofs and checks` proves all 8 propositions.
  - Appendix also has its own example explaining the proof map.
- Main examples now cover:
  - product coset and RR periods;
  - neutral `Q` section on `CP1`;
  - circle KK gauge-field model;
  - D0 Aharonov-Bohm phase;
  - D8-like local boundary coordinates;
  - spin-c half-integral flux on a projective line;
  - three observables separating D0/D8/D9;
  - first three `H^0(CP1,O(2j))` zero-mode spaces and Casimirs.
- Verification: `pdflatex` run twice; no warnings/errors, no undefined refs,
  no underfull/overfull boxes, no forbidden-word hits, and no `\over` hits.

## D10 boundary action and moduli space — 13:43 CEST
User objective: construct the actual D10 boundary action on
`W9=M4 x CP2 x S1_Q`, carry the `H^0(CP1,O(2j))` endpoint spaces, preserve
the `Q` photon boundary, produce the Chan-Paton/Wilson insertions used in the
article, and study the moduli space.

- Added `paper/d10-boundary-action.tex` and built
  `paper/d10-boundary-action.pdf` (7 pages).
- Construction:
  - D8-like source: `N8(S_DBI+S_WZ)` on `W9`, with
    `dF0=N8 delta_W9`.
  - Spin-c `Q` line: `F_Q/2pi=6h_Q+x/2`, `x=(2m+1)h_Q`.
  - Payen/coadjoint endpoint action for `g_j(tau) in SU(2)`, quantizing to
    `V_j=H^0(CP1,O(2j))`, `j in {0,1/2,1}`.
  - Boundary neutral field `eta_0` with `Q eta_0=0`, proving the photon
    direction has no boundary mass term.
  - Current kernel uses `A_j=sum_a T_a^(j) tensor e_a`, with
    `A_j^dagger A_j=j(j+1)`.
  - Feshbach reduction gives `X=j(j+1)/(X+j(j+1))`; `j=0` remains massless.
- Moduli-space result:
  - Minimal moduli:
    `disjoint union over (m,N8) of U(1)_theta_Q x R_{>0,mu}`.
  - Enlarged deformation includes `R_{>0,kappa_cur}` and optional
    `R_{>0,M_perp}`; canonical slice is `kappa_cur=1`.
- Verification: `pdflatex` run twice; no warnings/errors, no undefined refs,
  no underfull/overfull boxes, no forbidden placeholder phrases, and no
  `\over` hits.

## De Vries compatibility of boundary moduli — 13:52 CEST
User objective extended: explain or enhance the moduli for compatibility with
De Vries, including the Higgs mass and electroweak vacuum. User noted the
vacuum may come through Yukawa/fermions but is more likely direct.

- Updated `paper/d10-boundary-action.tex` and rebuilt
  `paper/d10-boundary-action.pdf` (9 pages).
- Enhanced the continuous moduli from only `theta_Q, mu` to:
  `theta_Q, mu, v_Q, lambda_H`, with optional `kappa_cur` and `M_perp`.
- Added section `Compatibility with the de Vries data`:
  - current metric deformation `c=sqrt(kappa_cur)`;
  - `X_pm(J;c)=(-c^2 J +/- sqrt(c^4 J^2+4c^2 J))/2`;
  - de Vries W/Z slice:
    `kappa_cur=1`, `M_W^2/mu^2=X_+(3/4;1)`,
    `M_Z^2/mu^2=X_+(2;1)`;
  - direct scalar/vacuum enhancement:
    `v_EW^2/(2mu^2)=|X_-(2;1)|`,
    `M_H^2/mu^2=|X_-(3/4;1)|`, `v_EW=sqrt2 v_Q`;
  - quartic modulus:
    `lambda_H=|X_-(3/4;1)|/(4|X_-(2;1)|)=0.12067...`.
- Kept Yukawa/fermion route out of the active action: it is identified only
  as an alternative replacement for the direct scalar condition.
- Verification: `pdflatex` run twice; no warnings/errors, no undefined refs,
  no underfull/overfull boxes, no forbidden placeholder phrases, and no
  `\over` hits.

## Proof/example audit after boundary-moduli edits — 13:58 CEST
User objective returned to the article quality gate: every section should have
graduate-level examples and arguments proved in main or appendix.

- Patched `paper/d10-boundary-action.tex` section `Summary of the construction`:
  - added proposition `Construction audit`;
  - added proof referencing the earlier propositions that prove each summary
    claim;
  - added example `Canonical compatibility checklist`.
- Rebuilt:
  - `paper/d10-boundary-action.pdf` (9 pages);
  - `paper/d10-kk-branes.pdf` (10 pages).
- Current section audit:
  - `d10-boundary-action.tex`: 8 sections; each has 1 proposition, 1 proof,
    and 1 example.
  - `d10-kk-branes.tex`: 8 main sections each have 1 proposition and
    1 example; appendix `Proofs and checks` proves all 8 propositions and has
    its own example.
- Verification: `pdflatex` run twice for both articles; no warnings/errors,
  no undefined refs, no underfull/overfull boxes, no forbidden placeholder
  phrases, and no `\over` hits.

## Current metric and vacuum potential attack — 14:08 CEST
User objective: attack goals 1 and 2 sequentially, and record the conclusions.

- Added `loop/current-metric-vacuum-attack.md`.
- Current-metric conclusion:
  - the KK current metric gives `G_ab=L_2^2 delta_ab`;
  - the Payen/Schur channel uses the orthonormal frame `e_a=K_a/L_2`;
  - hence `A_j^dagger A_j=j(j+1)` and the canonical value is
    `kappa_cur=1`;
  - any `kappa_cur != 1` requires an added boundary current metric, not the
    minimal D10 current geometry.
- Vacuum-potential conclusion:
  - a compatible selector potential in `rho, tau, v_Q, lambda_H, kappa_cur`
    pins the de Vries slice
    `kappa_cur=1`,
    `v_Q^2=mu_B(rho,tau)^2(1+sqrt3)`, and
    `lambda_H=(3+sqrt57)/(32(1+sqrt3))`;
  - it then gives `v_EW=sqrt2 v_Q` and
    `M_H^2=2 lambda_H v_EW^2`;
  - `rho,tau` reduce to the bulk coefficient-balance equations, so the
    absolute scale remains dependent on the integrated coefficients `B_i` and
    boundary scale function `mu_B(rho,tau)`.
- Verification: no TeX changed; forbidden placeholder/filler check passed on
  the new note.

## Unified D10 boundary/current/vacuum article — 14:21 CEST; full inclusion audit 14:36 CEST
User objective: unify the two TeX articles and the new current-metric/vacuum
note into a whole new article.

- Added `paper/d10-unified-boundary-current-vacuum.tex`.
- Rebuilt `paper/d10-unified-boundary-current-vacuum.pdf` (22 pages) after
  expanding the unified article from a synthesis into a full inclusion article.
- Article chain:
  - Part I contains the transformed full body of `paper/d10-kk-branes.tex`,
    with labels/references prefixed by `kk:`.
  - Part II contains the transformed full body of
    `paper/d10-boundary-action.tex`, with labels/references prefixed by `bd:`.
  - Part III contains the derived current-metric and coupled-vacuum material
    from `loop/current-metric-vacuum-attack.md`.
  - D10 carrier and probe windows:
    `M4 x CP2 x CP1`, M-circle/RR one-form, D0 probe, and D8-like boundary.
  - Boundary action:
    `W9=M4 x CP2 x S1_Q`, spin-c `Q` line, neutral photon section, endpoint
    orbit action, and `H^0(CP1,O(2j))` sectors for `j=0,1/2,1`.
  - Canonical current metric:
    KK current metric fixes `A_j^dagger A_j=j(j+1)` and `kappa_cur=1`.
  - Feshbach/de Vries slice:
    positive roots give the W/Z values; negative roots give the direct
    `v_Q` and `lambda_H` scalar assignments.
  - Coupled potential:
    selector potential pins `kappa_cur`, `v_Q`, and `lambda_H`; `rho,tau`
    obey the bulk coefficient-balance equations.
- Verification:
  - exact transformed source-body containment passed for both source articles;
  - source counts were preserved and extended:
    source articles have 17 sections, 16 propositions, 17 examples in total;
    unified article has 19 sections, 18 propositions, 19 examples;
  - `pdflatex` completed cleanly after cross-reference pass;
  - no LaTeX warning/error/undefined/overfull/underfull hits in the final log;
  - no forbidden placeholder/filler hits in the new TeX;
  - no `\over` hits in the new TeX.

## Long-term plan priority edit — 14:40 CEST
User objective: demote point 2 until the other gates are done, unless a
dependency appears.

- Updated `loop/long-term-devries-research-plan.md`.
- Gate 2 now carries an explicit deferred-priority note.
- Near-term sequence is now:
  1. Gate 1, Feshbach kernel;
  2. Gate 3, current metric;
  3. Gates 4 and 5, vacuum coefficients and selector potential;
  4. Gate 6, consistency checks;
  5. Gate 7, quantum/phenomenological matching;
  6. Gate 2 only after the others, unless Gate 1 or Gate 3 requires it.
- Verification: forbidden placeholder/filler check passed on the plan.

## Milestone traversal — 14:55 CEST
User objective: go across all milestones of
`loop/long-term-devries-research-plan.md`.

- Renamed the plan's active headings from gates to milestones to avoid the
  pre-decision staging language.
- Added `loop/devries-milestone-traversal-2026-05-25.md`.
- Traversed all seven milestones with claim/test/decision structure:
  - Milestone 1: Feshbach reduction works algebraically once `S_quad^(j)` is
    present; local D10 origin of `S_quad^(j)` is not derived.
  - Milestone 2: representation assignment remains deferred; no dependency
    blocks Milestones 1 or 3.
  - Milestone 3: `same current metric => kappa_cur=1` is derived; full D10
    metric plus RR/current vertical term remains to compute.
  - Milestone 4: bulk scaling and stationarity equations are present;
    coefficients `B_i` and `mu_B(rho,tau)` are not computed.
  - Milestone 5: selector potential is compatible but not induced from the
    local action.
  - Milestone 6: local consistency checks pass; global source balance,
    tadpoles, backreaction, and auxiliary-light-mode checks remain.
  - Milestone 7: no scheme/threshold phenomenology calculation exists yet.
- Global decision: the project is still a coherent D10 compatibility
  mechanism, not a proof that de Vries is forced.
- Verification: forbidden placeholder/filler check passed on the plan and the
  traversal note.

## `j=3/2` diphoton check — 15:19 CEST
User observation: a moduli branch could retain a `j=3/2` state in the range of
the Run 2 diphoton feature.

- Added `loop/jthreehalf-diphoton-phenomenology-check-2026-05-25.md`.
- Computed the positive-branch mass with the scale fixed by the `Z` slot:
  `mu=106.577412817518 GeV` and `M_{3/2}=96.5383318606582 GeV`.
- Checked the value against the published CMS Run 2 low-mass diphoton result:
  the largest deviation is at `95.4 GeV`, with local/global significance
  `2.9/1.3 sigma`, so this is a conditional phenomenology discriminator, not a
  discovery claim.
- Updated Milestone 7 in `loop/long-term-devries-research-plan.md` to include
  the `j=3/2` check only for a tower/moduli branch that retains that channel.

## Milestone 1 `q_j` source tests — 15:27 CEST
Execution objective: keep the Feshbach step constructive by testing possible
D10 sources of the image-channel field.

- Added `loop/milestone1-q-channel-source-tests-2026-05-25.md`.
- Tested five sources against the needed positive image field, diagonal
  `B+mu^2J_j`, mixing `mu^2A_j`, shared current metric, and single-pole
  spectral requirement.
- Decisions:
  - D8 normal fluctuation: scalar/radial support only, not an `Im A_j`
    propagating channel by itself.
  - Coadjoint endpoint rotor: supplies `V_j`, `T_a`, and `T_aT_b`, but no
    propagating denominator.
  - Boundary-current oscillator: surviving constructive route, provided its
    zero-mode Casimir gap and single-pole dominance are derived.
  - Hubbard-Stratonovich field: useful localization of a derived kernel, not a
    source of the pole.
  - RR/current vertical mode: common scale and normalization support, not the
    representation-dependent image channel.
- Updated the Milestone 1 plan and constructive-kernel note with the narrowed
  route.

## Boundary-rotor Casimir-gap candidate — 15:36 CEST
Execution objective: turn the surviving `q_j` route into a concrete local
mechanism to test.

- Added `loop/milestone1-boundary-rotor-casimir-gap-candidate-2026-05-25.md`.
- Candidate mechanism: a propagating boundary-current rotor has
  `H_rot=(2I)^-1 sum_a R_aR_a`; on spin `j`, this gives
  `M_q^2=mu^2 j(j+1)` if `1/(2I)=mu^2`.
- The Payen/coadjoint endpoint variable and the propagating oscillator are kept
  as separate roles: the endpoint supplies `V_j,T_a,T_aT_b`; the oscillator
  supplies `B+mu^2J_j`.
- Added failure tests: direct WZW conformal weight `J/(k+2)`, shifted Casimir,
  rescaled Casimir, or uncontrolled multi-pole density.
- Updated the Milestone 1 plan and source-test note with the rotor candidate.

## Milestone 3 current metric execution — 15:49 CEST
Execution objective: compute whether the current metric fixes `kappa_cur=1`
or leaves a boundary normalization parameter.

- Added `loop/milestone3-current-metric-execution-2026-05-25.md`.
- Computed the KK current metric:
  `G_ab^(2)=Vol^-1 int sqrt(g) g(K_a,K_b)=L_2^2 delta_ab`, so using
  `e_a=K_a/L_2` gives `A_j^dagger A_j=j(j+1)`.
- Inserted the Bailin-Love/Weinberg split:
  `L_{2,BL}^2=(1+beta)L_{2,horiz}^2` with
  `beta=0.328481702082924367895293909852`.
- Found the failure branch: if the boundary sees only the horizontal `CP1`
  current while the weak gauge coupling uses the full parent length, then
  `kappa_cur=1/(1+beta)=0.7527390090748721`, `c=0.8676053302480755`, and
  `sin^2 theta_W=0.24226537471822063`.
- Milestone 3 decision: `kappa_cur=1` passes only if the D8 endpoint/current
  channel couples to the full Bailin-Love current including the vertical
  RR/current piece.  This is now an explicit dependency for Milestones 1 and 6.

## Milestones 4 and 5 vacuum-selector execution — 16:02 CEST
Execution objective: test whether the bulk vacuum coefficients and selector
potential currently force the scale and scalar data.

- Added `loop/milestone4-5-vacuum-selector-execution-2026-05-25.md`.
- Evaluated the coupled `rho,tau` stationarity equations at
  `rho_*=9.463469757158872`.
- Found that Milestone 4 is a coefficient-balance target, not yet a prediction:
  `B_R,B_H,B_0,B_2,B_4,B_6,B_loc` and `mu_B(rho,tau)` are not computed from the
  selected D10 background.
- The `B_0`/Romans term has large target weights:
  `4.554107135924378e5` in the `rho` equation and `-2.873177010112117e6` in
  the `tau` equation after scaling.
- Milestone 5 decision:
  - `kappa_cur` is not a minimal selector variable on the full-current branch;
  - the `v_Q` condition is compatible with the neutral `eta` field but not
    induced by the current action;
  - the `lambda_H` condition is a scalar-Hessian target, not a computed
    coefficient.
- Updated the long-term plan with these execution decisions.

## Milestone 6 consistency execution — 16:13 CEST
Execution objective: audit the required local and global consistency checks
before any proof claim.

- Added `loop/milestone6-consistency-execution-2026-05-25.md`.
- Local passes:
  - spin-c/Freed-Witten placement on `CP2`;
  - local D8/O8 convention and Romans source formula;
  - photon masslessness from `Q eta_0=0`;
  - positive reduced Feshbach spectral density for a positive `q_j` oscillator.
- Conditional pass:
  - gauge invariance of the augmented kernel if `p_j,q_j` transform in
    `V_j,Im A_j`; the local-origin action is still Milestone 1.
- Not passed:
  - full Bianchi/tadpole equations;
  - backreaction of D8/O8/RR sources on the product/coset ansatz;
  - mass gaps for the auxiliary complement, higher rotor levels, and string
    oscillator modes;
  - D8/RR placement of the full Bailin-Love current required by Milestone 3.
- Updated the long-term plan with the Milestone 6 decision.

## Milestone 7 phenomenology execution — 16:26 CEST
Execution objective: compare the tree-level de Vries outputs with current
scheme-specific experimental inputs.

- Added `loop/milestone7-phenomenology-execution-2026-05-25.md`.
- Checked current external inputs:
  - PDG live 2026 W entry: `m_W=80.3625 +/- 0.0077 GeV`,
    `m_W/m_Z=0.88136 +/- 0.00015`;
  - PDG 2025 gauge/Higgs summary: `m_Z=91.1880 +/- 0.0020 GeV`,
    `m_H=125.20 +/- 0.11 GeV`, `sin^2(theta_eff)=0.23148 +/- 0.00013`;
  - CMS 2026 W mass: `80.3602 +/- 0.0099 GeV`;
  - CMS HIG-20-002: largest low-mass diphoton deviation at `95.4 GeV`,
    local/global `2.9/1.3 sigma`.
- Computed tree-level values:
  - `sin^2 theta_dV=0.2231013223008662`;
  - PDG-live on-shell value `0.2233390021445395`, pull `1.56 sigma`;
  - CMS-2026 W-mass on-shell value `0.22338345807193183`, pull `1.45 sigma`;
  - raw scalar scale `mu sqrt(J_H)=122.38971037206139 GeV`;
  - tower-branch `M_{3/2}=96.53875533197167 GeV`.
- Milestone 7 decision: still a close on-shell mass-ratio clue, but no
  phenomenological prediction until threshold/running, scalar Hessian, and
  possible `j=3/2` production/branching are computed.
- Updated the long-term plan with the current-data execution decision.

## Milestone 2 representation assignment execution — 16:37 CEST
Execution objective: return to the deferred representation assignment after
executing the other milestones.

- Added `loop/milestone2-representation-assignment-execution-2026-05-25.md`.
- Borel-Weil gives `V_j=H^0(CP1,O(2j))` and
  `T_aT_a=j(j+1)` for all half-integer `j`, so it supplies the needed
  `0,3/4,2` Casimirs but does not exclude higher representations.
- Finite branch decision:
  `SU(2)_2` gives only `j=0,1/2,1`; then photon/W/Z assignment is coherent:
  `j=0` has no Feshbach coupling and is protected by `Q eta_0=0`,
  `j=1/2` is the lowest center-odd/fundamental endpoint sector, and `j=1` is
  the lowest center-even neutral bilinear.
- Tower branch decision:
  a Peter-Weyl rotor oscillator permits `j=3/2` and higher; this keeps the
  `96.54 GeV` diphoton discriminator but removes finite-set predictivity.
- Updated the long-term plan with the branch fork.

## Rotor stress test — 16:47 CEST
Execution objective: test whether the Milestone 1 rotor candidate is compatible
with Milestone 2's finite representation assignment.

- Added `loop/milestone1-rotor-stress-test-2026-05-25.md`.
- Result:
  - a second-order `SU(2)` rotor gives the desired positive Casimir gap
    `H=J_j/(2I)` and passes the diagonal `B+mu^2J_j` part if
    `1/(2I)=mu^2`;
  - the same rotor has a Peter-Weyl tower and does not exclude `j=3/2`;
  - it also needs an additional D8/current projection to land in `Im A_j` and
    an action-derived vertex `mu^2A_j` with no unwanted contact term.
- Branch tension:
  - rotor tower branch keeps the `96.54 GeV` state and loses finite-set
    predictivity;
  - finite `SU(2)_2` branch keeps photon/W/Z only but needs a zero-mode
    Casimir mass operator instead of direct `L0`.
- Updated the Milestone 1 rotor note and Milestone 2 assignment note.

## Milestone execution summary — 16:54 CEST
Execution objective: consolidate the all-milestone execution state after the
first pass across Milestones 1--7.

- Added `loop/milestone-execution-summary-2026-05-25.md`.
- Summary decision: the construction is still a D10 compatibility framework,
  not a proof that de Vries is forced.
- Main fork:
  - finite current branch: finite photon/W/Z set, but needs a zero-mode
    Casimir mass operator in the finite sector;
  - rotor tower branch: natural `mu^2J` gap and `j=3/2` phenomenology, but no
    finite-set predictivity.
- Next work order is narrowed to:
  finite-sector mass operator or tower acceptance, D8/RR full-current placement,
  Bianchi/tadpole source table, IIA vacuum coefficients, and scalar Hessian.

## Finite zero-mode image operator — 17:07 CEST
Execution objective: attack the finite-branch mass-operator bottleneck.

- Added `loop/milestone1-finite-zero-mode-image-operator-2026-05-25.md`.
- Candidate:
  - keep the `SU(2)_2` finite Hilbert space `V0 + V1/2 + V1`;
  - define `A_jp=sum_a T_a p tensor e_a`;
  - set the image channel `Q_j=Im A_j`;
  - use the image Hamiltonian `mu^2 A_jA_j^dagger` on `Q_j`.
- Algebra:
  - for `q=A_jp`, `A_jA_j^dagger q=J_j q`;
  - the Feshbach denominator is therefore `B+mu^2J_j`;
  - no Peter-Weyl rotor tower is introduced.
- Updated the rotor stress test, milestone summary, and long-term plan.

## Finite image local-origin test — 17:18 CEST
Execution objective: reduce the finite image-channel D10-origin problem to a
concrete contact-residue calculation.

- Added `loop/milestone1-finite-image-local-origin-test-2026-05-25.md`.
- Positive square test:
  `mu^2||A_j^dagger q_j-p_j||^2` gives the desired image mass and mixing but
  also produces an unwanted `+mu^2||p_j||^2` open-channel contact.
- The endpoint Wilson second variation has the right sign to cancel this
  contact.
- The new finite-branch test is:
  after image projection with `P_j=(1/J_j)A_jA_j^dagger`, the Wilson contact
  must be `-mu^2` times the identity on `V_j`.
- If the projected contact residue is `1`, the finite branch can avoid the
  rotor tower while keeping the de Vries kernel.  If not, the pole equation is
  shifted.
## 2026-05-25 17:32 CEST -- Wilson contact residue

- Added `milestone1-wilson-contact-residue-calculation-2026-05-25.md`.
- Completing the finite image-channel square fixes the required contact as
  `-\mu^2`.
- The raw Wilson second variation gives `-\mu^2J_j`, and image projection does
  not remove the `J_j` factor.
- An inverse image metric
  `(A_jA_j^\dagger|_{\operatorname{Im}A_j})^{-1}` gives the unit residue.
- Conclusion: ordinary Wilson expansion alone does not derive the finite
  Feshbach kernel; the finite branch needs an inverse-image-metric boundary
  contact or an equivalent local term.
## 2026-05-25 17:45 CEST -- 1PI contact bookkeeping

- Added `milestone1-1pi-contact-bookkeeping-2026-05-25.md`.
- The inverse image metric is the static Schur complement of the retained
  `q_j` oscillator:
  `-mu^2 A_j^dagger(A_jA_j^dagger|_Im)^-1A_j=-mu^2`.
- The finite branch is therefore not rejected by the inverse metric itself.
- The branch fails if the raw Wilson `T_aT_b` term is also present as a direct
  1PI `p_j` contact.
- Milestone 1 is now narrowed to a no-double-counting test for the retained
  image oscillator action.
## 2026-05-25 17:58 CEST -- Connected versus 1PI Wilson test

- Added `milestone1-connected-1pi-wilson-test-2026-05-25.md`.
- The endpoint action is linear in the source, so the Wilson second derivative
  is a two-current connected response, not a microscopic quadratic seagull.
- If `q_j` is retained as the local image-current channel, that connected
  response is represented by `q_j` exchange.
- Conclusion: the raw `T_aT_b` Wilson tensor should not be added again as a
  direct 1PI `p_j` contact.  The residue obstruction is removed at this
  bookkeeping level.
- Milestone 1 now reduces to deriving the local `q_j` oscillator, its gap, its
  sign, and the `mu^2A_j` mixing coefficient from the D10 boundary dynamics.
## 2026-05-25 18:13 CEST -- `q_j` coefficient lock

- Added `milestone1-q-oscillator-coefficient-lock-2026-05-25.md`.
- A generic canonically normalized image oscillator has
  `Gamma=B-gamma^2 mu^4 J/(B+alpha mu^2 J)`.
- With `mu_eff^2=alpha mu^2`, the pole equation is
  `X=r^2 J/(X+J)` with `r=gamma/alpha`.
- The de Vries pole requires `r=1`.
- A single local current-displacement square
  `alpha mu^2 ||A_j^dagger Q_j-p_j||^2-alpha mu^2||p_j||^2`
  forces `gamma=alpha`; the common coefficient is absorbed into `mu_eff`.
- Milestone 1 now asks whether the D10 boundary dynamics generate that square,
  or another coefficient-lock mechanism, for the first positive image-current
  pole.
## 2026-05-25 18:28 CEST -- Current-displacement square origin test

- Added `milestone1-current-displacement-square-origin-test-2026-05-25.md`.
- DBI/Stueckelberg displacement terms have the right one-square structure and
  would force `gamma=alpha`.
- The bare D8 normal displacement is a scalar on `W9`, not an
  `Im A_j subset V_j tensor R^3` field.
- The endpoint orbit action supplies `A_j` but no second-order image oscillator.
- A generic boundary-current oscillator still has independent `alpha,gamma`
  unless it is identified as a vector-bundle displacement.
- Conclusion: the finite proof path now needs an `Im A_j` displacement field
  from the D8/open-current interface.  Without that field, the finite branch is
  compatible but not forced.
## 2026-05-25 15:48 CEST -- Mixed Hom image-displacement test

- Added `milestone1-mixed-hom-displacement-test-2026-05-25.md`.
- The mixed sector `H^0(CP1,Hom(O(0),O(2j)))=V_j` passes the rank/isometry
  test: `Q_j=A_jy_j/sqrt(J_j)` lies in `Im A_j` for `j>0`.
- The action test still has not passed: de Vries needs the one-square Hom norm
  `||sqrt(J_j)y_j-p_j||^2`, while a generic mixed-sector action leaves
  `r=c_g sqrt(Z_y)/c_m`.
## 2026-05-25 15:55 CEST -- Mixed Hom local-action source test

- Added `milestone1-mixed-hom-local-action-source-test-2026-05-25.md`.
- Payen supplies the endpoint representation and Wilson insertions `T_a`,
  `T_aT_b`; it does not supply a propagating Hom field with the one-square norm.
- The current D8 DBI/WZ package supplies geometric norms and RR charges, but
  no term identifying the mixed Hom mode with `sqrt(J_j)y_j-p_j`.
- Verdict for the current source package: finite branch remains compatible, not
  predictive; the next non-dependent item is the D8/RR full-current placement.
## 2026-05-25 16:05 CEST -- D8/RR full-current placement test

- Added `milestone3-d8-rr-full-current-placement-test-2026-05-25.md`.
- Payen fixes the endpoint representation tensor for whichever connection is
  inserted; it does not choose full Bailin-Love current over horizontal `CP1`.
- The D8 WZ skeleton ties the carrier to RR/Chern charge data, but does not add
  the vertical `L_{2,vert}` contribution to the endpoint current metric.
- Verdict: `kappa_cur=1` remains a full-current branch condition in the written
  action.  The horizontal-only placement gives `sin^2 theta_W=0.242265...`.
## 2026-05-25 16:15 CEST -- Source-balance table

- Added `milestone6-source-balance-table-2026-05-25.md`.
- Two-endpoint type I' bookkeeping can cancel the total eight-charge.
- The minimal spin-c lift leaves induced lower charge `208h_Q+673h_Q^2`.
- No current bulk flux, image sector, K-theory identification, or extra local
  source cancels that vector, so Milestone 6 fails globally for the current
  data.
## 2026-05-25 16:24 CEST -- Lower-charge cancellation test

- Added `milestone6-lower-charge-cancellation-test-2026-05-25.md`.
- Unequal type I' endpoint D8 stacks fail the D6 tadpole because the remaining
  lift integer is odd.
- Balanced stacks can cancel D6 with opposite spin-c lifts, but the D4 residual
  is `(4M^2-3)h_Q^2`, with minimum `h_Q^2`.
- Existing bulk-flux coefficients do not provide a selected `H,F0,F2`
  cancellation, so Milestone 6 still fails globally for the current package.
## 2026-05-25 16:34 CEST -- H-flux cancellation test

- Added `milestone6-h-flux-cancellation-test-2026-05-25.md`.
- Product `CP2 x CP1` and flag `F_{1,2}(C^3)` have only even cohomology, so
  `H^3=H^5=0`.
- With no NS5 source, closed `H` has no cohomology class; `HF0` and `HF2` cannot
  cancel the lower source entries.
- Milestone 6 now needs a localized/K-theory/image lower-charge sector or a
  different compactification/source package.
## 2026-05-25 16:42 CEST -- K-theory cancellation test

- Added `milestone6-k-theory-cancellation-test-2026-05-25.md`.
- Product and flag spaces have torsion-free even cohomology, so the rational
  Chern character detects the lower charge data.
- A bare K-theory identification cannot set the nonzero `h_Q` or `h_Q^2`
  lower vector to zero.
- Milestone 6 now needs an actual localized or image lower-charge sector.
## 2026-05-25 16:11 CEST -- Image lower-charge sector test

- Added `milestone6-image-lower-charge-sector-test-2026-05-25.md`.
- Same-lift source balance would require a lower-only image vector
  `-208h_Q-673h_Q^2`.
- The balanced opposite-lift endpoint package cancels D6 first and leaves a
  minimal D4 residual `h_Q^2`.
- The irreducible missing source is therefore a pure negative D4 unit
  `-h_Q^2`.
- A literal anti-D4 or O4-like image source would enlarge the source package and
  add localized tension/backreaction data not present in the current action.
## 2026-05-25 16:30 CEST -- O4 image realization test

- Added `milestone6-o4-image-realization-test-2026-05-25.md`.
- In the doubled type I' convention, `O4^-` has charge `-1` in D4 units, so
  the charge magnitude matches the missing `-h_Q^2`.
- A clean O4 support would require `{pt}_{CP2} x S^1_Q`.
- Holomorphic projective involutions of `CP2` fix `CP0 union CP1`; with the
  `RP1` fixed circle in `CP1` this gives an O4 component plus an O6 component.
- Standard complex conjugation fixes `RP2`, giving O6-type support with the
  `CP1` fixed circle.
- Verdict: the O4 match is not a current-package cancellation; it requires an
  enlarged O4/O6 source table or must be rejected.
## 2026-05-25 16:21 CEST -- O4/O6 source-table test

- Added `milestone6-o4-o6-source-table-test-2026-05-25.md`.
- The holomorphic product involution contributes `-4h_Q-h_Q^2` in the flattened
  source table: `O6^-` gives `-4h_Q`, `O4^-` gives `-h_Q^2`.
- The D8 endpoint D6 lattice is `16Z h_Q`, so a single O4/O6 package cannot be
  absorbed by changing endpoint lifts.
- Multiple identical packages also fail: D6 cancellation requires the package
  count to be a multiple of four, while the balanced endpoint D4 coefficient
  `4M^2-3` is `1 mod 8`.
- Verdict: the O4/O6 enlargement does not close Milestone 6 inside the current
  D8/O8 endpoint package.
## 2026-05-25 16:24 CEST -- Source-balance no-go

- Added `milestone6-source-balance-no-go-2026-05-25.md`.
- Scoped assumptions: current D8/O8 type I' endpoints, selected product/flag
  topology, closed `H` with no NS5 source, rational K-theory charge detection,
  and the tested product O4/O6 package.
- Endpoint-only source balance fails; closed `H` and bare K-theory do not erase
  the lower vector.
- The product O4/O6 package fails both single-copy and multi-copy D6/D4
  congruence tests.
- Verdict: the current D8/O8 package fails Milestone 6 as a global
  compactification proof.
## 2026-05-25 16:33 CEST -- Extra-mode mass-gap table

- Added `milestone6-extra-mode-mass-gap-table-2026-05-25.md`.
- If the finite image field is unprojected in `V_j tensor R^3`, the complement
  `({Im A_j})^\perp` has denominator `B` and is massless.
- The mixed Hom field removes that complement by mapping `V_j` to `Im A_j`,
  but the current source package does not derive the one-square Hom action.
- The rotor branch keeps a light tower: with the Z fixing the scale,
  `j=3/2` is `96.5388 GeV`, `j=2` is `99.5795 GeV`, and higher states remain
  near the weak scale.
- Verdict: the current action fails Milestone 6's extra-light-mode check.
## 2026-05-25 16:32 CEST -- Vacuum rank and selector test

- Added `milestone4-5-vacuum-rank-selector-test-2026-05-25.md`.
- On the selector branch the squared selector terms have zero `rho,tau`
  derivatives, so they do not select the bulk moduli.
- The bulk stationarity equations are two linear constraints on seven
  coefficients.
- Example fit: with `B_H=B_0=B_2=B_6=0`, stationarity at any chosen `rho` is
  obtained from `B_4=B_R tau^2` and
  `B_loc=-(2/3)B_R tau rho^-2`; at `rho_*` this is
  `B_loc=-0.007444027070759169 B_R tau`.
- Combined with the Milestone 6 source-balance no-go, Milestones 4 and 5 remain
  compatibility data, not vacuum/scalar predictions.
## 2026-05-25 16:40 CEST -- Neutral scalar Hessian rank test

- Added `milestone5-neutral-scalar-hessian-rank-test-2026-05-25.md`.
- For a canonical radial potential
  `V_h=a h^2+b h^4+V_0`, the nonzero minimum has
  `h_0^2=-a/(2b)` and `M_h^2=8b h_0^2=-4a`.
- Imposing the selector value `h_0^2=2J_v mu_B^2` leaves
  `M_h^2/mu_B^2=16bJ_v`; the de Vries value `J_H` is obtained by setting
  `lambda_H=J_H/(4J_v)`, with `b=lambda_H/4`.
- Neutral mixing does not fix the number: `M_h^2=J_H mu_B^2` is one spectral
  constraint on the Hessian matrix.
- Verdict: the negative-branch scalar numbers are compatible targets, not
  scalar-Hessian predictions in the present action.
## 2026-05-25 16:45 CEST -- Replacement source requirements

- Added `milestone6-replacement-source-requirements-2026-05-25.md`.
- For an added lower-source sector
  `Q_new=alpha h_Q+beta h_Q^2`, source balance requires
  `alpha=-(N_L M_L+N_R M_R)/2` and
  `beta=-[((2M_L^2-1)N_L+(2M_R^2-1)N_R)/16-1]`.
- The minimal balanced opposite-lift target is `Q_new=-h_Q^2`.
- Unequal endpoint stacks require
  `Q_new=-16M h_Q-(4M^2-3)h_Q^2`.
- Any D6-bearing repair must fit the `16Z h_Q` endpoint lattice.  The tested
  O4/O6 package `-4k h_Q-kh_Q^2` fails because D6 cancellation forces
  `k=0 mod 4`, while the balanced endpoint D4 coefficient is `1 mod 8`.
## 2026-05-25 16:55 CEST -- Source branch decision

- Added `milestone6-source-branch-decision-2026-05-25.md`.
- The minimal charge repair `-h_Q^2` is not accepted as a patch to the current
  compactification route.
- A standalone anti-D4 would add localized tension, an open sector, and
  backreaction; the scalar potential and mode spectrum would have to be
  recomputed.
- An O4-only source is not produced by the tested product involutions.  The
  natural product O4/O6 package fails the endpoint congruences.
- Verdict: the current D8/O8 compactification branch is closed for proof
  claims.  A revived branch must be a new compactification ansatz, not a
  source patch.
## 2026-05-25 17:02 CEST -- Current-route no-prediction theorem

- Added `current-route-no-prediction-theorem-2026-05-25.md`.
- The theorem is scoped to the present D8/O8/Payen/RR package, endpoint
  spaces, finite image/Hom candidate, rotor candidate, closed `H`, bare
  K-theory, and tested product O4/O6 routes.
- Verdict: under those assumptions, at least one mandatory pass condition
  fails on every path to a de Vries prediction.  The current route is a
  compatibility framework, not a proof branch.
## 2026-05-25 17:08 CEST -- Goal completion audit

- Added `goal-completion-audit-2026-05-25.md`.
- Audited all seven milestones against their execution notes and the
  route-level theorem.
- Verified that the unified article and `/tmp` PDF copy are current.
- Verdict: the milestone execution objective is complete for the scoped
  current D8/O8 boundary-current route.
