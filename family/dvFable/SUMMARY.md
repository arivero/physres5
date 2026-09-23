# dvFable: pre-registered forcing tests on the coefficient lock

Curated 2026-09-23 for physres5. Target labels (A1-A3, D-pole, D-assign,
D-kernel, D-partner, D-filters) are as in `family/chats-regge-kk/SUMMARY.md`.

## Provenance

- **Source.** `/home/codexssh/dvFable`, a git repository with two commits:
  `e690851` (2026-06-11 13:37: charter, README, symlinks) and `2ca4c70`
  (2026-09-23: goals, calc scripts, loop iterations 1-4, notes).

- **Working dates.** 2026-06-11 13:31 to 2026-06-12 00:37. `OPUS_IDEAS.md`
  was added 2026-07-01.

- **Symlinks into dv2**, which were not followed: `PRIOR-AGENT.md`,
  `loop-history/`, `prior-work/`, `corpus/`, `references/`. Their content is
  covered by `family/dv2/` and `family/chats-regge-kk/`. `CLAUDE.md` points
  to `AGENTS.md`.

- **Method.**
  - Each iteration had two arms: Codex GPT-5.5 (xhigh) and a Claude (Fable
    5) agent. One argued for a construction, the other against, and they
    swapped roles every iteration.
  - Every algebraic claim in a verdict has a SymPy/NumPy check in `calc/`
    that asserts and exits 0.
  - Iteration 2 used GPT-5.5 in both seats after three infrastructure
    failures on the Claude side. The run logged this as a deviation.

- **Sister run.** The sister run `~/kkFable` (on the space `X_{1,1}`) was
  read once, read-only. It is outside this folder.

## Goal and final conclusion

**Goal.** `GOALS.md` (fixed 2026-06-11) pre-registers three terminal states:

- **T1 FORCED**, with five conditions:
  1. the principle can be stated without reference to the measured angle;
  2. the lock is a theorem;
  3. the channel assignment is an output;
  4. the principle explains why Sugawara fails;
  5. the result survives an adversarial round and predicts something it was
     not fitted to.

- **T2**, an unrestricted no-go.

- **T3**, a quantified coincidence backed by a pre-registered look-elsewhere
  accounting.

The gating question: is there a principle that forces the lock
(`r = gamma/alpha = 1` with `A^dag A = C 1` and no level shift) and outputs
the assignment `gamma: 0`, `W: 1/2`, `Z: 1`?

**Final state.** No terminal state was reached. The candidate principles
closed as follows:

| Candidate | Principle | Verdict |
|---|---|---|
| (b') | open-channel compositeness, `Z = 0` | ruled out on entry: `Z^-1 = 1 + C/(X_+ + C)^2 > 1` |
| (d) | 4D gauge/Stueckelberg invariance, locality, one scale | dropped after two failed rounds (iterations 1-2) |
| (b) | Hubbard-Stratonovich origin of `V = X^2/2 - C log(X+C)` | ruled out: any such construction gives `X = GC/(X+C)` |
| (h) | single trace-normalized Yang-Mills term (gauge-Higgs) | ruled out for the whole class (iteration 3) |
| (c) | relativistic orbit `beta^2 gamma = sqrt C` (the 2005 construction) | interim: the arguing-against arm found it unforced and likely dead; the arguing-for arm never returned |
| (i), (a), (e), (g) | Hessian functional; WZW map selection; exact duality; global-form channel selection | queued |

Every closed class leaves the same free number: `g^2/alpha = 1`,
equivalently `Sigma_j(0) = mu^2` in every channel. The 2026-07-01 review
named T3 as the likely end state. The look-elsewhere engine T3 needs was
never built.

## Valuable ideas and results

1. **Frozen scorecard and the physres5 datum.** *Bears on:* A2, D-pole.

   | Datum | Convention | `sin^2` | Pull |
   |---|---|---|---|
   | PDG-live 2026 W 80.3625(77), Z 91.1880(20) | Breit-Wigner | 0.223339(153) | +1.56 |
   | same | pole | 0.223280(153) | +1.17 |
   | CMS 2026 W 80.3602(99) | Breit-Wigner | 0.223383(194) | +1.45 |
   | PDG direct ratio 0.88136(15) | as quoted | 0.223205(264) | +0.39 |
   | physres5 Sec. 3 (PDG 2025 W 80.3692(133)) | pole | 0.2231768(2608) | +0.29 |
   | PDG-live 2026 W, physres5 conversion (`Gamma_W = 2.14`) | pole | 0.2233064(1527) | +1.34 |

   The last row is my recomputation. The pull depends mainly on which W
   average is used. About three significant digits match. `(1/2, 1)` stays
   the only half-integer pair within 3 sigma for `j <= 4`.
   Files: `notes/2026-06-11-empirical-scorecard.md`,
   `calc/scorecard_2026.py`.

2. **One equation in three forms** (A1). The orbit form
   `X_+ = beta^2, beta^2 gamma = sqrt C`, the gap form `X = C/(X+C)` and the
   quadratic are one equation, with `X_W = (sqrt57 - 3)/8` and
   `X_Z = sqrt3 - 1`. File: `calc/devries_core.py`.

3. **The lock, stated once** (A1, D-kernel). Every realization needs three
   conditions:
   - **B1**, induced gap: `mu^2 H_QQ = H_QP H_PQ`. Equivalently,
     `Sigma_j(0) = mu^2` in every channel, or `g^2/alpha = 1`.
   - **B2**, minimal portal: an unsubtracted self-energy with a single
     vertex.
   - **B3**, the same kinetic normalization in every channel.

   In physres5's Appendix D notation:
   - `Sigma_ha Sigma_ah = Sigma_aa` is B1;
   - `Sigma_hh = 0` is B2;
   - the unit coefficient of `lambda` in both channels is B3;
   - `Sigma_aa = J` is the bare-Casimir map.

   Generic values give `x^2 + J x - r^2 J = 0`.

4. **Gauge invariance does not fix r** (A1, D-kernel).
   - With only the fields `(p, Q)`, every local gauge-invariant quadratic
     action gives `Gamma_P(B) = B R(B)`: the open channel stays massless.
   - Adding the Goldstone gives a five-parameter invariant family through
     the de Vries point, with pole polynomial `X^2 + C X - r^2 C`.
   - Every such statement is unchanged under `A -> cA`, `C -> c^2 C`, so
     symmetry cannot choose between the zero-mode map (0.2231) and the `L0`
     map (0.3014).

5. **The square root has to come from a resolvent** (D-kernel).
   - `X_+(C)` is not a rational function of `C`, because `C(C+4)` is not a
     perfect square.
   - So a mechanism that matches for all `C` must contain a resolvent (a
     Schur complement). A rational kernel fitted at `C = 3/4` and `C = 2`
     would be over-fitting.

6. **Single-trace Gram theorem** (D-kernel, physres5 Secs. 6c-6g).
   - For every internal background, a single Yang-Mills trace gives the
     transverse kernel `B + D^dag D`.
   - So the static Schur complement is at least zero, the couplings obey
     the cone `gamma^2 C <= s(alpha C + m_0^2)`, and the spectrum is a
     plain sum with no genuine resolvent.
   - The coefficients are fixed, but they land in the Manton class of
     rational angles (SU(3) 3/4, O(5) 1/2, G2 1/4).
   - The algebraic `C` sits in the vertex and a Laplacian eigenvalue in the
     gap: `C - q^2` on `S2` with flux, giving controls 0.2968/0.3170; `4C`
     on `S3`. So in a geometric reduction `Sigma_aa` and
     `Sigma_ha Sigma_ah` come from different operators.
   - An interval/CHM or G2 route built on one Yang-Mills trace therefore
     needs brane-localized or loop terms, and those bring the free number
     back.

7. **Curator's note: the determinant obstruction** (my translation of the
   bound above into physres5 notation; D-kernel, D-pole).
   - The Appendix D target has `det K_J(0) = -J < 0`.
   - If the static kernel is, up to sign, the static Schur complement of a
     positive source operator (a unitary bulk with an invertible heavy
     sector, plus non-negative boundary terms), its 2x2 determinant is at
     least zero.
   - So a route needs one of three indefinite ingredients: a
     tachyonic-sign boundary mass; a wrong-sign kinetic term; or a pole
     map in which `lambda` is not the mass-squared of a positive operator.
   - Shifting `lambda` by a constant `s_0 >= J + x_+` restores positivity,
     but it changes the predicted ratio, because the relation uses `x_+`
     itself as the mass-squared ratio.

8. **Spectral principles leave the lock free** (D-kernel).
   - KSRF I holds for every value of the parameter `a`. KSRF II is
     equivalent to `a = 2`, which is vector dominance, a dynamical input.
   - A positive, causal counterexample
     `gamma^2 mu^4 C/(B + m_0^2 + lambda mu^2 C)` shows that forbidding
     extra poles (CDD factors) is a choice.
   - The bootstrap closure `h s = (w-1) g^2` is satisfied by every `h`.

9. **Residue bound** (D-pole). `Z^-1 = 1 + C/(X_+ + C)^2`, so
   `Z_W = 0.699` and `Z_Z = 0.789`. A pole map in this realization carries
   residues below one.

10. **The orbit reading, audited** (A1, D-filters).
    - The period weight is the lock: `T = k h/(m_0 c^2)` gives
      `gamma beta^2 = sqrt C/k`. Variants give 0.2231, 0.2077 (proper-time
      clock), 0.1198 and 0.3571.
    - A rigidly rotating string gives the Regge form `J = E^2/(2 pi sigma)`.
    - At a common radius, the central force needed differs between the two
      channels by a factor 1.853.
    - Half-integer orbital angular momentum at `j = 1/2` is forbidden.

11. **Quadratic-shape inventory.**
    - `X^2 + c_1 X - c_2 = 0` appears everywhere: sphere harmonics, AdS
      masses, the Poincare-Casimir form.
    - The de Vries content is the single condition `c_1 = c_2`.
    - Useful for pricing look-elsewhere in T3.

12. **The sister run agrees** (A1, A3).
    - kkFable isolated the same two postulates by its own route.
    - A spin-c Dirac square gives `C_G - C_K + |rho|^2`, not the bare
      `j(j+1)`.
    - On its carrier the `j = 1/2` slot carries colour.
    - Its geometric angles are either rigid and wrong, or set by a free
      modulus.

13. **A sharper acceptance standard.** The five T1 conditions refine
    physres5's Appendix D acceptance criterion. Condition 4 is the most
    useful: a valid principle must explain why Sugawara fails.

## Negative results worth keeping

- Candidates (b'), (b), (d) and (h) are closed, as tabled above.

- **The orbit reading (c)** is at best a mnemonic for the gap form. No
  published action derives the period condition.

- **Geometric map selection** is answered negatively by the vertex/gap
  split.

- **Withdrawn claims:**
  - "kappa = 1 from the canonical `X^2/2` norm";
  - "0.42 sigma";
  - dv2's "conditional gauge pass" (it was only internal covariance);
  - dv2's three in-loop articles, labelled "displacement activity" in the
    goals.

- **Correction:** Manton's SU(3) value is `sin^2 = 3/4`; 1/4 belongs to G2.
  This affects dv2 `AGENT.md`, `claudeFinal.tex` and the PRL.

## Open threads

- **(i) Hessian formulation.** A first-order operator whose second
  variation is `[[0, D^dag],[D, -c D^dag D]]` with `c = 1` forced. As a
  saddle Hessian it escapes the positivity bound. Test: find a class of
  functionals that fixes `c`, or show `c` stays free (OPUS_IDEAS item 1).
  *Bears on:* A1, D-filters.

- **(g) Global form and line operators.** Does any global form allow
  `j = 3/2` while keeping the assignment? *Bears on:* A3, D-assign,
  physres5 Sec. 8.

- **(a)** WZW map selection at level 2; **(e)** an exact duality that
  pins `r = 1`.

- **Loop-level Hosotani dynamics.** Would need to derive `g^2/alpha = 1`.

- **Bracken-Green characteristic identities.** Needs a literature pass
  before it can be admitted.

- **The T3 look-elsewhere engine.** Enumerate the hypothesis classes in
  advance and score them against the frozen datum (OPUS_IDEAS item 2).
  *Bears on:* A2, D-pole.

- **Iteration 4's arguing-for output is missing.** The geometric embedding
  and the paper wait for a terminal state.

## Manifest of copied files

All files are byte-identical copies; none was edited. The scripts need
SymPy and NumPy; all eight exited 0 when re-run on 2026-09-23.

| Path | Bytes | Content |
|---|---:|---|
| `README.md` | 2097 | mission and layout (symlink paths refer to dv2) |
| `GOALS.md` | 9863 | goal tree, terminal standards, anti-goals, protocol |
| `notes/LOG.md` | 15586 | loop log, iterations 0-4 |
| `notes/2026-06-11-empirical-scorecard.md` | 2897 | frozen datum |
| `notes/2026-06-11-forcing-candidates-ledger.md` | 14052 | candidate ledger |
| `notes/2026-06-11-iter1-gauge-lock-verdict.md` | 6171 | iteration 1 |
| `notes/2026-06-11-iter2-boundary-verdict.md` | 4992 | iteration 2 |
| `notes/2026-06-12-iter3-ghu-verdict.md` | 5411 | iteration 3 |
| `notes/2026-06-11-quadratic-shape-inventory.md` | 3714 | `(c1,c2)` family |
| `notes/2026-06-12-kkfable-cross-import.md` | 4481 | sister-run import |
| `calc/devries_core.py` | 2766 | forms, values, residues, Sugawara control |
| `calc/scorecard_2026.py` | 3615 | pulls, pole shift, uniqueness |
| `calc/iter1_gauge_lock.py` | 7740 | iteration 1, arguing-for algebra |
| `calc/iter1_adversary_checks.py` | 5259 | iteration 1, arguing-against algebra |
| `calc/iter2_boundary_checks.py` | 3329 | KSRF, CDD, bootstrap |
| `calc/iter3_checks.py` | 5834 | Gram theorem, Manton and monopole controls |
| `calc/iter4_orbit_checks.py` | 3945 | orbit weights |
| `calc/quadratic_shape_family.py` | 2724 | shape inventory |

Total 0.10 MB (18 files).

**Not copied:** `AGENTS.md`, `OPUS_IDEAS.md`, the 16 loop PROMPT/OUT agent
logs, and the symlinks.

Mentions of `PRIOR-AGENT.md` and `loop-history/` now correspond to
`family/dv2/AGENT.md` and `family/dv2/loop/` (a subset). References to
`loop/OUT-*` are dangling. There are no absolute paths, emails or tokens.

