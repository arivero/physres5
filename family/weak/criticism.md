# Findings

## 1. The paper's central electroweak-mass claim is asserted, not derived

The main result is built on directly identifying positive eigenvalues of the scalar seed matrices with the gauge-boson masses, rather than deriving the $W/Z$ mass matrix from the Lagrangian. The abstract already states that diagonalising the scalar seeds and "identifying the positive eigenvalues with $M_W^2$ and $M_Z^2$" fixes $\sin^2\theta_W$ [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L34), and the same move is repeated explicitly in the gauge-sector prediction section [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L188) [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L190). But the preceding Lagrangian still contains the ordinary gauge couplings $g$ and $g'$ [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L171) [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L180), and no gauge-boson mass matrix is derived from vacuum expectation values. As written, the step from scalar eigenvalues to $M_W$ and $M_Z$ is a postulate, not a consequence of the model.

This is especially problematic because the text simultaneously says the triplet portal coupling must stay small so that the triplet vev remains below the $\rho$-parameter bound [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L183), while also using the triplet positive eigenvalue to set $M_Z$ [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L191). Without an explicit symmetry-breaking derivation, the paper has not shown how the triplet seed controls the physical $Z$ mass at all.

## 2. The Higgs-mass "prediction" is not supported by the potential written in the paper

The paper claims that the protected negative trace fixes the physical Higgs mass, with measured $v$ as the only further input [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L37). But the scalar potential still contains unconstrained quartic couplings $\lambda_d$, $\lambda_t$, and $\lambda_{dt}$ [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L175), and the manuscript never performs a minimization or diagonalizes the full physical scalar sector. The key Higgs formula,

$$
m_h^2 + \frac{v^2}{2} = m_0^2\big(|\lambda_{\mathbf 2,-}| + |\lambda_{\mathbf 3,-}|\big),
$$

is simply inserted in the predictions section [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L211), with no derivation from the stated Lagrangian. On the present draft, $m_h$ is therefore not predicted by the model; it is fixed by an extra assumption introduced after the Lagrangian.

## 3. The stated predictive power is overstated and partly circular

Several headline claims overstate what is actually predicted. The abstract says the model agrees with PDG electroweak boson masses at the per-mille level [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L38), but the gauge section then takes $M_Z$ as an input to determine $m_0$ [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L203). Once $M_Z$ is used to normalize the scale, claiming agreement of the model with the full $(M_W,M_Z)$ pair is misleading: only one of those masses is actually tested. The same section also says the derived $\sin^2\theta_W$ is "in agreement with the PDG fit to 10 digits" [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L203), which is not a defensible experimental statement. Current electroweak fits do not determine any definition of $\sin^2\theta_W$ to anything like $10^{-10}$ precision, so this phrasing substantially exaggerates the evidence.

The discussion repeats the same overstatement by saying the framework reproduces $M_W$, $M_Z$, $\sin^2\theta_W$, and $m_h$ at per-mille level using only $M_Z$ and $v$ as inputs [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L268). Given Findings 1 and 2, that summary is stronger than the derivation actually supports.

## 4. The phenomenology sections do not validate the central model claim as strongly as the text suggests

The MadGraph section says the model reproduces SM-like diboson cross-sections and calls this a "non-trivial check" [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L227) [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L241). But the paragraph immediately explains that the BSM physics "does not affect the tree-level gauge-boson amplitudes" [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L239). If that is true, then SM-like leading-order diboson rates are the expected trivial outcome, not a meaningful validation of the Casimir-locking hypothesis.

The EWPT section is also written more strongly than the underlying implementation supports. The paper presents precise $S$, $T$, $U$ numbers and claims agreement within $2\sigma$ [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L253), but the actual script uses an approximate leading-log form for $\Delta S$ and explicitly notes that a full one-loop result would require Passarino-Veltman functions [model/ewpt/STU.py](/home/codexssh/weak/model/ewpt/STU.py#L98). That is useful as a rough consistency check, but not enough to support a polished precision-phenomenology claim in the current wording.

## 5. The draft contains non-scholarly or technically loose framing that should be removed before circulation

The phrase "chat-confirmed role of hypercharge" in the gauge-group section is not acceptable scholarly support [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L168). If the low-energy gauge-group choice is important, it needs a physics argument or citation, not a reference to chat history.

There is also a technical looseness in the line describing the $Y=0$ triplet as "real triplet \`a la Georgi--Machacek" [model/paper/main.tex](/home/codexssh/weak/model/paper/main.tex#L183). A lone real $Y=0$ triplet is not the Georgi-Machacek scalar sector; the custodial GM construction uses a larger triplet content arranged to preserve custodial symmetry. The current phrasing risks confusing readers about what field content is actually being claimed.

# Open Questions

1. What is the explicit gauge-boson mass matrix derived from the Lagrangian after symmetry breaking, and how does it lead to Eq. (gauge_id) without simply postulating the identification?
2. What is the minimization procedure for the scalar potential, and how does it eliminate the freedom in $\lambda_d$, $\lambda_t$, and $\lambda_{dt}$ so that $m_h$ becomes a prediction rather than an ansatz?
3. Which definition of $\sin^2\theta_W$ is being compared to PDG, and what experimental uncertainty should be quoted instead of "10 digits"?
4. Is the 91.2 GeV neutral scalar already excluded by LEP/LHC searches once realistic couplings and mixing angles are included?

# Summary

The current draft has an interesting organizing idea, but the paper overclaims what has been derived. The main issue is not presentation; it is that the central identifications for $M_W$, $M_Z$, and $m_h$ are not yet obtained from the stated Lagrangian. Until those derivations are supplied, the manuscript reads more like a numerically suggestive ansatz than a completed electroweak model.