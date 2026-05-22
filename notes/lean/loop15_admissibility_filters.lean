/-!
Loop 15 admissibility filters.

These notes are Lean-style research notes.  They are not compiled.
-/

namespace DeVries.Loop15

constant SourceOperator : Type
constant FieldBasis : Type
constant Projection : Type
constant Normalization : Type
constant Matrix2 : Type
constant Representation : Type
constant OperatorTensor : Type

constant Q : Matrix2
constant K_seed_one : Matrix2
constant K_minus_sigma3 : Matrix2

structure TraceTransferWitness where
  source : SourceOperator
  basis : FieldBasis
  projection : Projection
  normalization : Normalization
  identifies_Q : Prop
  identifies_seed : Prop
  identifies_minus : Prop

axiom no_trace_transfer_without_witness :
  TraceTransferWitness -> Prop

structure WignerEckartRoute where
  parent_representation : Representation
  operator_tensor : OperatorTensor
  projection : Projection
  normalization : Normalization
  derives_ordered_pair : Prop

axiom doublet_parent_selection_filter :
  WignerEckartRoute -> Prop

axiom triplet_axial_parent_casimir_filter :
  WignerEckartRoute -> Prop

structure SO32BoundaryCompletion where
  has_orientifold_or_endpoint_model : Prop
  extra_states_projected_or_decoupled : Prop
  anomaly_check : Prop
  hypercharge_check : Prop
  global_form_check : Prop
  couples_to_electroweak_KJ : Prop

def AdmissibleSO32 (c : SO32BoundaryCompletion) : Prop :=
  c.has_orientifold_or_endpoint_model /\
  c.extra_states_projected_or_decoupled /\
  c.anomaly_check /\
  c.hypercharge_check /\
  c.global_form_check /\
  c.couples_to_electroweak_KJ

end DeVries.Loop15
