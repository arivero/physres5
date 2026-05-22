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

end DeVries.O4SourceKernel
