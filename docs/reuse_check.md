# Reuse-check decision — generation tooling

Decision: reuse c-minz/Python-causets to generate the poset (C, <=) for 1+1D Schwarzschild
sprinklings and the box-matched Minkowski control; write only minimal glue. Keep
vidh2000/MSci_Schwarzschild_Causets as an INDEPENDENT C++ cross-check oracle (its BH_causal2D
is a separately-authored implementation of the same He-Rideout relation) — the independent
second implementation the methodology requires.

Evidence (read-only scratch inspection):
- Minz: pure Python (numpy<2, matplotlib). BlackHoleSpacetime 2D; EF causal relation
  spacetimes.py:706-708 matching the project's He-Rideout convention. Poisson sprinkling
  sprinkledcauset.py:155. Poset via PastMatrix (causet.py:308); minimal elements via PastInf
  (causet.py:487); maximal-length paths via Paths(length='max') (causet.py:848). Flat control
  via FlatSpacetime + cuboid. Verified: imports under numpy<2 (no sprinkling run).
- vidh2000: C++ core (BH_causal2D/3D/4D), needs boost + manual patch; its Python is plotting
  only and reuses Minz. Inspected via shallow clone (full .git > 0.5 GB).

Glue to write (minimal, ours):
1. Box-matched cuboid for BH and Minkowski (same edges).
2. O(i) = longest timelike chain from each minimal element, as single-source longest-path on
   the DAG (element height) in topological order — NOT all-pairs Paths.
3. Assert sqrt(-g) = 1, making the 2D coordinate-uniform = natural-volume dependence explicit.
4. Vectorized poset accelerator (past_matrix_fast), replicating Minz's closed-form 2D relations
   (FlatSpacetime isCausal_flat2D spacetimes.py:295; BlackHoleSpacetime EF isCausal_BH2D
   spacetimes.py:759 — closed form, no Newton). Minz REMAINS the reference relation: the fast
   path is admissible only where verify_fast_matches_minz() confirms bit-for-bit agreement on
   the same coordinates (gated, raises otherwise). Verified EXACT vs Minz across seeds {20240617,
   7, 42, 99} × intensities {420, 1500, 3000} × {BH, MINK}, N up to ~3046, AND directly at the
   dense ceiling N=10017 (intensity 10000, seed 20240617, BH + box-matched MINK): 100,340,289
   pairs each agree bit-for-bit (dev/gate_highN.py, 2026-06-19; Minz gen+poset 2221s BH / 4392s
   MINK on dev). This closes the prior audit gap (the fast path had been relied on in sweeps up to
   N~10⁴–2·10⁴ but the exact gate had only run to N~3046). Not a new physics
   claim — a verified third implementation; vidh2000 C++ stays the independent cross-check.

Cost (measured on dev, this machine): Minz pure-Python relate() is O(N^2) and dominates
generation (~0.78s @N=424, ~24s @N=2008, ~N^2.3 → ~16 min/sprinkling at N=1e4). The accelerator
removes that: past_matrix_fast at N=1e4 in ~2.3s, N=2e4 in ~8s, memory bounded by row-block
chunking (~0.5 GB @1e4). The estimator (also dense) is then the next limit (~5s @1e4, ~24s @2e4).
Architectural ceiling: the dense N×N bool poset caps the pipeline near N~2-3e4 here (~10 GB at
N=1e5); the preregistration's high range (n up to 2e6) would need a sparse/graph redesign of BOTH
generation and the estimator — not yet done.

[UNVERIFIED] / open: per-sprinkling N and ensemble size for a clear SIGNAL (bimodality) are still
not measured; to be determined on dev. (Compute COST per the figures above is now measured.)
