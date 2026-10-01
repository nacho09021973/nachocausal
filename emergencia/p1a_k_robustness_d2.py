#!/usr/bin/env python3
"""K-robustness of the 22-24 competition peak, under a paired design.

The admissibility floor ``K0`` of the sealed selector ``MIN_COVERAGE_LEX`` is
swept over ``K in {2,3,4,5}`` while every other ingredient is held fixed.  The
seed depends only on ``n``, so the four arms re-score *the same* permutations
and the comparison carries no sampling noise.

Nothing sealed is edited.  ``K`` is injected by parameter, every statistic is
computed by the sealed :mod:`p1a_orbital_multiplicity_d2` helpers, and the
``K=3`` arm must reproduce the sealed campaign exactly or the run is void.

Governed by ``P1a_contrato_robustez_en_K_d2.md``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import multiprocessing
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from itertools import combinations
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import numpy as np

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_large_n_orbital_baseline_d2 as baseline
from emergencia import p1a_orbital_backend_preflight_d2 as orbital
from emergencia import p1a_orbital_multiplicity_d2 as multiplicity
from emergencia import p1a_tie_aut_diagnostic as frozen


PHASE = "POST_HOC_EXPLORATORY_K_ROBUSTNESS_OF_COMPETITION_PEAK"

K_VALUES = (2, 3, 4, 5)
K_ANCHOR = 3
N_VALUES = multiplicity.N_VALUES
N_MC = multiplicity.N_MC
SCIENTIFIC_SEED_BASE = multiplicity.SCIENTIFIC_SEED_BASE
INSTANCE_TIMEOUT_S = multiplicity.INSTANCE_TIMEOUT_S
PARALLEL_WORKERS = multiplicity.PARALLEL_WORKERS

PRIMARY_OBSERVABLE = "P_R_ge_5_given_E"
SECONDARY_OBSERVABLES = ("U_n_star", "Sbar_n_tie", "H_tie_n")

REFERENCE_WINDOW = (22, 24)
MIN_NONEMPTY_FOR_ANALYSIS = 1_000

ARM_MAINTAINS = "MANTIENE"
ARM_SHIFTS = "DESPLAZA"
ARM_UNDETERMINED = "INDETERMINADO"

TERMINAL_ROBUST = "ROBUST_TO_K"
TERMINAL_DEPENDENT = "K_DEPENDENT_LOCATION"
TERMINAL_INCONCLUSIVE = "INCONCLUSIVE_K_ROBUSTNESS"

SEALED_SELECTOR_PATH = Path(sealed.__file__).resolve()
SEALED_SELECTOR_SHA256 = (
    "71594620005e2b83c22874a9a554a254755a468fd1c63429309d2264f79bda2b"
)

HERE = Path(__file__).resolve().parent
RESULTS_DIR = HERE / "resultados"
CONTRACT_PATH = HERE / "P1a_contrato_robustez_en_K_d2.md"
PRIOR_SUMMARY_PATH = RESULTS_DIR / multiplicity.SUMMARY_CSV_FILENAME

SUMMARY_CSV_FILENAME = "p1a_k_robustness_summary_d2.csv"
LONG_CSV_FILENAME = "p1a_k_robustness_long_d2.csv"
JSON_FILENAME = "p1a_k_robustness_resumen.json"

SUMMARY_FIELDS = (
    "PHASE",
    "K",
    "n",
    "seed",
    "N_total",
    "N_empty",
    "N_nonempty",
    "backend_failures",
    "analyzable",
    "P_R_ge_5_given_E",
    "P_R_ge_5_given_E_ci95_low",
    "P_R_ge_5_given_E_ci95_high",
    "U_n_star",
    "U_n_star_ci95_low",
    "U_n_star_ci95_high",
    "Sbar_n_tie",
    "Sbar_n_tie_ci95_low",
    "Sbar_n_tie_ci95_high",
    "H_tie_n",
    "H_tie_n_ci95_low",
    "H_tie_n_ci95_high",
)

LONG_FIELDS = ("PHASE", "K", "n", "seed", "R", "count")


# --------------------------------------------------------------------------
# K-parameterised selector.  Mirrors the sealed
# ``orbital.materialize_lex_maximizers`` with ``sealed.K0`` replaced by ``k``;
# ``validate_selector_equivalence_at_anchor`` proves the two agree at k=3.
# --------------------------------------------------------------------------
def materialize_lex_maximizers_k(permutation: Sequence[int], k: int):
    perm = sealed.validate_permutation(permutation)
    counts, comparable = sealed.interval_count_matrix(perm)
    relation = frozen._as_relation(comparable)
    scored = []
    for a, b, c, d in combinations(range(len(perm)), 4):
        if not (comparable[a, b] and comparable[b, c] and comparable[c, d]):
            continue
        past = int(counts[a, b])
        future = int(counts[c, d])
        if past < k or future < k:
            continue
        scored.append(((a, b, c, d), (min(past, future), past + future)))
    if not scored:
        return relation, (), None
    best_score = max(score for _, score in scored)
    maximizers = tuple(candidate for candidate, score in scored if score == best_score)
    return relation, maximizers, best_score


def evaluate_with_k(permutation: Sequence[int], k: int, *, timeout_s: float | None):
    """Mirror of ``orbital.evaluate_orbital_backend`` with the floor injected."""

    try:
        with orbital._deadline(timeout_s):
            relation, maximizers, _ = materialize_lex_maximizers_k(permutation, k)
            if not maximizers:
                return orbital.STATUS_EMPTY, 0, 0
            partition, _, _ = orbital._orbit_partition_vf2(
                relation, maximizers, complete_orbits=False
            )
            n_orbits = len(partition)
            status = (
                orbital.STATUS_ORBITAL_UNIQUE
                if n_orbits == 1
                else orbital.STATUS_ORBITAL_NONUNIQUE
            )
            return status, len(maximizers), n_orbits
    except Exception as error:  # fail closed, never classify
        raise RuntimeError(f"BACKEND_FAILURE k={k}: {type(error).__name__}: {error}")


def run_size(n: int, k: int) -> tuple[multiplicity.RawMultiplicity, str]:
    seed = multiplicity.scientific_seed(n)
    stream = baseline._uniform_permutations(n, N_MC, seed)
    empty = 0
    r_counts: Counter[int] = Counter()
    digest = hashlib.sha256()
    observed = 0
    print(f"K_ROBUSTNESS K={k} n={n} replicates={N_MC} seed={seed} START", flush=True)
    for observed, permutation in enumerate(stream, start=1):
        digest.update(bytes(permutation))
        status, _, r = evaluate_with_k(permutation, k, timeout_s=INSTANCE_TIMEOUT_S)
        if status == orbital.STATUS_EMPTY:
            empty += 1
        else:
            if not isinstance(r, int) or r < 1:
                raise RuntimeError("nonempty result lacks certified R")
            if (r == 1) != (status == orbital.STATUS_ORBITAL_UNIQUE):
                raise RuntimeError("status and exact orbit multiplicity disagree")
            r_counts[r] += 1
        if observed % 25_000 == 0:
            print(f"K_ROBUSTNESS K={k} n={n} progress={observed}/{N_MC}", flush=True)
    if observed != N_MC:
        raise RuntimeError(f"replicate count mismatch at n={n},k={k}")
    if empty + sum(r_counts.values()) != N_MC:
        raise RuntimeError("EMPTY and R counts do not partition the sample")
    print(f"K_ROBUSTNESS K={k} n={n} COMPLETE", flush=True)
    raw = multiplicity.RawMultiplicity(
        n=n,
        method="MC",
        total=N_MC,
        seed=seed,
        empty=empty,
        r_counts=tuple(sorted(r_counts.items())),
        backend_failures=0,
        median_time_ms=0.0,
        p95_time_ms=0.0,
    )
    return raw, digest.hexdigest()


# --------------------------------------------------------------------------
# Hard controls
# --------------------------------------------------------------------------
def validate_sealed_selector_untouched() -> str:
    digest = hashlib.sha256(SEALED_SELECTOR_PATH.read_bytes()).hexdigest()
    if digest != SEALED_SELECTOR_SHA256:
        raise RuntimeError(
            f"sealed selector changed: {digest} != {SEALED_SELECTOR_SHA256}"
        )
    return digest


def validate_selector_equivalence_at_anchor(sample: int = 400) -> int:
    """At k=K_ANCHOR the injected floor must reproduce the sealed selector."""

    checked = 0
    for n in (8, 12, 20, 24):
        for permutation in baseline._uniform_permutations(n, sample // 4, 4_242 + n):
            mine = materialize_lex_maximizers_k(permutation, K_ANCHOR)
            theirs = orbital.materialize_lex_maximizers(permutation)
            if mine[1] != theirs[1] or mine[2] != theirs[2]:
                raise RuntimeError(
                    f"injected floor disagrees with sealed selector at n={n}"
                )
            checked += 1
    return checked


def _prior_primary() -> dict[int, str]:
    with PRIOR_SUMMARY_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return {
        int(row["n"]): tuple(
            row[field]
            for field in (
                PRIMARY_OBSERVABLE,
                f"{PRIMARY_OBSERVABLE}_ci95_low",
                f"{PRIMARY_OBSERVABLE}_ci95_high",
                *SECONDARY_OBSERVABLES,
            )
        )
        for row in rows
        if int(row["n"]) in N_VALUES
    }


def validate_anchor_reproduces_sealed(rows: Sequence[Mapping[str, object]]) -> None:
    prior = _prior_primary()
    for row in rows:
        if int(row["K"]) != K_ANCHOR:
            continue
        n = int(row["n"])
        observed = tuple(
            str(row[field])
            for field in (
                PRIMARY_OBSERVABLE,
                f"{PRIMARY_OBSERVABLE}_ci95_low",
                f"{PRIMARY_OBSERVABLE}_ci95_high",
                *SECONDARY_OBSERVABLES,
            )
        )
        if observed != prior[n]:
            raise RuntimeError(
                f"K={K_ANCHOR} arm does not reproduce the sealed campaign at n={n}"
            )


# --------------------------------------------------------------------------
# Localisation criterion (contract section 5)
# --------------------------------------------------------------------------
def operational_plateau(
    points: Mapping[int, tuple[float, float, float]]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return (argmax set, OPERATIONAL_PLATEAU).

    Not a 95% confidence set for the argmax; see the contract's frozen warning.
    """

    if not points:
        return (), ()
    best = max(value for value, _, _ in points.values())
    argmax = tuple(sorted(n for n, (value, _, _) in points.items() if value == best))
    lo_ref = min(points[n][1] for n in argmax)
    hi_ref = max(points[n][2] for n in argmax)
    plateau = tuple(
        sorted(n for n, (_, lo, hi) in points.items() if not (hi < lo_ref or lo > hi_ref))
    )
    return argmax, plateau


def classify_arm(
    points: Mapping[int, tuple[float, float, float]], censored: Sequence[int]
) -> tuple[str, tuple[int, ...], tuple[int, ...]]:
    window = set(REFERENCE_WINDOW)
    if window & set(censored):
        argmax, plateau = operational_plateau(points)
        return ARM_UNDETERMINED, argmax, plateau
    argmax, plateau = operational_plateau(points)
    if not plateau:
        return ARM_UNDETERMINED, argmax, plateau
    if not window & set(plateau):
        return ARM_SHIFTS, argmax, plateau
    if set(argmax) <= window:
        return ARM_MAINTAINS, argmax, plateau
    return ARM_UNDETERMINED, argmax, plateau


def decide_terminal(arms: Mapping[int, str], censored: Mapping[int, Sequence[int]]) -> str:
    others = [k for k in K_VALUES if k != K_ANCHOR]
    if any(arms[k] == ARM_SHIFTS for k in others):
        return TERMINAL_DEPENDENT
    if all(arms[k] == ARM_MAINTAINS and not censored[k] for k in others):
        return TERMINAL_ROBUST
    return TERMINAL_INCONCLUSIVE


# --------------------------------------------------------------------------
# Assembly
# --------------------------------------------------------------------------
def summary_row(raw: multiplicity.RawMultiplicity, k: int) -> dict[str, object]:
    full = multiplicity.summarize(raw)
    analyzable = raw.nonempty >= MIN_NONEMPTY_FOR_ANALYSIS
    row: dict[str, object] = {
        "PHASE": PHASE,
        "K": k,
        "n": raw.n,
        "seed": raw.seed,
        "N_total": raw.total,
        "N_empty": raw.empty,
        "N_nonempty": raw.nonempty,
        "backend_failures": raw.backend_failures,
        "analyzable": "YES" if analyzable else "CENSORED",
    }
    for field in (PRIMARY_OBSERVABLE, *SECONDARY_OBSERVABLES):
        row[field] = full[field]
        row[f"{field}_ci95_low"] = full[f"{field}_ci95_low"]
        row[f"{field}_ci95_high"] = full[f"{field}_ci95_high"]
    if set(row) != set(SUMMARY_FIELDS):
        raise RuntimeError("summary schema mismatch")
    return row


def long_rows(results: Mapping[tuple[int, int], multiplicity.RawMultiplicity]):
    for (k, n), raw in sorted(results.items()):
        yield {"PHASE": PHASE, "K": k, "n": n, "seed": raw.seed, "R": 0, "count": raw.empty}
        for r, count in raw.r_counts:
            yield {"PHASE": PHASE, "K": k, "n": n, "seed": raw.seed, "R": r, "count": count}


def _csv_bytes(rows: Iterable[Mapping[str, object]], fields: Sequence[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def validate_long_recomposition(encoded: bytes, rows: Sequence[Mapping[str, object]]) -> None:
    totals: dict[tuple[int, int], int] = {}
    nonempty: dict[tuple[int, int], int] = {}
    for record in csv.DictReader(io.StringIO(encoded.decode("utf-8"))):
        key = (int(record["K"]), int(record["n"]))
        count = int(record["count"])
        totals[key] = totals.get(key, 0) + count
        if int(record["R"]) >= 1:
            nonempty[key] = nonempty.get(key, 0) + count
    for row in rows:
        key = (int(row["K"]), int(row["n"]))
        if totals[key] != int(row["N_total"]):
            raise RuntimeError("long recomposition disagrees with summary totals")
        if nonempty.get(key, 0) != int(row["N_nonempty"]):
            raise RuntimeError("long recomposition disagrees with summary nonempty")


def run_all(*, write: bool) -> dict[str, object]:
    controls: dict[str, object] = {
        "SEALED_SELECTOR_UNTOUCHED": validate_sealed_selector_untouched(),
        "ANCHOR_SELECTOR_EQUIVALENCE_CHECKED": validate_selector_equivalence_at_anchor(),
        "CONTRACT_SHA256": hashlib.sha256(CONTRACT_PATH.read_bytes()).hexdigest(),
    }

    context = multiprocessing.get_context("fork")
    results: dict[tuple[int, int], multiplicity.RawMultiplicity] = {}
    digests: dict[tuple[int, int], str] = {}
    with ProcessPoolExecutor(max_workers=PARALLEL_WORKERS, mp_context=context) as pool:
        futures = {
            pool.submit(run_size, n, k): (k, n) for k in K_VALUES for n in N_VALUES
        }
        for future, key in futures.items():
            raw, digest = future.result()
            results[key] = raw
            digests[key] = digest

    # PAIRED_SAMPLE_IDENTITY: one permutation stream per n, shared by every K.
    for n in N_VALUES:
        seen = {digests[(k, n)] for k in K_VALUES}
        if len(seen) != 1:
            raise RuntimeError(f"paired design broken at n={n}: {seen}")
    controls["PAIRED_SAMPLE_IDENTITY"] = "PASS"
    controls["BACKEND_FAILURES"] = sum(r.backend_failures for r in results.values())

    rows = [summary_row(results[(k, n)], k) for k in K_VALUES for n in N_VALUES]
    validate_anchor_reproduces_sealed(rows)
    controls["K3_ARM_REPRODUCES_SEALED_CAMPAIGN"] = "PASS"

    long_data = _csv_bytes(long_rows(results), LONG_FIELDS)
    validate_long_recomposition(long_data, rows)
    controls["LONG_RECOMPOSITION"] = "PASS"

    arms: dict[int, str] = {}
    censored: dict[int, list[int]] = {}
    geometry: dict[str, object] = {}
    for k in K_VALUES:
        points: dict[int, tuple[float, float, float]] = {}
        censored[k] = []
        for n in N_VALUES:
            row = next(r for r in rows if r["K"] == k and r["n"] == n)
            if row["analyzable"] != "YES" or row[PRIMARY_OBSERVABLE] == "NA":
                censored[k].append(n)
                continue
            points[n] = (
                float(row[PRIMARY_OBSERVABLE]),
                float(row[f"{PRIMARY_OBSERVABLE}_ci95_low"]),
                float(row[f"{PRIMARY_OBSERVABLE}_ci95_high"]),
            )
        verdict, argmax, plateau = classify_arm(points, censored[k])
        arms[k] = verdict
        geometry[str(k)] = {
            "verdict": verdict,
            "argmax": list(argmax),
            "operational_plateau": list(plateau),
            "censored_n": censored[k],
        }

    terminal = decide_terminal(arms, censored)
    payload = {
        "PHASE": PHASE,
        "result_status": terminal,
        "contract": CONTRACT_PATH.name,
        "design": {
            "K_VALUES": list(K_VALUES),
            "K_ANCHOR": K_ANCHOR,
            "N_VALUES": list(N_VALUES),
            "N_MC": N_MC,
            "seed_formula": f"{SCIENTIFIC_SEED_BASE}+n (independent of K)",
            "primary_observable": PRIMARY_OBSERVABLE,
            "secondary_observables": list(SECONDARY_OBSERVABLES),
            "reference_window": list(REFERENCE_WINDOW),
            "min_nonempty_for_analysis": MIN_NONEMPTY_FOR_ANALYSIS,
        },
        "controls": controls,
        "arms": geometry,
        "caveats": (
            "OPERATIONAL_PLATEAU is a plateau definition from overlapping marginal "
            "Wilson intervals; it is NOT a 95% confidence set for the argmax and "
            "carries no nominal coverage. n* is the observed grid extremum only. "
            "The 24/26 boundary of the reference window is operationally fragile "
            "(1.6e-4 in probability in the sealed campaign). No critical-scale, "
            "transition, RG, universality, asymptotic or physical-entropy claim."
        ),
    }
    if write:
        for path, digest in write_artifacts(rows, long_data, payload):
            print(f"WROTE {path} sha256={digest}", flush=True)
    print(json.dumps(payload, indent=2, sort_keys=True), flush=True)
    return payload


def write_artifacts(rows, long_data, payload):
    summary_path = RESULTS_DIR / SUMMARY_CSV_FILENAME
    long_path = RESULTS_DIR / LONG_CSV_FILENAME
    json_path = RESULTS_DIR / JSON_FILENAME
    targets = [summary_path, long_path, json_path]
    if any(p.exists() or p.with_suffix(p.suffix + ".sha256").exists() for p in targets):
        raise FileExistsError("refusing to overwrite a K-robustness artifact")
    summary_digest = comparison._write_with_sidecar(
        summary_path, _csv_bytes(rows, SUMMARY_FIELDS), overwrite=False
    )
    long_digest = comparison._write_with_sidecar(long_path, long_data, overwrite=False)
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    json_digest = comparison._write_with_sidecar(json_path, encoded, overwrite=False)
    return [
        (summary_path, summary_digest),
        (long_path, long_digest),
        (json_path, json_digest),
    ]


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--write-artifacts", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    print(f"PHASE={PHASE}")
    print(
        f"K_VALUES={K_VALUES} N_VALUES={N_VALUES} N_MC={N_MC} "
        f"W={REFERENCE_WINDOW} PRIMARY={PRIMARY_OBSERVABLE} PAIRED=YES"
    )
    if args.write_artifacts and not args.run:
        raise ValueError("--write-artifacts requires --run")
    if args.run:
        run_all(write=args.write_artifacts)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
