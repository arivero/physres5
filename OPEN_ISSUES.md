# Open analytical issues

## O1. Derive the W/Z assignment

**Question.** Why does the charged W comparison sample \(J=3/4\) while the neutral Z comparison samples \(J=2\)?

**Current working idea.** The \(J=2\) datum has an adjoint-current reading through the \(SU(2)_L\) gauge sector. The \(J=3/4\) datum belongs to the Higgs/order-parameter doublet side. The missing step is the ordered sampling rule that turns \((J_H,J_{\rm adj})=(3/4,2)\) into the W/Z quotient.

**Success criterion.** A derivation from the gauge-Higgs sector that yields the ordered pair \((J_W,J_Z)=(3/4,2)\) directly and rules out post-selection.

## O2. Pole-mass scheme

**Question.** What exact mass convention makes the numerical comparison meaningful?

**Current working idea.** Use complex pole positions for the descriptive low-energy spectral clue. Treat Breit-Wigner/on-shell and running weak angle inputs as scheme transformations. The comparison to CDF-II is descriptive and source-audit pending.

**Success criterion.** A section with formulas for converting conventional quoted masses into pole quantities, including uncertainty propagation and a table of current inputs.

## O3. Negative branch and Higgs scale

**Question.** Does \(x_-(J)\) encode the Higgs/order-parameter scale, a tachyonic mass term, or an auxiliary branch?

**Current working idea.** The negative root is the main reason the numerics matter: with the vector-spectrum normalization, the two negative magnitudes point toward the Higgs/order-parameter scales. The scalar-sector map must be gauge-invariant and scheme-controlled.

**Success criterion.** A gauge-invariant expression connecting \(x_-(J)\) to \(\mu_H^2\), \(\lambda\), \(v\), or a pole observable.

**Latest refinement.** Sec. V now treats the negative branch as a scalar-functional theorem target:
\[
\mathcal F_{\rm sc}
=
\mathcal F_{\rm sc}
\big(H^\dagger H,(D_\mu H)^\dagger D^\mu H,V(H),
\hbox{boundary or compactification data}\big),
\qquad
\mathcal F_{\rm sc}(J_\star)=C_{\rm sc}|x_-(J_\star)|.
\]
The route-specific maps are endpoint brane-scalar data, interval boundary/modulus data, and \(G_2\) singularity-deformation data.

## O4. Dynamical derivation from string/brane/Regge data

**Question.** Why should a string/brane/KK system generate exactly this two-branch secular equation?

**Current working idea.** The construction preserves high-spin/Regge asymptotics while splitting low-spin branches. Candidate mechanisms include open-string endpoint data, KK momentum/winding charges, interval boundary conditions, and brane/bulk mixing.

**Success criterion.** Derive the matrix or quadratic equation from a variational problem, boundary condition, or compactification mode equation.

**Latest refinement.** The target is now expressed as simultaneous trace/determinant data:
\[
\operatorname{tr}\mathcal M_J=-J,\qquad \det\mathcal M_J=-J,
\qquad \mathcal M_J=\begin{pmatrix}0&\sqrt J\\ \sqrt J&-J\end{pmatrix}.
\]
Candidate routes are endpoint/Chan--Paton data, interval boundary eigenvalue conditions, and localized \(G_2\) spectral operators.

**Toy-operator target.** The current two-channel action writes the missing dynamics as
\[
\kappa_J^2=J,\qquad \tau_J=J.
\]
The next derivation must identify the physical origin of these entries: endpoint charge normalization, interval boundary variation, localized \(G_2\) data, or a shared operator whose low-energy reduction fixes both.

**Endpoint refinement.** The brane-Higgsing route now has a concrete dictionary:
Chan--Paton labels supply matrix fields, coincident branes supply adjoint gauge fields and scalars, and separated branes give scalar/vector mixing through stretched strings. The unresolved step is the reduction of this matrix worldvolume data to \(\kappa_J^2=\tau_J=J\) and the ordered pair \((3/4,2)\).

**Interval refinement.** The KK route now has a parallel dictionary:
interval variational data supply a boundary kernel \(K_J^{\rm int}(\lambda)\), boundary kinetic and mass terms supply eigenvalue-dependent conditions, and the DeVries target is
\[
\Sigma_{hh,J}^{\rm int}=0,\qquad
\Sigma_{aa,J}^{\rm int}=J,\qquad
\Sigma_{ha,J}^{\rm int}\Sigma_{ah,J}^{\rm int}=J.
\]
The unresolved steps are the derivation of these three entries, the ordered electroweak assignment, and the scalar map \(u_-(J)\mapsto\mathcal F_{\rm KK}\).

**\(G_2\) refinement.** The local \(G_2\) route now has a parallel kernel:
\[
K_J^{G_2}(\lambda)=
\begin{pmatrix}
\lambda+\Sigma_{hh,J}^{G_2} & \Sigma_{ha,J}^{G_2}\\
\Sigma_{ah,J}^{G_2} & \lambda+\Sigma_{aa,J}^{G_2}
\end{pmatrix},
\]
with target
\[
\Sigma_{hh,J}^{G_2}=0,\qquad
\Sigma_{aa,J}^{G_2}=J,\qquad
\Sigma_{ha,J}^{G_2}\Sigma_{ah,J}^{G_2}=J.
\]
The unresolved steps are the derivation from singular gauge loci and Higgs-bundle data, the scalar map \(u_-(J)\mapsto\mathcal F_{G_2}\), and anomaly/global-form compatibility.

**Route-comparison refinement.** Sec. VI.G now places the endpoint, interval, and \(G_2\) routes into one kernel target:
\[
K_{J,r}(\lambda)=
\begin{pmatrix}
\lambda+\Sigma_{hh,J}^{r} & \Sigma_{ha,J}^{r}\\
\Sigma_{ah,J}^{r} & \lambda+\Sigma_{aa,J}^{r}
\end{pmatrix},
\qquad
r\in\{\mathrm{end},\mathrm{int},G_2\}.
\]
The shared acceptance criterion is
\[
\Sigma_{hh,J}^{r}=0,\qquad
\Sigma_{aa,J}^{r}=J,\qquad
\Sigma_{ha,J}^{r}\Sigma_{ah,J}^{r}=J,
\]
plus the ordered electroweak map, pole placement, negative-branch scalar map, and global checks.  The next proof-level pass should derive one of these entries from source data.

## O8. Pole placement versus high-scale placement

**Question.** Why does the clean DeVries value attach to the low-energy pole spectrum, and how are GUT-scale or compactification-scale boundary readings separated?

**Current working idea.** The pole reading gives the spectral language its electroweak content. The GUT lineage provides the comparison class: clean weak-angle values such as \(3/8\) are high-scale structural data related to experiment by running.

**Success criterion.** Identify a dynamical object whose eigenvalue or pole condition is naturally evaluated at the W/Z pole spectrum, or else move the construction to a high-scale boundary interpretation.

**Ledger refinement.** Sec. VI.A now splits the problem into four arrows:
\[
\mathcal S\to\mathcal O_J\to\mathcal M_J\to\{x_\pm(J)\}\to
(\sin^2\theta_{\rm pole},\mathcal F_{\rm sc},\mathcal C_{\rm top}).
\]
The exact algebra covers the branch arrow. The source-theory, two-channel reduction, and physical-assignment arrows remain open.

## O5. Electroweak ray and forbidden deformations

**Question.** How does the construction encode the full broken-to-unbroken electroweak ray while avoiding independent unphysical limits?

**Current working idea.** The vacuum scale \(v\) is radial; the DeVries ratio fixes the projective direction. Taking \(v\to0\) restores the full gauge symmetry with the projective ratio held fixed.

**Success criterion.** A precise statement in the gauge-Higgs Lagrangian and the mass matrix.

## O6. Flavor boundary

**Question.** How should the Rivero flavor/endpoint material be represented while keeping generation-topology claims conditional?

**Current working idea.** State SO(32)-flavor as a separate organizing clue compatible or incompatible with compactification topology.

**Success criterion.** A section that gives the boundary condition and prevents overclaiming.

## O7. Global form of the Standard Model gauge group

**Question.** Can line operators or global-form data provide a topological test connected to the DeVries construction?

**Current working idea.** Include as a topological appendix and possible discriminant, separate from the mass-ratio derivation.

**Success criterion.** A clear appendix explaining \((SU(3)\times SU(2)\times U(1))/\Gamma\), \(\Gamma\subset \mathbb Z_6\), and the exact relation to possible tests.

## O9. Theorem-target ledger

**Question.** Can the manuscript state every open derivation as a theorem target with explicit hypotheses, conclusion, source status, and failure mode?

**Current working idea.** Add a formal appendix collecting the pole-placement, electroweak-assignment, boundary-determinant, negative-branch, and global-form compatibility targets.

**Success criterion.** A referee can locate the exact missing proof for each speculative step and see which manuscript claim depends on it.

**Status-ledger refinement.** Sec. IX now adds a claim hierarchy, minimum viable derivation chain, route-selection ledger, and referee-facing tests.  The compiled draft reached 62 pages; the remaining burden is derivational rather than architectural.
