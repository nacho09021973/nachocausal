# Comite Decision 042 — Cierre de la línea de localizadores C1–C5

STATUS: LINE_CLOSURE_DOCUMENTARY / CANDIDATE_5_NEVER_OPENED  
NO_IMPLEMENTATION / NO_EVALUATION_SEEDS / NO_FREEZE / NO_RECONSTRUCTION_CLAIM  
DATE: 2026-07-20

Este documento **cierra la línea de localizadores relacionales C1–C5** para el propósito de
localizar estructura tipo horizonte / borde en el orden finito. No reabre C4 ni C5, no implementa,
no lanza seeds de evaluación, no sella un estimador y no afirma reconstrucción métrica ni
horizonte de eventos global.

```text
C1_TO_C5_LOCALIZER_LINE = EXHAUSTED_FOR_LOCALIZATION
CANDIDATE_5 = NEVER_OPENED
HONEST_NEGATIVE = YES
```

---

## 1. Propósito

Dejar un ledger legible de **fracasos y bloqueos**, con anclas de repositorio, para que un
reentrada futura no repita el mismo canal con otro nombre. Al final se anotan **ideas para un
eventual C6** — solo como menú, sin autorización.

---

## 2. Contexto del programa

Objetivo estratégico del hilo (no del sellado prereg-002): observables **order-only** sobre
causets finitos que capturen estructura asociada a trapping / horizonte aparente / borde, sin
coordenadas en la selección, sin pretender identificar el horizonte de eventos global
(`docs/claim_grammar.md` §3: teleología del horizonte; patch finito).

Lo que **sí** quedó en el programa sellado (prereg-002 PASS en 1+1D, etc.) es **independiente**
de esta línea C1–C5. Este ledger no toca el seal.

---

## 3. Ledger de fracasos / bloqueos (C1 → C5)

### C3 (temprano) — colapso de anchura futura

| Campo | Contenido |
|---|---|
| **Objeto** | Colapso de anchura del futuro (long-thin future / funnel) |
| **Intención** | Proxy de singularidad / funnel |
| **Muerte** | **REJECTED** — falla el control Hayward (agujero regular sin singularidad): el funnel es de singularidad, no de horizonte aparente |
| **Ancla** | `docs/comite/comite_decision_006_…` (C3 ya rechazado en el dossier); `dev/X0_Qn_wellposedness_NOTES.md` §11.3 |
| **Lección** | No confundir funnel de singularidad/truncación con trapping |

```text
C3_EARLY = REJECTED_HAYWARD_SINGULARITY_FUNNEL
```

---

### C1 — cuello de botella / flujo a través de ideales (y rastro relacional)

| Campo | Contenido |
|---|---|
| **Objeto** | Antichain / ideal con mínimo de flujo de covers hacia el complemento; más tarde referencia `R=Max(C)`, past relacional, interface |
| **Intención** | Membrana one-way / bottleneck order-only |
| **Muertes en cadena** | (1) Definición no cerrada: búsqueda de antichain, “mínimo local pronunciado”, parámetros abiertos. (2) Con `R=Max(C)` en poset finito: `down(Max)=C`, interface vacía — **trivialización**. (3) No-identificabilidad completion/truncation abierta. (4) Guardas y specs sin cierre de `ASYMMETRY_SCORE` / `BULK_CONTROL` / umbrales |
| **Anclas** | Decisiones 006, 008, 009, 010, 012–013; `dev/PR003_C1_*`; Lean formal parcial sin física cerrada |
| **Lección** | Ideal/filtro es order-canónico; la física de “horizonte” no cae gratis. `Max` como referencia rompe en lo finito |

```text
C1 = BLOCKED_UNCLOSED_DEFINITION + FINITE_MAX_TRIVIALIZATION + COMPLETION_OPEN
C1_NEVER_PROMOTED_TO_FROZEN_LOCALIZER
```

---

### C2 — colapso de solape futuro de un wavefront

| Campo | Contenido |
|---|---|
| **Objeto** | `κ(A) = \|⋂ J⁺(a_i)\| / E_indep` sobre antichain/wavefront |
| **Intención** | Focusing / common future anómalo |
| **Muerte** | Normalizador `E_indep` no intrínseco/cerrado; confusión fuerte con truncación de caja (todos los futuros se fusionan en el techo); Hayward solo “condicional” |
| **Ancla** | Decision 006 (REFINE, no promoción); notas X0 §11.2 |
| **Lección** | El numerador joint es legítimo; sin null order-only y sin control de techo, mide la caja |

```text
C2 = BLOCKED_E_INDEP_AND_TRUNCATION_CONFOUND
C2_NEVER_PROMOTED
```

---

### C3 (tercer localizador) — futuros truncados / selectores marginales en minimales

| Campo | Contenido |
|---|---|
| **Objeto** | Localizer sobre `Min(C)` con scores order-only tipo longitud/volumen de futuro (`L`, `V`) y brazos de truncación; scoring de borde solo post-selección |
| **Intención** | Localizar onset de truncación de futuros / borde asociado |
| **Muerte** | Desarrollo limpio pero terminal **INCONCLUSIVE**; dominancia de borde; sinergia de pares insuficiente; esencialmente canal **marginal** |
| **Ancla** | `docs/preregistration_square_box_truncated_futures_localization_draft.md`; `evidence/square_box_truncated_futures_localization_20260719/`; resumen en `dev/PR003_C4_…` §2 |
| **Lección** | `L,V` en minimales ven la pared de la caja; no bastan para un localizador de horizonte |

```text
C3_THIRD_LOCALIZER = INCONCLUSIVE_EDGE_DOMINATED_MARGINAL
```

*(Numeración histórica: el “C3” del comité 006 es el width-collapse; el “tercer localizador” del hilo square-box se llamó también C3 en notas C4. Aquí se distinguen como C3-early y C3-third.)*

---

### C4 — convergencia de common-future condicionada en vecinos

| Campo | Contenido |
|---|---|
| **Objeto** | Score de solape común de futuros en pares de minimales “vecinos”, con persistencia bajo peel |
| **Intención** | Información **no marginal** (joint), localizada en aristas de un grafo `E_M` |
| **Muerte** | **`NEIGHBOR_GRAPH_UNRESOLVED`**: no hay grafo `E_M ⊂ binom(Min,2)` order-only, relabel-invariante, no circular, cerrado en empates. Rideout–Wallden y Boguñá–Krioukov no suministran ese `E_M` en el dominio C4 (Decision 039) |
| **Lo que sí se demostró** | Toy finito: el solape no está determinado por el par de volúmenes marginales |
| **Anclas** | `dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md` (`136c193`); `docs/comite/comite_decision_039_…` (`a5276bb`) |
| **Lección** | Joint futures ≠ vecinos espaciales intrínsecos. All-pairs no es grafo de vecinos |

```text
C4 = REJECTED_NO_INTRINSIC_NEIGHBOR_GRAPH
CANDIDATE_4 = CONCEPT_BLOCKED_NEVER_OPENED_AS_PREREG
```

---

### C5 — matriz global de common-future → bloque / partición

| Campo | Contenido |
|---|---|
| **Objeto** | Matriz `A_ij = \|J⁺(i)∩J⁺(j)\|` sobre todos los minimales; mapa a partición/abstención |
| **Intención** | Evitar `E_M`; localizar vía estructura de bloques de la matriz |
| **Arco** | 040: familia matriz sobrevive como espacio de búsqueda. 041: familias incompletas no cierran S1–S4. Existencia de mapas sin umbral. Φ★ filas exactas → muerta en ensemble (ruido). Φ★_L Laplaciano+peel nombrada. No-colapso vs `V` (PROVED). Sin dual lateral tipo `Max`. F1b PASS. Suite F1–F7: **FAIL en F3** (ambigüedad pared↔bridge) |
| **Muerte para localización** | (1) Filas exactas no emiten en régimen tipo Poisson. (2) No existe peel lateral canónico (pared = embebimiento). (3) Suite sintética: el corte twin de la “señal” bridge es el mismo que el de un surrogado de dos paredes |
| **Lo que sí se demostró** | Mapas formales cerrados; no-colapso algebraico a márgenes; techo controlable por peel; relabeling; techo-only no da detección estable |
| **Anclas** | Decisiones 040–041; `dev/C5_*.md`; suite `dev/c5_f1_f7_synthetic_suite.py`; commits `d5759e6` … `0da8919` |
| **Lección** | Información joint existe y no es solo `V`; **localizar región** choca con la caja/paredes. Generativo lateral no se puede sustituir por un truco espectral |

```text
C5_SEARCH_FAMILY = GLOBAL_COMMON_FUTURE_MATRIX   # objeto vivo como matemática
C5_LOCALIZATION_CHANNEL = EXHAUSTED
C5_F3 = FAIL_WALL_BRIDGE_TWIN_AMBIGUITY
CANDIDATE_5 = NEVER_OPENED
PHI_STAR_L = FORMAL_MAP_NOT_LOCALIZER
```

---

## 4. Tabla resumen

| Línea | Idea en una línea | Terminal |
|---|---|---|
| C3-early | Anchura futura / funnel | `REJECTED_HAYWARD` |
| C1 | Bottleneck / ideal / Max | `BLOCKED_UNCLOSED + MAX_TRIVIAL` |
| C2 | Common future / κ | `BLOCKED_E_INDEP + TRUNCATION` |
| C3-third | `L,V` en minimales | `INCONCLUSIVE_EDGE_MARGINAL` |
| C4 | Joint en vecinos | `REJECTED_NO_E_M` |
| C5 | Matriz → bloque espectral | `EXHAUSTED_LOCALIZATION (F3)` |

```text
NONE_OF_C1_C5_BECAME_A_FROZEN_HORIZON_LOCALIZER
NO_FAKE_CANDIDATE_PASS_ON_THIS_LINE
```

---

## 5. Lecciones transversales (para no repetir)

1. **Order-only es necesario, no suficiente.** Casi todos los canales mueren en techo, pared o definición abierta.
2. **El horizonte de eventos global no está en el patch finito.** Claim grammar: como mucho proxy cuasi-local; `NO_RECONSTRUCTION_CLAIM`.
3. **Marginal vs joint:** C3-third murió marginal; C4/C5 probaron joint real; joint no implica localizable.
4. **Vecinos espaciales no son order-gratis** en minimales (C4/039).
5. **Paredes no son `Max`:** no hay dual canónico lateral (C5 lateral note); la suite F3 lo operacionaliza.
6. **Igualdad exacta / umbrales:** o eres frágil al ruido, o reintroduces calibración prohibida.
7. **Fracaso documentado > almost-PASS.** Esta línea terminó sin `CANDIDATE_5` a propósito.

---

## 6. Estado de lo que queda de C5

No se borra la matemática útil:

- Matriz de common-future como objeto de estudio.
- Φ★_L como mapa formal y oráculo de estructura joint.
- Ledger F1–F7 y no-colapso vs `V`.

Se **prohíbe** sin nueva autorización mayor:

- Abrir `CANDIDATE_5` sobre particiones twin de minimales como localizador de región/horizonte.
- Reabrir C4 llamando all-pairs “vecinos”.
- “Arreglar” F3 con ε-clustering o grafo de vecinos no resuelto.

```text
C5_AS_LOCALIZER = CLOSED
C5_AS_JOINT_DIAGNOSTIC = ARCHIVAL_OK
```

---

## 7. Ideas posibles para un eventual C6

Solo menú. **Ninguna autorizada. Ninguna implementada. Ningún seed.**

### C6-A — Proxy cuasi-local de expansión / trapping (recomendado si se vuelve)

- Target distinto del “bloque de minimales” y del horizonte global.
- Alineado con EGS / focusing y con la gramática de claims (proxy de expansión/trapping definido aparte).
- Exige definición cerrada order-only o order+cardinalidad, nulls, y suite techo/pared **antes** de código.

### C6-B — Intervalos / Alexandrov y abundancias (BD-like) con target de curvatura o manifoldness

- No es localización de horizonte; es otra pregunta física (curvatura, dimensión efectiva).
- Riesgo: densidad y dimensión en el null (ya visto en C2).

### C6-C — Clasificación BH vs MINK con matriz joint, **sin** mapa a región

- Usar espectro/resúmenes de `A` como clasificador de familia causal, no como localizador.
- Más humilde; no resuelve Schwarzschild 3+1D localization.
- Debe declarar `CLASSIFICATION_ONLY`, nunca “detecta horizonte”.

### C6-D — Cortes/ideales revisitados solo con clase de búsqueda **totalmente cerrada**

- Reabrir C1 solo si el cuantificador sobre antichains/ideales queda algebraicamente cerrado (sin “mínimo pronunciado” libre).
- Prior alto de repetir trivialización o borde; solo con dual techo/pared en el diseño desde el día 0.

### C6-E — Pausa limpia de localizadores

- Consolidar negativos C1–C5, paper/theory package, no nuevo observable.
- A veces lo más productivo en la frontera.

### C6-F — (Exploratorio) 1+1D 2-órdenes y bordes izquierdo/derecho

- Solo en 1+1D; realisers no canónicos en general.
- Útil como laboratorio de paredes, no como teoría 3+1D.

### C6-G — Explicitamente **no** hacer

- Φ★_L con ε, k-means, o “el bloque más cercano al borde” con coordenadas.
- Reintroducir `E_M` sin resolver Decision 039.
- Prometer horizonte de eventos desde un patch finito.

---

## 8. Cierre del día

```text
TODAY = 2026-07-20
C1_TO_C5_LOCALIZER_LINE = EXHAUSTED_FOR_LOCALIZATION
DOCUMENTED_FAILURES = YES
CANDIDATE_5 = NEVER_OPENED
C6 = IDEAS_ONLY_NOT_AUTHORIZED
MAYBE_SOMEDAY = YES
NO_SHAME_IN_HONEST_NEGATIVES = YES
```

Si algún día se logra, será con un **objeto y un target distintos**, no repitiendo C5 con otro autovector.

---

## 9. Índice mínimo de anclas

| Tema | Ruta |
|---|---|
| Adjudicación C1/C2/C3-early | `docs/comite/comite_decision_006_…` |
| C1 trivialización / preflight | `docs/comite/comite_decision_009_…`, `010_…` |
| C4 notas | `dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md` |
| C4 grafo | `docs/comite/comite_decision_039_…` |
| C5 espacio | `docs/comite/comite_decision_040_…` |
| C5.1 mapas | `docs/comite/comite_decision_041_…` |
| C5 paquete Φ / lateral / no-colapso | `dev/C5_*.md` |
| C5 Path A | `dev/C5_PATH_A_LINE_TERMINAL.md` |
| Suite F1–F7 | `dev/C5_F1_F7_SUITE_ADJUDICATION.md` |
| Gramática / teleología | `docs/claim_grammar.md` |

---

## 10. Terminal final

```text
COMMITTEE_DECISION_042 = C1_C5_LOCALIZER_LINE_CLOSED
VERDICT = EXHAUSTED_FOR_LOCALIZATION
CANDIDATE_5_NEVER_OPENED
C6_IDEAS_RECORDED_NOT_AUTHORIZED
NO_IMPLEMENTATION
NO_EVALUATION_SEEDS
NO_RECONSTRUCTION_CLAIM
END_OF_DAY_HANDOFF = CLEAN
```
