# Formula density sweep — result record

Status: **FORMULA / EXPLORATORY RESULT.** This is not part of the sealed
prereg-002 PASS/FAIL claim. It records the independent density-scaling run
requested for the `formula` branch.

## Run

Command:

```bash
python scripts/formula_density_sweep.py
```

Artifacts written locally:

```text
results/formula_density_sweep_per_seed.csv
results/formula_density_sweep_aggregate.json
results/formula_cpp_48000_tau_ext_per_seed.csv
results/formula_cpp_48000_tau_ext_aggregate.json
results/formula_cpp_96000_tau_ext_per_seed.csv
results/formula_cpp_96000_tau_ext_aggregate.json
```

The initial per-seed CSV has 200 data rows plus header: 5 density levels x 40
seeds. The high-density C++ extension adds 40 rows each at `lambda=48000` and
`lambda=96000`. `results/` is git-ignored, so the aggregate is transcribed below.

For `lambda >= 48000`, some BH clouds have more minimal elements than the sealed
tau table covers (`n > 128`). The C++ formula runner therefore used its documented
formula-only Uniform[0,1] Monte Carlo tau extension. This is exploratory and does
not modify the sealed validation path.

## Aggregate table

| lambda | N_mean | n_clean | med width/2M | std midpoint | med center error | coverage | abstain BH/MINK | fp |
|---:|---:|---:|---:|---:|---:|---:|:--:|---:|
| 1500 | 1498.175 | 40 | 0.158769 | 0.028296 | 0.018444 | 0.975 | 0.00 / 1.00 | 0.00 |
| 3000 | 2997.425 | 40 | 0.138209 | 0.025652 | 0.014751 | 0.900 | 0.00 / 1.00 | 0.00 |
| 6000 | 5996.250 | 40 | 0.076415 | 0.016097 | 0.008668 | 0.850 | 0.00 / 1.00 | 0.00 |
| 12000 | 11994.750 | 40 | 0.053767 | 0.011494 | 0.007161 | 0.900 | 0.00 / 1.00 | 0.00 |
| 24000 | 23992.675 | 40 | 0.048883 | 0.007583 | 0.004254 | 0.850 | 0.00 / 1.00 | 0.00 |
| 48000 | 47989.700 | 40 | 0.036170 | 0.004878 | 0.003399 | 0.775 | 0.00 / 1.00 | 0.00 |
| 96000 | 95985.350 | 40 | 0.022842 | 0.003109 | 0.003106 | 0.550 | 0.00 / 0.975 | 0.025 |

All BH rows are clean and non-abstaining. MINK controls abstain under the tau
gate in all but one high-density seed at `lambda=96000`.

## Scaling extraction

Log-log slopes over the first five density levels:

```text
median width/2M      gamma = -0.476
std midpoint         gamma = -0.496
median center error  gamma = -0.527
```

Log-log slopes over all seven density levels after the C++ high-density
extension:

```text
median width/2M      gamma = -0.461
std midpoint         gamma = -0.551
median center error  gamma = -0.463
```

Tail slopes for `N >= 6000`:

```text
median width/2M      gamma = -0.406
std midpoint         gamma = -0.598
median center error  gamma = -0.404
```

Local slopes:

```text
median width/2M      -0.200, -0.855, -0.507, -0.137
std midpoint         -0.141, -0.672, -0.486, -0.600
median center error  -0.322, -0.767, -0.275, -0.751
```

Free-power model `Y = A*N^(-alpha)` on the first five density levels:

| metric | alpha | A | RSS |
|---|---:|---:|---:|
| median width/2M | 0.476 | 5.332 | 0.000585 |
| std midpoint | 0.496 | 1.185 | 0.0000217 |
| median center error | 0.527 | 0.919 | 0.00000358 |

Fixed discreteness model `Y = a*N^(-1/2)`:

| metric | a | RSS |
|---|---:|---:|
| median width/2M | 6.512 | 0.000599 |
| std midpoint | 1.208 | 0.0000219 |
| median center error | 0.735 | 0.00000318 |

Residual model `Y = Y_inf + A*N^(-alpha)` grid diagnostic:

| metric | alpha | Y_inf | A | RSS |
|---|---:|---:|---:|---:|
| median width/2M | 0.386 | -0.022305 | 3.146 | 0.000564 |
| std midpoint | 0.077 | -0.086421 | 0.203 | 0.00000955 |
| median center error | 0.337 | -0.005108 | 0.280 | 0.00000261 |

The residual fits are diagnostics only; with five points, a negative fitted
residual floor should not be over-interpreted as physical.

Seven-level model diagnostics after adding `48000` and `96000`:

| metric | fixed `a` in `a*N^-1/2` | free alpha | residual `Y_inf` |
|---|---:|---:|---:|
| median width/2M | 6.539 | 0.461 | -0.000974 |
| std midpoint | 1.204 | 0.551 | -0.010321 |
| median center error | 0.737 | 0.463 | 0.000286 |

## Reading

This sweep supports the conservative formula-branch claim:

```text
W_H, sigma_rhat, median center error = O(ell) = O(rho^(-1/2))
```

The strongest signal is that three independently meaningful quantities remain
near exponent `1/2` after adding two higher-density levels: width `0.461`,
midpoint dispersion `0.551`, and median center error `0.463`. The width sequence
is still locally irregular, especially the shallow `12000 -> 24000` slope, so
this is evidence for discreteness-scale convergence rather than a precise new
law with a fixed prefactor.

The `lambda=96000` point exposes an important physical/estimator tension:
precision keeps improving, but coverage drops to `0.55`, close to the weak
coverage floor. This is consistent with the earlier warning that the
order-statistic bracket is a localisation bracket, not a calibrated confidence
interval.

No model here justifies treating the earlier `-0.523` as a special exponent.
