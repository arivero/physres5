# Conversation Harvest Gaps

Companion to [conversation-priority-index.md](conversation-priority-index.md).

This file records ideas present in the source conversations that the
priority index dropped or materially under-weighted. It was built from a
full read of the 15 substantive cleaned conversations.

Source path prefix: `../devries-string-2026-05-24-clean/`. Conversation
legend used in anchors below:

- 01 = `01-prompt-execution-request-...md` (founding mega-thread)
- 02 = `02-resume-for-project-...md`
- 04 = `04-higgs-top-z-relation-comparison-...md`
- 06 = `06-particle-theory-approaches-...md`
- 07 = `07-kaluza-klein-and-constraints-...md`
- 08 = `08-extract-project-details-...md`
- 09 = `09-su-2-spin-and-flux-...md`
- 10 = `10-chiral-particle-interaction-...md`
- 15 = `15-electroweak-vacuum-concerns-...md`
- 16 = `16-conceptual-innovation-inquiry-...md`

## Meta-finding

The harvest kept the geometry-scaffolding ideas (the K5/K6/K7 ladder,
the dimension flow) and dropped two layers: the named mechanisms that
close the hard gaps, and most user-originated directives. The Atiyah
hint was one instance of a systematic pattern. The downstream effect is
the `M^{pqr}` construction with the operator and selector rebuilt from
scratch, because the existing solutions were filtered out before
prioritization.

## A. Dropped solutions to the central paradox

The spine gap is: get from Casimir labels `(s=1/2, s=1)` to physical
`W/Z` vectors, and source the `-J` sign and the `sqrt(J)` off-diagonal.
The conversations supply concrete answers.

- **G1. `SU(2)_L` as a magnetic / Seiberg-dual gauge group.** 16:1886-1900,
  1241-1253. Assistant from a duality directive. `s=1/2` labels the
  electric/dual branch; `W` is the magnetic IR vector pole; W/Z partially
  composite (Csaki-Shirman-Terning, Cacciapaglia-Sannino). Named
  resolution of the two-vectors paradox.
- **G2. de Vries is a pole-mass secular condition.** 16:1786-1833,
  2450-2588. `s^2_pole = 1 - M_W,pole^2 / M_Z,pole^2`, complex-pole
  sharpening `s_V = M^2 - i Gamma M`, residual ~ -2.8 MeV. The number is
  a pole condition distinct from a running-coupling fit.
- **G3. Worked branch-quotient propagator construction.** 16:2590-2630,
  2773-2823. `Gamma_W(X) = Z_W (X - X+(1/2))`, etc., giving
  `M_W^2 = X+(1/2)`, `M_Z^2 = X+(1)`, `M_gamma^2 = 0`, `rho = 1`. The
  "next calculation" already executed.
- **G4. Freund-Rubin flux criticality as the origin of `-J`.** 09:408-493.
  In AdS4 x M vacua, background flux mixes form degrees: off-diagonal
  `sqrt(J)`, diagonal Laplacian, `M^2 = Delta_L - 4 m^2`. `tr = det = -J`
  becomes a self-dual flux tuning against curvature.
- **G5. Henkel-Lauret Curl operator gives `sqrt(J)` geometrically.**
  09:461-467, 1293-1319. On `S^3`, `Curl = *d` is self-adjoint on coexact
  1-forms and `Delta_1 = Curl^2`, so `Curl ~ +/- sqrt(J)`. A
  project-uploaded reference. The off-diagonal is a first-order operator.
- **G6. K6 as a transfer operator with a normal-form theorem.**
  01:8489-9018. `I_EW: K7 -> K5` as a morphism, `K6 in Hom(K7,K5)`. A
  minimal axiom set (Q exact, SU(2) covariance, one tangent + one normal
  channel, Casimir factorization, Regge-product preservation, no free
  parameter) forces `D_T` uniquely. This is the conceptual pivot the user
  demanded (01:8271).
- **G7. Poincare-Casimir parent operator.** 16:261-280, 1002-1066;
  06:1141. `X^2 - X C2 + C1 C2 = 0` with `C1 = m^2`, `C2 = -m^2 s(s+1)`,
  giving `s^2_dV = 0.22310132` and negative roots near 176 GeV and
  122 GeV. The 2x2 block is downstream of this; it is what ties `s=1/2,1`
  specifically to W/Z.

## B. User-originated directives dropped (Atiyah-class)

- **G8. EPJC footnote charge-lift / gluing metric.** 01:9889-9909,
  10221-10292. User directive: "see what you make of their footnotes."
  Gives `Q = (1/5)(2/3 Y1 - Y2)` and `theta_W` as a gauge-kinetic gluing
  metric of `Q -> T3 + Y`. A different `theta_W` mechanism than the de
  Vries block.
- **G9. Lens `q` as a rational `T3/Y` Heegaard gluing.** 01:3177,
  3316-3403. User hint: "see if the selection of the space selects
  weinberg angle." The lens parameter `q`, together with `p=6`, could fix the
  `T3/Y` mixing via the Heegaard gluing map. Only `q=1` was ever used.
- **G10. Lattice / continuous `s^2_{q,p}` tower.** 15:347-628. User
  proposed sampling the Casimir at lattice points `(q/2, p)`. Closed form
  `s^2_{q,p}`, de Vries = point `(1,1)`, large-spin decay `~1/p^3`
  preserving the Regge slope. A predictive family, never pursued.
- **G11. Koide / Sumino sqrt-mass weighting.** 06:2348, 2655-2663, 3765.
  User: "I see no reactions to this yet, about koide." The sqrt-mass
  weighting echoes the project's own `sqrt(J)`.
- **G12. Heterodox-derivation taxonomy (user-authored).** 06:2341-2351.
  Division algebras / `J3(O)` / `SO(8)` triality (Furey, Boyle); cobordism
  / `Z16` global anomaly / symmetric mass generation (Wang, Tong); p-adic
  / adelic physics. Competing generation mechanisms, none entered.
- **G13. `-4/3` chiral particle and emergent-EM dark matter.** 10:9-11,
  325-327. Two user threads: how a `-4/3` state is seen by emergent
  `U(1)_EM`, and whether it is a dark-matter candidate.
- **G14. Two recurring user paradoxes, resolved in-thread.** 07:11, 314-471;
  15:11, 169-345; 07:538-621. (a) Why de Vries has a rigid separation from `M_W = M_Z`:
  rigidity is a critical-point/phase feature, `M_W=M_Z` needs `g'^2 < 0`.
  (b) How one dimension grows to 11 and shrinks to 9: two distinct circle
  operations, `S1_M` reduction then `S1_EW` T-dual/open projection, with a
  D0-tower vs Neumann-zero-mode test. Resolutions entered the project
  late through P0.9.

## C. Strongest mechanism and constraint drops

- **G15. `c=1` as the single falsifiable target.** 07:2164-2221. The most
  general coupling-preserving deformation is `A_J(c)=[[0,sqrt(J)],
  [sqrt(J),-cJ]]`; de Vries requires `c=1`; the brane action
  `S_DBI + S_WZ + S_RR` must give exactly `c=1`.
- **G16. Two gauge kinetic functions are required.** 08:1372-1428.
  `s_W^2 = f2/(f2+f_Y)`, `e^-2 = f2 + f_Y`. One radius fixes the scale;
  two gauge kinetic functions fix the angle. Radial data `{v,mu,R}` and projective data `{g'/g, s_W^2}`
  must be separated.
- **G17. Higgs = radion.** 09:496-567, 1598-1656. The stabilizing modulus
  and the symmetry-breaking field are the same size modulus; EW scale as a
  geometric mean `mu ~ sqrt(v M_Z / 2) ~ 107 GeV`; named precedents Bucci,
  Haba-Oda. Falsifiable coupling-pattern test `g_hWW, g_hZZ, g_hff`.
- **G18. Sen tachyon condensate of the old hadronic string; two scales.**
  09:569-678, 1413-1478. The negative branch as the old dual-model tachyon
  condensing a la Sen, with the coupling read at the hadronic slope
  `alpha' ~ (1 GeV)^-2`, which is where `1/alpha = 135.3` lands. Intercept
  scale ~100 GeV vs slope/coupling scale ~1 GeV; the ~100 factor is
  intrinsic. Explains where `1/alpha` lives.
- **G19. Torrente-Lujan NNLO running boundary.** 04:800-973. The exact NNLO
  boundary predicts `M_H = 123.19 GeV`, `M_t = 177.81 GeV`, matching the de
  Vries negative roots (122.39, 176.16). User-caught; assistant conceded it
  was under-weighted.
- **G20. Regge invariant is the branch product.** 01:8759-8793, 9020-9048;
  16:305-347. `lambda+ lambda- = -T(T+1)` is the Regge-preserving object;
  the two roots are factors of one invariant. Sharper than the
  positive-branch reading; bears on the Regge moduli selector.
- **G21. q-brane Regge scaling.** 02:190-211; 16:339-347. `M^2 ~ J^{2q/(q+1)}`:
  `q=0` point-like, `q=1` string, `q -> inf` tachyonic/`J^2`. The bounded
  positive branch and the growing branch are brane-dimension endpoints.
- **G22. Reciprocal / parallel relation.** 08:280-306, 1139-1171.
  `1/M+^2 + 1/M-^2 = 1/mu^2`; pole condition `x = J/(J+x)` read as an
  inverted seesaw / Riccati equation.
- **G23. Diagonal `Z6` charge-lattice congruence.** 01:7450-7468.
  `r + 2 c3 + 3 c2 + q_Y = 0 (mod 6)` with SM integer hypercharges. The
  computable form of the global-form gate, coupling lens-`r` to the color
  and weak centers.
- **G24. Equivariant selection rules and a threat term.** 01:5337-5343,
  7091-7111, 7235-7239. Higgs doublet survives in nontrivial flat
  sectors `y + r = 0 (mod 6)`; vectors obey `y + eta + r = 0 (mod 6)`; a
  Berger deformation injects a hypercharge `d*y^2` term that must vanish for
  exact de Vries.
- **G25. Exact vacuum-scale identities.** 01:1478-1494; 08:247-274.
  `|m_{1,-}| = v/sqrt(2)` forced by `G = sqrt(3)+1`; prescription
  `v = sqrt(2) M-(2)` fixes the tree-level set and the alpha corollary.
- **G26. 96.5 GeV `j=3/2` neutral state.** 08:352-364. Next upper-branch
  state, a predicted neutral spin-0 slot; conditional link to the ~95 GeV
  diphoton feature. Near-term-falsifiable.
- **G27. Relativistic-orbit derivation of `F+(S)`.** 01:674-704.
  `beta^2 / sqrt(1 - beta^2) = sqrt(j(j+1))` gives the same `F+(S)`,
  a non-Casimir origin. Relevant because the user de-emphasized Casimir.
- **G28. Ratio-vs-scale numeric decomposition.** 01:6113-6181, 7788-7884.
  The block hits the mass ratio to ~1e-4; the absolute scale carries a
  common ~2.4% threshold. A precise falsifiability target.

## D. Stop-Check Verdict

- **G29. The `T+ H0` norm is 1, while the doublet Casimir is 3/4.**
  08:1199-1209. With `T_a=sigma_a/2`,
  `T_+=T_1+iT_2=[[0,1],[0,0]]`, and
  `H_0=(0,v/sqrt(2))^T`, one gets
  `||T_+H_0||^2/||H_0||^2=1`. The Casimir calculation still gives
  `sum_a ||T_a eta_0||^2=3/4`. Verdict: use
  `J_branch(1/2)=3/4` as the de Vries/Poincare-Casimir branch label
  from G1-G3/G7, and use `N_W=1` as the literal charged
  broken-vacuum orbit norm. Requirement: any D10/D6 interface that maps
  `X_+(1/2)` to the physical `W` pole must carry this branch quotient or
  dual-sector conversion explicitly.

## E. Named comparators and programs never used

- **G30. Witten `S^5 x S^3` Pati-Salam via `U(1)` quotient.** 16:1139-1179.
  `SU(4) x SU(2) x SU(2)` on `S^5 x S^3`, quotient by a `U(1)`, gives the
  SM gauge group in D=11. The historical precedent for the D=11 -> D=9
  picture.
- **G31. Finite Unified Theories / Zimmermann reduction of couplings.**
  06:875-881. RG-invariant relations `g_i = f_i(g)`, `y = f(g)`,
  `lambda = f(g)`. An on-target named program for parameter reduction.
- **G32. Custodial `SU(2)_L x SU(2)_R -> SU(2)_D`, `rho = 1`.** 16:1902-1932,
  2636-2733. A hard constraint on any de Vries propagator construction; a
  flat higgsless model gives W/Z off by ~10% without it; EWSB as a
  boundary-condition breaking with an AdS/CFT dictionary.
- **G33. EPJC Footnote 2: dual mass protection, M2/M5 SU(9).**
  01:9992-10058, 10373-10391. Two protections `P_D` (top) and `P_M`
  (neutrinos) meeting at K6; `84 = dim Lambda^3(9)` as an M2/M5 brane-charge
  space with `SU(9)`. A candidate reason for why `t, nu, H, W, Z` are the
  EW-special states.
- **G34. sBootstrap flavour counting and SO(32) interpretation.**
  16:968-998, 1099-1135, 1209-1221. `r = 2p - 1`, `(p-r)^2 = 1` select five
  light flavours with the top as spectator; an `SO(32) -> SU(5)` flavour
  interpretation with a falsifiable `+4/3` chiral diagnostic; a
  hyperbootstrap on ordered pairs `(Y, T3)`.

## Status

This is a recovery list with status control. Items move into
[conversation-priority-index.md](conversation-priority-index.md) or the
[claim-ledger.md](claim-ledger.md) after a decision on priority. The
highest-value user-originated items are G8, G9, G10, G11, G12, G13, G14.
G29 has a stop-check verdict: `J_branch(1/2)=3/4` and `N_W=1`.
