"""Tests for PR011 freeze geometry sanity (no TV certification)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


_ROOT = Path(__file__).resolve().parent.parent


def test_pr011_freeze_sanity_check_passes() -> None:
    script = _ROOT / "dev" / "pr011_freeze_sanity_check.py"
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "PR011_FREEZE_SANITY=PASS" in proc.stdout