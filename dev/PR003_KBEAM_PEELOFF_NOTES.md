# PR-003 Fase #3 / R2 — K-beam peel-off falsification (dev, NOT a result)

Авал: `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md` §9 R2. Produced by
`dev/measure_kbeam_peeloff.py` (GPU build + transitive-reduction matmul via `dev/backend.py` on the
local NVIDIA RTX 5060; beam combinatorics on CPU/numba). **Exploration only — nothing frozen, not
validated, not audited.** Construction + ranking are order-only; `r` reveals ONLY to score `d⊥`,
never to seed/build/rank/cut. 6 seeds `EXPLORE_POOL[:6]`, t_edge=6, `RESERVED_002` untouched. Seal
`6e2c3888…` confirmed **before and after** (`dev/kbeam_peeloff.log`); `git status` shows no
`M nachocausal/`. HEAD `5081f4e`, branch `main`, numpy 2.4.6 (GPU venv — dev only; the seal is a
file-SHA, not a numpy version).

## The question (the one thing Fase #3 needed deciding)

`BARE_RELOCALISATION` (`dev/PR003_NEAR_HORIZON_NOTES.md:112-119`): a bracket-seeded fuzzy ladder is
adherent for only `k*≈2-3` rungs, then **peels off** — its `d⊥/ℓ` drifts to 5-8 by the tail. The
single greedy tracer (`explore_direction.greedy_ladder`) is **myopic** (commits to the first valid
successor, no backtrack). **Is the peel-off algorithmic (greedy myopia, curable by keeping more
hypotheses) or physical (a marginally-unstable null orbit = the order-only localisation wall)?**

## Method (binding protocol, declared before peeking — comité-003 §9 R2)

- **(a) Box fixed** (t_edge=6); the K-beam is compared against the **single-tracer greedy baseline**
  at the *same* box and the *same* seed rungs (`measure_pr003.boundary_minimals_invariant`).
- **(b) Order-only ranking only.** A K-beam over EGS fuzzy ladders (Def 2): at each depth, expand
  every survivor by all Def-2-valid successor rungs and keep the top-K by the **interval-cardinality
  regularity** reward `−(|cp−c₀|+|cq−c₀|)`, `c₀ = 1.5M−1` the centre of the band `[M−1, 2M−1]`
  (M=3) — purely interval-abundance, order-only. **No relphi, no embedding direction.** (relphi
  already failed Fase #1-B.)
- **(c) Three-way report, no silent win.** Per K, scored with hidden `r`: the `d⊥/ℓ` of the order-only
  **top-1** ladder (what an order-only selector picks) and the **min over the K survivors** (best
  ladder the beam retained) at the reference tail depth `k_ref=8`, plus the reach fraction.

GPU honesty: the link/covering matmul `C·C` is integer-valued (0/1 float32, counts ≪ 2²⁴), so the
GPU link matrix is bit-identical to CPU. Ladder-primitive `selftest()` passes before any measurement.

## Result (2026-06-25, 6 seeds, t_edge=6; `d⊥/ℓ`, k_ref=8, ADH=3ℓ)

| intensity | ℓ | single-tracer tail `d⊥/ℓ` | top-1 @k=8 (K=1→64) | min-beam @k=8 (K=1→64) | n@k=8 (K=1→64) | reach≥8 (K=64) |
|---:|---:|---:|---|---|---|---:|
| 3600  | 0.0447 | 6.40 (n=2)  | 0.3 → 4.8 | 0.3 → 3.8 | 2 → 103 | 19% |
| 7200  | 0.0316 | 5.72 (n=8)  | 3.2 → 6.6 | 3.2 → 5.3 | 8 → 147 | 23% |
| 14400 | 0.0224 | 0.88 (n=1)* | nan → 6.1 | nan → 4.9 | 0 → 144 | 22% |

\* the 14400 single-tracer tail rests on **one** ladder — anecdotal (matches the wobble already
flagged in `PR003_NEAR_HORIZON_NOTES.md:142-145`). The 6.40 / 5.72 greedy tails **reproduce
`measure_truncated_head` exactly** (same seeds) — a consistency check, not a new drift.

Per-depth `min-beam d⊥/ℓ` profile (K=64, pooled): adherent head `≈1.6-2.0ℓ` for k=1-3, then **rises
monotonically to ≈4-6ℓ by k=6-8 and stays there** at every density.

## Reading — verdict: PEEL-OFF NOT CURED BY K → PHYSICAL-leaning (under-reach-caveated)

- **A wider beam enumerates more but does not adhere better.** As K grows 1→64 the number of ladders
  reaching k=8 grows ≈50× (2→103, 8→147, 0→144), yet the **order-only top-1** ladder's `d⊥/ℓ` at k=8
  stays **≈5-7ℓ for all K** — no improvement. An order-only ranking cannot *select* a ladder that
  stays adherent past the head.
- **Even the post-hoc best-retained (min-beam) plateaus far above adherence.** It settles at `≈4-6ℓ`
  and only drifts down slowly *as more ladders are sampled* (an order-statistic effect of the growing
  n, not a converging adherent ladder); it never approaches the head's `≈2ℓ` nor crosses ADH=3ℓ.
- **The head is the only adherent part — exactly `BARE_RELOCALISATION`.** k≤3 stays `≈2ℓ` at all K and
  all densities; the seed neighbourhood (prereg-002 floor) is reconfirmed, and *everything past it
  peels regardless of beam width.*

**Conclusion.** The peel-off is **not greedy myopia**: keeping K=2…64 hypotheses, ranked by the
order-only fuzzy-ladder regularity, does **not** recover an adherent extended ladder. This is
evidence the wall is **physical** — order-only information genuinely runs out past the seed
neighbourhood — which **hardens the Le Cam O(ℓ) bound** (`dev/PR003_INFO_BOUND_NOTES.md`): no
order-only multi-hypothesis search localises finer than the seed `O(ℓ)` floor.

## Caveats / scope (binding honesty)

- **UNDER-REACH is real (the protocol-(c) INCONCLUSIVE axis).** At t_edge=6 the reach to k=8 is only
  ≤23% even at K=64; EGS sharpen the contrast at `t*/r_S∈[0,50]` (~8× taller). So "physical" is
  established **only within the box's reachable depth**; whether a taller box would let an adherent
  ladder extend is **untested**. A taller-box run is a NEW prereg (different BOX_AREA/ℓ-table), out
  of scope for a dev step (comité-003 §9 C2). Honest label: **PHYSICAL within box reach** — NOT
  algorithmic, and **not** a clean unconditional PHYSICAL.
- dev / scored with hidden `r` — NOT frozen, NOT validated, NOT audited.
- No "apparent horizon" framing; only order-only behaviour of fuzzy ladders in a finite 1+1D patch.
- The order-only beam score (interval-regularity) is one principled choice; a different order-only
  score *might* rank differently, but it cannot manufacture adherence the geometry does not retain
  (the min-beam envelope — independent of ranking — also peels).

## Consequence

R2 disfavours the "algorithmic / curable" reopening of `BARE_RELOCALISATION` and supports
consolidating on the measured `O(ℓ)` floor as the Fase #3 result (the Le Cam bound,
`dev/PR003_INFO_BOUND_NOTES.md`). The only surviving way to reopen extension would be a **taller-box
prereg** addressing the under-reach caveat — a committing step, not a dev probe. This note freezes
nothing.
