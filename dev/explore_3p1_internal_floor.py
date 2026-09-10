"""EXPLORATION (dev/) — Paper III, Phase 1: INTERNAL RESOLUTION FLOOR of the
interval leg, measured on a combinatorial quantity whose N-dependence is known
exactly.

WHY THIS EXISTS. The 17-replicate run left beta = 0.2604 against an asymptotic
1/4, a shift of +0.0105 that was compared against a floor of 0.0179 imported from
the BOX leg. The interval leg had no exactly-known calibrator of its own, because
N is fixed and rho * Vol = N by construction. This script supplies one.

THE CALIBRATOR. The average abundance of k-chains in a causal set sprinkled into
an Alexandrov interval of n-dimensional Minkowski space. Primary source:
"Discrete geometry of a small causal diamond" (Roy, Sinha, Surya), sec. 2,
reproducing Meyer; local copy at
biblioteca/derived-md/Discrete geometry of a small causal diamond.md.
Eq. (9) of that paper gives

    chi_k = (1/k) (Gamma(n+1)/2)^(k-1) Gamma(n/2)Gamma(n)
                  / (Gamma(kn/2) Gamma((k+1)n/2))

and eq. (8) gives <C_k> = chi_k (rho V_0)^k for a POISSON sprinkling.

ENSEMBLE. Our leg is BINOMIAL: exactly N i.i.d. uniform points (contract sec.
1.4, R003). chi_k is a volume fraction — it is P(x_1 < x_2 < ... < x_k) for k
i.i.d. uniform points — so it does not depend on the ensemble; only the counting
does. A given k-subset forms a chain in exactly one of its k! orderings, so

    E[C_k] = C(N,k) * k! * chi_k = N(N-1)...(N-k+1) * chi_k

with a FALLING FACTORIAL where the Poisson form has N^k. That law is EXACT at
every finite N: it carries no finite-size correction at all. That is what makes
it a floor and not another unknown.

THIS IS A CONTROL, NOT AN OBSERVABLE. C_k is not promoted, not interpreted, and
not part of any Paper III claim. It exists to measure what our own pipeline does
to a quantity whose answer is already known.

SAME CAUSAL SETS. The posets of the 17-replicate run are not stored, only their
Ls. This script regenerates them deterministically by importing the very sprinkler
that produced them, and re-derives L with the committed chain routine so the
identity can be checked seed by seed against the committed artifact.

Run:  python3 dev/explore_3p1_internal_floor.py
NOT on the validation path. Does not touch nachocausal/.
"""

from __future__ import annotations

import json
import time
from math import gamma

import numpy as np

from explore_3p1_bg_reference import (PRECISION17_SEEDS, PRECISION_NS,
                                      longest_chain_endpoint_to_endpoint,
                                      sprinkle_interval_4d)

DIM = 4                     # 3+1
KS = (2, 3, 4)              # the k we can count exactly and cheaply
OUT = "dev/explore_3p1_internal_floor_results.json"
BLOCK = 64


def chi(k: int, n: int = DIM) -> float:
    """Roy-Sinha-Surya eq. (9), verbatim. chi_1 = 1; chi_2 = 1/20 at n = 4."""
    return (1.0 / k) * (gamma(n + 1) / 2.0) ** (k - 1) * gamma(n / 2) * gamma(n) \
        / (gamma(k * n / 2) * gamma((k + 1) * n / 2))


def falling(N: int, k: int) -> float:
    out = 1.0
    for i in range(k):
        out *= (N - i)
    return out


def expected_Ck(N: int, k: int) -> float:
    """EXACT binomial expectation. No finite-size correction."""
    return chi(k) * falling(N, k)


def count_chains(pts: np.ndarray) -> tuple[int, int, int]:
    """C_2, C_3, C_4 of the sprinkled points, exactly.

    The causal relation is the one the committed chain routine uses: sort by t,
    then i < j is a relation iff dt^2 >= |dx|^2. Counting is blocked so the N x N
    relation matrix is never materialised (it would be 1 GB at N = 32000).

        C_2 = number of relations
        C_3 = sum_j indeg(j) * outdeg(j)          (i < j < k)
        C_4 = sum over relations j < k of indeg(j) * outdeg(k)
    """
    order = np.argsort(pts[:, 0], kind="stable")
    p = pts[order]
    n = p.shape[0]
    t = np.ascontiguousarray(p[:, 0])
    x = np.ascontiguousarray(p[:, 1:])

    def block_rel(a: int, b: int) -> np.ndarray:
        """Relation matrix of rows [a, b) against all columns, computed with the
        SAME arithmetic as the committed chain routine: a literal coordinate
        difference, squared and summed. An algebraically equivalent Gram-matrix
        expansion is faster but not bit-identical near the light cone, and this
        control exists to reproduce that routine's causal set, not to be quick."""
        dt = t[None, :] - t[a:b, None]
        d2 = ((x[None, :, :] - x[a:b, None, :]) ** 2).sum(2)
        return (dt > 0) & (dt * dt >= d2)

    indeg = np.zeros(n, dtype=np.int64)
    outdeg = np.zeros(n, dtype=np.int64)
    for a in range(0, n, BLOCK):
        b = min(a + BLOCK, n)
        rel = block_rel(a, b)
        outdeg[a:b] += rel.sum(1)
        indeg += rel.sum(0)
    C2 = int(outdeg.sum())
    C3 = int((indeg * outdeg).sum())

    # C_4 needs indeg/outdeg complete, so it is a second pass. int64 is safe:
    # the largest term is bounded by N^2 <= 1.1e9 and the sum by C_2 * N^2, which
    # is ~5e16 at N = 32000, well inside int64.
    C4 = 0
    for a in range(0, n, BLOCK):
        b = min(a + BLOCK, n)
        i, j = np.nonzero(block_rel(a, b))
        C4 += int((indeg[i + a] * outdeg[j]).sum())
    return C2, C3, C4


def main() -> int:
    tau = 1.0
    t_start = time.time()
    rows = []
    for N in PRECISION_NS:
        per = {"N": N, "n_seeds": len(PRECISION17_SEEDS), "L": [],
               "C2": [], "C3": [], "C4": []}
        for s in PRECISION17_SEEDS:
            pts = sprinkle_interval_4d(s, N, tau)
            per["L"].append(int(longest_chain_endpoint_to_endpoint(pts, tau)))
            c2, c3, c4 = count_chains(pts)
            per["C2"].append(c2)
            per["C3"].append(c3)
            per["C4"].append(c4)
        for k in KS:
            a = np.asarray(per[f"C{k}"], dtype=float)
            per[f"mean_C{k}"] = float(a.mean())
            per[f"sd_C{k}"] = float(a.std(ddof=1))
            per[f"exact_C{k}"] = expected_Ck(N, k)
            per[f"ratio_C{k}"] = float(a.mean()) / expected_Ck(N, k)
        rows.append(per)
        print(f"N={N:6d}  " + "  ".join(
            f"C{k}: {per[f'mean_C{k}']:.6g} / {per[f'exact_C{k}']:.6g} "
            f"= {per[f'ratio_C{k}']:.6f}" for k in KS), flush=True)

    payload = {
        "role": "INTERNAL_CALIBRATION_CONTROL",
        "not_an_observable": True,
        "tau": tau,
        "dim": DIM,
        "ensemble": "binomial (exactly N i.i.d. uniform points)",
        "seeds": list(PRECISION17_SEEDS),
        "Ns": list(PRECISION_NS),
        "ks": list(KS),
        "chi_k": {str(k): chi(k) for k in KS},
        "exact_law": "E[C_k] = chi_k * N(N-1)...(N-k+1)   (exact at every finite N)",
        "source": ("Roy, Sinha, Surya, 'Discrete geometry of a small causal "
                   "diamond', sec. 2 eq. (8)-(9), reproducing Meyer; local copy "
                   "biblioteca/derived-md/Discrete geometry of a small causal diamond.md"),
        "rows": rows,
        "runtime_s": round(time.time() - t_start, 2),
    }
    with open(OUT, "w") as fh:
        json.dump(payload, fh, indent=2)
    print(f"wrote {OUT}   ({payload['runtime_s']} s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
