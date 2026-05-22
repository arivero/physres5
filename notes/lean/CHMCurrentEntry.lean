/-!
Loop 27 note to self: CHM current-entry extraction and Berger-S3 middle-line test.

These notes are uncompiled. They record theorem obligations introduced after
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

structure CurrentExtraction where
  transverseTrace : BoundaryTrace
  currentProjection : Projection
  chmProduct : CHMProduct
  dtnKernel : Kernel
  braneKernel : Kernel
  referenceKernel : Kernel
  endpointNormalConvention : Type
  photonProjection : Type
  orderedWZBoundaryMap : Type
  lambdaToPoleMap : PoleMap
  normalizedCurrent : Prop

def currentExtractionAdmissible (C : CurrentExtraction) : Prop :=
  C.normalizedCurrent

def currentExtractionGivesSigmaAA (C : CurrentExtraction) : Prop :=
  True

/- Obligation 1:
   Define a_J = P_{a,J} A_T^boundary with <a_J,a_J>_CHM = 1 and compute
     K_cur,J(lambda)
       = <a_J,(K_DtN,T,J + K_brane,T,J - K_ref,T,J)a_J>_CHM.
   The target is K_cur,J(lambda) = lambda + Sigma_AA,J + higher-order terms
   with Sigma_AA,J = J in the selected normalization. -/
axiom loop27_chm_current_entry_required :
  ∃ C : CurrentExtraction,
    currentExtractionAdmissible C ∧ currentExtractionGivesSigmaAA C

structure SingleSourceKKFixing where
  u : SourceVariable
  tDim : Type
  tEW : Type
  reducedKernel : Kernel
  scalarMap : ScalarFunctional
  poleMap : PoleMap
  sameSourceVariable : Prop

def singleSourceKKFixingReady (S : SingleSourceKKFixing) : Prop :=
  S.sameSourceVariable

/- Obligation 2:
   Parent physres6 material enters as a theorem target after one source
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
