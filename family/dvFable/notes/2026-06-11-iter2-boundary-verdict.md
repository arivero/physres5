# Iteration 2 verdict: can the iteration-1 boundary (B1+B2) be derived?

**Verdict: UNFORCED-WITH-BOUNDARY (second strike) ⇒ candidate (d) RETIRED
under the two-strike rule. The boundary is now a single dimensionless
closure: g²/α = 1, equivalently Σ_j(0) = μ² channel-universally — a
dynamical normalization no symmetry, analyticity, or self-consistency
principle examined supplies.**

Question as registered (`notes/LOG.md`, iteration 2): derive B1 (induced
gap/no-CDD: μ²H_QQ = H_QP H_PQ ⇔ residue R = μ²·ν₀) and B2 (unsubtracted,
single vertex) from a defined non-ad-hoc principle, or show each route
fails or smuggles.

Arms: codex GPT-5.5 adversary (`loop/OUT-codex-iter2.txt`) and codex
GPT-5.5 constructor (`loop/OUT-codex-iter2-constructor.txt`). Protocol
note: the Claude constructor arm failed three times on infrastructure
(2× API-529 overload, 1× session token limit), so iteration 2 is
single-family (GPT-5.5 in both seats). Mitigations, recorded: (i) the
roles were truly adversarial and the runs independent; (ii) every
algebraic claim is re-verified by the Claude side in
`calc/iter2_boundary_checks.py`; (iii) the iteration-1 Fable-5 adversary
(§1.5 of `loop/OUT-claude-iter1.md`) had already reached the same
characterization of the boundary cross-family (CDD ambiguity; KSRF a = 2
dynamical; compositeness not symmetry-derivable). The constructor-retry
prompts disclosed the homogeneity and KSRF-I/II hazards (a bar-raise: any
FORCED claim had to beat the named obstructions); the constructor returned
UNFORCED anyway.

## Route verdicts (cross-consistent, verified)

1. **KSRF-class saturation — SMUGGLES.** HLS bookkeeping
   (m_ρ² = a g²F², g_ρππ = (a/2)g, g_ρ = a g F²): KSRF I
   (g_ρ = 2F²g_ρππ) is an identity for every a — the all-loop Ward
   low-energy theorem (Harada–Kugo–Yamawaki). KSRF II
   (m_ρ² = 2F²g_ρππ²) forces a = 2: one-pole saturation/vector dominance,
   a dynamical input. A finite SU(2)₂ zero-mode sector supplies "one
   retained basis state", not "the spectral function is exhausted with no
   CDD/contact term": truncation-as-saturation is the smuggle.
   [verified: calc §1]
2. **No-CDD as a theorem — FAILS.** Explicit counterexample:
   Σ = γ²μ⁴C/(B + m₀² + λμ²C) is positive, unsubtracted, causal, and
   violates B1 for m₀ ≠ 0 (matching as an identity in C forces δ = 0,
   λ = γ²). An intrinsic closed-channel gap is consistent with every
   kinematic requirement: no-CDD is a choice. The constructor adds: even
   granting no-CDD, the residue is controlled by the derivative of the
   channel loop function at the pole, not universally by R = μ²ν₀.
   [verified: calc §2]
3. **Bootstrap / mutual induction — FAILS (degenerate).** The closure
   H_QQ = w·H_QP K_P(0)⁻¹ H_PQ reduces to hs = (w−1)g²: at w = 1, s = 0
   every gap normalization h > 0 is a fixed point (the closure is
   homogeneous); h = 1 must be inserted. The constructor's sharper form:
   using "closed gap induced by the same portal" to set the normalization
   IS B1 itself — circular. [verified: calc §3]

No standard unitarity/causality/analyticity/asymptotics theorem ties a
single-pole residue to its pole position; that tie is the CDD ambiguity,
and removing it is a dynamics, not a kinematic consequence.

## The retired boundary, stated in its cleanest forms (equivalent)

- Hamiltonian: μ²H_QQ = H_QP H_PQ on Im A_j, with portal H_PQ = μ²A†.
- Spectral: R_j = μ²·ν_j (residue = scale × position), every channel.
- Static: **Σ_j(0) = μ² for all j** — the static self-energy is
  channel-blind; the Casimir enters only the dispersion. [verified: calc §4]
- Dimensionless: g²/α = 1 — one number, the same number in every route.

Minor defect, flagged: the constructor's Sugawara-control section drifted
into WZW central-charge bookkeeping (c = 3k/(k+2), h_j = C_j/(k+2)); the
control's substance is intact (the L0 weighting gives h_j = C_j/4 at
k = 2, the recorded failed value), and the adversary ran the control
cleanly (any valid principle carries C → c²C; nothing rescues 0.3014).

## Consequence for the ledger

- Candidate (d) RETIRED (two strikes: gauge invariance — iteration 1;
  spectral/self-consistency principles — iteration 2). Boundary recorded
  above; per the CORRECTION rule it is a signpost: the closure must come
  from a dynamics with MORE structure than symmetry + spectral
  consistency. The named survivor with that structure in this program is
  the forced geometry itself (single higher-D trace) → new candidate (h),
  iteration 3.
- Candidate (b) (HS/large-N potential origin) dies by inheritance: any
  defined Hubbard–Stratonovich construction carries its four-fermion
  coupling G into the saddle equation as X = GC/(X+C)-type, i.e. the same
  free closure (the identity is iteration 1's X² + CX − r²C family,
  `calc/iter1_adversary_checks.py` check 4, with r² = G). No dedicated
  iteration spent.
