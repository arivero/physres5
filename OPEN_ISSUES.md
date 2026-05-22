# Open analytical issues

## O1. Derive the W/Z assignment

**Question.** Why does the charged W comparison sample \(J=3/4\) while the neutral Z comparison samples \(J=2\)?

**Current working idea.** The \(J=2\) datum has an adjoint-current reading through the \(SU(2)_L\) gauge sector. The \(J=3/4\) datum belongs to the Higgs/order-parameter doublet side. The missing step is the ordered sampling rule that turns \((J_H,J_{\rm adj})=(3/4,2)\) into the W/Z quotient.

**Success criterion.** A derivation from the gauge-Higgs sector that yields the ordered pair \((J_W,J_Z)=(3/4,2)\) directly and rules out post-selection.

**Parent-workspace refinement.** The `../weak` critique turns this into a
mass-map theorem.  The assignment must pass through a gauge-Higgs mass matrix,
pole self-energy map, or equivalent source-theory reduction.  SO(32) flavor
bookkeeping supplies the ordered pair only after an electroweak-operator
coupling: the adjacent audit places triplet data in adjoint branches and
weak-doublet data in spinor branches, so the flavor ledger needs a coupling to
the electroweak operator.

**Loop 11 normalization refinement.** The ordered assignment must specify the
mathematical channel by which \(J_H=3/4\) enters the charged comparison.  The
allowed channels are: a Higgs-representation contribution inside the
gauge-Higgs mass map, a scalar contribution to the W transverse pole
self-energy, or a source/boundary label coupled to the Higgsing field.  The
target mass-map equation is
\[
(D_\mu H)^\dagger D^\mu H
\longrightarrow
\left(M_W^2,M_Z^2\right)
=
\left(\frac{g^2v^2}{4},\frac{(g^2+g'^2)v^2}{4}\right)
\longrightarrow
\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2}
=
\frac{x_+(C_2(\mathbf 2))}{x_+(C_2(\mathrm{adj}))}.
\]

**Loop 12 theorem-target refinement.** Appendix D Target 0 and Target II now
place the ordered assignment inside a unified source-to-pole theorem.  The
assignment is accepted only after the same reduced field basis supplies the
source kernel, the maps
\[
P_W:\ h_J\mapsto C_2(\mathbf 2),\qquad
P_Z:\ a_J\mapsto C_2(\mathrm{adj}),
\]
and the transverse-pole matching chain.  Interval, endpoint, and \(G_2\)
versions are variants of this same sampling theorem.

## O2a. Pole convention formula

**Question.** Which exact pole convention defines \(M_{V,\rm pole}\) in the W/Z comparison?

**Current working idea.** Use complex pole positions for the descriptive low-energy spectral clue. Treat Breit-Wigner/on-shell and running weak angle inputs as scheme transformations. The manuscript currently writes
\[
s_V=M_{V,\rm pole}^2-iM_{V,\rm pole}\Gamma_{V,\rm pole},
\qquad
\Delta^{-1}_{T,V}(s_V)=0.
\]
The remaining convention task is to state the exact relation to the quoted variable-width Breit--Wigner parameters used for W and Z inputs.

**Success criterion.** A source-backed formula section states the complex-pole convention, the Breit--Wigner translation, and the conditions under which \(M_{V,\rm BW}^2=M_{V,\rm pole}^2+\Gamma_{V,\rm pole}^2\) is used.

**Round 3 refinement.** Sec. III now fixes the \(s_V=M_{V,\rm pole}^2-iM_{V,\rm pole}\Gamma_{V,\rm pole}\) parameterization, records the alternative \(s_{\rm pole}=(M-i\Gamma/2)^2\) convention as a translation target, and states the common variable-width Breit--Wigner conversion chain before \(\sPole\) is formed. The remaining work is a current W/Z input audit in O2b.

## O2b. Current electroweak input audit

**Question.** What current source-audited W/Z inputs should be used for a descriptive pole-ratio comparison?

**Current working idea.** Keep the inherited numerical arithmetic as provenance in the appendix while the body defers a current comparison. The CDF-II comparison remains descriptive until all inputs share a pole convention and propagated uncertainty.

**Success criterion.** A table with source, quoted convention, quoted masses and widths, converted pole masses, uncertainty propagation, and the resulting \(\sin^2\theta_{\rm pole}\). This belongs to a later calculation phase approved by the user.

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

**Parent-workspace refinement.** The signed-root mechanism notes give a useful
EFT obstruction template:
\[
V_{\rm eff}\supset
\frac12\Psi_-^T
\left[m_-^2{\bf 1}+c_Yg'^2(H^\dagger H)\sigma_3\right]\Psi_-,
\qquad
\Delta M_-^2=\frac{c_Yg'^2v^2}{2}\sigma_3 .
\]
This supplies a gauge-invariant form for a two-state negative sector.  The
physical identity of \(\Psi_-\), the coefficient \(c_Y\), and the map to
\(x_-(J)\) remain UV matching data.

**Loop 11 normalization refinement.** Route-specific scalar candidates in the
main text are source addresses.  They acquire physical status after a
gauge-invariant scalar functional, normalization, and electroweak scheme are
derived.

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

**Schur-complement refinement.** The advisor route adds a concrete reduction target. Let \(L_J\) be a tower, bulk, or heavy-sector operator coupled to a boundary light sector by \(V_J\). The effective boundary kernel is
\[
K^{\rm eff}_J(\lambda)
=K^{\rm bdry}_J(\lambda)
-V_J^\dagger(\lambda-L_J)^{-1}V_J .
\]
The unresolved derivation is a source-backed choice of \(K^{\rm bdry}_J\), \(L_J\), \(V_J\), and inner product such that
\[
K^{\rm eff}_J(\lambda)
\longrightarrow
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix}.
\]
This route should be tested first against interval boundary kinetic terms and brane-localized Higgsing data in the Csaki--Hubisz--Meade fragments.

**Dimensional Schur-complement refinement.** Round 2 makes this the active
O10/O4 bridge.  The \(D=10/6\) middle line is represented by a light boundary
sector \(\mathcal H_J=\operatorname{span}\{h_J,a_J\}\), a heavy or compact
operator \(L_J\), a boundary kernel \(K^{\rm bdry}_J(\lambda)\), and a coupling
map \(V_J\).  The required reduction is
\[
K^{\rm eff}_J(\lambda)
=K^{\rm bdry}_J(\lambda)
-V_J^\dagger(\lambda-L_J)^{-1}V_J
\longrightarrow
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix}.
\]
The next proof step is to identify \(K^{\rm bdry}_J\), \(L_J\), \(V_J\), the
inner product, and the decoupling or block-diagonal treatment of additional
light channels.

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

**prTalks Regge/source-note refinement.** The adjacent `../prTalks` PDFs add two Regge-compatible theorem targets. The intercept version treats \(j\) as a sector label and adds an oscillator \(n\):
\[
M_{n,j,\pm}^2=\mu^2x_{j,\pm}+\frac{n}{\alpha'},
\qquad
J=n+j .
\]
The product version keeps the exact invariant
\[
x_+(J)x_-(J)=-J,
\qquad
-M_+^2M_-^2=\mu^4J .
\]
Both remain obligations until a worldsheet, boundary, Kaluza--Klein, or \(G_2\) operator derives the DeVries block and identifies the branch status.

**Parent-workspace normalization audit.** Adjacent `../weak` mechanism notes
show that \(\sqrt{C_2}\), \(C_2\), and the common normalization require one
source-theory explanation.  Any endpoint, interval, brane, KK, Regge, or
\(G_2\) route must derive
\[
\Sigma_{hh,J}=0,\qquad
\Sigma_{aa,J}=J,\qquad
\Sigma_{ha,J}\Sigma_{ah,J}=J
\]
from one operator, field basis, and inner product.  Hosotani/Wilson-line
weight-squared spectra, single-generator Wigner--Eckart elements, and free
Wilson coefficients are failure modes to test explicitly.

**Loop 11 normalization refinement.** Comparing endpoint, interval, and \(G_2\)
\(\Sigma\)-entries requires one stated field basis and inner product for the
reduced two-channel light space.  Extra channels, nonorthogonal projections,
or route-dependent normalizations must be handled before the entries can be
identified across routes.

**Loop 12 theorem-target refinement.** Appendix D Target 0 promotes the common
route requirement to a source-to-pole matching theorem:
\[
\mathcal S_r\to\mathcal H_{J,r}\to K^{\rm eff}_{J,r}(\lambda)
\to \Pi^{(4)}_{T,V}(s;J,r)\to
\Delta^{-1}_{V,T}(s_V;J,r)=0.
\]
The Schur-complement version must specify \(K^{\rm bdry}_{J,r}\), \(L_{J,r}\),
\(V_{J,r}\), \(\langle\cdot,\cdot\rangle_r\), \(P_{J,r}\), and the
decoupling or block-diagonal treatment of additional light channels.  A
route comparison is meaningful only inside that one basis and normalization.

## O8. Pole placement versus high-scale placement

**Question.** Why does the clean DeVries value attach to the low-energy pole spectrum, and how are GUT-scale or compactification-scale boundary readings separated?

**Current working idea.** The pole reading gives the spectral language its electroweak content. The GUT lineage provides the comparison class: clean weak-angle values such as \(3/8\) are high-scale structural data related to experiment by running.

**Success criterion.** Identify a dynamical object whose eigenvalue or pole condition is naturally evaluated at the W/Z pole spectrum, or else move the construction to a high-scale boundary interpretation.

**Chain refinement.** Sec. VI.A now splits the problem into four arrows:
\[
\mathcal S\to\mathcal O_J\to\mathcal M_J\to\{x_\pm(J)\}\to
(\sin^2\theta_{\rm pole},\mathcal F_{\rm sc},\mathcal C_{\rm top}).
\]
The exact algebra covers the branch arrow. The source-theory, two-channel reduction, and physical-assignment arrows remain open.

**Matching-theorem refinement.** Round 2 makes the pole-placement theorem a
three-arrow matching chain:
\[
\mathcal S_r
\longrightarrow
K_{J,r}^{\rm bare}(\lambda)
\longrightarrow
\Gamma_{\rm eff}^{(4)}[H,W,B]
\longrightarrow
\Delta^{-1}_{V,T}(s)\big|_{s=s_{W,Z}} .
\]
The first arrow is route-specific source reduction.  The second arrow is
four-dimensional effective matching.  The third arrow is the dressed transverse
pole condition.  The pole reading requires all three arrows in one scheme.

**Round 3 refinement.** Sec. VI.G and Appendix D now state the same burden as a pole self-energy matching theorem:
\[
K_{J,r}^{\rm bare}(\lambda)
\longrightarrow
\Pi_{T,V}^{(4)}(s;J,r),
\qquad
\Delta^{-1}_{T,V}(s_V;J,r)=0 .
\]
If the clean quotient is derived at compactification or unification scale, the manuscript relocates the physical claim to that scheme and treats the pole comparison as descriptive motivation.

**Parent-workspace refinement.** The signed-root custodial no-go suggests a
concrete obstruction to test whenever \(3/8=C_F/C_A\) enters a negative-sector
or custodial explanation.  Usual electroweak breaking supplies
\[
M_Z^2-M_W^2=\frac{g'^2v^2}{4}
\]
through the hypercharge spurion \(T_R^3\).  A full SU(2) Casimir ratio requires
an additional UV threshold, charge lattice, or custodial-generator sum.  The
same standard applies to string and Regge variants: Chan--Paton traces,
hypercharge embeddings, and Regge \(C_F/C_A\) factors must be matched to the
four-dimensional pole condition.

**Loop 11 normalization refinement.** The pole-placement theorem must state
whether the DeVries determinant is preserved exactly under four-dimensional
matching or obtained after a projection, field redefinition, or
renormalization prescription.  The \(G_2\) route carries a specific scale
tension: local singularity data naturally live at a compactification scale, so
the pole reading requires a compactification-to-EFT-to-complex-pole matching
theorem.

**Loop 12 theorem-target refinement.** Target 0 joins O1, O4, and O8.  A
successful route must carry the determinant through the reduced kernel and
then into the transverse self-energy in the pole scheme.  If a projection,
field redefinition, or renormalization prescription changes the determinant,
the manuscript must state the changed object and its matching law.  The
\(G_2\) route keeps the compactification-to-EFT-to-complex-pole theorem as a
named unresolved obligation.

## O5. Electroweak ray and forbidden deformations

**Question.** How does the construction encode the full broken-to-unbroken electroweak ray while avoiding independent unphysical limits?

**Current working idea.** The vacuum scale \(v\) is radial; the DeVries ratio fixes the projective direction. Taking \(v\to0\) restores the full gauge symmetry with the projective ratio held fixed.

**Success criterion.** A precise statement in the gauge-Higgs Lagrangian and the mass matrix.

**Loop 13 rank-and-ray refinement.** Appendix D now states O5 as an
electroweak ray admissibility theorem.  The tree-level ray is
\[
H_t=\frac{1}{\sqrt2}\binom{0}{t v+h},
\qquad
g(t)=g,\qquad g'(t)=g',
\]
with
\[
M_W^2(t)=t^2\frac{g^2v^2}{4},
\qquad
M_Z^2(t)=t^2\frac{(g^2+g'^2)v^2}{4},
\qquad
M_\gamma^2(t)=0.
\]
A source route is ray-admissible when one radial parameter controls the charged
and neutral massive vector sectors, the photon remains the null mode, and the
ordered sampling maps commute with the \(t\to0\) limiting projective datum.
Coupling-space paths such as \(g\to0\), \(g'\to0\), \(g'/g\to0\), and
custodial-breaking mass shifts are separate deformation problems.

## O6. Flavor boundary

**Question.** How should the Rivero flavor/endpoint material be represented while keeping generation-topology claims conditional?

**Current working idea.** State SO(32)-flavor as a separate organizing clue compatible or incompatible with compactification topology.

**Success criterion.** A section that gives the boundary condition and prevents overclaiming.

**Parent-workspace refinement.** Adjacent SO(32) notes are useful as flavor
boundary provenance.  The current safe use is representation bookkeeping:
adjoint branches can supply triplet-like data, spinor branches can supply
doublet-like data, and orientifold/orbifold projection data are needed for
branch selection.  Generation-topology claims stay inside the existing caveat
until a compactification map and global-form check are supplied.

## O7. Global form of the Standard Model gauge group

**Question.** Can line operators or global-form data provide a topological test connected to the DeVries construction?

**Current working idea.** Include as a topological appendix and possible discriminant, separate from the mass-ratio derivation.

**Success criterion.** A clear appendix explaining \((SU(3)\times SU(2)\times U(1))/\Gamma\), \(\Gamma\subset \mathbb Z_6\), and the exact relation to possible tests.

## O9. Theorem-target ledger

**Question.** Can the manuscript state every open derivation as a theorem target with explicit hypotheses, conclusion, source status, and failure mode?

**Current working idea.** Add a formal appendix collecting the pole-placement, electroweak-assignment, boundary-determinant, negative-branch, and global-form compatibility targets.

**Success criterion.** A referee can locate the exact missing proof for each speculative step and see which manuscript claim depends on it.

**Status refinement.** Sec. IX now presents the conclusion and analytical status, while Appendix D holds the claim hierarchy, minimum derivation chain, and derivation checklist. The remaining burden is derivational.

**Loop 12 refinement.** Appendix D now begins with Target 0, the unified
source-to-pole matching theorem.  The theorem-target ledger therefore has a
lead object that packages the source reduction, reduced basis, DeVries kernel,
ordered W/Z sampling maps, and pole matching before the route-specific targets
are compared.

## O10. Higgs interpolation \(D=11\to D=10\to D=9\) and colourless \(D=7\to D=6\to D=5\)

**Question.** Can the Higgs/electroweak sector be reconstructed as an interpolation whose full-gauge version has total dimensions \(D=11,10,9\) and KK internal dimensions \(7,6,5\), while its colourless electroweak version has total dimensions \(D=7,6,5\) and KK internal dimensions \(3,2,1\)?

**Local source trail.** The closest local ChatGPT/source note is `/home/codexssh/phys3/sources/unbroken_susy.md`, Section V, lines 69--71. It records the claim that D=11 lacks the required electroweak chirality and that electroweak \(SU(2)\times U(1)\) interpolates, under a W-mass deformation, between descriptions labeled d=9 and D=11. Witten's KK fragments give the primary source trail: `context/source_fragments/witten1981/pages_001-010.md` states the seven-extra-dimensional minimum for \(SU(3)\times SU(2)\times U(1)\), and `context/source_fragments/witten1981/pages_011-017.md` states the associated fermion quantum-number obstruction. The same Witten fragment contains the \(SU(3)\times U(1)\) symmetry address around the five-dimensional sphere construction.

**Current working idea.** Treat this as a source-audit and reconstruction task. The massless-Higgs or unbroken-electroweak limit carries the full \(SU(3)\times SU(2)\times U(1)\) symmetry and belongs to Witten's seven-extra-dimensional KK setting, hence total \(D=11\). The formal infinite-Higgs or infinitely broken limit leaves \(SU(3)\times U(1)_{\rm em}\) and belongs to a five-extra-dimensional KK setting, hence total \(D=9\). The working DeVries construction should be tested as an internal six-dimensional interpolation between those endpoints, hence total \(D=10\). In this form the model may avoid Witten's seven-dimensional fermion obstruction because its physical interior point carries six extra dimensions and the Witten obstruction applies to the seven-extra-dimensional unbroken compactification.

**Colourless electroweak count.** If colour is treated as an external spectator sector, the corresponding count is
\[
n_{\rm KK}^{\rm ew}=3:\ SU(2)\times U(1),
\qquad
n_{\rm KK}^{\rm ew}=2:\ \hbox{DeVries electroweak interpolation sector},
\qquad
n_{\rm KK}^{\rm ew}=1:\ U(1)_{\rm em}.
\]
This gives the total-dimensional chain \(D=7\to D=6\to D=5\). The middle \(D=6\) case has a string-theory source trail through six-dimensional superstring vacua and dualities, including type IIA on K3, heterotic on \(T^4\), and six-dimensional anomaly/string-universality constraints. The colour-inclusive \(D=11\to D=10\to D=9\) chain remains the canonical narrative when the full \(SU(3)\) colour factor is kept inside the KK symmetry count.

**Top-quark subquestion.** The interpolation should also explain why the top quark sits at the electroweak scale. In Standard Model source language, fermion masses arise from Yukawa couplings to the Higgs vev, the top has the largest Higgs coupling, and top loops strongly affect Higgs production and vacuum stability. The DeVries version of the question is whether the six-dimensional interior or the negative-branch scalar datum selects the top as the fermion most directly tied to the electroweak order parameter.

**Required reconstruction.**

1. Define the seven-extra-dimensional endpoint: field content, \(SU(3)\times SU(2)\times U(1)\) symmetry, Witten fermion obstruction, and massless-Higgs or unbroken-electroweak limit.
2. Define the five-extra-dimensional endpoint: \(SU(3)\times U(1)_{\rm em}\), compact-space candidate, fermion statement, and infinite-Higgs or infinitely broken limit.
3. Define the six-extra-dimensional interior model: gauge group, scalar/order-parameter variable, compactification data, and relation to Witten's seven-dimensional fermion obstruction.
4. State the interpolation parameter in the gauge-Higgs Lagrangian, boundary condition, or compactification data.
5. Relate the interpolation to the current DeVries branch language, especially the role of \(x_-(J)\) as a possible scalar/order-parameter datum.
6. Give the colourless electroweak \(3/2/1\) count and specify when colour is a spectator sector.
7. Connect the top Yukawa/electroweak-scale fact to the interpolation, or record that the interpolation has no derived top-sector consequence.
8. Identify primary sources for each endpoint before any manuscript claim is promoted beyond conjecture.

**Success criterion.** A manuscript subsection or appendix gives a source-backed endpoint dictionary
\[
n_{\rm KK}=7:\ SU(3)\times SU(2)\times U(1),
\qquad
n_{\rm KK}=6:\ \hbox{DeVries interpolation sector},
\qquad
n_{\rm KK}=5:\ SU(3)\times U(1)_{\rm em},
\]
plus the colourless electroweak dictionary
\[
n_{\rm KK}^{\rm ew}=3:\ SU(2)\times U(1),
\qquad
n_{\rm KK}^{\rm ew}=2:\ \hbox{DeVries electroweak interpolation sector},
\qquad
n_{\rm KK}^{\rm ew}=1:\ U(1)_{\rm em}.
\]
The same subsection must give a precise interpolation map compatible with the electroweak ray, the ordered \((J_H,J_{\rm adj})=(3/4,2)\) assignment problem, the negative-branch scalar target, and the top-quark electroweak-scale subquestion.

**Round 2 refinement.** Appendix E now states a source-status table and a
commutative compatibility diagram.  Appendix D now includes Target VI:
dimensional interpolation.  The middle-dimensional data required at a DeVries
point are
\[
\mathfrak I_J(t_\star)
=
\big(
\mathcal B(t_\star),\,
\mathcal H_J(t_\star),\,
K_J(t_\star,\lambda),\,
\mathcal R_{\rm pole}
\big),
\qquad
\mathcal H_J(t_\star)=\operatorname{span}\{h_J,a_J\}.
\]
Thus the \(D=10\) and colourless \(D=6\) middle lines are active
reconstruction targets: they must provide a compact, boundary, or singular
object \(\mathcal B\), the two-channel light subspace, the DeVries kernel, and
the pole-matching rule.

**Parent-workspace refinement.** The parent `../phys3` files add provenance
for the D=11 chirality-obstruction language, the D=9/D=11 interpolation note,
and SO(32)/Chan--Paton counting.  Witten 1981 and the six-dimensional string
sources remain the controlling primary-source trail.  Parent projection notes
also require explicit boundary, orientifold, orbifold, or singular data when a
branch projection is invoked; Wilson-line data alone leave the projection
unresolved.

**Loop 12 theorem-target refinement.** Appendix D now states the source-backed
full-gauge endpoint as \((D,n_{\rm KK})=(11,7)\) with
\(SU(3)\times SU(2)\times U(1)\).  The \((9,5)\) endpoint is a reconstruction
target until the surviving \(U(1)\) is derived as \(U(1)_{\rm em}\).  The
\((10,6)\) and colourless \((6,2)\) middle lines are Schur-complement labels:
they name the required reduced source sector, light subspace, kernel, ordered
assignment, and pole-matching rule.  The endpoint dictionary depends on the
same electroweak assignment theorem recorded in O1.

**Loop 13 parameter refinement.** The electroweak ray parameter and the
dimensional interpolation parameter are distinct theorem data:
\[
t_{\rm EW}\equiv\hbox{gauge-Higgs radial coordinate},
\qquad
t_{\rm dim}\equiv\hbox{compact, boundary, brane, or singular coordinate}.
\]
A source theory must derive either a map
\[
\chi:\ t_{\rm dim}\mapsto t_{\rm EW}
\]
or a joint source variable \(u\mapsto(t_{\rm dim}(u),t_{\rm EW}(u))\).  A
dimensional family may still be useful when it derives a compactification
sector or a kernel, but control of the electroweak ray and pole ratio requires
this additional map.

## O11. Adjacent `prTalks` source-note validation

**Question.** Which user-provided `../prTalks` PDFs contain conceptual material that should survive into the manuscript program, and which claims require primary-source upgrades?

**Current working idea.** Treat the PDFs as project source notes. Keep the PDFs themselves as source objects, because text extraction misses plots, equation layout, radicals, and embedded images. Valid content includes the electroweak ray/projective-angle reading, the orbit quadratic, Reggeization alternatives, the minimal \(D_T\) two-channel block, the effective-dimension interpolation, and the negative-branch/top-sector obligation.

**Success criterion.** `context/prtalks_source_notes.md` and `notes/lean/PrTalks.lean` record the valid content, the PDF-reading caveat, the agent-read mathematical transcriptions, and the primary-source upgrade queue. Any promotion into manuscript prose must point back either to primary local literature or to an explicitly labeled project-source note.

## O12. Parent-workspace source-note validation

**Question.** Which adjacent parent-workspace text notes can sharpen the
manuscript while keeping adjacent-project overclaims out of journal-facing
prose?

**Current working idea.** Use `../weak` as a normalization and failure-mode
audit, `../phys3` as dimensional-interpolation and SO(32)/Chan--Paton
provenance, `../signed-dv-custodial-project` as negative-branch and string-UV
obstruction memory, and `../dualsm` as review-process discipline.  `../recap`
and `../orbits` remain outside current manuscript claims unless a later
source-specific task makes them relevant.

**Promoted obligations.**

1. Scalar-seed assignments to W/Z observables require a gauge-Higgs mass
   matrix, pole self-energy map, or equivalent source-theory reduction.
2. Negative-branch Higgs/top readings require a scalar potential,
   gauge-invariant scalar functional, or UV-matched two-state EFT.
3. Endpoint, interval, brane, KK, Regge, and \(G_2\) routes must produce the
   DeVries block from one operator and one normalization rule.
4. Custodial \(3/8=C_F/C_A\) explanations must supply an extra threshold,
   charge lattice, or generator-sum mechanism beyond the hypercharge
   \(T_R^3\) spurion.
5. SO(32)-flavor and Chan--Paton counts remain flavor-boundary provenance until
   a coupling to the electroweak operator is derived.

**Success criterion.** `context/parent_workspace_source_notes.md` and
`notes/lean/AdjacentWorkspaceGuardrails.lean` record the audited content and
the theorem targets.  Parent-derived claims promoted to manuscript prose must
carry either primary-source support or an explicit project-source label.

## O13. Casimir keyword load versus derivational role

**Provenance.** Human operator note (2026-05-22), added out of band while the
loop runs.  Treat as a directive, not auto-generated content.

**Question.** Does the manuscript over-weight the keyword "Casimir" in its
framing relative to the work that the Casimir structure actually does?

**Observation.** The word appears about fifteen times in roughly seventeen
thousand body words, and it is concentrated in the title and the
Sec.~II operator name.  The body is carried by `pole` (\(\sim\)238), `g_2`
(\(\sim\)118), `higgs` (\(\sim\)102), `string` (\(\sim\)99), and `brane`
(\(\sim\)97), while the physical target, the weak mixing angle, is named about
eleven times.  The construction derives nothing from a Casimir operator: only
the input number \(J=s(s+1)\) is a quadratic-Casimir eigenvalue, and the matrix
\(Q(J)\) is an ansatz fed by that number.  The branch \(s=\tfrac12\to J=\tfrac34\)
and \(s=1\to J=2\) is the one place the Casimir reading carries weight, and that
identification is exactly the unproven ordered-assignment target O1.

**Internal corroboration.** The loop-13 Referee~B report lists \(J\) as a
"Casimir/current datum, overlap product, or compactification charge with one
normalization," i.e. one of three interchangeable readings of the same number.
This matches the project stance in `AGENTS.md` and `PROJECT_BRIEF.md`, where
Casimir language is a construction and historical clue and the physics is to
come from electroweak, string, brane, Kaluza--Klein, or \(G_2\) mechanisms.

**Risk.** A title led by "Casimir" collides with the Casimir effect, misdirects
referee and index search away from the electroweak pole-ratio subject, and
foregrounds a clue over the observable.

**Current working idea.** Demote Casimir to a labeled clue inside Sec.~II,
foreground the secular/orbit quadratic and the pole-ratio observable, and state
explicitly in Sec.~II that only \(J=s(s+1)\) enters as a Casimir eigenvalue
while \(Q(J)\) is an ansatz awaiting a source-theory derivation (Target~0, O4).
A candidate retitle: "A Secular Mass-Ratio Construction for the Electroweak
Pole Spectrum and Its String/Kaluza--Klein Interpretation."

**Success criterion.** The title and the Sec.~II heading no longer lead with
Casimir, Sec.~II states the ansatz status and the single Casimir-eigenvalue
input, the abstract names the weak mixing angle / pole ratio, and the Casimir
lineage survives as a cited historical clue.
