# N4 — Custodial symmetry under Option B

Date: 2026-06-11.

**VERDICT: DEAD under Option B on X_{1,1}. The custodial reading of T4 was a
statement about a spectator SO(3) — and under Option B there is no spectator:
the isometry budget su(3) ⊕ so(3) is fully consumed by colour and weak, and
the centralizer of the gauged algebra inside the isometry algebra is trivial.
T4's quaternionic so(4) structure on m_3 survives as geometry but changes
meaning: its "custodial-like" factor becomes the gauged weak group itself, so
nothing is left over to protect ρ. Moreover ρ has nothing to protect: the
would-be Higgs doublets are all colour-charged (N6), so an SM-like ρ
parameter is not even defined. Repair path: custodial symmetry of a composite
(colour-singlet bilinear) sector — target for future derivation, out of
scope.**

Conventions: N0. Inputs: T4 (+ its verification pass, whose corrected L/R
quaternion labels are used here), N1, N6 (doublet census).

## 1. What "custodial" requires

A custodial SU(2)_R must (a) be a symmetry of the EW-breaking (Higgs) sector,
(b) commute with the gauged SU(2)_L, (c) not be gauged itself with SM-visible
couplings (it is an approximate global symmetry), and (d) combine with
SU(2)_L into SO(4) ≅ SU(2)_L×SU(2)_R acting on the four real Higgs
components, so the vacuum breaks SU(2)_L×SU(2)_R → SU(2)_diag and enforces
ρ = m_W²/(m_Z² cos²θ_W) = 1 at tree level.

## 2. No spectator group exists under Option B

Expansion block.
- Domain: isometry algebra iso(X_{1,1}) = su(3) ⊕ so(3) (Wilking, cited;
  existence derived in N1 §2).
- Option-B gauging consumes both summands: su(3) → colour, so(3) → weak.
- A custodial generator must commute with the full gauged algebra (it has to
  survive as a global symmetry of the gauge-fixed theory), i.e. lie in the
  centralizer of su(3) ⊕ so(3) inside itself. Centralizer of su(3) in
  su(3)⊕so(3) is so(3) (su(3) simple, centre 0); intersecting with the
  centralizer of so(3) (= su(3)) leaves 0. **No continuous spectator.**
- Contrast with Option A: there the gauged EW sat entirely inside su(3),
  leaving the whole so(3) summand as the spectator — which is precisely what
  T4 evaluated. The Option-A custodial candidate exists because Option A
  under-uses the isometry budget; Option B exhausts it.
- Status: derived (two lines of centralizer algebra; independently posed to
  the GPT-5.5 collaborator as check A/Q3a).

## 3. T4's quaternionic structure, re-read with Option-B labels

T4 established on m_3 ≅ C² ≅ H (the base directions) a commuting pair
Sp(1)×Sp(1) = SO(4) of quaternion multiplications, of which only a U(2) is
holomorphic (C-linear for the fixed complex structure), the complementary
two generators being the complex-structure-rotating pair; and the fibre
SO(3) realizes the (I,J,K)-rotating SU(2) as I = 1 on m_0. Its verification
pass corrected which side is which (with J₀ = left-multiplication-by-i, the
holomorphic SU(2) acting irreducibly on the doublet is the RIGHT factor; the
J-rotating pair lies in the LEFT factor). All of that is metric/complex
geometry, identification-independent — it survives. The physics labels flip:

| Object on m_3 | Option-A meaning (T4) | Option-B meaning |
|---|---|---|
| holomorphic U(2) = SU(2)·U(1)_8 | gauged EW: SU(2)_L × hypercharge line | subalgebra of COLOUR acting on two base directions; q8 = ±3 gluon weights |
| m_3 as doublet, I = 1/2 | Higgs doublet candidate (2_{±3} in the 8) | a weak-doublet, colour-octet scalar harmonic (N6) |
| complex-structure-rotating SU(2) (acts as I=1 on the fibre m_0) | spectator Wilking SO(3) = custodial candidate | the GAUGED weak SU(2)_L itself |
| H ↔ H̃ swap (right-quaternion j, anti-holomorphic realization) | custodial swap protecting ρ | part of the weak gauge action / colour-sector geometry; protects nothing |

The headline of T4 — "right group, right breaking pattern, wrong place,
needs extra input" — degrades under Option B to "right group, but it is the
weak group": a symmetry cannot be custodial with respect to itself. The
SU(2)_L×SU(2)_R → SU(2)_diag pattern needs two DISTINCT SU(2)s acting on one
colour-singlet doublet; Option B has one SU(2) (gauged) and zero spectators
(§2).

## 4. ρ has no carrier anyway

The custodial question presupposes an SM-like breaking vev. N6 proves the
scalar-FIELD doublet census under Option B: every weak-doublet scalar-field
harmonic on X_{1,1} is colour-charged (minimal cases: colour triplet at
twist |m| = 1, colour octet at |m| = 3); a colour-singlet weak-doublet
scalar field does not exist for any line twist (connection-component
scalars sit outside this census — N6 §2 scope, sharpened 2026-06-11). A vev in any existing doublet breaks SU(3)_c;
the resulting vacuum is not the SM's, and m_W/m_Z bookkeeping in the SM
sense does not apply. So under Option B on X_{1,1}, ρ = 1 is neither
protected nor violated — it is undefined. The custodial row of the ledger
dies for lack of a patient, independently of §2's lack of a doctor.

## 5. Counterargument pass

1. *"Custodial symmetry in the SM is accidental, not isometric; maybe the
   reduced potential has an accidental SO(4) even though no isometry
   supplies it."* Accidental symmetries act on the fields that exist. The
   minimal doublet is colour-octet; an accidental SO(4) on it would be a
   custodial symmetry of a colour-breaking sector — not condition (a)-(d).
   Until a colour-singlet doublet exists (composite route, §6), there is no
   sector for the accident to protect.
2. *"The Betti U(1) (N2 §5) or discrete isometries could play spectator."*
   A custodial group must be (a copy of) SU(2); a U(1) or a finite group
   cannot enforce ρ = 1 by the SU(2)_diag argument.
3. *"Under Option A, T4 also found the custodial action obstructed
   (so(4) > u(2)); maybe Option B is no worse."* The obstruction types
   differ in kind. Option A: the candidate exists, acts in the wrong
   holomorphic frame — repairable by an assumption about the reduced
   potential (T4(d), conjecture C3-physics). Option B: no candidate exists
   at all (§2) and no Higgs sector exists for it (§4). Not symmetrical.

## 6. Repair path (named, not pursued)

A composite colour-singlet doublet (quark-bilinear condensate, e.g. the
3̄⊗3 → 1 channel of N6's quark-like slots) could in principle carry an
SU(2)_L×SU(2)_R structure of its own, with custodial symmetry emerging in
the strong sector — the technicolor-shaped escape. Deriving the bilinear
spectrum and its symmetries from the X_{1,1} Dirac sector is a well-posed
future task; nothing in the present geometry performs it. Status: target for
future derivation, outside the current derivation chain.

## 7. Kill criteria

- Exhibiting a continuous isometry of (X_{1,1}, g_t) outside SU(3)×SO(3)
  (contradicts Wilking; would reopen §2).
- Exhibiting a colour-singlet weak-doublet scalar harmonic (contradicts
  N6's census; would reopen §4).

## Sources

- archive/verification_20260531/T4.md and its independent verification
  (so(4)/u(2) structure; corrected left/right labels; doublet census inputs).
- archive/verification_20260531/R5.md part (d) ("custodial reading lost" —
  here derived rather than asserted).
- N1 (isometry derivation, rank budget), N6 (scalar census).
- Wilking, Proc. AMS 127 (1999) 1191–1194.
