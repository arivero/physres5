# `j=3/2` diphoton phenomenology check -- 2026-05-25

## Point of the check

The positive-branch mass law gives a sharp side test if the boundary/current
sector has a moduli branch that keeps the next internal representation instead
of truncating at `j=1`.

This is not part of the current proof of the D10 construction.  It is a
phenomenology discriminator between two readings:

- finite branch: the endpoint/current sector is effectively level two and
  keeps only `j=0,1/2,1`;
- tower branch: a nearby moduli slice retains `j=3/2` as a physical neutral
  scalar or scalar-like boundary mode.

## Positive-branch calculation

Use

```tex
X_+(J)=\frac{-J+\sqrt{J^2+4J}}{2},
\qquad
J=j(j+1).
```

Fix the common scale from the `Z` slot:

```tex
M_Z=91.1876 GeV,
\qquad
J_Z=2,
\qquad
X_+(2)=0.7320508075688772.
```

Then

```tex
\mu={M_Z\over \sqrt{X_+(2)}}=106.577412817518 GeV.
```

For the next internal representation,

```tex
j={3\over2},
\qquad
J={15\over4},
\qquad
X_+\!\left({15\over4}\right)=0.8204823316059779,
```

so

```tex
M_{3/2}
=\mu\sqrt{X_+(15/4)}
=96.5383318606582 GeV.
```

The same scale fixed from the `W` slot gives `96.53--96.61 GeV` for the
standard recent `M_W` inputs, so the value is stable at this level.

## Experimental hook

CMS published a full Run 2 search for a standard-model-like low-mass Higgs
boson in the diphoton channel, over `70--110 GeV`, using `2016--2018` data at
`13 TeV`.  The published CMS result reports no significant excess, with the
largest deviation at `95.4 GeV` and local/global significance `2.9/1.3 sigma`.

Source:

```text
CMS-HIG-20-002 / CERN-EP-2024-088,
Phys. Lett. B 860 (2025) 139067,
https://cms-results.web.cern.ch/cms-results/public-results/publications/HIG-20-002/
```

The CMS public briefing records the same Run 2 search and describes the
`95.4 GeV` feature:

```text
https://cms.cern/news/what-if-there-was-second-and-lighter-higgs-boson
```

## D10/moduli interpretation

The `j=3/2` mass is useful only if a D10 moduli branch supplies a physical
channel beyond the level-two endpoint sector.

Required branch conditions:

1. The finite `j<=1` selector must be relaxed or replaced on that branch.
2. The `j=3/2` channel must be `Q` neutral or have a neutral scalar component
   that can decay to two photons.
3. The same positive Feshbach/current kernel and scale `mu` must apply.
4. The mode must have a production and diphoton branching fraction below the
   CMS limits while still capable of creating a `95--97 GeV` excess.
5. The branch must not introduce extra light charged states already excluded by
   LEP or LHC searches.

## Consequence for the research plan

This check does not outrank the kernel-origin problem.  It should be attached
to Milestone 7 and used after Milestones 1, 3, 4, 5, and 6 have produced a
predictive branch.

If the theory forces the finite level-two sector, the `96.54 GeV` state is
absent.  If a neighboring moduli branch retains the tower, the `j=3/2` mass is
a near-term experimental discriminator.
