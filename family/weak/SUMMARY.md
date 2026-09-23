# weak: Casimir-locked seesaw for the electroweak bosons

Curated for physres5 on 2026-09-23. The source repository was read and left unchanged.
Numbers were recomputed during curation with M_Z = 91.1876 GeV, M_W = 80.3692 GeV, m_H = 125.20 GeV, v = 246.21965 GeV (from G_F) and m_t = 172.7 GeV.
The 17 copied scripts were run from a scratch copy on 2026-09-23 and all exit with code 0. seeds.py carries 12 assertions; most others print results and end with one exit status; L_gauge.py, L_scalar.py and recast_91GeV.py contain no check.

**physres5 hooks.** A1: the Casimir matrix Q(J) = μ²[[0, √J], [√J, −J]]. A2: pole placement. A3: ordered assignment (J_W, J_Z) = (3/4, 2).
Appendix D targets: D-pole (pole placement and Δ_match), D-assign (electroweak assignment and ray admissibility),
D-kernel (local route kernel: light subspace, inner product ⟨·,·⟩_J, normalization Λ_J, entry conditions Σ_hh = 0, Σ_aa = J, Σ_ha Σ_ah = J, pole map),
D-partner (negative branch, scalar functional F_sc, α endpoint), D-branch, D-Regge and D-SUSYQM (the three additional filters).

**Notation map.** weak writes M_R² = m₀²[[0, √C₂(R)], [√C₂(R), −C₂(R)]] with C₂(2) = 3/4 (doublet), C₂(3) = 2 (triplet) and eigenvalues λ±(R).
This is Q(J) with μ = m₀, J = C₂(R) and λ± = x±(J). The golden papers call the same scale M∞ or M*.

## 1. Provenance

- Source: `/home/codexssh/weak`, git, 34 commits. Content commits run 2026-05-16 04:53 → 14:41 (last content commit `5823d99`); `9a9e025` (2026-09-23) committed the agent notes, criticism files, chat transcripts, UFO model, reference PDFs, validation scripts and OPUS_IDEAS.md.
- Origin: a chat titled "BSM alternatives to SU(2)×U(1)" (16 May 2026, 03:57), kept as the "cosas alex" .html export and its .md transcription (raw transcripts, left uncopied). SEED.md (04:12) fixes the seed: doublet and triplet blocks, m₀ ≈ 106.58 GeV, a spurion Δ ≈ 700 GeV², and a list of items still underived.
- Two agent lines worked in the repository that day. A Claude pipeline (acknowledgements cite Claude Opus 4.7) produced PHASE_1–5.md, VERIFICATION.md, PAPER.md/PAPER.tex, the `model/` tree (SymPy scripts, FeynRules file, hand-built UFO, MadGraph cards), `model/paper/main.tex`, LAGRANGIAN.md and LAGRANGIAN_PC.md. A Codex line (acknowledgements cite OpenAI ChatGPT/Codex) produced codexModel.tex, epjc.tex, epjc.txt and `model/algebra/codex_model_check.py`. criticism.md reviews an early `main.tex`; criticism2.md reviews the Koide-era PAPER.md; ADVERSARIAL.md is the pipeline's own red-team note. The two criticism files carry no reviewer name.
- Relation to physres5: the seed is A1 with the A3 assignment. weak sets λ₊(2)m₀² = M_W², λ₊(3)m₀² = M_Z², |λ₋(2)|m₀² = m²_{h,bare}, and in main.tex |λ₋(3)|m₀² − Δ = v²/2. physres5 reads the same objects as a kinematical pole-spectrum statement; weak tries to realize them as a particle model.
- Relation to golden/golden2 (2026-05-26): same matrix in mass variables, same m₀, same j = 3/2 value 96.5 GeV. The eigenvalue |λ₋(2)|^½ m₀ = 122.39 GeV is m_{h,bare} here and v/2 in golden2; golden §63 and weak's rank-1 spurion treat the same 122.4 → 125.2 GeV gap.

## 2. Manuscripts and maturity

| Draft | Pages | Last change | Content |
|---|---|---|---|
| `PAPER.tex` (REVTeX, PRD style; PAPER.md is its Markdown twin) | 6, two-column | 05-16 06:21 | seed and its three structural conditions, ten-pair scan, Fit B, rank-1 spurion, spurion mechanisms, SO(32)/sBootstrap placement, bosonic-seesaw literature, caveats (a)–(h) including the Wigner–Eckart no-go |
| `model/paper/main.tex` ("v4, PRD submission candidate") | 15 | 05-16 14:41 | adds the bidirectional spurion and the negative-branch sum rule, Q1–Q6 status, the 91 GeV scalar recast, the R = 4 channel, an EWPT estimate, the MadGraph check, a partial-compositeness sketch and an LRSM remark |
| `codexModel.tex` | 11 | 05-16 05:56 | a separate conservative model: inert ℤ₂-odd real singlet and Y = 0 triplet with a rank-one Higgs portal; W and Z masses from \|D_μH\|²; a heavy-doublet bosonic see-saw matching; five decision gates |
| `epjc.tex` (with the positioning note `epjc.txt`) | 6 | 05-16 06:13 | the seed as a mass texture, with explicit completion requirements |

**Most mature of the three named manuscripts: PAPER.tex.** After its first draft it was revised in five commits: the Koide sections were excised after criticism2.md, the input/output count and the scan objective were corrected, the text moved to REVTeX, and the Wigner–Eckart no-go entered caveat §6(a). Its caveats (a)–(c) answer the three weak points of ADVERSARIAL.md, its accounting is consistent (M_W anchors m₀, Δ is fitted to m_H, the predictions are M_Z and m_{h,bare}), and it is in journal format with a complete bibliography and an AI disclosure.
codexModel.tex is careful about gauge invariance and removes the de Vries relation from the gauge sector altogether; epjc.tex is a short positioning draft whose stance (a texture plus completion tests) matches the physres5 stance.

The fourth draft, `model/paper/main.tex`, carries the most results and was edited last, so its source is copied alongside PAPER.tex (its 15-page PDF was dropped during de-duplication). Its internal inconsistencies are listed in §6.1.

## 3. Goal and final conclusion

**Goal.** Replace the free Higgs-potential parameters by representation data: one 2×2 Casimir-locked mass-squared block per SU(2) representation (doublet and triplet) with a shared scale; read the eigenvalues as M_W², M_Z², the bare Higgs mass² and (in main.tex) v²/2; then find a Lagrangian origin, a mechanism for the Higgs shift, and collider tests.

**Conclusion stated by the authors.** A "numerically suggestive ansatz". Its genuine outputs are M_Z from M_W (−6.8×10⁻⁵, the de Vries quotient) and m_{h,bare} = 122.38 GeV. Δ = (26.42 GeV)² is fitted to m_H. The √C₂ entry and b = 1 remain postulates, the Wigner–Eckart route is excluded, the triplet half of the bidirectional spurion has no mechanism, and the step from scalar eigenvalues to vector masses lacks a derivation.

**Curator's conclusion.** For physres5 this is the most direct test bed of A1 and A3 as a particle model. Its lasting results are the list of failed field-theory routes to the entry condition Σ_ha Σ_ah = J, the reformulation that moves J into the channel metric, the rank-1 structure of any scalar-side shift, and the negative-branch sum rule as an F_sc candidate.

## 4. Valuable ideas and results

1. **A1 with conventions and postulates separated.** Three structural conditions fix the texture: det < 0; a trace polynomial in C₂ without constant term; a protected zero in the (1,1) slot. The off-diagonal coefficient a is absorbed into m₀ by the kinetic normalization of the protected field, b = 1 is a postulate, and the m_H match needs a/b = 1 to 6×10⁻⁴ (PHASE_1 §2; PAPER.tex §2; main.tex §3; robustness.py).
   *Reason:* an explicit accounting of which parts of A1 are convention and which carry content.
   *Bears on:* A1, D-kernel.

2. **No-go list for the off-diagonal √C₂.** Σ_hh = 0 follows from a ℤ₂ or chiral protection and Σ_aa = J from Φ†T^aT^aΦ. Σ_ha Σ_ah = J has no single-operator renormalizable origin.
   An adjoint-spurion contraction saturates at j² < j(j+1) (ratio √(j/(j+1)) = 0.577 for the doublet, 0.707 for the triplet); a Hosotani Wilson line gives weight²; loops and heavy-field lifts give C₂.
   The singlet–doublet matrix element of any SU(2) generator vanishes because 1 ⊗ ½ contains no singlet; the axial generator of the SO(4) bidoublet gives Σ|⟨1|T_A|3⟩|² = 3 against the required 2, and every (j, j) parent gives 4j(j+1) ≠ 2.
   Only the non-analytic operator S√(Φ†T^aT^aΦ) or a representation-dependent coupling reproduces √C₂ (LAGRANGIAN.md L1–L5; LAGRANGIAN_PC.md; PAPER.tex §6(a)).
   *Reason:* closes the natural field-theory routes to the physres5 entry condition and points to first-order operators whose square gives the block, the D-SUSYQM route.
   *Bears on:* D-kernel, D-SUSYQM, A1.

3. **The Casimir can live in the channel metric.** Writing the second field as φ = φ̃/√J (its kinetic term then carries 1/J) turns the seed into the J-independent golden-ratio matrix G = μ²[[0, 1], [1, −1]] with channel metric K = diag(1, 1/J); det(G − xK) = 0 is x² + Jx − J = 0 (LAGRANGIAN.md §3; LAGRANGIAN_PC.md §4 item 3 writes the rescaled matrix as C₂·[[0, 1], [1, −1]], which is incorrect; the congruence was verified during curation).
   *Reason:* the entry conditions Σ_aa = J and Σ_ha Σ_ah = J collapse into one statement, ⟨a_J, a_J⟩ = 1/J for the current channel, which is the inner product ⟨·,·⟩_J of the physres5 source package; a boundary or interval route can supply it as a J-dependent mode normalization.
   *Bears on:* D-kernel (inner product and Λ_J), A1.

4. **Representation scan.** Among the ten SU(2) pairs with C₂ < 12, {2, 3} wins by a factor ≈ 300 in maximum fractional error; the next pair (2, 4) misses M_Z by 5.9%.
   The custodial decomposition (2, 2) = 1 ⊕ 3 selects {1, 3} and fails (the singlet block is identically zero); a two-mode 5D SU(2) KK truncation selects {3, 3} and fails (no doublet slot) (PHASE_2; PAPER.tex §3.2).
   Caveat: the m_{h,bare} target is the doublet's own negative root, so for every {2, n} pair the discriminating number is M_Z/M_W alone; the texture is held fixed and no trials factor is computed.
   *Reason:* a first look-elsewhere table for A3 and two rejected selection rules.
   *Bears on:* A3, D-assign.

5. **Rank-1 structure of the scalar-side shift.** Lifting the doublet negative root to m_H with M_W fixed requires δM² = −Δ P₋, with P₋ the projector on the tachyonic eigenvector; for J = 3/4, P₋ = [[½ − √57/38, −2√19/19], [−2√19/19, ½ + √57/38]].
   A trace-preserving shift moves M_W to 84.60 GeV and a determinant-preserving one to 78.47 GeV; Δ = 698 GeV² = (26.42 GeV)² (PHASE_3 §1; PAPER.tex §4.2).
   *Reason:* fixes the algebraic form of any scalar-side Δ_match that leaves the physres5 vector datum untouched; golden §63 states the same lock as a loop condition.
   *Bears on:* D-partner, D-pole.

6. **Negative-branch sum rule.** m_H² + v²/2 = μ²(|x₋(3/4)| + |x₋(2)|) holds to 4.1×10⁻⁴ with μ from M_W and 5.4×10⁻⁴ with μ from M_Z (19–25 GeV² out of 45 987 GeV²) (main.tex §7).
   Since x₋ = −J − x₊, it is a trace identity over both blocks: M_W² + M_Z² − m_H² − v²/2 = Tr[Q(3/4) + Q(2)] = −(11/4)μ².
   Equivalently, the doublet shift m_H² − |x₋(3/4)|μ² and the triplet shift |x₋(2)|μ² − v²/2 agree to 3–4%, both ≈ (26.6 GeV)².
   Caveat: the combination was chosen after inspection, and the triplet half has no mechanism (§5 item 7).
   *Reason:* an F_sc candidate built from two scheme-clean inputs (the Higgs pole and G_F), with precision comparable to that of the vector ratio.
   *Bears on:* D-partner, A2.

7. **Fermion no-go.** A common-scale Casimir seed spans at most x₊(∞)/x₊(3/4) = 1.76 in mass squared, so it cannot host the lepton hierarchy; the negative branch fits the leptons only with SU(2) representations of dimension 4, 884 and 14 867 (PHASE_4 §1).
   *Reason:* supports the physres5 separation of flavour from the electroweak mass-angle problem.
   *Bears on:* physres5 §7 (flavour boundary).

8. **SO(32) placement.** SO(32) ⊃ SO(28) × SO(4) ⊃ SO(28) × SU(2)_diag carries triplets in the adjoint 496 and doublets only in the spinor 32 768; the chain accommodates {2, 3} and selects neither the pair nor the removal of singlets (PHASE_5 §Q1; PAPER.tex §5.1). PHASE_5 also records that arXiv:2407.05397 classifies scalars under a flavour SU(5) and never passes through SU(2)_W.
   *Reason:* the place where the physres5 SO(32)-flavour caveat meets A3.
   *Bears on:* A3, physres5 §7.

9. **Particle content implied by a literal reading of A1.** A Y = 0 triplet scalar degenerate with the Z at 91.19 GeV, gauge-phobic and fermion-phobic, allowed by the LEP HZ′ bound for portal coupling λ_dt < 0.012 (main.tex §11; recast_91GeV.py); an R = 4 channel at 96.54 GeV and 227.85 GeV with a doubly charged member (main.tex §10).
   main.tex §10 and §13 read j as the SU(2)_L isospin of composite scalar channels, by analogy with meson isospin.
   *Reason:* shows what A1 predicts when its eigenvectors are taken as fields; physres5 must state whether the J = 2 positive eigenvector is the Z pole itself (pole map) or a scalar partner.
   *Bears on:* D-pole, D-assign, D-Regge.

10. **Literature map for two-channel scalar matrices.** Calmet–Oliver (hep-ph/0606209), H. D. Kim's SUSY bosonic see-saw (hep-ph/0501059), the Chivukula–Dobrescu–Georgi–Hill top see-saw with the fermionic texture [[0, M], [M, −m]] (hep-ph/9809470), the radiative bosonic see-saw of Haba–Ishida–Okada–Yamaguchi (arXiv:1508.06828) and Caracciolo–Parolini–Serone partial compositeness (arXiv:1211.7290); none ties the entries to √C₂ and −C₂ (LITERATURE.md; PAPER.tex §5.3).
    In the Kim-type block [[0, ε], [ε, +M²]] the light eigenvalue is tachyonic (codexModel.tex §2); in Q(J) the diagonal entry is −J, so the tachyonic eigenvalue is the larger one, |x₋| > x₊.
    *Reason:* ready references for the physres5 source inventory, and a precise statement of how Q(J) differs from the standard bosonic see-saw.
    *Bears on:* A1.

## 5. Negative results and criticisms worth keeping

1. **Scalar eigenvalues identified with gauge-boson masses by postulate** (criticism.md #1). With the paper's own Lagrangian, M_W = gv/2 comes from |D_μH|² with free g and g′; the triplet eigenvalue has no route to the Z mass, and a triplet VEV large enough to matter would break ρ = 1. codexModel.tex abandons the identification for this reason. *Bears on:* D-pole, D-assign: physres5 must supply the map from a kernel eigenvalue to a vector pole on the admissible vacuum ray.

2. **Higgs formula inserted after the Lagrangian** with free quartics (criticism.md #2). The later Q2 computation shows m²_{h,bare} = m₀²|λ₋(2)| at tree level in canonical normalization and needs λ_h^eff = 0.247 for the observed v, four times the composite-Higgs estimate 0.06 (main.tex §12, Q2). *Bears on:* D-partner.

3. **Counting and circularity** (criticism.md #3, criticism2.md #2, ADVERSARIAL #2–3): M_W is an anchor, Δ is fitted, and an early draft claimed ten-digit agreement for sin²θ_W. The Standard Model already predicts M_W from (M_Z, G_F, α) at the sub-permille level through Δr.

4. **Scheme** (EW_corrections.py; model/RESULTS.md Phase B): 0.22310 matches the on-shell definition at about 1σ and misses MS-bar (0.23121) and sin²θ_eff (0.23153) by 3.5%; Δr ≈ 4% enters through the M_W anchor. The physres5 pole target 0.2231768 ± 0.0002608 lies 0.29σ from the de Vries value. *Bears on:* D-pole.

5. **Fine tuning** (ADVERSARIAL #1; robustness.py): a (1,1) entry of 0.05 m₀² or a 2% change of the off-diagonal breaks the fit, and a/b = 1 must hold to 6×10⁻⁴. *Bears on:* A1.

6. **Top-loop mechanism for Δ** (PAPER.tex §4.3): the hard cutoff Λ = m₀ = 106.6 GeV lies below m_t = 172.7 GeV. (3y_t²/8π²)(m_t² − m₀²) = 690 GeV² = 0.99 Δ, while the log piece gives 1077 GeV² = 1.54 Δ. A quadratic top-loop term cut off below the top mass has no standard meaning, so the 1% agreement is best treated as a coincidence (the paper calls it regulator-dependent). *Bears on:* D-partner.

7. **Triplet half of the bidirectional spurion** (main.tex §7; Q6_triplet_gauge_CW.py): the one-loop gauge contribution (3g²/16π²)C₂(3)m₀²/4 = (6.78 GeV)² is 15.6 times short of the required (26.8 GeV)². *Bears on:* D-partner.

8. **The MadGraph check tests nothing new:** the UFO is the Standard Model with m_H = 125.30 GeV and no new vertices, so SM-like diboson rates are guaranteed (criticism.md #4; main.tex §8). MG5_debug records a failed UFO import from a /tmp path; the three LO runs in `model/madgraph/runs/` exist. The S, T, U numbers use a leading-log ΔS.

9. **LRSM remark** (main.tex §14; LRSM_extension_mock.py): M(W_R)/M(Z_R) = 0.881 follows only from reusing the eigenvalue identification. With the script's own couplings (g_R = 0.653, g_BL = 0.413) the standard LRSM gauge-mass formulas give 0.60 for triplet breaking and 0.85 for doublet breaking, and triplet breaking bounds the ratio by 1/√2. *Bears on:* A3.

10. **Lepton and quark extensions withdrawn** (criticism2.md #1, #4, #5; PHASE_4–5): the ℤ₃ circulant imposed Koide and used the full lepton spectrum for its centre; the (s, c, b) exactness relied on curated masses; the ℤ₃ permutation symmetry was misidentified with the centre of SU(3).

## 6. Open threads

### 6.1 Known errors and inconsistencies

| Location | Issue |
|---|---|
| `model/paper/main.tex` abstract vs §6 | m₀ is anchored on M_W in the abstract (106.57 GeV) and on M_Z in §6 (106.578 GeV) |
| `main.tex` §6 and §12 (Q3) vs §13 | 0.22310 is compared with an on-shell value 0.22290(28) that matches no stated input (the PDG 2024 masses give 0.22320), and §13 quotes 0.09% agreement |
| `main.tex` §7 vs §12 (Q6) | v/√2 is called a model output, later "matched but not strictly derived" |
| `main.tex` §14 | LRSM ratio 0.881 conflicts with the LRSM gauge-mass formulas (§5 item 9) |
| `model/lagrangian/Q6_triplet_gauge_CW.py`, final block [8] | the summary says the triplet gauge loop matches the top shift and quotes (10–20 GeV)²; its own step [4] gives (6.78 GeV)², 15.6 times short; main.tex uses the step [4] number |
| `LAGRANGIAN_PC.md` §4 item 3 | rescaled matrix written as m₀²C₂[[0, 1], [1, −1]]; the correct form is m₀²[[0, 1], [1, −1]] with kinetic weight 1/C₂ on the second field (or m₀²[[0, C₂], [C₂, −C₂²]] with weight C₂) |
| `PAPER.tex` bibliography | the arXiv:1508.06828 entry carries the title "Gauge coupling unification in a classically scale invariant model" and lists R. Takahashi; `refs/refs.bib` and LITERATURE.md give the correct entry (Haba, Ishida, Okada, Yamaguchi, "Bosonic seesaw mechanism in a classically conformal extension of the Standard Model", PLB 754 (2016) 349) |
| `SEED.md` | still calls Δ "trace-preserving" and writes f² = f₀² − Δ with f = v/√2; PHASE_3 §1 shows both are inconsistent with Δ ≈ +700 GeV² (SEED.md is marked do-not-overwrite) |
| `VERIFICATION.md` §2 | "2 parameters match 4 independent observables", the overcount that criticism2.md #2 flagged and PAPER.tex corrected |

### 6.2 Open calculations

1. Derive Σ_ha Σ_ah = J from a first-order operator whose square gives the block, or from a J-dependent channel norm (§4 item 3), using the failed routes of §4 item 2 as the checklist.

2. A mechanism for the triplet half of the spurion, or a decision to drop the sum rule.

3. A pole map from the J = 2 eigenvalue to the Z pole without a triplet VEV. The five decision gates of codexModel.tex (Fermi scale, alignment, precision, dark sector, implementation) are a usable acceptance template.

4. Look-elsewhere statistics for A3 with the texture varied (weak OPUS_IDEAS #1; physres5 OPUS_IDEAS #1).

5. Convert the print-style scripts into asserting tests, and repair the MG5/UFO pipeline once new fields enter the model (weak OPUS_IDEAS #2).

6. weak OPUS_IDEAS #3 proposes promoting the LRSM ratio to a paper-grade prediction; the check in §5 item 9 shows it fails as stated.

## 7. Manifest

Copied verbatim from the source HEAD. The source layout is preserved so that relative references resolve (`model/paper/main.tex` reads `../../refs/refs.bib`; the scripts import each other through `model/`).

Manuscripts and notes:

| Path in `family/weak/` | Bytes | Role |
|---|---|---|
| `PAPER.tex` | 36 359 | most mature of the three named manuscripts |
| `PAPER.pdf` | 338 366 | its PDF, 6 pp |
| `model/paper/main.tex` | 52 258 | PRD v4 draft (fourth manuscript) |
| `refs/refs.bib` | 9 475 | bibliography used by main.tex |
| `criticism.md` | 7 267 | review of main.tex v2 |
| `criticism2.md` | 5 228 | review of the Koide-era PAPER.md |
| `ADVERSARIAL.md` | 3 911 | red-team note |
| `LAGRANGIAN.md` | 26 363 | Lagrangian attempts L1–L5 |
| `LAGRANGIAN_PC.md` | 14 030 | Wigner–Eckart computation |
| `SEED.md` | 1 550 | original seed statement |
| `PHASE_1.md` … `PHASE_5.md` | 13 211; 14 420; 16 610; 20 543; 22 762 | pipeline phases: seed algebra, representation selection, spurion, fermion extension, corpus |
| `VERIFICATION.md` | 13 989 | numerical cross-check |
| `LITERATURE.md` | 11 548 | INSPIRE literature survey |
| `model/RESULTS.md` | 4 886 | Phase A–D synthesis |
| `SUMMARY.md` | — | this file |

Scripts and model file:

| Path in `family/weak/` | Bytes | Role |
|---|---|---|
| `model/algebra/`: seeds.py, ewsb_check.py, robustness.py, EW_corrections.py, derived_couplings.py, spin_three_half.py | 8 244; 4 208; 7 237; 6 060; 7 107; 5 029 | seed algebra and checks |
| `model/lagrangian/`: L_gauge.py, L_scalar.py, L_doublet_minimisation.py, L_SO5_SO4_composite.py, Q1_full_chain.py, Q2_potential_minimisation.py, Q6_triplet_gauge_CW.py, L_PC_sketch.py, LRSM_extension_mock.py | 5 516; 5 654; 8 459; 10 949; 8 817; 9 638; 10 479; 9 107; 11 215 | Lagrangian-level Q1–Q6 and extensions |
| `model/phenomenology/recast_91GeV.py` | 9 054 | LEP/LHC recast of the 91 GeV scalar |
| `model/ewpt/STU.py` | 8 576 | oblique-parameter estimate |
| `model/feynrules/casimir_seesaw.fr` | 10 068 | FeynRules model file |

Left uncopied: the "cosas alex" .html/.md chat transcripts and their tooling (transcribe_chat_html.py, validate.py, validate_transcription.py); `refs/*.pdf` (third-party papers); `model/madgraph/runs/` and the MadGraph cards; `model/ufo/` (the SM UFO with one mass changed); `model/py.py` and `model/paper/py.py` (generated parser tables); MG5_debug; LaTeX build files; codexModel.tex/.pdf, epjc.tex/.pdf/.txt and `model/algebra/codex_model_check.py` (summarized in §2); PAPER.md (Markdown twin of PAPER.tex); PAPERNotes.bib (REVTeX control stub); OPUS_IDEAS.md (summarized in §6.2); AGENTS.md; `model/run_all.sh` (calls the excluded MG5/UFO stages).

