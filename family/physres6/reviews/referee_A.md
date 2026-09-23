# Referee A report — "Electroweak couplings fixed by Kaluza–Klein moduli"

Manuscript: `manuscript/main.tex`. Supporting: `context/claims_ledger.md`,
`calculations/kk_fixing_concept.md`, `calculations/alpha_derivation_attempt.md`.

Recommendation: **major revision before publishable.** The algebra is correct and
reproduces the quoted numbers, but the prose repeatedly upgrades *assigned* and
*coincidence*-level statements to the rhetorical status of *derivations*, and
contains one outright physical inconsistency (the 96.5 GeV state) that must be
fixed. The mechanism, as written, does not "fix" the couplings — it *relates* two
of them given two undischarged assignments.

---

## Central claim

The two dimensionless electroweak couplings (`sin²θ`, `α`) are not free SM inputs
but are fixed by the geometry of electroweak symmetry breaking, because the order
parameter that breaks the electroweak symmetry **is** the field that stabilizes
the Kaluza–Klein modulus `R`. Witten's result (coupling ~ `(M_pR)^{-p}`, but `R`
a free modulus) leaves a coupling geometric-yet-undetermined; the claim is that
tachyon condensation of the lower branch of `Q(J)=μ²[[0,√J],[√J,−J]]`
(`J=s(s+1)`) pins `R` and therefore the couplings. Chirality forces `D=10`
(interior point between an unbroken `D=11` endpoint, which Witten's no-go forbids,
and a broken `D=9` endpoint). The numbers (`sin²θ=0.2231`, `1/α=135.3`, the
one-scale spectrum, the 96.5 GeV state) are offered as evidence only.

I reproduced every quoted number independently (eigenvalues, `sin²θ=0.223101`,
`g²=0.41634`, `1/α=135.29`, `μ=106.578` GeV, the table percentages, `M₊(15/4)=
96.54`). The arithmetic is sound. The problems are physical and rhetorical.

---

## Strongest source-supported result

The mixing-angle ratio, **Eq. (eq:sin2)**:
`sin²θ = 1 − x₊(3/4)/x₊(2) = 0.223101`, agreeing with the **on-shell** value
`1 − M_W²/M_Z² = 0.223213` to 0.05%. This is the paper's best result because:

- It is genuinely parameter-free: a ratio within a single branch, scale `μ`
  cancels, no second assignment needed beyond the `(J_W,J_Z)=(3/4,2)` assignment.
- The matched quantity is correctly identified as the **pole-mass / on-shell**
  angle, and is correctly stated to be *distinct* from the effective (0.23155)
  and MSbar (0.23129) definitions. This distinction is handled honestly in the
  prose and matches ledger rows #4, #6.

Even here, note the result is "agreement with one specific scheme," not a
prediction of "the" weak mixing angle; the manuscript states this correctly and
should keep doing so.

---

## Weakest inference

The `D=10`-from-chirality argument (section "Chirality forces ten dimensions")
plus the claim that `α` is "an infrared quantity." Both are presented with the
grammar of derivation ("forces," "is a consequence of the picture, not an
adjustment") while resting on undischarged steps.

1. **`D=10` argument is hand-waved, not sound as written.** The chain is:
   `SU(3)×SU(2)×U(1)` needs 7 internal dims (`D=11`); Witten forbids chiral
   fermions there; full breaking to `SU(3)×U(1)_em` needs 5 internal dims
   (`D=9`); therefore the physical (partially broken) system sits at the
   "midpoint" 6 internal dims = `D=10`. Three gaps:
   - The dimension counts "7 → 5 → therefore 6 in between" treat the number of
     internal dimensions as a *continuous interpolation parameter* that the order
     parameter slides along. No such interpolation is constructed; spacetime
     dimension is not a vacuum-expectation-value continuum. The "midpoint" is
     asserted, not shown. (The supporting note `kk_fixing_concept.md` calls this
     "physres5 O10" but provides no construction either.)
   - Witten's no-go forbids chiral fermions in the `D=11` *unbroken* coset
     compactification. The Letter asserts the obstruction "does not apply at the
     `D=10` interior" — true that `D=10` string compactifications have chiral
     fermions, but that is a *different theory* (superstring), not the analytic
     continuation of the `D=11` SUGRA setup. Invoking "`D=10` is the critical
     dimension of the superstring, where chiral fermions are standard" silently
     swaps frameworks mid-argument.
   - The minimal internal-dimension count to realize `SU(3)×SU(2)×U(1)` as an
     isometry group is itself the (Witten) 7; nothing forces the broken endpoint
     to be exactly 5 internal dims rather than fewer — `U(1)_em` needs 1, `SU(3)`
     needs ≥4, so 5 is a *lower bound*, not "the" endpoint. The arithmetic that
     produces "6" depends on these being exact.
   This is the section most likely to draw a desk-reject from a string/SUGRA
   referee. It should be demoted to a conjecture/motivation, not a "force."

2. **"`α` is infrared / matches `α(~1 GeV)`" is not robustly defensible.** The
   construction value is `1/α = 135.29`. PDG endpoints are `1/α(0)=137.036` and
   `1/α(M_Z)=127.955`. My back-of-envelope running (lepton loops + a typical
   `Δα_had(1 GeV) ≈ 0.003–0.004`) gives `1/α(1 GeV) ≈ 134.8–135.3`, so 135.3 is
   *roughly* in the GeV region — but the scale that reproduces 135.3 is fixed by
   the hadronic vacuum-polarization contribution, whose value/uncertainty at low
   `q²` is exactly the part that is least well controlled (the data-driven vs
   lattice `Δα_had` tension; the same hadronic VP that drives the `(g−2)_μ`
   dispute). Quoting a sharp "near the hadronic (~1 GeV) scale" hides this: the
   matching is to a *band* of scales, and the precise scale that lands on 135.3
   is sensitive to a quantity carrying ~percent-level (and currently disputed)
   uncertainty. The ledger (#15) flags this as a **coincidence** with a
   "hadronic-VP caveat"; the prose presents it as a **consequence** of the
   picture ("not an adjustment"). That is overclaiming relative to the ledger.

---

## Hidden assumptions (not flagged with sufficient prominence in the prose)

- **H1 — Two undischarged assignments carry the whole result.** `sin²θ` rests on
  assignment A1 `(J_W,J_Z)=(3/4,2)` (ledger #8, tag **A**, "not derived").
  `α` additionally rests on A2 `v=√2·M₋(2)` ⟺ `g²=x₊(3/4)·x₊(2)` (ledger #9, tag
  **A**, "not derived"; `alpha_derivation_attempt.md` confirms PARTIAL,
  "still an assumption"). The abstract and Eqs. (eq:sin2)–(eq:alpha) read as if
  the couplings are *derived*; in fact they are *computed from two assigned
  cross-slot relations*. The manuscript does concede the assignments in the
  Discussion's penultimate paragraph, but the abstract's "fixes `α` as a pure
  number" and "The parameter-free numerical agreement is the evidence" do not
  carry that caveat.

- **H2 — `Q(J)` is not derived from any internal manifold.** By the authors' own
  `kk_fixing_concept.md`: the `√J` off-diagonal is "grounded" (Hodge exact-form
  eigenvalue), the `0` gauge entry is "natural," but the tachyonic `−J` entry is
  "open — needs a specific 6-manifold." So the operator that is the spine of the
  paper is two-thirds motivated, one-third assumed. The Letter states this in the
  Discussion ("the tachyonic entry `−J` requires the internal curvature to
  supply…"), which is good — but the abstract's "A breaking operator at each
  internal level realizes this" presents `Q(J)` as established.

- **H3 — `J=s(s+1)` Laplacian eigenvalue is used at half-integer `s` (s=1/2 →
  J=3/4; s=3/2 → J=15/4).** A Laplacian/Casimir eigenvalue `l(l+1)` on a compact
  manifold is normally integer-`l` (scalar harmonics). Using `s=1/2, 3/2`
  presupposes the modes live in *spinor/representation* labels, not scalar
  harmonic labels. This is internally consistent with reading `s` as a sector
  index (see (b) below) but is never justified as a Laplacian spectrum — it is
  assumed.

- **H4 — `v = √2·M₋(2)` reads the `J=2` negative branch as the top-Yukawa scale
  with `y_t ≈ 1`.** This `y_t≈1` is an extra input (ledger #10, tag **A/R**)
  smuggled into the chain that "fixes" `α`. It should be named where Eq.
  (eq:alpha) is introduced, not left in the ledger.

- **H5 — One-scale spectrum agreements are post-hoc identifications.** Table
  `tab:spectrum` labels `x₋(3/4)→h?` and `x₋(2)→t?` with question marks, agreeing
  at −2.2% and +2.1%. These are coincidence-level (ledger #18, #19, tag **C**)
  and the assignment of *which* negative-branch slot is the Higgs vs the top is
  chosen to match, not predicted. The question marks are honest; the surrounding
  sentence ("returns scalar and fermion scales near the Higgs and top and the
  vacuum, each within a percent—from one input") reads as a clean prediction.

---

## (a) The 96.5 GeV state: a genuine inconsistency — MUST fix

**This is a physical contradiction, not a labeling nuance.** Lines 126–129:

> "the next level `s=3/2` places a state at `M₊=μ√x₊(15/4)=96.5 GeV`, near the
> diphoton excess around `95.4 GeV` … this is not a gauge boson; in ten
> dimensions a chiral state of exotic charge is available, for which the level
> label is a representation index."

The ~95.4 GeV CMS/ATLAS feature is a **diphoton (`X→γγ`) invariant-mass excess**:
the resonance is a *neutral, colour-singlet* object (it decays to two photons; by
the Landau–Yang theorem it is also spin-0 or spin-2, not spin-1). A **chiral
state of exotic (e.g. charge-4/3, ledger #23/#31) charge** is electrically
charged and (per the supporting notes) coloured. **A charged, coloured state
cannot *be* a `γγ` resonance.** It cannot be pair-produced and appear as a single
narrow `γγ` bump at 96.5 GeV; it is not neutral; charge-4/3 colour states are
strongly constrained / would not present as a low-mass diphoton peak.

So the manuscript asserts the *same* `s=3/2` state is simultaneously (i) the
neutral diphoton excess and (ii) a charged exotic-chirality state. These are
mutually exclusive identities. The numerical coincidence (`96.5` vs `95.4`, ~1%)
is fine to *report*, but the *interpretation* is self-contradictory.

**Fix (choose one, do not assert both):**

- **Option 1 (recommended, most honest):** Report only the numerical proximity:
  "the next level places a *neutral scalar* slot at 96.5 GeV, ~1% from the
  reported 95.4 GeV diphoton excess; if this excess is confirmed, this slot is a
  candidate." Drop the "chiral state of exotic charge" entirely from this
  sentence. A diphoton resonance needs a *neutral, spin-0/2* assignment — and the
  authors' own framework already has neutral negative-branch (order-parameter /
  scalar) slots that are the natural diphoton candidates.
- **Option 2:** Keep the exotic-charge chiral state as a *separate* prediction
  (some other signature, e.g. pair-produced coloured exotics), and **sever it
  from the diphoton excess**. Then the 96.5 GeV number is no longer "near the
  diphoton excess" in any meaningful sense unless a neutral slot also lands there.

Either way, the current sentence must be rewritten so that one object is not given
two incompatible charge/spin identities. As written this is the single most
serious correctness error in the Letter.

---

## (b) The label `s` in `J=s(s+1)`: three distinct things — check it is not silently equated

The flag is correct and the manuscript is **partly, but not fully, clean.**

`s` is invoked in three roles across the paper and the program:

1. **Sector / representation index** — `s=1/2` ↔ doublet `J=3/4`, `s=1` ↔ adjoint
   `J=2` (lines 94–95). Here `s` labels which gauge/internal block.
2. **Physical Lorentz spin** — the diphoton excess, by Landau–Yang, must be a
   spin-0 or spin-2 *Lorentz* state.
3. **Regge oscillator level** — the Discussion's trajectory
   `M²_{n,j,±}=μ²x_{j,±}+n/α'` with `J=n+j` (lines 161–163, ledger #25) uses `n`
   (oscillator) and `j` separately.

Findings:

- The Letter mostly keeps (1) and (3) separate: it writes `J=n+j` and puts the
  present states at `n=0`, so the level label `j` is not equated to the Regge
  oscillator number `n`. Good.
- **However, lines 94–95 write `J=3/4 (s=1/2)` and `J=2 (s=1)` with no statement
  that `s` here is a sector index and NOT spin.** A reader will naturally read
  "`s=1/2`" as "spin-1/2" and "`s=1`" as "spin-1" — and the latter is even
  *suggestively correct* for `W`/`Z` (spin-1 gauge bosons sit in the `s=1`
  block), which makes the conflation almost invisible and therefore dangerous.
  But then `s=1/2`→`J=3/4` is *also* assigned to the (spin-1) charged gauge
  bosons `W`, so `s` there is clearly *not* spin. The two assignments are mutually
  inconsistent if `s` is read as Lorentz spin. The manuscript never says this.
- **Line 129** finally says "the level label is a representation index" — but only
  for the `s=3/2` state, and only after the inconsistent (a) sentence. The same
  clarification is needed at first use (lines 94–95).
- The half-integer `s` (H3 above) reinforces the spin confusion: `s=1/2, 3/2`
  *look* like fermion spins.

**Fix:** At first use (lines 71–73 and 93–95) add an explicit sentence:
"Here `s` labels the internal representation/sector setting the Laplacian
eigenvalue `J=s(s+1)`; it is neither the four-dimensional Lorentz spin of the
state nor the Regge oscillator level `n`, which are independent." Then `s=1` for
the `Z` block must not be allowed to read as "the `Z` has spin 1 because `s=1`"
(coincidental and misleading). This is cheap to fix and currently genuinely
ambiguous.

---

## On the on-shell vs effective weak-angle distinction

**Stated correctly.** Lines 118–120 identify the matched quantity as the on-shell
`1−M_W²/M_Z²=0.22320` (pole masses) and explicitly distinguish it from the
effective (0.23155) and MSbar (0.23129) definitions, citing MartinRobertson2025.
This matches ledger #4/#6 and is the right way to state it. **No change needed**,
except: the construction predicts the *tree-level/on-shell mass ratio*, so the
text should avoid implying it predicts "the weak mixing angle" full stop. One word
("the on-shell mass-ratio angle") at the abstract level would prevent
overreading. Minor.

---

## Exact revisions needed (concrete)

1. **Abstract, lines 33–35.** "its lower branch is the order parameter, fixing
   `α` as a pure number, `1/α=135.3`, in the infrared. The parameter-free
   numerical agreement is the evidence." — `α` is *not* fixed without assignment
   A2 (`v=√2·M₋(2)`, `y_t≈1`). Revise to: "…fixing `α` as a pure number once a
   cross-level identification (stated below) is assumed." Remove "parameter-free"
   when describing `α` specifically, or state plainly that `α` is parameter-free
   *given two assignments*. (Maps to ledger #9, #12, tag A.)

2. **Lines 58–69 ("Chirality forces ten dimensions"), and `kk_fixing_concept.md`
   §"Why D=10".** Demote "forces" to "motivates/suggests." Add one sentence
   acknowledging that (i) spacetime dimension is not literally a vacuum
   continuum being interpolated, (ii) `D=9`/5-internal is a lower bound not a
   forced endpoint, and (iii) the `D=10` chiral-fermion statement borrows the
   *superstring* framework, distinct from the `D=11` SUGRA setup whose no-go is
   cited. As written it is the section most exposed to desk rejection.

3. **Lines 126–129 (the 96.5 GeV state).** Resolve the (a) inconsistency: do not
   call the same state both the neutral `γγ` excess and a charged exotic-chirality
   state. Recommended rewrite (Option 1): assign the diphoton candidate to a
   *neutral* slot (Landau–Yang ⇒ spin 0 or 2), and either drop the exotic-charge
   sentence or move it to a separate, non-diphoton prediction. (Ledger #22 is
   tag C; ledger #23 is tag A — the prose must not present #23 as the explanation
   of #22.)

4. **Lines 71–73 and 93–95.** Add the `s`-is-a-sector-index disclaimer (see (b)).
   Explicitly state `s` ≠ Lorentz spin ≠ Regge level `n`. Without it, `s=1`↔`Z`
   reads as a spin claim.

5. **Lines 110–115 (`α` in the infrared).** Soften "near the hadronic
   (~1 GeV) scale" and "not an adjustment." State that the matching is to a *range*
   of low scales and that the precise scale reproducing 135.3 depends on the
   hadronic vacuum-polarization contribution, which carries the relevant (and
   currently disputed) uncertainty. The ledger (#15) already tags this **C** with
   a hadronic-VP caveat; the prose must not exceed the ledger. Quantitatively:
   `Δα_had` at low `q²` is the controlling, least-certain input, so a sharp scale
   claim is not defensible.

6. **Eq. (eq:alpha) / lines 101–109 and Table caption.** State at point of use
   that this rests on assignment A2 (`v=√2·M₋(2)` ⟺ `g²=x₊(3/4)x₊(2)`) and the
   reading `y_t≈1` (ledger #9, #10). Currently these only appear in the
   Discussion's penultimate paragraph and in the ledger. Move the caveat to the
   equation.

7. **Table `tab:spectrum`, lines 141–142 and surrounding sentence (122–124).**
   The "h?" and "t?" question marks are honest; the sentence "returns scalar and
   fermion scales near the Higgs and top and the vacuum, each within a percent"
   should add "with the slot-to-particle identification chosen post hoc" or
   similar, since the negative-branch slot assignment is not predicted (ledger
   #18–#20, tag C). Also note the agreements are −2.2%, +2.1%, +1.2% — "within a
   percent" is inaccurate for two of the three; change to "within a few percent."

8. **Abstract line 32 / line 91 ("One operator then does both jobs").** `Q(J)` is
   not derived: the `−J` entry is open (authors' own `kk_fixing_concept.md`). The
   Discussion (lines 155–160) concedes this — the abstract should not present the
   operator as established. Add "we posit" or equivalent.

### Summary of prose-vs-ledger mismatches (the core "honest labeling" failure)

- Ledger #9 = **A** (assigned), prose presents `α` as fixed/derived → fix #1, #6.
- Ledger #15 = **C** with VP caveat, prose presents IR placement as
  "consequence, not adjustment" → fix #5.
- Ledger #23 = **A** (open identity), prose uses it to *explain* #22 and
  contradicts the neutral nature of the excess → fix #3.
- Ledger #18–#20 = **C**, prose reads as clean predictions "within a percent"
  → fix #7.

The derived rows (#1–#3, #7, #11, #12, #16, #17, #21, #24) are correctly stated
and I reproduced all of them numerically.
