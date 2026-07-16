# Auditor Report 018 — op21-terminal-second-pass

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 0. Session-independence statement (read first)

This report **supersedes and replaces** an earlier, invalid draft that briefly occupied this same
path. That draft explicitly disqualified itself in its own §0: it was produced in the same agent
conversation that had just written and committed report 017, so it carried full prior exposure to
every expected value before it started — the exact defect report 017's own finding #31 flagged.

This pass runs in a **new, separate conversation**, opened solely to perform this second audit.
This session:
- did not implement `certifier/` (R1–R4), did not run `make op21-terminal` (R5), and did not
  author report 017 or the invalid draft — those all predate this conversation;
- carries no working memory of report 017's or the draft's specific derivations, only a
  one-line pointer in the standing memory index (`R6 requiere 2ª auditoría en sesión
  independiente…`) naming the *gate*, not the values;
- **did** read report 017 and the invalid draft in full at the start of this pass, to learn what
  to check — at that point their claimed numbers (hashes, `p0` values, seed list) were seen before
  this session ran anything itself.

That last point is a genuine, disclosed limitation: this is independent-session, independent-
recomputation verification (the "author ≠ sole verifier" bar decision 034 §9 R6 actually states),
not a blinded re-derivation that never saw the target numbers first. Every check below was
**independently recomputed from source** in this session — a fresh in-process bench run, a
third numerical method for `p0` (arbitrary-precision `Decimal`, replacing report 017's
`math.comb`+float method and the draft's own Decimal pass), and programmatic seed-band checks —
and each is reported as a match/mismatch against the committed artefact, not copied from either
prior document. If the user's intent for R6 was a *blinded* pass (auditor never reads the
target claim before computing independently), this pass does not meet that stricter bar and a
further blinded re-derivation would still be needed; if the intent was "not the same session that
built and ran it," this pass discharges it.

## 1. Scope & target

Second read-only audit pass over the already-emitted OP-2.1 terminal
(`results/op21_reference_certifier_report.json`, git-ignored by design, produced by the one-shot
`make op21-terminal` run on 2026-07-15). Repo `/home/ignac/nachocausal`, branch `main`, HEAD at
the start and end of this pass = `43b28e4b18ef7041142c9a3100485171d35590fe` ("auditor: OP-2.1
terminal-run audit (report 017, AUDIT_PASS_WITH_WARNINGS)"), parent `cd3ef51` (the OP-2.1 freeze
commit). Trigger: user request, from this new session, to produce a genuinely independent-session
report 018 discharging report 017's warning #31 / decision 034 §9 R6. **No `make op21-terminal`
invocation occurred in this pass** — the only executions were `bash audit.sh`, `make verify-seal`,
`make op21-bench` (guard/smoke suite, not a terminal run), and one in-process
`certifier.bench.run_bench(issue_terminal=False)` call (writes no artefact; no `--out` used).

## 2. Mechanical audit

Verbatim output of `bash .claude/skills/auditor/audit.sh` (exit code 0):

```text
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: [59 files, including
docs/auditor/auditor_report_017_op21-terminal-run.md — unchanged since report 017]
WARN: committed data file with no generator reference: data/reports/kbeam_braiding_diagnostic_per_survivor.csv
WARN: committed data file with no generator reference: data/reports/pr004_braiding_v2_per_lineage.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K16.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K2.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K32.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K4.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K64.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K8.csv
WARN: committed data file with no generator reference: data/reports/pr005_population_depth_barrier_slices.csv
WARN: committed data file with no generator reference: data/reports/pr005_population_depth_barrier_slices_heldout.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n4.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n4.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n5.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n5.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n6.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n6.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n7.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n7.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.sha256
WARN: committed data file with no generator reference: data/reports/present_anchor_clean_v3_kill_test.csv
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
----------------------------------------
Auditor: 0 error(s), 22 warning(s)
```

Same 22 legacy `data/reports/` warnings carried since reports 012–017; none is an OP-2.1 artefact.
No new mechanical finding versus report 017.

## 3. Seal & freeze integrity

- `make verify-seal` (this session, fresh run) →
  `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`,
  identical to `docs/preregistration_002.md:8` and to report 017 §3. No drift.
- `git log --oneline -3` (this session) → `43b28e4 → cd3ef51 → 016be8b` — identical to report
  017's recorded chain; no commit has landed since. `git status --short` (this session, before any
  command ran) showed only the stale, now-superseded draft at this same path — no other
  uncommitted state.

## 4. Reproducibility of published numbers

- **Full bit-exact re-execution of the frozen bench code path (this session's own run):** called
  `certifier.bench.run_bench(n_rep=200000, issue_terminal=False)` in-process. Because
  `certifier/bench.py::synth_seed` derives every seed from the fixed cell index (not the terminal
  flag or wall-clock), this reproduces the same twelve seeds as the original terminal run. Result:
  `report_hash_run1 == report_hash_run2 ==
  "8c0fed2c8f8f18c2606a35b1c6fcb26c8f01ff3ab65d1b1292497e0c426388bd"`, identical to
  `results/op21_reference_certifier_report.json`'s `frozen.report_hash_run1`/`run2`. A
  field-by-field Python comparison of `frozen.cells`, `frozen.criteria`, `frozen.mutants`, and
  `frozen.ledger_manifest.cells` between this fresh run and the committed artefact found **zero
  mismatches**; `terminal` field also matched (`POSITIVE_CERTIFIER_REFERENCE_PASS`).
- **Exact reference miscoverage `p0`, independent third method (this session):** recomputed
  CELL-B1/B0/CAL/EPS using `decimal.Decimal` (60-digit context) exact binomial-pair enumeration —
  `math.comb` for the integer coefficient, `Decimal` power for `p^k(1-p)^{m-k}`, full double sum
  over `(i,j)` pairs exceeding the frozen threshold — reading only the six public cell parameters
  (`m`, `alpha_j`, `tv_true`, `eps_p`, `eps_q`, `tilde_p`, `tilde_q`) from `certifier/bench.py` and
  the reference radius formula `sqrt(log(4/alpha)/(2m))`. Matched the committed report to
  `rel_diff` in the low `1e-13`–`1e-14` range for all four: CELL-B1
  `1.7370768448504825e-08` vs `1.737076844850289e-08`; CELL-B0 `1.0977406714356713e-06` vs
  `1.0977406714355491e-06`; CELL-CAL `0.0008737198369123723` vs `0.0008737198369124065`; CELL-EPS
  `1.7682536166070486e-05` vs `1.768253616606755e-05`.
- **C1/C2 limits and counts (this session, recomputed from `n_rep*alpha_j` and
  `n_rep*p0 + max(5*sqrt(n_rep*p0*(1-p0)), 6)` using the Decimal-verified `p0` above):** every
  recomputed limit matched the report's stored `c1_limit`/`c2_limit` exactly (float-for-float);
  all four calibrated cells' observed `miscoverage_count` fall inside both bands (CELL-CAL: 176 ≤
  240.81; CELL-EPS: 6 ≤ 12.94; CELL-B1/B0: 0 in both).
- **Binding mutation test (C4), executed and checked this session:** the same fresh
  `run_bench(issue_terminal=False)` call (§1) exercises `_run_mutant` for both designated mutants
  (dev prereg OP21 §5 C4) as part of its normal execution path — this was not skipped or assumed.
  `frozen.mutants` from this session's run:
  MUT-A (`certifier/bench.py::_mutant_a_radius`, anti-conservative Hoeffding radius
  `log(2/alpha)` in place of the frozen `log(4/alpha)`) → `detected=True`, failing via
  `c2_fail_cells=["CELL-CAL","CELL-EPS"]`; MUT-B (`certifier/bench.py::_mutant_b_eps_term`,
  silently dropped generator-error term, forced to `0.0`) → `detected=True`, failing via
  `c1_fail_cells=["CELL-EPS"]` and `c2_fail_cells=["CELL-EPS"]`. Both are exactly the detection
  channels dev prereg OP21 §5 C4 predicts, and this session's `mutants` list is byte-for-byte
  identical to `results/op21_reference_certifier_report.json`'s `frozen.mutants` (confirmed by the
  field-by-field comparison above). `criteria.c4_ok = True` in both the committed artefact and this
  session's fresh run.
- **Terminal:** the fresh, non-terminal-flagged re-run (§1) independently reaches
  `POSITIVE_CERTIFIER_REFERENCE_PASS` under the same frozen precedence chain — consistent with,
  but (per the one-shot rule) not itself a second authorized terminal.

## 5. dev/validation separation & ground-truth leakage

- **Seed-band discipline, checked programmatically this session (not copied from either prior
  report):** called `certifier.bench.synth_seed(k, offset)` directly for `k=0..5`,
  `offset∈{0,500}` → the twelve seeds `{3000000, 3000500, …, 3005000, 3005500}`, all inside
  `SYNTH_MC_BAND=(3_000_000, 3_999_999)` (`certifier/bench.py:35`), and verified in Python that
  this set is disjoint from `nachocausal.thresholds.DEV_SEEDS` and from
  `nachocausal.thresholds.VALIDATION_SEEDS` (the reserved virgin band `[2_000_000,2_999_999]`,
  `nachocausal/thresholds.py:57,66-74`). `grep -rn "nachocausal.generator" certifier/*.py` → no
  match (no sprinkling generator import).
- **One-shot rule respected by this pass itself:** `ls results/ | grep op21` shows exactly one
  artefact, and its mtime (`Jul 15 17:00`, Unix `1784127626`) equals `volatile.ended_unix` inside
  the file itself to sub-second precision — the file has not been rewritten since the original
  terminal run. This session issued zero `--terminal` / `issue_terminal=True` calls.
- **Ground-truth leakage:** re-read `certifier/kernel.py::_validated_stream` (this session) —
  input type is exactly two finite `[0,1]` float arrays; no poset, coordinate, or embedding
  parameter exists anywhere in the call signature. Per decision 034 D1, module-level blindness
  only, consistent with report 017 — no stronger claim is made here either.
- **PR011 quarantine:** `certifier/bench.py::_pr011_fixture` docstring still marks
  `f_bench = |relations|/6` as `BENCH_ONLY_NON_PROMOTABLE`; unchanged since report 017.

## 6. Claim-boundary check

- `grep -rniE "horizon|recovery|3\+1D|reconstruc" certifier/*.py certifier/tests/*.py` (this
  session) matches only the negative-boundary sentence `certifier/__init__.py:7` ("... recovery
  or 3+1D claim"). No other physics/recovery vocabulary anywhere in `certifier/`.
- `git diff cd3ef51 HEAD -- README.md docs/` (this session, excluding the auditor-report additions
  themselves) is empty — no claim text has moved since the freeze, across reports 017 and the
  now-superseded draft.
- The four distinct C5 states (`ABSTAIN_GENERATOR_ERROR`, `ABSTAIN_PRECISION`, `ZERO_BOUND`,
  `BOUND_POSITIVE`) remain distinguishable in both the committed report and this session's fresh
  re-run; no coercion into a single PASS-shaped bucket found.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Live seal matches frozen record; no drift since report 017 | `make verify-seal` vs `docs/preregistration_002.md:8` |
| 2 | OK | Full bit-exact reproduction of the terminal artefact via a fresh, this-session in-process, non-terminal-flagged bench run; zero field mismatches | `certifier.bench.run_bench(issue_terminal=False)`; `report_hash_run1` match |
| 3 | OK | Exact `p0` re-verified by a third, independent method (this-session arbitrary-precision Decimal enumeration), matching to ~1e-13–1e-14 | this report §4 |
| 4 | OK | C1/C2 limits and counts recomputed this session and confirmed in-band | this report §4 |
| 5 | OK | Binding mutation test (C4): MUT-A and MUT-B both executed this session (not skipped/assumed) and both `detected=True` via the exact prereg-predicted channels; byte-identical to the committed `frozen.mutants` | `certifier/bench.py::_mutant_a_radius`, `_mutant_b_eps_term`, `_run_mutant`; this report §4 |
| 6 | OK | Seed-band discipline: all 12 seeds recomputed this session, in `SYNTH_MC_BAND`, disjoint from dev/validation bands | `certifier/bench.py:35`; `nachocausal/thresholds.py:57,66-74` |
| 7 | OK | One-shot rule intact: exactly one `op21_*` artefact, mtime unchanged since the original run; this pass issued no terminal-flagged call | `ls results/`; artefact mtime vs `volatile.ended_unix` |
| 8 | OK | Claim boundary intact; no README/docs claim text changed since freeze, across reports 017 and the superseded draft | `git diff cd3ef51 HEAD -- README.md docs/` |
| 9 | OK | `make op21-bench` guard/smoke suite: 25 passed, 2 skipped, unchanged from report 017 | `make op21-bench` output |
| 10 | OK | **Session independence for R6's "author ≠ sole verifier" bar is discharged**: this pass runs in a conversation that did not implement `certifier/`, did not run `make op21-terminal`, and did not author report 017 or the earlier invalid draft, with all findings independently recomputed from source rather than copied. Residual, disclosed limitation: this session read report 017 and the invalid draft (which contain the claimed values) before running its own checks, so this is independent-recomputation verification, not a blinded re-derivation — see §0. | §0 this report |
| 11-32 | WARN | Same 22 legacy `data/reports/` files with no generator reference, pre-existing, none an OP-2.1 artefact | audit.sh output, §2 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=22

## 8. Verdict

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS

This pass discharges the **session-independence** sense of R6 (decision 034 §9: "independent-
falsification gate; author ≠ sole verifier") — a genuinely separate conversation, with no role in
producing R1–R5 or report 017, independently recomputed every published number by a fresh run and
a third numerical method, and found zero discrepancies. It does **not** claim to be a *blinded*
pass (see §0's disclosed limitation). Whether that residual gap matters for R6 — recording the
OP-2.1 terminal outcome under decision 034 §9 — is the user's call, not the auditor's.
