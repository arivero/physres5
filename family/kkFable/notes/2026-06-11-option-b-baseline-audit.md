# N0 — Option-B baseline audit: inherited state, provenance, acceptance ledger

Date: 2026-06-11.
Status: process note (inventory and source-status ledger; no physics verdicts here).

## Purpose

kkFable resolves the open fork raised 2026-05-31 in `wastebook.md`: which SU(3)
does the CP² base of X_{1,1} carry? Option A (all prior physics): base SU(3) =
electroweak. Option B (this workspace): base SU(3) = colour SU(3)_c, fibre
S³/SO(3) = electroweak SU(2)_L. This note records what Option-B material
already exists, where the inherited ledgers disagree, and which inherited
claims kkFable accepts by citation versus re-derives by hand.

## Provenance discrepancy (recorded, not repaired)

- `wastebook.md`, entry **[OPEN FORK, user-raised 2026-05-31] "Which SU(3)?"**,
  ends: "Candidate task R5: work out the flipped identification. NOT YET RUN."
- The archive of the same verification campaign contains a **completed R5
  run**: `archive/verification_20260531/R5.md`, with the full task answered
  ((a) breaking pattern, (b) U(1)_Y triage, (c) θ_W re-derivation, (d) verdict
  table) and **two independent adversarial verification passes** appended, the
  second of which issues one MAJOR correction (the gauge-rank deficit).
- `tasks/R5.md` is the prompt that produced it.
- The kkFable charter (`README.md`/`CLAUDE.md`, 2026-06-11) quotes the
  wastebook phrasing, so it was written against the stale ledger state.

Reading: the wastebook entry predates the R5 execution and was never updated;
the archived run is genuine prior work. The wastebook is symlinked read-only
history and stays as is; this note and the final ledger
(`notes/OPTION-B-VERDICTS.md`) carry the corrected state.

User decision (2026-06-11, this session): **audit and build on R5** — cite it
as a prior source, re-derive by hand every load-bearing claim that enters a
verdict row, and direct new effort at what R5 left open.

## Inventory of inherited Option-B-relevant material

| Item | Where | Content relevant to Option B |
|---|---|---|
| R5 run | `archive/verification_20260531/R5.md` | breaking-pattern consistency; U(1)_Y triage (3 candidates, 1 survivor); sin²θ_W = (1+t)/(2+t) free modulus; A-vs-B verdict table; verification pass 2: rank-4-vs-3 deficit (MAJOR), hypercharge-spectrum doubt (MINOR) |
| R5 prompt | `tasks/R5.md` | task statement; note its parenthetical "rank 2+1=3 = rank of SM" is FALSE (SM rank = 4), already flagged inside R5 |
| T1 | `archive/verification_20260531/T1.md` | spin^c line L = O(k), k odd; X_{1,1} spin; charge-n bundle = O(n) along the λ_8/U(1)_{1,1} direction; Kreck–Stolz data |
| T2 | `archive/verification_20260531/T2.md` | invariant metrics 10→2→1; m_0 = fibre (scale x1), m_3 = base (scale x2), Wilking t = x1/x2 − 1; Einstein points t = +1, −3/5 |
| T3 | `archive/verification_20260531/T3.md` | Killing-inertia coupling rule 1/g² ∝ block scale; Schur rigidity inside a simple factor; cross-factor ratio free |
| T4 | `archive/verification_20260531/T4.md` | SU(3)→SU(2)×U(1)_8 branching tables; parity law q8 ≡ 2I (mod 2); doublet census (all doublets at odd q8, minimal 2_{±3} in the 8); Casimir j=1 on m_0, j=1/2 on m_3; centralizer(su(2), su(3)) = u(1)_8; so(4) = 6 > u(2) = 4 obstruction; its verification pass corrects the L/R quaternion labels |
| T5 | `archive/verification_20260531/T5.md` + wastebook C7 | De Vries signed-Hessian algebra: a_J = (√(J²+4J)−J)/2; EW assignment j=1/2 → J=3/4, j=1 → J=2; cos²θ_W = a_{1/2}/a_1 ⇒ sin²θ_W = 0.2231; c=1 and D†D = j(j+1) are extra postulates |
| T6 | `archive/verification_20260531/T6.md` + wastebook C6 | Witten odd-dimension chirality no-go ACTIVE for X_{1,1}; spin^c does not evade it; CDF citation corrected to M^{p,q,r} = U(1) bundle over CP²×S², isometry SU(3)×SU(2)×U(1) |
| R4 | `archive/verification_20260531/R4.md` | 1/4 vs 3/8; 3/8 needs colour+EW inside one simple group; CP³ = SU(4)/U(3) Pati–Salam |
| Dolan–Nash material | `docs/KaluzaKlein_Hilo_Higgsing_KaluzaKlein_Review.md` (lines ~1485, 2291–2399, per R5's verbatim extraction) | U(1)_Y as background flux on CP²; spin^c index ind D_n = (n²−1)/8; n=3 → 1 generation, n=5 → 3 |

## Acceptance ledger (cited vs re-derived vs new)

Standing constraint: **no Python in kkFable.** All prior sympy artifacts
(`calc/`, `/tmp/r5_*.py`) are historical corroboration only; any number or
identity that enters a kkFable verdict row is re-derived by hand in the note
that uses it.

| Claim | Source | kkFable treatment |
|---|---|---|
| C1–C4 geometry (Kuiper–Massey, fibration, Wilking form, spin/spin^c, 3-Sasakian) | wastebook Established + T1/T2 | **cited, not redone** (charter instruction; identification-independent) |
| Isometry group = SU(3)×SO(3), no larger | Wilking 1999 via T2/T3 | cited (theorem in the literature); the existence of the SO(3) factor re-derived by hand in N1 |
| Rank deficit (Option B needs rank 4, carrier has 3) | R5 verification pass 2 | **re-derived by hand** in N1/N2 (load-bearing) |
| U(1)_Y candidate kills: bare lift, colour-λ_8 | R5(b) | **re-derived by hand** in N2 (load-bearing) |
| sin²θ_W = x1/(x1 + k_Y x2) free modulus | R5(c) + T3 | **re-derived by hand** in N3 (load-bearing) |
| Branching tables, parity law q8 ≡ 2I (mod 2) | T4 + its verification (two independent computations: Schur characters and Gelfand–Tsetlin) | cited; the parity law additionally gets a one-line structural proof in N2/N6 (central element argument), independent of tables |
| Spin^c index (n²−1)/8 | docs (Dolan–Nash) via R5 | **re-derived by hand** in N6 (one-line characteristic-class integral) |
| De Vries algebra (a_J, b_J; 0.2231 at c=1) | T5/wastebook C7 | cited as algebra; only the slot ASSIGNMENT is re-examined (N5); the c=1 and D†D = j(j+1) postulates stay flagged open, not relitigated |
| Witten odd-dim no-go active; spin^c does not evade | T6 | cited (N7); identification-independent |
| Custodial re-derivation under Option B | — absent from R5 | **new work** (N4) |
| De Vries EW reassignment under Option B | — absent from R5 | **new work** (N5) |
| Hypercharge locus / matter spectrum under Option B | only a MINOR doubt in R5 verification | **new work** (N6) |
| Charter candidate: fibre SO(3)→SU(2) lift obstruction as the U(1) completing EW, strong (U(2)-lift) form | — absent from R5 (R5 killed only the bare double-cover form) | **new work** (N2) |

## Conventions fixed for all kkFable notes

- H8 := diag(1,1,−2) (the U(1)_{1,1} generator, antihermitian factor i
  suppressed); q8 := H8-eigenvalue. λ_8-normalized versions differ by 1/√3 and
  are not used.
- Isotropy chain: U(1)_{1,1} = Z(U(2)) ⊂ U(2) = S(U(2)×U(1)) ⊂ SU(3).
- m_0 = vertical (fibre) block, metric scale x1; m_3 = horizontal (base CP²)
  block, scale x2; Wilking modulus t = x1/x2 − 1.
- I = fibre SO(3)/SU(2) spin of a 4D mode (T4's j); the letter J is reserved
  for the De Vries Casimir value J = j(j+1) in N5.
- Option-B map: left SU(3) factor → SU(3)_c; right SO(3) factor → SU(2)_L
  (weak); any hypercharge-like charge is written Y with its normalization
  stated where used.

## Pointers

Derivation notes this audit feeds: N1 (dictionary/rank budget), N2 (U(1)_Y),
N3 (θ_W), N4 (custodial), N5 (De Vries), N6 (hypercharge locus/matter),
N7 (chirality), N8 = `notes/OPTION-B-VERDICTS.md` (deliverable ledger).
