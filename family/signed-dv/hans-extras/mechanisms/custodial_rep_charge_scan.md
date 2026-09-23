# Custodial `SU(2)_R + X` charge scan

## Question

Composite-Higgs and custodial models often embed hypercharge as

```text
Y = T_R^3 + X.
```

Could the paired D-term charge `Y=3/8` arise naturally from a custodial
representation plus an ordinary `X` charge?

## Scan

The script `algebra/custodial_rep_charge_scan.py` scans `SU(2)_R` spins through
`j_R=4`.  The `T_R^3` weights are integer or half-integer.  Assuming an ordinary
`X` lattice with unit `1/6`, the required value is

```text
X = 3/8 - T_R^3.
```

For every scanned weight, `X/(1/6)` is a quarter-integer rather than an
integer.  No ordinary-lattice hit appears.

## Interpretation

This closes the most direct custodial-representation loophole for the paired
D-term boundary model.  A model can still introduce a nonstandard `X` charge
lattice, kinetic mixing, or a hidden sector, but that is additional UV
engineering.  The coefficient is then inherited from the exotic charge
assignment, not predicted by custodial symmetry.

## Verdict

No mainstream custodial `SU(2)_R + X` embedding with ordinary charge
quantization naturally supplies `Y=3/8`.
