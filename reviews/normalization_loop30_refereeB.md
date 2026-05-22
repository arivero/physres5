# Loop 30 Referee B Report

## Central Claim

The CHM interval/current-entry route should be stated as a source-controlled
theorem target.  CHM supplies variational boundary conditions,
eigenvalue-dependent brane kinetic terms, the modified scalar product,
gauge-fixing structure, vector Robin data from boundary scalar vevs,
\(A_5/\pi_i\) scalar equations, and photon/custodial boundary bookkeeping.
The DeVries-specific claim remains
\[
\widehat K^{\rm cur}_J(\widehat\lambda)
=
\widehat\lambda+\widehat\Sigma_{aa,J}^{\rm CHM}
+O(\widehat\lambda^2),
\qquad
\widehat\Sigma_{aa,J}^{\rm CHM}=J.
\]

## Strongest Source-Supported Improvement

Add a CHM current-entry convention lemma:
\[
\partial_y f_\lambda|_{y_i}\sim
-\frac{\lambda}{M_i}f_\lambda(y_i),
\qquad
(f,g)_{\rm CHM}
=
\int fg+\sum_i M_i^{-1}f(y_i)g(y_i),
\]
with the gauge-sector boundary facts
\[
\partial_y A_\mu|_{y_i}\mp v_i^2 A_\mu(y_i)=0,
\qquad
\left(\frac{m^2}{\xi_i}-v_i^2\right)\pi_i+v_iA_5|_{y_i}=0.
\]
This separates source facts from the DeVries target and gives the interval
route a derivation interface.

## Weakest Inference

CHM gives coefficients built from boundary kinetic terms, scalar vevs, gauge
couplings, interval size, endpoint signs, and group embeddings.  The universal
Casimir label \(J\), shared source scale \(\Lambda_J\), and common
normalization for \(J_H=3/4\) and \(J_{\rm adj}=2\) remain open.

## Hidden Assumptions

- The scalar-product formula extends to the transverse gauge-current trace.
- Rendered-PDF inspection fixes endpoint signs and dimensions.
- \(K^{\rm ref}_{T,J}\) is fixed by symmetry or photon subtraction.
- \(\Lambda_J\) comes from the source action.
- \(P_{a,J}\) decouples extra light channels and preserves the photon zero
  mode.
- Gauge-fixing dependence cancels from the physical transverse entry.
- The small-\(\widehat\lambda\) expansion maps to \(m_n^2\) and then to
  \(\Pi_T^{(4)}(s)\).
- The Hodge/SUSY-QM off-diagonal test and the CHM diagonal-current test share
  one reduced Hilbert space.

## Exact Edit Targets

- `manuscript/sections/06c_kaluza_klein_boundary.tex`: convert the CHM source
  paragraph into a convention lemma and add the hatted-current proof packet.
- `manuscript/sections/06g_route_comparison.tex`: keep route-level acceptance
  criteria and point details to Sec. VI.C.
- `manuscript/sections/D_theorem_targets.tex`: make the CHM current extraction
  a named subtarget with hypotheses, conclusion, and failure mode.
- `context/source_inventory.md` and `context/concept_claims_matrix.md`: record
  the rendered-PDF inspection and split source facts from theorem data.
- `OPEN_ISSUES.md`: update O4 and cross-reference O1, O8, O10, and O20.

## Score

5/5.  The loop should improve source control and keep the equality to \(J\) as
an explicit theorem target.
