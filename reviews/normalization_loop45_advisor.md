# Loop 45 Advisor

Role: advisor synthesizing the two referee reports into an implementation
package.

Files changed by advisor: zero.  Numerical scripts: untouched.

## Implementation Package

Make the CHM current-entry package a shared admissibility lemma across Sec.
VI.C, Sec. VI.G, Target 0, Target III, and Target X.

The lemma should define
\[
\widetilde a_\gamma=P_\gamma a_\gamma^{(0)},\qquad
\widetilde z_J=P_{a,J}\Pi_{\gamma^\perp}^{(T)}z^{(0)}
\]
and require positive projected norms, photon-orthogonality preservation,
source-ordered or commuting projectors, photon-reference subtraction, a shared
\(\Lambda_{\rm CHM}\), and a current-slope datum
\[
Z_J^{\rm cur}
=\partial_{\widehat\lambda}\widehat K_J^{\rm cur}(0)>0.
\]
The comparison with \(J\) should use the canonical kernel
\[
\widehat K_{J,{\rm can}}^{\rm cur}
=(Z_J^{\rm cur})^{-1}\widehat K_J^{\rm cur}.
\]

## Equation Target

The first neutral-current pass/fail theorem is
\[
\widehat K_{J,{\rm can}}^{\rm cur}(\widehat\lambda)
=\widehat\lambda+\widehat\Sigma_{aa,J}^{\rm CHM,can}
+O(\widehat\lambda^2),
\qquad
\widehat\Sigma_{aa,2}^{\rm CHM,can}=2.
\]
The same source package then carries
\[
\Delta_W^{\rm CHM},\quad
\Delta_Y^{\rm CHM},\quad
\Sigma_{ha,J}\Sigma_{ah,J},\quad
\Delta_{\rm O1/O10}.
\]

## Ledger Updates

Update O1, O4, the concept matrix, and `notes/lean/CHMCurrentEntry.lean` so the
admissibility lemma becomes the shared object referenced by the manuscript.

## Scores

Post-edit target: conceptual clarity 4.5; source control 4.5; electroweak
correctness 4.5; proof-spine quality 4.25; PRD prose 4; open-gap honesty 5.
