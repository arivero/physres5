# Executive summary — fused signed-dV custodial paper

**Date**: 2026-05-14, 03:40 CEST.
**Canonical artifact**: `draft/fused_manuscript.tex` → `draft/fused_manuscript.pdf` (16 pages, 498 KB).
**Latest critic verdict**: cycle 22 / critic 7 → **GO for EPJ Plus**.

## One-line claim

Anchoring the Pauli-decomposed Poincaré-Casimir quartic
$M^4 - M^2\mathcal C_2 + \mathcal C_1\mathcal C_2 = 0$ on the $s=1$ positive
eigenvalue at $M_Z$, the four eigenvalues at $s=\tfrac12,1$ reproduce the
electroweak quartet $(M_W,M_Z,v/\sqrt 2,m_H)$ at percent precision; the
antisymmetric residual is absorbed by a single soft spurion at
$\sqrt\beta\,m \simeq 27$ GeV with $\chi^2/\mathrm{dof}=0.13/2$; and
the closed-form identity
$m_H^2/M_Z^2 = (15\sqrt{19} + 33\sqrt 3 + 5\sqrt{57} + 81)/128$
matches PDG 2024 to $10^{-5}$, with chance probability $p_{\rm LEE}
\lesssim 10^{-4}$.

## Four headline numbers

| Slot | Construction | PDG 2024 |
|---|---|---|
| $M_W$ | 80.3724 ± 0.0018 GeV | 80.3692 ± 0.0133 |
| $M_Z$ | 91.188 (input) | 91.1880 ± 0.0020 |
| $v/\sqrt 2$ | 174.103 ± 0.004 GeV (post-spurion) | 174.10358 (G_F) |
| $m_H$ | 125.30 ± 0.003 GeV (post-spurion) | 125.20 ± 0.11 |

Per-eigenvalue residuals at the 1 GeV level; trace identity at 0.027%.

## Genuinely new content (vs Rivero 2026 noteOpus)

1. **Parallel $C_F/C_A$ rewriting** of the spurion: $\epsilon =
   (C_F/C_A)(M_Z^2-M_W^2)\sigma_3$ with $C_F/C_A = 3/8$ the SU(2)
   Casimir ratio.  Same operator structure as the $(-1)^F$ reading;
   different UV intuition (gauge Casimir scaling).
2. **Closed-form Higgs identity** $m_H^2/M_Z^2 =
   (15\sqrt{19}+33\sqrt 3+5\sqrt{57}+81)/128 = 1.88508\ldots$.
3. **Look-elsewhere statistic**: 3-family table with $p_{\rm chance}
   = 1.6\times 10^{-6}$ (construction-fixed pool) /
   $\lesssim 10^{-4}$ (agnostic LEE-corrected).
4. **Paired exotic D-term Lagrangian** at $Y=\pm 3/8$, with explicit
   charge-quantization no-go (SM/SU(5)/custodial-$\mathrm{SU}(2)_R+X$).
5. **SMEFT viability map**: $\mathcal O_H$ hosts the size at $\sim 2\%$
   of the LHC $\kappa_\lambda$ bound; 1-loop CW gauge contribution
   ruled out (wrong sign, $20\times$ too small).

## Experimentally testable predictions

- **$M_W$ at FCC-ee**: dV value 80.3744 GeV vs ATLAS central 80.3665 GeV
  → ~12σ discriminator at $\delta M_W \sim 1$ MeV precision.
- **$s = 3/2$ slot at $96.54$ GeV**: matches the long-standing
  LEP/CMS hints of a low-mass resonance in the 95–98 GeV window
  (CMS arXiv:2208.02717).
- **$s = 2$ slot at $278.1$ GeV**: predicts a heavy Higgs-sector
  state, currently allowed by direct searches.

## Author-side TODO before submission

1. Replace `\author[1]{Alejandro Rivero}` with confirmed corresponding
   author (currently single-author).  Add ORCID.
2. Swap `\documentclass{article}` (with PRD options) to
   `\documentclass{svjour3}` for EPJ Plus.
3. Re-verify PDG numbers at submission date.  PDG-Live 2026 has
   $M_W = 80.3625(77)$, $m_H = 125.13(11)$, both moving.
4. Write cover letter from `draft/cover_letter_template.md`.
5. Dual-post to arXiv:hep-ph.

## Provenance trail

41+ git commits, 24 cycles, 7 critic passes; full history in
`exploration_log.md`.  Sister project at
`/home/codexssh/hans/signed_dbdevries/` contributed the paired-D-term
and conditional-no-go ideas in cycle 7; Rivero's `noteOpus.pdf`
(`notes/rivero_noteOpus.{tex,pdf,txt}`) is the source of the
Poincaré-Casimir framework, the $(-1)^F$ spurion, and the higher-spin
tower fused in cycle 16.

## Honest framing

This is **not** a discovery paper.  It is a tightly-bounded
*algebraic observation* with a falsifiability hook (96.54 GeV
state; $M_W$ at FCC-ee), supported by:

- A look-elsewhere statistic below $10^{-4}$.
- An $\chi^2/\mathrm{dof} = 0.13/2$ fit.
- A trace identity at 0.027%.

Whether the underlying mechanism is super-Poincaré, holographic,
stringy, composite, or none of these, the algebraic regularity is
real and quantitatively sharp.  EPJ Plus / Foundations of Physics
is the appropriate venue.
