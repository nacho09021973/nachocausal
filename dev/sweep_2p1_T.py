"""2+1 phase B: sweep of the box height T at two densities (dev exploration; NO verdict).

Design fixed BEFORE running (2026-10-12): T in {6, 8, 10, 12, 16}; rho in {32, 63} points per
unit 2+1 volume (vol = T * pi * (R_HI^2 - R_LO^2)); seeds 7_000_100..7_000_109 (2+1
exploration band) for every cell.  One subprocess per (T, rho, seed) because T is a module
constant of the generator (env NC2P1_T_EDGE).  Appends one JSON line per realisation.
Usage: .venv/bin/python dev/sweep_2p1_T.py OUT.jsonl
"""
import json
import math
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
T_LIST = (6.0, 8.0, 10.0, 12.0, 16.0)
# Plateau confirmation, declared after the first pass and BEFORE any T = 20 result: the
# inherited t_min rule (docs/estimator_v2_decision_spec.md, Decision 2) needs stability on
# [t_min, 2 t_min], and the first pass gives t_min = 10 at rho = 63, so T = 20 is required.
T_LIST = T_LIST + (20.0,)
RHO_LIST = (32.0, 63.0)
SEEDS = range(7_000_100, 7_000_110)
VOL_PER_T = math.pi * (1.3 ** 2 - 0.1 ** 2)


def main():
    out = Path(sys.argv[1])
    done = set()
    if out.exists():
        for l in out.read_text().splitlines():
            d = json.loads(l); done.add((d["T_EDGE"], d["rho"], d["seed"]))
    for rho in RHO_LIST:
        for T in T_LIST:
            n_mean = int(round(rho * T * VOL_PER_T))
            for seed in SEEDS:
                if (T, rho, seed) in done:
                    continue
                env = dict(os.environ, NC2P1_T_EDGE=str(T))
                res = subprocess.run([sys.executable, str(ROOT / "dev" / "explore_2p1_estimator.py"),
                                      str(n_mean), str(seed)], env=env, capture_output=True, text=True)
                line = [l for l in res.stdout.splitlines() if l.startswith("{")]
                if res.returncode != 0 or not line:
                    rec = {"T_EDGE": T, "rho": rho, "seed": seed, "error": res.stderr[-500:]}
                else:
                    rec = json.loads(line[-1]); rec.update({"T_EDGE": T, "rho": rho, "n_mean": n_mean})
                with out.open("a") as fh:
                    fh.write(json.dumps(rec) + "\n")
                print(T, rho, seed, "ok" if "error" not in rec else "ERROR", flush=True)


if __name__ == "__main__":
    main()
