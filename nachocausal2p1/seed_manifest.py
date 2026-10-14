"""C2 seed-manifest producer and reader (CANDIDATE; no draw before explicit C2).

C1 seals the instrument and recipe. C2 adds only docs/validation_004_seeds.json.
This module draws seed identifiers, never causets, and is their permanent generator.
Future authorised C2: python -m nachocausal2p1.seed_manifest <full-C1-SHA>
The SHA rule supplies reproducibility, not externally supplied randomness.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess

import numpy as np

from . import thresholds

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_REL = "docs/validation_004_seeds.json"
MANIFEST_PATH = ROOT / MANIFEST_REL
FROZEN_DOC = "docs/preregistration_004.md"
SEALED_PATHS = ("nachocausal/", "nachocausal2p1/", FROZEN_DOC)


def _git(*args: str) -> str:
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"C2 provenance check failed: git {' '.join(args)}: {result.stderr}")
    return result.stdout


def _check_freeze(freeze_commit: str) -> None:
    if thresholds.STATUS != "FROZEN":
        raise RuntimeError("C2 manifest requires the C1 FROZEN instrument.")
    thresholds.draw_seed_from_commit(freeze_commit)  # full lowercase SHA, never an abbreviation
    # C1 is the unique commit introducing the frozen document, not a later convenient SHA.
    introduced = _git("log", "--diff-filter=A", "--format=%H", "--", FROZEN_DOC).splitlines()
    if introduced != [freeze_commit]:
        raise RuntimeError("freeze_commit must be the unique C1 commit introducing the frozen doc.")
    _git("diff", "--exit-code", freeze_commit, "--", *SEALED_PATHS)


def _draw(freeze_commit: str) -> list[int]:
    draw_seed = thresholds.draw_seed_from_commit(freeze_commit)
    lo, hi = thresholds.VIRGIN_BAND
    return sorted(int(s) for s in np.random.default_rng(draw_seed).choice(
        np.arange(lo, hi + 1), size=thresholds.ENSEMBLE, replace=False))


def check_manifest(doc: dict) -> dict:
    """Check binding to C1, unchanged instrument, band, and exact frozen draw recipe."""
    if not isinstance(doc, dict) or set(doc) != {"freeze_commit", "draw_seed", "seeds"}:
        raise ValueError("C2 manifest must contain exactly freeze_commit, draw_seed, seeds.")
    sha = doc["freeze_commit"]
    if not isinstance(sha, str):
        raise ValueError("freeze_commit must be a full lowercase SHA string.")
    _check_freeze(sha)
    if type(doc["draw_seed"]) is not int or doc["draw_seed"] != thresholds.draw_seed_from_commit(sha):
        raise ValueError("C2 draw_seed does not match freeze_commit.")
    seeds = doc["seeds"]
    if not isinstance(seeds, list) or any(type(s) is not int for s in seeds):
        raise ValueError("C2 seeds must be a list of integer identifiers.")
    if not seeds:
        raise ValueError("C2 manifest cannot have an empty seed list.")
    thresholds.check_validation_seeds(seeds)
    if seeds != _draw(sha):
        raise ValueError("C2 seeds do not match the sorted frozen draw recipe.")
    return doc


def load_manifest() -> dict:
    """C3 reads exactly the C2 manifest committed in HEAD, never an uncommitted substitution."""
    thresholds.assert_environment()
    raw = MANIFEST_PATH.read_text()
    if raw != _git("show", f"HEAD:{MANIFEST_REL}"):
        raise RuntimeError("C2 manifest differs from its committed HEAD version.")
    if _git("status", "--porcelain"):
        raise RuntimeError("C3 requires a clean tree before reading the C2 manifest.")
    return check_manifest(json.loads(raw))


def create_manifest(freeze_commit: str) -> Path:
    """Explicit C2 only. Refuse pre-freeze, dirty tree, instrument drift and overwriting."""
    thresholds.assert_environment()
    _check_freeze(freeze_commit)
    if MANIFEST_PATH.exists():
        raise FileExistsError("C2 manifest already exists; do not redraw or overwrite it.")
    if _git("status", "--porcelain"):
        raise RuntimeError("C2 requires a clean tree before drawing.")
    doc = {"freeze_commit": freeze_commit,
           "draw_seed": thresholds.draw_seed_from_commit(freeze_commit),
           "seeds": _draw(freeze_commit)}
    thresholds.check_validation_seeds(doc["seeds"])
    with MANIFEST_PATH.open("x") as f:
        f.write(json.dumps(doc, indent=2) + "\n")
        f.flush()
        os.fsync(f.fileno())
    return MANIFEST_PATH


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("freeze_commit", help="full SHA of the authorised C1 freeze commit")
    args = parser.parse_args()
    print(create_manifest(args.freeze_commit))
