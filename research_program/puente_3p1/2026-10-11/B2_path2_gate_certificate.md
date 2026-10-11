# B2 — certificado de la compuerta en `t0`: `drho/dt > 0` con redondeo dirigido

> **STATUS: `CERTIFICATE_FROZEN / PENDING_INDEPENDENT_AUDIT`.** El objeto se congela y se sube
> **antes** de auditarlo, como B1.5 (§11 de su nota). No se promociona a resultado establecido
> hasta que una auditoría independiente —de otra familia de modelos— lo dé por bueno.
> Guardarraíles de B2 intactos: `no_new_path`, `no_new_t0`, `no_new_points`, `no_search`,
> `no_adjustment`.

**Fecha:** 2026-10-11 · **Verificador:** `verify_b2_path2_gate_certificate.py` →
`verification_b2_path2_gate_certificate.json` · **Regla:**
`dev/B2_PROMOTION_RULE_AMENDMENT_2026-10-11.md` (firmada por el PI).

```text
S_lo = +0.0013679385529351228          (S = B' − 2 (Z'/Z) B, en lambda(0.5))
drho/dt(t0) >= +0.007047462946767621    enclosure [0.00704746, +inf), excluye cero
TERMINAL = B2_CORRECTED_POSITIVE        (pendiente de auditoría)
```

---

## 1. Qué establece y qué no

Establece, bajo las hipótesis de §6, que la derivada direccional de `rho` en el punto congelado
`lambda* = lambda(0.5)`, a lo largo de la dirección congelada `d = lambda1 − lambda0`, es
**estrictamente positiva**. Con eso, la ley `n=2` distingue localmente los puntos de la curva
congelada en `t0`: identificabilidad local en el sentido de la función inversa, **solo en `t0`**.

**No** establece:

- monotonía de `rho` en un vecindario de `t0` ni en la malla de B2.1 (`B2.1` sigue
  `INCONCLUSIVE_BY_BOUNDS`; el control en vecindario es otra pregunta);
- identificabilidad global, ni de `phi` fuera de esta curva, ni `n=3`;
- nada sobre B3, que sigue inconcluso tras `dev/B2_2_SIGN_BUG_2026-10-11.md`.

## 2. Cadena

1. **Representación** (`dev/B2_NEW_REPRESENTATION_2026-10-11.md`). `Delta_max` (B1.2 §2) es la
   separación temporal de la métrica 2D `q(UV)² dU dV`.
2. **Desigualdad triangular inversa.** Con `x ∈ P` e `y ∈ Q`:
   `Delta(P_top, Q_bot) <= Delta(x,y) <= Delta(P_bot, Q_top)` cuando los órdenes lo permiten. Cada
   par de celdas se acota con **un** par de esquinas de la retícula.
3. **Cota inferior entre esquinas.** El presupuesto de la recta (B1.2 LB, hipótesis H1b de B1.5),
   como suma de Riemann inferior de `q` sobre el rango intervalar de `w(tau)` en cada celda de `tau`.
4. **Cota superior entre esquinas.** `min(Cauchy–Schwarz, inf_c calibración)`.
   - Cauchy–Schwarz es B1.2 UB, que es H1a de B1.5.
   - La calibración es `W_c = c ln V + Phi_c(UV)`, con `Phi_c' = F/(2(c + sqrt(c² + F w)))`. Por
     AM-GM, `dW_c >= dtau` a lo largo de toda curva causal futura, siempre que `c` sea válido en
     el rectángulo causal.
   - **Cada `c` da una cota válida por separado**, así que la rejilla de `c` no se certifica.
5. **Ensamblado** (solo `S_lo`). `B'_lo` usa la cota inferior de `H` en las caras con `v_n > 0` y
   la superior en `V=v1`; `B_hi = 2 sum W_P W_Q p(UB)`;
   `S_lo = B'_lo − (2 Z'_hi/Z_lo) B_hi`. Velocidades normales con la normal exterior
   (`dev/B2_2_SIGN_BUG_2026-10-11.md`).

## 3. Aritmética

| objeto | tratamiento |
|---|---|
| operaciones binary64 (también dentro de numba) | `np.nextafter` un ulp hacia afuera tras cada operación |
| `q`, `G` | tablas certificadas de 65 537 nodos (con `w=0` como nodo) construidas con la capa escalar **auditada** de B1.5 (`s_encl`/`q_encl`/`G_encl`, `mpmath.iv`, sin Lambert W); cada consulta es rigurosa solo por monotonía (`q` creciente; `G` creciente en `w<=0` y decreciente en `w>=0`) |
| `p(b) = (1−cos min(b,pi))/2` | tabla certificada de 131 073 nodos en `[0, 3.2]`, `mpmath.iv`; `p` no decreciente |
| `ln V` en los nodos | `mpmath.iv` |
| velocidades `v_n` | racionales exactos (`Fraction`) de los binary64 de `lambda0`, `lambda1` |
| `Phi_c` | integrandos acotados por celda de tabla (`c<0` sin cancelación); sumas prefijas dirigidas por ambos lados |
| pesos `W_P`, caras, `Z`, `Z'` | subceldas `8×8` / `8` con envolventes de `G`; teselado con extremos exactos |
| sumas | secuenciales dirigidas |
| índices de tabla | comparaciones exactas de binary64 |
| compilación | se comprueba que el IR de LLVM de los 19 kernels no tiene `fast`/`contract`/`reassoc`/`fma`; el control está probado por mutación (un kernel `fastmath` es detectado) y exige que cada kernel tenga firma compilada (la primera versión pasaba en vacío por 11 kernels auxiliares: corregido) |

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
separación de cero empieza en `M = 64`. Tiempo: 19 s (14 s las tablas), 2.6 GB.

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

- **H1.** De B1.2 §2: `Delta_max = min(pi, sup L[U])` sobre curvas monótonas, y su lectura como
  separación temporal de `q² dU dV`. De ahí salen la cota de la recta (H1b), la de Cauchy–Schwarz
  (H1a), la desigualdad triangular inversa y la calibración. **Las dos últimas son nuevas y son lo
  primero que debe auditarse.**
- **H2.** `rho = B/Z²`, con `B = ∫∫_{K×K} w w h` y `h(x,y) = p(Delta_max)` simétrica (B1.5 §2).
- **H3.** Transporte de Reynolds para `B(t)` con `h` acotada y continua: `B' = 2∫_{∂K} w v_n H`.
  Contrastado numéricamente (`dev/B2_GATE_RESULT_2026-10-11.md` §3, 0.2 %), no demostrado aquí.
- **H4.** IEEE-754 binary64 correctamente redondeado, `mpmath.iv` para la capa escalar, y
  compilación sin `fast-math` ni contracción (comprobado en el IR, §3).
- **H5. Convención del punto.** El punto certificado es el binary64 `lambda* = path(0.5)` que
  evalúan los scripts congelados de B2, y la dirección es `d = L1 − L0` exacta. Es la misma
  convención implícita de B1.5, que certificó los binary64 de `lambda1`. Se declara aquí
  explícitamente.

## 7. Qué debe mirar la auditoría

1. La calibración: la desigualdad AM-GM, la elección de la raíz menor, la validez en el
   rectángulo y el tratamiento de `c < 0`.
2. La desigualdad triangular inversa para `Delta_max` con el tope `min(pi, ·)`: el tope conserva
   la cota superior y la inferior porque `p` es no decreciente y vale 1 a partir de `pi`.
3. Qué cota va a cada término de `S_lo`, y los signos de `v_n`.
4. Los índices de tabla y las direcciones de redondeo de `ub_table`, `lb_rows`, `face_h` y
   `phi_prefix`.
5. H3 y H5.
