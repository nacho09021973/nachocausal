# X₀ — Well-posedness of the adversary law Q_n (simple vs composite) + reference sourcing for X₁ (dev, NOT a result)

> Analytic step authorised by `docs/comite/comite_decision_005_…md` §9 step 1 (the falsifier's minimal
> test) + step 2 (source the X₁ statistics references). **No code, no seed, no sealed-path execution, no
> commit, no prereg.** Procedencia: HEAD `fafd880`, branch `main`, `make verify-seal` =
> `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (confirmed before writing). Runs no
> sealed code, burns no seed. Resolves the nested `<X₀>` of comité-005; leaves `<X₁>` open with sourced
> references.

## 0. The question (comité-005 falsifier)

> For a fixed small `n` and density `ρ`, is the law `Q_n` on isomorphism classes of `n`-element posets
> implied by *"a flat Minkowski patch with a shaped future boundary whose `V`-marginal matches `H_trap`"*
> **uniquely determined** (⟹ SIMPLE law, the four-case classification of comité-005 §1 applies) or
> **underdetermined** (⟹ COMPOSITE family, reframe as uniform/minimax separation)?

## 1. The exact order-theoretic reduction (lo ESTABLECIDO)

In 1+1D Minkowski, pass to **null coordinates** `u = t − r`, `v = t + r`. The causal future is
`y ≽ x ⟺ u_y ≥ u_x AND v_y ≥ v_x`. Hence:

> **The 1+1D Minkowski causal order of a point set is exactly the 2-dimensional dominance (product)
> order on `(u, v)`.** (Standard; the 1+1D light cone factorises into two null half-lines. This is the
> Minkowski branch of the sealed generator, `nachocausal/generator.py:113-114`,
> `C = (dt>0) & (dt ≥ |Δr|)`, which in `(u,v)` is `Δu≥0 ∧ Δv≥0`.)

Consequences, all order-invariant and relabel-invariant:
- **Future-volume:** `V(x) = |{y : u_y ≥ u_x, v_y ≥ v_x} ∩ Patch|`, i.e. `ρ·A(u_x,v_x)` in expectation,
  where `A(u_x,v_x) = area` of the patch region north-east of `x` (the up-set area).
- **Interval cardinality (the focusing carrier):** for `x ≼ y`,
  `|[x,y]| = |{z : u_x≤u_z≤u_y, v_x≤v_z≤v_y}| ≈ ρ·(u_y−u_x)(v_y−v_x)` = the count in the **axis-aligned
  rectangle** with corners `x, y`. This is a **pairwise** (joint) quantity.
- A "shaped future boundary" of the patch is the **upper-right frontier** of the region `R ⊂ (u,v)`.

## 2. Resolution of X₀: Q_n is COMPOSITE (the V-marginal does NOT pin the boundary)

**Dimension argument (decisive).** The matching constraint is on the **marginal law of the scalar `V`**,
i.e. the univariate distribution of `A(u_x,v_x)` as `x` ranges over the (random) minimal frontier of `R`.
This is **one univariate probability law**. The object being chosen — the boundary profile / region `R` —
is an **infinite-dimensional** degree of freedom (a planar region, equivalently a frontier function
`u ↦ v_bdy(u)`). A single univariate distribution cannot determine an infinite-dimensional region: the
map `R ↦ (V\text{-marginal})` has **infinite-dimensional fibers**. Therefore the set of flat patches
consistent with a fixed `V`-marginal is an infinite family, and

```
Q_n  is  COMPOSITE  (a family {Q_n^θ}_θ of laws),  NOT a single (simple) law.
```

**Why this is not a technicality — the unmatched DOF is precisely the focusing channel.** `V` is an
up-set **area** (a one-apex functional). The full suborder law is fixed by *all* interval cardinalities
`|[x,y]| ∝ (u_y−u_x)(v_y−v_x)` — **pairwise rectangle counts** — and joint overlaps
`|fut(x)∩fut(y)|` (the area of the common north-east quadrant). These joint quantities are **not
functions of the one-point `V`-marginal**: one can hold the histogram of up-set areas over minimal apexes
fixed while redistributing where that area sits in `(u,v)`, which changes the rectangle/overlap law.
So matching `V` leaves the **interval-covariance (focusing) structure free** — exactly the
`σ(C_loc)∖σ(V)` channel the audit (§10.2) and the physicist isolated. The adversary family is the set of
all flat patches that mimic `V` but may differ in focusing.

**Small-n sanity (illustrative, no run).**
- `n = 2`: the `V`-marginal records, for the minimal point(s), the up-set size — essentially `P(`the two
  points are comparable`)` and the size of the larger up-set. Many regions `R` realise the same such
  scalar law while giving different `|[x,y]|` (the single interval, when the pair is comparable). Already
  underdetermined.
- `n = 3`: the iso-classes of a 3-element poset (antichain, 3-chain, "V" `a≺b,a≺c`, "Λ" `a≺c,b≺c`, single
  edge + isolated) have probabilities under sprinkling into `R` that depend on the *joint* (pairwise)
  geometry; the `V`-marginal (multiset of minimal up-set sizes) constrains only the marginal counts, so
  distinct `R` with the same `V`-marginal assign **different** probabilities to "V" vs "Λ" vs "chain".
  The map `R ↦ (`law on 3-element iso-classes`)` is many-to-one onto the `V`-marginal constraint.

**Verdict of X₀: `COMPOSITE`.** The simple-vs-simple four-case classification of comité-005 §1 does **not**
apply as stated; it must be reframed.

## 3. Consequence — the correct (reframed) object

The identifiability problem is a **simple-vs-composite** asymptotic test:

```
H_trap      = { P_n }                        (simple: the Schwarzschild-interior law)
H_no-trap   = 𝒬_n = { Q_n^θ : θ }            (composite: ALL flat patches matching the V-marginal)
```

The four-case dichotomy of `dev/INTRINSIC_OBSERVABLE_AUDIT_NOTES.md` §10.1 now applies to the **least
favourable pairing**, not to a single `(P_n,Q_n)`:

- **Identifiable (an intrinsic order-only T exists)** ⟺ `sup_{θ} affinity(P_n, Q_n^θ) → 0`, i.e. `T`
  must separate `P_n` from **every** flat `V`-matched patch *uniformly* (minimax separation;
  `‖P_n − Q_n^θ‖_TV → 1` uniformly in θ).
- **Non-identifiable** ⟺ **∃ θ** with `Q_n^θ` contiguous (or merely not separated) to `P_n`: the
  adversary only needs **one** flat patch that mimics `P_n`'s focusing structure as well as its `V`.

This is the honest sharpening: to *claim* an intrinsic trapping observable you must beat the **worst-case**
flat mimic; to *refute* one you need a **single** good mimic. Both directions are strictly harder/cleaner
than the simple-law version — exactly the falsifier's point.

**Sharpened nested token (updates comité-005):**
`UNDECIDED_NEEDS_<X₁: a uniform/minimax bound — sup over the V-matched flat family 𝒬_n of the affinity
(equivalently a lower bound on inf_θ ‖P_n − Q_n^θ‖_TV) for the FULL unlabelled-suborder law under
transitive (sprinkled-Poisson, = 2D-dominance) dependence; via a second-moment / Bretagnolle–Huber
two-point bound applied to the least-favourable member, with edge-independence replaced by a Poisson
U-statistic / Janson variance decomposition of the iso-invariant interval-cardinality-covariance statistic>`.

Note `X₁` is now **minimax over a composite family**, not a single-pair bound — this is the precise
correction `X₀` forces.

## 4. The two-line external question (for Brightwell/Kleijn), now well-posed

> In the 2D-dominance (1+1D-Minkowski) order of a Poisson sprinkling, let 𝒬_n be the family of flat
> patches whose one-point future-volume marginal matches that of a Schwarzschild-interior sprinkling P_n.
> Is `inf_{Q∈𝒬_n} ‖P_n − Q‖_TV → 1` (a uniform/minimax separation by some iso-invariant interval-
> cardinality functional), or is some `Q∈𝒬_n` contiguous to `P_n` — and which second-moment / contiguity
> technique for transitive (non-edge-independent) random orders settles it?

## 5. References to source for X₁ (comité-005 step 2)

Needed because the statistics machinery is **absent from `biblioteca/`** (comité-005 §7 literature
verdict). Identified by author/title/year. **Bibliographic status legend (this session):**
`[CITE-CONFIRMED]` = author/title/year/venue + arXiv-id/DOI verified via web search (provenance §5.1
below); `[CONTENT-UNVERIFIED]` = the paper exists but I have **not read it** to confirm it contains the
*transitive-dependence / composite-minimax* machinery `X₁` needs; `[UNVERIFIED]` = not yet web-confirmed.
**No reference is physically in `biblioteca/` yet** — `[CITE-CONFIRMED]` means citable-by-coordinate, not
sourced-into-the-library.

**Two-point / TV ↔ testing / Bretagnolle–Huber (the X₁ core):**
- Tsybakov, *Introduction to Nonparametric Estimation*, Springer 2009 — Ch. 2 (Le Cam two-point method,
  Fano, Assouad; the TV↔testing affinity; the Bretagnolle–Huber inequality `1−TV ≥ ½·exp(−KL)`). Already
  cited heuristically in `dev/PR003_INFO_BOUND_NOTES.md:53`. [standard textbook; CONTENT-UNVERIFIED — not
  in biblioteca]
- Bretagnolle & Huber, *Estimation des densités: risque minimax*, **Z. Wahrscheinlichkeitstheorie verw.
  Gebiete 47:119–137 (1979)** (now *Probab. Theory Related Fields*; corrections in *Sém. Probab.
  Strasbourg* 13:647, 1979) — the original `KL → TV` inequality. [CITE-CONFIRMED; CONTENT-UNVERIFIED]

**Contiguity (Le Cam's lemmas) — for the non-identifiable direction:**
- Le Cam, *Asymptotic Methods in Statistical Decision Theory*, Springer 1986 — contiguity, Le Cam's
  first/second/third lemmas. [standard; CONTENT-UNVERIFIED]
- van der Vaart, *Asymptotic Statistics*, CUP 1998 — Ch. 6 (contiguity, log-likelihood-ratio control); the
  accessible standard reference. [standard; CONTENT-UNVERIFIED]

**Composite / minimax testing (forced by X₀ = composite):**
- Ingster & Suslina, *Nonparametric Goodness-of-Fit Testing under Gaussian Models*, Springer 2003 —
  composite-alternative separation rates, contiguity of sequences. [standard; CONTENT-UNVERIFIED]

**Second-moment / contiguity on DEPENDENT random structures (the edge-independence replacement):**
- Janson, Łuczak & Ruciński, *Random Graphs*, Wiley 2000 — Ch. on small-subgraph counts, the
  second-moment method, contiguity of random-structure sequences. [standard; CONTENT-UNVERIFIED]
- Janson, *Random Regular Graphs: Asymptotic Distributions and Contiguity*, **Combin. Probab. Comput.
  4(4):369–405 (1995)** — the prototype contiguity-via-small-cycle-counts argument for dependent models.
  [CITE-CONFIRMED; CONTENT-UNVERIFIED]
- *(distinct, later paper — NOT a "companion" to the 1995 one; a separate work):* Janson, *Asymptotic
  equivalence and contiguity of some random graphs*, **arXiv:0802.1637**, published as **Random Struct.
  Algorithms 36:26–45 (2010)** — explicit contiguity/asymptotic-equivalence criteria for random-graph
  sequences; arXiv-available, so a directly **readable** carrier of the "contiguity of random-structure
  sequences" template. [CITE-CONFIRMED; CONTENT-UNVERIFIED]
- Wormald, contiguity results for random regular graphs (survey, *Models of random regular graphs*, 1999).
  [UNVERIFIED]

**Poisson U-statistics / Wiener–Itô chaos (the right variance calculus for iso-invariant counts on a
sprinkling):**
- Last & Penrose, *Lectures on the Poisson Process*, CUP 2017 — Poisson U-statistics, chaos expansion,
  second-moment / variance decomposition. [standard; CONTENT-UNVERIFIED — the directly applicable tool,
  since our counts are iso-invariant functionals of a Poisson point process]
- Reitzner & Schulte, *Central limit theorems for U-statistics of Poisson point processes*, **Ann. Probab.
  41(6):3879–3909 (2013), DOI 10.1214/12-AOP817, arXiv:1104.1039** — Malliavin/Wiener–Itô chaos expansion
  ⟹ exact **variance formula** for Poisson U-statistics; example application = length of a *random
  geometric graph* (a sprinkling functional, directly analogous to our interval-cardinality counts).
  [CITE-CONFIRMED; CONTENT-UNVERIFIED — arXiv-available, readable]

**Random-order / poset-specific (Brightwell formulation half):**
- Brightwell & Dowker (or Brightwell, *Models of random partial orders*, surveys) — random partial orders,
  dimension-2 (dominance) orders; relabel-invariant observables. [UNVERIFIED — Brightwell–Dowker
  "Observables in causal set cosmology" gr-qc/0210061 referenced but NOT a standalone biblioteca doc per
  comité-005 §7]
- **Kleijn & Rizzelli, *Contiguity and remote contiguity of some random graphs*, arXiv:2402.11334 (2024),
  *J. Appl. Probab.* 63(1):316–333 (2026)** (published online Aug 2025; DOI carries 2025, but the
  **volume year is 2026** — cite the volume as 2026, not 2025). [CITE-CONFIRMED — the user-identified
  random-graph contiguity paper, now pinned by exact coordinates; CONTENT-UNVERIFIED. Its abstract is
  **suggestive, not yet confirmed-applicable**: it asks *to what extent the defining parameters of a
  random-graph sequence may be perturbed without losing an asymptotic property*, and introduces **remote
  contiguity** for sequences that are not mutually contiguous. This *resembles* the COMPOSITE-family 𝒬_n
  problem forced by X₀, but **whether it is the tool we need is exactly what §7 content-verification must
  decide** — the body results use likelihood ratios built from **independent Bernoulli edges**, which do
  NOT automatically transfer to transitive (2D-dominance / DAG) causal orders. **Do not assert
  applicability before §7.**]

### 5.1 Bibliographic verification provenance (this session)
Done at HEAD `fafd880`, `main`, via `WebSearch` only (no biblioteca read, no code, no seed, sealed path
untouched). The four previously-`[UNVERIFIED]` non-textbook entries are now `[CITE-CONFIRMED]`:
Bretagnolle–Huber 1979 (Z. Wahrsch. 47:119–137); Janson 1995 (Combin. Probab. Comput. 4(4):369–405) **and
the distinct** Janson arXiv:0802.1637 (Random Struct. Algorithms 36:26–45, 2010) — two separate papers, not
an article + companion; Reitzner–Schulte 2013 (Ann. Probab. 41(6):3879–3909 / arXiv:1104.1039);
**Kleijn–Rizzelli arXiv:2402.11334 / J. Appl. Probab. 63(1):316–333 (2026)** (online Aug 2025; volume year
2026). The textbooks (Tsybakov 2009,
Le Cam 1986, van der Vaart 1998, Ingster–Suslina 2003, Janson–Łuczak–Ruciński 2000, Last–Penrose 2017) are
standard and not separately web-checked. **`CONTENT-UNVERIFIED` stands for all of them** — confirming a
paper exists does not confirm it carries the transitive-dependence/minimax machinery; that requires
reading, which is the next reversible step. Three arXiv-available items (2402.11334, 1104.1039, 0802.1637)
are the readable entry points if content-verification is authorised next.

## 6. Status

- **`X₀` RESOLVED: `COMPOSITE`.** The flat `V`-matched adversary is a *family*; the problem is
  simple-vs-composite (minimax), not the simple-pair four-case classification. The unmatched degrees of
  freedom are exactly the interval-cardinality (focusing) joint structure.
- **`X₁` REFRAMED** accordingly (minimax over 𝒬_n) and its references identified above. **comité-005 step 2
  partly done:** the four non-textbook entries are now `[CITE-CONFIRMED]` by exact coordinates (§5.1).
  **Kleijn–Rizzelli is now also CONTENT-VERIFIED — see §7.** Verdict: **`APPLICABLE_ONLY_AFTER_NEW_LIKELIHOOD_PROOF`**.
  Still pending: physically sourcing the remaining PDFs into `biblioteca/`; CONTENT-verifying the other items.
- **Next reversible step (NOT done here, NOT authorised yet):** per §7, the abstract layer (Def A.1 +
  Lemma A.2 + the Hellinger-affinity exclusion of §3.2) transfers to our laws, but **every operational
  handle needs a new transitive-dependence likelihood/affinity computation**. Options: (i) attempt that
  affinity / second-moment computation for the sprinkled-poset likelihood ratio; (ii) the
  Bretagnolle–Huber route on the least-favourable 𝒬_n member; (iii) send the §4 two-line question to a real
  external expert. **None authorised yet.**
- Freezes nothing; sealed path untouched; seal `6e2c3888…` intact; no commit.

## 7. CONTENT-VERIFICATION — Kleijn & Rizzelli, arXiv:2402.11334 (read in full this session)

> Authorised by the user as the *only* content-verification this step: extract the exact statements
> applicable to **general** measures (esp. the likelihood-ratio criterion); identify the **direction** of
> remote contiguity, the **domination** hypotheses, the role of **a_n**, **which parts require
> edge-independence**, and **what new proof** would transfer it to the composite family 𝒬_n. No minimax
> bound attempted; no expert contacted; no commit. Read via the arXiv PDF (v1, 17 Feb 2024); line-level
> anchors are to that PDF's lemma/equation numbers.

### 7.1 Exact statements that ARE measure-theoretically general (no edge-independence)
- **Definition of remote contiguity (Def. A.1).** For measurable spaces `(X_n,B_n)`, sequences
  `P_n,Q_n ∈ M₁(X_n)`, and a rate `ρ_n↓0`: `Q_n ⊳ ρ_n⁻¹ P_n` ("Q_n is ρ_n-remotely contiguous w.r.t.
  P_n") iff for every measurable `φ_n:X_n→[0,1]`, `P_nφ_n = o(ρ_n) ⟹ Q_nφ_n = o(1)`. Contiguity `Q_n ⊳ P_n`
  is the special case "for all `a_n↓0`". Stated for **arbitrary** measurable spaces — applies verbatim to
  our `X_n` = iso-classes of `n`-element posets.
- **General sufficient criterion (Lemma A.2, "remotely contiguous analogue of Le Cam's First Lemma").**
  `Q_n ⊳ a_n⁻¹ P_n` if **any** of: (ii) ∀ε>0 ∃δ>0 with `Q_n(dP_n/dQ_n < δ a_n) < ε` for large `n` [the
  practical one]; (v) under `Q_n`, every subsequence of `a_n·(dP_n/dQ_n)⁻¹` has a weakly convergent
  subsequence [the "insightful" one]; plus (i),(iii),(iv). **No independence used** — pure RN-derivative
  control.
- **General EXCLUSION criterion (subsection 3.2, stated "fully general" on p.20–21).** Via the
  `a_n`-weighted test risk `π'_n(φ)=a_n⁻¹E_{P_n}φ + E_{Q_n}(1−φ)`: **Lemma 3.6** — if some test sequence has
  `π'_n(φ_n)=o(1)` then `(P_n,Q_n)` are NOT `a_n`-remotely contiguous, and this holds **whenever the
  Hellinger affinity `α(P_n,Q_n)=o(a_n^{1/2})`**. The paper explicitly says (p.21) "the arguments of
  subsection 3.2 are fully general."
- **Domination hypothesis (Remark A.3).** Mild and standard: take any `ν_n` dominating both (e.g.
  `ν_n=(P_n+Q_n)/2`), set `p_n=dP_n/dν_n`, `q_n=dQ_n/dν_n`; `(dP_n/dQ_n)⁻¹` is defined `Q_n`-a.s. No mutual
  absolute continuity beyond a common dominating measure is required. **Our `P_n,Q_n^θ` on a common finite
  set of poset iso-classes trivially share `ν_n`** — domination is a non-issue.

### 7.2 Direction and the role of a_n (for our orientation)
- **Direction.** `Q_n ⊳ a_n⁻¹ P_n` lifts a property *known for `P_n`* (the reference, at known rate `a_n`)
  to `Q_n` (the perturbed law). To use it for **non-identifiability** we set `P_n` = the law whose
  estimator-failure rate is known and `Q_n^θ` = the adversary, and conclude no test separates **only if we
  get (near-)mutual control** (remote contiguity is *asymmetric* and *weaker* than contiguity; one-sided
  remote contiguity alone does **not** forbid a consistent test — the affinity must also stay bounded
  below).
- **Role of `a_n`.** `a_n↓0` is the **known rate** at which `P_n(A_n)→0`. Smaller `a_n` ⟹ weaker (easier)
  conclusion but requires the property to be known to hold *faster*. In the ER body, `a_n` is pinned to the
  KL-type divergence `R_n` (Lemma 3.7: `Q_n⊳a_n⁻¹P_n ⟺ a_n=o(exp(−R_n))`). **For our problem `a_n` is
  unpinned** — we have no closed-form rate for the sealed estimator's success event under `P_n`. That is an
  *additional* gap beyond the likelihood computation (matches comité-005 falsifier point 7 on the unpinned
  `ρ_n→∞` rate).

### 7.3 Which parts REQUIRE independent Bernoulli edges (the non-transferable core)
Every **operational** result is built on the product likelihood ratio of `½n(n−1)` **independent**
Bernoulli edges (eq. 5): `dP_n/dQ_n(Y_n)=∏_{i<j}(…)`. Specifically independence is load-bearing in:
- the **variance** `s_n² = Σ_{i<j} k_{n,ij}² q_{n,ij}(1−q_{n,ij})` (eq. 8) — "variance of a sum = sum of
  variances" uses edge-independence;
- the **Lindeberg–Feller CLT** (Thm. B.1) driving Lemmas 3.4/3.5 — stated for **independent** triangular
  arrays (the paper notes dependent versions "exist" but uses the independent one);
- the **factorised Hellinger affinity** `α(P_n,Q_n)=∏_{i<j}(√(p q)+√((1−p)(1−q)))` (eq. 15) — a product
  **only** because edges are independent;
- all concrete conditions (Lemmas 3.1, 3.4, 3.5, 3.7; Prop. 3.2; Cors. 3.9/3.10; the §4 domains) inherit
  this. **None of these transfers to a sprinkled poset**, whose suborder law is a transitively-dependent
  functional of a Poisson process — the relation matrix is not a product of independent edge-Bernoullis
  (the very transitive dependence the comité-005 memo §6 / audit isolate).
- The authors themselves flag this: dependence "makes the analysis more demanding technically, but the
  machinery of remote contiguity continues to apply" (p.20) — i.e. the **framework** survives, the
  **computations** must be redone. They prove **no** dependent case.

### 7.4 What new proof would transfer it to the composite family 𝒬_n
To use Kleijn–Rizzelli on our problem one must supply, for the **non-product** sprinkled-poset likelihood
ratio `dP_n/dQ_n^θ` (with `Q_n^θ` ranging over the V-matched flat family of X₀):
1. **A replacement for eq. 5/8/15 under transitive dependence** — a tractable expression or second-moment
   bound for `dP_n/dQ_n^θ` and for the **Hellinger affinity** `α(P_n,Q_n^θ)`, with the edge-independence
   product replaced by a **Poisson U-statistic / Wiener–Itô variance decomposition** (this is precisely
   where Reitzner–Schulte 2013 / Last–Penrose 2017 enter — §5).
2. **A CLT for dependent arrays** to replace Thm. B.1 (the paper points to "versions for dependent random
   variables") OR a direct second-moment/Bretagnolle–Huber route avoiding the CLT.
3. **A pinned rate `a_n`** = the known decay of the estimator-success (or focusing-detection) event under
   `P_n` (§7.2).
4. **The minimax/composite wrap** forced by X₀: for the *non-identifiable* direction it suffices to exhibit
   **one** `θ` with `α(P_n,Q_n^θ)` bounded below (no consistent test); for the *identifiable* direction one
   needs `sup_θ α(P_n,Q_n^θ)=o(a_n^{1/2})` via the §3.2 exclusion criterion — a **uniform** affinity bound
   over the family. Kleijn–Rizzelli gives the *template* for both, not the *bound*.

### 7.5 Verdict
**`APPLICABLE_ONLY_AFTER_NEW_LIKELIHOOD_PROOF`.** The paper's **abstract layer** (Def. A.1; Lemma A.2(ii)/(v);
the §3.2 Hellinger-affinity exclusion `α=o(a_n^{1/2})`; the mild Rem. A.3 domination) is genuinely
measure-theoretic and **does apply** to our `(P_n,Q_n^θ)` on poset iso-classes — so it is **not**
`NOT_APPLICABLE`. But **every operational handle** (variance `s_n²`, the Lindeberg–Feller CLT, the
factorised affinity eq. 15, and all of §3–§4) **requires independent Bernoulli edges** and therefore does
**not** transfer to the transitively-dependent sprinkled-poset law — so it is **not** `DIRECTLY_APPLICABLE`.
Using it on 𝒬_n requires the new transitive-dependence affinity / second-moment computation itemised in
§7.4 (the Poisson-U-statistic replacement of the edge product), plus a pinned `a_n`. This **confirms the
user's prior expectation** and **does not authorise** attempting that bound or contacting an expert. CONTENT
status for Kleijn–Rizzelli is now **VERIFIED**; all other §5 references remain `CONTENT-UNVERIFIED`.

— Done at HEAD `fafd880`, `main`. No code, no seed, no sealed-path execution, no new file, no commit; seal
`6e2c3888…` re-verified intact after the read.

## 8. LATENT-KL / DATA-PROCESSING AUDIT for the Bretagnolle–Huber route (reversible; no commit)

> User charge (this step, post comité-005-brief commit `aef48ce`): audit whether
> `D_KL(P_n‖Q_n^θ) ≤ D_KL(P̃_n‖Q̃_n^θ)` is legitimate via a **single, hypothesis-independent** observation
> kernel `K_n` with `P_n=P̃_n K_n`, `Q_n^θ=Q̃_n^θ K_n`. Reversible, no numeric bound, no seeds, no sim.
> Done at HEAD `aef48ce`, `main`; seal `6e2c3888…` re-verified before/after; no new file.

### 8.0 The inequality to license
Data-processing for KL: for **any** Markov kernel `K`, `D_KL(μK‖νK) ≤ D_KL(μ‖ν)`. So the target
inequality holds **iff** both observable laws are pushforwards of the latent laws through **the same**
`K_n`. The whole question is the existence of that common `K_n`. (Direction note: a KL *upper* bound feeds
**Bretagnolle–Huber** `1−TV(P_n,Q_n^θ) ≥ ½·exp(−D_KL(P_n‖Q_n^θ))`, i.e. it serves the **non-identifiable**
direction — "some flat θ mimics" — by keeping TV away from 1. It does NOT serve the identifiable
direction, which needs a TV *lower* bound / affinity argument, §7.1.)

### 8.1 Exact spaces, and what the observable is
- **Observable space `X_n`** = **isomorphism classes** of `n`-element posets (the relabel-invariant,
  order-only σ-algebra fixed by the audit / comité — `INTRINSIC_OBSERVABLE_AUDIT_NOTES.md` §3, comité-005
  §2). **Not** the labeled poset.
- **Two candidate latent spaces:**
  - **(L1) labeled order** `X̃_n^{ord}` = strict partial orders (relation matrices) on vertex set `[n]`.
  - **(L2) point configuration** `X̃_n^{cfg}` = the sprinkled point set in a 2D coordinate space — the
    *tractable* level (Poisson ⟹ closed-form KL), which is what the B–H route actually needs.

### 8.2 Generation maps under each hypothesis (written out)
- **`P_n` (Schwarzschild interior):** (a) sprinkle `{x_i}` Poisson-uniform in the `(t,r)` coordinate box
  `B_BH` (`t∈[0,6]`, `r∈[0.1,1.3]`, constant-density since the induced 1+1D metric determinant is constant,
  EGS derived-md:135); (b) assign order by the **BH light cone** built from the tortoise term
  `func = r + 2 r_S log(|r−r_S|/r_S)`, `r_S=0.5` (`generator.py:104`, `thresholds.py:40,42`); (c) project
  labeled order ↦ iso-class.
- **`Q_n^θ` (flat V-matched patch, X₀-COMPOSITE):** (a) sprinkle `{x_i}` Poisson-uniform in a flat region
  `R^θ⊂(u,v)`; (b) assign order by the **flat dominance** rule `Δu≥0 ∧ Δv≥0` (X₀ §1–2: 1+1D Minkowski
  causal order = 2D dominance); (c) project to iso-class.

**Compact form (user's framing).** `P_n = (Φ_{g_0})_# μ_{g_0,n}`, `Q_n^θ = (Φ_{g_θ})_# μ_{g_θ,n}`, where
`μ_{g,n}` is the sprinkling law of the points under geometry `g`, `Φ_g` is the **order map** (config ↦
causal order), and a fixed label-forgetting map composes after. **The crux is `Φ_{g_0} ≠ Φ_{g_θ}`** (tortoise
vs flat). A common-kernel reduction `P_n=P̃_n K_n`, `Q_n^θ=Q̃_n^θ K_n` with **one non-trivial `K_n`** is
therefore **not given** by this representation.

### 8.3 Are these the same kernel? — the decisive check
- **At the labeled→iso-class stage (L1 ⟶ X_n):** the kernel `K_n^{quot}` = quotient by the `S_n` relabeling
  action. This is a *fixed deterministic* map **independent of hypothesis** (the symmetric group acts the
  same regardless of which law produced the labeled order). ⟹ DPI through `K_n^{quot}` is **always valid**:
  `D_KL(P_n‖Q_n^θ) ≤ D_KL(P̃_n^{ord}‖Q̃_n^{ord})`. **But this is useless**: the labeled-order KL is still a
  transitively-dependent object with no Poisson closed form — no tractability gain (and labeled KL ≥
  iso-class KL anyway, consistent with DPI). This is the *trivially-valid-but-non-tractable* reduction.
- **At the config→order stage (L2 ⟶ order):** the two generation kernels **DIFFER** — `P_n` uses the
  **tortoise** causal rule on box `B_BH`; `Q_n^θ` uses the **flat** rule on region `R^θ`. Different
  deterministic functions of the configuration ⟹ **no common kernel from `X̃_n^{cfg}` as-is**. The naive
  point-process data-processing reduction is therefore **INVALID as stated**.

### 8.4 Whether a common channel CAN be constructed (the load-bearing point)
A common channel **can** be built, because **every 1+1D spacetime is conformally flat**: in double-null
coordinates `ds² = −Ω²(U,V)dU dV`, conformal maps preserve causal structure, and the causal order is again
the **2D-dominance order on `(U,V)`**. The sealed generator's tortoise term is *precisely* the construction
of BH null coordinates `U_BH=t−r_*`, `V_BH=t+r_*` with `r_*=func` (`generator.py:104`). Hence:
- Define **`Φ_BH:(t,r)↦(U_BH,V_BH)`**. Then the BH causal order of `{x_i}` **equals the 2D-dominance order
  of `{Φ_BH(x_i)}`** — the *same* rule as the flat case, now in the common `(U,V)` null plane.
- **Common kernel `K_n`** := [take 2D-dominance order in the `(U,V)` plane] ∘ [quotient to iso-class]. This
  `K_n` is **hypothesis-independent**. The hypothesis difference is pushed entirely into the **latent
  intensity**: `P̃_n` = Poisson with intensity `ρ/|J_{Φ_BH}|` on `Φ_BH(B_BH)`; `Q̃_n^θ` = Poisson with
  intensity `ρ` on `R^θ`, both in the SAME `(U,V)` plane. ⟹ `P_n=P̃_n K_n`, `Q_n^θ=Q̃_n^θ K_n` with a common
  `K_n`. ✓ — **but only after this construction is carried out and its hypotheses checked.**

**Genuine obstruction (why it is not automatic).** The box `r∈[0.1,1.3]` **straddles `r_S=0.5`**, and
`r_* = r + 2r_S log|r−r_S|` ⟹ `r_*→±∞` as `r→r_S`. So `Φ_BH` is **not a global homeomorphism**: it splits
the box at the horizon, the image `Φ_BH(B_BH)` is non-compact, and `|J_{Φ_BH}|→∞` at `r_S` ⟹ the latent
intensity `ρ/|J_{Φ_BH}|` **degenerates exactly at the horizon image**. Physically apt — the horizon is
where the latent representation becomes singular — but it means the common-channel construction needs a
real lemma, not a one-liner.

**Why the generic "absorb the geometry into the latent" move FAILS (user's correction).** The naive fix —
enlarge the latent to `(g, x_{1:n})` and set `K_n(g,x_{1:n}) = Φ_g(x_{1:n})` — does give a single
hypothesis-independent kernel, but the two latent laws then live on **different fibers of the `g`-component**
(`g=g_0` vs `g=g_θ`). For fixed distinct geometries these latent laws are **mutually singular**, so
`D_KL(P̃_n‖Q̃_n^θ)=∞` and DPI yields only the vacuous `D_KL(P_n‖Q_n^θ) ≤ ∞`. So a *useful* common channel
must **not** carry `g` as a latent coordinate; it must push the entire geometry difference into the
**sprinkling density on a shared domain with a shared order rule** — which is exactly (and only) what the
`(U,V)` null-coordinate construction attempts. This is the precise reason the identity kernel and the
expanded-space kernel are both inadmissible as the "exists" witness.

**Conformal invariance ALONE is not sufficient (user's caveat).** Even granting that `Φ_{g_0}` and
`Φ_{g_θ}` both reduce to 2D-dominance in their respective null coordinates, that does **not** by itself
guarantee that the **physically-separated horizon survives as a distinguishable parameter** inside the
common representation. The common-channel map could wash the horizon signature into a region/measure-zero
artefact, or the V-matched flat family could reproduce the resulting latent density to within the
contiguity scale (§8.7) — in which case the representation exists but is *non-identifiable*, or it may
*not* exist with `f_P ≪ f_Q^θ` at all. Whether the horizon (`r_S` / the `|J_{Φ_BH}|` blow-up) remains a
non-negligible separating feature of `f_P` versus the flat family is itself **part of what the lemma must
prove**, not a corollary of conformal flatness.

### 8.5 Unconditioned Poisson vs conditioned on `N=n` (required distinction)
- **Unconditioned** (`N∼Poisson`): latent laws are Poisson point processes; for intensities `λ_P,λ_Q^θ`
  on the common `(U,V)` plane the latent KL is the **closed form**
  `D_KL = ∫ ( λ_P log(λ_P/λ_Q^θ) − λ_P + λ_Q^θ ) \,dU\,dV` (finite iff `λ_P≪λ_Q^θ`).
- **Conditioned on `N=n`** (the sealed experiment fixes levels `n∈{1500,…}`): Poisson conditioned on total
  count `n` is **exactly** `n` i.i.d. draws from the normalized intensity `f=λ/∫λ`. By tensorization the
  latent KL is **`D_KL(P̃_n‖Q̃_n^θ) = n · D_KL(f_P ‖ f_Q^θ)`**, with
  `f_P ∝ ρ/|J_{Φ_BH}|` on `Φ_BH(B_BH)`, `f_Q^θ ∝ ρ` on `R^θ`. Clean, but **finite only if
  `supp(f_P) ⊆ supp(f_Q^θ)`** (i.e. the flat region must cover the BH null-image; V-marginal matching does
  **not** by itself guarantee this — a real condition, tied to the §8.4 non-compact image).

### 8.6 The applicable latent-KL formula (if §8.4 lemma holds, conditioned case)
`D_KL(P_n‖Q_n^θ) ≤ D_KL(P̃_n‖Q̃_n^θ) = n ∫_{(U,V)} f_P log(f_P/f_Q^θ)`, then
`1 − TV(P_n,Q_n^θ) ≥ ½ exp( − n ∫ f_P log(f_P/f_Q^θ) )`.

### 8.7 Parameter-separation condition for the physical horizon
Non-identifiability of the horizon **via this route** requires the composite family `𝒬_n` to contain a
`θ_n` keeping the latent KL `O(1)`, i.e. (conditioned) **single-point** `D_KL(f_P‖f_Q^{θ_n}) = O(1/n)`,
equivalently the flat mimic reproduces the BH null-coordinate density — *including the `|J_{Φ_BH}|` horizon
signature* — to **Hellinger distance `O(n^{−1/2})`**. Writing `θ_BH` for the (degenerate, singular)
latent intensity of the true interior and `δ_n := inf_{θ∈𝒬_n} D_KL(f_P‖f_Q^θ)`:
- `n·δ_n → 0` ⟹ TV bounded `<1` ⟹ **horizon NOT identifiable** (B–H delivers).
- `n·δ_n → ∞` ⟹ B–H upper bound vacuous; the affinity/TV-lower-bound route (§7.1) is needed; possibly
  identifiable.
So `θ_n` must approach `θ_BH` at the **contiguity scale `‖θ_n−θ_BH‖ ∼ n^{−1/2}`** in the latent metric,
*while staying inside the V-matched flat family*, for a testing lower bound to imply non-identifiability.

### 8.8 Verdict
**`VALID_ONLY_AFTER_COMMON_CHANNEL_CONSTRUCTION`.** The naive point-process reduction is **invalid as
stated** (§8.3: the config→order kernels differ — tortoise rule on `B_BH` vs flat rule on `R^θ`). The
trivially-valid labeled-order quotient (§8.3) gives the inequality but **no tractability**. A genuinely
useful common channel **does exist** — 1+1D conformal flatness ⟹ both orders are 2D-dominance orders in a
common `(U,V)` null plane via `Φ_BH` (§8.4) — **but only after constructing it and discharging the
horizon-singularity / support hypotheses**. Hence not `VALID` as-is and not `INVALID`.

**Recording rule (per user).** The "exists" branch must **NOT** be recorded on the basis of `K_n=Id`
(valid but vacuous — latent KL = the very poset-law KL, no tractability) **nor** the generic
source→detector→features analogy (that drifts into an instrumental problem foreign to causal sets). Only a
*non-trivial common channel with finite, controllable latent KL* counts as a witness.

**DPI is a positive lever, not only a warning.** Once such a channel exists, the implication is genuinely
useful: `D_KL(P̃_n‖Q̃_n^{θ_n}) ≤ C ⟹ D_KL(P_n‖Q_n^{θ_n}) ≤ C`, feeding a *positive* Bretagnolle–Huber lower
bound on the testing error `1−TV ≥ ½e^{−C}` ⟹ **horizon non-identifiable** along `θ_n`.

**Smallest new lemma required (and nothing beyond it yet) — Common-channel lemma with finite KL:**
> Construct explicitly a **common latent space**, a **hypothesis-independent kernel `K_n`**, and laws
> `P̃_n, Q̃_n^{θ_n}` whose `K_n`-images are **exactly** `P_n, Q_n^{θ_n}`, such that: (1) `K_n` is the single
> map `K_n((u_i,v_i)_{i=1}^n) = ` iso-class of the poset `{u_i≤u_j ∧ v_i≤v_j}` — a **shared domain + shared
> product-order rule**, with all geometry pushed into the sprinkling density `p_θ(u,v)` (so `g` is **not** a
> latent coordinate — avoiding the singular-fiber trap of §8.4); (2) **`P̃_n ≪ Q̃_n^{θ_n}`** with the latent
> KL **finite and controllable** — conditioned `N=n`, i.i.d.: `D_KL(P̃_n‖Q̃_n^θ)=n·D_KL(p_0‖p_θ)`;
> unconditioned Poisson: `∫[λ_0 log(λ_0/λ_θ) − λ_0 + λ_θ]dν`, given absolute continuity; (3) the explicit
> `Φ_BH:(t,r)↦(U_BH,V_BH)` (`r_*=r+2r_S log|r−r_S|`) realising (1) for the BH side, with its `r→r_S`
> singularity (`r_*→±∞`, `|J_{Φ_BH}|→∞`, non-compact image) regularized; and **(4) a proof that `θ_n` can be
> chosen inside the V-matched flat family `𝒬_n` while preserving a non-negligible separation of the physical
> horizon** (i.e. the `|J_{Φ_BH}|`/`r_S` signature is not washed out — NOT a corollary of conformal
> invariance, §8.4). Only with (1)–(4) does `P_n=P̃_n K_n`, `Q_n^θ=Q̃_n^θ K_n` hold non-trivially with finite
> latent KL, licensing §8.6.

**Next audit (per user, when authorised):** attempt **specifically** the common null-coordinate
representation with **different volume densities** `p_0,p_θ` — items (1)–(4) above — and nothing past it.

**Stop line (per charge):** do NOT yet proceed to U-statistics, dependent-array CLT, or a direct
second-moment / numeric bound. The next reversible step, if authorised, is *only* the §8.4/§8.8 common-
channel lemma (the `Φ_BH` causal-order⟺dominance proof + horizon regularization), nothing past it.

— Done at HEAD `aef48ce`, `main`. No code, no seed, no sealed-path execution, no new file, no commit; seal
`6e2c3888…` re-verified intact before and after.

## 9. COMMON-CHANNEL LEMMA AUDIT (authorised scope; reversible; no commit)

> User charge: resolve the single question — **can ALL geometric dependence be moved into the sprinkling
> measure while keeping the domain, the order rule, and the kernel-to-poset fixed?** Acceptance needs
> conditions (1)–(6) **simultaneously**; close with exactly one of four verdicts. No numeric asymptotics, no
> code/sim/seed, no new file, no commit. Done at HEAD `aef48ce`; seal `6e2c3888…` verified at start and end.

### 9.1 What DOES reduce cleanly (conditions 2,3,4, and 1-as-a-set)
- **Common order rule (cond. 2) — SOLID.** 1+1D spacetimes are conformally flat: in double-null coordinates
  `ds²=−Ω²(U,V)dU dV`, and the causal order is **conformally invariant** ⟹ for *every* geometry the order is
  the **product order** `x≺y ⟺ U_x<U_y ∧ V_x<V_y`. The sealed generator's tortoise `r_*=r+2r_S log|r−r_S|`
  (`generator.py:104`) is exactly the BH null-coordinate construction; the flat case is X₀ §1 (Mink = 2D
  dominance). So a common product-order rule with no residual `θ` is available.
- **Fixed kernel (cond. 3) — SOLID.** `K_n((u_i,v_i)) = ` iso-class of `{u_i<u_j ∧ v_i<v_j}` is one fixed
  deterministic map; the `θ`-dependence is carried by the chart `ψ_θ:D→spacetime_θ` pre-composed into the
  *latent* law, not by `K_n`. Avoids the singular-fiber trap of §8.4 (geometry `g` is NOT a latent coord).
- **Geometry into the intensity (cond. 4) — SOLID.** Sprinkling intensity in null coords is `λ_θ=ρ·Ω²_θ`
  (metric volume `√−g = Ω²`); pushing through the chart `ψ_θ` and the axis-monotone gauge `U↦f(U),V↦g(V)`
  (which preserves the product order) deposits everything into `λ_θ(U,V)` / its normalisation `p_θ`.
- **Common domain as a set (cond. 1) — available but see §9.3.** One can take `D=[0,1]²` via copula
  normalisation (uniformise each marginal). The set is common; the *supports within it* are the problem.

### 9.2 The horizon-straddling box forces a regular (Kruskal-type) chart
The sealed box is `r∈[0.1,1.3]`, which **straddles `r_S=0.5`**, and `r_*→±∞` as `r→r_S`. So in any
tortoise-based `(u,v)` chart the BH box image is **non-compact** (the `r→r_S` edges run to infinity) and
splits interior/exterior. A finite common `D` therefore requires a **horizon-regular chart** — Kruskal
`(U,V)=(∓e^{∓κ u},e^{κ v})`, `κ=1/(2r_S)` — which is product-order-preserving (monotone on each piece) and
maps the horizon to the *interior* null locus `UV=0`, where `Ω²_Kruskal` is **smooth and positive** (the
horizon is a coordinate, not curvature, singularity). So crossing `r_S` is not by itself a block.

### 9.3 The genuine wall: support / domain SHAPE (condition 5) — NOT discharged
After a horizon-regular chart, `P_n` lives on `D_BH` = the Kruskal image of the `(t,r)` box: a **curved,
geometry-specific** region with the horizon line `UV=0` threading its interior. `Q_n^θ` lives on the flat
shaped patch `R^θ`. For a *single* measurable `D` carrying *one* product order to host both with
`p_0≪p_θ`, `D_BH` and `R^θ` must be **order-isomorphic via axis-monotone maps** with compatible 2D support.
But:
- X₀ established `𝒬_n` is **COMPOSITE** and matches only the **`V`-marginal**; the `V`-marginal is a
  one-point up-set-area functional and **does not control the 2D support shape / order-iso class** of the
  region. Two regions agreeing on the `V`-marginal can be non-order-isomorphic (X₀ §2).
- The BH box's defining edges (`r=0.1` interior near the singularity-truncation, `r=1.3` exterior,
  `t∈[0,6]`) map under Kruskal to specific curves; nothing in the V-matched flat family is guaranteed to
  reproduce that boundary, so `supp(p_0)⊄supp(p_θ)` generically ⟹ `D_KL(p_0‖p_θ)=∞` (the §8.5 caveat,
  now localised to the box geometry). **Not established; concretely obstructed by the box+horizon shape.**

### 9.4 The only bypass forfeits condition 6 (the support–localisation DICHOTOMY)
One *can* force common support by mapping each geometry's region **bijectively onto `[0,1]²`** (per-`θ`
uniformisation). Then both `p_0,p_θ` have full support, KL is finite — **but the identification is
`θ`-dependent and physically scrambling**: a point `(0.5,0.5)∈D` denotes *different physical events* under
`P_0` vs `Q^θ`, so there is **no `θ`-independent readout of the horizon's location** (condition 6 fails).
This is the warned-against move (§8.8 recording rule): it is *kin to the identity-kernel vacuity* — it
buys finiteness by erasing physical meaning. Hence a **dichotomy**:
> **either** keep a physically-faithful single chart ⟹ supports incompatible (**cond. 5 fails**, §9.3),
> **or** force common support by per-`θ` uniformisation ⟹ horizon localisation lost (**cond. 6 fails**, §9.4).
There is currently **no construction satisfying (5) and (6) simultaneously**. (Note: the *focusing* contrast
— BH `Ω²` is a genuine **joint** function of `UV` vs the flat **independence** copula — does survive
uniformisation, so a *functional* separation persists; but "distinct **localisation** of the horizon," cond.
6's literal demand, does not survive the `θ`-dependent uniformisation.)

### 9.5 PPP vs `N=n` — the decisive distinction (recorded, not used to claim a verdict)
- **Conditioned `N=n`** (the sealed levels): normalisation **removes the total-intensity scale**; only the
  *spatial shape* `p_θ` survives. So a pure **global-scale** difference `λ_θ=c_θλ_0 ⟹ p_θ=p_0` is invisible
  to the conditioned poset. BH-vs-flat is **not** pure scale (the *copula* differs), so it would survive *if*
  a channel existed — but the **metric-volume** difference (`∫√−g` differs between BH box and flat patch) is
  exactly the scale that conditioning **discards**.
- **Unconditioned PPP** keeps the total-intensity term, hence strictly more information (the volume).
- **Conditional formulas (NOT licensed — verdict is not CONSTRUCTED):** *were* (5)&(6) met, then
  conditioned `D_KL(P̃_n‖Q̃_n^θ)=n·D_KL(p_0‖p_θ)`, and unconditioned
  `D_KL(PPP(λ_0)‖PPP(λ_θ))=∫[λ_0 log(λ_0/λ_θ)−λ_0+λ_θ]dν` (given `λ_0≪λ_θ`). Per charge these are recorded
  **only conditionally**, with **no asymptotic bound attempted**.

### 9.6 Verdict
**`COMMON_CHANNEL_BLOCKED_BY_SUPPORT_OR_DOMAIN`.** Conditions 2,3,4 reduce cleanly (conformal invariance ⟹
common product order; fixed kernel; geometry→intensity), and a common *set* `D` is available. But the
**physically-faithful** common channel is blocked at **condition 5**: `D_BH` (Kruskal image of the
horizon-straddling `(t,r)` box) and the V-matched flat `R^θ` are not shown order-isomorphic with compatible
support — and the `V`-marginal matching of `𝒬_n` (X₀ COMPOSITE) does not control 2D support shape. The only
bypass (per-`θ` uniformisation to `[0,1]²`) restores finiteness only by forfeiting **condition 6**
(horizon localisation), so it does not yield a CONSTRUCTED channel either. Hence not CONSTRUCTED, not
EXISTS-BUT-HORIZON-LOST as a *clean* statement (the support horn fails first), not NOT-ESTABLISHED in the
vacuous sense — the obstruction is **specifically support/domain**, with condition 6 as the coupled
secondary horn.

**Smallest next lemma (if pursued) — resolve the 5↔6 dichotomy:**
> Exhibit (or refute) an **axis-monotone order-isomorphism** `D_BH ≅ R^θ` for some `θ∈𝒬_n` such that
> (a) `supp(p_0)⊆supp(p_θ)` (finite latent KL) **and** (b) there is a **`θ`-independent functional** on the
> common `D` that recovers the horizon's *location* (not merely the focusing/joint-dependence contrast).
> A positive answer ⟹ `COMMON_CHANNEL_CONSTRUCTED` and licenses §9.5's formulas; a proof that (a) and (b)
> cannot hold together ⟹ `…_BLOCKED…` is permanent and the B–H-via-latent-KL route must instead accept the
> uniformised channel with horizon read off the **copula** (focusing), not the location.

**Stop line (per charge):** do NOT proceed to U-statistics, dependent-array CLT, or any second-moment /
numeric bound. Next reversible step, only if authorised, is the single 5↔6 dichotomy lemma above.

— Done at HEAD `aef48ce`, `main`. No code, no seed, no sealed-path execution, no new file, no commit; seal
`6e2c3888…` re-verified intact at start (§9 header) and end.

## 10. REINTERPRETATION of the §9 block (user decision) + the new minimal question

> Recorded verbatim-in-substance as the user's project-direction decision after the §9 audit. Conceptual /
> strategic; not a derived math result. Reversible, untracked, no commit, no seal touch.

### 10.1 The §9 block is a RESULT, not a failure of the central goal
§9 failed *one concrete route* (a common pre-geometric latent space preserving support, order **and the
classical horizon localisation** simultaneously). Reinterpreted, its real content is:
> **The classical horizon localisation does NOT survive as a common pre-geometric coordinate.**
This is compatible with — and probably *informs* — the existence of a *quantum/relational* horizon property.
**Condition 6 (a common functional recovering the horizon's *location*) may itself be importing into the
pre-geometric level something that should only appear in the semiclassical limit.** Before a classical
geometry exists there is no pre-existing `r` or surface to localise.

### 10.2 The clean separation the audit produced
- **Relational structure that DOES survive** (relabeling/iso-invariant, chart-free): the product order, the
  `U`–`V` dependence, **focusing**, changes in accessibility patterns. (§9.4: the focusing/joint-dependence
  contrast — BH `Ω²(UV)` vs the flat independence copula — survives uniformisation.)
- **Classical localisation that does NOT survive**: identifying "the same point/line" (`r=r_S`) across
  geometries via a common chart (§9.4 dichotomy, condition-6 horn).

### 10.3 Reframed object (supersedes the §9.6 "smallest next lemma", which is NOT authorised)
The quantum object should **not** be `H(C) = ` a localised line/subset. It should be
`𝔥(C) = ` a **relational structure of separation / trapping / loss-of-accessibility**, with localisation
**emergent**: `𝔥(C) ──(semiclassical limit)──▶ ℋ_classical`, i.e. localisation is a property of the
continuum correspondence, not of the fundamental definition.
- **Working hypothesis (user):** *the quantum precursor of the horizon may be a relational transition of
  focusing / accessibility, not a localised surface; its maximal change concentrates near the horizon in the
  semiclassical regime and produces the classical surface.* NOT yet shown to be "the horizon."

### 10.4 The new minimal question (next step — CONCEPTUAL, order-theoretic only)
> **Is there a covariant order property that detects an accessibility / focusing transition, with no
> coordinates, no embedding, and no continuum horizon given?**

Acceptance criteria for a candidate `𝔥`:
1. invariant under relabeling / poset isomorphisms;
2. defined without `r,t,U,V`, metric, or embedding;
3. needs no prior knowledge of which elements are inside/outside;
4. does not depend on matching points between two geometries;
5. absent or non-concentrated in the **flat control**;
6. concentrates semiclassically near the Schwarzschild horizon;
7. admits a formulation over **quantum histories**, not only a fixed classical poset.

### 10.5 What is NOT authorised now (explicit)
- ✗ the §9.6 order-isomorphism-with-localisation-functional lemma (the user judges the localisation demand
  conceptually misplaced);
- ✗ KL / Bretagnolle–Huber / minimax (those compare models *after* the observable is fixed; we are still
  deciding **which observable represents the horizon**);
- ✗ U-statistics, dependent CLT, second-moment, numerics, seeds.

### 10.6 Consequence for the prior PASS (re-reading, no change to any frozen result)
- Prior (prereg-002 PASS): there **is** a relational signal in the Schwarzschild-sprinkling causal order
  associated with the horizon transition — *but it is not yet known* whether it is a **fundamental** order
  property or only reflects its semiclassical **embedding**.
- §9 adds: that signal **cannot be cleanly identified as a common *position*** inside a latent space shared
  with the flat model.
- Together these **do not close** the quantum route; they **clean** it: *do not seek a quantum coordinate of
  the horizon; seek a relational transition whose localisation emerges classically.*
- **Standing caveat (founding rule):** "focusing survives uniformisation" (§9.4) shows a *chart-free
  functional separation exists*, but does **not** yet prove that separation is **intrinsic** rather than an
  embedding artefact (sources S/B/F, audit §10.2; the `relphi` outgoing-direction failure still stands).
  Criterion 5 (absent in flat control) is exactly the guardrail that must be able to fail.

— Recorded at HEAD `aef48ce`, `main`. No code, no seed, no sealed-path execution, no new file, no commit;
seal `6e2c3888…` re-verified intact.

## 11. CANDIDATE EXPLORATION — relational order predicates for a trapping/accessibility transition

> User charge (option a): reversible *conceptual* exploration, ≤3 candidates, order-relations only, each with
> the 9 fields. **Forbidden as covert rewrites:** `relphi`, continuous/discrete expansion (EGS Θ), outgoing
> direction, null coordinates, distance-to-horizon. Do NOT yet require surface localisation — identify a
> **relational transition** first. Distinguish (at least conceptually) three families: future accessibility /
> focusing-contraction / bottleneck-separation. No code/seed/file/commit. Done at HEAD `aef48ce`.
>
> **Key clarification used throughout:** the partial order's **future/past** direction is *intrinsic* to any
> poset and is NOT the forbidden "outgoing (spatial null) direction" (the thing `relphi`/EGS needed an
> embedding for). Using `J⁺`/`J⁻`, incomparability, antichains, intervals, links and Dilworth width is
> order-only. **Discriminator for trapping- vs singularity-specificity = the Hayward counterfactual**
> (audit artefact-veto 2): a regular (Hayward) BH *has* a trapped region/apparent horizon but *no*
> singularity (EGS derived-md:157,166-169,195,199); a genuine *trapping* predicate must survive it.

### 11.1 Candidate C1 — **causal bottleneck / minimal outward-flux antichain** (family: bottleneck/separation)
1. **Definition (order-only).** For an antichain `A⊂C`, let `T_A = {x : x≺a for some a∈A} ` (its past
   region) and measure the **outward causal bandwidth** `β(A) = #{links (x,y) : x∈down(A), y∉down(A)∪A}`
   normalised by `|A|` (links = covering relation, intrinsic). `C1 = ` "∃ antichain `A` whose `β(A)` is a
   pronounced local minimum — a low-bandwidth membrane separating a sub-order from the bulk." Predicate
   value = the bandwidth deficit `Δ(A) = β̄_bulk − β(A)`.
2. **Reference relational structure.** Self-calibration only: `β̄_bulk` = the causet's *own* mean
   crossing-bandwidth over generic antichains of the same `|A|` (so the baseline is order-intrinsic; no
   embedding). Quasi-local: `β(A)` is a neighbourhood functional.
3. **Why trapping / loss of accessibility.** A horizon is a one-way membrane: outward causal influence is
   suppressed, so future-directed links crossing *outward* through the trapped region's boundary antichain
   are anomalously few — a minimum of causal "bandwidth." This is accessibility-loss expressed as a cut, not
   as a coordinate.
4. **Localisation only semiclassically.** `A` is a discrete element set with no location; only when `C` is
   manifoldlike does the minimal-bandwidth antichain *concentrate* on the horizon hypersurface.
5. **Schwarzschild prediction.** A persistent low-`β` antichain bordering the trapped region (outward links
   suppressed); `Δ(A)>0` and stable across density.
6. **Flat-control prediction.** No anomalous minimum — causal bandwidth is extensive/homogeneous, so
   `β(A)≈β̄_bulk` for all cuts; `Δ≈0`.
7. **Falsifier.** Reject if flat-control sprinklings exhibit equally-low-bandwidth antichains (no separation
   of `Δ` from the flat null), OR if the minimum is an artefact of the box boundary (must subtract via the
   MINK twin with the *same* truncation).
8. **Global vs quasi-local.** Quasi-local statistic; *finding* the minimal cut may need a semi-global search.
9. **Quantum-histories event.** `β`, `Δ` are order functionals ⟹ "∃ antichain with `β<β₀`" is a
   relabel-invariant **measurable set of causets** — a covariant event over a sum-over-histories. ✓
   **Hayward check: PASSES** — the apparent horizon of a regular BH is itself a one-way membrane (outward
   flux suppressed) independent of any interior singularity ⟹ trapping-specific. **Strongest candidate.**

### 11.2 Candidate C2 — **future-overlap collapse of a wavefront antichain** (family: focusing/contraction)
1. **Definition (order-only).** For an antichain `A={a₁,…,a_m}` (a relational "wavefront": mutually
   incomparable), compare the **shared future** `S(A)=⋂_i J⁺(a_i)` to the **union future** `U(A)=⋃_i J⁺(a_i)`.
   Convergence index `κ(A)=|S(A)| / E_indep[|S(A)|]`, where `E_indep` is the value expected if the futures
   met "generically." `C2 = ` "∃ wavefront `A` with `κ(A)≫1` — initially-incomparable elements whose causal
   futures over-reconverge."
2. **Reference relational structure.** The generic/independent overlap expectation, supplied by the causet's
   own **interval-abundance statistics** (Benincasa–Dowker `C_k`, order-intrinsic; `Benincasa_Dowker_2010_…`
   in biblioteca) — not an embedding.
3. **Why trapping / focusing.** Geodesic focusing = neighbouring causal curves converge; the order analogue
   is anomalously large *common* future for a spread-out wavefront. Pure set-lattice reconvergence.
4. **Localisation only semiclassically.** `A` and `S(A)` are element sets; only when manifoldlike does the
   maximally-converging wavefront sit near the horizon.
5. **Schwarzschild prediction.** Wavefront antichains straddling the trapped region show `κ>1` (futures
   reconverge); generic wavefronts show `κ≈1`.
6. **Flat-control prediction.** `κ≈1` everywhere (no anomalous reconvergence at fixed geometry).
7. **Falsifier (load-bearing).** Reject if `κ` is driven by the **box/singularity truncation** (all futures
   merge because they hit the truncated end, not because of focusing) — *must* be subtracted via the MINK
   twin with identical truncation; if `κ_BH≈κ_MINK`, reject.
8. **Global vs quasi-local.** Quasi-local in `A`; the overlap can run deep (semi-global tail).
9. **Quantum-histories event.** `κ(A)` is an order functional; "∃ wavefront with `κ>κ₀`" is a covariant event
   over histories. ✓ **Distinct from forbidden EGS expansion:** uses only set-overlap of antichain futures —
   *no* predistance, *no* reference ladder, *no* spatial radius, *no* in/out split. **Hayward check: PASSES
   in principle** (focusing is generic to trapping, present for Hayward) *iff* the truncation confound (§7)
   is removed. **Well-posed, with a mandatory truncation control.**

### 11.3 Candidate C3 — **future width-collapse / "long-thin future"** (family: future accessibility) — EXAMINED, REJECTED
1. **Definition (order-only).** For a sub-order `T`, accessibility deficit `w(T) = width(J⁺(T)) / |J⁺(T)|`
   where `width` = Dilworth maximum-antichain size of the future (intrinsic "transverse extent"). `C3 = `
   "∃ `T` whose future is **long and thin**: large `|J⁺|`, small `width` ⟹ `w` anomalously low." Genuinely
   distinct from the already-used `V=|J⁺|` (adds the Dilworth-width dimension).
2. **Reference relational structure.** Bulk `width/|J⁺|` ratio (self-calibrated).
3. **Why trapping.** A captured future fails to "re-spread" — a thin causal tube rather than a spreading cone.
4–6. Localisation emergent; Schwarzschild → low `w` in the trapped region; flat → generic `w`.
7. **Falsifier / fatal flaw.** A "long-thin future" is *exactly* what the **singularity truncation**
   produces (everything funnels into the truncated end), so `C3` tracks the singularity, not trapping.
   **Hayward check: FAILS** — a regular BH has a trapped region but *no* funnel, so `width` does not collapse
   there ⟹ `C3` is **singularity-specific, embedding-/truncation-driven** (audit §4.3 artefact-veto-2;
   `PR003_INFO_BOUND_NOTES.md:136`). **REJECTED as not trapping-intrinsic.**
8–9. (Moot.) Would be quasi-local + a covariant event, but the family yields only this artefact-prone form.

### 11.4 Cross-cutting assessment
- **Hayward counterfactual is the clean discriminator:** C1 and C2 survive it (one-way membrane / focusing
  exist for regular BHs); C3 fails it (needs the singularity funnel). So the **future-accessibility family,
  defined order-only, collapses into a singularity artefact** — an honest negative for that family.
- **Standing intrinsicality caveat (kept ACTIVE, per user):** C1 and C2 being order-only and well-posed does
  **not** prove their signal is *intrinsic* rather than a semiclassical-embedding shadow; surviving
  uniformisation (§9.4) or Hayward is *necessary, not sufficient*. The flat-control falsifiers (C1 §7, C2 §7)
  are the guardrails that must be able to fail — none may be waived. (Recall `relphi` *passed* a global AUC
  yet failed robustness; an unfalsified-but-untested predicate is decoration.)
- **What "ready for committee" means here:** two well-posed, order-only, non-forbidden candidates (C1, C2)
  with explicit falsifiers exist and are adjudicable — *not* that either is confirmed.

### 11.5 Verdict
**`CANDIDATE_SET_READY_FOR_COMMITTEE`.** Two well-posed relational candidates survive — **C1 (causal
bottleneck / minimal outward-flux antichain; bottleneck family; strongest, passes Hayward)** and **C2
(future-overlap collapse of a wavefront antichain; focusing family; passes Hayward iff the truncation
control holds)** — both order-only, none a rewrite of `relphi`/expansion/outgoing/null-coords/horizon-
distance, each with a flat-control falsifier and a quantum-histories formulation. The **future-accessibility
family yields only C3**, which the Hayward counterfactual rejects as singularity-specific. The intrinsicality
caveat remains active: readiness = adjudicable, not proven.

**If (b) is authorised:** the committee question is *which of C1/C2 should become the project's horizon
observable* (or whether to merge them: a bottleneck **whose** crossing wavefront also over-converges). The
committee must attach, as binding, the flat-control separation test and the Hayward counterfactual to any
candidate it advances; nothing is sealed or run here.

— Recorded at HEAD `aef48ce`, `main`. No code, no seed, no sealed-path execution, no new file, no commit;
seal `6e2c3888…` re-verified intact before and after.

## 12. CLOSED DEFINITION of C1 (per comité-006 = REFINE; user chose "Close C1 in writing")

> Scope: comité-006 (`docs/comite/comite_decision_006_…md`, verdict `RECOMMEND_REVISE_AND_RECONVENE` =
> `REFINE_CANDIDATES_BEFORE_PROMOTION`) §9 step 1. Reversible analytic closure of C1 only; **C2 left open**
> (user's choice). NO code, seed, sim, run, freeze, or commit. Every degree of freedom is pinned to a
> **principled, data-independent** value so there is no latent post-hoc DOF (warden §6 condition). This is
> the closed *form*; its actual freeze + an independent blind falsification are the **reconvene** step, NOT
> done here. Done at HEAD `aef48ce`; seal `6e2c3888…` re-verified before/after.

### 12.1 The five binding fixes (comité-006) this section must discharge
(a) replace "outward" with an order-only forward-flux across an order ideal; (b) a **closed** antichain/cut
search class chosen on principled grounds, not from data; (c) "pronounced local minimum" made a quantitative
order functional with a **pre-committed comparator**; (d) defeat the leaky-cut / missing-link bypass
(Surya :886); (e) the **selection** (argmax), not only the statistic, must be relabel-invariant.

### 12.2 Order-only primitives (every symbol derived from `≺`)
Finite causet `C=(E,≺)`, strict partial order. All of the following are relabel-invariant:
- **Height** `h(x)` = number of elements in the longest chain ending at `x` (intrinsic discrete proper time;
  Myrheim/Brightwell — the longest-chain functional the project already uses). Occupied heights
  `1..H = max_x h(x)`. Level `L_k = {x : h(x)=k}` (an antichain).
- **Level down-set** `D_k = {x : h(x) ≤ k}` — a genuine **order ideal** (down-set: `x∈D_k, w≺x ⇒ w∈D_k`),
  order-canonical, no embedding. The family `{D_k}_{k=1..H-1}` is a totally-ordered **intrinsic foliation**.
- **Forward-crossing flux** `Φ(D_k) = #{(x,y) : x∈D_k, y∉D_k, x≺y}` — **counts the full order relation, NOT
  the covering relation**. (This is fix (d): because every relation that crosses the cut is counted, the
  Surya :886 "missing-link bypass" — a past element linked to a future element *skipping* the interface
  antichain — cannot deflate `Φ`; nothing bypasses a full-relation cut. The leaky-cut pathology is specific
  to counting *covers/links* across an inextendible antichain; we count relations across a down-set.)
- **Interface width** `w(D_k) = |L_k| = |{x : h(x)=k}|` (the maximal elements of `D_k` are exactly `L_k`) —
  an order-only "area" of the cut.
- **Specific forward bandwidth** `b_k = Φ(D_k) / w(D_k)` — forward-crossing relations per interface element.

### 12.3 The closed C1 predicate (deterministic, seed-free)
- **Self-calibration without an MC null (removes the seed DOF entirely).** Restrict to bulk levels
  `K = {k : the k-th occupied-height decile is neither the bottom nor the top decile of [1,H]}` (boundary
  layers excluded; the 10%/90% cut is **pre-committed** and data-independent). Set
  `β̄_bulk = median_{k∈K} b_k`, `s_bulk = 1.4826 · median_{k∈K}|b_k − β̄_bulk|` (robust MAD scale).
- **Membrane score** `z_k = (β̄_bulk − b_k) / s_bulk` (a level whose forward bandwidth dips below the
  foliation's own robust centre). This makes cuts of different size/depth **comparable** (fix (c)/axis 3):
  `z` is dimensionless and self-normalised.
- **Predicate (pre-committed comparator):** `C1(C) = 1` iff `max_{k∈K} z_k ≥ z*`, with **`z* = 3`** pinned
  now as the standard robust-outlier bound (3 MAD), a principled, data-independent threshold — NOT tuned to
  any sprinkling. The **membrane locus** is `k* = argmax_{k∈K} z_k`; ties broken by **smallest k**, then by
  the lexicographically-smallest multiset of heights of `L_{k}` — **never by element label** (fix (e):
  `h`, `K`, `b_k`, `z_k`, and the tie-break key are all functions of `≺` alone, so both the predicate value
  and the selected `k*` / `L_{k*}` are relabel-invariant).
- **What "outward" became (fix (a)):** the predicate contains **no spatial direction**. `Φ` is the
  *temporally-forward* relation count escaping an order ideal `D_k` — the future/past asymmetry is intrinsic
  to `≺`; the forbidden object (the spatial *outgoing-null* leg that `relphi`/EGS needed an embedding for)
  never appears. A low-`b_k` level is "a slice of intrinsic time across which forward causal influence per
  interface element is anomalously suppressed."

### 12.4 The 8 axes, re-checked against the CLOSED form
1. **Intrinsicality** — PASS: `h, L_k, D_k, Φ, w, b, β̄_bulk, s_bulk, z, z*, k*` are all `≺`-functionals.
2. **Orientation** — PASS: only the intrinsic forward direction is used; no "exterior" label (fix a).
3. **Normalisation** — PASS: `z_k` self-normalises across size/depth via the foliation's robust median/MAD;
   no external scale.
4. **Hayward** — PASS in principle: a regular BH's apparent horizon still suppresses forward escape across
   the trapped slices, with no singularity required (EGS md:157,166-169,195,199). To be *confirmed*, not
   assumed (axis 8).
5. **Flat control** — a genuine rejector: in a flat MINK sprinkling the foliation is homogeneous, so
   `b_k ≈ const` ⇒ `max z_k < z*` ⇒ `C1=0`. If a flat twin yields `C1=1`, C1 is falsified.
6. **Truncation** — partially handled, residual risk named: the bottom/top-decile exclusion drops the box's
   temporal end-caps; but a `b_k` dip could still sit on the `r=0.1` (near-singularity) spatial edge rather
   than `r_S`. **Binding control:** the MINK twin must use the **same point cloud + same box**, and `C1`
   must fire on BH but not on the twin (the dip must be causality-induced, not box-induced).
7. **Quantum covariance** — PASS: `C1(C)∈{0,1}` (and the real-valued `max_k z_k`) is a relabel-invariant
   functional of the order ⇒ `{C : max_k z_k ≥ z*}` is a measurable set of causets, a covariant event over
   histories.
8. **Semiclassical correspondence** — the *prediction*, not part of the definition: whether `k*` (the
   membrane slice) concentrates near `r=r_S` as the sprinkling becomes manifoldlike is to be **tested**
   through the frozen path, never built in.

### 12.5 Falsifier carried into the closed form
- **Minimal test (unchanged in spirit, now concrete):** on `DEV_SEEDS`, one BH + one MINK twin (same cloud,
  same box): compute `{b_k}`, `{z_k}`, `C1`. (i) Relabel-conjugate the input and re-compute — `k*` and `C1`
  must be invariant (Guard-v on the *selection*, fix e); any change ⇒ leakage, C1 fails before any physics.
  (ii) `C1_BH=1 ∧ C1_MINK=0` is the pass; `C1_MINK=1` or `C1_BH=0` falsifies. (iii) Record whether `k*`
  sits at a box end-cap rather than the interior (truncation artefact).
- **Honest residual (the genuine modelling assumption, now FROZEN not tunable):** the search class is the
  **height foliation** `{D_k}`. A horizon is not obviously a constant-height slice, so this class *may*
  miss a membrane that is "vertical" in intrinsic time — in which case `C1` simply returns 0 and **is
  falsified for this geometry**, which is the correct, non-tunable outcome. A richer order-canonical search
  class (e.g. down-sets generated by future-deficient antichains) is a *different* closed candidate to be
  written and frozen separately — NOT a post-hoc widening after seeing `C1=0`.

### 12.6 Status
- **C1 is now a CLOSED, falsifiable, order-only, relabel-invariant, seed-free definition** (§12.2–12.3),
  discharging fixes (a)–(e). Intrinsicality caveat stays ACTIVE: closed + Hayward-passing-in-principle is
  NECESSARY, not SUFFICIENT — only the flat-control/Hayward/truncation tests (axes 5,6,4) can produce a real
  rejection, and they must be able to fail.
- **NOT done (needs explicit authorisation + reconvene):** C2 re-posing (still open); any dev probe; freezing
  `z*`/the decile rule/the search class into a prereg; promoting C1 as the project axis; an independent
  *blind* falsification pass (required by the independent-falsification gate before any promotion). No
  commit of this note as a result.

— Recorded at HEAD `aef48ce`, `main`. No code, no seed, no sealed-path execution, no new file, no commit;
seal `6e2c3888…` re-verified intact before and after.
