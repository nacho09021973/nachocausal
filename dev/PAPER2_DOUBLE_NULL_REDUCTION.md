# Paper II (1+1D) — Reducción nula doble del generador congelado

STATUS: PRUEBA_ANALITICA / NOTAS_DE_EXPLORACION / NO_ES_PREREGISTRO / NO_SELLA_NADA
DATE: 2026-09-08
CAPA: dev/. No modifica `nachocausal/`. El seal queda intacto.

Ejecuta el **paso F** del informe de estado del puente 1+1D. Objeto: demostrar que
la relación causal que calcula `nachocausal/generator.py:88-133` con `kind="BH"`
es, **en el exterior y en el interior por separado**, el orden componente a
componente en un par de coordenadas nulas, y exhibir el término exacto que
impide pegar ambas cartas a través de `r = r_S`.

Asignación editorial: esto es **Paper II** (puente matemático 1+1D). El material
3+1D vive en [[PAPER3_3P1_SCALE_NOTES]].

---

## 0. Qué se prueba y qué no

**Se prueba** (deductivamente, y se verifica contra el código):

- P1. Las dos direcciones nulas que el código fija, más la declaración `det g = -1`
  del propio repo, determinan la métrica **unívocamente**; `func` no es libre.
- P2. `func` **no es la coordenada tortuga** `r_* = r + r_S ln(|r-r_S|/r_S)`. Es la
  coordenada nula saliente del chart `t*`, con un factor `2 r_S`, y está forzada.
- P3. Reducción nula doble exacta, bloque a bloque (Teorema 1, cuatro casos).
- P4. El guardián `earlier` (`t_j < t_i`) es **redundante** fuera de la diagonal.
- P5. Forma normal de Hammersley: en coordenadas nulas el sprinkling es un Poisson
  planar de intensidad `mu = rho·|f|/2` con `f = 1 - r_S/r`, y `ds^2 = |f| dv dw`.
- P6. De P5 **más el teorema externo de Deuschel–Zeitouni** se deriva
  `L(i)/sqrt(2 rho) -> tau_max(x)`. Esta pieza es **condicional**: Deuschel–Zeitouni
  no está en `biblioteca/` y no se demuestra aquí. Y es **bloque a bloque**: vale
  para `F_x` contenido enteramente en el exterior o enteramente en el interior, no
  para futuros que crucen el horizonte.

**No se prueba**: nada que cruce `r = r_S`. §7 aísla la obstrucción, que resulta
ser cuádruple y no una molestia técnica.

---

## 1. El chart está forzado por el código

El código fija dos condiciones de frontera nula. Con `C[i,j] = (j precede a i)`,
`dt = t_i - t_j`, `t_in = r_j - r_i`, `t_out = func_i - func_j`:

```text
rama entrante (b2):  dt = t_in    <=>   t_i + r_i = t_j + r_j
rama saliente (b3):  dt = t_out   <=>   t_i - func_i = t_j - func_j
```

Es decir, los rayos nulos del chart `t*` cumplen

```text
entrante:  dt*/dr = -1
saliente:  dt*/dr = R'(r),      R(r) := func(r) = r + 2 r_S ln(|r-r_S|/r_S).
```

**Lema 1.** `R'(r) = (r + r_S)/(r - r_S) = (2-f)/f`, con `f := 1 - r_S/r`.

*Prueba.* Derivación directa; verificado simbólicamente (§9).

**Lema 2 (la métrica está determinada).** En 2D una métrica lorentziana queda
fijada por sus dos direcciones nulas salvo factor conforme. Escribiendo
`g = Lambda·(dt* + dr)(dt* - R' dr)` se obtiene

```text
det g = -Lambda^2 (1 + R')^2 / 4 = -Lambda^2 r^2/(r-r_S)^2,
```

de modo que **`det g = -1` fuerza `Lambda = ±f`**, y con la orientación temporal
correcta

```text
ds^2 = f dt*^2 - 2(1-f) dt* dr + (f-2) dr^2,      det g = -1.
```

*Prueba.* Cálculo directo; verificado simbólicamente (§9).

**Corolario 1 (`func` no es la tortuga).** La tortuga estándar es
`r_* = r + r_S ln(|r-r_S|/r_S)`, con `r_*' = 1/f = r/(r-r_S)`. Aquí
`R' = (2-f)/f = (r+r_S)/(r-r_S)`, luego `R != r_*`: difieren en el coeficiente
del logaritmo por un factor 2. La confusión es natural y da un chart equivocado.
`R` es la coordenada nula **saliente del chart `t*`**, no la tortuga de
Schwarzschild.

Esto también cierra la coherencia interna del generador: la afirmación
`det g = -1` de su docstring (`nachocausal/generator.py:10-12`) no es un añadido,
es **equivalente** a la elección de `func`.

---

## 2. Las dos coordenadas nulas y su orientación

```text
v(t*,r) := t* + r                (nula entrante)
U(t*,r) := t* - R(r)             (nula saliente)
W       := -U = R(r) - t*
psi(r)  := r + R(r),             psi'(r) = 2r/(r - r_S)
```

Regiones: `D_ext = {r > r_S}`, `D_int = {0 < r < r_S}`.

| | `R'` | `psi'` | orientación futura |
|---|---|---|---|
| `D_ext` | `> 0` (R crece) | `> 0` | `v` y `U` **crecen** |
| `D_int` | `< 0` (R decrece) | `< 0` | `v` y `W` **crecen** |

Se define la **coordenada saliente orientada al futuro**

```text
w := U   en D_ext,        w := W   en D_int.
```

Identidad útil en ambos bloques:

```text
psi(r) = v - U  (exterior)   =   v + W  (interior).
```

`psi` es biyectiva en cada bloque: `psi: D_ext -> (-inf, +inf)` creciente, y
`psi: D_int -> (-inf, 0)` decreciente, con `psi(0+) = 0` y `psi(r_S∓) = -inf`.

---

## 3. Teorema 1 — reducción nula doble

> **Teorema 1.** Sean `p_j = (t_j, r_j)` y `p_i = (t_i, r_i)` distintos, con
> `r_i, r_j != r_S`. La relación calculada por `past_matrix_fast(·, "BH", r_S)`
> satisface exactamente:
>
> **(a) Bloque exterior** (`r_i, r_j > r_S`):
> `j ≺ i  <=>  v_j <= v_i  y  U_j <= U_i`.
>
> **(b) Bloque interior** (`r_i, r_j < r_S`):
> `j ≺ i  <=>  v_j <= v_i  y  W_j <= W_i`.
>
> **(c) Cruce hacia dentro** (`r_j > r_S > r_i`):
> `j ≺ i  <=>  v_j <= v_i`.   *(la coordenada saliente no interviene)*
>
> **(d) Cruce hacia fuera** (`r_i > r_S > r_j`): **nunca**.
>
> En (a) y (b) la relación es, por tanto, el **orden componente a componente**
> en `(v, w)`.

### Prueba

Traducción previa de las ramas del código (identidades elementales):

```text
dt >= t_in            <=>   v_i >= v_j
dt >= t_out           <=>   U_i >= U_j
t_out >= dt           <=>   U_i <= U_j   <=>   W_i >= W_j
```

Las ramas quedan: `b2` pide `v_i >= v_j`; `b3` pide `U_i >= U_j`; `b1` pide
`W_i >= W_j` **y** `v_i >= v_j`; el resto devuelve `False`. La cobertura es
exhaustiva y disjunta salvo en `r_j = r_S` (medida nula; `np.where` evalúa `b1`
primero).

**(a).** Dos subcasos.

*`r_i <= r_j`* — se aplica `b2`. `R` crece en `D_ext`, luego `R_i <= R_j` y
`U_i - U_j = dt - (R_i - R_j) >= dt`. Si `v_i >= v_j` entonces
`dt >= r_j - r_i >= 0`, con igualdad sólo si `p_i = p_j`; luego `dt > 0` y
`U_i > U_j`. Recíprocamente, si el código devuelve `True` vale `v_i >= v_j`, y
`U_i >= U_j` sale gratis por lo anterior. Ambas condiciones equivalen a la del
código.

*`r_i > r_j`* — se aplica `b3`. `v_i - v_j = dt + (r_i - r_j) > dt`. Si
`U_i >= U_j` entonces `dt >= R_i - R_j > 0` (R estrictamente creciente), luego
`dt > 0` y `v_i > v_j`. Recíproco análogo.

En ambos subcasos la conjunción `{v_i >= v_j} ∧ {U_i >= U_j}` coincide con lo que
el código evalúa. ∎(a)

**(b).** Supóngase `v_i >= v_j` y `W_i >= W_j`. Sumando y usando
`psi(r) = v + W`:

```text
psi(r_i) = v_i + W_i >= v_j + W_j = psi(r_j),
```

y como `psi` **decrece** en `D_int`, se sigue `r_i <= r_j`. Luego la rama
aplicable es `b1`, cuyas dos condiciones son exactamente `W_i >= W_j` y
`v_i >= v_j`. Además `dt >= r_j - r_i >= 0`, con igualdad sólo si `p_i = p_j`,
así que `t_i > t_j`. Recíprocamente, si el código devuelve `True` por `b1`, ambas
condiciones se leen directamente. ∎(b)

Obsérvese que aquí **ninguna de las dos es redundante**: el código comprueba las
dos, y debe hacerlo.

**(c).** Con `r_j > r_S > r_i` se tiene `r_j > r_i`, luego se aplica `b2` y la
única condición es `v_i >= v_j` (y `dt >= r_j - r_i > 0` es automático). Que ésta
sea además la relación causal correcta se ve así: el rayo entrante desde `p_j`
es `v = v_j` y penetra el horizonte; un punto `p` de ese rayo a radio
`r_0 < r_S` tiene `W_p = psi(r_0) - v_j`. Como `psi(r_0) -> -inf` cuando
`r_0 -> r_S^-`, para cualquier interior `p_i` con `v_i >= v_j` se puede elegir
`r_0` con `W_p <= W_i`; por (b), `p ≺ p_i`, y por transitividad `p_j ≺ p_i`. El
recíproco es que `v` crece a lo largo de toda curva causal futura. ∎(c)

**(d).** Ninguna rama se activa, luego el código devuelve `False`. Es correcto:
en `D_int` las dos pendientes nulas dan `dr/dt* = -1` y
`dr/dt* = (r - r_S)/(r + r_S) ∈ (-1, 0)`, ambas **estrictamente negativas**, de
modo que `r` decrece estrictamente a lo largo de cualquier curva causal futura y
`r_S` no puede recruzarse hacia fuera. ∎(d)

> **Corolario 2 (el guardián `earlier` es redundante).** Para puntos distintos,
> las condiciones nulas de (a)–(c) implican `t_i > t_j`. El factor
> `earlier = (t_j < t_i)` del código sólo excluye la diagonal, que `fill_diagonal`
> ya elimina. No hay información causal en él.

> **Corolario 3 (convexidad causal de los bloques).** Por (d), toda curva causal
> entre dos puntos exteriores permanece exterior, y entre dos interiores
> permanece interior. Ambos bloques son **causalmente convexos**, que es
> justamente la hipótesis bajo la cual el orden componente a componente en un
> chart nulo doble coincide con la relación causal global restringida al bloque.
> Sin este corolario, (a) y (b) serían sólo condiciones necesarias.

---

## 4. Teorema 2 — forma normal de Hammersley

> **Teorema 2.** En cada bloque, escrito en `(v, w)`:
>
> (i) `ds^2 = |f| dv dw`, con `f = 1 - r_S/r`;
> (ii) `dt* dr = (|f|/2) dv dw`, luego un sprinkling de Poisson de intensidad
> `rho` respecto del volumen es, en coordenadas nulas, un Poisson planar de
> intensidad **`mu(v,w) = rho·|f(r)|/2`**;
> (iii) el orden causal es el orden componente a componente en `(v,w)`.

> **Alcance del Teorema 2 y del Corolario 4.** (i)–(iii) son un cambio de
> variables y no dependen de ningún resultado externo, pero están enunciados
> **en cada bloque por separado**: la carta `(v, w)` no existe globalmente (O1).
> El Corolario 4, que es donde aparece la ley de altura, está además
> **condicionado al teorema externo de Deuschel–Zeitouni**, ausente de
> `biblioteca/` y no demostrado aquí. Tal como está, el paquete cubre
> `F_x ⊂ D_ext` o `F_x ⊂ D_int`, y **no** cubre futuros truncados que crucen
> `r = r_S`.

*Prueba.* (iii) es el Teorema 1. Para (ii), el jacobiano es
`det ∂(v,U)/∂(t*,r) = -(1 + R') = -2/f`, luego `|J| = 2/|f|`. Como `det g = -1`,
el elemento de volumen es `dvol = dt* dr` — que es exactamente lo que muestrea
`numpy_sprinkle` (uniforme en la caja), de modo que la intensidad respecto del
volumen natural es la misma `rho`. Para (i), en un chart nulo doble
`g_vv = g_ww = 0` y `det g = -(g_vw)^2`; con `det g = -1/J^2` se obtiene
`g_vw = |f|/2` y `ds^2 = 2 g_vw dv dw = |f| dv dw`. Verificado simbólicamente
(§9). ∎

**Comprobación de consistencia.** Con `r_S -> 0`, `f -> 1`, `mu -> rho/2`, y
`ds^2 -> dv dw`: exactamente el diccionario Minkowski (`dt dr = ½ du dv`).

### Corolario 4 — la ley de altura, derivada

Sea `F_x` contenido en un solo bloque. El problema «cadena futura máxima» es
ahora literalmente el problema de Hammersley con densidad variable. Aplicando el
límite variacional (Deuschel–Zeitouni; §8, insumo externo),

```text
L / sqrt(mu)  ->  2 sup_gamma ∫ sqrt(dv dw)
```

y sustituyendo `mu = rho|f|/2`:

```text
L  ->  2 sqrt(rho/2) · sup_gamma ∫ sqrt(|f| dv dw)
    =  sqrt(2 rho) · sup_gamma ∫ dtau
    =  sqrt(2 rho) · tau_max(x).
```

El supremo de `∫ dtau` sobre curvas causales futuras es, por definición, la
distancia lorentziana máxima alcanzable dentro de `F_x`. **La constante
`sqrt(2 rho)` y la identificación del límite con el tiempo propio no se postulan:
salen del jacobiano y del factor conforme.** En el caso intervalo,
`tau_max = tau`, `A = tau^2/2`, y `L -> 2 sqrt(rho A)`, es decir `m_2 = 2`.

Esto convierte el punto (ii) del enunciado candidato del Paper II en un teorema
**condicionado a un único insumo externo** — Deuschel–Zeitouni, que no está en
`biblioteca/` y no se demuestra aquí — y **válido sólo dentro de un bloque**. No
es un enunciado sobre `F_x` que cruce el horizonte.

---

## 5. Concordancia numérica con lo ya medido

Las tablas del informe anterior (lectura aritmética de artefactos comprometidos,
sin re-ejecutar nada) dan `tau_hat = <L>/sqrt(2 rho)`:

| dataset | geometría | `tau_max` geométrico | `tau_hat` (MINK, rho más alta) |
|---|---|---|---|
| `dev/rvar_egs_falsification_test_result.json` | caja alta, `T=6` | 6.0 | 5.922 (98.7 %) |
| `evidence/new_geometry_20260719/per_seed_metrics.csv` (sellado) | cuadrada, `T=2.4` | 2.4 | 2.322 (96.8 %) |

Convergencia por debajo y monótona en `rho`, como corresponde a una corrección
de tamaño finito. El Corolario 4 explica *por qué* la constante es `sqrt(2 rho)`
y no otra.

---

## 6. Consecuencia inmediata: por qué falló el sort saliente

`dev/PR003_RVAR_STRUCTURE_PROBE_REPORT.md:33-36` midió que ordenar por la
coordenada entrante `p = t+r` da **0 violaciones** de propiedad de intervalo
(24/24), mientras que la saliente **falla con 5000+ violaciones**. El Teorema 1
lo explica exactamente:

- `v = t + r` es una coordenada nula **global**, monótona al futuro en ambos
  bloques y en el cruce (caso (c)). Ordenar por ella es siempre lícito.
- La saliente **cambia de orientación** al cruzar `r_S`: crece al futuro fuera
  (`U`), decrece al futuro dentro (`-W`). Un único sort saliente mezcla dos
  orientaciones opuestas. Las violaciones no eran ruido numérico: son el
  contenido del caso (b).

---

## 7. La obstrucción en `r = r_S`, aislada

La reducción es exacta bloque a bloque y **no se puede pegar**. Cuatro hechos
independientes, cada uno suficiente por sí solo.

Antes de enunciarlos, una distinción que no debe perderse:

- **O1–O3 son obstrucciones de la forma normal `(v, w)`** inducida por el
  generador, es decir, del cambio de variables — no de la geometría ni del
  proceso puntual. En el chart original `(t*, r)` con `det g = -1` el horizonte
  `r = r_S` es **perfectamente regular**: la métrica es suave allí, el volumen es
  `dt* dr`, y el sprinkling de Poisson tiene intensidad `rho` constante a través
  de `r_S`. Lo que se degenera es la carta nula, no la física.
- **O4 es un enunciado sobre la propia relación causal**, no sobre la carta. Se
  enuncia, eso sí, en el embedding (§7.1).

**O1 — la carta no es global (falta de inyectividad).** La lectura de `r` a
partir de `(v, w)` **cambia de fórmula** al cruzar: `psi(r) = v - w` en el
exterior, `psi(r) = v + w` en el interior. Un par `(v, w)` desnudo, sin la
etiqueta del bloque, no determina `r`. Y aun conociendo la etiqueta, los rangos
se solapan: `psi(D_int) = (-inf, 0)` está **contenido** en `psi(D_ext) = R`.
Luego la etiqueta interior/exterior es información **extra**, no derivable de
`(v, w)`: ningún par de coordenadas nulas de este chart separa los dos bloques.

**O2 — el horizonte está en el infinito de coordenadas *de la carta nula*.**
`R(r) -> -inf` cuando `r -> r_S` **por ambos lados**, luego `|U|, |W| -> inf`. La
superficie `r = r_S` no es una curva del plano `(v, w)`: es su frontera al
infinito. Un problema variacional sobre una región que la toca no está planteado
sobre un dominio acotado.

Precisión: esto es una propiedad de `(v, w)`, no del espaciotiempo. En `(t*, r)`
el horizonte está a distancia coordenada finita y la métrica es regular
(`det g = -1` en todo el dominio). La divergencia procede de `R' = (2-f)/f`, que
estalla en `f = 0`.

**O3 — la densidad de la forma normal se anula allí.** `mu = rho|f|/2 -> 0`
cuando `r -> r_S`. En la forma normal de Hammersley el horizonte es una **línea
de densidad nula**, y los teoremas de límite variacional disponibles piden
densidad acotada inferiormente en el dominio.

Precisión, y es importante no leerlo al revés: **la densidad física del
sprinkling no desaparece.** El proceso es Poisson de intensidad `rho` uniforme
respecto de `dvol = dt* dr`, y `rho` no depende de `r`; el número esperado de
elementos en cualquier vecindad del horizonte es el mismo que en cualquier otra
región de igual volumen. El factor `|f|/2` es el **jacobiano** `dt* dr / dv dw`,
que degenera porque la carta nula estira el horizonte al infinito (O2). `mu -> 0`
es una afirmación sobre densidad **por unidad de `dv dw`**, no sobre elementos
por unidad de volumen.

**O4 — el cruce sólo lo decide `v`.** Por el caso (c), toda relación causal que
atraviesa el horizonte se decide con la coordenada entrante **sola**. La
coordenada saliente no transporta información a través de `r_S`. Los dos
problemas de Hammersley no se acoplan por su par de coordenadas: se acoplan por
un único canal unidireccional.

### 7.1 Estatus de O4: exacto en el embedding, no todavía intrínseco

O4 es una **caracterización exacta de la relación cruzada**, y como tal es un
resultado firme: por el caso (c) del Teorema 1, `j ≺ i` con `r_j > r_S > r_i`
equivale a `v_j <= v_i`, sin ninguna condición sobre la coordenada saliente.

Pero está enunciado **en el embedding**. Tanto `v = t* + r` como la partición
`r ≷ r_S` que separa los cuatro casos son funciones de las coordenadas ocultas.
O4 dice que *si* se conoce el embedding, la relación cruzada colapsa a una sola
coordenada.

**Su reformulación intrínseca en lenguaje de posets queda ABIERTA.** No se afirma
aquí que exista un invariante de orden que detecte ese colapso, ni que «colapsar
un canal de dos coordenadas a uno» tenga una imagen order-only. Leerlo como una
versión order-only de *el orden recuerda pero no define* sería exactamente el
error que la regla fundacional del repo prohíbe: el embedding puntúa, nunca
define el observable. Convertir O4 en un enunciado sobre `C` solo —o probar que
no se puede— es trabajo pendiente, no un corolario de este documento.

---

## 8. Qué queda abierto

| Pieza | Estado tras este documento |
|---|---|
| Reducción nula doble, bloque a bloque | **PROBADA** (Teorema 1), verificada contra el código |
| `func` forzada por `det g = -1` | **PROBADA** (Lema 2, Corolario 1) |
| Forma normal de Hammersley, `mu = rho\|f\|/2` | **PROBADA** (Teorema 2) |
| `L -> sqrt(2 rho) tau_max` **dentro de un bloque** | **PROBADA condicionalmente** — falta Deuschel–Zeitouni, ausente de `biblioteca/` |
| `V/rho -> A` | elemental (Campbell/Slivnyak); pendiente el término de borde |
| Lo anterior para `F_x` que **cruza** el horizonte | **ABIERTO** — O1–O4 |
| Reformulación intrínseca (order-only) de O4 | **ABIERTA** — §7.1; O4 es hoy un enunciado en el embedding |
| Efectos de borde de caja (minimales) | **ABIERTO** — Madsen concede que la capa excluida no encoge con `rho` |

Insumo externo único e identificado: un teorema de límite variacional tipo
Hammersley para densidad variable en región general (Deuschel–Zeitouni 1995,
*Limiting curves for i.i.d. records*). **No está en `biblioteca/`.** Adquirirlo es
el siguiente paso barato y de mayor apalancamiento.

Para el caso que cruza el horizonte hacen falta, además, o bien una versión que
admita densidad que se anula sobre una curva interior (O3), o bien un lema de
pegado que descomponga `sup_gamma` en los dos bloques usando O4.

---

## 9. Verificación

`dev/verify_double_null_reduction.py` hace dos cosas, ninguna estadística:

1. **Cross-check algebraico** del Teorema 1 contra el `past_matrix_fast`
   congelado, sobre conjuntos de puntos deterministas en seis regímenes
   (caja congelada, dominio ancho, sólo exterior, sólo interior, pegado al
   horizonte con `|r-r_S|` hasta `1e-9`, y un `r_S` distinto).
   Resultado: **0 desajustes en 2 090 000 pares ordenados**.
2. **Verificación simbólica** (sympy) de `R' = (2-f)/f`, `det g = -1` con
   `Lambda = f`, `det ∂(v,U)/∂(t*,r) = -2/f`, `dt* dr = (|f|/2) dv dU` y
   `psi' = 2r/(r-r_S)`.

Sale con código 0 si y sólo si todo pasa. No modifica `nachocausal/`; sólo
importa `past_matrix_fast` y lo evalúa.

### Registro de ejecución

```text
fecha    : 2026-09-08
HEAD     : ed56e91
comando  : python3 dev/verify_double_null_reduction.py
salida   : ALL CHECKS PASS (2090000 ordered pairs compared, 0 mismatches;
           0 symbolic failures)
exit     : 0
```

Seis regímenes en verde (caja congelada, dominio ancho, sólo exterior, sólo
interior, `|r-r_S|` hasta `1e-9`, `r_S = 2.0`) y las ocho identidades simbólicas
en verde. `nachocausal/` no fue tocado: el verificador sólo lo importa.
