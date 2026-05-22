# Referee/advisor improvement cycle

This file records the autonomous improvement loop to run after each manuscript pass.

## Cycle protocol

1. **Referee A subagent pass.** Call a GPT-5.5 subagent as a skeptical PRD referee focused on correctness, scheme discipline, and overclaiming. Record:
   - central claim;
   - strongest source-supported result;
   - weakest inference;
   - hidden assumptions;
   - exact revisions or calculations needed.
2. **Referee B subagent pass.** Call a second GPT-5.5 subagent as an independent PRD referee focused on string/Kaluza--Klein/\(G_2\) depth, source control, and manuscript structure. Record the same fields as Referee A.
3. **Advisor subagent pass.** Call a GPT-5.5 subagent as an advisor trying to improve the paper after reading both referee reports. Record:
   - one new conceptual route;
   - one string/Kaluza-Klein mechanism to test;
   - one source to read;
   - one equation or diagram the manuscript needs.
4. **Implementation pass.** Apply revisions that improve derivational clarity, source traceability, or conceptual structure.
5. **Editor pass.** Call a lightweight editor subagent, configured below GPT-5.5, to flag banned contrast patterns, journalistic language, hype, adjectival positioning, and deviations from Physical Review D prose. Store the report in `reviews/`, resolve alerts, and run the prose scans.
6. **Random recall pass.** Choose at least one random bibliography or source-inventory entry and one random local note or Lean-style note. Inspect them with the recall skills, then record any equation, test, source-fragment gap, or issue-ledger consequence in `reviews/`, `context/`, or `notes/lean/`.
7. **Surprise recall pass.** If the advisor pass is conceptually exhausted, use `skills/surprise-source-recall/SKILL.md` to search adjacent local fragments and, if needed, web sources.
8. **Notes pass.** Add Lean-style obligations in `notes/lean/` for unresolved derivations.

The three subagent calls are mandatory for every substantial loop: two referee subagents and one advisor subagent, all configured to GPT-5.5. Store their reports in `reviews/` before implementation.
The editor pass is mandatory for every substantial loop. Use a faster model tier
than GPT-5.5 so the editor functions as a style sentinel with a separate scope
from the conceptual referees.

## Cycle 0 status

- Source fragments exist for all local PDFs and CDF-II.
- The manuscript has been reframed as a PRD conceptual program.
- The key idea is the combined positive-branch pole-ratio clue and negative-branch Higgs/order-parameter clue.
- The central missing calculation remains the ordered sampling rule \((J_H,J_{\rm adj})=(3/4,2)\to(M_W,M_Z)\).

## Referee score table

Use scores from 1 to 5. Record the score after each full referee/advisor/implementation loop.

| Loop | Conceptual clarity | Source control | String/KK depth | Electroweak correctness | Open-gap honesty | Referee summary |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 2 | 2 | 2 | 3 | 4 | Seed draft reframed; source corpus created; major derivations still open. |
| 1 | 3 | 3 | 3 | 3 | 4 | Compiled 29-page draft; string/KK, \(G_2\), flavor, global-form, core determinant, and negative branch sections expanded; central derivations remain open. |
| 2 | 4 | 3 | 4 | 4 | 4 | Compiled 33-page draft; formal pole-scheme ledger, custodial assignment theorem target, and toy endpoint-boundary operator added; central derivations remain explicit open targets. |
| 3 | 4 | 4 | 4 | 4 | 5 | Compiled 43-page draft; theorem-target appendix and endpoint/brane-Higgsing dictionary added; remaining speculative claims are explicitly attached to derivation targets. |
| 4 | 4 | 4 | 4 | 4 | 5 | Compiled 44-page draft; radical-placement ledger added to connect source theory, operator, matrix, branches, pole ratio, scalar functional, and topology constraints. |
| 5 | 4 | 4 | 5 | 4 | 5 | Compiled 46-page draft; KK interval section expanded with variational boundary data, interval kernel, entry dictionary, electroweak assignment theorem, and scalar-branch target. |
| 6 | 5 | 4 | 5 | 4 | 5 | Compiled 49-page draft after \(G_2\) expansion; singular support, Higgs-bundle variables, local kernel, anomaly/global checks, and scalar-branch map added. |
| 7 | 5 | 5 | 5 | 5 | 5 | Compiled 62-page draft; route-comparison section, expanded negative-branch scalar-functional analysis, and status ledger added. |
| 8 | 5 | 5 | 5 | 5 | 5 | Added O10 dimensional-interpolation theorem target, source-status table, Schur-complement bridge, \(G_2\) entry targets, and pole-matching chain; determinant and assignment derivations remain open. |
| 9 | 5 | 5 | 5 | 5 | 5 | Compiled 66-page draft; exact pole parameterization, Breit--Wigner mass/width convention chain, O8 self-energy matching theorem, and adjacent `prTalks` source-note/Lean index added. |
| 10 | 5 | 5 | 5 | 5 | 5 | Parent-workspace pass added source-note guardrails, one-source normalization audit, custodial single-generator obstruction, and O12 validation issue; manuscript derivations remain explicit open targets. |
| 11 | 5 | 5 | 5 | 5 | 5 | Normalized abstract, introduction, route comparison, and conclusion around assumptions and theorem targets; added electroweak mass-map and matching refinements. |
| 12 | 5 | 5 | 5 | 5 | 5 | Added unified source-to-pole Target 0, tightened route basis/projection obligations, clarified dimensional endpoint status, and indexed the broader parent workspace inventory. |
| 13 | 5 | 5 | 5 | 5 | 5 | Added electroweak ray admissibility as a theorem target, separated dimensional and electroweak interpolation parameters, and sharpened the \(G_2\) inner-product obligation. |
| 14 | 5 | 5 | 5 | 5 | 5 | Added targeted parent-workspace audit notes for Wrong Turn provenance, trace-space separation, Wigner--Eckart failure modes, SO(32) flavor/string boundary obligations, and top-sector cautions. |
| 15 | 5 | 5 | 5 | 5 | 5 | Demoted Casimir framing to input status, added audit-derived admissibility filters, recorded Wigner--Eckart as a failed tested subroute, and tightened SO(32) flavor/string boundary obligations. |
| 16 | 5 | 5 | 5 | 5 | 5 | Normalized O17 into an electromagnetic endpoint theorem target, added scalar/vector and \(U(1)_{\rm em}\) matching obligations, and recorded parent/prTalks source provenance for the alpha route. |
| 17 | 5 | 5 | 5 | 5 | 5 | Normalized O18 into a Regge-intercept survival target, separated sector and oscillator labels, and moved higher-slot phenomenology into a source-audited assignment ledger. |
| 18 | 5 | 5 | 5 | 5 | 5 | Normalized O10 as a factorized active-channel interpolation, demoted the \(D=9\) endpoint to a geometric \(U(1)\) until the electromagnetic embedding theorem, and added a top-sector source-map target. |
| 19 | 5 | 5 | 5 | 5 | 5 | Sharpened the interval route with CHM source boundary data, a Dirichlet-to-Neumann kernel target, electroweak boundary proof obligations, and parent-root triage refresh. |
| 20 | 5 | 5 | 5 | 5 | 5 | Added route-matching remainders, split interval source data from open normalization, marked the CHM Dirichlet-to-Neumann subtarget as the source-controlled route test, and recorded the eaten-Goldstone boundary-kernel synthesis. |
| 21 | 5 | 5 | 5 | 5 | 5 | Integrated the interval source pack, repaired source indexing, added gauge-fixing and source-to-pole obligations for the eaten-Goldstone square, and placed running-alpha and diphoton material into theorem ledgers. |
| 22 | 5 | 5 | 5 | 5 | 5 | Added O19 as Target IX, recorded branch-scaling and brane-duality admissibility, updated Lean/source ledgers, and normalized Appendix D acceptance conditions. |
| 23 | 5 | 5 | 5 | 5 | 5 | Promoted O20 into Target X, added local SUSY-QM/electroweak-superconnection sources, recorded the Hodge factorization route, and kept the breaking operator and projection as explicit obligations. |
| 24 | 5 | 5 | 5 | 5 | 5 | Refined O1 through the electroweak-superconnection assignment test, added scheme-safe pole remainders, refreshed the parent workspace inventory, and made CHM/Target X the active source-controlled route test. |
| 25 | 5 | 5 | 5 | 5 | 5 | Closed O13--O15 as normalization guardrails, added O16 project-source status, sharpened CHM/superconnection filters, and refreshed the parent-directory source inventory. |
| 26 | 5 | 5 | 5 | 5 | 5 | Added claim-status taxonomy for dimensional interpolation, expanded the single-source \(u\) datum with \(v,m_h^2,K_J,\mathcal Y_{\rm top}\), and sharpened O17, CHM/top, and \(G_2\) endpoint obligations. |
| 27 | 5 | 5 | 5 | 5 | 5 | Normalized the CHM current-entry extraction, recorded the Loop 27 parent-directory read, added the BF-admissible Berger-\(S^3\)/CHM target, and updated Lean/source ledgers. |
| 28 | 5 | 5 | 5 | 5 | 5 | Added hatted CHM current-entry normalization, recorded the source-scale convention audit, and linked the Hodge/SUSY-QM off-diagonal test to the CHM diagonal-current test as the active proof spine. |
| 29 | 5 | 5 | 5 | 5 | 5 | Closed O2a, O5, O6, O7, O9, O11, O12, and O16 as structural normalization issues, preserved residual derivational obligations, and normalized Sec. IX fixed-filter prose. |
| 30 | 5 | 5 | 5 | 5 | 5 | Rendered CHM convention audit, photon-reference subtraction, hatted current-entry theorem target, parent-directory source extraction, and updated O4/source/Lean ledgers. |
| 31 | 5 | 5 | 5 | 5 | 5 | Added O10 single-source pass/fail package with \(\Lambda_J\), inner product, projection, hatted kernel, endpoint subtargets, optional CHM top extension, and parent-directory source queues. |
| 32 | 5 | 5 | 5 | 5 | 5 | Tightened O3 into a same-source scalar-functional target with \(J_\star\), \(C_{\rm sc}\), scheme/scale, holonomy-curvature route, auxiliary-branch failure outcome, and parent-directory source queue. |
| 33 | 5 | 5 | 5 | 5 | 5 | Tightened O1 into a same-source ordered-sampling package with \(P_W\), \(P_Z\), \(P_\gamma\), shared \(\Lambda_J\), CHM \(h_J/W/Z/\gamma\) ledger, Coquereaux grading vocabulary, and parent-directory source queue. |
| 34 | 5 | 5 | 5 | 5 | 5 | Tightened O4 into an entry-by-entry source-kernel ledger: CHM current entry first, Hodge/SUSY-QM square-root entry second, \(G_2\) local audit third, endpoint/Chan--Paton matrix arena, and parent-directory source queue. |
| 35 | 5 | 5 | 5 | 5 | 5 | Tightened O17 into a photon-zero endpoint theorem target with scalar/vector normalization, compact \(U(1)_{\rm em}\) kinetic normalization, split \(\theta/\alpha\) matching remainders, Salam--Strathdee/Witten source trail, and Jegerlehner/Martin--Robertson scheme trail. |
| 36 | 5 | 5 | 5 | 5 | 5 | Tightened O18/O19 into a shared sector-duality package \(\mathfrak R_j\), separating DeVries sector label, oscillator level, physical spin, and putative brane angular momentum, with D0/space-filling labels demoted to admissibility diagnostics. |
| 37 | 5 | 5 | 5 | 5 | 5 | Removed remaining loop/provenance language from O1/O10 body passages, added the CHM single-source interval theorem diagram, and tied dimensional interpolation to manuscript-facing sources. |
| 38 | 5 | 5 | 5 | 5 | 5 | Tightened O20 into a source-equation target: rendered Witten pages 665--666 support the Hodge square-root template, while the one-channel \(B_J\), ordered electroweak samples, and pole-chain map remain explicit theorem data. |
| 39 | 5 | 5 | 5 | 5 | 5 | Tightened the Coquereaux O1/O20 audit into a graded-curvature projection target, recorded source-internal normalization freedoms and the \(3/8\) weak-angle value, and queued detailed superconnection sources for acquisition. |
| 40 | 5 | 5 | 5 | 5 | 5 | Normalized the active O1/O4/O10/O20 package as a boundary electroweak superconnection on a CHM interval, with one hatted kernel, photon subtraction, ordered projectors, scalar branch, and pole remainder. |
| 41 | 5 | 5 | 5 | 5 | 5 | Tightened exact-looking pole statements with remainders, added the holonomy-superconnection scalar Hessian target, focused O4 on \(\widehat\Sigma_{aa,2}^{\rm CHM}=2\), and recorded a random Lean/source recall pass. |
| 42 | 4 | 4 | 4 | 3 | 5 | Recalibrated current-review scores for open derivations; added the Ward-projected neutral-current target, active proof spine, score-table correction, and random Lean/source recall record. |
| 43 | 4 | 4 | 4 | 4 | 5 | Added source-normalized photon and \(Z\) trace definitions, charged Goldstone projector remainder, proof-obligation wording, Appendix D remainder cleanup, and random Lean/source recall record. |

## Scoring rubric

- **Conceptual clarity:** the paper states the pole-placement burden and the role of the negative branch.
- **Source control:** claims point to local fragments or marked source-audit gaps.
- **String/KK depth:** string theory and Kaluza-Klein mechanisms drive the paper.
- **Electroweak correctness:** gauge-Higgs statements, pole/running distinctions, and representation claims are correct.
- **Open-gap honesty:** conjectures, clues, and derivations are labeled with their status.

## Next referee questions

- Does the abstract make the pole-placement burden clear enough?
- Does the string/Kaluza-Klein section demonstrate command of compactification spectra through mechanisms and equations?
- Does the negative-branch section make the Higgs/vacuum clue explicit while keeping the derivation status clear?
- Does the electroweak section correctly place \(J=3/4\) on the Higgs/order-parameter side?
- Which missing source best supports the historical dual-model/QCD-string framing?
- Can a future pass turn one matrix entry into an explicit source-theory derivation?
- Does the pole-scheme section give enough formal definition for PRD review?
- Does the theorem-target appendix give a referee a complete map of assumptions, consequences, and missing derivations?
- Does the three-route comparison ledger constrain future string/Kaluza--Klein work tightly enough?
- Which source-backed historical material should be added next to connect seventies string theory, Regge spectra, endpoint charges, and electroweak structure?
- Does the O10 dimensional Schur-complement target give a concrete enough bridge among dimensional interpolation, the ordered \(J\)-assignment, the DeVries kernel, and pole placement?
- Does the parent-workspace normalization audit give strong enough failure-mode tests for the next endpoint, interval, brane, KK, Regge, or \(G_2\) derivation attempt?
- Does the A1--A3/T1--T3 hierarchy make the main text read as paper-level exposition while preserving all open obligations?
- Does Target 0 give a complete acceptance test from source theory to reduced kernel, ordered W/Z sampling, and complex-pole matching?
- Which parent-workspace cluster should receive a targeted audit after the broad `..` inventory: `../prTalks`, `../hans/signed_dbdevries`, `../weak`, or `../phys4/notes`?
- Does the rank-and-ray theorem make the allowed electroweak deformation precise enough for source-route testing?
- Can one interval or \(G_2\) source route derive the map from a dimensional or geometric parameter to the electroweak radial ray?
- Do the audit-derived filters now make coefficient transfer, failed parent routes, and SO(32) completion obligations referee-checkable?
- Does Target VII state enough scheme, threshold, and compactification data for
  a referee to see exactly what the alpha endpoint route must prove?
- Which primary source best controls running \(\alpha(Q)\) near the proposed
  matching region, including hadronic vacuum polarization conventions?
- Does Target VIII make the \(j\), \(N_{\rm osc}\), and physical-spin labels
  distinct enough for a string/KK referee?
- Which primary experimental and phenomenology sources are required before a
  low-mass diphoton or charge-\(4/3\) reading can enter manuscript prose?
- Does the factorized active-channel diagram make the \(D=11/10/9\) and
  colourless \(D=7/6/5\) stories read as one theorem target?
- What source or calculation can decide whether the \(D=9\) geometric
  \(U(1)\) has Standard Model electromagnetic normalization?
- Can the interval route produce a common source variable
  \(u\mapsto(t_{\rm dim},t_{\rm EW},\mathcal F_{\rm sc},\mathcal Y_{\rm top})\)?
