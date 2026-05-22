# Loop 28 Open-Issue Completion Audit

Objective audited: normalize the paper according to
`reviews/paper_normalization_plan.md` and `reviews/referee_advisor_cycle.md`
while actively working `OPEN_ISSUES.md`.

## Requirements derived from the objective

- The manuscript body should read as physics exposition: definitions,
  assumptions, constructions, consequences, and theorem targets.
- Process and review material should live in appendices or repo notes.
- Every substantial loop must use two referee subagents and one advisor
  subagent, then record the reports.
- Remaining analytical gaps must be visible in `OPEN_ISSUES.md`, source
  ledgers, and Lean-style notes.
- Verification for this phase is `make manuscript`.

## Loop 28 status

The loop actively worked O1, O4, O10, and O20 by replacing the CHM
current-entry target with hatted variables and a source scale \(\Lambda_J\).
This prevents a physical boundary kernel from being compared to the
dimensionless DeVries entry before the source normalization is specified.

The loop also added a proof-spine ordering:
\[
{\rm Hodge/SUSY\text{-}QM}\to \Sigma_{ha,J}\Sigma_{ah,J}=J,\qquad
{\rm CHM}\to\widehat\Sigma_{aa,J}^{\rm CHM}=J .
\]
Both entry tests now require one reduced basis, one source scale, one
projection, and one pole map.

## New issue noticed

CHM convention audit.  Before equation-level derivation of
\(\widehat\Sigma_{aa,J}^{\rm CHM}=J\), the rendered CHM PDF must be inspected
for endpoint signs, dimensions of boundary kinetic terms, scalar-product
normalization, photon projection, and the variables entering
\(K^{\rm brane}_{T,J}\).  This is now recorded as an O4 refinement.

## Completion state

The full goal remains open.  O1, O3, O4, O8, O10, O17, O18, O19, and O20 still
contain derivational obligations.  This loop raises the evidentiary standard
for O4 and supplies a clearer manuscript spine for the next derivation pass.
