# Literature search: prior work near the Casimir-locked seesaw

## 1. Methodology

Search engine: InspireHEP `/api/literature` JSON endpoint, queried with
`fields=titles,authors,arxiv_eprints,publication_info,abstracts&size=10-20`.
About twenty distinct queries were issued, covering the six themes in the
task brief: (i) bosonic / Higgs-sector seesaws, (ii) Casimir or
representation-theoretic mass spectra, (iii) doublet+triplet Higgs
sectors and custodial symmetry, (iv) Koide formula derivations from
discrete flavour symmetries, (v) top-quark seesaw, (vi) algebraic 125 GeV
Higgs predictions. Queries that returned zero hits were retried with
broader keywords and with author-only constraints. A handful of likely
candidates were verified individually by arXiv ID (Calmet-Oliver,
Rivero-Gsponer, Rivero composite-bosons, H.D. Kim, Foot, Ma,
Chanowitz-Golden). The final pool is roughly 40 candidate papers; below
they are reduced to the genuinely informative subset.

A caveat: several of the citations in PAPER.md ([2], [3], the
Chanowitz-Golden 1985 work) are preprints or pre-1990 publications, and
the InspireHEP full-text search is weak on those. They were verified by
direct arXiv-ID or author+keyword queries.

## 2. Verified-strong precursors

These are the eight papers that share either the **2x2 scalar mass-squared
matrix with a tachyonic eigenvalue driving EWSB**, or the **Koide-formula
geometric/discrete-symmetry derivation**, and so are genuine intellectual
ancestors of the construction in PAPER.md.

1. **Calmet & Oliver, "A Seesaw Mechanism in the Higgs Sector"**
   arXiv:hep-ph/0606209, EPL 77 (2007) 51002.
   A two-Higgs-doublet 2x2 mass-squared matrix is diagonalized and one
   eigenvalue is driven tachyonic; this is essentially the bosonic-seesaw
   skeleton of our Eq.(1) restricted to the doublet sector and without
   Casimir-locking. Already cited as [6]; the citation is well-placed
   and should be retained.

2. **Kim (Hyung Do), "Electroweak Symmetry Breaking from SUSY Breaking
   with Bosonic See-Saw Mechanism"**
   arXiv:hep-ph/0501059, Phys. Rev. D 72 (2005) 055015.
   Coins the modern term "bosonic see-saw" for a 2x2 scalar
   mass-squared matrix whose negative eigenvalue is the SM Higgs. The
   currently-cited Kim ref [7] *attributes the paper to "J. E. Kim",
   which is incorrect*: the author is Hyung Do Kim. This should be fixed
   in the bibliography.

3. **Chivukula, Dobrescu, Georgi, Hill, "Top Quark Seesaw Theory of
   Electroweak Symmetry Breaking"**
   arXiv:hep-ph/9809470, Phys. Rev. D 59 (1999) 075003.
   2x2 fermion-mass-matrix seesaw whose lighter eigenstate is the top
   quark and which simultaneously drives EWSB through top condensation.
   This is the *fermionic* analogue of our scalar seesaw; the structural
   parallel (2x2 matrix, single seed scale, role-reversal of eigenvalues)
   is direct. Already cited as [8]; well-placed.

4. **Haba et al., "Bosonic seesaw mechanism in a classically conformal
   extension of the Standard Model"**
   arXiv:1508.06828, Phys. Lett. B 754 (2016) 349.
   A modern, well-developed bosonic-seesaw realisation in which
   radiative Coleman-Weinberg dynamics of a U(1)_{B-L} sector
   generates the negative Higgs mass-squared via a 2x2 scalar matrix.
   Our top-loop M4 mechanism (Sec. 4.3) is conceptually identical in
   structure. **Not currently cited; should be added.**

5. **Foot, "A Note on Koide's lepton mass relation"**
   arXiv:hep-ph/9402242 (1994).
   The original geometric reading of the Koide formula as the
   half-angle-45-deg cone condition on the sqrt(m_i)-vector — exactly
   the r=a/sqrt(2) circle we exploit in Sec. 5. Reference [3] of
   PAPER.md (Rivero-Gsponer) cites and reviews Foot; we should cite
   Foot directly as well. **Currently missing; should be added.**

6. **Ma, "Lepton Family Symmetry and Possible Application to the Koide
   Mass Formula"**
   arXiv:hep-ph/0612022, Phys. Lett. B 649 (2007) 287.
   A Z_3-based finite flavour group is shown to produce charged-lepton
   masses proportional to v_i^2 and to be the natural symmetry-theoretic
   substrate of the Koide relation. This is the closest existing
   derivation of our Hermitian Z_3 circulant from a Lagrangian. **Not
   currently cited; should be added as a precursor for Sec. 5.3.**

7. **Koide, "Charged Lepton Mass Matrix With Democratic Family Mixing"**
   Z. Phys. C 45 (1989) 39.
   Earliest derivation by Koide of the Q=2/3 relation from a democratic
   3x3 mass matrix; the matrix is the S_3-symmetric (a,b,b;b,a,b;b,b,a)
   ancestor of our circulant. Useful as the founding reference for
   the Sec. 5 construction; not currently cited.

8. **Chanowitz & Golden, "Higgs Boson Triplets With M(W) = M(Z) cos
   theta_W"**
   Phys. Lett. B 165 (1985) 105. [pre-arXiv; verified on InspireHEP]
   The foundational paper showing that an SU(2)_L triplet with the
   right vev can be added to the doublet without spoiling rho=1 at
   tree level. Our construction puts the triplet into the M_Z slot of
   a Casimir-locked seed — a *different* role — but Chanowitz-Golden
   is the canonical reference for "triplet contributing to electroweak
   gauge-boson masses." Not currently cited; should be added as a
   background-but-essential reference.

## 3. Moderate-overlap neighbors

These share a mechanism or sector but differ in essential details
(usually: same bosonic-seesaw structure but different UV motivation;
or same discrete-symmetry flavour structure but different fitting target).

- **Haba & Yamada, "Electroweak symmetry breaking through bosonic
  seesaw..."** arXiv:1509.01923 — companion paper to 1508.06828.
- **Ishida et al., "Invisible Axion-Like Dark Matter from Electroweak
  Bosonic Seesaw"** arXiv:1601.04934 / 1606.00192 — bosonic seesaw as
  portal to dark-matter sector.
- **Ishida & Matsuzaki, "Bosonic-Seesaw Portal Dark Matter"** (PTEP 2016).
- **Ishida et al., "Scalegenesis via dynamically induced multiple
  seesaws"** arXiv:1701.03306.
- **Haba & Tabata, "A new dynamics of electroweak symmetry breaking
  with classical scale invariance"** arXiv:1502.00679.
- **Hosotani et al., "Gauge-Higgs Seesaw Mechanism in Six-Dimensional
  Grand Unification"** arXiv:1706.03503 — "seesaw" applied to gauge-Higgs
  unification, structurally distinct but lexically the same.
- **Bazzocchi & Frigerio, "A Heavy Higgs from flavor and EWSB
  unification"** arXiv:hep-ph/0407358 — collective breaking with triplet.
- **Koide, "S_4 Flavor Symmetry Embedded in SU(3) and Lepton Masses"**
  arXiv:0705.2275 — alternative discrete-flavour derivation of Q=2/3.
- **Koide, "Charged Lepton Mass Formula: Development and Prospect"**
  arXiv:0706.2534 — review of all Koide-derivation approaches up to 2007.
- **Davis, "An empirical relation between lepton masses from the
  symmetric permutation group"** Mod. Phys. Lett. A 40 (2025) 2450209 —
  recent S_3-based reading of Koide; thematically close to our Sec. 5.

## 4. Background reading

- Koide (1983), "A Fermion-Boson Composite Model of Quarks and Leptons" — original.
- Kartavtsev (2011), arXiv:1111.0480 — Koide extension to quarks.
- Xing & Zhang (2006), arXiv:hep-ph/0602134 — running of Koide ratio.
- Rodejohann & Zhang (2011), arXiv:1101.5525 — Koide for neutrinos.
- Koide (2010), arXiv:1001.4877 — Yukawaon approach to Sumino relation.
- Koide & Sumino (2011), arXiv:1007.4739 — family gauge symmetry tests.
- Perelstein (2005), arXiv:hep-ph/0512128 — Little Higgs review.
- Schmaltz et al. (2008), arXiv:0812.2477 — collective quartics with triplets.
- Kundu (2022), arXiv:2111.14195 — custodial symmetry beyond GM.
- Logan (2015), arXiv:1504.07608 — hVV couplings in GM model.

## 5. Honest assessment of PAPER.md citations

Current bibliography (PAPER.md Sec. 6.4 and references):

- **[1] Rivero, "An interpretation of scalars in SO(32)", arXiv:2407.05397.**
  Verified as published EPJC 84 (2024) 1058. Well-placed; this is the
  literal claim being borrowed (SO(32) parent group). Use as-is.

- **[2] Rivero, "Supersymmetry with composite bosons", arXiv:hep-ph/0512065.**
  Verified as preprint only — no journal publication located. The
  paper itself does not derive the spurion size we use; the citation
  is for the sBootstrap *framework* and is appropriate as a structural
  context, not as a derivation. The paper text already records the
  preprint-only status. Keep.

- **[3] Rivero & Gsponer, "The strange formula of Dr. Koide", arXiv:hep-ph/0505220.**
  Verified as preprint only. This paper is a review of Koide
  including Foot's geometric reading — it is *not* the originator
  of the geometric reading itself. **Recommendation: add Foot
  hep-ph/9402242 as the primary citation for the geometric reading
  used in Sec. 5.2, and keep [3] as a secondary historical review.**

- **[4] Slansky, Phys. Rept. 79 (1981) 1.** Standard, well-placed.

- **[5] PDG 2024.** Standard.

- **[6] Calmet-Oliver, hep-ph/0606209.** Well-placed precursor for the
  bosonic seesaw idea (see entry 1 above). Keep.

- **[7] Kim, hep-ph/0501059.** Author is **Hyung Do Kim**, not
  J. E. Kim. *Fix the author name in the bibliography*. Keep the
  citation; it is the right reference for "bosonic see-saw mechanism".

- **[8] Chivukula-Dobrescu-Georgi-Hill, hep-ph/9809470.** Well-placed.
  Keep.

### What is conspicuously missing

Three additions would meaningfully strengthen the bibliography:

a. **Haba et al. arXiv:1508.06828** — the cleanest modern bosonic-seesaw
   construction in which the small Higgs mass is *generated radiatively*
   (Coleman-Weinberg of a hidden U(1)). This is the closest mechanistic
   analogue to our M4 top-loop spurion, and the connection between the
   scale m_0 and a radiative-EWSB cutoff has been studied carefully
   there. Add to Sec. 4.3 alongside the discussion of M4.

b. **Foot arXiv:hep-ph/9402242** — the original geometric reading of
   Koide as a 45-deg cone, which is the construction we reproduce in
   Sec. 5.2 via the circulant. Currently the geometric reading is
   sourced only through the Rivero-Gsponer review [3].

c. **Ma arXiv:hep-ph/0612022** — the closest existing derivation of a
   Z_3-symmetric Lagrangian producing the Koide relation. Add to
   Sec. 5.3 as the precedent for embedding the Hermitian circulant in
   a discrete-flavour symmetry.

A fourth optional addition is **Chanowitz-Golden Phys. Lett. B 165
(1985) 105** as the canonical reference for "a triplet contributing
to the electroweak gauge-boson mass sector while preserving custodial
SU(2)". Our triplet plays a different role (it provides the M_Z slot
via its Casimir, not via a vev that breaks custodial), so the
Chanowitz-Golden citation needs to come with a one-sentence
disclaimer explaining the difference.

### What is not missing

No paper in the InspireHEP corpus appears to construct a 2x2 scalar
mass-squared matrix whose entries are *fixed by the quadratic Casimir
of the SU(2) representation* with a single seed scale. The
"Casimir-locked" shape of Eq. (1) — both diagonal and off-diagonal
entries scaling with C_2(R) — is not a known construction in the
existing literature. The combination of (i) bosonic seesaw + (ii)
representation-theoretic mass-spectrum locking + (iii) doublet/triplet
selection by minimal-Casimir is, to the precision of this search,
novel. The strongest direct precursors remain the three already cited
([6], [7], [8]) plus the three additions recommended above; there is
no "missing parent paper" that subsumes the whole construction.
