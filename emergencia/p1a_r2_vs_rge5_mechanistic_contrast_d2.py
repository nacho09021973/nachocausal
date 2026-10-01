#!/usr/bin/env python3
"""Finite post-hoc contrast of exact-orbit groups R=2 and R>=5.

The runner deterministically reproduces the sealed n=22,24,40 PCG64 samples.
It records only six descriptors frozen in the accompanying contract and refuses
to write artifacts unless the exact R partition reproduces the prior campaign.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import multiprocessing
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_gate_altura_duracion_lex_d2 as bootstrap_source
from emergencia import p1a_large_n_orbital_baseline_d2 as baseline
from emergencia import p1a_orbital_backend_preflight_d2 as orbital
from emergencia import p1a_orbital_multiplicity_d2 as multiplicity


PHASE = "POST_HOC_EXPLORATORY_R2_VS_RGE5_MECHANISTIC_CONTRAST"
SCIENTIFIC_TERMINAL = "R2_RGE5_COMBINATORIAL_CONTRAST_COMPLETED"
N_VALUES = (22, 24, 40)
N_MC = multiplicity.N_MC
SCIENTIFIC_SEED_BASE = multiplicity.SCIENTIFIC_SEED_BASE
INSTANCE_TIMEOUT_S = multiplicity.INSTANCE_TIMEOUT_S
PARALLEL_WORKERS = 3
BOOTSTRAP_REPLICATES = 1_000
BOOTSTRAP_SEED_BASE = 2_608_276_000
BOOTSTRAP_INTERVAL_METHOD = "PERCENTILE_95_LINEAR"

GROUP_R2 = "R_EQ_2"
GROUP_RGE5 = "R_GE_5"
GROUP_ORDER = (GROUP_R2, GROUP_RGE5)
COUNT_ORDER = ("EMPTY", "R_EQ_1", "R_EQ_2", "R_EQ_3_4", "R_GE_5")

OBSERVABLES = (
    "n_maximizers",
    "n_automorphisms",
    "primary_score",
    "secondary_score",
    "mean_orbit_size",
    "max_orbit_size",
)
OBSERVABLE_UNITS = {
    "n_maximizers": "candidates",
    "n_automorphisms": "automorphisms",
    "primary_score": "poset_elements",
    "secondary_score": "poset_elements",
    "mean_orbit_size": "candidates_per_orbit",
    "max_orbit_size": "candidates",
}

HERE = Path(__file__).resolve().parent
RESULTS_DIR = HERE / "resultados"
CONTRACT_PATH = HERE / "P1a_contrato_contraste_mecanistico_r2_rge5_d2.md"
PRIOR_SUMMARY_PATH = RESULTS_DIR / multiplicity.SUMMARY_CSV_FILENAME
PRIOR_LONG_PATH = RESULTS_DIR / multiplicity.LONG_CSV_FILENAME
PRIOR_JSON_PATH = RESULTS_DIR / multiplicity.JSON_FILENAME

SUMMARY_CSV_FILENAME = "p1a_r2_vs_rge5_mechanistic_contrast_summary_d2.csv"
LONG_CSV_FILENAME = "p1a_r2_vs_rge5_mechanistic_contrast_long_d2.csv"
JSON_FILENAME = "p1a_r2_vs_rge5_mechanistic_contrast_resumen.json"

SUMMARY_FIELDS = (
    "PHASE",
    "n",
    "seed",
    "N_total",
    "N_empty",
    "N_R1",
    "N_R2",
    "N_R3_4",
    "N_Rge5",
    "backend_failures",
    "observable",
    "unit",
    "N_group_R2",
    "N_group_Rge5",
    "mu_R2",
    "mu_R2_ci95_low",
    "mu_R2_ci95_high",
    "mu_Rge5",
    "mu_Rge5_ci95_low",
    "mu_Rge5_ci95_high",
    "delta_Rge5_minus_R2",
    "delta_ci95_low",
    "delta_ci95_high",
    "cohen_d",
    "cohen_d_ci95_low",
    "cohen_d_ci95_high",
)

LONG_FIELDS = (
    "PHASE",
    "n",
    "seed",
    "sample_index",
    "group",
    "R",
    "observable",
    "value",
)


@dataclass(frozen=True)
class DescriptorRecord:
    sample_index: int
    group: str
    r: int
    values: tuple[float, ...]


@dataclass(frozen=True)
class SizeResult:
    n: int
    seed: int
    total: int
    counts: tuple[tuple[str, int], ...]
    records: tuple[DescriptorRecord, ...]
    backend_failures: int

    @property
    def counter(self) -> Counter[str]:
        return Counter(dict(self.counts))


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def scientific_seed(n: int) -> int:
    if n not in N_VALUES:
        raise ValueError(f"scientific seed requested outside {N_VALUES}")
    return SCIENTIFIC_SEED_BASE + n


def bootstrap_seed(n: int) -> int:
    if n not in N_VALUES:
        raise ValueError(f"bootstrap seed requested outside {N_VALUES}")
    return BOOTSTRAP_SEED_BASE + n


def _prior_partition() -> dict[int, Counter[str]]:
    empty: dict[int, int] = {}
    with PRIOR_SUMMARY_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            n = int(row["n"])
            if n in N_VALUES:
                empty[n] = int(row["N_empty"])
    r_counts: dict[int, Counter[int]] = defaultdict(Counter)
    with PRIOR_LONG_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            n = int(row["n"])
            if n in N_VALUES:
                r_counts[n][int(row["r"])] = int(row["count"])
    expected: dict[int, Counter[str]] = {}
    for n in N_VALUES:
        if n not in empty or not r_counts[n]:
            raise RuntimeError(f"prior multiplicity partition is incomplete at n={n}")
        counts = r_counts[n]
        expected[n] = Counter(
            {
                "EMPTY": empty[n],
                "R_EQ_1": counts[1],
                "R_EQ_2": counts[2],
                "R_EQ_3_4": counts[3] + counts[4],
                "R_GE_5": sum(count for r, count in counts.items() if r >= 5),
            }
        )
        if sum(expected[n].values()) != N_MC:
            raise RuntimeError(f"prior partition does not sum to N_MC at n={n}")
    return expected


def validate_sources() -> dict[str, object]:
    digests = {
        path.name: baseline._verify_sidecar(path)
        for path in (PRIOR_SUMMARY_PATH, PRIOR_LONG_PATH, PRIOR_JSON_PATH)
    }
    prior = json.loads(PRIOR_JSON_PATH.read_text(encoding="utf-8"))
    if prior["result_status"] != multiplicity.SCIENTIFIC_TERMINAL:
        raise RuntimeError("prior orbital-multiplicity campaign is not complete")
    wrapper_digest = _sha256(Path(orbital.__file__))
    if wrapper_digest != prior["provenance"]["backend_wrapper_sha256"]:
        raise RuntimeError("VF2 wrapper changed after multiplicity campaign")
    design = prior["design"]
    if (
        int(design["replicates_per_scientific_n"]) != N_MC
        or int(design["seed_base"]) != SCIENTIFIC_SEED_BASE
        or not set(N_VALUES).issubset(set(int(n) for n in design["scientific_n"]))
    ):
        raise RuntimeError("prior sample design does not contain the frozen contrast")
    return {
        "artifact_digests": digests,
        "contract_sha256": _sha256(CONTRACT_PATH),
        "backend_wrapper_sha256": wrapper_digest,
        "backend_wrapper_byte_identical": True,
        "prior_partition": _prior_partition(),
    }


def classify_r(result: orbital.BackendResult) -> str:
    if result.status == orbital.STATUS_EMPTY:
        return "EMPTY"
    r = result.n_orbits_on_m
    if not isinstance(r, int) or r < 1:
        raise RuntimeError("nonempty backend outcome lacks certified exact R")
    if r == 1:
        return "R_EQ_1"
    if r == 2:
        return "R_EQ_2"
    if r in (3, 4):
        return "R_EQ_3_4"
    return "R_GE_5"


def descriptor_values(
    permutation: Sequence[int], result: orbital.BackendResult
) -> tuple[float, ...]:
    r = result.n_orbits_on_m
    if not isinstance(r, int) or r < 2:
        raise ValueError("descriptors are only materialized for exact R>=2")
    if (
        not result.automorphism_enumeration_complete
        or result.n_automorphisms is None
        or result.orbits is None
    ):
        raise RuntimeError("used outcome lacks a complete exact orbit partition")
    _, maximizers, score = orbital.materialize_lex_maximizers(permutation)
    if maximizers != result.maximizers:
        raise RuntimeError("descriptor access changed the exact maximizer set")
    if score is None:
        raise RuntimeError("nonempty used outcome lacks its exact maximum score")
    orbit_sizes = tuple(sorted((len(orbit) for orbit in result.orbits), reverse=True))
    if len(orbit_sizes) != r or sum(orbit_sizes) != result.n_maximizers:
        raise RuntimeError("exact orbit sizes do not partition M(C)")
    values = (
        float(result.n_maximizers),
        float(result.n_automorphisms),
        float(score[0]),
        float(score[1]),
        result.n_maximizers / r,
        float(max(orbit_sizes)),
    )
    if len(values) != len(OBSERVABLES) or not all(math.isfinite(x) for x in values):
        raise RuntimeError("invalid frozen descriptor vector")
    return values


def _uniform_permutations(n: int, replicates: int, seed: int) -> Iterable[tuple[int, ...]]:
    yield from baseline._uniform_permutations(n, replicates, seed)


def run_size(n: int) -> SizeResult:
    seed = scientific_seed(n)
    counts: Counter[str] = Counter()
    records: list[DescriptorRecord] = []
    print(f"R2_VS_RGE5 n={n} replicates={N_MC} seed={seed} START", flush=True)
    for sample_index, permutation in enumerate(
        _uniform_permutations(n, N_MC, seed), start=1
    ):
        result = orbital.evaluate_orbital_backend(
            permutation, complete_orbits=False, timeout_s=INSTANCE_TIMEOUT_S
        )
        if result.status == orbital.STATUS_BACKEND_FAILURE:
            raise RuntimeError(
                f"BACKEND_FAILURE n={n} sample={sample_index}: "
                f"{result.error_type}: {result.error_message}"
            )
        label = classify_r(result)
        counts[label] += 1
        if label in (GROUP_R2, GROUP_RGE5):
            values = descriptor_values(permutation, result)
            records.append(
                DescriptorRecord(
                    sample_index=sample_index,
                    group=label,
                    r=int(result.n_orbits_on_m),
                    values=values,
                )
            )
        if sample_index % 25_000 == 0:
            print(f"R2_VS_RGE5 n={n} progress={sample_index}/{N_MC}", flush=True)
    if sum(counts.values()) != N_MC:
        raise RuntimeError(f"classification partition failed at n={n}")
    if len(records) != counts[GROUP_R2] + counts[GROUP_RGE5]:
        raise RuntimeError(f"used record count failed at n={n}")
    return SizeResult(
        n=n,
        seed=seed,
        total=N_MC,
        counts=tuple((label, counts[label]) for label in COUNT_ORDER),
        records=tuple(records),
        backend_failures=0,
    )


def run_scientific() -> list[SizeResult]:
    context = multiprocessing.get_context("fork")
    results: dict[int, SizeResult] = {}
    with ProcessPoolExecutor(max_workers=PARALLEL_WORKERS, mp_context=context) as executor:
        futures = {executor.submit(run_size, n): n for n in N_VALUES}
        for future in as_completed(futures):
            n = futures[future]
            results[n] = future.result()
            print(f"R2_VS_RGE5 n={n} COMPLETE", flush=True)
    return [results[n] for n in N_VALUES]


def _arrays(result: SizeResult) -> tuple[np.ndarray, np.ndarray]:
    by_group = {
        group: np.asarray(
            [record.values for record in result.records if record.group == group],
            dtype=np.float64,
        )
        for group in GROUP_ORDER
    }
    for group, array in by_group.items():
        if array.ndim != 2 or array.shape[1] != len(OBSERVABLES) or len(array) < 2:
            raise RuntimeError(f"insufficient descriptor matrix for {group} at n={result.n}")
    return by_group[GROUP_R2], by_group[GROUP_RGE5]


def point_statistics(
    r2: np.ndarray, rge5: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if r2.ndim != 2 or rge5.ndim != 2 or r2.shape[1] != rge5.shape[1]:
        raise ValueError("group matrices must be two-dimensional with matching columns")
    mu2 = r2.mean(axis=0)
    mu5 = rge5.mean(axis=0)
    delta = mu5 - mu2
    var2 = r2.var(axis=0, ddof=1)
    var5 = rge5.var(axis=0, ddof=1)
    pooled_var = ((len(r2) - 1) * var2 + (len(rge5) - 1) * var5) / (
        len(r2) + len(rge5) - 2
    )
    d = np.full(r2.shape[1], np.nan, dtype=np.float64)
    positive = pooled_var > 0
    d[positive] = delta[positive] / np.sqrt(pooled_var[positive])
    return mu2, mu5, delta, d


def _weighted_group_stats(
    values: np.ndarray, counts: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    total = int(counts.sum())
    mean = (counts[:, None] * values).sum(axis=0) / total
    sumsq = (counts[:, None] * values * values).sum(axis=0)
    variance = (sumsq - total * mean * mean) / (total - 1)
    return mean, np.maximum(variance, 0.0)


def bootstrap_statistics(
    r2: np.ndarray,
    rge5: np.ndarray,
    *,
    seed: int,
    replicates: int = BOOTSTRAP_REPLICATES,
) -> dict[str, tuple[np.ndarray, np.ndarray]]:
    if r2.ndim != 2 or rge5.ndim != 2 or r2.shape[1] != rge5.shape[1]:
        raise ValueError("group matrices must be two-dimensional with matching columns")
    n_observables = r2.shape[1]
    unique2, counts2 = np.unique(r2, axis=0, return_counts=True)
    unique5, counts5 = np.unique(rge5, axis=0, return_counts=True)
    n2 = len(r2)
    n5 = len(rge5)
    rng = np.random.Generator(np.random.PCG64(seed))
    samples = {
        name: np.full((replicates, n_observables), np.nan, dtype=np.float64)
        for name in ("mu_R2", "mu_Rge5", "delta", "cohen_d")
    }
    for replicate in range(replicates):
        draw2 = rng.multinomial(n2, counts2 / n2)
        draw5 = rng.multinomial(n5, counts5 / n5)
        mu2, var2 = _weighted_group_stats(unique2, draw2)
        mu5, var5 = _weighted_group_stats(unique5, draw5)
        delta = mu5 - mu2
        pooled_var = ((n2 - 1) * var2 + (n5 - 1) * var5) / (n2 + n5 - 2)
        d = np.full(n_observables, np.nan, dtype=np.float64)
        positive = pooled_var > 0
        d[positive] = delta[positive] / np.sqrt(pooled_var[positive])
        samples["mu_R2"][replicate] = mu2
        samples["mu_Rge5"][replicate] = mu5
        samples["delta"][replicate] = delta
        samples["cohen_d"][replicate] = d
    intervals: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    for name, matrix in samples.items():
        lows = np.full(n_observables, np.nan, dtype=np.float64)
        highs = np.full(n_observables, np.nan, dtype=np.float64)
        for index in range(n_observables):
            finite = matrix[:, index][np.isfinite(matrix[:, index])]
            if len(finite):
                lows[index], highs[index] = bootstrap_source.percentile_interval(finite)
        intervals[name] = (lows, highs)
    return intervals


def _number(value: float | int | None) -> str:
    if value is None or (isinstance(value, float) and not math.isfinite(value)):
        return "NA"
    if isinstance(value, int):
        return str(value)
    return format(float(value), ".17g")


def summarize(result: SizeResult) -> list[dict[str, object]]:
    r2, rge5 = _arrays(result)
    mu2, mu5, delta, d = point_statistics(r2, rge5)
    intervals = bootstrap_statistics(r2, rge5, seed=bootstrap_seed(result.n))
    counts = result.counter
    rows: list[dict[str, object]] = []
    for index, observable in enumerate(OBSERVABLES):
        row: dict[str, object] = {
            "PHASE": PHASE,
            "n": result.n,
            "seed": result.seed,
            "N_total": result.total,
            "N_empty": counts["EMPTY"],
            "N_R1": counts["R_EQ_1"],
            "N_R2": counts["R_EQ_2"],
            "N_R3_4": counts["R_EQ_3_4"],
            "N_Rge5": counts["R_GE_5"],
            "backend_failures": result.backend_failures,
            "observable": observable,
            "unit": OBSERVABLE_UNITS[observable],
            "N_group_R2": len(r2),
            "N_group_Rge5": len(rge5),
            "mu_R2": _number(mu2[index]),
            "mu_Rge5": _number(mu5[index]),
            "delta_Rge5_minus_R2": _number(delta[index]),
            "cohen_d": _number(d[index]),
        }
        for prefix, interval_name in (
            ("mu_R2", "mu_R2"),
            ("mu_Rge5", "mu_Rge5"),
            ("delta", "delta"),
            ("cohen_d", "cohen_d"),
        ):
            low, high = intervals[interval_name]
            row[f"{prefix}_ci95_low"] = _number(low[index])
            row[f"{prefix}_ci95_high"] = _number(high[index])
        if set(row) != set(SUMMARY_FIELDS):
            raise RuntimeError(
                f"summary schema mismatch missing={set(SUMMARY_FIELDS)-set(row)} "
                f"extra={set(row)-set(SUMMARY_FIELDS)}"
            )
        rows.append(row)
    return rows


def _csv_bytes(rows: Iterable[Mapping[str, object]], fields: Sequence[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def long_rows(results: Sequence[SizeResult]) -> Iterable[dict[str, object]]:
    for result in results:
        for record in result.records:
            for observable, value in zip(OBSERVABLES, record.values):
                yield {
                    "PHASE": PHASE,
                    "n": result.n,
                    "seed": result.seed,
                    "sample_index": record.sample_index,
                    "group": record.group,
                    "R": record.r,
                    "observable": observable,
                    "value": _number(value),
                }


def validate_long_recomposition(
    encoded: bytes, summary_rows: Sequence[Mapping[str, object]]
) -> None:
    values: dict[tuple[int, str, str], list[float]] = defaultdict(list)
    reader = csv.DictReader(io.StringIO(encoded.decode("utf-8")))
    for row in reader:
        values[(int(row["n"]), row["group"], row["observable"])].append(
            float(row["value"])
        )
    by_n_observable = {
        (int(row["n"]), str(row["observable"])): row for row in summary_rows
    }
    for n in N_VALUES:
        matrices = {}
        for group in GROUP_ORDER:
            columns = [values[(n, group, observable)] for observable in OBSERVABLES]
            lengths = {len(column) for column in columns}
            if len(lengths) != 1:
                raise RuntimeError("long artifact lost configuration-grain descriptors")
            # ``.T`` of a column stack is F-contiguous, and ``var(axis=0)``
            # accumulates in a layout-dependent order; that shifted ``cohen_d``
            # by ~1e-13 on bit-identical data.  Match the summary path's
            # C-contiguous layout so the comparison is exact.
            matrices[group] = np.ascontiguousarray(
                np.asarray(columns, dtype=np.float64).T
            )
        mu2, mu5, delta, d = point_statistics(
            matrices[GROUP_R2], matrices[GROUP_RGE5]
        )
        for index, observable in enumerate(OBSERVABLES):
            row = by_n_observable[(n, observable)]
            expected = (
                float(row["mu_R2"]),
                float(row["mu_Rge5"]),
                float(row["delta_Rge5_minus_R2"]),
                None if row["cohen_d"] == "NA" else float(row["cohen_d"]),
            )
            observed = (mu2[index], mu5[index], delta[index], d[index])
            for left, right in zip(expected, observed):
                if left is None:
                    if math.isfinite(float(right)):
                        raise RuntimeError("long recomposition changed NA Cohen d")
                elif not math.isclose(left, float(right), rel_tol=1e-13, abs_tol=1e-13):
                    raise RuntimeError("long recomposition disagrees with summary points")


def validate_results(
    results: Sequence[SizeResult],
    summary_rows: Sequence[Mapping[str, object]],
    long_data: bytes,
    source_validation: Mapping[str, object],
) -> dict[str, str]:
    expected = source_validation["prior_partition"]
    assert isinstance(expected, dict)
    controls = {
        "BACKEND_FAILURES": "0",
        "EXACT_R_FROM_N_ORBITS_ON_M": "PASS",
        "COUNTS_PARTITION_TOTAL": "PASS",
        "PRIOR_COUNTS_REPRODUCED": "PASS",
        "COMPLETE_AUTOMORPHISM_ENUMERATION_FOR_USED": "PASS",
        "ORBIT_SIZES_PARTITION_M": "PASS",
        "MAXIMIZER_SCORE_REACCESS_MATCH": "PASS",
        "DESCRIPTOR_REDUCTION_DETERMINISTIC": "PASS",
        "LONG_RECOMPOSITION": "PASS",
    }
    for result in results:
        if result.backend_failures or sum(result.counter.values()) != result.total:
            controls["COUNTS_PARTITION_TOTAL"] = "FAIL"
        if result.counter != Counter(expected[result.n]):
            controls["PRIOR_COUNTS_REPRODUCED"] = "FAIL"
        if len(result.records) != result.counter[GROUP_R2] + result.counter[GROUP_RGE5]:
            controls["COUNTS_PARTITION_TOTAL"] = "FAIL"
    try:
        validate_long_recomposition(long_data, summary_rows)
    except Exception:
        controls["LONG_RECOMPOSITION"] = "FAIL"
        raise
    if any(value == "FAIL" for value in controls.values()):
        raise RuntimeError(f"mechanistic contrast hard guard failed: {controls}")
    return controls


def report_payload(
    results: Sequence[SizeResult],
    summary_rows: Sequence[Mapping[str, object]],
    controls: Mapping[str, str],
    source_validation: Mapping[str, object],
    summary_digest: str,
    long_digest: str,
) -> dict[str, object]:
    return {
        "artifact_schema": "P1A_R2_VS_RGE5_MECHANISTIC_CONTRAST_D2_V1",
        "phase": PHASE,
        "result_status": SCIENTIFIC_TERMINAL,
        "design": {
            "n": list(N_VALUES),
            "window_n": [22, 24],
            "control_n": 40,
            "groups": list(GROUP_ORDER),
            "excluded": ["EMPTY", "R_EQ_1", "R_EQ_3_4"],
            "observables": list(OBSERVABLES),
            "replicates_per_n": N_MC,
            "scientific_seed_formula": "260828000+n",
            "bootstrap_replicates": BOOTSTRAP_REPLICATES,
            "bootstrap_seed_formula": "2608276000+n",
            "bootstrap_unit": "configuration/permutation",
            "standardized_separation": "Cohen d with pooled sample variance",
            "hypothesis_tests": False,
            "p_values": False,
        },
        "source_validation": {
            key: value
            for key, value in source_validation.items()
            if key != "prior_partition"
        },
        "sample_counts": [
            {"n": result.n, **dict(result.counts)} for result in results
        ],
        "controls": dict(controls),
        "results": list(summary_rows),
        "artifacts": {
            SUMMARY_CSV_FILENAME: {"sha256": summary_digest, "phase": PHASE},
            LONG_CSV_FILENAME: {"sha256": long_digest, "phase": PHASE},
        },
        "provenance": {
            "contract": f"emergencia/{CONTRACT_PATH.name}",
            "contract_sha256": _sha256(CONTRACT_PATH),
            "runner": "emergencia/p1a_r2_vs_rge5_mechanistic_contrast_d2.py",
            "runner_sha256": _sha256(Path(__file__)),
            "backend_wrapper": "emergencia/p1a_orbital_backend_preflight_d2.py",
            "backend_wrapper_sha256": _sha256(Path(orbital.__file__)),
            "prior_multiplicity_runner_sha256": _sha256(Path(multiplicity.__file__)),
            "bootstrap_reference": "emergencia/p1a_gate_altura_duracion_lex_d2.py",
            "bootstrap_reference_sha256": _sha256(Path(bootstrap_source.__file__)),
        },
        "claim_ceiling": (
            "finite-n post-hoc exploratory descriptor contrast only; distinguish a "
            "general R>=5 property from window-specific strengthening; no causal, "
            "mechanism-proved, transition, critical-scale, RG, universal, "
            "thermodynamic, or asymptotic claim"
        ),
    }


def write_artifacts(
    results: Sequence[SizeResult],
    summary_rows: Sequence[Mapping[str, object]],
    long_data: bytes,
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
        raise FileExistsError("refusing to overwrite a mechanistic-contrast artifact")
    summary_data = _csv_bytes(summary_rows, SUMMARY_FIELDS)
    summary_digest = comparison._write_with_sidecar(
        summary_path, summary_data, overwrite=False
    )
    long_digest = comparison._write_with_sidecar(long_path, long_data, overwrite=False)
    payload = report_payload(
        results,
        summary_rows,
        controls,
        source_validation,
        summary_digest,
        long_digest,
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
    results = run_scientific()
    summary_rows = [row for result in results for row in summarize(result)]
    long_data = _csv_bytes(long_rows(results), LONG_FIELDS)
    controls = validate_results(results, summary_rows, long_data, source_validation)
    summary_digest = hashlib.sha256(_csv_bytes(summary_rows, SUMMARY_FIELDS)).hexdigest()
    long_digest = hashlib.sha256(long_data).hexdigest()
    payload = report_payload(
        results,
        summary_rows,
        controls,
        source_validation,
        summary_digest,
        long_digest,
    )
    if write:
        for path, digest in write_artifacts(
            results, summary_rows, long_data, controls, source_validation
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
        f"N_VALUES={N_VALUES} N_MC={N_MC} OBSERVABLES={OBSERVABLES} "
        f"BOOTSTRAP={BOOTSTRAP_REPLICATES} R_EXACT=YES"
    )
    if args.write_artifacts and not args.run:
        raise ValueError("--write-artifacts requires --run")
    if args.run:
        run_all(write=args.write_artifacts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
