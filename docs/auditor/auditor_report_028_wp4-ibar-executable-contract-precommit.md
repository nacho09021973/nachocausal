# Auditor Report 028 — wp4-ibar-executable-contract-precommit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `main`, HEAD `8a9ce63`. Trigger: **precommit audit
of the executable numerical contract only**, before an implementation authorization exists.

Target: untracked
`research_program/work_packages/wp4_ibar_interval_executable_contract.md`. The audit checks that
the contract freezes the numerical choices before code, preserves the prior abstentions, provides
an interval-wide envelope rather than a grid maximum, and creates no authorization to implement or
execute a quadrature.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code **0**, verbatim diagnostic tail:

```text
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.sha256
WARN: committed data file with no generator reference: data/reports/present_anchor_clean_v3_kill_test.csv
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
WARN: committed data file with no generator reference: evidence/new_geometry_20260719/mink_control_metrics.csv
----------------------------------------
Auditor: 0 error(s), 23 warning(s)
```

The complete 23-warning set is the unchanged generator-reference baseline for committed
`data/reports/` and `evidence/` files. The target is a document only and introduces no data,
generator, output, seed, or executable path.

## 3. Seal & freeze integrity

| Item | Value | Anchor |
| --- | --- | --- |
| Live seal | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `make verify-seal` |
| Frozen record | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `docs/preregistration_002.md:8` |
| Drift | **none** | — |

`nachocausal/thresholds.py` is not changed. **OK.**

## 4. Reproducibility of published numbers

The target reports no evaluated value of `I(tau)`, `Ibar`, the constant-level defeater, or
`n*`. Its decimal values are prospective contract parameters — geometry, mesh levels, derivative
steps and tolerances — not empirical claims. The fixed geometry is the previously recorded WP4
diamond: `wp4_comparable_pair_separation.md:347-353,394`.

The contract preserves, rather than replaces:

```text
IBAR_DIAMOND_INTERVAL = INCONCLUSIVE_NUMERICAL_NONCONVERGENCE
CONSTANT_LEVEL_DEFEATER = NOT_EVALUATED_IBAR_UNAVAILABLE
```

It makes an evaluated output impossible at this stage and explicitly leaves any later execution to a
separate authorization. No ungenerated numerical scientific result is published. **OK.**

## 5. dev/validation separation & ground-truth leakage

The target declares `CONTRACT_ONLY` and both
`IMPLEMENTATION_AUTHORIZATION = NOT_GRANTED` and
`EXECUTION_AUTHORIZATION = NOT_GRANTED`
(`wp4_ibar_interval_executable_contract.md:3-9`). It creates no code path, seed use, sprinkling,
observable, estimator, hidden embedding, sealed-bank contact, or output. Its §9 requires a later
audit before an implementation decision and expressly does not grant execution (`:212-218`).
**OK.**

## 6. Claim-boundary check

The contract cannot turn a mesh maximum into `Ibar`: it separates `Ibar_mesh` from
`Ibar_envelope` and requires directed-rounding interval enclosures over every tau cell
(`wp4_ibar_interval_executable_contract.md:147-180`). It says a lower point bound cannot declare a
defeater violation. Its three non-success terminals preserve the two abstention labels
(`:182-210`), and even the converged terminal requires a later execution audit and PI instruction
before a scientific label can advance. No claim about reconstruction, localisation, curvature, 3+1D,
a numerical PASS, or a numerical FAIL is made. **OK.**

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Object, measure, fixed corners and interval are explicit; prior nonconvergence and defeater abstention are preserved | `...executable_contract.md:11-32` |
| 2 | OK | The primary method fixes root tolerance, interpolation scope, separate spatial/coplanar grids, and fail-closed numerical checks | `:34-76` |
| 3 | OK | Four spatial levels, five derivative steps, absolute/relative tolerances, two later confirmations, and a no-refinement-on-failure rule remove post-hoc tuning | `:50-123` |
| 4 | OK | Interior symmetric and endpoint/unavailable-side unilateral Hellinger formulas are declared before execution and are not mixed for one node | `:78-107` |
| 5 | OK | Independent validation uses adaptive Gauss--Kronrod in `(x,y)`, bracketed quantile inversion without PCHIP or primary-grid reuse, at one endpoint and one interior point | `:125-145` |
| 6 | OK | Supremum certification requires directed-rounding interval upper and lower enclosures over all 160 cells; `Ibar_mesh` cannot substitute for `Ibar_envelope` | `:147-180` |
| 7 | OK | Exactly four fail-closed terminals are defined; none grants a defeater decision or execution authority | `:182-218` |
| 8 | OK | No implementation/execution authorization, seed path, ground-truth path, or scientific overclaim is introduced | `:3-9,202-218` |
| 9 | WARN x23 | Pre-existing mechanical generator-reference baseline, not attributable to the target | `bash .claude/skills/auditor/audit.sh` (§2) |

AUDIT_ERRORS=0
AUDIT_WARNINGS=23

## 8. Verdict

The contract is a sound documentary precondition for a future implementation decision. Its numerical
parameters are fixed before code exists; its independent route is distinct in both quadrature and
quantile construction; and its interval-arithmetic requirement prevents the prohibited replacement
of the supremum by a maximum over sampled `tau` values.

The only warnings are the unchanged 23-file repository baseline. No `/comite` question is exposed:
the contract does not resolve a scientific claim or silently choose an interpretation. It remains
necessary to keep it uncommitted until the user decides the next documentary action; this audit
does not authorize implementation, execution, a defeater result, or any status upgrade.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS

