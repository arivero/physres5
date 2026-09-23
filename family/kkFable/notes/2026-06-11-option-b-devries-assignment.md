# N5 — The De Vries electroweak assignment under Option B

Date: 2026-06-11.

**VERDICT: The De Vries ALGEBRA survives (it is identification-independent
spectral data of the carrier), but the ELECTROWEAK ASSIGNMENT — and with it
the scale-free prediction sin²θ_W = 0.2231 — is DEAD under Option B on
X_{1,1}. The j = 1/2 slot, which the assignment reads as the W-mass/Higgs
sector, consists under Option B exclusively of colour-charged states (N6);
its condensation would break SU(3)_c, so the M_W²/M_Z² reading is
inconsistent with unbroken colour. The inverted assignment is excluded
numerically (it gives cos²θ_W > 1). Combined with N3, Option B retains no
sharp electroweak number from either inherited mechanism. The c = 1 and
D†D = j(j+1) postulates remain open exactly as before (wastebook C7) and are
not relitigated here.**

Conventions: N0 (the letter j is the fibre spin; J = j(j+1)). Inputs:
wastebook C7 / T5 (algebra and assignment), T4 (sector identification),
N6 (colour content of the j = 1/2 sector).

## 1. The inherited algebra (cited, numbers re-checked by hand)

Signed Hessian A(D) = [[0, D†], [D, −c·D†D]] with D†D = J·1 on the spin-j
sector, J = j(j+1); De Vries condition c = 1. Characteristic polynomial per
sector: λ² + Jλ − J = 0, roots +a_J (vector-mass branch) and −b_J (vacuum
branch), a_J = (√(J²+4J) − J)/2.

Hand checks:
- j = 1/2: J = 3/4; a_{1/2} = (√(9/16 + 3) − 3/4)/2 = (√57 − 3)/8.
- j = 1: J = 2; a_1 = (√12 − 2)/2 = √3 − 1.
- Assignment (Option A reading): cos²θ_W = M_W²/M_Z² = a_{1/2}/a_1
  = (√57−3)/(8(√3−1)) = (√57−3)(√3+1)/16 (using (√3−1)(√3+1) = 2).
- sin²θ_W = 1 − cos²θ_W = (19 + 3√3 − √57 − 3√19)/16
  (expansion: (√57−3)(√3+1) = 3√19 + √57 − 3√3 − 3). Numerically
  (√57 ≈ 7.5498, 3√3 ≈ 5.1962, 3√19 ≈ 13.0767):
  (19 + 5.1962 − 7.5498 − 13.0767)/16 = 3.5697/16 = 0.22311.
  Matches the wastebook's 0.2231013 to the digits computable by hand. ✓

The sector labels are geometric: (a_1, b_1) ↔ the j = 1 fibre triplet (m_0);
(a_{1/2}, b_{1/2}) ↔ the j = 1/2 spin^c doublet sector. The geometry of these
sectors is identification-independent; what Option A vs B changes is what
they MEAN physically.

## 2. The assignment under Option B, slot by slot

Expansion block.
- j = 1 sector (m_0, colour singlet, q8 = 0): under Option B these are the
  weak-adjoint directions — the gauge sector of SU(2)_L itself. Reading its
  branch eigenvalue as the Z-mass slot presumes EW breaking with the SM
  pattern; a vacuum-branch condensate here would be a weak-TRIPLET vev,
  which breaks SU(2)_L without a doublet and is excluded by ρ-phenomenology
  in the SM sense — and in any case supplies no doublet Higgs.
- j = 1/2 sector: by the parity law (N2 §3b) every j = 1/2 state carries odd
  q8, and by the census (N6) every such harmonic/section is colour-charged
  under Option B — minimal realizations: colour triplet at twist |m| = 1,
  colour octet at |m| = 3 (the m_3 doublet, which under Option A was the
  Higgs candidate). The De Vries assignment needs this slot to be the
  EW-condensing sector that feeds M_W. A colour-charged condensate breaks
  SU(3)_c: inconsistent with the Option-B premise that colour is the exact,
  confining, unbroken base isometry.
- Conclusion: under Option B the pairing "j = 1/2 ↔ W-mass slot, j = 1 ↔
  Z-mass slot" attaches EW observables to sectors that can no longer carry
  them. The number 0.2231 detaches from sin²θ_W: it remains a spectral ratio
  of the carrier with no electroweak observable attached.
- Status: derived from N6's census plus the inherited assignment; no new
  postulate introduced.

## 3. The inverted assignment is excluded numerically

Could Option B rescue a prediction by swapping the slots (j = 1, the now
manifestly weak-gauge triplet, as the W slot; j = 1/2 as the Z slot)?
Then cos²θ_W = a_1/a_{1/2} = (√3−1)/((√57−3)/8) = 8(√3−1)/(√57−3)
≈ 8·0.7321/4.5498 ≈ 1.287 > 1 — impossible for a cosine squared. Hand
exclusion, no further assumptions needed. (Any assignment must pick the
smaller-eigenvalue sector for W since M_W < M_Z; a_{1/2} < a_1 forces the
original pairing, which §2 kills on colour grounds.)

## 4. Status of the open C7 postulates

Unchanged and untouched by the flip: c = 1 is not implied by the order-one
condition, inner fluctuations, or the real structure (wastebook C7); a bare
D†D = j(j+1) remains rejected as a production premise (a spin^c Dirac square
is C_G − C_K + |ρ|², not bare j(j+1)); the construction of a first-order
D_patch whose second variation is A(D) with c = 1 remains the open
"Deliverable 4". These are Option-A-facing open items; under Option B they
become moot for the EW reading (§2) but remain open as carrier spectral
questions. Production rule honoured: j(j+1) appears above only as the
evaluated SU(2) Casimir C₂(j) of the named operator A(D) per the wastebook
header standard.

## 5. Counterargument pass

1. *"The geometry still 'predicts' 0.2231; only the name changed."* The
   number is a ratio of branch eigenvalues between two sectors. Calling it
   sin²θ_W is an identification of those sectors with the W and Z mass
   slots. Under Option B that identification contradicts unbroken colour
   (§2) or unitarity of the angle (§3). A number with no observable attached
   predicts nothing.
2. *"A composite colour-singlet doublet (N4 §6, N6 repair path) could
   inherit the j = 1/2 eigenvalue."* Possible in principle; it would require
   showing the composite's mass operator inherits A(D)'s j = 1/2 branch
   value — a new derivation with new postulates, not a transfer of the
   existing one. Status: target for future derivation, outside the chain.
3. *"Under Option A the assignment also attached W to a q8 = ±3 'octet'
   doublet — why was that acceptable?"* Under Option A the SU(3) carrying
   the 8 was the electroweak group; an EW-octet label costs nothing
   physical (it is broken flavour structure of the EW sector). Under Option
   B the same label is colour, which must remain exact. The asymmetry is
   the entire content of the fork.

## 6. Kill criteria

- A colour-singlet j = 1/2 sector on X_{1,1} (would reopen §2; excluded by
  N6's census for scalar fields and line twists; the gravitino-sector
  loophole of N6 §7 concerns an (I_w = 0, Y = −1) fermion, not the bosonic
  condensate slot the assignment needs).
- An error in the eigenvalue arithmetic of §1/§3 (checkable by hand in two
  lines each).

## Sources

- wastebook.md C7 entry and archive/verification_20260531/T5.md (algebra,
  c = 1, EW assignment, 0.2231; open postulates).
- archive/verification_20260531/T4.md (sector geometry: m_0 = j=1 triplet,
  doublets at odd q8).
- N2 (parity law), N3 (the other sharp number's death), N6 (colour census of
  the j = 1/2 sector).
