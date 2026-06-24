# PR-003 S3 — iterative-reseed v1 (HARDEN): 3rd density + τ(n) stopping rule (dev, NOT a result)

Sandbox notes for `docs/comite/comite_decision_002_*` §9 **S3**. Produced by
`dev/measure_iterative_reseed_v1.py` (reuses the SEALED v2 localiser untouched; advance is
dev-side accounting only). **Exploration only — nothing frozen, not validated, not audited.**
Scored with hidden `r` (reveal ONLY to score; construction + the abstain cut are order-only).
6 seeds `EXPLORE_POOL[:6]`, t_edge=6, `RESERVED_002` untouched. `make verify-seal` =
`6e2c3888…` **before and after** (`dev/iterative_reseed_v1.log:3`).

## What S3 changed over v0 (no new rule, no threshold touched)

1. **3rd density 14400** (criterion (d): does coverage/persistence converge?).
2. **Honest coverage.** v0's `cover_frac` was `covers / localised`, silently dropping the
   abstaining + degenerate fronts from BOTH the locus and the denominator — biased UP
   (falsifier, `comite_decision_002` §5 "verdict coercion 3"). v1 counts every candidate
   front (size ≥ NMIN=8); abstain + degenerate count as **misses**. Reports both rates.
3. **τ(n) as the order-only stopping rule + alignment diagnostic.** The frozen `τ(n)` gate
   (`fixtures/tau_table.json`, sealed) is the principled order-only stop — NOT a new rule.
   Diagnostic (r scores only, never cuts): among the fronts τ(n) abstained on, what fraction
   *would* have covered R_S if forced? If ≪ the localised cover-rate, τ(n) drops the
   non-covering tail (good stopping rule).

## Result (2026-06-24, 6 seeds, t_edge=6) — convergence table

| intensity |   ℓ    | n_loc/seed | d⊥/ℓ | phys d⊥ | cov OPT | cov HONEST | abstain | abst would-cover | conn | r-IQR | Guard-v | MINK ctrl |
|----------:|-------:|-----------:|-----:|--------:|--------:|-----------:|--------:|-----------------:|-----:|------:|:-------:|:----------|
|    3600   | 0.0447 |     96     | 0.52 | 0.0231  |   74%   |  **51%**   |   30%   |       40%        | 90%  | 0.0417|  6/6    | PASS (4 fronts, cov 1%) |
|    7200   | 0.0316 |    146     | 0.63 | 0.0199  |   65%   |  **48%**   |   26%   |       37%        | 95%  | 0.0309|  6/6    | PASS (4 fronts, cov 1%) |
|   14400   | 0.0224 |    234     | 0.88 | 0.0198  |   54%   |  **44%**   |   17%   |       35%        | 93%  | 0.0296|  6/6    | PASS (14 fronts, cov 2%) |

## Reading (precise — verdict and what it does / does NOT show)

**Verdict S3: the convergence criterion does NOT hold.** The roadmap's pre-committed bar for
Fase #1 is "coverage no se degrada (idealmente mejora) con densidad"
(`hoja_de_ruta_24_jun_2026.md:64,80`). Across the third density:

- **Coverage degrades monotonically** — HONEST 51%→48%→**44%**, OPTIMISTIC 74%→65%→**54%**.
  Adding 14400 did not arrest it; it continued the 3600→7200 decline. Under the stated bar
  this is a **FAIL of convergence**, not a caveat (falsifier, §5 "verdict coercion 2").
- **Per-piece bracket widens in ℓ-units** — d⊥/ℓ 0.52→0.63→**0.88**. Physical d⊥ plateaus
  ~0.020 (each piece stays O(ℓ)-adherent in absolute terms), but it is **not tightening
  relative to the discreteness scale** as density rises.

**What genuinely survives (honest, but does not rescue the verdict):**
- **Breadth grows:** localising fronts 96→146→**234** (more of the patch's t* sampled).
- **Connectivity high & stable** (90→95→93%) and **robust scatter shrinks** (IQR 0.042→0.030,
  below `θ_stab` at all three). Guard-v relabel **6/6** at every density; **MINK flat control
  PASSES** at every density (≤14 stray fronts, honest coverage ≤2% — locus is BH-specific).
- **τ(n) IS a working order-only stopping rule.** At every density the abstained fronts'
  would-cover rate (40/37/35%) sits well **below** the localised cover-rate (74/65/54%): the
  frozen gate preferentially abstains on the non-covering tail. This answers Fase #2's
  question ("is there an order-only stopping rule?") affirmatively — `τ(n)` is one.
  **But it is not strong enough to make coverage converge:** it removes part of the tail, and
  at 14400 it abstains *less* (17%), readmitting non-covering fronts (cov_opt → 54%).

**Why coverage falls (physics, honest):** consistent with the EGS truncation picture the
committee flagged — interior outgoing futures starve, biasing localised fronts; higher density
thins interior ladders rather than thickening the adherent core. This is the **same
density-fragility EGS mark as a known open problem of the ladder method** (md:469); iterative
re-seeding **inherits, does not escape** it. (Same direction as the expansion variant's S1/S2
NEGATIVE, `dev/PR003_EXPANSION_ROBUSTNESS_NOTES.md`.)

**Caveats / scope (honest):**
- dev / v0–v1 / scored with hidden `r` — **NOT frozen, NOT validated, NOT audited**.
- "connected" is the weak notion (any causal link between adjacent fronts, not a through-chain).
- per-front localisation **reuses** the sealed v2 localiser; the only advance was the connected
  ordered subset + honest accounting, neither a new localisation principle nor a passing one.
- t_edge=6 (EGS sharpen the contrast only at t*/r_S∈[0,50], ~8× longer); a taller-box committing
  run would need a NEW prereg (different BOX_AREA/ℓ-table), out of scope for this dev step.
- no "apparent horizon" framing is made; only order-only localisation of hidden r_S within the
  bracket in a finite 1+1D patch.

## Consequence (per the plan)

`comite_decision_002` §9 and the user's S3 charge pre-committed: **if S3 does not hold, PR-003
enters Fase #3 — accept `BARE_RELOCALISATION` as the achievable-scale result.** S3 did not hold
(coverage degrades at the third density). The honest label for iterative-reseed across v0+v1 is
**INCONCLUSIVE-as-an-extended-object / NEGATIVE on convergence**: it does NOT establish a
density-robust extended horizon locus. It DOES leave on the record two true sub-findings — a
working order-only stopping rule (`τ(n)`), and a per-piece adherent, connected, relabel- and
flat-control-robust locus whose *breadth* grows — none of which survive as a *converging
extended object*.

**Open uncertainty (one line, no plan):** whether ANY order-only construction (not just this
re-seed) can make the extended locus' coverage density-robust in this 1+1D patch is left open;
on the cascade's evidence (expansion S1/S2 NEGATIVE; re-seed S3 non-converging) the extended
object is set aside and PR-003 consolidates on the measured bound.
