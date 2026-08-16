# Hoja de ruta — agosto de 2026

```text
ESTADO: RETIRADA DEL PERÍMETRO ACTIVO
FECHA: 2026-08-15
DECISIÓN: traslado íntegro a backlog por autorización explícita del PI
```

La línea EF-0–EF-8 ya no forma parte del trabajo en curso. Su contenido histórico se
conserva en [`docs/backlog_hallazgos.md`](backlog_hallazgos.md), entrada de 2026-08-15,
con el alcance y las reservas fijados por
[`docs/foro/foro_decision_001_ef4-falsacion-adversarial.md`](foro/foro_decision_001_ef4-falsacion-adversarial.md).

Esta remisión no autoriza ni valida ninguna afirmación matemática de la línea retirada.

## Actualización 2026-08-16 — cierre del barrido EF-4 y apertura de `NC-0`

La nota `docs/scope_note_2026-08-16_ef4_partial_staircase_search_DRAFT.md` fue
firmada y ejecutada pese a conservar `_DRAFT` en el nombre histórico. Su terminal
`OPEN_AT_COMPUTE_CAP` permanece intacto, pero la corrección de dominio de su §12 y
la adjudicación de `docs/backlog_hallazgos.md` §12 establecen que el barrido recorrió
`F_test(n,rho)` con `rho in {3,4}`, no la sucesión formal
`rho_n=ceil((n^2 log n)^(1/3))`.

Esta actualización prevalece operativamente sobre los handoffs históricos que
aparecen más abajo y todavía describen la nota como no firmada o el falsificador
como siguiente gate. Se conservan únicamente como cronología de decisiones.

En consecuencia, no hay un siguiente gate computacional de escaleras. C1 formal
sigue `INCONCLUSIVE`; aumentar el cap, instrumentar histogramas o buscar un puente
desde `rho` fijo no está autorizado ni científicamente motivado por ese run.

La continuación relacionada `NC-0` queda autorizada por la firma del PI en
`docs/program_reopening_note_2026-08-16_normalised_channel.md`. Su alcance es
exclusivamente la auditoría documental y matemática del canal normalizado
`T_n=1-rho_max^2` descrita en la lista cerrada de esa nota. Ninguna obligación de
`NC-0` ha sido ejecutada todavía.

```text
EF4_PARTIAL_STAIRCASE_RUN = CLOSED_NONPROBATIVE_FOR_FORMAL_SEQUENCE
EF4_C1 = OUT_OF_SCOPE / INCONCLUSIVE
EF4_NEXT_COMPUTE_GATE = NONE
NORMALISED_CHANNEL_NC0 = AUTHORISED / NOT_YET_EXECUTED
NORMALISED_CHANNEL_EXECUTION_AUTHORISED = YES_WITHIN_SIGNED_SCOPE
NEXT_GATE = NC0_ROUND4_AUDIT
```

## Handoff para 2026-08-17 — R1 primero; EF-4 sólo con nota nueva

```text
ESTADO: HANDOFF DOCUMENTAL / NO REABRE EF-0--EF-8
PRIORIDAD ACTIVA: R1 — manuscrito de límites
FECHA LÍMITE R1: 2026-09-11
EF4/C1: OUT_OF_SCOPE / INCONCLUSIVE
AUTORIZACIÓN DE EJECUCIÓN EF-4: NO
```

La pregunta pendiente de EF-4 es precisa, pero no desplaza el entregable con fecha. La primera
acción de la próxima sesión será revisar el estado y las obligaciones restantes de R1. Cualquier
trabajo nuevo sobre escaleras exige una nota firmada separada; este handoff sólo deja preparado el
contrato que esa nota podría autorizar.

### Actualización 2026-08-16 — R1 cerrado; siguiente gate EF-4 sólo documental

El handoff anterior queda resuelto antes de la fecha prevista. R1 superó su completion test en la
rama autorizada `reopen/r1-r2-limits-writeup`.

```text
R1_STATUS: CLOSED / COMPLETION_TEST_PASSED_2026-08-16
R1_REMOTE_HEAD: 591cf536653d9502cb591f4e31d24200dbca1963
R1_COMPILED_SOURCE: 265a9538d16171b0403fdd63a7e6f3a530d3878e
R2_PREFACTOR: OPEN / [UNVERIFIED]
EF4/C1: OUT_OF_SCOPE / INCONCLUSIVE
AUTORIZACIÓN_DE_EJECUCIÓN_EF4: NO
NEXT_GATE: nota de alcance EF-4; firma del PI antes de cualquier código o ejecución
```

El siguiente acto previsto por esta hoja se ha materializado únicamente como **borrador no
firmado** en
[`docs/scope_note_2026-08-16_ef4_partial_staircase_search_DRAFT.md`](scope_note_2026-08-16_ef4_partial_staircase_search_DRAFT.md).
Su existencia no reabre EF-0--EF-8 y no autoriza ejecutar la búsqueda. Hasta que el bloque de firma
del borrador sea sustituido por autorización explícita del PI, el terminal operativo sigue siendo
`NO_EXECUTION_AUTHORISED`.

### Estado endurecido de la evidencia finita

Las escaleras tienen `rho-1` puntos. Por tanto, con `rho=2` la contención parcial es
**estructuralmente imposible para todo `n`**. Un `COMPATIBLE_FAILURES=0` en ese régimen no pone a
prueba la rama de contención parcial del análisis de casos.

| `(n,rho)` | No vacuidad y capacidad estructural | Resultado | Estado de evidencia |
|---|---|---|---|
| `(12,2)` | vacuo; escalera de un punto | el disyunto `small_product` vale siempre | registrado por foro-001 |
| `(24,2)` | no vacuo; contención parcial imposible | `40/40` casos compatibles que muerden pasan `loss_case` | script commiteado |
| `(30,2)` | no vacuo; contención parcial imposible | `1157/1157`; `COMPATIBLE_FAILURES=0` | `[UNVERIFIED]`: sin script commiteado |
| `(34,3)` | no vacuo; contención parcial posible | `36/36`, pero `PARTIAL_STAIRCASE_CASES=0` | `[UNVERIFIED]`: sin script commiteado |
| `(36,2)` | no vacuo; contención parcial imposible | `19239/19239`; `COMPATIBLE_FAILURES=0` | `[UNVERIFIED]`: omitido del resumen previo y sin script commiteado |

Para `(36,2)` se reportaron además `3.469.799.025` tuplas abstractas y `47.813` fallos abstractos.
No añaden evidencia sobre la rama estructural: todos los casos compatibles que requerían
`loss_case` pasaron, y `rho=2` impide por definición una contención parcial.

Conclusión vigente: entre `n=12`, `24`, `30`, `34` y `36`, la lógica de escaleras parciales **no
ha sido ejercitada ni una vez**. C1 permanece `INCONCLUSIVE`.

### Aritmética que acota la búsqueda

Con

\[
N=\texttt{free\_count}=n-2\rho-2,
\qquad
\tau=\frac18+\frac{\rho}{N},
\]

la no vacuidad `tau<1/4` equivale a

\[
n>10\rho+2.
\]

Como `n` debe ser par y `10rho+2` ya es par, el primer candidato es exactamente

\[
n_{\min}(\rho)=10\rho+4.
\]

Así, la búsqueda propuesta empieza en `(34,3)` y `(44,4)`. El primero ya fue inspeccionado fuera
de script commiteado y no produjo contención parcial; la siguiente exploración de `rho=3` debe
subir por `n=36,38,...`, mientras la rama `rho=4` empieza en `n=44`.

### Contrato propuesto para una futura nota firmada

No barrer `C(n,4)^2` y filtrar después. Enumerar directamente cadenas compatibles con `F_n` y,
dentro de ellas, sólo las que muerden. Para una 4-cadena, si `a_-,a_+` son sus números de filas
libres en los bloques pasado/futuro y `b_-,b_+` los de columnas libres, la comparación exacta es

\[
8\min(a_-b_-,a_+b_+)
\;\mathop{\le}^{\texttt{small\_product}}\;
N(N+8\rho).
\]

Esto evita coma flotante y permite preagrupar candidatos por
`(a_-,a_+,b_-,b_+)`. La compatibilidad debe imponerse **antes** del veredicto:

```text
r_i prescrito  => c_i = P(r_i)
c_i prescrita  => r_i = P^{-1}(c_i)
```

Perímetro propuesto:

1. `rho in {3,4}`;
2. recorrer los pares admisibles en orden determinista: primero `n` creciente y, a igual `n`,
   `rho` creciente, siempre desde `n_min(rho)`;
3. detener la búsqueda de parámetros al terminar el primer `(n,rho)` que contenga al menos una
   cadena compatible que muerda y contenga una fracción estricta no vacía de una escalera;
4. en ese primer par, completar el barrido de **todas** las cadenas compatibles que muerden para
   decidir si alguna falla los tres disyuntos;
5. detener inmediatamente ante el primer fallo compatible, conservando el testigo completo;
6. fijar en la nota un tope de cómputo medido en `COMPATIBLE_BITING_CHAINS`, no en tuplas
   abstractas; si se alcanza, terminar `OPEN_AT_COMPUTE_CAP`;
7. determinista, aritmética entera, cero semillas y cero escritura fuera de los artefactos
   expresamente listados por la nota.

Antes de confiar en el enumerador directo, éste debe reproducir como control el resultado
commiteado de `(24,2)`:

```text
REQUIRES_LOSS_CASE=40
LOSS_CASE_PASS=40
COMPATIBLE_FAILURES=0
PARTIAL_STAIRCASE_CASES=0
```

Terminales propuestos para la ejecución futura:

```text
REFUTED_BY_COMPATIBLE_WITNESS
FIRST_PARTIAL_PAIR_EXHAUSTED_NO_FAILURE
OPEN_AT_COMPUTE_CAP
```

Nada de esta sección autoriza crear el script, ejecutar la búsqueda, modificar tests sellados ni
promover tokens científicos. El siguiente acto posible sobre EF-4 es **redactar y firmar la nota
de alcance**; no ejecutar todavía.
