#!/usr/bin/env python3
"""Generate the four-slot signed M^2 spectrum figure for the manuscript.

Numerical values are taken from algebra/higher_spin_slots.py and the
joint-fit table tab:highers (m = 106.578 GeV, beta = 0.0634).
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Inputs
MZ = 91.1876
MZ2 = MZ * MZ

# Positive sector: algebraic (unperturbed) values from higher_spin_slots.py
# Column "M_+ (GeV)"
M_pos = {
    "1/2": 80.37444307,
    "1": 91.18760000,
    "3/2": 96.53833186,
    "2": 99.57908993,
    "5/2": 101.4534987,
    "3": 102.6802013,
}

# Negative sector: (-1)^F-corrected values from manuscript Table tab:highers
# These are |M_{s,-}|_corr (GeV) at m = 106.578, beta = 0.0634
M_neg_corr = {
    "1/2": 125.30,   # +(-1)^F correction (s=1/2, 2s+1=2 -> +)
    "1": 174.10,
    "3/2": 229.43,
    "2": 278.12,
    "5/2": 332.27,
    "3": 382.27,
}

spin_labels = ["1/2", "1", "3/2", "2", "5/2", "3"]
x_positions = np.arange(len(spin_labels))

# Compute signed M^2 / MZ^2
y_pos = np.array([M_pos[s] ** 2 / MZ2 for s in spin_labels])
y_neg = np.array([-(M_neg_corr[s] ** 2) / MZ2 for s in spin_labels])

fig, ax = plt.subplots(figsize=(7.0, 4.6))

# Connecting vertical lines
for xi, ypp, ynn in zip(x_positions, y_pos, y_neg):
    ax.plot([xi, xi], [ynn, ypp], color="gray", lw=0.6, alpha=0.6, zorder=1)

# Positive sector squares
ax.scatter(
    x_positions,
    y_pos,
    marker="s",
    s=80,
    color="tab:blue",
    edgecolor="black",
    linewidth=0.6,
    zorder=3,
    label=r"$M_{s,+}^2/M_Z^2$ (algebraic)",
)

# Negative sector diamonds (corrected)
ax.scatter(
    x_positions,
    y_neg,
    marker="D",
    s=80,
    color="tab:red",
    edgecolor="black",
    linewidth=0.6,
    zorder=3,
    label=r"$-|M_{s,-}|^2/M_Z^2$ (with $(-1)^{2s+1}\beta m^2$)",
)

# Reference zero line
ax.axhline(0.0, color="black", lw=0.7, alpha=0.7)

# Labels for special slots
# s=1/2 (index 0)
ax.annotate(
    "W",
    xy=(x_positions[0], y_pos[0]),
    xytext=(6, 6),
    textcoords="offset points",
    fontsize=11,
    color="tab:blue",
)
ax.annotate(
    r"$-m_h^2$",
    xy=(x_positions[0], y_neg[0]),
    xytext=(6, -4),
    textcoords="offset points",
    fontsize=11,
    color="tab:red",
)

# s=1 (index 1)
ax.annotate(
    "Z",
    xy=(x_positions[1], y_pos[1]),
    xytext=(6, 6),
    textcoords="offset points",
    fontsize=11,
    color="tab:blue",
)
ax.annotate(
    r"$-v^2/2$",
    xy=(x_positions[1], y_neg[1]),
    xytext=(6, -4),
    textcoords="offset points",
    fontsize=11,
    color="tab:red",
)

# s=3/2 (index 2): annotate the LEP/CMS 95 GeV anomaly
ax.annotate(
    "96.54 GeV\n(LEP/CMS 95 GeV)",
    xy=(x_positions[2], y_pos[2]),
    xytext=(20, 18),
    textcoords="offset points",
    fontsize=9,
    color="tab:blue",
    arrowprops=dict(arrowstyle="->", color="tab:blue", lw=0.7, shrinkA=0, shrinkB=2),
)

# Axes formatting
ax.set_xticks(x_positions)
ax.set_xticklabels(spin_labels)
ax.set_xlabel(r"spin $s$")
ax.set_ylabel(r"signed $M^2 / M_Z^2$")
ax.set_ylim(-4.0, 1.2)
ax.set_xlim(-0.4, len(spin_labels) - 0.6)
ax.grid(True, axis="y", linestyle=":", alpha=0.4)

ax.set_title(
    r"Four-slot signed dV / Poincar\'e-Casimir spectrum, current best fit",
    fontsize=11,
)

ax.legend(loc="lower left", fontsize=9, framealpha=0.9)

fig.tight_layout()
out_path = "/home/codexssh/signed-dv-custodial-project/draft/figs/spectrum.pdf"
fig.savefig(out_path, format="pdf")
print("Wrote", out_path)
