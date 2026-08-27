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
>   **PROVED**. Global rigidity — `c_tau` is injective in `tau`, so the family is pairwise
>   informative *everywhere* and `I(tau) = 0` on any subinterval is impossible — is now **PROVED**
>   (§4, Proposition 5). Strict positivity `I(tau) > 0` at *every single* `tau` (as opposed to
>   outside a possible discrete exceptional set) remains open; it is not needed for the floor.
>   The physical `Omega(ell)` reading is **structurally resolved** (§5a, Proposition 6):
>   `V(tau)*Ibar` is exactly dilation-invariant, giving the floor `prereg-003`'s `O(ell)` *form*
>   intrinsically. **Numerically illustrated** (NUMERICAL, not proved): `~35 ell` for one moderate
>   reference shape. Under the named thin near-horizon reshaping of §5a, R2 now proves
>   `kappa ~ lambda^6` with prefactor `a^6/32` for the scanned symmetric shape, hence degradation
>   as `~ell/lambda^3`. A more general aspect family has prefactor
>   `a b^3(4a-b)^2/288`; the tuned shape `b=4a` cancels this leading term.
>
> Taxonomy labels (taxonomy §10): object = continuous geometric position/curvature parameter of a
> 1+1D Schwarzschild family; task =
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

**Dichotomy (restated).** For any `tau != tau'` in `[tau_0, tau_1]`: either `c_tau != c_{tau'}`
(the family is informative at that pair), or `c_tau = c_{tau'}`, in which case
`(theta_tau, theta_{tau'})` is an **exact `TV = 0` witness pair for relative horizon location** —
an even stronger result than the floor. Either branch serves the program; the floor theorem below
needs neither. Proposition 5 (next) shows the second branch never occurs on this family.

**The Ricci scalar of the family (elementary, verified symbolically with sympy —
`research_program/work_packages/wp4_fisher_localization_floor_symbolic_checks.py`, run with
`python3 research_program/work_packages/wp4_fisher_localization_floor_symbolic_checks.py`).** For
`g_t = -(1 - t/r) dv^2 + 2 dv dr`, direct computation of the Christoffel symbols, Riemann tensor,
and contraction gives

`R_t(v, r) = -2t / r^3`,

independent of `v` (as staticity requires). It is used below only as a fixed, `t`-linear,
computable scalar invariant, carried covariantly by any isometry; no physical horizon-limit
reading is claimed for it (that is the separate open item 2 of §6).

**Proposition 5 (global rigidity: no exact re-identification in the diamond family).** For the
diamond family of §4, `c_tau != c_{tau'}` for every pair `tau != tau'` in `[tau_0, tau_1]`.
Equivalently, `tau -> c_tau` is injective: the exact-witness branch of the dichotomy above never
fires anywhere in this family — every pair is genuinely order-informative.

*Proof.* Suppose toward contradiction `c_tau = c_{tau'}` for some `tau != tau'` in
`[tau_0, tau_1]`. By the rigidity remark of `first_witness_pair_candidates.md` §4 (same copula on
a null box implies isometric up to a global constant scale), there is a diffeomorphism
`Psi : D_tau -> D_{tau'}`, acting in null coordinates as `Psi(Ũ, v) = (phi(Ũ), psi(v))` for
increasing bijections `phi` of the `Ũ`-ranges and `psi` of the shared `v`-range `[v_p, v_q]`, with
`Psi^* g_{tau'} = k g_tau` for a constant `k > 0` (the Jacobian of the reparametrization is exactly
what turns "same copula" into "isometric up to a global constant").

1. *`Psi` fixes the corners.* Increasing bijections between intervals send endpoints to endpoints.
   Both diamonds share the `v`-range `[v_p, v_q]` exactly, so `psi(v_p) = v_p`, `psi(v_q) = v_q`;
   similarly `phi` maps the endpoints of `[Ũ_tau(p), Ũ_tau(q)]` to those of
   `[Ũ_{tau'}(p), Ũ_{tau'}(q)]`. Hence `Psi(p) = p` and `Psi(q) = q` as points of the shared
   `(v, r)` chart (the corners are fixed points of the EF chart, independent of `tau`).
2. *The Ricci scalar pins `k` and forces `r`-preservation.* Constant-conformal covariance of the
   Ricci scalar, `R[kappa g] = R[g] / kappa` for any constant `kappa > 0` (verified directly for
   this family: scaling the metric by a symbolic constant and recomputing `R` returns exactly
   `R/kappa`), together with `Psi^* g_{tau'} = k g_tau`, gives
   `R_{tau'}(Psi(x)) = k^{-1} R_tau(x)` for every `x` in `D_tau`. At `x = p`:
   `-2 tau' / r_p^3 = k^{-1} (-2 tau / r_p^3)`, so `k = tau / tau'`. Substituting this `k` back at
   a general point `x = (v, r)`: `r'(Psi(x))^3 = (k tau'/tau) r(x)^3 = r(x)^3`, so
   `r'(Psi(x)) = r(x)`: `Psi` preserves the areal-radius coordinate exactly — in `(v, r)`
   coordinates it can only move `v`, via `psi`.
3. *`r`-preservation is algebraically impossible for `tau != tau'`.* Writing `Psi`'s null-coordinate
   action with `r`-preservation substituted in gives, for every `(v, r)` in the (two-dimensional)
   box, equation `(*)`:
   `W_{tau'}(r) = -e^{psi(v)/2tau'} * phi( -e^{-v/2tau} W_tau(r) )`.
   Two derivatives of `(*)` pin down the constraint **without ever solving for `phi` in closed
   form** — solving the intermediate ODE gives a power law `phi(u) = K|u|^C`, but `phi` must map
   `Ũ_tau(p) < 0` to `Ũ_{tau'}(p) < 0` and `Ũ_tau(q) > 0` to `Ũ_{tau'}(q) > 0`, crossing `u = 0`,
   where `|u|^C` is not licensed to change sign; the route below sidesteps this entirely.
   - *(i) `d/dv` at fixed `r`.* Differentiating `(*)` in `v` (verified symbolically) gives
     `psi'(v) = (tau'/tau) * h(u)`, `h(u) := u phi'(u)/phi(u)`, `u` the argument of `phi`. The left
     side does not depend on `r`; at fixed `v = v_0`, as `r` ranges over the box's (nondegenerate)
     `r`-extent, `u` ranges over a nondegenerate interval (`W_tau' > 0`), so `h` is constant on
     that interval, equal to `(tau/tau') psi'(v_0)`. As `v_0` varies continuously the swept
     `u`-intervals vary continuously and overlap for nearby `v_0`; chaining this across the
     connected box forces `h(u)` to be **one single constant `C`** on the whole range of `u`
     achieved anywhere in the box.
   - *(ii) `d/dr` at fixed `v`, closing `(*)` on itself.* Differentiating `(*)` in `r` instead, and
     eliminating `phi(u)` using `(*)` itself (rather than solving for `phi`), gives directly
     `L_{tau'}(r) = h(u) * L_tau(r)`, with `L_t(r) := d/dr ln W_t(r) = r / (t(r - t))` (elementary;
     matches `W_t' = r e^{r/t}/t^2`). Verified symbolically — this is the identity checked in
     `wp4_fisher_localization_floor_symbolic_checks.py::check_r_derivative_route`, which never
     constructs `phi` explicitly.

   Combining (i) and (ii): `L_{tau'}(r) = C * L_tau(r)` for all `r` in the box, i.e.
   `tau(r - tau) = C * tau'(r - tau')` as an identity of linear functions of `r`
   (verified symbolically). Matching the coefficient of `r` gives `C = tau/tau'`; matching the
   constant term gives `C = (tau/tau')^2`. These two values of `C` agree only if `tau = tau'`,
   contradicting the hypothesis. ∎

**Corollary (`I` vanishes on no subinterval).** `I(tau) = 0` cannot hold for every `tau` in any
nondegenerate subinterval of `[tau_0, tau_1]`.

*Proof.* If `I ≡ 0` on `[tau_a, tau_b]`, then since `I(tau) = 4 int ( d/dtau sqrt(c_tau) )^2` and
`I >= 0` is continuous (Proposition 4), `d/dtau c_tau(x,y) = 0` for a.e. `tau` in `[tau_a, tau_b]`,
for a.e. `(x,y)` (Fubini). By Lemma R, `tau -> c_tau(x,y)` is `C^1`, so `d/dtau c_tau(x,y)` is
continuous in `tau` and hence vanishes for *every* `tau` in `[tau_a, tau_b]`, for a.e. `(x,y)`.
Then `c_tau(x,y)` is constant in `tau` on `[tau_a, tau_b]` for a.e. `(x,y)`, i.e.
`c_{tau_a} = c_{tau_b}` — contradicting Proposition 5. ∎

**On strict positivity (status updated, was open).** Proposition 5 and its corollary resolve the
dichotomy in favor of branch (a) *everywhere*, and rule out `I ≡ 0` on any subinterval — a strictly
stronger statement than what the original sketch aimed at. What remains open is only the pointwise
claim `I(tau) > 0` at *every single* `tau` in `[tau_0, tau_1]`, as opposed to outside a possible
discrete (isolated, measure-zero) exceptional set. A plausible route to close this fully:
`c_tau(x,y)` is built from real-analytic ingredients (`W_tau`, its analytic-IFT inverse, since
`W_tau' > 0`, and exponentials), so it should be jointly real-analytic in `(x, y, tau)`; combined
with the injectivity of Proposition 5, a non-constant real-analytic function of `tau` (for a.e.
`(x,y)`) can have at most isolated critical points, which would upgrade `I(tau) > 0` to hold
outside a discrete set. This is **not carried out here** — it needs analyticity of the marginals
despite the `tau`-dependent box boundary (`Ũ_tau(p), Ũ_tau(q)` move with `tau`), which has not been
checked — and is left as the precise remaining gap.

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
Hellinger tensorization `1 - H^2_n/2 = (1 - H^2/2)^n` gives `H^2_n <= n H^2`. In copula
coordinates every member of the family is the unit square with the same product order; all
`tau`-dependence sits in the sampling density `c_tau`. Hence the measurable map from the `n`
copula samples to the unlabeled poset is parameter-independent (Lemma 1 of
`first_witness_pair_candidates.md`; the diamond is a null box), so by data processing and `TV <= H`
(`wp4_two_point_theorem.md` Obs. 5.3), `TV( Q^n ) <= H_n <= sqrt(n) * (|delta|/2) sqrt(Ibar)`.
(2) The estimation-to-testing reduction: the test "nearest endpoint to `tau_hat`" errs only if
`tau_hat` is at distance `>= |delta|/2` from the truth; apply Teorema 2 of
`wp4_two_point_theorem.md`. (3) Immediate from (2), with the strict inequality as per the audited
consequence 2 of that note. ∎

**What the theorem quantifies over.** All functions of the observed unlabeled poset (randomized
included), at the stated fixed `n`, in the order-only channel, both models conditioned on
`N = n`. The bound holds a fortiori because it already holds at the point-process level; it can
therefore be loose for posets, and it says nothing about what any estimator *achieves*.

## 5a. The floor in physical units: dilation invariance of `V(tau) * Ibar` (item 2 of §6)

**Motivation.** §5's floor is stated in abstract statistical units (`n`, `Ibar`). To compare it to
`prereg-003`'s operational floor `Error(r̂ - r_S) >= K * ell`, `ell = rho^(-1/2)`
(`docs/preregistration_003.md` §1), it must be rewritten in units of the discreteness scale `ell`.
With `n = rho * V(tau)` (`V(tau)` the `g_tau`-area of `D_tau`; sprinkling density `rho`), so that
`ell = sqrt(V(tau)/n)`, §5's floor `delta_n ~ 1/sqrt(n Ibar)` becomes

`delta_n / ell = 1 / sqrt( Ibar * V(tau) ) =: 1 / sqrt(kappa)`,

with `kappa := V(tau) * Ibar` **dimensionless** (`I` has units `1/length^2` since `tau` has units
of length; `V` has units `length^2`). Item 2 of §6 asked whether this `kappa` degenerates (`-> 0`
or `-> infinity`) as the diamond's corners are enlarged, which would make "`O(ell)`" a
size-dependent, non-intrinsic statement. It does not — this is now proved.

**Lemma (exact dilation covariance of the diamond family).** For `s > 0`, let the "`s`-scaled
family" be the diamond family of §4 built from corners `(s v_p, s r_p)`, `(s v_q, s r_q)` and range
`[s tau_0, s tau_1]`. Write `V'`, `I'` for its area and Fisher information as functions of its own
parameter `tau' := s tau`. Then:

1. `W_{s t}(s r) = W_t(r)` identically (elementary; verified symbolically —
   `research_program/work_packages/wp4_fisher_localization_floor_symbolic_checks.py`), hence the
   null coordinate is exactly scale-covariant: `Ũ_{s t}(s v, s r) = Ũ_t(v, r)`.
2. `D_{s tau} = s * D_tau` (the dilated image, as a subset of the `(v, r)` plane) — immediate
   from 1.
3. `det g_t = -1` for every `t` (§4), so the sampling measure on `D_t` is always Lebesgue `dv dr`;
   hence `V'(s tau) = s^2 V(tau)` (elementary area scaling under a linear dilation by `s`,
   Jacobian `s^2`, verified symbolically).
4. `c'_{s tau} = c_tau` exactly as copula densities on the unit square. *Proof:* the map
   `(v, r) -> (s v, s r)` acts on null coordinates as `Ũ -> Ũ` (identity, by 1) and `v -> s v` (an
   increasing reparametrization of the second coordinate alone, `s > 0`) — precisely the
   per-coordinate reparametrization that leaves a copula unchanged (Sklar's theorem; the same
   invariance used and verified in Proposition 5's audit). Concretely: pushing the uniform
   `dv' dr'` sampling measure on `D_{s tau}` forward through `(v', r') = (s v, s r)` and then to
   null coordinates gives `h'_{s tau}(Ũ', v') = s * h_tau(Ũ', v'/s)` (Jacobian `s^2` from 3, times
   `1/s` from the coordinate substitution `dv = dv'/s`); the constant prefactor `s` cancels under
   copula normalization, and `v' = s v` is exactly the per-coordinate rank-preserving
   reparametrization Sklar's theorem quotients out.
5. Consequently, `c'_{tau'}(x, y) = c_{tau'/s}(x, y)` exactly, so by the chain rule
   `I'(s tau) = I(tau) / s^2` (verified symbolically: `d/dtau' f(tau'/s) = f'(tau'/s)/s`, squared
   and integrated).

**Proposition 6 (`V * Ibar` is a dilation-invariant shape functional).**
`kappa(tau) := V(tau) * I(tau)`, evaluated for the `s`-scaled family at its corresponding
parameter `s tau`, equals `kappa(tau)` for every `s > 0`: it depends only on the *dimensionless
shape* of the diamond (the ratios `r_p/tau_0, r_q/tau_0, v_p/tau_0, ...`), never on its absolute
size.

*Proof.* Immediate from the Lemma: `V'(s tau) * I'(s tau) = [s^2 V(tau)] * [I(tau)/s^2] =
V(tau) * I(tau)`. ∎

**Corollary (the floor has the `O(ell)` form, structurally).** Writing `kappa_bar :=
V * Ibar_{[tau_0,tau_1]}` (evaluating `V` at a reference point of the range; exact if `V` is
constant across `[tau_0, tau_1]`, an `O(1)` approximation for a range narrow relative to `tau_0`,
otherwise tracked as a function of `tau`):

`delta_n ~ ell / sqrt(kappa_bar)`,

and `kappa_bar` is a *pure number*, identical across the whole dilation orbit of a given diamond
shape. This is the first order-only, information-theoretic (not estimator-induced) statement with
the exact `O(ell)` *form* of `prereg-003`'s operational floor `(★)` — it shows that form is not an
artifact of the particular box size chosen, only of the box *shape*.

**Deterministic numerical reference values (item (i), now available — NUMERICAL, not a proof).**
`research_program/work_packages/wp4_kappa_numeric_reference.py` gives a **quadrature-based
numerical reference** for `V(tau)` and `I(tau)` — quantities Proposition 4 and this section define
*exactly*, evaluated here by deterministic quadrature (trapezoid rule + root-finding for the
transcendental `r = r_tau(Ũ, v)`; PCHIP monotone interpolation for the marginal quantile maps — no
closed form exists for `W_tau^{-1}`, so this is a numeric, not symbolic, evaluation) because they
have no closed form, not computed in closed form themselves. "Deterministic" describes the
*method* (reproducible, no randomness anywhere in the pipeline) — it is **not a simulation**: no
Poisson sprinkling, no order-only estimator, no random seed. It does **not** mean the reported
numbers are exact or error-free: they carry ordinary quadrature/discretization error, bounded only
by the stability checks below, not by a proof. `I(tau)` is estimated via the QMD expansion itself
(`H^2(c_{tau-delta/2}, c_{tau+delta/2}) ~= (delta^2/4) I(tau)`, Proposition 4), checked stable to
`<0.1%` across a `4x` range of `delta` (confirms the QMD asymptotic regime is reached, not
finite-difference noise), and cross-checked (the copula integrates to `~1` over the unit square;
the two ways of computing `V` — integrating `m1` vs `m2` — agree to `<1e-6`).

For a moderate reference diamond (`tau=1`, `r_p=2, r_q=0.5, v_p=0, v_q=1`):
`V ~= 1.4717`, `I ~= 5.415e-4`, `kappa ~= 7.97e-4`, giving `delta_tau/ell ~ 1/sqrt(kappa) ~= 35.4`
— i.e. **the two-point floor for this shape is `~35 ell`, not `~1 ell`**: a genuine, large `O(1)`
constant, not `O(ell)` in the naive sense of "order unity in `ell`-units".

**Item (iii) — reshaping toward a thin near-horizon diamond (R2, analytically resolved for the
named family).** Fix `a,b>0` and, at `tau=1`, take

`r_p=1+a lambda`, `r_q=1-a lambda`, `v_p=0`, `v_q=b lambda`.

The corners are *not* dilated together with `tau`: this is a change of dimensionless shape, the
case Proposition 6 does not cover.

**Proposition 7 (thin-shape asymptotic and prefactor).** As `lambda -> 0`, with the physical
corners held fixed when differentiating in `tau`,

`I_lambda(1) = [b^2(4a-b)^2/576] lambda^4 + O(lambda^5)`,

`V_lambda(1) = 2ab lambda^2 + O(lambda^3)`, and hence

`kappa_lambda(1) = [a b^3(4a-b)^2/288] lambda^6 + O(lambda^7)`.

For the scanned symmetric shape `a=b=0.3`,

`kappa_lambda(1) = (a^6/32) lambda^6 + O(lambda^7)
                  = 2.278125e-5 lambda^6 + O(lambda^7)`,

so `delta_tau/ell ~ sqrt(32) a^{-3} lambda^{-3}`. Thus halving the linear shape parameter
multiplies the asymptotic floor by `8`. If `b=4a`, however, the displayed prefactor vanishes:
this proposition does **not** claim a `lambda^6` leading law for that tuned aspect ratio; its
next nonzero order remains open.

*Proof.* Introduce the matched variable `sigma=(tau-1)/lambda` and unit-square coordinates
`y=v/(b lambda)`, `z=(Utilde-Utilde_p)/(Utilde_q-Utilde_p)`. The exact inverse null-coordinate
map is

`r_tau(Utilde,v) = tau {1 + W_0[-Utilde exp(v/(2tau)-1)]}`.

Expanding its normalized Jacobian at fixed `sigma`, and writing `Z=z-1/2`, `Y=y-1/2`, gives a
fixed-square density `p=1+lambda p_1+lambda^2 p_2+lambda^3 p_3+O(lambda^4)` with
`p_1=4aZ+(b/2)Y` and
`partial_sigma p_2|_0=-(2a+b)Z+(b/2)Y`. Both are additive marginal deformations. Since
`partial_tau=lambda^{-1} partial_sigma`, the first non-additive copula score is the two-way
zero-marginal projection of
`B:=partial_sigma p_3|_0-p_1 partial_sigma p_2|_0`, namely

`partial_tau log c_tau|_{tau=1}
 = lambda^2 [b(4a-b)/2] ZY + O(lambda^3)`.

Marginal-quantile motion enters only at `O(lambda^3)` because `p_1` is additive. Integrating the
square against the limiting uniform copula and using
`int_0^1 (z-1/2)^2 dz=1/12` yields the coefficient of `I`. Finally `det g_tau=-1`, while the
leading radial and temporal widths are `2a lambda` and `b lambda`, giving the coefficient of `V`
and therefore of `kappa`. The algebraic projection and integrals are checked exactly by
`dev/r2_lambda6_06_prefactor.py`; no sampling or random seed is used. ∎

The pre-existing deterministic scan is consistent with Proposition 7. For `a=b=0.3`, shrinking
from `lambda=1` to `lambda=0.05` gave `kappa` falling from `1.68e-5` to `3.53e-13`; its fitted
exponents `5.917` (all six points) and `5.988` (smallest four) were numerical precursors, not
inputs to the derivation. At `lambda=0.20,0.10,0.05`, the numerical `I` divided by the analytic
leading term is respectively `0.98265, 0.98982, 0.99161`.

**What this suggests, stated carefully.** This is consistent with — and gives one candidate
quantitative account of — a pattern noted informally in this project's PR004 attempts (parked
present-anchor and ladder-braiding diagnostics; see `dev/`, `data/reports/`): diagnostics that
probe small, local, near-horizon patches for fine order-only localization may be attempting
something close to an information-theoretic wall, not merely fighting an implementation defect.
**This is a plausibility argument from a numerical scan of one particular family, not a proof that
any specific PR004 diagnostic hits this wall** — no PR004 output was read or used to produce these
numbers, and no PR004 diagnostic's actual probed shape has been checked against this scan.

**What is still NOT done.** (i) *[now available, see above]*. (ii) Comparing any of these numbers
to `prereg-003`'s measured `K_LOC` constant — a different quantity (bounds the *sealed estimator's*
output, §1-2 there), not something this floor claims to explain or reproduce. (iii) *[partially
examined and analytically resolved for the named aspect family, see Proposition 7]* — the next
nonzero order at the tuned cancellation `b=4a`, and any classification over more general
reshaping paths, remain open. (iv) Whether PR004's actual diagnostic patches correspond to any
specific `(r_p, r_q, v_p, v_q)` in this family at all — the diamond family is a mathematical
construction for proving a floor, not a description of what PR004's ladder/peel-off procedure
geometrically probes; this connection has not been made.

## 6. What remains open

1. **`I(tau) > 0` at every single `tau`** (§4): the exact-witness branch of the dichotomy is now
   ruled out everywhere and `I` cannot vanish on any subinterval (Proposition 5 + corollary,
   **PROVED**); pointwise positivity outside a possible discrete exceptional set remains open (not
   needed for the floor).
2. **The physical `Omega(ell)` reading**: **structurally resolved** (§5a, Proposition 6,
   **PROVED**) — `V(tau) * Ibar` is exactly dilation-invariant, so `delta_n ~ ell / sqrt(kappa_bar)`
   with `kappa_bar` a pure, size-independent number. **Numerically illustrated** (§5a,
   `wp4_kappa_numeric_reference.py`, NUMERICAL): `kappa_bar ~ 8e-4` for one moderate reference
   shape (`delta_tau ~ 35 ell`). **Analytically resolved for the named thin-shape family**
   (Proposition 7): `kappa_lambda(1) = [a b^3(4a-b)^2/288] lambda^6+O(lambda^7)`, reducing to
   `(a^6/32)lambda^6+O(lambda^7)` for the scanned `a=b=0.3`, so
   `delta_tau/ell ~ lambda^-3`. Still open: the next order at the tuned cancellation `b=4a`;
   any comparison to `prereg-003`'s measured `K_LOC` (a different, estimator-bound quantity);
   whether PR004's diagnostics actually probe shapes in this degrading regime (not checked
   against any PR004 output).
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
  `Ibar < infinity` proved; global rigidity proved (Proposition 5: `c_tau` injective in `tau`,
  `I ≡ 0` on no subinterval); `I > 0` at every single `tau` remains open only outside a possible
  discrete exceptional set.
- **Localization floor on the diamond family: PROVED** (§5) — the statistical implication *and*
  the model regularity it needs. This upgrades the substantive content of Theorem B from PARTIAL
  to PROVED **on the corrected family**, with the remaining open item (pointwise positivity) that
  does not bear on the floor's validity.
- **The floor's `O(ell)` form is intrinsic, not just operational** (§5a, Proposition 6, PROVED):
  `V*Ibar` is exactly dilation-invariant, giving `delta_n ~ ell/sqrt(kappa_bar)` with `kappa_bar` a
  size-independent pure number. This is the first order-only, information-theoretic statement
  sharing `prereg-003`'s operational-floor *form*; it does not reproduce or bound `prereg-003`'s
  measured constant.
- **The floor degrades sharply under the named thin near-horizon reshaping (PROVED for that
  family)**: Proposition 7 gives
  `kappa_lambda(1)=[a b^3(4a-b)^2/288]lambda^6+O(lambda^7)` and therefore
  `delta_tau/ell ~ lambda^-3` whenever `b!=4a`. The scanned `a=b=0.3` prefactor is `a^6/32`;
  its deterministic numerical fit was the precursor and agrees with the asymptotic coefficient.
  The tuned shape `b=4a` is explicitly excluded from the leading-law claim. Connecting this
  mathematical family to any PR004 diagnostic remains a plausibility argument only: no PR004
  output or shape was used.
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
  Müller does **not** contain: Fisher/Hellinger/QMD machinery, a local minimax floor on a regular
  parametric family, a horizon-related target, or the exact (`TV = 0`) scale-orbit statement.
  **External-reader correction (2026-07-28):** his Theorem 3 must nevertheless be counted as the
  closest quantitative precursor. For normalized flat cylinders it gives
  `P(total order) >= 1 - 4*pi*K^2*T^(-1/n)` while `d^-` grows with temporal-diameter separation.
  This is a continuous one-parameter family with an explicit sample-size/geometric-degeneracy
  bound, albeit by collapse to total order rather than QMD/local two-point regularity.
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
  order-only discrimination of the continuous geometric parameter becomes impossible. No lower
  bounds, no horizon target, no Fisher/Le Cam machinery — as the memo reported.

**On the memo's novelty verdict — revised after reading the three primary sources.** The memo's
core negative finding is confirmed on this sample: none of the three contains the project's
Fisher/Hellinger/QMD chain, a Le Cam risk statement on a regular Schwarzschild family, or a
horizon-related target. Müller Thm 3 does contain a quantitative bound for a continuous geometric
family, so the earlier blanket phrase “no localization-rate floor” was too strong. The memo's
framing "no antecedent for finite-`n` indistinguishability constructions"
must be narrowed: **Müller's Theorem 2 is exactly such a construction** (fixed `K`,
`epsilon`-close order laws, arbitrarily different geometry), published December 2025, for the
target "Lorentzian distance/diameter". The honest novelty claim for this annex therefore
narrows to: the **regular parametric family + QMD/Fisher expansion + two-point `1/sqrt(n)`
floor for a continuous geometric parameter in the order-only channel**, the **exact scale-orbit
(`TV = 0`) statement**, and the **Kruskal-degeneracy diagnosis** — with Müller's bump
construction (Thm 2) and quantitative cylinder degeneration (Thm 3) acknowledged as the closest
published relatives on the indistinguishability side.
**`[CORRECCIÓN 2026-07-28 — contradicción interna resuelta]`** La versión previa de este párrafo
cerraba con "Boguñá-Krioukov and the memo's broader corpus claims remain unverified; an independent
search is still due before any public novelty statement", lo que **contradecía** el bullet de
Boguñá-Krioukov de §9 (`:543`), que ya lo declara "**now locally verified**" con el PDF en
`biblioteca/PhysRevD.110.024008-accepted.pdf`. La frase era un remanente anterior a esa
verificación. Estado real a 2026-07-28:

- **Boguñá-Krioukov 2024: VERIFICADO localmente** (bullet de §9, PDF presente). Ya no figura como
  pendiente.
- **Corpus más amplio del memo: sigue sin verificarse pieza a pieza**, y esa parte de la advertencia
  **se mantiene**.
- **La búsqueda independiente EXIGIDA (WP5 Paso D) SE HA REALIZADO** y está registrada, con su
  método, sus límites y su veredicto, en
  `research_program/bibliography/wp5_paso_d_independent_novelty_review.md` (2026-07-28). Terminal:
  `NOVELTY_NOT_REFUTED / NOVELTY_NOT_CERTIFIED` — autoriza un claim de novedad **acotado y
  comparativo**, no la novedad como hecho establecido.
- **Corroboración externa nueva y directamente pertinente a este anexo**, incorporada a
  `biblioteca/` en esa revisión: de Brito–Eichhorn–Pfeiffer 2023 (Eur. Phys. J. Plus 138, 592;
  `biblioteca/2301.13525v2.pdf`) construye invariantes de orden superior **solo de la forma
  `R² − □R`** — todos derivados del escalar de Ricci; y Eichhorn–Mack–Le–Wagner 2026
  (`biblioteca/2605.27514v1.pdf`) afirma en texto que "no explicit construction of, e.g., the
  Kretschmann scalar, has so far been achieved". Ninguno contiene cota inferior estadística,
  maquinaria Fisher/Le Cam, ni target de horizonte.
