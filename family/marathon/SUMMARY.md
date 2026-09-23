# marathon: "A Casimir Ladder for the Electroweak Bosons", a hand-derived synthesis

Curated 2026-09-23 for the physres5 family archive. Copied files are unchanged
from the source; the manifest lists sizes and hashes.

Shorthand, as in `../physres6/SUMMARY.md`. physres5 assumptions: **A1** Casimir
matrix; **A2** pole placement; **A3** ordered assignment (3/4, 2). Appendix D
targets: **D1** pole placement; **D2** assignment and ray admissibility;
**D3** local route kernel; **D4** partner branch and alpha endpoint; **D5**
branch scaling, Regge intercept survival, SUSY-QM origin.

## Provenance

- **Source:** `/home/codexssh/marathon`, a flat directory of 11 files without
  version control.
- **Dates:** every file was written on 2026-07-02 between 00:53 and 01:41 CEST.
  `main.pdf` was built at 01:40 from the final `main.tex`.
- **Method:** written by Claude Fable 5 with no code execution allowed, so every
  closed form was derived symbolically and every decimal computed by hand.
  Two other models checked the work:
  - a Claude Sonnet subagent verified the bibliography (`refs_notes.md`);
  - GPT-5.5, run through the Codex CLI, refereed `draft_v1.tex` adversarially
    (`referee_gpt55.md`).

  The README mentions an earlier 15-point review round that was never archived.
- **Relation to the siblings:** a synthesis over the Rivero corpus.
  - It shares the kernel x² + Jx − J = 0 with physres5 and physres6. It
    recomputes the scale M∞ = μ = 106.578 GeV and the 96.5 GeV slot that
    physres6 also reports.
  - physres6's acknowledgment anchors its de Vries attribution.
  - The quartic 64x⁴ − 304x³ + 414x² − 190x + 25 comes from the golden and
    golden2 repositories.
  - κ = 3/8 = C_F/C_A comes from hans/signed_dbdevries. This follows Mission 6
    in `~/globalFableGoals.md`, which this paper partly carries out.
  - The negative-branch matches and the unaudited Monte Carlo figures come from
    other corpus files.

## Goal and final conclusion

**Goal.** The paper sets out to:

- state the de Vries–Rivero kernel once;
- prove its exact algebra by hand;
- test whether the corpus formulations are one object;
- extract the consequences that need no new dynamics.

**Conclusion** (`main.pdf`: 14 pages as built; the README says 12):

- **One object.** sin²θ = (19 − 3√19 + 3√3 − √57)/16 = 0.2231013 has minimal
  polynomial 64x⁴ − 304x³ + 414x² − 190x + 25, which is the golden-line quartic.
  The kernel line and the quartic line are therefore one coincidence, and the
  count of independent confirmations goes down.
- **m_W prediction.** Given m_Z = 91.1876 GeV, the kernel predicts the
  tree-level on-shell value m_W = 80.3745(19) GeV. That is:
  - +0.4σ from PDG 2024;
  - +1.4σ from CMS 2024;
  - −6.1σ from CDF II;
  - about 3σ above the SM global fit.
- **Status.** The kernel is presented as a spectral ansatz. A derivation needs
  three numbered assumptions: an internal SU(2)_i label, pairing through the
  generators, and a partner with mass J, a tachyonic sign and nesting. The paper
  lists five failure conditions and the trials that any significance claim must
  price. It leaves significance to a future trials-corrected audit.

## Valuable ideas and results

1. **Theorem 1: the quartic is the minimal polynomial** (Sec. 4). The proof runs
   over the Galois orbit in Q(√3, √19). As a side result, sin²θ is
   ruler-and-compass constructible.
   *Why:* it turns a numerical agreement between two corpus lines into an
   identity, which prevents double counting.
   *Bears on:* A1 and A3 at (3/4, 2); physres5's trials accounting.
2. **Theorem 2: the branch quartic family** (Sec. 4.1).
   - The quartic's roots are the four branch combinations
     s_ab = 1 − λ_a(J_W)/λ_b(J_Z): 0.2231, 0.5173, 1.2082 and 2.8014.
   - The Galois group acts as branch swaps.
   - Identically in I and K, the roots satisfy
     x⁴ − (4+I)x³ + [6 + 2I − κ(I+2)]x² − (4+I)(1−κ)x + (1−κ)², with κ = I/K.

   *Why:* the negative branch is the Galois conjugate of the positive one, so
   the arithmetic ties the two together, and the family is a ready hypothesis
   class for a look-elsewhere scan over (I, K) that can be registered in
   advance.
   *Bears on:* D4 partner branch; A3 (κ = J_W/J_Z); trials accounting.

3. **Degree-8 corollary.** ρ = m_W²/m_Z² has minimal polynomial
   64y⁴ + 48y³ − 114y² + 18y + 9. m_W/m_Z has degree 8, with minimal
   polynomial 64z⁸ + 48z⁶ − 114z⁴ + 18z² + 9. The proof uses a negative Galois
   conjugate of ρ.
   *Why:* it gives the exact algebraic target for the mass ratio.
   *Bears on:* D1.

4. **Resummation identity** (Prop. 1). f(X) = J/(J + X) has the kernel roots as
   its fixed points. λ₊ is its unique attractor on [0, ∞), with multiplier
   1 − λ₊. f is the zero-frequency Schur reduction of
   [[0, √J], [√J, −(J + X)]], so any nested decimation with uniform rung data
   (√J, J) ends at λ₊.
   *Why:* it gives a level-by-level (Kaluza–Klein-like) origin for the kernel,
   in the Schur-complement language that physres5's interval route already
   uses.
   *Bears on:* D3; D5.

5. **Operator-norm coefficient lock** (Assumption 2, Sec. 9).
   Σ_p |⟨p|J⃗|v⟩|² = ⟨v|J⃗²|v⟩ = J for every state of every representation. The
   reduction onto (|v⟩, J⃗|v⟩/√J) therefore has off-diagonal exactly √J for all
   j, including half-integer j. A mixing gJ⃗ with g ≠ 1 would spoil the
   five-digit m_W/m_Z match, which points to a gauge coupling to isometry
   currents.
   *Why:* it gives a basis-free origin for √J that works at J = 3/4, the
   representation-theory twin of physres6's ‖dφ‖² = J‖φ‖² (which needs S³
   spinor harmonics at half-integer j).
   *Bears on:* A1; D3 (Σ_ha·Σ_ah = J); A3.

6. **Branch sum rules** (Prop. 2, Sec. 7). m₋² − m₊² = J·M∞² and
   m₊·m₋ = √J·M∞² at every j.
   *Why:* any negative-branch identification must satisfy these exact
   constraints.
   *Bears on:* D4.

7. **Vacuum no-go** (Lemma 1, Sec. 7). m₋(1/2) = v/2 and m₋(1) = v/√2 cannot
   both hold. Both would need |λ₋(2)|/|λ₋(3/4)| = 2, but the ratio is
   8(1+√3)/(3+√57) = 2.07173. That is 1.8% in the mass ratio; the data miss by
   −0.58% and +1.18%. The J = 2 match reads compactly as
   v = (1+√3)·m_Z = |λ₋(2)|·m_Z.
   *Why:* it forces a choice of identification, and the v/√2 one is physres6's
   scale tie, which carries its α.
   *Bears on:* D4 partner branch and alpha endpoint.

8. **Tower with an accumulation point** (Sec. 6). Extending the assignment to
   higher j gives levels at 96.54, 99.58, 101.45 and 102.68 GeV. They approach
   M∞ = m_Z√((1+√3)/2) = 106.58 GeV as M∞(1 − 1/2J). With infinitely many
   levels below 107 GeV, either the couplings must fall with j or the tower
   must end.
   *Why:* it turns "higher slots" into concrete, bounded phenomenology.
   *Bears on:* D5 branch scaling and Regge intercept survival.

9. **Label-conservation pattern** (Sec. 6.1). With (γ, W, Z) = (0, 1/2, 1),
   j = 3/2 appears in no neutral two-boson channel, only in W±Z.
   - Single production of the neutral state needs label breaking.
   - Pair production opens at 193 GeV, within the LEP 2 reach of √s = 209 GeV.
   - The pattern is conditional and qualitative: no Lagrangian is given, and
     the 4D spin, CP and width are unspecified.

   *Why:* a LEP 2 recast becomes the sharpest retrodictive test available, and
   FCC-ee is decisive up to 106.58 GeV.
   *Bears on:* D5.
10. **Scheme and data honesty** (Sec. 5).
    - Breit–Wigner and complex-pole masses differ by Γ²/2m ≈ 34 MeV for the Z
      and 27 MeV for the W. That exceeds the experimental errors (about 16× for
      the Z, 2× for the W), and the kernel does not say which mass it predicts.
    - The exact on-shell reading sits about 3σ above the SM global-fit
      m_W = 80.355(6) and would need new physics in Δr.

    *Why:* it states what the pole-placement theorem has to settle.
    *Bears on:* A2; D1 (Δ_match).
11. **κ = 3/8 = C_F/C_A = J_W/J_Z** (Sec. 8). The custodial-EFT coefficient is
    the kernel's own Casimir pair. It is also a coordinate of the Theorem 2
    family: e₃ = e₁(1−κ) and e₄ = (1−κ)².
    *Why:* the kernel, the quartic and κ are one coincidence on the pair
    (3/4, 2).
    *Bears on:* A3.
12. **Trials list** (Sec. 11). The choices to price are:
    - the kernel among 2×2 textures;
    - J = j(j+1);
    - the positive branch;
    - the channel assignment;
    - the m_Z anchor;
    - the on-shell scheme;
    - the tower extension and its link to the 95 GeV hints;
    - the negative-branch matches.

    *Why:* any significance claim must price these choices.
    *Bears on:* physres5's status and tests section.
13. **Attribution trace** (`refs_notes.md`, `refs.bib`). The line runs:
    - from H. de Vries's Physics Forums post #44 of November 2004 (thread "All
      the lepton masses from G, π, e"; the permalink was live on 2026-07-02),
    - through de Vries–Rivero, hep-ph/0503104,
    - to Rivero, hep-ph/0606171, Sec. 3.

    The notes also sort out five references:
    - two distinct Koide papers (Lett. Nuovo Cim. 34 (1982) 201 and
      Phys. Lett. B120 (1983) 161);
    - Sumino's two papers, arXiv:0812.2090 and arXiv:0812.2103;
    - rdss1983, which is the instability paper;
    - the ATLAS 95 GeV search, which is arXiv:2407.07546;
    - the sBootstrap paper, which is arXiv:0710.1526.

    *Why:* physres5's bibliography cites neither the 2004 post nor
    hep-ph/0503104.
    *Bears on:* physres5 provenance.

## Curator's cross-checks (computed 2026-09-23, not in the source)

- **Numbers re-checked.** Every closed form and decimal in `main.tex` was
  recomputed with sympy and numpy (a scratch computation, not archived). The
  check covered:
  - the λ values and the sin²θ radical;
  - the three minimal polynomials;
  - the Theorem 2 identity (symbolic in I and K, with numeric spot checks);
  - the tower masses;
  - M∞;
  - m_W;
  - the pulls, sum-rule percentages and no-go ratio.

  All agree to within last-digit rounding. The precise values are
  m_W = 80.37444 (printed as 80.3745) and a CDF pull of −6.16σ (printed as
  −6.1σ).
- **The flat chain, more sharply than Remark 1.** Take the semi-infinite chain
  with diagonal (0, −J, −J, …) and hopping √J. For J > 1 it has exactly one
  isolated boundary state, at λ = 1 (mass M∞, the accumulation point). For
  J < 1 it has none. Analytically the decay ratio is 1/√J, and a numerical run
  at N = 3000 confirms it. The flat chain never produces λ₊, at any J.
- **Link to physres6.** physres6's scale tie v = √2·M₋(2) is this paper's
  v = (1+√3)·m_Z. By Lemma 1, the two negative-branch identifications give
  different values of α: 1/α = 135.29 under v/√2 and 130.60 under v/2.

## Negative results worth keeping

- **Flat chain.** λ₊ lies inside the essential band [−J − 2√J, −J + 2√J]
  exactly when J < 9/4, which covers both physical Casimirs. Together with the
  cross-check above, the flat chain fails at every J, so any microscopic origin
  has to be a nested decimation.
- **Per-component ladder coupling.** A single matrix element
  ⟨j, m±1|J±|j, m⟩ gives √J only for integer j taken from m = 0. At j = 1/2 it
  gives 1 where √(3/4) is needed. Only the operator-norm version works for
  every j.
- **The v/2 and v/√2 identifications.** At most one can be exact (Lemma 1).
- **Over-determination.** The quartic line, the kernel line and κ = 3/8 all sit
  on the single Casimir pair (3/4, 2), so between them they give one
  confirmation.
- **Draft errors the referee caught.**
  - The first irreducibility proof was false: the {s₁, s₄} pair sums to
    (19 − √57)/8, where the draft had 19/8. The orbit argument replaced it.
  - The draft read the recursion physically as a "Feshbach ladder at zero
    external momentum". That reading was unsound, because a Feshbach
    self-energy depends on energy and must be evaluated at the pole. The final
    text keeps only the static Schur and continued-fraction identity.
- **Data.** A CDF II-like m_W (80.4335) excludes the kernel at −6.1σ, and the
  exact on-shell reading needs new physics in Δr.
- **Diphoton link.** The first draft's "exactly the profile" link to the 95 GeV
  diphoton hints was withdrawn. CMS reports 2.9σ local (1.3σ global) at
  95.4 GeV, and ATLAS reports 1.7σ local.

## Open threads

- **One-loop matching:** fix the scheme and mass definition the kernel predicts
  (physres5 D1, Δ_match).
- **Retrodiction:** follow the pull across PDG editions.
- **LEP 2 and FCC-ee:** recast LEP 2 for pair-produced narrow neutral states at
  96–104 GeV, and scan with FCC-ee up to 106.58 GeV.
- **The tower:** find a mechanism that ends it or decouples it.
- **Trials:** run an auditable trials-factor analysis with the Theorem 2 family
  as the hypothesis class. The corpus Monte Carlo probabilities (10⁻⁴ to 10⁻⁶)
  remain unaudited.
- **Geometry:** sweep coset geometries for one that realizes Assumptions 1–3
  together (physres5 D3).
- **Lagrangian:** write one for the label pattern (referee revision 5, not
  done). A spin-1 tower state cannot decay to γγ (Landau–Yang).
- **Data-table items the referee flagged and the final text keeps:**
  - the "PDG-live 2026" pins m_W = 80.3625(77) and s² = 0.223339(153), marked
    unverified;
  - the on-shell row 0.22305(23), whose central value differs from the 0.22320
    implied by the PDG 2024 masses in the same table.

  For comparison, physres5 uses the pole-mass value 0.2231768 ± 0.0002608.
- **Cosmetic:** `feshbach1958` sits in the bibliography with no citation in the
  text.

## GPT-5.5 referee report (summarized; the file is a session log)

Its verdict on `draft_v1.tex` was "reject in present form". The referee
confirmed the Galois conjugates, the symmetric functions, the continued-fraction
convergence, the sum rules and Lemma 1. It objected to the spectral, dynamical
and collider readings. The table gives the status of its 12 mandatory revisions
in the final `main.tex`.

| # | Revision | Status in `main.tex` |
|---|---|---|
| 1 | Correct the irreducibility proof; prove degree 8 | Done (orbit argument; negative conjugate) |
| 2 | Downgrade Prop. 1 to a continued-fraction identity | Done (resummation identity) |
| 3 | Justify or drop the physical KK/Feshbach ladder | Done: kept as a hypothesis, plus Remark 1 |
| 4 | Treat the tower as an extra assumption; address accumulation | Done |
| 5 | Give a Lagrangian before collider selection rules | Open; the section is recast as a conditional, qualitative pattern |
| 6 | Use accurate diphoton language and significances | Done (local significances quoted) |
| 7 | Use one consistent data table; cite or drop the 2026 pin | Partial (pins kept and marked unverified) |
| 8 | Add the SM electroweak-fit comparison | Done |
| 9 | Define the mass scheme | Open; stated as the largest uncertainty |
| 10 | Treat the negative branch as numerology | Done |
| 11 | Fix the citations | Done, except an electroweak-scheme reference |
| 12 | Run an auditable trials analysis | Open; the trials are listed |

## Left out of the copy

- **`referee_gpt55.md`** (80 KB): a raw Codex CLI session log with the session
  header, shell commands, file dumps and web searches. It is summarized above.
- **`draft_v1.tex`** (40 KB): the superseded first draft that the review
  examined.
- **`README.md`:** the author's overview, folded into this summary. A copy would
  also make GitHub show it in place of this summary.
- **`main.aux`, `main.log`, `main.out`:** build products.
- The source contains no third-party PDFs and no scripts, because of the no-code
  constraint.

## Manifest

Every file is copied unchanged from `/home/codexssh/marathon/`. The hash column
gives the first 12 hex digits of SHA-256. `main.tex` builds with two pdflatex
passes because it carries an inline thebibliography. `refs.bib` is the verified
reference record, kept for reuse in citations.

| File | Bytes | SHA-256 | Content |
|---|---:|---|---|
| `main.tex` | 52093 | 52462fc5a4a6 | Final paper source |
| `main.pdf` | 373831 | 3bdd72cb5504 | Built paper, 14 pages |
| `refs.bib` | 10536 | f0b50cf44e57 | Verified bibliography with disambiguation notes |
| `refs_notes.md` | 10370 | f9f2e5c6972f | Verification notes and the de Vries attribution trace |

Total: 4 files, 446,830 bytes.

