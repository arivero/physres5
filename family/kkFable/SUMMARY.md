# kkFable: Option-B re-derivation on the Aloff–Wallach space X_{1,1}

Curated for physres5 on 2026-09-23. Everything outside this file is a verbatim
copy of project-authored material (see the manifest at the end).

**Tags** follow `../kkorchestra/SUMMARY.md`: A1 matrix, A2 pole placement,
A3 ordered assignment; D-pole, D-EW, D-kernel, D-branch, D-filter (Appendix D
targets); App-E (dimensional interpolation); §08 (global form).

## Provenance

- **Source:** `/home/codexssh/kkFable`, a git repository with six commits and
  a clean working tree. The workspace was created 2026-06-11. Notes N0–N7 and
  the verdict ledger were committed that day; N9–N12 and the collaborator
  addenda on 2026-06-12. The final commit (dated 2026-09-23) records the N12
  §5b addition and the didactic paper, both written 2026-06-12.
  `OPUS_IDEAS.md` (2026-07-01) holds three follow-up proposals from a later
  review.
- **Siblings:** successor of `kkorchestra` (see `../kkorchestra/SUMMARY.md`).
  It symlinks that workspace read-only: `CLAIMS.md`, `wastebook.md`, `docs/`,
  `sources/`, `archive/`, `tasks/`, plus `prior-notes/`, `prior-out/`,
  `calc-history/`, `PRIOR-AGENTS.md` and `PRIOR-NOTES-INDEX.md`. Only
  `notes/`, `out/`, `sources-local/`, the charter and `OPUS_IDEAS.md` were
  authored here, and no symlink was followed or copied. The sibling `dvFable`
  imports kkFable's results in
  `../dvFable/notes/2026-06-12-kkfable-cross-import.md`: the c = 1 lock, the
  bare-Casimir objection, the N5 assignment obstruction, the N3 free-modulus
  angle, and the didactic paper as a style model.
- **Method:** pencil-and-paper derivations under the inherited no-Python
  rule. Five independent checks (A–E) by GPT-5.5 through the codex CLI, with
  neutral prompts, are recorded in the note addenda as colleague
  verification; all confirmed.
- **Not copied:** `sources-local/`, which holds five third-party PDFs with
  agent digests. Cite them as Dolan–Nash hep-th/0207078 and hep-th/0207007;
  Fabbri–Fré–Gualtieri–Termonia hep-th/9903036 (the M^{111} spectrum);
  Castellani hep-th/9912277 (G/H geometry); and Duff–Nilsson–Pope
  arXiv:2502.07710 ("Kaluza–Klein Supergravity 2025"). Also not copied: the
  charter `README.md`/`AGENTS.md` (summarized here), LaTeX build files,
  `.gitignore` and the git history.

## Goal and final conclusion

**Goal.** Settle kkorchestra's open fork "Which SU(3)?". Under Option A the
CP² base carries the electroweak SU(3) and colour is absent; all prior physics
used this reading. Under Option B the base carries colour SU(3)_c and the SO(3)
fibre carries weak SU(2)_L. The deliverable is a claim-by-claim verdict table.

**Conclusion.** Option B is dead on X_{1,1} as a Standard-Model carrier. There
are three proved reasons and one inherited one:

1. There is no dynamical hypercharge boson. The isometry group SU(3)×SO(3)
   has rank 3 against the Standard Model's 4. The only hypercharge-like
   circle, U(1)_{1,1}, is the quotiented isotropy circle and has no Killing
   vector.
2. There is no elementary-scalar Higgs doublet: colour-singlet weak-doublet
   scalar harmonics do not exist for any line twist.
3. There is no e_R among Dirac modes: colour-singlet fermions have Y = 0 or
   sit in the lepton doublet.
4. Witten's odd-dimension chirality no-go applies to both options.

Both inherited numbers die under Option B. The rigid 1/4 becomes the free
modulus sin²θ = (1+t)/((1+t)+k_Y). The De Vries assignment fails because the
j = 1/2 slot is colour-charged, and the inverted assignment gives
cos²θ = 1.287. Option A remains the only self-consistent reading of X_{1,1},
as a colourless electroweak toy. Option B's gauge content belongs on the
M^{pqr} family: "flip the carrier, not the labels". The continuation filled
e_R (from gravitino components) and the Higgs (from internal tensors) at the
level of quantum-number slots. That leaves two irreducible obstructions: no
dynamical U(1)_Y and no chirality. It also derived an electroweak alternation
along the D5–D6–D7 ladder and a mechanism for the D7 → D6 transition.

## Valuable ideas and results

1. **The De Vries assignment requires a colourless electroweak carrier.**
   Under Option B the j = 1/2 sector consists only of colour-charged states,
   so reading it as the W channel breaks colour.
   *Why:* it fixes which SU(3) the physres5 labels can live in, and supports
   the colourless count of Appendix E.
   *Bears on:* A3, D-EW, App-E.
   `notes/2026-06-11-option-b-devries-assignment.md` (N5)

2. **The order of the assignment follows from monotonicity.** x₊(J) increases
   with J and M_W < M_Z. So given the pair {3/4, 2}, the W channel must carry
   3/4; the swapped order gives cos²θ = 1.287.
   *Why:* A3's ordering needs no extra input. The open parts are the pair
   itself and the channel identification.
   *Bears on:* A3. N5 §3

3. **Electroweak alternation along the ladder.** The rungs D5 = S⁵/Z_n,
   D6 = SU(3)/T² and D7 = X_{1,1} (total dimension 9/10/11) have gauge
   algebras u(3), su(3) and su(3)⊕so(3), ranks 3/2/3. Hypercharge is gauged
   only at D5 and weak SU(2) only at D7. At D6 both are flux labels.
   *Why:* a direct test of the physres5 full-gauge chain D = 11/10/9. On this
   family the D = 11 rung lacks U(1)_Y and the D = 10 rung carries no
   electroweak gauge bosons. The D = 9 rung matches the SU(3)×U(1)_geom
   endpoint, with U(1) the hypercharge circle.
   *Bears on:* App-E.
   `notes/2026-06-11-option-b-d5d6d7-ladder.md` (N9)

4. **The D7 → D6 transition is a quintet Higgsing.** The collapse is a
   Berger-type axis squash of the fibre, and its order parameter is a weak
   quintet (I = 2) metric modulus. Along it, W^± become massive while W⁰ stays
   massless. Fibre charges turn into monopole flux r = 2I₃. The W^± leave
   through a diverging vev (infinite moduli distance); the surviving U(1)
   leaves through a diverging coupling at zero mass.
   *Why:* the obvious geometric interpolation parameter runs off the
   electroweak ray, because the neutral boson stays massless. This is a
   concrete constraint on the Appendix E map χ: t_dim → t_EW.
   *Bears on:* App-E, D-EW.
   `notes/2026-06-12-option-b-ladder-transitions.md` (N12)

5. **Tower scalings at the two ends.** Near D7 the flux tower is a momentum
   tower, M_r ∝ |r|/R. Near D6 the lowest monopole harmonic (j = |r|/2,
   eigenvalue j(j+1) − r²/4 = |r|/2) gives M_r² ∝ |r|. Nothing in this bosonic
   family protects linearity, which is Witten's BPS ingredient.
   *Why:* this is the only Regge-like material in either project (M² linear in
   the label at leading order). It is also a concrete Kaluza–Klein case where
   a j(j+1) Casimir arrives with an isotropy subtraction.
   *Bears on:* D-filter (branch scaling, Regge survival), A1. N12 §5b

6. **The Higgs is forced into the internal geometry.** No elementary
   scalar-field Higgs slot exists on any homogeneous carrier examined
   (X_{1,1}, S⁵×S², M^{111}), by the charge-locking lemma. On X_{1,1} the slot
   appears in internal tensor components (3-form and metric components).
   *Why:* the order-parameter channel h_J of a KK route should be a connection
   or tensor mode. This supports gauge-Higgs, Hosotani and CSDR readings.
   *Bears on:* D-kernel. N6 §2,
   `notes/2026-06-11-option-b-m111-carrier-test.md` (N10) §2,
   `notes/2026-06-12-option-b-completing-the-generation.md` (N11) §3

7. **Geometry enforces the Standard Model Z₆ charge correlation.** Y = m/6 is
   fixed by the lepton doublet. Every slot then obeys
   6Y ≡ 2t(λ) + 3·(2I_w) (mod 6), where t is the colour triality. The element
   ζ = diag(−1,−1,1) lies in U(1)_{1,1} and acts as −1 in SU(2); it is the Z₂
   in U(2) = (SU(2)×U(1))/Z₂. Five of seven slots (Q_L, u_R, d_R, L, ν_R)
   land with the right quantum numbers.
   *Why:* a worked example of a compactification fixing the global quotient
   and the charge lattice.
   *Bears on:* §08, D-branch (α endpoint: charge lattice).
   `notes/2026-06-11-option-b-hypercharge-locus-and-matter.md` (N6) §4–5,
   `notes/2026-06-11-option-b-u1y-origin.md` (N2) §3b

8. **Weinberg's simple-factor rule.** A coupling ratio is rigid only while
   both generators sit in one simple factor. Across two factors,
   sin²θ = x₁/(x₁ + k_Y·x₂) is a free shape modulus.
   *Why:* any KK, interval or G₂ route to the W/Z ratio must keep the two
   channels inside one simple factor, or derive the modulus.
   *Bears on:* A2, A3, D-kernel.
   `notes/2026-06-11-option-b-weinberg-angle.md` (N3)

9. **Complementary exclusion among carriers.** The rank-4 carriers gain the
   hypercharge boson and lose the matter. M^{111} has no SU(2) doublets at any
   Kaluza–Klein level, and its only massless charged colour/weak singlets are
   gravitini. S⁵×S² fills 2 of 7 slots. X_{1,1} has rank 3 and fills 5 of 7 in
   the Dirac sector, or all 7 once gravitino and tensor modes are included
   (N11).
   *Why:* it maps the homogeneous-coset landscape that a physres5 KK route
   would enter.
   *Bears on:* App-E, D-kernel. N10

10. **The didactic paper.** A 14-page self-contained account of the old
    Kaluza–Klein toolbox worked end to end on X_{1,1}: isometries become gauge
    bosons, Weinberg's inertia rule, Frobenius spectroscopy, spin^c parity and
    index counting.
    *Why:* a teaching reference, and the style model dvFable adopted.
    `out/OPTIONB_X11_DIDACTIC.tex/.pdf`

**G₂ and Regge.** kkFable contains no G₂-holonomy analysis and no Regge
trajectories beyond item 5. Its digest of Duff–Nilsson–Pope
(arXiv:2502.07710, §3) records the link to physres5 §06d. That review names
singular G₂ compactifications (Acharya–Denef–Hofman–Lambert; Atiyah–Witten) as
the known escape from the chirality no-go that kills X_{1,1}.

## Negative results worth keeping

1. **Option B on X_{1,1}:** dead, for the three proved absences plus
   chirality listed above. `notes/OPTION-B-VERDICTS.md`

2. **Every dynamical hypercharge candidate fails.**
   - The bare SO(3) → SU(2) lift adds no Cartan generator.
   - A colour Cartan cannot serve, since Z(su(3)) = 0.
   - The U(2)-lift U(1), proven identical to the spin^c/Dolan–Nash flux
     circle, acts trivially on X_{1,1}.
   - The Betti U(1) (b₂ = 1) leaves all Kaluza–Klein modes neutral; the
     literature states this verbatim for M^{111}.

   N2, N10

3. **Aloff–Wallach trichotomy.** X_{k,l} with k = l gives colour plus weak.
   When the weights k, l, −k−l are pairwise distinct, it gives colour plus
   hypercharge. No member gives all three. N2 §6

4. **Squashing breaks nothing.** Every invariant metric g_t keeps the full
   SU(3)×SO(3), so electroweak breaking needs a charged vev. N1 §5

5. **Custodial symmetry under Option B.** The centralizer of su(3)⊕so(3) in
   itself is zero, so no spectator group remains, and ρ has no colour-singlet
   doublet to act on. N4

6. **The 1/4 rigidity and the De Vries assignment under Option B:** both dead
   (items 1, 2 and 8 above). N3, N5

7. **Rank-4 repairs do not restore the matter** (complementary exclusion).
   N10

8. **A discarded shortcut.** An (S⁵×S³)/U(1) model admitted coloured doublets
   that M^{111} forbids. It describes a different space and was dropped; the
   note keeps it as a warning against shortcut models. N10 §7

9. **Chirality.** Witten's no-go carries over unchanged. The base index
   (n² − 1)/8 organizes multiplicities and gives no 4D chirality. N7, N6 §6

## Open threads

1. The D6 ↔ D5 half of the ladder: does the D5 hypercharge boson leave
   through the vev exit or the coupling exit? N12 §4, `OPUS_IDEAS.md` #1
   [App-E]
2. The shape of the reduced potential along the quintet direction ("hat
   formation"), seeded by the two Einstein points t = +1 (3-Sasakian) and
   t = −3/5 (squashed). N12 §5, `OPUS_IDEAS.md` #2
3. The forced CSDR Higgs computation on X_{1,1}: the sign of the reduced
   potential on the internal-tensor doublets. `OPUS_IDEAS.md` #2 [D-kernel]
4. The charge-locking lemma as a classification theorem over Castellani's
   list of 7D coset Einstein spaces. `OPUS_IDEAS.md` #3
5. A protection mechanism for a linear tower in the emergence reading (the
   missing BPS ingredient). N12 §5b [D-filter]
6. The strong-coupling fate of the surviving U(1) at the collapse endpoint.
   N12 §4
7. A composite (quark-bilinear) Higgs with its own custodial symmetry under
   Option B. N4 §6
8. The postulates c = 1 and D†D = j(j+1): unchanged from kkorchestra and
   still open. N5 §4 [A1]

## Manifest of copied files

All files are byte-identical copies (`cp -p`, timestamps kept) from
`/home/codexssh/kkFable/`, at the same relative paths. Relative links in them
follow the source layout, including symlink names such as `prior-notes/`, and
resolve only for files copied here. Note numbering: N8 is
`notes/OPTION-B-VERDICTS.md`.

| Path | Bytes | Content |
|---|---:|---|
| `notes/OPTION-B-VERDICTS.md` | 11,284 | the verdict ledger (N8) |
| `notes/README.md` | 4,654 | index of N0–N12 |
| `notes/2026-06-11-option-b-baseline-audit.md` | 7,387 | N0: provenance, acceptance ledger, conventions |
| `notes/2026-06-11-option-b-dictionary-and-rank-budget.md` | 8,384 | N1: dictionary, rank budget 3 < 4 |
| `notes/2026-06-11-option-b-u1y-origin.md` | 14,452 | N2: origin of U(1)_Y, lift-equals-flux theorem, candidate kills |
| `notes/2026-06-11-option-b-weinberg-angle.md` | 6,790 | N3: free-modulus weak angle |
| `notes/2026-06-11-option-b-custodial.md` | 7,377 | N4: custodial symmetry dead under Option B |
| `notes/2026-06-11-option-b-devries-assignment.md` | 6,926 | N5: De Vries assignment under Option B |
| `notes/2026-06-11-option-b-hypercharge-locus-and-matter.md` | 13,663 | N6: slot table, Z₆ law, index |
| `notes/2026-06-11-option-b-chirality-carryover.md` | 3,010 | N7: chirality no-go |
| `notes/2026-06-11-option-b-d5d6d7-ladder.md` | 10,991 | N9: electroweak alternation |
| `notes/2026-06-11-option-b-m111-carrier-test.md` | 13,316 | N10: rank-4 carriers, complementary exclusion |
| `notes/2026-06-12-option-b-completing-the-generation.md` | 10,795 | N11: gravitino e_R, tensor Higgs |
| `notes/2026-06-12-option-b-ladder-transitions.md` | 14,239 | N12: quintet collapse, two exits, tower test |
| `out/OPTIONB_X11_DIDACTIC.tex` | 44,071 | didactic paper, standalone LaTeX |
| `out/OPTIONB_X11_DIDACTIC.pdf` | 370,682 | compiled paper (14 pp.) |

Total: 16 copied files, 548,021 bytes, plus this summary. `OPUS_IDEAS.md` was
dropped during de-duplication: its three proposals appear under Open threads
above and in `../IDEAS.md`, and the file stays in the source repository.

