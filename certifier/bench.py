"""Reference bench for the OP-2.1 positive certifier (dev prereg OP21 §§4-6).

Not part of the prereg-002 evaluation path.

Everything numeric here is frozen in dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md:
the cells, the seed-derivation rule over SYNTH_MC_BAND, N_REP, the exact reference
miscoverage (computed from the frozen radius FORMULA, independent of the kernel under
test), the criteria C1-C6 and the terminal precedence chain. The bench certifies a
statistics tool; it makes no physical statement of any kind.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
import subprocess
import time
from dataclasses import dataclass

import numpy as np

from certifier import kernel
from certifier.kernel import (
    STATE_ABSTAIN_GENERATOR_ERROR,
    STATE_ABSTAIN_PRECISION,
    STATE_BOUND_POSITIVE,
    STATE_ZERO_BOUND,
)
from certifier.ledger import CertificationLedger

# --- Frozen bench constants (dev prereg OP21 §4) ------------------------------

SYNTH_MC_BAND = (3_000_000, 3_999_999)
N_REP = 200_000
ALPHA_TOTAL_BENCH = 0.50

TERMINAL_INVALID = "POSITIVE_CERTIFIER_INVALID"
TERMINAL_REPRODUCIBILITY_FAIL = "REFERENCE_REPRODUCIBILITY_FAIL"
TERMINAL_COVERAGE_FAIL = "REFERENCE_COVERAGE_FAIL"
TERMINAL_PRECISION_ABSTAIN = "REFERENCE_PRECISION_ABSTAIN"
TERMINAL_PASS = "POSITIVE_CERTIFIER_REFERENCE_PASS"

# Total, deterministic precedence (dev prereg OP21 §6; mirrors op13:190-208).
TERMINAL_PRECEDENCE = (
    TERMINAL_INVALID,
    TERMINAL_REPRODUCIBILITY_FAIL,
    TERMINAL_COVERAGE_FAIL,
    TERMINAL_PRECISION_ABSTAIN,
    TERMINAL_PASS,
)


class SeedBandError(RuntimeError):
    """A seed outside SYNTH_MC_BAND or outside the frozen derivation rule (G3)."""


def synth_seed(cell_index: int, stream_offset: int) -> int:
    """Frozen derivation rule (dev prereg OP21 §4.1): base + 1000*k (+500 for Q)."""
    if stream_offset not in (0, 500):
        raise SeedBandError(f"stream_offset must be 0 (P) or 500 (Q), got {stream_offset}")
    seed = SYNTH_MC_BAND[0] + 1000 * cell_index + stream_offset
    if not (SYNTH_MC_BAND[0] <= seed <= SYNTH_MC_BAND[1]):
        raise SeedBandError(f"derived seed {seed} leaves SYNTH_MC_BAND {SYNTH_MC_BAND}")
    return seed


@dataclass(frozen=True)
class BenchCell:
    cell_id: str
    kind: str            # "bernoulli" | "uniform_split" | "pr011"
    tilde_p: float       # generated P success prob (bernoulli only)
    tilde_q: float       # generated Q success prob (bernoulli only)
    m: int
    alpha_j: float
    eps_p: float
    eps_q: float
    tv_true: float | None   # None => resolved at runtime (pr011 enumeration)
    calibrated: bool        # C2 applies (exact p0 computable, bernoulli only)


# Frozen cell list, in seed-index order k = 0..5 (dev prereg OP21 §4.2).
CELLS: tuple[BenchCell, ...] = (
    BenchCell("CELL-B1", "bernoulli", 0.50, 0.80, 200, 0.01, 0.0, 0.0, 0.30, True),
    BenchCell("CELL-B0", "bernoulli", 0.50, 0.50, 200, 0.01, 0.0, 0.0, 0.00, True),
    BenchCell("CELL-CAL", "bernoulli", 0.50, 0.50, 50, 0.25, 0.0, 0.0, 0.00, True),
    BenchCell("CELL-EPS", "bernoulli", 0.65, 0.35, 200, 0.10, 0.15, 0.15, 0.00, True),
    BenchCell("CELL-U", "uniform_split", math.nan, math.nan, 200, 0.05, 0.0, 0.0, 1.00, False),
    BenchCell("CELL-PR011", "pr011", math.nan, math.nan, 200, 0.04, 0.0, 0.0, None, False),
)


# --- Exact reference miscoverage (dev prereg OP21 §4.3) -----------------------
# Computed from the FORMULA frozen in the prereg, independently of certifier.kernel.

def _reference_radius(m: int, alpha: float) -> float:
    return math.sqrt(math.log(4.0 / alpha) / (2.0 * m))


def _binomial_pmf(m: int, p: float) -> np.ndarray:
    k = np.arange(m + 1, dtype=float)
    log_pmf = (
        math.lgamma(m + 1)
        - np.array([math.lgamma(x + 1) for x in k])
        - np.array([math.lgamma(m - x + 1) for x in k])
        + k * math.log(p)
        + (m - k) * math.log(1.0 - p)
    )
    return np.exp(log_pmf)


def exact_miscoverage_bernoulli(cell: BenchCell) -> float:
    """P( |X/m - Y/m| > tv_true + r_p + r_q + eps_p + eps_q ), X~Bin(m,tilde_p), Y~Bin(m,tilde_q)."""
    r = _reference_radius(cell.m, cell.alpha_j)
    threshold = cell.tv_true + 2.0 * r + cell.eps_p + cell.eps_q
    pmf_p = _binomial_pmf(cell.m, cell.tilde_p)
    pmf_q = _binomial_pmf(cell.m, cell.tilde_q)
    frac = np.arange(cell.m + 1, dtype=float) / cell.m
    mask = np.abs(frac[:, None] - frac[None, :]) > threshold
    return float((pmf_p[:, None] * pmf_q[None, :])[mask].sum())


# --- PR011 quarantined integration fixture (dev prereg OP21 §4.2, BENCH_ONLY) --

_PR011_CACHE: dict | None = None


def _pr011_fixture() -> dict:
    """Poset laws (read-only from the PR011 enumeration module) pushed through the
    BENCH_ONLY_NON_PROMOTABLE witness f_bench(poset) = |relations| / 6.

    f_bench is not a witness candidate, never seeds OP-2.2, and appears in no
    promotion/feature/orientation/frontier/abstention decision (op13:98-104).
    """
    global _PR011_CACHE
    if _PR011_CACHE is not None:
        return _PR011_CACHE
    from dev import pr011_tv_certification_enumeration as enum

    n, grid_m = 4, 12
    n_pairs = n * (n - 1) // 2  # C(4,2) = 6
    laws = []
    for tau in enum.TAU_PAIR:
        fam, copula = enum.build_diamond_family(tau)
        grid = enum.copula_grid(copula, fam, grid_m)
        raw = enum.poset_law_from_grid(grid, n)
        law, _ = enum.normalize_law(raw)
        keys = sorted(law, key=lambda key: (len(key), sorted(key)))
        values = np.array([len(key) / n_pairs for key in keys], dtype=float)
        probs = np.array([law[key] for key in keys], dtype=float)
        laws.append((values, probs / probs.sum()))
    tv_exact = enum.enumerate_tv(n, enum.TAU_PAIR[0], enum.TAU_PAIR[1], grid_m=grid_m).tv
    _PR011_CACHE = {"laws": laws, "tv_exact": float(tv_exact)}
    return _PR011_CACHE


# --- Stream draws (frozen seed rule; the only RNG use in certifier/) -----------

def _drawers(cell: BenchCell, cell_index: int):
    rng_p = np.random.default_rng(synth_seed(cell_index, 0))
    rng_q = np.random.default_rng(synth_seed(cell_index, 500))
    if cell.kind == "bernoulli":
        def draw_p():
            return (rng_p.random(cell.m) < cell.tilde_p).astype(float)

        def draw_q():
            return (rng_q.random(cell.m) < cell.tilde_q).astype(float)
    elif cell.kind == "uniform_split":
        def draw_p():
            return 0.5 * rng_p.random(cell.m)

        def draw_q():
            return 0.5 + 0.5 * rng_q.random(cell.m)
    elif cell.kind == "pr011":
        fixture = _pr011_fixture()
        (values_p, probs_p), (values_q, probs_q) = fixture["laws"]

        def draw_p():
            return values_p[rng_p.choice(values_p.size, size=cell.m, p=probs_p)]

        def draw_q():
            return values_q[rng_q.choice(values_q.size, size=cell.m, p=probs_q)]
    else:  # pragma: no cover - frozen cell list
        raise ValueError(f"unknown cell kind {cell.kind!r}")
    return draw_p, draw_q


def _resolved_tv_true(cell: BenchCell) -> float:
    if cell.tv_true is not None:
        return cell.tv_true
    return _pr011_fixture()["tv_exact"]


# --- Single bench pass ---------------------------------------------------------

def _single_pass(n_rep: int) -> dict:
    """One full pass over the frozen cells. Exercises the REAL kernel entry point
    (module attribute lookup, so the designated mutation points apply)."""
    ledger = CertificationLedger(ALPHA_TOTAL_BENCH)
    for cell in CELLS:
        ledger.register_cell(
            cell.cell_id, cell.m, cell.m, cell.alpha_j, cell.eps_p, cell.eps_q
        )
    ledger.freeze()

    cells_report: dict[str, dict] = {}
    for k, cell in enumerate(CELLS):
        draw_p, draw_q = _drawers(cell, k)
        tv_true = _resolved_tv_true(cell)
        count = 0
        max_tv_lower = 0.0
        for _ in range(n_rep):
            cert = kernel.certify_tv_lower(
                draw_p(), draw_q(), cell.alpha_j, cell.eps_p, cell.eps_q
            )
            if cert.state not in (STATE_BOUND_POSITIVE, STATE_ZERO_BOUND):
                raise RuntimeError(
                    f"{cell.cell_id}: unexpected abstention {cert.state} in coverage MC"
                )
            if cert.tv_lower > max_tv_lower:
                max_tv_lower = cert.tv_lower
            if cert.tv_lower > tv_true:
                count += 1
        # One ledger-certified certificate per cell (continuing the same frozen
        # RNG streams) for the op13-style manifest.
        ledger.certify_cell(cell.cell_id, draw_p(), draw_q())
        p0 = exact_miscoverage_bernoulli(cell) if cell.calibrated else None
        cells_report[cell.cell_id] = {
            "kind": cell.kind,
            "m": cell.m,
            "alpha_j": cell.alpha_j,
            "eps_p": cell.eps_p,
            "eps_q": cell.eps_q,
            "tv_true": tv_true,
            "n_rep": n_rep,
            "miscoverage_count": count,
            "max_tv_lower": max_tv_lower,
            "p0_exact": p0,
            "c1_limit": n_rep * cell.alpha_j,
            "c2_limit": (
                None if p0 is None
                else n_rep * p0 + max(5.0 * math.sqrt(n_rep * p0 * (1.0 - p0)), 6.0)
            ),
        }

    # C5 — abstention semantics (deterministic; dev prereg OP21 §5).
    half = np.full(16, 0.5)
    c5 = {
        "generator_error_none": kernel.certify_tv_lower(half, half, 0.1, None, 0.0).state,
        "generator_error_nan": kernel.certify_tv_lower(half, half, 0.1, math.nan, 0.0).state,
        "precision": kernel.certify_tv_lower(
            half, half, 0.1, 0.0, 0.0, precision_budget=0.01
        ).state,
        "zero_bound": kernel.certify_tv_lower(half, half, 0.1, 0.0, 0.0).state,
    }

    manifest = ledger.manifest()
    for entry in manifest["cells"].values():
        entry["certified_at_unix"] = None  # volatile; excluded from the frozen hash

    return {"cells": cells_report, "c5": c5, "ledger_manifest": manifest}


def _canonical_hash(frozen_report: dict) -> str:
    payload = json.dumps(frozen_report, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# --- Criteria (dev prereg OP21 §5) ----------------------------------------------

def _coverage_criteria(pass_report: dict) -> dict:
    c1_fail, c2_fail, c6_fail = [], [], []
    for cell_id, cell in pass_report["cells"].items():
        if cell["miscoverage_count"] > cell["c1_limit"]:
            c1_fail.append(cell_id)
        if cell["c2_limit"] is not None and cell["miscoverage_count"] > cell["c2_limit"]:
            c2_fail.append(cell_id)
        if cell["max_tv_lower"] < 0.0:
            c6_fail.append(cell_id)
    u_cell = pass_report["cells"]["CELL-U"]
    if not (u_cell["max_tv_lower"] < u_cell["tv_true"]):
        c6_fail.append("CELL-U")
    c5 = pass_report["c5"]
    c5_ok = (
        c5["generator_error_none"] == STATE_ABSTAIN_GENERATOR_ERROR
        and c5["generator_error_nan"] == STATE_ABSTAIN_GENERATOR_ERROR
        and c5["precision"] == STATE_ABSTAIN_PRECISION
        and c5["zero_bound"] == STATE_ZERO_BOUND
    )
    return {
        "c1_fail_cells": sorted(c1_fail),
        "c2_fail_cells": sorted(c2_fail),
        "c5_ok": c5_ok,
        "c6_fail_cells": sorted(c6_fail),
        "coverage_ok": not (c1_fail or c2_fail or c6_fail),
    }


# --- Designated mutants (dev prereg OP21 §5 C4) ---------------------------------

def _mutant_a_radius(m: int, alpha: float) -> float:
    """Anti-conservative radius: log(2/alpha) instead of log(4/alpha)."""
    return math.sqrt(math.log(2.0 / alpha) / (2.0 * m))


def _mutant_b_eps_term(eps_p: float, eps_q: float) -> float:
    """Silently dropped generator-error terms."""
    return 0.0


def _run_mutant(name: str, attr: str, mutant, n_rep: int) -> dict:
    original = getattr(kernel, attr)
    setattr(kernel, attr, mutant)
    try:
        report = _single_pass(n_rep)
    finally:
        setattr(kernel, attr, original)
    criteria = _coverage_criteria(report)
    return {
        "mutant": name,
        "detected": not criteria["coverage_ok"],
        "c1_fail_cells": criteria["c1_fail_cells"],
        "c2_fail_cells": criteria["c2_fail_cells"],
    }


# --- Full bench + terminal (dev prereg OP21 §§5-7) -------------------------------

def run_bench(n_rep: int = N_REP, issue_terminal: bool = False) -> dict:
    """Run the frozen bench. `issue_terminal=True` is reserved for the single
    authorized terminal-issuing run (dev prereg OP21 §7); dev-loop calls use the
    default and may not be cited."""
    started = time.time()
    volatile = {
        "started_unix": started,
        "numpy": np.__version__,
        "uname": platform.uname()._asdict(),
        "n_rep": n_rep,
        "issue_terminal": issue_terminal,
        "seed_rule": "default_rng(3_000_000 + 1000*k [+500 for Q]) per dev prereg OP21 §4.1",
    }
    try:
        volatile["commit"] = subprocess.run(
            ["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception:  # noqa: BLE001 - provenance best-effort outside a checkout
        volatile["commit"] = None

    diagnostics: list[str] = []
    terminal = None
    frozen: dict = {}
    try:
        from nachocausal import thresholds as _th  # read-only: env pin + band constants (G2)
        _th.assert_environment()

        if issue_terminal and n_rep != N_REP:
            terminal = TERMINAL_PRECISION_ABSTAIN
            diagnostics.append(
                f"terminal requested with n_rep={n_rep} != frozen N_REP={N_REP}"
            )
        else:
            mutants = [
                _run_mutant("MUT-A", "hoeffding_radius", _mutant_a_radius, n_rep),
                _run_mutant("MUT-B", "_eps_term", _mutant_b_eps_term, n_rep),
            ]
            c4_ok = all(m["detected"] for m in mutants)

            pass_1 = _single_pass(n_rep)
            pass_2 = _single_pass(n_rep)
            hash_1, hash_2 = _canonical_hash(pass_1), _canonical_hash(pass_2)
            c3_ok = hash_1 == hash_2
            criteria = _coverage_criteria(pass_1)

            frozen = {
                "cells": pass_1["cells"],
                "c5": pass_1["c5"],
                "ledger_manifest": pass_1["ledger_manifest"],
                "criteria": {**criteria, "c3_ok": c3_ok, "c4_ok": c4_ok},
                "mutants": mutants,
                "report_hash_run1": hash_1,
                "report_hash_run2": hash_2,
            }
            if not criteria["c5_ok"]:
                terminal = TERMINAL_INVALID
                diagnostics.append("C5 abstention-state semantics violated")
            elif not c3_ok:
                terminal = TERMINAL_REPRODUCIBILITY_FAIL
            elif not (criteria["coverage_ok"] and c4_ok):
                terminal = TERMINAL_COVERAGE_FAIL
                if not c4_ok:
                    diagnostics.append("MUTATION_POWER_MISSING: the bench is decoration")
            else:
                terminal = TERMINAL_PASS
    except Exception as exc:  # guard/ledger/seed-band integrity broken
        terminal = TERMINAL_INVALID
        diagnostics.append(f"{type(exc).__name__}: {exc}")

    volatile["ended_unix"] = time.time()
    assert terminal in TERMINAL_PRECEDENCE
    return {
        "terminal": terminal,
        "diagnostics": diagnostics,
        "frozen": frozen,
        "volatile": volatile,
    }


def main(argv: list[str] | None = None) -> int:
    """CLI for the bench. `--terminal` marks the single authorized terminal-issuing
    run (dev prereg OP21 §7). The exit code is 0 whenever a terminal was emitted:
    PASS, FAIL and ABSTAIN are reported alike (plan:646-663)."""
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--terminal", action="store_true",
                        help="the one-shot terminal-issuing run (requires frozen prereg)")
    parser.add_argument("--n-rep", type=int, default=N_REP)
    parser.add_argument("--out", default=None, help="write the full JSON report here")
    args = parser.parse_args(argv)

    report = run_bench(n_rep=args.n_rep, issue_terminal=args.terminal)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, sort_keys=True, indent=2), encoding="utf-8")
    for cell_id, cell in sorted(report.get("frozen", {}).get("cells", {}).items()):
        print(f"{cell_id}: count={cell['miscoverage_count']} "
              f"c1_limit={cell['c1_limit']:.1f} "
              f"c2_limit={'-' if cell['c2_limit'] is None else format(cell['c2_limit'], '.1f')} "
              f"p0={'-' if cell['p0_exact'] is None else format(cell['p0_exact'], '.3g')}")
    for mutant in report.get("frozen", {}).get("mutants", []):
        print(f"{mutant['mutant']}: detected={mutant['detected']} "
              f"(C1 fail: {mutant['c1_fail_cells']}, C2 fail: {mutant['c2_fail_cells']})")
    for line in report["diagnostics"]:
        print(f"diagnostic: {line}")
    print(f"OP21_TERMINAL={report['terminal']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
