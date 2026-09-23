# Goal Completion Audit

Date: 2026-05-26T13:00:00+02:00

## Current Objective

```text
finish job on the Gamma_EW
```

## Completion Verdict

Status: active. Completion evidence is incomplete for the full
`Gamma_EW` objective.

The project now has a coherent algebraic worksheet for the localized
electroweak boundary cycle

```text
Gamma_EW = M4 x CP2 x S1_Q
```

and the one-mode image-source algebra is closed.  Report 23 adds a local
type-I' readout representative returning the finite normal form. Completion
requires the flux-quantized global extension and a boundary Dirac-Dolbeault
derivation of the endpoint operators from one action.

## Current Requirement Audit

| requirement | current evidence | verdict | required evidence for completion |
| --- | --- | --- | --- |
| D10 carrier definition | `codexVersion.tex`, `progressReport17.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` use `Gamma_EW=M4 x CP2 x S1_Q`. | covered | Preserve the D10 construction lock. |
| Boundary/current action skeleton | `codexVersion.tex`, `progressReport18.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now record the quadratic master form with current, image, Wilson, and determinant rows. | quadratic worksheet covered | Compute each row from a chosen localized D8/O8 spectrum and charge distribution. |
| Action-to-certificate extraction map | `progressReport22.tex`, `codexVersion.tex`, `gamma-ew-boundary-quadratic-action-audit.md`, and `codexVersion-proof-gates.md` now define `Efrak_Gamma(Q_Gamma^(2))=D_Gamma`, with readouts for `r_Gamma,s`, `T_Gamma`, `varrho_Gamma`, `chi_Gamma`, `x_Gamma,Q`, `m_sigma`, `epsilon_sigma,Q`, and `lambda_sigma,alpha`. | extraction worksheet covered | Evaluate `Q_Gamma^(2)` from the concrete D8/O8 boundary operator, metric pullback, sector weights, and endpoint spectrum. |
| Finite local normal form | `progressReport22.tex`, `codexVersion.tex`, `gamma-ew-boundary-quadratic-action-audit.md`, and `codexVersion-proof-gates.md` now define `A_Gamma^nf` with `P_s[G+B]_CP2=r_Gamma,s^2hat gamma_s`, current pullback `Pi_EW iota_Gamma^*C_1=q_Gamma theta_Gamma,s^3`, endpoint image block `B_sigma`, determinant block `B_chi`, and `L_Q=(x_Gamma,Q/chi_Gamma)L_Q,max(varrho_Gamma)`, giving `R_Gamma(A_Gamma^nf;D_Gamma)=0`. | finite normal form covered | Derive the same normal form from a concrete global D8/O8 configuration. |
| Global D8/O8 lift residual | `progressReport22.tex`, `codexVersion.tex`, `gamma-ew-boundary-quadratic-action-audit.md`, and `codexVersion-proof-gates.md` now define `Gfrak_Gamma`, the localized readout `Lfrak_Gamma(Gfrak_Gamma)=A_Gamma^nf`, the Romans source equation, the total D8/O8 charge row, and `Q_lower^tot=0`, assembled into `R_Gamma^glob(Gfrak_Gamma)`. | global residual worksheet covered | Exhibit a concrete `Gfrak_Gamma` with `R_Gamma^glob(Gfrak_Gamma)=0`. |
| Minimal endpoint-real datum | `progressReport23.tex`, `codexVersion.tex`, `gamma-ew-boundary-quadratic-action-audit.md`, and `codexVersion-proof-gates.md` now set `Q_O8,L=Q_O8,R=-16`, `N_8,L=N_8,R=16`, `W_7=H0(CP1,O(7))`, `rk_C(E_7^C)=16`, `qfrak_C1=337`, `Q_D8/O8^<8=208h_Q+673h_Q^2`, and `Q_bulk^<8=-208h_Q-673h_Q^2`, so `Q_lower^tot=0`. | endpoint and charge rows covered | Combine with the local readout representative and complete the global extension. |
| Localized readout equality | `progressReport23.tex`, `codexVersion.tex`, `gamma-ew-boundary-quadratic-action-audit.md`, `codexVersion-proof-gates.md`, and `claim-ledger.md` now give a local type-I' representative with `P_sG_CP2=r_Gamma,s^2hat gamma_s`, `W_s r_Gamma,s^2=p_Gamma,s chi_Gamma T_Gamma,min`, normal-form current coframes, diagonal `B_sigma`, and `B_chi^dagger B_chi=(z_chi/L_H)^2`, yielding `R_T=R_x=R_varrho=R_epsilon=R_g=R_chi=0`. | local readout representative covered | Extend this representative to a flux-quantized global type-I' configuration and derive `B_sigma,B_chi` from the boundary Dirac-Dolbeault operator. |
| Global extension split | `progressReport23.tex`, `codexVersion.tex`, `codexVersion-proof-gates.md`, and `claim-ledger.md` now separate the global extension into `R_per,s=q_Gamma ell_Gamma,s/(2pi)-n_Gamma,s-nu_Gamma,s`, the boundary Dirac-Dolbeault residual `R_DD`, and the lower-source condition `Q_lower^tot=0`. | extension worksheet covered | Compute the common rational-period locus and construct `D_partial,Gamma^(7)` from the boundary complex. |
| Shared DBI measure | `progressReport18.tex`, `codexVersion.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now define the sector-sum density `dnu_Gamma,s=kappa_8 omega_s e^-phi_s sqrt(gamma_Gamma,s)d^5sigma` and the common inner product `<X,Y>_Gamma=sum_s int dnu_Gamma,s gamma_s^mn tr(Pi_s X_m Pi_s Y_n)`. | action density covered | Compute the retained sector list, `omega_s`, projectors `Pi_s`, pulled-back metric, and dilaton profile from the localized D8/O8 configuration. |
| Retained D8/O8 sector assignment | `progressReport18.tex`, `codexVersion.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now set `W_Q=H0(CP1,O(Q))`, `E_Q=(W_Q op W_Q^vee)^Omega`, and at `Q=7` obtain `rk_C(E_Q^C)=16`, `q_8^net=0`, `k=0`, with row projectors `Pi_Q`, `Pi_sigma`, and `Pi_chi`. | sector bookkeeping covered | Derive the orientifold sign, endpoint reality convention, row projectors, and localized spectrum from the D8/O8 boundary operator. |
| Orientifold endpoint reality | `progressReport18.tex`, `codexVersion.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now define `J_n e_k=(-1)^k e_{n-k}`, `J_n^2=(-1)^n`, and the doubled involution `Omega_n(s,lambda)=(J_n^-1 lambda,J_n s)`. This yields `Tr P_Omega,1 P_1^chi=2`, `Tr P_Omega,2 P_2^chi=2`, and `d_1=d_2=d_chi`. | endpoint reality covered | Derive the determinant sign `sigma_chi`, common threshold `M_chi`, and oscillator spectrum from `B_Gamma^chi`. |
| Charged oscillator determinant | `progressReport18.tex`, `codexVersion.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now give the charged circle spectrum `lambda_{ell,r}=p_E^2+M_chi^2+(2pi ell+rx)^2/L_H^2`, `r=1,2`, with Euclidean complex-boson sign `sigma_chi=+1` and `N_Gamma^chi=2d_chi F(M_chi L_H)`. | determinant spectrum covered | Derive `M_chi`, `L_H`, and `Z_Gamma,0` from the localized D8/O8 operator and density row. |
| RR/current coframe extraction | `progressReport18.tex`, `codexVersion.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now split `theta_Gamma^A=theta_Gamma,CP^A+q_A^-1 Pi_A iota_Gamma^*C_1`, define the curvature check with `F_2`, and read out `L_{2,Gamma}`, `L_Q`, and `det L_Gamma=R_dV K_33 L_Q^2`. | current extraction row covered | Compute the pulled-back `C_1,F_2`, the CP/endpoint coframe piece, and the resulting current matrix from the localized geometry. |
| CS source polynomial | `progressReport18.tex`, `codexVersion.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now compute `Y_Gamma=N8[1+f_m h_Q+(f_m^2/2-1/16)h_Q^2]`, the `C_1` source coefficient `qfrak_C1=N8(f_m^2/2-1/16)`, the minimal spin-c value `qfrak_C1=337`, and the compact zero-mode equation `<I_1,Gamma,omega_Q>_Gamma=0`. | source polynomial covered | Compute the retained RR Green operator, O8/lower-charge completion, and projected `C_1` coframe for `A=3,Y`. |
| Finite Green coframe readout | `progressReport18.tex`, `codexVersion.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now express `G_1,Gamma I_1,A^perp` through one-form eigenmodes and give a finite spectral formula for `K_AB^Gamma` in terms of `h_A`, `Omega_Q`, `p_A`, `K_AB^CP`, `B_Ai`, `P_Ai`, `lambda_i`, and `q_A`. | Green matrix formula covered | Compute the spectrum `lambda_i`, overlaps `B_Ai`, CP projections `P_Ai`, harmonic coefficients `h_A`, and compact source completion from the localized geometry. |
| `S1_Q` Fourier source test | `progressReport18.tex`, `codexVersion.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now reduce the product circle Green solve to Fourier coefficients `a_A,n`, `b_A,n` with `lambda_n=(2pi n/L_Q)^2`, giving `K_AB^Green=mu8^2 q_A^-1 q_B^-1 sum_n(a_A,n a_B,n+b_A,n b_B,n)/lambda_n^2`. Constant spin-c source has zero perpendicular Fourier content. | circle Green test covered | Compute the O8/bulk Fourier profile or harmonic `h_A` that supplies nonzero sourced vertical current. |
| Harmonic current closure | `progressReport19.tex`, `codexVersion.tex`, and `gamma-ew-boundary-quadratic-action-audit.md` now express `L_AB^Gamma=Chat_AB+v_A p_B+v_B p_A+Omega_Q v_Av_B` with `v_A=q_A^-1 h_A`, reduce the product orthogonal specialization to `L^Gamma=C+Omega_Q vv^T`, and give the fixed-direction amplitude equation for `u=Omega_Qv_3^2`. The massive-neutral row has `u_N=D_C/((1-R_dV)C_Q)` with `L_Q^2=C_Q`; the `Q`-parallel row obeys a quadratic amplitude equation. The harmonic coefficients are now Wilson-line variables `Pi_A C_{1,harm}=2pi vartheta_A omega_Q`, with `vartheta_A in R/Z`. The product DBI row gives `Omega_Q=Z_Gamma,Q/L_Q`, and the density bridge gives `tau_Q=Z_Gamma,Q/Z_Gamma,0`. | harmonic amplitude, Wilson-line, DBI norm, and density-ratio filters covered | Compute `C_AB`, `Z_Gamma,0`, `tau_Q`, `L_Q`, `vartheta_3`, and `vartheta_Y` from localized harmonic `C_1`, O8/bulk completion, and current normalization. |
| Wilson charge chamber | `progressReport20.tex`, `codexVersion.tex`, `gamma-ew-boundary-quadratic-action-audit.md`, and `claim-ledger.md` now use `c_1(L_Y)-Q c_1(L_T3)=6h` and the quotient line operator `O_Y(gamma_Q)=Hol_LY(gamma_Q)Hol_LT3(gamma_Q)^(-Q)` to fix `q_3=21`, `q_Y=21`, `Theta_N=1/2`, `U_Gamma^(21)=16pi^2 zfrak_Gamma^CP2/441`, `tau_Q=16`, and `zfrak_Gamma^CP2>=441 u_N^pt(q)/(16pi^2)` in the retained `Q=7` product row. The shape-envelope readout is `varrho_Gamma=C_h^Gamma/C_0^Gamma`, `q_Gamma=(32/25)varrho_Gamma`, and `U_Gamma^CP2>=u_Gamma^sh(varrho_Gamma)`. | quotient-line period, density reduction, and density-shape envelope covered | Compute `zfrak_Gamma^CP2`, `C_h^Gamma/C_0^Gamma`, and image operator data from the localized action. |
| Unit weak-current coframe | Boundary-current closure proposition gives `int dnu_Gamma gamma_Gamma^-1(theta_Gamma^a,theta_Gamma^b)=L_{2,Gamma}^2 delta_ab` and hence `A_j^dagger A_j=j(j+1)`. | algebraic criterion covered | Derive `theta_Gamma^a`, `dnu_Gamma`, and `L_{2,Gamma}` from the localized `C1,F2` and boundary image channel. |
| Article coverage of auxiliary discoveries | `article-research-coverage-audit.md`, `codexVersion.tex`, `progressReport23.tex`, `README.md`, and `progress-report-log.md` now map the major auxiliary clusters, conversation-harvest triage, D10 current-frame lift `e_a=Ktilde_a/L_{2,Gamma}`, frozen consistency checks, and final handoff-prose cleanup to the RR/current section. | coverage audit updated | User steering freezes derivation work in this pass; continue coverage and consistency cleanup for existing material. |
| Schur image branch | One-mode image-source closure and finite-matrix extraction give `D_AB=L_2^-2 C_Ai(M^-1)^ijC_Bj`, with Schur condition `w_Y=rho_sigma w_3` and `||w_3||^2=delta_sigma`. | algebraic closure covered | Compute `M_img`, `psi_sigma`, `m_sigma`, and `Theta_img,sigma` from the local D8/O8 operator. |
| Minimal local realization packet | `progressReport17.tex`, `progressReport20.tex`, `codexVersion.tex`, `codexVersion-proof-gates.md`, and `gamma-ew-boundary-quadratic-action-audit.md` now record `P_Gamma,sigma=(dnu_Gamma,psi_sigma,m_sigma,Xi_sigma,G^(psi),Z_Gamma,0,N_Gamma^chi)` and the constant-profile scalar packet `P_Gamma^cp=(kappa_8,e^-phi_0 Omega_Gamma,r_Gamma,L_Q,varrho_Gamma,m_sigma,z_chi,sigma_chi d_chi)`. | worksheet covered | Derive the packet scalars from the localized D8/O8 boundary operator. |
| Hosotani kinetic row | Point-projector metric gives `Z_Gamma,H=(Q/4)Z_Gamma,0` and `beta_diag/alpha_mix^2=1`. | tensor and metric target covered | Derive `Z_Gamma,0`, `Z_Gamma,H`, `mu_Gamma`, and `w_H` from the same action. |
| Endpoint determinant row | Payen trace and Borel-Weil endpoint rows give `N_Gamma^chi=2 sigma_chi d_chi F(z)` with positive minimal sign. | trace and sign placement covered | Derive the charged oscillator spectrum, threshold `z`, and signed multiplicity from the localized boundary complex. |
| Neutral and electromagnetic length | Point-evaluation row gives the neutral candidate and the diagnostic `L_Q^2/L_2^2=64`; alpha closure requires `k_alpha=4.648394337766...`. | target covered | Compute the complete localized neutral matrix including CP2, Chan-Paton, image, frame, and current contributions to `L_Q`. |
| D8/O8 charge and global consistency | WZ and spin-c skeletons record `N8`, O8 curvature terms, and Freed-Witten shift candidates. | skeleton covered | Select endpoint distribution, Romans jump, lower-charge cancellation, and K-theory convention. |
| Manuscript/control placement | Proof bookkeeping is in auxiliary files and `% CONTROL` comments; typeset manuscript contains physics statements and conditional propositions. | covered | Maintain this split through future TeX edits. |
| Build health | `pdflatex` x2 passed for `progressReport23.tex` and `codexVersion.tex`; log scan reports package metadata lines for `rerunfilecheck` alone. | covered | Repeat after each TeX edit. |

## Latest Concrete Progress

Report 21 compresses the determinant, CP2 density, and loop-length constraints
to one normalized endpoint coordinate:

```text
x_Gamma,Q=Z_Gamma,0/Z_chi,max
=kappa_8V_Gamma,Q/(2Z_chi,max).
```

The determinant threshold and compactification interval become

```text
Xi_Gamma^cp=x_Gamma,Q^4,
z_chi=F^{-1}(x_Gamma,Q^4),
L_Q/L_Q,max(varrho_Gamma)<=x_Gamma,Q<=1.
```

The remaining D8/O8 calculation has to compute the pair
`(x_Gamma,Q,L_Q)` from the localized boundary action; then
`R_Gamma^2=2Z_chi,max x_Gamma,Q/(kappa_8L_Q)`.

Report 22 gives the sector-sum data as a finite trace-density package:

```text
H_S=oplus_{s in S_Gamma} C|s>,
W_Gamma|s>=omega_s e^-phi_s|s>,
R_Gamma|s>=r_Gamma,s^2|s>.
```

It gives

```text
e^-phi_0 Omega_Gamma=Tr_S W_Gamma,
R_Gamma^2=Tr_S(W_Gamma R_Gamma),
x_Gamma,Q=kappa_8L_QTr_S(W_Gamma R_Gamma)/(2Z_chi,max).
```

Writing `T_Gamma=Tr_S(W_Gamma R_Gamma)`, the active pass surface is

```text
T_Gamma>=441u_Gamma^sh(varrho_Gamma)/(8pi^2kappa_8),
0<L_Q<=2Z_chi,max/(kappa_8T_Gamma).
```

Equivalently:

```text
L_Q=2Z_chi,max x_Gamma,Q/(kappa_8T_Gamma),
0<x_Gamma,Q<=1.
```

At lower-density saturation:

```text
T_Gamma=441u_Gamma^sh(varrho_Gamma)/(8pi^2kappa_8),
L_Q=x_Gamma,Q L_Q,max(varrho_Gamma).
```

Density-ratio form:

```text
chi_Gamma=T_Gamma/T_Gamma,min(varrho_Gamma)>=1,
L_Q=(x_Gamma,Q/chi_Gamma)L_Q,max(varrho_Gamma),
x_Gamma,Q=chi_Gamma L_Q/L_Q,max(varrho_Gamma),
0<L_Q<=L_Q,max(varrho_Gamma)/chi_Gamma.
```

Sector variables:

```text
zeta_Gamma,s=omega_s e^-phi_s r_Gamma,s^2/T_Gamma,min(varrho_Gamma)>=0,
chi_Gamma=sum_s zeta_Gamma,s,
L_Q=x_Gamma,Q L_Q,max(varrho_Gamma)/sum_s zeta_Gamma,s.
```

Fixed-loop interval:

```text
x_Gamma,Q=(L_Q/L_Q,max(varrho_Gamma))sum_s zeta_Gamma,s,
1<=sum_s zeta_Gamma,s<=L_Q,max(varrho_Gamma)/L_Q.
```

Sector-fraction radius readout:

```text
p_Gamma,s=zeta_Gamma,s/chi_Gamma,
p_Gamma,s>=0,
sum_s p_Gamma,s=1,
omega_s e^-phi_s r_Gamma,s^2=p_Gamma,s chi_Gamma T_Gamma,min(varrho_Gamma),
r_Gamma,s^2=441p_Gamma,s chi_Gamma u_Gamma^sh(varrho_Gamma)/
(8pi^2 kappa_8 omega_s e^-phi_s).
```

Report 23 adds the localized readout equality.  With

```text
W_s r_Gamma,s^2=p_Gamma,s chi_Gamma T_Gamma,min(varrho_Gamma)
```

and the normal-form current coframes, the DBI density gives
`T_Gamma^rd=chi_Gamma T_Gamma,min`, the coframe quotient gives
`varrho_Gamma`, the endpoint blocks give `R_epsilon=R_g=R_chi=0`, and
`L_Q=(x_Gamma,Q/chi_Gamma)L_Q,max` gives `R_x=0`.

The next evidence row is the global type-I' extension with flux quantization
and the boundary Dirac-Dolbeault origin of `B_sigma,B_chi`.
The article now states this row as `R_per,s=0`, `R_DD=0`, and
`Q_lower^tot=0`.

Finite data certificate:

```text
D_Gamma=(S_Gamma; omega_s,phi_s,p_Gamma,s,b_Gamma,s,rho_Gamma,s;
chi_Gamma,x_Gamma,Q,L_Q; m_sigma,epsilon_sigma,Q,lambda_sigma,alpha).
```

```text
varrho_Gamma=sum_{s in S_Gamma,0} b_Gamma,s rho_Gamma,s,
T_Gamma=chi_Gamma T_Gamma,min(varrho_Gamma),
L_Q=(x_Gamma,Q/chi_Gamma)L_Q,max(varrho_Gamma),
z_chi=F^{-1}(x_Gamma,Q^4),
epsilon_sigma,Q^2=||Pi_eta_Q^perp B_sigma^dagger B_sigma eta_Q||^2/
(m_sigma^2||eta_Q||^2),
g_sigma,perp=min_alpha lambda_sigma,alpha/m_sigma.
```

```text
chi_Gamma>=1,
0<x_Gamma,Q<=1,
0<varrho_Gamma<varrho_c,
epsilon_sigma,Q=0,
g_sigma,perp>1,
sum_s p_Gamma,s=1,
sum_{s in S_Gamma,0}b_Gamma,s=1,
p_Gamma,s,b_Gamma,s,rho_Gamma,s>=0.
```

Action-to-certificate extraction:

```text
Q_Gamma^(2)=(S_Gamma; omega_s,phi_s,gamma_Gamma,s^CP2;
theta_Gamma,s^3,P_0^Gamma,P_h^Gamma,Pi_Q; B_sigma,eta_Q,L_Q),
Efrak_Gamma(Q_Gamma^(2))=D_Gamma.
```

```text
Av_{s,Pi_Q}(f)=int_CP2_s sqrt(hat gamma_s) tr_Es(Pi_Q f Pi_Q)/
int_CP2_s sqrt(hat gamma_s) tr_Es(Pi_Q),
r_Gamma,s^2=Av_{s,Pi_Q}[(1/4)tr_hat gamma_s gamma_Gamma,s^CP2],
T_Gamma=sum_s omega_s e^-phi_s r_Gamma,s^2,
varrho_Gamma=sum_s C_h,s^Gamma/sum_s C_0,s^Gamma,
x_Gamma,Q=kappa_8L_QT_Gamma/(2Z_chi,max),
epsilon_sigma,Q^2=||Pi_eta_Q^perp B_sigma^dagger B_sigma eta_Q||^2/
(m_sigma^2||eta_Q||^2),
{lambda_sigma,alpha}=Spec(Pi_eta_Q^perp B_sigma^dagger B_sigma Pi_eta_Q^perp).
```

Algebraic inverse packet:

```text
S_Gamma,+={s:p_Gamma,s>0},
gamma_Gamma,s^CP2=r_Gamma,s^2 hat gamma_s,
r_Gamma,s^2=p_Gamma,s chi_Gamma T_Gamma,min(varrho_Gamma)/
(omega_s e^-phi_s).
```

```text
P_0^Gamma theta_Gamma,s^3
=(b_Gamma,s C_Gamma/(omega_s e^-phi_s))^(1/2)hat e_0,s,
P_h^Gamma theta_Gamma,s^3
=(b_Gamma,s rho_Gamma,s C_Gamma/(omega_s e^-phi_s))^(1/2)hat e_h,s.
```

```text
B_sigma^dagger B_sigma
=m_sigma |e_0><e_0|+sum_alpha lambda_sigma,alpha |e_alpha><e_alpha|,
Ifrak_Gamma(D_Gamma;C_Gamma,hat e)=Q_Gamma^(2),
Efrak_Gamma(Ifrak_Gamma(D_Gamma;C_Gamma,hat e))=D_Gamma.
```

Charged determinant extension:

```text
z_chi=F^{-1}(x_Gamma,Q^4),
M_chi=z_chi/L_H,
E_chi=C,
sigma_chi d_chi=+1.
```

```text
P_1^chi=span{u,v},
P_2^chi=span{u^2,v^2},
B_chi^dagger B_chi=M_chi^2 1_E_chi,
B_{r,Gamma}^chi=1_{P_r^chi} tensor B_chi.
```

```text
N_Gamma^chi=2F(M_chiL_H)=2x_Gamma,Q^4,
Qtilde_Gamma^(2)
=(Q_Gamma^(2);P_1^chi,P_2^chi,E_chi,B_chi,L_H,sigma_chi d_chi).
```

Finite action residual:

```text
A_Gamma=(P_s[G+B],F_s,phi_s,omega_s,Pi_s; iota_Gamma^*C_1;
B_sigma,B_chi,L_Q,L_H)_{s in S_Gamma},
R_Gamma(A_Gamma;D_Gamma)=(R_T,R_x,R_varrho,R_epsilon,R_g,R_chi).
```

```text
R_T=T_Gamma(A_Gamma)/T_Gamma,min(varrho_Gamma)-chi_Gamma,
R_x=kappa_8L_QT_Gamma(A_Gamma)/(2Z_chi,max)-x_Gamma,Q,
R_varrho=C_h^Gamma(A_Gamma)/C_0^Gamma(A_Gamma)-varrho_Gamma.
```

```text
R_epsilon=epsilon_sigma,Q,
R_g=max{0,1-min_alpha lambda_sigma,alpha/m_sigma},
R_chi=(M_chiL_H-z_chi)/(1+z_chi).
```

Completion row:

```text
R_Gamma(A_Gamma;D_Gamma)=0.
```

Current passes add the endpoint-character charge period and the DBI
sector-sum inner product:

```text
<X,Y>_Gamma
=sum_s int dnu_Gamma,s gamma_s^mn tr_Es(Pi_s X_m,s Pi_s Y_n,s).
```

This identifies

```text
K_AB^Gamma=<theta_Gamma^A,theta_Gamma^B>_Gamma,
G_AB^(psi)=<psi_sigma theta_Gamma^A,psi_sigma theta_Gamma^B>_Gamma,
Z_Gamma,0=<eta_0,eta_0>_Gamma,
M_img=Q_Gamma,sigma^dagger Q_Gamma,sigma.
```

It also fixes the retained local sector row:

```text
W_Q=H0(CP1,O(Q)), E_Q=(W_Q op W_Q^vee)^Omega,
Q=7 -> rk_C(E_Q^C)=16, q_8^net=0, k=0.
```

The row projectors are:

```text
Pi_Q=P_Omega P_E_Q,
Pi_sigma=|e_sigma><e_sigma|,
Pi_chi=P_1^chi+P_2^chi.
```

Current pass also adds the endpoint reality operator:

```text
J_n e_k=(-1)^k e_{n-k}, J_n^2=(-1)^n,
Omega_n(s,lambda)=(J_n^-1 lambda,J_n s).
```

It gives:

```text
Tr P_Omega,1 P_1^chi=2,
Tr P_Omega,2 P_2^chi=2,
d_1=d_2=d_chi.
```

Current pass adds the charged oscillator spectrum:

```text
lambda_{ell,r}=p_E^2+M_chi^2+(2pi ell+rx)^2/L_H^2,
r=1,2, ell in Z.
```

The determinant row reads:

```text
sigma_chi=+1,
N_Gamma^chi=2d_chi F(M_chi L_H).
```

Current pass also adds the RR/current coframe extraction:

```text
theta_Gamma^A=theta_Gamma,CP^A+q_A^-1 Pi_A iota_Gamma^*C_1,
d_Gamma theta_Gamma^A=d_Gamma theta_Gamma,CP^A+q_A^-1 Pi_A iota_Gamma^*F_2.
```

It reads out:

```text
L_Q^2=(1,1)L_Gamma(1,1)^T,
det L_Gamma=R_dV K_33^Gamma L_Q^2.
```

Current pass adds the CS source polynomial:

```text
Y_Gamma=N8[1+f_m h_Q+(f_m^2/2-1/16)h_Q^2],
qfrak_C1=N8(f_m^2/2-1/16).
```

For the minimal spin-c local stack:

```text
m=0, N8=16 -> qfrak_C1=337.
```

The projected coframe solve is now:

```text
Pi_A iota_Gamma^*C_1
=Pi_A C_{1,harm}+mu8 G_{1,Gamma}I_{1,A}^perp.
```

with compact zero-mode condition:

```text
<I_{1,A}^Gamma,omega_Q>_Gamma=0.
```

Current pass also adds the finite Green coframe readout:

```text
G_{1,Gamma}I_{1,A}^perp=sum_i B_Ai lambda_i^-1 alpha_i.
```

It turns the current matrix into finite spectral data:

```text
(h_A,Omega_Q,p_A,K_AB^CP,B_Ai,P_Ai,lambda_i,q_A),
A,B=3,Y.
```

Current pass adds the `S1_Q` Fourier source test:

```text
lambda_n=(2pi n/L_Q)^2,
K_AB^Green=mu8^2 q_A^-1 q_B^-1
sum_n(a_A,n a_B,n+b_A,n b_B,n)/lambda_n^2.
```

Constant spin-c source gives zero perpendicular Fourier content, so the
nonzero sourced vertical row now targets O8/bulk Fourier profile or harmonic
`h_A`.

Current pass starts Report 19 and adds the harmonic current closure equation:

```text
L_AB^Gamma=Chat_AB+v_A p_B+v_B p_A+Omega_Q v_Av_B,
v_A=q_A^-1 h_A.
```

In the product orthogonal specialization:

```text
L^Gamma=C+Omega_Q vv^T,
L_{2,vert}^2=Omega_Q v_3^2.
```

For a fixed direction `t=v_Y/v_3`, the vertical amplitude
`u=Omega_Qv_3^2` satisfies

```text
A_tu^2+B_tu+D_C=0.
```

The massive-neutral harmonic row has

```text
v_Y=-v_3,
L_Q^2=C_Q,
u_N=D_C/((1-R_dV)C_Q).
```

The `Q`-parallel harmonic row has

```text
v_Y=v_3,
4R_dV u^2+(R_dV(4C_33+C_Q)-C_N)u+D_C=0.
```

With `int_{S1_Q}omega_Q=1`, the harmonic coefficients can be written as

```text
Pi_A C_{1,harm}=2pi vartheta_A omega_Q,
vartheta_A in R/Z.
```

Then

```text
v_A=2pi q_A^-1 vartheta_A,
t=q_3 vartheta_Y/(q_Y vartheta_3),
u=(2pi)^2 Omega_Q q_3^-2 vartheta_3^2.
```

For the product DBI row,

```text
Omega_Q=Z_Gamma,Q/L_Q,
L_{2,vert}^2=(2pi)^2 Z_Gamma,Q L_Q^-1 q_3^-2 vartheta_3^2.
```

Using `tau_Q=Z_Gamma,Q/Z_Gamma,0`,

```text
L_{2,vert}^2=(2pi)^2 tau_Q Z_Gamma,0 L_Q^-1 q_3^-2 vartheta_3^2.
```

For a shared CP2 density profile and normalized endpoint vector,
`tau_Q=tr_E_Q Pi_Q`; at `Q=7`, the full retained trace gives `tau_Q=16`.

Using `q_3=3Q` and the full trace `tau_Q=2(Q+1)`,

```text
L_{2,vert}^2=
8pi^2(Q+1)Z_Gamma,0 delta_vartheta_3^2/(9Q^2L_Q).
```

At `Q=7`,

```text
delta_vartheta_3=(21/(8pi))sqrt(L_Q L_{2,vert}^2/Z_Gamma,0).
```

The Wilson chamber requires

```text
L_{2,vert}^2<=(16pi^2/441)Z_Gamma,0/L_Q.
```

The density-per-loop inversion is now

```text
Xi_Q^harm=Z_Gamma,0/(L_Q L_{2,vert}^2)
=9Q^2/(8pi^2(Q+1)delta_vartheta_3^2).
```

At `Q=7`, the fundamental Wilson chamber gives

```text
Xi_7^harm>=441/(16pi^2)=2.792665124141....
```

For the photon-preserving massive-neutral identity chamber,

```text
delta_vartheta_Y=-(q_Y/q_3)delta_vartheta_3,
\qquad
Theta_N=(1/2)min(1,|q_3/q_Y|),
```

and

```text
Xi_Q^harm>=9Q^2/(8pi^2(Q+1)Theta_N^2).
```

Combining the chamber with

```text
u_N=D_C/((1-R_dV)C_Q)
```

gives the direct density condition

```text
Z_Gamma,0/L_Q>=9Q^2D_C/(8pi^2(Q+1)Theta_N^2(1-R_dV)C_Q).
```

At `Q=7`,

```text
Z_Gamma,0/L_Q>=441D_C/(64pi^2Theta_N^2(1-R_dV)C_Q).
```

For the point-evaluation base row,

```text
q=lambda^2,
C_33^pt=1+(Q^2+1)q/(Q+1)^2,
C_Q^pt=(Q+1)^2C_33^pt,
Delta_C^pt=(Q-1)^2q(q+2).
```

At `Q=7`,

```text
u_N^pt(q)=[R_dV(25q+32)^2-576q(q+2)]/
[32(1-R_dV)(25q+32)].
```

This amplitude vanishes at

```text
q_c=3.511614004347....
```

The derivative is negative on `q>0`:

```text
du_N^pt/dq=-[(14400-15625R_dV)q^2+(36864-40000R_dV)q+
(36864-25600R_dV)]/[32(1-R_dV)(25q+32)^2].
```

The positive branch decreases from

```text
u_N^pt(0)=R_dV/(1-R_dV)=3.482268368857...
```

to zero at `q_c`.

The corresponding density condition is

```text
Z_Gamma,0/L_Q>=441[R_dV(25q+32)^2-576q(q+2)]/
[2048pi^2Theta_N^2(1-R_dV)(25q+32)].
```

Set

```text
U_Gamma=64pi^2Theta_N^2 Z_Gamma,0/(441L_Q).
```

The saturation curve solves

```text
A_q q^2+B_q(U_Gamma)q+C_q(U_Gamma)=0,
```

where

```text
A_q=576-625R_dV,
B_q=1152-1600R_dV+800(1-R_dV)U_Gamma,
C_q=1024((1-R_dV)U_Gamma-R_dV).
```

The positive branch is

```text
q_sat=(-B_q+sqrt(B_q^2-4A_qC_q))/(2A_q).
```

The chamber pass is

```text
q_sat<=q<q_c,
\qquad
delta_vartheta_3^2=Theta_N^2u_N^pt(q)/U_Gamma.
```

## Cross-Vector Massive-Neutral Extension

The product specialization can be lifted to nonzero CP--circle overlap
`p_A`.  In the photon-preserving direction

```text
v=a(1,-1)^T,
```

write

```text
C=[[A,B],[B,D]],  C_Q=A+2B+D,  p_Q=p_3+p_Y,
S_p=p_3(D+B)-p_Y(A+B).
```

Then

```text
det(C+vp^T+pv^T+Omega_Q vv^T)
=Delta_C+2aS_p+a^2(Omega_QC_Q-p_Q^2).
```

The branch condition is

```text
((1-R_dV)Omega_QC_Q-p_Q^2)a^2
+2(S_p-R_dV p_3C_Q)a-D_C=0.
```

Using `u=Omega_Qa^2`, `epsilon=sign(a)`, and `y=sqrt(u)`, the local pass
equation becomes

```text
A_Ny^2+2epsilon B_Ny-D_C=0,
A_N=(1-R_dV)C_Q-p_Q^2/Omega_Q,
B_N=(S_p-R_dV p_3C_Q)/sqrt(Omega_Q).
```

This moves the unresolved product-orthogonality input into two computed
overlap scalars.  Required evidence: compute `p_3`, `p_Y`, and `Omega_Q` from
the localized D8/O8 density and retained CP coframe.

## DBI Cross-Vector Readout

For `theta_{Gamma,CP}^A=theta_i^A dy^i` and `omega_Q=ds_Q/L_Q`, the localized
DBI inner product gives

```text
p_A=L_Q^-1 sum_sigma int dnu_{Gamma,sigma}
gamma_sigma^{is_Q} tr(Pi_Q theta_i^A Pi_Q),
Omega_Q=L_Q^-2 sum_sigma int dnu_{Gamma,sigma}
gamma_sigma^{s_Qs_Q} tr Pi_Q.
```

Hence a block-product internal metric proves

```text
p_3=p_Y=0,
Omega_Q=Z_Gamma,Q/L_Q.
```

Remaining evidence: derive the actual D8/O8 pulled-back metric and retained
current-frame projection.  In an adapted `Q`-circle coframe, a measured
nonzero `p_A` comes from vertical leakage of the CP coframe or retained
off-diagonal frame contribution.

## Leakage Projection Result

The leakage coefficient is

```text
ell_A=gamma_Gamma^-1(theta_Gamma,CP^A,chi_Q)/
gamma_Gamma^-1(chi_Q,chi_Q).
```

For the product carrier, `theta_Gamma,CP^A=pi_CP2^* alpha_A` and the adapted
metric `ds_Gamma^2=g_ij dy^i dy^j+L_Q^2 chi_Q^2` give

```text
ell_3=ell_Y=0,
p_3=p_Y=0,
Omega_Q=Z_Gamma,Q/L_Q.
```

Thus the active product-carrier row returns to the product harmonic closure.
A leakage branch remains available as a separate realization with an explicit
`chi_Q` component in the retained CP coframe.

## Charge-Chamber Specialization

The D9 descent fixes `q_3=3Q`, hence `q_3=21` for the retained `Q=7` stack.
The photon-preserving chamber radius is

```text
Theta_N(21,q_Y)=(1/2)min(1,|21/q_Y|).
```

Consequently,

```text
Theta_N=1/2                 for |q_Y|<=21,
Theta_N=21/(2|q_Y|)         for |q_Y|>21.
```

The product-carrier density filter is

```text
Z_Gamma,0/L_Q >= 441 u_N^pt(q)/(16pi^2)        for |q_Y|<=21,
Z_Gamma,0/L_Q >= q_Y^2 u_N^pt(q)/(16pi^2)      for |q_Y|>21.
```

Line data in the retained `Q=7` row obey

```text
c_1(L_Y)=6h+Q eta,
c_1(L_T3)=eta,
c_1(L_Y)-Q c_1(L_T3)=6h.
```

Endpoint-character extraction then gives

```text
T_3 eta_Q=-(Q/2)eta_Q,
Y eta_Q=(Q/2)eta_Q,
q_Y=3Q=21.
```

Quotient line-operator extraction gives the same period.  Define

```text
O_Y(gamma_Q)=Hol_LY(gamma_Q)Hol_LT3(gamma_Q)^(-Q).
```

Its Chern class is `6h`, so its `S1_Q` character is unit.  Therefore

```text
Hol_LY(gamma_Q)=Hol_LT3(gamma_Q)^Q.
```

For `eta_Q=eta_0^{odot Q}`, the integer hypercharge charge is

```text
y eta_Q=3Q eta_Q.
```

Thus

```text
Theta_N(21,21)=1/2,
delta_vartheta_Y=-delta_vartheta_3,
Z_Gamma,0/L_Q >= 441 u_N^pt(q)/(16pi^2).
```

Equivalently,

```text
U_Gamma^(21)=16pi^2 Z_Gamma,0/(441L_Q),
U_Gamma^(21)>=u_N^pt(q),
delta_vartheta_3^2=delta_vartheta_Y^2=u_N^pt(q)/(4U_Gamma^(21)).
```

In the product metric row,

```text
Z_Gamma,0=L_Q Z_Gamma,0^CP2,
Z_Gamma,0^CP2=sum_s int_CP2,s dmu_Gamma,s^CP2 tr(Pi_Q |eta_Q|^2 Pi_Q).
```

Therefore

```text
U_Gamma^(21)=16pi^2 Z_Gamma,0^CP2/441,
Z_Gamma,0^CP2 >= 441 u_N^pt(q)/(16pi^2).
```

With common endpoint density and unit rank-one normalization,

```text
Z_Gamma,0^CP2=zfrak_Gamma^CP2,
Z_Gamma,Q^CP2=16 zfrak_Gamma^CP2,
tau_Q=16.
```

For a constant product profile,

```text
zfrak_Gamma^CP2=kappa_8 sum_s omega_s e^-phi_s Vol(CP2_s,gamma_CP2,s).
```

The common-profile density-dominated pass is

```text
kappa_8 e^-phi_0 Omega_Gamma Vol(CP2,gamma_CP2)
>=9.724809426610...,
Omega_Gamma=sum_s omega_s.
```

Using `int_CP2 h_Q^2=1` and `J_Gamma,s=r_Gamma,s h_Q`,

```text
Vol(CP2_s)=r_Gamma,s^2/2.
```

The metric-scale pass is

```text
sum_s omega_s e^-phi_s r_Gamma,s^2
>=19.449618853220.../kappa_8,
```

and the common-profile form is

```text
r_Gamma^2>=19.449618853220.../(kappa_8 e^-phi_0 Omega_Gamma).
```

Point-row shape readout:

```text
theta_Gamma^3=theta_3,0+theta_3,h,
<theta_3,0,theta_3,h>_Gamma=0,
q_Gamma=((Q+1)^2/(Q^2+1))(C_h^Gamma/C_0^Gamma).
```

For `Q=7`,

```text
q_Gamma=(32/25)(C_h^Gamma/C_0^Gamma).
```

Set

```text
varrho_Gamma=C_h^Gamma/C_0^Gamma.
```

Coframe-projection extraction:

```text
C_0^Gamma
=<P_0^Gamma theta_Gamma^3,P_0^Gamma theta_Gamma^3>_{Gamma,Pi_Q},
C_h^Gamma
=<P_h^Gamma theta_Gamma^3,P_h^Gamma theta_Gamma^3>_{Gamma,Pi_Q}.
```

Thus

```text
varrho_Gamma
=<P_h^Gamma theta_Gamma^3,P_h^Gamma theta_Gamma^3>_{Gamma,Pi_Q}
/<P_0^Gamma theta_Gamma^3,P_0^Gamma theta_Gamma^3>_{Gamma,Pi_Q},
C_0^Gamma>0.
```

Sector coframe row:

```text
C_0,s^Gamma=omega_s e^-phi_s
<P_0^Gamma theta_Gamma,s^3,P_0^Gamma theta_Gamma,s^3>_{s,Pi_Q},
C_h,s^Gamma=omega_s e^-phi_s
<P_h^Gamma theta_Gamma,s^3,P_h^Gamma theta_Gamma,s^3>_{s,Pi_Q}.
```

```text
C_0^Gamma=sum_s C_0,s^Gamma,
C_h^Gamma=sum_s C_h,s^Gamma,
varrho_Gamma=sum_s C_h,s^Gamma/sum_s C_0,s^Gamma.
```

```text
b_Gamma,s=C_0,s^Gamma/C_0^Gamma,
rho_Gamma,s=C_h,s^Gamma/C_0,s^Gamma,
b_Gamma,s>=0,
sum_{s in S_Gamma,0} b_Gamma,s=1,
varrho_Gamma=sum_{s in S_Gamma,0} b_Gamma,s rho_Gamma,s.
```

Then

```text
q_Gamma=(32/25)varrho_Gamma,
0<varrho_Gamma<varrho_c,
varrho_c=(25/32)q_c=2.743448440896....
```

The density-shape amplitude is

```text
u_Gamma^sh(varrho_Gamma)
=[625R_dV(1+varrho_Gamma)^2
-576varrho_Gamma^2-900varrho_Gamma]/
[625(1-R_dV)(1+varrho_Gamma)].
```

The localized chamber pass becomes

```text
U_Gamma^CP2>=u_Gamma^sh(varrho_Gamma),
0<varrho_Gamma<varrho_c.
```

Equivalently,

```text
Z_Gamma,0^CP2 >= (441/(16pi^2))u_Gamma^sh(varrho_Gamma).
```

The density-dominated pass is

```text
Z_Gamma,0^CP2 >= 9.724809426610....
```

For lower positive density,

```text
U_Gamma^CP2=16pi^2 Z_Gamma,0^CP2/441,
q_sat(U_Gamma^CP2)<=q<q_c.
```

Remaining localized evidence: compute `zfrak_Gamma^CP2`,
`C_h^Gamma/C_0^Gamma`, and the image operator data from the D8/O8 density row.

The previous pass added the minimal local realization packet:

```tex
P_Gamma,sigma
=
(dnu_Gamma,psi_sigma,m_sigma,Xi_sigma,G^(psi),Z_Gamma,0,N_Gamma^chi).
```

The required image readout is

```tex
int_Gamma dnu_Gamma |psi_sigma|^2=1,
\qquad
M_img psi_sigma=m_sigma psi_sigma,
\qquad
m_sigma>0,
```

and

```tex
L_2^-1 int_Gamma dnu_Gamma psi_sigma
gamma_Gamma^-1(theta_Gamma^A,Xi_sigma)
=(g_sigma)_A,
\qquad A=3,Y.
```

Constant-profile normalized source mode:

```tex
psi_Gamma,0=(L_Q zfrak_Gamma^CP2)^(-1/2) eta_Q,
\qquad
int_Gamma dnu_Gamma tr(Pi_Q |psi_Gamma,0|^2 Pi_Q)=1.
```

Taking `e_sigma=psi_Gamma,0` and

```tex
J_A^(sigma)=L_2 sqrt(m_sigma)(g_sigma)_A e_sigma^flat
```

gives

```tex
C_Asigma=L_2 sqrt(m_sigma)(g_sigma)_A,
\qquad
D_AB=(g_sigma)_A(g_sigma)_B.
```

For

```tex
G_AB^(0)=int_Gamma dnu_Gamma psi_Gamma,0^2
gamma_Gamma^-1(theta_Gamma^A,theta_Gamma^B),
```

the Gram-dual image one-form is

```tex
Xi_sigma=L_2 psi_Gamma,0 (G^(0))^{-1 BC}(g_sigma)_C theta_Gamma^B.
```

It gives

```tex
R_Xi,sigma=0.
```

Single-pass constant-profile packet:

```tex
P_Gamma^cp
=
(kappa_8,e^-phi_0 Omega_Gamma,r_Gamma,L_Q,
varrho_Gamma,m_sigma,z_chi,sigma_chi d_chi).
```

Density-sector extraction:

```tex
e^-phi_0 Omega_Gamma=sum_s omega_s e^-phi_s,
\qquad
Omega_Gamma=sum_s omega_s.
```

Common-row dilaton:

```tex
e^-phi_0=(sum_s omega_s e^-phi_s)/(sum_s omega_s).
```

The endpoint trace factor stays as `tau_Q=16`.

The packet returns

```tex
zfrak_Gamma^CP2=(1/2)kappa_8 e^-phi_0 Omega_Gamma r_Gamma^2,
Z_Gamma,0=L_Q zfrak_Gamma^CP2,
Z_Gamma,Q=16L_Q zfrak_Gamma^CP2,
Z_Gamma,H=(Q/4)Z_Gamma,0,
q_Gamma=(32/25)varrho_Gamma,
U_Gamma^CP2=(16pi^2/441)zfrak_Gamma^CP2.
```

It also returns

```tex
psi_sigma=psi_Gamma,0,
M_img psi_sigma=m_sigma psi_sigma,
N_Gamma^chi=2sigma_chi d_chi F(z_chi).
```

Endpoint image-spectrum extraction:

```tex
M_img=Q_img^dagger Q_img,
\qquad
Q_img=1_{CP2 x S1_Q} tensor B_sigma,
```

```tex
m_sigma
=<eta_Q,B_sigma^dagger B_sigma eta_Q>_{E_Q}
/<eta_Q,eta_Q>_{E_Q}.
```

The one-line image condition is

```tex
B_sigma^dagger B_sigma eta_Q=m_sigma eta_Q,
\qquad
Pi_sigma^perp B_sigma^dagger B_sigma eta_Q=0,
\qquad
m_sigma>0.
```

Endpoint normal form:

```tex
Pi_eta_Q=|eta_Q><eta_Q|/<eta_Q,eta_Q>_{E_Q},
\qquad
Pi_eta_Q^perp=1_{E_Q}-Pi_eta_Q.
```

```tex
B_sigma^dagger B_sigma
=m_sigma Pi_eta_Q+B_sigma,perp^dagger B_sigma,perp,
\qquad
B_sigma,perp=Pi_eta_Q^perp B_sigma,perp Pi_eta_Q^perp.
```

Complement separation:

```tex
B_sigma,perp^dagger B_sigma,perp>=M_sigma,perp^2 Pi_eta_Q^perp,
\qquad
M_sigma,perp^2>m_sigma.
```

Endpoint gap ratio:

```tex
g_sigma,perp=M_sigma,perp^2/m_sigma,
\qquad
g_sigma,perp>1.
```

For diagonal endpoint spectrum on `Pi_eta_Q^perp E_Q`,

```tex
B_sigma^dagger B_sigma e_sigma,alpha
=lambda_sigma,alpha e_sigma,alpha,
\qquad
g_sigma,perp=min_alpha lambda_sigma,alpha/m_sigma.
```

Minimal positive determinant block:

```tex
B_chi^dagger B_chi=M_chi^2 1_E_chi,
E_chi=C,
sigma_chi d_chi=+1.
```

With

```tex
Xi_Gamma^cp
=[21375.716460702053... lambda_F/(2w_H^8)]
(L_Q zfrak_Gamma^CP2/v_EW)^4,
```

the determinant threshold pass is

```tex
0<Xi_Gamma^cp<=1,
z_chi=F^{-1}(Xi_Gamma^cp).
```

Neutral-density upper constraint:

```tex
0<Z_Gamma,0=L_Q zfrak_Gamma^CP2<=Z_chi,max,
\qquad
Z_chi,max=v_EW[2w_H^8/(21375.716460702053... lambda_F)]^(1/4)
=0.0983506713707568... w_H^2 lambda_F^(-1/4)v_EW.
```

Together with the density-shape lower row:

```tex
0<L_Q<=Z_chi,max/zfrak_Gamma^CP2
<=16pi^2 Z_chi,max/(441 u_Gamma^sh(varrho_Gamma)).
```

Equivalent radius band:

```tex
441u_Gamma^sh(varrho_Gamma)/(8pi^2 kappa_8 e^-phi_0 Omega_Gamma)
<=r_Gamma^2
<=2Z_chi,max/(kappa_8 e^-phi_0 Omega_Gamma L_Q).
```

Full sector-sum reduction:

```tex
R_Gamma^2=sum_s omega_s e^-phi_s r_Gamma,s^2,
\qquad
zfrak_Gamma^CP2=(kappa_8/2)R_Gamma^2.
```

Sector-sum compactification band:

```tex
441u_Gamma^sh(varrho_Gamma)/(8pi^2 kappa_8)
<=R_Gamma^2
<=2Z_chi,max/(kappa_8 L_Q).
```

Trace-density row:

```tex
H_S=oplus_{s in S_Gamma} C|s>,
\qquad
W_Gamma|s>=omega_s e^-phi_s|s>,
\qquad
R_Gamma|s>=r_Gamma,s^2|s>.
```

```tex
e^-phi_0 Omega_Gamma=Tr_S W_Gamma,
\qquad
R_Gamma^2=Tr_S(W_Gamma R_Gamma).
```

```tex
Z_Gamma,0=(kappa_8L_Q/2)Tr_S(W_Gamma R_Gamma),
\qquad
Z_Gamma,Q=8kappa_8L_QTr_S(W_Gamma R_Gamma),
```

```tex
Z_Gamma,H=(Qkappa_8L_Q/8)Tr_S(W_Gamma R_Gamma).
```

Set

```tex
T_Gamma=Tr_S(W_Gamma R_Gamma).
```

The trace pass surface is

```tex
T_Gamma>=441u_Gamma^sh(varrho_Gamma)/(8pi^2kappa_8),
\qquad
0<L_Q<=2Z_chi,max/(kappa_8T_Gamma).
```

Equivalently, with `0<x_Gamma,Q<=1`,

```tex
L_Q=2Z_chi,max x_Gamma,Q/(kappa_8T_Gamma).
```

At lower-density saturation,

```tex
T_Gamma=441u_Gamma^sh(varrho_Gamma)/(8pi^2kappa_8),
\qquad
L_Q=x_Gamma,Q L_Q,max(varrho_Gamma).
```

Density-ratio form:

```tex
chi_Gamma=T_Gamma/T_Gamma,min(varrho_Gamma)>=1,
\qquad
L_Q=(x_Gamma,Q/chi_Gamma)L_Q,max(varrho_Gamma),
```

```tex
x_Gamma,Q=chi_Gamma L_Q/L_Q,max(varrho_Gamma),
\qquad
0<L_Q<=L_Q,max(varrho_Gamma)/chi_Gamma.
```

Sector variables:

```tex
zeta_Gamma,s=omega_s e^-phi_s r_Gamma,s^2/T_Gamma,min(varrho_Gamma)>=0,
\qquad
chi_Gamma=sum_s zeta_Gamma,s,
```

```tex
L_Q=x_Gamma,Q L_Q,max(varrho_Gamma)/sum_s zeta_Gamma,s.
```

Fixed-loop interval:

```tex
x_Gamma,Q=(L_Q/L_Q,max(varrho_Gamma))sum_s zeta_Gamma,s,
\qquad
1<=sum_s zeta_Gamma,s<=L_Q,max(varrho_Gamma)/L_Q.
```

Sector-fraction radius readout:

```tex
p_Gamma,s=zeta_Gamma,s/chi_Gamma,
\qquad
p_Gamma,s>=0,
\qquad
sum_s p_Gamma,s=1,
```

```tex
omega_s e^-phi_s r_Gamma,s^2
=p_Gamma,s chi_Gamma T_Gamma,min(varrho_Gamma),
```

```tex
r_Gamma,s^2=441p_Gamma,s chi_Gamma u_Gamma^sh(varrho_Gamma)/
(8pi^2 kappa_8 omega_s e^-phi_s).
```

Finite data certificate:

```tex
D_Gamma=(S_Gamma; omega_s,phi_s,p_Gamma,s,b_Gamma,s,rho_Gamma,s;
chi_Gamma,x_Gamma,Q,L_Q; m_sigma,lambda_sigma,alpha).
```

```tex
varrho_Gamma=sum_{s in S_Gamma,0} b_Gamma,s rho_Gamma,s,
\qquad
T_Gamma=chi_Gamma T_Gamma,min(varrho_Gamma),
```

```tex
L_Q=(x_Gamma,Q/chi_Gamma)L_Q,max(varrho_Gamma),
\qquad
z_chi=F^{-1}(x_Gamma,Q^4),
\qquad
g_sigma,perp=min_alpha lambda_sigma,alpha/m_sigma.
```

```tex
chi_Gamma>=1,\quad
0<x_Gamma,Q<=1,\quad
0<varrho_Gamma<varrho_c,\quad
g_sigma,perp>1.
```

```tex
sum_s p_Gamma,s=1,\qquad
sum_{s in S_Gamma,0}b_Gamma,s=1,\qquad
p_Gamma,s,b_Gamma,s>=0.
```

Sector coframe row:

```tex
C_0,s^Gamma=omega_s e^-phi_s
<P_0^Gamma theta_Gamma,s^3,P_0^Gamma theta_Gamma,s^3>_{s,Pi_Q},
```

```tex
C_h,s^Gamma=omega_s e^-phi_s
<P_h^Gamma theta_Gamma,s^3,P_h^Gamma theta_Gamma,s^3>_{s,Pi_Q}.
```

```tex
C_0^Gamma=sum_s C_0,s^Gamma,
\qquad
C_h^Gamma=sum_s C_h,s^Gamma,
\qquad
varrho_Gamma={sum_s C_h,s^Gamma\over sum_s C_0,s^Gamma}.
```

```tex
b_Gamma,s=C_0,s^Gamma/C_0^Gamma,
\qquad
rho_Gamma,s=C_h,s^Gamma/C_0,s^Gamma,
\qquad
varrho_Gamma=sum_{s in S_Gamma,0} b_Gamma,s rho_Gamma,s.
```

Product-threshold row:

```tex
V_Gamma,Q=L_QR_Gamma^2,
\qquad
Z_Gamma,0=(kappa_8/2)V_Gamma,Q.
```

```tex
Xi_Gamma^cp
=(Z_Gamma,0/Z_chi,max)^4
=(kappa_8V_Gamma,Q/(2Z_chi,max))^4.
```

Equivalently,

```tex
0<V_Gamma,Q<=2Z_chi,max/kappa_8,
\qquad
z_chi=F^{-1}[(kappa_8V_Gamma,Q/(2Z_chi,max))^4].
```

Normalized endpoint coordinate:

```tex
x_Gamma,Q=Z_Gamma,0/Z_chi,max
=kappa_8V_Gamma,Q/(2Z_chi,max)
=kappa_8L_QT_Gamma/(2Z_chi,max),
\qquad
Xi_Gamma^cp=x_Gamma,Q^4,
\qquad
z_chi=F^{-1}(x_Gamma,Q^4).
```

Compactification pass:

```tex
L_Q/L_Q,max(varrho_Gamma)<=x_Gamma,Q<=1.
```

Compactification interval test:

```tex
I_{r^2}(varrho_Gamma,L_Q)
=[r_min^2(varrho_Gamma),r_max^2(L_Q)].
```

```tex
r_min^2=441u_Gamma^sh(varrho_Gamma)/
(8pi^2 kappa_8 e^-phi_0 Omega_Gamma),
\qquad
r_max^2=2Z_chi,max/(kappa_8 e^-phi_0 Omega_Gamma L_Q).
```

It is populated exactly when

```tex
0<L_Q<=L_Q,max(varrho_Gamma),
\qquad
L_Q,max=16pi^2Z_chi,max/(441u_Gamma^sh(varrho_Gamma)).
```

The same local pass has to return

```tex
R_Xi,sigma=0,
\qquad
Z_Gamma,H={Q\over4}Z_Gamma,0,
\qquad
N_Gamma^chi=2 sigma_chi d_chi F(z).
```

Report 18 adds the quadratic master form:

```tex
S_Gamma^(2)
=int_M4[
-1/4 K_AB^Gamma F_A F_B
+1/2(f_H^2)_ab partial theta_H^a partial theta_H^b
+1/2<r,M_img r>_Gamma
+L_2 j_A<r,J_A>_Gamma
+1/2 Str_chi log B_Gamma^chi(theta_H)].
```

It reduces the local extraction to

```tex
(D_AB,Z_Gamma,H/Z_Gamma,0,N_Gamma^chi)
=
(D_sigma,Q/4,2 sigma_chi d_chi F(z)).
```

The image sector now has a finite-matrix extraction:

```tex
D_AB=L_2^-2 C_Ai(M^-1)^ij C_Bj,
\qquad
w_Y=rho_sigma w_3,
\qquad
||w_3||^2=delta_sigma.
```

The determinant sector has the matching finite-spectrum row:

```tex
N_Gamma^chi
=2 sum_alpha sigma_alpha d_alpha F(M_alpha L_H).
```

Current minimal spectrum package:

```tex
H_img,sigma^src=span{e_sigma},
\qquad
C_3sigma=L_2 sqrt(m_sigma delta_sigma),
\qquad
C_Ysigma=rho_sigma C_3sigma.
```

The endpoint side is

```tex
E_1^chi=span{u,v} tensor E_chi,
\qquad
E_2^chi=span{u^2,v^2} tensor E_chi,
\qquad
N_Gamma^chi=2d_chi F(M_chi L_H).
```

Current boundary-complex ansatz:

```tex
H_Gamma^loc
=span{e_sigma} op (P_1^chi op P_2^chi) tensor E_chi op H_perp,
```

with

```tex
Q_Gamma,sigma
=sqrt(m_sigma)Pi_e_sigma
op (1_P1^chi op 1_P2^chi) tensor B_chi
op Q_perp.
```

It reduces the charged threshold to

```tex
F(M_chi L_H)
=21375.716460702053... lambda_F
(Z_Gamma,0/v_EW)^4/(2d_chi w_H^8).
```

Current image-line closure:

```tex
e_sigma=psi_sigma,
\qquad
Xi_sigma,min=L_2 psi_sigma c_sigma^B theta_Gamma,B,
\qquad
c_sigma=G^(psi)^-1g_sigma.
```

Then

```tex
C_Asigma=L_2 sqrt(m_sigma)(g_sigma)_A,
\qquad
D_AB=(g_sigma)_A(g_sigma)_B.
```

## Completion Condition

The `Gamma_EW` job is complete when a single localized D8/O8 computation
returns:

```text
dnu_Gamma, theta_Gamma^a, theta_Gamma^Y,
L_2,Gamma, L_Q, M_img, psi_sigma, m_sigma, Xi_sigma,
Z_Gamma,0, Z_Gamma,H, N_Gamma^chi, z, sigma_chi d_chi
```

and verifies:

```text
unit current metric,
one Schur branch D_sigma,
R_Xi,sigma=0 or a sourced residual explanation,
Z_Gamma,H=(Q/4)Z_Gamma,0,
endpoint determinant density,
neutral mass ratio,
electromagnetic length,
D8/O8 charge consistency.
R_Gamma(A_Gamma;D_Gamma)=0.
```

Until that calculation exists, the objective remains active.
