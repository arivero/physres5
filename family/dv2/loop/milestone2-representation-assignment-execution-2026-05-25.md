# Milestone 2 representation-assignment execution -- 2026-05-25

## Milestone question

Milestone 2 asks whether one boundary rule forces

```tex
j=0,{1\over2},1
```

and assigns them to the photon, W, and Z slots without choosing labels after
the mass formula is known.

## What Borel-Weil supplies

For every half-integer `j>=0`,

```tex
V_j=H^0(CP1,O(2j))
```

is the spin-`j` irreducible representation of `SU(2)`, and

```tex
\sum_aT_a^{(j)}T_a^{(j)}=j(j+1).
```

This proves the availability of the needed Casimirs:

```tex
j=0\Rightarrow J=0,
\qquad
j={1\over2}\Rightarrow J={3\over4},
\qquad
j=1\Rightarrow J=2.
```

It does not exclude higher representations.  By itself the `CP1` line-bundle
construction gives a tower.

## Finite branch: `SU(2)_2`

If the endpoint/current sector is an `SU(2)_2` integrable sector, the allowed
representations are

```tex
j=0,{1\over2},1.
```

On this branch, higher `j` is absent by the level rule.  The assignments are:

- `j=0`: photon slot, because `A_0=0`, the Feshbach coupling vanishes, and
  `Q eta_0=0` protects the electromagnetic boundary.
- `j=1/2`: charged weak slot, because it is the lowest nontrivial
  center-odd/fundamental endpoint sector.
- `j=1`: neutral massive slot, because it is the lowest center-even non-singlet
  and appears in the neutral bilinear
  `V_{1/2}\otimes V_{1/2}^*=V_0\oplus V_1`.

This is a coherent selection rule.  It keeps the observed particles as
four-dimensional spin-one vector poles; the `j` label is internal.

The finite branch also removes the `j=3/2` diphoton state.

## Tower branch

If the boundary-current oscillator is a Peter-Weyl rotor tower, then the same
representation mechanism allows all

```tex
j=0,{1\over2},1,{3\over2},2,\ldots .
```

The first three labels can still be used for photon/W/Z, but higher states are
not excluded.  In that branch, the next positive-branch mass is

```tex
M_{3/2}=96.54 GeV
```

when the common scale is fixed by the `Z` slot.  The diphoton check becomes a
necessary phenomenology test.

## Execution decision

Milestone 2 passes only on the finite `SU(2)_2` branch:

```text
SU(2)_2 endpoint/current sector => j=0,1/2,1 only.
```

It does not pass from the current D10 boundary action alone.  The action uses

```tex
\JJ_2=\{0,{1\over2},1\}
```

as the retained endpoint set, but the local D10 derivation of the level-two
rule is not supplied.

Thus the project now has a branch fork:

1. finite branch: better W/Z predictivity, no `j=3/2` state;
2. tower branch: possible `96.54 GeV` state, but finite-set assignment is no
   longer a prediction.

Milestone 2 therefore feeds back into Milestone 1: deriving the boundary-current
oscillator must also decide whether the oscillator is level-two finite or a
rotor tower.

Rotor stress-test update:
`loop/milestone1-rotor-stress-test-2026-05-25.md` confirms this fork.  The
simple second-order rotor gives the desired Casimir gap but not the finite
level-two spectrum.  The finite `SU(2)_2` sector gives the desired spectrum but
needs a D10 mechanism for a zero-mode Casimir mass operator instead of the
direct conformal-weight gap.
