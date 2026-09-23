# Mechanism scorecard

This scorecard separates exact algebra, allowed EFT structure, and actual
coefficient derivation.

| Candidate | Mainstream? | Gets custodial spurion? | Gets `sigma_3`/trace? | Gets `3/8` without assignment? | Status |
|---|---:|---:|---:|---:|---|
| Signed-root algebra | N/A | N/A | Yes algebraically | Yes algebraically | Exact identities only |
| Custodial EFT/HEFT | Yes | Yes | Only with added `Psi_-` | No | Symmetry-motivated Wilson coefficient |
| Minimal negative-sector EFT | Yes as EFT | Yes | Yes by operator choice | No, needs `c_Y=3/16` | Cleanest ansatz |
| Two-state projector | Yes as mechanics | N/A | Traceless matrices diagonalize to `sigma_3` | No | Basis/projector not derived |
| Paired exotic D term | Yes as Lagrangian | Yes | Yes, exactly traceless | No, needs `q_S=3/8` | Operator form derived, coefficient assigned |
| Charge quantization | Yes as test | N/A | N/A | Rejects natural `q_S=3/8` | Exotic under SM/`SU(5)` lattice |
| Custodial `SU(2)_R+X` scan | Yes as group test | Yes | N/A | No | `Y=3/8` absent for ordinary `X` lattice |
| Composite Higgs | Yes | Yes | Not naturally | No | Strong-sector coefficients arbitrary |
| Quiver/deconstruction | Yes | Yes | Possible | No | Threshold engineering |
| SUSY D terms | Yes | Partly | Possible | No | Wrong/tunable normalizations |
| Regge field theory | Yes | No | No | `C_F/C_A` appears in wrong observable | Rejected |
| GUT hypercharge | Yes | Coupling boundary | No | No | Same number, different quotient |
| `SU(5)` rep scan | Yes as group test | N/A | N/A | No | `Y=3/8` absent from ordinary tensor lattice |
| Hidden-`U(1)` kinetic mixing | Yes | Possible | Possible with paired fields | No | Continuous mixing parameter |
| String/D-brane UV | Yes as UV model building | Possible | Model-dependent | No universal result | Reduces to EFT matching |

## Current best statement

The strongest mainstream embedding is:

```text
V_eff = 1/2 Psi_-^T [
  m_-^2 1 + c_Y g'^2 (H^\dagger H) sigma_3
] Psi_-,
c_Y = 3/16.
```

Equivalently, a paired exotic D-term can produce

```text
Delta M_-^2 = q_S (M_Z^2-M_W^2) sigma_3
```

with `q_S=3/8`.  Both are legitimate Lagrangian/EFT constructions of the
operator form.  Neither predicts the coefficient from mainstream group theory.

## Classification

The best result is **phenomenological with a symmetry-motivated EFT embedding**.
It is not derived.  The exact step that fails is the replacement of the
single-generator hypercharge spurion by the full `SU(2)` ratio `C_F/C_A`, or
equivalently the assignment of a hidden-sector charge/Wilson coefficient equal
to `3/8`.

The most compact formulation is in `conditional_no_go.md`: under ordinary
custodial EFT assumptions, the operator form is allowed but the coefficient is
not predicted.

## Independent criticism

An independent criticism pass agreed with this classification.  It found no
natural route that avoids either a Wilson coefficient `c_Y=3/16` or an exotic
charge `q_S=3/8`.  The paired D-term model is the strongest explicit
Lagrangian boundary case, but it does not turn the coefficient into a
prediction.
