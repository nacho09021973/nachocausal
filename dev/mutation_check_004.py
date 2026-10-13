"""Mutation check for tests/test_004_criteria_can_fail.py (prereg-004 step 4). Generator of the
mutation table in dev/PREREG004_STEP_4_2026-10-13.md; added after auditor report 043, warning 4.

Each mutation edits a COPY of nachocausal2p1/validate.py inside a temporary tree (the repo files
are never touched), runs the step-4 test file there, and reports how many tests fail. A mutation
that no test catches would mean the criterion is decoration.
Usage: .venv/bin/python dev/mutation_check_004.py
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPY = ("nachocausal", "nachocausal2p1", "tests/test_004_criteria_can_fail.py",
        "dev/2p1_sweep_T_rho126_v2_2026-10-12.jsonl")
MUTATIONS = (
    ("coverage term dropped from (ii)",
     'and prim["coverage_frac"] >= thresholds.COVERAGE_FLOOR', "and True"),
    ("escape_pass forced True",
     '"iv_flat_escapes_primary": bool(prim["escape_pass"])', '"iv_flat_escapes_primary": True'),
    ("loc_pass uses 2*theta",
     'res["median_width_over_2M"] <= res["theta_loc"]',
     'res["median_width_over_2M"] <= 2 * res["theta_loc"]'),
    ("escape count allows MAX_MINK_ESCAPES + 1",
     "<= thresholds.MAX_MINK_ESCAPES", "<= thresholds.MAX_MINK_ESCAPES + 1"),
    ("v_order_only forced True",
     '"v_order_only": bool(guard_ran)', '"v_order_only": True'),
)


def run_tests(tree):
    p = subprocess.run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                        "tests/test_004_criteria_can_fail.py"],
                       cwd=tree, capture_output=True, text=True)
    m = re.search(r"(\d+) failed", p.stdout)
    return int(m.group(1)) if m else 0, p.stdout.strip().splitlines()[-1]


def main():
    with tempfile.TemporaryDirectory() as tmp:
        tree = Path(tmp)
        for rel in COPY:
            src, dst = ROOT / rel, tree / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            (shutil.copytree if src.is_dir() else shutil.copy2)(src, dst)
        target = tree / "nachocausal2p1" / "validate.py"
        pristine = target.read_text()
        failed, line = run_tests(tree)
        print(f"baseline (no mutation): {line}")
        assert failed == 0, "baseline must pass"
        caught = 0
        for name, old, new in MUTATIONS:
            assert pristine.count(old) == 1, f"mutation anchor not unique: {name}"
            target.write_text(pristine.replace(old, new))
            failed, line = run_tests(tree)
            caught += failed > 0
            print(f"{name}: {line}")
        target.write_text(pristine)
        print(f"caught {caught}/{len(MUTATIONS)}")


if __name__ == "__main__":
    main()
