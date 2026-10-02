"""PUENTE-3P1 / B1.5 — refinement audit of the analytic separation.

Every choice of the proof parameters (K, L, cell counts) yields a *valid* pair of
bounds, so the certificate cannot be manufactured by tuning them.  What tuning
could hide is a bound that only separates at one lucky setting.  This audit
re-runs the chain across a ladder of settings and records whether U0 stays below
L1 throughout, and whether both bounds move monotonically towards the B1.4
numerical bands as the partition refines.

Deterministic: no seeds, no Monte Carlo, no search over lambda.
"""
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b15", os.path.join(HERE, "verify_b1_5_analytic_separation.py"))
b15 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b15)

LADDER = [(6, 6, 160, 60), (8, 8, 240, 80), (12, 12, 320, 120),
          (16, 16, 480, 160), (20, 20, 600, 200)]


def main():
    rows = []
    for K, L, nu, nv in LADDER:
        b15.K_ANCHORS, b15.L_CELLS = K, L
        b15.N_CELLS_U, b15.N_CELLS_V = nu, nv
        u0 = b15.rho_upper(b15.LAMBDA0)
        l1 = b15.rho_lower(b15.LAMBDA1)
        rows.append({"K": K, "L": L, "N_cells_U": nu, "N_cells_V": nv,
                     "U0": u0, "L1": l1, "gap": l1 - u0,
                     "relative_margin": (l1 - u0) / u0,
                     "separated": bool(u0 < l1)})
        print(f"K={K:<3d}L={L:<3d}nU={nu:<4d}nV={nv:<4d} "
              f"U0={u0:.6f} L1={l1:.6f} gap={l1-u0:+.6f} "
              f"{'SEPARATED' if u0 < l1 else 'not separated'}")
    u0s = [r["U0"] for r in rows]
    l1s = [r["L1"] for r in rows]
    sep = [r["separated"] for r in rows]
    first = next((i for i, s in enumerate(sep) if s), None)
    # A coarse setting that fails to separate is not a contradiction: its bounds
    # are valid, merely too weak.  What would discredit the chain is a REVERSAL,
    # i.e. separation at one setting and none at a strictly finer one.
    no_reversal = first is not None and all(sep[first:])
    mono = (all(a >= b for a, b in zip(u0s, u0s[1:]))
            and all(a <= b for a, b in zip(l1s, l1s[1:])))
    out = {
        "unit": "PUENTE-3P1/B1.5-refinement",
        "ladder": rows,
        "coarsest_setting_that_separates": (rows[first]["K"], rows[first]["L"],
                                            rows[first]["N_cells_U"],
                                            rows[first]["N_cells_V"]) if first is not None else None,
        "no_reversal_after_threshold": bool(no_reversal),
        "separated_at_finest": rows[-1]["separated"],
        "U0_decreasing_under_refinement": all(a >= b for a, b in zip(u0s, u0s[1:])),
        "L1_increasing_under_refinement": all(a <= b for a, b in zip(l1s, l1s[1:])),
        "U0_stays_above_true_rho0_band_low": all(u > 0.012756190222626588 for u in u0s),
        "L1_stays_below_true_rho1_band_high": all(v < 0.04383499708576354 for v in l1s),
        "no_seeds": True, "no_monte_carlo": True, "no_search": True,
        "terminal": ("B1.5_REFINEMENT_MONOTONE_NO_REVERSAL" if (no_reversal and mono)
                     else "B1.5_REFINEMENT_UNSTABLE"),
    }
    print(json.dumps({k: v for k, v in out.items() if k != "ladder"}, indent=2))
    with open(os.path.join(HERE, "verification_b1_5_refinement_audit.json"), "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
