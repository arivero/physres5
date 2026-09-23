# Proposal as stated (claims C1–C7)

Source: user-uploaded note "Higgsing Kaluza–Klein Review". This file records the claims
*as proposed*; verification verdicts are in wastebook.md.

Core move: replace the quaternionic Hopf fibration S^3 -> S^7 -> S^4 (fibre SU(2), base
symmetry SO(5) — "wrong group") as the KK carrier with an Aloff–Wallach construction
SO(3) -> X_{1,1} -> CP^2, where
  X_{1,1} = SU(3)/U(1)_{1,1} = (SU(3)×SO(3))/U(2)_Delta,  U(1)_{1,1}=diag(z,z,z^-2).
Rationale: CP^2 = SU(3)/U(2) has stabilizer U(2) ~ SU(2)×U(1) (electroweak-like).

C1  CP^2/conj ≅ S^4 (Kuiper–Massey). Branch locus RP^2. The quotient is SO(3)-equivariant
    but NOT SU(3)-equivariant; hence the conjugation map is not used as the carrier.
C2  Aloff–Wallach X_{k,l} fibres over CP^2 with fibre the lens space S^3/Z_{|k+l|}.
C3  X_{1,1} has fibre SO(3) (Wilking identification (SU(3)×SO(3))/U(2)_Delta); dim 7.
C4  CP^2 is non-spin / spin^c; X_{1,1} is the Boyer–Galicki–Mann homogeneous 3-Sasakian
    SO(3)-bundle over CP^2. SO(3) -> Sp(1)=SU(2) lift is obstructed; that obstruction is
    where hypercharge enters.
C5  Weinberg angle = ratio of homogeneous Killing inertias; "non-arbitrary", not a free
    radius modulus.
C6  Anchors: Witten 1981 (7 = min dim for SU(3)×SU(2)×U(1)); Castellani–D'Auria–Fré
    (CP^2×S^3 with SU(3)×SO(4)); Weinberg 1983 (couplings from inertias).
C7  "De Vries condition": Dirac block A(D)=[[0,D],[D†,-D†D]] with an originally claimed
    j(j+1) eigenstructure;
    pairing (a_1,b_1) <-> j=1 / SO(3)_R and (a_{1/2},b_{1/2}) <-> j=1/2 / spin^c; the Higgs
    Hessian factorizes into a signed block. USER-INTERNAL: defined in the files
    kk_devries_signed_hessian and the Dolan–Nash/WZ addenda (not in this bundle).
    Current production standard: final documents may use this number only as the evaluated
    `SU(2)` Casimir `C_2(j)` of a specified operator/sector, never as a bare Dirac-square input.
