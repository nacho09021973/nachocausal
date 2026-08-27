#!/usr/bin/env python3
"""Post-hoc finite-n profile of the exact number of maximizing orbits.

This runner reproduces the deterministic PCG64 samples from the sealed orbital
curve refinement and records R=|M/Aut(C)| instead of only its indicator R=1.
EMPTY remains separate.  Any backend failure or mismatch with the prior binary
counts aborts before artifacts are written.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import multiprocessing
import time
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from itertools import permutations
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_gate_altura_duracion_lex_d2 as bootstrap_source
from emergencia import p1a_large_n_orbital_baseline_d2 as baseline
from emergencia import p1a_orbital_backend_preflight_d2 as orbital
from emergencia import p1a_orbital_curve_refinement_d2 as refinement


PHASE = "POST_HOC_EXPLORATORY_ORBITAL_MULTIPLICITY"
SCIENTIFIC_TERMINAL = "ORBITAL_MULTIPLICITY_PROFILE_COMPLETED"
EXACT_N = (6, 7, 8, 9)
N_VALUES = refinement.N_VALUES
N_MC = refinement.N_MC
SCIENTIFIC_SEED_BASE = refinement.SCIENTIFIC_SEED_BASE
INSTANCE_TIMEOUT_S = refinement.INSTANCE_TIMEOUT_S
PARALLEL_WORKERS = refinement.PARALLEL_WORKERS

QUANTILES = (0.50, 0.75, 0.90, 0.95, 0.99)
QUANTILE_METHOD = "inverted_cdf"
BOOTSTRAP_REPLICATES = 1_000
BOOTSTRAP_SEED_BASE = 2_608_275_000
BOOTSTRAP_INTERVAL_METHOD = "PERCENTILE_95_LINEAR"
SHANNON_TOLERANCE = 1e-12

HERE = Path(__file__).resolve().parent
RESULTS_DIR = HERE / "resultados"
CONTRACT_PATH = HERE / "P1a_contrato_multiplicidad_orbital_posthoc_d2.md"
FROZEN_EXACT_PATH = RESULTS_DIR / "p1a_tie_aut_exacto_d2.json"
BACKEND_PREFLIGHT_PATH = RESULTS_DIR / "p1a_orbital_backend_preflight_resumen.json"
PRIOR_CSV_PATH = RESULTS_DIR / refinement.CSV_FILENAME
PRIOR_JSON_PATH = RESULTS_DIR / refinement.JSON_FILENAME

SUMMARY_CSV_FILENAME = "p1a_orbital_multiplicity_summary_d2.csv"
LONG_CSV_FILENAME = "p1a_orbital_multiplicity_distribution_d2.csv"
JSON_FILENAME = "p1a_orbital_multiplicity_resumen.json"

SUMMARY_FIELDS = (
    "PHASE",
    "method",
    "interval_method_probabilities",
    "interval_method_distributional",
    "n",
    "seed",
    "N_total",
    "N_empty",
    "N_nonempty",
    "N_R_ge_2",
    "backend_failures",
    "E_n",
    "E_n_ci95_low",
    "E_n_ci95_high",
    "U_n",
    "U_n_star",
    "U_n_star_ci95_low",
    "U_n_star_ci95_high",
    "P_R_2_given_E",
    "P_R_2_given_E_ci95_low",
    "P_R_2_given_E_ci95_high",
    "P_R_3_4_given_E",
    "P_R_3_4_given_E_ci95_low",
    "P_R_3_4_given_E_ci95_high",
    "P_R_ge_5_given_E",
    "P_R_ge_5_given_E_ci95_low",
    "P_R_ge_5_given_E_ci95_high",
    "Sbar_n",
    "Sbar_n_ci95_low",
    "Sbar_n_ci95_high",
    "Sbar_n_tie",
    "Sbar_n_tie_ci95_low",
    "Sbar_n_tie_ci95_high",
    "H_n",
    "H_n_ci95_low",
    "H_n_ci95_high",
    "H_tie_n",
    "H_tie_n_ci95_low",
    "H_tie_n_ci95_high",
    "median_R_given_E",
    "median_R_given_E_ci95_low",
    "median_R_given_E_ci95_high",
    "q75_R_given_E",
    "q75_R_given_E_ci95_low",
    "q75_R_given_E_ci95_high",
    "q90_R_given_E",
    "q90_R_given_E_ci95_low",
    "q90_R_given_E_ci95_high",
    "q95_R_given_E",
    "q95_R_given_E_ci95_low",
    "q95_R_given_E_ci95_high",
    "q99_R_given_E",
    "q99_R_given_E_ci95_low",
    "q99_R_given_E_ci95_high",
    "median_R_given_tie",
    "median_R_given_tie_ci95_low",
    "median_R_given_tie_ci95_high",
    "q75_R_given_tie",
    "q75_R_given_tie_ci95_low",
    "q75_R_given_tie_ci95_high",
    "q90_R_given_tie",
    "q90_R_given_tie_ci95_low",
    "q90_R_given_tie_ci95_high",
    "q95_R_given_tie",
    "q95_R_given_tie_ci95_low",
    "q95_R_given_tie_ci95_high",
    "q99_R_given_tie",
    "q99_R_given_tie_ci95_low",
    "q99_R_given_tie_ci95_high",
    "max_R_observed",
    "shannon_decomposition_residual",
)

LONG_FIELDS = (
    "PHASE",
    "method",
    "n",
    "r",
    "count",
    "p_given_E",
    "p_given_E_ci95_low",
    "p_given_E_ci95_high",
    "q_given_tie",
    "q_given_tie_ci95_low",
    "q_given_tie_ci95_high",
)


@dataclass(frozen=True)
class RawMultiplicity:
    n: int
    method: str
    total: int
    seed: int | None
    empty: int
    r_counts: tuple[tuple[int, int], ...]
    backend_failures: int
    median_time_ms: float
    p95_time_ms: float

    @property
    def counter(self) -> Counter[int]:
        return Counter(dict(self.r_counts))

    @property
    def nonempty(self) -> int:
        return sum(count for _, count in self.r_counts)

    @property
    def ties(self) -> int:
        return sum(count for r, count in self.r_counts if r >= 2)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scientific_seed(n: int) -> int:
    if n not in N_VALUES:
        raise ValueError(f"scientific seed requested outside {N_VALUES}")
    return SCIENTIFIC_SEED_BASE + n


def bootstrap_seed(n: int, population: str) -> int:
    if n not in N_VALUES:
        raise ValueError("bootstrap seed is only defined on the scientific grid")
    code = {"NONEMPTY": 1, "TIE": 2}.get(population)
    if code is None:
        raise ValueError("unknown bootstrap population")
    return BOOTSTRAP_SEED_BASE + 10 * n + code


def validate_sources() -> dict[str, object]:
    paths = (
        FROZEN_EXACT_PATH,
        BACKEND_PREFLIGHT_PATH,
        PRIOR_CSV_PATH,
        PRIOR_JSON_PATH,
    )
    digests = {path.name: baseline._verify_sidecar(path) for path in paths}
    preflight = json.loads(BACKEND_PREFLIGHT_PATH.read_text(encoding="utf-8"))
    prior = json.loads(PRIOR_JSON_PATH.read_text(encoding="utf-8"))
    wrapper_digest = _sha256(Path(orbital.__file__))
    if wrapper_digest != preflight["provenance"]["generator_sha256"]:
        raise RuntimeError("VF2 wrapper changed after exhaustive validation")
    if wrapper_digest != prior["provenance"]["backend_wrapper_sha256"]:
        raise RuntimeError("VF2 wrapper changed after curve refinement")
    if preflight["exhaustive_equivalence"]["backend_equivalence"] != "PASS":
        raise RuntimeError("VF2 exhaustive validation is not PASS")
    if prior["result_status"] != "ORBITAL_CURVE_REFINEMENT_COMPLETED":
        raise RuntimeError("prior curve refinement is not complete")
    design = prior["design"]
    if (
        tuple(design["n_preregistered"]) != N_VALUES
        or int(design["replicates_per_n"]) != N_MC
        or int(design["seed_base"]) != SCIENTIFIC_SEED_BASE
        or bool(design["pooling_with_prior"])
    ):
        raise RuntimeError("prior refinement design does not match frozen reproduction")
    return {
        "artifact_digests": digests,
        "contract_sha256": _sha256(CONTRACT_PATH),
        "backend_wrapper_sha256": wrapper_digest,
        "backend_wrapper_byte_identical": True,
        "prior_payload": prior,
    }


def _p95(values: Sequence[float]) -> float:
    ordered = sorted(values)
    return ordered[max(0, math.ceil(0.95 * len(ordered)) - 1)]


def _uniform_permutations(n: int, replicates: int, seed: int) -> Iterable[tuple[int, ...]]:
    yield from baseline._uniform_permutations(n, replicates, seed)


def accumulate(
    n: int,
    stream: Iterable[Sequence[int]],
    *,
    method: str,
    total: int,
    seed: int | None,
    timeout_s: float | None,
    progress_every: int | None = None,
) -> RawMultiplicity:
    empty = 0
    failures = 0
    r_counts: Counter[int] = Counter()
    timings: list[float] = []
    observed = 0
    for observed, permutation in enumerate(stream, start=1):
        started = time.perf_counter()
        result = orbital.evaluate_orbital_backend(
            permutation, complete_orbits=False, timeout_s=timeout_s
        )
        timings.append(time.perf_counter() - started)
        if result.status == orbital.STATUS_BACKEND_FAILURE:
            failures += 1
            raise RuntimeError(
                f"BACKEND_FAILURE method={method} n={n} replicate={observed}: "
                f"{result.error_type}: {result.error_message}"
            )
        if result.status == orbital.STATUS_EMPTY:
            if result.n_orbits_on_m != 0 or result.n_maximizers != 0:
                raise RuntimeError("EMPTY backend result carried nonempty orbit data")
            empty += 1
        elif result.status in (
            orbital.STATUS_ORBITAL_UNIQUE,
            orbital.STATUS_ORBITAL_NONUNIQUE,
        ):
            r = result.n_orbits_on_m
            if not isinstance(r, int) or r < 1:
                raise RuntimeError("nonempty backend result lacks certified R")
            if (r == 1) != (result.status == orbital.STATUS_ORBITAL_UNIQUE):
                raise RuntimeError("backend status and exact orbit multiplicity disagree")
            r_counts[r] += 1
        else:
            raise RuntimeError(f"unknown backend status {result.status}")
        if progress_every and observed % progress_every == 0:
            print(f"{method} n={n} progress={observed}/{total}", flush=True)
    if observed != total:
        raise RuntimeError(f"replicate count mismatch at n={n}: {observed} != {total}")
    if empty + sum(r_counts.values()) != total:
        raise RuntimeError("EMPTY and R counts do not partition the sample")
    return RawMultiplicity(
        n=n,
        method=method,
        total=total,
        seed=seed,
        empty=empty,
        r_counts=tuple(sorted(r_counts.items())),
        backend_failures=failures,
        median_time_ms=1000 * float(np.median(timings)),
        p95_time_ms=1000 * _p95(timings),
    )


def _frozen_exact_counts() -> dict[int, Counter[int]]:
    payload = json.loads(FROZEN_EXACT_PATH.read_text(encoding="utf-8"))
    return {
        int(row["n"]): Counter(
            {int(r): int(count) for r, count in row["r_counts_all_permutations"].items()}
        )
        for row in payload["aggregates"]
    }


def run_exact_validation() -> list[RawMultiplicity]:
    expected = _frozen_exact_counts()
    rows: list[RawMultiplicity] = []
    for n in EXACT_N:
        raw = accumulate(
            n,
            permutations(range(n)),
            method="EXACT",
            total=math.factorial(n),
            seed=None,
            timeout_s=None,
        )
        observed = raw.counter
        observed[0] = raw.empty
        if observed != expected[n]:
            raise RuntimeError(
                f"exact full-R distribution mismatch at n={n}: "
                f"observed={dict(observed)} expected={dict(expected[n])}"
            )
        rows.append(raw)
        print(f"EXACT_R n={n} counts={dict(sorted(observed.items()))} PASS", flush=True)
    return rows


def _run_scientific_size(n: int) -> RawMultiplicity:
    seed = scientific_seed(n)
    print(f"MULTIPLICITY n={n} replicates={N_MC} seed={seed} START", flush=True)
    return accumulate(
        n,
        _uniform_permutations(n, N_MC, seed),
        method="MONTE_CARLO_REPRODUCTION",
        total=N_MC,
        seed=seed,
        timeout_s=INSTANCE_TIMEOUT_S,
        progress_every=25_000,
    )


def run_scientific() -> list[RawMultiplicity]:
    context = multiprocessing.get_context("fork")
    results: dict[int, RawMultiplicity] = {}
    with ProcessPoolExecutor(max_workers=PARALLEL_WORKERS, mp_context=context) as executor:
        futures = {executor.submit(_run_scientific_size, n): n for n in N_VALUES}
        for future in as_completed(futures):
            n = futures[future]
            results[n] = future.result()
            print(f"MULTIPLICITY n={n} COMPLETE", flush=True)
    return [results[n] for n in N_VALUES]


def _prior_counts(source_validation: Mapping[str, object]) -> dict[int, tuple[int, int, int]]:
    prior = source_validation["prior_payload"]
    assert isinstance(prior, dict)
    return {
        int(row["n"]): (
            int(row["empty_count"]),
            int(row["orbital_unique_count"]),
            int(row["orbital_nonunique_count"]),
        )
        for row in prior["results"]
    }


def validate_scientific_reproduction(
    rows: Sequence[RawMultiplicity], source_validation: Mapping[str, object]
) -> None:
    expected = _prior_counts(source_validation)
    if tuple(row.n for row in rows) != N_VALUES:
        raise RuntimeError("scientific grid is incomplete or out of order")
    for row in rows:
        observed = (row.empty, row.counter[1], row.ties)
        if observed != expected[row.n]:
            raise RuntimeError(
                f"prior binary-count reproduction failed at n={row.n}: "
                f"observed={observed} expected={expected[row.n]}"
            )


def _probability_interval(count: int, total: int, exact: bool) -> tuple[float | None, float | None]:
    if total == 0:
        return None, None
    value = count / total
    return (value, value) if exact else sealed.wilson_interval(count, total)


def _entropy(counts: Mapping[int, int]) -> float | None:
    total = sum(counts.values())
    if total == 0:
        return None
    value = 0.0
    for count in counts.values():
        if count:
            probability = count / total
            value -= probability * math.log(probability)
    return value


def _mean_log(counts: Mapping[int, int]) -> float | None:
    total = sum(counts.values())
    if total == 0:
        return None
    return sum(count * math.log(r) for r, count in counts.items()) / total


def _count_quantile(counts: Mapping[int, int], quantile: float) -> int | None:
    if not 0 < quantile <= 1:
        raise ValueError("quantile must lie in (0,1]")
    total = sum(counts.values())
    if total == 0:
        return None
    target = max(1, math.ceil(quantile * total))
    cumulative = 0
    for value in sorted(counts):
        cumulative += counts[value]
        if cumulative >= target:
            return value
    raise RuntimeError("empirical quantile escaped observed support")


def _distribution_metrics(counts: Mapping[int, int]) -> dict[str, float | int | None]:
    return {
        "mean_log": _mean_log(counts),
        "entropy": _entropy(counts),
        **{f"q{int(q * 100):02d}": _count_quantile(counts, q) for q in QUANTILES},
    }


def bootstrap_distribution(
    counts: Mapping[int, int], *, seed: int, replicates: int = BOOTSTRAP_REPLICATES
) -> dict[str, tuple[float, float]]:
    values = np.asarray(sorted(counts), dtype=np.int64)
    frequencies = np.asarray([counts[int(value)] for value in values], dtype=np.int64)
    total = int(frequencies.sum())
    if total == 0:
        return {}
    probabilities = frequencies / total
    rng = np.random.Generator(np.random.PCG64(seed))
    names = ("mean_log", "entropy", *(f"q{int(q * 100):02d}" for q in QUANTILES))
    samples = {name: np.empty(replicates, dtype=np.float64) for name in names}
    for replicate in range(replicates):
        draw = rng.multinomial(total, probabilities)
        draw_counts = {
            int(value): int(count)
            for value, count in zip(values, draw)
            if int(count) > 0
        }
        metrics = _distribution_metrics(draw_counts)
        for name in names:
            samples[name][replicate] = float(metrics[name])
    return {
        name: bootstrap_source.percentile_interval(array)
        for name, array in samples.items()
    }


def _binary_entropy(value: float) -> float:
    if value <= 0.0 or value >= 1.0:
        return 0.0
    return -value * math.log(value) - (1.0 - value) * math.log(1.0 - value)


def _number(value: float | int | None) -> str:
    if value is None:
        return "NA"
    if isinstance(value, int):
        return str(value)
    return format(value, ".17g")


def _put_interval(
    row: dict[str, object], prefix: str, interval: tuple[float | None, float | None]
) -> None:
    row[f"{prefix}_ci95_low"] = _number(interval[0])
    row[f"{prefix}_ci95_high"] = _number(interval[1])


def summarize(raw: RawMultiplicity) -> dict[str, object]:
    counts = raw.counter
    tie_counts = Counter({r: count for r, count in counts.items() if r >= 2})
    exact = raw.method == "EXACT"
    nonempty = raw.nonempty
    ties = raw.ties
    unique = counts[1]
    e = nonempty / raw.total
    u = unique / raw.total
    u_star = unique / nonempty if nonempty else None
    r2 = counts[2]
    r34 = counts[3] + counts[4]
    r5 = sum(count for r, count in counts.items() if r >= 5)
    nonempty_metrics = _distribution_metrics(counts)
    tie_metrics = _distribution_metrics(tie_counts)
    nonempty_bootstrap = (
        {}
        if exact
        else bootstrap_distribution(counts, seed=bootstrap_seed(raw.n, "NONEMPTY"))
    )
    tie_bootstrap = (
        {}
        if exact or not ties
        else bootstrap_distribution(tie_counts, seed=bootstrap_seed(raw.n, "TIE"))
    )
    h = nonempty_metrics["entropy"]
    h_tie = tie_metrics["entropy"]
    shannon_residual = None
    if u_star is not None and h is not None:
        rhs = _binary_entropy(u_star) + (1.0 - u_star) * float(h_tie or 0.0)
        shannon_residual = float(h) - rhs

    row: dict[str, object] = {
        "PHASE": PHASE,
        "method": raw.method,
        "interval_method_probabilities": "EXACT_POINT" if exact else "WILSON_95",
        "interval_method_distributional": (
            "EXACT_POINT" if exact else BOOTSTRAP_INTERVAL_METHOD
        ),
        "n": raw.n,
        "seed": raw.seed if raw.seed is not None else "NA",
        "N_total": raw.total,
        "N_empty": raw.empty,
        "N_nonempty": nonempty,
        "N_R_ge_2": ties,
        "backend_failures": raw.backend_failures,
        "E_n": _number(e),
        "U_n": _number(u),
        "U_n_star": _number(u_star),
        "P_R_2_given_E": _number(r2 / nonempty if nonempty else None),
        "P_R_3_4_given_E": _number(r34 / nonempty if nonempty else None),
        "P_R_ge_5_given_E": _number(r5 / nonempty if nonempty else None),
        "Sbar_n": _number(nonempty_metrics["mean_log"]),
        "Sbar_n_tie": _number(tie_metrics["mean_log"]),
        "H_n": _number(h),
        "H_tie_n": _number(h_tie),
        "max_R_observed": max(counts) if counts else "NA",
        "shannon_decomposition_residual": _number(shannon_residual),
    }
    _put_interval(row, "E_n", _probability_interval(nonempty, raw.total, exact))
    _put_interval(row, "U_n_star", _probability_interval(unique, nonempty, exact))
    for prefix, count in (
        ("P_R_2_given_E", r2),
        ("P_R_3_4_given_E", r34),
        ("P_R_ge_5_given_E", r5),
    ):
        _put_interval(row, prefix, _probability_interval(count, nonempty, exact))

    metric_mapping = {
        "Sbar_n": (nonempty_metrics, nonempty_bootstrap, "mean_log"),
        "H_n": (nonempty_metrics, nonempty_bootstrap, "entropy"),
        "Sbar_n_tie": (tie_metrics, tie_bootstrap, "mean_log"),
        "H_tie_n": (tie_metrics, tie_bootstrap, "entropy"),
    }
    for prefix, (metrics, intervals, name) in metric_mapping.items():
        value = metrics[name]
        interval = (
            (float(value), float(value))
            if exact and value is not None
            else intervals.get(name, (None, None))
        )
        _put_interval(row, prefix, interval)

    quantile_prefixes = {
        0.50: "median_R",
        0.75: "q75_R",
        0.90: "q90_R",
        0.95: "q95_R",
        0.99: "q99_R",
    }
    for population, metrics, intervals in (
        ("given_E", nonempty_metrics, nonempty_bootstrap),
        ("given_tie", tie_metrics, tie_bootstrap),
    ):
        for quantile, base_prefix in quantile_prefixes.items():
            name = f"q{int(quantile * 100):02d}"
            prefix = f"{base_prefix}_{population}"
            value = metrics[name]
            row[prefix] = _number(value)
            interval = (
                (float(value), float(value))
                if exact and value is not None
                else intervals.get(name, (None, None))
            )
            _put_interval(row, prefix, interval)
    if set(row) != set(SUMMARY_FIELDS):
        missing = set(SUMMARY_FIELDS) - set(row)
        extra = set(row) - set(SUMMARY_FIELDS)
        raise RuntimeError(f"summary schema mismatch missing={missing} extra={extra}")
    return row


def distribution_rows(raw: RawMultiplicity) -> list[dict[str, object]]:
    counts = raw.counter
    exact = raw.method == "EXACT"
    nonempty = raw.nonempty
    ties = raw.ties
    if not counts:
        return []
    rows: list[dict[str, object]] = []
    for r in range(1, max(counts) + 1):
        count = counts[r]
        p = count / nonempty
        p_interval = _probability_interval(count, nonempty, exact)
        q = count / ties if r >= 2 and ties else None
        q_interval = (
            _probability_interval(count, ties, exact) if r >= 2 and ties else (None, None)
        )
        rows.append(
            {
                "PHASE": PHASE,
                "method": raw.method,
                "n": raw.n,
                "r": r,
                "count": count,
                "p_given_E": _number(p),
                "p_given_E_ci95_low": _number(p_interval[0]),
                "p_given_E_ci95_high": _number(p_interval[1]),
                "q_given_tie": _number(q),
                "q_given_tie_ci95_low": _number(q_interval[0]),
                "q_given_tie_ci95_high": _number(q_interval[1]),
            }
        )
    return rows


def validate_outputs(
    raw_rows: Sequence[RawMultiplicity],
    summary_rows: Sequence[Mapping[str, object]],
    long_rows: Sequence[Mapping[str, object]],
) -> dict[str, str]:
    controls = {
        "BACKEND_FAILURES": "0",
        "COUNTS_PARTITION_TOTAL": "PASS",
        "FULL_R_DISTRIBUTION_SUMS_TO_NONEMPTY": "PASS",
        "P_R1_EQUALS_U_STAR": "PASS",
        "E_TIMES_U_STAR_EQUALS_U": "PASS",
        "SBAR_NONNEGATIVE": "PASS",
        "SBAR_TIE_GE_LOG2": "PASS",
        "MEAN_LOG_DIRECT_DEFINITION": "PASS",
        "SHANNON_DECOMPOSITION": "PASS",
        "LONG_TABLE_COMPLETE_SUPPORT": "PASS",
    }
    long_by_n: dict[int, list[Mapping[str, object]]] = {}
    for row in long_rows:
        long_by_n.setdefault(int(row["n"]), []).append(row)
    for raw, summary in zip(raw_rows, summary_rows):
        if raw.backend_failures or raw.empty + raw.nonempty != raw.total:
            controls["COUNTS_PARTITION_TOTAL"] = "FAIL"
        if sum(raw.counter.values()) != raw.nonempty:
            controls["FULL_R_DISTRIBUTION_SUMS_TO_NONEMPTY"] = "FAIL"
        u_star = raw.counter[1] / raw.nonempty
        if not math.isclose(float(summary["U_n_star"]), u_star, abs_tol=1e-15):
            controls["P_R1_EQUALS_U_STAR"] = "FAIL"
        if not math.isclose(
            float(summary["E_n"]) * float(summary["U_n_star"]),
            float(summary["U_n"]),
            abs_tol=1e-15,
        ):
            controls["E_TIMES_U_STAR_EQUALS_U"] = "FAIL"
        if float(summary["Sbar_n"]) < -1e-15:
            controls["SBAR_NONNEGATIVE"] = "FAIL"
        if raw.ties and float(summary["Sbar_n_tie"]) < math.log(2) - 1e-15:
            controls["SBAR_TIE_GE_LOG2"] = "FAIL"
        direct = sum(count * math.log(r) for r, count in raw.counter.items()) / raw.nonempty
        if not math.isclose(float(summary["Sbar_n"]), direct, abs_tol=1e-15):
            controls["MEAN_LOG_DIRECT_DEFINITION"] = "FAIL"
        if abs(float(summary["shannon_decomposition_residual"])) > SHANNON_TOLERANCE:
            controls["SHANNON_DECOMPOSITION"] = "FAIL"
        expected_support = list(range(1, max(raw.counter) + 1))
        observed_support = [int(row["r"]) for row in long_by_n.get(raw.n, [])]
        if observed_support != expected_support:
            controls["LONG_TABLE_COMPLETE_SUPPORT"] = "FAIL"
    if any(value == "FAIL" for value in controls.values()):
        raise RuntimeError(f"multiplicity hard guard failed: {controls}")
    return controls


def _csv_bytes(rows: Sequence[Mapping[str, object]], fields: Sequence[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def report_payload(
    summary_rows: Sequence[Mapping[str, object]],
    controls: Mapping[str, str],
    source_validation: Mapping[str, object],
    summary_digest: str,
    long_digest: str,
) -> dict[str, object]:
    scientific = [row for row in summary_rows if row["method"] != "EXACT"]
    return {
        "artifact_schema": "P1A_ORBITAL_MULTIPLICITY_D2_V1",
        "phase": PHASE,
        "result_status": SCIENTIFIC_TERMINAL,
        "design": {
            "exact_n": list(EXACT_N),
            "scientific_n": list(N_VALUES),
            "replicates_per_scientific_n": N_MC,
            "seed_base": SCIENTIFIC_SEED_BASE,
            "seed_formula": "260828000 + n",
            "generator": "numpy.random.Generator(PCG64)",
            "sample_relation": "deterministic reproduction of curve-refinement samples",
            "bootstrap_replicates": BOOTSTRAP_REPLICATES,
            "bootstrap_seed_base": BOOTSTRAP_SEED_BASE,
            "bootstrap_method": BOOTSTRAP_INTERVAL_METHOD,
            "quantiles": list(QUANTILES),
            "quantile_method": QUANTILE_METHOD,
            "hypothesis_tests": False,
            "p_values": False,
        },
        "source_validation": {
            key: value for key, value in source_validation.items() if key != "prior_payload"
        },
        "controls": dict(controls),
        "results": list(summary_rows),
        "observed_extrema": {
            "grid_minimum_U_star": min(
                scientific, key=lambda row: float(row["U_n_star"])
            )["n"],
            "grid_maximum_Sbar_tie": max(
                scientific, key=lambda row: float(row["Sbar_n_tie"])
            )["n"],
            "grid_maximum_H_tie": max(
                scientific, key=lambda row: float(row["H_tie_n"])
            )["n"],
            "maximum_R_observed": max(int(row["max_R_observed"]) for row in scientific),
        },
        "artifacts": {
            SUMMARY_CSV_FILENAME: {"sha256": summary_digest, "phase": PHASE},
            LONG_CSV_FILENAME: {"sha256": long_digest, "phase": PHASE},
        },
        "provenance": {
            "contract": f"emergencia/{CONTRACT_PATH.name}",
            "contract_sha256": _sha256(CONTRACT_PATH),
            "runner": "emergencia/p1a_orbital_multiplicity_d2.py",
            "runner_sha256": _sha256(Path(__file__)),
            "backend_wrapper": "emergencia/p1a_orbital_backend_preflight_d2.py",
            "backend_wrapper_sha256": _sha256(Path(orbital.__file__)),
            "bootstrap_reference": "emergencia/p1a_gate_altura_duracion_lex_d2.py",
            "bootstrap_reference_sha256": _sha256(Path(bootstrap_source.__file__)),
        },
        "claim_ceiling": (
            "post-hoc finite-n multiplicity profile through n=40; log R is an operational "
            "residual-multiplicity observable; no causal entropy, asymptotic, transition, "
            "critical-scale, RG, universality, or physical-entropy claim"
        ),
    }


def write_artifacts(
    summary_rows: Sequence[Mapping[str, object]],
    long_rows: Sequence[Mapping[str, object]],
    controls: Mapping[str, str],
    source_validation: Mapping[str, object],
) -> list[tuple[Path, str]]:
    summary_path = RESULTS_DIR / SUMMARY_CSV_FILENAME
    long_path = RESULTS_DIR / LONG_CSV_FILENAME
    json_path = RESULTS_DIR / JSON_FILENAME
    targets = (
        summary_path,
        summary_path.with_suffix(summary_path.suffix + ".sha256"),
        long_path,
        long_path.with_suffix(long_path.suffix + ".sha256"),
        json_path,
        json_path.with_suffix(json_path.suffix + ".sha256"),
    )
    if any(path.exists() for path in targets):
        raise FileExistsError("refusing to overwrite an orbital-multiplicity artifact")
    summary_data = _csv_bytes(summary_rows, SUMMARY_FIELDS)
    long_data = _csv_bytes(long_rows, LONG_FIELDS)
    summary_digest = comparison._write_with_sidecar(summary_path, summary_data, overwrite=False)
    long_digest = comparison._write_with_sidecar(long_path, long_data, overwrite=False)
    payload = report_payload(
        summary_rows, controls, source_validation, summary_digest, long_digest
    )
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    json_digest = comparison._write_with_sidecar(json_path, encoded, overwrite=False)
    return [
        (summary_path, summary_digest),
        (long_path, long_digest),
        (json_path, json_digest),
    ]


def run_all(*, write: bool) -> tuple[list[dict[str, object]], dict[str, object]]:
    source_validation = validate_sources()
    exact_rows = run_exact_validation()
    scientific_rows = run_scientific()
    validate_scientific_reproduction(scientific_rows, source_validation)
    raw_rows = [*exact_rows, *scientific_rows]
    summary_rows = [summarize(row) for row in raw_rows]
    long_rows = [item for row in raw_rows for item in distribution_rows(row)]
    controls = validate_outputs(raw_rows, summary_rows, long_rows)
    summary_digest = hashlib.sha256(_csv_bytes(summary_rows, SUMMARY_FIELDS)).hexdigest()
    long_digest = hashlib.sha256(_csv_bytes(long_rows, LONG_FIELDS)).hexdigest()
    payload = report_payload(
        summary_rows, controls, source_validation, summary_digest, long_digest
    )
    if write:
        for path, digest in write_artifacts(
            summary_rows, long_rows, controls, source_validation
        ):
            print(f"WROTE {path} sha256={digest}", flush=True)
    print(json.dumps(payload, indent=2, sort_keys=True), flush=True)
    return summary_rows, payload


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--write-artifacts", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    print(f"PHASE={PHASE}")
    print(
        f"N_VALUES={N_VALUES} N_MC={N_MC} SEED_FORMULA={SCIENTIFIC_SEED_BASE}+n "
        f"BOOTSTRAP={BOOTSTRAP_REPLICATES} R_EXACT=YES"
    )
    if args.write_artifacts and not args.run:
        raise ValueError("--write-artifacts requires --run")
    if args.run:
        run_all(write=args.write_artifacts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
