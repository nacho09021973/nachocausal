# Formula — empirical finite-density convergence law

Status: **FORMULA / INDEPENDENT RESEARCH BRANCH — EXPLORATORY ANALYSIS.**
This branch is separate from the sealed prereg-002 PASS. It must not modify the
sealed validation claim, thresholds, seeds, or PASS/FAIL criteria. Its purpose is
to ask whether the existing PASS data support an empirical convergence law for
the reconstructed horizon bracket width at finite density.

## Research question

Can the reconstructed horizon bracket width be characterized by the discreteness
scale of the causal set?

The candidate scaling is

```text
W_H(rho) ~ C * ell(rho)
```

where `W_H` is the reconstructed horizon bracket width and `ell` is the
microscopic discreteness scale. For a Poisson sprinkling in 1+1 dimensions,

```text
ell(rho) ~ rho^(-1/2)
```

so the empirical finite-density expansion to test is

```text
W_H(rho) = A*rho^(-1/2) + B*rho^(-1) + ...
```

or, for fixed patch volume `V` with `N = rho*V`,

```text
W_H(N) = a*N^(-1/2) + b*N^(-1) + ...
```

In dimensionless form, using a fixed patch scale `L`,

```text
W_H / L = a*N^(-1/2) + b*N^(-1) + ...
```

The defensible target claim, if supported, is only

```text
W_H = O(ell) = O(rho^(-1/2))
```

in the 1+1D Schwarzschild causal-set benchmark, with constants depending on the
estimator and protocol.

## Physical interpretation

If the fitted exponent is compatible with `-1/2`, the result is stronger than
"the bracket gets narrower." It would indicate that the ordinal boundary
resolution is limited by the microscopic causal-set scale, rather than by a
macroscopic residual width.

Related quantities to measure, without imposing an exponent after seeing data:

```text
E_H(rho) = |r_hat_H - r_H| ~ C_E*rho^(-alpha)
sigma_rhat_H(rho) ~ C_sigma*rho^(-beta)
```

The natural hypothesis is `alpha ~= beta ~= 1/2`, but the branch must estimate
these exponents rather than assume them.

## Existing data extraction before any new run

The first analysis must use only already-recorded results from
`docs/preregistration_002_result.md`. No new sprinkling, no new seeds, and no
new validation run are needed for this first pass.

The PASS result records the following per-level width proxy:

| lambda | Nbar | median `|dr|/(2M)` |
|---:|---:|---:|
| 1500 | 1518 | 0.172 |
| 3000 | 3026 | 0.137 |
| 6000 | 6037 | 0.072 |
| 12000 | 12052 | 0.064 |

Preliminary log-log extraction from these four already-recorded points:

```text
fit log(W) = c + gamma*log(Nbar)
gamma_all = -0.523
```

Local slopes are not stable:

```text
1518 -> 3026   gamma = -0.330
3026 -> 6037   gamma = -0.931
6037 -> 12052  gamma = -0.170
```

Reading: the all-level slope is numerically compatible with `-1/2`, but the
four-point sequence is too sparse and locally irregular to establish a stable
law. It is valid as a motivation for the `formula` branch, not as a conclusion.

The local `results/validation.json` aggregate also records boundary midpoint
dispersion, but not the mean midpoint or per-seed midpoint rows. Existing-data
extraction gives:

```text
sigma_rhat(N) slope = -0.503
```

Reading: the seed-to-seed dispersion is also globally compatible with the
discreteness-scale hypothesis. The error of the center,
`E_H = |mean(r_hat_H)-r_H|`, cannot be extracted from the current aggregate
artifact because the mean midpoint is not stored.

## Models to compare

Use the already-recorded widths first:

1. Pure discreteness scaling:

   ```text
   W(N) = a*N^(-1/2)
   ```

2. Two-term fixed-exponent expansion:

   ```text
   W(N) = a*N^(-1/2) + b*N^(-1)
   ```

3. Free exponent:

   ```text
   W(N) = A*N^(-alpha)
   ```

4. Residual-width alternative:

   ```text
   W(N) = W_inf + A*N^(-alpha)
   ```

The key falsification check is whether a model with `W_inf > 0` is favored. A
nonzero residual width would weaken the claim that the bracket contracts to the
microscopic scale.

## Guardrails

- Do not claim a new fundamental formula.
- Do not claim `W_H = A*rho^(-1/2)` as a stable law from the current PASS alone.
- Keep this branch explicitly exploratory unless a future protocol is frozen
  before new data are generated.
- The non-primary `lambda = 6000` caveat in prereg-002 (`fp = 0.10`) must stay in
  view when interpreting scaling.
- Negative controls and fresh seeds are future work, not evidence for this first
  extraction.

## Next concrete steps

1. Use `scripts/formula_extract_existing.py` to reproduce the existing aggregate
   extraction without running the benchmark or generating new causets.
2. Report uncertainty honestly: four density levels are insufficient for a
   strong asymptotic claim.
3. If the existing-data analysis remains compatible with `O(rho^(-1/2))`, design
   a new frozen exploratory-to-confirmatory protocol before generating any new
   density sweep or seed set.
