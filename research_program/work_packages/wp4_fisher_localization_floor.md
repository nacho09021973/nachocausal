# Annex — Fisher regularity and the order-only localization floor (Theorem B resolution)

> **Working draft, REVISABLE, not frozen.** This annex resolves the status of hypothesis (H) of
> `research_program/models/first_witness_pair_candidates.md` §3 (Theorem B). Mathematics only: no
> simulations, no PR004 output, no estimator evaluation, no empirical claim.
>
> **Headline verdicts.**
> - (H) for the family of record (fixed Kruskal box, mass parameter): **FAILED — refuted in
>   closed form. Fisher information is identically zero; the family is degenerate** (it is the
>   scale orbit of Theorem A in disguise).
> - (H) for the naive repair (fixed Eddington–Finkelstein coordinate box): **FAILED — the family
>   is non-regular** (support motion; Hellinger distance is first order in the shift, not second).
>   A weaker floor of order `1/n` survives.
> - (H) for the corrected family (causal-diamond family with fixed EF corners): regularity and
>   finite Fisher information **PROVED**; the `1/sqrt(n)` localization floor on this family is
>   **PROVED**. Strict positivity `I(tau) > 0` at every `tau` remains open (it is not needed for
>   the floor). The physical `Omega(ell)` reading remains open.
>
> Taxonomy labels (taxonomy §10): object = horizon-location parameter of a 1+1D family; task =
> localization lower bound; evidence level = intrinsic (laws, not estimators); claim type =
> theorem/proof on a named family; what it does NOT show — see §7.

## 1. The model of record and what must be checked

`first_witness_pair_candidates.md` §3 defined Theorem B on: a fixed compact null box `D` in
Kruskal coordinates `(U, V)`, metrics `g_t = -Omega_t(U,V) dU dV` with `t` the mass parameter,
sampling conditioned on `N = n` (i.i.d. from the normalized volume measure, Lemma 0 there),
observation = unlabeled poset, order-only channel. Hypothesis (H) demanded: the copula family
`{c_t}` is `L^2`-differentiable with Fisher information `0 < I(t) <= Ibar < infinity`.

Formally, with `H^2(p,q) := int (sqrt(p) - sqrt(q))^2` (range `[0,2]`; the alternative convention
`h^2 = H^2/2` turns the expansions below into `h^2 = delta^2 I/8 + o(delta^2)`), (H) is:
differentiability in quadratic mean (QMD) of `tau -> c_tau` with

`H^2( c_tau, c_{tau+delta} ) = (delta^2 / 4) I(tau) + o(delta^2), 0 < I(tau) < infinity.`

## 2. Refutation for the family of record (Proposition 1)

**Proposition 1 (degeneracy).** On a fixed Kruskal box `D`, the normalized volume measure of the
1+1D Schwarzschild metric is independent of the mass parameter. Hence the copula, and by Lemma 1
of `first_witness_pair_candidates.md` the poset law at every `n`, are mass-independent, and
`I(t) = 0` identically.

*Proof.* Kruskal coordinates for mass `M` (horizon radius `tau = 2M`) satisfy
`UV = (1 - r/2M) e^{r/2M}` with conformal factor `Omega_M = (32 M^3 / r) e^{-r/2M}`. Substitute
`x := r/2M`. The constraint becomes `UV = (1 - x) e^x`, so `x = x(UV)` is the same function of
`UV` for every `M`. Then

`Omega_M(U,V) = (32 M^3 / (2 M x)) e^{-x} = 16 M^2 * e^{-x(UV)} / x(UV).`

The `M`-dependence is a global constant factor `16 M^2`, which cancels on normalization. ∎

**Reading.** The "horizon location within the fixed box" intuition of the original §3 was wrong:
Kruskal coordinates are scale-invariant and pin the horizon at `U = 0` for every mass. Fixing a
Kruskal box is exactly the covariant-patch choice of Theorem A; the family is the scale orbit,
carries zero information, and the clause `0 < I` of (H) is **false**. (Consistency check: this
makes the whole family an exact `TV = 0` continuum, which is Theorem A restated — the target that
differs along it is absolute `r_s` only; the horizon does not move relative to the box.)

## 3. The naive repair fails differently: fixed coordinate box (Propositions 2-3)

The natural repair is to pin the patch to coordinates **not** adapted to the horizon. Take
ingoing Eddington-Finkelstein (EF) coordinates `(v, r)`,

`g_tau = -(1 - tau/r) dv^2 + 2 dv dr`,

which cover the horizon smoothly; note `det g = -1`, so the volume measure is `dv dr` — uniform
on any fixed `(v,r)`-box `B = [0,T] x [r_a, r_b]`, for every `tau`. The `tau`-dependence enters
only through the causal order. Global null coordinates exist (see §4): `Ṽ = v` and
`Ũ = -e^{-v/(2tau)} W_tau(r)` with `W_tau(r) := e^{r/tau} (r/tau - 1)`, which is smooth and
strictly increasing (`W' = r e^{r/tau} / tau^2 > 0`).

**Proposition 2 (non-regularity; sketch).** The image of the uniform law on `B` in `(Ũ, v)`
coordinates has support `S_tau = { (Ũ, v) : v in [0,T], Ũ in -e^{-v/(2tau)} [W_tau(r_b), W_tau(r_a)] }`,
whose boundary curves move at nonzero speed in `tau` (for generic `r_a, r_b`), while the density
is bounded below by a positive constant up to the boundary. Consequently, for small `delta`,

`H^2( p_tau, p_{tau+delta} ) >= c_1 |delta|`

(one law assigns zero and the other at least a fixed positive density on a region of area
`asymp |delta|`). Hellinger is **first order** in the shift: QMD fails, the Fisher information of
the family is not defined as a finite quadratic form, and the expansion of §1 is false. ∎ (sketch)

This is the classical support-parameter phenomenon (cf. `Uniform[0, theta]`): the family is
non-regular, and `1/sqrt(n)` is not the natural two-point scale.

**Proposition 3 (consolation floor, order `1/n`).** For the fixed-box family, with densities
bounded above and boundary speed bounded, `TV( p_tau, p_{tau+delta} ) <= C |delta|`; hence by the
coupling bound `TV( p_tau^{ox n}, p_{tau+delta}^{ox n} ) <= n C |delta|`, data processing to
posets, and the two-point theorem: no order-only estimator can localize `tau` in this family to
precision better than order `1/(C n)` at fixed `n`. ∎ (proof: elementary chain as stated; the
boundary-motion constant `C` is finite by smoothness of `W_tau` in `tau` on compacts)

Honesty note: for support families, point-level estimation at rate `1/n` is typically *possible*
(extreme-order statistics), so this floor may be tight at the point level; whether the poset-level
channel attains it is unknown (data processing gives upper bounds on distinguishability only).

## 4. The corrected family: causal diamonds with fixed EF corners

**Construction.** Fix `0 < r_q < tau_0 <= tau_1 < r_p` and `v_p < v_q`. Let
`p = (v_p, r_p)` (exterior) and `q = (v_q, r_q)` (interior) be fixed points of the EF chart, and
for `tau in [tau_0, tau_1]` let the patch be the causal diamond
`D_tau := J^+_tau(p) ∩ J^-_tau(q)`.

*Null coordinates.* Outgoing null curves of `g_tau` satisfy `dv = 2 dr / f`, i.e.
`u := v - 2 r*_tau(r)` constant, `r*_tau = r + tau ln| r/tau - 1 |`. Define globally

`Ũ := -e^{-v/(2 tau)} W_tau(r), W_tau(r) = e^{r/tau} ( r/tau - 1 ),`

smooth across the horizon. Verification that `Ũ` is null: along `dr = (f/2) dv`,
`dŨ = e^{-v/(2tau)} [ (W/(2tau)) dv - W' dr ]` and
`W' f / 2 = ( r e^{r/tau} / tau^2 ) * ( (r - tau)/r ) / 2 = e^{r/tau} (r/tau - 1) / (2 tau) = W/(2 tau)`,
so `dŨ = 0` exactly. Along future ingoing null curves (`dv = 0`, `dr < 0`), `dŨ > 0`. Hence
`(Ũ, v)` is a global double-null chart on `r > 0` and the causal order is the product order.

*Diamond as null box.* `q in J^+_tau(p)` for every `tau in [tau_0, tau_1]`: `v_q > v_p` and
`Ũ_q > 0 > Ũ_p` (since `W_tau(r_q) < 0 < W_tau(r_p)` for `r_q < tau < r_p`). The diamond is the
coordinate box `[Ũ_p, Ũ_q] x [v_p, v_q]`, nonempty, straddling the horizon `Ũ = 0`. Its minimal
`r`-value over the closed box is `r_q > 0`: the singularity is avoided automatically, and `r`
ranges over a compact subinterval of `(0, infinity)`, uniformly over `tau in [tau_0, tau_1]`.

*Sampling density.* The volume measure `dv dr` pushes to the null box with density

`h_tau(Ũ, v) = e^{v/(2tau)} / ( A_tau * W'_tau( r_tau(Ũ, v) ) ) = e^{v/(2tau)} tau^2 / ( A_tau * r e^{r/tau} ) |_{r = r_tau(Ũ,v)},`

where `r_tau(Ũ,v) = W_tau^{-1}( -e^{v/(2tau)} Ũ )` and `A_tau` is the normalizing area.

**Lemma R (regularity).** On the closed box, uniformly over `tau in [tau_0, tau_1]`:
(i) `r_tau(Ũ,v)` is jointly smooth in `(Ũ, v, tau)` (implicit function theorem; `W' > 0` bounded
below on the compact `r`-range); (ii) `h_tau` is jointly smooth and bounded above and below by
positive constants; (iii) the marginal densities `m_1(Ũ; tau), m_2(v; tau)` (integrals of `h_tau`
over box slices) are smooth in all arguments and bounded below (differentiation under the
integral sign with dominated, smooth, bounded integrands); (iv) the marginal quantile maps are
`C^1` in `(x, tau)` (inverse function theorem, densities bounded below); (v) therefore the copula
density

`c_tau(x, y) = h_tau( F_tau^{-1}(x), G_tau^{-1}(y) ) / [ m_1( F_tau^{-1}(x); tau ) * m_2( G_tau^{-1}(y); tau ) ]`

is jointly continuous, `C^1` in `tau`, bounded above and below by positive constants, with
`|d/dtau c_tau|` bounded — hence the score `d/dtau log c_tau` is bounded uniformly. ∎
(Each step is elementary calculus on a compact domain with explicit smooth functions; nothing is
assumed beyond the formulas above.)

**Proposition 4 (Fisher finiteness and QMD).** `I(tau) = int (d/dtau log c_tau)^2 c_tau` is
finite and continuous on `[tau_0, tau_1]`; set `Ibar := sup I(tau) < infinity`. The family is
differentiable in quadratic mean, and

`H^2( c_tau, c_{tau+delta} ) = (delta^2 / 4) I(tau) + o(delta^2)`,

with the uniform integrated bound (no expansion needed)

`H^2( c_tau, c_{tau+delta} ) <= delta * int_tau^{tau+delta} ( I(s)/4 ) ds <= ( delta^2 / 4 ) Ibar.`

*Proof.* Boundedness of score and `c` (Lemma R) gives finiteness and continuity of `I`. QMD
follows from the standard sufficient criterion (pointwise `C^1` in the parameter plus finite,
continuous Fisher information — e.g. van der Vaart, *Asymptotic Statistics*, Lemma 7.6). For the
integrated bound: `sqrt(c_tau(x))` is `C^1` in `tau` with derivative `(d c/dtau)/(2 sqrt(c))`
bounded, so by Cauchy-Schwarz along the parameter path
`( sqrt(c_{tau+delta}) - sqrt(c_tau) )^2 <= delta int_tau^{tau+delta} ( d_s sqrt(c_s) )^2 ds`;
integrate over the unit square and use `int (d_s sqrt(c_s))^2 = I(s)/4`. ∎

**On strict positivity (open).** `I(tau) > 0` at every `tau` is **not proved here**. What is
available: (a) *Dichotomy*: for any `tau != tau'`, either `c_tau != c_{tau'}` (the family is
informative at that pair), or `c_tau = c_{tau'}`, in which case `(theta_tau, theta_{tau'})` is an
**exact `TV = 0` witness pair for relative horizon location** — an even stronger result than the
floor. Either branch serves the program; the floor theorem below needs neither. (b) If
`c` were `tau`-independent on a subinterval, the copulas there would coincide pairwise; ruling
this out reduces, via the rigidity remark of `first_witness_pair_candidates.md` §4 (same copula on
a null box implies isometric up to global scale) and the fact that a causal isomorphism must map
the diamond's order-minimum `p` and order-maximum `q` to each other, to an explicit monotonicity
check on dimensionless corner invariants (e.g. `R tau^2 |_p = 2 (tau / r_p)^3` is injective in
`tau` at fixed `r_p`, which already blocks pure scale maps). Completing that check is left open;
`I(tau) = 0` is in any case impossible on a whole subinterval unless the exact-witness branch of
the dichotomy fires there.

## 5. The localization floor on the corrected family (Theorem, PROVED)

**Theorem (order-only two-point localization floor).** For the diamond family of §4, every `n`,
every `tau, tau + delta in [tau_0, tau_1]`, and every (possibly randomized) order-only estimator
`tau_hat = f(C_n)`:

1. `TV( Q^n_tau, Q^n_{tau+delta} ) <= (|delta|/2) sqrt( n Ibar )`, where `Q^n_tau` is the poset
   law at `n` points conditioned on `N = n`;
2. consequently `P_tau( |tau_hat - tau| >= |delta|/2 ) + P_{tau+delta}( |tau_hat - (tau+delta)| >= |delta|/2 ) >= 1 - (|delta|/2) sqrt( n Ibar )`;
3. hence no order-only estimator localizes `tau` to precision `|delta|/2` with confidence
   `1 - epsilon` at both endpoints whenever `|delta| < 2 (1 - 2 epsilon) / sqrt( n Ibar )`:
   a localization floor of order `1 / sqrt( n Ibar )` at fixed `n`.

*Proof.* (1) Chain: Proposition 4 gives `H^2( c_tau, c_{tau+delta} ) <= (delta^2/4) Ibar`;
Hellinger tensorization `1 - H^2_n/2 = (1 - H^2/2)^n` gives `H^2_n <= n H^2`; the poset is a
function of the `n` copula samples (Lemma 1 of `first_witness_pair_candidates.md`; the diamond is
a null box, so the lemma applies), so by data processing and `TV <= H`
(`wp4_two_point_theorem.md` Obs. 5.3), `TV( Q^n ) <= H_n <= sqrt(n) * (|delta|/2) sqrt(Ibar)`.
(2) The estimation-to-testing reduction: the test "nearest endpoint to `tau_hat`" errs only if
`tau_hat` is at distance `>= |delta|/2` from the truth; apply Teorema 2 of
`wp4_two_point_theorem.md`. (3) Immediate from (2), with the strict inequality as per the audited
consequence 2 of that note. ∎

**What the theorem quantifies over.** All functions of the observed unlabeled poset (randomized
included), at the stated fixed `n`, in the order-only channel, both models conditioned on
`N = n`. The bound holds a fortiori because it already holds at the point-process level; it can
therefore be loose for posets, and it says nothing about what any estimator *achieves*.

## 6. What remains open

1. **`I(tau) > 0` pointwise** (§4): open; not needed for the floor; the dichotomy is proved.
2. **The physical `Omega(ell)` reading**: the scaling corollary of the superseded §3 relied on a
   one-scale family; the diamond family has fixed corner scales, so relating
   `1/sqrt(n Ibar)` to `ell` requires computing how `Ibar` and the diamond volume scale along a
   covariant enlargement of the corners — not done. Any claim that the operational `O(ell)` floor
   of `prereg-003` is intrinsic remains unsupported.
3. **Poset-level tightness**: all distance control is inherited from the point level; a technique
   for bounding poset-law distances *below* the point-level bound (or matching upper bounds via
   an explicit order-only estimator) is still missing — same open item as Attempt C.
4. **The `1/n` box-family gap** (§3): whether the order-only channel attains the `1/n` point-level
   rate for support-type families is unknown.

## 7. Verdicts (task rubric)

- **(H) for the family of record: FAILED.** Not by divergence but by *vanishing*: `I ≡ 0`
  (Proposition 1, closed form). The family was ill-chosen — degenerate, a reparametrization of
  Theorem A's scale orbit. The PARTIAL verdict previously recorded for Theorem B was therefore
  optimistic about the wrong family; corrected in `first_witness_pair_candidates.md` §3.
- **(H) for the fixed-EF-box repair: FAILED** (non-regular: support motion, `H^2 asymp |delta|`,
  Proposition 2). Weakest surviving statement: the `1/n` floor of Proposition 3.
- **(H) for the diamond family: regularity established** (Lemma R, Proposition 4): QMD holds,
  `Ibar < infinity` proved; `I > 0` pointwise open (dichotomy proved instead).
- **Localization floor on the diamond family: PROVED** (§5) — the statistical implication *and*
  the model regularity it needs. This upgrades the substantive content of Theorem B from PARTIAL
  to PROVED **on the corrected family**, with the two clearly flagged open items (positivity;
  physical `ell` scaling) that do not bear on the floor's validity.
- **No physical horizon-limit claim is made.** The floor is a property of one named 1+1D family
  in one named channel at fixed `n`; it is not a statement about generic horizons, higher
  dimensions, or the sealed estimator.

## 8. Standard references

- A. W. van der Vaart, *Asymptotic Statistics*, CUP (1998), Lemma 7.6 (sufficient condition for
  QMD). `[estándar, no verificado contra biblioteca/ local]`
- R. Höpfner, *Asymptotic Statistics — With a View to Stochastic Processes*, De Gruyter (2014):
  Hellinger distance Def. 1.18; `L^2`-differentiability Def. 4.1-4.2; local Hellinger expansion
  under `L^2`-differentiability Props. 4.7-4.8 (his convention `h^2 = H^2/2`, hence the
  `delta^2 I/8` form); Le Cam's second lemma §4.2; contiguity Ch. 3. **Locally verified**:
  `biblioteca/Asymptotic Statistics.pdf` (the file so named is Höpfner, not van der Vaart). In
  our compact smooth setting, Lemma R verifies Höpfner's Def. 4.1 directly (dominated
  convergence), giving a locally-checkable alternative route to Proposition 4's QMD step.
- A. B. Tsybakov, *Introduction to Nonparametric Estimation*, Springer (2009), §2.4 (two-point
  method; TV/Hellinger inequalities). `[estándar, no verificado contra biblioteca/ local]`
- Kruskal extension and EF coordinates: any standard GR text (e.g. Wald, *General Relativity*,
  §6.4). `[estándar, no verificado contra biblioteca/ local]`

## 9. Bibliographic positioning (support, provisional)

Source: `biblioteca/Novedad bibliografica PW4.md` (2026-07-08), a machine-assisted literature
search memo placed in the git-ignored local library. Its citation markers are unresolved
artifacts, so per the repo's verification rules its contents are **leads, not verified sources**,
except where cross-checked against local `biblioteca/` holdings below. The memo's summary of the
WP4 result (order-only channel, `N = n` conditioning, regular parametric family, the bound
`TV <= (|delta|/2) sqrt(n Ibar)`, and the `1/sqrt(n Ibar)` floor) matches this annex accurately;
one terminological caveat: the memo calls the floor "minimax", while this annex proves a
**two-point** bound — minimax-flavored but not a full minimax theorem.

**Locally verifiable anchors.**

- Eichhorn-Gamito-Stokes 2026, *Towards black-hole horizons and geodesic focusing in causal
  sets* (`biblioteca/2605.06813v1.pdf`, derived-md available): the closest thematic antecedent —
  discrete horizon identification via ladders/fuzzy ladders — and, per the memo and our own WP2
  matrix (§2.6-2.7), a constructive/diagnostic line with no statistical lower bound. This
  supports the positioning of §5's floor as complementary to (not competing with) that line.
- Höpfner 2014 (see §8): the statistical machinery is textbook material; the memo's point that
  the *novelty* cannot lie in Le Cam/Hellinger themselves is confirmed and already our own §7
  framing.

**Primary sources now locally verified (2026-07-08, PDFs in `biblioteca/`).**

- **Braun 2025** (arXiv:2507.01907, `biblioteca/2507.01907v1.pdf`), *Spacetime reconstruction by
  order and number*. Theorem 1.4: for causally continuous, future chronocomplete spacetimes of
  **equal** finite volume `lambda` and dimension **`d >= 3`** (standing assumption, his §1.1),
  the laws of the **labeled** chronological adjacency matrices `C^k` coincide for **every**
  `k in N` iff the spacetimes are smoothly isometric; Theorem 1.5 (weighted): conclusion weakens
  to measure-preserving conformal isometry. Three clean separations from this annex: (i) his
  `d >= 3` vs our `d = 2` (HKMM-type rigidity is exactly what 2D lacks — our null-reparametrization
  invariance, Lemma 1 of `first_witness_pair_candidates.md`, is the 2D failure mode); (ii) his
  observable is labeled matrices for all `k` jointly — his own Remark 3.10 states the unlabeled
  (permutation-invariant) version, Bombelli's conjecture, **remains open**, and the unlabeled
  poset is precisely our channel; (iii) his equal-volume hypothesis is the "number" input — and
  our Theorem A dilation pair (whose construction is dimension-independent) exhibits identical
  adjacency laws at every `k` for **non-isometric** spacetimes with different volumes, i.e. it
  shows the necessity of that hypothesis. No contradiction in either direction; our 2D null-box
  rigidity remark is neither implied nor superseded.
- **Müller 2025** (arXiv:2503.01719v2, `biblioteca/2503.01719v2.pdf`), *On the Hauptvermutung of
  Causal Set Theory*. **The memo undersold this paper.** Theorem 1: the countable Hauptvermutung
  is true. Theorem 2: the finite Hauptvermutung is **false** for the Lorentzian Gromov-Hausdorff
  distance `d^-` — and structurally this is a published **fixed-`K` witness-pair construction**:
  for every `K`, `epsilon`, `D` there are unit-volume Cauchy slabs `X, Y` with equal boundaries,
  `d^-(X,Y) > D`, yet `|| C_K(X) - C_K(Y) ||_1 < epsilon`, where `C_K` is the (permutation-
  invariant) law of the `K`-point order relation. Mechanism: a conformal bump confined to a thin
  neighborhood of a maximizing curve inside a region of volume `v` with `(1-v)^K > epsilon`, so
  the `K`-sample laws differ only on configurations that hit the bump. Three consequences for us:
  (a) the *genre* "two completions, target differs arbitrarily, fixed-`K` order laws
  `epsilon`-close" **exists in print** — it instantiates the `canonical_counterexamples.md` §10
  checklist for target = timelike diameter / Lorentzian distance; (b) his pair is `K`-dependent
  (`v ~ log(1/epsilon)/K`), which **confirms** Attempt C's structural analysis in
  `first_witness_pair_candidates.md` §4 (fixed distinct pairs separate; fixed-`n` witnesses need
  `n`-dependent geometry); (c) the small-volume-bump mechanism is a **candidate technique** for a
  horizon-existence witness at fixed `n` — see the post-study note added to that document. What
  Müller does **not** contain: any Fisher/Hellinger/QMD machinery, any localization-rate floor,
  any horizon-related target, or the exact (`TV = 0`) scale-orbit statement.
- **Madsen 2026** (arXiv:2607.05840, `biblioteca/2607.05840v1.pdf`), *On the uniqueness of
  embeddings of causal sets*. Positive-side, general `d`, globally hyperbolic: a
  "well-conditioned embedding" (order + volume-faithfulness + longest-chain/proper-time
  correspondence) into two spacetimes forces an `epsilon`-approximate isometry, with
  `epsilon -> 0` in the high-density limit (Cor. 5.6: common density `rho`,
  `rho lambda^d >= c (log rho V)^2`, probability `>= 1 - 2 (rho V)^{-K'}`). Quotes verbatim that
  "the causal order alone is famously insufficient", crediting Müller's negative result.
  Complementary to this annex: his is an asymptotic uniqueness *upper-bound-side* result under
  order + volume + chain input; ours is a fixed-`n` *lower bound* in the order-only channel.
- **Boguñá-Krioukov 2024** (Phys. Rev. D 110, 024008, accepted manuscript at
  `biblioteca/PhysRevD.110.024008-accepted.pdf`, now locally verified), *Measuring spatial
  distances in causal sets via causal overlaps*. Positive-side: an estimator of **spacelike**
  distances from causal-overlap counts, with relative error `~ 1/sqrt(rho V)` vanishing in the
  continuum limit even at Planck-scale separations (their Eq. 30). Two scope notes relevant
  here: the analysis is anchored in **Minkowski** `M^{d+1}` (curved case only sketched via local
  flatness in their §VI), and the estimator counts elements in overlap regions, i.e. it operates
  in the **order + cardinality** channel of WP3 §2, not order-only. Complementary to this annex
  in the clean sense: their upper-bound-side `1/sqrt(n)`-type rate for a *different* target
  (spatial distance, flat space) matches the parametric scale at which our two-point floor says
  order-only discrimination of the horizon-location parameter becomes impossible. No lower
  bounds, no horizon target, no Fisher/Le Cam machinery — as the memo reported.

**On the memo's novelty verdict — revised after reading the three primary sources.** The memo's
core negative finding is confirmed on this sample: none of the three contains Fisher/Hellinger/
QMD machinery, a Le Cam two-point argument, a localization-rate floor, or a horizon-location
target. But the memo's framing "no antecedent for finite-`n` indistinguishability constructions"
must be narrowed: **Müller's Theorem 2 is exactly such a construction** (fixed `K`,
`epsilon`-close order laws, arbitrarily different geometry), published December 2025, for the
target "Lorentzian distance/diameter". The honest novelty claim for this annex therefore
narrows to: the **regular parametric family + QMD/Fisher expansion + two-point `1/sqrt(n)`
floor for a horizon-location parameter in the order-only channel**, the **exact scale-orbit
(`TV = 0`) statement**, and the **Kruskal-degeneracy diagnosis** — with Müller's bump
construction acknowledged as the closest published relative on the indistinguishability side.
Boguñá-Krioukov and the memo's broader corpus claims remain unverified; an independent search is
still due before any public novelty statement.
