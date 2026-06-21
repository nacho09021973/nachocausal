# Pre-registration 001 — Result record (step #5, blind validation)

Status: **PROCEDURE PRE-COMMITTED — RESULT PENDING.** This file is committed
*before* the blind validation run (step #5) is executed, fixing the run command,
the environment, the seed set, the binding reporting rule, and the destination of
the verdict. The "Result" section below is intentionally blank until the single
committed run completes. It is filled in **once**, with whatever the run emits.

This realises `docs/preregistration.md:59-67` (frozen protocol) and the sealed
instrument of `docs/preregistration_001_addendum.md`.

## Binding reporting rule (pre-committed)

- **One run, one verdict.** `validate.run()` is invoked exactly once over
  `thresholds.VALIDATION_SEEDS`, with `label="validation"`, default `guard=True`,
  no manual `seeds=` and no `guard=False`.
- **All three outcomes are reported identically.** PASS, FAIL, and INCONCLUSIVE
  are transcribed here verbatim. A FAIL or INCONCLUSIVE is **not** a licence to
  re-run on other seeds, loosen a threshold, or re-interpret a secondary N as the
  primary endpoint (`preregistration.md:55-57`; addendum PASS/FAIL rule). The
  validation seeds cannot be un-seen; this run is scientifically one-way.
- **No post-hoc anything.** The thresholds, boundary definition, geometry,
  ensemble, primary endpoint (intensity 12000), and seed set are those frozen in
  the addendum. Nothing below is decided after seeing validation data.

## Run command (pre-committed)

Executed only in the sealed CPU environment (`assert_environment()` hard-fails
otherwise), in the background (several hours; CPU only — **never** the GPU venv,
whose float `log` in the BH matrix build is not guaranteed bit-exact):

```bash
cd /home/adnac/nachocausal
nohup .venv/bin/python -m nachocausal.validate > results/validation_run.log 2>&1 &
```

`validate.run()` writes the machine verdict to `results/validation.json`
(git-ignored). After completion the verdict + the full 4-level table is
transcribed into the "Result" section here (committed).

### Launcher correction (2026-06-21, BEFORE any validation data was seen)

On the first launch attempt the committed command `python -m nachocausal.validate`
exited 0 in seconds and produced an **empty** `results/validation_run.log` and **no**
`results/validation.json`: at the time of pre-commit, `nachocausal/validate.py` had
**no `if __name__ == "__main__":` block** (and there is no `nachocausal/__main__.py`),
so `-m` merely imported the module and exited — a silent no-op. Fix (commit on
`main`): a `__main__` block was added to `validate.py` that calls `run()` with the
frozen defaults (no `seeds=`, `guard=True`, `label="validation"`) and prints the
verdict. This is a launcher-only change: **`thresholds.py` is untouched, the seal
SHA256 is unchanged, and no validation seed had been analysed** (empty log, no
verdict file) — it is not post-hoc tuning of any frozen quantity. The run command
above is unchanged and now executes the single committed run.

## Pre-flight gate (must be green before launch)

| Check | Command | Required |
|---|---|---|
| Seal intact | `make verify-seal` | SHA256 = `ad02cb57e1445ca83a489bd4f3f9cae151517ca2aedbd1b29c44c60ac65f7faa` |
| Package unmodified | `git status --porcelain nachocausal/ docs/` | empty |
| Regression + leak + seed guards | `make test` | all pass |
| Sealed path reproduces today | `make dry-run` (DEV seeds, verdict discarded) | completes, behaves as sealed |
| Environment | sealed `.venv` | numpy 1.26.4, Python 3.12.3, CPU |

## Pre-flight provenance snapshot (captured 2026-06-20T16:51:29Z)

- commit: `e6a5dbf931090ee564afeb107579d254b655608e` (`e6a5dbf`, branch `main`)
- package diff (`nachocausal/`, `docs/`): empty
- `thresholds.py` SHA256: `ad02cb57e1445ca83a489bd4f3f9cae151517ca2aedbd1b29c44c60ac65f7faa`
- env: `Linux 6.6.87.2-microsoft-standard-WSL2 x86_64`; Python 3.12.3; numpy 1.26.4
- pip freeze (sealed venv): numpy==1.26.4, pytest==8.4.2, pluggy==1.6.0,
  iniconfig==2.3.0, packaging==26.2, Pygments==2.20.0

(A launch-time snapshot — commit, pip freeze, uname, numpy/python, start/end
timestamps — is re-captured at the moment of the actual run and recorded with the
result.)

## Validation seed set (frozen; addendum line 48)

`11, 23, 57, 88, 137, 271, 314, 577, 911, 1618, 2024, 4099, 5040, 6700, 7777,
8191, 9001, 12289, 27644, 65537` (disjoint from DEV_SEEDS, asserted in code).

## PASS/FAIL rule (frozen; addendum lines 93-101)

PASS iff **ALL** at the primary N (intensity 12000): (i) `p_perm ≤ 1e-4` and
significant at every N≥3000; (ii) median `|dr|/(2M)` ≤ θ_loc, not
IQR-inconclusive, coverage ≥ 0.5, convergence-slack (b) holds; (iii) boundary
r-std ≤ θ_stab; (iv) LOO false-positive fraction ≤ 0.05; (v) Guard-v raised on no
causet. Any unmet → FAIL; primary level with < 18/20 valid seeds → INCONCLUSIVE.

## Result

**PENDING — not yet executed.** To be filled once, from `results/validation.json`,
with the verdict and the full 4-level table (per intensity: N_mean, n_valid,
p_perm, significant, median_width/2M, IQR, coverage, boundary_r_std, fp_fraction,
and the five check booleans), plus the launch-time provenance snapshot.
