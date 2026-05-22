/-!
Loop 27 note: CHM current-entry extraction and Berger-S3 middle-line test.

These notes are uncompiled. They state theorem obligations introduced after
the parent-directory read and the Loop 27 referee/advisor pass.
-/

namespace DeVries.CHMCurrentEntry

constant BoundaryTrace : Type
constant CHMProduct : Type
constant Projection : Type
constant Kernel : Type
constant SourceVariable : Type
constant ScalarFunctional : Type
constant PoleMap : Type
constant BergerParameter : Type
constant BFCondition : Type
constant SourceScale : Type

structure CurrentExtraction where
  transverseTrace : BoundaryTrace
  currentProjection : Projection
  chmProduct : CHMProduct
  dtnKernel : Kernel
  braneKernel : Kernel
  referenceKernel : Kernel
  sourceScale : SourceScale
  endpointNormalConvention : Type
  photonProjection : Type
  orderedWZBoundaryMap : Type
  lambdaToPoleMap : PoleMap
  normalizedCurrent : Prop
  hattedSpectralVariable : Prop
  photonReferenceSubtraction : Prop

def currentExtractionAdmissible (C : CurrentExtraction) : Prop :=
  C.normalizedCurrent ∧
  C.hattedSpectralVariable ∧
  C.photonReferenceSubtraction

def currentExtractionGivesSigmaAA (C : CurrentExtraction) : Prop :=
  True

/- Obligation 1, updated in Loop 28:
   Define a_J = P_{a,J} A_T^boundary with <a_J,a_J>_CHM = 1 and compute
     Khat_cur,J(lambdahat)
       = Lambda_J^{-2}
         <a_J,(K_DtN,T,J + K_brane,T,J - K_ref,T,J)a_J>_CHM.
   The target is
     Khat_cur,J(lambdahat)
       = lambdahat + Sigmahat_AA,J + higher-order terms
   with Sigmahat_AA,J = J in the selected source normalization. -/
axiom loop27_chm_current_entry_required :
  ∃ C : CurrentExtraction,
    currentExtractionAdmissible C ∧ currentExtractionGivesSigmaAA C

structure PhotonReferenceSubtraction where
  photonProjection : Projection
  referenceKernel : Kernel
  transverseKernel : Kernel
  photonZeroFixed : Prop
  sharedSourceScale : Prop

def photonReferenceSubtractionReady (P : PhotonReferenceSubtraction) : Prop :=
  P.photonZeroFixed ∧ P.sharedSourceScale

/- Obligation 1c, updated in Loop 30:
   The current entry must be photon-reference subtracted before it is compared
   with J:
     P_gamma^dagger (K_T - K_ref) P_gamma = 0
   and
     Sigmahat_AA,J =
       Lambda_CHM^{-2}[
         <a_J, K_T(0) a_J>_CHM
         - <a_gamma, K_T(0) a_gamma>_CHM].
   The shared scale Lambda_CHM, photon projection P_gamma, current projection
   P_a,J, and reference kernel K_ref are source data. -/
axiom loop30_photon_reference_required :
  ∃ C : CurrentExtraction,
    C.photonReferenceSubtraction ∧
    C.normalizedCurrent ∧
    C.hattedSpectralVariable

axiom loop30_photon_reference_subtraction_data_required :
  ∃ P : PhotonReferenceSubtraction, photonReferenceSubtractionReady P

structure Loop44CHMAdmissibleCurrentEntry where
  neutralTrace : BoundaryTrace
  chmProduct : CHMProduct
  photonReferenceKernel : Kernel
  sourceScale : SourceScale
  currentProjection : Projection
  photonProjection : Projection
  positivePhotonNorm : Prop
  positiveGammaPerpNorm : Prop
  projectionOrderFixed : Prop
  deltaWCHM : Prop
  deltaYCHM : Prop
  sigmaAA2Target : Prop

def loop44CHMAdmissibleCurrentEntryReady
  (C : Loop44CHMAdmissibleCurrentEntry) : Prop :=
  C.positivePhotonNorm ∧
  C.positiveGammaPerpNorm ∧
  C.projectionOrderFixed ∧
  C.deltaWCHM ∧
  C.deltaYCHM ∧
  C.sigmaAA2Target

axiom loop44_chm_admissible_current_entry_required :
  ∃ C : Loop44CHMAdmissibleCurrentEntry,
    loop44CHMAdmissibleCurrentEntryReady C

structure Loop45CHMAdmissibilityLemma where
  neutralTrace : BoundaryTrace
  chmProduct : CHMProduct
  photonProjection : Projection
  gammaPerpProjection : Projection
  photonReferenceKernel : Kernel
  sourceScale : SourceScale
  currentSlope : Type
  positivePhotonNorm : Prop
  positiveGammaPerpNorm : Prop
  orthogonalityPreserved : Prop
  projectorOrderOrCommutation : Prop
  photonReferenceSubtraction : Prop
  sharedLambdaCHM : Prop
  kineticSlopePositive : Prop
  canonicalSigmaAA2 : Prop

def loop45CHMAdmissibilityLemmaReady
  (C : Loop45CHMAdmissibilityLemma) : Prop :=
  C.positivePhotonNorm ∧
  C.positiveGammaPerpNorm ∧
  C.orthogonalityPreserved ∧
  C.projectorOrderOrCommutation ∧
  C.photonReferenceSubtraction ∧
  C.sharedLambdaCHM ∧
  C.kineticSlopePositive ∧
  C.canonicalSigmaAA2

/- Obligation 1d, updated in Loop 45:
   The CHM current-entry comparison uses the canonical kernel
     Khat_cur_can,J = (Z_cur,J)^(-1) Khat_cur,J
   with
     Z_cur,J = d Khat_cur,J / d lambdahat at lambdahat = 0 > 0.
   The first pass/fail target is
     Sigmahat_AA,2^CHM,can = 2.
   The same admissibility lemma must also carry positive projected norms,
   photon-orthogonality preservation, source ordered projectors or a
   commutation theorem, photon reference subtraction, and one Lambda_CHM. -/
axiom loop45_chm_admissibility_lemma_required :
  ∃ C : Loop45CHMAdmissibilityLemma,
    loop45CHMAdmissibilityLemmaReady C

structure FactorizationFirstSpine where
  hodgeOffDiagonal : Prop
  chmCurrentDiagonal : Prop
  commonReducedBasis : Prop
  commonPoleMap : Prop

def factorizationFirstReady (F : FactorizationFirstSpine) : Prop :=
  F.hodgeOffDiagonal ∧
  F.chmCurrentDiagonal ∧
  F.commonReducedBasis ∧
  F.commonPoleMap

/- Obligation 1b:
   The active proof spine separates the Hodge/SUSY-QM off-diagonal target
     Sigma_HA,J * Sigma_AH,J = J
   from the hatted CHM current target
     Sigmahat_AA,J = J.
   Both targets must live in one reduced basis with one pole map. -/
axiom loop28_factorization_first_spine_required :
  ∃ F : FactorizationFirstSpine, factorizationFirstReady F

structure SingleSourceKKFixing where
  u : SourceVariable
  tDim : Type
  tEW : Type
  sourceScale : SourceScale
  reducedKernel : Kernel
  scalarMap : ScalarFunctional
  poleMap : PoleMap
  sameSourceVariable : Prop

def singleSourceKKFixingReady (S : SingleSourceKKFixing) : Prop :=
  S.sameSourceVariable

/- Obligation 2:
   Parent physres6 material is a theorem target after one source
   variable supplies t_dim, t_EW, K_J, F_sc, and the pole map. -/
axiom loop27_parent_kk_fixing_guardrail :
  ∃ S : SingleSourceKKFixing, singleSourceKKFixingReady S

structure BergerCHMTarget where
  rho : BergerParameter
  hodgeOneFormKernel : Kernel
  chmBoundaryKernel : Kernel
  projectionToTwoChannels : Projection
  innerProduct : CHMProduct
  extraChannelDecoupling : Type
  bfScalarCheck : BFCondition
  scalarFunctional : ScalarFunctional
  poleMap : PoleMap

def bergerCHMGivesDeVriesKernel (B : BergerCHMTarget) : Prop :=
  True

def bergerCHMHasBFAdmissibleScalar (B : BergerCHMTarget) : Prop :=
  True

/- Obligation 3:
   Use the Henkel-Lauret one-form Hodge-Laplacian matrix on homogeneous
   three-spheres as a source arena. Test whether a Berger parameter rho and a
   CHM boundary kernel project to the DeVries block while the negative branch
   passes a BF scalar-admissibility check. -/
axiom loop27_berger_chm_middle_line_required :
  ∃ B : BergerCHMTarget,
    bergerCHMGivesDeVriesKernel B ∧ bergerCHMHasBFAdmissibleScalar B

end DeVries.CHMCurrentEntry
