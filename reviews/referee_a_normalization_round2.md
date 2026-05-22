# Referee A normalization round 2

## Central claim

O10 proposes a dimensional endpoint dictionary: full-gauge
\(D=11\to10\to9\) with \(n_{\rm KK}=7,6,5\), and colourless
electroweak \(D=7\to6\to5\) with \(n_{\rm KK}^{\rm ew}=3,2,1\).
Its intended role is to make the DeVries sector the interior interpolation
point and connect that point to O1's ordered
\((J_H,J_{\rm adj})=(3/4,2)\) assignment and O4's two-channel kernel
target.

## Strongest source-supported result

`manuscript/sections/E_dimensional_interpolation.tex` gives a clean
source-backed endpoint for \(D=11\): Witten's seven-extra-dimensional
\(SU(3)\times SU(2)\times U(1)\) KK setting and its fermion obstruction.
`manuscript/sections/04_electroweak_embedding.tex` states the electroweak
ray, the Higgs doublet invariant \(J_H=3/4\), and the adjoint invariant
\(J_{\rm adj}=2\). `manuscript/sections/06g_route_comparison.tex` gives
the strongest formal bridge to O4 through the shared kernel conditions
\(\Sigma_{hh}=0\), \(\Sigma_{aa}=J\), and
\(\Sigma_{ha}\Sigma_{ah}=J\).

## Weakest inference

The middle \(D=10\) or colourless \(D=6\) line is presently a placement
ansatz. The manuscript has source support for endpoint symmetries and for
the existence of six-dimensional string settings. The DeVries determinant
still needs an operator, compact space, boundary condition, or light
subspace at the interior dimensional step. O10 currently organizes O1 and
O4; it has not derived them.

## Hidden assumptions

The count assumes each gauge-symmetry endpoint maps monotonically to a
minimal KK dimension and that electroweak breaking can be modeled as motion
along that dimensional chain. It assumes the Witten seven-dimensional
obstruction applies to the endpoint while the six-dimensional interior can
evade it. It assumes colour may be treated as a spectator in the \(3/2/1\)
count while preserving the electroweak assignment problem. It also assumes
the interpolation parameter \(t\) can be identified with the Higgs radial
direction, boundary data, or compactification deformation while preserving
the allowed broken-to-unbroken electroweak ray.

## Exact revisions needed

Add an O10 theorem target to `manuscript/sections/D_theorem_targets.tex`
with hypotheses, conclusion, current evidence, and failure mode. In
`manuscript/sections/E_dimensional_interpolation.tex`, define the required
data for the middle line: compact/internal object, gauge group, light
subspace \(\mathcal H_J=\mathrm{span}\{h_J,a_J\}\), interpolation
parameter \(t\), and kernel \(K_J(t,\lambda)\). Add an explicit
compatibility paragraph tying O10 to O1 and O4: the middle model must
produce \((J_W,J_Z)=(J_H,J_{\rm adj})\) and the same kernel target used in
Sec. VI.G. Label the \(D=10\) and colourless \(D=6\) claims as
reconstruction targets until one kernel entry or ordered assignment is
derived.
