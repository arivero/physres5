# Normalization loop 12 - Advisor

## Recommendation

Add a lead target in Appendix D: unified source-to-pole matching.  It should
combine O1, O4, and O8 into one theorem target:
\[
\mathcal S_r
\to \mathcal H_J
\to K^{\rm eff}_{J,r}(\lambda)
\to \Pi^{(4)}_{T,V}(s;J,r)
\to s_{W,Z}.
\]

The theorem should specify
\[
\mathcal H_J=\operatorname{span}\{h_J,a_J\},\qquad
\langle\cdot,\cdot\rangle_r,\qquad P_J,
\]
plus a route-specific Schur complement
\[
K^{\rm eff}_{J,r}(\lambda)
=
K^{\rm bdry}_{J,r}(\lambda)
-V_{J,r}^{\dagger}(\lambda-L_{J,r})^{-1}V_{J,r}.
\]

Its DeVries acceptance condition is
\[
K^{\rm eff}_{J,r}(\lambda)
=
\begin{pmatrix}
\lambda&-\sqrt J\\
-\sqrt J&\lambda+J
\end{pmatrix}
\]
in the same field basis used for pole matching.  The electroweak sampling maps
are
\[
P_W:\ h_J\mapsto C_2(\mathbf 2)=3/4,\qquad
P_Z:\ a_J\mapsto C_2(\mathrm{adj})=2.
\]

This gives endpoint, interval, and \(G_2\) routes a shared reduced test while
allowing them to differ in \((K^{\rm bdry},L,V)\).

## Lean update

Add `UnifiedSourceToPoleMatching` after `PoleSelfEnergyMatching` in
`notes/lean/DeVriesProgram.lean`, with fields for light subspace, inner
product, Schur complement, DeVries kernel, charged doublet projector, neutral
adjoint projector, transverse self-energy map, and common pole scheme.
