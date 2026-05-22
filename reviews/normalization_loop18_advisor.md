# Loop 18 Advisor

Role: advisor proposing a high-risk/high-value improvement after the two O10
referee passes.

## Conceptual Route

Make O10 a factorized active-channel interpolation:
\[
D=4+n_c+n_{\rm ew},\qquad n_c=4,\qquad n_{\rm ew}:3\to2\to1.
\]
The full \(D=11\to10\to9\) chain is then the colour-restored version of the
same active electroweak interpolation.  The speculative middle line becomes a
concrete demand: identify the \(n_{\rm ew}=2\) source object whose light sector
gives the DeVries kernel.

## Mechanism To Test

Use an interval electroweak boundary problem with boundary scalar data.  A
two-channel interval reduction could have \(h_J\) as a boundary order-parameter
amplitude and \(a_J\) as a current or gauge amplitude.  The target Schur
complement is
\[
K^{\rm eff}_J(\lambda)
=
K^{\rm bdry}_J(\lambda)
-V_J^\dagger(\lambda-L_J)^{-1}V_J
\to
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix}.
\]

## Source To Read

`context/source_fragments/09_csaki_hubisz_meade_ewsb_from_extra_dimensions_hep_ph_0510275/pages_011-020.md`
is the key local fragment.  It records boundary scalar vevs modifying gauge
boundary conditions, vector masses controlled by interval data, and possible
\(A_5/\pi_i\) scalar remnants.

## Equation Or Diagram Needed

Appendix E should include the factorized active-channel diagram:
\[
\begin{array}{ccccc}
\mathcal C_4\times \mathcal E_3
&\xrightarrow{u}&
\mathcal C_4\times \mathcal E_2(u_\star)
&\xrightarrow{u}&
\mathcal C_4\times \mathcal E_1
\\
D=11 && D=10 && D=9
\\[3pt]
\mathcal E_3
&\xrightarrow{u}&
\mathcal E_2(u_\star)
&\xrightarrow{u}&
\mathcal E_1
\\
D=7 && D=6 && D=5 .
\end{array}
\]
Attach \(\mathcal E_2(u_\star)\to\mathcal H_J\to K_J
\to(J_H,J_{\rm adj})\to\Delta^{-1}_{T,V}\).

## Top-Sector Advice

Treat the top as a diagnostic of the order-parameter channel.  A source theory
must define a fermion overlap or boundary datum
\[
\mathcal Y_f(u_\star):\psi_f,\mathcal H_J\longmapsto y_f
\]
and then test whether \(\mathcal Y_t\) is selected or extremal at the middle
point.  Until that map is derived, Appendix E should record the Standard Model
top-Higgs source fact and an open top-sector target.
