# SEED DOCUMENT — Casimir-locked seesaw for EWSB
# DO NOT OVERWRITE. Re-attach at start of every session.

Two SU(2) representations contribute to electroweak symmetry breaking:
R = 2 (doublet) and R = 3 (triplet/adjoint).

For each R, define the 2x2 mass-squared seed:

    M_R^2 = m_0^2 * [[ 0,        sqrt(C2(R)) ],
                     [ sqrt(C2(R)), -C2(R)    ]]

with t_R^2 = C2(R).

Doublet: C2(2) = 3/4, t_2 = sqrt(3)/2
Triplet: C2(3) = 2,   t_3 = sqrt(2)

Eigenvalues:
  doublet: m_0^2 * { (sqrt(57)-3)/8 , -(sqrt(57)+3)/8 }
  triplet: m_0^2 * { sqrt(3)-1     , -(sqrt(3)+1)     }

Inputs (experimental): M_Z = 91.1876 GeV, G_F = 1.1663787e-5 GeV^-2.
Outputs (predicted):   M_W = 80.369 GeV, m_h ~ 125.3 GeV.

Internal seed scale: m_0 ~ 106.58 GeV. This is NOT a Higgs mass.

Trace-preserving spurion Delta ~ 700 GeV^2 shifts the bare negative root
  m_h,bare ~ 122.4 GeV  ->  m_h,phys ~ 125.3 GeV
with f^2 = f_0^2 - Delta where f = v/sqrt(2).

NOT YET DERIVED:
  - why R=2 and R=3, not other pairs
  - the algebraic origin of Delta
  - the fermion sector
  - the connection to the sBootstrap (arXiv hep-ph/0512065) and
    to SO(32) scalars (arXiv 2407.05397)

CONVENTIONS:
  - Metric and sign conventions: SM standard (mostly-plus is fine).
  - C2(R) is the quadratic Casimir of SU(2) in representation R.
  - All masses in GeV.

EXPERIMENTAL TARGETS (PDG 2024 / G_F-derived):
  M_W       = 80.369  GeV
  m_h       = 125.20  GeV
  v/sqrt(2) = 174.10  GeV
  m_e       = 0.5109989 MeV
  m_mu      = 105.65837 MeV
  m_tau     = 1776.86 MeV
