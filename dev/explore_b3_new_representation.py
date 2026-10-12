"""B3 with the new representation: float exploration (NOT a certificate).

Question: at the frozen point, with the cell-level bounds the B2 gate certificate uses
(straight line below; min(calibration, Cauchy-Schwarz) above), how wide are the enclosures of
drho/dx_i along the three B3 chart directions, and does any component of dphi wedge drho
exclude zero?

S(e) = 2 sum_f v_f(e) I_f - 2 (B/Z) sum_f v_f(e) J_f,  I_f in [I_lo, I_hi], B in [B_lo, B_hi]:
lower AND upper H on every face (the gate needed only one per face), and B from both sides.
dphi as in research_program/puente_3p1/2026-09-12/verify_b3_transverse_n2.py.

Floats throughout, reusing dev/explore_b2_path2_prototype.py.
Usage: .venv/bin/python dev/explore_b3_new_representation.py [M ...]
"""
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "dev"))
sys.path.insert(0, str(ROOT / "research_program" / "puente_3p1" / "2026-09-12"))
import explore_b2_path2_prototype as pp  # noqa: E402
from verify_b3_transverse_n2 import jacobian_chart, phi_shape_derivative, LSTAR  # noqa: E402

V0, V1, UOUT, UIN = pp.V0, pp.V1, pp.UOUT, pp.UIN
assert np.allclose(LSTAR[:4], (V0, V1, UOUT, UIN))


def face_vn(e):
    dv0, dv1, duout, duin = e[:4]
    return {"U=-u_out": duout, "U=u_in": duin, "V=v0": -dv0, "V=v1": dv1}


def iv_mul(a, b):
    c = [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
    return [min(c), max(c)]


def pieces(M):
    Ug = np.linspace(-UOUT, UIN, M + 1)
    Vg = np.linspace(V0, V1, M + 1)
    iu, iv = np.meshgrid(np.arange(M + 1), np.arange(M + 1), indexing="ij")
    PU, PV = Ug[iu].ravel(), Vg[iv].ravel()
    pid = lambda i, j: i * (M + 1) + j  # noqa: E731
    A = np.stack([c * np.log(PV) + np.interp(PU * PV, pp.cb.WT, pp.PHI_TAB[k])
                  for k, c in enumerate(pp.C_LIST)])
    lb, ub = pp.corner_bounds(PU, PV, A, pp.C_LIST, pp.C_WLO, pp.C_WHI, pp.cb.WT, pp.QT, pp.TN, pp.TW)
    plb = pp.p_inplace(lb); del lb
    pub = pp.p_inplace(ub); del ub
    W = pp.cell_weights(Ug, Vg)
    Z = W.sum()
    ci, cj = np.meshgrid(np.arange(M), np.arange(M), indexing="ij")
    ci, cj = ci.ravel(), cj.ravel()
    Wc = W.ravel()
    bot, top = pid(ci, cj), pid(ci + 1, cj + 1)
    B_hi = 2.0 * float(Wc @ pub[np.ix_(bot, top)] @ Wc)
    B_lo = 2.0 * float(Wc @ plb[np.ix_(top, bot)] @ Wc)
    faces = {"U=-u_out": (np.zeros(M, int), np.arange(M), True, -UOUT),
             "U=u_in": (np.full(M, M), np.arange(M), True, UIN),
             "V=v0": (np.arange(M), np.zeros(M, int), False, V0),
             "V=v1": (np.arange(M), np.full(M, M), False, V1)}
    out = {}
    for name, (fi, fj, along_V, fixed) in faces.items():
        if along_V:
            s0, s1 = pid(fi, fj), pid(fi, fj + 1)
            fw = pp.segment_weights(fixed, Vg, True)
        else:
            s0, s1 = pid(fi, fj), pid(fi + 1, fj)
            fw = pp.segment_weights(fixed, Ug, False)
        H_lo = (plb[np.ix_(s1, bot)] + plb[np.ix_(top, s0)].T) @ Wc
        H_hi = (pub[np.ix_(s0, top)] + pub[np.ix_(bot, s1)].T) @ Wc
        out[name] = {"I": [float(fw @ H_lo), float(fw @ H_hi)], "J": float(fw.sum())}
    return {"M": M, "Z": Z, "B": [B_lo, B_hi], "faces": out}


def S_enclosure(pc, e):
    vn = face_vn(e)
    P = [0.0, 0.0]
    Q = 0.0
    for name, f in pc["faces"].items():
        t = iv_mul([vn[name], vn[name]], f["I"])
        P = [P[0] + t[0], P[1] + t[1]]
        Q += vn[name] * f["J"]
    R = [pc["B"][0] / pc["Z"], pc["B"][1] / pc["Z"]]
    RQ = iv_mul(R, [Q, Q])
    return [2 * P[0] - 2 * RQ[1], 2 * P[1] - 2 * RQ[0]]


def main():
    Ms = [int(a) for a in sys.argv[1:]] or [32, 64]
    J = jacobian_chart()
    dphi = np.array([phi_shape_derivative(LSTAR, J[:, j]) for j in range(3)])
    d = np.array(LSTAR) * 0
    d[:4] = np.array((0.2, 0.8, 2.0, 0.9)) - np.array((0.5, 1.0, 1.0, 0.5))
    for M in Ms:
        pc = pieces(M)
        Z2 = pc["Z"] ** 2
        drho = [[s / Z2 for s in S_enclosure(pc, J[:, j])] for j in range(3)]
        drho_d = [s / Z2 for s in S_enclosure(pc, d)]
        cross = []
        for i, j in ((0, 1), (0, 2), (1, 2)):
            a = iv_mul([dphi[i], dphi[i]], drho[j])
            b = iv_mul([-dphi[j], -dphi[j]], drho[i])
            cross.append([a[0] + b[0], a[1] + b[1]])
        print(json.dumps({"M": M, "Z": pc["Z"], "B": pc["B"], "dphi_dx": dphi.tolist(),
                          "drho_dx": drho, "drho_along_d_check": drho_d,
                          "cross_x1x2_x1x3_x2x3": cross,
                          "excludes_zero": [bool(c[0] > 0 or c[1] < 0) for c in cross]}, indent=1),
              flush=True)


if __name__ == "__main__":
    main()
