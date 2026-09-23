# Findings

## 1. The charged-lepton section is not a one-input prediction

The abstract says the Hermitian $\mathbb{Z}_3$ circulant predicts $m_e,m_\mu$ "at one anchored input" [PAPER.md](PAPER.md#L11), and the conclusion repeats the same predictive framing [PAPER.md](PAPER.md#L258). But the actual construction in Section 5.4 first fixes

$$
a = \tfrac{1}{3}(\sqrt{m_e}+\sqrt{m_\mu}+\sqrt{m_\tau})
$$

from the full PDG lepton spectrum, then imposes $r=a/\sqrt{2}$, and then separately anchors $\lambda_0=\sqrt{m_\tau}$ [PAPER.md](PAPER.md#L186). Table 3 also labels $m_\tau$ as an anchor rather than an output [PAPER.md](PAPER.md#L194). That means the lepton sector is using the observed spectrum to determine both the center and the phase before presenting $m_e$ and $m_\mu$ as predictions. On the current write-up, this is a constrained reconstruction of the charged-lepton masses, not a one-anchor prediction.

## 2. The electroweak observable counting is internally inconsistent

Table 2 explicitly marks $M_W$ as the anchor, $m_h$ as "anchored by $\Delta$", and $v/\sqrt{2}$ as an external input [PAPER.md](PAPER.md#L112) [PAPER.md](PAPER.md#L115) [PAPER.md](PAPER.md#L116). The text immediately below then says, "With two parameters $(m_0,\Delta)$ the model matches four independent observables" [PAPER.md](PAPER.md#L118). Later, the caveat section correctly states that $M_W$ is anchored, not predicted [PAPER.md](PAPER.md#L242). Those statements cannot all be true at once. On the paper's own bookkeeping, the genuine electroweak outputs are much narrower than the prose claims, essentially $M_Z$ and $m_{h,\mathrm{bare}}$ once $M_W$, $\Delta$, and $G_F$ are treated as inputs.

## 3. The representation-selection scan is not defined against a single target set

Section 3.2 says that for each pair the remaining eigenvalues are tested against $\{M_Z,m_{h,\mathrm{bare}},v/\sqrt{2}\}$ [PAPER.md](PAPER.md#L68). The same sentence then says Table 1 summarizes the maximum fractional error against $\{M_W,M_Z,m_{h,\mathrm{bare}}\}$ [PAPER.md](PAPER.md#L68). The caption changes the metric again and says the table reports the maximum fractional deviation only across $\{M_Z,m_{h,\mathrm{bare}}\}$ [PAPER.md](PAPER.md#L70). Since the uniqueness claim of the $\{2,3\}$ pair leans on this scan, the objective function needs to be stated once and held fixed. As written, the selection result is suggestive, but the scoring criterion is internally inconsistent.

## 4. The flavour-symmetry interpretation makes an unjustified group-theory jump

Section 5.3 correctly identifies the immediate symmetry of the Hermitian circulant as the cyclic permutation $P$ generating $\mathbb{Z}_3$ [PAPER.md](PAPER.md#L182). The text then concludes that the construction admits a natural embedding into an $\mathrm{SU}(3)_F$ flavour symmetry broken to its $\mathbb{Z}_3$ centre [PAPER.md](PAPER.md#L182). That is not the same statement: the center of $\mathrm{SU}(3)$ acts by common phases, while the structure used here is built from permutations in generation space. The natural bridge is a discrete flavour-permutation subgroup, or an $S_3$/Weyl action, not automatically the center of $\mathrm{SU}(3)$. This section needs either a derivation of that embedding or a narrower statement of what is actually being claimed.

## 5. The $(s,c,b)$ success depends on a curated mass input choice

The quark extension is presented as if the same circulant cleanly captures the $(s,c,b)$ tuple, but the calculation is performed on "Rivero's iterated values" rather than on a clearly specified modern benchmark such as running masses at a stated scale [PAPER.md](PAPER.md#L200). Because light-quark masses are strongly scheme- and scale-dependent, exact agreement for one curated tuple does not yet establish that the relation is robust. The paper should either define the renormalization scheme and comparison scale explicitly and test against that benchmark, or present the $(s,c,b)$ result as an illustrative reconstruction rather than an exact empirical success.

# Open Questions

1. What is the minimal independent input set for the charged-lepton circulant? Can $a$ be fixed without importing the full observed lepton spectrum?
2. What single target set defines the ten-pair scan in Section 3.2, and how does the ranking change if that target set is changed?
3. Is the intended flavour statement a $\mathbb{Z}_3$ permutation symmetry, an $S_3$ Weyl action, or an actual breaking pattern from continuous $\mathrm{SU}(3)_F$? Those are different claims and should not be merged.
4. Which renormalization scheme and scale are intended for the $(s,c,b)$ quark masses, and does the claimed exactness survive under that standard choice?

# Summary

The markdown paper is stronger than the earlier draft in one respect: it openly names several caveats instead of hiding them. The remaining problem is not tone but bookkeeping. The paper still overstates what is predicted, mixes input conventions inside key tables, and makes one group-theory step in the flavour section that is looser than the surrounding algebra. Tightening those three areas would materially improve the manuscript's credibility even before any new physics derivation is added.