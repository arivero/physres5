# signed-dv family: signed de Broglie–de Vries roots and the κ = 3/8 correction

Curated on 2026-09-23 for physres5 from two sibling projects. Both projects
read the negative roots of the physres5 secular equation x² + Jx − J = 0 at
J = 3/4 and J = 2 as Higgs-sector mass slots. They also test a proposed
correction ΔM₋² = κ(M_Z² − M_W²)σ₃ with κ = C_F/C_A = 3/8. Statements
attributed to a project quote that project. Items marked **[C#]** are curator
checks. Neither source project contains them; `curator_checks.py` in this
folder reproduces them, and its section numbers match the tags.

Tags for physres5 targets: **A1** the 2×2 matrix Q(J); **A2** pole placement;
**A3** the ordered assignment (J_W, J_Z) = (3/4, 2). The five subsections of
`manuscript/sections/D_theorem_targets.tex` are **D-pole** (pole placement),
**D-assign/ray** (electroweak assignment and ray admissibility), **D-kernel**
(local route kernel), **D-partner/α** (partner branch and scalar data, with
the α endpoint), and **D-filters** (branch scaling, Regge survival, SUSY-QM
origin).

## 1. Provenance

| | hans | signed-dv |
|---|---|---|
| Source | `/home/codexssh/hans`, work in `signed_dbdevries/` | `/home/codexssh/signed-dv-custodial-project` |
| Git | `master`, 19 commits, head `faf607f`, clean tree | `main`, 42 commits, head `e090bfc`, clean tree |
| Research window | 2026-05-14 01:59–02:37 CEST, 18 commits, cycles 0–16 | 2026-05-14 02:04–03:41 CEST, 41 commits, 24 cycles, 7 critic passes |
| Last commit | 2026-09-23, adds `OPUS_IDEAS.md` | 2026-09-23, adds `OPUS_IDEAS.md` |
| Main output | conditional no-go and mechanism scorecard; PRD-style note `draft/main.tex` | EPJ Plus manuscript `draft/fused_manuscript.tex` (16 pp.) with a GO verdict |

Both runs started from the same autonomous-agent prompt: signed-dv's
`prompt.md` and hans's `project_prompt.md` are byte-identical. They ran the
same night, and hans started five minutes earlier. Work moved in both
directions:

- hans cycle 0 (`b539b87`) archived signed-dv's first artifacts under
  `signed_dbdevries/sister_project_import/`. In cycles 15–16 hans imported
  signed-dv's look-elsewhere and scheme results and reran `look_elsewhere.py`,
  reproducing p = 1.564×10⁻⁶.
- signed-dv cycle 7 imported hans's paired exotic D-term, minimal
  negative-sector EFT, conditional no-go, and charge-lattice scans.
- In cycles 15–17 signed-dv merged four of its results into A. Rivero's May
  2026 note "noteOpus": the C_F/C_A rewriting with its closed form, the
  look-elsewhere statistic, the D-term with the charge no-go, and the SMEFT
  map. noteOpus supplies the Poincaré-Casimir quartic, the (−1)^F spurion and
  the higher-spin tower. The merged `draft/fused_manuscript.tex` lists A. Rivero
  as sole author and acknowledges Claude Opus 4.7.

hans holds the mechanism and no-go side. signed-dv holds the statistics, the
scheme analysis and the merged manuscript. The construction goes back to
H. de Vries (Physics Forums post, November 2004) and A. Rivero,
arXiv:hep-ph/0606171 (2006).

Relation to physres5: both projects use the same roots x±(J). physres5 uses
x₊(3/4)/x₊(2) for the W/Z pole quotient. This family keeps that quotient and
reads the partner roots as |x₋(3/4)| ↔ m_H² and |x₋(2)| ↔ v²/2 = (2√2 G_F)⁻¹,
in units μ² = M_Z²/x₊(2).

## 2. Goal and final conclusion

**Goal.** The projects asked whether ΔM₋² = (C_F/C_A)(M_Z² − M_W²)σ₃ follows
from a mainstream framework, with SU(2) Casimirs C_F = 3/4 and C_A = 2. The
candidates were custodial SU(2)_L × SU(2)_R EFT, composite Higgs, quiver or
deconstructed models, SUSY D-terms, gauge Reggeization, and D-brane UV
completions.

**Spectrum.** Masses in GeV, with the projects' anchor M_Z = 91.1876 GeV:

| slot | root | read as | uncorrected | with κ = 3/8 | data |
|---|---|---|---|---|---|
| (1,+) | x₊(2) = √3 − 1 | M_Z | 91.1876 (input) | — | 91.1876 |
| (½,+) | x₊(¾) = (√57 − 3)/8 | M_W | 80.3744 | — | 80.3692 ± 0.0133 (PDG 2024) |
| (½,−) | x₋(¾) = −(√57 + 3)/8 | m_H | 122.389 | 125.199 | 125.20 ± 0.11 (PDG 2024); 125.13 ± 0.11 (PDG-Live 2026) |
| (1,−) | x₋(2) = −(√3 + 1) | v/√2 | 176.161 | 174.175 | 174.1036 (from G_F) |

The correction shifts |M²| of the two partner slots by ±κ(M_Z² − M_W²) and
preserves their sum. The corrected slots have exact closed forms:
m_H²/M_Z² = (15√19 + 33√3 + 5√57 + 81)/128 = 1.885081 and
(v/√2)²/M_Z² = (3√57 + 9√19 + 199 + 119√3)/128 = 3.648388.

**Final conclusion.**

1. **κ = 3/8 is a phenomenological ansatz that has not been derived.**
   Custodial symmetry supplies the spurion M_Z² − M_W² = g′²v²/4 and allows
   κ(M_Z² − M_W²)σ₃ on an assumed two-state negative sector. Every surveyed
   framework leaves κ free. Every explicit realization inserts 3/8 by hand:
   the Wilson coefficient c_Y = 3/16 in ½Ψ₋ᵀ[c_Y g′²(H†H)σ₃]Ψ₋, the exotic
   hypercharge q_S = 3/8 in a paired D-term, or a continuous kinetic-mixing
   parameter. hans's verdict is "symmetry-motivated but not derived".
   signed-dv's verdict is "phenomenological only — an algebraic identity
   supported by a one-parameter post-diction".
2. **Empirical content.** The fit gives two post-dictions (M_W from M_Z, and
   m_H with κ) and one mismatch: M_F exceeds v/√2 by 4×10⁻⁴ in mass, or
   25 GeV² in mass squared. The inputs are one anchor and one ratio. The Higgs
   slot alone wants κ_H = 0.3751 (PDG 2024) or 0.3656 (PDG-Live 2026), each
   ±0.015 from δm_H. The v slot wants κ_F = 0.3884. With the projects' anchor
   a single κ cannot fit both slots.
3. **Look-elsewhere p-value.** The manuscript's headline is p_LEE ≲ 10⁻⁴
   (an "agnostic radical pool"), with a Bayes factor of 10⁴–10⁵. The script
   `algebra/look_elsewhere.py` scans (a√p + b√q + c√r + d)/D with integer
   coefficients in [−50, 50]:
   - Family B (any radical triple from {1,2,3,5,7,11,13,17,19,57},
     D ∈ {64,128,256}): 107,443/6.87×10¹⁰ = 1.56×10⁻⁶.
   - Family A (the dV radicals, D = 128): 2.76×10⁻⁶.
   - The script's Bayes factor is 6.4×10⁵.

   The curator recount **[C9]** reproduces these numbers and finds three
   problems:
   - The scan window (10⁻⁵ absolute on m_H²/M_Z²) is narrower than the dV
     formula's own residual of 3.1×10⁻⁵, so the formula under test fails the
     scan's criterion.
   - A window equal to the 1σ uncertainty of m_H²/M_Z² (3.3×10⁻³, from
     δm_H = 0.11 GeV) gives 5.3×10⁻⁴ for Family B and 9.1×10⁻⁴ for Family A.
     The Bayes factor then drops to about 1.9×10³.
   - No script computes the ≲10⁻⁴ figure. Neither figure includes a trials
     factor for the choice of κ, the slot map, or the target.
4. **Manuscript status.** Critic 7 (cycle 22) issued GO for EPJ Plus; the
   source file is `critique/cycle22_final_pass.md`. `FINAL_STATE.md` records
   `run_checks.sh` exiting 0 in 43.8 s and a clean two-pass pdflatex build:
   16 pages, all 34 citation keys resolved. The curator reran the copies in
   this folder from a scratch mirror. `run_checks.sh` exits 0 in 43.6 s,
   `hans-extras/algebra/run_all_checks.py` reports 14/14 PASS, and
   `draft/fused_manuscript.tex` compiles to 16 pages with no warnings.
5. **FCC-ee inconsistency.** The source `README.md` says ~8σ.
   `EXECUTIVE_SUMMARY.md` says ~12σ and names the ATLAS central value
   80.3665 GeV as its reference. The manuscript conclusion (§13) says ~10σ.
   Checks **[C4]** show which reference each figure fits:
   - Against ATLAS 80.3665 GeV the dV M_W sits 7.9 MeV high: 7.9σ at
     δM_W = 1 MeV.
   - The 12σ figure fits the PDG-Live 2026 average, 80.3625 GeV (11.9 MeV).
   - The ~10σ figure fits PDG 2024, 80.3692 GeV, at δM_W = 0.5 MeV
     (10.5–11.2σ).

   The three documents use three reference values, and EXECUTIVE_SUMMARY
   pairs its 12σ with the wrong one. All three compare against Breit–Wigner
   masses (item 14 of §5).

## 3. Valuable ideas and results for physres5

Manuscript section numbers refer to `draft/fused_manuscript.tex`.

1. **Partner-slot reading: |x₋(¾)| ↔ m_H² and |x₋(2)| ↔ v²/2.**
   *Targets:* **D-partner/α**, A3. *Source:* manuscript §3 and §9;
   `algebra/scalar_scale_identification.py`.
   This gives App. D's scalar functional F_sc two concrete candidates: the
   Higgs pole mass and the vacuum-ray normalization from G_F. Under A3 the
   doublet label J = ¾ lands on the Higgs boson on the partner branch.
2. **A κ-free sum rule.** By Vieta, (v/√2)² + m_H² = [11/4 + x₊(¾) + x₊(2)] μ²,
   with μ² = M_Z²/x₊(2).
   *Target:* **D-partner/α**. *Source:* manuscript §5, eq. (trace), and App. B.
   This tests the partner-branch reading with no fitted parameter. The unit is
   σ = 2m_Hδm_H = 27.5 GeV². On the Breit–Wigner anchor (M_Z = 91.1879 GeV,
   PDG 2024 m_H) the residual is −25 GeV², or −0.9σ. On physres5's
   complex-pole anchor it is +9 GeV² with the PDG 2024 m_H and −8 GeV² with
   the PDG-Live 2026 m_H, about ±0.3σ **[C7]**.
3. **Vieta and the hidden-coupling factorization.** The signed trace ratio
   and the determinant ratio both equal J_W/J_Z = 3/8. Also
   cos²θ_dV = (J_W/J_Z)·F_dyn, with F_dyn = [√(1+4/J_W) − 1]/[√(1+4/J_Z) − 1]
   **[C1]**.
   *Targets:* A3, **D-assign/ray**. *Source:* `hans-extras/stress_tests.md`
   and the source note `notes/original_hidden_coupling_note.tex`.
   The ratio of the two A3 labels sits inside the pole quotient, and it equals
   the proposed κ. A derivation of A3 fixes 3/8 as J_W/J_Z. Using it as a σ₃
   coefficient remains a separate assumption.
4. **On-shell-subtracted deformation:**
   P_J(x) + λ(x − x₊(J)) = (x − x₊)(x − x₋ + λ).
   *Targets:* **D-partner/α**, A1. *Source:*
   `hans-extras/algebra/deformation_scan.py`.
   The deformation moves the partner root and holds the pole quotient exactly.
   It is the explicit form of physres5's "auxiliary status" option. A
   partner-branch correction therefore costs one parameter and has no effect
   on sin²θ.
5. **Two-state projector.** Every real traceless 2×2 perturbation
   diagonalizes to σ₃.
   *Targets:* **D-kernel**, **D-partner/α**. *Source:*
   `hans-extras/mechanisms/two_state_projector.md`.
   The σ₃ form carries content only after a source fixes the branch basis.
   physres5 requires the same data for u±(J) = α±h_J + β±a_J and its inner
   product.
6. **Custodial-parent obstruction.** The quadratic has no g′ parameter, and
   the W/Z split comes from the J labels. The family x² + Cx − χC degenerates
   only by sending x₊ → 0. A regular parent equation needs an extra C_* and a
   chosen interpolation.
   *Target:* **D-assign/ray**. *Source:* `hans-extras/stress_tests.md`;
   `algebra/explore_deformations.py`.
   This independently supports physres5's single-ray admissibility rule:
   custodial g′ → 0 limits need new structure outside the construction.
7. **Rapidity form.** x₊ = tanh²η and |x₋| = sinh²η, with sinh η tanh η = √J.
   Hence x₋(J) = −x₊(J)/(1 − x₊(J)) **[C1]**.
   *Targets:* **D-partner/α**; **D-filters** (SUSY-QM origin). *Source:*
   manuscript §2, eq. (rapidity).
   This gives the partner root a kinematic meaning: β² and (γβ)² of one
   orbit. It complements physres5's eq. (negative-from-positive), and it
   offers one variable whose two projections produce both branches.
8. **Scheme evidence for low-energy placement.** The scale μ from W and from Z
   agrees to 7 MeV with PDG masses, and to 0.58 GeV with MS-bar(M_Z) inputs.
   sin²θ_MS-bar(M_Z) = 0.2315 lies 4% away. One-loop running never returns
   M_W/M_Z = 0.881419 above M_Z.
   *Targets:* A2, **D-pole**. *Source:* manuscript §8.
   This supports A2 over running or high-scale placement. The section comes
   from the noteOpus spine, and the repository has no RGE script for it.
9. **α-endpoint arithmetic [C8].** Take M_W² = g²v²/4 and the reading
   (s = 1, −) ↔ v/√2. Then g² = 2x₊(¾)/|x₋(2)| and α = g² s²_dV/4π. This
   gives 1/α = 135.29 uncorrected and 132.26 with κ = 3/8, against
   1/α_Gμ = 132.10.
   *Target:* **D-partner/α**. *Source:* curator only.
   This places the reading in the tree-level G_μ scheme. Its accuracy equals
   the accuracy of the v/√2 slot, so it adds no independent evidence.
10. **Higher-spin tower.** M₊(s) accumulates at μ ≈ 106.6 GeV: 96.54, 99.58,
    101.45 and 102.68 GeV for s = 3/2 to 3. |M₋(s)| grows like μ√J.
    *Target:* **D-filters**. *Source:* manuscript §7, Table 2;
    `algebra/higher_spin_slots.py`.
    This is a worked case for the Regge-survival filter. A tower reading puts
    extra positive-branch states at 96–107 GeV, and a source route must remove
    or exhibit them. The manuscript presents 96.54 GeV as a prediction and
    compares it with the LEP/CMS 95–98 GeV hints.
11. **Look-elsewhere machinery.**
    *Target:* **D-pole**. *Source:* `algebra/look_elsewhere.py` and
    `curator_checks.py` §9.
    The script is a template for item 1 of physres5's `OPUS_IDEAS.md`, a scan
    over alternative (J_W, J_Z). [C9] adds two lessons: set the window from
    the experimental σ, and count trials over the modelling choices.
12. **Complex-pole re-anchoring [C7].** On physres5's M_Z,pole = 91.1538 GeV:
    - κ_F moves from 0.3886 to 0.3763.
    - M_F(κ = 3/8) − v/√2 falls from +72 MeV to +7 MeV.
    - κ_H with the PDG-Live 2026 m_H moves from 0.3656 to 0.3720.
    - The dV M_W offset falls from +5.5 MeV to +4.0 MeV.

    *Targets:* A2, **D-partner/α**. *Source:* curator only.
    physres5's own pole convention (A2) sharpens the partner-slot coincidence
    the projects reported. Any import of their numbers should use this anchor.
    The coefficient is still not derived.

## 4. Negative results worth keeping

- **No framework fixes κ.**
  - Custodial EFT and HEFT leave κ as a free Wilson coefficient.
  - Minimal composite Higgs (SO(5)/SO(4)) gives a gauge Coleman–Weinberg term
    with multiplicity 3g² + g′² and strong-sector integrals.
  - Quiver and deconstructed models tie κ to site couplings and link masses.
  - SUSY D-terms give a hypercharge normalization of 1/8, and their SU(2)_L
    D-term survives g′ → 0.
  - Gauge Reggeization carries C_F/C_A in the trajectory functions of
    high-energy amplitudes, which is a different observable.
  - String and D-brane models reduce to the same EFT matching.

  Sources: `hans-extras/mechanisms/scorecard.md`, `referee_report.md`,
  `hans-extras/referee_report.md`.
- **Conditional no-go (hans).** Assume the SM gauge group and the SM
  hypercharge normalization. Custodial breaking then enters through the single
  gauged generator T_R³. At order g′² the available group factors are
  (T_R³)² = 1/4, Tr_F/Tr_adj = 1/4 and Y_H²/2 = 1/8. C_F/C_A = 3/8 sums all
  three generators. Reaching 3/8 needs a UV threshold, an exotic charge, or a
  chosen Wilson coefficient. `hans-extras/mechanisms/conditional_no_go.md`
  lists the assumptions.
- **Paired exotic D-term.** V_D = (g′²/2)(q_H|H|² + q_S|S₊|² − q_S|S₋|²)²
  gives an exactly traceless split with κ = 2q_H q_S = q_S. The target needs
  q_S = 3/8, and that charge fails every standard embedding:
  - It sits off the 1/6 hypercharge lattice: (3/8)/(1/6) = 9/4.
  - No SU(5) tensor weight through rank 8 equals ±3/8.
  - No embedding Y = T_R³ + X through j_R = 4, with X on the 1/6 lattice,
    gives 3/8.
  - The fields carry electric charges ±3/8 as singlets, or 7/8 and −1/8 as
    doublets.

  Hidden-U(1) kinetic mixing reaches q_eff = 3/8 only through a continuous
  mixing parameter.
- **GUT 3/8.** Minimal SU(5) gives sin²θ_W = (3/5)/(1 + 3/5) = 3/8 as a
  unification boundary value. C_F/C_A = (3/4)/2 is a weak-scale Casimir
  quotient. The two share a rational number and differ in group theory.
  physres5's scheme map lists the GUT boundary value as a comparison class,
  so this warning applies there as well.
- **Size.** The target (3/8)(M_Z² − M_W²) = (3/32)g′²v² ≈ 696 GeV² is
  tree-sized.
  - The SM one-loop gauge Coleman–Weinberg term gives −32.7 GeV²: opposite
    sign and about 20× smaller.
  - The top loop gives about −1100 GeV² at Λ = m_t.
  - A one-loop origin needs a finite coefficient A = 2π² (full C_F) or 6π²
    (single generator).
  - A quadratic threshold needs M ≈ 1.1–1.9 TeV, and its sign depends on the
    model.
- **SMEFT viability map (soft no-go).** O_H hosts the size at
  c_H/Λ² ≈ 0.095 TeV⁻², about 2% of the κ_λ bound. O_H□ needs 15× its bound.
  The T parameter excludes O_HD by a factor of 73. The g′²v² form requires
  Λ ≈ 2.3 TeV for c_H = 1. The projects found no UV completion with
  c_H ∝ g′².
- **One identity counted three times.** The signed trace ratio, the
  determinant ratio and C_F/C_A all equal J_W/J_Z by Vieta: the roots at each J
  sum to −J and multiply to −J. Early drafts presented them as three results.
- **Snapshot dependence.** κ_H falls from 0.3751 to 0.3656 when m_H moves from
  125.20 to 125.13 GeV. δm_H = 0.11 GeV alone spans κ_H ± 0.015. The quoted
  10⁻⁵ agreement therefore describes one central value.
- **Post-diction.** Two inputs, a scale and a ratio, produce four outputs.
  Anchoring on M_W or m_H in place of M_Z reproduces the other slots at similar
  precision (`algebra/mw_tension_and_anchors.py`). The signed-dv higher-spin
  scan found no slot within 5 GeV of a known SM mass.
- **v-slot scheme.** No standard vev definition lands on M_F = 174.175 GeV.
  The candidates were v from G_F, v√(1 − Δr), and MS-bar at m_t. The 25 GeV²
  residual is about 1.9% of Δr·v²/2 ≈ 1100–1330 GeV²
  (`algebra/running_mass_results.md`).
- **Other checks.**
  - CDF II (M_W = 80.4335 ± 0.0094 GeV) would exclude the positive-branch M_W
    at about 6σ.
  - No single MS-bar scale reproduces both sectors (manuscript §8).
  - De Vries's auxiliary formula tan θ = β₁⁴ misses the Casimir value of r_W
    by 8×10⁻⁶. It is a near-identity in surds (manuscript App. A).

## 5. Open threads

**Submission blockers**, from `SUBMISSION_CHECKLIST.md` and critic 7:

1. Confirm the author block and affiliation, and add an ORCID. The block
   currently reads A. Rivero, EUPT, Universidad de Zaragoza, with an
   institutional e-mail address.
2. Change `\documentclass{article}` with PRD options to `svjour3`, then
   recompile.
3. Lock the PDG inputs to a dated snapshot. The text mixes PDG 2024 headline
   numbers with a PDG-Live 2026 caveat.
4. Confirm the publication status of Antusch–Hinze–Saad, arXiv:2510.01312.
5. Finish the remaining editorial tasks:
   - Write the cover letter from the source's
     `draft/cover_letter_template.md` (not copied).
   - Plan the arXiv hep-ph posting.
   - Shorten the acknowledgments and place the AI-use disclosure as EPJ Plus
     policy requires.
   - Change "equivalent" to "parallel" in the acknowledgments.

**Consistency defects found during curation.** Fix these before submission.
The numbers come from `curator_checks.py`.

6. The FCC-ee significance appears three ways (§2, item 5). Choose one
   reference value, one FCC-ee resolution and one mass scheme.
7. The Table 1 predictions (80.3724, 176.1602 and 122.3879 GeV) disagree with
   the table's own ratios times M_Z = 91.1880 GeV, which give 80.3748,
   176.1617 and 122.3897 GeV **[C3]**. The W entry is off by 2.4 MeV, which
   exceeds its quoted ±1.8 MeV. `EXECUTIVE_SUMMARY.md` repeats 80.3724.
8. Fix M1 changed the displayed m_H to 125.20 ± 0.11 GeV, but the derived
   numbers still use the noteOpus value 125.25 ± 0.17 **[C5]**:

   | Quantity | Printed (m_H = 125.25) | With m_H = 125.20 |
   |---|---|---|
   | m_H-slot scale | 109.069 ± 0.148 GeV | 109.025 ± 0.096 GeV |
   | trace identity | 0.027% | 0.055% (0.093% with 125.13) |
   | δ(m_H²) | +708 GeV² | +696 GeV² |
   | χ²/dof | 0.13/2 (curator refit: 0.26/2) | 0.99/2 (4.7/2 with PDG-Live 2026 W, Z, H) |

9. Eq. (spurion), M²_{s,−} → M²_{s,−} + (−1)^{2s+1}βm², moves both slots
   away from the data when applied to the signed eigenvalues: 119.4 and
   178.2 GeV. Table 2's 125.30 and 174.10 GeV come from shifting |M²_{s,−}|
   instead **[C6]**. App. B repeats the signed form. In physres5's signed
   variables the correction reads x₋(¾) → x₋(¾) − κΔ and x₋(2) → x₋(2) + κΔ,
   with Δ = x₊(2) − x₊(¾).
10. Eq. (pauli), σ⁺⊗C₁C₂ + σ⁻⊗1 + ½(1 − σ_z)⊗C₂, has determinant −C₁C₂.
    Its characteristic polynomial λ² + Jm²λ + Jm⁴ has complex roots for
    J < 4, while the quartic requires +C₁C₂ **[C2]**. physres5's symmetric
    Q(J) = μ²[[0, √J], [√J, −J]] has the correct trace and determinant (A1).
11. The look-elsewhere statistic has the three problems listed in §2, item 3.
12. The Conclusions (§13) call the C_F/C_A form an "exact rewriting" of the
    (−1)^F spurion. §6.1, after fix M2, says the two differ by 3.4% in β.
13. `SUBMISSION_CHECKLIST.md` still lists critic 7 as "(in-flight)", while
    `FINAL_STATE.md` and the cycle-22 critique record GO.
14. Every comparison uses PDG Breit–Wigner (running-width) masses, and the
    text calls them pole masses. physres5's complex-pole inputs lower M_Z by
    34.1 MeV and M_W by 28.5 MeV. Item 12 of §3 gives the consequences.

**Research threads:**

15. Derive κ. signed-dv `OPUS_IDEAS.md` item 1 proposes tree-level matching
    of candidate UV completions onto O_H and O_HD, to test whether
    c_H ∝ g′² emerges with κ = C_F/C_A. The candidates are a real singlet, a
    custodial triplet, a hypercharged scalar with a kinetic-mixed U(1), and
    the 2HDM alignment limit. hans `OPUS_IDEAS.md` item 3 proposes extending
    the conditional no-go to all orders in the T_R³ spurion and adding
    one-loop matching in the two boundary models.
16. Harden the look-elsewhere statistic, as both `OPUS_IDEAS.md` files
    propose: decoy targets for an empirical null, a description-length prior,
    windows set by the experimental σ, and a trials factor over the modelling
    choices.
17. Build one dated input file with Monte Carlo propagation to κ, the sum rule
    and the FCC-ee statement, including the complex-pole conversion (both
    `OPUS_IDEAS.md` files).
18. Find a bound-state origin for the negative root (Bethe–Salpeter or
    anti-bound state), as the signed-dv referee report proposes. It would give
    physres5's partner branch a dynamical source.
19. Settle the physical meaning of μ = 106.58 GeV (106.54 GeV on the
    complex-pole anchor) and the fate of the 96–107 GeV positive-branch tower.
20. hans cites p = 1.564×10⁻⁶ but its repository lacks `look_elsewhere.py`
    (hans `OPUS_IDEAS.md` item 1). This folder now holds both.

## 6. Curator checks

`curator_checks.py` needs numpy, scipy and sympy. It runs in about 10 s and
writes nothing. Its inputs are:

- PDG 2024 and PDG-Live 2026 values, as recorded in
  `hans-extras/literature/experimental_inputs.md`;
- G_F = 1.1663788×10⁻⁵ GeV⁻²;
- physres5's complex-pole M_Z = 91.1538 GeV and M_W = 80.3407 GeV, from
  `manuscript/sections/03_pole_observable.tex`.

| Tag | Check | Result |
|---|---|---|
| C1 | exact identities | x₊ + x₋ = −J; x₊x₋ = −J; x₋ = −x₊/(1 − x₊); cos²θ_dV = (3/8)F_dyn; trace and determinant ratios both 3/8 |
| C2 | manuscript eq. (pauli) | determinant has the wrong sign: char. poly λ² + Jm²λ + Jm⁴ |
| C3 | Table 1 | entries off by 1.5–2.4 MeV from ratio × M_Z |
| C4 | FCC-ee offsets | 7.9 MeV vs ATLAS 2024; 5.2–5.6 MeV vs PDG 2024; 11.9–12.3 MeV vs PDG-Live 2026 |
| C5 | m_H input dependence | derived numbers use 125.25 ± 0.17; χ² refit 0.26 / 0.99 / 4.7 for 2 dof |
| C6 | spurion sign | signed rule gives 119.41 / 178.19 GeV; magnitude rule gives 125.30 / 174.11 GeV |
| C7 | anchor dependence | §3 item 12. Sum-rule residual −25.0 / −42.5 GeV² on the Breit–Wigner anchor and +9.4 / −8.1 GeV² on the complex-pole anchor, for m_H = 125.20 / 125.13 |
| C8 | α endpoint | 1/α = 135.29 uncorrected, 132.26 corrected; 1/α_Gμ = 132.10 |
| C9 | look-elsewhere recount | window 10⁻⁵: A 2.76×10⁻⁶, B 1.56×10⁻⁶ (reproduces the script). Window = dV residual 3.1×10⁻⁵: A 8.5×10⁻⁶, B 5.1×10⁻⁶. Window = 1σ (3.3×10⁻³): A 9.1×10⁻⁴, B 5.3×10⁻⁴ |

## 7. Manifest

The folder totals about 0.87 MB, including this file. Copies are verbatim and
keep the source-relative layout, so links inside the copied notes (`draft/…`,
`algebra/…`, `mechanisms/…`) resolve wherever the target was copied.

**signed-dv**, copied from `/home/codexssh/signed-dv-custodial-project/` with
the same relative paths:

| Path | Bytes | Content |
|---|---:|---|
| `draft/fused_manuscript.tex` | 86,648 | canonical EPJ Plus manuscript: noteOpus spine plus signed-dv §6.1, §6.2, §11, §12 |
| `draft/fused_manuscript.pdf` | 509,842 | compiled 16-page PDF, built 2026-05-14 03:39 after the last .tex edit |
| `draft/figs/spectrum.pdf` | 23,435 | Fig. 1, the signed spectrum for s = ½ to 3 |
| `draft/figs/make_spectrum.py` | 3,495 | figure generator; line 147 writes to an absolute path inside the source project |
| `run_checks.sh` | 1,310 | runs the 12 scripts below in about 45 s; rewrites the timing line of `algebra/look_elsewhere_results.md` |
| `algebra/verify_signed_roots.py` | 2,887 | exact roots, trace and determinant identities, corrected slots |
| `algebra/explore_deformations.py` | 12,351 | deformation catalogue: η, η_s, on-shell subtraction, Regge intercept, spurions, custodial parent, σ₃ |
| `algebra/oneloop_gauge_higgs.py` | 4,806 | SM one-loop Coleman–Weinberg gauge term (−32.7 GeV²) |
| `algebra/scalar_scale_identification.py` | 3,734 | corrected slots compared with m_H and v/√2 |
| `algebra/precision_decomposition.py` | 4,866 | trace/traceless split of the physical shifts (κ_t = 0.3818, ε_s ≈ −12 GeV²) |
| `algebra/oneloop_top_higgs.py` | 5,689 | top-loop δm_H² and Δρ |
| `algebra/higher_spin_slots.py` | 2,982 | slots for s = 0 to 3 |
| `algebra/closed_form_predictions.py` | 4,574 | closed-form radicals for m_H²/M_Z² and (v/√2)²/M_Z² |
| `algebra/smeft_nogo.py` | 6,931 | SMEFT viability map |
| `algebra/mw_tension_and_anchors.py` | 4,191 | CDF tension and anchor independence |
| `algebra/running_mass_scheme.py` | 10,213 | vev-scheme dependence of the v/√2 slot |
| `algebra/running_mass_results.md` | 2,737 | results of the scheme script |
| `algebra/look_elsewhere.py` | 15,476 | look-elsewhere scan, Families A, B and C |
| `algebra/look_elsewhere_results.md` | 3,644 | results of the look-elsewhere scan |
| `final_recommendation.md` | 4,001 | cycle-17 status and contents of the merged paper |
| `FINAL_STATE.md` | 2,425 | end-to-end verification record |
| `referee_report.md` | 6,666 | cycle-10 referee report |
| `EXECUTIVE_SUMMARY.md` | 4,029 | one-page summary, including the ~12σ statement flagged above |
| `SUBMISSION_CHECKLIST.md` | 3,025 | EPJ Plus checklist with author and ORCID placeholders |

**hans-extras**, copied from `/home/codexssh/hans/signed_dbdevries/` with the
same relative paths:

| Path | Bytes | Content |
|---|---:|---|
| `algebra/custodial_rep_charge_scan.py` | 1,669 | Y = T_R³ + X scan through j_R = 4 |
| `algebra/su5_weight_lattice_scan.py` | 1,715 | SU(5) tensor weights through rank 8 |
| `algebra/two_state_projector_scan.py` | 3,582 | σ₃ basis and single-generator traces |
| `algebra/deformation_scan.py` | 4,303 | on-shell-subtracted deformation |
| `algebra/paired_dterm_model.py` | 2,018 | paired exotic D-term |
| `algebra/kinetic_mixing_charge_shift.py` | 1,611 | kinetic mixing for q_eff = 3/8 |
| `algebra/charge_lattice_check.py` | 2,305 | Y = 3/8 against the SM and SU(5) lattices |
| `algebra/effective_operator_matching.py` | 2,676 | matching that gives c_Y = 3/16 |
| `algebra/gut_hypercharge_normalization.py` | 1,809 | SU(5) sin²θ_W = 3/8 check |
| `algebra/loop_threshold_estimates.py` | 2,915 | loop, threshold and D-term sizes |
| `algebra/negative_sector_fit.py` | 3,464 | κ_H, κ_F and the trace leak for two input sets |
| `algebra/current_input_comparison.py` | 1,950 | historical versus current inputs |
| `algebra/verify_spectrum.py` | 3,605 | exact spectrum |
| `algebra/weak_angle_comparison.py` | 1,809 | positive-branch angle against on-shell inputs |
| `algebra/run_all_checks.py` | 1,510 | runs every script in its folder (14/14 PASS here) |
| `algebra/README.md` | 2,948 | script index; its two sister scripts are `../../algebra/explore_deformations.py` and `../../algebra/verify_signed_roots.py` in this folder |
| `final_recommendation.md` | 9,825 | ranked mechanisms and per-cycle updates |
| `referee_report.md` | 12,262 | referee answers, mechanism by mechanism |
| `stress_tests.md` | 4,602 | gauge, scheme and custodial-parent stress tests |
| `mechanisms/conditional_no_go.md` | 2,471 | the conditional no-go |
| `mechanisms/scorecard.md` | 3,127 | mechanism scorecard |
| `mechanisms/two_state_projector.md` | 2,504 | projector and T_R³ obstruction |
| `mechanisms/minimal_negative_sector_eft.md` | 2,389 | EFT with c_Y = 3/16 |
| `mechanisms/paired_exotic_dterm.md` | 2,357 | D-term construction |
| `mechanisms/kinetic_mixing.md` | 1,523 | kinetic-mixing escape route |
| `mechanisms/charge_quantization.md` | 1,445 | charge-lattice check |
| `mechanisms/custodial_rep_charge_scan.md` | 1,117 | custodial charge scan |
| `mechanisms/su5_rep_scan.md` | 1,160 | SU(5) scan |
| `mechanisms/gut_hypercharge.md` | 1,966 | GUT 3/8 comparison |
| `mechanisms/loop_thresholds.md` | 2,650 | size estimates |
| `phenomenology/negative_sector_fit.md` | 1,911 | κ drift between input sets |
| `literature/experimental_inputs.md` | 2,357 | PDG 2024 and PDG-Live 2026 inputs with URLs |

**Curator files:** `SUMMARY.md` (this file) and `curator_checks.py`
(11,484 bytes).

**Left in the sources.**

signed-dv:
- `notes/rivero_noteOpus.{tex,pdf,txt}`: A. Rivero's May 2026 note, an input
  whose content forms the manuscript spine.
- `notes/original_hidden_coupling_note.{tex,pdf}`: an input note "prepared
  from a working conversation". §3 item 3 restates its F_dyn identity.
- `exploration_log.md`: the cycle narrative.
- `critique/`: eight critic reports, summarized in `SUBMISSION_CHECKLIST.md`
  and `FINAL_STATE.md`.
- `mechanisms/`: expanded copies of the hans analyses plus the six
  prompt-mandated surveys.
- `literature/` and `bibliography/seed_references.bib`: the manuscript
  carries its own inline bibliography.
- `draft/prd_signed_root_draft.*` and `draft/relation_to_prior_numerology.tex`:
  superseded pre-fusion drafts.
- `draft/cover_letter_template.md`, `prompt.md` and `README.md`.
- `checks_output.txt`: output from 02:33, before the last cycles; regenerate
  it with `run_checks.sh`.
- `OPUS_IDEAS.md`: its proposals appear in §5.
- LaTeX build files and `__pycache__/`.

hans:
- `sister_project_import/`: verbatim copies of early signed-dv files.
- `algebra/explore_deformations_extended.py` and
  `algebra/verify_signed_roots_extended.py`: byte-identical to the signed-dv
  scripts copied above.
- `draft/main.{tex,pdf}` and build files: the hans note, whose content the
  copied notes cover.
- `research_cycles.md` and `sister_project_synthesis.md`.
- The six prompt-mandated mechanism surveys.
- `phenomenology/lee_sister_assessment.md`,
  `phenomenology/scheme_sister_assessment.md` and
  `phenomenology/weak_angle_comparison.md`: restatements of signed-dv results.
- The bibliographies under `literature/`.
- `project_prompt.md`, `README.md`, `OPUS_IDEAS.md` and
  `notes/original_hidden_coupling_note.*`.
