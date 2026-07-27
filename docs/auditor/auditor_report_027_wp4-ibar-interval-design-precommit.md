# Auditor Report 027 — wp4-ibar-interval-design-precommit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `main`, HEAD `aa5b1cf`. Trigger: **precommit audit of
the design only**, before any implementation or execution concerning the Fisher-information interval
quantity. The only scientific-design target is the untracked document
`research_program/work_packages/wp4_ibar_interval_numerical_design.md`.

This audit does not evaluate `I(tau)`, `Ibar`, the constant-level defeater, or any new quadrature.
It checks whether the proposed numerical contract leaves post-hoc degrees of freedom in its
convergence test, independent validation, interval envelope, or fail-closed terminals.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code **0**:

```text
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.sha256
WARN: committed data file with no generator reference: data/reports/present_anchor_clean_v3_kill_test.csv
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
WARN: committed data file with no generator reference: evidence/new_geometry_20260719/mink_control_metrics.csv
----------------------------------------
Auditor: 0 error(s), 23 warning(s)
```

The complete 23-warning set is the established generator-reference baseline for committed
`data/reports/` and `evidence/` files. This target creates neither data nor a generator; none is
attributable to the design document.

## 3. Seal & freeze integrity

| Item | Value | Anchor |
| --- | --- | --- |
| Live seal | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `make verify-seal` |
| Frozen record | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `docs/preregistration_002.md:8` |
| Drift | **none** | — |

`nachocausal/thresholds.py` is absent from the working-tree changes. **OK.**

## 4. Reproducibility of published numbers

The target publishes no newly computed result, no claimed value of `I(tau)`, no value of `Ibar`, and
no numerical constant. Its fixed geometry (`r_p=3.0`, `r_q=0.5`, `v_p=0.0`, `v_q=0.02`,
`tau in [1.0,1.2]`) is the already recorded WP4 diamond and pair:
`wp4_comparable_pair_separation.md:347-353,394`.

The design correctly preserves the present status
`IBAR_DIAMOND_INTERVAL = INCONCLUSIVE_NUMERICAL_NONCONVERGENCE` and
`CONSTANT_LEVEL_DEFEATER = NOT_EVALUATED_IBAR_UNAVAILABLE`
(`wp4_ibar_interval_numerical_design.md:40-56`). It explicitly forbids deriving a `PASS`, `FAIL`,
efficiency constant, poset-information comparison, or `n*` from the unavailable quantity. **OK.**

## 5. dev/validation separation & ground-truth leakage

The target is expressly `DESIGN_ONLY / NO_IMPLEMENTATION / NO_EXECUTION`
(`wp4_ibar_interval_numerical_design.md:3-7`): it changes no integrator, invokes no sprinkling,
consumes no seed, and touches neither the sealed bank nor thresholds. Its authorization boundary
requires separate later PI approvals for implementation and execution (`:151-160`). There is no
new observable, hidden embedding, ground-truth score, persisted output, or route from exploratory
results into the sealed path. **OK.**

## 6. Claim-boundary check

The document does not elevate the current numerical nonconvergence to a scientific refutation, and
does not claim metric reconstruction, localisation, curvature, 3+1D, or an estimator result
(`wp4_ibar_interval_numerical_design.md:48-56,164-169`). It also distinguishes a point estimate,
a mesh maximum, and an interval envelope (`:114-129`), so it does not substitute a grid maximum for
the required supremum. **OK.**

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | The integrand and measure are stated: `I(tau)` is integrated against Lebesgue `dx dy` on the unit square after the normalized-volume copula construction; EF volume is `dv dr` | `wp4_ibar_interval_numerical_design.md:18-36` |
| 2 | OK | Small density, score cancellation, quantile inversion, root/monotonicity, and endpoint hazards have explicit fail-closed treatment; no silent clipping or extrapolation is permitted | `...design.md:58-70` |
| 3 | OK | Spatial resolution and the `tau`-derivative step are separate refinement axes, including a declared boundary rule for one-sided derivatives | `...design.md:72-84` |
| 4 | WARN | Concrete resolution ladders, numerical tolerances, and the selected independent route are deliberately deferred to a later executable contract. This is safe only because the document forbids implementation/execution until they are proposed before first execution, audited, and frozen; no terminal may be claimed before then | `...design.md:86-110,151-160` |
| 5 | OK | The convergence design prohibits post-hoc selection: it requires ordered ladders, absolute and relative tolerances, two confirmation levels, and fail-closed numerical/domain checks | `...design.md:86-100` |
| 6 | OK | Independent validation is required for an interior and an endpoint value, and disagreement must yield nonconvergence rather than route selection or averaging | `...design.md:102-110` |
| 7 | OK | The required interval certification is explicit: only `Ibar_envelope`, with a derivative/regularity bound or adaptive interval control between nodes, can support the uniform proposition; a grid maximum alone is insufficient | `...design.md:112-129` |
| 8 | OK | The four permitted terminals are exhaustive and fail-closed; unresolved envelope control cannot be converted into defeater `PASS` or `FAIL` | `...design.md:131-149` |
| 9 | OK | No `/comite` referral is required at this stage: there is no unresolved scientific conclusion or choice being silently decided. The future choice of numerical tolerances/independent method is expressly gated as a later, separately auditable executable contract | `...design.md:98-110,157-160` |
| 10 | WARN x23 | Pre-existing mechanical generator-reference baseline, not attributable to the target | `bash .claude/skills/auditor/audit.sh` (§2) |

AUDIT_ERRORS=0
AUDIT_WARNINGS=24

## 8. Verdict

The design passes its precommit audit with one bounded design-stage warning and the 23 pre-existing
mechanical warnings. It correctly fixes the object, separates both refinement axes, requires
independent validation, and — critically — rejects a mere grid maximum as certification of
`Ibar = sup_[tau in [1.0,1.2]] I(tau)`. It requires an upper envelope controlled between nodes by
regularity/derivative information or adaptive interval subdivision.

The remaining numerical thresholds and independent implementation choice are not yet executable
parameters, but this does not create a post-hoc route now: they must be declared before any first
execution, audited, and frozen in a later contract. Until that happens, the only permissible state
is design/audit completion; no quadrature, constant-level defeater decision, or scientific label may
advance. This is not a `/comite` issue at the present boundary.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
