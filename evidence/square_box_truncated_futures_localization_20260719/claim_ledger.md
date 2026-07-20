# Claim ledger — SQUARE_BOX_2P4 truncated-futures localization contract

STATUS: CONTRACT_FROZEN_NO_EVALUATION_RUN
FROZEN_BY: human review
FROZEN_DATE: 2026-07-20
DATE: 2026-07-19

## Allowed claims

- This localizer contract is now frozen. Its design (observables, selectors, controls,
  thresholds) is fixed in writing before any confirmatory seed is drawn or evaluated.
- The localizer targets low future observables among minimals:

```text
low L(i), low V(i)
```

combined into a bivariate score `T(i)`, compared against four order-only baseline controls
(low-`L` alone, low-`V` alone, random-uniform) plus a coordinate-based, post-selection-only edge
diagnostic that is never a selector.
- This is separate from the frozen largest-gap localizer; it does not repair, reopen, or retune it.
- Confirmatory seeds are pinned and disjoint from every prior seed band in the project's history:

```text
TRUNC_FUT_DEV_SEEDS  = 4_500_000 .. 4_500_015
TRUNC_FUT_EVAL_SEEDS = 4_600_000 .. 4_600_031
```

- The prior R-VAR closure remains intact:

```text
CLOSED_NEGATIVE_RESULT [GEOMETRY_SPECIFIC]
```

- The sealed dispersion result this design is motivated by remains intact and separately bounded:

```text
BH_MINK_DISPERSION_DIFFERENCE_DETECTED
```

- The synergy/superiority statistical contract is fully pinned: `alpha_FWER = 0.01` (`d = 2`,
  `alpha_per_contrast = 0.005`), `EFFECT_FLOOR = 1.0` (a materiality threshold, not an instrumental
  resolution claim), `N_PAIR_MIN = 26`, `MIN_N(alpha, d) = max(ceil(0.5*n_pair), ceil(log2(d/alpha)))`.
  The boundary-confound diagnostic is its own separate family (`alpha_edge = 0.01`, `d_edge = 1`),
  never pooled with the primary synergy family.
- `RANDOM_CONTROL_SALT = 20260720` is pinned — a deterministic stream-separation/reproducibility
  constant, not an entropy source, chosen before and independent of any run.
- The seal for this contract is the git commit SHA that introduces its `CONTRACT_FROZEN` status —
  not a document-text hash.

## Forbidden claims

- No truncated-futures localization result exists yet — freezing the design is not evaluating it.
- This contract does not claim horizon localization or synergy detection of any kind; both are
  contingent on a confirmatory run that has not happened.
- This contract does not repair, reopen, supersede, or reinterpret R-VAR, the sealed dispersion
  result, or the frozen largest-gap localizer.
- This contract does not silently retune any prior threshold.
- No future summary or addendum may cite the §16 primary-localization terminal without co-stating
  the §16.1 synergy terminal in the same statement (§16.2).
- No future confirmatory terminal produced under this contract may be treated as settled without an
  independent `/auditor` certification of the produced `evaluation_summary.json`/`RESULT_SEALED.txt`
  (§16.2).
- No dev-seed or eval-seed evaluation may be backdated to before this freeze commit (§13).

## Pending human review — Stage C (confirmatory execution)

- Whether and when to authorize the §13 development-only support check on `TRUNC_FUT_DEV_SEEDS`.
- Whether and when to authorize the confirmatory evaluation on `TRUNC_FUT_EVAL_SEEDS`.
- Neither is authorized by this freeze. This freeze pins the design only.
