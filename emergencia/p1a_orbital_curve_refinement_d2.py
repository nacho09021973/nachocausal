#!/usr/bin/env python3
"""Independent post-hoc refinement of the orbital curve on n=20,22,...,40.

The campaign is deliberately local to the apparent finite-n minimum.  Previous
n=24,32 samples are retained as separate anchors and are never pooled with the new
replicates.  No asymptotic model or hypothesis test is computed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Sequence

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_large_n_orbital_baseline_d2 as baseline
from emergencia import p1a_orbital_backend_preflight_d2 as orbital


PHASE = "POST_HOC_EXPLORATORY_ORBITAL_CURVE_REFINEMENT"
N_VALUES = tuple(range(20, 41, 2))
N_MC = 100_000
SCIENTIFIC_SEED_BASE = 260_828_000
PARALLEL_WORKERS = 4

ENGINEERING_GATE_N = (36, 40)
ENGINEERING_GATE_INSTANCES = 100
ENGINEERING_GATE_SEED_BASE = 260_829_000
ENGINEERING_GATE_P95_MAX_S = 0.25
INSTANCE_TIMEOUT_S = 5.0

HERE = Path(__file__).resolve().parent
RESULTS_DIR = HERE / "resultados"
PRIOR_CSV = RESULTS_DIR / baseline.CSV_FILENAME
PRIOR_JSON = RESULTS_DIR / baseline.JSON_FILENAME
BACKEND_PREFLIGHT = RESULTS_DIR / "p1a_orbital_backend_preflight_resumen.json"
CSV_FILENAME = "p1a_orbital_curve_refinement_d2.csv"
JSON_FILENAME = "p1a_orbital_curve_refinement_resumen.json"
FIELDS = baseline.FIELDS


def scientific_seed(n: int) -> int:
    if n not in N_VALUES:
        raise ValueError(f"scientific seed requested outside {N_VALUES}")
    return SCIENTIFIC_SEED_BASE + n


def engineering_seed(n: int) -> int:
    if n not in ENGINEERING_GATE_N:
        raise ValueError(f"engineering seed requested outside {ENGINEERING_GATE_N}")
    return ENGINEERING_GATE_SEED_BASE + n


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_sources() -> dict[str, object]:
    digests = {
        PRIOR_CSV.name: baseline._verify_sidecar(PRIOR_CSV),
        PRIOR_JSON.name: baseline._verify_sidecar(PRIOR_JSON),
        BACKEND_PREFLIGHT.name: baseline._verify_sidecar(BACKEND_PREFLIGHT),
    }
    prior = json.loads(PRIOR_JSON.read_text(encoding="utf-8"))
    preflight = json.loads(BACKEND_PREFLIGHT.read_text(encoding="utf-8"))
    wrapper_digest = _sha256(Path(orbital.__file__))
    if prior["result_status"] != "LARGE_N_BASELINE_COMPLETED":
        raise RuntimeError("prior large-n baseline is not complete")
    if wrapper_digest != preflight["provenance"]["generator_sha256"]:
        raise RuntimeError("VF2 wrapper changed after exhaustive validation")
    return {
        "artifact_digests": digests,
        "wrapper_sha256": wrapper_digest,
        "wrapper_byte_identical": True,
        "prior_payload": prior,
    }


def run_engineering_gate() -> tuple[list[dict[str, object]], tuple[int, ...]]:
    rows: list[dict[str, object]] = []
    passed: dict[int, bool] = {}
    for n in ENGINEERING_GATE_N:
        seed = engineering_seed(n)
        raw = baseline._accumulate(
            n,
            baseline._uniform_permutations(n, ENGINEERING_GATE_INSTANCES, seed),
            method="ENGINEERING_BENCHMARK",
            replicates=ENGINEERING_GATE_INSTANCES,
            seed=seed,
            timeout_s=INSTANCE_TIMEOUT_S,
        )
        p95 = baseline._p95(raw.timings_s)
        passed[n] = raw.backend_failures == 0 and p95 <= ENGINEERING_GATE_P95_MAX_S
        row = {
            "n": n,
            "instances": ENGINEERING_GATE_INSTANCES,
            "seed": seed,
            "success": ENGINEERING_GATE_INSTANCES - raw.backend_failures,
            "backend_failure": raw.backend_failures,
            "median_time_s": __import__("statistics").median(raw.timings_s),
            "p95_time_s": p95,
            "max_time_s": max(raw.timings_s),
            "p95_gate_s": ENGINEERING_GATE_P95_MAX_S,
            "status": "PASS" if passed[n] else "FAIL",
        }
        rows.append(row)
        print(
            f"ENGINEERING_GATE n={n} failures={raw.backend_failures} "
            f"p95_s={p95:.6f} status={row['status']}",
            flush=True,
        )

    authorized: list[int] = []
    for n in N_VALUES:
        if n <= 32:
            authorized.append(n)
        elif n <= 36 and passed[36]:
            authorized.append(n)
        elif n > 36 and passed[36] and passed[40]:
            authorized.append(n)
    return rows, tuple(authorized)


def _run_scientific_size(n: int) -> baseline.RawCounts:
    seed = scientific_seed(n)
    print(f"REFINEMENT n={n} replicates={N_MC} seed={seed} START", flush=True)
    return baseline._accumulate(
        n,
        baseline._uniform_permutations(n, N_MC, seed),
        method="MONTE_CARLO_REFINEMENT",
        replicates=N_MC,
        seed=seed,
        timeout_s=INSTANCE_TIMEOUT_S,
        progress_every=25_000,
    )


def run_scientific(authorized: Sequence[int]) -> list[baseline.RawCounts]:
    context = multiprocessing.get_context("fork")
    results: dict[int, baseline.RawCounts] = {}
    with ProcessPoolExecutor(max_workers=PARALLEL_WORKERS, mp_context=context) as executor:
        futures = {executor.submit(_run_scientific_size, n): n for n in authorized}
        for future in as_completed(futures):
            n = futures[future]
            results[n] = future.result()
            print(f"REFINEMENT n={n} COMPLETE", flush=True)
    return [results[n] for n in sorted(results)]


def summarize(raw: baseline.RawCounts) -> dict[str, object]:
    row = baseline.summarize(raw)
    row["PHASE"] = PHASE
    return row


def validate_rows(rows: Sequence[dict[str, object]]) -> dict[str, str]:
    failures = sum(int(row["backend_failures"]) for row in rows)
    counts_pass = all(
        int(row["empty_count"])
        + int(row["orbital_unique_count"])
        + int(row["orbital_nonunique_count"])
        + int(row["backend_failures"])
        == N_MC
        for row in rows
    )
    u_le_e = all(int(row["orbital_unique_count"]) <= int(row["nonempty_count"]) for row in rows)
    ratio_pass = all(
        math.isclose(
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
        "ALL_PREREGISTERED_SIZES_COMPLETED": (
            "PASS" if tuple(int(row["n"]) for row in rows) == N_VALUES else "FAIL"
        ),
        "NO_POOLING_WITH_PRIOR_ANCHORS": "PASS",
    }
    if failures or any(value == "FAIL" for value in controls.values()):
        raise RuntimeError(f"refinement hard guard failed: {controls}")
    return controls


def _prior_anchor_rows(source_validation: dict[str, object]) -> dict[int, dict[str, object]]:
    prior = source_validation["prior_payload"]
    assert isinstance(prior, dict)
    return {
        int(row["n"]): row
        for row in prior["results"]
        if row["method"] == "MONTE_CARLO" and int(row["n"]) in (24, 32)
    }


def anchor_comparison(
    rows: Sequence[dict[str, object]], source_validation: dict[str, object]
) -> list[dict[str, object]]:
    prior = _prior_anchor_rows(source_validation)
    current = {int(row["n"]): row for row in rows if int(row["n"]) in (24, 32)}
    comparison_rows: list[dict[str, object]] = []
    for n in (24, 32):
        comparison_rows.append(
            {
                "n": n,
                "prior_seed": int(prior[n]["seed"]),
                "new_seed": int(current[n]["seed"]),
                "pooled": False,
                "prior_U_star_hat": float(prior[n]["U_star_hat"]),
                "new_U_star_hat": float(current[n]["U_star_hat"]),
                "delta_new_minus_prior": (
                    float(current[n]["U_star_hat"]) - float(prior[n]["U_star_hat"])
                ),
            }
        )
    return comparison_rows


def _trend(rows: Sequence[dict[str, object]], field: str) -> str:
    values = [float(row[field]) for row in rows]
    if all(left <= right for left, right in zip(values, values[1:])) and any(
        left < right for left, right in zip(values, values[1:])
    ):
        return "INCREASED"
    if all(left >= right for left, right in zip(values, values[1:])) and any(
        left > right for left, right in zip(values, values[1:])
    ):
        return "DECREASED"
    return "NON_MONOTONE"


def _rows_to_csv(rows: Sequence[dict[str, object]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def report_payload(
    rows: Sequence[dict[str, object]],
    source_validation: dict[str, object],
    gate: Sequence[dict[str, object]],
    authorized: Sequence[int],
    controls: dict[str, str],
    csv_digest: str,
) -> dict[str, object]:
    minimum = min(rows, key=lambda row: float(row["U_star_hat"]))
    maximum_g = max(rows, key=lambda row: float(row["G_hat"]))
    return {
        "artifact_schema": "P1A_ORBITAL_CURVE_REFINEMENT_D2_V1",
        "phase": PHASE,
        "result_status": "ORBITAL_CURVE_REFINEMENT_COMPLETED",
        "design": {
            "n_preregistered": list(N_VALUES),
            "n_authorized": list(authorized),
            "replicates_per_n": N_MC,
            "seed_base": SCIENTIFIC_SEED_BASE,
            "seed_formula": "260828000 + n",
            "parallel_workers": PARALLEL_WORKERS,
            "primary_estimand": "U_star_hat",
            "secondary_fixed_estimands": ["U_hat", "E_hat", "G_hat"],
            "prior_anchor_n": [24, 32],
            "pooling_with_prior": False,
            "hypothesis_tests": False,
            "p_values": False,
            "asymptotic_fit": False,
        },
        "source_validation": {
            key: value for key, value in source_validation.items() if key != "prior_payload"
        },
        "engineering_gate": list(gate),
        "controls": controls,
        "results": list(rows),
        "independent_anchor_comparison": anchor_comparison(rows, source_validation),
        "observed_structure": {
            "scope": "finite n=20,22,...,40 only",
            "E_hat": _trend(rows, "E_hat"),
            "U_hat": _trend(rows, "U_hat"),
            "U_star_hat": _trend(rows, "U_star_hat"),
            "G_hat": _trend(rows, "G_hat"),
            "sampled_minimum_U_star": {
                "n": int(minimum["n"]),
                "value": float(minimum["U_star_hat"]),
            },
            "sampled_maximum_G": {
                "n": int(maximum_g["n"]),
                "value": float(maximum_g["G_hat"]),
            },
        },
        "artifacts": {CSV_FILENAME: {"sha256": csv_digest, "phase": PHASE}},
        "provenance": {
            "runner": "emergencia/p1a_orbital_curve_refinement_d2.py",
            "runner_sha256": _sha256(Path(__file__)),
            "backend_wrapper_sha256": _sha256(Path(orbital.__file__)),
        },
        "claim_ceiling": (
            "independent post-hoc finite-n curve refinement through n=40; no pooling, "
            "asymptotic law, convergence, transition, crossover mechanism, RG, or universality claim"
        ),
    }


def write_artifacts(
    rows: Sequence[dict[str, object]],
    source_validation: dict[str, object],
    gate: Sequence[dict[str, object]],
    authorized: Sequence[int],
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
        raise FileExistsError("refusing to overwrite a curve-refinement artifact")
    csv_data = _rows_to_csv(rows)
    csv_digest = comparison._write_with_sidecar(csv_path, csv_data, overwrite=False)
    report = report_payload(rows, source_validation, gate, authorized, controls, csv_digest)
    encoded = (json.dumps(report, indent=2, sort_keys=True) + "\n").encode("utf-8")
    json_digest = comparison._write_with_sidecar(json_path, encoded, overwrite=False)
    return [(csv_path, csv_digest), (json_path, json_digest)]


def run_all(*, write: bool) -> tuple[list[dict[str, object]], dict[str, object]]:
    source_validation = validate_sources()
    gate, authorized = run_engineering_gate()
    raw_rows = run_scientific(authorized)
    rows = [summarize(raw) for raw in raw_rows]
    controls = validate_rows(rows)
    csv_digest = hashlib.sha256(_rows_to_csv(rows)).hexdigest()
    report = report_payload(rows, source_validation, gate, authorized, controls, csv_digest)
    if write:
        for path, digest in write_artifacts(rows, source_validation, gate, authorized, controls):
            print(f"WROTE {path} sha256={digest}", flush=True)
    print(json.dumps(report, indent=2, sort_keys=True), flush=True)
    return rows, report


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
        f"POOLING_WITH_PRIOR=NO WORKERS={PARALLEL_WORKERS}"
    )
    if args.write_artifacts and not args.run:
        raise ValueError("--write-artifacts requires --run")
    if args.run:
        run_all(write=args.write_artifacts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
