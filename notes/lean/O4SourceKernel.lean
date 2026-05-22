/-!
Loop 34 O4 source-kernel theorem notes.

This file is research memory and is kept outside Lean compilation.
It records the entry-by-entry source obligations for the DeVries kernel.
-/

namespace DeVries.O4SourceKernel

constant Interval : Type
constant GaugeCoupling : Type
constant Kernel : Type
constant CHMProduct : Type
constant Projection : Type
constant SourceScale : Type
constant PoleMap : Type
constant LocalOperator : Type
constant Pairing : Type
constant SuperconnectionCurvature : Type
constant OrderedProjectorPackage : Type
constant ADERootLattice : Type
constant SingularSupport : Type
constant HiggsBundleSource : Type
constant CompletionLedger : Type
constant SourceFragmentBindings : Type
constant LocalizedWavefunction : Type
constant LocalizedCurrentMode : Type
constant MorseCriticalData : Type
constant PointMetric : Type
constant FlowKernel : Type
constant BilinearFunctional : Type
constant OrientationConvention : Type
constant RejectionLedger : Type

structure CHMCurrentEntryData where
  interval : Interval
  g5 : GaugeCoupling
  dtnKernel : Kernel
  braneKernel : Kernel
  chmProduct : CHMProduct
  photonProjection : Projection
  currentProjection : Projection
  referenceKernel : Kernel
  sourceScale : SourceScale
  poleMap : PoleMap
  chmEquationAudit : Prop
  photonZeroReference : Prop
  hattedSpectralVariable : Prop
  currentEntryEqualsJ : Prop

def chmCurrentEntryReady (D : CHMCurrentEntryData) : Prop :=
  D.chmEquationAudit ∧
  D.photonZeroReference ∧
  D.hattedSpectralVariable ∧
  D.currentEntryEqualsJ

axiom loop34_chm_current_entry :
  ∃ D : CHMCurrentEntryData, chmCurrentEntryReady D

structure HodgeSquareRootData where
  differential : Type
  adjoint : Type
  zeroFormState : Type
  oneFormState : Type
  innerProduct : Type
  wittenDeformationAudit : Prop
  squareRootEntry : Prop
  breakingDiagonalOpen : Prop
  commonReducedBasis : Prop

def hodgeSquareRootReady (H : HodgeSquareRootData) : Prop :=
  H.wittenDeformationAudit ∧
  H.squareRootEntry ∧
  H.breakingDiagonalOpen ∧
  H.commonReducedBasis

axiom loop34_hodge_square_root_companion :
  ∃ H : HodgeSquareRootData, hodgeSquareRootReady H

structure G2LocalKernelAudit where
  localOperator : LocalOperator
  pairing : Pairing
  higgsBundleEquations : Prop
  currentEntryTarget : Prop
  flowOverlapTarget : Prop
  globalCompletionDeferred : Prop

def g2LocalKernelTarget (G : G2LocalKernelAudit) : Prop :=
  G.higgsBundleEquations ∧
  G.currentEntryTarget ∧
  G.flowOverlapTarget ∧
  G.globalCompletionDeferred

axiom loop34_g2_local_kernel :
  ∃ G : G2LocalKernelAudit, g2LocalKernelTarget G

structure Loop47G2ADEPairingTarget where
  adeRootLattice : ADERootLattice
  singularSupport : SingularSupport
  higgsBundleSource : HiggsBundleSource
  localOperator : LocalOperator
  singularSupportPairing : Pairing
  currentProjection : Projection
  sourceScale : SourceScale
  completionLedger : CompletionLedger
  sourceFragments : SourceFragmentBindings
  higgsBundleEquations :
    -- Phi = sum_i t_i df_i, rho = sum_i t_i rho_i, Delta f_i = rho_i.
    Prop
  matterLocalization :
    -- f_Q = sum_i q_i f_i and df_Q(p) = 0.
    Prop
  a1SubsetA2Enhancement :
    -- ad A2 restricted to A1 x U(1) yields ad A1, singlet, and charged doublets.
    Prop
  currentSlopePositive :
    -- Z_J^G2 = d_{hat lambda} K_J^{G2,cur}(0) > 0.
    Prop
  projectedNormPositive :
    Prop
  currentPairingEqualsJ :
    -- K_J^{G2,cur,can} = hat lambda + Sigma_aa,J^{G2,can} + ...
    -- with Sigma_aa,2^{G2,can} = 2.
    Prop
  flowOverlapDeferred :
    Prop
  ewProjectorsDeferred :
    Prop
  poleMapDeferred :
    Prop
  anomalyGlobalFormDeferred :
    Prop

def loop47G2ADEPairingReady (G : Loop47G2ADEPairingTarget) : Prop :=
  G.higgsBundleEquations ∧
  G.matterLocalization ∧
  G.a1SubsetA2Enhancement ∧
  G.currentSlopePositive ∧
  G.projectedNormPositive ∧
  G.currentPairingEqualsJ ∧
  G.flowOverlapDeferred ∧
  G.ewProjectorsDeferred ∧
  G.poleMapDeferred ∧
  G.anomalyGlobalFormDeferred

axiom loop47_g2_ade_pairing_target_required :
  ∃ G : Loop47G2ADEPairingTarget, loop47G2ADEPairingReady G

structure Loop48G2FlowOverlapTarget where
  localizedOrderParameter : LocalizedWavefunction
  localizedCurrentMode : LocalizedCurrentMode
  morseOrMorseBottCriticalData : MorseCriticalData
  pointMetric : PointMetric
  flowKernel : FlowKernel
  bilinearHA : BilinearFunctional
  bilinearAH : BilinearFunctional
  orientationConvention : OrientationConvention
  sameBasisAsTargetIIIg : Prop
  chargeSectorCompatible : Prop
  pointMetricPositive : Prop
  sourceScaleSharedWithTargetIIIg : Prop
  orientationSumDefined : Prop
  extraChannelsControlled : Prop
  productEqualsJ :
    -- hat Sigma_ha,J^G2 * hat Sigma_ah,J^G2 = J.
    Prop
  ewProjectorsDeferred : Prop
  poleMapDeferred : Prop
  rejectionLedger : RejectionLedger

def loop48G2FlowOverlapReady (G : Loop48G2FlowOverlapTarget) : Prop :=
  G.sameBasisAsTargetIIIg ∧
  G.chargeSectorCompatible ∧
  G.pointMetricPositive ∧
  G.sourceScaleSharedWithTargetIIIg ∧
  G.orientationSumDefined ∧
  G.extraChannelsControlled ∧
  G.productEqualsJ ∧
  G.ewProjectorsDeferred ∧
  G.poleMapDeferred

axiom loop48_g2_flow_overlap_target_required :
  ∃ G : Loop48G2FlowOverlapTarget, loop48G2FlowOverlapReady G

structure EndpointArenaData where
  chanPatonLabels : Prop
  matrixFields : Prop
  worldvolumeKernelRequired : Prop
  projectionRequired : Prop
  innerProductRequired : Prop
  kappaTauTarget : Prop

def endpointArenaObligation (E : EndpointArenaData) : Prop :=
  E.chanPatonLabels ∧
  E.matrixFields ∧
  E.worldvolumeKernelRequired ∧
  E.projectionRequired ∧
  E.innerProductRequired ∧
  E.kappaTauTarget

axiom loop34_endpoint_arena :
  ∃ E : EndpointArenaData, endpointArenaObligation E

structure CrossIssueLinks where
  O1_projectors : Prop
  O3_scalarPackage : Prop
  O8_poleRemainder : Prop
  O10_singleSourceVariable : Prop
  O20_commonReducedBasis : Prop

def crossIssueLinksReady (C : CrossIssueLinks) : Prop :=
  C.O1_projectors ∧
  C.O3_scalarPackage ∧
  C.O8_poleRemainder ∧
  C.O10_singleSourceVariable ∧
  C.O20_commonReducedBasis

axiom loop34_o4_cross_issue_links :
  ∃ C : CrossIssueLinks, crossIssueLinksReady C

structure ScIntKernelData where
  dtnKernel : Kernel
  braneKernel : Kernel
  superconnectionCurvature : SuperconnectionCurvature
  photonReferenceKernel : Kernel
  projector : Projection
  sourceScale : SourceScale
  poleMap : PoleMap
  hattedKernelEqualsDeVriesBlock : Prop
  remainderDerived : Prop
  extraChannelsDecouple : Prop

def scIntKernelReady (S : ScIntKernelData) : Prop :=
  S.hattedKernelEqualsDeVriesBlock ∧
  S.remainderDerived ∧
  S.extraChannelsDecouple

axiom loop40_sc_int_kernel :
  ∃ S : ScIntKernelData, scIntKernelReady S

structure Loop42ActiveProofSpine where
  chmNeutralCurrentEntry : CHMCurrentEntryData
  hodgeSquareRootEntry : HodgeSquareRootData
  orderedProjectors : OrderedProjectorPackage
  sharedReducedBasis : Prop
  sharedSourceScale : Prop
  photonProjectionInSameProduct : Prop
  poleRemainderCarried : Prop

def loop42ActiveProofSpineReady (S : Loop42ActiveProofSpine) : Prop :=
  S.sharedReducedBasis ∧
  S.sharedSourceScale ∧
  S.photonProjectionInSameProduct ∧
  S.poleRemainderCarried

axiom loop42_active_proof_spine_obligation :
  ∃ S : Loop42ActiveProofSpine, loop42ActiveProofSpineReady S

end DeVries.O4SourceKernel
