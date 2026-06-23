# Phase 0 dev notes — bimodality of O (exploration only, NOT a result)

Sandbox notes for docs/roadmap.md Phase 0. No verdict, no frozen threshold.

## Sweep 1 (dev/sweep_o.py, 2026-06-18)

Box edges=[2.0,1.2] center=[1.0,0.7] r_S=0.5; dev seeds {20240617,13,101};
intensities {420,1500,3000,6000}; BH vs box-matched MINK. fast==Minz gate kept at
the smallest intensity per (kind,seed).

### Findings
- **Order-only recovery works and scales.** The blind 1-D 2-means split of O (sees
  only O) recovers the true interior/exterior partition with split_acc 0.88→1.00,
  ≥0.94 at N≳1500, ~0.99 at N~6000.
- **Localisation saturates the discreteness floor.** Boundary gap dr/M: 0.21→0.03 as
  N grows. ℓ/(2M)=ρ^−½/(2M) is ≈0.15 (N=424), 0.08 (1500), 0.057 (3000), 0.04 (6000).
  Observed dr/M ≈ (0.8–1.4)·ℓ/(2M): the boundary localises to ~1 discreteness length.
  → supports θ_loc = k·ℓ/(2M) with k≈1–2 (preregistration.md:50).
- **Control is clean.** MINK split_acc scatters around chance (0.11–0.86, ~0.5): the
  2-means split of Minkowski O is uncorrelated with r. No false horizon.

### Two methodological corrections (carry into Sweep 2)
1. **BC (bimodality coefficient) is the WRONG proxy** — flat ~0.22 for BH, sometimes
   higher for MINK. BH separation is ASYMMETRIC (few low-O interior vs many high-O
   exterior); skew/kurtosis-based BC misses it. Use Hartigan's dip (the frozen θ_sig,
   preregistration.md:52), implemented in pure numpy (diptest/scipy absent; do NOT
   modify the Minz venv).
2. **Cost 59m41s** — Minz `intensify()` runs its O(N²) `relate()` on every sprinkle
   even though we only need coordinates for the accelerator. Fix: draw Poisson-uniform
   points in numpy, build the poset with past_matrix_fast only, and keep ONE fast==Minz
   cross-check at small N per kind (not per run). Lets us reach the dense ceiling N~2e4.

## Sweep 2 (dev/sweep_o2.py, 2026-06-18) — control-anchored, numpy sprinkle

8 dev seeds; intensities {1500,3000,6000,12000}; t-extents {2.0,6.0}; r_edge=1.2.
fast==Minz gate passed bit-for-bit (BH+MINK) at N=424. Runtime 8m50s, reached N~12000.

### Findings
- **Signal is robust and blind-significant.** z_sep = (mean BH − mean MINK)/std MINK over
  seeds. Tall box (t=6.0): z_sep = 5.2 (N=1519), 10.0 (3027), 8.7 (6039), 9.2 (12055). Narrow
  box (t=2.0): z_sep = 2.4, 1.7, 4.8, 6.2 — marginal at low N. → freeze the TALL geometry.
- **Larger timelike extent sharpens the jump** (paper Sec. III confirmed): sep_BH ~5.5 narrow
  → ~8.5 tall.
- **Localisation tracks the discreteness scale, k≈1, in BOTH boxes.** Normalising by
  ℓ=ρ^−½ (ρ=N/area; tall area=7.2, narrow=2.4): drM/(ℓ/2M) ≈ 0.9–1.1 everywhere
  (e.g. tall N=12055 drM=0.049 vs ℓ/2M=0.049). → θ_loc = k·ℓ/(2M), k=1–2 well supported.
- **Recovery acc_BH ≈ 0.97–0.98** (dev scoring) throughout.
- **Blind statistic choice:** 2m_sep discriminates everywhere; gap-ratio only in the tall box.
  Use control-anchored z on 2m_sep as the dev θ_sig proxy.

### Remaining before any freeze (Phase 0 → pre-registration addendum)
1. Implement + validate Hartigan's dip in its OWN environment (the frozen θ_sig); the dev z is
   a proxy, not the frozen test.
2. Fix the validation geometry (tall box) and ensemble size (8 seeds gave stable z; confirm).
3. Write frozen threshold VALUES (θ_loc k, θ_sig level, θ_stab, θ_fp) before generating any
   validation seed. Validation seeds disjoint from DEV_SEEDS.

## Dip / θ_sig validation (dev/dip_check.py + dev/dip_diag.py, 2026-06-18)

Own venv ~/nachocausal-dip-venv (diptest 0.11.0, numpy 2.4.6, scipy 1.17.1); isolated from
the Minz venv. O multisets dumped via dev/dump_o.py -> dev/o_samples.json (tall box, 8 seeds).

### Findings
- **diptest is well-calibrated on CONTINUOUS data**: uniform false-positive ≈ 0.6–1.3% at
  α=0.01; power rises with n and separation (strong only ≥4σ, n≥150).
- **The real BH bimodality is dramatic and legitimately dip-significant**: interior cluster
  O∈[1,18] vs exterior O∈[50,132] with a clean gap; dip p≈0, frac_p<0.01 = 0.88 (N=1519) →
  1.00 (N≥3027), despite small |minimal| (22–64). Genuine signal. ✓
- **The raw dip p-value is INVALID on our tied integer O**: the box-matched MINK control trips
  p<0.01 at 12–50%, FAR above α. Diagnosed as a TIES ARTIFACT, not box-edge bimodality:
  diptest FP on tied unimodal integers explodes when the value-range K is small
  (K=10: FP 0.04→0.77 as n grows; K≥30: FP ~0.001–0.004). The MINK O is a tight integer cluster
  (range ~5–15, heavy ties) — exactly the pathological small-K regime. The BH O spans K~130, so
  its significance is real.

### Consequence for the freeze (revises the earlier "dip = frozen θ_sig" plan)
- Keep Hartigan's dip as the bimodality STATISTIC, but its significance must be
  **CONTROL-CALIBRATED**: BH dip (or 2m_sep) exceeds the box-matched MINK empirical null
  (percentile / z), NOT diptest's continuous tabulated p. This is robust to discreteness/ties
  and unifies criteria (i) θ_sig and (iv) θ_fp (preregistration.md:40-43) into one
  control-anchored test. The Sweep-2 control-anchored z (9–10σ, tall box) is therefore the
  CORRECT frozen approach, not merely a dev proxy.
- Alternative considered and rejected: jittering O to break ties (changes the statistic, not
  principled). Control calibration is preferred.

## Independent adversarial audit (2026-06-18)

A separate agent (fresh context, tasked to BREAK the Phase-0 claim) ran 34 tool actions and
could not. Independently re-executed, not just read:
- O is strictly order-only: monkeypatched estimate_O to depend on labels → Guard-v RAISED (real,
  not decoration). Split threshold uses only O (sweep_o2.py:98 before r is read at :99).
- Accelerator gate: regenerated Minz vs fast posets on a NEW seed (555), N≤2008, BH+MINK →
  0 disagreements over 4M+ pairs each. Glue3 uniformity guard fails on radial densification
  (chi2=1021≫18.467).
- Control: BH/MINK share one identical point cloud, differ only in causality.
- θ_loc: independently recomputed drM/(ℓ/2M) = 0.92,1.07,1.30,1.01 → matches notes; principled,
  not fitted.
- Reproducibility: regenerated all 64 O multisets → 0/64 mismatch vs o_samples.json; dip checks
  and tie-artifact reproduce.
Verdict: no cheating or unjustified hardcoding.

### Audit gaps still open (carry into the freeze plan)
1. [CLOSED 2026-06-19] fast==Minz now verified DIRECTLY at the dense ceiling N=10017 (intensity
   10000, seed 20240617), BH + box-matched MINK: 100,340,289 pairs each, 0 disagreements
   (dev/gate_highN.py, dev/gate_highN.log). Minz gen+poset 2221s BH / 4392s MINK on this machine
   (intensify's incremental O(N²) relate dominates; PastMatrix itself is <3s). Cost ran higher
   than the ~16 min reuse_check.md estimate because relate scales ~N^2.6 (BH) / ~N^3 (MINK), not
   pure N², and MINK's denser causality makes it ~2× BH at N=1e4. The vectorized accelerator
   stays admissible at the ceiling; audit gap #1 is no longer open.
2. vidh2000 C++ independent cross-check (prototype_o.py:207) not present/run.
3. Frozen Hartigan-dip θ_sig still deferred; reuse_check signal-N still [UNVERIFIED].
