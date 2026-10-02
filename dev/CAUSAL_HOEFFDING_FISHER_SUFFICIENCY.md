# Causal Hoeffding Theorem — Fisher sufficiency of finite-poset U-statistics

## 1. Status

STATUS: `PROVED / DEV_EXPLORATION / NOT_COMMITTEE_REVIEWED`
SCOPE: ABSTRACT U-STATISTIC RESULT, DIMENSION-FREE, NO GEOMETRIC INPUT
RELATION_TO_PROGRAM: closes the `S_N^full → S_N^poset` bridge that the O1-3+1D audit
(2026-09-01 session) found missing; supersedes the "permutation substitute" framing of that
audit's `NEXT_SINGLE_OBLIGATION`.

This document was derived and independently audited (analytic proof + two disjoint exact
numerical checks, no Monte Carlo) in conversation on branch `emergencia/p1a-canal-sigma-m`,
HEAD `3b3a82f` at time of writing. It has **not** gone through `/comite` or `/auditor`. It
authorizes nothing beyond being a citable, re-derivable dev artifact — no threshold, no
validation run, no claim promotion.

## 2. Setting

`(D,μ)` a probability space; `X_1,…,X_N` iid `~μ`; `Y_N=[P_N]` the unlabelled causal-order
isomorphism class induced by `X_1,…,X_N`. `ψ∈L²_0(μ)` (mean zero), `S_N=cΣ_iψ(X_i)`, `c>0`
a fixed dimensional constant. For `k≥2` and `F` a bounded function of the isomorphism class
of a `k`-point induced sub-poset, define

```
φ_F(x) = E[F([P_k]) | X_1=x] - E[F([P_k])]          (first-order Hoeffding projection)
U_{N,F} = Σ_{|A|=k} F([P_A])                          (order-invariant U-statistic)
η_N(ψ)  = Var(E[S_N|Y_N]) / Var(S_N)
```

## 3. Theorem (Causal Hoeffding)

If `φ_F≠0`, then for every `N≥k`:

```
Cov(S_N,U_{N,F}) = c·N·C(N-1,k-1)·⟨ψ,φ_F⟩                                   (exact)
Var(U_{N,F})     = N·C(N-1,k-1)²·‖φ_F‖² + Σ_{j=2}^k C(N-j,k-j)²C(N,j)ζ_j    (exact, ζ_j:=Var(g_j))
```

and consequently

```
liminf_{N→∞} η_N(ψ) ≥ ⟨ψ,φ_F⟩² / (‖ψ‖²‖φ_F‖²).
```

In particular `ψ=φ_F ⟹ η_N(ψ)→1` (sandwiched with `η_N≤1`, always true by the law of total
variance). More generally, for `H_caus := closure span{φ_F : k≥2, F bounded on k-posets}`,

```
liminf_{N→∞} η_N(ψ) ≥ ‖Proj_{H_caus}ψ‖² / ‖ψ‖²          ⟹    ψ∈H_caus ⟹ η_N(ψ)→1.
```

**`c` cancels identically** — the bound is a pure squared-cosine, independent of the
conformal normalization constant.

### 3.1 Proof sketch (full derivation in session; re-derivable from §4)

1. **Exact Hoeffding decomposition.** `h_F(x_1,…,x_k)=Σ_{S⊆{1,…,k}} g_{|S|}(x_S)` via the
   canonical degenerate kernels `g_j` (`g_0=θ_F`, `g_1=φ_F`), giving the exact finite-`N`
   identity `U_{N,F}=Σ_{j=0}^k C(N-j,k-j) Σ_{|S|=j} g_j(X_S)`.
2. **Orthogonality across all distinct subsets `S≠S'` (any levels `j,j'`)** is proved by
   iterated single-argument degeneracy + Fubini (not merely asserted): for `s∈S\S'`,
   conditioning on everything but `X_s` and using `E_{X_s}[g_j(x_{S\s},X_s)]=0` for *every*
   fixed `x_{S\s}` gives zero after integrating out the rest. This gives the exact variance
   formula in §3, and `Cov(ψ(X_i),g_j(X_S))=0` for `j≥2` (only `j=1,S={i}` survives), which
   gives the exact covariance formula.
3. **Cauchy–Schwarz**: `U_{N,F}` is `[P_N]`-measurable (order-invariant by construction), so
   `Var(E[S_N|Y_N]) ≥ Cov(S_N,U_{N,F})²/Var(U_{N,F})`. Substituting §3's exact formulas and
   dividing by `I_N^full=c²N‖ψ‖²` gives the bound; `c` cancels exactly.
4. **Finite span.** For `W_M=span{φ_{F_1},…,φ_{F_M}}` (`M` fixed), the rescaled Gram matrix
   `Ĝ_N=(Cov(√N·U_{N,F_m}/(NC(N-1,k_m-1)), √N·U_{N,F_{m'}}/(NC(N-1,k_{m'}-1))))` converges
   *entrywise* to the `L²` Gram matrix `G` of `{φ_{F_m}}` (leading contribution from
   overlap-`1` index pairs; overlap-`≥2` pairs are a relatively `O(1/N)` correction —
   confirmed numerically, see §4). Finite-dimensional matrix inversion is continuous at the
   invertible limit `G`, giving `liminf_N η_N(ψ) ≥ ‖Proj_{W_M}ψ‖²/‖ψ‖²` for every fixed `M`.
5. **Closure, without exchanging limits.** The bound in step 4 holds for *every* `M`
   independently (each after its own completed `N→∞`), and `‖Proj_{W_M}ψ‖` is non-decreasing
   in `M`; a single fixed number (`liminf_Nη_N(ψ)`) that dominates every term of an increasing
   sequence dominates its supremum. No `M↔N` limit exchange is used.
6. **Automatic separability.** For each fixed `k` there are only finitely many isomorphism
   classes of `k`-element posets, so `{φ_F}` for fixed `k` spans a finite-dimensional space;
   `H_caus` is the closure of a countable union of finite-dimensional spaces — separable by
   construction, not by assumption.
7. **Gauge side.** If a family `q_ε∝e^{cεψ}` leaves the law of `[P_k]` first-order stationary
   for every `k`, differentiating the (finite, hence trivially exchangeable) sum
   `Σ_π F(π)P_ε(π)` under `ε` and using exchangeability of the `k` iid coordinates gives
   `0 = kc⟨ψ,φ_F⟩` for every `F,k`, i.e. `ψ⊥H_caus`. Taking orthogonal complements:
   `G_D⊂H_caus^⊥ ⟹ H_caus⊂G_D^⊥` for any `G_D` satisfying that stationarity property.

## 4. Independent numerical audit (exact arithmetic, no Monte Carlo)

Two disjoint checks, both exact (`Fraction`/`sympy` rational arithmetic), scratchpad-only:

- **Continuous 3+1D check** (`k=2`, `F`=comparability, on the standard causal diamond
  `I((-1,0),(1,0))⊂M^{3+1}`): symbolic integration reproduces `V_4(τ)=πτ⁴/24`, `\bar a=1/10`,
  `σ²=Var(a)=1/100`, `τ²=7/100` exactly, and the theorem's bound collapses to the
  previously-verified exact rate `η_N(ψ)≥(2N-2)/(2N+5)`, `1-η_N≤7/(2N+5)`.
- **Discrete toy poset** (4-point diamond order, `k=2` and `k=3` simultaneously, multinomial-
  exact enumeration `N=3..50`): `Var(U_{N,F})` and `Cov(S_N,U_{N,F})` match the closed forms
  **exactly** at every `N` tested (both `k=2` and `k=3`, including the full degenerate `ζ_2`
  term). The cross-degree ratio `Cov(U_{N,F_2},U_{N,F_3})`'s overlap-`1` prediction over the
  true value rises monotonically `0→0.84` from `N=3` to `N=50`, consistent with the claimed
  `1-O(1/N)` convergence used in step 4 above.

Companion script: `dev/verify_causal_hoeffding_theorem.py` (re-run to reproduce every number
in this section; deterministic, no seeds).

## 5. Corollary — Fisher information geometry (verified via polarization)

`H_caus` is a closed linear subspace (closure of a span), so for `ψ_1,…,ψ_m∈H_caus` every
combination `ψ_a=Σaₐψₐ` is again in `H_caus`, hence `η_N(ψ_a)→1`. Applying this to
`ψ_α+ψ_β` and `ψ_α-ψ_β` and using the polarization identity
`Cov(a,b)=¼[Var(a+b)-Var(a-b)]` on `a=E[S_N^α|Y_N]`, `b=E[S_N^β|Y_N]` gives, for the full
(multi-parameter) Fisher matrices `I_{N,αβ}^{full}=c²N⟨ψ_α,ψ_β⟩` (exact) and
`I_{N,αβ}^{poset}=Cov(E[S_N^α|Y_N],E[S_N^β|Y_N])`:

```
(1/N) I_{N,αβ}^{poset}  →  c²⟨ψ_α,ψ_β⟩   =  (1/N) I_{N,αβ}^{full}
```

entrywise, on **any finite-dimensional subspace of `H_caus`** — not just a single direction.
The poset recovers the full Fisher metric restricted to `H_caus`, asymptotically.

## 6. Reformulation and the open reduction

Define the **causal observation tangent operator** `T_D ψ := (⟨ψ,φ_F⟩)_{k,F}`. Then, as a
direct Hilbert-space fact (orthogonal complement of a set = orthogonal complement of the
closure of its span): `ker T_D = H_caus^⊥`. Since `G_D` (directions generated by a flow
preserving the diamond) is itself a linear subspace (its defining equation
`4(ψ-μ_0ψ)=-div X` is linear), the geometric conjecture `H_caus=G_D^⊥` is *equivalent* to

```
ker T_D = closure(G_D).
```

**One direction is already established** (§3.1 step 7, conditional on `G_D`'s stationarity
property): `G_D ⊂ ker T_D`, i.e. `closure(G_D) ⊂ ker T_D` — every direction generated by a
diamond-preserving flow is first-order invisible to every finite causet law.

**The hard direction is OPEN and is the single remaining obligation:**

```
ker T_D  ⊆  closure(G_D)          [in d≥3, for a fixed Alexandrov diamond in flat Minkowski]
```

i.e.: every perturbation invisible at first order to the law of *every* finite causet is,
up to closure, gauge. This is a genuine classification problem — the operational content of
"the order sees curvature" for `d≥3` — not a formality.

### 6.1 Why this is not expected to be formally free (1+1D counterexample-shaped warning)

`docs/hoja_de_ruta_septiembre_2026.md` already proves, for the 1+1D copula/rank channel
(Teorema 14, "el sector antisimétrico es invisible bilinealmente", and Teorema 19,
"visibilidad de segundo orden ya en `N=2`"), that the antisymmetric tangent sector is exactly
first-order-invisible to the poset law yet becomes visible at second order and is **not** a
gauge direction. Translated to this framework: that sector lies in `ker T_D` but is not known
to lie in `closure(G_D)` merely by degree-1 vanishing. `ker T_D = closure(G_D)` is therefore
**not** a formal consequence of the definitions in any dimension — the `d≥3` rigidity has to
enter the proof substantively (e.g. via curvature/Weyl-tensor control unavailable in 1+1D
conformal flatness), or the reduction should be expected to fail in the same shape it already
failed once.

## 7. Next single obligation

Prove or refute, for a fixed Alexandrov diamond `D⊂M^{3+1}` (flat, no curvature yet):
`ker T_D ⊆ closure(G_D)`. Do not assume it transfers from the (already-shown-fragile) 1+1D
first-order/second-order structure.
