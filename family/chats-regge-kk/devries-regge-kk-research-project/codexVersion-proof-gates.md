# codexVersion Proof-Gate Notes

Auxiliary control file for `codexVersion.tex`. Proof gates and task
bookkeeping stay here, in the progress reports, in `claim-ledger.md`, or in
`goal-completion-audit.md`. The manuscript may point here through TeX comments.

## Current Thesis

`codexVersion.tex` develops the D10 boundary-current route:

```text
Type IIA on CP2 x CP1 with flag/current refinement
-> Q-boundary Gamma_EW = M4 x CP2 x S1_Q
-> D9 (SU3_c x U1_Q)/Z3 endpoint
```

The manuscript-level result is a conditional D10 operator theorem. The
technical program is to derive the boundary/current sector that realizes the
conditions.

## Steering Locks

- Tuple-family fits such as `(12,14,91,1)` are density diagnostics.
- The relation `r=Q(P+Q)=91` is an internal consistency condition inside a
  specified realization and carries zero construction-evidence weight.
- The vertical-length closure equation is a compactification constraint on
  any D10 IIA realization that hosts the branch operator.
- Keep the `Q`-boundary carrier, `Z6 -> Z3` endpoint, KLT flag admissibility,
  and Connes finite-sheet dictionary as realization data.
- The alpha-backsolved value `rho_*=9.463...` is archived. Absolute
  electromagnetic normalization remains unresolved; the active route is the
  localized `L_Q` calculation.
- Hosotani/gauge-Higgs steering: derive the single-portal premise by
  identifying `phi` with a Wilson-line zero mode
  `theta_H=int_gamma A_int` on a retained weak or boundary cycle.
- The decisive Hosotani expansion must produce the linear insertion
  `alpha_mix A_j` and the quadratic self-energy
  `beta_diag A_j^dagger A_j` from one localized D10 action, with
  `beta_diag=alpha_mix^2`.
- Hosotani compatibility checks: holonomy periodicity, `Q`-neutral vacuum
  component, absence of an independent curvature-shifted operator, finite
  Wilson-line potential, Connes sheet scalar dictionary, and `Gamma_EW` Schur
  auxiliary origin.
- Pure `S1_Q` Hosotani test: `U_Q(theta)=exp(i theta Q)` gives zero first and
  second insertions on `eta0` because `Q eta0=0`; the scalar cycle must be a
  retained transverse weak/current or Chan-Paton boundary-complex cycle.
- Hosotani calculation order:
  1. Select `gamma_H` and its generator embedding in the current frame `e_a`.
  2. Compute the four-dimensional kinetic coefficient `f_H^2` and the
     holonomy scale `mu_Gamma` from the localized `Gamma_EW` action.
  3. Expand `U_H=P exp(i mu_Gamma int_gamma_H xi^a e_a T_a^(j))`; verify
     first insertion `i mu_Gamma T_a^(j)` and second insertion
     `-mu_Gamma^2 T_a^(j)T_b^(j)`.
  4. Canonically normalize the scalar and check
     `beta_diag/alpha_mix^2=1` in the same current frame.
  5. Derive the periodic potential
     `V_H(theta_H)=sum_m c_m cos(m w_H theta_H)` and test its finite
     stationary point against `ell_H=1/|v_F|=sqrt(2)/v_EW`.
  6. Check finite-triple compatibility: KO6 grading, Poincare-duality
     multiplicity, determinant-one hypercharge lift, and survival of the
     `Q` projection.
- Hosotani local-data checklist:
  `(gamma_H, omega_H, n_H^a, (f_H^2)_{ab}, w_H)`, with
  `int_gamma_H omega_H=1`, current-frame direction `n_H^a e_a`, kinetic matrix
  from localized DBI/Yang-Mills plus endpoint terms, and charge-lattice period
  `theta_H ~ theta_H + 2pi/w_H`.
- Hosotani stationary scalar check:
  `|f_H theta_H,*|=|v_F|=v_EW/sqrt(2)`; the neutral vector `eta0` is the
  unitary-gauge component, and the full cycle assignment still has to carry the
  electroweak doublet before the `Q`-neutral projection.
- Rejected Hosotani rows: curvature-shifted tensor, independent second
  operator, mismatched current frame, or scalar support on pure `S1_Q`.
- Detailed Hosotani steering:
  H1 holonomy algebra: one Wilson expansion has to give
  `i mu_Gamma T_a^(j)` and `-mu_Gamma^2 T_a^(j)T_b^(j)` in the same
  current frame used by `A_j`.
  H2 localized normalization: compute `f_H^2`, endpoint metric terms,
  `mu_Gamma`, and charge period `w_H` from the D10 `Gamma_EW` action.
  H3 scalar vacuum: derive the Fourier coefficients `c_m` in
  `V_H(theta_H)=sum_m c_m cos(m w_H theta_H)` and test
  `|f_H theta_H,*|=v_EW/sqrt(2)`.
- Hosotani row data:
  `(gamma_H, omega_H, n_H^a, (f_H^2)_{ab}, w_H, mu_Gamma, c_m)`, plus the
  finite-sheet map to `v_F` and the Schur-scale comparison
  `mu_*^2=M_Z^2/X_+(2)`.
- Point-projector normalization:
  `G_ab^(p)=Re <0|T_a(1-P_p)T_b|0>=(Q/4) diag(1,1,0)`, giving
  `alpha_mix=2 mu_Gamma/(sqrt(Q) f_Gamma)`,
  `beta_diag=4 mu_Gamma^2/(Q f_Gamma^2)`, and
  `beta_diag/alpha_mix^2=1`.
- Mass-dictionary discipline:
  `Q=7` supplies the filtration/current metric stack; the physical mass
  block uses the `Q_w=1` doublet specialization, hence
  `M_W^2=g2^2 v_Gamma^2/4`,
  `M_Z^2=(g2^2+gY^2)v_Gamma^2/4`, and
  `v_Gamma=sqrt(2)|v_F|`.
- Hosotani-Schur scale ratio:
  `mu_Gamma,Schur^2=mu_*^2=(g2^2+gY^2)f_H^2 theta_H,*^2/(2X_+(2))`.
  The local target is
  `chi_H=2X_+(2)mu_Gamma,Schur^2/((g2^2+gY^2)f_H^2 theta_H,*^2)=1`.
  With `f_H^2=Q f_Gamma^2/4`, this becomes
  `mu_Gamma,Schur^2=Q(g2^2+gY^2)f_Gamma^2 theta_H,*^2/(8X_+(2))`.
- Minimal Hosotani Fourier test:
  `V_H=c1 cos x+c2 cos 2x`, `x=w_H theta_H`, gives interior stationary
  branch `cos x_*=-c1/(4c2)`, local minimum conditions `c2>0`,
  `|c1|<4c2`, finite-sheet ratio
  `c1/c2=-4 cos(w_H v_EW/(sqrt(2) f_H))`, and canonical curvature
  `m_theta^2=4w_H^2 c2 sin^2 x_*/f_H^2`.
  Full-curvature specialization gives
  `c2=M_H^2 f_H^2/(4w_H^2 sin^2 x_*)` and
  `c1=-(M_H^2 f_H^2/w_H^2) cos x_*/sin^2 x_*`.
  Eliminating `f_H` gives
  `c2/v_EW^4=lambda_F/(4x_*^2 sin^2 x_*)`,
  `c1/v_EW^4=-lambda_F cos x_*/(x_*^2 sin^2 x_*)`, and
  `f_H=w_H v_EW/(sqrt(2)x_*)`.
- One-tower Hosotani filter:
  a massless charge-one tower with `c_m=A1/m^5` gives `c1/c2=32`; the
  interior condition `|c1/c2|<4` requires extra spectral contributions.
  With charge-one amplitude `A1` and charge-two amplitude `A2`,
  `A2/A1=-1/(4 cos x_*)-1/32`.
  Sign branches: `A1>0` gives `A2/A1>7/32` and `pi/2<x_*<pi`;
  `A1<0` gives `A2/A1<-9/32` and `0<x_*<pi/2`.
- General massless charge-spectrum formula:
  `V_H=sum_r A_r sum_m cos(m r x)/m^5=sum_n c_n cos(nx)`, with
  `c_n=n^-5 sum_{r|n} r^5 A_r`.
  Hence `c1=A1`, `c2=A1/32+A2`, `c3=A1/243+A3`, and
  `c4=A1/1024+A2/32+A4`.
- Borel-Weil charge-parity test:
  use integer charge `q=2m` on `H^0(CP1,O(n)) ~= V_{n/2}`, giving
  `q=-n,-n+2,...,n`.
  `O(1)` supplies `|q|=1`, `O(2)` supplies `|q|=2`, and `O(7)` supplies
  `|q|=1,3,5,7`.
  The weak-period stack has zero `A2`; the line-square sector
  `O(2) ~= Sym^2 O(1)` is the minimal Borel-Weil second-harmonic source.
- Signed Hosotani supertrace target:
  `A_r=C_H sum_{|q_alpha|=r} sigma_alpha d_alpha tau_alpha`.
  For `O(1)+O(2)`, define `S1` and `S2` from the charge-one and charge-two
  towers. Then `A2/A1=S2/S1`.
  Finite-minimum pass:
  `S1>0: S2/S1>7/32` and `S1<0: S2/S1<-9/32`.
  Same-sign charged weights give `S2=S1`, `c1/c2=32/33`,
  `cos x_*=-8/33`, `x_*=1.815660181000518...`, and
  `f_H/v_EW=0.389448856446748... w_H`.
- Charge-conjugate pair reduction:
  if the localized real structure pairs `+r` and `-r` with the same threshold
  weight, then `S_r=2 sigma_r d_r tau_r`.
  For `O(1)` and `O(2)`,
  `S2/S1=sigma2 d2 tau2/(sigma1 d1 tau1)=chi12`.
  Equal-weight pass: `chi12=1`.
  General pass:
  `sigma1 d1 tau1>0: chi12>7/32` and
  `sigma1 d1 tau1<0: chi12<-9/32`.
- Threshold-resolved harmonic target:
  for a flat local circle, use
  `F(z)=exp(-z)(1+z+z^2/3)` and `tau_{r,m}=F(m z_r)`.
  With `D_r=C_H 2 sigma_r d_r` and `chi12^(0)=D2/D1`,
  `c1=D1 F(z1)` and `c2=D1 F(2z1)/32+D2 F(z2)`.
  Hence
  `c2/c1=F(2z1)/(32F(z1))+chi12^(0)F(z2)/F(z1)`.
  Equal signed-base pass gives
  `cos x_*=-1/[4(F(2z1)/(32F(z1))+F(z2)/F(z1))]`.
- Equal-base threshold domain:
  `F'(z)=-(1/3)exp(-z)z(1+z) <= 0`.
  For `D2=D1` and `D1>0`, the finite-minimum pass is
  `F(z2)>F(z1)/4-F(2z1)/32`.
  At `z1=0`, this gives `F(z2)>7/32`, hence
  `z2<3.773046018411012...`.
  The common-threshold ray `z2=z1` passes because
  `1+F(2z1)/(32F(z1))>1/4`.
- Holomorphic zero-mode pass:
  Borel-Weil sectors are Dolbeault kernels,
  `H^0(CP1,O(n))=ker dbar_{O(n)}` for `n>=0`.
  The `q=+-1` pair in `O(1)` and the `q=+-2` pair in `O(2)` therefore have
  `z1=z2=0`; the `q=0` middle state in `O(2)` is independent of `theta_H`.
  With common signed oscillator data `sigma2 d2=sigma1 d1`, the coefficients
  are `c1=D1`, `c2=33D1/32`, hence `c1/c2=32/33`,
  `cos x_*=-8/33`, and
  `f_H/v_EW=0.389448856446748... w_H`.
- Common boundary-complex multiplicity:
  in homogeneous coordinates `[u:v]`,
  `O(1)` has charged basis `u(q=+1), v(q=-1)`, and
  `O(2)` has charged basis `u^2(q=+2), uv(q=0), v^2(q=-2)`.
  The `uv` mode is Wilson-neutral.
  A common localized boundary complex `B_Gamma` acting with the same sign and
  degeneracy on `(u,v)` and `(u^2,v^2)` gives
  `sigma2=sigma1`, `d2=d1`, and `D2=D1`.
- Charged-projector trace form:
  `P1^chi` projects onto `span{u,v}` and `P2^chi` projects onto
  `span{u^2,v^2}`, so `Tr P1^chi=Tr P2^chi=2` and
  `P2^chi=1-|uv><uv|`.
  A common oscillator block
  `B_Gamma^chi=B0 otimes P_r^chi` gives
  `D_r=C_H sigma Tr_{P_r^chi} 1=2 C_H sigma`, hence `D2=D1` and
  `V_H(x)=D1 cos x+(33/32)D1 cos(2x)`.
- Equivariant Dolbeault character pass:
  `Ind_{S1} dbar_{O(n)}(x)=sum_{k=0}^n exp(i(n-2k)x)` for `n>=0`.
  Thus `I1(x)=2 cos x` and `I2(x)=1+2 cos(2x)`.
  The `1` term is Wilson-neutral.  Common endpoint sign and density on the
  two Dolbeault zero-mode sectors give `A1=A2`, hence
  `c1=A1`, `c2=A1/32+A2=33A1/32`, `c1/c2=32/33`, and `cos x_*=-8/33`.
  The `cos x_*=-8/33` value is the two-harmonic truncation.
  Pair-normalized form:
  `V_BW(x)=D sum_{m>=1} [cos(mx)+cos(2mx)]/m^5`, giving
  `c1=D` and `c2=33D/32`.
  Full massless-character stationary equation:
  `Im Li4(e^{ix})+2 Im Li4(e^{2ix})=0`, with
  `x_full=1.837672606049940...` and
  `f_H/v_EW=0.384783872197163... w_H`.
  Curvature factor:
  `K_full=-Re Li3(e^{ix_full})-4 Re Li3(e^{2ix_full})=3.557941701817797...`.
  Matching `M_H^2=2 lambda_F v_EW^2` gives
  `D/v_EW^4=0.083227124394645... lambda_F`.
  Common-threshold flow:
  `V_z(x)=D sum_{m>=1} F(mz)[cos(mx)+cos(2mx)]/m^5`.
  Roots: `x_0=1.837672606...`, `x_1=1.834541900...`,
  `x_2=1.829406205...`, and
  `x_infty=acos(-1/4)=1.823476581936975...`.
  Localized determinant amplitude:
  `D=(3/(4 pi^2)) N_Gamma^chi/L_H^4`, with
  `N_Gamma^chi=Str_chi zeta_alpha` after canonical zero-mode normalization.
  Common DBI/open-boundary density cancels from the Wilson-angle dependent
  determinant and enters `f_H^2` plus threshold parameters.
  Full massless-character target:
  `(3/(4 pi^2)) N_Gamma^chi/(L_H^4 v_EW^4)=0.083227124394645... lambda_F`,
  equivalently
  `N_Gamma^chi/(L_H^4 v_EW^4)=1.095225057620535... lambda_F`.
  Loop-length metric bridge:
  if `omega_H=ds/L_H`, then `f_H^2=Z_Gamma,H/L_H`.
  With `x_*=w_H theta_H,*` and `f_H theta_H,*=v_EW/sqrt2`,
  `L_H=2 x_*^2 Z_Gamma,H/(w_H^2 v_EW^2)`.
  Substitution gives
  `N_Gamma^chi w_H^8 v_EW^4/(16 x_*^8 Z_Gamma,H^4)=1.095225057620535... lambda_F`
  for the full massless-character root.
- Point-projector Hosotani metric bridge:
  `f_H^2=Q f_Gamma^2/4`.  With the full massless-character root,
  `f_H/v_EW=0.384783872197163... w_H`, hence for `Q=7`,
  `f_Gamma/v_EW=0.290869266954901... w_H`.
  The common-density equation is
  `Z_Gamma,H/L_H=Q f_Gamma^2/4`, and the localized density target is
  `N_Gamma^chi/Z_Gamma,H^4=2279.126786313921... lambda_F/(w_H^8 v_EW^4)`.
- DBI coefficient map:
  `S_YM^Gamma=-(T8(2 pi alpha')^2/4) int_Gamma e^-phi sqrt(gamma_Gamma) tr_end F^2`.
  With `A_s=theta_H omega_H,s n_H^a T_a`,
  `f_H^2=T8(2 pi alpha')^2 int_Gamma,int e^-phi sqrt(gamma_Gamma) g^ss omega_H,s^2 T_H`.
  For `omega_H=ds/L_H`, this gives
  `Z_Gamma,H=T8(2 pi alpha')^2 int_CP2 e^-phi sqrt(gamma_perp) T_H`
  and `f_H^2=Z_Gamma,H/L_H`.
  The determinant factor is
  `N_Gamma^chi=sum_{alpha in ker B_Gamma^chi} sigma_alpha d_alpha tau_alpha`.
  Convention:
  `N_Gamma,1^chi=N_Gamma,2^chi=N_Gamma^chi` in the equal-amplitude
  Borel-Weil pass; the total charged supertrace over `O(1) op O(2)` is
  `2 N_Gamma^chi`.  The curvature target uses the per-pair amplitude.
- Endpoint trace evaluation:
  `G_ab^(p)=Re <0|T_a K_p T_b|0>=(Q/4) diag(1,1,0)_ab`.
  Defining `Z_Gamma,0=T8(2 pi alpha')^2 int_CP2 e^-phi sqrt(gamma_perp) Z_end`
  gives `Z_Gamma,H=(Q/4)Z_Gamma,0` and `f_Gamma^2=Z_Gamma,0/L_H`.
  For `Q=7`,
  `N_Gamma^chi/Z_Gamma,0^4=21375.716460702053... lambda_F/(w_H^8 v_EW^4)`.

## Proof Gates

1. Derive the D10 boundary/current sector on `Gamma_EW`.
2. Localize the source `L_{2,conn}^2=L_{2,vert}^2` current from `C1` and
   `F2` on `Gamma_EW`.
3. Derive the boundary image current frame from the localized action and
   prove `kappa_cur=1`.
4. Derive the local Schur auxiliary field `y`, the common coefficient
   `mu_*^2`, the sign of `-A_j A_j^dagger`, and the positive coefficient
   of the orthogonal-complement gap.
5. Derive the Hosotani/Wilson-line realization of `phi` and prove that its
   localized expansion gives the single Schur coupling with
   `beta_diag=alpha_mix^2`.
6. Derive the product-to-flag transition from retained D10 current/branch
   data.
7. Compute the one-scale effective potential selecting `lambda_*`, the
   overall compactification scale, and the D10 threshold window.
8. Derive the finite spectral-action normalization for `v_F`, `M_H`, and the
   determinant-one fermion representation.
9. Test the branched `CP2 -> S4` clue for half-integer survival and operator
   coupling.

## Evidence Already Carried Into The Manuscript

- Borel-Weil sectors: `H^0(CP1,O(2j)) ~= V_j`, `j=0,1/2,1`.
- Current zero-mode algebra: `A_j^dagger A_j = j(j+1)`.
- Schur block algebra: `[[0,A_j^dagger],[A_j,-A_j A_j^dagger]]`.
- Conditional `c=1` proposition from the single-portal hypothesis.
- Gauge-Higgs placement of the single portal and bare-Casimir normalization.
- Q-neutral photon: `Q eta_0 = 0`.
- Custodial identity: `rho_cust=1` from the same Schur pole definitions.
- Finite Connes sheet: `d_sheet=1/||Phi||`, `ell_H=sqrt(2)/v_EW`.
- Local finite potential and gauge Hessian: radial `M_H` curvature,
  `W/Z/photon` masses, and Schur image-sector separation.
- Scale bridge: `lambda_F=M_H^2/(2 v_EW^2)` and
  `mu_*^2=M_Z^2/X_+(2)`.
- Hosotani scale bridge:
  `mu_Gamma,Schur^2=mu_*^2=(g2^2+gY^2)f_H^2 theta_H,*^2/(2X_+(2))`.
- Canonical source-to-Schur anchor:
  `mu_*^2 X_+(2)=M_Z^2=(C^2 v_EW^2/4)G_EW`.
- Charged source-to-Schur consistency:
  `1/(1+u)=X_+(3/4)/X_+(2)`, hence
  `u=L2^2/LY^2=0.2871691363429836`.
- Modern scalar extension: local `sigma` mixing block in the
  `(h,sigma)` Hessian.
- Local KO6 edge: `H_rq -> H_wq`, first-order factors zero, and local
  Higgs-sector hypercharge equations.
- Connes/KK goal audit: `connes-kk-goal-completion-audit.md`.
- Global form descent: `Z6 -> Z3`.
- D8-like carrier: `Gamma_EW = M4 x CP2 x S1_Q`.
- Payen boundary action: endpoint group variable quantizes to `V_j` and
  gives Wilson-loop insertions `T_a^(j)`, `T_a^(j)T_b^(j)`.
- Payen tensor coefficient: with `A_tau=mu xi^a T_a`, the Wilson expansion
  gives `i mu T_a` and `-mu^2 T_a T_b`, hence `b=a^2` and dimensionless
  `a=1` in the orthonormal current frame after the common scale is factored.
- Boundary auxiliary placement:
  `H^0(CP1,Hom(O(0),O(2j))) = V_j` on the mixed Chan-Paton sector.
- Boundary-complex metric route:
  `E_0=O(0)`, `E_j=O(2j)`,
  `Ecal_j=Hom(E_0,E_j) ~= O(2j)`, so unitary Chan-Paton metrics give one
  Hermitian zero-mode norm for `y`, `t`, and `A_j^dagger n`.
- Line-square scale bridge:
  for `L=O(1)`, `V_1=H^0(CP1,L^2) ~= Sym^2 V_{1/2}` and a unit
  `Q`-neutral section gives a unit tensor-square vector in the neutral
  anchor channel, with doubled charges `T3=-1`, `Y=1`, and `Q=0`.
- Line-square norm fork:
  zero-mode Hilbert tensoring gives `Z_Ecal,1=Z0 I0` and `chi_Gamma=1`;
  pointwise tensor-profile integration gives `Z_Ecal,1=Z0 I2` and
  `chi_Gamma=I2/I0`.  The D8/open-boundary action must choose the former
  or derive `I2=I0`.
- Payen support for the zero-mode branch:
  canonical quantization of the endpoint degree gives a finite-dimensional
  Hilbert space carrying `R`, and the path integral gives a Wilson trace; with
  `R=V_j`, the line-square anchor sits inside the endpoint Hilbert
  representation.
- Payen orientifold endpoint reality:
  the non-oriented endpoint construction requires `R ~= R^*`.  For `SU(2)`,
  `V_{1/2}` is pseudoreal and `V_1` is real, so the retained weak sectors pass
  this source-backed reality test.  Connect the test to the concrete
  orientifold or branch involution on `Gamma_EW`.
- Shared-density gate:
  write
  `dnu_Gamma=T8(2pi alpha')^2 e^-phi sqrt(gamma_Gamma) W_Gamma d^5sigma`.
  The finite source gives `Z0 I0=int dnu_Gamma |eta0|^2`, and the
  endpoint Hilbert embedding gives the same coefficient because
  `||eta_hat0 odot eta_hat0||=1`.  Derive `W_Gamma` from the local
  frame conversion, orientifold-image factor, Chan-Paton stack data, and
  reduction normalization.
- Localized readout equality:
  with `W_s=omega_s e^-phi_s`,
  `P_sG_CP2=r_Gamma,s^2hat gamma_s`,
  `W_s r_Gamma,s^2=p_Gamma,s chi_Gamma T_Gamma,min(varrho_Gamma)`,
  `Pi_EW iota_Gamma,s^*C_1=q_Gamma theta_Gamma,s^3`,
  `P_0^Gamma theta_Gamma,s^3=(b_Gamma,s C_Gamma/W_s)^(1/2)hat e_0,s`,
  `P_h^Gamma theta_Gamma,s^3=(b_Gamma,s rho_Gamma,s C_Gamma/W_s)^(1/2)hat e_h,s`,
  diagonal `B_sigma`, and
  `B_chi^dagger B_chi=(z_chi/L_H)^2 1_E_chi`, the extracted residuals
  are `R_T=R_x=R_varrho=R_epsilon=R_g=R_chi=0`.  The remaining global
  derivation is the flux-quantized type-I' extension and the boundary
  Dirac-Dolbeault origin of `B_sigma,B_chi`.
- Global extension split:
  the article now records
  `R_per,s=q_Gamma ell_Gamma,s/(2pi)-n_Gamma,s-nu_Gamma,s` and the
  endpoint spectral residual `R_DD` for `D_partial,Gamma^(7)`.  The
  completion row is `R_per,s=0`, `R_DD=0`, and `Q_lower^tot=0`.
- Image projector:
  `P_im^(j)=J^-1 A_j A_j^dagger` for `J>0`, with
  `V_j otimes V_1 = V_{j+1} + V_j + V_{j-1}` and `Im A_j ~= V_j`.
  Equivalently, for `B_j=sum_a T_a^(j) otimes S_a^(1)`,
  `P_im^(j)=-((B_j-j)(B_j+j+1))/(j(j+1))`.
- Orthogonal-complement projector:
  `P_perp^(j)=1-P_im^(j)=B_j(B_j+1)/(j(j+1))`, giving the canonical
  local gap term `M_perp^2 <n,P_perp n>`.
- Complement spectral-gap route:
  a self-adjoint localized boundary-complex Laplacian with kernel `Im A_j`
  gives positive `lambda_perp,j` on the compact `P_perp` sector.
- Shared-density complement ratio:
  with `H_Gamma,j=L2(Gamma_EW,int,dnu_Gamma) tensor (V_j tensor V_1)`,
  `P_perp` acts fibrewise and
  `M_perp,j^2=inf <n,Delta_Gamma,j n>_Gamma` over normalized complement
  modes.  The remaining finite number is
  `r_perp,j=M_perp,j^2/mu_Gamma^2>0`, provided
  `ker Delta_Gamma,j=Im A_j`.
- Weak-length split:
  `L_{2,Gamma}^2 = L_{2,horiz}^2 + L_{2,vert}^2`.
- Neutral integral extraction:
  `I_AB^Gamma=int dnu_Gamma gamma_Gamma^-1(theta_Gamma^A,theta_Gamma^B)`
  for `A,B in {3,Y}` gives `L_2^2=I_33`, `L_Y^2=I_YY`,
  `epsilon_Gamma=I_3Y`, `u=I_33/I_YY`, and
  `chi_Gamma=I_3Y/sqrt(I_33 I_YY)`.  The same triple gives
  `alpha_Gamma`, `M_W`, and `M_Z`.
- Rank-two neutral requirement:
  if `theta_Gamma^Y=c theta_Gamma^3`, then `det L_Gamma=0`.
  The `S1_Q` factor supplies photon protection; finite `G_Z^Gamma`
  requires a second current direction from the `CP2`, Chan-Paton, or
  boundary-complex sector.
- Rank-two neutral normal form:
  with `theta_Gamma^3=a_Gamma e_Q+b_Gamma e_N` and
  `theta_Gamma^Y=c_Gamma e_Q-b_Gamma e_N`, one obtains
  `theta_Gamma^Q=(a_Gamma+c_Gamma)e_Q`,
  `det L_Gamma=b_Gamma^2(a_Gamma+c_Gamma)^2`,
  `G_Z^Gamma=1/b_Gamma^2`, and
  `b_Gamma^2=R_dV L_2^2`.
- Neutral-line projection:
  `L_N=L_T3^-1 tensor L_Y` has boundary current
  `theta_Gamma^N=theta_Gamma^Y-theta_Gamma^3`; the massive neutral
  direction is
  `e_N=-P_Qperp theta_Gamma^N/||P_Qperp theta_Gamma^N||`, and the
  pass condition becomes
  `||P_Qperp theta_Gamma^N||^2=4 R_dV L_2^2`.
- Projection determinant identity:
  `||P_Qperp theta_Gamma^N||^2=4 det L_Gamma/L_Q^2`; equivalently
  `det L_Gamma=R_dV L_2^2 L_Q^2`.
- Neutral line class target:
  `c1(L_N)=c1(L_Y)-c1(L_T3)=6(h+eta)`, and the physical pass is
  `N_N^Gamma/(4 L_2^2)=R_dV` with
  `N_N^Gamma=int dnu_Gamma gamma_Gamma^-1(P_Qperp theta_N,
  P_Qperp theta_N)`.
- Boundary Hodge-matrix target:
  with `omega_T=omega_eta`, `omega_Y=6 omega_h+7 omega_eta`,
  `omega_N=6(omega_h+omega_eta)`, and `omega_Q=6 omega_h+8 omega_eta`,
  compute `N_N^Gamma=<omega_N,omega_N>-<omega_N,omega_Q>^2/<omega_Q,omega_Q>`
  from `H_ij^Gamma`; for `A=H_hh`, `B=H_heta`, `C=H_etaeta`, this equals
  `36(AC-B^2)/(9A+24B+16C)`, and the pass equation is
  `9(AC-B^2)/(9A+24B+16C)=R_dV L_2^2`.
- Weak-current Hodge specialization:
  if `L_2^2=H_etaeta`, then
  `9(r_H-s_H^2)/(9r_H+24s_H+16)=R_dV`, with
  `r_H=H_hh/H_etaeta`, `s_H=H_heta/H_etaeta`; the diagonal case gives
  `H_hh/H_etaeta=16R_dV/(9(1-R_dV))=6.190...`.
- Bulk KLT control metric:
  `h=x+y`, `eta_harm=-x/2+y/2+z`,
  `||x||^2=||y||^2~lambda^(1/2)`, `||z||^2~lambda^(-3/2)`, hence
  `r_H^bulk=4lambda^2/(lambda^2+2)` and `s_H=0`; this reaches
  `2.666...` at the top of the KLT interval.  The boundary pass therefore
  needs a localized measure or frame factor.  With
  `L_2^2=kappa_H C_bulk`, one gets
  `kappa_H=9lambda^2/(R_dV(13lambda^2+8))`.
- Boundary representative shift:
  for `eta(t)=t(x+y)+y+z` and `q=lambda^2`,
  `A=2q`, `B=(2t+1)q`, `C=(2t^2+2t+1)q+1`, and the `L_2^2=C` pass equation is
  `9q(q+2)=2R_dV(16qt^2+40qt+29q+8)(q(2t^2+2t+1)+1)`.
  With `s=t+7/8`, this becomes
  `F0(q)-2R_dV q(7q+32)s^2-64R_dV q^2s^4=0`, where
  `F0(q)=(576q^2+1152q-R_dV(625q^2+1600q+1024))/64`. Real roots occur for
  `q>=q_c`, with
  `q_c=32(25R_dV+18 sqrt(1-R_dV)-18)/(576-625R_dV)=3.511614004347...`,
  hence `lambda_c=1.873930095907...`; inside the KLT interval, the pass range
  is `lambda_c<=lambda<=2`. The remaining task is to derive `t` from the
  localized boundary representative.
- Weak-current frame-factor fork:
  with `L_2^2=kappa_H C`,
  `kappa_H(q,t)=9q(q+2)/(2R_dV(16qt^2+40qt+29q+8)(q(2t^2+2t+1)+1))`;
  its maximum over the representative family occurs at `t=-7/8` and equals
  `kappa_H^max(q)=576q(q+2)/(R_dV(25q+32)^2)`.  The equation
  `kappa_H^max=1` recovers `q_c`; lower `lambda` values require
  `0<kappa_H<=kappa_H^max`.
- Boundary-weight source for `t=-7/8`:
  if `h=x+y`, `eta(t)=t x+(t+1)y+z`, and the localized horizontal Hodge metric
  has weights `w_x,w_y` with no cross term, then
  `<eta(t),h>_partial=0` gives `t=-w_y/(w_x+w_y)`.  The center
  `t=-7/8` is equivalent to `w_y:w_x=7:1`.  Derive or reject this split from
  the localized current, Chan-Paton, or Chern-Weil metric.
- Weak-period source for the `7:1` split:
  setting `w_y:w_x=Q:1` gives `t_Q=-Q/(Q+1)`.  With the primitive
  line-lattice relation `P=Q-1`, the retained class
  `zeta=P h+Q eta(t_Q)` becomes
  `zeta=Q(y+z)-h/(Q+1)`.  For `Q=7`,
  `zeta=7(y+z)-h/8`, hence `8 zeta=56(y+z)-h`.  Test whether the
  D8-like boundary complex derives the `Q+1=8` lift.
- D8/O8 half-rank match:
  with `N8=2n`, `q8_net=N8-16=2(n-8)`, and `k=n-8`, the identification
  `n=Q+1` sends `Q=7` to `n=8`, `N8=16`, `q8_net=0`, and `k=0`.  Test whether
  the boundary Chan-Paton complex derives `n=Q+1`.
- Borel-Weil half-rank source:
  if the Chan-Paton half-stack is the weak-period zero-mode space
  `H^0(CP1,O(Q))`, then `n=dim H^0(CP1,O(Q))=Q+1`.  For `Q=7`, this gives
  `N8=2 dim H^0(CP1,O(7))=16`, matching the neutral D8/O8 endpoint.
- Point-evaluation filtration source:
  for a boundary point `p in CP1`,
  `0 -> O(Q-1) -> O(Q) -> O(Q)|_p -> 0` gives
  `0 -> H^0(O(Q-1)) -> H^0(O(Q)) -> O(Q)|_p -> 0`, hence
  `dim ker(ev_p)=Q` and `dim im(ev_p)=1`.  An endpoint trace metric gives
  `w_y:w_x=Q:1`; for `Q=7`, this derives the `7:1` split, `t_Q=-7/8`,
  the eightfold lift, and the same half-rank `n=Q+1`.
- Reduced pass equation:
  substituting `t_Q=-Q/(Q+1)` gives
  `9q(q+2)=2 R_dV (q(5Q^2+18Q+29)/(Q+1)^2+8)(q(Q^2+1)/(Q+1)^2+1)`.
  For `Q=7`, `576q(q+2)=R_dV(25q+32)^2`, so
  `q_c=3.511614004347...` and `lambda_c=1.873930095907...`.
- Electromagnetic length consequence:
  with `P=Q-1`, `omega_T=eta(t_Q)`,
  `omega_Y=(Q-1)h+Q eta(t_Q)`, and
  `omega_Q=(Q-1)h+(Q+1)eta(t_Q)`.  The shifted Hodge entries are
  `A=2q`, `B=-(Q-1)q/(Q+1)`, and
  `C=(Q^2+1)q/(Q+1)^2+1`.  In the weak-current specialization
  `L_2^2=C`, the photon length is
  `L_Q^2=(Q-1)^2A+2(Q-1)(Q+1)B+(Q+1)^2C=(Q+1)^2L_2^2`.
  For `Q=7`, this gives `L_Q^2=64L_2^2`.  The determinant identity
  `det L_Gamma=(Q-1)^2q(q+2)=R_dV L_2^2L_Q^2` recovers the reduced
  `Q` equation.  Full alpha closure requires the complete localized
  electromagnetic matrix, including CP2, Chan-Paton, image, or frame terms.
- Scale and Schur row:
  on the neutral pass surface,
  `G_Z^Gamma=L_Q^2/det L_Gamma=1/(R_dV L_2^2)`.  Writing `C_W` for the
  Weinberg length-normalization constant,
  `M_W^2=C_W^2 v_EW^2/(4L_2^2)` and
  `M_Z^2=C_W^2 v_EW^2/(4R_dV L_2^2)`.  Since
  `R_dV=X_+(3/4)/X_+(2)`, the local Schur coefficient is
  `mu_Gamma^2=M_Z^2/X_+(2)=M_W^2/X_+(3/4)
  =C_W^2 v_EW^2/(4X_+(3/4)L_2^2)`.  The same row gives
  `alpha_Gamma=C_W^2/(4pi(Q+1)^2L_2^2)
  =M_W^2/(pi(Q+1)^2v_EW^2)`.
- Alpha filter:
  for `Q=7`, the point-evaluation row gives
  `alpha_Gamma=M_W^2/(64 pi v_EW^2)`.  With representative inputs
  `M_W=80.377 GeV`, `v_EW=246.21965 GeV`, this gives
  `alpha_Gamma^{-1}=1886.738366864...`.  The physical input
  `alpha^{-1}=137.035999084...` corresponds to
  `k_alpha=M_W^2/(pi alpha v_EW^2)=4.648394337766...`, so the row has
  `k_Q/k_alpha=13.768195069001...`.  Full alpha closure needs an effective
  factor `r_Q=k_alpha/64=0.072631161528...` in the electromagnetic current
  norm.
- Alpha-closed neutral matrix target:
  setting `L_2^2=1`, `k=k_alpha`, and
  `Lhat_Gamma=[[1,epsilon],[epsilon,y]]`, the alpha and de Vries conditions
  are `1+y+2epsilon=k` and `y-epsilon^2=R_dV k`.  Thus
  `epsilon_pm=-1 +/- sqrt(k(1-R_dV))` and
  `y_pm=k+1 -/+ 2sqrt(k(1-R_dV))`.  Numerically
  `sqrt(k_alpha(1-R_dV))=1.018362864274...`.  The two positive branches are
  `epsilon=0.018362864274...`, `y=3.611668609219...`,
  `chi=0.009662432587...`, and
  `epsilon=-2.018362864274...`, `y=7.685120066313...`,
  `chi=-0.728071311237...`.
- Correction matrix diagnostic:
  at the point-evaluation neutral root, normalized by `L_2^2=1`,
  `Lhat_pt=[[1,2.778688215142...],
  [2.778688215142...,57.442623569715...]]`.  Subtracting this row from the
  alpha-closed `+` branch gives eigenvalues
  `0.141172793435...` and `-53.972127753932...`; subtracting it from the
  `-` branch gives `0.458256512522...` and `-50.215760015924...`.  Therefore
  a positive additive `Q`-norm term is excluded as the alpha-closure
  mechanism; the missing effect must be a projection, quotient, frame
  renormalization, image subtraction, or destructive cross term.
- Rank-one projection/rescaling target:
  each alpha-closed target satisfies
  `T_pm=(Lhat_pt-D_pm)/s_pm` with `D_pm>=0` and `rank D_pm=1`.  The `+`
  branch has `s_+=0.859516413258733...`,
  `eig(D_+)={0,54.478818707582...}`, and image-line slope
  `19.667102015222...`.  The `-` branch has
  `s_-=0.672682628439277...`,
  `eig(D_-)={0,52.600294175197...}`, and image-line slope
  `12.637293988103...`.  The localized `Gamma_EW` action has to derive this
  rank-one subtraction plus common current-frame rescaling from endpoint image,
  quotient, or DBI/CS current data.
- One-field boundary auxiliary row:
  with `J=(J3,JY)`,
  `S_img^(2)=1/2 J^T Lhat_pt J+r_img ell_pm^T J+1/2 m_pm r_img^2`.
  Eliminating `r_img` gives
  `T_pm=s_pm^-1(Lhat_pt-ell_pm ell_pm^T/m_pm)`.  Equivalently
  `ell_pm ell_pm^T/m_pm=delta_pm(1,rho_pm)^T(1,rho_pm)`.  The coefficient
  targets are
  `(+): s=0.859516413258733..., s^-1=1.163444914575446...,
  delta=0.140483586741..., rho=19.667102015222...` and
  `(-): s=0.672682628439277..., s^-1=1.486585140930646...,
  delta=0.327317371561..., rho=12.637293988103...`.
- Weak-period source-line test:
  `(1,rho_pm)=((1+rho_pm)/2)(1,1)+((rho_pm-1)/2)(-1,1)`, so
  `nu_pm=(rho_pm-1)/(rho_pm+1)`.  The branches give
  `nu_+=0.903227844982...` and `nu_-=0.853343339101...`.  The weak-period
  point-evaluation line has `rho_Q=2Q+1=15` and
  `nu_Q=Q/(Q+1)=7/8=0.875`.  The alpha length condition gives
  `delta(rho)=(64-k_alpha)/((1+rho)^2-k_alpha)`.  At `rho=15`, this gives
  `delta=0.236129805122...` and determinant ratio
  `Rcal(15)=0.999999862211...`, versus
  `R_dV=0.776898677699...`.  Thus the bare weak-period source line is a
  rejected single-auxiliary subcase.  A viable one-field localized action has
  to derive `rho_+` or `rho_-`.
- Source-slope equation:
  set `c_rho=(1,rho)^T` and
  `M_rho=Lhat_pt-delta(rho)c_rho c_rho^T`.  The requirements
  `(1,1)M_rho(1,1)^T=k_alpha(M_rho)_33` and
  `det M_rho=R_dV k_alpha(M_rho)_33^2` give the polynomial
  `P_rho(rho)=rho^4-29.874189325032...rho^3
  +170.407256725780...rho^2+591.897671281551...rho
  +93.118987613750...`.  Its roots are
  `-2.264774980142...`, `-0.165431698151...`,
  `12.637293988103...`, and `19.667102015221...`.  The negative roots have
  `delta(rho)<0`; positive Schur subtraction keeps the two positive roots.
- Auxiliary coupling extraction:
  with positive image mass `m>0`, the localized coefficients obey
  `ell_3^2/m=delta`, `ell_Y/ell_3=rho`, and `s=(M_rho)_33=1-delta`.
  The additive roots have
  `rho=-0.165431698151..., delta=-15.018536535911...` and
  `rho=-2.264774980142..., delta=-19.467594207010...`.
  The Schur roots have
  `rho_+=19.667102015221..., delta_+=0.140483586741..., s_+=0.859516413259...`
  and
  `rho_-=12.637293988103..., delta_-=0.327317371561..., s_-=0.672682628439...`.
- Image-mode extraction formula:
  choose a normalized localized image eigenmode `psi` with
  `int_Gamma dnu_Gamma |psi|^2=1` and
  `m_psi=<psi,M_img psi>_Gamma`.  Let
  `J_A=gamma_Gamma^-1(theta_Gamma^A,Theta_img)` for `A=3,Y` and
  `ell_A[psi]=int_Gamma dnu_Gamma psi J_A`.  The dimensionless invariants are
  `delta_psi=ell_3[psi]^2/(m_psi L_2^2)`,
  `rho_psi=ell_Y[psi]/ell_3[psi]`, and `s_psi=1-delta_psi`.  The localized
  action has to return one of the two Schur triples
  `(0.140483586741...,19.667102015221...,0.859516413259...)` or
  `(0.327317371561...,12.637293988103...,0.672682628439...)`.
- Image Green-kernel form:
  define `D_AB=L_2^-2 <J_A,M_img^-1 J_B>_Gamma` for `A,B=3,Y`.
  Integrating out the image sector gives `K_eff=K_pt-L_2^2 D`.  The one-field
  Schur row is the rank-one case `D_33 D_YY-D_3Y^2=0` with `D_33>0`.
  The two target matrices are
  `D_+=[[0.140483586741...,2.762905031905...],
  [2.762905031905...,54.338335120840...]]` and
  `D_-=[[0.327317371561...,4.136405851826...],
  [4.136405851826...,52.272976803636...]]`.
- Spectral rank diagnostic:
  with `M_img psi_n=m_n psi_n`, `m_n>0`, and
  `ell_A^(n)=int_Gamma dnu_Gamma psi_n J_A`, the correction matrix is
  `D_AB=sum_n ell_A^(n)ell_B^(n)/(m_n L_2^2)`.  Setting
  `u_n=(ell_3^(n),ell_Y^(n))/(L_2 sqrt(m_n))` gives
  `D=sum_n u_n u_n^T` and
  `Delta_rank=D_33 D_YY-D_3Y^2
  =sum_{n<m}(u_n^3 u_m^Y-u_n^Y u_m^3)^2`.  The local spectrum passes a
  Schur branch when `Delta_rank=0` and
  `(D_33,D_3Y/D_33)` equals `(delta_+,rho_+)` or `(delta_-,rho_-)`.
  Multiple localized image modes can contribute when their source-slope ratio
  is common and their strengths add to the selected `delta`.
- Green-metric source factorization:
  define `(F,G)_G=L_2^-2 <F,M_img^-1 G>_Gamma`, so `D_AB=(J_A,J_B)_G`.
  For branch `sigma in {+,-}`, the exact target is
  `D^(sigma)=delta_sigma (1,rho_sigma)^T(1,rho_sigma)`.  Equivalently,
  `||J_Y-rho_sigma J_3||_G^2=0` and `||J_3||_G^2=delta_sigma`.
  With a positive image Green metric, the local calculation reduces to
  source proportionality in the sourced image quotient plus the weak-source
  norm.
- Weak-period source-line consequence:
  a pure weak-period image source has `J_Y=rho_Q J_3`, `rho_Q=2Q+1`, hence
  `D=delta_Q(1,rho_Q)^T(1,rho_Q)`.  For `Q=7`, `rho_Q=15`.  The Schur
  branches require `rho_D=12.637293988103...` or `19.667102015221...`.
  With the alpha-length value,
  `delta_Q=(64-k_alpha)/((1+rho_Q)^2-k_alpha)=0.236129805122...` and
  `Rcal(15)=0.999999862211...`.  Required sourced-image options: deform to
  `rho_-`, deform to `rho_+`, or project the weak-period source away from the
  Schur image channel.
- Coframe deformation target:
  using `delta_Q` as reference, write
  `J_3^(sigma)=a_sigma J_3^(Q)` and
  `J_Y^(sigma)=a_sigma(rho_Q+zeta_sigma)J_3^(Q)`.  Branch matching gives
  `zeta_sigma=rho_sigma-rho_Q` and `a_sigma^2=delta_sigma/delta_Q`.
  For `Q=7`, the `+` branch target is
  `(zeta_+,a_+^2,a_+)=(4.667102015221...,0.594942204219...,0.771324966677...)`.
  The `-` branch target is
  `(zeta_-,a_-^2,a_-)=(-2.362706011897...,1.386175588431...,1.177359583318...)`.
- Source-coframe matrix form:
  with `C_Q=(J_3^(Q),J_Y^(Q))^T`, use
  `C_sigma=R_sigma C_Q`,
  `R_sigma=a_sigma [[1,0],[zeta_sigma,1]]`.  This gives
  `R_sigma(1,rho_Q)^T=a_sigma(1,rho_sigma)^T` and
  `R_sigma D_Q R_sigma^T=D_sigma`.  For `Q=7`,
  `R_+=[[0.771324966677...,0],
  [3.599852306368...,0.771324966677...]]` and
  `R_-=[[1.177359583318...,0],
  [-2.781754565670...,1.177359583318...]]`.
  The lower-left entry is the localized `T3`-to-`Y` source mixing target.
- Pullback coframe target:
  inside the image source quotient,
  `theta_Gamma,sigma^3=a_sigma theta_Gamma,Q^3` and
  `theta_Gamma,sigma^Y=a_sigma(theta_Gamma,Q^Y
  +zeta_sigma theta_Gamma,Q^3)`.  Equivalently,
  `Z_img^(sigma)=a_sigma^2 Z_img^(Q)` and
  `beta_Y3^(sigma)=zeta_sigma`.  For `Q=7`, the `+` branch needs
  `(Z_img^(+)/Z_img^(Q),beta_Y3^+)=(0.594942204219...,4.667102015221...)`.
  The `-` branch needs
  `(Z_img^(-)/Z_img^(Q),beta_Y3^-)=
  (1.386175588431...,-2.362706011897...)`.
- Green projection extraction:
  compute `delta_hat_G=D_33`, `rho_hat_G=D_3Y/D_33`, and
  `epsilon_hat_G^2=(D_33 D_YY-D_3Y^2)/D_33^2`.  The Schur-branch pass is
  `(delta_hat_G,rho_hat_G,epsilon_hat_G^2)=(delta_sigma,rho_sigma,0)`.
  Then `a_sigma^2=delta_hat_G/delta_Q` and
  `zeta_sigma=rho_hat_G-rho_Q`.  Direct pullback readout:
  `Z_hat_img=D_33`, `beta_hat_Y3=D_3Y/D_33-rho_Q`, and
  `E_hat_perp=D_YY-D_3Y^2/D_33`.  Branch pass:
  `Z_hat_img/Z_img^(Q)=a_sigma^2`, `beta_hat_Y3=zeta_sigma`, and
  `E_hat_perp=0`.  A projected-image realization uses a
  `G`-self-adjoint idempotent `Pi_sigma` with
  `Pi_sigma J_Y=rho_sigma Pi_sigma J_3` and
  `||Pi_sigma J_3||_G^2=delta_sigma`.
- Induced source-metric block:
  `H_sigma=R_sigma R_sigma^T
  =a_sigma^2[[1,zeta_sigma],[zeta_sigma,1+zeta_sigma^2]]`,
  `det H_sigma=a_sigma^4`, and
  `chi_sigma=zeta_sigma/sqrt(1+zeta_sigma^2)`.  For `Q=7`,
  `H_+=[[0.594942204219...,2.776655960251...],
  [2.776655960251...,13.553878831880...]]`, with
  `chi_+=0.977806418243...`.  Also
  `H_-=[[1.386175588431...,-3.275125396331...],
  [-3.275125396331...,9.124334052058...]]`, with
  `chi_-=-0.920912188652...`.  Plus branch trace:
  `(H_+)_3Y=2.776655960251...` sits near
  `(Lhat_pt)_3Y=2.778688215142...`, mismatch
  `Delta_3Y=0.002032254891...`.
- Canonical one-field packet:
  write `S_img,sigma^(2)=1/2 m_sigma r_sigma^2
  +L_2 sqrt(m_sigma) r_sigma g_sigma^T J`, with
  `g_sigma=sqrt(delta_sigma)(1,rho_sigma)^T`.  Eliminating `r_sigma` gives
  `-1/2 L_2^2 J^T g_sigma g_sigma^T J`, hence
  `D_sigma=g_sigma g_sigma^T`.  The branch vectors are
  `g_+=(0.374811401563...,7.371454070999...)` and
  `g_-=(0.572116571654...,7.230005311453...)`.
- Image-profile overlap target:
  for normalized `psi_sigma` with `M_img psi_sigma=m_sigma psi_sigma`,
  the image profile has to obey
  `int_Gamma dnu_Gamma psi_sigma gamma_Gamma^-1(theta_Gamma^A,Theta_img,sigma)
  =L_2 sqrt(m_sigma)(g_sigma)_A`, `A=3,Y`.  With
  `Xi_sigma=Theta_img,sigma/sqrt(m_sigma)`, this becomes
  `L_2^-1 int_Gamma dnu_Gamma psi_sigma
  gamma_Gamma^-1(theta_Gamma^A,Xi_sigma)=(g_sigma)_A`.
  Define
  `G_AB^(psi)=int_Gamma dnu_Gamma psi_sigma^2
  gamma_Gamma^-1(theta_Gamma^A,theta_Gamma^B)`.  For invertible `G^(psi)`,
  `Xi_sigma=L_2 psi_sigma c_sigma^B theta_Gamma,B` with
  `c_sigma^B=(G^(psi)^-1)^{BA}(g_sigma)_A` solves the overlap equations.
  With `G^(psi)=[[A_psi,B_psi],[B_psi,C_psi]]` and
  `Delta_psi=A_psi C_psi-B_psi^2`,
  `c_sigma^3=(C_psi(g_sigma)_3-B_psi(g_sigma)_Y)/Delta_psi` and
  `c_sigma^Y=(-B_psi(g_sigma)_3+A_psi(g_sigma)_Y)/Delta_psi`.  In an
  orthonormal weighted current frame, `Xi_sigma=L_2 psi_sigma[
  (g_sigma)_3 theta_Gamma^3+(g_sigma)_Y theta_Gamma^Y]`.
- Minimal-norm image profile:
  decompose `Xi_sigma=Xi_sigma,min+Xi_sigma,perp`, with
  `int_Gamma dnu_Gamma psi_sigma gamma_Gamma^-1(theta_Gamma^A,Xi_sigma,perp)=0`.
  The forced profile norm is
  `||Xi_sigma,min||_Gamma^2/L_2^2=g_sigma^T G^(psi)^-1 g_sigma`.
  In an orthonormal weighted current frame, the branch values are
  `54.478818707582...` and `52.600294175197...`.  Nonzero orthogonal image
  content raises the image-profile norm without changing the Schur matrix.
  Profile residual:
  `R_Xi,sigma=||Xi_sigma,perp||_Gamma^2/||Xi_sigma,min||_Gamma^2`.
  The minimal image-source realization has `R_Xi,sigma=0`; a positive value
  records extra localized image content to explain from the D8/O8 spectrum.
- One-mode closure:
  after fixing the orientation of `r_sigma`, a positive one-mode image sector
  over `Gamma_EW` realizes
  `D_sigma=delta_sigma(1,rho_sigma)^T(1,rho_sigma)` precisely when
  `L_2^-1 int_Gamma dnu_Gamma psi_sigma
  gamma_Gamma^-1(theta_Gamma^A,Xi_sigma)=(g_sigma)_A`, `A=3,Y`.
  The overlap vector is
  `ell_A=L_2 sqrt(m_sigma)(g_sigma)_A`, so integrating out `r_sigma` gives
  `D_AB=ell_A ell_B/(m_sigma L_2^2)=(g_sigma)_A(g_sigma)_B`.
  Remaining D8/O8 data: `psi_sigma`, `Theta_img,sigma`, and `R_Xi,sigma`.
- Minimal local realization data:
  `P_Gamma,sigma=(dnu_Gamma,psi_sigma,m_sigma,Xi_sigma,G^(psi),
  Z_Gamma,0,N_Gamma^chi)`.
  Required readouts:
  `int_Gamma dnu_Gamma |psi_sigma|^2=1`,
  `M_img psi_sigma=m_sigma psi_sigma`, `m_sigma>0`,
  `L_2^-1 int_Gamma dnu_Gamma psi_sigma
  gamma_Gamma^-1(theta_Gamma^A,Xi_sigma)=(g_sigma)_A` for `A=3,Y`,
  `R_Xi,sigma=0`, `Z_Gamma,H=(Q/4)Z_Gamma,0`, and
  `N_Gamma^chi=2 sigma_chi d_chi F(z)`.
  Compact worksheet for the single localized D8/O8 computation.
- Quadratic master form:
  `S_Gamma^(2)=int_M4[-1/4 K_AB^Gamma F_A F_B
  +1/2(f_H^2)_ab partial theta_H^a partial theta_H^b
  +1/2<r,M_img r>_Gamma+L_2 j_A<r,J_A>_Gamma
  +1/2 Str_chi log B_Gamma^chi(theta_H)]`.
  It reads out
  `K_AB^Gamma=int dnu_Gamma gamma_Gamma^-1(theta_Gamma^A,theta_Gamma^B)`,
  `D_AB=L_2^-2<J_A,M_img^-1J_B>_Gamma`,
  `Z_Gamma,H=(Q/4)Z_Gamma,0`, and
  `N_Gamma^chi=2 sigma_chi d_chi F(z)`.
  Single-pass target:
  `(D_AB,Z_Gamma,H/Z_Gamma,0,N_Gamma^chi)
  =(D_sigma,Q/4,2 sigma_chi d_chi F(z))`.
- DBI sector-sum measure:
  label the retained D8 image sectors after the O8 projection by `S_Gamma`.
  The DBI expansion gives
  `dnu_Gamma,s=kappa_8 omega_s e^-phi_s sqrt(gamma_Gamma,s)d^5sigma`.
  The common inner product is
  `<X,Y>_Gamma=sum_s int dnu_Gamma,s gamma_s^mn
  tr_Es(Pi_s X_m,s Pi_s Y_n,s)`.  Hence
  `K_AB^Gamma=<theta_Gamma^A,theta_Gamma^B>_Gamma`,
  `G_AB^(psi)=<psi_sigma theta_Gamma^A,
  psi_sigma theta_Gamma^B>_Gamma`,
  `Z_Gamma,0=<eta_0,eta_0>_Gamma`, and
  `M_img=Q_Gamma,sigma^dagger Q_Gamma,sigma` with this adjoint.
- Retained D8/O8 sector assignment:
  take the weak-period Chan-Paton half-stack
  `W_Q=H0(CP1,O(Q))`, `dim W_Q=Q+1`, and the orientifold-real double
  `E_Q=(W_Q op W_Q^vee)^Omega`.  At `Q=7`, this gives
  `rk_C(E_Q^C)=16`, `q_8^net=16-16=0`, and `k=16/2-8=0`.
  The row projectors are
  `Pi_Q=P_Omega P_E_Q`, `Pi_sigma=|e_sigma><e_sigma|`, and
  `Pi_chi=P_1^chi+P_2^chi`, with
  `P_1^chi=proj_span{u,v}` and `P_2^chi=proj_span{u^2,v^2}`.
  The row inner product is
  `<X,Y>_{Gamma,Pi}=int dmu_Gamma gamma^mn tr_Hloc(Pi X_m Pi Y_n)`.
- Orientifold reality row:
  for `H_n=H0(CP1,O(n))` with `e_k=u^{n-k}v^k`, define
  `J_n e_k=(-1)^k e_{n-k}`.  Then `J_n^2=(-1)^n`, so `n=1` is
  pseudoreal and `n=2` is real.  On the doubled endpoint,
  `Omega_n(s,lambda)=(J_n^-1 lambda,J_n s)`, `Omega_n^2=1`.
  The charged bases obey `J_1u=v`, `J_1v=-u`, `J_2u^2=v^2`,
  `J_2uv=-uv`, and `J_2v^2=u^2`.  Therefore
  `Tr P_Omega,1 P_1^chi=2` and `Tr P_Omega,2 P_2^chi=2`;
  orientifold survival contributes `alpha_parity=0` and `d_1=d_2=d_chi`.
- Charged oscillator determinant row:
  set `x=w_H theta_H`.  The localized charged oscillator has circle spectrum
  `lambda_{ell,r}(x)=p_E^2+M_chi^2+(2pi ell+rx)^2/L_H^2`,
  `ell in Z`, for charges `r=1,2`.  The Euclidean complex-boson Gaussian
  fixes `sigma_chi=+1`.  Poisson resummation gives
  `V_chi(x)=(3/(4pi^2 L_H^4))2d_chi sum_{m>=1}F(mz_chi)
  (cos(mx)+cos(2mx))/m^5`, with `z_chi=M_chi L_H`.
  Hence `N_Gamma^chi=2d_chi F(z_chi)`, and for `d_chi=1`,
  `M_chi=L_H^-1 F^-1(N_Gamma^chi/2)`.
- RR/current coframe extraction row:
  split retained coframes by
  `theta_Gamma^A=theta_Gamma,CP^A+q_A^-1 Pi_A iota_Gamma^*C_1`,
  `A=3,Y`, with
  `d_Gamma theta_Gamma^A=d_Gamma theta_Gamma,CP^A
  +q_A^-1 Pi_A iota_Gamma^*F_2`.  The weak triplet pass is
  `<theta_Gamma^a,theta_Gamma^b>_{Gamma,Pi_Q}
  =L_{2,Gamma}^2 delta^ab`.
  The neutral current matrix is
  `L_Gamma=[[K_33,K_3Y],[K_3Y,K_YY]]`,
  `K_AB=<theta_Gamma^A,theta_Gamma^B>_{Gamma,Pi_Q}`.
  Then `theta_Gamma^Q=theta_Gamma^3+theta_Gamma^Y`,
  `L_Q^2=(1,1)L_Gamma(1,1)^T`, and the neutral branch test is
  `det L_Gamma=R_dV K_33 L_Q^2`.
- CS source polynomial row:
  `S_CS^Gamma=mu8 sum_s epsilon_s int_Gamma_s sum_r C_{9-2r}
  wedge [Y_Gamma,s]_{2r}`, with
  `Y_Gamma,s=ch(Fcal_s)sqrt(Ahat(TGamma_s)/Ahat(NGamma_s))`.
  On the active spin-c CP2 row,
  `Fcal_Q/(2pi)=f_m h_Q`, `f_m=m+13/2`, and
  `Y_Gamma=N8[1+f_m h_Q+(f_m^2/2-1/16)h_Q^2]`.
  The `C_1` variation gives
  `qfrak_C1=N8(f_m^2/2-1/16)`, hence `qfrak_C1=337` for
  `m=0`, `N8=16`.  With
  `I_{1,A}^Gamma=Pi_A(qfrak_C1 ds_Q)+I_{1,A}^O8+I_{1,A}^bulk`,
  compact solvability imposes
  `<I_{1,A}^Gamma,omega_Q>_Gamma=0`.  The Green source is the
  zero-mode-subtracted one-form `I_{1,A}^perp`.  The projected one-form solve
  is `Pi_A iota_Gamma^*C_1=Pi_A C_{1,harm}
  +mu8 G_{1,Gamma}I_{1,A}^perp`, leading to the vertical-length readout
  `L_{2,vert}^2=q_3^-2||Pi_3 C_{1,harm}
  +mu8 G_{1,Gamma}I_{1,3}^perp||_{Gamma,Pi_Q}^2`.
- Finite Green coframe readout:
  choose one-form eigenmodes
  `<alpha_i,alpha_j>_{Gamma,Pi_Q}=delta_ij` and
  `Delta_{1,Gamma}alpha_i=lambda_i alpha_i`, with `lambda_i>0`.
  Define `B_Ai=<alpha_i,I_{1,A}^perp>`, `P_Ai=<alpha_i,theta_Gamma,CP^A>`,
  `Pi_A C_{1,harm}=h_A omega_Q`,
  `Omega_Q=<omega_Q,omega_Q>`, and
  `p_A=<theta_Gamma,CP^A,omega_Q>`.  Then
  `G_{1,Gamma}I_{1,A}^perp=sum_i B_Ai lambda_i^-1 alpha_i`.
  The current matrix becomes the finite spectral expression with entries
  `K_AB^CP+q_A^-1 h_A p_B+q_B^-1 h_B p_A
  +q_A^-1q_B^-1 h_Ah_B Omega_Q
  +mu8 q_A^-1 sum_i B_AiP_Bi/lambda_i
  +mu8 q_B^-1 sum_i B_BiP_Ai/lambda_i
  +mu8^2q_A^-1q_B^-1 sum_i B_AiB_Bi/lambda_i^2`.
- `S1_Q` Fourier source test:
  on the product zero-mode reduction, write
  `I_{1,A}^Gamma=rho_A(varphi)ds_Q`,
  `ds_Q=R_Qdvarphi`, and `L_Q=2pi R_Q`.  The compact condition removes
  `bar rho_A`, leaving
  `rho_A^perp=sum_{n>=1}(a_A,n cos nvarphi+b_A,n sin nvarphi)` with
  `lambda_n=(2pi n/L_Q)^2`.  The Green-current contribution is
  `K_AB^Green=mu8^2q_A^-1q_B^-1 sum_n
  (a_A,n a_B,n+b_A,n b_B,n)/lambda_n^2`.  A constant spin-c stack source
  `rho_A=Pi_A qfrak_C1` has zero perpendicular source and contributes
  through the tadpole equation.  Nonzero sourced vertical current requires
  Fourier content in `I_{1,A}^O8+I_{1,A}^bulk` or harmonic coefficient `h_A`.
- Harmonic current closure row:
  set `v_A=q_A^-1h_A` and
  `Chat_AB=K_AB^CP+K_AB^Green+K_AB^{CP-Green}`.  With
  `p_A=<theta_Gamma,CP^A,omega_Q>` and
  `Omega_Q=<omega_Q,omega_Q>`, the neutral matrix is
  `L_AB^Gamma=Chat_AB+v_Ap_B+v_Bp_A+Omega_Qv_Av_B`.
  The branch-current closure equation is
  `det L^Gamma=R_dV(Chat_33+2v_3p_3+Omega_Qv_3^2)
  (C_Q+2v_Qp_Q+Omega_Qv_Q^2)`.  In the product orthogonal specialization,
  `L^Gamma=C+Omega_Qvv^T`,
	  `det L^Gamma=det C+Omega_Q(C_YYv_3^2-2C_3Yv_3v_Y+C_33v_Y^2)`,
	  and `L_{2,vert}^2=Omega_Qv_3^2`.  For a fixed direction
	  `t=v_Y/v_3`, set `u=Omega_Qv_3^2`, `Delta_C=det C`,
	  `C_Q=C_33+2C_3Y+C_YY`, `C_N=C_33-2C_3Y+C_YY`, and
	  `D_C=R_dV C_33 C_Q-Delta_C`.  The amplitude satisfies
	  `A_tu^2+B_tu+D_C=0`, with `A_t=R_dV(1+t)^2` and
	  `B_t=R_dV(C_33(1+t)^2+C_Q)-(C_YY-2tC_3Y+t^2C_33)`.  The
	  massive-neutral row `v_Y=-v_3` gives
	  `u_N=D_C/((1-R_dV)C_Q)` and `L_Q^2=C_Q`.  The `Q`-parallel row
	  `v_Y=v_3` gives
	  `4R_dV u^2+(R_dV(4C_33+C_Q)-C_N)u+D_C=0`.  With
	  `int_{S1_Q}omega_Q=1`, the harmonic RR potential is
	  `Pi_A C_{1,harm}=2pi vartheta_A omega_Q`, `vartheta_A in R/Z`.
	  Thus `v_A=2pi q_A^-1vartheta_A`,
	  `t=q_3vartheta_Y/(q_Yvartheta_3)`, and
	  `u=(2pi)^2 Omega_Q q_3^-2 vartheta_3^2`.  The massive-neutral
	  Wilson-line row is `q_3^-1vartheta_3+q_Y^-1vartheta_Y=0`; the
	  `Q`-parallel row is `q_3^-1vartheta_3-q_Y^-1vartheta_Y=0`.
	  In the product metric row, `omega_Q=ds_Q/L_Q` and
	  `Omega_Q=Z_Gamma,Q/L_Q`, with
	  `Z_Gamma,Q=sum_s int_CP2_s kappa8 omega_s e^-phi_s
	  sqrt(gamma_CP2,s) tr_Es Pi_Q`.  Hence
	  `L_{2,vert}^2=(2pi)^2 Z_Gamma,Q L_Q^-1 q_3^-2 vartheta_3^2`.
	  Defining `tau_Q=Z_Gamma,Q/Z_Gamma,0` gives
	  `L_{2,vert}^2=(2pi)^2 tau_Q Z_Gamma,0 L_Q^-1 q_3^-2 vartheta_3^2`.
	  For a shared CP2 density profile and normalized endpoint vector
	  `eta_0`, `tau_Q=tr_E_Q Pi_Q`; at `Q=7`, the full retained trace gives
	  `tau_Q=16`.  With `q_3=3Q` and full retained trace
	  `tau_Q=2(Q+1)`,
	  `L_{2,vert}^2=8pi^2(Q+1)Z_Gamma,0 delta_vartheta_3^2/(9Q^2L_Q)`.
	  For `Q=7`, the row is
	  `L_{2,vert}^2=(64pi^2/441)(Z_Gamma,0/L_Q)delta_vartheta_3^2`.
	  The Wilson chamber `|delta_vartheta_3|<=1/2` gives
	  `L_{2,vert}^2<=(16pi^2/441)Z_Gamma,0/L_Q`.
	  Defining `Xi_Q^harm=Z_Gamma,0/(L_Q L_{2,vert}^2)` gives
	  `Xi_Q^harm=9Q^2/(8pi^2(Q+1)delta_vartheta_3^2)`.
	  For `Q=7`, `Xi_7^harm=441/(64pi^2 delta_vartheta_3^2)`, hence
	  `Xi_7^harm>=441/(16pi^2)=2.792665124141...` in the fundamental
	  Wilson chamber.  In the photon-preserving massive-neutral identity
	  chamber, `delta_vartheta_Y=-(q_Y/q_3)delta_vartheta_3`; with
	  `Theta_N=(1/2)min(1,|q_3/q_Y|)`,
	  `Xi_Q^harm>=9Q^2/(8pi^2(Q+1)Theta_N^2)`.
	  Combining this with the massive-neutral amplitude
	  `u_N=D_C/((1-R_dV)C_Q)` gives the direct density condition
	  `Z_Gamma,0/L_Q>=9Q^2D_C/(8pi^2(Q+1)Theta_N^2(1-R_dV)C_Q)`,
	  with `441 D_C/(64pi^2 Theta_N^2(1-R_dV)C_Q)` at `Q=7`.
	  In the point-evaluation base row, `q=lambda^2`,
	  `C_33^pt=1+(Q^2+1)q/(Q+1)^2`,
	  `C_Q^pt=(Q+1)^2C_33^pt`, and
	  `Delta_C^pt=(Q-1)^2q(q+2)`.  For `Q=7`,
	  `u_N^pt(q)=[R_dV(25q+32)^2-576q(q+2)]/
	  [32(1-R_dV)(25q+32)]`, vanishing at
	  `q_c=3.511614004347...`.  The density condition becomes
	  `Z_Gamma,0/L_Q>=441[R_dV(25q+32)^2-576q(q+2)]/
	  [2048pi^2Theta_N^2(1-R_dV)(25q+32)]`.
	  Its derivative is negative on `q>0`:
	  `du_N^pt/dq=-[(14400-15625R_dV)q^2+(36864-40000R_dV)q+
	  (36864-25600R_dV)]/[32(1-R_dV)(25q+32)^2]`.  Thus the target
	  decreases from `R_dV/(1-R_dV)=3.482268368857...` to zero at `q_c`.
	  Define
	  `U_Gamma=64pi^2Theta_N^2 Z_Gamma,0/(441L_Q)`.  The saturation
	  curve solves
	  `A_q q^2+B_q(U_Gamma)q+C_q(U_Gamma)=0`, where
	  `A_q=576-625R_dV`,
	  `B_q=1152-1600R_dV+800(1-R_dV)U_Gamma`, and
	  `C_q=1024((1-R_dV)U_Gamma-R_dV)`.  The positive branch is
	  `q_sat=(-B_q+sqrt(B_q^2-4A_qC_q))/(2A_q)`, and the chamber pass is
	  `q_sat<=q<q_c`.  The Wilson representative is
	  `delta_vartheta_3^2=Theta_N^2u_N^pt(q)/U_Gamma`.
	- Massive-neutral cross-vector row:
	  retain the CP--circle overlap vector `p=(p_3,p_Y)` and set
	  `v=a(1,-1)^T`.  For `C=[[A,B],[B,D]]`,
	  `C_Q=A+2B+D`, `p_Q=p_3+p_Y`, and
	  `S_p=p_3(D+B)-p_Y(A+B)`, one has
	  `det(C+vp^T+pv^T+Omega_Q vv^T)
	  =Delta_C+2aS_p+a^2(Omega_QC_Q-p_Q^2)`.
	  Since `L_Q^2=C_Q`, branch closure gives
	  `((1-R_dV)Omega_QC_Q-p_Q^2)a^2
	  +2(S_p-R_dV p_3C_Q)a-D_C=0`.  With
	  `u=Omega_Qa^2`, `epsilon=sign(a)`, and `y=sqrt(u)`,
	  `A_Ny^2+2epsilon B_Ny-D_C=0`, where
	  `A_N=(1-R_dV)C_Q-p_Q^2/Omega_Q` and
	  `B_N=(S_p-R_dV p_3C_Q)/sqrt(Omega_Q)`.  Hence
	  `u_epsilon=((-epsilon B_N+sqrt(B_N^2+A_ND_C))/A_N)^2`
	  for `A_N!=0`, with affine limit `D_C^2/(4B_N^2)`.
	- DBI cross-vector readout:
	  for `theta_{Gamma,CP}^A=theta_i^A dy^i` and `omega_Q=ds_Q/L_Q`,
	  `p_A=L_Q^-1 sum_sigma int dnu_{Gamma,sigma}
	  gamma_sigma^{is_Q} tr(Pi_Q theta_i^A Pi_Q)`.  Also
	  `Omega_Q=L_Q^-2 sum_sigma int dnu_{Gamma,sigma}
	  gamma_sigma^{s_Qs_Q} tr Pi_Q`.  A block-product internal metric
	  gives `gamma^{is_Q}=0`, hence `p_3=p_Y=0` and
	  `Omega_Q=Z_Gamma,Q/L_Q`.  In a connection-adapted circle coframe
	  `chi_Q=ds_Q+A`, horizontal `theta_{Gamma,CP}^A` gives the same
	  zero-overlap row; nonzero `p_A` requires vertical leakage
	  `theta_{Gamma,CP}^A=theta_H^A+ell_A chi_Q`.
	- Leakage projection lemma:
	  `ell_A=gamma_Gamma^-1(theta_{Gamma,CP}^A,chi_Q)/
	  gamma_Gamma^-1(chi_Q,chi_Q)`.  For the product carrier
	  `pi_CP2:CP2 x S1_Q -> CP2`,
	  `theta_{Gamma,CP}^A=pi_CP2^* alpha_A` and
	  `ds_Gamma^2=g_ij dy^i dy^j+L_Q^2 chi_Q^2` give
	  `gamma_Gamma^-1(pi_CP2^* alpha_A,chi_Q)=0`.  Hence
	  `ell_3=ell_Y=0`, `p_3=p_Y=0`, and
	  `Omega_Q=Z_Gamma,Q/L_Q` in the active product-carrier row.
	- Charge-chamber specialization:
	  the D9 descent fixes `q_3=3Q`; for `Q=7`, `q_3=21`.  Thus
	  `Theta_N(21,q_Y)=(1/2)min(1,|21/q_Y|)`.  The chamber gives
	  `Theta_N=1/2` for `|q_Y|<=21` and
	  `Theta_N=21/(2|q_Y|)` for `|q_Y|>21`.  The density filter is
	  `Z_Gamma,0/L_Q>=441 u_N^pt(q)/(16pi^2)` in the first row and
	  `Z_Gamma,0/L_Q>=q_Y^2 u_N^pt(q)/(16pi^2)` in the second row.
	- Endpoint-character and quotient-line period:
	  the retained `Q=7` line data obey
	  `c_1(L_Y)=6h+Q eta`, `c_1(L_T3)=eta`, and
	  `c_1(L_Y)-Q c_1(L_T3)=6h`.  The quotient line operator
	  `O_Y(gamma_Q)=Hol_{L_Y}(gamma_Q)Hol_{L_T3}(gamma_Q)^(-Q)`
	  has class `6h`, hence unit `S1_Q` character.  Therefore
	  `Hol_{L_Y}(gamma_Q)=Hol_{L_T3}(gamma_Q)^Q`.  For
	  `eta_Q=eta_0^{odot Q}`, the endpoint character has
	  `T_3 eta_Q=-(Q/2)eta_Q` and `Y eta_Q=(Q/2)eta_Q`.
	  Integer hypercharge `y=6Y` gives `q_Y=3Q=21`.  Hence
	  `Theta_N(21,21)=1/2`, `delta_vartheta_Y=-delta_vartheta_3`,
	  and `Z_Gamma,0/L_Q>=441 u_N^pt(q)/(16pi^2)` in the product row.
	  The inverse-density coordinate is
	  `U_Gamma^(21)=16pi^2 Z_Gamma,0/(441L_Q)`, with chamber test
	  `U_Gamma^(21)>=u_N^pt(q)` and shortest representatives
	  `delta_vartheta_3^2=delta_vartheta_Y^2=u_N^pt(q)/(4U_Gamma^(21))`.
	  In the product metric row,
	  `Z_Gamma,0=L_Q Z_Gamma,0^CP2`, where
	  `Z_Gamma,0^CP2=sum_s int_CP2,s dmu_Gamma,s^CP2
	  tr(Pi_Q |eta_Q|^2 Pi_Q)`.  Hence
	  `U_Gamma^(21)=16pi^2 Z_Gamma,0^CP2/441`, and the density pass is
	  `Z_Gamma,0^CP2>=441 u_N^pt(q)/(16pi^2)`.
	  With common endpoint density and unit rank-one normalization,
	  `Z_Gamma,0^CP2=zfrak_Gamma^CP2`,
	  `Z_Gamma,Q^CP2=16 zfrak_Gamma^CP2`, and `tau_Q=16`.
	  For a constant product profile,
	  `zfrak_Gamma^CP2=kappa_8 sum_s omega_s e^-phi_s
	  Vol(CP2_s,gamma_CP2,s)`, giving the density-dominated pass
	  `kappa_8 e^-phi_0 Omega_Gamma Vol(CP2,gamma_CP2)
	  >=9.724809426610...` in the common-profile row.
	  With `int_CP2 h_Q^2=1` and `J_Gamma,s=r_Gamma,s h_Q`, one has
	  `Vol(CP2_s)=r_Gamma,s^2/2`.  The metric-scale pass is
	  `sum_s omega_s e^-phi_s r_Gamma,s^2
	  >=19.449618853220.../kappa_8`, and for a common metric and dilaton
	  `r_Gamma^2>=19.449618853220.../(kappa_8 e^-phi_0 Omega_Gamma)`.
	  The shape readout is
	  `q_Gamma=((Q+1)^2/(Q^2+1))(C_h^Gamma/C_0^Gamma)`, where
	  `C_0^Gamma` and `C_h^Gamma` are the localized endpoint and horizontal
		  Hodge components of `theta_Gamma^3`.  For `Q=7`,
		  `q_Gamma=(32/25)varrho_Gamma`, where
		  `varrho_Gamma=C_h^Gamma/C_0^Gamma`.  Coframe-projection extraction:
		  `C_0^Gamma=<P_0^Gamma theta_Gamma^3,
		  P_0^Gamma theta_Gamma^3>_{Gamma,Pi_Q}` and
			  `C_h^Gamma=<P_h^Gamma theta_Gamma^3,
			  P_h^Gamma theta_Gamma^3>_{Gamma,Pi_Q}`, so
			  `varrho_Gamma` is the quotient with `C_0^Gamma>0`.  Thus
			  sector entries
			  `C_0,s^Gamma=omega_s e^-phi_s
			  <P_0^Gamma theta_Gamma,s^3,
			  P_0^Gamma theta_Gamma,s^3>_{s,Pi_Q}` and
			  `C_h,s^Gamma=omega_s e^-phi_s
			  <P_h^Gamma theta_Gamma,s^3,
			  P_h^Gamma theta_Gamma,s^3>_{s,Pi_Q}` give
			  `varrho_Gamma=sum_s C_h,s^Gamma/sum_s C_0,s^Gamma`.
			  With
			  `b_Gamma,s=C_0,s^Gamma/C_0^Gamma` and
			  `rho_Gamma,s=C_h,s^Gamma/C_0,s^Gamma`,
			  `varrho_Gamma=sum_{s in S_Gamma,0}
			  b_Gamma,s rho_Gamma,s`.
			  Thus
			  `0<varrho_Gamma<varrho_c=(25/32)q_c=2.743448440896...`, and
	  `u_Gamma^sh(varrho_Gamma)=[625R_dV(1+varrho_Gamma)^2
	  -576varrho_Gamma^2-900varrho_Gamma]/
	  [625(1-R_dV)(1+varrho_Gamma)]`.  The chamber pass is
	  `U_Gamma^CP2>=u_Gamma^sh(varrho_Gamma)`, equivalently
	  `Z_Gamma,0^CP2>=(441/(16pi^2))u_Gamma^sh(varrho_Gamma)`.
	  Since `u_N^pt(q)` decreases from `3.482268368857...` to zero at
	  `q_c=3.511614004347...`, the density-dominated pass is
	  `Z_Gamma,0^CP2>=9.724809426610...`; otherwise the active interval is
	  `q_sat(U_Gamma^CP2)<=q<q_c`.
- Finite-matrix extraction:
  choose a `Gamma`-orthonormal image basis `e_i`, set
  `M_ij=<e_i,M_img e_j>_Gamma` and `C_Ai=<e_i,J_A>_Gamma`.
  Then `D_AB=L_2^-2 C_Ai(M^-1)^ijC_Bj`.
  With `w_A=L_2^-1M^-1/2 C_A`, the Schur condition is
  `w_Y=rho_sigma w_3` and `||w_3||^2=delta_sigma`.
  For the determinant row, equality of the two charged Borel-Weil spectra gives
  `N_Gamma^chi=2 sum_alpha sigma_alpha d_alpha F(M_alpha L_H)`.
- Minimal finite spectrum package:
  `H_img,sigma^src=span{e_sigma}`,
  `M_img e_sigma=m_sigma e_sigma`,
  `C_3sigma=L_2 sqrt(m_sigma delta_sigma)`,
  `C_Ysigma=rho_sigma C_3sigma`.
  Hence `D_AB=(g_sigma)_A(g_sigma)_B`.
  In the constant-profile product row,
  `psi_Gamma,0=(L_Q zfrak_Gamma^CP2)^(-1/2)eta_Q` is normalized by
  `int dnu_Gamma tr(Pi_Q |psi_Gamma,0|^2 Pi_Q)=1`.  Taking
  `e_sigma=psi_Gamma,0` and
  `J_A^(sigma)=L_2 sqrt(m_sigma)(g_sigma)_A e_sigma^flat` gives the
  required source couplings.  With
  `G_AB^(0)=int dnu_Gamma psi_Gamma,0^2
  gamma_Gamma^-1(theta_Gamma^A,theta_Gamma^B)`, the image one-form is
  `Xi_sigma=L_2 psi_Gamma,0 (G^(0))^{-1 BC}(g_sigma)_C theta_Gamma^B`,
  giving `R_Xi,sigma=0`.
	  Single-pass packet:
	  `P_Gamma^cp=(kappa_8,e^-phi_0 Omega_Gamma,r_Gamma,L_Q,
	  varrho_Gamma,m_sigma,z_chi,sigma_chi d_chi)`.
	  Density-sector extraction:
	  `e^-phi_0 Omega_Gamma=sum_s omega_s e^-phi_s`,
	  `Omega_Gamma=sum_s omega_s`, and
	  `e^-phi_0=(sum_s omega_s e^-phi_s)/(sum_s omega_s)` in the common row.
	  The endpoint trace factor is `tau_Q=16`.
	  It returns `zfrak_Gamma^CP2=(1/2)kappa_8 e^-phi_0 Omega_Gamma r_Gamma^2`,
	  `Z_Gamma,0=L_Q zfrak_Gamma^CP2`,
  `Z_Gamma,Q=16L_Q zfrak_Gamma^CP2`,
  `Z_Gamma,H=(Q/4)Z_Gamma,0`,
  `q_Gamma=(32/25)varrho_Gamma`,
  `U_Gamma^CP2=(16pi^2/441)zfrak_Gamma^CP2`,
	  `psi_sigma=psi_Gamma,0`,
	  `M_img psi_sigma=m_sigma psi_sigma`, and
	  `N_Gamma^chi=2sigma_chi d_chi F(z_chi)`.
	  Endpoint image-spectrum row:
	  `M_img=Q_img^dagger Q_img`,
	  `Q_img=1_{CP2 x S1_Q} tensor B_sigma`, and
	  `m_sigma=<eta_Q,B_sigma^dagger B_sigma eta_Q>_{E_Q}/
	  <eta_Q,eta_Q>_{E_Q}`.
	  The one-line image condition is
	  `B_sigma^dagger B_sigma eta_Q=m_sigma eta_Q`,
	  `Pi_sigma^perp B_sigma^dagger B_sigma eta_Q=0`, and
	  `m_sigma>0`.
	  Endpoint normal form:
	  `Pi_eta_Q=|eta_Q><eta_Q|/<eta_Q,eta_Q>_{E_Q}`,
	  `B_sigma^dagger B_sigma
	  =m_sigma Pi_eta_Q+B_sigma,perp^dagger B_sigma,perp`, with
	  `B_sigma,perp=Pi_eta_Q^perp B_sigma,perp Pi_eta_Q^perp`.
		  The one-mode reduction has a separated complement for
		  `B_sigma,perp^dagger B_sigma,perp>=M_sigma,perp^2 Pi_eta_Q^perp`
		  and `M_sigma,perp^2>m_sigma`.
		  Equivalently,
		  `g_sigma,perp=M_sigma,perp^2/m_sigma>1`.  For diagonal endpoint
		  spectrum on `Pi_eta_Q^perp E_Q`,
		  `B_sigma^dagger B_sigma e_sigma,alpha
		  =lambda_sigma,alpha e_sigma,alpha` and
		  `g_sigma,perp=min_alpha lambda_sigma,alpha/m_sigma`.
		  Minimal positive determinant block:
	  `B_chi^dagger B_chi=M_chi^2 1_E_chi`, `E_chi=C`, and
	  `sigma_chi d_chi=+1`.  With
	  `Xi_Gamma^cp=[21375.716460702053... lambda_F/(2w_H^8)]
	  (L_Q zfrak_Gamma^CP2/v_EW)^4`, the determinant threshold pass is
	  `0<Xi_Gamma^cp<=1` and `z_chi=F^{-1}(Xi_Gamma^cp)`.
	  This gives
	  `0<Z_Gamma,0=L_Q zfrak_Gamma^CP2<=Z_chi,max`, where
	  `Z_chi,max=v_EW[2w_H^8/(21375.716460702053... lambda_F)]^(1/4)
	  =0.0983506713707568... w_H^2 lambda_F^(-1/4)v_EW`.
	  Combining with the density-shape lower row gives
	  `0<L_Q<=Z_chi,max/zfrak_Gamma^CP2
	  <=16pi^2 Z_chi,max/(441 u_Gamma^sh(varrho_Gamma))`.
	  The equivalent radius band is
	  `441u_Gamma^sh(varrho_Gamma)/(8pi^2 kappa_8 e^-phi_0 Omega_Gamma)
	  <=r_Gamma^2
	  <=2Z_chi,max/(kappa_8 e^-phi_0 Omega_Gamma L_Q)`.
	  Full sector-sum reduction:
		  `R_Gamma^2=sum_s omega_s e^-phi_s r_Gamma,s^2`,
		  `zfrak_Gamma^CP2=(kappa_8/2)R_Gamma^2`, and
		  `441u_Gamma^sh(varrho_Gamma)/(8pi^2 kappa_8)
		  <=R_Gamma^2<=2Z_chi,max/(kappa_8L_Q)`.
		  Trace-density row:
		  `H_S=oplus_{s in S_Gamma}C|s>`,
		  `W_Gamma|s>=omega_s e^-phi_s|s>`,
		  `R_Gamma|s>=r_Gamma,s^2|s>`,
		  `e^-phi_0 Omega_Gamma=Tr_S W_Gamma`, and
		  `R_Gamma^2=Tr_S(W_Gamma R_Gamma)`.
		  Thus `Z_Gamma,0=(kappa_8L_Q/2)Tr_S(W_Gamma R_Gamma)`,
		  `Z_Gamma,Q=8kappa_8L_QTr_S(W_Gamma R_Gamma)`, and
		  `Z_Gamma,H=(Qkappa_8L_Q/8)Tr_S(W_Gamma R_Gamma)`.
		  Set `T_Gamma=Tr_S(W_Gamma R_Gamma)`.
		  The trace pass surface is
		  `T_Gamma>=441u_Gamma^sh(varrho_Gamma)/(8pi^2kappa_8)`
		  and `0<L_Q<=2Z_chi,max/(kappa_8T_Gamma)`.
		  Equivalently, with `0<x_Gamma,Q<=1`,
		  `L_Q=2Z_chi,max x_Gamma,Q/(kappa_8T_Gamma)`.
			  At lower-density saturation,
			  `T_Gamma=441u_Gamma^sh(varrho_Gamma)/(8pi^2kappa_8)` and
			  `L_Q=x_Gamma,Q L_Q,max(varrho_Gamma)`.
			  Define
			  `chi_Gamma=T_Gamma/T_Gamma,min(varrho_Gamma)>=1`.
			  Then
			  `L_Q=(x_Gamma,Q/chi_Gamma)L_Q,max(varrho_Gamma)`,
			  `x_Gamma,Q=chi_Gamma L_Q/L_Q,max(varrho_Gamma)`,
			  and
			  `0<L_Q<=L_Q,max(varrho_Gamma)/chi_Gamma`.
			  In sector variables,
			  `zeta_Gamma,s=omega_s e^-phi_s r_Gamma,s^2/
			  T_Gamma,min(varrho_Gamma)>=0`,
			  `chi_Gamma=sum_s zeta_Gamma,s`, and
			  `L_Q=x_Gamma,Q L_Q,max(varrho_Gamma)/
			  sum_s zeta_Gamma,s`.
			  For fixed `L_Q`,
			  `x_Gamma,Q=(L_Q/L_Q,max(varrho_Gamma))sum_s zeta_Gamma,s`
			  and
			  `1<=sum_s zeta_Gamma,s<=L_Q,max(varrho_Gamma)/L_Q`.
			  Sector fractions
			  `p_Gamma,s=zeta_Gamma,s/chi_Gamma` obey
			  `p_Gamma,s>=0` and `sum_s p_Gamma,s=1`.  Each retained
			  sector then satisfies
			  `omega_s e^-phi_s r_Gamma,s^2
			  =p_Gamma,s chi_Gamma T_Gamma,min(varrho_Gamma)`,
			  hence
			  `r_Gamma,s^2=441p_Gamma,s chi_Gamma
			  u_Gamma^sh(varrho_Gamma)/
			  (8pi^2 kappa_8 omega_s e^-phi_s)`.
			  Finite data certificate:
				  `D_Gamma=(S_Gamma; omega_s,phi_s,p_Gamma,s,
				  b_Gamma,s,rho_Gamma,s; chi_Gamma,x_Gamma,Q,L_Q;
				  m_sigma,epsilon_sigma,Q,lambda_sigma,alpha)`.  It gives
				  `varrho_Gamma=sum_{s in S_Gamma,0}
				  b_Gamma,s rho_Gamma,s`,
				  `T_Gamma=chi_Gamma T_Gamma,min(varrho_Gamma)`,
				  `L_Q=(x_Gamma,Q/chi_Gamma)L_Q,max(varrho_Gamma)`,
				  `z_chi=F^{-1}(x_Gamma,Q^4)`,
				  `epsilon_sigma,Q^2=
				  ||Pi_eta_Q^perp B_sigma^dagger B_sigma eta_Q||^2/
				  (m_sigma^2||eta_Q||^2)`, and
				  `g_sigma,perp=min_alpha lambda_sigma,alpha/m_sigma`.
				  Its algebraic conditions are
				  `chi_Gamma>=1`, `0<x_Gamma,Q<=1`,
				  `0<varrho_Gamma<varrho_c`,
				  `epsilon_sigma,Q=0`, `g_sigma,perp>1`,
				  `sum_s p_Gamma,s=1`, `sum_s b_Gamma,s=1`,
				  and `p_Gamma,s,b_Gamma,s,rho_Gamma,s>=0`.
				  Action-to-certificate map:
				  `Q_Gamma^(2)=(S_Gamma; omega_s,phi_s,
				  gamma_Gamma,s^CP2; theta_Gamma,s^3,
				  P_0^Gamma,P_h^Gamma,Pi_Q; B_sigma,eta_Q,L_Q)`.
				  With
				  `Av_{s,Pi_Q}(f)=int_CP2_s sqrt(hat gamma_s)
				  tr_Es(Pi_Q f Pi_Q)/
				  int_CP2_s sqrt(hat gamma_s) tr_Es(Pi_Q)`,
				  `r_Gamma,s^2=Av_{s,Pi_Q}
				  [(1/4)tr_hat gamma_s gamma_Gamma,s^CP2]`,
				  `T_Gamma=sum_s omega_s e^-phi_s r_Gamma,s^2`,
				  `x_Gamma,Q=kappa_8L_QT_Gamma/(2Z_chi,max)`,
				  `m_sigma=<eta_Q,B_sigma^dagger B_sigma eta_Q>/
				  <eta_Q,eta_Q>`, and
				  `{lambda_sigma,alpha}=Spec(Pi_eta_Q^perp
				  B_sigma^dagger B_sigma Pi_eta_Q^perp)`,
				  plus `epsilon_sigma,Q^2=
				  ||Pi_eta_Q^perp B_sigma^dagger B_sigma eta_Q||^2/
				  (m_sigma^2||eta_Q||^2)`,
				  the readout map is
				  `Efrak_Gamma(Q_Gamma^(2))=D_Gamma`.
				  Algebraic inverse packet:
				  `S_Gamma,+={s:p_Gamma,s>0}`,
				  `gamma_Gamma,s^CP2=r_Gamma,s^2 hat gamma_s`,
				  `r_Gamma,s^2=p_Gamma,s chi_Gamma
				  T_Gamma,min(varrho_Gamma)/(omega_s e^-phi_s)`,
				  `P_0^Gamma theta_Gamma,s^3=
				  (b_Gamma,s C_Gamma/(omega_s e^-phi_s))^(1/2)
				  hat e_0,s`,
				  `P_h^Gamma theta_Gamma,s^3=
				  (b_Gamma,s rho_Gamma,s C_Gamma/
				  (omega_s e^-phi_s))^(1/2)hat e_h,s`, and
				  `B_sigma^dagger B_sigma=m_sigma |e_0><e_0|
				  +sum_alpha lambda_sigma,alpha |e_alpha><e_alpha|`.
				  Hence
				  `Ifrak_Gamma(D_Gamma;C_Gamma,hat e)=Q_Gamma^(2)`
				  and
				  `Efrak_Gamma(Ifrak_Gamma(D_Gamma;C_Gamma,hat e))
				  =D_Gamma`.
				  Charged determinant extension:
				  `z_chi=F^{-1}(x_Gamma,Q^4)`,
				  `M_chi=z_chi/L_H`, `E_chi=C`,
				  `sigma_chi d_chi=+1`,
				  `P_1^chi=span{u,v}`,
				  `P_2^chi=span{u^2,v^2}`,
				  `B_chi^dagger B_chi=M_chi^2 1_E_chi`,
				  and `B_{r,Gamma}^chi=1_{P_r^chi} tensor B_chi`.
				  Hence `N_Gamma^chi=2F(M_chiL_H)=2x_Gamma,Q^4`
				  and
				  `Qtilde_Gamma^(2)=(Q_Gamma^(2);
				  P_1^chi,P_2^chi,E_chi,B_chi,L_H,
				  sigma_chi d_chi)`.
				  Finite action residual:
				  `A_Gamma=(P_s[G+B],F_s,phi_s,omega_s,Pi_s;
				  iota_Gamma^*C_1; B_sigma,B_chi,L_Q,L_H)_s`.
				  Define
				  `R_Gamma(A_Gamma;D_Gamma)=(R_T,R_x,R_varrho,
				  R_epsilon,R_g,R_chi)`, with
				  `R_T=T_Gamma(A_Gamma)/T_Gamma,min(varrho_Gamma)
				  -chi_Gamma`,
				  `R_x=kappa_8L_QT_Gamma(A_Gamma)/(2Z_chi,max)
				  -x_Gamma,Q`,
				  `R_varrho=C_h^Gamma(A_Gamma)/C_0^Gamma(A_Gamma)
				  -varrho_Gamma`,
				  `R_epsilon=epsilon_sigma,Q`,
					  `R_g=max{0,1-min_alpha lambda_sigma,alpha/m_sigma}`,
					  and `R_chi=(M_chiL_H-z_chi)/(1+z_chi)`.
					  Completion row: `R_Gamma(A_Gamma;D_Gamma)=0`.
					  Finite local normal form:
					  `W_s=omega_s e^-phi_s`,
					  `P_s[G+B]_CP2=r_Gamma,s^2hat gamma_s`,
					  `r_Gamma,s^2=p_Gamma,s chi_Gamma
					  T_Gamma,min(varrho_Gamma)/W_s`,
					  `Pi_EW iota_Gamma^*C_1|_s
					  =q_Gamma theta_Gamma,s^3`,
					  `P_0^Gamma theta_Gamma,s^3
					  =(b_Gamma,s C_Gamma/W_s)^(1/2)hat e_0,s`,
					  `P_h^Gamma theta_Gamma,s^3
					  =(b_Gamma,s rho_Gamma,s C_Gamma/W_s)^(1/2)
					  hat e_h,s`,
					  `B_chi^dagger B_chi=(z_chi/L_H)^2 1_E_chi`,
					  and `L_Q=(x_Gamma,Q/chi_Gamma)
					  L_Q,max(varrho_Gamma)`.  This gives
					  `R_Gamma(A_Gamma^nf;D_Gamma)=0`.
					  Global D8/O8 lift row:
					  `Gfrak_Gamma=(X_10,I_O8,iota_Gamma,s,E_s,F_s,
					  phi_s,G,B,C_1,F_0,Omega)_s`,
					  `Lfrak_Gamma(Gfrak_Gamma)=A_Gamma^nf`,
					  `dF_0=sum_s N_8,s delta_Gamma_s
					  +sum_a Q_O8,a delta_O8,a`,
					  `sum_s N_8,s+sum_a Q_O8,a=0`,
					  and
					  `Q_lower^tot=[sum_s ch(E_s)exp(F_s/2pi)
					  sqrt(Ahat(TGamma_s)/Ahat(NGamma_s))
					  +sum_a Q_O8,a^curv]_<8=0`.
					  The global residual
					  `R_Gamma^glob(Gfrak_Gamma)=0` implies
					  `R_Gamma(A_Gamma;D_Gamma)=0`.
					  Minimal endpoint-real datum:
					  `Q_O8,L=Q_O8,R=-16`,
					  `N_8,L=N_8,R=16`,
					  `k_epsilon=N_8,epsilon/2-8=0`,
					  `W_7=H0(CP1,O(7))`,
					  `dim W_7=8`,
					  `E_7=(W_7 op W_7^vee)^Omega`,
					  `rk_C(E_7^C)=16`,
					  `qfrak_C1=16((13/2)^2/2-1/16)=337`,
					  `Q_D8/O8^<8=208h_Q+673h_Q^2`,
					  and `Q_bulk^<8=-208h_Q-673h_Q^2`.
					  With
					  `Lfrak_Gamma(Gfrak_Gamma^(7))=A_Gamma^nf`,
					  one has
					  `R_Gamma^glob(Gfrak_Gamma^(7))=0`.
					  Product-threshold row:
				  `V_Gamma,Q=L_QR_Gamma^2`,
			  `Z_Gamma,0=(kappa_8/2)V_Gamma,Q`, and
		  `Xi_Gamma^cp=(Z_Gamma,0/Z_chi,max)^4
		  =(kappa_8V_Gamma,Q/(2Z_chi,max))^4`.
		  Thus `0<V_Gamma,Q<=2Z_chi,max/kappa_8` and
		  `z_chi=F^{-1}[(kappa_8V_Gamma,Q/(2Z_chi,max))^4]`.
		  Normalized endpoint coordinate:
		  `x_Gamma,Q=Z_Gamma,0/Z_chi,max
		  =kappa_8V_Gamma,Q/(2Z_chi,max)
		  =kappa_8L_QT_Gamma/(2Z_chi,max)`,
		  `Xi_Gamma^cp=x_Gamma,Q^4`,
		  `z_chi=F^{-1}(x_Gamma,Q^4)`, and
		  `L_Q/L_Q,max(varrho_Gamma)<=x_Gamma,Q<=1`.
		  Define `I_{r^2}(varrho_Gamma,L_Q)
	  =[r_min^2(varrho_Gamma),r_max^2(L_Q)]`, where
	  `r_min^2=441u_Gamma^sh(varrho_Gamma)/
	  (8pi^2 kappa_8 e^-phi_0 Omega_Gamma)` and
	  `r_max^2=2Z_chi,max/(kappa_8 e^-phi_0 Omega_Gamma L_Q)`.
	  The interval is populated exactly when
	  `0<L_Q<=L_Q,max(varrho_Gamma)`, with
	  `L_Q,max=16pi^2Z_chi,max/(441u_Gamma^sh(varrho_Gamma))`.
	  Endpoint row:
	  `E_1^chi=span{u,v} tensor E_chi`,
  `E_2^chi=span{u^2,v^2} tensor E_chi`,
  `(B_r,Gamma^chi)^dagger B_r,Gamma^chi=M_chi^2 1_{2d_chi}`.
  Positive determinant sign gives `N_Gamma^chi=2d_chi F(M_chi L_H)`;
  the minimal row has `d_chi=1`.
- Single-block boundary complex:
  `H_Gamma^loc=span{e_sigma} op (P_1^chi op P_2^chi) tensor E_chi op H_perp`
  with `P_1^chi=span{u,v}` and `P_2^chi=span{u^2,v^2}`.
  The operator
  `Q_Gamma,sigma=sqrt(m_sigma)Pi_e_sigma
  op (1_P1^chi op 1_P2^chi) tensor B_chi op Q_perp`
  gives `M_img` on the image line and
  `B_r,Gamma^chi=1_{P_r^chi} tensor B_chi`.
  Density target:
  `F(M_chi L_H)=21375.716460702053... lambda_F
  (Z_Gamma,0/v_EW)^4/(2d_chi w_H^8)`.
- Profile-to-matrix closure:
  identify `e_sigma=psi_sigma`.  With
  `G_AB^(psi)=int dnu_Gamma psi_sigma^2
  gamma_Gamma^-1(theta_Gamma^A,theta_Gamma^B)` and
  `c_sigma=G^(psi)^-1 g_sigma`, set
  `Xi_sigma,min=L_2 psi_sigma c_sigma^B theta_Gamma,B` and
  `Theta_img,sigma=sqrt(m_sigma)Xi_sigma,min`.
  Then `C_Asigma=L_2 sqrt(m_sigma)(g_sigma)_A`,
  `M_11=m_sigma`, and `D_AB=(g_sigma)_A(g_sigma)_B`.
- Effective-period diagnostic:
  interpreting `rho_sigma=2Q_eff^(sigma)+1` gives
  `Q_eff^(+)=9.333551007611...` and `Q_eff^(-)=5.818646994052...`.
  Both values lie outside the integral weak-period lattice, so a period relabel
  is excluded.  Remaining routes: Green-source coframe deformation or
  projection inside the localized image sector.
- Point-projector current metric:
  with `J_Q=Q/2`, `|0>=|J_Q,J_Q>`, `P_p=|0><0|`, and `K_p=1-P_p`,
  `G_ab^(p)=Re <0|T_a K_p T_b|0>` gives
  `G_ab^(p)=(Q/4) diag(1,1,0)` in the Hermitian current basis.  This supplies
  the equal transverse weak-current metric for the Hosotani local-data test.
  With common localized density `f_Gamma^2`, the normalized transverse
  coefficients are `alpha_mix=2 mu_Gamma/(sqrt(Q) f_Gamma)` and
  `beta_diag=4 mu_Gamma^2/(Q f_Gamma^2)`, hence
  `beta_diag/alpha_mix^2=1`.
- Hypercharge endpoint mass block:
  writing the weak period as `Q_w`, `J_w=Q_w/2`, and assigning
  `Y|0>=-J_w|0>` gives `Q_em|0>=0`.  The endpoint-line metric on
  `(T3,Y)` gives
  `N_AB^(p)=(Q_w^2/4)[[1,-1],[-1,1]]`, with null direction `(1,1)` and
  massive direction `(1,-1)`.  Scope: endpoint mass block; gauge-kinetic
  neutral lengths remain assigned to the localized current matrix.
- Gauge-coupled endpoint masses:
  inserting `(g2,gY)` gives
  `M_N^2=v_Gamma^2 J_w^2 [[g2^2,-g2 gY],[-g2 gY,gY^2]]`,
  photon `A=(gY W3+g2 B)/sqrt(g2^2+gY^2)`, and
  `M_Z^2=v_Gamma^2 J_w^2(g2^2+gY^2)`.  The transverse projector gives
  `M_W^2=v_Gamma^2 Q_w g2^2/4`.  At `Q_w=1`, the standard electroweak
  doublet normalization follows.
- Endpoint/Connes amplitude bridge:
  the finite-line amplitude is `|v_F|=v_EW/sqrt(2)`, and the endpoint
  gauge-mass convention is `v_Gamma=v_EW=sqrt(2)|v_F|`.  Hence
  `M_W^2=g2^2 |v_F|^2/2` and
  `M_Z^2=(g2^2+gY^2)|v_F|^2/2`.
- Boundary current pullback normal form:
  with `iota_Gamma:Gamma_EW -> K6` and retained weak projection `Pi_EW`,
  write `Pi_EW iota_Gamma^*C_1=q_Gamma theta_Gamma^3` and
  `Pi_EW iota_Gamma^*F_2=q_Gamma d_Gamma theta_Gamma^3`.  The norm target is
  `int dnu_Gamma gamma_Gamma^-1(theta_Gamma^a,theta_Gamma^b)
  =L_{2,Gamma}^2 delta^{ab}`, giving
  `e_Gamma^a=theta_Gamma^a/L_{2,Gamma}`.
- Boundary-frame neutral matrix:
  recompute `K_Gamma,AB=int dnu_Gamma
  gamma_Gamma^-1(theta_Gamma^A,theta_Gamma^B)` for
  `A,B in {T3,Y,Q}`.  The source-metric identity
  `L_Q^2=L_2^2+L_Y^2` is a target value; propagate any derived replacement
  through alpha and the neutral mass block.
- Neutral pass equation:
  with `R_dV=X_+(3/4)/X_+(2)`,
  `M_W^2/M_Z^2=det(L_Gamma)/(L_2^2 L_Q^2)=R_dV`, equivalently
  `eps_Gamma^2+2 R_dV L_2^2 eps_Gamma+R_dV L_2^4
  +(R_dV-1)L_2^2 L_Y^2=0`.
- Neutral positivity filter:
  `u>0`, `|delta|<sqrt(u)`, `u+1+2 delta>0`, and
  `0<u<=R_dV^-1`.  At `u=u_dV`, both `delta_+=0` and
  `delta_-=-2(1-R_dV)` pass positivity, so the localized action has to
  select the neutral branch.
- Neutral correlation target:
  `chi_Gamma=eps_Gamma/(L_2 L_Y)=delta/sqrt(u)`, with
  `R_dV=(1-chi_Gamma^2)/(u+1+2 chi_Gamma sqrt(u))`.  At `u=u_dV`,
  `chi_+=0` and `chi_-=-2 sqrt(R_dV(1-R_dV))`.
- Neutral factorization target:
  `L_Gamma=L_Y^2 [[u,chi_Gamma sqrt(u)],[chi_Gamma sqrt(u),1]]`.
  The localized action must compute `(L_Y^2,u,chi_Gamma)` from the three
  current-frame integrals.
- Pass surface parameterization:
  with `y=sqrt(u)`,
  `R_dV y^2+2 R_dV chi_Gamma y+R_dV+chi_Gamma^2-1=0`, hence
  `y_pm(chi)=-chi +/- sqrt((1-R_dV)(1-chi^2)/R_dV)`.
- Observable scale closure:
  with `D_Gamma=u+1+2 chi_Gamma sqrt(u)` and
  `Lambda_Gamma=C^2/L_Y^2`,
  `alpha_Gamma=Lambda_Gamma/(4 pi D_Gamma)`,
  `M_W^2=Lambda_Gamma v_EW^2/(4u)`, and
  `M_Z^2=Lambda_Gamma v_EW^2 D_Gamma/(4u(1-chi_Gamma^2))`.
- Observable inversion closure:
  `Lambda_Gamma^(alpha)=4 pi alpha_Gamma D_Gamma`,
  `Lambda_Gamma^(W)=4u M_W^2/v_EW^2`, and
  `Lambda_Gamma^(Z)=4u(1-chi_Gamma^2)M_Z^2/(v_EW^2 D_Gamma)` must agree.
- Inverse electroweak reconstruction:
  with `S_W=M_W^2/(pi alpha_Gamma v_EW^2)`,
  `S_Z=M_Z^2/(pi alpha_Gamma v_EW^2)`, and `R_obs=S_W/S_Z`,
  the current data obey `S_W u=u+1+2 varsigma sqrt(u(1-R_obs S_W u))`.
- CP1 control integral:
  `Vol(CP1)^-1 int g(K_a,K_b) = (2/3) R_w^2 delta_ab`.
- D10 boundary-current frame:
  `e_Gamma^a=theta_Gamma^a/L_{2,Gamma}` gives `kappa_cur=1` after the
  localized norm equality is derived.
- Boundary operator package:
  `B_Gamma=(dnu_Gamma,theta_Gamma^a,theta_Gamma^Y,eta0,
  Delta_Gamma,j,mu_Gamma^2)` collects the current, neutral, endpoint,
  complement, and auxiliary equations into a D10 candidate filter.
- KLT one-shape flag line: `a=b=A`, `c=lambda A`.
- Tuple-family density caution:
  close numerical hits are rejected as construction evidence.  The Schur
  operator and localized boundary action are the weak-angle source.
