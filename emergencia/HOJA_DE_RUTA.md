# Hoja de ruta — Emergencia e identificabilidad del tiempo

> **ESTADO: HOJA DE RUTA v1.0 · 2026-08-03 · REVISABLE · SIN NUEVA
> AUTORIZACIÓN NUMÉRICA.**
>
> Este documento organiza la línea independiente `emergencia` dentro del laboratorio
> `nachocausal`. Resume decisiones ya cerradas, identifica la única rama cuantitativa
> todavía abierta y ordena los próximos gates. No modifica contratos anteriores, no
> reabre representaciones aparcadas y no autoriza por sí mismo nuevas ejecuciones.

## 1. Objetivo de la línea

La pregunta general es:

> ¿Qué estructura temporal métrica puede identificarse a partir de un orden causal
> finito y de sus conteos, bajo qué canal de observación y con qué resolución?

El programa distingue explícitamente:

1. orientación causal;
2. duración relativa;
3. escala temporal absoluta;
4. selección intrínseca de endpoints;
5. calibración ensemble-level;
6. resolución para una realización individual;
7. y reconstrucción geométrica más amplia.

La línea actual trabaja en la familia mínima `d=2`, con posets producto procedentes
de puntos iid en un cuadrado de coordenadas nulas y condicionado a `N=n`.

```text
CANAL_ACTUAL = POSET_NO_ETIQUETADO + CARDINALIDAD_FIJA_N
DIMENSION_ACTUAL = 2
ESCALA_FISICA_ABSOLUTA = NO_IDENTIFICADA_EN_ESTE_CANAL
COCIENTE_TEMPORAL = NO_AUTORIZADO
```

> **Formulación corregida del canal (2026-08-04).** El observable es la clase de
> isomorfismo del poset no etiquetado; **sus cardinalidades son observables
> legítimos** — `Orden + Número = Geometría` es la premisa de la teoría, no una
> concesión. En los experimentos con `N=n` solo se condiciona la cardinalidad
> **global**, lo que elimina su información de escala absoluta, pero **no** los
> conteos internos ni la información métrica **relativa**. Por tanto el no-go de
> escala absoluta de Fase 0 pertenece al canal condicionado `N=n`, no a los causal
> sets en general.
>
> Consecuencia para `COUNT_VOLUME`: usar `m` en el selector y después en el estimador
> **no** es «hacer trampa». El problema real es la **dependencia inducida por
> selección** (incluido el sesgo del ganador), no el uso de cardinalidades. La
> etiqueta de «circularidad» de Fase 6 debe leerse en ese sentido restringido y no
> como objeción al conteo.

## 2. Recorrido realizado

### Fase 0 — Formulación y no-go de escala

Se abrió la línea como problema de identificabilidad y se separaron los canales
`fixed-n`, Poisson con densidad desconocida, Poisson con densidad conocida e input
geométrico externo.

En la familia mínima se estableció que una dilatación global puede preservar la ley
del poset condicionado a `N=n`; por tanto, la escala absoluta no puede recuperarse de
ese canal sin información adicional.

Documentos:

- `Identificabilidad del tiempo métrico desde orden causal finito.md`
- `T0_modelo_minimo_y_proposicion_cero.md`

### Fase 1 — Selección intrínseca de dos intervalos

Se formuló el problema previo a cualquier estimador: escoger dos intervalos sin
coordenadas, endpoints externos, etiquetas ni desempates arbitrarios. Los
automorfismos obligan a permitir abstención o salida conjuntista.

Se definió `F_cov,3`, que maximiza cobertura total con soporte mínimo `k_0=3`.

Documentos:

- `P1a_seleccion_intrinseca_y_automorfismos.md`
- `P1a_primer_selector_de_cobertura.md`

### Fase 2 — Puerta teórica y disponibilidad en `d=2`

El poset bidimensional se redujo a una permutación uniforme. El evento sin candidato
se identificó con altura menor que seis y se enumeraron exactamente las permutaciones
para `n=6,7,8,9`.

La simulación hasta `n=64` produjo:

```text
POINT_SELECTOR_OPERATIONALLY_VIABLE
```

Esto cerró únicamente la objeción “el selector casi nunca produce una salida”. No
demostró validez métrica.

Documentos:

- `P1a_puerta_teorica_en_Minkowski.md`
- `P1a_contrato_enumeracion_y_monte_carlo_d2.md`
- `P1a_resultados_enumeracion_y_monte_carlo_d2.md`

### Fase 3 — Estabilidad y degeneración del selector de cobertura

`F_cov,3` resultó estable bajo thinning, pero el intervalo menor quedó en `m_min=3`
en aproximadamente `74–78 %` de las selecciones del régimen alto. El balance medio
colapsó al crecer `n`.

```text
F_cov,3_IDENTITY_STABILITY = PASS
F_cov,3_MINIMUM_SUPPORT_QUALITY = FAIL
F_cov,3_METRIC_PROMOTION = CLOSED
```

Documentos:

- `P1a_contrato_estabilidad_y_sesgo_d2.md`
- `P1a_resultados_estabilidad_y_sesgo_d2.md`

### Fase 4 — Comparación de selectores balanceados

Se compararon sobre una muestra nueva:

```text
COVERAGE,
MIN_ONLY,
MIN_COVERAGE_LEX.
```

`MIN_ONLY` protegió mejor el balance, pero no superó el gate de estabilidad.
`MIN_COVERAGE_LEX` eliminó el suelo observado, mantuvo alta disponibilidad y superó
los umbrales de thinning.

```text
SELECTED_SELECTOR = MIN_COVERAGE_LEX
```

Documentos:

- `P1a_contrato_comparacion_selectores_balanceados_d2.md`
- `P1a_resultados_comparacion_selectores_balanceados_d2.md`

### Fase 5 — Altura frente a duración latente

Para cada intervalo seleccionado se comparó

```text
ell_hat_H = H/(2 sqrt(n))
```

con la duración nula latente `ell=sqrt(Delta u Delta v)`.

La escala media fue razonable, el error relativo mediano fue `10–14 %` y el target
latente resultó estable bajo thinning. Sin embargo, la correlación individual quedó
entre `0.22` y `0.29`.

```text
PARK_LEX_HEIGHT_REPRESENTATION
```

La altura aproxima el centro de la banda seleccionada, pero no discrimina bien qué
intervalo individual tiene mayor duración.

Documentos:

- `P1a_contrato_gate_altura_duracion_lex_d2.md`
- `P1a_resultados_gate_altura_duracion_lex_d2.md`

### Fase 6 — Dos representaciones alternativas

Se abrieron:

```text
COUNT_VOLUME = sqrt((m-2)/(n-2)),
HEIGHT_WIDTH = (H+W)/(4 sqrt(n)).
```

Resultados:

| Representación | Correlación individual | Error relativo mediano | Estado |
|---|---:|---:|---|
| `HEIGHT_ONLY` | 0.23–0.27 | 10–14 % | aparcada previamente |
| `HEIGHT_WIDTH` | 0.37–0.47 | 12–14 % | aparcada fuerte |
| `COUNT_VOLUME` | 0.53–0.57 | 7–11 % | abierta, no cualificada |

```text
ALTERNATIVE_TERMINAL = INCONCLUSIVE_ALTERNATIVE_REPRESENTATIONS
COUNT_VOLUME = OPEN_THEORY_REQUIRED
HEIGHT_WIDTH = PARKED
```

Documentos:

- `P1a_contrato_representaciones_alternativas_d2.md`
- `P1a_resultados_representaciones_alternativas_d2.md`

## 3. Estado consolidado

| Componente | Estado | Consecuencia |
|---|---|---|
| Canal `fixed-n`, `d=2` | activo | no confundir con escala Poisson física |
| Selección intrínseca puntual | construida | debe permitir abstención por empate |
| `F_cov,3` | cerrada como vía métrica | soporte menor degenerado |
| `MIN_ONLY` | no seleccionado | estabilidad insuficiente |
| `MIN_COVERAGE_LEX` | selector de trabajo | target estable y bien soportado |
| `HEIGHT_ONLY` | aparcada | resolución individual fuerte insuficiente |
| `HEIGHT_WIDTH` | aparcada | fórmula concreta con fallo fuerte |
| `COUNT_VOLUME` | abierta | señal moderada; teoría de selección pendiente |
| Cociente de alturas | cerrado | nunca ejecutado |
| Cociente de cardinalidades | cerrado | riesgo de circularidad con el selector |
| `d>=3` | no abierto | no extrapolar resultados bidimensionales |
| P2, escala con `rho` conocida | abierta | línea separada del canal actual |
| P3, cotas finitas | abierta | necesaria para interpretar resolución |

La infraestructura reproducible incluye cinco ejecutores, artefactos CSV/JSON con
sidecars SHA-256 y `59` pruebas específicas. El estado del worktree no constituye
una publicación ni un commit.

## 4. Lecciones científicas acumuladas

1. **Disponibilidad no implica identificabilidad.** Un selector puede ser único y
   estable sin producir intervalos métricamente informativos.
2. **La selección es parte del target.** Cambiar el score cambia casi por completo
   los endpoints y la distribución de duraciones.
3. **Calibración media no implica resolución individual.** Un estimador próximo a la
   duración media puede tener correlación muy baja dentro de una banda estrecha.
4. **Orden y número aportan información distinta.** La cardinalidad del intervalo
   contiene más señal de duración que la altura en la familia evaluada.
5. **Más invariantes no garantizan más resolución.** Añadir anchura a altura mejoró
   parcialmente el benchmark, pero no superó el no-go operacional.
6. **La estabilidad del target puede exceder la de los endpoints.** Tras thinning,
   cambian con frecuencia los elementos seleccionados mientras las duraciones
   permanecen próximas.
7. **El selector puede crear circularidad.** `MIN_COVERAGE_LEX` usa cardinalidades;
   una razón basada en esas mismas cardinalidades puede quedar artificialmente
   balanceada por construcción.

## 5. Próximo programa prioritario — Rama `COUNT_VOLUME`

El siguiente trabajo no debe ser otra simulación directa. Primero se necesita una
puerta teórica condicionada por selección.

### CV-1 — Definir el experimento estadístico seleccionado

Congelar:

```text
S = {MIN_COVERAGE_LEX produce una cuadrupla unica},
observacion por intervalo = (m,n,side,S),
target = ell=sqrt(Delta u Delta v).
```

Debe quedar explícito si el estimando es:

- `E[ell | m,n,side,S]`;
- la distribución completa `P(ell | m,n,side,S)`;
- un intervalo de predicción;
- o una cota minimax de error.

No deben mezclarse estimación puntual, ranking individual y razón entre lados.

**Entregable propuesto:**

```text
emergencia/P1a_count_volume_experimento_condicionado_d2.md
```

### CV-2 — Derivar la ley sin selección

Para endpoints fijados y `N=n`, partir de:

```text
m-2 | A ~ Binomial(n-2,A),
A = ell^2.
```

Hay que registrar con precisión qué cambia cuando:

- los endpoints forman parte de la muestra;
- el intervalo es uno entre muchos candidatos;
- y la cuádrupla maximiza un score basado en `m`.

La fórmula binomial sin selección será un baseline matemático, no el modelo final.

### CV-3 — Incorporar el evento de selección

Objetivo central:

```text
P(ell | m,n,side,S).
```

Rutas posibles, en orden de preferencia:

1. factorización exacta o recurrencia en la representación por permutaciones;
2. cotas analíticas para el likelihood ratio seleccionado/no seleccionado;
3. enumeración exacta en tamaños pequeños para conjeturar la forma;
4. simulación calibrada solo después de congelar la aproximación.

No se ajustará una regresión flexible sobre los artefactos ya usados para descubrir
la rama y se presentará después como validación.

### CV-4 — Cota de resolución

La correlación moderada puede reflejar ruido finito corregible o una limitación del
target seleccionado. La pregunta apropiada es:

```text
Var(ell | m,n,side,S)
```

y, más generalmente, el riesgo mínimo de cualquier estimador medible respecto de la
observación congelada.

Se buscarán:

- varianza posterior/condicional;
- intervalos de predicción finitos;
- una cota inferior de Bayes, Le Cam o información;
- y su dependencia en `n`.

Si la cota inferior impide correlación o error útiles, la rama se cerrará sin ampliar
la cuadrícula numérica.

### CV-5 — Auditoría de circularidad antes de una razón

Antes de definir cualquier

```text
ell_hat_minus / ell_hat_plus
```

se debe cuantificar cuánto de su concentración proviene de que el selector maximiza
`min(m_minus,m_plus)`.

Preguntas mínimas:

- ¿la razón de cardinalidades queda forzada cerca de uno?
- ¿el target latente también queda concentrado cerca de uno?
- ¿queda variación suficiente para evaluar resolución?
- ¿un control con endpoints no seleccionados produce una dispersión distinta?

**Kill criterion conceptual:** si el selector determina casi por completo la razón
observable antes de aplicar el estimador, esa combinación selector–representación no
puede presentarse como recuperación independiente del target.

**Entregable propuesto:**

```text
emergencia/P1a_count_volume_auditoria_circularidad_d2.md
```

## 6. Gates posteriores posibles

### Gate CV-T — Teoría suficiente para nueva ejecución

Solo se abrirá una nueva simulación si CV-1 a CV-5 fijan:

- target y condicionamiento exactos;
- observable permitido;
- modelo o aproximación seleccionada;
- parámetros completos y semillas;
- separación desarrollo/validación;
- métricas y terminales;
- y un tratamiento explícito de circularidad.

Terminales propuestos:

```text
COUNT_VOLUME_THEORY_READY_FOR_INDEPENDENT_VALIDATION
COUNT_VOLUME_NONIDENTIFIABLE_UNDER_SELECTED_CHANNEL
COUNT_VOLUME_THEORY_INCONCLUSIVE
```

### Gate CV-N — Escalado en `n`

Si CV-T lo autoriza, una muestra independiente a tamaños mayores podrá distinguir:

- mejora real de resolución con densidad;
- plateau de correlación;
- concentración creciente del target;
- y sesgo de selección persistente.

Los tamaños, réplicas y umbrales no se fijan en esta hoja de ruta; pertenecerán a un
contrato nuevo. No se reutilizarán resultados de `n<=128` como validación.

### Gate CV-R — Posible razón

Solo podrá preregistrarse una razón si:

1. la representación individual supera su gate en ambos lados;
2. la ley condicionada está controlada;
3. la auditoría de circularidad pasa;
4. el target conserva dispersión no trivial;
5. y existe una muestra final independiente.

Hasta entonces:

```text
RATIO_STATUS = CLOSED
```

## 7. Ramas secundarias, no prioritarias

### S1 — Selector con mayor dispersión temporal

`MIN_COVERAGE_LEX` ofrece soporte y estabilidad, pero comprime la banda de duración.
Puede diseñarse otro selector order-only que imponga soporte suficiente sin maximizar
directamente el balance.

Requisitos:

- no usar altura o duración latente en el score;
- no fijar por construcción la razón futura;
- conservar equivariancia y abstención;
- repetir disponibilidad, estabilidad, borde y dispersión del target.

Esta rama no debe abrirse en paralelo a CV-1 salvo documento independiente, para no
mezclar fallo de representación con cambio de target.

### S2 — Salida conjuntista

En vez de exigir una cuádrupla única, estudiar el conjunto completo de maximizadores
puede conservar información que el selector puntual descarta.

Targets posibles:

- distribución de duraciones sobre el argmax;
- intervalos identificados por órbitas de automorfismos;
- funcionales simétricos del conjunto.

Requiere definir una pérdida para objetos conjuntistas; no es una extensión mecánica
del estimador puntual.

### S3 — Mayor densidad para altura

El `PARK` de altura se refiere a `n=64,96,128` y al selector actual. Una reapertura a
tamaños mayores necesitaría una razón teórica para esperar una tasa de mejora y un
contrato independiente. No debe realizarse solo porque la infraestructura permite
simular más.

### S4 — `d>=3`

No abrir hasta cerrar una pregunta concreta en `d=2`. En dimensiones superiores
desaparece la representación por una sola permutación, cambian las constantes de
cadenas y anchuras y aumenta el coste de selección.

```text
D_HIGHER_STATUS = PARKED_PENDING_D2_THEORY
```

### S5 — Estimador híbrido cadena + volumen (peso óptimo de varianza inversa)

Propuesta externa (2026-08-04): combinar `HEIGHT_ONLY` (`ell_hat_h=H/(2 sqrt(n))`,
nuestro análogo de un estimador basado en cadena máxima) y `COUNT_VOLUME`
(`ell_hat_count=sqrt((m-2)/(n-2))`, análogo de un estimador basado en volumen) con
un peso `alpha*(m,S)` que minimiza el MSE, en vez del promedio no ponderado que ya
falló en `HEIGHT_WIDTH` (Fase 6, `(H+W)/(4 sqrt(n))`). La distinción con
`HEIGHT_WIDTH` es real: ese combinaba altura y anchura (dos estadísticos
extremales) sin pesos; esto combinaría altura y conteo (un extremal y un agregado)
con pesos adaptativos de varianza inversa.

No se abre ahora. El protocolo propuesto exige generar un ensemble nuevo (con y sin
selector, para medir `Var(ell|m,S)`, `Var(ell|H,S)`, `Var(ell|m,H,S)` y estimar
`alpha*` con validación cruzada) — exactamente el tipo de ejecución que CV-3/CV-4
buscan evitar hasta agotar la vía puramente deductiva (ver
`emergencia/P1a_count_volume_cota_resolucion_d2.md`). Se aparca, no se descarta:

```text
S5_HYBRID_ESTIMATOR = PARKED_REQUIRES_NEW_SAMPLE
S5_DISTINCT_FROM_HEIGHT_WIDTH = YES (pesos optimos, no promedio)
S5_PRECONDITION = CV3_CV4_THEORETICAL_TRACK_EXHAUSTED_OR_STALLED
```

Si CV-3/CV-4 se estancan en la vía puramente deductiva, S5 es el candidato natural
para reabrir con su propio contrato (muestra nueva, partición train/test explícita
para evitar el sobreajuste de `alpha*` que la propia propuesta señala como riesgo).

## 8. Conexión con P2 y P3

### P2 — Escala absoluta con `rho` conocida

P2 debe conservar la ley aleatoria de `N` y una densidad conocida. No puede usar los
resultados `fixed-n` como prueba de escala absoluta. Su apertura requerirá otro modelo
generativo y otra pregunta de identificabilidad.

### P3 — Cotas finitas

CV-4 es ya un primer work package concreto de P3. Las cotas de riesgo condicionado
por selección pueden convertirse en la contribución teórica más importante de esta
línea, aunque ningún estimador puntual termine superando el gate.

## 9. Orden recomendado de trabajo

```text
AHORA
  -> CV-1 definir experimento seleccionado
  -> CV-2 baseline binomial sin seleccion
  -> CV-3 ley condicionada por seleccion
  -> CV-4 cota de resolucion
  -> CV-5 auditoria de circularidad

DESPUES, SEGUN TERMINAL CV-T
  -> validacion independiente a mayor n
  -> o cierre de COUNT_VOLUME

SOLO SI PASAN TEORIA, RESOLUCION Y CIRCULARIDAD
  -> preregistrar una razon

EN PARALELO SOLO COMO LINEAS SEPARADAS
  -> selector con mayor dispersion
  -> salida conjuntista
  -> P2 escala absoluta
  -> P3 cotas finitas generales
```

## 10. Próxima acción concreta

La siguiente acción recomendada es documental y matemática:

```text
crear P1a_count_volume_experimento_condicionado_d2.md
```

Debe contener:

1. definición exacta de `S`, observación y target;
2. baseline binomial para endpoints fijados;
3. diagrama de dependencias introducidas por `MIN_COVERAGE_LEX`;
4. cantidades que deben derivarse antes de simular;
5. criterios para decidir entre cálculo exacto, cota o aproximación;
6. y terminales de la puerta teórica.

No se recomienda todavía:

- calcular un cociente;
- ajustar una regresión sobre los CSV existentes;
- ampliar `n` sin hipótesis de tasa;
- abrir `d>=3`;
- ni reinterpretar `COUNT_VOLUME` como escala absoluta.

## 11. Estado de control

```text
ROADMAP_VERSION = 1.0
ROADMAP_DATE = 2026-08-03
CURRENT_PRIORITY = COUNT_VOLUME_SELECTION_CONDITIONAL_THEORY
CURRENT_NUMERICAL_AUTHORIZATION = NONE
CURRENT_RATIO_AUTHORIZATION = NONE
CURRENT_HIGHER_DIMENSION_AUTHORIZATION = NONE
NEXT_DELIVERABLE = P1a_count_volume_experimento_condicionado_d2.md
NOVELTY_CERTIFIED = NO
```

## 12. Actualización — CV-1/CV-2 entregados

El entregable de §10/§11 fue producido:

```text
emergencia/P1a_count_volume_experimento_condicionado_d2.md
```

Congela el estimando (ley condicional `L(ell|m,n,side,S)` vía media y varianza, sin
mezclar ranking ni razón), deriva con demostración el baseline binomial
`m-2|A ~ Binomial(n-2,A)`, traza el diagrama de dependencias que introduce el argmax
de `MIN_COVERAGE_LEX` y fija el orden de rutas (exacta, cota, enumeración pequeña,
simulación calibrada) para CV-3. No calcula ningún resultado numérico ni resuelve
CV-3, CV-4 o CV-5.

```text
CV1_CV2_STATUS = COMPLETE
NEXT_DELIVERABLE = P1a_count_volume_ley_condicionada_d2.md
CURRENT_PRIORITY = COUNT_VOLUME_SELECTION_CONDITIONAL_THEORY (sin cambio)
CURRENT_NUMERICAL_AUTHORIZATION = NONE (sin cambio)
```

## 13. Actualización — CV-3, Ruta 1 (resultado parcial)

```text
emergencia/P1a_count_volume_ley_condicionada_d2.md
```

Demuestra que, condicionado a la forma discreta (rangos) del hueco ganador, la ley
geométrica de `A` (y por tanto de `ell`) es exactamente un producto de dos Beta
independientes, **sin ninguna distorsión por la selección**: toda la acción de
`MIN_COVERAGE_LEX` ocurre en qué forma resulta ganadora (objeto puramente
combinatorio sobre la permutación `pi`), no en la geometría del hueco una vez fijada
la forma. Da también la ley marginal exacta de `m` dado la forma (hipergeométrica,
verificada a mano para `n=4`). Deja abierto el peso combinatorio
`w(s|m,n,side,S)` — cuántas permutaciones producen cada forma ganadora — que ahora
es la única pieza pendiente tanto para CV-3 como, releída, para CV-4 y CV-5.

```text
CV3_STATUS = PARTIAL_COMPLETE_STRUCTURAL_RESULT_ONLY
CV3_ROUTE1_STATUS = PARTIAL_SUCCESS_NOT_ABANDONED
CURRENT_NUMERICAL_AUTHORIZATION = NONE (sin cambio)
```

## 14. Actualización — CV-4, cota inferior conservadora (resultado parcial)

```text
emergencia/P1a_count_volume_cota_resolucion_d2.md
```

Demuestra que `Var(ell|m,n,side,S) >= min` de la varianza geométrica cerrada sobre
el conjunto de formas compatibles con haber observado ese `m` — una cota que **no
necesita** resolver el peso combinatorio `w(s|m,n,side,S)` que CV-3 dejó abierto,
solo una restricción de soporte hipergeométrico. Verificada a mano en un caso de
juguete (`n=4,m=3`: cota `0.0220`, desviación típica `>=0.148`). No calcula el
número comparable al régimen publicado (`n=64,96,128`); eso requeriría una
evaluación determinista (no estocástica) de la fórmula cerrada, ejecución nueva no
autorizada aquí. Rama secundaria `S5` (híbrido cadena+volumen, propuesta externa)
registrada y aparcada en §7 hasta que la vía deductiva CV-3/CV-4 se agote.

```text
CV4_STATUS = PARTIAL_STRUCTURAL_BOUND_ONLY
CURRENT_NUMERICAL_AUTHORIZATION = NONE (sin cambio para muestras nuevas/estocasticas)
```

## 15. Actualización — CV-4 evaluada en `n=64,96,128`

La cota conservadora se evaluó (lectura determinista, sin generar datos nuevos)
sobre la muestra ya sellada de Fase 6:

```text
n=64:  cota/MSE ~ 0.28   n=96:  cota/MSE ~ 0.31   n=128: cota/MSE ~ 0.33
```

La cota —deliberadamente débil, sin resolver `w` ni apretar la restricción del lado
opuesto— ya cubre al menos un tercio de la escala del error cuadrático observado de
`COUNT_VOLUME`, de forma estable en los tres tamaños. `B_n/MSE_obs` no es una
descomposición del error; lo que la cota respalda es la **obstrucción a la
identificación por instancia**. La otra mitad de la hipótesis del PI (la
"calibrabilidad en promedio", [[emergencia-count-volume-strategic-assessment]] en
memoria) no se deduce de CV-4: necesita la evidencia de calibración de Fase 6.

```text
CV4_STATUS = PARTIAL_STRUCTURAL_BOUND_EVALUATED_ON_PUBLISHED_REGIME
CURRENT_NUMERICAL_AUTHORIZATION = NONE (sin cambio para muestras nuevas/estocasticas)
```

## 16. Actualización — CV-4 traducida a correlación (ítem 1 cerrado)

`emergencia/P1a_count_volume_cota_correlacion_d2.md`. Teorema CV-4.2: para todo
estimador medible respecto de `(m,n,side,S)`,
`rho^2 <= 1 - B_n/Var(Y_n)`. Demostrado minimizando sobre todo recalibrado afín, así
que `B_n` **sigue siendo cota inferior después de calibración afín** (verificado
además empíricamente en los seis estratos, junto con `rho_obs <= rho_max_ub_Bn`).

```text
B_n/Var(Y_n)   = 0.27-0.31   frente al umbral de exclusion 1-0.80^2 = 0.36
rho_max_ub_Bn  = 0.831-0.857 (COTA SUPERIOR, no rho_max; gate no excluido por ella)
NRMSE_sigma,min = 0.515-0.556
k_necesario    = 1.17-1.36
rho_obs        = 0.530-0.566
```

> **Corrección (§18).** `rho_max_ub_Bn` es una cota superior inducida por `B_n`, no
> la correlación máxima. La lectura original de este apartado —«brecha del estimador
> >> brecha techo-gate»— **queda retractada**: el `rho_max` real del canal es
> `0.532-0.568`, luego `rho_obs` está a `<=0.0007` del óptimo y **la brecha es de la
> información, no del estimador**.

Resultado operativo: el ítem 2 (apretar `F_relax` con el hueco del lado opuesto)
pasa de objetivo cualitativo a **objetivo numérico**: un factor `>=1.36` sobre `B_n`
excluiría el gate en los seis estratos, `>=1.17` solo en `n=128` futuro. Si el
apriete alcanzable queda por debajo de `1.17`, la exclusión estructural del gate por
esta vía queda descartada sin necesidad de resolver `w`. **No abordar `w` antes.**

```text
CV4_METRIC_TRANSLATION = DONE
CV4_GATE_0.80_STRUCTURALLY_EXCLUDED_BY_BOUND = NO
NEXT_DELIVERABLE = apretar F_relax (item 2), objetivo factor >= 1.36
CURRENT_NUMERICAL_AUTHORIZATION = NONE (sin cambio para muestras nuevas/estocasticas)
```

## 17. Actualización — ítem 2 cerrado por un argumento: vía descartada

`emergencia/P1a_count_volume_techo_apriete_d2.md`. Antes de invertir en apretar
`F_relax`, se acotó analíticamente el factor máximo que esa vía puede aportar.

Teorema CV-4.3: la restricción del lado opuesto (`k_-,l_- <= n-3`, de
`alpha<beta<gamma<delta` con `k_+,l_+>=1`) es una cota **superior**, y la esquina
inferior `s_min(m)=(max(2,m-1),max(2,m-1))` es factible siempre que `m<=n` y
sobrevive a **cualquier** apriete que solo baje cotas superiores. Luego
`B_n^tight <= E_m[Var(ell|s_min(m))]`, techo independiente de lo agresiva que sea la
restricción.

```text
factor con la restriccion concreta k,l<=n-3 : 1.000000
factor MAXIMO de cualquier apriete por arriba: 1.000017   (se necesitaba >= 1.17)
```

Razón estructural: `Var(ell|k,l)` es pequeña en ambos extremos del rango de `k` (con
`k` pequeño porque la escala lo es; con `k` cerca de `n` porque `Beta(k,n+1-k)` se
concentra), y el mínimo vive en el extremo inferior — justo el que las cotas
superiores no tocan. El `argmin` ya está en la esquina inferior en 72 de los 74
pares `(m,n)` de la muestra.

**Consecuencia:** el ítem 2 queda cerrado sin evaluación cara. La única vía viva para
subir `B_n` es elevar la cota **inferior** sobre `(k,l)` — demostrar que las formas
con `k` o `l` cerca de `m-1` no pueden ganar el argmax del selector. Eso es
exactamente `w(s|m,n,side,S)`. La exclusión estructural del gate `0.80` pasa
íntegramente por `w`, o no pasa; no hay atajo intermedio.

```text
CV4_TIGHTER_FEASIBLE_SET = DONE_AND_CLOSED
CV4_ITEM2_VERDICT = ABANDON_ROUTE_WITHOUT_RESOLVING_W
CV4_ONLY_REMAINING_ROUTE = LOWER_BOUND_ON_(k,l) == w (Ruta 1, CV-3 Seccion 11)
NEXT_DECISION = si w merece el coste, o si CV-4 se cierra donde esta
CURRENT_NUMERICAL_AUTHORIZATION = NONE (sin cambio para muestras nuevas/estocasticas)
```

> **La conclusión `CV4_ONLY_REMAINING_ROUTE = w` de este apartado queda superada por
> §18: era cierta solo dentro de la vía de la descomposición en formas.**

## 18. Actualización — el canal `G` es `sigma(m)`; `w` era innecesario

`emergencia/P1a_count_volume_canal_sigma_m_d2.md`. **PENDIENTE DE AUDITORÍA
INDEPENDIENTE DE PUNTO ÚNICO**; no sustituye todavía al cierre de CV-4.

Dentro de un estrato, `n` y `side` son constantes y `S` es un evento, luego
`G = sigma(m,n,side,S) = sigma(m)`; y `COUNT_VOLUME = sqrt((m-2)/(n-2))` es biyección
creciente de `m`, luego `sigma(COUNT_VOLUME) = G`. La clase de estimadores
`G`-medibles **es** la clase de funciones de `COUNT_VOLUME`, y `rho_max` es una
identidad finito-muestral (ANOVA de un factor sobre `m`, `K=19..29` bins) sobre la
muestra ya sellada: sin `w`, sin `F_relax`, sin iid, sin bootstrap, sin ejecución
nueva.

```text
T_emp = SSW/SST     = 0.6773-0.7175   (umbral de exclusion: > 0.36)
rho_max_emp         = 0.5315-0.5681   (gate: 0.80)
CV4_SEALED_SAMPLE_STATUS = GATE_EXCLUDED_EXACTLY
CV4_POPULATION_STATUS = STRONGLY_SUPPORTED_UNDER_IID_NOT_CLOSED_FORM_THEOREM
W_STATUS = UNNECESSARY_FOR_SEALED_G_CHANNEL
```

`B_n` era floja por un factor `2.27-2.56`; toda la flojedad estaba en el paso
`min_{F_relax}`. El factor `1.17-1.36` que faltaba sí existía, pero no por donde se
buscaba. CV-4.1 y CV-4.3 siguen siendo correctos y no quedan contradichos
(`B_n <= E[Var(Y|G)]` en los seis estratos); dejan de estar en el camino crítico.

**Retractación registrada:** `P1a_count_volume_cota_correlacion_d2.md` §3. Los
`0.83-0.86` no eran `rho_max` sino una cota superior vía `B_n`
(`rho_max_ub_Bn`), y la lectura «la brecha es del estimador» es falsa
en el sentido opuesto: `COUNT_VOLUME` está a `<=0.0007` en `rho` del óptimo
`G`-medible. **La obstrucción es de la información, no del estimador.**

```text
CV4_AUDIT_ROUND_1 = FAIL_MATERIAL (T_oos presentado como cota; retractacion
                   incompleta en el repo; frase historica "brecha del estimador")
CV4_AUDIT_ROUND_1_FIXES = APPLIED (intervalo [0.679,0.721] retirado; rho_max_ub_Bn
                   renombrado en los 4 documentos y en el ejecutable del item 1;
                   frase historica retirada de §16)
CV4_AUDIT_ROUND_2 = FAIL_MATERIAL (renominacion incompleta en 2 superficies:
                   cabecera de salida del ejecutable del item 1 y clave del estado
                   de control documental)
CV4_AUDIT_ROUND_2_FIXES = APPLIED (rho_max_ub_Bn / CV4_RHO_MAX_UB_BN exactos en las
                   27 apariciones; recuento de controles -> seis; retirada la
                   contradiccion del techo de afirmacion de CV-4.1 §6)
CV4_AUDIT_ROUND_3 = FAIL_MATERIAL (CV-4.1 §8 reactivaba como vigente la lectura
                   refutada de "MSE no explicado" y margen del estimador)
CV4_AUDIT_ROUND_3_FIXES = APPLIED (retirada la accion obsoleta de CV-4.1 §8;
                   estados NOT_DONE y acciones pendientes sustituidos por remision
                   al resultado canonico DONE_AND_CLOSED de §17)
CV4_AUDIT_ROUND_4 = FAIL_MATERIAL (T_emp atribuido hasta n=16000 sin artefactos
                   mas alla de n=128; identidad, hashes y codigo = PASS)
CV4_AUDIT_ROUND_4_FIXES = APPLIED_BY_PI_AUTHORISATION_2026_08_17 (las cuatro
                   expresiones de tres superficies dicen ahora n=64,96,128)
CV4_AUDIT_ROUND_5 = PASS_AFTER_DOCUMENTARY_REMEDIATION
CV4_AUDIT_STATUS = CLOSED_PASS
AUDIT_POINT = emergencia/p1a_count_volume_canal_sigma_m_d2.py
AUDIT_ITEMS = (1) definicion literal de S, (2) ANOVA empirico exacto,
              (3) funcion de influencia + etiqueta "correccion intrabin"
CV4_4_POPULATION_LEMMA = SCOPED_DOWN (P1a_count_volume_lema_kl_d2.md): solo la
                   pieza Beta-producto, NO el b completo. Identidad exacta
                   Var(ell|k,l)=kl/(n+1)^2*(1-R(k,n)R(l,n)) derivada
                   algebraicamente; cadena de Wendel escrita y uniforme sobre
                   TODAS las formas 1<=k,l<=n, incluidas las degeneradas:
                   P_{1,n}<= (n+1/4)/(n+1)^2 <= 1/n. La cota puntual elimina la
                   dependencia de w_n para P_1; no hace falta un lema de
                   no-degeneracion ni controlar colas del selector. Estados:
                   BETA_PRODUCT_IDENTITY = NUMERICALLY_VERIFIED_DERIVATION_PENDING
                   WENDEL_SOURCE = UNVERIFIED_LOCALLY
                   A2_CONDITIONAL_VARIANCE_BOUND = UNIFORM_ALL_SHAPES_PENDING_AUDIT
                   A3_SELECTOR_TAIL_OR_NONDEGENERACY_FOR_P1 = UNNECESSARY
                   A4_P1_ANALYTIC_REGIME = RESOLVED_PENDING_IDENTITY_WENDEL_AUDIT
                   A4_NEW_EXECUTION_REQUIRED = NO
                   P2_SCALING = OPEN_REQUIRES_W_N
                   FULL_B_SCALING = NOT_ESTABLISHED
                   La heuristica 1/(4k)+1/(4l) queda RECHAZADA como base de prueba:
                   yerra hasta +143% cuando k,l = Theta(n).
CV4_RICHER_CHANNEL_STATUS = OUT_OF_SCOPE_ONLY_LINEAR_FAMILY_TESTED
CURRENT_NUMERICAL_AUTHORIZATION = NONE (sin cambio para muestras nuevas/estocasticas)
```

## 19. Decisión del PI (2026-08-05) — estado limpio y redirección

Cierra la ruta B (§13 de `emergencia/P1a_puerta_teorica_en_Minkowski.md`, certificado
de unicidad por familia prescrita). Firmada en
`docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md` §11;
detalle técnico en §13.9 de la puerta teórica.

### 19.1 El estado limpio, en cuatro puntos

1. **Mecanismo plantado: válido.** La ruta B aportó una idea combinatoria real —
   prescribir `F_B` y colocar la cuádrupla en el máximo exacto del paisaje libre.
2. **Certificado: incompleto e innecesario.** No cierra (inconsistencia de banda —
   Def. 13.1 mal formada para `rho >= n/4` y Lema 13.4 `FALSE_AS_WRITTEN`— y cota
   aplicada al bloque equivocado —Lema 13.9, caso 2 de la Prop. 13.12—). Y aun
   parcheado seguiría siendo estratégicamente vacío en `n ≈ 64–128`: `n_0` cae entre
   `5.7e4` y `1.2e9` según `C`. Una cota de `Pr(S)` que solo empieza a funcionar tan
   lejos no aporta nada utilizable.
3. **Objetivo absoluto `P_{2,n} -> 0`: descartado por vacuidad.** El colapso conjunto
   de numerador y denominador (Advertencia 13.16) lo liquida como demostración de
   recuperación. No es que sea difícil: es que sería verdadero y no diría nada.
4. **Problema normalizado: abierto.** Solo el cociente `T_n = 1 - rho_max^2` conserva
   sustancia. El `~0.70` observado exclusivamente en `n ∈ {64,96,128}`
   (`T_emp ∈ [0.6773, 0.7175]`, seis estratos) es **evidencia numérica finita,
   no un teorema ni evidencia hasta `n=16000`**. La pregunta es
   `liminf T_n > 0`, o una variante cuantitativa más fina.

Esto evita cerrar un teorema correcto pero científicamente vacío, y señala el lugar
exacto donde podría residir el resultado real.

### 19.2 Lo que NO se prioriza

- **Reparar el certificado.** No se reanuda. Las reparaciones escritas en §13.2 y
  §13.5 quedan como `SKETCH` no verificado por terceros, y ahí se quedan.
- **Más fuerza bruta computacional.** La verificación exhaustiva C2 del comité 050
  no se ejecuta y su contrato no se congela. `G_n` es vacuo a todo `n` enumerable;
  el propio comité no la recomendaba.

### 19.3 Redirección

La **objeción dimensional** (Braun `d >= 3`, `docs/bibliography_claims.md` §1.3;
Madsen `d > 2` vía Müller, §2.5bis) afecta la **vía de identificabilidad** que
exploraba esta hoja de ruta —reconstrucción/embedding a partir de orden y número—,
que es donde esos teoremas viven y donde excluyen `d=2`.

**No toca automáticamente la línea de horizonte** en la reducción esféricamente
simétrica `(t, r)`, que es el programa principal del repositorio (`README.md`,
`docs/preregistration*.md`): ahí la pregunta es de **recuperabilidad** de estructura
de horizonte, no de identificabilidad del espaciotiempo. El esfuerzo se concentra ahí
a partir de ahora.

**Perímetro vigente de esa línea, que esta redirección NO altera.** La línea de
horizonte está bajo cierre **deóntico** (`docs/program_closure_note_2026-07-30.md`,
firmado tras el acta 049) con reapertura **acotada**
(`docs/program_reopening_note_2026-07-31.md`), cuyo perímetro es una lista cerrada de
dos ítems —**R1**, llevar `docs/manuscript_limits_draft.md` a entregable; **R2**,
derivar analíticamente el exponente `kappa ~ lambda^6`— y cuya regla §6.1 dice
literalmente: *«Perímetro fijo: R1 y R2. Nada entra sin una nueva nota firmada.»*
Reconstrucción de horizonte en cualquier reformulación sigue **cerrada**. La
redirección de §19.3 apunta en la dirección de **límites**, que es la que la
reapertura autoriza; cualquier cosa fuera de R1/R2 exige nota nueva firmada, no esta
sección. Cajas de tiempo vigentes: R2 hasta **2026-08-14**, conjunto hasta
**2026-09-11**.

**Ampliación efectiva (2026-08-05).** El perímetro pasó a tres ítems con la firma de
`docs/program_reopening_note_2026-08-05_R3.md`: **R3**, la dicotomía de cópula nula en
`d=2` (`research_program/work_packages/wp6_d2_null_copula_dichotomy.md`). R3 cede
explícitamente el gate de WP5 —`1+1D` deja de tener que servir a `3+1D`— porque su valor
está en que `d=2` es la dimensión que HKMM, Braun y Madsen excluyen. Las cajas de tiempo
de R1 y R2 **no** se prorrogan por ello.

Registrado con precisión, porque la diferencia importa: «no toca automáticamente» es
un enunciado de **alcance**, no una afirmación de transferencia. Que la exclusión
dimensional no se aplique no demuestra que la línea de horizonte esté libre; demuestra
que la objeción publicada no la alcanza por ese camino.

### 19.4 Deuda que NO se cancela

- La auditoría independiente de punto único de §18
  (`emergencia/p1a_count_volume_canal_sigma_m_d2.py`) sigue **pendiente**; el cierre
  de la ruta B no la sustituye ni la anula.
- Los puntos 3, 4 y 5 de la lista `OPEN` de §13.8 quedan como deuda **archivada** de
  una sección cerrada, no como trabajo pendiente.

```text
RUTA_B_STATUS = CLOSED_UNREPAIRED_BY_PI_2026-08-05
PLANTED_MECHANISM = VALID_IDEA_RETAINED
PRESCRIBED_FAMILY_CERTIFICATE = INCOMPLETE_AND_UNNECESSARY
ABSOLUTE_TARGET_P2_TO_ZERO = DISCARDED_AS_VACUOUS
NORMALISED_CHANNEL_LIMINF_T_N = OPEN_ONLY_LIVE_QUESTION
T_N_EVIDENCE = EMPIRICAL_ONLY_N_64_96_128_NOT_A_THEOREM
CERTIFICATE_REPAIR = NOT_PRIORITISED
BRUTE_FORCE_VERIFICATION = NOT_AUTHORISED
DIMENSIONAL_OBJECTION_SCOPE = IDENTIFIABILITY_ROUTE_NOT_AUTOMATICALLY_HORIZON_LINE
NEXT_FOCUS = HORIZON_LINE_IN_SPHERICALLY_SYMMETRIC_T_R_REDUCTION
CV4_SINGLE_POINT_AUDIT = STILL_PENDING_NOT_CANCELLED
```

## 20. Cierre del tramo `covtree` (2026-08-06)

Se registra aquí para que esta hoja siga siendo el libro mayor único de lo abierto y lo
cerrado. **`covtree` es una línea deliberadamente disjunta de `nachocausal`**: sin
embeddings, sin conos, sin horizontes y sin sprinklings. No entra en el perímetro de
reapertura R1/R2/R3 de §19.3, **no lo consume ni lo amplía**, y no cancela ninguna de las
deudas de §19.4. La regla §6.1 de la nota de reapertura sigue intacta.

**Problema.** Gutzeit–Shaban–Yeats–Zalel, *Sizes of witnesses in Covtree*,
arXiv:2605.00622v1. Dado `Gamma_n` de `k` posets no etiquetados de talla `n`, `Q` es
*testigo* si `Gamma_n` es exactamente el conjunto de tipos de sus `n`-downsets. Para `k=3`
los autores prueban `|Q| <= (3/2)(n+1)` (enunciado **existencial**) y conjeturan
`|Q| <= n+3`, sin poder demostrarlo.

### 20.1 Lo que queda establecido

1. **Gate `n=6`, `k=3` — SELLADO en `87c2d49`.** Todo nodo `Gamma_6` con `|Gamma_6| = 3`
   posee un testigo de talla `<= 9 = n+3`, en todas las alturas; condicionado al Teorema
   5.1 del artículo. Sello re-verificado el 2026-08-06 y reproduce exacto (fuente
   `f2264bdf…`, salida `bf314aa2…`, exit 0). **No se avanza ni se toca.**
2. **`Max(Q) ∩ U != vacío` — DEMOSTRADO**, para todo `n`, todo `m >= 3` y `k = 3`, bajo
   las hipótesis auténticas de §5 del artículo. Nada usa `n = 6`. Cadena: Lema A (los
   maximales de cada mitad de la amalgama lo son de `Q`; no necesita §5), Lema B
   (`dist(A,C) = m` por Prop. 4.4 fuerza `>= m-1` copias interiores distintas de `tau_B`,
   luego un tipo de multiplicidad 1 nunca es `tau_B`) y el Lema 5.2 importado.
3. **`|Max(Q)| = 2 <=> Q irreducible` — PROBADO en `n=6`, `m=4`**, con una dirección
   **vacua**: no existe ninguna instancia §5-admisible con `>= 3` maximales a esa talla.
4. **Lema de camino corto — PROBADO, todo `n`.** Si `L` es la longitud del camino
   especial mínimo global en `G_n(Q)`, la unión de sus vértices es un sub-testigo de talla
   `<= n+3` cuando `L <= 3`. Reproduce `740/748` reducibilidades **sin enumerar downsets**
   y reformula la conjetura: *todo nodo admite un testigo con `L <= 3`*.

Registro: rama `covtree/regularidad-u` = **`c98ed7d`**, hija de `87c2d49`, empujada a
`origin`. Documento `covtree/regularidad_de_U.md`; artefactos `covtree/regularity_u.cpp` y
`covtree/s5_xtab.cpp`, que reutilizan sin modificar la maquinaria de enumeración sellada.

### 20.2 El error de clase, que es la lección

La bandera «§5» usada al principio sólo pedía que **existiera** un camino `A-B-B-B-C` de
longitud 4. El montaje del artículo (p. 14) exige minimalidad **fuerte global**: ningún
camino más corto de esa forma **para ninguna terna de tipos distintos**. Con el criterio
correcto, **8 de las 748** amalgamas del barrido son §5-admisibles, no 284.

- En las 276 restantes el Lema 5.2 es **falso** (5782 violaciones), verificado a mano.
- Las `740` no estrictas quedan **correctamente fuera** del contraste del Lema 5.2: ni lo
  confirman ni lo refutan. Su reducibilidad sí queda *demostrada*, por §20.1(4).
- El sello **no** se ve afectado: el gate sólo exige que lo barrido sea un
  **superconjunto** de los testigos mínimos de talla 10, y la sobre-enumeración únicamente
  puede añadir supervivientes, nunca ocultarlos. Lo corregido es el uso *interpretativo*
  de la submuestra, no el veredicto.

Lección transferible, del mismo tipo que las de §4: *una submuestra etiquetada con el
nombre de una hipótesis no satisface la hipótesis*. Toda estadística «dentro de §5»
anterior a `c98ed7d` está medida en la clase equivocada y queda retirada.

### 20.3 Lo que sigue abierto y lo que se congela

- **«Exactamente uno» (`|Max(Q) ∩ U| = 1`): ABIERTO.** La estructura sólo entrega `>= 1`;
  no hay ningún paso que acote por arriba. Evidencia finita `8/8`, sin respaldo
  estructural. La refutación anterior (valores 1,2,3,4) queda **retirada** por estar medida
  fuera de §5. No se afirma en ninguna dirección.
- **Recíproco `|Max(Q)| >= 3 => Q reducible`:** su único contenido no trivial vive en
  `n >= 7`. En `n = 6` es cierto por vacuidad, de modo que **no hay nada que ganar
  buscándole evidencia a `n = 6`**.
- **Decisión del PI (2026-08-06): tramo CONGELADO.** Sin abrir `n >= 7`, sin más
  enumeraciones y sin tocar el sello. No queda deuda técnica ni lógica inmediata.
  Riesgo de scooping real y vigente: grupo activo de Yeats (NSERC/Perimeter), tesis de
  Shaban 2025. Cualquier reapertura empieza por `n >= 7` y exige decisión nueva.

```text
COVTREE_TRACK_STATUS = FROZEN_BY_PI_2026-08-06
N6_K3_GATE = SEALED_AT_87c2d49_REVERIFIED_BYTE_EXACT
REGULARITY_OF_U = PROVED_ALL_N_ALL_M_GE_3_K_3
EXACTLY_ONE_MAXIMAL_IN_U = OPEN_NO_STRUCTURAL_SUPPORT
PRIOR_REFUTATION_OF_EXACTLY_ONE = WITHDRAWN_MEASURED_OUTSIDE_S5
MAX2_IFF_IRREDUCIBLE = PROVED_AT_N6_CONVERSE_VACUOUS
SHORT_PATH_LEMMA = PROVED_ALL_N_REPRODUCES_740_OF_748
N_PLUS_3_CONJECTURE = REFORMULATED_AS_EXISTS_WITNESS_WITH_L_LE_3
S5_ADMISSIBLE_INSTANCES = 8_OF_748_NOT_284
NON_STRICT_740 = OUTSIDE_LEMMA_5_2_TEST_BY_CONSTRUCTION
N_GE_7 = NOT_OPENED_REQUIRES_NEW_DECISION
COVTREE_PERIMETER_RELATION = DISJOINT_DOES_NOT_CONSUME_R1_R2_R3
```

## 21. Figuras del manuscrito de límites — LISTAS (2026-08-06)

Decisión del PI: hacer el manuscrito **pedagógico**, dirigido a estudiantes antes que a
especialistas. Registrado aquí porque cambia el vehículo, no el contenido: los teoremas
son los mismos, lo que cambia es a quién se le explican.

**Motivo.** La relatividad general se vende sola con la malla elástica hundida. Los
conjuntos causales se dibujan siempre de dos maneras —diagramas de Hasse abstractos, o
puntos en Minkowski con conos encima— y **ninguna enseña qué deja de ver el orden**, que
es exactamente de lo que vive este manuscrito. Esa figura no existe en el campo.

Nota de método que conviene no perder: dirigir las figuras a estudiantes **sube** el
listón de exactitud, no lo baja. Un especialista lee el pie de figura y perdona una
imprecisión; un estudiante se cree el dibujo literalmente.

### 21.1 Lo entregado

Cinco figuras en `viz/`, en inglés (el manuscrito lo está), commits `e4eb5d5`
(primera versión) y `0f6e8a6` (traducción íntegra: etiquetas, docstrings, nombres de
función, ficheros y README).

| # | Fichero | Qué demuestra | Ancla |
|---|---|---|---|
| 1 | `fig01_dictionary.py` | Qué se tira a la basura al pasar del espaciotiempo al causet | — |
| 2 | `fig02_invisible_scale.py` | La escala absoluta es invisible al orden | Teorema 3.1 |
| 3 | `fig03_teleology.py` | Lo que pasa fuera del parche no está en el parche | Teorema 3.2 |
| 4 | `fig04_box_wall.py` | Por qué murieron los localizadores C1–C5 | acta 042 |
| 5 | `fig05_what_is_recoverable.py` | Lo que el orden **sí** lee: `r/r_s` | pareja de la 2 |

**Las figuras 2 y 5 son una pareja y deben ir juntas.** La 2 dice que `r_s` es
invisible; la 5, que `r/r_s` no lo es. Son la tesis del manuscrito en dos imágenes.

Ejecución: `python3 viz/make_figures.py`. Semilla fija por figura; dos ejecuciones dan
hashes idénticos.

### 21.2 Por qué esto no son ilustraciones sino cálculos

Dos propiedades exactas de Schwarzschild 1+1 hacen el código auditable de un vistazo,
documentadas línea a línea en `viz/causet_core.py`:

1. `det g = -1`, luego la forma de volumen es `dt dr` y el sprinkling es **uniforme en
   el rectángulo `(t, r)`** — cualquier peso en el código sería un error;
2. en coordenadas tortuga la métrica es conformemente plana, luego el orden causal es
   **exactamente** el orden producto en las nulas `(u, v)`. No se integra ninguna
   geodésica ni se aproxima nada.

Dos comprobaciones **abortan la figura** en vez de dibujar algo falso: `fig02` verifica
que `Φ_s` preserva el orden elemento a elemento; `fig03`, que las dos continuaciones
dejan el parche observado idéntico.

Cifras impresas en los propios paneles:

- `fig02` — 0 discrepancias de orden en 12×12 relaciones.
- `fig04` — `corr(|J+|, t) = -0.951`, `corr(|J+|, r) = +0.164`, en banda `+0.465`. Es
  decir: **la pared de la caja explica el 91 % de la varianza** del observable más
  natural del orden, y la física sólo reaparece al condicionar a una banda temporal
  estrecha. Es el modo de fallo del ledger C1–C5, ahora con cifras propias.
- `fig05` — `|r_s=1 − r_s=7|` máx = `0.0101` frente a desviación típica `0.0248`.

### 21.3 Trampa registrada para que no se reintroduzca

El Teorema 3.1 es `TV = 0` entre **leyes**, no entre realizaciones. Dos sprinklings
*independientes* a masas distintas **no** dan el mismo poset. Lo que ocurre es que
`Φ_s` es un isomorfismo de orden, y el teorema es lo que convierte esa construcción en
genérica en vez de en un caso escogido. Si una versión futura de la figura —o un pie de
figura— sugiere «dos tiradas independientes salieron iguales», **afirma algo falso y hay
que rechazarla**. Va escrito en `viz/README.md` para que sobreviva a esta sesión.

### 21.4 Lo que sigue sin hacerse

Las figuras no tocan el sello (`thresholds.py sha256 = 6e2c3888…` verificado intacto),
no consumen la banda de semillas reservada y no afirman reconstrucción.

Queda pendiente, y es lo único que separa el material de un entregable:

1. insertar las cinco en `docs/manuscript_limits_draft.md` con sus pies —el pie de la
   Figura 2 debe llevar la distinción leyes/realizaciones de §21.3, que es donde mira un
   árbitro—;
2. ~~retirar el token `NOT_FOR_ARXIV`~~ — **HECHO (2026-08-06)**. Sustituido por
   `CLEARED_FOR_ARXIV_BY_PI_2026-08-06`, con la condición previa de verificación de
   sello descargada en el propio acto (`thresholds.py sha256 = 6e2c3888…`, coincide
   con `docs/preregistration_002.md`). La cabecera registra qué anula esa decisión y
   qué no: anula la cláusula 3 de la nota de cierre («se conservan como registro… no
   como anuncio»); **no** anula `NO_PUBLIC_NOVELTY_CLAIM`, que sigue vigente y es
   compatible, porque un paper de límites no afirma prioridad.

**Estado del repositorio en esta fecha:** siete ramas locales sincronizadas con
`origin`; `covtree/n6-gate` sellada en `87c2d49` y `covtree/regularidad-u` en `c98ed7d`;
`emergencia/p1a-canal-sigma-m` en cabeza. El trabajo vive en rama, **no en `main`**: quien
llegue a la portada del repositorio no ve nada de esto.

```text
FIGURES_STATUS = READY_FIVE_FIGURES_ENGLISH_COMMITTED
FIGURES_LANGUAGE = ENGLISH_MATCHING_MANUSCRIPT
FIGURES_REPRODUCIBLE = BYTE_IDENTICAL_ACROSS_RUNS
FIGURES_SELF_CHECKING = FIG02_AND_FIG03_ABORT_ON_FALSE_HYPOTHESIS
FIG02_FIG05 = A_PAIR_MUST_TRAVEL_TOGETHER
BOX_WALL_QUANTIFIED = 91_PERCENT_OF_VARIANCE_IS_THE_APPARATUS
LAWS_VS_REALISATIONS_TRAP = RECORDED_IN_VIZ_README
SEAL = UNTOUCHED_6e2c3888
MANUSCRIPT_INSERTION = PENDING
NOT_FOR_ARXIV_TOKEN = WITHDRAWN_2026-08-06_SEAL_VERIFIED_AT_CLEARANCE
NO_PUBLIC_NOVELTY_CLAIM = STILL_IN_FORCE_NOT_SUPERSEDED
CLOSURE_NOTE_CLAUSE_3 = SUPERSEDED_BY_PI_CLEARANCE
WORK_LIVES_ON_BRANCH_NOT_MAIN = TRUE
```
