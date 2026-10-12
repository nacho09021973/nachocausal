# B2 — certificado de la compuerta en `t0`: `drho/dt > 0` con redondeo dirigido

> **STATUS: `CERTIFICATE_FROZEN / AUDITED — AUDIT_PASS_CONDITIONAL_B15_DEPENDENCIES`, con la
> condición comprobada después (§8). NO promocionado: la promoción la decide el PI.** El objeto se
> congeló y se subió **antes** de auditarlo, como B1.5 (§11 de su nota). Lo auditó el sanedrín
> del 2026-10-11 (cinco casas de cinco familias de modelos), que no encontró ningún fallo en
> el número. Esta revisión de la nota solo corrige el texto según su veredicto; el verificador y
> el JSON son los de `7909c0e`.
> Guardarraíles de B2 intactos: `no_new_path`, `no_new_t0`, `no_new_points`, `no_search`,
> `no_adjustment`. La enmienda sigue vigente: excluir cero en `t0` **no** emite un terminal de
> B2.1.

**Fecha:** 2026-10-11 (texto corregido el 2026-10-12 a partir de `beaf6af`) · **Verificador:**
`verify_b2_path2_gate_certificate.py` → `verification_b2_path2_gate_certificate.json` ·
**Regla:** `dev/B2_PROMOTION_RULE_AMENDMENT_2026-10-11.md` (firmada por el PI).

```text
S_lo = +0.0013679385529351228          (S = B' − 2 (Z'/Z) B, en lambda(0.5))
drho/dt(t0) >= +0.007047462946767621    enclosure [0.00704746, +inf), excluye cero
TERMINAL = B2_CORRECTED_POSITIVE        (auditado con pase condicional; sin promocionar)
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
