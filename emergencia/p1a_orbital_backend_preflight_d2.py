#!/usr/bin/env python3
"""Engineering-only preflight for an n>9 orbital-uniqueness backend.

The candidate backend is the already-installed NetworkX directed VF2 matcher.  The
strict order relation is encoded as a directed graph, so directed graph
automorphisms are exactly poset automorphisms.  This module does not estimate any
large-n scientific probability and refuses to overwrite its report artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import signal
import statistics
import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from importlib import metadata
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable, Iterator, Sequence

import networkx as nx
from networkx.algorithms.isomorphism import DiGraphMatcher

from emergencia import p1a_enumeracion_simulacion as sealed
from emergencia import p1a_tie_aut_diagnostic as frozen


PHASE = "ORBITAL_BACKEND_PREFLIGHT"
SCIENTIFIC_LARGE_N_RUN = False
BACKEND_NAME = "NetworkX DiGraphMatcher/VF2"
BACKEND_VERSION = metadata.version("networkx")
BACKEND_PROVENANCE = "Debian/Ubuntu package python3-networkx 2.8.8-1ubuntu1"

STATUS_ORBITAL_UNIQUE = "ORBITAL_UNIQUE"
STATUS_ORBITAL_NONUNIQUE = "ORBITAL_NONUNIQUE"
STATUS_EMPTY = "EMPTY"
STATUS_BACKEND_FAILURE = "BACKEND_FAILURE"

EXACT_N = (6, 7, 8, 9)
EXPECTED_TOTAL = sum(math.factorial(n) for n in EXACT_N)

# Frozen before benchmark results are observed.
BENCHMARK_N = (10, 12, 16)
BENCHMARK_INSTANCES = 100
BENCHMARK_SEED = 260_826
BENCHMARK_TIMEOUT_S = 5.0
READY_P95_S = 0.25
READY_MAX_S = 2.0
PROMISING_P95_S = 2.0
PROMISING_MAX_S = BENCHMARK_TIMEOUT_S

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "resultados/p1a_orbital_backend_preflight_resumen.json"

Quadruple = tuple[int, int, int, int]
Relation = tuple[tuple[bool, ...], ...]
Score = tuple[int, int]


@dataclass(frozen=True)
class BackendResult:
    status: str
    n_maximizers: int
    n_orbits_on_m: int | None
    n_automorphisms: int | None
    automorphism_enumeration_complete: bool
    maximizers: tuple[Quadruple, ...]
    orbits: tuple[tuple[Quadruple, ...], ...] | None
    error_type: str | None = None
    error_message: str | None = None


@dataclass(frozen=True)
class BenchmarkRow:
    n: int
    instances: int
    success: int
    backend_failure: int
    median_time: float
    p95_time: float
    max_time: float
    median_n_maximizers: float
    max_n_maximizers: int


class BackendTimeout(TimeoutError):
    """Raised by the fail-closed wall-clock guard."""


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@contextmanager
def _deadline(seconds: float | None) -> Iterator[None]:
    if seconds is None:
        yield
        return
    if seconds <= 0:
        raise ValueError("timeout must be positive")
    previous_handler = signal.getsignal(signal.SIGALRM)

    def alarm_handler(signum, frame):  # type: ignore[no-untyped-def]
        raise BackendTimeout(f"backend exceeded {seconds:g} seconds")

    signal.signal(signal.SIGALRM, alarm_handler)
    previous_timer = signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, *previous_timer)
        signal.signal(signal.SIGALRM, previous_handler)


def materialize_lex_maximizers(
    permutation: Sequence[int],
) -> tuple[Relation, tuple[Quadruple, ...], Score | None]:
    """Unbounded-size copy of the frozen exact definition of M(C), not a proxy."""

    perm = sealed.validate_permutation(permutation)
    counts, comparable = sealed.interval_count_matrix(perm)
    relation = frozen._as_relation(comparable)
    scored: list[tuple[Quadruple, Score]] = []
    for a, b, c, d in combinations(range(len(perm)), 4):
        if not (comparable[a, b] and comparable[b, c] and comparable[c, d]):
            continue
        past = int(counts[a, b])
        future = int(counts[c, d])
        if past < sealed.K0 or future < sealed.K0:
            continue
        scored.append(((a, b, c, d), (min(past, future), past + future)))
    if not scored:
        return relation, (), None
    best_score = max(score for _, score in scored)
    maximizers = tuple(candidate for candidate, score in scored if score == best_score)
    return relation, maximizers, best_score


def relation_to_digraph(relation: Relation) -> nx.DiGraph:
    """Encode every strict-order pair as a directed edge."""

    n = len(relation)
    if n == 0 or any(len(row) != n for row in relation):
        raise ValueError("expected a nonempty square relation")
    graph = nx.DiGraph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from(
        (source, target)
        for source in range(n)
        for target in range(n)
        if relation[source][target]
    )
    return graph


def _find(parent: dict[Quadruple, Quadruple], item: Quadruple) -> Quadruple:
    while parent[item] != item:
        parent[item] = parent[parent[item]]
        item = parent[item]
    return item


def _union(
    parent: dict[Quadruple, Quadruple], left: Quadruple, right: Quadruple
) -> None:
    root_left = _find(parent, left)
    root_right = _find(parent, right)
    if root_left != root_right:
        parent[max(root_left, root_right)] = min(root_left, root_right)


def _orbit_partition_vf2(
    relation: Relation,
    maximizers: tuple[Quadruple, ...],
    *,
    complete_orbits: bool,
) -> tuple[tuple[tuple[Quadruple, ...], ...], int, bool]:
    graph = relation_to_digraph(relation)
    matcher = DiGraphMatcher(graph, graph)
    maximizer_set = set(maximizers)
    parent = {candidate: candidate for candidate in maximizers}
    representative = min(maximizers)
    representative_orbit: set[Quadruple] = set()
    automorphisms_seen = 0

    for mapping in matcher.isomorphisms_iter():
        automorphisms_seen += 1
        for candidate in maximizers:
            image = tuple(mapping[element] for element in candidate)
            if image not in maximizer_set:
                raise RuntimeError("VF2 automorphism image escaped M(C)")
            _union(parent, candidate, image)
            if candidate == representative:
                representative_orbit.add(image)
        if not complete_orbits and representative_orbit == maximizer_set:
            return ((tuple(sorted(maximizers))),), automorphisms_seen, False

    if automorphisms_seen == 0:
        raise RuntimeError("VF2 lost the identity automorphism")
    groups: dict[Quadruple, list[Quadruple]] = {}
    for candidate in maximizers:
        groups.setdefault(_find(parent, candidate), []).append(candidate)
    partition = tuple(sorted(tuple(sorted(group)) for group in groups.values()))
    flattened = [candidate for orbit in partition for candidate in orbit]
    if set(flattened) != maximizer_set or len(flattened) != len(maximizers):
        raise RuntimeError("VF2 orbit partition does not cover M(C) exactly once")
    return partition, automorphisms_seen, True


def evaluate_orbital_backend(
    permutation: Sequence[int],
    *,
    complete_orbits: bool = False,
    timeout_s: float | None = None,
) -> BackendResult:
    """Evaluate r_orb with four fail-closed public states."""

    try:
        with _deadline(timeout_s):
            relation, maximizers, _ = materialize_lex_maximizers(permutation)
            if not maximizers:
                return BackendResult(
                    STATUS_EMPTY, 0, 0, None, True, (), (), None, None
                )
            partition, automorphisms_seen, enumeration_complete = _orbit_partition_vf2(
                relation, maximizers, complete_orbits=complete_orbits
            )
            n_orbits = len(partition)
            status = STATUS_ORBITAL_UNIQUE if n_orbits == 1 else STATUS_ORBITAL_NONUNIQUE
            return BackendResult(
                status=status,
                n_maximizers=len(maximizers),
                n_orbits_on_m=n_orbits,
                n_automorphisms=automorphisms_seen if enumeration_complete else None,
                automorphism_enumeration_complete=enumeration_complete,
                maximizers=maximizers,
                orbits=partition,
            )
    except Exception as error:
        return BackendResult(
            status=STATUS_BACKEND_FAILURE,
            n_maximizers=0,
            n_orbits_on_m=None,
            n_automorphisms=None,
            automorphism_enumeration_complete=False,
            maximizers=(),
            orbits=None,
            error_type=type(error).__name__,
            error_message=str(error),
        )


def _expected_status(diagnostic: frozen.TieAutDiagnostic) -> str:
    if not diagnostic.maximizers:
        return STATUS_EMPTY
    return STATUS_ORBITAL_UNIQUE if diagnostic.n_orbits == 1 else STATUS_ORBITAL_NONUNIQUE


def _comparison_mismatch(
    permutation: tuple[int, ...],
    expected: frozen.TieAutDiagnostic,
    observed: BackendResult,
) -> dict[str, object] | None:
    checks = {
        "status": observed.status == _expected_status(expected),
        "n_maximizers": observed.n_maximizers == expected.n_maximizers,
        "maximizers": observed.maximizers == expected.maximizers,
        "n_orbits_on_m": observed.n_orbits_on_m == expected.n_orbits,
        "orbit_partition": observed.orbits == expected.orbits,
        "group_order": observed.n_automorphisms == expected.n_automorphisms,
    }
    if all(checks.values()):
        return None
    return {
        "permutation": list(permutation),
        "checks": checks,
        "expected": {
            "status": _expected_status(expected),
            "n_maximizers": expected.n_maximizers,
            "n_orbits_on_m": expected.n_orbits,
            "n_automorphisms": expected.n_automorphisms,
            "maximizers": expected.maximizers,
            "orbits": expected.orbits,
        },
        "observed": asdict(observed),
    }


def exhaustive_equivalence() -> tuple[dict[str, object], dict[str, tuple[int, ...]]]:
    counts: dict[int, int] = {}
    first_mismatch: dict[str, object] | None = None
    selected: dict[str, tuple[int, ...]] = {}
    selected_metrics: dict[str, int] = {}

    for n in EXACT_N:
        matched = 0
        for permutation in permutations(range(n)):
            expected = frozen.evaluate_tie_aut(permutation)
            observed = evaluate_orbital_backend(permutation, complete_orbits=True)
            mismatch = _comparison_mismatch(permutation, expected, observed)
            if mismatch is not None:
                mismatch["n"] = n
                first_mismatch = mismatch
                break
            matched += 1

            if expected.maximizers:
                if expected.n_automorphisms == 1 and "AUT_TRIVIAL" not in selected:
                    selected["AUT_TRIVIAL"] = permutation
                if expected.diagnostic_state == frozen.DIAGNOSTIC_TIE_AUT_ONLY and "TIE_AUT_ONLY" not in selected:
                    selected["TIE_AUT_ONLY"] = permutation
                if expected.diagnostic_state == frozen.DIAGNOSTIC_TIE_NONAUT and "TIE_NONAUT" not in selected:
                    selected["TIE_NONAUT"] = permutation
                candidates = {
                    "AUT_LARGE": int(expected.n_automorphisms or 0),
                    "MANY_MAXIMIZERS": expected.n_maximizers,
                    "MANY_ORBITS": expected.n_orbits,
                }
                for label, metric in candidates.items():
                    if metric > selected_metrics.get(label, -1):
                        selected_metrics[label] = metric
                        selected[label] = permutation
        counts[n] = matched
        print(f"EXHAUSTIVE n={n} matched={matched}/{math.factorial(n)}", flush=True)
        if first_mismatch is not None:
            break

    total = sum(counts.values())
    passed = first_mismatch is None and total == EXPECTED_TOTAL
    return {
        "counts": {str(n): counts.get(n, 0) for n in EXACT_N},
        "total": total,
        "expected_total": EXPECTED_TOTAL,
        "backend_equivalence": "PASS" if passed else "FAIL",
        "first_mismatch": first_mismatch,
    }, selected


def adversarial_results(selected: dict[str, tuple[int, ...]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for label in (
        "AUT_TRIVIAL",
        "AUT_LARGE",
        "TIE_AUT_ONLY",
        "TIE_NONAUT",
        "MANY_MAXIMIZERS",
        "MANY_ORBITS",
    ):
        permutation = selected[label]
        expected = frozen.evaluate_tie_aut(permutation)
        observed = evaluate_orbital_backend(permutation, complete_orbits=True)
        rows.append(
            {
                "case": label,
                "n": len(permutation),
                "permutation": "".join(str(value) for value in permutation),
                "expected_diagnostic": expected.diagnostic_state,
                "group_order": expected.n_automorphisms,
                "n_maximizers": expected.n_maximizers,
                "n_orbits_on_m": expected.n_orbits,
                "backend_status": observed.status,
                "match": _comparison_mismatch(permutation, expected, observed) is None,
            }
        )
    return rows


def _fixed_benchmark_permutations(n: int) -> Iterable[tuple[int, ...]]:
    rng = random.Random(BENCHMARK_SEED + n)
    for _ in range(BENCHMARK_INSTANCES):
        yield tuple(rng.sample(range(n), n))


def engineering_benchmark() -> list[BenchmarkRow]:
    rows: list[BenchmarkRow] = []
    for n in BENCHMARK_N:
        timings: list[float] = []
        n_maximizers: list[int] = []
        success = failures = 0
        for permutation in _fixed_benchmark_permutations(n):
            started = time.perf_counter()
            result = evaluate_orbital_backend(
                permutation, complete_orbits=False, timeout_s=BENCHMARK_TIMEOUT_S
            )
            timings.append(time.perf_counter() - started)
            n_maximizers.append(result.n_maximizers)
            if result.status == STATUS_BACKEND_FAILURE:
                failures += 1
            else:
                success += 1
        ordered = sorted(timings)
        p95 = ordered[max(0, math.ceil(0.95 * len(ordered)) - 1)]
        row = BenchmarkRow(
            n=n,
            instances=len(timings),
            success=success,
            backend_failure=failures,
            median_time=statistics.median(timings),
            p95_time=p95,
            max_time=max(timings),
            median_n_maximizers=statistics.median(n_maximizers),
            max_n_maximizers=max(n_maximizers),
        )
        rows.append(row)
        print(
            f"BENCHMARK n={n} instances={row.instances} success={success} "
            f"failures={failures} p95_s={p95:.6f}",
            flush=True,
        )
    return rows


def engineering_verdict(
    equivalence: dict[str, object], benchmark: Sequence[BenchmarkRow]
) -> str:
    if equivalence["backend_equivalence"] != "PASS":
        return "NOT_READY"
    if any(row.backend_failure for row in benchmark):
        return "NOT_READY"
    if all(row.p95_time <= READY_P95_S and row.max_time <= READY_MAX_S for row in benchmark):
        return "READY"
    if all(
        row.p95_time <= PROMISING_P95_S and row.max_time < PROMISING_MAX_S
        for row in benchmark
    ):
        return "PROMISING_BUT_EXPENSIVE"
    return "NOT_READY"


def report_payload(
    equivalence: dict[str, object],
    adversarial: Sequence[dict[str, object]],
    benchmark: Sequence[BenchmarkRow],
) -> dict[str, object]:
    verdict = engineering_verdict(equivalence, benchmark)
    return {
        "artifact_schema": "P1A_ORBITAL_BACKEND_PREFLIGHT_D2_V1",
        "phase": PHASE,
        "scientific_large_n_run": False,
        "backend": {
            "name": BACKEND_NAME,
            "version": BACKEND_VERSION,
            "provenance": BACKEND_PROVENANCE,
            "route": "ORBITS",
            "poset_encoding": "directed graph of the complete strict-order relation",
            "automorphism_group_preserved": True,
            "full_group_required_for_r_orb": False,
            "installed_alternatives": [],
        },
        "predeclared_benchmark": {
            "n": list(BENCHMARK_N),
            "instances_per_n": BENCHMARK_INSTANCES,
            "seed": BENCHMARK_SEED,
            "timeout_s": BENCHMARK_TIMEOUT_S,
            "ready_p95_s": READY_P95_S,
            "ready_max_s": READY_MAX_S,
            "promising_p95_s": PROMISING_P95_S,
            "promising_max_s": PROMISING_MAX_S,
        },
        "exhaustive_equivalence": equivalence,
        "adversarial_cases": list(adversarial),
        "benchmark": [asdict(row) for row in benchmark],
        "engineering_verdict": verdict,
        "scientific_guard": {
            "large_n_u_estimated": False,
            "large_n_e_estimated": False,
            "state_unique_used_as_proxy": False,
            "frozen_artifacts_overwritten": False,
        },
        "provenance": {
            "generator": "emergencia/p1a_orbital_backend_preflight_d2.py",
            "generator_sha256": _sha256(Path(__file__)),
            "frozen_instrument": "emergencia/p1a_tie_aut_diagnostic.py",
            "frozen_instrument_sha256": _sha256(Path(frozen.__file__)),
            "randomness": "benchmark only; fixed local PRNG seed",
        },
    }


def write_report(payload: dict[str, object], path: Path = DEFAULT_OUTPUT) -> tuple[Path, str]:
    sidecar = path.with_suffix(path.suffix + ".sha256")
    if path.exists() or sidecar.exists():
        raise FileExistsError(f"refusing to overwrite {path} or its sidecar")
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    digest = hashlib.sha256(encoded).hexdigest()
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    temporary.write_bytes(encoded)
    temporary.replace(path)
    sidecar.write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return path, digest


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-preflight", action="store_true")
    parser.add_argument("--write-artifact", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    print(f"PHASE={PHASE}")
    print(f"BACKEND={BACKEND_NAME} VERSION={BACKEND_VERSION}")
    print("ROUTE=ORBITS FULL_AUT_GROUP_REQUIRED=NO")
    if not args.run_preflight:
        return 0
    equivalence, selected = exhaustive_equivalence()
    adversarial: list[dict[str, object]] = []
    benchmark: list[BenchmarkRow] = []
    if equivalence["backend_equivalence"] == "PASS":
        adversarial = adversarial_results(selected)
        benchmark = engineering_benchmark()
    payload = report_payload(equivalence, adversarial, benchmark)
    print(json.dumps(payload, indent=2, sort_keys=True))
    if args.write_artifact:
        path, digest = write_report(payload)
        print(f"WROTE {path} sha256={digest}")
    return 0 if equivalence["backend_equivalence"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
