# Experimental Inputs

The exact algebra scripts use the project-stated historical input

```text
M_Z = 91.1876 GeV
G_F = 1.1663788e-5 GeV^-2
```

This choice reproduces the quoted de Broglie-de Vries numerical masses.

For comparison with current public summaries:

| Quantity | Value recorded | Source |
| --- | ---: | --- |
| `M_W` | `80.3692 +- 0.0133 GeV` | PDG 2024 Gauge and Higgs summary table |
| `M_Z` | `91.1880 +- 0.0020 GeV` | PDG 2024 Gauge and Higgs summary table |
| `m_H` | `125.20 +- 0.11 GeV` | PDG 2024 Gauge and Higgs summary table |
| `G_F` | `1.1663788(6)e-5 GeV^-2` | PDG electroweak review / NIST-CODATA 2022 |

PDG Live values accessed on 2026-05-14:

| Quantity | Value recorded | Source |
| --- | ---: | --- |
| `M_W` | `80.3625 +- 0.0077 GeV` | PDG Live 2026 W listing |
| `M_Z` | `91.1879 +- 0.0020 GeV` | PDG Live 2026 Z listing |
| `m_H` | `125.13 +- 0.11 GeV` | PDG Live 2026 H listing |
| `G_F` | `1.1663787(6)e-5 GeV^-2` | NIST-CODATA 2022 constants |

Notes:

- The PDG 2024 gauge/Higgs summary table cites S. Navas et al. (Particle Data
  Group), Phys. Rev. D 110, 030001 (2024), and lists the W, Z, and H masses
  above.  URL: https://pdg.lbl.gov/2024/tables/rpp2024-sum-gauge-higgs-bosons.pdf
- The PDG 2026 live W listing, accessed during this run, gives
  `M_W = 80.3625 +- 0.0077 GeV`.  This illustrates that W averages are still
  moving as post-CDF-II combinations evolve.  URL:
  https://pdgprod.lbl.gov/pdgprod/pdgLive/Particle.action?home=&node=S043
- The PDG 2026 live Z listing, accessed during this run, gives
  `M_Z = 91.1879 +- 0.0020 GeV`.  URL:
  https://pdgprod.lbl.gov/pdgprod/pdgLive/Particle.action?init=0&node=S044
- The PDG 2026 live Higgs listing, accessed during this run, gives
  `m_H = 125.13 +- 0.11 GeV`.  URL:
  https://pdgprod.lbl.gov/pdgprod/pdgLive/Particle.action?home=&node=S126
- The Fermi constant value is quoted in the PDG electroweak review and in
  NIST-CODATA 2022 constants.  The NIST extensive listing gives
  `G_F = 1.1663787(6)e-5 GeV^-2`.  URLs:
  https://pdg.lbl.gov/2024/reviews/rpp2024-rev-standard-model.pdf and
  https://physics.nist.gov/cuu/pdf/all.pdf

The phenomenological comparison in this project should therefore be read as a
comparison against the specified `M_Z=91.1876 GeV` normalization and the
2024-era Higgs/Fermi scales, not as a global electroweak fit.
