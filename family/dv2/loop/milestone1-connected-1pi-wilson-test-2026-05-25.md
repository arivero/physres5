# Milestone 1 connected/1PI Wilson test -- 2026-05-25

## Question

The finite branch now depends on one bookkeeping point:

```tex
{\delta^2 W_j\over\delta\xi^a\delta\xi^b}\sim -\mu^2T_aT_b
```

Should this be added as a direct 1PI `p_j` contact after the image channel
`q_j` has already been retained?

## Endpoint action is linear in the source

The endpoint action has the schematic source coupling

```tex
S_{\rm end}^{(j)}
=S_{\rm orbit}^{(j)}+\int_{\partial\Sigma}d\tau\,
A_\tau^a(\tau)J_a^{(j)}(\tau).
```

There is no microscopic `A_tau^2` term in this first-order endpoint action.
Therefore the second derivative of the Wilson factor at zero source is a
two-insertion current correlator:

```tex
{\delta^2 W_j\over\delta A^a(\tau)\delta A^b(\tau')}
\sim
\langle T_{\partial\Sigma}J_a(\tau)J_b(\tau')\rangle.
```

It is a connected response of the endpoint current system after the endpoint
variables have been integrated, not a separate local seagull term in the
retained-field 1PI action.

## Retaining `q_j` already keeps the current response

If the image current oscillator is kept as a local field,

```tex
q_j\in{\rm Im}\,A_j,
```

then the retained 1PI action is

```tex
S_{\rm 1PI}^{(j)}
=\langle p_j,Bp_j\rangle
+\langle q_j,(B+\mu^2A_jA_j^\dagger)q_j\rangle
-\mu^2\langle q_j,A_jp_j\rangle
-\mu^2\langle A_jp_j,q_j\rangle.
```

The connected two-current response seen by `p_j` is obtained after eliminating
`q_j`:

```tex
\Gamma_j(B)
=B-\mu^4A_j^\dagger(B+\mu^2A_jA_j^\dagger)^{-1}A_j.
```

At `B=0`, this gives the unit static contact

```tex
\Gamma_j(0)=-\mu^2{\bf 1}_{V_j}.
```

Thus the `T_aT_b` tensor belongs to the current response that the `q_j` exchange
is representing.  Adding the same Wilson second derivative as a separate direct
1PI `p_j` contact double counts the endpoint current response.

## Equal-time part

The path-ordered product decomposes as

```tex
T_aT_b={1\over2}\{T_a,T_b\}+{1\over2}[T_a,T_b].
```

The antisymmetric commutator part is not a symmetric mass contact.  The
symmetric Casimir contraction is the current-current response.  In the retained
`q_j` description it is reproduced by exchange through the image channel.

## Decision

At the level of connected versus 1PI bookkeeping, the finite branch passes the
no-double-counting test:

- `S_end` is linear in the source and has no direct quadratic seagull;
- the Wilson second derivative is a two-current connected insertion;
- retaining `q_j` is the local 1PI representation of that current channel;
- the raw `T_aT_b` term should not be added again as a direct `p_j` contact.

This removes the Wilson-contact residue obstruction for the finite branch.
Milestone 1 is still not closed: the actual D10 boundary dynamics must derive
the existence, gap, and coefficient of the retained `q_j` oscillator.
