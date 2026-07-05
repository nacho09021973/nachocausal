# Auditor Report 005 — prereg002-pass-raw-artifact-integrity

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/adnac/nachocausal`, branch `main`, HEAD `abf90f0`, audited 2026-07-03.
Trigger: falsifier finding of comité 015
(`docs/comite/comite_decision_015_r-var-selector-adjudication.md` §5, failure mode 7b): the
on-disk `results/validation.json` + `results/validation_run.log` appear to contain the
prereg-001-era **FAIL** (seeds 11…65537, thresholds sha `ad02cb57…`), while
`docs/preregistration_002_result.md:11` cites `results/validation.json` as the raw output of the
prereg-002 **PASS**. Question: is the published PASS backed by a live, inspectable raw artifact,
or only by the committed transcription?

Note on working-tree state at audit time: `formal/HorizonFormal/HorizonFormal/Horizon.lean` was
restored to HEAD immediately before this audit (user-authorised, comité 015 precondition);
`git status` shows it clean. Remaining modified tracked file: `INSTRUCCIONES.md` (out of scope).

## 2. Mechanical audit

```
Auditor — auditing: /home/adnac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
```

Exit code: 0.

## 3. Seal & freeze integrity

- `make verify-seal` (this session) → `nachocausal/thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- MATCHES the frozen record `docs/preregistration_002.md:8` and the seal commit `573cfcb`
  ("Seal prereg-002 (prereq #3)", 2026-06-22 12:20:06 +0200). Live instrument = the one the
  current prereg names. No drift.
- Seed-band guards in the sealed file are real and can fail: `nachocausal/thresholds.py:66-79`
  (`VALIDATION_SEEDS` 20 values in `[2_076_703, 2_983_811]`; asserts band membership and
  disjointness from `DEV_SEEDS`).

## 4. Reproducibility of published numbers

**The audited claim:** `docs/preregistration_002_result.md:7-12` — "Verdict: PASS … Raw output:
`results/validation.json` (git-ignored; transcribed below)."

**Finding — the cited raw artifact does not contain the PASS. It contains the prereg-001-era
FAIL:**

- `results/validation.json` on disk (mtime **2026-06-21 12:14**, `ls -la results/`):
  `seeds = [11, 23, 57, 88, 137, 271, 314, 577, 911, 1618, 2024, 4099, 5040, 6700, 7777, 8191,
  9001, 12289, 27644, 65537]`; `verdict = FAIL`;
  `checks = {…, ii_localisation_primary: False, iv_false_positive_primary: False, …}`
  (read this session via `json.load`).
- `results/validation_run.log` (mtime 2026-06-21 12:14) ends: `== DONE in 32.5 min == /
  verdict: FAIL / written: /home/adnac/nachocausal/results/validation.json`.
- `results/validation_provenance_launch.txt` records that run's instrument:
  `thresholds_sha256: ad02cb57e1445ca83a489bd4f3f9cae151517ca2aedbd1b29c44c60ac65f7faa`
  (the **prereg-001** seal, superseded per `docs/estimator_v2_seal.md:9` "Was `ad02cb57…` for
  the prereg-001 instrument"), commit `672eb14`, captured 2026-06-21T09:05:58Z.
- **Timeline contradiction:** the file's mtime (2026-06-21 12:14) **predates the prereg-002 seal
  commit** `573cfcb` (2026-06-22 12:20:06) and the PASS record commit `fee12d5` (2026-06-22
  12:33:20). Therefore the prereg-002 PASS run never wrote to the cited path **on this machine**.
- **No live artifact anywhere in the working copy backs the PASS:** a repo-wide grep for the
  first held-out seed `2076703` (excluding `.git/`, `biblioteca/`, `.lake/`) matches only
  text/spec artifacts: `nachocausal/thresholds.py`, `docs/preregistration_002.md`,
  `docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md`. No `results/*`, no
  `dev/*.log`, no JSON contains any virgin-band seed.
- **No launch provenance exists for the PASS**, in asymmetry with the FAIL run (which has
  `results/validation_provenance_launch.txt` with commit, sha, uname, pip freeze, UTC
  timestamps). `docs/preregistration_002_result.md` contains no timestamps, no uname, no elapsed
  time, no per-seed log.
- **Timing plausibility gap (unexplained, not adjudicated):** the window between the seal commit
  (12:20:06) and the PASS record commit (12:33:20) is **13m14s**. The smaller prereg-001 run (80
  BH `_per_seed` calls, same intensities, same machine) took **32.5 min**
  (`results/validation_run.log`), with the 12000-intensity tier alone at ~75 s/seed × 20 = ~25
  min. The prereg-002 protocol additionally scores paired MINK controls (the transcribed table's
  "abstain BH / MINK" column, `docs/preregistration_002_result.md:29-34`, implies ~160 calls).
  Consistent innocent explanations exist (run on a faster machine — `results/` is git-ignored
  (`.gitignore:21`) so raw output would not sync; or launch before the seal *commit* with the
  sealed file content already final on disk — the deterministic draw
  `VALIDATION_DRAW_SEED=20260622` and matching SHA make this possible), but **none is recorded
  anywhere in the repo**.

**What remains true:** the PASS's generator IS committed and deterministic — `validate.run()` on
the sealed package at `573cfcb` with the frozen `VALIDATION_SEEDS` would reproduce the verdict
bit-for-bit in principle. The auditor did NOT run it (running the sealed validation path is
forbidden to this role; re-running a committing step is the user's call, and prereg-002's binding
rule "first and only evaluation of the held-out band" makes any re-run itself a committee
matter). The PASS is therefore **not unbacked in the generator sense, but it is backed today
solely by the committed transcription** (`fee12d5`), with its cited raw-output pointer
contradicted by the file at that path.

Other published numbers (prereg-001 FAIL, `docs/preregistration_001_result.md`): the on-disk
artifacts fully corroborate the published FAIL (coverage/fp values in `results/validation.json`
match the FAIL-era record). The report-alike rule was honoured: the FAIL is recorded as plainly
as the PASS. `make test` was not re-run this session (fixtures unchanged since seal; audit.sh
covers the structural checks).

## 5. dev/validation separation & ground-truth leakage

- **No virgin-seed leak found:** no `dev/` script, log, or ensemble references any seed in
  `[2_000_000, 2_999_999]` (grep for `2076703` and band patterns across `dev/*.log`, `dev/*.py`;
  zero hits outside thresholds/docs). The `EXPLORE_POOL` (`dev/explore_seeds.py:23`) and
  `DEV_SEEDS` (`thresholds.py:57`) are disjoint from the band, and the sealed file asserts it
  (`thresholds.py:76-79`).
- **Exploration sandbox out of the sealed path:** `results/` is git-ignored by design
  (`.gitignore:21`); `dev/dev_ensemble_raw/` untracked; no sealed-path file imports from `dev/`
  (unchanged since auditor 001/002).
- **Hidden embedding:** no new path found by which the embedding defines or guides the
  observable; the R-VAR spec under committee review is write-only and unimplemented. No change
  to the standing assessment.

## 6. Claim-boundary check

- `docs/preregistration_002_result.md:52-64` states the bounded claim correctly ("Means… finite
  patch… Does NOT mean: the global event horizon… full metric reconstruction; 3+1D…"). No
  over-claim found in the audited documents.
- The transparent caveat at the non-primary level (fp=0.10 at 6000, recorded, verdict scored at
  primary only, `docs/preregistration_002_result.md:47-50`) is the frozen rule applied as
  written, not a coercion.
- No abstain/OUT_OF_DOMAIN coerced into PASS/FAIL was found in the audited scope.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | ERROR | The prereg-002 PASS's cited raw artifact is contradicted on disk: `results/validation.json` contains the prereg-001-era FAIL (seeds 11…65537, `verdict=FAIL`, instrument `ad02cb57…`), with mtime 2026-06-21 12:14 **predating the prereg-002 seal commit** (573cfcb, 2026-06-22 12:20). No file in the working copy contains the PASS raw output or any virgin-band seed. The published PASS is backed today solely by the committed transcription (fee12d5). | `docs/preregistration_002_result.md:11` vs `ls -la results/` + `json.load(results/validation.json)` + `results/validation_provenance_launch.txt` + `git log 573cfcb`/`fee12d5`; grep `2076703` repo-wide |
| 2 | WARN | Timing plausibility gap, unexplained in the repo: 13m14s between seal commit (12:20:06) and PASS record commit (12:33:20), vs 32.5 min measured for the smaller prereg-001 run (80 calls) on this machine; prereg-002 scores ~160 calls (BH+MINK). Innocent explanations exist (faster second machine, git-ignored results not syncing; pre-commit launch with final file content) but none is recorded. | `results/validation_run.log` (32.5 min); `git log --date=iso 573cfcb fee12d5`; `docs/preregistration_002_result.md:29-34` |
| 3 | WARN | Provenance asymmetry: the FAIL run has a full launch snapshot (`results/validation_provenance_launch.txt`: commit, sha, uname, pip freeze, UTC times); the PASS has none — no timestamps, no host, no per-seed log, nowhere. The strongest published result has the weakest provenance chain. | `results/validation_provenance_launch.txt` vs `docs/preregistration_002_result.md` (no provenance block) |
| 4 | OK | Seal intact and matches the binding record; live instrument = prereg-002 instrument. | `make verify-seal` → `6e2c3888…` = `docs/preregistration_002.md:8` |
| 5 | OK | No dev/validation seed leak: no virgin-band seed appears in any dev script, log, or artifact; disjointness asserted in the sealed file. | grep `2076703` / band patterns; `thresholds.py:76-79` |
| 6 | OK | Claim boundary respected; FAIL and PASS reported alike; non-primary fp caveat recorded transparently. | `docs/preregistration_002_result.md:47-64`; `docs/preregistration_001_result.md` |
| 7 | OK | Mechanical audit clean (0 errors, 0 warnings); prereg-001 FAIL artifacts fully corroborate the published FAIL. | `bash .claude/skills/auditor/audit.sh` (exit 0); `results/validation.json` vs prereg-001 record |

AUDIT_ERRORS=1
AUDIT_WARNINGS=2

## 8. Verdict

AUDIT_VERDICT=AUDIT_FAIL

**What this verdict does and does not say.** It does NOT say the PASS is fabricated: the
generator is committed, deterministic, and seeded; the transcription may well be the faithful
output of a run on another machine whose git-ignored raw output never reached this working copy.
It DOES say that, as of this audit, the published PASS fails the project's own first founding
rule at the artifact level: its cited backing (`results/validation.json`) is contradicted by the
file at that path, and no live artifact anywhere in this working copy can corroborate the
transcription. Remediation is the user's call; the auditor recommends (a) recovering the original
raw `validation.json` + run log + provenance from whatever machine executed the PASS run and
archiving them (e.g. `results/prereg002/` or a committed provenance note recording host and
timestamps), and (b) renaming or archiving the prereg-001-era files so the stale pointer cannot
mislead again; failing (a), the honest label for the PASS's raw backing is `[UNVERIFIED]` in any
document that builds on it, until a committee adjudicates whether a supervised, explicitly
authorised re-verification run (same sealed instrument, same frozen seeds, outcome reported
alike) is compatible with the "first and only evaluation" rule.
