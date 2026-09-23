# Milestone execution summary -- 2026-05-25

## Global result

All seven milestones in `loop/long-term-devries-research-plan.md` now have an
execution note.  The current construction remains a D10 compatibility framework,
not a proof that the de Vries relation is forced.  The scoped theorem is now
recorded in `current-route-no-prediction-theorem-2026-05-25.md`: under the
current D8/O8/Payen/RR assumptions, at least one mandatory pass condition fails
on every route that would make the de Vries number predictive.
The completion audit is recorded in
`goal-completion-audit-2026-05-25.md`.

The main fork is:

1. finite current branch: can select `j=0,1/2,1`; the leading candidate is now
   the zero-mode image operator `mu^2 A_jA_j^dagger` on `Im A_j`, but the raw
   Wilson contact has residue `J_j`, not the unit residue required by the
   finite Feshbach pole; the inverse image metric itself is the static Schur
   complement of the retained `q_j` oscillator, and the Wilson second
   derivative is a connected current response rather than an extra direct 1PI
   contact when `q_j` is retained; a generic local `q_j` oscillator leaves a
   residue ratio `r=gamma/alpha`, while a single current-displacement square
   forces `r=1`; the mixed Hom sector
   `H^0(CP1,Hom(O(0),O(2j)))=V_j` supplies a candidate image displacement via
   the isometry `A_j/sqrt(J_j)`, but the current D10 boundary package has not
   derived the required one-square Hom action; the Payen endpoint action gives
   Wilson tensors, and the D8 DBI/WZ source package gives geometric/topological
   brane data, but neither derives the Hom square in the current action;
2. rotor tower branch: naturally gives the `mu^2j(j+1)` gap, but allows
   `j=3/2` and higher states, including the `96.54 GeV` diphoton test.

## Milestone decisions

| Milestone | Execution note | Decision |
|---|---|---|
| 1. Feshbach kernel | `milestone-execution-2026-05-25.md`, `milestone1-q-channel-source-tests-2026-05-25.md`, `milestone1-boundary-rotor-casimir-gap-candidate-2026-05-25.md`, `milestone1-rotor-stress-test-2026-05-25.md`, `milestone1-finite-zero-mode-image-operator-2026-05-25.md`, `milestone1-finite-image-local-origin-test-2026-05-25.md`, `milestone1-wilson-contact-residue-calculation-2026-05-25.md`, `milestone1-1pi-contact-bookkeeping-2026-05-25.md`, `milestone1-connected-1pi-wilson-test-2026-05-25.md`, `milestone1-q-oscillator-coefficient-lock-2026-05-25.md`, `milestone1-current-displacement-square-origin-test-2026-05-25.md`, `milestone1-mixed-hom-displacement-test-2026-05-25.md`, `milestone1-mixed-hom-local-action-source-test-2026-05-25.md` | Bare action fails.  Augmented kernel works.  The finite image-channel candidate requires a unit contact.  Raw Wilson expansion gives residue `J_j`; the unit inverse image metric is the static Schur complement of the retained `q_j` oscillator.  The Wilson second derivative is a connected response, so it is not an extra direct 1PI contact when `q_j` is retained.  A generic local oscillator leaves `r=gamma/alpha`; a single current-displacement square forces `r=1`.  The mixed Hom sector gives the right finite field content through `Q_j=A_jy_j/sqrt(J_j)`, but Payen plus D8 DBI/WZ does not derive the one-square Hom action that locks the coefficient. |
| 2. `j=0,1/2,1` assignment | `milestone2-representation-assignment-execution-2026-05-25.md` | Passes only on a finite `SU(2)_2` branch.  Borel-Weil alone gives a tower. |
| 3. Current metric | `milestone3-current-metric-execution-2026-05-25.md`, `milestone3-d8-rr-full-current-placement-test-2026-05-25.md` | Full-current branch gives `kappa_cur=1`.  Horizontal-only branch gives `kappa_cur=0.752739...` and fails the weak-angle test.  The current D8/Payen/RR source package does not derive that the boundary image channel uses the full Bailin-Love current rather than the horizontal `CP1` current. |
| 4. Bulk vacuum coefficients | `milestone4-5-vacuum-selector-execution-2026-05-25.md`, `milestone4-5-vacuum-rank-selector-test-2026-05-25.md` | Scaling equations are concrete, but coefficients and `mu_B(rho,tau)` are not computed.  The rank test shows two stationarity equations for seven coefficients; e.g. `B_4=B_R tau^2` and `B_loc=-(2/3)B_R tau rho^-2` make any chosen `rho` stationary in a reduced coefficient slice.  Together with the Milestone 6 source-balance no-go, the current localized coefficient is not a valid global source coefficient for the D8/O8 route. |
| 5. Selector potential | `milestone4-5-vacuum-selector-execution-2026-05-25.md`, `milestone4-5-vacuum-rank-selector-test-2026-05-25.md`, `milestone5-neutral-scalar-hessian-rank-test-2026-05-25.md` | `kappa_cur` is removed on the full-current branch.  On the selector branch the squared selector terms have zero `rho,tau` derivatives, so they do not select the bulk moduli.  The neutral scalar Hessian test shows that a one-field radial potential has two free coefficients for the two scalar targets `h_0^2=2J_v mu_B^2` and `M_h^2=J_H mu_B^2`; adding neutral mixing turns the mass target into one spectral constraint on a larger Hessian.  Thus `v_Q` and `lambda_H` remain compatible scalar targets, not induced coefficients. |
| 6. Consistency checks | `milestone6-consistency-execution-2026-05-25.md`, `milestone6-source-balance-table-2026-05-25.md`, `milestone6-lower-charge-cancellation-test-2026-05-25.md`, `milestone6-h-flux-cancellation-test-2026-05-25.md`, `milestone6-k-theory-cancellation-test-2026-05-25.md`, `milestone6-image-lower-charge-sector-test-2026-05-25.md`, `milestone6-o4-image-realization-test-2026-05-25.md`, `milestone6-o4-o6-source-table-test-2026-05-25.md`, `milestone6-source-balance-no-go-2026-05-25.md`, `milestone6-extra-mode-mass-gap-table-2026-05-25.md`, `milestone6-replacement-source-requirements-2026-05-25.md`, `milestone6-source-branch-decision-2026-05-25.md` | Local spin-c, photon, D8 convention, and reduced positivity checks pass.  The global source-balance check fails for the current D8/O8 package.  Endpoint data cannot cancel lower charges; closed `H` and K-theory cannot erase them; and the tested O4/O6 package fails the D6/D4 congruence test.  The replacement-source equations show that the minimal cohomological repair is `-h_Q^2` on the balanced opposite-lift endpoint choice; any D6-bearing repair must satisfy the `16Z h_Q` endpoint lattice.  The branch decision rejects this as a patch: an anti-D4, O4-only source, or generic D6-bearing source changes the source content/topology and forces a new source table, vacuum, mode spectrum, and backreaction calculation.  The extra-mode check also fails for the current action: an unprojected image field has a massless complement, the Hom route removes it only on the compatible branch whose one-square action is not derived, and the rotor branch keeps a light tower beginning at `96.54 GeV`.  Thus the current route is not a global compactification proof. |
| 7. Phenomenology | `milestone7-phenomenology-execution-2026-05-25.md` | Current W/Z data give a `1.5 sigma` on-shell pull.  No threshold/running prediction.  The `j=3/2` tower mass is `96.54 GeV`, near the CMS `95.4 GeV` feature but with no production calculation. |

## Next work order

The next calculation should not be another broad traversal.  The bottleneck is
now narrow:

1. treat the current D8/O8 compactification branch as closed for proof claims;
2. formulate a new compactification ansatz with changed source content/topology
   only if the project continues beyond the scoped branch.

The source table has exposed an explicit lower-charge obstruction, and the
scalar Hessian rank test removes the nearest Higgs-sector shortcut.
The milestone execution objective is complete for the scoped current route.
