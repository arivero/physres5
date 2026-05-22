/-!
Loop 24 note to self: electroweak superconnection assignment for O1.

This is a Lean-style research note.  It is kept outside Lean compilation.
The goal is to trigger expert review of the ordered W/Z assignment.
-/

namespace DeVries.SuperconnectionAssignment

constant GaugeHiggsComplex : Type
constant OddHiggs : Type
constant EvenCurrent : Type
constant PoleScheme : Type
constant InnerProduct : Type
constant MatchingRemainder : Type
constant BoundaryKernelCompatibility : Type
constant AnomalyLedger : Type

constant Phi_odd : OddHiggs
constant F_even_gamma_perp : EvenCurrent
constant J_H : Real
constant J_adj : Real
constant Delta_sc : MatchingRemainder

structure SuperconnectionReduction where
  complex : GaugeHiggsComplex
  innerProduct : InnerProduct
  poleScheme : PoleScheme
  odd_higgs_channel : OddHiggs
  even_transverse_current : EvenCurrent
  P_W_assigns_doublet : J_H = (3 / 4 : Real)
  P_Z_assigns_adjoint : J_adj = (2 : Real)
  same_complex_supplies_both_maps : Prop
  photon_null_direction_preserved : Prop
  ew_ray_preserved : Prop
  trace_space_separated : Prop
  wigner_eckart_route_excluded : Prop
  so32_flavour_requires_explicit_coupling : Prop
  anomaly_ledger : AnomalyLedger
  anomaly_ledger_consistent : Prop
  chm_boundary_kernel_compatibility : BoundaryKernelCompatibility
  negative_branch_scalar_map_required : Prop
  matching_remainder_derived : Prop

def O1SuperconnectionTarget (S : SuperconnectionReduction) : Prop :=
  S.same_complex_supplies_both_maps ∧
  S.photon_null_direction_preserved ∧
  S.ew_ray_preserved ∧
  S.trace_space_separated ∧
  S.wigner_eckart_route_excluded ∧
  S.so32_flavour_requires_explicit_coupling ∧
  S.anomaly_ledger_consistent ∧
  S.negative_branch_scalar_map_required ∧
  S.matching_remainder_derived

axiom superconnection_assignment_obligation :
  ∃ S : SuperconnectionReduction, O1SuperconnectionTarget S

/- Diagram to check in manuscript form:

Phi_odd  --P_W-->  J_H = 3/4
  | D_J + D_J^dagger |
F_even^{gamma^perp} --P_Z--> J_adj = 2

M_W,pole^2 / M_Z,pole^2
  = x_+(J_H) / x_+(J_adj) + Delta_sc.

Acceptance test:
1. source a single electroweak superconnection complex;
2. define the inner product on odd Higgs and even transverse-current data;
3. derive P_W and P_Z from that complex;
4. preserve the electroweak ray and photon zero mode;
5. keep odd-Higgs, even-current, and interval-boundary trace spaces separated
   until a common source operator defines the comparison;
6. record the Wigner--Eckart route as excluded for the tested parents;
7. require an explicit SO(32)-flavour coupling to the electroweak kernel;
8. match the superconnection data to a CHM boundary kernel;
9. derive or compute Delta_sc in the pole scheme;
10. connect the negative eigenvector to a gauge-invariant scalar functional.
11. attach an anomaly ledger for added gauge-Higgs or fermionic channels.
-/

end DeVries.SuperconnectionAssignment
