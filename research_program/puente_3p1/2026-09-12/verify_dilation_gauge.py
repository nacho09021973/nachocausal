"""PUENTE-3P1 / B0 — verificacion simbolica de la orbita de dilatacion.

Verifica, sobre la carta Kruskal congelada en
`research_program/synthesis/op11_spherical_dual_target.md` §2, las tres
afirmaciones que fijan que target 3+1D es admisible a `fixed_n`:

  C1  s(UV) = r/(2M) queda determinado por el producto UV, sin M explicito
      (la rama s>0 de f(s)=(s-1)e^s es estrictamente creciente).
  C2  sqrt(-det g) = 32 M^4 s e^{-s} sin(theta), es decir la dependencia en M
      del elemento de volumen factoriza exactamente como M^4.
  C3  la medida normalizada mu_M/mu_M(K) es independiente de M para todo patch
      K congelado en coordenadas Kruskal (lambda fijo).

No ejecuta simulacion, no consume semillas, no toca ningun sello.
Salida: verification_dilation_gauge.json
"""
import json
import sympy as sp

U, V, M, th = sp.symbols("U V M theta", real=True)
s = sp.Symbol("s", positive=True)

# --- C1: monotonia estricta de f(s)=(s-1)e^s en s>0 -------------------------
f = (s - 1) * sp.exp(s)
fp = sp.simplify(sp.diff(f, s))
c1_derivative = sp.srepr(fp)
c1_strictly_increasing = bool(sp.simplify(fp - s * sp.exp(s)) == 0)  # f' = s e^s > 0 en s>0

# --- C2: elemento de volumen de la metrica OP-1.1 ---------------------------
# ds^2 = -(32 M^3/r) e^{-r/2M} dU dV + r^2 dOmega^2,  r = 2 M s
r = 2 * M * s
g_UV = -sp.Rational(1, 2) * (32 * M**3 / r) * sp.exp(-r / (2 * M))   # componente simetrica
g = sp.Matrix([
    [0,    g_UV, 0,      0],
    [g_UV, 0,    0,      0],
    [0,    0,    r**2,   0],
    [0,    0,    0,      r**2 * sp.sin(th)**2],
])
det_g = sp.simplify(g.det())
vol = sp.simplify(sp.sqrt(-det_g))
vol_expected = 32 * M**4 * s * sp.exp(-s) * sp.Abs(sp.sin(th))
c2_matches = bool(sp.simplify(vol - vol_expected) == 0)

# --- C3: la M-dependencia es un prefactor global -> se cancela al normalizar -
integrand = vol / (32 * M**4)          # parte M-independiente del integrando
c3_integrand_is_M_free = bool(sp.simplify(sp.diff(integrand, M)) == 0)
# mu_M(K) = M^4 * mu_1(K) para K congelado en (U,V,theta,phi) => cociente sin M
c3_normalized_measure_M_free = c2_matches and c3_integrand_is_M_free

out = {
    "unit": "PUENTE-3P1/B0",
    "source_chart": "research_program/synthesis/op11_spherical_dual_target.md#2",
    "C1_f_prime": c1_derivative,
    "C1_f_prime_equals_s_exp_s": c1_strictly_increasing,
    "C1_s_determined_by_UV": c1_strictly_increasing,
    "C2_volume_element": sp.srepr(vol),
    "C2_matches_32_M4_s_exp_minus_s_sin_theta": c2_matches,
    "C3_integrand_M_free": c3_integrand_is_M_free,
    "C3_normalized_measure_M_free": c3_normalized_measure_M_free,
    "CONCLUSION": (
        "DILATION_IS_PURE_GAUGE_AT_FIXED_N" if (c1_strictly_increasing and c3_normalized_measure_M_free)
        else "VERIFICATION_FAILED"
    ),
}
assert c1_strictly_increasing, "C1 fallo: f'(s) != s e^s"
assert c2_matches, "C2 fallo: elemento de volumen no factoriza como M^4"
assert c3_normalized_measure_M_free, "C3 fallo: la medida normalizada depende de M"
print(json.dumps(out, indent=2))
with open(__file__.rsplit("/", 1)[0] + "/verification_dilation_gauge.json", "w") as fh:
    json.dump(out, fh, indent=2)
