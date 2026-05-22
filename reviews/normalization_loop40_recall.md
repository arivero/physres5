# Loop 40 Random Recall

## Draw

- Bibliography: `CsakiHubiszMeade2005`, `HenkelLauret2026`.
- Source fragments:
  `context/source_fragments/08_alvarezgaume_vazquezmozo_field_theory_and_standard_model_2306_08097/pages_061-070.md`,
  `context/source_fragments/04_polchinski_what_is_string_theory_hep_th_9411028/pages_071-080.md`,
  `context/source_fragments/04_polchinski_what_is_string_theory_hep_th_9411028/pages_091-100.md`,
  and `context/source_fragments/03_ginsparg_applied_conformal_field_theory_hep_th_9108028/pages_001-010.md`.

## Source Read

Alvarez-Gaume--Vazquez-Mozo pages 61--70 record Wigner-Weyl and
Nambu-Goldstone realizations, the vacuum charge criterion, unbroken subalgebra
condition, expansion around a vev, and the mass matrix as a Hessian at the
vacuum.

Polchinski pages 71--80 record the worldsheet S-matrix as a sum over compact
topologies and moduli, vertex-operator insertions, BRST ghost insertions, and
the \((1,1)\) condition for physical vertex operators.  Pages 91--100 record
local redundancy from gauging a nonlinear symmetry, electric/magnetic charge
lattices, the \(\tau=\theta/(2\pi)+i2\pi/e^2\) parameter, and \(SL(2,\mathbb Z)\)
charge transformations.

Ginsparg pages 1--10 record conformal invariance, the special force of
two-dimensional conformal symmetry, and the role of CFT constraints in string
solution spaces and internal degrees of freedom.

## Consequence

The sc/int package is compatible with the recall pass.  The electroweak
assignment must remain tied to a vacuum charge criterion and Hessian/mass
matrix data.  The string route needs vertex/operator and moduli data if it is
used to promote the interval-superconnection kernel beyond a field-theory
boundary package.  The O17 endpoint route needs charge-lattice and duality data
in addition to photon zero-mode subtraction.  These points are recorded in the
source inventory and remain issue-ledger obligations.

## Extra Note Review

Random note/source draw:
`notes/lean/loop15_admissibility_filters.lean`,
`reviews/normalization_loop37_recall.md`,
`context/source_fragments/06_tong_gauge_theory_notes/pages_161-170.md`,
`context/source_fragments/45_hosotani_dynamical_mass_generation_compact_extra_dimensions_plb126_1983/pages_001-005.md`,
and
`context/source_fragments/24_acharya_witten_chiral_fermions_g2_hep_th_0109152/pages_021-027.md`.

The Loop 15 Lean note still matches the active sc/int package: a trace-transfer
witness needs a source operator, field basis, projection, normalization, and
trace-space identification.  The SO(32) filter remains a separate completion
obligation involving endpoints, anomaly, hypercharge, global form, and
electroweak coupling.

Tong pages 161--170 record the index theorem, axial charge violation, topology
of \(F\wedge F\), and instanton zero-mode selection.  Hosotani pages 1--5
record compact \(S^1\) gauge-Higgs dynamics, twisted boundary conditions,
Wilson-line phases, one-loop effective potential, and gauge periodicity of the
holonomy variable.  Acharya--Witten pages 21--27 record \(G_2\) singularity
deformation, local \(U(1)^2\to U(1)\) breaking from the C-field sector, chiral
matter at the conical singularity, the Type IIA/D6-brane comparison in a
special case, and Higgsing to a diagonal gauge group.

Consequence: the sc/int theorem package keeps the Loop 15 witness fields.  The
scalar branch should keep the Hosotani holonomy/effective-potential route in
view.  The \(G_2\) route should express deformation, localized matter,
anomaly, and current-entry data with the same precision used for CHM.
