# Plan operativo definitivo — 15 julio 2026

Conversión en hoja de ruta del trabajo sobre evidencia positiva, transferencia 1+1D -> 3+1D y
recoverability Schwarzschild desde `order+number`. Sigue el formato de
`docs/plan_avanzado_14_julio_2026.md`: anclajes verificables, dependencias, gates, terminales
explícitos y reglas de parada.

> **Estado:** `DRAFT_OPERATIONAL_PLAN` / `REVISABLE` / `THEORY_FIRST` /
> **`PROGRAM_NORTH_PARTIALLY_SUPERSEDED` (2026-07-28)**
>
> No es preregistro, no congela umbrales y no autoriza ejecución. Los documentos de fases futuras
> solo podrán adquirir estado normativo mediante sus propios gates `/comite`, `/auditor` y decisión
> explícita del PI.

**Commit de referencia:** `584a9f0`.

**Precedencia (actualizada 2026-07-28):** la hoja de ruta de **norte de programa** y de producto
del ciclo vigente es

- `research_program/synthesis/phase0_program_north_decision.md` (Fase 0; R1–R3),
- `tarea_grok_2.md` (Fases 0–4 unificadas).

En particular, el norte **localizar / reconstruir horizonte Schwarzschild 3+1 order-only**
mediante nuevos localizadores de la matriz post-PR008 queda
`ABANDONED_AS_PROGRAM_NORTH` bajo R1 de la Fase 0 (pendiente `PI_SIGN_OFF` del checklist).
Este plan del 15-jul **se conserva** como fotografía operativa THEORY_FIRST y como referencia de
PR011/PR012, order+number y transferencia; **no** autoriza reabrir ese norte abandonado.
Conserva `docs/plan_avanzado_14_julio_2026.md` como fotografía del 14-07-2026 y no reinterpreta
ningún resultado PR-003/PR011/PR012.

---

## 0. Diagnóstico verificado que motiva el plan

1. **La certificación PR011/PR012 disponible es de cota superior.** PR011 certificó
   `TV <= epsilon` mediante Hellinger en `n=4,...,8`
   (`research_program/synthesis/pr011_mass_distinguishability_viability.md:347-350`). Esto
   certifica dificultad. `epsilon < 1` excluye `TV=1`, no `TV=0`; la prueba `TV>0` de la familia
   procede de un argumento de rigidez separado.
2. **No existe todavía tecnología general de cota inferior poset-level.** Recoverability positiva
   necesita un testigo order-only y una pérdida geométrica preespecificada. Separar dos leyes no
   equivale por sí solo a localizar una frontera.
3. **El régimen PR011 es casi ciego.** Sus cotas implican suelo minimax `0.4954-0.4977`
   (`pr011_mass_distinguishability_viability.md:352-359`). El valor
   `H² = 1.329351347556e-06` (`:344`) sugiere la escala de puntos
   `n_release ~ 1/H² ~ 7.5e5` `[HEURÍSTICA, NO CERTIFICADA]`. Esta escala indica cuándo la cota
   superior de puntos deja de forzar ceguera; no es el `n_star` de recuperación del poset.
4. **PR012 sigue siendo `DRAFT_SCOPE`.** Estudia `TV` frente a `Delta tau` a `n=8` fijo, no una
   escalera de densidad ni de patch (`research_program/synthesis/pr012_tv_curve_scope.md:20-27`).
   Sus abstenciones `GRID_RESOLUTION_ABSTAIN` son un precedente formal útil (`:69-71`).
5. **La transferencia dimensional está abierta.** La órbita directa de dilatación puede
   generalizarse: masa y patch co-escalados preservan orden y la normalización elimina el factor
   global al condicionar en `N=n`. Lo específicamente 2D es la recíproca basada en cópulas:
   "`TV=0` si y solo si misma órbita de escala". Esa clase debe rederivarse en 3+1D.
6. **El selector relacional sigue abierto.** `dev/PR003_C1_RELATIONAL_SPEC.md:174-182` mantiene
   abiertos score, control de bulk, promoción e interpretación física. No se importará a 3+1D
   antes de fijar el target que deba seleccionar.

---

## 1. Reglas transversales

### 1.1 Puerta WP5 para todo trabajo 1+1D

Todo ítem nuevo 1+1D debe declarar en su spec:

1. qué pregunta 3+1D responde;
2. qué objeto transfiere: teorema, certificador, ley de escala o control;
3. qué resultado negativo haría innecesario continuar;
4. por qué no es tuning del pipeline sellado.

Si una tarea 1+1D no sirve demostrablemente a la decisión 3+1D, emite
`WP5_RELEVANCE_FAIL` y no se ejecuta.

### 1.2 Separación obligatoria de capas

- `dev/`: selección de candidatos y falsificación barata.
- teoría: teoremas, contraejemplos y contratos estadísticos, sin evidencia física empírica.
- confirmación: semillas vírgenes, spec congelada, artefacto primario y terminal automático.
- embedding: solo generador, ground truth y scoring; nunca inferencia.

### 1.3 Dos límites, dos escaleras

- **Densidad:** `rho -> infinity`, o `ell -> 0`, a geometría y patch físicos fijos.
- **Extensión:** patch creciente a geometría y `ell` fijos.

No se variarán juntos atribuyendo el resultado a uno solo.

### 1.4 Dirección de la evidencia

- cota superior de TV: dificultad o blindness;
- cota inferior de TV: separación observable;
- pérdida geométrica: fidelidad del reconstructor;
- cota inferior + pérdida: candidato a recoverability positiva.

### 1.5 Toda fase puede fallar o abstenerse

Un gate sin terminal negativo es decoración. `FAILED_DATA_CONTRACT`, `LEAKAGE_DETECTED`,
`RESOURCE_ABORT` y los modos `ABSTAIN` tienen precedencia sobre cualquier terminal científico.

---

## 2. Rúbrica ejecutable de transferencia y confirmación

La rúbrica original de siete ejes se amplía con canal/escala y abstención. Cada celda debe contener
un puntero `file:line`, una demostración o el literal `NO_ESPECIFICABLE`.

| Eje | Pregunta obligatoria | Terminal negativo mínimo |
|---|---|---|
| Target | ¿Qué objeto continuo y discreto se estima? | `TARGET_NOT_SPECIFIABLE` |
| Orientación/dualidad | ¿Convención o acción sobre `G union G^op`? | `DUAL_CLOSURE_FAIL` |
| Canal/escala | ¿`fixed_n` u `order+number`; qué se conoce de `rho`? | `CHANNEL_AMBIGUOUS` |
| Patch | ¿Qué información pierde la truncación y cómo se extiende? | `PATCH_CONTRACT_FAIL` |
| Límite continuo | ¿Qué ley se reclama en densidad y cuál en extensión? | `LIMIT_NOT_TESTABLE` |
| Salida/pérdida | ¿Salida order-only y geometría solo en scoring? | `TARGET_WITNESS_MISMATCH` |
| Alternativas | ¿Contra qué nulas y adversarias se separa? | `ADVERSARIAL_CLASS_MISSING` |
| Garantía | ¿Cota superior, inferior o ambas, y a qué nivel? | `GUARANTEE_DIRECTION_MISSING` |
| Abstención | ¿Cuándo debe negarse a producir salida? | `ABSTENTION_NOT_DEFINED` |

---

## Fase 0 — Auditoría de supervivencia y gramática de claims

**Estado al abrir:** sin código, sin simulaciones y sin tocar sellos.

### OP-0.1 Matriz de supervivencia PR011/PR012

Aplicar la rúbrica de §2 a:

- familia `G_diamond`;
- canal `N=n`;
- target escalar `tau`;
- certificador Hellinger;
- escalera `n=4,...,8`;
- curva PR012 en `Delta tau`;
- interfaz `H[C;R]` y selector de `R`.

**Entregable:** `research_program/synthesis/survival_matrix_1p1_to_3p1.md`.

**Gate:** `/auditor` verifica que cada celda tenga anclaje real o `NO_ESPECIFICABLE` honesto.

**Terminales:**

- `SURVIVAL_MATRIX_COMPLETE`
- `SURVIVAL_MATRIX_BLOCKED(<celda>)`
- `SURVIVAL_MATRIX_AUDIT_FAIL`

**Puerta WP5:** la matriz decide qué partes 1+1D pueden financiar trabajo 3+1D; no produce ciencia
nueva 1+1D.

### OP-0.2 Gramática de claims

Congelar para textos futuros las siguientes fronteras:

- **Teleología:** un patch finito puede recuperar un proxy cuasi-local dentro de una familia; no
  define por sí solo el horizonte de eventos global. Cualquier convergencia debe probarse bajo
  límites separados de densidad y extensión.
- **Orientación:** localización equivariante bajo dualidad; carácter BH/WH anti-equivariante o
  condicionado a una convención temporal congelada.
- **Escala:** `N` estima `rho V`; lo intrínseco se expresa en unidades de
  `ell = rho^(-1/d)`. Identificar `rho` con una escala física es otra hipótesis.
- **Ensemble/instancia:** performance con alta probabilidad sobre sprinklings; unicidad
  single-instance solo bajo hipótesis declaradas de buen condicionamiento.
- **Adversarial:** control de error bajo la familia objetivo y separación frente a alternativas
  son garantías distintas.
- **Dinámica:** sprinklear una geometría conocida no demuestra emergencia dinámica; la supresión
  de órdenes no manifold-like es una condición separada.

**Entregable:** `docs/claim_grammar.md`.

**Gates:** `/comite` adopta la gramática; `/auditor` verifica anclajes y que ninguna frase convierta
un objetivo en resultado.

**Terminales:**

- `CLAIM_GRAMMAR_ADOPTED`
- `CLAIM_GRAMMAR_OVERCLAIM`
- `CLAIM_GRAMMAR_ANCHOR_FAIL`

### Gate de Fase 0

```text
PHASE_0_AUDIT_READY =
  SURVIVAL_MATRIX_COMPLETE
  + CLAIM_GRAMMAR_ADOPTED
```

---

## Fase 1 — Cierre teórico previo a código 3+1D

**Dependencia:** puede redactarse en paralelo a Fase 0, pero no cerrarse antes de
`PHASE_0_AUDIT_READY`.

### OP-1.1 Target esférico y clausura dual

Definir la familia provisional:

```text
G_3p1_pm = G_BH union G_WH = G union G^op
```

El target continuo primario será el atrapamiento puntual en simetría esférica: signo de las dos
expansiones nulas futuras de las esferas de simetría, con frontera `r=2M` en Schwarzschild.

Separar salidas:

```text
H_hat(P^op)   = H_hat(P)       # localización bajo la correspondencia dual
chi_hat(P^op) = -chi_hat(P)    # carácter BH/WH
```

Tareas:

1. fijar patches BH/WH emparejados y la involución sobre bordes;
2. separar orientación temporal de dirección exterior;
3. declarar truncaciones angular, radial y temporal;
4. definir canales `fixed_n` y `order+number` sin mezclarlos;
5. especificar target, salida, pérdida y abstención sin embedding en inferencia.

**Terminales:**

- `DUAL_FAMILY_CLOSED`
- `DUAL_CLOSURE_NOT_SPECIFIABLE`
- `PATCH_DUALITY_MISMATCH`
- `TARGET_NOT_SPECIFIABLE`

### OP-1.2 Clase `TV=0` en 3+1D

Distinguir:

1. igualdad de leyes a un `n` fijo;
2. igualdad para todo `n`;
3. equivalencia o contigüidad asintótica.

Tareas:

- probar la inclusión de la órbita de dilatación cuando masa y patch co-escalan;
- estudiar la recíproca dentro de `G_3p1_pm` usando rigidez causal/volumen apropiada a `d>2`, no
  cópulas 2D;
- declarar qué información añade `N` con `rho` conocida;
- comprobar si `H/chi` es constante sobre las clases `TV=0` relevantes;
- si la clasificación completa es inabordable, restringir el lema a las parejas que usaría el
  futuro preregistro.

**Terminales:**

- `TV_ZERO_CLASS_CHARACTERIZED`
- `TV_ZERO_CLASS_SCOPED_TO_CANDIDATE_FAMILY`
- `TARGET_NONIDENTIFIABLE_TV_ZERO`
- `TV_ZERO_CHARACTERIZATION_OPEN`

Solo los dos primeros permiten avanzar; el segundo restringe el claim a la subfamilia probada.

### OP-1.3 Protocolo de evidencia positiva

Para un testigo preespecificado `f: Omega_n -> [0,1]`:

```text
TV(P,Q) >= |E_P[f] - E_Q[f]|.
```

Una forma de certificado unilateral será:

```text
TV_lower_f = max(0, |mu_hat_P - mu_hat_Q| - radius_P - radius_Q).
```

Debe cerrarse:

- desigualdad de concentración y sus hipótesis;
- selección del testigo separada de certificación, o cota uniforme válida;
- corrección por multiplicidad sobre `n`, masas, patches y alternativas;
- muestreo fijo o confidence sequence si existe parada secuencial;
- error del generador exacto/aproximado dentro de la cobertura;
- pérdida geométrica independiente de la separación estadística;
- definición posterior de
  `n_star(delta_tau; eta) = min{n: TV_lower_f >= eta}`.

El testigo óptimo para TV no se identificará automáticamente con el proxy físico. Solo un testigo
que además satisfaga la pérdida congelada habilita recoverability.

**Terminales:**

- `POSITIVE_EVIDENCE_PROTOCOL_PROVED`
- `ADAPTIVE_SELECTION_UNCONTROLLED`
- `GENERATOR_ERROR_NOT_BOUNDED`
- `NO_VALID_POSITIVE_CERTIFICATE`
- `TARGET_WITNESS_MISMATCH`

### OP-1.4 Orientación estadística, opcional

Preguntar si las leyes BH/WH son estadísticamente distinguibles sin convención. No es requisito
para claims de localización y solo se abre si se pretende inferir carácter sin fijar orientación.

**Terminales:** `ORIENTATION_LEMMA_PROVED` / `ORIENTATION_CONVENTION_REQUIRED` /
`ORIENTATION_LEMMA_OPEN`.

### OP-1.5 Selector de `R`, diferido

No reabrir el selector relacional hasta que OP-1.1 fije qué target 3+1 debe seleccionar. La
interfaz `H[C;R]` puede sobrevivir formalmente mientras `R(C)` siga siendo el bloqueo físico.

### Gate de Fase 1

```text
PHASE_1_THEORY_READY =
  DUAL_FAMILY_CLOSED
  + (TV_ZERO_CLASS_CHARACTERIZED
     or TV_ZERO_CLASS_SCOPED_TO_CANDIDATE_FAMILY)
  + POSITIVE_EVIDENCE_PROTOCOL_PROVED
```

Requiere revisión bibliográfica primaria, revisión matemática independiente, `/comite` y
`/auditor` antes de convertirse en contrato de implementación.

---

## Fase 2 — Certificador positivo y ley de escala 1+1D

**Dependencias:** `PHASE_0_AUDIT_READY` y protocolo OP-1.3 probado. No requiere cerrar todavía toda
la geometría 3+1D, pero cada ítem pasa la puerta WP5.

### OP-2.1 Certificador positivo de referencia

Implementar un módulo genérico que reciba dos streams de `f(C) in [0,1]` y produzca una cota
inferior unilateral auditable.

Verificaciones mínimas:

- leyes sintéticas con TV conocida;
- cobertura, reproducibilidad y multiplicidad;
- optional stopping si aplica;
- abstención por precisión o recursos;
- prueba de que el estimador de intervalo no consume información geométrica.

PR011 puede usarse como banco de integración, nunca como nueva confirmación física.

**Terminales:**

- `POSITIVE_CERTIFIER_REFERENCE_PASS`
- `REFERENCE_COVERAGE_FAIL`
- `REFERENCE_REPRODUCIBILITY_FAIL`
- `REFERENCE_PRECISION_ABSTAIN`
- `POSITIVE_CERTIFIER_INVALID`

**Puerta WP5:** produce la tecnología que necesitará 3+1D cuando enumerar posets sea imposible.

**Terminal registrado:** `POSITIVE_CERTIFIER_REFERENCE_PASS` (run 2026-07-15, freeze commit
`cd3ef51`, artefacto `results/op21_reference_certifier_report.json`, git-ignored por diseño).
R6 (auditoría independiente, decisión 034 §9) satisfecho por dos pasadas: auditor report 017
(commit `43b28e4`, `AUDIT_PASS_WITH_WARNINGS`, misma sesión que R1-R5 — advertencia #31 de
independencia de sesión) y auditor report 018 (commit `22f7719`, `AUDIT_PASS_WITH_WARNINGS`,
sesión nueva y separada de R1-R5 y del report 017; recomputación independiente de `report_hash`,
`p0` por tercer método, bandas C1/C2, banda de semillas y detección MUT-A/MUT-B). Los 22 warnings
restantes en ambos informes son deuda histórica de `data/reports/` ajena a OP-2.1. Este terminal
es un input verificado del gate de Fase 2 abajo; el gate en su conjunto permanece abierto hasta
terminal explícito de OP-2.2, terminal explícito de OP-2.3 y decisión explícita sobre PR012.

### OP-2.2 Testigo de desarrollo en la familia PR011

Solo en `dev/`, con semillas de desarrollo y candidatos declarados antes de scoring:

- explorar testigos sobre `tau=0.95` frente a `1.05`;
- separar cota inferior de TV y fidelidad geométrica;
- seleccionar como máximo un testigo para una futura spec;
- no llamarlo proxy de horizonte si solo discrimina masas.

Una candidata PR013 solo puede proponerse después de `/comite`; este plan no la abre.

**Terminales:**

- `REFERENCE_WITNESS_READY_FOR_FREEZE`
- `REFERENCE_WITNESS_SEPARATION_ONLY`
- `REFERENCE_WITNESS_INCONCLUSIVE`
- `REFERENCE_WITNESS_FAIL`

**Puerta WP5:** valida selección/certificación del testigo y cuantifica cuánto orden conserva del
canal de puntos.

### OP-2.3 Ley `n_star(Delta tau)`

Con el certificador y un testigo congelado, medir la menor cardinalidad donde la cota inferior
poset-level cruza un umbral `eta` preespecificado. Contrastar, sin asumir, la heurística Fisher.

Separar siempre:

- `n_release`: escala heurística del canal de puntos;
- `n_star`: cruce certificado del testigo poset-level;
- coste Monte Carlo: número de realizaciones necesario para resolver el intervalo.

**Terminales:**

- `SCALING_LAW_MEASURED`
- `SCALING_LAW_PARTIAL`
- `SCALING_LAW_UNRESOLVED`
- `SCALING_RESOURCE_ABSTAIN`

**Puerta WP5:** sin ley de escala no puede presupuestarse honestamente un experimento 3+1D.

### OP-2.4 Re-adjudicación de PR012

Tras OP-2.1/OP-2.3, `/comite` propone y el PI decide entre:

1. ejecutar PR012 tal como está;
2. re-scope hacia la ley de escala;
3. cerrarlo sin ejecución con terminal explícito.

Este plan no cancela, congela ni ejecuta PR012.

**Terminales:**

- `PR012_EXECUTE_AS_DRAFT_SCOPE`
- `PR012_RESCOPE_TO_SCALING`
- `PR012_CLOSE_WITHOUT_EXECUTION`
- `PR012_DECISION_DEFERRED`

### Gate de Fase 2

```text
PHASE_2_POSITIVE_REFERENCE_READY =
  POSITIVE_CERTIFIER_REFERENCE_PASS
  + terminal explícito de OP-2.2
  + terminal explícito de OP-2.3
  + decisión explícita sobre PR012
```

Un resultado inconcluso no se convierte en GO por prosa.

---

## Fase 3 — GO/NO-GO para desarrollo 3+1D

**Dependencias obligatorias:**

1. `SURVIVAL_MATRIX_COMPLETE`;
2. `CLAIM_GRAMMAR_ADOPTED`;
3. `PHASE_1_THEORY_READY`;
4. `POSITIVE_CERTIFIER_REFERENCE_PASS`;
5. terminal de ley de escala, aunque sea parcial o abstención bien explicada;
6. decisión explícita sobre PR012.

`/comite` debe evaluar, como mínimo:

- identificabilidad del target dentro de la clase `TV=0`;
- coste proyectado desde `n_star` y coste Monte Carlo;
- disponibilidad de generador causal 3+1D verificable;
- riesgo de leakage y automorphism/relabeling;
- clase adversarial mínima;
- si el resultado posible justifica el coste.

**Terminales:**

- `GO_3P1_DEVELOPMENT`
- `NO_GO_3P1_THEORY_INCOMPLETE`
- `NO_GO_3P1_RESOURCE_INFEASIBLE`
- `NO_GO_3P1_TARGET_NONIDENTIFIABLE`
- `DEFER_3P1_PENDING_EVIDENCE`

Solo `GO_3P1_DEVELOPMENT`, seguido de autorización explícita del PI, abre Fase 4. No abre
preregistro ni confirmación.

---

## Fase 4 — Preflight y desarrollo 3+1D

### OP-4.1 Data contract del generador

Tareas:

1. implementar o reutilizar relación causal Schwarzschild 3+1D con casos analíticos;
2. verificar Poisson, volumen, unidades y `ell=rho^(-1/4)`;
3. verificar covarianza de escala donde corresponda;
4. verificar dualidad mediante acoplamiento o transformación estructural BH/WH; Monte Carlo solo
   diagnostica, no prueba igualdad en ley;
5. proyectar a registro `order+number` sin coordenadas, radios o etiquetas;
6. verificar relabeling/automorfismos;
7. mantener ground truth en una capa de scoring separada;
8. medir cobertura, coste y errores antes de puntuar proxies.

**Terminales:**

- `GENERATOR_3P1_DATA_CONTRACT_PASS`
- `CAUSAL_RELATION_VERIFICATION_FAIL`
- `DUAL_GENERATOR_MISMATCH`
- `ORDER_PROJECTION_LEAK`
- `GENERATOR_RESOURCE_INFEASIBLE`
- `FAILED_DATA_CONTRACT`

### OP-4.2 Desarrollo del testigo/proxy

Solo tras `GENERATOR_3P1_DATA_CONTRACT_PASS`:

- declarar una lista corta de familias de candidatos;
- verificar equivariancia de `H_hat` y anti-equivariancia de `chi_hat`;
- medir separación y pérdida geométrica por separado;
- incluir salida `ABSTAIN`;
- falsificar borde, densidad, cardinalidad, truncación y singularidad;
- evaluar MINK/no-horizonte, WH dual, patch-shift, mass-shift, scale-orbit y controles de borde;
- seleccionar como máximo un candidato para freeze.

**Terminales:**

- `WITNESS_CANDIDATE_READY_FOR_FREEZE`
- `CANDIDATE_FAMILY_NEGATIVE_RESULT`
- `TARGET_WITNESS_MISMATCH`
- `DUAL_EQUIVARIANCE_FAIL`
- `BOUNDARY_DOMINATED`
- `NO_CERTIFIED_DEV_SEPARATION`
- `ABSTENTION_RATE_INFEASIBLE`

Un resultado negativo cierra la familia probada; no autoriza rediseño sobre las mismas muestras.

---

## Fase 5 — GO/NO-GO confirmatorio y preregistro 3+1D

**Dependencias:** `GENERATOR_3P1_DATA_CONTRACT_PASS` y un único
`WITNESS_CANDIDATE_READY_FOR_FREEZE`.

### OP-5.1 Decisión confirmatoria

`/comite` evalúa la matriz de nueve ejes completa y emite:

- `GO_3P1_CONFIRMATION`
- `NO_GO_3P1_CANDIDATE_INSUFFICIENT`
- `NO_GO_3P1_ADVERSARIAL_GAP`
- `NO_GO_3P1_COMPUTE_INFEASIBLE`
- `DEFER_3P1_CONFIRMATION`

### OP-5.2 Prerregistro

Debe congelar:

- familia dual, masas y patches;
- canal `fixed_n` y/o `order+number`;
- semillas confirmatorias vírgenes;
- testigo, salida, orientación y abstención;
- pérdida set-valued y de carácter;
- `TV_lower_f`, confianza y multiplicidad;
- `eta`, `n_star` y presupuesto Monte Carlo;
- alternativas adversariales;
- escalera de densidad y escalera de patch separadas;
- error del generador;
- precedencia completa de terminales.

**Gate:** `/comite`, `/auditor` de leakage, `/auditor` estadístico y autorización explícita del PI.

**Terminales de bloqueo:**

- `PREREG_3P1_READY`
- `PREREG_TARGET_AMBIGUOUS`
- `PREREG_THRESHOLDS_UNANCHORED`
- `PREREG_ADVERSARIAL_INCOMPLETE`
- `PREREG_COMPUTE_INFEASIBLE`
- `PREREG_AUDIT_FAIL`

---

## Fase 6 — Ejecución confirmatoria

**Dependencia:** preregistro sellado y autorización expresa.

Orden obligatorio:

1. verificar código, entorno, hashes y semillas;
2. ejecutar data contract antes de scoring;
3. materializar artefacto primario inmutable;
4. releer el artefacto persistido;
5. calcular terminales automáticamente;
6. auditar antes de interpretar.

**Terminales científicos:**

- `PASS_WITNESS_SEPARATION_ONLY`
- `PASS_SET_LOCALIZATION_NO_CONVERGENCE`
- `PASS_DENSITY_CONVERGENCE_PATCH_OPEN`
- `PASS_PATCH_STABILITY_DENSITY_OPEN`
- `PASS_BOTH_LIMITS_WITHIN_FROZEN_FAMILY`
- `FAIL_NO_POSITIVE_SEPARATION`
- `FAIL_GEOMETRIC_FIDELITY`
- `FAIL_ADVERSARIAL_SPECIFICITY`

**Terminales con precedencia:**

- `FAILED_DATA_CONTRACT`
- `LEAKAGE_DETECTED`
- `RESOURCE_ABORT`
- `PRECISION_ABSTAIN`
- `INSUFFICIENT_VALID_LEVELS`

Ningún PASS implica horizonte de eventos global, Kerr, reconstrucción métrica general o dinámica
de gravedad cuántica.

---

## Fase 7 — Puente intrínseco hacia área

**Dependencia:** localización confirmada y especificidad adversarial dentro de la familia.

Usar `H_hat` para producir el corte/partición requerido por horizon molecules o un canal de área
equivalente, manteniendo el horizonte verdadero solo en scoring.

Tareas:

- recuperar área en unidades de `ell`;
- controlar borde y dependencia del corte;
- comparar cortes nulos no-horizonte y particiones desplazadas;
- separar ley en esperanza de recoverability single-instance.

**Terminales:**

- `AREA_RECOVERY_CONFIRMED_WITH_INTRINSIC_CUT`
- `LOCALIZATION_PASS_AREA_FAIL`
- `AREA_SIGNAL_CUT_GENERIC`
- `AREA_SINGLE_INSTANCE_INCONCLUSIVE`

Esta fase es el puente cuantitativo hacia termodinámica de agujeros negros; no forma parte del claim
mínimo de localización 3+1D.

---

## Fase 8 — Puente a dinámica de gravedad cuántica

**Dependencia:** opcional; no bloquea Fases 0-7.

Requiere una dinámica y medida declaradas, gate independiente de manifold-likeness, tratamiento de
dominación entrópica y una definición del target cuando no existe embedding conocido.

**Terminales:**

- `DYNAMICAL_BRIDGE_NOT_YET_DEFINED`
- `MANIFOLDLIKE_SECTOR_NOT_ESTABLISHED`
- `OBSERVABLE_TRANSFERS_TO_DYNAMICAL_ENSEMBLE`

Un PASS sobre sprinklings Schwarzschild no abre automáticamente esta fase.

---

## Orden de dependencias e hitos

```text
M0  PHASE_0_AUDIT_READY
        |
        +--> M1 PHASE_1_THEORY_READY
        |          |
        +--> M2 PHASE_2_POSITIVE_REFERENCE_READY
                   |
                   v
             M3 GO_3P1_DEVELOPMENT
                   |
             M4 GENERATOR_3P1_DATA_CONTRACT_PASS
                   |
             M5 WITNESS_CANDIDATE_READY_FOR_FREEZE
                   |
             M6 GO_3P1_CONFIRMATION / PREREG_3P1_READY
                   |
             M7 CONFIRMATORY_TERMINAL_EMITTED
                   |
             M8 AREA_BRIDGE_TERMINAL_EMITTED
```

Fase 1 puede investigarse en paralelo a Fase 0, pero no cerrarse antes de su auditoría. Fase 2 solo
abre código 1+1D después de probar OP-1.3. Ningún código 3+1D abre antes de `GO_3P1_DEVELOPMENT`.

---

## Reglas de parada

| Si ocurre | Acción obligatoria |
|---|---|
| Fase 0 no completa anclajes | no congelar gramática ni supervivencia |
| Target no constante sobre clase `TV=0` | no abrir código 3+1D para ese target |
| Protocolo positivo inválido | no ejecutar Monte Carlo científico |
| Tarea 1+1D falla puerta WP5 | no ejecutarla |
| Certificador falla cobertura | reparar método; no cambiar target |
| Ley de escala queda abstain | presupuestar con el límite demostrado, no extrapolar |
| GO desarrollo es negativo | no construir generador/proxy 3+1D |
| Generador falla data contract | no puntuar candidatos |
| Candidato no separa o no localiza | cerrar familia; no retunar en las mismas muestras |
| Preregistro no ancla umbrales | no consumir semillas confirmatorias |
| Confirmación falla contrato/leakage | no emitir terminal científico |
| Separa pero no localiza | claim solo de testigo |
| Localiza sin ambos límites | nombrar exactamente el límite abierto |
| Área falla | conservar localización; no promover a termodinámica |

---

## Qué NO autoriza este plan

- Iniciar Fase 0 o Fase 1 sin una instrucción posterior explícita.
- Ejecutar, congelar, cancelar o re-scope PR012 sin OP-2.4 y decisión comité+PI.
- Abrir PR013 o un preregistro de estimación de masa.
- Tocar `thresholds.py`, prereg-002/003 o el sello `6e2c3888`.
- Consumir semillas confirmatorias.
- Escribir o ejecutar código 3+1D antes de `GO_3P1_DEVELOPMENT`.
- Emitir claims 3+1D antes de un terminal confirmatorio auditado.
- Presentar `n_release` como `n_star`.
- Presentar un testigo discriminante como reconstructor sin pérdida geométrica.
- Inferir emergencia dinámica a partir de sprinklings de una geometría conocida.

## Próximo paso propuesto

Una vez aceptado este plan, la primera unidad operativa propuesta es **Fase 0, OP-0.1: matriz de
supervivencia**, completamente read-only respecto de código y datos. Su inicio requiere una nueva
instrucción explícita del PI.
