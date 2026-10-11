# B2 — compuerta de `S` en `t0`: la representación de B1.5 no alcanza

**Fecha:** 2026-10-11
**Autorizado por:** el PI, con la regla enmendada y firmada
(`dev/B2_PROMOTION_RULE_AMENDMENT_2026-10-11.md`: éxito si `0 ∉` envolvente de `drho_dt`).
**Sonda:** `dev/explore_b2_gate_ideal_interval.py` — diagnóstico, no certificado. Sin artefactos de
verificación, sin sprinklings, guardarraíles intactos (`t0`, curva y puntos congelados; sin búsqueda).

```text
INTERVALO_IDEAL_DE_S(t0) = [-0.00336, +0.01125]      contiene cero
ANCHURA = HOLGURA ANGULAR (el error de integración es < 1e-5)
COMPUERTA = DETENIDA ANTES DE CONSTRUIR EL CERTIFICADO
REPRESENTACIÓN (H1a + H1b de B1.5) = AGOTADA EN t0
B2 = SIGUE BLOQUEADO;  B2.1 = INCONCLUSIVE_BY_BOUNDS (sin cambio)
OPCION_B (recostear M=16) = MISMO TECHO, S_ideal = [-0.00309, +0.01105]
```

---

## 1. Por qué se midió esto primero

La cadena de B1.5 descansa en dos desigualdades puntuales (B1.5 §7, H1a y H1b):

```text
p(b_line(x,y))  <=  h(x,y)  <=  p(a_CS(x,y))
```

Todo lo demás en esa cadena —polinomios para `p`, anclaje del perfil, envolventes por celdas,
redondeo dirigido— solo **ensancha**. Así que el mejor intervalo que cualquier versión certificada
de la cadena podría dar es el que resulta de integrar esas dos cotas **sin error de integración**.
Si ese intervalo ideal contiene cero, construir el certificado es gasto sin posibilidad de éxito.

Es el criterio en el que coincidieron las cuatro casas del sanedrín: un cero a resolución finita
detiene por presupuesto; un cero en el intervalo **ideal** agota la representación.

## 2. Resultado

`S = B' - 2 (Z'/Z) B` en `lambda(0.5) = (0.35, 0.9, 1.5, 0.7, 0.1)`, con las velocidades normales
corregidas (`v_n`: `+1.0`, `+0.4`, `+0.3`, `-0.2` para `U=-u_out`, `U=u_in`, `V=v0`, `V=v1`):

| orden | `rho` | `B'` | `2(Z'/Z)B` | `S` | `drho/dt` |
|---|---|---|---|---|---|
| 16 | [0.01966, 0.03087] | [0.00640, 0.01745] | [0.00621, 0.00975] | [-0.00335, 0.01124] | [-0.0172, 0.0579] |
| 24 | [0.01973, 0.03096] | [0.00642, 0.01747] | [0.00623, 0.00977] | [-0.00336, 0.01124] | [-0.0173, 0.0579] |
| 32 | [0.01975, 0.03099] | [0.00642, 0.01748] | [0.00624, 0.00978] | [-0.00336, 0.01125] | [-0.0173, 0.0579] |

`Z = 0.440556`, `Z' = +0.358274`. La tabla es estable a 1e-5 entre órdenes: **toda** la anchura es
holgura angular, nada es integración. El extremo inferior se queda corto en `0.00336`: para
excluir cero, la cota inferior de `B'` tendría que subir más de un 50 % (de 0.0064 a 0.0098) sin
que se mueva la superior de `B`.

Contribución de cada cara a `B'` (orden 32):

```text
U=-u_out  v_n=+1.0   [0.00395, 0.00693]
U=u_in    v_n=+0.4   [0.00287, 0.00549]
V=v0      v_n=+0.3   [0.00641, 0.00917]
V=v1      v_n=-0.2   [-0.00682, -0.00410]
```

La cara `V=v1` entra con signo negativo: allí la cota *superior* de `h` resta, y eso es lo que más
ensancha el intervalo.

## 3. Controles

- **`Z'`**: igual al valor por diferencias finitas, `+0.358274`.
- **Término de caras de `B'`**: fijando `h = p(b_line)` en todas partes, `dB_lo/dt` por diferencias
  finitas vale `0.009114` y la suma de caras `0.009133` (0.2 %, cuadratura junto a los bordes de
  orden, donde `h` tiene esquinas).
- **Coherencia con lo registrado**: el intervalo ideal de `rho`, `[0.0198, 0.0310]`, queda dentro
  de la envolvente de B2.1 en `t0`, `[0.0195, 0.0347]`, y es más estrecho, como debe ser: B2.1 usa
  una cota superior de `h` más burda que Cauchy–Schwarz.
- **Coherencia con el signo esperado**: el intervalo de `drho/dt`, `[-0.017, +0.058]`, contiene la
  pendiente que sugieren las envolventes de B2.1 (`~+0.015` a `+0.031`).

## 4. Qué significa y qué no

- **No** dice que `rho'(t0) = 0` ni que el signo sea dudoso. Dice que con la información puntual
  `b_line <= Delta_max <= a_CS` el signo no se puede certificar en `t0`, a ninguna resolución.
- **Por eso no se construyó el certificado con redondeo dirigido.** La jornada presupuestada por el
  sanedrín habría producido, en el mejor caso, un intervalo más ancho que este.
- Lo que haría falta es una **representación más fina** de `Delta_max`, no más resolución. Las dos
  vías naturales serían una cota inferior por una familia de curvas causales explícitas más rica
  que la recta (p. ej. quebradas, tomando el máximo), o una cota superior mejor que Cauchy–Schwarz.
  Ninguna está autorizada ni evaluada aquí, y las dos son representaciones nuevas, no refinamiento:
  necesitan decisión del PI.
- **Opción (B), recostear `M=16`: comprobado, hereda el mismo techo.** El certificado de B2 iba a
  usar las cotas angulares de B1.4 con el kernel corregido
  (`B1/verify_certified_rho_frozen_pair.py::rho_bounds`): superior **igual** a `a_CS` (con `V>0`
  el máximo de `q` está siempre en `Uy`) e inferior el máximo sobre **19 quebradas** de dos
  tramos (`beta` de 0.05 a 0.95, la recta es `beta=0.5`). Con esa representación, sin error de
  integración:

  ```text
  S_ideal(t0) = [-0.00309, +0.01105]      (orden 16 y 24 iguales a 1e-5)
  ```

  Las quebradas solo suben el extremo inferior de `-0.00336` a `-0.00309`. Una partición en cajas
  no puede estrechar lo que ya es holgura de la representación: **(B) no puede excluir cero en
  `t0`**, a ningún `M`. La opción queda resuelta en negativo sin gastar en ella.

## 5. Dónde está la holgura, y qué representación haría falta

Colapsando la banda a cada uno de sus extremos (diagnóstico, orden 16):

```text
h = p(b_line) en todas partes   ->  S = +0.00292
h = p(a_CS)   en todas partes   ->  S = +0.00498
banda completa [p(b_line), p(a_CS)] ->  S in [-0.00336, +0.01124]
```

Ninguna de las dos cotas, tomada como si fuera exacta, da signo dudoso: las dos dan `S > 0`, lo
cual es coherente con `rho' > 0` pero **no es una prueba** (la `h` verdadera no es ninguna de las
dos). El cero entra solo por la **mezcla adversa**: cota inferior en las caras que suman, superior
en `B` y en la cara `V=v1`, que resta. Como `S` es afín en la banda, para excluir cero la banda de
`h` tendría que estrecharse aproximadamente a la mitad (factor ~1.9 alrededor de su punto medio,
estimación lineal sin certificar).

Eso fija qué tendría que tener una representación nueva para merecer una compuerta certificada:

1. una banda puntual de `Delta_max` alrededor de la mitad de ancha que `[b_line, a_CS]`, **o**
2. una representación que **acople** `h` en caras y volumen, de modo que no se pueda escoger el
   extremo desfavorable en cada sitio por separado.

Las quebradas de dos tramos no son la vía: cubren un 8 % del déficit. Qué lado de la banda
conviene atacar no está medido aquí. Ninguna de las dos vías está autorizada: son decisión del PI.
