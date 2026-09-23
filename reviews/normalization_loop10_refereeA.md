# Normalization loop 10 - Referee A

## Central risk

Parent material should enter `physres5` as guardrails and theorem obligations.
The main risk is importing the exact failure mode identified in
`../physres5lineage/weak/criticism.md`: treating DeVries eigenvalues as \(M_W^2\),
\(M_Z^2\), or Higgs-sector quantities before deriving the gauge-boson mass
matrix, scalar functional, or pole self-energy map.

## Strongest useful content

The strongest adjacent import is the `../physres5lineage/weak/criticism.md` checklist:

- Scalar seed entries need a gauge-Higgs or pole-self-energy derivation before
  they can be identified with W/Z observables.
- Higgs/order-parameter claims need a scalar potential minimization or
  gauge-invariant scalar functional.
- Fixing the scale with \(M_Z\) turns W-sector agreement into a descriptive
  clue with a remaining derivation burden.
- Precision comparisons require scheme, uncertainty, and convention control.
- Manuscript prose should remove chat/process provenance.

The useful dimensional note is `../phys3/sources/unbroken_susy.md`, Section V:
it gives local provenance for the \(D=9\leftrightarrow D=11\) interpolation
that O10 is already reconstructing from Witten-source fragments.

## Weakest inference

The weakest inference would be to promote the D=11/D=9 interpolation into a
selected D=10 construction before specifying compact geometry, chirality
mechanism, boundary or singular data, and the vector-scalar operator that
produces the DeVries block.

## Requested updates

- Add adjacent workspace entries to `context/source_inventory.md` as local
  source notes and critique notes.
- Add claim-matrix rows for scalar-seed assignment, negative-branch Higgs
  interpretation, and \(D=9\to10\to11\) interpolation.
- Add O1/O3/O4/O8/O10 refinements in `OPEN_ISSUES.md`.
- Add Lean-style notes for postulate-versus-derivation obligations.

## Language guidance

Use phrases such as source-note provenance, reconstruction target, failure
mode, open derivation, conjectural dimensional interpolation, and descriptive
pole comparison until the matching theorem is supplied.  Avoid prediction,
derivation, and precision language for W/Z/Higgs observables during the
conceptual phase.
