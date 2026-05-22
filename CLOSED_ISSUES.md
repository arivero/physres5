# Closed Issues

This ledger preserves issues moved out of `OPEN_ISSUES.md` after referee and
advisor review.  Closure records cite the manuscript state and residual theorem
targets that remain active elsewhere.

## O1. Derive the W/Z assignment

**Closed in Loop 53.**

**Closure evidence.** The introduction and Sec.~IV now state the ordered
assignment
\[
(J_W,J_Z)=(J_H,J_{\rm adj})=(3/4,2)
\]
as the working assumption \(A3\) for the conditional pole-ratio proposal.
The safe electroweak reading is explicit: the charged comparison samples the
Higgs/order-parameter channel through a source projection, while the neutral
comparison samples the photon-orthogonal adjoint/current channel.  Appendix~D
Target~II records the corresponding theorem target with
\[
P_W(h_J)=3/4,\qquad
P_Z(a_J^{\gamma^\perp})=2,\qquad
P_\gamma(a_\gamma)=0,
\]
and Target~I carries the pole-scheme remainder.

**Residual target.** O1 is closed as assumption and theorem-target
bookkeeping.  No source derivation is claimed.  A source completion must still
derive the projection package, the shared normalization, photon subtraction,
and the pole remainder through \(T1\), Appendix~D Targets~0, I, II, III, VI,
and X.  O2b supplies the current input audit, and O3 supplies the scalar
partner map.

## O13. Casimir Keyword Load Versus Derivational Role

**Closed in Loop 25.**

**Closure evidence.** The title foregrounds the secular mass-ratio construction
and electroweak pole spectrum.  The abstract names the W/Z complex-pole
mass-ratio observable \(\sPole\).  Section~II states that \(J=s(s+1)\) is the
historical quadratic-Casimir input and that \(Q(J)\) is an ansatz awaiting a
source-theory derivation.

**Residual target.** The ordered assignment
\((J_W,J_Z)=(3/4,2)\) is assumption \(A3\); its source proof remains
Appendix~D Target~II and Target~I material.

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

**Residual target.** Target~I remains active for source-specific pole matching
and future electroweak-average covariance refinements.

## O2b. Current electroweak input audit

**Closed in Loop 54.**

**Closure evidence.** Section~III now contains a current W/Z input audit using
PDG mass-dependent-width Breit--Wigner inputs:
\[
M_{W,\rm BW}=80.3692\pm0.0133\,{\rm GeV},\qquad
\Gamma_{W,\rm BW}=2.14\pm0.05\,{\rm GeV},
\]
\[
M_{Z,\rm BW}=91.1879\pm0.0020\,{\rm GeV},\qquad
\Gamma_{Z,\rm BW}=2.4955\pm0.0023\,{\rm GeV}.
\]
The same section converts them with
\[
M_{V,\rm pole}=M_{V,\rm BW}/\sqrt{1+\gamma_V^2},
\qquad
\gamma_V=\Gamma_{V,\rm BW}/M_{V,\rm BW},
\]
and obtains
\[
M_{W,\rm pole}=80.3407\pm0.0134\,{\rm GeV},\qquad
M_{Z,\rm pole}=91.1538\pm0.0020\,{\rm GeV},
\]
\[
\left(s^2_{\rm pole}\right)_{\rm PDG\,audit}=0.2231768\pm0.0002608 .
\]
The propagated uncertainty is stated as an uncorrelated-input descriptive
error.  CDF-II and CMS 2026 are retained as W-mass inputs requiring a common Z
input, width convention, covariance prescription, and averaging rule before
they can replace the descriptive W/Z audit line.

**Residual target.** O2b is closed as the current descriptive input audit.
Future precision updates belong to Target~I or a later calculation phase with
the covariance matrices and averaging prescription supplied.

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

**Residual target.** Appendix~D Target~II, Appendix~D Target~0,
Appendix~D Target~I, Appendix~D Target~III, and Appendix~D Target~VI still
have to derive a source route whose ordered assignment, kernel, scale
placement, and dimensional variables commute with this ray.

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

## O10. Higgs interpolation \(D=11\to D=10\to D=9\) and colourless \(D=7\to D=6\to D=5\)

**Closed in Loop 50.**

**Closure evidence.** Appendix~E now gives the source-status dictionary for the
full-gauge chain
\[
n_{\rm KK}=7:\ SU(3)\times SU(2)\times U(1),
\qquad
n_{\rm KK}=6:\ \hbox{DeVries interpolation sector},
\qquad
n_{\rm KK}=5:\ SU(3)\times U(1)_{\rm geom},
\]
and the colour-spectator electroweak chain
\[
n_{\rm KK}^{\rm ew}=3:\ SU(2)\times U(1),
\qquad
n_{\rm KK}^{\rm ew}=2:\ \hbox{DeVries electroweak interpolation sector},
\qquad
n_{\rm KK}^{\rm ew}=1:\ U(1)_{\rm geom}\to U(1)_{\rm em}.
\]
It also states the formal joint-source map
\[
u\mapsto
\big(t_{\rm dim},t_{\rm EW},v,m_h^2,\Lambda_J,
\langle\cdot,\cdot\rangle_u,P_J,\widehat K_J,\mathcal D_J^{\rm extra},
\mathcal F_{\rm sc},\mathcal Y_{\rm top},\mathcal R_{\rm pole}\big),
\]
the middle-line pass/fail kernel, the electroweak-ray compatibility condition,
the ordered \((J_H,J_{\rm adj})=(3/4,2)\) assignment dependency, the
negative-branch scalar target, and the top-sector map.  Appendix~D Target~VI
mirrors these data as a maintained theorem target.

**Residual target.** O10 is closed as a manuscript-architecture and
source-status issue.  The source derivations remain open in the narrower
targets: Target~II for ordered W/Z sampling, O3 for the negative branch,
Target~0 and Target~III for the source kernel, Target~I for pole placement,
O17/Target~VII for electromagnetic endpoint normalization, Target~X for the
Hodge or superconnection origin, and Appendix~D Target~VI for the dimensional
source package.

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
physics obligations remain in Target~II, O3, Appendix~D Target~VI,
Appendix~D Target~VIII, Appendix~D Target~IX, and Appendix~D Target~X.

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
remain in Target~II, O3, Appendix~D Target~0, Appendix~D Target~III,
Appendix~D Target~VI, Appendix~D Target~VIII, Appendix~D Target~IX, and
Appendix~D Target~X.

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

## O17. Electromagnetic coupling \(\alpha\) as the content of the \(D=9\) \(U(1)\) endpoint

**Closed in Loop 49.**

**Closure evidence.** Section~IX now states explicitly that the present
construction does not predict \(\alpha\).  Appendix~D Target~VII and
Appendix~E record the precise reason: the current manuscript lacks a derived
scalar normalization for \(x_-(J)\), a source-fixed \(U(1)_{\rm em}\)
generator and charge lattice, and a scheme-fixed matching pair
\((Q_\alpha,\Delta_{\rm th})\).  Logan and Dawson support the low-energy bridge
\(M_W^2=g^2v^2/4\) and \(e=g\sin\theta_W\).  Salam--Strathdee and Witten
support only the qualitative Kaluza--Klein mechanism that four-dimensional
gauge couplings depend on compactification data.  Martin--Robertson and
Jegerlehner show that any comparison to \(\alpha\) requires a declared running
scheme, thresholds, and hadronic-vacuum-polarization convention.  The current
state of the manuscript is therefore a rejection of O17 as a present
prediction claim: \(\alpha\) remains a Standard Model input, and the DeVries
construction contributes the pole-ratio clue \(\sPole\).

**Residual target.** Target~VII remains in the manuscript as a future
source-theory corollary.  A later route may still derive scalar/vector
normalization, electromagnetic generator normalization, charge lattice, and
the matching pair \((Q_\alpha,\Delta_{\rm th})\) from one source package.

## O18. The \(s=3/2\) positive state and a Regge completion

**Closed in Loop 51.**

**Closure evidence.** Section~VI.B and Appendix~D Target~VIII now give the
Regge-intercept bookkeeping required for the first higher positive branch:
\[
M^2_{N_{\rm osc},j,\sigma}
=
\mu^2x_\sigma\!\big(j(j+1)\big)
+\frac{N_{\rm osc}}{\alpha'}
+\Delta^{\rm Regge}_{N_{\rm osc},j,\sigma},
\qquad \sigma=\pm .
\]
They separate the DeVries sector label \(j\), the oscillator or tower level
\(N_{\rm osc}\), and the physical trajectory spin supplied by the source
theory.  Target~VIII also records the first higher slot,
\[
M^2_{0,3/2,+}
=
\mu^2x_+(15/4)+\Delta^{\rm Regge}_{0,3/2,+},
\]
and routes every particle-level interpretation through the source package
\[
\mathfrak R_j=(K_j,\alpha',P_{\rm surv},\mathcal B_{\rm ND},
\mathcal Q,\mathcal T,\chi_{\rm spin}).
\]
The Biekotter--Heinemeyer--Weiglein \(95.4\) GeV diphoton source remains a
collider-ledger entry, with branch identity, gauge representation, survival
projection, production, decay, width, and exclusions supplied by a future source
theory.

**Residual target.** O18 is closed as a manuscript-architecture and
bookkeeping issue.  The derivations remain active in narrower targets:
Target~II for the ordered low-sector W/Z sampling, Target~0 and Target~III for the source
kernel and common slope, Target~I for pole placement and matching, Target~IX
for the brane-scaling and boundary-duality test, and Appendix~D Target~VIII
for the \(j=3/2\) particle assignment and future upgrades of the Regge source
package.

## O4. Dynamical derivation from string/brane/Regge data

**Closed in Loop 52.**

**Closure evidence.** Section~VI.G and Appendix~D Target~III now give a
maintained source-kernel ledger for every active route.  The common target is
\[
K_{J,r}(\lambda)=
\begin{pmatrix}
\lambda+\Sigma_{hh,J}^{r} & \Sigma_{ha,J}^{r}\\
\Sigma_{ah,J}^{r} & \lambda+\Sigma_{aa,J}^{r}
\end{pmatrix},
\qquad
\Sigma_{hh,J}^{r}=0,\quad
\Sigma_{aa,J}^{r}=J,\quad
\Sigma_{ha,J}^{r}\Sigma_{ah,J}^{r}=J,
\]
with \(r\) an endpoint, interval, \(G_2\), Regge, or Hodge/SUSY-QM route.  The
ledger records the CHM hatted current-entry protocol, the \(G_2\) ADE-pairing
and flow-overlap tests, the endpoint/Chan--Paton matrix arena, and the shared
boundary-superconnection interval package
\[
\widehat K_J^{\rm sc/int}
=
\Lambda_J^{-2}P_{\rm sc}^\dagger
\big[
K_T^{\rm DtN}+K_T^{\rm brane}
+\langle\mathcal F_{\rm sc},\mathcal F_{\rm sc}\rangle_{\rm sc}
-K_\gamma^{\rm ref}
\big]P_{\rm sc}.
\]

**Residual target.** O4 is closed as a route-architecture and theorem-target
ledger.  The physical derivation remains distributed across Target~II for
ordered W/Z sampling, O3 for the scalar partner, Target~0 and Target~III for source-kernel
entry derivations, Target~I for pole matching, Target~VI for the dimensional
source package, Target~X for the Hodge/superconnection reduced basis, and
global-form completion checks.

## O8. Pole placement versus high-scale placement

**Closed in Loop 52.**

**Closure evidence.** Section~III and Appendix~D Target~I define the pole
observable and the route-matching chain.  The comparison uses
\[
\sPole=1-\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2},
\]
with common line-shape inputs translated into the same complex-pole convention
before the ratio is formed.  Target~I states the source-to-pole chain
\[
\mathcal S
\longrightarrow
K_J^{\rm bare}(\lambda)
\longrightarrow
\Gamma_{\rm eff}[H,W,B]
\longrightarrow
\Delta^{-1}_{V,T}(s)\big|_{s=s_{W,Z}},
\]
and the matched quotient
\[
\sPole
=
1-\frac{x_+(J_H)}{x_+(J_{\rm adj})}
+\Delta_{\rm match}.
\]
High-scale, compactification-scale, running, and effective-angle readings are
therefore separate boundary-data problems with their own running, threshold,
and scheme maps.

**Residual target.** O8 is closed as a scheme and scale-placement ledger.  A
later source route still has to compute \(\Delta_{\rm match}\) in Target~I,
derive the ordered samples in Target~II, and use the current input audit in
Sec.~\ref{sec:current-wz-audit}.

## O19. Brane-scaling identity of the two branches

**Closed in Loop 52.**

**Closure evidence.** Section~VI.B and Appendix~D Target~IX now state the
branch-scaling admissibility test in terms of the shared Regge/D-brane package
\(\mathfrak R_j\) and the axis map
\[
\chi_{\rm spin}:\ j\mapsto s_{\rm br}(j),
\qquad
J_{\rm br}=s_{\rm br}(s_{\rm br}+1).
\]
With a source-supplied mass reading, the algebraic diagnostic is
\[
x_+(J_{\rm br})=1+O(s_{\rm br}^{-2}),\qquad
|x_-(J_{\rm br})|=s_{\rm br}(s_{\rm br}+1)+O(1).
\]
The D0 and space-filling labels are recorded as admissibility diagnostics.
A literal T-duality reading still requires a compact coordinate, a
Neumann--Dirichlet boundary-condition map, charge matching, tension matching,
and a negative-branch mass or scalar-functional reading.

**Residual target.** O19 is closed as a branch-scaling and brane-duality
bookkeeping issue.  Future physical use remains inside Target~IX, tied to
Target~VIII for \(\mathfrak R_j\), O3 for the negative-branch reading, and
global-form or boundary-condition data for a concrete completion.

## O20. The operator as a broken N=2 supersymmetric quantum mechanics

**Closed in Loop 52.**

**Closure evidence.** Appendix~D Target~X and Section~VI.G now state the
Hodge/SUSY-QM theorem target.  The de Rham/Hodge template supplies the
square-root entry
\[
D_Je^0_J=\sqrt J\,e^1_J,\qquad
D_J^\dagger e^1_J=\sqrt J\,e^0_J,
\]
and the projected operator target is
\[
Q_{{\rm red},J}
=
Q_{{\rm dR},J}+B_J,\qquad
B_J=
\begin{pmatrix}0&0\\0&-J\end{pmatrix}.
\]
Witten supplies the de Rham/SUSY-QM and Witten-deformation source equations;
Coquereaux supplies the finite electroweak superconnection arena; CHM supplies
the interval boundary kernels and photon-zero bookkeeping used by the shared
sc/int package.

**Residual target.** O20 is closed as a Hodge/superconnection route ledger.
Target~X remains the maintained acceptance target for the finite projection,
the source of \(J\), the breaking operator \(B_J\), extra-channel decoupling,
ordered electroweak samples, scalar partner, and pole-map compatibility.
