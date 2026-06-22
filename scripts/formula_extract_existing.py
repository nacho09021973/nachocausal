"""Extract first-pass formula-branch scalings from recorded prereg-002 results.

This script deliberately uses recorded outputs only. It prefers the local
results/validation.json aggregate if present, and otherwise falls back to the
table transcribed in docs/preregistration_002_result.md. It does not run the
benchmark, generate new causets, or inspect per-seed hidden state.
"""

from __future__ import annotations

import math
import json
import re
from pathlib import Path

import numpy as np


RESULT_DOC = Path("docs/preregistration_002_result.md")
RESULT_JSON = Path("results/validation.json")
ROW_RE = re.compile(
    r"^\|\s*(?:\*\*)?(?P<lam>\d+)(?:\*\*)?(?:\s*\([^)]*\))?\s*"
    r"\|\s*(?P<nbar>\d+)\s*"
    r"\|\s*\d+\s*"
    r"\|\s*(?:\*\*)?[-+0-9.eE]+(?:\*\*)?\s*"
    r"\|\s*(?:True|False)\s*"
    r"\|\s*(?:\*\*)?(?P<width>[-+0-9.]+)(?:\*\*)?\s*\|"
)


def load_recorded_aggregates(
    json_path: Path = RESULT_JSON, doc_path: Path = RESULT_DOC
) -> tuple[str, np.ndarray, np.ndarray, np.ndarray | None]:
    """Return source, Nbar, width, and optional midpoint dispersion aggregates."""

    if json_path.exists():
        data = json.loads(json_path.read_text(encoding="utf-8"))
        rows = sorted(
            data["levels"].values(),
            key=lambda row: float(row["intensity"]),
        )
        nbar = np.array([float(row["N_mean"]) for row in rows])
        width = np.array([float(row["median_width_over_2M"]) for row in rows])
        r_std = np.array([float(row["boundary_r_std"]) for row in rows])
        return str(json_path), nbar, width, r_std

    nbar, width = load_recorded_widths_from_doc(doc_path)
    return str(doc_path), nbar, width, None


def load_recorded_widths_from_doc(path: Path = RESULT_DOC) -> tuple[np.ndarray, np.ndarray]:
    """Return Nbar and median |dr|/(2M) values from the transcribed result table."""

    nbar: list[float] = []
    width: list[float] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ROW_RE.match(line)
        if match:
            nbar.append(float(match.group("nbar")))
            width.append(float(match.group("width")))

    if len(nbar) != 4:
        raise RuntimeError(f"expected 4 table rows, found {len(nbar)}")

    return np.array(nbar), np.array(width)


def fit_power_law(nbar: np.ndarray, width: np.ndarray) -> tuple[float, float]:
    """Fit log(W) = intercept + gamma log(N)."""

    gamma, intercept = np.polyfit(np.log(nbar), np.log(width), 1)
    return float(gamma), float(intercept)


def fit_fixed_expansion(nbar: np.ndarray, width: np.ndarray) -> tuple[float, float]:
    """Fit W = a N^-1/2 + b N^-1."""

    design = np.column_stack([nbar**-0.5, nbar**-1.0])
    a, b = np.linalg.lstsq(design, width, rcond=None)[0]
    return float(a), float(b)


def fit_residual_model(
    nbar: np.ndarray, width: np.ndarray
) -> tuple[float, float, float, float]:
    """Grid-fit W = W_inf + A N^-alpha.

    Four points are too few for a strong nonlinear inference; this is a compact
    diagnostic to see whether a residual-width term is immediately demanded.
    """

    best: tuple[float, float, float, float] | None = None
    for alpha in np.linspace(0.05, 1.5, 1451):
        design = np.column_stack([np.ones_like(nbar), nbar ** (-alpha)])
        w_inf, amp = np.linalg.lstsq(design, width, rcond=None)[0]
        pred = design @ np.array([w_inf, amp])
        rss = float(np.square(width - pred).sum())
        if best is None or rss < best[0]:
            best = (rss, float(alpha), float(w_inf), float(amp))

    assert best is not None
    return best


def print_metric_report(label: str, nbar: np.ndarray, values: np.ndarray) -> None:
    gamma, intercept = fit_power_law(nbar, values)
    a, b = fit_fixed_expansion(nbar, values)
    rss_resid, alpha_resid, w_inf, amp = fit_residual_model(nbar, values)

    print(label)
    print("-" * len(label))
    print("values:", " ".join(f"{x:.6g}" for x in values))
    print(f"log-log slope gamma: {gamma:.3f}")
    print(f"log-log intercept: {intercept:.3f}")
    print("local slopes:")
    for lo_n, hi_n, lo_w, hi_w in zip(nbar[:-1], nbar[1:], values[:-1], values[1:]):
        slope = (math.log(hi_w) - math.log(lo_w)) / (math.log(hi_n) - math.log(lo_n))
        print(f"  {lo_n:.0f}->{hi_n:.0f}: {slope:.3f}")
    print("fixed expansion value = a*N^-1/2 + b*N^-1:")
    print(f"  a = {a:.3f}")
    print(f"  b = {b:.3f}")
    print("residual model value = W_inf + A*N^-alpha, grid diagnostic:")
    print(f"  alpha = {alpha_resid:.3f}")
    print(f"  W_inf = {w_inf:.6g}")
    print(f"  A = {amp:.3f}")
    print(f"  rss = {rss_resid:.6g}")
    print()


def main() -> None:
    source, nbar, width, r_std = load_recorded_aggregates()

    print("Formula branch: recorded prereg-002 aggregates only")
    print(f"source: {source}")
    print("Nbar:", " ".join(f"{x:.0f}" for x in nbar))
    print()

    print_metric_report("W = median |dr|/(2M)", nbar, width)
    if r_std is not None:
        print_metric_report("sigma_rhat = boundary_r_std", nbar, r_std)
    else:
        print("sigma_rhat unavailable: the transcribed result table lacks boundary_r_std precision.")
    print()
    print("E_H unavailable: recorded aggregates do not include mean midpoint or per-seed midpoints.")
    print("Caution: four density levels motivate the O(rho^-1/2) hypothesis;")
    print("they do not establish a stable asymptotic law.")


if __name__ == "__main__":
    main()
