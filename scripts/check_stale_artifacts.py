"""Detect verification artifacts whose generating code changed after they were written.

A `verification_X.json` is produced by `verify_X.py`. The artifact goes stale when
the script OR anything the script imports from the repo is committed after the
artifact's own last commit. The dangerous case is the transitive one: the script
itself never changes, one of its imports does, and no diff in the generating file
records the drift.

That is exactly how the four B2 artifacts went stale when `6f866a2` corrected the
angular kernel on 2026-09-13 (see `dev/B2_STALE_ARTIFACTS_2026-10-11.md`).

Read-only: inspects git history and import graphs, runs nothing and writes nothing.

    python3 scripts/check_stale_artifacts.py [--root DIR] [--quiet]

Exit status 1 if any artifact is stale, so it can gate CI.
"""
from __future__ import annotations

import argparse
import ast
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def commit_time(path: Path) -> int | None:
    """Unix time of the last commit touching `path`, or None if untracked."""
    out = subprocess.run(
        ["git", "log", "-1", "--format=%ct", "--", str(path)],
        cwd=REPO, capture_output=True, text=True,
    ).stdout.strip()
    return int(out) if out else None


def commit_date(path: Path) -> str:
    out = subprocess.run(
        ["git", "log", "-1", "--format=%ad", "--date=short", "--", str(path)],
        cwd=REPO, capture_output=True, text=True,
    ).stdout.strip()
    return out or "untracked"


def local_imports(script: Path) -> list[str]:
    """Module names imported by `script`, excluding the standard library and third party.

    Only the names matter: resolution against sibling files happens in `dependencies`.
    """
    try:
        tree = ast.parse(script.read_text(encoding="utf-8", errors="replace"))
    except (SyntaxError, OSError):
        return []
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names += [a.name.split(".")[0] for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            names.append(node.module.split(".")[0])
        elif isinstance(node, ast.ImportFrom) and node.level:
            names.append((node.module or "").split(".")[0])
    return names


def dependencies(script: Path) -> set[Path]:
    """Transitive closure of repo-local modules reachable from `script`, including itself.

    A name resolves to a local module if `<name>.py` exists beside the importer or
    in one of the directories scripts here add to sys.path (the sibling `B1/`).
    """
    seen: set[Path] = set()
    stack = [script]
    while stack:
        cur = stack.pop()
        if cur in seen or not cur.exists():
            continue
        seen.add(cur)
        search = [cur.parent, cur.parent / "B1", *cur.parent.glob("*/")]
        for name in local_imports(cur):
            for d in search:
                cand = d / f"{name}.py"
                if cand.exists() and cand not in seen:
                    stack.append(cand)
                    break
    return seen


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default="research_program",
                    help="directory to scan (default: research_program)")
    ap.add_argument("--quiet", action="store_true", help="print only stale artifacts")
    args = ap.parse_args()

    root = REPO / args.root
    if not root.is_dir():
        print(f"no such directory: {root}", file=sys.stderr)
        return 2

    artifacts = sorted(root.rglob("verification_*.json"))
    stale, checked, orphan = [], 0, []

    for art in artifacts:
        script = art.parent / f"verify_{art.stem[len('verification_'):]}.py"
        if not script.exists():
            orphan.append(art)
            continue
        t_art = commit_time(art)
        if t_art is None:
            continue
        checked += 1
        newer = [
            dep for dep in dependencies(script)
            if (t := commit_time(dep)) is not None and t > t_art
        ]
        if newer:
            stale.append((art, script, sorted(newer)))

    if stale:
        print(f"STALE: {len(stale)} of {checked} artifacts predate their own code\n")
        for art, script, newer in stale:
            print(f"  {art.relative_to(REPO)}")
            print(f"    artifact written {commit_date(art)}")
            for dep in newer:
                via = "the script itself" if dep == script else "imported module"
                print(f"    changed {commit_date(dep)}  {dep.relative_to(REPO)}  ({via})")
            print()
        print("Regenerating an artifact overwrites a verification record. That is a PI")
        print("decision, not an automatic fix -- this check only reports.")
    elif not args.quiet:
        print(f"OK: all {checked} artifacts are at least as new as their code.")

    if orphan and not args.quiet:
        print(f"\n{len(orphan)} artifact(s) with no matching verify_*.py, not checked:")
        for art in orphan:
            print(f"  {art.relative_to(REPO)}")

    return 1 if stale else 0


if __name__ == "__main__":
    raise SystemExit(main())
