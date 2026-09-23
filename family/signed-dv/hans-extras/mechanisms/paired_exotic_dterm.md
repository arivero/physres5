# Paired exotic D-term model

## Purpose

This is the most literal mainstream Lagrangian construction found so far for a
trace-preserving negative-sector split.  Add two complex scalars `S_+` and
`S_-` with opposite hypercharges `+q_S` and `-q_S`.  The Abelian electroweak
D-term contains

```text
V_D = g'^2/2 (q_H |H|^2 + q_S |S_+|^2 - q_S |S_-|^2)^2.
```

After electroweak symmetry breaking, with `|H|^2 -> v^2/2`,

```text
delta m_+^2 = + g'^2 q_H q_S v^2/2,
delta m_-^2 = - g'^2 q_H q_S v^2/2.
```

The trace shift is exactly zero.

## Matching

Since

```text
M_Z^2 - M_W^2 = g'^2 v^2/4,
```

the relative coefficient is

```text
kappa = delta m_+^2/(M_Z^2-M_W^2) = 2 q_H q_S.
```

For the Standard Model Higgs convention `q_H=1/2`,

```text
kappa = q_S.
```

The target `kappa=3/8` is obtained by assigning

```text
q_S = 3/8.
```

## What works

This construction satisfies several requested properties:

1. The split vanishes with `g' -> 0`, equivalently in the custodial limit.
2. It is proportional to the same hypercharge spurion as `M_Z^2-M_W^2`.
3. It is exactly trace-preserving for the paired sector.
4. It leaves the ordinary `W/Z` pole masses fixed at tree level except through
   the usual Higgs vev and gauge couplings.
5. It has a conventional Lagrangian origin.

## What fails

The coefficient is not predicted.  It is the assigned hypercharge `q_S`, not
the group-theory ratio `C_F/C_A`.  Writing `q_S=3/8` simply moves the target
number from the Wilson coefficient into the charge table.

The fields are also exotic.  If `S_\pm` are `SU(2)_L` singlets, their electric
charges are `Q=Y=+/-3/8`.  If they are doublets, their component charges are
fractional:

```text
Y=+3/8:  Q =  7/8, -1/8
Y=-3/8:  Q =  1/8, -7/8.
```

Scalars do not introduce gauge anomalies, and vectorlike fermion partners with
opposite hypercharges can also cancel anomalies.  The phenomenological problem
is instead fractionally charged exotic matter unless a confinement, decay, or
hidden-sector mechanism is added.  Those additions are outside the original
signed-root proposal and reintroduce model dependence.

## Verdict

This is a useful boundary case.  It proves that the requested operator can come
from a mainstream Lagrangian, but only after assigning an exotic charge equal to
the desired coefficient.  It is therefore **engineered**, not derived.
