/-!
Loop 31 note to self: parent directory source queues for O10 and top.

This is a Lean-style research note kept outside Lean compilation.
It records obligations triggered by the parent-directory read.
-/

namespace DeVries.ParentDirectoryLoop31

constant ParentSourceNote : Type
constant PrimarySource : Type
constant SourceCoordinate : Type
constant SourceScale : Type
constant InnerProduct : Type
constant Projection : Type
constant ReducedKernel : Type
constant ExtraChannelRule : Type
constant ScalarFunctional : Type
constant TopDatum : Type
constant PoleMap : Type

structure ParentReadScope where
  prTalks_provenance : ParentSourceNote
  phys3_unbroken_susy_note : ParentSourceNote
  phys4_top_brane_note : ParentSourceNote
  dualsm_brane_dictionary : ParentSourceNote
  weak_electroweak_guardrails : ParentSourceNote
  primary_upgrade_required : Prop

axiom loop31_parent_read_scope :
  ∃ S : ParentReadScope, S.primary_upgrade_required

structure O10SingleSourcePackage where
  u : SourceCoordinate
  t_dim_supplied : Prop
  t_EW_supplied : Prop
  v_supplied : Prop
  mh2_supplied : Prop
  LambdaJ : SourceScale
  innerProduct : InnerProduct
  projection : Projection
  kernel : ReducedKernel
  extraChannelRule : ExtraChannelRule
  scalarFunctional : ScalarFunctional
  topDatum : TopDatum
  poleMap : PoleMap
  same_source_variable : Prop

def o10PackageReady (P : O10SingleSourcePackage) : Prop :=
  P.t_dim_supplied ∧
  P.t_EW_supplied ∧
  P.v_supplied ∧
  P.mh2_supplied ∧
  P.same_source_variable

axiom o10_middle_line_requires_package :
  ∃ P : O10SingleSourcePackage, o10PackageReady P

structure TopBoundaryQueue where
  hanany_witten_primary : PrimarySource
  witten_mtheory_primary : PrimarySource
  d6_as_kk_monopole_primary : PrimarySource
  top_as_boundary_datum : TopDatum
  attached_to_same_u : Prop

def topBoundaryQueueAdmissible (T : TopBoundaryQueue) : Prop :=
  T.attached_to_same_u

axiom top_queue_is_optional_until_primary_sources :
  ∃ T : TopBoundaryQueue, topBoundaryQueueAdmissible T

end DeVries.ParentDirectoryLoop31

