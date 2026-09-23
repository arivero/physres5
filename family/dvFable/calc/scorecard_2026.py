# G1.0 empirical scorecard freeze (2026-06-11).
# Inputs as recorded in loop-history/milestone7-phenomenology-execution
# (PDG-live 2026 / CMS 2026 / PDG direct-ratio entry) plus PDG widths.
# Computes the on-shell sin^2 pulls of the de Vries value under each datum
# and both mass conventions (Breit-Wigner vs pole), the effective digits,
# and re-scores the inherited "(1/2,1) unique within 3 sigma (j<=4)" claim.
import math
from fractions import Fraction

SIN2_DV = 0.2231013223008663          # from calc/devries_core.py (30-digit)
RATIO_DV = 0.8814185598789792

# --- frozen inputs (provenance in the note) ---
MW_PDG, SW_PDG = 80.3625, 0.0077      # PDG live 2026 world avg
MZ_PDG, SZ_PDG = 91.1880, 0.0020
MW_CMS, SW_CMS = 80.3602, 0.0099      # CMS 2026
R_PDG, SR_PDG = 0.88136, 0.00015      # PDG direct m_W/m_Z entry
GZ, GW = 2.4955, 2.085                # widths (PDG 2024), for BW->pole shift


def onshell(mw, sw, mz, sz):
    r = mw/mz
    s2 = 1 - r*r
    ds = math.hypot(2*mw/mz**2*sw, 2*mw**2/mz**3*sz)
    return s2, ds


def pole(m, g):                        # BW (running-width) -> pole mass
    return m - g*g/(2*m)


rows = []
for tag, mw, sw, mz, sz in [
        ("PDG-masses BW ", MW_PDG, SW_PDG, MZ_PDG, SZ_PDG),
        ("CMS-W    BW ", MW_CMS, SW_CMS, MZ_PDG, SZ_PDG),
        ("PDG-masses pole", pole(MW_PDG, GW), SW_PDG, pole(MZ_PDG, GZ), SZ_PDG),
        ("CMS-W    pole", pole(MW_CMS, GW), SW_CMS, pole(MZ_PDG, GZ), SZ_PDG)]:
    s2, ds = onshell(mw, sw, mz, sz)
    rows.append((tag, s2, ds, (s2 - SIN2_DV)/ds))

# direct-ratio entry (convention of the entry itself; quote as-is)
s2_r = 1 - R_PDG**2
ds_r = 2*R_PDG*SR_PDG
rows.append(("ratio-entry    ", s2_r, ds_r, (s2_r - SIN2_DV)/ds_r))

print("scorecard_2026: on-shell sin^2 targets vs de Vries", SIN2_DV)
for tag, s2, ds, pull in rows:
    print(f"  {tag}: sin^2 = {s2:.6f} +- {ds:.6f}   pull = {pull:+.2f} sigma")

pulls = [abs(r[3]) for r in rows]
assert 0.3 < min(pulls) < 0.6 and 1.4 < max(pulls) < 1.7  # band 0.4-1.6 sigma

# effective digits: relative deviation against the most precise datum
s2_best, ds_best = rows[0][1], rows[0][2]
rel = abs(s2_best - SIN2_DV)/s2_best
print(f"  relative deviation (PDG BW datum): {rel:.2e}  -> ~3 matched digits")
assert 5e-4 < rel < 2e-3

# BW->pole shifts for the record
print(f"  BW->pole shifts: dmZ = {MZ_PDG-pole(MZ_PDG,GZ)*1.0:+.4f} -> "
      f"{GZ*GZ/(2*MZ_PDG):.4f} GeV, dmW = {GW*GW/(2*MW_PDG):.4f} GeV")

# --- re-score of the inherited uniqueness claim ---
# Half-integer pairs (j_W, j_Z), 1/2 <= j_W < j_Z <= 4 (X+ monotonic in C, so
# sin^2 in (0,1) needs j_W < j_Z). Pull vs the PDG BW datum. Inherited claim:
# only (1/2, 1) within 3 sigma. This is a re-score of a recorded claim
# against frozen data (T3 accounting), not a fit.
def xplus(c):
    return (-c + math.sqrt(c*c + 4*c))/2


halves = [Fraction(n, 2) for n in range(1, 9)]
hits = []
for jw in halves:
    for jz in halves:
        if jw >= jz:
            continue
        cw, cz = float(jw*(jw+1)), float(jz*(jz+1))
        s2 = 1 - xplus(cw)/xplus(cz)
        pull = (s2_best - s2)/ds_best
        if abs(pull) < 3:
            hits.append((jw, jz, s2, pull))
print("  pairs within 3 sigma of the PDG BW datum (j <= 4):")
for jw, jz, s2, pull in hits:
    print(f"    (j_W, j_Z) = ({jw}, {jz}): sin^2 = {s2:.6f}, pull = {pull:+.2f}")
assert [(h[0], h[1]) for h in hits] == [(Fraction(1, 2), Fraction(1, 1))]
print("  re-score: (1/2, 1) remains the unique pair within 3 sigma; its own")
print("  pull is now ~1.6 sigma (BW) / ~1.2 (pole) / ~0.4 (ratio entry).")
print("scorecard_2026: ALL CHECKS PASS")
