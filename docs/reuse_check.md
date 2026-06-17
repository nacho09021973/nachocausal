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

[UNVERIFIED] / open: per-sprinkling N and ensemble size for a clear signal are not yet measured;
to be determined on dev with this tooling.
