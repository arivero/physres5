# N12 — Ladder transitions: the quintet collapse, charge-to-flux conversion, and the two exits

Date: 2026-06-12.

**VERDICT: The D7→D6 transition is now a derived mechanism, and the
gauge-boson transport problem (N9 §4) splits cleanly. (1) The collapse
X_{1,1} → Y_6 is an invariant-metric family (axis-squash of the fibre) whose
order parameter is a weak QUINTET (I_w = 2) metric modulus: W^± Higgs up
along the family while U(1)_{T₃} stays exact. (2) Quantum numbers transport
smoothly: the eaten fibre weight becomes the monopole flux of the limit,
r = 2I₃ — the mechanism behind N9's electroweak alternation. (3) Gauge
DYNAMICS does not transport: the broken pair exits through a diverging vev
(infinite distance in moduli space) while the surviving abelian exits
through diverging coupling at zero mass — user-raised dichotomy ("vacuum to
infinity" vs "only the masses go") realized BOTH at once, assigned by
representation. (4) The restoration direction D6→D7 passes the inherited
M-theory-style tower test by construction (modulus = circle radius, infinite
family = flux charges, M ~ |r|/R): a continuous control parameter with a
critically discontinuous endpoint — the 10↔11-type jump in total dimension,
with the Mexican-hat distinction (sliding a vev vs changing the potential's
shape) locating the genuine criticality at the endpoint, not along the
family. D6↔D5 remains the open half, organized by the same dichotomy.**

Conventions: N0; total spacetime dimension D_tot = 4 + D_int, so the
internal ladder D5/D6/D7 reads 9/10/11 in total — the numerology of the
classic string/M-theory jumps, used here only as an organizing analogy.
Inputs: N9 (alternation), T2 (metric family, Einstein points), check E Q4
(charge-to-flux), prior-notes/MTheory_Style_Tower_Test_For_Extra_Dimension.md
(criterion), docs/SourceDigest_Witten_MTheory_Jump_arXiv.md (benchmark),
prior-notes/Bosonic_Potential_Stabilization_System.md (potential data).

## 1. The collapse family

Expansion block.
- U(1)_{1,1} acts trivially on m_0 (all of m_0 sits at q8 = 0), so ANY inner
  product on m_0 extends to an invariant metric on X_{1,1} (part of T2's
  10-parameter family). Choose the T₃-axis split m_0 = R·T₃ ⊕ m_0^⊥ and set
  g = x_∥ (−B)|_{T₃} ⊕ x_⊥ (−B)|_{m_0^⊥} ⊕ x₂ (−B)|_{m_3}.
- Isometry along the family: left SU(3) always; right SO(3) iff x_∥ = x_⊥,
  else right U(1)_{T₃} (the split is U(1)-invariant: T₃ fixes its axis and
  rotates m_0^⊥). Berger-type fibre squash; curvature stays bounded as
  x_∥ → 0 and the Gromov–Hausdorff limit is Y_6 = X_{1,1}/SO(2) (the
  S¹ = T²/U(1)_{1,1} orbits collapse).
- Status: derived (the only cited input is T2's parametrization).

## 2. The order parameter is a weak quintet

Expansion block.
- The space of inner products on m_0, as a representation of the right
  SO(3), is Sym²(3) = 1 ⊕ 5: the trace (overall fibre scale, the old t
  modulus) and a QUINTET. The axis-squash x_∥ ≠ x_⊥ is the I₃ = 0 component
  of the 5.
- 4D reading: the quintet is a scalar field Φ₅ (colour-singlet, I_w = 2,
  Y = 0 — an allowed slot by N6's rules: integer I_w at q8 = 0 ✓);
  the family is its flat direction at frozen shape. A vev ⟨Φ₅⟩ ∝
  (x_⊥ − x_∥) breaks SU(2)_L → U(1)_{T₃} with
  M²(W^{I₃ = ±1}) ∝ g₂² ⟨Φ₅⟩², M(W⁰) = 0 — geometric Higgsing in the
  I_w = 2 channel.
- Honesty: an I = 2 order parameter is NOT the SM doublet mechanism (it
  preserves no custodial relation and gives no fermion masses); it is the
  LADDER's own Higgsing. The SM-Higgs slot lives elsewhere (N11 §3). The
  two must not be conflated; under Option A this same quintet is the
  T3-axis squash of the custodial fibre — also not the SM Higgs.
- Status: derived (representation content); the mass formula's coefficient
  needs the reduced kinetic normalization (target; scaling and group theory
  suffice for this note's claims).

## 3. Quantum numbers transport: charge → flux (r = 2I₃)

Expansion block.
- On the fibre RP³ = SO(3), L² = ⊕_I V_I ⊗ V_I* (integer I); collapsing the
  right-T₃ orbits sends the right-weight-I₃ component to sections of the
  monopole bundle O(r) over the limit S² with r = 2I₃ (4π fibre period;
  check E Q4 CONFIRM).
- Ladder meaning: a D7 mode's gauged U(1)_{T₃} charge becomes, at D6, the
  vertical monopole flux label r of the fermion bridge (its "weak twist") —
  and N9's alternation now has a mechanism: collapse converts ISOMETRY
  CHARGE into FLUX LABEL; restoration converts back. The same statement on
  the other circle (U(1)_{1,1}) is T1's: its charge is the O(n) flux at
  every rung where it is not geometric.
- Status: derived for the fibre (the global statement on X_{1,1} follows
  fibrewise; the base spectator indices are untouched by the collapse).

## 4. Dynamics does not transport: the two exits

Expansion block. Track couplings and masses through x_∥ → 0 with the
inertia rule (1/g² ∝ block scale × volume, V ∝ √(x_∥ x_⊥² x₂⁴)):
- **Broken pair W^± — the vev exit.** 1/g_W² ∝ x_⊥ V stays finite (mildly
  x_∥-dependent through V); the canonical modulus distance behaves as
  σ ∝ M_P log(x_⊥/x_∥) → ∞: infinite distance in moduli space, the vev
  ⟨Φ₅⟩ → ∞ in canonical units, M_W → ∞ with g_W finite. The broken sector
  decouples by vacuum displacement: the user's "vacuum goes to infinity"
  aspect.
- **Surviving U(1)_{T₃} — the coupling exit.** Massless along the whole
  family (exact isometry), but 1/g²_{T₃} ∝ x_∥ V → 0: the coupling
  DIVERGES at the endpoint with zero mass: the "only the masses/couplings
  go" aspect — at fixed (indeed zero) mass, the gauge dynamics leaves
  through strong coupling.
- So the transition realizes BOTH exits at once, assigned by
  representation: non-abelian broken directions exit via the vev; the
  surviving abelian exits via the coupling. The transport problem of N9 §4
  is now precisely located: charge lattices continue (§3), but the
  strong-coupling fate of the surviving abelian at the endpoint —
  confinement, duality, or absorption into the flux sector — is the open
  dynamical question. (At D6 the T₃-tower reappears as flux sectors; an
  infinitely-coupled U(1) whose charges have become flux labels is
  suggestively dual-sounding; recorded as a target, not a claim.)
- D5↔D6 (the 9↔10 rung) is organized by the same dichotomy, but the
  S² → S¹ fibre move is not a free-orbit collapse; the boundary reading
  (M_5(n) = ∂D(O(n)), index/inflow data on the disk bundle — the bridge
  note's framing plus Witten's orbifold/five-brane lesson) is the candidate
  framework. OPEN; the question to settle first: does the Y-boson of D5
  leave toward D6 through the vev aspect (decoupling with the broken
  sector) or the coupling aspect (strong coupling at zero mass)?
- Status: derived (both exits; the scalings are the inertia rule plus the
  log-canonical normalization of moduli kinetic terms); endpoint dynamics
  open.

## 5. Criticality: the 10↔11 reading and the tower test

Expansion block.
- The inherited criterion (M-theory-style tower test): an emergent/collapsing
  dimension must carry an infinite labelled family with a closing KK-like
  gap, the label geometric, the scaling computed not posited; a finite
  restored multiplet is only symmetry restoration.
- The D6→D7 restoration passes by construction: modulus = the circle size
  R ∝ √x_∥; infinite family = the T₃/flux charges r (geometric labels, §3);
  masses M_r ∝ |r|/R with the gap closing as R grows — Witten's three
  benchmark ingredients (radius modulus, infinite charge family,
  M ~ |n|/R), realized here literally rather than by analogy. In total
  dimension this is the 10 → 11 jump pattern: a continuously-moving
  parameter with a critically discontinuous endpoint (at x_∥ = 0
  infinitely many states degenerate and the description changes dimension).
- The Mexican-hat distinction (user-raised, 2026-06-12): moving along the
  family slides a vev within a fixed phase — nothing critical happens at
  any x_∥ > 0; genuine criticality requires the POTENTIAL to change shape.
  Two shape facts are inherited: the reduced potential on the t-axis has
  TWO stationary points (3-Sasakian t = +1 and squashed t = −3/5, T2's
  Einstein metrics) — a two-well structure on the invariant moduli — and
  the collapse direction is a runaway (infinite distance), not a minimum.
  The hat-formation question — which deformations (flux n, curvature
  couplings, the cosmological term) move the wells and can merge or create
  them — is the precise critical-structure target for the ladder; the
  Einstein-point data are its first two data points. Target for future
  derivation: the reduced V(x_∥, x_⊥, x₂) on the axis-squash family
  (the t-axis potential is in the prior Bosonic_Potential note; the
  quintet direction extends it).
- Status: tower test derived; hat-formation analysis open with named data.

## 5b. Collapse view vs emergence view (user-raised, 2026-06-12)

Question: N12 derives the D7→D6 COLLAPSE, while Witten's benchmark is the
D6→D7-shaped EMERGENCE (IIA → M: dimension grows with the modulus). Are both
views suitable?

Expansion block.
- Same family, two readings. Collapse (D7→D6): geometry fundamental; the
  momentum tower M_r ∝ ħ|r|/R decouples upward; flux labels = frozen
  charges (§3). Status: derived. Emergence (D6→D7): the D6 description
  fundamental; the flux sectors r are discovered to organize into a tower
  whose gap closes as the modulus grows; the circle is inferred, not
  assumed. Status: suitable as kinematics, but with one missing dynamical
  ingredient relative to Witten's case:
- The BPS asymmetry. Witten's D0 tower is BPS: M_n = |n|/(g_s ℓ_s) exactly
  linear in the charge, protected to strong coupling — that linearity is
  tower-test ingredient 3 and SUSY pays for it. Here, near the D6 end the
  monopole-sector ground masses scale as M_r² ∝ ħ²·|r|/(2 R_{S²}²)·(1+…)
  (lowest monopole harmonic j = |r|/2: eigenvalue j(j+1) − r²/4 = |r|/2 at
  leading order) — √|r|, not linear. Linearity in |r| holds near the D7 end
  (momentum regime) and must SURVIVE deep collapse for the emergence
  reading to be exact; nothing protects it in this bosonic family. Sharp
  statement: **both views are suitable; the collapse view is a theorem of
  the family, the emergence view is Witten's reading minus the BPS
  protection — its missing ingredient is a protected linear tower, and
  finding (or excluding) a protection mechanism here is a well-posed open
  problem.** (Failure mode 2 of the inherited tower test is exactly a
  √|r| tower whose gap closes too slowly relative to charge.)
- The gauge sector matches across the readings. In IIA → M the RR
  graviphoton ENTERS from strong coupling as R₁₁ grows (11D inertia:
  1/g² ∝ R₁₁³); our U(1)_{T₃} EXITS to strong coupling under collapse
  (§4). Same mechanism, opposite orientation — Witten's case is the
  existence proof that the strong-coupling end of the coupling exit is
  physical rather than pathological.
- Frame-dependence of the criticality: from D7 the endpoint is a smooth
  infinite-distance limit of a fixed theory; from D6 it is the nucleation
  of a new dimension. One transition, read from the ordered or the
  disordered side — consistent with §5's Mexican-hat discipline (the
  qualitative event sits at the endpoint in both readings).
- Status: derived (the √|r| vs |r|/R scalings and the coupling matching);
  open (the protection mechanism).

## 6. Counterargument pass

1. *"A Berger collapse is a smooth family; calling its endpoint 'critical'
   is rhetoric."* The endpoint fails every smooth-family property the
   interior has: the dimension drops, the isometry group jumps, infinitely
   many KK states degenerate (gap → 0), and the moduli distance is
   infinite. Those are the standard operational signatures of a critical
   point in the tower-test sense; the language is earned.
2. *"The U(1) coupling divergence may be an artifact of the volume
   normalization."* The RATIO 1/g²_{T₃} : 1/g²_W ∝ x_∥ : x_⊥ → 0 is
   normalization-free; however the absolute 4D couplings also feel V's
   x_∥-dependence — stated; the two-exit assignment only uses the ratio
   plus the masslessness of the T₃ boson (exact isometry), which is
   normalization-independent.
3. *"The quintet might be tachyonic or stabilized — without V this is
   kinematics."* Correct and intended: this note derives the MAP of the
   transition (order parameter, charges, exits); the potential's shape on
   the quintet direction is the named open target (§5). The Einstein-point
   facts are cited where known.
4. *"The 9/10/11 numerology imports string conclusions without string
   inputs."* Only the test criterion is imported (and it is stated
   abstractly: tower + closing gap + geometric label); every checked
   ingredient is computed on X_{1,1} itself.

## 7. Kill criteria

- A demonstration that the axis-squash family's curvature blows up at
  finite x_∥ (would break the collapse picture; Berger-type fibres are the
  standard counterexample-free case).
- A computation of the reduced quadratic action giving the T₃-tower a gap
  that does NOT close as the circle is restored (would fail the tower test
  and kill the 10↔11 reading — the tower-test note's failure mode 2).
- For §3: any fibre harmonic whose collapsed limit fails r = 2I₃.

## Sources

- T2 (metric family, Einstein points), N9 (alternation), N11 (slot
  separation), check E Q4 (charge-to-flux; session transcript).
- prior-notes/MTheory_Style_Tower_Test_For_Extra_Dimension.md (criterion,
  benchmark scalings, failure modes).
- docs/SourceDigest_Witten_MTheory_Jump_arXiv.md (hep-th/9503124 benchmark;
  hep-th/9512219 boundary/defect lesson).
- prior-notes/Bosonic_Potential_Stabilization_System.md (t-axis potential
  data for §5).
- prior-out/D6_FERMION_BRIDGE.md, TRANSITION_1D3D_5D7D.md (ladder
  definitions; the r-twist this note identifies as eaten T₃ charge).
