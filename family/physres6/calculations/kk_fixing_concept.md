# Kaluza–Klein fixing — the conceptual core of the paper

Without this, the numbers are numerology. With it, they are evidence.

## The problem, stated by Witten (1981)

Witten's realistic Kaluza–Klein analysis [WittenKK1981, pp. 011–017] states two
facts on the same page:

1. **The gauge couplings are determined by the geometry.** They scale as a power
   of `1/(M_p R)`, with `R` the radius of the extra dimensions. *The coupling is
   the size.*
2. **The geometry is not fixed.** "The field equations do not determine the
   radius of the circle. Space-time dependent fluctuations of this radius would
   be observed as a massless scalar degree of freedom." `R` is a modulus.

Together: Kaluza–Klein makes each coupling a geometric quantity but leaves the
geometry a free modulus. **A KK theory predicts couplings only if something
fixes the modulus.** That missing ingredient is "KK fixing."

## The claim: the order parameter is the modulus-fixer

The breaking operator `Q(J)` has two branches, and they do two different jobs:

- **positive branch `x₊(J)`** — the massive gauge KK vectors (`W`, `Z`); the
  mixing angle is the ratio across levels `J=3/4` and `J=2`.
- **negative branch `x₋(J)`** — a mode whose condensation **fixes the modulus
  `R`**. It is the order parameter / vacuum.

So one operator both populates the gauge spectrum *and* stabilizes the size.
Electroweak symmetry breaking (the negative branch condensing) **is** Kaluza–Klein
modulus stabilization. Once `R` is pinned by the vacuum, Witten's geometric
coupling is no longer free, and `g`, `sin²θ`, `α` are all determined. That is why
the couplings are not independent inputs.

## Why α is infrared (a consequence, not an add-on)

The coupling is read where the geometry is fixed — at the compactification /
condensation scale, not at `M_Z`. So `1/α=135.3` should match the running
coupling in the infrared (`~1` GeV, hadronic region), between `1/α(0)=137.0` and
`1/α(M_Z)=128.0`. The IR placement is a prediction of the picture: the coupling
is fixed at the scale where the modulus is fixed.

## Why D=10: the fermion bypass (forced, not chosen)

The order parameter interpolates between two endpoints (physres5 O10):
- **D=11, 7 internal dims** — unbroken `SU(3)×SU(2)×U(1)`. Witten 1981 proves
  this seven-extra-dimensional compactification **cannot** yield chiral fermions
  with the correct quantum numbers (the fermion obstruction) [WittenKK1981].
- **D=9, 5 internal dims** — fully broken `SU(3)×U(1)_em`.

Breaking (negative-branch condensation) places the physical system at the
**midpoint, D=10 (6 internal dims)**. This is decisive:
- D=10 is the critical dimension of the superstring, where chiral fermions are
  standard (heterotic / type I on a 6-manifold).
- Witten's no-go is specific to the D=11 unbroken point; the interior at D=10 is
  not subject to it.

So the interpolation is **forced by fermion chirality**, not optional: the system
cannot sit at the unbroken D=11 endpoint (no chiral fermions), and D=10 is also
where the Regge/string trajectories `M²_{n,j,±}=μ²x_{j,±}+n/α'` live and where the
moduli whose stabilization fixes the coupling reside. The candidate chiral
charge-4/3 `s=3/2` state and the top on the negative branch then have a home:
chiral matter exists at D=10.

## Attempt to derive Q(J) from a D=10 reduction (PARTIAL)

Framework: gauge symmetry breaking from extra-dimensional geometry (gauge-Higgs
unification, or Higgsless boundary conditions à la Csáki–Hubisz–Meade [CHM]),
where the 4D gauge field and the breaking scalar are components of one higher-D
gauge field, gauge masses are geometric, and chiral fermions arise from
boundary/internal data [CHM].

At internal level `J=l(l+1)` (Laplacian eigenvalue), a vector and a scalar mode
mix into the `2×2`:
- `A_μ` from a coexact 1-form: bare 4D mass² = `0` (gauge invariance);
- the exact 1-form `dφ` satisfies `|dφ|² = J|φ|²`, so the vector–scalar
  (would-be-Goldstone) mixing is `√J` — grounded by the Hodge exact/coexact
  structure [HL];
- the would-be-Higgs scalar carries mass² `= −J` (tachyonic), from the internal
  curvature/holonomy contribution.

This gives `Q(J)=[[0,√J],[√J,−J]]`, with `tr=−J`, `det=−J`. Crucially `det<0`:
one eigenvalue is tachyonic ⇒ instability ⇒ condensation ⇒ breaking ⇒ modulus
stabilization — exactly the spine.

Status of the three entries:
- `√J` (off-diagonal): **grounded** (exact-form eigenvalue).
- `0` (gauge): **natural** (higher-D gauge invariance forbids a bare mass).
- `−J` (breaking): **open** — needs a specific 6-manifold whose curvature gives
  the would-be-Higgs mass² `= −J·μ²` at each level. Not derived here.

So (2) identifies `Q(J)` as the level-`J` fluctuation matrix of extra-dimensional
gauge symmetry breaking and grounds two of three entries; the tachyonic `−J` is
the remaining computation. The KK-fixing concept does not depend on completing
it; only the quantitative lock to `135.3` does.

## What is grounded vs open

Grounded in the local literature:
- coupling = geometry, radius = free modulus: Witten 1981 [WittenKK1981].
- internal Higgs mechanism, modes "eaten": Duff–Nilsson–Pope [DNP].
- vector (1-form) modes split into exact (would-be Goldstone) and coexact
  (transverse vector), eigenvalues organized by the isometry Casimir `J=l(l+1)`:
  Henkel–Lauret for `S³` [HL]; lens-space spectra [Lauret, daSilva].

Open (these are derivations, not the concept):
1. a specific 6-dimensional (D=10) internal space whose mode reduction yields
   `Q(J)=[[0,√J],[√J,−J]]`;
2. that the negative-branch condensation pins `R` to the value giving
   `1/α=135.3` and the `~1` GeV scale;
3. the assignment `J_W=3/4`, `J_Z=2`.

The conceptual mechanism above is what turns (1)–(3) into a physics program
instead of a coincidence. It is the result the Letter must carry.
