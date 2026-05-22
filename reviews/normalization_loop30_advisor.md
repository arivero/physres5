# Loop 30 Advisor Report

## Conceptual Improvement

Make the CHM interval/current-entry route the first attempted
source-controlled derivation, centered on
\[
\widehat\Sigma_{aa,J}^{\rm CHM}=J.
\]
State it as a pass/fail source theorem: CHM boundary variation, boundary
kinetic product, transverse projection, photon subtraction, and source scale
\(\Lambda_J\) determine the entry or reject the interval route as the active
derivation.

## Mechanism To Test

Test the transverse boundary impedance mechanism
\[
K^{\rm DtN}_{T,J}(\lambda)
+K^{\rm brane}_{T,J}(\lambda)
-K^{\rm ref}_{T,J},
\]
expanded at small \(\lambda\), with
\(a_J=P_{a,J}A_\mu^{T,\partial}\) normalized by the CHM product.  Use the
photon zero mode as the reference channel and require one
\(\Lambda_{\rm CHM}\) convention for \(J_H=3/4\) and \(J_{\rm adj}=2\).

## Source Passage

Inspect the rendered CHM PDF:

- Eqs. (2.11)--(2.23): boundary kinetic term, eigenvalue-dependent boundary
  condition, modified scalar product.
- Eqs. (2.30)--(2.44): gauge fixing, \(A_5/\pi_i\) boundary equations, vector
  Robin data.
- Eqs. (3.35)--(3.43): photon zero mode, W/Z towers, custodial defect, brane
  kinetic remedy.

## Equation Needed

Add a source-audit equation defining the reference subtraction:
\[
P_\gamma^\dagger
\left(K^{\rm DtN}_{T}+K^{\rm brane}_{T}-K^{\rm ref}_{T}\right)
P_\gamma=0,
\]
and the candidate current entry
\[
\widehat\Sigma_{aa,J}^{\rm CHM}
=
\frac{1}{\Lambda_{\rm CHM}^2}
\left[
\left\langle a_J,K_T(0)a_J\right\rangle_{\rm CHM}
-
\left\langle a_\gamma,K_T(0)a_\gamma\right\rangle_{\rm CHM}
\right].
\]

## File Targets

- `manuscript/sections/06c_kaluza_klein_boundary.tex`
- `manuscript/sections/06g_route_comparison.tex`
- `manuscript/sections/D_theorem_targets.tex`
- `context/source_inventory.md`
- `context/concept_claims_matrix.md`
- `OPEN_ISSUES.md`
- `notes/lean/CHMCurrentEntry.lean`

## Score

5/5 as a high-risk, source-controlled improvement.
