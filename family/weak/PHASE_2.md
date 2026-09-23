# PHASE 2 — Representation selection rule for {R_1, R_2} = {2, 3}

Status: completed in Phase 2 of 7.
Inputs read: `/home/codexssh/weak/SEED.md`, `/home/codexssh/weak/PHASE_1.md`.
Scope: evaluate five named selection rules; enumerate all 10 pairs of SU(2) irreps
with C2 < 12; test each against the Fit-B target set
{M_W = 80.369, M_Z = 91.188, m_h_bare = 122.4, v/sqrt(2) = 174.10} GeV using
m_0 = 106.5702 GeV from Phase 1; identify near-misses; conclude.

Conventions for this phase: (a,b) = (1,1) as fixed in Phase 1; eigenvalues of the
2x2 seed `[[0, t],[t, -t^2]]` are `lambda_± = (-C2 ± sqrt(C2^2 + 4 C2))/2` in
m_0^2 units. SU(2) irrep of dimension n has C2 = (n^2 - 1)/4.

---

## 1. The five named selection rules

For each rule we report which pair it selects, then list (C2_1, C2_2) and the
four eigenvalues in m_0^2 units AND in GeV (using m_0 = 106.5702 GeV from
Phase 1, Fit B).

### Rule (A) — two lowest non-trivial irreducible representations of SU(2)

Non-trivial means n >= 2. The two lowest are n = 2 and n = 3. **Selects {2, 3}.**

- (C2_1, C2_2) = (3/4, 2), (t_1, t_2) = (sqrt(3)/2, sqrt(2)).
- Eigenvalues (m_0^2 units):
  - doublet: lambda_+ = (sqrt(57) - 3)/8 = +0.568729; lambda_- = -(sqrt(57)+3)/8 = -1.318729.
  - triplet: lambda_+ = sqrt(3) - 1 = +0.732051; lambda_- = -(sqrt(3)+1) = -2.732051.
- Masses (GeV) with m_0 = 106.5702: {80.369, |i| 122.381, 91.181, |i| 176.149}.
- **Verdict.** Numerically consistent with all four Fit-B targets (M_W, m_h_bare,
  M_Z to 0.1%; the leftover triplet lambda_- = 176.15 GeV is the unidentified
  Phase-1 observation near m_top). Rule (A) is a clean, parameter-free,
  group-theoretic rule that uniquely picks {2,3}; it is logically the strongest
  of the five at selecting the pair. **PASSES.**

### Rule (B) — doublet and adjoint forced phenomenologically by Higgs and W content

The SM Higgs is an SU(2)_W doublet (n=2); the SU(2)_W gauge bosons live in the
adjoint (n=3). **Selects {2, 3}** by hand-input phenomenology.

- (C2_1, C2_2) = (3/4, 2), eigenvalues and masses identical to Rule (A).
- **Verdict.** Numerically identical to (A). It "works" trivially because it
  *defines* the answer by the data we are trying to predict. **PASSES, but
  circular** — it uses the SM matter content as input rather than deriving the
  pair from first principles.

### Rule (C) — minimize |C2(R_1) + C2(R_2) - k| for some integer k

Compute C2_1 + C2_2 for the 10 admissible pairs:

| pair  | C2 sum | nearest integer | distance |
|-------|-------:|----------------:|---------:|
| (2,3) | 2.75   | 3               | 0.25     |
| (2,4) | 4.50   | 4 or 5          | 0.50     |
| (2,5) | 6.75   | 7               | 0.25     |
| (2,6) | 9.50   | 9 or 10         | 0.50     |
| (3,4) | 5.75   | 6               | 0.25     |
| (3,5) | 8.00   | 8               | 0.00     |
| (3,6) | 10.75  | 11              | 0.25     |
| (4,5) | 9.75   | 10              | 0.25     |
| (4,6) | 12.50  | 12 or 13        | 0.50     |
| (5,6) | 14.75  | 15              | 0.25     |

For **k = 3**, the unique minimizer is **(2,3)** with distance 0.25 (next: (2,4)
at 1.5). However, the rule is parametric in k:
- k = 6: unique minimizer is (3,4) at 0.25.
- k = 8: unique minimizer is (3,5) at 0.00 (a perfect hit).
- k = 12: unique minimizer is (4,6) at 0.50.

So Rule (C) picks {2,3} only if one independently postulates k = 3. The rule is
**ambiguous without a justification for k**, and there is no obvious group
theory reason for k = 3 (it is not the dimension of the adjoint, nor the
Dynkin index of any pair, nor the number of generators). **Verdict: only
"passes" via the ad-hoc choice k = 3.** Predicted eigenvalue spectrum is then
identical to (A).

### Rule (D) — SU(2)_L x SU(2)_R / Z_2 custodial decomposition of the Higgs sector

The Higgs bidoublet (2,2) under SU(2)_L x SU(2)_R decomposes under the diagonal
custodial SU(2)_V as (2 x 2) = 1 + 3: a **singlet plus triplet**.
**Selects {1, 3}** (the strict reading of the rule).

- (C2_1, C2_2) = (0, 2), (t_1, t_2) = (0, sqrt(2)).
- Eigenvalues for R = 1 (singlet, C2 = 0): both = 0 (trivially degenerate).
- Eigenvalues for R = 3 (triplet, C2 = 2): +0.732051, -2.732051, giving
  +91.181 GeV and |i| 176.149 GeV.
- **Verdict.** Predicts only **two** nonzero eigenvalues (the singlet sector is
  identically massless in this skeleton because C2 = 0 forces both diagonal
  entries to vanish and the off-diagonal t = sqrt(C2) = 0 as well). No
  prediction for M_W (80.4) and no prediction for m_h_bare (122.4). **FAILS.**

(An alternative loose reading — "the Higgs is a doublet and the W^a is a
triplet, hence {2, 3}" — is just rule (B) relabelled.)

### Rule (E) — two lowest KK modes of a 5D SU(2) gauge theory truncated to two modes

In a 5D SU(2) gauge theory compactified on an interval, the gauge boson is
adjoint-valued at every KK level; the zero mode and the first KK mode both
transform as **n = 3** under the 4D SU(2). **Selects {3, 3}** (same rep, two
KK copies).

- (C2_1, C2_2) = (2, 2), eigenvalues degenerate between the two copies.
- The four eigenvalues collapse to two distinct values: +0.732051 and -2.732051
  in m_0^2 units, giving +91.181 GeV and |i| 176.149 GeV, each with
  multiplicity two.
- **Verdict.** Cannot produce four distinct mass scales; in particular it
  produces no doublet eigenvalue near M_W = 80.369 GeV and no scalar eigenvalue
  near m_h_bare = 122.4 GeV. **FAILS.**

---

## 2. Full 10-pair enumeration table

SU(2) irreps of dimension n in {2,3,4,5,6} have C2(n) = (n^2-1)/4 in
{3/4, 2, 15/4, 6, 35/4} — all < 12. There are C(5,2) = 10 unordered pairs.

For each pair, the four eigenvalues are {lambda_+(R_1), lambda_-(R_1),
lambda_+(R_2), lambda_-(R_2)} in m_0^2 units, with lambda_± = (-C2 ± sqrt(C2^2 +
4 C2))/2. Masses in GeV use m_0 = 106.5702 GeV; for lambda < 0 we list the
magnitude (the eigenvalue is the squared mass and is negative — interpreted as
the bare Higgs / tachyonic slot in the seesaw).

| pair  | (C2_1, C2_2)    | (t_1, t_2)            | R_1 eigvals (m_0^2 units)        | R_2 eigvals (m_0^2 units)         | R_1 masses (GeV)            | R_2 masses (GeV)              |
|-------|-----------------|-----------------------|----------------------------------|-----------------------------------|-----------------------------|-------------------------------|
| (2,3) | (0.7500, 2.0000)| (0.8660, 1.4142)      | (+0.56873, -1.31873)             | (+0.73205, -2.73205)              | +80.369, |i| 122.381        | +91.181, |i| 176.149          |
| (2,4) | (0.7500, 3.7500)| (0.8660, 1.9365)      | (+0.56873, -1.31873)             | (+0.82048, -4.57048)              | +80.369, |i| 122.381        | +96.532, |i| 227.833          |
| (2,5) | (0.7500, 6.0000)| (0.8660, 2.4495)      | (+0.56873, -1.31873)             | (+0.87298, -6.87298)              | +80.369, |i| 122.381        | +99.572, |i| 279.388          |
| (2,6) | (0.7500, 8.7500)| (0.8660, 2.9580)      | (+0.56873, -1.31873)             | (+0.90616, -9.65616)              | +80.369, |i| 122.381        | +101.447, |i| 331.160         |
| (3,4) | (2.0000, 3.7500)| (1.4142, 1.9365)      | (+0.73205, -2.73205)             | (+0.82048, -4.57048)              | +91.181, |i| 176.149        | +96.532, |i| 227.833          |
| (3,5) | (2.0000, 6.0000)| (1.4142, 2.4495)      | (+0.73205, -2.73205)             | (+0.87298, -6.87298)              | +91.181, |i| 176.149        | +99.572, |i| 279.388          |
| (3,6) | (2.0000, 8.7500)| (1.4142, 2.9580)      | (+0.73205, -2.73205)             | (+0.90616, -9.65616)              | +91.181, |i| 176.149        | +101.447, |i| 331.160         |
| (4,5) | (3.7500, 6.0000)| (1.9365, 2.4495)      | (+0.82048, -4.57048)             | (+0.87298, -6.87298)              | +96.532, |i| 227.833        | +99.572, |i| 279.388          |
| (4,6) | (3.7500, 8.7500)| (1.9365, 2.9580)      | (+0.82048, -4.57048)             | (+0.90616, -9.65616)              | +96.532, |i| 227.833        | +101.447, |i| 331.160         |
| (5,6) | (6.0000, 8.7500)| (2.4495, 2.9580)      | (+0.87298, -6.87298)             | (+0.90616, -9.65616)              | +99.572, |i| 279.388        | +101.447, |i| 331.160         |

**Inputs vs. outputs.** With m_0 = 106.5702 GeV fixed by **anchoring R = 2's
lambda_+ to M_W^2** (Fit B), M_W is by construction an **input** for any pair
containing R = 2. M_Z and m_h_bare are then **outputs**. v/sqrt(2) = 174.10 GeV
is the downstream interpretation of |lambda_-(doublet)|^(1/2) once the Phase 1
identification f^2 = |doublet lambda_-| m_0^2 is adopted — i.e. for any pair
containing R = 2, the m_h_bare slot doubles as the v/sqrt(2) slot. We also
anchor each non-{2,...} pair separately (fit m_0 so that some eigenvalue equals
M_W) to give the pair its fairest chance.

**Best assignment per pair**, fitting M_W (anchor) and then asking M_Z and
m_h_bare each to be matched by *any* remaining eigenvalue, maximum fractional
error:

| pair  | anchor    | m_0 (GeV) | M_Z prediction (GeV) | m_h_bare prediction (GeV) | max frac err |
|-------|-----------|-----------|----------------------|---------------------------|--------------|
| (2,3) | R2_+ -> M_W | 106.570 | R3_+ -> 91.181 (0.01%)    | R2_- -> 122.381 (0.02%)        | **0.02 %**       |
| (2,4) | R2_+ -> M_W | 106.570 | R4_+ -> 96.532 (5.86%)    | R2_- -> 122.381 (0.02%)        | 5.86 %       |
| (2,5) | R2_+ -> M_W | 106.570 | R5_+ -> 99.572 (9.19%)    | R2_- -> 122.381 (0.02%)        | 9.19 %       |
| (2,6) | R2_+ -> M_W | 106.570 | R6_+ -> 101.447 (11.25%)  | R2_- -> 122.381 (0.02%)        | 11.25 %      |
| (3,4) | R4_+ -> M_W | 88.727  | R3_+ -> 75.910 (16.75%)   | R3_- -> 146.660 (19.82%)       | 19.82 %      |
| (3,5) | R5_+ -> M_W | 86.017  | R3_+ -> 73.604 (19.29%)   | R3_- -> 142.180 (16.16%)       | 19.29 %      |
| (3,6) | R6_+ -> M_W | 84.428  | R3_+ -> 72.241 (20.78%)   | R3_- -> 139.547 (13.93%)       | 20.78 %      |
| (4,5) | R5_+ -> M_W | 86.017  | R4_+ -> 77.910 (14.56%)   | R4_- -> 183.886 (50.24%)       | 50.24 %      |
| (4,6) | R6_+ -> M_W | 84.428  | R4_+ -> 76.479 (16.13%)   | R4_- -> 180.502 (47.46%)       | 47.46 %      |
| (5,6) | R6_+ -> M_W | 84.428  | R5_+ -> 78.880 (13.50%)   | R5_- -> 221.339 (80.83%)       | 80.83 %      |

**Only (2,3) is consistent within 5 %.** Next-best pair (2,4) misses M_Z by
5.9 %; all pairs without R = 2 miss the m_h_bare slot by >= 14 % and (typically)
overshoot wildly because the negative eigenvalue of higher reps grows ~ -C2.

---

## 3. Three near-miss pairs

1. **(2, 4) — quartet replacement of the triplet.** Doublet anchors M_W = 80.369
   and m_h_bare = 122.38 exactly; **fails** because the quartet's upper
   eigenvalue gives +96.53 GeV for M_Z (5.9 % high), driven by C2(4) = 15/4
   exceeding C2(3) = 2 and inflating the positive eigenvalue.

2. **(3, 4) — triplet plus quartet, no doublet.** Anchoring quartet lambda_+ to
   M_W; **fails** because without n = 2 there is no eigenvalue near the Higgs
   slot (best is triplet lambda_- = 146.66 GeV, 19.8 % off m_h_bare = 122.4)
   and M_Z is undershot by 16.8 % since both reps have C2 too large for the
   refitted m_0 = 88.7 GeV.

3. **(2, 5) — doublet plus quintet (next "higher-spin" choice).** Doublet again
   nails M_W and m_h_bare; **fails** because C2(5) = 6 pushes the quintet's
   positive eigenvalue to +99.57 GeV (9.2 % above M_Z = 91.19), and there is no
   integer k for which Rule (C) selects (2,5) uniquely without independently
   selecting (3,5) or (2,7).

(Worth noting: a fourth near-miss class is (3,3) from Rule E with two KK copies
of the adjoint — it lands at 91.18 GeV and 176.15 GeV but produces no doublet
slot at all; it fails for the same reason as Rule D.)

---

## 4. Conclusion — which rule selects {2, 3}

- **Rule (A)** — "two lowest non-trivial irreps of SU(2)" — **uniquely picks {2,3}**
  with zero free parameters and no phenomenological input. Among the five
  candidate rules this is the *only* one that is simultaneously (i)
  group-theoretic, (ii) parameter-free, and (iii) consistent with the data.
- **Rule (B)** picks {2,3} but is **circular**: it inputs SM matter content as
  its definition.
- **Rule (C)** picks {2,3} only for **k = 3**, which itself requires an
  external justification this skeleton does not supply.
- **Rule (D)** picks {1,3} under the strict custodial decomposition reading,
  which **fails** numerically (singlet sector is identically massless).
- **Rule (E)** picks {3,3} (degenerate KK pair), which **fails** numerically
  (only two distinct eigenvalues; no doublet slot).

Across the 10 admissible pairs, **{2,3} is also the unique numerical winner**:
its max fractional error against {M_W, M_Z, m_h_bare} is 0.02 %; the next pair
((2,4)) is at 5.86 %, a factor ~300 worse. The numerical dominance of {2,3} is
driven by two independent facts:

1. The doublet (n = 2) is the only irrep whose *negative* eigenvalue, in
   units of M_W, lands near m_h_bare = 122.4 GeV. Concretely,
   sqrt(|lambda_-/lambda_+|)(doublet) = sqrt(1.31873/0.56873) = 1.523, and
   1.523 * 80.369 = 122.4 GeV. No other irrep gives this ratio: n = 3 gives
   sqrt(2.73205/0.73205) = 1.932 -> 155.3 GeV; n = 4 gives 2.36 -> 189.7 GeV; etc.

2. Once R_1 = 2 is forced by the Higgs slot, the positive eigenvalue of the
   *other* rep, in units of M_W, must land on M_Z / M_W = 1.1346. Solving
   sqrt(lambda_+(R)/lambda_+(2)) = 1.1346 gives lambda_+(R) =
   1.1346^2 * 0.56873 = 0.7320, which is exactly lambda_+(R = 3) = sqrt(3) - 1.
   No other integer-dimensional SU(2) irrep does this.

**Bottom line.** Rule (A) is the unique a priori rule among the five that
uniquely picks {2,3}; Rule (B) is the unique phenomenological one. Rules (C),
(D), (E) either need an extra parameter (C), pick a different pair that fails
the data (D, E), or both. Independently, **{2,3} is the unique numerical winner
in the 10-pair enumeration by a factor of ~300 in max fractional error**, so
even without a selection rule the data themselves uniquely select {2,3} to the
prescribed 5 % accuracy.

What this does *not* settle: whether Rule (A) is "physical" in the sense of
following from a deeper structure (e.g. the lowest two highest-weight reps of
a Bost-Connes-style truncation, or the first two layers of the sBootstrap
representation tower hinted at in the seed), or whether it is merely a
post-hoc ordering. That is a Phase 7 question.
