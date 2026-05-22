# Normalization Loop 48 Advisor

Role: advisor synthesizing Loop48 referee reports.

Files edited by advisor: none.  
Calculations: none.

## Recommended Conceptual Route

Add Target IIIh: local \(G_2\) flow-overlap product theorem.  It tests whether
localized matter at \(df_Q=0\), normalized local wavefunctions, the
point-support metric, and flow-line/tree data can produce
\[
\widehat\Sigma_{ha,J}^{G_2}\widehat\Sigma_{ah,J}^{G_2}=J
\]
in the same basis, pairing, orientation convention, \(\Lambda_{G_2}\), and
projection convention used for Target IIIg.

## Mechanism To Test

Use a \(G_2\) Higgs-bundle Morse-flow mechanism.  A localized
order-parameter wavefunction \(\psi_{h,J}\) at an isolated-Morse or Morse-Bott
critical set couples to a projected ADE current mode \(a_J^{G_2}\) through an
oriented flow kernel \(\mathcal K_{\rm flow}^{G_2}(\gamma)\) and bilinear maps
\[
B_{ha}^{G_2},\qquad B_{ah}^{G_2}.
\]

## Source To Read

Primary source: Braun, Cizel, Hubner, and Schafer-Nameki, especially the local
Higgs-bundle and flow sections.  The needed source facts are matter
localization, \(f_Q\), flow lines, mass terms, flow trees, orientation signs,
and cancellation of multiple flow contributions.

## Needed Equation

\[
\widehat\Sigma_{ha,J}^{G_2}
=
\Lambda_{G_2}^{-1}
B_{ha}^{G_2}\!\left(
\psi_{h,J},
\mathcal K_{\rm flow}^{G_2}(\gamma)a_J^{G_2}
\right),
\]
\[
\widehat\Sigma_{ah,J}^{G_2}
=
\Lambda_{G_2}^{-1}
B_{ah}^{G_2}\!\left(
a_J^{G_2},
\mathcal K_{\rm flow}^{G_2}(\gamma)\psi_{h,J}
\right),
\]
with
\[
\langle\psi_{h,J},\psi_{h,J}\rangle_{G_Q}=1,\qquad
\langle a_J^{G_2},a_J^{G_2}\rangle_{G_2,u}=1,\qquad
\widehat\Sigma_{ha,J}^{G_2}\widehat\Sigma_{ah,J}^{G_2}=J.
\]

## Exact Edit Set

- `manuscript/sections/06d_g2_localization.tex`: add the flow-overlap subtarget
  after the singular-support pairing and revise the off-diagonal entry
  paragraph.
- `manuscript/sections/D_theorem_targets.tex`: extend Target IIIg and add
  Target IIIh with hypotheses, conclusion, evidence, and failure modes.
- `manuscript/sections/06g_route_comparison.tex`: route-index the proof spine
  and add the \(G_2\) current-entry plus flow-overlap sequence.
- `OPEN_ISSUES.md`: update O4 with Loop48 flow-overlap obligation and rejection
  outputs.
- `context/concept_claims_matrix.md`: update the \(G_2\) local-operator row.
- `notes/lean/O4SourceKernel.lean`: add `Loop48G2FlowOverlapTarget`.

## Projected Scores

Conceptual clarity: 4.75.  
Source control: 4.75.  
String/\(G_2\) depth: 4.75.  
Electroweak correctness: 4.5.  
Open-gap honesty: 5.
