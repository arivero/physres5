# Negative-Sector Physical Fit

## Purpose

This cycle checks the clue that the corrected negative roots fail individually
but nearly preserve the negative-sector trace.  The calculation is in
`algebra/negative_sector_fit.py`.

For each input set, define

```text
Delta_H = m_h^2 - M_H0^2
Delta_F = (v/sqrt(2))^2 - M_F0^2
gap     = M_Z^2 - M_W0^2.
```

The target correction would imply

```text
Delta_H/gap = 3/8,
-Delta_F/gap = 3/8,
Delta_H + Delta_F = 0.
```

## Results

### Project-statement inputs

Inputs:

```text
M_Z = 91.1876 GeV
m_h = 125.20 GeV
G_F = 1.1663788e-5 GeV^-2
```

Fit:

```text
Delta_H/gap                  = 0.3751387901
-Delta_F/gap                 = 0.3884437590
(Delta_H-Delta_F)/(2 gap)    = 0.3817912745
(Delta_H+Delta_F)/gap        = -0.0133049688
```

The Higgs shift alone is essentially `3/8`.  The Fermi/vev shift prefers a
larger coefficient.  The traceless best-fit coefficient is above `3/8`.

### PDG Live 2026 comparison inputs

Inputs accessed on 2026-05-14:

```text
M_Z = 91.1879 GeV
m_h = 125.13 GeV
G_F = 1.1663787e-5 GeV^-2
```

Fit:

```text
Delta_H/gap                  = 0.3656374888
-Delta_F/gap                 = 0.3885498696
(Delta_H-Delta_F)/(2 gap)    = 0.3770936792
(Delta_H+Delta_F)/gap        = -0.0229123808
```

The current Higgs central value weakens the individual `3/8` agreement, while
the traceless coefficient remains close to `3/8`.

## Interpretation

The original observation is strongest when the Higgs central value is taken as
`125.20 GeV`.  With current PDG Live central values, the fit is still nearby but
less striking.

This does not produce a derivation.  It tells us where a future model would
have to work:

1. explain why the Higgs shift lands close to `3/8 gap`;
2. explain why the Fermi/vev shift is larger;
3. explain why the trace leak is small but nonzero if the correction is not
   exactly traceless in physical observables.
