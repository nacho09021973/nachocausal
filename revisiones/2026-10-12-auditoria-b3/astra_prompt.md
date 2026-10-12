Eres ASTRA, auditor independiente. No tienes acceso a ficheros, terminal, web ni herramientas: todo lo disponible está en este prompt. No escribas llamadas a herramientas; escribe tu intervención directamente. Etiqueta como [SOURCE] sólo lo que aparece abajo; cualquier otra cosa es, como mucho, [INFERENCE] o [UNVERIFIED]. Responde en español, como máximo 1200 palabras, punto por punto (§5.1–5 de la nota y el punto 6 del acta), con clasificación y condición de concesión, y termina con una línea 'Veredicto: <uno de los veredictos posibles>'.

# Acta — auditoría del certificado de B3

**Fecha:** 2026-10-12. **Convoca:** el PI. **Casa:** ASTRA (sellada, una sola intervención).

Se te pide **auditar**, no proponer trabajo nuevo. El objeto está congelado y subido **antes**
de esta auditoría (`1f7286d`). Tu trabajo es intentar **romperlo**. Un acuerdo fácil no tiene
valor.

No tienes herramientas. Solo cuentan esta acta y los adjuntos:

1. `B3_certificate.md` — la nota, con la lista de auditoría en su §5.
2. `verify_b3_certificate.py` — el verificador.
3. `verification_b3_certificate.json` — su salida.
4. `B3_transverse_n2_audit.md` — la especificación de B3: la carta, los terminales y la
   definición de `phi`. Su cuerpo es histórico.
5. `verify_b3_transverse_n2.py` — el verificador histórico, que define `phi_shape_derivative`.
6. `verify_b2_path2_gate_certificate.py` — el verificador de la compuerta, cuyo `run()` se llama
   sin cambios.
7. `B2_path2_gate_certificate.md` — la nota de la compuerta, ya auditada y promocionada.

## 1. Qué se afirma

En el punto congelado y en la carta de B3, la componente `(x2, x3)` del producto
`dphi ∧ drho` es `>= +0.0077379 > 0`. Junto con el rango 3 de la carta y `drho ≠ 0`, eso da
`B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY`.

## 2. Lo que no se reabre

La cadena de la compuerta: H1–H5, la monotonía del `sup`, la calibración y Cauchy–Schwarz
integral, la capa escalar de B1.5 y sus kernels. Aquí se audita **el uso** de esa maquinaria
para B3 y las piezas nuevas: `dphi`, la cota burda de `|drho_2|` y la lógica del producto.

## 3. Lo que se te pide

Responde los cinco puntos de §5 de la nota. Para cada hallazgo, da una clasificación
(`SE_SOSTIENE`, `MENOR`, `REQUIERE_CORRECCIÓN` o `INVALIDA`) y la condición mínima de
concesión. Añade además:

6. **Algo que la nota no pregunta.** Busca cualquier pieza que pueda hacer que `W23 > 0` sea
   cierto en el código y falso en la matemática.

**Veredictos posibles:** `AUDIT_PASS`, `AUDIT_PASS_CONDITIONAL_<COND>`,
`AUDIT_REQUIRES_MINOR_FIX`, `AUDIT_FAIL`.

### Adjunto: B3_certificate.md
```
# B3 — certificado: `n=2` no recupera `phi` localmente en el punto congelado

> **STATUS: `FROZEN / PENDING_INDEPENDENT_AUDIT`.** Se congela y se sube **antes** de
> auditarlo. No se promociona hasta que lo revise otra familia de modelos. Guardarraíles de B3
> intactos: punto congelado, carta congelada, sin búsqueda de curvas, puntos ni parámetros.

**Fecha:** 2026-10-12 · **Verificador:** `verify_b3_certificate.py` →
`verification_b3_certificate.json` · **Especificación:**
`research_program/puente_3p1/2026-09-12/B3_transverse_n2_audit.md` · **Exploración previa:**
`dev/explore_b3_new_representation.py`.

Las cifras abreviadas están redondeadas hacia afuera: las cotas inferiores, hacia abajo; las
superiores, hacia arriba.

```text
M = 128
dphi/dx2            ∈ [0.4571239, 0.4572009]
dphi/dx3            ∈ [−0.0002180, −0.0001548]
drho/dx3            >= +0.0183232        (S_lo(e3) >= +0.0035566)
|drho/dx2|          <= 2.9271            (cota burda: H <= Z)
W23 = dphi_2 drho_3 − dphi_3 drho_2  >=  +0.0077379  > 0
carta: det(dv1, du_out, du_in / dx) = −10133099161583616/8106479329266893 ≠ 0  → rango 3
fastmath_guard: 19 kernels, IR ejecutado (caché vacía), sin flags, mutante detectado, ok
TERMINAL = B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY   (pendiente de auditoría)
```

Con `M = 64` el resultado es el mismo, con menos margen: `drho/dx3 >= +0.0121942` y
`W23 >= +0.0048460`.

---

## 1. Qué establece y qué no

En el punto congelado `lambda*`, el binary64 `path(0.5)` (convención H5 de la compuerta), y en
la carta cociente por el gauge `x = (v1/v0, u_in/u_out, u_in·v1)` con `v0` fijo, **`dphi` no es
paralelo a `drho`**: la componente `(x2, x3)` del producto `dphi ∧ drho` es estrictamente
positiva. Como la carta tiene rango 3 y `drho ≠ 0` (porque `drho/dx3 > 0`), existe una dirección
física `v` con `drho(v) = 0` y `dphi(v) ≠ 0`. Por tanto, **la ley `n=2`, una única escalar
`rho`, no puede reconstruir `phi` localmente en la familia física tridimensional.** Es el
terminal negativo de la especificación de B3, que justifica **proponer** el paso a `n=3`, no
autorizarlo.

**No** establece:
- nada fuera de `lambda*`;
- nada sobre `n=3`;
- ninguna afirmación global. Tampoco dice que `rho` no contenga información sobre `phi`: B2.1 muestra
  que `rho` sí distingue los puntos de la curva congelada. Lo que falla es recuperar `phi` en
  las direcciones transversales.

Respecto al 2026-10-11, B3 pasa de `INCONCLUSIVE_BY_BOUNDS` a este terminal. Es la misma
conclusión que el terminal histórico de 2026-09-12, pero ahora con soporte: el histórico se
retiró porque se apoyaba en un error de signo.

## 2. Cadena

**Por qué basta la componente `(x2, x3)`.** `dphi ≈ (−9e-5, 0.457, −2e-4)` es casi paralelo a
`e2`, de modo que `W23 ≈ 0.457 · drho_3`. Basta certificar `drho_3 > 0` con margen y acotar el
resto.

1. **`drho/dx3`.** La dirección `e3 = dlambda/dx3 = (0, 0, u_out/x3, 1/v1)` mueve solo las dos
   caras `U`, ambas con `v_n > 0`. Es exactamente el caso del certificado de la compuerta, que
   solo construye `S_lo`. Se llama al `run()` auditado de la compuerta **sin modificarlo**, con
   su tabla de velocidades `VN_FR` fijada a los racionales exactos de `e3`. Las caras `V` tienen
   velocidad exactamente 0: `frac_iv(0)` da `(−ε, +ε)` con `ε` subnormal, una contribución
   válida y despreciable. Resultado: `drho_3 >= S_lo(e3)/Z_hi²`.
2. **`dphi`.** `phi = Z_in/(Z_in + Z_out)`, con `Z_in` y `Z_out` las partes de `K` con `U > 0` y
   `U < 0`. Por tanto `dphi = (Z_out dZ_in − Z_in dZ_out)/(Z_in + Z_out)²`. Los `dZ` son
   integrales de `G` sobre las caras que se mueven; la cara `U = 0` no se mueve. `Z_in` y
   `Z_out` salen de `cell_weights` y las integrales de cara de `segment_weights`, ambos de la
   compuerta, y todo se combina en `mpmath.iv`.
3. **`|drho/dx2|`, cota burda.** `e2` solo mueve la cara `U = −u_out`, con `v = −u_out/x2`. Como
   `H <= Z`, se tiene `|S(e2)| <= 2|v| J (Z_hi + B_hi/Z_lo)`, y por tanto `|drho_2| <= 2.9271`.
   Basta porque va multiplicada por `|dphi_3| <= 0.000218`.
4. **`W23 >= dphi_2^lo · drho_3^lo − |dphi_3|^hi · |drho_2|^hi`**, con todos los factores
   positivos en su sentido.
5. **Carta.** El jacobiano es exacto en racionales desde los binary64 de `lambda*`, con las
   filas `(v1, u_out, u_in)`. Su determinante `≠ 0` da rango 3.

## 3. Hipótesis

Las de la compuerta, sin cambios:
- H1, con `V_ε`;
- H2;
- H3, que es teorema en cualquier rectángulo y para cualquier campo de velocidades de caras;
- H4;
- H5, la convención del punto;
- `B15_DEPENDENCIES`.

La definición de `phi` es la de B3 (`verify_b3_transverse_n2.py`, `phi_shape_derivative`).

## 4. Controles

- **`dphi`.** Las envolventes certificadas contienen los valores flotantes de B3
  (`−9.4276e-05`, `0.457162`, `−1.8642e-04`).
- **`Z` y `B_hi`.** Coinciden bit a bit con los de la compuerta, porque no dependen de la
  dirección.
- **Exploración en flotante** (`dev/explore_b3_new_representation.py`, `M = 64`): daba
  `drho/dx3 ∈ [0.0132, 0.0444]`. La cota certificada con `M = 64`, `0.0121942`, queda por debajo,
  como debe.
- **Control de fast-math.** Es el de B2.1: IR de las sobrecargas ejecutadas, caché privada
  vacía y `cache_hits == 0`, aplicado a los 19 kernels de la compuerta, que aquí sí se ejecutan
  todos.

## 5. Qué debe mirar la auditoría

1. Que llamar a `gate.run()` con `VN_FR` sustituido sea legítimo: que `run` solo use `VN_FR`
   para las velocidades y que el caso `v_n = 0` (rama superior con `vn_lo = −ε`) sea válido.
2. La fórmula de `dphi` y los signos de cada término de cara, en particular que la cara `U = 0`
   no se mueve.
3. La cota burda de `|S(e2)|`, en concreto que `I_f <= J_f · Z_hi` porque `H <= Z`.
4. La lógica B3: que una componente del producto distinta de cero, junto con rango 3 y
   `drho ≠ 0`, implique la existencia de `v` con `drho(v) = 0` y `dphi(v) ≠ 0`.
5. El jacobiano de la carta, y que la convención H5 (punto binary64) sea la de la especificación
   de B3.
```

### Adjunto: verify_b3_certificate.py
```
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
import re  # noqa: E402
from fractions import Fraction as Fr  # noqa: E402

import numpy as np  # noqa: E402
from mpmath import iv  # noqa: E402
from numba import njit  # noqa: E402

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
    gate._compile_helpers()
    flags, chars = {}, {}
    uncompiled = [fn.py_func.__name__ for fn in gate.KERNELS if not fn.signatures]
    for fn in gate.KERNELS:
        irs = b21.executed_ir(fn)
        flags[fn.py_func.__name__] = sorted({m.group(0) for ir in irs for m in gate._FAST.finditer(ir)})
        chars[fn.py_func.__name__] = sum(len(i) for i in irs)

    @njit(fastmath=True)
    def _mutant(a, b, c):
        return a * b + c
    _mutant(1.0, 2.0, 3.0)
    mutant = bool(gate._FAST.search("".join(b21.executed_ir(_mutant))))
    clean = all(not v for v in flags.values())
    return {"kernels_checked": len(flags), "inspection": "executed overloads, private empty cache",
            "min_ir_chars": min(chars.values()), "kernels_without_compiled_signature": uncompiled,
            "flags_found": {k: v for k, v in flags.items() if v}, "all_clean": clean,
            "mutation_fastmath_detected": mutant, "ok": bool(clean and mutant and not uncompiled)}


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
    W23_lo = d2.a * drho3_lo.a - max(abs(d3.a), abs(d3.b)) * drho2_abs.b
    W23_lo = iv.mpf(W23_lo).a
    wedge_nonzero = bool(d2.a > 0 and drho3_lo.a > 0 and W23_lo > 0)
    guard = guard_all_gate_kernels()
    terminal = ("B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY"
                if (wedge_nonzero and chart_rank3 and guard["ok"]) else "B3_INCONCLUSIVE_BY_BOUNDS")
    f = lambda x: [float(x.a), float(x.b)]  # noqa: E731
    out = {
        "unit": "PUENTE-3P1/B3_CERTIFICATE", "M": M,
        "frozen_lambda_binary64": [float(x) for x in gate.LAM],
        "chart_x": [str(x) for x in X], "chart_jacobian_columns": [[str(v) for v in c] for c in cols],
        "chart_det_rows_v1_uout_uin": str(det), "chart_rank_three": chart_rank3,
        "drho_dx3": {"S_lo_e3": r3["S_lo"], "Z": r3["Z"], "B_hi": r3["B_hi"],
                     "Bprime_lo_e3": r3["Bprime_lo"], "lower_bound": float(drho3_lo.a)},
        "drho_dx2_abs_upper": float(drho2_abs.b),
        "phi_pieces": {k: f(v) for k, v in pc.items()},
        "dphi_dx": [f(x) for x in dphis],
        "wedge_x2x3_lower_bound": float(W23_lo),
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
```

### Adjunto: verification_b3_certificate.json
```
{
  "unit": "PUENTE-3P1/B3_CERTIFICATE",
  "M": 128,
  "frozen_lambda_binary64": [
    0.35,
    0.9,
    1.5,
    0.7,
    0.1
  ],
  "chart_x": [
    "8106479329266893/3152519739159347",
    "3152519739159347/6755399441055744",
    "25555836100601103743381618598871/40564819207303340847894502572032"
  ],
  "chart_jacobian_columns": [
    [
      "0",
      "3152519739159347/9007199254740992",
      "-9457559217478041/16212958658533786",
      "-9938380705789317246726257466409/36508337286573007663824977788928"
    ],
    [
      "0",
      "0",
      "-10133099161583616/3152519739159347",
      "0"
    ],
    [
      "0",
      "0",
      "60847228810955011271841753858048/25555836100601103743381618598871",
      "9007199254740992/8106479329266893"
    ]
  ],
  "chart_det_rows_v1_uout_uin": "-10133099161583616/8106479329266893",
  "chart_rank_three": true,
  "drho_dx3": {
    "S_lo_e3": 0.0035566169202515,
    "Z": [
      0.4405407017748797,
      0.44057200155799914
    ],
    "B_hi": 0.004203439539650638,
    "Bprime_lo_e3": 0.016656259402041157,
    "lower_bound": 0.018323283533122254
  },
  "drho_dx2_abs_upper": 2.927099935487002,
  "phi_pieces": {
    "Z_in": [
      0.14060974862899192,
      0.1406155109432403
    ],
    "Z_out": [
      0.29993685068542414,
      0.299950621762525
    ],
    "J_uin": [
      0.1971015597072508,
      0.19711354905943865
    ],
    "J_uout": [
      0.19631624930250563,
      0.19632385353923282
    ],
    "J_v1_in": [
      0.25327762676204474,
      0.25329397086776434
    ],
    "J_v1_out": [
      0.5408276317482059,
      0.54085467728044
    ],
    "J_v0_in": [
      0.25709052250100234,
      0.25709196207503443
    ],
    "J_v0_out": [
      0.5493592460664208,
      0.5493662646588399
    ]
  },
  "dphi_dx": [
    [
      -0.00010861124690337548,
      -7.994461832225411e-05
    ],
    [
      0.4571239125441492,
      0.45720089409969633
    ],
    [
      -0.00021798837350369034,
      -0.00015485165745401006
    ]
  ],
  "wedge_x2x3_lower_bound": 0.007737937305297059,
  "dphi_wedge_drho_certified_nonzero": true,
  "fastmath_guard": {
    "kernels_checked": 19,
    "inspection": "executed overloads, private empty cache",
    "min_ir_chars": 8801,
    "kernels_without_compiled_signature": [],
    "flags_found": {},
    "all_clean": true,
    "mutation_fastmath_detected": true,
    "ok": true
  },
  "no_new_path": true,
  "no_new_point": true,
  "no_search": true,
  "no_seeds": true,
  "no_monte_carlo": true,
  "terminal": "B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY"
}
```

### Adjunto: B3_transverse_n2_audit.md
```
# B3 — Auditoría transversal de identificabilidad a `n=2`

> **CORRECCIÓN 2026-10-11 — terminal sin soporte.** Importaba el `evaluate` erróneo de B2.2 y combinaba los extremos del producto cruzado sin aritmética de intervalos. Corregido, ninguna derivada de `rho` ni componente del wedge excluye cero: `B3_INCONCLUSIVE_BY_BOUNDS`. La conclusión «`n=2` no reconstruye localmente `phi`» queda sin soporte (ni establecida ni refutada); las cifras de abajo son históricas. Ver `dev/B2_2_SIGN_BUG_2026-10-11.md`.

> **STATUS: `FROZEN_POINT / GAUGE_QUOTIENTED_CHART / DIRECT_SHAPE_DERIVATIVES`.**
> No se buscan curvas, puntos testigo ni nuevos parámetros.

## Punto y coordenadas físicas

Se usa exactamente el punto `lambda(t0)` de B2, con `t0=0.5`:

```text
lambda* = (0.35, 0.9, 1.5, 0.7, 0.1)
x* = (I1,I2,I3) = (v1/v0, u_in/u_out, u_in*v1)
   = (2.5714285714, 0.4666666667, 0.63).
```

El chart local fija el gauge `v0=0.35` y reconstruye

```text
v1 = v0*x1,  u_in = x3/v1,  u_out = u_in/x2.
```

## Cálculo

Se calculan `dphi` y `drho` en las tres direcciones `x1,x2,x3` mediante derivadas de forma
directas. Para `rho` se usa la fórmula de términos de borde de B2.2, propagando las cotas
angulares de B1.2; no se usan diferencias finitas. Para `phi` se usa la derivada de borde de sus
integrales interior/exterior.

La condición necesaria para que `phi` sea localmente recuperable de la única escalar `rho` es

```text
ker(d rho) subset ker(d phi),  equivalent to  dphi parallel drho.
```

## Terminales

```text
B3_POSITIVE_N2_COMPATIBLE       dphi || drho (necesario, no suficiente)
B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY
                                dphi wedge drho != 0 in the physical chart
B3_INCONCLUSIVE_BY_BOUNDS        las envolventes no deciden la proporcionalidad
```

Un terminal negativo justifica pasar a la ley `n=3`; ninguno de los terminales es una afirmación
de reconstrucción global.

## Resultado en el punto congelado

La evaluación directa da

```text
dphi/dx = (-9.4276e-05, 4.5716e-01, -1.8642e-04)
```

Dos componentes del producto cruzado excluyen cero, pero la componente `(x1,x3)` conserva una
envolvente estrecha que todavía contiene cero:

```text
cross(x1,x2) in [ 8.3573e-04,  7.3400e-03]
cross(x1,x3) in [-4.3322e-07,  1.2257e-06]
cross(x2,x3) in [-1.2413e-02, -7.5961e-03]

CHART_RANK = 3
D_RHO_NONZERO = CERTIFIED
D_PHI_WEDGE_D_RHO = CERTIFIED_NONZERO
TERMINAL = B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY
```

Ya que basta una sola componente del wedge separada de cero, las componentes `(x1,x2)` y
`(x2,x3)` certifican `dphi wedge drho != 0`; no es necesario resolver la componente `(x1,x3)`.
Como el chart tiene rango 3 y `drho != 0`, existe una dirección física `v` con
`drho(v)=0` y `dphi(v)!=0`. Por tanto `n=2` no puede reconstruir localmente `phi` en toda la
familia física tridimensional. Esto justifica proponer el paso a `n=3`, pero no lo autoriza.

**Artefacto:** `verification_b3_transverse_n2.json`.

> **Actualización 2026-10-12.** Con la maquinaria certificada de la compuerta, B3 es
> `B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY`: la componente `(x2, x3)` del producto
> `dphi ∧ drho` es `>= +0.0077379`. El resultado está congelado y pendiente de auditoría. Ver
> `research_program/puente_3p1/2026-10-12/B3_certificate.md`.
```

### Adjunto: verify_b3_transverse_n2.py
```
"""PUENTE-3P1 / B3 — transverse n=2 audit at frozen B2 point."""
import json
import sys
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import lambertw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from verify_b2_2_shape_derivative import evaluate  # noqa: E402

LSTAR = np.array((0.35, 0.9, 1.5, 0.7, 0.1))
XSTAR = np.array((LSTAR[1] / LSTAR[0], LSTAR[3] / LSTAR[2], LSTAR[3] * LSTAR[1]))


def jacobian_chart():
    x1, x2, x3 = XSTAR
    v0, v1, uout, uin, _ = LSTAR
    return np.array([[0.0, 0.0, 0.0], [v0, 0.0, 0.0],
                     [-uout / x1, -uout / x2, uout / x3],
                     [-uin / x1, 0.0, 1.0 / v1], [0.0, 0.0, 0.0]])


def phi_shape_derivative(lam, velocity):
    v0, v1, uout, uin, _ = lam
    dv0, dv1, duout, duin, _ = velocity
    s = lambda uv: (1.0 + lambertw(-uv / np.e, 0).real)
    fin = quad(lambda V: (1.0 - s(uin * V) ** 3) / V, v0, v1,
               epsabs=1e-12, epsrel=1e-12)[0] / 3.0
    fout = quad(lambda V: (s(-uout * V) ** 3 - 1.0) / V, v0, v1,
                epsabs=1e-12, epsrel=1e-12)[0] / 3.0
    gin = lambda U, V: s(U * V) * np.exp(-s(U * V))
    din = duin * quad(lambda V: gin(uin, V), v0, v1)[0]
    dout = duout * quad(lambda V: gin(-uout, V), v0, v1)[0]
    din += dv1 * quad(lambda U: gin(U, v1), 0.0, uin)[0]
    din -= dv0 * quad(lambda U: gin(U, v0), 0.0, uin)[0]
    dout += dv1 * quad(lambda U: gin(U, v1), -uout, 0.0)[0]
    dout -= dv0 * quad(lambda U: gin(U, v0), -uout, 0.0)[0]
    p = fin / (fin + fout)
    return ((1.0 - p) * din - p * dout) / (fin + fout)


def main():
    J = jacobian_chart()
    dphi = np.array([phi_shape_derivative(LSTAR, J[:, j]) for j in range(3)])
    drho_orders = []
    for order in (10, 14):
        drho_orders.append(np.array([evaluate(LSTAR, order, J[:, j])[0:2]
                                     for j in range(3)]))
    margin = np.max(np.abs(drho_orders[1] - drho_orders[0]))
    drho_interval = np.column_stack((drho_orders[1][:, 0] - margin,
                                     drho_orders[1][:, 1] + margin))
    cross_intervals = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        # drho_i and drho_j vary independently: enclose each product separately
        # and add the intervals, rather than pairing lower with lower endpoints.
        term_j = [dphi[i] * drho_interval[j, k] for k in (0, 1)]
        term_i = [-dphi[j] * drho_interval[i, k] for k in (0, 1)]
        cross_intervals.append([min(term_j) + min(term_i), max(term_j) + max(term_i)])
    # One certified nonzero wedge component is sufficient for non-proportionality.
    wedge_nonzero = any(a > 0 or b < 0 for a, b in cross_intervals)
    chart_rank_three = np.linalg.matrix_rank(J[1:4, :]) == 3
    drho_nonzero = any(a > 0 or b < 0 for a, b in drho_interval)
    out = {"unit": "PUENTE-3P1/B3", "frozen_lambda": LSTAR.tolist(),
           "gauge_quotiented_coordinates": XSTAR.tolist(), "dphi_dx": dphi.tolist(),
           "drho_dx_enclosures": drho_interval.tolist(),
           "cross_product_enclosures": cross_intervals,
           "chart_rank_three": bool(chart_rank_three),
           "drho_nonzero": bool(drho_nonzero),
           "dphi_wedge_drho_certified_nonzero": bool(wedge_nonzero),
           "no_new_path": True, "no_new_point": True, "no_search": True,
           "no_seeds": True, "no_monte_carlo": True,
           "terminal": ("B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY"
                        if wedge_nonzero and chart_rank_three and drho_nonzero
                        else "B3_INCONCLUSIVE_BY_BOUNDS")}
    print(json.dumps(out, indent=2))
    with open(HERE / "verification_b3_transverse_n2.json", "w") as fh:
        json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
```

### Adjunto: verify_b2_path2_gate_certificate.py
```
"""PUENTE-3P1 / B2 path 2 -- directed-rounding lower bound of S at the frozen t0.

Rule (dev/B2_PROMOTION_RULE_AMENDMENT_2026-10-11.md, signed by the PI):

    B2_CORRECTED_POSITIVE  iff  0 not in formal_enclosure(drho_dt),

with drho_dt = S / Z^2 and S = B' - 2 (Z'/Z) B.  The expected sign is positive,
so this file builds only a certified LOWER bound S_lo; S_lo > 0 gives the
one-sided enclosure [S_lo/Z_hi^2, +inf) of drho_dt, which excludes zero.

Representation (dev/B2_NEW_REPRESENTATION_2026-10-11.md).  Delta_max(x,y) is the
time separation of the 2D Lorentzian metric F(w) dU dV, F = q^2, w = UV.
  * Reverse triangle inequality: for x in cell P and y in cell Q,
        P_top <= Q_bot  =>  Delta(x,y) >= Delta(P_top, Q_bot),
        P_bot <= Q_top  =>  Delta(x,y) <= Delta(P_bot, Q_top),
    so every cell pair is bounded by ONE pair of lattice corners.
  * Lower corner bound: straight-line budget sqrt(dU dV) int_0^1 q(w(tau)) dtau,
    a lower Riemann sum of q over the interval range of w on each tau-cell.
  * Upper corner bound: min of
      - Cauchy-Schwarz  sqrt(dU int q(U_b V)^2 dV)          (B1.2 section 3), and
      - calibration     c (nu_b - nu_a) + Phi_c(w_b) - Phi_c(w_a),  nu = ln V,
        Phi_c' = F / (2 (c + sqrt(c^2 + F w))), for every c valid on the causal
        rectangle (c^2 + F w >= 0 there, and c + sqrt(...) > 0).
    Each c gives a valid bound on its own, so the c grid needs no certification.
  * h = p(Delta) with p(b) = (1 - cos min(b, pi))/2, nondecreasing on [0, inf).

Which bound goes where (only S_lo is built):
  B'_lo = sum over faces of 2 v_n int_face w H,  H(x) = int_K w(y) h(x,y) dy;
          LOWER H on U=-u_out, U=u_in, V=v0 (v_n > 0), UPPER H on V=v1 (v_n < 0).
  B_hi  = 2 sum_{P,Q} W_P W_Q p(UB(P_bot, Q_top)).
  S_lo  = B'_lo - (2 Z'_hi / Z_lo) B_hi.

Arithmetic, following B1.5 section 5bis:
  * every binary64 operation is pushed one ulp outward (np.nextafter, also inside
    numba kernels); sums are directed sequential or directed prefix sums;
  * transcendental functions enter ONLY through certified monotone tables built
    with B1.5's audited scalar layer (s_encl / q_encl / G_encl, mpmath.iv, no
    Lambert W).  A lookup is rigorous by monotonicity alone: q increasing in w,
    G increasing for w <= 0 and decreasing for w >= 0 (0 is a table node), p
    nondecreasing.  Table indices are located by exact float comparisons;
  * ln V at the lattice nodes and the face velocities are enclosed exactly
    (mpmath.iv / fractions.Fraction);
  * the numba kernels are checked for fast-math / contraction flags in their
    LLVM IR, and that check is itself mutation-tested.

Frozen point convention (declared, as in B1.5): the certified point is the
binary64 lambda* = path(0.5) that the frozen B2 scripts evaluate, and the
direction is d = L1 - L0 taken exactly from the binary64 L0, L1.  The quantity is
the directional derivative of rho at lambda* along d.

Determinism: no seeds, no Monte Carlo, no search over lambda, t0 or points.
Usage: .venv/bin/python research_program/puente_3p1/2026-10-11/verify_b2_path2_gate_certificate.py [M]
"""
import json
import math
import re
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
from numba import njit, prange
from mpmath import iv

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "2026-09-12" / "B1"))
import verify_b1_5_analytic_separation as b15  # noqa: E402

INF = math.inf

# --- frozen inputs -----------------------------------------------------------
L0 = np.array((0.5, 1.0, 1.0, 0.5, 0.1))
L1 = np.array((0.2, 0.8, 2.0, 0.9, 0.1))
T0 = 0.5
LAM = (1.0 - T0) * L0 + T0 * L1          # binary64, exactly as the frozen scripts
V0, V1, UOUT, UIN = (float(x) for x in LAM[:4])
DFR = [Fraction(float(b)) - Fraction(float(a)) for a, b in zip(L0, L1)]
# outward normal velocities (dev/B2_2_SIGN_BUG_2026-10-11.md)
VN_FR = {"U=-u_out": DFR[2], "U=u_in": DFR[3], "V=v0": -DFR[0], "V=v1": DFR[1]}

# --- proof parameters (any values give a valid bound; larger = tighter) -------
M_DEFAULT = 128      # lattice cells per side
R_SUB = 8            # sub-cells per lattice cell for weights and CS integrals
N_TAU = 64           # tau-cells for the line budget
NT_HALF = 2 ** 15    # w-table nodes on each side of w = 0
NP = 2 ** 17         # p-table nodes on [0, P_MAX]
P_MAX = 3.2
C_POS = np.geomspace(1e-3, 50.0, 260)
C_NEG = -np.geomspace(1e-3, 50.0, 120)


def up(x):
    return np.nextafter(x, INF)


def dn(x):
    return np.nextafter(x, -INF)


def frac_iv(fr):
    return float(dn(float(fr))), float(up(float(fr)))


# ---------------------------------------------------------------------------
# 1. Certified monotone tables.
# ---------------------------------------------------------------------------
def w_table():
    wlo = float(dn(-UOUT * V1)) - 1e-3
    whi = float(up(UIN * V1)) + 1e-3
    left = np.linspace(wlo, 0.0, NT_HALF + 1)
    right = np.linspace(0.0, whi, NT_HALF + 1)[1:]
    wt = np.concatenate([left, right])
    assert np.all(np.diff(wt) > 0) and wt[NT_HALF] == 0.0
    return wt


def certified_tables(wt):
    qlo = np.empty_like(wt); qhi = np.empty_like(wt)
    glo = np.empty_like(wt); ghi = np.empty_like(wt)
    for k, w in enumerate(wt):
        qlo[k], qhi[k] = b15.q_encl(float(w))
        glo[k], ghi[k] = b15.G_encl(float(w))
    Flo = dn(qlo * qlo)
    Fhi = up(qhi * qhi)
    return qlo, qhi, glo, ghi, Flo, Fhi


def p_table():
    bt = np.linspace(0.0, P_MAX, NP + 1)
    plo = np.empty_like(bt); phi = np.empty_like(bt)
    pi_iv = iv.pi
    for k, b in enumerate(bt):
        B = iv.mpf(float(b))
        if B.a >= pi_iv.b:                 # certified b >= pi: p = 1
            plo[k] = phi[k] = 1.0
            continue
        if B.b <= pi_iv.a:                 # certified b <= pi
            val = (iv.mpf(1) - iv.cos(B)) / 2
            plo[k], phi[k] = b15.iv_lo(val), min(1.0, b15.iv_hi(val))
        else:                              # b within rounding of pi
            val = (iv.mpf(1) - iv.cos(iv.mpf([pi_iv.a, float(b)]))) / 2
            plo[k], phi[k] = b15.iv_lo(val), 1.0
    return bt, plo, phi


def nu_enclosures(Vg):
    lo = np.empty_like(Vg); hi = np.empty_like(Vg)
    for j, v in enumerate(Vg):
        x = iv.log(iv.mpf(float(v)))
        lo[j], hi[j] = b15.iv_lo(x), b15.iv_hi(x)
    return lo, hi


# ---------------------------------------------------------------------------
# 2. Numba kernels.  Directed rounding by np.nextafter after every operation.
# ---------------------------------------------------------------------------
@njit(cache=True)
def _up(x):
    return np.nextafter(x, np.inf)


@njit(cache=True)
def _dn(x):
    return np.nextafter(x, -np.inf)


@njit(cache=True)
def k_below(t, x):
    """Largest k with t[k] <= x (t increasing); -1 if none."""
    lo, hi = 0, t.size - 1
    if x < t[0]:
        return -1
    if x >= t[hi]:
        return hi
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if t[mid] <= x:
            lo = mid
        else:
            hi = mid
    return lo


@njit(cache=True)
def k_above(t, x):
    """Smallest k with t[k] >= x; t.size if none."""
    lo, hi = 0, t.size - 1
    if x <= t[0]:
        return 0
    if x > t[hi]:
        return t.size
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if t[mid] >= x:
            hi = mid
        else:
            lo = mid
    return hi


@njit(cache=True)
def p_lo_of(b, bt, plo):
    if b <= 0.0:
        return 0.0
    k = k_below(bt, b)
    return plo[k]


@njit(cache=True)
def p_hi_of(b, bt, phi):
    if b <= 0.0:
        return 0.0
    k = k_above(bt, b)
    if k >= bt.size:
        return 1.0
    return phi[k]


@njit(cache=True)
def phi_cell_bounds(c, wt, Flo, Fhi):
    """Per table cell [w_k, w_k+1]: certified (phi_lo, phi_hi) or invalid."""
    n = wt.size - 1
    plo = np.zeros(n); phi = np.zeros(n); ok = np.zeros(n, np.bool_)
    cc_lo, cc_hi = _dn(c * c), _up(c * c)
    for k in range(n):
        f_lo, f_hi = Flo[k], Fhi[k + 1]          # F increasing in w
        a, b = wt[k], wt[k + 1]
        # X = F w over the cell, interval product (F > 0)
        x1, x2, x3, x4 = _dn(f_lo * a), _dn(f_lo * b), _dn(f_hi * a), _dn(f_hi * b)
        X_lo = min(min(x1, x2), min(x3, x4))
        y1, y2, y3, y4 = _up(f_lo * a), _up(f_lo * b), _up(f_hi * a), _up(f_hi * b)
        X_hi = max(max(y1, y2), max(y3, y4))
        if c > 0.0:
            disc_lo = _dn(cc_lo + X_lo)
            if disc_lo < 0.0:
                continue
            den_lo = _dn(c + _dn(math.sqrt(disc_lo)))
            den_hi = _up(c + _up(math.sqrt(_up(cc_hi + X_hi))))
        else:
            # c + sqrt(c^2 + X) = X / (sqrt(c^2 + X) - c), no cancellation for c < 0
            if X_lo <= 0.0:
                continue
            den_lo = _dn(X_lo / _up(_up(math.sqrt(_up(cc_hi + X_lo))) - c))
            den_hi = _up(X_hi / _dn(_dn(math.sqrt(_dn(cc_lo + X_hi))) - c))
            if den_lo <= 0.0:
                continue
        plo[k] = _dn(f_lo / _up(2.0 * den_hi))
        phi[k] = _up(f_hi / _dn(2.0 * den_lo))
        ok[k] = True
    return plo, phi, ok


@njit(cache=True)
def phi_prefix(c, wt, Flo, Fhi):
    """Directed prefix sums of the upper and lower cell integrals of Phi_c',
    from the first node k0 of the valid run that reaches the top of the table.
    Returns k0, PU_lo, PU_hi, PL_lo, PL_hi (NaN below k0)."""
    plo, phi, ok = phi_cell_bounds(c, wt, Flo, Fhi)
    n = wt.size
    k0 = n - 1
    while k0 > 0 and ok[k0 - 1]:
        k0 -= 1
    PU_lo = np.full(n, np.nan); PU_hi = np.full(n, np.nan)
    PL_lo = np.full(n, np.nan); PL_hi = np.full(n, np.nan)
    PU_lo[k0] = PU_hi[k0] = PL_lo[k0] = PL_hi[k0] = 0.0
    for k in range(k0, n - 1):
        h_lo, h_hi = _dn(wt[k + 1] - wt[k]), _up(wt[k + 1] - wt[k])
        tu_lo, tu_hi = _dn(phi[k] * h_hi), _up(phi[k] * h_hi)
        tl_lo, tl_hi = _dn(plo[k] * h_lo), _up(plo[k] * h_lo)
        # the upper cell term is phi_hi*h_hi; rounding both ways bounds its prefix
        PU_lo[k + 1] = _dn(PU_lo[k] + tu_lo)
        PU_hi[k + 1] = _up(PU_hi[k] + tu_hi)
        PL_lo[k + 1] = _dn(PL_lo[k] + tl_lo)
        PL_hi[k + 1] = _up(PL_hi[k] + tl_hi)
    return k0, PU_lo, PU_hi, PL_lo, PL_hi


@njit(parallel=True, cache=True)
def calibration_point_tables(cs, wt, Flo, Fhi, wlo_pt, whi_pt, nulo_pt, nuhi_pt):
    """Separable per-point pieces of the calibration bound, for every c:
       case wb_hi >= wa_lo : UB_c <= AU_hi[b,c] - AU_lo[a,c]
       case wb_hi <  wa_lo : UB_c <= AL_hi[b,c] - AL_lo[a,c]
    plus thr[c] = w of the first valid node."""
    nc, npt = cs.size, wlo_pt.size
    AU_lo = np.full((npt, nc), np.nan); AU_hi = np.full((npt, nc), np.nan)
    AL_lo = np.full((npt, nc), np.nan); AL_hi = np.full((npt, nc), np.nan)
    thr = np.empty(nc)
    for j in prange(nc):
        c = cs[j]
        k0, PU_lo, PU_hi, PL_lo, PL_hi = phi_prefix(c, wt, Flo, Fhi)
        thr[j] = wt[k0]
        for i in range(npt):
            kb = k_below(wt, wlo_pt[i])       # point used as the past end a
            ka = k_above(wt, whi_pt[i])       # point used as the future end b
            if kb < k0 or ka >= wt.size:
                continue
            if c > 0.0:
                cnu_lo, cnu_hi = _dn(c * nulo_pt[i]), _up(c * nuhi_pt[i])
            else:
                cnu_lo, cnu_hi = _dn(c * nuhi_pt[i]), _up(c * nulo_pt[i])
            AU_lo[i, j] = _dn(cnu_lo + PU_lo[kb]); AU_hi[i, j] = _up(cnu_hi + PU_hi[ka])
            AL_lo[i, j] = _dn(cnu_lo + PL_lo[kb]); AL_hi[i, j] = _up(cnu_hi + PL_hi[ka])
    return AU_lo, AU_hi, AL_lo, AL_hi, thr


@njit(parallel=True, cache=True)
def ub_table(M, Ug, Vg, wlo_pt, whi_pt, AU_lo, AU_hi, AL_lo, AL_hi, thr,
             Pcs_lo, Pcs_hi, bt, phi_p):
    """p_hi(UB(a,b)) for every lattice pair a <= b (strict in both); 0 otherwise."""
    n1 = M + 1
    npt = n1 * n1
    out = np.zeros((npt, npt))
    nc = thr.size
    for a in prange(npt):
        ia, ja = a // n1, a % n1
        for ib in range(ia + 1, n1):
            du_hi = _up(Ug[ib] - Ug[ia])
            for jb in range(ja + 1, n1):
                b = ib * n1 + jb
                # Cauchy-Schwarz with U_b fixed, prefix sums along V
                I_hi = _up(Pcs_hi[ib, jb] - Pcs_lo[ib, ja])
                best = _up(math.sqrt(_up(du_hi * I_hi)))
                # rectangle w-range from its four lattice corners
                c2, c3 = ia * n1 + jb, ib * n1 + ja
                rwlo = min(min(wlo_pt[a], wlo_pt[b]), min(wlo_pt[c2], wlo_pt[c3]))
                case_up = whi_pt[b] >= wlo_pt[a]
                cmin = np.inf
                for j in range(nc):
                    if thr[j] > rwlo:
                        continue
                    # plain differences; one outward step on the minimum suffices,
                    # since up() is monotone: min_j up(d_j) = up(min_j d_j)
                    if case_up:
                        v = AU_hi[b, j] - AU_lo[a, j]
                    else:
                        v = AL_hi[b, j] - AL_lo[a, j]
                    if v < cmin:
                        cmin = v
                if cmin < np.inf:
                    cmin = _up(cmin)
                    if cmin < best:
                        best = cmin
                out[a, b] = p_hi_of(best, bt, phi_p)
    return out


@njit(parallel=True, cache=True)
def lb_rows(src, forward, Ug, Vg, M, wt, qlo, bt, plo_p, ntau):
    """p_lo(LB) for pairs (s, x): s in src (lattice ids), x over all lattice
    points; forward: s is the past end; else s is the future end."""
    n1 = M + 1
    npt = n1 * n1
    out = np.zeros((src.size, npt))
    inv = 1.0 / ntau                       # exact: ntau is a power of two
    for r in prange(src.size):
        s = src[r]
        for x in range(npt):
            if forward:
                a, b = s, x
            else:
                a, b = x, s
            ia, ja, ib, jb = a // n1, a % n1, b // n1, b % n1
            if not (Ug[ib] > Ug[ia] and Vg[jb] > Vg[ja]):
                continue
            Ua, Va = Ug[ia], Vg[ja]
            du_lo, du_hi = _dn(Ug[ib] - Ua), _up(Ug[ib] - Ua)
            dv_lo, dv_hi = _dn(Vg[jb] - Va), _up(Vg[jb] - Va)
            acc = 0.0
            for k in range(ntau):
                t0, t1 = k * inv, (k + 1) * inv
                U_lo = _dn(Ua + _dn(du_lo * t0))
                U_hi = _up(Ua + _up(du_hi * t1))
                V_lo = _dn(Va + _dn(dv_lo * t0))
                V_hi = _up(Va + _up(dv_hi * t1))
                # w = U V with V > 0: the minimum is at V_lo if U_lo >= 0, else V_hi
                w_lo = _dn(U_lo * V_lo) if U_lo >= 0.0 else _dn(U_lo * V_hi)
                kq = k_below(wt, w_lo)
                if kq >= 0:                    # below the table: q > 0 is the bound
                    acc = _dn(acc + qlo[kq])
            line = _dn(_dn(math.sqrt(_dn(du_lo * dv_lo))) * _dn(acc * inv))
            out[r, x] = p_lo_of(line, bt, plo_p)
    return out


@njit(parallel=True, cache=True)
def b_hi_sum(M, W_hi, pub):
    """2 sum_{P,Q} W_P W_Q p_hi(UB(P_bot, Q_top)), directed upward."""
    n1 = M + 1
    nc = M * M
    part = np.zeros(nc)
    for P in prange(nc):
        iP, jP = P // M, P % M
        bot = iP * n1 + jP
        acc = 0.0
        for Q in range(nc):
            iQ, jQ = Q // M, Q % M
            top = (iQ + 1) * n1 + (jQ + 1)
            v = pub[bot, top]
            if v > 0.0:
                acc = _up(acc + _up(W_hi[Q] * v))
        part[P] = _up(W_hi[P] * acc)
    tot = 0.0
    for P in range(nc):
        tot = _up(tot + part[P])
    return _up(2.0 * tot)


@njit(cache=True)
def face_h(M, s0, s1, W, vals_fwd, vals_bwd, use_top_bot_lower):
    """H on each face segment from per-(segment endpoint, lattice point) tables.

    use_top_bot_lower (lower bound): fwd uses (s1 -> Q_bot), bwd (Q_top -> s0).
    otherwise (upper bound):         fwd uses (s0 -> Q_top), bwd (Q_bot -> s1).
    vals_fwd[r, x] / vals_bwd[r, x] are indexed by the segment endpoint row r.
    Sums are rounded down for the lower bound and up for the upper bound."""
    n1 = M + 1
    nseg = s0.size
    H = np.zeros(nseg)
    for i in range(nseg):
        acc = 0.0
        for Q in range(M * M):
            iQ, jQ = Q // M, Q % M
            bot = iQ * n1 + jQ
            top = (iQ + 1) * n1 + (jQ + 1)
            if use_top_bot_lower:
                v = vals_fwd[i + 1, bot] + vals_bwd[i, top]     # both >= 0
                acc = _dn(acc + _dn(W[Q] * _dn(v)))
            else:
                v = vals_fwd[i, top] + vals_bwd[i + 1, bot]
                acc = _up(acc + _up(W[Q] * _up(v)))
        H[i] = acc
    return H


# ---------------------------------------------------------------------------
# 3. Weights by sub-cell envelopes of G (unimodal, peak 1/e at w = 0).
# ---------------------------------------------------------------------------
@njit(cache=True)
def tiling(a, b, r):
    """r+1 increasing nodes with the endpoints EXACTLY a and b, so sub-cells
    tile the cell with no gap or overlap (numba's linspace does not promise it)."""
    xs = np.linspace(a, b, r + 1)
    xs[0] = a
    xs[r] = b
    for k in range(r):
        if not xs[k] < xs[k + 1]:
            raise ValueError("non-increasing tiling")
    return xs


@njit(cache=True)
def g_range(wl, wh, wt, glo, ghi, e_inv_hi):
    """Certified (lo, hi) of G over [wl, wh]; 0 is a node of wt."""
    if wh <= 0.0:
        lo = glo[k_below(wt, wl)]
        hi = ghi[k_above(wt, wh)]
    elif wl >= 0.0:
        lo = glo[k_above(wt, wh)]
        hi = ghi[k_below(wt, wl)]
    else:
        lo = min(glo[k_below(wt, wl)], glo[k_above(wt, wh)])
        hi = e_inv_hi
    return lo, hi


@njit(cache=True)
def rect_w(u0, u1, v0, v1):
    a, b, c, d = u0 * v0, u0 * v1, u1 * v0, u1 * v1
    lo = min(min(_dn(a), _dn(b)), min(_dn(c), _dn(d)))
    hi = max(max(_up(a), _up(b)), max(_up(c), _up(d)))
    return lo, hi


@njit(cache=True)
def cell_weights(Ug, Vg, r, wt, glo, ghi, e_inv_hi):
    M = Ug.size - 1
    W_lo = np.zeros(M * M); W_hi = np.zeros(M * M)
    for i in range(M):
        us = tiling(Ug[i], Ug[i + 1], r)
        for j in range(M):
            vs = tiling(Vg[j], Vg[j + 1], r)
            alo = 0.0; ahi = 0.0
            for a in range(r):
                for b in range(r):
                    wl, wh = rect_w(us[a], us[a + 1], vs[b], vs[b + 1])
                    gl, gh = g_range(wl, wh, wt, glo, ghi, e_inv_hi)
                    ar_lo = _dn(_dn(us[a + 1] - us[a]) * _dn(vs[b + 1] - vs[b]))
                    ar_hi = _up(_up(us[a + 1] - us[a]) * _up(vs[b + 1] - vs[b]))
                    alo = _dn(alo + _dn(ar_lo * gl))
                    ahi = _up(ahi + _up(ar_hi * gh))
            W_lo[i * M + j] = alo; W_hi[i * M + j] = ahi
    return W_lo, W_hi


@njit(cache=True)
def segment_weights(fixed, grid, r, wt, glo, ghi, e_inv_hi):
    n = grid.size - 1
    lo = np.zeros(n); hi = np.zeros(n)
    for i in range(n):
        xs = tiling(grid[i], grid[i + 1], r)
        alo = 0.0; ahi = 0.0
        for a in range(r):
            w1, w2 = fixed * xs[a], fixed * xs[a + 1]
            wl = min(_dn(w1), _dn(w2)); wh = max(_up(w1), _up(w2))
            gl, gh = g_range(wl, wh, wt, glo, ghi, e_inv_hi)
            alo = _dn(alo + _dn(_dn(xs[a + 1] - xs[a]) * gl))
            ahi = _up(ahi + _up(_up(xs[a + 1] - xs[a]) * gh))
        lo[i] = alo; hi[i] = ahi
    return lo, hi


@njit(cache=True)
def cs_prefix(Ug, Vg, r, wt, Fhi):
    """Directed prefix sums along V of upper bounds of int F(U_i V) dV per cell."""
    n1 = Ug.size
    P_lo = np.zeros((n1, n1)); P_hi = np.zeros((n1, n1))
    for i in range(n1):
        u = Ug[i]
        for j in range(n1 - 1):
            vs = tiling(Vg[j], Vg[j + 1], r)
            cell = 0.0
            for a in range(r):
                # w = u V monotone in V: the max is at the upper end iff u >= 0
                wmax = _up(u * vs[a + 1]) if u >= 0.0 else _up(u * vs[a])
                cell = _up(cell + _up(_up(vs[a + 1] - vs[a]) * Fhi[k_above(wt, wmax)]))
            P_lo[i, j + 1] = _dn(P_lo[i, j] + cell)
            P_hi[i, j + 1] = _up(P_hi[i, j] + cell)
    return P_lo, P_hi


# ---------------------------------------------------------------------------
# 4. Guard: no fast-math or contraction in any compiled kernel.
# ---------------------------------------------------------------------------
_FAST = re.compile(r"\b(fast|contract|reassoc|afn|arcp|nnan|ninf|nsz)\b|llvm\.fma|fmuladd")
KERNELS = (tiling, phi_cell_bounds, phi_prefix, calibration_point_tables, ub_table, lb_rows,
           b_hi_sum, face_h, g_range, rect_w, cell_weights, segment_weights, cs_prefix,
           k_below, k_above, p_lo_of, p_hi_of, _up, _dn)


def fastmath_flags(fn):
    found = set()
    for sig in fn.signatures:
        found |= {m.group(0) for m in _FAST.finditer(fn.inspect_llvm(sig))}
    return sorted(found)


def _compile_helpers():
    """Helpers called only from other kernels register no signature of their
    own; compile each once from Python with the argument types the kernels use,
    so the guard inspects real IR rather than passing vacuously."""
    t = np.linspace(-1.0, 1.0, 9)
    tiling(0.0, 1.0, 4); phi_cell_bounds(1.0, t, t + 2.0, t + 3.0)
    phi_prefix(1.0, t, t + 2.0, t + 3.0); g_range(-0.5, 0.5, t, t, t, 1.0)
    rect_w(0.0, 1.0, 0.5, 1.0); k_below(t, 0.1); k_above(t, 0.1)
    p_lo_of(0.1, t, t); p_hi_of(0.1, t, t); _up(1.0); _dn(1.0)


def fastmath_guard():
    _compile_helpers()
    flags = {fn.py_func.__name__: fastmath_flags(fn) for fn in KERNELS}
    uncompiled = [fn.py_func.__name__ for fn in KERNELS if not fn.signatures]

    @njit(fastmath=True)
    def _mutant(a, b, c):
        return a * b + c
    _mutant(1.0, 2.0, 3.0)
    mutant_caught = bool(fastmath_flags(_mutant))
    clean = all(not v for v in flags.values())
    return {"kernels_checked": len(flags), "kernels_without_compiled_signature": uncompiled,
            "flags_found": {k: v for k, v in flags.items() if v},
            "all_clean": clean, "mutation_fastmath_detected": mutant_caught,
            "ok": bool(clean and mutant_caught and not uncompiled)}


# ---------------------------------------------------------------------------
# 5. Assembly.
# ---------------------------------------------------------------------------
def run(M):
    t_start = time.time()
    Ug = np.linspace(-UOUT, UIN, M + 1)
    Vg = np.linspace(V0, V1, M + 1)
    assert Ug[0] == -UOUT and Ug[-1] == UIN and Vg[0] == V0 and Vg[-1] == V1
    assert np.all(np.diff(Ug) > 0) and np.all(np.diff(Vg) > 0) and Vg[0] > 0
    n1 = M + 1

    wt = w_table()
    qlo, qhi, glo, ghi, Flo, Fhi = certified_tables(wt)
    bt, plo_p, phi_p = p_table()
    e_inv_hi = b15.E_INV_HI
    nulo, nuhi = nu_enclosures(Vg)
    t_tables = time.time()

    # lattice points: id = i*(M+1) + j, (U_i, V_j)
    iu, jv = np.divmod(np.arange(n1 * n1), n1)
    PU, PV = Ug[iu], Vg[jv]
    wlo_pt, whi_pt = dn(PU * PV), up(PU * PV)
    nulo_pt, nuhi_pt = nulo[jv], nuhi[jv]

    cs = np.concatenate([C_POS, C_NEG])
    AU_lo, AU_hi, AL_lo, AL_hi, thr = calibration_point_tables(
        cs, wt, Flo, Fhi, wlo_pt, whi_pt, nulo_pt, nuhi_pt)
    Pcs_lo, Pcs_hi = cs_prefix(Ug, Vg, R_SUB, wt, Fhi)
    pub = ub_table(M, Ug, Vg, wlo_pt, whi_pt, AU_lo, AU_hi, AL_lo, AL_hi, thr,
                   Pcs_lo, Pcs_hi, bt, phi_p)
    del AU_lo, AU_hi, AL_lo, AL_hi
    t_ub = time.time()

    W_lo, W_hi = cell_weights(Ug, Vg, R_SUB, wt, glo, ghi, e_inv_hi)
    Z_lo, Z_hi = b15.sum_dn(W_lo), b15.sum_up(W_hi)
    B_hi = b_hi_sum(M, W_hi, pub)

    faces = {"U=-u_out": ("U", 0, -UOUT), "U=u_in": ("U", M, UIN),
             "V=v0": ("V", 0, V0), "V=v1": ("V", M, V1)}
    Bp_terms, Zp_lo_terms, Zp_hi_terms, face_out = [], [], [], {}
    for name, (axis, idx, fixed) in faces.items():
        if axis == "U":
            pts = idx * n1 + np.arange(n1)                  # (U fixed, V_j)
            fw_lo, fw_hi = segment_weights(fixed, Vg, R_SUB, wt, glo, ghi, e_inv_hi)
        else:
            pts = np.arange(n1) * n1 + idx                  # (U_i, V fixed)
            fw_lo, fw_hi = segment_weights(fixed, Ug, R_SUB, wt, glo, ghi, e_inv_hi)
        vn_lo, vn_hi = frac_iv(VN_FR[name])
        s0, s1 = pts[:-1], pts[1:]
        if vn_lo > 0:
            fwd = lb_rows(pts, True, Ug, Vg, M, wt, qlo, bt, plo_p, N_TAU)
            bwd = lb_rows(pts, False, Ug, Vg, M, wt, qlo, bt, plo_p, N_TAU)
            H = face_h(M, s0, s1, W_lo, fwd, bwd, True)
            inner = b15.sum_dn(dn(fw_lo * H))
            term = float(dn(2.0 * dn(vn_lo * inner)))
            Zp_lo_terms.append(float(dn(vn_lo * b15.sum_dn(fw_lo))))
            Zp_hi_terms.append(float(up(vn_hi * b15.sum_up(fw_hi))))
        else:
            fwd = pub[pts, :]                               # (s -> Q_top), s past end
            bwd = pub[:, pts].T                             # (Q_bot -> s), s future end
            H = face_h(M, s0, s1, W_hi, fwd, bwd, False)
            inner = b15.sum_up(up(fw_hi * H))
            term = float(dn(2.0 * dn(vn_lo * inner)))     # vn < 0: lower = vn_lo * hi
            Zp_lo_terms.append(float(dn(vn_lo * b15.sum_up(fw_hi))))
            Zp_hi_terms.append(float(up(vn_hi * b15.sum_dn(fw_lo))))
        Bp_terms.append(term)
        face_out[name] = {"v_n": [vn_lo, vn_hi], "Bprime_contribution_lower": term}
    Bp_lo = b15.sum_dn(Bp_terms)
    Zp_lo, Zp_hi = b15.sum_dn(Zp_lo_terms), b15.sum_up(Zp_hi_terms)
    assert Zp_lo > 0
    k_hi = float(up(2.0 * up(Zp_hi / Z_lo)))
    S_lo = float(dn(Bp_lo - up(k_hi * B_hi)))
    drho_lo = float(dn(S_lo / up(Z_hi * Z_hi))) if S_lo > 0 else float(dn(S_lo / dn(Z_lo * Z_lo)))
    return {
        "M": M, "R_sub": R_SUB, "N_tau": N_TAU, "w_table_nodes": int(wt.size),
        "p_table_nodes": int(bt.size), "c_values": int(cs.size),
        "Z": [Z_lo, Z_hi], "Zprime": [Zp_lo, Zp_hi], "two_Zp_over_Z_hi": k_hi,
        "B_hi": B_hi, "Bprime_lo": Bp_lo, "faces": face_out,
        "S_lo": S_lo, "drho_dt_lower_bound": drho_lo,
        "seconds": {"tables": round(t_tables - t_start, 1), "ub_table": round(t_ub - t_tables, 1),
                    "total": round(time.time() - t_start, 1)},
    }


def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else M_DEFAULT
    res = run(M)
    guard = fastmath_guard()
    positive = bool(res["S_lo"] > 0 and guard["ok"])
    out = {
        "unit": "PUENTE-3P1/B2_PATH2_GATE_CERTIFICATE",
        "rule": "B2_CORRECTED_POSITIVE iff 0 not in formal_enclosure(drho_dt) "
                "(amendment signed 2026-10-11)",
        "frozen_point": {"lambda_star_binary64": [float(x) for x in LAM],
                         "direction_exact": [str(f) for f in DFR], "t0": T0},
        "representation": "time separation of q(UV)^2 dU dV; corners by reverse triangle "
                          "inequality; lower = straight line; upper = min(Cauchy-Schwarz, "
                          "HJ calibration)",
        "arithmetic": {
            "mode": "outward_directed_rounding_end_to_end",
            "operations": "np.nextafter one ulp outward after each binary64 op, also in numba",
            "transcendentals": "certified monotone tables from B1.5 scalar layer "
                               "(s_encl/q_encl/G_encl, mpmath.iv dps 25); p and ln V by mpmath.iv",
            "lambert_w_used": False,
            "fastmath_guard": guard,
        },
        **res,
        "enclosure_of_drho_dt": [res["drho_dt_lower_bound"], "+inf"],
        "no_new_path": True, "no_new_t0": True, "no_new_points": True,
        "no_search": True, "no_adjustment": True, "no_seeds": True, "no_monte_carlo": True,
        "terminal": "B2_CORRECTED_POSITIVE" if positive else "B2_GATE_NOT_CERTIFIED_AT_THIS_RESOLUTION",
    }
    print(json.dumps(out, indent=2))
    if len(sys.argv) <= 1:
        with open(HERE / "verification_b2_path2_gate_certificate.json", "w") as fh:
            json.dump(out, fh, indent=2)


if __name__ == "__main__":
    main()
```

### Adjunto: B2_path2_gate_certificate.md
```
# B2 — certificado de la compuerta en `t0`: `drho/dt > 0` con redondeo dirigido

> **STATUS: `B2_GATE = CERTIFIED_POSITIVE_AT_T0`** (`AUDIT_PASS_CONDITIONAL_B15_DEPENDENCIES`,
> condición verificada; promocionado por el PI el 2026-10-12, §9). `B2.1` y `B3` siguen en
> `INCONCLUSIVE_BY_BOUNDS`. El objeto se congeló y se subió **antes** de auditarlo, como B1.5
> (§11 de su nota). Lo auditó el sanedrín del 2026-10-11 (cinco casas de cinco familias de
> modelos), que no encontró ningún fallo en el número. La revisión del 2026-10-12 solo corrige
> el texto según su veredicto; el verificador y el JSON son
> los de `7909c0e`.
> Guardarraíles de B2 intactos: `no_new_path`, `no_new_t0`, `no_new_points`, `no_search`,
> `no_adjustment`. La enmienda sigue vigente: excluir cero en `t0` **no** emite un terminal de
> B2.1.

**Fecha:** 2026-10-11 (texto corregido el 2026-10-12 a partir de `beaf6af`) · **Verificador:**
`verify_b2_path2_gate_certificate.py` → `verification_b2_path2_gate_certificate.json` ·
**Regla:** `dev/B2_PROMOTION_RULE_AMENDMENT_2026-10-11.md` (firmada por el PI).

```text
S_lo = +0.0013679385529351228          (S = B' − 2 (Z'/Z) B, en lambda(0.5))
drho/dt(t0) >= +0.007047462946767621    enclosure [0.00704746, +inf), excluye cero
TERMINAL = B2_CORRECTED_POSITIVE        (auditado con pase condicional; promocionado, §9)
```

---

## 1. Qué establece y qué no

Establece, bajo las hipótesis de §6, que la derivada direccional de `rho` es **estrictamente
positiva** en el punto binary64 congelado `lambda*_binary64 = path(0.5)` (H5), a lo largo de la
dirección exacta `d = L1 − L0`.

Como H3 es un teorema y la derivada que da es continua en el parámetro (§6, H3), de ahí se
sigue lo siguiente. En la recta `γ(s) = lambda*_binary64 + s·d`, `rho∘γ` es **estrictamente
creciente en algún intervalo de `s = 0` cuyo radio no está cuantificado**. Es, por tanto,
inyectiva en ese intervalo. Esta es la identificabilidad local que da el certificado, y no da
más.

**No** establece:

- **un radio.** El intervalo existe, pero el certificado no dice lo grande que es. Por eso no
  dice nada de la malla `{0.45, …, 0.55}` de B2.1, que sigue en `INCONCLUSIVE_BY_BOUNDS`. Para
  B2.1 haría falta otro certificado, por ejemplo una cota inferior de `rho'` en un intervalo dado.
- **el signo en el punto medio real de la curva.** `lambda*_binary64` y el punto medio real
  `(L0 + L1)/2` pueden diferir en menos de un ulp por componente. Con un radio sin cuantificar
  no se puede afirmar que el segundo caiga dentro del intervalo; hace falta un paso de
  transferencia, que está sin hacer;
- identificabilidad global, ni de `phi` fuera de esta recta, ni `n=3`;
- nada sobre B3, que sigue inconcluso tras `dev/B2_2_SIGN_BUG_2026-10-11.md`.

## 2. Cadena

1. **Representación** (`dev/B2_NEW_REPRESENTATION_2026-10-11.md`). `Delta_max` (B1.2 §2) es,
   antes del tope `min(pi, ·)`, la separación temporal `τ` de la métrica 2D `q(UV)² dU dV`. La
   justificación, incluida la regularización `V_ε`, está en H1 (§6).
2. **Monotonía respecto a los extremos.** Para `τ` sin tope, si `z` está en el futuro causal de
   `x`, la concatenación da `τ(x,y) >= τ(x,z) + τ(z,y) >= τ(z,y)`. Con `x ∈ P` e `y ∈ Q`:
   `τ(P_top, Q_bot) <= τ(x,y)` si `P_top <= Q_bot`, y `τ(x,y) <= τ(P_bot, Q_top)`. El tope
   `min(pi, ·)` y `p` son no decrecientes, así que ambas desigualdades pasan a `Delta_max` y a
   `h`. **No** se usa ninguna desigualdad triangular inversa aditiva para la cantidad con tope,
   que en general sería falsa. Cada par de celdas se acota con **un** par de esquinas de la
   retícula.
3. **Cota inferior entre esquinas.** El presupuesto de la recta (B1.2 LB, hipótesis H1b de B1.5),
   como suma de Riemann inferior de `q` sobre el rango intervalar de `w(tau)` en cada celda de `tau`.
4. **Cota superior entre esquinas.** `min(Cauchy–Schwarz integral, inf_c calibración)`.
   - **Cauchy–Schwarz integral: lema nuevo de la auditoría** (CIRO, ronda 2). **No** es la UB de
     B1.2, que es `q_max sqrt(dU dV)`, ni la H1a de B1.5. Para una curva admisible `U(V)` entre
     `a` y `b`:
     `L[U] = ∫ q(U(V)V) sqrt(U'(V)) dV <= sqrt(dU ∫ q(U(V)V)² dV) <= sqrt(dU ∫ q(U_b V)² dV)`.
     La primera desigualdad es Cauchy–Schwarz con `∫ U' dV = dU`. La segunda usa `U(V) <= U_b`,
     `V > 0` y que `q` es positiva y creciente en `w`; la monotonía de `q` ya estaba auditada.
   - La calibración es `W_c = c ln V + Phi_c(UV)`, con `Phi_c' = F/(2(c + sqrt(c² + F w)))`. Con
     `s = sqrt(c² + F w)` se cumplen exactamente `Phi_c' w + c = (s + c)/2` y
     `4 Phi_c'(Phi_c' w + c) = F`. Por AM-GM, `dW_c >= dtau` a lo largo de toda curva causal
     futura, siempre que `c` sea válido en el rectángulo causal: `c² + F w >= 0` y `s + c > 0`.
     Con `c < 0` lo segundo equivale a `F w > 0`, de modo que el cruce de `w = 0` exige `c > 0`.
     La auditoría lo comprobó (N3).
   - **Cada `c` da una cota válida por separado**, así que la rejilla de `c` no se certifica.
   - **La resta `AU`/`AL`** (ABNER, ronda 1, y CIRO, ronda 2). Para un `c` fijo, la cota es
     `c(ν_b − ν_a) + ∫_{w_a}^{w_b} Phi_c'`. `phi_prefix` acumula, desde el nodo `k0`, dos sumas
     exactas sobre las celdas de la tabla. `ΣU` suma los términos superiores `phi_hi[k]·h_hi[k]`,
     y `ΣL` los inferiores `plo[k]·h_lo[k]`, todos `>= 0`. Cada suma se encierra por ambos
     lados con prefijos dirigidos: `PU_lo[k] <= ΣU[k0..k) <= PU_hi[k]`, y lo mismo con `PL`.
     - Si `w_b >= w_a`, con `kb = k_below(w_a,lo)` y `ka = k_above(w_b,hi)`, se tiene
       `[w_a, w_b] ⊆ [wt[kb], wt[ka]]`. Por tanto
       `∫ Phi_c' <= ΣU[kb..ka) = ΣU[k0..ka) − ΣU[k0..kb) <= PU_hi[ka] − PU_lo[kb]`.
       El prefijo común `ΣU[k0..kb)` se cancela en las sumas exactas, y cada extremo se acota en
       la dirección favorable. Por eso `AU_lo[a]` **no** necesita ser una cota inferior de
       `A_c(a)`, y no lo es.
     - Si `w_b < w_a`, la integral es negativa y `[wt[ka], wt[kb]] ⊆ [w_b, w_a]`. Por tanto
       `∫_{w_a}^{w_b} Phi_c' <= −ΣL[ka..kb) <= PL_hi[ka] − PL_lo[kb]`. Si `ka > kb`, el último
       término es `>= 0` y la cota sigue siendo válida.
     - Los términos `c ν` se acotan por separado (`cnu_lo`, `cnu_hi`), con el orden de `nulo` y
       `nuhi` invertido cuando `c < 0`.
5. **Ensamblado** (solo `S_lo`). `B'_lo` usa la cota inferior de `H` en las caras con `v_n > 0` y
   la superior en `V=v1`; `B_hi = 2 sum W_P W_Q p(UB)`;
   `S_lo = B'_lo − (2 Z'_hi/Z_lo) B_hi`. Velocidades normales con la normal exterior
   (`dev/B2_2_SIGN_BUG_2026-10-11.md`): `+1.0, +0.4, +0.3, −0.2`, comprobadas por la auditoría
   (N4). En `face_h`, la cota se justifica **por orientación**. Cada sumando acota el núcleo de
   su propia orientación, y su suma es el núcleo simétrico. En `V=v1` el sumando futuro es
   exactamente cero, porque ninguna `Q_top` tiene `V > v1`, y la orientación pasada la cubre
   `pub[Q_bot, s1]`. No se trata de «dos cotas del mismo `p`». El factor 2 de `b_hi_sum` cuenta
   dos veces la diagonal `P = Q`, lo que es conservador.

## 3. Aritmética

| objeto | tratamiento |
|---|---|
| operaciones binary64 (también dentro de numba) | `np.nextafter` un ulp hacia afuera tras cada operación |
| `q`, `G` | tablas certificadas de 65 537 nodos (con `w=0` como nodo) construidas con la capa escalar **auditada** de B1.5 (`s_encl`/`q_encl`/`G_encl`, `mpmath.iv`, sin Lambert W); cada consulta es rigurosa solo por monotonía (`q` creciente; `G` creciente en `w<=0` y decreciente en `w>=0`). Nodos efectivos `wt[0] = -1.3510000000000002`, `wt[-1] = 0.6310000000000001`. El margen `1e-3` de `w_table` no lleva redondeo dirigido y no lo necesita, porque `fl(a − e) <= a` y `fl(a + e) >= a` para `e > 0` |
| `p(b) = (1−cos min(b,pi))/2` | tabla certificada de 131 073 nodos en `[0, 3.2]`, `mpmath.iv` (`iv.cos`, `iv.pi`, **fuera** de la capa auditada de B1.5: H4); `p` no decreciente |
| `ln V` en los nodos | `mpmath.iv` (`iv.log`, **fuera** de la capa auditada de B1.5: H4) |
| velocidades `v_n` | racionales exactos (`Fraction`) de los binary64 de `lambda0`, `lambda1` |
| `Phi_c` | integrandos acotados por celda de tabla (`c<0` sin cancelación); sumas prefijas dirigidas por ambos lados (§2.4) |
| pesos `W_P`, caras, `Z`, `Z'` | subceldas `8×8` / `8` con envolventes de `G`; teselado con extremos exactos; `E_INV_HI = iv_hi(iv.exp(-1)) >= 1/e` acota el pico de `G` |
| sumas | fuera de numba (`Z`, `Z'`, `inner` de cada cara, las cuatro contribuciones de `B'`): **árbol por parejas dirigido de B1.5** (`b15.sum_dn`/`b15.sum_up`), con un `nextafter` hacia afuera en cada suma; dentro de los kernels (`b_hi_sum`, `face_h`): acumulación secuencial con `_up`/`_dn` en cada suma, en variables privadas de cada iteración de `prange` |
| índices de tabla | comparaciones exactas de binary64 |
| compilación | se comprueba que el IR de LLVM de los 19 kernels no tiene `fast`/`contract`/`reassoc`/`fma`; el control está probado por mutación (un kernel `fastmath` es detectado) y exige que cada kernel tenga firma compilada (la primera versión pasaba en vacío por 11 kernels auxiliares: corregido). Las sumas de B1.5 son Python y numpy fuera de numba, y por eso no entran en este control: su garantía es semántica (§8) |

*Nota sobre el verificador.* La cabecera de `verify_b2_path2_gate_certificate.py` conserva dos
etiquetas que esta revisión corrige: «Cauchy–Schwarz (B1.2 section 3)» y «directed sequential».
El script no se edita para no alterar el objeto auditado en `7909c0e`. Donde no coincidan,
prevalece esta nota.

## 4. Resultado y auditoría de refinamiento

| `M` | `B_hi` | `B'_lo` | `S_lo` | terminal |
|---|---|---|---|---|
| 16 | — | — | −0.005184 | no certifica |
| 32 | 0.004858 | 0.006516 | −0.001387 | no certifica |
| 48 | 0.004558 | 0.007259 | −0.000156 | no certifica |
| 64 | 0.004414 | 0.007638 | **+0.000458** | positivo |
| 96 | 0.004273 | 0.008015 | **+0.001064** | positivo |
| **128** | **0.004203** | **0.008205** | **+0.001368** | **positivo (reportado)** |

En `M = 128`: `Z ∈ [0.4405407, 0.4405720]`, `Z' ∈ [0.3582566, 0.3582912]`,
`2Z'/Z <= 1.6265975`. Contribuciones inferiores a `B'`:

```text
U=-u_out  +0.0037812    U=u_in  +0.0027552    V=v0  +0.0061629    V=v1  −0.0044941
```

`B_hi` decrece y `B'_lo` crece con `M`, sin reversión. Toda `M` da una cota válida; la
separación de cero empieza en `M = 64`. Tiempo: 19 s (14 s las tablas), 2.6 GB. El refinamiento
monótono es **consistencia interna**, no una prueba de certificación (sanedrín, pérdidas comunes).

## 5. Controles

- **Coherencia por pares** (`M = 32`, 3088 pares de la retícula). Las cotas certificadas
  `p_lo`/`p_hi` se comparan con la banda flotante independiente de
  `dev/explore_b2_calibration_band.py` (geodésica por disparo y calibración):
  0 pares con `p_lo` certificado por encima de la superior flotante; 0 con `p_hi` por debajo de la
  geodésica; 0 con `p_lo > p_hi`.
- **Contra el prototipo flotante** (`dev/explore_b2_path2_prototype.py`) a la misma `M`: la capa
  certificada pierde `~1.2e-4` en `S` (`M = 128`: `+0.001368` frente a `+0.001499`) y queda en el
  lado correcto en cada pieza (`B_hi` mayor, `B'_lo` menor).
- **`Z`, `Z'`** contienen los valores de cuadratura (`0.440556`, `0.358274`).
- El límite `M → ∞` del prototipo (`+0.002411`) coincide con el intervalo ideal medido por otra
  vía (`+0.002419`).

## 6. Hipótesis

- **H1. Representación.** B1.2 §2 da `Delta_max = min(pi, sup L[U])`, con el `sup` tomado sobre
  las curvas monótonas `U(V)` absolutamente continuas. Ese `sup` sin tope **es** la separación
  temporal `τ` de `q² dU dV`, porque el `sup` sobre gráficas `U(V)` coincide con el `sup` sobre
  todas las curvas causales futuras (`dU >= 0`, `dV >= 0`). El argumento es la **regularización
  `V_ε`** (ASTRA, ronda 1):
  - Sea una curva causal entre extremos con `ΔV > 0`, parametrizada por `U + V` y reescalada a
    `s ∈ [0, 1]`; sus coordenadas son Lipschitz.
  - Se cambia `V(s)` por `V_ε(s) = (1−ε) V(s) + ε (V_a + ΔV·s)` y se mantiene `U(s)`. La curva
    nueva tiene los mismos extremos, sigue siendo monótona y no sale del rectángulo. Además
    `V_ε' >= ε ΔV`, así que `U` es función absolutamente continua de `V_ε` y la curva es
    admisible en B1.2.
  - Cuando `ε → 0`, la longitud converge a la original: `q(U V_ε)` converge uniformemente en un
    compacto con `UV < 1`, y `sqrt(U' V_ε')` converge casi por doquier con una cota integrable.
  - Si `ΔV = 0`, la longitud es cero (convención degenerada de B1.2 §3).

  Este argumento cubre los **enlaces horizontales** de la cara `V=v0`. `face_h` acota cada
  punto `x` de esa cara mediante `s1` en el sentido futuro y mediante `s0` en el pasado. Ambos
  enlaces tienen `ΔV = 0` y ninguno se puede parametrizar por `V`. En las caras `U = const` los
  enlaces son verticales y admisibles con `U' = 0`. **No se usa ningún argumento de «medida
  nula»**: el que se propuso en la auditoría fallaba en toda la cara `V=v0` y está retirado.
  De H1 salen la cota de la recta (H1b), la monotonía de §2.2 y la calibración. La cota de
  Cauchy–Schwarz integral es un lema aparte (§2.4).
- **H2.** `rho = B/Z²`, con `B = ∫∫_{K×K} w w h` y `h(x,y) = p(Delta_max)` simétrica, extendida
  por cero a los pares incomparables (B1.5 §2).
- **H3. Transporte de Reynolds: teorema.** `B' = 2∫_{∂K} w v_n H`. El integrando
  `w(x) w(y) h(x,y)` no depende de `t` (`G_encl` y `q_encl` solo reciben `w`); toda la
  dependencia en `t` está en `K(t)`, un rectángulo de caras afines en `t`. Si `h` es continua
  en `K × K`, basta Leibniz iterado. La continuidad la da el **módulo de continuidad de ASTRA**
  (ronda 1):
  - Para `ΔU, ΔV > 0`, todas las curvas de B1.2 se escriben con una misma clase de funciones
    `f` absolutamente continuas y crecientes, con `f(0) = 0` y `f(1) = 1`:
    `L_θ[f] = sqrt(ΔU ΔV) ∫_0^1 q((U_a + ΔU f(s))(V_a + ΔV s)) sqrt(f'(s)) ds`.
  - Como `∫ sqrt(f') <= 1`, la continuidad uniforme de `q` da un módulo de continuidad respecto
    a los extremos **independiente de `f`**, y tomar el `sup` lo conserva.
  - En los extremos degenerados basta la cota `q_max sqrt(ΔU ΔV) → 0`.
  - La extensión por cero a los pares incomparables también es continua.

  La misma continuidad hace que la derivada sea continua en `t` (y en `s` a lo largo de `γ`),
  que es lo que usa §1. El contraste numérico anterior (`dev/B2_GATE_RESULT_2026-10-11.md` §3,
  0.2 %) queda como control.
- **H4. Hipótesis de entorno.** Aritmética IEEE-754 binary64 correctamente redondeada en todas
  las operaciones. **Todas** las evaluaciones de `mpmath.iv` del verificador devuelven
  envolventes correctas: `exp` (en `E_INV_HI`), `cos` y `pi` (en `p_table`) y `log` (en
  `nu_enclosures`), además de las que hace internamente la capa escalar de B1.5. Y la
  compilación se hace sin `fast-math` ni contracción, lo que se comprueba en el IR (§3). La
  auditoría de B1.5 cubre `s_encl`/`q_encl`/`G_encl` y la conversión `iv_lo`/`iv_hi`. **No**
  cubre `iv.cos`, `iv.log` ni `iv.pi`, que se asumen aquí como hipótesis de entorno y no se
  atribuyen a B1.5.
- **H5. Convención del punto.** El punto certificado es el binary64 `lambda* = path(0.5)` que
  evalúan los scripts congelados de B2, y la dirección es `d = L1 − L0` exacta. Es la misma
  convención implícita de B1.5, que certificó los binary64 de `lambda1`. Por eso el objeto de §1
  es la recta `γ` que pasa por ese punto, no la curva afín real en su parámetro `t0`.
- **`λ5` congelada.** La quinta componente de `lambda` es `epsilon_s = 0.1`
  (`B1/B1_3_frozen_pair_and_rho.md:22-23`), igual en `L0`, `L1` y `lambda*`, así que `d5 = 0`.
  Es una componente **congelada que no se mueve**. Solo entra como condición de admisibilidad
  `u_in v1 <= 1 − epsilon_s = 0.9`. En `lambda*`, `u_in v1 = 0.7·0.9 = 0.63`, lo que cuadra con
  el nodo superior `wt[-1] = 0.631`, que incluye el margen. `q_encl` y `G_encl` solo reciben `w`,
  y B1.5 certificó ambos extremos con `λ5 = 0.1` y la misma interfaz. La auditoría retiró `λ5`
  como condición en la ronda 3, y aquí se declara para que no vuelva a quedar implícita.

## 7. Qué se pidió a la auditoría

Esta lista es la de la versión congelada (`7909c0e`) y se conserva tal cual. Las respuestas
están en §8.

1. La calibración: la desigualdad AM-GM, la elección de la raíz menor, la validez en el
   rectángulo y el tratamiento de `c < 0`.
2. La desigualdad triangular inversa para `Delta_max` con el tope `min(pi, ·)`: el tope conserva
   la cota superior y la inferior porque `p` es no decreciente y vale 1 a partir de `pi`.
3. Qué cota va a cada término de `S_lo`, y los signos de `v_n`.
4. Los índices de tabla y las direcciones de redondeo de `ub_table`, `lb_rows`, `face_h` y
   `phi_prefix`.
5. H3 y H5.

## 8. Auditoría

**Sanedrín del 2026-10-11** (`revisiones/2026-10-11-auditoria-certificado-b2/`, commit
`beaf6af`; objeto auditado: este directorio en `7909c0e`). Participaron cinco casas: CLAUDE
OPUS, ASTRA (`gpt-6-astra`), CIRO (`grok-4.6`), ABNER (`deepseek-v4-pro`) y GEMINI
(`gemini-3.8-flash`, la variante flash, más débil que la pro que supone el diseño). Hubo tres
rondas más residuo y veredicto, sin ningún turno fallido.

```text
AUDIT_PASS_CONDITIONAL_B15_DEPENDENCIES   (unánime; leído como implicación, no como validez)
```

La cadena analítica se sostiene en cinco puntos:

- **N1**, con la regularización `V_ε` (H1);
- **N2**, por monotonía del `sup` respecto a los extremos (§2.2);
- **N3**, porque la calibración es exacta y la rama `c<0` es correcta;
- **N4**, porque los signos de `v_n` son correctos en `B'` y en `Z'`;
- **H3**, que pasa a ser teorema.

En el código visible, el factor 2 de la diagonal es conservador, el margen de `w_table`
conserva la cobertura y no hay reducciones paralelas sobre variables exteriores.

**La condición** son tres hechos sobre dependencias de B1.5 que las casas no podían ver. Se
comprobaron fuera del sanedrín el mismo 2026-10-11:

| hecho | comprobación posterior (2026-10-11) |
|---|---|
| `E_INV_HI >= 1/e` | `E_INV_HI = 0.36787944117144233 = iv_hi(iv.exp(-1))` (`B1/verify_b1_5_analytic_separation.py:171`); `>= 1/e` comprobado en `mpmath`. Cubierto por la 2.ª ronda de auditoría de B1.5 (§11) |
| `sum_dn <= Σ <= sum_up` | árbol por parejas con un `nextafter` hacia afuera en cada suma (`:114-140`); sustituyó a `math.fsum` en la 2.ª ronda de auditoría de B1.5 |
| dominio de `q_encl`/`G_encl` | nodos efectivos `wt[0] = -1.3510000000000002`, `wt[-1] = 0.6310000000000001`; `s_encl` certifica cada punto por dos desigualdades escalares, válidas para todo `w < 1` (B1.5 §5) |
| (v) reproducción | reejecutado a `M=128`: `S_lo`, `B_hi`, `B'_lo`, `Z`, `Z'`, la cota y el terminal **idénticos bit a bit** al JSON congelado; `fastmath_guard.ok = True` |

**Correcciones de la nota pedidas por el veredicto y aplicadas en esta revisión.** Ninguna toca
`S_lo`.

- H4 se reescribe como hipótesis de entorno sobre todo `mpmath.iv` (§6).
- Cauchy–Schwarz integral se etiqueta como lema nuevo (§2.4).
- Se incluye el argumento `V_ε` en H1 y se retira la medida nula (§6).
- Se justifica la resta `AU`/`AL` (§2.4).
- §1 pasa a decir monotonía estricta en un intervalo **no cuantificado** de `γ`.
- «Sumas secuenciales» pasa a «árbol por parejas dirigido de B1.5» (§3).
- H3 pasa a ser teorema (§6).
- Se declara `λ5` (§6).

**Lo que el certificado NO da**, según las cinco casas:

- la transferencia del signo al punto medio real de la curva;
- un radio cuantificado de monotonía, sin el cual no sirve para B2.1.

**Diferencia con B1.5.** B1.5 llegó a `AUDIT_PASS_FORMAL` en su tercera ronda. Este certificado
tiene un pase **condicional**, y la condición se comprobó fuera del sanedrín, no en una segunda
ronda. Si eso basta para promocionarlo lo decide el PI (`docs/hoja_de_ruta_12_oct_2026.md` §2).

## 9. Promoción

Decisión del PI del 2026-10-12, tomada después de la revisión de texto `a671493` y **sin**
segunda ronda del sanedrín. El PI dio por suficiente el pase condicional unánime, porque la
condición está comprobada fuera del sanedrín (§8).

```text
B2_GATE = CERTIFIED_POSITIVE_AT_T0   (AUDIT_PASS_CONDITIONAL_B15_DEPENDENCIES, condición verificada)
B2.1    = INCONCLUSIVE_BY_BOUNDS     (sin cambio)
B3      = INCONCLUSIVE_BY_BOUNDS     (sin cambio)
```

El alcance es el de §1: el signo en `lambda*_binary64` a lo largo de `d`, y monotonía en un
intervalo no cuantificado de `γ`. **No** da el radio que pide B2.1 ni el signo en el punto
medio real. La enmienda sigue vigente: excluir cero en `t0` **no** emite un terminal de B2.1.

```text
PI: Nacho Martín              fecha: 2026-10-12
```

## Adenda 2026-10-12 — el control de fast-math pasa en vacío con la caché

El `fastmath_guard` de este verificador lee el IR con `inspect_llvm`. Cuando los kernels se
cargan desde la caché de numba (`cache=True`), ese IR es un módulo vacío, y el control da
`ok = True` sin haber inspeccionado nada. Esto afecta a las reejecuciones de §8: la
reproducción bit a bit y probablemente la condición (v). Se comprobó aparte recompilando los
19 kernels sin caché: **ninguno tiene flags** (`dev/explore_gate_fastmath_fresh_ir.py`). El
número y el terminal no cambian; solo cambia la evidencia del control. Detalle en
`dev/B2_FASTMATH_GUARD_CACHE_FINDING_2026-10-12.md`. Este verificador no se edita, porque es el
objeto auditado.
```
