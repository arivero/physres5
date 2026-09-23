# Relative Gain Source Action Admission Test

Date: 2026-06-01.

Status: exact algebra plus admission test for the surviving signed-source route in the
no-priori De Vries programme.

## Purpose

The active route needs a source action whose second variation gives a retained response block
with:

```text
mixed term:          <q,P^*p>,
response stiffness: <p,P P^* p>,
coefficient ratio:  c=beta/alpha^2,
```

while `P` and its multiplier are computed elsewhere from the named branch, boundary, group, or
finite operator.  The algebraic source shape has now been isolated:

```text
relative gain = mismatch before response - mismatch after response.
```

This note records the exact calculation and the conditions under which it can count as a source
action rather than an imposed subtraction.

## Exact Algebra

Let

```text
q in E,
p in F,
h=P^*p in E,
```

with one Hilbert or finite trace norm on `E`.  Define the positive mismatch energy:

```text
E_mis(q,p) = (tau/2) ||q-P^*p||_E^2.
```

The relative gain is:

```text
G(q,p) = E_mis(q,0) - E_mis(q,p).
```

Expansion gives:

```text
G(q,p)
  = tau Re <q,P^*p>_E
    - (tau/2) <p,P P^*p>_F.
```

Thus the Hessian in the retained variables has:

```text
overall factor tau,
mixed entry P^*,
response stiffness P P^*.
```

After the overall factor `tau` is separated as the physical scale, the normal-form convention is:

```text
alpha_norm=1,
beta_norm=1,
c=1.
```

The coefficient comes from the same squared norm in the first and second variations of
`E_mis`.  No representation multiplier has entered this calculation.

## Weighted Norm Version

If the source mismatch norm is weighted by a positive operator `W_E` on `E`,

```text
E_mis(q,p) = (tau/2) ||W_E^(1/2)(q-P^*p)||^2,
```

then the same calculation gives:

```text
G(q,p)
  = tau Re <q,W_E P^*p>
    - (tau/2) <p,P W_E P^*p>.
```

The same block appears with the weighted adjoint convention.  The named operator under test
becomes the weighted map, and the coefficient relation survives because the same `W_E` appears
in both entries.

Failure occurs if the unpatched baseline uses a different norm `B_E`:

```text
(tau/2)||B_E q||^2 - (tau/2)||W_E^(1/2)(q-P^*p)||^2.
```

Then a `q-q` entry remains unless `B_E^*B_E=W_E`.  The source no longer has the retained
two-field normal form.

## Response Kinetic Normalization

The relative gain computes the response stiffness.  The response kinetic norm still has to be
read from the same source package or from a separately justified trace metric:

```text
||p_r||_kin^2 = m_r(u) |p_r|^2.
```

On a retained singular sector, canonical normalization gives:

```text
K_r^can = K_r(u)/m_r(u).
```

The route survives only when `m_r(u)` is common across the compared sectors, or when the source
computes a controlled correction.  If the kinetic norm of `p` is the image norm
`||P^*p||^2`, the multiplier collapses to one on every nonzero retained sector.

## Admission Criteria

A relative-gain block can enter the active derivation only if one of the following source
origins is written before the comparison:

```text
1. boundary/interface effective action difference between unpatched and patched configurations;
2. finite trace source principle whose observable is the response improvement;
3. constraint or saddle action where G is the unreduced quadratic form and stability is supplied
   by other fields;
4. determinant or gluing source whose second variation is the graph-distance improvement.
```

In each case the source has to provide the baseline, patched norm, response field, and response
kinetic norm in the same convention.

The following constructions do not pass admission:

```text
choosing the relative sign only to cancel the q-q entry,
adding a free counterterm to tune beta,
using a positive mismatch energy as the final Hessian,
integrating out p before reading the retained spectrum,
choosing P after the desired multiplier is known,
using image stiffness as the kinetic norm of p.
```

## Proargument

The strongest current chain is:

```text
unitary branch or trace norm
  -> one mismatch energy E_mis(q,p),

source computes response improvement
  -> G=E_mis(q,0)-E_mis(q,p),

same squared norm
  -> mixed term and P P^* stiffness with unit coefficient ratio,

separate common response kinetic norm
  -> multiplier survives canonical normalization,

named group-action or boundary operator
  -> mu_r and shifts are computed independently.
```

Together with the KK covariant-derivative normalization result, this gives a coherent route:
ordinary KK symmetry can protect the dimensionless group-action multiplier, while a relative
source can protect the signed coefficient.

## Counterargument

The route still lacks the physical source.  A finite or boundary model that contains only the
positive mismatch energy supplies stabilization and branch selection, not the retained signed
block.  A model with an independent image-stiffness term changes the coefficient.  A model whose
response norm equals image stiffness erases the multiplier.  Any of those outputs deletes the
candidate from the De Vries derivation while leaving any non-De-Vries constraint it computes.

## Repair Tests

For the next source proposal, record:

```text
E_mis(q,p) from the parent action,
E_mis(q,0) from the same parent action,
whether the effective observable is a gain, a constraint, or a positive energy,
the norm used in both terms,
the retained response field p,
the response kinetic coefficient m_r(u),
the p-p stiffness operator M,
any independent image-stiffness term,
the named P and computed multiplier mu_r,
the shifts sigma_r^can.
```

Accept the coefficient part only if the source gives the relative gain with one norm and no
independent image term.  Accept the De Vries comparison only after the named operator and
response kinetic quotient have also been computed.

## Ledger Consequence

The algebraic part of the relative-gain route is now settled:

```text
relative gain with one mismatch norm
  -> M=P P^*,
  -> unit coefficient ratio in the signed block.
```

The physical-source part remains open.  The active search therefore narrows to finding a D5,
D6, D7, Calderon, finite trace, determinant, or branch-interface action that naturally computes
that relative gain and its response kinetic norm.
