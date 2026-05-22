# Normalization Loop 47 Advisor

Role: advisor integrating the two referee reports.

## Recommended Conceptual Route

Add Target IIIg as a local \(G_2\) ADE-pairing theorem target.  The target should
first test the current entry
\[
\widehat\Sigma_{aa,2}^{G_2,{\rm can}}=2,
\]
then record the flow-overlap product, electroweak projectors, compact charge
lattice, anomaly/global-form checks, and pole map as completion data.

## Mechanism To Test

Use the local Higgs-bundle equations
\[
\Phi=\sum_i t_i df_i,\qquad \rho=\sum_i t_i\rho_i,\qquad
\Delta f_i=\rho_i,
\]
with the charge functions
\[
f_Q=\sum_iq_if_i,\qquad \rho_Q=\sum_iq_i\rho_i,\qquad df_Q(p)=0.
\]
Pair the current-support term on \(M_3\) with a point-support metric at
localized matter points.  The point term supports the later flow-overlap
target.

## Source To Read

Read Braun et al. pages 1--20 and 61--70 for the ALE fibration, ADE
singularity, Higgs-bundle equations, \(f_Q\), matter localization, and flow
data.  Use Acharya--Witten pages 1--10 and 21--27 plus Witten anomaly pages
1--10 for singular support and compact-completion constraints.

## Needed Equations

Local source datum:
\[
u_{G_2}^{\rm loc}
=
(M_3,\Gamma_{\rm ADE},W,\Phi,\rho_i,f_i,Q,p,\gamma,
A_1\subset A_2,\Lambda_{G_2}).
\]

Singular-support pairing:
\[
\langle \eta,\zeta\rangle_{G_2,u}
=
\int_{M_3}{\rm Tr}_{\rm ADE}(\eta\wedge *_{M_3}\zeta)
+
\sum_{p\in Z(df_Q)}
\eta(p)^\dagger\mathsf G_Q(p)\zeta(p).
\]

Canonical current target:
\[
\widehat K_J^{G_2,{\rm cur,can}}(\widehat\lambda)
=
\widehat\lambda+\widehat\Sigma_{aa,J}^{G_2,{\rm can}}
+O(\widehat\lambda^2),
\qquad
\widehat\Sigma_{aa,2}^{G_2,{\rm can}}=2.
\]

Completion data:
\[
\Sigma_{ha,J}^{G_2}\Sigma_{ah,J}^{G_2}=J,\qquad
P_W(h_J)=3/4+\Delta_W^{G_2},\qquad
P_Z(a_J^{\gamma^\perp})=2+\Delta_Y^{G_2}.
\]

Pole map:
\[
\frac{M_{W,\rm pole}^2}{M_{Z,\rm pole}^2}
=
\frac{x_+(3/4)}{x_+(2)}+\Delta_{\rm match}^{G_2}.
\]

## Projected Scores After Implementation

Conceptual clarity: 4.5.  
Source control: 4.75.  
String/KK/\(G_2\) depth: 4.5.  
Electroweak correctness: 4.5.  
Open-gap honesty: 5.
