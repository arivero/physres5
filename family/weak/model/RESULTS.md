# Phase A/B/C/D Results Synthesis

Status: completed 2026-05-16. Paper v4 (PRD submission candidate) at
[paper/main.tex](paper/main.tex), 13 pages.

## Phase A — Robustness scan of seed coefficients (a, b)

**Verdict: FINE-TUNED in the a/b ratio at ~10⁻³.**

- Along `a = b` (10× rescaling: 0.7 → 5.0): predictions unchanged
  (m_0 absorbs the rescaling). This is gauge-trivial, not robustness.
- Orthogonal direction (a/b varied): `d(δm_h/m_h)/d(a/b)|_{(1,1)} = +0.67`.
  A 1% misalignment of a vs b shifts m_h by 0.67%.
- The model's 0.04% accuracy on m_h requires `a/b = 1 ± 6×10⁻⁴`.

**Implication:** the "Casimir lock" is the operational postulate that
the off-diagonal `√C₂` coefficient and the diagonal `−C₂` coefficient
share the SAME prefactor (no symmetry derivation in v4). Phase D
sketches a UV origin where this naturally emerges.

Script: [algebra/robustness.py](algebra/robustness.py)

## Phase B — Scheme dependence of sin²θ_W and bookkeeping fix

**Verdict: model's sin²θ_W = 0.22310 is the on-shell value;
disagreement with MS-bar / effective-leptonic schemes (~3.5%) is
~100× larger than the model's claimed precision.**

- The algebraic prediction matches PDG_OS to 0.1% (1σ).
- It does NOT match MS-bar (0.23121, 3.5% off) or effective-leptonic
  (0.23153, 3.6% off).
- Δr ≈ 4% one-loop EW correction is implicit in the M_W anchor;
  the model inherits but does not predict Δr.
- **Abstract overcount fixed** (per criticism2.md point 2): old wording
  "2 parameters → 4 outputs" was double-counting. Honest count:
  1 parameter-free prediction (M_Z, 0.007%) + 1 fitted + 1 consistency
  check via the cross-irrep negative-branch trace identity.

Script: [algebra/EW_corrections.py](algebra/EW_corrections.py)

## Phase C — 91 GeV scalar phenomenological recast

**Verdict: NOT EXCLUDED. LEP HZ' is the strongest constraint
(λ_dt < 0.012), automatically satisfied by ρ-parameter requirement.**

- Φ^t_+ at 91.19 GeV is gauge-phobic (no direct ZΦΦ vertex) and
  fermion-phobic (Y=0 triplet forbids tree-level Yukawas).
- Production via Higgs portal λ_dt only: σ ∝ sin²θ_mix ≈ 12.6 λ_dt.
- LEP HZ' combined: σ/σ_SM < 0.15 → λ_dt < 0.012 (strongest).
- ATLAS diphoton 65–110 GeV: weaker; allows SM-strength couplings.
- FCC-ee/CEPC at √s = 240 GeV would probe λ_dt ∼ 10⁻⁴.
- **Q4 of Status section now ANSWERED: model survives.**

Script: [phenomenology/recast_91GeV.py](phenomenology/recast_91GeV.py)

## Phase D — Partial-compositeness origin of the a = b lock

**Verdict: a = b emerges naturally if `m_χ² = y|ε| C₂(R)`, i.e., the
composite mass and the elementary-composite mixing share a common
higher-dim operator origin above Λ_HC.**

- UV: SU(N)_HC × global symmetry, with SU(2)_L gauged inside the global.
- Mixing: `y ε^A ψ_R T^A_R χ_R` (adjoint-charged spurion).
- Off-diagonal naturally scales as `y|ε| √C₂(R)` (generator norm).
- Diagonal composite mass `m_χ²` is SU(2)-singlet from HC dynamics.
- Lock condition: `m_χ² = y|ε| C₂(R)` — common-origin requirement.

**Conceptual closing:** the j labels are the SU(2)_L charges of
hypercolor BOUND STATES (composite scalars), structurally analogous to
isospin labels of QCD mesons. Same group theory; different physical
referent. The chat's spin-3/2 dismissal is rescued in this reading: j
is internal SU(2)_L charge of a composite scalar, not Lorentz spin.

Script: [lagrangian/L_PC_sketch.py](lagrangian/L_PC_sketch.py)

## Net effect on paper v4 (PRD submission candidate)

- New §3 paragraph (robustness in (a, b)) — Phase A
- §6 abstract bookkeeping corrected — Phase B
- New §8 (91 GeV scalar phenomenology) — Phase C, **answers Q4**
- New §11 (partial-compositeness sketch) — Phase D
- Q4 in Status updated: ANSWERED
- Acknowledgements added with mandatory generative-AI disclosure
- Title bumped to v4, byline placeholdered for [Author]/[Affiliation]
- Paper now 13 pages (was 11), 6 sections + 5 subsections

## Where the model stands after A/B/C/D

| dimension | before | after |
|---|---|---|
| numerical match | 4 quantities to 0.04% | unchanged (no new fits) |
| robustness | not tested | fine-tuned in a/b at 10⁻³ |
| scheme | "PDG to 10 digits" | on-shell, ~1σ vs PDG_OS |
| 91 GeV viability | open question Q4 | answered: not excluded |
| UV origin | open question Q5 | sketch: PC with common-origin condition |
| publication readiness | v3 draft, 11 pages | v4, 13 pages, ack + AI disclosure |

## What's still open

- **Q1**: derive M_W² = m_0² λ_+(2) from a Higgs-mechanism mass matrix
- **Q2**: derive m_h,bare² = m_0² |λ_-(2)| from scalar-potential minimisation
- **Q3**: scheme-precise sin²θ_W comparison at one-loop
- **Q5**: specific UV completion (choice of N for SU(N)_HC, fermion content)
- **Q6**: dynamical mechanism for the triplet half of the bidirectional Δ
