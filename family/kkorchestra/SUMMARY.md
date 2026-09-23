# kkorchestra: the CP²/Aloff–Wallach Kaluza–Klein programme

Curated for physres5 on 2026-09-23. Everything outside this file is a verbatim
copy of project-authored material (see the manifest at the end).

**Tags used below for physres5 targets.** A1 = the 2×2 Casimir matrix
[[0,√J],[√J,−J]]; A2 = pole placement; A3 = the ordered assignment
J_W = 3/4 (Higgs doublet), J_Z = 2 (adjoint). From Appendix D
(`manuscript/sections/D_theorem_targets.tex`): D-pole = pole placement;
D-EW = electroweak assignment and ray admissibility; D-kernel = local route
kernel (boundary determinant, G2/ADE pairing); D-branch = partner/negative
branch and α endpoint; D-filter = branch scaling, Regge intercept survival,
SUSY-QM origin. App-E = Appendix E dimensional interpolation; §08 = global
form.

## Provenance

- **Source:** `/home/codexssh/kkorchestra`, a local workspace without git
  (42 MB; 17 MB of that is `docs/`, 18 MB is a third-party clone in
  `sources/stringbook`).
- **Dates:** the proposal arrived as a user-uploaded chat review
  ("Higgsing Kaluza–Klein Review", transcript dated 2026-05-30). A
  verification campaign (tasks T1–T6 and R1–R5, each with an independent
  verifier pass) ran on 2026-05-31 and is archived in
  `archive/verification_20260531/`. The 225 research notes and the 35 files in
  `out/` date from 2026-06-01.
- **Working rules** (its `AGENTS.md`): no Python for new work; every
  load-bearing equation carries a status (derived, cited, conditional,
  rejected, target). From 2026-06-01 the bare identification D†D = j(j+1) is
  banned as a premise of produced documents. A named operator with
  P†P|_r = x0·μ_r + σ_r (multiplier μ_r, common scale x0, residual σ_r)
  replaces it. Older reports that still use the bare form were moved to
  `archive/`.
- **Siblings:** `kkFable` (git, 2026-06-11/12) is the successor workspace. It
  symlinks all of kkorchestra read-only and settles the open fork recorded at
  the end of `wastebook.md` ("Which SU(3)?"). See `../kkFable/SUMMARY.md`.
- **De Vries provenance:** the signed-Hessian definitions were transcribed
  from the user's own files (`kk_devries_signed_hessian`, the Dolan–Nash/WZ
  addenda) as quoted inside a chat-review transcript in `docs/`. On a
  J-eigenmode the kkorchestra block A(D) = [[0,D†],[D,−D†D]] with D†D = J is
  the physres5 matrix.
- **Not copied:** `docs/` (87 files: transcriptions and PDFs of third-party
  papers, two chat transcripts, agent digests of arXiv papers); `sources/`;
  `calc/` (historical sympy/numpy scripts and arrays); `tasks/` (agent
  prompts); `.claude/`; LaTeX build files; and about 200 further notes, mostly
  D6 wall-source audits and Connes-translation coverage ledgers. Their
  conclusions are condensed in `notes/DeVries_Current_Source_Status_Audit.md`.

## Goal and final conclusion

**Goal.** Replace the quaternionic Hopf carrier S³ → S⁷ → S⁴ (base symmetry
SO(5)) by the Aloff–Wallach bundle SO(3) → X_{1,1} = SU(3)/U(1)_{1,1} → CP²,
whose base stabilizer U(2) has electroweak shape. Verify the claims C1–C7 of
the proposal. Then find a source action that produces the De Vries signed
Hessian, whose electroweak reading gives sin²θ = 0.2231013223.

**Conclusion.**

1. The geometry holds (C1–C4). CP²/conj ≅ S⁴ with branch locus RP²; X_{1,1}
   has fibre SO(3) ≅ RP³ and the Wilking form (SU(3)×SO(3))/U(2); X_{1,1} is
   spin and 3-Sasakian, while CP² needs a spin^c line O(odd). The literature
   anchors (C6) hold after two corrections: the Castellani–D'Auria–Fré paper
   uses the M^{pqr} spaces, and Wilking is Proc. AMS 127 (1999) 1191–1194.
2. The Weinberg-inertia claim (C5) holds inside the simple SU(3). The ratio
   is metric-independent by Schur's lemma and gives tree sin²θ_W = 1/4 with
   k_Y = 3. Standard Model running reaches that value only near 3.6–3.9 TeV.
   Across the two simple factors of SU(3)×SO(3) every coupling ratio is a
   free modulus.
3. The De Vries layer (C7) is correct algebra resting on three postulates:
   c = 1, D†D = j(j+1) with no shift, and the W/Z sector assignment. The
   source search that followed examined about thirty candidate actions and
   closes with the verdict "No current branch derives the unscaled De Vries
   coefficient."
4. Witten's odd-dimension chirality no-go holds on X_{1,1}; the spin^c twist
   leaves it intact.
5. Tree-level ρ = 1 follows from Schur's lemma on the single real U(2)-block
   m_3 ≅ R⁴. This holds for every Wilking modulus and independently of
   De Vries.

Net result: X_{1,1} gives the De Vries labels a geometric home and gives
ρ = 1, and the project produced a precise list of what a source action must
supply. The matrix itself stays underived.

## Valuable ideas and results

1. **The physres5 matrix is the Hessian of a relative gain.** Take
   E(q,p) = ½‖q − P†p‖². The gain G = E(q,0) − E(q,p) = Re⟨q,P†p⟩ − ½⟨p,PP†p⟩
   has Hessian [[0,P†],[P,−PP†]]. On a singular pair with P†P = J this is
   [[0,√J],[√J,−J]].
   *Why:* the baseline subtraction removes the q–q entry (Σ_hh = 0), and one
   norm makes the diagonal the square of the off-diagonal (c = 1). Only the
   spectral statement P†P = J remains to derive. A weighted norm keeps c = 1
   when the same weight enters the baseline. At the algebraic level this
   answers the Hessian-formulation candidate (i) queued in
   `../dvFable/notes/2026-06-12-kkfable-cross-import.md`.
   *Bears on:* A1, D-kernel, D-filter (SUSY-QM origin: one first-order
   operator supplies both entries).
   `notes/Relative_Gain_Source_Action_Admission_Test.md`

2. **Two independent normalization conditions.** In canonical variables the
   block is [[0,αP†],[αP,−βPP†]] with P†P = x0·C₂(j). The De Vries form needs
   β = α² (shape, c = 1) and α²·x0 = 1 (scale).
   *Why:* the secular equation is nonlinear in J, so a common rescaling of
   both Casimirs moves the W/Z ratio. Curator's check (awk): at the De Vries
   point, d sin²θ/d ln x0 ≈ −0.070 and d sin²θ/d ln c ≈ −0.140. Staying
   inside the pole error 0.00026 therefore needs x0 = 1 within about 0.4% and
   c = 1 within about 0.2%. Round SO(3) symmetry fixes anisotropy and leaves
   x0 = γ²/R_A² free.
   *Bears on:* A1, D-kernel (the normalization scale Λ_J).
   `notes/Scale_Absorption_Criterion_For_DeVries.md`,
   `notes/Common_Scale_x0_Moduli_Obstruction.md`

3. **A shift-free Casimir operator exists; geometric Dirac squares carry
   shifts.** The vertical Casimir gradient P = √x0·Σ_i J_i ⊗ e_i on V_j gives
   P†P = x0·C₂(j) with no remainder. Smooth Dirac squares add scalar and
   bundle curvature terms. Kostant's cubic Dirac square is
   C_G − C_H + ‖ρ_G‖² − ‖ρ_H‖². So D†D = j(j+1) is a second postulate of the
   same rank as c = 1.
   *Why:* it narrows which operator can supply Σ_aa = J.
   *Bears on:* A1, D-kernel.
   `notes/Math_Problems_Golden_Rule_J_Candidates.md` (candidates A–H),
   `archive/verification_20260531/T5.md` (verifier correction 1)

4. **Geometric home for the assignment labels.** Under the U(2) isotropy the
   tangent space of X_{1,1} splits as m = m_0 ⊕ m_3. The SU(2)_L Casimir is 2
   on m_0 (adjoint, q8 = 0) and 3/4 on m_3 (doublet, q8 = ±3, Y = ±1/2). The
   parity law q8 ≡ 2I (mod 2) forces half-integer isospin onto odd spin^c
   twists.
   *Why:* J_Z = 2 and J_W = 3/4 are the Casimirs of the two isotropy blocks,
   adjoint and Higgs doublet. The geometry fixes the labels; c, the shift and
   the W/Z channel map stay open.
   *Bears on:* A3, D-EW.
   `archive/verification_20260531/T4.md`, `T5.md` part (c)

5. **Schur-complement form and branch bookkeeping.** Eliminating the second
   channel at spectral parameter λ gives J/(λ + cJ) = λ. The positive root
   obeys a²/(1 − c·a) = K; the negative-root magnitude obeys
   b²/(1 + c·b) = K.
   *Why:* it matches the Schur-complement target of physres5 §06c and keeps
   the vector and scalar branch formulas apart.
   *Bears on:* D-kernel, D-branch.
   `notes/Boundary_Hessian_Schur_Complement_Derivation.md`

6. **De Vries as a custodial refinement.** ρ = 1 (κ_c = κ_n from one m_3
   block) and c = 1 (β = α² from one sewing operator) are independent
   equalities. An action producing both would make De Vries a "special
   custodial situation". The j = 1 sector has to stay a reference or endpoint
   sector, because an m_0 triplet condensate spoils the Z mass relation.
   *Why:* it separates the electroweak ray, which kkorchestra derives on the
   m_3 branch for all Wilking moduli, from the spectral ratio.
   *Bears on:* D-EW (ray admissibility), A3.
   `notes/DeVries_Special_Custodial_Situation.md`,
   `out/M3_DOUBLET_CUSTODIAL_LECTURE.tex/.pdf`

7. **Placement against the spectral Standard Model.** The block form overlaps
   the chiral off-diagonal Dirac structure. c = 1 follows from none of the
   order-one condition, inner fluctuations, or the KO-dimension and
   real-structure signs (checked against Chamseddine–Connes–Marcolli
   hep-th/0610241, arXiv:2001.02902, arXiv:1703.05279).
   *Why:* physres5 cannot import A1 from the NCG axioms.
   *Bears on:* A1.
   `archive/verification_20260531/T5.md` part (b);
   `out/CONNES_NCG_TRANSLATION_KK_PROGRAM.tex/.pdf` (the full translation; it
   names the missing object as a source-derived quadratic form on the
   retained second channel)

8. **Tower criterion for an emergent dimension.** A finite restored multiplet
   (the four m_3 scalars) gives symmetry restoration only. An extra-dimension
   claim needs an infinite labelled family whose gap closes as M_n ~ n/R, with
   the scaling computed from the source (benchmark: Witten hep-th/9503124).
   *Why:* a ready acceptance test for tower and Regge-type claims.
   *Bears on:* D-filter (branch scaling, Regge survival), App-E (the 10 → 11
   step).
   `notes/MTheory_Style_Tower_Test_For_Extra_Dimension.md`

9. **The D5–D6–D7 ladder.** Suspending the Hopf ladder S¹ ← S² → S³ over CP²
   gives D5 = M_5(n) = S(O(n)) ≅ S⁵/Z_n, D6 = the flag Y_6 = SU(3)/T², and
   D7 = X_{1,1}. In total spacetime dimension these are 9/10/11. The
   even-dimensional D6 rung was proposed as the fermion carrier that escapes
   the odd-dimensional chirality no-go through a transition.
   *Why:* the closest worked precedent for the physres5 D = 11/10/9 chain and
   its D = 10 middle line. kkFable tests it and finds an electroweak
   alternation.
   *Bears on:* App-E.
   `out/TRANSITION_1D3D_5D7D.md`, `out/D6_FERMION_BRIDGE.md`,
   `notes/Higgs_Phase_Dimension_Dictionary_Conjecture.md`

10. **CSDR centralizer obstruction on the flag.** Coset-space dimensional
    reduction on SU(3)/T² with parent SU(3)_W leaves only C(T²) = T². The
    electroweak U(2)_W appears only from the one-circle endpoint
    SU(3)/U(1)_8.
    *Why:* an independent reason the D = 10 flag rung cannot host the
    electroweak gauge group.
    *Bears on:* App-E, D-kernel.
    `out/ELECTROWEAK_REDUCTION_STATUS_REPORT.md`

11. **Two competing weak-angle mechanisms.** Killing inertia gives the value
    1/4 at the compactification scale, which running reaches near
    3.6–3.9 TeV. De Vries 0.2231 was read directly as the on-shell ratio.
    *Why:* a geometric coupling ratio is a running-coupling boundary
    condition, so a KK derivation of 0.2231 as a pole ratio must supply
    Δ_match.
    *Bears on:* A2, D-pole.
    `wastebook.md`, `archive/verification_20260531/REPORT.md`, `T5.md`
    (C5-versus-C7 table)

12. **Manton's G₂ CSDR baseline.** Six-dimensional Yang–Mills with gauge
    group G₂ on S² gives θ_W = 30°, λ/g² = 1/6 and m_H = m_Z from one action.
    At the pole, M_W/M_Z = √3/2 misses by about 100σ and m_H misses by
    32 GeV. G₂ enters here as a gauge group, with no holonomy content.
    *Why:* the standard example of a rigid common-source electroweak
    prediction, and of tree ratios failing at the pole. Its quantized version
    gives a threshold target and no De Vries operator.
    *Bears on:* A2, D-branch (scalar functional).
    `notes/Electroweak_Manton_G2_Common_Source_Baseline.md`,
    `notes/Electroweak_Quantized_Manton_DeVries_Small_Run.md`

13. **Lens endpoint and the charge lattice.** The deck group Z_n of the D5
    lens space supplies charge periods and flat characters. Z_5 cannot serve
    as the Standard Model quotient Γ ⊂ Z_6, and the weak angle still needs a
    kinetic normalization.
    *Why:* a concrete test for the physres5 embedding U(1)_geom → U(1)_em.
    *Bears on:* D-branch (α endpoint), App-E (D = 9 endpoint), §08.
    `notes/D5_Lens_Weinberg_EM_Compatibility_Criterion.md`

**Curator's note on the G₂ and Regge routes.** kkorchestra contains no
G₂-holonomy and no Regge-trajectory analysis. Two standard facts, unused in the
project, link its carriers to physres5 §06d. First, the flag manifold SU(3)/T²
(the D6 rung) with its nearly-Kähler metric is the link of a G₂-holonomy cone.
The smoothings of that cone are the Bryant–Salamon metrics on Λ²₋(CP²), and
M-theory on it is treated in Atiyah–Witten, hep-th/0107177. Second, the
squashed Einstein metric on the 3-Sasakian X_{1,1} (Wilking point t = −3/5)
carries a nearly parallel G₂ structure (Friedrich–Kath–Moroianu–Semmelmann,
J. Geom. Phys. 23 (1997) 256). The chirality no-go that kills the smooth
X_{1,1} is the reason the literature moves to singular G₂ spaces.

## Negative results worth keeping

Routes shown dead for deriving the De Vries block on this carrier:

1. **Ordinary KK or geometric-Higgs vacuum Hessian.** The reduced Lagrangian
   gives a positive vector mass matrix G_IJ(T_a q₀)^I(T_b q₀)^J and a scalar
   Hessian. It has no retained second channel and therefore no signed
   two-channel block. A KK route has to add a boundary, interface, defect or
   finite-trace term with its own second field. [D-kernel]
   `notes/Physics_First_KK_Lagrangian_Hessian_Audit.md`

2. **Direct Dirichlet-to-Neumann (Calderón) boundary energy.** On a
   half-cylinder Λ² = x0·C₂(j), so DtN supplies √J. The on-shell energy
   ⟨q,Λq⟩ is positive and first order, and it fixes no c. Finite collars add
   the sector-dependent shift x0·C₂(j)·[coth²(T√(x0·C₂(j))) − 1] (Dirichlet)
   or its tanh analogue (Neumann). [D-kernel, interval/CHM route]
   `notes/Product_Collar_DtN_Normalization_Test.md`

3. **Eliminating the second channel by orthogonal projection.** The reduced
   Hessian becomes a projector with eigenvalues 0 and 1, and the J-dependence
   disappears. A unit auxiliary field gives λ² + λ − K = 0 instead. Both
   channels must be retained when the spectrum is read. [D-kernel: the
   projection onto H_J] `notes/Projection_Gain_Spectral_Obstruction.md`

4. **Symmetry alone.** Unitary sheet exchange and affine mismatch symmetry fix
   the variables and leave c = (τ_m + τ_h)/τ_m² free. [A1]
   `notes/Symmetry_Only_Coefficient_NoGo.md`

5. **Positive local potentials.** det[[0,√J],[√J,−J]] = −J < 0, so the block
   is indefinite. No stable positive boundary, defect or mismatch energy can
   have it as its full Hessian. The negative root needs a signed, constraint,
   Lorentzian or auxiliary reading. [D-branch]
   `notes/Positive_Local_Source_Relative_Gain_Audit.md`

6. **Twenty-seven D6 wall-source candidates:** conical Einstein defects,
   Lovelock and induced-brane gravity, Yang–Mills jump energy,
   eta/determinant/gluing data, determinant polarization, sheet-exchange
   projection, fixed-locus and boundary-Higgs sources with free couplings,
   formal influence covariances, smoothing layers, and finite wall modules
   without a source package. Each yields a positive stiffness, a hard
   projection, or a coefficient chosen after comparison. [D-kernel]
   `notes/DeVries_Current_Source_Status_Audit.md`

7. **Quantized Manton reduction** (one-loop or fuzzy): a legitimate threshold
   target that yields no retained-response operator. [D-kernel]
   `notes/Electroweak_Quantized_Manton_DeVries_Small_Run.md`

8. **Raw CP² (Fubini–Study) inertia** gives 1/4 and cannot produce 0.2231.
   The value 3/8 is unreachable on CP² (it forces irrational charges) and
   belongs to CP³ = SU(4)/U(3), the Pati–Salam coset. [A2] `wastebook.md`
   (R4 entry)

9. **Wilking SO(3) as custodial SU(2)_R.** It has the right algebra and
   breaking pattern, but it acts holomorphically on the fibre m_0 and misses
   the Higgs block m_3 (dim so(4) = 6 > dim u(2) = 4). A physical custodial
   reading needs an assumption about the reduced potential. [D-EW]
   `archive/verification_20260531/T4.md`

10. **Chirality.** The odd-dimensional no-go holds on X_{1,1}. Spin^c repairs
    w₂ of the base and leaves the vector-like pairing intact. This is the
    motivation for the singular-G₂ route. `wastebook.md` (C6 entry)

## Open threads

1. A physical action whose natural observable is the relative gain
   E(q,0) − E(q,p), with one norm and a retained second channel. Candidates:
   an interface effective-action difference, a finite trace, a constraint or
   saddle action, or a determinant/gluing source. This is the central open
   problem. [A1, D-kernel]
2. The scale condition α²·x0 = 1, derived from the same action. [D-kernel]
3. The Dirac/Kostant shift table for the j = 1/2 and j = 1 sectors, showing
   that the shifts cancel or stay small. [A1]
4. The D6 wall covariance A_B (or softness κ_B) in one trace convention: the
   "missing object" of the status audit.
5. Pole placement: never attempted; the De Vries number was read as the
   on-shell ratio by assumption. [A2, D-pole]
6. A scalar functional for the negative branch: none identified. [D-branch]
7. Gauge-boson transport across the D5–D6–D7 transitions (taken up by
   kkFable).
8. A source-derived Higgs quartic: CSDR/Yang–Mills λ = g²/2 overshoots, and
   Manton's 1/6 misses m_H.

## Manifest of copied files

All files are byte-identical copies (`cp -p`, timestamps kept) from
`/home/codexssh/kkorchestra/`, at the same relative paths. Relative links
inside them follow the source layout and resolve only for files copied here.

### Top level and archive

| Path | Bytes | Content |
|---|---:|---|
| `CLAIMS.md` | 1,968 | claims C1–C7 as proposed |
| `wastebook.md` | 17,044 | verification ledger: established, failed, open; per-claim verdicts; R4 note; the "Which SU(3)?" fork |
| `archive/verification_20260531/REPORT.md` | 11,027 | consolidated C1–C7 verdict table |
| `archive/verification_20260531/T4.md` | 23,398 | branching tables, parity law, Casimirs on m_0/m_3, custodial test, verifier pass |
| `archive/verification_20260531/T5.md` | 27,371 | De Vries algebra, c-scan, NCG placement, extra-postulate verdict, verifier pass (keeps the bare D†D = j(j+1) form the project later banned) |

### Notes

| Path | Bytes | Content |
|---|---:|---|
| `notes/DeVries_Current_Source_Status_Audit.md` | 22,231 | final state of the source search; the 27 deleted routes |
| `notes/Relative_Gain_Source_Action_Admission_Test.md` | 6,286 | relative-gain Hessian equals the De Vries block |
| `notes/Boundary_Hessian_Schur_Complement_Derivation.md` | 9,091 | c = β/α², Schur reading, branch equations |
| `notes/Scale_Absorption_Criterion_For_DeVries.md` | 5,028 | β = α² and α²·x0 = 1 |
| `notes/Common_Scale_x0_Moduli_Obstruction.md` | 4,868 | round symmetry leaves x0 free |
| `notes/Math_Problems_Golden_Rule_J_Candidates.md` | 13,143 | candidate operators A–H and open problems |
| `notes/Projection_Gain_Spectral_Obstruction.md` | 6,716 | projection erases the J-dependence |
| `notes/Symmetry_Only_Coefficient_NoGo.md` | 5,367 | symmetry fixes variables; c stays free |
| `notes/Positive_Local_Source_Relative_Gain_Audit.md` | 5,470 | indefinite block versus positive energies |
| `notes/Physics_First_KK_Lagrangian_Hessian_Audit.md` | 5,083 | ordinary KK Hessian lacks the block |
| `notes/Product_Collar_DtN_Normalization_Test.md` | 5,132 | DtN gives √J and no c; finite-collar shifts |
| `notes/DeVries_Special_Custodial_Situation.md` | 8,793 | ρ = 1 versus c = 1 |
| `notes/MTheory_Style_Tower_Test_For_Extra_Dimension.md` | 5,878 | tower criterion for emergent dimensions |
| `notes/Higgs_Phase_Dimension_Dictionary_Conjecture.md` | 5,875 | D7/D6/D5 as symmetric/broken/phase branches (conjecture) |
| `notes/Electroweak_Manton_G2_Common_Source_Baseline.md` | 6,676 | Manton G₂ baseline and pole residuals |
| `notes/Electroweak_Quantized_Manton_DeVries_Small_Run.md` | 10,053 | quantized Manton: threshold target only |
| `notes/D5_Lens_Weinberg_EM_Compatibility_Criterion.md` | 6,063 | lens endpoint, charge periods, Γ ⊂ Z_6 |

### Deliverables (`out/`)

| Path | Bytes | Content |
|---|---:|---|
| `out/TRANSITION_1D3D_5D7D.md` | 7,959 | D1/D2/D3 ↔ D5/D6/D7 ladder dictionary |
| `out/D6_FERMION_BRIDGE.md` | 14,456 | D6 flag rung as fermion carrier (proposal) |
| `out/ELECTROWEAK_REDUCTION_STATUS_REPORT.md` | 14,842 | electroweak reduction report; CSDR centralizer obstruction |
| `out/CONNES_NCG_TRANSLATION_KK_PROGRAM.tex` | 67,064 | NCG translation manuscript, standalone LaTeX |
| `out/CONNES_NCG_TRANSLATION_KK_PROGRAM.pdf` | 450,722 | compiled manuscript (26 pp.) |
| `out/M3_DOUBLET_CUSTODIAL_LECTURE.tex` | 14,073 | lecture on the m_3 doublet and ρ = 1, standalone LaTeX |
| `out/M3_DOUBLET_CUSTODIAL_LECTURE.pdf` | 373,379 | compiled lecture (8 pp.) |

Total: 29 copied files, 1,155,056 bytes, plus this summary. The pandoc PDF of
the status report (115,235 bytes) was dropped during de-duplication, since the
Markdown source above carries the same text.

