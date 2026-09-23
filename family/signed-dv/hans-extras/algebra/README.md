# Algebra Checks

`verify_spectrum.py` verifies the exact signed-root identities and reproduces
the numerical masses quoted in the project statement.

`deformation_scan.py` records symbolic tests of simple deformations of

```text
P_s(x) = x^2 + C_s x - C_s.
```

The main algebraic result is that an on-shell-subtracted deformation

```text
P_s(x) -> P_s(x) + lambda_s (x - x_{s,+})
```

preserves the positive root exactly and shifts the negative root exactly.  This
is the clean mathematical realization of a negative-sector projector.  It is
not, by itself, a field-theory derivation of the coefficient.

`current_input_comparison.py` repeats the formula under the project-stated
`M_Z`, the PDG 2024 summary value, and the PDG Live 2026 value accessed during
this run.  This keeps the exact algebra separate from moving experimental
averages.

`explore_deformations_extended.py` and `verify_signed_roots_extended.py` are
imported from the sister project.  They are retained as a more verbose
deformation catalogue and as an independent numerical check of physical deltas.

`effective_operator_matching.py` matches the cleanest negative-sector EFT
operator to the proposed correction and shows that the required coefficient is
`c_Y = 3/16` in that normalization.

`negative_sector_fit.py` decomposes the physical Higgs and Fermi/vev shifts
into individual, trace, and traceless coefficients.

`two_state_projector_scan.py` checks whether the `sigma_3` negative-sector
operator is physical or merely a diagonal-basis convention, and compares the
full `C_F/C_A` factor with single-generator hypercharge traces.

`loop_threshold_estimates.py` estimates whether perturbative loops, heavy
thresholds, or Abelian D terms can naturally produce a tree-size `3/8` shift.

`gut_hypercharge_normalization.py` checks the familiar `SU(5)` origin of
`sin^2 theta_W=3/8` and shows that it is not the same group-theory quotient as
the proposed `SU(2)` Casimir ratio.

`paired_dterm_model.py` tests a concrete paired-scalar D-term Lagrangian that
can produce an exactly traceless split, showing that the target coefficient is
then an assigned exotic hypercharge.

`charge_lattice_check.py` checks whether the `Y=3/8` D-term charge lies on the
ordinary Standard Model or minimal-`SU(5)` charge lattice.

`run_all_checks.py` executes every algebra/check script and reports a compact
pass/fail summary.

`su5_weight_lattice_scan.py` enumerates simple `SU(5)` tensor hypercharge
weights and confirms that `Y=3/8` is absent from the ordinary `1/6` lattice.

`weak_angle_comparison.py` compares the exact positive-branch weak angle to
current on-shell W/Z inputs.

`custodial_rep_charge_scan.py` scans `Y=T_R^3+X` custodial embeddings and shows
that `Y=3/8` does not arise for ordinary `X` charge quantization.

`kinetic_mixing_charge_shift.py` checks how hidden-`U(1)` kinetic mixing could
engineer an effective `3/8` charge and why this adds a continuous parameter.
