# Final Recommendation

## Ranking

1. Custodial EFT / HEFT spurion: best mainstream language.  Result:
   symmetry-motivated.
2. Composite Higgs: good custodial structure and hypercharge spurions.  Result:
   symmetry-motivated but coefficient is strong-sector dependent.
3. Quiver / non-decoupling D terms: good engineering framework.  Result:
   phenomenological matching.
4. Supersymmetric D terms: real `g'^2 v^2` scalar corrections, but no root
   projector and no `3/8` prediction.  Result: phenomenological.
5. Gauge-theory Reggeization: explains why `C_F/C_A` is a legitimate field
   theory ratio, but not why it corrects electroweak masses.  Result: rejected
   for this purpose.
6. String / D-brane UV: can reproduce low-energy ingredients, but no universal
   correction.  Result: rejected as an explanation.

## Answer to the Final Question

The signed de Broglie-de Vries spectrum can be embedded in a mainstream
custodial EFT only as a phenomenological or symmetry-motivated ansatz:

```text
Delta M_-^2 = kappa (M_Z^2-M_W^2) sigma_3.
```

Custodial symmetry and hypercharge gauging justify the dependence on
`M_Z^2-M_W^2`, and `sigma_3` makes the negative-sector trace correction vanish.
However, mainstream custodial field theory does not derive

```text
kappa = C_F/C_A = 3/8.
```

The step that fails is the identification of the Wilson coefficient with the
ratio of full `SU(2)` Casimirs.  Hypercharge gauges only `T_R^3`; the vector
splitting is `g'^2 v^2/4`; and there is no standard two-state negative-root
sector on which a root-space `sigma_3` acts.  A UV completion could match onto
`kappa=3/8`, but none of the surveyed mainstream mechanisms predicts it without
additional model-dependent assumptions.

## Cleanest Statement

The strongest defensible claim is:

```text
The 3/8 correction is the unique simple trace-preserving leading
custodial-breaking ansatz if one assumes a two-state signed negative-root
sector and chooses the Wilson coefficient to be the SU(2) Casimir ratio.
```

That is not a derivation.  It is a compact phenomenological rule with good
spurion behavior.

## Current-Input Note

Using the PDG Live 2026 `M_Z = 91.1879 GeV` accessed on 2026-05-14 gives

```text
M_W0 = 80.374707 GeV
M_H  = 125.199384 GeV
M_F  = 174.175759 GeV.
```

These are still close to the Higgs and Fermi scales, but the comparison remains
a phenomenological on-shell relation.  It is not a global electroweak fit and
does not repair the missing derivation of `kappa=3/8`.

## Sister-Project Update

The imported sister project makes the rejection sharper:

- HEFT/SMEFT: the custodial spurion is `T_R^3`; single-generator traces give
  `1/4`, not `3/8`.
- MCHM: the gauge Coleman-Weinberg contribution has `3 g^2 + g'^2`, not a
  `C_F/C_A` coefficient.
- SUSY D terms: the natural hypercharge coefficient is `1/8`, and the Higgs
  D-term contribution does not vanish for `g' -> 0`.
- Reggeization: `C_F/C_A` is real and mainstream, but it is attached to
  high-energy trajectory functions, not to the scalar mass correction.

These points do not change the status; they reduce the chance that a simple
mainstream derivation was missed.

## Cycle 1 Update

The cleanest explicit EFT ansatz is now recorded in
`mechanisms/minimal_negative_sector_eft.md`:

```text
V_eff contains 1/2 Psi_-^T [
  m_-^2 1 + c_Y g'^2 (H^\dagger H) sigma_3
] Psi_-.
```

It matches the proposed correction for `c_Y = 3/16`.  This is gauge-invariant
and trace-preserving, but it confirms that the coefficient is a Wilson
coefficient unless a UV model derives `c_Y`.

## Cycle 2 Update

The physical negative-sector fit is now recorded in
`phenomenology/negative_sector_fit.md`.  The project-statement inputs give

```text
Delta_H/gap            = 0.3751387901
-Delta_F/gap           = 0.3884437590
kappa_traceless        = 0.3817912745
```

Current PDG Live inputs move the Higgs-side coefficient to `0.3656374888` while
leaving the Fermi-side coefficient near `0.38855`.  This supports the cautious
statement that the trace-preserving `3/8` rule is a good phenomenological ansatz
but not exact under current central values.

## Cycle 3 Update

The two-state projector test in `mechanisms/two_state_projector.md` strengthens
the negative conclusion.  A traceless two-state correction can always be rotated
into a `sigma_3` form, so the matrix structure is not by itself a derivation.
More importantly, a hypercharge spurion supplies the selected generator
`T_R^3`; at order `g'^2` this naturally gives `(T_R^3)^2 = 1/4` in a
fundamental, not the full `C_F = 3/4`.  The desired `3/8` therefore still
requires an additional matching assumption.

## Cycle 4 Update

The loop and threshold estimate in `mechanisms/loop_thresholds.md` shows that
the target shift is tree-size:

```text
epsilon = (3/32) g'^2 v^2.
```

An ordinary one-loop hypercharge self-energy would need a finite coefficient
`A=2 pi^2` even if the full `C_F` were available, or `A=6 pi^2` for the actual
single-generator factor.  D terms can be tree-size, but the target then
corresponds to assigning an effective scalar charge `q_S=3/8`; this is not a
derivation of the Casimir ratio.

## Cycle 5 Update

The `SU(5)` check in `mechanisms/gut_hypercharge.md` rules out another tempting
shortcut.  Minimal unification gives `sin^2 theta_W=3/8` from
`(3/5)/(1+3/5)`, whereas the proposed correction uses the `SU(2)` ratio
`(3/4)/2`.  The equality is numerical, not a common derivation.  GUT
normalization fixes a high-scale coupling boundary condition and does not
generate the negative-sector `sigma_3` threshold.

## Cycle 6 Update

The paired D-term construction in `mechanisms/paired_exotic_dterm.md` is the
closest explicit Lagrangian model:

```text
V_D = g'^2/2 (q_H |H|^2 + q_S |S_+|^2 - q_S |S_-|^2)^2.
```

It gives a trace-preserving split with `kappa=2 q_H q_S`; for `q_H=1/2`, the
target requires `q_S=3/8`.  This derives the operator form from a D term, but
not the coefficient.  The coefficient is an exotic hypercharge assignment, and
the resulting fields carry fractional electric charges unless additional hidden
structure is introduced.

## Cycle 7 Update

The charge-lattice check in `mechanisms/charge_quantization.md` confirms that
`Y=3/8` is not on the usual Standard Model/minimal-`SU(5)` `1/6` hypercharge
lattice because `(3/8)/(1/6)=9/4`.  Thus the paired D-term model is a useful
existence proof for the operator form, but not a natural embedding of the
coefficient.

## Scorecard Update

The mechanism scorecard is in `mechanisms/scorecard.md`.  It separates the
current result into three layers:

1. Exact signed-root algebra: valid.
2. Mainstream EFT/D-term operator form: valid if a two-state negative sector is
   introduced.
3. Prediction of `3/8`: not derived.  It enters as `c_Y=3/16`, `q_S=3/8`, or
   an equivalent matching choice.

## Cycle 9 Update

The `SU(5)` tensor scan in `mechanisms/su5_rep_scan.md` confirms that ordinary
tensor representations built from the minimal `SU(5)` hypercharge weights stay
on the `1/6` lattice and do not contain `Y=3/8`.  A GUT rescue would require a
changed charge lattice or additional exotic/product-group structure.

## Cycle 10 Update

The positive-branch weak-angle check in `phenomenology/weak_angle_comparison.md`
shows that the root value `sin^2(theta_W,+)=0.2231013223...` is close to, but
not identical with, current on-shell W/Z inputs.  This reinforces that the
signed-root spectrum is an on-shell phenomenological structure, not a precision
electroweak-fit derivation.

## Conditional No-Go

The concise no-go statement is in `mechanisms/conditional_no_go.md`.  Under
ordinary custodial EFT assumptions, hypercharge supplies the single generator
`T_R^3`, so the leading spurion supports
`kappa(M_Z^2-M_W^2)sigma_3` but does not select the full-Casimir ratio
`C_F/C_A=3/8`.  Deriving `3/8` requires an additional UV matching coefficient,
exotic charge assignment, or altered charge lattice.

## Cycle 13 Update

The custodial `Y=T_R^3+X` scan in
`mechanisms/custodial_rep_charge_scan.md` finds no ordinary-lattice way to
obtain `Y=3/8`: with `T_R^3` integer or half-integer and `X` quantized in
units of `1/6`, the required `X` is always off-lattice.  This strengthens the
conclusion that the paired D-term construction needs exotic charge engineering.

## Cycle 14 Update

Hidden-`U(1)` kinetic mixing, documented in `mechanisms/kinetic_mixing.md`, can
evade the ordinary charge lattice by producing
`q_eff=q_0+epsilon(g_X/g_Y)q_X`.  It can therefore engineer `q_eff=3/8`, but
only by choosing a continuous mixing parameter.  This is a mainstream escape
hatch for charge quantization, not a derivation of the Casimir coefficient.

## LEE Update

The sister project's look-elsewhere result is now assessed in
`phenomenology/lee_sister_assessment.md`.  I accept its implication at face
value: within the stated radical/denominator search family, the closed-form
Higgs-ratio match has `p_LEE = 1.564e-6`, so the pattern should not be dismissed
as casual numerology.  The sister script was rerun locally and reproduced that
number.

This upgrades the phenomenological status, not the derivation status.  The
current combined verdict is:

```text
LEE-significant phenomenological pattern;
operator form engineerable in EFT/D terms;
3/8 coefficient not derived from mainstream custodial field theory.
```

## Scheme Update

The sister scheme-dependence result is now summarized in
`phenomenology/scheme_sister_assessment.md`.  The `M_F` residual relative to
`v_bare/sqrt(2)` is about `25 GeV^2`, roughly `1.9%` of the natural one-loop
electroweak scale `Delta r * v^2/2 = 1100--1330 GeV^2`.  That makes the
residual plausible as a missing radiative correction, but no standard scheme
lands on the dV value.  This softens the phenomenology; it does not derive the
coefficient.
