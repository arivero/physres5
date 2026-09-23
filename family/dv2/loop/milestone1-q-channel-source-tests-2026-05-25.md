# Milestone 1 `q_j` channel source tests -- 2026-05-25

## Input from the current D10 action

The local D10 boundary package supplies:

- the D8-like carrier
  `W9=M4 x CP2 x S1_Q`, with one weak/projective normal;
- the DBI/Wess-Zumino source on `W9`;
- the neutral `Q` boundary field `eta`;
- the endpoint coadjoint-orbit action `S_end^(j)`;
- Wilson insertions `T_a^(j)` and ordered products `T_a^(j)T_b^(j)`.

The existing package supplies the tensor data for the current map

```tex
A_jp=\sum_a T_a^{(j)}p\otimes e_a,
\qquad
A_j^\dagger A_j=J_j.
```

It does not by itself supply a propagating image-channel field with inverse
propagator `B+mu^2J_j`.

## Origin requirements

The required source for `q_j` must supply:

1. a positive field in `Im A_j`;
2. a diagonal operator `B+mu^2J_j`;
3. a mixing `mu^2 A_j` with the boundary/vector pole channel;
4. the same current metric used by the KK weak frame;
5. a single leading pole, or a controlled positive spectral density whose first
   pole has the same residue and gap.

## Test 1: D8 normal fluctuation

The D8-like boundary has one Dirichlet normal coordinate in the weak/projective
factor.  A small normal displacement is a scalar on `W9`.

This candidate has the right geometric location, but it fails the image-channel
test in its bare form:

- a single normal displacement is not a field in `V_j tensor R^3`;
- its mass comes from the DBI second variation, extrinsic curvature, and local
  brane potential, not from the endpoint Casimir `J_j`;
- it has no universal mixing `A_jp_j` with each endpoint sector;
- tensoring it with `A_jp_j` makes it a composite of `p_j`, not an independent
  Gaussian channel with its own denominator.

Decision: the D8 normal fluctuation is not the source of `q_j` by itself.  It
can still contribute to the scalar/radial selector and to the `lambda_H`
branch.

## Test 2: coadjoint endpoint rotor alone

The endpoint action

```tex
S_end^(j)=
\int_{\partial\Sigma}
\langle\lambda_j,
-i g_j^{-1}(\partial_tau+i A_tau^aT_a^{(j)})g_j\rangle d tau
```

is first order on the coadjoint orbit.  Quantization gives `V_j`, and the
Wilson expansion gives insertions of `T_a` and `T_aT_b`.

This gives the algebra in `A_j`, but not the Feshbach denominator:

- the rotor is the finite Chan-Paton/internal endpoint space, not a
  second-order propagating field;
- the Wilson expansion gives local ordered products, not
  `(B+mu^2J_j)^-1`;
- the coefficient of a current-current contact term is not enough to create a
  pole.

Decision: the endpoint rotor supplies the `A_j` tensor but not the `q_j`
propagator.

## Test 3: propagating boundary-current oscillator

The strongest candidate is a first retained open-string boundary-current mode
whose polarization lies in the weak current image:

```tex
q_j\in Im A_j\subset V_j\otimes R^3.
```

This candidate passes the representation and sign tests if its kinetic term is
positive.  The Wilson insertion supplies the mixing tensor, and the canonical
KK current frame supplies

```tex
A_j^\dagger A_j=J_j.
```

The hard calculation is the gap:

```tex
M_q^2 = mu^2 J_j.
```

A standard affine-current conformal-weight gap would give `J_j/(k+2)`, which
is the wrong normalization for the de Vries number.  The wanted channel must
use the target-space current zero modes or a brane-current oscillator whose
mass is controlled by the zero-mode Casimir, not the worldsheet conformal
weight.

Decision: this is the leading constructive candidate.  Milestone 1 reduces to
deriving this oscillator and proving the zero-mode Casimir gap and single-pole
dominance.

## Test 4: Hubbard-Stratonovich field for the second Wilson variation

A Hubbard-Stratonovich field can localize a current-current term.  If the
effective current-current kernel already has the form

```tex
K_j(B)=mu^4(B+mu^2J_j)^-1 P_j,
```

then introducing `q_j` gives the local Feshbach action.

This is useful bookkeeping, but it does not create the physical pole.  With an
algebraic auxiliary field one gets a contact term, not the denominator
`B+mu^2J_j`.  A propagating field or derived positive current-current
correlator is still needed.

Decision: Hubbard-Stratonovich localization is a conversion of a derived
current-current kernel into the `q_j` action.  It is not the source of the
kernel by itself.

## Test 5: RR/current vertical interface mode

The Bailin-Love/Weinberg split contains a vertical contribution to the weak
length.  In the D10 reading this vertical part is naturally associated with
RR/current interface data.

This can help with the common current metric and the scale `mu`, but it does
not by itself carry endpoint representation data:

- RR modes are not naturally fields in `V_j tensor R^3`;
- the vertical length contributes to gauge normalization, not a
  representation-dependent gap `mu^2J_j`;
- it does not produce the endpoint mixing `A_jp_j` without the Wilson/current
  sector.

Decision: the RR/current vertical piece is a normalization and scale source,
not the `q_j` image-channel source.

## Execution result

The source tests leave one viable route:

```text
q_j = first propagating boundary-current oscillator in Im A_j.
```

The D8 normal fluctuation and RR/current vertical piece can support the vacuum
and normalization story.  The endpoint rotor supplies `A_j`.  The
Hubbard-Stratonovich step can rewrite a derived current-current correlator as a
local two-channel action.

Milestone 1 is therefore narrowed to one calculation: derive the quadratic
action of the first boundary-current oscillator and show that its leading
spectral density is

```tex
rho_j(nu)=mu^4J_j delta(nu-mu^2J_j)
```

or that a positive multi-pole density reduces to the same low-energy kernel.

The candidate rotor mechanism is written in
`loop/milestone1-boundary-rotor-casimir-gap-candidate-2026-05-25.md`.  It uses a
zero-mode rotor Hamiltonian `H=(2I)^-1 C_2` with `1/(2I)=mu^2`, separating the
Payen/coadjoint endpoint variable from the propagating oscillator that supplies
the Feshbach denominator.

## Link to the `j=3/2` phenomenology check

If the endpoint/current sector is finite at level two, the physical spectrum
stops at `j=1` and there is no `j=3/2` mass.  If a neighboring moduli branch
turns the boundary-current oscillator into a tower, the next positive-branch
mass is `96.54 GeV`, making the diphoton check in
`loop/jthreehalf-diphoton-phenomenology-check-2026-05-25.md` relevant.
