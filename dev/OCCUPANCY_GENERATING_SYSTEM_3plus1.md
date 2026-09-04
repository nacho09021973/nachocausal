# Occupancy generating system — k-free moment identity for ker T_D (3+1D radial reduction)

## 1. Status

STATUS: `OCCUPANCY_GENERATING_SYSTEM_PROVED` (analytic, exact) / `OCCUPANCY_GAUGE_CHECK = PASS`
(audit, see §7) / `VPLUS_RIESZ_IDENTITY_PROVED_WITH_DOMAIN_RESTRICTION` (see §11) /
`RADIAL_VOLTERRA_REDUCTION = PROVED` (see §12) / `RADIAL_OCCUPANCY_LOCAL_SYSTEM = PROVED` (see
§14) / `RADIAL_KERNEL_UNIQUENESS = OPEN` (not attempted yet) / `DEV_EXPLORATION /
NOT_COMMITTEE_REVIEWED`

SCOPE: compresses the combinatorial data of the causal-Hoeffding first-order projections
`φ_{k,u,v}` for the occupancy statistic `F_{k,u,v}=Σ_i u^{N_i^-}v^{N_i^+}`, for *every* `k` at
once, into a single `k`-free weak identity (§4) that every `ψ∈ker T_D` must satisfy. Builds on
`CAUSAL_HOEFFDING_FISHER_SUFFICIENCY.md` (the abstract `⟨ψ,φ_F⟩=0` orthogonality for
`ψ∈ker T_D`, taken as given here) and on the already-closed facts `ker T_D = H_caus^⊥`,
`t ∈ ker T_D`, `V_+^*=V_-` (re-derived independently in §3), and the closed `k≤3` computation
(sector even dim 3, sector odd dim 1, total dim 4 for first projections at `k=3`).

This document was derived and independently audited (analytic derivation + exact symbolic
integration for four of the five gauge-check moments, high-precision deterministic quadrature
— not Monte Carlo — for the remaining two) in conversation on branch
`emergencia/p1a-canal-sigma-m`, HEAD `2e8b3b8` at time of writing. It has **not** gone through
`/comite` or `/auditor`. It authorizes nothing beyond being a citable, re-derivable dev
artifact — no threshold, no validation run, no claim promotion. In particular §7's two
Volterra moments are explicitly flagged as numerically-confirmed, not symbolically derived —
do not cite them as closed-form lemmas.

## 2. Setting

`D = {(t,x)∈R×R³ : |t|+|x|<1}` (the Alexandrov interval between `(-1,0)` and `(1,0)` in 3+1D
flat Minkowski — verified: `I^+(-1,0)∩I^-(1,0) = D` exactly), `dμ_0 = (3/2π) dt d³x`
(normalized, total mass 1). For radial (`SO(3)`-invariant) functions, `dμ_0 = 6r²dr dt`,
`0≤r<1-|t|`. For `x=(t,x)`, `X_1,…,X_k` iid `~μ_0`:

```
N_i^- = #{predecessors of i},   N_i^+ = #{successors of i}
α(x) = [(1-t)²-r²]²/16 = μ_0(I^+(x)),    β(x) = [(1+t)²-r²]²/16 = μ_0(I^-(x))
V_+f(x) = ∫_{I^+(x)} f dμ_0,             V_-f(x) = ∫_{I^-(x)} f dμ_0
```

(`α=μ_0(I^+(x))`, `β=μ_0(I^-(x))` confirmed directly from the Lorentz-invariant Alexandrov-
interval volume formula `Vol(τ)=(π/24)τ⁴` in 3+1D: `Vol(D)=Vol(τ=2)=2π/3`, matching
`∫(4π/3)(1-|t|)³dt=2π/3`; and `μ_0(I^-(x))=(3/2π)·(2π/3)β(x)=β(x)` since `I^-(x)∩D` is itself
the Alexandrov interval `[(-1,0),x]` of proper time `4√β(x)`.)

## 3. Occupancy definition, conditional expectation, Volterra adjoint

```
F_{k,u,v}(P) = Σ_i u^{N_i^-}v^{N_i^+}          — isomorphism-class invariant, finite poly in u,v

m_{u,v}(x) = 1+(u-1)β(x)+(v-1)α(x)
E[u^{N_1^-}v^{N_1^+} | X_1=x] = m(x)^{k-1}

E[F_{k,u,v} | X_1=x]
  = m(x)^{k-1} + (k-1)C_{k-2}(u,v)
  + (k-1)(u-1)V_+[m^{k-2}](x) + (k-1)(v-1)V_-[m^{k-2}](x),      C_n(u,v):=∫_D m^n dμ_0
```

rederived from scratch (not assumed) by conditioning on `X_1=x`, splitting the `k-1` other
points into "the specific pairwise relation with `X_2`" (factor `u`/`v`/`1` by
`y∈I^+(x)`/`y∈I^-(x)`/incomparable) times "`k-2` further points" (giving `m(y)^{k-2}` by the
same single-particle argument applied to `y`).

**Volterra adjoint** (Fubini, no `□²` used):
```
⟨f,V_+g⟩ = ∫∫_{x≺y} f(x)g(y) dμ_0dμ_0 = ⟨V_-f,g⟩     ⟹     V_+^* = V_-
```

## 4. Master generating identity and weak polynomial form

For `ψ∈ker T_D` (`⟨ψ,1⟩=0` kills the `x`-constant term `(k-1)C_{k-2}`; the causal-Hoeffding
orthogonality `⟨ψ,φ_{k,u,v}⟩=0` kills the rest by construction), with `n=k-1`, `a=u-1`,
`b=v-1`, `m=1+aβ+bα`:

```
0 = ⟨ψ,m^n⟩ + na⟨V_-ψ,m^{n-1}⟩ + nb⟨V_+ψ,m^{n-1}⟩                                   (*)_n
```

Multinomial expansion in `(a,b)`, using `n·C(n-1,p-1,q)=p·C(n,p,q)` and
`n·C(n-1,p,q-1)=q·C(n,p,q)` (**all `n`-dependence cancels exactly**), gives — first for
`n≥p+q` (any single such `n` suffices; the resulting equation is `n`-independent) and hence for
**every** `p,q≥0`:

```
⟨ψ,β^pα^q⟩ + p⟨V_-ψ,β^{p-1}α^q⟩ + q⟨V_+ψ,β^pα^{q-1}⟩ = 0                              (2)
```

equivalently, for every polynomial `P(α,β)=Σc_{p,q}β^pα^q`:

```
⟨ψ,P⟩ + ⟨V_-ψ,∂_βP⟩ + ⟨V_+ψ,∂_αP⟩ = 0        ∀ψ∈ker T_D, ∀P∈R[α,β]                    (3)
```

No extension to non-polynomial test functions is claimed here (would need Sobolev/topology
input not established in this document).

**Degree triangularity** (structural only, no invertibility claimed): at total degree
`m=p+q` there are exactly `m+1` equations `(p,q)`, `p+q=m`; each ties a degree-`m` moment of
`ψ` to degree-`(m-1)` moments of `V_-ψ` and `V_+ψ`.

## 5. Sanity check k=2

```
F_{2,u,v} = 2+(u+v-2)·1_comparable   ⟹   φ_{2,u,v}=(u+v-2)φ_comp,  φ_comp=α+β-const
```
matches (3) at `(p,q)=(1,0)`.

## 6. Sanity check k=3 — rank audit

| class | structure | F_{3,u,v} |
|---|---|---|
| A | antichain | 3 |
| R | one relation + isolated pt | 1+u+v |
| V | 1 min → 2 incomp max | v²+2u |
| Λ | 2 incomp min → 1 max | u²+2v |
| C | total chain | u²+uv+v² |

Direct enumeration on the 5 unlabelled 3-posets matches exactly. Expanding `φ_{3,u,v}(x)`
(centered, i.e. after the constant-killing map `F↦E[F|X_1=·]-E[F]` — the raw span of
`F_{3,u,v}` before centering is not the object being counted here) in `(a,b)=(u-1,v-1)`:
linear term `∝ 2(a+b)(α+β)` (1 direction: `φ_comp`); quadratic terms span
`{β²+2V_+β, α²+2V_-α, 2αβ+2V_+α+2V_-β}`. Under time-reversal `t↦-t` (`α↔β`, `V_+↔V_-`): the
first two swap into 1 even + 1 odd combination, the third is invariant (even). Total: **3 even
+ 1 odd = 4**, matching the closed `k=3` first-projection dimension exactly (even/odd split
included). Independent audit of the general formula: **passes**.

## 7. AUDIT — gauge check ψ=t

`t∈ker T_D` (closed fact) is a corollary check of (2)/(3), not a separate hypothesis: any
`ψ∈L²(μ_0)` with `⟨ψ,1⟩=0` and the causal-Hoeffding orthogonality automatically satisfies (2);
`t` is bounded on `D` hence in `L²`. The check below is an **orientation/adjoint/normalization
audit**, not a new proof obligation.

### 7a. Exact (sympy, closed-form rational integration)

```
⟨t,α⟩  = -1/60      ⟨t,β⟩  = 1/60
⟨t,α²⟩ = -1/210     ⟨t,β²⟩ = 1/210
⟨t,αβ⟩ = 0
```

### 7b. Numerically confirmed (deterministic Gauss–Legendre quadrature, NOT Monte Carlo,
NOT a closed-form derivation)

`V_-α(x)`, `V_+β(x)` require integrating a radial function over the past/future Alexandrov
cone of a point off the coordinate origin — a 3D ball-intersection ("lens") integral with no
elementary closed form derived in this session. Reduced via the solid-angle factor
`h(ρ,r,s)=clip((s²-(ρ-r)²)/(2ρr),0,2)` to a 4-fold nested integral, evaluated by tensor
Gauss–Legendre with exact substitution of the (t,r)- and (t',ρ)-dependent bounds. Convergence
(monotone toward the targets as resolution increases):

```
N=20×120:  ⟨t,V_-α⟩=0.0023810653   (target 1/420=0.0023809524,  diff 1.1e-7)
N=30×180:  ⟨t,V_-α⟩=0.0023809625                                  diff 1.0e-8
N=45×260:  ⟨t,V_-α⟩=0.00238095144                                 diff -9.4e-10
```
and symmetrically `⟨t,V_+β⟩→-1/420` at the same rate. Sanity check performed first:
numerically reconstructed `μ_0(I^-(x))` matches `β(x)` (the closed-form Lorentz-invariant
volume) to confirm the cone/measure geometry before trusting the rest.

```
A := V_-α,  ⟨t,A⟩ = 1/420 (numerical)         B := V_+β,  ⟨t,B⟩ = -1/420 (numerical)
```

### 7c. The five checks of (2) at ψ=t

```
(1,0): ⟨t,β⟩+⟨V_-t,1⟩ = ⟨t,β⟩+⟨t,α⟩         =  1/60 - 1/60          = 0   [exact, 7a]
(0,1): ⟨t,α⟩+⟨V_+t,1⟩ = ⟨t,α⟩+⟨t,β⟩         = -1/60 + 1/60          = 0   [exact, 7a]
(2,0): ⟨t,β²⟩+2⟨V_-t,β⟩ = ⟨t,β²⟩+2⟨t,B⟩     =  1/210 + 2(-1/420)    = 0   [7a exact + 7b numeric]
(0,2): ⟨t,α²⟩+2⟨V_+t,α⟩ = ⟨t,α²⟩+2⟨t,A⟩     = -1/210 + 2(1/420)     = 0   [7a exact + 7b numeric]
(1,1): ⟨t,αβ⟩+⟨V_-t,α⟩+⟨V_+t,β⟩ = ⟨t,αβ+V_+α+V_-β⟩ = 0              [exact, parity argument]
```

The `(1,1)` case needs no computation: `αβ` is even in `t` (`α(-t,r)=β(t,r)` ⟹
`αβ(-t,r)=βα(t,r)=αβ(t,r)`, confirmed numerically `⟨t,αβ⟩=0` in 7a); and
`V_+α(-t,r)=V_-β(t,r)` follows from the time-reversal map `R:(t,r)↦(-t,r)` being a symmetry of
`(D,μ_0)` with `R(I^+(x))=I^-(R(x))` and `α∘R=β`, so `V_+α+V_-β` is even in `t`; `t`(odd)
times an even function integrates to `0` against the `t`-symmetric `μ_0`.

**`GAUGE_CHECK = PASS`.**

## 8. Verdict

```
OCCUPANCY_GENERATING_SYSTEM_PROVED
```

## 9. Next single obligation

Do **not** compute `k=4` class by class. Classify the radial kernel of the weak identity (3):

```
ψ ∈ L²_0(D)^{SO(3)},   ∀P∈R[α,β]:  ⟨ψ,P⟩+⟨V_-ψ,∂_βP⟩+⟨V_+ψ,∂_αP⟩=0    ⟹?   ψ∈span{t}
```

First move: change of variables `(t,r)↦(α,β)` (§10 below). Finding: this chart has a fold
degeneracy exactly where the physically interesting axis `r=0` lives, so the integration-by-
parts step is deferred to the smooth `(u,v)` double-null chart (§10, end) rather than done
directly in `(α,β)`. `□²` is deliberately not invoked yet.

## 10. Change of variables (t,r)↔(α,β) — fold degeneracy

STATUS: exploratory groundwork for §9, verified (sympy symbolic Jacobian + numeric round-trip
and domain checks), not yet a classification result.

**Inverse map** (exact, confirmed by round-trip on random samples in `D∩{r≥0}`):
```
t = √β - √α
r² = (1-√α-√β)² - 4√(αβ)     [= 1+t²-2√α-2√β]
```

**Image domain** — a curved triangle (confirmed: max of `α^{1/4}+β^{1/4}` over
`D∩{r≥0}` is `1`, attained exactly on `r=0`; `200000`-sample sweep, max `0.999999999985837`):
```
Ω = {(α,β) : α,β≥0,  α^{1/4}+β^{1/4} ≤ 1}
```
Vertices: `(1,0)↔`past tip `(t,r)=(-1,0)`; `(0,1)↔`future tip `(1,0)`; `(0,0)↔`equator
`(0,1)`. The two *straight* edges (`α=0,β∈[0,1]` and `β=0,α∈[0,1]`) are the image of the true
light-cone boundary `r=1-|t|` of `D`. The *curved* edge `α^{1/4}+β^{1/4}=1` is the image of the
interior symmetry axis `r=0`.

**Jacobian** (sympy, exact factorization):
```
∂(α,β)/∂(t,r) = r·τ_F²·τ_P²/8,     τ_F²=(1-t)²-r²,  τ_P²=(1+t)²-r²
```

**Weight** (verified to machine precision against `w·|J|=6r²` on random samples):
```
dμ_0 = w(α,β) dα dβ,      w(α,β) = 3r(α,β)/√(αβ)
```

**Fold.** `∂(α,β)/∂(t,r) → 0` exactly as `r→0`, i.e. exactly on the *curved* boundary of `Ω`
— consistent with `α,β` depending on `r` only through `r²` (the same degeneracy as `x↦x²` at
the origin: `r` and `-r` give the same `(α,β)`, only resolved by the `r≥0` convention). So
`(α,β)` is a genuine diffeomorphism on the *open* region `r>0` (interior of `Ω`) but degenerates
on its curved edge — precisely where the object of interest (`ψ` radial, and in particular the
gauge direction `t`) lives on the axis. `w` also blows up like `1/√α` (resp. `1/√β`) on the two
straight edges (image of the true causal boundary of `D`) — an integrable, polar-coordinate-
type singularity, not further examined here.

**Consequence for §9.** Integration by parts directly in `(α,β)` would have to fight both the
fold (curved edge) and the `1/√(αβ)` blow-up (straight edges) simultaneously. Deferred:
instead, do the "polynomial density → weak PDE" step of §9 in the smooth double-null chart
```
u=t-r, v=t+r,     dμ_0 = (3/4)(v-u)² du dv,     Ω_{uv} = {-1<u≤v<1}   (no fold, no blow-up)
α = (1-u)²(1-v)²/16,     β = (1+u)²(1+v)²/16
```
treating `R[α,β]` as the subring of `R[u,v]` generated by these two quartics (not the full
polynomial ring in `u,v`) — i.e. (3) is tested only against that restricted family, and the
integration by parts / distributional step happens in `(u,v)`, not `(α,β)`.

## 11. Riesz identity — `□²V_±ψ = 12ψ` in `D'(D°)`

STATUS: `VPLUS_RIESZ_IDENTITY_PROVED_WITH_DOMAIN_RESTRICTION` (the restriction to `D°`, not a
global statement up to `∂D`, is exactly the scope targeted — not a weakness).

**Minkowski (global, `s=t²-r²`, `□=-∂_t²+Δ`):**
```
□F(s) = -4[sF''(s)+2F'(s)]                                          (sympy-verified, exact)
K_+ = θ(t-r) = θ(t)θ(s),  K_- = θ(-t-r)                              (future/past cone indicators)
□K_+ = -4θ(t)δ(s) = -(2/r)δ(t-r)         (two independent methods: direct radial distributional
                                           calculus, and the w=r·K_+ 1D-reduction — agree exactly,
                                           no hidden vertex term: w is Lipschitz at r=0, unlike 1/r)
G_ret := -(1/2π)θ(t)δ(s)  satisfies  □G_ret = δ_0     (cross-checked against the standard
   □_std G_ret^std=δ_0, G_ret^std=δ(t-r)/(4πr)θ(t); consistent with the SAME volume constant
   V(τ)=(π/24)τ⁴ cited in biblioteca/derived-md/QFT_On_Causal_Sets_arXiv2306.04800.md, eq.17-19)
□K_+ = 8πG_ret   ⟹   □²K_+ = 8πδ_0        K_- via time-reversal (□ commutes with t↦-t): □²K_-=8πδ_0
```

**Restriction to `D`:** `f:=(3/2π)ψ·1_D` (extended by zero), `K_+*f = V_-ψ` and `K_-*f = V_+ψ`
exactly as *functions* on `D°` (since `J^∓(x)` and `I^∓(x)` differ only on the light cone,
measure zero). `□²(K_+*f)=(□²K_+)*f=8πδ_0*f=8πf`. Locality of distributional derivatives —
testing only against `φ∈C_c^∞(D°)`, which never sees anything outside `D°` — means the equality
`V_-ψ=K_+*f` need only hold *on* `D°` (it does, exactly) for the restricted identity to follow;
no boundary flux or cancellation argument is needed:
```
□²V_-ψ = 12ψ,   □²V_+ψ = 12ψ     in D'(D°),   ∀ψ∈L²(D,μ_0)
```
Sanity check (`ψ=1`): `V_-1=β`, `V_+1=α`, and `□²β=12`, `□²α=12` — exact, sympy, radial
`□f=-f_tt+f_rr+(2/r)f_r`. This is the `ψ=1` instance of the general result, not a substitute for
it — the general derivation goes through the Minkowski `K_±` computation above, not a
term-by-term check.

## 12. Radial null-coordinate reduction in 3+1D

STATUS: `RADIAL_VOLTERRA_REDUCTION = PROVED` (all identities below sympy-verified exactly).
Separate from and does **not** resolve `RADIAL_KERNEL_CLASSIFICATION = OPEN` (§9).

### 12.1 Jacobian correction

An earlier pass through this derivation (same conversation) inverted the chain rule using rows
of `J⁻¹` directly instead of `(J⁻¹)ᵀ` — plausible enough to be worth recording. Caught by a
Kronecker-delta audit (`∂_α α=1, ∂_α β=0, ∂_β α=0, ∂_β β=1`, checked symbolically): the naive
row-based `∂_β` failed this test; the transpose-corrected one passes exactly. Corrected result:
```
∂_α = 4/[(u-1)(v-1)(u-v)] · [-(u+1)∂_u+(v+1)∂_v]        (unchanged — this one was already right)
∂_β = 4/[(u+1)(v+1)(u-v)] · [(u-1)∂_u-(v-1)∂_v]          (CORRECTED — was previously stated with
                                                            denominator (u-1)(v-1) instead of
                                                            (u+1)(v+1); wrong)
```

### 12.2 Radial reduction lemma

For radial `f(t,r)`, `u=t-r,v=t+r` (sympy-verified exactly, full chain rule):
```
□f = -(4/r) ∂_u∂_v(rf)
```

### 12.3 Fourth-order equations for `a=rV_-ψ`, `b=rV_+ψ`

Applying §12.2 twice and using the Riesz identity (§11) `□²V_∓ψ=12ψ`:
```
16/r · a_{uuvv} = 12ψ   ⟹   a_{uuvv} = (3r/4)ψ = (3/8)(v-u)ψ
```
identically for `b`. So with `q=a+b`, `h=a-b`:
```
a_{uuvv} = b_{uuvv} = (3/8)(v-u)ψ
q_{uuvv} = (3/4)(v-u)ψ,     h_{uuvv} = 0
```
Local general solution of the homogeneous piece (verified by direct substitution):
```
h(u,v) = A_0(u) + v·A_1(u) + B_0(v) + u·B_1(v)
```
(four single-variable functions — likely relevant to the classification step, not used yet.)

### 12.4 Volterra representations (exact scope: retarded/advanced selection, not arbitrary solutions)

```
a(u,v) = (3/8) ∫_{-1}^u (u-ξ) ∫_{-1}^v (v-η)(η-ξ) ψ(ξ,η) dη dξ            (= r·V_-ψ)
b(u,v) = (3/8) ∫_u^1  (ξ-u) ∫_v^1  (η-v)(η-ξ) ψ(ξ,η) dη dξ                 (= r·V_+ψ)
```
Verified `a_{uuvv}=(3/8)(v-u)ψ` for **general** `ψ` (not just `ψ=1`) via Fundamental-Theorem-of-
Calculus differentiation under the integral sign, both `u`-derivatives and both `v`-derivatives,
symbolically with an abstract `ψ(ξ,η)`; same for `b`. These are the solutions singled out by the
retarded/advanced causal conditions attached to `V_-`/`V_+`, not generic solutions of the PDE —
confirmed structurally (holds for any `ψ`, not fitted): `a(-1,v)=0`, `∂_ua(-1,v)=0`, `a(u,-1)=0`
(vanishing because the integration bounds start at `-1`, independent of `ψ`); symmetric advanced
conditions for `b` at the `+1` bounds.

**Sanity check, `ψ=1`** (exact symbolic integration, difference `0`):
```
a(u,v)|_{ψ=1} = r·β(u,v)         b(u,v)|_{ψ=1} = r·α(u,v)
```

## 13. Occupancy identity substituted into `(u,v)` — mechanical form (provenance record)

STATUS: sympy-verified exactly (see §14 for the canonical, non-singular form — this section is
kept only as a traceable derivation record, not the form to build on).

Substituting the corrected `∂_α,∂_β` (§12.1), `A=a/r,B=b/r` (§12.4), and `dμ_0=(3/4)(v-u)²dudv`
into the occupancy weak identity (3) gives (sympy: mechanical substitution, no simplification
choices):
```
∫_Ω { (3/4)(v-u)²ψP
      + 6[ b(u+1)/((u-1)(v-1)) − a(u-1)/((u+1)(v+1)) ] P_u
      + 6[ a(v-1)/((u+1)(v+1)) − b(v+1)/((u-1)(v-1)) ] P_v } du dv = 0
```
Apparent simple poles at each of the triangle's degenerate loci, split unevenly between the `a`-
and `b`-terms — not yet informative on its own; resolved in §14.

## 14. Regular canonical formulation — `(X,Y)` transport system

STATUS: `RADIAL_OCCUPANCY_LOCAL_SYSTEM = PROVED` (every displayed identity below sympy-verified
exactly against §13's mechanical form). `RADIAL_KERNEL_UNIQUENESS = OPEN` — not attempted.

### 14.1 Geometric correction

The `(u,v)`-triangle `𝒯={-1<u≤v<1}` has **three edges**: `u=-1`, `v=1`, and the diagonal `u=v`
(the radial-quotient axis `r=0`). The loci `v=-1` and `u=1` are not edges — they are only the
two vertices `(-1,-1)` (past tip) and `(1,1)` (future tip); the third vertex `(-1,1)` is the
equator `(t,r)=(0,1)`. (Corrects loose "three straight+curved boundary pieces" language used
informally in §10/§13's framing — the fold-vs-edge structure there is still correct, this is
just the precise vertex/edge count for `𝒯`.)

### 14.2 The `(1±u)(1±v)`-normalization that kills the poles

Using `√α=(1-u)(1-v)/4`, `√β=(1+u)(1+v)/4` (§10):
```
X := a/√β,      Y := b/√α
```
Substitution `b(u+1)/[(u-1)(v-1)] = (1+u)Y/4`, `−a(u-1)/[(u+1)(v+1)] = (1-u)X/4` (and the
analogous `P_v`-coefficient pair) turns §13's identity into, after dividing by the common factor
`3/2` (sympy-verified: both `P_u` and `P_v` coefficients match exactly):
```
∫_𝒯 { ½(v-u)²ψP + [(1-u)X+(1+u)Y]P_u − [(1-v)X+(1+v)Y]P_v } du dv = 0      (10)
```
No `(u-v)` denominator anywhere — the diagonal (`r=0`) is not singular in this formulation. The
apparent poles at `u=±1,v=±1` are absorbed into `X,Y`, not eliminated by algebraic cancellation
of the weight; see §14.4 for what actually kills them.

### 14.3 Interior distributional PDE

For `P∈C_c^∞(𝒯°)` (compact support strictly inside `𝒯`, no boundary term — same locality
argument as §11), integrating (10) by parts in `u` and `v` gives, in `D'(𝒯°)`:
```
½(v-u)²ψ − ∂_u[(1-u)X+(1+u)Y] + ∂_v[(1-v)X+(1+v)Y] = 0                    (11)
```
Expanding (sympy-verified: the zero-order `X,Y` terms cancel exactly, leaving only first
derivatives):
```
[(1-v)∂_v−(1-u)∂_u]X + [(1+v)∂_v−(1+u)∂_u]Y = −½(v-u)²ψ                   (12)
```
With `D_- := (1-v)∂_v−(1-u)∂_u`, `D_+ := (1+v)∂_v−(1+u)∂_u`:
```
D_-X + D_+Y = −½(v-u)²ψ                                                    (13)
```

### 14.4 Causal vanishing — the actual mechanism behind §13's apparent poles

From §12.4's boundary facts `a(-1,v)=0, ∂_ua(-1,v)=0, a(u,-1)=0` (structural, holds for every
`ψ`): **heuristically**, for `a` regular enough to Taylor-expand, `a=O((u+1)²)` as `u→-1`; since
`√β~(u+1)(v+1)` there, `X=a/√β→0` at the retarded edge `u=-1`. Symmetrically `Y→0` at the
advanced edge `v=1` (from `b`'s analogous vanishing at the `+1` bounds). This is the actual
mechanism — not a cancellation internal to the weight `w` — and it is **not** independently
proved here as a uniform bound for general `ψ∈L²(D,μ_0)`; it is a structural consequence of
already-proved facts (§12.4) plus an unverified regularity assumption, flagged accordingly. A
rigorous trace argument for general `ψ∈L²` is deferred to whenever the classification actually
needs it.

### 14.5 Coupling to the Riesz identity — closing `ψ` out of the system

`a=(1+u)(1+v)X/4`, `b=(1-u)(1-v)Y/4` turn §12.3's `a_{uuvv}=b_{uuvv}=(3/8)(v-u)ψ` into
(sympy-verified — direct consequence of the substitution, exact):
```
∂_u²∂_v²[(1+u)(1+v)X] = (3/2)(v-u)ψ                                        (14)
∂_u²∂_v²[(1-u)(1-v)Y] = (3/2)(v-u)ψ                                        (15)
```
Eliminating `ψ`: `∂_u²∂_v²[(1+u)(1+v)X] = ∂_u²∂_v²[(1-u)(1-v)Y]`. Closed local system for
`(X,Y,ψ)`, no `V_±` operators remaining:
```
D_-X + D_+Y = -½(v-u)²ψ
∂_u²∂_v²[(1+u)(1+v)X] = (3/2)(v-u)ψ
∂_u²∂_v²[(1-u)(1-v)Y] = (3/2)(v-u)ψ
```

## 15. Next single obligation

Classify the solutions of the system (13)–(15) subject to the causal conditions on `X,Y`
(§14.4, made rigorous as needed). If that solution space is one-dimensional and corresponds to
`ψ=t`, this closes `ker(T_D|_radial)=span{t}` — this is the final attack, not another
preparatory reduction.
