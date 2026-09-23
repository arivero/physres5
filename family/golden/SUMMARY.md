# golden and golden2: quantized quartic, superstrings and Kaluza–Klein

Curated for physres5 on 2026-09-23. The source repositories were read and left unchanged.
Every number quoted below was recomputed during curation from PDG 2024 inputs
M_Z = 91.1876 GeV, M_W = 80.3692 GeV, m_H = 125.20 GeV, v = 246.21965 GeV (from G_F) and m_t = 172.7 GeV.

**physres5 hooks.** A1: the Casimir matrix Q(J) = μ²[[0, √J], [√J, −J]]. A2: pole placement.
A3: ordered assignment (J_W, J_Z) = (3/4, 2). Appendix D targets (`manuscript/sections/D_theorem_targets.tex`):
D-pole (pole placement and Δ_match), D-assign (electroweak assignment and ray admissibility),
D-kernel (local route kernel: light subspace, inner product, normalization Λ_J, entry conditions
Σ_hh = 0, Σ_aa = J, Σ_ha Σ_ah = J, pole map), D-partner (negative branch, scalar functional F_sc, α endpoint),
D-branch, D-Regge and D-SUSYQM (the three additional filters). App-E: `E_dimensional_interpolation.tex`.

**Notation map.** golden solves x⁴ + Λ_j x² − Λ_j = 0 with Λ_j = j(j+1) and x = m/M∞.
golden2 writes u = x² = M²/M*² and λ = j(j+1). Hence x_golden² = u_golden2 = x_physres5, λ = Λ_j = J,
and M∞ = M* = μ (the weak project calls it m₀). The spin-½ and spin-1 entries are the physres5 samples J = 3/4 and J = 2,
so x_{1/2}/x_1 = √(x₊(3/4)/x₊(2)) = 0.881418559879 is the de Vries quotient and 1 − x₊(3/4)/x₊(2) = 0.22310132.

## 1. Provenance

| | golden | golden2 |
|---|---|---|
| Source path | `/home/codexssh/golden` | `/home/codexssh/golden2` |
| Git | 19 commits; content 2026-05-26 22:18 → 2026-05-27 00:02 (last content commit `5c5a009`); `4ae034f` (2026-09-23) adds OPUS_IDEAS.md | 15 commits; content 2026-05-26 22:16 → 2026-05-27 00:29 (last content commit `abc1930`); `187ed32` (2026-09-23) adds conversation.txt, the slide and OPUS_IDEAS.md |
| Stated author | "Codex GPT 5.5" | "Claude Opus 4.7" |
| Format | one LaTeX file, 71 numbered sections, 7 TikZ figures | Markdown with raw TikZ blocks, built by pandoc + xelatex with `tikz-header.tex`; 18 sections, 6 appendices, 5 figures |
| PDF | 50 pp. The 53-page layout of `a31716a`/`3d15db8` was cut back to 50 pp in `5c5a009`, which removed four background sections (Einstein-frame scaling, worldsheet CFT, Calabi–Yau local sectors, flux quantization) | 40 pp |
| Review | one Claude Opus critique; its text is absent from the repo, and the user's reply (golden/conversation_user_inputs.txt, input 11) records its two accepted demands | two GPT-5.5 referee reports, pasted into the session and logged in golden2/conversation.txt; the second report's verified items were patched in `faf9e0c` |

Both papers carry the title "Experimental Predictions of String Theory".

**Relation between the two versions.** The user ran two agent sessions in parallel from one prompt sequence (Codex and Claude Code); their first commits are two minutes apart.
The prompt logs (golden2/conversation.txt, 32 user messages; golden/conversation_user_inputs.txt, 13 inputs; both summarized here and left uncopied) show the sequence:
study x⁴ + x²J² − J² = 0 at J = 1; quantize J² → j(j+1) for j ≤ 3/2; write a 50-page article linking it to superstrings and Kaluza–Klein;
a user hint with the numbers 0.7541414352817 and 0.855599677167 (golden §6 quotes the same numbers), which led both sessions to the W/Z quotient;
GeV values for j = 0 and 3/2; the tachyonic branch as m_t or the electroweak vacuum; an introduction on 2025–26 AI results on Erdős problems;
a "cutthroat" reframing along string, Kaluza–Klein and Connes lines; a work loop on the tachyonic Higgs seed; the classical 1981–84 Kaluza–Klein reading
(infrared SU(3)×U(1) in five extra dimensions, electroweak restoration in seven); recovery of themes deleted since the first commit;
J as a brane angular momentum, since neither branch scales as Regge; illustrations with a 53-page limit; cross-vendor criticism;
credit for the quotient to Hans de Vries (Physics Forums, 2004); and, after the second referee report, "path but no retreat" (patch errors, keep the framing).

**Relation to the siblings.** The weak project (2026-05-16, ten days earlier) uses the same 2×2 Casimir matrix, the same scale m₀ ≈ 106.57 GeV and the same j = 3/2 value 96.5 GeV.
golden §63 (Higgs work loop) and weak's rank-1 spurion address the same gap between the negative-branch seed 122.4 GeV and m_H = 125.2 GeV.
The D = 11/10/9 interpolation already in physres5 App-E is the same dimensional-flow idea that golden §17 and golden2 §4.8 introduce at the user's request.

## 2. Canonical version

**golden2 is canonical.**
(1) It is the reviewed version: two GPT-5.5 referee rounds, with the second round's verified errors patched in `faf9e0c`.
(2) It states the claims in their most testable form: the explicit normalization M* = v√3/4, algebraic gauge couplings, a residual table for four scales, the Higgs geometric-mean identity, the j ≤ 10 spectrum and a stated falsifier window.
(3) It records the concessions that physres5 needs as negative results: the single-field Kaluza–Klein route fails, the spectral-action estimate misses by 30.6%, three of the four "lines" share one ansatz, and the Myers radius grows without saturating.
(4) Its last content commit is the later one, and it carries the corrected field statement for the de Vries number.

golden is kept as the companion, as source only (its 50-page PDF was dropped during de-duplication). Its algebra is cleaner, and it holds two items absent from golden2: the coefficient test for a reduced potential (§68) and a Higgs work program that locks the W/Z ratio (§63).
About half of its length is generic Kaluza–Klein and string background (for example §§12–16, 20–28, 30–32 and 49–54).

## 3. Goal and final conclusion

**Goal.** A 50-page article (53 at one stage) that reads the Casimir-quantized quartic as an electroweak mass law and embeds it in Kaluza–Klein, superstring and Connes spectral-geometry language.
Both introductions frame the work against 2025–26 news about AI solutions of Erdős problems; that framing carries no physics content.

**Conclusion stated by the papers.** One mass scale and the first two nonzero spins give M_W/M_Z = 0.881418559879, 6.5×10⁻⁵ from the measured ratio.
The negative branch gives 122.4 GeV and 176.2 GeV, read as v/2 and v/√2 (golden2) or as the bare Higgs seed and the vacuum scale (golden).
The product m_H² = M_Z·|M₋(j=1)| gives 126.8 GeV. The j = 3/2 root gives 96.5 GeV. The Kaluza–Klein, string, Connes (and, in golden2, AdS/CFT) lines are presented as consistent with the quartic.

**Curator's conclusion.** The durable content is the algebra of the secular equation in mass variables, the one precise coincidence that physres5 already takes as its starting point, and a set of explicit failures of candidate derivations.
The four-scale identification, the Higgs value and the 96.5 GeV state agree at 0.6–1.3%, which is 90–200 times the residual of the vector ratio, and each rests on an extra identification rule.
Neither paper derives the quartic from a controlled model. The referee verdicts were REJECT (first GPT-5.5 report) and "Mathematical interest: LOW" (second report).

## 4. Valuable ideas and results

1. **Mass form and inverse quantization rule.** With x = m/μ the relation reads m⁴/[μ²(μ² − m²)] = j(j+1); in physres5 variables the positive root obeys J = x²/(1 − x) (golden §6, §55; golden2 eq. 2.6).
   *Reason:* every positive-branch mass lies below μ, and any measured ratio converts directly into the Casimir it requires.
   *Bears on:* A1, D-branch.

2. **Bounded tower and non-Regge growth of both branches.** x₊ = 1 − 1/J + 2/J² − …, |x₋| = J + 1 − 1/J + …; neither branch follows J ∝ α′M² (golden §19; golden2 §16.1).
   With μ fixed by M_Z, a tower labelled by j would put positive-branch states at 96.54, 99.58, 101.45, 102.68, 103.52, 104.12 GeV for j = 3/2 … 4, accumulating at μ = 106.58 GeV,
   and negative-branch magnitudes at 227.85, 279.41, 331.18, 383.21 GeV for j = 3/2 … 3 (golden2 §14.7 and App. D, which print the positive values about 0.01 GeV high).
   *Reason:* this is the spectrum that any physres5 route inherits once J labels a tower; D-Regge demands that it be predicted or projected out.
   *Bears on:* D-Regge, D-branch.

3. **Three readings of J.** Accidental (the SU(2) Casimir of a harmonic, current-algebra or finite-spectral sector), literal (the Noether charge of a wrapped or polarized brane under a fixed-J Legendre transform), and holographic (a spin or R-charge of a dual operator whose bulk carrier is an expanded brane) (golden §19, §29).
   golden2 §16 adds the fuzzy-sphere reading: J is the Casimir of the N = 2j + 1 matrix representation of a Myers dielectric brane.
   *Reason:* the brane readings attach J to a brane collective coordinate, the language of the physres5 endpoint route (§6f).
   *Bears on:* D-kernel (endpoint route), D-Regge.

4. **Radial normalization μ = v√3/4.** Setting μ² = 3v²/16 = J_W v²/4 reproduces M_Z to +3.6×10⁻⁴ and M_W to +4.3×10⁻⁴ with v from G_F (golden2 §14.3).
   Equivalently g² = J_W x₊(J_W) = 3(√57 − 3)/32 = 0.42655 against 4M_W²/v² = 0.42618, and g² + g′² = 3(√3 − 1)/4 = 0.54904 against 4√2 G_F M_Z² = 0.54864.
   The agreement holds in the G_F scheme; the MS-bar value ĝ_Z² = 4πα̂/(ŝ²ĉ²) = 0.55251 (α̂⁻¹ = 127.951, ŝ² = 0.23122) sits 0.7% higher, and golden2's own spectral-action estimate gives μ/v = 0.3315.
   *Reason:* physres5 fixes μ provisionally by M_Z and keeps v as the radial datum; this is the one explicit proposal that ties μ to v, with a sharp check.
   *Bears on:* D-pole, D-kernel (normalization Λ_J).

5. **Negative-branch magnitudes as Higgs-sector scales.** With μ fixed by M_Z: |x₋(3/4)|^½ μ = 122.39 GeV (v/2 − 0.59%) and |x₋(2)|^½ μ = 176.16 GeV (v/√2 + 1.18%, m_t + 2.0%).
   Vieta gives M₊|M₋| = μ²√J exactly, and the rule m_H² := M_Z·|M₋(J=2)| = √2 μ² gives 126.74 GeV (+1.2%; golden2 quotes 126.79 GeV with μ = v√3/4) (golden2 §14.2–14.5; golden §6 table).
   physres5 §5 lists the same magnitudes as descriptive arithmetic. golden2 assigns them to v/2 and v/√2; golden assigns the J = 3/4 value to a bare Higgs seed.
   *Reason:* explicit, normalized candidates for F_sc, each with its residual on record.
   *Bears on:* D-partner, A2.

6. **The duality map is the Vieta involution.** golden2 §7 defines the "winding" variable ũ = u/(1 − u) and proves u·ũ = J.
   On the positive root this gives ũ₊ = J/x₊ = −x₋ = |x₋| exactly (1.31873 at J = 3/4; 1 + √3 at J = 2). golden2 computes both sides at J = 2 in separate sections and never connects them.
   *Reason:* the physres5 relation x₋ = −J/x₊ acquires a momentum–winding reading in which the partner branch is the dual image of the vector branch.
   *Bears on:* D-branch, D-partner.

7. **The secular equation as a stationarity condition, with a coefficient test.** V(x) = x⁶/6 + J x⁴/4 − J x²/2 has dV/dx = x(x⁴ + J x² − J).
   Its nonzero extrema are the positive roots, V″ = 2x⁴(2 − x²)/(1 − x²) > 0 there, and the origin is unstable for J > 0 (golden §9, §44, §66).
   A reduced potential A x⁶ + B J x⁴ − C J x² reproduces the relation exactly when 2B = 3A and C = 3A (golden §68).
   golden §61 assigns the three terms to brane tension, the fixed-J Legendre transform and the Wess–Zumino coupling; a rotor with moment of inertia I ∝ x² contributes J/x², so that assignment still needs a worked brane model.
   *Reason:* a one-field alternative to the 2×2 matrix of A1 and a concrete pass/fail test for any Kaluza–Klein or brane reduction.
   *Bears on:* A1, D-kernel, D-SUSYQM.

8. **Higgs work program with the vector ratio locked.** m²_{H,pole} = |m_{T,1/2}|² + Π_H(m_H²) + Δ_th + Δ_mix needs +682.9 GeV², i.e. +4.56% of the seed (golden normalizes μ on M_W = 80.3625 GeV; seed 122.371 GeV, target 125.13 GeV).
   The correction is admissible only if the bracket 1 + ½(Π_W/M²_{W,0} − Π_Z/M²_{Z,0}) + Δ_ct multiplying M_W/M_Z stays at 1 within the measured tolerance (golden §63).
   weak/PAPER.tex §4.2 shows that the shift must be rank-1 along the tachyonic eigenvector; a trace-preserving shift moves M_W to 84.60 GeV.
   *Reason:* the correct statement of the scalar-side matching problem, including the constraint that protects the physres5 observable.
   *Bears on:* D-partner, D-pole.

9. **Field of definition.** cos²θ = x₊(3/4)/x₊(2) lies in ℚ(√3, √19): √57 = √3·√19 comes from the J = 3/4 discriminant 57/16 and √3 from the J = 2 discriminant 12; cos θ needs one more quadratic extension (golden2 §13.11, corrected after referee #2).
   *Reason:* the exact algebraic statement of the de Vries number for the physres5 algebra appendix.
   *Bears on:* A1, A3.

10. **Dimensional flow.** Witten's count needs seven extra dimensions for SU(3)×SU(2)×U(1) isometry and five for SU(3)×U(1); golden2 identifies the two extra dimensions with the SU(2)_L/U(1) sphere, whose scalar Laplacian eigenvalues are ℓ(ℓ+1)/R² (golden §17; golden2 §4.7–4.8, where the transition is now continuous and the 6D middle row is gone).
    *Reason:* sibling source of the physres5 dimensional interpolation.
    *Bears on:* App-E.

11. **Higher-rank generalization.** x² + C₂(R) x − C₂(R) = 0 for any compact group, with state density (1 − M²/μ²)^(−r/2) near saturation for rank r; SU(3) gives M₊/μ = 0.876, 0.946, 0.949 for C₂ = 4/3, 3, 10/3 (golden §58; golden2 §17).
    *Reason:* shows what changes if the Casimir labels come from a group other than SU(2).
    *Bears on:* A3.

## 5. Negative results and criticisms worth keeping

1. **Single-field Kaluza–Klein fails.** On S² with the linear back-reaction 1/R² = (1 − M²/μ²)/R₀², the relation becomes x(1 + J) = J (golden2 §5.1, as patched after referee #2).
   At J = 2 this gives 2/3 against 0.732, and the pair (3/4, 2) then gives sin²θ = 5/14 = 0.357. Reaching x² + Jx − J = 0 needs 1/R² ∝ (1 − x)/x, which is singular as x → 0. *Bears on:* A1, D-kernel.

2. **Spinor harmonics give J + ¼.** The Dirac operator on a round S² of radius R has eigenvalues ±(k + 1)/R, so a spin-j mode has mass² (j + ½)²/R² = [j(j+1) + ¼]/R², and the j = ½ level sits at 1/R² where J_W = 3/4 is required.
   golden2 §5.3 and App. C use (ℓ + ½)(ℓ + 3/2)/R², which equals j(j+1)/R² and misstates the spectrum; they also read the j = ½ root as a gravitino, which conflicts with the W assignment of §14.
   A Kaluza–Klein route to J_W through spinor harmonics needs a −¼ curvature term. *Bears on:* D-kernel, A3.

3. **golden2's two-field Lagrangian fails.** Eq. (12.1) has the degenerate kinetic matrix [[1, 1], [1, 1]]; its mass condition is J²(J² − 2M²) = 0, a single root M² = J²/2.
   Two canonically normalized fields with the physres5 mass matrix Q(J) give x² + Jx − J = 0, so the correct two-field realization is A1 itself. *Bears on:* A1.

4. **Spectral-triple line.** golden2 §15.2 writes D_F²(D_F² + λΛ²) = λΛ⁴ without a derivation (referee #2), and the saddle estimate of §15.3 gives μ/v = 0.3315 against √3/4 = 0.4330, a 30.6% gap.
   §15.1 also attributes both Casimirs to the ℍ summand. In the spectral Standard Model the doublet value belongs to the Higgs, a fluctuation of the finite Dirac operator between ℂ and ℍ, and the adjoint value belongs to the SU(2) gauge field, a fluctuation of the spacetime Dirac operator; this pairing matches the physres5 A3 split into order parameter and current (curator remark). *Bears on:* D-kernel, A3.

5. **Shared ansatz.** Three of the four "converging" readings (Kaluza–Klein, Connes, AdS/CFT) rest on the same back-reacting-radius ansatz; golden2 §15.6 concedes that the convergence comes from that shared input.

6. **Myers radius.** At fixed flux the dielectric radius grows as √(N² − 1), and published fuzzy-sphere matrix-model spectra give SU(2) harmonic towers without the paired roots u± (golden2 §16.3; referee #2 cites hep-th/0110172 and hep-th/0306270). *Bears on:* D-kernel, D-Regge.

7. **Loop estimates for the residuals.** golden2 eq. (14.13) evaluates to 1.0054 where the text prints 1.003, and since μ < m_H the stated direction "bare above IR" is reversed.
   Eq. (14.14) gives δm_H² = +38.6 GeV² = +0.25% of m_H², where the text prints −2.5%. The one-loop story for the negative-branch residuals is therefore unsupported. *Bears on:* D-partner, D-pole.

8. **Referee #1 (GPT-5.5, REJECT).** The paper parametrizes selected numbers; v/2 and v/√2 are VEV-derived scales while the measured m_H and m_t are not roots; μ = v√3/4 is empirical and differs by 3.6×10⁻⁴ from the M_Z normalization used in the same section; eq. (14.6) mixes pole inputs with running-coupling language; the §16 admission of non-Regge scaling undercuts §§6–10.
   Falsifiers proposed: absence of a 96.54 GeV spin state and of the 99–107 GeV thicket, an elementary state in 107–122 GeV, or a controlled spectral or brane calculation that confirms the 30.6% gap.
   Directions proposed: a look-elsewhere analysis of the de Vries coincidence, a derivation or no-go from a finite spectral triple, an LHC/LEP reinterpretation of the 96–107 GeV and 228 GeV states.

9. **Referee #2 (GPT-5.5, "Mathematical interest: LOW").** New content is limited to the quartic packaging, the four-scale identification and the geometric-mean proposal. The de Vries ratio, Koide-type numerology, Connes–Chamseddine, the grand-symmetry and σ-field repairs (arXiv:1304.0415, 1409.2471), Witten's dimension count and Myers branes are prior work.
   Witten's bound concerns the minimal dimension that hosts an isometry group and supports no energy-dependent dimension; the fuzzy-sphere reading is a retrofit.

10. **The 96.5 GeV state.** The j = 3/2 root sits 1.2% from the 95.4 GeV diphoton excess, 30 times looser than the matches of the core relation; the weak project reached the same number independently and demoted it.

## 6. Open threads

### 6.1 Known errors (status at the last content commits)

Numerical and dimensional errors:

| Location | Printed | Correct value or issue | Status |
|---|---|---|---|
| golden2 (14.13) | ratio ≈ 1.003, "0.3% shift in the correct direction (bare > IR)" | 1.0054 with the stated inputs; μ < m_H, so the direction statement is reversed | unpatched |
| golden2 (14.14) | δm_H² ≈ −2.5% of m_H² | +38.6 GeV² = +0.25% (y_t = 0.992, m_t = 172.7 GeV, μ = 106.58 GeV) | unpatched |
| golden2 (14.7) | boxed M₊\|M₋\| = μ²√J | boxed form fixed in `faf9e0c`; the sentence after it still says μ√(j(j+1)), and the line before (14.10) still reads "M₊(1)·\|M₋(1)\| = M*√2 = v√6/4" (correct: μ²√2 = 3√2 v²/16) | partly patched |
| golden2 (10.2) | Σ_{s=2}^{j} (2s − 1) = j² − 1 | arithmetic correct since `faf9e0c`; the sum starts at s = 2 although W and Z are massive, and the count has no stated role | arithmetic fixed, meaning open |
| golden2 §13.8 | ΔT ≈ 4×10⁻⁴ and FCNC bounds for M* ≳ 1 TeV | §14 sets M* = 106.6 GeV, where the same formula gives ΔT ≈ 0.034 g*² | unpatched |
| golden §6, §34, §55, §69 | x_{3/2} ≈ ±0.9062 | 0.9058; the GeV value 96.524 uses the correct root | unpatched |

Derivation and algebra errors:

| Location | Printed | Correct value or issue | Status |
|---|---|---|---|
| golden2 §5.1–5.2 | x²(1 + λ) = λ | correct since `faf9e0c` | fixed |
| golden2 §5.3, App. C | fermion KK mass² (ℓ + ½)(ℓ + 3/2)/R²; j = ½ root read as a gravitino | Dirac spectrum on S² gives (j + ½)²/R²; the gravitino reading conflicts with §14 | unpatched |
| golden2 §5.7 | static-radion derivation of (★) | the displayed steps do not produce (★); the section labels itself ansatz-level | unpatched |
| golden2 §8.8, §11.2, §12, §15.5, §16.6 | the back-reaction (5.1) yields (★) | contradicts the §5.1 concession | unpatched |
| golden2 (12.1) | two-field Lagrangian yields u± | yields only M² = J²/2 | unpatched |
| golden2 (2.8) | J = t², x = t/√(1 + t²) parametrizes the curve | on that x the curve needs J = t²/√(1 + t²) | unpatched |
| golden2 (2.9), §8.4 | "hidden self-duality" of the curve | the map sends every curve point to J = 1 | unpatched |
| golden2 (2.12) | resolvent cubic (y − J²)(y² + 4) | (y − J²)(y² + 4J²) | unpatched |
| golden2 §2.7 | fixed points of u → u²/(1 − u) are φ-related | fixed points are 0 and ½ | unpatched |

### 6.2 Open calculations

1. Derive the relation from one concrete model and apply the coefficient test 2B = 3A, C = 3A: a 6D Einstein–Maxwell reduction on M₄ × S² in Einstein frame, or the fixed-J Legendre transform of a DBI + Wess–Zumino brane action (golden §68; golden OPUS_IDEAS #1).

2. Compute the custodial Higgs loop with the W/Z bracket held at 1 (golden §63; golden OPUS_IDEAS #3), using the rank-1 structure found in weak/PAPER.tex §4.2.

3. Look-elsewhere statistics for the de Vries ratio alone and for the four-scale identification (referee #1; golden2 OPUS_IDEAS #2). physres5 OPUS_IDEAS #1 proposes the same scan over (J_W, J_Z).

4. Close or refute the 30.6% spectral-action gap with the σ-field flow of arXiv:1409.2471 and the grand-symmetry coefficient of arXiv:1304.0415 (golden2 OPUS_IDEAS #3).

5. Decide whether the j ≥ 3/2 states (96.5–106.6 GeV thicket, 227.8 GeV) exist or are projected out; D-Regge requires an answer for any route that invokes a tower.

6. A script that regenerates every number in either paper; neither repository contains code, and golden2 App. E describes mpmath computations that were never committed (both OPUS_IDEAS files).

The OPUS_IDEAS.md files (Fable subagent proposals dated 2026-07-01) are summarized in items 1–4 and 6 and were left uncopied.

## 7. Manifest

Files copied verbatim from the HEAD of each source repository:

| Path in `family/golden/` | Source | Bytes | Role |
|---|---|---|---|
| `golden2/quartic_strings_kk.md` | `/home/codexssh/golden2/quartic_strings_kk.md` | 135 645 | canonical source |
| `golden2/quartic_strings_kk.pdf` | `/home/codexssh/golden2/quartic_strings_kk.pdf` | 294 667 | canonical PDF, 40 pp |
| `golden2/tikz-header.tex` | `/home/codexssh/golden2/tikz-header.tex` | 601 | LaTeX header for the pandoc + xelatex build (commit `abc1930`) |
| `golden/quantized_quartic_superstrings_kaluza_klein.tex` | `/home/codexssh/golden/quantized_quartic_superstrings_kaluza_klein.tex` | 122 387 | companion source |
| `SUMMARY.md` | written during curation | — | this file |

The companion PDF (50 pp, 404 127 bytes) was dropped during de-duplication; rebuild it from the .tex or read it in the source repository.

Left uncopied: `golden2/conversation.txt` and `golden/conversation_user_inputs.txt` (raw prompt logs, summarized in §1 and §5);
`golden2/quartic_slide.jpg` and `golden/quartic_gate_social_slide.{jpg,svg}` (promotional slides); both `OPUS_IDEAS.md` files (summarized in §6.2);
the LaTeX build files `.aux`, `.log`, `.out`; `.gitignore` and `.gitattributes`. Neither repository contains scripts.

