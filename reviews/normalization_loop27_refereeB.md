# Normalization Loop 27 Referee B

## Scope

Read-only referee pass on the CHM interval source fragments, the
Dirichlet-to-Neumann/current-entry target, label discipline, and pole matching.

## Findings

The CHM route is viable as a theorem target.  CHM supplies variational boundary
conditions, modified products, gauge fixing, vector Robin data, scalar
\(A_5/\pi_i\) equations, photon/custodial accounting, and source templates for
self-energy matching.  The equality \(\Sigma_{aa,J}=J\) remains a DeVries
entry theorem.

The current amplitude needs a definition.  It should be a normalized transverse
boundary gauge trace/current amplitude with a stated inner product and matching
convention.  The Dirichlet-to-Neumann kernel also needs sign, endpoint-normal,
and subtraction conventions.

## Requested Definition

Use
\[
K^{\rm cur}_{J}(\lambda)
=
P_{a,J}^{\dagger}
\left[
K^{\rm DtN}_{T,J}(\lambda)
+K^{\rm brane}_{T,J}(\lambda)
-K^{\rm ref}_{T,J}(\lambda)
\right]
P_{a,J},
\qquad
\langle a_J,a_J\rangle_{\rm CHM}=1 .
\]
Then state
\[
K^{\rm cur}_{J}(\lambda)
=\lambda+J+O(\lambda^2/\Lambda_{\rm KK}^2)
\]
or \(\Sigma_{aa,J}\equiv K^{\rm cur}_{J}(0)=J\), with the convention declared.

## Source-Control Caveat

The source-controlled statement is the existence of a transverse boundary
kernel from the CHM boundary action and natural boundary conditions.  The
\(J\)-normalization, projection, photon zero mode, ordered W/Z map, and pole
matching are theorem data.

## Score

Source-controlled theorem-target readiness: 7/10.
