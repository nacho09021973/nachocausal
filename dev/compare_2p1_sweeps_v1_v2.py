"""Compare the T sweep before (v1, CPU with possibly stale numba-cached tables) and after
(v2, GPU / fixed tables), seed by seed.  Same clouds: they depend only on (T, seed).
Usage: python dev/compare_2p1_sweeps_v1_v2.py v1.jsonl v2.jsonl
"""
import collections
import json
import sys

def load(p):
    return {(d["rho"], d["T_EDGE"], d["seed"]): d for d in map(json.loads, open(p)) if "error" not in d}

v1, v2 = load(sys.argv[1]), load(sys.argv[2])
cells = collections.defaultdict(lambda: collections.Counter())
for k in sorted(set(v1) & set(v2)):
    a, b = v1[k]["BH"], v2[k]["BH"]
    c = cells[k[:2]]
    c["n"] += 1
    c["same_n"] += v1[k]["n"] == v2[k]["n"]
    c["same_O_quartiles"] += a["O_quartiles"] == b["O_quartiles"]
    c["same_bracket"] += (a.get("r_lo"), a.get("r_hi")) == (b.get("r_lo"), b.get("r_hi"))
    c["same_cover"] += a.get("covers_2M") == b.get("covers_2M")
    c["same_mink_abstain"] += v1[k]["MINK"]["abstain"] == v2[k]["MINK"]["abstain"]
for (rho, T), c in sorted(cells.items()):
    print(f"rho={rho:g} T={T:g}: {c['n']} seeds | same N {c['same_n']} | same O quartiles "
          f"{c['same_O_quartiles']} | same bracket {c['same_bracket']} | same cover {c['same_cover']}"
          f" | same MINK gate {c['same_mink_abstain']}")
