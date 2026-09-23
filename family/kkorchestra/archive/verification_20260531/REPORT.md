# Consolidated verification report — CP^2 / Aloff–Wallach KK carrier (claims C1–C7)

Date: 2026-05-31. Synthesis over subtasks T1–T6 and their independent verifiers.
Carrier under test: SO(3) -> X_{1,1}=SU(3)/U(1)_{1,1}=(SU(3)xSO(3))/U(2)_Delta -> CP^2.

## Verdict table

| Claim | Status | Deciding computation / citation |
|-------|--------|---------------------------------|
| **C1** CP^2/conj = S^4 (Kuiper-Massey); branch locus RP^2; SO(3)- not SU(3)-equivariant | **confirmed** | Massey 1973 / Kuiper 1974 / Hillman arXiv:1705.05038 (Established); U(1)_{1,1}=i*diag(1,1,-2)=lambda_8 forced as commutant of su(2)_L [calc/wb_1.py] |
| **C2** X_{k,l} fibres over CP^2 with fibre S^3/Z_{\|k+l\|}; X_{1,1}: dim 7, fibre SO(3)=RP^3 | **confirmed** | calc/wb_T1.py: \|H^4(X_{k,l})\|=\|k^2+kl+l^2\|=\|(k+l)^2-kl\| (Gysin det, identity proven in sympy), =Z/3 at (1,1); Escher-Ziller BundleTop.pdf Prop 4.3 |
| **C3** X_{1,1} fibre SO(3); Wilking (SU(3)xSO(3))/U(2)_Delta; dim 7 | **confirmed** | calc/wb_2c.py: invariant metrics 10->2->1 (Schur), m_0=su(2)_L fibre (vertical), Einstein at t=+1 (3-Sasakian) & t=-3/5 (squashed); Wilking Proc. AMS 127 (1999) **1191-1194** (page corrected from "3111") |
| **C4** CP^2 non-spin/spin^c; X_{1,1} BGM 3-Sasakian; SO(3)->Sp(1) obstruction = hypercharge | **confirmed** (T6 sub-claim corrected) | calc/wb_T1.py: w_2(TCP^2)=H!=0, **w_2(TX_{1,1})=0 (X_{1,1} SPIN)**; repair L=O(odd), minimal O(1), canonical K^{-1}=O(3); Escher-Ziller Prop 4.3 + BG98 hep-th/9810250 **Cor 1.2.7** "every 3-Sasakian manifold is spin" |
| **C5** Weinberg angle = ratio of Killing inertias, non-arbitrary (no free radius modulus) | **confirmed** (load-bearing) + **semisimple caveat** | calc/wb_3a_exact.py: invariant-form space on su(3) EXACTLY 1-dim => I(X)=(1/8)tr_m(Q)\|X\|^2, sin^2 theta_W metric-independent; sin^2=1/4 (lepton 3-plet); k_Y=3 (NOT SU(5) 5/3); SM running => M_c~3.7 TeV (calc/wb_3d/e.py). Caveat: g_cust^2/g_EW^2=1/(1+t) FREE (SU(3)xSO(3) semisimple) |
| **C6** Anchors: Witten 1981, CDF, Weinberg 1983 | **confirmed** (CDF characterization corrected) | Witten 1981 NPB186,412 + Witten 1983 Shelter Island (odd-dim no-go) confirmed; **CDF doi 10.1016/0550-3213(84)90265-7 = "SU(3)xSU(2)xU(1) from D=11 SUGRA", uses M^{p,q,r}=U(1) bundle over CP^2xS^2, NOT product CP^2xS^3 with SU(3)xSO(4)**; no_prior_instance=TRUE; chirality no-go ACTIVE, spin^c does not evade (DNP25 arXiv:2502.07710 PDF) |
| **C7** "De Vries condition" / signed Dirac-block Hessian A(D)=[[0,D†],[D,−D†D]], j(j+1) | **algebra confirmed / geometric derivation open** (was blocked) | archive/verification_20260531/T5.md: definition found in docs/ (quoting user files). **c=1**, char poly λ²+Jλ−J=0, sin²θ_W=(19+3√3−√57−3√19)/16=**0.2231013223** verified in sympy (≈ PDG on-shell). Placement vs spin^c spectral triple = INDEPENDENT; c=1 (and D†D=j(j+1)) are EXTRA POSTULATES, not derived from X_{1,1} geometry |

## Narrative

### What was confirmed
The differential-topological and group-theoretic backbone of the proposal is sound and now
fully grounded in computation plus primary sources:

- **C1-C3 (geometry/topology).** X_{1,1}=SU(3)/U(1)_{1,1} is a 7-manifold, an SO(3)=RP^3
  principal bundle over CP^2, and via Wilking is the normal homogeneous (SU(3)xSO(3))/U(2)_Delta
  with a genuine second SO(3) isometry factor acting transitively on the fibre. The integral
  cohomology ring (H^*=Z,0,Z,0,Z/3,Z,0,Z, u^2 generating H^4=Z/3) and the order law
  |H^4(X_{k,l})|=|k^2+kl+l^2| were DERIVED (Gysin determinant, sympy identity), not assumed.
  The invariant-metric moduli collapse 10->2->1 (Schur, two inequivalent U(2)-irreps m_0, m_3),
  matching Wilking's 1-parameter g_t, with exactly two Einstein metrics (3-Sasakian t=+1 and
  squashed t=-3/5, canonical 1/5 squash factor).

- **C4 (spin/spin^c).** CP^2 is non-spin (w_2=H!=0); the TOTAL space X_{1,1} is SPIN (w_2=0),
  consistent with Boyer-Galicki-Mann ("every 3-Sasakian manifold is spin"). The spin
  obstruction therefore lives on the base CP^2 and is repaired by an ODD line bundle L=O(k)
  (minimal O(1); canonical spin^c determinant K^{-1}=O(3)), identified with odd quanta of the
  lambda_8 hypercharge U(1). Kreck-Stolz invariants s_1=1/112, s_2=35/36 (=-1/36), s_3=1/18,
  p_1=0 mod 3.

- **C5 (Weinberg angle, the central physics claim).** The proposal's load-bearing assertion --
  that sin^2 theta_W is fixed by group theory, not a free radius modulus -- is CORRECT and was
  upgraded from Monte-Carlo to an EXACT Schur proof: the space of SU(3)-invariant symmetric
  forms on su(3) is one-dimensional (adjoint irreducible), so I(X)=(1/8)tr_m(Q)|X|^2 and the
  coupling ratio is metric-independent. Tree sin^2 theta_W=1/4 (lepton 3-plet embedding,
  rep-independent), with hypercharge normalization k_Y=3 (explicitly NOT the SU(5) value 5/3).
  SM 1-/2-loop running takes 1/4 -> the measured 0.231 with a compactification scale M_c~3.7-3.85
  TeV.

- **C6 (precedence + chirality).** The literature anchors are real: Witten 1981 (7 = min dim)
  and Witten 1983 (odd-dimension chirality no-go). No prior model bases a KK/coset electroweak
  construction on CP^2 as the sole base with custodial symmetry from a fibre. The Witten
  odd-dimension chirality no-go is ACTIVE for X_{1,1} and is NOT evaded by the spin^c twist
  (the two obstructions -- base w_2 vs. odd-dim charge-conjugate pairing -- are logically
  independent).

### What was corrected
- **CDF characterization (C6, CLAIMS.md).** The cited Castellani-D'Auria-Fre paper
  (doi 10.1016/0550-3213(84)90265-7) is "SU(3)xSU(2)xU(1) from D=11 supergravity" and uses the
  M^{p,q,r} family = U(1) bundle over CP^2xS^2 with isometry SU(3)xSU(2)xU(1) (SU(3)xSU(2) at
  M^{1,1,1}). It does NOT use the product CP^2xS^3, and SU(3)xSO(4) never appears. CLAIMS.md C6's
  "(CP^2xS^3 with SU(3)xSO(4))" parenthetical is inaccurate. The product CP^2xS^3 (isometry
  SU(3)xSO(4)) is a distinct Einstein 7-manifold not studied as an 11D SUGRA vacuum. The anchor
  still supports "7 is the minimal/natural dimension for SU(3)xSU(2)xU(1)," just via a different
  internal manifold than CLAIMS.md states.

- **w_2(X_{1,1}) sign (T6 sec. c).** T6's intermediate text said X_{1,1} is spin^c-but-not-spin
  with w_2!=0; this is wrong -- X_{1,1} is SPIN (w_2=0) by BGM/BG98 Cor 1.2.7, with the w_2
  obstruction belonging to the base CP^2 (this is exactly the C4-spin Established line and T1's
  result). The Witten no-go verdict is unchanged by the correction (odd-dimensionality, not
  spin-vs-spin^c, is the operative obstruction).

- **Wilking citation page (C3, T6).** Proc. AMS 127 (1999) **1191-1194** (DOI
  10.1090/S0002-9939-99-04613-4), not "3111".

- **Minor supporting-script defects (non-load-bearing).** T2's wb_2b.py has a buggy Ricci
  closed-form, superseded by the validated wb_2c.py (final answer correct). T4's wb_T4d.py has a
  left/right quaternion labeling error in the illustrative complex-structure-rotation demo (the
  so(4)=6 > u(2)=4 obstruction conclusion is convention-independent and survives). T1 sec.(c)(ii)
  used the wrong mechanism phrasing ("TCP^2 x L spin") for the spin^c repair; the correct
  determinant-line condition gives the identical arithmetic (k odd) and the stated answer is
  correct.

### What remains open
- **C3-physics / C5 caveat (custodial identification).** The Wilking SO(3)_R has the correct
  custodial SU(2)_R algebra and breaking pattern (right-quaternion (2_L,2_R) bidoublet, H<->H~
  swap = SM i*sigma2*K, Cartan diag(+i,-i) flips hypercharge, U(1)_Y->U(1)_T3R) -- "more than a
  name coincidence." But it acts holomorphically as j=1 on the vertical fibre m_0, NOT on the
  horizontal Higgs doublet m_3 (so(4)=6 > u(2)=4: no second holomorphic doublet-SU(2)). Calling
  it the PHYSICAL custodial symmetry requires (i) the dimensionally-reduced Higgs potential to be
  the accidental-Sp(1)_R-symmetric quaternionic-frame V(|Phi|^2) (not yet constructed), and (ii)
  fixing the free semisimple SU(3):SO(3) coupling/squash modulus t (only pinned at the two
  Einstein points, by curvature, not by gauge physics). "Less than a derivation."

- **Compactification scale / matter content.** The few-TeV M_c assumes literal SM matter; a real
  prediction needs the actual X_{1,1} spin^c-Dirac spectrum (and would include KK-tower power-law
  running / thresholds), and must be reconciled with collider bounds on KK gauge bosons.

- **C7 (De Vries).** NO LONGER BLOCKED (definition located in docs/, quoting the user files).
  The signed Hessian A(D)=[[0,D†],[D,−D†D]] with D†D=j(j+1), the c=1 condition, and the EW
  assignment (j=1/2⇒J=3/4, j=1⇒J=2) give cos²θ_W=a_{1/2}/a_1 ⇒ sin²θ_W=0.2231013223 — VERIFIED
  in sympy (matches the PDG on-shell value). Two findings: (i) placement vs the spin^c
  spectral-triple SM is INDEPENDENT — the block FORM overlaps the Dirac-square structure, but
  c=1 is not implied by the order-one condition, the inner-fluctuation/Higgs mechanism, or the
  KO/real structure; (ii) the geometric split (q8 even/j=1/no spin^c vs q8 odd/j=1/2/spin^c, via
  the proven parity law q8≡2I mod 2 + T1's L=O(odd)) makes the LABELS automatic, but c=1 — and
  even D†D=j(j+1) (a spin^c Dirac square is C_G−C_K+|ρ|², not bare j(j+1)) — remain EXTRA
  POSTULATES, the docs' own open "Deliverable 4" and kill-criterion. STILL OPEN: whether a real
  first-order D_patch on the geometry yields c=1 (the De Vries operator's geometric origin).
  Provenance caveat: recovered from the docs synthesis, not from raw files in tasks/.

- **C5 vs C7 — two competing sin²θ_W mechanisms.** The proposal now carries TWO predictions for
  the same observable: C5/T3 homogeneous Killing-inertia → tree 1/4 (runs to 0.231 at M_c≈3.7 TeV)
  vs C7 De Vries signed-Hessian → scale-free 0.2231 directly. As raw values they COMPETE
  (1/4 ≠ 0.2231); reconciled only by scale/role separation. The documents pick the De Vries W/Z
  ratio as the "real" Tier-0 prediction and explicitly demote the raw CP² Fubini-Study 1/4.

### Bottom line
The geometric and group-theoretic core of the proposal (C1-C4, and the non-arbitrariness of the
Weinberg angle C5) is correct and well-grounded. The headline weakness flagged by the
verification is the C5 semisimple caveat (custodial coupling is a free modulus, not predicted),
the unresolved C3-physics custodial identification (correct algebra, wrong locus, needs the
reduced potential), and -- most seriously -- the still-ACTIVE Witten odd-dimension chirality
no-go (C6), which the spin^c twist does not evade. One CLAIMS.md literature characterization
(CDF = CP^2xS^3) is factually corrected. C7 (De Vries) was UNBLOCKED once its definition was
found in docs/: the c=1 signed-Hessian algebra is verified and lands sin²θ_W=0.2231 on the
on-shell value, but as a prediction-from-geometry it rests on two undischarged postulates (c=1
and D†D=j(j+1)) and competes with — rather than confirms — the C5 raw-inertia value 1/4.
