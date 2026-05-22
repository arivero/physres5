# Loop 19 Advisor Report

## New Conceptual Route

Use the CHM interval problem as a Dirichlet-to-Neumann boundary-kernel route.
The source action defines bulk mode equations and endpoint variations.  Solving
the bulk problem with boundary values fixed gives a boundary kernel, and the
brane kinetic/scalar terms add brane-local pieces before projection to
\(\mathcal H_J=\operatorname{span}\{h_J,a_J\}\).

## Mechanism To Test

Boundary scalar vevs and boundary kinetic terms can feed the two required
source channels:
\[
  \partial_y A_\mu\mp v_i^2A_\mu=0,\qquad
  \partial_y f=-\frac{m_n^2}{M_i}f.
\]
The mechanism to test is whether one normalization of endpoint wavefunctions,
brane inertia, and scalar-vector mixing yields both \(\Sigma_{aa,J}=J\) and
\(\Sigma_{ha,J}\Sigma_{ah,J}=J\).

## Source To Read

Use CHM Sections 3.2 and 3.3 for charged/neutral spectra, photon zero mode,
custodial boundary assignments, boundary scalar limits, and brane kinetic
terms.

## Equation Needed

Add the source-data map
\[
S_{5D}[A_M]+\sum_i S_i[\Phi_i,A_\mu]
\Longrightarrow
\left(
\partial_y A_\mu\mp v_i^2A_\mu,\,
\partial_y f+\frac{m^2}{M_i}f,\,
(m^2/\xi_i-v_i^2)\pi_i+v_iA_5
\right)_{\partial I}
\Longrightarrow
K^{\rm int}_J(\lambda)
\Longrightarrow
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix}.
\]
