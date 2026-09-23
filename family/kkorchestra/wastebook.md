# Wastebook: Higgsing the Kaluza–Klein carrier — CP^2 / Aloff–Wallach route

Historical ledger.  Entries below preserve the verification trail, including claims later rejected
as production inputs.  Current produced documents must not use a bare `D†D=j(j+1)` assumption; the
allowed form is a specified operator with squared modulus `P†P|_j=x0 C_2(j)+sigma_j`.

## Toolkit
numpy 2.4.4, scipy 1.17.1, sympy 1.14.0, mpmath 1.3.0 — full stack.

## Question
The uploaded note proposes replacing the quaternionic Hopf fibration
  S^3 -> S^7 -> S^4   (fibre SU(2), base symmetry SO(5))
as a Kaluza–Klein "carrier" by an Aloff–Wallach construction
  SO(3) -> X_{1,1} -> CP^2 ,   X_{1,1} = SU(3)/U(1)_{1,1} = (SU(3) x SO(3))/U(2)_Delta,
because CP^2 = SU(3)/U(2) has stabilizer U(2) ~ SU(2) x U(1) (electroweak-like) rather
than SO(5). Claims to test, in order of centrality:

(C1) CP^2 / conj ≅ S^4 (Kuiper–Massey); branched 2:1 cover CP^2 -> S^4 over RP^2; the
     conjugation quotient is NOT SU(3)-equivariant (only an SO(3) subgroup survives).
(C2) Aloff–Wallach X_{k,l}=SU(3)/U(1)_{k,l}, U(1)_{k,l}=diag(z^k,z^l,z^{-k-l}); projection
     to CP^2 with lens-space fibre U(2)/U(1)_{k,l} ≅ S^3/Z_{|k+l|}.
(C3) X_{1,1}: |k+l|=2 => fibre S^3/Z_2 = RP^3 ≅ SO(3); the Wilking identification
     X_{1,1} ≅ (SU(3) x SO(3))/U(2)_Delta; dimension 7; isotropy rep.
(C4) CP^2 is not spin (w_2≠0); it is spin^c. Boyer–Galicki–Mann: positive QK base => SO(3)
     principal bundle, 3-Sasakian total space, with an obstruction to lifting SO(3)->Sp(1)=SU(2).
     This lift is claimed to carry hypercharge / half-integer reps.
(C5) Weinberg angle: claim that g^2/g'^2 = I_{U(1)}/I_{SU(2)} (ratio of homogeneous Killing
     inertias) is determined by the homogeneous metric, not a free radius ratio — "non-arbitrary."
     TEST: how many free parameters actually remain in the normal-metric inertia ratio?
(C6) Literature anchors: Witten 1981 (7 = min dim for SU(3)xSU(2)xU(1)); Castellani–D'Auria–Fré
     (CP^2 x S^3 with SU(3) x SO(4)); Weinberg 1983 (charges/couplings from extra-dim inertias).
(C7) "De Vries" layer: a Dirac-type block A(D)=[[0,D],[D†,-D†D]] with eigenstructure j(j+1),
     pairing (a_1,b_1)<->SO(3)_R (j=1) and (a_{1/2},b_{1/2})<->Spin^c/SU(2) (j=1/2). Identify
     what this is and whether the geometric split makes it natural.

## Established  ✓
- (C1) CP^2/conj ≅ S^4 (Massey 1973, Kuiper 1974; Hillman arXiv:1705.05038 explicit). Branch locus
  RP^2, normal Euler number ±2. The involution-commuting group is SO(3)=real points of SU(3), so the
  quotient is SO(3)-equivariant but NOT SU(3)-equivariant. Note's C1 correct.
- (C1-structure) U(1)_{1,1} generator = i*diag(1,1,-2) is forced (commutant of su(2)_L) and equals the
  lambda_8/hypercharge direction inside U(2). So the quotiented circle in X_{1,1} IS the hypercharge U(1).
- (C2/C3) dim X_{1,1}=7; fibre U(2)/U(1)_{1,1} = PU(2) = SO(3) = RP^3 = S^3/Z_2 (|k+l|=2). [wb_1]
- (C3) Wilking (Proc. AMS 127, 1999): X_{1,1}=M^7_{1,1} isometric to normal homogeneous (SU(3)xSO(3))/U(2).
  Isometry group enhanced to SU(3)xSO(3); the extra SO(3) is a genuine second factor and is exactly the
  group acting transitively on the SO(3) fibre over CP^2 (custodial candidate).
- (C4) X_{1,1} = the homogeneous 3-Sasakian 7-manifold over Wolf space Gr_2(C^3)=CP^2 (Boyer-Galicki-Mann
  1994, Crelle 455). Konishi/Sakamoto: positive-scalar-curv QK base => principal SO(3) bundle with
  3-Sasakian total space; generic foliation fibre SO(3), Sp(1) only with extra lift. Note's C4 correct.
- (C4-spin) CP^2 not spin (w_2≠0, odd intersection form); spin^c. SO(3)->Sp(1)=SU(2) lift obstructed; this
  is where the spin^c line / hypercharge enters. Consistent with note.
- (C5-mechanism) For G SIMPLE the coset Killing-inertia I(X)=(1/8)tr_m(Q)|X|^2_Killing — ratio is
  metric-INDEPENDENT (Schur, adjoint irreducible). Verified numerically with anisotropic invariant metrics
  [wb_2: I(l3)/I(l8)≈1.01 stable across two different metrics]. Hence within SU(3) the SU(2)_L vs U(1)_Y
  coupling ratio is FIXED by group theory, not a free radius. Note's central claim (no free radius modulus
  for theta_W) is mechanically CORRECT.
- (C5-value) Tree sin^2(theta_W) = Tr(T3^2)/Tr(Q^2) over an SU(3) multiplet = 1/4 (lepton 3-plet,
  g'^2/g^2=1/3) or 3/4 (quark 3-plet). [wb_3] Independent corroboration: 7D KK with shape modulus gives
  0.25<sin^2<1, =1/4 at the symmetric point (Nucl.Phys.B 1985, 0550-3213(85)90232-9).
- (C6) Witten 1981 (NPB186,412): 7 = min dim for SU(3)xSU(2)xU(1) from 11D SUGRA; fermion chirality is the
  known obstruction. Weinberg/Candelas-Weinberg 1983-84: couplings from internal circumferences/inertias.

## Conjectures  ~
- (C3-physics) Fibre SO(3) = custodial SU(2)_R/SO(3)_R: the Wilking extra-SO(3) factor IS a genuine extra
  isometry acting on the fibre (established), but its identification as the physical CUSTODIAL symmetry of
  the SM Higgs sector is an interpretation, not shown. Needs harmonic/scalar-sector analysis.
- (C5-caveat) 1/4 is the symmetric-point tree value; agreement with 0.231 requires RG running from the
  compactification scale and a specified matter embedding (which rep the SM matter occupies). The custodial
  SO(3) coupling RELATIVE to electroweak is a free modulus (relative size of the SU(3) vs SO(3) factor),
  since the full isometry SU(3)xSO(3) is semisimple not simple — so custodial-protection strength is tunable,
  not predicted. Note does not flag this.

## Failed  ✗
- (none outright false). The one correction: the SO(3) fibre is, in the bare-SU(3) picture, the
  projectivization of the SAME U(2) containing SU(2)_L — it is the enhanced SU(3)xSO(3) structure (not the
  bare coset) that supplies an independent SO(3) for a custodial reading. Identification requires the
  enhancement.

## Open  ?
- (C7) "De Vries condition" / block A(D)=[[0,D],[D†,-D†D]] with eigenstructure j(j+1), pairs
  (a_1,b_1)<->j=1, (a_{1/2},b_{1/2})<->j=1/2: structure is recognizably in the spin^c spectral-triple /
  Higgs-as-connection family (Connes-Chamseddine; spin^c-only SM, arXiv:2001.02902), but no PUBLIC result
  named "De Vries" matched. Referenced via user's own files (kk_devries_signed_hessian). Treat as
  user-internal; cannot verify without those files.
- Exact spin^c structure / Kreck-Stolz invariants of X_{1,1}; the explicit hypercharge line bundle.
- Full invariant-metric moduli under the enhanced SU(3)xSO(3) (bare count is 10 [wb_2]; enhanced is far fewer
  — Wilking's normal-homogeneous metric is 1-parameter); locate Einstein/3-Sasakian points.
- Whether CDF (0550-3213(84)90265-7) or anyone built a CP^2-based (not S^4-based) KK custodial model before.
- The chirality problem (Witten no-go) for this specific carrier: does the spin^c twist evade it?

## Workflow verdicts (2026-05-31)

Consolidated synthesis over subtasks T1–T6 (+ independent verifiers). Report: archive/verification_20260531/REPORT.md.

- **C1 (CP^2/conj=S^4, SO(3)- not SU(3)-equivariant) — CONFIRMED.** Already Established
  (Massey 1973/Kuiper 1974/Hillman arXiv:1705.05038); reconfirmed in T1 context. U(1)_{1,1}
  generator = i·diag(1,1,−2) = λ_8 (commutant of su(2)_L) [wb_1]. Deciding: wb_1 + Hillman.

- **C2 (X_{k,l} fibres over CP^2, fibre S^3/Z_{|k+l|}) — CONFIRMED.** dim X_{1,1}=7; fibre
  U(2)/U(1)_{1,1}=PU(2)=SO(3)=RP^3=S^3/Z_2 (|k+l|=2). |H^4(X_{k,l})|=|k^2+kl+l^2| DERIVED via
  Gysin det (=|(k+l)^2−kl|, identity proven in sympy), cyclic since gcd=1, =Z/3 at (1,1).
  Deciding: calc/wb_T1.py + Escher–Ziller BundleTop.pdf Prop 4.3.

- **C3 (fibre SO(3), Wilking (SU(3)×SO(3))/U(2)_Δ, dim 7) — CONFIRMED.** T2 reproduces the
  Wilking 1-parameter family g_t (10→2→1 via Schur), the SO(3)-fibre summand m_0=su(2)_L
  (vertical), CP^2 base m_3 (horizontal). Two Einstein metrics: 3-Sasakian t=+1, squashed
  t=−3/5, exact 1/5 squash factor. Wilking cite corrected to Proc. AMS 127 (1999) **1191–1194**
  (NOT 3111). Deciding: calc/wb_2c.py + Wilking 1999.

- **C4 (CP^2 non-spin/spin^c; X_{1,1} BGM 3-Sasakian; SO(3)→Sp(1) obstruction = hypercharge)
  — CONFIRMED, with a sharpening that CORRECTS T6.** Computed: w_2(TCP^2)=H≠0 (CP^2 non-spin);
  **w_2(TX_{1,1})=0, X_{1,1} is SPIN** (Escher–Ziller Prop 4.3; BGM/BG98 Cor 1.2.7 "every
  3-Sasakian manifold is spin"). The spin obstruction lives on the BASE CP^2, repaired by an
  ODD line bundle L=O(k), k odd (minimal O(1); canonical spin^c det K^{-1}=O(3)); charge-n
  line bundle = O(n) along λ_8 hypercharge. Kreck–Stolz: s_1=1/112, s_2=−1/36≡35/36, s_3=1/18,
  p_1=0 mod 3. NOTE: T6 §(c) wrongly said w_2(X_{1,1})≠0 — corrected here (X_{1,1} spin); the
  Witten verdict is unaffected. Deciding: calc/wb_T1.py + Escher–Ziller Prop 4.3 + BG98 Cor 1.2.7.

- **C5 (Weinberg angle = Killing-inertia ratio, non-arbitrary) — CONFIRMED (load-bearing),
  with the semisimple-modulus caveat.** Proven EXACTLY (not Monte-Carlo): SU(3)-invariant
  symmetric-form space is 1-dim (adjoint irreducible ⇒ Schur), so I(X)=(1/8)tr_m(Q)|X|^2 and
  sin^2θ_W is metric-INDEPENDENT within the simple SU(3). Tree sin^2=Tr(T3^2)/Tr(Q^2)=1/4
  (lepton 3-plet; rep-independent), 3/4 (quark), 1/2 (full gen). Hypercharge norm k_Y=3 (NOT
  SU(5) 5/3). SM 1-/2-loop running reaches 1/4 at M_c≈3.7/3.85 TeV ⇒ literal tree boundary
  forces a few-TeV compactification scale. CAVEAT (now firmly Established, was Conjecture): the
  custodial SO(3) coupling g_cust^2/g_EW^2=1/(1+t) is a FREE modulus (SU(3)×SO(3) semisimple,
  not simple); custodial strength tunable, not predicted. Deciding: calc/wb_3a_exact.py,
  wb_3b/d/e/g.py + Candelas–Weinberg 1984.

- **C6 (Witten 1981, CDF, Weinberg 1983 anchors) — CONFIRMED with one citation CORRECTED.**
  Witten 1981 (NPB186,412) = 7 min dim + chirality obstruction: confirmed. Witten 1983 Shelter
  Island = odd-dim no-go: confirmed (= ref [16] in Dolan–Nash). **CDF doi 10.1016/0550-3213(84)
  90265-7 CORRECTION: the paper is "SU(3)⊗SU(2)⊗U(1) from D=11 SUGRA" using M^{p,q,r} = U(1)
  bundle over CP^2×S^2, NOT the product "CP^2×S^3 with SU(3)×SO(4)" as CLAIMS.md C6 states.**
  Isometry is SU(3)×SU(2)×U(1) (SU(3)×SU(2) at M^{1,1,1}), never SU(3)×SO(4). No prior KK/coset
  model uses CP^2 as sole base with custodial symmetry from the fibre (no_prior_instance=TRUE).
  Chirality: Witten odd-dim no-go ACTIVE for X_{1,1}; spin^c (which repairs the BASE w_2) does
  NOT evade it (Cl(7) simple, charge-conjugate pairing ⇒ vector-like). Deciding: T6 PDF
  extractions (DNP25 arXiv:2502.07710, BG98, Wilking, Dolan–Nash) + ScienceDirect PII.

- **C7 ("De Vries condition" / signed Dirac-block Hessian) — UNBLOCKED & RUN (T5, 2026-05-31).**
  Definition located in docs/KaluzaKlein_Hilo_Higgsing_KaluzaKlein_Review.md (quoting the user
  files kk_devries_signed_hessian + KK-addenda-DolanNash-and-WZ); raw files still absent from
  tasks/ (provenance caveat). VERIFIED in sympy: signed Hessian A(D)=[[0,D†],[D,−D†D]], D†D=J=
  j(j+1), two-coeff A_c(D)=[[0,D†],[D,−c·D†D]], **De Vries condition c=1** (load-bearing: c=0.5→
  sin²=0.3014, c=1→0.2231, c=2→0.1198). Char poly λ²+Jλ−J=0; roots +a_J (positive, vector-mass
  branch) and −b_J (negative, scalar-instability/VACUUM branch), a_J=(√(J²+4J)−J)/2, b_J=
  (√(J²+4J)+J)/2. EW assignment j=1/2⇒J=3/4, j=1⇒J=2: a_{1/2}=(√57−3)/8, b_{1/2}=(√57+3)/8,
  a_1=√3−1, b_1=√3+1. cos²θ_W=M_W²/M_Z²=a_{1/2}/a_1=(√57−3)(√3+1)/16 ⇒ **sin²θ_W=(19+3√3−√57−
  3√19)/16=0.2231013223** (≈ PDG on-shell), the scale-free "Tier-0" prediction.
  • Placement vs spin^c spectral-triple SM = **INDEPENDENT**: the block FORM overlaps the
    Dirac-square / chiral-off-diagonal structure (CCM §3.6; arXiv:2001.02902 Krein-shift;
    arXiv:1703.05279), but c=1 is NOT implied by the order-one condition, the inner-fluctuation/
    Higgs mechanism, or the KO/real structure.
  • Geometric naturalness = **EXTRA-POSTULATE**: T4's proven q8≡2I mod 2 + T1's L=O(odd) make the
    LABELS (j=1 SO(3)-fibre / j=1/2 spin^c-doublet) and the existence of D_patch automatic, but
    c=1 — and even D†D=j(j+1) (a spin^c Dirac square is C_G−C_K+|ρ|², not bare j(j+1)) — are
    UN-DERIVED. Both are the docs' own open "Deliverable 4" / kill-criterion.
  • C5 vs C7: **two competing sin²θ_W mechanisms** for the same observable — raw Killing-inertia
    1/4 (+RG to M_c≈3.7 TeV) vs scale-free De Vries 0.2231. They compete (1/4≠0.2231); the docs
    pick De Vries as the real prediction and demote the Fubini-Study 1/4.
  Verifier survives (conf 0.9, number reproduced to 12 digits, no fatal/major). Deciding: archive/verification_20260531/T5.md
  + sympy (/tmp/devries*.py) + CCM/Connes local docs + arXiv:2001.02902, 1703.05279.

### Resolved Open items (moved from Open)
- Exact spin^c structure / Kreck–Stolz invariants / hypercharge line bundle of X_{1,1}: RESOLVED
  by T1 (s_1=1/112, s_2=35/36, s_3=1/18; L=O(odd), minimal O(1); X_{1,1} spin).
- Enhanced SU(3)×SO(3) invariant-metric moduli + Einstein/3-Sasakian points: RESOLVED by T2
  (Wilking 10→2→1; Einstein at t=+1 3-Sasakian and t=−3/5 squashed; 1/5 squash).
- Whether anyone built a CP^2-based KK custodial model before: RESOLVED by T6 — none found
  (no_prior_instance=TRUE); and CDF's actual content corrected (M^{p,q,r}, not CP^2×S^3).
- Chirality (Witten no-go) for this carrier / does spin^c evade it: RESOLVED by T6 — no-go
  ACTIVE; spin^c repairs base w_2 but does not evade odd-dim chirality pairing.

### Still Open / Conjectural
- (C3-physics) Whether the KK-reduced Higgs potential on X_{1,1} actually has the accidental
  Sp(1)_R symmetry that would make the Wilking SO(3) the PHYSICAL custodial SU(2)_R: T4 shows
  the SO(3)_R has the correct custodial ALGEBRA + breaking pattern (right-quaternion (2_L,2_R)
  bidoublet, H↔H̃ swap, U(1)_Y→U(1)_T3R) but acts holomorphically as j=1 on the FIBRE m_0, not
  on the horizontal Higgs doublet m_3 (so(4)=6 > u(2)=4 obstruction). "More than a name
  coincidence, less than a derivation." Needs the explicit reduced potential.
- (C5) The custodial coupling/squash modulus t is fixed only at the two Einstein points by
  curvature; no dynamical vacuum-selection principle pins it.
- (C7) De Vries ALGEBRA verified (sin²θ_W=0.2231); but the c=1 factorization and the
  D†D=j(j+1) identification are EXTRA POSTULATES. STILL OPEN: construct a real first-order
  D_patch on the spin^c-lifted SO(3)→X_{1,1}→CP² bundle whose second variation is exactly
  A(D) (c=1), i.e. derive 0.2231 from the geometry rather than postulate it (docs' Deliverable 4).
  Also open: which (j=1/2,j=1) → (W/Z) slot assignment is forced (q8=±1 vs ±3 doublets).
- A full M_c prediction needs the actual X_{1,1} spin^c-Dirac matter spectrum (not done; T3's
  few-TeV scale assumes literal SM matter); KK-tower power-law running / thresholds not included.
- T4 wb_T4d.py has a (minor, flagged) left/right quaternion labeling error in the illustrative
  J-rotation demo (does not affect the obstruction conclusion); wb_2b.py has a buggy Ricci
  closed-form, SUPERSEDED by the validated wb_2c.py.

## Scratchwork
(newest on top)

- **[R4, 2026-05-31] The 1/4 inertia and "why not 3/8".** sin^2=1/(1+k_Y); lepton 3-plet k_Y=3→1/4,
  SU(5) 5bar k_Y=5/3→3/8. R4 (verified conf 0.96): 3/8 is unreachable in this carrier — setting
  sin^2=3/8 forces the hypercharge coefficient b=±√5/6 ⇒ IRRATIONAL electric charges (number-
  theoretic: 5n²=36m² has no integer solution). Structural reason: CP^2=SU(3)/U(2) is the
  ELECTROWEAK SU(3) (3-plet = weak doublet+singlet, no colour); 3/8 needs colour+EW in ONE SIMPLE
  group. **CP^3=SU(4)/U(3) is that group: SU(4)=Pati-Salam (U(3)=SU(3)_c×U(1)_{B−L}, lepton=4th
  colour), SO(10)-16 → sin^2=3/8 (verified).** So 1/4 ↔ EW SU(3)/CP^2, 3/8 ↔ Pati-Salam SU(4)/CP^3
  (the 2nd factor of the fuzzy CP^2×CP^3 generation structure), De Vries 0.2231 ↔ c=1 signed Hessian
  — three distinct mechanisms. Holds under EITHER CP^2 identification since SU(3)×SO(3) is semisimple.
  Deciding: calc/r4_38.py, r4_pati_salam.py, archive/verification_20260531/R4.md.

- **[OPEN FORK, user-raised 2026-05-31] Which SU(3)?** All Round-1/R4 physics assumed CLAIMS.md's
  CP^2-base SU(3) = ELECTROWEAK (3-3-1/Weinberg-SU(3)_L, no colour). User proposes the FLIP:
  CP^2 base = COLOUR SU(3)_c, S^3/SO(3) fibre = electroweak SU(2)_L. Geometry (C1-C4) is
  identification-INDEPENDENT; the physics (θ_W=1/4, hypercharge locus, custodial T4, De Vries EW
  assignment) is NOT — it is Option-A-specific. Option B is arguably more physical (has colour;
  unbroken-colour=base-isometry matches KK; fibre SO(3)→SU(2) lift obstruction = the U(1) completing
  EW). Open obstruction: origin of U(1)_Y under colour-base; θ_W must be RE-DERIVED (1/4 does not
  apply). Candidate task R5: work out the flipped identification. NOT YET RUN.
