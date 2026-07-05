#!/usr/bin/env python3
"""Validate an /alloy-verifier note."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "## 1. Question",
    "## 2. Model under test",
    "## 3. Tooling status",
    "## 4. Exact run record",
    "## 5. Findings",
    "## 6. Scope limits",
    "## 7. Verdict",
    "## 8. Next step",
]

VALID_VERDICTS = {
    "ALLOY_PASS_BOUNDED",
    "ALLOY_COUNTEREXAMPLE_FOUND",
    "ALLOY_MODEL_INVALID",
    "ALLOY_TOOL_UNAVAILABLE",
    "NOT_READY_FOR_ALLOY",
}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_alloy_report.py <report.md>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"ALLOY_CHECK=FAIL missing file: {path}")
        return 1

    text = path.read_text(encoding="utf-8")
    ok = True

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            print(f"ALLOY_CHECK=FAIL missing heading: {heading}")
            ok = False

    if "{{" in text or "}}" in text:
        print("ALLOY_CHECK=FAIL unresolved template placeholder found")
        ok = False

    match = re.search(r"^ALLOY_VERDICT=([A-Z_]+)$", text, re.MULTILINE)
    if not match:
        print("ALLOY_CHECK=FAIL missing ALLOY_VERDICT")
        ok = False
    else:
        verdict = match.group(1)
        if verdict not in VALID_VERDICTS:
            print(f"ALLOY_CHECK=FAIL invalid verdict: {verdict}")
            ok = False

    if ok:
        print("ALLOY_CHECK=PASS")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
