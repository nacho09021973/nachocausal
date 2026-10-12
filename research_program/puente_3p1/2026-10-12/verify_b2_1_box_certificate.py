"""PUENTE-3P1 / B2.1 -- drho/dt > 0 on the whole frozen mesh hull t in [0.45, 0.55].

B2.1 (research_program/puente_3p1/2026-09-12/B2_1_local_order_law_injectivity.md) asks for local
injectivity of t -> rho(lambda(t)) near t0 = 0.5 on the frozen mesh {0.45, ..., 0.55}, by "an
envelope of the derivative that excludes zero".  The gate certificate (2026-10-11, promoted) gives
the sign only AT t0; its continuity transfer (2026-10-12) reaches a radius of 1e-7 only, because h
has a sqrt modulus.  This file instead bounds S directly over BOXES of lambda.

Box.  [0.45, 0.55] is cut into N equal t-intervals T_k.  On T_k every coordinate of lambda(t) is
affine and monotone, for the binary64-endpoint curve and for the decimal curve alike; c_lo / c_hi
are the outward-rounded min / max over both curves and both ends.  For every lambda in that box:
    K_in  = [-uo_lo, ui_lo] x [v0_hi, v1_lo]   subset of  K(lambda)  subset of
    K_out = [-uo_hi, ui_hi] x [v0_lo, v1_hi].
Each face of K(lambda) lies in a thin STRIP (e.g. U = u_in(lambda) in [ui_lo, ui_hi]).  The
direction d enters only through the face velocities v_n, enclosed for both curves' d.

Bounds (g, h >= 0, so integrals are monotone in the domain):
  Z      in [Z(K_in)_lo, Z(K_out)_hi];          B <= B(K_out)_hi   (gate's b_hi_sum on K_out)
  I_f = int_face g H_K, faces with v_n > 0 (U=-u_out, U=u_in, V=v0):
         I_f >= sum over strip cells of the INNER face extent of len_lo * g_lo(cell) * H_lo(cell),
         H_lo(cell) = sum_Q W_lo(Q) [p_lo(LB(c_top, Q_bot)) + p_lo(LB(Q_top, c_bot))],  Q in K_in,
         by monotonicity of the sup in the endpoints (gate note section 2.2): every x of the cell
         lies above c_bot and below c_top, and H_K >= H_{K_in};
  face V=v1 (v_n < 0): I_f <= sum over strip cells of the OUTER extent of len_hi * g_hi * H_hi,
         H_hi(cell) = sum_Q W_hi(Q) [p_hi(UB(c_bot, Q_top)) + p_hi(UB(Q_bot, c_top))],  Q in K_out,
         whose lattice has v1_lo as its second-to-last V node, so both cell corners are lattice
         points and the gate's ub_table applies unchanged;
  J_f = int_face g: upper over the outer extent for v_n > 0, lower over the inner extent for v1;
  S_lo = B'_lo - (2 Z'_hi / Z_lo) B_hi,   B'_lo = 2 sum_f (v_n lo) * (I_f lower or upper).

Arithmetic: the gate's (section 3 of its note): one ulp outward after every binary64 operation,
certified monotone tables from B1.5's scalar layer, B1.5's directed pairwise sums, fast-math guard
over the gate's kernels AND the three new ones.  M (lattice) and N (boxes) are proof parameters:
any values give valid bounds.

Determinism: no seeds, no Monte Carlo, no search over lambda, t0 or points; the curve and the
interval [0.45, 0.55] are the frozen B2.1 ones.
Usage: .venv/bin/python research_program/puente_3p1/2026-10-12/verify_b2_1_box_certificate.py
       [M N [k0 k1]]     (a partial range k0..k1-1 prints and does not write the JSON)
"""
import json
import math
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from numba import njit, prange

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "2026-10-11"))
import verify_b2_path2_gate_certificate as gate  # noqa: E402

b15 = gate.b15
up, dn, _up, _dn = gate.up, gate.dn, gate._up, gate._dn

# --- frozen inputs ---------------------------------------------------------------------------
L0, L1 = gate.L0, gate.L1                                  # binary64, as every frozen B2 script
DEC0 = ("0.5", "1.0", "1.0", "0.5", "0.1")
DEC1 = ("0.2", "0.8", "2.0", "0.9", "0.1")
T_LO, T_HI = Fr(45, 100), Fr(55, 100)                      # hull of the frozen B2.1 mesh
CURVES = [([Fr(float(x)) for x in L0], [Fr(float(x)) for x in L1]),
          ([Fr(x) for x in DEC0], [Fr(x) for x in DEC1])]

# --- proof parameters (any values give a valid bound) -----------------------------------------
M_DEFAULT = 128
N_DEFAULT = 100
R_SUB, N_TAU = gate.R_SUB, gate.N_TAU


def coord_range(i, ta, tb):
    """Outward binary64 (lo, hi) of coordinate i over t in [ta, tb], both curves."""
    vals = [a[i] + t * (b[i] - a[i]) for a, b in CURVES for t in (ta, tb)]
    return float(dn(float(min(vals)))), float(up(float(max(vals))))


def vn_range(name):
    """Outward (lo, hi) of the outward normal velocity of a face, both curves' directions."""
    idx, sgn = {"U=-u_out": (2, 1), "U=u_in": (3, 1), "V=v0": (0, -1), "V=v1": (1, 1)}[name]
    vals = [sgn * (b[idx] - a[idx]) for a, b in CURVES]
    return float(dn(float(min(vals)))), float(up(float(max(vals))))


def w_table_global():
    """One certified w table for every box: the range of K_out over the whole interval."""
    uo = coord_range(2, T_LO, T_HI)[1]
    ui = coord_range(3, T_LO, T_HI)[1]
    v1 = coord_range(1, T_LO, T_HI)[1]
    wlo = float(dn(-uo * v1)) - 1e-3
    whi = float(up(ui * v1)) + 1e-3
    assert whi < 1.0
    left = np.linspace(wlo, 0.0, gate.NT_HALF + 1)
    right = np.linspace(0.0, whi, gate.NT_HALF + 1)[1:]
    wt = np.concatenate([left, right])
    assert np.all(np.diff(wt) > 0) and wt[gate.NT_HALF] == 0.0
    return wt


# ---------------------------------------------------------------------------------------------
# New kernels (the rest are the gate's, imported unchanged).
# ---------------------------------------------------------------------------------------------
@njit(parallel=True, cache=True)
def lb_rows_xy(srcU, srcV, forward, Ug, Vg, wt, qlo, bt, plo_p, ntau):
    """p_lo(LB) between arbitrary source points and every lattice point.  Same arithmetic as the
    gate's lb_rows; forward: the source is the past end, else the future end."""
    n1 = Ug.size
    npt = n1 * n1
    out = np.zeros((srcU.size, npt))
    inv = 1.0 / ntau
    for r in prange(srcU.size):
        for x in range(npt):
            ix, jx = x // n1, x % n1
            if forward:
                Ua, Va, Ub, Vb = srcU[r], srcV[r], Ug[ix], Vg[jx]
            else:
                Ua, Va, Ub, Vb = Ug[ix], Vg[jx], srcU[r], srcV[r]
            if not (Ub > Ua and Vb > Va):
                continue
            du_lo, du_hi = _dn(Ub - Ua), _up(Ub - Ua)
            dv_lo, dv_hi = _dn(Vb - Va), _up(Vb - Va)
            acc = 0.0
            for k in range(ntau):
                t0, t1 = k * inv, (k + 1) * inv
                U_lo = _dn(Ua + _dn(du_lo * t0))
                U_hi = _up(Ua + _up(du_hi * t1))
                V_lo = _dn(Va + _dn(dv_lo * t0))
                V_hi = _up(Va + _up(dv_hi * t1))
                w_lo = _dn(U_lo * V_lo) if U_lo >= 0.0 else _dn(U_lo * V_hi)
                kq = gate.k_below(wt, w_lo)
                if kq >= 0:
                    acc = _dn(acc + qlo[kq])
            line = _dn(_dn(math.sqrt(_dn(du_lo * dv_lo))) * _dn(acc * inv))
            out[r, x] = gate.p_lo_of(line, bt, plo_p)
    return out


@njit(cache=True)
def strip_weights(u_face, a0, a1, grid, r, wt, glo, ghi, e_inv_hi):
    """Per segment of `grid` along a face: (lo, hi) of len * G over the strip cell.
    u_face: the face is U = const in [a0, a1] and the grid runs along V; else V = const."""
    n = grid.size - 1
    lo = np.zeros(n); hi = np.zeros(n)
    for i in range(n):
        xs = gate.tiling(grid[i], grid[i + 1], r)
        alo = 0.0; ahi = 0.0
        for a in range(r):
            if u_face:
                wl, wh = gate.rect_w(a0, a1, xs[a], xs[a + 1])
            else:
                wl, wh = gate.rect_w(xs[a], xs[a + 1], a0, a1)
            gl, gh = gate.g_range(wl, wh, wt, glo, ghi, e_inv_hi)
            alo = _dn(alo + _dn(_dn(xs[a + 1] - xs[a]) * gl))
            ahi = _up(ahi + _up(_up(xs[a + 1] - xs[a]) * gh))
        lo[i] = alo; hi[i] = ahi
    return lo, hi


@njit(cache=True)
def face_h_cells(M, W, fwd, bwd, lower):
    """H per strip cell from per-cell rows over the lattice of an M x M cell grid.
    lower: fwd[i] = p_lo(c_top -> .), bwd[i] = p_lo(. -> c_bot): uses Q_bot / Q_top.
    upper: fwd[i] = p_hi(c_bot -> .), bwd[i] = p_hi(. -> c_top): uses Q_top / Q_bot."""
    n1 = M + 1
    ncell = fwd.shape[0]
    H = np.zeros(ncell)
    for i in range(ncell):
        acc = 0.0
        for Q in range(M * M):
            iQ, jQ = Q // M, Q % M
            bot = iQ * n1 + jQ
            top = (iQ + 1) * n1 + (jQ + 1)
            if lower:
                v = fwd[i, bot] + bwd[i, top]
                acc = _dn(acc + _dn(W[Q] * _dn(v)))
            else:
                v = fwd[i, top] + bwd[i, bot]
                acc = _up(acc + _up(W[Q] * _up(v)))
        H[i] = acc
    return H


NEW_KERNELS = (lb_rows_xy, strip_weights, face_h_cells)
# Gate kernels this file never calls: replaced by the three new ones above.  They are excluded
# BY NAME, so the guard still demands a compiled signature for every kernel that runs here.
GATE_UNUSED = ("lb_rows", "face_h", "segment_weights")


def fresh_ir(fn):
    """LLVM IR of `fn` recompiled WITHOUT the on-disk cache, for every signature it has run with.

    A dispatcher loaded from numba's cache returns an EMPTY module from inspect_llvm (numba warns
    "Inspection disabled for cached code"), so a guard reading it passes vacuously.  Recompiling
    the same py_func with the same options minus `cache` gives the IR that is actually inspected;
    each module must contain the function's definition, so an empty one fails."""
    opts = {k: v for k, v in fn.targetoptions.items() if k not in ("cache", "nopython")}
    fresh = njit(**opts)(fn.py_func)
    out = []
    for sig in fn.signatures:
        fresh.compile(sig)
        ir = fresh.inspect_llvm(sig)
        if "define " not in ir or fn.py_func.__name__ not in ir:
            raise RuntimeError("empty or foreign IR for %s" % fn.py_func.__name__)
        out.append(ir)
    return out


def fastmath_guard():
    gate._compile_helpers()
    used = tuple(fn for fn in gate.KERNELS if fn.py_func.__name__ not in GATE_UNUSED) + NEW_KERNELS
    assert len(used) == len(gate.KERNELS) - len(GATE_UNUSED) + len(NEW_KERNELS)
    uncompiled = [fn.py_func.__name__ for fn in used if not fn.signatures]
    flags, ir_chars = {}, {}
    for fn in used:
        irs = fresh_ir(fn)
        flags[fn.py_func.__name__] = sorted({m.group(0) for ir in irs for m in gate._FAST.finditer(ir)})
        ir_chars[fn.py_func.__name__] = sum(len(ir) for ir in irs)

    @njit(fastmath=True)
    def _mutant(a, b, c):
        return a * b + c
    _mutant(1.0, 2.0, 3.0)
    mutant_caught = bool(gate.fastmath_flags(_mutant))
    # the mutant must also be caught THROUGH fresh_ir, the path the kernels go through
    mutant_fresh = bool(gate._FAST.search(fresh_ir(_mutant)[0]))
    clean = all(not v for v in flags.values())
    return {"kernels_checked": len(flags), "inspection": "fresh recompilation without cache",
            "min_ir_chars": min(ir_chars.values()),
            "gate_kernels_excluded_as_unused": list(GATE_UNUSED),
            "kernels_without_compiled_signature": uncompiled,
            "flags_found": {k: v for k, v in flags.items() if v}, "all_clean": clean,
            "mutation_fastmath_detected": bool(mutant_caught and mutant_fresh),
            "ok": bool(clean and mutant_caught and mutant_fresh and not uncompiled)}


# ---------------------------------------------------------------------------------------------
# One box.
# ---------------------------------------------------------------------------------------------
def run_box(ta, tb, M, T):
    wt, qlo, glo, ghi, Flo, Fhi, bt, plo_p, phi_p = T
    e_inv = b15.E_INV_HI
    v0_lo, v0_hi = coord_range(0, ta, tb)
    v1_lo, v1_hi = coord_range(1, ta, tb)
    uo_lo, uo_hi = coord_range(2, ta, tb)
    ui_lo, ui_hi = coord_range(3, ta, tb)
    assert 0 < v0_lo < v0_hi < v1_lo < v1_hi and 0 < ui_lo < ui_hi and 0 < uo_lo < uo_hi
    n1 = M + 1

    # ---- inner lattice: Z_lo and lower H ----
    Ug_i = np.linspace(-uo_lo, ui_lo, n1)
    Vg_i = np.linspace(v0_hi, v1_lo, n1)
    assert Ug_i[0] == -uo_lo and Ug_i[-1] == ui_lo and Vg_i[0] == v0_hi and Vg_i[-1] == v1_lo
    assert np.all(np.diff(Ug_i) > 0) and np.all(np.diff(Vg_i) > 0)
    Wi_lo, _ = gate.cell_weights(Ug_i, Vg_i, R_SUB, wt, glo, ghi, e_inv)
    Z_lo = b15.sum_dn(Wi_lo)

    # ---- outer lattice: Z_hi, B_hi, upper H; v1_lo is its second-to-last V node ----
    Ug_o = np.linspace(-uo_hi, ui_hi, n1)
    Vg_o = np.concatenate([np.linspace(v0_lo, v1_lo, M), [v1_hi]])
    assert Ug_o[0] == -uo_hi and Ug_o[-1] == ui_hi and Vg_o[0] == v0_lo
    assert Vg_o[M - 1] == v1_lo and Vg_o[M] == v1_hi
    assert np.all(np.diff(Ug_o) > 0) and np.all(np.diff(Vg_o) > 0)
    _, Wo_hi = gate.cell_weights(Ug_o, Vg_o, R_SUB, wt, glo, ghi, e_inv)
    Z_hi = b15.sum_up(Wo_hi)
    nulo, nuhi = gate.nu_enclosures(Vg_o)
    iu, jv = np.divmod(np.arange(n1 * n1), n1)
    PU, PV = Ug_o[iu], Vg_o[jv]
    wlo_pt, whi_pt = dn(PU * PV), up(PU * PV)
    cs = np.concatenate([gate.C_POS, gate.C_NEG])
    AU_lo, AU_hi, AL_lo, AL_hi, thr = gate.calibration_point_tables(
        cs, wt, Flo, Fhi, wlo_pt, whi_pt, nulo[jv], nuhi[jv])
    Pcs_lo, Pcs_hi = gate.cs_prefix(Ug_o, Vg_o, R_SUB, wt, Fhi)
    pub = gate.ub_table(M, Ug_o, Vg_o, wlo_pt, whi_pt, AU_lo, AU_hi, AL_lo, AL_hi, thr,
                        Pcs_lo, Pcs_hi, bt, phi_p)
    del AU_lo, AU_hi, AL_lo, AL_hi
    B_hi = gate.b_hi_sum(M, Wo_hi, pub)

    # ---- faces ----
    lower_faces = {   # name: (u_face, strip a0, a1, inner grid along the face, outer grid)
        "U=-u_out": (True, -uo_hi, -uo_lo, Vg_i, Vg_o),
        "U=u_in": (True, ui_lo, ui_hi, Vg_i, Vg_o),
        "V=v0": (False, v0_lo, v0_hi, Ug_i, Ug_o),
    }
    Bp_terms, Zp_hi_terms, Zp_lo_terms, face_out = [], [], [], {}
    for name, (u_face, a0, a1, g_in, g_out) in lower_faces.items():
        vn_lo, vn_hi = vn_range(name)
        assert vn_lo > 0
        seg_lo, _ = strip_weights(u_face, a0, a1, g_in, R_SUB, wt, glo, ghi, e_inv)
        if u_face:     # cell j: c_bot = (a0, V_j), c_top = (a1, V_j+1)
            bU, bV, tU, tV = np.full(M, a0), g_in[:-1], np.full(M, a1), g_in[1:]
        else:          # cell i: c_bot = (U_i, a0), c_top = (U_i+1, a1)
            bU, bV, tU, tV = g_in[:-1], np.full(M, a0), g_in[1:], np.full(M, a1)
        fwd = lb_rows_xy(tU.copy(), tV.copy(), True, Ug_i, Vg_i, wt, qlo, bt, plo_p, N_TAU)
        bwd = lb_rows_xy(bU.copy(), bV.copy(), False, Ug_i, Vg_i, wt, qlo, bt, plo_p, N_TAU)
        H = face_h_cells(M, Wi_lo, fwd, bwd, True)
        inner = b15.sum_dn(dn(seg_lo * H))
        term = float(dn(2.0 * dn(vn_lo * inner)))
        Jo_lo, Jo_hi = strip_weights(u_face, a0, a1, g_out, R_SUB, wt, glo, ghi, e_inv)
        Ji_lo, _ = strip_weights(u_face, a0, a1, g_in, R_SUB, wt, glo, ghi, e_inv)
        Zp_hi_terms.append(float(up(vn_hi * b15.sum_up(Jo_hi))))
        Zp_lo_terms.append(float(dn(vn_lo * b15.sum_dn(Ji_lo))))
        Bp_terms.append(term)
        face_out[name] = term

    # face V = v1 (v_n < 0): upper I over the outer extent, strip cells on the outer lattice
    vn_lo, vn_hi = vn_range("V=v1")
    assert vn_hi < 0
    _, seg_hi = strip_weights(False, v1_lo, v1_hi, Ug_o, R_SUB, wt, glo, ghi, e_inv)
    cbot = np.arange(M) * n1 + (M - 1)            # (U_i, v1_lo)
    ctop = (np.arange(M) + 1) * n1 + M            # (U_i+1, v1_hi)
    H = face_h_cells(M, Wo_hi, pub[cbot, :], pub[:, ctop].T.copy(), False)
    inner = b15.sum_up(up(seg_hi * H))
    term = float(dn(2.0 * dn(vn_lo * inner)))
    Ji_lo, _ = strip_weights(False, v1_lo, v1_hi, Ug_i, R_SUB, wt, glo, ghi, e_inv)
    Zp_hi_terms.append(float(up(vn_hi * b15.sum_dn(Ji_lo))))
    Zp_lo_terms.append(float(dn(vn_lo * b15.sum_up(seg_hi))))
    Bp_terms.append(term)
    face_out["V=v1"] = term
    del pub

    Bp_lo = b15.sum_dn(Bp_terms)
    Zp_lo, Zp_hi = b15.sum_dn(Zp_lo_terms), b15.sum_up(Zp_hi_terms)
    assert Zp_hi > 0
    k_hi = float(up(2.0 * up(Zp_hi / Z_lo)))
    S_lo = float(dn(Bp_lo - up(k_hi * B_hi)))
    drho_lo = float(dn(S_lo / up(Z_hi * Z_hi))) if S_lo > 0 else None
    return {"t": [str(ta), str(tb)],
            "box": {"v0": [v0_lo, v0_hi], "v1": [v1_lo, v1_hi], "u_out": [uo_lo, uo_hi],
                    "u_in": [ui_lo, ui_hi]},
            "Z": [Z_lo, Z_hi], "Zprime": [Zp_lo, Zp_hi], "two_Zp_over_Z_hi": k_hi,
            "B_hi": B_hi, "Bprime_lo": Bp_lo, "faces_Bprime_lower": face_out,
            "S_lo": S_lo, "drho_dt_lower_bound": drho_lo}


def tables():
    wt = w_table_global()
    qlo, qhi, glo, ghi, Flo, Fhi = gate.certified_tables(wt)
    bt, plo_p, phi_p = gate.p_table()
    return wt, qlo, glo, ghi, Flo, Fhi, bt, plo_p, phi_p


def main():
    args = sys.argv[1:]
    M = int(args[0]) if args else M_DEFAULT
    N = int(args[1]) if len(args) > 1 else N_DEFAULT
    k0, k1 = (int(args[2]), int(args[3])) if len(args) > 3 else (0, N)
    full = (k0, k1) == (0, N) and M == M_DEFAULT and N == N_DEFAULT
    t_start = time.time()
    T = tables()
    t_tab = time.time() - t_start
    width = (T_HI - T_LO) / N
    boxes = []
    for k in range(k0, k1):
        ta, tb = T_LO + k * width, T_LO + (k + 1) * width
        t1 = time.time()
        res = run_box(ta, tb, M, T)
        res["seconds"] = round(time.time() - t1, 1)
        boxes.append(res)
        print(f"box {k:3d} t=[{float(ta):.4f},{float(tb):.4f}]  S_lo={res['S_lo']:+.6f}  "
              f"B'_lo={res['Bprime_lo']:.6f}  B_hi={res['B_hi']:.6f}  ({res['seconds']} s)",
              flush=True)
    guard = fastmath_guard()
    worst = min(boxes, key=lambda b: b["S_lo"])
    all_pos = all(b["S_lo"] > 0 for b in boxes)
    terminal = ("B2.1_POSITIVE_DERIVATIVE" if (all_pos and guard["ok"] and full)
                else "B2.1_INCONCLUSIVE_BY_BOUNDS" if full else "PARTIAL_RUN_NO_TERMINAL")
    out = {
        "unit": "PUENTE-3P1/B2.1_BOX_CERTIFICATE",
        "interval_t": [str(T_LO), str(T_HI)], "curves": "binary64 endpoints and decimal, both",
        "M": M, "N": N, "boxes_run": [k0, k1], "R_sub": R_SUB, "N_tau": N_TAU,
        "w_table_nodes": int(T[0].size), "seconds_tables": round(t_tab, 1),
        "min_S_lo": worst["S_lo"], "min_S_lo_box_t": worst["t"],
        "min_drho_dt_lower_bound": min((b["drho_dt_lower_bound"] or -1.0) for b in boxes),
        "fastmath_guard": guard, "boxes": boxes,
        "no_new_path": True, "no_new_t0": True, "no_new_points": True, "no_search": True,
        "no_adjustment": True, "no_seeds": True, "no_monte_carlo": True,
        "terminal": terminal,
    }
    print(json.dumps({k: v for k, v in out.items() if k != "boxes"}, indent=2))
    if full:
        (HERE / "verification_b2_1_box_certificate.json").write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
