/-!
Loop 25 note to self: parent-directory read.

This is a Lean-style research note.  It records source queues and obligations
learned from the read-only pass over `..`.  It is kept outside Lean
compilation.
-/

namespace DeVries.ParentDirectoryLoop25

constant ParentCluster : Type
constant PrimarySource : Type
constant ProjectSourceLabel : Type
constant GaugeHiggsOperator : Type
constant BoundaryKernel : Type
constant ScalarFunctional : Type

structure ParentReadProtocol where
  pdfs_remain_source_objects : Prop
  text_extraction_is_access_aid : Prop
  runtime_state_excluded : Prop
  manuscript_claims_need_primary_or_project_label : Prop

def parentReadAdmissible (P : ParentReadProtocol) : Prop :=
  P.pdfs_remain_source_objects ∧
  P.text_extraction_is_access_aid ∧
  P.runtime_state_excluded ∧
  P.manuscript_claims_need_primary_or_project_label

axiom loop25_parent_read_protocol :
  ∃ P : ParentReadProtocol, parentReadAdmissible P

structure ElectroweakRayQueue where
  photon_null_direction_preserved : Prop
  common_higgs_radial_parameter : Prop
  wz_projective_ratio_preserved : Prop
  ordered_sampling_requires_source_operator : Prop

def electroweakRayQueueReady (E : ElectroweakRayQueue) : Prop :=
  E.photon_null_direction_preserved ∧
  E.common_higgs_radial_parameter ∧
  E.wz_projective_ratio_preserved ∧
  E.ordered_sampling_requires_source_operator

axiom prtalks_ray_queue_promotes_O1 :
  ∃ E : ElectroweakRayQueue, electroweakRayQueueReady E

structure SuperconnectionSourceQueue where
  su21_sources_required : Prop
  odd_higgs_doublet_sector : Prop
  even_photon_orthogonal_current_sector : Prop
  one_inner_product_required : Prop
  pole_matching_required : Prop

def superconnectionQueueAdmissible (S : SuperconnectionSourceQueue) : Prop :=
  S.su21_sources_required ∧
  S.odd_higgs_doublet_sector ∧
  S.even_photon_orthogonal_current_sector ∧
  S.one_inner_product_required ∧
  S.pole_matching_required

axiom phys4_superconnection_queue_requires_primary_upgrade :
  ∃ S : SuperconnectionSourceQueue, superconnectionQueueAdmissible S

structure WignerEckartObstruction where
  tested_parent_routes_excluded : Prop
  revival_requires_new_parent : Prop
  revival_requires_operator_tensor_type : Prop
  revival_requires_projection : Prop
  revival_requires_normalization : Prop

def wignerEckartRouteClosedGuardrail (W : WignerEckartObstruction) : Prop :=
  W.tested_parent_routes_excluded ∧
  W.revival_requires_new_parent ∧
  W.revival_requires_operator_tensor_type ∧
  W.revival_requires_projection ∧
  W.revival_requires_normalization

axiom weak_wigner_eckart_guardrail :
  ∃ W : WignerEckartObstruction, wignerEckartRouteClosedGuardrail W

structure ChmEntryTarget where
  kernel : BoundaryKernel
  derive_current_entry : Prop
  sigma_aa_equals_J : Prop
  photon_zero_mode_preserved : Prop
  scalar_product_fixed : Prop
  pole_map_fixed : Prop

def chmEntryTargetReady (C : ChmEntryTarget) : Prop :=
  C.derive_current_entry ∧
  C.sigma_aa_equals_J ∧
  C.photon_zero_mode_preserved ∧
  C.scalar_product_fixed ∧
  C.pole_map_fixed

axiom chm_current_entry_is_next_source_target :
  ∃ C : ChmEntryTarget, chmEntryTargetReady C

structure HiggsBranchInterpolationQueue where
  scalarFunctional : ScalarFunctional
  negative_branch_enters_order_parameter : Prop
  top_sector_source_map_required : Prop
  gauge_invariance_required : Prop
  same_source_variable_required : Prop

def higgsBranchQueueAdmissible (H : HiggsBranchInterpolationQueue) : Prop :=
  H.negative_branch_enters_order_parameter ∧
  H.top_sector_source_map_required ∧
  H.gauge_invariance_required ∧
  H.same_source_variable_required

axiom parent_higgs_interpolation_queue :
  ∃ H : HiggsBranchInterpolationQueue, higgsBranchQueueAdmissible H

end DeVries.ParentDirectoryLoop25
