# Open analytical issues

## O1. Derive the W/Z assignment

**Question.** Why does the charged W comparison sample \(J=3/4\) while the neutral Z comparison samples \(J=2\)?

**Current working idea.** The \(J=2\) datum has an adjoint-current reading through the \(SU(2)_L\) gauge sector. The \(J=3/4\) datum belongs to the Higgs/order-parameter doublet side. The missing step is the ordered sampling rule that turns \((J_H,J_{\rm adj})=(3/4,2)\) into the W/Z quotient.

**Success criterion.** A derivation from the gauge-Higgs sector that yields the ordered pair \((J_W,J_Z)=(3/4,2)\) directly and rules out post-selection.

**Parent-workspace refinement.** The `../weak` critique turns this into a
mass-map theorem.  The assignment must pass through a gauge-Higgs mass matrix,
pole self-energy map, or equivalent source-theory reduction.  SO(32) flavor
bookkeeping supplies the ordered pair once an electroweak-operator
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
assignment is accepted when the same reduced field basis supplies the
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
arena.  The issue closes when
\[
\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2}
=
\frac{x_+(J_H)}{x_+(J_{\rm adj})}
+\Delta_{\rm O1}
\]
has a derived \(\Delta_{\rm O1}\) or a stated source remainder.

**Loop 37 boundary-kernel refinement.** The manuscript now states the
O1/Target~VI interface as a single-source interval theorem diagram.  In the CHM version one
source datum \(u_{\rm int}\) must supply
\[
\left(K_T^{\rm DtN}+K_T^{\rm brane},P_\gamma,
\langle\cdot,\cdot\rangle_{u_{\rm int}}\right)
\longrightarrow
\widehat K_J,
\qquad
\left(v,g,g'\right)
\longrightarrow
\left(P_W,P_Z,P_\gamma,\Lambda_J\right),
\]
with
\[
\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2}
=
\frac{x_+(3/4)}{x_+(2)}
+\Delta_{\rm O1/O10}(u_{\rm int}).
\]
This refinement removes loop/process language from Sec. IV and makes CHM the
first source arena for the shared projection, photon subtraction, normalization,
and pole-remainder test.  O1 stays open because \(P_W\), \(P_Z\), \(P_\gamma\),
\(\Lambda_J\), \(\widehat K_J\), and \(\Delta_{\rm O1/O10}\) still require a
source derivation.

**Loop 39 Coquereaux audit.** The local Coquereaux source records a finite
electroweak superconnection arena: odd matrices \(\Omega_\pm,\Omega'_\pm\),
even generators \(I_3,Y,Q\), a generalized connection with gauge one-forms and
scalar zero-forms, and curvature
\(\mathcal F_{\rm Coq}=d\mathcal A_{\rm Coq}+
\mathcal A_{\rm Coq}\odot\mathcal A_{\rm Coq}\).  Rendered pages 70--76 record
the \(U(1)\times U(1)\) connection, the graded product and curvature, the
source-internal \(Z/P\) rotation, the \(SU(2|1)\) lepton and quark matrices,
and the extended-family \(3/8\) weak-angle value.  O1 can use this as finite
gauge-Higgs algebra.  The scalar-product freedoms set a normalization
obligation.  The O1 closure package requires
\[
\mathcal A_{\rm Coq}\mapsto
\left(P_{\rm sc},\langle\cdot,\cdot\rangle_{\rm sc},
P_W,P_Z,P_\gamma,\Delta_{\rm O1}\right)
\]
with \(P_W(h_J)=3/4\), \(P_Z(a_J^{\gamma^\perp})=2\), photon subtraction, and
complex-pole matching derived in one source ledger.

**Loop 40 sc/int closure package.** O1 is tied to the boundary
electroweak-superconnection interval package
\[
\mathfrak D_{\rm sc/int}
=
\left(
K_T^{\rm DtN},K_T^{\rm brane},\mathcal F_{\rm sc},
P_{\rm sc},P_W,P_Z,P_\gamma,K_\gamma^{\rm ref},
\Lambda_J,\langle\cdot,\cdot\rangle_{\rm CHM},\mathcal R_{\rm pole}
\right).
\]
The closure condition is a same-package derivation of
\[
P_W(\Phi_{\rm odd})=\frac34,\qquad
P_Z(F_{\rm even}^{\gamma^\perp})=2,\qquad
P_\gamma(F_{\rm even}^{\gamma})=0,\qquad
\Delta_{\rm O1/O10}\ \hbox{in the complex-pole scheme}.
\]

**Loop 42 Ward-projected neutral-current refinement.** O1 now includes an
explicit neutral transverse trace space
\(\mathcal N_T^\partial=\operatorname{span}\{W_T^3,B_T\}\) with a photon
projector and a hypercharge remainder:
\[
\Pi_{\gamma^\perp}^{(T)}
=1-|a_\gamma\rangle\langle a_\gamma|_{u_{\rm EW}},
\qquad
a_J^{\gamma^\perp}
=P_{a,J}\Pi_{\gamma^\perp}^{(T)}(W_T^3,B_T),
\]
\[
P_Z(a_J^{\gamma^\perp})=2+\Delta_Y(u_{\rm EW}),
\qquad P_\gamma(a_\gamma)=0.
\]
The charged side is tested by the Goldstone-vector mixing terms
\[
\mathcal L_{\partial G V}
=iM_W[(\partial_\mu G^-)W^{+\mu}-(\partial_\mu G^+)W^{-\mu}]
+M_Z(\partial_\mu G^0)Z^\mu.
\]
Closure requires \(\Delta_Y\), \(P_W\), \(P_Z\), \(P_\gamma\), and the pole
remainder from one gauge-Higgs or interval source package.

**Loop 43 source-product normalization refinement.** O1 now spells out the
tree-level neutral trace directions and their source normalization:
\[
a_\gamma^{(0)}
=\frac{g'W_T^3+gB_T}{\sqrt{g^2+g'^2}},
\qquad
z^{(0)}
=\frac{gW_T^3-g'B_T}{\sqrt{g^2+g'^2}},
\]
\[
a_\gamma=
\frac{P_\gamma a_\gamma^{(0)}}
{\sqrt{\langle P_\gamma a_\gamma^{(0)},P_\gamma a_\gamma^{(0)}
\rangle_{u_{\rm EW}}}},
\qquad
a_J^{\gamma^\perp}
=
\frac{P_{a,J}\Pi_{\gamma^\perp}^{(T)}z^{(0)}}
{\sqrt{\langle P_{a,J}\Pi_{\gamma^\perp}^{(T)}z^{(0)},
P_{a,J}\Pi_{\gamma^\perp}^{(T)}z^{(0)}
\rangle_{u_{\rm EW}}}}.
\]
The charged side has the companion target
\[
P_W(h_J)=\frac34+\Delta_W(u_{\rm EW}),\qquad
\Delta_W(u_{\rm EW})\stackrel{\rm closure}{=}0.
\]
The active analytical task is the joint derivation of \(\Delta_W\),
\(\Delta_Y\), and \(\Delta_{\rm O1}\) from the same source product, photon
reference, CHM current entry, and pole map.

**Loop 44 CHM projector-package refinement.** The O1/O4 bridge now records
the admissibility data for the Ward-projected traces:
\[
\langle\widetilde a_\gamma,\widetilde a_\gamma\rangle_{u_{\rm EW}}>0,\qquad
\langle\widetilde a_J^{\gamma^\perp},
\widetilde a_J^{\gamma^\perp}\rangle_{u_{\rm EW}}>0,
\]
plus either an ordered product \(P_{a,J}\Pi_{\gamma^\perp}^{(T)}\) or a
commutation theorem on \(\mathcal N_T^\partial\).  The CHM version packages
\[
u_{\rm CHM}\mapsto
\left(
\mathcal N_T^\partial,\langle\cdot,\cdot\rangle_{\rm CHM},
P_{h,J},P_{a,J}^{\gamma^\perp},P_\gamma,
K_{\gamma,J}^{\rm ref},\Lambda_{\rm CHM},\mathcal R_{\rm pole}
\right),
\]
and the target conditions are
\[
\widehat\Sigma_{aa,2}^{\rm CHM}=2,\qquad
\widehat{\mathcal I}_{h,3/4}^{\rm CHM}=\frac34,\qquad
\Delta_Y^{\rm CHM}=\Delta_W^{\rm CHM}=0,
\]
to be derived together with \(\Delta_{\rm O1/O10}\) in the pole scheme.  O1 remains open
because these projector, norm, source-scale, and pole-map conditions still
await derivation from the interval action.

**Loop 45 CHM admissibility-lemma refinement.** The CHM current package is now
a shared admissibility lemma.  Closure requires positive projected CHM norms,
photon-orthogonality preservation, ordered or commuting projectors,
photon-reference subtraction, one \(\Lambda_{\rm CHM}\), and
\[
Z_J^{\rm cur}
=\partial_{\widehat\lambda}\widehat K_J^{\rm cur}(0)>0.
\]
The canonical target is
\[
\widehat\Sigma_{aa,2}^{\rm CHM,can}=2,
\]
followed by \(\Delta_W^{\rm CHM}=0\), \(\Delta_Y^{\rm CHM}=0\), the same-basis
Hodge product, and the pole remainder \(\Delta_{\rm O1/O10}\).

**Loop 46 CHM source-equation protocol refinement.** O1 now requires the
ordered source-equation extraction
\[
\left\{
P_\gamma,\,
P_{a,2}^{\gamma^\perp},\,
K_{\gamma,2}^{\rm ref},\,
\Lambda_{\rm CHM},\,
Z_2^{\rm cur},\,
\langle\cdot,\cdot\rangle_{\rm CHM}
\right\}
\longrightarrow
\widehat\Sigma_{aa,2}^{\rm CHM,can}.
\]
Accepted closure requires \(\widehat\Sigma_{aa,2}^{\rm CHM,can}=2\) with
positive projected norms, preserved photon orthogonality, and
\(Z_2^{\rm cur}>0\).  The rejection ledger is
\[
\widehat\Sigma_{aa,2}^{\rm CHM,can}\ne2,\qquad
Z_2^{\rm cur}\le0,\qquad
\langle a_2^{\gamma^\perp},a_2^{\gamma^\perp}\rangle_{\rm CHM}\le0,\qquad
\langle a_2^{\gamma^\perp},a_\gamma\rangle_{\rm CHM}\ne0.
\]
Those outputs set \(\Delta_Y^{\rm CHM}\), the admissible source scale, or the
projector normalization for the interval route.

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

**Loop 39 scalar-functional target.** Sec. V treats the negative branch as a scalar-functional theorem target:
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

**Loop 41 holonomy-superconnection refinement.** The active scalar route joins
the Hosotani holonomy to the boundary electroweak superconnection package:
\[
\mathcal W_{\rm sc}
=
{\rm P}\exp\int_I(A_5+\Phi_{\rm odd})\,dy,
\qquad
\widehat{\mathcal F}_{\rm sc}^{\rm Hol/sc}
=
\Lambda_J^{-2}
\left.
\frac{\partial^2V_{\rm eff}(\mathcal W_{\rm sc})}
{\partial\alpha_{\rm sc}^2}
\right|_{\alpha_\star}.
\]
The O3 closure condition is
\[
\widehat{\mathcal F}_{\rm sc}^{\rm Hol/sc}
=C_{\rm sc}|x_-(J_\star)|+\Delta_{\rm Hol/sc}
\]
using the same \(P_{\rm sc}\), \(\Lambda_J\), photon reference, and pole map as
the sc/int vector kernel.  Closure requires a source derivation of
\(\Delta_{\rm Hol/sc}\).  This turns the negative branch into a Hessian
diagnostic for the same source package.

**Loop 42 scalar-provenance refinement.** The negative-branch opening now
states the branch magnitudes as provisional scalar-side comparison scales.
The physical target remains the same-source scalar functional
\(\widehat{\mathcal F}_{\rm sc}\) with a derived normalization and scheme.

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
main text are source candidates.  They acquire physical status after a
gauge-invariant scalar functional, normalization, and electroweak scheme are
derived.

**Loop 21 source-pack refinement.** Bucci and Haba--Oda support scalar-modulus,
radion, Dirichlet-Higgs, and boundary-Higgs address candidates for O3/Target~VI.
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

**Endpoint refinement.** The brane-Higgsing route has a concrete dictionary:
Chan--Paton labels supply matrix fields, coincident branes supply adjoint gauge fields and scalars, and separated branes give scalar/vector mixing through stretched strings. The unresolved step is the reduction of this matrix worldvolume data to \(\kappa_J^2=\tau_J=J\) and the ordered pair \((3/4,2)\).

**Interval refinement.** The KK route has a parallel dictionary:
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
test has a normalized extraction:
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
the hatted current entry into an acceptance source theorem.  Source facts now
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
source-to-pole matching, Target~VI for the single source variable and
\(\Lambda_J(u)\), and O20 for the common reduced basis with the Hodge
off-diagonal test.  Issue status remains open.

**Loop 34 source-kernel theorem refinement.** The first O4 acceptance theorem is
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
\(\Delta_{\rm match}^{(r)}\), to Target~VI through \(u\) and \(\Lambda_J(u)\), and
to O20 through the common reduced basis.

**Loop 40 sc/int kernel refinement.** The active O4 package is
\[
\widehat K^{\rm sc/int}_J(\widehat\lambda)
=
\Lambda_J^{-2}P_{\rm sc}^\dagger
\Big[
K_T^{\rm DtN}+K_T^{\rm brane}
+\langle\mathcal F_{\rm sc},\mathcal F_{\rm sc}\rangle_{\rm sc}
-K_\gamma^{\rm ref}
\Big]P_{\rm sc}.
\]
The closure test is the DeVries block plus a derived pole-scheme remainder:
\[
\widehat K^{\rm sc/int}_J(\widehat\lambda)
=
\begin{pmatrix}
\widehat\lambda&-\sqrt J\\
-\sqrt J&\widehat\lambda+J
\end{pmatrix}
+\Delta_J^{\rm sc/int}(\widehat\lambda).
\]
This package ties O4 to O1 through the ordered projectors, to O3 through the
scalar functional, to O8 through \(\Delta_J^{\rm sc/int}\), to Target~VI through
\(\Lambda_J(u)\), and to O20 through \(P_{\rm sc}\).

**Loop 41 proof-test refinement.** The next O4 acceptance test is the hatted CHM
current entry in the sc/int package:
\[
\widehat\Sigma_{aa,2}^{\rm CHM}=2 .
\]
A derivation has to fix \(P_{a,2}^{\gamma^\perp}\), \(P_\gamma\),
\(K_\gamma^{\rm ref}\), \(\Lambda_J\), the CHM product, and the map into the
complex-pole transverse self-energy in one convention.  The scalar extension is
the holonomy-superconnection Hessian in O3.

**Loop 42 proof-spine refinement.** The route-comparison section now displays
the active proof spine:
\[
\begin{array}{ccc}
(H,W^a,B;t) & \longrightarrow & (J_H,J_{\rm adj},J_\gamma)\\
\downarrow && \downarrow\\
(K_T^{\rm DtN}+K_T^{\rm brane},\mathcal F_{\rm sc})
& \longrightarrow &
(\widehat\Sigma_{aa,2}^{\rm CHM},
\Sigma_{ha,J}\Sigma_{ah,J},
P_W,P_Z,P_\gamma,\Delta_{\rm O1/O10}).
\end{array}
\]
The three named derivations are the CHM neutral-current entry, the same-basis
Hodge/SUSY-QM off-diagonal product, and the ordered projector package with a
pole remainder.

**Loop 45 CHM admissibility-lemma refinement.** O4 now starts its entry-level
test from a shared CHM lemma.  The source route must supply positive projected
norms for \(P_\gamma a_\gamma^{(0)}\) and
\(P_{a,J}\Pi_{\gamma^\perp}^{(T)}z^{(0)}\), preserve photon orthogonality,
state the projector order or commutation theorem, perform photon-reference
subtraction, derive the shared \(\Lambda_{\rm CHM}\), and derive the current
slope
\[
Z_J^{\rm cur}
=\partial_{\widehat\lambda}\widehat K_J^{\rm cur}(0)>0.
\]
The diagonal acceptance test is
\[
\widehat\Sigma_{aa,2}^{\rm CHM,can}=2.
\]
The same reduced basis must then carry the Hodge/SUSY-QM off-diagonal product,
\(\Delta_W^{\rm CHM}\), \(\Delta_Y^{\rm CHM}\), and the pole remainder
\(\Delta_{\rm O1/O10}\).

**Loop 46 CHM source-equation protocol refinement.** The entry-level test has
an explicit extraction and rejection sequence.  CHM equations define
\(\mathcal N_T^\partial\), \(\langle\cdot,\cdot\rangle_{\rm CHM}\),
\(K^{\rm DtN}_{T,J}\), and \(K^{\rm brane}_{T,J}\).  Photon subtraction fixes
\((P_\gamma,K_{\gamma,J}^{\rm ref})\).  The canonical current entry is then
read after \(P_{a,2}^{\gamma^\perp}\), \(\Lambda_{\rm CHM}\), and
\(Z_2^{\rm cur}\) are fixed.  The accepted case is
\(\widehat\Sigma_{aa,2}^{\rm CHM,can}=2\); the four rejection outputs are the
noncanonical constant entry, nonpositive current slope, nonpositive projected
\(Z\)-trace norm, and photon-orthogonality failure.

**Dimensional Schur-complement refinement.** Round 2 makes this the active
Target~VI/O4 bridge.  The \(D=10/6\) middle line is represented by a light boundary
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

**\(G_2\) refinement.** The local \(G_2\) route has a parallel kernel:
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
Loop 47 adds a local \(G_2\) ADE-pairing test.  The
source datum is
\[
u_{G_2}^{\rm loc}=(M_3,\Gamma_{\rm ADE},W,\Phi,\rho_i,f_i,Q,p,\gamma,
A_1\subset A_2,\Lambda_{G_2}),
\]
with the local enhancement target
\[
\operatorname{ad}A_2\!\downarrow_{A_1\times U(1)}
=
(\operatorname{ad}A_1)_0\oplus{\bf 1}_0\oplus{\bf 2}_{+q}\oplus{\bf 2}_{-q}.
\]
The singular-support pairing is
\[
\langle\eta,\zeta\rangle_{G_2,u}
=
\int_{M_3}{\rm Tr}_{\rm ADE}(\eta\wedge *_{M_3}\zeta)
+
\sum_{p\in Z(df_Q)}
\eta(p)^\dagger\mathsf G_Q(p)\zeta(p).
\]
The canonical current-entry test is
\[
\widehat K_J^{G_2,{\rm cur,can}}(\widehat\lambda)
=
\widehat\lambda+\widehat\Sigma_{aa,J}^{G_2,{\rm can}}
+O(\widehat\lambda^2),
\qquad
\widehat\Sigma_{aa,2}^{G_2,{\rm can}}=2.
\]
Loop 48 adds the downstream flow-overlap target.  With a localized
order-parameter wavefunction \(\psi_{h,J}^{G_2}\), a projected ADE current
mode \(a_J^{G_2}\), a point or component metric \(\mathsf G_Q\), oriented
flow kernels \(\mathcal K_{\rm flow}^{G_2}(\gamma)\), and bilinear maps
\(B_{ha}^{G_2},B_{ah}^{G_2}\), the theorem target is
\[
\begin{aligned}
\widehat\Sigma_{ha,J}^{G_2}
&=
\Lambda_{G_2}^{-1}
\sum_\gamma\epsilon_\gamma
B_{ha}^{G_2}\!\left(
\psi_{h,J}^{G_2},
\mathcal K_{\rm flow}^{G_2}(\gamma)a_J^{G_2}
\right),
\\
\widehat\Sigma_{ah,J}^{G_2}
&=
\Lambda_{G_2}^{-1}
\sum_\gamma\epsilon_\gamma
B_{ah}^{G_2}\!\left(
a_J^{G_2},
\mathcal K_{\rm flow}^{G_2}(\gamma)\psi_{h,J}^{G_2}
\right),
\end{aligned}
\qquad
\widehat\Sigma_{ha,J}^{G_2}\widehat\Sigma_{ah,J}^{G_2}=J .
\]
The rejection ledger is: noncanonical product, nonpositive \(\mathsf G_Q\),
missing orientation convention, extra coupled light channel, or failure of the
same-basis projection shared with Target IIIg.
Loop 49 records a failed derivation step for the broad Braun route.  The source
matrix supported by Braun--Cizel--Hubner--Schafer-Nameki is the Morse--Witten
two-point matrix
\[
M_{\rm MW}^{ab}
=
\sum_\gamma n_\gamma e^{-tq(f(p_a)-f(p_b))},
\qquad
n_\gamma=\pm1,
\]
acting between localized chiral multiplet ground states.  The missing map is
\[
M_{\rm MW}^{ab}
\leadsto
\left(
\widehat\Sigma_{ha,J}^{G_2},
\widehat\Sigma_{ah,J}^{G_2}
\right)
\]
in a closed \((h_J^{G_2},a_J^{G_2})\) block.  The obstruction is the absent
source identification of the projected ADE current \(a_J^{G_2}\) as a
Morse--Witten endpoint state.  The narrowed test is
\[
\widehat\Sigma_{ha,J}^{G_2}=\Lambda_{G_2}^{-1}M_{ha}^{\rm MW},
\qquad
\widehat\Sigma_{ah,J}^{G_2}=\Lambda_{G_2}^{-1}M_{ah}^{\rm MW},
\]
after same-basis compatibility with Target IIIg, positivity of \(\mathsf G_Q\),
orientation convention, and extra-channel control are derived.  A failure of
that embedding rejects the Braun flow-overlap route for Target IIIh while
leaving Braun's localization and interaction data available as source support
for \(G_2\) model building.
The unresolved steps are the local derivation of
\(\mathcal K_{\rm cur}^{\rm ADE}\), positivity of \(Z_2^{G_2}\), extra-channel
control, the narrowed Morse--Witten embedding test above, the scalar map
\(u_-(J)\mapsto\mathcal F_{G_2}\), compact charge-lattice completion,
hypercharge embedding, anomaly/global-form compatibility, and pole matching.

**Route-comparison refinement.** Sec. VI.G places the endpoint, interval, and \(G_2\) routes into one kernel target:
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
has the form
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

## O18. The \(s=3/2\) positive state and a Regge completion

**Provenance.** Human operator note (2026-05-22).  Awareness note: keep this on
the books.  Regge is the priority mechanism.

**Awareness.** Once \(\mu\) and the electroweak pole placement are assumed, the
positive branch defines a slot for every sector label:
\[
M_+(s)=\mu\sqrt{x_+\!\big(s(s+1)\big)},\qquad
M_+(\tfrac32)=\mu\sqrt{x_+(15/4)}.
\]
Adjacent notes compare the corresponding numerical value with a low-mass
diphoton phenomenology note.  That comparison belongs to a later source-audited
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

**Loop 36 sector-duality refinement.** O18 and O19 now share a source package
\[
\mathfrak R_j=
\big(K_j,\alpha',P_{\rm surv},\mathcal B_{\rm ND},
\mathcal Q,\mathcal T,\chi_{\rm spin}\big),
\]
where \(P_{\rm surv}\) is the projection or BRST/GSO survival rule,
\(\mathcal B_{\rm ND}\) is the Neumann--Dirichlet boundary-condition map,
\(\mathcal Q\) records charges, \(\mathcal T\) records tensions, and
\(\chi_{\rm spin}\) maps a DeVries sector label to a putative rotating-brane
angular momentum.  The \(j=3/2\) slot remains an assignment ledger entry
pending \(\mathfrak R_{3/2}\), gauge quantum numbers, production, decay, width,
and collider-source data.  Biekotter--Heinemeyer--Weiglein remain a collider
ledger source, with branch identity supplied by the source theory.

## O19. Brane-scaling identity of the two branches

**Provenance.** Human operator note (2026-05-22), from a `../physres6`
cross-check that caught and corrected a prior misreading.

**Question.** Which brane scaling does each DeVries branch follow as mass versus
spin, and does the identification survive a worldvolume/Regge derivation?

**Finding (verify independently).** Measured against a putative rotating-brane
angular momentum \(s_{\rm br}\), with
\(J_{\rm br}=s_{\rm br}(s_{\rm br}+1)\), the branch asymptotics give the
diagnostic
\[
M_+(s_{\rm br})\to\mu,\qquad
|M_-(s_{\rm br})|\sim \mu s_{\rm br}.
\]
If a source route supplies the rotating-brane law
\(M\sim s_{\rm br}^{p/(p+1)}\), the diagnostic labels are \(p=0\) for the
bounded positive branch and \(p\to\infty\) for the linearly growing negative
branch.  The primary source for this exponent remains open.

**Axis caveat.** The DeVries label \(j\), the oscillator level \(N_{\rm osc}\),
physical Regge spin, and \(s_{\rm br}\) are separate labels.  The map
\(\chi_{\rm spin}:j\mapsto s_{\rm br}\) is required for a physical
brane-scaling diagnostic.

**Duality.** The branch inversion \(x\to-J/x\) (\(M^2\to-\mu^4J/M^2\)) is an
algebraic pairing.  A T-duality interpretation requires a compact coordinate,
Neumann--Dirichlet boundary-condition exchange, charge matching, tension
matching, and a negative-branch mass or scalar-functional reading.

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

**Loop 36 sector-duality refinement.** Target IX now depends on the same
\(\mathfrak R_j\) source package as O18 plus the axis map
\[
\chi_{\rm spin}:\ j\mapsto s_{\rm br}(j),
\qquad
J_{\rm br}=s_{\rm br}(s_{\rm br}+1).
\]
The D0 and space-filling labels are admissibility diagnostics pending a primary
rotating-\(p\)-brane scaling source and a boundary-condition duality map.  O19
fails as a brane-duality target if \(\chi_{\rm spin}\), the negative-branch
reading, or the Neumann--Dirichlet lift of \(x\mapsto-J/x\) is absent.

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
- Fayet (1403.5951): electroweak supersymmetry vocabulary in which spin-zero
  BEH fields appear in massive gauge multiplets with \(W\) and \(Z\) bosons;
  the DeVries branch assignment remains an O3/O20 theorem datum.
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

**Loop 38 source-equation refinement.** Rendered Witten pages 665--666 now give
the equation-level support for the Hodge side: \(Q_1=d+d^*\),
\(Q_2=i(d-d^*)\), \(H=dd^*+d^*d\), the deformed \(d_t=e^{-ht}de^{ht}\), and the
Hamiltonian \(H_t\) with gradient and Hessian terms.  The accepted source
claim is the de Rham/SUSY-QM template for a normalized square-root pair.  O20
also requires an explicit source operator for the one-channel entry
\(B_J=\operatorname{diag}(0,-J)\) in the same finite basis.  Candidate
mechanisms are a boundary/self-adjoint-extension term or a superconnection
curvature term, with a common inner product, fixed sign convention, absence of
extra light modes, \(J=\lambda_J=s(s+1)\), and compatibility with O1/O3 and the
pole-mass chain.

**Loop 39 Coquereaux projection refinement.** The candidate superconnection
route is the graded-curvature projection
\[
P_{\rm sc}^\dagger
\langle\mathcal F_{\rm Coq},\mathcal F_{\rm Coq}\rangle_{\rm sc}
P_{\rm sc}
=
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix}
+\Delta_{\rm sc}^{\rm op}(\lambda).
\]
Coquereaux supplies the \(\mathbb Z_2\)-graded finite matrix arena and the
electroweak odd/even vocabulary.  The projection \(P_{\rm sc}\), the common
inner product, \(J=s(s+1)\), \(B_J\), extra-channel decoupling, the
negative-branch scalar map, and complex-pole matching remain O20 theorem data.

**Loop 40 boundary-superconnection refinement.** Target X has an interval
implementation:
\[
\widehat K^{\rm sc/int}_J
=
\Lambda_J^{-2}P_{\rm sc}^\dagger
\left(K_T^{\rm DtN}+K_T^{\rm brane}
+\langle\mathcal F_{\rm sc},\mathcal F_{\rm sc}\rangle_{\rm sc}
-K_\gamma^{\rm ref}\right)P_{\rm sc}.
\]
Witten supplies the Hodge square-root template; Coquereaux supplies the finite
odd/even gauge-Higgs algebra; CHM supplies boundary kernels and photon-zero
bookkeeping.  O20 closure requires these inputs to give \(B_J\), the
two-channel projection, extra-channel decoupling, and the pole/scalar branch
map in one self-adjoint reduced basis.

**Loop 41 holonomy-superconnection refinement.** The candidate source for the
scalar side of \(B_J\) is the compact holonomy
\[
\mathcal W_{\rm sc}={\rm P}\exp\int_I(A_5+\Phi_{\rm odd})\,dy .
\]
The O20 test asks whether
\[
\Lambda_J^{-2}P_{\rm sc}^\dagger
\left[
K_T^{\rm DtN}+K_T^{\rm brane}
+\partial_{\alpha_{\rm sc}}^2V_{\rm eff}(\mathcal W_{\rm sc})
-K_\gamma^{\rm ref}
\right]P_{\rm sc}
\]
supplies the DeVries block and the negative-branch scalar Hessian in one
self-adjoint basis.  The detailed IJMP A superconnection source remains an
acquisition target for scalar products, curvature norms, Higgs potential terms,
and \(Z/\gamma\) conventions.

============================ REMEMBER TO CLOSE AND REMOVE ISSUES THAT ARE TERMINATED, AND COMMIT ===============
============================ REMEMBER TO CLOSE AND REMOVE ISSUES THAT HAVE REACHED THE SUCCESS CRITERIUM, AND COMMIT ===============
