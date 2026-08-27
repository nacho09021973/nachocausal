#!/usr/bin/env python3
"""Exact n=8 fibre audit for the a(kappa)=0 TIE/Aut cores.

The finite question is whether the 14 labelled permutations with a=0 observed
inside B_8 represent many non-isomorphic posets or multiplicity inside a smaller
number of isomorphism fibres.  This runner makes no asymptotic inference.
"""

from __future__ import annotations

import hashlib
import json
import os
from collections import Counter, defaultdict
from itertools import permutations
from pathlib import Path

from dev.r3_bridge_e_fibers import canonical_form, relation_matrix
from emergencia import p1a_comparar_selectores_d2 as comparison
from emergencia import p1a_tie_aut_diagnostic as tie_aut
from emergencia import p1a_tie_aut_generic_cross as generic_cross


N = 8
EXPECTED_TIES = 214
EXPECTED_BAD = 71
EXPECTED_ZERO = 14
PRECOMMITTED_QUESTION = (
    "How many poset-isomorphism fibres contain the 14 labelled B_8 cores "
    "with a(kappa)=0?"
)
CLAIM_CEILING = "exact n=8 fibre decomposition only; no asymptotic inference"
DEFAULT_OUTPUT = Path(
    "emergencia/resultados/p1a_tie_aut_resistant_fibers_n8.json"
)


def _canonical_id(canonical: tuple[bool, ...]) -> str:
    packed = bytes(int(value) for value in canonical)
    return hashlib.sha256(packed).hexdigest()


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def audit_fibres() -> dict[str, object]:
    selector_ties = 0
    bad_count = 0
    zero_count = 0
    fibres: dict[tuple[bool, ...], list[tuple[tuple[int, ...], int]]] = defaultdict(list)

    for raw_core in permutations(range(N)):
        core = tuple(raw_core)
        optimized = comparison.evaluate_selectors(core)[
            comparison.MIN_COVERAGE_LEX
        ]
        if optimized.state != comparison.STATE_TIE:
            continue
        selector_ties += 1
        diagnostic = tie_aut.evaluate_tie_aut(core)
        if diagnostic.diagnostic_state != tie_aut.DIAGNOSTIC_TIE_NONAUT:
            continue
        bad_count += 1
        summary = generic_cross.generic_cross_repairability(core)
        if summary.a == 0:
            zero_count += 1
        canonical = canonical_form(relation_matrix(core), N)
        fibres[canonical].append((core, summary.a))

    if selector_ties != EXPECTED_TIES:
        raise RuntimeError("n=8 selector TIE count does not reproduce the frozen run")
    if bad_count != EXPECTED_BAD:
        raise RuntimeError("n=8 B count does not reproduce the frozen run")
    if zero_count != EXPECTED_ZERO:
        raise RuntimeError("n=8 a=0 count does not reproduce the frozen run")
    if sum(len(members) for members in fibres.values()) != EXPECTED_BAD:
        raise RuntimeError("isomorphism fibres do not partition B_8")

    records = []
    zero_fibre_count = 0
    for canonical, members in sorted(fibres.items(), key=lambda item: item[0]):
        a_counts = Counter(a for _, a in members)
        zero_members = [core for core, a in members if a == 0]
        if zero_members:
            zero_fibre_count += 1
        records.append(
            {
                "canonical_id": _canonical_id(canonical),
                "fibre_size_in_B8": len(members),
                "a_distribution": {
                    str(a): a_counts[a] for a in sorted(a_counts)
                },
                "members": [list(core) for core, _ in sorted(members)],
                "a_zero_members": [list(core) for core in sorted(zero_members)],
            }
        )

    return {
        "artifact_schema": "P1A_TIE_AUT_RESISTANT_FIBRES_N8_V1",
        "result_status": "OBSERVED_REPRODUCIBLE_FINITE_N_NOT_ASYMPTOTIC",
        "precommit": {
            "question": PRECOMMITTED_QUESTION,
            "claim_ceiling": CLAIM_CEILING,
        },
        "measure": "uniform labelled permutations in S_8",
        "counts": {
            "selector_ties": selector_ties,
            "B_8": bad_count,
            "a_zero": zero_count,
            "B_8_isomorphism_fibres": len(fibres),
            "a_zero_isomorphism_fibres": zero_fibre_count,
        },
        "fibres": records,
        "provenance": {
            "runner": "emergencia/p1a_tie_aut_resistant_fibers_n8.py",
            "runner_sha256": _sha256(Path(__file__)),
            "canonicalization": "dev/r3_bridge_e_fibers.py",
            "canonicalization_sha256": _sha256(Path("dev/r3_bridge_e_fibers.py")),
            "generic_cross_source_sha256": _sha256(
                Path("emergencia/p1a_tie_aut_generic_cross.py")
            ),
            "tie_aut_source_sha256": _sha256(
                Path("emergencia/p1a_tie_aut_diagnostic.py")
            ),
            "command": (
                "python -m emergencia.p1a_tie_aut_resistant_fibers_n8 "
                "--write-artifact"
            ),
            "new_dependencies": [],
            "randomness": None,
        },
    }


def _write_artifact(payload: dict[str, object]) -> str:
    if DEFAULT_OUTPUT.exists():
        raise FileExistsError(f"refusing to overwrite {DEFAULT_OUTPUT}")
    encoded = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    DEFAULT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    temporary = DEFAULT_OUTPUT.with_name(f".{DEFAULT_OUTPUT.name}.tmp-{os.getpid()}")
    temporary.write_bytes(encoded)
    temporary.replace(DEFAULT_OUTPUT)
    digest = hashlib.sha256(encoded).hexdigest()
    sidecar = DEFAULT_OUTPUT.with_suffix(DEFAULT_OUTPUT.suffix + ".sha256")
    sidecar.write_text(f"{digest}  {DEFAULT_OUTPUT.name}\n", encoding="utf-8")
    return digest


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    print(f"PRECOMMITTED_QUESTION={PRECOMMITTED_QUESTION}", flush=True)
    print(f"CLAIM_CEILING={CLAIM_CEILING}", flush=True)
    payload = audit_fibres()
    counts = payload["counts"]
    print(
        "RESISTANT_FIBRES_N8 "
        f"B={counts['B_8']} A_ZERO={counts['a_zero']} "
        f"B_FIBRES={counts['B_8_isomorphism_fibres']} "
        f"ZERO_FIBRES={counts['a_zero_isomorphism_fibres']}",
        flush=True,
    )
    if args.write_artifact:
        digest = _write_artifact(payload)
        print(f"ARTIFACT={DEFAULT_OUTPUT}", flush=True)
        print(f"ARTIFACT_SHA256={digest}", flush=True)


if __name__ == "__main__":
    main()
