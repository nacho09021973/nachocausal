# Auditor Report 025 — wp4-annex-c-remediation-reaudit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/adnac/nachocausal`, branch `main`, commit `5a53a6b` (working tree carries three
untracked files: the two Annex C artefacts and report 024). Trigger: **remediation re-audit** of
`docs/auditor/auditor_report_024_wp4-annex-c-comparable-pair-separation-precommit.md`, which closed
`AUDIT_VERDICT=AUDIT_FAIL` on 1 error plus 4 target-attributable warnings. Task: confirm or refute
that findings 1–5 of report 024 are closed, and check that the remediation edits introduced no new
defect.

Targets:

- `research_program/work_packages/wp4_comparable_pair_separation.md` (293 lines, edited)
- `research_program/work_packages/wp4_comparable_pair_separation_checks.py` (348 lines, edited: new
  check `[4b]`)

This report supersedes report 024's verdict; report 024 remains the record of what was wrong.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code **0**, tail (full listing is identical to report
024 §2 and is not re-pasted at length; the seal-`ok` line and all 23 WARN lines are byte-identical):

```text
WARN: committed data file with no generator reference: data/reports/present_anchor_clean_v3_kill_test.csv
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
WARN: committed data file with no generator reference: evidence/new_geometry_20260719/mink_control_metrics.csv
----------------------------------------
Auditor: 0 error(s), 23 warning(s)
```

Baseline unchanged: **0 errors, 23 warnings**, all 23 pre-existing and none attributable to Annex C
(the target adds no file under `data/`, `results/`, `evidence/` or `outputs/`). The remediation
introduced no new mechanical finding.

## 3. Seal & freeze integrity

| Item | Value | Anchor |
| --- | --- | --- |
| Live seal | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `make verify-seal` |
| Frozen record | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `docs/preregistration_002.md:8` |
| Drift | **none** — exact match, unchanged from report 024 §3 | — |

`nachocausal/thresholds.py` does not appear in `git status --short`. The remediation touched only
the two Annex C files. **OK.**

## 4. Reproducibility of published numbers

Script re-run twice: exit `0` both times, captures **byte-identical** (`diff -q`). Still
deterministic after the edit.

**Finding 1 of report 024 — CLOSED.** The new committed check `[4b]`
(`..._checks.py:306-318`) emits all four patch volumes and both relative differences:

```text
[4b] patch volume V(tau) = vol(D_tau), r_p=3.0, r_q=0.5 (note §5 item 1, the cardinality confounder):
     dv=4.00  tau=1.00   V(tau) = 11.501608349297
     dv=4.00  tau=1.20   V(tau) = 10.794261266781
     dv=4.00  relative difference |V(tau')-V(tau)|/V(tau) = 6.150e-02
     dv=0.02  tau=1.00   V(tau) = 0.049967998677
     dv=0.02  tau=1.20   V(tau) = 0.049922210322
     dv=0.02  relative difference |V(tau')-V(tau)|/V(tau) = 9.164e-04
```

The note now quotes these digit-for-digit and cites the check by name
(`wp4_comparable_pair_separation.md:220-222`: "a `tau`-dependent volume (check [4b]):
`V(1.0) = 11.501608349297` against `V(1.2) = 10.794261266781` … `6.150e-02` … `9.164e-04`"). The
previously ellipsised, unbacked digits are gone. Better than the minimum fix: the check carries
`assert v_a != v_b` (`..._checks.py:316`), so the proposition §5 item 1 rests on is a guardrail
that can actually fail rather than a printed number.

**Full provenance sweep, re-run.** Every numeric literal with ≥3 decimal places in the note (17
distinct) was required to appear **verbatim** in a fresh stdout capture: **unmatched = 0** (was 4).

**Cross-reference integrity (new check, not in report 024).** The note references check labels
`[1] [2] [3] [4] [4b] [5] [6] [7] [7b] [8] [9]`; the script emits exactly
`[1] [2] [3] [4] [4b] [5] [6] [7] [7b] [8] [9]`. No dangling or stale reference was introduced by
inserting `[4b]` mid-sequence.

**Prose-claim spot checks against the output.** The note's "eight `(tau, r_p, r_q)` configurations"
in check `[7b]` — output has exactly **8** data rows. Its "agrees to between 7 and 3 significant
digits" — measured relative differences span `3.33e-07` to `8.52e-04`, i.e. ~6–7 down to ~3
significant digits. Accurate. **OK.**

**Finding 4 of report 024 — CLOSED.** `…separation.md:100` now reads "symbolically — residual
exactly `0` — and against direct quadrature to `|diff| = 1.11e-15`", matching the printed value
exactly; the flattering rounding is gone and the symbolic residual is stated too.

**Finding 5 of report 024 — CLOSED.** `…separation.md:85-87` now reads "disagreed with the
quadrature by tens of sigma … That figure came from a discarded intermediate state and is *not*
reproducible from this repo; it is recorded as history, not as a result." The unreproducible `78` is
removed and the provenance is declared.

## 5. dev/validation separation & ground-truth leakage

Re-verified after the edit, not assumed:

- **Import surface unchanged.** `numpy`, `sympy`, `scipy.special.lambertw` only
  (`..._checks.py:32-34`).
- **No sealed-path contact.** Grep for `nachocausal|thresholds|seed_band|EXPLORE_POOL|dev/` and for
  any write path (`open(|write|savetxt|to_csv`) over the script returns nothing but the docstring's
  own disclaimer at line 11. The new `[4b]` block only calls the already-audited `area_sub` and
  prints; it writes no file and introduces no new dependency.
- **No validation artefact produced.** `git status --short` lists only the three untracked files.
- **Ground-truth leakage.** Unchanged from report 024 §5: no hidden embedding, no estimator, no
  observable — nothing for the rule to be violated on. The adjacent risk (a statistic that secretly
  reads absolute scale) remains explicitly tested and passing: check `[6]` gives dilation
  invariance to `< 1e-15`, so the statistic still cannot separate a Theorem-A scale-orbit pair.
- **Pause discipline.** Still a calculation only, as `docs/hoja_de_ruta_24_jul_2026.md` §2.1
  authorises. No roadmap §3 "No hacer" item breached. The ficha
  (`research_program/bibliography/ficha_se_busca_tv_order_only.md`) is **still unmodified** — it
  does not appear in `git status --short` — so the §2.4 ordering (audit before status change) is
  still intact at the time of this report. **OK.**

## 6. Claim-boundary check

**Finding 2 of report 024 — CLOSED, and the disclosure is now stronger than the minimum fix.**
`…separation.md:169-176` replaces "One step is argued" with "*Two steps are argued rather than
written out,* and both are labelled as such in §6", enumerating **(i)** analyticity of `p` in `dv`
at `0^+` and **(ii)** uniformity in `tau` of the `O(dv^2)` remainder. Item (ii) does not merely
name the gap, it concedes the substance of the original objection: "Continuity in `tau` of each
expansion coefficient … is *not* by itself enough for a uniform remainder bound; that needs joint
control, e.g. analyticity in `(dv, tau)` … which the same argument as (i) should give but which is
not carried out." The §6 label at `:278-280` now matches: "with the **two** steps noted in §4 —
(i) … (ii) … — argued rather than written out, and with `dv_0` non-effective."

*Observation, not a new finding.* Corollary C6 remains labelled `[PROVED (leading order)]` while
one of its supporting steps is conceded as "not carried out". This audit does **not** raise it as a
defect: the gap is now disclosed twice, in the proof and in the label, and the note supplies the
`[NUMERICAL]` fallback for the named pair (`:281-282`). That is the repo's established convention
for a proof leaning on a standard-but-unwritten regularity step. It is recorded here so a future
`/comite` sees it without having to rediscover it.

**Finding 3 of report 024 — CLOSED.** `…separation.md:180-183` now reads "For each admissible
`(r_p, r_q, tau_0, tau_1)` there is `dv_0 > 0` — depending on those four numbers only — such that
for all `0 < dv < dv_0` …". The quantifier no longer ranges `dv_0` over `dv`, and the dependency is
stated explicitly.

**No over-claim crept in.** Re-scan for `reconstruct|asymptotic horizon|3+1D|closes Forma L|proves
Forma L`: the only hit is `:247`, which is a *disclaimer* ("Nothing here is about the 3+1D
Schwarzschild pairs of FWP §2 or OP-1.2"). Forma L is still denied in the headline (`:22`, "It does
**not** close Forma L") and still `[OPEN]` in the status table (`:283`). §5's four-item obstruction
list is unchanged and this audit again finds no channel obstruction omitted from it. The claim made
remains inside the finite-patch 1+1D localisation boundary. **OK.**

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Report 024 finding 1 **CLOSED**: all four `V(tau)` values + both relative differences now emitted by committed check `[4b]` and quoted literally, with `assert v_a != v_b` guarding the claim | `..._checks.py:306-318`; `...separation.md:220-222` |
| 2 | OK | Report 024 finding 2 **CLOSED**: "two steps" enumerated in §4 and matched in the §6 label; step (ii) concedes that coefficient continuity is insufficient | `...separation.md:169-176`, `:278-280` |
| 3 | OK | Report 024 finding 3 **CLOSED**: `dv_0` now quantified over `(r_p, r_q, tau_0, tau_1)` only | `...separation.md:180-183` |
| 4 | OK | Report 024 finding 4 **CLOSED**: `\|diff\| = 1.11e-15` matches printed output; symbolic residual `0` also stated | `...separation.md:100` |
| 5 | OK | Report 024 finding 5 **CLOSED**: `78` removed, replaced by "tens of sigma" + explicit non-reproducibility declaration | `...separation.md:85-87` |
| 6 | OK | Provenance sweep clean: 17/17 numeric literals (≥3 decimals) appear verbatim in fresh stdout; unmatched = 0 (was 4) | `grep -F` over fresh capture |
| 7 | OK | Check-label cross-references intact after inserting `[4b]`: 11 referenced = 11 emitted, no dangling reference | `grep -oE` over note vs stdout |
| 8 | OK | Prose claims match output: `[7b]` has exactly 8 rows; relative differences span `3.33e-07`–`8.52e-04` ("7 to 3 significant digits") | `...separation.md:269-271`; check `[7b]` |
| 9 | OK | Script still deterministic and green: exit 0 twice, two captures byte-identical | `diff -q` over two stdout captures |
| 10 | OK | Seal unchanged and matching the frozen record; `thresholds.py` untouched | `make verify-seal`; `docs/preregistration_002.md:8` |
| 11 | OK | No new dependency or sealed-path contact from the edit; import surface still numpy/sympy/scipy; no write path | `..._checks.py:32-34`; grep for write/dev/threshold patterns |
| 12 | OK | Orbit test still passes to `< 1e-15`; statistic cannot separate a Theorem-A scale-orbit pair | check `[6]` |
| 13 | OK | No over-claim introduced: Forma L still denied in headline and `[OPEN]` in status table; only 3+1D mention is a disclaimer | `...separation.md:22,247,283` |
| 14 | OK | Ficha status labels still unedited — roadmap §2.4 ordering intact | `git status --short` |
| 15 | WARN ×23 | Pre-existing mechanical baseline (committed data files with no generator reference) — unchanged, **not attributable to this target** | `bash .claude/skills/auditor/audit.sh` (§2) |

AUDIT_ERRORS=0
AUDIT_WARNINGS=23

## 8. Verdict

All five findings of report 024 are **confirmed closed**, and the remediation introduced no new
defect: the provenance sweep is clean (17/17, was 13/17), check-label cross-references survived the
insertion of `[4b]`, the import surface and seal are unchanged, and the claim boundary is intact.
Two fixes went beyond the minimum — `[4b]` carries an assertion rather than merely printing, and
§4's step (ii) concedes the substance of the objection instead of relabelling it.

The residual 23 warnings are the repo's pre-existing `data/reports/` generator-reference baseline,
identical to report 024 §2 and to report 023; none arises from Annex C. Under the protocol they
keep the verdict at `AUDIT_PASS_WITH_WARNINGS` rather than `AUDIT_PASS`. They are a standing repo
hygiene item, not a finding against this target, and should not be read as qualifying Annex C.

Annex C is now sound ground. The roadmap §2.4 precondition is satisfied: the ficha's
`[OPEN por par]` label for ingredient (a) of §7.1 may be changed on the strength of this audit,
provided the change is scoped to what §5 of the note actually supports — ingredient (a) for the
WP4 §4 diamond family only, with Forma L left `[OPEN]`. One carry-forward for any future
`/comite`: the disclosed-but-unwritten uniformity step behind Corollary C6 (§6, "Observation").

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
