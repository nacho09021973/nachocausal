# Fase 2 — Bibliografía adversarial + plan ítem 5

> **STATUS: PHASE_2_OPENED / SEARCH_AND_PLANNING / NO_EXTERNAL_CONTACT_MADE /
> ITEM_5_STILL_PENDING / NOT_A_NOVELTY_CERTIFICATE / DOES_NOT_TOUCH_SEAL.**
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
| **Envío real + respuesta de lector humano** | **Sí** — único descargo del ítem 5 |

Ningún correo se ha enviado. Ninguna dirección de correo se almacena en este repo.

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
| V6 | Bombelli 1987 PhD | Zeeman: isomorfismos causales Minkowski = Poincaré + dilataciones; «up to a global scale factor» (`biblioteca/derived-md/`) | N2 | Precursor continuo de órbita de escala |
| V7 | Boguñá–Krioukov, PRD **110**, 024008 (2024) | Escala \(\rho^{-1/(d+1)}\); tasas constructivas | N1 (anverso) | §6 complementary rates |
| V8 | Müller, arXiv:2503.01719 | Teorema 2 | N2 / vecino N1 | Pariente cualitativo |
| V9 | Tsybakov, *Introduction to Nonparametric Estimation* (2009) | Método dos puntos (textbook; PDF local) | N1 técnica | Explicit non-novelty of method |

**Efecto sobre N2.** La vía de refutación del paquete §4.2(7) («cualquier enunciado de la
órbita de dilatación») queda **parcialmente satisfecha en el continuo** (V4–V6) y en el
**eslogan CST** (V1–V3). El TV=0 exacto a \(N=n\) del Teorema A / manuscript Thm 3.1 **sigue
siendo formalización del canal de sprinkling**, no descubrimiento físico — alineado con
degradación a lema.

**Efecto sobre N4.** El argumento dimensional \(V\cdot I\) (deflación del paquete) se registra
como `DIMENSIONAL_ANALYSIS_BACKGROUND`; no se busca “prioridad de κ” como teorema.

**Efecto sobre N1.** Ninguna de V1–V9 es un suelo minimax order-only para un parámetro de
posición de familia Schwarzschild en poset no etiquetado. N1 **no hundido** por este lote.

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
| Q3 | `Fisher information copula parameter estimation scale` site:arxiv.org | Inferencia en cópulas / semiparamétrica | **No verificado como sink de κ o de Thm 3.8**; queda en lista de peinado humano Tier B |
| Q4 (Paso D previo) | INSPIRE `causal set` ∧ {Fisher, minimax, Le Cam, …} | Cero antecedentes CST genuinos (falsos positivos holografía) | **No** |

### 2.3 Lectura del log

```text
PHASE2_ST_PR_SWEEP = EXECUTED_ABSTRACT_LEVEL / NO_N1_SINK_FOUND / NOVELTY_NOT_CERTIFIED
```

- Confirma el hueco: hay abundante **técnica** de cotas inferiores para procesos de Poisson e
  intensidades; **no** se encontró (a nivel abstract) un paper que enuncie el suelo order-only
  del canal poset no etiquetado para el parámetro de la familia diamante EF / horizonte 1+1.
- Un paper de 1990–2015 no indexado en estas consultas **puede existir**. Por eso el ítem 5
  Tier B sigue siendo el flanco real de N1.
- **Cero hits ≠ novedad.** Misma regla que Paso D.

### 2.4 Literaturas ampliadas (para peinado / lectores)

Añadidas a `external_reader_candidates_n1_n5.md` §3.1:

| Subcampo | Términos de búsqueda | Por qué |
|---|---|---|
| Minimax + PPP | `two-point method Poisson process`, `Hellinger affinity point process`, `minimax intensity estimation` | Hueco N1 |
| Geometric inference | `minimax manifold estimation`, `support estimation lower bound` | Localización de forma |
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

## 3. Paso 2.3 — Plan de envío ítem 5 (sin ejecutar contacto)

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
```

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

### 3.4 Checklist de envío (PI)

```text
[ ] Elegir 1× Tier A (letra ítem 5)
[ ] Elegir 0–1× Tier B (recomendado para N1)
[ ] Preparar PDF/zip del paquete §3.2 sin material sellado innecesario
[ ] Redactar email fuera del repo
[ ] Registrar aquí tras envío: FECHA, TIER (A/B), "SENT" sin nombre si se desea privacidad
[ ] Registrar respuesta: REFUTED_CLAIM / NO_PRIOR_KNOWN / DECLINED / NO_REPLY (plazo)

ITEM_5_STATUS: NOT_SENT
```

### 3.5 Plazo sugerido

- T0: envío.  
- T0+21 días: si no hay respuesta, un recordatorio.  
- T0+45 días sin respuesta: marcar `NO_REPLY`; ítem 5 **no** descargado; manuscript sigue con
  hedge; no afirmar novedad absoluta de N1.

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
| Thm 3.1 | Background V1–V6 ya alineado en §6 del draft |
| Thm 3.8 | Hedge ítem 5 **permanece** hasta envío+respuesta o peinado ST superior |
| N2/N4/N5 | Sin medalla — sin cambio |
| arXiv | **Bloqueado** para claims de novedad de N1 hasta política §3.1 |

Parche opcional menor al manuscript (no obligatorio si §6 ya cita): añadir nota al pie en
Thm 3.1 “finite-\(n\) sprinkling formalization of Order+Number; continuum anchors V4–V6”.

---

## 6. Checklist Fase 2

```text
[x] 2.1 Anclas V1–V9 documentadas + tabla en paquete adversarial §7
[x] 2.2 Log Q1–Q4 + literaturas ampliadas en candidatos §3.1
[x] 2.3 Plan ítem 5 (protocolo; NOT_SENT)
[x] 2.4 Política de hundimiento de N1
[ ] Envío real Tier A
[ ] Envío real Tier B (recomendado)
[ ] Respuesta registrada
[ ] Si aplica: parche manuscript por prior

PHASE_2_DOC_COMPLETE: 2026-07-28
ITEM_5_STATUS: NOT_SENT
NEXT: PI ejecuta contacto fuera del repo; o cierra Fase 2 documental y mantiene hedge
```

---

## 7. Frase de gobierno

> *Fase 2 peina y ancla; no certifica novedad. El ítem 5 solo cae cuando un humano ajeno al
> proyecto responde — o cuando una cita verificada hunde el claim sin necesidad de cortesía.*
