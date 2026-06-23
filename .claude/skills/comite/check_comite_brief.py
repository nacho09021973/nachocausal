#!/usr/bin/env python3
"""Validate a /comite decision brief.

A guardrail that cannot fail is decoration: this gate fails a brief that is missing a required
section, still contains an unfilled template placeholder, carries an invalid / missing verdict
string, or pairs a pre-registration BLOCK with a PROCEED verdict (the founding-rule invariant
stated in SKILL.md step 4 and brief sections 6 & 8). Stdlib only. Prints `BRIEF_CHECK=PASS` or
`BRIEF_CHECK=FAIL` and exits 0 / 1.

Usage: python .claude/skills/comite/check_comite_brief.py <brief.md>
"""
import re
import sys

REQUIRED_HEADINGS = [
    "## 1. Decision question",
    "## 2. Verified state",
    "## 3. Dossier",
    "## 4. Expert briefs",
    "### Reproducibility engineer brief",
    "### Mathematician brief",
    "### Physicist brief",
    "## 5. Falsifier attack",
    "## 6. Pre-registration verdict",
    "## 7. Literature verdict",
    "## 8. Synthesis",
    "## 9. Next-step spec",
    "## 10. Verdict",
    "## 11. User sign-off",
]

PROCEED_VERDICTS = {
    "RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP",
    "RECOMMEND_PROCEED_WITH_CAVEATS",
}
VALID_VERDICTS = PROCEED_VERDICTS | {
    "RECOMMEND_REVISE_AND_RECONVENE",
    "RECOMMEND_DO_NOT_PROCEED",
}


def check(path: str) -> list[str]:
    errs: list[str] = []
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        return [f"cannot read brief: {e}"]

    for h in REQUIRED_HEADINGS:
        if h not in text:
            errs.append(f"missing required section heading: {h!r}")

    leftover = re.findall(r"\{\{[A-Z_]+\}\}", text)
    if leftover:
        errs.append(f"unfilled template placeholders remain: {sorted(set(leftover))}")

    m = re.search(r"^COMMITTEE_DECISION_VERDICT=(\S+)\s*$", text, re.MULTILINE)
    if not m:
        errs.append("no COMMITTEE_DECISION_VERDICT=<verdict> line found")
    elif m.group(1) not in VALID_VERDICTS:
        errs.append(
            f"invalid verdict {m.group(1)!r}; must be one of {sorted(VALID_VERDICTS)}"
        )

    # Founding-rule invariant: a pre-registration BLOCK (section 6) cannot coexist with a PROCEED
    # verdict. The warden writes "Verdict: BLOCK" in its filled section when it blocks.
    prereg_block = re.search(r"(?im)^\s*[-*]?\s*Verdict:\s*BLOCK\b", text)
    if prereg_block and m and m.group(1) in PROCEED_VERDICTS:
        errs.append(
            f"pre-registration BLOCK present but overall verdict is a PROCEED verdict "
            f"({m.group(1)}) — forbidden by the freeze discipline"
        )

    return errs


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_comite_brief.py <brief.md>", file=sys.stderr)
        return 2
    errs = check(sys.argv[1])
    if errs:
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        print("BRIEF_CHECK=FAIL")
        return 1
    print("BRIEF_CHECK=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
