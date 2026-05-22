# Normalization Loop 34 Advisor

Role: advisor synthesis for O4 source-kernel tightening.

Status: review only.

## Advisor Thesis

Loop 34 should tighten O4 into an entry-by-entry source-kernel proof ledger.
The active pass/fail theorem is the hatted CHM current entry
\(\widehat\Sigma^{\rm CHM}_{aa,J}=J\).  The companion theorem is the
Hodge/SUSY-QM square-root product \(\Sigma_{ha,J}\Sigma_{ah,J}=J\).
\(G_2\) supplies a local operator audit.  Endpoint/Chan--Paton supplies a
matrix arena pending an explicit worldvolume kernel and projection.

## Minimum Manuscript Patch

- `manuscript/sections/06c_kaluza_klein_boundary.tex`: after
  `eq:chm-current-entry-normalized`, add a named CHM current-entry theorem
  target.  List \(P_{a,J}^{\gamma^\perp}\), \(P_\gamma\),
  \(K^{\rm ref}_{T,J}\), \(\Lambda_{\rm CHM}\), endpoint signs, CHM product,
  and pole map as theorem data for promotion of
  \(\widehat\Sigma^{\rm CHM}_{aa,J}=J\).
- `manuscript/sections/06g_route_comparison.tex`: after
  `eq:route-common-target`, add the Loop 34 route priority: CHM current entry
  first; Hodge square-root entry second; \(G_2\) local kernel third;
  endpoint/Chan--Paton as matrix-arena support.  In branch interpretation, tie
  \(\mathcal F_{{\rm sc},r}\) to Appendix D's same-source scalar package.
- `manuscript/sections/06f_endpoint_higgsing.tex`: in the endpoint completion
  criterion, state that Chan--Paton and brane Higgsing source matrix fields,
  with the DeVries step requiring a worldvolume quadratic kernel, projection,
  inner product, and \(\kappa_J^2=\tau_J=J\).
- `manuscript/sections/06d_g2_localization.tex`: after
  `eq:g2-self-energy-target` or in the entry dictionary, add the Braun et al.
  source-equation audit and label \(\Sigma_{aa,J}^{G_2}=J\) plus the
  flow-overlap product as local entry targets pending the local operator and
  inner product.
- `manuscript/sections/D_theorem_targets.tex`: in the CHM current-entry
  subtarget, cite the CHM equation ranges from the source inventory.  In
  Target X, require the Witten \(d_t\), \(d_t+d_t^\dagger\), and
  Hodge-Laplacian Hamiltonian audit as prerequisites for elevating the Hodge
  route.

## Source Equations To Cite Or Audit

CHM:
\[
S_{\rm brane,kin}^{(0)},\quad
\partial_y f_n(0)=-(m_n^2/M_0)f_n(0),\quad
(f,g)_{\rm CHM}=\int fg+\sum_i M_i^{-1}f(y_i)g(y_i),
\]
\[
\partial_y A_\mu|_{y_i}\mp v_i^2 A_\mu(y_i)=0,\quad
\left(m^2/\xi_i-v_i^2\right)\pi_i+v_iA_5|_{y_i}=0,
\]
plus photon subtraction and hatted current extraction.  Cite CHM
Eqs. (2.11)--(2.23), (2.30)--(2.44), and (3.32)--(3.43).

Hodge:
\[
d_t=e^{-th}de^{th},\quad d_t+d_t^\dagger,\quad
H_t=(d_t+d_t^\dagger)^2,
\]
\[
D_Je_J^0=\sqrt J e_J^1,\quad D_J^\dagger e_J^1=\sqrt J e_J^0,\quad
B_J=\begin{pmatrix}0&0\\0&-J\end{pmatrix}.
\]

\(G_2\):
\[
\Phi=\sum_i t_i df_i,\quad \rho=\sum_i t_i\rho_i,\quad \Delta f_i=\rho_i,
\]
\[
f_Q=\sum_i q_i f_i,\quad \rho_Q=\sum_i q_i\rho_i,\quad df_Q(p)=0,
\]
plus flow-line mass terms and trivalent-flow/Yukawa equations.

Endpoint:
\[
|\psi;m,n\rangle,\quad A_a=(A_a)^m{}_n,\quad \Phi^I=(\Phi^I)^m{}_n,
\]
\[
S_{\rm brane}\sim\int\operatorname{Tr}\left[
-\frac{1}{4g_{\rm YM}^2}F^2-\frac12D\Phi D\Phi
+\frac14[\Phi,\Phi]^2+\cdots\right],
\quad
D_a\Phi^I=\partial_a\Phi^I+i[A_a,\Phi^I],
\]
plus \(\langle h|K|h\rangle=0\), \(\langle a|K|a\rangle=J\), and the
off-diagonal product \(J\).

## Scope Connections

Keep one cross-reference sentence per obligation.  O1 supplies
\(P_W,P_Z,P_\gamma\) and \((J_W,J_Z)=(3/4,2)\).  O3 supplies the same-source
scalar package for \(u_-(J)\).  O8 supplies \(\Delta^{(r)}_{\rm match}\) and
the complex-pole chain.  O10 supplies one source variable \(u\), one
\(\Lambda_J(u)\), and the broken-to-unbroken ray.  O20 supplies the common
reduced basis joining Hodge factorization to the CHM current entry.  This loop
adds zero source families, numerical checks, or global compactification program.

## Scores

| Loop | Theorem target | Derived physics | Readability | Reason |
|---|---:|---:|---:|---|
| 34 | 4/5 | 2/5 | 4/5 | O4 has precise entry tests and source ledgers; the determinant entries, ordered sampling, pole matching, and scalar map remain open. |
