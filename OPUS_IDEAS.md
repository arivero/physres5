# Innovations for Opus

Proposed by a Fable subagent review of this repo on 2026-07-01.

## 1. Scheme-safe electroweak comparison pipeline with uncertainty propagation and coincidence statistics

The repo's entire numerical layer is `calculations/devries_spectrum.py` (about 50 lines of seed arithmetic) plus `data/pdg_ew_inputs.yaml`, which is explicitly flagged as "project seeds... update from current electroweak source before final manuscript." Meanwhile `calculations/electroweak_pole_scheme.md` lists five unimplemented work items — Breit-Wigner-to-complex-pole conversion, uncertainty propagation from M_Z/M_W/widths with correlations, and separation of sin²θ_pole from MS-bar and effective angles — and Appendix D defines the matching remainder Δ_match that the manuscript never actually computes with errors. Opus would build a `calculations/pole_comparison.py` module that performs the pole-scheme conversions (the ~34 MeV Z-mass shift matters at the claimed 10⁻⁴ precision), propagates PDG uncertainties to a σ-level statement of Δ_match, and adds a look-elsewhere scan over alternative (J_W, J_Z) spin assignments to quantify how special the (3/4, 2) coincidence is — feeding source-audited numbers directly into Sec. 3 and Appendix B with tests under `calculations/tests/`.

**Size:** medium

## 2. Promote the pseudo-Lean research memory to a compiling Lean 4 / mathlib project

The 19 files in `notes/lean/` are stated to "sit outside any Lean project and stay outside compilation": they use Lean 3 syntax (`constant`) and every proposition is a `True` placeholder, so the dependency ledger they encode is unchecked prose in disguise. The exact algebraic layer of the paper is fully formalizable: the secular equation x² + Jx − J = 0, root sum/product identities, the branch-scaling involution x ↦ −J/x (Loop 22's Target IX guardrail), the rank-and-ray admissibility theorem (Loop 13), and the equivalence between the kernel entry conditions Σ_hh=0, Σ_aa=J, Σ_ha·Σ_ah=J and the two-channel operator Q(J) from `D_theorem_targets.tex`. Opus would scaffold a real Lake/mathlib project, prove the exact statements, and encode each open physics obligation as a named hypothesis structure — making the theorem-target ledger in Appendix D machine-checked for logical dependencies and giving the "trigger expert review" purpose of these notes actual teeth.

**Size:** medium-large

## 3. Mechanize the CHM interval-route kernel derivation and test the entry condition Σ_aa,J = J

`reviews/pending_future_work.md` names Loop 27's CHM current-entry extraction as "the immediate source-theory problem": derive K_J^cur = ⟨a_J, (K^DtN + K^brane − K^ref) a_J⟩ from interval gauge-Higgs boundary data and check whether it reproduces the required kernel entry Σ_aa,J = J, with the pipeline (v₀, v_L, R₀, θ_H) → boundary kernels → K_J^eaten(λ) → Π_T(s;J) spelled out in the Loop 21 target. This is the single derivation step the whole 56-loop referee cycle keeps circling, and it is mechanizable: Opus would implement the 5D interval mode decomposition, Dirichlet-to-Neumann operator, photon zero-mode projection, and ordered W/Z boundary map in SymPy, then symbolically/numerically test the three entry conditions and extract the derived pole remainder Δ_match^(interval). Either outcome is publishable progress by the project's own standard ("each substantial pass should end with one physics result"): a derived entry condition partially closes the pole-placement theorem target, and a clean failure gets recorded as a route falsification in the Sec. 6g comparison ledger.

**Size:** large
