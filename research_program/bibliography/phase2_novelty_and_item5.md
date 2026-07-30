# Fase 2 — Bibliografía adversarial + cierre ítem 5

> **STATUS: PHASE_2_EXTERNAL_RESPONSES_ADJUDICATED /
> ITEM_5_DISCHARGED_BOTH_TIERS / NOT_A_NOVELTY_CERTIFICATE /
> DOES_NOT_TOUCH_SEAL.**
>
> Ejecuta los pasos 2.1–2.4 de `tarea_grok_2.md` §1.3 / hoja de ruta Fase 2, tras
> manuscript interno de límites (`docs/manuscript_limits_draft.md`, PI review OK).
>
> FECHA DE APERTURA: 2026-07-28 · HEAD: `66cec59`
> Sello: `thresholds.py sha256 = 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (intacto)

**Qué descarga y qué no**

| Entrega | ¿Descarga ítem 5? |
|---|---|
| 2.1 Anclas verificadas en paquete adversarial | No |
| 2.2 Log de búsqueda math.ST/PR + literaturas ampliadas | No |
| 2.3 Plan de envío a lectores Tier A/B | No (plan ≠ envío) |
| 2.4 Política si un lector hunde N1 | No (regla condicional) |
| **Envío real + respuesta de lector humano** | **Sí** — cumplido en ambos tiers; ver §3.4–§3.6 |

Los dos contactos y las dos respuestas se gestionaron fuera del árbol trackeado. Ningún nombre,
dirección de correo ni texto íntegro de respuesta se almacena en este repo; el registro público
queda limitado a tier, fecha de recepción, huella SHA-256, adjudicación y acciones.

---

## 0. Adjudicación N1–N5 (ya firmada en Fase 0; aquí es input)

| Claim | Estatus de programa (Fase 0) | Implicación para novedad pública |
|---|---|---|
| **N1** / Thm 3.8 | Mantener **acotado** (instanciación) | Único claim que aún pide peinado ST/PR + Tier B |
| **N2** / Thm 3.1 | **Lema**; no contribución de novedad | Citar anclas Order+Number; no “resultado nuevo” |
| **N3** | Remark de diseño | No contribución |
| **N4** | Corolario dimensional | No contribución |
| **N5** | **Retirado** como contribución | Solo disciplina DPI en notación |

El manuscript de límites ya refleja esto. Fase 2 no reabre N2/N4/N5 como medallas.

---

## 1. Paso 2.1 — Anclas verificadas (prioridad adversarial filtrada)

**Procedencia.** Pista vía LLM (sesión Grok / `tarea_grok_1.md`), **re-verificada a fuente
primaria** en el filtro documentado en `tarea_grok_2.md` §1.1 (operador).  
Marca: `LLM_LEAD_HUMAN_VERIFIED`.

Incorporadas también en
`external_adversarial_review_package_n1_n5.md` §7 (tabla ampliada) y, para candidatos,
en `external_reader_candidates_n1_n5.md` §3.1.

| # | Cita | Localización verificada | Afecta | Uso en manuscript |
|---|---|---|---|---|
| V1 | Dowker & Zalel, arXiv:1703.07556 | §1.1: «lacking only information about local physical scale»; «Number plus Order equals Geometry, in R. Sorkin's slogan» | N2 | Background Thm 3.1 |
| V2 | Madsen, arXiv:2607.05840 | Intro: «order alone is famously insufficient…» | N2 | Background Thm 3.1 |
| V3 | Braun, arXiv:2507.01907 | §1.1; §3.3 Order / conformal; §3.4 Number / isometry | N2 | Background; contrast labeled vs unlabeled |
| V4 | HKMM, J. Math. Phys. **17**, 174 (1976) | Resultado clásico (vía refs de Braun) | N2 | Continuum conformal |
| V5 | Malament, J. Math. Phys. **18**, 1399 (1977) | Resultado clásico (vía refs de Braun) | N2 | Continuum causal→topology/conformal |
| V6 | Bombelli 1987 PhD | `biblioteca/derived-md/Bombelli_1987_PhD.md:500-502`: “up to a global scale factor”; Zeeman = Poincaré + dilataciones | N2 | Precursor continuo directo de órbita de escala |
| V7 | Boguñá–Krioukov, PRD **110**, 024008 (2024) | Escala \(\rho^{-1/(d+1)}\); tasas constructivas | N1 (anverso) | §6 complementary rates |
| V8 | Müller, arXiv:2503.01719 | Teoremas 2–3; Thm 3: `E >= 1−4πK²T^(−1/n)` en cilindros planos | N2 / vecino N1 | Precursor cualitativo **y cuantitativo**; no QMD/minimax local |
| V9 | Tsybakov, *Introduction to Nonparametric Estimation* (2009) | Método dos puntos (textbook; PDF local) | N1 técnica | Explicit non-novelty of method |

**Efecto sobre N2.** La vía de refutación del paquete §4.2(7) («cualquier enunciado de la
órbita de dilatación») queda **parcialmente satisfecha en el continuo** (V4–V6) y en el
**eslogan CST** (V1–V3). El TV=0 exacto a \(N=n\) del Teorema A / manuscript Thm 3.1 **sigue
siendo formalización del canal de sprinkling**, no descubrimiento físico — alineado con
degradación a lema.

**Efecto sobre N4.** El argumento dimensional \(V\cdot I\) (deflación del paquete) se registra
como `DIMENSIONAL_ANALYSIS_BACKGROUND`; no se busca “prioridad de κ” como teorema.

**Efecto sobre N1.** Ninguna de V1–V9 es el suelo minimax order-only para el parámetro geométrico
de la familia Schwarzschild en poset no etiquetado. N1 **no hundido**, pero V8 impide afirmar que
no existe un precursor cuantitativo para familias geométricas continuas.

---

## 2. Paso 2.2 — Log de búsqueda math.ST / math.PR (hueco N1)

### 2.1 Objetivo

Buscar **prioridad de la instanciación** (o un corolario inmediato) de un suelo tipo dos puntos /
Fisher para:

- parámetro geométrico / de localización / de forma;
- datos de proceso puntual de Poisson (o poset / orden inducido);
- en particular canal “solo estructura de orden / rangos / cópula”.

**No** se busca redescubrir Le Cam/Tsybakov (ya textbook).

### 2.2 Consultas ejecutadas (2026-07-28)

Herramienta: búsqueda web / arXiv abstracts (misma clase de medio que Paso D; **no** MathSciNet
completo). Log reproducible por reformulación:

| ID | Query (resumen) | Hits relevantes (abstract-level) | ¿Prior de N1/Thm 3.8? |
|---|---|---|---|
| Q1 | `two-point method OR "Le Cam" Poisson process location parameter estimation lower bound` site:arxiv.org | Polyanskiy–Wu dualizing Le Cam (funcionales); Ray–Schmidt-Hieber Le Cam distance density/Poisson/Gaussian; change-point Poisson; semiparametric spatial PP efficiency | **No** — métodos generales o targets distintos (intensidad, change-point), no orden causal no etiquetado Schwarzschild |
| Q2 | `minimax estimation intensity function Poisson process geometric parameter` site:arxiv.org | Literatura de estimación de intensidad / semiparamétrica espacial | **No** — no poset order-only |
| Q3 | `Fisher information copula parameter estimation scale` site:arxiv.org | Inferencia en cópulas / semiparamétrica | **No verificado como sink de κ o de Thm 3.8**; permanece como residual tras Tier B |
| Q4 (Paso D previo) | INSPIRE `causal set` ∧ {Fisher, minimax, Le Cam, …} | Cero antecedentes CST genuinos (falsos positivos holografía) | **No** |

### 2.3 Lectura del log

```text
PHASE2_ST_PR_SWEEP = EXECUTED_ABSTRACT_LEVEL / NO_N1_SINK_FOUND / NOVELTY_NOT_CERTIFIED
```

- Confirma el hueco: hay abundante **técnica** de cotas inferiores para procesos de Poisson e
  intensidades; **no** se encontró (a nivel abstract) un paper que enuncie el suelo order-only
  del canal poset no etiquetado para el parámetro de la familia diamante EF / horizonte 1+1.
- Un paper de 1990–2015 no indexado en estas consultas **puede existir**. Tier B cubrió el flanco
  procedimental sin hallar un sink; el riesgo bibliográfico residual permanece.
- **Cero hits ≠ novedad.** Misma regla que Paso D.

### 2.4 Literaturas ampliadas (para peinado / lectores)

Añadidas a `external_reader_candidates_n1_n5.md` §3.1:

| Subcampo | Términos de búsqueda | Por qué |
|---|---|---|
| Minimax + PPP | `two-point method Poisson process`, `Hellinger affinity point process`, `minimax intensity estimation` | Hueco N1 |
| Geometric inference | `minimax manifold estimation`, `support estimation lower bound` | Localización de forma |
| Random geometric graphs / latent space | `unlabeled geometric graph lower bound`, `latent position DAG`; pista Bubeck–Ding–Eldan–Rácz `READER_LEAD_UNVERIFIED` | Hueco residual N1 |
| Shape theory | Kendall; Dryden–Mardia; `Procrustes Fisher information` | Escala vs forma (N2/N4 conceptual) |
| Cópula / ranks | Joe; Nelsen; `semiparametric efficiency copula`, `rank statistics information` | Order-only ≈ información de rango |
| Info–computation gaps | Abbe; Decelle–Krzakala–Moore–Zdeborová | Disciplina ex-N5 (no prior del mapa CST) |

### 2.5 Papers “vecinos de método” (no sinks; para el revisor ST)

Si un lector Tier B pide “qué ya conocéis en ST”, la lista mínima honestas es:

1. Tsybakov (2009) — dos puntos (textbook).  
2. Ray & Schmidt-Hieber, arXiv:1608.01824 — distancias de Le Cam entre experimentos
   densidad / Poisson / ruido gaussiano.  
3. Polyanskiy & Wu, arXiv:1902.05616 — dualización del método de Le Cam para funcionales.  
4. Birgé, model selection for Poisson processes (clásico).  
5. Trauthwein–Yukich, arXiv:2605.23292 — localización en espacio de Poisson (ya Tier B1 del
   proyecto; herramientas, no el teorema N1).

Ninguno se marca como contenedor de Thm 3.8 sin lectura a texto completo por un humano.

---

## 3. Paso 2.3 — Protocolo de envío ítem 5 (fijado antes del contacto)

### 3.1 Objetivo del ítem 5 (letra + espíritu)

| | |
|---|---|
| **Letra** (`wp5_paso_d` §6) | Lector competente en **causal set theory**, sin implicación en el proyecto |
| **Espíritu** (paquete §7 + candidatos) | Cubrir también el hueco ST/PR de **N1** |

**Resolución de gobernanza (Fase 2):**

```text
ITEM_5_PROTOCOL =
  ENVÍO_MÍNIMO: 1× Tier A  (cumple la letra)
  ENVÍO_RECOMENDADO: 1× Tier A + 1× Tier B  (cumple letra + espíritu para N1)
  HASTA_RESPUESTA: N1 wording = hedge only (ya en manuscript §1.6 / §6.5)

  DESCARGA DEL ÍTEM 5 (resuelto por el PI, 2026-07-28):
    SALIDA_(a) — exige respuesta registrada de AMBOS tiers.
    Ver external_reader_candidates_n1_n5.md §4.1 para la regla completa.
    Un solo tier, DECLINED o NO_REPLY ⇒ ítem 5 SIGUE ABIERTO.
```

Con la salida (a) fijada, «envío recomendado» y «envío exigido para descargar» coinciden: el
`ENVÍO_MÍNIMO` de 1× Tier A cumple la letra del ítem pero ya **no** basta para marcarlo descargado.

Un solo Tier A **descarga la letra** del ítem 5 pero **no** certifica N1 frente a math.ST.
El manuscript interno puede vivir con hedge; **arXiv con “first lower bound…”** exige al menos
Tier B o un peinado ST documentado más fuerte que Q1–Q4.

### 3.2 Paquete a enviar (contenido, no personas)

1. Carta del paquete adversarial §1 (pedir **refutación**, no validación).  
2. Fichas N1–N5 del paquete §4 **con adjudicación Fase 0 pegada arriba** (N2 lema, N5 fuera, …).  
3. Tabla de anclas V1–V9 (este doc §1).  
4. Extracto manuscript: abstract + §3 (Thm 3.1, 3.2, 3.8) + claim cards.  
5. Formulario §8.2 del paquete.  
6. **No** enviar: umbrales sellados innecesarios; seeds; código de validación; opiniones sobre
   personas.

### 3.3 Candidatos (solo por obra pública; sin email en repo)

Ver `external_reader_candidates_n1_n5.md`:

| Tier | Ejemplos por **obra** (no ranking de personas) | Pregunta principal |
|---|---|---|
| A | Autores de Braun 2507.01907; Müller 2503.01719; Madsen 2607.05840; EGS 2605.06813; línea Dowker/Surya | N2 lema ¿fiel?; Müller contrast ¿fiel?; ¿sobre-afirmación? |
| B | Autores de Trauthwein–Yukich 2605.23292; comunidad minimax PPP (a localizar por citas de Tsybakov en PP) | ¿N1 ya es corolario en ST/PR? |

**Regla ética del repo.** Este documento **no** elige a quién escribir ni almacena correos.
La elección táctica la hace el PI **fuera** del árbol git.

### 3.4 Registro de envío y respuesta (PI)

```text
[x] Contacto Tier A realizado fuera del repo
[x] Contacto Tier B realizado fuera del repo
[x] Respuesta Tier A recibida y adjudicada
[x] Respuesta Tier B recibida y adjudicada

SEND_DATE_TIER_A: NOT_RECORDED
SEND_DATE_TIER_B: NOT_RECORDED
RESPONSE_RECEIVED_TIER_A: 2026-07-28
RESPONSE_RECEIVED_TIER_B: 2026-07-28

LOCAL_ONLY_RESPONSE_A_SHA256:
  c3aa2a1088ef3e39c0ede116aeab724c7fc88c53495a107517307dda216a25c8
LOCAL_ONLY_RESPONSE_B_SHA256:
  6a337c1b7a7c06c9f21da81e27937e11dc047c8ba3e4f7f7352657273a6fea46

ITEM_5_STATUS: DISCHARGED_BOTH_TIERS_2026-07-28
```

Las fechas de envío no se infieren de la fecha de creación de los PDF. Las huellas identifican
los dos artefactos locales ignorados por git; no convierten las respuestas en evidencia científica
ni permiten reconstruir identidad o contenido desde el repositorio público.

### 3.5 Plazo sugerido

- T0: envío.  
- T0+21 días: si no hay respuesta, un recordatorio.  
- T0+45 días sin respuesta: marcar `NO_REPLY`; ítem 5 **no** descargado; manuscript sigue con
  hedge; no afirmar novedad absoluta de N1.

### 3.6 Adjudicación conjunta de las dos respuestas

**Resultado de protocolo: escenario (B), no (A) ni (C).**

```text
TIER_A:
  N2 = KNOWN_BACKGROUND / KEEP_AS_INSTRUMENTAL_LEMMA
  N1 = PARTIAL_OVERLAP_WITH_MUELLER_THEOREM_3 / NEEDS_BOUNDED_REFORMULATION
  CORRECTNESS_INCIDENT_OUTSIDE_N1_N5 = THEOREM_3_2_CAUSAL_CONVEXITY_GAP

TIER_B:
  N1 = APPARENTLY_DISTINCT_AS_FAMILY_SPECIFIC_INSTANTIATION
  N4 = MODEL_SPECIFIC_SCALING_COROLLARY / NOT_AN_INDEPENDENT_RESULT
  METHOD = STANDARD_TWO_POINT_QMD_HELLINGER_DATA_PROCESSING
  REQUIRED_CLARIFICATION = PARAMETER_INDEPENDENT_POSET_MAP
  GENERAL_POISSON_FUNCTIONAL_SINK = NOT_FOUND

JOINT:
  PRIOR_FOR_N1 = NOT_FOUND_BY_EITHER_READER
  NOVELTY_CERTIFIED = NO
  ABSOLUTE_PRIORITY_LANGUAGE = FORBIDDEN
  ITEM_5_DISCHARGED = YES
```

La respuesta Tier A confirma que N2 está bien tratado como formalización finita de un principio
conocido, pero exige tres concesiones: citar de forma directa el pasaje de Bombelli sobre escala
global/dilataciones; reconocer el Teorema 3 de Müller como precursor cuantitativo más cercano; y no
describir \(\tau\) como un detector de horizonte. Además detecta un hueco matemático independiente
de prioridad: la prueba teleológica de Thm 3.2 necesita que \(P\) sea causalmente convexo (o que el
canal use solo curvas internas a \(P\)).

La respuesta Tier B valida la cadena de Thm 3.8 con una aclaración obligatoria: en coordenadas de
cópula todos los miembros viven en el cuadrado unidad con orden producto fijo; por eso el mapa
muestra→poset es independiente de \(\tau\). También confirma que Trauthwein–Yukich no contiene el
suelo: su “localization” es localización de *scores* para aproximación normal, no estimación minimax
de un parámetro de posición.

**Acciones vinculadas a esta adjudicación:**

| ID | Acción | Estado |
|---|---|---|
| R-A1 | Acotar la frase de ceguera absoluta a la órbita de dilatación | `APLICADA` |
| R-A2 | Hacer explícita la causal convexidad en Thm 3.2 | `APLICADA` |
| R-A3 | Añadir Müller Thm 3 como precursor cuantitativo y retirar “no hay tasa” | `APLICADA` |
| R-A4 | Alinear N1 con “parámetro geométrico continuo”, no “horizon detector” | `APLICADA` |
| R-A5 | Citar Bombelli directamente; HKMM/Malament solo como precursores de la dirección difícil | `APLICADA` |
| R-B1 | Explicar por qué el mapa a poset es independiente de \(\tau\) | `APLICADA` |
| R-B2 | Mantener N1 como instanciación acotada y la maquinaria como `[BACKGROUND]` | `APLICADA` |
| R-B3 | Registrar grafos geométricos/espacio latente como hueco bibliográfico residual | `APLICADA` |

---

## 4. Paso 2.4 — Política si un lector hunde un claim

| Evento | Acción obligatoria en el repo |
|---|---|
| Prior real de **N1**/Thm 3.8 | Retirar o reescribir como corolario; quitar cualquier hedge de “to our knowledge” que sugiera primacía; actualizar manuscript §3 y §6 |
| Prior de **N2** más fuerte que lema | Ya es lema; incorporar cita y acortar Thm 3.1 a “standard + TV calculation” |
| Prior de **N3/N4/N5** | Ya no son contribuciones; solo ajustar background |
| “APPARENTLY_DISTINCT” en N1 de Tier A **solo** | **No** certifica novedad; no cambiar hedge hasta Tier B o peinado ST fuerte |
| Refutación de corrección matemática (no prioridad) | Abrir incidente de prueba; no es ítem 5 |

```text
IF external_reader_cites_prior_for_N1:
    novelty_claim_N1 := RETRACTED_OR_REDUCED
    manuscript := patch within 7 days of verified citation
```

---

## 5. Consecuencias para el manuscript de límites

| Pieza | Estado tras Fase 2 (docs) |
|---|---|
| Thm 3.1 | Background V1–V6 alineado; Bombelli citado como precursor directo de escala global/dilataciones |
| Thm 3.2 | Hipótesis causal-convexa añadida tras objeción Tier A |
| Thm 3.8 | Ítem 5 descargado; se mantiene wording comparativo y acotado por el solapamiento con Müller Thm 3 y el hueco residual ST |
| N2/N4/N5 | Sin medalla — sin cambio |
| arXiv | Lenguaje de primacía absoluta **prohibido**; la descarga del ítem 5 no equivale a certificado de novedad |

La salida correcta es el escenario (B) del paquete §9: el suelo se presenta como instanciación
explícita sobre una familia lorentziana regular; QMD/Hellinger/Le Cam/data processing se declaran
maquinaria estándar.

---

## 6. Checklist Fase 2

```text
[x] 2.1 Anclas V1–V9 documentadas + tabla en paquete adversarial §7
[x] 2.2 Log Q1–Q4 + literaturas ampliadas en candidatos §3.1
[x] 2.3 Protocolo ítem 5 fijado antes de los envíos
[x] 2.4 Política de hundimiento de N1
[x] Envío real Tier A (fecha no consignada)
[x] Envío real Tier B (fecha no consignada)
[x] Respuestas de ambos tiers registradas y adjudicadas
[x] Parche de reformulación/corrección aplicado al paquete, anexo y manuscript

PHASE_2_DOC_COMPLETE: 2026-07-28
ITEM_5_STATUS: DISCHARGED_BOTH_TIERS_2026-07-28
NEXT: verificación mecánica del parche; luego revisión editorial del manuscript sin lenguaje de primacía
```

---

## 7. Frase de gobierno

> *Fase 2 peinó, recibió dos respuestas y corrigió; no certificó novedad. N1 sobrevive como
> instanciación acotada, con maquinaria estándar y solapamientos declarados.*
