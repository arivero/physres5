/-!
Lean-style notes for the O17 electromagnetic endpoint target.

These notes are not compiled.  They record the obligations that must be
derived before the alpha route can enter the manuscript as physics.
-/

namespace DeVries.AlphaEndpoint

structure SecularBranchData where
  JH : Type
  Jv : Type
  xPlus : Type -> Type
  xMinusAbs : Type -> Type
  sDeV : Type

structure ScalarVectorNormalization where
  mu : Type
  Cv : Type
  Cw : Type
  vacuumBranchNormalization : Prop
  chargedVectorNormalization : Prop
  commonScale : Prop
  gaugeInvariantScalarFunctional : Prop

def scalarVectorNormalizationReady
    (N : ScalarVectorNormalization) : Prop :=
  N.vacuumBranchNormalization ∧
  N.chargedVectorNormalization ∧
  N.commonScale ∧
  N.gaugeInvariantScalarFunctional

axiom alpha_route_requires_scalar_vector_normalization :
  ∃ N : ScalarVectorNormalization, scalarVectorNormalizationReady N

structure ElectromagneticEndpoint where
  compactBase : Type
  u1emGenerator : Type
  chargeLattice : Type
  compactMetric : Type
  wavefunction : Type
  kineticTermDerived : Prop
  generatorNormalizationFixed : Prop
  chargeNormalizationFixed : Prop
  endpointIdentifiedAsU1em : Prop

def electromagneticEndpointReady (E : ElectromagneticEndpoint) : Prop :=
  E.kineticTermDerived ∧
  E.generatorNormalizationFixed ∧
  E.chargeNormalizationFixed ∧
  E.endpointIdentifiedAsU1em

axiom D9_endpoint_requires_U1em_kinetic_normalization :
  ∃ E : ElectromagneticEndpoint, electromagneticEndpointReady E

structure AlphaMatching where
  observable : Type
  scheme : Type
  Qalpha : Type
  thresholdPrescription : Type
  deltaAlphaMatch : Type
  runningConventionSpecified : Prop
  hadronicVacuumPolarizationControlled : Prop
  thresholdDataSourceAudited : Prop
  poleWeakAngleMatchedToCouplingAngle : Prop

def alphaMatchingReady (M : AlphaMatching) : Prop :=
  M.runningConventionSpecified ∧
  M.hadronicVacuumPolarizationControlled ∧
  M.thresholdDataSourceAudited ∧
  M.poleWeakAngleMatchedToCouplingAngle

axiom alpha_endpoint_requires_matching_data :
  ∃ M : AlphaMatching, alphaMatchingReady M

structure AlphaEndpointTheorem where
  branchData : SecularBranchData
  normalization : ScalarVectorNormalization
  endpoint : ElectromagneticEndpoint
  matching : AlphaMatching
  sourceKernelDerived : Prop
  orderedAssignmentDerived : Prop
  negativeBranchScalarMapDerived : Prop
  dimensionalEndpointDerived : Prop

def alphaEndpointTheoremReady (T : AlphaEndpointTheorem) : Prop :=
  T.sourceKernelDerived ∧
  T.orderedAssignmentDerived ∧
  T.negativeBranchScalarMapDerived ∧
  T.dimensionalEndpointDerived ∧
  scalarVectorNormalizationReady T.normalization ∧
  electromagneticEndpointReady T.endpoint ∧
  alphaMatchingReady T.matching

axiom O17_has_conditional_theorem_status :
  ∃ T : AlphaEndpointTheorem, alphaEndpointTheoremReady T

end DeVries.AlphaEndpoint
