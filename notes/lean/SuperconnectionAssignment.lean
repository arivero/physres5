/-!
Loop 24 note to self: electroweak superconnection assignment for O1.

This is a Lean-style research note.  It is kept outside Lean compilation.
The goal is to trigger expert review of the ordered W/Z assignment.
-/

namespace DeVries.SuperconnectionAssignment

constant GaugeHiggsComplex : Type
constant OddHiggs : Type
constant EvenCurrent : Type
constant PoleScheme : Type
constant InnerProduct : Type
constant MatchingRemainder : Type
constant BoundaryKernelCompatibility : Type
constant AnomalyLedger : Type
constant OmegaOdd : Type
constant EvenAnticommutators : Type
constant PhotonProjection : Type
constant CoquereauxCurvature : Type
constant CoquereauxNormalization : Type
constant CHMDtNKernel : Type
constant CHMBraneKernel : Type
constant PhotonReferenceKernel : Type
constant SourceScale : Type
constant PoleRemainder : Type
constant SuperconnectionHolonomy : Type
constant ScalarHessian : Type

constant Phi_odd : OddHiggs
constant F_even_gamma_perp : EvenCurrent
constant J_H : Real
constant J_adj : Real
constant Delta_sc : MatchingRemainder

structure SuperconnectionReduction where
  complex : GaugeHiggsComplex
  innerProduct : InnerProduct
  poleScheme : PoleScheme
  odd_higgs_channel : OddHiggs
  even_transverse_current : EvenCurrent
  P_W_assigns_doublet : J_H = (3 / 4 : Real)
  P_Z_assigns_adjoint : J_adj = (2 : Real)
  same_complex_supplies_both_maps : Prop
  photon_null_direction_preserved : Prop
  ew_ray_preserved : Prop
  trace_space_separated : Prop
  wigner_eckart_route_excluded : Prop
  so32_flavour_requires_explicit_coupling : Prop
  anomaly_ledger : AnomalyLedger
  anomaly_ledger_consistent : Prop
  chm_boundary_kernel_compatibility : BoundaryKernelCompatibility
  negative_branch_scalar_map_required : Prop
  matching_remainder_derived : Prop

structure CoquereauxProjectionTarget where
  omegaOdd : OmegaOdd
  evenGenerators : EvenAnticommutators
  curvature : CoquereauxCurvature
  normalization : CoquereauxNormalization
  photonProjection : PhotonProjection
  odd_higgs_to_JH : Prop
  even_current_to_Jadj : Prop
  source_internal_weak_angle : String
  pole_quotient_matching_required : Prop

def O1SuperconnectionTarget (S : SuperconnectionReduction) : Prop :=
  S.same_complex_supplies_both_maps ∧
  S.photon_null_direction_preserved ∧
  S.ew_ray_preserved ∧
  S.trace_space_separated ∧
  S.wigner_eckart_route_excluded ∧
  S.so32_flavour_requires_explicit_coupling ∧
  S.anomaly_ledger_consistent ∧
  S.negative_branch_scalar_map_required ∧
  S.matching_remainder_derived

axiom superconnection_assignment_obligation :
  ∃ S : SuperconnectionReduction, O1SuperconnectionTarget S

structure BoundarySuperconnectionIntervalTarget where
  complex : GaugeHiggsComplex
  curvature : CoquereauxCurvature
  dtnKernel : CHMDtNKernel
  braneKernel : CHMBraneKernel
  photonReference : PhotonReferenceKernel
  sourceScale : SourceScale
  poleRemainder : PoleRemainder
  oddHiggsToThreeFourths : Prop
  evenCurrentToTwo : Prop
  photonToZero : Prop
  scalarBranchSameSource : Prop
  hattedKernelEqualsTargetBlock : Prop

def boundarySuperconnectionIntervalReady
  (T : BoundarySuperconnectionIntervalTarget) : Prop :=
  T.oddHiggsToThreeFourths ∧
  T.evenCurrentToTwo ∧
  T.photonToZero ∧
  T.scalarBranchSameSource ∧
  T.hattedKernelEqualsTargetBlock

axiom loop40_boundary_superconnection_interval_obligation :
  ∃ T : BoundarySuperconnectionIntervalTarget,
    boundarySuperconnectionIntervalReady T

structure BoundarySuperconnectionHolonomyTarget where
  intervalTarget : BoundarySuperconnectionIntervalTarget
  Wsc : SuperconnectionHolonomy
  scalarHessian : ScalarHessian
  sameProjectionScaleAndPhotonReference : Prop
  vectorKernelGivesOrderedSamples : Prop
  scalarHessianGivesNegativeBranch : Prop
  complexPoleRemainderDeclared : Prop

def boundarySuperconnectionHolonomyReady
  (T : BoundarySuperconnectionHolonomyTarget) : Prop :=
  T.sameProjectionScaleAndPhotonReference ∧
  T.vectorKernelGivesOrderedSamples ∧
  T.scalarHessianGivesNegativeBranch ∧
  T.complexPoleRemainderDeclared

axiom loop41_boundary_superconnection_holonomy_obligation :
  ∃ T : BoundarySuperconnectionHolonomyTarget,
    boundarySuperconnectionHolonomyReady T

/- Diagram to check in manuscript form:

Phi_odd  --P_W-->  J_H = 3/4
  | D_J + D_J^dagger |
F_even^{gamma^perp} --P_Z--> J_adj = 2

M_W,pole^2 / M_Z,pole^2
  = x_+(J_H) / x_+(J_adj) + Delta_sc.

Acceptance test:
1. source a single electroweak superconnection complex;
2. define the inner product on odd Higgs and even transverse-current data;
3. derive P_W and P_Z from that complex;
4. preserve the electroweak ray and photon zero mode;
5. keep odd-Higgs, even-current, and interval-boundary trace spaces separated
   until a common source operator defines the comparison;
6. record the Wigner--Eckart route as excluded for the tested parents;
7. require an explicit SO(32)-flavour coupling to the electroweak kernel;
8. match the superconnection data to a CHM boundary kernel;
9. derive or compute Delta_sc in the pole scheme;
10. connect the negative eigenvector to a gauge-invariant scalar functional.
11. attach an anomaly ledger for added gauge-Higgs or fermionic channels.
12. audit Coquereaux's Omega matrices, even anticommutators, curvature norm,
    scalar-product freedoms, and source-internal weak-angle value as
    prerequisites for promoting the superconnection beyond an assignment arena.
-/

end DeVries.SuperconnectionAssignment
