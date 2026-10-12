"""B4-R phase 0: feasibility of a rank-3 certificate for the n=3 law (dev; NO terminal).

Spec: research_program/puente_3p1/2026-10-12/B4R_n3_reopening_spec.md section 5 (signed).
Floats with the SAME cell-level bounds a certificate would use (straight line below,
min(calibration, CS) above, via dev/explore_b2_path2_prototype.py), round-to-nearest.

For each chart direction e_j (B3 chart) it encloses the 12 entries of Dm, m = (rho, E[f^2],
E[p^2], E[pf]), by interval arithmetic over cell/segment bounds of F (future) and P (past):
    F_lo(P) = sum_Q W_Q p_lo(P_top -> Q_bot)      F_hi(P) = sum_Q W_Q p_hi(P_bot -> Q_top)
    P_lo(P) = sum_Q W_Q p_lo(Q_top -> P_bot)      P_hi(P) = sum_Q W_Q p_hi(Q_bot -> P_top)
derivatives by B4.3 section 3 and H3 for rho.  Z and weights are floats (Gauss): only the
h-bounds give width, so the predicted width is a LOWER estimate of a certificate's.
Gate (frozen in the spec):  sigma_pred(128) = sigma_min(R Dm_centre) - ||E_128||_F > 0.
Usage: .venv/bin/python dev/explore_b4r_phase0.py [M ...]     (default 32 64 128)
"""
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "dev"))
sys.path.insert(0, str(ROOT / "research_program" / "puente_3p1" / "2026-09-12"))
import explore_b2_path2_prototype as pp  # noqa: E402
from verify_b3_transverse_n2 import jacobian_chart  # noqa: E402

V0, V1, UOUT, UIN = pp.V0, pp.V1, pp.UOUT, pp.UIN
R = np.diag([1.0, 1e4, 1e4, 1e4])
REF_SIGMA = (147.87681303807526, 2.604993840152783, 0.03825194123838259)


# ---- interval helpers on (lo, hi) numpy pairs --------------------------------------------
def imul(a, b):
    c = np.stack([a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]])
    return c.min(0), c.max(0)


def iadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def iscale(s, a):
    return (s * a[0], s * a[1]) if s >= 0 else (s * a[1], s * a[0])


def isum(a, w):           # sum_k w_k a_k with w >= 0
    return float(w @ a[0]), float(w @ a[1])


def rowdot(T, rows, vec, chunk=1024):
    out = np.empty(rows.size)
    for i in range(0, rows.size, chunk):
        out[i:i + chunk] = T[rows[i:i + chunk]] @ vec
    return out


def tables(M):
    Ug = np.linspace(-UOUT, UIN, M + 1)
    Vg = np.linspace(V0, V1, M + 1)
    iu, iv = np.meshgrid(np.arange(M + 1), np.arange(M + 1), indexing="ij")
    PU, PV = Ug[iu].ravel(), Vg[iv].ravel()
    A = np.stack([c * np.log(PV) + np.interp(PU * PV, pp.cb.WT, pp.PHI_TAB[k])
                  for k, c in enumerate(pp.C_LIST)])
    lb, ub = pp.corner_bounds(PU, PV, A, pp.C_LIST, pp.C_WLO, pp.C_WHI, pp.cb.WT, pp.QT, pp.TN, pp.TW)
    return Ug, Vg, pp.p_inplace(lb), pp.p_inplace(ub)


def run(M):
    Ug, Vg, plb, pub = tables(M)
    n1, npt = M + 1, (M + 1) ** 2
    pid = lambda i, j: i * n1 + j  # noqa: E731
    W = pp.cell_weights(Ug, Vg).ravel()
    Z = float(W.sum())
    ci, cj = np.meshgrid(np.arange(M), np.arange(M), indexing="ij")
    bot, top = pid(ci, cj).ravel(), pid(ci + 1, cj + 1).ravel()
    Wbot = np.zeros(npt); Wbot[bot] = W
    Wtop = np.zeros(npt); Wtop[top] = W
    colP_lo = Wtop @ plb          # [x] = sum_Q W_Q p_lo(Q_top -> x)
    colP_hi = Wbot @ pub          # [x] = sum_Q W_Q p_hi(Q_bot -> x)
    Fc = (rowdot(plb, top, Wbot), rowdot(pub, bot, Wtop))
    Pc = (colP_lo[bot], colP_hi[top])
    fc, pc = (Fc[0] / Z, Fc[1] / Z), (Pc[0] / Z, Pc[1] / Z)
    wn = W / Z

    faces = {"U=-u_out": (np.zeros(M, int), np.arange(M), True, -UOUT),
             "U=u_in": (np.full(M, M), np.arange(M), True, UIN),
             "V=v0": (np.arange(M), np.zeros(M, int), False, V0),
             "V=v1": (np.arange(M), np.full(M, M), False, V1)}
    seg = {}
    for name, (fi, fj, along_V, fixed) in faces.items():
        if along_V:
            s0, s1 = pid(fi, fj), pid(fi, fj + 1)
            fw = pp.segment_weights(fixed, Vg, True)
        else:
            s0, s1 = pid(fi, fj), pid(fi + 1, fj)
            fw = pp.segment_weights(fixed, Ug, False)
        Fs = (rowdot(plb, s1, Wbot), rowdot(pub, s0, Wtop))
        Ps = (colP_lo[s0], colP_hi[s1])
        v0s = np.zeros(npt); v0s[s0] = fw
        v1s = np.zeros(npt); v1s[s1] = fw
        # cell -> face integrals of h, both orientations
        DFc = (rowdot(plb, top, v0s), rowdot(pub, bot, v1s))      # x in P before y on face
        DPc = ((v1s @ plb)[bot], (v0s @ pub)[top])                # y on face before x in P
        seg[name] = {"fw": fw, "f": (Fs[0] / Z, Fs[1] / Z), "p": (Ps[0] / Z, Ps[1] / Z),
                     "H": (Fs[0] + Ps[0], Fs[1] + Ps[1]), "DF": DFc, "DP": DPc, "J": float(fw.sum())}
    del plb, pub

    B = (float(W @ (Fc[0] + Pc[0])), float(W @ (Fc[1] + Pc[1])))
    rho = (B[0] / Z ** 2, B[1] / Z ** 2)
    Mff = isum((fc[0] ** 2, fc[1] ** 2), wn)
    Mpp = isum((pc[0] ** 2, pc[1] ** 2), wn)
    Mfp = isum((fc[0] * pc[0], fc[1] * pc[1]), wn)

    J = jacobian_chart()
    rows_lo, rows_hi = np.zeros((4, 3)), np.zeros((4, 3))
    for j in range(3):
        dv0, dv1, duo, dui = J[:4, j]
        an = {"U=-u_out": duo, "U=u_in": dui, "V=v0": -dv0, "V=v1": dv1}
        DZ = sum(an[k] * seg[k]["J"] for k in seg)
        Bp, bff, bpp, bfp = (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)
        DF, DP = (np.zeros(M * M), np.zeros(M * M)), (np.zeros(M * M), np.zeros(M * M))
        for k, s in seg.items():
            a = an[k]
            if a == 0.0:
                continue
            Bp = iadd(Bp, iscale(2 * a, isum(s["H"], s["fw"])))
            bff = iadd(bff, iscale(a / Z, isum((s["f"][0] ** 2, s["f"][1] ** 2), s["fw"])))
            bpp = iadd(bpp, iscale(a / Z, isum((s["p"][0] ** 2, s["p"][1] ** 2), s["fw"])))
            bfp = iadd(bfp, iscale(a / Z, isum((s["f"][0] * s["p"][0], s["f"][1] * s["p"][1]), s["fw"])))
            DF = iadd(DF, iscale(a, s["DF"]))
            DP = iadd(DP, iscale(a, s["DP"]))
        # Df = (DF Z - F DZ)/Z^2
        Df = iadd(iscale(1 / Z, DF), iscale(-DZ / Z ** 2, Fc))
        Dp = iadd(iscale(1 / Z, DP), iscale(-DZ / Z ** 2, Pc))
        Drho = iadd(iscale(1 / Z ** 2, Bp), iscale(-2 * DZ / Z ** 3, B))
        t_ff = isum(imul(fc, Df), wn)
        t_pp = isum(imul(pc, Dp), wn)
        t_fp = isum(iadd(imul(Df, pc), imul(fc, Dp)), wn)
        DMff = iadd(iadd(bff, iscale(2.0, t_ff)), iscale(-DZ / Z, Mff))
        DMpp = iadd(iadd(bpp, iscale(2.0, t_pp)), iscale(-DZ / Z, Mpp))
        DMfp = iadd(iadd(bfp, t_fp), iscale(-DZ / Z, Mfp))
        for r, iv in enumerate((Drho, DMff, DMpp, DMfp)):
            rows_lo[r, j], rows_hi[r, j] = iv
    centre, half = (rows_lo + rows_hi) / 2, (rows_hi - rows_lo) / 2
    Rc, RE = R @ centre, R @ half
    sv = np.linalg.svd(Rc, compute_uv=False)
    sigma_pred = float(sv[-1] - np.linalg.norm(RE))
    return {"M": M, "Z": Z, "moments_lo_hi": [list(rho), list(Mff), list(Mpp), list(Mfp)],
            "Dm_centre": centre.tolist(), "Dm_halfwidth": half.tolist(),
            "R_Dm_singular_values_centre": sv.tolist(),
            "R_E_frobenius": float(np.linalg.norm(RE)), "sigma_pred": sigma_pred,
            "relative_halfwidth_rows": (np.abs(half).max(1) / np.abs(centre).max(1)).tolist(),
            "gate_passes_at_this_M": sigma_pred > 0}


def main():
    Ms = [int(a) for a in sys.argv[1:]] or [32, 64, 128]
    print(json.dumps({"reference_sigma_regenerated_2026_10_11": REF_SIGMA}))
    for M in Ms:
        print(json.dumps(run(M), indent=1), flush=True)


if __name__ == "__main__":
    main()
