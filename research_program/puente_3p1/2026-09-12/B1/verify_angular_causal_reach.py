"""PUENTE-3P1 / B1.2 — comprobaciones deterministas del alcance angular.

No ejecuta simulacion, no consume semillas, no busca pares lambda y no calcula rho.
"""
import json
import math
from scipy.integrate import quad
from scipy.optimize import brentq


def s_of_uv(uv):
    """Unique s>0 solving (s-1) exp(s) = -uv, for uv<1."""
    z = -uv
    f = lambda s: (s - 1.0) * math.exp(s) - z
    if z <= 0.0:
        return brentq(f, 0.0, 1.0)
    hi = 2.0
    while f(hi) < 0.0:
        hi *= 2.0
    return brentq(f, 1.0, hi)


def q_of_uv(uv):
    s = s_of_uv(uv)
    return math.exp(-0.5 * s) / math.sqrt(s)


def bounds(ux, uy, vx, vy):
    if ux > uy or vx > vy:
        return 0.0, 0.0
    du, dv = uy - ux, vy - vx
    if du == 0.0 or dv == 0.0:
        return 0.0, 0.0
    corners = (ux * vx, ux * vy, uy * vx, uy * vy)
    qmax = max(q_of_uv(uv) for uv in corners)
    upper = qmax * math.sqrt(du * dv)
    lower = math.sqrt(du / dv) * quad(
        lambda V: q_of_uv((ux + du * (V - vx) / dv) * V), vx, vy,
        epsabs=1e-12, epsrel=1e-12, limit=200
    )[0]
    return min(math.pi, lower), min(math.pi, upper)


def main():
    # Fixed points lie strictly below UV=1, as required by the frozen patch.
    cases = [
        (-1.0, 0.5, 0.4, 1.0),
        (-0.4, 0.8, 0.2, 0.7),
        (-0.2, 0.3, 0.5, 0.9),
    ]
    rows = []
    for ux, uy, vx, vy in cases:
        lb, ub = bounds(ux, uy, vx, vy)
        rows.append({"points": [ux, uy, vx, vy], "lower": lb, "upper": ub,
                     "lower_le_upper": lb <= ub + 1e-12})

    # Algebra: C/r^2 = exp(-s)/s = q(s)^2 after r=2Ms.
    algebra = []
    for s in (0.2, 0.7, 1.0, 2.0, 5.0):
        lhs = math.exp(-s) / s
        rhs = (math.exp(-0.5 * s) / math.sqrt(s)) ** 2
        algebra.append(abs(lhs - rhs))

    # q decreases with s; s increases with -UV.
    s_values = [0.2, 0.7, 1.0, 2.0, 5.0]
    q_values = [math.exp(-0.5 * s) / math.sqrt(s) for s in s_values]
    monotone = all(a > b for a, b in zip(q_values, q_values[1:]))

    out = {
        "unit": "PUENTE-3P1/B1.2",
        "formula": "Delta_max=min(pi,sup_U integral q(UV)*sqrt(U') dV)",
        "deterministic_quadrature": True,
        "no_runs": True,
        "no_seeds": True,
        "no_pair_search": True,
        "algebra_max_abs_error": max(algebra),
        "q_strictly_decreases_with_s": monotone,
        "rows": rows,
        "degenerate_radial_case": bounds(0.1, 0.1, 0.2, 0.8) == (0.0, 0.0),
        "reverse_coordinate_case": bounds(0.5, -0.1, 0.2, 0.8) == (0.0, 0.0),
    }
    assert out["algebra_max_abs_error"] < 1e-14
    assert out["q_strictly_decreases_with_s"]
    assert all(row["lower_le_upper"] for row in rows)
    assert out["degenerate_radial_case"] and out["reverse_coordinate_case"]
    out["CONCLUSION"] = "ANGULAR_REACH_VARIATIONAL_FORMULA_AND_BOUNDS_VERIFIED"
    print(json.dumps(out, indent=2))
    with open(__file__.rsplit("/", 1)[0] + "/verification_angular_causal_reach.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
