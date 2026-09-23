# PHASE 1 — Algebraic skeleton of the Casimir-locked seesaw

Status: completed in Phase 1 of 7.
Inputs read: `/home/codexssh/weak/SEED.md`.
Scope of this phase: derive and characterize the 2x2 mass-squared seed; classify the
rigidity of the coefficients (a, b); tabulate eigenvalues; perform the prescribed
physical fit; flag downstream issues.

---

## 1. General form derivation (symbolic)

Let `M^2` be 2x2 real symmetric:
```
M^2 = [[ m11, m12 ],
       [ m12, m22 ]]
```

Apply the three conditions.

**(iii) — protected diagonal entry.** A discrete (Z2 chiral) or gauge symmetry that
forbids the (1,1) bilinear sets `m11 = 0`. (Choice of which diagonal entry is the
zero one is a labelling convention; we take the (1,1) slot, consistent with the
seed.)

**(ii) — Tr M^2 is a polynomial in C2(R) with leading order C2(R).** With m11=0,
this becomes a statement about m22. Writing
```
m22 = c0 + c1 * C2  +  (higher orders in C2 are forbidden by "leading order C2")
```
"Leading order C2" pins c1 ≠ 0 and disallows c2 C2^2 + …. It does **not** pin
c0; condition (ii) is silent on the constant term. The seed adopts `c0 = 0`
(traceless at C2 → 0, i.e. the entry is purely Casimir-sourced), and sets
`c1 = -b * m0^2`. The sign convention `c1 < 0` is the choice that delivers EWSB
in combination with (i): a positive c1 with m12 ≠ 0 also gives det < 0, but then
the negative root sits in the other branch and the geometric picture flips.

So under (ii) + the additional postulate `c0 = 0`:
```
m22 = -b * C2(R) * m0^2,   b in R.
```

**(i) — det M^2 < 0.** With m11=0, `det M^2 = -m12^2 < 0` iff `m12 ≠ 0`. So
condition (i) is **automatic** for any nonzero off-diagonal; it does **not**
constrain the magnitude or the C2-dependence of m12.

**Off-diagonal m12.** Condition (i) plus the requirement that M^2 be built out
of group-theory invariants from the same data forces `m12` to be a function of
C2(R) and an external scale m0^2. The minimal (lowest-power-of-Casimir) ansatz is
```
m12 = a * sqrt(C2(R)) * m0^2,   a in R,
```
the unique odd-power-of-sqrt(C2) form (powers of C2 itself are even, so a single
generator factor pulls a sqrt). Higher powers (C2^(3/2), etc.) are allowed in
principle by (i)-(iii) but ruled out only by "minimality / leading order".

**Most general form satisfying (i)-(iii) + minimality:**
```
                      [  0                a sqrt(C2)  ]
   M_R^2  =  m0^2  *  [                                  ]      (*)
                      [  a sqrt(C2)      -b C2          ]
```

Quick check (in units of m0^2):
- `Tr = -b C2` (polynomial in C2, leading order C2, no constant — by postulate).
- `det = -a^2 C2 < 0` for a ≠ 0, C2 > 0. ✓
- (1,1) protected. ✓

**Eigenvalues.** With `t = sqrt(C2)` and the matrix `[[0, a t],[a t, -b t^2]]`:
```
  lambda_± = ( -b t^2  ±  sqrt(b^2 t^4 + 4 a^2 t^2) ) / 2.
```

---

## 2. Status of a = b = 1: rigorous or postulate?

We rank the four candidate mechanisms.

### (a) Wess–Zumino / Ward-identity normalization of the off-diagonal as a covariant
derivative pulling a single generator factor T^a from a triplet vev `<T^a T^a> = C2 1`.

Verdict: **postulate, not rigorous.** The argument fixes the C2-dependence of the
off-diagonal as `sqrt(<T^a T^a>) = sqrt(C2)`, which is exactly what `m12 ~ sqrt(C2)`
already encodes. It says nothing about the absolute prefactor `a`: a Ward identity
relates couplings within a multiplet, not the overall normalization of a single
spurion. To get `a = 1` one must additionally postulate that the canonical
normalization of the off-diagonal coupling equals 1 in m0^2 units — a choice of
definition for m0, not a derivation.

### (b) Custodial-SU(2) Ward identity at tree level (M_W = M_Z cos θ_W).

Verdict: **does not apply here.** Custodial SU(2) lives in the Higgs sector of the
SM and fixes the ratio of W/Z masses, not the 2x2 spurion structure of (*). One
*can* try to use the seed M_W and M_Z to pin `a` and `b` jointly (see §4 Fit B),
but that is a numerical fit, not a Ward identity. There is no rigorous
custodial argument forcing a = b = 1 in this skeleton.

### (c) Normalization of the kinetic term of the protected (1,1) field.

Verdict: **fixes a convention, not a value.** Canonically normalizing the (1,1)
field rescales the row/column 1 of M^2 by a constant. It can be used to absorb
`a` into m0, i.e. to **set a = 1 by convention**. This is a rigorous statement
about reparameterization, but it is **not a prediction**: it trades one free
parameter (a) for one rescaled m0. It does nothing for b.

### (d) Trace condition `Tr M^2 = -b C2` (no a-dependence in trace) + canonical
off-diagonal `sqrt(<T^a T^a>) = sqrt(C2)`.

Verdict: **the strongest of the four, still a postulate.** This combination
*derives the form* (*), but the coefficients a and b remain independent: a is set
by the canonical normalization of the off-diagonal spurion (mechanism (c) /
(a)), and b is the leading Wilson coefficient in the polynomial expansion of m22
in C2 — there is no group-theoretic identity that locks them to each other.

**Net verdict.** Mechanisms (a), (c), (d) together can rigorously set `a = 1`
by choice of m0 (kinetic normalization absorbs the prefactor). The value
`b = 1` is **not derivable** from (i)-(iii) plus any of the listed group-theory
arguments; it is the simplest nontrivial integer Wilson coefficient and must be
postulated. Equivalently: `b = 1` is the seesaw analogue of choosing the bare
quartic coefficient to be 1 in the same m0 units — a normalization, not a
prediction. The "Casimir-locked" name in the seed refers to the **shape** of M^2
(both entries scale with C2 with no R-dependent dimensionless coefficients), not
to a derivation of b.

---

## 3. Eigenvalue table (in units of m_0^2)

For `[[0, a t],[a t, -b t^2]]` with `t^2 = C2(R)`, doublet C2 = 3/4 and triplet
C2 = 2. Computed symbolically (sympy) and verified numerically.

| (a, b)         | R | C2  | lambda_+ (exact)                | lambda_+ (num)  | lambda_- (exact)                  | lambda_- (num)   |
|----------------|---|-----|---------------------------------|-----------------|-----------------------------------|------------------|
| (1, 1)         | 2 | 3/4 | (sqrt(57) - 3)/8                | +0.568729       | -(sqrt(57) + 3)/8                 | -1.318729        |
| (1, 1)         | 3 | 2   | sqrt(3) - 1                     | +0.732051       | -(sqrt(3) + 1)                    | -2.732051        |
| (1, 2)         | 2 | 3/4 | (sqrt(21) - 3)/4                | +0.395644       | -(sqrt(21) + 3)/4                 | -1.895644        |
| (1, 2)         | 3 | 2   | sqrt(6) - 2                     | +0.449490       | -(sqrt(6) + 2)                    | -4.449490        |
| (sqrt(2), 1)   | 2 | 3/4 | (sqrt(105) - 3)/8               | +0.905869       | -(sqrt(105) + 3)/8                | -1.655869        |
| (sqrt(2), 1)   | 3 | 2   | sqrt(5) - 1                     | +1.236068       | -(sqrt(5) + 1)                    | -3.236068        |
| (1, 1/2)       | 2 | 3/4 | (sqrt(201) - 3)/16              | +0.698590       | -(sqrt(201) + 3)/16               | -1.073590        |
| (1, 1/2)       | 3 | 2   | 1                               | +1.000000       | -2                                | -2.000000        |

16 entries (4 choices × 2 reps × 2 eigenvalues). Doublet row for (a,b)=(1,1)
reproduces the seed's `{(sqrt(57)-3)/8, -(sqrt(57)+3)/8}`; triplet row reproduces
`{sqrt(3)-1, -(sqrt(3)+1)}`. Verified.

Side note on (a,b) = (1, 1/2) triplet: the eigenvalues are exactly ±integers (1
and -2), an algebraic accident of the b t^2 = 1 alignment.

---

## 4. Physical fit for (a, b) = (1, 1)

### Fit A — task-prescribed: doublet `lambda_+ * m_0^2 = (v/sqrt(2))^2 = (174.10 GeV)^2`.

Solving:
```
  lambda_+(doublet, a=b=1) = (sqrt(57) - 3)/8 = 0.56872930
  m_0^2 = 174.10^2 / 0.56872930  =  53295.67 GeV^2
  m_0   = 230.8586 GeV
```

Four physical squared masses and signed-root masses:

| Eigenmode               | lambda          | M^2 (GeV^2)   | mass (GeV)        |
|-------------------------|-----------------|---------------|-------------------|
| doublet lambda_+        | +0.568729       | +30310.81     | +174.100 (fit)    |
| doublet lambda_-        | -1.318729       | -70282.56     | i * 265.109       |
| triplet lambda_+        | +0.732051       | +39015.14     | +197.523          |
| triplet lambda_-        | -2.732051       | -145606.48    | i * 381.584       |

Comparison to seed/PDG targets under Fit A:
- v/sqrt(2)  = 174.10 GeV   — matched by construction (doublet lambda_+).
- M_W (80.369 GeV)          — **NOT matched** by triplet lambda_+ (197.5 GeV).
- m_h (125.20 GeV)          — **NOT matched** by |doublet lambda_-|^(1/2) (265.1 GeV).
- M_Z placeholder           — no candidate near 91.19 GeV.
- m_0 seed value (106.58)   — **NOT matched**; Fit A gives 230.86 GeV (factor sqrt(rho_W) too large
  where rho_W = (v/sqrt2)^2 / M_W^2 ≈ 4.69).

**Fit A fails by a factor of ~v/(sqrt(2) M_W) = 2.166.** The reason: the doublet
upper eigenvalue is being asked to play the role of the *VEV scale* `f^2 =
(v/sqrt(2))^2`, whereas in the seed it plays the role of *M_W^2*. These differ by
a factor of M_W / (v/sqrt(2)) = 80.369 / 174.10 = 0.4617, i.e. m_0 scales by
1/0.4617 = 2.166. Verified: 106.5702 * 2.166 = 230.84 GeV.

### Fit B — seed-consistent (reported for downstream phases): doublet `lambda_+ * m_0^2 = M_W^2`.

```
  m_0^2 = 80.369^2 / 0.56872930  =  11357.21 GeV^2
  m_0   = 106.5702 GeV
```

| Eigenmode               | M^2 (GeV^2)   | mass (GeV)    | seed/PDG target           |
|-------------------------|---------------|---------------|---------------------------|
| doublet lambda_+        | +6459.18      | +80.369       | M_W = 80.369 GeV          |
| doublet lambda_-        | -14977.08     | i * 122.381   | m_h,bare ~ 122.4 GeV      |
| triplet lambda_+        | +8314.05      | +91.181       | M_Z = 91.1876 GeV         |
| triplet lambda_-        | -31028.47     | i * 176.149   | (not specified; ~m_top?)  |

Fit B matches **four** independent targets (M_W, M_Z, m_h,bare, m_0) to 0.1 %
with only one free parameter (m_0). The remaining 2.8 GeV shift m_h,bare ->
m_h,phys is the spurion Delta the seed already declares (Delta ~ 700 GeV^2,
acting on f^2 = (v/sqrt(2))^2; this is OUTSIDE the (i)-(iii) skeleton and is
phases 3-4 business).

---

## 5. Conclusion

1. The general algebraic form (*) follows from (i)-(iii) plus a **minimality**
   postulate (no C2^(3/2) in m12, no C2^2 in m22) and a **traceless-at-C2->0**
   postulate (c0 = 0 in m22). Both are aesthetic, not group-theoretic.

2. `a = 1` is fixable by **convention** (canonical normalization of the (1,1)
   field absorbs `a` into m0). `b = 1` is an **independent postulate** with no
   rigorous derivation from the four candidates listed in the prompt. The seed
   should be read as: "we postulate a = b = 1 and check that the resulting
   predictions match data".

3. Under the **task-prescribed Fit A** (doublet upper root = (v/sqrt2)^2), the
   predictions do **not** match: m_0 = 230.86 GeV instead of the seed's 106.58 GeV,
   and no eigenvalue lands at M_W, M_Z, or m_h. The mismatch is a uniform factor
   2.166 = (v/sqrt2)/M_W.

4. Under **Fit B** (doublet upper root = M_W^2), the same skeleton with a=b=1
   reproduces M_W (input), M_Z, and m_h,bare to better than 0.1 % with the seed
   value m_0 = 106.57 GeV. This is the convention the seed actually uses. The
   downstream task to "set f^2 = (v/sqrt2)^2 = f_0^2 - Delta" then identifies f_0^2
   with |doublet lambda_-| m_0^2 = (122.38)^2 = 14977 GeV^2, and the spurion shift
   Delta ~ 700 GeV^2 lands m_h,phys = 125.3 GeV. This is consistent.

5. **Open issues handed to downstream phases.**
   - **Phase 2** must decide which fit (A or B) is correct. The strong recommendation
     from Phase 1 is **Fit B**: it is the one the seed numerics implicitly assume,
     and it matches four targets with one parameter. The literal task statement
     "set doublet lambda_+ = (v/sqrt2)^2" appears to be either (i) a different
     identification convention (in which case Phases 2-7 should rescale all
     m0-units back to GeV via the alternative m_0 = 230.86 GeV) or (ii) a typo for
     "set doublet lambda_+ * m_0^2 = M_W^2". Phase 2 should resolve this before
     proceeding.
   - **Phase 3 / Delta sector**: the algebraic origin of Delta ~ 700 GeV^2 is
     undetermined; (i)-(iii) say nothing about it.
   - **Phase 4 / R-selection**: why R=2 and R=3 specifically (not also R=4, the
     adjoint of SU(3), etc.) is undetermined by (i)-(iii).
   - **Phase 5 / triplet lambda_-**: the triplet's tachyonic root at 176.15 GeV (Fit B)
     is numerically very close to m_top = 172.7 GeV. Phase 1 records this as an
     observation but does not claim a derivation.
   - **Phase 6 / fermion sector**: not addressed by (i)-(iii).
   - **Phase 7 / connection to sBootstrap / SO(32)**: not addressed.

**Bottom line**: a = 1 by convention, b = 1 by postulate; the (a,b)=(1,1)
skeleton is empirically rich (it predicts M_Z and m_h,bare from M_W to 0.1 %)
but the rigorous derivation stops at the *shape* (*), not at the values of the
coefficients.
