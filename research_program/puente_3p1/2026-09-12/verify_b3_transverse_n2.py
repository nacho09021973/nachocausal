"""PUENTE-3P1 / B3 — transverse n=2 audit at frozen B2 point."""
import json
import sys
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import lambertw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from verify_b2_2_shape_derivative import evaluate  # noqa: E402

LSTAR = np.array((0.35, 0.9, 1.5, 0.7, 0.1))
XSTAR = np.array((LSTAR[1] / LSTAR[0], LSTAR[3] / LSTAR[2], LSTAR[3] * LSTAR[1]))


def jacobian_chart():
    x1, x2, x3 = XSTAR
    v0, v1, uout, uin, _ = LSTAR
    return np.array([[0.0, 0.0, 0.0], [v0, 0.0, 0.0],
                     [-uout / x1, -uout / x2, uout / x3],
                     [-uin / x1, 0.0, 1.0 / v1], [0.0, 0.0, 0.0]])


def phi_shape_derivative(lam, velocity):
    v0, v1, uout, uin, _ = lam
    dv0, dv1, duout, duin, _ = velocity
    s = lambda uv: (1.0 + lambertw(-uv / np.e, 0).real)
    fin = quad(lambda V: (1.0 - s(uin * V) ** 3) / V, v0, v1,
               epsabs=1e-12, epsrel=1e-12)[0] / 3.0
    fout = quad(lambda V: (s(-uout * V) ** 3 - 1.0) / V, v0, v1,
                epsabs=1e-12, epsrel=1e-12)[0] / 3.0
    gin = lambda U, V: s(U * V) * np.exp(-s(U * V))
    din = duin * quad(lambda V: gin(uin, V), v0, v1)[0]
    dout = duout * quad(lambda V: gin(-uout, V), v0, v1)[0]
    din += dv1 * quad(lambda U: gin(U, v1), 0.0, uin)[0]
    din -= dv0 * quad(lambda U: gin(U, v0), 0.0, uin)[0]
    dout += dv1 * quad(lambda U: gin(U, v1), -uout, 0.0)[0]
    dout -= dv0 * quad(lambda U: gin(U, v0), -uout, 0.0)[0]
    p = fin / (fin + fout)
    return ((1.0 - p) * din - p * dout) / (fin + fout)


def main():
    J = jacobian_chart()
    dphi = np.array([phi_shape_derivative(LSTAR, J[:, j]) for j in range(3)])
    drho_orders = []
    for order in (10, 14):
        drho_orders.append(np.array([evaluate(LSTAR, order, J[:, j])[0:2]
                                     for j in range(3)]))
    margin = np.max(np.abs(drho_orders[1] - drho_orders[0]))
    drho_interval = np.column_stack((drho_orders[1][:, 0] - margin,
                                     drho_orders[1][:, 1] + margin))
    cross_intervals = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        vals = [dphi[i] * drho_interval[j, k] - dphi[j] * drho_interval[i, k]
                for k in (0, 1)]
        cross_intervals.append([min(vals), max(vals)])
    # One certified nonzero wedge component is sufficient for non-proportionality.
    wedge_nonzero = any(a > 0 or b < 0 for a, b in cross_intervals)
    chart_rank_three = np.linalg.matrix_rank(J[1:4, :]) == 3
    drho_nonzero = any(a > 0 or b < 0 for a, b in drho_interval)
    out = {"unit": "PUENTE-3P1/B3", "frozen_lambda": LSTAR.tolist(),
           "gauge_quotiented_coordinates": XSTAR.tolist(), "dphi_dx": dphi.tolist(),
           "drho_dx_enclosures": drho_interval.tolist(),
           "cross_product_enclosures": cross_intervals,
           "chart_rank_three": bool(chart_rank_three),
           "drho_nonzero": bool(drho_nonzero),
           "dphi_wedge_drho_certified_nonzero": bool(wedge_nonzero),
           "no_new_path": True, "no_new_point": True, "no_search": True,
           "no_seeds": True, "no_monte_carlo": True,
           "terminal": ("B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY"
                        if wedge_nonzero and chart_rank_three and drho_nonzero
                        else "B3_INCONCLUSIVE_BY_BOUNDS")}
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b3_transverse_n2.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
