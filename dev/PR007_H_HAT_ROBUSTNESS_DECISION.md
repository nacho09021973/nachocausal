# PR007 H_hat Robustness Decision

STATUS: DECISION_ONLY
SCOPE: PREREG_DIRECTION / NO_CODE / NO_EXPERIMENTS
RELATION_TO_PR006: NEXT_STEP_AFTER_REPLICATED_FIXED_K_LOCALIZATION_SIGNAL

## Decision

PR006 establishes a fixed-K order-only scalar localization signal, not a geometric
horizon reconstruction.

PR007 will test whether this scalar estimator is robust or convergent under
preregistered nuisance-axis variation.

## Fixed Inheritance From PR006

PR007 inherits the PR006 estimator object:

```text
H_hat = lower-median first_empty_depth at K_REF = 8
```

The inherited meaning remains:

```text
order-only early-emptying depth at fixed K_REF = 8
```

It does not become:

```text
horizon radius, reconstructed horizon surface, or K-invariant physical barrier
```

## PR007 Question

Does `H_hat` remain stable, or show a controlled convergence pattern, when nuisance axes
vary under a preregistered protocol?

Candidate nuisance axes for PR007:

- seed block;
- intensity / density;
- patch size;
- EGS fuzziness parameter `M`;
- start population size.

## Constraints

- Keep `K_REF = 8` frozen unless a later preregistration explicitly defines a different
  single-K estimator.
- Do not introduce multi-K aggregation in PR007 unless its aggregation rule is frozen
  before validation.
- Do not use embedded radial position, shell labels, straddle status, horizon-side
  labels, or any `GROUND_TRUTH_READOUT / NOT_ORDER_ONLY_EVIDENCE` column to tune
  `H_hat`.
- Do not reinterpret PR006 as a horizon reconstruction, radial localization, or
  K-invariant barrier result.
- Do not run PR007 until its command, nuisance-axis grid, seed policy, output path,
  report path, data contract, and terminal decision tree are frozen in a separate
  preregistration commit.

## Allowed PR007 Claim Shape

If a future PR007 validation passes, the allowed claim shape is:

```text
The fixed-K order-only scalar estimator H_hat is robust/convergent under the
preregistered nuisance-axis variation tested in PR007.
```

The disallowed claim shape remains:

```text
H_hat reconstructs the geometric horizon or proves a K-invariant physical barrier.
```
