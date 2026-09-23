# Lagrangian-attempt report for the Casimir-locked seed

Status: first-pass derivation attempt. Five candidate Lagrangians evaluated; one
synthesis proposed. **Honest headline: no mechanism cleanly derives all three
features. The off-diagonal $\sqrt{C_2(R)}$ scaling is the structural gap and
remains a postulate.** Below: target, per-mechanism verdict, synthesis, and
literature comparison.

---

## 1. The target and the three features

We seek a Lagrangian density $\mathcal{L}$ whose mass-squared matrix in a
two-field basis $(s, \phi_R)$ is

$$
M_R^2 \;=\; m_0^2 \begin{pmatrix} 0 & \sqrt{C_2(R)} \\ \sqrt{C_2(R)} & -C_2(R) \end{pmatrix},
\qquad C_2(R) \text{ the quadratic Casimir of } \mathrm{SU}(2)_W \text{ in rep } R,
$$

with the SAME seed scale $m_0\simeq 106.57$ GeV across the two representations
$R\in\{\text{doublet},\text{triplet}\}$, $C_2(2)=3/4$, $C_2(3)=2$.

Three features must be produced:

| Feature | Entry        | Required mechanism                                  |
|---------|--------------|-----------------------------------------------------|
| (i)     | $M^2_{ss}=0$ | Discrete symmetry (e.g. $\mathbb{Z}_2$: $s\to -s$)  |
| (ii)    | $M^2_{\phi\phi}=-C_2(R)\,m_0^2$ | $\mathrm{SU}(2)$-invariant bilinear $\Phi^\dagger T^aT^a\Phi$ with negative sign |
| (iii)   | $M^2_{s\phi}=\sqrt{C_2(R)}\,m_0^2$ | **Single** generator factor — a single $T^a$ pulled by an adjoint spurion/VEV/derivative |

The crux is feature (iii). Standard $\mathrm{SU}(2)$-invariant bilinears in
$\Phi_R$ produce $C_2(R) = \mathrm{Tr}_R(T^aT^a)$ — an even power of $T^a$.
A genuine $\sqrt{C_2(R)}$ requires either an adjoint spurion to break the
group invariance, a non-renormalizable square-root operator, or a
representation-dependent fine-tune in dimensionless couplings. None of these
arises from group theory alone.

For each candidate below, the mass matrix is computed from the quadratic
action around the vacuum $(\langle s\rangle, \langle \Phi_R\rangle)$ specified
by the mechanism. The verdict for each entry uses:

- **MATCHES**: produces the target entry with the right $C_2$ scaling and no R-dependent coupling.
- **PARTIAL**: produces correct sign and order but with wrong scaling, requires R-dependent rescaling, or requires averaging not physically realized by the Lagrangian.
- **FAILS**: produces no contribution to that entry.

---

## 2. Mechanisms

### L1 — Adjoint-spurion mixing

**Lagrangian.** Real singlet $S$, complex $\Phi_R$ in rep $R$, real adjoint
$\Sigma^a$ with VEV $\langle\Sigma^a\rangle=v_\Sigma\xi^a$, $\xi^a\xi^a=1$.
Impose $\mathbb{Z}_2:\,S\to -S$ to forbid $S^2$.

$$
\mathcal{L}_{L1} = |\partial S|^2/2 + |D\Phi_R|^2
\;-\;\lambda_\phi\,m_0^2\,\Phi_R^\dagger T^aT^a\Phi_R
\;+\;\kappa\, S\,\Sigma^a\,\Phi_R^\dagger T^a\Phi_R
\;+\;\text{h.c.}\,.
$$

**Mass matrix around $(\langle S\rangle=0,\langle\Phi_R\rangle=0)$.** The
$\kappa$ term is **cubic** in dynamical fields; at $\Phi_R=0$ it contributes
zero bilinear mixing. Thus

$$
M^2_{L1} \;=\; \begin{pmatrix} 0 & 0 \\ 0 & -\lambda_\phi C_2(R)\, m_0^2\end{pmatrix}
\quad\Rightarrow\quad
\text{(i) MATCHES},\;(ii)\text{ MATCHES with }\lambda_\phi=1,\;(iii)\text{ FAILS}.
$$

If instead $\Phi_R$ acquires a VEV $\Phi_R = v_R w$ (with $w^\dagger w=1$),
the trilinear $\kappa S\Sigma^a\Phi^\dagger T^a\Phi$ expands to a bilinear
in $(S,\delta\Phi)$. Summing over all $\delta\Phi$-components:

$$
\sum_i |M^2_{S,\delta\Phi^i}|^2 \;=\; (\kappa v_\Sigma v_R)^2\,\xi^a\xi^b\, w^\dagger T^aT^b w
\;\le\; (\kappa v_\Sigma v_R)^2\, j(R)^2,
$$

with $j(R)=(\dim R-1)/2$ the highest weight (verified symbolically: for the
doublet with $w=(1,0)$, $w^\dagger(\xi.T)^2 w = 1/4 = j^2$; for the triplet
highest-weight $w_t=(1,i,0)/\sqrt 2$, $w_t^\dagger(\xi.T)^2 w_t \in [1/2,1]$
depending on $\xi$). Since $j(R) < \sqrt{C_2(R)} = \sqrt{j(j+1)}$ strictly
(equality only in the trivial $j=0$ rep), this mechanism systematically
UNDERSHOOTS $\sqrt{C_2}$ by a factor $\sqrt{j/(j+1)}$:

$$
\frac{j}{\sqrt{C_2}} \;=\; \sqrt{\frac{j}{j+1}} \;=\;
\begin{cases} 1/\sqrt 3 \approx 0.577 & (\text{doublet}) \\ 1/\sqrt 2 \approx 0.707 & (\text{triplet})\end{cases}
$$

The deficit factor is **representation-dependent**, so a single
$R$-independent $\kappa v_\Sigma$ cannot reproduce $\sqrt{C_2(R)}$ across both
reps.

**Verdict L1: PARTIAL.** (i) and (ii) match cleanly; (iii) at best gives
$j(R)$, not $\sqrt{C_2(R)}$. A representation-by-representation rescaling
of $\kappa$ would recover the target but would violate the single-seed
postulate of the model.

### L2 — Hosotani / Wilson-line in 5D

**Lagrangian.** 5D $\mathrm{SU}(2)$ gauge theory on $S^1/\mathbb{Z}_2$; bulk
scalar $\Phi_R$ in rep $R$; Hosotani Wilson-line phase $\alpha$ in the
adjoint via $\langle A_5^a\rangle = (\alpha/gR_5)\xi^a$.

**KK mass spectrum.** For a state of $(\xi.T)$-eigenvalue $m$ in $R$:

$$
M^2_{n,m} \;=\; \bigl(n + \alpha m\bigr)^2 / R_5^2.
$$

Doublet ($m=\pm 1/2$): $M^2_{0,\pm 1/2}=(\alpha/2)^2/R_5^2$ (twofold).
Triplet ($m=-1,0,+1$): $M^2_{0,0}=0$ (the gauge-Higgs zero mode),
$M^2_{0,\pm 1}=\alpha^2/R_5^2$.

All eigenvalues are **non-negative** (no tachyon without boundary
symmetry breaking) and scale as $(weight)^2$, not $C_2(R)$.

**Verdict L2: FAILS.** No natural $\{0,\sqrt{C_2},-C_2\}$ structure;
KK masses scale as weight$^2$ (=$m^2$) not $C_2(R)=j(j+1)$, and there
is no off-diagonal mixing without ad-hoc boundary terms. The mechanism
that famously produces a Casimir-shaped Coleman–Weinberg potential in
Hosotani GHU (e.g. $V \sim \mathrm{Tr}[\cos(\alpha \,T_R)]$ summed over
KK modes — see Hosotani 1983, Antoniadis-Benakli-Quiros 2001) gives
$\Phi$-self-couplings, not the 2×2 mass matrix shape we need.

### L3 — Singlet + rep-$R$ via covariant derivative with adjoint spurion

**Lagrangian.** Real singlet $S$, complex $\Phi_R$, external (frozen)
adjoint spurion $n^a$ with $|n|=1$, $\mathbb{Z}_2:\, S\to -S$:

$$
\mathcal{L}_{L3} = |\partial S|^2/2 + |D\Phi_R|^2 - m_0^2 C_2(R)|\Phi_R|^2
\;+\;\lambda\, S\,(\Phi_R^\dagger T^a\Phi_R)\, n^a \;+\;\text{h.c.}\,.
$$

**Mass matrix.** Same problem as L1: the $\lambda$ term is cubic in
fields. At $\Phi_R=0$, no bilinear $s\phi$ mixing is generated. If
$\Phi_R$ gets a VEV $v_R w$,

$$
|M^2_{s\phi}|_{\mathrm{eff}}^2 \;=\; 4\lambda^2 v_R^2\, w^\dagger(n.T)^2 w
\;\le\; 4\lambda^2 v_R^2\, j(R)^2,
$$

bounded by $j(R)$ as in L1. For $|M^2_{s\phi}|=m_0^2\sqrt{C_2(R)}$ we
would need $\lambda v_R = (m_0/2)\sqrt{C_2(R)}/j(R)$ — explicitly
$R$-dependent (ratio $\sqrt{C_2(2)}/j(2)=\sqrt 3$ vs $\sqrt{C_2(3)}/j(3)=\sqrt 2$).

**Verdict L3: PARTIAL.** (i) holds by $\mathbb{Z}_2$, (ii) holds by
postulate, (iii) requires an R-dependent rescaling of $\lambda v_R$ —
incompatible with the single-seed structure.

### L4 — Coleman–Weinberg from a heavy fermion in rep $R$ (Haba-like)

**Lagrangian.** Real singlet $S$ (classically scale-invariant, no
$S^2$ term), complex $\Phi_R$ in rep $R$, heavy Dirac fermion $\psi_R$
in rep $R'$, portal couplings:

$$
\mathcal{L}_{L4} = |\partial S|^2/2 + |D\Phi_R|^2 - M_\psi\bar\psi\psi
+ y_S\, S\,\bar\psi\psi + y_\phi\,\Phi_R^\dagger \bar\psi_L\psi_R + \mathrm{h.c.}
+ \lambda_p|S|^2|\Phi_R|^2.
$$

**One-loop CW effective potential.** The dominant gauge-loop
contribution to $V_{\rm eff}(\Phi_R)$ at $S=0$ has the form
$V_{\rm eff} \supset \tfrac{3}{64\pi^2}\,g^4\,(C_2(R))^2|\Phi_R|^4
\log|\Phi_R|^2/\mu^2$. Its mass-like contribution to $M^2_{\phi\phi}$
from a hard cutoff $\Lambda$:

$$
\delta M^2_{\phi\phi} \;\sim\; \frac{3g^2}{16\pi^2}\,C_2(R)\,\Lambda^2,
$$

which gives the **correct $C_2(R)$ scaling for entry (ii)** with the
right sign IF the gauge contribution is negative (e.g. via fermion-loop
dominance: a heavy Dirac fermion in rep $R$ generates
$\delta M^2_{\phi\phi}\sim -y_\phi^2 N_R \Lambda^2/16\pi^2$, where
$N_R = \dim R\,C_2(R)/\dim_{\mathrm{adj}}$ contains the Dynkin index
$T(R)\propto \dim R\cdot C_2(R)$).

**Off-diagonal $M^2_{s\phi}$.** Loop diagrams mixing $S$ and $\Phi_R$
require closure over both legs. With portal $\lambda_p|S|^2|\Phi_R|^2$
plus Yukawas $y_S, y_\phi$, the one-loop mixing diagram has structure
$\Sigma_{S\phi}(p^2) \sim y_S y_\phi M_\psi^2/(16\pi^2) \cdot
\mathrm{Tr}[T_R^aT_R^a]/\dim R = y_Sy_\phi M_\psi^2 C_2(R)/(16\pi^2)$ —
scaling as $C_2(R)$, **not** $\sqrt{C_2(R)}$.

Pulling a single $T^a$ requires an external adjoint spurion (returning
to L1), so the radiative mechanism cannot by itself produce
$\sqrt{C_2}$ from group-trace alone.

**Verdict L4: PARTIAL.** This is the closest mechanistic precursor to
the M4 top-loop $\Delta$ mechanism cited as Haba et al.\ (arXiv
1508.06828) in §5.3 of PAPER.md. Verified by direct text inspection
that the Haba mass matrix is

$$
M^2_{\rm Haba} = \begin{pmatrix} \lambda_{H_1\Phi} v_\Phi^2 & \lambda_{\rm mix}v_\Phi^2 \\
\lambda_{\rm mix}v_\Phi^2 & \lambda_{H_2\Phi}v_\Phi^2\end{pmatrix},
$$

(Haba eq.\ (4)) with **independent dimensionless couplings** $\lambda_{H_1\Phi}$,
$\lambda_{H_2\Phi}$, $\lambda_{\rm mix}$ — there is **no Casimir locking**.
Our (i), (ii), (iii) are 3 constraints on these 3 couplings, but no
group-theory identity forces those values.

(ii) MATCHES with sign provided by fermion loop. (iii) FAILS without an
external adjoint structure. (i) requires scale invariance OR $\mathbb{Z}_2$.

### L5 — Direct postulate: Casimir-coupled scalar potential with weight-aligned VEV

**Lagrangian.** Real singlet $S$ ($\mathbb{Z}_2$-protected), complex
$\Phi_R$ with VEV along a maximal weight: $\langle\Phi_R\rangle = v_R w_R$.
Fixed adjoint spurion $\xi^a$, $|\xi|=1$:

$$
\mathcal{L}_{L5} \supset -m_0^2\,\Phi_R^\dagger T^aT^a\Phi_R
+\;2m_0^2\,\frac{S}{v_R}\,\xi^a\,(\Phi_R^\dagger T^a\Phi_R).
$$

**Mass matrix around the VEV.** $(2,2)$ entry: $-m_0^2 C_2(R)$ ✓.
$(1,1)$ entry: $0$ ✓ (no $S^2$ term).
$(1,2)$ entry: from the trilinear after $\Phi_R = v_R w_R + \delta\phi$:

$$
M^2_{s,\delta\phi} \;=\; 2m_0^2\,\xi^a\,(w_R^\dagger T^a)_i.
$$

Effective off-diagonal squared (summed over $\delta\phi$ components):

$$
|M^2_{s\phi}|^2 \;=\; 4m_0^4\,\xi^a\xi^b\,(w_R^\dagger T^aT^bw_R)
\;\le\; 4m_0^4\,j(R)^2,
$$

bounded by $j(R)^2$ — **the same constraint as in L1.**

Explicit values from sympy:

- Doublet, $w=(1,0)^T$, any unit $\xi$: $\sum_a(w^\dagger T^aw)^2 = 1/4 = (1/2)^2$.
- Triplet, $w_t=(1,i,0)/\sqrt 2$, $\xi=(0,0,1)$: $\sum_a |w_t^\dagger T^aw_t|^2 = 1$.
- Triplet, $w_t=(1,i,0)/\sqrt 2$, $\xi=(1,0,0)$: $\sum_a |w_t^\dagger T^aw_t|^2 = 1/2$.

Saturation by single-state contraction is $j(R)^2$, never $C_2(R)=j(j+1)$.
The mismatch ratio $j/\sqrt{C_2}=\sqrt{j/(j+1)}\in\{1/\sqrt 3,1/\sqrt 2\}$
varies between reps, so no single rescaling works.

**Verdict L5: PARTIAL.** Same algebraic obstruction as L1 — adjoint
spurion contracted with $\Phi^\dagger T^a\Phi$ saturates at $j$, not at
$\sqrt{C_2}$. To get exact $\sqrt{C_2}$ one would need the
**non-renormalizable square-root operator**
$\mathcal{O}_{\sqrt{C}} = S\,\sqrt{\Phi^\dagger T^aT^a\Phi}$, whose
expectation gives $\sqrt{C_2}\,v_R\,S$ but is not analytic in
$\Phi_R$ and so not a legitimate Lagrangian term.

---

## 3. Synthesis: closest candidate, residual gap, and the required postulate

**Closest candidate: L4 (radiative) for (ii) + L1 or L5 (adjoint
spurion + $\mathbb{Z}_2$) for (i), plus a postulated trilinear for
(iii).**

The combined Lagrangian that delivers the most structure with the
fewest postulates:

$$
\boxed{\;\mathcal{L}_{\rm best} \;=\; \tfrac{1}{2}|\partial S|^2 + |D\Phi_R|^2
\;-\;m_0^2\,\Phi_R^\dagger T^aT^a\Phi_R
\;+\;\eta\,m_0^2\,S\,\sqrt{\Phi_R^\dagger T^aT^a\Phi_R}\,/\,v_R\;}
$$

with $\mathbb{Z}_2$: $S\to -S$ (forbids $S^2$) and a Casimir-aligned
VEV $\langle\Phi_R\rangle = v_R w_R$ around which the square root
linearizes:

- Around $\Phi_R = v_R w_R$: $\sqrt{\Phi^\dagger T^aT^a\Phi}/v_R
  \to \sqrt{C_2(R)} + $ (linear fluctuation).
- Mass-mixing $M^2_{s\phi} = \eta m_0^2 \sqrt{C_2(R)}$.
- For $\eta=1$, this **reproduces feature (iii) exactly**.

**Residual gap.** The square-root operator is **not analytic in
$\Phi_R$**. It is a meaningful EFT operator only in the broken phase
where $|\Phi_R|>0$ is well-defined; it cannot be a Wilson coefficient
in a renormalizable UV Lagrangian. The Casimir-locked seed therefore
**does not lift to a renormalizable Lagrangian without imposing
$\sqrt{C_2(R)}$ as an R-dependent coupling by hand.**

**Is there a symmetry that fixes the ratio $|M^2_{s\phi}|^2 /
|M^2_{\phi\phi}| = m_0^2$ (i.e., $C_2/C_2=1$, the "balanced seesaw"
point)?** Yes, but only at the level of the matrix structure, not of
the underlying Lagrangian. Define the rescaled fields
$\tilde s = s$, $\tilde\phi = \phi/\sqrt{C_2(R)}$. In this basis the
matrix becomes $m_0^2[[0,C_2],[C_2,-C_2^2]]$, manifestly proportional to
$C_2$. So a $\mathbb{Z}_2$ symmetry $\tilde s \leftrightarrow \tilde\phi$
(up to sign and the factor $-C_2$ on the diagonal) would force the
balance. But this $\mathbb{Z}_2$ acts on the $C_2$-rescaled basis,
which is itself R-dependent — so it is a **derived symmetry of the
matrix**, not a fundamental symmetry of the Lagrangian.

**No fundamental symmetry of $(s,\Phi_R)$ in canonical kinetic basis
that produces the Casimir-locked balance has been identified.** The
balance remains a postulate.

---

## 4. Comparison with the bosonic-seesaw literature

The PAPER.md bibliography cites four bosonic-seesaw precursors:

| Ref | Mass matrix structure | Casimir locked? |
|-----|----------------------|------------------|
| Calmet–Oliver (hep-ph/0606209) | $[[m_a^2, m_c^2],[m_c^2, m_b^2]]$, all free, $m_a,m_b$ real, $m_c^2$ possibly complex | No — three free parameters |
| Kim (hep-ph/0501059) | 2x2 with seed from SUSY mediation | No — SUSY-mediation parameters |
| Chivukula–Dobrescu–Georgi–Hill (hep-ph/9809470) | Top-quark seesaw: $[[0,M],[M,-m]]$ on fermion side | Structurally analogous (the $(0,\sqrt{},-C)$ shape) **but fermion-side**; no $C_2$ scaling |
| Haba–Ishida–Okada–Yamaguchi (1508.06828) | $[[\lambda_{H_1\Phi}v_\Phi^2,\lambda_{\rm mix}v_\Phi^2],[\lambda_{\rm mix}v_\Phi^2, \lambda_{H_2\Phi}v_\Phi^2]]$ via CW dynamics | No — three independent $\lambda$ couplings; CW produces signs but not $C_2$ scaling |

**Direct text-inspection findings:**

- Haba (eq. 4 and 8–9 of arXiv 1508.06828): The bosonic seesaw is
  realized via *quartic-coupling hierarchy* $\lambda_{H_1\Phi}\ll
  \lambda_{\rm mix}\ll \lambda_{H_2\Phi}$, not by group-theory
  invariants. Closest mechanistic precedent for the radiative
  generation of a negative bare-Higgs mass-squared (=M4 of §4.3 of
  PAPER.md) but **does not derive the $\sqrt{C_2}$ shape**.
- Calmet–Oliver (eq. 3–4 of hep-ph/0606209): Two-Higgs-doublet mass
  matrix $-(h_a^\dagger,h_b^\dagger)\binom{m_a^2\;\,m_c^2}{m_c^2\;m_b^2}\binom{h_a}{h_b}$
  with $m_a,m_b$ real and $m_c^2$ allowed complex. One eigenvalue is
  required negative by fiat. The closest *shape* analogue of our
  doublet sector, but no Casimir scaling and the parameters $m_a,m_b,m_c$
  are unconstrained except by the negativity requirement.
- Chivukula–Dobrescu–Georgi–Hill: This is a fermion-side seesaw; the
  matrix shape $[[0,M],[M,-m]]$ is the closest published analogue of
  Eq. (1) restricted to the doublet, but applied to top and a heavy
  vectorlike fermion, with **no group-theory derivation** of the
  zero in the $(1,1)$ slot beyond "the top is left-handed only".

**Bottom line of literature comparison:** The Casimir-locked seed of
PAPER.md is structurally novel: no published bosonic-seesaw construction
ties the off-diagonal to $\sqrt{C_2(R)}$ and the lower-diagonal to
$-C_2(R)$ via a single representation-labelled $m_0$. Haba et al.\
supplies the closest *radiative* mechanism for the negative
mass-squared piece (feature (ii) sign + magnitude) and is the right
citation for §4.3 M4 of PAPER.md, but does **not** derive (iii).

---

## 5. Concrete next steps to close the residual gap

Three calculations would settle the question whether $\sqrt{C_2(R)}$ is
derivable or must remain a postulate.

1. **Clebsch-Gordan / multiplet-embedding test.** Embed $(s,\Phi_R)$
   into an irreducible rep $R'$ of a larger group $G\supset \mathrm{SU}(2)_W$
   such that $R'$ branches under $\mathrm{SU}(2)_W$ as $\mathbf{1}\oplus R$.
   The off-diagonal block of the parent Casimir $C_2(G)\big|_{R'}$
   restricted to the $(\mathbf{1},R)$ off-diagonal is a Clebsch coefficient
   $\propto\sqrt{C_2(R)}$ for some natural choices of $G$ and embedding.
   Specifically, for $G=\mathrm{SU}(2)\times\mathrm{SU}(2)$ with $R'$ the
   bidoublet, or for $G=\mathrm{SO}(N)$ embedding via the Slansky chain of
   §5.1, check whether the bilinear $\mathbf 1\,T^a_{R'}\,R$ matrix
   element saturates $\sqrt{C_2(R)}$. If yes, the
   $\sqrt{C_2}$ off-diagonal is a **group-theory consequence of the
   parent-group embedding** and Rule A (§3.1 of PAPER.md) plus the
   parent group fixes feature (iii). This is by far the most promising
   route and ties directly to the SO(32) embedding already discussed
   in §5.1.

2. **Custodial-extension test.** Augment the singlet $s$ to a multiplet
   $S^a$ in the adjoint (matching the spurion direction). Then
   $S^a\Phi^\dagger T^a\Phi$ is a true bilinear mass-mixing operator
   between the $(\dim_{\rm adj})$ components of $S^a$ and $\Phi_R$. The
   $(\dim_{\rm adj}\times \dim R)\times(\dim_{\rm adj}\times\dim R)$
   mass matrix can be diagonalized; the magnitude of the off-diagonal
   block in the singlet-projected basis is exactly $\sqrt{C_2(R)}$ —
   *if* the projection is well-defined. Check whether the bare-singlet
   projector $P_s$ commutes with the matrix in a way that leaves an
   effective 2x2 with $\sqrt{C_2}$ off-diagonal. This is the
   "adjoint-extended $S$" completion.

3. **Bilinear lift via auxiliary heavy field.** Introduce a heavy
   complex scalar $\chi_R^a$ in the (adjoint $\otimes$ R) rep with
   mass $M_\chi\gg m_0$. Couple via renormalizable bilinears
   $\chi^{a\dagger} T^a\Phi_R\, S/M_\chi + \text{h.c.}$. After
   integrating out $\chi$, the induced effective $S\Phi_R$ bilinear
   gets a coefficient
   $\sim \mathrm{tr}_R[T^aT^a]/M_\chi = C_2(R)\dim R/(M_\chi\dim_{\rm adj})$
   — gives $C_2$, not $\sqrt{C_2}$. So this UV completion does **not**
   produce feature (iii); the trace closes one full adjoint loop.

The first route (Clebsch-Gordan from a parent-group embedding) is the
most promising. It is the only one that ties (iii) to a derivation rather
than a postulate, and it is consistent with the SO(32) parent-group
chain already cited in PAPER.md §5.1. A symbolic computation of the
relevant Clebsch coefficients for the doublet and triplet of
$\mathrm{SU}(2)_W$ embedded in $\mathrm{SO}(4)\subset\mathrm{SO}(32)$ is
the concrete next step.

---

## 6. Peer-agent input: partial compositeness à la Caracciolo–Parolini–Serone

After completing the L1–L5 analysis above we peeked at the sibling agents' work in `/home/codexssh/weak/model/lagrangian/` (read-only). They have independently arrived at the same problem and have proposed a concrete UV framework: **partial compositeness in the sense of Caracciolo, Parolini and Serone, "UV Completions of Composite Higgs Models with Partial Compositeness," arXiv:1211.7290 (SISSA-32/2012/EP)**.

The peer construction (`model/lagrangian/L_PC_sketch.py`):

- A hypercolor gauge group $\mathrm{SU}(N)_{\rm HC}$ confines at scale $\Lambda_{\rm HC}\sim$ TeV.
- $\mathrm{SU}(2)_W$ is gauged as a subgroup of the global symmetry of the HC sector.
- For each $R\in\{2,3\}$ of $\mathrm{SU}(2)_W$ there are two scalar copies:
  - **elementary** $\Psi_R$: an SM-style elementary scalar with bare mass protected to zero by a $\mathbb{Z}_2$ acting on $\Psi$ (the $(1,1)$ slot of Eq.~(1));
  - **composite** $\chi_R$: a HC bound state in rep $R$ of $\mathrm{SU}(2)_W$, with strong-dynamics mass $-m_\chi^2$ on the $(2,2)$ slot.
- Mixing: $\mathcal{L}_{\rm mix} = y\,\epsilon^A\,\Psi_R^a (T^A_R)_{ab}\,\chi_R^b + \text{h.c.}$, with $\epsilon^A$ an adjoint spurion (its dimensionful magnitude $y|\epsilon|$ playing the role of $m_0^2$).

The peer sketch claims the resulting 2x2 mass matrix in the $(\Psi,\chi)$ basis is
$$
M^2 \;=\; \begin{pmatrix} 0 & y|\epsilon|\sqrt{C_2(R)}\\ y|\epsilon|\sqrt{C_2(R)} & -m_\chi^2\end{pmatrix},
$$
and identifies the Casimir-locked $a=b=1$ shape by imposing $m_\chi^2 = y|\epsilon|\,C_2(R)$ — i.e.\ the composite mass-squared and the elementary–composite mixing are tied to the same UV origin with a $C_2(R)$ enhancement on the composite-mass side.

**What the peer reading buys us:**

- A **physically motivated origin for the $(1,1)$ zero**: in PC the elementary $\Psi$ has no bare mass; the zero is forced by a chiral protection that is generic in PC constructions.
- A **physically motivated origin for the $-C_2(R)$ scaling on the $(2,2)$ slot**: the composite mass comes from a contraction $\langle\chi^\dagger T^a T^a\chi\rangle = C_2(R)\langle|\chi|^2\rangle$ when $\mathrm{SU}(2)_W$ is gauged inside the HC global symmetry. This is *automatic* in PC for a confining HC sector that respects $\mathrm{SU}(2)_W$ as a vector subgroup.
- A **published precedent for the framework** (Caracciolo et al.\ 1211.7290), which legitimates the UV reading.

**What the peer reading does *not* settle:** exactly the same $\sqrt{C_2(R)}$ obstruction as L1. The peer's "$M_{\rm mix} = y|\epsilon|\sqrt{C_2(R)}$" is obtained by equating $\sqrt{\mathrm{Tr}_R(T^A T^A)}=\sqrt{\dim R\cdot C_2(R)}$ with $\sqrt{C_2(R)}$ after a hidden normalisation. Treating $\epsilon^A$ as a fluctuating adjoint VEV (so $\langle\epsilon^A\epsilon^B\rangle\propto\delta^{AB}$) and taking the singlet projection of $\Psi^\dagger T^A\chi$ vanishes ($\mathrm{Tr}\,T^A=0$); treating $\epsilon^A$ as aligned along a single Cartan direction recovers the $j(R) = (\dim R-1)/2$ saturation of L1. Either way, **a single adjoint spurion does not naturally give $\sqrt{C_2(R)}$** in the off-diagonal mass entry. The peer sketch hand-waves this point at lines 78–79 of `L_PC_sketch.py`; the resolution is left to "the HC strong-coupling scale and the elementary–composite mixing share a common origin".

**Convergent picture, with honest gap:**

The peer's partial-compositeness framework supplies the *physics interpretation* of the seed: $\Psi$ = elementary, $\chi$ = composite, mixing from a UV portal between the two. Features (i) and (ii) are derivable in PC. Feature (iii) — the $\sqrt{C_2(R)}$ off-diagonal — still needs the Wigner–Eckart / Clebsch–Gordan argument of our own §5 step 1: $\Psi$ and $\chi$ are to be reinterpreted as the singlet and rep-$R$ projections of a single parent multiplet $R'$ in a larger group $G\supset\mathrm{SU}(2)_W$ (the same SO(32) chain as PAPER.md §5.1). The matrix element of $T^A_{R'}$ between the singlet and the $R$-component is then $\propto\sqrt{C_2(R)}$ by Wigner–Eckart, *not* by isotropy of $\epsilon^A$.

So the synthesis is:

| Feature | Partial-compositeness (peer) | Parent-rep / Wigner–Eckart (our §5) |
|---------|---|---|
| (i) $(1,1)=0$ | Elementary $\Psi$ has no bare mass | Chiral protection on the singlet branch |
| (ii) $(2,2)=-m_0^2 C_2(R)$ | $\langle\chi T^aT^a\chi\rangle = C_2(R)|\chi|^2$ from HC dynamics | Parent Casimir restricted to the $R$ branch |
| (iii) $(1,2)=m_0^2\sqrt{C_2(R)}$ | **Hand-waved** in the peer sketch | $\langle 1|T^a_{R'}|R\rangle\propto\sqrt{C_2(R)}$ by Wigner–Eckart |

The two readings are not competing; they are *compatible*. PC supplies the elementary/composite skeleton and the strong-dynamics origin of the $-C_2(R)$ tachyonic slot; the parent-rep embedding supplies the algebraic origin of the $\sqrt{C_2(R)}$ off-diagonal. A fully successful Lagrangian construction would have:

1. A confining HC sector whose global symmetry $G_{\rm global}\supset\mathrm{SU}(2)_W$ branches to produce both the elementary (singlet) and composite ($R$) representations as components of a single parent multiplet $R'$.
2. The IR mass-mixing structure of Eq.~(1) emerging from the parent-rep covariant derivative once $G_{\rm global}\to\mathrm{SU}(2)_W$ via the Wilson-line / Hosotani mechanism.

The Caracciolo–Parolini–Serone framework realises (1) explicitly for the Higgs sector with $\mathrm{SO}(5)/\mathrm{SO}(4)$ coset; an analogous construction for our $(\mathbf{1}\oplus\mathbf{2}\oplus\mathbf{3})$ content is the natural next derivation target.

---

## 7. Honest summary

No mechanism in $\{L_1,\dots,L_5\}$ alone cleanly derives all three features.

- (i) $M^2_{ss}=0$ is **derivable** from a $\mathbb{Z}_2$ symmetry $S\to -S$ or from chiral protection on an elementary field in PC.
- (ii) $M^2_{\phi\phi}=-C_2(R)\,m_0^2$ is **derivable** from $-m_0^2\Phi_R^\dagger T^aT^a\Phi_R$, either postulated as a renormalisable operator or generated dynamically by HC confinement (PC) or radiatively (Haba 1508.06828).
- (iii) $M^2_{s\phi}=\sqrt{C_2(R)}\,m_0^2$ has **no renormalisable origin from a single adjoint spurion** (saturation at $j(R)<\sqrt{C_2(R)}$). The peer agents' partial-compositeness sketch hand-waves this point. The square-root operator $S\sqrt{\Phi^\dagger T^aT^a\Phi}$ produces the right shape but is non-renormalisable. The only known route that derives $\sqrt{C_2(R)}$ without postulating it is the **Wigner–Eckart matrix element of $T^A$ in a parent representation $R'\supset\mathbf{1}\oplus R$** — convergent with both the peer-agent partial-compositeness reading and the SO(32) parent-group embedding of PAPER.md §5.1.

**Verdict on whether we now have a Lagrangian:** *not yet*. We have:
1. A peer-validated effective-Lagrangian framework (partial compositeness, Caracciolo et al.\ 1211.7290) that supplies features (i) and (ii) from physical principles, and
2. A concrete group-theory route (Wigner–Eckart in a parent rep) that would supply feature (iii) as a derived Clebsch coefficient rather than a postulate.

These two ingredients have not yet been combined into a single explicit Lagrangian with a derivable seed matrix. The combination is the next concrete derivation task. The §6(a) caveat in PAPER.md ("the seed structure is engineered, not derived") still stands honestly, but is now narrower: the remaining algebraic gap is a *single* Clebsch coefficient inside a partial-compositeness UV completion, not the whole seed structure.
