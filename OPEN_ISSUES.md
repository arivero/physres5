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

**Loop 24 superconnection refinement.** The active O1 test uses an
electroweak-superconnection assignment,
\[
P_W:\Phi_{\rm odd}\mapsto J_H=\frac34,\qquad
P_Z:F_{\rm even}^{\gamma^\perp}\mapsto J_{\rm adj}=2,
\]
with one gauge-Higgs complex, one inner product, and one pole-matching map.
The comparison has to take the form
\[
\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2}
=
\frac{x_+(J_H)}{x_+(J_{\rm adj})}
+\Delta_{\rm sc}.
\]
The exact pole statement requires a derived value for \(\Delta_{\rm sc}\).
The local source address is Coquereaux's \(SU(2|1)\) superconnection fragments
in `context/source_fragments/50_coquereaux_algebraic_superconnections_su2_1_electroweak_1992/`;
Appendix D Target X records the theorem version.

**Loop 28 normalization refinement.** The ordered W/Z assignment also requires
a common dimensionless source normalization for the \(J_H=3/4\) and
\(J_{\rm adj}=2\) samples.  The active CHM version introduces a source scale
\(\Lambda_J\) and hatted spectral variable
\(\widehat\lambda=\lambda/\Lambda_J^2\).  The same source scale, field
normalization, and pole map must apply to the odd Higgs/order-parameter channel
and the even transverse-current channel before their quotient has physical
meaning.

**Loop 33 ordered-sampling refinement.** The O1 success criterion is now a
single source package
\[
u_{\rm EW}\mapsto
\big(
\mathcal H_J,\langle\cdot,\cdot\rangle_{u_{\rm EW}},
\Lambda_J,P_W,P_Z,P_\gamma,\mathcal R_{\rm pole},\mathcal F_{\rm sc}
\big)
\]
with
\[
P_W(h_J)=J_H=\frac34,\qquad
P_Z(a_J^{\gamma^\perp})=J_{\rm adj}=2,\qquad
P_\gamma(a_\gamma)=0.
\]
The CHM interval version must define \(P_{h,J}\), \(P_{a,J}^{\gamma^\perp}\),
\(P_W\), \(P_Z\), \(K^{\rm ref}_{T,J}\), \(\Lambda_{\rm CHM}\), endpoint signs,
and the pole map in one ledger.  Coquereaux supplies generalized-connection
grading vocabulary; CHM supplies the active source-controlled normalization
arena.  The issue stays open until
\[
\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2}
=
\frac{x_+(J_H)}{x_+(J_{\rm adj})}
+\Delta_{\rm O1}
\]
has a derived \(\Delta_{\rm O1}\) or a stated source remainder.

## O2b. Current electroweak input audit

**Question.** What current source-audited W/Z inputs should be used for a descriptive pole-ratio comparison?

**Current working idea.** Keep the inherited numerical arithmetic as provenance in the appendix while the body defers a current comparison. The CDF-II comparison remains descriptive until all inputs share a pole convention and propagated uncertainty.

**Success criterion.** A table with source, quoted convention, quoted masses and widths, converted pole masses, uncertainty propagation, and the resulting \(\sin^2\theta_{\rm pole}\). This belongs to a later calculation phase approved by the user.

## O3. Negative branch and Higgs scale

**Question.** Does \(x_-(J)\) encode the Higgs/order-parameter scale, a tachyonic mass term, or an auxiliary branch?

**Current working idea.** The negative root is the main conceptual reason the
numerical clue remains interesting: under the vector-spectrum normalization,
the two negative magnitudes point toward scalar/order-parameter scales.  The
scalar-sector map must be gauge-invariant, scheme-controlled, and derived from
the same source reduction as the positive branch.

**Success criterion.** A same-source scalar package
\[
u\mapsto
\big(
\mathcal H_J,\langle\cdot,\cdot\rangle_u,P_J,\Lambda_J,
\mathcal R_{\rm pole},\mathcal F_{\rm sc}
\big)
\]
with source-fixed \(J_\star\), normalization \(C_{\rm sc}\), scheme/scale,
mass dimension, and pole-vs-potential status, connecting \(x_-(J_\star)\) to
\(\mu_H^2\), \(\lambda v^2\), \(v\), a Higgs pole observable, a Wilson-line
curvature, a boundary modulus, or a compactification eigenvalue.

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

**Loop 32 refinement.** The priority route is the interval
gauge-Higgs/Hosotani target
\[
\mathcal F_{\rm sc}^{\rm Hol}
=
\left.
\frac{\partial^2 V_{\rm eff}(\alpha_H;\Lambda,s_{\rm ren})}
     {\partial\alpha_H^2}
\right|_{\alpha_H=\alpha_\star},
\qquad
\alpha_H\sim g_5\int_I dy\,A_5,
\]
derived from the same \(\mathcal H_J\), inner product, projection, scale, and
boundary determinant as the vector pole quotient.  If the negative eigenvector
projects to auxiliary or gauge-fixed data, O3 resolves as an auxiliary-branch
outcome and the Higgs-sector claim leaves the conclusion.

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

**Loop 21 source-pack refinement.** Bucci and Haba--Oda support scalar-modulus,
radion, Dirichlet-Higgs, and boundary-Higgs address candidates for O3/O10.
Hosotani supports a compact gauge-field or Wilson-line scalar candidate.
Breitenlohner--Freedman supply an AdS boundary-condition caveat for negative
mass-squared scalar modes; the DeVries negative branch still requires a
route-specific scalar functional and normalization theorem.

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

**Dirichlet-to-Neumann interval refinement.** Loop 19 sharpens the interval
route into a source-data theorem target.  CHM supplies boundary kinetic data,
modified scalar products, vector Robin data from boundary scalar vevs, and
\(A_5/\pi_i\) scalar boundary equations.  The reduced target is
\[
K^{\rm int}_J(\lambda)
=
P_J^\dagger
\left(K^{\rm DtN}_J(\lambda)+K^{\rm brane}_J(\lambda)\right)P_J
\longrightarrow
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix}.
\]
The unresolved step is the source-backed choice of \(K^{\rm DtN}_J\),
\(K^{\rm brane}_J\), \(P_J\), the CHM inner product, and the decoupling or
block form of extra interval modes.

**Eaten-Goldstone boundary-kernel refinement.** Loop 20 asks whether the CHM
gauge-fixed interval system can put the vector pole clue and scalar partner in
one boundary kernel:
\[
S_{5D}[A_M,\Phi_i]
\xrightarrow{\delta S,\mathcal G_\xi}
\left(K_T^{\partial I}[A_\mu],K_{A_5\pi}^{\partial I}\right)
\xrightarrow{P_J^\dagger(\cdot)P_J}
K_J^{\rm eaten}(\lambda)
\longrightarrow
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix}.
\]
The open data are the projection \(P_J\), the CHM product, the \(J\)
normalization, the photon zero mode, the ordered W/Z boundary map, and the
matching of \(K_J^{\rm eaten}\) to the pole scheme.

**Loop 21 interval source-pack refinement.** The active CHM route now uses the
boundary trace variables
\[
h_J\sim P_J(\pi_i,A_5,\delta v,\delta R,\theta_H),
\qquad
a_J\sim P_J(A_\mu^{\rm bdry}),
\]
with \(v_i\) boundary Higgs data, \(R\) an interval/radion datum, and
\(\theta_H\) a Hosotani/Wilson-line phase.  The source-controlled square is
\[
(v_0,v_L,R_0,\theta_H)
\to
\left(K_T^{\partial I},K_{A_5\pi}^{\partial I}\right)
\to K_J^{\rm eaten}(\lambda)
\to \Pi^{(4)}_{T,V}(s;J).
\]
The next proof step is derivation of at least one entry, preferably
\(\Sigma_{aa,J}=J\), from the boundary operator and inner product, with
gauge-fixing parameter treatment, physical-scalar/eaten-mode separation,
photon zero-mode preservation, and \(\lambda\mapsto m_n^2\mapsto\Pi_T(s)\)
supplied.

**Loop 27 current-entry normalization refinement.** The CHM current-channel
test now has a normalized extraction:
\[
K^{\rm cur}_J(\lambda)
=
\left\langle a_J,
\left(K^{\rm DtN}_{T,J}(\lambda)
+K^{\rm brane}_{T,J}(\lambda)-K^{\rm ref}_{T,J}(\lambda)\right)a_J
\right\rangle_{\rm CHM},
\qquad
\langle a_J,a_J\rangle_{\rm CHM}=1.
\]
The first entry target is
\[
K^{\rm cur}_J(\lambda)=
\lambda+\Sigma_{aa,J}^{\rm CHM}
+O(\lambda^2/\Lambda_{\rm KK}^2),
\qquad
\Sigma_{aa,J}^{\rm CHM}=J.
\]
The open data are the transverse projection \(P_{a,J}\), the reference
subtraction \(K^{\rm ref}_{T,J}\), endpoint-normal conventions, the
dimensionless \(J\)-normalization, photon projection, ordered W/Z boundary map,
and \(\lambda\mapsto m_n^2\mapsto\Pi_T^{(4)}(s)\) matching.

**Loop 28 convention and entry-order refinement.** The CHM current-channel
target must be written in hatted variables:
\[
\widehat\lambda=\frac{\lambda}{\Lambda_J^2},
\qquad
\widehat K^{\rm cur}_J
=
\Lambda_J^{-2}K^{\rm cur}_J .
\]
The theorem must derive \(\Lambda_J\), the CHM normalization of \(a_J\),
endpoint-normal signs, the reference subtraction, and the condition that the
same dimensionless normalization applies to \(J_H=3/4\) and
\(J_{\rm adj}=2\).  The active proof spine separates two entry tests:
Hodge/SUSY-QM factorization targets
\(\Sigma_{ha,J}\Sigma_{ah,J}=J\), and the hatted CHM current kernel targets
\(\widehat\Sigma_{aa,J}^{\rm CHM}=J\).  A source-control audit is still needed:
inspect the rendered CHM PDF for endpoint signs, dimensions of boundary
kinetic terms, scalar-product normalization, and the variables entering
\(K^{\rm brane}_{T,J}\).

**Loop 30 rendered CHM convention refinement.** The rendered CHM audit turns
the hatted current entry into a pass/fail source theorem.  Source facts now
include the boundary kinetic term and \(M_i^{-1}\) endpoint product, the
eigenvalue-dependent scalar boundary condition, vector Robin data, the
\(A_5/\pi_i\) scalar boundary equations, and photon/custodial boundary
bookkeeping.  The next derivation must determine
\[
K^{\rm ref}_{T,J},\qquad P_\gamma,\qquad P_{a,J},\qquad
\Lambda_{\rm CHM}
\]
from the same source data before using
\[
\widehat\Sigma_{aa,J}^{\rm CHM}
=
\Lambda_{\rm CHM}^{-2}
\left[
\langle a_J,K_{T,J}(0)a_J\rangle_{\rm CHM}
-
\langle a_\gamma,K_{T,J}(0)a_\gamma\rangle_{\rm CHM}
\right]
=J .
\]
This keeps O4 tied to O1 for the ordered W/Z boundary map, O8 for
source-to-pole matching, O10 for the single source variable and
\(\Lambda_J(u)\), and O20 for the common reduced basis with the Hodge
off-diagonal test.  Issue status remains open.

**Loop 34 source-kernel theorem refinement.** The first O4 pass/fail theorem is
now the hatted CHM current entry:
\[
\mathfrak D_{\rm O4}^{\rm CHM}
=
(I,g_5,K_T^{\rm DtN},K_T^{\rm brane},
\langle\cdot,\cdot\rangle_{\rm CHM},
P_\gamma,P_{a,J},K^{\rm ref}_{T,J},\Lambda_{\rm CHM},\mathcal R_{\rm pole}),
\]
with source equations audited from CHM Eqs.~(2.11)--(2.23),
(2.30)--(2.44), and (3.32)--(3.43).  The theorem target is
\[
\widehat K^{\rm cur}_J(\widehat\lambda)
=
\widehat\lambda+\widehat\Sigma_{aa,J}^{\rm CHM}
+O(\widehat\lambda^2),
\qquad
\widehat\Sigma_{aa,J}^{\rm CHM}=J .
\]
The companion O20 target is the Hodge/SUSY-QM square-root entry
\[
D_Je^0_J=\sqrt J\,e^1_J,\qquad
D_J^\dagger e^1_J=\sqrt J\,e^0_J,
\qquad
\Sigma_{ha,J}\Sigma_{ah,J}=J.
\]
Endpoint/Chan--Paton is now recorded as a matrix arena requiring a worldvolume
quadratic kernel and projection.  The \(G_2\) route is recorded as a local
operator audit with source equations
\[
\Phi=\sum_i t_i df_i,\quad \rho=\sum_i t_i\rho_i,\quad
f_Q=\sum_i q_i f_i,\quad \rho_Q=\sum_i q_i\rho_i,\quad df_Q(p)=0.
\]
O4 remains tied to O1 through \(P_W,P_Z,P_\gamma\), to O3 through the
same-source scalar package for \(u_-(J)\), to O8 through
\(\Delta_{\rm match}^{(r)}\), to O10 through \(u\) and \(\Lambda_J(u)\), and
to O20 through the common reduced basis.

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

**Loop 20 route-remainder refinement.** A route-specific exact pole statement
now has the form
\[
\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2}
=
\frac{x_+(J_H)}{x_+(J_{\rm adj})}
+\Delta^{(r)}_{\rm match}.
\]
The source-to-EFT-to-pole theorem must derive
\(\Delta^{(r)}_{\rm match}=0\) in the selected pole scheme or compute a
controlled remainder with fixed sign, scale, and field-basis dependence.

**Loop 21 source-audit refinement.** Every exact pole statement in the interval,
endpoint, \(G_2\), alpha, or Regge route must use the same remainder form before
it appears as a physical claim.  The CHM interval square is the current active
test case for fixing the field basis and matching map.

## O10. Higgs interpolation \(D=11\to D=10\to D=9\) and colourless \(D=7\to D=6\to D=5\)

**Question.** Can the Higgs/electroweak sector be reconstructed as an interpolation whose full-gauge version has total dimensions \(D=11,10,9\) and KK internal dimensions \(7,6,5\), while its colourless electroweak version has total dimensions \(D=7,6,5\) and KK internal dimensions \(3,2,1\)?

**Local source trail.** The closest local ChatGPT/source note is `/home/codexssh/phys3/sources/unbroken_susy.md`, Section V, lines 69--71. It records the claim that D=11 lacks the required electroweak chirality and that electroweak \(SU(2)\times U(1)\) interpolates, under a W-mass deformation, between descriptions labeled d=9 and D=11. Witten's KK fragments give the primary source trail: `context/source_fragments/witten1981/pages_001-010.md` states the seven-extra-dimensional minimum for \(SU(3)\times SU(2)\times U(1)\), and `context/source_fragments/witten1981/pages_011-017.md` states the associated fermion quantum-number obstruction. The same Witten fragment contains the \(SU(3)\times U(1)\) symmetry address around the five-dimensional sphere construction.

**Current working idea.** Treat this as a source-audit and reconstruction task. The unbroken electroweak endpoint \(v=0\) carries the full \(SU(3)\times SU(2)\times U(1)\) symmetry and belongs to Witten's seven-extra-dimensional KK setting, hence total \(D=11\). The formal heavy-\(W/Z\) decoupling endpoint leaves a five-extra-dimensional \(SU(3)\times U(1)\) geometric address, hence total \(D=9\). The \(U(1)_{\rm em}\) identification requires an embedding theorem, generator normalization, and charge lattice. The working DeVries construction should be tested as an internal six-dimensional interpolation between those endpoints, hence total \(D=10\). Promotion beyond conjecture requires a six-dimensional chirality, anomaly, and light-spectrum account, together with an explicit relation to Witten's seven-dimensional fermion obstruction.

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

1. Define the seven-extra-dimensional endpoint: field content, \(SU(3)\times SU(2)\times U(1)\) symmetry, Witten fermion obstruction, and unbroken electroweak endpoint.
2. Define the five-extra-dimensional endpoint: \(SU(3)\times U(1)\) geometric address, compact-space candidate, fermion statement, formal heavy-\(W/Z\) decoupling endpoint, and electromagnetic embedding theorem.
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
n_{\rm KK}=5:\ SU(3)\times U(1)_{\rm geom},
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

**Loop 18 active-channel refinement.** Appendix E now rewrites the dimensional
claim as a factorized active-channel target
\[
D=4+n_c+n_{\rm ew},\qquad n_c=4,\qquad n_{\rm ew}:3\to2\to1.
\]
The source datum is strengthened to
\[
u\mapsto
\big(t_{\rm dim}(u),t_{\rm EW}(u),
\mathcal F_{\rm sc}(u;J),\mathcal Y_{\rm top}(u)\big).
\]
Thus the same source variable must control the compact or boundary channel,
the electroweak ray, the negative-branch scalar functional, and any top-sector
Yukawa or boundary datum.  Witten's \(SU(3)\times U(1)\) five-sphere address is
kept geometric until the electromagnetic embedding theorem supplies
normalization and charge data.  The top entry is recorded as a theorem target:
\[
\mathcal Y_{\rm top}(u_\star)\to y_t,\qquad
m_t=y_t v/\sqrt2,\qquad
\Pi^{(t)}_{VV}(s;u_\star).
\]

**Loop 26 single-source refinement.** Appendix E now records the claim-status
taxonomy: Witten's seven-extra-dimensional endpoint is source-backed, the
\(D=9\) \(U(1)_{\rm geom}\) endpoint is an electromagnetic embedding target,
the \(D=10\) and colourless \(D=6\) middle lines are reconstruction labels, and
the scalar/top readings are conjectural source maps.  The joint source datum is
expanded to
\[
u\mapsto
\big(t_{\rm dim}(u),t_{\rm EW}(u),v(u),m_h^2(u),K_J(u,\lambda),
\mathcal F_{\rm sc}(u;J),\mathcal Y_{\rm top}(u)\big).
\]
O17 is recorded as downstream of O1, O3, O10, and pole/running matching.  CHM
adds a top-sector source fact: heavy top mass and \(Zb\bar b\) constraints put
pressure on third-generation localization and boundary mixing; a DeVries claim
requires a map from that datum to \(\mathcal Y_{\rm top}(u)\).

**Loop 27 parent/Advisor refinement.** Parent `../physres6` is absorbed as a
conditional KK-fixing theorem target.  The \(D=10\) and colourless \(D=6\)
middle lines remain reconstruction labels until one source variable supplies
\(t_{\rm dim}\), \(t_{\rm EW}\), \(K_J\), \(\mathcal F_{\rm sc}\), and the pole
map.  The BF-admissible Berger-\(S^3\)/CHM test is now a subtarget:
\[
\Delta^{(1)}_{S^3_{\rm Berger}(\rho)}
\to K_J^{\rm geom}(\rho,\lambda)
\to P_J^\dagger(K_J^{\rm geom}+K_J^{\rm CHM})P_J
\to
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix}.
\]
The scalar admissibility condition is
\[
-\frac{9}{4L_{\rm AdS}^2}\le \mu^2x_-(J)<0,
\qquad
u_-(J)\mapsto\mathcal F_{\rm sc}(u;J).
\]
The open data are \(\rho\), \(P_J\), the reduced two-channel subspace, the
boundary/geometric inner product, extra-channel decoupling, and scalar boundary
condition.

**Loop 28 normalization refinement.** The middle-dimensional Schur-complement
data must include the source scale \(\Lambda_J(u)\) and the wavefunction
normalizations that turn the physical kernel into the dimensionless DeVries
block:
\[
u\mapsto
\big(t_{\rm dim}(u),t_{\rm EW}(u),\Lambda_J(u),K_J(u,\widehat\lambda),
\mathcal F_{\rm sc}(u;J),\mathcal Y_{\rm top}(u)\big).
\]
This scale datum is part of the same single-source burden as the
electroweak-ray map, negative-branch scalar functional, and top-sector source
map.

**Loop 31 single-source pass/fail refinement.** Appendix E and Target VI now
make the \(D=10/6\) middle line a normalized source package:
\[
u\mapsto
\big(t_{\rm dim},t_{\rm EW},v,m_h^2,\Lambda_J,
\langle\cdot,\cdot\rangle_u,P_J,\widehat K_J,\mathcal D_J^{\rm extra},
\mathcal F_{\rm sc},\mathcal Y_{\rm top},\mathcal R_{\rm pole}\big),
\qquad
\widehat\lambda=\lambda/\Lambda_J(u)^2 .
\]
The pass/fail theorem is
\[
(\mathcal B(u),\langle\cdot,\cdot\rangle_u,P_J(u),\Lambda_J(u),
\mathcal D_J^{\rm extra}(u))
\mapsto
\widehat K_J(u,\widehat\lambda)
\stackrel{u=u_\star}{=}
\begin{pmatrix}
\widehat\lambda&-\sqrt J\\
-\sqrt J&\widehat\lambda+J
\end{pmatrix}.
\]
The \(D=9\) endpoint obligation is split into compact generator, Standard
Model electromagnetic charge lattice, and four-dimensional kinetic
normalization.  The colourless \(D=5\) endpoint is \(U(1)_{\rm geom}\) until
the same embedding theorem supplies \(U(1)_{\rm em}\).  The top-sector
question is an optional extension:
\[
\mathcal Y_{\rm top}(u_\star)\to
(y_t,m_t,\Pi^{(t)}_{VV}),
\]
with representation, localization or boundary data, anomaly/global-form
checks, and pole-scheme matching in the same reduced basis.  The active CHM
source test uses
\[
u_{\rm int}=(R,v_i,Z_i,\theta_H,c_{Q_3},c_{t_R},M_{\rm mix},\ldots)
\]
to ask whether one interval datum supplies
\((K_T^{\partial I},K_{A_5\pi}^{\partial I},\mathcal Y_{\rm top})\) together
with the hatted DeVries kernel.  The Loop 31 parent-directory read adds
top-as-boundary and D6/KK-monopole source queues as project provenance; primary
Hanany--Witten, M-theory, and D6/KK-monopole sources are required before any
manuscript-facing claim.

## O17. Electromagnetic coupling \(\alpha\) as the content of the \(D=9\) \(U(1)\) endpoint

**Provenance.** Human operator note (2026-05-22).  Treat as a human directive;
agent provenance begins in the loop reports.

**Question.** Does the construction predict the electromagnetic coupling
\(\alpha\), and at what scale does the clean value live?

**Structure (conditional target).** The positive branch fixes the weak angle as a
pure construction number,
\[
\sin^2\theta_{dV}=1-\frac{x_+(3/4)}{x_+(2)}=0.2231\ldots
\]
Conjecture: the \(J=2\) negative branch fixes the radial vacuum normalization.
With the identification
\[
v=\sqrt2\,M_-(J{=}2),
\qquad
M_-(J)=\mu\sqrt{|x_-(J)|},
\qquad
M_W=\mu\sqrt{x_+(3/4)},
\]
both \(M_W\) and \(v\) scale with \(\mu\), so the \(SU(2)\) coupling is
\(\mu\)-independent and \(\alpha\) is a pure number:
\[
g^2=\frac{4M_W^2}{v^2}=\frac{2\,x_+(3/4)}{|x_-(2)|},
\qquad
\alpha_\star=\frac{g^2\sin^2\theta_{dV}}{4\pi}.
\]
The numerical clue that motivated O17 belongs to a later source-audited
calculation phase.  The current manuscript may use only the symbolic
dependency on the scalar theorem.

**Scale placement.** The proposed scale placement is an open matching target.
It must specify which electromagnetic coupling is meant: on-shell
\(\alpha(0)\), \(\MSbar\) \(\hat\alpha(\mu)\), an effective
\(\alpha(q^2)\), a Euclidean hadronic-vacuum-polarization coupling, or a
threshold-matched low-energy EFT coupling.  The theorem must identify the
scale \(Q_\alpha\), the threshold prescription, and the matching remainder
\(\Delta_{\alpha,{\rm match}}\).

**Geometric reading.** In the O10 picture, the negative branch may control a
vacuum or compactification datum that sets the size or normalization of the
\(D=9\) \(U(1)\) endpoint.  A source derivation must show that the compact
\(U(1)_{\rm em}\) gauge kinetic normalization and charge normalization are
fixed by the same source datum.

**Open derivations.**
1. Derive the identification \(v=\sqrt2\,M_-(J{=}2)\): why the \(J=2\) negative
   branch equals \(v/\sqrt2\), the top-Yukawa scale \(m_t=y_t v/\sqrt2\) with
   \(y_t\simeq1\).  This is the negative-branch analog of the O1 ordered
   assignment.
2. Derive the \(\sim1\) GeV scale placement of the clean \(\alpha\).
3. Connect, if possible, to the geometric size of the \(D=9\) \(U(1)\).

**Honest status.** O17 is a conditional theorem target downstream of O1, O3,
O8, and O10.  The scalar assignment \(v=\sqrt2\,M_-(2)\), the common
normalization \(\mu\), the \(U(1)_{\rm em}\) endpoint, and the matching
scale all require derivations.

**Failure mode.** If the scalar theorem leaves \(v=\sqrt2\,M_-(2)\) unproved,
the source route lacks a construction value for \(g\).
If the compact endpoint lacks a fixed \(U(1)_{\rm em}\) charge normalization
or matching scale, \(\alpha\) remains a standard low-energy input.  Records:
O1 (assignment), O3 (negative branch/vacuum scale), O8 (scale placement),
O10 (\(D=9\) \(U(1)\) endpoint), Appendix D Targets VI--VII.

**Loop 16 normalization.** The manuscript now records this issue as Appendix D
Target VII and Appendix E's electromagnetic endpoint-normalization bridge.  The
minimal symbolic target is
\[
g_{\rm sec}^2=
\frac{4C_Wx_+(J_H)}{C_v|x_-(J_v)|},
\qquad
\alpha_{\mathcal S}(Q_\alpha)=
\frac{g_{\rm sec}^2\sin^2\theta_{dV}}{4\pi}
+\Delta_{\alpha,{\rm match}}(Q_\alpha).
\]
The next source task is a primary audit of running electromagnetic coupling
definitions and compactification gauge-coupling normalization.

**Loop 21 source-audit refinement.** Jegerlehner supplies the running
\(\alpha(E)\) and Adler-function source for the O17 scheme audit.  Any
intermediate-scale comparison must specify effective, \(\MSbar\), on-shell, or
Euclidean conventions, plus hadronic vacuum-polarization and threshold
prescriptions.

**Loop 35 photon-zero normalization refinement.** O17 is now a three-part
endpoint theorem target.  The same source datum \(u\) must supply the photon
null projection, the scalar vacuum normalization, and the electromagnetic
kinetic normalization:
\[
u\to
\big(P_W,P_Z,P_\gamma,\Lambda_J,\mathcal F_{\rm sc},\xi_{\rm em}\big)
\to
\big(\sin^2\theta_{\mathcal S}(Q_\alpha),g_{\rm sec}^2,e_{\rm geom}^2\big).
\]
The matching split is
\[
\sin^2\theta_{\mathcal S}(Q_\alpha)
=
\sin^2\theta_{dV}+\Delta_\theta(Q_\alpha),
\qquad
\alpha_{\mathcal S}(Q_\alpha)
=
\frac{g_{\rm sec}^2\sin^2\theta_{\mathcal S}(Q_\alpha)}{4\pi}
+\Delta_{\rm th}(Q_\alpha).
\]
The endpoint package is
\[
\mathfrak E_\alpha(u)
=
\big(\xi_{\rm em},\Gamma_Q,N_{\rm gen},g_D,g_5,
\mathcal T_\alpha,Q_\alpha\big),
\]
where \(\Gamma_Q\) is the charge lattice, \(N_{\rm gen}\) is the generator
normalization, and \(\mathcal T_\alpha\) is the threshold prescription.  The
active source task is a Salam--Strathdee/Witten Kaluza--Klein gauge-kinetic
audit joined to Jegerlehner/Martin--Robertson scheme control.  O17 remains
downstream of O1 ordered sampling, O3 scalar normalization, O8 pole/running
placement, and O10 endpoint embedding.

## O18. The \(s=3/2\) positive state and a Regge completion

**Provenance.** Human operator note (2026-05-22).  Awareness note: keep this on
the books.  Regge is the priority mechanism.

**Awareness.** Once \(\mu\) and the electroweak pole placement are assumed, the
positive branch defines a slot for every sector label:
\[
M_+(s)=\mu\sqrt{x_+\!\big(s(s+1)\big)},\qquad
M_+(\tfrac32)=\mu\sqrt{x_+(15/4)}.
\]
Adjacent notes compare the corresponding numerical value with a reported
low-mass diphoton hint.  That comparison belongs to a later source-audited
phenomenology phase.  The current manuscript use is the symbolic higher-slot
obligation.

**Identity is open.**  The \(SU(2)\times U(1)\) vector spectrum already assigns
the Standard Model \(W\) and \(Z\) slots.  The identity of the \(s=3/2\) branch
belongs to the branch-to-particle assignment problem (O1).  Operator hypothesis
to test: the \(s=3/2\) positive slot may belong to a sector with exotic
charge-\(4/3\) bookkeeping, with the secular label read as a representation
index distinct from physical spin.  This hypothesis requires an
\(SU(3)\times SU(2)\times U(1)\) representation, chirality or vectorlike status,
anomaly ledger, mass-generation rule, production modes, decay modes, widths, and
exclusions.

**Regge framing (priority).**  Promote each \((j,\pm)\) root to a Regge intercept,
\[
M^2_{N_{\rm osc},j,\pm}
=
\mu^2 x_\pm\!\big(j(j+1)\big)
+\frac {N_{\rm osc}}{\alpha'}
+\Delta^{\rm Regge}_{N_{\rm osc},j,\pm},
\]
with \(j\) a DeVries-sector label and \(N_{\rm osc}\) the oscillator or tower
level.  The physical trajectory spin has to be supplied by the source theory.
This is the leading candidate dynamical origin (ties to O4) and the natural home
for higher slots such as \(s=3/2\).

**Collider-source caution.**  A light charged or coloured chiral state faces a
separate collider and representation burden.  The manuscript needs a
compatibility ledger before using a low-mass diphoton, charge-\(4/3\), or
coloured-state reading: primary CMS/ATLAS sources, the phenomenology paper,
local/global significance, look-elsewhere status, pair-production bounds,
single-production assumptions, decay channels, and widths.  Records: O1
(assignment), O4 (dynamical origin), the closed prTalks source-note ledger,
and Appendix D Target VIII.  Companion lean note:
`notes/lean/ReggeHigherBranch.lean`.

**Loop 17 normalization.**  The manuscript now records O18 as
Target VIII, a Regge-intercept survival and higher-branch-slot theorem target.
The main correction is notation: \(j\) labels the DeVries sector,
\(N_{\rm osc}\) labels the oscillator or KK tower level, and physical spin comes
from the source theory.  The first higher positive slot is a projection and
assignment problem until a source route derives the kernel, common slope,
projection rule, and gauge quantum numbers.

**Loop 21 source-audit refinement.** Biekotter--Heinemeyer--Weiglein supply a
neutral \(95.4\) GeV diphoton phenomenology ledger source for Target VIII.
The DeVries branch identity, projection survival, gauge representation, and
production/decay ledger remain source-theory obligations.

## O19. Brane-scaling identity of the two branches

**Provenance.** Human operator note (2026-05-22), from a `../physres6`
cross-check that caught and corrected a prior misreading.

**Question.** Which brane scaling does each DeVries branch follow as mass versus
spin, and does the identification survive a worldvolume/Regge derivation?

**Finding (verify independently).** Measured against the spin \(s\) (with
\(J=s(s+1)\) the Casimir label), via the rotating-brane law
\(M\sim s^{p/(p+1)}\):
- positive branch: \(M_+\to\mu\) bounded \(\Rightarrow p=0\) point / D0-brane;
- negative branch: \(M_-\propto s\) (since \(|x_-|\to J=s(s+1)\), so
  \(M_-^2\propto s(s+1)\)) \(\Rightarrow p\to\infty\) space-filling brane.
A fundamental string (\(M\sim s^{1/2}\)) is excluded: \(M_-/\sqrt s\) grows.

**The trap.** Reading \(M_-^2\propto J\) against the Casimir \(J\) wrongly
suggests a string (\(M\sim\sqrt J\)); an intermediate "D0/D1" reading made this
error and is withdrawn. Use the spin \(s\) as the Regge axis.

**Duality.** The branch inversion \(x\to-J/x\) (\(M^2\to-\mu^4J/M^2\)) exchanges
the point (D0, all-Dirichlet) and the space-filling brane (all-Neumann): a
full-T-duality pair.

**Success criterion.** Derive the point/space-filling correspondence from a
worldvolume or Regge mechanism; reconcile the space-filling growth of the sector
label with the conventional linear Regge tower (which comes from the separate
oscillator \(n\) in \(M_{n,j,\pm}^2=\mu^2x_{j,\pm}+n/\alpha'\)); and state
whether the inversion is literally full T-duality. Cross-check:
`../physres6/calculations/branch_duality.md`.

**Loop 22 theorem-target refinement.** Appendix D now records Target IX:
branch scaling and brane-duality admissibility.  The accepted algebraic input is
\[
x_+(s(s+1))=1+O(s^{-2}),\qquad |x_-(s(s+1))|=s(s+1)+O(1),
\]
giving the diagnostic \(M_+\to\mu\) and \(|M_-|\sim\mu s\) under the chosen
mass reading.  Tong's D-brane/T-duality vocabulary supplies source addresses
for D0, space-filling, and Neumann--Dirichlet exchange.  The open data are the
rotating-brane exponent source, the branch survival rule, the negative-branch
mass or scalar-functional reading, and the boundary-condition duality map.

## O20. The operator as a broken N=2 supersymmetric quantum mechanics

**Provenance.** Human operator note (2026-05-22), from `../physres6`. Refines O4
(dynamical origin); touches O1 and O3.

**Statement.** O20 tests whether the off-diagonal \(\sqrt J\) of \(Q(J)\) can be
derived from a de Rham/Hodge supersymmetric quantum-mechanics reduction.  With
the exterior derivative \(d\) and its adjoint \(\delta\), Witten's Morse-theory
construction gives supercharges whose Hamiltonian is the Hodge Laplacian and
whose Witten deformation couples the complex to Morse data.  The DeVries target
asks for normalized \(0/1\)-form channels
\[
D_Je^0_J=\sqrt J\,e^1_J,\qquad
D_J^\dagger e^1_J=\sqrt J\,e^0_J,
\]
plus a sourced breaking operator \(B_J=\operatorname{diag}(0,-J)\) in the same
two-channel basis.  This gives O4 a named theorem target: a de Rham supercharge,
a finite projection, and a supersymmetry-breaking diagonal.

**Electroweak-SUSY home (for O1/O3).**
- Fayet (1403.5951): the Higgs as the spin-0 SUSY partner of the \(Z\); a
  supersymmetry relating the neutral gauge boson and the order parameter, i.e.
  the positive (\(Z\)) and negative (Higgs/order-parameter) branches.
- the \(su(2/1)\) electroweak superconnection (Ne'eman; Fairlie; Coquereaux et
  al.): electroweak gauge fields as the even part, the Higgs as the odd part of a
  superconnection.
- spin from worldline SUSY (Gates--Rana, hep-th/9504025): one supercharge is the
  spin/Dirac structure.

**Working conjecture.** A broken \(N=2\) reduction in the IR with one supercharge
from the spin/Hodge grading \((d/\delta)\) and another electroweak grading from
the \(su(2/1)\) superconnection.  The two branches would be read as the split
eigenchannels of this finite reduction.  This is a conjectural synthesis built
from published pieces.

**Success criterion.** Derive the \(-J\) breaking from a specified
supersymmetry-breaking term, identify the second supercharge with the \(su(2/1)\)
odd generators, and reconcile with O1 (the \((3/4,2)\) assignment) and O3
(negative branch = order parameter). Cross-check: `../physres6` (broken \(N=2\)
SUSY QM in the Letter).

**Loop 23 theorem-target refinement.** Appendix D now records Target X:
Hodge/SUSY-QM origin of the DeVries block.  The source-audited local corpus now
contains Witten's scanned Morse-theory paper, Fayet's gauge/BEH supersymmetry
paper, Gates--Rana on worldline supersymmetry, and Coquereaux's \(SU(2|1)\)
electroweak superconnection talk.  The accepted use is the off-diagonal
factorization target
\[
Q_{{\rm dR},J}=
\begin{pmatrix}0&\sqrt J\\ \sqrt J&0\end{pmatrix},
\qquad
Q_{{\rm red},J}=Q_{{\rm dR},J}+B_J,
\qquad
B_J=\begin{pmatrix}0&0\\0&-J\end{pmatrix}.
\]
The open data are the source of \(J\), the projection to two channels, the
breaking operator, the electroweak \(su(2/1)\) map, and the pole/scalar
compatibility chain.

**Loop 28 factorization-first refinement.** Target X is now the off-diagonal
entry test in the active proof spine.  The conjectural Hodge/superconnection
route must derive
\[
D_Je^0_J=\sqrt J\,e^1_J,\qquad
D_J^\dagger e^1_J=\sqrt J\,e^0_J
\]
in the same reduced basis that carries \(P_W\), \(P_Z\), the hatted CHM current
entry, and the negative-branch scalar functional.  The projection, breaking
operator \(B_J=\operatorname{diag}(0,-J)\), and compatibility with O1 and O3
remain open theorem data.

============================ REMEMBER TO CLOSE AND REMOVE ISSUES THAT ARE TERMINATED, AND COMMIT ===============
============================ REMEMBER TO CLOSE AND REMOVE ISSUES THAT HAVE REACHED THE SUCCESS CRITERIUM, AND COMMIT ===============
