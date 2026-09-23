# De Vries as a Special Custodial Situation

Date: 2026-06-01.

Status: focused analysis of whether the De Vries signed-Hessian condition should be read as a
new custodial situation.

## Short Answer

De Vries can be read as a special strengthened custodial situation under a specific condition:
the electroweak deformation first satisfies the ordinary custodial requirement

```text
one m_3 doublet deformation,
kappa_c = kappa_n,
rho = 1,
```

and then the same sewing or patching deformation has a signed Hessian

```text
H_c(P) =
  [ 0       P^* ]
  [ P   -c P P^* ],
P^*P|_j = x0 C_2(j)+sigma_j,
c=1.
```

In that reading, De Vries is a spectral custodial refinement: ordinary custodial symmetry ties
the charged and neutral weak stiffnesses, while De Vries also ties the linear sewing operator to
the quadratic stiffness operator with the same normalization.

The stronger name is justified only if one action supplies both facts:

```text
rho=1 from the single m_3 four-block,
c=1 from the same boundary/interface Hessian.
```

## Ordinary Custodial Layer

The validated custodial calculation in `archive/verification_20260531/R2.md` uses the horizontal block

```text
m_3 ~= C^2 ~= R^4.
```

For a single doublet vacuum,

```text
(M^2)_{ab}=kappa <T_a H,T_b H>_{m_3},
g_t|_{m_3}=x_2(-B)|_{m_3}.
```

Since `m_3` is one irreducible real `U(2)` block, every invariant quadratic form on that block
has one scalar coefficient.  The weak mass matrix therefore has

```text
kappa_c = kappa_n,
rho = m_W^2/(m_Z^2 cos^2 theta_W)=1.
```

This layer needs no De Vries arithmetic.  It needs a single `m_3` doublet and suppression of the
vertical `m_0` triplet.

## De Vries Layer

The De Vries block starts after the ordinary custodial layer.  It assigns the two representation
sectors

```text
j=1/2,      C_2=3/4,      spin^c doublet / m_3 sector,
j=1,        C_2=2,        integer adjoint / fibre-memory sector.
```

The signed Hessian on a singular-vector pair has characteristic equation

```text
lambda^2 + c K_j lambda - K_j = 0,
K_j=P^*P|_j.
```

For `c=1` and `K_j=j(j+1)`,

```text
a_j = (sqrt(K_j^2+4K_j)-K_j)/2,
b_j = (sqrt(K_j^2+4K_j)+K_j)/2.
```

The vector branch ratio is

```text
M_W^2/M_Z^2 = a_{1/2}/a_1.
```

This gives the De Vries value

```text
sin^2(theta_W)=0.2231013223...
```

The De Vries condition therefore adds a second equality on top of custodial `rho=1`:

```text
ordinary custodial:      kappa_c = kappa_n,
De Vries refinement:     beta = alpha^2, hence c=1.
```

Here `alpha` is the coefficient of the linear sewing term and `beta` is the coefficient of the
quadratic stiffness term in the unreduced boundary/interface Hessian.

## Constructive Reading

The strongest constructive reading is:

```text
De Vries = custodial sewing quantization.
```

The 3D Hopf lesson says that two apparent operations, charged `S^2` deformation and neutral
`S^1` phase/twist, must come from one doublet deformation to give `rho=1`.

The D5/D6/D7 version says that the `j=1/2` spin^c doublet and the `j=1` fibre-memory sector
must come from one sewing operator `P`.  The same operator must appear

```text
linearly:       alpha P,
quadratically:  beta P P^*.
```

Then ordinary custodial symmetry becomes the mass-matrix equality, while De Vries becomes the
factorized Hessian equality.  The two conditions form a ladder:

```text
single sewing deformation
  -> one real m_3 four-block
  -> kappa_c = kappa_n
  -> rho = 1
  -> H_{alpha,beta}(P) with beta=alpha^2
  -> De Vries roots.
```

This deserves the name "special custodial situation" when the same geometric object produces the
whole ladder.

## Objections

### 1. `rho=1` Does Not Imply De Vries

The `m_3` mass-matrix proof gives `kappa_c=kappa_n` for every Wilking ratio `t`.  It has no
information about the signed-Hessian coefficient `c`.  A model can pass the orthodox custodial
test and still have

```text
c != 1.
```

Therefore De Vries supplies extra spectral structure beyond ordinary custodial symmetry.

### 2. De Vries Arithmetic Does Not By Itself Protect `rho`

The signed block can be written on abstract `j=1/2` and `j=1` sectors.  That algebra alone does
not prove that the electroweak vacuum is a single `m_3` doublet or that the `m_0` triplet has zero
vacuum value.  A physical model still needs

```text
m_3,eff^2 < 0,
<Phi_0> = 0,
m_0,eff^2 + lambda_03 v^2/2 > 0.
```

### 3. The `j=1` Sector Has Two Possible Meanings

The `j=1` label can mean:

```text
vertical m_0 triplet datum,
fibre-memory endpoint datum,
adjoint reference sector in the patching Hessian.
```

The first option is dangerous for electroweak symmetry breaking because an `m_0` triplet vacuum
spoils the `Z` mass relation.  The safer De Vries interpretation uses `j=1` as a reference or
endpoint sector inside the sewing Hessian, with no `m_0` triplet vacuum.

### 4. Ordinary DtN Gives Only The First-Order Boundary Operator

The product-collar DtN model gives

```text
S_on-shell = (tau/2)<q,Lambda q>,
Lambda^2|_j = x0 C_2(j).
```

That supplies square-root Casimir data.  The signed De Vries block needs another
boundary/interface field and the action-level relation

```text
c=beta/alpha^2.
```

Thus DtN can feed a special custodial situation only after the interface Hessian has been
derived.

### 5. Sector Shifts Can Break The Special Relation

The comparison uses `j=1/2` and `j=1`.  Any uncontrolled shift

```text
sigma_{1/2},     sigma_1
```

changes the De Vries roots.  A valid special custodial situation needs sector-independent
normalization and controlled residual shifts.

## Tests

### Test A: Ordinary Custodial Criterion

Check the mass matrix at the proposed vacuum:

```text
H in m_3,
<Phi_0>=0,
kappa_c=kappa_n,
rho=1.
```

Failure here prevents any special-custodial reading of De Vries in the electroweak sector.

### Test B: Common Sewing Operator

Identify one operator `P` whose sectors include the doublet and reference labels:

```text
P^*P|_{1/2}=x0 (3/4)+sigma_{1/2},
P^*P|_1=x0 (2)+sigma_1.
```

The same `P` must enter both sectors.

### Test C: Hessian Normalization

Derive the boundary or patching Hessian:

```text
H_{alpha,beta}(P) =
  [ 0          alpha P^* ]
  [ alpha P   -beta P P^* ].
```

After canonical normalization,

```text
c=beta/alpha^2.
```

The special De Vries case requires

```text
beta=alpha^2.
```

### Test D: Branch Assignment

Use the positive branch for vector masses and the negative branch for scalar/vacuum data:

```text
a_j^2/(1-c a_j)=K_j,
b_j^2/(1+c b_j)=K_j.
```

Mixing these branch formulas changes the interpretation.

## Repair Paths

1. Boundary/interface repair.

   Use the Calderon/DtN operator as `P`, then derive an interface action with a second boundary
   variable.  Among the available routes, this gives the most direct `alpha,beta` calculation.

2. Finite-module repair.

   Build a finite `SU(2)` module where `P^*P=C_2`, then match the finite trace action
   to the D5/D6/D7 boundary data.  This route can explain the `j(j+1)` quantization, but it must
   still preserve `rho=1` on the `m_3` branch.

3. Branch-cover repair.

   Treat the `CP^2 -> S^4` branch data as the source of the sewing operator.  The `j=1/2`
   sector then lives in the spin^c lift, while the `j=1` sector records fibre/link data without
   forcing a triplet vacuum.

4. Potential-selection repair.

   Use defect, boundary, flux, or CSDR terms to make the `m_3` branch light and the `m_0`
   branch heavy:

   ```text
   m_3,eff^2<0,
   m_0,eff^2 + lambda_03 v^2/2>0.
   ```

## Failure Criteria

The special-custodial reading fails if any of the following occurs:

```text
kappa_c != kappa_n at the selected vacuum,
an unavoidable m_0 triplet vacuum appears,
the j=1 sector must be a physical triplet condensate,
P^*P has large uncontrolled sigma_j shifts,
c differs between j=1/2 and j=1,
c is adjusted by a free counterterm rather than derived,
the positive and negative root branches are interchanged.
```

## Working Conclusion

De Vries should be treated as a candidate spectral custodial refinement layered above the
orthodox `rho=1` test.

The ordinary custodial layer says:

```text
one m_3 doublet deformation controls charged and neutral weak masses.
```

The De Vries layer says:

```text
one sewing operator controls linear patching and quadratic stiffness.
```

When both statements come from the same D5/D6/D7 boundary or branch action, De Vries amounts to
a special new custodial situation: a factorized sewing version of custodial symmetry that fixes a
scale-free W/Z ratio in addition to protecting `rho=1`.

Until that common action is derived, the safe classification is:

```text
ordinary custodial symmetry: established conditionally on the m_3 branch,
De Vries special custodial refinement: algebra verified, geometric origin open.
```
