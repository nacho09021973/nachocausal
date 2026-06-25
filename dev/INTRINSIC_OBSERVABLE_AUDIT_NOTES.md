# Auditoría: ¿el observable de horizonte sellado es un evento intrínseco de una historia causal? (dev, NOTA CONCEPTUAL — NO es un resultado)

> **Naturaleza de esta nota.** Auditoría conceptual de admisibilidad intrínseca. **No** ejecuta código,
> **no** quema semillas, **no** toca el path sellado, **no** abre prereg, **no** propone implementación.
> No autoriza dinámica cuántica ni coarse-graining cuántico. Su única salida es un veredicto de
> admisibilidad y un siguiente paso *reversible* (definición/prueba en papel).
>
> Procedencia: HEAD `fafd880`, branch `main`, `make verify-seal` = `6e2c3888…` (confirmado ANTES de
> escribir; esta nota no corre código sellado). Path sellado `nachocausal/` intacto.
>
> **Tres cosas que esta nota mantiene SEPARADAS en todo momento (no se borran):**
> 1. **OBS-1** — observable *order-only sobre una historia individual* (un causal set concreto).
> 2. **CG-2** — *coarse-graining de un conjunto de historias* (una medida sobre `C`).
> 3. **DEC-3** — *funcional de decoherencia / medida cuántica*.
> El pipeline actual vive enteramente en OBS-1 (de hecho, en un OBS-1 *con gemelo MINK*, ver §4). CG-2 y
> DEC-3 **no existen** en el repo y esta nota no los construye.

---

## 1. Pregunta exacta (falsable)

> ¿Existe, con los ingredientes **actuales** del pipeline, una propiedad del causal set que sea
> (i) función únicamente del orden `C`, (ii) invariante bajo reetiquetado de elementos, (iii) definible
> sin embedding, sin coordenada radial, sin `r_S`, sin Schwarzschild de fondo y sin conocer interior/
> exterior, (iv) computable sobre **una sola** historia (sin un gemelo MINK como control), y (v) cuyo
> valor codifique "hay una región atrapada / hay una transición marginal"?

Falsable: basta exhibir, para *cualquier* componente candidato, una de las dependencias prohibidas
(antichain distinguida, truncamiento de parche, singularidad impuesta, control contrafáctico MINK,
coordenada) para que ese componente **no** sea un evento intrínseco. El veredicto se decide por qué
componentes sobreviven a las cinco condiciones simultáneamente.

---

## 2. Qué observable tenemos realmente

Mapa actual `C ↦ salida`, separando lo que ve el **estimador** de lo que ve el **generador/evaluador**:

**Generador (ve coordenadas, `r_S`, métrica EF, caja — NUNCA entra al estimador):**
- `numpy_sprinkle` (`generator.py:37`): Poisson-uniforme en la caja `T_EDGE×R_EDGE = 6.0×1.2`
  (`thresholds.py:37-41`); fija `ℓ = ρ^(-1/2)` y los bordes del parche.
- `past_matrix_fast` (`generator.py:88`): construye `C[i,j]` desde coordenadas + `r_S` + métrica EF;
  la rama BH usa el término tortuga `func = r + 2r_S·log(|r−r_S|/r_S)` (`generator.py:104`) — aquí
  entran Schwarzschild, `r_S` y el truncamiento por la singularidad.

**Estimador (ve SOLO `C`, matriz booleana N×N; `tests/test_leak.py` prohíbe importar scoring):**
- Minimales = filas todo-False (`estimator.py:127`) → la antichain `PastInf` (borde pasado del parche).
- `O(i) = |futuro(i)| = C[:,i].sum()` para cada minimal (`estimate_O_volume`, `estimator.py:113-131`).
- `two_means_split` (`estimator.py:80`): 2-means 1-D sobre el multiset `{O(i)}` → umbral `thr`, `sep`.
- `improvement` (`estimator.py:134`) → gate `τ(n)`: abstiene si `improvement < τ(n)`
  (`gate.py:53`, tabla MC independiente de datos).
- `verify_order_only` (`estimator.py:164`): RAISES si `O` cambia bajo permutación — prueba ejecutable
  de invariancia bajo reetiquetado del observable de producción.

**Evaluador (revela `r`/`r_S` — NUNCA realimenta; `validate.py:101` lo congela antes de revelar):**
- `blind_bracket` (`scorer.py:26`): revela `r` y mapea el corte en `O` a `[r_lo, r_hi]`, punto medio
  `r̂`. **Usa coordenada radial.**
- `covers = r_lo ≤ R_S ≤ r_hi` (`scorer.py:56`): **conoce `r_S`.**
- `d = sep_BH − sep_MINK` (`validate.py:110`), test de significancia (i): **contraste contra un gemelo
  MINK same-cloud.** El juicio "hay horizonte" vive en este contraste, no en una sola historia.
- `theta_loc/theta_stab = K_LOC·ℓ(/2M)` (`thresholds.py:106-113`): `2M = R_S` entra en el bar.

---

## 3. Tabla de admisibilidad intrínseca

`order-only`: ¿función sólo de `C`? · `emb-free`: ¿sin coordenadas? · `relabel-inv`: ¿invariante bajo
permutación? · `estruct. externa`: ¿necesita antichain/frontera/control? · `historias arb.`: ¿sobrevive
en un causal set arbitrario (incl. no manifoldlike)?

| componente (file:line) | order-only | emb-free | relabel-inv | estruct. externa | historias arb. | observación |
|---|:--:|:--:|:--:|:--:|:--:|---|
| relación causal `C` (`generator.py:88` la genera) | ✔ | ✔ (como objeto) | ✔ | no | ✔ | Intrínseca como objeto; pero AQUÍ se fabrica desde coords+`r_S`. |
| `|futuro/pasado(i)|` cardinalidad (`estimator.py:128`) | ✔ | ✔ | ✔ | no\* | ✔ pero **diverge** sin parche | \*finito SÓLO por truncamiento de la caja; en historia infinita/cerrada es ∞ o mal definido. |
| antichain minimal `PastInf` (`estimator.py:127`) | ✔ | ✔ | ✔ (como conjunto) | **sí** | parcial | Es el **borde pasado del parche**; en historia sin borde distinguido no existe canónicamente. |
| `O` = future-volume sobre minimales (`estimator.py:113`) | ✔ | ✔ | ✔ | **sí** | **no** | Ancla en antichain distinguida + truncamiento; ver §4. |
| `two_means_split → thr,sep` (`estimator.py:80`) | ✔(deriv.) | ✔ | ✔ | hereda de `O` | ✔ sobre cualquier multiset | Opera sobre un multiset; intrínseco *si* el multiset lo es. |
| `improvement` (`estimator.py:134`) | ✔(deriv.) | ✔ | ✔ | hereda de `O` | ✔ | Estadístico interno de una sola historia. |
| gate `τ(n)` (`gate.py:53`) | ✔ | ✔ | ✔ | no (null abstracto) | ✔ | Independiente de datos; null Uniforme MC. Pieza sana. |
| Guard-v relabel (`estimator.py:164`) | ✔ | ✔ | — (lo *prueba*) | no | ✔ | Garantía ejecutable de (ii). |
| intervalo/diamante `|[e,f]|` (proxy dev exp.) | ✔ | ✔ | ✔ | no | ✔ | Invariante de orden canónico (BD); sobrevive en no-manifoldlike. |
| `relphi`/`rel_field` (`explore_direction.py:86`) | ✔ | ✔ | ✔ | no | ✔ | Order-only y relabel-inv, PERO discriminante de dirección **no fiable** (falló robustez). |
| ladders / K-beam (`measure_kbeam_peeloff.py`) | ✔(constr.) | ✔(constr.) | ✔ | no | ✔ | Construcción order-only; **peel-off PHYSICAL** dentro del alcance (ver §6 falsif.). |
| expansión `Θ_out` sign-change (`measure_expansion_horizon.py`) | ✔(constr.) | ✔(proxy) | ✔ | depende de split | ✔ | El cruce a `r*` requirió split por `relphi`; **falló robustez** (S1/S2). |
| `blind_bracket → r̂` (`scorer.py:26`) | ✘ | ✘ | — | **sí** | ✘ | Revela `r`. SÓLO evaluación. |
| `covers R_S` (`scorer.py:56`) | ✘ | ✘ | — | **sí** | ✘ | Conoce `r_S`. SÓLO evaluación. |
| `theta_loc/stab` via `2M=R_S` (`thresholds.py:106`) | ✘ | ✘ | — | **sí** | ✘ | Bar anclado a `r_S` y `ℓ`. SÓLO evaluación. |
| sprinkle + caja (`generator.py:37`) | ✘ | ✘ | — | **sí** | ✘ | Coordenadas + parche. Generación externa. |
| BH+singularidad (`generator.py:104`) | ✘ | ✘ | — | **sí** | ✘ | Schwarzschild + término tortuga. Genera el contraste mismo. |
| control MINK `d=sep_BH−sep_MINK` (`validate.py:110`) | ✘ | ✘ | — | **sí (contrafáctico)** | ✘ | El "hay horizonte" vive aquí; una sola historia no tiene gemelo. |

Las **seis preguntas** por componente se responden por columnas de la tabla (1=order-only, 2=relabel-inv,
3=¿necesita foliación/antichain/frontera? = "estruct. externa", 4=¿sobrevive no-manifoldlike? =
"historias arb."), más: (5) ¿puede ser evento medible del espacio de historias? — sólo los que tienen
✔ en las cinco condiciones de §1; hoy: `C`, cardinalidades/intervalos y los estadísticos derivados,
**pero ninguno tal como se ensambla en `O`** (§4). (6) Significado semiclásico: `O` recupera el
truncamiento EGS del futuro interior; los intervalos recuperan volumen causal local; el gate recupera
"estructura bimodal no atribuible al azar".

---

## 4. Dependencias clásicas ocultas

Partes que NO entran como coordenadas al estimador pero dependen implícitamente de Schwarzschild, del
parche, del borde, de la singularidad o de una selección por embedding:

1. **Antichain minimal = borde pasado del parche.** `O(i)` se define "contando el futuro **desde los
   minimales**" (`estimator.py:127`). "Minimal" es una propiedad de orden, pero *que exista una
   antichain distinguida desde la que medir* es una consecuencia del corte temporal inferior de la caja
   (`t∈[0,T_EDGE]`, `generator.py:45`). En una historia sin borde pasado distinguido no hay anclaje.
2. **Finitud de `|futuro(i)|` = truncamiento del parche.** El future-volume es finito **sólo** porque la
   caja corta el futuro por arriba y por los lados. Sin parche, `|futuro|` diverge. El observable es,
   literalmente, "volumen causal futuro **dentro de la caja**".
3. **El contraste que hace que `O` lleve el horizonte = singularidad impuesta.** Lo que separa
   interior/exterior en `O` es que el futuro interior está **truncado hacia la singularidad** (término
   tortuga `func`, `generator.py:104`; EGS). Es Schwarzschild-singular-específico — falla para un BH
   regular (Hayward) (`PR003_INFO_BOUND_NOTES.md:136`). El "atrapamiento" detectado es, en parte, la
   firma del corte singular, no orden puro.
4. **Conocer `r_S`.** Entra tres veces fuera del estimador: generación (`generator.py:104`), bar
   (`thresholds.py:106-113`, `2M=R_S`) y scoring (`covers`, `scorer.py:56`).
5. **Conversión a posición radial y "covers".** `blind_bracket` (`scorer.py:26`) y `covers`
   (`scorer.py:56`) son embedding puro; toda la noción de "posición del horizonte" es externa.
6. **El control contrafáctico MINK (la dependencia más sutil).** El juicio operativo "hay horizonte" es
   el contraste pareado `d = sep_BH − sep_MINK` (`validate.py:110`, test i). Una historia individual
   **no tiene** gemelo MINK same-cloud; sin él, `sep_BH` por sí solo no afirma "horizonte". Esta es una
   estructura externa de **comparación**, no de coordenadas, y es la que más amenaza la intrínseca-idad.
7. **`relphi` como selección.** Donde la expansión funcionó (3600), el split interior/exterior dependió
   de `relphi` (`PR003_EXPANSION_NOTES.md:73`), un discriminante de dirección no robusto: una selección
   que *imita* el conocimiento interior/exterior sin ser fiable.

---

## 5. Candidato mínimo a evento cuánticamente admisible (UN candidato, TENTATIVO — no es un resultado)

**T — "evento de atrapamiento intrínseco" (existencia, NO localización).**

- **Dominio:** cualquier causal set finito `(P, ≺)`. Sin embedding, sin `r_S`, sin caja Schwarzschild.
- **Datos necesarios:** sólo el orden `C` y cardinalidades de intervalos `|[x,y]|` derivadas de él.
- **Definición tentativa:** sea `g(x)` una medida *order-only* de la tasa de crecimiento del volumen
  causal futuro local de `x` (p.ej. construida con cardinalidades de intervalos `|[x,·]|`, sin
  antichain distinguida ni pareo de ladders). `T = 1` (existe región atrapada) sii existe un subconjunto
  conexo `W ⊆ P` maximal donde `g` está deprimida respecto a la mediana ambiente por un margen, **y** la
  depresión supera el null order-only abstracto del gate (`gate.py`) — i.e. no atribuible al azar.
- **Invariancia bajo reetiquetado:** sí — `g` se construye sólo de `|[x,y]|`, invariante de orden; `W`
  es un subconjunto, invariante como conjunto bajo permutación.
- **Condición de existencia:** gate-significativa (reutiliza `τ`, pieza ya independiente de datos).
- **Límite semiclásico esperado:** en el parche Schwarzschild esprinclado, `W` debería solapar el
  interior geométrico `r<R_S` — **a verificar**, nunca a asumir.
- **Por qué NO es S1/S2/S3 ni `kbeam`:** aquellos producen una **localización** `r̂`/`r*` puntuada por
  `d⊥`/`covers` contra `R_S` (S1/S2: cruce de `Θ_out` a `r*` vía `relphi`; S3: re-seeding iterativo;
  kbeam: ladders rankeadas que reportan `d⊥/ℓ`). `T` es un **evento de existencia binario** sin `r̂`,
  sin antichain ancla, sin pareo de ladders, sin split por `relphi`, sin sign-change-en-`r*`, juzgado
  por un null order-only **interno** en vez de por un gemelo MINK o una distancia coordenada. Compara
  contra las definiciones exactas: difiere en el *tipo de salida* (existencia vs locus) y en el *juez*
  (null interno vs contrafáctico/coordenada).

**Honestidad obligatoria:** `T` es tentativo y **hoy NO es defendible**. Su poder discriminante
plausiblemente sigue derivando del truncamiento singular (§4.3), de modo que el falsificador F-SING
(abajo) lo amenaza directamente, y no está demostrado que `g` distinga interior de Minkowski **sin**
restar un control MINK (§4.6). Es una *definición tentativa para ser probada o refutada en papel*, no un
observable establecido. Si la prueba de §9 falla, `T` cae.

---

## 6. Falsificadores

Cualquiera que se cumpla descarta la reinterpretación como evento cuántico intrínseco del componente
evaluado:

- **F-COORD:** requiere coordenadas/embedding → `blind_bracket`, `covers`, `theta_*` (✘ ya).
- **F-RS:** requiere conocer `r_S`/el horizonte de antemano → bar y scoring (✘ ya).
- **F-MANIFOLD:** sólo funciona en causal sets manifoldlike ya identificados → si `T`/`g` exige
  estructura de variedad (foliación, dirección), cae.
- **F-PATCH:** confunde **borde del parche** con atrapamiento → si la depresión de `g` o la bimodalidad
  de `O` se reproduce en una caja Minkowski por puro efecto de borde, es artefacto. (`O` es vulnerable:
  su finitud ES el borde, §4.2.)
- **F-SING:** depende de la singularidad impuesta → si `T` desaparece para un BH regular (Hayward), no
  es intrínseco al "atrapamiento" sino a la singularidad (EGS; `PR003_INFO_BOUND_NOTES.md:136`).
- **F-AGOTADO:** reproduce matemáticamente un observable ya agotado en PR-003 → si `g`/`T` colapsa a la
  definición de expansión `Θ_out` (`measure_expansion_horizon.py`), a la ladder/K-beam
  (`measure_kbeam_peeloff.py`) o al re-seeding S3, hereda sus negativos (peel-off PHYSICAL; S1/S2 no
  robustos). Debe compararse definición-a-definición antes de proponerlo.
- **F-CONTRAFACTUAL:** no puede computarse sobre una sola historia sin un gemelo MINK → si "hay
  horizonte" sólo emerge de `sep_BH − sep_MINK` (`validate.py:110`), no es un evento de historia
  individual sino de un **par** de historias (un coarse-graining contrastivo, CG-2, no OBS-1).
- **F-RELABEL:** no expresable como evento invariante bajo reetiquetado (descarta cualquier `g` que use
  índices/orden de fila).

---

## 7. Qué sobrevive del pipeline actual

- **Sobreviven sin modificación (intrínsecas, order-only, relabel-inv, no-manifoldlike-safe):** la
  relación `C`; cardinalidades de futuro/pasado e **intervalos/diamantes `|[e,f]|`**; los estadísticos
  derivados `two_means_split`/`improvement` *como operadores sobre un multiset*; el **gate `τ(n)`**
  (null abstracto, independiente de datos); el **Guard-v** (garantía de relabel-invariancia). Estas son
  las piezas con ✔ en las cinco columnas de §3.
- **Sobreviven sólo como calibración semiclásica:** `O = future-volume` **sobre la antichain minimal**
  (necesita parche + antichain), `relphi`, la construcción de ladders/K-beam y la expansión `Θ_out`:
  útiles como diagnósticos calibrados contra Schwarzschild, **no** como eventos intrínsecos (anclan en
  parche/singularidad/`relphi`).
- **Deben sustituirse (para un evento intrínseco):** el anclaje en la antichain minimal (§4.1); la
  finitud-por-parche de `|futuro|` (§4.2); el contraste vía gemelo MINK (§4.6) por un juez **interno**
  de una sola historia.
- **Exclusivamente externas de evaluación:** `blind_bracket`, `covers`, `theta_loc/stab`, el sprinkle
  con coordenadas, y la generación BH/MINK. No forman parte de ningún observable intrínseco.

---

## 8. Veredicto

### `PARTIALLY_ADMISSIBLE_REQUIRES_RELATIONAL_REDEFINITION`

**Justificación.** Los *ingredientes atómicos* del pipeline (relación `C`, cardinalidades de futuro/
pasado, intervalos `|[e,f]|`, los estadísticos `two_means_split`/`improvement`, el gate `τ` y el
Guard-v) **sí** son order-only, invariantes bajo reetiquetado y bien definidos sobre historias
arbitrarias, incluso no-manifoldlike. Existe incluso un evento order-only de **una sola historia** ya
presente — "el multiset de future-volumes de la antichain minimal tiene estructura bimodal significativa
(`improvement ≥ τ(n)`)" (`gate.py:53`). Pero el **observable ensamblado** (`O` sobre minimales →
2-means → `r̂` → `covers`) **no** es un evento intrínseco: depende simultáneamente de (i) una antichain
distinguida (borde pasado del parche, §4.1), (ii) el truncamiento del parche para que `|futuro|` sea
finito (§4.2), (iii) la singularidad impuesta para que `O` lleve el contraste (§4.3), (iv) un control
contrafáctico MINK para que el juicio "hay horizonte" exista (§4.6), y (v) coordenadas/`r_S` para toda la
conversión radial y el scoring (§4.4-4.5). Por tanto el diagnóstico **deja de ser intrínseco exactamente
en el paso "future-volume anclado en la antichain minimal del parche, juzgado contra un gemelo MINK"**.
Convertirlo en un evento de historia exige una **redefinición relacional** (eliminar el ancla-antichain,
la finitud-por-parche y el contraste MINK por un juez interno); existe a lo sumo un candidato *tentativo
y hoy no defendible* (`T`, §5), no un observable establecido. De ahí "parcialmente admisible, requiere
redefinición relacional" — ni admisible tal cual, ni imposible en principio.

Este veredicto **no autoriza** implementación, dinámica cuántica, CG-2, DEC-3, ni reabrir rutas de
PR-003.

**Nota sobre el esquema formal (etiquetado como tal).** Una eventual lectura por-historias escribiría
amplitudes tipo `exp(i S_BDG / ħ)` con `S_BDG` la acción de Benincasa–Dowker. Esto es **sólo un esquema
formal**, no una teoría: faltan el espacio de historias, la medida, las condiciones de contorno, el
estado inicial, el tratamiento de automorfismos (reetiquetados), la regularización de `S_BDG`, y —sobre
todo— una **definición concreta del funcional de decoherencia** (DEC-3). Nada de eso existe aquí y esta
nota no lo provee. El `0.4 ℓ` medido (`PR003_INFO_BOUND_NOTES.md:197-202`) es **anchura operacional
semiclásica** producida por sprinkling clásico + respuesta del estimador; **no** es anchura cuántica del
horizonte ni evidencia de superposición de geometrías.

---

## 9. Siguiente paso reversible (UNA prueba conceptual, sin código)

**Prueba en papel — "discriminación de una sola historia sin gemelo MINK".** Antes de cualquier
implementación, demostrar (o construir contraejemplo a) la afirmación:

> Existe un funcional order-only `g` construido sólo de cardinalidades de intervalos `|[x,y]|`,
> **sin antichain distinguida y sin sustraer un control MINK**, tal que su distribución sobre los
> elementos de un parche Schwarzschild esprinclado difiere de la de un parche Minkowski por encima de
> la fluctuación de Poisson — i.e. una **discriminación de una sola historia**.

Es la pieza necesaria porque hoy todo el contenido "hay horizonte" descansa en el contraste pareado
`sep_BH − sep_MINK` (§4.6): si `g` no discrimina sin ese gemelo, el observable es intrínsecamente
**contrastivo** (un CG-2 sobre pares de historias), no un OBS-1, y el veredicto se endurece hacia
`NOT_ADMISSIBLE`. Si `g` sí discrimina, queda definido el dominio mínimo donde `T` (§5) podría
formularse — y sólo entonces tendría sentido considerar pasos posteriores. La prueba es puramente
analítica, reversible, no quema semillas ni toca el sello. La §10 ejecuta el primer tramo de esa
prueba: la **formulación como problema de identificabilidad**, antes de proponer ningún estimador.

---

## 10. Formulación del paso §9 como problema de identificabilidad (prueba conceptual en papel)

> Continuación analítica del §9 (segunda pasada). No es un teorema cerrado: es la **formulación rigurosa
> del problema de existencia** + la reducción que aísla dónde vive (o muere) la identificabilidad. Marco
> explícitamente lo *establecido* (reducciones, confound, estratificación) frente a lo *abierto* (la
> contigüidad, que es el teorema en sí). Sin código, sin medición, sin commit.

### 10.1 El problema de existencia (identificabilidad)

Causal set finito `C = (P, ≺)`. Funcional **invariante por isomorfismo de poset** `T: C → ℝ`
(`T(C)=T(C')` si `C ≅ C'`). Dos clases de historias finitas, `H_trap` y `H_no-trap`. Se busca `T` tal que:

1. invariante bajo isomorfismos del poset (⊇ relabel-invariancia, §3);
2. sin embedding, coordenadas ni parámetros del generador (`r_S`, `T_EDGE`, métrica);
3. definido sobre **una sola** historia;
4. **sin** control MINK emparejado;
5. separación asintótica: `Pr_{H_trap}(T∈A) → 1` y `Pr_{H_no-trap}(T∈A) → 0` para algún boreliano `A`.

**Cuestión primaria:** ¿puede existir tal `T` con los ingredientes ordinales actuales (cardinalidades de
futuro/pasado e intervalos `|[x,y]|`)?

**Precisión sobre el régimen (corregido).** Sean `P_n` (ley observable bajo `H_trap`) y `Q_n` (bajo
`H_no-trap`), tomadas aquí como **dos sucesiones de leyes simples**. Existe un test **consistente** (que
realiza la separación (5)) exactamente cuando las leyes se separan asintóticamente; en variación total,
`‖P_n − Q_n‖_TV → 1`. **[Alcance]** esta equivalencia es para `P_n, Q_n` *simples*; si más adelante `H_trap`
y `H_no-trap` pasan a ser **familias compuestas** (p.ej. todo el plano-borde-moldeado admisible), hay que
sustituirla por **separación uniforme/minimax** entre familias (`inf/sup` sobre miembros). La
**contigüidad mutua**
(`P_n ◁ Q_n` y `Q_n ◁ P_n`: todo evento cuya probabilidad → 0 bajo una ley también → 0 bajo la otra) es una
condición **estrictamente más fuerte**. La relación correcta es una **implicación, no una equivalencia**:

```
contigüidad mutua  ⟹  no identificabilidad asintótica   (la recíproca NO vale en general).
```

Es decir: probar contigüidad **basta** para matar `T`, pero la mera no-separación (`‖P_n−Q_n‖_TV ↛ 1`) NO
implica contigüidad. Además, la contigüidad **unilateral** (`P_n ◁ Q_n` con `Q_n ⋪ P_n`, o la orientación
inversa) ya obstruye un test consistente —errores de ambos tipos → 0— **sin** ser contigüidad mutua: si
hubiera test consistente con región crítica `R_n` (`Q_n(R_n)→0`, `P_n(R_n)→1`), `P_n ◁ Q_n` forzaría
`P_n(R_n)→0`, contradicción. Por tanto la clasificación honesta tiene **cuatro casos**, no tres:

```
(1) Separación asintótica:        ‖P_n − Q_n‖_TV → 1                  (∃ test consistente; ∃ T).
(2) Contigüidad mutua:            P_n ◁ Q_n  y  Q_n ◁ P_n             (⟹ no identificable).
(3) Contigüidad unilateral:       P_n ◁ Q_n  XOR  Q_n ◁ P_n           (⟹ no test consistente; asimétrico).
(4) Complemento residual:         ‖P_n−Q_n‖_TV ↛ 1,  P_n ⋪ Q_n,  Q_n ⋪ P_n.
```

(4) se define como **complemento** de (1)–(3), no como un régimen concreto: incluye `liminf‖·‖_TV = 0`,
`limsup‖·‖_TV = 1` sin convergencia, oscilaciones entre subsecuencias, o separación en una subsecuencia y
solapamiento fuerte en otra. El régimen regular `0 < liminf ≤ limsup‖P_n−Q_n‖_TV < 1` es un **subcaso
especialmente relevante** de (4), no su definición. (2) y (3) **ambas** impiden identificabilidad
consistente; (3) es asimétrico y no debe clasificarse como (4). (1) la permite.

### 10.2 El confound de tres vías, relativo a σ(V) (lo ESTABLECIDO — insuficiencia del ESCALAR, no del orden)

El único escalar que el pipeline lee del orden para el "atrapamiento" es el volumen de futuro
`V(x) = |{y : x ≼ y}|` (= `O(i)` en minimales, `estimator.py:128`). Para un sprinkling de densidad `ρ`,
`E[V(x)] = ρ · vol\!\big(J^+(x) ∩ \text{Caja} ∩ \{r>0\}\big)`. **Tres causas distintas reducen ese mismo
volumen y entran en el MISMO escalar:**

- **(S) singularidad/horizonte:** el cono `J^+(x)` de un `x` interior está *enfocado y cortado* en `r=0`
  (término tortuga, `generator.py:104`). Causa física buscada.
- **(B) borde futuro del parche:** `x` cerca de `t=T_EDGE` tiene `J^+` simplemente *no muestreado*
  (`generator.py:45`). Artefacto de caja.
- **(F) finitud / no-manifoldlike:** `x` cerca de la anticadena maximal de un poset finito genérico tiene
  futuro pequeño por finitud, sin geometría alguna.

**Lema de confound (establecido, elemental) — alcance EXACTO: σ(V).** `V(x)` es un escalar; (S), (B), (F)
reducen el mismo `vol(J^+(x) ∩ …)`. Por tanto **ningún procedimiento medible respecto de `σ(V)`** (la
σ-álgebra/información generada por la familia de volúmenes de futuro) puede atribuir el déficit a una causa
una vez igualada la ley de `V`. El control MINK suministra `E[V_flat(x)] = ρ·vol(J^+(x) ∩ \text{Caja})`
—misma caja, sin el corte `{r>0}`— y la resta `V_BH − V_MINK` cancela (B) [misma caja] y aísla (S). **Por
eso el gemelo MINK es estructuralmente necesario en el diseño actual: es una sustracción de fondo del efecto
de borde** dentro de `σ(V)`.

**Lo que el lema demuestra y lo que NO (corregido).** Demuestra **insuficiencia del estadístico escalar `V`**
(equivalentemente: de cualquier funcional `σ(V)`-medible) cuando las marginales de `V` se igualan. **No**
demuestra todavía insuficiencia del **orden local completo**: el suborden observable contiene una σ-álgebra
`σ(C_loc) ⊋ σ(V)` y la sustracción MINK podría, en principio, ser innecesaria para un funcional fuera de
`σ(V)`. (Confirma §4.6 sólo al nivel de `σ(V)`.)

### 10.3 El atrapamiento intrínseco se reduce a *enfocamiento* (lo ESTABLECIDO, con el cuello de botella)

Atrapamiento geométrico = `Θ_out ≤ 0` = área transversal no creciente a lo largo del nulo saliente =
enfocamiento de Raychaudhuri. Proxy order-only (EGS Eq. 14; `measure_expansion_horizon.py:13`): para `u,v`
en un mismo "frente", la cardinalidad del **diamante causal envolvente** `|[u∧v, u∨v]|` mide su separación
mutua al cuadrado; su tasa de cambio hacia el futuro es la expansión `E`; atrapamiento ⇔ `E` cambia de
signo. Es order-only e iso-invariante **dada** una noción de "frente" y de "dirección saliente". Esa
dirección exige un discriminante order-only = `relphi`, que **falló robustez** (S1/S2,
`PR003_EXPANSION_NOTES.md:73`). **Conclusión:** incluso la *definición* de atrapamiento intrínseco hace
cuello de botella en el mismo ingrediente no fiable — el problema no es de estimación, es de definición.

### 10.4 Reducción de la existencia a un problema de *matching* (lo ESTABLECIDO; aísla lo ABIERTO)

`T` separa (S) de (B)/(F) sii existe un estadístico de orden cuya ley difiere entre los ensembles con
solapamiento → 0. Construyo el adversario que vuelve **no informativo el primer orden**:

> **Adversario de borde moldeado.** Tómese un parche *plano* cuya frontera futura se moldee para que la ley
> de `V_flat(x)` **iguale** la de `V_BH(x)` (es un único grado de libertad —el perfil del borde— ajustado a
> una única marginal; siempre factible).

Igualar la marginal de `V` elimina **sólo** la información de primer orden contenida en `V` (i.e. en
`σ(V)`). **No** prueba que la información restante se reduzca a vuestro proxy de enfocamiento ya ensayado.
El orden conjunto puede contener otros canales de segundo o mayor orden, p.ej.:

```
|I(x,y)| (interval. envolvente) ,  |fut(x) ∩ fut(y)| ,  grados (in/out) ,  motifs ,  covarianzas multiescala.
```

Hay que separar dos cosas que NO son lo mismo:
- **(2-relphi)** el segundo orden *accesible mediante `relphi`* — el único canal ya ensayado, que falló
  robustez (§10.3);
- **(2-todo)** *todo* posible segundo (o mayor) orden ordinal del suborden observable.

Que `relphi` falle acota (2-relphi), **no** (2-todo): no está demostrado que `relphi` sea el único canal
posible. Por tanto la cuestión de existencia debe formularse sobre el **suborden observable completo**, no
sobre un proxy:

> **(Q-ident, reformulada)** Sean `P_n`, `Q_n` las leyes del **suborden observable completo** (la
> distribución del tipo de iso-orden / de los estadísticos iso-invariantes accesibles localmente) bajo
> Schwarzschild-interior y bajo *cualquier* parche plano con la marginal de `V` igualada. ¿En cuál de los
> cuatro casos de §10.1 (separación / contigüidad mutua / contigüidad unilateral / ninguna) caen?

- **(1) Separación:** `‖P_n−Q_n‖_TV → 1` → existe `T` iso-invariante (un funcional de orden conjunto, no
  necesariamente de enfocamiento) → candidato genuino a evento `E_trap = {C : T(C)∈A}` (entonces, y sólo
  entonces, estudiable como CG-2).
- **(2) Contigüidad mutua** o **(3) contigüidad unilateral** (cualquier dirección): ambas ⟹ **no
  identificabilidad consistente** → *el atrapamiento no es identificable desde información ordinal local de
  una sola historia finita sin condiciones de contorno adicionales.* Explicaría por qué el parche, la
  singularidad y el control MINK fueron imprescindibles — obstrucción conceptual, no fallo del estimador.
  (Es una **implicación**: cualquiera de las dos contigüidades basta; ver §10.1. (3) sería un régimen
  asimétrico interesante en sí mismo — p.ej. detectable la *ausencia* pero no la *presencia* de
  atrapamiento, o viceversa.)
- **(4) Complemento residual** (`‖P_n−Q_n‖_TV ↛ 1`, `P_n ⋪ Q_n`, `Q_n ⋪ P_n`): incluye el subcaso regular
  `0 < liminf ≤ limsup‖P_n−Q_n‖_TV < 1` (discriminación parcial, no consistente) y también
  oscilaciones/subsecuencias — a caracterizar.

**Lo ABIERTO es exactamente (Q-ident reformulada).** Lo **establecido** aquí es estrictamente: (a) el primer
orden en `σ(V)` es no informativo bajo matching, y (b) si hubiera discriminación, vive en `σ(C_loc)∖σ(V)` —
del cual el enfocamiento vía `relphi` es **un** canal (fallido), no el único. NO está establecido que toda la
identificabilidad recaiga en el enfocamiento, ni que las leyes sean contiguas. El fracaso de la expansión es
**evidencia débil** sobre (2-relphi), no una prueba sobre (2-todo) ni sobre la contigüidad.

### 10.5 La capa de manifoldlikeness (caso F — eleva el listón; inferencia plausible, NO teorema)

Para que "atrapamiento" signifique algo hay que excluir (F): certificar **manifoldlikeness**. La conclusión
razonable y acotada es:

> Certificar manifoldlikeness **con garantías fuertes** probablemente requiere información **no puramente
> local** y un **régimen asintótico** (estimador de dimensión Bombelli–Meyer por cadenas/longest-chain;
> abundancias de intervalos tipo Benincasa–Dowker — refs en `biblioteca/`, [UNVERIFIED] aquí a line-level).

**Lo que NO afirmo:** que sea *imposible* construir diagnósticos locales. Puede haber **indicadores locales**
de dimensión o regularidad (p.ej. abundancias de intervalos cortos), aunque no constituyan una
*certificación suficiente*. Por tanto la inferencia "un observable admisible sería **bietápico** (certificado
global de manifoldlikeness + funcional local)" es una **inferencia plausible, no un teorema**: rebaja la
esperanza de "un solo funcional local con garantía fuerte", pero no la cierra.

### 10.6 Qué probaría cada rama de la clasificación de cuatro casos (sin ejecutarlo)

- **(1) Separación:** exhibir un funcional iso-invariante `T` sobre `σ(C_loc)` y un `A` con `vol`-marginal
  igualada cuya potencia → 1 (`‖P_n−Q_n‖_TV → 1`); refuta toda contigüidad construyendo el test. El
  enfocamiento es **un** candidato a `T`, no el único (los otros canales de §10.4).
- **(2) Contigüidad mutua (más profundo):** construir sucesiones `C_trap^{(n)}, C_no-trap^{(n)}`
  (Schwarzschild-interior vs plano-borde-moldeado) cuyas leyes del **suborden observable completo** sean
  mutuamente contiguas (Le Cam). Requiere igualar no sólo la marginal de `V` sino la ley conjunta de los
  estadísticos iso-invariantes accesibles (`|[u∧v,u∨v]|`, `|fut(x)∩fut(y)|`, grados, motifs, …) a los
  órdenes accesibles localmente.
- **(3) Contigüidad unilateral:** establecer una sola dirección (`P_n ◁ Q_n` o `Q_n ◁ P_n`) y **refutar la
  otra** (exhibir un evento que separe en el sentido contrario). Ya basta para la no-identificabilidad
  consistente, y caracteriza un régimen asimétrico (detectable un lado, no el otro).
- **(4) Complemento residual:** descartar (1)–(3), i.e. `‖P_n−Q_n‖_TV ↛ 1`, `P_n ⋪ Q_n`, `Q_n ⋪ P_n`; el
  subcaso regular `0 < liminf ≤ limsup‖·‖_TV < 1` es la discriminación parcial no consistente, pero (4)
  abarca también oscilaciones/subsecuencias.

Ninguna se ejecuta aquí. La §10 deja el problema **bien planteado** y aísla **lo establecido** (`V`/`σ(V)`
insuficiente) frente a **lo abierto** (en cuál de los cuatro casos caen `P_n, Q_n` del suborden completo).
Esa clasificación, no otro estimador, es el siguiente objeto a atacar en papel.

---

## Cierre

Esta nota es exploración conceptual; no congela nada, no mide nada, no autoriza implementación. La
contribución es deliberadamente del lado negativo/diagnóstico: **el estimador semiclásico no define
todavía un observable sobre historias causales arbitrarias porque ancla en una antichain de parche,
necesita el truncamiento del parche para ser finito, hereda su contraste de la singularidad impuesta, y
delega el juicio "hay horizonte" en un gemelo MINK (al nivel de `σ(V)`)** — y eso es más útil que afirmar
prematuramente que ya tenemos un observable de gravedad cuántica.

**Veredicto actualizado tras la corrección de §10 (qué está ESTABLECIDO vs qué queda AISLADO-pero-ABIERTO):**

- ESTABLECIDO: **`V` (el volumen de futuro) no puede ser el observable intrínseco final** — insuficiencia de
  cualquier funcional `σ(V)`-medible bajo matching de la marginal de `V` (§10.2).
- AISLADO pero ABIERTO: **¿contiene el suborden observable completo información de enfocamiento (u otro orden
  conjunto) no reproducible por un borde plano adversarial?** — la clasificación en **cuatro casos**
  (separación / contigüidad mutua / contigüidad unilateral / complemento residual) de `P_n, Q_n`, leyes
  *simples* (separación uniforme/minimax si pasan a familias compuestas) (§10.1, §10.4, §10.6).
- NO demostrado: contigüidad, ni no-identificabilidad del orden local completo, ni que `relphi`/enfocamiento
  sea el único canal de segundo orden, ni imposibilidad de indicadores locales de manifoldlikeness.

El veredicto global de §8 (`PARTIALLY_ADMISSIBLE_REQUIRES_RELATIONAL_REDEFINITION`) se mantiene; §10 lo afina
señalando que la redefinición relacional pendiente es precisamente esa clasificación de leyes del suborden
completo — el núcleo matemático del proyecto a partir de aquí, no un nuevo estimador.
