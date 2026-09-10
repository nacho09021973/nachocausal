"""EXPLORATION (dev/) — Paper III, Phase I reference leg.

Separates the two things that the L ~ V^{1/4} claim conflates:

  (A) the KNOWN Brightwell-Gregory law, which holds inside an ALEXANDROV
      INTERVAL:  L / (rho * Vol)^{1/d} -> m_d  (d = 4 here);
  (B) the box-TRUNCATED future |J^+(i) cap D|, which is not an interval, so
      the BG constant does not apply and L^4 / V is a SHAPE functional.

Leg (A) is the calibration anchor: if our chain code reproduces m_4 inside
intervals, then any departure measured in leg (B) is geometry, not a bug.

NOT on the validation path. Does not touch nachocausal/.
"""

from __future__ import annotations

import json
import sys

import numpy as np

DIAMOND_VOL_COEFF = np.pi / 24.0  # 4D Alexandrov interval: V = (pi/24) tau^4


def sprinkle_interval_4d(seed: int, n_target: int, tau: float = 1.0) -> np.ndarray:
    """Uniform in the causal diamond between (0,0,0,0) and (tau,0,0,0),
    by rejection from the bounding box. Endpoints are NOT included."""
    rng = np.random.default_rng(seed)
    out = []
    got = 0
    while got < n_target:
        m = int((n_target - got) / DIAMOND_VOL_COEFF * 1.4) + 64
        t = rng.random(m) * tau
        x = (rng.random((m, 3)) - 0.5) * tau
        rad = np.linalg.norm(x, axis=1)
        keep = (rad <= t) & (rad <= tau - t)  # inside J^+(p) and J^-(q)
        pts = np.column_stack([t[keep], x[keep]])
        out.append(pts)
        got += pts.shape[0]
    return np.vstack(out)[:n_target]


def longest_chain_endpoint_to_endpoint(pts: np.ndarray, tau: float) -> int:
    """Longest chain from (0,0,0,0) to (tau,0,0,0) through the sprinkled
    points. Returned as the number of INTERIOR elements on the chain, which is
    the quantity BG normalises by N^{1/d}."""
    order = np.argsort(pts[:, 0], kind="stable")
    p = pts[order]
    n = p.shape[0]
    t = p[:, 0]
    x = p[:, 1:]
    best = np.ones(n, dtype=np.int64)  # every point is reachable from p and reaches q
    block = 512
    for a in range(n - 1, -1, -block):
        b = max(a - block + 1, 0)
        idx = np.arange(b, a + 1)
        for i in idx[::-1]:
            dt = t[i + 1 :] - t[i]
            if dt.size == 0:
                continue
            d2 = np.sum((x[i + 1 :] - x[i]) ** 2, axis=1)
            succ = dt * dt >= d2
            if succ.any():
                best[i] = 1 + int(best[i + 1 :][succ].max())
    return int(best.max()) if n else 0


def main() -> int:
    tau = 1.0
    rows = []
    for n_target in (500, 1000, 2000, 4000, 8000, 16000):
        Ls = []
        for seed in (21, 22, 23):
            pts = sprinkle_interval_4d(seed, n_target, tau)
            Ls.append(longest_chain_endpoint_to_endpoint(pts, tau))
        L = float(np.mean(Ls))
        m4 = L / n_target**0.25
        rows.append({"N": n_target, "mean_L": L, "L_over_N_quarter": m4, "Ls": Ls})
        print(f"N={n_target:6d}  <L>={L:8.2f}  L/N^(1/4)={m4:6.4f}", flush=True)

    Ns = [r["N"] for r in rows]
    Ls = [r["mean_L"] for r in rows]
    slope = float(np.polyfit(np.log(Ns), np.log(Ls), 1)[0])
    print(f"\nd log <L> / d log N = {slope:.4f}   (BG expects 1/4)")
    print("local slopes:", [
        round(float(np.log(Ls[i + 1] / Ls[i]) / np.log(Ns[i + 1] / Ns[i])), 4)
        for i in range(len(Ns) - 1)
    ])
    with open("dev/explore_3p1_bg_reference_results.json", "w") as fh:
        json.dump({"tau": tau, "rows": rows, "global_slope": slope}, fh, indent=2)
    print("wrote dev/explore_3p1_bg_reference_results.json")
    return 0


# ---------------------------------------------------------------------------
# Precision leg. Same code path as main(), more seeds and one N decade further.
# Deterministic: seeds 101..108 fixed. Persisted so that the table in
# dev/PAPER3_3P1_SCALE_NOTES.md sec. 3.1 has a machine-readable backing.
#
# REPLICATION EXTENSION (PI decision, 2026-09-10). Phase 1 found that what limits
# this design is the REPLICA COUNT, not the range of N: with 8 integer-valued
# replicas the N=8000 point carries 71.7% of the constant-model chi2 purely
# because six of its eight replicas coincide. The extension therefore adds nine
# seeds at the SAME four N and changes nothing else -- same sprinkler, same chain
# routine, same normalisation, same tau, same binomial process, same observable.
#
# The two runs are separate artifacts with separate identities. The 8-seed one is
# historical and is never overwritten: it backs sec. 3.1 of the notes through
# dev/verify_3p1_notes_figures.py. This is the same NEW_VERSIONED_ARTIFACT policy
# the box leg already follows for its pre-R001 / R001 lineages.
#
# Seeds 109..117 continue the existing block contiguously. They were fixed by
# that rule alone, before any of them was run, and are disjoint from every other
# seed list in Paper III: box leg (11,12,13), interval base leg (21,22,23),
# precision leg (101..108), point-process audit (101,102,103 and 999).
# ---------------------------------------------------------------------------
PRECISION_NS = (2000, 8000, 16000, 32000)
PRECISION_SEEDS = tuple(range(101, 109))
PRECISION_OUT = "dev/explore_3p1_bg_reference_precision_results.json"

PRECISION17_SEEDS = tuple(range(101, 118))  # 101..108 historical + 109..117 added
PRECISION17_OUT = "dev/explore_3p1_bg_reference_precision17_results.json"


def main_precision(seeds: tuple = PRECISION_SEEDS, out: str = PRECISION_OUT) -> int:
    """Default arguments reproduce the historical 8-seed artifact byte for byte.

    Seeds are consumed in the order given and each seed's chain is independent of
    every other, so the first len(PRECISION_SEEDS) entries of the 17-seed run are
    the 8-seed run's entries, value for value. That identity is what certifies
    the extension did not perturb the design, and it is checked in section [A3]
    of dev/verify_3p1_phase0_contract.py.
    """
    tau = 1.0
    rows = []
    for n_target in PRECISION_NS:
        Ls = [
            longest_chain_endpoint_to_endpoint(sprinkle_interval_4d(s, n_target, tau), tau)
            for s in seeds
        ]
        a = np.asarray(Ls, dtype=float)
        sem = float(a.std(ddof=1) / np.sqrt(a.size))
        rows.append(
            {
                "N": n_target,
                "n_seeds": len(seeds),
                "mean_L": float(a.mean()),
                "sem_L": sem,
                "L_over_N_quarter": float(a.mean()) / n_target**0.25,
                "Ls": [int(v) for v in Ls],
            }
        )
        print(
            f"N={n_target:6d}  <L>={a.mean():7.3f} +/- {sem:.3f}  "
            f"L/N^(1/4)={a.mean() / n_target**0.25:.4f}",
            flush=True,
        )
    Ns = [r["N"] for r in rows]
    Ls = [r["mean_L"] for r in rows]
    local = [
        float(np.log(Ls[i + 1] / Ls[i]) / np.log(Ns[i + 1] / Ns[i]))
        for i in range(len(Ns) - 1)
    ]
    print("local slopes:", [round(v, 4) for v in local])
    with open(out, "w") as fh:
        json.dump(
            {"tau": tau, "seeds": list(seeds), "rows": rows,
             "local_slopes": local}, fh, indent=2)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--precision":
        sys.exit(main_precision())
    if len(sys.argv) > 1 and sys.argv[1] == "--precision17":
        sys.exit(main_precision(PRECISION17_SEEDS, PRECISION17_OUT))
    sys.exit(main())
