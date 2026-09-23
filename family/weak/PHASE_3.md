# PHASE 3 — Algebraic origin of the spurion Delta

Status: completed in Phase 3 of 7.
Inputs read: `/home/codexssh/weak/SEED.md`, `/home/codexssh/weak/PHASE_1.md`,
`/home/codexssh/weak/PHASE_2.md`.
Scope: clarify the seed's "trace-preserving" language for the spurion Delta;
fix the required magnitude (and sign) of Delta; estimate Delta from five candidate
mechanisms (M1 soft-SUSY, M2 compositeness, M3 Seiberg dual / dim-6, M4 one-loop
top matching, M5 trace-anomaly / Higgs-quartic beta); identify which lands at the
right value with at most one TeV-scale auxiliary.

Inputs from previous phases (all GeV):
m_0 = 106.5702, v/sqrt(2) = 174.10, M_W = 80.369, M_Z = 91.1876,
m_top = 172.7, m_h_bare = 122.381, m_h_phys = 125.20 (PDG 2024 = 125.20 GeV).
Yukawa: y_t = sqrt(2) m_top / v_SM = 0.99196 with v_SM = sqrt(2) * v/sqrt(2) = 246.21 GeV.
SU(2) gauge: g_2 = 2 M_W / v_SM = 0.65284, alpha_W = g_2^2 / (4 pi) = 0.03392.

---

## 1. Sanity check on the term "trace-preserving spurion"

### 1.1 What the seed actually requires numerically

The seed identifies the doublet **negative** eigenvalue with m_h^2 (bare):
under Fit B (Phase 1), lambda_-(doublet) m_0^2 = -(sqrt(57)+3)/8 m_0^2 = -14977.08 GeV^2,
so m_h_bare^2 = |lambda_-| m_0^2 = 14977.08 GeV^2 and m_h_bare = 122.381 GeV.
The shift to the physical pole m_h_phys = 125.20 GeV requires

    Delta = m_h_phys^2 - m_h_bare^2 = 125.20^2 - 122.381^2 = +697.96 GeV^2     (3.1)

(equivalent to shifting the *eigenvalue* of M^2 by **-697.96 GeV^2**, i.e. the
tachyonic eigenvalue becomes more negative by 698 GeV^2). The seed's own
formula `f^2 = f_0^2 - Delta` with `f = v/sqrt(2)` is internally inconsistent
with the seed's own numerical claim of Delta ~ 700 GeV^2: identifying f with
v/sqrt(2) = 174.10 GeV and f_0 with 122.381 GeV gives Delta = -15333.7 GeV^2,
not +698 GeV^2. **We follow the task statement** (Delta shifts m_h, not v) and
take (3.1) as the target.

### 1.2 Does "trace-preserving" work algebraically?

A 2x2 symmetric M^2 has Tr = lambda_+ + lambda_-. A shift that **literally**
preserves Tr forces

    delta_lambda_+ + delta_lambda_- = 0    i.e.  delta_lambda_+ = -delta_lambda_-. (3.2)

Applied to our case (delta_lambda_- = -697.96 GeV^2):

    delta_lambda_+ = +697.96 GeV^2
    => M_W^2 shifts from 6459.18 -> 7157.13 GeV^2
    => M_W shifts from 80.369 -> 84.600 GeV.                                    (3.3)

This is a **+4.23 GeV shift in M_W**, ~325 sigma outside the PDG value
(80.369 +/- 0.013 GeV). Verified symbolically with sympy on both natural
Tr-preserving moves: (a) off-diagonal-only shift `M -> M + d * [[0,1],[1,0]]`
and (b) sigma_3-traceless `M -> M + D * [[1,0],[0,-1]]`. Both yield M_W = 84.6 GeV.
**Literal trace-preserving FAILS.**

A **det-preserving** shift would require delta_lambda_+ / lambda_+ +
delta_lambda_- / lambda_- = 0, i.e. delta_lambda_+ = -(lambda_+/lambda_-)
delta_lambda_- = -0.4313 * 697.96 = -301.0 GeV^2, shifting M_W^2 from 6459.18
to 6158.17, i.e. M_W = 78.47 GeV (off by ~1.9 GeV, 146 sigma). Also FAILS.

The **only** shift consistent with (i) m_h: 122.38 -> 125.20 and (ii) M_W
left at 80.369 to PDG precision is a **rank-1 spectator-preserving** spurion:
delta(M^2) = c * |v_-><v_-| where v_- is the unit eigenvector of the
tachyonic root. In the (a=b=1, doublet) gauge basis this rank-1 matrix is

                 [ 1/2 - sqrt(57)/38     -2*sqrt(19)/19 ]
    P_- =        [                                    ]
                 [ -2*sqrt(19)/19         1/2 + sqrt(57)/38 ]

(verified with sympy; Tr P_- = 1, det P_- = 0). Spurion is Delta * P_- with
Delta_eigenvalue = -697.96 GeV^2 (so |m_h^2| moves up by 698 GeV^2). This
spurion is **neither trace- nor det-preserving**: it shifts Tr M^2 by
+Delta_eigenvalue = -697.96 GeV^2 and det M^2 by lambda_+ * Delta_eigenvalue =
-4.51e6 GeV^4.

### 1.3 Verdict on the terminology

"Trace-preserving spurion" in the seed is a **misnomer**. The correct labels are:

- **Spectator-preserving** (preserves the M_W eigenvalue), or equivalently
- **Eigenstate-aligned rank-1**: the spurion is proportional to the projector
  on the tachyonic eigenvector and therefore affects exactly one eigenvalue.

If one instead wants a shift expressible diagonally in the (1,1)/(2,2) basis,
neither pure (1,1) nor pure (2,2) addition works:

- M -> M + diag(Delta, 0) needs Delta = -15673.8 GeV^2 to land m_h_phys, and
  forces M_W down to 40.4 GeV (catastrophic).
- M -> M + diag(0, Delta) needs Delta = -7156.6 GeV^2, forces M_W to 68.8 GeV.

Both verified with sympy. The seed's wording "trace-preserving" cannot be
made consistent with the stated numerics under any interpretation; the
physically operative spurion is rank-1 aligned along v_-.

---

## 2. Required Delta — fixed sign and convention

Throughout the rest of this phase we use:

    Delta := + (m_h_phys^2 - m_h_bare^2)
           = + 697.96 GeV^2     (positive)                                       (3.4)

with the convention "Delta is a positive shift of the **physical** Higgs mass-squared".
Equivalently, the eigenvalue of M^2 in the tachyonic slot shifts by -Delta:

    lambda_-(doublet) m_0^2:  -14977.08  ->  -15675.04 GeV^2.                    (3.5)

Targets for the five mechanism estimates: Delta in [620, 780] GeV^2 (i.e. the
seed range 700 +/- ~10%) — anything within an order of magnitude with a TeV-
scale single auxiliary is a candidate. Anything within a factor of 2 is a fit.

---

## 3. Five candidate mechanisms

For each: explicit prefactor, formula, value of one auxiliary scale Lambda_X
(if needed) to hit Delta = 698 GeV^2, and verdict.

### 3.1 M1 — soft SUSY breaking

Mechanism: a soft mass-squared term `+m_soft^2 * |h|^2` added directly to the
(2,2) tachyonic entry by SUSY breaking. Prefactor at tree level is **1**.

    Delta_M1 = m_soft^2          (prefactor 1, no loop)                          (3.6)

Target: m_soft = sqrt(698) = **26.4 GeV**.

Verdict: **fundamentally incompatible at tree level.** A 26 GeV scalar SUSY
mass is excluded by LEP (>100 GeV chargino bound, >~750 GeV gluino, >~1 TeV
squark from LHC). A typical TeV-scale SUSY breaking would yield m_soft^2 ~
10^6 GeV^2 -> Delta_M1 ~ 1500x too large.

Loop-suppressed variant (anomaly-mediated): m_soft^2 ~ (alpha_W/(4 pi))^2 *
Lambda_susy^2 with (alpha_W/(4 pi))^2 = 7.3e-6. Then Lambda_susy = sqrt(698 /
7.3e-6) = **9.8 TeV** (or ~340 TeV with alpha/(4 pi) replaced by 1/(16 pi^2)
of the soft-mass two-loop expression). Possible but contrived: requires a
specific mediation scheme tuned to deliver exactly 700 GeV^2 with no other
visible SUSY consequences.

**Verdict: MISSES at tree level by ~1500x; AMSB variant requires Lambda_susy ~
10 TeV plus an ad hoc choice of mediator. NOT preferred.**

### 3.2 M2 — compositeness threshold

Mechanism: in a composite-Higgs / pNGB picture, top loops at the confining
scale Lambda_c give a Coleman-Weinberg-like shift to m_h^2:

    Delta_M2 = (N_c y_t^2 / (16 pi^2)) * Lambda_c^2     (prefactor = 3 y_t^2 / (16 pi^2) = 0.01869)  (3.7)

Target: Lambda_c = sqrt(698 / 0.01869) = **193 GeV**.

Verdict: **misses by factor ~10** in TeV-range expectation. A natural composite-
Higgs scale is Lambda_c >~ 1 TeV (to evade EW precision and direct searches),
which would give Delta_M2 ~ 19000 GeV^2 — 27x too large. Forcing Lambda_c =
193 GeV puts the compositeness scale below the EW scale, ruled out. (The
formula is also dimensionally identical to the M4 quadratic-CW piece below,
modulo the cutoff convention.)

**Verdict: MISSES by ~27x at 1 TeV; the required Lambda_c = 193 GeV is
phenomenologically excluded.**

### 3.3 M3 — Seiberg-duality / dim-6 |H|^4 operator

Mechanism: an irrelevant operator c_6 (H^dag H)^3 / Lambda_d^2 = c_6 |H|^6 /
Lambda_d^2, generated at a dual scale Lambda_d, shifts m_h^2 by the second
derivative of the potential at the vev. With c_6 = O(1) and using v_sqrt2 =
174.10 GeV for the VEV:

    Delta_M3 ~ c_6 * v_sqrt2^4 / Lambda_d^2     (prefactor c_6 = O(1))           (3.8)

Target (c_6 = 1): Lambda_d = v_sqrt2^2 / sqrt(Delta) = 30310.81 / 26.42 =
**1.147 TeV**. For c_6 = 4 (a factor common in (H^dag H)^3 expansions),
Lambda_d = 2.295 TeV.

Verdict: **fits at Lambda_d ~ 1-2 TeV** with O(1) Wilson coefficient. This is
the most generic UV-physics statement: any new physics at ~1.5 TeV that
couples to the Higgs as a dim-6 operator generates a Delta of the right size.

**Verdict: FITS at Lambda_d ~ 1.1-2.3 TeV (c_6 in [1, 4]). VIABLE.**

(Note: the previous run's claim that Lambda_d ~ 2.3 TeV hits the target
corresponds to c_6 ~ 4, which is the natural overall normalization for the
(H^dag H)^3 operator coefficient with H = (h + v)/sqrt(2). Both 1.1 TeV and
2.3 TeV are in the same ballpark and depend on Wilson-coefficient convention.)

### 3.4 M4 — one-loop electroweak matching (top loop)

Mechanism: the bare Higgs mass-squared at the seed scale m_0 = 106.6 GeV is
matched to the physical pole by SM running. The top loop dominates. Two
sub-pieces:

(a) Quadratically-divergent CW piece (regulated by a hard cutoff at the seed
scale m_0):

    Delta_M4,quad = -(3 y_t^2 / (8 pi^2)) * (m_0^2 - m_top^2)
                  = -0.03739 * (11357.2 - 29825.3)
                  = +**690.46 GeV^2**                                            (3.9)

Prefactor: 3 y_t^2 / (8 pi^2) = **0.03739** (no auxiliary scale needed; Lambda_X
is fixed to m_0 by the seed itself). Ratio to target: **0.989** — within **1%**.

(b) Log piece (standard CW):

    Delta_M4,log = -(3 y_t^2 / (8 pi^2)) * m_top^2 * log(m_0^2 / m_top^2)
                 = -0.03739 * 29825.3 * (-0.96550)
                 = +**1076.6 GeV^2**                                             (3.10)

Ratio to target: 1.54x.

Sign: positive in both cases. The top loop drives the Higgs eigenvalue more
negative as one runs from UV (m_0) to IR (m_top), and m_0 < m_top makes the
log piece flip sign relative to the usual Lambda_UV >> m_top convention. In
eigenvalue language, lambda_-(m_top) - lambda_-(m_0) < 0 (more negative),
which in mass-squared language is +Delta. Consistent.

**Verdict: FITS REMARKABLY WELL with no auxiliary scale.** The quadratic-CW
piece at Lambda = m_0 hits the target to **1%**; the log piece hits within
1.54x. The seed scale m_0 = 106.57 GeV — which Phases 1-2 fixed by matching
the doublet lambda_+ to M_W — turns out to be exactly the cutoff that makes
the top loop give the right Delta. No new physics scale is required.

(There is one caveat: a quadratic-cutoff regulator is not strictly defined
in MS-bar; the result is regulator-dependent. The agreement to 1% is suspicious-
looking — it may be coincidence, or it may indicate that the model has an
implicit definition of m_0 as a physical cutoff. The log-piece ratio 1.54x is
more conservative and still passes the order-of-magnitude test.)

### 3.5 M5 — trace anomaly / Higgs-quartic beta function

Mechanism: a conformal-anomaly piece in the Higgs effective potential
proportional to beta_lambda, picking up a scale^2 factor. The dominant top
contribution to beta_lambda is

    beta_lambda_top = -6 y_t^4 / (16 pi^2) = -0.03679                            (3.11)

So with Lambda_X^2 the relevant scale:

    Delta_M5 = |beta_lambda| * Lambda_X^2     (prefactor 6 y_t^4 / (16 pi^2) = 0.0368)  (3.12)

Target: Lambda_X = sqrt(698 / 0.0368) = **138 GeV** (~v/sqrt(2)).

Verdict: with Lambda_X = m_top, Delta_M5 = 0.0368 * 29825 = **1097 GeV^2**
(1.57x); with Lambda_X = v_sqrt2, Delta_M5 = 1115 GeV^2 (1.60x). The natural
scale that delivers exactly 698 is Lambda_X ~ 138 GeV — essentially the EW
scale itself. The mechanism is numerically degenerate with M4 (both use the
top loop), but the parametrics are slightly different: M4 uses y_t^2 m_top^2,
M5 uses y_t^4 Lambda^2.

**Verdict: WITHIN ~1.6x with Lambda_X at the EW scale (no new physics needed);
overlaps with M4. VIABLE but harder to disentangle from M4.**

---

## 4. Summary table

| Mech | Prefactor                   | Formula                                          | Lambda_X needed     | Delta(Lambda_X = TeV) | Verdict                          |
|------|-----------------------------|--------------------------------------------------|---------------------|-----------------------|----------------------------------|
| M1   | 1 (tree)                    | m_soft^2                                         | 26 GeV (excl.)      | 10^6 GeV^2 (~1500x)   | excluded; AMSB tunable to ~10 TeV |
| M2   | 3 y_t^2/(16 pi^2) = 0.019   | (3 y_t^2/(16 pi^2)) Lambda_c^2                   | 193 GeV (excl.)     | 18700 GeV^2 (~27x)    | misses by ~27x                   |
| M3   | c_6 = O(1)                  | c_6 v_sqrt2^4 / Lambda_d^2                       | **1.1-2.3 TeV**     | 1473 (~2.1x at 1 TeV) | **FITS** at Lambda_d ~ 1.5 TeV   |
| M4   | 3 y_t^2/(8 pi^2) = 0.037    | (3 y_t^2/(8 pi^2)) [Lambda^2-m_top^2 (quad) or m_top^2 log(Lambda^2/m_top^2) (log)] | none (Lambda = m_0) | quad: 690 (0.99x); log: 1077 (1.54x) | **FITS** with no aux. scale       |
| M5   | 6 y_t^4/(16 pi^2) = 0.037   | (6 y_t^4/(16 pi^2)) Lambda_X^2                   | 138 GeV (~EW scale) | log piece at m_top: 1097 (1.57x) | within 1.6x; overlaps M4         |

Required Delta = +697.96 GeV^2 (with M_W = 80.369 input).

---

## 5. Conclusion — which mechanism is viable

**Two mechanisms land within an order of magnitude with at most one TeV-scale
auxiliary:**

1. **M4 (one-loop top matching, quadratic-CW piece at cutoff = m_0)** is the
   most economical: it produces Delta = 690.5 GeV^2 (1.1% above target) with
   **no new auxiliary scale at all** — the cutoff Lambda is fixed to the
   seed's own m_0 = 106.57 GeV. The fit is to 1%; the log piece is 1.54x off.
   The catch is regulator-dependence of the quadratic piece, so the agreement
   may be a numerical coincidence or it may indicate that the seed's m_0 is
   physically the matching scale.

2. **M3 (dim-6 |H|^4 operator at Lambda_d ~ 1-2 TeV)** is the most generic:
   any UV physics that couples to the Higgs via (H^dag H)^3 at a TeV-scale
   produces a Delta of the right order with c_6 = O(1). For c_6 = 1, Lambda_d
   = 1.15 TeV; for c_6 = 4 (a natural normalization), Lambda_d = 2.30 TeV.
   This is a top-down ("there's new physics at ~1.5 TeV") explanation, in
   contrast to M4's bottom-up ("the SM running between m_0 and m_top does it
   for free").

M5 is numerically as good as M4 to within 1.6x but is not independent of M4
(both are top-loop driven and arguably the same physics counted twice in
different language). M1 and M2 miss by 27x to 1500x at their natural scales
and require contortions to fit.

**Recommendation for downstream phases.** The seed should drop the term
"trace-preserving" entirely; it is a misnomer (Section 1). The physically
operative spurion is rank-1 aligned with the tachyonic eigenvector. Of the
five mechanisms, **M4 is preferred on grounds of economy** (no new scale,
1% agreement) — but with the caveat that its quadratic piece is regulator-
dependent. **M3 is preferred if a clean dimensional-analysis / Wilsonian
interpretation is wanted**, with Lambda_d ~ 1.5 TeV as a concrete prediction
of new physics. Phases 4-7 may want both interpretations on the table:

- If the model is fundamental in the seesaw sense, m_0 is the UV cutoff and
  M4 explains Delta automatically (Phase 6 fermion sector then needs to be
  compatible with the running between m_0 and m_top).
- If the model is effective field theory with a UV completion above 1 TeV,
  M3 says the completion sits at Lambda_d ~ 1-2 TeV and is *the* phenomenologically
  testable consequence of this picture (collider searches, dim-6 fits).

These two options are not mutually exclusive — M4 (calculable IR running) and
M3 (uncalculable UV matching) can both contribute, with M4 dominating in the
seed-scale matching and M3 setting the size of the residual UV-sensitive piece.

---

## 6. Open issues handed to downstream phases

- **Phase 4 (more spurion sectors)**: the same rank-1 projector logic should
  be applied to the triplet sector. The triplet lambda_- = -2.732 m_0^2 ->
  176.15 GeV (Fit B) is close to m_top = 172.7 GeV; a similar small spurion
  could land this at exactly m_top.
- **Phase 5 (fermion masses)**: the choice between M3 and M4 is constrained
  by whether m_top is an input to the Higgs sector (M4 view) or both come
  from a common UV at ~1-2 TeV (M3 view).
- **Phase 7 (sBootstrap / SO(32) connection)**: the rank-1 spectator-preserving
  spurion may have a natural meaning as an SO(32) singlet emerging at the
  bottom of an SO(32) -> SU(2) decomposition; this is not pursued here.
