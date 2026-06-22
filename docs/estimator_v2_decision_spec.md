# Estimator-v2 — decision & specification (design only; toward pre-registration 002)

Status: **DESIGN / DECISION DOCUMENT — not a pre-registration, not sealed, not
code.** It records a committee deliberation (2026-06-22) and two user decisions
that resolve the two stability caveats surfaced in
`docs/estimator_v2_exploration.md` (Findings 3-4) **before** estimator-v2 is
integrated and re-sealed (prerequisite #2). No threshold here is set on outcome:
all evidence cited used **EXPLORE_POOL** only; the reserved prereg-002 band
`[2_000_000, 2_999_999]` was never evaluated; the sealed `nachocausal/` package,
`thresholds.py`, and the seal SHA256 (`ad02cb57…`) are **untouched**.

## Verified state (committee session 2026-06-22)

- Seal intact: `sha256 nachocausal/thresholds.py = ad02cb57…` == `addendum:122`
  (`make verify-seal`). Git `1db2a76`, `main` synced.
- Frozen **form** of success criterion (ii): `Δr/M ≤ θ_loc`,
  `θ_loc = k·ℓ/(2M)`, `ℓ = ρ^(-1/2)` (`preregistration.md:41,50`).
- Sealed **operationalisation** of (ii) (`addendum:51,96-97`): *(a)* median over
  seeds of bracket `width/(2M) ≤ 2ℓ_λ/(2M)` (ℓ from frozen intensity & fixed
  area, never realized N); *(b)* convergence-slack; *(c)* **coverage ≥ 0.5**.
- Frozen claim (`addendum:80-83`): the order-statistic bracket **covers** r_S and
  its **width contracts toward ℓ** as ρ grows; **no** asymptotic event-horizon
  claim.

## The committee's grounding correction

The exploration framed two caveats as "coverage falls 0.97→0.78" and "short patch
fails". Checked against the **actually frozen** threshold (coverage **≥ 0.5**, not
≈ 1), the picture is sharper:

| Axis | width/(2M) vs θ_loc = 2ℓ/(2M) | coverage vs frozen **0.5** |
|---|---|---|
| density I = 1500…24000 | 0.159…0.043 ≤ 0.277…0.069 — **passes, with margin** | 0.97→0.78 — **≥ 0.5 throughout** |
| patch t_edge = 12 / 6 | 0.088 / 0.086 ≤ 0.139 — passes | 1.00 / 0.93 — passes |
| **patch t_edge = 3** | 0.086 ≤ 0.139 — passes | **0.35 < 0.5 — BREACHES** |

So the **density** trend does **not** breach the frozen criterion; the only true
breach is the **short time-patch**. Mechanism at t_edge = 3: bias **+0.0262**
exceeds the bracket **half-width** (~0.0215) — the interval is decentred by more
than its own radius, hence coverage 0.35. This makes "recalibrate the interval" an
*optional strengthening*, not a forced fix, while "impose a minimum extent" is a
genuine validity condition.

## Three objects, separated (the design)

The current bracket conflates roles. The spec separates them:

1. **Point estimate** = the 2-means split **midpoint**. Primary localisation
   criterion = the already-frozen `Δr/M ≤ θ_loc = k·ℓ/(2M)`. Evidence: midpoint
   bias ≤ 0.0028 (< 0.5 % of R_S) and shrinks with ℓ; **passes**. **Not
   recalibrated.**
2. **Uncertainty interval** = the order-statistic bracket `[r_lo, r_hi]`.
   **Decision: keep the sealed operationalisation unchanged** — median
   `width/(2M) ≤ θ_loc` + convergence-slack + **coverage ≥ 0.5**; **no
   recalibration.**
3. **Valid extent domain** = `t_edge ≥ t_min`. **New** precondition (a validity
   gate on the experimental configuration, **not** a change to the estimator
   algorithm).

## Decision 1 — coverage: keep the frozen ≥ 0.5 floor, do not recalibrate

Rationale and the recorded trade-off:
- Against the frozen `coverage ≥ 0.5`, the density sweep passes everywhere
  (min 0.78). There is no failure to fix, and recalibrating *after having seen*
  the EXPLORE_POOL coverage numbers (0.78/0.85/…) carries a reverse-engineering
  risk (`preregistration.md:49`, committee auditor).
- **Domain-expert tension, recorded:** a non-calibrated interval whose width
  contracts toward ℓ will *eventually* fail to cover a point r_S once the width
  drops below the residual lattice scatter — this **is** the 0.97→0.78 decline.
  One cannot simultaneously claim "width contracts freely toward ℓ" **and**
  "controlled nominal coverage." We **keep the width-contraction claim**
  (`addendum:82`); `coverage ≥ 0.5` stays a deliberately **weak floor**, not a
  nominal-coverage guarantee.
- **Honest caveat to carry into prereg-002:** the monotone margin decline
  (0.97→0.78 over ρ = 208→3333) is a **documented, expected property** of the
  min/max bracket, not a defect; it must be reported as such alongside any PASS.
  If a future programme wants a *calibrated* interval, that is a **new** criterion
  with its own principled anchor, frozen on EXPLORE_POOL, and a separate re-seal —
  explicitly out of scope here.

Consequence: estimator-v2's interval semantics are **unchanged**. The only
estimator changes that motivate the eventual re-seal remain those from
Findings 1-2 (HEIGHT→VOLUME observable; the data-independent `τ(n)` abstaining
gate). This decision **shrinks** the re-seal surface.

## Decision 2 — minimum extent: t_min by "bias ≤ half-width", plateau-confirmed

`t_min` = the smallest `t_edge`, **at the reference density ρ = 833** (the matched
density of Finding 4's patch sweep), such that **all** hold and are **flat
(plateau) up to 2·t_edge**:

1. `|bias| = |mean midpoint − R_S| ≤ bracket half-width` (the sharp discriminator:
   t_edge = 3 fails it — 0.0262 > 0.0215; t_edge = 6, 12 pass it);
2. `coverage ≥ 0.5` (consistent with Decision 1's frozen floor);
3. the above are **stable** across `[t_edge, 2·t_edge]` (the plateau, guarding
   against a single-point coincidence).

Provisional reading from the existing three points: **t_edge = 3 is
out-of-domain**; **t_edge = 6** (the sealed `T_EDGE`) sits on the plateau
(coverage 0.93, bias −0.0022 ≪ half-width); t_edge = 12 confirms the plateau
(1.00, −0.0014). The exact boundary `t_min ∈ (3, 6]` is **not yet pinned** — the
three points jump 3→6.

> Patches with `t_edge < t_min` are declared **out of the experiment's domain of
> validity**, not "corrected" by inflating the bracket. The sealed prereg-001
> endpoint (t_edge = 6) is in-domain.

## Pre-commit guardrails (carry to the freeze)

- **Anchoring discipline preserved** (`preregistration.md:49`): no threshold
  reverse-engineered from seen outcomes. Decision 1 changes nothing frozen;
  Decision 2 adds a domain precondition anchored to a *structural* property (bias
  vs. its own interval radius), not tuned to a target number.
- **EXPLORE_POOL only**, sealed package untouched, reserved band never evaluated —
  true of every datum above and of any confirmatory sweep below.
- **One re-seal, later** (prereq #2/#5): integrate VOLUME + `τ(n)` gate (+ the
  `t_min` domain gate as a config precondition) into the path `validate.run()`
  executes, with tests and a single new seal SHA. Held-out seeds drawn from the
  reserved 002 band **only at sealing time**. Today's document touches no code,
  no seal.

## Open items / next reversible step

1. **Pin `t_min` (confirmatory fine sweep).** A reversible EXPLORE_POOL pre-flight
   over `t_edge ∈ {4, 5, 6, 8, 10}` at ρ = 833, applying the Decision-2 criterion,
   to locate the plateau edge in (3, 6] and confirm flatness. Until then `t_min`
   is provisionally `6` (the sealed value, known in-domain). Should also check
   whether `t_min` is density-dependent (re-run at ρ = 1667, the primary
   endpoint).
2. **Freeze** `t_min` (and re-affirm the unchanged coverage criterion) on
   EXPLORE_POOL **before** any prereg-002 held-out seed is seen.
3. **Then** prerequisite #2: integrate + re-seal once; **then** prerequisite #3:
   freeze prereg-002; **then** the single blind run.
