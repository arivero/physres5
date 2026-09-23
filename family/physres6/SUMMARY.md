# physres6: a PRL spin-off on electroweak couplings fixed by Kaluza–Klein moduli

Curated 2026-09-23 for the physres5 family archive. Copied files are unchanged
from the source; the manifest lists sizes and hashes.

Shorthand. physres5 assumptions: **A1** the 2×2 Casimir matrix
[[0,√J],[√J,−J]]; **A2** pole placement; **A3** the ordered assignment
J_W = 3/4 (Higgs doublet), J_Z = 2 (adjoint). physres5 Appendix D targets
(`manuscript/sections/D_theorem_targets.tex`): **D1** pole placement;
**D2** electroweak assignment and ray admissibility; **D3** local route kernel
(boundary determinant, G2/ADE pairing); **D4** partner/negative branch and
alpha endpoint; **D5** branch scaling, Regge intercept survival, SUSY-QM origin.

physres6's own ledger labels its hypotheses "A1" (the assignment
(J_W, J_Z) = (3/4, 2)) and "A2" (v = √2·M₋(2)). In this summary A1–A3 keep the
physres5 meaning, and physres6's second hypothesis is called the **scale tie**.

## Provenance

- **Source:** `/home/codexssh/physres6`, a git repository (branch `master`, no
  remote, 4 commits, HEAD `52442b5`, author arivero).
- **Dates:** created 2026-05-22. All research content was committed that day
  between 14:08 and 14:34 CEST:
  - `ed860ab`: the initial Letter;
  - `9aa6c57`: the derived-versus-assigned table, the reciprocal invariant and
    the branch duality;
  - `42a8b79`: the broken N=2 SUSY-QM reading and the corrected branch scaling.

  The built PDF (14:34) matches the final `main.tex`. The test caches date from
  2026-07-01. A Fable review wrote `OPUS_IDEAS.md` on 2026-07-02, and it was
  committed on 2026-09-23.
- **Relation to the siblings:** a Physical Review Letters spin-off of physres5.
  - Its `AGENTS.md` names physres5 as the companion long version and leaves the
    theorem-target program there.
  - It inherited physres5 snapshots in `context/inherited/`: an older
    `OPEN_ISSUES.md` with O1, O4, O10, O17 and O18, plus
    `concept_claims_matrix.md` and `project_memory.md`. It also inherited
    physres5's scripts and test file.
  - The marathon paper (`../marathon/`) shares the kernel, the scale
    μ = M∞ = 106.578 GeV and the s = 3/2 slot at 96.5 GeV.

## Goal and final conclusion

**Goal.** A short Letter arguing that one breaking operator
Q(J) = μ²[[0,√J],[√J,−J]], J = s(s+1), fixes both dimensionless electroweak
couplings. The proposed mechanism is that electroweak symmetry breaking is
Kaluza–Klein moduli stabilization. Witten (Nucl. Phys. B186 (1981) 412) makes
gauge couplings functions of the compactification radius and leaves the radius
a free modulus. The tachyonic lower branch of Q(J) is proposed as the order
parameter that fixes it.

**Conclusion as shipped** (`manuscript/main.pdf`: 3 pages as built in revtex PRL
format, about 2400 words):

- sin²θ = 1 − x₊(3/4)/x₊(2) = 0.223101, within 0.04% of the on-shell
  1 − M_W²/M_Z² = 0.22320.
- With the scale tie v = √2·M₋(2), μ cancels in g = 2M_W/v. That gives
  g² = x₊(3/4)·x₊(2) and 1/α = 4π/[x₊(3/4)(x₊(2) − x₊(3/4))] = 135.29. The
  Letter places this value in the few-GeV hadronic region of the running
  coupling.
- One input (M_Z) fixes μ = 106.578 GeV and the spectrum:
  - W at 80.375;
  - M₋(3/4) = 122.39 (M_h −2.2%);
  - M₋(2) = 176.16 (m_t +2.1%);
  - v = 249.13 (+1.2%);
  - the next positive slot, M₊(3/2) = 96.54 GeV.
- **Status:** referees A and B both asked for major revision, and the final text
  carries most of their fixes. The mechanism is still a hypothesis. The −J
  entry, the assignment and the scale tie are underived, and the Letter's
  Table I lists them as assigned.

## Valuable ideas and results

1. **Scale-tie chain with closed-form couplings**
   (`calculations/alpha_derivation_attempt.md`).
   - The equivalences: v = √2·M₋(2) ⟺ g² = x₊(3/4)·x₊(2) ⟺
     g_Z = √(g²+g′²) = x₊(2) = √3 − 1 ⟺ v = (1+√3)·M_Z ⟺ μ² = v·M_Z/2.
   - Consequences: g′² = x₊(2)(x₊(2) − x₊(3/4)),
     e² = x₊(3/4)(x₊(2) − x₊(3/4)) and 1/α = 135.29.
   - The number itself comes from Rivero, hep-ph/0606171, which already gives
     α⁻¹ = 135.28 at tree level with λ_h = 1.

   *Why:* it names the one extra hypothesis that an α claim needs and puts it in
   closed form.
   *Bears on:* D4 alpha endpoint; uses A3.
2. **Reciprocal invariant** (`calculations/reciprocal_invariant.md`).
   tr Q = det Q ⟺ 1/x₊ + 1/x₋ = 1 ⟺ 1/M₊² + 1/M₋² = 1/μ² ⟺ tr Q(J)⁻¹ = 1/μ²
   at every level. Each gauge mass is therefore the parallel combination of μ²
   and its partner.
   *Why:* the inverse operator has the same trace at every level, and that
   single condition is something a source route could deliver in one step.
   *Bears on:* A1; D3.
3. **Sign reduction** (same note). When the upper diagonal is zero, tr = det
   forces (off-diagonal)² = −(lower diagonal). A Hodge off-diagonal √J then
   fixes the diagonal at −J. The only free input left is the sign of the
   partner entry.
   *Why:* it cuts physres5's entry conditions Σ_aa = J and Σ_ha·Σ_ah = J down
   to one datum plus a sign.
   *Bears on:* A1; D3; D5 SUSY-QM origin.
4. **Broken N=2 SUSY-QM reading and a positivity obstruction**
   (`manuscript/main.tex`, `calculations/squashed_s3_attempt.md`).
   - {d, δ} = Δ pairs φ with dφ/√J at eigenvalue J, with mixing √J. The −J
     entry breaks the degeneracy.
   - The Hodge Laplacian is non-negative while det Q = −J < 0, so Q(J) cannot
     be a Hodge Laplacian.
   - The negative entry therefore has to come from somewhere else: the
     Weitzenböck/Bochner curvature term (∇*∇ = Δ − Ric) on a squashed Berger
     S³, a Hosotani Wilson-line potential, or both.

   *Why:* it sharpens physres5's Hodge subroute
   (`06c_kaluza_klein_boundary.tex`); the de Rham part supplies √J, and the
   obstruction shows where −J has to come from.
   *Bears on:* D5 SUSY-QM origin; A1.

5. **S³ = SU(2) fingerprint** (`calculations/kk_free_thoughts.md` §1,
   `reviews/advisor.md` §2). J = 3/4 needs half-integer harmonics. S³ carries
   them by Peter–Weyl; S² has integer l only. Henkel–Lauret (arXiv:2605.05406,
   Lemma 2.1 and Prop. 3.3) write the S³ 1-form Laplacian as a Casimir
   diagonal, a connection cross-term and a curvature term 2q(R). That is the
   shape of Q(J).
   *Why:* it picks the smallest internal geometry that can host the W slot and
   names a concrete computation.
   *Bears on:* A3; D3.

6. **Branch inversion and brane scaling** (`calculations/branch_duality.md`).
   x → −J/x (M² → −μ⁴J/M²) swaps the two branches and has no real fixed point.
   Against spin s, M₊ → μ stays bounded (D0-like) and M₋ grows like s
   (space-filling). The inversion therefore pairs all-Dirichlet with
   all-Neumann.
   *Why:* it supplies the algebra behind physres5's branch-scaling filter, with
   spin fixed as the axis.
   *Bears on:* D5 branch scaling; D4 partner branch.

7. **Regge completion with separate labels** (`main.tex`, Fig. 1).
   M²_{N_osc,j,±} = μ²x_±(j(j+1)) + N_osc/α′. The sector label j, the
   oscillator level N_osc and the Lorentz spin are kept distinct.
   *Why:* this consistent form replaced an additive J = n + j version after
   referee B caught it.
   *Bears on:* D5 Regge intercept survival.

8. **KK-fixing mechanism** (`calculations/kk_fixing_concept.md`). Couplings are
   geometric and the radius is a modulus (Witten 1981, pp. 424–425). The order
   parameter is therefore proposed as the stabilizer (the Higgs = radion
   reading). Its negative mode is admissible above the Breitenlohner–Freedman
   bound.
   *Why:* it is the family's only physical account of why a coupling gets
   fixed at all.
   *Bears on:* D4 alpha endpoint and partner branch.

9. **Derived-versus-assigned ledger** (`context/claims_ledger.md`, Table I of
   the Letter). Every quantitative sentence has a row tagged derived, assigned,
   coincidence or cited.
   *Why:* the referees found the overclaims by checking the prose against this
   ledger, which makes it a ready template.
   *Bears on:* physres5's status ledger (`09_status_and_tests.tex`).

10. **Reference audit** (`reviews/reference_audit.md`). The audit:
    - gives page-level quotes from Witten 1981;
    - confirms that Rivero 2006 already contains α⁻¹ = 135.28 and the vacuum
      hint;
    - rates Salam–Strathdee as weak support for gauge-Higgs unification;
    - finds that the DuffNilssonPope1986 key points at the 2025 retrospective
      arXiv:2502.07710;
    - finds that Jegerlehner2019 is arXiv:0807.4206, from 2008;
    - notes that the Regge and dual-resonance framing lacks Veneziano 1968 and
      Chew–Frautschi.

    *Why:* these corrections apply directly to the bibliography physres5 shares.
    *Bears on:* physres5 bibliography, all targets.

## Curator's cross-checks (computed 2026-09-23, not in the source)

These use the copied `devries_spectrum.py` values and the measured
M_W = 80.3692, M_Z = 91.1880 and v = 246.22 GeV.

- **The scale tie is marathon's compact form.** It says v = (1+√3)·M_Z =
  249.13 GeV, which is 1.18% high. Equivalently, g_Z = √3 − 1 = 0.73205
  against the tree-level 2M_Z/v = 0.74070 (−1.17%).
- **α follows from that offset.** The measured (M_W, M_Z, v) give a tree-level
  1/α = 132.10. Scaling it by (v_tie/v)² = 1.0238 gives 135.24, within 0.04% of
  135.29. The "infrared α" agreement is therefore the scale tie's 1.18% offset
  in v, squared, and α and v count as one test.
- **α depends on which identification is chosen.** Marathon's Lemma 1 says
  m₋(1/2) = v/2 and m₋(1) = v/√2 cannot both hold. The scale tie is the v/√2
  identification. Taking the other one (v/2, off by −0.58%) as exact gives
  g² = x₊(3/4)/|x₋(3/4)| = 0.43127 and 1/α = 130.60.

## Negative results worth keeping

- **D = 10 "forced by chirality".** Both referees showed that the
  D = 11 → 10 → 9 interpolation is an analogy, for four reasons:
  - spacetime dimension is an integer;
  - no interpolating field is exhibited;
  - Witten's D = 11 no-go says nothing about chirality for this construction at
    D = 10;
  - five internal dimensions is only a lower bound for SU(3)×U(1).

  The body now calls it motivation, but the abstract still says "forces".
  Bears on physres5 Appendix E (O10).
- **Hodge and S² routes.** Q(J) cannot be a Hodge Laplacian, by positivity. S²
  cannot host the kernel either: as a symmetric space it gives a pure Casimir
  with no negative diagonal, and it carries integer l only.
- **Scale tie underived.** The derivation attempt ended PARTIAL. It reduces
  exactly to g² = x₊(3/4)·x₊(2) and goes no further.
- **Additive Regge label.** J = n + j contradicts the Casimir J = j(j+1) that
  reproduces 3/4, 2 and 15/4.
- **Charged reading of the 96.5 GeV slot.** One state cannot be both the neutral
  γγ excess (spin 0 or 2 by Landau–Yang) and a charged chiral charge-4/3 state.
  The Letter dropped the charged reading, though `devries_spectrum.py` still
  prints "chiral 4/3?".
- **String reading of the negative branch.** The step "M₋² ∝ J, hence a string
  or D1" used the Casimir as the axis. Against spin, M₋ grows linearly and
  M₋/√s grows too, so the branch is space-filling and matches no string law.
- **"The order parameter is the stabilizer".** Bucci (hep-ph/0403012) and
  Haba–Oda (arXiv:1102.1970) establish a link between electroweak breaking and
  radion stabilization. The claim that the order parameter is the complete
  stabilizer goes beyond them, and the final Letter labels it as its own
  hypothesis.
- **A sharp 1 GeV scale for α.** Referee A's running estimate gives
  1/α(1 GeV) ≈ 134.8–135.3. The scale that returns 135.3 is set by the hadronic
  vacuum polarization, which is the least certain input, so the Letter can claim
  only a low-energy band.

## Open threads

- **Referee items still open in the final `main.tex`:**
  - the abstract says chirality "forces" D = 10;
  - the abstract presents the operator as established ("A breaking operator at
    each internal level realizes this");
  - the text calls the lower-branch matches "each within a percent", though the
    deviations are −2.2%, +2.1% and +1.2%;
  - the scale tie enters the sentence before Eq. (3) with no "assumption"
    label.

  The referee reports reviewed a draft older than the first commit, so their
  line numbers do not match the copied text.
- **Berger-sphere computation** (OPUS_IDEAS 1, advisor §2). Apply Henkel–Lauret
  Prop. 3.3 to the metric g(a,b,c), scan the squashing and a Wilson-line phase,
  and test whether tr = det = −J holds at the s = 1/2 and s = 1 levels. A hit
  would deliver A1 and A3 together; a miss would rule out tree-level squashing.
- **Running-α inversion** (OPUS_IDEAS 2). Use Jegerlehner's Δα_had
  (arXiv:0807.4206) to find the scale Q* where 1/α(Q*) = 135.29, with its band.
  Given the cross-check above, the result measures the scale tie's offset in v.
- **Trials-factor Monte Carlo** (OPUS_IDEAS 3) over assignments and scale-tie
  primitives. Marathon's Theorem 2 family supplies a hypothesis class that can
  be registered in advance.
- **Tests.** `make test` fails at collection:
  - the test file, identical to physres5's, imports `mw_from_mz`; physres5's
    `devries_spectrum.py` defines it, but physres6's rewrite dropped it;
  - `scripts/check_project.py` also fails, because it requires
    `PROJECT_BRIEF.md`, `OPEN_ISSUES.md` and `codex_tasks/`, none of which
    exist here, and the Makefile's `|| true` hides that failure;
  - the assertions for g, 1/α and the spectrum planned as PLAN task T1 were
    never added.
- **Bibliography.** Fix the Jegerlehner key and year, the DuffNilssonPope1986
  metadata and the Salam–Strathdee attribution, and add dual-resonance sources.
- **Physics identifications.** The identity of the 96.54 GeV slot is open
  (physres5 O18). The scale tie also has two readings: a top Yukawa y_t ≈ 1 in
  physres6 and a Higgs quartic λ_h ≈ 1 in Rivero 2006.

## Left out of the copy

- **Third-party material.** `references/pdfs/` holds 35 MB of third-party papers
  and `context/source_fragments/` holds 8 MB of text extracted from them. Cite
  these instead:
  - Rivero, hep-ph/0606171;
  - Witten, Nucl. Phys. B186 (1981) 412;
  - Henkel–Lauret, arXiv:2605.05406;
  - Duff–Nilsson–Pope, arXiv:2502.07710 and Phys. Rept. 130 (1986) 1;
  - Breitenlohner–Freedman, Ann. Phys. 144 (1982) 249;
  - Hosotani, Phys. Lett. B126 (1983) 309;
  - Salam–Strathdee, Ann. Phys. 141 (1982) 316;
  - Bucci, hep-ph/0403012;
  - Haba–Oda, arXiv:1102.1970;
  - Csáki–Hubisz–Meade, hep-ph/0510275;
  - Jegerlehner, arXiv:0807.4206;
  - Biekötter et al., arXiv:2306.03889;
  - Martin–Robertson, arXiv:1907.02500;
  - Lauret, arXiv:1604.02471;
  - Da Silva, arXiv:2411.03525.
- **`context/inherited/`:** older snapshots of physres5's own files.
- **`reviews/codex_review.md`:** a raw Codex CLI session log. It makes three
  points:
  1. the operator was chosen, and nothing yet shows it to be the
     radion-stabilization operator of a controlled chiral D = 10
     compactification;
  2. the gap is a reduced action in which one normalized modulus sector fixes
     the radius and also yields the gauge normalization, the scale tie and the
     (3/4, 2) assignment;
  3. the fix is a derived-versus-assigned box, which became Table I.
- **Process documents** (`PLAN.md`, `OPUS_IDEAS.md`, `AGENTS.md`), folded into
  this summary. The lessons physres6 drew from physres5 are worth keeping:
  - state a derived result as a result, outside the theorem-target list;
  - cap referee passes at two;
  - measure progress by a derived result, an accurate ledger and a compiling
    paper.
- **Files identical to physres5's own copies:**
  `calculations/negative_branch_higgs_scale.md`,
  `calculations/electroweak_pole_scheme.md`, `context/style_policy.md`, the
  scripts, and `calculations/tests/test_devries_spectrum.py`. The test file was
  also left out because it fails at import and would fail any pytest run that
  discovers it inside physres5.
- **Build and tooling files:** `main.aux`, `.bbl`, `.blg`, `.log`, `.out`,
  `mainNotes.bib`, `__pycache__`, `.pytest_cache` and the `Makefile`.

## Manifest

Every file is copied unchanged from the same relative path in
`/home/codexssh/physres6/`. The hash column gives the first 12 hex digits of
SHA-256. `manuscript/` builds with pdflatex and bibtex (revtex4-2), and
`python3 calculations/devries_spectrum.py` reproduces the Letter's numbers.

| File | Bytes | SHA-256 | Content |
|---|---:|---|---|
| `manuscript/main.tex` | 15208 | 428057b3a0e0 | Final Letter source |
| `manuscript/main.pdf` | 271977 | cf27e68ec4c7 | Built Letter, 3 pages |
| `manuscript/macros.tex` | 271 | 524785d9dab9 | Macros needed by `main.tex` |
| `manuscript/references.bib` | 8702 | 33c1da6e2ae3 | Bibliography |
| `context/claims_ledger.md` | 2885 | c5f987e1561b | 25-row claims ledger |
| `calculations/devries_spectrum.py` | 3682 | aff0327d54d3 | Verification script (`make numbers`) |
| `calculations/kk_fixing_concept.md` | 5926 | 6e893772ecdf | Mechanism note; partial Q(J) derivation |
| `calculations/kk_free_thoughts.md` | 3987 | b8260e279114 | S³ fingerprint, flux reading, Higgs = radion |
| `calculations/alpha_derivation_attempt.md` | 2392 | 4368b8b84a9f | Scale-tie reduction (PARTIAL) |
| `calculations/reciprocal_invariant.md` | 2200 | ec75e3c0a3d5 | tr Q⁻¹ = 1/μ²; sign reduction |
| `calculations/branch_duality.md` | 3170 | 28849cf765af | x → −J/x; corrected brane scaling |
| `calculations/squashed_s3_attempt.md` | 2558 | 340d7b53d07c | S³/Berger route; positivity obstruction |
| `reviews/referee_A.md` | 18428 | 0cff31fd8d88 | Referee A: major revision |
| `reviews/referee_B.md` | 19485 | 730dcd02f95e | Referee B: KK and string physics |
| `reviews/advisor.md` | 13882 | 45a6c15026e0 | Advisor: BF framing, Berger S³ computation |
| `reviews/reference_audit.md` | 13824 | e169efe426ce | Citation-by-citation audit |

Total: 16 files, 388,577 bytes.

