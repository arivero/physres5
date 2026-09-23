# dv2: clean restart, gap-equation reformulation, and the D10 boundary-current milestones

Curated 2026-09-23 for physres5. Target labels (A1-A3, D-pole, D-assign,
D-kernel, D-partner, D-filters) are as in `family/chats-regge-kk/SUMMARY.md`.

## Provenance

- **Source.** `/home/codexssh/dv2`, a git repository with two commits:
  `ab7433c` (2026-05-25, "paper") and `710399a` (2026-09-23, archive commit).
  558 files, 37 MB, of which 15 MB are third-party PDFs and 1.7 MB a corpus
  copy.

- **Working window.** 2026-05-25, from 12:14 to about 18:30 CEST, per
  `loop/LOOP-LOG.md` (whose timestamps are partly out of order). A review
  subagent added `OPUS_IDEAS.md` on 2026-07-01.

- **Method.**
  - Each sub-question went to a Codex arm (GPT-5.5, xhigh) and a Claude Opus
    arm, and the two answers were cross-checked.
  - The Claude arm ran out of tokens during iteration 2. After that, the
    Codex arm worked alone ("solo" in the log), following user directives.

- **Relation to siblings.**
  - `prior-work/` is the chats workspace as of the fork; the later versions
    are in `family/chats-regge-kk/`.
  - `corpus/` equals `chats/devries-string-2026-05-24-{clean,index}`.
  - dv2 added `d10-superstring-kk-brane-symmetry.md` and ledger row C88 to
    its prior-work copy. Both are contained in
    `paper/d10-unified-boundary-current-vacuum.tex`, Part I.
  - dvFable symlinks `AGENT.md`, `loop/`, `prior-work/`, `corpus/` and
    `references/`.

## Goal and final conclusion

**Goal (AGENT.md).** Decide whether the de Vries relation has a physical
origin or is a coincidence, and write the answer up at Phys. Rev. D
standard, as a test of LLM research on an open problem. The rule was
solve-or-no-go. A later user "CORRECTION" made construction the default and
admitted only unrestricted no-gos. User directives then added D10 brane
articles and a seven-milestone plan.

**Conclusions.**

1. **A(J) cannot be an elementary gauge mass matrix.** This is a positivity
   (PSD, Gram) argument, and both arms derived it independently.
   AGENT.md itself calls this no-go circular as a verdict on the relation,
   since it removes only one reading of the numbers.

2. **The quadratic has a positive, unitary reformulation** as the
   self-consistency (gap) equation `X = C/(X+C)`. There are three
   realizations:
   - a rainbow/NJL bubble;
   - a rank-one Feshbach two-channel Hamiltonian;
   - the large-N saddle of `V = X^2/2 - C log(X+C)`.

   Each carries one free normalization. dvFable later withdrew the
   iteration-1 claim that the canonical `X^2/2` norm fixes it.

3. **The D10 boundary-current route forces nothing.** The seven milestones
   end in a scoped theorem. Setting: Type IIA on `M4 x CP2 x CP1`, a D8-like
   boundary `W9 = M4 x CP2 x S1_Q`, Payen endpoint variables and Borel-Weil
   sectors. Under these assumptions, at least one mandatory pass condition
   fails on every path that would make the number a prediction. The file's
   summary: "D10 boundary data are compatible with de Vries"; the route does
   not force it.

4. **The pull grew with new data.** Against 2026 W-mass inputs the on-shell
   pull is 1.45 to 1.56 sigma, up from the 0.42 sigma quoted at the start.

## Valuable ideas and results

1. **Positivity (PSD/Gram) bound.**
   - A PSD matrix with a zero diagonal entry has a vanishing row. A(J) has
     `M11 = 0` and `M12 = sqrt J`, so it is not PSD.
   - By Sylvester's law its signature (1,1) survives any positive kinetic
     redefinition. So Q(J) has to be read as a reduced kernel, a Hessian or
     a pre-Goldstone object, never as an elementary mass-squared matrix.
   - Loopholes checked:
     - the propagator reading gives a tachyon or ghost;
     - scalar-vector mixing disappears in unitary gauge;
     - the 5D interval operator is positive;
     - monopole harmonics with half-integer j give a positive operator;
     - the complex-pole shift (about 3e-4) is far too small.
   - Loopholes left open: a composite or magnetic-dual W, and a
     Proca/non-gauge vector.
   - *Bears on:* A1, D-kernel. The kernel form of this bound, in physres5
     notation, is in the curator's note of `family/dvFable/SUMMARY.md`.

2. **Mass ratio versus coupling ratio.**
   - The de Vries relation contains no `g` or `g'`. It matches the SM angle
     only once `rho = 1` is imposed.
   - On physres5's electroweak ray, `M_W^2/M_Z^2 = g^2/(g^2+g'^2)`, so the
     relation fixes `g'/g`. A derivation therefore has to output a coupling
     ratio or Weinberg-length ratio.
   - *Bears on:* D-assign, A3.

3. **Gap form.**
   - `X = C/(X+C)` gives a rank-one Feshbach
     `H_eff = mu^4 C/(E - mu^2 C)`, with positive Kallen-Lehmann density
     `mu^4 C delta(nu - mu^2 C)` and positive residue. The solution
     saturates, `0 < X_+ < 1`.
   - This is physres5's Schur-complement kernel with one closed channel.
   - File: `paper/devries.tex`.
   - *Bears on:* A1, D-kernel, D-filters.

4. **The lock as one number.**
   - A generic local image oscillator gives `X = r^2 J/(X+J)` with
     `r = gamma/alpha`. De Vries needs `r = 1`.
   - A single displacement square,
     `alpha mu^2 ||A^dag Q - p||^2 - alpha mu^2 ||p||^2`, forces
     `gamma = alpha`. The field-normalization-invariant form is
     `c_m = c_g Z_q^(1/2)`.
   - This is physres5's condition `Sigma_ha Sigma_ah = Sigma_aa`.
   - File: `loop/milestone1-q-oscillator-coefficient-lock-2026-05-25.md`.
   - *Bears on:* A1, D-kernel.

5. **Wilson-contact bookkeeping.**
   - The raw Wilson second variation gives contact `-mu^2 J_j`, while the
     finite branch needs `-mu^2`.
   - The unit inverse image metric equals the static Schur complement of a
     retained image oscillator.
   - The Wilson second derivative is a connected two-current response, so
     it must not be added again as a 1PI contact.
   - Files: `loop/milestone1-wilson-contact-residue-*`,
     `loop/milestone1-connected-1pi-*`.
   - *Bears on:* D-kernel.

6. **Mixed Hom sector.**
   - `H^0(CP1, Hom(O(0),O(2j))) = V_j` supplies the image field
     `Q_j = A_j y_j/sqrt(J_j)` inside `Im A_j`.
   - Neither Payen nor the D8 DBI/WZ terms supply the needed one-square
     action, so `r = c_g sqrt(Z_y)/c_m` stays free.
   - This names the local term that a disk-level string computation would
     have to produce.
   - *Bears on:* A1, D-kernel.

7. **Current-metric normalization.**
   - The KK current metric `G_ab = L_2^2 delta_ab` gives `kappa_cur = 1`
     when the full current couples.
   - If the boundary sees only the horizontal current, the Bailin-Love
     split (`beta = 0.328482`) gives `kappa = 0.75274` and
     `sin^2 = 0.24227`.
   - File: `loop/milestone3-current-metric-execution-2026-05-25.md`.
   - *Bears on:* A1, D-kernel.

8. **Finite branch versus tower branch.**
   - Finite branch: `SU(2)_2` gives exactly `{0,1/2,1}` and removes
     `j=3/2`. The photon is `j=0` (`A_0 = 0`, `Q eta_0 = 0`); the W is the
     lowest centre-odd sector; the Z is the lowest centre-even non-singlet
     in `1/2 x 1/2 = 0 + 1`.
   - Tower branch: a Peter-Weyl rotor gives the gap `mu^2 j(j+1)` and keeps
     `j=3/2` at 96.54 GeV and `j=2` at 99.58 GeV.
   - *Bears on:* A3, D-assign, D-filters.

9. **Source test for the image channel.** Five candidate sources were
   tested: D8 normal mode, endpoint rotor, boundary-current oscillator,
   Hubbard-Stratonovich field and RR vertical mode. Only the
   boundary-current oscillator supplies a propagating `Im A_j` pole.
   *Bears on:* D-kernel.

10. **2026 phenomenology.**
    - Predicted `M_W = 80.3748 GeV`.
    - On-shell pull +1.56 sigma with the PDG-live W mass
      (80.3625 +- 0.0077) and +1.45 sigma with the CMS 2026 W mass
      (80.3602 +- 0.0099).
    - The raw scalar scale is 122.39 GeV against `m_H` = 125.20 +- 0.11.
    - `j=3/2` sits 1.14 GeV above the CMS 95.4 GeV diphoton feature (2.9
      sigma local, 1.3 global).
    - The relation must never be compared with
      `sin^2 theta_eff = 0.23148`.
    - *Bears on:* A2, D-pole, D-partner, D-filters.

11. **Selector-potential slice** (compatibility data only).
    - `kappa_cur = 1`, `v_Q^2 = mu_B^2 (1 + sqrt3)`,
      `lambda_H = (3 + sqrt57)/(32 (1 + sqrt3)) = 0.12067`,
      `M_H^2 = 2 lambda_H v_EW^2`.
    - This spells out what a scalar functional `F_sc` would have to output.
    - *Bears on:* D-partner.

12. **D10 carrier picture** (`paper/d10-unified-...`).
    - KK symmetry as a target-space symmetry of the IIA sigma model.
    - D0 as the electric `C1` probe.
    - The D8-like object on `W9` as the source of the Romans mass.
    - The spin-c line `F_Q/2pi = 6 h_Q + x/2` (Freed-Witten on `CP2`).
    - *Bears on:* D-kernel inputs.

## Negative results worth keeping

- **A(J) as an elementary Higgs/KK mass matrix.** Excluded, as above.

- **Standard gauge-Higgs unification on `S2`** (Lim-Maru-Hasegawa
  computation). It gives a Goldstone plus a separate scalar, with no Schur
  block. Gauge-Higgs unification supplies only the bare-Casimir portal.

- **Wrong normalizations.** Direct Sugawara `L0` gives 0.3014 and the
  horizontal-only current 0.2423.

- **D8/O8 source balance on `CP2 x CP1` and the flag manifold fails.**
  - The minimal spin-c lift leaves lower charge `208 h_Q + 673 h_Q^2`.
  - Balanced opposite lifts leave `(4M^2 - 3) h_Q^2`, at least `h_Q^2`.
  - `H^3 = H^5 = 0`, so H-flux cannot cancel it, and bare K-theory cannot
    erase it.
  - The product O4/O6 package `-4k h_Q - k h_Q^2` fails the congruences:
    D6 cancellation needs `k = 0 mod 4`, while the D4 coefficient is
    `1 mod 8`.
  - The route is closed; reviving it needs a new compactification ansatz.

- **Vacuum and scalar sector.**
  - Bulk stationarity gives two equations for seven coefficients, so any
    `rho` can be made stationary.
  - The selector terms do not select `rho` and `tau`.
  - The radial Hessian has enough free coefficients to fit `m_H`.
  - Result: no vacuum or Higgs prediction.

- **Extra light modes.** An unprojected image field leaves a massless
  complement, and the rotor tower keeps light states near 96 to 100 GeV.

- **Iteration 2.** The selection-rule question produced nothing usable.

## Open threads

- **Derive the Hom one-square boundary term** from disk-level two-point and
  contact terms of the Payen endpoint action coupled to D8 DBI/WZ
  (OPUS_IDEAS item 1). *Bears on:* A1, D-kernel.

- **A new compactification ansatz for the `-h_Q^2` deficit** (lens-space
  `S1_Q` fibrations, flag, branched covers), with an automated
  charge-lattice congruence checker (item 2).

- **Milestone 7 in full** (item 3): on-shell to MS-bar conversion, running of
  `lambda_H` from 0.12067, and a production estimate for `j=3/2`.
  *Bears on:* A2, D-pole, D-filters.

- **The open positivity loopholes:** a composite or magnetic-dual W, and a
  Proca/non-gauge vector. dvFable queues these as candidate (e).

## Manifest of copied files

All files are byte-identical copies; none was edited. The three .tex files
build standalone.

| Path | Bytes | Content |
|---|---:|---|
| `AGENT.md` | 17729 | distilled state: PSD bound, red-team verdict, CORRECTION rule, lead |
| `paper/devries.tex` / `.pdf` | 6794 / 133440 | "A self-consistency reading", 2 pp |
| `paper/d10-new-advances-2026-05-25.tex` / `.pdf` | 34854 / 281481 | final article with the scoped theorem, 13 pp |
| `paper/d10-unified-boundary-current-vacuum.tex` / `.pdf` | 59340 / 341826 | combined article, 22 pp |
| `loop/LOOP-LOG.md` | 42985 | loop journal, all verdicts |
| `loop/long-term-devries-research-plan.md` | 19438 | seven milestones, pass/fail rules |
| `loop/goal-completion-audit-2026-05-25.md` | 5493 | milestone audit |
| `loop/current-route-no-prediction-theorem-2026-05-25.md` | 3487 | scoped theorem |
| `loop/milestone-execution-summary-2026-05-25.md` | 7734 | summary and fork |
| `loop/milestone1-*` (7 notes) | 26587 | image-channel sources, rotor, Wilson residue, 1PI test, lock, Hom tests |
| `loop/milestone2-representation-assignment-execution-2026-05-25.md` | 3122 | assignment |
| `loop/milestone3-*` (2 notes) | 7406 | current metric, D8/RR placement |
| `loop/milestone4-5-vacuum-rank-selector-test-2026-05-25.md` | 3395 | vacuum rank |
| `loop/milestone5-neutral-scalar-hessian-rank-test-2026-05-25.md` | 3357 | scalar Hessian |
| `loop/milestone6-*` (4 notes) | 12487 | mass gaps, source balance, repair requirements, decision |
| `loop/milestone7-phenomenology-execution-2026-05-25.md` | 4614 | 2026 data |
| `loop/jthreehalf-diphoton-phenomenology-check-2026-05-25.md` | 3012 | 96.54 GeV check |

Total 1.02 MB (30 files).

**Not copied:**

- `references/` (third-party PDFs), `corpus/` (duplicates chats) and
  `prior-work/` (duplicates chats).

- The loop PROMPT/OUT agent logs (verdicts summarized above).

- `d10-kk-branes` and `d10-boundary-action` (contained in the unified
  article).

- 18 intermediate milestone notes, `README.md`, `OPUS_IDEAS.md` (summarized
  under open threads) and build logs.

Links from the notes to uncopied loop notes are left dangling. One absolute
path appears: `/tmp/d10-new-advances-2026-05-25.pdf` in the goal audit, a
temporary copy, left as-is.

