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

**Second pass (2026-09-04).** Four further modules — `PermutationPoset.lean`,
`AlmostChain.lean`, `Fiber.lean`, `ClassSum.lean` — close what the first pass reported
as its one genuine formal boundary, `CLASS_SUM_TO_POSET_BRIDGE`. Its rows are marked
below. As an independent guard against a *mis-modelled* statement (a formalization that
compiles but states something weaker or different from Appendix C), the fiber lemma is
additionally cross-checked by brute-force enumeration over all of `S_N` for `N = 2..6`
in `fiber_bruteforce_check.py`, which recomputes the fiber from the raw definitions and
compares it against `{τ, τ⁻¹}`; it passes for all `binom N 2` pairs at every one of
those `N`. That script is evidence about the *statement*, never about the proof — the
proof is the Lean term, checked by the kernel for all `N` at once. A
**third pass** then closed the matrix half of Appendix C; it is recorded in its own
section at the end of this file (`## Third pass — matrix closure of Theorem C`), which
supersedes two specific rows/verdicts of the earlier sections. The earlier sections are
left exactly as they were written — they are the record of what those passes concluded,
not a description of the present state.

## Theorem C — the class-sum span theorem (§4, Appendix B, Appendix C)

| CLAIM | LEAN THEOREM | STATUS | ASSUMPTIONS | WHAT LEAN CERTIFIES | WHAT LEAN DOES NOT CERTIFY |
|---|---|---|---|---|---|
| `E_N = \mathbf1^\perp`, `\dim E_N = N-1` | `EN`, `finrank_EN` (`FiniteLinearAlgebra.lean`) | `LEAN_PROVED` | `N ≥ 1` | `EN N` is exactly the kernel of the coordinate-sum functional on `Fin N → ℝ`, and its dimension is `N - 1`, for every `N`. | Nothing withheld — this is the full claim. |
| `\operatorname{Sym}(E_N)` as doubly-centered symmetric matrices | `DCSymM` | `LEAN_PROVED` (definition + submodule laws) | — | `DCSymM N` (symmetric `N×N` matrices with vanishing row sums) is a genuine `ℝ`-submodule of `Matrix (Fin N) (Fin N) ℝ`, matching Appendix B's `\widetilde M` construction. | That this is *isomorphic* to `\operatorname{Sym}^2 P_{N-1}` inside `H` — that isomorphism (`\mathfrak T_N`/`\Lambda_N`, Appendix B (B.4)–(B.5)) is not built; see the `OUT_OF_SCOPE_ANALYTIC` row below. |
| Edge Laplacians `L_{ij}` are linearly independent and span `\operatorname{Sym}(E_N)` | `edgeLaplacian_linearIndependent`, `DCSymM_eq_sum_edgeLaplacian` | `LEAN_PROVED` | `N ≥ 1` (uses `i < j` pairs, vacuous for `N ≤ 1`) | For every `N`, `\{L_{ij} : i<j\}` (`\binom N2` matrices) is linearly independent **and** spans `DCSymM N` exactly, via an *explicit reconstruction formula* `M = \sum_{i<j}(-M_{ij})\bullet L_{ij}` for every `M \in \operatorname{DCSymM} N` — a direct, complete route to Appendix C's target span `\operatorname{span}\{A_C\vert_{E_N}\} = \operatorname{Sym}(E_N)`, bypassing the paper's own interval-cycle/identity-recovery argument (see next row). | **This is not by itself the paper's theorem.** `L_{ij}` is a general edge Laplacian, not a near-chain-poset class sum `A_{C_{a,b}}`. The poset side of that connection is now proved (rows below); what is still missing is the matrix chain (C.12)–(C.19) that expresses one family through the other — see `APPENDIX_C_MATRIX_HALF` below. |
| Identity recovery `1 - 2s_N = \frac{(N-3)^2+2}{6} > 0` (App. C (C.18)–(C.20)) | `sN`, `one_sub_two_sN_eq`, `one_sub_two_sN_pos` | `LEAN_PROVED` | none (holds for *every* `N : ℕ`, not just `N ≥ 2`) | The exact algebraic identity and its strict positivity, proved as a genuine `∀ N` statement (`ring` + `positivity`), not a finite check. This is the specific target requested and is **not** used by the `DCSymM_eq_sum_edgeLaplacian` route above (that route sidesteps the need for it); it stands as an independently certified fact matching the paper's own argument shape. | That `s_N` as defined here is *the* coefficient sum arising from the paper's specific `L`-to-`Q` triangular substitution (C.13)–(C.17) — that derivation (which combinatorial coefficients `c_{a,b}` sum to `s_N`) is not formalized; `sN` is simply defined by the paper's closed form `(N-1)(5-N)/12`. |
| `P_\sigma` is a genuine poset; `[P_\sigma]` as an unlabeled isomorphism class; fibers closed under inversion | `leSigma_refl/_trans/_antisymm`, `PosetIsomorphic` (+`_refl/_symm/_trans`), `posetIso_inv`, `posetIsomorphic_inv` (`PermutationPoset.lean`) | `LEAN_PROVED` | — | The three order laws of `i \preceq_\sigma j \iff i\le j \wedge \sigma i\le\sigma j`, proved from the definition; `[P_\sigma]=[P_\tau]` modelled as an explicit order-isomorphism (a bijection carrying one relation to the other, *not* a labeled equality); and §3's closure `\sigma\in\Gamma_C\iff\sigma^{-1}\in\Gamma_C` as a real isomorphism witness `i\mapsto\sigma(i)`. Both relations are `Decidable`, so `\Gamma_C` is an honest `Finset`, not a choice artefact. | The bundled mathlib `PartialOrder (Fin N)` *instance* is deliberately not registered (one canonical order per type; different `\sigma` would need different instances). Nothing downstream uses the bundled form. |
| `\tau_{a,b}` is a permutation; self-inverse exactly in the adjacent case | `tau`, `tau_val`, `tau_self_inv_of_adjacent`, `tau_ne_inv_of_not_adjacent` (`AlmostChain.lean`) | `LEAN_PROVED` | `a<b` | The interval cycle is built as a genuine `Equiv.Perm (Fin N)` (injectivity proved, not assumed), with a closed value formula; and the manuscript's parenthetical "when `b=a+1` the two displayed permutations coincide" is proved in **both** directions — `\tau=\tau^{-1}` iff `b=a+1`. | Nothing withheld. |
| **Every linear extension of `C_{a,b}` inserts `z` after exactly `k\in\{a,\ldots,b\}` chain elements** (Appendix C, the sentence before (C.3)) | `IsExtension`, `extension_val`, `extension_eq_tau`, `extension_eq_one` (`Fiber.lean`) | `LEAN_PROVED` | `a<b` | The full classification: for *every* extension `\pi` of `P_{\tau_{a,b}}`, `k:=\pi(b)` satisfies `a\le k\le b` and `\pi` is then determined pointwise by the closed formula (`\pi=L_k`); in particular `L_a=\tau_{a,b}` and `L_b=\mathrm{id}`. Proved by a counting argument, not asserted. The manuscript states this in one line without proof. | Nothing withheld for this statement. |
| **`\Gamma_{C_{a,b}}=\{\tau_{a,b},\tau_{a,b}^{-1}\}` (C.5)** | `fiber_eq` (`Fiber.lean`), `fiber_almostChain` (`ClassSum.lean`) | `LEAN_PROVED` | `a<b` | The fiber lemma itself, as an **iff** (both inclusions), for every `N` and every `a<b`, following the manuscript's own realizer route: an isomorphism `e:P_\sigma\cong P_\tau` pushes the natural order and the `\sigma`-order forward to two extensions of `P_\tau` whose intersection is `P_\tau`, the two incomparabilities `a\parallel b` and `b-1\parallel b` force `\{k_1,k_2\}=\{a,b\}`, and `\sigma=\pi_2\pi_1^{-1}\in\{\tau,\tau^{-1}\}`. Also given as a `Finset` identity, so the class sum can be computed. | The identification of `[P_{\tau_{a,b}}]` with the manuscript's *abstract presentation* (C.1)–(C.2) (chain `c_1<\cdots<c_{N-1}` plus `z`) is a presentation choice, not a separately proved lemma: the Lean class is defined as the isomorphism class of `P_{\tau_{a,b}}`. The two agree by inspection (the incomparable pairs of `P_{\tau_{a,b}}` are exactly `(i,b)`, `a\le i<b`), and that fact is used inside the proof, but it is not stated as its own theorem. |
| **`S_{a,b}=2A_{C_{a,b}}` (`b=a+1`), `=A_{C_{a,b}}` (`b>a+1`) — (C.11)** | `permM`, `permM_transpose`, `classSum`, `Sab`, `Sab_eq_two_classSum`, `Sab_eq_classSum`, `Sab_nonzero_smul_classSum`, `span_Sab_eq_span_classSum` (`ClassSum.lean`) | `LEAN_PROVED` | `a<b` | Exactly (C.11), in the manuscript's own matrix convention (3.12) `P_\sigma=\sum_ie_ie_{\sigma(i)}^\top`, including `P_\sigma^\top=P_{\sigma^{-1}}` (3.8), the "nonzero scalar either way" statement, and its span consequence. **The matrices Appendix C manipulates are certified to be nonzero multiples of the class sums of genuine unlabeled two-dimensional poset classes.** | — |
| The `\binom N2` classes `C_{a,b}` are pairwise distinct (conclusion of (C.6)) | `tau_ne_self_iff`, `almostChain_pair_eq_of_isomorphic` (`Fiber.lean`) | `LEAN_PROVED` | `a<b`, `a'<b'` | Distinct pairs give non-isomorphic classes, so the family really supplies `\binom N2` distinct classes. | Proved by a **different route** than the manuscript's: via the non-fixed set of `\tau_{a,b}` being the interval `[a,b]` (invariant under inversion), not via the strict-past-cardinality multiset of (C.6). The multiset computation (C.6) itself is not formalized. |
| `\operatorname{span}\{A_C\vert_{E_N}:C\in\mathcal C_N\}=\operatorname{Sym}(E_N)` — the span statement itself | — | `NOT_FORMALIZED` (`APPENDIX_C_MATRIX_HALF`) | — | Nothing. | **This is now the genuine remaining boundary of Theorem C.** What is missing is no longer the poset side but the *matrix* side of Appendix C: (a) `Q_{a,b}:=2I_{E_N}-S_{a,b}\vert_{E_N}` is the cycle's graph Laplacian and the triangular identities (C.13)–(C.14) with their inversion (C.15); (b) the identity-recovery step (C.17)–(C.19), i.e. that the coefficients `c_{a,b}` of (C.17) sum to `s_N` — only the *algebra* `1-2s_N>0` from the closed form is proved (see the row above), never the derivation that this particular sum equals `s_N`. Reported honestly: `THEOREM_C_LEAN=PARTIAL`, not `LEAN_PROVED`. |
| `V_N = \operatorname{Sym}^2 P_{N-1}` transported from the `E_N` reduction | — | `OUT_OF_SCOPE_ANALYTIC` | — | — | Needs the shifted-Legendre/Bernstein polynomial Hilbert space `H = L^2_0([0,1])`; not attempted. |

**`THEOREM_C_LEAN = PARTIAL`** — but the boundary has moved, and it is worth being
precise about where it now sits.

The pure finite-linear-algebra core (independence, explicit spanning,
identity-recovery non-vanishing) was already fully certified. What the first pass
flagged as its single most expensive missing step — `CLASS_SUM_TO_POSET_BRIDGE`, the
fact that the matrices Appendix C manipulates are the class sums of *actual* unlabeled
poset classes — is now **closed**: the poset `P_\sigma`, the unlabeled isomorphism
class, the fiber `\Gamma_C`, the near-chain family `\tau_{a,b}`, the classification of
linear extensions, the fiber lemma (C.5), the class-sum identity (C.11), and the
pairwise distinctness of the `\binom N2` classes are all proved, with no `sorry` and
only the three standard axioms.

`CLASS_SUM_TO_POSET_BRIDGE = LEAN_PROVED`.

What is still **not** certified is the *matrix half* of Appendix C: the cycle-Laplacian
identities (C.12)–(C.16) and the identity-recovery step (C.17)–(C.19) that removes the
shared `2I_{E_N}` term. Those are ordinary finite matrix computations rather than a
conceptual obstacle, but they are computations that have not been done here, so the
end-to-end span statement (4.1) remains unformalized and Theorem C stays `PARTIAL`.
The remaining transport (B.9)–(B.10) to `\operatorname{Sym}^2P_{N-1}` is separately
`OUT_OF_SCOPE_ANALYTIC`, unchanged.

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
all modules compiling. Conditions (2)–(5) are met. Condition (1) is now **partly** met:
the class-sum-to-poset bridge itself *is* built and proved (`PermutationPoset.lean`,
`AlmostChain.lean`, `Fiber.lean`, `ClassSum.lean`), which was the step flagged in
`ClaimMap.md` as the one at realistic risk of being abandoned. What still blocks (1) is
the matrix half of Appendix C — (C.12)–(C.19) — which the first pass had already
certified in an equivalent but *different* form (`DCSymM_eq_sum_edgeLaplacian` spans
`\operatorname{Sym}(E_N)` by edge Laplacians via an explicit reconstruction formula) and
which is therefore not a conceptual gap, only an unfinished bookkeeping chain between
the two certified halves. Until that chain is written the honest verdict stays `PARTIAL`.

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

---

## Third pass — matrix closure of Theorem C

Scope of this pass: Appendix C (C.12)–(C.21) only, plus the class-sum conclusion. No
other front was opened (no Theorem F, no Hilbert–Schmidt density, no Bernstein/`L²`
transport, no second order, no change to the manuscript). New modules:
`Restriction.lean`, `CycleLaplacian.lean`, `SpanTheoremC.lean`.

### What it supersedes

Two statements in the sections above are superseded and should be read against this
section instead:

1. In the Theorem C table, the row `APPENDIX_C_MATRIX_HALF = NOT_FORMALIZED` — the
   chain (C.12)–(C.21) it describes is now proved.
2. The `THEOREM_C_LEAN = PARTIAL` verdict paragraph and the `Why not PASS` paragraph of
   the Global result, insofar as they attribute the gap to the missing matrix chain.

### The `E_N` model

`Sym(E_N)` is the already-certified `DCSymM N`; restriction to `E_N` is conjugation by
the projection `cproj = I - N⁻¹J`, and `I_{E_N}` is `cproj` itself. `restr M` fixes
`DCSymM` (`restr_eq_self`) and lands in it on symmetric inputs (`restr_mem_DCSymM`), so
no information is added or lost by the model. No second notion of matrix, restriction,
class sum or permutation matrix was introduced: `DCSymM`, `edgeLaplacian`, `tau`,
`fiber`, `classSum`, `Sab` are the objects already in this directory.

| CLAIM | LEAN THEOREM | STATUS | WHAT LEAN CERTIFIES | WHAT LEAN DOES NOT CERTIFY |
|---|---|---|---|---|
| `Q_{a,b} := 2I_{E_N} - S_{a,b}\vert_{E_N}` (C.12) | `Smat`, `Qmat`, `Qmat_of_lt`, `Qmat_eq_two_one_sub_Sab` (`CycleLaplacian.lean`) | `LEAN_PROVED` | `Q` is *defined* from the `S_{a,b}` that (C.11) already ties to the real class sum — the Laplacian description is derived, never assumed. `Qmat_eq_two_one_sub_Sab` additionally shows `2I - S_{a,b}` is already in `Sym(E_N)`, so the restriction is invisible here. | — |
| `2I - (P_σ+P_σᵀ) = ∑_i L_{i,σ(i)}` (the mechanism behind (C.13)–(C.14)) | `two_smul_one_sub_permSym` | `LEAN_PROVED` | The identity for **every** permutation of `Fin N`, proved entrywise. It is strictly more general than the paper's step and is what makes the cycle decomposition fall out. | — |
| **(C.13)** `Q_{a,a+1} = 2L_{a,a+1}` | `Qmat_adjacent` | `LEAN_PROVED` | The length-two case with the unique edge counted twice, from the definition of `Q`. | — |
| **(C.14)** `Q_{a,b} = L_{a,b} + ∑_{k∈[a,b)}L_{k,k+1}` | `Qmat_eq_cycleLaplacian`, `Qmat_nonadjacent`, `pathL` | `LEAN_PROVED` | `Q_{a,b}` is the consecutive cycle's graph Laplacian, for every `a<b`. Index convention: 0-indexed `Fin N`, so the manuscript's `L_{a+1,b+1}` is `edgeLaplacian N a b`; vertex sets agree (`{a,…,b}`). | — |
| **(C.15)** triangular inversion | `wInv`, `edgeLaplacian_eq_Qcomb` | `LEAN_PROVED` | An **explicit** coefficient vector `wInv i j` with `∑_{x<y} wInv i j (x,y)·Q_{x,y} = L_{ij}`, proved algebraically from (C.13)–(C.14). One uniform formula covers both of the manuscript's cases: at `j=i+1` the long-interval term and the single adjacent term collide and give `L = ½Q`. No dimension count is used. | — |
| **(C.16)** `span{Q_{a,b}} = Sym(E_N)` | `span_QSet` | `LEAN_PROVED` | Equality of submodules, via (C.15) and the already-certified edge-Laplacian span `span_LSet` (which is (C.8)). | — |
| **(C.9)** `I_{E_N} = N⁻¹∑_{i<j}L_{ij}` | `cproj_eq_sum_edgeLaplacian` (`Restriction.lean`) | `LEAN_PROVED` | Obtained from the first pass's reconstruction theorem by reading off `cproj`'s off-diagonal entries. | — |
| **(C.17)** explicit `c_{a,b}` | `cCoef`, `cproj_eq_Qcomb_cCoef` | `LEAN_PROVED` | `c` is **constructed** — `c := N⁻¹ ∑_{i<j} wInv i j`, i.e. (C.9) with each `L_{ij}` substituted by (C.15) — and then `∑_p c_p Q_p = I_{E_N}` is proved. `c` is never obtained from an existential, and `cCoef_eq_zero_of_not_lt` shows it is supported on the pairs `a<b`, so the coefficient *sum* below counts nothing spurious. | — |
| **(C.18)** `∑_{a<b} c_{a,b} = s_N` | `coeffSum_wInv`, `pair_distance_sum`, `coeffSum_cCoef_eq_sN` | `LEAN_PROVED` | **The step that was deliberately left uncertified before.** `coeffSum_wInv` proves the manuscript's distance argument — one edge at distance `d=j-i` contributes total coefficient `1-d/2` (`1/2` at `d=1`; one long-interval term of coefficient `1` minus `d` adjacent terms of `1/2`) — and `pair_distance_sum` evaluates `∑_{i<j}(1-(j-i)/2) = N·s_N` in closed form. The first pass proved `sN` *by its closed form*; this pass proves that the sum of the coefficients actually constructed in (C.17) equals it. | — |
| **(C.19)** `(1-2s_N)I_{E_N} = -∑ c_{a,b}S_{a,b}\vert_{E_N}` | `identity_elimination` | `LEAN_PROVED` | The identity-term elimination, from (C.17) and the definition of `Q`. | — |
| **(C.20)** `1-2s_N = ((N-3)²+2)/6 > 0` | `one_sub_two_sN_pos` (first pass) | `REUSED` | Reused, not re-proved; used here only through `≠ 0`. | — |
| **(C.21)** `span{S_{a,b}\vert_{E_N}} = Sym(E_N)` | `span_SSet` | `LEAN_PROVED` | Equality of submodules. `I_{E_N}` enters the span by dividing (C.19) by the nonzero scalar of (C.20); every `Q_{a,b}` then follows, and (C.16) closes it. | — |
| **`span{A_C\vert_{E_N} : C∈𝒞_N} = Sym(E_N)`** | `span_classSum_restr_eq` | `LEAN_PROVED` | **The target of this pass**, as an equality of submodules, for every `N ≠ 0` (the manuscript states `N ≥ 2`; at `N=1` both sides are `0`). The `⊇` direction goes through the real class sums via the certified (C.11) scalar; the `⊆` direction needs `A_C` symmetric, proved as `classSum_isSymm` from the fiber's closure under inversion (manuscript (3.8)). `classSum_congr` proves `A_C` depends only on the class, so indexing by permutations is indexing by classes. No dimension count substitutes for the inclusion. | That `DCSymM N` *is* `Sym(E_N)` is the model set up in `FiniteLinearAlgebra.lean`, not a separately proved isomorphism theorem. |

### Guardrails

`appendixC_matrix_check.py` recomputes every object of this pass from the raw
definitions (`tau`, `P_σ`, `S`, `cproj`, `restr`, `Q`, `wInv`, `cCoef`) and checks
(C.13), (C.14), (C.15), (C.17), (C.18), (C.19), (C.20), (C.21) and the final class-sum
span numerically for `N = 2..6`, including that the span has rank `C(N,2)` over *all*
realized poset classes. `fiber_bruteforce_check.py` (second pass) still passes for
`N = 2..6`. **Neither script participates in any Lean proof**; they are evidence that the
formalized statements say what Appendix C says, against the risk of a formalization that
compiles while stating something weaker. The proofs are the Lean terms, kernel-checked
for all `N` at once.

`#print axioms` on `two_smul_one_sub_permSym`, `Qmat_eq_two_one_sub_Sab`,
`Qmat_eq_cycleLaplacian`, `Qmat_adjacent`, `Qmat_nonadjacent`, `edgeLaplacian_eq_Qcomb`,
`span_QSet`, `cproj_eq_Qcomb_cCoef`, `coeffSum_wInv`, `pair_distance_sum`,
`coeffSum_cCoef_eq_sN`, `identity_elimination`, `span_SSet`, `classSum_isSymm` and
`span_classSum_restr_eq` reports only `propext`, `Classical.choice`, `Quot.sound`. The
`sorry`/`admit`/`axiom` grep over `S1Paper/*.lean` is still empty. `lake build` compiles
the whole tree (4716 jobs).

### Status after this pass

```text
CLASS_SUM_TO_POSET_BRIDGE      = LEAN_PROVED   (second pass)
THEOREM_C_FINITE_MATRIX_FORM   = LEAN_PROVED   (this pass)
BERNSTEIN_TRANSPORT_TO_VN      = NOT_FORMALIZED
```

> **[RETIRED — see the fourth pass below.]** The token
> `THEOREM_C_FINITE_MATRIX_FORM` is left here as the historical record of what this pass
> concluded, but it is **no longer the operative certificate**: auditor report 037 (W-16)
> found its name broader than the theorem behind it, since the manuscript's boxed
> Theorem C also asserts `dim V_N = rank G_{[P]}^{(N)}`. It is replaced by the narrower
> tokens of the fourth pass. Read those, not this line.

**No `POTENTIAL_PAPER_LOGIC_GAP` was found.** Every step of (C.12)–(C.21) went through
with the real definitions, and the manuscript's two-case split in (C.11) and
(C.13)/(C.14) is exactly right — in Lean the adjacent case is forced, not chosen.

**What this does and does not license.** Lean now certifies the finite matrix theorem
that is the combinatorial hinge of Theorem C: the class sums of unlabeled
two-dimensional poset classes, restricted to `E_N`, span `Sym(E_N)` for every `N`. It
does **not** certify Theorem C as stated in the manuscript, which is about
`V_N = Sym²P_{N-1}`: the transport `Sym(E_N) ↔ Sym²P_{N-1}` through `Λ_N`/`𝔗_N`
(Appendix B (B.9)–(B.10)) needs the shifted-Legendre/Bernstein polynomial Hilbert space
and is still `OUT_OF_SCOPE_ANALYTIC`, as are Theorem F's asymptotics and the density
statement. The paper is not "Lean-certified"; its finite combinatorial core now is.

---

## Fourth pass — dimension and certificate-width closure

Scope: close auditor finding **W-16** of
`docs/auditor/auditor_report_037_wp6-s1-paper-and-lean-evidence.md`. No new mathematical
front; no change to the manuscript, outline or bibliography. Everything below lands in
`SpanTheoremC.lean` (no new module was needed).

W-16 said, correctly: the third pass's summary token named "the finite matrix form of
Theorem C", but the manuscript's boxed Theorem C is `V_N = Sym²P_{N-1}` **and**
`dim V_N = rank G_{[P]}^{(N)} = C(N,2)`, while Lean proved only the span equality — there
was no `finrank` theorem for `DCSymM` at all. Two things were done: the dimension was
actually proved, and the token was split so that no part of it can be read as covering
the Gram rank or the Bernstein transport.

| CLAIM | LEAN THEOREM | STATUS | WHAT LEAN CERTIFIES | WHAT LEAN DOES NOT CERTIFY |
|---|---|---|---|---|
| `#{(i,j) : i<j} = C(N,2)` | `card_pairs`, `sum_range_id_eq_choose`, `card_filter_lt_fin` | `LEAN_PROVED` | The index set of the edge Laplacians has exactly `N.choose 2` elements. | — |
| `{L_{ij}}` is a **basis** of `Sym(E_N)` | `edgeBasis` | `LEAN_PROVED` | The first pass's independence (`edgeLaplacian_linearIndependent`) and spanning (`DCSymM_eq_sum_edgeLaplacian`) assembled into an actual `Module.Basis` of `DCSymM N`. Nothing is re-derived. | — |
| `dim Sym(E_N) = C(N,2)` | `finrank_DCSymM`, `finrank_DCSymM_eq_half` | `LEAN_PROVED` | `Module.finrank ℝ (DCSymM N) = N.choose 2`, and the same in the manuscript's arithmetic form `N(N-1)/2` (via `Nat.choose_two_right`), for every `N`. | — |
| **`dim span{A_C\vert_{E_N} : C∈𝒞_N} = C(N,2)`** | `finrank_span_classSum_restr`, `finrank_span_classSum_restr_eq_half` | `LEAN_PROVED` | The dimension of the **certified class-sum span itself** — stated for `ASet N`, i.e. the real class sums of `ClassSum.lean`, not for the edge Laplacians. It is `span_classSum_restr_eq` that carries the poset content; this theorem only computes that module's dimension. Holds for every `N ≠ 0`. | — |
| `dim V_N = rank G_{[P]}^{(N)}` | — | `NOT_FORMALIZED` (`THEOREM_C_GRAM_RANK`) | Nothing. | **Deliberately not attempted.** No Lean object for the Fisher/Gram matrix `G_{[P]}^{(N)}` exists: `grep -rniE 'gram|rank G'` over `S1Paper/*.lean` returns only the two docstring lines in `SpanTheoremC.lean` that disclaim it. It follows in the ordinary paper from the span, but that inference is *not* Lean-checked and must not be reported as if it were. |

### Operative certificate (supersedes the third pass's single token)

```text
CLASS_SUM_TO_POSET_BRIDGE           = LEAN_PROVED      (second pass)
THEOREM_C_CLASS_SUM_SPAN            = LEAN_PROVED      (third pass)
THEOREM_C_CLASS_SUM_SPAN_DIMENSION  = LEAN_PROVED      (this pass)
THEOREM_C_GRAM_RANK                 = NOT_FORMALIZED
BERNSTEIN_TRANSPORT_TO_VN           = NOT_FORMALIZED
THEOREM_C_FINITE_MATRIX_FORM        = RETIRED          (too broad; replaced by the two
                                                        THEOREM_C_CLASS_SUM_SPAN* tokens)
```

**Lean certifies the finite class-sum span theorem and its dimension; it does not certify
the Bernstein transport to `V_N = Sym²P_{N-1}`, nor a separate theorem identifying the
rank of the Fisher/Gram matrix.** Consequently the ledger must not be read, at any point,
as `Theorem C as stated in the manuscript = Lean proved`.

### Checks

`lake build` PASS (4716 jobs). `#print axioms` on `card_pairs`, `edgeBasis`,
`finrank_DCSymM`, `finrank_DCSymM_eq_half`, `finrank_span_classSum_restr` and
`finrank_span_classSum_restr_eq_half` reports only `propext`, `Classical.choice`,
`Quot.sound`. The `sorry`/`admit`/`axiom` grep over `S1Paper/*.lean` is still empty. The
dimension value agrees with `appendixC_matrix_check.py`, which independently finds span
rank `C(N,2)` for `N = 2..6`; that script still participates in no Lean proof.

`ClaimMap.md` remains untouched (pre-registered planning), as do the manuscript, the
outline, the bibliography, and auditor report 037 — the report is historical evidence and
is not rewritten after the remediation it prompted.
