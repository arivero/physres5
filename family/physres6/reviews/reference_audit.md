# Reference Audit — physres6 Letter

**Manuscript:** `/home/codexssh/physres6/manuscript/main.tex`
**Bibliography:** `/home/codexssh/physres6/manuscript/references.bib`
**PDFs:** `/home/codexssh/physres6/references/pdfs/`
**Date:** 2026-05-22

Method: read the Letter to extract each citation's role, then read the abstract and
relevant sections of each cited PDF and compared. Verdicts: **OK** (PDF supports the
claim), **WEAK** (partial / loosely attributed support), **MISATTRIBUTED** (PDF does
not support the claim, or wrong document).

---

## Per-reference verdicts

### Rivero2006 — `01_..._hep-ph-0606171.pdf` — **OK**
Cited as the origin of the construction (de Vries–Rivero weak-angle observation; fitting
M_Z also "hints" the EW vacuum).
- Abstract: "It took a long time to us to realize than when the formulae were adjusted to
  the mass of Z^0 then the value of the electroweak vacuum was also hinted." — matches
  the "hints the EW vacuum" wording exactly.
- p.2: s_dV^2 = 1 − m^2_{1/2,+}/m^2_{1,+} = 0.22310132, "unexpectedly near of the mass
  shell Weinberg angle"; using M_Z as input returns W, top-scale and vacuum eigenvalues;
  and "a tree level estimate of the fine structure constant, getting α^{-1} = 135.28."
- This is precisely the construction the Letter extends. Fully supports.

### WittenKK1981 — `witten1981.pdf` — **OK** (all three sub-claims verbatim)
(a) *Gauge couplings ~ power of 1/(M_p R).* p.425: "the gauge coupling constants, which
are determined by integrating the action over the compact dimensions, would scale as a
rather high power of 1/(M_p R), where M_p is the Planck mass and R is the radius of the
extra dimensions." — verbatim.
(b) *Radius an undetermined modulus / massless scalar.* p.424–425: "there is a massless
scalar ... because the classical field equations do not determine the radius of the
circle. Space-time dependent fluctuations of this radius would be observed as a massless
scalar degree of freedom." — verbatim.
(c) *D=11 / 7-internal-dim chiral-fermion no-go.* Abstract: "It is possible to obtain an
SU(3)×SU(2)×U(1) gauge group, but the proper fermion quantum numbers are difficult to
achieve." p.416 derives 4+7=11 as the minimum total dimension for the SM gauge group.
All three uses are accurately attributed.

### PDG2025 — `32_PDG2025_Physical_Constants.pdf` — **OK**
Cited for M_W, M_Z, M_h, m_t, v, 1/α(0)=137.036, 1/α(M_Z), and the weak-angle scheme
definitions.
- Table 1.1 (Revised Sept. 2025): m_W = 80.3692(133) GeV, m_Z = 91.1880(20) GeV,
  α^{-1} = 137.035999177 (footnote: world average 137.035999178(8)), and footnote giving
  α^{-1}(M_Z) ~ 1/128 at Q^2 = m_W^2. sin^2θ(MSbar) = 0.23121; the effective-angle
  footnote gives s^2_eff = 0.23154. Fermi constant G_F listed (→ v via standard relation).
- The Letter's quoted on-shell numbers (M_W=80.369, M_Z=91.188) match the pole-mass values
  (Breit-Wigner minus ~34/27 MeV) consistent with PDG. Supports.

### MartinRobertson2025 — `34_..._1907.02500.pdf` — **OK**
Cited for the scheme distinctions of the weak mixing angle (effective vs MSbar; vs
on-shell/pole).
- "Standard Model parameters in the tadpole-free pure MSbar scheme." Abstract and §I make
  the MSbar-vs-on-shell distinction central; the code "also computes the weak mixing angle
  as defined by the PDG/RPP" (the effective scheme) as distinct from its own MSbar
  quantities. The load-bearing claim (distinct scheme definitions exist and differ) is
  firmly supported. The exact decimals (effective 0.23155, MSbar 0.23129) are SMDR outputs
  consistent with this paper's framework; the scheme taxonomy is the cited point and is OK.
- Bibliographic note: bib year is 2025 (v5 is 23 Jul 2025); original arXiv is 2019. Not a
  content problem.

### Bucci2004 — `40_..._hep-ph-0403012.pdf` — **OK**
Cited for EWSB linked to radion stabilization.
- Title: "Electroweak symmetry breaking and radion stabilization in universal extra
  dimensions." Abstract/intro: the radion is "the scalar excitation of the
  extra-dimensional metric tensor whose vacuum expectation value fixes the size of extra
  dimensions"; electroweak breaking driven by condensation of the higher-dimensional Higgs
  scalar, with radion and Higgs effective potentials tied together. Directly on point.

### HabaOda2011 — `41_..._1102.1970.pdf` — **OK**
Cited for a Higgs identified as the radion stabilizer.
- Title: "Dirichlet Higgs as radion stabilizer in warped compactification." Abstract: shows
  the Goldberger–Wise (radion-stabilizing) scalar can be played by a bulk Higgs — "SU(2)_R
  triplet Higgs ... can be identified with the Goldberger–Wise scalar." Exactly the claim.

### Hosotani1983 — `45_..._PLB126_1983.pdf` — **OK**
Cited for gauge-Higgs unification: the order parameter is a component of the
higher-dimensional gauge field, potential fixed by compactification.
- "Dynamical Mass Generation by Compact Extra Dimensions." This is the Hosotani-mechanism
  paper: the order parameter is the extra-dimensional gauge-field component A_y (Wilson
  line) acquiring a VEV ⟨A_y⟩≠0; the one-loop effective potential V_eff (eq. 6) is fixed by
  the compactification (it depends on the circumference β). "SU(2) symmetry breaks down to
  U(1) without the scalar fields developing non-vanishing expectation value." Squarely
  supports the gauge-Higgs-unification clause.

### SalamStrathdee1982 — `44_..._IC-81-211.pdf` — **WEAK**
Cited (paired with Hosotani) for gauge-Higgs unification, "the order parameter is a
component of the higher-dimensional gauge field with its potential fixed by the
compactification."
- "On Kaluza–Klein Theory." The PDF is solid *general* Kaluza–Klein grounding: harmonic /
  normal-mode expansions on quotient spaces G/H, spontaneous compactification, and the
  resulting massive multiplets — and is in fact a natural support for the Letter's
  Laplacian-eigenvalue / harmonic structure (the J=s(s+1) machinery). However, it is NOT a
  gauge-Higgs-unification paper: it does not establish the specific claim that the order
  parameter is a gauge-field component with a compactification-fixed potential. That claim
  is carried by Hosotani alone. The Salam–Strathdee citation is appropriate as general KK
  grounding but loosely attributed for the gauge-Higgs clause it is attached to. Recommend
  either moving it to a general-KK sentence or pairing the gauge-Higgs clause with a true
  GHU reference (e.g. Manton 1979, Hosotani, or the Csaki–Hubisz–Meade TASI lectures
  already in the folder, `09_...hep-ph-0510275`).
- Minor bib note: entry lists Annals Phys. 141, 316; report number IC/81/211 matches the
  PDF.

### DuffNilssonPope1986 — `10_..._2502.07710.pdf` — **OK** (content), with a bib mismatch
Cited for KK supergravity, the BF bound, and squashed-sphere instabilities (negative-mass
modes).
- The PDF on hand is "Kaluza-Klein Supergravity 2025" (Duff, Nilsson, Pope; arXiv
  2502.07710), a retrospective. It covers exactly the cited material: squashed S^7
  compactifications, "Squashing, Higgs and space invaders" (§5), "The criterion for vacuum
  stability" (§6), and states the BF bound explicitly: scalar fields in 4d AdS are stable
  even when "(mass)^2 is negative, provided that it is not too negative ... M^2 ≥ −m^2 ...
  the so-called Breitenlohner–Freedman (BF) bound." Supports the negative-mass / squashed
  instability claim.
- **Bibliographic mismatch:** the .bib entry `DuffNilssonPope1986` points to the classic
  Phys. Rept. 130 (1986); the file actually present is the 2025 paper. Same authors,
  overlapping content, claim supported by the file on hand — but the bib metadata and the
  PDF describe different documents. Either update the entry to the 1986 Phys. Rept. (and
  obtain that PDF) or re-key the 2025 paper. Verdict OK on the *claim*, flagged on the
  metadata.

### BreitenlohnerFreedman1982 — `46_..._AnnPhys144_1982.pdf` — **OK**
Cited for the BF bound (m^2<0 admissible in AdS above the bound).
- "Stability in Gauged Extended Supergravity," Annals Phys. 144, 249 (1982) — the original
  BF paper. Abstract: gauged extended supergravities have "scalar field potentials which
  are unbounded below. Nevertheless ... ground states with anti-de Sitter background
  geometry which are stable against fluctuations." This is the canonical source for "m^2<0
  is admissible in AdS above the bound." Exactly correct.

### Jegerlehner — `43_..._0807.4206.pdf` — **OK** (content); bib key mislabeled
Cited (as `\cite{Jegerlehner2019}`) for running α(E), hadronic vacuum polarization, the
IR/low-scale value.
- "The running fine structure constant α(E) via the Adler function." Abstract/§1: hadronic
  vacuum polarization controls effective α(E); "α(E) above 1 GeV is a factor of 10 less
  well known than ... α(M_Z)"; the 1.4–2.4 GeV region is "the most problematic." Directly
  supports the Letter's statement that the hadronic / few-GeV region carries the
  vacuum-polarization uncertainty.
- **Bib note:** the key is `Jegerlehner2019` and the in-text macro is `\cite{Jegerlehner2019}`,
  but the entry (and PDF) is arXiv 0807.4206, year 2008. The key name is misleading though
  the citation resolves to the correct paper. Cosmetic; consider renaming the key or
  confirming the intended Jegerlehner reference.

### Biekotter2023 — `42_..._2306.03889.pdf` — **OK**
Cited for the ~95.4 GeV diphoton excess (a neutral γγ feature).
- "The 95.4 GeV di-photon excess at ATLAS and CMS." Abstract: ATLAS+CMS combined γγ excess
  at m_φ = 95.4 GeV, signal strength μ_γγ = 0.24, interpreted as the lightest Higgs (a
  neutral scalar) in an S2HDM. Confirms the Letter's "neutral and spin-0" γγ feature.

---

## Summary table

| Reference | File | Verdict |
|---|---|---|
| Rivero2006 | 01_...0606171 | OK |
| WittenKK1981 | witten1981 | OK |
| PDG2025 | 32_... | OK |
| MartinRobertson2025 | 34_... | OK |
| Bucci2004 | 40_...0403012 | OK |
| HabaOda2011 | 41_...1102.1970 | OK |
| Hosotani1983 | 45_...PLB126 | OK |
| SalamStrathdee1982 | 44_...IC-81-211 | WEAK |
| DuffNilssonPope1986 | 10_...2502.07710 | OK (bib points to wrong document) |
| BreitenlohnerFreedman1982 | 46_...AnnPhys144 | OK |
| Jegerlehner | 43_...0807.4206 | OK (bib key mislabeled "2019") |
| Biekotter2023 | 42_...2306.03889 | OK |

No outright misattributions of physics content. One WEAK (Salam–Strathdee attached to a
gauge-Higgs-unification clause it doesn't establish) and two bibliographic-metadata flags
(DuffNilssonPope key vs. the 2025 file actually present; Jegerlehner key year).

---

## IR-string / Regge / duality themes — coverage gap

The Letter explicitly (a) places α at a ~1 GeV (hadronic) scale, (b) reads the spectrum as
a Chew–Frautschi / Regge plot with common-slope trajectories
M^2 = μ^2 x_±(j(j+1)) + N_osc/α' (Fig. 2 caption and Discussion), and (c) calls these
"the string (Regge) excitations of the same ten-dimensional compactification."

What the cited PDFs actually contain on these themes:

- **String/Regge as an infrared/hadronic theory (1968–71 dual-resonance origin,
  α' ~ (1 GeV)^{-2}).** NOT covered by any cited reference. The closest touch is
  Rivero2006, which mentions "preservation of the string tension (from the asymptotic Regge
  trajectory)" and the high-spin Regge limit, but it does not develop the dual-resonance /
  hadronic-string identification. Witten1981 mentions the modern (Scherk–Schwarz, Cremmer–
  Scherk) "dual models" revival only in passing, in the *Planck-scale* gravitational
  context — the opposite (UV) regime from the Letter's IR/hadronic α'. No reference
  establishes the original dual-resonance-model viewpoint or α' ~ (1 GeV)^{-2}.

- **Any duality (s–t / open–closed / UV–IR / strong–weak).** NOT covered among the *cited*
  set. (The folder contains uncited string-duality papers — Strominger hep-th/9504047,
  Sen hep-th/9504027, Witten hep-th/9511030 — but these treat *modern* string–string and
  small-instanton dualities at the fundamental-string scale, not the s–t channel duality of
  the dual resonance model nor a UV/IR or strong–weak duality relevant to placing α in the
  hadronic IR. None is cited in the Letter, and none addresses the 1968-era duality the
  Regge framing invokes.)

The cited set is essentially all modern KK / electroweak / supergravity. The
IR-string and duality themes that the Letter leans on rhetorically (Regge trajectories,
α' at the hadronic scale, Chew–Frautschi reading) have **no supporting reference**.

### References that would be needed
- **Veneziano 1968** ("Construction of a crossing-symmetric, Regge-behaved amplitude...",
  Nuovo Cim. A57, 190) — the founding dual-resonance amplitude, embodying s–t channel
  (DHS) duality and Regge behavior.
- A **dual-resonance-model / early-string review** establishing the hadronic origin and
  α' ~ (1 GeV)^{-2}, e.g. Fubini–Veneziano, or the Scherk 1975 review, or
  Di Vecchia's "The birth of string theory," or Veneziano's historical reviews.
- A **Chew–Frautschi / Regge-trajectory** primary source for the M^2-vs-spin linear
  trajectory reading used in Fig. 2 (e.g. Chew–Frautschi 1961, or a Regge-phenomenology
  review; Collins, "An Introduction to Regge Theory").
- For the **duality** claim specifically (if the Letter intends to invoke s–t or UV/IR or
  open–closed duality), a dedicated source: the dual-resonance s–t duality (Veneziano /
  Dolen–Horn–Schmid), or a modern open–closed / holographic-QCD duality reference if the
  intent is a hadronic-string–gauge correspondence at ~1 GeV.

Without at least the first two, the Regge/IR-string framing in the abstract, Discussion,
and Fig. 2 is currently unsupported by the bibliography.
