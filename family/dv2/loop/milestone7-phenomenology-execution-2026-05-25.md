# Milestone 7 phenomenology execution -- 2026-05-25

## Source check

Current external inputs used in this execution:

- PDG live 2026 `W` entry:
  `m_W=80.3625 +/- 0.0077 GeV`,
  `m_W/m_Z=0.88136 +/- 0.00015`.
  Source: `https://pdgprod.lbl.gov/pdgprod/pdgLive/Particle.action?home=&node=S043`.
- PDG 2025 gauge/Higgs summary:
  `m_Z=91.1880 +/- 0.0020 GeV`,
  `m_H=125.20 +/- 0.11 GeV`,
  `sin^2(theta_eff)=0.23148 +/- 0.00013`.
  Source: `https://pdg.lbl.gov/2025/tables/rpp2025-sum-gauge-higgs-bosons.pdf`.
- CMS 2026 `W` mass:
  `m_W=80.3602 +/- 0.0099 GeV`.
  Source: `https://www.nature.com/articles/s41586-026-10168-5`.
- CMS Run 2 low-mass diphoton search:
  largest deviation at `95.4 GeV`, local/global significance `2.9/1.3 sigma`.
  Source: `https://cms-results.web.cern.ch/cms-results/public-results/publications/HIG-20-002/`.

## Tree-level de Vries mass-ratio check

The positive-branch values are

```tex
X_+(3/4)=0.5687293044088437,
\qquad
X_+(2)=0.7320508075688772.
```

Thus

```tex
\sin^2\theta_{\rm dV}
=1-{X_+(3/4)\over X_+(2)}
=0.2231013223008662,
```

and

```tex
{M_W\over M_Z}_{\rm dV}
=0.8814185598789793.
```

Using `m_Z=91.1880 GeV`, the predicted W mass is

```tex
M_W^{\rm dV}=80.37479563824436 GeV.
```

With the PDG live 2026 W mass,

```tex
\sin^2\theta_{\rm OS}
=1-\left({80.3625\over91.1880}\right)^2
=0.2233390021445395.
```

Propagating the stated `m_W,m_Z` errors gives

```tex
\sigma_{\sin^2}=0.00015268229144653166.
```

The pull is therefore

```tex
{0.2233390021445395-0.2231013223008662\over
0.00015268229144653166}
=1.56.
```

Using the CMS 2026 W mass gives

```tex
\sin^2\theta_{\rm OS}=0.22338345807193183,
\qquad
\sigma_{\sin^2}=0.00019435985446957638,
\qquad
{\rm pull}=1.45.
```

Decision: the on-shell mass-ratio comparison remains close, but it is not a
sub-sigma match with current inputs.

## Scheme distinction

The de Vries number above is an on-shell mass-ratio number:

```tex
\sin^2\theta_{\rm OS}=1-M_W^2/M_Z^2.
```

It should not be compared directly to the effective leptonic weak angle

```tex
\sin^2\theta_{\rm eff}=0.23148 +/- 0.00013.
```

The gap between `0.2231` and `0.2315` is the ordinary electroweak scheme and
radiative-correction gap.  Milestone 7 would require a D10 threshold/running
calculation before comparing to running or effective angles.

The PDG summary also notes that the listed `Z` mass is a Breit-Wigner resonance
parameter and lies about `34 MeV` above the real part of the pole position.  If
one shifts `m_Z` down by `34 MeV` as a pole-position control, the `j=3/2` mass
below moves by only about `36 MeV`, not by a GeV.

## Higgs/radial check

The scalar negative-branch target used in the project gives

```tex
J_H={3+\sqrt{57}\over8}=1.3187293044088437.
```

With the same `mu` fixed by the `Z` slot,

```tex
\mu={m_Z\over \sqrt{X_+(2)}}=106.57788032587578 GeV,
```

the raw scalar mass scale is

```tex
\mu\sqrt{J_H}=122.38971037206139 GeV.
```

The measured Higgs mass is `125.20 +/- 0.11 GeV`.  The raw scalar number is
therefore a nearby diagnostic, not a prediction.  The difference is much larger
than the experimental error, and the project has not computed the scalar
Hessian, threshold corrections, or mixing needed to move it.

## `j=3/2` diphoton check

For a tower/moduli branch retaining `j=3/2`,

```tex
X_+(15/4)=0.8204823316059779,
```

and

```tex
M_{3/2}=96.53875533197167 GeV
```

using the same `Z`-fixed scale.

This sits `1.14 GeV` above the CMS full-Run-2 diphoton feature at `95.4 GeV`.
Since the signal strength, width, branching fraction, and production mode are
not computed by the current D10 model, this is only a branch discriminator:

- finite level-two branch: no `j=3/2` state;
- tower/moduli branch: a neutral state near `96.5 GeV` must be confronted with
  diphoton limits and Run 3 data.

## Execution decision

Milestone 7 does not pass as a phenomenological prediction in the current
state.

What is supported:

- the on-shell W/Z mass-ratio number is still close to current data;
- the `j=3/2` branch gives a falsifiable mass near the CMS low-mass diphoton
  feature;
- the scheme distinction is now explicit.

What is not supported:

- no threshold calculation connects the D10 boundary scale to the measured
  on-shell, pole, running, or effective electroweak schemes;
- no scalar Hessian calculation turns the `122.39 GeV` raw scalar scale into
  the observed Higgs mass;
- no production or branching calculation exists for the conditional `j=3/2`
  state.

Milestone 7 therefore remains a later-stage test after Milestones 1, 3, 4, 5,
and 6 have produced a predictive branch.
