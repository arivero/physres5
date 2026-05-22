/-!
Loop 34 parent-directory source note.

This Lean-style file is research memory and sits outside Lean compilation.
It records valid imports from the direct read of `..` during the O4
source-kernel loop.
-/

namespace DeVries.ParentDirectoryLoop34

inductive ParentCluster where
  | prTalks
  | weak
  | physres6
  | phys4
  | phys3
  | signedDvCustodial
  | dualsm
  | futureQueue
  deriving Repr

structure ParentReadProtocol where
  credentialsOutsideClaims : Prop
  runtimeCachesOutsideClaims : Prop
  generatedLogsOutsideClaims : Prop
  pdfsRemainSourceObjects : Prop
  textExtractionAccessAid : Prop
  projectSourcesAreProvenance : Prop
  primarySourceUpgradeRequired : Prop

def parentReadProtocolValid (P : ParentReadProtocol) : Prop :=
  P.credentialsOutsideClaims ∧
  P.runtimeCachesOutsideClaims ∧
  P.generatedLogsOutsideClaims ∧
  P.pdfsRemainSourceObjects ∧
  P.textExtractionAccessAid ∧
  P.projectSourcesAreProvenance ∧
  P.primarySourceUpgradeRequired

axiom loop34_parent_read_protocol :
  ∃ P : ParentReadProtocol, parentReadProtocolValid P

structure O4CHMSourcePackage where
  interval : Type
  gaugeCoupling : Type
  dtnKernel : Type
  braneKernel : Type
  chmInnerProduct : Type
  photonProjector : Type
  currentProjector : Type
  referenceKernel : Type
  sourceScale : Type
  poleMap : Type
  photonZeroFixed : Prop
  currentEntryTarget : Prop
  sameSourceScaleForJHAndJadj : Prop
  sourceToPoleRequired : Prop

def chmCurrentEntryTheoremTarget (D : O4CHMSourcePackage) : Prop :=
  D.photonZeroFixed ∧
  D.currentEntryTarget ∧
  D.sameSourceScaleForJHAndJadj ∧
  D.sourceToPoleRequired

axiom loop34_chm_current_entry_target :
  ∃ D : O4CHMSourcePackage, chmCurrentEntryTheoremTarget D

structure WeakFailureModes where
  hosotaniWeightSquared : Prop
  singleGeneratorMatrixElement : Prop
  wignerEckartDoubletFailure : Prop
  wignerEckartTripletMismatch : Prop
  freeWilsonCoefficientWarning : Prop
  oneOperatorBasisInnerProductRequired : Prop

def weakGuardrailValid (W : WeakFailureModes) : Prop :=
  W.hosotaniWeightSquared ∧
  W.singleGeneratorMatrixElement ∧
  W.wignerEckartDoubletFailure ∧
  W.wignerEckartTripletMismatch ∧
  W.freeWilsonCoefficientWarning ∧
  W.oneOperatorBasisInnerProductRequired

axiom loop34_weak_guardrail :
  ∃ W : WeakFailureModes, weakGuardrailValid W

structure KKFixingImport where
  positiveBranchGaugeSpectrum : Prop
  negativeBranchModulusFixer : Prop
  hodgeSquareRootCandidate : Prop
  gaugeZeroCandidate : Prop
  diagonalMinusJOpen : Prop
  commonSourceVariableRequired : Prop

def kkFixingObligation (K : KKFixingImport) : Prop :=
  K.positiveBranchGaugeSpectrum ∧
  K.negativeBranchModulusFixer ∧
  K.hodgeSquareRootCandidate ∧
  K.gaugeZeroCandidate ∧
  K.diagonalMinusJOpen ∧
  K.commonSourceVariableRequired

axiom loop34_kk_fixing_import :
  ∃ K : KKFixingImport, kkFixingObligation K

structure BranchInvolutionTarget where
  xPlusTimesXMinus : Prop
  involutionSwapsBranches : Prop
  sourceDualityIdentificationRequired : Prop
  algebraicStatusAllowed : Prop

def branchInvolutionObligation (B : BranchInvolutionTarget) : Prop :=
  B.xPlusTimesXMinus ∧
  B.involutionSwapsBranches ∧
  B.sourceDualityIdentificationRequired ∧
  B.algebraicStatusAllowed

axiom loop34_branch_involution_import :
  ∃ B : BranchInvolutionTarget, branchInvolutionObligation B

structure BraneTopImport where
  chanPatonMatrixArena : Prop
  hananyWittenSourceQueue : Prop
  mTheoryLiftSourceQueue : Prop
  topAsGlobalMatchingDatum : Prop
  numericalTopClaimsDeferred : Prop

def braneTopImportValid (B : BraneTopImport) : Prop :=
  B.chanPatonMatrixArena ∧
  B.hananyWittenSourceQueue ∧
  B.mTheoryLiftSourceQueue ∧
  B.topAsGlobalMatchingDatum ∧
  B.numericalTopClaimsDeferred

axiom loop34_brane_top_import :
  ∃ B : BraneTopImport, braneTopImportValid B

end DeVries.ParentDirectoryLoop34
