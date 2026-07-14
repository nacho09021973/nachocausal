# Auditor Report 012 — pr012-draft-scope-preflight

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

**Trigger:** G2a-style preflight on a PR012 draft, requested before the draft is committed and
before any future freeze/publication decision. The draft's scope (candidate (a): TV vs Δτ curve
at fixed n=8, corrected `BC^n` tensorization) was set by a **direct PI directive** following
`docs/comite/comite_decision_023_pr012-scope-adjudication.md`'s `RECOMMEND_REVISE_AND_RECONVENE`
verdict, not a second full `/comite` session — the draft spec's own §0 discloses this.

**Target:** three new, currently **untracked** files: `dev/pr012_tv_curve_certification.py`,
`tests/test_pr012_tv_curve_certification.py`, `research_program/synthesis/pr012_tv_curve_scope.md`
(status `DRAFT_SCOPE`, explicitly not `FROZEN`).

**Out of scope:** authorizing a freeze, authorizing publication of `data/reports/pr012_*`
artifacts, PR011's own already-audited results (unchanged, re-verified only as a cross-check
anchor in §4 below).

## 2. Mechanical audit

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: [35 files, incl.
      auditor_report_001..011, comite_decision_001..023, hoja_de_ruta_*, preregistration_002/003]
WARN: committed data file with no generator reference: [22 pre-existing entries, unchanged from
      auditor_report_010/011 — see those reports for the full list]
----------------------------------------
Auditor: 0 error(s), 22 warning(s)
```

Exit code: `0`. Unchanged from `auditor_report_011` — expected, since the PR012 draft's `curve`
command was only ever run with `--dry-run` this session; no `data/reports/pr012_*` artifact
exists to be flagged either way.

## 3. Seal & freeze integrity

- `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
  (unchanged).
- `grep -n "thresholds\|nachocausal/" dev/pr012_tv_curve_certification.py
  tests/test_pr012_tv_curve_certification.py research_program/synthesis/pr012_tv_curve_scope.md`
  → **no matches**. None of the three new files reference `nachocausal/thresholds.py` or the
  sealed estimator path at all.

## 4. Reproducibility of published numbers

All six items requested in the trigger scope were independently re-derived or re-run this
session, not read from the draft's own prose.

**4.1 — Reuse, not redefinition (item 1).** Independently confirmed by identity check, not just
value equality:

```
>>> pr012.terminal_for_epsilon is pr011.terminal_for_epsilon
True
>>> pr012.R_P is pr011.R_P, pr012.R_P == pr011.R_P
True True
>>> pr012.TAU_FAMILY == pr011.TAU_FAMILY
True
```

`dev/pr012_tv_curve_certification.py` imports these from `dev.pr011_tv_certification_enumeration`
(after this session's import-path fix — see §7) rather than redefining them; there is no drift
surface for the frozen anchor or for the already-fixed (`auditor_report_011`) terminal-selection
logic.

**4.2 — Tensorization math and the claimed cross-check (item 2).** Re-derived from raw
`math.sqrt`/exponentiation, independently of `pr012`'s own functions, using PR011's frozen
certification pair's `H² = 1.3293513475560046e-06`:

| `n` | naive (independent) | tensorized (independent) | ratio | `1/√n` |
|---|---|---|---|---|
| 4 | 0.004611899229 | 0.002305947316 | 0.500000 | 0.500000 |
| 5 | 0.005764874036 | 0.002578126618 | 0.447213 | 0.447214 |
| 6 | 0.006917848843 | 0.002824195271 | 0.408248 | 0.408248 |
| 7 | 0.008070823650 | 0.003050478525 | 0.377964 | 0.377964 |
| 8 | 0.009223798457 | 0.003261097632 | 0.353553 | 0.353553 |

The independently-derived `naive` column at every `n` matches the corresponding
`epsilon_certified_upper` already published in `data/reports/pr011_tv_certification_n{4..8}.csv`
exactly (spot-checked `n=8` directly against the committed CSV: `0.009223798457` in both). The
`ratio ≈ 1/√n` claim holds to 6 significant figures at every `n`. Both the module docstring's and
the spec's §3 claim that the correction is "not negligible even at PR011's tractable n" (a ~2.83x
tightening at `n=8`) are **confirmed, not merely asserted**.

**4.3 — The two floors are genuinely distinct (item 3).** `HELLINGER_H2_REL_TOL = 1e-3` is
confirmed, by `git log -p --follow`, to have been introduced in commit `873573f` ("Add PR011 TV
enumeration scaffold and discharge G0b") — well before this session, not a threshold invented for
PR012. Independently re-running `verify_hellinger_stability` (PR011's own, unmodified function)
directly on the two smallest grid points:

```
dt=0.0125: RAISES -- Hellinger grid instability: rel_gap=1.274664e-03 > 0.001
dt=0.025:  RAISES -- Hellinger grid instability: rel_gap=1.199696e-03 > 0.001
dt=0.05:   OK h2=3.318788e-07
```

confirms both flagged points genuinely fail PR011's pre-existing gate, and the third point (the
next rung up in the frozen ladder) does not. The spec's characterization of this as "PR011's
frozen instability guard doing its job," not a new PR012 threshold, is accurate. The separate,
deeper `DELTA_TAU_FLOOR=1e-9` (floating-point/quadrature noise floor, established earlier this
session by comparing measured `H²` against the proved Fisher/QMD `(Δτ²/4)Ībar` law across eleven
decades) is correctly described as a different, non-binding-in-practice floor — the two are not
conflated in the spec text.

**4.4 — Test suite and CLI dry-run (item 6).** Re-run independently this session:

```
$ python3 -m pytest tests/test_pr012_tv_curve_certification.py tests/test_pr011_tv_certification_enumeration.py -q
34 passed in 72.52s
$ python3 dev/pr012_tv_curve_certification.py curve --dry-run
[output matches the spec §4 preview table row-for-row, including both GRID_RESOLUTION_ABSTAIN
 rows and all four certified rows' epsilon/minimax-floor/terminal values]
```

No discrepancy between the spec's claimed preview table and the live re-run.

## 5. dev/validation separation & ground-truth leakage

- No hidden-embedding contact anywhere in the three new files (this is the pure theory-side
  identifiability track, same as PR011).
- `Δτ` ladder, `DELTA_TAU_FLOOR`, and `FIXED_N=8` are all fixed in the module before any curve
  point is computed (verified by reading the module: the ladder and floor are module-level
  constants defined above every function, not derived inside `certify_curve`).
- No PR009/PR010 input path referenced anywhere in the three new files.

## 6. Claim-boundary check

- **OK (item 5):** independently confirmed that every reported row — in the CLI printer
  (`_print_curve`), the CSV renderer (`render_curve_csv`/`CURVE_CSV_FIELDS`), and the spec's own
  §4 table — carries `terminal` and `minimax_error_floor` (or, for abstained points, an explicit
  `n/a`/`None`) side by side on the same line/row. There is no code path or table row in this
  draft where `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` appears without its numeric consequence
  attached, which is the specific over-claim pattern `auditor_report_011` found and fixed in
  PR011. `grep` for "distinguish" in the spec surfaces exactly one hit, and it is the corrective
  sentence explicitly warning against reading the curve as showing "easy" distinguishability, not
  an over-claim.
- **OK:** no claim of metric reconstruction, asymptotic/global horizon, 3+1D, or absolute-unit
  mass estimation found in any of the three new files; §2.2/§6 of the spec restate PR011's claim
  boundary and add the curve-specific caveat.
- **OK:** the spec's §0 and §8 disclose plainly that this scope was set by a direct PI directive,
  not a fresh multi-agent `/comite` session, and that G2a/G2b remain open pending this very audit
  and a future publication decision — no gate is silently marked discharged that wasn't.
- **WARN (minor, documentation-only):** the Theorem-A-converse rigidity argument this draft leans
  on (spec §2.1) is, by the spec's own admission, an unlabeled prose paragraph in
  `first_witness_pair_candidates.md` §4 (a *different* section, about a failed attempt), not a
  separately numbered, fully spelled-out theorem. The spec already flags this itself (§2.1
  caveat, §9) rather than hiding it — recorded here as a WARN because it remains a real,
  un-closed loose end this draft depends on, not because the spec mischaracterizes it.

## 7. Findings

| # | Severity | Finding | Anchor |
|---|---|---|---|
| 1 | OK | `terminal_for_epsilon`, frozen anchor constants reused by import (identity-checked), not redefined | §4.1 |
| 2 | OK | Tensorized bound formula independently re-derived, matches claimed `1/√n` ratio and PR011's published `n=8` value exactly | §4.2 |
| 3 | OK | `DELTA_TAU_FLOOR` and `HELLINGER_H2_REL_TOL` are genuinely distinct, correctly characterized; the two abstained grid points genuinely fail PR011's pre-existing (not new) gate | §4.3 |
| 4 | OK | No reference to `nachocausal/thresholds.py` or sealed estimator in any of the three new files; seal unchanged | §3 |
| 5 | OK | Every curve-point terminal is reported with its minimax-floor consequence attached — the `auditor_report_011` over-claim pattern is not repeated | §6 |
| 6 | OK | Test suite (34/34) and CLI dry-run independently re-run this session, match the spec's §4 table exactly; dry-run writes no artifact | §4.4 |
| 7 | WARN | The Theorem-A-converse argument this draft relies on (spec §2.1) remains an unlabeled paragraph in a different section, not a named, separately proved lemma — the spec discloses this itself | §6 |
| 8 | OK (self-corrected mid-session, noted for the record) | An initial import-path bug (`sys.path.insert(_HERE)` + bare `pr011_tv_certification_enumeration` import) caused a duplicate module load that broke an identity-based drift-check test; fixed to `sys.path.insert(_ROOT)` + `from dev.pr011_tv_certification_enumeration import ...` before this audit ran. Verified fixed in §4.1. | resolved prior to this audit, not a live finding |

AUDIT_ERRORS=0
AUDIT_WARNINGS=1

## 8. Verdict

Every claim this draft makes about itself — reuse without redefinition, the correctness and
magnitude of the tensorization correction, the two-floor characterization, the claim-boundary
discipline, and the reproducibility of its own preview table — was independently re-derived or
re-run this session and confirmed. No error found; the seal is untouched; no artifact has been
published. The single warning is a pre-existing, self-disclosed loose end (an unlabeled but
apparently load-bearing rigidity argument in a different document) that does not block committing
this draft, but should be resolved — by promoting it to a named lemma, or by an explicit
`/comite`/literature check — before this spec is marked `FROZEN` or before any curve artifact is
published. This draft is sound ground to commit as `DRAFT_SCOPE`; G2a is now discharged. G2b
(pre-publication `ε` audit) and the freeze decision itself remain open, as the spec's own §8
already states.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
