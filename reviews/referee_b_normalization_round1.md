# Referee B normalization report, round 1

## Central claim

The manuscript's defensible central claim is: the Rivero--de Vries quadratic
\[
x^2+Jx-J=0
\]
defines a two-branch spectral clue whose positive branch is numerically close to the W/Z pole-angle ratio, and whose physical interpretation requires a string/brane/KK/\(G_2\) derivation of the same two-channel determinant plus the ordered assignment
\[
(J_W,J_Z)=(3/4,2).
\]

The present manuscript states a structured research program; it does not yet establish the claim dynamically.

## Strongest source-supported result

The strongest result is the three-route reduction framework in `manuscript/sections/06g_route_comparison.tex`: endpoint/D-brane, interval KK, and localized \(G_2\) mechanisms are all reduced to the same kernel target
\[
\Sigma_{hh}=0,\qquad \Sigma_{aa}=J,\qquad \Sigma_{ha}\Sigma_{ah}=J.
\]
The sources support the existence of the arenas: Chan--Paton/D-brane matrix fields, interval boundary spectra, and singular \(G_2\) localization.  The manuscript correctly separates that support from the still-open DeVries-specific reduction.

## Weakest inference

The weakest inference is the low-energy pole placement of a determinant naturally motivated by high-scale or compactification mechanisms.  This is especially sharp for the \(G_2\) route, where local singularity data plausibly organize representations and couplings, while the W/Z pole interpretation needs a matching theorem.

The second weak point is the ordered sampling rule: the manuscript identifies \(J_H=3/4\) and \(J_{\rm adj}=2\), while the charged W comparison sampling the Higgs/order-parameter invariant remains the central missing derivation.

## Hidden assumptions

- A source theory admits a protected two-dimensional light subspace \(\mathcal H_J=\mathrm{span}\{h_J,a_J\}\).
- Heavy modes can be integrated out without adding extra light channels or changing the determinant class.
- A normalization exists in which both \(\tau_J=J\) and \(\kappa_J^2=J\) hold simultaneously.
- The determinant survives radiative corrections and scheme conversion to complex pole masses.
- The negative branch maps to a gauge-invariant scalar/order-parameter functional, instead of an auxiliary eigenvalue.
- \(G_2\) local data can be matched to the Standard Model global form, anomaly constraints, and electroweak pole observables.

## Exact revisions needed

1. Move all visible section-status paragraphs out of the main body. Put them in Appendix D, `OPEN_ISSUES.md`, or review notes.
2. Rename and rewrite `manuscript/sections/09_status_and_tests.tex` as a journal conclusion. Move claim hierarchy, decision ledger, and referee-facing tests to Appendix D.
3. Keep one compact route-comparison table in the body. Move detailed route ledgers, decision trees, and next-research-pass language from `manuscript/sections/06g_route_comparison.tex` to an appendix or review file.
4. Recast mechanism sections in paper form:
   \[
   \text{source fact}\to\text{model ansatz}\to\text{required equation}\to\text{failure mode}.
   \]
   Avoid project, current draft, useful, owed, hard test, and referee language in the body.
5. Add page-level source audit for the string/KK/\(G_2\) claims recorded in `context/concept_claims_matrix.md`.
6. Strengthen one route with an actual calculation target before further expansion.  The best candidate is the interval route: derive at least one entry, preferably \(\Sigma_{aa,J}=J\), from an explicit boundary action or variational condition in `manuscript/sections/06c_kaluza_klein_boundary.tex`.
7. Demote any stronger wording around the negative branch unless a scalar functional is supplied.  Keep it as an eigenvector obligation, as in Appendix D.

No files were edited by the subagent.
