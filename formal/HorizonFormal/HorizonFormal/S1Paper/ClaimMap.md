# S1 Paper — Lean formalization claim map

Normative source: `research_program/synthesis/wp6_s1_finite_causal_order_manuscript.tex`
at HEAD `2bd82cd719896bf9e2a3974eef6d8fe1e00dd4b7`. Section/equation numbers below refer
to that file. The outline (`wp6_s1_finite_causal_order_paper_outline.md`) is consulted
only to check proof detail when the `.tex` compresses a step.

This document is planning only. It is written *before* any Lean proof in this
directory and is not edited afterwards to match whatever turned out to be easy —
the `PLANNED_STATUS` column records intent; the final, honest outcome is recorded
separately in `FORMALIZATION_STATUS.md`.

Status vocabulary for this map:

- `TARGET_FULL_PROOF` — intend to prove the mathematical content in Lean.
- `TARGET_LOGICAL_INTERFACE` — intend to prove an abstract theorem whose hypotheses
  are exactly the analytic facts the paper's instance would need; the S1-specific
  instantiation of those hypotheses is not attempted.
- `TARGET_EXACT_CHECK` — a finite, exact arithmetic identity (not an all-N theorem);
  formalized as such and never presented as the all-N statement.
- `OUT_OF_SCOPE_ANALYTIC` — requires substantial new real-analysis/measure-theory
  infrastructure disproportionate to this pass; not attempted.

| PAPER_CLAIM | PAPER_LOCATION | LEAN_TARGET | DEPENDENCIES | PLANNED_STATUS |
|---|---|---|---|---|
| $E_N=\mathbf1^\perp$, $\dim E_N=N-1$ | §3 (3.11), App. B (B.1) | `EN`, `EN_finrank` in `FiniteLinearAlgebra.lean` | rank–nullity for the sum functional | `TARGET_FULL_PROOF` |
| Edge Laplacians $L_{ij}\vert_{E_N}$ linearly independent and span $\operatorname{Sym}(E_N)$ | App. C (C.7)–(C.9) | `edgeLaplacian`, `edgeLaplacian_linearIndependent`, `edgeLaplacian_span` | `EN`, a finite-dim notion of `Sym(E_N)` as symmetric bilinear/self-adjoint endos | `TARGET_FULL_PROOF` |
| Interval-cycle / almost-chain triangularization $\operatorname{span}\{Q_{a,b}\}=\operatorname{Sym}(E_N)$ | App. C (C.10)–(C.16) | `Qab`, `Qab_span` | edge Laplacian basis | `TARGET_FULL_PROOF` (abstract matrices; not yet tied to actual posets — see next row) |
| Identity recovery $1-2s_N=\frac{(N-3)^2+2}{6}>0$ for all $N\ge2$ | App. C (C.18)–(C.20) | `one_sub_two_sN_pos` | pure algebra | `TARGET_FULL_PROOF` |
| $\operatorname{span}\{S_{a,b}\vert_{E_N}\}=\operatorname{Sym}(E_N)$ | App. C (C.19)–(C.21) | `Sab_span` | identity recovery + triangularization | `TARGET_FULL_PROOF` |
| $S_{a,b}$ *is* (up to nonzero scalar) the class sum $A_{C_{a,b}}$ of the near-chain poset family, and hence $\operatorname{span}\{A_C\vert_{E_N}:C\in\mathcal C_N\}=\operatorname{Sym}(E_N)$ | §4 body, App. C (C.11) | bridge lemma tying `Sab` to an actual `A_C` built from a poset/fiber definition | poset isomorphism classes, $\Gamma_C=\{\sigma:[P_\sigma]=C\}$, near-chain poset $C_{a,b}$, proof that $\Gamma_{C_{a,b}}=\{\tau_{a,b},\tau_{a,b}^{-1}\}$ | `TARGET_FULL_PROOF` attempted; realistic risk of landing on `OUT_OF_SCOPE_ANALYTIC`/partial — flagged up front, not a moving target after the fact |
| Transport $\operatorname{span}\{A_C\vert_{E_N}\}=\operatorname{Sym}(E_N)\iff V_N=\operatorname{Sym}^2P_{N-1}$ | App. B (B.9)–(B.10) | — | isomorphism $\mathfrak T_N$/$\Lambda_N$ between $E_N$-matrices and $P_{N-1}\otimes P_{N-1}$, i.e. the Bernstein basis realization of $H$ | `OUT_OF_SCOPE_ANALYTIC` — needs the shifted-Legendre/Bernstein polynomial Hilbert space $H=L^2_0([0,1])$, not attempted here |
| $\ker D\mathscr S_N=V_N^{\perp_{\rm sym}}\oplus\bigwedge^2H$; $D\mathscr S_N=B_NP_N^{\rm vis}$ | §5 (5.5)–(5.6), App. D | abstract theorem: a linear map out of a finite-dim inner-product space, given as a sum of representative-indexed functionals, factors through orthogonal projection onto the span of its representatives, injectively | finite-dim inner product space theory (mathlib) | `TARGET_LOGICAL_INTERFACE` |
| Quotient identification $\mathcal X/\ker D\mathscr S_N\simeq V_N$ | §5 (5.7)–(5.9) | same abstract theorem, quotient form | mathlib `Submodule.quotient`, orthogonal complement | `TARGET_LOGICAL_INTERFACE` |
| Strict nesting $V_N\subsetneq V_{N+1}$ | App. D (D.10)–(D.12), Cor. E | abstract witness-based strict-inclusion theorem + explicit instantiation of the witness in the $E_N$/edge-Laplacian model | finite-dim subspace lattice | `TARGET_FULL_PROOF` for the abstract witness theorem; instantiation against the true $P_{N-1}$ filtration is `OUT_OF_SCOPE_ANALYTIC` (needs the polynomial space, see above) |
| Density $\overline{\bigcup_N V_N}=\mathcal X_{\rm sym}$ | App. D (D.14)–(D.15) | — | density of polynomials in $L^2([0,1])$ | `OUT_OF_SCOPE_ANALYTIC` |
| Theorem F: conditional-variance identity $\Delta_N=\mathbb E[\operatorname{Var}(\cdot\mid[P_{\Pi_N}])]$ | §6 (6.15), App. E (E.10) | — | random permutations, conditional expectation on a finite probability space | `OUT_OF_SCOPE_ANALYTIC` (attempt only if cheap; see below) |
| Theorem F: positivity/data-processing $0\le\widehat F_N\le I$ | §6 (6.3) | possible abstract fact: data-processing inequality for conditional-expectation-type positive operators | — | `TARGET_LOGICAL_INTERFACE` if it falls out cheaply from the abstract Cor. D interface; otherwise `OUT_OF_SCOPE_ANALYTIC` |
| Theorem F: support projection $\ne$ Fisher operator ($\widehat F_N\ne P_N^{\rm vis}$) | §6 (6.4) | — | needs the actual $F_2=2/9\cdot(\cdot)$ instance | `TARGET_EXACT_CHECK` via the $N=2$ spectrum below |
| Theorem F: exact spectra $N=2,3,4$ | §6 (6.6)–(6.13), App. F | exact rational/determinant identities | pure finite arithmetic | `TARGET_EXACT_CHECK` |
| Theorem F: asymptotic retention $I_N^\Pi(f)/N\to4\|f\|^2$, $\Delta_N(f)/N\to0$ | §6 (6.16)–(6.17), App. E | — | Bernstein–Durrmeyer eigenfunctions, 4th-moment permutation identity, order statistics | `OUT_OF_SCOPE_ANALYTIC` |
| Theorem F: $\widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym}$, not in operator norm | §6 (6.20), (6.26) | abstract fact: pointwise convergence to $T$ + a per-$N$ unit witness with $T_Nh_N=0,\ Th_N=h_N$ $\Rightarrow \|T_N-T\|\ge1$ | finite/general normed space operator norm | `TARGET_FULL_PROOF` (abstract, self-contained; does **not** instantiate the S1 Fisher operator) |
| Theorem G: parity mechanism (even function $\Rightarrow$ vanishing derivative at 0) | §7 (7.4)–(7.6) | abstract calculus lemma for $f:\mathbb R\to V$ ($V$ a finite-dim normed space), $f$ even $\Rightarrow$ $f'(0)=0$ when differentiable | mathlib `deriv`/`HasDerivAt` | `TARGET_FULL_PROOF` |
| Theorem G: fiber inversion closure ($\Gamma_C$ closed under $\sigma\mapsto\sigma^{-1}$) | §3 (used in §7 proof) | already available if the poset bridge (row above) is built; otherwise stated as an abstract closure hypothesis | — | tied to poset bridge status |
| Uniform-deletion kernel: well-defined, non-negative, rows sum to 1, $\varepsilon$-independent by construction | App. G (G.13)–(G.14) | `DeletionKernel` abstract structure over `Fin`-indexed finite classes | finite combinatorics | `TARGET_FULL_PROOF` |
| Projective consistency $\mu_{m-1}(\varepsilon)=K_{m,m-1}\mu_m(\varepsilon)$ composed to $K_{N\to2}$ | §7 (7.13)–(7.14), App. G (G.16)–(G.17) | composition of linear maps | linear algebra | `TARGET_FULL_PROOF` (as an abstract composition fact; the *specific* iid-deletion derivation of each $\mu_{m-1}=K\mu_m$ step is a probability fact, taken as a hypothesis) |
| Jet propagation $\mu_2''(0)=K_{N\to2}\mu_N''(0)$, hence $\mu_2''(0)\ne0\Rightarrow\mu_N''(0)\ne0$ | App. G (G.18) | abstract: for a linear map $K$ and vector $v$, $Kv\ne0\Rightarrow v\ne0$ (contrapositive of linearity), applied to $v=\mu_N''(0)$ | linearity of differentiation composed with a constant linear map | `TARGET_FULL_PROOF` |
| Corollary H closure: parity + $N{=}2$ non-vanishing + propagation $\Rightarrow r_N(\gamma_\psi)=2$ | App. G (G.19), §7 (7.16) | packaging theorem naming exactly the required hypotheses | all of the above | `TARGET_FULL_PROOF` (abstract packaging; the concrete $\mu_2''\ne0$ input is taken as a hypothesis unless the exact-check below is completed) |
| $N=2$ second derivatives $\mu_2''(\text{antichain})=8/5$, $\mu_2''(\text{chain})=-8/5$ from the moment identities (G.9)–(G.12) | App. G (G.9)–(G.12) | arithmetic derivation from the stated moment values $A_{jk}, M_i(jk)$ taken as hypotheses | pure arithmetic (rationals with $\sqrt{15}$ cancelling) | `TARGET_EXACT_CHECK`, labelled `N2_ALGEBRA_FROM_MOMENTS_FORMALIZED`; the polynomial-integral derivation of the moments themselves is `OUT_OF_SCOPE_ANALYTIC` (`N2_INTEGRAL_FORMALIZED` not attempted) |

## Reading this table

Every `TARGET_FULL_PROOF` and `TARGET_EXACT_CHECK` row is either fully closed with
no `sorry`/`axiom`, or downgraded in `FORMALIZATION_STATUS.md` with an explicit
`POTENTIAL_PAPER_LOGIC_GAP` note if something genuinely does not go through. Every
`TARGET_LOGICAL_INTERFACE` row produces a theorem whose *hypotheses* are exactly the
un-formalized analytic facts (type B in the task's A/B/C split); it is never reported
as having certified the S1 instance itself. Every `OUT_OF_SCOPE_ANALYTIC` row is
absent from Lean entirely (type C).
