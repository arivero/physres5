# Project memory for Codex

## Established project facts

- The current manuscript draft is being developed as a Physical Review D article. The long target is at least sixty pages with readable string-theory and Kaluza-Klein context.
- The central construction is the DeVries/Rivero Casimir mass operator and its positive-root ratio for \(J=3/4\) and \(J=2\).
- Compare with the pole observable \(1-M_W^2/M_Z^2\). Treat running weak mixing angles, on-shell conventions, and Breit-Wigner inputs as scheme-dependent material requiring explicit translation.
- The vacuum scale \(v\) is radial. The DeVries number is treated as angular/projective.
- The construction must preserve the full electroweak broken-to-unbroken ray. Independent one-boson massless limits sit outside the working construction unless a section analyzes them explicitly.
- The W/Z assignment remains a central conceptual calculation. A plausible route uses the Higgs doublet and adjoint/current representation data; observed vector spin alone is insufficient for the \(J=3/4\) sample.
- The negative root is analytically important. Its relation to the Higgs/order-parameter scale remains open.
- Casimir language is a clue and construction. The project focus is electroweak, still related to Kaluza-Klein, strings, branes, and G2 singularities.
- Generation structure has the working flavor caveat: an SO(32)-flavor interpretation may or may not be compatible with compactification topology.

## Current operating memory

- Active phase: conceptual manuscript work.
- Avoid numerical scripts, numerical sanity checks, and filler arithmetic unless the user explicitly opens a calculation phase.
- Real progress means improved manuscript prose, source-backed claims, clearer physical assumptions, Lean-style obligations, referee/advisor records, or updated open issues.
- Treat the positive-branch observation as Hans's clue. The negative branch is part of the same analytical object and motivates a scalar/order-parameter investigation.
- The conceptual burden is radical placement: identify what object carries \(\sqrt{J^2+4J}\), at which scale, and under which scheme.
- The string-theory framing should recover the older dual-model and Kaluza-Klein particle-structure ambition while keeping conjectures labeled.
- Use affirmative exposition. Correct technical errors directly. Avoid rhetorical negative/contrast formulas and adjectival positioning.
- Keep Lean-style notes in `notes/lean/` for obligations, theorem targets, and expert-trigger prompts. These notes are working memory kept outside Lean compilation.
- Maintain referee/advisor review loops, including the score table, so conceptual quality and open gaps are visible across iterations.
- For every substantial loop, call two GPT-5.5 referee subagents and one GPT-5.5 advisor subagent before implementation; record their reports in `reviews/`.
- After each completed referee/advisor/implementation loop, compile, run prose scans, and commit the loop checkpoint.
- Use the local source fragments and source inventory before writing literature claims. Use surprise recall and internet search only to find new source material, then record the source trail.
- Treat `pdftotext` as an access aid. Keep PDFs as source objects for plots, images, radicals, and equation layout. For mathematical content, inspect the rendered PDF and label agent-read transcriptions.
- Adjacent `../prTalks` PDFs have been indexed as project source notes in `context/prtalks_source_notes.md` and `notes/lean/PrTalks.lean`. They preserve idea provenance for the electroweak ray, orbit quadratic, Reggeization alternatives, minimal two-channel block, dimensional interpolation, and negative-branch/top obligations. Literature claims from those PDFs still need primary-source upgrades before manuscript citation.
- The parent workspace pass is indexed in `context/parent_workspace_source_notes.md` and `notes/lean/AdjacentWorkspaceGuardrails.lean`. Valid imports are guardrails and theorem targets: scalar-seed assignments need gauge-Higgs or pole-self-energy maps, each source route must produce the DeVries block from one operator and normalization rule, the negative-sector EFT coefficient needs UV matching, and SO(32)-flavor notes stay inside the flavor-boundary ledger until coupled to the electroweak operator.
- Loop 22 added O19 as Appendix D Target IX: branch scaling and brane-duality admissibility.  The large-\(s\) guardrail is \(x\mapsto -J/x\), \(M_+\to\mu\), and \(|M_-|\sim\mu s\) when \(J=s(s+1)\).  The source route still owes a rotating-brane exponent, branch survival rule, negative-branch mass or scalar reading, and boundary-condition duality map.
- Loop 23 promotes O20 into Appendix D Target X: Hodge/SUSY-QM origin of the DeVries block.  The working target is \(D_Je^0_J=\sqrt J e^1_J\), \(D_J^\dagger e^1_J=\sqrt J e^0_J\), and \(Q_{{\rm red},J}=Q_{{\rm dR},J}+B_J\) with \(B_J=\operatorname{diag}(0,-J)\).  Local source PDFs now cover Witten Morse theory, Fayet gauge/BEH supersymmetry, Gates--Rana worldline supersymmetry, and Coquereaux \(SU(2|1)\) superconnections.  Keep the route in theorem-target status until the \(J\) spectrum, finite projection, breaking term, and O1/O3 compatibility are derived.
- Loop 24 refreshes the parent `..` read and records the active superconnection assignment test.  Use
  \[
  P_W:\Phi_{\rm odd}\mapsto J_H=\frac34,\qquad
  P_Z:F_{\rm even}^{\gamma^\perp}\mapsto J_{\rm adj}=2,
  \qquad
  M_{W,\rm pole}^2/M_{Z,\rm pole}^2
  =
  x_+(J_H)/x_+(J_{\rm adj})+\Delta_{\rm sc}.
  \]
  The required proof uses one gauge-Higgs complex, one inner product, photon-zero and electroweak-ray preservation, a derived pole remainder, and a scalar map for the negative branch.  The parent source-note imports are provenance and guardrails; the manuscript source address is the local Coquereaux fragment set plus Target X.
- Loop 25 closes O13--O15 into `CLOSED_ISSUES.md`.  Casimir framing,
  trace-space separation, and Wigner--Eckart failed-route status now function as
  closed guardrails.  O16 remains open with an explicit project-source label for
  the SO(32) branching data.  The manuscript now uses a neutral-sector
  determinant pole condition, a CHM current-entry target
  \(\Sigma_{aa,J}=J\), and a Target X superconnection/CHM compatibility square.
- Loop 25 parent-directory sidecar reads confirm that `../prTalks` is already a
  source-object queue for electroweak ray, KK-dimensional, Regge, and
  negative-branch ideas; `../weak` and `../phys4` provide superconnection,
  Wigner--Eckart obstruction, Higgs-interpolation, and brane/KK source queues.
  Treat these as source-note provenance until primary literature or explicit
  project-source status supports manuscript use.
- Loop 26 refines dimensional interpolation.  Appendix E now has an explicit
  claim-status taxonomy; the source variable is
  \[
  u\mapsto(t_{\rm dim},t_{\rm EW},v,m_h^2,K_J,\mathcal F_{\rm sc},
  \mathcal Y_{\rm top}).
  \]
  O17 is downstream of O1, O3, O10, and pole/running matching.  The CHM source
  adds third-generation localization and boundary-mixing pressure as the
  top-sector source fact; a DeVries map to \(\mathcal Y_{\rm top}(u)\) remains
  open.  `notes/lean/DimensionalInterpolation.lean` records the obligations.
- Loop 27 answers the direct parent-directory read by recording
  `context/parent_directory_loop27_read.md`.  The active import from
  `../physres6` is conditional KK-fixing architecture, with the middle
  \(D=10\) and \(D=6\) lines still reconstruction labels.  The manuscript now
  defines the CHM current-entry extraction
  \[
  K^{\rm cur}_J(\lambda)=
  \langle a_J,(K^{\rm DtN}_{T,J}+K^{\rm brane}_{T,J}-K^{\rm ref}_{T,J})a_J
  \rangle_{\rm CHM},
  \qquad \Sigma_{aa,J}^{\rm CHM}=J,
  \]
  and adds a BF-admissible Berger-\(S^3\)/CHM middle-line target using the
  Henkel--Lauret one-form Hodge-Laplacian fragment.  `notes/lean/CHMCurrentEntry.lean`
  records the obligations.

## Resume state after context renewal

- Renewal checklist: read the repository-root `AGENTS.md`, then this memory file, then `OPEN_ISSUES.md`, `context/source_inventory.md`, `context/concept_claims_matrix.md`, and `reviews/referee_advisor_cycle.md` before making manuscript claims.
- Active instruction hierarchy for this workspace: preserve precision; label assumptions, conjectures, derived consequences, and open analytical obligations; keep the DeVries relation kinematical until a dynamical derivation is supplied.
- The active thread target remains the long Physical Review D version of at least sixty readable pages unless the user explicitly revises the goal.
- Conceptual work has priority: source reading, manuscript architecture, physical interpretation, theorem targets, referee/advisor critique cycles, and Lean-style notes.
- Verification in the current phase means `make manuscript`. Calculation commands are reserved for a user-approved calculation phase.
- Style rule for renewal: use affirmative exposition; correct technical errors directly; avoid rhetorical contrast formulas and adjectival positioning.
- Current compiled draft: `manuscript/main.pdf`, last known length 84 pages after the Loop 24 `make manuscript`.
- The 60-page long-version target has been reached in page count. Continue improving derivational force and source audit quality in future passes.
- Recently expanded sections: pole-scheme ledger, electroweak assignment theorem target, radical placement ledger, dual-model lineage, expanded Kaluza-Klein interval route, toy boundary operator, endpoint gauge-data and brane-Higgsing dictionary, expanded G2 localization, three-route comparison, expanded negative-branch scalar-functional analysis, theorem-target appendix, flavor boundary, global-form constraints, and status ledger.
- Pending next work: choose one matrix entry in the route comparison and push it toward a derivation from endpoint, interval, or \(G_2\) source data.
- Editorial next work: run `reviews/paper_normalization_plan.md` to turn the reference draft from workshop/scaffolding prose into paper prose.
- Added pending reconstruction issue O10: the canonical full-gauge interpolation is total \(D=11\to D=10\to D=9\), corresponding to internal KK \(7\to6\to5\), from full \(SU(3)\times SU(2)\times U(1)\) through a DeVries six-dimensional interior to \(SU(3)\times U(1)_{\rm em}\). Treat this as source-audit pending; start from `/home/codexssh/phys3/sources/unbroken_susy.md` lines 69--71 and Witten 1981 fragments.
- Also preserve the colourless electroweak count: total \(D=7\to D=6\to D=5\), corresponding to internal KK \(3\to2\to1\), with six-dimensional superstrings as the middle-dimensional source anchor.
- Round 2 converted O10 into a dimensional Schur-complement target: the \(D=10/6\) middle line must provide \(\mathcal B(t_\star)\), \(\mathcal H_J=\operatorname{span}\{h_J,a_J\}\), \(K_J(t_\star,\lambda)\), and the pole-matching rule.
- New O10 subquestion: explain why the top quark sits at the electroweak scale. Source-backed SM facts are top Yukawa dominance, nondecoupling, and top sensitivity in Higgs/vacuum-stability physics; any DeVries explanation remains open.
- New O11 source-note validation issue: preserve `../prTalks` PDFs as source objects, use extracted text only as an access aid, and promote only structural obligations or primary-source-backed claims.
- New O12 parent-workspace validation issue: preserve adjacent text notes as source-note provenance, promote their critique content into O1/O3/O4/O6/O8/O10 obligations, and replace adjacent-project claims with primary sources before manuscript citation.
- Loop 11 normalized the abstract, introduction, VI.G route comparison, and conclusion around the A1--A3/T1--T3 hierarchy.  The active central theorem target is now also recorded as an electroweak mass-map theorem from the Higgs kinetic term and W/Z mass matrix to the ordered DeVries quotient after pole matching.
- Loop 12 adds Appendix D Target 0: a unified source-to-pole matching theorem
  \[
  \mathcal S_r\to\mathcal H_{J,r}\to K^{\rm eff}_{J,r}(\lambda)
  \to \Pi^{(4)}_{T,V}(s;J,r)\to
  \Delta^{-1}_{V,T}(s_V;J,r)=0.
  \]
  The route comparison now requires one reduced field basis, inner product,
  projection/decoupling rule, ordered W/Z sampling map, and pole-matching
  scheme before endpoint, interval, and \(G_2\) routes can be compared.
- Loop 12 also broadens the `..` parent inventory.  Relevant clusters are
  `../prTalks`, `../hans/signed_dbdevries`, `../weak`, `../phys3`, `../phys4`,
  `../physres1`, `../dualsm`, `../signed-dv-custodial-project`, and `../recap`.
  Runtime state, caches, security reviews, and unrelated generated outputs are
  excluded from manuscript claims.
- Loop 13 promotes O5 to Appendix D Target IIa: electroweak ray
  admissibility.  The allowed deformation has one radial gauge-Higgs
  parameter, fixed \(g:g'\), simultaneous W/Z mass collapse, and persistent
  photon null direction.  Coupling-space and custodial-breaking paths are
  separate deformation problems.
- Loop 13 also separates the dimensional-interpolation parameter from the
  electroweak ray parameter.  Future O10 work needs a source map
  \(\chi:t_{\rm dim}\mapsto t_{\rm EW}\) or a joint source variable before the
  dimensional chain can control the electroweak ray.
- Loop 14 targeted the parent workspace.  The source-note import now includes
  Wrong Turn provenance, a Wigner--Eckart failed route result for tested
  natural parents, a three-trace-space separation rule, SO(32) flavor/string
  boundary obligations, and a top-as-boundary-datum caution.  These are
  guardrails and theorem targets until primary sources or derivations promote
  them.
- Keep calculation scripts closed during the conceptual phase. LaTeX compilation remains the verification command.

## Manuscript posture

The manuscript should read as precise physics exposition with one strong motivating observation and a sequence of analytical tests. The authorial voice should keep the speculative status of the dynamical interpretation explicit.
