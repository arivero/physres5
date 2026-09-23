# KK Evidence Memo

## Scope

This memo records what the classical KK sources currently prove or constrain. It is not a derivation of the de Vries operator. It is the evidence layer for deciding what the `D=9 -> D=10 -> D=11` structure is allowed to be.

## Sources Actually Inspected

The PDFs are scanned, so the first pass used page-image inspection rather than full OCR.

| Source | Local file | Inspected pages | Evidence extracted |
|---|---|---:|---|
| R. Coquereaux and A. Jadczyk, "Harmonic expansion and dimensional reduction in G/H Kaluza-Klein theories," CERN-TH-4023/84, Class. Quantum Grav. 3 (1986) 29-42. | [coquereaux-jadczyk-1986-harmonic-expansion-gh-kk.pdf](references/classical-kk-1980s/coquereaux-jadczyk-1986-harmonic-expansion-gh-kk.pdf) | 1-4 | Generalized Peter-Weyl/Frobenius harmonic expansion for matter fields, tensor/spinor reduction, Laplace and Dirac operators, and the `N(H)/H` gauge issue. |
| A. Jadczyk, "On the effective gauge group from G/H spontaneous compactification," CERN-TH-4332/85. | [jadczyk-1985-effective-gauge-group-gh.pdf](references/classical-kk-1980s/jadczyk-1985-effective-gauge-group-gh.pdf) | 1-4 | Two reduction schemes: a `G`-invariant scheme with `N(H)/H` gauge bosons, and a non-`G`-invariant scheme with a larger local effective group involving `N(H)/H` and `Aut G`. Also confirms non-unique truncation. |
| R. D'Auria and P. Fre, "On the spectrum of the N=2 SU(3) x SU(2) x U(1) gauge theory from D=11 supergravity," CERN-TH-3861, Class. Quantum Grav. 1 (1984) 447-468. | [dauria-fre-1984-spectrum-su3-su2-u1-d11.pdf](references/classical-kk-1980s/dauria-fre-1984-spectrum-su3-su2-u1-d11.pdf) | 1-4 | D=11 Freund-Rubin compactification with `SU(3) x SU(2) x U(1)` and `N=2`, spectra on `M^{pqr}` spaces, an extra `U(1)` vector multiplet from `B_2=1`, and explicit warning that full towers/multiplets matter. |
| M. J. Duff, "Modern Kaluza-Klein Theories," Imperial/TP/83-84/45, lectures delivered at the Kaluza-Klein Workshop, Chalk River, August 1983. | [duff-1984-modern-kaluza-klein-theories-kek-8408052.pdf](references/classical-kk-1980s/duff-1984-modern-kaluza-klein-theories-kek-8408052.pdf) | 1-5 | States the three possible KK origins of spin-1 gauge bosons: metric/isometry fields, spin-connection/tangent-space composite fields, or higher-dimensional Yang-Mills fields inserted by hand. Also records Witten's `d=11` max/min observation and focuses attention on `S^7`, `M^{pqr}`, and broken vacua. |
| S. Weinberg, "Charges from Extra Dimensions," Phys. Lett. B 125 (1983) 265-269. | [weinberg-1983-charges-from-extra-dimensions-inspire.json](references/charge-normalization/weinberg-1983-charges-from-extra-dimensions-inspire.json) | abstract metadata | Gives the rms-circumference prescription for calculating gauge couplings from compact dimensions. This is the source-backed form of the `D=9` alpha gate. |
| Z. F. Ezawa and I. G. Koh, "Are the SU(3) X SU(2) X U(1) Interactions From the D=11 Supergravity the Strong and Electroweak Interactions?", Phys. Lett. B 142 (1984) 153-156. | [ezawa-koh-1984-d11-su3-su2-u1-couplings-inspire.json](references/charge-normalization/ezawa-koh-1984-d11-su3-su2-u1-couplings-inspire.json) | abstract metadata | Reports that direct `D=11` supergravity coupling strengths are drastically different from extrapolated strong/electroweak strengths. This is a warning against declaring raw `M^{pqr}` isometry matching successful. |
| D. Bailin and A. Love, "Coupling Constant Ratios From the Kaluza-Klein Manifolds M(pqr)," Phys. Lett. B 144 (1984) 359-364. | [bailin-love-1984-mpqr-coupling-ratios.pdf](references/charge-normalization/bailin-love-1984-mpqr-coupling-ratios.pdf) | equations 52, 54, 55 | Gives the `M^{pqr}` coupling-ratio formulas used in [mpqr-weak-angle-scan.md](mpqr-weak-angle-scan.md). The formulas allow close weak-angle matches but do not select the labels. |
| B. L. Hu and T. C. Shen, "Weak Angle From Kaluza-Klein Theory With Deformed Internal Space," Phys. Lett. B 178 (1986) 373-378. | [hu-shen-1986-weak-angle-deformed-internal-space-inspire.json](references/charge-normalization/hu-shen-1986-weak-angle-deformed-internal-space-inspire.json), [hu-shen-1986-weak-angle-digitalcommons.html](references/charge-normalization/hu-shen-1986-weak-angle-digitalcommons.html) | abstract metadata | Establishes a classical-KK precedent in which an electroweak coupling ratio is related to an internal deformation/shape parameter. The exact formula remains missing until the full paper is obtained. |
| M. J. Duff, "Supergravity, Kaluza-Klein and superstrings," CERN-TH-4568/86. | [duff-1986-supergravity-kk-superstrings.pdf](references/classical-kk-1980s/duff-1986-supergravity-kk-superstrings.pdf) | 1-2 | Reviews the merger of supergravity/KK with string theory and notes applications of KK techniques to strings on group manifolds. |
| M. J. Duff, B. E. W. Nilsson, C. N. Pope, and N. P. Warner, "Kaluza-Klein approach to the heterotic string (II)," CERN-TH-4357/86. | [duff-nilsson-pope-warner-1986-kk-heterotic-string-ii.pdf](references/classical-kk-1980s/duff-nilsson-pope-warner-1986-kk-heterotic-string-ii.pdf) | 1-2 | Heterotic gauge bosons can be approached through a KK compactification of a higher-dimensional bosonic string on group manifolds `SO(32)` or `E8 x E8`; consistency requires scalar fields. |

## Source-Backed Constraints

### 1. Harmonic Expansion Is The Correct KK Language

Coquereaux/Jadczyk do not treat the internal space as a decorative label. They set up fields as sections of equivariant vector bundles, decompose them by irreducible representations of the compact symmetry group `G`, and then interpret each harmonic type as an effective field on the lower-dimensional spacetime.

Consequence:

```text
The de Vries label j cannot be assigned by analogy only.
It must be tied to a harmonic sector of a specific field bundle.
```

For Candidate A this means:

```text
Scalar S3 harmonics, spinor harmonics, form harmonics, and current-algebra states
are different objects. The project must state which one supplies j=1/2 and j=1.
```

### 2. The Gauge Group Is Not Automatically The Full Isometry Group

The effective gauge group in `G/H` compactification is constrained by the reduction scheme. The inspected Jadczyk abstract gives:

```text
G-invariant reduction: consistent truncation with N(H)/H gauge bosons.
Non-G-invariant reduction: a larger local effective group involving N(H)/H and Aut G.
```

Coquereaux/Jadczyk also describe local product choices of `E` as differing by gauge transformations with gauge group `N(H)/H`.

Consequence:

```text
The surviving U(1)_Q cannot be declared from the visual factor S1_Q alone.
It must be derived from the normalizer/effective-gauge-group data of the compactification.
```

This is a direct constraint on the `D=9` endpoint and on the alpha calculation.

### 3. Finite Truncation Is Not Unique

Jadczyk explicitly warns that harmonic expansion and truncation are generally not unique. A `G`-invariant truncation can be consistent, but different choices of subgroup `G` can leave different finite spectra.

Consequence:

```text
The project's moduli-space triage rule is necessary, not optional.
If several truncations exist, select first by exact de Vries compatibility,
then by Regge/string compatibility, then by weaker Casimir-product compatibility.
```

This supports [moduli-space-triage.md](moduli-space-triage.md), but it does not prove the de Vries point.

### 4. A Source-Backed D=11 Standard-Model-Like Parent Exists

D'Auria/Fre state that D=11 supergravity admits a Freund-Rubin compactification with `SU(3) x SU(2) x U(1)` symmetry and `N=2` supersymmetry. Their analysis is on `M^{pqr}` spaces and computes spectra for `0,1,2,3`-forms, scalar Laplacian eigenvalues, and a `*d` operator on 3-forms.

They also state that `B_2=1` gives an extra `U(1)` vector multiplet, so the four-dimensional theory is coupled to the gauge multiplet of:

```text
SU(3) x SU(2) x U(1)
```

Consequence:

```text
The evidence-backed D=11 parent is not C4 x S3 as a global compact space.
It is closer to an M^{pqr} coset compactification with the desired gauge content.
```

The old `C4 x S3_EW` candidate can remain useful only as a local factorization, low-mode mnemonic, or truncation target.

### 5. The Full Tower Matters

D'Auria/Fre emphasize that Freund-Rubin solutions contain infinite multiplets and that it is not automatically clear which ones should be retained in the four-dimensional theory. They give an example where fields that look like a simple hypermultiplet by degree count do not satisfy the expected mass sum rule and instead mix into a larger multiplet.

Consequence:

```text
A two-state de Vries block is not justified by selecting two attractive states.
It must be a closed projected block, or the neglected states must be shown to decouple.
```

This is now a hard pass/fail gate for `k6-operator-derivation.md`.

### 6. Negative Mass-Squared Is Not Automatically Fatal

The inspected D'Auria/Fre pages include an example with a spin-1/2 mass-squared entry written as negative in their units. In AdS/Freund-Rubin spectra, negative mass-squared values can appear without immediately implying a pathological flat-space tachyon.

Consequence:

```text
The de Vries negative branch may be compatible with a compactification spectrum,
but only after the correct AdS/unitarity/stability condition is checked.
```

This supports keeping the negative branch as a possible internal spectral datum, not as a physical four-dimensional tachyon.

### 7. The String Bridge Prefers Group-Manifold/CFT Structure

Duff's 1986 review explicitly frames the merger of supergravity, KK theory, and string theory, including KK methods for strings on group manifolds. The heterotic KK paper constructs string gauge structure from group-manifold compactification and notes consistency constraints involving scalars.

Consequence:

```text
Regge priority should favor an SU(2) current-algebra or group-manifold interface,
not an arbitrary smooth Sigma2 inserted between S3 and S1.
```

This supports the `SU(2)_2` direction in [rns-k6-action-candidate.md](rns-k6-action-candidate.md), but it also warns that a heterotic/group-manifold formulation may be more natural than a minimal Type IIA RNS ansatz.

### 8. The Electroweak Gauge Boson Route Must Be Declared

Duff 1984 separates three mechanisms for spin-1 gauge bosons in KK theory:

```text
route i: metric components from the isometry group of the internal dimensions
route ii: composite fields from the spin connection and tangent-space group
route iii: elementary higher-dimensional Yang-Mills fields inserted by hand
```

This matters because the de Vries clue involves `W`, `Z`, `v`, and `alpha`. Those labels cannot be attached after a spectral calculation. The compactification must say where the electroweak vector bosons come from.

Consequence:

```text
Candidate B must not hide the gauge-boson origin.
Route i points to M^{pqr} isometry/effective-gauge data.
Route ii points to tangent-space, spinorial, or current-algebra structure.
Route iii is a fallback but weakens the geometric claim.
```

Duff also reports Witten's observation that `d=11` is both the maximum dimension allowed by supersymmetry and the minimum needed to accommodate an `SU(3) x SU(2) x U(1)` isometry group. This strengthens the decision to treat `M^{pqr}` as the classical parent rather than treating `C4 x S3` as a global compactification.

### 9. Alpha Is A Generator-Norm Problem

Weinberg's charge prescription turns the `D=9` alpha target into a geometric normalization condition:

```tex
\alpha_Q={16\pi^2G\over L_Q^2}.
```

For the current de Vries alpha target:

```tex
{L_Q\over\sqrt G}=146.16396265602495.
```

The de Vries weak-angle target also fixes:

```tex
{L_Y\over L_2}=1.866083698246127.
```

Consequence:

```text
The project must compute rms circumferences or equivalent current-algebra levels.
SU(2) x U(1) labels alone do not produce electroweak parameters.
```

This also reframes the `M^{pqr}` problem. D'Auria/Fre give isotropy `U(1)'` and `U(1)''` embeddings involving color and weak generators, including `J_3^w`. Those embeddings are candidates for building physical charge generators, but they are not yet the electromagnetic generator.

### 10. Raw D=11 Coupling Matching Is Disfavored

Ezawa/Koh directly tested whether the `D=11` `SU(3) x SU(2) x U(1)` couplings could be identified with strong and electroweak couplings and reported a strong mismatch.

Consequence:

```text
The preferred route cannot simply say:
M^{pqr} has SU(3) x SU(2) x U(1), therefore electroweak parameters follow.
```

The remaining viable options are:

- find a special `M^{pqr}` metric/modulus whose Bailin/Love coupling-ratio formulas satisfy the Weinberg/de Vries target;
- use a string/current-algebra normalization in the D=10 layer while keeping `M^{pqr}` as the D=11 parent;
- demote the de Vries alpha match to numerology if neither route works.

### 11. Shape Moduli Can Be Coupling Data

Hu/Shen is not an `M^{pqr}` paper, but its metadata is important for the current hypothesis. It reports a seven-dimensional KK model with a deformed Taub internal space where the electroweak coupling ratio is related to an internal shape parameter.

Consequence:

```text
The statement "the vacuum extremum fixes the compact shape, therefore fixes
the weak angle" is not alien to classical KK. It has a source-backed analogue.
```

Limit:

```text
This does not prove the de Vries value and does not give the M(pqr) formulas.
It only justifies making a shape-modulus weak-angle calculation a first-class gate.
```

### 12. The D=11 Parent Is Unbroken

The `M^{pqr}` parent supplies unbroken gauge data. It does not by itself supply a Higgs vev or physical `W/Z` masses.

Consequence:

```text
D=11 target: compute g_2 and g_Y from generator norms.
D=10/D=9 target: specify the breaking layer that introduces v and gives M_W, M_Z.
```

This matters for the de Vries interpretation. The `j=1/2` and `j=1` labels can be used in the parent only as representation/coupling-ratio targets. Calling them physical `W` and `Z` masses is premature until the lower-dimensional breaking mechanism is built.

## Revised Structure Suggested By The Evidence

The evidence-aligned replacement for the global parent is:

```tex
K_7^{cl} = M^{pqr}
          = {SU(3) \times SU(2) \times U(1)
             \over
             SU(2)_c \times U(1)' \times U(1)''}.
```

The inspected D'Auria/Fre pages show the subgroup used for harmonic expansion as:

```tex
R = SU(2)_c \times U(1)' \times U(1)''.
```

They also show that the `U(1)'` and `U(1)''` generators are built from linear combinations involving color and weak generators, including a weak `J_3` contribution. This is exactly the type of structure needed for an electroweak charge-mixing problem.

The current working chain should therefore be rewritten as:

```text
D=11: K7 = M^{pqr} parent with unbroken SU(3) x SU(2) x U(1) isometry/gauge data.
D=10: K6 = one-circle reduction, quotient, or string-current interface of K7; possible breaking/interface layer.
D=9:  K5 = second circle/boundary reduction with exact U(1)_Q retained after breaking.
```

The old chain:

```text
C4 x S3_EW -> C4 x Sigma2 -> C4 x S1_Q
```

should now be treated as a local or effective model of the electroweak part of `M^{pqr}`, not as the full compactification.

## Compatibility With The de Vries Hint

The evidence supports the following limited compatibility:

| de Vries ingredient | Classical KK support | Status |
|---|---|---|
| Internal `SU(2)` label `j` | `M^{pqr}` has an `SU(2)` factor and the harmonic-expansion formalism decomposes fields by group representations. | plausible but field-sector dependent |
| `j=1/2` and `j=1` slots | Allowed if the selected sector is spinorial/current-algebraic or otherwise carries half-integer representations. | not yet proven for the relevant KK field |
| Off-diagonal `sqrt(j(j+1))` | First-order operators such as Dirac or `*d` can naturally square to Casimir/Laplacian data; D'Auria/Fre explicitly compute a `*d` operator. | structurally plausible |
| Negative branch | Freund-Rubin/AdS spectra can contain negative mass-squared entries in source pages. | plausible, needs stability bound |
| Exact block `[[0,sqrt(J)],[sqrt(J),-J]]` | No inspected source gives this block. | unproven |
| Electromagnetic `alpha` boundary | Jadczyk constrains effective gauge group; D'Auria/Fre supplies `U(1)` data; Weinberg supplies the rms-circumference gate. | not computed |
| Regge/string compatibility | Duff sources support KK/string group-manifold interfaces. | supports direction, not result |
| Origin of `W`, `Z`, and photon | Duff 1984 supplies the route taxonomy: metric/isometry, tangent-space/spin-connection composite, or inserted Yang-Mills. | route not selected |
| Gauge-coupling normalization | Weinberg gives rms-circumference rule; Ezawa/Koh warn raw D=11 coupling matching is discrepant. | concrete gate added |
| Higgs/breaking layer | D=11 parent should be unbroken; `v`, `M_W`, and `M_Z` require a lower-dimensional mechanism. | not constructed |

## Current Verdict

The strongest current KK structure is:

```text
M^{pqr} D=11 parent
with unbroken SU(2)-U(1) coupling data,
then a D=10/D=9 reduction or interface that breaks to a D=9 U(1)_Q boundary.
```

This is more defensible than the original `C4 x S3` global ansatz because it is anchored in 1980s D=11 KK literature with `SU(3) x SU(2) x U(1)` content.

It still does not meet the full project goal because the decisive calculation remains missing:

```tex
\Pi_j \mathcal D_{K_6} \Pi_j
=
\mu^2
\begin{pmatrix}
0 & \sqrt{j(j+1)}\\
\sqrt{j(j+1)} & -j(j+1)
\end{pmatrix}
```

for the same normalization that gives the `D=9` electromagnetic coupling.

It also requires a breaking mechanism:

```tex
g_2,g_Y\quad\hbox{unbroken in D=11}
\quad\longrightarrow\quad
v,M_W,M_Z,U(1)_{\rm em}\quad\hbox{at the D=9 boundary}.
```

## Next Required Reading

1. Read enough of D'Auria/Fre to extract the exact `M^{pqr}` metric/coset data and the scalar/vector/form eigenvalue formulas.
2. Use the local Weinberg PDF to refine the `D=9` alpha convention checks beyond the abstract-level rms rule.
3. Use the local Bailin/Love PDF and [mpqr-weak-angle-scan.md](mpqr-weak-angle-scan.md) to constrain the `M^{pqr}` labels; the next problem is the selector, not source acquisition.
4. Inspect Witten's realistic-KK obstruction before making any claim about fermions/chirality.
5. Decide whether the `D=10` interface is Type IIA from the M-circle or heterotic/group-manifold from the Duff-Nilsson-Pope-Warner construction.
6. Use the Appelquist-Chodos-Freund book index when accessible; the Archive metadata is local, but the full index/OCR is not.
7. Acquire Hu/Shen or an equivalent source with the deformation-to-weak-angle formula, then test whether the same kind of shape modulus can exist in `M^{pqr}` or the D=10 string-current bridge.
