"""PUENTE-3P1 / B2 — path frozen before rho evaluation.

Uses the deterministic B1.4 interval routine. No path search, lambda tuning, seeds, or Monte Carlo.
"""
import json
import math
import sys
from pathlib import Path
from scipy.integrate import quad
from scipy.special import lambertw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "B1"))
from verify_certified_rho_frozen_pair import rho_bounds  # noqa: E402

LAMBDA0 = (0.5, 1.0, 1.0, 0.5, 0.1)
LAMBDA1 = (0.2, 0.8, 2.0, 0.9, 0.1)
T0 = 0.5
H = 0.1


def path(t):
    return tuple((1.0 - t) * a + t * b for a, b in zip(LAMBDA0, LAMBDA1))


def invariants(lam):
    v0, v1, uout, uin, _ = lam
    return (v1 / v0, uin / uout, uin * v1)


def phi(lam):
    v0, v1, uout, uin, _ = lam
    s = lambda uv: (1.0 + lambertw(-uv / math.e, 0).real)
    fin = quad(lambda V: (1.0 - s(uin * V) ** 3) / V, v0, v1,
               epsabs=1e-12, epsrel=1e-12)[0] / 3.0
    fout = quad(lambda V: (s(-uout * V) ** 3 - 1.0) / V, v0, v1,
                epsabs=1e-12, epsrel=1e-12)[0] / 3.0
    return fin / (fin + fout)


def main():
    # The path and t0 are frozen first. Geometry is evaluated next; rho comes last.
    samples = [T0 - H, T0, T0 + H]
    lambdas = [path(t) for t in samples]
    pre = [{"t": t, "lambda": list(lam), "invariants": invariants(lam), "phi": phi(lam)}
           for t, lam in zip(samples, lambdas)]
    dphi = (pre[2]["phi"] - pre[0]["phi"]) / (2.0 * H)
    rho_rows = []
    for t, lam in zip(samples, lambdas):
        lo, hi, z = rho_bounds(lam, 14)
        rho_rows.append({"t": t, "lambda": list(lam), "rho_lower": lo,
                         "rho_upper": hi, "normalization_Z": z})

    # A derivative can be certified from bands only if all endpoint combinations have one sign.
    d_rho_min = (rho_rows[2]["rho_lower"] - rho_rows[1]["rho_upper"]) / H
    d_rho_max = (rho_rows[2]["rho_upper"] - rho_rows[1]["rho_lower"]) / H
    positive = dphi != 0.0 and (d_rho_min > 0.0 or d_rho_max < 0.0)
    null = (rho_rows[0]["rho_lower"] == rho_rows[0]["rho_upper"] ==
            rho_rows[1]["rho_lower"] == rho_rows[1]["rho_upper"] ==
            rho_rows[2]["rho_lower"] == rho_rows[2]["rho_upper"])
    out = {
        "unit": "PUENTE-3P1/B2",
        "path_frozen_before_rho": True,
        "path": "lambda(t)=(1-t)*lambda0+t*lambda1",
        "t0": T0, "finite_difference_half_width": H,
        "pre_rho_geometry": pre, "dphi_dt_central": dphi,
        "rho_bands": rho_rows,
        "drho_dt_certified_interval": [d_rho_min, d_rho_max],
        "no_search": True, "no_seeds": True, "no_monte_carlo": True,
        "terminal": ("B2_POSITIVE" if positive else
                      "B2_NULL_RHO_DIRECTION" if null else "B2_INCONCLUSIVE_BY_BOUNDS"),
    }
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b2_frozen_physical_path.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
