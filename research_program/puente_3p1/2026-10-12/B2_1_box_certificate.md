# B2.1 — certificado por cajas: `drho/dt > 0` en todo `t ∈ [0.45, 0.55]`

> **STATUS: `B2.1_POSITIVE_DERIVATIVE`** (ASTRA: `AUDIT_PASS_CONDITIONAL_IR_EJECUTADO_Y_COTA_DECIMAL`,
> con las dos condiciones atendidas; promocionado por el PI el 2026-10-12, §9). Se congeló y se
> subió **antes** de auditarlo (`f1e030f`), como la compuerta y la transferencia del signo.
> Guardarraíles de B2 intactos: `no_new_path`, `no_new_t0`,
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
fastmath_guard        : 19 kernels, IR ejecutado y clausurado por sobrecarga (§4), sin flags, mutante detectado, ok = True
TERMINAL = B2.1_POSITIVE_DERIVATIVE   (ASTRA: pase condicional, condiciones atendidas en §8; promocionado, §9)
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
`strip_weights`, `face_h_cells`): 19 en total. Los otros tres de la compuerta (`lb_rows`,
`face_h`, `segment_weights`) no se ejecutan aquí.

**El control inspecciona el código que se ejecutó, completo** (`guard_kernels`, el mismo para
B3; afinado en las rondas 2 y 3 de ASTRA sobre B3, adenda de §8):
- la ejecución usa una caché de numba privada y vacía (`NUMBA_CACHE_DIR` temporal, fijada antes
  de importar numba), así que todo kernel se compila en el propio proceso, y se exige
  `stats.cache_hits == 0`;
- **por sobrecarga** ejecutada: se recorren todas las librerías que enlaza (`_linking_libraries`,
  leído sin `getattr`, de modo que si falta falla), se exige la `define` de su nombre mangled
  exacto (`fndesc.mangled_name`) y se comprueba la **clausura**: todo símbolo de código de numba
  que se **referencia** tiene que estar definido en el conjunto inspeccionado;
- ningún cuerpo numérico (kernels y cuerpos `parfor`) puede llamar por puntero, que es lo único
  que la clausura no ve; en numba esas llamadas solo aparecen en envoltorios y en el asignador;
- cada kernel paralelo tiene que tener cuerpos `prange` reales definidos, y el mutante
  `fastmath` se detecta por la misma vía.

`dev/explore_ir_guard_negative_tests.py` termina con error si no detecta alguno de estos cuatro
casos: kernel cargado de caché, cuerpo `prange` eliminado, símbolo exacto ausente y llamada
indirecta en un cuerpo numérico. La
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
  `S_lo ≈ −0.0059`. La cota **sí** depende del ancho de la caja, así que no es vacía.
- **Contra la compuerta.** Las cajas que bordean `t0` dan `+0.0013072` (`[0.499, 0.5]`) y
  `+0.0013090` (`[0.5, 0.501]`), frente a `+0.0013679` del punto aislado con la misma `M`. Una caja
  de ancho `1e-3` cuesta `~6e-5` en `S`.
- **Determinismo.** Cuatro ejecuciones completas, con las cuatro versiones del control de fast-math,
  dan las mismas `S_lo` bit a bit. Tiempo (cuarta ejecución): 582 s en cajas y 13.3 s en tablas.
- **Control de fast-math** (historia). La primera ejecución dio `ok = False`, y estaba bien que lo diera.
  Exigía firma compilada en tres kernels de la compuerta que este verificador no usa
  (`lb_rows`, `face_h`, `segment_weights`); ahora se excluyen por nombre. Al corregirlo
  apareció un fallo más serio: con `cache=True`, `inspect_llvm` devuelve un módulo vacío y el
  control pasaba en vacío. La segunda versión recompilaba sin caché. ASTRA objetó que eso no
  inspecciona el código ejecutado; la versión final es la de §4. Afecta
  también al control de la compuerta, cuyos 19 kernels se comprobaron aparte, limpios
  (`dev/B2_FASTMATH_GUARD_CACHE_FINDING_2026-10-12.md`).

Muestra de cajas (todas en el JSON). Las cotas inferiores (`S_lo`, `drho/dt`, `B'_lo`) están
truncadas hacia abajo y `B_hi` redondeada hacia arriba:

| caja `t` | `S_lo` | `drho/dt >=` | `B_hi` | `B'_lo` |
|---|---|---|---|---|
| `[9/20, 451/1000]` | `+0.0012174` | `+0.0067948` | `0.003732` | `0.007459` |
| `[19/40, 119/250]` | `+0.0012626` | `+0.0067607` | `0.003969` | `0.007813` |
| `[499/1000, 1/2]` | `+0.0013072` | `+0.0067297` | `0.004209` | `0.008165` |
| `[1/2, 501/1000]` | `+0.0013090` | `+0.0067285` | `0.004219` | `0.008180` |
| `[21/40, 263/500]` | `+0.0013543` | `+0.0066854` | `0.004482` | `0.008557` |
| `[549/1000, 11/20]` | `+0.0013992` | `+0.0066480` | `0.004747` | `0.008933` |


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

## 8. Auditoría

**ASTRA** (`gpt-6-astra`, esfuerzo alto, sellada; llamada directa a `codex exec` con las
banderas de sanedrín) auditó `f1e030f`: `revisiones/2026-10-12-auditoria-b2_1-cajas/`
(`acta.md`, `astra_prompt.md`, `astra.md`).

```text
AUDIT_PASS_CONDITIONAL_IR_EJECUTADO_Y_COTA_DECIMAL
```

**Se sostiene:**
- §7.1, las inclusiones, las franjas y las extensiones;
- §7.2, los vértices y las orientaciones;
- §7.3, la retícula exterior con la fila delgada;
- §7.4, `Z'` y el ensamblado. Advierte además que exigir `Z'_hi > 0` en lugar de `Z'_lo > 0`
  es una relajación válida;
- §7.5, las dos curvas y las velocidades;
- la uniformidad: ninguna pieza de `run_box` usa un valor de una `lambda` concreta.

No encontró ningún contraejemplo al signo.

**Condiciones y cómo se atendieron:**

| condición | atendida |
|---|---|
| **IR ejecutado.** `fresh_ir` inspeccionaba un dispatcher recompilado, no el ejecutado, y la búsqueda de texto admitía la `define` de otra función | el control final se describe en §4: caché privada vacía, `cache_hits == 0`, librerías enlazadas con los cuerpos `prange`, `define` del nombre mangled propio y prueba negativa con un kernel de caché. Tercera ejecución completa, idéntica bit a bit, con `ok = True` |
| **Cota decimal.** El acta decía `drho/dt >= 0.0066481`, por encima del valor certificado `0.006648095…` | la nota muestra las cotas inferiores truncadas hacia abajo y las superiores redondeadas hacia arriba (§6). El mismo error, redondear cotas hacia el lado equivocado, apareció en la compuerta (`+0.00705`), en la tabla diagnóstica de la transferencia y en una cota superior de la transferencia. Se corrigió en las notas; las actas cerradas y los mensajes de commit quedan como estaban |

Precisión de ASTRA que se adopta: «cualquier `M` y `N`» significa cualquier par que permita
construir la retícula y superar sus comprobaciones.

**Límites:** una sola casa y una sola ronda, no un sanedrín. ASTRA no ejecutó nada.

## 9. Promoción

Decisión del PI del 2026-10-12, sobre el pase condicional de ASTRA con las dos condiciones
atendidas (`998811d`), y **sin** segunda casa. El PI sabe que es una auditoría más ligera que la
de la compuerta: una sola casa y una sola ronda.

```text
B2_GATE             = CERTIFIED_POSITIVE_AT_T0               (sin cambio)
B2_GATE_REAL_POINT  = B2_SIGN_TRANSFERRED_TO_REAL_MIDPOINT   (sin cambio)
B2.1                = B2.1_POSITIVE_DERIVATIVE               (antes INCONCLUSIVE_BY_BOUNDS)
B3                  = INCONCLUSIVE_BY_BOUNDS                 (sin cambio)
```

Alcance: `drho/dt >= +0.0066480` en todo `t ∈ [0.45, 0.55]`, en las dos lecturas de la curva.
`rho∘lambda` es estrictamente creciente en ese intervalo, y la malla congelada de B2.1 queda
ordenada estrictamente. **No** dice nada fuera de `[0.45, 0.55]`, ni sobre `phi`, ni sobre `n=3`,
ni sobre B3.

```text
PI: Nacho Martín              fecha: 2026-10-12
```

### Adenda 2026-10-12 — el control de IR, auditado en B3

El `executed_ir` de este verificador se escribió **después** de la auditoría de B2.1, para
atender su condición, y por tanto ningún auditor lo había visto. ASTRA lo revisó en las rondas
2 y 3 de la auditoría de B3 (`revisiones/2026-10-12-auditoria-b3/`):
- encontró cuatro huecos de cobertura y, después, el de las llamadas indirectas;
- se corrigieron con la clausura por sobrecarga y la regla de llamadas indirectas (§4);
- la evidencia es la de la nota de B3, §6.

La cuarta ejecución completa con el control final da las mismas `S_lo` bit a bit.
