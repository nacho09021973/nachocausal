# R-VAR Part F feasibility probe — measurement report

Authorized scope (PI, 2026-07-05): a measurement only, per comité 019 §9 step 1
(`docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md`). No μ computed, no
Part F step 3 run, no `EXPLORE_POOL`/`VALIDATION_SEEDS` touched, no threshold frozen, no
reconstruction claim, no BH-patch track. MINK only, one draw per production intensity, dev seed
`SEED=20240617` (precedent: `dev/gate_highN.py:20`), well outside `EXPLORE_POOL` (`1_000_000+`,
`dev/PR003_RVAR_MU_FREEZE_ADDENDUM.md:161-162`).

Script: `dev/measure_pr003_rvar_partF_feasibility_probe.py`. Result:
`dev/rvar_partF_feasibility_probe_result.json`. Total wall time: ~11s.

## What was measured

For each of `thresholds.INTENSITIES` (1500/3000/6000/12000), one MINK sprinkle via the
already-verified, already-polynomial `numpy_sprinkle` + `past_matrix_fast`
(`nachocausal/generator.py`). From the resulting past matrix:

- `N` actually generated (realized Poisson draw)
- `|Max(C)|` (maximal antichain size) — read off the past matrix directly, O(N) column scan
- `2^|Max(C)|` — the size of the family `family_A` (`dev/measure_pr003_rvar_gate0.py:67-79`)
  would have to enumerate
- number of Hasse cover relations and the wall time to compute them, via a vectorized
  boolean-matmul transitive reduction (measurement-only; not a proposed replacement for any
  Part F/D.2 code path — see script docstring)
- an analytical, deliberately optimistic lower bound on enumerate-and-filter wall time, from a
  raw `itertools.combinations` throughput benchmark (`~1.21e7` trivial subsets/s on this
  machine). **`family_A` itself was never run at production N** — per the falsifier's explicit
  instruction (comité 019 §5), this settles the question by arithmetic alone.

## Results

| Intensity | N | \|Max(C)\| | 2^\|Max\| | \|covers\| | t(past matrix) | t(covers) | est. enum time (optimistic floor) | verdict |
|---|---|---|---|---|---|---|---|---|
| 1500  | 1507  | 15 | 32,768            | 7,349  | 0.034s | 0.028s | 0.0027 s        | FEASIBLE_TO_REQUEST_PARTF |
| 3000  | 3009  | 22 | 4,194,304         | 16,566 | 0.163s | 0.153s | 0.346 s         | MARGINAL |
| 6000  | 6013  | 26 | 67,108,864        | 37,857 | 0.366s | 1.085s | 5.53 s          | MARGINAL |
| 12000 | 12019 | 40 | 1,099,511,627,776 | 83,481 | 1.177s | 7.380s | ~9.07×10⁴ s (~25h) | INFEASIBLE |

`OVERALL_VERDICT = INFEASIBLE`.

## Reading

- **`|Max(C)|` grows with N as the mathematician/falsifier predicted** (comité 019 §4-§5): not
  tiny, not linear in a friendly way — 15 → 22 → 26 → 40 across the frozen four levels.
- At `N=12000` (the frozen `PRIMARY_INTENSITY`, `thresholds.py:47`), `2^|Max|≈1.1×10¹²`. Even
  the **optimistic floor** (raw subset generation, no downset/crossing_interface work, which
  `family_A` actually does per subset) is ~25 hours for a *single* draw. Part F's frozen
  calibration needs `M=200` valid patches per level (`PR003_RVAR_MU_FREEZE_ADDENDUM.md`) — the
  real `family_A` cost per subset is strictly higher than this floor, so 200 draws at this level
  is not a "slow but eventually done" job, it is categorically infeasible with the only
  Gate-0-verified implementation.
- **The `1500`-only level is comfortably feasible** in isolation (`2.7ms` optimistic-floor
  estimate), but per comité 019's falsifier (§5, "Verdict coercion" / "Freeze violations"), a
  1-level table cannot serve the addendum's frozen "exactly the 4 levels, no interpolation"
  requirement without a separate committee-level amendment — this probe does not by itself
  license a scoped 1500-only run.
- `3000` and `6000` are labeled `MARGINAL` (between `10^5` and `10^8` subsets) — not
  comfortably feasible, not yet categorically ruled out; a real `family_A` run (which this probe
  deliberately did not attempt) would very likely push actual wall time well past the optimistic
  floor shown here, given per-subset work beyond raw generation.
- Cover-relation counts (7,349 → 83,481) confirm the second blocker the falsifier flagged
  (comité 019 §5.2, pure-Python `is_cover` being O(N³)) is real in shape but not, by itself, the
  binding constraint once computed via vectorized numpy (`t_covers` stayed under 8s even at
  `N=12019`) — the `2^|Max|` enumeration is the dominant, categorical blocker.

## Verdict

**`INFEASIBLE`** for the frozen four-level table as specified, using the only Gate-0-verified
`family_A` implementation. This is consistent with, and now empirically grounds, comité 019's
`RECOMMEND_DO_NOT_PROCEED`.

Per comité 019 §9 step 3, the options now on the table (not decided here — this is measurement
only) are: (a) design and separately Gate-0-verify a genuinely polynomial `𝒜(C)`-restricted
algorithm, if the falsifier's disjunctive-predicate concern (§5.1: D.1's membership constraint is
not expressible as a Picard closure) can be resolved; (b) reconsider Part F's design at the
specification level (a new committee question); (c) restrict to a level where `|Max|` is
tractable — but the falsifier's objection stands: fewer than 4 levels does not satisfy the
addendum's own frozen requirement without a further amendment.

This probe does not decide among (a)/(b)/(c); it only replaces the asymptotic argument with a
number, as requested.
