# Loop 43 Advisor

## Conceptual Route

Make Loop 43 a Ward-projected neutral-current tightening loop.  Section IV
should define \(\Delta_Y(u_{\rm EW})\) as a source remainder and treat
\(\Delta_Y=0\) as a closure outcome.  The charged Goldstone-vector terms should
be framed as the test for \(P_W(h_J)=3/4\).

## Mechanism

The active mechanism remains the CHM interval boundary kernel:
\[
K_T^{\rm DtN}+K_T^{\rm brane},
\]
with photon reference subtraction, CHM product, and shared
\(\Lambda_{\rm CHM}\).  This supplies the clearest source spine for
\(P_\gamma\), \(P_Z\), and \(\widehat\Sigma_{aa,2}^{\rm CHM}=2\).

## Recall Target

Revisit
`context/source_fragments/09_csaki_hubisz_meade_ewsb_from_extra_dimensions_hep_ph_0510275/pages_021-030.md`
and `notes/lean/O1OrderedSampling.lean` for photon zero-mode bookkeeping and
the neutral projector ledger.

## Equation Target

Add the normalized trace definitions
\[
a_\gamma^{(0)}=\frac{g'W_T^3+gB_T}{\sqrt{g^2+g'^2}},
\qquad
z^{(0)}=\frac{gW_T^3-g'B_T}{\sqrt{g^2+g'^2}},
\]
then normalize \(P_{a,J}a_\gamma^{(0)}\) and
\(P_{a,J}\Pi_{\gamma^\perp}^{(T)}z^{(0)}\) in the source product.

## Implementation Package

Revise Sec. IV projector definitions and Goldstone-vector paragraph; revise
Sec. VI.G into proof-obligation prose; remove workflow phrasing from Appendix
D; add \(\Delta_{\rm O1}^{\rm ray}(t)\) to the acceptance criterion; update
open issues, Lean notes, and review records.

## Scores

Conceptual clarity 4; source control 4; string/KK depth 4; proof spine 4; PRD
prose 3; open-gap honesty 5.
