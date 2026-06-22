# Formula — proposed density-scaling run protocol

Status: **PROPOSED PROTOCOL, NOT YET RUN.** This document is a pre-run cartela
for the independent `formula` branch. It is not part of the sealed prereg-002
PASS/FAIL claim and must not alter the sealed validation path.

## Purpose

Test whether the reconstructed horizon bracket width and boundary-location
dispersion scale with the causal-set discreteness length:

```text
W_H = O(ell) = O(rho^(-1/2))
sigma_rhat = O(ell) = O(rho^(-1/2))
```

The branch should estimate exponents and finite-density corrections; it should
not search for a correction that makes the previous four-point slope exactly
`-0.523`.

## Existing-data motivation

Using only recorded prereg-002 aggregates:

```text
W_H slope          = -0.523
sigma_rhat slope  = -0.503
```

These values motivate the `rho^(-1/2)` hypothesis. They do not establish an
asymptotic law because there are only four density levels and local slopes are
irregular.

## Fixed geometry

Keep the prereg-002 in-domain geometry fixed:

```text
t_edge = 6.0
r_edge = 1.2
r_center = 0.7
box area V = 7.2
r_S = 2M = 0.5
```

With fixed `V`, density and expected point count are interchangeable:

```text
rho = lambda / V
ell = rho^(-1/2)
```

## Density grid

Recommended first new formula sweep:

```text
lambda = 1500, 3000, 6000, 12000, 24000
```

Rationale: it extends the existing octave grid by one higher-density level
without changing geometry. The current accelerator materializes an `N x N`
boolean past matrix, so `48000` is likely memory-expensive and should not be the
default first extension.

Optional resource-gated extension, decided before launch:

```text
lambda = 48000
```

No intermediate density may be added after seeing results from the first run
unless it is explicitly labelled as follow-up exploration.

## Seeds

Use a new seed band reserved for formula exploration, disjoint from:

- prereg-001 burned validation seeds;
- prereg-002 held-out validation seeds `[2_000_000, 2_999_999]`;
- existing dev seeds and EXPLORE_POOL seeds where practical.

Recommended deterministic draw:

```text
FORMULA_SEED_BAND = [4_000_000, 4_999_999]
FORMULA_DRAW_SEED = 20260623
n_seeds_per_level = 40
```

Draw once with pinned numpy and record the exact seed tuple before running the
scaling sweep. Do not replace individual seeds after inspecting outcomes.

Deterministic seed tuple produced by:

```bash
python scripts/formula_density_sweep.py --print-seeds-only
```

```text
4182344 4189677 4194591 4224390 4261015 4274211 4282923 4285417
4305367 4320335 4349451 4363335 4374324 4383419 4393453 4422787
4423879 4435504 4469892 4483532 4505593 4509980 4515071 4551783
4594211 4602230 4611520 4630069 4659517 4666838 4784245 4790986
4839913 4867974 4886061 4918700 4926213 4945652 4959535 4987184
```

## Metrics to store per seed

For each `(lambda, seed)` store a row with:

```text
lambda
seed
N
n_min_BH
improvement_BH
tau_n_BH
abstained_BH
r_lo
r_hi
width
width_over_2M
midpoint
center_error = abs(midpoint - r_S)
covers
clean
sep_BH
sep_MINK
abstained_MINK
```

Aggregate per density:

```text
N_mean
median(width_over_2M)
iqr(width_over_2M)
mean(width_over_2M)
std(width_over_2M)
mean(midpoint)
std(midpoint)
abs(mean(midpoint) - r_S)
median(center_error)
coverage_frac
abstain_frac_BH
abstain_frac_MINK
fp_fraction
p_perm
```

The current `results/validation.json` aggregate is insufficient for `E_H`
because it lacks the mean midpoint and per-seed midpoint rows. The formula run
must write a per-seed CSV or JSONL.

## Models fixed before run

Fit each metric `Y` in:

```text
Y in {median_width_over_2M, sigma_rhat, median_center_error}
```

using these models:

```text
M1: Y = a*N^(-1/2)
M2: Y = a*N^(-1/2) + b*N^(-1)
M3: Y = A*N^(-alpha)
M4: Y = Y_inf + A*N^(-alpha)
```

Optional diagnostic only, not selector:

```text
M5: Y = a*N^(-1/2)*(log N)^p
```

`M5` is allowed only as a sensitivity check. It should not be used to rescue a
preferred exponent unless a separate physical argument is written before seeing
the fit.

## Interpretation rules

- Main support for the formula branch is `alpha` compatible with `1/2` for
  width and dispersion, plus no positive residual floor demanded by `M4`.
- A fitted exponent near `0.523` is not special; it counts only as compatible
  with `1/2` within finite-density uncertainty.
- If `Y_inf > 0` is stable and positive for width or dispersion, the
  discreteness-floor claim is weakened.
- The non-primary prereg-002 `lambda = 6000` false-positive caveat remains a
  diagnostic warning; do not hide it in scaling plots.
- Any new negative-control or Minkowski scaling claim must be analysed
  separately from the BH boundary-width scaling.

## Deliverables

Before running:

1. Record exact seeds.
2. Record the command and code commit/hash.
3. Confirm the script writes per-seed and aggregate artifacts.

Default launch command:

```bash
python scripts/formula_density_sweep.py
```

C++ accelerated launch command:

```bash
python scripts/formula_density_sweep_cpp.py
```

The C++ path keeps Python in charge of sprinkling, tau-gate semantics,
aggregation, and artifact writing. The compiled kernel
`cpp/formula_volume_kernel.cpp` receives coordinates on stdin and computes the
order-derived future-volume observable without materializing the full `N x N`
past matrix. Smoke validation against the Python runner:

```bash
python scripts/formula_density_sweep_cpp.py --intensities 1500 --seed-count 2 --label formula_cpp_smoke --force-build
python scripts/formula_density_sweep.py --intensities 1500 --seed-count 2 --label formula_py_smoke
```

The two smoke CSVs matched on the critical fields: minimal counts, improvements,
separations, bracket edges, width, midpoint, and center error.

For formula-only high-density sweeps where the number of minimal elements
exceeds the sealed tau table (`n > 128`), `scripts/formula_density_sweep_cpp.py`
computes a local data-independent Uniform[0,1] Monte Carlo extension of `tau(n)`
with deterministic per-`n` seeds. This is explicitly exploratory and does not
modify `nachocausal/fixtures/tau_table.json` or the sealed validation path.

Resource-gated smaller smoke command:

```bash
python scripts/formula_density_sweep.py --intensities 1500 --seed-count 2 --label formula_smoke
```

After running:

1. Commit or transcribe aggregate tables.
2. Preserve raw per-seed formula artifacts unless they are too large; if too
   large, store checksums and a compact aggregate.
3. Report all models M1-M4, with M5 clearly labelled optional diagnostic.
4. State explicitly whether results support only `O(ell)` or something stronger.
