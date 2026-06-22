# Pre-registration 002 — RESULT: **PASS**

The single blind `validate.run()` on the prereg-002 held-out seeds was executed
**once**, exactly as frozen. Per the binding reporting rule
(`docs/preregistration_002.md`), the outcome is recorded regardless of value.

- **Verdict: PASS** — all six frozen checks hold at the primary endpoint
  (intensity 12000), `t_edge = 6` (in-domain).
- Run: `python -m nachocausal.validate` on the SEALED package at commit `573cfcb`,
  seal `nachocausal/thresholds.py` SHA256 `6e2c3888…` (`make verify-seal`),
  numpy 1.26.4. Raw output: `results/validation.json` (git-ignored; transcribed
  below). First and only evaluation of the held-out band.

## Frozen verdict

```
checks = {
  i_significant_primary_and_above_3000 : True,
  ii_localisation_primary              : True,
  ii_convergence_slack                 : True,
  iii_stability_primary                : True,
  iv_false_positive_primary            : True,
  v_order_only                         : True,
}  -> PASS
```

## Per-level table (transcribed from results/validation.json; 20/20 valid each)

| λ | N̄ | n_valid | p_perm | sig | med\|dr\|/2M | θ_loc | loc | coverage | r_std | θ_stab | stab | fp | fp_ok | abstain BH / MINK |
|---:|---:|:--:|---:|:--:|---:|---:|:--:|:--:|---:|---:|:--:|---:|:--:|:--:|
| 1500 | 1518 | 20 | 9.54e-07 | True | 0.172 | 0.277 | True | 0.95 | 0.022 | 0.139 | True | 0.00 | True | 0.00 / 1.00 |
| 3000 | 3026 | 20 | 9.54e-07 | True | 0.137 | 0.196 | True | 0.85 | 0.019 | 0.098 | True | 0.05 | True | 0.00 / 0.95 |
| 6000 | 6037 | 20 | 9.54e-07 | True | 0.072 | 0.139 | True | 0.85 | 0.013 | 0.069 | True | 0.10 | **False** | 0.00 / 0.90 |
| **12000** (primary) | 12052 | 20 | **9.54e-07** | True | **0.064** | 0.098 | True | **0.95** | **0.008** | 0.049 | True | **0.00** | True | 0.00 / 1.00 |

## Reading

- **(i)** sign-flip permutation `p = 9.54e-7 ≤ 1e-4` at every level (and at every
  N ≥ 3000, as required). **(ii)** median `|dr|/(2M) = 0.064 ≤ θ_loc = 0.098`,
  coverage `0.95 ≥ 0.5`, and the 4-N width sequence (0.172→0.137→0.072→0.064)
  contracts within the convergence slack. **(iii)** boundary r-std `0.008 ≤
  θ_stab = 0.049`. **(iv)** LOO false-positive `0.00 ≤ 0.05` at the primary.
  **(v)** Guard-v raised on no causet (O is order-only on every causet).
- **The τ(n) gate behaves as designed:** BH abstention = 0.00 at every level (it
  never suppresses the real signal); MINK abstention = 0.90–1.00 (it suppresses
  the structureless control, which is what closes the false-positive axis).
- **Transparent caveat:** at the **non-primary** level 6000, fp = 0.10 does not
  clear θ_fp. The frozen PASS/FAIL rule evaluates (iv) **only at the primary
  endpoint** (12000), where fp = 0.00; this non-primary fp does not affect the
  verdict but is recorded.

## What this PASS does and does NOT mean

**Means (the frozen, bounded claim):** the causal order alone — with no
coordinates accessible to the estimator — carries enough information to localise
the horizon-associated boundary **significantly and stably** in a 1+1D
Schwarzschild model within a **finite patch** (`t_edge = 6`), with the bracket
width contracting toward the discreteness floor as density grows, while the
box-matched flat control shows no such separation.

**Does NOT mean:** the global event horizon defined by future null infinity; full
metric reconstruction; 3+1D Schwarzschild; Kerr; or general manifoldlikeness. It
is a **recoverability** result for the order-only estimator under the frozen
protocol, not a reconstruction claim.

## Provenance

decision `bb21147` → freeze #1 `7d25c34` → estimator-v2 seal #2 `2f4c4a99`
(`22b7660`) → prereg-002 seal #3 `6e2c3888` (`573cfcb`) → **this blind run #4**.
