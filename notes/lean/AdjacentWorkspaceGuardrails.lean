/-!
Lean-style notes for the parent-workspace pass.

These notes record obligations learned from adjacent projects in `..`.
They are research memory and stay outside compilation.
-/

namespace DeVries.AdjacentWorkspace

/- Parent source-note protocol. -/
structure ParentSourceNote where
  path : String
  sourceNoteProvenance : Prop
  primaryUpgradeRequired : Prop
  validAsGuardrail : Prop
  validAsTheoremTarget : Prop
  calculationPhaseDeferred : Prop

def parentSourceNoteProtocol (P : ParentSourceNote) : Prop :=
  P.sourceNoteProvenance ∧
  P.primaryUpgradeRequired ∧
  P.validAsGuardrail ∧
  P.validAsTheoremTarget ∧
  P.calculationPhaseDeferred

axiom parent_workspace_protocol_required :
  ∀ P : ParentSourceNote, parentSourceNoteProtocol P

/- Gauge-Higgs assignment guardrail from ../weak/criticism.md. -/
structure GaugeHiggsMassMap where
  sourceOperator : Type
  fieldBasis : Type
  gaugeHiggsMassMatrix : Prop
  transversePoleSelfEnergyMap : Prop
  orderedSamplingRule : Prop
  schemeControl : Prop

def WZAssignmentDerived (M : GaugeHiggsMassMap) : Prop :=
  M.gaugeHiggsMassMatrix ∧
  M.transversePoleSelfEnergyMap ∧
  M.orderedSamplingRule ∧
  M.schemeControl

axiom scalar_seed_quotient_requires_mass_map :
  ∃ M : GaugeHiggsMassMap, WZAssignmentDerived M

/- Single-source DeVries block normalization. -/
structure DeVriesBlockSource where
  sourceOperator : Type
  fieldBasis : Type
  innerProduct : Type
  Sigma_hh_zero : Prop
  Sigma_aa_equals_J : Prop
  offDiagonalProduct_equals_J : Prop
  commonNormalizationRule : Prop

def blockFromOneSourceOperator (B : DeVriesBlockSource) : Prop :=
  B.Sigma_hh_zero ∧
  B.Sigma_aa_equals_J ∧
  B.offDiagonalProduct_equals_J ∧
  B.commonNormalizationRule

axiom endpoint_interval_brane_G2_routes_need_one_source_operator :
  ∃ B : DeVriesBlockSource, blockFromOneSourceOperator B

/- Negative-sector EFT target from the signed-root project.
   V_eff contains c_Y g'^2 (H^dag H) sigma_3 for a two-state Psi_- sector.
   The Wilson coefficient and field identity are UV matching data. -/
structure NegativeSectorEFT where
  PsiMinus : Type
  scalarFunctional : Type
  cY : Type
  gaugeInvariantOperator : Prop
  coefficientMatchedByUV : Prop
  fieldIdentityMatchedByUV : Prop
  poleBranchMap : Prop

def negativeSectorEFTDerived (E : NegativeSectorEFT) : Prop :=
  E.gaugeInvariantOperator ∧
  E.coefficientMatchedByUV ∧
  E.fieldIdentityMatchedByUV ∧
  E.poleBranchMap

axiom negative_branch_EFT_requires_UV_matching :
  ∃ E : NegativeSectorEFT, negativeSectorEFTDerived E

/- Custodial single-generator obstruction.
   Hypercharge gauges T_R^3; C_F/C_A uses the full SU(2) Casimir.
   The proof target is the extra threshold, charge lattice, or generator sum. -/
structure CustodialSingleGeneratorObstruction where
  usualHiggsHypercharge : Prop
  hyperchargeSpurionTR3 : Prop
  vectorSplitting_gprime_v : Prop
  singleGeneratorFactors : Prop
  fullCasimirRatioTarget : Prop
  extraMatchingDatum : Prop

def custodialSingleGeneratorResolved
    (C : CustodialSingleGeneratorObstruction) : Prop :=
  C.usualHiggsHypercharge ∧
  C.hyperchargeSpurionTR3 ∧
  C.vectorSplitting_gprime_v ∧
  C.singleGeneratorFactors ∧
  C.fullCasimirRatioTarget ∧
  C.extraMatchingDatum

axiom custodial_single_generator_obstruction_requires_matching :
  ∃ C : CustodialSingleGeneratorObstruction,
    custodialSingleGeneratorResolved C

/- String and Regge source-arena guardrails. -/
structure StringReggeRoute where
  sourceTheory : Type
  bareKernel : Type
  fourDimensionalEffectiveAction : Type
  chanPatonOrHyperchargeData : Prop
  reggeCasimirData : Prop
  coefficientDerivation : Prop
  branchStatusRule : Prop
  polePlacementRule : Prop

def stringReggeRouteReady (R : StringReggeRoute) : Prop :=
  R.chanPatonOrHyperchargeData ∧
  R.reggeCasimirData ∧
  R.coefficientDerivation ∧
  R.branchStatusRule ∧
  R.polePlacementRule

axiom string_regge_route_requires_coefficient_and_pole_map :
  ∃ R : StringReggeRoute, stringReggeRouteReady R

/- SO(32) flavor boundary. -/
structure SO32FlavorBoundary where
  adjointTripletBranch : Prop
  spinorDoubletBranch : Prop
  orientifoldOrOrbifoldProjectionData : Prop
  couplingToElectroweakOperator : Prop
  generationTopologyCaveat : Prop

def SO32FlavorBoundaryReady (F : SO32FlavorBoundary) : Prop :=
  F.adjointTripletBranch ∧
  F.spinorDoubletBranch ∧
  F.orientifoldOrOrbifoldProjectionData ∧
  F.couplingToElectroweakOperator ∧
  F.generationTopologyCaveat

axiom SO32_flavor_requires_boundary_and_coupling_data :
  ∃ F : SO32FlavorBoundary, SO32FlavorBoundaryReady F

/- Dimensional interpolation provenance from ../phys3. -/
structure ParentDimensionalInterpolation where
  D11ChiralityObstructionSourceTrail : Prop
  D9D11ElectroweakInterpolationNote : Prop
  Witten1981PrimaryControl : Prop
  sixDimensionalInteriorKernel : Prop
  colourless321Account : Prop

def parentDimensionalInterpolationReady
    (I : ParentDimensionalInterpolation) : Prop :=
  I.D11ChiralityObstructionSourceTrail ∧
  I.D9D11ElectroweakInterpolationNote ∧
  I.Witten1981PrimaryControl ∧
  I.sixDimensionalInteriorKernel ∧
  I.colourless321Account

axiom parent_dimensional_interpolation_requires_primary_control :
  ∃ I : ParentDimensionalInterpolation, parentDimensionalInterpolationReady I

end DeVries.AdjacentWorkspace
