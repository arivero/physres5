# Loop 28 Referee B Report

## Sharpest normalization defect

The CHM current-entry target mixes a physical, dimensionful boundary kernel
with the dimensionless DeVries entry \(J\).  The displayed target in Sec. VI.C,
Sec. VI.G, and Appendix D writes
\[
K^{\rm cur}_J(\lambda)
=
\lambda+\Sigma_{aa,J}^{\rm CHM}
+O(\lambda^2/\Lambda_{\rm KK}^2),
\qquad
\Sigma_{aa,J}^{\rm CHM}=J .
\]
The text still owes a declared dimensionless normalization for \(\lambda\),
\(K^{\rm cur}\), the Dirichlet-to-Neumann kernel, brane terms, and \(J\).

## Recommended edits

Use hatted variables:
\[
\widehat\lambda=\frac{\lambda}{\Lambda_J^2},
\qquad
\widehat K^{\rm cur}_J
=
\Lambda_J^{-2}K^{\rm cur}_J .
\]
Define \(\Lambda_J\) as the source scale that makes the spectral variable
dimensionless.  The CHM current theorem should read
\[
\widehat K^{\rm cur}_J(\widehat\lambda)
=
\widehat\lambda+\widehat\Sigma_{aa,J}^{\rm CHM}
+O(\widehat\lambda^2),
\qquad
\widehat\Sigma_{aa,J}^{\rm CHM}=J .
\]
The open data are \(P_{a,J}\), \(K^{\rm ref}_{T,J}\), \(\Lambda_J\),
endpoint-normal conventions, photon projection, the ordered W/Z boundary map,
and the map
\(\widehat\lambda\mapsto m_n^2/\Lambda_J^2\mapsto\Pi_T^{(4)}(s)\).

## Issue-ledger updates

- O4 needs the hatted CHM target and the derivation of \(\Lambda_J\).
- O1 needs the common dimensionless normalization for the \(J_H=3/4\) and
  \(J_{\rm adj}=2\) samples.
- O10 needs \(\Lambda_J(u)\) and wavefunction normalizations inside the
  middle-dimensional Schur-complement data.

## Score

Progress after applying the recommendations: 5/5 for normalization discipline.
The central derivations remain open and properly labeled as theorem targets.
