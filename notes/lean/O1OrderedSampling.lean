/-!
Loop 33 note to self: O1 ordered W/Z sampling package.

This is a Lean-style research note.  It is kept outside Lean compilation.
The goal is to trigger expert review of the same-source projection theorem.
-/

namespace DeVries.O1OrderedSampling

constant SourceVariable : Type
constant HilbertSpaceJ : Type
constant InnerProduct : Type
constant SourceScale : Type
constant PoleMap : Type
constant ScalarFunctional : Type
constant ChargedSample : Type
constant NeutralSample : Type
constant PhotonSample : Type
constant Remainder : Type
constant IntervalSourceDatum : Type
constant BoundaryKernel : Type
constant PhotonProjector : Type
constant NormalizedKernel : Type
constant CouplingRay : Type
constant BoundarySuperconnectionDatum : Type
constant SuperconnectionProjector : Type
constant NeutralTraceSpace : Type
constant HyperchargeRemainder : Type
constant GoldstoneVectorMixing : Type

constant J_H : Real
constant J_adj : Real
constant J_gamma : Real

structure O1SourcePackage where
  uEW : SourceVariable
  HJ : HilbertSpaceJ
  innerProduct : InnerProduct
  LambdaJ : SourceScale
  poleMap : PoleMap
  scalarFunctional : ScalarFunctional
  hJ : ChargedSample
  aJ_gamma_perp : NeutralSample
  aGamma : PhotonSample
  P_W_assigns_Higgs_doublet : J_H = (3 / 4 : Real)
  P_Z_assigns_adjoint_current : J_adj = (2 : Real)
  P_gamma_assigns_null : J_gamma = (0 : Real)
  same_basis_for_h_and_a : Prop
  same_scale_for_JH_and_Jadj : Prop
  photon_reference_subtraction_fixed : Prop
  gamma_perp_projection_defined : Prop
  source_to_pole_remainder_derived : Prop
  negative_branch_same_source : Prop

def O1TargetReady (P : O1SourcePackage) : Prop :=
  P.same_basis_for_h_and_a ∧
  P.same_scale_for_JH_and_Jadj ∧
  P.photon_reference_subtraction_fixed ∧
  P.gamma_perp_projection_defined ∧
  P.source_to_pole_remainder_derived ∧
  P.negative_branch_same_source

axiom ordered_sampling_open_obligation :
  ∃ P : O1SourcePackage, O1TargetReady P

structure O1O10BoundaryKernelDiagram where
  uint : IntervalSourceDatum
  KT_DtN : BoundaryKernel
  KT_brane : BoundaryKernel
  photonProjector : PhotonProjector
  innerProduct : InnerProduct
  normalizedKernel : NormalizedKernel
  couplingRay : CouplingRay
  chargedProjector : ChargedSample
  neutralProjector : NeutralSample
  photonSample : PhotonSample
  sourceScale : SourceScale
  poleMap : PoleMap
  remainder : Remainder
  oneSourceControlsBoundaryKernel : Prop
  oneSourceControlsRay : Prop
  photonSubtractionDefined : Prop
  sharedNormalization : Prop
  poleRemainderDerived : Prop

def boundaryKernelDiagramReady (D : O1O10BoundaryKernelDiagram) : Prop :=
  D.oneSourceControlsBoundaryKernel ∧
  D.oneSourceControlsRay ∧
  D.photonSubtractionDefined ∧
  D.sharedNormalization ∧
  D.poleRemainderDerived

axiom loop37_o1_o10_boundary_kernel_obligation :
  ∃ D : O1O10BoundaryKernelDiagram, boundaryKernelDiagramReady D

structure ScIntO1Closure where
  uintsc : BoundarySuperconnectionDatum
  Psc : SuperconnectionProjector
  photonProjector : PhotonProjector
  sourceScale : SourceScale
  poleMap : PoleMap
  chargedProjector : ChargedSample
  neutralProjector : NeutralSample
  scalarFunctional : ScalarFunctional
  oddHiggsAssigned : J_H = (3 / 4 : Real)
  evenCurrentAssigned : J_adj = (2 : Real)
  photonNullAssigned : J_gamma = (0 : Real)
  oneSourceInnerProduct : Prop
  oneSourceScale : Prop
  complexPoleRemainderDerived : Prop

def scIntO1ClosureReady (S : ScIntO1Closure) : Prop :=
  S.oneSourceInnerProduct ∧ S.oneSourceScale ∧ S.complexPoleRemainderDerived

axiom loop40_sc_int_o1_closure :
  ∃ S : ScIntO1Closure, scIntO1ClosureReady S

structure Loop42WardProjectedNeutralTarget where
  neutralTraceSpace : NeutralTraceSpace
  photonProjector : PhotonProjector
  hyperchargeRemainder : HyperchargeRemainder
  goldstoneVectorMixing : GoldstoneVectorMixing
  chargedProjector : ChargedSample
  neutralProjector : NeutralSample
  photonSample : PhotonSample
  neutralProductShared : Prop
  gammaPerpProjectionDefined : Prop
  hyperchargeRemainderDerived : Prop
  chargedInsertionFromGoldstoneMixing : Prop
  sameSourceAsCHMCurrentEntry : Prop
  samePoleMap : Prop

def loop42WardProjectedNeutralReady
  (T : Loop42WardProjectedNeutralTarget) : Prop :=
  T.neutralProductShared ∧
  T.gammaPerpProjectionDefined ∧
  T.hyperchargeRemainderDerived ∧
  T.chargedInsertionFromGoldstoneMixing ∧
  T.sameSourceAsCHMCurrentEntry ∧
  T.samePoleMap

axiom loop42_ward_projected_neutral_obligation :
  ∃ T : Loop42WardProjectedNeutralTarget,
    loop42WardProjectedNeutralReady T

/- CHM ledger target:
   h_J = P_h,J(pi_i, A_5, delta v_i, delta R, alpha_H)
   a_J^{gamma_perp} = P_a,J^{gamma_perp} A_mu^{T,boundary}
   a_gamma = P_gamma A_mu^{T,boundary}

   Target:
   I_hat_h,J_H^CHM = 3/4
   Sigma_hat_aa,J_adj^CHM = 2

   The same Lambda_CHM and CHM product must serve both rows before
   M_W,pole^2 / M_Z,pole^2 =
     x_+(J_H) / x_+(J_adj) + Delta_O1
   has source-theory content.
-/

end DeVries.O1OrderedSampling
