"""PUENTE-3P1 / B3 -- n=2 versus phi at the frozen point, with the gate's certified machinery.

B3 (research_program/puente_3p1/2026-09-12/B3_transverse_n2_audit.md) asks whether dphi is
parallel to drho in the gauge-quotiented chart x = (v1/v0, u_in/u_out, u_in v1), v0 fixed, at the
frozen point lambda* (the binary64 path(0.5), the gate's H5).  One wedge component excluding
zero gives B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY: there is a direction v with
drho(v) = 0 and dphi(v) != 0.  Since 2026-10-11 B3 is INCONCLUSIVE_BY_BOUNDS.

This file certifies the (x2, x3) component,
    W23 = dphi_2 drho_3 - dphi_3 drho_2  >  0,
from four enclosures:
  * drho_3 >= S_lo(e3)/Z_hi^2.  Along e3 = d lambda/d x3 only the two U faces move, both with
    v_n > 0 -- exactly the gate's case.  The gate's audited run() is called UNCHANGED, with its
    face-velocity table VN_FR set to e3's exact rationals (V faces: exactly 0).
  * dphi_2, dphi_3 from phi = Z_in/(Z_in + Z_out) (U > 0 and U < 0 parts of K):
        dphi = (Z_out dZ_in - Z_in dZ_out)/(Z_in + Z_out)^2,
    dZ by face integrals of G, all from the gate's cell_weights / segment_weights, combined in
    mpmath.iv.
  * |drho_2| crudely: along e2 only U = -u_out moves, and H <= Z, so
        |S(e2)| <= 2 |v| J (Z_hi + B_hi/Z_lo),  J = int_face G.
Chart rank 3 is an exact rational determinant.  The fast-math guard is B2.1's (executed IR,
private empty numba cache), over all 19 gate kernels.

Determinism: no seeds, no Monte Carlo, no search; frozen point and chart as in B3.
Usage: .venv/bin/python research_program/puente_3p1/2026-10-12/verify_b3_certificate.py [M]
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_b2_1_box_certificate as b21  # noqa: E402  (sets the private numba cache first)

import json  # noqa: E402
from fractions import Fraction as Fr  # noqa: E402

import numpy as np  # noqa: E402
from mpmath import iv  # noqa: E402

gate, b15 = b21.gate, b21.b15
iv.dps = 30

LAM = [Fr(float(x)) for x in gate.LAM[:4]]        # (v0, v1, u_out, u_in), binary64, exact
V0, V1, UO, UI = LAM
X = (V1 / V0, UI / UO, UI * V1)                     # chart coordinates at lambda*


def chart_jacobian():
    """Columns d lambda / d x_j, exact rationals; gauge v0 fixed (research B3 note)."""
    x1, x2, x3 = X
    return [  # rows v0, v1, u_out, u_in
        [Fr(0), Fr(0), Fr(0)],
        [V0, Fr(0), Fr(0)],
        [-UO / x1, -UO / x2, UO / x3],
        [-UI / x1, Fr(0), 1 / V1],
    ]


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def I(x):
    x = Fr(x)
    return iv.mpf(x.numerator) / iv.mpf(x.denominator)


def F(lo, hi):
    return iv.mpf([lo, hi])


def guard_all_gate_kernels():
    """B2.1's guard (executed IR, symbol closure, prange bodies) over all 19 gate kernels."""
    gate._compile_helpers()
    return b21.guard_kernels(gate.KERNELS)


def phi_pieces(M):
    """Enclosures of Z_in, Z_out and the face integrals of G that dphi needs."""
    wt = gate.w_table()
    _, _, glo, ghi, _, _ = gate.certified_tables(wt)
    e = b15.E_INV_HI
    v0, v1, uo, ui = (float(x) for x in LAM)
    Vg = np.linspace(v0, v1, M + 1)
    Ui = np.linspace(0.0, ui, M + 1)
    Uo = np.linspace(-uo, 0.0, M + 1)
    assert Vg[0] == v0 and Vg[-1] == v1 and Ui[-1] == ui and Uo[0] == -uo
    assert Ui[0] == 0.0 and Uo[-1] == 0.0
    out = {}
    lo, hi = gate.cell_weights(Ui, Vg, gate.R_SUB, wt, glo, ghi, e)
    out["Z_in"] = F(b15.sum_dn(lo), b15.sum_up(hi))
    lo, hi = gate.cell_weights(Uo, Vg, gate.R_SUB, wt, glo, ghi, e)
    out["Z_out"] = F(b15.sum_dn(lo), b15.sum_up(hi))
    for key, fixed, grid in (("J_uin", ui, Vg), ("J_uout", -uo, Vg),      # U faces, along V
                             ("J_v1_in", v1, Ui), ("J_v1_out", v1, Uo),    # V = v1, split at U = 0
                             ("J_v0_in", v0, Ui), ("J_v0_out", v0, Uo)):   # V = v0
        lo, hi = gate.segment_weights(fixed, grid, gate.R_SUB, wt, glo, ghi, e)
        out[key] = F(b15.sum_dn(lo), b15.sum_up(hi))
    return out


def dphi(pc, col):
    dv0, dv1, duo, dui = (I(c) for c in col)
    dZin = dui * pc["J_uin"] + dv1 * pc["J_v1_in"] - dv0 * pc["J_v0_in"]
    dZout = duo * pc["J_uout"] + dv1 * pc["J_v1_out"] - dv0 * pc["J_v0_out"]
    Zs = pc["Z_in"] + pc["Z_out"]
    return (pc["Z_out"] * dZin - pc["Z_in"] * dZout) / Zs ** 2


def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else gate.M_DEFAULT
    J = chart_jacobian()
    cols = [[J[r][c] for r in range(4)] for c in range(3)]
    det = det3([J[1], J[2], J[3]])
    chart_rank3 = det != 0

    # drho_3 lower bound: the gate's run() with e3's face velocities
    e3 = cols[2]
    assert e3[0] == 0 and e3[1] == 0 and e3[2] > 0 and e3[3] > 0
    gate.VN_FR = {"U=-u_out": e3[2], "U=u_in": e3[3], "V=v0": -e3[0], "V=v1": e3[1]}
    r3 = gate.run(M)
    Z = F(*r3["Z"])
    # S_lo > 0 divides by Z_hi^2; otherwise by Z_lo^2 (still a valid lower bound)
    drho3_lo = I(r3["S_lo"]) / (iv.mpf(r3["Z"][1]) ** 2 if r3["S_lo"] > 0 else iv.mpf(r3["Z"][0]) ** 2)

    # |drho_2| crude upper bound; e2 moves only U = -u_out
    pc = phi_pieces(M)
    e2 = cols[1]
    assert e2[0] == 0 and e2[1] == 0 and e2[3] == 0
    S2_abs = 2 * abs(I(e2[2])) * pc["J_uout"].b * (Z.b + iv.mpf(r3["B_hi"]) / Z.a)
    drho2_abs = S2_abs / Z.a ** 2

    dphis = [dphi(pc, c) for c in cols]
    d2, d3 = dphis[1], dphis[2]
    # every factor is positive here: W23 >= lo(dphi_2) lo(drho_3) - hi|dphi_3| hi|drho_2|, in iv
    abs3 = iv.mpf(max(abs(d3.a), abs(d3.b)))
    W23 = iv.mpf(d2.a) * iv.mpf(drho3_lo.a) - abs3 * iv.mpf(drho2_abs.b)
    W23_lo = W23.a
    wedge_nonzero = bool(d2.a > 0 and drho3_lo.a > 0 and W23_lo > 0)
    guard = guard_all_gate_kernels()
    terminal = ("B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY"
                if (wedge_nonzero and chart_rank3 and guard["ok"]) else "B3_INCONCLUSIVE_BY_BOUNDS")
    f = lambda x: [b15.iv_lo(x), b15.iv_hi(x)]  # noqa: E731   outward into binary64
    out = {
        "unit": "PUENTE-3P1/B3_CERTIFICATE", "M": M,
        "frozen_lambda_binary64": [float(x) for x in gate.LAM],
        "chart_x": [str(x) for x in X], "chart_jacobian_columns": [[str(v) for v in c] for c in cols],
        "chart_det_rows_v1_uout_uin": str(det), "chart_rank_three": chart_rank3,
        "drho_dx3": {"S_lo_e3": r3["S_lo"], "Z": r3["Z"], "B_hi": r3["B_hi"],
                     "Bprime_lo_e3": r3["Bprime_lo"], "lower_bound": b15.iv_lo(drho3_lo)},
        "drho_dx2_abs_upper": b15.iv_hi(drho2_abs),
        "phi_pieces": {k: f(v) for k, v in pc.items()},
        "dphi_dx": [f(x) for x in dphis],
        "wedge_x2x3_lower_bound": b15.iv_lo(W23),
        "dphi_wedge_drho_certified_nonzero": wedge_nonzero,
        "fastmath_guard": guard,
        "no_new_path": True, "no_new_point": True, "no_search": True, "no_seeds": True,
        "no_monte_carlo": True, "terminal": terminal,
    }
    print(json.dumps(out, indent=2))
    if len(sys.argv) <= 1:
        (HERE / "verification_b3_certificate.json").write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
