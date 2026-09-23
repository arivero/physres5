# Long-term de Vries research plan -- 2026-05-25

## Status

The present D10 construction has not proved the de Vries relation as a forced
prediction.  The current D8/O8 boundary-current route is now closed as a proof
branch by `loop/current-route-no-prediction-theorem-2026-05-25.md`.
The milestone execution objective is audited in
`loop/goal-completion-audit-2026-05-25.md`.

Traversal record: `loop/devries-milestone-traversal-2026-05-25.md` walks
across all seven milestones and records the current decision for each one.

Execution record: `loop/milestone-execution-2026-05-25.md` starts the actual
milestone execution.  Milestone 1 now has a decision: the bare D10 boundary
action does not force the Feshbach kernel; the kernel is obtained only in the
augmented action where `S_quad^(j)` is added.

What is established now:

- The D10 carrier/probe picture is coherent:
  `M4 x CP2 x CP1`, the M-circle/RR one-form, the D0 probe, and the D8-like
  boundary carrier `W9=M4 x CP2 x S1_Q` fit into one Type IIA layer.
- The boundary action can carry endpoint spaces
  `V_j=H^0(CP1,O(2j))` for `j=0,1/2,1`.
- The endpoint spaces give the Casimirs `J=j(j+1)`, hence `0,3/4,2`.
- Given the Feshbach boundary kernel, the pole equation is
  `X=J/(X+J)`.
- The canonical KK current metric fixes `kappa_cur=1` when the boundary
  Schur/Payen channel uses the same orthonormal current frame as the weak gauge
  metric.
- A coupled selector potential can place
  `rho,tau,v_Q,lambda_H,kappa_cur` on a de Vries-compatible branch.

The unproved step is the forcing step: the construction must derive the
Feshbach kernel, its coefficient, and the vacuum selector from the local
D10/string/brane dynamics rather than adding them as compatible structures.
For the scoped D8/O8/Payen/RR package tested here, that forcing step fails.

## Research goal

Turn the present result from:

```text
D10 boundary data are compatible with de Vries.
```

into one of the two final outcomes:

```text
The D10 boundary dynamics force the de Vries relation.
```

or

```text
The D10 boundary dynamics do not force the de Vries relation; the present
agreement is a compatible placement, not a prediction.
```

## Milestone 1 -- Derive the Feshbach kernel from the boundary action

Execution decision: failed for the bare boundary action, passed only for the
augmented model with `S_quad^(j)` included as an extra local quadratic channel.
The next source test narrows the augmented channel: `q_j` should be treated as
the first propagating boundary-current oscillator in `Im A_j`, not as a generic
auxiliary field.
The current constructive candidate is a boundary rotor/current oscillator whose
Hamiltonian is the zero-mode Casimir, `H=(2I)^-1 C_2`, with `1/(2I)=mu^2`.
Finite-branch update: the stronger finite candidate is the zero-mode image
operator `mu^2A_jA_j^dagger` on `Im A_j`.  It gives the same denominator without
introducing the Peter-Weyl rotor tower.  Completing the square fixes the
required contact as `-\mu^2`.  The raw Wilson second variation gives
`-\mu^2J_j`, while an inverse image metric gives the required unit residue.
The inverse image metric is also the static Schur complement of the retained
`q_j` oscillator, so the finite branch now depends on whether the raw Wilson
`T_aT_b` term appears as a separate direct 1PI contact.  The endpoint action is
linear in the source, so the Wilson second derivative is a connected
two-current response.  When `q_j` is retained, that response is represented by
`q_j` exchange and should not be added again as a direct 1PI term.  A generic
local oscillator leaves a dimensionless residue ratio `r=gamma/alpha`; a single
current-displacement square forces `r=1`, with the common coefficient absorbed
into the boundary scale.  The current D10 boundary package does not identify the
needed `Im A_j` displacement field; DBI supplies the right square mechanism for
a brane displacement, but the bare normal displacement is not an `Im A_j`
boundary-current field.  The mixed Hom sector
`H^0(CP1,Hom(O(0),O(2j)))=V_j` passes the rank test: for `j>0`,
`Q_j=A_jy_j/sqrt(J_j)` is an image displacement.  The current action still has
to derive the single Hom square `||sqrt(J_j)y_j-p_j||^2`; a generic mixed
sector leaves the residue ratio free.  The Payen endpoint source and D8 DBI/WZ
package in the current action do not derive this Hom square, so the finite
branch remains compatible rather than predictive unless a new local
open-string field theory input supplies it.

Current input:

```tex
S_quad^(j)
= <p_j,Bp_j> + <q_j,(B+mu^2J_j)q_j>
 -mu^2<q_j,A_jp_j> -mu^2<A_jp_j,q_j>.
```

Current output:

```tex
Gamma_j(B)=B-mu^4J_j/(B+mu^2J_j),
qquad
X=J_j/(X+J_j).
```

Needed derivation:

- Start from the local D8-like boundary action on `W9`.
- Identify the actual boundary/vector channel `p_j`.
- Derive the first propagating boundary-current oscillator and identify it
  with the image channel `q_j`.
- Derive the diagonal term `B+mu^2J_j`.
- Derive the boundary moment of inertia relation `1/(2I)=mu^2` if the rotor
  realization is used.
- Derive the off-diagonal coefficient `mu^2 A_j`.
- Derive the retained local `q_j` oscillator from the D10 boundary dynamics.
- Derive a current-displacement square, or another coefficient-lock mechanism
  that enforces `gamma=alpha`.
- If the finite branch is kept, add a source-backed local open-string field
  theory derivation of the Hom one-square action.
- Prove that the leading image-current pole is positive and dominates.
- Prove the sign.
- Prove the spectral measure is positive and effectively single-pole in the
  regime used for the W/Z relation.

Pass condition:

```tex
rho_j(nu)=mu^4 J_j delta(nu-mu^2 J_j)
```

or a derived positive spectral density whose low-energy pole gives the same
coefficient without tuning.

Fail condition:

The local boundary action gives a different coefficient, multi-pole structure,
wrong sign, or nonuniversal normalization. Then the current D10 mechanism is
only de Vries-compatible, not predictive.

## Milestone 2 -- Force the `j=0,1/2,1` assignment

Priority: deferred unless a dependency appears.  This milestone should not
block the kernel, current-metric, vacuum, consistency, or phenomenology
milestones except where one of those milestones needs a specific representation
assignment to proceed.

Execution decision: Borel-Weil supplies the representations and Casimirs, but it
does not exclude higher `j`.  The assignment passes only on a finite `SU(2)_2`
endpoint/current branch.  A Peter-Weyl rotor tower keeps higher states, including
the conditional `j=3/2` diphoton check, and therefore fails finite-set
predictivity.

Current input:

```tex
V_j=H^0(CP1,O(2j)),qquad j in {0,1/2,1}.
```

Current interpretation:

- `j=0`: photon slot.
- `j=1/2`: W slot.
- `j=1`: Z slot.

Needed derivation:

- Show why the endpoint/current sector is level two, or otherwise finite with
  only these three retained representations.
- Show why the charged weak boundary mode uses the fundamental endpoint
  `j=1/2`.
- Show why the neutral massive mode uses the adjoint or lowest neutral bilinear
  `j=1`.
- Show why the photon is the `j=0` neutral boundary state, not merely assigned
  that label.

Pass condition:

The same boundary rule gives all three assignments and excludes higher `j`.

Fail condition:

If `j=1/2` and `j=1` remain labels chosen after the fact, the numerical match is
not a prediction.

## Milestone 3 -- Compute the current metric in the full D10 carrier

Execution decision: the current metric gives `kappa_cur=1` only on the
full-current branch where the D8 boundary image channel sees the
Bailin-Love/Weinberg weak current including the vertical RR/current piece.  A
horizontal-only boundary channel gives `kappa_cur=1/(1+beta)=0.7527390090748721`
and predicts `sin^2 theta_W=0.24226537471822063`, so that branch fails.  The
current D8/Payen/RR source package does not derive the full-current placement;
`kappa_cur=1` is therefore a branch condition in the written action.

Current result:

```tex
G_ab^(2)=L_2^2 delta_ab,
qquad
e_a=K_a/L_2,
qquad
A_j^dagger A_j=j(j+1).
```

Needed derivation:

- Compute the current metric using the actual D10 internal geometry and RR
  current contribution.
- Include the Bailin-Love horizontal/vertical split.
- Add a source-backed RR/current boundary kinetic term, or parent-current lift,
  that makes the boundary Schur/Payen map use the full `L_2=L_{2,BL}` rather
  than only the horizontal `CP1` length.
- Show that no hidden boundary normalization reintroduces `kappa_cur`.

Pass condition:

The computed metric and the boundary image metric are the same object, so
`kappa_cur=1` is not adjustable.

Fail condition:

If the boundary map uses a different metric than the KK weak gauge metric,
`kappa_cur` becomes an extra physical parameter and de Vries compatibility is
weaker.

## Milestone 4 -- Compute the bulk vacuum coefficients

Execution decision: the current workspace gives the IIA scaling form and the
stationarity equations, but it does not compute the integrated coefficients
`B_R,B_H,B_0,B_2,B_4,B_6,B_loc` or the boundary scale function
`mu_B(rho,tau)`.  At `rho_*=9.463469757158872`, the equations are coefficient
balances with more unknowns than constraints, so Milestone 4 has not passed as
a prediction.  The rank test sharpens this: with
`B_H=B_0=B_2=B_6=0`, one can make any chosen `rho` stationary by taking
`B_4=B_R tau^2` and `B_loc=-(2/3)B_R tau rho^-2`.  At the target this is
`B_loc=-0.007444027070759169 B_R tau`.  Since Milestone 6 rejects the current
D8/O8 source package, the localized coefficient also lacks a valid global
source completion in this route.

Current potential:

```tex
V_bulk
=-B_R tau^-2 rho^-2
 +B_H tau^-2 rho^-6
 +B_0 tau^-4 rho^6
 +B_2 tau^-4 rho^2
 +B_4 tau^-4 rho^-2
 +B_6 tau^-4 rho^-6
 +B_loc tau^-3.
```

Current stationarity:

```tex
partial_rho V_bulk=0,
qquad
partial_tau V_bulk=0.
```

Needed derivation:

- Compute `B_R,B_H,B_0,B_2,B_4,B_6,B_loc` from the compactification data.
- Include localized D8/O8 source contributions and sign conventions.
- Determine the boundary scale function `mu_B(rho,tau)`.
- Solve the `rho,tau` equations.
- Check whether the solution selects the target `rho_*` and the absolute
  electroweak scale.

Pass condition:

The same stationary point gives the de Vries-compatible weak angle and the
absolute scales without inserting them as inputs.

Fail condition:

If the coefficients are free enough to fit the target, the vacuum potential is
a compatibility framework, not a prediction.

## Milestone 5 -- Derive or reject the selector potential

Execution decision: `kappa_cur` should be removed from the minimal selector on
the full-current branch after Milestone 3.  The `v_Q` and `lambda_H` terms are
compatible with the boundary scalar package.  The selector rank test shows that
once the squared selector terms vanish, their `rho,tau` derivatives vanish, so
the selector does not select the bulk moduli.  The neutral scalar Hessian rank
test also fails to force the negative-branch scalar values: a one-field radial
potential has two free coefficients for the two targets
`h_0^2=2J_v mu_B^2` and `M_h^2=J_H mu_B^2`, while neutral mixing only turns the
mass target into a spectral constraint on a larger Hessian.

Current selector:

```tex
V_sel
=C_cur(rho,tau)(kappa_cur-1)^2
 +C_v(rho,tau)(v_Q^2-mu_B(rho,tau)^2(1+sqrt3))^2
 +C_H(rho,tau)(lambda_H-lambda_dV)^2.
```

Needed derivation:

- Derive the `kappa_cur` pinning term from the current metric or remove
  `kappa_cur` as a variable.
- Derive the `v_Q` condition from the boundary scalar dynamics.
- Derive the `lambda_H` condition from the radial Hessian.
- Decide whether the negative branch is a true scalar Hessian branch or only a
  numerical placement.

Pass condition:

The selector is the local effective potential induced by the D10 boundary
action.

Fail condition:

If `v_Q` and `lambda_H` remain free scalar coefficients, the Higgs/vacuum part
remains a compatible enhancement rather than a derivation.

## Milestone 6 -- Consistency checks

Execution decision: local checks pass for spin-c placement, photon protection,
D8 parity/convention, and positivity of the assumed Feshbach channel.  The full
compactification check has not passed.  The first source table cancels total
eight-charge in a two-endpoint type I' distribution, but the minimal spin-c lift
leaves lower charge `208h_Q+673h_Q^2` with no supplied cancellation.
Independent endpoint lifts do not solve this inside the current type I' data:
unequal stacks fail D6, while balanced opposite lifts leave at least `h_Q^2`
D4 charge.  Closed `H`-flux also fails as a cancellation route on the selected
product and flag spaces because `H^3=H^5=0`.  A bare K-theory identification
also fails because the lower vector has nonzero rational Chern character on
torsion-free even-cohomology spaces.
The localized/image lower-charge test shows that the best balanced endpoint
package needs a new pure negative D4 image/source `-h_Q^2`; the same-lift
package would need `-208h_Q-673h_Q^2`.  No such source is included in the
current D8/O8 package.  The O4 realization test found that `O4^-` has the
right charge magnitude in the doubled convention, but standard product
involutions do not give a clean O4-only fixed locus: holomorphic projective
involutions on `CP2` give an O4 support together with an O6 support after the
`CP1` fixed circle is included, while standard complex conjugation gives
O6-type support.  The O4/O6 source-table test then rejects the holomorphic
package inside the current endpoint lattice: the companion O6 source is
`-4h_Q`, while D8 endpoint D6 charges lie in `16Z h_Q`; multiple copies fail
the combined D6/D4 congruences.  The source-balance no-go consolidates this:
within the scoped D8/O8 package, endpoint data, closed `H`, bare K-theory, and
the tested product O4/O6 package cannot make the lower Bianchi classes vanish.
The extra-mode mass-gap table also fails the current action: an unprojected
image field has a massless complement, the mixed Hom route removes that
complement only on the branch whose one-square action is not derived, and the
rotor branch keeps a light tower beginning at `96.54 GeV`.  Backreaction is not
solved.  The replacement-source equations show that a balanced opposite-lift
endpoint package reduces the missing charge to `-h_Q^2`, while unequal stacks
require `-16M h_Q-(4M^2-3)h_Q^2`.  Any D6-bearing repair must land in the
endpoint lattice `16Z h_Q`.  The tested O4/O6 package has
`-4k h_Q-kh_Q^2`; the D6 condition forces `k` to be a multiple of four, while
the balanced endpoint D4 coefficient is `1 mod 8`.  The source-branch decision
therefore closes the current D8/O8 compactification route as a global proof
branch: adding an anti-D4, O4-only image, or generic D6-bearing repair changes
the source content or topology and forces a new source table, vacuum, mode
spectrum, and backreaction calculation.

These checks are mandatory before any proof claim:

- Tadpole and flux balance.
- Freed-Witten/spin-c consistency on `CP2`.
- Romans source sign and D8/O8 charge convention.
- Gauge invariance of the boundary action.
- Positivity and unitarity of the reduced propagator.
- Photon masslessness from `Q eta_0=0`.
- Absence of extra light modes from the auxiliary complement.
- Backreaction compatibility with the assumed product/coset geometry.
- Cancellation or absorption of the lower source vector
  `208h_Q+673h_Q^2`.
- If the balanced endpoint lift is used, realization or rejection of the
  negative D4 image/source `-h_Q^2`.
- If the O4 route is used, the accompanying O6 component and all new localized
  source terms must be included.
- The holomorphic O4/O6 package does not close against the current endpoint
  charge lattice.
- Under these assumptions, the current D8/O8 route fails global source balance.
- A replacement source must supply the lower charge vector dictated by
  `milestone6-replacement-source-requirements-2026-05-25.md`; the minimal
  target is `-h_Q^2`.
- The current D8/O8 source branch is closed for proof claims by
  `milestone6-source-branch-decision-2026-05-25.md`.
- The unprojected finite image field and the rotor tower fail the extra-mode
  gap test for the finite W/Z branch.

Pass condition:

The same parameter point satisfies all consistency checks.  For the current
D8/O8 source package this pass condition is not met.

Fail condition:

Any required consistency condition forces a different kernel, metric, or vacuum.

## Milestone 7 -- Quantum and phenomenological matching

Execution decision: with current inputs, the tree-level on-shell de Vries
number gives `sin^2 theta=0.2231013223008662`.  PDG live 2026 masses give
`sin^2 theta_OS=0.2233390021445395`, a `1.56 sigma` pull; the CMS 2026 W mass
gives a `1.45 sigma` pull.  This is still close, but no threshold/running
calculation exists.  The raw scalar number is `122.39 GeV`, not the observed
Higgs mass.  A tower branch gives `M_{3/2}=96.54 GeV`, near the CMS Run 2
`95.4 GeV` diphoton feature, but production and branching are not computed.

Needed work:

- Distinguish on-shell and pole definitions for `M_W,M_Z`.
- Track the conditional `j=3/2` positive-branch scalar check:
  `M_{3/2}=96.54 GeV` when the common scale is fixed by `M_Z`.  This belongs
  only to a tower/moduli branch that keeps `j=3/2`; the finite level-two branch
  has no such state.  Compare with the CMS full-Run-2 low-mass diphoton feature
  at `95.4 GeV` only after the branch is derived.
- Track threshold corrections from the D10 boundary scale to the measured scale.
- Run `lambda_H` to the electroweak scale.
- Check whether the predicted Higgs-scale radial mode remains near the observed
  Higgs mass after standard corrections.
- Check whether the weak angle agreement survives within current experimental
  uncertainties after scheme conversion.

Pass condition:

The derived relation lands in the measured scheme without an uncontrolled
threshold correction.

Fail condition:

If scheme conversion or thresholds dominate the de Vries number, the apparent
match is not stable.

## Near-term sequence

1. Work Milestone 1 first: derive or reject the Feshbach kernel from the local
   boundary action.
2. Work Milestone 3 next: compute the full current metric.
3. Work Milestones 4 and 5 together: bulk vacuum coefficients and selector
   potential.
4. Run Milestone 6 before writing any proof claim.
5. Run Milestone 7 before making contact with measured masses.
6. Return to Milestone 2 after the other milestones, unless Milestone 1 or
   Milestone 3 exposes a direct dependency on the `j=0,1/2,1` assignment.

## Paper strategy

The current unified TeX article should be read as the construction and
compatibility article.  It should not claim that de Vries has been forced.

Future papers should split by completed milestone:

- Paper A: D10 boundary construction and canonical current metric.
- Paper B: local derivation of the Feshbach kernel, if Milestone 1 passes.
- Paper C: vacuum coefficient calculation and selector potential, if Milestones 4
  and 5 pass.
- Paper D: phenomenology and scheme matching, if the preceding milestones pass.

If a milestone fails, the deliverable becomes a no-prediction theorem for that route:
the D10 construction remains coherent, but de Vries is not forced by it.
The scoped current-route deliverable has reached that status.
