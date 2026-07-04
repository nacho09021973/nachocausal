# Parte F — Addendum de freeze de μ (revisión post-comité 018)

Status: **DRAFT_NOT_FREEZE — texto únicamente, no comiteado (aún), no ejecutado, NO es un freeze
final hasta que el PI autorice su commit.** El hueco EMPTY_FAMILY (antigua §4) fue adjudicado por
`docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md`
(`COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`); esta revisión implementa su
§9.1 exactamente, cerrando los 6 puntos ahí exigidos. Ninguna semilla de `EXPLORE_POOL` ni
`VALIDATION_SEEDS` ha sido tocada por escribir este documento; no se ha ejecutado ningún script;
no se ha modificado `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md` ni la implementación de R-VAR. Esta
revisión, aunque se comitee, **NO autoriza la ejecución de Parte F** (ver §6).

**Gate 0 Tier 0 (`b142377`) y Tier 1 (`55e19b8`, 100/100, 0 mismatches) están PASS — necesarios
pero NO suficientes para el cómputo de μ.** Gate 0 verifica que el algoritmo (min-cut vs fuerza
bruta) es correcto; este addendum fija los NÚMEROS y el PROCEDIMIENTO del cómputo estadístico de
μ (Parte F, F2), que es una pregunta distinta y requiere su propia autorización de ejecución
separada, exactamente como Tier 0 → Tier 1 requirieron cada uno la suya en vez de heredar la del
paso anterior.

Spec controladora: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md`, Parte F (líneas 484-552 al momento de
escribir este addendum).

---

## 0. Objeto estadístico de μ — resuelto por comité 018

**`μ_n := cuantil empírico (1−α) de { max_{D∈𝒜(C_j)} S(C_j) : j=1..M }`, condicionado a
`𝒜(C_j)≠∅`.** Esto es numéricamente el objeto "A" del hueco original. Adicionalmente, y de forma
obligatoria (no opcional), la **tasa de `EMPTY_FAMILY` se reporta por separado, por nivel de
intensidad**, como diagnóstico de proveniencia — nunca plegada dentro de la distribución de `S`.

- **`EMPTY_FAMILY_CONVENTION := COND_ON_A(C)_NEQ_EMPTY_WITH_SEPARATE_RATE_REPORT`** — este es el
  único token válido; sustituye cualquier mención anterior de "A", "B" o "C" sueltas.
- **Se rechaza mapear `EMPTY_FAMILY` a `S:=0` — y la razón fijada aquí es de TIPO, no de
  seguridad estadística.** `S:{D∈𝒜(C)}→ℚ` es una función parcial, indefinida exactamente donde
  `𝒜(C)=∅`; `max_{D∈∅} S` no existe, no es `0`. Además `S=0` es un valor INTERIOR alcanzable
  (`A(D)=0` para un corte genuinamente balanceado, v2.2 D.2:`:311-312`) — mapear `EMPTY_FAMILY` a
  `0` colisionaría abstención estructural con datos de score reales, exactamente en el centro de
  la distribución. **Nota de precisión (comité 018 §5, hallazgo del falsificador):** mapear a `0`
  NO es estadísticamente inseguro en el sentido ingenuo — bajo esa convención `FP_RATE_NULL≤α` se
  mantiene exacto por construcción. Se rechaza de todos modos porque es un error de tipo/categoría
  (asignar un valor numérico donde la función no está definida), no porque viole el umbral de
  falsos positivos. No se cite la razón FP-insegura en ningún texto futuro.
  Ancla: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md` D.1/D.2/D.3 (`:270-458`); comité 018 §4-§5.
- **Esta elección está forzada, no es una preferencia**: la escalera tipada de D.3
  (`DISCONNECTED_HASSE → EMPTY_FAMILY → LOW_CONTRAST (vs μ) → INCOHERENT_ARGMAX`, orden fijo,
  `:453-458`) ya evalúa `EMPTY_FAMILY` ANTES de la comparación contra μ — un parche con
  `𝒜(C)=∅` nunca llega al gate de μ. Calibrar μ sobre cualquier población distinta de
  `𝒜(C)≠∅` mediría contra una población que el gate nunca compara.
- **La justificación de este addendum para la elección NO se apoya en la tasa observada de
  Gate 0 Tier 1 (190/191 MINK vacíos a `TOY_INTENSITY=9.0`).** Esa cifra es de un nivel de
  juguete no-calibración y se cita abajo (§4) solo como contexto de por qué el hueco se detectó,
  nunca como evidencia a favor de la convención — la convención descansa únicamente en el orden
  tipado ya congelado de D.3, que es válido con independencia de cualquier tasa observada o por
  observar. (Corrección respecto al borrador anterior de este mismo addendum, que sí mencionaba
  la cifra en la sección de justificación — comité 018 §9.1 lo marca como a corregir.)

## 1. M exacto (no piso)

**`M := 200`**, congelado por igualdad, no por piso, y **`M` cuenta exclusivamente parches con
`𝒜(C)≠∅` ("draws admisibles no vacíos")** — esto es una aclaración/enmienda textual explícita a
F2 (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:511-512`, que dice literalmente "M parches NULOS" sin
especificar si cuenta todos los sprinkleados o solo los no vacíos; comité 018 §5 hallazgo (4)
señala que dejarlo implícito sería una enmienda silenciosa de una cláusula defectuosa). Se
enmienda aquí, por escrito, ANTES de cualquier ejecución: **M=200 = 200 parches con
`𝒜(C_j)≠∅`**, no 200 parches sprinkleados en bruto.

- **Base del valor 200:** es el número que el falsificador de comité 017 ya nombró como *piso*
  (`M≥200`, v2.2:527). Congelarlo aquí como valor exacto, sin ajustarlo hacia arriba ni hacia
  abajo, es la elección con menor grado de libertad disponible.
- **Argumento estructural (no depende de datos):** para `α=0.05`, el cuantil empírico `(1−α)` de
  M=200 nulos admisibles cae en el rango de orden `k=⌈0.95·200⌉=190`, dejando 10 estadísticos en o
  por encima del cuantil — suficiente granularidad para que el cuantil no esté determinado por 1-2
  valores extremos. Este argumento usa solo M y α, ninguno de los dos observado.
- **M es por nivel de intensidad**, no global: se necesitan M=200 parches nulos admisibles
  INDEPENDIENTES por cada uno de los 4 niveles de §3 (800 parches nulos admisibles en total para
  el paso 3), porque μ_n es función del nivel n (Parte F, F2). "Independientes" significa aquí:
  ningún root ni ninguna sub-semilla se reutiliza entre niveles — ver §4b (asignación
  root→nivel), que es precisamente lo que cierra el gap 1 del falsificador de comité 018 (una
  tabla μ correlacionada entre niveles por reuso de streams).

## 2. Esquema exacto de spawn y regla de agotamiento (corregida)

**`numpy.random.SeedSequence(root).spawn(K)`**, consumido en orden, con
`MAX_CHILDREN_PER_ROOT = 400` por root como válvula de seguridad — idéntico, verbatim, a la
receta ya ejecutada y aprobada en Gate 0 Tier 1
(`dev/measure_pr003_rvar_gate0_tier1.py:184`, `SeedSequence(root).spawn(MAX_CHILDREN_PER_ROOT)`).

- **Rationale:** no se elige entre `Generator.spawn(k)` y `SeedSequence(seed).spawn(k)` como una
  decisión nueva — se reusa la que ya corrió bajo autorización y pasó Gate 0 Tier 1.
- **Regla de agotamiento (corregida — comité 018 §5, hallazgo del falsificador #2):** el borrador
  anterior de este addendum decía que agotar `MAX_CHILDREN_PER_ROOT=400` hijos de UN root sin
  alcanzar M forzaba un abort duro inmediato — esto CONTRADECÍA el comportamiento real del script
  de Tier 1 ya ejecutado y aprobado (`dev/measure_pr003_rvar_gate0_tier1.py:180-186`), que al
  agotar un root simplemente continúa con el siguiente root de su pool asignado, sin abortar.
  **Regla única, ahora reconciliada con el precedente de Tier 1:** dentro del bloque de roots
  asignado a un nivel (§4b), los roots se consumen EN ORDEN; al agotar los 400 hijos de un root
  sin haber alcanzado M=200 admisibles para ese nivel, se pasa al siguiente root del MISMO bloque
  — nunca se aborta a nivel de root individual, igual que Tier 1. El abort duro solo ocurre a
  nivel de BLOQUE COMPLETO (ver §4c, `OUT_OF_DOMAIN_UNCALIBRATED`): si TODOS los roots asignados a
  un nivel se agotan sin juntar M=200 admisibles, ESE nivel (no el proceso completo) aborta y se
  reporta como hallazgo — nunca se amplía el cap, nunca se toman roots de otro bloque o de otro
  pool (calibración ↔ test), nunca se reduce M silenciosamente.

## 3. Niveles μ_n enumerados

**Exactamente los 4 niveles de `nachocausal/thresholds.py:INTENSITIES`:**

```
(1500.0, 3000.0, 6000.0, 12000.0)
```

- Estos son los mismos 4 niveles sellados del resto del proyecto (per Parte F, v2.2:513),
  **no** el `TOY_INTENSITY=9.0` usado en Gate 0 Tier 1 (que el propio informe de Tier 1 etiquetó
  explícitamente como "no tiene significado estadístico/de calibración").
- **Interpolación entre niveles PROHIBIDA** (v2.2:513) — un parche BH futuro debe evaluarse
  contra la μ del nivel exacto de su intensidad de sprinkling; si no coincide con ninguno de los
  4, R-VAR abstiene (`NO_CALIBRATED_LEVEL` o equivalente), no interpola.

## 4. Sub-pools disjuntos, asignación root→nivel, y regla OUT_OF_DOMAIN (todo congelado ahora)

### 4a. Partición de rol (calibración vs. test) — sin dilema falso

**Corrección respecto al borrador anterior (comité 018 §5, hallazgo del falsificador #3 —
"dilema falso"):** el borrador previo afirmaba que excluir el root `1_000_000` (ya consumido por
Gate 0 Tier 1 para verificación de algoritmo, no para estadística de μ) exigiría una partición
simétrica `[1:21]`/`[21:41]` inviable sin ampliar `EXPLORE_POOL` (40 roots). Esto era falso: una
partición ASIMÉTRICA excluye `1_000_000` sin redimensionar nada.

- **`MU_CALIBRATION_ROOTS := EXPLORE_POOL[1:21]`** = `1_000_001..1_000_020` (20 roots).
- **`MU_FALSIFICATION_TEST_ROOTS := EXPLORE_POOL[21:40]`** = `1_000_021..1_000_039` (19 roots).
- `1_000_000` queda **excluido de ambos pools** de Parte F — no se reutiliza el root que Gate 0
  Tier 1 ya consumió para un propósito distinto, cerrando la superposición que el borrador
  anterior dejaba como pregunta abierta, sin tocar `EXPLORE_POOL` fuera de sus 40 roots
  existentes.
- Disjunción de sub-pools por rol (paso 3 vs. paso 5) satisfecha literalmente
  (v2.1/v2.2:543-546).

### 4b. Asignación root→nivel de intensidad (nueva — cierra el gap 1 del falsificador)

El borrador anterior no fijaba qué roots alimentan qué nivel de intensidad, dejando abierta la
posibilidad de reusar los mismos streams de sub-semilla en los 4 niveles (tabla μ correlacionada
entre niveles, contradiciendo la propia palabra "INDEPENDIENTES" de §1). Se fija aquí, en bloques
contiguos y disjuntos:

**Calibración (`MU_CALIBRATION_ROOTS`, 20 roots → 5 roots por nivel):**

| Nivel `n` | Roots asignados |
| --- | --- |
| 1500.0 | `1_000_001..1_000_005` |
| 3000.0 | `1_000_006..1_000_010` |
| 6000.0 | `1_000_011..1_000_015` |
| 12000.0 | `1_000_016..1_000_020` |

**Test de falsación (`MU_FALSIFICATION_TEST_ROOTS`, 19 roots → 5/5/5/4):**

| Nivel `n` | Roots asignados |
| --- | --- |
| 1500.0 | `1_000_021..1_000_025` |
| 3000.0 | `1_000_026..1_000_030` |
| 6000.0 | `1_000_031..1_000_035` |
| 12000.0 | `1_000_036..1_000_039` |

Cada bloque tiene capacidad `(#roots)×400` intentos de sprinkling antes de agotarse (2000 para
calibración por nivel, 2000/2000/2000/1600 para test) — margen amplio frente a M=200 admisibles
salvo que la tasa de `EMPTY_FAMILY` a esa intensidad sea patológicamente alta (>90%), caso
cubierto por §4c. Ningún root se comparte entre niveles ni entre roles: los 4×5 + 4×5(+4) = 39
roots (más el `1_000_000` excluido) cubren exactamente los 40 roots de `EXPLORE_POOL`, sin
solape.

### 4c. Regla `OUT_OF_DOMAIN_UNCALIBRATED` (congelada ahora, sin grados de libertad diferidos)

**Comité 018 §5 (hallazgo del falsificador #6) y §9.1(6): esta regla se congela ahora porque no
cuesta ningún grado de libertad nuevo — es consecuencia mecánica de números ya congelados
(bloques de roots fijos × 400 hijos × M=200) — diferirla sería peor que congelarla.**

- Si, para un nivel `n` dado, el bloque COMPLETO de roots asignado (§4b) se agota (todos sus
  roots consumen sus 400 hijos cada uno) sin alcanzar M=200 parches admisibles
  (`𝒜(C)≠∅`), ese nivel se marca **`OUT_OF_DOMAIN_UNCALIBRATED`** para el paso 3: no se calcula
  `μ_n` para ese nivel, no se amplía el bloque, no se toman roots de otro bloque/pool, no se
  reduce M. La ejecución se detiene y se reconvoca al comité con el hallazgo — igual que la regla
  de "HALT, no ajustar" de comité 017 ante un mismatch de Gate 0.
  Ancla: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md` D.2.3 (regla halt-no-adjust de Gate 0, mismo
  patrón aplicado aquí).
- Un nivel `OUT_OF_DOMAIN_UNCALIBRATED` en el paso 3 nunca se reporta como PASS ni como FAIL del
  mecanismo — es un tercer estado explícito, igual de visible, sin coerción silenciosa a
  PASS/FAIL (D.4, regla de reporte simétrico).
- La misma regla aplica simétricamente al paso 5 (test de falsación) sobre
  `MU_FALSIFICATION_TEST_ROOTS`, con su propio piso — ver §5.

### 4d. Tasa de `EMPTY_FAMILY` — reporte obligatorio, provenance-only, claim-inert

- Se reporta, por nivel `n` y por rol (calibración/test), la proporción observada:
  `rate_empty(n) := (# draws con 𝒜(C)=∅ encontrados) / (# draws totales intentados hasta juntar
  M admisibles o agotar el bloque)`. Esta es una proporción simple bajo una regla de parada
  secuencial (no un estimador insesgado de la tasa poblacional) — se etiqueta como tal; no se cita
  como si fuera una medición de tasa poblacional libre de sesgo de parada.
  Ancla: comité 018 §5 hallazgo del falsificador #6 (estimador bajo stop-at-M no está libre de
  sesgo de parada).
- **`rate_empty(n)` es diagnóstico de PROVENIENCIA únicamente — `CLAIM-INERT`.** Nunca se cita
  como evidencia de que el pipeline "ve geometría" ni de ninguna otra cosa que exceda la
  localización order-only de `r=2M` en el patch finito. Esto ata la cláusula permanente
  `NON_CORROBORATION` (comité 017 §8): ningún acuerdo futuro entre R-VAR y el estimador sellado
  `O_min` sobre un parche BH puede citarse como corroboración independiente del PASS de
  prereg-002, y del mismo modo `rate_empty` no se cita como evidencia física adicional más allá
  de su rol de diagnóstico interno.
- Este reporte ya es exigido por D.4 item 1 (`FP_RATE_NULL` por nivel de intensidad,
  `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md:472-473`) — no es una obligación nueva inventada por este
  addendum, sino la aplicación de una regla ya congelada.

## 5. Enrutamiento de salida, disciplina de etiquetas, y piso del paso 5

- Salida cruda del paso 3 (si se autoriza) a `dev/mu_freeze_table_raw.json`, no comiteada hasta
  el commit de freeze (paso 4).
- El commit de freeze (paso 4) debe incluir: los 4 valores `μ_n` (uno por nivel, condicionados
  per §0), `rate_empty(n)` por nivel (§4d), la provenance completa (commit HEAD, versión de
  python/numpy, bloque de roots y children exactos consumidos por sub-pool y nivel, timestamp
  UTC) — mismo patrón que `PR003_RVAR_GATE0_TIER0_REPORT.md`/`TIER1_REPORT.md`.
- Toda mención de la tabla μ debe portar su propio label de alcance:
  `MU_TABLE_STATUS = FROZEN [NULL_ONLY; PRE_BH_PATCH; EMPTY_FAMILY_CONVENTION=
  COND_ON_A(C)_NEQ_EMPTY_WITH_SEPARATE_RATE_REPORT; LEVELWISE_OOD=<lista de niveles
  OUT_OF_DOMAIN_UNCALIBRATED, si los hay>]` — nunca "μ" desnuda.
- `α := 0.05` se cita siempre con la advertencia ya fijada en v2.2 (reutilización de
  `THETA_FP`, no derivación) — no se relaja esa etiqueta en el commit de freeze.
- **Piso del paso 5 (test de falsación) — congelado ahora, cierra el riesgo de PASS vacío
  (comité 018 §5, hallazgo del falsificador, "verdict coercion"):** el test de falsación mínima
  de 015/017 sobre `MU_FALSIFICATION_TEST_ROOTS` requiere, por nivel, un mínimo de **200 parches
  nulos admisibles (`𝒜(C)≠∅`)** elegibles para el gate de μ (mismo valor que M, reutilizado por
  simetría — mismo argumento de granularidad de cuantil de §1, ningún número nuevo introducido).
  Si un nivel no alcanza ese piso dentro de su bloque asignado (§4b/§4c), el veredicto de
  falsación para ese nivel es **`INCONCLUSIVE`**, nunca `PASS` — un test que solo puede "pasar"
  porque casi todos los nulos abstuvieron por `EMPTY_FAMILY` no es un test con poder, y no se
  reporta como si lo tuviera.

## 6. Condición de parada

**Este addendum, aunque se comitee, NO autoriza la ejecución del paso 3 (cómputo de tabla μ) ni
ningún paso de Parte F.** Gate 0 Tier 0/Tier 1 PASS son condición NECESARIA (verifican que el
algoritmo D.2.1/D.2.2 es correcto) pero NO SUFICIENTE (no dicen nada sobre el objeto estadístico
de μ, que es lo que este addendum fija). Ejecutar Parte F (sprinkling de
`MU_CALIBRATION_ROOTS`/`MU_FALSIFICATION_TEST_ROOTS`, cómputo de `μ_n`, commit de freeze) requiere
una **autorización explícita separada del PI**, exactamente como Gate 0 Tier 0 → Tier 1
requirieron cada uno la suya en vez de heredar la del paso anterior. El objeto estadístico ya está
adjudicado (comité 018); lo que falta autorizar es la ejecución misma — dos eventos distintos, no
uno.

---

## Resumen para decisión del PI

- **Objeto estadístico de μ: RESUELTO** (comité 018, §0 arriba) — `μ_n` condicionado a
  `𝒜(C)≠∅`, tasa `EMPTY_FAMILY` reportada aparte, B rechazado por error de tipo.
- **Mecánico / sin grados de libertad reales:** §2 (spawn scheme, reusa Tier 1 verbatim, regla de
  agotamiento reconciliada), §3 (niveles, cita directa de `thresholds.INTENSITIES`), §4a-b
  (partición de roles y asignación root→nivel, ahora explícita y sin solape).
- **Con grados de libertad reales, fijados aquí con argumento explícito:** §1 (M=200,
  argumentado; ahora también aclarado que cuenta solo draws admisibles), §4c
  (`OUT_OF_DOMAIN_UNCALIBRATED`, congelado sin diferir), §5 (piso del paso 5, reutiliza M=200 sin
  introducir un número nuevo).
- **Ya no quedan huecos abiertos de redacción conocidos** tras esta revisión (comité 018 §9.1
  puntos 1-7 cerrados). Pendiente únicamente: (i) commit de esta revisión, sujeto a autorización
  del PI; (ii) opcionalmente, el test de falsación de bajo costo que propuso el falsificador de
  018 (dos agentes independientes escriben el plan de consumo exacto a partir de este texto y se
  comparan — cero semillas, cero ejecución) como chequeo de que la ambigüedad quedó realmente
  cerrada; (iii) tras (i), una autorización explícita y separada del PI para ejecutar el paso 3 de
  Parte F — no concedida por este documento.
