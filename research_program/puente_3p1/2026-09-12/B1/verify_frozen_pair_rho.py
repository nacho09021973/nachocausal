"""PUENTE-3P1 / B1.3 — par congelado y intervalo determinista para rho.

The pair is declared in the module constants before any rho calculation. This file performs no
lambda search, no Monte Carlo, no seed use, and no estimator fitting.
"""
import json
import math
from scipy.integrate import quad
from scipy.optimize import brentq


LAMBDA0 = (0.5, 1.0, 1.0, 0.5, 0.1)
LAMBDA1 = (0.2, 0.8, 2.0, 0.9, 0.1)


def s_of_uv(uv):
    z = -uv
    f = lambda s: (s - 1.0) * math.exp(s) - z
    if z <= 0.0:
        return brentq(f, 0.0, 1.0)
    hi = 2.0
    while f(hi) < 0.0:
        hi *= 2.0
    return brentq(f, 1.0, hi)


def G(uv):
    s = s_of_uv(uv)
    return s * math.exp(-s)


def q(uv):
    s = s_of_uv(uv)
    return math.exp(-0.5 * s) / math.sqrt(s)


def invariants(lam):
    v0, v1, uo, ui, _ = lam
    return (v1 / v0, ui / uo, ui * v1)


def phi(lam):
    v0, v1, uo, ui, _ = lam
    fin = quad(lambda V: (1.0 - s_of_uv(ui * V) ** 3) / V,
               v0, v1, epsabs=1e-12, epsrel=1e-12, limit=200)[0] / 3.0
    fout = quad(lambda V: (s_of_uv(-uo * V) ** 3 - 1.0) / V,
                v0, v1, epsabs=1e-12, epsrel=1e-12, limit=200)[0] / 3.0
    return fin / (fin + fout)


def angular_probability(budget):
    return (1.0 - math.cos(min(math.pi, max(0.0, budget)))) / 2.0


def rho_interval(lam):
    v0, v1, uo, ui, _ = lam
    ulo, uhi = -uo, ui
    corners = (ulo * v0, ulo * v1, uhi * v0, uhi * v1)
    qmin, qmax = min(q(x) for x in corners), max(q(x) for x in corners)

    def ordered_integral(qbound):
        def integrate_uy(uy, vx, vy):
            return quad(lambda ux: G(ux * vx) * G(uy * vy) *
                        angular_probability(qbound * math.sqrt((uy - ux) * (vy - vx))),
                        ulo, uy, epsabs=2e-8, epsrel=2e-7, limit=100)[0]

        def integrate_vx(vx, vy):
            return quad(lambda uy: integrate_uy(uy, vx, vy), ulo, uhi,
                        epsabs=2e-8, epsrel=2e-7, limit=100)[0]

        return quad(lambda vy: quad(lambda vx: integrate_vx(vx, vy), v0, vy,
                                    epsabs=2e-7, epsrel=3e-6, limit=100)[0],
                    v0, v1, epsabs=2e-7, epsrel=3e-6, limit=100)[0]

    z = quad(lambda V: quad(lambda U: G(U * V), ulo, uhi,
                            epsabs=1e-11, epsrel=1e-11, limit=100)[0],
             v0, v1, epsabs=1e-11, epsrel=1e-11, limit=100)[0]
    # Exchange symmetry contributes the factor two.
    return 2.0 * ordered_integral(qmin) / z**2, 2.0 * ordered_integral(qmax) / z**2, z


def main():
    # Freeze and record the pair before any rho/interval evaluation.
    pair = (LAMBDA0, LAMBDA1)
    pre = [{"lambda": list(lam), "invariants": invariants(lam), "phi": phi(lam)}
           for lam in pair]
    assert pre[0]["invariants"] != pre[1]["invariants"]
    assert abs(pre[0]["phi"] - pre[1]["phi"]) > 1e-12

    intervals = []
    for lam in pair:
        lo, hi, z = rho_interval(lam)
        intervals.append({"lambda": list(lam), "rho_lower": lo, "rho_upper": hi,
                          "normalization_Z": z})

    separated = intervals[0]["rho_upper"] < intervals[1]["rho_lower"] or \
        intervals[1]["rho_upper"] < intervals[0]["rho_lower"]
    out = {
        "unit": "PUENTE-3P1/B1.3",
        "frozen_pair_before_rho": True,
        "lambda_pair": [list(LAMBDA0), list(LAMBDA1)],
        "pre_rho_geometry": pre,
        "rho_intervals": intervals,
        "no_search": True,
        "no_seeds": True,
        "no_monte_carlo": True,
        "quadrature_deterministic": True,
        "terminal": "B1.3_POSITIVE" if separated else "B1.3_INCONCLUSIVE_BY_BOUNDS",
    }
    print(json.dumps(out, indent=2))
    with open(__file__.rsplit("/", 1)[0] + "/verification_frozen_pair_rho.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
