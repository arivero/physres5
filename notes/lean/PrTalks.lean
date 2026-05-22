/-!
Lean-style notes for the adjacent `../prTalks` PDFs.

These notes are research memory. They are kept outside compilation.
The PDFs remain the source objects; text extraction is an access aid.
Formulas marked `agentVisualRead` were transcribed from the rendered PDF view
because OCR can lose radicals, plots, and equation layout.
-/

namespace DeVries.PrTalks

/- PDF source discipline. -/
structure PdfSource where
  path : String
  pages : Nat
  textExtractionAid : Prop
  pdfRemainsSourceObject : Prop
  agentVisualRead : Prop
  primaryLiteratureUpgradeRequired : Prop

def prTalksPdfProtocol (P : PdfSource) : Prop :=
  P.textExtractionAid ∧
  P.pdfRemainsSourceObject ∧
  P.primaryLiteratureUpgradeRequired

axiom pdf_source_protocol_required :
  ∀ P : PdfSource, prTalksPdfProtocol P

/- Electroweak ray: radial Higgs scale plus projective DeVries datum. -/
structure ElectroweakRaySourceNote where
  radialOrderParameter : Type
  projectiveAngleDatum : Type
  photonMasslessAlongRay : Prop
  wMassAlongRay : Prop
  zMassAlongRay : Prop
  orderedSamplingOpen : Prop

def electroweakRayObligation (R : ElectroweakRaySourceNote) : Prop :=
  R.photonMasslessAlongRay ∧
  R.wMassAlongRay ∧
  R.zMassAlongRay ∧
  R.orderedSamplingOpen

axiom prtalks_electroweak_ray_promotes_assignment_obligation :
  ∃ R : ElectroweakRaySourceNote, electroweakRayObligation R

/- Orbit quadratic source note. -/
structure OrbitQuadratic where
  beta : Type
  spinLabel : Type
  landePauliReplacement : Prop
  betaEquation : Prop
  devriesQuadratic : Prop
  sameRadiusMassRatioQuestion : Prop

def orbitQuadraticGivesSameAlgebra (O : OrbitQuadratic) : Prop :=
  O.landePauliReplacement ∧
  O.betaEquation ∧
  O.devriesQuadratic ∧
  O.sameRadiusMassRatioQuestion

axiom orbit_note_requires_physical_identification :
  ∃ O : OrbitQuadratic, orbitQuadraticGivesSameAlgebra O

/- Regge alternatives extracted from the adjacent PDFs. -/
inductive ReggeReading where
  | interceptTower
  | productInvariant

structure ReggeizationProblem where
  reading : ReggeReading
  sectorLabel_j : Type
  oscillator_n : Type
  alphaPrime : Type
  positiveRootIntercept : Prop
  negativeRootInterceptOrPartner : Prop
  commonSlope : Prop
  worldsheetOriginRequired : Prop
  tachyonBranchRuleRequired : Prop
  survivesProjection_j_three_halves : Prop

def interceptReggeization (P : ReggeizationProblem) : Prop :=
  P.reading = ReggeReading.interceptTower ∧
  P.positiveRootIntercept ∧
  P.negativeRootInterceptOrPartner ∧
  P.commonSlope ∧
  P.worldsheetOriginRequired ∧
  P.survivesProjection_j_three_halves

def productInvariantReggeization (P : ReggeizationProblem) : Prop :=
  P.reading = ReggeReading.productInvariant ∧
  P.positiveRootIntercept ∧
  P.negativeRootInterceptOrPartner ∧
  P.worldsheetOriginRequired

axiom prtalks_regge_intercept_obligation :
  ∃ P : ReggeizationProblem, interceptReggeization P

axiom prtalks_regge_product_obligation :
  ∃ P : ReggeizationProblem, productInvariantReggeization P

/- Agent visual read from `cosas alex`, page 35 and page 50:
   D_T = [[0, a sqrt(S_T)], [a sqrt(S_T), -b S_T]]
   S_T = T(T+1)
   eigenvalues = (-b S_T +/- sqrt(b^2 S_T^2 + 4 a^2 S_T))/2
   DeVries normalization: a^2=b and a=b=1.
-/
structure MinimalTwoChannelBlock where
  representationLabel : Type
  ST : Type
  offDiagonalSqrtCasimir : Prop
  diagonalMinusCasimir : Prop
  positiveBranchLimit : Prop
  normalizationCondition : Prop
  derivationFromSourceOperatorRequired : Prop

def minimalBlockMatchesDeVriesTarget (B : MinimalTwoChannelBlock) : Prop :=
  B.offDiagonalSqrtCasimir ∧
  B.diagonalMinusCasimir ∧
  B.positiveBranchLimit ∧
  B.normalizationCondition ∧
  B.derivationFromSourceOperatorRequired

axiom prtalks_minimal_block_is_theorem_target :
  ∃ B : MinimalTwoChannelBlock, minimalBlockMatchesDeVriesTarget B

/- Representation-channel reading:
   H has T=1/2, H^dagger sigma^a H has T=1,
   observed W and Z remain Lorentz spin one.
-/
structure RepresentationChannelReading where
  higgsDoubletChannel : Prop
  adjointCurrentChannel : Prop
  observedVectorBosonsSpinOne : Prop
  orderedChargedNeutralSamplingOpen : Prop

def representationReadingObligation (R : RepresentationChannelReading) : Prop :=
  R.higgsDoubletChannel ∧
  R.adjointCurrentChannel ∧
  R.observedVectorBosonsSpinOne ∧
  R.orderedChargedNeutralSamplingOpen

axiom prtalks_representation_channel_reading_required :
  ∃ R : RepresentationChannelReading, representationReadingObligation R

/- Dimensional interpolation note. -/
structure EffectiveDimensionInterpolation where
  rho : Type
  radiusOne : Type
  radiusTwo : Type
  chiOne : Prop
  chiTwo : Prop
  deff9to10to11 : Prop
  fullGaugeKK765 : Prop
  colourSpectatorKK321 : Prop
  K7_unbrokenStandardModel : Prop
  K6_interfacePackage : Prop
  K5_brokenVisibleEndpoint : Prop
  activeElectroweakChannel321 : Prop
  geometricU1Endpoint : Prop
  electromagneticEmbeddingRequired : Prop
  vectorScalarLaplacianBlockRequired : Prop
  chiralityAndSingularityAccountRequired : Prop

def interpolationObligation (I : EffectiveDimensionInterpolation) : Prop :=
  I.chiOne ∧
  I.chiTwo ∧
  I.deff9to10to11 ∧
  I.fullGaugeKK765 ∧
  I.colourSpectatorKK321 ∧
  I.K7_unbrokenStandardModel ∧
  I.K6_interfacePackage ∧
  I.K5_brokenVisibleEndpoint ∧
  I.activeElectroweakChannel321 ∧
  I.geometricU1Endpoint ∧
  I.electromagneticEmbeddingRequired ∧
  I.vectorScalarLaplacianBlockRequired ∧
  I.chiralityAndSingularityAccountRequired

axiom prtalks_dimensional_interpolation_requires_primary_source_upgrade :
  ∃ I : EffectiveDimensionInterpolation, interpolationObligation I

/- Negative branch and top-sector obligation. -/
inductive NegativeBranchRole where
  | scalarFunctional
  | yukawaSectorFunctional
  | boundaryDatum
  | compactificationDatum
  | auxiliaryPartner

structure NegativeBranchProgram where
  role : NegativeBranchRole
  gaugeInvariantMapRequired : Prop
  topScaleAccountRequired : Prop
  commonSourceVariableRequired : Prop
  topYukawaMapRequired : Prop
  topSelfEnergyMapRequired : Prop
  numericalProximityDeferred : Prop
  calculationPhaseRequired : Prop

def negativeBranchPrTalksObligation (N : NegativeBranchProgram) : Prop :=
  N.gaugeInvariantMapRequired ∧
  N.topScaleAccountRequired ∧
  N.commonSourceVariableRequired ∧
  N.topYukawaMapRequired ∧
  N.topSelfEnergyMapRequired ∧
  N.numericalProximityDeferred ∧
  N.calculationPhaseRequired

axiom prtalks_negative_branch_top_obligation :
  ∃ N : NegativeBranchProgram, negativeBranchPrTalksObligation N

end DeVries.PrTalks
