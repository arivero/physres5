# OPTION-B VERDICTS — the claim-by-claim ledger

Date: 2026-06-11. Deliverable of the kkFable run (charter: `README.md`).
Question resolved: the **[OPEN FORK, 2026-05-31]** "Which SU(3)?" —
Option A: CP² base = electroweak SU(3) (all prior physics);
Option B: CP² base = colour SU(3)_c, fibre S³/SO(3) = weak SU(2)_L.

This ledger supersedes the stale wastebook state ("R5 NOT YET RUN"; see
provenance note N0): the prior repo's archived R5 run and its two
verification passes are inherited sources; every load-bearing claim entering
a row below was re-derived by hand in the cited kkFable note (no Python; two
independent GPT-5.5 collaborator checks, recorded in N2/N6).

Notes: N0 = baseline audit, N1 = dictionary/rank budget, N2 = U(1)_Y origin,
N3 = Weinberg angle, N4 = custodial, N5 = De Vries, N6 = hypercharge
locus/matter, N7 = chirality (files listed in `notes/README.md`).

## The table

| # | Claim (Option-A wording) | Verdict under Option B | Where derived |
|---|---|---|---|
| C1 | CP²/conj ≅ S⁴; quotient SO(3)- not SU(3)-equivariant | **SURVIVES AS-IS** (identification-independent geometry) | cited: wastebook C1, T1 |
| C2 | X_{k,l} → CP², lens fibre S³/Z_{k+l} | **SURVIVES AS-IS** | cited: wastebook C2 |
| C3 | X_{1,1} fibre SO(3); Wilking (SU(3)×SO(3))/U(2)_Δ | **SURVIVES AS-IS**; the right-SO(3) re-derived by hand | N1 §2; cited: Wilking, T2 |
| C4 | CP² spin^c; X_{1,1} spin; SO(3)→Sp(1) lift obstruction "is where hypercharge enters" | geometry **SURVIVES**; the hypercharge reading **RE-DERIVED**: the obstruction-completing U(1) and the base flux line are ONE circle (U(1)_{1,1}), proven via the parity law — but it is background-only (see U(1)_Y row) | N2 §3 (proof), N2 §4 (kill) |
| C5 | θ_W = Killing-inertia ratio, non-arbitrary; tree sin²θ_W = 1/4 | **DEAD.** Strictly: no dynamical U(1)_Y on X_{1,1} ⇒ θ_W undefined. Counterfactually: sin²θ_W = (1+t)/((1+t)+k_Y), a free Wilking modulus — no rigidity survives the cross-factor split | N3 (hand derivation); inherits T3d caveat |
| — | **U(1)_Y origin** (charter attack-first item: fibre-lift U(1) — prove or kill) | **PROVEN as structure, KILLED as dynamics.** The U(2)-lift U(1) ≡ spin^c/Dolan–Nash flux U(1) ≡ U(1)_{1,1} (theorem, via ζ-parity law); it acts trivially on X ⇒ no Killing vector ⇒ no 4D Y boson. All rivals killed by hand (colour-λ₈: Z(su(3)) = 0; bare lift: no new Cartan; Betti U(1): no charged light states). Rank budget 4 > 3 confirmed | N2; N1 §4 |
| — | **Hypercharge locus** | **RE-DERIVED WITH NEW CONTENT.** Y = m/6 on the U(1)_{1,1} twist charge (normalization forced by the L slot). Geometry enforces the SM Z₆ correlation 6Y ≡ −2t(λ) + 3(2I_w) mod 6 (up to one conjugation convention). Slots Q_L, u_R, d_R, L, ν_R: all EXIST with correct quantum numbers. Background charge lattice only (no boson, C5/U(1)_Y rows) | N6 §4–5 |
| — | **Matter spectrum completeness** (new row) | **FAILS — two exclusion theorems.** (1) No colour-singlet weak-doublet ELEMENTARY-SCALAR FIELD for any twist ⇒ the Higgs has no scalar-harmonic slot (a connection-component/CSDR or composite Higgs is the named escape — scope per N6 §2, sharpened 2026-06-11 review). (2) Colour-singlet fermions: I_w = 1/2 forces Y = ∓1/2 (= L), I_w = 0 forces Y = 0 (= ν_R) ⇒ **no e_R slot**. Loopholes recorded: gravitino sector can fill e_R in 11D-type embeddings; composite (q̄q) Higgs — both outside the derivation chain | N6 §2–3, §7 |
| — | **Custodial T4** | **DEAD.** No spectator: centralizer of su(3)⊕so(3) in itself = 0; Option B gauges both factors. T4's so(4) structure survives as geometry but its "custodial" factor becomes the weak group itself; and ρ is undefined for lack of a colour-singlet doublet | N4 |
| C7 | De Vries signed Hessian; EW assignment (j=1/2, j=1) ⇒ sin²θ_W = 0.2231 | algebra **SURVIVES** (identification-independent; eigenvalues re-checked by hand); EW assignment **DEAD**: the j = 1/2 condensate slot is colour-charged; inverted assignment excluded (cos²θ_W > 1). 0.2231 detaches from any observable. c = 1, D†D = j(j+1) postulates: unchanged, still open | N5 |
| C6 | Literature anchors (Witten 1981; CDF M^{p,q,r}; Weinberg 1983) | **SURVIVE, RE-POINTED.** Under Option B the CDF/Witten M^{p,q,r} family (isometry SU(3)×SU(2)×U(1), rank 4, colour on CP²) is the natural literature home of the gauge content; X_{1,1} trades the hypercharge circle for the SO(3) fibre. Aloff-Wallach trichotomy: k=l → colour+weak, no Y; k≠l → colour+Y, no weak; never all three | N2 §6; wastebook C6 correction |
| — | Breaking pattern (R5(a)) | **SURVIVES, SHARPENED.** Unbroken colour = unbroken base isometry remains Option B's structural gain; but squashing breaks nothing (all g_t fully invariant), so EW breaking needs a charged vev — and the only doublet vevs available are coloured (matter row) | N1 §5, N6 §2 |
| — | Chirality (Witten odd-dim no-go) | **UNCHANGED OBSTRUCTION** (both options): spectrum vector-like; spin^c does not evade; identification-independent | N7; cited: T6 |

## Resolution of the fork

**Option B is DEAD on X_{1,1} as a Standard-Model carrier.** Three
independent structural absences, each a short hand-proved theorem on this
carrier, would each suffice:

1. no dynamical hypercharge boson (rank 4 > 3; the unique candidate circle
   is the quotiented isotropy circle — N2);
2. no elementary-scalar Higgs slot (colour-singlet weak-doublet scalar
   fields do not exist — N6 Theorem 1, scoped to scalar fields; a
   connection-component or composite Higgs remains the only route);
3. no e_R slot (colour-singlet fermions are pinned to Y = 0 or the L
   doublet — N6 Theorem 2);

with the chirality no-go (N7) outstanding in both options on top. Both
inherited sharp numbers die under Option B: the rigid 1/4 (N3) and the De
Vries 0.2231 (N5). R5's headline trade — "colour gained, 1/4 lost" — was an
understatement; the full price list is: colour gained; 1/4 lost, 0.2231
lost, the Y boson lost, the Higgs slot lost, e_R lost.

**What Option B gets right is equally sharp**, and survives as the
constructive residue of this run:
- the breaking-pattern reading (unbroken colour = base isometry) — the one
  structural point where B beats A (N1 §5);
- the lift-obstruction = flux identity: hypercharge, weak doublet-ness and
  the spin^c repair are one Z₂-correlated structure (N2 §3), whose
  fingerprint is the SM's own Z₆ charge correlation (N6 §5);
- five of seven SM matter slots with the correct (colour, I_w, Y), with the
  Y normalization forced, and a clean division of labour — base flux indexes
  the quarks, fibre spinor structure carries the leptons (N6 §4, §6).

**The geometry forces neither identification (R5), but SM-completeness
forces the choice on this carrier:** Option A is the only self-consistent
reading of X_{1,1} (a predictive, colourless electroweak toy: rigid 1/4 or,
with the De Vries postulates, 0.2231); Option B's gauge content lives
naturally on the M^{p,q,r} family instead, where colour-on-CP² plus a
genuine hypercharge circle is the classic construction. The fork is
resolved: **flip the carrier, not the labels** — on X_{1,1} the flip
fails for enumerated, theorem-level reasons; pursuing Option-B physics means
moving to a rank-4 carrier (M^{p,q,r}-type) or paying for the missing pieces
dynamically (composite Higgs, gravitino-sector e_R), each a named target for
future derivation, none performed by the present geometry.

## Continuation findings (same date, post-deliverable run "towards discovery")

Two further notes extend the ledger beyond the charter; sources downloaded
and digested in `sources-local/`:

- **N9 (D5–D6–D7 ladder):** gauge content per rung is u(3) / su(3) /
  su(3)⊕so(3) — ranks 3/2/3, never 4; the electroweak pair alternates
  (Y gauged only at D5, weak only at D7, both flux at D6). New open problem
  for the prior D6 fermion-bridge programme: its rung transitions must
  transport GAUGE BOSONS, not only chiral matter. The inherited "S⁵×S²
  priority" rule is explained as the family's minimal rank-4 completion.
- **N10 (rank-4 carrier test):** COMPLEMENTARY EXCLUSION. The carriers that
  fix the gauge rank lose the matter mechanism: M^{111} (Fabbri–Fré,
  computed) gauges SU(3)×SU(2)×U(1)_R + a Betti U(1)' with every KK state
  neutral under it (verbatim — retro-anchoring the N2 Betti kill), but
  admits NO SU(2) doublets at any level (J ∈ N), no quark/lepton slots, and
  its only massless charged colour/weak singlets are the two gravitini
  (y = ±1) — the same gravitino-borne e_R pattern N6 §7 found on X_{1,1}.
  The Higgs-doublet slot fails on every homogeneous carrier examined
  (charge-locking lemma): within this family the SM Higgs cannot be an
  elementary scalar harmonic — connection components (CSDR), composites, or
  finite/fuzzy modules are forced.
- **Literature alignment (Dolan–Nash digests):** their SM-from-CP²×CP³
  spectrum (with e_R at the q = −3 canonical spin^c twist) gauges HOLONOMY,
  never the CP² isometry — Option-A-shaped, with colour on the CP³ factor;
  consistent with, and explanatory of, Option B's e_R failure.

## Second continuation (2026-06-12): the slots close, the obstructions sharpen

- **N11:** within the same equivariant framework as N6, the two missing
  slots are filled by the larger supergravity field menu: e_R from the
  internal gravitino components (Δ₇⊗m has exactly one 1_{±6} colour-singlet
  — at twice the lepton twist, the canonical-bundle locus; survives
  gravitino gauge fixing) and the Higgs from twisted internal tensors
  (Λ³m, Sym²m doublets at odd charge). The charge-doubling mechanism is
  X_{1,1}-specific (fails on S⁵×S²: check E). All seven SM slots now exist
  on X_{1,1} under Option B; the irreducible obstructions reduce to exactly
  two carrier-level facts: **no dynamical U(1)_Y (N2) and no chirality
  (N7).**
- **N12:** the D7→D6 transition derived: quintet (I_w = 2) metric order
  parameter Higgses W^±; charges convert to fluxes (r = 2I₃); dynamics
  exits two ways at once — the broken pair through a diverging vev
  (infinite moduli distance), the surviving abelian through diverging
  coupling at zero mass. The restoration direction passes the inherited
  M-theory-style tower test by construction (the 10↔11-type critical jump);
  the t-axis two-Einstein-point structure is the seed of the hat-formation
  (criticality) analysis; D6↔D5 remains open, organized by the
  vev-vs-coupling dichotomy.
- Deliverable of this phase: the didactic paper in `out/` (LaTeX + PDF).

## Audit against the charter

- θ_W = 1/4: row C5 — re-derived, dead (N3). ✓
- hypercharge locus: dedicated row — re-derived with new content (N2/N6). ✓
- custodial T4: dedicated row — dead (N4). ✓
- De Vries EW assignment: row C7 — dead, algebra survives (N5). ✓
- known obstruction (U(1)_Y origin, fibre-lift candidate): dedicated row —
  proven as structure, killed as dynamics (N2). ✓
- C1–C4 carried over by citation, not redone. ✓
- Every row points to a derivation note; every note carries its
  counterargument pass and kill criteria; no symlinked file was written.
