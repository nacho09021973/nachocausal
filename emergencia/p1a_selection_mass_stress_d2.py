"""Pieza B — stress test preinscrito sobre la masa de seleccion Pr_n(S).

Autorizado por la Firma 2 de
`docs/scope_note_2026-08-21_selection_mass_stress_test_DRAFT.md` Seccion 9.5.

Objetivo primario:   Pr_n(S) en tamanos nuevos.
Diagnostico secundario: n * Var_hat(ell | n, side, S).

Ningun terminal puede ser PROVED ni REFUTED: un barrido finito no decide
inf_{n>=n_0} Pr_n(S) > 0 en ninguna direccion.

El selector NO se reimplementa: se invoca el de
`emergencia/p1a_comparar_selectores_d2.py`, igual que hace
`emergencia/p1a_representaciones_alternativas_d2.py`.
"""

from __future__ import annotations

import math
import statistics
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, ".")

from emergencia import p1a_comparar_selectores_d2 as comparison  # noqa: E402
from emergencia import p1a_count_volume_cota_correlacion_d2 as correlation  # noqa: E402
from emergencia import p1a_enumeracion_simulacion as sealed  # noqa: E402
from emergencia import p1a_estabilidad_d2 as previous  # noqa: E402
from emergencia import p1a_gate_altura_duracion_lex_d2 as height_gate  # noqa: E402
from emergencia import p1a_representaciones_alternativas_d2 as alternatives  # noqa: E402

# ---------------------------------------------------------------- Seccion 4.1
STRESS_N = (192, 256, 384, 512)
STRESS_BATCHES = 8
STRESS_REPLICATES_PER_N = {192: 12_000, 256: 12_000, 384: 4_000, 512: 4_000}
STRESS_REPLICATES_PER_BATCH = {192: 1_500, 256: 1_500, 384: 500, 512: 500}

# ---------------------------------------------------------------- Seccion 4.3
STRESS_BOOTSTRAP_REPLICATES = 10_000

# ---------------------------------------------------------------- Seccion 4.4
STRESS_COORDINATE_SEED_BASE = 2_610_000_000
STRESS_BOOTSTRAP_SEED_BASE = 2_620_000_000

HISTORICAL_BASES = (
    2_608_030_000,
    2_608_035_000, 2_608_036_000, 2_608_037_000,
    2_608_038_000, 2_608_039_000,
    2_608_040_000, 2_608_041_000, 2_608_042_000, 2_608_043_000,
    2_608_044_000, 2_608_045_000,
)
RESERVED_002 = (2_000_000, 2_999_999)
# Margen de guarda: cualquier expansion historica vale a lo sumo ~100*n+batch,
# es decir < 10^5 por encima de su base. 10^6 es un orden de magnitud mas.
GUARD_MARGIN = 1_000_000

# ---------------------------------------------------------------- Seccion 4.5
PRIMARY_FAMILY_SIZE = 4      # 4 intervalos Wilson
SECONDARY_FAMILY_SIZE = 8    # 4 tamanos x 2 lados
FAMILY_ALPHA = 0.05
BUDGET_SECONDS = 6 * 60 * 60

# ---------------------------------------------------------------- Seccion 5.1
# Congelados por la Firma 2. El script los recalcula y aborta si no coinciden.
FLOOR = 0.38
BAND_LOW = 0.15
BAND_HIGH = 0.41

SIDES = height_gate.SIDES


def stress_coordinate_seed(n: int, batch: int) -> int:
    if n not in STRESS_N or not 0 <= batch < STRESS_BATCHES:
        raise ValueError("coordinate seed outside the preregistered contract")
    return STRESS_COORDINATE_SEED_BASE + 1000 * n + batch


def stress_bootstrap_seed(n: int, side: str) -> int:
    if n not in STRESS_N or side not in SIDES:
        raise ValueError("bootstrap seed outside the preregistered contract")
    return STRESS_BOOTSTRAP_SEED_BASE + 1000 * n + SIDES.index(side)


def emitted_seeds() -> set[int]:
    seeds: list[int] = []
    for n in STRESS_N:
        for batch in range(STRESS_BATCHES):
            seeds.append(stress_coordinate_seed(n, batch))
        for side in SIDES:
            seeds.append(stress_bootstrap_seed(n, side))
    if len(seeds) != len(set(seeds)):
        raise AssertionError("semillas duplicadas dentro del conjunto emitido")
    return set(seeds)


def historical_seeds() -> set[int]:
    """Reconstruye el historico LLAMANDO a las funciones, no copiando numeros."""
    seeds: set[int] = set()
    for n in sealed.MC_N:
        for batch in range(sealed.MC_BATCHES):
            seeds.add(sealed.seed_for(n, batch))
    for n in previous.BASE_N:
        for batch in range(previous.BASE_BATCHES):
            seeds.add(previous.coordinate_seed(n, batch))
            seeds.add(previous.thinning_seed(n, batch))
    for n in comparison.BASE_N:
        for batch in range(comparison.BASE_BATCHES):
            seeds.add(comparison.coordinate_seed(n, batch))
            seeds.add(comparison.thinning_seed(n, batch))
    for n in height_gate.BASE_N:
        for batch in range(height_gate.BASE_BATCHES):
            seeds.add(height_gate.coordinate_seed(n, batch))
            seeds.add(height_gate.thinning_seed(n, batch))
        for side in height_gate.SIDES:
            seeds.add(height_gate.bootstrap_seed(n, side))
    for n in alternatives.BASE_N:
        for batch in range(alternatives.BASE_BATCHES):
            seeds.add(alternatives.coordinate_seed(n, batch))
        for representation in alternatives.REPRESENTATIONS:
            for side in alternatives.SIDES:
                seeds.add(alternatives.bootstrap_seed(representation, n, side))
    # baseline_seed recorre tamanos de intervalo y tiene su propia guarda de
    # dominio (k0); se barre un rango holgado y se respeta esa guarda.
    for size in range(0, 601):
        for module in (previous, height_gate):
            try:
                seeds.add(module.baseline_seed(size))
            except ValueError:
                continue
    return seeds


def preflight_seeds() -> dict[str, object]:
    """Seccion 4.4: assert sobre CONJUNTOS completos, no sobre bases."""
    emitted = emitted_seeds()
    historical = historical_seeds()
    collision = emitted & historical
    if collision:
        raise AssertionError(f"colision de semillas con el historico: {sorted(collision)}")
    low, high = RESERVED_002
    reserved_hits = {s for s in emitted if low <= s <= high}
    if reserved_hits:
        raise AssertionError(f"semillas dentro de RESERVED_002: {sorted(reserved_hits)}")
    # La guarda cubre tambien cualquier semilla historica no reconstruida.
    guard = max(max(historical), max(HISTORICAL_BASES)) + GUARD_MARGIN
    if min(emitted) <= guard:
        raise AssertionError(
            f"banda insuficiente: min(emitidas)={min(emitted)} <= guarda={guard}"
        )
    return {
        "emitted": len(emitted),
        "historical": len(historical),
        "max_historical": max(historical),
        "min_emitted": min(emitted),
        "guard": guard,
    }


def preflight_thresholds() -> dict[str, float]:
    """Seccion 5.1: recalcula FLOOR y la banda y aborta si no reproducen."""
    masses = correlation.selection_mass(correlation.SUMMARY_JSON)
    p_dev = min(ratio for _, _, ratio in masses.values())
    summary = correlation.summarize(correlation.load_rows(correlation.INTERVALS_CSV))
    n_var = [n * s["var_y"] for (n, _), s in summary.items()]
    v_dev = (min(n_var) + max(n_var)) / 2.0
    derived_floor = math.floor((2.0 / 3.0) * p_dev * 100) / 100
    derived_low = round(0.6 * v_dev, 2)
    derived_high = round(1.6 * v_dev, 2)
    for name, derived, frozen in (
        ("FLOOR", derived_floor, FLOOR),
        ("BAND_LOW", derived_low, BAND_LOW),
        ("BAND_HIGH", derived_high, BAND_HIGH),
    ):
        if abs(derived - frozen) > 1e-9:
            raise AssertionError(
                f"{name} derivado {derived} != congelado {frozen} (Seccion 5.1)"
            )
    return {"p_dev": p_dev, "v_dev": v_dev}


def bonferroni_z(family_size: int) -> float:
    per_test = FAMILY_ALPHA / family_size
    return statistics.NormalDist().inv_cdf(1.0 - per_test / 2.0)


def run_size(n: int) -> dict[str, object]:
    """Genera un tamano completo. Nunca devuelve un tamano parcial."""
    replicates_total = STRESS_REPLICATES_PER_N[n]
    per_batch = STRESS_REPLICATES_PER_BATCH[n]
    if per_batch * STRESS_BATCHES != replicates_total:
        raise AssertionError(f"lotes inconsistentes en n={n}")
    selected = 0
    replicate = 0
    latents: dict[str, list[float]] = {side: [] for side in SIDES}
    for batch in range(STRESS_BATCHES):
        rng = np.random.Generator(np.random.PCG64(stress_coordinate_seed(n, batch)))
        for _ in range(per_batch):
            u_sorted, v_sorted, permutation = previous.product_permutation(
                rng.random(n), rng.random(n)
            )
            outcome = comparison.evaluate_selectors(permutation)[
                comparison.MIN_COVERAGE_LEX
            ]
            if outcome.state == comparison.STATE_UNIQUE:
                if outcome.selection is None:
                    raise RuntimeError("unique lex outcome missing selection")
                selected += 1
                a, b, c, d = outcome.selection.quadruple
                for side, start, stop in (
                    (height_gate.PAST, a, b),
                    (height_gate.FUTURE, c, d),
                ):
                    latents[side].append(
                        height_gate.latent_duration(u_sorted, v_sorted, start, stop)
                    )
            replicate += 1
    if replicate != replicates_total:
        raise RuntimeError(f"replicate mismatch at n={n}")
    for side in SIDES:
        if len(latents[side]) != selected:
            raise RuntimeError(f"latent row mismatch at n={n} side={side}")
    return {"n": n, "selected": selected, "replicates": replicate, "latents": latents}


def bootstrap_n_var(n: int, side: str, values: list[float]) -> tuple[float, float, float]:
    array = np.asarray(values, dtype=np.float64)
    point = n * float(np.var(array, ddof=1))
    rng = np.random.Generator(np.random.PCG64(stress_bootstrap_seed(n, side)))
    size = array.size
    stats = np.empty(STRESS_BOOTSTRAP_REPLICATES, dtype=np.float64)
    for i in range(STRESS_BOOTSTRAP_REPLICATES):
        sample = array[rng.integers(0, size, size)]
        stats[i] = n * float(np.var(sample, ddof=1))
    per_test = FAMILY_ALPHA / SECONDARY_FAMILY_SIZE
    lo = float(np.percentile(stats, 100.0 * per_test / 2.0))
    hi = float(np.percentile(stats, 100.0 * (1.0 - per_test / 2.0)))
    return point, lo, hi


def selection_trend(wilson: dict[int, tuple[float, float]]) -> str:
    """Seccion 5.2: cascada ordenada, exhaustiva y excluyente."""
    lo192, hi192 = wilson[192]
    lo384, hi384 = wilson[384]
    lo512, hi512 = wilson[512]
    if hi512 < lo192:
        return "DECAYING"
    if lo512 > hi192:
        return "RISING"
    if max(lo384, lo512) <= min(hi384, hi512):
        return "STABILISING"
    return "INDETERMINATE"


def variance_signal(
    points: dict[tuple[int, str], float],
    intervals: dict[tuple[int, str], tuple[float, float]],
) -> str:
    """Seccion 5.3: lectura de un solo lado; solo el crecimiento va en contra."""
    for side in SIDES:
        series = [points[(n, side)] for n in STRESS_N]
        strictly_increasing = all(x < y for x, y in zip(series, series[1:]))
        if strictly_increasing and intervals[(512, side)][0] > intervals[(192, side)][1]:
            return "GROWTH_SIGNAL"
    if all(intervals[(512, side)][1] <= intervals[(192, side)][1] for side in SIDES):
        return "BOUNDED_CONSISTENT"
    return "INDETERMINATE"


def recommendation(terminal: str, floor_verdict: str, trend: str, signal: str) -> str:
    """Seccion 6.2. La primera clausula tiene prioridad."""
    if terminal != "STRESS_B_COMPLETED":
        return "UNDECIDED"
    if trend == "DECAYING" or signal == "GROWTH_SIGNAL":
        return "NO"
    if trend in ("STABILISING", "RISING") and floor_verdict == "MET" and signal != "GROWTH_SIGNAL":
        return "YES"
    return "UNDECIDED"


def print_blocked_terminal(started: float, reason: Exception) -> None:
    print("  PREFLIGHTS = FAIL")
    print()
    print(f"STRESS_B_TERMINAL              = STRESS_B_BLOCKED")
    print(f"STRESS_B_SIZES_COMPLETED       = []")
    print(f"STRESS_B_ELAPSED_SECONDS       = {time.monotonic() - started:.1f}")
    print(f"STRESS_B_BLOCKED_REASON        = {type(reason).__name__}: {reason}")
    print("ANALYTIC_ATTACK_RECOMMENDED    = UNDECIDED")
    print("ANALYTIC_ATTACK_AUTHORISED     = NO")
    print("LEAN_STATUS                    = FROZEN_VALID_NOT_RETRACTED")
    print("LEAN_NEW_FORMALIZATION         = NOT_AUTHORIZED")
    print("NOVELTY_CERTIFIED              = NO")


def main() -> int:
    started = time.monotonic()
    print("PIEZA B - PROSPECTIVE_PREREGISTERED")
    print()

    print("PREFLIGHTS (cualquier fallo termina en STRESS_B_BLOCKED)")
    try:
        seed_report = preflight_seeds()
    except Exception as exc:
        print_blocked_terminal(started, exc)
        return 1
    print(
        f"  semillas emitidas={seed_report['emitted']} "
        f"historicas={seed_report['historical']} "
        f"max(historicas)={seed_report['max_historical']} "
        f"min(emitidas)={seed_report['min_emitted']} "
        f"guarda={seed_report['guard']}"
    )
    try:
        threshold_report = preflight_thresholds()
    except Exception as exc:
        print_blocked_terminal(started, exc)
        return 1
    print(
        f"  umbrales reproducidos: FLOOR={FLOOR} BAND=[{BAND_LOW}, {BAND_HIGH}] "
        f"(p_dev={threshold_report['p_dev']:.4f} v_dev={threshold_report['v_dev']:.4f})"
    )
    z_primary = bonferroni_z(PRIMARY_FAMILY_SIZE)
    z_note = 100.0 * (1.0 - FAMILY_ALPHA / PRIMARY_FAMILY_SIZE)
    print(f"  Wilson por test al {z_note:.3f} % (z={z_primary:.4f}, Bonferroni sobre 4)")
    print("  PREFLIGHTS = PASS")
    print()

    results: dict[int, dict[str, object]] = {}
    elapsed_by_size: dict[int, float] = {}
    terminal = "STRESS_B_COMPLETED"
    for n in STRESS_N:
        size_start = time.monotonic()
        results[n] = run_size(n)
        elapsed_by_size[n] = time.monotonic() - size_start
        total = time.monotonic() - started
        print(
            f"STRESS_SIZE_DONE n={n} selected={results[n]['selected']} "
            f"replicates={results[n]['replicates']} "
            f"seconds={elapsed_by_size[n]:.1f} total={total:.1f}",
            flush=True,
        )
        if total >= BUDGET_SECONDS and n != STRESS_N[-1]:
            terminal = "STRESS_B_BUDGET_EXHAUSTED"
            print(f"BUDGET_REACHED_AFTER n={n}; se detiene la escalera", flush=True)
            break

    completed = tuple(sorted(results))
    if completed != STRESS_N:
        terminal = "STRESS_B_BUDGET_EXHAUSTED"

    print()
    print("Objetivo primario: Pr_n(S)")
    print(f"{'n':>5} {'selected':>9} {'replicas':>9} {'Pr_n(S)':>9} {'W_lo':>8} {'W_hi':>8}")
    wilson: dict[int, tuple[float, float]] = {}
    for n in completed:
        selected = int(results[n]["selected"])
        trials = int(results[n]["replicates"])
        lo, hi = sealed.wilson_interval(selected, trials, z=z_primary)
        wilson[n] = (lo, hi)
        print(
            f"{n:>5} {selected:>9} {trials:>9} {selected / trials:>9.4f} "
            f"{lo:>8.4f} {hi:>8.4f}"
        )

    print()
    print("Diagnostico secundario: n * Var_hat(ell)")
    print(f"{'n':>5} {'side':>7} {'n*Var':>9} {'B_lo':>9} {'B_hi':>9}")
    points: dict[tuple[int, str], float] = {}
    intervals: dict[tuple[int, str], tuple[float, float]] = {}
    for n in completed:
        latents = results[n]["latents"]
        for side in SIDES:
            point, lo, hi = bootstrap_n_var(n, side, latents[side])
            points[(n, side)] = point
            intervals[(n, side)] = (lo, hi)
            print(f"{n:>5} {side:>7} {point:>9.4f} {lo:>9.4f} {hi:>9.4f}")

    if terminal == "STRESS_B_COMPLETED":
        floor_verdict = (
            "MET" if all(wilson[n][0] >= FLOOR for n in STRESS_N) else "NOT_MET"
        )
        trend = selection_trend(wilson)
        band = (
            "IN"
            if all(
                BAND_LOW <= points[(n, side)] <= BAND_HIGH
                for n in STRESS_N
                for side in SIDES
            )
            else "OUT"
        )
        signal = variance_signal(points, intervals)
    else:
        floor_verdict = "NOT_EVALUABLE"
        trend = "NOT_EVALUABLE"
        band = "NOT_EVALUABLE"
        signal = "NOT_EVALUABLE"

    advice = recommendation(terminal, floor_verdict, trend, signal)

    print()
    print(f"STRESS_B_TERMINAL              = {terminal}")
    print(f"STRESS_B_SIZES_COMPLETED       = {list(completed)}")
    print(f"STRESS_B_ELAPSED_SECONDS       = {time.monotonic() - started:.1f}")
    print(f"SELECTION_MASS_CANDIDATE_FLOOR = {floor_verdict}")
    print(f"SELECTION_MASS_TREND           = {trend}")
    print(f"VARIANCE_CANDIDATE_BAND        = {band}")
    print(f"VARIANCE_ORDER_SIGNAL          = {signal}")
    print(f"ANALYTIC_ATTACK_RECOMMENDED    = {advice}")
    print("ANALYTIC_ATTACK_AUTHORISED     = NO")
    print("LEAN_STATUS                    = FROZEN_VALID_NOT_RETRACTED")
    print("LEAN_NEW_FORMALIZATION         = NOT_AUTHORIZED")
    print("NOVELTY_CERTIFIED              = NO")
    return 0


if __name__ == "__main__":
    sys.exit(main())
