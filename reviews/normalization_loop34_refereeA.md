# Normalization Loop 34 Referee A

Role: PRD correctness and source-discipline referee for O4.

Status: review only.

## Central Claim

The manuscript frames the DeVries clue as a source-to-pole theorem target:
\[
Q(J)=\mu^2\begin{pmatrix}0&\sqrt J\\ \sqrt J&-J\end{pmatrix},
\qquad
\det K_J(\lambda)=\lambda^2+J\lambda-J,
\]
with trace/determinant data equivalent to
\[
\Sigma_{hh,J}=0,\quad \Sigma_{aa,J}=J,\quad
\Sigma_{ha,J}\Sigma_{ah,J}=J .
\]
The same source package must supply the ordered electroweak map \(J_W=3/4\),
\(J_Z=2\), pole matching, and a scalar interpretation of the negative branch.

## Strongest Source-Supported Result

The interval/CHM route is the strongest target. The draft separates
source-backed boundary ingredients from the DeVries-specific theorem:
CHM supplies eigenvalue-dependent boundary conditions, modified products,
vector Robin data, \(A_5/\pi_i\) scalar equations, photon/custodial
bookkeeping, and a normalized current-entry extraction target. Relevant
locations are `manuscript/sections/06c_kaluza_klein_boundary.tex`,
`manuscript/sections/06g_route_comparison.tex`, and
`manuscript/sections/D_theorem_targets.tex`. The endpoint and \(G_2\)
routes are source-supported as arenas for matrix fields and localized
gauge-matter data, with determinant entries left open.

## Weakest Inference

The weakest inference is the jump from source arenas to the common
normalized \(J\)-entries.  The current manuscript leaves
\(\Sigma_{aa,J}=J\), \(\Sigma_{ha,J}\Sigma_{ah,J}=J\), and
\(\Sigma_{hh,J}=0\) as theorem targets from a stated source action/operator
with a fixed projection and inner product.  The exact pole claim and
scalar-branch claim also remain theorem targets, since
\(\Delta^{(r)}_{\rm match}\), \(\Delta_{\rm O1}\), and
\(\mathcal F_{\rm sc}\) are source-reduction data.

## Hidden Assumptions

- A single reduced Hilbert space contains order-parameter and current
  channels with one inner product and one \(\Lambda_J\).
- The same invariant \(J\) fixes both diagonal trace data and off-diagonal
  mixing data.
- The \(h_J\) channel can be normalized to zero by a physical symmetry,
  boundary condition, or subtraction.
- The photon reference subtraction fixes a physical zero while leaving the
  massive neutral entry fixed.
- Extra light modes decouple or block-diagonalize as a prerequisite for reading
  the \(2\times2\) determinant.
- A boundary or compactification determinant survives matching into the
  complex-pole scheme.
- The negative eigenvector belongs to a gauge-invariant scalar functional
  from the same source package.
- Local \(G_2\) data can be embedded into a global Standard
  Model-compatible compactification with the required charge
  normalization.

## Exact Revisions Needed

1. Add a short current-theorem status sentence after the common route
   target in `manuscript/sections/06g_route_comparison.tex`: the three
   \(\Sigma\)-entries are theorem targets; the interval current entry is the
   first pass/fail target.
2. In the CHM section, define the minimal source data needed for
   \(P_{a,J}\), \(P_\gamma\), \(K^{\rm ref}_{T,J}\),
   \(\Lambda_{\rm CHM}\), and endpoint signs as prerequisites for
   \(\widehat\Sigma_{aa,J}^{\rm CHM}=J\). The open-data list
   around `06c_kaluza_klein_boundary.tex` should become a theorem/pass-fail
   box.
3. In the endpoint section, state in the completion criterion that
   Chan-Paton and brane Higgsing source the matrix arena and still require
   a worldvolume quadratic kernel and projection for
   \(\kappa_J^2=\tau_J=J\).
4. In the \(G_2\) section, label \(\Sigma_{aa,J}^{G_2}=J\) and the
   flow-overlap product as local conjectural entry targets pending a local
   operator and inner product.
5. Tie the same-source scalar obligation directly to the route comparison:
   the scalar map in `06g_route_comparison.tex` should cite the Appendix D
   condition that the first five package entries match the vector pole
   package.
6. Keep every exact pole-ratio display paired with a remainder pending the
   matching theorem.

## Scores

Theorem target: 4/5. The target is sharp: common kernel,
trace/determinant entries, route-specific dictionaries, ordered W/Z
sampling, pole matching, and same-source scalar obligations are named.
The first pass/fail derivation should be isolated as one calculation
problem.

Derived physics claim: 1/5. The draft has derived algebra for \(Q(J)\)
and strong source discipline for candidate arenas. The dynamical source of
\(Q(J)\), the ordered \(3/4,2\) electroweak sampling, the pole matching
remainder, and the scalar functional remain open.
