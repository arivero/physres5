# Loop 28 Advisor Report

## Conceptual move

Use a factorization-first proof spine for the normalization pass:

1. Hodge/SUSY-QM factorization supplies the off-diagonal target,
   \[
   D_Je^0_J=\sqrt J e^1_J,\qquad
   D_J^\dagger e^1_J=\sqrt J e^0_J .
   \]
2. The electroweak superconnection assigns the two reduced channels,
   \[
   \Phi_{\rm odd}\mapsto J_H=3/4,\qquad
   F_{\rm even}^{\gamma^\perp}\mapsto J_{\rm adj}=2 .
   \]
3. The CHM interval boundary kernel tests the diagonal current entry,
   \[
   \Sigma_{aa,J}^{\rm CHM}=J .
   \]
4. The negative branch is read from the same eigenbasis as the scalar-functional
   target.

This ordering gives O20 the square-root entry, O1 the ordered labels, O4 the
diagonal current test, and O3 the eigenvector consequence.

## Implementation recipe

- Add a short entry-order paragraph in `06c_kaluza_klein_boundary.tex` after
  the Hodge factorization paragraph.
- In `06g_route_comparison.tex`, state the active pair of tests:
  \(Q_{\rm dR}\to \Sigma_{ha}\Sigma_{ah}=J\) and
  \(K_{\rm CHM}^{\rm cur}\to \Sigma_{aa}=J\).
- In `D_theorem_targets.tex`, cross-reference Target X and Target III.
- In `09_status_and_tests.tex`, replace the broad “derive one entry” sentence
  with the ordered obligation.
- In `OPEN_ISSUES.md`, record this ordering under O4 and O20 as conjectural
  until the projection and breaking operator are derived.

## Score

Advisor score: 4/5.  The manuscript has strong source control and honest
theorem targets.  The readability bottleneck is ordering: valid routes compete
before the reader sees the proof spine.
