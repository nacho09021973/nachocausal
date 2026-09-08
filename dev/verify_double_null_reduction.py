"""EXPLORATION (dev/) — verifier for dev/PAPER2_DOUBLE_NULL_REDUCTION.md.

Two checks, neither of them statistical:

  1. Algebraic cross-check of Theorem 1 against the FROZEN past_matrix_fast, on
     deterministic point sets in six regimes.
  2. Symbolic verification (sympy) of the chart identities of Lemmas 1-2 and
     Theorem 2.

Reads `nachocausal.generator` and evaluates it; modifies nothing. No sprinkling
statistic is produced and no seed band is touched.

Run:  python3 dev/verify_double_null_reduction.py      -> exit 0 iff all pass
"""

from __future__ import annotations

import os
import sys

import numpy as np

# dev/ scripts are run from the repo root; make the import work regardless of cwd
# without touching the package itself.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nachocausal.generator import past_matrix_fast  # noqa: E402

VERIFY_SEED = 20260908


def R_of(r: np.ndarray, r_S: float) -> np.ndarray:
    """Outgoing null coordinate of the t* chart (this is `func`, NOT the
    tortoise coordinate: R' = (2-f)/f, whereas r_*' = 1/f)."""
    return r + 2.0 * r_S * np.log(np.abs(r - r_S) / r_S)


def theorem1(pts: np.ndarray, r_S: float) -> np.ndarray:
    """C[i, j] = True iff j precedes i, from the double-null characterisation.

    exterior block : v_j <= v_i and U_j <= U_i
    interior block : v_j <= v_i and W_j <= W_i      (W = -U)
    inward cross   : v_j <= v_i                     (outgoing coord absent)
    outward cross  : never
    """
    t, r = pts[:, 0], pts[:, 1]
    v = t + r
    U = t - R_of(r, r_S)
    W = -U
    vi, vj = v[:, None], v[None, :]
    Ui, Uj = U[:, None], U[None, :]
    Wi, Wj = W[:, None], W[None, :]
    ext_i, ext_j = (r > r_S)[:, None], (r > r_S)[None, :]
    out = np.where(
        ext_i & ext_j,
        (vi >= vj) & (Ui >= Uj),
        np.where(
            ~ext_i & ~ext_j,
            (vi >= vj) & (Wi >= Wj),
            np.where(ext_j & ~ext_i, vi >= vj, False),
        ),
    )
    np.fill_diagonal(out, False)
    return out


def _case(name: str, pts: np.ndarray, r_S: float) -> tuple[int, int]:
    C = past_matrix_fast(pts, "BH", r_S)
    P = theorem1(pts, r_S)
    bad = int(np.count_nonzero(C != P))
    n = pts.shape[0]
    print(
        f"  {'OK      ' if bad == 0 else 'MISMATCH'}  {name:38s} "
        f"N={n:5d} pairs={n * n:9d} relations={int(C.sum()):8d} mismatches={bad}"
    )
    return bad, n * n


def check_algebraic() -> tuple[int, int]:
    rng = np.random.default_rng(VERIFY_SEED)
    bad = pairs = 0
    cases = []
    p = np.column_stack([rng.random(700) * 6.0, 0.1 + rng.random(700) * 1.2])
    cases.append(("frozen box t[0,6] r[0.1,1.3]", p, 0.5))
    p = np.column_stack([rng.random(700) * 20.0, 0.01 + rng.random(700) * 5.0])
    cases.append(("wide domain r[0.01,5.01]", p, 0.5))
    p = np.column_stack([rng.random(500) * 6.0, 0.51 + rng.random(500) * 3.0])
    cases.append(("exterior only r>r_S", p, 0.5))
    p = np.column_stack([rng.random(500) * 6.0, 0.001 + rng.random(500) * 0.498])
    cases.append(("interior only r<r_S", p, 0.5))
    d = 10.0 ** (-rng.uniform(1, 9, 600))
    p = np.column_stack(
        [rng.random(600) * 6.0, 0.5 + np.where(rng.random(600) < 0.5, -d, d)]
    )
    cases.append(("near-horizon |r-r_S| in [1e-9,1e-1]", p, 0.5))
    p = np.column_stack([rng.random(500) * 30.0, 0.05 + rng.random(500) * 8.0])
    cases.append(("r_S=2.0, r[0.05,8.05]", p, 2.0))
    print("1. Theorem 1 vs frozen past_matrix_fast(kind='BH')")
    for name, pts, rs in cases:
        b, n = _case(name, pts, rs)
        bad += b
        pairs += n
    return bad, pairs


def check_symbolic() -> int:
    try:
        import sympy as sp
    except ImportError:
        print("2. symbolic checks SKIPPED (sympy not installed)")
        return 0
    r, rS, Lam = sp.symbols("r r_S Lambda", positive=True)
    f = 1 - rS / r
    Rp = sp.simplify(sp.diff(r + 2 * rS * sp.log(r - rS), r))  # R' on r > r_S
    g = Lam * sp.Matrix([[1, (1 - Rp) / 2], [(1 - Rp) / 2, -Rp]])
    J = sp.Matrix([[1, 1], [1, -Rp]]).det()
    psi_p = sp.simplify(sp.diff(r + (r + 2 * rS * sp.log(r - rS)), r))
    checks = [
        ("Lemma 1   R' = (2-f)/f", sp.simplify(Rp - (2 - f) / f) == 0),
        ("Lemma 2   det g = -1 at Lambda = f", sp.simplify(g.subs(Lam, f).det() + 1) == 0),
        ("Lemma 2   g_00 = f", sp.simplify(g.subs(Lam, f)[0, 0] - f) == 0),
        ("Lemma 2   g_01 = -(1-f)", sp.simplify(2 * g.subs(Lam, f)[0, 1] + 2 * (1 - f)) == 0),
        ("Lemma 2   g_11 = f-2", sp.simplify(g.subs(Lam, f)[1, 1] - (f - 2)) == 0),
        ("Thm 2     det d(v,U)/d(t*,r) = -2/f", sp.simplify(J + 2 / f) == 0),
        ("Thm 2     dt* dr = (|f|/2) dv dU", sp.simplify(1 / sp.Abs(J) - sp.Abs(f) / 2) == 0),
        ("Sec 2     psi' = 2r/(r-r_S)", sp.simplify(psi_p - 2 * r / (r - rS)) == 0),
    ]
    print("\n2. Symbolic chart identities")
    bad = 0
    for name, ok in checks:
        print(f"  {'OK      ' if ok else 'FAIL    '}  {name}")
        bad += 0 if ok else 1
    return bad


def main() -> int:
    bad_a, pairs = check_algebraic()
    bad_s = check_symbolic()
    print(
        f"\nRESULT: {'ALL CHECKS PASS' if bad_a + bad_s == 0 else 'FAILURES'}"
        f"  ({pairs} ordered pairs compared, {bad_a} mismatches; "
        f"{bad_s} symbolic failures)"
    )
    return 0 if bad_a + bad_s == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
