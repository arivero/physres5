/-!
Loop 32 note to self: negative branch as a same-source scalar-functional
target.

This is a Lean-style research note kept outside Lean compilation.
It records theorem obligations for O3 after the referee/advisor cycle.
-/

namespace DeVries.NegativeBranchScalar

constant SourceCoordinate : Type
constant Scheme : Type
constant SpinLabel : Type
constant HilbertSpace : Type
constant InnerProduct : Type
constant Projection : Type
constant SourceScale : Type
constant PoleMap : Type
constant ScalarFunctional : Type
constant BranchValue : Type
constant Holonomy : Type
constant EffectivePotential : Type
constant ObservableKind : Type
constant BoundaryDatum : Type
constant G2Datum : Type

structure SameSourceBranchPackage where
  u : SourceCoordinate
  Jstar : SpinLabel
  HJ : HilbertSpace
  innerProduct : InnerProduct
  projection : Projection
  LambdaJ : SourceScale
  poleMap : PoleMap
  scalarFunctional : ScalarFunctional
  scheme : Scheme
  positiveBranchValue : BranchValue
  negativeBranchValue : BranchValue
  sameOperatorSuppliesBranches : Prop
  scalarFunctionalGaugeInvariant : Prop
  normalizationSharedOrDeclared : Prop
  observableKindDeclared : Prop

def o3ScalarPackageReady (P : SameSourceBranchPackage) : Prop :=
  P.sameOperatorSuppliesBranches ∧
  P.scalarFunctionalGaugeInvariant ∧
  P.normalizationSharedOrDeclared ∧
  P.observableKindDeclared

axiom o3_requires_same_source_package :
  ∃ P : SameSourceBranchPackage, o3ScalarPackageReady P

structure WilsonLineScalarRoute where
  u : SourceCoordinate
  alphaH : Holonomy
  Veff : EffectivePotential
  scheme : Scheme
  curvatureFunctional : ScalarFunctional
  sameHJ : HilbertSpace
  sameProjection : Projection
  branchMatch : Prop

def wilsonLineRouteReady (W : WilsonLineScalarRoute) : Prop :=
  W.branchMatch

axiom interval_gauge_higgs_priority_route :
  ∃ W : WilsonLineScalarRoute, wilsonLineRouteReady W

structure RouteIngredientLedger where
  endpointBoundaryScalar : BoundaryDatum
  intervalHolonomyOrRadion : BoundaryDatum
  g2Deformation : G2Datum
  deVriesMapDerived : Prop
  pdfFormulaChecksDone : Prop

def ledgerReadyForManuscriptClaim (L : RouteIngredientLedger) : Prop :=
  L.deVriesMapDerived ∧ L.pdfFormulaChecksDone

axiom route_ingredients_are_addresses :
  ∃ L : RouteIngredientLedger, True

end DeVries.NegativeBranchScalar

