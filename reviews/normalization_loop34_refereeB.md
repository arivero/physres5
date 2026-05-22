# Normalization Loop 34 Referee B

Role: string/KK/\(G_2\) mechanism referee for O4.

Status: review only.

## Central O4 Claim

A source route must derive the normalized two-channel kernel
\[
K_J(\lambda)\to
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix},
\qquad
\Sigma_{hh}=0,\quad \Sigma_{aa}=J,\quad
\Sigma_{ha}\Sigma_{ah}=J,
\]
then use the same light space, inner product, scale, and pole map to obtain
the ordered electroweak sampling \((J_W,J_Z)=(3/4,2)\).

## Strongest Route

The interval/CHM Dirichlet-to-Neumann route is the next concrete
source-kernel theorem. It has source-level boundary equations, modified
inner product, vector Robin data, scalar \(A_5/\pi_i\) equations,
custodial bookkeeping, and photon zero-mode accounting. The sharp next
theorem should prove the hatted CHM current entry
\[
\widehat K^{\rm cur}_J(\widehat\lambda)=
\widehat\lambda+\widehat\Sigma^{\rm CHM}_{aa,J}
+O(\widehat\lambda^2),
\qquad
\widehat\Sigma^{\rm CHM}_{aa,J}=J .
\]
The Hodge/SUSY-QM route should remain the companion theorem for
\(\Sigma_{ha}\Sigma_{ah}=J\), since \(D e^0_J=\sqrt J e^1_J\) is the
cleanest source of the square-root entry.

## Weakest Route Inference

Endpoint/Chan-Paton is currently the weakest route as a kernel derivation.
It supplies matrix-valued fields and a plausible scalar/vector arena. It
still must select \(\kappa_J^2=\tau_J=J\), the two-dimensional projection,
and the ordered \((3/4,2)\) sampling. \(G_2\) is less direct than CHM, yet
stronger than endpoint as a localization dictionary because Braun et al.
supply explicit \(f_Q,\rho_Q,df_Q=0\) data.

## Hidden Assumptions

- One source Hilbert space supports \(h_J\), \(a_J\), \(P_W\), \(P_Z\),
  and \(P_\gamma\).
- The CHM product and \(\Lambda_{\rm CHM}\) make both charged
  order-parameter and neutral/current channels dimensionless in the same
  way.
- Photon subtraction fixes a physical zero.
- Extra boundary, Goldstone, \(A_5\), radion, and tower modes decouple or
  block-diagonalize.
- The Hodge/SUSY-QM eigenvalue \(J\) is the same invariant as the CHM
  current \(J\).
- The source kernel survives EFT matching into the transverse W/Z
  complex-pole scheme.
- The negative branch has a gauge-invariant scalar functional.

## Exact Manuscript Revisions Needed

1. In Sec. VI.C, promote the next theorem target to a named CHM
   current-entry theorem centered on
   `eq:chm-boundary-kinetic-source-normalization`,
   `eq:chm-boundary-kinetic-data`,
   `eq:chm-boundary-vector-scalar-data`,
   `eq:chm-current-entry-photon-subtracted`, and
   `eq:chm-current-entry-normalized`.
2. Cite CHM source equations explicitly: Eqs. (2.11)--(2.23),
   (2.30)--(2.44), and (3.32)--(3.43), per
   `context/source_inventory.md`.
3. Add a sentence that the first sharpenable proof is
   \(\widehat\Sigma^{\rm CHM}_{aa,J}=J\). The full determinant also needs
   the off-diagonal square-root theorem.
4. In Sec. VI.F, mark endpoint/Chan-Paton as an arena pending a worldvolume
   quadratic kernel and projection.
5. In Sec. VI.D, add an explicit source-equation audit obligation for
   Braun et al. \(G_2\) Higgs-bundle equations:
   \(\Phi=\sum t_i df_i\), \(\rho=\sum t_i\rho_i\),
   \(f_Q=\sum q_i f_i\), \(\rho_Q=\sum q_i\rho_i\),
   \(df_Q(p)=0\), and flow-line/Yukawa equations.
6. In Appendix D Target X, require source-equation citations for Witten's
   \(d_t=e^{-th}de^{th}\), \(d_t+d_t^\dagger\), and Hodge-Laplacian
   Hamiltonian as prerequisites for elevating the Hodge route.
7. In Sec. VI.G, state the route priority: CHM current entry first;
   Hodge/SUSY-QM square-root entry second; \(G_2\) local kernel third;
   endpoint/Chan-Paton as matrix-arena support.

## Scores

Theorem target: 4/5. The target is precise and source-addressed.

Derived mechanism: 2/5. The ingredients are cited, while the DeVries
entries and ordered W/Z map remain open.
