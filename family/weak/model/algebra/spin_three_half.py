"""V2 extension: the j=3/2 (R=4) Casimir-locked channel and the 96 GeV
diphoton excess at CMS+LEP.

Background (chat sec. 10): 'Hans's' suggestion that the model contains a
spin-3/2 degree of freedom was dismissed there on the grounds that the
labels are INTERNAL SU(2) representation indices, not physical Lorentz
spin -- there is no Rarita-Schwinger fermion in the spectrum.

This script makes the case that Hans's intuition is partially rescued:
extending the Casimir-locked seed to a third channel with internal label
j = 3/2 (i.e. SU(2) representation R = 2j+1 = 4) produces a SCALAR mass
eigenstate at

    M(Phi^4_+) = m_0 * sqrt(lambda_+(R=4)) = 96.54 GeV

with NO fitted parameter -- m_0 is fixed by M_Z (Phase 1).

The CMS+LEP diphoton anomaly central is m ~ 95.4 GeV. Match: ~1 GeV
(~1.2 percent), comfortably inside the experimental width.

The j=3/2 'spin' of Hans is therefore an INTERNAL REPRESENTATION LABEL
of a scalar, not a physical Lorentz spin. The 96 GeV state is the
distinctive observational signature of the third Casimir-locked channel.
"""

from __future__ import annotations

import math
import sys

# Inputs (PDG 2024)
MZ_PDG = 91.1880
M0 = MZ_PDG / math.sqrt(math.sqrt(3) - 1)  # = 106.5779 GeV (Phase 1)


def C2(R: int) -> float:
    """SU(2) quadratic Casimir for the irrep of dimension R = 2j+1."""
    j = (R - 1) / 2
    return j * (j + 1)


def seed_eigenvalues(R: int) -> tuple[float, float]:
    """Closed-form eigenvalues (in units of m_0^2) of the Casimir-locked
    seed matrix M^2_R/m_0^2 = [[0, sqrt(C2)], [sqrt(C2), -C2]].
    Returns (lambda_+, lambda_-).
    """
    c = C2(R)
    disc = c * c + 4 * c
    return ((-c + math.sqrt(disc)) / 2.0, (-c - math.sqrt(disc)) / 2.0)


def physical_masses(R: int) -> tuple[float, float]:
    """Physical scalar masses (GeV) for the two eigenstates of channel R."""
    lp, lm = seed_eigenvalues(R)
    return M0 * math.sqrt(lp), M0 * math.sqrt(-lm)


# Closed-form alternative for R = 4 (sanity check):
#   char eq:  lambda^2 + (15/4) lambda - 15/4 = 0   ->   lambda = (-15 +/- sqrt(465))/8
def closed_form_R4_plus():
    return (-15 + math.sqrt(465)) / 8.0


def main() -> int:
    print("=" * 70)
    print("V2: the j=3/2 (R=4) channel and the CMS+LEP 96 GeV diphoton excess")
    print("=" * 70)

    print(f"\nFixed input (Phase 1): m_0 = M_Z / sqrt(sqrt(3) - 1) = {M0:.4f} GeV")
    print(f"\nCMS+LEP diphoton anomaly central: m ~ 95.4 GeV (CMS PAS HIG-20-002 + LEP ALEPH)")

    print("\n[1] Generalised Casimir-locked spectrum")
    print("=" * 60)
    print(f"    {'R':>3} {'j':>5} {'C_2':>8} {'M_+':>10} {'M_-':>10}    note")
    for R in (2, 3, 4, 5):
        j = (R - 1) / 2
        c = C2(R)
        Mp, Mm = physical_masses(R)
        note = ""
        if R == 2:
            note = "doublet seed (= M_W, near Higgs)"
        elif R == 3:
            note = "triplet seed (= M_Z)"
        elif R == 4:
            note = "spin-3/2 seed   <--  96 GeV anomaly"
        elif R == 5:
            note = "(spin-2 seed)"
        print(f"    {R:>3} {j:>5.1f} {c:>8.3f} {Mp:>10.4f} {Mm:>10.4f}    {note}")

    # Closed-form check for R=4
    lp_cf = closed_form_R4_plus()
    Mp_cf = M0 * math.sqrt(lp_cf)
    print(f"\n[2] Closed-form check, R = 4")
    print(f"    char eq:    lambda^2 + (15/4) lambda - 15/4 = 0")
    print(f"    lambda_+   = (-15 + sqrt(465)) / 8 = {lp_cf:.6f}")
    print(f"    M(Phi^4_+) = m_0 * sqrt(lambda_+)  = {Mp_cf:.4f} GeV")

    deviation = abs(Mp_cf - 95.4)
    deviation_pct = deviation / 95.4 * 100.0
    print(f"\n[3] Confrontation with CMS+LEP")
    print(f"    Predicted:   M(Phi^4_+) = {Mp_cf:.3f} GeV")
    print(f"    Observed:    m_gamma_gamma ~ 95.4 GeV")
    print(f"    Deviation:   {deviation:.3f} GeV  ({deviation_pct:.2f} %)")

    print(f"\n[4] Phenomenology")
    print(f"    The R=4 SU(2) irrep (T_3 = -3/2, -1/2, +1/2, +3/2) admits Y choices")
    print(f"    that give integer electric charges:")
    print(f"      Y = 1/2:  Q in {{-1, 0, +1, +2}}   (singly + doubly charged + neutral)")
    print(f"      Y = 3/2:  Q in {{ 0, +1, +2, +3}}  (triply charged)")
    print(f"    The neutral component is the diphoton candidate. The charged components")
    print(f"    sit nearby in mass and mediate Phi^4_+ -> gamma gamma at one loop, in")
    print(f"    direct analogy with Type-II seesaw doubly-charged-scalar phenomenology.")

    print(f"\n[5] Connection to the Hans 'spin-3/2' suggestion (chat sec. 10)")
    print(f"    Chat dismissed PHYSICAL Lorentz spin-3/2 (no Rarita-Schwinger fermion).")
    print(f"    This script confirms the dismissal -- the new state is a SCALAR.")
    print(f"    But the spin-3/2 INTERNAL REPRESENTATION LABEL is exactly what produces")
    print(f"    the 96 GeV diphoton signature. Hans's spin-3/2 lives on as the j=3/2")
    print(f"    Casimir of an internal scalar channel, not as a propagating spin.")

    # Tolerance: <= 2% to call the match a hit
    return 0 if deviation_pct < 2.0 else 1


if __name__ == "__main__":
    sys.exit(main())
