#!/usr/bin/env python3
"""Post-hoc exploratory large-n orbital baseline, with hard engineering gates.

This runner samples uniform permutations directly.  It never simulates thinning
masks and never substitutes literal selector uniqueness for orbital uniqueness.
Exact n=6..9 reproduction and n=24,32 engineering benchmarks run before any
scientific Monte Carlo sample is materialized.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import os
import statistics
import time
from collections import Counter
from dataclasses import dataclass
from itertools import permutations
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_orbital_backend_preflight_d2 as orbital


PHASE = "POST_HOC_EXPLORATORY_LARGE_N_BASELINE"
EXACT_N = (6, 7, 8, 9)
MC_N = (10, 12, 16, 24, 32)
N_MC = 100_000
SCIENTIFIC_SEED_BASE = 260_826_000

ENGINEERING_GATE_N = (24, 32)
ENGINEERING_GATE_INSTANCES = 100
ENGINEERING_GATE_SEED_BASE = 260_827_000
ENGINEERING_GATE_P95_MAX_S = 0.25
INSTANCE_TIMEOUT_S = 5.0

HERE = Path(__file__).resolve().parent
RESULTS_DIR = HERE / "resultados"
FROZEN_ORBITAL_PATH = RESULTS_DIR / "p1a_tie_aut_exacto_d2.json"
BACKEND_PREFLIGHT_PATH = RESULTS_DIR / "p1a_orbital_backend_preflight_resumen.json"
MACROTEST_PATH = RESULTS_DIR / "p1a_macrotest_exploratorio_resumen.json"
CSV_FILENAME = "p1a_large_n_orbital_baseline_d2.csv"
JSON_FILENAME = "p1a_large_n_orbital_baseline_resumen.json"

FIELDS = (
    "PHASE",
    "method",
    "interval_method",
    "n",
    "replicates",
    "seed",
    "empty_count",
    "nonempty_count",
    "orbital_unique_count",
    "orbital_nonunique_count",
    "U_hat",
    "U_ci95_low",
    "U_ci95_high",
    "E_hat",
    "E_ci95_low",
    "E_ci95_high",
    "U_star_hat",
    "U_star_ci95_low",
    "U_star_ci95_high",
    "G_hat",
    "backend_failures",
    "median_time_ms",
    "p95_time_ms",
)


@dataclass(frozen=True)
class RawCounts:
    n: int
    method: str
    replicates: int
    seed: int | None
    empty: int
    orbital_unique: int
    orbital_nonunique: int
    backend_failures: int
    timings_s: tuple[float, ...]

    @property
    def nonempty(self) -> int:
        return self.orbital_unique + self.orbital_nonunique


def scientific_seed(n: int) -> int:
    if n not in MC_N:
        raise ValueError(f"scientific seed requested outside {MC_N}")
    return SCIENTIFIC_SEED_BASE + n


def engineering_seed(n: int) -> int:
    if n not in ENGINEERING_GATE_N:
        raise ValueError(f"engineering seed requested outside {ENGINEERING_GATE_N}")
    return ENGINEERING_GATE_SEED_BASE + n


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _verify_sidecar(path: Path) -> str:
    sidecar = path.with_suffix(path.suffix + ".sha256")
    fields = sidecar.read_text(encoding="utf-8").strip().split()
    if len(fields) != 2 or fields[1] != path.name:
        raise RuntimeError(f"invalid sidecar for {path}")
    digest = _sha256(path)
    if digest != fields[0]:
        raise RuntimeError(f"SHA-256 mismatch for {path}")
    return digest


def validate_sources() -> dict[str, object]:
    digests = {
        FROZEN_ORBITAL_PATH.name: _verify_sidecar(FROZEN_ORBITAL_PATH),
        BACKEND_PREFLIGHT_PATH.name: _verify_sidecar(BACKEND_PREFLIGHT_PATH),
        MACROTEST_PATH.name: _verify_sidecar(MACROTEST_PATH),
    }
    preflight = json.loads(BACKEND_PREFLIGHT_PATH.read_text(encoding="utf-8"))
    wrapper_digest = _sha256(Path(orbital.__file__))
    validated_digest = preflight["provenance"]["generator_sha256"]
    if wrapper_digest != validated_digest:
        raise RuntimeError("VF2 wrapper is not byte-identical to exhaustive validation")
    if preflight["engineering_verdict"] != "READY":
        raise RuntimeError("prior VF2 engineering verdict is not READY")
    if preflight["exhaustive_equivalence"]["total"] != orbital.EXPECTED_TOTAL:
        raise RuntimeError("prior VF2 exhaustive total is incomplete")
    return {
        "artifact_digests": digests,
        "wrapper_current_sha256": wrapper_digest,
        "wrapper_validated_sha256": validated_digest,
        "wrapper_byte_identical": True,
        "prior_preflight": preflight,
    }


def _p95(values: Sequence[float]) -> float:
    ordered = sorted(values)
    return ordered[max(0, math.ceil(0.95 * len(ordered)) - 1)]


def _accumulate(
    n: int,
    permutation_stream: Iterable[Sequence[int]],
    *,
    method: str,
    replicates: int,
    seed: int | None,
    timeout_s: float | None,
    progress_every: int | None = None,
) -> RawCounts:
    counts: Counter[str] = Counter()
    timings: list[float] = []
    observed = 0
    for observed, permutation in enumerate(permutation_stream, start=1):
        started = time.perf_counter()
        result = orbital.evaluate_orbital_backend(
            permutation, complete_orbits=False, timeout_s=timeout_s
        )
        timings.append(time.perf_counter() - started)
        counts[result.status] += 1
        if result.status == orbital.STATUS_BACKEND_FAILURE:
            raise RuntimeError(
                f"BACKEND_FAILURE at method={method}, n={n}, replicate={observed}: "
                f"{result.error_type}: {result.error_message}"
            )
        if result.status not in (
            orbital.STATUS_EMPTY,
            orbital.STATUS_ORBITAL_UNIQUE,
            orbital.STATUS_ORBITAL_NONUNIQUE,
        ):
            raise RuntimeError(f"unknown backend status {result.status}")
        if progress_every and observed % progress_every == 0:
            print(f"{method} n={n} progress={observed}/{replicates}", flush=True)
    if observed != replicates:
        raise RuntimeError(f"replicate count mismatch at n={n}: {observed} != {replicates}")
    return RawCounts(
        n=n,
        method=method,
        replicates=replicates,
        seed=seed,
        empty=counts[orbital.STATUS_EMPTY],
        orbital_unique=counts[orbital.STATUS_ORBITAL_UNIQUE],
        orbital_nonunique=counts[orbital.STATUS_ORBITAL_NONUNIQUE],
        backend_failures=counts[orbital.STATUS_BACKEND_FAILURE],
        timings_s=tuple(timings),
    )


def _frozen_expected_counts() -> dict[int, tuple[int, int, int]]:
    payload = json.loads(FROZEN_ORBITAL_PATH.read_text(encoding="utf-8"))
    expected: dict[int, tuple[int, int, int]] = {}
    for aggregate in payload["aggregates"]:
        n = int(aggregate["n"])
        optimized = aggregate["optimized_state_counts"]
        diagnostic = aggregate["diagnostic_state_counts"]
        expected[n] = (
            int(optimized.get("EMPTY", 0)),
            int(diagnostic.get("UNIQUE", 0)) + int(diagnostic.get("TIE_AUT_ONLY", 0)),
            int(diagnostic.get("TIE_NONAUT", 0)),
        )
    return expected


def run_exact_control() -> tuple[list[RawCounts], bool]:
    expected = _frozen_expected_counts()
    rows: list[RawCounts] = []
    passed = True
    for n in EXACT_N:
        raw = _accumulate(
            n,
            permutations(range(n)),
            method="EXACT",
            replicates=math.factorial(n),
            seed=None,
            timeout_s=None,
        )
        observed = (raw.empty, raw.orbital_unique, raw.orbital_nonunique)
        passed &= observed == expected[n] and raw.backend_failures == 0
        rows.append(raw)
        print(
            f"EXACT_CONTROL n={n} observed={observed} expected={expected[n]} "
            f"status={'PASS' if observed == expected[n] else 'FAIL'}",
            flush=True,
        )
        if not passed:
            break
    return rows, passed


def _prior_lower_sizes_pass(source_validation: dict[str, object]) -> bool:
    preflight = source_validation["prior_preflight"]
    assert isinstance(preflight, dict)
    benchmark = {int(row["n"]): row for row in preflight["benchmark"]}  # type: ignore[index]
    return all(
        n in benchmark
        and int(benchmark[n]["backend_failure"]) == 0
        and int(benchmark[n]["success"]) == 100
        for n in (10, 12, 16)
    )


def _uniform_permutations(n: int, replicates: int, seed: int) -> Iterable[tuple[int, ...]]:
    rng = np.random.Generator(np.random.PCG64(seed))
    for _ in range(replicates):
        yield tuple(int(value) for value in rng.permutation(n))


def run_engineering_gate(
    source_validation: dict[str, object],
) -> tuple[list[dict[str, object]], tuple[int, ...]]:
    authorized: list[int] = [10, 12, 16] if _prior_lower_sizes_pass(source_validation) else []
    rows: list[dict[str, object]] = []
    for n in ENGINEERING_GATE_N:
        seed = engineering_seed(n)
        raw = _accumulate(
            n,
            _uniform_permutations(n, ENGINEERING_GATE_INSTANCES, seed),
            method="ENGINEERING_BENCHMARK",
            replicates=ENGINEERING_GATE_INSTANCES,
            seed=seed,
            timeout_s=INSTANCE_TIMEOUT_S,
        )
        p95 = _p95(raw.timings_s)
        passed = raw.backend_failures == 0 and p95 <= ENGINEERING_GATE_P95_MAX_S
        if passed:
            authorized.append(n)
        row = {
            "n": n,
            "instances": ENGINEERING_GATE_INSTANCES,
            "seed": seed,
            "success": ENGINEERING_GATE_INSTANCES - raw.backend_failures,
            "backend_failure": raw.backend_failures,
            "median_time_s": statistics.median(raw.timings_s),
            "p95_time_s": p95,
            "max_time_s": max(raw.timings_s),
            "p95_gate_s": ENGINEERING_GATE_P95_MAX_S,
            "status": "PASS" if passed else "FAIL",
        }
        rows.append(row)
        print(
            f"ENGINEERING_GATE n={n} failures={raw.backend_failures} "
            f"p95_s={p95:.6f} status={row['status']}",
            flush=True,
        )
    return rows, tuple(n for n in MC_N if n in authorized)


def run_scientific(authorized_sizes: Sequence[int]) -> list[RawCounts]:
    rows: list[RawCounts] = []
    for n in authorized_sizes:
        seed = scientific_seed(n)
        print(f"MONTE_CARLO n={n} replicates={N_MC} seed={seed} START", flush=True)
        rows.append(
            _accumulate(
                n,
                _uniform_permutations(n, N_MC, seed),
                method="MONTE_CARLO",
                replicates=N_MC,
                seed=seed,
                timeout_s=INSTANCE_TIMEOUT_S,
                progress_every=25_000,
            )
        )
    return rows


def _number(value: float | None) -> str:
    return "NA" if value is None else format(value, ".17g")


def summarize(raw: RawCounts) -> dict[str, object]:
    if raw.backend_failures:
        raise RuntimeError("cannot summarize a run with backend failures")
    if raw.empty + raw.nonempty != raw.replicates:
        raise RuntimeError("counts do not sum to replicates")
    if raw.orbital_unique > raw.nonempty:
        raise RuntimeError("U count exceeds E count")

    u = raw.orbital_unique / raw.replicates
    e = raw.nonempty / raw.replicates
    u_star = raw.orbital_unique / raw.nonempty if raw.nonempty else None
    g = raw.orbital_nonunique / raw.replicates
    if raw.method == "EXACT":
        u_interval = (u, u)
        e_interval = (e, e)
        u_star_interval = (u_star, u_star)
        interval_method = "EXACT_POINT"
    else:
        u_interval = sealed.wilson_interval(raw.orbital_unique, raw.replicates)
        e_interval = sealed.wilson_interval(raw.nonempty, raw.replicates)
        u_star_interval = (
            sealed.wilson_interval(raw.orbital_unique, raw.nonempty)
            if raw.nonempty
            else (None, None)
        )
        interval_method = "WILSON_95"

    return {
        "PHASE": PHASE,
        "method": raw.method,
        "interval_method": interval_method,
        "n": raw.n,
        "replicates": raw.replicates,
        "seed": raw.seed if raw.seed is not None else "NA",
        "empty_count": raw.empty,
        "nonempty_count": raw.nonempty,
        "orbital_unique_count": raw.orbital_unique,
        "orbital_nonunique_count": raw.orbital_nonunique,
        "U_hat": _number(u),
        "U_ci95_low": _number(u_interval[0]),
        "U_ci95_high": _number(u_interval[1]),
        "E_hat": _number(e),
        "E_ci95_low": _number(e_interval[0]),
        "E_ci95_high": _number(e_interval[1]),
        "U_star_hat": _number(u_star),
        "U_star_ci95_low": _number(u_star_interval[0]),
        "U_star_ci95_high": _number(u_star_interval[1]),
        "G_hat": _number(g),
        "backend_failures": raw.backend_failures,
        "median_time_ms": _number(1000 * statistics.median(raw.timings_s)),
        "p95_time_ms": _number(1000 * _p95(raw.timings_s)),
    }


def validate_rows(rows: Sequence[dict[str, object]], exact_passed: bool) -> dict[str, str]:
    counts_pass = all(
        int(row["empty_count"])
        + int(row["orbital_unique_count"])
        + int(row["orbital_nonunique_count"])
        + int(row["backend_failures"])
        == int(row["replicates"])
        for row in rows
    )
    failures = sum(int(row["backend_failures"]) for row in rows)
    u_le_e = all(int(row["orbital_unique_count"]) <= int(row["nonempty_count"]) for row in rows)
    ratio_pass = all(
        row["U_star_hat"] == "NA"
        if int(row["nonempty_count"]) == 0
        else math.isclose(
            float(row["U_star_hat"]),
            int(row["orbital_unique_count"]) / int(row["nonempty_count"]),
            rel_tol=0,
            abs_tol=1e-15,
        )
        for row in rows
    )
    controls = {
        "BACKEND_FAILURES": str(failures),
        "COUNTS_SUM_TO_NMC": "PASS" if counts_pass else "FAIL",
        "U_LE_E": "PASS" if u_le_e else "FAIL",
        "U_STAR_EQUALS_U_OVER_E": "PASS" if ratio_pass else "FAIL",
        "EXACT_BASELINE_REPRODUCTION": "PASS" if exact_passed else "FAIL",
    }
    if failures or any(value == "FAIL" for value in controls.values()):
        raise RuntimeError(f"scientific hard guard failed: {controls}")
    return controls


def _trend(rows: Sequence[dict[str, object]], field: str) -> str:
    values = [float(row[field]) for row in sorted(rows, key=lambda item: int(item["n"]))]
    if all(left < right for left, right in zip(values, values[1:])):
        return "INCREASED"
    if all(left > right for left, right in zip(values, values[1:])):
        return "DECREASED"
    return "NON_MONOTONE"


def _rows_to_csv(rows: Sequence[dict[str, object]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def payload(
    rows: Sequence[dict[str, object]],
    source_validation: dict[str, object],
    exact_passed: bool,
    engineering_gate: Sequence[dict[str, object]],
    authorized_sizes: Sequence[int],
    controls: dict[str, str],
    csv_digest: str,
) -> dict[str, object]:
    mc_rows = [row for row in rows if row["method"] == "MONTE_CARLO"]
    return {
        "artifact_schema": "P1A_LARGE_N_ORBITAL_BASELINE_D2_V1",
        "phase": PHASE,
        "result_status": (
            "LARGE_N_BASELINE_COMPLETED"
            if tuple(authorized_sizes) == MC_N
            else "LARGE_N_BASELINE_PARTIALLY_COMPLETED"
        ),
        "design": {
            "exact_n": list(EXACT_N),
            "mc_n_preregistered": list(MC_N),
            "mc_n_authorized": list(authorized_sizes),
            "replicates_per_mc_n": N_MC,
            "seed_base": SCIENTIFIC_SEED_BASE,
            "seed_formula": "260826000 + n",
            "generator": "numpy.random.Generator(PCG64)",
            "thinning_masks_simulated": False,
            "hypothesis_tests": False,
            "p_values": False,
        },
        "source_validation": {
            key: value for key, value in source_validation.items() if key != "prior_preflight"
        },
        "exact_baseline_reproduction": "PASS" if exact_passed else "FAIL",
        "engineering_gate": list(engineering_gate),
        "controls": controls,
        "results": list(rows),
        "observed_structure": {
            "scope": "finite sampled n values only",
            "E_hat": _trend(mc_rows, "E_hat"),
            "U_hat": _trend(mc_rows, "U_hat"),
            "U_star_hat": _trend(mc_rows, "U_star_hat"),
            "G_hat": _trend(mc_rows, "G_hat"),
        },
        "extension_preflight": {
            "LARGE_N_EXTENSION_ENGINEERING_FEASIBLE": (
                "YES"
                if not any(int(row["backend_failures"]) for row in mc_rows)
                and max(float(row["p95_time_ms"]) for row in mc_rows) <= 250
                else "NO"
            ),
            "larger_sizes_executed": False,
        },
        "artifacts": {CSV_FILENAME: {"sha256": csv_digest, "phase": PHASE}},
        "provenance": {
            "runner": "emergencia/p1a_large_n_orbital_baseline_d2.py",
            "runner_sha256": _sha256(Path(__file__)),
            "backend_wrapper": "emergencia/p1a_orbital_backend_preflight_d2.py",
            "backend_wrapper_sha256": _sha256(Path(orbital.__file__)),
        },
        "claim_ceiling": (
            "post-hoc exploratory finite-n description through n=32; no asymptotic law, "
            "convergence, phase transition, RG, universality, or n->infinity claim"
        ),
    }


def write_artifacts(
    rows: Sequence[dict[str, object]],
    source_validation: dict[str, object],
    exact_passed: bool,
    engineering_gate: Sequence[dict[str, object]],
    authorized_sizes: Sequence[int],
    controls: dict[str, str],
) -> list[tuple[Path, str]]:
    csv_path = RESULTS_DIR / CSV_FILENAME
    json_path = RESULTS_DIR / JSON_FILENAME
    targets = (
        csv_path,
        csv_path.with_suffix(csv_path.suffix + ".sha256"),
        json_path,
        json_path.with_suffix(json_path.suffix + ".sha256"),
    )
    if any(path.exists() for path in targets):
        raise FileExistsError("refusing to overwrite a large-n baseline artifact")
    csv_digest = comparison._write_with_sidecar(csv_path, _rows_to_csv(rows), overwrite=False)
    summary = payload(
        rows,
        source_validation,
        exact_passed,
        engineering_gate,
        authorized_sizes,
        controls,
        csv_digest,
    )
    encoded = (json.dumps(summary, indent=2, sort_keys=True) + "\n").encode("utf-8")
    json_digest = comparison._write_with_sidecar(json_path, encoded, overwrite=False)
    return [(csv_path, csv_digest), (json_path, json_digest)]


def run_all(*, write: bool) -> tuple[list[dict[str, object]], dict[str, object]]:
    source_validation = validate_sources()
    exact_raw, exact_passed = run_exact_control()
    if not exact_passed:
        raise RuntimeError("IMPLEMENTATION_INVALID: exact baseline reproduction failed")
    engineering_gate, authorized_sizes = run_engineering_gate(source_validation)
    scientific_raw = run_scientific(authorized_sizes)
    rows = [summarize(raw) for raw in (*exact_raw, *scientific_raw)]
    controls = validate_rows(rows, exact_passed)
    csv_digest = hashlib.sha256(_rows_to_csv(rows)).hexdigest()
    summary = payload(
        rows,
        source_validation,
        exact_passed,
        engineering_gate,
        authorized_sizes,
        controls,
        csv_digest,
    )
    if write:
        for path, digest in write_artifacts(
            rows,
            source_validation,
            exact_passed,
            engineering_gate,
            authorized_sizes,
            controls,
        ):
            print(f"WROTE {path} sha256={digest}", flush=True)
    print(json.dumps(summary, indent=2, sort_keys=True), flush=True)
    return rows, summary


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--write-artifacts", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    print(f"PHASE={PHASE}")
    print(f"MC_N={MC_N} N_MC={N_MC} SEED_FORMULA={SCIENTIFIC_SEED_BASE}+n")
    if args.write_artifacts and not args.run:
        raise ValueError("--write-artifacts requires --run")
    if args.run:
        run_all(write=args.write_artifacts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
