"""dev launcher — runs the SEALED blind validation with a live progress line.

NOT part of the sealed package (dev/ is untracked). It does NOT change any
number: it monkey-patches validate._per_seed with a PASS-THROUGH wrapper that
calls the original, returns its result untouched, and only prints timing. The
verdict comes from the unmodified validate.run() -> results/validation.json,
identical to `python -m nachocausal.validate`.

Run with the SEALED venv only:  .venv/bin/python dev/run_validation_instrumented.py
"""

from __future__ import annotations

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal import validate, thresholds  # noqa: E402

# Measured per-(seed,intensity) cost (sealed venv, this machine) — for ETA only;
# never touches results.
_LEVEL_SECS = {1500.0: 1.1, 3000.0: 4.3, 6000.0: 18.1, 12000.0: 75.7}

_orig_per_seed = validate._per_seed
_seeds = list(thresholds.VALIDATION_SEEDS)
_TOTAL = len(_seeds) * len(thresholds.INTENSITIES)
# run() iterates intensity-major (all seeds at 1500, then 3000, ...): build the
# expected order so ETA reflects the cheap->expensive ramp.
_expected_remaining = [_LEVEL_SECS[lam] for lam in thresholds.INTENSITIES for _ in _seeds]
_state = {"n": 0, "t_start": time.perf_counter()}


def _timed_per_seed(seed, intensity, guard=True):
    t0 = time.perf_counter()
    out = _orig_per_seed(seed, intensity, guard)  # original, result untouched
    dt = time.perf_counter() - t0
    i = _state["n"]
    _state["n"] = i + 1
    elapsed = time.perf_counter() - _state["t_start"]
    eta = sum(_expected_remaining[i + 1:])
    print(
        f"[{i+1:>2}/{_TOTAL}] intensidad={intensity:>7.0f} seed={seed:>5} "
        f"N={out['N']:>6}  dt={dt:5.1f}s  elapsed={elapsed/60:5.1f}min  "
        f"ETA~{eta/60:4.1f}min",
        flush=True,
    )
    return out


validate._per_seed = _timed_per_seed

if __name__ == "__main__":
    print(
        f"== blind validation (instrumented launcher) ==\n"
        f"seeds={len(_seeds)}  intensities={list(thresholds.INTENSITIES)}  "
        f"total _per_seed calls={_TOTAL}\n"
        f"verdict will be written to results/validation.json (unmodified validate.run)\n",
        flush=True,
    )
    verdict = validate.run()  # write=True -> results/validation.json
    total = time.perf_counter() - _state["t_start"]
    print(f"\n== DONE in {total/60:.1f} min ==", flush=True)
    print(f"verdict: {verdict.get('verdict')}", flush=True)
    print(f"checks: {verdict.get('checks', verdict.get('reason'))}", flush=True)
    print(f"written: {os.path.join(validate.RESULTS_DIR, verdict['label'] + '.json')}", flush=True)
