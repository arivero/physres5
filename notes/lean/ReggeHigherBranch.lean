/-!
Lean-style obligations for O18.

These notes are research memory and are not compiled.
-/

namespace DeVries.ReggeHigherBranch

structure ReggeInterceptTower where
  SectorLabel : Type
  OscillatorLevel : Type
  PhysicalSpinLabel : Type
  alphaPrime : Type
  sectorCasimir_Aj : SectorLabel -> Type
  commonSlope : Prop
  devriesKernelDerived : Prop
  sectorLabelSeparatedFromPhysicalSpin : Prop
  projectionRuleDerived : Prop
  negativeBranchStatusRule : Prop

def reggeTowerAcceptable (T : ReggeInterceptTower) : Prop :=
  T.commonSlope ∧
  T.devriesKernelDerived ∧
  T.sectorLabelSeparatedFromPhysicalSpin ∧
  T.projectionRuleDerived ∧
  T.negativeBranchStatusRule

constant targetVIII_candidate : ReggeInterceptTower

def targetVIII_obligations : Prop :=
  reggeTowerAcceptable targetVIII_candidate

structure HigherPositiveSlot where
  sector_j_three_halves : Type
  positiveInterceptSurvives : Prop
  gaugeRepresentationAssigned : Prop
  anomalyLedgerComplete : Prop
  massGenerationDerived : Prop
  productionChannelDerived : Prop
  decayChannelDerived : Prop
  widthDerived : Prop
  colliderSourcesAudited : Prop

def higherSlotPhenomenologyReady (H : HigherPositiveSlot) : Prop :=
  H.positiveInterceptSurvives ∧
  H.gaugeRepresentationAssigned ∧
  H.anomalyLedgerComplete ∧
  H.massGenerationDerived ∧
  H.productionChannelDerived ∧
  H.decayChannelDerived ∧
  H.widthDerived ∧
  H.colliderSourcesAudited

constant j_three_halves_candidate : HigherPositiveSlot

def j_three_halves_assignment_obligations : Prop :=
  higherSlotPhenomenologyReady j_three_halves_candidate

end DeVries.ReggeHigherBranch
