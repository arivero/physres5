# Merged ideas from the de Vries–Rivero family

This file collects, once each, the results that the ten sibling folders in
`family/` contribute to physres5. Several of them were found independently by
two to six projects; each entry lists every source, so a repeated discovery
shows up as one idea with several witnesses. The per-project detail, the
numbers and the file paths are in each folder's `SUMMARY.md`.

Tags: **A1** the Casimir matrix Q(J) = μ²[[0,√J],[√J,−J]]; **A2** pole
placement; **A3** the ordered assignment (J_W, J_Z) = (3/4, 2); **D-pole**,
**D-assign**, **D-kernel**, **D-partner**, **D-filters** for the five
subsections of `manuscript/sections/D_theorem_targets.tex`; **App-E**
dimensional interpolation; **§7** flavour boundary; **§8** global form.
Source names are the folder names under `family/`.

## 0. Actions for the manuscript

1. **Update the W input (Sec. 3, eq. `spole-current-input`).** pdgLive 2026
   lists M_W = 80.3625 ± 0.0077 GeV (the average excludes CDF 2022) and
   Γ_W = 2.14 ± 0.05 GeV; both lines were read from pdglive.lbl.gov on
   2026-09-23. With physres5's own Breit–Wigner-to-pole conversion and
   M_Z = 91.1879 ± 0.0020 GeV this gives s²_pole = 0.2233064 ± 0.0001550,
   and the de Vries value 0.2231013 sits at **+1.32σ**. The current text uses
   PDG 2025 (80.3692 ± 0.0133) and gets 0.2231768 ± 0.0002608, +0.29σ; the
   same script reproduces that number exactly. dv2, dvFable, signed-dv
   (hans) and marathon recorded the 2026 value independently; CMS 2026 alone
   (80.3602 ± 0.0099) gives +1.27σ. PDG-Live 2026 also lists
   m_H = 125.13 ± 0.11 GeV (recorded by hans; not re-read here).
2. **Complete the attribution.** The bibliography cites Rivero,
   hep-ph/0606171, only. Add H. de Vries, Physics Forums post #44, November
   2004 (thread "All the lepton masses from G, π, e"), and de Vries–Rivero,
   hep-ph/0503104. A verified record is in `marathon/refs.bib` and
   `marathon/refs_notes.md`. For the Regge framing of Sec. 6, Veneziano
   (1968) and Chew–Frautschi are the primary sources (physres6 reference
   audit); Sec. 6 now cites them through Tong's notes.
3. **Price the coincidence.** A trials-corrected look-elsewhere statement is
   the open item named by the most projects: physres5 `OPUS_IDEAS.md` #1,
   dvFable (terminal state T3), marathon (trials list), signed-dv (recount
   C9), weak (representation scan) and both golden referees. Parts on hand:
   - `signed-dv/algebra/look_elsewhere.py` as a scan engine, with two lessons
     from the recount: set the window from the experimental σ, and count
     trials over the modelling choices (a 1σ window moves p from 1.6×10⁻⁶
     to about 5×10⁻⁴).
   - marathon's Theorem 2 family over κ = J_W/J_Z as a hypothesis class that
     can be registered in advance.
   - dvFable's quadratic-shape inventory: the de Vries content is the single
     condition c₁ = c₂ in x² + c₁x − c₂ = 0.
   - marathon's list of choices to price: the texture among 2×2 forms,
     J = j(j+1), the positive branch, the channel map, the M_Z anchor, the
     scheme, the tower extension, the negative-branch matches.
   Count the kernel, the quartic and κ = 3/8 as **one** coincidence
   (marathon Theorems 1–2; signed-dv Vieta identity).
4. **State one derived result as a result.** The relative-gain Hessian
   (kkorchestra) and the single-portal Schur completion (chats-regge-kk) are
   the family's only positive construction of A1 (Sec. 2 below). It reduces
   A1 to one spectral statement, P†P = J with no shift, plus the choice of
   gain functional. It fits a short subsection before the theorem targets,
   in line with physres6's lesson that derived results stay outside the
   target list.
5. **Write the obstructions into the route sections (6c–6g) and App. D.**
   The determinant obstruction, the single-trace Gram theorem, the resolvent
   requirement and the Hodge positivity bound (Sec. 3 below) each remove a
   whole class of routes and name the indefinite ingredient a surviving
   route must contain.

## 1. Exact algebra (one object, several notations)

- **Root identities.** x₊ + x₋ = −J, x₊x₋ = −J, 1/x₊ + 1/x₋ = 1, hence
  tr Q(J)⁻¹ = 1/μ² at every level and x₋ = −J/x₊ = −x₊/(1 − x₊).
  Rapidity form: x₊ = tanh²η, |x₋| = sinh²η, sinh η tanh η = √J. The
  golden2 "winding" map ũ = u/(1 − u) and physres6's branch inversion
  x → −J/x are this same Vieta involution. Sources: chats-regge-kk (G20,
  G22), physres6 (reciprocal invariant, branch duality), signed-dv
  (rapidity), golden (duality map). [A1, D-partner, D-filters]
- **Entry conditions reduce to one datum.** With Σ_hh = 0, tr = det forces
  (off-diagonal)² = −(lower diagonal) (physres6). Equivalently, Q(J) is
  congruent to μ²[[0,1],[1,−1]] with channel metric diag(1, 1/J), so
  Σ_aa = J and Σ_haΣ_ah = J become the single statement ⟨a_J, a_J⟩ = 1/J
  (weak). [A1, D-kernel]
- **Resolvent forms.** The gap equation X = J/(X + J) has three positive
  realizations: an NJL bubble, a rank-one Feshbach Hamiltonian and a large-N
  saddle (dv2). λ₊ is the unique attractor of f(X) = J/(J + X), the
  zero-frequency Schur reduction of [[0,√J],[√J,−(J+X)]], so nested
  decimation with uniform rungs (√J, J) ends at λ₊ (marathon). The Schur
  complement reads J/(λ + cJ) = λ (kkorchestra). [A1, D-kernel]
- **Stationarity form.** V(x) = x⁶/6 + Jx⁴/4 − Jx²/2 has the positive roots
  as its nonzero extrema; a reduced potential Ax⁶ + BJx⁴ − CJx² reproduces
  the relation exactly when 2B = 3A and C = 3A, a pass/fail test for any
  reduction (golden §68). [A1, D-kernel]
- **Number field.** sin²θ = (19 − 3√19 + 3√3 − √57)/16 lies in ℚ(√3, √19)
  and has minimal polynomial 64x⁴ − 304x³ + 414x² − 190x + 25 (the golden
  quartic). Its four roots are the branch combinations
  1 − λ_a(J_W)/λ_b(J_Z), with the Galois group acting as branch swaps.
  ρ = M_W²/M_Z² has minimal polynomial 64y⁴ + 48y³ − 114y² + 18y + 9.
  Sources: marathon (Theorems 1–2, degree-8 corollary), golden (field of
  definition). [A1, A3]
- **Vieta and κ.** The signed trace ratio, the determinant ratio and
  C_F/C_A all equal J_W/J_Z = 3/8; cos²θ = (3/8)·F_dyn with
  F_dyn = [√(1+4/J_W) − 1]/[√(1+4/J_Z) − 1]. One identity, counted once.
  Sources: signed-dv, marathon. [A3]
- **Branch sum rules.** m₋² − m₊² = Jμ² and m₊m₋ = √J μ² at every j
  (marathon; golden). [D-partner]

## 2. The coefficient lock: constructions of A1 and the one free number

Six projects isolated the same free number in different notation:
r = γ/α = 1 (dv2), g²/α = 1 (dvFable), β = α² (kkorchestra), c = 1
(chats-regge-kk), a/b = 1 (weak), and the operator-norm lock g = 1
(marathon). dvFable states the full set once:

- **B1** induced gap: Σ_haΣ_ah = Σ_aa, i.e. r = 1;
- **B2** minimal portal: Σ_hh = 0;
- **B3** the same kinetic normalization in every channel;
- the bare Casimir map Σ_aa = J with no level shift, and the scale
  condition α²x₀ = 1 (kkorchestra).

Generic values give x² + Jx − r²J = 0. Sensitivity at the de Vries point:
d sin²θ/d ln x₀ ≈ −0.070 and d sin²θ/d ln c ≈ −0.140, so staying inside the
pole error needs x₀ = 1 within 0.4% and c = 1 within 0.2% (kkorchestra
curator check); the m_H match needs a/b = 1 within 6×10⁻⁴ (weak).

**Positive constructions.** Three notations for one object:

1. Single-portal Schur completion H_j = [[0, A†],[A, −AA†]] on
   V_j ⊕ Im A_j with A†A = J (chats-regge-kk; PRL Supplemental Sec. III).
2. Relative-gain Hessian: the gain E(q,0) − E(q,p) with
   E = ½‖q − P†p‖² has Hessian [[0,P†],[P,−PP†]]; the baseline
   subtraction gives Σ_hh = 0 and one norm gives c = 1 (kkorchestra).
3. Single displacement square αμ²‖A†Q − p‖² − αμ²‖p‖², which forces γ = α
   (dv2, milestone 1).

Each moves the lock into the choice of functional. Supporting pieces:

- **Operator-norm origin of √J.** Σ_p |⟨p|J⃗|v⟩|² = J for every state of
  every representation, so the reduction onto (|v⟩, J⃗|v⟩/√J) has
  off-diagonal exactly √J at half-integer j too; a single ladder matrix
  element gives 1 at j = ½ (marathon). [A1, A3]
- **Current zero modes.** SU(2)_k zero modes satisfy Σ_a J₀^aJ₀^a = j(j+1)
  with unit coefficient, while L₀ gives j(j+1)/(k+2); level 2 truncates to
  {0, ½, 1}. This is the only mechanism in the family that both truncates
  the channel set and supplies the unit Casimir (chats-regge-kk, dv2).
  [A1, A3, D-filters]
- **Shift-free Casimir operator.** The vertical Casimir gradient
  P = √x₀ Σ_i J_i ⊗ e_i gives P†P = x₀C₂ exactly; smooth and Kostant Dirac
  squares add curvature shifts (C_G − C_H + ‖ρ_G‖² − ‖ρ_H‖²), so
  D†D = j(j+1) is a second postulate of the same rank as c = 1
  (kkorchestra, kkFable). [A1]

## 3. Obstructions and dead routes

**Positivity family.** These remove every route whose kernel is the static
Schur complement of a positive operator:

- A(J) has a zero diagonal entry and a nonzero off-diagonal, so it fails to
  be positive semidefinite; its (1,1) signature survives positive kinetic
  redefinitions, so Q(J) is a reduced kernel, Hessian or pre-Goldstone
  object (dv2).
- det K_J(0) = −J < 0; the static Schur complement of a positive source
  (unitary bulk, invertible heavy sector, non-negative boundary terms) has
  determinant ≥ 0 (dvFable curator note). Shifting λ by a constant restores
  positivity and changes the predicted ratio.
- No stable positive boundary, defect or mismatch energy has the block as
  its full Hessian (kkorchestra).
- The Hodge Laplacian is non-negative, so the −J entry needs a curvature
  term (Weitzenböck on a squashed Berger S³) or a Wilson-line potential
  (physres6).

A surviving route needs one indefinite ingredient: a tachyonic boundary
mass, a wrong-sign kinetic term, a constraint, saddle or auxiliary reading,
or a pole map in which λ is not the mass-squared of a positive operator.

**Gauge-theory reductions.**

- Single-trace Gram theorem: one trace-normalized Yang–Mills term gives the
  transverse kernel B + D†D for every background; its Schur complement is
  ≥ 0, the spectrum is a plain sum, and the fixed coefficients land on the
  Manton rational angles (SU(3) 3/4, O(5) 1/2, G₂ 1/4). In geometric
  reductions Σ_aa and Σ_haΣ_ah come from different operators (dvFable,
  iteration 3). Interval/CHM and G₂ routes therefore need brane-localized or
  loop terms, which bring the free number back.
- Standard gauge-Higgs unification on S² gives a Goldstone and a separate
  scalar with no Schur block (dv2).
- The ordinary KK vacuum Hessian has no retained second channel
  (kkorchestra); single-field KK on S² gives x = J/(1+J) (golden2); the flat
  semi-infinite chain never produces λ₊ (marathon).
- No single renormalizable operator yields √C₂: an adjoint spurion
  saturates at j², Wigner–Eckart gives 0 for the doublet and 3 against 2 for
  the triplet (weak).
- X₊(C) is irrational in C, so a mechanism valid for all C must contain a
  resolvent; a rational kernel fitted at 3/4 and 2 over-fits (dvFable).

**Principles that leave r free.** Local gauge invariance (a five-parameter
invariant family through the de Vries point), KSRF I and II, CDD
exclusion, bootstrap closure (dvFable); symmetry alone (kkorchestra); the
NCG order-one condition, inner fluctuations and KO signs (kkorchestra T5).

**Wrong normalizations.** Sugawara L₀ gives 0.3014, the Weitzenböck-shifted
curl 0.2670, the horizontal-only current 0.2423 (chats-regge-kk, dv2); S²
spinor harmonics give J + ¼ (golden); orthogonal projection erases the
J-dependence; Dirichlet-to-Neumann data supply √J and leave c free
(kkorchestra).

**String and brane routes.** D8/O8 source balance fails on CP² × CP¹ and
the flag manifold, and the D10 boundary-current route ends in a scoped
theorem: compatible with de Vries, forcing nothing (dv2). A Regge-trajectory
reading of the finite two-root block fails (chats-regge-kk); the negative
branch grows like s against spin, matching no string law (physres6); the
Myers radius grows without saturating (golden2).

**Carriers.** Option B on X_{1,1} (colour on the base) is dead: no
dynamical hypercharge boson, no elementary Higgs doublet, no e_R, and the
chirality no-go (kkFable). Across two simple factors the weak angle is a
free modulus (kkFable N3). The D = 10 flag rung carries no electroweak gauge
bosons (kkorchestra CSDR centralizer; kkFable ladder).

**The κ = 3/8 correction.** No surveyed framework fixes κ; a conditional
no-go limits single-generator custodial breaking; the D-term charge 3/8
sits off the hypercharge lattice; the GUT 3/8 is a different group-theory
number (signed-dv, hans).

**Statistics.** Integer fits in the M^{pqr} family are dense: 138 hits
within 10⁻³ (chats-regge-kk).

## 4. Assignment and the electroweak ray (A3, D-assign)

- **Order.** x₊(J) increases with J and M_W < M_Z, so the pair {3/4, 2}
  fixes the order; the swap gives cos²θ = 1.287 (kkFable).
- **Geometric home.** The two isotropy blocks of X_{1,1} carry SU(2)_L
  Casimirs 2 (adjoint, m₀) and 3/4 (Higgs doublet, m₃); the assignment
  needs a colourless electroweak carrier (kkorchestra T4, kkFable N5).
  Borel–Weil V_j = H⁰(CP¹, O(2j)) supplies the labels 0, 3/4, 2 and keeps
  the photon massless through Qη₀ = 0 (chats-regge-kk).
- **Doublet label versus orbit norm.** J_W = 3/4 is the doublet Casimir;
  the broken-vacuum charged-orbit norm equals 1, so a map from x₊(3/4) to
  the W pole needs an explicit branch-quotient conversion (chats-regge-kk,
  G29).
- **Mass ratio versus coupling ratio.** The relation contains no g or g′;
  on physres5's ray it fixes g′/g, so a derivation must output a coupling or
  Weinberg-length ratio (dv2). α needs absolute lengths:
  α_EM = 16π²G/(L₂² + L_Y²) (chats-regge-kk).
- **ρ = 1 and c = 1 are independent.** kkorchestra derives ρ = 1 on the m₃
  block for every Wilking modulus; an action giving both would make de Vries
  a special custodial situation.
- **Scans.** {2, 3} beats the other nine SU(2) pairs with C₂ < 12 by a
  factor of about 300 (weak); (½, 1) is the only half-integer pair within
  3σ for j ≤ 4 (dvFable). SO(32) accommodates {2, 3} and selects neither
  the pair nor the removal of singlets (weak, meeting physres5 §7).

## 5. Pole placement and data (A2, D-pole)

- 2026 inputs: action 1 above. CDF II (80.4335) excludes the relation at
  about 6σ (marathon, signed-dv).
- Breit–Wigner and complex-pole masses differ by Γ²/2m ≈ 34 MeV (Z) and
  27 MeV (W), which exceeds the experimental errors (marathon). The
  relation must never be compared with sin²θ_eff (dv2); MS-bar sits 4%
  away, and one-loop running never returns M_W/M_Z = 0.881419 above M_Z
  (signed-dv §8). Both support A2.
- A geometric coupling ratio is a boundary condition for running (the
  Killing-inertia 1/4 is reached near 3.6–3.9 TeV); a KK derivation of 0.2231
  as a pole ratio must supply Δ_match (kkorchestra).
- The residues in the gap realization are Z_W = 0.699 and Z_Z = 0.789, so a
  pole map there carries residues below one (dvFable).
- Radial normalization μ = v√3/4 reproduces M_Z to +3.6×10⁻⁴ in the G_F
  scheme, with g² = J_W·x₊(J_W) (golden2).
- Re-anchoring on physres5's complex-pole M_Z sharpens the partner-slot
  coincidences (signed-dv C7).

## 6. Partner branch, scalar functional and α (D-partner)

- **Candidate F_sc.** |x₋(3/4)| ↔ m_H² and |x₋(2)| ↔ v²/2 (signed-dv;
  golden2 reads them as v/2 and v/√2; weak reads the first as the bare
  Higgs mass). The two vacuum readings v/2 and v/√2 cannot both hold
  exactly: the needed ratio is 2 and the actual one 2.07173 (marathon,
  Lemma 1).
- **κ-free sum rule, found twice.** m_H² + v²/2 = μ²[11/4 + x₊(3/4) +
  x₊(2)], a trace identity over both blocks. It holds at −0.9σ on the
  Breit–Wigner anchor and about ±0.3σ on physres5's complex-pole anchor
  (signed-dv); weak found the same identity to 4–5×10⁻⁴.
- **Rank-1 scalar shift.** Lifting the doublet partner root to m_H with M_W
  fixed requires δM² = −ΔP₋ along the tachyonic eigenvector; a
  trace-preserving shift moves M_W to 84.60 GeV (weak). golden §63 states
  the same lock as a loop condition on the W/Z bracket.
- **Auxiliary status made explicit.** P_J(x) + λ(x − x₊) moves x₋ and holds
  sin²θ exactly (signed-dv, hans).
- **α.** The scale tie v = √2·M₋(2) is v = (1+√3)M_Z, 1.18% high, and gives
  1/α = 135.29; the "infrared α" agreement is that offset squared, so α and v
  count as one test (physres6 with curator check; signed-dv C8). The v/2
  reading gives 130.60. Rivero hep-ph/0606171 already has 135.28.
- **What F_sc must output.** λ_H = (3 + √57)/(32(1 + √3)) = 0.12067 on the
  selector slice (dv2); on homogeneous carriers the Higgs slot sits in
  tensor or connection modes, which favours gauge-Higgs, Hosotani and CSDR
  readings of h_J (kkFable). physres6 proposes the order parameter as the
  radius stabilizer (Higgs = radion).
- **Flavour stays separate.** A common-scale seed spans at most 1.76 in
  mass squared, so it cannot host the lepton hierarchy (weak), supporting
  §7.

## 7. Towers, Regge behaviour and branch scaling (D-filters)

- **The tower.** With μ fixed by M_Z, a j-labelled tower gives 96.54, 99.58,
  101.45, 102.68 GeV, … accumulating at μ = 106.58 GeV (chats-regge-kk, dv2,
  physres6, marathon, signed-dv, golden, weak). A route must predict these
  states or project them out. The SU(2)₂ finite branch removes j = 3/2; a
  Peter–Weyl rotor keeps it (dv2).
- **Tests.** In the label pattern (γ, W, Z) = (0, ½, 1), j = 3/2 appears
  only in the W±Z channel; neutral pair production opens at 193 GeV, inside
  LEP 2 reach (marathon). The CMS 95.4 GeV feature (2.9σ local, 1.3σ global)
  sits 1.14 GeV from the j = 3/2 slot; dv2, golden and weak all demoted the
  match.
- **Scaling against spin.** M₊ stays bounded (D0-like) and M₋ grows like s
  (space-filling); the inversion pairs Dirichlet with Neumann (physres6).
  Neither branch follows a Regge law (golden). The Regge completion keeps
  labels apart: M² = μ²x±(j(j+1)) + N_osc/α′ (physres6).
- **Emergent-dimension test.** A finite restored multiplet gives symmetry
  restoration only; an extra dimension needs an infinite family with gap
  M_n ∼ n/R computed from the source (kkorchestra). Near the D7 end of the
  ladder the flux tower is a momentum tower; near D6 it gives M² ∝ |r|
  (kkFable).

## 8. Dimensional interpolation and global form (App-E, §8)

- **The D5–D6–D7 ladder** (total dimension 9/10/11): hypercharge is gauged
  only at D5 and weak SU(2) only at D7; the D = 10 rung carries no
  electroweak gauge bosons. The D7 → D6 collapse is a weak-quintet (I = 2)
  Higgsing along which the neutral boson stays massless, so this geometric
  parameter runs off the electroweak ray (kkorchestra, kkFable). This is a
  concrete constraint on the App-E map χ: t_dim → t_EW.
- **Global form.** Z₆ → Z₃ descent to (SU(3)_c × U(1)_Q)/Z₃
  (chats-regge-kk); the geometry of X_{1,1} enforces
  6Y ≡ 2t + 3·(2I_w) (mod 6) (kkFable); the D5 lens deck group supplies
  charge periods, and Z₅ fails as the Standard Model quotient (kkorchestra).
- **G₂.** The flag SU(3)/T² with its nearly-Kähler metric is the link of a
  G₂-holonomy cone (Bryant–Salamon on Λ²₋(CP²); Atiyah–Witten,
  hep-th/0107177), and the squashed Einstein metric on X_{1,1} carries a
  nearly parallel G₂ structure (curator notes in kkorchestra). Chiral matter
  needs singular G₂ loci (Acharya–Witten, hep-th/0109152), so the
  chats-regge-kk exclusion of D = 11, based on smooth reductions, leaves
  physres5's localized G₂ route open.

## 9. Method worth reusing

- A status-labelled claim ledger (about 340 rows, chats-regge-kk) and a
  derived-versus-assigned table (physres6, Table I).
- Pre-registered terminal states T1–T3 (dvFable). T1 condition 4 is a sharp
  acceptance test: a valid principle must explain why Sugawara fails.
- Five decision gates for a model (Fermi scale, alignment, precision, dark
  sector, implementation) in weak's `codexModel.tex` (summarized in
  `weak/SUMMARY.md`).
- physres6's process lessons: state a derived result as a result, cap
  referee passes at two, measure progress by a derived result, an accurate
  ledger and a compiling paper.
- Known errors in sibling drafts are tabled in `golden/SUMMARY.md` §6.1,
  `weak/SUMMARY.md` §6.1, `signed-dv/SUMMARY.md` §5 items 6–14,
  `physres6/SUMMARY.md` (open referee items) and `marathon/SUMMARY.md`
  (open threads). Reuse their numbers only with those corrections.

## 10. Open calculations, ranked

1. The trials-corrected look-elsewhere engine (action 3).
2. A physical gain functional that fixes c: an interface effective-action
   difference, a finite trace, a constraint or saddle action, a
   determinant/gluing source, or the disk-level Hom one-square term from the
   Payen endpoint action with D8 DBI/WZ (kkorchestra thread 1; dvFable
   candidate (i); dv2; weak §6.2; chats-regge-kk gate G1).
3. The squashed-S³ computation with a Wilson line: test tr = det = −J at
   s = ½ and 1 with the Henkel–Lauret Laplacian (arXiv:2605.05406). A hit
   delivers A1 and A3 together (physres6 `OPUS_IDEAS` #1).
4. The CHM interval kernel (physres5 `OPUS_IDEAS.md` #3), built with the
   indefinite ingredient that Sec. 3 requires.
5. The coefficient test 2B = 3A, C = 3A on a concrete reduction: 6D
   Einstein–Maxwell on M₄ × S², or a fixed-J Legendre transform of a DBI +
   Wess–Zumino brane (golden §68).
6. The running-α inversion Q* with Jegerlehner's Δα_had (arXiv:0807.4206);
   it measures the scale tie's offset in v (physres6 `OPUS_IDEAS` #2).
7. A LEP 2 recast for pair-produced narrow neutral states at 96–104 GeV and
   an FCC-ee scan up to 106.58 GeV (marathon).
8. Partner-branch dynamics: a bound-state or anti-bound-state origin of the
   negative root (signed-dv referee), a mechanism for the rank-1 scalar
   shift (weak, golden §63), and tree-level matching onto O_H and O_HD to
   test κ = C_F/C_A (signed-dv `OPUS_IDEAS` #1).
9. Lean formalization of Sec. 1 (physres5 `OPUS_IDEAS.md` #2).
10. Global form and line operators: whether any global form admits j = 3/2
    while keeping the assignment (dvFable candidate (g)).
