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
> `[OPEN por par]` since v2 of that ficha — for this family. Together with the exact fixed-`n`
> variance identity of §4b, it supports the narrowly scoped two-point result recorded in §6:
> `fixed_n` only, diamond family only, and only for sufficiently small `dv`. It does not license a
> Poisson-unconditioned, reconstruction, localisation, or 3+1D claim.
>
> **Addendum 2026-07-25 (§4b).** The variance side is now done too: the first Hoeffding projection
> `h_1` is in closed form (Prop C7), `zeta_1 = Var(h_1) > 0` strictly (Prop C8), `zeta_1 = 1/36 +
> O(dv^2)` (Thm C9), and `Var(S_n) = Theta(n^3)` is verified against Monte Carlo. This **closes item
> 3** of §5 and reduces item 4 to the single inequality `zeta_1 * Ibar >= kappa^2 dv^2 / 54`. Forma
> The former channel blocker is removed only for the conditioned `fixed_n` Chebyshev route; the
> constant-level efficiency question and the one-way `Ibar` defeater remain open.
>
> **Addendum 2026-07-29 (§4).** The two analytic steps previously only argued are now written out.
> After pulling the varying diamond back to the unit square, the ray flow gives a jointly
> real-analytic extension `P(tau, dv)` through `dv = 0`. Taylor's formula on a compact rectangle
> yields both `|R| <= C_0 dv^2` and `|partial_tau R| <= C_1 dv^2`, uniformly in `tau`. The derivative
> bound — stronger than the absolute remainder bound alone — closes Corollary C6 for the whole
> compact `tau` interval. The proof does not numerically evaluate `C_1` or certify a named `dv_0`.
>
> Verification script (all checks pass, exit 0, ~9 s):
> `wp4_comparable_pair_separation_checks.py`, run with
> `PYTHONDONTWRITEBYTECODE=1 python3
> research_program/work_packages/wp4_comparable_pair_separation_checks.py`.

## 1. The question, in the ficha's own terms

Ficha §2.1(B) reduced candidate 7.1 (number of comparable pairs) to *one* unverified scalar
inequality, having imported Reitzner–Schulte 2013 for the fluctuation ingredient:

> **Lo que NO cierra — el único punto que falta:** `p(theta) != p(theta')` para el par concreto
> que se quiera usar (WP4 diamante, OP-1.1/1.2, u otro). Sigue `[OPEN por par]` … la
> inyectividad de `tau -> c_tau` (WP4 Prop 5) no implica la de `tau -> p(tau)`.

That last clause is the crux and it is correct: Proposition 5 of `wp4_fisher_localization_floor.md`
proves `tau -> c_tau` injective, but `p` is a single real functional of `c_tau`, and injectivity of
a family says nothing about injectivity of a scalar reduction of it. This annex computes the scalar.

**Convention note.** Throughout the ficha and this annex, `p(theta)` is the probability that two
i.i.d. points are *comparable*, i.e. `2 int int 1[x prec y] dc dc` because exactly one of
`x prec y`, `y prec x` holds a.s. This annex computes that quantity, written `p(tau)` throughout,
and reports Kendall's `tau_K = 2 p - 1` alongside.

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

**Theorem C4 (joint analytic extension and uniform remainder).** Fix
`0 < r_q < tau_0 <= tau_1 < r_p` and put `K := [tau_0, tau_1]`. There are
`epsilon > 0` and finite constants `C_0, C_1`, depending only on
`(r_p, r_q, tau_0, tau_1)`, such that for every `tau in K` and
`0 < dv <= epsilon`,

```text
p(tau) = 1/2 + kappa(r_p, r_q) * tau * dv + R(tau, dv),
kappa(r_p, r_q)
  = [ (r_p^2-r_q^2) - 2 r_p r_q log(r_p/r_q) ]
    / [ 12 r_p r_q (r_p-r_q)^2 ],

|R(tau, dv)|             <= C_0 dv^2,
|partial_tau R(tau, dv)| <= C_1 dv^2.
```

*Proof.* Write `a := r_p`, `b := r_q`, `d := dv`, and
`Rho(tau,r,D) := rho_tau(r,D)`. We first remove both moving integration boundaries and the apparent
singularity at `d = 0`.

**Step 1: the ray flow is jointly analytic on one uniform neighbourhood.** It is defined implicitly
by

```text
F(tau,r,D,y) := omega_tau(y) - exp(D/(2 tau)) omega_tau(r) = 0.
```

At `D = 0`, `y = r`, while
`partial_y F = omega_tau'(y) = y exp(y/tau)/tau^2 > 0`. The real-analytic implicit-function theorem
therefore makes `Rho` real-analytic in `(tau,r,D)` near every `(tau,r,0)` with
`tau > 0`, `r > 0`. Choose a compact `tau`-interval slightly larger than `K` but still inside
`(b,a)`, and a compact positive `r`-interval whose interior contains `[b,a]`. A finite subcover of
their product gives a single
`eta > 0` on which `Rho` is jointly analytic for `|D| < eta`. Shrinking `eta` if needed keeps every
radius below inside that same positive `r`-interval; the local branches agree because
`omega_tau` is strictly increasing. Equivalently, the explicit formula
`Rho=tau[1+W_0(exp(D/(2tau)) omega_tau(r)/e)]` makes the uniform choice transparent: on those
compact intervals and for small uniform `|D|`, the argument of `W_0` stays in a compact subset of
`(-1/e,infinity)`, away from its branch point.

**Step 2: pull Proposition C3 back to a fixed square and factor the vanishing orders.** For
`s,u in [0,1]` set

```text
A(tau,s,d) := Rho(tau,a,(1-s)d),
B(tau,s,d) := Rho(tau,b,-s d),
x(tau,s,u,d) := B + u(A-B),
H(tau,s,u,d) := Rho(tau,x,s d)^2 + B^2 - x^2 - b^2.
```

Since `A-B=a-b>0` at `d=0`, one uniform shrink of `eta` also ensures `A>B` on the compact
`(tau,s)` domain for `0<d<eta`; this is the physical slice orientation.
For positive `d`, the substitutions `D = s d` and `r = B + u(A-B)` turn the numerator `N` of
Proposition C3 into

```text
N(tau,d) = d int_0^1 int_0^1 (A-B) H du ds.
```

All factors are jointly analytic. At `d = 0`, `A=a`, `B=b`,
`x=b+u(a-b)`, and `H=0`. Hence analytic division by `d` (equivalently,
`H/d = int_0^1 partial_d H(tau,s,u,lambda d) dlambda`) gives a jointly analytic `Hhat` with
`H=d Hhat`. Consequently

```text
N(tau,d) = d^2 Nhat(tau,d)
```

for a jointly analytic `Nhat`, including at `d=0`: compactness of the unit square supplies one
common analytic neighbourhood, so its convergent local power series may be integrated term by term.

The patch volume satisfies

```text
V(tau,d) = Rho(tau,a,d)^2 + Rho(tau,b,-d)^2 - a^2 - b^2
         = d Vhat(tau,d).
```

Indeed `V(tau,0)=0`, and the ray ODE gives

```text
partial_d V(tau,0)
  = 2a (a-tau)/(2a) - 2b (b-tau)/(2b)
  = a-b.
```

Analytic division, now written
`Vhat(tau,d)=int_0^1 partial_d V(tau,lambda d) dlambda`, shows that `Vhat` is jointly analytic and
`Vhat(tau,0)=a-b>0`, uniformly in `tau`. After one more uniform shrink of `eta`, `Vhat` has no zero
on a neighbourhood of `K x {0}`. Therefore

```text
P(tau,d) := 2 Nhat(tau,d) / Vhat(tau,d)^2
```

is a jointly real-analytic extension through `d=0` of the physical probability `p(tau)` for
`d>0`.

**Step 3: identify the first two coefficients.** Expand the analytic ray flow from its ODE,

```text
Rho(tau,r,D)
  = r + D (r-tau)/(2r) + D^2 tau(r-tau)/(8r^3) + O(D^3),
```

substitute into the fixed-square formula above, and integrate the retained coefficients. The
elementary antiderivatives are `r(r-2tau)/2`, `r/4-tau log(r)/4`, and their polynomial
combinations. The resulting coefficients are

```text
Nhat(tau,0) = (a-b)^2/4,       Vhat(tau,0) = a-b,
P(tau,0) = 1/2,               partial_d P(tau,0) = kappa(a,b) tau.
```

This is exactly the closed algebra checked symbolically in check [7]; Steps 1–2 now license the
coefficient extraction from that series.

**Step 4: obtain the uniform bounds.** Choose `0 < epsilon < eta` so that the closed rectangle
`K x [-epsilon,epsilon]` lies in the analytic domain of `P`, and define the finite constants

```text
C_0 := (1/2) max_{K x [-epsilon,epsilon]} |partial_d^2 P|,
C_1 := (1/2) max_{K x [-epsilon,epsilon]} |partial_tau partial_d^2 P|.
```

Taylor's formula with integral remainder gives, for `0 <= d <= epsilon`,

```text
R(tau,d)
  = d^2 int_0^1 (1-z) partial_d^2 P(tau,z d) dz,

partial_tau R(tau,d)
  = d^2 int_0^1 (1-z) partial_tau partial_d^2 P(tau,z d) dz.
```

The two asserted bounds follow simultaneously and uniformly in `tau`. ∎

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

*Proof.* Put `kappa := kappa(r_p,r_q)>0`. The derivative bound in Theorem C4 gives

```text
partial_tau p(tau) >= kappa dv - C_1 dv^2.
```

If `C_1=0`, take `dv_0=epsilon`; otherwise take
`dv_0=min{epsilon, kappa/(2C_1)}`. Then
`partial_tau p(tau) >= kappa dv/2 > 0` throughout `[tau_0,tau_1]` whenever
`0<dv<dv_0`, proving strict increase and hence the asserted inequality. Notice that the absolute
uniform bound on `R` alone would prove separation only for each pre-fixed pair; the
`partial_tau R` bound is what makes one `dv_0` work for the whole interval. ∎

**Quantifier ledger.** The uniformity just proved concerns the small-lapse radius, not the testing
cardinality. More precisely:

1. There is one `dv_0= dv_0(r_p,r_q,tau_0,tau_1)>0` such that, for every fixed
   `0<dv<dv_0` and all `tau,tau' in K`,

   ```text
   |p(tau')-p(tau)| >= (kappa dv/2) |tau'-tau|.
   ```

2. In the `fixed_n` channel, for every such fixed `dv` and every fixed pair
   `tau != tau'`, midpoint Chebyshev and data processing give

   ```text
   TV(Q^n_tau,Q^n_tau')
     >= 1 - 4(2n-3) / [n(n-1) |p(tau')-p(tau)|^2]  -> 1.
   ```

   Thus `n_0` depends on `(dv,tau,tau')` (and on the requested error level).

3. No `n_0` is uniform over all distinct pairs in `K`, because `|tau'-tau|` may approach zero.
   If one restricts instead to `|tau'-tau|>=eta>0`, the first display gives the uniform gap
   `|Delta_p| >= kappa dv eta/2`, and the same Chebyshev bound supplies an `n_0` uniform over that
   separated parameter set.

**Consistency with scale invariance.** `kappa` is homogeneous of degree `-2`, so `kappa * tau * dv`
is invariant under `(tau, r_p, r_q, dv) -> s (tau, r_p, r_q, dv)` — as it must be, since `p` is
(check [6]). This is a nontrivial check on the closed form: an algebra slip would generically
break it.

**Quantitative caveat.** The proof defines valid constants `C_0`, `C_1` as compact suprema and gives
`dv_0=min{epsilon,kappa/(2C_1)}` when `C_1>0`, but it does **not** evaluate or certify those suprema
numerically. Thus Corollary C6 is now fully proved and uniform in `tau`, but no named `dv` is admitted
by the analytic bound alone. The named values in §6 remain numerical statements at working
precision.

## 4b. Variance at fixed `n`, and non-degeneracy (added 2026-07-25)

`S_n` = number of comparable pairs among `n` i.i.d. points of `D_tau`. It is a `U`-statistic with
the symmetric kernel `f(x,y) = 1[x, y comparable]`, so its exact Hoeffding variance is

```text
Var(S_n) = C(n,2) [ 2 (n-2) zeta_1 + zeta_2 ],
zeta_1 = Var( h_1(X) ),   h_1(x) := P( x comparable with Y ),   zeta_2 = Var(f) = p (1-p).
```

**Proposition C7 (`h_1` in closed form).** For `x = (v_x, r_x)` in `D_tau`, with `D := v_q - v_x`
and `D' := v_x - v_p = dv - D`,

```text
h_1(x) = [ vol(J^+(x) ^ D_tau) + vol(J^-(x) ^ D_tau) ] / V(tau),
vol(J^+(x) ^ D_tau) = rho(r_x, D)^2  + rho(r_q, -D)^2  - r_x^2 - r_q^2,
vol(J^-(x) ^ D_tau) = rho(r_p, D')^2 + rho(r_x, -D')^2 - r_p^2 - r_x^2.
```

*Proof.* `J^-(x) ^ D_tau = J^+(p) ^ J^-(x)` because `x in J^-(q)` gives `J^-(x) subset J^-(q)`;
then apply Proposition C2 to the pair `(p, x)` exactly as it was applied to `(x, q)`. ∎

So `zeta_1` is one more 2D integral of the same kind, with the same spectral convergence.
**A free consistency check comes with it:** `h_1` is assembled from *both* time directions and must
average back to `p`, since `E[h_1(X)] = 2 V^{-2} int vol(J^+(x) ^ D) dV = p`. Verified to
`|diff| = 7.77e-16` at `dv = 4` and `9.10e-15` at `dv = 0.02` (check [10]) — an independent test of
Proposition C2 in the past direction, which nothing before this section exercised.

**Proposition C8 (non-degeneracy).** `zeta_1 > 0` strictly, for every admissible
`(tau, r_p, r_q, dv)`.

*Proof.* `h_1` is continuous on the compact `D_tau`, so it suffices that it is non-constant.
`h_1(p) = h_1(q) = 1`: `D_tau subset J^+(p)` and `D_tau subset J^-(q)`, so both corners are
comparable with everything. For interior `x`, the set of points spacelike to `x` is the union of the
two open rectangles `{Utilde < Utilde_x, v > v_x}` and `{Utilde > Utilde_x, v < v_x}` of the null
box, both of positive measure, so `h_1(x) < 1`. ∎ (Check [11] exhibits the range,
`h_1 in [0.000265, 0.999852]` at `dv = 4`.)

**Theorem C9 (the independence-limit value, exact).** `zeta_1 -> 1/36` as `dv -> 0^+`, and the
correction is second order: `zeta_1 = 1/36 + O(dv^2)`.

*Proof of the limit.* As `dv -> 0` the copula tends to independence (§3), so in rank coordinates
`h_1(u,w) = u w + (1-u)(1-w)`. Substituting `a = u - 1/2`, `b = w - 1/2` gives the exact identity
`h_1 = 1/2 + 2 a b` with `a, b` independent `U(-1/2, 1/2)`, whence
`zeta_1 = 4 Var(ab) = 4 E[a^2] E[b^2] = 4 (1/12)^2 = 1/36`. ∎ The `O(dv^2)` order is
`[NUMERICAL]`: successive halvings of `dv` give ratios `2.17, 2.97, 3.44, 3.70, 3.85 -> 4`
(check [11]). Note this is *one order better* than `p` itself, whose correction is `O(dv)`.

**Consequences.** `Var(S_n) = Theta(n^3)` with leading coefficient `zeta_1`, so the Chebyshev step
of ficha §6.3 is available and the statistic is non-degenerate — item 3 of §5 below is **closed**.
Numbers for the diamond of record (`r_p = 3`, `r_q = 0.5`, `tau = 1`): `zeta_1 = 0.02733369969886`
at `dv = 4`, `0.02777783467369` at `dv = 0.02`. The exact finite-`n` formula was verified against
Monte Carlo at `n = 5, 10, 20` — `0.73`, `0.31`, `0.14` sigma (check [12]).

**The §6.4 consistency check, now at the level of constants.** Combining the Chebyshev lower bound
with `Delta_p = kappa dv delta` and `sigma^2 ~ n^3 zeta_1`,

```text
TV >= 1 - 32 zeta_1 / ( n kappa^2 dv^2 delta^2 )   against   TV <= (delta/2) sqrt(n Ibar)  [WP4 §5].
```

Both sides depend on `n` and `delta` only through `t := delta sqrt(n)`, so the requirement that the
lower bound never exceed the proved upper bound is one scalar inequality. Minimising
`B t + A/t^2 - 1` over `t > 0` (with `A = 32 zeta_1/(kappa^2 dv^2)`, `B = sqrt(Ibar)/2`) gives
`3 A^{1/3} B^{2/3} / 2^{2/3} >= 1`, i.e. `A B^2 >= 4/27`, i.e.

```text
zeta_1 * Ibar >= kappa^2 dv^2 / 54,     and with zeta_1 = 1/36:   Ibar >= (2/3) kappa^2 dv^2.
```

(Derived symbolically, check [13].) **This is a one-way test:** violation would refute the chain;
satisfaction proves nothing. It is **stated, not executed** — `Ibar` for these corners is still not
computed. Numerically the requirement is `Ibar >= 9.754357e-03` at `dv = 4` and
`2.399599e-07` at `dv = 0.02`.

*Why the test is not as weak as those small numbers suggest* `[UNVERIFIED — reasoning, not
computed]`. As `dv -> 0` the family degenerates toward independence, so `Ibar` should vanish too:
with `c_tau = 1 + eps g_tau` and `eps ~ dv`, the score is `~ eps partial_tau g` and hence
`Ibar ~ C dv^2` for some constant `C`. If so, **both** sides of the requirement are `O(dv^2)`, it
becomes `dv`-free at leading order, and reduces to `C >= (2/3) kappa^2` — a genuine comparison of
two constants, neither trivially satisfied nor trivially violated. The `dv`-scaling of `Ibar` has
not been computed here; establishing it (and `C`) is the precise remaining step, and it is the same
object WP4 §5a has only as `[NUMERICAL]` `V*Ibar` for one reference shape.

## 5. What this closes, and what it does NOT

**Closed.** Ingredient (a) of ficha §7.1 — `p(theta) != p(theta')` — for the WP4 §4 diamond
family. Together with ficha §2.1(B) (Reitzner–Schulte 2013, fluctuation ingredient with an
explicit `lambda^{-1/2}` rate uniform in `theta`), the *mean-separation* and *fluctuation*
ingredients 1 and 2 of ficha §6 are now both in hand for candidate 7.1 on a named family.

**Channel split and remaining limits.** The unconditioned Poisson route remains contaminated, but
the conditioned `fixed_n` route is closed at leading order by the exact U-statistic moments plus
Chebyshev; no CLT or de-Poissonisation is used in that route.

1. **The cardinality confounder is live in the very channel where Reitzner–Schulte applies.**
   Their CLT is for *unconditioned Poisson* U-statistics (`lambda -> infinity`, mode 1 of ficha
   §1.3). But this family has a `tau`-dependent volume (check [4b]):
   `V(1.0) = 11.501608349297` against `V(1.2) = 10.794261266781` at `dv = 4` (relative difference
   `6.150e-02`), and `0.049967998677` against `0.049922210322` at `dv = 0.02` (`9.164e-04`). With
   `rho` known, the marginal `N ~ Poisson(rho V(tau))` therefore separates `tau` from `tau'` **on
   its own**, which is exactly the trivial mechanism ficha §1.2 and §9.2 forbid counting. Any
   Forma L built in that channel would be contaminated unless the statistic is normalised (e.g.
   `S / C(N,2)`, whose law is *not* what Reitzner–Schulte controls) or the channel conditioned.
2. **The honest channel is `fixed_n`.** Conditioning on `N = n` removes the confounder (ficha §1.3
   mode 3, FWP Lemma 0). Reitzner–Schulte's Poisson CLT does not apply there, but it is not needed:
   `E S_n = C(n,2)p` and the exact variance identity below give the two-point Chebyshev bound
   directly. De-Poissonisation remains only an optional route to a finer distributional constant.
3. ~~The variance asymptotics are not verified here.~~ **CLOSED 2026-07-25, §4b.** `zeta_1 > 0`
   strictly (Proposition C8, proved), `zeta_1 = 1/36 + O(dv^2)` (Theorem C9), and
   `Var(S_n) = C(n,2)[2(n-2) zeta_1 + zeta_2] = Theta(n^3)` verified against Monte Carlo at
   `n = 5, 10, 20`. The Chebyshev step of ficha §6.3 is therefore available. Consequence worth
   stating: with the variance in hand, the comparable-pair count is **rate-optimal in `n`** against
   WP4 §5's proved floor — both the Chebyshev threshold and the point at which the upper bound
   becomes informative sit at `delta ~ n^{-1/2}`.
4. **Ficha §6.4's consistency check is now reduced to a single scalar inequality, still
   unexecuted.** §4b shows the requirement is exactly `zeta_1 * Ibar >= kappa^2 dv^2 / 54`, i.e.
   `Ibar >= (2/3) kappa^2 dv^2` in the small-`dv` regime. With `zeta_1` computed, the only missing
   quantity is `Ibar` for *these* corners — WP4 §5a has `V * Ibar` only `[NUMERICAL]` and for one
   reference shape. The test is one-way (violation refutes, satisfaction proves nothing), and the
   `[UNVERIFIED]` reasoning in §4b suggests both sides are `O(dv^2)`, so it is not vacuous.
   `[OPEN — one number missing]`

**Also not claimed.** (i) Nothing here is about the 3+1D Schwarzschild pairs of FWP §2 or OP-1.2;
those are Theorem-A pairs, where `p` is necessarily *equal* (same copula) — and check [6] confirms
the statistic respects that rather than falsely separating them. (ii) No monotonicity claim at
arbitrary `dv`: the numerics show `p` *decreasing* in `tau` at `dv = 4`, far outside the asymptotic
regime, while Corollary C6 proves uniform increase on a fixed compact `tau` interval only for
sufficiently small `dv`. The theorem is asymptotic and is stated as such.
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
- **Theorem C4, Lemma C5, Corollary C6** — `[PROVED]`. Theorem C4 constructs the joint analytic
  extension and proves `C^1`-uniform `O(dv^2)` control; Corollary C6 uses the derivative bound to make
  one `dv_0` work on the whole compact `tau` interval. `dv_0` is proof-defined but not numerically
  certified. The downstream `fixed_n` convergence `TV -> 1` is for each fixed pair; its `n_0`
  remains pair-dependent unless a positive minimum separation `|tau'-tau|>=eta` is imposed. This is
  the internal mathematical status of a working draft; external adversarial review remains pending.
- **`p(tau) != p(tau')` at the named pair `(1.0, 1.2)` for the named `dv`** — `[NUMERICAL]` at
  working precision, and `[PROVED]` for all sufficiently small `dv` via Corollary C6.
- **Propositions C7, C8** (`h_1` closed form; `zeta_1 > 0`) — `[PROVED]`. **Theorem C9**: the limit
  `zeta_1 -> 1/36` is `[PROVED]` (exact, via `h_1 = 1/2 + 2ab`); the `O(dv^2)` *order* of the
  correction is `[NUMERICAL]`.
- **`Var(S_n) = C(n,2)[2(n-2) zeta_1 + zeta_2]`** — `[PROVED]` (standard Hoeffding decomposition),
  and `[NUMERICAL]`-confirmed against Monte Carlo at `n = 5, 10, 20`. `zeta_1` itself is
  `[NUMERICAL]` (quadrature) except for its `dv -> 0` limit.
- **`zeta_1 * Ibar >= kappa^2 dv^2 / 54`** (§6.4 consistency requirement) — `[PROVED]` as a
  *requirement* derived from the two bounds; **not evaluated**, since `Ibar` is unknown for these
  corners. The claim that both sides are `O(dv^2)` is `[UNVERIFIED]` reasoning.
- **Adopted label block (PI C3/C4, 2026-07-27; retained below as historical wording).**

  ```text
  FORMA_L_FUERTE_fixed_n
    = PROVED_LEADING_ORDER / NON_EFFECTIVE_x2 / TWO_POINT_ONLY / DIAMOND_FAMILY_ONLY

  [PROVED (orden dominante en dv; la analiticidad de p en dv en 0^+ queda argumentada, NO escrita)
  — CONSISTENCIA DE TEST A DOS PUNTOS, canal fixed_n, familia diamante WP4 §4 ÚNICAMENTE]

  Para todo (r_p, r_q) admisible y todo par FIJO tau != tau' en (r_q, r_p), EXISTE dv_0 > 0 NO
  EFECTIVO tal que para todo 0 < dv < dv_0, TV(Q^n_tau, Q^n_tau') -> 1 cuando n -> infinito.
  NO EFECTIVO DOS VECES: dv_0 y n_0(dv, tau, tau'). SIN UNIFORMIDAD en (tau, tau').
  El régimen documental fijado es dv = 0.02; dv = 4 se reporta como fuera del régimen probado.
  NO es estimador, localización, reconstrucción ni 3+1D. DEFEATER VIVO (no premisa):
  zeta_1 * Ibar >= kappa^2 dv^2 / 54, enunciado y NO ejecutado.

  EFICIENCIA_CONSTANTE_fixed_n = OPEN_CONSTANT_LEVEL_ONLY
  [OPEN — SÓLO A NIVEL DE CONSTANTES]: permanecen abiertos el prefactor verdadero de TV(Q^n), la
  pérdida constante de la compresión Iso_n -> S_n y el chequeo unidireccional con Ibar. Ni
  observable nuevo, ni CANDIDATE_7, ni estimador.

  S_N_BLINDNESS_AT_dv_star = PROVED_EXISTS (dv* no localizado)
  Existe dv* in (0.02, 4) con Delta_p(dv*) = 0 exactamente; S_n es ciego a nivel de medias allí
  para todo n. Ninguna afirmación se extrapola fuera de dv < dv_0.
  ```

  **Mathematical update 2026-07-29.** Theorem C4 now closes the analyticity and uniform-remainder
  caveats, and Corollary C6 proves the stronger common-`dv_0` statement on every fixed compact
  `tau` interval. Consequently, the historical line `SIN UNIFORMIDAD en (tau,tau')` is superseded
  as a statement about `dv_0`; it remains valid only for the pair-dependent testing cardinality
  `n_0` when no minimum parameter separation is imposed. The historical block is not silently
  rewritten here: promoting its governance label, propagating the result into the manuscript, and
  computing a certified numerical `dv_0` are separate documentary or quantitative actions not
  performed in this addendum.

## 7. Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 research_program/work_packages/wp4_comparable_pair_separation_checks.py
```

Deterministic apart from check [4], whose Monte Carlo is seeded (`seed=20260725`) and reported with
standard errors. Verified environment in this checkout: Python 3 with sympy 1.14.0, numpy 1.26.4,
scipy 1.17.1. The sealed validation path's numpy pin is untouched and irrelevant here — this script
is not part of it. The script asserts every check and exits non-zero on any failure.
