"""Bounded guards for the exact n=8 resistant-fibre artifact."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ARTIFACT = Path("emergencia/resultados/p1a_tie_aut_resistant_fibers_n8.json")
SIDECAR = ARTIFACT.with_suffix(ARTIFACT.suffix + ".sha256")
WITNESS = [0, 1, 2, 4, 5, 7, 3, 6]


def test_resistant_fibre_artifact_hash_and_counts() -> None:
    encoded = ARTIFACT.read_bytes()
    digest = hashlib.sha256(encoded).hexdigest()
    assert SIDECAR.read_text(encoding="utf-8").split()[0] == digest

    payload = json.loads(encoded)
    assert payload["counts"] == {
        "B_8": 71,
        "B_8_isomorphism_fibres": 37,
        "a_zero": 14,
        "a_zero_isomorphism_fibres": 8,
        "selector_ties": 214,
    }
    assert sum(record["fibre_size_in_B8"] for record in payload["fibres"]) == 71
    assert sum(len(record["a_zero_members"]) for record in payload["fibres"]) == 14


def test_witness_fibre_has_two_zero_repairability_realizers() -> None:
    payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    record = next(record for record in payload["fibres"] if WITNESS in record["members"])

    assert record["fibre_size_in_B8"] == 2
    assert record["a_distribution"] == {"0": 2}
    assert record["a_zero_members"] == [
        WITNESS,
        [0, 1, 2, 6, 3, 4, 7, 5],
    ]
