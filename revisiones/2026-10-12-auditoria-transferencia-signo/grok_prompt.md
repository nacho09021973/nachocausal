---
name: auditor-sellado
description: Auditor sellado
---
Eres CIRO, auditor independiente. No tienes acceso a ficheros, terminal, web ni herramientas: todo lo disponible está en este prompt. No escribas llamadas a herramientas de ningún tipo; escribe tu intervención directamente. Etiqueta como [SOURCE] sólo lo que aparece abajo; cualquier otra cosa es, como mucho, [INFERENCE] o [UNVERIFIED]. Responde en español, como máximo 900 palabras, punto por punto (1-5 del acta y el diagnóstico de radio), con clasificación de cada hallazgo (SE_SOSTIENE / MENOR / REQUIERE_CORRECCIÓN / INVALIDA) y condición de concesión, y termina con una línea 'Veredicto: <uno de los veredictos posibles>'. Nota: la otra casa (ABNER) audita por separado; no verás su turno.

# Acta — auditoría de la transferencia del signo de B2 al punto medio real

**Fecha:** 2026-10-12. **Convoca:** el PI. **Casas:** CIRO y ABNER. El PI ha pedido una
auditoría ligera a dos casas, no el sanedrín completo.

Se os pide **auditar**, no proponer trabajo nuevo. El objeto está congelado y subido **antes**
de esta auditoría (`7bcc087`). Vuestro trabajo es intentar **romperlo**: buscad una
desigualdad falsa, un caso que no esté cubierto o una constante que no acote lo que dice
acotar. Un acuerdo fácil no tiene valor.

No tenéis herramientas. Solo cuentan esta acta y los adjuntos:

1. `B2_sign_transfer.md` — la nota: qué cierra, la cota, el diagnóstico de radio y las
   hipótesis.
2. `verify_b2_sign_transfer.py` — el verificador completo (`mpmath.iv`).
3. `verification_b2_sign_transfer.json` — su salida.
4. `B2_path2_gate_certificate.md` — la nota de la compuerta, ya auditada y promocionada. Da el
   contexto: H1–H5, la parametrización de ASTRA en H3 y las cotas que se heredan.

## 1. Qué se afirma

La compuerta certificó `S(lambda*; d) >= S_lo = +0.0013679` en el binary64
`lambda* = path(0.5)`, a lo largo de la `d` exacta de los binary64. La nota afirma que, para
todo punto `m` a distancia sup `<= 1e-16` de `lambda*` y toda dirección `d'` a distancia sup
`<= 1e-16` de `d`:

```text
S(m; d') >= S_lo − DS_point − DS_dir >= +0.0013679131 > 0
```

Ese conjunto contiene el punto medio decimal y el punto medio exacto de los extremos binary64.

## 2. Lo que no se reabre

La auditoría de la compuerta (sanedrín 2026-10-11, pase condicional con la condición
verificada) cubre la cadena N1–N4, H3 como teorema, H4 como hipótesis de entorno y la capa
escalar de B1.5 (`s_encl`, `q_encl`, `G_encl`, `E_INV_HI`). Aquí solo se audita la cota
de continuidad nueva.

## 3. Lo que se os pide

Para cada punto, decid si se sostiene y, si no, cuál es la condición mínima para concederlo.

1. **El módulo `ω_h`.** La cota de `|h(x,y) − h(x',y)|` en los casos degenerados (un par
   comparable y el otro no, `A` o `B` nulos) y en las dos orientaciones. La desigualdad
   `|√s − √t| <= √|s−t|`. Que `w_f` no salga del rango donde valen `L_q` y `q_max`. Que usar
   **la misma** clase de `f` para los dos pares sea legítimo.
2. **`ΔI_f`.** Que `H_K <= Z` y que el término `|KΔK'|` cubra el cambio de `K` dentro de `H`.
   Que los extremos de cada cara estén bien contados.
3. **`q'` y `G'`.** Las fórmulas vía `ds/dw = −1/(s e^s)` y la monotonía en `s` de cada factor
   que se usa para acotarlas.
4. **`Δk` y el término de dirección.** La linealidad de `S` en la dirección. Que el término de
   dirección use `B/Z`, y no `k`, como coeficiente de `J_f`.
5. **El código frente a la nota.** Que cada fórmula del script sea la de la nota, que el
   redondeo vaya hacia afuera (`mpmath.iv`, `.a`/`.b`) y que no se use ningún valor en `m` como
   si fuera conocido.

**El diagnóstico de radio** (§3 de la nota) no entra en el terminal, pero afirma un radio de
`1e-7` en `γ`. Atacadlo también si veis un fallo.

**Veredictos posibles:** `AUDIT_PASS`, `AUDIT_PASS_CONDITIONAL_<COND>`,
`AUDIT_REQUIRES_MINOR_FIX`, `AUDIT_FAIL`.

### Adjunto: research_program/puente_3p1/2026-10-12/B2_sign_transfer.md
```
# B2 — transferencia del signo de la compuerta al punto medio real

> **STATUS: `FROZEN / PENDING_INDEPENDENT_AUDIT`.** Como el certificado de la compuerta, se
> congela y se sube **antes** de auditarlo, y no se promociona hasta que lo revise otra familia
> de modelos. Guardarraíles de B2 intactos: `no_new_path`, `no_new_t0`, `no_search`,
> `no_adjustment`. La enmienda sigue vigente: nada de esto emite un terminal de B2.1.

**Fecha:** 2026-10-12 · **Verificador:** `verify_b2_sign_transfer.py` →
`verification_b2_sign_transfer.json` (determinista, < 1 s) · **Parte de:** el certificado
promocionado `research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md` (`7909c0e`,
`be34b74`).

```text
S_lo (compuerta, en lambda*_binary64, dirección d)   = +0.0013679385529351228
pérdida por desplazar el punto  (DELTA = 1e-16)      <=  2.5435e-08
pérdida por cambiar la dirección (EPS = 1e-16)       <=  1.8215e-16
S en el punto medio real, dirección real             >= +0.0013679131178324765
drho/dt en el punto medio real                       >= +0.0070473319080282945
TERMINAL = B2_SIGN_TRANSFERRED_TO_REAL_MIDPOINT      (pendiente de auditoría)
```

## 1. Qué cierra

El certificado de la compuerta da el signo en el binary64 `lambda* = path(0.5)` a lo largo de
la `d = L1 − L0` exacta de los binary64 (su H5). El sanedrín señaló que eso **no** era el signo
en el punto medio real de la curva. Esta nota lo transfiere a los dos candidatos razonables a
«punto medio real»:

| objetivo | distancia sup del punto a `lambda*` | distancia sup de la dirección a `d` |
|---|---|---|
| punto medio decimal `(lambda0 + lambda1)/2`, dirección decimal | `1/22517998136852480 ≈ 4.4e-17` | `≈ 4.4e-17` |
| punto medio exacto de los extremos binary64 `(L0 + L1)/2`, dirección `d` | `1/18014398509481984 ≈ 5.6e-17` | `0` |

Ambos caen dentro del conjunto declarado: punto a distancia sup `<= DELTA = 1e-16` y dirección a
distancia sup `<= EPS = 1e-16`. **El signo vale en todo ese conjunto.** La quinta componente,
`epsilon_s`, también difiere en `~5.6e-18` en el caso decimal, pero `rho` no depende de ella:
solo es una condición de admisibilidad (nota de la compuerta, §6).

## 2. La cota

`S(x; e) = 2 Σ_f v_f(e) I_f − 2 (B/Z) Σ_f v_f(e) J_f`, con `I_f = ∫_f g H_K` y `J_f = ∫_f g`.
Es la forma de H3 de la compuerta, que es un teorema y vale en cualquier rectángulo. `S` es
**lineal en la dirección**, así que

```text
S(m; d') = S(lambda*; d) − [S(lambda*; d) − S(m; d)] + S(m; d' − d)
        >= S_lo − DS_point − DS_dir .
```

**Término de dirección.** `|S(m; e)| <= EPS Σ_f (2 L_f g_max Z_max + 2 L_f g_max B_max/Z_min)`,
donde `L_f` es la longitud de la cara agrandada `2·DELTA`.

**Término de punto.** Al mover el rectángulo `K → K'` cada coordenada se desplaza `<= DELTA`.
Se acotan estas piezas:

- `|K Δ K'| <= 2δ(L_v + 2δ) + 2δ(L_u + 2δ)`, de donde `|ΔZ| <= g_max |KΔK'|` y
  `|ΔB| <= 2 g_max² |K∪K'| |KΔK'|`, porque `h <= 1`.
- `|ΔJ_f| <= 2δ g_max + L_f L_G c_max δ`: los extremos, más el desplazamiento de `G(UV)` a lo
  largo de la cara.
- `|ΔI_f| <= 2δ g_max Z_max + L_f [L_G c_max δ Z_max + g_max (g_max |KΔK'| + Z_max ω_h)]`. Esto
  sale de `H_K(x) <= Z` y de
  `|H_{K'}(x') − H_K(x)| <= g_max |KΔK'| + Z_max sup_y |h(x',y) − h(x,y)|`.
- `k = 2Z'/Z`: `|Δk| <= 2(|ΔZ'|/Z_min + |Z'| |ΔZ|/(Z_min Z_lo))`, y
  `|k_m B_m − k_* B_*| <= |Δk| B_max + k_* |ΔB|`.

Las cotas de `lambda*` (`Z`, `Z'`, `B_hi`, `2Z'/Z`, `S_lo`) se leen del JSON congelado de la
compuerta, y el script comprueba su terminal, su `M` y su `S_lo`.

**El módulo de `h`, la única pieza que no es Lipschitz.** Para `x, x'` a distancia sup `<= δ`
de un mismo `y`, sea `A = dU`, `B = dV` del par. Siempre se cumple
`Delta <= q_max sqrt(A⁺ B⁺)`. Con `A, B > 0`, la parametrización de ASTRA (H3 de la compuerta)
escribe `T = sqrt(AB) sup_f ∫ q(w_f) sqrt(f')` sobre **una misma** clase de `f` para los dos
pares, con `∫ sqrt(f') <= 1`. Por orientación:

```text
|T − T'| <= q_max sqrt(δ (A_max + B_max + δ))                    [ |√s − √t| <= √|s − t| ]
          + sqrt(A_max B_max) L_q (U_max + V_max + δ) δ          [ |w_f − w'_f| <= (U_max+V_max+δ) δ ]
```

El primer término cubre también los casos degenerados: si un par no es comparable, `T' = 0` y
`T <= q_max sqrt(|A⁺B⁺ − A'⁺B'⁺|)`. El tope `min(pi,·)` es 1-Lipschitz y `p` es ½-Lipschitz.
Además `h = p(T_fut) + p(T_past)`, con a lo sumo uno no nulo. Por tanto
`|h(x,y) − h(x',y)| <= ω_h`, la cota de arriba, que vale `4.2e-8` para `δ = 1e-16`. Que el
módulo sea `sqrt(δ)` y no `δ` refleja el cono de luz: cerca de él, `Delta ~ sqrt(dU dV)`.

**Constantes**, todas con la capa escalar auditada de B1.5 y `mpmath.iv`, en el rango de `w`
del rectángulo agrandado, `[−1.3500000000000005, 0.6300000000000002]`:

| constante | cota | por qué |
|---|---|---|
| `g_max` | `E_INV_HI = 0.36787944117144233` | pico de `G` en `1/e` |
| `s` | `[0.68122, 1.34998]` | `s_encl` en los extremos; `s` es decreciente en `w` |
| `q_max` | `2.5303063` | `q_encl(w_cap)`; `q` es creciente en `w` |
| `L_q` | `5.0781904` | `q'(w) = q(1/2 + 3/(2s))/(s e^s)`, con todos los factores decrecientes en `s` |
| `L_G` | `0.1315394` | `|G'(w)| = |1−s| e^{−2s}/s <= max|1−s| · e^{−2 s_min}/s_min` |

## 3. Diagnóstico: el radio que da este módulo

La misma cota, con la dirección fija y el punto en cualquier lugar de la bola sup de radio `r`.
La lista de radios está fijada de antemano y no se busca nada:

| `r` | `1e-16` | `1e-12` | `1e-9` | `1e-8` | `1e-7` | `1e-6` |
|---|---|---|---|---|---|---|
| cota inferior de `S` | `+0.0013679` | `+0.0013654` | `+0.0012875` | `+0.0011134` | `+0.0005621` | `−0.0011910` |

Como `max|d_i| = 1`, los puntos `γ(s)` con `|s| <= 1e-7` caen en la bola de radio `1e-7`. Por
tanto `rho∘γ` es **estrictamente creciente en `|s| <= 1e-7`**. Es un radio cuantificado, pero
la malla de B2.1 (`t ∈ [0.45, 0.55]`) pide `|s| <= 0.05`, unas `5·10⁵` veces más. El factor
`sqrt(r)` del módulo de `h` hace que este método **no pueda** llegar a B2.1 aumentando el
margen. Para B2.1 hace falta otro objeto, por ejemplo una cota inferior de `rho'` en un
intervalo construida directamente, como la compuerta, sobre una caja de `lambda`. Esta fila es
diagnóstica y no entra en el terminal.

## 4. Hipótesis

- **Las de la compuerta**, sin cambios: H1 (con `V_ε`), H2, H3 (que vale en cualquier
  rectángulo, también en el de `m`), H4 (entorno IEEE-754 + `mpmath.iv`) y la condición
  `B15_DEPENDENCIES` verificada. Las cotas de `lambda*` se heredan del JSON congelado.
- **La parametrización de ASTRA** `T = sqrt(AB) sup_f ∫ q(w_f) sqrt(f')`, con la misma clase de
  `f` para todo par con `A, B > 0`. La auditoría la aceptó como base del módulo de continuidad
  de H3, y aquí se usa con constantes explícitas.
- **`rho` no depende de `epsilon_s`** (nota de la compuerta, §6).

## 5. Qué debe mirar la auditoría

1. El módulo `ω_h`: los casos degenerados, las dos orientaciones y que `w_f` no salga del rango
   donde valen `L_q` y `q_max`.
2. La descomposición de `ΔI_f`: que `H_K <= Z` y que el término `|KΔK'|` cubre el cambio de `K`
   dentro de `H`.
3. Las fórmulas de `q'` y `G'` vía `ds/dw = −1/(s e^s)`, y la monotonía en `s` de cada factor.
4. Que leer las cotas de `lambda*` del JSON, en lugar de recalcularlas, es legítimo, dado que el
   verificador de la compuerta lo reproduce bit a bit.
5. Que ningún término usa `S`, `Z` o `B` en `m` como si fueran conocidos: solo sus cotas.
```

### Adjunto: research_program/puente_3p1/2026-10-12/verify_b2_sign_transfer.py
```
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
```

### Adjunto: research_program/puente_3p1/2026-10-12/verification_b2_sign_transfer.json
```
{
  "unit": "PUENTE-3P1 / B2 sign transfer",
  "gate_certificate": {
    "json": "research_program/puente_3p1/2026-10-11/verification_b2_path2_gate_certificate.json",
    "S_lo": 0.0013679385529351228,
    "frozen_in": "7909c0e"
  },
  "targets": {
    "decimal_midpoint": {
      "point_offset_sup": "1/22517998136852480",
      "direction_offset_sup": "1/22517998136852480",
      "epsilon_s_offset": "1/180143985094819840"
    },
    "binary64_endpoint_midpoint": {
      "point_offset_sup": "1/18014398509481984",
      "direction_offset_sup": "0",
      "epsilon_s_offset": "0"
    }
  },
  "rho_independent_of_epsilon_s": "declared (gate note section 6); q_encl/G_encl take only w",
  "main": {
    "delta": "1/10000000000000000",
    "eps": "1/10000000000000000",
    "constants": {
      "w_cap": 0.6300000000000002,
      "w_floor": -1.3500000000000005,
      "s_min": 0.6812206505986326,
      "s_max": 1.349981001072602,
      "q_max_hi": 2.5303063407120603,
      "L_q_hi": 5.078190383946766,
      "L_G_hi": 0.13153942081917575,
      "g_max_hi": 0.36787944117144233
    },
    "omega_h_hi": 4.196038502463764e-08,
    "dZ_hi": 2.023336926442933e-16,
    "dB_hi": 1.801312619879316e-16,
    "dZprime_hi": 1.7061387394308095e-16,
    "dS_point_hi": 2.5435102463949117e-08,
    "dS_dir_hi": 1.821462725283141e-16,
    "S_lower_at_target": 0.0013679131178324765,
    "drho_dt_lower_at_target": 0.0070473319080282945,
    "sign_transferred": true
  },
  "diagnostic_radius_table_direction_fixed": [
    {
      "radius": "1/10000000000000000",
      "S_lower": 0.0013679131178326587
    },
    {
      "radius": "1/100000000000000",
      "S_lower": 0.0013676842017718135
    },
    {
      "radius": "1/1000000000000",
      "S_lower": 0.0013653950274350472
    },
    {
      "radius": "1/10000000000",
      "S_lower": 0.0013425019112162197
    },
    {
      "radius": "1/1000000000",
      "S_lower": 0.0012874902930650148
    },
    {
      "radius": "1/100000000",
      "S_lower": 0.0011134334441674422
    },
    {
      "radius": "1/10000000",
      "S_lower": 0.0005620685623911853
    },
    {
      "radius": "1/1000000",
      "S_lower": -0.0011910016214978154
    }
  ],
  "no_new_path": true,
  "no_new_t0": true,
  "no_search": true,
  "no_adjustment": true,
  "terminal": "B2_SIGN_TRANSFERRED_TO_REAL_MIDPOINT"
}
```

### Adjunto: research_program/puente_3p1/2026-10-11/B2_path2_gate_certificate.md
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
```
