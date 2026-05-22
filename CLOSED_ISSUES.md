# Closed Issues

This ledger preserves issues moved out of `OPEN_ISSUES.md` after referee and
advisor review.  Closure records cite the manuscript state and residual theorem
targets that remain active elsewhere.

## O13. Casimir Keyword Load Versus Derivational Role

**Closed in Loop 25.**

**Closure evidence.** The title foregrounds the secular mass-ratio construction
and electroweak pole spectrum.  The abstract names the W/Z complex-pole
mass-ratio observable \(\sPole\).  Section~II states that \(J=s(s+1)\) is the
historical quadratic-Casimir input and that \(Q(J)\) is an ansatz awaiting a
source-theory derivation.

**Residual target.** The ordered assignment
\((J_W,J_Z)=(3/4,2)\) remains O1 and Appendix~D Target~I material.

## O14. Trace-Space Separation

**Closed in Loop 25.**

**Closure evidence.** Section~II, Section~VI.G, Appendix~D, and
`notes/lean/SuperconnectionAssignment.lean` keep the DeVries branch matrix,
rank-one seed matrices, signed negative-sector matrices, odd Higgs spaces, even
current spaces, and interval boundary products in separate ledgers until a
common source operator supplies the comparison.

**Residual target.** Future source routes still owe the operator, field basis,
inner product, and normalization that bind these spaces.

## O15. Wigner--Eckart Route Status

**Closed in Loop 25.**

**Closure evidence.** Section~VI.G and Appendix~D record the Wigner--Eckart or
Clebsch route as a failed tested subroute.  The doublet-parent and triplet-axial
checks are archived as excluded derivations of the DeVries off-diagonal entry.

**Residual target.** A future revival requires a different parent
representation, operator tensor type, projection, or normalization.

## O2a. Pole Convention Formula

**Closed in Loop 29.**

**Closure evidence.** Section~III defines the comparison observable
\(\sPole\), fixes the complex-pole convention
\[
s_V=M_{V,\rm pole}^2-iM_{V,\rm pole}\Gamma_{V,\rm pole},
\]
states the charged and neutral transverse pole conditions, records the
alternate \(s_{\rm pole}=(M-i\Gamma/2)^2\) parameterization, and gives the
variable-width Breit--Wigner conversion
\[
M_{V,\rm pole}
=
\frac{M_{V,\rm BW}}{\sqrt{1+\gamma_V^2}},
\qquad
\Gamma_{V,\rm pole}
=
\frac{\Gamma_{V,\rm BW}}{\sqrt{1+\gamma_V^2}},
\qquad
M_{V,\rm BW}^2=M_{V,\rm pole}^2+\Gamma_{V,\rm pole}^2 .
\]
Appendix~D Target~I repeats the same convention map inside the pole-placement
theorem target.

**Residual target.** O2b remains open for the current W/Z input audit,
uncertainty propagation, and source-specific mass/width convention table.

## O5. Electroweak Ray and Forbidden Deformations

**Closed in Loop 29.**

**Closure evidence.** Section~IV derives the tree-level gauge-Higgs mass matrix,
the photon null mode, the projective W/Z ratio, and the radial family
\[
H_t=\frac{1}{\sqrt2}\binom{0}{t v+h},
\qquad
M_W^2(t)=t^2\frac{g^2v^2}{4},
\qquad
M_Z^2(t)=t^2\frac{(g^2+g'^2)v^2}{4},
\qquad
M_\gamma^2(t)=0.
\]
Appendix~D Target~IIa records the same ray as an admissibility theorem and
lists the failure modes for source routes.

**Residual target.** O1, O4, O8, and O10 still have to derive a source route
whose ordered assignment, kernel, scale placement, and dimensional variables
commute with this ray.

## O6. Flavor Boundary

**Closed in Loop 29.**

**Closure evidence.** Section~VII states the boundary condition: a link between
the two-channel electroweak determinant and generation/flavor organization
requires explicit model data.  It gives the Higgs-doublet and adjoint/current
representation samples, labels SO(32)-flavor material as a project-source
boundary sector, and lists the required checks: representation space, Standard
Model chiral fermion map, orientifold/tadpole or endpoint constraints,
extra-state projection, anomaly cancellation, hypercharge normalization,
global-form compatibility, and coupling to the electroweak determinant.

**Residual target.** A completion still has to derive the flavor-to-electroweak
operator coupling, projection of extra states, anomaly ledger, hypercharge
normalization, and ordered W/Z assignment.

## O7. Global Form of the Standard Model Gauge Group

**Closed in Loop 29.**

**Closure evidence.** Section~VIII states
\[
\GSM=\frac{SU(3)_C\times SU(2)_W\times U(1)_Y}{\Gamma},
\qquad
\Gamma\subset \mathbb Z_6,
\]
explains line-operator and topological-response tests, and formulates the
global-form compatibility condition for any compactification, endpoint, or
\(G_2\) completion.  Appendix~D Target~V keeps the same quotient and
completion checks in theorem-target form.

**Residual target.** Any specific source route still has to identify
\(\Gamma\), surviving line operators, Higgs/order-parameter transformation
law, anomaly compatibility, and the compatibility of \(\mathcal O_J\) with
the same quotient.

## O9. Theorem-Target Ledger

**Closed in Loop 29.**

**Closure evidence.** Appendix~D now supplies the requested ledger structure:
a common theorem-target format, Target~0 for unified source-to-pole matching,
Target~0a for admissibility filters, Targets~I--X for pole placement,
electroweak assignment, ray admissibility, boundary determinant, negative
branch, global form, dimensional interpolation, electromagnetic endpoint,
Regge survival, branch scaling, and Hodge/SUSY-QM origin.  It also contains
the claim hierarchy, minimum derivation chain, common acceptance criterion, and
derivation checklist.  Section~IX summarizes the same hierarchy in journal
prose.

**Residual target.** Appendix~D remains a maintained artifact.  New speculative
routes must add or update their theorem targets, and the issue-specific
derivations remain open under their current O-numbers.

## O11. Adjacent `prTalks` Source-Note Validation

**Closed in Loop 29.**

**Closure evidence.** `context/prtalks_source_notes.md` records the PDF source
protocol, text-extraction caveat, visual-transcription caveat, inventory of the
adjacent PDFs, valid project content, promoted obligations, and primary-source
upgrade queue.  `notes/lean/PrTalks.lean` mirrors the protocol and records the
electroweak-ray, orbit-quadratic, Regge, minimal-block, dimensional,
negative-branch, and top-sector obligations in Lean-style notes.

**Residual target.** Manuscript uses of prTalks-derived material require
primary local literature or an explicit project-source label.  The active
physics obligations remain in O1, O10, O17, O18, O19, and O20.

## O12. Parent-Workspace Source-Note Validation

**Closed in Loop 29.**

**Closure evidence.** `context/parent_workspace_source_notes.md` records the
parent-source protocol, relevant parent inventory, promoted guardrails,
loop-by-loop parent refreshes, and source-upgrade queues.  Valid imports are
constraints, failure modes, theorem targets, source-upgrade queues, and
provenance trails.  `notes/lean/AdjacentWorkspaceGuardrails.lean` mirrors the
protocol and records the mass-map, one-source block, negative-sector EFT,
custodial, string/Regge, SO(32), and dimensional-interpolation guardrails.

**Residual target.** Parent-derived manuscript claims require primary-source
support or explicit project-source status.  The residual physics obligations
remain in O1, O3, O4, O10, O17, O18, O19, and O20.

## O16. SO(32) Flavor/String Completion Boundary

**Closed in Loop 29.**

**Closure evidence.** Section~VII states the SO(32)-flavor role as
project-source boundary bookkeeping and completion arena, records
\[
16=(5,3)+(1,1),
\qquad
\wedge^2(5,3)=(15,\bar3)+(\overline{10},6),
\]
and lists the checks required for journal-facing use.  Appendix~D Target~V
preserves the same data as a global-form and localization compatibility target.

**Residual target.** A concrete SO(32) completion still has to derive the
orientifold or endpoint construction, projection or decoupling of extra states,
anomaly and hypercharge checks, global-form compatibility, and a coupling from
the flavor sector to the electroweak DeVries operator.
