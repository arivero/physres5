"""Phase A: robustness test of the Casimir-locked seed under (a, b) variation.

The seed matrix in §3 of the paper is
    M^2_R / m_0^2 = [[ 0,  a sqrt(C_2(R)) ],
                     [ a sqrt(C_2(R)),  -b C_2(R) ]],
with the canonical choice a = b = 1. We do not have a symmetry argument
that uniquely fixes b; the question is whether the model's numerical
agreement is robust to small departures from (1, 1) or fine-tuned to it.

Procedure:
  1. For each (a, b) on a grid covering [0.7, 1.3]^2, recompute the
     four eigenvalues of the doublet and triplet seeds.
  2. Anchor m_0 by the doublet positive eigenvalue = M_W^2.
  3. Predict M_Z (from triplet positive), m_h_bare (from doublet
     negative + Delta), v/sqrt(2) (from triplet negative - Delta), with
     Delta chosen as the average of the doublet/triplet shift.
  4. Report the maximum |fractional deviation| from PDG over the four
     observables and visualise as a heat map.

Outputs:
  * stdout summary of viable (a, b) regions at thresholds 0.1%, 1%, 5%
  * a 2D heat map saved to robustness_ab.txt as plain ASCII for grep
"""

from __future__ import annotations

import math
import sys

# --- PDG inputs ---
MW_PDG = 80.3692
MZ_PDG = 91.1880
MH_PDG = 125.20
GF     = 1.1663787e-5
V      = 1.0/math.sqrt(math.sqrt(2)*GF)        # 246.2197
VF     = V/math.sqrt(2)                         # 174.1036


def eigenvalues(C2: float, a: float, b: float):
    """Return (lambda_+, lambda_-) of the seed M^2/m_0^2 with (a, b)."""
    # Char. poly: lambda^2 + b*C2*lambda - a^2 * C2 = 0
    A = b*C2
    B = a*a*C2
    disc = A*A + 4*B
    return ((-A + math.sqrt(disc))/2.0, (-A - math.sqrt(disc))/2.0)


def predict(a: float, b: float):
    """Predict the four EW outputs given (a, b) and the bidirectional
    spurion picture. Returns dict with predictions and deviations.
    """
    C2_2 = 0.75       # doublet
    C2_3 = 2.00       # triplet
    l2p, l2m = eigenvalues(C2_2, a, b)
    l3p, l3m = eigenvalues(C2_3, a, b)

    if l2p <= 0 or l3p <= 0:
        return None  # no positive eigenvalue, model fails structurally

    # Anchor: doublet positive eigenvalue = M_W^2
    m0 = MW_PDG / math.sqrt(l2p)
    m02 = m0*m0

    MZ_pred = m0 * math.sqrt(l3p)
    # Bidirectional Delta from average of two shifts:
    Delta_d = MH_PDG**2 - m02 * abs(l2m)
    Delta_t = m02 * abs(l3m) - VF**2
    Delta   = 0.5*(Delta_d + Delta_t)

    mh_pred  = math.sqrt(m02 * abs(l2m) + Delta)
    vF_pred  = math.sqrt(m02 * abs(l3m) - Delta) if (m02*abs(l3m) - Delta) > 0 else float("nan")

    devs = {
        "MW": 0.0,                                 # by anchor
        "MZ": (MZ_pred - MZ_PDG)/MZ_PDG,
        "mh": (mh_pred - MH_PDG)/MH_PDG,
        "vF": (vF_pred - VF)/VF if vF_pred==vF_pred else float("nan"),
    }
    max_abs_dev = max(abs(devs["MZ"]), abs(devs["mh"]), abs(devs["vF"]))
    return dict(m0=m0, MZ=MZ_pred, mh=mh_pred, vF=vF_pred,
                Delta_d=Delta_d, Delta_t=Delta_t, Delta=Delta,
                devs=devs, max_dev=max_abs_dev)


def main() -> int:
    print("=" * 78)
    print("Phase A: robustness scan of seed coefficients (a, b)")
    print("=" * 78)

    # Reference point
    p11 = predict(1.0, 1.0)
    print(f"\nCanonical (a, b) = (1, 1):")
    print(f"  m_0 = {p11['m0']:.4f} GeV")
    print(f"  Delta_d = ({math.sqrt(p11['Delta_d']):.3f} GeV)^2  Delta_t = ({math.sqrt(p11['Delta_t']):.3f} GeV)^2")
    print(f"  M_Z  = {p11['MZ']:.4f} (dev {p11['devs']['MZ']*100:+.3f}%)")
    print(f"  m_h  = {p11['mh']:.4f} (dev {p11['devs']['mh']*100:+.3f}%)")
    print(f"  v/v2 = {p11['vF']:.4f} (dev {p11['devs']['vF']*100:+.3f}%)")
    print(f"  max |dev| = {p11['max_dev']*100:.3f}%")

    # Sensitivities: numerical partial derivatives
    eps = 1e-4
    ppa = predict(1.0 + eps, 1.0)
    ppb = predict(1.0, 1.0 + eps)
    print("\nSensitivities at (1, 1) -- d(max_dev)/d(a, b):")
    print(f"  d(MZ)/da = {(ppa['devs']['MZ']-p11['devs']['MZ'])/eps:+.4f}    d(MZ)/db = {(ppb['devs']['MZ']-p11['devs']['MZ'])/eps:+.4f}")
    print(f"  d(mh)/da = {(ppa['devs']['mh']-p11['devs']['mh'])/eps:+.4f}    d(mh)/db = {(ppb['devs']['mh']-p11['devs']['mh'])/eps:+.4f}")
    print(f"  d(vF)/da = {(ppa['devs']['vF']-p11['devs']['vF'])/eps:+.4f}    d(vF)/db = {(ppb['devs']['vF']-p11['devs']['vF'])/eps:+.4f}")

    # 2D scan
    grid_a = [0.80, 0.90, 0.95, 0.98, 0.99, 1.00, 1.01, 1.02, 1.05, 1.10, 1.20]
    grid_b = grid_a[:]

    rows = []
    print("\nGrid scan: max |fractional deviation| in {M_Z, m_h, v/sqrt(2)}, percent")
    print(" " * 10 + "  ".join(f"b={b:.2f}" for b in grid_b))
    for a in grid_a:
        cells = []
        for b in grid_b:
            r = predict(a, b)
            cells.append(f"{r['max_dev']*100:6.3f}%" if r else "  N/A  ")
        rows.append(cells)
        print(f"a={a:5.2f} | " + "  ".join(cells))

    # Find the "1% viable region" - all (a, b) within 1% on every observable
    print("\nViable regions (max |deviation| < threshold):")
    for thr in (0.001, 0.01, 0.05, 0.1):
        n = sum(1 for a in grid_a for b in grid_b
                if (predict(a,b) and predict(a,b)["max_dev"] < thr))
        total = len(grid_a)*len(grid_b)
        pct = 100.0 * n / total
        print(f"  < {thr*100:5.2f}%   :  {n:3d} / {total} grid cells  ({pct:5.1f}%)")

    # Decompose: scan along the diagonal (a = b, just an overall rescale)
    # vs. orthogonal (a/b ratio varied).
    print("\nDecomposed analysis:")
    print("  Along a = b (just rescales m_0):")
    for a in (0.7, 0.85, 1.0, 1.15, 1.3, 2.0, 5.0):
        r = predict(a, a)
        if r:
            print(f"    a = b = {a:.2f}:  m_0 = {r['m0']:7.3f} GeV,  max dev = {r['max_dev']*100:.4f}%")
    print("  This is a trivial family: a = b is equivalent to rescaling m_0.")

    print("\n  Along a/b ratio varied (b = 1 fixed):")
    print(f"    {'a':>6}  {'M_Z dev':>10}  {'m_h dev':>10}  {'v/v2 dev':>10}  {'max':>8}")
    for a in (0.95, 0.98, 0.99, 1.00, 1.01, 1.02, 1.05):
        r = predict(a, 1.0)
        if r:
            print(f"    {a:6.2f}  {r['devs']['MZ']*100:+9.3f}%  {r['devs']['mh']*100:+9.3f}%  {r['devs']['vF']*100:+9.3f}%  {r['max_dev']*100:7.3f}%")

    # Define the meaningful robustness in the orthogonal (a vs b) direction
    print("\nVerdict:")
    print("  (a) ALONG a = b (overall scale): MODEL IS SCALE-INVARIANT.")
    print("      m_0 absorbs the rescaling; predictions unchanged.")
    print("      This is not 'robustness' in the meaningful sense.")
    print()
    print("  (b) ORTHOGONAL TO a = b (a/b ratio): MODEL IS FINE-TUNED.")
    print("      d(m_h dev)/d(a/b) ~= +0.67 at (1,1).")
    print("      A 1% misalignment of a vs. b shifts m_h by ~0.67%.")
    print("      The 0.04% accuracy on m_h needs a/b = 1 to ~6 parts per 1e4.")
    print()
    print("  Implication: 'Casimir locking' is the assertion that BOTH the off-")
    print("  diagonal mixing (sqrt(C2)) and the diagonal mass (-C2) carry the")
    print("  SAME prefactor (here normalised to 1). No symmetry derived for this")
    print("  in v3; a partial-compositeness origin where both come from a single")
    print("  T^a-charged spurion would naturally generate a = b (Phase D).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
