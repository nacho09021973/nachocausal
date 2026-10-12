# B2 — transferencia del signo de la compuerta al punto medio real

> **STATUS: `B2_SIGN_TRANSFERRED_TO_REAL_MIDPOINT`** (`AUDIT_PASS`, dos casas a ciegas;
> promocionado por el PI el 2026-10-12, §6). Se congeló y se subió **antes** de auditarlo
> (`7bcc087`). Lo auditaron CIRO (Grok) y ABNER (DeepSeek, por la web):
> `revisiones/2026-10-12-auditoria-transferencia-signo/RESUMEN.md`. El único hallazgo, MENOR y
> documental, está corregido: el redondeo de las constantes de §2. Fue una auditoría más ligera
> que la de la compuerta: dos casas en vez de cinco y una sola ronda, sin cruce entre ellas.
> Guardarraíles de B2 intactos: `no_new_path`, `no_new_t0`, `no_search`, `no_adjustment`.
> La enmienda sigue vigente: nada de esto emite un terminal de B2.1.

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
TERMINAL = B2_SIGN_TRANSFERRED_TO_REAL_MIDPOINT      (AUDIT_PASS, dos casas; promocionado, §6)
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
del rectángulo agrandado, `[−1.3500000000000005, 0.6300000000000002]`. Los valores de la tabla
están redondeados **hacia arriba** a 8 cifras; los exactos, que son los que usa el cálculo,
están en el JSON:

| constante | cota | por qué |
|---|---|---|
| `g_max` | `E_INV_HI = 0.36787944117144233` | pico de `G` en `1/e` |
| `s` | `[0.68122, 1.34998]` | `s_encl` en los extremos; `s` es decreciente en `w` |
| `q_max` | `2.53030635` | `q_encl(w_cap)`; `q` es creciente en `w` |
| `L_q` | `5.07819039` | `q'(w) = q(1/2 + 3/(2s))/(s e^s)`, con todos los factores decrecientes en `s` |
| `L_G` | `0.13153943` | `|G'(w)| = |1−s| e^{−2s}/s <= max|1−s| · e^{−2 s_min}/s_min` |

## 3. Diagnóstico: el radio que da este módulo

La misma cota, con la dirección fija y el punto en cualquier lugar de la bola sup de radio `r`.
La lista de radios está fijada de antemano y no se busca nada. La tabla muestra 6 de los 8
radios de `DIAG_RADII`; el JSON los tiene todos:

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

## 6. Promoción

Decisión del PI del 2026-10-12, sobre el `AUDIT_PASS` de dos casas a ciegas (`57e62eb`), y
sabiendo que es una auditoría más ligera que la de la compuerta.

```text
B2_GATE             = CERTIFIED_POSITIVE_AT_T0               (sin cambio)
B2_GATE_REAL_POINT  = B2_SIGN_TRANSFERRED_TO_REAL_MIDPOINT   (nuevo)
B2.1                = INCONCLUSIVE_BY_BOUNDS                 (sin cambio)
B3                  = INCONCLUSIVE_BY_BOUNDS                 (sin cambio)
```

Alcance: `drho/dt >= +0.0070473` en el punto medio real, tanto en el decimal como en el exacto
de los extremos binary64, a lo largo de la dirección real. Como diagnóstico, `rho∘γ` es
estrictamente creciente en `|s| <= 1e-7`. **No** da nada para la malla de B2.1, y la enmienda
sigue vigente.

```text
PI: Nacho Martín              fecha: 2026-10-12
```
