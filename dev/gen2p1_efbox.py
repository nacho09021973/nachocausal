"""2+1D equatorial Schwarzschild bench, phase B: generator on the 1+1D-style tall EF box (dev).

Acta: docs/acta_frente_2p1_ecuatorial_2026-10-12.md (phase B signed).  Geometry mirrors the
sealed 1+1D bench (nachocausal/thresholds.py): ingoing Eddington-Finkelstein time t* in
[0, T_EDGE], r in [R_LO, R_HI] = [0.1, 1.3], 2M = 0.5, plus phi in S^1.
    metric  -(1-2M/r) dv^2 + 2 dv dr + r^2 dphi^2,  v = t* + r,  sqrt(-g) = r
so the sprinkle is uniform in (t*, phi) and has density ~ r in r.
Kruskal map (4M = 1):  s = r/2M,  V = e^v,  w = UV = (1-s) e^s,  U = w / V.
Order (lemma E1 section 3, ambient spacetime: every causal rectangle of two points of the box
lies in {V > 0, UV < 1}):  x < y  <=>  U_x < U_y, V_x < V_y and dist_phi <= min(pi, sup L).
Stages: (1) line budget below / Cauchy-Schwarz above, 64-node Gauss with a relative safety
margin; (3) the (U,V) geodesic shot for the rest (as dev/gen2p1_equatorial.py).
Tables in z = log(1 - w), because w spans ~[-3e4, 0.98] here.
MINK control: the same cloud with the flat 2+1 order  dt >= |x - y|  in polar (r, phi).
Usage: .venv/bin/python dev/gen2p1_efbox.py N seed
"""
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from numba import njit, prange
from scipy.special import lambertw, roots_legendre

ROOT = Path(__file__).resolve().parents[1]

import os
T_EDGE = float(os.environ.get("NC2P1_T_EDGE", "6.0"))   # dev knob for the T-dependence probe
R_LO, R_HI, TWO_M = 0.1, 1.3, 0.5
FOUR_M = 2.0 * TWO_M
EXPLORE_BAND = (7_000_000, 7_000_999)          # 2+1 exploration seeds (phase B)
VIRGIN_BAND = (8_000_000, 8_999_999)           # reserved for prereg-004; never used here
TOL, REL_MARGIN = 1e-6, 1e-3
SHOOT_STEPS = 4096          # legacy linear integrator (kept for reference only)
COARSE = (128, 512)         # (steps in ln V, steps in U): max error 4.1e-3 on 20k pairs
FINE = (2048, 8192)         # converged to ~1e-7 (1024 vs 2048 differ by 1.7e-6)
COARSE_MARGIN = 0.05        # > 10x the measured coarse error
N_HYP = 48

# z range: w_min ~ (1 - s_max) e^{s_max} * e^{T + R_HI - R_LO}; margin of 1 in z
ZMIN = -4.0
ZMAX = math.log(1.0 + 21.6 * math.exp(T_EDGE + 1.2)) + 1.0
NZ = int(round((ZMAX - ZMIN) / 3.6e-5)) + 1
ZT = np.linspace(ZMIN, ZMAX, NZ)
_W = 1.0 - np.exp(ZT)
_S = 1.0 + lambertw(-_W / math.e, 0).real
QT = 2.0 * np.exp(-_S / 2.0) / _S ** 1.5
DLNF = (1.0 + 3.0 / _S) / (_S * np.exp(_S))
DZ = (ZMAX - ZMIN) / (NZ - 1)
# calibration W_c = c ln V + Phi_c(w), Phi_c' = F / (2 (c + sqrt(c^2 + F w))), on a z grid
NZC = 20001
ZC = np.linspace(ZMIN, ZMAX, NZC)
WC = 1.0 - np.exp(ZC)                                     # decreasing in z
_SC = 1.0 + lambertw(-WC / math.e, 0).real
FC = (2.0 * np.exp(-_SC / 2.0) / _SC ** 1.5) ** 2
C_LIST = np.concatenate([np.geomspace(1e-4, 1e3, 400), -np.geomspace(1e-4, 1e3, 200)])


def _phi_table(c):
    """Phi_c(w) on WC (NaN where c is invalid); valid set = one w-interval."""
    disc = c * c + FC * WC
    den = c + np.sqrt(np.maximum(disc, 0.0))
    ok = (disc >= 0.0) & (den > 0.0) & ((c >= 0.0) | (WC > 0.0))
    fp = FC / (2.0 * np.where(ok, den, 1.0))
    out = np.full(WC.shape, np.nan)
    idx = np.nonzero(ok)[0]
    if idx.size < 2 or np.any(np.diff(idx) != 1):
        return out, (np.nan, np.nan)
    i0, i1 = idx[0], idx[-1]
    # integrate in w (WC decreases with index): Phi(w) relative to the largest valid w
    seg = 0.5 * (fp[i0 + 1:i1 + 1] + fp[i0:i1]) * (WC[i0 + 1:i1 + 1] - WC[i0:i1])
    out[i0:i1 + 1] = np.concatenate([[0.0], np.cumsum(seg)])
    return out, (WC[i1], WC[i0])


_PT = [_phi_table(c) for c in C_LIST]
PHI_TAB = np.stack([x[0] for x in _PT])
C_WLO = np.array([x[1][0] for x in _PT]); C_WHI = np.array([x[1][1] for x in _PT])
_keep = np.isfinite(C_WLO)
C_LIST, PHI_TAB, C_WLO, C_WHI = C_LIST[_keep], PHI_TAB[_keep], C_WLO[_keep], C_WHI[_keep]


def point_tables(U, V):
    """A[c, i] = c ln V_i + Phi_c(w_i); interpolation in z (WC is decreasing)."""
    z = np.log(1.0 - U * V)
    A = np.empty((C_LIST.size, U.size))
    for k, c in enumerate(C_LIST):
        A[k] = c * np.log(V) + np.interp(z, ZC, PHI_TAB[k])
    return A


GN, GW = roots_legendre(64)
GN, GW = (GN + 1.0) / 2.0, GW / 2.0


def to_kruskal(t, r):
    s = r / TWO_M
    V = np.exp((t + r) / FOUR_M)
    w = (1.0 - s) * np.exp(s)
    return w / V, V


def sprinkle(n_mean, rng):
    """Poisson with density ~ r on [0,T] x [R_LO,R_HI] x S^1 (sqrt(-g) = r)."""
    n = rng.poisson(n_mean)
    t = rng.uniform(0.0, T_EDGE, n)
    r = np.sqrt(rng.uniform(R_LO ** 2, R_HI ** 2, n))      # density ~ r
    phi = rng.uniform(0.0, 2.0 * math.pi, n)
    return t, r, phi


@njit(cache=True)
def _tab(T, w):
    z = math.log(1.0 - w)
    x = (z - ZMIN) / DZ
    k = int(x)
    if k < 0:
        k = 0
    if k >= T.size - 1:
        k = T.size - 2
    a = x - k
    return T[k] * (1.0 - a) + T[k + 1] * a


@njit(cache=True)
def qi(w):
    return _tab(QT, w)


@njit(cache=True)
def dlnf(w):
    return _tab(DLNF, w)


@njit(parallel=True, cache=True)
def stage1(U, V, phi, A, cwlo, cwhi):
    n = U.size
    rel = np.zeros((n, n), np.int8)
    for i in prange(n):
        for j in range(n):
            du, dv = U[j] - U[i], V[j] - V[i]
            if not (du > 0.0 and dv > 0.0):
                continue
            d = abs(phi[j] - phi[i])
            if d > math.pi:
                d = 2.0 * math.pi - d
            line = 0.0
            for k in range(GN.size):
                line += GW[k] * qi((U[i] + du * GN[k]) * (V[i] + dv * GN[k]))
            line *= math.sqrt(du * dv)
            # orbit curve: move in U to the hyperbola w = wm < 0, follow it from V_i to V_j,
            # move in U to y; admissible for wm in [w_i, w_j], wm < 0.  Exact angular reach
            # q(wm) sqrt(-wm) ln(V_j / V_i).  Max over N_HYP points of the interval.
            wa, wb = U[i] * V[i], min(U[j] * V[j], -1e-12)
            if wa < wb:
                lnr = math.log(V[j] / V[i])
                for k in range(N_HYP + 1):
                    wm = wa + (wb - wa) * k / N_HYP
                    val = qi(wm) * math.sqrt(-wm) * lnr
                    if val > line:
                        line = val
            if d <= min(line * (1.0 - REL_MARGIN), math.pi) - TOL:
                rel[i, j] = 1
                continue
            # Cauchy-Schwarz with U_b fixed, integrated in y = ln V
            ya, yb = math.log(V[i]), math.log(V[j])
            cs = 0.0
            for k in range(GN.size):
                vv = math.exp(ya + (yb - ya) * GN[k])
                qq = qi(U[j] * vv)
                cs += GW[k] * qq * qq * vv
            ub = math.sqrt(du * cs * (yb - ya))
            if d > min(ub * (1.0 + REL_MARGIN), math.pi) + TOL:
                continue
            # calibration over the c grid valid on the causal rectangle
            w1, w2, w3, w4 = U[i] * V[i], U[i] * V[j], U[j] * V[i], U[j] * V[j]
            wlo = min(min(w1, w2), min(w3, w4)); whi = max(max(w1, w2), max(w3, w4))
            for c in range(cwlo.size):
                if wlo >= cwlo[c] and whi <= cwhi[c]:
                    val = A[c, j] - A[c, i]
                    if val < ub:
                        ub = val
            if d > min(ub * (1.0 + REL_MARGIN), math.pi) + TOL:
                continue
            rel[i, j] = -1
    return rel


@njit(cache=True)
def _shoot(ua, va, vb, p0, steps):
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
        if u2 * v2 >= 0.999 or u3 * v2 >= 0.999 or u4 * v4 >= 0.999:
            return math.inf, 0.0
        l1 = qi(U * v) * math.sqrt(max(p, 0.0))
        l2 = qi(u2 * v2) * math.sqrt(max(p2, 0.0))
        l3 = qi(u3 * v2) * math.sqrt(max(p3, 0.0))
        l4 = qi(u4 * v4) * math.sqrt(max(p4, 0.0))
        L += h * (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0
        U += h * (k1u + 2.0 * k2u + 2.0 * k3u + k4u) / 6.0
        p += h * (k1p + 2.0 * k2p + 2.0 * k3p + k4p) / 6.0
        v = v4
        if p <= 0.0 or not math.isfinite(U) or not math.isfinite(p):
            return math.inf, 0.0
    return U, L


@njit(cache=True)
def _shoot_y(ua, va, vb, P0, steps):
    """V-parametrised geodesic in y = ln V:  U' = P,  P' = P + (F'/F)(UV) V P (U - P),
    L = int q(UV) sqrt(P V) dy.  Returns (U at vb, L)."""
    ya, yb = math.log(va), math.log(vb)
    h = (yb - ya) / steps
    U, P, y, L = ua, P0, ya, 0.0
    for _ in range(steps):
        v1 = math.exp(y); v2 = math.exp(y + 0.5 * h); v4 = math.exp(y + h)
        k1u = P;                 k1p = P + dlnf(U * v1) * v1 * P * (U - P)
        u2 = U + 0.5 * h * k1u;  p2 = P + 0.5 * h * k1p
        k2u = p2;                k2p = p2 + dlnf(u2 * v2) * v2 * p2 * (u2 - p2)
        u3 = U + 0.5 * h * k2u;  p3 = P + 0.5 * h * k2p
        k3u = p3;                k3p = p3 + dlnf(u3 * v2) * v2 * p3 * (u3 - p3)
        u4 = U + h * k3u;        p4 = P + h * k3p
        k4u = p4;                k4p = p4 + dlnf(u4 * v4) * v4 * p4 * (u4 - p4)
        if u2 * v2 >= 0.999 or u3 * v2 >= 0.999 or u4 * v4 >= 0.999:
            return math.inf, 0.0
        l1 = qi(U * v1) * math.sqrt(max(P * v1, 0.0))
        l2 = qi(u2 * v2) * math.sqrt(max(p2 * v2, 0.0))
        l3 = qi(u3 * v2) * math.sqrt(max(p3 * v2, 0.0))
        l4 = qi(u4 * v4) * math.sqrt(max(p4 * v4, 0.0))
        L += h * (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0
        U += h * (k1u + 2.0 * k2u + 2.0 * k3u + k4u) / 6.0
        P += h * (k1p + 2.0 * k2p + 2.0 * k3p + k4p) / 6.0
        y += h
        if P <= 0.0 or not math.isfinite(U) or not math.isfinite(P):
            return math.inf, 0.0
    return U, L


@njit(parallel=True, cache=True)
def shoot_pairs_fast(ua, va, ub, vb, steps_y, steps_u):
    """As shoot_pairs, but V-parametrised pairs integrate in ln V (steps_y), U-parametrised
    ones linearly (steps_u); bisection stops once the endpoint is hit to 1e-12."""
    n = ua.size
    L = np.zeros(n); miss = np.zeros(n)
    for k in prange(n):
        useU = (ub[k] - ua[k]) > (vb[k] - va[k])
        if useU:
            x0, y0, y1, target = va[k], ua[k], ub[k], vb[k]
            slope = (target - x0) / (y1 - y0)
        else:
            x0, y0, y1, target = ua[k], va[k], vb[k], ub[k]
            slope = (target - x0) / (math.log(y1) - math.log(y0))      # dU/dy guess
        lo, hi = math.log(slope) - 30.0, math.log(slope) + 30.0
        Xe = math.inf; Lk = 0.0
        for _ in range(90):
            mid = 0.5 * (lo + hi)
            if useU:
                Xe, Lk = _shoot(x0, y0, y1, math.exp(mid), steps_u)
            else:
                Xe, Lk = _shoot_y(x0, y0, y1, math.exp(mid), steps_y)
            if math.isfinite(Xe) and abs(Xe - target) < 1e-12:
                break
            if Xe > target:
                hi = mid
            else:
                lo = mid
        L[k] = Lk
        miss[k] = abs(Xe - target) if math.isfinite(Xe) else math.inf
    return L, miss


@njit(parallel=True, cache=True)
def shoot_pairs(ua, va, ub, vb, steps):
    n = ua.size
    L = np.zeros(n); miss = np.zeros(n)
    for k in prange(n):
        if (ub[k] - ua[k]) > (vb[k] - va[k]):
            x0, y0, y1, target = va[k], ua[k], ub[k], vb[k]
        else:
            x0, y0, y1, target = ua[k], va[k], vb[k], ub[k]
        slope = (target - x0) / (y1 - y0)
        lo, hi = math.log(slope) - 30.0, math.log(slope) + 30.0
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


def bh_order(t, r, phi, rng=None, audit=20000):
    U, V = to_kruskal(t, r)
    t0 = time.time()
    A = point_tables(U, V)
    rel = stage1(U, V, phi, A, C_WLO, C_WHI)
    t1 = time.time() - t0
    amb = rel == -1
    ii, jj = np.nonzero(amb)
    near, n_fine = 0, 0
    coarse_mask = np.zeros(ii.size, bool)
    if ii.size:
        d = np.abs(phi[jj] - phi[ii]); d = np.minimum(d, 2 * math.pi - d)
        Lc, mc = shoot_pairs_fast(U[ii], V[ii], U[jj], V[jj], *COARSE)
        dmax = np.minimum(Lc, math.pi)
        # a coarse miss is never trusted: those pairs go to the fine shot (which must hit)
        far = (np.abs(d - dmax) > COARSE_MARGIN) & (mc < 1e-9)
        coarse_mask = far
        rel[ii[far], jj[far]] = (d[far] <= dmax[far]).astype(np.int8)
        k = np.nonzero(~far)[0]
        n_fine = int(k.size)
        if k.size:
            Lf, mf = shoot_pairs_fast(U[ii[k]], V[ii[k]], U[jj[k]], V[jj[k]], *FINE)
            assert np.all(mf < 1e-9), "fine shooting missed on %d pairs" % int((mf >= 1e-9).sum())
            dm = np.minimum(Lf, math.pi)
            near = int((np.abs(d[k] - dm) < TOL).sum())
            rel[ii[k], jj[k]] = (d[k] <= dm).astype(np.int8)
    order = rel.astype(bool)
    stats = {"n": int(t.size), "relations": int(order.sum()), "stage3_pairs": int(ii.size),
             "stage3_fine_pairs": n_fine, "near_boundary_pairs_tol": near,
             "seconds_stage12": round(t1, 1), "seconds_total": round(time.time() - t0, 1)}
    if rng is not None and audit:
        # (a) pairs decided by stages 1-2; (b) pairs decided by the coarse shot: both vs FINE
        si, sj = np.nonzero((U[None, :] > U[:, None]) & (V[None, :] > V[:, None]) & ~amb)
        ci, cj = ii[coarse_mask], jj[coarse_mask]
        out = {}
        for name, (xi, xj) in (("stage12", (si, sj)), ("coarse_shot", (ci, cj))):
            if xi.size == 0:
                continue
            pick = rng.choice(xi.size, size=min(audit, xi.size), replace=False)
            a, b = xi[pick], xj[pick]
            La, ma = shoot_pairs_fast(U[a], V[a], U[b], V[b], *FINE)
            da = np.abs(phi[b] - phi[a]); da = np.minimum(da, 2 * math.pi - da)
            hit = ma < 1e-9
            ex = da <= np.minimum(La, math.pi)
            out[name] = {"sample": int(pick.size), "endpoint_failures": int((~hit).sum()),
                         "disagreements_among_hit": int((ex[hit] != order[a, b][hit]).sum())}
        stats["audit_vs_fine"] = out
    return order, stats


def mink_order(t, r, phi):
    x, y = r * np.cos(phi), r * np.sin(phi)
    dt = t[None, :] - t[:, None]
    dist = np.hypot(x[None, :] - x[:, None], y[None, :] - y[:, None])
    return (dt > 0.0) & (dt >= dist)


def radial_check(t, r):
    """Same-angle pairs: the 2+1 order must equal the sealed 1+1D EF closed form."""
    sys.path.insert(0, str(ROOT))
    from nachocausal.generator import past_matrix_fast
    C = past_matrix_fast(np.c_[t, r], "BH", r_S=TWO_M)          # C[i,j]: j precedes i
    U, V = to_kruskal(t, r)
    K = (U[None, :] > U[:, None]) & (V[None, :] > V[:, None])     # K[i,j]: i precedes j
    return int((K != C.T).sum()), int(K.sum())


def transitivity_violations(order):
    A = order.astype(np.float32)
    return int((((A @ A) > 0.5) & ~order).sum())


def main():
    n_mean = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else EXPLORE_BAND[0]
    assert EXPLORE_BAND[0] <= seed <= EXPLORE_BAND[1], "phase B uses the 2+1 exploration band only"
    rng = np.random.default_rng(seed)
    t, r, phi = sprinkle(n_mean, rng)
    order, st = bh_order(t, r, phi, rng)
    st["transitivity_violations"] = transitivity_violations(order)
    mism, tot = radial_check(t, r)
    st["radial_check_vs_1p1_closed_form"] = {"mismatches": mism, "kruskal_ordered_pairs": tot}
    mk = mink_order(t, r, phi)
    st["mink_relations"] = int(mk.sum())
    st["mink_transitivity_violations"] = transitivity_violations(mk)
    print(json.dumps(st, indent=1))


if __name__ == "__main__":
    main()
