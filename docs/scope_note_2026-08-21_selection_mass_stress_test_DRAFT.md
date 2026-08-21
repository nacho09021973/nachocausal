# Nota de alcance acotada — `Pr_n(S)` como objetivo primario y `n·Var(ell|S)` como diagnóstico

```text
ESTADO: PIEZA A FIRMADA Y EJECUTADA / PIEZA B BLOQUEADA HASTA FIRMA 2
FECHA_BORRADOR: 2026-08-21
REVISION: v3 — dos correcciones finales del PI (§0.1) y regla de salida (§6.4)
NATURALEZA: EXPLORATORIA — NINGÚN TERMINAL PUEDE SER `PROVED` NI `REFUTED`
NO_SUSTITUYE: docs/program_closure_note_2026-07-30.md
NO_SUSTITUYE: docs/program_reopening_note_2026-07-31.md
NO_MODIFICA: PR #7, sello, ni los tokens publicados de NC-0..NC-2F
SELLO: intacto — los seis estratos sellados se leen, no se regeneran
SEMILLAS_RESERVED_002: banda virgen [2.000.000–2.999.999] permanece sin quemar
LEAN_STATUS: FROZEN_VALID_NOT_RETRACTED
LEAN_NEW_FORMALIZATION: NOT_AUTHORIZED
```

## 0. Qué corrige esta revisión

La v1 recibió `REVISE_AND_RECONVENE` con cinco bloqueos materiales. Correcciones:

| # | Bloqueo | Corrección |
|---|---|---|
| 1 | §3.2 prohibía usar cifras `[UNVERIFIED]` y §4 las usaba para fijar umbrales | **Dos firmas con bloqueo duro** (§7). La Firma 1 autoriza sólo la Pieza A; los umbrales de la Pieza B se **re-derivan por regla** de la salida verificada, en la Firma 2 |
| 2 | Los predicados no correspondían a las hipótesis | §5 reescrito: los umbrales pasan a ser **candidatos operativos** y se separan de la lectura sobre el orden asintótico. Ninguna condición se enuncia ya en prosa: todas se leen sobre extremos de intervalo |
| 3 | `ANALYTIC_ATTACK_RECOMMENDED` sin regla derivadora; faltaba terminal de ejecución | §6.2 añade la tabla de derivación y §6.1 el terminal `STRESS_B_*` |
| 4 | Semillas incompletamente especificadas | §4.4 fija generador, funciones de expansión, lotes, réplicas por lote y bootstrap, y exige `assert` sobre **conjuntos completos** de semillas, no sobre bases |
| 5 | Cuatro Wilson marginales no son un intervalo conjunto | §4.5 fija corrección de Bonferroni por familia, orden de ejecución, trato del tamaño incompleto y medición del presupuesto |

Un error real que salió al especificar (4): la v1 fijaba **bases** (`2_608_046_000` y
`2_608_047_000`) pero **ninguna función de expansión**. Aplicándoles la convención histórica de la
línea, `base + 100*n + batch`, la escalera de coordenadas invade la base de bootstrap en cuanto
`n>=192` (`2_608_046_000 + 100·192 = 2_608_065_200 > 2_608_047_000`). Comprobar bases no basta:
hay que comprobar conjuntos emitidos. El bloqueo 4 estaba bien puesto.

### 0.1 Qué corrige la v3

Tras ejecutar la Pieza A, el PI ordenó dos correcciones y una autorización:

1. **`RISING` añadido al predicado de tendencia** (§5.2). Sin él, una masa que sube con fuerza caía
   en `INDETERMINATE` por dejar de solaparse los intervalos — castigaba justo el escenario
   favorable. `YES` admite ahora `STABILISING | RISING` (§6.2).
2. **Bootstrap de `1000` a `10000` remuestreos** (§4.3). A `99.375 %`, `1000` dejan `3.1`
   observaciones por cola; `10000` dejan `31.2`.
3. **Umbrales congelados y su emisión autorizada** (§5.1). La regla produce `FLOOR = 0.38`,
   `BAND_LOW = 0.15`, `BAND_HIGH = 0.41`, y el script los verifica con aborto.

Además se añade la **regla de salida** (§6.4): esta nota autoriza **una etapa más y una parada
obligatoria**, no una continuación abierta.

## 1. Por qué existe esta nota y qué invierte

El marcador `docs/status_note_2026-08-21_normalized_theorem_ledger.md` dejó el frente vivo en tres
deudas. Esta nota **invierte el orden de ataque**: `Pr_n(S)>=c>0` pasa de deuda lateral a
**objetivo primario**, y `Var(ell|n,h,S)=O(1/n)` baja a **diagnóstico secundario**.

La inversión se apoya en una implicación ya demostrada:

\[
\inf_{n\ge n_0}\Pr_n(S)>0
\;\Longrightarrow\;
\text{NC2E.1}
\;\Longrightarrow\;
\operatorname{Var}(\ell\mid n,h,S)=O(1/n)
\;\Longrightarrow\;
\liminf_n T_n^h>0 .
\tag{1.1}
\]

Primer eslabón: **Corolario 8.1 de `NC-2F(b)`**, etiquetado **condicional** —
`Pr_n(S)>=c>0` implica `NC2E.1` con `C_q=3.4\cdot10^9/c`
(`emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md:514-517`). Segundo y tercero: NC-2E
y la Proposición NC1-P (`emergencia/P1a_count_volume_preflight_asintotico_d2.md:117-138`).

La hipótesis 4 ya tiene una puerta condicional abierta y su llave es la deuda catalogada como
lateral. Todo el esfuerzo desde `NC-2D` fue por la otra puerta.

### 1.1 Dos cautelas que la nota no puede borrar

1. **El dominio del Corolario 8.1 es `n>=10^40`.** Ninguna ejecución finita corroborará jamás el
   eslabón final de (1.1).
2. **`Pr_n(S)>=c>0` no es fácil por ser plausible.** La cota inferior demostrada hoy es
   `Pr_n(S)>=½n^{-(40\sqrt{n\log n}+5)}` (`NC-2F-a`). Que la exploración salga favorable **no dice
   que demostrar masa uniforme para la unicidad del selector sea alcanzable**; dice que el intento
   no está desaconsejado por los datos. Ésa es toda la decisión que esta nota compra.

## 2. Dos piezas separadas y una barrera entre ellas

| | Pieza A | Pieza B |
|---|---|---|
| Etiqueta | `DESCRIPTIVE_ALREADY_SEEN` | `PROSPECTIVE_PREREGISTERED` |
| Datos | los seis estratos sellados, ya vistos | tamaños nuevos, nunca vistos |
| Semillas | ninguna | §4.4 |
| Estatuto | re-lectura descriptiva | test preinscrito |
| Fija umbrales | **sí** (es desarrollo) | **no** — los recibe congelados en la Firma 2 |
| Valida | **no, nunca** | sí, dentro de §5 |
| Autorizada por | **Firma 1** | **Firma 2**, aún no otorgada |

Los seis estratos vistos son **desarrollo** y nunca validación.

## 3. Pieza A — `DESCRIPTIVE_ALREADY_SEEN`

### 3.1 Qué se autoriza (lista cerrada)

Extender `emergencia/p1a_count_volume_cota_correlacion_d2.py` (134 líneas) para que **emita** y
**verifique**, leyendo los artefactos sellados sin regenerarlos:

1. `selected_count(n) / base_replicates_per_n` para los tres tamaños, desde
   `emergencia/resultados/p1a_representaciones_resumen.json`
   (`metrics[].selected_count`, `contract.base_replicates_per_n`);
2. `n * Var_hat(ell)` por estrato — la columna `Var(Y)` existente multiplicada por `n`;
3. `assert` de sha256 de los dos artefactos:
   ```text
   p1a_representaciones_intervalos_d2.csv
     5110688b89142bf06e738a6f66bb41fa7c248e29352392b8bc763480ebd3ab08
   p1a_representaciones_resumen.json
     7176a3a6e55cf309911a636592780880c55574773d398a9a620a1536ea7899dc
   ```
4. `assert` de que las columnas preexistentes de
   `emergencia/P1a_count_volume_cota_correlacion_d2.md:101-106` se reproducen **verbatim** a los
   mismos cuatro decimales.

La tabla del documento se actualiza copiando la salida del script, nunca al revés.

### 3.2 Estatuto de las cifras

Toda cifra derivada que circule antes de esa ejecución —cualquier valor de `n·Var(Y)`, cualquier
cociente `selected_count/12000`— es **`[UNVERIFIED]`**, por la regla de
`memoria_claude/numbers-must-come-from-committed-script.md` y el `AUDIT_FAIL` del 2026-07-25.

**Consecuencia operativa, y ésta es la barrera del bloqueo 1:** ninguna de esas cifras puede fijar
un umbral de la Pieza B. Los umbrales de §5 se derivan de la **salida commiteada** de la Pieza A,
en la Firma 2, y por la regla escrita en §5.1 — no por elección libre.

### 3.3 Qué no es la Pieza A

No es preinscripción y no puede etiquetarse como tal: sus estadísticos ya se vieron y discutieron
antes de escribir esta nota. Su función legítima es **anclar** los umbrales de §5, y su único
terminal admisible es descriptivo.

### 3.4 Ejecución (2026-08-21)

Ejecutada bajo la Firma 1. Salida verbatim en
`emergencia/P1a_count_volume_cota_correlacion_d2.md` §8. Los dos `assert` pasan: sha256 de los dos
artefactos sellados y reproducción verbatim de las seis filas preexistentes.

```text
PIECE_A_TERMINAL = STRESS_A_DESCRIPTIVE_EMITTED
PIECE_A_SEALED_HASHES_VERIFIED = YES
PIECE_A_VERBATIM_ROWS_REPRODUCED = 6
PIECE_A_SELECTION_MASS_RANGE = [0.5845, 0.6945]
PIECE_A_N_VAR_RANGE = [0.2477, 0.2657]
```

**Una cifra ad hoc no sobrevivió al script.** El valor de `n·Var_hat` para `(128, PAST)` que venía
circulando era `0.2580`, calculado multiplicando la columna publicada **ya redondeada**
(`128 × 0.002016`). El script, que multiplica la varianza sin redondear, emite **`0.2581`**. Las
otras cinco coinciden. Es un dígito y no cambia ninguna conclusión, pero es exactamente el modo de
fallo que la regla de procedencia existe para atrapar, y queda registrado en vez de corregido en
silencio.

## 4. Pieza B — especificación de ejecución

Congelada por la **Firma 2**. Orden obligatorio: (i) ejecutar y commitear la Pieza A; (ii) derivar
umbrales por §5.1 y firmar; (iii) commitear el script; (iv) ejecutar; (v) commitear resultados.
Los pasos (iii) y (iv) no pueden fusionarse ni invertirse.

### 4.1 Escalera y réplicas

```text
STRESS_N                 = (192, 256, 384, 512)
STRESS_BATCHES           = 8
STRESS_REPLICATES_PER_N  = {192: 12000, 256: 12000, 384: 4000, 512: 4000}
STRESS_REPLICATES_PER_BATCH = {192: 1500, 256: 1500, 384: 500, 512: 500}
```

Con `4000` réplicas el error estándar binomial en `p≈0.6` es `≈0.0077`.

### 4.2 Generador

Script **nuevo**: `emergencia/p1a_selection_mass_stress_d2.py`.

**Reutiliza por importación, sin copiar** (el selector no se reimplementa):

```text
from emergencia import p1a_comparar_selectores_d2 as comparison
    comparison.evaluate_selectors, comparison.MIN_COVERAGE_LEX, comparison.STATE_UNIQUE
from emergencia import p1a_estabilidad_d2 as previous
    previous.product_permutation
from emergencia import p1a_gate_altura_duracion_lex_d2 as height_gate
    height_gate.SIDES
```

Son los mismos tres módulos que importa `p1a_representaciones_alternativas_d2.py:27-29`, y la
lógica de unicidad es la de su `_selected_lex` (`:177-184`), invocada, no duplicada.

`emergencia/p1a_representaciones_alternativas_d2.py` **no se modifica**: su guarda
`coordinate_seed` levanta `ValueError` fuera de `BASE_N=(64,96,128)` (`:128-131`) y esa guarda es
contrato congelado.

### 4.3 Bootstrap

```text
STRESS_BOOTSTRAP_REPLICATES = 10000
MÉTODO = percentil, remuestreo con reemplazo de las filas del estrato (n, side)
```

**El tamaño sube de `1000` a `10000` respecto del contrato existente**
(`emergencia/P1a_contrato_representaciones_alternativas_d2.md:112`), y la razón es aritmética: los
intervalos de §4.5 son al `99.375 %`, luego cada cola vale `0.3125 %`. Con `1000` remuestreos eso
deja `3.1` observaciones por cola — insuficiente para sostener esa precisión. Con `10000` quedan
`31.2`.

`31` por cola sigue siendo modesto: la regla de pulgar habitual para percentiles estables pide
`~100`, que exigiría `32000` remuestreos. El bootstrap es sobre filas ya generadas y su coste es
despreciable frente a la generación de réplicas, así que subir a `32000` es viable si la Firma 2
lo prefiere. Se deja en `10000` por instrucción explícita del PI y se declara la resolución
resultante en vez de disimularla.

### 4.4 Semillas — especificación completa

```text
STRESS_COORDINATE_SEED_BASE = 2_610_000_000
STRESS_BOOTSTRAP_SEED_BASE  = 2_620_000_000

STRESS_COORDINATE_SEED(n, batch) = STRESS_COORDINATE_SEED_BASE + 1000*n + batch
    dominio: n in STRESS_N, 0 <= batch < STRESS_BATCHES        -> 32 semillas
STRESS_BOOTSTRAP_SEED(n, side)   = STRESS_BOOTSTRAP_SEED_BASE  + 1000*n + side_code
    side_code(PAST)=0, side_code(FUTURE)=1                     -> 8 semillas
```

La zancada `1000*n` es obligatoria: con `100*n` la escalera invade la base contigua en cuanto
`n>=192`, que es el error de la v1 documentado en §0.

**`assert` exigido — sobre conjuntos, no sobre bases.** El script debe:

1. construir el conjunto `E` de las 40 semillas que emite y comprobar `len(E) == 40` (sin
   duplicados internos);
2. reconstruir el conjunto histórico `H` **llamando a las funciones de semilla históricas sobre
   sus dominios congelados**, no copiando números: las de
   `p1a_representaciones_alternativas_d2.py` y las de los demás módulos de la línea P1a con bases
   `2_608_030_000`, `2_608_035_000`–`2_608_043_000`, `2_608_044_000`, `2_608_045_000`;
3. comprobar `E ∩ H == {}` y emitir `|E|`, `|H|`, `max(H)` y `min(E)` en stdout;
4. comprobar que `E` no interseca `RESERVED_002 = [2_000_000, 2_999_999]`.

Si cualquiera de los cuatro falla, el script aborta sin generar nada.

### 4.5 Intervalos, orden, tamaño incompleto y presupuesto

**Intervalos.** Los predicados de §5 leen extremos de intervalo, luego el nivel debe ser
**simultáneo por familia**, con Bonferroni:

```text
FAMILIA PRIMARIA   (Pr_n(S)):   4 intervalos Wilson  -> cada uno al 1 - 0.05/4 = 98.75 %
FAMILIA SECUNDARIA (n·Var_hat): 8 intervalos bootstrap -> cada uno al 1 - 0.05/8 = 99.375 %
```

Cada familia queda así al 95 % simultáneo. **Las dos familias no se corrigen entre sí**: se declara
explícitamente que el nivel conjunto sobre ambas no es 95 %. Wilson y no Wald: a `p≈0.6` y
`N>=4000` casi coinciden, así que la elección **no es material**; se fija por escrito sólo para
que la lectura de los extremos no quede a elección posterior.

**Orden de ejecución.** Tamaños en orden ascendente `192 -> 256 -> 384 -> 512`, estrictamente
secuencial, proceso único, sin paralelismo.

**Tamaño incompleto.** Un tamaño es **completo** (todas sus réplicas) o se **descarta entero**. Un
tamaño parcial no se reporta y no entra en ningún predicado. Si falta cualquiera de los cuatro,
`STRESS_B_TERMINAL = STRESS_B_BUDGET_EXHAUSTED` y §6.2 fuerza `ANALYTIC_ATTACK_RECOMMENDED =
UNDECIDED`.

**Presupuesto.** `6 h` de reloj, medidas con `time.monotonic()` desde el arranque del proceso y
**consultadas sólo en las fronteras entre tamaños**, nunca dentro de un tamaño — precisamente para
que no puedan producirse tamaños parciales. Si al terminar un tamaño el transcurrido es `>= 6 h`,
la ejecución para. El tamaño en vuelo cuando se cruza el umbral **se completa** y su sobrecoste se
reporta. El script emite el transcurrido por tamaño. **Ampliar el presupuesto tras ver datos
parciales queda prohibido** y exige firma nueva.

## 5. Predicados de decisión

Ninguno de estos predicados decide `\inf_{n\ge n_0}\Pr_n(S)>0` ni `Var(ell|n,h,S)=O(1/n)`. Un
barrido finito es compatible con cualquier constante y cualquier `n_0` posterior.

### 5.1 Regla de derivación de los umbrales — aplicada, valores congelados

Sea `p_dev` el **mínimo verificado** de `selected_count/base_replicates_per_n` sobre los tres
tamaños de desarrollo, y `v_dev` el **centro del rango verificado** de `n·Var_hat` sobre los seis
estratos, ambos tal como los emita la Pieza A:

```text
FLOOR      = floor_2dec( (2/3) * p_dev )
BAND_LOW   = round_2dec( 0.6 * v_dev )
BAND_HIGH  = round_2dec( 1.6 * v_dev )
```

Tras la ejecución de §3.4 los insumos están verificados y emitidos por el script
(`PIECE_A_SELECTION_MASS_RANGE = [0.5845, 0.6945]`, `PIECE_A_N_VAR_RANGE = [0.2477, 0.2657]`). La
regla aplicada a ellos **no** reproduce los valores que se eyeballearon en la v1. Los umbrales
quedan congelados en:

```text
FLOOR     = 0.38        (v1 eyeballeaba 0.40)
BAND_LOW  = 0.15
BAND_HIGH = 0.41        (v1 eyeballeaba 0.40)
```

Que la regla y el ojo discrepen en dos de los tres es exactamente la razón de tener una regla, y
la razón de que los umbrales no puedan fijarse a mano.

**Los tres valores son una afirmación comprobable, no una transcripción.** La Firma 2 autoriza a
`emergencia/p1a_count_volume_cota_correlacion_d2.py` a **emitirlos y verificarlos**: el script los
recalcula por esta regla desde la precisión completa y **aborta** si no coinciden con los tres
números de arriba. Si alguna vez dejaran de coincidir, la ejecución falla en vez de degradarse en
silencio.

Son **umbrales operativos**, no cantidades con significado asintótico.

### 5.2 Objetivo primario — `Pr_n(S)`

Dos lecturas independientes. `W_lo(n)`, `W_hi(n)` son los extremos Wilson al 98.75 % de §4.5.

```text
SELECTION_MASS_CANDIDATE_FLOOR =
    MET      <=>  W_lo(n) >= FLOOR  para los cuatro n de STRESS_N
    NOT_MET  <=>  en caso contrario

SELECTION_MASS_TREND =   (cascada ordenada, exhaustiva y excluyente)
    DECAYING       <=>  W_hi(512) < W_lo(192)
    RISING         <=>  NO(DECAYING)  Y  W_lo(512) > W_hi(192)
    STABILISING    <=>  NO(DECAYING)  Y  NO(RISING)
                        Y  [W_lo(384),W_hi(384)] ∩ [W_lo(512),W_hi(512)] != {}
    INDETERMINATE  <=>  en caso contrario
```

`RISING` se añade porque sin él una masa que **sube con fuerza** cae en `INDETERMINATE`: los
intervalos de `384` y `512` dejan de solaparse precisamente por subir, y el solapamiento era la
única vía a `STABILISING`. Una masa creciente favorece `Pr_n(S)>=c>0` tanto como una estable, y el
predicado tiene que decirlo. La cascada está ordenada para que el veredicto sea determinista
cuando dos condiciones podrían valer a la vez.

**Lectura obligatoria, precomprometida.** `NOT_MET` **no** desfavorece `Pr_n(S)>=c>0`. Una masa
estable en `0.30` incumple `FLOOR = 0.38` y **sigue favoreciendo** masa positiva: `FLOOR` mide una
escala candidata, no la hipótesis. `STABILISING` y `RISING` son ambas favorables. Sólo `DECAYING`
es una señal contraria, y tampoco refuta nada.

### 5.3 Diagnóstico secundario — `n·Var(ell|n,h,S)`

La hipótesis 4 es una **cota superior**: `n·Var <= C`. Por tanto la lectura es **de un solo lado**.
`B_lo(n,h)`, `B_hi(n,h)` son los extremos bootstrap al 99.375 % de §4.5.

```text
VARIANCE_CANDIDATE_BAND =
    IN   <=>  n·Var_hat(n,h) in [BAND_LOW, BAND_HIGH] para los cuatro n y ambos lados
    OUT  <=>  en caso contrario

VARIANCE_ORDER_SIGNAL =
    GROWTH_SIGNAL       <=>  existe h con n·Var_hat(·,h) estrictamente creciente en los
                             cuatro tamaños  Y  B_lo(512,h) > B_hi(192,h)
    BOUNDED_CONSISTENT  <=>  para ambos lados,  B_hi(512,h) <= B_hi(192,h)
    INDETERMINATE       <=>  en caso contrario
```

**Lecturas obligatorias, precomprometidas.**

- Que `n·Var_hat` **baje** de `BAND_LOW` **favorece** `O(1/n)`: es una varianza menor de lo
  esperado. Cuenta como `BOUNDED_CONSISTENT` si cumple su condición, y **nunca** como señal
  contraria. `OUT` por abajo no es un resultado negativo.
- Estabilizarse en `0.50` **sigue siendo** `O(1/n)`: `OUT` por arriba con
  `BOUNDED_CONSISTENT` significa que la escala candidata era mala, no que el orden falle.
- Sólo `GROWTH_SIGNAL` es una señal contraria al orden, y tampoco lo refuta.

## 6. Terminales precomprometidos

### 6.1 Terminales de ejecución

```text
STRESS_A_TERMINAL = STRESS_A_DESCRIPTIVE_EMITTED | STRESS_A_BLOCKED

STRESS_B_TERMINAL = STRESS_B_COMPLETED
                  | STRESS_B_BUDGET_EXHAUSTED
                  | STRESS_B_BLOCKED
```

`STRESS_B_COMPLETED` exige los cuatro tamaños completos. `STRESS_B_BLOCKED` cubre el aborto por
`assert` de semillas (§4.4) o por cualquier fallo de integridad.

### 6.2 Regla de derivación de la recomendación

```text
si STRESS_B_TERMINAL != STRESS_B_COMPLETED:
    ANALYTIC_ATTACK_RECOMMENDED = UNDECIDED           (forzado, sin excepción)

en otro caso:
    NO         <=  SELECTION_MASS_TREND = DECAYING
                   O VARIANCE_ORDER_SIGNAL = GROWTH_SIGNAL
    YES        <=  SELECTION_MASS_TREND in {STABILISING, RISING}
                   Y SELECTION_MASS_CANDIDATE_FLOOR = MET
                   Y VARIANCE_ORDER_SIGNAL != GROWTH_SIGNAL
    UNDECIDED  <=  en cualquier otro caso
```

La primera cláusula tiene prioridad sobre la segunda. `ANALYTIC_ATTACK_RECOMMENDED` es una
**recomendación**; `ANALYTIC_ATTACK_AUTHORISED = NO` es invariante de esta nota y abrir el ataque
exige nota y firma nuevas.

### 6.3 Bloque completo a emitir

```text
STRESS_A_TERMINAL              = ...
STRESS_B_TERMINAL              = ...
SELECTION_MASS_CANDIDATE_FLOOR = MET | NOT_MET
SELECTION_MASS_TREND           = STABILISING | RISING | DECAYING | INDETERMINATE
VARIANCE_CANDIDATE_BAND        = IN | OUT
VARIANCE_ORDER_SIGNAL          = BOUNDED_CONSISTENT | GROWTH_SIGNAL | INDETERMINATE
ANALYTIC_ATTACK_RECOMMENDED    = YES | NO | UNDECIDED
ANALYTIC_ATTACK_AUTHORISED     = NO
LEAN_STATUS                    = FROZEN_VALID_NOT_RETRACTED
LEAN_NEW_FORMALIZATION         = NOT_AUTHORIZED
NOVELTY_CERTIFIED              = NO
```

### 6.4 Regla de salida — parada obligatoria

Esta nota autoriza **exactamente una etapa más**. No existe continuación automática por ninguna
rama. Precomprometido antes de ejecutar:

```text
ANALYTIC_ATTACK_RECOMMENDED = NO
    -> APARCAR la línea. No se amplía la escalera, no se repite el barrido,
       no se busca otra ruta a la hipótesis 4.

ANALYTIC_ATTACK_RECOMMENDED = UNDECIDED        (incluye BUDGET_EXHAUSTED)
    -> APARCAR igualmente. Un inconcluso NO autoriza ampliar tamaños,
       réplicas ni presupuesto: eso sería convertir el agotamiento en
       una prórroga, que §4.5 prohíbe.

ANALYTIC_ATTACK_RECOMMENDED = YES
    -> abrir ÚNICAMENTE un preflight analítico corto sobre masa uniforme,
       sin Lean, bajo nota y firma nuevas. Si ese preflight no produce un
       lema concreto y plausible para la unicidad del selector, APARCAR
       también.
```

Las tres ramas terminan en aparcar salvo una, y esa una termina en aparcar si no entrega un lema.
**Ninguna rama autoriza formalización.** `LEAN_NEW_FORMALIZATION = NOT_AUTHORIZED` sobrevive a
cualquier veredicto de esta nota.

Justificación registrada: la línea ha aislado una condición precisa y una puerta condicional real
—no está en «ningún sitio»—, pero lo que sigue sin saberse es si esa puerta puede demostrarse
abierta asintóticamente. Un ensayo acotado más está justificado; una continuación abierta no.

## 7. Qué sigue prohibido

- **Lean**: ni una línea nueva. Lo formalizado no se retracta, no se amplía y no se toca.
- Ejecutar cualquier parte de §4 o §5 **antes de la Firma 2**. Sin Firma 2 no se extrae ni una
  semilla.
- Modificar el sello, los seis estratos, `p1a_representaciones_alternativas_d2.py` o cualquier
  token publicado de `NC-0`..`NC-2F`.
- Tocar `RESERVED_002`.
- Emitir `PROVED`, `REFUTED` o `NC2E_O3 = CLOSED`, o mover cualquier token de la cadena NC.
- Elegir umbrales fuera de la regla de §5.1, o recalcularlos después de ver datos nuevos. Los tres
  valores de §5.1 están congelados y el script aborta si no los reproduce.
- Continuar la línea por cualquier rama que §6.4 mande aparcar.
- Ampliar presupuesto, escalera o réplicas tras ver datos parciales.
- Abrir el ataque analítico a la masa uniforme.
- Reabrir `DENOMINATOR_POSITIVITY` (cerrado en `docs/status_note_2026-08-21_normalized_theorem_ledger.md` §3.3).
- Lenguaje de novedad absoluta. `NOVELTY_CERTIFIED = NO`.

## 8. Riesgos declarados

1. **Régimen preasintótico.** `Pr_n(S)` crece en `n in {64,96,128}` mientras la cota demostrada
   decae como `n^{-2n^{4/5}}`. O la cota es enormemente floja, o el crecimiento observado es un
   artefacto de tamaños pequeños con un máximo posterior. Cuatro tamaños más mueven el horizonte
   de `128` a `512` y nada más.
2. **Compatibilidad no es viabilidad.** Un `YES` no dice que la masa uniforme sea demostrable. La
   dificultad de demostrar unicidad del selector con masa acotada por debajo es **desconocida** y
   esta nota no la estima.
3. **Dependencia entre piezas.** Los umbrales de §5.1 se derivan de datos de desarrollo. La Pieza B
   no es independiente de la Pieza A; lo que aporta es que quedan fijados por regla y **antes** de
   ver los tamaños nuevos.
4. **Coste de `n=512`.** No hay medición previa. Por eso el presupuesto de §4.5 es duro y el
   terminal por agotamiento es `BUDGET_EXHAUSTED`, no una prórroga.
5. **Nivel simultáneo entre familias.** Corregido dentro de cada familia, no entre ellas (§4.5).
   Declarado, no disimulado.

## 9. Firmas

### 9.1 Revisión de la v1

```text
REVIEW_VERDICT: REVISE_AND_RECONVENE
REVIEW_DATE: 2026-08-21
REVIEW_SCOPE: cinco bloqueos materiales, resueltos en §0
```

### 9.2 Firma 1 — autoriza **exclusivamente** la Pieza A

```text
FIRMADO_POR: Ignacio Martín (PI)
FECHA_FIRMA: 2026-08-21
DECISION: PIEZA_A_AUTORIZADA
AUTHORISED_SCOPE: lista cerrada de §3.1 — extensión del script existente, emisión y
  verificación de las dos magnitudes derivadas, asserts de sha256 y de reproducción verbatim
NOT_AUTHORISED: todo §4, todo §5, todo lo listado en §7; ninguna semilla
LITERAL_SIGNOFF: "firmo por P.I Ignacio Martín a 21 de agosto de 2.026"
```

### 9.3 Bloqueo duro

La Pieza B **no puede ejecutarse ni firmarse** hasta que la Pieza A esté ejecutada y commiteada y
sus cifras dejen de ser `[UNVERIFIED]`. Los umbrales de §5.1 se derivan de esa salida, por la regla
escrita, y no por elección.

### 9.4 Firma 2 — autorizaría la Pieza B

```text
FIRMADO_POR: PENDIENTE
FECHA_FIRMA: PENDIENTE
DECISION: PENDIENTE
FLOOR_CONGELADO: 0.38          (regla de §5.1 sobre la salida commiteada de la Pieza A)
BAND_CONGELADA: [0.15, 0.41]   (idem)
AUTORIZA_ADEMAS: emisión y verificación por script de FLOOR/BAND_LOW/BAND_HIGH,
  con aborto si no reproducen los tres valores congelados
AUTHORISED_SCOPE: PENDIENTE — §4, §5 y la regla de salida de §6.4
```
