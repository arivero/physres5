# Referee A normalization report, round 1

## Central claim

The manuscript claims that the Rivero--de Vries quadratic
\[
x^2+Jx-J=0,\qquad J=s(s+1)
\]
has a positive-branch quotient
\[
1-\frac{x_+(3/4)}{x_+(2)}=0.22310132\ldots
\]
close to the weak angle defined from the W/Z pole-mass ratio, and that this algebraic coincidence may indicate a two-channel string/Kaluza--Klein/boundary spectral origin.  In its current form this is a structured conjectural program, not yet a derived electroweak result.

## Strongest source-supported result

The strongest physics is the scheme-aware electroweak setup: the manuscript correctly separates the pole ratio from \(\overline{\rm MS}\) angles, effective weak mixing angles, line-shape masses, and high-scale GUT values.  The tree-level gauge-Higgs mass matrix and projective ray in `manuscript/sections/04_electroweak_embedding.tex` are standard and source-supported.  The algebra of \(Q(J)\), roots, trace, and determinant in `manuscript/sections/02_casimir_operator.tex` is exact.

## Weakest inference

The weakest inference is the ordered assignment
\[
(J_W,J_Z)=(3/4,2)
\]
from the Higgs doublet and adjoint current data.  The manuscript is honest that this is open, but the body still sometimes lets the assignment function like a working interpretation.  Both W and Z are vector poles after symmetry breaking, while \(J=3/4\) is assigned to the Higgs/order-parameter side.  The text identifies plausible representation invariants, but it does not derive why the charged vector comparison samples the doublet invariant.

A close second is the negative-branch scalar interpretation.  The near-Higgs/order-parameter-scale statement remains numerological until a gauge-invariant scalar functional and scheme are fixed.

## Hidden assumptions

- The clean DeVries value is assumed to attach to low-energy complex poles, although no dynamical pole condition has been derived.
- The quoted pole comparison still depends on unaudited seed inputs and placeholder arithmetic.
- The Breit-Wigner to pole conversion is stated but not used in a current W/Z table with propagated uncertainties.
- The same two-channel determinant is assumed to control vector pole data and scalar/order-parameter data.
- The \(J=3/4,2\) sampling is assumed to be selected by gauge-Higgs structure rather than post-selection.
- The zero entry \(\Sigma_{hh}=0\), trace entry \(\Sigma_{aa}=J\), and mixing product \(\Sigma_{ha}\Sigma_{ah}=J\) are route targets, but no source theory fixes them.
- The near-Higgs-scale reading assumes a normalization by \(M_Z^2=\mu^2x_+(2)\) whose physical status is open.

## Exact revisions needed

1. Replace all process language in the main body: current draft, project, seed arithmetic, referee-facing, next calculation, ledger, and decision tree. Keep the content, but recast it as definitions, assumptions, propositions, and open problems.
2. Move all visible `\paragraph*{Section status.}` paragraphs out of the paper body or convert them into short theorem/open-problem statements.
3. In Sec. III, finish the pole-mass scheme audit before making any numerical comparison. Add a table with quoted input convention, \(M_{\rm BW}\), \(\Gamma_{\rm BW}\), converted \(M_{\rm pole}\), uncertainty propagation, and resulting \(\sin^2\theta_{\rm pole}\). Until then, remove or demote the near-conventional-averages statement.
4. Define the complex-pole convention fully. State whether \(s_p=(M_p-i\Gamma_p/2)^2\) is being approximated or whether \(s_p=M_p^2-iM_p\Gamma_p\) is the definition. Then state the exact relation to the variable-width Breit--Wigner convention used for W/Z inputs.
5. In the abstract, soften the scalar-scale statement so it is clearly conjectural.
6. In Sec. IV, keep the electroweak mass-matrix derivation, but explicitly state that Eq. \((J_W,J_Z)=(3/4,2)\) is a theorem target requiring an additional map.
7. In Sec. V, make the scalar-side reading conditional on deriving and normalizing the same determinant by the vector spectrum.
8. In route sections, reduce analogy claims. Keep only source-supported addresses for boundary data, towers, localized gauge sectors, and scalar moduli. Mark exact DeVries entries as unproved.
9. Convert Sec. IX into a PRD-style conclusion: what is derived, what is assumed, what must be calculated. Move route-selection workflow and referee checklist material to Appendix D or `reviews/`.
10. Update `OPEN_ISSUES.md` after the normalization pass by splitting O2 into two tasks: pole-convention formula and current-input numerical audit.

## Referee judgment

The manuscript is strongest when it presents a precise algebraic coincidence plus a disciplined list of derivational obligations.  It becomes vulnerable whenever conjectural placement, ordered sampling, or scalar-branch interpretation reads like physics already obtained.  The next paper-normalization pass should narrow the main claim, complete the pole-scheme comparison, and move research-process scaffolding out of the body.

No files were edited by the subagent.
