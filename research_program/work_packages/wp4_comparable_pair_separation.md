# WP4 Annex C — the comparable-pair probability separates `tau` on the diamond family

> **Working draft, REVISABLE, not frozen.** Mathematics only: symbolic algebra, deterministic
> quadrature, and one fixed-seed Monte-Carlo cross-check of that quadrature. No simulation of the
> bench, no sprinkling experiment, no estimator, no threshold, no seed band, no validation
> artifact. Nothing here imports from `nachocausal/`. The programme remains in
> `PROGRAMA_EN_PAUSA_LIMPIA` (`docs/marcador_reentrada_2026-07-19.md`); this annex is the step 1
> of `docs/hoja_de_ruta_24_jul_2026.md` §2 — a calculation, explicitly authorised there as
> *"un cálculo simbólico/analítico … no una ejecución ni una implementación de estimador"*.
>
> **Headline.** For the causal-diamond family of `wp4_fisher_localization_floor.md` §4, the
> order-only scalar `p(tau)` of `research_program/bibliography/ficha_se_busca_tv_order_only.md`
> §7.1 — the probability that two i.i.d. points are causally comparable — obeys
>
> ```text
> p(tau) = 1/2 + kappa(r_p, r_q) * tau * dv + O(dv^2),
> kappa(r_p, r_q) = [ (r_p^2 - r_q^2) - 2 r_p r_q log(r_p/r_q) ] / [ 12 r_p r_q (r_p - r_q)^2 ] > 0,
> ```
>
> the leading term being **strictly proportional to `tau`**. Hence `p(tau) != p(tau')` for
> `tau != tau'` once `dv` is small, which settles ingredient **(a)** of ficha §7.1 —
> `[OPEN por par]` since v2 of that ficha — for this family. It does **not** close Forma L: §5
> lists exactly what still blocks that, and why the blocker is a *channel* problem, not this
> inequality.
>
> Verification script (all checks pass, exit 0):
> `wp4_comparable_pair_separation_checks.py`, run with
> `.venv/bin/python research_program/work_packages/wp4_comparable_pair_separation_checks.py`.

## 1. The question, in the ficha's own terms

Ficha §2.1(B) reduced candidate 7.1 (number of comparable pairs) to *one* unverified scalar
inequality, having imported Reitzner–Schulte 2013 for the fluctuation ingredient:

> **Lo que NO cierra — el único punto que falta:** `p(theta) != p(theta')` para el par concreto
> que se quiera usar (WP4 diamante, OP-1.1/1.2, u otro). Sigue `[OPEN por par]` … la
> inyectividad de `tau -> c_tau` (WP4 Prop 5) no implica la de `tau -> p(tau)`.

That last clause is the crux and it is correct: Proposition 5 of `wp4_fisher_localization_floor.md`
proves `tau -> c_tau` injective, but `p` is a single real functional of `c_tau`, and injectivity of
a family says nothing about injectivity of a scalar reduction of it. This annex computes the scalar.

**Convention note (a discrepancy inside the ficha, harmless here).** Ficha §7.1 defines
`p(theta)` as the probability that two i.i.d. points are *comparable*; ficha §2.1(B) defines it as
`int int 1[x prec y] dc dc`, which is **half** of that (exactly one of `x prec y`, `y prec x` holds
a.s.). This annex computes the §7.1 quantity, written `p(tau)` throughout, and reports Kendall's
`tau_K = 2 p - 1` alongside. The factor 2 is common to both parameters and so cannot affect the
inequality `p(theta) != p(theta')`; the ficha should nonetheless be made internally consistent.

## 2. Setup (all of it taken from WP4 §4, nothing new)

Fix `0 < r_q < tau_0 <= tau <= tau_1 < r_p` and `v_p < v_q`; write `dv := v_q - v_p > 0`. On the
Eddington–Finkelstein chart, `g_tau = -(1 - tau/r) dv^2 + 2 dv dr`; corners `p = (v_p, r_p)`
(exterior) and `q = (v_q, r_q)` (interior) are held fixed as `tau` varies, and the patch is the
causal diamond `D_tau := J^+_tau(p) ^ J^-_tau(q)`.

**Fact C0 (the sampling measure is flat in these coordinates).** `det g_tau = -1` identically, so
`sqrt(-det g_tau) = 1` and `vol(g_tau) = dv dr`: the normalised sampling measure of `D_tau` is
*uniform Lebesgue measure* on `D_tau` in the `(v, r)` chart. (Check [1].) All `tau`-dependence
therefore sits in the *shape of the region* and in the causal order, not in a density prefactor.

**Null chart and the order.** With `omega_tau(r) := e^{r/tau}(r/tau - 1)`, WP4 §4 establishes that
`Utilde := -e^{-v/(2 tau)} omega_tau(r)` is an exactly null coordinate, that `(Utilde, v)` is a
global double-null chart on `r > 0`, and that the causal order is the **product order**, both
coordinates increasing to the future. Elementary properties used below:
`omega_tau : (0, infinity) -> (-1, infinity)` is a strictly increasing bijection with
`omega_tau(tau) = 0` and `omega_tau'(r) = r e^{r/tau} / tau^2 > 0`; its inverse is explicit in the
principal Lambert branch, `omega_tau^{-1}(w) = tau (1 + W_0(w/e))`.

**The ray flow.** Let
`rho_tau(r_0, D) := omega_tau^{-1}( e^{D/(2 tau)} omega_tau(r_0) )` be the areal radius at
`v = v_0 + D` of the outgoing null ray through `(v_0, r_0)`. Differentiating the defining relation,

```text
d rho / d D = (rho - tau) / (2 rho),      rho(r_0, 0) = r_0.
```

(Check [2].) Two consequences matter. (i) The sign of `rho - tau` is preserved, so **no outgoing
ray crosses the horizon** `r = tau` — the horizon *is* the ray `Utilde = 0`. (ii) Exterior rays
(`r_0 > tau`) rise in `v` while interior rays (`r_0 < tau`) fall. The two `r`-boundaries of
`D_tau` therefore move in opposite senses, so `min_{D_tau} r = r_q` and
`max_{D_tau} r = rho_tau(r_p, dv)`, both attained at `v = v_q`. (This is the same statement as
WP4 §4's "its minimal `r`-value over the closed box is `r_q > 0`"; getting it backwards is a real
trap — it was an actual bug in the first draft of the Monte-Carlo cross-check of this annex, which
clipped away most of the diamond and disagreed with the quadrature by tens of sigma before being
fixed. That figure came from a discarded intermediate state and is *not* reproducible from this
repo; it is recorded as history, not as a result.)

## 3. Exact reduction: from a 4-fold integral to a 2-fold one

**Lemma C1 (ray integral in closed form).** For any `r_0 > 0` and any `D` for which the ray stays
in `r > 0`,

```text
int_{v_0}^{v_0 + D} rho_tau(r_0, v - v_0) dv = rho_tau(r_0, D)^2 - r_0^2 + tau * D.
```

*Proof.* Both sides vanish at `D = 0`. Differentiating the right side in `D` and using the ray ODE,
`d/dD [ rho^2 + tau D ] = 2 rho (rho - tau)/(2 rho) + tau = rho`, which is the integrand. ∎
(Check [3], symbolically — residual exactly `0` — and against direct quadrature to `|diff| = 1.11e-15`.)

**Proposition C2 (sub-diamond areas in closed form).** For `x = (v_x, r_x)` in `D_tau`, put
`D := v_q - v_x`. Then `J^+(x) ^ D_tau = J^+(x) ^ J^-(q)` and

```text
vol( J^+(x) ^ D_tau ) = rho_tau(r_x, D)^2 + rho_tau(r_q, -D)^2 - r_x^2 - r_q^2.
```

In particular the patch volume is `V(tau) = rho_tau(r_p, dv)^2 + rho_tau(r_q, -dv)^2 - r_p^2 - r_q^2`.

*Proof.* `x in J^+(p)` gives `J^+(x) subset J^+(p)`, whence the first equality. At fixed
`v in [v_x, v_q]`, `Utilde` is decreasing in `r`, so the slice of `J^+(x) ^ J^-(q)` is
`{ r : R_q(v) <= r <= R_x(v) }` where `R_c` denotes the outgoing ray through `c` — non-empty for
every such `v` precisely because `Utilde_x <= Utilde_q`. Integrate `R_x - R_q` over `[v_x, v_q]`
with Lemma C1 applied to each (for `R_q`, start the ray at its `v = v_x` value
`rho_tau(r_q, -D)`); the two `tau * D` terms cancel. ∎

**Proposition C3 (the reduction).** With `alpha(D) := rho_tau(r_p, dv - D)` and
`beta(D) := rho_tau(r_q, -D)`,

```text
p(tau) = 2 V(tau)^{-2} * int_0^{dv} dD int_{beta(D)}^{alpha(D)}
             [ rho_tau(r, D)^2 + beta(D)^2 - r^2 - r_q^2 ] dr.
```

*Proof.* Points are exchangeable and a.s. untied, and comparability of `x, y` in a product order
means exactly that `x prec y` or `y prec x`, so `p = 2 P(X prec Y)`. Then
`P(X prec Y) = V^{-2} int_{D_tau} vol(J^+(x) ^ D_tau) dv_x dr_x` by Fubini, and Proposition C2
supplies the inner volume in closed form; substituting `D = v_q - v_x` and reading off the
`r`-extent of `D_tau` at that `v` gives the stated domain. ∎

**What this buys.** The naive object is a 4-fold integral over `D_tau x D_tau` of an indicator.
Proposition C3 is a 2-fold integral of an integrand that is *real-analytic on the closed domain*
(compositions of `exp`, `log`, and `W_0` away from its branch point — the argument of `W_0` stays
`>= omega_tau(r_q)/e > -1/e` throughout). Gauss–Legendre therefore converges spectrally: 15 digits
by `n = 80` nodes per axis (check [5]). Three independent routes agree: the quadrature, a
fixed-seed rejection-sampling Monte Carlo that counts comparable pairs, and the same sample scored
through the closed form of Proposition C2 instead (check [4], agreement within 1 sigma, and the
Monte-Carlo area matches `V(tau)` to 0.1%).

**Interpretation.** In a null box, comparability is concordance of the two null coordinates, and
concordance is rank-invariant; so `p(tau) = (1 + tau_K(c_tau))/2` with `tau_K` Kendall's tau of the
copula `c_tau`. Two corollaries. First, `p` is *exactly* a copula functional, so it automatically
passes the mandatory orbit test of ficha §4 — verified numerically to `< 1e-15` under joint
dilation `(tau, r_p, r_q, dv) -> s * (...)` (check [6]), i.e. the statistic is provably blind to
the Theorem-A scale orbit and cannot manufacture a spurious separation there. Second, `p = 1/2`
is the independence/flat value (a 1+1D Minkowski causal interval has comparable fraction exactly
`1/2`), so `p - 1/2` measures how far the diamond's copula sits from independence.

## 4. Leading asymptotics in the null lapse

**Theorem C4.** Fix admissible `(tau, r_p, r_q)`. As `dv -> 0^+`,

```text
p(tau) = 1/2 + kappa(r_p, r_q) * tau * dv + O(dv^2),
kappa(r_p, r_q) = [ (r_p^2 - r_q^2) - 2 r_p r_q log(r_p / r_q) ] / [ 12 r_p r_q (r_p - r_q)^2 ].
```

*Derivation (machine-verified, check [7]).* Expand the ray flow as a series in the lapse from the
ODE of §2, `rho = r + D (r-tau)/(2r) + D^2 tau (r-tau)/(8 r^3) + ...`; substitute into
Proposition C3; integrate the retained orders in `r` in closed form (the antiderivatives are
elementary, `r(r-2tau)/2`, `r/4 - tau log(r)/4`, …); put `D = dv * t` and integrate `t` over
`[0,1]`. Writing `N = dv^2 * Nhat(dv)` and `V = dv * Vhat(dv)` — the leading coefficients are
`Nhat(0) = (r_p-r_q)^2/4` and `Vhat(0) = r_p - r_q != 0` — the ratio `p = 2 Nhat / Vhat^2` extends
to `dv = 0` with value exactly `1/2`, and its first Taylor coefficient is the stated
`kappa * tau`. Sympy confirms both the `dv^0` coefficient (`= 1/2`) and that the `dv^1`
coefficient equals `kappa * tau` identically. ∎

*Two steps are argued rather than written out,* and both are labelled as such in §6. **(i)** That
`p` is analytic in `dv` at `0^+`, which licenses reading Taylor coefficients off the formal series.
It holds because `N` and `V` are integrals of analytic integrands over analytically-varying domains,
hence analytic in `dv`, and `Vhat(0) != 0` removes the apparent singularity of the ratio.
**(ii)** That the `O(dv^2)` remainder is uniform in `tau` over `[tau_0, tau_1]` (used in Corollary
C6). Continuity in `tau` of each expansion coefficient — which does follow from the explicit
formulas — is *not* by itself enough for a uniform remainder bound; that needs joint control, e.g.
analyticity in `(dv, tau)` on a neighbourhood of `{0} x [tau_0, tau_1]`, which the same argument as
(i) should give but which is not carried out. A fully written proof would spell both out.

**Lemma C5 (positivity of `kappa`).** `kappa(r_p, r_q) > 0` strictly for all `0 < r_q < r_p`.

*Proof.* With `x := r_p/r_q > 1`, the numerator is `2 r_p r_q [ (x - 1/x)/2 - log x ]`. Put
`phi(x) := (x - 1/x)/2 - log x`. Then `phi(1) = 0` and
`phi'(x) = (1 + 1/x^2)/2 - 1/x = (x-1)^2 / (2 x^2) > 0` for `x != 1`, so `phi(x) > 0` for `x > 1`.
The denominator is positive. ∎ (Check [8].)

**Corollary C6 (the inequality the ficha asked for).** For each admissible
`(r_p, r_q, tau_0, tau_1)` there is `dv_0 > 0` — depending on those four numbers only — such that
for all `0 < dv < dv_0`, the map `tau -> p(tau)` is strictly increasing on `[tau_0, tau_1]`; in
particular

```text
p(tau) != p(tau')    for every    tau != tau'    in [tau_0, tau_1].
```

*Proof.* Theorem C4 with Lemma C5: the `dv^1` coefficient is `kappa * tau` with `kappa > 0` fixed,
strictly increasing in `tau`, and the remainder is `O(dv^2)` uniformly in `tau` over the compact
`[tau_0, tau_1]` (the expansion's coefficients are continuous in `tau` there). ∎

**Consistency with scale invariance.** `kappa` is homogeneous of degree `-2`, so `kappa * tau * dv`
is invariant under `(tau, r_p, r_q, dv) -> s (tau, r_p, r_q, dv)` — as it must be, since `p` is
(check [6]). This is a nontrivial check on the closed form: an algebra slip would generically
break it.

**Effectivity caveat.** `dv_0` is **not** made explicit: no remainder bound was computed, so
Corollary C6 is an asymptotic statement. For a *named* `dv` the inequality is established
numerically instead, at working precision — see §6.

## 5. What this closes, and what it does NOT

**Closed.** Ingredient (a) of ficha §7.1 — `p(theta) != p(theta')` — for the WP4 §4 diamond
family. Together with ficha §2.1(B) (Reitzner–Schulte 2013, fluctuation ingredient with an
explicit `lambda^{-1/2}` rate uniform in `theta`), the *mean-separation* and *fluctuation*
ingredients 1 and 2 of ficha §6 are now both in hand for candidate 7.1 on a named family.

**Not closed — Forma L is not obtained, and the obstruction is the channel.** Four items, in the
order they bite:

1. **The cardinality confounder is live in the very channel where Reitzner–Schulte applies.**
   Their CLT is for *unconditioned Poisson* U-statistics (`lambda -> infinity`, mode 1 of ficha
   §1.3). But this family has a `tau`-dependent volume (check [4b]):
   `V(1.0) = 11.501608349297` against `V(1.2) = 10.794261266781` at `dv = 4` (relative difference
   `6.150e-02`), and `0.049967998677` against `0.049922210322` at `dv = 0.02` (`9.164e-04`). With
   `rho` known, the marginal `N ~ Poisson(rho V(tau))` therefore separates `tau` from `tau'` **on
   its own**, which is exactly the trivial mechanism ficha §1.2 and §9.2 forbid counting. Any
   Forma L built in that channel would be contaminated unless the statistic is normalised (e.g.
   `S / C(N,2)`, whose law is *not* what Reitzner–Schulte controls) or the channel conditioned.
2. **The honest channel is `fixed_n`, and there the imported CLT does not apply as stated.**
   Conditioning on `N = n` removes the confounder (ficha §1.3 mode 3, FWP Lemma 0) and puts the
   whole burden on the order — but a de-Poissonisation step is then needed, and Reitzner–Schulte
   supply none. `[OPEN]`
3. **The variance asymptotics for the `fixed_n` statistic are not verified here.** The Chebyshev
   route of ficha §6.3 needs `Var_theta S_n = Theta(n^3)`, i.e. non-degeneracy of the first
   Hoeffding projection `h_1(x) = P(x comparable with Y)`. That is plausible and computable with
   exactly the machinery of §3 (`h_1` is a ratio of closed-form sub-diamond volumes, by
   Proposition C2 applied to `J^+(x)` and `J^-(x)`), but it **was not computed**. `[OPEN]`
4. **Ficha §6.4's mandatory consistency check passes only at the level of rates.** In `fixed_n`,
   `Delta_mu = C(n,2) * Delta_p` with `Delta_p ~ kappa * dv * delta`, and `sigma = Theta(n^{3/2})`
   under item 3, so the Chebyshev threshold sits at `delta ~ n^{-1/2}`; the *proved* upper bound
   `TV(Q^n_tau, Q^n_{tau+delta}) <= (|delta|/2) sqrt(n Ibar)` (WP4 §5) becomes informative at the
   same `delta ~ n^{-1/2}`. Same rate, no contradiction — and, conditional on item 3, the
   comparable-pair count would be **rate-optimal in `n`** against WP4's floor, which is a
   substantive statement worth recording. The *constant*-level check is **not** performed: it
   compares `kappa * dv` against `sqrt(zeta_1 * Ibar)`, and `Ibar` for these corners is not
   available (WP4 §5a has `V * Ibar` only `[NUMERICAL]`, for one reference shape) nor is `zeta_1`.
   `[OPEN]`

**Also not claimed.** (i) Nothing here is about the 3+1D Schwarzschild pairs of FWP §2 or OP-1.2;
those are Theorem-A pairs, where `p` is necessarily *equal* (same copula) — and check [6] confirms
the statistic respects that rather than falsely separating them. (ii) No global monotonicity in
`tau`: the numerics show `p` *decreasing* in `tau` at `dv = 4`, far outside the asymptotic regime,
while Theorem C4 gives increase for small `dv`. The theorem is asymptotic and is stated as such.
(iii) Nothing here touches the sealed prereg-002 result, the C1–C6 negative ledger, or the
programme's pause; no candidate is opened and no observable is implemented.

## 6. Numerical record and status labels

Diamond of record: `r_p = 3.0`, `r_q = 0.5`; concrete pair `tau = 1.0`, `tau' = 1.2`
(admissible: `r_q < tau, tau' < r_p`). Full output: check [9] of the script.

| `dv` | `p(1.0)` | `p(1.2)` | `p(tau') - p(tau)` | Theorem C4 leading term |
|---|---|---|---|---|
| `0.02` (asymptotic regime) | `0.500591097337296` | `0.500705392489878` | `+1.142952e-04` | `+1.199901e-04` |
| `4.0` (far outside it) | `0.548382340298801` | `0.547994788251956` | `-3.875520e-04` | `+2.399802e-02` |

Kendall's `tau_K` at `dv = 0.02`: `0.001182194675` vs `0.001410784980`. Quadrature is stable to
15 digits (check [5]); the separation is 10–11 orders of magnitude above that, so it is not a
numerical artefact.

Closed-form `kappa * tau` against Richardson-extrapolated quadrature (check [7b]) agrees to
between 7 and 3 significant digits across eight `(tau, r_p, r_q)` configurations, the residual
being extrapolation error in the *numerical* column, not in the exact one.

Status labels, in the ficha's own vocabulary:

- **Facts C0, Lemma C1, Propositions C2, C3** — `[PROVED]`. Elementary; the two symbolic identities
  and the closed forms are machine-verified, and the reduction is cross-checked by two independent
  numerical routes.
- **Theorem C4, Lemma C5, Corollary C6** — `[PROVED (leading order)]`, with the **two** steps noted
  in §4 — (i) analyticity of `p` in `dv` at `0^+`, (ii) uniformity in `tau` of the `O(dv^2)`
  remainder — argued rather than written out, and with `dv_0` non-effective.
- **`p(tau) != p(tau')` at the named pair `(1.0, 1.2)` for the named `dv`** — `[NUMERICAL]` at
  working precision, and `[PROVED]` for all sufficiently small `dv` via Corollary C6.
- **Forma L for candidate 7.1** — `[OPEN]`. Items 1–4 of §5.

## 7. Reproduction

```text
.venv/bin/python research_program/work_packages/wp4_comparable_pair_separation_checks.py
```

Deterministic apart from check [4], whose Monte Carlo is seeded (`seed=20260725`) and reported with
standard errors. Environment: sympy 1.14.0, numpy 1.26.4, scipy 1.17.1 (the repo `.venv`; the
sealed validation path's numpy pin is untouched and irrelevant here — this script is not part of
it). The script asserts every check and exits non-zero on any failure.
