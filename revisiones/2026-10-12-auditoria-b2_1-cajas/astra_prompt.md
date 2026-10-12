Eres ASTRA, auditor independiente. No tienes acceso a ficheros, terminal, web ni herramientas: todo lo disponible está en este prompt. No escribas llamadas a herramientas; escribe tu intervención directamente. Etiqueta como [SOURCE] sólo lo que aparece abajo; cualquier otra cosa es, como mucho, [INFERENCE] o [UNVERIFIED]. Responde en español, como máximo 1200 palabras, punto por punto (§7.1–5 de la nota y los puntos 6–7 del acta), con clasificación y condición de concesión, y termina con una línea 'Veredicto: <uno de los veredictos posibles>'.

# Acta — auditoría del certificado por cajas de B2.1

**Fecha:** 2026-10-12. **Convoca:** el PI. **Casa:** ASTRA (sellada, una sola intervención).

Se te pide **auditar**, no proponer trabajo nuevo. El objeto está congelado y subido **antes**
de esta auditoría (`f1e030f`). Tu trabajo es intentar **romperlo**: busca una inclusión falsa,
un vértice mal elegido, una cota en la dirección equivocada o un caso que no esté cubierto. Un
acuerdo fácil no tiene valor. En este proyecto, de once errores, diez los encontró una familia
de modelos distinta de la que escribió el código.

No tienes herramientas. Solo cuentan esta acta y los adjuntos:

1. `B2_1_box_certificate.md` — la nota: qué afirma, la cadena (§3), la aritmética, las
   hipótesis, los controles y la lista de auditoría (§7).
2. `verify_b2_1_box_certificate.py` — el verificador de cajas, completo.
3. `verify_b2_path2_gate_certificate.py` — el verificador de la compuerta. B2.1 importa sus
   kernels **sin cambios**: `cell_weights`, `calibration_point_tables`, `cs_prefix`,
   `ub_table`, `b_hi_sum`, `g_range`, `rect_w`, `tiling` y las tablas.
4. `B2_path2_gate_certificate.md` — la nota de la compuerta, ya auditada y promocionada. Da
   H1–H5 y la monotonía del `sup` respecto a los extremos (§2.2).
5. `resumen_json.json` — la salida del verificador sin la lista de las 100 cajas.

## 1. Qué se afirma

Para todo `t ∈ [0.45, 0.55]`, en las dos lecturas de la curva (extremos binary64 y decimal),
`drho/dt(t) >= +0.0066481 > 0`. Para ello se parte el intervalo en 100 cajas y en cada una se
acota `S` por debajo, de forma uniforme para todo `lambda` de la caja, con un rectángulo
interior `K_in` y uno exterior `K_out`, y con las caras ensanchadas en franjas. Terminal:
`B2.1_POSITIVE_DERIVATIVE`.

## 2. Lo que no se reabre

La auditoría de la compuerta, con pase condicional y la condición verificada, cubre:
- la representación (H1, con `V_ε`);
- la monotonía del `sup` respecto a los extremos;
- la calibración y Cauchy–Schwarz integral dentro de `ub_table`;
- H3 como teorema;
- la capa escalar de B1.5;
- los kernels importados.

Aquí se audita el **ensamblado por cajas** y los **tres kernels nuevos** (`lb_rows_xy`,
`strip_weights`, `face_h_cells`).

## 3. Lo que se te pide

Responde los cinco puntos de §7 de la nota. Para cada hallazgo, indica una clasificación
(`SE_SOSTIENE`, `MENOR`, `REQUIERE_CORRECCIÓN` o `INVALIDA`) y la condición mínima de concesión.
Además:

6. **El control de fast-math nuevo** (`fresh_ir`): ¿puede pasar en vacío de alguna otra forma?
7. **Algo que la nota no pregunta.** ¿Hay alguna pieza de `run_box` que use un valor de una
   `lambda` concreta como si valiera para toda la caja?

**Veredictos posibles:** `AUDIT_PASS`, `AUDIT_PASS_CONDITIONAL_<COND>`,
`AUDIT_REQUIRES_MINOR_FIX`, `AUDIT_FAIL`.

### Adjunto: B2_1_box_certificate.md
```
# B2.1 — certificado por cajas: `drho/dt > 0` en todo `t ∈ [0.45, 0.55]`

> **STATUS: `FROZEN / PENDING_INDEPENDENT_AUDIT`.** Como la compuerta y la transferencia del
> signo, se congela y se sube **antes** de auditarlo, y no se promociona hasta que lo revise
> otra familia de modelos. Guardarraíles de B2 intactos: `no_new_path`, `no_new_t0`,
> `no_new_points`, `no_search`, `no_adjustment`.

**Fecha:** 2026-10-12 · **Verificador:** `verify_b2_1_box_certificate.py` →
`verification_b2_1_box_certificate.json` · **Especificación:**
`research_program/puente_3p1/2026-09-12/B2_1_local_order_law_injectivity.md` · **Controles:**
`dev/explore_b2_1_box_controls.py`.

```text
t ∈ [9/20, 11/20]   N = 100 cajas contiguas de ancho 1/1000,  M = 128
min_k S_lo            = +0.0012174762052819036   (caja t ∈ [9/20, 451/1000])
max_k S_lo            = +0.0013992726582646622   (caja t ∈ [549/1000, 11/20])
min_k drho/dt lower   = +0.006648095518840022
fastmath_guard        : 19 kernels, IR recompilado sin caché (>= 4556 caracteres), sin flags, mutante detectado, ok = True
TERMINAL = B2.1_POSITIVE_DERIVATIVE   (pendiente de auditoría)
```

---

## 1. Qué establece y qué no

B2.1 pide inyectividad local de `t ↦ rho(lambda(t))` cerca de `t0 = 0.5`, en la malla congelada
`{0.45, 0.475, 0.5, 0.525, 0.55}`, mediante «una envolvente de derivada que excluya cero». La
enmienda de la regla de promoción exige que ese control sea **en un vecindario**, no solo en
`t0`.

Este certificado establece, bajo las hipótesis de §5, que **`drho/dt > 0` en todo el intervalo
`[0.45, 0.55]`**, que es la envolvente de la malla congelada. Vale para las dos lecturas de la
curva, la de los extremos binary64 y la decimal. Por tanto `rho∘lambda` es estrictamente
creciente en `[0.45, 0.55]`, en particular inyectiva, y los cinco puntos de la malla quedan
ordenados estrictamente.

**No** establece:
- nada fuera de `[0.45, 0.55]`, ni en otra curva, ni para `phi`, ni para `n=3`;
- identificabilidad global;
- nada sobre B3.

## 2. Por qué funciona donde el módulo de continuidad no llegaba

La transferencia del signo llevaba el signo de `t0` a sus vecinos con un módulo de continuidad.
Como `h` es Hölder-½ cerca del cono, ese módulo se agota en un radio de `1e-7`. Este certificado
no transfiere nada: **acota `S` directamente y de forma uniforme en cajas de `lambda`**, con la
misma maquinaria auditada que la compuerta. El ancho de la caja no entra por una raíz, sino
porque las caras se ensanchan hasta convertirse en franjas.

## 3. Cadena

**Cajas.** `[0.45, 0.55]` se parte en `N` intervalos iguales `T_k`. En cada `T_k`, cada
coordenada de `lambda(t)` es afín y monótona en las dos curvas. `c_lo` y `c_hi` son el mínimo y
el máximo, redondeados hacia afuera, sobre las dos curvas y los dos extremos. Para todo `lambda`
de esa caja:

```text
K_in  = [−uo_lo, ui_lo] × [v0_hi, v1_lo]   ⊆   K(lambda)   ⊆   K_out = [−uo_hi, ui_hi] × [v0_lo, v1_hi]
```

Cada cara de `K(lambda)` cae dentro de una **franja** delgada; por ejemplo, `U = u_in(lambda)`
cae en `[ui_lo, ui_hi]`. La dirección solo entra por las velocidades normales `v_n`, que se
encierran para las `d` de ambas curvas.

**Cotas.** Como `g, h >= 0`, toda integral es monótona en el dominio.
- `Z ∈ [Z(K_in)_lo, Z(K_out)_hi]` y `B <= B(K_out)_hi`, con `cell_weights` y `b_hi_sum` de la
  compuerta.
- **Caras con `v_n > 0`** (`U=−u_out`, `U=u_in`, `V=v0`). Se toma
  `I_f >= Σ_celdas len_lo · g_lo(celda) · H_lo(celda)`. La suma recorre las celdas de franja de
  la extensión **interior** de la cara, que está contenida en la cara real, y el integrando es
  `>= 0`. Para `H` se usa
  `H_lo(celda) = Σ_{Q ⊆ K_in} W_lo(Q) [p_lo(LB(c_top, Q_bot)) + p_lo(LB(Q_top, c_bot))]`. Vale
  por la monotonía del `sup` respecto a los extremos (§2.2 de la compuerta): todo punto `x` de
  la celda está por encima de `c_bot` y por debajo de `c_top`, y además `H_K >= H_{K_in}`. De
  los dos sumandos, a lo sumo uno es no nulo. `LB` es la cota de la recta de la compuerta,
  calculada desde vértices de franja, que no son nodos de la retícula: es el kernel nuevo
  `lb_rows_xy`.
- **Cara `V=v1`** (`v_n < 0`). Se toma `I_f <= Σ_celdas len_hi · g_hi · H_hi`, sobre la
  extensión **exterior**, con
  `H_hi(celda) = Σ_{Q ⊆ K_out} W_hi(Q) [p_hi(UB(c_bot, Q_top)) + p_hi(UB(Q_bot, c_top))]`. Cada
  sumando acota su propia orientación. La retícula exterior tiene `v1_lo` como penúltimo nodo
  en `V`, así que los dos vértices de cada celda de franja son nodos de la retícula y el
  `ub_table` de la compuerta (Cauchy–Schwarz integral más calibración) se aplica sin cambios.
- **`Z'`.** `J_f = ∫_f g` se acota por arriba sobre la extensión exterior en las caras con
  `v_n > 0`, y por abajo sobre la extensión interior en `V=v1`. Con eso,
  `Z'_hi = Σ v_n^hi J_f^hi + v_n^hi(v1) · J^lo(v1)`.
- **Ensamblado.** `S_lo = B'_lo − (2 Z'_hi/Z_lo) B_hi`, con `B'_lo = 2 Σ_f v_n^lo · I_f`
  (cota inferior en las caras con `v_n > 0`, superior en `V=v1`). Es válido porque
  `k = 2Z'/Z <= 2Z'_hi/Z_lo` y `B >= 0`. Por H3, que es teorema en cualquier rectángulo,
  `drho/dt(t) = S(lambda(t); d)/Z²` en cada `t`.

## 4. Aritmética

La misma de la compuerta (§3 de su nota): un ulp hacia afuera tras cada operación binary64,
tablas monótonas certificadas con la capa escalar de B1.5, sumas por el árbol dirigido de B1.5 y
control de fast-math en el IR de LLVM. Los kernels de la compuerta se importan **sin cambios**.
El control cubre los 16 que este verificador usa, más los 3 nuevos (`lb_rows_xy`,
`strip_weights`, `face_h_cells`): 19 en total. Inspecciona IR **recompilado sin caché** (§6).
Los otros tres de la compuerta (`lb_rows`, `face_h`, `segment_weights`) no se ejecutan aquí. La
tabla de `w` es una sola para todas las cajas y cubre `K_out` en todo el intervalo, con el
margen de `1e-3`.

`M` (la retícula) y `N` (las cajas) son parámetros de la prueba: cualquier valor da una cota
válida. Se fijaron después de una prueba en `dev` con `M=64` sobre tres cajas (`k = 0, 49, 99`),
que ya dio `S_lo ≈ +0.00039` en las tres. No hay búsqueda sobre `lambda`, `t0` ni puntos.

## 5. Hipótesis

Las de la compuerta, sin cambios:
- H1, con `V_ε`;
- H2;
- H3, que es teorema en cualquier rectángulo;
- H4, el entorno IEEE-754 más `mpmath.iv`;
- la condición `B15_DEPENDENCIES`, ya verificada;
- `rho` no depende de `epsilon_s`.

No se añade ninguna hipótesis analítica nueva. Lo nuevo es el **ensamblado** (§3) y los tres
kernels.

## 6. Controles

- **Kernel nuevo frente al auditado.** `lb_rows_xy`, alimentado con nodos de la retícula, da
  **lo mismo bit a bit** que el `lb_rows` auditado de la compuerta en los dos sentidos
  (`M = 32`, 1 de cada 7 fuentes; 40 142 y 39 822 entradas no nulas) (`dev/explore_b2_1_box_controls.py`).
- **Control negativo.** Una sola caja sobre todo `[0.45, 0.55]` con `M = 64` da
  `S_lo = −0.005916`. La cota **sí** depende del ancho de la caja, así que no es vacía.
- **Contra la compuerta.** Las cajas que bordean `t0` dan `+0.0013072` (`[0.499, 0.5]`) y
  `+0.0013091` (`[0.5, 0.501]`), frente a `+0.0013679` del punto aislado con la misma `M`. Una caja
  de ancho `1e-3` cuesta `~6e-5` en `S`.
- **Determinismo.** Dos ejecuciones completas (antes y después de corregir el control de
  fast-math) dan las mismas `S_lo` bit a bit. Tiempo: 591 s en cajas y 13.5 s en tablas.
- **Control de fast-math.** La primera ejecución dio `ok = False`, y estaba bien que lo diera.
  Exigía firma compilada en tres kernels de la compuerta que este verificador no usa
  (`lb_rows`, `face_h`, `segment_weights`); ahora se excluyen por nombre. Al corregirlo
  apareció un fallo más serio: con `cache=True`, `inspect_llvm` devuelve un módulo vacío y el
  control pasaba en vacío. Ahora recompila sin caché y exige la `define` de cada función. Afecta
  también al control de la compuerta, cuyos 19 kernels se comprobaron aparte, limpios
  (`dev/B2_FASTMATH_GUARD_CACHE_FINDING_2026-10-12.md`).

Muestra de cajas (todas en el JSON):

| caja `t` | `S_lo` | `drho/dt >=` | `B_hi` | `B'_lo` |
|---|---|---|---|---|
| `[9/20, 451/1000]` | `+0.0012175` | `+0.0067949` | `0.003731` | `0.007460` |
| `[19/40, 119/250]` | `+0.0012626` | `+0.0067608` | `0.003969` | `0.007813` |
| `[499/1000, 1/2]` | `+0.0013072` | `+0.0067297` | `0.004209` | `0.008165` |
| `[1/2, 501/1000]` | `+0.0013091` | `+0.0067285` | `0.004219` | `0.008180` |
| `[21/40, 263/500]` | `+0.0013543` | `+0.0066854` | `0.004482` | `0.008558` |
| `[549/1000, 11/20]` | `+0.0013993` | `+0.0066481` | `0.004746` | `0.008934` |


## 7. Qué debe mirar la auditoría

1. Las inclusiones `K_in ⊆ K(lambda) ⊆ K_out`, con la dirección de redondeo de cada lado, y que
   cada cara caiga en su franja. También que la extensión interior esté contenida en la cara
   real y que la exterior la contenga.
2. Los vértices `c_bot`/`c_top` de cada celda de franja, y qué orientación usa cada uno en
   `H_lo` y en `H_hi`.
3. La retícula exterior con el nodo `v1_lo` insertado. Que `cbot = i·n1 + (M−1)` y
   `ctop = (i+1)·n1 + M` sean los vértices correctos. Que la fila delgada superior no rompa
   ninguna hipótesis de `ub_table`, `cs_prefix`, `cell_weights` ni `b_hi_sum`.
4. Las cotas de `Z'`: superior en las caras con `v_n > 0` y en `V=v1`, y el signo de
   `v_n^hi · J^lo`.
5. Que `v_n` encierre las direcciones de ambas curvas, y que `coord_range` recorra las dos
   curvas y los dos extremos de cada caja.
```

### Adjunto: verify_b2_1_box_certificate.py
```
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

### Adjunto: resumen_json.json
```
{
 "unit": "PUENTE-3P1/B2.1_BOX_CERTIFICATE",
 "interval_t": [
  "9/20",
  "11/20"
 ],
 "curves": "binary64 endpoints and decimal, both",
 "M": 128,
 "N": 100,
 "boxes_run": [
  0,
  100
 ],
 "R_sub": 8,
 "N_tau": 64,
 "w_table_nodes": 65537,
 "seconds_tables": 13.5,
 "min_S_lo": 0.0012174762052819036,
 "min_S_lo_box_t": [
  "9/20",
  "451/1000"
 ],
 "min_drho_dt_lower_bound": 0.006648095518840022,
 "fastmath_guard": {
  "kernels_checked": 19,
  "inspection": "fresh recompilation without cache",
  "min_ir_chars": 4556,
  "gate_kernels_excluded_as_unused": [
   "lb_rows",
   "face_h",
   "segment_weights"
  ],
  "kernels_without_compiled_signature": [],
  "flags_found": {},
  "all_clean": true,
  "mutation_fastmath_detected": true,
  "ok": true
 },
 "no_new_path": true,
 "no_new_t0": true,
 "no_new_points": true,
 "no_search": true,
 "no_adjustment": true,
 "no_seeds": true,
 "no_monte_carlo": true,
 "terminal": "B2.1_POSITIVE_DERIVATIVE",
 "boxes_sample": [
  {
   "t": [
    "9/20",
    "451/1000"
   ],
   "box": {
    "v0": [
     0.36469999999999997,
     0.36500000000000005
    ],
    "v1": [
     0.9097999999999999,
     0.9100000000000001
    ],
    "u_out": [
     1.4499999999999997,
     1.4510000000000003
    ],
    "u_in": [
     0.6799999999999999,
     0.6804000000000001
    ]
   },
   "Z": [
    0.42260120526994965,
    0.4232914634782337
   ],
   "Zprime": [
    0.3529764830981395,
    0.35352194666819714
   ],
   "two_Zp_over_Z_hi": 1.6730759035217333,
   "B_hi": 0.0037310217029350736,
   "Bprime_lo": 0.007459758711979199,
   "faces_Bprime_lower": {
    "U=-u_out": 0.0034680098333777997,
    "U=u_in": 0.0025112944725399723,
    "V=v0": 0.005504349890057935,
    "V=v1": -0.004023895483996506
   },
   "S_lo": 0.0012174762052819036,
   "drho_dt_lower_bound": 0.006794874842562031,
   "seconds": 7.6
  },
  {
   "t": [
    "499/1000",
    "1/2"
   ],
   "box": {
    "v0": [
     0.3499999999999999,
     0.35030000000000006
    ],
    "v1": [
     0.8999999999999999,
     0.9002000000000001
    ],
    "u_out": [
     1.4989999999999999,
     1.5000000000000002
    ],
    "u_in": [
     0.6995999999999999,
     0.7000000000000001
    ]
   },
   "Z": [
    0.44002377413798693,
    0.4407308727560021
   ],
   "Zprime": [
    0.3579493522860139,
    0.35849674855534586
   ],
   "two_Zp_over_Z_hi": 1.629442632992485,
   "B_hi": 0.004208731299425984,
   "Bprime_lo": 0.00816509184548599,
   "faces_Bprime_lower": {
    "U=-u_out": 0.0037708642727811215,
    "U=u_in": 0.002746976163532811,
    "V=v0": 0.006144929820827533,
    "V=v1": -0.004497678411655473
   },
   "S_lo": 0.0013072056353914299,
   "drho_dt_lower_bound": 0.0067297195254427695,
   "seconds": 5.4
  },
  {
   "t": [
    "1/2",
    "501/1000"
   ],
   "box": {
    "v0": [
     0.34969999999999996,
     0.35000000000000003
    ],
    "v1": [
     0.8997999999999999,
     0.9000000000000001
    ],
    "u_out": [
     1.4999999999999998,
     1.5010000000000001
    ],
    "u_in": [
     0.6999999999999998,
     0.7004000000000001
    ]
   },
   "Z": [
    0.4403818758215305,
    0.4410893187505041
   ],
   "Zprime": [
    0.35805104687082945,
    0.3585984801838062
   ],
   "two_Zp_over_Z_hi": 1.6285796481285355,
   "B_hi": 0.0042189807816816645,
   "Bprime_lo": 0.008180046168260761,
   "faces_Bprime_lower": {
    "U=-u_out": 0.003777249098287884,
    "U=u_in": 0.0027519425278571172,
    "V=v0": 0.006158570350839971,
    "V=v1": -0.004507715808724207
   },
   "S_lo": 0.0013090999313685812,
   "drho_dt_lower_bound": 0.006728522634482155,
   "seconds": 5.6
  },
  {
   "t": [
    "549/1000",
    "11/20"
   ],
   "box": {
    "v0": [
     0.33499999999999996,
     0.33530000000000004
    ],
    "v1": [
     0.8899999999999999,
     0.8902000000000001
    ],
    "u_out": [
     1.5489999999999997,
     1.5500000000000003
    ],
    "u_in": [
     0.7195999999999999,
     0.7200000000000001
    ]
   },
   "Z": [
    0.4580536106731589,
    0.4587779629327104
   ],
   "Zprime": [
    0.36304434422745385,
    0.3635937718340331
   ],
   "two_Zp_over_Z_hi": 1.587559898500497,
   "B_hi": 0.004746012329083471,
   "Bprime_lo": 0.008933851509706527,
   "faces_Bprime_lower": {
    "U=-u_out": 0.0041004915336339,
    "U=u_in": 0.0030031466083055096,
    "V=v0": 0.006855959566463882,
    "V=v1": -0.0050257461986967615
   },
   "S_lo": 0.0013992726582646622,
   "drho_dt_lower_bound": 0.006648095518840022,
   "seconds": 5.8
  }
 ],
 "boxes_omitted": "100 boxes; all S_lo > 0"
}```
