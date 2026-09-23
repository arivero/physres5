# N2 — Where does U(1)_Y come from when the base is colour?

Date: 2026-06-11.

**VERDICT: The charter candidate — "the fibre SO(3)→SU(2) lift obstruction as
the U(1) completing electroweak" — is PROVEN as structure and KILLED as
dynamics. Proven: the U(1) that completes the fibre SO(3) to U(2) exists, is
forced on every weak-doublet sector, and is literally the same circle as the
base spin^c/Dolan–Nash flux line (one U(1)_{1,1}, two faces; the parity law
q8 ≡ 2I mod 2 is its fingerprint). Killed: that circle is the quotiented
isotropy circle of X_{1,1}; it acts trivially on the carrier, has no Killing
vector, and so yields NO massless 4D hypercharge boson. Every alternative
candidate dies by hand computation below. Under Option B on X_{1,1},
hypercharge exists only as a background bundle charge — there is no dynamical
U(1)_Y. (Sharpens R5(b) and confirms R5 verification pass 2 without computer
algebra.)**

Conventions: N0. Inputs: N1 (right-SO(3) derivation, rank budget), T1 (spin^c
line L = O(k), k odd), T4 (branching tables, parity law — re-proven here
structurally), R5 (prior triage).

## 1. The candidate list

(i) the bare double-cover lift SO(3) → SU(2) of the fibre;
(ii) a Cartan direction of the colour SU(3) (λ_8-as-Y, or B−L inside SU(3)_c);
(iii) the charter candidate in strong form: the U(2)-style lift of the fibre,
SO(3) → U(2) = (SU(2)×U(1))/Z₂, spin^c-analogous;
(iv) the Dolan–Nash background flux on the base = T1's spin^c line O(k);
(v) a Betti/p-form U(1) (gauge boson from a higher-form field on a harmonic
2-form);
(vi) carrier modification (out of scope as a fix; surveyed as repair path §6).

## 2. Kills by hand: (i) and (ii)

Expansion block (i) — bare lift adds no U(1).
- The double cover SU(2) → SO(3) has discrete kernel Z₂. rank SU(2) = rank
  SO(3) = 1: passing to the cover adds no Cartan generator, hence no new gauge
  boson; it only admits half-integer-I representations. Whatever supplies a
  hypercharge generator, the bare lift cannot. Status: derived (one line).

Expansion block (ii) — no hypercharge inside colour.
- Requirement: Y must commute with every unbroken colour generator (leptons
  carry Y and no colour; gluons carry no Y), i.e. Y ∈ centre of su(3)_c.
- Calculation: su(3) is simple; its centre as a Lie algebra is 0. (Directly:
  a diagonal traceless generator diag(a,b,c) commuting with the root vectors
  E_{12}, E_{13} forces a=b=c, hence 0.) So no Y inside su(3)_c. Gauging a
  non-central direction (e.g. H8 = diag(1,1,−2), which fails to commute with
  the four root directions E_{13}, E_{23}, E_{31}, E_{32} — its ad-eigenvalues
  there are ±3) would make Y a coloured generator and its massless gauging
  would single out a colour direction, breaking SU(3)_c. Status: derived;
  agrees with R5(b)(ii).
- B−L variant: B−L commutes with colour but is not contained in su(3)_c at
  all (it is a flavour/baryon-number charge, not a Killing direction of the
  carrier); as a 4D gauge boson it would need its own Killing vector, which
  the rank budget (N1 §4) shows does not exist. Killed by the same count.

## 3. The charter candidate, strong form: the U(2)-lift U(1) — proven as structure

The bare-lift kill (i) leaves the candidate the charter actually points at:
repairing the SO(3)→SU(2) lift obstruction the spin^c way, by enlarging to

  U(2) = (SU(2) × U(1)) / Z₂ ,

so that half-integer fibre isospin is allowed at the price of a correlated
U(1) charge. Three statements, each derived by hand:

**(3a) Weak-doublet sectors on X_{1,1} are forced to carry the U(2)-lift, and
its U(1) charge is the bundle charge n.**

Expansion block.
- Variables/domain: charge-n homogeneous line bundle O(n) = SU(3) ×_{U(1)} C_n
  over X (equivalently pulled back data along the λ_8/H8 direction; T1);
  sections Γ(O(n)); the right U(2)-action from N1 §2.
- Action: for u ∈ U(2) ⊂ N_{SU(3)}(U(1)_{1,1}), right translation x ↦ xu maps
  fibres of O(n) to fibres; because U(1)_{1,1} = Z(U(2)) is central, the
  character z^n is preserved and the action on Γ(O(n)) is by the full U(2),
  with the central circle acting by multiplication by z^n. On X itself only
  U(2)/Z = SO(3) acts (N1 §2); on charge-n sections the genuine actor is U(2).
- Readout: the fibre symmetry on charged sections is the U(2)-lift of the
  fibre SO(3), and the lift's U(1) charge IS n. Status: derived.

**(3b) The parity law q8 ≡ 2I (mod 2) is the fingerprint of the Z₂ in
(SU(2)×U(1))/Z₂ — one-line structural proof.**

Expansion block.
- The element ζ := exp(iπ H8) = diag(−1,−1,1) ∈ SU(3) lies in U(1)_{1,1}
  (z = −1) AND equals the element −1₂ of the SU(2) block (upper block −1₂,
  lower entry det(−1₂)^{-1} = 1). One group element, two evaluations on any
  weight state of any SU(3)-irrep:
  as exp(iπH8): e^{iπ q8} = (−1)^{q8};  as −1₂ ∈ SU(2): (−1)^{2I}.
  Equality of the two gives (−1)^{q8} = (−1)^{2I} on every state. ∎
- This re-proves T4's parity law (there verified state-by-state through the
  branching tables, twice) without tables. Consequence: I half-integer ⇔ q8
  odd ⇔ the section needs O(odd) — the T1 spin^c-repair condition. The Z₂
  identified in U(2) = (SU(2)×U(1))/Z₂ is ζ.
- Status: derived. Cross-check: every row of T4's tables satisfies it.

**(3c) Lift-U(1) ≡ base flux U(1): one circle, two faces.**

The U(1) of the U(2)-lift (3a) acts by the character z^n of U(1)_{1,1}; the
Dolan–Nash flux line / T1 spin^c line O(k) is the homogeneous bundle of the
same circle U(1)_{1,1} along the same H8 direction (T1; R5(b)(iii)). They are
the same U(1) with the same charge label. So the charter's "U(1) completing
electroweak from the fibre-lift obstruction" and the "hypercharge flux on the
colour base" are not two candidates; they are one object: the isotropy circle
U(1)_{1,1}, seen from the fibre side as the lift-completing U(1) and from the
base side as the spin^c/flux line. The parity law is the statement that the
two faces are glued by ζ. Status: derived.

This is the **proof half** of "prove it or kill it": Option B's hypercharge,
if it exists at all, is necessarily this circle, and it comes with the
doublet/odd-charge correlation that the SM in fact has (developed
quantitatively in N6).

## 4. The kill half: that circle is not dynamical on X_{1,1}

Expansion block.
- The circle U(1)_{1,1} is the isotropy subgroup divided out in X = G/H. Its
  right action on X is trivial by construction (xH·h = xH). A trivial action
  has zero Killing vector field; the KK ansatz produces one massless 4D gauge
  boson per Killing vector (N1 §4 rule). Hence: **no 4D gauge boson for this
  U(1).** It acts on bundles over X (charges, holonomies, characteristic
  classes), never on X.
- Independent confirmation by counting: N1 §4's rank budget (3 available, 4
  needed; centralizer closure) — re-derived there by hand — leaves no Cartan
  room regardless of which circle one tries to gauge.
- Status: derived. This upgrades R5's "external bundle datum, an extra
  assumption" to the sharp form of its verification pass 2: a missing gauge
  boson, structurally unavoidable on this carrier.

Physical consequence: no massless B field ⇒ no photon/Z mixing sector; the
"electroweak" of Option B on X_{1,1} is a pure gauged SU(2)_L (≅ SO(3)) with
background-quantized hypercharge labels. Electromagnetism as a dynamical
U(1)_EM = T₃+Y cannot be assembled. As an SM carrier this is fatal on its own,
before the matter-sector findings of N6.

## 5. Candidate (v): Betti / p-form U(1) — killed by the charged-matter test

Expansion block.
- Existence: b₂(X_{1,1}) = 1. Hand derivation: the long exact homotopy
  sequence of U(1) → SU(3) → X with π₁(SU(3)) = π₂(SU(3)) = 0 gives
  π₂(X) ≅ π₁(U(1)) = Z and π₁(X) ≅ π₀(U(1)) = 0; simply connected, so by
  Hurewicz H₂(X;Z) ≅ π₂(X) = Z, hence H²(X;Z) = Z, b₂ = 1. So in a parent
  theory with a 3-form (11D-supergravity-type embeddings), the reduction
  C₃ = A_μ dx^μ ∧ ω₂ on the harmonic 2-form ω₂ produces one massless 4D
  U(1) gauge field. The rank-3 isometry budget is thus genuinely extendable
  to 3+1 — but:
- Kill: KK harmonics (the entire perturbative matter spectrum) are neutral
  under p-form U(1)s; the charged objects are wrapped branes/solitons, with
  masses at the compactification scale. Hypercharge must charge every SM
  fermion (all of Q_L, u_R, d_R, L, e_R carry Y ≠ 0). A U(1) under which the
  light spectrum is neutral cannot be Y. Status: derived at the level of the
  standard KK charge rule (a 4D mode's charge under A_μ from C₃ is its
  ω₂-wrapping number, zero for harmonic field modes); recorded as an
  obstruction with this named source rule rather than a computed spectrum.
- Side value: this U(1) is electroweak-sterile but not useless — it is the
  natural candidate for a dark/global charge in any 11D embedding; out of
  scope here.

## 6. Repair-path survey (bounded; comparisons, not a new programme)

Within the Aloff-Wallach family the gauge content trichotomizes (hand
derivation of the right factor: N1 §2 for k=l; for k,l,−k−l pairwise distinct
the continuous centralizer of U(1)_{k,l} in SU(3) is the maximal torus T², so
the right factor is T²/U(1)_{k,l} ≅ U(1)):

| Carrier | Isometry | Option-B reading | Missing |
|---|---|---|---|
| X_{1,1} | SU(3)×SO(3), rank 3 | colour + weak | hypercharge |
| X_{k,l}, k≠l | SU(3)×U(1), rank 3 | colour + hypercharge | weak SU(2) |
| any X_{k,l} | rank ≤ 3 | — | one factor always |

So no Aloff-Wallach space carries the full Option-B gauge content. The
minimal known 7-manifolds that do are the M^{p,q,r} spaces — U(1) bundles
over CP²×S² with isometry SU(3)×SU(2)×U(1), rank 4 (CDF, citation corrected
in wastebook C6; Witten's 7-dimensional minimum realized). There, colour on
CP², weak on S², hypercharge along the U(1) fibre: Option B's gauge content is
exactly the M^{p,q,r} design. Verdict for the fork: **Option B's natural home
in the literature is the M^{p,q,r} family; X_{1,1} trades the hypercharge
circle away for the enhanced SO(3) fibre.** The two constructions sit at the
two ends of one trade: gauge-complete but standard (M^{p,q,r}) versus
rank-deficient but with the 3-Sasakian/spin^c structure that makes the
doublet-hypercharge correlation automatic (§3). Recorded as a comparison and
repair target, not pursued further here.

## 7. Counterargument pass

1. *"A background flux can still produce a 4D gauge boson by the usual
   flux-compactification mechanism (gauge field from the isometry of an
   enlarged total space)."* That mechanism re-introduces the circle as a
   geometric direction — which is the M^{p,q,r} repair of §6, a different
   carrier, conceded as the repair path. On X_{1,1} itself the circle is
   divided out; there is nothing to oscillate.
2. *"Maybe Y is dynamical but massive (Stueckelberg/Green-Schwarz-like), and
   the SM Y emerges below."* A massive Y cannot deliver the massless photon's
   unbroken U(1)_EM = T₃+Y; killed by the same photon-assembly requirement
   as §4.
3. *"The rank argument assumes only isometry gauge bosons; §5 shows a fourth
   massless U(1) exists in 11D embeddings."* Acknowledged and addressed: the
   Betti U(1) fails the charged-matter test, which is identification- and
   embedding-independent for perturbative modes.
4. *"R5 called the flux reading 'consistent'; this note calls the absence of
   a Y boson 'fatal'. Which is it?"* Both, about different questions. As a
   bundle/charge bookkeeping device the flux U(1) is consistent and even
   structurally elegant (§3); as the SM's dynamical hypercharge it does not
   exist on this carrier (§4). R5's verification pass 2 already drew this
   line; this note re-derives it and makes the photon-assembly consequence
   explicit.

## 8. Kill criteria / what would overturn this note

- A massless 4D vector on X_{1,1} beyond SU(3)×SO(3)×(Betti U(1)) — none is
  known; Wilking's classification plus the b₂ count exhausts the standard
  sources.
- A mechanism giving KK harmonics nonzero charge under the Betti U(1)
  (would revive candidate (v); no such mechanism for elementary modes).
- An error in the two-line evaluations of §2–§4 (each is elementary and
  checkable by eye).

## Verification

- Independent collaborator check (GPT-5.5 via codex CLI, prompts phrased
  neutrally, derivation requested by hand): parity-law proof, Δ₇
  decomposition, centralizer/normalizer computations — verdicts recorded in
  the addendum below when the run completes; any refutation halts the
  dependent rows in N8.
- Internal cross-checks: §3b parity law against every row of T4's tables
  (holds); §4 against R5 verification pass 2 (agrees); §6 trichotomy against
  T2/Wilking at k=l (agrees).

## Addendum — collaborator verdicts (check A, completed 2026-06-11)

Independent run (GPT-5.5, codex exec, read-only, prompt self-contained and
neutral; no repo access):
- **Q1 parity law — CONFIRM.** Same ζ = exp(iπH8) = diag(−1,−1,1) two-way
  evaluation; (−1)^{q8} = (−1)^{2I} on every weight state.
- **Q2 spinor module — CONFIRM.** Δ₇ = 2_{+3} ⊕ 2_{−3} ⊕ 3_0 ⊕ 1_0, derived
  by an independent route (so(7) half-spin weights ½(±e₁±e₂±e₃) with
  e₁ ↦ (2,0), e₂ ↦ (1,3), e₃ ↦ (1,−3) under (2I₃, q8)). Used in N6.
- **Q3a centralizer of su(3)⊕so(3) in itself = 0 — CONFIRM** (both summands
  have trivial centre). Used in N1 §4, N4 §2.
- **Q3b normalizer trichotomy — CONFIRM.** Pairwise-distinct weights ⇒
  N⁰ = T², right factor T²/U(1) ≅ U(1); k=l=1 ⇒ N⁰ = S(U(2)×U(1)) with
  centre U(1)_{1,1}, right factor PU(2) ≅ SO(3). Used in §6.

## Sources

- archive/verification_20260531/R5.md (prior triage and verification passes).
- archive/verification_20260531/T1.md (spin^c line O(k), k odd; λ_8/H8 line).
- archive/verification_20260531/T4.md (+ its verification) — branching tables,
  parity law (two independent table-level verifications).
- wastebook.md C6 entry (CDF correction: M^{p,q,r} = U(1) bundle over CP²×S²,
  isometry SU(3)×SU(2)×U(1)).
- docs/KaluzaKlein_Hilo_Higgsing_KaluzaKlein_Review.md (Dolan–Nash flux-as-Y
  passages, lines ~2291–2399 per R5's verbatim extraction).
- Witten, NPB 186 (1981) 412 (7-dimensional minimum; M^{p,q,r} context).
