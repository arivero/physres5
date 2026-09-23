# Forcing-candidates ledger (G1.1)

**Verdict line: LIVE LEDGER (updated per iteration). Status values:
QUEUED / RUNNING / KILLED / RETIRED (2× UNFORCED-WITH-BOUNDARY) / FORCED.**

Admission rule (`GOALS.md`): a candidate enters only if (a) its principle is
statable without the measured angle, (b) it has a kill-test executable in ≤1
iteration, (c) it is not a rephrasing or an additional realization of an
existing entry. Realizations of `X = C/(X+C)` score zero — three exist
already (rank-one Feshbach; saddle of `½X² − C log(X+C)`; NJL rainbow) and a
fourth is drift, not progress.

The object every candidate must force (the unforced core of all three
realizations): the coefficient lock — same Casimir `C` as coupling numerator
and closed-channel gap with unit relative coefficient (`r = γ/α = 1`), map
normalization `A†A = C` with no level shift — plus the channel assignment
`γ:0, W:½, Z:1` as output (T1 standard, all five conditions).

## Entries

### (d) Gauge/Stueckelberg protection of the one-square lock — STRIKE 1 DONE: UNFORCED-WITH-BOUNDARY (2026-06-11); STRIKE 2 RUNNING (iteration 2)

Principle: 4D gauge invariance of the open vector channel (bare mass
forbidden; Q compensates δp Stueckelberg-fashion) + locality + single scale
forces `Γ_P(B) = B − μ⁴C/(B+μ²C)`.

Strike 1 (iteration 1, cross-confirmed, all algebra verified —
`notes/2026-06-11-iter1-gauge-lock-verdict.md`): UNFORCED, by pincer. Strict
(p,Q) content ⇒ Theorem A: every local invariant quadratic action gives
`Γ_P(B) = B·R(B)` (massless open channel) — the de Vries kernel is not
gauge-realizable there at all, and the sub-class "local invariant
gauge-field Lagrangian forces de Vries" is KILLED by derivation (the PSD
no-go re-derived inside the class). With the mandatory Goldstone π,
Stueckelberg invariance is toothless: five-parameter invariant deformation
family (r, m₀, s, η, Z₁) through the de Vries point. Side results:
resolvent NECESSITY (X+(C) irrational over R(C): no rational-in-C local
kernel matches identically; the gap shape is forced for identity-in-C
mechanisms); Lorentz-type dichotomy (kernel needs vector-Q exchange + scalar
compensator simultaneously; the 4D transcription is an ASSUMED embedding);
prior run's "conditional gauge pass" de-certified (was internal covariance,
not a 4D gauge pass).

Named boundary (the strike-2 target): **B1** induced-gap/no-CDD
`μ²H_QQ = H_QP·H_PQ` (spectral: residue R = μ²·ν₀ channel-universally;
closed-channel compositeness — Z=0-class for the CLOSED channel, distinct
from the open-channel (b′) kill); **B2** portal minimality (unsubtracted
Σ, single current vertex: s = η = 0); **B3** channel-universal kinetics
(ASSUMED — it is the same-radius/single-μ postulate, = (c3) below).
Gauge-Ward identities cannot substitute (transversality); the viable class
is spectral/current-algebra (KSRF II is the known approximate analogue).

Strike 2 (iteration 2, DONE 2026-06-11): UNFORCED-WITH-BOUNDARY again —
**(d) RETIRED** (`notes/2026-06-11-iter2-boundary-verdict.md`,
`calc/iter2_boundary_checks.py`). KSRF saturation SMUGGLES (KSRF I = Ward
theorem for every a; KSRF II ⇔ a = 2 = VMD, dynamical); no-CDD FAILS
(positive unsubtracted counterexample with intrinsic gap m₀ ≠ 0); bootstrap
FAILS (homogeneous closure, hs = (w−1)g²: every normalization is a fixed
point). Retired boundary, cleanest forms: g²/α = 1 ⇔ R = μ²ν₀ ⇔
**Σ_j(0) = μ² channel-universally** (static self-energy channel-blind;
Casimir only in the dispersion). No kinematic theorem ties residue to
position (CDD ambiguity). Signpost → candidate (h).

### (a) Map selection: current zero modes vs Sugawara — QUEUED (updated by iteration 3)

Iteration-3 finding (slot split): the geometric reduction does NOT select
the unshifted map — it puts the algebraic Casimir in the portal slot and
the spectral Laplacian (C − q² with flux; 4C on S³) in the gap slot, and
generates no 1/(k+2) shift. The geometric branch of (a) is therefore
answered negatively; what remains of (a) is only the WZW/boundary version
(level-2 zero-mode sector as boundary data), to be time-boxed as before.
Cross-corroboration (kkFable, 2026-06-12 import §3): a spin^c Dirac square
on their carrier gives C_G − C_K + |ρ|², not bare j(j+1) — their stated
reason for rejecting the bare-Casimir map as a production premise.

Principle: the boundary/zero-mode structure of the `SU(2)_2` current sector
selects the unshifted Casimir map (`A†A = C`, no `1/(k+2)`) over the `L0`
weighting as the physical mass operator. Kill-test: enumerate the consistent
boundary mass operators in the level-2 sector (`J₀·J₀` vs `L0` vs mixtures
under the boundary-state consistency conditions); if both normalizations are
equally admissible boundary data, the candidate selects channels but not the
operator → UNFORCED-WITH-BOUNDARY. Time-box: 1 iteration (it already consumed
dv2 iter-2/iter-3 and much of the milestone-1 chain).

### (b) Hubbard–Stratonovich origin of the saddle potential — KILLED BY INHERITANCE (2026-06-11)

Principle was: a defined HS construction generates
`V(X) = ½X² − C log(X+C)`. The pre-registered kill-test ("exhibit the
g-dependence") is answered by iteration 2 without a dedicated iteration:
any defined HS construction carries its four-fermion coupling G into the
saddle as `X = GC/(X+C)`-type — the iteration-1 family `X² + CX − r²C`
with `r² = G` (`calc/iter1_adversary_checks.py` check 4). "What fixes G"
is the retired (d)-boundary closure g²/α = 1. The Casimir-not-dimension
fingerprint stays useful (current-contracted loops give C, plain traces
give 2j+1) and is inherited by (h).

### (b′) Compositeness `Z = 0` condition — KILLED (at admission, 2026-06-11)

The single-pole rank-one resolvent has `Z⁻¹ = 1 + C/(X₊+C)² > 1` strictly;
`Z = 0` impossible (`calc/devries_core.py` §7). Revival as continuum/
multi-pole variant = new candidate, fresh admission, and it loses the
rational pole equation.

### (c) Orbit/Bohr–Sommerfeld quantization `β²γ = √C` — RUNNING (iteration 4; archival test SOLVED 2026-06-11)

Promoted 2026-06-12 after the iteration-3 kill: with symmetry, spectral
kinematics, and tree geometry all closed, the orbit reading — where j is a
mechanical label, not an internal-space quantum number (the iteration-3
deep flag) — is the most distinctive remaining lock candidate, and the
period condition (c2) is the lock in orbit clothes.

Principle: an internal relativistic orbit with speed β and quantized
angular momentum obeys `β²γ = √C` (the orbit form of the same quadratic;
equivalence verified in `calc/devries_core.py`). Admission passes (statable
without the angle).

Archival kill-test SOLVED from the corpus
(`corpus/clean/14-string-theory-and-orbits-….md`, lines 314–425): candidate
(c) IS the original 2005 de Vries construction. Its ingredient list, each
one currently unforced:
- (c1) de Broglie quantization of a relativistic circular orbit with the
  Landé–Pauli replacement, `L = γm₀βc·r = √(j(j+1))ħ`;
- (c2) period condition `T_r = h/(m₀c²)` (orbit period = Compton period),
  which eliminates the radius and yields `γβ² = √(j(j+1))`;
- (c3) same-radius matching across channels, `r_½ = r₁`, giving
  `M_j ∝ β_j` hence `X_j = β_j²` — the orbit avatar of the single-scale μ;
  each channel's orbit is built on its own pole mass (the self-consistency
  that makes this the gap equation in different clothes). Cross-link
  (iteration 1): (c3) is the orbit-language form of boundary condition B3
  (channel-universal kinetic normalization) in entry (d) — one assumption,
  two languages;
- (c4) channel set `{½, 1}` for the massive sector; the W↔½, Z↔1 assignment
  is then forced by mass ordering alone (reversal gives negative sin²) — so
  (c) reduces the assignment leg to "why channels {0, ½, 1}", same as (g).
The corpus already names the missing derivation: derive `r_½ = r₁` from
electroweak symmetry breaking rather than imposing it.

Physical kill-test (updated): a defined Lagrangian (string/flux-tube/
rotating-loop) must derive (c1)+(c2)+(c3) jointly — in particular the period
condition (c2), which is the orbit-language coefficient lock. Classify the
choices `{γβ = √C, γβ² = √C} × {L = j, √(j(j+1)), j+½}`; selecting by which
one hits the number is forbidden (no-scan discipline).

Originality consequence: any (c) result must credit the 2005 lore (de
Vries/Rivero; the corpus is the primary carrier); only a Lagrangian
derivation of (c1)–(c3) would be new.

### (h) Gauge-Higgs/higher-D kinetic-term normalization closure — KILLED at class level (iteration 3, 2026-06-12, cross-confirmed)

Verdict (`notes/2026-06-12-iter3-ghu-verdict.md`, `calc/iter3_checks.py`):
for every internal background the single-trace transverse kernel is
`K_T(B) = B + D†D` (Gram) ⇒ Γ_P(0) ≥ 0, Gram cone `γ²C ≤ s(αC+m₀²)`
(s = 0 ⇒ γ = 0), pure-YM sector a direct sum with no irreducible
resolvent. The coefficients ARE trace-locked and the locked point is the
Manton/Gram class (seagull mass linear in C; angle a rational
embedding-trace number) — forced to the wrong place. Map-slot split:
algebraic C in vertex, spectral Laplacian in gap (S² flux: C − q²; S³: 4C
but D = 11-excluded and background unstable at tree level). Escapes E1–E4
named, all outside the admission premise (E1 = loop dynamics = the retired
(d)-closure, fresh admission required). Corrigendum recorded: Manton SU(3)
row is sin² = 3/4 (1/4 is G₂/Fairlie).

### (h-archive) original admission text (2026-06-11)

Principle: the forced geometry's single trace-normalized kinetic term
`−(1/4g_D²)F_MN F^MN`, reduced on the internal SU(2) zero-mode sector,
fixes ALL relative coefficients of the 4D quadratic (p, Q, π) system —
there is no per-term freedom because there is one term. The question is
whether the forced point is the de Vries point. Admission: (a) statable
without the angle ✓; (b) kill-test in one iteration: compute the reduction,
read off the family coordinates `(r = γ/α, s, η, Z, m₀, map weight)` from
iterations 1–2, locate the point ✓; (c) not a rephrasing — (d) asked
whether symmetry/spectral principles force the closure (no); (h) asks
whether the single-trace geometry does (GHU supplies the Goldstone, so the
toothless branch applies and the coefficients are a computable landing
point, not a free family) ✓. Known prior data point the arms must
reproduce/locate in family coordinates: standard GHU on S² gives Goldstone
+ separate scalar, NO Schur block (codex Lim–Maru–Hasegawa calc, dv2) —
likely the γ = 0 or pure-Gram point. SCOPE: zero-mode quadratic level only;
no global compactification claims (D8/O8 stays closed); the known
horizontal-only failure (sin² = 0.2423) is a control. Partially subsumes
(a): the same reduction outputs the map weight (zero-mode vs Sugawara).
Inherits (b)'s Casimir-vs-dimension fingerprint as a control.

### (e) Composite / magnetic-dual W with duality-pinned coefficients — QUEUED (demoted)

Demoted to realization unless an exact duality statement (Seiberg-class)
pins `r = 1` and the map. Kill-test: name the duality frame and the exact
result, or drop. Obligatory literature pass: hidden local symmetry,
Abbott–Farhi, Suzuki-type composite weak bosons, Klebanov–Polyakov.

### (g) Global-form / line-operator selection of the channel set — QUEUED

Targets the assignment leg (T1 condition 3), today the weakest: the
`γ:0, W:½, Z:1` story rests on `½⊗½ = 0⊕1` + center parity (coherent, not
derived). Principle: the allowed global form of the gauge group and its line
operator lattice select `{0, ½, 1}` with the center rule. Kill-test:
rep-theoretic — exhibit whether any global form admits `j = 3/2` while
keeping the assignment; if yes, the finite set is a choice, not an output.
Carrier-level data point (kkFable import §4): on X_{1,1} the assignment is
obstructed in the SM-compatible reading (j = ½ slot colour-charged;
inverted assignment gives cos² > 1) and floats only on a colourless toy —
"0.2231 detaches from any observable" there.

### (i) Hessian/variational formulation (kkFable "Deliverable 4") — QUEUED (admitted 2026-06-12)

Principle: a first-order operator/superpotential structure D_patch whose
critical-point second variation is the signed Hessian
`A(D) = [[0, D†],[D, −c·D†D]]` with c = 1 forced by the functional's
structure. Imported from the sister run (kkFable C7/N5; see
`notes/2026-06-12-kkfable-cross-import.md` §2 — the two programs' open
cores coincide). As a Hessian the indefinite block is legitimate (saddle),
so this is a genuinely different class from retired (d) (variational
geometry/Morse, not Lagrangian symmetry). Kill-test (one iteration):
exhibit the functional class with c forced, or show the c-knob persists in
every class — in which case it is the same free closure retired in
iteration 2 and (i) dies by inheritance. Caution: the "vector-mass branch"
reading of the positive Hessian eigenvalue is itself underived.

## Exclusions (pre-T1 drift; re-enter only as T3 accounting data)

α ≈ 135.3 corpus item; Higgs/top/Z pole relations (Torrente-Lujan);
μ ≈ √(v·M_Z/2); the 96.54 GeV `j=3/2` diphoton discriminator (tower branch
only, post-T1).

## De-certified prior claims (per `GOALS.md`; do not cite)

1. "κ = 1 fixed by the canonical ½X² norm" (LOOP-LOG iter-1 verdict line) —
   convention, not a lock; knob re-opens as `r = γ/α`.
2. "(½,1) unique within 3σ (j ≤ 4)" as originally scored — superseded datum;
   re-scored 2026-06-11 (holds; see scorecard note) and filed as T3 material.

## Equivalence decision (charter alignment)

The charter's "orbit-loophole question for X+ = β²" is form-independent:
orbit, gap, and quadratic forms are one equation (`calc/devries_core.py`
§§2–4). The gap form is the live formulation; the orbit reading lives here
as candidate (c) only.
