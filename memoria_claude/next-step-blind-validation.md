---
name: next-step-blind-validation
description: Step #5 blind validation EXECUTED 2026-06-21 → verdict FAIL; next is dev/ estimator-v2 work toward a new pre-registration 002
metadata: 
  node_type: memory
  type: project
  originSessionId: 232b08ee-6185-48b8-a363-e50f44024aae
---

Step #5 (the blind validation run) was **EXECUTED on 2026-06-21** at commit
`672eb14` in the sealed CPU venv (numpy 1.26.4). Single committed `validate.run()`
over the 20 frozen `VALIDATION_SEEDS`. **Verdict: `FAIL`** (~32.5 min on CPU).
Result transcribed into `docs/preregistration_001_result.md` (committed);
machine verdict archived at `results/prereg001/validation.json` (moved from
`results/validation.json` on 2026-07-03 per auditor 005 — see
[[prereg002-pass-artifact-gap]]).

Why FAIL (3 of 5 checks held): significance strong (p≈1e-6 at all 4 N),
convergence/stability/order-only OK. Two failed at primary N (intensity 12000):
- **(ii) localisation** — bracket width passed but **coverage of true R_S = 0.30
  < 0.50** (falls with N: 0.65→0.60→0.40→0.30). The `max`/`min` order-statistic
  bracket (`scorer.py:53-54`) is narrow but off-centre/brittle.
- **(iv) false-positive** — LOO fp = **0.10 > 0.05** at every level;
  `two_means_split` always splits, so Minkowski tails get a spurious `sep`.

**Binding consequence (do NOT violate):** the 20 validation seeds are **burned** —
a FAIL is not licence to re-run them, re-tune, or reinterpret. Any re-validation of
an improved estimator needs a **new pre-registration 002**: re-sealed estimator-v2,
new seal SHA, **fresh held-out seeds disjoint from DEV_SEEDS and the burned
validation set**, frozen thresholds unchanged (they're principled, not tuned).

**Next action (committee 2026-06-21, user-authorised):** improve the ESTIMATOR in
`dev/` on DEV_SEEDS only, WITHOUT touching frozen thresholds. First axis chosen:
a **richer order-only observable O** (combine future height with past height /
interval cardinality / link valence) to sharpen interior-vs-exterior separation
near the boundary → lift coverage. Second axis: a **bimodality-gated split**
(abstain when no real gap) to cut false positives. The sealed
`nachocausal/estimator.py` stays untouched; v2 lives in dev/ until prereg-002.
See [[gpu-exploration-backend]] for the dev venv.
