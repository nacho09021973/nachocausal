# Nota de ampliación acotada del perímetro — R4

```text
ESTADO: FIRMADA — R4 AUTORIZADO (ver §10)
FECHA: 2026-08-28
AMPLIA: docs/program_reopening_note_2026-07-31.md (perímetro R1, R2)
        docs/program_reopening_note_2026-08-05_R3.md (perímetro R3)
NO_REVOCA: docs/program_closure_note_2026-07-30.md, que permanece íntegra
SELLO: intacto — no se toca
       nachocausal/thresholds.py sha256 =
       6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
SEMILLAS: banda virgen [2,000,000–2,999,999] permanece sin quemar
NATURALEZA: documental y de gobernanza. Cero semillas, cero simulación, cero ejecución.
ORIGEN: comité 051, condición G1
        docs/comite/comite_decision_051_s1-gate-geometric-tangent-classification.md
```

## 1. Por qué hace falta esta nota, y por qué llega tarde

La regla §6.1 de la nota del 31 de julio dice literalmente: *«Perímetro fijo: R1 y R2.
Nada entra sin una nueva nota firmada.»*

Se ha buscado, sin suponerlo, una autorización posterior que ya cubra el trabajo del
2026-08-28. Ámbitos existentes, leídos en su literalidad:

- **R1** (`program_reopening_note_2026-07-31.md:25-29`) — llevar
  `docs/manuscript_limits_draft.md` a entregable. Es redacción, no investigación.
- **R2** (`:30-35`) — derivar analíticamente el exponente `λ⁶` de
  `wp4_fisher_localization_floor.md` §5a. **Menciona «Fisher», pero es otro objeto**: el
  suelo de localización cerca del horizonte, no la eficiencia Fisher del poset no
  etiquetado.
- **R3** (`program_reopening_note_2026-08-05_R3.md:38-43`) — lista cerrada: cerrar el
  puente E, redactar el resultado de la dicotomía de cópula nula, y la auditoría de
  novedad.

**Ninguna de las tres cubre la frontera de tangente geométrico y retención Fisher.** No
existe nota posterior. `docs/backlog_hallazgos.md` —destino obligado de todo hallazgo
fuera de perímetro por la regla §6.2— no existe.

```text
R4_GOVERNANCE_GAP = CONFIRMED
```

Esta nota se redacta **después** de que el trabajo empezara, y eso se dice sin
suavizarlo. La brecha fue detectada por el comité 051, no por el guardarraíl que debía
haberla impedido: **el guardarraíl falló, y queda registrado que falló.**

Esta nota hace dos cosas distintas que no deben confundirse: **ratifica
retroactivamente** lo ya comprometido (§3) y **autoriza hacia adelante** una lista
cerrada (§5). La ratificación retroactiva es una excepción documentada, no un
precedente.

## 2. Hechos verificados en esta sesión

```text
git branch --show-current  -> emergencia/p1a-canal-sigma-m
git rev-parse HEAD         -> 99cec0d8f479620938e475c563cf9799cfed4692
git rev-parse @{u}         -> 99cec0d8f479620938e475c563cf9799cfed4692   (rama sincronizada)
make verify-seal           -> 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
                              coincide con docs/preregistration_002.md:7-8 — SELLO INTACTO
```

Los tres commits en cuestión, verificados literalmente y no supuestos:

```text
236b1824d86ad3c169e574bf263ecde40310eb04  2026-08-28  Ignacio
  prove asymptotic Fisher efficiency for unlabeled 2D posets
4bcbfc50a95ddb7af52bfa002974016b9eafbd43  2026-08-28  Ignacio
  document unlabeled 2D poset Fisher theorem
99cec0d8f479620938e475c563cf9799cfed4692  2026-08-28  Ignacio
  add September roadmap for geometric tangent bridge
```

## 3. Situación de los tres commits: dos ejes que no se mezclan

**Eje A — validez matemática y documental.** No está en cuestión y esta nota no la toca.
El comité 051 verificó que el sello permanece intacto, que ningún instrumento sellado
fue tocado, que no se consumió ninguna semilla y que no hay simulación. El teorema de
`236b182` sigue en pie por su propia demostración.

**Eje B — situación de gobernanza en el momento de ser creados.** Fuera de perímetro. No
llevaban nota firmada ni línea `GOBERNANZA:`, a diferencia del hermano de R3
(`research_program/work_packages/wp6_d2_null_copula_dichotomy.md:7`).

```text
COMMITS: 236b1824, 4bcbfc50, 99cec0d8
EJE_A_VALIDEZ_MATEMATICA: NO_AFECTADA_POR_ESTA_NOTA
EJE_B_GOBERNANZA: OUT_OF_SCOPE_AT_COMMIT_TIME
DECISION_R4: RETROSPECTIVELY_RATIFIED_BY_R4
```

**R4 no borra ni disimula la brecha.** Ratificar significa admitir el trabajo al
perímetro hacia adelante, no reescribir la historia diciendo que estaba autorizado.

Condiciones de la ratificación:

1. Se crea `docs/backlog_hallazgos.md` y se registra allí esta brecha con su fecha, de
   modo que quede en acta y no se pierda al ratificarse.
2. Todo artefacto de R4, incluidos los ya comprometidos cuando se editen, lleva cabecera
   `GOBERNANZA:` apuntando a esta nota.

## 4. Qué se añade — un solo frente

```text
R4 — GEOMETRIC FISHER-RETENTION BRIDGE IN d=2
```

El objeto autorizado es **exclusivamente** la cadena:

```text
conformal perturbation in a 1+1 null diamond
  -> copula tangent
  -> rank/permutation score
  -> exact channel Pi_N -> [P_Pi_N]
  -> relative Fisher-information retention
```

**Resultados de entrada preservados, no reabiertos:**

```text
ASYMPTOTIC_POSET_FISHER_EFFICIENCY_FOR_BOUNDED_SEPARABLE_SCORES
FAMILY_FROZEN
NO_UNIVERSALITY_CLAIM
PRIORITY = PROVISIONAL_NOT_SEALED
```

`docs/hoja_de_ruta_septiembre_2026.md` es el plan de referencia. **La hoja de ruta es
PLAN, no autorización automática de todas sus fases**; ella misma se autodeclara «Plan
REVISABLE, no congelado» (`:3`). Las fases S3–S7 no quedan autorizadas por existir en
ese documento.

## 5. Qué autoriza R4 — lista cerrada

1. **Regularizar y preservar** los tres commits del 2026-08-28 identificados en §2, en
   los términos del §3.

2. **Cerrar S1**, `GEOMETRIC_TANGENT_CLASSIFICATION`, incluyendo y sólo incluyendo:
   - la derivación `geometric -> density -> copula tangent`;
   - la clasificación del sector **symmetric rank-one**;
   - las hipótesis necesarias sobre `a_{i,N}`;
   - los falsificadores analíticos;
   - correcciones **puramente documentales** de normalización;
   - las reparaciones T1–T19 del comité 051 §9.2.

3. **Habilitar la SOLICITUD de apertura de S2** —no la apertura— mediante una puerta de
   **dos niveles**.

   **Nivel 1 — condiciones técnicas.** Cuando se cumplan **simultáneamente**:

   ```text
   GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
   roadmap normalization            = consistent
   working tree                     = clean after preservation commits
   ```

   el estado pasa a ser, y sólo a ser:

   ```text
   S2_READINESS = READY_FOR_PI_DECISION
   S2           = NOT_OPEN
   ```

   **Nivel 2 — decisión del PI.** S2 se abre únicamente mediante una decisión explícita
   y posterior del PI, registrada como

   ```text
   DECISION_S2 = AUTORIZADO      <-- forma que tomaria esa decision futura.
                                     NO esta fijada en esta nota. Ver §10.
   ```

   > Las condiciones técnicas son necesarias para **solicitar** la apertura de S2,
   > no suficientes para **autorizarla**. La transición S1 -> S2 requiere una
   > decisión explícita del PI después de preservar S1 y corregir la
   > normalización contractual.

   Mientras `DECISION_S2` siga pendiente, **ninguna lectura de esta nota autoriza S2**,
   se cumplan o no las tres condiciones del Nivel 1. Un agente o lector que encuentre
   las tres condiciones satisfechas debe detenerse y pedir la decisión, nunca proceder.

   Si el PI autoriza S2, queda limitada al primer teorema completo:

   ```text
   geometry 1+1 -> copula tangent -> symmetric rank score
                -> existing combinatorial theorem
                -> Fisher retention for Pi_N -> [P_Pi_N]
   ```

4. **Auditoría bibliográfica y de prioridad** del resultado geométrico, **sólo después**
   de que exista un teorema S2 estable. Hasta entonces no se emite ninguna afirmación de
   prioridad.

## 5bis. Resolución del gate de WP5

Existe una decisión previa según la cual el trabajo en `1+1D` es puramente instrumental
y sólo debe continuarse si sirve demostrablemente al objetivo `3+1D`. R4 pide que ese
gate **ceda aquí**, y la cesión queda otorgada con alcance estrecho y motivos explícitos.

**Por qué NO se autoriza R4:**

- **no** porque se haya demostrado transferencia a `3+1`; no se ha demostrado ninguna;
- **no** como reanudación, ni total ni parcial, del programa de reconstrucción de
  horizonte.

**Por qué SÍ se autoriza:**

- como **rama teórica autónoma**, deductiva, sin consumo de semillas, sin simulación y
  con el sello intacto;
- porque desarrolla hasta una formulación geométrica acotada en `d=2` el resultado
  Fisher/combinatorio **ya obtenido**, en lugar de abrir un frente nuevo.

**Alcance exacto de la cesión:**

- alcanza únicamente **S1** y cualquier **S2 que el PI autorice explícitamente después**
  por la puerta de dos niveles de §5.3;
- **no** autoriza S4–S7 de la hoja de ruta;
- **no** autoriza ninguna transferencia dimensional.

Debe quedar inequívoco que esa cesión

```text
PROPOSED_GATE_WP5_CESSION = NARROW_YES
    <-- alcance estrecho de este §5bis.
        Token autoritativo fijado en §10.
```

**no** implica

```text
WP5_GENERAL_GATE_REPEALED = SI
```

ni rehabilita ningún objetivo previamente cerrado. El gate general de WP5 sigue vigente
para todo lo que no sea R4.

## 6. Qué NO autoriza R4

Permanece explícitamente fuera:

- generalización simétrica **finite-rank**;
- bilineal genérico `f(u)g(v)` con `f != g` como nuevo teorema Fisher;
- **teorema del sector asimétrico**;
- mejora de la tasa (`rate improvement`);
- cualquier extensión a `2+1` o `3+1`;
- reconstrucción o **localización de horizonte** por esta rama;
- nuevas simulaciones; semillas —**ninguna**—; nuevos observables empíricos;
- claims de universalidad;
- claims de suficiencia respecto a coordenadas continuas completas;
- el vocabulario `first`, `breakthrough`, `novelty certified` o equivalentes.

Sigue vigente además todo lo listado en §5 de R3 y §3 de la nota del 31 de julio.

## 7. Rebaja explícita de la lectura de novedad

La clasificación

```text
P psi = lambda f (x) f   <=>   psi = alpha(u) + beta(v) + lambda f(u) f(v)
```

**no debe presentarse como matemática nueva en sí misma.** Su núcleo algebraico es una
instancia de la descomposición clásica **ANOVA / Hoeffding**, que este mismo repositorio
ya usa bajo ese nombre en
`research_program/work_packages/wp4_ibar_direct_score_derivation.md:305-308`. El
verificador de literatura del comité 051 lo confirmó y no halló fuente primaria dedicada
en `biblioteca/`: es material de manual (Hoeffding 1948; proyección de Hájek).

Lo potencialmente aportado, **si sobrevive a auditoría**, no es `ker P =
{alpha(u)+beta(v)}`, sino la cadena concreta

```text
perturbación geométrica -> tangente de cópula -> score de rangos
                        -> retención Fisher tras Pi_N -> [P_Pi_N]
```

`NOVELTY_CERTIFIED = NO` para todo lo de R4 hasta auditoría independiente.

## 7bis. Tensión declarada — la teoría de cópulas no es todavía un puente al benchmark

- S1 y S2 trabajan sobre un **diamante/caja en coordenadas nulas normalizadas**,
  `[0,1]^2` con `mu_0 = du dv`.
- La maquinaria PIT/cópula **depende** de esa representación rectangular de producto:
  exige que el parche sea una caja de coordenadas nulas.
- El **benchmark histórico** del programa usa un dominio y unas coordenadas
  **distintas**: caja finita en Eddington–Finkelstein `(t*, r)`
  (`docs/preregistration.md:61-62`, `docs/preregistration_001_addendum.md:39-40`).
- **No existe todavía ninguna demostración** de que un teorema S2 pueda transportarse al
  benchmark mediante un cambio de coordenadas o una adaptación de dominio. Nadie lo ha
  intentado.
- Esa ausencia **no invalida** S1 ni un eventual S2, **porque sus enunciados quedan
  restringidos explícitamente a la caja nula** y así deben escribirse en todo texto
  derivado.
- Sí **prohíbe** interpretar S1 o S2 como resultado sobre el benchmark, como
  localización de horizonte, o como puente demostrado a `3+1`.

```text
BENCHMARK_COORDINATE_BRIDGE = OPEN_NOT_REQUIRED_FOR_S2
NO_BENCHMARK_TRANSFER_CLAIM
```

Este puente **no** se intenta resolver bajo R4. Queda registrado como abierto, y como no
requerido para que S1 o S2 sean enunciados válidos dentro de su propio alcance.

## 8. Gate especial por el mismatch de normalización

Queda registrado el incidente descubierto al derivar la cadena. La hoja de ruta actual
mezcla, con **el mismo `lambda`**, un tangente de cópula escrito como

```text
h_psi = lambda f (x) f            (§2.2, Convención A)
```

con un score escrito como

```text
S_N = 2 lambda sum_i a_i a_{pi(i)}    (§2.3, Convención B)
```

Ninguna de las dos fórmulas es falsa; lo incompatible es usar el mismo símbolo en dos
niveles que difieren por el factor `2`. Hasta corregir esa convención documental:

```text
GEOMETRIC_TANGENT_CLASSIFICATION = OPEN_WITH_EXACT_OBLIGATION
```

**Obligación exacta.** Alinear la definición rank-one de la hoja de ruta §2.2 con la
convención demostrada,

```text
P psi = psi - psi_U - psi_V + bar psi = lambda f (x) f,
h_psi = 2 lambda f (x) f,
```

de modo que el score

```text
S_N(pi) = 2 lambda sum_i a_{i,N} a_{pi(i),N}
```

use el mismo `lambda` en todas las etapas.

**Lectura obligatoria de este token, para que nadie la malinterprete después.** `OPEN`
aquí **no** significa que la demostración tenga un hueco. La cadena matemática puede
estar completa y el token de fase permanecer legítimamente cerrado. La obligación
pendiente es de **coherencia contractual** entre la definición preregistrada y la
convención demostrada, no de matemática. Esa separación es precisamente la respuesta al
problema de auto-satisfacción del criterio que detectó el comité 051 §8.3: un documento
no puede darse por aprobado contra un criterio que él mismo redefine en el acto.

Secuencia de certificación vinculante:

```text
R4 firmada
  -> WP como OPEN_WITH_EXACT_OBLIGATION
  -> corrección del roadmap §2.2 (commit propio, fechado antes)
  -> promoción mínima a PROVED
  -> S2
```

`PROVED` no se emite antes de ese orden.

## 9. Test de terminado

R4 está terminado cuando, y sólo cuando:

1. las reparaciones T1–T19 del comité 051 están aplicadas y verificadas por re-diff
   textual (comité 051 §9.4);
2. la Convención B está enmendada en la hoja de ruta §2.2, en commit propio y **fechado
   antes** de cualquier reafirmación de `PROVED`;
3. ninguna afirmación de prioridad aparece sin la auditoría de §5.4, y ésta incorpora de
   partida el hallazgo ANOVA / Hoeffding de §7;
4. el alcance —diamante plano de Minkowski, sólo `d=2`, sólo sector rank-one simétrico,
   no es reconstrucción, no es horizonte— está reproducido literalmente en cualquier
   texto derivado.

## 10. Firma

**Firmada.** `R4 AUTORIZADO` por decisión explícita del PI.

```text
ESTADO_FIRMA: FIRMADA — R4 AUTORIZADO
FIRMADA_POR: Ignacio Martin (PI)
FECHA_FIRMA: 2026-08-28
AUTORISED_SCOPE: R4 (lista cerrada de §5)

DECISION_R4: AUTORIZADO
DECISION_RATIFICACION_RETROACTIVA: SI
                                   (236b1824, 4bcbfc50, 99cec0d8)
GATE_WP5_CEDE_AQUI = SI
                     (alcance estrecho de §5bis;
                      el gate general permanece vigente fuera de R4)
DECISION_S1: AUTORIZADO EL CIERRE
             (fase: OPEN_WITH_EXACT_OBLIGATION, ver §8)
DECISION_S2: PENDING_FUTURE_PI_DECISION

NOT_AUTORIZADO: todo lo listado en §6
CAJAS_DE_TIEMPO: sin cambio (conjunto -> 2026-09-11)
```

`DECISION_S2 = AUTORIZADO` **no puede fijarse en esta nota**. Requiere una decisión
posterior del PI, tomada después de preservar S1 y de corregir la normalización
contractual, por la puerta de dos niveles de §5.3.
