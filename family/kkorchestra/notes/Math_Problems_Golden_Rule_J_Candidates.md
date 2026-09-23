# Open Math Problems and Golden-Rule `J` Candidates

Date: 2026-06-01.

Scope: local review of `out/`, `docs/`, `CLAIMS.md`, `wastebook.md`, and the consolidated
verification notes.  The aim is to separate grounded mathematics from the unresolved operator
and action problems around the relation

```text
J = C_2(j),
P^*P|_j = x0 C_2(j) + sigma_j,
x^2/(c x + 1) = x0 C_2(j) + sigma_j.
```

Here `C_2(j)` means the quadratic `SU(2)` Casimir eigenvalue on a specified
irreducible sector `V_j`.  A bare equality `D^*D=j(j+1)` is not used as a project input.
The operator must be named, for example a vertical Casimir gradient, a boundary square-root
operator, or a finite interface operator whose squared modulus has been computed.

## Stable Ground

The following points can be treated as inputs for the next stage.

1. `CP^2/conj -> S^4` gives a two-fold branched cover with branch locus `RP^2`, equivariant
   only under the real `SO(3)` subgroup.
2. `X_{1,1}=SU(3)/U(1)_{1,1}` is a seven-dimensional Aloff-Wallach carrier with fibre
   `SO(3)=RP^3` over `CP^2`, and the Wilking presentation
   `(SU(3) x SO(3))/U(2)_Delta`.
3. `CP^2` needs a spin^c line, while `X_{1,1}` itself is spin.  Odd line bundles `O(n)` on
   `CP^2` carry the half-integer sectors.
4. The CP2 index formula

   ```text
   ind D_n = (n^2 - 1)/8
   ```

   gives the solid `n=5 -> 3` diagnostic, with `n=5` still requiring selection by the
   bosonic model.
5. The custodial control calculation is firm in the single `m_3` doublet branch:

   ```text
   kappa_c = kappa_n,
   rho = 1.
   ```

6. The De Vries signed block algebra is internally consistent.  The allowed input for its
   spectral parameter is a computed equation `P^*P|_j=x0 C_2(j)+sigma_j`, not a bare
   Dirac-square identification.  The action coefficient `c=1` still has to come from the same
   reduced quadratic form.

## Math Problems To Address

### 1. Self-Adjoint Branch Domain

The D6 branch cover uses

```text
CP^2 -> S^4,
B_4 = pi^{-1}(RP^2) subset Y_6,
G_B psi_+ = psi_-.
```

The missing object is the self-adjoint domain on `Y_6 \ B_4`.  A complete calculation must give:

```text
G_B D_+ = D_- G_B,
G_B^* G_B = 1,
Green boundary form = 0,
Def_B(n,r;G_B) from the tangential branch-link operator.
```

Repair route: formulate the branch as an APS/interface problem with a Calderon projector.

Stop condition: no self-adjoint sheet-exchange domain exists, or the resulting defect invariant
has no stable dependence on the bosonic variables.

### 2. Boundary Calderon and DtN Spectrum

The boundary programme has the right order-one operator:

```text
P_boundary = |A_Sigma|_ren,
P_boundary^*P_boundary|_j = x0 C_2(j) + sigma_j.
```

The hard problem is the exact spectrum beyond the principal symbol.  Curvature, finite collar
length, holonomy, torsion, flat characters, and endpoint conditions all feed `sigma_j`.

Deliverables:

```text
Sigma = M_5(5), N_B, or D7 cylinder boundary,
A_Sigma^2|_j = x0 C_2(j) + alpha + sigma_j,
same subtraction alpha for j=1/2 and j=1,
controlled residual sigma_j.
```

Stop condition: `sigma_j` differs by sector at the same size as `x0 C_2(j)`.

### 3. Derivation of the Signed Hessian Coefficient

The spectral block

```text
H_c(P) =
  [ 0        P^* ]
  [ P   -c P P^* ]
```

has the desired De Vries value only when `c=1`.  Spectral theory alone gives `P`; the quadratic
action gives `c`.

Deliverables:

```text
one reduced action,
one normalization for the linear gluing term,
one normalization for the quadratic stiffness term,
c independent of j.
```

Stop condition: the reduced Hessian gives sector-dependent `c`, or independent coefficients
with no symmetry or variational reason to identify them.

### 4. Bosonic Stabilization Coefficients

The current potential framework isolates the necessary signs but not the coefficients:

```text
V_total =
  V_grav + V_YM + V_defect + V_boundary + V_Calderon
  + V_KK-sf + V_flux + V_higher.
```

The project needs the radion, D7 squash, and D6 adiabatic-shape Hessians from one proposed
vacuum.  The D7 curvature calculation gives the shape signs:

```text
F_7''(2/5) > 0,
F_7''(2) < 0,
V_shape = -C_R exp(-lambda phi) F_7(a).
```

Thus pure curvature stabilizes the `a=2` direction and destabilizes the `a=2/5` direction after
the sign in `V_shape` is included.  Any squashed-vacuum use needs extra positive Hessian terms.

Deliverables:

```text
partial_phi V = 0,      partial_phi^2 V > 0,
partial_a V = 0,        partial_a^2 V > 0,
partial_epsilon V = 0,  partial_epsilon^2 V > 0.
```

### 5. D5 Boundary Character and APS/Calderon Compatibility

The rank-two `n=5` flat characters with determinant `exp(-2 pi i/5)` are known:

```text
(a,b) = (0,4), (1,3), (2,2).
```

The balanced lift `(1,3)` gives the D5-symmetric diagnostic.  The remaining problem is spectral:
the same convention must enter the APS eta invariant, Calderon projector, and boundary
square-root spectrum.

Deliverables:

```text
xi_5^Th(5,r;chi_{1,3}),
C_5(5,r;chi_{1,3}),
Fredholm pair (C_5, P_APS),
P_boundary^*P_boundary in the same Thom convention.
```

### 6. D7 Spectral Flow and Restoration Bound

The D7 endpoint needs a controlled path rather than a smooth odd-dimensional chirality claim.
The current bound has the form

```text
d_*^2 > B d_* R_7 + A R_7^2.
```

Deliverables:

```text
B_{7,k,s,mu}^2
  = R_s^{-2} d_k(s)^2 + H_mu^2
    + E^0_{s,mu}
    + R_s^{-1} d_k(s) E^1_{s,mu},
A = sup ||E^0||,
B = sup ||E^1||.
```

Stop condition: the selected path violates the no-crossing bound, forcing nonzero
`Delta_KK`.

### 7. Selection of `n=5`

The index value at `n=5` is reliable, but the choice of `n=5` still needs a dynamical or
topological selector.

Candidate selectors:

```text
defect monodromy,
D5 flat determinant condition,
finite module size,
D7 spectral-flow quantization,
minimum of V_total,
compatibility with P^*P = x0 C_2 + sigma_j.
```

Stop condition: `n=5` remains an external choice disconnected from branch, boundary, or
bosonic equations.

### 8. Custodial Branch Selection

The single `m_3` doublet branch protects `rho=1`.  The vertical `m_0` triplet branch spoils the
electroweak pattern.  The potential must therefore select

```text
m_{3,eff}^2 < 0,
lambda_3 > 0,
m_{0,eff}^2 + lambda_03 v^2/2 > 0.
```

Endpoint and stabilization terms must preserve the isotropic real metric on `m_3 ~= R^4` or
produce a computed deviation from `rho=1`.

### 9. Homogeneous Dirac and Kostant Shift Accounting

Natural smooth Dirac squares give

```text
D^2 = connection Laplacian + scalar curvature/4 + bundle curvature,
D_K^2 = C_G - C_H + ||rho_G||^2 - ||rho_H||^2.
```

The project needs an audited table of shifts in the `j=1/2` and `j=1` sectors.  A
renormalized Dirac route survives only if the shifts cancel, subtract universally, or become
small controlled `sigma_j`.

### 10. Finite/Fuzzy and Noncommutative Replacements

Finite modules can enforce `P^*P=C_2` at matrix level and make the signed Hessian literal.
The open mathematical problem is compatibility with the continuum data:

```text
spin^c parity,
n=5,
D5 eta,
D6 branch defect,
custodial m_3 branch,
gravity/radion sector.
```

Finite or fuzzy constructions become useful only if they impose constraints on bosonic
coefficients, branch signs, or boundary spectra.

## Golden-Rule `J` Candidates

### Candidate A: Vertical Casimir Gradient

Object:

```text
P_6^vert psi = sqrt(x0) sum_i (J_i psi) tensor e_i,
(P_6^vert)^* P_6^vert = x0 sum_i J_i^2 = x0 C_2(j).
```

Origin: `J_i` are the self-adjoint generators of the irreducible `SU(2)` module
`V_j=Sym^(2j)(C^2)`.  The identity `sum_i J_i^2=C_2(j) Id` supplies the quantisation.

Strength: gives a clean `J=C_2(j)` on `V_j` with no analytic shift.

Risk: may be a hand-built representation operator unless the reduced action produces it.

Next calculation: derive it from the vertical kinetic term, branch gluing term, or CSDR
quadratic action and compute the associated `c`.

### Candidate B: Boundary Calderon/DtN Operator

Object:

```text
D = c(nu)(partial_u + A_Sigma + R_u),
P_boundary = |A_Sigma|_ren.
```

Strength: boundary square-root operators naturally have principal symbol
`sqrt(Delta_boundary)` and belong to the D5, branch-link, and D7 settings.

Risk: exact eigenvalues may carry sector-dependent `sigma_j`.

Next calculation: product-collar model for `M_5(5)` and `N_B`, followed by curvature and
flat-character corrections.

### Candidate C: Polar Patching Operator

Object:

```text
P = U |P|,
|P| = (P^*P)^(1/2).
```

Strength: places the square root in the modulus of an interface or sheet-exchange map, matching
the branch-cover geometry.

Risk: a purely unitary `G_B` has trivial modulus, so the useful `P` must include transmission,
boundary stiffness, or a Schur complement.

Next calculation: build the folded branch quadratic form and identify the positive operator
whose polar modulus enters the Hessian.

### Candidate D: Branch-Link Tangential Operator

Object:

```text
A_{N_B,n,r,G}^2|_j = x0 C_2(j) + alpha_B + sigma_{B,j},
CP^1 -> N_B -> L^3(4,1).
```

Strength: directly uses the `CP^2 -> S^4` branched cover, so a success would connect the
golden-rule equation to the D6 object rather than to an auxiliary finite matrix.

Risk: the link spectrum mixes the `CP^1` vertical Casimir with the lens-space base spectrum and
the sheet-exchange phase.

Next calculation: separate the `CP^1` angular spectrum from the `L^3(4,1)` flat/eta data in the
adiabatic limit.

### Candidate E: D7 Cylinder DtN/Spectral-Flow Operator

Object:

```text
Lambda_T|_j =
sqrt(x0 C_2(j)) coth(T sqrt(x0 C_2(j))).
```

Strength: gives a concrete finite-length deformation of the square-root law and ties `sigma_j`
to restoration length or endpoint radius.

Risk: finite-cylinder corrections are sector-dependent unless a limit or cancellation suppresses
them.

Next calculation: identify whether the D7 restoration path requires the infinite-cylinder
limit, or whether the finite `coth` correction becomes the desired rational deformation.

### Candidate F: Finite `SU(2)` or Fuzzy Interface Hessian

Object:

```text
H_interface = H_{j=1/2} direct_sum H_{j=1},
D_F^*D_F = C_2.
```

Strength: turns the De Vries block into a finite matrix problem with exact `J` eigenvalues.

Risk: can reproduce the arithmetic while bypassing gravity and boundary constraints.

Next calculation: derive the finite trace action and match its coefficients to the continuum
D5/D6/D7 data.

### Candidate G: Renormalized Kostant Cubic Dirac

Object:

```text
D_ren^2 =
D_K^2 - (||rho_G||^2 - ||rho_H||^2) - curvature_endomorphism.
```

Strength: stays close to standard homogeneous spin geometry.

Risk: the subtraction may be an imposed normal ordering with no physical variational origin.

Next calculation: compute the sector shifts explicitly for the `j=1/2` and `j=1` sectors and
test universality.

### Candidate H: Boundary Schur Complement

Object:

```text
K =
[ A  P^* ]
[ P  B   ],
K_eff = A - P^* B^{-1} P.
```

Strength: rational eigenvalue relations often arise by eliminating an auxiliary field.  This
could explain why the observed rule is rational in `x` while the underlying object is a square
root of `J`.

Risk: many Schur complements can be engineered; the auxiliary field must have a clear geometric
identity.

Next calculation: integrate out one boundary/interface scalar in the D5 or branch quadratic
action and compare the resulting characteristic equation with `x^2/(c x+1)=x0 J+sigma_j`.

## Recommended Order

1. Work out Candidate B and Candidate H together: boundary square-root plus boundary quadratic
   action gives the shortest route to both `P^*P` and `c`.
2. Use Candidate D as the D6-specific version of the same calculation, because it uses the
   branched `CP^2 -> S^4` data.
3. Keep Candidate A as the finite clean model and normalization reference.
4. Use Candidate G only after the shift table is explicit.
5. Use Candidate F when it imposes a coefficient or selection rule on the bosonic problem.

## Minimal Success Standard

A successful golden-rule derivation should provide, in one convention,

```text
P^*P|_{j=1/2} = x0 (3/4) + sigma_{1/2},
P^*P|_{j=1}   = x0 (2)   + sigma_1,
c_{1/2} = c_1,
|sigma_1 - sigma_{1/2}| controlled or explained,
n=5 and chi_{1,3} compatible with the same boundary/interface data,
rho=1 preserved in the selected `m_3` branch.
```

The strongest near-term target is therefore not the numerical value alone.  The decisive target
is a single boundary/interface action whose square-root operator, signed Hessian coefficient,
flat-character choice, and custodial branch selection all use the same normalization.

The action-level algebra is recorded in
`notes/Boundary_Hessian_Schur_Complement_Derivation.md`: an unreduced block with mixed coefficient
`alpha` and quadratic coefficient `beta` gives `c=beta/alpha^2`, with `c=1` equivalent to
`beta=alpha^2` after canonical normalization.
The product-collar scalar test in `notes/Product_Collar_DtN_Normalization_Test.md` adds an
important limitation: ordinary DtN directly gives `<q,Lambda q>`, so the signed Hessian needs an
extra boundary/interface variable.
