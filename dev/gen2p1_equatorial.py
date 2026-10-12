"""2+1D equatorial Schwarzschild bench, phase A: sprinkling + causal order generator (dev).

Acta: docs/acta_frente_2p1_ecuatorial_2026-10-12.md (signed: front open, phase A authorised).
Order: lemma E1 (research_program/puente_3p1/2026-10-12/E1_equatorial_restriction_lemma.md
section 3), on a rectangular patch K x S^1 in Kruskal (U, V), V > 0:
    dU > 0 and dV > 0 :  x < y  <=>  dist_phi(x, y) <= Delta_max(x, y) = min(pi, sup L[U])
    dU = 0 or dV = 0  :  measure zero for a Poisson sprinkling (never happens; asserted)
Delta_max is the time separation of the 2D metric q(UV)^2 dU dV.

Three stages decide each ordered pair (floats; this is the GROUND-TRUTH GENERATOR, not the
estimator, and it never feeds the estimator anything but the order):
  1. line budget (lower) and Cauchy-Schwarz (upper), 16-node Gauss, all ordered pairs (numba);
  2. calibration upper bound inf_c [W_c(y) - W_c(x)] over the c-grid, per-point tables (numba);
  3. the constant-c geodesic by bisection (dev/explore_b2_calibration_band.py), which gives
     Delta_max up to integration error; pairs closer than TOL to the boundary are counted.
Sprinkling: Poisson, density proportional to the 2+1 volume r C dU dV dphi ~ e^{-s(UV)}
(E1 section 3), by rejection.  Ground truth (coordinates) is returned SEPARATELY from the order.

Usage: .venv/bin/python dev/gen2p1_equatorial.py N [seed]    (timing / consistency report)
"""
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from numba import njit, prange
from scipy.special import lambertw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "dev"))
import explore_b2_calibration_band as cb  # noqa: E402

# Patch: the bridge's frozen patch K(lambda*) (exploration default; prereg-004 fixes the bench's)
V0, V1, UOUT, UIN = (float(x) for x in cb.LAM[:4])
WT = cb.WT                                    # uniform w table
QT = np.sqrt(cb.FT)
W0, DW = float(WT[0]), float(WT[1] - WT[0])
TN, TW = cb.gate.TN, cb.gate.TW
C_LIST = np.array(sorted(cb.PHI))
PHI_TAB = np.stack([np.nan_to_num(cb.PHI[c], nan=np.nan) for c in C_LIST])
C_WLO = np.array([cb.VALID[c][0] for c in C_LIST])
C_WHI = np.array([cb.VALID[c][1] for c in C_LIST])
TOL = 1e-6
SHOOT_STEPS = 256
ST = 1.0 + lambertw(-WT / math.e, 0).real          # s(w) on the w table
DLNF = (1.0 + 3.0 / ST) / (ST * np.exp(ST))       # d ln F / dw, F = q^2


def s_of_w(w):
    return 1.0 + lambertw(-np.asarray(w) / math.e, 0).real


def sprinkle(n_mean, rng):
    """Poisson sprinkling on [-u_out, u_in] x [v0, v1] x [0, 2 pi) with density ~ e^{-s(UV)}."""
    gmax = float(np.exp(-s_of_w(UIN * V1)))         # e^{-s} increases with w; max at w_max
    # expected count of the uniform proposal so that the accepted count is Poisson(n_mean)
    area_mean = float(np.mean(np.exp(-s_of_w(rng.uniform(-UOUT, UIN, 200000)
                                                   * rng.uniform(V0, V1, 200000)))))
    m = rng.poisson(n_mean * gmax / area_mean)
    U = rng.uniform(-UOUT, UIN, m)
    V = rng.uniform(V0, V1, m)
    keep = rng.uniform(0.0, gmax, m) < np.exp(-s_of_w(U * V))
    U, V = U[keep], V[keep]
    phi = rng.uniform(0.0, 2.0 * math.pi, U.size)
    return U, V, phi


@njit(cache=True)
def qi(w):
    x = (w - W0) / DW
    k = int(x)
    if k < 0:
        k = 0
    if k >= QT.size - 1:
        k = QT.size - 2
    t = x - k
    return QT[k] * (1.0 - t) + QT[k + 1] * t


@njit(parallel=True, cache=True)
def stage12(U, V, phi, A, cwlo, cwhi):
    """rel[i,j] = 1 if i < j decided, 0 if decided unrelated, -1 if ambiguous after stage 2."""
    n = U.size
    rel = np.zeros((n, n), np.int8)
    for i in prange(n):
        for j in range(n):
            if i == j:
                continue
            du, dv = U[j] - U[i], V[j] - V[i]
            if not (du > 0.0 and dv > 0.0):
                continue
            d = abs(phi[j] - phi[i])
            if d > math.pi:
                d = 2.0 * math.pi - d
            line = 0.0
            cs = 0.0
            for k in range(TN.size):
                vv = V[i] + dv * TN[k]
                line += TW[k] * qi((U[i] + du * TN[k]) * vv)
                qq = qi(U[j] * vv)
                cs += TW[k] * qq * qq
            line *= math.sqrt(du * dv)
            cs = math.sqrt(du * dv * cs)
            if d <= min(line, math.pi) - TOL:
                rel[i, j] = 1
                continue
            if d > min(cs, math.pi) + TOL:
                continue
            # stage 2: calibration over the c grid valid on the causal rectangle
            w1, w2, w3, w4 = U[i] * V[i], U[i] * V[j], U[j] * V[i], U[j] * V[j]
            wlo = min(min(w1, w2), min(w3, w4))
            whi = max(max(w1, w2), max(w3, w4))
            ub = cs
            for c in range(cwlo.size):
                if wlo >= cwlo[c] and whi <= cwhi[c]:
                    val = A[c, j] - A[c, i]
                    if val < ub:
                        ub = val
            if d > min(ub, math.pi) + TOL:
                continue
            rel[i, j] = -1
    return rel


@njit(cache=True)
def dlnf(w):
    x = (w - W0) / DW
    k = int(x)
    if k < 0:
        k = 0
    if k >= DLNF.size - 1:
        k = DLNF.size - 2
    t = x - k
    return DLNF[k] * (1.0 - t) + DLNF[k + 1] * t


@njit(cache=True)
def _shoot(ua, va, vb, p0, steps):
    """Integrate the geodesic of F(UV) dU dV with V as parameter from (ua, va), slope p0 = dU/dV:
    U' = p, p' = (F'/F)(UV) p (U - V p).  Returns (U at vb, proper time int q(UV) sqrt(p) dV).
    By the U <-> V symmetry the same routine integrates V(U) with the roles exchanged."""
    h = (vb - va) / steps
    U, p, v, L = ua, p0, va, 0.0
    for _ in range(steps):
        k1u = p;                        k1p = dlnf(U * v) * p * (U - v * p)
        u2 = U + 0.5 * h * k1u;         p2 = p + 0.5 * h * k1p;   v2 = v + 0.5 * h
        k2u = p2;                       k2p = dlnf(u2 * v2) * p2 * (u2 - v2 * p2)
        u3 = U + 0.5 * h * k2u;         p3 = p + 0.5 * h * k2p
        k3u = p3;                       k3p = dlnf(u3 * v2) * p3 * (u3 - v2 * p3)
        u4 = U + h * k3u;               p4 = p + h * k3p;         v4 = v + h
        k4u = p4;                       k4p = dlnf(u4 * v4) * p4 * (u4 - v4 * p4)
        l1 = qi(U * v) * math.sqrt(max(p, 0.0))
        l2 = qi(u2 * v2) * math.sqrt(max(p2, 0.0))
        l3 = qi(u3 * v2) * math.sqrt(max(p3, 0.0))
        l4 = qi(u4 * v4) * math.sqrt(max(p4, 0.0))
        L += h * (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0
        U += h * (k1u + 2.0 * k2u + 2.0 * k3u + k4u) / 6.0
        p += h * (k1p + 2.0 * k2p + 2.0 * k3p + k4p) / 6.0
        v = v4
        if p <= 0.0 or U > 10.0 or not math.isfinite(U):
            return math.inf, 0.0
    return U, L


@njit(parallel=True, cache=True)
def shoot_pairs(ua, va, ub, vb, steps):
    """Delta_max by shooting on the log of the initial slope.  The metric F(UV) dU dV is
    symmetric under U <-> V, so each pair is integrated along the coordinate with the LARGER
    increment (V-parametrised for steep pairs is a stiff Riccati equation).  The end value of
    the other coordinate is increasing in the initial slope.  Returns (L, miss)."""
    n = ua.size
    L = np.zeros(n); miss = np.zeros(n)
    for k in prange(n):
        if (ub[k] - ua[k]) > (vb[k] - va[k]):       # parametrise by U: roles swapped
            x0, y0, y1, target = va[k], ua[k], ub[k], vb[k]
        else:                                       # parametrise by V
            x0, y0, y1, target = ua[k], va[k], vb[k], ub[k]
        slope = (target - x0) / (y1 - y0)
        lo, hi = math.log(slope) - 25.0, math.log(slope) + 25.0
        for _ in range(90):
            mid = 0.5 * (lo + hi)
            Xe, _ = _shoot(x0, y0, y1, math.exp(mid), steps)
            if Xe > target:
                hi = mid
            else:
                lo = mid
        Xe, Lk = _shoot(x0, y0, y1, math.exp(0.5 * (lo + hi)), steps)
        L[k] = Lk
        miss[k] = abs(Xe - target) if math.isfinite(Xe) else math.inf
    return L, miss


@njit(parallel=True, cache=True)
def _bounds(U, V, A, cwlo, cwhi, ii, jj):
    n = ii.size
    line = np.zeros(n); ub = np.zeros(n)
    for k in prange(n):
        i, j = ii[k], jj[k]
        du, dv = U[j] - U[i], V[j] - V[i]
        a = 0.0; cs = 0.0
        for t in range(TN.size):
            vv = V[i] + dv * TN[t]
            a += TW[t] * qi((U[i] + du * TN[t]) * vv)
            qq = qi(U[j] * vv)
            cs += TW[t] * qq * qq
        line[k] = math.sqrt(du * dv) * a
        best = math.sqrt(du * dv * cs)
        w1, w2, w3, w4 = U[i] * V[i], U[i] * V[j], U[j] * V[i], U[j] * V[j]
        wlo = min(min(w1, w2), min(w3, w4)); whi = max(max(w1, w2), max(w3, w4))
        for c in range(cwlo.size):
            if wlo >= cwlo[c] and whi <= cwhi[c]:
                val = A[c, j] - A[c, i]
                if val < best:
                    best = val
        ub[k] = best
    return line, ub


def bounds_pairs(U, V, A, ii, jj):
    return _bounds(U, V, A, C_WLO, C_WHI, ii.astype(np.int64), jj.astype(np.int64))


def point_tables(U, V):
    """A[c, i] = c ln V_i + Phi_c(U_i V_i)  (NaN outside the validity of c)."""
    w = U * V
    nu = np.log(V)
    A = np.empty((C_LIST.size, U.size))
    for k, c in enumerate(C_LIST):
        A[k] = c * nu + np.interp(w, WT, PHI_TAB[k])
    return A


def generate(n_mean, seed):
    rng = np.random.default_rng(seed)
    t0 = time.time()
    U, V, phi = sprinkle(n_mean, rng)
    n = U.size
    assert np.unique(U).size == n and np.unique(V).size == n      # no dU = 0 / dV = 0 pair
    A = point_tables(U, V)
    rel = stage12(U, V, phi, A, C_WLO, C_WHI)
    t12 = time.time() - t0
    amb_mask = rel == -1
    ii, jj = np.nonzero(amb_mask)
    near = 0
    if ii.size:
        d = np.abs(phi[jj] - phi[ii]); d = np.minimum(d, 2 * math.pi - d)
        L, miss = shoot_pairs(U[ii], V[ii], U[jj], V[jj], SHOOT_STEPS)
        assert np.all(miss < 1e-9), "shooting missed the endpoint on %d pairs" % int((miss >= 1e-9).sum())
        # consistency: the geodesic is an admissible curve (>= line) and below every upper bound
        line, ub = bounds_pairs(U, V, A, ii, jj)
        assert np.all(L >= line - 1e-9) and np.all(L <= ub + 1e-9), "geodesic outside [line, UB]"
        dmax = np.minimum(L, math.pi)
        near = int((np.abs(d - dmax) < TOL).sum())
        rel[ii, jj] = (d <= dmax).astype(np.int8)
    order = rel.astype(bool)
    # audit: a sample of pairs decided in stages 1-2, recomputed with the exact geodesic
    staged = (U[None, :] > U[:, None]) & (V[None, :] > V[:, None]) & ~amb_mask
    si, sj = np.nonzero(staged)
    pick = rng.choice(si.size, size=min(20000, si.size), replace=False)
    a_i, a_j = si[pick], sj[pick]
    La, ma = shoot_pairs(U[a_i], V[a_i], U[a_j], V[a_j], SHOOT_STEPS)
    da = np.abs(phi[a_j] - phi[a_i]); da = np.minimum(da, 2 * math.pi - da)
    exact = da <= np.minimum(La, math.pi)
    hit = ma < 1e-9
    audit = {"sample": int(pick.size), "endpoint_failures": int((~hit).sum()),
             "disagreements_among_hit": int((exact[hit] != order[a_i, a_j][hit]).sum()),
             "failed_pairs_UaUbVaVb": np.c_[U[a_i], U[a_j], V[a_i], V[a_j]][~hit][:5].tolist()}
    stats = {"n": int(n), "ordered_pairs": int(((U[None, :] > U[:, None]) & (V[None, :] > V[:, None])).sum()),
             "relations": int(order.sum()), "stage3_pairs": int(ii.size),
             "near_boundary_pairs_tol": near, "tol": TOL,
             "seconds_stage12": round(t12, 1), "seconds_total": round(time.time() - t0, 1),
             "audit_stage12_vs_exact": audit}
    return order, (U, V, phi), stats


def transitivity_violations(order):
    """Number of (i,k) with i<j<k but not i<k.  A causal order must give 0."""
    A = order.astype(np.float32)
    two = (A @ A) > 0.5
    return int((two & ~order).sum())


def main():
    n_mean = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    order, _, stats = generate(n_mean, seed)
    t = time.time()
    stats["transitivity_violations"] = transitivity_violations(order)
    stats["seconds_transitivity"] = round(time.time() - t, 1)
    print(json.dumps(stats, indent=1))


if __name__ == "__main__":
    main()
