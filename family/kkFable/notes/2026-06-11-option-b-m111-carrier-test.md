# N10 — The rank-4 carrier test: does fixing the gauge sector fix the matter?

Date: 2026-06-11.

**VERDICT: NO — COMPLEMENTARY EXCLUSION. The rank-4 carriers that repair
X_{1,1}'s gauge deficit lose the matter structure X_{1,1} had. On M^{111}
(the literature's fully computed colour-on-CP²-type carrier, Fabbri–Fré et
al.): the gauge sector is exactly SU(3)×SU(2)×U(1)_R (+ a Betti U(1)' under
which every KK state is neutral), but the harmonic lattice admits only
triality-zero colour reps and INTEGER weak isospin — no SU(2) doublet of any
kind at any level, no quark or lepton slots ("could not be found", verbatim),
and colour-singlet matter is pinned to Y = 0; the only massless charged
colour/weak singlets are the two GRAVITINI (y = ±1). On the product S⁵×S²
the charge-locking lemma kills the Higgs slot the same way. Within the
family examined, gauge-rank completeness and doublet/lepton structure are
mutually exclusive: X_{1,1} has the spin^c doublet mechanism and the right
lepton lattice but not the gauge rank; the rank-4 carriers have the gauge
rank but not the doublets. The Higgs-doublet slot fails on EVERY homogeneous
carrier examined — an elementary-scalar no-go that explains structurally why
this programme keeps being pushed toward Higgs-from-connection (CSDR),
composites, or finite/fuzzy modules.**

Conventions: N0. Inputs: N2 §6 and N9 §6 (the repair candidates), N6
(X_{1,1} slot table), sources-local digests (Fabbri–Fré hep-th/9903036;
Dolan–Nash hep-th/0207078/0207007; KK Supergravity 2025).

## 1. The question

N8 resolved the fork negatively for X_{1,1} with three structural absences
(Y boson, Higgs slot, e_R slot) and named the rank-4 carriers — S⁵×S²
(inherited priority rule) and M^{p,q,r} — as the repair path for the first.
This note tests whether that repair also buys back the other two.

## 2. Charge-locking lemma (scalars)

Expansion block.
- Claim: on any coset G/H with SU(3) ⊂ G and a U(1)_Y ⊂ G isometry, a
  SCALAR mode that is an SU(3)-singlet can only carry the Y-charges whose
  character restricts trivially to H. In particular, if every SU(3)-singlet
  irrep of G restricts nontrivially to H except at Y = 0, then charged
  colour-singlet scalars do not exist — for any extra line twist (twisting
  shifts the balance, never creates an H-invariant in a 1-dimensional rep
  with nontrivial H-character).
- Proof: Frobenius — a scalar mode in the G-irrep V occurs iff V contains an
  H-invariant vector; for 1-dimensional V (SU(3)-singlet, Y-charge y), the
  H-invariant exists iff the H-character of V is trivial. ∎
- Application (a), lens factor: S⁵/Z_n = U(3)/(U(2)×Z_n); the SU(3)-singlet
  U(3)-irreps are det^k, and det^k|_{U(2)} = (det A)^k, nontrivial unless
  k = 0. Colour-singlet scalars on the lens factor carry Y = 0. ∎
- Scope (sharpened after adversarial review, 2026-06-11): the "for any
  extra line twist" clause holds for twists by characters trivial on the
  rep in question; on non-simply-connected lens versions (n > 1), torsion
  (flat) twists by the rep's own H-character would re-admit charged
  singlets, and on every carrier the lemma covers scalar FIELDS (W = 1),
  not internal tensor components — the same scoping as N6 Theorem 1. The
  family-wide Higgs conclusion is therefore: no ELEMENTARY scalar-field
  Higgs slot, under the untwisted-or-trivial-character twist policy stated
  here; connection-component (CSDR) scalars are exactly the named escape.
- Application (b), S⁵×S²: the S² factor contributes weak structure only;
  colour-singlet weak-doublet scalars exist there (odd monopole twist on
  S², N9 §6) but ALWAYS at Y = 0 by (a). The SM Higgs slot (1, 2, Y = ±1/2)
  fails on S⁵×S². ∎
- Application (c), M^{111}: the digest's eq. (6.9): scalar harmonics obey
  2J₃ = Y = (2/3)(M₂−M₁); colour singlet (M₁ = M₂ = 0) forces Y = 0.
  Same lemma, realized inside the paper's constraint. ∎
- Status: derived (independent collaborator run on (a)/(b) pending —
  addendum); (c) cited.

## 3. M^{111}: the exact lattice (cited from hep-th/9903036 via digest)

- Coset: M^{pqr} = SU(3)×SU(2)×U(1) / (SU(2)^c × U(1)' × U(1)''), with
  SU(2)^c = the isospin SU(2) inside SU(3) and the two H-circles given by
  eqs. (4.9)–(4.10); the spectrum is computed at p = q = r = 1 and "does not
  depend on the actual value of p = q or of r ≠ 0".
- Gauge sector (eq. 3.44): massless vectors of SU(3)×SU(2)×U(1)_R — rank 4,
  the U(1)_R graviphoton being the isometry circle — PLUS the Betti
  multiplet U(1)' from A_{μij} on the closed 2-form, with the verbatim
  statement "All Kaluza Klein states are neutral under U(1)'". This is the
  literature anchor that retroactively grounds N2 §5's charged-matter kill
  (there stated as a named rule; here computed in the closest relevant
  model).
- Global selection rule (eq. 3.1): only M₂−M₁ ∈ 3Z (triality zero) and
  J ∈ N occur. Consequences:
  - **No SU(2) doublet — coloured or not — anywhere in the KK spectrum.**
    The doublet-enabling mechanism of X_{1,1} (the parity law tying odd
    line-bundle charge to half-integer fibre isospin, N2 §3) has no M^{111}
    analogue; its H contains SU(2)^c and two circles that lock J to
    integers.
  - **No quark slots** (no triality-1 reps at all) and **no lepton slots**;
    the paper's own verdict: "the quark and lepton representations could not
    be found in the hypermultiplet spectrum".
  - Hypermultiplets (the only spin-1/2 matter) sit at (M₂, M₁) = (3k, 0),
    J = k, y₀ = 2k — coloured, integer isospin.
- Charge lock (eq. 5.13): Y = (2/3)(M₂−M₁) plus fixed shifts (∓2 bosonic,
  ∓1 fermionic). Colour-singlet multiplets have y₀ = 0; the charged members
  inside them are heavy (long multiplets, lightest at E₀ = 4) — EXCEPT the
  two massless gravitini at y = ±1.

## 4. The gravitino resonance

N6 §7 recorded, as a loophole on X_{1,1}, that an e_R-like slot
(colour-singlet, weak-singlet, |Y| = 1) exists in the gravitino
(Rarita–Schwinger) sector of an 11D-type embedding. On M^{111} this is not a
loophole but the computed spectrum: **the only massless charged
colour/weak-singlet states of the compactification are the two N = 2
gravitini at y = ±1.** Across both carriers, the e_R quantum numbers
persistently surface in the gravitino sector and nowhere else. Recorded as a
cross-carrier pattern (comparison status): if this family has an electron at
all, it is gravitino-borne — a sharp, falsifiable structural hint, with the
obvious objection (a gravitino is not an electron; supersymmetry breaking
and a spin-changing mechanism would have to intervene) stated alongside.

## 5. S⁵×S² (the inherited priority carrier)

- Gauge sector: (U(3)/Z_n)×SO(3) for the lens versions — rank 4: colour +
  Y + weak (N9 §6). The gauge repair works.
- Scalars: weak doublets exist (odd S² monopole twists) but only at Y = 0
  (§2b); Higgs slot fails.
- Fermions (verified, checks C Q3 and D — addendum): the lens-factor spinor
  bundle (Δ₅ = 1_{−1} ⊕ 2_0 ⊕ 1_{+1} under U(2)) admits colour-triplet
  fermion modes only at Hopf charges c ∈ {−1/2, +5/2} (+ conjugates) and
  colour-singlet fermion modes only at c = ±3/2. Fixing the normalization
  on Q_L (Y = −c/3) the slot table is: **Q_L ✓ (c = −1/2 → 1/6) and
  L ✓ (c = +3/2 → −1/2); u_R, d_R, ν_R, e_R all FAIL** (would need
  c = −2, +1, 0, +3, none allowed — ν_R fails because colour-singlet
  fermions cannot sit at c = 0 at all). Scope: Dirac sector with line
  twists, as elsewhere. Two of seven SM slots — strictly worse than
  X_{1,1}'s five of seven, despite the complete gauge sector.

## 6. Complementary exclusion (synthesis)

| Carrier | gauge rank 4? | weak doublets? | lepton L lattice? | e_R slot? | Higgs slot? |
|---|---|---|---|---|---|
| X_{1,1} (D7) | no (3) | yes (odd-twist spin^c) | yes (Y = ∓1/2 exact) | no (Dirac sector) | no |
| Y_6 (D6) | no (2) | flux label only | flux label only | no | no |
| M_5(n) (D5) | no (3) | absent | absent | (addendum) | no |
| S⁵×S² | **yes** | yes (S² freedom; scalars at Y = 0 only) | L lands (c = 3/2); ν_R fails | no (and u_R, d_R fail too) | no |
| M^{111} | **yes** (+ neutral Betti U(1)') | **none at any level** | none | gravitini only | no |

Two readings:
1. **Complementary exclusion.** In every examined member of the
   colour-on-CP²-side family, gauge-rank completeness and the
   doublet/lepton matter mechanism exclude each other. X_{1,1} is the
   matter-best, gauge-deficient extreme; M^{111} is the gauge-complete,
   matter-empty extreme. No member does both.
2. **The Higgs no-go column.** The Higgs slot fails everywhere, by the
   locking lemma or stronger lattice rules. Within this family the SM Higgs
   cannot be an elementary scalar harmonic; it must come from connection
   components (the CSDR route the prior repo's Electroweak notes develop),
   from composites (N4 §6/N6 §7), or from finite/fuzzy internal modules
   (Dolan–Nash's own closing speculation). This converts a scattered
   observation of the prior corpus into a per-carrier-proved pattern.

The Dolan–Nash contrast completes the picture (digest, hep-th/0207078):
their celebrated SM spectrum from CP²×CP³ — including e_R at the q = −3
canonical spin^c twist — gauges the HOLONOMY groups and never the isometry;
their CP² isometry SU(3) is floated only as a generation symmetry. The
literature's one working SM-from-CP² spectrum is therefore Option-A-shaped
(electroweak from the U(2) side of CP²), and its colour lives on a separate
factor. Option B's failures here and the holonomy route's success are two
faces of the same fact: the CP² isometry SU(3) is the wrong home for colour
if leptons and the Higgs are to be colour-blind.

## 7. Counterargument pass

1. *"Other (p,q,r) might admit doublets."* The computed spectrum covers
   p = q, r ≠ 0 (paper's statement of independence). For p ≠ q the space
   loses all supersymmetry and the harmonic analysis changes; no
   computation exists showing doublets appear, and the H-embedding still
   contains SU(2)^c plus two circles. Recorded as unproven possibility, not
   a repair. (A first-principles general-(p,q,r) lattice derivation is a
   well-posed future task; an earlier attempt in this session to shortcut
   it through an (S⁵×S³)/U(1) model FAILED against the computed M^{111}
   lattice — that model describes a different space and admits coloured
   doublets M^{111} forbids; discarded, recorded here as a warning.)
2. *"AdS-scale 'heavy' is a vacuum artifact; the charged long-multiplet
   members might become light elsewhere."* Possible in principle, but then
   nothing remains of the computed spectrum as evidence either way; the
   slot STRUCTURE (which (rep, J, Y) occur at all) is the
   vacuum-independent content, and it already excludes doublets and quark/
   lepton reps.
3. *"The exclusion table mixes Dirac-sector statements (X_{1,1}) with full
   supergravity spectra (M^{111})."* True, and deliberate: each row uses
   the strongest available analysis for that carrier; the Higgs column is
   proved by the same scalar lemma in all rows, and the doublet column by
   per-carrier exact selection rules. The fermionic rows are labelled where
   sector-dependent.

## 8. Kill criteria

- A computed M^{pqr} (p ≠ q) or other rank-4 homogeneous spectrum
  exhibiting an SU(2) doublet or a charged colour-singlet matter slot would
  break the complementary-exclusion reading (and would instantly become the
  programme's preferred carrier — the criterion is constructive).
- A colour-singlet charged scalar on any carrier here (contradicts §2).
- For the gravitino pattern (§4): a non-gravitino massless (1,1)_{Y≠0}
  state anywhere in the family.

## Addendum — collaborator verdicts (checks C and D, completed 2026-06-12)

First launches died silently on 2026-06-11; relaunched with captured
output, both completed (GPT-5.5, codex exec, neutral prompts). The
original check D Q3 — posed on the (S⁵×S³)/U(1) model §7.1 discards — was
dropped from the relaunch entirely.
- **Locking lemma (D Q1) — CONFIRM.** det^k|_{U(2)} = 1_{2k}, nontrivial
  unless k = 0: colour-singlet scalars carry zero Hopf charge; the S²
  factor adds weak isospin but never hypercharge; Higgs-like scalar killed
  on (S⁵/Z_n)×S² for any monopole twist.
- **Fermion lattice (C Q3 + D Q2) — CONFIRM, with the slot table of §5:**
  colour-triplets at c ∈ {−1/2, +5/2} (+conj.), colour-singlets at
  c = ±3/2 only; with Y = −c/3 fixed by Q_L: Q_L and L land, u_R, d_R,
  ν_R, e_R fail. The complementary-exclusion verdict of §6 is therefore
  fully verified on the product carrier: gauge rank 4, matter 2/7.

## Sources

- sources-local/FabbriFre_M111_Spectrum_hep-th_9903036.md (digest; eqs.
  1.3, 3.1, 3.44, 4.2, 4.9–4.11, 5.13, 5.14, 6.9; verbatim negatives).
- sources-local/DolanNash_SM_Fermions_From_CPN_hep-th_0207078.md and
  DolanNash_Spinc_Matrix_hep-th_0207007.md (digests; holonomy-not-isometry;
  e_R at q = −3; no Higgs construction).
- sources-local/KK_Supergravity_2025_arXiv_2502.07710.md (chirality no-go
  reaffirmed; singular-G₂ escape).
- N2 §5–6, N6, N9 (internal inputs).
