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
