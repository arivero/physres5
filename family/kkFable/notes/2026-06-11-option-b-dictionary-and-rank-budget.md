# N1 — Option-B dictionary and the gauge-rank budget

Date: 2026-06-11.

**VERDICT: The Option-B identification is well-posed as a map of symmetry
factors, and its breaking-pattern reading (unbroken colour = base isometry,
weak broken in the fibre sector) survives. But the carrier's 4D gauge content
is SU(3)×SO(3) with Cartan rank 3, while Option B needs rank 4; the deficit —
no Killing direction left for a dynamical U(1)_Y — is re-derived by hand below
and is structural, not a normalization choice. (Confirms R5 verification pass
2; feeds N2, N3.)**

## 1. Carrier data (cited)

X_{1,1} = SU(3)/U(1)_{1,1}, with U(1)_{1,1} = {diag(z, z, z^{-2})}, generator
H8 = diag(1,1,−2). Wilking presentation X_{1,1} ≅ (SU(3)×SO(3))/U(2)_Δ;
fibration SO(3) → X_{1,1} → CP² = SU(3)/U(2). Isometry group of every metric
in the invariant family: SU(3)×SO(3) (Wilking 1999, via T2/T3; cited). All of
this is identification-independent (C1–C4, Established).

## 2. Hand derivation: where the SO(3) factor comes from

Expansion block.
- Variables/domain: G = SU(3); H = U(1)_{1,1} ⊂ U(2) := S(U(2)×U(1)) ⊂ G;
  coset X = G/H with left G-action.
- Claim: the normalizer N_G(H) contains U(2), and N_G(H)⁰/H ≅ SO(3) acts on X
  on the right, commuting with the left G-action.
- Calculation: U(1)_{1,1} = {diag(z,z,z^{-2})} is the centre of U(2) (an
  element diag(A, det A^{-1}) commutes with diag(z,z,z^{-2}) for every A ∈
  U(2), and conversely a central element of U(2) must be scalar in the 2×2
  block, hence of the form diag(z,z,z^{-2}) by the determinant condition). A
  subgroup is normalized by anything that centralizes it, so U(2) ⊆ N_G(H).
  For n ∈ N_G(H), the map xH ↦ xnH is well defined on X and commutes with
  every left translation; its kernel as an action of N_G(H) is H itself. Hence
  the group acting is N_G(H)⁰/H ⊇ U(2)/Z(U(2)) = PU(2) ≅ SO(3).
- Orbits: the right-U(2) orbit through xH is xU(2)/H = U(2)/U(1)_{1,1} =
  PU(2) ≅ SO(3) ≅ RP³ — these orbits are the fibres of X → CP² = G/U(2). So
  the SO(3) factor acts transitively on each fibre and trivially on the base
  point. (Matches T2's m_0 = vertical block.)
- Maximality (cited, not re-proven): Wilking 1999 shows SU(3)×SO(3) is the
  full isometry group of the invariant family; kkFable uses only "at least"
  (derived here) plus "no more" (cited).
- Status: derived here (existence), cited (maximality).

One structural fact falls out of this derivation and carries N2: the circle
U(1)_{1,1} = Z(U(2)) — the only U(1) available to complete the fibre PU(2) to
U(2) — **acts trivially on X by construction** (it is the quotiented isotropy
circle). It contributes no Killing vector and therefore no 4D gauge boson.

## 3. The Option-B dictionary

| Geometric object | Option-B physics |
|---|---|
| left SU(3) (base isometry, transitive on CP²) | colour SU(3)_c, unbroken |
| right SO(3) (fibre isometry, transitive on RP³ fibres) | weak SU(2)_L (as SO(3) = SU(2)/Z₂; rep content of matter handled in N2/N6) |
| U(1)_{1,1} = Z(U(2)) (acts trivially on X) | the only intrinsic hypercharge-like circle; background/structure datum (N2) |
| m_0 (vertical, scale x1) | weak-sector block |
| m_3 (horizontal, scale x2) | colour/base block |
| Wilking modulus t = x1/x2 − 1 | free shape modulus (becomes the θ_W modulus in N3) |

## 4. Hand derivation: the rank budget

Expansion block.
- Rule used: in Kaluza–Klein reduction on a homogeneous space, the massless 4D
  gauge bosons are in one-to-one correspondence with the Killing vectors; the
  4D gauge group is the isometry group (Weinberg 1983 / standard KK; cited via
  T3). Commuting independent gauge bosons = Cartan generators of Isom.
- Carrier budget: rank(SU(3)×SO(3)) = rank SU(3) + rank SO(3) = 2 + 1 = **3**.
  Explicitly: {λ_3-direction, H8-direction} ⊂ su(3), {T_3} ⊂ so(3).
- SM demand: rank(SU(3)_c × SU(2)_L × U(1)_Y) = 2 + 1 + 1 = **4** (two gluon
  Cartans, W³, B). The four must be independent massless 4D vector fields.
- Option-B allocation: SU(3) → SU(3)_c consumes both base Cartans as gluons
  (under Option B, λ_3 and H8 are colour-octet members, see N2 §2); SO(3) →
  SU(2)_L consumes the fibre Cartan as W³. Remaining Cartan directions for a
  hypercharge boson: 3 − 3 = **0**.
- Linear-algebra closure: any candidate Y boson would be a constant linear
  combination of the 11 isometry gauge fields; commuting with all of SU(3)_c
  forces it into the centralizer of su(3) inside su(3)⊕so(3), which is so(3);
  commuting with all of SU(2)_L then forces it into the centralizer of so(3)
  in so(3) = 0. So no combination works — the deficit is not evaded by mixing.
- Option-A contrast: Option A needs only T_3 and Y as electroweak Cartans and
  places both inside the simple SU(3) (rank 2 of the available 3 used; the
  SO(3) factor stays a spectator). Option A fits the budget; Option B exceeds
  it by one.
- Residuals: gauge bosons of non-isometry origin (p-form/Betti U(1)s) are not
  counted here; they are examined and killed as hypercharge in N2 §5.
- Status: derived here. Agrees with R5 verification pass 2 (its MAJOR
  correction), now obtained without computer algebra.

## 5. Breaking pattern under Option B (restated with one correction)

R5(a) concluded: unbroken colour = unbroken base isometry is natural, and weak
breaking belongs to the fibre/Higgs sector. Both halves survive re-statement,
with one sharpening:

- The KK vacuum (any invariant metric g_t) leaves the **entire** SU(3)×SO(3)
  unbroken — changing the squash modulus t does not break any isometry, since
  every g_t is invariant under the full group (T2). So "shrinking the fibre"
  by itself is not a Higgs mechanism for SU(2)_L.
- Electroweak breaking therefore requires a vev in a charged harmonic sector
  (a 4D scalar field), not a shape change. Which charged scalars exist, and
  whether any is a colour singlet, is the subject of N6 — and the answer found
  there (no colour-singlet weak-doublet scalar exists on X_{1,1}) is what
  ultimately decides the Option-B Higgs question.
- The asymmetry that favours Option B's reading stands: colour must be
  unbroken, and the base isometry is automatically unbroken; Option A instead
  assigns a broken gauge sector (electroweak) to the never-broken base.

## 6. Counterargument pass

1. *"The isometry group might be larger for a special metric, supplying the
   missing Cartan."* Wilking's theorem covers the whole invariant family; the
   enhancement from the bare-coset expectation already happened (SU(3)×U(1)
   → SU(3)×SO(3) absorbs the normalizer circle into SO(3)). A larger group
   would contradict the cited classification. Rejected on the cited theorem;
   if a non-invariant metric were used, the carrier would no longer be the
   homogeneous X_{1,1} of C1–C4.
2. *"W bosons could come from somewhere other than the isometry, freeing the
   fibre Cartan to serve as Y."* Massless non-abelian 4D gauge fields in KK
   arise only from isometries; charged vectors from generic KK towers sit at
   the compactification scale. Then SU(2)_L would be absent at low energy.
   Rejected.
3. *"The deficit is an artifact of demanding all four Cartans be isometric;
   the SM only needs U(1)_Y as a gauge symmetry of the effective theory."*
   Correct as stated — and that is the precise content of the verdict: on
   X_{1,1}, Y can exist only as a non-isometric (background/bundle) datum,
   which yields no massless 4D Y boson. Whether such a background Y suffices
   for any SM-like reading is the question N2 and N6 answer.

## 7. Kill criteria / what would overturn this note

- Exhibiting a fourth commuting massless vector in the KK spectrum of X_{1,1}
  with charged light matter (N2 §5 examines the only known candidate class,
  Betti U(1)s, and finds the charged-matter requirement fails).
- A flaw in the centralizer computation of §4 (elementary; two lines).

## Sources

- Wilking, Proc. AMS 127 (1999) 1191–1194 (isometry enhancement; via T2/T3).
- archive/verification_20260531/R5.md (parts (a), (d); verification pass 2,
  rank deficit).
- archive/verification_20260531/T2.md (metric blocks, modulus t).
- archive/verification_20260531/T3.md (KK coupling/inertia rule).
- Weinberg 1983 doc (`docs/Weinberg_Charges_From_Extra_Dimensions_1983.md`),
  couplings from internal inertias.
