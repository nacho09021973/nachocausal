# Finite causal-set geometric indeterminacy

## Program synthesis — identifiability track (WP3/WP4)

**Status:** `INTEGRATED_SYNTHESIS`

**Normative status:** This is not a preregistration, protocol, implementation authorization,
or run authorization. It does not modify, reinterpret, or delay the frozen PR010 protocol.
PR010 must be closed under its own rules before any empirical certification step derived
from this document is opened.

**Integration base:** commit `11ef1d64d72a337bfdc8723e917a3477c171a825` (verified descendant of
`c43dc070b912d9340919c41d5b42e6d88e751854`).

**Audit terminal (2026-07-14):** `MATHEMATICAL_AUDIT_PASS_WITH_CONDITIONS` — theorems sound;
integrated here by deduplicating against existing WP4 proofs and anchoring Schwarzschild
instantiation to refutations already in the repo.

**Relation to frozen results:** This document closes the *programmatic* framing of the item
**OPEN — minimax floor over `C`** in `docs/preregistration_003.md` §7. It does **not** amend
`prereg-003` (★): the sealed operational floor `O(ℓ)` for the future-volume channel remains a
layer-(1) estimator bound, not a universal minimax statement.

**Repo anchors (do not re-prove here):**

| Topic | Authoritative file |
|---|---|
| Two-point / Le Cam theorem (PROVED) | `research_program/work_packages/wp4_two_point_theorem.md` |
| Exact blindness witness (Theorem A, PROVED) | `research_program/models/first_witness_pair_candidates.md` §2 |
| Fisher regularity + diamond-family floor (PROVED) | `research_program/work_packages/wp4_fisher_localization_floor.md` |
| Taxonomy layers (1)/(2)/(3) | `research_program/taxonomy/identifiability_taxonomy.md` |
| Certification tiers | `research_program/work_packages/wp3b_identifiability_criteria.md` |

**Not a PR-series artifact:** Do not number this track as PR011. Empirical certification, if
opened later, requires its own preregistration after PR010 closes.

## 1. Research question

For a finite causal set observed only through its unlabeled causal order and cardinality,
what geometric resolution is achievable by the best possible order-only estimator?

The proposed object is not a Heisenberg uncertainty relation between noncommuting operators.
It is an information-theoretic lower bound caused by a finite stochastic observation channel:

```text
Lorentzian geometry
    -> finite Poisson sprinkling
    -> unlabeled causal order plus cardinality
    -> order-only estimator
```

The scientific hypothesis is that geometrically different spacetimes may induce identical or
nearly identical laws on finite unlabeled causal sets. If so, no order-only estimator can
reconstruct the differing geometric target uniformly with arbitrarily small error.

## 2. Scope and exclusions

This synthesis concerns classical finite causal sets. It does not claim:

- a quantum uncertainty relation;
- a canonical position-momentum pair;
- measurement disturbance or operator noncommutativity;
- a universal no-go theorem for all continuum observables;
- that failure of PR009, PR010, or any other estimator proves indeterminacy;
- reconstruction of a global event horizon from an unspecified finite patch;
- any result in 3+1 dimensions.

The first defensible target is a scalar geometric parameter in a tightly restricted 1+1D
Schwarzschild family. Set-valued reconstruction and 3+1 transfer are later extensions.

## 3. Admissible geometries

Let `G` be a class of finite-volume, causally well-behaved Lorentzian regions. Before any
theorem is applied scientifically, `G` must freeze:

1. dimension;
2. topology and regularity assumptions;
3. boundary and continuation conditions;
4. allowed metric family and parameter range;
5. total-volume treatment;
6. sprinkling density;
7. whether the analysis is unconditional or conditional on cardinality;
8. the target geometric functional and its metric.

Without these restrictions, non-identifiability can be made trivial by hiding an arbitrarily
large geometric change in an arbitrarily small-volume region or beyond the observed patch.

## 4. Finite order-only observation law

For `g in G`, let

```math
X_{g,\rho} \sim \operatorname{PPP}(M_g,\rho\,d\operatorname{vol}_g)
```

be a Poisson point process of density `rho` on the finite region `M_g`. The induced causal set is

```math
C_{g,\rho}=\operatorname{Ord}_g(X_{g,\rho}).
```

Only its isomorphism class `[C]` is observed. Cardinality is retained because number is intrinsic
causal-set information. Let

```math
P_{g,\rho}=\operatorname{Law}([C_{g,\rho}])
```

be the probability law on the countable space of finite unlabeled posets.

Two admissible observation models are possible, but one must be frozen before use:

- **Unconditional:** observe `[C]`, including random cardinality `N`.
- **Fixed-cardinality:** condition on `N=n`, producing `P_{g,n}` on isomorphism classes of
  `n`-element posets (the channel in which `wp4_two_point_theorem.md` is proved).

For shape or horizon-location questions, admissible geometries should have equal expected
volume, or the analysis should condition on `N`, so that total cardinality does not solve the
problem by a trivial volume leak (`wp4_two_point_theorem.md` Obs. 5.2).

### 4.1 Composite adversaries

If matching a marginal (for example future-volume `V`) does not **uniquely** determine the
generating law `Q_n`, the adversary is a **composite** family of measures, not a simple
hypothesis. The two-point bounds below apply after fixing a simple pair `(P,Q)` or after
stating a **uniform** bound over the composite class (minimax over adversaries). See
`docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md` §5 (minimal
test on well-posedness of `Q_n`).

## 5. Geometric target and estimator

Let

```math
T:G\longrightarrow(\Theta,d_\Theta)
```

be a diffeomorphism-invariant geometric target with values in a metric space. An order-only
estimator is any function on isomorphism classes (randomized estimators: `wp4_two_point_theorem.md`
Obs. 5.1)

```math
\widehat T:\mathcal C_{\mathrm{fin}}/{\simeq}\longrightarrow\Theta.
```

On a finite sample space all such maps are measurable; relabeling invariance is exact.

Its risk at `g` is

```math
R_g(\widehat T)
=
\mathbb E_{C\sim P_{g,\rho}}
\left[d_\Theta\!\left(\widehat T(C),T(g)\right)\right].
```

The minimax risk over the full allowed estimator class is

```math
\mathcal R_\rho^*(G,T)
=
\inf_{\widehat T}
\sup_{g\in G}
R_g(\widehat T).
```

This is the quantity needed for an estimator-independent (taxonomy layer-(3)) claim. The
performance of one chosen observable is not a substitute for it.

### 5.1 Ensemble vs single-instance

Bounds on `R_g` and on classification error are **ensemble** statements: they hold in
expectation over the sprinkling law. They do **not** imply that one realized finite causal set
permits inference at the same precision (Poisson fluctuation, finite-`n` boundary sensitivity).
See `wp4_two_point_theorem.md` Obs. 5.4 and `wp3b_identifiability_criteria.md` §4.

## 6. Two-geometry indeterminacy — proved core and metric extensions

Choose `g_0,g_1 in G` and define

```math
\Delta_T=d_\Theta\!\left(T(g_0),T(g_1)\right),
\qquad
\varepsilon_\rho=\operatorname{TV}\!\left(P_{g_0,\rho},P_{g_1,\rho}\right),
```

with

```math
\operatorname{TV}(P,Q)=\sup_A|P(A)-Q(A)|
=\frac12\sum_c|P(c)-Q(c)|.
```

### 6.1 Proved two-point bound (authoritative: `wp4_two_point_theorem.md` §3)

For every order-only estimator `f` on a fixed channel (e.g. conditioned on `N=n`):

```math
P_{g_0,\rho}\!\left(f(C)\neq T(g_0)\right)
+
P_{g_1,\rho}\!\left(f(C)\neq T(g_1)\right)
\geq 1-\varepsilon_\rho,
```

with **equality** for the likelihood-ratio test. Immediate consequences (same file, §3):

```math
\max_{i\in\{0,1\}} P_{g_i,\rho}\!\left(f(C)\neq T(g_i)\right)\geq\frac{1-\varepsilon_\rho}{2}.
```

**Boundary case:** if `TV = 1-2\alpha`, a balanced test can achieve error exactly `\alpha` under
both models; strict inequality is required for a strict impossibility claim at level `\alpha`.

### 6.2 Metric-risk corollaries (extension of §6.1; same reduction)

For any estimator `\widehat T` and any metric `d_\Theta`, the nearest-target test implies:
if the binary test errs under `g_i`, then `d_\Theta(\widehat T(C),T(g_i))\geq\Delta_T/2`. Hence

```math
\max_{i\in\{0,1\}}
P_{g_i,\rho}\!\left(
d_\Theta\!\left(\widehat T(C),T(g_i)\right)\geq\frac{\Delta_T}{2}
\right)
\geq\frac{1-\varepsilon_\rho}{2},
```

and, using `\mathbb E[d]\geq(\Delta_T/2)\,P(d\geq\Delta_T/2)`,

```math
\mathcal R_\rho^*(G,T)\geq\frac{\Delta_T}{4}(1-\varepsilon_\rho).
```

**Scientific content** is not these reductions (standard Le Cam). It is exhibiting admissible
pairs with meaningful `\Delta_T` and **certified** small `\varepsilon_\rho`.

## 7. Geometric indeterminacy modulus

Define

```math
\omega_\rho(\varepsilon;G,T)
=
\sup_{\substack{g,h\in G\\
\operatorname{TV}(P_{g,\rho},P_{h,\rho})\leq\varepsilon}}
d_\Theta(T(g),T(h)).
```

This is the largest geometric difference hidden within an `\varepsilon`-indistinguishable class
of finite order laws. From §6.2,

```math
\mathcal R_\rho^*(G,T)\geq\frac{1-\varepsilon}{4}\,\omega_\rho(\varepsilon;G,T).
```

For confidence level `1-\alpha`, define the minimax confidence radius

```math
r_{\rho,\alpha}^*
=
\inf_{\widehat T}
\inf\left\{
r:\sup_{g\in G}
P_{g,\rho}\!\left(d_\Theta(\widehat T(C),T(g))>r\right)
\leq\alpha
\right\}.
```

For **`0<\alpha<\tfrac12`** (so `1-2\alpha>0`),

```math
\boxed{
r_{\rho,\alpha}^*
\geq
\frac12\,
\omega_\rho(1-2\alpha;G,T)
}
```

with the usual limiting interpretation if the supremum is not attained. At `\alpha=\tfrac12` the
boxed bound is vacuous; at equality `TV=1-2\alpha` the strict impossibility clause of §6.1
applies.

In words: the best guaranteed geometric resolution is at least half the geometric diameter that
can remain hidden inside statistically indistinguishable finite-order laws.

## 8. KL and information corollaries

If a certified calculation gives `D_{\mathrm{KL}}(P_{g_0,\rho}\Vert P_{g_1,\rho})\leq\kappa`, then
Pinsker gives `TV\leq\sqrt{\kappa/2}` and

```math
\mathcal R_\rho^*(G,T)\geq\frac{\Delta_T}{4}\left[1-\sqrt{\kappa/2}\right]_+.
```

Certification routes: `wp4_two_point_theorem.md` Obs. 5.3; data processing is valid only when
the statistic is a provable function of the latent draw on a **common** probability space.

### 8.1 Fisher analogy — sketch only

For a regular one-parameter family, one may define order-only Fisher information
`I_{\mathrm{ord},\rho}(\theta)` and motivate `\delta\theta\sqrt{I_{\mathrm{ord},\rho}(\theta)}\gtrsim 1`
under QMD. This is an analogy, not a quantum commutator theorem.

**Do not invoke `\sqrt{n}` rates without proving regularity.** The repo already contains:

- **Degeneracy:** fixed Kruskal box ⇒ `I\equiv 0` (`wp4_fisher_localization_floor.md` Prop. 1);
- **Non-regularity:** fixed EF coordinate box ⇒ support motion, floor `O(1/n)` (Props. 2–3);
- **Proved regular family:** causal diamonds with fixed EF corners ⇒ floor
  `O(1/\sqrt{n\bar I})` and structural `O(\ell)` form via `\kappa=V\cdot\bar I` (§5–5a of that
  annex).

KL bounds on sprinkled posets with transitive dependence require a validated variance
decomposition; edge-independence does not transfer automatically
(`docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md`).

## 9. Schwarzschild instantiation — anchored to WP4

A one-parameter Schwarzschild family `G_{\mathrm{Sch}}` and target `T(g_M)=R_H(g_M)=2M` are the
right *first scalar* problem, but **patch and coordinates must be frozen** independently of PR009
or PR010 outcomes.

### 9.1 Instantiations already in the repo (do not rediscover)

| Construction | Target | TV / information | Regime |
|---|---|---|---|
| Fixed Kruskal box, scale orbit | absolute `r_s` | `TV=0` exact | **C** (Theorem A) |
| Fixed EF `(v,r)` box | `tau=2M` | non-regular; floor `O(1/n)` | not `1/\sqrt{n}` |
| Causal diamonds, fixed EF corners | `tau` in range | proved `1/\sqrt{n\bar I}` floor | **B** candidate |

See `first_witness_pair_candidates.md` §2 (Theorem A) and `wp4_fisher_localization_floor.md`
§§2–5.

### 9.2 What remains for a fresh `G_{\mathrm{Sch}}` freeze

Equal-volume or fixed-`N` discipline; explicit mass interval; boundaries and continuation;
independence from sealed estimator outcomes. Any certified bound

```math
\operatorname{TV}(P_{M_0,\rho},P_{M_1,\rho})\leq\varepsilon
```

implies `\mathcal R_{\rho,H}^*\geq|M_1-M_0|(1-\varepsilon)/2` via §6.2. Scalar localization
should precede set-valued horizon subsets.

## 10. Set-valued extension

After the scalar case, an order-only estimator may return `\widehat H(C)\subseteq C`. The hidden
embedding may be used only by the scorer to define a truth band, e.g.
`H_{\kappa,\rho}(X,g_M)=\{x\in X:|R(x)-2M|\leq\kappa\ell_\rho\}` with `\ell_\rho=\rho^{-1/d}`.

A general set-valued lower bound requires a decision-theoretic formulation over the joint latent
law of `(C,H_{\mathrm{truth}})`. It must not be obtained by informally substituting a random
target into the scalar theorem.

## 11. Global event-horizon caveat

The global event horizon is teleological. Two global continuations agreeing on the observed finite
patch but differing outside induce the same order law inside the patch while having different
global horizons — a trivial exact no-go.

Nontrivial finite-patch questions require either:

1. freeze global continuation (known Schwarzschild family); or
2. target a local horizon-associated or trapped-surface functional within the observed region.

No finite-patch result may silently switch between these targets (`docs/preregistration_003.md`
§2; EGS; comité 005).

## 12. Three scientifically distinct regimes

The scaling of `\omega_\rho` separates three claims.

### A. Finite-density indeterminacy

`\omega_\rho(\varepsilon)>0` for finite `\rho`, and `\omega_\rho(\varepsilon)\to 0` as
`\rho\to\infty`. Limited resolution at finite density; asymptotically recoverable.

### B. Intrinsic order-only resolution floor

`\liminf_{\rho\to\infty}\omega_\rho(\varepsilon)>0`. Irreducible ambiguity as density increases
within the frozen class. **Partial instance:** diamond family floor in `wp4_fisher_localization_floor.md`.

### C. Exact order-only blindness

`P_{g,\rho}=P_{h,\rho}` with `T(g)\neq T(h)`. Strongest no-go; requires an explicit pair.
**Instance:** Theorem A (`first_witness_pair_candidates.md` §2), `TV=0` with different absolute
`r_s` on the scale orbit.

## 13. Acceptable certification routes

An indeterminacy claim requires an **upper bound** on statistical distinguishability:

1. **Explicit coupling** with correct marginals;
2. **Analytic KL bound** with justified common channel and data processing;
3. **Exact finite-`N` enumeration** with certified numerical error;
4. **Rigorous approximation theorem** before using a surrogate law.

Simulation may discover pairs or falsify a proposed bound; it cannot alone certify a no-go at
production `N` (`wp3b_identifiability_criteria.md` §7).

## 14. Evidence that is explicitly insufficient

The following do not establish geometric indeterminacy:

- failure of one observable or finite collection thereof;
- classifier at chance or failure to optimize a classifier;
- overlapping histograms, timeouts, insufficient coverage, absence of significance;
- post-hoc pair discovery;
- algorithms that do not exhaust the full order `\sigma`-algebra.

A successful classifier **falsifies** exact blindness. An unsuccessful one supplies **no** certified
TV upper bound without approximation guarantees.

## 15. Minimal future research unit

After PR010 is independently completed and closed, the smallest defensible unit is specified as
**PR011 (viability)** in `research_program/synthesis/pr011_mass_distinguishability_viability.md`:

1. freeze the causal-diamond EF family `G_◊` and target `τ = 2M` (§9.2; not Kruskal / scale orbit);
2. channel: order-only conditioned on `N = n`;
3. theory-anchored mass pair without PR009/PR010 inputs;
4. certify `TV(P_n(τ_0), P_n(τ_1))` (or prove `TV = 0`) at tractable `n`;
5. emit a viability terminal (§8 of that spec) — **not** a mass-estimation result.

Scaling, estimation prereg, and confirmation bands are **later** units, gated on PR011
`PAIR_DISTINGUISHABLE_AT_TRACTABLE_N`.

No 3+1 claim until scalar viability resolves in the controlled 1+1 family.

## 16. Decisions required before preregistration

Deliberately unresolved:

- exact admissible mass interval and patch/continuation;
- unconditional vs fixed-cardinality observation;
- density or cardinality ladder; scalar loss and confidence level;
- pair-selection rule; certification method; numerical error budget;
- development and confirmation bands; stopping rule and compute budget;
- whether the first terminal is finite-density only or asymptotic scaling.

None may be selected using unpublished PR009 or PR010 scientific contents.

## 17. Draft terminal vocabulary

Placeholders for a later freeze document:

- `NONTRIVIAL_FINITE_ORDER_LOWER_BOUND_ESTABLISHED`
- `EXACT_ORDER_ONLY_BLINDNESS_ESTABLISHED`
- `TARGET_RECOVERABLE_AT_TESTED_RESOLUTION`
- `INCONCLUSIVE_DISTINGUISHABILITY_CERTIFICATION`
- `INVALID_MODEL_CLASS_OR_TARGET`
- `FAILED_DATA_CONTRACT`
- `FAILED_RUNTIME`

No label may be emitted until thresholds, precedence, and evidence contract are separately frozen.

## 18. Program interpretation

Reconstruction and indeterminacy are not competing narratives:

```text
constructive upper bound: an estimator attains error <= delta
information lower bound: no estimator can attain error < delta_min
```

If both hold at comparable scales, the program identifies the actual finite order-only resolution
of the geometric target — stronger than either a single successful estimator or a single failed
observable.

Pair with `prereg-002` (recoverability upper bound) and `prereg-003` (operational floor (★) on
the sealed channel); this synthesis targets the OPEN minimax-over-`C` item without reinterpreting
(★) as intrinsic.

## 19. Primary sources

1. Luca Bombelli, *Statistical Lorentzian geometry and the closeness of Lorentzian manifolds*,
   J. Math. Phys. 41 (2000), 6944–6958. <https://arxiv.org/abs/gr-qc/0002053>
2. Mehdi Saravani and Siavash Aslanbeigi, *On the Causal Set-Continuum Correspondence*, Class.
   Quantum Grav. 31 (2014), 205013. <https://arxiv.org/abs/1403.6429>
3. Olaf Muller, *On the Hauptvermutung of Causal Set Theory*, arXiv:2503.01719 (rev. 2026).
4. David Rideout and Petros Wallden, *Spacelike distance from discrete causal order*, Class.
   Quantum Grav. 26 (2009), 155013. <https://arxiv.org/abs/0810.1768>

Standard statistics (Le Cam, Tsybakov): cited in `wp4_two_point_theorem.md` §7; source into
`biblioteca/` before external memos rely on them.

## 20. Integration record

Independent mathematical audit (2026-07-14): constants and TV convention verified; measurability
on finite iso-classes OK; cardinality conditioning load-bearing; global-horizon caveat OK;
PR010 non-interference OK; deduplication against `wp4_two_point_theorem.md` required — applied
in §6.

**Current terminal:**

```text
INTEGRATED_SYNTHESIS — NOT_READY_FOR_PR_NUMBERING_OR_PREREGISTRATION
```