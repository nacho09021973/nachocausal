# Estimator-v2 — FROZEN input contract (prerequisite #1 freeze)

Status: **FROZEN documentary contract.** This is the **immutable input** to
prerequisite #2 (integrate estimator-v2 into the audited path + a single
re-seal). It contains **no code and changes no seal** — the sealed
`nachocausal/thresholds.py` SHA256 is still `ad02cb57…` and stays so until #2's
single re-seal. Once committed, #2 must implement **exactly** this contract and
nothing it does not state. All evidence below is **EXPLORE_POOL** only; the
reserved prereg-002 band `[2_000_000, 2_999_999]` was never evaluated.

## Immutable provenance

- **Decision/deliberation** (committee 2026-06-22 + user decisions):
  `docs/estimator_v2_decision_spec.md` at **commit `bb21147`**, git blob
  `d5358d345fb4b550b1ced4b6b39016de4ed102c2`, content
  **SHA256 `44f544952513bb5b7ef2bb55bdbda3831f321b94c1ebe9e86ed9e2caa5595e85`**.
- **Frozen baseline** (inherited verbatim except the change-list below):
  prereg-001 addendum `docs/preregistration_001_addendum.md`, seal
  `ad02cb57e1445ca83a489bd4f3f9cae151517ca2aedbd1b29c44c60ac65f7faa`.
- **Empirical support**: Findings 1–4 in `docs/estimator_v2_exploration.md`;
  t_min pinned by `dev/explore_tmin.py` (2026-06-22).

## Scope — what this freeze does / does not do

- **Does:** fix the estimator-v2 observable, point estimate, gate, domain, and
  the localisation-criterion treatment as an immutable contract for #2.
- **Does NOT:** touch any code or the seal SHA (that is #2's single re-seal); draw
  or fix prereg-002 held-out seeds (that is #3, at sealing time).

---

## Frozen clauses

### A. Observable — future VOLUME
`O_min(i) = |future(i)|` = column-sum of the boolean past matrix `C` over the
**minimal elements** (rows of `C` with empty past). Order-only,
permutation-invariant. **Replaces** prereg-001's future-HEIGHT (longest future
chain). [Finding 1]

### B. Point estimate — bracket midpoint
The blind split is the **1-D 2-means threshold `thr` on integer `O`** (classify
`O < thr`; `thr` is a half-integer midpoint ⇒ exact ties impossible, no tie rule).
Revealing `r` forms the order-statistic bracket `[r_lo, r_hi] = [max r over low-O,
min r over high-O]`. The **point estimate of the boundary location in `r`** is the
**bracket midpoint `0.5·(r_lo + r_hi)`**. The point estimate is **not**
recalibrated.

### C. Abstaining gate — τ(n)
`improvement(O_min) = 1 − SSE2/SSE1` = variance explained by the best 1-D
2-partition (== 2-means in 1D) of the minimal-element `O` values.
`τ(n)` = the **(1−α) quantile of `improvement` under an abstract `Uniform[0,1]`
null at matched `n`**, with **α = 0.01 ⇒ τ = p99**, computed by Monte Carlo with
**`NULL_MC_SEED = 20260621`**, **`NULL_MC_REPS = 40000`**, draws
`numpy.random.default_rng(NULL_MC_SEED).random(n)`. **`n`** = number of minimal
elements (count of empty columns of `C`; order-only, no embedding). The null is
**data-independent** — no project seeds, no sprinkling, no ground truth.
**Gate semantics:** a causet **ABSTAINS** (`sep → 0`; **no boundary claimed** for
that causet — it makes no localisation claim and contributes a null `sep` to the
control/permutation statistics) **iff `improvement(O_min) < τ(n)`**; otherwise it
proceeds with its `sep`. [Finding 2; this is what achieves θ_fp (iv)]

### D. Domain gate — `T_EDGE_MIN = 6`
`T_EDGE_MIN = 6.0`. Any configuration with **`t_edge < 6` is OUT-OF-DOMAIN**: it is
reported as **outside the experiment's domain of validity** and is **never counted
as a physical FAIL** of the recoverability hypothesis (a distinct status, akin to
INCONCLUSIVE-for-domain). `t_edge = 6` equals the sealed `T_EDGE`, so `BOX_AREA`
stays `7.2` and the **frozen `ℓ_λ` / `θ_loc` numeric table (addendum:57–62) applies
verbatim**. `t_min` was pinned to 6 (smallest extent meeting all three Decision-2
clauses incl. plateau; density-robust at ρ=833 and ρ=1667). The stricter
alternative `t_min = 8` is recorded but **not adopted**. [Decision 2]

### E. Localisation criterion (ii) — UNCHANGED, coverage stays a weak floor
Median over seeds of bracket width `|dr|/(2M) ≤ θ_loc = 2·ℓ_λ/(2M)`, with `ℓ_λ`
from the **frozen intensity & fixed area, never realized N**; inconclusive if
per-seed IQR > θ_loc; **coverage ≥ 0.5**. [addendum:51]
**EXPLICIT (Decision 1):** `coverage ≥ 0.5` is a **deliberately weak floor** and is
**not** to be reinterpreted as nominal coverage. The order-statistic bracket is
**not recalibrated**. The frozen claim stays *“the bracket covers r_S and its width
contracts toward ℓ”* (addendum:82), **not** controlled nominal coverage. The
documented monotone margin decline (coverage 0.97→0.78 over ρ=208→3333, Finding 4)
is an **expected property** of the min/max bracket, reported alongside any PASS.

### F. Convergence-slack (b) — UNCHANGED
`m_{k+1} ≤ m_k + ℓ_k/(2M)` over the 4-intensity sequence. [addendum:88]

### G. Remaining criteria — UNCHANGED from the prereg-001 addendum
θ_sig (i): paired sign-flip permutation `p_perm ≤ 1e-4`, significant at every
N ≥ 3000. θ_stab (iii): std of blind boundary r-location across seeds `≤ 2·ℓ_λ`.
θ_fp (iv): LOO false-positive fraction `≤ 0.05` (now **achieved by gate C**).
Guard-v (v): `verify_order_only` raises on any non-relabel-invariant causet.
**PASS iff ALL** hold at the primary endpoint (intensity 12000); a primary level
with < 18/20 valid seeds → INCONCLUSIVE. [addendum:95–99]

### H. Evaluation order (frozen)
Per causet, strictly: **(1) DOMAIN** — if `t_edge < T_EDGE_MIN` ⇒ OUT-OF-DOMAIN,
stop (no estimate, no FAIL). **(2) ESTIMATOR** — volume observable `O_min`,
2-means split `thr`, bracket → midpoint. **(3) GATE** — τ(n): if
`improvement < τ(n)` ⇒ abstain (`sep → 0`). **(4) CRITERIA** — (i) permutation
significance, (ii) width/θ_loc + coverage ≥ 0.5, (iii) θ_stab, (iv) LOO fp, (b)
convergence-slack, (v) Guard-v, then the PASS/FAIL aggregation.

### I. Anti-reverse-engineering (binding)
No parameter in this contract — the τ table, α, `NULL_MC_SEED`, `NULL_MC_REPS`,
`T_EDGE_MIN`, or any threshold — may be recalibrated, selected, or tuned using the
reserved prereg-002 band `[2_000_000, 2_999_999]`, which stays **virgin** until #3
sealing. Every datum used to fix this contract is EXPLORE_POOL only.
(`preregistration.md:49`, committee auditor.)

### J. Inherited frozen geometry & ensemble — UNCHANGED
Geometry: tall box `t_edge=6.0, r_edge=1.2, r_center=0.7`, EF metric,
`area = 7.2`, `r ∈ [0.1, 1.3]` spanning `r_S = 2M = 0.5`. Intensities
`{1500, 3000, 6000, 12000}`; primary endpoint `12000`; 20 seeds/level; same point
cloud per seed for BH & MINK. [addendum:37–62]

---

## Change-list vs prereg-001 (exactly three)

1. **Observable**: future-HEIGHT → future-VOLUME (clause A).
2. **New abstaining gate** `τ(n)` (clause C) — achieves θ_fp (iv).
3. **New domain gate** `T_EDGE_MIN = 6` (clause D).

Everything else — criteria forms, thresholds, geometry, ensemble, anchoring
discipline, PASS/FAIL aggregation — is **inherited verbatim** from the prereg-001
addendum.

## After this freeze commit, #2 is mechanical

1. integrate **exactly** clauses A–J into the path `validate.run()` executes;
2. add a test per clause (observable, gate semantics + frozen τ MC, domain gate +
   OUT-OF-DOMAIN status, evaluation order, each criterion);
3. assert `validate.run()` uses **only** the new path;
4. assert `dev/` never enters production;
5. **re-seal once** (new `thresholds.py` SHA), held-out seeds drawn from the
   reserved 002 band only at that sealing.

**Sequence:** freeze #1 (this document) → integrate & test #2 → re-seal → freeze
prereg-002 (#3) → single blind run.
