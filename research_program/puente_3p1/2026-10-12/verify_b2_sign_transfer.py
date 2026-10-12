"""PUENTE-3P1 / B2 -- transfer of the gate's sign from lambda*_binary64 to the real midpoint.

The gate certificate (research_program/puente_3p1/2026-10-11/, frozen in 7909c0e, promoted in
be34b74) bounds S(lambda*; d) >= S_lo > 0 at the binary64 point lambda* = path(0.5) along the
exact binary64 direction d = L1 - L0 (its H5).  This file shows that the sign survives the move
to the real curve, by an explicit continuity modulus, for every point within sup-distance
DELTA of lambda* and every direction within sup-distance EPS of d.  Both real targets lie in
that set:

  * the decimal midpoint  m_dec = (lambda0_dec + lambda1_dec)/2,  direction d_dec;
  * the exact midpoint of the binary64 endpoints  m_bin = (L0 + L1)/2,  direction d.

Objects (gate note, section 2 and H2/H3): rectangle K = [-u_out, u_in] x [v0, v1] in (U, V);
weight g = G(UV), G(w) = s e^{-s}; q(w) = 2 e^{-s/2} s^{-3/2}; (1 - s) e^s = w;
h = p(Delta_max), p(b) = (1 - cos min(b, pi))/2;  H_K(x) = int_K g(y) h(x, y) dy;
Z = int_K g;  B = int int g g h;  for a direction e, with I_f = int_f g H_K and J_f = int_f g
over face f and v_f(e) its outward normal velocity,
    S(x; e) = 2 sum_f v_f(e) I_f - 2 (B/Z) sum_f v_f(e) J_f ,   drho/dt = S / Z^2 .
S is linear in e, so  S(m; d') = S(m; d) + S(m; d' - d).

Bound, every piece enclosed in mpmath.iv with outward rounding:
  (1) point shift  |S(m; d) - S(lambda*; d)| <= DS_point(DELTA)
  (2) direction    |S(m; d' - d)|           <= DS_dir(DELTA, EPS)
  => S(m; d') >= S_lo - DS_point - DS_dir.

The modulus of h (the only non-Lipschitz piece): for x, x' within DELTA in each coordinate and
any y, writing A = dU, B = dV for the pair, Delta_max <= q_max sqrt(A+ B+) always, and for
A, B > 0 ASTRA's parametrisation (gate note H3) gives
    T = sqrt(A B) sup_f int_0^1 q(w_f(s)) sqrt(f'(s)) ds,   int sqrt(f') <= 1,
over one class of f for both pairs.  Hence, per orientation,
    |T - T'| <= q_max sqrt(DELTA (A_max + B_max + DELTA))
                + sqrt(A_max B_max) L_q (U_max + V_max + DELTA) DELTA ,
the cap min(pi, .) is 1-Lipschitz and p is 1/2-Lipschitz, and h = p(T_fut) + p(T_past) with
at most one nonzero, so |h(x,y) - h(x',y)| <= omega_h := the bound above.

Constants: g <= E_INV_HI (B1.5, >= 1/e).  On the w range of the enlarged rectangle,
s in [s_min, s_max] from B1.5's audited s_encl;  q increasing in w, so q_max = q_encl(w_cap);
 q'(w) = q (1/2 + 3/(2s)) / (s e^s)  (every factor decreasing in s)  => L_q at s_min;
|G'(w)| = |1 - s| e^{-2s} / s  <= max(|1-s_min|, |1-s_max|) e^{-2 s_min} / s_min.

Determinism: no seeds, no search over lambda, t0 or points.  The radius table at the end is a
diagnostic on a fixed list and does not enter the terminal.
Usage: .venv/bin/python research_program/puente_3p1/2026-10-12/verify_b2_sign_transfer.py
"""
import json
import sys
from fractions import Fraction as Fr
from pathlib import Path

from mpmath import iv

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT / "2026-09-12" / "B1"))
import verify_b1_5_analytic_separation as b15  # noqa: E402

iv.dps = 40
GATE_JSON = ROOT / "2026-10-11" / "verification_b2_path2_gate_certificate.json"
OUT = HERE / "verification_b2_sign_transfer.json"

# --- frozen inputs -------------------------------------------------------------------------
L0 = (0.5, 1.0, 1.0, 0.5, 0.1)          # binary64, as every frozen B2 script
L1 = (0.2, 0.8, 2.0, 0.9, 0.1)
DEC0 = ("0.5", "1.0", "1.0", "0.5", "0.1")
DEC1 = ("0.2", "0.8", "2.0", "0.9", "0.1")
NAMES = ("v0", "v1", "u_out", "u_in", "epsilon_s")

DELTA = Fr(1, 10 ** 16)                 # declared point radius (sup norm), >= both targets
EPS = Fr(1, 10 ** 16)                   # declared direction radius (sup norm)
DIAG_RADII = [Fr(1, 10 ** k) for k in (16, 14, 12, 10, 9, 8, 7, 6)]


def I(x):
    """Exact rational or float -> tight interval."""
    x = Fr(x)
    return iv.mpf(x.numerator) / iv.mpf(x.denominator)


def lam_star():
    """The binary64 path(0.5), computed exactly as the frozen scripts compute it."""
    import numpy as np
    lam = 0.5 * np.array(L0) + 0.5 * np.array(L1)
    return [Fr(float(x)) for x in lam]


def targets():
    ls = lam_star()
    m_dec = [(Fr(a) + Fr(b)) / 2 for a, b in zip(DEC0, DEC1)]
    m_bin = [(Fr(a) + Fr(b)) / 2 for a, b in zip(L0, L1)]
    d_bin = [Fr(b) - Fr(a) for a, b in zip(L0, L1)]
    d_dec = [Fr(b) - Fr(a) for a, b in zip(DEC0, DEC1)]
    out = {}
    for name, m, dd in (("decimal_midpoint", m_dec, d_dec), ("binary64_endpoint_midpoint", m_bin, d_bin)):
        dpt = max(abs(a - b) for a, b in zip(m[:4], ls[:4]))
        ddir = max(abs(a - b) for a, b in zip(dd[:4], d_bin[:4]))
        out[name] = {"point_offset_sup": dpt, "direction_offset_sup": ddir,
                     "epsilon_s_offset": abs(m[4] - ls[4])}
    return ls, d_bin, out


def scalar_constants(ls, delta):
    v0, v1, uo, ui = ls[:4]
    w_max = (ui + delta) * (v1 + delta)
    w_min = -(uo + delta) * (v1 + delta)
    assert w_max < 1
    w_cap = float(b15.up(float(w_max)))
    w_flr = float(b15.dn(float(w_min)))
    assert Fr(w_cap) >= w_max and Fr(w_flr) <= w_min
    s_min = b15.s_encl(w_cap)[0]           # s decreasing in w
    s_max = b15.s_encl(w_flr)[1]
    q_max = I(b15.q_encl(w_cap)[1])        # q increasing in w
    S = I(s_min)
    qS = 2 * iv.exp(-S / 2) / S ** iv.mpf(1.5)
    L_q = qS * (iv.mpf(1) / 2 + 3 / (2 * S)) / (S * iv.exp(S))
    one_minus = max(abs(1 - Fr(s_min)), abs(1 - Fr(s_max)))
    L_G = I(one_minus) * iv.exp(-2 * S) / S
    return {"w_cap": w_cap, "w_floor": w_flr, "s_min": s_min, "s_max": s_max,
            "q_max": q_max, "L_q": iv.mpf(L_q.b), "L_G": iv.mpf(L_G.b)}


def bound(ls, d_bin, gate, delta, eps):
    v0, v1, uo, ui = (I(x) for x in ls[:4])
    dl, ep = I(delta), I(eps)
    k = scalar_constants(ls, delta)
    gmax = I(b15.E_INV_HI)
    Lu, Lv = uo + ui, v1 - v0                       # V-face and U-face lengths
    Umax, Vmax = uo + dl, v1 + dl                   # u_out >= u_in, V > 0
    Amax, Bmax_ = Lu + 2 * dl, Lv + 2 * dl
    KD = 2 * dl * (Lv + 2 * dl) + 2 * dl * (Lu + 2 * dl)     # |K symdiff K'|
    KU = Amax * Bmax_                                          # |K union K'|

    Z_lo, Z_hi = I(gate["Z"][0]), I(gate["Z"][1])
    Zp_abs = I(max(abs(gate["Zprime"][0]), abs(gate["Zprime"][1])))
    k_star = I(gate["two_Zp_over_Z_hi"])
    B_hi = I(gate["B_hi"])

    dZ = gmax * KD
    Zmin, Zmax = Z_lo - dZ, Z_hi + dZ
    assert Zmin.a > 0
    dB = 2 * gmax ** 2 * KU * KD
    Bmax = B_hi + dB

    omega = k["q_max"] * iv.sqrt(dl * (Amax + Bmax_ + dl)) \
        + iv.sqrt(Amax * Bmax_) * k["L_q"] * (Umax + Vmax + dl) * dl

    # faces: (name, |v_n| at lambda*, length, coordinate bound for the G' term)
    vabs = {"U=-u_out": abs(d_bin[2]), "U=u_in": abs(d_bin[3]),
            "V=v0": abs(d_bin[0]), "V=v1": abs(d_bin[1])}
    faces = [("U=-u_out", Lv, Vmax), ("U=u_in", Lv, Vmax), ("V=v0", Lu, Umax), ("V=v1", Lu, Umax)]
    dI, dJ = {}, {}
    for name, length, cmax in faces:
        dJ[name] = 2 * dl * gmax + length * k["L_G"] * cmax * dl
        dI[name] = 2 * dl * gmax * Zmax + length * (
            k["L_G"] * cmax * dl * Zmax + gmax * (gmax * KD + Zmax * omega))
    dZp = sum(I(vabs[n]) * dJ[n] for n, _, _ in faces)
    dk = 2 * (dZp / Zmin + Zp_abs * dZ / (Zmin * Z_lo))
    dS_point = 2 * sum(I(vabs[n]) * dI[n] for n, _, _ in faces) + dk * Bmax + k_star * dB

    dS_dir = iv.mpf(0)
    for name, length, _ in faces:
        Lf = length + 2 * dl
        dS_dir += ep * (2 * Lf * gmax * Zmax + 2 * Lf * gmax * Bmax / Zmin)

    S_lo = I(gate["S_lo"])
    S_m = S_lo - dS_point - dS_dir
    drho = S_m / Zmax ** 2
    f = lambda x: float(x.b) if hasattr(x, "b") else float(x)   # noqa: E731
    return {
        "delta": str(delta), "eps": str(eps),
        "constants": {"w_cap": k["w_cap"], "w_floor": k["w_floor"], "s_min": k["s_min"],
                      "s_max": k["s_max"], "q_max_hi": f(k["q_max"]), "L_q_hi": f(k["L_q"]),
                      "L_G_hi": f(k["L_G"]), "g_max_hi": f(gmax)},
        "omega_h_hi": f(omega), "dZ_hi": f(dZ), "dB_hi": f(dB), "dZprime_hi": f(dZp),
        "dS_point_hi": f(dS_point), "dS_dir_hi": f(dS_dir),
        "S_lower_at_target": float(S_m.a),
        "drho_dt_lower_at_target": float(drho.a) if S_m.a > 0 else None,
        "sign_transferred": bool(S_m.a > 0),
    }


def main():
    gate = json.loads(GATE_JSON.read_text())
    assert gate["terminal"] == "B2_CORRECTED_POSITIVE" and gate["M"] == 128
    assert gate["S_lo"] == 0.0013679385529351228
    ls, d_bin, tg = targets()
    assert [float(x) for x in ls] == gate["frozen_point"]["lambda_star_binary64"]
    for t in tg.values():                               # both targets inside the declared set
        assert t["point_offset_sup"] <= DELTA and t["direction_offset_sup"] <= EPS

    main_res = bound(ls, d_bin, gate, DELTA, EPS)
    diag = [{"radius": str(r), "S_lower": bound(ls, d_bin, gate, r, Fr(0))["S_lower_at_target"]}
            for r in DIAG_RADII]
    terminal = "B2_SIGN_TRANSFERRED_TO_REAL_MIDPOINT" if main_res["sign_transferred"] \
        else "B2_SIGN_TRANSFER_INCONCLUSIVE"
    out = {
        "unit": "PUENTE-3P1 / B2 sign transfer",
        "gate_certificate": {"json": str(GATE_JSON.relative_to(ROOT.parent.parent)),
                             "S_lo": gate["S_lo"], "frozen_in": "7909c0e"},
        "targets": {n: {k: str(v) for k, v in t.items()} for n, t in tg.items()},
        "rho_independent_of_epsilon_s": "declared (gate note section 6); q_encl/G_encl take only w",
        "main": main_res,
        "diagnostic_radius_table_direction_fixed": diag,
        "no_new_path": True, "no_new_t0": True, "no_search": True, "no_adjustment": True,
        "terminal": terminal,
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
