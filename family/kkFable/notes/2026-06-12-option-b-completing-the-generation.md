# N11 — Completing the generation on X_{1,1}: e_R from gravitino components, the Higgs from internal tensors, and the charge-doubling mechanism

Date: 2026-06-12.

**VERDICT: RE-OPENED IN OPTION B's FAVOUR (slot level). Within the
equivariant-bundle framework that already underlies N6 (fields = sections of
homogeneous bundles W ⊗ O(m) on X_{1,1}, m = background flux number), the two
missing matter slots are filled by enlarging W beyond scalars and Dirac
spinors: (1) the internal gravitino components ψ_m (W = Δ₇⊗m, 4D spin-1/2)
contain the e_R slot — a colour-singlet weak-singlet at exactly twice the
lepton-doublet charge, |Y| = 1 in the SAME normalization Y = m/6 that N6
fixed on L; (2) twisted internal-tensor scalars (W = Λ³m, the 3-form
components A_{mnp}, and W = Sym²m, metric components) contain the Higgs slot
(1, I_w = 1/2, |Y| = 1/2). The mechanism for (1) is a charge doubling
special to X_{1,1}: the spinor and tangent bundles share the same charged
doublet 2_{±3}, and 2⊗2 → 1 adds the charges; carriers whose tangent charge
is too small (S⁵×S²) provably cannot double, and M^{111}'s computed spectrum
realizes its only charged singlets as gravitini — the cross-carrier pattern
of N10 §4 now has a mechanism. The two irreducible Option-B obstructions
that remain are exactly N2's (no dynamical Y boson) and N7's (chirality).**

Conventions: N0; Y = m/6 throughout (the N6 normalization). Inputs: N6
(mode dictionary, Δ₇, slot table), N10 §4 (gravitino pattern), T1, T2.
Framework status: equivariant model building with background U(1) flux —
the same premise N6's slot table already uses (stated there in §1); pure
11D supergravity provides the W-menu below but only the m = 0 column of
twists.

## 1. The Rarita–Schwinger module: W = Δ₇ ⊗ m

Expansion block.
- m_C = 3_0 ⊕ 2_{+3} ⊕ 2_{−3} (complexified tangent: fibre m_0 = 3_0,
  base m_3 = 2_{+3} + conjugate); Δ₇ = 2_{+3} ⊕ 2_{−3} ⊕ 3_0 ⊕ 1_0 (N6 §1).
  In 11D-type supergravity the internal components ψ_m of the gravitino are
  4D SPIN-1/2 fermions valued in this W (the 4D spin-3/2 states sit in ψ_μ,
  W = Δ₇ — N6's Dirac column). The e_R candidate below is therefore an
  ordinary spin-1/2 fermion, not a 4D gravitino.
- Full decomposition of Δ₇ ⊗ m_C by (2I+1)_q sectors (dim 56):
  q = ±6: (1 ⊕ 3) each [from 2_{±3}⊗2_{±3}];
  q = ±3: (2 ⊕ 4) ⊕ (2 ⊕ 4) ⊕ 2 each [2_{±3}⊗3_0, 3_0⊗2_{±3}, 1_0⊗2_{±3}];
  q = 0: (1 ⊕ 3) ⊕ (1 ⊕ 3) ⊕ (1 ⊕ 3 ⊕ 5) ⊕ 3
  [2_{+3}⊗2_{−3}, 2_{−3}⊗2_{+3}, 3_0⊗3_0, 1_0⊗3_0].
  Dimension check: 2(1+3) + 2(6+6+2) + (4+4+9+3) = 8 + 28 + 20 = 56. ✓
- Colour-singlet (λ = 1) slot menu, by twist (charge balance q + m = 0):

| twist m | (I_w, Y) content from Δ₇⊗m | SM reading |
|---|---|---|
| ∓6 | (0, ±1) ⊕ (1, ±1) | **e_R slot** ✓ + weak-triplet exotic at |Y| = 1 |
| ∓3 | 2×(1/2, ±1/2) ⊕ 2×(3/2, ±1/2) ⊕ (1/2, ±1/2) | extra L-type doublets + I = 3/2 exotics |
| 0 | 3×(0,0) ⊕ 4×(1,0) ⊕ (2,0) | ν_R-type + neutral exotics |

- The e_R slot: (λ = 1, I_w = 0, Y = ±1) at twist m = ∓6 — twice the
  lepton-doublet twist, hence |Y(e_R)| = 2|Y(L)| = 1 in the SAME unit N6
  fixed. No new normalization freedom is consumed. ∎
- Status: derived (independent collaborator verification, check E Q1 —
  addendum).

## 2. The charge-doubling mechanism, and why it is special

Expansion block.
- On X_{1,1} the charged piece of the SPINOR module and the charged piece of
  the TANGENT module are the same U(2)-type doublet 2_{±3} (both faces of
  m_3; T4/N6). The SU(2) Clebsch–Gordan 2 ⊗ 2 ⊃ 1 then produces an
  SU(2)-singlet at the SUM of the charges: 1_{±6}. Charge doubling requires
  (i) equal charges on the two factors and (ii) a singlet in their product.
- S⁵ contrast (verified, check E Q3): there Δ₅ = 1_{−1} ⊕ 2_0 ⊕ 1_{+1} and
  m_5 = 2_{+1} ⊕ 2_{−1} ⊕ 1_0 — the spinor's charged pieces are SINGLETS
  and the tangent's charged pieces are DOUBLETS: 1 ⊗ 2 contains no singlet,
  and the 2_0 ⊗ 2_{±1} singlets sit at charge ±1, not ±2. The colour-singlet
  menu stays at c = ±3/2 (N10 §5): no doubling, no e_R, even in the
  gravitino sector. The N10 §4 pattern ("e_R is gravitino-borne, and only
  where the base charge is large enough") is now a theorem-level mechanism:
  **e_R needs the tangent and spinor bundles to share one odd-charged
  doublet — the signature of the CP² spin^c geometry of X_{1,1}.**
- Canonical-bundle reading: 1_{+6} = Λ²(2_{+3}) ⊗ (paired spinor) — the
  charge 6 is 2 × 3 = 2 × c₁-charge of K_{CP²}^{1/2}-shifted structures;
  on CP² itself Dolan–Nash place e_R at the canonical twist q = −3 = K
  (digest, hep-th/0207078 §3.3). The X_{1,1} slot at m = ∓6 is the 7D
  avatar: the electron singlet persistently sits at the canonical-twist
  locus of the spin^c geometry. Status: comparison (exact on CP², slot-level
  on X_{1,1}).

## 3. The Higgs slot from internal tensors: W = Λ³m and Sym²m

Expansion block.
- Λ³(m_C) decomposition (dim 35 = C(7,3); derivation by
  Λ³(A⊕B⊕C) = ⊕ Λ^aA⊗Λ^bB⊗Λ^cC, a+b+c = 3):
  1_0 [Λ³3_0] ⊕ (2⊕4)_{±3} [Λ²3_0⊗2_{±3}] ⊕ 3_{±6} [3_0⊗Λ²2_{±3}] ⊕
  (3 ⊕ 1 ⊕ 3 ⊕ 5)_0 [3_0⊗(2_{+3}⊗2_{−3}); Λ³ of the ±3 pair] ⊕
  **2_{±3}** [Λ²2_{±3} ⊗ 2_{∓3}].
  Dimension check: 1 + 12 + 6 + 12 + 4 = 35. ✓
- Twisted 3-form scalars at λ = 1, m = ∓3 pick the 2_{±3} (and (2⊕4)_{±3})
  components: **(1, I_w = 1/2, Y = ±1/2) — the Higgs slot.** Sym²(m) gives
  doublets at the same odd charges through 3_0 ⊗ 2_{±3} (metric components
  g_{(fibre,base)}). ∎
- Reading: the locking lemma (N10 §2) said function-scalars can never carry
  the Higgs's quantum numbers; this section says internal-TENSOR scalars can
  — the Higgs, if present at all, is forced to be an internal-geometry mode
  (a metric or form-field component along charged internal directions).
  This is the structural reason the literature's working constructions put
  the Higgs in the internal gauge-field/connection components (CSDR,
  gauge-Higgs unification): not a modelling preference but a selection rule.
- Status: derived (check E Q2 — addendum); the identification of WHICH
  tensor mode (3-form vs metric vs a connection in an enlarged framework)
  survives dynamics is open and belongs to the mass-spectrum question, not
  the slot question.

## 4. What remains irreducible

With §1–§3, every SM matter and Higgs SLOT exists on X_{1,1} under Option B
(Q_L, u_R, d_R, L, ν_R: N6; e_R: §1; H: §3). The surviving obstructions are
exactly two, and both are slot-independent:
1. **No dynamical U(1)_Y** (N2: rank 4 > 3; the Y circle acts trivially).
   No enlargement of W changes the isometry group.
2. **Chirality** (N7: the 7D no-go pairs every slot with its conjugate).
Both live at the level of the carrier itself — which is what the ladder
analysis (N9, N12) is about: the rungs that have the Y boson or the chiral
index are different spaces.

## 5. Counterargument pass

1. *"With W large enough anything fits — this is slot inflation."* The menu
   of W is not free: scalars from W = 1, Sym²m, Λ^k m and fermions from
   W = Δ₇, Δ₇⊗m exhaust the bosonic/fermionic content of gravity-plus-flux
   on X_{1,1} (metric, p-forms, gravitino). Within that fixed menu the slots
   appear at specific twists with no further choices, and the failures of
   N6 remain failures in their sectors (e.g. there is still no e_R among
   Dirac fermions, no Higgs among function scalars). The non-trivial
   statement is that the SUGRA field content is exactly enough — and that
   it fails to be enough on S⁵×S² (§2): inflation would not distinguish
   carriers.
2. *"The exotics (weak triplet at |Y| = 1, I = 3/2 states, the 5_0) are
   phenomenological poison."* They are KK-tower companions; whether they
   are heavy or light is a mass-spectrum question outside slot analysis —
   flagged, not resolved. The honest statement: the slot table is necessary,
   not sufficient.
3. *"ψ_m modes are gauge-variant (gravitino gauge transformations eat some
   components)."* True: κ-symmetry/gravitino gauge fixing removes the
   γ-trace and longitudinal parts of Δ₇⊗m. The removed piece is one Δ₇
   (γ-trace) — subtracting Δ₇'s singlet content (charges 0, ±3 sectors at
   I_w = 1/2... explicitly: 2_{±3} ⊕ 3_0 ⊕ 1_0) does NOT touch the q = ±6
   singlets, which arise only in Δ₇⊗m. The e_R slot survives gauge fixing. ∎
4. *"Why trust slot-level statements at all?"* They are the
   identification-dependent part of the programme — what died for Option B
   in N6 and what revives here. Masses, potentials, and chirality are the
   carrier-level part; §4 keeps them explicitly separate.

## 6. Kill criteria

- A computation showing the q = ±6 singlets of Δ₇⊗m are removed by the
  supergravity constraints (would kill §1; §5.3 checks the γ-trace, the
  remaining freedom is the longitudinal δψ_m = ∇_m ε with ε ∈ Δ₇ — also
  charge-bounded by ±3, so it cannot reach ±6 either).
- A carrier with small tangent charge exhibiting charge doubling (would
  break the §2 mechanism).
- An SM-quantum-number slot needed beyond the W-menu of §5.1 (would revive
  the slot-inflation charge).

## Addendum — collaborator verdicts (check E, completed 2026-06-12)

GPT-5.5 (codex exec, neutral prompt), all items CONFIRM:
- **Q1 (Δ₇⊗m):** decomposition reproduced; by charge: (1⊕3)_{±6},
  (3·2 ⊕ 2·4)_{±3}, (3·1 ⊕ 4·3 ⊕ 5)_0; dim 4+4+14+14+20 = 56; singlet
  content exactly 1_{+6} ⊕ 1_{−6} ⊕ 3·1_0 — the e_R slot is unique per
  sign. (§1's table restates this by twist.)
- **Q2 (Λ³m):** confirmed, with the doublet census sharpened: TWO doublet
  copies at each odd charge (2·2_{±3} ⊕ 4_{±3}); dim 13+8+8+3+3 = 35.
- **Q3 (S⁵ contrast):** singlet content of Δ₅⊗m₅ is 2·1_{+1} ⊕ 2·1_{−1};
  the doubled-charge pieces 2_{±2} are doublets, not singlets — no
  extension of the colour-singlet menu; the doubling mechanism of §2 is
  confirmed as an X_{1,1}-specific feature.
- **Q4 (charge → flux):** under collapse of the right U(1) ⊂ SU(2), the
  weight m_R becomes monopole charge r = 2m_R on S² (4π fibre period).
  Used in N12 §3.

## Sources

- N6 (dictionary, Δ₇, normalization), N10 §4 (pattern), N2/N7 (the two
  irreducible obstructions).
- sources-local/DolanNash_SM_Fermions_From_CPN_hep-th_0207078.md (e_R at the
  canonical twist on CP²).
- sources-local/FabbriFre_M111_Spectrum_hep-th_9903036.md (M^{111} charged
  singlets = gravitini).
- archive/verification_20260531/T1.md, T2.md (bundle and metric data).
