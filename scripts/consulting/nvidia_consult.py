#!/usr/bin/env python3
"""Prepare and optionally run external NVIDIA advisory consultations."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shlex
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_NVIDIA_HOME = Path("~/ai/nvidia-consult").expanduser()
DEFAULT_OUTPUT_ROOT = Path("dev/consultations/nvidia")
DEFAULT_TIMEOUT_SECONDS = 600
ADVISORY_LABEL = "ADVISORY_ONLY_NOT_EVIDENCE"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare an external NVIDIA advisory consultation dossier.")
    parser.add_argument("--question", help="Consultation question or review request.")
    parser.add_argument(
        "--context",
        action="append",
        type=Path,
        default=[],
        help="File or directory to include in the dossier. Can be passed multiple times.",
    )
    parser.add_argument("--note", action="append", default=[], help="Extra note to include in the dossier.")
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--consultation-id", help="Stable ID for the consultation directory.")
    parser.add_argument("--nvidia-home", type=Path, default=Path(os.environ.get("NVIDIA_CONSULT_HOME", DEFAULT_NVIDIA_HOME)))
    parser.add_argument("--nvidia-cmd", default=os.environ.get("NVIDIA_CONSULT_CMD"))
    parser.add_argument("--run", action="store_true", help="Run the configured external command.")
    parser.add_argument("--check-only", action="store_true", help="Only print NVIDIA adapter status.")
    parser.add_argument("--max-file-bytes", type=int, default=200_000)
    parser.add_argument("--timeout-seconds", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path.cwd()
    status = inspect_nvidia(args.nvidia_home.expanduser(), args.nvidia_cmd)

    if args.check_only:
        print(json.dumps(status, indent=2, sort_keys=True))
        return 0

    if not args.question:
        print("error: --question is required unless --check-only is used", file=sys.stderr)
        return 2

    consultation_id = args.consultation_id or make_consultation_id()
    output_dir = args.output_root / consultation_id
    output_dir.mkdir(parents=True, exist_ok=False)

    manifest = build_manifest(repo_root, args, status, consultation_id)
    context_blocks = collect_context(args.context, args.max_file_bytes)
    dossier = render_dossier(manifest, args.question, args.note, context_blocks)

    write_text(output_dir / "dossier.md", dossier)
    write_json(output_dir / "manifest.json", manifest)

    if not args.run:
        print(f"Dossier: {output_dir / 'dossier.md'}")
        print(f"Manifest: {output_dir / 'manifest.json'}")
        print("NVIDIA consult not invoked: pass --run with NVIDIA_CONSULT_CMD or --nvidia-cmd to execute.")
        return 0

    if not args.nvidia_cmd:
        write_text(output_dir / "response.md", render_failure("NVIDIA_CONSULT_CMD is not configured.", status))
        print("error: NVIDIA_CONSULT_CMD is not configured; response.md records the failure", file=sys.stderr)
        return 2

    command = command_argv(args.nvidia_cmd)
    if not command:
        write_text(output_dir / "response.md", render_failure("NVIDIA consult command is empty.", status))
        print("error: NVIDIA consult command is empty; response.md records the failure", file=sys.stderr)
        return 2

    if not command_exists(command[0]):
        message = f"NVIDIA consult command not found: {command[0]}"
        write_text(output_dir / "response.md", render_failure(message, status))
        print(f"error: {message}; response.md records the failure", file=sys.stderr)
        return 2

    completed = subprocess.run(
        command,
        input=dossier,
        text=True,
        capture_output=True,
        timeout=args.timeout_seconds,
        check=False,
    )
    response = render_response(command, completed, status)
    write_text(output_dir / "response.md", response)
    print(f"Response: {output_dir / 'response.md'}")
    return completed.returncode


def inspect_nvidia(nvidia_home: Path, nvidia_cmd: str | None) -> dict[str, object]:
    argv = command_argv(nvidia_cmd) if nvidia_cmd else []
    return {
        "nvidia_home": str(nvidia_home),
        "nvidia_home_exists": nvidia_home.exists(),
        "nvidia_cmd_configured": bool(nvidia_cmd),
        "nvidia_cmd": nvidia_cmd,
        "nvidia_command_found": command_exists(argv[0]) if argv else False,
        "external_repo": external_repo_metadata(nvidia_home),
        "adapter_contract": "configured command reads dossier from stdin and writes answer to stdout",
    }


def build_manifest(repo_root: Path, args: argparse.Namespace, status: dict[str, object], consultation_id: str) -> dict[str, object]:
    return {
        "consultation_id": consultation_id,
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "repo_root": str(repo_root),
        "git": git_metadata(repo_root),
        "nvidia": status,
        "question_sha256": sha256_text(args.question),
        "context": [str(path) for path in args.context],
        "max_file_bytes": args.max_file_bytes,
        "run_requested": args.run,
    }


def git_metadata(repo_root: Path) -> dict[str, object]:
    return {
        "head": git_output(repo_root, ["rev-parse", "HEAD"]),
        "branch": git_output(repo_root, ["branch", "--show-current"]),
        "status_short": git_output(repo_root, ["status", "--short"]),
    }


def git_output(repo_root: Path, args: list[str]) -> str | None:
    completed = subprocess.run(["git", *args], cwd=repo_root, text=True, capture_output=True, check=False)
    if completed.returncode == 0:
        return completed.stdout.strip()
    return None


def external_repo_metadata(repo_root: Path) -> dict[str, object]:
    git_dir = repo_root / ".git"
    if not git_dir.exists():
        return {"is_git_repo": False, "head": None, "status_short": None}
    return {
        "is_git_repo": True,
        "head": direct_git_output(repo_root, ["rev-parse", "HEAD"]),
        "status_short": direct_git_output(repo_root, ["status", "--short"]),
    }


def direct_git_output(repo_root: Path, args: list[str]) -> str | None:
    completed = subprocess.run(["git", *args], cwd=repo_root, text=True, capture_output=True, check=False)
    if completed.returncode == 0:
        return completed.stdout.strip()
    return None


def collect_context(paths: list[Path], max_file_bytes: int) -> list[dict[str, object]]:
    blocks = []
    for path in paths:
        if path.is_dir():
            for child in sorted(path.rglob("*")):
                if child.is_file():
                    blocks.append(read_context_file(child, max_file_bytes))
        elif path.is_file():
            blocks.append(read_context_file(path, max_file_bytes))
        else:
            blocks.append({"path": str(path), "included": False, "reason": "path does not exist"})
    return blocks


def read_context_file(path: Path, max_file_bytes: int) -> dict[str, object]:
    size = path.stat().st_size
    if size > max_file_bytes:
        return {"path": str(path), "included": False, "bytes": size, "reason": "file exceeds max_file_bytes"}
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return {"path": str(path), "included": False, "bytes": size, "reason": "not utf-8 text"}
    return {
        "path": str(path),
        "included": True,
        "bytes": size,
        "sha256": sha256_text(text),
        "text": text,
    }


def render_dossier(manifest: dict[str, object], question: str, notes: list[str], context_blocks: list[dict[str, object]]) -> str:
    lines = [
        "# NVIDIA consultation dossier",
        "",
        "## Question",
        "",
        question,
        "",
        "## Metadata",
        "",
        "```json",
        json.dumps(manifest, indent=2, sort_keys=True),
        "```",
        "",
    ]
    if notes:
        lines.extend(["## Notes", ""])
        lines.extend(f"- {note}" for note in notes)
        lines.append("")
    lines.extend(["## Context", ""])
    if not context_blocks:
        lines.extend(["No context files were attached.", ""])
    for block in context_blocks:
        lines.extend([f"### {block['path']}", ""])
        if not block.get("included"):
            lines.extend([f"Not included: {block.get('reason', 'unknown reason')}", ""])
            continue
        lines.extend(
            [
                f"Bytes: {block['bytes']}",
                f"SHA256: {block['sha256']}",
                "",
                "```text",
                str(block["text"]),
                "```",
                "",
            ]
        )
    return "\n".join(lines)


def render_failure(message: str, status: dict[str, object]) -> str:
    return "\n".join(
        [
            "# NVIDIA consultation response",
            "",
            f"Advisory label: {ADVISORY_LABEL}",
            "Status: failed before model invocation",
            "",
            f"Reason: {message}",
            "",
            "## Adapter status",
            "",
            "```json",
            json.dumps(status, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )


def render_response(command: list[str], completed: subprocess.CompletedProcess[str], status: dict[str, object]) -> str:
    return "\n".join(
        [
            "# NVIDIA consultation response",
            "",
            f"Advisory label: {ADVISORY_LABEL}",
            f"Status: {'ok' if completed.returncode == 0 else 'command_failed'}",
            f"Return code: {completed.returncode}",
            f"Command: {shlex.join(command)}",
            "",
            "## Adapter status",
            "",
            "```json",
            json.dumps(status, indent=2, sort_keys=True),
            "```",
            "",
            "## Stdout",
            "",
            completed.stdout or "",
            "",
            "## Stderr",
            "",
            "```text",
            completed.stderr or "",
            "```",
            "",
        ]
    )


def make_consultation_id() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def command_argv(command: str | None) -> list[str]:
    return shlex.split(command or "")


def command_exists(program: str) -> bool:
    if "/" in program:
        return Path(program).exists()
    return shutil.which(program) is not None


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, data: dict[str, object]) -> None:
    write_text(path, json.dumps(data, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
