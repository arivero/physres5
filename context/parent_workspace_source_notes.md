# Parent workspace source notes

These notes summarize manuscript-relevant material read from `..` during the
parent-workspace pass.  They are project source notes and critique provenance.
Primary literature claims still need support from `references/pdfs/` or newly
downloaded papers before they enter manuscript prose as cited physics.

## Reading protocol

- Adjacent project files are local research memory, review artifacts, and
  exploratory drafts.
- Valid imports are constraints, failure modes, theorem targets, source-upgrade
  queues, and provenance trails.
- Manuscript-bound claims require primary sources or an explicitly labeled
  project-source status.
- Numerical tables and fit claims in adjacent projects stay outside the current
  conceptual phase.
- PDF extraction remains an access aid.  Image-bearing PDFs remain source
  objects for formula layout, plots, radicals, and diagrams.

## Inventory

| Parent path | Status for this manuscript | Valid content |
|---|---|---|
| `../weak/criticism.md` | critique provenance | Direct scalar-seed identifications with \(M_W\), \(M_Z\), \(m_h\), or the Higgs order parameter require a gauge-Higgs mass matrix, pole self-energy map, scalar potential, or gauge-invariant scalar functional.  Precision and prediction language require scheme control and independent inputs. |
| `../weak/PHASE_1.md` | normalization audit | The generalized block \(m_0^2\begin{pmatrix}0&a\sqrt{C_2}\\a\sqrt{C_2}&-bC_2\end{pmatrix}\) records the key normalization issue: \(a\) can be absorbed into the scale convention, while \(b\) remains an independent Wilson coefficient until a source operator fixes it. |
| `../weak/LAGRANGIAN.md` | mechanism audit | Hosotani/Wilson-line spectra provide weight-squared towers.  A DeVries derivation must produce the full \(C_2(R)\) block and the off-diagonal product from one source operator. |
| `../weak/LAGRANGIAN_PC.md` | mechanism audit | The Wigner-Eckart route fails for the natural parent representations tested there.  A generator matrix element alone leaves the \(\sqrt{C_2(R)}\) off-diagonal unsupplied for the two electroweak samples. |
| `../weak/PHASE_5.md` | SO(32) audit | SO(32) adjoint branching supplies weak triplets, while weak doublets appear in a spinor branch.  This supports treating SO(32) flavor bookkeeping as separate from the ordered electroweak assignment theorem. |
| `../phys3/sources/unbroken_susy.md` | dimensional-interpolation provenance | The local note behind O10 records the D=11 chirality obstruction and a D=9/D=11 electroweak interpolation idea.  Witten 1981 fragments remain the primary-source control. |
| `../phys3/sources/bootstrap_charges.md` and `../phys3/sources/up_to_SO32.md` | Chan-Paton/bootstrap provenance | These files record the project-source trail for \(N=3,k_u=2,k_d=3\) and SO(32)-flavor counting.  Generation claims require the existing flavor caveat and a primary-source upgrade. |
| `../phys3/results/orientifold_projection.md` | brane-structure caution | Wilson-line data alone leave the separation of the \((15,\bar 3)\) and \((\overline{10},6)\) branches unresolved in that project note.  Projection data require orientifold, orbifold, or equivalent external structure. |
| `../phys3/results/so30_vs_so32.md` | flavor-boundary caution | The \((15,\bar 3)\) source is the tensor-product embedding; the ambient orthogonal group acts as a container.  This weakens uniqueness claims for SO(32) flavor organization. |
| `../signed-dv-custodial-project/mechanisms/conditional_no_go.md` | negative-sector no-go template | Under ordinary SM electroweak breaking with hypercharge as a single \(T_R^3\) spurion, custodial EFT can motivate the operator form \(\Delta M_-^2=\kappa(M_Z^2-M_W^2)\sigma_3\).  The coefficient \(\kappa=C_F/C_A=3/8\) requires an additional UV threshold, charge lattice, or matching assumption. |
| `../signed-dv-custodial-project/mechanisms/minimal_negative_sector_eft.md` | EFT theorem target | A two-state negative sector can be encoded through \(c_Yg'^2(H^\dagger H)\sigma_3\).  The coefficient and the physical identity of \(\Psi_-\) remain matching data. |
| `../signed-dv-custodial-project/mechanisms/string_uv.md` | string-UV caution | D-brane or string embeddings can host gauge sectors, Chan-Paton factors, hypercharge embeddings, and thresholds.  The needed source-theory result is a coefficient and pole-matching derivation, including a branch-status rule for the negative root. |
| `../signed-dv-custodial-project/mechanisms/regge_field_theory.md` | Regge theorem target | \(C_F/C_A=3/8\) has a natural leading-log Reggeization meaning in SU(2), while the manuscript still owes a map from that high-energy \(t\)-channel statement to a vacuum scalar functional or vector pole self-energy. |
| `../dualsm/assessment/GENERAL-REPORT.md` | workflow discipline | Dense speculative corpora need source-grounded assessment, contradiction checks, adjudication, and scoped claims.  Use this as process memory only. |
| `../dualsm/sources/` | future source queue | Seiberg duality and dualized-SM sources may help future duality claims.  Current electroweak determinant work can proceed independently. |
| `../recap/` | excluded for current manuscript claims | Mostly Koide and fermion mass material.  Use only after a future flavor-specific source audit. |
| `../orbits/` | excluded for current manuscript claims | Navigation/orbit notes read as outside the current electroweak string/KK manuscript. |

## Promoted obligations

### Gauge-Higgs assignment

The adjacent `weak` critique sharpens O1.  The ordered assignment
\[
  (J_H,J_{\rm adj})=(3/4,2)
  \longrightarrow
  (M_W,M_Z)
\]
requires a gauge-Higgs mass matrix, pole self-energy map, or equivalent
source-theory reduction.  A scalar-seed quotient alone remains a kinematical
clue.

### Single-source normalization

Every endpoint, interval, Kaluza-Klein, brane, or \(G_2\) route must produce
\[
  \Sigma_{hh,J}=0,\qquad
  \Sigma_{aa,J}=J,\qquad
  \Sigma_{ha,J}\Sigma_{ah,J}=J
\]
from one operator, field basis, and normalization rule.  The parent audit
shows that fixing \(\sqrt{C_2}\) and fixing the \(-C_2\) diagonal entry are
separate tasks until a common source operator binds them.

### Negative-sector EFT obstruction

The signed-root project supplies a useful theorem target:
\[
  V_{\rm eff}\supset
  \frac12\Psi_-^T
  \left[
    m_-^2{\bf 1}
    + c_Y g'^2(H^\dagger H)\sigma_3
  \right]\Psi_-,
  \qquad
  \Delta M_-^2=\frac{c_Yg'^2v^2}{2}\sigma_3 .
\]
Matching the coefficient to a Casimir ratio is a UV matching problem.  The
project-source lesson is the obligation; the Higgs-sector derivation remains
open.

### Custodial single-generator obstruction

With usual electroweak breaking and custodial breaking through the gauged
single generator \(T_R^3\),
\[
  M_Z^2-M_W^2=\frac{g'^2v^2}{4}.
\]
Single-generator factors such as \((T_R^3)^2\) supply single-generator data.
Obtaining the full SU(2) Casimir ratio
\[
  \frac{C_F}{C_A}=\frac{3/4}{2}=\frac38
\]
requires an extra UV threshold, exotic charge lattice, or custodial-generator
sum.  Characterizing that datum is the theorem target.

### String and Regge route discipline

D-brane, heterotic, Regge, and Chan-Paton language can provide a source arena
for the DeVries block.  The required result has the form
\[
  \mathcal S_r
  \longrightarrow
  K_{J,r}^{\rm bare}(\lambda)
  \longrightarrow
  \Gamma_{\rm eff}^{(4)}[H,W,B]
  \longrightarrow
  \Delta^{-1}_{T,V}(s_V;J,r)=0 .
\]
Regge \(C_F/C_A\), Chan-Paton traces, and hypercharge embeddings are candidate
inputs.  The manuscript must still derive the coefficient, branch status, and
pole placement.

### SO(32) and flavor boundary

SO(32)-flavor notes belong in the flavor-boundary ledger.  They can motivate
representation bookkeeping and source-upgrade work.  They derive the ordered
W/Z assignment only after a coupling to the DeVries electroweak operator is
given.

## Source-upgrade queue

- Source-audit custodial EFT and HEFT/SMEFT treatments before using the
  negative-sector EFT obstruction in manuscript prose.
- Add primary brane/Chan-Paton sources if SO(32) or endpoint flavor counting
  moves beyond the boundary section.
- Page-check Witten 1981 and the six-dimensional string sources before
  promoting the \(D=11/10/9\) and \(D=7/6/5\) interpolation beyond
  reconstruction status.
- Use the signed-root mechanism notes as no-go templates, then replace them
  with primary field-theory or string-theory sources for any journal claim.
