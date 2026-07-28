# Fase 0 — Decisión de norte del programa

> **STATUS: PHASE_0_CLOSED / PI_SIGN_OFF_RECORDED /
> NOT_A_PREREGISTRATION / NOT_A_NOVELTY_CERTIFICATE / DOES_NOT_TOUCH_SEAL /
> DOES_NOT_DISCHARGE_ITEM_5 / FASE_1_OPENED.**
>
> **Fase 1 outline:** `research_program/synthesis/phase1_limits_paper_outline.md`
> (abierto 2026-07-28).
>
> Documento de gobernanza. Cierra la Fase 0 de la hoja de ruta
> `tarea_grok_2.md` (raíz del repo). No ejecuta código, no consume semillas, no
> modifica `thresholds.py`, no autoriza estimadores nuevos ni kill tests de
> localizadores de horizonte.
>
> FECHA DE APERTURA: 2026-07-28 · HEAD al abrir: `e9744d8`
> FECHA DE CIERRE (PI_SIGN_OFF): 2026-07-28

**Precedencia:** mientras este documento esté en vigor con `PI_SIGN_OFF`, gobierna
sobre el norte implícito de
`docs/plan_operativo_15_julio_2026.md` y de
`research_program/work_packages/next_observable_candidate_matrix.md` en todo lo
relativo a **localización / reconstrucción de horizonte Schwarzschild 3+1
order-only**. No reinterpreta resultados PR sellados ni cotas ya probadas.

---

## 1. Qué es la Fase 0

Tres entregas, y solo esas:

| ID | Entrega | Criterio de hecho |
|---|---|---|
| **0.1** | Confirmar o enmendar **R1–R3** y la adjudicación **N1–N5** | Checklist §7 firmado por el PI |
| **0.2** | Marcar el norte reconstructor horizonte 3+1 order-only como abandonado en la matriz de candidatos | Banner operativo en la matriz (§2 de este doc + edición de la matriz) |
| **0.3** | Fijar vocabulario `EMPIRICAL_FAILURE_OF_CLASS_L` vs `PROVED_NON_IDENTIFIABILITY` | §3 de este doc + ancla en taxonomía |

**Prohibido en Fase 0:** código nuevo de estimadores, semillas de validación, tocar el sello, abrir PR de localizador, convocar comité para “un candidato más” de horizonte.

---

## 2. Decisiones R1–R3 (texto operativo)

### R1 — Abandono del norte reconstructor

```text
ABANDONED_AS_PROGRAM_NORTH:
  localizar o reconstruir estructura de horizonte de Schwarzschild 3+1
  (evento global, región atrapada, codim-2, trapping, o proxy de los mismos)
  mediante un nuevo observable order-only en la línea de la matriz post-PR008
  (ladders, cuts, molecules, retuning de profundidad, Page–Shoom-like, etc.).
```

**Motivo (no es la prueba del no-go):** conjunción fallida target+canal+ambición
dimensional (ledger C1–C6; matriz de supervivencia `tau = DOES_NOT_TRANSFER`;
OP-1.2 ceguera de masa a `fixed_n`; claim_grammar teleología del horizonte global).

**Qué sigue permitido bajo R1:**

- redactar el paper de límites (Fase 1);
- trabajo teórico de no-go con pares testigo / TV / Fisher sobre targets **nombrados**;
- abrir más adelante un **programa nuevo** (Order+Number, clasificación, etc.) con
  claim grammar propio — no como “continuación” del reconstructor.

**Qué queda prohibido sin nuevo `PI_SIGN_OFF` que revoque R1:**

- kill tests o pre-registros de nuevos localizadores de horizonte order-only;
- abstracts del tipo “towards reconstructing BH horizons from causal sets” sin la
  negación explícita del paquete finito order-only.

### R2 — Producto del ciclo actual

```text
PRODUCTO_DEL_CICLO = paper / manuscript de LÍMITES DE RECUPERABILIDAD
  (cegueras demostradas + ledger de negativos tipados + positivo acotado 1+1),
  NO un reconstructor de horizonte 3+1.
```

### R3 — Regla epistémica vinculante

```text
Ledger C1–C6  →  etiqueta EMPIRICAL_FAILURE_OF_CLASS_L  (o de lista L)
NO se cita como prueba de  PROVED_NON_IDENTIFIABILITY.

Imposibilidad / no-go solo con:
  igualdad o contigüidad de leyes (TV, Hellinger, Fisher, dos puntos),
  o no-funcionalidad del target por definición (horizonte global / patch).
```

---

## 3. Vocabulario vinculante (entrega 0.3)

| Etiqueta | Significado | Forma canónica | Ejemplo en el repo |
|---|---|---|---|
| `EMPIRICAL_FAILURE_OF_CLASS_L` | Toda regla en una lista o clase **nombrada** `L` falla bajo un protocolo fijado | `∀ T ∈ L: falla(T \| protocolo P)` | C1–C6 bajo sus terminales; kill tests fallidos |
| `PROVED_NON_IDENTIFIABILITY` | **Ningún** estimador medible del canal alcanza riesgo arbitrariamente bajo | Existe par \(g_0,g_1\) con \(T(g_0)\neq T(g_1)\) y \(\mathrm{Law}_K(g_0)=\mathrm{Law}_K(g_1)\) (o TV≤ε ⇒ suelo minimax) | Teorema A / OP-1.2 (masa a `N=n`); horizonte global vs patch (`claim_grammar` §3); suelo Fisher N1 en familia regular 1+1 |

**Prohibido:**

- llamar “no-go” o “indeterminación demostrada” a un terminal del ledger sin par testigo / cota de leyes;
- llamar “solo no encontramos el estimador” a un caso con `TV≡0` en el target.

**Capas ya existentes** (no se reemplazan; se etiquetan):

| Capa taxonomía (`identifiability_taxonomy.md`) | Etiqueta Fase 0 |
|---|---|
| 4.1 Límite del estimador | caso particular de `EMPIRICAL_FAILURE_OF_CLASS_L` con `\|L\|=1` |
| 4.2 Límite de familia | `EMPIRICAL_FAILURE_OF_CLASS_L` con `L=F` (si F es por protocolo, no por TV) **o** `PROVED_NON_IDENTIFIABILITY` si hay cota sobre todas las medibles de F |
| 4.3 Límite intrínseco del orden | solo `PROVED_NON_IDENTIFIABILITY` |

Ancla adicional: `research_program/taxonomy/identifiability_taxonomy.md` §4.4 (añadido con esta Fase 0).

---

## 4. Adjudicación N1–N5 (aceptada en PI_SIGN_OFF)

> Estado: **ACEPTADA** en §7 (2026-07-28). Sin enmiendas.
> No descarga el ítem 5 del Paso D (lector humano independiente).

| Claim | Adjudicación | Wording permitido en manuscript |
|---|---|---|
| **N1** | Mantener **acotado** (instanciación; técnica de libro) | Suelo de localización en familia EF 1+1 con QMD probado; no “nuevo método de Le Cam” |
| **N2** | **Degradar a lema** instrumental | Formalización exacta de Order+Number a `N=n`; citas Dowker–Zalel, Madsen, Braun, HKMM/Malament, Zeeman/Bombelli |
| **N3** | **Remark** de diseño de familia | Kruskal fijo ⇒ degeneración; no contribución numerada |
| **N4** | **Debilitar** a corolario dimensional de N2 + reparametrización | `κ=V·I` adimensional; no teorema de novedad |
| **N5** | **Retirar** como contribución | DPI + disciplina “ciego ⇏ visible” en 2–4 frases de notación; sin N-número |

**Teoremas del paper de límites (mapa a R2), independientes del branding N\*:**

| ID | Contenido | Etiqueta |
|---|---|---|
| (T1) | Ceguera exacta de masa/escala a `N=n` (1+1 y 3+1) | `PROVED_NON_IDENTIFIABILITY` |
| (T2) | Horizonte de eventos global no es funcional del patch finito | `PROVED_NON_IDENTIFIABILITY` (definición / teleología) |
| (T3) | Suelo \(\sim n^{-1/2}\) en familia regular 1+1 | `PROVED_NON_IDENTIFIABILITY` (tasa; capa minimax) |
| Ledger | C1–C6 | `EMPIRICAL_FAILURE_OF_CLASS_L` |

---

## 5. Entrega 0.2 — Matriz de candidatos

Editado en
`research_program/work_packages/next_observable_candidate_matrix.md`:

- banner superior `PROGRAM_NORTH = ABANDONED_AS_PROGRAM_NORTH` (horizonte SW 3+1 order-only);
- los candidatos A–C de la matriz **no** se reabren como ruta a ese norte;
- decisión 046 y terminales previos **no** se reescriben; solo se les antepone la prohibición de programa.

La matriz puede seguir existiendo como **archivo histórico de triage** y como
referencia de *por qué* se abandonó el norte. No autoriza ejecución.

---

## 6. Fases siguientes

1. **Fase 1 — ABIERTA (2026-07-28):** outline autoritativo en
   `phase1_limits_paper_outline.md`. Siguiente entrega de redacción: draft §3
   (T1)–(T3) only.
2. **Fase 2** — biblio N1–N5 + ítem 5 (paralelo; no bloquea redactar límites sin claim de novedad de N1).  
3. **Fase 3** — preferencia: **B2** después del manuscript; no B4 prematuro; B1 solo como programa nuevo.

Detalle: `tarea_grok_2.md` §4–§5.

---

## 7. Checklist PI (Fase 0) — FIRMADO

Sesión de firma: 2026-07-28. El PI acepta el texto de R1–R3 y la tabla N1–N5
**sin enmiendas**, tras la deliberación registrada en `tarea_grok_2.md` y la
apertura explícita de Fase 0 en conversación de trabajo. Preferencia Fase 3:
**B2** (pares testigo / identificabilidad) después del paper de límites; no B4
prematuro.

```text
[x] R1 — ABANDONED_AS_PROGRAM_NORTH (horizonte SW 3+1 order-only vía nuevos localizadores)
    Enmienda: ninguna

[x] R2 — Producto del ciclo = paper de límites de recuperabilidad
    Enmienda: ninguna

[x] R3 — Ledger = EMPIRICAL_FAILURE_OF_CLASS_L; no-go solo con PROVED_NON_IDENTIFIABILITY
    Enmienda: ninguna

[x] N1 — mantener acotado
    Enmienda: ninguna

[x] N2 — degradar a lema
    Enmienda: ninguna

[x] N3 — remark de diseño
    Enmienda: ninguna

[x] N4 — debilitar a corolario dimensional
    Enmienda: ninguna

[x] N5 — retirar como contribución
    Enmienda: ninguna

[x] Fase 3 preferida tras paper: B2 (default de la hoja de ruta)
    Enmienda: ninguna — B1 solo como programa nuevo con grammar propia, no inmediato

[x] 0.2 — banner en next_observable_candidate_matrix verificado
[x] 0.3 — vocabulario §3 + taxonomía §4.4 verificado

PI_SIGN_OFF: Ignacio (PI / Nacho) — aceptación en sesión de trabajo 2026-07-28
FECHA: 2026-07-28
HEAD al firmar: e9744d8 (pre-commit del lote Fase 0; el commit de cierre actualiza el árbol)
```

---

## 8. Cierre de Fase 0

Fase 0 queda **cerrada** (2026-07-28):

1. §7 tiene `PI_SIGN_OFF` con R1–R3 y N1–N5 aceptados sin enmiendas;
2. la matriz lleva el banner de abandono;
3. la taxonomía incluye §4.4 con las dos etiquetas.

**Siguiente paso autorizado:** abrir **Fase 1** (outline + manuscript de límites)
sin reabrir el norte abandonado. Ítem 5 del Paso D sigue pendiente (no bloquea
redactar límites sin claim público de novedad de N1).
