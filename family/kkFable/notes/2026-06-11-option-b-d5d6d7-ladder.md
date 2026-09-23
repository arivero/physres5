# N9 — The D5–D6–D7 ladder under Option B: the electroweak alternation

Date: 2026-06-11.

**VERDICT: RE-DERIVED WITH NEW STRUCTURE. Under Option B the ladder
D5 = M_5(n) ← D6 = Y_6 = SU(3)/T² → D7 = X_{1,1} carries gauge content
u(3) / su(3) / su(3)⊕so(3): ranks 3 / 2 / 3 — never the SM's 4. The
electroweak Cartan pair (T₃, Y) is never simultaneously geometric: the
Y-circle is gauged only at D5, the T₃/weak directions only at D7, neither at
D6 (where both are flux indices n, r — exactly the two twists of the prior
D6 fermion bridge). The D5 ↔ D7 transition is an EXCHANGE of which
electroweak direction is isometry and which is background flux. Consequently
the N6 exclusions persist ladder-wide for scalars, and the SM is at best
PHASE-DISTRIBUTED across rungs, never assembled on one. The rank-4
completion within the family is the product/twisted-product direction
(S⁵×S², M^{p,q,r}) — which retroactively explains the inherited "S⁵×S²
priority" rule. (Feeds N10.)**

Conventions: N0. Inputs: prior-out/TRANSITION_1D3D_5D7D.md and
prior-out/D6_FERMION_BRIDGE.md (ladder definitions, cited); N1, N2, N6.

## 1. Ladder data (cited)

- D7: SO(3) → X_{1,1} = SU(3)/U(1)_{1,1} → CP².
- D6: S² → Y_6 = X_{1,1}/SO(2) ≅ SU(3)/T² → CP²; fermion bridge twists:
  base spin^c flux n (generations: ind D_n = (n²−1)/8), vertical monopole
  degree r (r = 1 weak doublet, r = 0 singlet).
- D5: M_5(n) = S(O(n)) → CP², the unit circle bundle of the hypercharge
  line; M_5(n) ≅ S⁵/Z_n for n > 0; n = 1 is the Hopf S⁵.
- Circle relations: S¹ = T²/U(1)_{1,1} → X_{1,1} → Y_6 (D6→D7 restoration);
  D6→D5 collapses each S² fibre to its axis circle (the O(n) phase).

## 2. The two circles inside T²

Expansion block.
- T² ⊂ SU(3) = the diagonal torus, spanned by H8 = diag(1,1,−2) (the
  U(1)_{1,1}/hypercharge direction, T1) and H3 = diag(1,−1,0) (the
  isotropy-SU(2) Cartan; under Option B the weak T₃ axis after the fibre
  identification, N1 §3). B-orthogonal: tr(H8·H3) = 1−1+0 = 0.
- D7 quotients by U(1)_{1,1} only: the H3-circle survives into the coset and
  generates the fibre SO(3)'s Cartan — geometric, gauged. The Y-circle is
  the isotropy — flux only (N2 §4).
- D6 quotients by all of T²: both circles are isotropy — both flux.
- D5 keeps the O(n)-phase circle as the FIBRE of M_5(n): the Y-circle is
  geometric there; the weak directions are gone (the S² collapsed).
- Status: derived (the D5 identification of the fibre circle with the
  U(1)_{1,1} phase is T1's: O(n) is the homogeneous bundle of that circle).

## 3. Per-rung gauge content

Expansion block (one rung per row; KK rule of N1 §4 throughout).

| Rung | Isometry (identity component) | Hand derivation | Option-B gauge content | rank |
|---|---|---|---|---|
| D7 X_{1,1} | SU(3)×SO(3) | N1 §2 (right factor = N(U(1)_{1,1})⁰/U(1)_{1,1} = U(2)/Z = SO(3)); maximality cited (Wilking) | colour + weak; Y flux | 3 |
| D6 Y_6 | SU(3) | N(T²)⁰ = T²: any X ∈ su(3) normalizing t² preserves each root space; ad(t²) is nondegenerate on every root direction, so X ∈ t². Right factor T²/T² = trivial; Weyl group finite. (Maximality of SU(3) as the full isometry of a generic invariant metric: asserted on this normalizer evidence, no independent citation located — flagged; the rank-2 row would survive any finite or rank-preserving enhancement) | colour only; Y AND weak flux (n, r) | 2 |
| D5 M_5(n) | U(3)/Z_n (n>2; at n=1 the full SO(6), n=2 larger than U(3)/Z₂ — both still rank 3) | the round S⁵ ⊂ C³ has Isom = SO(6); for n>2 the centralizer of the deck scalar rotation z·1 (z ≠ z̄) in SO(6) is U(3); quotient acts as U(3)/Z_n. Contains SU(3)×U(1)_Y up to finite quotient: the U(1) factor IS the fibre/O(n)-phase circle | colour + hypercharge; weak absent | 3 |

- The SM needs rank 4 on a single space. Ceiling on the ladder: 3.
- Status: derived; the D6 normalizer and D5 isometry statements were posed
  independently to the GPT-5.5 collaborator (check C) — verdicts in the
  addendum.

## 4. The electroweak alternation theorem

| Rung | Y-circle | weak (T₃/SO(3)) |
|---|---|---|
| D5 | **geometric — gauged U(1)_Y** | absent (flux memory r at best) |
| D6 | flux (n) | flux (r) |
| D7 | flux (n) | **geometric — gauged SO(3)** |

**On no rung are both electroweak directions geometric.** The D5 ↔ D7
transition through D6 exchanges the geometric and flux roles of the two EW
Cartans, with D6 the fully-fluxed middle where both are indices and only
colour is dynamical. Proof = rows of §3 plus §2's circle bookkeeping. ∎

Two readings:
- Option-A comparison: under A the whole EW pair sits inside the base SU(3),
  hence is gauged at every rung — and colour is absent at every rung. The
  alternation is the Option-B face of one and the same rank ceiling; the
  flip relocates the deficit, never removes it.
- The bridge's gauge-sector gap (new open item): the D6 fermion bridge moves
  CHIRAL MATTER between rungs by spectral flow; this theorem shows the
  transitions also create/destroy GAUGE BOSONS (Y appears at D5, W at D7).
  A consistent transition story must say what Higgses/un-Higgses them — the
  gauge-boson analogue of the fermionic spectral flow, nowhere derived in
  the prior corpus. Recorded as an open problem for the bridge programme.

## 5. Colour-singlet pinning persists ladder-wide (scalars)

Expansion block.
- D6: a colour-singlet mode has λ = 1, whose unique weight is (q3, q8) =
  (0,0); the charge-balance condition against the two twists forces n = r =
  0 on that sector. No colour-singlet weak-doublet (r would need to be odd)
  and no colour-singlet hypercharged scalar at D6. Same two-line proof shape
  as N6 Theorem 1, now with two charges. ∎
- D5: SU(3) already acts transitively on S⁵ (hence on S⁵/Z_n), so
  SU(3)-invariant functions are constants: colour-singlet scalar modes carry
  Hopf/U(1)_Y charge 0. No charged colour-singlet scalars at D5. ∎
- D7: N6 Theorems 1–2.
- Fermions evade partially, rung by rung, through the spinor bundle's
  charged components (N6 §3 at D7; check C Q3 examines the D5 lens-space
  spinor — if colour-singlet charged spinor modes exist there, the e_R slot
  that fails at D7 has a natural D5 home as lens/boundary data, matching the
  prior repo's assignment of eta/boundary roles to D5). Verdict recorded in
  the addendum.
- Synthesis (labelled conjecture, not theorem): under Option B the SM
  spectrum is phase-distributed — quark/index sector at D6 (base flux),
  lepton doublets at D7 (fibre spinor twist), hypercharge boson and
  (pending check C) e_R-like data at D5 — with no single rung carrying all
  of it. The exclusion theorems are per-rung statements; the ladder
  satisfies each on a neighbour. Whether transitions can knit these into
  one 4D theory is the bridge programme's open gauge-sector problem (§4).

## 6. The rank-4 completion and the S⁵×S² rule explained

The family's deficit is one circle (or one SU(2)) per rung. The completions
that keep CP²/colour data visible:
- **S⁵ × S²** = M_5(1) × S²: Isom⁰ ⊇ SO(6) × SO(3), and for the lens
  versions M_5(n>1) × S²: (U(3)/Z_n) × SO(3) — rank 4: colour + Y (from the
  S⁵/lens factor) + weak (from the S² factor). This is precisely the
  inherited standing rule "give S⁵×S² priority over S⁷ for Standard-Model
  endpoint diagnostics" (PRIOR-AGENTS.md) — explained: S⁵×S² is the minimal
  member of the CP²-suspended family carrying the full SM rank.
- **M^{p,q,r}**: the twisted version (U(1) bundle over CP²×S², isometry
  SU(3)×SU(2)×U(1), CDF/Witten), where the U(1) charge lattice ties base and
  sphere data — the classic colour-on-CP² KK construction (N2 §6).
Whether these completions also fill the MATTER slots that X_{1,1} lacks
(e_R, Higgs doublet) is N10's question.

## 7. Counterargument pass

1. *"The alternation is an artifact of insisting the EW pair be isometric;
   fluxes are legitimate carriers of quantum numbers."* For charge LABELS,
   yes (that is N6's lattice). For the SM, no: Y and W bosons are observed
   dynamical fields. A rung where they are flux has no photon and no W.
2. *"Maybe a different SO(2) ⊂ SO(3) choice at the D6→D5 collapse keeps
   some weak isometry."* Collapsing S² to any axis circle leaves the same
   lens-space topology; the surviving continuous isometry of the fibre is
   that one circle, and it is the O(n) phase (T1). No SU(2) survives on a
   collapsed fibre.
3. *"D5's U(1) might differ from hypercharge by a colour Cartan admixture."*
   Any admixture of λ_3/λ_8 is fixed by requiring colour-singlet leptons to
   be charged and gluons neutral — which forces the pure fibre-circle
   component, as in N2 §2's centre argument.

## 8. Kill criteria

- A rung metric with isometry strictly larger than §3's (would need to
  evade the normalizer computations; check C re-derived them independently).
- A colour-singlet charged SCALAR harmonic on any rung (contradicts §5's
  two-line proofs).
- For the synthesis conjecture: a no-go showing the D5↔D6↔D7 transitions
  cannot transport gauge-boson degrees of freedom (would kill the
  phase-distribution reading and with it the bridge's Option-B relevance).

## Addendum — collaborator verdicts (check C, completed 2026-06-12)

Provenance note: the first launches of checks C and D (2026-06-11) died
silently (zero output, no surviving process); relaunched 2026-06-12 with
output captured, both completed. Verdicts (GPT-5.5, codex exec, neutral
self-contained prompts):
- **Q1 flag normalizer — CONFIRM.** N_{SU(3)}(T²)⁰ = T² via root
  nondegeneracy; Weyl S₃ finite; connected isometry = (P)SU(3), rank 2.
  (Upgrades §3's flagged D6 row: the no-continuous-right-factor step is now
  independently derived; full maximality of SU(3) remains cited-free but
  rank-safe.)
- **Q2 lens isometry — CONFIRM.** C_{SO(6)}(e^{2πi/n}·1) = U(3) for n > 2
  (deck rotation forces complex-linearity); Isom⁰ = U(3)/Z_n; n = 1 gives
  SO(6), n = 2 gives SO(6)/±1 — all rank 3, as used in §3.
- **Q3 S⁵ spinor charges — CONFIRM (feeds N10).** SU(3)-invariant functions
  on S⁵ are constants; SU(3)-singlet SPINOR modes exist only at half-integer
  Hopf charge c = ±3/2 (double-cover shift; consistent with 4 of
  Spin(6) → 3 ⊕ 1 under U(3) with the factor-2 charge normalization).
- **Q4 monopole harmonics — CONFIRM.** j = |r|/2, |r|/2+1, …; j half-integer
  iff r odd.

## Sources

- prior-out/TRANSITION_1D3D_5D7D.md; prior-out/D6_FERMION_BRIDGE.md (ladder
  definitions, bridge twists (n, r), D5 collapse — all cited as proposals,
  per their own status lines).
- archive/verification_20260531/T1.md (O(n) along U(1)_{1,1}; M_5(n) circle).
- N1 (D7 isometry), N2 (flux-Y), N6 (exclusion theorems).
- PRIOR-AGENTS.md (the S⁵×S² priority rule, here explained).
- Wilking, Proc. AMS 127 (1999) (D7 maximality).
