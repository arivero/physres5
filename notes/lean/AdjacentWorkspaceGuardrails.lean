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

/- Broad `..` inventory pass from Loop 12.
   The parent workspace contains many projects and runtime directories.
   Only source-note provenance, theorem targets, and critique guardrails enter
   this manuscript. -/
structure ParentRootInventory where
  prTalksIndexed : Prop
  hansSignedDeVriesIndexed : Prop
  weakCritiqueIndexed : Prop
  phys3DimensionalProvenanceIndexed : Prop
  phys4RequiresTargetedAudit : Prop
  unrelatedRuntimeStateExcluded : Prop
  privateOrSecurityFilesExcluded : Prop
  primarySourceUpgradeRequired : Prop
  loop20VisibleQueuesCatalogued : Prop
  chmRemainsActiveIntervalSource : Prop

def parentRootInventoryReady (I : ParentRootInventory) : Prop :=
  I.prTalksIndexed ∧
  I.hansSignedDeVriesIndexed ∧
  I.weakCritiqueIndexed ∧
  I.phys3DimensionalProvenanceIndexed ∧
  I.phys4RequiresTargetedAudit ∧
  I.unrelatedRuntimeStateExcluded ∧
  I.privateOrSecurityFilesExcluded ∧
  I.primarySourceUpgradeRequired ∧
  I.loop20VisibleQueuesCatalogued ∧
  I.chmRemainsActiveIntervalSource

axiom parent_root_inventory_requires_triage :
  ∃ I : ParentRootInventory, parentRootInventoryReady I

/- Gauge-Higgs assignment guardrail from ../physres5lineage/weak/criticism.md. -/
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

/- Targeted parent audit from Loop 14. -/
structure PhysicsForumsWrongTurnProvenance where
  liveThreadAvailable : Prop
  localCatalogueAvailable : Prop
  fiveLightFlavorEndpointIdea : Prop
  topExcludedFlavorProvenance : Prop
  seibergAndBraneMechanismTrail : Prop
  directPostOrPrimarySourceRequired : Prop

def physicsForumsProvenanceReady
    (P : PhysicsForumsWrongTurnProvenance) : Prop :=
  P.liveThreadAvailable ∧
  P.localCatalogueAvailable ∧
  P.fiveLightFlavorEndpointIdea ∧
  P.topExcludedFlavorProvenance ∧
  P.seibergAndBraneMechanismTrail ∧
  P.directPostOrPrimarySourceRequired

axiom wrong_turn_thread_is_provenance_only :
  ∃ P : PhysicsForumsWrongTurnProvenance, physicsForumsProvenanceReady P

/- Distinct traces found across adjacent workspaces. -/
structure TraceSpaceSeparation where
  devriesBranchTrace : Type
  rankOneSeedTrace : Type
  negativeSectorSigmaTrace : Type
  separateNotation : Prop
  commonSourceOperatorRequired : Prop
  coefficientTransferExcludedUntilDerived : Prop

def traceSpacesSeparated (T : TraceSpaceSeparation) : Prop :=
  T.separateNotation ∧
  T.commonSourceOperatorRequired ∧
  T.coefficientTransferExcludedUntilDerived

axiom trace_arguments_require_disjoint_ledgers :
  ∃ T : TraceSpaceSeparation, traceSpacesSeparated T

/- Tested Wigner--Eckart/Clebsch route status. -/
structure WignerEckartRouteStatus where
  naturalParentsTested : Prop
  doubletParentSelectionRuleFailure : Prop
  tripletAxialWrongCasimirDatum : Prop
  alternativeParentOrProjectionRequired : Prop

def wignerEckartRouteClosedForTestedParents
    (W : WignerEckartRouteStatus) : Prop :=
  W.naturalParentsTested ∧
  W.doubletParentSelectionRuleFailure ∧
  W.tripletAxialWrongCasimirDatum ∧
  W.alternativeParentOrProjectionRequired

axiom wigner_eckart_route_is_negative_for_tested_parents :
  ∃ W : WignerEckartRouteStatus,
    wignerEckartRouteClosedForTestedParents W

/- SO(32) flavor-boundary theorem target from parent notes. -/
structure SO32FlavorTheoremTarget where
  vectorSixteenDecomposition : Prop
  exteriorSquareBlock : Prop
  symmetricFifteenFromTensorBlock : Prop
  typeIHeteroticBoundaryArena : Prop
  extraStateProjectionRequired : Prop
  electroweakOperatorCouplingRequired : Prop
  orientifoldTadpoleCompletionRequired : Prop

def SO32FlavorTheoremTargetReady (S : SO32FlavorTheoremTarget) : Prop :=
  S.vectorSixteenDecomposition ∧
  S.exteriorSquareBlock ∧
  S.symmetricFifteenFromTensorBlock ∧
  S.typeIHeteroticBoundaryArena ∧
  S.extraStateProjectionRequired ∧
  S.electroweakOperatorCouplingRequired ∧
  S.orientifoldTadpoleCompletionRequired

axiom SO32_flavor_target_requires_projection_and_coupling :
  ∃ S : SO32FlavorTheoremTarget, SO32FlavorTheoremTargetReady S

/- Brane and top-sector source-upgrade queue. -/
structure BraneTopBoundaryDatum where
  hananyWittenPrimarySource : Prop
  mTheoryD6KKMonopolePrimarySource : Prop
  m5CurvePrimarySource : Prop
  topAsFourthFlavorBoundaryDatum : Prop
  topNegativeBranchLinkDerived : Prop

def braneTopBoundaryDatumReady (B : BraneTopBoundaryDatum) : Prop :=
  B.hananyWittenPrimarySource ∧
  B.mTheoryD6KKMonopolePrimarySource ∧
  B.m5CurvePrimarySource ∧
  B.topAsFourthFlavorBoundaryDatum ∧
  B.topNegativeBranchLinkDerived

axiom top_boundary_datum_requires_separate_branch_map :
  ∃ B : BraneTopBoundaryDatum, braneTopBoundaryDatumReady B

end DeVries.AdjacentWorkspace
