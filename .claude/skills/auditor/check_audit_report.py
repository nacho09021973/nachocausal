#!/usr/bin/env python3
"""Validate an /auditor integrity report.

A guardrail that cannot fail is decoration: this gate fails a report that is missing a required
section, still contains an unfilled template placeholder, carries an invalid / missing verdict
token, or whose verdict contradicts its own finding counts:
  - AUDIT_ERRORS > 0   must yield AUDIT_FAIL
  - AUDIT_ERRORS == 0 with AUDIT_WARNINGS > 0 must not be AUDIT_PASS (use AUDIT_PASS_WITH_WARNINGS)

Stdlib only. Prints `AUDIT_CHECK=PASS` or `AUDIT_CHECK=FAIL` and exits 0 / 1.

Usage: python .claude/skills/auditor/check_audit_report.py <report.md>
"""
import re
import sys

REQUIRED_HEADINGS = [
    "## 1. Scope & target",
    "## 2. Mechanical audit",
    "## 3. Seal & freeze integrity",
    "## 4. Reproducibility of published numbers",
    "## 5. dev/validation separation & ground-truth leakage",
    "## 6. Claim-boundary check",
    "## 7. Findings",
    "## 8. Verdict",
]

VALID_VERDICTS = {
    "AUDIT_PASS",
    "AUDIT_PASS_WITH_WARNINGS",
    "AUDIT_FAIL",
}


def _int(text: str, key: str) -> int | None:
    m = re.search(rf"^{key}=(\d+)\s*$", text, re.MULTILINE)
    return int(m.group(1)) if m else None


def check(path: str) -> list[str]:
    errs: list[str] = []
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        return [f"cannot read report: {e}"]

    for h in REQUIRED_HEADINGS:
        if h not in text:
            errs.append(f"missing required section heading: {h!r}")

    leftover = re.findall(r"\{\{[A-Z_]+\}\}", text)
    if leftover:
        errs.append(f"unfilled template placeholders remain: {sorted(set(leftover))}")

    m = re.search(r"^AUDIT_VERDICT=(\S+)\s*$", text, re.MULTILINE)
    verdict = m.group(1) if m else None
    if not m:
        errs.append("no AUDIT_VERDICT=<verdict> line found")
    elif verdict not in VALID_VERDICTS:
        errs.append(f"invalid verdict {verdict!r}; must be one of {sorted(VALID_VERDICTS)}")

    n_err = _int(text, "AUDIT_ERRORS")
    n_warn = _int(text, "AUDIT_WARNINGS")
    if n_err is None:
        errs.append("no AUDIT_ERRORS=<n> count line found")
    if n_warn is None:
        errs.append("no AUDIT_WARNINGS=<n> count line found")

    # Verdict must match the finding counts — the wall a green-but-broken audit cannot pass.
    if verdict in VALID_VERDICTS and n_err is not None:
        if n_err > 0 and verdict != "AUDIT_FAIL":
            errs.append(
                f"AUDIT_ERRORS={n_err} (>0) but verdict is {verdict}, not AUDIT_FAIL"
            )
        if n_err == 0 and (n_warn or 0) > 0 and verdict == "AUDIT_PASS":
            errs.append(
                f"AUDIT_WARNINGS={n_warn} (>0) but verdict is AUDIT_PASS; "
                "use AUDIT_PASS_WITH_WARNINGS"
            )

    return errs


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_audit_report.py <report.md>", file=sys.stderr)
        return 2
    errs = check(sys.argv[1])
    if errs:
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        print("AUDIT_CHECK=FAIL")
        return 1
    print("AUDIT_CHECK=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
