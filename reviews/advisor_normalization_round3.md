# Advisor normalization round 3

## One new conceptual route

Treat the DeVries kernel as a finite-rank contribution to the dressed
transverse inverse propagator.  The route target is
\[
K_{J,r}^{\rm bare}(\lambda)
\mapsto
\Pi^{(4)}_{T,V}(s)
\mapsto
\Delta^{-1}_{T,V}(s_V)=0,
\]
so O8 becomes a pole self-energy matching theorem.

## One string/Kaluza--Klein mechanism to test

Interval KK boundary self-energy: a brane-localized order-parameter channel
\(h_J\) couples to a bulk adjoint gauge profile \(a_J\), and integrating out
the KK tower gives the Schur-complement kernel with target entries
\[
\Sigma_{hh}=0,\qquad
\Sigma_{aa}=J,\qquad
\Sigma_{ha}\Sigma_{ah}=J.
\]

## One source to read

Martin--Robertson, pages 11--20 in the local fragment set.  Use it to pin down
how their code distinguishes pole masses, variable-width Breit--Wigner masses,
and matching-scale dependence for W/Z.

## One equation or diagram the manuscript needs

A convention-and-placement diagram:
\[
(M_{V,\rm BW},\Gamma_{V,\rm BW})
\stackrel{\rm common\ variable\ width\ convention}{\longrightarrow}
(M_{V,\rm pole},\Gamma_{V,\rm pole})
\longrightarrow
s_V=M_{V,\rm pole}^2-iM_{V,\rm pole}\Gamma_{V,\rm pole}
\longrightarrow
\sPole .
\]
This should sit beside
\[
\mathcal S_r\to K^{\rm bare}_{J,r}\to \Gamma_{\rm eff}^{(4)}[H,W,B]\to
\Delta^{-1}_{T,V}(s_V)=0.
\]

## Implementation priorities

First, state the exact pole parameterization and width convention for the
Breit--Wigner translation.  Second, mark Eq. `eq:route-pole-ratio-target` as
conditional on the O8 matching theorem.  Third, add the failure mode: if the
clean quotient is derived at compactification or unification scale, the
physical claim relocates to that scale and the pole comparison becomes
descriptive.  Fourth, keep all W/Z numerical input work deferred to the
approved calculation phase.
