# Loop 39 Random Recall

## Draw

- Bibliography: `BraunEtAl2019`.
- Lean note: `notes/lean/NegativeBranchScalar.lean`.
- Source fragment: `context/source_fragments/06_tong_gauge_theory_notes/pages_071-080.md`.

## Source Read

`BraunEtAl2019` remains a local \(G_2\) Higgs-bundle source for gauge sectors,
matter localization, and mass/Yukawa data tied to one geometric input.

`NegativeBranchScalar.lean` records the same-source scalar-functional
obligation: the negative eigenvalue needs a gauge-invariant scalar functional,
the same operator as the positive branch, a shared or declared normalization,
and a stated observable kind.

Tong gauge-theory pages 71--80 record instanton collective coordinates,
scale-size integration, the running Yang--Mills coupling, the one-loop beta
function with \(C({\rm adj})\), and the RG-invariant scale.

## Consequence

The Coquereaux superconnection route now carries two extra reminders.  First,
its source-internal weak-angle normalizations live in a classical algebraic
ledger; the manuscript's pole statement requires a renormalized matching
ledger.  Second, the odd Higgs slot supports O3/O20 through a same-source scalar
functional tied to the vector branch.  The first point is recorded in
`context/source_inventory.md`; the second is recorded in
`notes/lean/NegativeBranchScalar.lean`.

## Extra Note Review

Random follow-up draw:

- Lean note: `notes/lean/DeVriesProgram.lean`.
- Source fragments:
  `context/source_fragments/19_logan_higgs_physics_tasi_1406_1786/pages_021-030.md`,
  `context/source_fragments/48_fayet_susy_sm_higgs_z_partner_1403_5951/pages_001-010.md`,
  `context/source_fragments/44_salam_strathdee_on_kaluza_klein_theory_ic_81_211/pages_011-020.md`,
  and `context/source_fragments/02_tong_string_theory_notes/pages_031-040.md`.

`DeVriesProgram.lean` reviews the core obligations: pole-placement clue status,
radical attachment, electroweak mass-map theorem, electroweak-ray admissibility,
the adjoint-boson posture, negative-branch scalar map, and flavor boundary.
Loop 39 stays aligned with these obligations by treating Coquereaux as a finite
source arena whose projection, normalization, branch map, and pole chain remain
theorem data.

The source fragments add four reminders.  Logan pages 21--30 identify off-shell
Higgs decays, loop-induced \(\gamma\gamma\), \(gg\), and \(Z\gamma\) channels,
and top/W loop roles as Higgs-observable context.  Fayet pages 1--10 supply the
spin-zero BEH partner-of-\(Z\) vocabulary inside massive supersymmetric gauge
multiplets.  Salam--Strathdee pages 11--20 supply the \(G/H\) harmonic expansion,
\(H\)-content selection, and zero-mode Yang--Mills reduction.  Tong string pages
31--40 supply the constrained transverse oscillator expansion and Virasoro-mode
constraints.  These reminders reinforce the current theorem posture: scalar,
KK, and string routes require an explicit projection/constraint map to carry the
DeVries radical.
