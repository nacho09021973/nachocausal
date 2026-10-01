"""Verify this snapshot or run an archived script in a disposable copy.

The scientific files remain byte-for-byte copies of their original sources.
Only historical file paths are redirected at runtime, without editing scripts.
"""
import argparse
import builtins
import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import sys
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(check_sources=False):
    manifest = json.loads((ROOT / "PROVENANCE.json").read_text())
    for entry in manifest["files"]:
        target = ROOT / entry["archived_path"]
        if target.stat().st_size != entry["bytes"] or digest(target) != entry["sha256"]:
            raise RuntimeError(f"Archive mismatch: {target}")
        if check_sources:
            source = Path(entry["source"])
            if source.stat().st_size != entry["bytes"] or digest(source) != entry["sha256"]:
                raise RuntimeError(f"Source mismatch: {source}")
    if check_sources:
        expected = {entry["source"] for entry in manifest["files"]}
        excluded = {entry["source"] for entry in manifest["excluded"]}
        current = set()
        for source_root in manifest["source_roots"]:
            source_root = Path(source_root)
            paths = [source_root] if source_root.is_file() else source_root.rglob("*")
            current.update(str(p) for p in paths if p.is_file() and str(p) not in excluded
                           and "__pycache__" not in p.parts and p.suffix != ".pyc")
        if current != expected:
            raise RuntimeError(f"Source inventory changed: {sorted(current ^ expected)}")
    print(f"Verified {len(manifest['files'])} archived scientific files"
          + (" and all original sources." if check_sources else "."))
    return manifest


def run_script(relative_script, arguments):
    manifest = verify()
    archived = {entry["archived_path"] for entry in manifest["files"]}
    if relative_script not in archived or not relative_script.endswith(".py"):
        raise ValueError("Select a Python script listed in PROVENANCE.json.")
    with tempfile.TemporaryDirectory(prefix="radial-3p1-archive-") as scratch:
        copy = Path(scratch) / "snapshot"
        shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        mapping = {entry["source"]: copy / entry["archived_path"] for entry in manifest["files"]}
        original_open = builtins.open
        redirects = []

        def archival_open(file, *args, **kwargs):
            key = os.fspath(file) if isinstance(file, (str, os.PathLike)) else file
            if key in mapping:
                redirects.append(key)
                file = mapping[key]
            return original_open(file, *args, **kwargs)

        previous_argv, previous_cwd = sys.argv[:], Path.cwd()
        script = copy / relative_script
        try:
            sys.argv = [str(script), *arguments]
            os.chdir(copy)
            with patch("builtins.open", archival_open):
                runpy.run_path(str(script), run_name="__main__")
        finally:
            sys.argv = previous_argv
            os.chdir(previous_cwd)
        print(f"Historical source reads redirected: {len(redirects)}.")
        for entry in manifest["files"]:
            if entry["archived_path"].endswith(".json"):
                same = digest(copy / entry["archived_path"]) == entry["sha256"]
                print(f"JSON {'matches snapshot' if same else 'differs from snapshot'}: "
                      f"{entry['archived_path']}")
    verify()
    print("Disposable run finished; archived files were preserved.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    verification = commands.add_parser("verify")
    verification.add_argument("--sources", action="store_true",
                              help="Also check original paths on the source workstation.")
    execution = commands.add_parser("run")
    execution.add_argument("script", help="Archive-relative script path.")
    execution.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.command == "verify":
        verify(args.sources)
    else:
        run_script(args.script, args.arguments)
