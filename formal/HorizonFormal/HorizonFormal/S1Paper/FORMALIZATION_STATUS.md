# S1 Paper — Lean 4 formalization status

Source of truth for the mathematical claims:
`research_program/synthesis/wp6_s1_finite_causal_order_manuscript.tex` (HEAD
`2bd82cd719896bf9e2a3974eef6d8fe1e00dd4b7`), consulted against
`research_program/synthesis/wp6_s1_finite_causal_order_paper_outline.md` for proof
detail where the `.tex` compresses a step. Lean 4.31.0 / mathlib pinned at `v4.31.0`
(`formal/HorizonFormal/lean-toolchain`, `lakefile.toml`), unmodified.

Every theorem below was checked with `#print axioms` and depends **only** on
`propext`, `Classical.choice`, `Quot.sound` — the three standard axioms every mathlib
proof uses. No `sorry`, `admit`, `postulate`, or project-introduced `axiom` appears
anywhere in `formal/HorizonFormal/HorizonFormal/S1Paper/*.lean` (verified by
`grep -RInE '\bsorry\b|\badmit\b|\baxiom\b|\bsorryAx\b|\bpostulate\b'`, whose only hit
is the textual mention of that rule inside `ClaimMap.md`).

Status vocabulary (as specified): `LEAN_PROVED`, `LEAN_PROVED_ABSTRACT_INTERFACE`,
`LEAN_EXACT_CHECK`, `PARTIAL`, `NOT_FORMALIZED`.

## Theorem C — the class-sum span theorem (§4, Appendix B, Appendix C)

| CLAIM | LEAN THEOREM | STATUS | ASSUMPTIONS | WHAT LEAN CERTIFIES | WHAT LEAN DOES NOT CERTIFY |
|---|---|---|---|---|---|
| `E_N = \mathbf1^\perp`, `\dim E_N = N-1` | `EN`, `finrank_EN` (`FiniteLinearAlgebra.lean`) | `LEAN_PROVED` | `N ≥ 1` | `EN N` is exactly the kernel of the coordinate-sum functional on `Fin N → ℝ`, and its dimension is `N - 1`, for every `N`. | Nothing withheld — this is the full claim. |
| `\operatorname{Sym}(E_N)` as doubly-centered symmetric matrices | `DCSymM` | `LEAN_PROVED` (definition + submodule laws) | — | `DCSymM N` (symmetric `N×N` matrices with vanishing row sums) is a genuine `ℝ`-submodule of `Matrix (Fin N) (Fin N) ℝ`, matching Appendix B's `\widetilde M` construction. | That this is *isomorphic* to `\operatorname{Sym}^2 P_{N-1}` inside `H` — that isomorphism (`\mathfrak T_N`/`\Lambda_N`, Appendix B (B.4)–(B.5)) is not built; see the `OUT_OF_SCOPE_ANALYTIC` row below. |
| Edge Laplacians `L_{ij}` are linearly independent and span `\operatorname{Sym}(E_N)` | `edgeLaplacian_linearIndependent`, `DCSymM_eq_sum_edgeLaplacian` | `LEAN_PROVED` | `N ≥ 1` (uses `i < j` pairs, vacuous for `N ≤ 1`) | For every `N`, `\{L_{ij} : i<j\}` (`\binom N2` matrices) is linearly independent **and** spans `DCSymM N` exactly, via an *explicit reconstruction formula* `M = \sum_{i<j}(-M_{ij})\bullet L_{ij}` for every `M \in \operatorname{DCSymM} N` — a direct, complete route to Appendix C's target span `\operatorname{span}\{A_C\vert_{E_N}\} = \operatorname{Sym}(E_N)`, bypassing the paper's own interval-cycle/identity-recovery argument (see next row). | **This is not yet the paper's theorem.** `L_{ij}` is a general edge Laplacian, not necessarily a near-chain-poset class sum `A_{C_{a,b}}`. See `CLASS_SUM_TO_POSET_BRIDGE` below — the bridge from this fact to the paper's actual claim is **not formalized**. |
| Identity recovery `1 - 2s_N = \frac{(N-3)^2+2}{6} > 0` (App. C (C.18)–(C.20)) | `sN`, `one_sub_two_sN_eq`, `one_sub_two_sN_pos` | `LEAN_PROVED` | none (holds for *every* `N : ℕ`, not just `N ≥ 2`) | The exact algebraic identity and its strict positivity, proved as a genuine `∀ N` statement (`ring` + `positivity`), not a finite check. This is the specific target requested and is **not** used by the `DCSymM_eq_sum_edgeLaplacian` route above (that route sidesteps the need for it); it stands as an independently certified fact matching the paper's own argument shape. | That `s_N` as defined here is *the* coefficient sum arising from the paper's specific `L`-to-`Q` triangular substitution (C.13)–(C.17) — that derivation (which combinatorial coefficients `c_{a,b}` sum to `s_N`) is not formalized; `sN` is simply defined by the paper's closed form `(N-1)(5-N)/12`. |
| `S_{a,b}` *is* (up to nonzero scalar) the class sum `A_{C_{a,b}}` of the near-chain poset family, and `\operatorname{span}\{A_C\vert_{E_N}:C\in\mathcal C_N\}=\operatorname{Sym}(E_N)` for the *actual* poset classes | — | `NOT_FORMALIZED` (`CLASS_SUM_TO_POSET_BRIDGE`) | — | Nothing. | This is the genuine formal boundary of this pass: no `PartialOrder` instance for the near-chain family `C_{a,b}` is constructed, no isomorphism-class quotient `[P_\sigma]` or fiber `\Gamma_C=\{\sigma : [P_\sigma]=C\}` is built, and the fact `\Gamma_{C_{a,b}}=\{\tau_{a,b},\tau_{a,b}^{-1}\}` (Appendix C (C.1)–(C.5)) is not proved. **Per the task's own instruction, this is reported honestly rather than papered over: `THEOREM_C_LEAN=PARTIAL`, not `LEAN_PROVED`.** |
| `V_N = \operatorname{Sym}^2 P_{N-1}` transported from the `E_N` reduction | — | `OUT_OF_SCOPE_ANALYTIC` | — | — | Needs the shifted-Legendre/Bernstein polynomial Hilbert space `H = L^2_0([0,1])`; not attempted. |

**`THEOREM_C_LEAN = PARTIAL`.** The pure finite-linear-algebra core (independence,
explicit spanning, identity-recovery non-vanishing) is fully and honestly certified —
this is a real, non-trivial, complete piece of mathematics with zero gaps in what it
claims. What is **not** certified is that the specific matrices spanning
`\operatorname{Sym}(E_N)` are the paper's actual poset class sums. This was judged, in
advance, to be the single most expensive remaining step (needs poset theory, `S_N`-orbit
combinatorics, and the near-chain family's realizer uniqueness argument) and was left as
an explicit, reported boundary rather than forced through or quietly assumed.

## Corollary D — kernel, factorization, quotient (§5, Appendix D)

| CLAIM | LEAN THEOREM | STATUS | ASSUMPTIONS | WHAT LEAN CERTIFIES | WHAT LEAN DOES NOT CERTIFY |
|---|---|---|---|---|---|
| `\ker D\mathscr S_N = V_N^{\perp_{\rm sym}}\oplus\bigwedge^2H`; `D\mathscr S_N = B_NP_N^{\rm vis}`; `B_N` injective on `V_N` | `ScoreData.ker_D_eq_orthogonal`, `ScoreData.D_eq_D_starProjection`, `ScoreData.injOn_D_V` (`AbstractQuotient.lean`) | `LEAN_PROVED_ABSTRACT_INTERFACE` | `𝒳` a finite-dimensional real inner-product space; `R : 𝒞 → 𝒳` (finite index `𝒞`); weights `w : 𝒞 → ℝ` all strictly positive | The **general** Hilbert-space fact: for `D f (C) := ⟪f,R(C)⟫/w(C)`, `\ker D` is exactly `(\operatorname{span}(\operatorname{range} R))^\perp`, `D` factors through the orthogonal `starProjection` onto `V:=\operatorname{span}(\operatorname{range} R)`, and `D` is injective on `V`. This is precisely the abstract shape the paper's §5/Appendix D argument needs. | That `𝒳 = H\widehat\otimes H` (infinite-dimensional — the finite-dimensionality hypothesis here is genuinely stronger than the paper's setting, though harmless since `V_N` itself is finite-dimensional), `𝒞 = \mathcal C_N`, `R = R_C^{(N)}`, `w = \mu_{N,0}` for the actual S1 construction. The S1 *instance* of this interface is not built (needs the `\mathcal C_N`/`R_C^{(N)}` objects, themselves downstream of the un-formalized poset bridge). |

## Strict nesting (Appendix D (D.10)–(D.12), Corollary E)

| CLAIM | LEAN THEOREM | STATUS | ASSUMPTIONS | WHAT LEAN CERTIFIES | WHAT LEAN DOES NOT CERTIFY |
|---|---|---|---|---|---|
| `V_N\subsetneq V_{N+1}` | `strict_nesting_of_witness` (`Nesting.lean`) | `PARTIAL` | `V ≤ W` submodules of a common module; a witness `w \in W\setminus V` | The abstract logical shape: an inclusion plus an explicit witness in the difference gives a *strict* inclusion (not merely a dimension comparison). | The S1 instantiation — producing the actual witness `p_1\odot p_N \in V_{N+1}\setminus V_N` — needs the polynomial space `P_{N-1}\subset P_N`; not built (`OUT_OF_SCOPE_ANALYTIC`, consistent with `ClaimMap.md`). |
| Density `\overline{\bigcup_N V_N}=\mathcal X_{\rm sym}` | — | `NOT_FORMALIZED` | — | — | Needs density of polynomials in `L^2([0,1])`; not attempted. |

## Theorem F — Fisher resolution (§6, Appendix E, Appendix F)

| CLAIM | LEAN THEOREM | STATUS | ASSUMPTIONS | WHAT LEAN CERTIFIES | WHAT LEAN DOES NOT CERTIFY |
|---|---|---|---|---|---|
| Conditional-variance identity, data processing, asymptotic retention `I_N^\Pi(f)/N\to4\|f\|^2` etc. | — | `NOT_FORMALIZED` (`THEOREM_F_ASYMPTOTIC`) | — | — | Needs order-statistic theory, the Bernstein–Durrmeyer eigenfunction computation, a 4th-moment permutation identity, and QMD machinery — a disproportionate new-theory build for this pass, exactly the boundary Phase VII anticipates. This is a scope decision, not a defect found in the paper. |
| `\widehat F_N\ne P_N^{\rm vis}` — support projection is not the Fisher operator | via `N2_Fisher_spectrum` (below): `2/9 \ne 1` | `LEAN_EXACT_CHECK` | — | The `N=2` instance is exact and nonzero-but-not-identity, exhibiting the phenomenon concretely. | Not a general-`N` argument (the paper doesn't need one for this qualitative point either). |
| `\widehat F_N\xrightarrow{\rm SOT}\Pi_{\rm sym}` is **not** operator-norm convergence, via a unit-vector witness (manuscript (6.26)) | `one_le_opNorm_of_witness` (`NormVsSOT.lean`) | `LEAN_PROVED_ABSTRACT_INTERFACE` | `T : E \to L[\mathbb R] E` bounded; unit vector `h` with `\|Th\|=1` | The exact abstract mechanism: a per-index unit-norm witness forces operator norm `\ge 1`, regardless of pointwise/SOT convergence elsewhere. This is precisely why SOT convergence in (6.20) does not contradict `\|\widehat F_N-\Pi_{\rm sym}\|\ge1` in (6.26). | The S1 witness `h_N=p_N\otimes p_N/\|p_N\|_{L^2}^2` and the operator `\widehat F_N-\Pi_{\rm sym}` itself are not constructed (needs the polynomial Hilbert space). |
| Exact `N=2,3,4` Fisher spectra | `N2_Fisher_spectrum`, `N3_Fisher_spectrum`, `N4_pure_eigenvalues`, `N4_cubic_determinant`, `N4_cubic_factor_ne_zero` (`ExactChecks.lean`) | `LEAN_EXACT_CHECK` | — | `\{2/9\}`; `\{3/8,3/40,3/200\}`; the three isolated `N=4` eigenvalues `12/25, 4/25, 4/525`; and the full `N=4` mixed-block characteristic determinant as a *polynomial identity in `\lambda`*, matching `144703125\lambda^3-9975000\lambda^2+142000\lambda-128` up to an exhibited, verified-nonzero rational factor — exactly the paper's "up to a nonzero rational factor" qualifier, made exact and machine-checked (`ring`). | The decreasing numerical ordering (6.13), since the manuscript gives the cubic's three roots only as decimal truncations with no closed form to check against exactly (reported, not silently dropped). |

## Theorem G / Corollary H — second-order detectability (§7, Appendix G)

| CLAIM | LEAN THEOREM | STATUS | ASSUMPTIONS | WHAT LEAN CERTIFIES | WHAT LEAN DOES NOT CERTIFY |
|---|---|---|---|---|---|
| Parity: even law ⟹ vanishing first derivative | `even_hasDerivAt_zero` (`Parity.lean`) | `LEAN_PROVED` | `v:\mathbb R\to(\iota\to\mathbb R)` even, differentiable at `0` | For a curve into a finite-dimensional real vector space, evenness forces the derivative at `0` to vanish — the exact abstract content of (7.4)–(7.6). | The S1 instantiation (`v = \mu_{N,\cdot}^{[P]}`, evenness from the coordinate-swap isometry `\iota`) is not built; the *mechanism* is fully certified abstractly. |
| Uniform-deletion kernel: non-negative, rows sum to 1, `\varepsilon`-independent by construction | `DeletionKernel` structure, `.nonneg`, `.rowSum_eq_one` (`DeletionKernel.lean`) | `LEAN_PROVED` (as an interface) | — | The combinatorial shape (G.13)–(G.14) exactly. | The construction of an actual `DeletionKernel` from `K_{m,m-1}(C,D)=\frac1m\#\{v\in C:[C\setminus\{v\}]=D\}` on real poset classes — needs the same poset infrastructure as the Theorem C bridge; not built. |
| Projective consistency, composition to `K_{N\to2}` | `DeletionKernel.comp`, `pushforward_comp` | `LEAN_PROVED` | — | Composing pushforwards along two kernels equals pushing forward along the composed kernel — exactly (G.16)–(G.17)'s logical content, and by iteration the full `K_{N\to2}` chain. | The *specific* probabilistic derivation that `\mu_{m-1}(\varepsilon)=K_{m,m-1}\mu_m(\varepsilon)` for the real iid-deletion mechanism (App. G, "Deletion of an iid point") — taken as a hypothesis (an instance of a `DeletionKernel`), not re-derived from probability theory. |
| Jet propagation `\mu_2''(0)=K_{N\to2}\mu_N''(0)`, hence `\mu_2''(0)\ne0\Rightarrow\mu_N''(0)\ne0` | `DeletionKernel.hasDerivAtPi_pushforward`, `.second_deriv_pushforward`, `.pushforward_ne_zero_of_ne_zero` (`JetPropagation.lean`) | `LEAN_PROVED` | Componentwise (`HasDerivAtPi`) first/second derivatives of the curve `v` | The derivative of a pushforward-by-a-fixed-linear-kernel curve is the pushforward of the derivative (twice, for the second derivative), and the exact logical implication `\mu_2''(0)\ne0\Rightarrow\mu_N''(0)\ne0` as the contrapositive of linearity (`K\cdot 0=0`). This is the precise "exact logical implication" the task asked to isolate. | The differentiability of `\mu_N^{[P]}` itself (taken as a hypothesis, matching the paper's own appeal to real-analyticity in Appendix G (G.3)). |
| Corollary H, exactly what hypotheses are needed | `corollaryH` (`CorollaryH.lean`) | `LEAN_PROVED` (packaging) | Evenness of `v`; componentwise first/second derivatives of `v` exist; a `DeletionKernel` `κ`; `κ`'s pushforward of the second derivative is nonzero | Combines parity + jet propagation into one theorem concluding `FirstZeroSecondNonzero v' v₂` (`v'=0 \wedge v_2\ne0`) — the paper's `r_N(\gamma_\psi)=2` made precise, with every needed hypothesis named explicitly (nothing hidden behind an equivalent-looking but circular assumption). | The concrete `\mu_2''\ne0` fact for the specific S1 witness `\psi` — supplied only as a hypothesis here; see the exact-check row below for its independent algebraic verification. |
| `N=2` second derivatives `\mu_2''(\text{antichain})=8/5`, `\mu_2''(\text{chain})=-8/5`, from the stated moments | `N2_moment_squares`, `N2_second_derivatives`, `N2_second_derivative_sum_zero` (`ExactChecks.lean`) | `LEAN_EXACT_CHECK` — specifically `N2_ALGEBRA_FROM_MOMENTS_FORMALIZED` | The moment values `A_{12}A_{21}=-1/15`, `A_{12}^2=A_{21}^2=1/15`, `M_1(12)M_2(12)=-4/15`, `M_1(12)^2=M_2(12)^2=4/15` (Appendix G (G.9)–(G.10)), taken as hypotheses | The *algebra* from the stated moments to the stated second derivatives, exactly reproducing (G.11)–(G.12), plus the consistency check `\sum_C\mu_2''(C)=0`. | `N2_INTEGRAL_FORMALIZED` is **not** done: the polynomial-integral computation that produces the moment values themselves (direct integration against the order-statistic densities, App. G before (G.9)) is not formalized. The two are kept explicitly distinct, per the task's instruction never to let one stand in for the other. |

## Global result

```text
LEAN_CORE_CERTIFICATION = PARTIAL
```

**Why not `PASS`.** The task's five simultaneous conditions for `PASS` are: (1) Theorem
C formalized *including* the class-sum-to-poset bridge; (2) Corollary D's logical core;
(3) nesting; (4) the deletion/propagation logic of Corollary H; (5) no `sorry`/axioms,
all modules compiling. Conditions (2)–(5) are met. Condition (1) is **not**: the
finite-linear-algebra span/independence/identity-recovery core of Theorem C is fully
certified, but the bridge connecting those matrices to actual poset class sums
`A_{C_{a,b}}` is not built. This was a deliberate, reported scope decision (flagged in
`ClaimMap.md` before any proof was attempted, not discovered after the fact and
rationalized), matching the task's own explicit instruction for exactly this outcome.

**What this pass is confident about, as a result of the adversarial exercise.** No
mathematical inconsistency was found between the paper and what Lean can certify. Every
genuinely finite, algebraic, or purely-logical claim examined — the edge-Laplacian
basis of `\operatorname{Sym}(E_N)`, the identity-recovery non-vanishing for *every* `N`,
the abstract kernel/quotient/injectivity package, the parity mechanism, the
deletion-kernel projective-consistency and jet-propagation logic, the `N{=}2,3,4` exact
arithmetic (including the full `N{=}4` characteristic-determinant polynomial identity)
— checked out exactly as stated, with no hidden hypothesis needed beyond what the
manuscript already states or transparently uses (e.g. real-analyticity for the second
derivative to be meaningful, already invoked in Appendix G (G.3)). No
`POTENTIAL_PAPER_LOGIC_GAP` was found.

## Explicit hypotheses surfaced by this exercise (type B, per the task's A/B/C split)

These are genuine mathematical facts the paper's argument needs, correctly identified
as inputs rather than re-derived, and never presented as Lean-proved:

1. The differentiability-in-a-neighborhood needed to speak of a *second* derivative at
   `0` (`CorollaryH.corollaryH`'s `hv₁` hypothesis) — matches the paper's own appeal to
   real-analyticity (Appendix G (G.3)), not an extra assumption beyond the paper.
2. The specific probabilistic fact that uniform deletion from an iid sample gives an iid
   subsample (App. G, "Deletion of an iid point") — taken as the defining property of a
   `DeletionKernel` instance, not re-derived from probability theory.
3. The moment values `A_{12}, A_{21}, M_1(12), M_2(12)` (Appendix G (G.9)–(G.10)) —
   taken as hypotheses in `N2_moment_squares`; their polynomial-integral derivation is
   `N2_INTEGRAL_FORMALIZED = NOT_FORMALIZED`.

None of these is a gap *in the paper* — each is a fact the manuscript itself states or
uses transparently. They are recorded here because the task requires every
not-independently-verified hypothesis to be named, not because they cast doubt on the
paper.
