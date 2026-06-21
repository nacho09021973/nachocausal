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

**Verdict: `FAIL`.** Executed 2026-06-21 — the single committed `validate.run()`
over the 20 frozen `VALIDATION_SEEDS` (`label="validation"`, `guard=True`, no
`seeds=`, no `guard=False`). Transcribed verbatim from `results/validation.json`.

Three of five checks held; **two were unmet at the primary N (intensity 12000):**
(ii) localisation and (iv) false-positive. Significance was strong at every level.

### Four-level table (per intensity, from `results/validation.json`)

| intensity | N_mean | n_valid | p_perm | sig | med w/2M | IQR/2M | θ_loc | coverage | r_std | θ_stab | fp_frac | status |
|---:|---:|---:|---:|:-:|---:|---:|---:|---:|---:|---:|---:|:-:|
| 1500  | 1514.4   | 20 | 3.81e-06 | ✓ | 0.1662 | 0.1572 | 0.2771 | 0.65 | 0.0232 | 0.1386 | 0.10 | scored |
| 3000  | 3020.3   | 20 | 9.54e-07 | ✓ | 0.1036 | 0.1063 | 0.1960 | 0.60 | 0.0214 | 0.0980 | 0.10 | scored |
| 6000  | 6028.8   | 20 | 9.54e-07 | ✓ | 0.0845 | 0.0499 | 0.1386 | 0.40 | 0.0161 | 0.0693 | 0.10 | scored |
| **12000** (primary) | 12040.75 | 20 | 9.54e-07 | ✓ | 0.0586 | 0.0466 | 0.0980 | **0.30** | 0.0131 | 0.0490 | **0.10** | scored |

### Five checks (primary N = intensity 12000)

| check | value |
|---|:-:|
| (i) significant at primary and every N≥3000 | **True** |
| (ii) localisation at primary (width ≤ θ_loc, not IQR-inconclusive, coverage ≥ 0.5) | **False** |
| (ii) convergence-slack (b) | True |
| (iii) stability at primary (boundary r-std ≤ θ_stab) | True |
| (iv) false-positive at primary (LOO fp ≤ 0.05) | **False** |
| (v) Guard-v raised on no causet (order-only) | True |

**Why FAIL (factual):**
- **(ii) localisation** — the bracket *width* passed (median 0.0586 ≤ θ_loc 0.0980),
  but **coverage of the true `R_S` was 0.30 < 0.50** required. The order-statistic
  bracket (`r_lo = max r` over predicted-interior, `r_hi = min r` over
  predicted-exterior; `scorer.py:53-54`) is narrow but off-centre: a single
  misclassified minimal element near the boundary breaks coverage. Coverage falls
  monotonically with N (0.65 → 0.60 → 0.40 → 0.30).
- **(iv) false-positive** — LOO false-positive fraction = **0.10 > 0.05** at every
  level. `two_means_split` always splits the O multiset, so pure-Minkowski seeds
  get a spurious `sep`; the tail produces false positives.

The causal order *does* carry horizon signal (sign-flip significance p ≈ 1e-6 at
all four N), but the frozen v1 estimator does **not** recover the Schwarzschild
horizon at the pre-registered fidelity. This is recorded as the outcome of
pre-registration 001; it is **not** licence to re-run or re-tune (binding rule
above). Any re-validation of an improved estimator requires a **new
pre-registration (002)** with a newly sealed estimator and **fresh held-out
seeds disjoint from `DEV_SEEDS` and from these now-burned `VALIDATION_SEEDS`**;
the frozen thresholds and primary endpoint do not move.

### Launch-time provenance snapshot (actual run)

- commit: `672eb1424feee580c628753b7ab5b6b76aa982c4` (`672eb14`, branch `main`)
- package diff (`nachocausal/`, `docs/`): 0 lines
- `thresholds.py` SHA256: `ad02cb57e1445ca83a489bd4f3f9cae151517ca2aedbd1b29c44c60ac65f7faa`
- env: `Linux 6.6.87.2-microsoft-standard-WSL2 x86_64`; Python 3.12.3; numpy 1.26.4
- pip freeze (sealed venv): numpy==1.26.4, pytest==8.4.2, pluggy==1.6.0,
  iniconfig==2.3.0, packaging==26.2, Pygments==2.20.0
- captured_utc 2026-06-21T09:05:58Z; tests 10 passed (sealed venv)
- run: verdict written to `results/validation.json` at completion (32.5 min, CPU)
- launcher note: the run was driven via `dev/run_validation_instrumented.py`, a
  non-sealed dev wrapper that adds a **pass-through** progress timer around
  `validate._per_seed` (calls the original, returns its result unchanged) and
  invokes the unmodified `validate.run()`; numerically identical to
  `python -m nachocausal.validate`. Full provenance trail in
  `results/validation_provenance_launch.txt`.
