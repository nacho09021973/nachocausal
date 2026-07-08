# First witness-pair candidates — WP4 §10 instantiation attempts

> **Working draft, REVISABLE, not frozen.** This document attempts to instantiate the
> counterexample templates of `research_program/models/canonical_counterexamples.md` (§5, §10)
> using the machinery of `research_program/work_packages/wp4_two_point_theorem.md` (Teorema 2 /
> two-point bound). It contains mathematics only: no simulations were run, no PR004 output was
> used, no estimator (sealed or otherwise) is evaluated, and no empirical claim is made. All
> statements are at **fixed `n`, order-only channel, conditioned on `N = n`** unless explicitly
> labeled otherwise.
>
> Results: **one PROVED exact pair (Theorem A, modest content, absolute-units target), one rate
> bound FAILED as stated and repaired + PROVED in the annex
> `research_program/work_packages/wp4_fisher_localization_floor.md` (Theorem B; see §3
> CORRECTION), one FAILED attempt (Attempt C, with the obstruction stated exactly).**

## 1. Setup and preparatory lemmas

Throughout: a completion `theta` is a pair (1+1D spacetime patch `(P_theta, g_theta)`, Poisson
sprinkling of intensity `rho` with respect to `vol(g_theta)`), observed as the induced unlabeled
finite poset. `T_loc(theta)` denotes the horizon location; `T_ex(theta) in {0,1}` denotes horizon
existence.

**Lemma 0 (cardinality handling).** Conditioned on `N = n`, the `n` sprinkled points are i.i.d.
with law `vol(g_theta) / vol(g_theta)(P_theta)` on `P_theta`.

*Proof.* Standard property of Poisson processes: given the total count on a set with finite
intensity measure `mu`, the points are i.i.d. from `mu / mu(P)`. ∎

All comparisons below condition both models on `N = n`, so the Poisson cardinality leak
(`wp4_two_point_theorem.md` Obs. 5.2) is closed by construction; where the leak re-opens in a
stronger channel, it is flagged explicitly (§2, Remark A3).

**Lemma 1 (copula reduction; null-box patches).** Let `(P, g)` be a 1+1D patch that is a
coordinate box `D = I x J` in global null coordinates `(U, V)` in which `g = -Omega(U,V) dU dV`
with `Omega` continuous and positive on `D`. Then:

1. the causal order on `D` is the coordinatewise product order: `p` precedes `q` iff
   `U(p) <= U(q)` and `V(p) <= V(q)` (future-directed causal curves have `dU >= 0`, `dV >= 0`;
   conversely, for a product domain the coordinate segment joining such `p, q` is a causal curve
   inside `D`);
2. the law of the unlabeled `n`-point poset under Lemma 0 sampling depends on `(P, g)` **only
   through the copula** `c` of the normalized measure `Omega dU dV / (its total mass)` — i.e.,
   only through the joint law of the coordinate ranks.

*Proof of (2).* With a continuous positive density, all `U`-values and all `V`-values are a.s.
distinct. The poset is the intersection of the two rank orders, hence a function of the
permutation matching `U`-ranks to `V`-ranks; the law of that permutation is exactly what the
copula determines. Increasing reparametrizations `U -> phi(U)`, `V -> psi(V)` change marginals but
not ranks, so any two models with the same copula induce the same poset law at every `n`. ∎

**Lemma 2 (dilation covariance of 1+1D Schwarzschild).** Let
`g_{r_s} = -(1 - r_s/r) dt^2 + (1 - r_s/r)^{-1} dr^2` and let `Phi_s : (t, r) -> (st, sr)` for
`s > 0`. Then `Phi_s^*( g_{s r_s} ) = s^2 g_{r_s}`.

*Proof.* Direct computation: at `(t,r)`, with `t' = st, r' = sr`,
`-(1 - s r_s / (s r)) s^2 dt^2 + (1 - r_s/r)^{-1} s^2 dr^2 = s^2 g_{r_s}`. ∎

Since a constant conformal factor does not change causal structure, and volume forms in 2D scale
as `vol(s^2 g) = s^2 vol(g)`, `Phi_s` maps the normalized sampling measure of the `r_s` model on a
patch `P` to that of the `s r_s` model on `Phi_s(P)`, preserving all causal relations.

## 2. Theorem A — exact witness pair for absolute horizon location (PROVED)

**1. Candidate pair.**
`theta_H = ` (1+1D Schwarzschild with horizon radius `r_s`, patch `P`, conditioned `N = n`);
`theta_H' = ` (1+1D Schwarzschild with horizon radius `s r_s`, patch `Phi_s(P)`, conditioned
`N = n`), for any fixed `s > 0, s != 1`. The patch `P` is arbitrary (it may straddle the horizon
and include the singularity-truncated interior); no null-box assumption is needed.

**2. Target.** `T_loc(theta) = r_s` in absolute units. `T_loc(theta_H) = r_s != s r_s =
T_loc(theta_H')`. (Both models have `T_ex = 1`; existence is **not** the target here.)

**3. Channel.** Order-only, fixed `n`.

**4. Cardinality handling.** Both models conditioned on `N = n` (Lemma 0).

**5. Closeness bound.** `TV( P_n(theta_H), P_n(theta_H') ) = 0` **exactly, for every `n`**.

*Proof.* By Lemma 2, `Phi_s` is a diffeomorphism from `P` to `Phi_s(P)` pulling `g_{s r_s}` back
to `s^2 g_{r_s}`. It preserves causal order (constant conformal factor) and maps the normalized
volume measure of `theta_H` to that of `theta_H'` (the `s^2` scaling cancels under
normalization). By Lemma 0, the `n` i.i.d. sample of `theta_H'` is the `Phi_s`-image in law of the
`n` i.i.d. sample of `theta_H`, with identical induced causal relations. Hence the unlabeled poset
laws are equal. ∎

**6. Verdict: PROVED.**

By `wp4_two_point_theorem.md` Teorema 2 with `TV = 0`: for every order-only estimator `f`, the sum
of error probabilities is `>= 1`. Since `s` ranges over `(0, infinity)`, the entire one-parameter
orbit `{ theta : r_s in (0, infinity) }` carries a single poset law: **the observed finite order
carries zero information about `r_s` in absolute units, at every fixed `n`.**

**Remark A1 (honest content assessment).** This formalizes, as an exact WP4-§10 witness pair, the
known CST slogan that order alone carries no scale ("Order + Number", bibliography matrix §2.2).
It is not a new physical discovery; its value is that WP4 §10's checklist is now satisfied once,
end to end, at evidence tier 1 (pair named, target named, distance = TV computed exactly, regime =
all fixed `n`, proof supplied).

**Remark A2 (what it does NOT kill).** Any *relative* localization target — horizon position in
units of the discreteness scale `ell`, of the patch size, or of `sqrt(n)` — is invariant under
`Phi_s` and is untouched by this pair. In particular this theorem does **not** contradict
`prereg-002` (which scores localization in units of `ell`) and does not activate any stop rule of
`canonical_counterexamples.md` §6. Its one binding governance consequence: **fine-localization
claims must always be stated in relative units**; absolute-unit claims are now theorem-backed as
impossible in this channel. The repo already complies.

**Remark A3 (channel leak, quantified).** In the order + cardinality channel with known
fundamental `rho`, the pair is distinguishable through `N` alone: `N ~ Poisson(rho V)` vs
`Poisson(rho s^2 V)`, whose Bhattacharyya affinity is `exp( -(sqrt(lambda) - sqrt(lambda'))^2 / 2 )`,
so discrimination becomes reliable once `|s - 1|` exceeds order `1/sqrt(rho V)` ~ `1/sqrt(n)`.
Scale is a Number observable, with `sqrt(n)`-precision — the two channels are cleanly separated by
this pair.

## 3. Theorem B — rate bound for relative horizon localization (PARTIAL)

> **CORRECTION (2026-07-08, post-audit annex — supersedes this section's family).** The
> fixed-Kruskal-box family below is **degenerate**: in Kruskal coordinates
> `Omega_t(U,V) = 16 t^2 e^{-x(UV)} / x(UV)` with `x(UV)` mass-independent, so the normalized
> measure, the copula, and the poset law do not depend on the mass parameter at all —
> `I(t) = 0` identically, and hypothesis (H)'s clause `0 < I` is **false**. The family is
> Theorem A's scale orbit in disguise (Kruskal coordinates pin the horizon at `U = 0` for every
> mass; the horizon does not move relative to the box). Theorem B **as stated below FAILS for
> this family**. The repaired construction — a causal-diamond family with fixed
> Eddington-Finkelstein corners, for which regularity is proved and the `1/sqrt(n)` floor is
> **PROVED** — is in `research_program/work_packages/wp4_fisher_localization_floor.md`. The text
> below is retained unedited for the record.

**1. Candidate pair (family).** Fix a compact null box `D` in Kruskal-type null coordinates
`(U, V)`, away from the singularity, and a family of metrics `g_t = -Omega_t(U,V) dU dV` on `D`,
where `t` in a compact interval `[t_0, t_1]` parametrizes the horizon location within the fixed
box (mass parameter in the Kruskal conformal factor). The pair is `(theta_t, theta_{t+delta})`
for small `delta`. Because the box is fixed while the horizon moves, `t` is a **relative**
location target — exactly what Theorem A leaves open.

**2. Target.** `T_loc(theta_t) = t`, with `T_loc(theta_t) != T_loc(theta_{t+delta})`.

**3. Channel.** Order-only, fixed `n`.

**4. Cardinality handling.** Both conditioned on `N = n`.

**5. Closeness bound (proved chain, modulo hypothesis (H)).** Let `c_t` be the copula density of
the normalized measure `Omega_t dU dV` on `D` (Lemma 1).

**(H)** *(unverified analytic hypothesis)*: the family `{ c_t }` is `L^2`-differentiable in `t`
with Fisher information `I(t) = int (d/dt log c_t)^2 c_t` bounded by `Ibar < infinity` on
`[t_0, t_1]`.

Under (H), the following chain is proved:

1. `H^2( c_t, c_{t+delta} ) <= (delta^2 / 4) * Ibar`
   (Cauchy-Schwarz on `sqrt(c_u)` along the path: `(sqrt(c_{t+delta}) - sqrt(c_t))^2 <=
   delta * int_t^{t+delta} (d_u sqrt(c_u))^2 du`, then integrate over the box).
2. Tensorization: `H^2_n := H^2( c_t^{ox n}, c_{t+delta}^{ox n} ) = 2( 1 - (1 - H^2/2)^n )
   <= n H^2`.
3. Data processing (poset is a function of the `n` copula samples, Lemma 1):
   `TV( P_n(theta_t), P_n(theta_{t+delta}) ) <= H_n <= (delta/2) sqrt( n Ibar )`.
4. Two-point conclusion (`wp4_two_point_theorem.md` Teorema 2 + the standard estimation-to-testing
   reduction): no order-only estimator `t_hat` can satisfy
   `P( |t_hat - t| >= delta/2 ) <= epsilon` under both `theta_t` and `theta_{t+delta}` whenever
   `(delta/2) sqrt(n Ibar) < 1 - 2 epsilon`. Hence a localization floor
   `delta_n = Theta( 1 / sqrt(n Ibar) )` at fixed `n`.

**Conditional scaling corollary** (flagged: rests on (H) *plus* an unverified scaling input). If
the family is taken in the one-scale regime where the box scales with `r_s` — so that
dimensional analysis gives `Ibar = kappa / r_s^2` with `kappa` dimensionless, and
`n = rho V = rho gamma r_s^2` — then the floor becomes

`delta_n ~ ell / sqrt( gamma kappa )`,

i.e. **a lower bound of order `ell`** for relative horizon localization, valid even for estimators
that see full coordinates (the bound is at the point-process level; order-only estimators inherit
it by data processing). If this corollary were completed, it would be the first intrinsic-level
statement quantitatively consistent with the operational `O(ell)` floor of `prereg-003`. It is
**not** completed here, and `prereg-003`'s floor remains instrument-level.

**6. Verdict: PARTIAL.**
Proved: steps 1-4 of the chain, given (H). Not proved: (H) itself — plausible on a compact box
away from the singularity, where `Omega_t` is smooth, positive, bounded above and below, and
smooth in `t`, so the copula density and its `t`-score should be bounded (the missing steps are
routine but genuinely unwritten: differentiability in `t` of the marginal quantile maps, and
square-integrability of the score); also not computed: the constants `kappa, gamma` of the scaling
corollary. Two further honesty notes: (i) the bound controls estimators with access to full point
coordinates, so it cannot capture any *additional* weakness specific to the order-only channel —
it is valid but possibly loose for posets; (ii) it is a two-point bound only — no matching upper
bound (no estimator achieving `O(1/sqrt(n))`) is claimed.

## 4. Attempt C — horizon-existence pair (FAILED)

**1. Candidate pair sought.** `theta_H` = Schwarzschild-type patch containing a horizon (Family
A); `theta_noH` = curved or flat non-horizon patch (Family B), with
`P_n(theta_H) approx P_n(theta_noH)` at fixed `n`.

**2. Target.** `T_ex(theta_H) = 1 != 0 = T_ex(theta_noH)`.

**3-4. Channel / cardinality.** Order-only, fixed `n`, both conditioned on `N = n`.

**5. Why the attempt fails — exact obstruction.** Two structural facts:

- **Exact equality is blocked by a rigidity observation.** For null-box models (Lemma 1 setting),
  equal copulas mean the normalized measures `Omega dU dV` agree after increasing
  reparametrizations of `U` and `V` — but such a reparametrization, with the Jacobian absorbed
  into `Omega`, is precisely a change of null coordinates, i.e. an isometry up to a global
  constant scale. In 2D the metric `-Omega dU dV` is determined by its area measure in null
  coordinates, so **same copula implies isometric up to global scale** — and an isometry cannot
  turn a horizon-free patch into a horizon-containing one. Exact (`TV = 0`) existence-witnesses
  of Theorem A's kind therefore do not exist in this class: the `TV = 0` equivalence class of a
  completion is exactly its scale orbit.
- **Approximate closeness cannot be certified by the only available tool.** Our sole technique
  for *upper-bounding* poset-law distance is data processing from the point-level laws (Lemma 1 +
  step 3 of Theorem B). For two **fixed** distinct geometries, the copula Hellinger gap is a fixed
  `h_0 > 0` (by the rigidity fact above), and tensorization then forces the point-level distance
  to grow: `H^2_n = 2(1 - (1 - h_0^2/2)^n) -> 2`. So the data-processing route yields a useless
  bound (`TV <= something -> 1`) precisely in the regime of interest. Crucially, this does **not**
  prove the poset laws separate — data processing gives upper bounds only, and the poset-level
  `TV` could in principle remain far below the point-level `TV`. What fails is the *proof
  technique*: we have no tool that upper-bounds poset-level `TV` strictly below the point-level
  bound. This is exactly the open item 2 of `wp4_two_point_theorem.md` §6 ("Abierto").

**6. Verdict: FAILED** (no concrete pair with a quantitative indistinguishability argument for
`T_ex` at fixed geometries and fixed `n`).

> **Post-study note (2026-07-08, after reading Müller 2025 — `biblioteca/2503.01719v2.pdf`).**
> Müller's Theorem 2 (finite Hauptvermutung false for `d^-`) both **confirms and partially
> unblocks** this section. Confirms: his witness pairs are `K`-dependent (bump volume
> `v ~ log(1/epsilon)/K`), exactly matching the structural conclusion above that fixed distinct
> geometry pairs separate and fixed-`n` witnesses need `n`-dependent geometry. Unblocks: his
> **small-volume conformal-bump mechanism** (confine the geometric difference to a region the
> `K`-sample misses with probability `> epsilon`) is a published technique for keeping fixed-`K`
> order-law distance small without any Fisher regularity — a candidate route to a
> horizon-existence witness at fixed `n` (item 4 below). The obstruction statement above stands
> for **fixed** pairs; the "no tool" phrasing should be read as scoped to that case. See
> `wp4_fisher_localization_floor.md` §9 for the full comparison.

**7. Next weakest theorems that might be provable.**

1. **SUPERSEDED by the annex.** This item originally proposed completing (H) on an explicitly
   parametrized Kruskal box family as "routine real analysis". That is now refuted: Proposition 1
   of `research_program/work_packages/wp4_fisher_localization_floor.md` shows `I = 0` identically
   on the Kruskal box family (the copula is mass-independent), so (H) is false there and cannot be
   completed. The valid repair is the corrected causal-diamond family with fixed EF corners, for
   which regularity and the `1/sqrt(n)` floor are proved in that annex.
2. **A closed-form non-geometric toy pair** (Family C design pattern, WP3 §5: a geometric model
   vs a poset-growth model matched on selected order statistics) where the copula or the poset
   law itself is computable exactly at small `n` — provable but of limited geometric meaning.
3. **An asymptotic contiguity conjecture** (explicitly a separate, asymptotic statement, not
   fixed-`n`): for horizon shifts `delta_n = c / sqrt(n)` in the Theorem B family, the sequences
   `P_n(theta_t)` and `P_n(theta_{t + delta_n})` are mutually contiguous. This is the standard
   LAN-type expectation given (H); it is stated here only as a conjecture.
4. **A Müller-style bump witness for horizon existence** (added post-study, 2026-07-08): adapt
   the small-volume conformal-bump mechanism of Müller 2025, Theorem 2
   (`biblioteca/2503.01719v2.pdf`) to create or destroy a horizon-like/trapping structure inside
   a region of volume `v ~ 1/n`, giving an `n`-dependent pair with `T_ex` differing and
   fixed-`n` order-law distance `< epsilon`. Open questions to settle before this is a theorem:
   whether a volume-`v` perturbation can change `T_ex` under Family A/B's definitions (a horizon
   is a global structure; Müller's target, timelike diameter, is changed by a thin tube — a
   horizon may need more volume), and whether the pair remains within the named WP3 families.

## 5. Summary

| Attempt | Target | Distance result | Verdict |
|---|---|---|---|
| A — dilation pair | `r_s` in absolute units | `TV = 0` exactly, all `n` | **PROVED** (content: order-only carries no scale; formal, modest) |
| B — fixed-box shifted horizon | `t` = relative horizon location | family shown DEGENERATE (`I = 0`, see §3 CORRECTION); floor `1/sqrt(n Ibar)` PROVED on the repaired diamond family (annex `wp4_fisher_localization_floor.md`) | **FAILED as stated; repaired and PROVED in annex** |
| C — existence pair | `T_ex` horizon vs no horizon | no bound obtained; technique-level obstruction identified | **FAILED** |

Against the `canonical_counterexamples.md` §10 checklist: Theorem A satisfies items 1-5 (with the
distance identically zero); Theorem B satisfies items 1-3 and half of 4 (the bound is conditional
on (H)); Attempt C fails item 4.

Governance (`canonical_counterexamples.md` §6): no stop condition for PR004 is triggered.
Theorem A adds one binding constraint — localization claims must be in relative units — with
which the repo's existing `d_perp / ell` convention already complies.

## 6. Non-goals

This document does not assert: that horizon existence is identifiable (Attempt C's failure is a
failure of proof technique, not evidence of identifiability); that the `O(ell)` operational floor
of `prereg-003` is intrinsic (Theorem B's scaling corollary is doubly conditional); that any
estimator achieves the Theorem B rate; any empirical result. No simulations were run; no PR004
output was read or used; the sealed estimator was not touched.
