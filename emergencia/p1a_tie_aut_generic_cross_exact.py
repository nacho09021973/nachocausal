#!/usr/bin/env python3
"""Exact finite-core falsifier for generic TIE/Aut cross repairability.

This permanent phase-2 runner scans the labelled permutation measure on S_7,
S_8, and S_9.  It filters the existing MIN_COVERAGE_LEX ties, retains exactly
the TIE_NONAUT cores, and computes

    a(kappa) = #{x : r(D_x(kappa)) = 1}.

The precommitted falsifier is ``min a == 0``.  Its occurrence is reported, not
asserted: one witness would challenge the linear outgoing-degree route but would
not by itself control the other transposition classes.  Absence through n=9 is
finite evidence only and is not promoted to a theorem or asymptotic claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from collections import Counter
from dataclasses import dataclass, field
from itertools import permutations
from pathlib import Path
from typing import Iterable, Sequence

from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_tie_aut_diagnostic as tie_aut
from emergencia import p1a_tie_aut_generic_cross as generic_cross


EXACT_N = (7, 8, 9)
FROZEN_TIE_AUT_ARTIFACT = Path(
    "emergencia/resultados/p1a_tie_aut_exacto_d2.json"
)
DEFAULT_OUTPUT = Path(
    "emergencia/resultados/p1a_tie_aut_generic_cross_exact_n7_n9.json"
)

PRECOMMITTED_QUESTION = "min_{kappa in B_m} a(kappa) = 0 for some m in {7,8,9}?"
PRECOMMITTED_FALSIFIER = "one TIE_NONAUT core with a(kappa)=0"
ZERO_INTERPRETATION = (
    "candidate antichain-padding family with O(1) generic cross repairs; "
    "other transposition classes still require proof"
)
POSITIVE_INTERPRETATION = (
    "no zero-repairable core in the exact finite scan; no theorem, no uniform "
    "linear lower bound, and no asymptotic claim"
)


@dataclass
class RepairabilityAggregate:
    """Exact labelled-permutation aggregate for one core size."""

    n: int
    permutations_scanned: int = 0
    selector_ties: int = 0
    tie_aut_only: int = 0
    bad_cores: int = 0
    a_counts: Counter[int] = field(default_factory=Counter)
    repairable_index_counts: Counter[int] = field(default_factory=Counter)
    minimum_a: int | None = None
    minimum_count: int = 0
    first_minimum_core: tuple[int, ...] | None = None
    first_zero_core: tuple[int, ...] | None = None

    def add_bad(
        self,
        core: tuple[int, ...],
        summary: generic_cross.GenericCrossSummary,
    ) -> None:
        if summary.core != core or len(summary.diagnostics) != self.n:
            raise RuntimeError("generic repairability summary does not match its core")
        if summary.a != len(summary.repairable_indices):
            raise RuntimeError("a(kappa) does not equal its repairable-index count")
        if any(
            diagnostic.core != core
            or diagnostic.core_index != index
            or diagnostic.expanded_size != 2 * self.n + 3
            or diagnostic.middle_size != self.n + 2
            for index, diagnostic in enumerate(summary.diagnostics)
        ):
            raise RuntimeError("generic D_x diagnostics failed the phase-2 guards")

        self.bad_cores += 1
        self.a_counts[summary.a] += 1
        self.repairable_index_counts.update(summary.repairable_indices)
        if self.minimum_a is None or summary.a < self.minimum_a:
            self.minimum_a = summary.a
            self.minimum_count = 1
            self.first_minimum_core = core
        elif summary.a == self.minimum_a:
            self.minimum_count += 1
        if summary.a == 0 and self.first_zero_core is None:
            self.first_zero_core = core

    def validate(self, expected: dict[str, int]) -> None:
        if self.permutations_scanned != math.factorial(self.n):
            raise RuntimeError(f"factorial scan mismatch at n={self.n}")
        if self.selector_ties != expected["selector_ties"]:
            raise RuntimeError(f"selector TIE count mismatch at n={self.n}")
        if self.tie_aut_only != expected["tie_aut_only"]:
            raise RuntimeError(f"TIE_AUT_ONLY count mismatch at n={self.n}")
        if self.bad_cores != expected["tie_nonaut"]:
            raise RuntimeError(f"TIE_NONAUT count mismatch at n={self.n}")
        if self.tie_aut_only + self.bad_cores != self.selector_ties:
            raise RuntimeError(f"orbit classes do not partition TIE at n={self.n}")
        if sum(self.a_counts.values()) != self.bad_cores:
            raise RuntimeError(f"a distribution does not cover B_n at n={self.n}")
        if self.bad_cores and self.minimum_a != min(self.a_counts):
            raise RuntimeError(f"minimum a disagrees with its distribution at n={self.n}")
        if self.minimum_count != self.a_counts[self.minimum_a]:
            raise RuntimeError(f"minimum multiplicity mismatch at n={self.n}")
        if (self.first_zero_core is not None) != (self.a_counts[0] > 0):
            raise RuntimeError(f"zero witness mismatch at n={self.n}")

    def as_dict(self) -> dict[str, object]:
        return {
            "n": self.n,
            "permutations_scanned": self.permutations_scanned,
            "selector_ties": self.selector_ties,
            "tie_aut_only": self.tie_aut_only,
            "bad_cores": self.bad_cores,
            "a_distribution": {
                str(a): self.a_counts[a] for a in sorted(self.a_counts)
            },
            "minimum_a": self.minimum_a,
            "minimum_count": self.minimum_count,
            "first_minimum_core": list(self.first_minimum_core or ()),
            "first_zero_core": (
                None if self.first_zero_core is None else list(self.first_zero_core)
            ),
            "repairable_index_counts": {
                str(index): self.repairable_index_counts[index]
                for index in range(self.n)
            },
        }


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _frozen_expectations() -> dict[int, dict[str, int]]:
    payload = json.loads(FROZEN_TIE_AUT_ARTIFACT.read_text(encoding="utf-8"))
    expected: dict[int, dict[str, int]] = {}
    for aggregate in payload["aggregates"]:
        n = int(aggregate["n"])
        if n not in EXACT_N:
            continue
        diagnostics = aggregate["diagnostic_state_counts"]
        expected[n] = {
            "selector_ties": int(aggregate["optimized_state_counts"]["TIE"]),
            "tie_aut_only": int(diagnostics["TIE_AUT_ONLY"]),
            "tie_nonaut": int(diagnostics["TIE_NONAUT"]),
        }
    if tuple(sorted(expected)) != EXACT_N:
        raise RuntimeError("frozen TIE/Aut artifact does not cover n=7,8,9")
    return expected


def scan_exact(
    n_values: Iterable[int] = EXACT_N,
) -> list[RepairabilityAggregate]:
    """Run the exact finite falsifier under the labelled uniform S_n measure."""

    sequence = tuple(int(n) for n in n_values)
    if not sequence or any(n not in EXACT_N for n in sequence):
        raise ValueError(f"n values must be a nonempty subset of {EXACT_N}")
    expected = _frozen_expectations()
    results: list[RepairabilityAggregate] = []
    for n in sequence:
        aggregate = RepairabilityAggregate(n=n)
        for raw_core in permutations(range(n)):
            core = tuple(raw_core)
            aggregate.permutations_scanned += 1
            optimized = comparison.evaluate_selectors(core)[
                comparison.MIN_COVERAGE_LEX
            ]
            if optimized.state != comparison.STATE_TIE:
                continue
            aggregate.selector_ties += 1
            diagnostic = tie_aut.evaluate_tie_aut(core)
            if diagnostic.diagnostic_state == tie_aut.DIAGNOSTIC_TIE_AUT_ONLY:
                aggregate.tie_aut_only += 1
                continue
            if diagnostic.diagnostic_state != tie_aut.DIAGNOSTIC_TIE_NONAUT:
                raise RuntimeError("selector TIE has an invalid orbit diagnostic")
            summary = generic_cross.generic_cross_repairability(core)
            aggregate.add_bad(core, summary)

        aggregate.validate(expected[n])
        results.append(aggregate)
        print(
            "GENERIC_CROSS_EXACT "
            f"N={n} B={aggregate.bad_cores} MIN_A={aggregate.minimum_a} "
            f"A_COUNTS={dict(sorted(aggregate.a_counts.items()))}",
            flush=True,
        )
    return results


def artifact_payload(
    aggregates: Sequence[RepairabilityAggregate],
) -> dict[str, object]:
    if tuple(aggregate.n for aggregate in aggregates) != EXACT_N:
        raise ValueError(f"final artifact requires exactly n={EXACT_N}")
    expectations = _frozen_expectations()
    for aggregate in aggregates:
        aggregate.validate(expectations[aggregate.n])

    global_minimum = min(int(aggregate.minimum_a) for aggregate in aggregates)
    first_zero = next(
        (
            {"n": aggregate.n, "core": list(aggregate.first_zero_core)}
            for aggregate in aggregates
            if aggregate.first_zero_core is not None
        ),
        None,
    )
    return {
        "artifact_schema": "P1A_TIE_AUT_GENERIC_CROSS_EXACT_N7_N9_V1",
        "result_status": "OBSERVED_REPRODUCIBLE_FINITE_N_NOT_ASYMPTOTIC",
        "precommit": {
            "question": PRECOMMITTED_QUESTION,
            "falsifier": PRECOMMITTED_FALSIFIER,
            "used_as_assert_or_pass_fail": False,
            "if_zero": ZERO_INTERPRETATION,
            "if_positive_through_n9": POSITIVE_INTERPRETATION,
        },
        "scope": {
            "n": list(EXACT_N),
            "measure": "uniform labelled permutations in S_n",
            "bad_core": "TIE_NONAUT, equivalently |M(C_kappa)/Aut(C_kappa)| >= 2",
            "a_definition": "#{x in [n] : |M(D_x(kappa))/Aut(D_x(kappa))| = 1}",
            "selector_changed": False,
            "asymptotic_claim": None,
            "other_transposition_classes_controlled": False,
            "input_congestion_b_n_studied": False,
            "thinning_rg_studied": False,
        },
        "outcome": {
            "global_minimum_a": global_minimum,
            "falsifier_observed": first_zero is not None,
            "first_zero_witness": first_zero,
        },
        "aggregates": [aggregate.as_dict() for aggregate in aggregates],
        "validation": {
            "all_guards_passed": True,
            "bad_counts_reproduced_from_frozen_tie_aut": True,
            "complete_global_M_recomputed_after_each_D_x": True,
            "automorphism_orbits_recomputed_after_each_D_x": True,
        },
        "provenance": {
            "command": (
                "python -m emergencia.p1a_tie_aut_generic_cross_exact "
                "--write-artifact"
            ),
            "runner": "emergencia/p1a_tie_aut_generic_cross_exact.py",
            "runner_sha256": _sha256(Path(__file__)),
            "generic_diagnostic": "emergencia/p1a_tie_aut_generic_cross.py",
            "generic_diagnostic_sha256": _sha256(
                Path("emergencia/p1a_tie_aut_generic_cross.py")
            ),
            "tie_aut_diagnostic": "emergencia/p1a_tie_aut_diagnostic.py",
            "tie_aut_diagnostic_sha256": _sha256(
                Path("emergencia/p1a_tie_aut_diagnostic.py")
            ),
            "frozen_tie_aut_artifact": str(FROZEN_TIE_AUT_ARTIFACT),
            "frozen_tie_aut_artifact_sha256": _sha256(FROZEN_TIE_AUT_ARTIFACT),
            "new_dependencies": [],
            "randomness": None,
        },
    }


def _write_artifact(path: Path, payload: dict[str, object]) -> str:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite existing artifact: {path}")
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    temporary.write_bytes(encoded)
    temporary.replace(path)
    digest = hashlib.sha256(encoded).hexdigest()
    sidecar = path.with_suffix(path.suffix + ".sha256")
    sidecar.write_text(f"{digest}  {path.name}\n", encoding="utf-8")
    return digest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    print(f"PRECOMMITTED_QUESTION={PRECOMMITTED_QUESTION}", flush=True)
    print(f"PRECOMMITTED_FALSIFIER={PRECOMMITTED_FALSIFIER}", flush=True)
    print("ASYMPTOTIC_CLAIM=NONE", flush=True)
    aggregates = scan_exact()
    payload = artifact_payload(aggregates)
    print(
        "GENERIC_CROSS_FALSIFIER "
        f"OBSERVED={payload['outcome']['falsifier_observed']} "
        f"GLOBAL_MIN_A={payload['outcome']['global_minimum_a']}",
        flush=True,
    )
    if args.write_artifact:
        digest = _write_artifact(DEFAULT_OUTPUT, payload)
        print(f"ARTIFACT={DEFAULT_OUTPUT}", flush=True)
        print(f"ARTIFACT_SHA256={digest}", flush=True)


if __name__ == "__main__":
    main()
