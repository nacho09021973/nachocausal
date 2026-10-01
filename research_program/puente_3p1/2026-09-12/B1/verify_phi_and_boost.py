"""PUENTE-3P1 / B1 — phi(lambda) en forma cerrada y estructura gauge de boost.

Verifica numericamente tres cosas sobre la carta Kruskal de op11 §2:

  D1  Reduccion a primitiva: con w = UV y s(w) definido por (1-s)e^s = w,
      el integrando de volumen cumple G(w)dw = -s^2 ds, luego
      W(w) = -s(w)^3/3 es primitiva de G. Se comprueba contra cuadratura 2D.

  D2  Forma cerrada de phi(lambda):
        F_in  = (1/3) int_{v0}^{v1} [1 - s(u_in V)^3]   dV/V
        F_out = (1/3) int_{v0}^{v1} [s(-u_out V)^3 - 1] dV/V
        phi   = F_in / (F_in + F_out)

  D3  El boost de Killing B_a: (U,V) -> (aU, V/a) es isometria; actua sobre
      lambda como (v0,v1,u_out,u_in) -> (v0/a, v1/a, a*u_out, a*u_in) y deja
      phi invariante. Es por tanto una direccion GAUGE en el espacio de patches:
      un par testigo que solo difiera por un boost es espurio.

No ejecuta simulacion, no consume semillas, no toca ningun sello.
Salida: verification_phi_and_boost.json
"""
import json
import numpy as np
from scipy.optimize import brentq
from scipy import integrate

# s(w): rama unica de (1-s)e^s = w, decreciente en s; w<1 (w=1 es r=0).
def s_of_w(w):
    if w >= 1.0:
        raise ValueError("w>=1 toca la singularidad r=0")
    f = lambda s: (1.0 - s) * np.exp(s) - w
    hi = 1.0
    while f(hi) > 0:          # exterior: s>1
        hi *= 2.0
        if hi > 1e4:
            raise RuntimeError("sin bracket")
    return brentq(f, 0.0, hi, xtol=1e-14, rtol=1e-15)

def G(w):                      # integrando de volumen, s e^{-s}
    s = s_of_w(w)
    return s * np.exp(-s)

# --- D1: primitiva W(w) = -s(w)^3/3 ---------------------------------------
def W(w):
    return -s_of_w(w) ** 3 / 3.0

d1_pairs = []
for (a, b) in [(-3.0, -0.5), (-1.0, 0.4), (0.05, 0.7), (-2.5, 0.9)]:
    quad, _ = integrate.quad(G, a, b, limit=300)
    prim = W(b) - W(a)
    d1_pairs.append({"a": a, "b": b, "quad": quad, "primitive": prim,
                     "abs_err": abs(quad - prim)})
d1_ok = all(p["abs_err"] < 1e-9 for p in d1_pairs)

# --- D2: forma cerrada de phi contra cuadratura 2D -------------------------
def phi_closed(v0, v1, u_out, u_in):
    f_in  = integrate.quad(lambda V: (1.0 - s_of_w(u_in * V) ** 3) / V,
                           v0, v1, limit=300)[0] / 3.0
    f_out = integrate.quad(lambda V: (s_of_w(-u_out * V) ** 3 - 1.0) / V,
                           v0, v1, limit=300)[0] / 3.0
    return f_in / (f_in + f_out), f_in, f_out

def phi_quad2d(v0, v1, u_out, u_in):
    inner = integrate.dblquad(lambda U, V: G(U * V), v0, v1,
                              lambda V: 0.0, lambda V: u_in, epsabs=1e-11)[0]
    outer = integrate.dblquad(lambda U, V: G(U * V), v0, v1,
                              lambda V: -u_out, lambda V: 0.0, epsabs=1e-11)[0]
    return inner / (inner + outer)

LAMBDAS = [  # (v0, v1, u_out, u_in), todos con u_in*v1 <= 1-eps_s
    (0.5, 1.0, 1.0, 0.5),
    (0.2, 0.8, 2.0, 0.9),
    (0.4, 1.6, 0.7, 0.4),
]
d2_rows = []
for (v0, v1, u_out, u_in) in LAMBDAS:
    pc, f_in, f_out = phi_closed(v0, v1, u_out, u_in)
    pq = phi_quad2d(v0, v1, u_out, u_in)
    d2_rows.append({"lambda": [v0, v1, u_out, u_in], "phi_closed": pc,
                    "phi_quad2d": pq, "abs_err": abs(pc - pq),
                    "u_in_times_v1": u_in * v1})
d2_ok = all(r["abs_err"] < 1e-8 for r in d2_rows)

# --- D3: invariancia de phi bajo el boost de Killing ------------------------
d3_rows = []
for (v0, v1, u_out, u_in) in LAMBDAS:
    base = phi_closed(v0, v1, u_out, u_in)[0]
    for a in (0.5, 1.7, 3.0):
        bo = phi_closed(v0 / a, v1 / a, a * u_out, a * u_in)[0]
        d3_rows.append({"lambda": [v0, v1, u_out, u_in], "a": a,
                        "phi": base, "phi_boosted": bo,
                        "abs_err": abs(base - bo)})
d3_ok = all(r["abs_err"] < 1e-9 for r in d3_rows)

# invariantes de boost: 4 parametros - 1 gauge = 3
def boost_invariants(v0, v1, u_out, u_in):
    return [v1 / v0, u_in / u_out, u_in * v1]

d3_inv = []
for (v0, v1, u_out, u_in) in LAMBDAS:
    i0 = boost_invariants(v0, v1, u_out, u_in)
    i1 = boost_invariants(v0 / 1.7, v1 / 1.7, 1.7 * u_out, 1.7 * u_in)
    d3_inv.append({"lambda": [v0, v1, u_out, u_in],
                   "inv": i0, "inv_boosted": i1,
                   "max_abs_err": max(abs(x - y) for x, y in zip(i0, i1))})
d3_inv_ok = all(r["max_abs_err"] < 1e-12 for r in d3_inv)

out = {
    "unit": "PUENTE-3P1/B1",
    "source_chart": "research_program/synthesis/op11_spherical_dual_target.md#2",
    "D1_primitive_matches_quadrature": d1_ok, "D1_rows": d1_pairs,
    "D2_closed_form_matches_2d_quadrature": d2_ok, "D2_rows": d2_rows,
    "D3_phi_boost_invariant": d3_ok, "D3_rows": d3_rows,
    "D3_boost_invariants_preserved": d3_inv_ok, "D3_invariant_rows": d3_inv,
    "BOOST_IS_GAUGE_ON_LAMBDA": bool(d3_ok and d3_inv_ok),
    "EFFECTIVE_LAMBDA_DIMENSION": 3,
    "CONCLUSION": ("PHI_CLOSED_FORM_VERIFIED_BOOST_IS_GAUGE"
                   if (d1_ok and d2_ok and d3_ok and d3_inv_ok) else "VERIFICATION_FAILED"),
}
for k in ("D1_primitive_matches_quadrature", "D2_closed_form_matches_2d_quadrature",
          "D3_phi_boost_invariant", "D3_boost_invariants_preserved"):
    assert out[k], f"fallo: {k}"
print(json.dumps({k: v for k, v in out.items() if not k.endswith("_rows")}, indent=2))
with open(__file__.rsplit("/", 1)[0] + "/verification_phi_and_boost.json", "w") as fh:
    json.dump(out, fh, indent=2)
