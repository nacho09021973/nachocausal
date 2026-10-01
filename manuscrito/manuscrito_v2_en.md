# Exact tangent visibility of finite causal-order laws and Fisher resolution in the S1 model

## Abstract

We study the unlabeled causal-order channel of an explicit $1+1$-dimensional conformal interaction model (S1), expanded at an independent reference geometry. For each cardinality $N$ we determine exactly which first-order perturbations survive the passage from the continuous copula to the law of the unlabeled causal order. The answer is $V_N=\operatorname{Sym}^2P_{N-1}$, where $P_{N-1}\subset L^2_0([0,1])$ is spanned by the first $N-1$ centered shifted-Legendre modes; the visible spaces have dimension $\binom N2$, are strictly nested, and their union is dense in the symmetric interaction Hilbert space. The score differential factors as $D\mathscr S_N=B_NP_N^{\rm vis}$ with $B_N$ injective, so its kernel is the symmetric orthogonal complement of $V_N$ together with the entire antisymmetric sector. Visibility and statistical resolution are different questions: the Fisher operator on $V_N$ is positive definite but anisotropic, and need not be diagonal in the modal basis. Normalized by $N$ continuous copula observations it converges to the symmetric projection in the strong operator topology, but not in operator norm. Finally, one explicit antisymmetric exponential orbit has an even finite-poset law whose first nonzero jet is of order exactly two for every $N\ge2$.

## 1. Introduction

In the S1 model, which components of a conformal perturbation remain visible after passing from the continuous copula to the unlabeled causal-order law at fixed cardinality $N$?

The object in question is due to [Bombelli2000]: the full law of an unlabeled causal poset at fixed cardinality $N$, sampled from a Lorentzian geometry. [Janson2011] supplies the limiting framework of poset kernels and consistent finite laws in which the construction sits, and [Surya2026] gives a related account, through expected interval abundances, of how increasing $N$ lifts degeneracies. None of the three computes the differential of the finite-$N$ law at a reference geometry.

Two ingredients of an answer exist in adjacent literatures. At the level of *labeled* permutations rather than *unlabeled* two-dimensional posets, the differential of a permutation-pattern statistic around the uniform reference is well understood: [EvenZohar2020] decomposes pattern densities via the representation theory of $S_N$ and isolates the standard-representation block realized through permutation matrices compressed to $\mathbf1^\perp$, and [Kurecka2022] differentiates the pattern density directly in a Bernstein-type basis on $E_N=\mathbf1^\perp$. In matrix form the two levels are separated by

$$
\mathbb R^{\mathcal C_N}
\xrightarrow{\ J_N\ }
\mathbb R^{S_N}
\xrightarrow{\ T_N\ }
\operatorname{End}(E_N),
\qquad
J_Ne_C=\mathbf1_{\Gamma_C},
\qquad
T_N(t)=\Bigl.\sum_{\pi\in S_N}t_\pi P_\pi\Bigr|_{E_N},
\tag{1.1}
$$

where $\mathcal C_N$ indexes unlabeled two-dimensional poset classes and $\Gamma_C\subset S_N$ is the fiber of $C$. Kurečka's gradient map has kernel $\ker T_N$. The causal-order quotient restricts the domain to the fiber-constant subspace $\operatorname{im}J_N$; what is needed is the *image* of that restriction. The abstract target module is also classical — [Diaconis1989] gives $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$ of dimension $\binom N2$ for unordered-pair effects on rankings — and so is the permutation-to-poset correspondence itself, whose fibers are described by [BayoumiElZaharKhamis1994].

The step taken here is to sum the permutation-level differential over these fibers and identify what the class sums span.

**Main result.** For every $N\ge2$, the class-sum score representatives span the full symmetric target module,

$$
\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}
=V_N=\operatorname{Sym}^2P_{N-1},
\qquad
\dim V_N=\binom N2,
$$

equivalently $T_N(\operatorname{im}J_N)=\operatorname{Sym}(E_N)$. This is Theorem 1 (§4); the proof is constructive at every $N$ and does not enumerate posets.

**Consequences.** The exact kernel, the identifiable quotient, and the factorization $D\mathscr S_N=B_NP_N^{\rm vis}$ with $F_N=B_N^*B_N$ positive definite on $V_N$ (§5) all follow from the span, together with strict nesting $V_N\subsetneq V_{N+1}$ and density of $\bigcup_NV_N$ in the symmetric sector.

**Second result.** In the fixed symmetric Hilbert–Schmidt sector, Fisher information is asymptotically retained: normalized by $N$ continuous copula observations, $\widehat F_N\to\Pi_{\rm sym}$ in the strong operator topology, and not in norm (§6).

**Final observation.** One explicit antisymmetric orbit has $r_N(\gamma_\psi)=2$ for every $N\ge2$: invisible at first order, detected at second (§7). This is an existence statement for a single witness, not a classification of the antisymmetric sector.

Everything below concerns the S1 model in a $1+1$-dimensional causal diamond, at first order (resp. second order in §7) about the independent reference point. No statement here concerns higher dimensions, general Lorentzian spacetimes, Schwarzschild or horizons, nonlinear identifiability at finite distance, or reconstruction of a geometry from a causet. §9 records the limits precisely.

## 2. The S1 model and the finite causal-order channel

Work in the flat $1+1$-dimensional causal diamond in null coordinates, reparametrized to $D=[0,1]^2$ with the product order $(u,v)\preceq(u',v')\iff u\le u',\ v\le v'$ and the uniform reference measure $\mu_0(du\,dv)=du\,dv$. A conformal generator $\psi\in C(D;\mathbb R)$ defines the volume-preserving exponential family

$$
g_\varepsilon=\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}\,g_0,
\qquad
Z(\varepsilon)=\int_De^{2\varepsilon\psi}\,d\mu_0,
\tag{2.1}
$$

whose sampling density for a Poisson sprinkling conditioned on $N$ points is $q_\varepsilon=e^{2\varepsilon\psi}/Z(\varepsilon)$. Differentiating at $\varepsilon=0$ gives $\dot g_0=2(\psi-\bar\psi)g_0$.

Four objects along the chain from geometry to statistic are kept separate: the generator $\psi$; the log-tangent $t_\psi=2(\psi-\bar\psi)$ of the normalized joint density; the copula-density tangent obtained after uniformizing both marginals,

$$
h_\psi=2\bigl[\psi-\psi_U-\psi_V+\bar\psi\bigr]=2\mathcal P\psi,
\qquad
\mathcal P=(I-M_u)(I-M_v),
\tag{2.2}
$$

with $\psi_U,\psi_V$ the marginal means; and the score of the finite discrete experiment. Both families have reference density $1$ at $\varepsilon=0$, but their tangents differ in general, by the marginal terms $2(\psi_U+\psi_V-2\bar\psi)$; passing to ranks applies the marginal probability integral transform and removes marginal information, so only $h_\psi$ is seen by the finite experiment.

A sample of $N$ points gives three progressively coarser observations. The continuous sample $(U_k,V_k)_{k\le N}$ has score $T_{N,\psi}=\sum_kh_\psi(U_k,V_k)$. Ordering by $U$ and recording the induced $V$-rank gives a *labeled* rank permutation $\Pi_N\in S_N$. Finally, the datum a causal set exposes is the *unlabeled* isomorphism class $[P_{\Pi_N}]$ of the permutation matrix, invariant under the choice of linear realizer.

Write $\mathcal C_N$ for the isomorphism classes of two-dimensional posets realized at cardinality $N$ and $\Gamma_C=\{\sigma\in S_N:[P_\sigma]=C\}$. The law studied throughout is

$$
\mu_{N,\varepsilon}^{[P]}(C):=\mathbb P_\varepsilon\bigl([P_{\Pi_N}]=C\bigr)
=\sum_{\sigma\in\Gamma_C}p_\varepsilon(\sigma),
\qquad
\mu_{N,0}^{[P]}(C)=\frac{|\Gamma_C|}{N!}>0,
\tag{2.3}
$$

closing the chain $\psi\to\dot g_0\to t_\psi\to h_\psi\to S_{N,\psi}\to\mu_{N,\varepsilon}^{[P]}$.

Throughout, $H=L^2_0([0,1])$ is the mean-zero space with shifted-Legendre basis $(p_m)_{m\ge1}$, orthonormalized as $(\ell_m)_{m\ge1}$ where convenient, $P_{N-1}=\operatorname{span}\{p_1,\ldots,p_{N-1}\}$, and $\mathcal X=H\widehat\otimes H$ with its symmetric and antisymmetric parts $\mathcal X_{\rm sym}=H\widehat\otimes_{\rm sym}H$ and $\mathcal X_{\rm alt}=\bigwedge^2H$. The coordinate-swap involution $(\mathfrak sf)(u,v)=f(v,u)$ is unitary and self-adjoint, with projections $\Pi_{\rm sym}=(I+\mathfrak s)/2$ and $\Pi_{\rm alt}=(I-\mathfrak s)/2$.

## 3. Scores and the quotient to unlabeled posets

**Quadratic-mean differentiability.** Fix an admissible generator $\psi\in C(D)$ and put $f=\mathcal P\psi$. The copula density satisfies $c_\varepsilon=1+2\varepsilon f+o(\varepsilon)$ uniformly on $D$, with both marginals of $f$ vanishing. Positivity and continuity on the compact domain give a common positive lower bound for $c_\varepsilon$ at small $|\varepsilon|$, so Taylor expansion of the square root with uniform remainder gives $\int(\sqrt{c_\varepsilon}-1-\varepsilon f)^2=o(\varepsilon^2)$: the one-observation copula experiment is QMD at zero with score $2f=h_\psi$. Taking the $N$-fold product gives the sample score $T_{N,\psi}=2\sum_kf(U_k,V_k)$.

The event $\{\Pi_N=\sigma\}$ is defined by strict coordinate inequalities and is independent of $\varepsilon$ (ties are null), and $c_\varepsilon$ and its $\varepsilon$-derivative are uniformly bounded near zero, so differentiation under the integral is valid. With $p_\varepsilon(\sigma)=\int_{\{\Pi_N=\sigma\}}\prod_kc_\varepsilon(U_k,V_k)$ and $p_0(\sigma)=1/N!$,

$$
S_N^\Pi(f)(\sigma)=\partial_\varepsilon\log p_\varepsilon(\sigma)\big|_0
=\mathbb E_0\bigl[T_{N,\psi}\mid\Pi_N=\sigma\bigr].
\tag{3.1}
$$

This conditional-score identity follows from the likelihood and assumes no independence after conditioning.

**Representatives.** Let

$$
d_i^{(N)}(t):=N\binom{N-1}{i-1}t^{i-1}(1-t)^{N-i},
\qquad
b_i^{(N)}:=d_i^{(N)}-1
\tag{3.2}
$$

be the $i$-th uniform order-statistic density and its centered version. Under the reference law order statistics are independent of ranks, so the two order-statistic vectors are independent of each other and jointly independent of $\Pi_N$. Given $\Pi_N=\sigma$ the point of $U$-rank $i$ is paired with the point of $V$-rank $\sigma(i)$, and that pair still has density $d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}$, so (3.1) gives $S_N^\Pi(f)(\sigma)=2\sum_i\langle f,d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\rangle$ and hence

$$
p_\sigma'(0;f)=\frac2{N!}\sum_{i=1}^N\bigl\langle f,d_i^{(N)}\otimes d_{\sigma(i)}^{(N)}\bigr\rangle.
\tag{3.3}
$$

Because both marginals of $f$ vanish, writing $d_i^{(N)}=1+b_i^{(N)}$ removes the constant and one-coordinate terms, so $\langle f,d_i^{(N)}\otimes d_j^{(N)}\rangle=\langle f,b_i^{(N)}\otimes b_j^{(N)}\rangle$ and

$$
\boxed{\;R_\sigma^{(N)}:=\frac2{N!}\sum_{i=1}^Nb_i^{(N)}\otimes b_{\sigma(i)}^{(N)},
\qquad
p_\sigma'(0;f)=\bigl\langle f,R_\sigma^{(N)}\bigr\rangle.\;}
\tag{3.4}
$$

The functions $d_i^{(N)}/N$ form the Bernstein basis of degree $N-1$; since $\sum_id_i^{(N)}=N$, centering leaves the single relation $\sum_ib_i^{(N)}=0$, and therefore $\operatorname{span}\{b_i^{(N)}\}=P_{N-1}$, so $R_\sigma^{(N)}\in P_{N-1}\otimes P_{N-1}$. Formula (3.4), derived for admissible continuous tangents, defines a bounded linear functional of every $f\in\mathcal X$; we use this Hilbert-space extension below without claiming that every such $f$ is geometrically realizable.

Summing (3.4) over a fiber, which is finite and $\varepsilon$-independent, gives the class representative and the score of the observable law:

$$
R_C^{(N)}:=\sum_{\sigma\in\Gamma_C}R_\sigma^{(N)},
\qquad
\partial_\varepsilon\mu_{N,\varepsilon}^{[P]}(C)\big|_0=\bigl\langle f,R_C^{(N)}\bigr\rangle,
\qquad
(D\mathscr S_Nf)(C)=\frac{\langle f,R_C^{(N)}\rangle}{\mu_{N,0}^{[P]}(C)}.
\tag{3.5}
$$

Since $\mathcal C_N$ is finite and every reference mass is positive, coordinatewise differentiability is equivalent here to the discrete QMD expansion with score (3.5). That score has zero mean: summing (3.4) over all $\sigma$, each $b_j^{(N)}$ occurs $(N-1)!$ times at every fixed position, and $\sum_jb_j^{(N)}=0$, so $\sum_CR_C^{(N)}=0$.

**Symmetry of the class sums.** Each fiber is closed under inversion. If $i<j$ and $\sigma(i)<\sigma(j)$, then setting $a=\sigma(i),b=\sigma(j)$ gives $a<b$ and $\sigma^{-1}(a)<\sigma^{-1}(b)$, so $i\mapsto\sigma(i)$ is a poset isomorphism $P_{\sigma^{-1}}\cong P_\sigma$: interchanging the two rank coordinates sends $\sigma$ to $\sigma^{-1}$ without changing the abstract poset. Since $(R_\sigma^{(N)})^\top=R_{\sigma^{-1}}^{(N)}$,

$$
\sigma\in\Gamma_C\iff\sigma^{-1}\in\Gamma_C,
\qquad
\bigl(R_C^{(N)}\bigr)^\top=R_C^{(N)},
\qquad
R_C^{(N)}\in\operatorname{Sym}^2P_{N-1}.
\tag{3.6}
$$

**Fisher form and visible space.** Polarizing (3.5),

$$
G_{[P]}^{(N)}(f,g)
=\bigl\langle D\mathscr S_Nf,D\mathscr S_Ng\bigr\rangle_{L^2(\mu_{N,0})}
=\sum_{C\in\mathcal C_N}\frac{\langle f,R_C^{(N)}\rangle\langle g,R_C^{(N)}\rangle}{\mu_{N,0}^{[P]}(C)}.
\tag{3.7}
$$

Because every reference mass is strictly positive, $\ker D\mathscr S_N=\ker G_{[P]}^{(N)}=\operatorname{span}\{R_C^{(N)}\}^{\perp}$, and by (3.6)

$$
V_N:=(\ker D\mathscr S_N)^\perp=\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}\subseteq\operatorname{Sym}^2P_{N-1}.
\tag{3.8}
$$

**Finite reduction.** Put $E_N:=\mathbf1^\perp\subset\mathbb R^N$ and

$$
\Lambda_N:E_N\to P_{N-1},
\qquad
\Lambda_Nz:=\sum_{i=1}^Nz_ib_i^{(N)}.
\tag{3.9}
$$

For $z\in E_N$ one has $\sum_iz_ib_i^{(N)}=\sum_iz_id_i^{(N)}$, which vanishes only when $z=0$ by linear independence of the Bernstein basis; since $\dim E_N=\dim P_{N-1}=N-1$, $\Lambda_N$ is an isomorphism. Fix

$$
P_\sigma:=\sum_{i=1}^Ne_ie_{\sigma(i)}^\top,
\qquad
A_C:=\sum_{\sigma\in\Gamma_C}P_\sigma,
\tag{3.10}
$$

so $A_C\mathbf1=|\Gamma_C|\mathbf1$ and $\mathbf1^\top A_C=|\Gamma_C|\mathbf1^\top$, hence $E_N$ is $A_C$-invariant, and inversion-closure of $\Gamma_C$ makes $A_C|_{E_N}\in\operatorname{Sym}(E_N)$. Identifying $\operatorname{Sym}(E_N)$ with $\operatorname{Sym}^2E_N$ by the Euclidean inner product, let $\mathfrak T_N=(\Lambda_N\otimes\Lambda_N)|_{\operatorname{Sym}^2E_N}$, a linear isomorphism onto $\operatorname{Sym}^2P_{N-1}$ (not an isometry: it preserves spans and ranks, not Fisher eigenvalues). Since $\sum_ib_i^{(N)}=0$, projecting onto $E_N$ in either index leaves the transported tensor unchanged, and (3.4)–(3.5) give exactly

$$
R_C^{(N)}=\frac2{N!}\,\mathfrak T_N\bigl(A_C|_{E_N}\bigr).
\tag{3.11}
$$

The scalar $2/N!$ is nonzero, so the reverse inclusion in (3.8) is equivalent to a purely combinatorial statement:

$$
\boxed{\;V_N=\operatorname{Sym}^2P_{N-1}
\iff
\operatorname{span}\{A_C|_{E_N}:C\in\mathcal C_N\}=\operatorname{Sym}(E_N).\;}
\tag{3.12}
$$

## 4. Exact tangent visibility

**Theorem 1 (class-sum span).** *For every $N\ge2$,*

$$
\boxed{\;V_N=\operatorname{Sym}^2P_{N-1},
\qquad
\dim V_N=\operatorname{rank}G_{[P]}^{(N)}=\binom N2.\;}
$$

*Equivalently, $T_N(\operatorname{im}J_N)=\operatorname{Sym}(E_N)$. The proof exhibits an explicit family of $\binom N2$ poset classes whose class sums span the target, at every $N$, without enumerating posets or extrapolating from small $N$.*

*Proof.* By (3.12) it suffices to prove $\operatorname{span}\{A_C|_{E_N}\}=\operatorname{Sym}(E_N)$.

**Step 1: a family of $\binom N2$ near-chain classes.** For integers $0\le a<b\le N-1$, let $C_{a,b}$ consist of a chain $c_1<\cdots<c_{N-1}$ and one further element $z$ with

$$
c_i<z\ (i\le a),
\qquad
z<c_i\ (i>b),
\qquad
z\parallel c_i\ (a<i\le b).
\tag{4.1}
$$

Every linear extension $L_k$ of $C_{a,b}$ inserts $z$ after exactly $k\in\{a,\ldots,b\}$ chain elements. The intersection $L_s\cap L_t$ places $c_1,\ldots,c_{\min(s,t)}$ below $z$ and $c_{\max(s,t)+1},\ldots,c_{N-1}$ above it, so

$$
L_s\cap L_t=C_{a,b}\iff\{s,t\}=\{a,b\}.
\tag{4.2}
$$

Any $\sigma$ with $P_\sigma\cong C_{a,b}$ pulls the natural order and the $\sigma$-order back to an ordered realizer pair; conversely, enumerating elements in the first order of an ordered realizer pair and recording ranks in the second produces such a $\sigma$. Applying an automorphism or a simultaneous relabeling to both orders leaves the relative-rank permutation unchanged, so the choice of isomorphism contributes nothing further. By (4.2) the only ordered realizer pairs are $(L_a,L_b)$ and $(L_b,L_a)$; normalizing the first extension to the natural order makes the relative permutation a cycle $\tau_{a,b}$ on the consecutive interval $I_{a,b}=\{a+1,\ldots,b+1\}$, and reversing the pair gives its inverse. Hence

$$
\Gamma_{C_{a,b}}=\{\tau_{a,b},\tau_{a,b}^{-1}\}
\tag{4.3}
$$

as a set without multiplicity; for $b=a+1$ the cycle is a transposition and the two coincide. These classes are pairwise distinct: the multiset of strict-past cardinalities is $\{0,\ldots,b-1,b+1,\ldots,N-1\}\uplus\{a\}$, which omits $b$ and repeats $a$, so it determines $(a,b)$.

**Step 2: from interval cycles to edge Laplacians.** For $1\le i<j\le N$ put $L_{ij}:=(e_i-e_j)(e_i-e_j)^\top$, understood below as restricted to $E_N$. Each annihilates $\mathbf1$; a vanishing combination on $E_N$ therefore vanishes on all of $\mathbb R^N$, and its $(i,j)$ entry is $-w_{ij}$, so every coefficient is zero. As there are $\binom N2=\dim\operatorname{Sym}(E_N)$ of them, they form a basis, and summing all edges gives

$$
\sum_{1\le i<j\le N}L_{ij}=NI_{E_N}.
\tag{4.4}
$$

Set $S_{a,b}:=P_{\tau_{a,b}}+P_{\tau_{a,b}}^\top$, so by (4.3)

$$
S_{a,b}=2A_{C_{a,b}}\ (b=a+1),
\qquad
S_{a,b}=A_{C_{a,b}}\ (b>a+1),
\tag{4.5}
$$

a nonzero scalar multiple either way, and put $Q_{a,b}:=2I_{E_N}-S_{a,b}|_{E_N}$. Since $\tau_{a,b}$ is the consecutive cycle on $I_{a,b}$, $Q_{a,b}$ is exactly that cycle's graph Laplacian, with the unique edge counted twice when the interval has length two:

$$
Q_{a,a+1}=2L_{a+1,a+2},
\qquad
Q_{a,b}=L_{a+1,b+1}+\sum_{k=a+1}^bL_{k,k+1}\quad(b>a+1).
\tag{4.6}
$$

These are triangular in interval length and invert as

$$
L_{i,i+1}=\tfrac12Q_{i-1,i},
\qquad
L_{ij}=Q_{i-1,j-1}-\tfrac12\sum_{k=i}^{j-1}Q_{k-1,k}\quad(j>i+1),
\tag{4.7}
$$

so $\operatorname{span}\{Q_{a,b}\}=\operatorname{span}\{L_{ij}\}=\operatorname{Sym}(E_N)$. This does not yet give the class sums, because the shared term $2I_{E_N}$ has been subtracted out of every $Q_{a,b}$.

**Step 3: the identity is itself a class-sum combination.** By (4.4) and (4.7) there are coefficients $c_{a,b}$ with $I_{E_N}=\sum_{a<b}c_{a,b}Q_{a,b}$. Their individual values are not needed, but their sum is. By (4.7) an edge $L_{ij}$ at distance $d=j-i$ carries total coefficient $1-d/2$ in its expression through the $Q$'s: this is $1/2$ for $d=1$, and for $d>1$ it is one long-interval term of coefficient $1$ minus $d$ adjacent terms of coefficient $1/2$. There are $N-d$ edges at distance $d$, so dividing (4.4) by $N$,

$$
s_N:=\sum_{a<b}c_{a,b}
=\frac1N\sum_{d=1}^{N-1}(N-d)\Bigl(1-\frac d2\Bigr)
=\frac{(N-1)(5-N)}{12}.
\tag{4.8}
$$

Substituting $Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}$ gives $(1-2s_N)I_{E_N}=-\sum_{a<b}c_{a,b}S_{a,b}|_{E_N}$, and

$$
\boxed{\;1-2s_N=\frac{N^2-6N+11}{6}=\frac{(N-3)^2+2}{6}>0\;}
\tag{4.9}
$$

for every integer $N$ — it never vanishes, at $N=3$ or anywhere else. Hence $I_{E_N}\in\operatorname{span}\{S_{a,b}|_{E_N}\}$; feeding this back into $Q_{a,b}=2I_{E_N}-S_{a,b}|_{E_N}$ puts every $Q_{a,b}$ in the same span, and Step 2 gives $\operatorname{span}\{S_{a,b}|_{E_N}\}=\operatorname{Sym}(E_N)$. By (4.5) the class sums themselves span, which is (3.12). $\square$

**Corollary 2 (filtration and density).** *For $N\ge2$,*

$$
V_N=\operatorname{Sym}^2P_{N-1}\subsetneq\operatorname{Sym}^2P_N=V_{N+1},
\qquad
\dim V_N=\binom N2,
\qquad
\overline{\bigcup_{N\ge2}V_N}=\mathcal X_{\rm sym}.
\tag{4.10}
$$

*Proof.* Write $x\odot y=x\otimes y+y\otimes x$. Orthogonality of the shifted-Legendre basis gives $P_N=P_{N-1}\oplus\operatorname{span}\{p_N\}$, hence the orthogonal decomposition

$$
V_{N+1}=V_N\oplus\{x\odot p_N:x\in P_{N-1}\}\oplus\operatorname{span}\{p_N\otimes p_N\},
\tag{4.11}
$$

so $p_1\odot p_N\in V_{N+1}\setminus V_N$ and the inclusion is strict at every step, with rank sequence $1,3,6,10,15,\ldots$. For density: if polynomials $q_m\to h$ in $L^2$ then $\|q_m-\int q_m-h\|\le2\|q_m-h\|\to0$, so centered polynomials are dense in $H$; finite sums of elementary tensors from a dense subspace are dense in $\mathcal X$, and applying the continuous projection $\Pi_{\rm sym}$ shows every symmetric Hilbert–Schmidt tensor is approximable by finite sums of symmetrized polynomial tensors, each lying in some $\operatorname{Sym}^2P_m=V_{m+1}$. $\square$

## 5. Kernel, quotient, and Fisher resolution

Let $\mathcal K_N:=L^2_0(\mathcal C_N,\mu_{N,0})$ be the space of mean-zero scores of the finite unlabeled-poset law, and $D\mathscr S_N:\mathcal X\to\mathcal K_N$ the bounded score differential of §3. Put

$$
P_N^{\rm vis}:=\Pi_{V_N}\Pi_{\rm sym},
\qquad
\mathcal X=V_N\oplus V_N^{\perp_{\rm sym}}\oplus\mathcal X_{\rm alt},
\tag{5.1}
$$

where $\perp_{\rm sym}$ denotes the orthogonal complement taken inside $\mathcal X_{\rm sym}$. Since $V_N\subset\mathcal X_{\rm sym}$, $P_N^{\rm vis}$ is the ambient orthogonal projection onto $V_N$.

**Corollary 3 (factorization, kernel, identifiable quotient).** *For $N\ge2$ let $B_N:=D\mathscr S_N|_{V_N}$. Then $B_N$ is injective,*

$$
\boxed{\;D\mathscr S_N=B_NP_N^{\rm vis},
\qquad
\ker D\mathscr S_N=V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H
=\bigl(\operatorname{Sym}^2P_{N-1}\bigr)^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H,\;}
\tag{5.2}
$$

*and, with $q_N$ the quotient map, $U_N([f]):=P_N^{\rm vis}f$ is a canonical isometric isomorphism giving the induced factorization $D\mathscr S_N=B_NU_Nq_N$ and*

$$
\boxed{\;\mathcal X/\ker D\mathscr S_N\simeq V_N=\operatorname{Sym}^2P_{N-1},
\qquad
\dim\bigl(\mathcal X/\ker D\mathscr S_N\bigr)=\binom N2.\;}
\tag{5.3}
$$

*Proof.* By (3.8) and Theorem 1, $(\ker D\mathscr S_N)^\perp=V_N$; splitting the ambient complement along $\mathcal X=\mathcal X_{\rm sym}\oplus\mathcal X_{\rm alt}$ gives the kernel in (5.2) and $\ker P_N^{\rm vis}=\ker D\mathscr S_N$, whence $D\mathscr S_Nf=D\mathscr S_NP_N^{\rm vis}f=B_NP_N^{\rm vis}f$. A vector in $\ker B_N$ lies in $V_N\cap V_N^\perp$, so $B_N$ is injective. Then $U_N$ is well defined, bijective, and isometric because $\|[f]\|=\inf_{k\in\ker}\|f+k\|=\|P_N^{\rm vis}f\|$. $\square$

Consequently, for $f,g\in\mathcal X$,

$$
D\mathscr S_Nf=D\mathscr S_Ng
\iff
P_N^{\rm vis}f=P_N^{\rm vis}g.
\tag{5.4}
$$

Combining (5.2) with Corollary 2 also gives $\bigcap_{N\ge2}\ker D\mathscr S_N=\bigwedge^2H$: the antisymmetric sector is invisible at first order simultaneously at every resolution. §7 shows what this does and does not imply.

**Resolution inside the visible sector.** The projection $P_N^{\rm vis}$ says *which* directions survive, not how strongly the law encodes them. That second datum is

$$
F_N:=B_N^*B_N:V_N\to V_N,
\qquad
D\mathscr S_N^*D\mathscr S_N=P_N^{\rm vis}F_NP_N^{\rm vis},
\tag{5.5}
$$

positive definite on $V_N$ because $B_N$ is injective and $V_N$ finite dimensional. The continuous reference experiment of $N$ independent copula observations has score $2\sum_kf(U_k,V_k)$ and Fisher form $4N\langle f,g\rangle$. Since $D\mathscr S_Nf$ is the conditional expectation of that score given $[P_{\Pi_N}]$ and conditional expectation contracts $L^2$ ([Pollard2013]), $I_N^{[P]}(f)\le4N\|f\|^2$; normalizing by that form gives

$$
\widehat F_N:=\frac1{4N}\,D\mathscr S_N^*D\mathscr S_N\quad\text{on }\mathcal X,
\qquad
0\le\widehat F_N\le I_{\mathcal X},
\qquad
\operatorname{supp}\widehat F_N=V_N.
\tag{5.6}
$$

In general $\widehat F_N\ne P_N^{\rm vis}$, equivalently $F_N\ne4NI_{V_N}$.

**Exact spectra at $N=2,3,4$.** Put

$$
x(t):=t-\tfrac12,
\qquad
q(t):=\bigl(t-\tfrac12\bigr)^2-\tfrac1{12},
\qquad
r(t):=\bigl(t-\tfrac12\bigr)^3-\tfrac3{20}\bigl(t-\tfrac12\bigr),
\tag{5.7}
$$

mutually orthogonal and spanning $P_1,P_2,P_3$ successively, and set $e_{11}=x\otimes x$, $e_{12}=x\otimes q+q\otimes x$, $e_{13}=x\otimes r+r\otimes x$, $e_{22}=q\otimes q$, $e_{23}=q\otimes r+r\otimes q$, $e_{33}=r\otimes r$. For $N=2$, $G_{[P]}^{(2)}(f,g)=256\langle f,e_{11}\rangle\langle g,e_{11}\rangle$. For $N=3$, in the basis $e_{11},e_{12},e_{22}$,

$$
\bigl[G_{[P]}^{(3)}\bigr]=\operatorname{diag}\Bigl(\tfrac1{32},\tfrac1{1200},\tfrac1{180000}\Bigr),
\qquad
\bigl[G_{\rm full}^{(3)}\bigr]=\operatorname{diag}\Bigl(\tfrac1{12},\tfrac1{90},\tfrac1{2700}\Bigr).
\tag{5.8}
$$

At $N=4$ three generalized eigenvectors remain pure,

$$
\widehat F_4e_{11}=\tfrac{12}{25}e_{11},
\qquad
\widehat F_4e_{12}=\tfrac4{25}e_{12},
\qquad
\widehat F_4e_{23}=\tfrac4{525}e_{23},
\tag{5.9}
$$

while $\operatorname{span}\{e_{13},e_{22},e_{33}\}$ is an invariant block on which, in that ordered basis,

$$
\bigl[G_{[P]}^{(4)}\bigr]_{\rm mix}
=\begin{pmatrix}
1/55125&1/354375&1/38587500\\
1/354375&11/455625&-1/49612500\\
1/38587500&-1/49612500&11/5402250000
\end{pmatrix},
\qquad
\bigl[G_{\rm full}^{(4)}\bigr]_{\rm mix}=\operatorname{diag}\Bigl(\tfrac1{1050},\tfrac1{2025},\tfrac1{490000}\Bigr),
\tag{5.10}
$$

with generalized eigenvalues the three real positive roots of

$$
144703125\lambda^3-9975000\lambda^2+142000\lambda-128=0,
\tag{5.11}
$$

numerically $0.0494521212879\ldots$, $0.0185160720400\ldots$, $0.000966047034941\ldots$ (for orientation only). Collecting:

| $N$ | $\operatorname{spec}_+(\widehat F_N)$ |
|---|---|
| $2$ | $\{2/9\}$ |
| $3$ | $\{3/8,\ 3/40,\ 3/200\}$, eigenvectors $e_{11},e_{12},e_{22}$ |
| $4$ | $\{12/25,\ 4/25,\ 4/525\}$ from (5.9), together with the three roots of (5.11) |

so that at $N=4$ the exact decreasing order is

$$
\tfrac{12}{25}>\tfrac4{25}>0.0494521212879\ldots>0.0185160720400\ldots>\tfrac4{525}>0.000966047034941\ldots>0.
\tag{5.12}
$$

The spectrum is already anisotropic at $N=3$, and the off-diagonal entries of (5.10) are the first modal mixing: $e_{13},e_{22},e_{33}$ are visible but are not individually Fisher eigenvectors. Membership in $V_N$ is therefore logically prior to, and does not determine, retained Fisher strength. These are exact fixed-$N$ calculations: they give no all-$N$ spectral formula and no monotonicity of eigenvalues in $N$.

## 6. Fisher retention with increasing $N$

Let $I_N^\Pi(f):=\mathbb E_0[S_N^\Pi(f)^2]$ be the Fisher information before the quotient, when the full rank permutation is observed, $I_N^{[P]}(f):=G_{[P]}^{(N)}(f,f)$, and, as a positive semidefinite bilinear form, $\Delta_N(f,g):=\mathbb E_0[S_N^\Pi(f)S_N^\Pi(g)]-G_{[P]}^{(N)}(f,g)=\mathbb E_0[\operatorname{Cov}_0(S_N^\Pi(f),S_N^\Pi(g)\mid[P_{\Pi_N}])]$, written $\Delta_N(f):=\Delta_N(f,f)=I_N^\Pi(f)-I_N^{[P]}(f)$ on the diagonal.

**Theorem 4 (Fisher resolution and asymptotic retention).** *Conditional expectation of scores along $\Pi_N\mapsto[P_{\Pi_N}]$ gives*

$$
\Delta_N(f)=\mathbb E_0\bigl[\operatorname{Var}_0\bigl(S_N^\Pi(f)\mid[P_{\Pi_N}]\bigr)\bigr]\ge0.
\tag{6.1}
$$

*For every $f\in\mathcal X$,*

$$
\frac{I_N^\Pi(f)}N\longrightarrow4\|f\|_{\mathcal X}^2,
\tag{6.2}
$$

*and if in addition $f\in\mathcal X_{\rm sym}$,*

$$
\frac{\Delta_N(f)}N\longrightarrow0,
\qquad
\frac{I_N^{[P]}(f)}N\longrightarrow4\|f\|_{\mathcal X}^2.
\tag{6.3}
$$

*For nonzero symmetric $f$, (6.2) gives a finite, generally nonuniform threshold $N_0(f)$ with $I_N^\Pi(f)>0$ for $N\ge N_0(f)$; on that range put*

$$
\rho_N(f):=\frac{I_N^\Pi(f)}{4N\|f\|^2},
\qquad
\kappa_N(f):=\frac{I_N^{[P]}(f)}{I_N^\Pi(f)},
\qquad
\eta_N^{\rm tot}(f):=\rho_N(f)\kappa_N(f)=\frac{I_N^{[P]}(f)}{4N\|f\|^2}.
\tag{6.4}
$$

*Then*

$$
\boxed{\;\rho_N(f)\to1,
\qquad
\kappa_N(f)\to1,
\qquad
\eta_N^{\rm tot}(f)\to1,
\qquad\text{the last equivalent at operator level to}\qquad
\widehat F_N\xrightarrow{\ \rm SOT\ }\Pi_{\rm sym}.\;}
\tag{6.5}
$$

*More generally, for $0\ne f=f_s+f_a$ decomposed into symmetric and antisymmetric parts,*

$$
\frac{I_N^{[P]}(f)}{4N\|f\|^2}\longrightarrow\frac{\|f_s\|^2}{\|f_s\|^2+\|f_a\|^2};
\tag{6.6}
$$

*the antisymmetric sector contributes zero to the numerator at every $N$, not merely asymptotically.*

The first limit in (6.5) concerns continuous observations versus ranks, the second ranks versus the unlabeled poset. They are distinct claims, and neither follows from the strict inclusions of Corollary 2.

*Proof.* Set $H_{ij}^{(N)}(f):=\langle f,d_i^{(N)}\otimes d_j^{(N)}\rangle$, so that $S_N^\Pi(f)(\sigma)=2\sum_iH_{i\sigma(i)}^{(N)}(f)$ by §3. Since $\sum_id_i^{(N)}=N$ and both marginals of $f$ vanish, $H^{(N)}(f)$ has zero row and column sums.

*(i) Exact Gram identity.* If $H,K$ have zero row and column sums and $\Pi_N$ is uniform, splitting the average by $i=j$ and $i\ne j$ gives $\mathbb E_0[\sum_iH_{i\Pi_N(i)}\sum_jK_{j\Pi_N(j)}]=\langle H,K\rangle_F/(N-1)$: the diagonal contributes $N^{-1}\langle H,K\rangle_F$, while the zero-sum identities reduce the off-diagonal numerator to $\langle H,K\rangle_F$ with probability factor $1/[N(N-1)]$. Hence

$$
I_N^\Pi(f)=\frac4{N-1}\bigl\|H^{(N)}(f)\bigr\|_F^2.
\tag{6.7}
$$

*(ii) Limit (6.2).* Let $\mathcal O_Na:=(\langle a,d_i^{(N)}\rangle)_{i\le N}$, so $H^{(N)}=(\mathcal O_N\otimes\mathcal O_N)f$, and $\widetilde{\mathcal O}_N:=N^{-1/2}\mathcal O_N$. The positive operator $\widetilde{\mathcal O}_N^*\widetilde{\mathcal O}_N$ is the Bernstein–Durrmeyer operator of degree $N-1$. It is triangular on the nested polynomial spaces, with the beta-integral formula giving a monomial of degree $m\le N-1$ the diagonal coefficient $N!(N-1)!/[(N+m)!(N-1-m)!]$; self-adjointness then makes the orthogonal differences between successive polynomial spaces invariant, so the $\ell_m$ are eigenfunctions with

$$
\lambda_{N-1,m}=\prod_{r=1}^m\frac{N-r}{N+r}\in[0,1]\ \ (1\le m\le N-1),
\qquad
\lambda_{N-1,m}=0\ \ (m\ge N),
\tag{6.8}
$$

and $\lambda_{N-1,m}\to1$ for each fixed $m$. Writing $f=\sum_{j,k}c_{jk}\ell_j\otimes\ell_k$, (6.7) becomes $I_N^\Pi(f)/N=\frac{4N}{N-1}\sum_{j,k}\lambda_{N-1,j}\lambda_{N-1,k}|c_{jk}|^2$, and dominated convergence in the square-summable array gives (6.2). Jensen's inequality with $\sum_id_i^{(N)}=N$ gives $\|\mathcal O_Na\|_{\ell^2}\le\sqrt N\|a\|$, hence the uniform bound

$$
0\le\frac{I_N^\Pi(f)}N\le\frac{4N}{N-1}\|f\|_{\mathcal X}^2\le8\|f\|_{\mathcal X}^2
\qquad(N\ge2).
\tag{6.9}
$$

*(iii) The fiber event.* Let $\mathcal G_N$ be the event that the strong interval tree of $\Pi_N$ has a prime root and every child of the root is either a leaf or a twin — a linear node with two leaf children. This is *not* the event that the whole incomparability graph is prime; twins are allowed. The strong interval tree is the modular decomposition tree of the permutation graph ([BouvelChauveMishnaRossin2009], Remark 1), so $\mathcal G_N$ is $[P_{\Pi_N}]$-measurable, the unlabeled poset determining its incomparability graph up to isomorphism. Theorem 2 of [BouvelChauveMishnaRossin2009], whose proof applies their Lemma 1 with $c=1$, states that the complement of this event has probability $O(N^{-1})$; so there are finite $C_{\rm fib},N_{\rm fib}$ with $\mathbb P_0(\mathcal G_N^c)\le C_{\rm fib}/N$ for $N\ge N_{\rm fib}$ (the source does not specify these constants and we do not sharpen them).

On $\mathcal G_N$ the fiber is exactly $\{\Pi_N,\Pi_N^{-1}\}$. Indeed, fix $\pi\in\mathcal G_N$ with maximal strong blocks $B_1,\ldots,B_m$ below the root and inflation $\pi=\alpha[\tau_1,\ldots,\tau_m]$; the root condition makes the incomparability graph of $\alpha$ prime and forces $|B_s|\le2$, so $\tau_s\in\{1,12,21\}$. If $[P_\sigma]=[P_\pi]$, a poset isomorphism carries canonical maximal strong modules to one another preserving sizes and induced types, so contracting gives isomorphic quotient posets. Gallai's uniqueness theorem for the two transitive orientations of a prime comparability graph ([Gallai1967]), after normalizing both linear orders by rank, forces the quotient permutation of $\sigma$ to be $\alpha$ or $\alpha^{-1}$. In the first case each internal pattern is fixed, since on a two-element block $12$ induces a chain and $21$ an antichain and an isomorphism cannot exchange them; in the second the inverse-of-an-inflation formula applies and the internal patterns $1,12,21$ are all involutions, giving $\pi^{-1}$.

*(iv) Fourth moment for symmetric finite rank.* Let $f=\sum_{r\le R}\alpha_ra_r\otimes a_r$ with centered orthonormal $a_r$. Put $x_i=(\mathcal O_Na)_i$ for one fixed profile, $S_2=\sum_ix_i^2$, $S_4=\sum_ix_i^4$, $(N)_r=N(N-1)\cdots(N-r+1)$. Then $\sum_ix_i=0$, $N^{-1}S_2\to\|a\|^2$, and $\max_i|x_i|=o(\sqrt N)$: for the last, choose bounded $b$ close to $a$ in $L^2$ and use $0\le d_i^{(N)}\le N$, $\int d_i^{(N)}=1$ to get $|(\mathcal O_Na)_i|/\sqrt N\le\|b\|_\infty/\sqrt N+\|a-b\|_2$ uniformly in $i$, then let $N\to\infty$ and $b\to a$. For $X_N(a)=\sum_ix_ix_{\Pi_N(i)}$, grouping four indices by coincidence pattern gives, for $N\ge4$,

$$
\mathbb E_0\bigl[X_N(a)^4\bigr]
=\frac{S_4^2}N+\frac{4S_4^2}{(N)_2}+\frac{3(S_2^2-S_4)^2}{(N)_2}
+\frac{6(2S_4-S_2^2)^2}{(N)_3}+\frac{9(S_2^2-2S_4)^2}{(N)_4}.
\tag{6.10}
$$

With $S_2=O(N)$ and $S_4\le(\max_i|x_i|)^2S_2=o(N^2)$ this is $o(N^3)$; since $S_N^\Pi(f)=2\sum_r\alpha_rX_N(a_r)$, Minkowski's inequality in $L^4$ gives $\mathbb E_0[S_N^\Pi(f)^4]=o(N^3)$.

*(v) Retention.* For symmetric $f$, $H^{(N)}(f)$ is symmetric, so $S_N^\Pi(f)(\sigma^{-1})=S_N^\Pi(f)(\sigma)$ and by (iii) the conditional variance in (6.1) vanishes on $\mathcal G_N$. Cauchy–Schwarz with (iii) and (iv) gives, for symmetric $f$ of fixed finite rank,

$$
0\le\Delta_N(f)\le\mathbb E_0\bigl[S_N^\Pi(f)^2\mathbf1_{\mathcal G_N^c}\bigr]
\le\mathbb P_0(\mathcal G_N^c)^{1/2}\,\mathbb E_0\bigl[S_N^\Pi(f)^4\bigr]^{1/2}=o(N).
\tag{6.11}
$$

To remove the rank restriction, note that $\mathcal L_N(f,g):=\Delta_N(f,g)/N$ is a positive form with $\mathcal L_N(f,f)\le8\|f\|^2$ by (6.1) and (6.9). Choose symmetric finite-rank $f_R\to f$; the triangle inequality for the induced seminorm gives $\sqrt{\mathcal L_N(f,f)}\le\sqrt{\mathcal L_N(f_R,f_R)}+\sqrt8\|f-f_R\|$. Taking $N\to\infty$ at fixed $R$ and only then $R\to\infty$ proves (6.3), and (6.4)–(6.5) follow by division once the denominator is positive.

*(vi) Antisymmetric part and SOT.* The transform $f\mapsto H^{(N)}(f)$ intertwines coordinate swap with matrix transpose, so $H^{(N)}(f_s)$ is symmetric and $H^{(N)}(f_a)$ skew; Frobenius orthogonality in (6.7) gives $I_N^\Pi(f)=I_N^\Pi(f_s)+I_N^\Pi(f_a)$, while (5.2) gives $I_N^{[P]}(f)=I_N^{[P]}(f_s)$. With (6.2) and (6.3) this is (6.6). Finally $\langle f,\widehat F_Nf\rangle=I_N^{[P]}(f)/(4N)\to\|\Pi_{\rm sym}f\|^2$; polarization gives weak-operator convergence, and since $0\le\widehat F_N\le I$ implies $\widehat F_N^2\le\widehat F_N$,

$$
\|\widehat F_Nf-\Pi_{\rm sym}f\|^2
\le\langle f,\widehat F_Nf\rangle+\|\Pi_{\rm sym}f\|^2-2\operatorname{Re}\langle\widehat F_Nf,\Pi_{\rm sym}f\rangle\longrightarrow0,
$$

which upgrades the convergence to SOT. $\square$

The convergence in (6.5) is not in operator norm. For the unit vector $h_N:=p_N\otimes p_N/\|p_N\|_{L^2}^2$, Theorem 1 gives $h_N\perp V_N$, so

$$
\widehat F_Nh_N=0,
\qquad
\Pi_{\rm sym}h_N=h_N,
\qquad
\|\widehat F_N-\Pi_{\rm sym}\|\ge1
\quad\text{for every }N.
\tag{6.12}
$$

Nor is $\widehat F_N$ a finite-$N$ projection: its nonzero eigenvalue at $N=2$ is $2/9$. The generic rate in (6.3)–(6.6) is only $o_f(1)$, with no rate or threshold uniform over the Hilbert–Schmidt unit sphere; the available $1-\kappa_N(f)=O(N^{-1/2})$ rate applies only to the bounded continuous finite-rank subclass. These statements concern the Hilbert completion of S1 interaction tangents and transfer directly to tangents already known to arise from admissible S1 paths.

## 7. A second-order antisymmetric witness

Let $\ell_1(t)=\sqrt3(2t-1)$ and $\ell_2(t)=\sqrt5(6t^2-6t+1)$, and set

$$
\psi(u,v):=\ell_1(u)\ell_2(v)-\ell_2(u)\ell_1(v)
=-2\sqrt{15}\,(u-v)\bigl(6uv-3u-3v+2\bigr).
\tag{7.1}
$$

It is antisymmetric under coordinate exchange, has zero marginals and zero mean, and satisfies

$$
\mathcal P\psi=\psi\ne0,
\qquad
h_\psi=2\psi\in\bigwedge\nolimits^2H,
\qquad
\|\psi\|_{L^2(D)}^2=2,
\qquad
\|h_\psi\|_{L^2(D)}^2=8,
\tag{7.2}
$$

so $\psi\notin\ker\mathcal P$: its first-order invisibility is not the marginal gauge of §2. Since $\psi$ is bounded, the normalized family $\gamma_\psi:\varepsilon\mapsto g_\varepsilon$ of (2.1) is an admissible S1 path for every real $\varepsilon$.

Let $\iota(u,v)=(v,u)$. It preserves the product order, the reference measure and the flat metric, while $\psi\circ\iota=-\psi$ and, by change of variables, $Z(-\varepsilon)=Z(\varepsilon)$. Hence

$$
\iota^*g_\varepsilon=g_{-\varepsilon}
\qquad(\varepsilon\in\mathbb R):
\tag{7.3}
$$

the two signs are identified by a discrete isometry of the S1 family.

**Theorem 5 (parity).** *For $\gamma_\psi$, every finite unlabeled-poset law is a real-analytic even function of $\varepsilon$; in particular all odd jets at $\varepsilon=0$ vanish, so $\partial_\varepsilon\mu_{N,\varepsilon}^{[P]}|_0=0$ for every $N\ge2$.*

*Proof.* For $\pi\in S_N$ put $T_\pi:=\sum_i\psi(U_{(i)},V_{(\pi(i))})$, with $U_{(1)}<\cdots<U_{(N)}$ and $V_{(1)}<\cdots<V_{(N)}$ two independent vectors of uniform order statistics and $\langle\cdot\rangle_0$ their joint expectation. The finite likelihood is

$$
p_\pi(\varepsilon)=\frac{\bigl\langle e^{2\varepsilon T_\pi}\bigr\rangle_0}{N!\,Z(\varepsilon)^N}.
\tag{7.4}
$$

Boundedness of $\psi$ on the compact $D$ dominates $e^{2\varepsilon T_\pi}$, $e^{2\varepsilon\psi}$ and all their $\varepsilon$-derivatives on compact $\varepsilon$-intervals, so differentiation under the integral is valid to every order and both numerator and $Z$ are real analytic, with $Z>0$ throughout. Since $\psi(v,u)=-\psi(u,v)$ and the two order-statistic families are i.i.d., exchanging their roles is a valid change of variables which, after reindexing $j=\pi(i)$, turns $T_\pi$ into $-T_{\pi^{-1}}$ and $Z(\varepsilon)$ into $Z(-\varepsilon)=Z(\varepsilon)$. Hence $p_\pi(-\varepsilon)=p_{\pi^{-1}}(\varepsilon)$, and summing over a fiber, closed under inversion by (3.6), gives $\mu_{N,\varepsilon}^{[P]}(C)=\mu_{N,-\varepsilon}^{[P]}(C)$. $\square$

To measure the first nonvanishing response of the complete finite law, define

$$
r_N(\gamma_\psi):=\inf\Bigl\{k\ge1:\ \partial_\varepsilon^k\mu_{N,\varepsilon}^{[P]}\big|_0\ne0\ \text{as a vector on }\mathcal C_N\Bigr\},
\tag{7.5}
$$

with $r_N=\infty$ if every jet vanishes; the invariant refers to the full path, not merely to its vanishing first-order tangent.

**The second jet at $N=2$.** Since $\bar\psi=0$, expanding (7.4) with $Z'(0)=0$ and $Z''(0)=4\|\psi\|^2_{L^2(D)}$ gives

$$
p_\pi'(0)=\frac2{N!}\langle T_\pi\rangle_0,
\qquad
p_\pi''(0)=\frac4{N!}\bigl(\langle T_\pi^2\rangle_0-N\|\psi\|_{L^2(D)}^2\bigr).
\tag{7.6}
$$

At $N=2$ the identity has the chain as its class and the transposition the antichain, each fiber a single involution, so $\mu_2''(C)=p_\pi''(0)$ with $\mu_{2,0}(\text{chain})=\mu_{2,0}(\text{antichain})=\tfrac12$. Both permutations being involutions, $p_\pi(-\varepsilon)=p_\pi(\varepsilon)$ individually and $\langle T_{\rm chain}\rangle_0=\langle T_{\rm antichain}\rangle_0=0$. For the second moments, expand $\psi=\ell_1\otimes\ell_2-\ell_2\otimes\ell_1$ inside each square; independence of the $U$- and $V$-processes factors every cross term, so with

$$
A_{jk}:=\mathbb E\bigl[\ell_j(U_{(1)})\ell_k(U_{(2)})\bigr],
\qquad
M_i(jk):=\mathbb E\bigl[\ell_j(U_{(i)})\ell_k(U_{(i)})\bigr],
\tag{7.7}
$$

direct integration against the pair density $2$ on $0<t_1<t_2<1$ and the marginals $2(1-t)$, $2t$ gives

$$
A_{11}=A_{22}=0,
\quad
A_{12}=-A_{21}=\tfrac1{\sqrt{15}},
\qquad
M_i(11)=M_i(22)=1,
\quad
M_1(12)=-\tfrac2{\sqrt{15}}=-M_2(12).
\tag{7.8}
$$

Expanding $\psi(x,y)^2=\ell_1(x)^2\ell_2(y)^2-2\ell_1(x)\ell_2(x)\ell_1(y)\ell_2(y)+\ell_2(x)^2\ell_1(y)^2$ and grouping $U$- against $V$-factors,

$$
\begin{aligned}
\bigl\langle\psi(U_{(i)},V_{(i)})^2\bigr\rangle_0&=2M_i(11)M_i(22)-2M_i(12)^2=\tfrac{22}{15},\\
\bigl\langle\psi(U_{(1)},V_{(2)})^2\bigr\rangle_0&=M_1(11)M_2(22)-2M_1(12)M_2(12)+M_1(22)M_2(11)=\tfrac{38}{15},\\
\bigl\langle\psi(U_{(1)},V_{(1)})\psi(U_{(2)},V_{(2)})\bigr\rangle_0&=2A_{11}A_{22}-2A_{12}A_{21}=\tfrac2{15},\\
\bigl\langle\psi(U_{(1)},V_{(2)})\psi(U_{(2)},V_{(1)})\bigr\rangle_0&=-\bigl(A_{12}^2+A_{21}^2\bigr)=-\tfrac2{15},
\end{aligned}
\tag{7.9}
$$

whence $\langle T_{\rm chain}^2\rangle_0=2\cdot\tfrac{22}{15}+2\cdot\tfrac2{15}=\tfrac{16}5$ and $\langle T_{\rm antichain}^2\rangle_0=2\cdot\tfrac{38}{15}-2\cdot\tfrac2{15}=\tfrac{24}5$. With $N\|\psi\|^2=4$ and prefactor $4/2!=2$, (7.6) gives

$$
\boxed{\;\partial_\varepsilon^2\mu_{2,\varepsilon}^{[P]}(\mathrm{antichain})\big|_0=\tfrac85,
\qquad
\partial_\varepsilon^2\mu_{2,\varepsilon}^{[P]}(\mathrm{chain})\big|_0=-\tfrac85,\;}
\tag{7.10}
$$

summing to zero as the constant total mass requires, i.e.

$$
\mu_{2,\varepsilon}^{[P]}(\mathrm{antichain})=\tfrac12+\tfrac45\varepsilon^2+O(\varepsilon^4),
\qquad
\mu_{2,\varepsilon}^{[P]}(\mathrm{chain})=\tfrac12-\tfrac45\varepsilon^2+O(\varepsilon^4).
\tag{7.11}
$$

The magnitude of the deformation is thus locally visible already at the smallest cardinality supporting two distinct causal orders, while its sign remains identified by (7.3).

**Propagation by uniform deletion.** For $m\ge3$, $C\in\mathcal C_m$, $D\in\mathcal C_{m-1}$ define

$$
K_{m,m-1}(C,D):=\frac1m\#\bigl\{v\in C:[C\setminus\{v\}]=D\bigr\}.
\tag{7.12}
$$

This is well defined on classes: an isomorphism $\phi:C\to C'$ restricts to an isomorphism $C\setminus\{v\}\to C'\setminus\{\phi(v)\}$, so it carries the counted set bijectively. It is a Markov kernel, since every $v$ deletes into exactly one class and there are $m$ elements, and it is purely combinatorial, hence independent of $\varepsilon$. If $X_1,\ldots,X_m$ are i.i.d. from $q_\varepsilon$ and $V$ is uniform on $\{1,\ldots,m\}$ and independent of them, then for each fixed $j$ the subvector $(X_i)_{i\ne j}$ is an i.i.d. sample of size $m-1$, and averaging over the independent uniform choice leaves that law unchanged; passing to ranks and then to the unlabeled poset gives $\mu_{m-1,\varepsilon}^{[P]}=K_{m,m-1}\mu_{m,\varepsilon}^{[P]}$ for every $\varepsilon$. Composing,

$$
K_{N\to2}:=K_{3,2}\circ\cdots\circ K_{N,N-1},
\qquad
\mu_{2,\varepsilon}^{[P]}=K_{N\to2}\,\mu_{N,\varepsilon}^{[P]},
\tag{7.13}
$$

with $K_{2\to2}=I$. Both sides are functions of $\varepsilon$ valued in finite-dimensional spaces joined by a fixed linear map, so differentiation commutes termwise with it:

$$
\bigl(\mu_2^{[P]}\bigr)^{(k)}(0)=K_{N\to2}\bigl(\mu_N^{[P]}\bigr)^{(k)}(0)
\qquad(k\ge1).
\tag{7.14}
$$

**Corollary 6.** *For the path (7.1),*

$$
\boxed{\;r_N(\gamma_\psi)=2\qquad\forall N\ge2.\;}
\tag{7.15}
$$

*Proof.* Theorem 5 gives $r_N\ge2$. If $(\mu_N^{[P]})''(0)$ vanished for some $N$, then (7.14) with $k=2$ would give $(\mu_2^{[P]})''(0)=0$, contradicting (7.10). $\square$

This is an existence statement for one admissible orbit: it neither classifies the second differential on $\bigwedge^2H$ nor asserts that every antisymmetric direction has order two, and no operator $Q_N$, quadratic null cone, estimator or rate is introduced. The first-order zero is the exact isometric fold $\varepsilon\leftrightarrow-\varepsilon$ of (7.3), so membership in $\ker D\mathscr S_N$ does not imply invariance of the full nonlinear law.

## 8. Relation to previous work

[Bombelli2000] sets up the framework: the complete law of an unlabeled causal poset at fixed cardinality, and a statistical comparison of two such laws. [Janson2011] supplies the limiting framework of poset kernels and consistent finite laws; [Surya2026] shows that increasing resolution lifts degeneracies, through expected interval abundances rather than the full unlabeled-poset law. None computes the differential of the finite-$N$ law, its rank, or its kernel.

The permutation-to-poset correspondence summed over in §3 is classical: [BayoumiElZaharKhamis1994] work explicitly with realizers, the closure of a fiber under $\sigma\mapsto\sigma^{-1}$, and the near-uniqueness of realizers for prime posets.

Before the quotient, the relevant differential structure is close to two existing constructions. [EvenZohar2020] decomposes pattern densities via the representation theory of $S_N$, isolating the standard-representation block of dimension $(N-1)^2$ realized through permutation matrices compressed to $\mathbf1^\perp$; his asymptotic regime concerns fluctuations of a random permutation's pattern profile as the host size grows, a different question from the local $\varepsilon$-derivative used here. The comparison with [Kurecka2022] can be made exact using (1.1): for $t=(t_\pi)$, put $M(t)=\sum_\pi t_\pi P_\pi$; his Lemma 9 expresses every coefficient of the gradient polynomial as a nonzero multiple of $\beta_i^\top M(t)\beta_j$ over a basis $\beta_2,\ldots,\beta_N$ of $E_N$, so the gradient map has kernel $\ker T_N$, and since $M(t)$ has constant row and column sums, $T_N(t)=0$ iff $M(t)$ is constant — his Lemma 12. The permutation-level differential, the Bernstein basis, the compression to $E_N$, the covering-matrix technique and this ambient kernel all belong to that work.

The causal-order quotient adds the first arrow of (1.1). Knowing the ambient kernel rewrites, but does not solve, the restricted-image problem,

$$
\operatorname{rank}(T_NJ_N)=\dim(\operatorname{im}J_N)-\dim\bigl(\operatorname{im}J_N\cap\ker T_N\bigr),
\tag{8.1}
$$

and Kurečka studies neither $\operatorname{im}J_N$ nor this intersection. Inversion-closure gives only $T_N(\operatorname{im}J_N)\subseteq\operatorname{Sym}(E_N)$; the near-chain construction of §4 supplies the reverse inclusion and hence $T_N(\operatorname{im}J_N)=\operatorname{Sym}(E_N)$, which is Theorem 1. [ChanKralNoelPehovaSharifzadehVolec2020] and [GarbeKralMalekshahianPenaguiao2025], on quasirandomness-forcing pattern sums and on the dimension of the feasible region of pattern densities, are adjacent but do not give a fiber-indexed span statement.

The target module is likewise not new. [Diaconis1989] decomposes functions on rankings and gives $M^{(N-2,2)}\simeq S^{(N)}\oplus S^{(N-1,1)}\oplus S^{(N-2,2)}$ for unordered-pair effects — the module and the dimension $\binom N2$ behind a Johnson-scheme reformulation of $\operatorname{Sym}(E_N)$ — and the monograph [Diaconis1988] develops the associated model family. Neither introduces unlabeled two-dimensional-poset fibers or their class sums. What is claimed here is the narrower statement that sums over those fibers generate exactly that module.

Fisher information after passing from continuous observations to ranks is also established. [HallinMelloukRifi2001] find Bernstein-type polynomials in Hájek projections of rank statistics, asymptotically rather than at exact finite $N$; [Hoff2007] establishes the rank likelihood as a marginal-free semiparametric likelihood; [HoffNiuWellner2014] and [SeiMatsumoto2020] develop the induced information and divergence of Gaussian-copula and rank models. None reaches the further quotient $\Pi_N\to[P_{\Pi_N}]$. The operator identity connecting the two levels is standard once the kernel is known: [Pollard2013] shows in the QMD framework that the score of a statistic is the conditional expectation of the original score, and any bounded operator on a Hilbert space factors tautologically through the projection onto the complement of its kernel. So (5.2) is not an independent construction; Theorem 1 is what pins the complement down exactly.

Finally, §7 uses established mechanisms. [RotnitzkyCoxBottaiRobins2000] relate the order of the first nonvanishing derivative to inferential behavior in models with singular information, including the sign ambiguity when that order is even. Within the permuton literature, [Chan2021] and [CrudeleDukesNoel2024] compute Hessians of pattern-density combinations around the uniform permuton once the gradient vanishes. Projective consistency under uniform deletion is standard. Theorem 5 and Corollary 6 combine these for one explicit S1 orbit.

Taken together, the precedents cover the permutation-level differential, the abstract representation-theoretic target, and the general mechanics of statistic-induced scores and singular first-order information. What is determined here is the effect of the additional quotient from labeled rank permutations to unlabeled finite causal-order laws, at every fixed $N$.

## 9. Scope and conclusion

At the independent reference point of the $1+1$-dimensional S1 model, the finite unlabeled causal-order law has an exactly computable local differential structure. The score representatives of §3 reduce the question to class sums over the fibers of the permutation-to-poset map; the constructive argument of §4 gives, for every $N\ge2$,

$$
\operatorname{span}\{R_C^{(N)}:C\in\mathcal C_N\}=V_N=\operatorname{Sym}^2P_{N-1},
\qquad
\dim V_N=\binom N2,
\tag{9.1}
$$

and hence

$$
D\mathscr S_N=B_NP_N^{\rm vis},
\qquad
\ker D\mathscr S_N=V_N^{\perp_{\rm sym}}\oplus\bigwedge\nolimits^2H,
\qquad
\mathcal X/\ker D\mathscr S_N\simeq V_N.
\tag{9.2}
$$

The visible spaces are strictly nested with dense union, so no fixed nonzero symmetric tangent stays invisible at every resolution. Visibility is not sensitivity: $F_N=B_N^*B_N$ is positive definite but anisotropic on $V_N$, and at $N=4$ visible modes mix before Fisher eigenvectors emerge. Normalized by $N$ continuous copula observations,

$$
\widehat F_N\xrightarrow{\ \rm SOT\ }\Pi_{\rm sym},
\qquad
\|\widehat F_N-\Pi_{\rm sym}\|\ge1\ \text{ for every }N,
\tag{9.3}
$$

so every fixed symmetric Hilbert–Schmidt tangent is asymptotically retained, but not uniformly over the unit sphere. Keeping the two stages — continuous observations to ranks, ranks to unlabeled posets — separate is what locates the corresponding Fisher losses. Finally, the antisymmetric orbit of §7 has $r_N(\gamma_\psi)=2$ at every $N\ge2$: a symmetry-forced first-order zero can still carry a nonzero second jet.

The limits of these statements are as follows.

**Model scope.** Every theorem concerns the explicit S1 interaction model in a $1+1$-dimensional causal diamond, expanded at the independent reference point. Nothing here establishes an analogue in $2+1$ or $3+1$ dimensions, for a general Lorentzian spacetime, for Schwarzschild or horizons, or for an arbitrary causal-set sampling model.

**Ambient tangents versus geometric realizability.** $\mathcal X$ is the analytic domain of the score operators, and the identities for $V_N$, $\ker D\mathscr S_N$ and $F_N$ classify the finite channel on that ambient space. They do not prove that every Hilbert–Schmidt direction is generated by an admissible curve of Lorentzian geometries; realizability remains open and is not needed for the classification.

**Differential identification versus nonlinear reconstruction.** Corollary 3 identifies the quotient seen by $D\mathscr S_N$. It does not imply injectivity of $\mathscr S_N$ at finite distance, recovery of coordinates or a metric from one causet, or reconstruction from the family of finite laws. Corollary 6 makes the gap concrete for one orbit; a general second-order operator, its null cone, and a classification of $\bigwedge^2H$ are not developed here.

**Pointwise asymptotics.** (9.3) is strong-operator convergence, with no uniform rate over the unit sphere. The exact Fisher spectra are confined to $N=2,3,4$; no all-$N$ spectral formula, uniform conditioning bound, or estimator is claimed.

**Priority.** The statistical comparison of finite causal-order laws, and the expectation that larger samples sharpen resolution, both have clear precedents, reviewed in §8 together with substantial partial precedents for the individual ingredients. We have not found an exact counterpart of the all-$N$ class-sum span theorem, or of the antisymmetric-orbit statement, in the literature considered there; that absence is not itself a priority claim, and the search was not exhaustive.

## References

- **[BayoumiElZaharKhamis1994]** Bayoumi I. Bayoumi, Mohamed H. El-Zahar, and Soheir M. Khamis. Counting two-dimensional posets. *Discrete Mathematics*, 131 (1–3): 29–37, 1994. doi: 10.1016/0012-365X(94)90370-0.
- **[Bombelli2000]** Luca Bombelli. Statistical Lorentzian geometry and the closeness of Lorentzian manifolds. *Journal of Mathematical Physics*, 41 (10): 6944–6958, 2000. doi: 10.1063/1.1288494.
- **[BouvelChauveMishnaRossin2009]** Mathilde Bouvel, Cédric Chauve, Marni Mishna, and Dominique Rossin. Average-case analysis of perfect sorting by reversals. In *Combinatorial Pattern Matching (CPM 2009)*, volume 5577 of *Lecture Notes in Computer Science*, pages 314–325, 2009. doi: 10.1007/978-3-642-02441-2_28.
- **[Chan2021]** Timothy F. N. Chan. *Substructure Densities in Extremal Combinatorics*. PhD thesis, Monash University and University of Warwick, February 2021.
- **[ChanKralNoelPehovaSharifzadehVolec2020]** Timothy F. N. Chan, Daniel Král', Jonathan A. Noel, Yanitsa Pehova, Maryam Sharifzadeh, and Jan Volec. Characterization of quasirandom permutations by a pattern sum. *Random Structures \& Algorithms*, 57 (4): 920–939, 2020. doi: 10.1002/rsa.20956.
- **[CrudeleDukesNoel2024]** Gabriel Crudele, Peter Dukes, and Jonathan A. Noel. Six permutation patterns force quasirandomness. *Discrete Analysis*, (8), 2024. doi: 10.19086/da.122973.
- **[Diaconis1988]** Persi Diaconis. *Group Representations in Probability and Statistics*, volume 11 of *Institute of Mathematical Statistics Lecture Notes–Monograph Series*. Institute of Mathematical Statistics, 1988. doi: 10.1214/lnms/1215467407.
- **[Diaconis1989]** Persi Diaconis. A generalization of spectral analysis with application to ranked data. *The Annals of Statistics*, 17 (3): 949–979, 1989. doi: 10.1214/aos/1176347251.
- **[EvenZohar2020]** Chaim Even-Zohar. Patterns in random permutations. *Combinatorica*, 40 (6): 775–804, 2020. doi: 10.1007/s00493-020-4212-z.
- **[Gallai1967]** Tibor Gallai. Transitiv orientierbare graphen. *Acta Mathematica Academiae Scientiarum Hungaricae*, 18 (1–2): 25–66, 1967. doi: 10.1007/BF02020961.
- **[GarbeKralMalekshahianPenaguiao2025]** Frederik Garbe, Daniel Král', Alexandru Malekshahian, and Raul Penaguiao. The dimension of the feasible region of pattern densities. *Mathematical Proceedings of the Cambridge Philosophical Society*, 178 (1): 1–14, 2025. doi: 10.1017/S0305004124000380.
- **[HallinMelloukRifi2001]** Marc Hallin, Amal Mellouk, and Khalid Rifi. Projection de hájek et polyn\^omes de bernstein. *Canadian Journal of Statistics*, 29 (1): 141–154, 2001. doi: 10.2307/3316057.
- **[Hoff2007]** Peter D. Hoff. Extending the rank likelihood for semiparametric copula estimation. *The Annals of Applied Statistics*, 1 (1): 265–283, 2007. doi: 10.1214/07-AOAS107.
- **[HoffNiuWellner2014]** Peter D. Hoff, Xiaoyue Niu, and Jon A. Wellner. Information bounds for Gaussian copulas. *Bernoulli*, 20 (2): 604–622, 2014. doi: 10.3150/12-BEJ499.
- **[Janson2011]** Svante Janson. Poset limits and exchangeable random posets. *Combinatorica*, 31 (5): 529–563, 2011. doi: 10.1007/s00493-011-2591-x.
- **[Kurecka2022]** Martin Kurečka. Lower bound on the size of a quasirandom forcing set of permutations. *Combinatorics, Probability and Computing*, 31 (2): 304–319, 2022. doi: 10.1017/S0963548321000298.
- **[Pollard2013]** David Pollard. A note on insufficiency and the preservation of Fisher information. In *From Probability to Statistics and Back: High-Dimensional Models and Processes — A Festschrift in Honor of Jon A. Wellner*, volume 9 of *Institute of Mathematical Statistics Collections*, pages 266–275. 2013. doi: 10.1214/12-IMSCOLL919.
- **[RotnitzkyCoxBottaiRobins2000]** Andrea Rotnitzky, D. R. Cox, Matteo Bottai, and James Robins. Likelihood-based inference with singular information matrix. *Bernoulli*, 6 (2): 243–284, 2000. doi: 10.2307/3318576.
- **[SeiMatsumoto2020]** Tomonari Sei and Kazuya Matsumoto. Properties of divergence for semiparametric copula models. *Proceedings of the Institute of Statistical Mathematics*, 68 (1): 25–44, 2020. URL https://www.ism.ac.jp/editsec/toukei/pdf/68-1-025.pdf.
- **[Surya2026]** Sumati Surya. Closeness function on coarse grained Lorentzian geometries. *Physical Review D*, 113: 024034, 2026. doi: 10.1103/txbf-hvz3.
