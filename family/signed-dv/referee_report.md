# Referee report (cycle 10 final)

## Executive verdict

**Status: algebraic identity with conditional no-go; publishable in
*EPJ Plus* as a 4–6 page note, not above.**

The cycle-8 critic's bottom line, re-endorsed after cycle-9 fixes:
the construction is a striking algebraic identity at $10^{-5}$,
properly attributed to de Vries (Nov 2004 Physics Forums) and Rivero
(arXiv:hep-ph/0606171, 2006); we add the closed-form
$M_H^2/M_Z^2$ identity, the LEE statistic, the paired-D-term
Lagrangian + conditional no-go, and the FCC-ee falsifier.  PRD/PRL
remain out of reach; *Foundations of Physics* is more selective than
the evidence warrants.

After the cycle-2 critic pass (`critique/cycle2_critique.md`), the cycle-3
analysis revisits the verdict honestly:

* The **trace identity** and **determinant identity** at $3/8$ are *one*
  fact, not two: both equal $-C_s$ by the form $P_s = x^2 + C_s x - C_s$
  (sum of roots = product of roots = $-C_s$).  This was overstated in
  earlier write-ups.
* The Casimir-ratio identification $C_F/C_A = 3/8$ in SU(2) is correct,
  but it is *the same fact* once more, since $C_2[2j+1] = j(j+1) = C_s$.
* The proposed correction $\Delta M_-^2 = (3/8)(M_Z^2 - M_W^2)\sigma_3$ is
  *contradicted by the data at the percent level*: the fitted traceless
  coefficient is $\epsilon_t/(M_Z^2 - M_W^2) = 0.3818$, not $0.3750$.
  The 1.8% deviation is far larger than the m_h experimental error.
* The fit to m_h, in isolation, is essentially exact at $3/8$
  (coefficient 0.37514, within m_h PDG error).  The fit to v/√2 wants
  coefficient 0.388.  An exact traceless $\sigma_3$ cannot do both.

## Exact algebra

* **Are the signed roots correct?**  Yes.  `algebra/verify_signed_roots.py`.
* **Are the trace and determinant identities correct?**  Yes — but they
  are corollaries of a single polynomial property
  ($\sum$ roots = $\prod$ roots = $-C_s$), not two independent
  identities.  This was inflated in earlier write-ups.
* **Are all numerical values reproducible?**  Yes; `./run_checks.sh`
  reproduces every number.

## Physical interpretation

* **Strongest interpretation of the negative roots after correction:**
  the four-slot spectrum reads $\{+M_Z^2, +M_W^2, -m_h^2, -v^2/2\}$,
  with the corrected negative slots matching $-m_h^2$ to $1.6\times10^{-5}$
  and $-v^2/2$ to $8\times10^{-4}$.  This is the cleanest phenomenological
  statement and survives the critic's challenges.
* **Weakest point:** the $\sigma_3$ ansatz is contradicted by the data.
  The actual fit prefers a coefficient 0.382, with a residual
  $\epsilon_s = -12.34\,\mathrm{GeV}^2$ that *does not* match any natural
  one-loop EW radiative scale ($\alpha M_Z^2/4\pi \approx 5$ GeV²;
  $\Delta r \cdot M_Z^2 \approx 300$ GeV²; $\Delta r \cdot v^2/2 \approx
  1100$ GeV²).  The 12 GeV² is too small to be EW radiative, but exactly
  the size of an unmotivated phenomenological residual.

## Main objections (updated post-critic)

1. **No Lagrangian for the signed-root equation.**  Unchanged.
2. **The "trace = det = 3/8" identity is a single tautology.**  The
   $C_F/C_A$ identification is the *same* statement once more.  The
   project should not present these as multiple independent results.
3. **The data prefers coefficient 0.382, not 3/8.**  Fitting $\sigma_3$ to
   m_h alone gives 0.3751 (essentially 3/8); fitting $\sigma_3$ to v/√2
   alone gives 0.388; the symmetric fit gives 0.382 with a 12 GeV²
   trace residual.  No 1-loop EW correction explains the 1.8% shift in
   the right direction.
4. **The on-shell-subtraction is two free parameters tuned to two data
   points.**  $\lambda_{1/2}=+\tfrac38(x_{1,+}-x_{1/2,+})$ and
   $\lambda_1=-\tfrac38(x_{1,+}-x_{1/2,+})$ are independent choices;
   labeling them $\pm (3/8)\Delta x$ is a *choice*, not a derivation.
5. **The σ_3 structure is imposed by basis choice.**  Any 2×2 perturbation
   admits the decomposition $a_0 \mathbb 1 + a_3 \sigma_3 + a_1 \sigma_1
   + a_2 \sigma_2$.  Calling the σ_3-only part "trace-preserving" is
   tautological.
6. **The Fermi-vacuum identification is suspiciously sharp.**  $M_F^{(\rm
   corr)} = v/\sqrt 2$ to 4 parts in $10^4$ is 40× tighter than the
   one-loop EW correction $\Delta r$ would naturally allow, suggesting
   either (i) the construction implicitly anchors to bare $G_F$ rather
   than the renormalized vev, or (ii) the agreement is overconvergent.
7. **The top loop swamps the gauge correction.**  $\delta m_h^2|_{\rm
   top, 1\text{-}loop} \sim -1100\,\mathrm{GeV}^2$ at $\Lambda = m_t$,
   roughly $1.5\times$ the magnitude of the proposed correction and with
   the wrong sign.  The dV correction does not stand out above the
   natural one-loop background.

## Higher-spin slots: empty

Checked $s = 3/2, 2, 5/2, 3$ slots.  None of the positive- or negative-root
mass values lands within 5 GeV of any known SM mass.  The dV structure
therefore picks out *only* the $s = 1$ and $s = 1/2$ slots — i.e. the
adjoint and fundamental Casimirs of SU(2) — and is not part of a
predictive tower.  The four-slot success is *post-dictive* by
construction: 4 numbers from 2 free parameters (overall scale + ratio).

## What the agent could *not* derive

* The dV polynomial form $x^2 + C_s x - C_s = 0$ has no Lagrangian.
* The interpretation of negative roots as $-(\mathrm{mass})^2$ slots is
  a sign convention.
* The exact value $3/8$ is contradicted by the v/√2 fit at the 1.8% level.

## What remains a useful observation

* The closed-form prediction $m_h^2 / M_Z^2 = (15\sqrt{19}+33\sqrt 3+
  5\sqrt{57}+81)/128$ matches the PDG m_h to $10^{-5}$.  This is a
  one-parameter Casimir-ratio fit but agrees with experiment essentially
  exactly.
* The closed-form prediction $\sin^2\theta_W^{\rm dV} = (19-3\sqrt{19}-
  \sqrt{57}+3\sqrt 3)/16 = 0.22310\ldots$ matches the on-shell PDG
  value of $\sin^2\theta_W$ at the $10^{-4}$ level.

## Required follow-up calculations

1. *Pursue the negative-result path*: prove that no dimension-≤6 SMEFT
   operator with a Wilson coefficient compatible with EWPT can generate
   the size $\epsilon_t = 696\,\mathrm{GeV}^2$ on $\delta m_h^2$.  If
   true, this is a clean small PRD-style result and is the most credible
   physics outcome.
2. *Bethe–Salpeter check*: ask whether the de Vries quadratic emerges
   from a 2-body bound-state equation; if yes, the negative root has a
   physical anti-bound-state interpretation, removing the sign-convention
   issue.
3. *Repeat the analysis with PDG-2024 inputs consistently* (currently
   m_h uses PDG 2024 central value with no error band; M_W is mixed
   between PDG average 80.369 and the on-shell PDG 80.379).
