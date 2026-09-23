# N6 — The hypercharge locus and the matter spectrum under Option B

Date: 2026-06-11.

**VERDICT: RE-DERIVED WITH NEW CONTENT, and it cuts both ways.
Successes: under Option B the hypercharge locus (Y = the U(1)_{1,1}
bundle/twist charge, Y = m/6) reproduces the slots Q_L, u_R, d_R, L, ν_R with
the correct (colour, weak isospin, |Y|) quantum numbers, and the geometry
enforces a Z₆-quotient charge correlation of the same form as the SM's
(6Y determined mod 6 by triality and doublet parity, up to one global
conjugation convention). Failures: (1) no colour-singlet weak-doublet
ELEMENTARY-SCALAR FIELD exists for any twist — the SM Higgs has no
scalar-harmonic slot and must be a connection-component or composite object
(scope sharpened in §2); (2) in the Dirac+line-twist sector, no
colour-singlet weak-singlet fermion with Y ≠ 0 exists — e_R has no slot. Both failures are exact consequences of the
same parity/weight structure that produces the successes. Loophole recorded:
a gravitino-sector (Rarita–Schwinger) mode can fill the e_R slot in 11D-type
embeddings; nothing fills the Higgs slot below the composite route.**

Conventions: N0; Y := m/6 where m is the line-twist charge (normalization
forced by the L slot, §4). Inputs: N2 (parity law, lift = flux), T4 tables,
R5(b) (Dolan–Nash flux reading). Independent verification: two GPT-5.5
collaborator runs (checks A and B; prompts neutral, no repo access), both
reproducing every claim below by hand; their derivations are incorporated
where they were cleaner than mine.

## 1. The mode dictionary (rule used throughout)

Expansion block.
- Domain: 4D KK modes of a field on X = SU(3)/U(1)_{1,1} valued in the
  homogeneous bundle with isotropy module W, twisted by the charge-m line
  O(m). By Frobenius reciprocity/Peter–Weyl, modes are labelled by an
  SU(3)-irrep λ (the 4D colour rep under Option B) together with one
  SU(2)-multiplet inside V_λ ⊗ W obeying the charge-balance condition
  q8(V_λ-weight) + q8(W-component) + m = 0.
- The fibre (weak) isospin I_w of the mode is the combined SU(2) spin of
  that multiplet (T4's rule, re-derived structurally in N2 §3).
- Branching data (T4, verified twice there, plus check A here):
  3 = 2_{+1} ⊕ 1_{−2}; 3̄ = 2_{−1} ⊕ 1_{+2}; 1 = 1_0.
  Spinor module: Δ₇ = 2_{+3} ⊕ 2_{−3} ⊕ 3_0 ⊕ 1_0 (hand derivation in
  check A via so(7) half-spin weights ½(±e₁±e₂±e₃), e₁ ↦ (2I₃,q8) = (2,0),
  e₂ ↦ (1,3), e₃ ↦ (1,−3); same result as the Λ•C²-twist route).
- Spin-content selection (elementary Clebsch–Gordan): I_w = 1/2 arises only
  from 2⊗3, 2⊗1, 1⊗2; I_w = 0 only from 2⊗2, 1⊗1.
- Status: derived (rule cited from T4/standard coset harmonics; all
  applications below are hand computations on this data).

## 2. Theorem 1 — no ELEMENTARY-SCALAR Higgs doublet: colour-singlet weak-doublet scalar FIELDS do not exist

Expansion block.
- Scope (sharpened after adversarial review, 2026-06-11): this theorem
  covers 4D scalars descending from scalar fields on X (isotropy module
  W = 1_0), with arbitrary line twists. It does NOT cover scalars from
  internal tensor components (e.g. W = m_3, the connection/metric
  components): a twisted m_3-valued scalar at λ = 1, m = ∓3 carries
  exactly Higgs quantum numbers (1, I_w = 1/2, Y = ±1/2). So the precise
  statement is: **the Higgs cannot be an elementary scalar harmonic; if it
  exists on this carrier it is a connection-component (CSDR-type) or
  composite object** — which is the same dichotomy the prior repo's
  Electroweak CSDR notes develop.
- Proof for W = 1_0: colour singlet means λ = 1 = 1_0, so V_λ ⊗ W = 1_0:
  the only available multiplet has I_w = 0 and q8 = 0, forcing m = 0.
  A doublet (I_w = 1/2) never occurs, for any integer twist m. ∎
- (Twisting shifts the charge-balance, never the SU(2) content of 1_0⊗1_0.)
- Minimal weak-doublet scalars that DO exist (all coloured):
  (λ = 3, component 2_{+1}, m = −1, Y = −1/6) and conjugate
  (λ = 3̄, 2_{−1}, m = +1, Y = +1/6); next the colour-octet doublets at
  |m| = 3 (T4's m_3 candidate 2_{±3} ⊂ 8 — the Option-A Higgs, here a
  coloured object).
- Consequence: electroweak breaking with unbroken colour has no elementary
  scalar carrier on X_{1,1} under Option B. Feeds N4 (ρ undefined) and N5
  (De Vries j = 1/2 condensate slot is coloured).
- Status: derived; independently confirmed (check B, Q1 — CONFIRM).

## 3. Theorem 2 — no e_R: colour-singlet fermions are weak-doublets at |Y| = 1/2 or singlets at Y = 0

Expansion block.
- Dirac fermions: W = Δ₇ (X_{1,1} is spin, T1; arbitrary extra line twists
  O(m) allowed). Colour singlet: λ = 1, so V_λ ⊗ W = Δ₇ itself.
- I_w = 0 requires the component 1_0 (the only SU(2)-singlet in Δ₇ — the
  3_0 gives I_w = 1, the 2_{±3} give I_w = 1/2): then q8 = 0 forces m = 0,
  Y = 0. So every colour-singlet weak-singlet fermion has Y = 0 (ν_R-like);
  |Y| = 1 (e_R) is excluded. ∎
- I_w = 1/2 requires the components 2_{±3}: then m = ∓3, Y = ∓1/2 — the
  lepton-doublet slot, and only it.
- The exclusion is sharper than the charge-balance bound |q8(Δ₇)| ≤ 3: even
  Y = ±1/2 is unavailable at I_w = 0. The e_R failure is a selection rule
  (I_w = 0 pins the W-component to 1_0), not a near-miss.
- Status: derived; independently confirmed (check B, Q2 — e_R absent).

## 4. The slot table (Dirac + line twists, both conjugation choices)

| SM slot | (colour, I_w, Y)_SM | realization on X_{1,1} | status |
|---|---|---|---|
| Q_L | (3, 1/2, +1/6) | λ=3̄: 2_{−1}⊗3_0 or 2_{−1}⊗1_0 or 1_{+2}⊗2_{−3}, m=+1, Y=+1/6 (conjugate at λ=3, m=−1) | EXISTS |
| u_R | (3, 0, +2/3) | λ=3̄: (2_{−1}⊗2_{−3})_{I_w=0}, m=+4, Y=+2/3 (conjugate at λ=3, m=−4) | EXISTS |
| d_R | (3, 0, −1/3) | λ=3̄: (2_{−1}⊗2_{+3})_{I_w=0} or 1_{+2}⊗1_0, m=−2, Y=−1/3 (conjugate at λ=3, m=+2) | EXISTS |
| L | (1, 1/2, −1/2) | λ=1: 1_0⊗2_{+3}, m=−3, Y=−1/2 (conjugate m=+3) | EXISTS |
| ν_R | (1, 0, 0) | λ=1: 1_0⊗1_0, m=0 | EXISTS |
| e_R | (1, 0, −1) | — | **ABSENT** (Theorem 2) |
| H | (1, 1/2, +1/2) scalar | — | **ABSENT** (Theorem 1) |

Notes. (a) The Y normalization Y = m/6 is forced, not fitted: the L slot
sits rigidly at m = ∓3 and must carry Y = ∓1/2. Given that, Q_L, u_R, d_R,
ν_R land on their SM values with no further freedom — a nontrivial
five-for-five hit on the realized slots. (b) The spectrum is vector-like
(each slot appears with its conjugate), as the Witten no-go demands (N7);
"which conjugate is called the particle" is the single global convention
mentioned in §5. (c) All realizations above were exhibited independently in
check B with the same (λ, component, m) data.

## 5. The Z₆ charge correlation — enforced by the geometry

Expansion block.
- Triality: every weight of V_λ has q8 ≡ t(λ) (mod 3) (t(3) = 1, t(3̄) = 2,
  t(1) = 0; check on 3: {1,1,−2} ≡ 1; on 8: {±3,0} ≡ 0). Every Δ₇ component
  has q8 ≡ 0 (mod 3). Hence 6Y = m = −q8(λ) − q8(W) ≡ −t(λ) (mod 3).
- Parity: q8 ≡ 2I (mod 2) on V_λ (N2 §3b) and on Δ₇ (inspection: 2_{±3}
  odd-odd, 3_0/1_0 even-even); tensor products add both sides mod 2, so
  6Y = m ≡ 2I_w (mod 2).
- Combined (sign corrected after adversarial review, 2026-06-11; the CRT
  combination of −t mod 3 and 2I_w mod 2 is +4t+3(2I_w) ≡ **2·t(λ) +
  3·(2I_w) (mod 6)**): one congruence fixing Y mod 1 from colour triality
  and weak doublet-parity. Every row of §4's slot table satisfies it
  (Q_L: λ=3̄, t=2, 2I_w=1: 4+3 ≡ 1 ≡ 6Y ✓; u_R: 4+0 ≡ 4 ✓; d_R: 4+3·0,
  6Y=−2 ≡ 4 ✓; L: 0+3 ≡ 3 ≡ −3 ✓; ν_R: 0 ✓). The SM's own correlation is
  the t ↦ −t form of the same law, so the geometry enforces the SM
  Z₆-quotient correlation exactly, with one global choice of which of 3/3̄
  is named "quark colour". On a vector-like spectrum (note (b) above) the
  choice is pure convention.
- e_R's residue (6Y ≡ 0) is arithmetically allowed by the congruence; its
  absence (§3) is a finer selection rule, beyond the Z₆ arithmetic.
- Status: derived; this matches check B's form verbatim (the note's first
  printing had the sign of the 2t term wrong; caught by the 2026-06-11
  adversarial review against the slot table and corrected).

## 6. The flux/index side (generation counting), re-derived by hand

Expansion block.
- The Dolan–Nash reading (R5(b)(iii), docs): hypercharge = background
  U(1) flux on CP², spin^c Dirac index on the base counting chiral zero
  modes. Spin^c index with twist c₁(L) = nH on CP²:
  ind D_n = ∫_{CP²} e^{nH/2} Â(CP²), Â = 1 − p₁/24, p₁(CP²) = 3H²,
  ∫ H² = 1: coefficient extraction gives n²/8 − 3/24 = n²/8 − 1/8 =
  **(n² − 1)/8**: n = 1 → 0, n = 3 → 1, n = 5 → 3. Matches the source
  verbatim (review doc lines ~2375–2397 per R5) and R5's two recomputations.
- Option-B meaning: the zero modes counted live on the COLOUR base — they
  are coloured chiral multiplets (quark-like), consistent with §4 where the
  quark slots indeed sit at coloured λ with twists. The lepton slots enter
  through the fibre/spinor structure (m = ∓3 — the Δ₇ components), invisible
  to the base index: base flux counts quarks, fibre spin structure carries
  leptons. A clean Option-B division of labour, new to this note.
- Status: index derived here by hand; the 4D chirality of these modes is
  still killed by the 7D no-go (N7) — the index organizes the spectrum, it
  does not rescue chirality.

## 7. Loopholes and repair paths (named, bounded)

1. **Gravitino sector fills e_R in 11D-type embeddings.** For W = Δ₇ ⊗ m
   (Rarita–Schwinger modes), the component 2_{+3}(Δ) ⊗ 2_{+3}(m₃) ⊃
   (I_w = 0, q8 = +6), giving λ = 1, m = −6, Y = −1: an e_R-like slot.
   Status: comparison/possible completion — requires committing to a
   specific parent supergravity and surviving its own zero-mode counting;
   not part of the present derivation chain.
2. **Composite Higgs.** Colour-singlet weak-doublet bilinears of the §4
   quark slots exist group-theoretically (3̄⊗3 ⊃ 1 with 2⊗1 ⊃ 2, e.g.
   ⟨q̄_{I_w=0} q_{I_w=1/2}⟩ at Y = ±1/2). Whether X_{1,1} dynamics condenses
   them is a strong-coupling question. Status: target for future derivation
   (same path as N4 §6, N5 §5.2).
3. **Higher line twists / other λ** cannot evade Theorems 1–2: both proofs
   quantify over all integer m and use only the I_w-selection rule, which is
   λ-independent for λ = 1.

## 8. Counterargument pass

1. *"The five-for-five slot success is numerology — Y = m/6 was reverse
   engineered."* One normalization constant fitted to one slot (L) and four
   further slots then land correctly with zero freedom, while the same
   structure refuses two slots that the SM does contain. A fit would have no
   reason to fail selectively on e_R and H. The pattern (successes and
   failures from one congruence + one selection rule) is structure, not fit.
2. *"Without a dynamical Y boson (N2), why do these Y labels matter?"* They
   are the charge lattice of the background U(1); they decide whether the
   OPTION-B spectrum could even match SM quantum numbers if the dynamics
   were repaired (M^{p,q,r}-type carrier or otherwise). The answer — yes for
   five slots, never for e_R and H on this carrier — is exactly what the
   ledger needs for the "hypercharge locus" row.
3. *"T4's tables already contained all this."* T4 computed the tables under
   Option A and never asked the colour-singlet questions; Theorems 1–2 and
   the Z₆ law are new consequences extracted for Option B. The tables are
   inputs, not the result.
4. *"Maybe e_R hides in a higher SU(3) rep that is colour-neutral in the
   infrared (confinement)."* A coloured λ confines into hadrons; an
   electron cannot be a hadron of unbroken SU(3)_c (it is colour-blind to
   arbitrary precision). Rejected.

## 9. Kill criteria

- Exhibiting a colour-singlet I_w = 1/2 scalar mode or a colour-singlet
  I_w = 0, Y ≠ 0 Dirac mode on X_{1,1} (would contradict Theorems 1–2;
  both quantified proofs are four lines and checkable by eye).
- A demonstration that the parity law or Δ₇ decomposition fails (both now
  verified by three independent routes: T4's two table-level computations
  and check A's structural/weight derivations).

## Verification

- Collaborator check B (GPT-5.5, codex exec, neutral prompt): Q1 scalar
  exclusion CONFIRM; Q2 slot table — identical realizations, e_R absent
  with the same selection-rule proof; Q3 Z₆ law in equivalent form. No
  refutations. Discrepancies: none; the collaborator's I_w-selection
  phrasing ("I_w = 0 forces the 1_0 component") was adopted in §3 as the
  cleaner argument.
- Internal: §4 slots satisfy §5's congruence (all rows checked by hand);
  §6 index values against the source quotation and R5's recomputations.

## Sources

- archive/verification_20260531/T4.md (+ verification): branching tables.
- archive/verification_20260531/T1.md: X_{1,1} spin; O(n) bundles.
- archive/verification_20260531/R5.md (b)(iii) and verification pass 2
  (the hypercharge-spectrum doubt this note resolves into precise theorems).
- docs/KaluzaKlein_Hilo_Higgsing_KaluzaKlein_Review.md (Dolan–Nash flux and
  index, lines ~2291–2399 via R5's verbatim extraction).
- Collaborator runs: GPT-5.5 via codex exec, 2026-06-11 (checks A, B);
  outputs preserved in the session transcript; treated as independent
  colleague verification, not as derivation sources — every load-bearing
  step is derived in-note.
