# The reciprocal invariant and the sign-reduction of Q(J)

Worked from the matrix's defining property. Verified in `devries_spectrum.py`.

## The defining property is trace = det

`Q(J)=μ²[[0,√J],[√J,−J]]` has `tr = −J` and `det = −J`. For a 2×2, `tr = det`
means (sum of eigenvalues) = (product), so the reciprocals partition unity:
```
1/x₊ + 1/x₋ = 1        for every J     (verified: =1.000000000 at J=3/4,2,15/4,1)
```
In masses, `M²_± = μ² x_±`:
```
1/M₊² + 1/M₋² = 1/μ²        ⟺        tr Q(J)⁻¹ = 1/μ².
```
The trace of the inverse operator (the zero-momentum Green's function) is fixed at
`1/μ²`, independent of the level J.

## Physical reading: parallel combination

```
1/M₊² = 1/μ² + 1/|M₋²|      (since M₋² < 0)
```
Each gauge boson `M₊` and its order-parameter partner `|M₋|` combine in parallel
to the single scale μ². Verified for the Z slot:
```
M_Z² = parallel(μ², |M₋(2)|²) = 8315.25 GeV²     (μ=106.58, M₋(2)=176.16)
```
μ is the harmonic scale tying each vector to its negative-branch partner.

## The −J collapses to a single sign

Write the matrix as off-diagonal `b`, diagonals `(0, d)`. `tr = det` forces
```
b² = −d.
```
In the geometric (Hodge) reading the off-diagonal is the exterior derivative,
`‖dφ‖² = J ‖φ‖²` so `b = √J`, and the lower diagonal is minus the internal
Laplacian eigenvalue, `d = −J`. Then `b² = J = −d` is automatic. So `√J` and `J`
are the same internal datum (the Laplacian eigenvalue and its square root); the
one physical input that is not fixed by geometry is the **sign of d** — that the
order-parameter tower carries `m² = −λ` rather than `+λ`.

So "derive `Q(J)` / find the 6-manifold" reduces to "explain one sign: why is the
order parameter a negative-mode." That is the Breitenlohner–Freedman / AdS
question, where `m² < 0` is admissible above the BF bound.

## Still open (not closed by this)
- the assignment W↔3/4, Z↔2;
- the explanation of the sign (the negative-mode itself);
- the ~1 GeV scale of α.

The invariant and the sign-reduction narrow the operator problem to one sign;
they do not solve the assignment or the scale.
