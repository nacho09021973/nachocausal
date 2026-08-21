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
import hashlib
import json
import math
import sys
from collections import defaultdict

sys.path.insert(0, "emergencia")

from p1a_count_volume_cota_resolucion_evaluacion_d2 import bound_for_m  # noqa: E402

INTERVALS_CSV = "emergencia/resultados/p1a_representaciones_intervalos_d2.csv"
SUMMARY_JSON = "emergencia/resultados/p1a_representaciones_resumen.json"
CORRELATION_GATE = 0.80

# Pieza A de docs/scope_note_2026-08-21_selection_mass_stress_test_DRAFT.md Seccion 3.1.
# Los artefactos se leen; no se regeneran. Los sha256 son los sellados en
# emergencia/P1a_count_volume_canal_sigma_m_d2.md Seccion 10.4.
SEALED_SHA256 = {
    INTERVALS_CSV: "5110688b89142bf06e738a6f66bb41fa7c248e29352392b8bc763480ebd3ab08",
    SUMMARY_JSON: "7176a3a6e55cf309911a636592780880c55574773d398a9a620a1536ea7899dc",
}

# Tabla congelada de emergencia/P1a_count_volume_cota_correlacion_d2.md lineas 101-106.
# Orden: (n, side) -> (Var(Y), B_n, B_n/Var, MSEobs/Var, B_n/MSEafin,
#                      rho_max_ub_Bn, rho_obs, NRMSE_min, k_necesario)
SEALED_TABLE = {
    (64, "FUTURE"): ("0.004152", "0.001102", "0.2654", "0.9491", "0.3908",
                     "0.8571", "0.5664", "0.5152", "1.36"),
    (64, "PAST"): ("0.004042", "0.001100", "0.2722", "0.9510", "0.4005",
                   "0.8531", "0.5660", "0.5217", "1.32"),
    (96, "FUTURE"): ("0.002671", "0.000771", "0.2885", "0.9539", "0.4012",
                     "0.8435", "0.5300", "0.5372", "1.25"),
    (96, "PAST"): ("0.002590", "0.000771", "0.2977", "0.9574", "0.4216",
                   "0.8380", "0.5420", "0.5457", "1.21"),
    (128, "FUTURE"): ("0.001935", "0.000598", "0.3087", "0.9261", "0.4398",
                      "0.8314", "0.5458", "0.5556", "1.17"),
    (128, "PAST"): ("0.002016", "0.000597", "0.2960", "0.9255", "0.4130",
                    "0.8390", "0.5322", "0.5441", "1.22"),
}


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_sealed_artifacts():
    """Punto 3 de la Seccion 3.1: los artefactos leidos son los sellados."""
    for path, expected in SEALED_SHA256.items():
        actual = sha256_of(path)
        if actual != expected:
            raise AssertionError(
                f"sha256 mismatch en {path}: esperado {expected}, leido {actual}"
            )
    return {path: SEALED_SHA256[path] for path in SEALED_SHA256}


def formatted_row(summary_entry):
    s = summary_entry
    return (
        f"{s['var_y']:.6f}",
        f"{s['bound_avg']:.6f}",
        f"{s['ratio_bound_over_var']:.4f}",
        f"{s['ratio_mse_over_var']:.4f}",
        f"{s['bound_avg'] / s['mse_affine_calibrated']:.4f}",
        f"{s['rho_max_ub_Bn']:.4f}",
        f"{s['rho_observed']:.4f}",
        f"{s['nrmse_sigma_min']:.4f}",
        f"{s['k_needed']:.2f}",
    )


def verify_verbatim_table(summary):
    """Punto 4 de la Seccion 3.1: las columnas preexistentes se reproducen verbatim."""
    if set(summary) != set(SEALED_TABLE):
        raise AssertionError(
            f"estratos {sorted(summary)} != congelados {sorted(SEALED_TABLE)}"
        )
    for key in sorted(SEALED_TABLE):
        got = formatted_row(summary[key])
        want = SEALED_TABLE[key]
        if got != want:
            raise AssertionError(f"fila {key} no reproduce verbatim: {got} != {want}")
    return len(SEALED_TABLE)


def selection_mass(path):
    """Punto 1 de la Seccion 3.1: Pr_n(S) empirica = selected_count / replicas."""
    with open(path) as f:
        data = json.load(f)
    replicates = data["contract"]["base_replicates_per_n"]
    counts = defaultdict(set)
    for metric in data["metrics"]:
        counts[int(metric["n"])].add(int(metric["selected_count"]))
    out = {}
    for n in sorted(counts):
        if len(counts[n]) != 1:
            raise AssertionError(f"selected_count inconsistente en n={n}: {counts[n]}")
        selected = counts[n].pop()
        out[n] = (selected, replicates, selected / replicates)
    return out


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
    verified = verify_sealed_artifacts()
    summary = summarize(load_rows(INTERVALS_CSV))
    verbatim_rows = verify_verbatim_table(summary)

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

    # ---- Pieza A, magnitudes derivadas (nota de alcance 2026-08-21, Seccion 3.1) ----
    # Ninguna de estas cifras decide nada: son descriptivas sobre datos ya vistos.
    print()
    print("PIEZA A - DESCRIPTIVE_ALREADY_SEEN (no es preinscripcion)")
    print()
    print("Objetivo primario: masa de seleccion empirica Pr_n(S) = selected_count/replicas")
    print(f"{'n':>4} {'selected':>9} {'replicas':>9} {'Pr_n(S)':>9}")
    masses = selection_mass(SUMMARY_JSON)
    for n, (selected, replicates, ratio) in masses.items():
        print(f"{n:>4} {selected:>9} {replicates:>9} {ratio:>9.4f}")

    print()
    print("Diagnostico secundario: n * Var_hat(ell) por estrato")
    print(f"{'n':>4} {'side':>6} {'Var(Y)':>9} {'n*Var(Y)':>9}")
    for (n, side), s in summary.items():
        print(f"{n:>4} {side:>6} {s['var_y']:>9.6f} {n * s['var_y']:>9.4f}")

    print()
    print("CONTROLES PIEZA A (deben ser todos True):")
    print(f"  sha256 sellados verificados = {len(verified) == len(SEALED_SHA256)}")
    print(f"  filas reproducidas verbatim = {verbatim_rows == len(SEALED_TABLE)}")
    print()
    print("PIECE_A_SEALED_HASHES_VERIFIED = YES")
    print(f"PIECE_A_VERBATIM_ROWS_REPRODUCED = {verbatim_rows}")
    print(
        "PIECE_A_SELECTION_MASS_RANGE = "
        f"[{min(r for _, _, r in masses.values()):.4f}, "
        f"{max(r for _, _, r in masses.values()):.4f}]"
    )
    print(
        "PIECE_A_N_VAR_RANGE = "
        f"[{min(n * s['var_y'] for (n, _), s in summary.items()):.4f}, "
        f"{max(n * s['var_y'] for (n, _), s in summary.items()):.4f}]"
    )
    print("PIECE_A_TERMINAL = STRESS_A_DESCRIPTIVE_EMITTED")
