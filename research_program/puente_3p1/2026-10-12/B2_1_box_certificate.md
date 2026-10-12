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
