"""CV-4 item 1: traduce la cota de varianza B_n a techo de correlacion.

Determinista, solo lectura sobre datos ya sellados de Fase 6. Reutiliza
`bound_for_m` del script de evaluacion ya auditado en
`emergencia/P1a_count_volume_cota_resolucion_d2.md` Seccion 5; no redefine la
formula demostrada.

Identidad usada (Seccion 3 del documento de traduccion):
  para cualquier estimador f medible respecto de (m,n,side,S),
  min_{a,b} E[(Y - a - b f)^2] = Var(Y)(1 - rho(Y,f)^2) >= E[Var(Y|.)] >= B_n,
por tanto  rho(Y,f)^2 <= 1 - B_n/Var(Y).
"""

import csv
import math
import sys
from collections import defaultdict

sys.path.insert(0, "emergencia")

from p1a_count_volume_cota_resolucion_evaluacion_d2 import bound_for_m  # noqa: E402

INTERVALS_CSV = "emergencia/resultados/p1a_representaciones_intervalos_d2.csv"
CORRELATION_GATE = 0.80


def load_rows(path):
    rows = defaultdict(list)
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            n = int(row["n"])
            if n not in (64, 96, 128):
                continue
            rows[(n, row["side"])].append(
                (
                    int(row["interval_size"]),
                    float(row["latent_duration"]),
                    float(row["estimate_count_volume"]),
                )
            )
    return rows


def pearson(xs, ys):
    count = len(xs)
    mx = sum(xs) / count
    my = sum(ys) / count
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    return sxy / math.sqrt(sxx * syy)


def summarize(rows):
    cache = {}
    out = {}
    for (n, side), entries in sorted(rows.items()):
        count = len(entries)
        ys = [y for _, y, _ in entries]
        fs = [f for _, _, f in entries]
        my = sum(ys) / count
        var_y = sum((y - my) ** 2 for y in ys) / (count - 1)

        bound_sum = 0.0
        for m, _, _ in entries:
            key = (m, n)
            if key not in cache:
                cache[key] = bound_for_m(m, n)
            bound_sum += cache[key]
        bound_avg = bound_sum / count

        mse_obs = sum((f - y) ** 2 for y, f in zip(ys, fs)) / count
        rho_obs = pearson(ys, fs)
        # MSE del mejor recalibrado afin de COUNT_VOLUME (a + b*f).
        mse_affine = var_y * (1.0 - rho_obs ** 2)

        ratio = bound_avg / var_y
        out[(n, side)] = {
            "count": count,
            "var_y": var_y,
            "bound_avg": bound_avg,
            "mse_observed": mse_obs,
            "mse_affine_calibrated": mse_affine,
            "ratio_bound_over_var": ratio,
            "ratio_mse_over_var": mse_obs / var_y,
            # COTA SUPERIOR de rho_max inducida por B_n; NO es la correlacion maxima
            # real (esa se calcula en p1a_count_volume_canal_sigma_m_d2.py).
            "rho_max_ub_Bn": math.sqrt(max(0.0, 1.0 - ratio)),
            "rho_observed": rho_obs,
            "nrmse_sigma_min": math.sqrt(ratio),
            "k_needed": (1.0 - CORRELATION_GATE ** 2) * var_y / bound_avg,
            "bound_survives_affine_calibration": mse_affine >= bound_avg,
            "gate_structurally_excluded": ratio > 1.0 - CORRELATION_GATE ** 2,
        }
    return out


if __name__ == "__main__":
    summary = summarize(load_rows(INTERVALS_CSV))

    print(
        f"{'n':>4} {'side':>6} {'count':>6} {'Var(Y)':>9} {'B_n':>9} {'B_n/Var':>8} "
        f"{'MSEobs/Var':>11} {'B_n/MSEafin':>12} {'rho_max_ub_Bn':>13} {'rho_obs':>8} "
        f"{'NRMSE_min':>10} {'k_needed':>9}"
    )
    for (n, side), s in summary.items():
        print(
            f"{n:>4} {side:>6} {s['count']:>6} {s['var_y']:>9.6f} {s['bound_avg']:>9.6f} "
            f"{s['ratio_bound_over_var']:>8.4f} {s['ratio_mse_over_var']:>11.4f} "
            f"{s['bound_avg'] / s['mse_affine_calibrated']:>12.4f} "
            f"{s['rho_max_ub_Bn']:>13.4f} {s['rho_observed']:>8.4f} "
            f"{s['nrmse_sigma_min']:>10.4f} {s['k_needed']:>9.2f}"
        )

    print()
    print("CONTROLES (deben ser todos True):")
    all_ok = True
    for (n, side), s in summary.items():
        checks = {
            "bound<=MSE_afin": s["bound_survives_affine_calibration"],
            "rho_obs<=rho_max_ub_Bn": s["rho_observed"] <= s["rho_max_ub_Bn"],
            "MSE_afin<=MSE_obs": s["mse_affine_calibrated"] <= s["mse_observed"],
        }
        all_ok &= all(checks.values())
        print(f"  n={n:>3} {side:>6}: " + "  ".join(f"{k}={v}" for k, v in checks.items()))

    print()
    print(f"CV4_TRANSLATION_CONSISTENCY = {'PASS' if all_ok else 'FAIL'}")
    excluded = all(s["gate_structurally_excluded"] for s in summary.values())
    print(f"CV4_GATE_0.80_STRUCTURALLY_EXCLUDED_BY_BOUND = {'YES' if excluded else 'NO'}")
    print(
        "CV4_MAX_K_NEEDED = "
        f"{max(s['k_needed'] for s in summary.values()):.2f}"
    )
