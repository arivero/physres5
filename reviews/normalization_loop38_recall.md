# Loop 38 Random Recall

## Draw

- Bibliography: `Logan2022`.
- Lean note: `notes/lean/SuperconnectionAssignment.lean`.
- Source fragment: `context/source_fragments/06_tong_gauge_theory_notes/pages_171-180.md`.

## Source Read

`Logan2022` is the scalar-sector and custodial-reference source for Higgs
physics.  It supports the O3/O20 scalar-side caution through the standard Higgs
sector.

The superconnection Lean note already records the ordered-assignment test:
\(\Phi_{\rm odd}\mapsto J_H=3/4\), \(F_{\rm even}^{\gamma^\perp}\mapsto
J_{\rm adj}=2\), photon preservation, electroweak-ray preservation, trace-space
separation, and the pole remainder.

Tong gauge-theory pages 171--180 record
\[
\sum_a Q_a^3=0,\qquad \sum_a Q_a=0,\qquad
d^{abc}(R)=\operatorname{tr}T^a\{T^b,T^c\},
\]
and the real/pseudoreal representation cancellation pattern.

## Consequence

The O1/O20 superconnection route carries an anomaly-ledger obligation if new
gauge-Higgs or fermionic channels enter the finite source basis.  The obligation
is now recorded in `context/source_inventory.md` and
`notes/lean/SuperconnectionAssignment.lean`.
