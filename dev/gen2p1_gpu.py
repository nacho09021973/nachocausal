"""2+1 equatorial bench: GPU (CuPy) port of the generator's heavy stages (dev only; NOT a verdict).

Run in .venv-gpu (CuPy 14, numpy 2).  Same algorithm, same tables, same margins as
dev/gen2p1_efbox.py, in DOUBLE precision CUDA kernels:
  * stage1_kernel : per ordered pair, line + orbit lower bound, Cauchy-Schwarz (ln V) and the
                    calibration grid upper bound  ->  rel in {1, 0, -1 (ambiguous)};
  * shoot_kernel  : the (U,V) geodesic shot by bisection on the log initial slope, V-pairs in
                    ln V, U-pairs linear; coarse and fine step counts as on CPU.
Acta rule gpu_dev_only: exploration only; the blind run stays CPU.  Validation against the CPU
generator: dev/validate_gen2p1_gpu.py.
"""
import math
import os
import sys
from pathlib import Path

import cupy as cp
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "dev"))
import gen2p1_efbox as gen  # noqa: E402  (tables, constants; T from NC2P1_T_EDGE)

SRC = r'''
#define INFINITY __longlong_as_double(0x7ff0000000000000ULL)
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif
extern "C" {
__device__ double tab(const double* T, double w, double zmin, double dz, int nz) {
    double z = log(1.0 - w);
    double x = (z - zmin) / dz;
    int k = (int)x;
    if (k < 0) k = 0;
    if (k >= nz - 1) k = nz - 2;
    double a = x - k;
    return T[k] * (1.0 - a) + T[k + 1] * a;
}

__global__ void stage1(const double* U, const double* V, const double* phi, int n,
                       const double* QT, double zmin, double dz, int nz,
                       const double* GN, const double* GW, int ng, int nhyp,
                       const double* A, const double* cwlo, const double* cwhi, int nc,
                       double tol, double relm, signed char* rel) {
    long long idx = (long long)blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= (long long)n * n) return;
    int i = (int)(idx / n), j = (int)(idx % n);
    signed char out = 0;
    double du = U[j] - U[i], dv = V[j] - V[i];
    if (!(du > 0.0 && dv > 0.0)) { rel[idx] = 0; return; }
    double d = fabs(phi[j] - phi[i]);
    if (d > M_PI) d = 2.0 * M_PI - d;
    double line = 0.0;
    for (int k = 0; k < ng; k++)
        line += GW[k] * tab(QT, (U[i] + du * GN[k]) * (V[i] + dv * GN[k]), zmin, dz, nz);
    line *= sqrt(du * dv);
    double wa = U[i] * V[i], wb = fmin(U[j] * V[j], -1e-12);
    if (wa < wb) {
        double lnr = log(V[j] / V[i]);
        for (int k = 0; k <= nhyp; k++) {
            double wm = wa + (wb - wa) * k / nhyp;
            double val = tab(QT, wm, zmin, dz, nz) * sqrt(-wm) * lnr;
            if (val > line) line = val;
        }
    }
    if (d <= fmin(line * (1.0 - relm), M_PI) - tol) { rel[idx] = 1; return; }
    double ya = log(V[i]), yb = log(V[j]), cs = 0.0;
    for (int k = 0; k < ng; k++) {
        double vv = exp(ya + (yb - ya) * GN[k]);
        double qq = tab(QT, U[j] * vv, zmin, dz, nz);
        cs += GW[k] * qq * qq * vv;
    }
    double ub = sqrt(du * cs * (yb - ya));
    if (d > fmin(ub * (1.0 + relm), M_PI) + tol) { rel[idx] = 0; return; }
    double w1 = U[i] * V[i], w2 = U[i] * V[j], w3 = U[j] * V[i], w4 = U[j] * V[j];
    double wlo = fmin(fmin(w1, w2), fmin(w3, w4)), whi = fmax(fmax(w1, w2), fmax(w3, w4));
    for (int c = 0; c < nc; c++) {
        if (wlo >= cwlo[c] && whi <= cwhi[c]) {
            double val = A[(long long)c * n + j] - A[(long long)c * n + i];
            if (val < ub) ub = val;
        }
    }
    if (d > fmin(ub * (1.0 + relm), M_PI) + tol) { rel[idx] = 0; return; }
    rel[idx] = -1;
}

__device__ void shoot_u(double ua, double va, double vb, double p0, int steps,
                        const double* QT, const double* DL, double zmin, double dz, int nz,
                        double* Xe, double* Lo) {
    double h = (vb - va) / steps, U = ua, p = p0, v = va, L = 0.0;
    for (int s = 0; s < steps; s++) {
        double k1u = p, k1p = tab(DL, U * v, zmin, dz, nz) * p * (U - v * p);
        double u2 = U + 0.5 * h * k1u, p2 = p + 0.5 * h * k1p, v2 = v + 0.5 * h;
        double k2u = p2, k2p = tab(DL, u2 * v2, zmin, dz, nz) * p2 * (u2 - v2 * p2);
        double u3 = U + 0.5 * h * k2u, p3 = p + 0.5 * h * k2p;
        double k3u = p3, k3p = tab(DL, u3 * v2, zmin, dz, nz) * p3 * (u3 - v2 * p3);
        double u4 = U + h * k3u, p4 = p + h * k3p, v4 = v + h;
        double k4u = p4, k4p = tab(DL, u4 * v4, zmin, dz, nz) * p4 * (u4 - v4 * p4);
        if (u2 * v2 >= 0.999 || u3 * v2 >= 0.999 || u4 * v4 >= 0.999) { *Xe = INFINITY; *Lo = 0; return; }
        double l1 = tab(QT, U * v, zmin, dz, nz) * sqrt(fmax(p, 0.0));
        double l2 = tab(QT, u2 * v2, zmin, dz, nz) * sqrt(fmax(p2, 0.0));
        double l3 = tab(QT, u3 * v2, zmin, dz, nz) * sqrt(fmax(p3, 0.0));
        double l4 = tab(QT, u4 * v4, zmin, dz, nz) * sqrt(fmax(p4, 0.0));
        L += h * (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        U += h * (k1u + 2.0 * k2u + 2.0 * k3u + k4u) / 6.0;
        p += h * (k1p + 2.0 * k2p + 2.0 * k3p + k4p) / 6.0;
        v = v4;
        if (p <= 0.0 || !isfinite(U) || !isfinite(p)) { *Xe = INFINITY; *Lo = 0; return; }
    }
    *Xe = U; *Lo = L;
}

__device__ void shoot_y(double ua, double va, double vb, double P0, int steps,
                        const double* QT, const double* DL, double zmin, double dz, int nz,
                        double* Xe, double* Lo) {
    double ya = log(va), yb = log(vb), h = (yb - ya) / steps;
    double U = ua, P = P0, y = ya, L = 0.0;
    for (int s = 0; s < steps; s++) {
        double v1 = exp(y), v2 = exp(y + 0.5 * h), v4 = exp(y + h);
        double k1u = P, k1p = P + tab(DL, U * v1, zmin, dz, nz) * v1 * P * (U - P);
        double u2 = U + 0.5 * h * k1u, p2 = P + 0.5 * h * k1p;
        double k2u = p2, k2p = p2 + tab(DL, u2 * v2, zmin, dz, nz) * v2 * p2 * (u2 - p2);
        double u3 = U + 0.5 * h * k2u, p3 = P + 0.5 * h * k2p;
        double k3u = p3, k3p = p3 + tab(DL, u3 * v2, zmin, dz, nz) * v2 * p3 * (u3 - p3);
        double u4 = U + h * k3u, p4 = P + h * k3p;
        double k4u = p4, k4p = p4 + tab(DL, u4 * v4, zmin, dz, nz) * v4 * p4 * (u4 - p4);
        if (u2 * v2 >= 0.999 || u3 * v2 >= 0.999 || u4 * v4 >= 0.999) { *Xe = INFINITY; *Lo = 0; return; }
        double l1 = tab(QT, U * v1, zmin, dz, nz) * sqrt(fmax(P * v1, 0.0));
        double l2 = tab(QT, u2 * v2, zmin, dz, nz) * sqrt(fmax(p2 * v2, 0.0));
        double l3 = tab(QT, u3 * v2, zmin, dz, nz) * sqrt(fmax(p3 * v2, 0.0));
        double l4 = tab(QT, u4 * v4, zmin, dz, nz) * sqrt(fmax(p4 * v4, 0.0));
        L += h * (l1 + 2.0 * l2 + 2.0 * l3 + l4) / 6.0;
        U += h * (k1u + 2.0 * k2u + 2.0 * k3u + k4u) / 6.0;
        P += h * (k1p + 2.0 * k2p + 2.0 * k3p + k4p) / 6.0;
        y += h;
        if (P <= 0.0 || !isfinite(U) || !isfinite(P)) { *Xe = INFINITY; *Lo = 0; return; }
    }
    *Xe = U; *Lo = L;
}

__global__ void shoot(const double* ua, const double* va, const double* ub, const double* vb,
                      int n, int steps_y, int steps_u,
                      const double* QT, const double* DL, double zmin, double dz, int nz,
                      double* Lout, double* miss) {
    int k = blockIdx.x * blockDim.x + threadIdx.x;
    if (k >= n) return;
    bool useU = (ub[k] - ua[k]) > (vb[k] - va[k]);
    double x0, y0, y1, target, slope;
    if (useU) { x0 = va[k]; y0 = ua[k]; y1 = ub[k]; target = vb[k]; slope = (target - x0) / (y1 - y0); }
    else { x0 = ua[k]; y0 = va[k]; y1 = vb[k]; target = ub[k]; slope = (target - x0) / (log(y1) - log(y0)); }
    double lo = log(slope) - 30.0, hi = log(slope) + 30.0, Xe = INFINITY, Lk = 0.0;
    for (int it = 0; it < 90; it++) {
        double mid = 0.5 * (lo + hi);
        if (useU) shoot_u(x0, y0, y1, exp(mid), steps_u, QT, DL, zmin, dz, nz, &Xe, &Lk);
        else shoot_y(x0, y0, y1, exp(mid), steps_y, QT, DL, zmin, dz, nz, &Xe, &Lk);
        if (isfinite(Xe) && fabs(Xe - target) < 1e-12) break;
        if (Xe > target) hi = mid; else lo = mid;
    }
    Lout[k] = Lk;
    miss[k] = isfinite(Xe) ? fabs(Xe - target) : INFINITY;
}
}
'''
_MOD = cp.RawModule(code=SRC, options=("-std=c++17",))
_STAGE1 = _MOD.get_function("stage1")
_SHOOT = _MOD.get_function("shoot")
_QT = cp.asarray(gen.QT); _DL = cp.asarray(gen.DLNF)
_GN = cp.asarray(gen.GN); _GW = cp.asarray(gen.GW)
_CWLO = cp.asarray(gen.C_WLO); _CWHI = cp.asarray(gen.C_WHI)


def stage1(U, V, phi):
    n = U.size
    A = cp.asarray(gen.point_tables(U, V))
    rel = cp.zeros(n * n, cp.int8)
    Ug, Vg, Pg = cp.asarray(U), cp.asarray(V), cp.asarray(phi)
    tpb = 256
    blocks = (n * n + tpb - 1) // tpb
    _STAGE1((blocks,), (tpb,), (Ug, Vg, Pg, np.int32(n), _QT, np.float64(gen.ZMIN),
                                np.float64(gen.DZ), np.int32(gen.NZ), _GN, _GW,
                                np.int32(gen.GN.size), np.int32(gen.N_HYP), A, _CWLO, _CWHI,
                                np.int32(_CWLO.size), np.float64(gen.TOL),
                                np.float64(gen.REL_MARGIN), rel))
    return cp.asnumpy(rel).reshape(n, n)


def shoot_pairs(ua, va, ub, vb, steps_y, steps_u):
    n = ua.size
    if n == 0:
        return np.zeros(0), np.zeros(0)
    L = cp.zeros(n); miss = cp.zeros(n)
    tpb = 128
    _SHOOT(((n + tpb - 1) // tpb,), (tpb,), (cp.asarray(ua), cp.asarray(va), cp.asarray(ub),
                                             cp.asarray(vb), np.int32(n), np.int32(steps_y),
                                             np.int32(steps_u), _QT, _DL, np.float64(gen.ZMIN),
                                             np.float64(gen.DZ), np.int32(gen.NZ), L, miss))
    return cp.asnumpy(L), cp.asnumpy(miss)


def bh_order(t, r, phi):
    """Same decisions as gen.bh_order (stage 1, coarse shot, fine shot within the margin)."""
    import time
    U, V = gen.to_kruskal(t, r)
    t0 = time.time()
    rel = stage1(U, V, phi)
    t1 = time.time() - t0
    ii, jj = np.nonzero(rel == -1)
    near, n_fine = 0, 0
    if ii.size:
        d = np.abs(phi[jj] - phi[ii]); d = np.minimum(d, 2 * math.pi - d)
        # per-pair Richardson tier: shots with 64 and 128 steps; their (capped) difference e
        # bounds the 128-step error (measured: true error <= 0.2 e on 300k pairs, T = 6, 8,
        # 16; never above 20 e + 1e-3).  Decide there only if the gap to the boundary
        # exceeds 20 e + 1e-3; the rest (~0.2-0.4%) go to the fine shot.
        L64, m64 = shoot_pairs(U[ii], V[ii], U[jj], V[jj], 64, 256)
        Lc, mc = shoot_pairs(U[ii], V[ii], U[jj], V[jj], *gen.COARSE)
        dmax = np.minimum(Lc, math.pi)
        e = np.abs(np.minimum(L64, math.pi) - dmax)
        far = (np.abs(d - dmax) > 20.0 * e + 1e-3) & (mc < 1e-9) & (m64 < 1e-9)
        rel[ii[far], jj[far]] = (d[far] <= dmax[far]).astype(np.int8)
        k = np.nonzero(~far)[0]
        n_fine = int(k.size)
        if k.size:
            Lf, mf = shoot_pairs(U[ii[k]], V[ii[k]], U[jj[k]], V[jj[k]], *gen.FINE)
            assert np.all(mf < 1e-9), "fine shooting missed on %d pairs" % int((mf >= 1e-9).sum())
            dm = np.minimum(Lf, math.pi)
            near = int((np.abs(d[k] - dm) < gen.TOL).sum())
            rel[ii[k], jj[k]] = (d[k] <= dm).astype(np.int8)
    order = rel.astype(bool)
    return order, {"n": int(t.size), "relations": int(order.sum()), "stage3_pairs": int(ii.size),
                   "stage3_fine_pairs": n_fine, "near_boundary_pairs_tol": near,
                   "seconds_stage1": round(t1, 2), "seconds_total": round(time.time() - t0, 2),
                   "device": "gpu-double", "tiering": "richardson 64/128, 20e+1e-3"}
