# R-VAR structure probe — measurement report + polynomial-algorithm candidate

Follow-up to `dev/PR003_RVAR_PARTF_FEASIBILITY_PROBE_REPORT.md` (commit `014d364`,
`PARTF_CURRENT_ALGORITHM = INFEASIBLE`) and to comité 019 §9
(`docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md`). Scope discipline
identical to the feasibility probe: dev seeds only (`20240617/13/101`, `dev/sweep_o.py`
precedent), MINK + BH, the 4 production intensities, read-only against the sealed generator.
No μ computed, no Part F step 3, no `EXPLORE_POOL`/`VALIDATION_SEEDS`, no threshold frozen, no
reconstruction claim.

Artifacts:

- `dev/measure_pr003_rvar_structure_probe.py` → `dev/rvar_structure_probe_result.json`
  (measurement; two per-draw certificates)
- `dev/explore_rvar_interval_dp.py` → `dev/rvar_interval_dp_result.json`
  (exploration prototype; toy-validated against the committed Gate 0 reference; production
  outputs claim-inert)

## Finding 1 — a polynomial exact algorithm for the *same* frozen object very likely exists

Comité 019's falsifier posed: *"it is unproven a polynomial algorithm for `max_{D∈𝒜(C)} S`
exists at all"* (§5.1, the disjunctive D.1 predicate). Three structural facts, each checked
this probe, dissolve the obstruction **for the posets this project actually generates**:

1. **Modularity.** For any down-set `D`, both `A(D)` and `B(D)` are modular:
   `A(D) = Σ_{v∈D} a_v`, `B(D) = Σ_{v∈D} b_v` with per-element coefficients read off the
   Hasse diagram (three-line telescoping proof in `dev/explore_rvar_interval_dp.py`'s
   docstring; it is the same linearization `maxflow_mincut_closure` already uses).
   **Verified exactly on every member of the toy poset's enumerated family: PASS.**
2. **Reparametrization.** 𝒜(C) members are exactly `D = ↓M`, `M ⊆ Max(C)`, so membership of
   `v` depends only on whether `I_v = {m ∈ Max : v ≤ m}` meets `M`.
3. **Interval structure (2D orders).** In 1+1D sprinklings, `I_v` is a **contiguous
   interval** of the maximal antichain sorted by a null coordinate. Measured: **0 violations
   in 24/24 production-scale draws** — MINK under `u = t−r` (theorem: dominance order), BH
   under the ingoing EF coordinate `p = t+r` (empirical; the outgoing coordinate flips inside
   the horizon and indeed fails, 5000+ violations — the *ingoing* sort is the right one).
   The property is **certifiable per draw in O(N·K)** before solving; a production
   implementation would emit a typed abstention on failure (a guardrail that can fail).

Together: the Dinkelbach inner step becomes a classic O(K²) gap-DP over the sorted antichain
(minimize the weight of elements whose whole interval falls between consecutive selected
positions), with a lexicographic tie-break toward maximal `B` that resolves the
`(A,B) = (0,0)` boundary-tie degeneracy Gate 0 Tier 0 already documented. Cost is O(N²)
end-to-end (dominated by the cover computation), replacing `2^K` enumerate-and-filter.

**Validation status:** exact match against the committed Gate 0 Tier 0 reference
(`dev/measure_pr003_rvar_gate0.py`) on its own 16-element toy poset — λ* match, argmax match
(unique), membership + `H ≠ ∅` all PASS. This is *weak* evidence by itself (K=3 on the toy);
a fresh Gate 0 for this implementation (zero-discrepancy vs `family_A` on sprinkled posets up
to K≈20, where 2^K is still enumerable — a regime Tier 0/1 never reached) is required before
any calibration or scoring use, per the addendum's own §6 discipline. **Not run here; not
authorized here.**

Timing at production N (dev seed, claim-inert): ≤ 9 Dinkelbach iterations everywhere; wall
time ≤ 9s per draw even at BH `K = 426` — where the only Gate-0-verified implementation would
need `2^426` subsets.

## Finding 2 — the deeper blocker: 𝒜(C) is *empty* on production MINK, certified

While running the DP on production MINK the family came back empty — and the reason is
geometric, not computational. Exact per-draw certificate (no enumeration): 𝒜(C) requires
`(C−D) ∩ Min ≠ ∅` for `D = ↓M`, `M ≠ ∅`; if **every minimal element lies below every maximal
element**, no nonempty `M` can avoid all of Min, hence 𝒜(C) = ∅. Counted on the past matrix:

| kind | draws | unrelated (min,max) pairs | minimals with partial `I_z` | family status |
|---|---|---|---|---|
| MINK | 12/12 (4 intensities × 3 seeds) | **0 in every draw** | 0 | **EMPTY, certified** |
| BH | 12/12 | 1327–15241 | **100% of minimals** in every draw | nonempty (DP finds members) |

The MINK emptiness is forced by the frozen tall-box geometry: light crosses the spatial width
in Δt = `R_EDGE` = 1.2 ≪ `T_EDGE` = 6, so the future cone of any bottom-layer element covers
the entire top layer. Minimal elements live at the bottom, maximal at the top → every min
below every max, essentially deterministically. BH is the exact opposite **because of the
horizon**: there are maximal elements deep inside the horizon (future cones truncated at
small r) that early outside minimals cannot reach — every minimal has a partial interval.

**Consequence for Part F as frozen:** the μ calibration substrate is MINK-only nulls
(addendum Part F2). At production N every null draw abstains `EMPTY_FAMILY` → `rate_empty ≈ 1`
→ the frozen OOD rule fires → **`OUT_OF_DOMAIN_UNCALIBRATED` even with unlimited compute**.
The freeze discipline itself worked (the OOD rule honestly detects the degeneracy), but the
frozen μ object is vacuous at production scale. Note this *inverts* comité 019's physicist
expectation (`EMPTY_FAMILY` rarer as N grows past the toy regime): measured, it saturates
at 100% — the toy regime's near-chain artifact and the production regime's geometric mixing
produce empty families for *different* reasons, on *both* ends.

## Flagged, not interpreted

The BH argmax at production N has `|D*| ≈ N − few` and `B ∈ {3,…,8}` (crossing interface of a
handful of covers under a few antichain positions). Whether the frozen score `S = A/B`
at production scale selects *horizon-like* cuts or *boundary-artifact* cuts is a physics
question Gate 0's toy scale could not see and these claim-inert values cannot answer. It
belongs to the comité (physicist seat) alongside Finding 2.

## What this changes

- The compute blocker (`014d364`) is real but **no longer the binding constraint**: Finding 1
  gives a credible polynomial path for the same frozen object (pending its own fresh Gate 0).
- The binding constraint is now Finding 2: **Part F's frozen calibration object is empty on
  its own null substrate at production scale.** No algorithm fixes that; it is a
  specification-level question — exactly comité 019 §9 step 3 option (b), now with measured
  grounds instead of asymptotic ones.
- The comité-018 dual-consumption-plan diff test remains pending but drops to third priority:
  it verifies the consumption plan of an object now known to be degenerate.

No verdict token is emitted here beyond the summary flags in
`dev/rvar_structure_probe_result.json`; the next committing step (redesign vs. record-as-
non-viable) is a committee/PI decision, not this probe's.
