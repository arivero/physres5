# SU(5) representation scan

## Question

Could a larger but ordinary `SU(5)` tensor representation contain a state with
hypercharge `Y=3/8`, rescuing the paired D-term construction?

## Weight-lattice result

The minimal `SU(5)` fundamental hypercharge weights are

```text
-1/3, -1/3, -1/3, +1/2, +1/2.
```

Each is an integer multiple of `1/6`.  Any ordinary tensor product of
fundamentals and antifundamentals has hypercharge equal to a sum of such
weights, and therefore remains on the `1/6` lattice.

The scan in `algebra/su5_weight_lattice_scan.py` enumerates tensor sums through
rank 8 and confirms that no `+/-3/8` weight appears.

## Interpretation

This is not a deep theorem about every possible UV construction.  It is a
practical check of the obvious escape hatch: ordinary `SU(5)` representation
theory does not naturally contain the `Y=3/8` charge needed by the paired
D-term boundary model.

To get `3/8`, one must change the charge lattice, use a product-group or
kinetic-mixing construction, or introduce a hidden/exotic sector.  Those options
are model-dependent and no longer explain the coefficient by the original
`SU(2)` Casimir ratio.
