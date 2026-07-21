# Paper outline — Order-only horizon localization: one in-patch positive + a six-channel negative ledger

STATUS: OUTLINE / PROPOSAL_ONLY / NOT_A_CLAIM / NOT_FROZEN / NO_NEW_RESULT
DATE: 2026-07-21
SCOPE: consolidation proposal (decision 042 §7 option C6-E). No implementation, no seeds, no
freeze, no seal change. This document only *proposes* how to package results that already exist;
it establishes no new scientific claim.

> Guardrails honoured verbatim: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`,
> `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`. The paper is a
> **recoverability benchmark**, never a reconstruction claim; every number cited is the literal
> output of a committed deterministic script under the frozen seal.

---

## Título de trabajo
**"Order-only horizon localization in a finite causal-set patch: one in-patch positive and a typed
ledger of six exhausted localization channels"**
*(recoverability benchmark — explícitamente `NO_RECONSTRUCTION_CLAIM`; patch finito 1+1D
Schwarzschild)*

## Tesis (una frase)
En un patch finito 1+1D de Schwarzschild, **un** observable order-only (volumen de futuro) localiza
estructura tipo horizonte con un PASS pre-registrado y sellado; y **seis** vías independientes de
localización de región mueren por una misma familia estructural de razones — no por la física. El
valor está tanto en el positivo como en la honestidad tipada de los negativos, y en un proceso que
se falsea a sí mismo.

## Ángulo de venta
No es "encontramos el horizonte". Es *"así se hace localización order-only con disciplina: un
positivo sellado, seis negativos tipados con anclas, y un proceso (comité + auditoría) que se
corrige a sí mismo"*. La honestidad-como-método es lo diferencial.

---

## Índice

### 1. Introducción y alcance
- Recoverability benchmark vs reconstrucción. Gramática de claims (`docs/claim_grammar.md` §3:
  teleología del horizonte, proxy cuasi-local, patch finito).
- Frontera de la afirmación desde la primera línea: 1+1D, patch finito, order-only en la selección,
  el embedding oculto **sólo puntúa** (nunca define ni guía).
- Contribución declarada: (i) un positivo in-patch sellado; (ii) un ledger de seis negativos
  tipados; (iii) una conclusión estructural transversal; (iv) el método (comité/auditoría) como
  aportación.

### 2. Fundamentos y reglas del juego *(por qué el método es creíble)*
- Separación dev/validación; congelado de umbrales antes de ver datos de validación.
- "Un guardarraíl que no puede fallar es decoración": todo número con backing verificable
  (file:line, comando, commit, cita) o marcado `[UNVERIFIED]`.
- El sello (`thresholds.py`, prereg-002 seal #3, sha256 `6e2c3888…bfefd4`) y la disciplina de
  auditoría (20+ reportes con dientes: `docs/auditor/…`).
- Anclas: `README.md`, `docs/preregistration.md`, `docs/reuse_check.md`, `CLAUDE.md`.

### 3. El positivo — localización in-patch con el observable de volumen
- Pre-registro `docs/preregistration_002.md`; resultado `docs/preregistration_002_result.md`
  (PASS); caveats documentados.
- Cierre honesto del gap de artefacto: SUPERVISED_REVERIFICATION MATCH — estado
  `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]`
  (`docs/comite/comite_decision_016_prereg002-supervised-reverification.md`,
  `docs/prereg002_reverification_{declaration,result}.md`).
- Sustento analítico: teorema de dos puntos + paquete teórico de Fase 1
  (`docs/comite/comite_decision_027…033`).
- Frontera: localización in-patch de un observable order-only, **no** reconstrucción métrica ni
  horizonte de eventos global.

### 4. El ledger de negativos tipados — la línea de localizadores C1–C6
- Encuadre: documentar negativos con anclas (file:line, commit, terminal) es un resultado.
  "Fracaso documentado > almost-PASS" (decision 042 §5.7).
- Tabla maestra (de `docs/comite/comite_decision_042_…` §4, ampliada con C6):

  | Canal | Idea en una línea | Terminal | Lección |
  |---|---|---|---|
  | C3-early | anchura futura / funnel | `REJECTED_HAYWARD` | funnel de singularidad ≠ trapping |
  | C1 | bottleneck / ideal / `Max` | `BLOCKED_UNCLOSED + MAX_TRIVIAL` | `Max` trivializa en lo finito |
  | C2 | common future / κ | `BLOCKED_E_INDEP + TRUNCATION` | sin null + techo, mide la caja |
  | C3-third | `L,V` en minimales | `INCONCLUSIVE_EDGE_MARGINAL` | canal marginal, ve la pared |
  | C4 | joint en vecinos | `REJECTED_NO_E_M` | no hay grafo de vecinos order-only (decision 039) |
  | C5 | matriz → bloque espectral | `EXHAUSTED (F3)` | pared ≠ `Max`; sin dual lateral (decision 040/041) |
  | **C6** | **antichain-cintura `W(p,q)`** | **`BLOCKED_NO_STABLE_CODIM2`** | **existe la antichain, no la pantalla estable ni el transporte (decision 043/044)** |

### 5. Caso de estudio C6 en detalle *(el más nuevo y el más limpio metodológicamente)*
- Objeto `W(p,q) = {x : p ≺* x ∧ x ≺* q}` (cintura de bi-enlaces de un intervalo de Alexandrov);
  **teorema de antichain order-only** (prueba completa → Apéndice A).
- Los cuatro gates: familia (existe, abundancia/estabilidad `|W|≥2` irresoluble sin ejecución);
  `|W|` como cardinalidad cerrada, no área física; sin transporte order-only canónico; sin signo
  order-only.
- **La revisión por comité como parte del método**: 043→044, cómo el red-team detectó la
  sobre-afirmación (abundancia "ALTA" contradictoria) y bajó el terminal al negativo conservador
  `NO_STABLE_CODIM2` (transporte queda como bloqueo adicional independiente). Viñeta vendible: el
  proceso se falsea a sí mismo.

### 6. La conclusión estructural transversal
- Los seis canales señalan lo mismo: localizar *región* de horizonte order-only en este banco choca
  con techo/pared, ausencia de pareo lateral order-only, y confusión escala↔profundidad — no con la
  física.
- Enlace con el hilo BD/PR011 (V4b): la validación de *fidelidad* de horizonte pediría una familia
  horizon-bearing con eje de colocación que este banco no tiene (dossier OP-2.2; decision 037;
  marcador `docs/marcador_reentrada_2026-07-19.md`).

### 7. Relación con la literatura
- Eichhorn–Gamito–Stokes, *Towards black-hole horizons and geodesic focusing in causal sets*
  (arXiv:2605.06813; `biblioteca/derived-md/…`): ladders como trazadores de geodésicas nulas,
  expansión `Θ=(1/A)dA/dλ`, focusing 1+1D. Qué motiva y qué **no** transfiere: transporte de
  pantallas, codim-2 en 1+1D (no hay 2-superficie espacial; sólo el signo de Θ, tras promediar).
- Benincasa–Dowker (abundancias de intervalos, acción): informan curvatura/manifoldness, **no** dan
  pantalla / transporte / signo.
- Rideout–Wallden, Boguñá–Krioukov: por qué no suministran el grafo de vecinos order-only que
  C4/C5/C6 necesitarían (decision 039, alcance acotado).

### 8. Límites y trabajo futuro honesto
- Lo que **NO** se afirma: reconstrucción métrica, horizonte de eventos global, 3+1D, área-law,
  identificación de superficie marginal.
- Qué haría falta para reabrir: resumen en §8.1 (las dos condiciones se exigen **a la vez**).

#### 8.1 Condiciones de reapertura *(por qué el listón es el banco, no el observable nº 7)*

Reabrir la línea de localización exige **dos condiciones simultáneas**, de **dos hilos distintos**
del programa. Ninguna basta por sí sola.

**(A) Objeto + target distintos — no otro autovector.** *(hilo localizadores C1–C6; decision 042
§6, §8.)* La línea C1–C6 cambiaba el observable pero conservaba el mismo problema y la misma
maquinaria de fondo:
- *target invariante:* "localizar la **región** de horizonte → partición/bloque espacial";
- *objeto de fondo invariante:* casi todo se reducía a la matriz de futuros comunes de los
  minimales y a un resumen espectral suyo (C4 → C5 → `Φ★_L`).
Elegir otro autovector, otro umbral o otro clustering de **esa misma matriz** es variación
cosmética, no un objeto nuevo — y por eso todos murieron por la misma pared. Reabrir exige cambiar
**las dos** cosas: (i) un objeto order-only que **no** sea "resumen de la common-future de
minimales", y (ii) un target definido por separado (p.ej. un proxy cuasi-local de expansión/trapping
con su propio criterio, no una etiqueta de región; cf. gramática de claims). Test rápido de
descarte: **si una idea se puede escribir como "otro autovector/umbral/clustering de la matriz de
minimales", es la misma línea con otro nombre** — prohibido (decision 042 §6).

**(B) Familia *horizon-bearing* con eje de colocación — el problema del banco.** *(hilo BD/PR011/
OP-2.2; `docs/marcador_reentrada_2026-07-19.md`, decision 037.)* Esta condición es sobre el
**test-bench**, no sobre el observable:
- *horizon-bearing:* la familia de causets sintéticos de validación debe contener la estructura de
  horizonte de forma controlada;
- *eje de colocación (placement axis):* la **posición del horizonte debe variar de forma conocida y
  controlada** a lo largo de un eje, para poder validar *fidelidad de localización* (casos con el
  horizonte en sitios distintos + comprobar que el observable lo sigue).
El banco actual **no tiene ese eje**: los tres objetos independientes (R-VAR, Candidate A/PR009/
PR010, BD/OP-2.2) chocaron con la misma degeneración estructural — la caja alta colapsa los futuros
en el techo (degeneración MINK-null de caja alta) y la señal de "pared" no se separa de la de
"bridge" (el `F3` de C5). El banco no puede, ni en principio, separar colocación de horizonte de
artefactos de la caja; por eso ningún observable order-only podía ganar ahí — **no por la física,
sino por falta de contraste en el banco**.

**Conclusión operativa.** El paso difícil **no** es inventar el observable nº 7, sino **construir el
banco**: una familia horizon-bearing con eje de colocación que no herede la degeneración de caja
alta ni la ambigüedad pared↔bridge. Mientras el test-bench no tenga ese eje, cualquier observable
nuevo vuelve a morir por la misma pared. Por eso la recomendación viva es **consolidar** (§3–§6),
no abrir C7: reabrir de verdad significa resolver primero el problema del banco, una empresa de otro
tamaño. Cualquier reapertura debe pasar por `/comite` dedicado + autorización explícita del PI
(decisiones 035/036/037), nunca por adaptación post-hoc.

### 9. Reproducibilidad
- Sello, seeds (bandas dev vs validación disjuntas), comandos, hashes; separación dev/validación;
  el rol de las auditorías y del comité. Cómo re-verificar el PASS y cada terminal negativo.

---

## Apéndices
- **A.** Prueba completa del teorema de antichain C6 (de `comite_decision_043` §5).
- **B.** Suite conceptual de falsificadores C6 (`comite_decision_043` §11).
- **C.** Índice de decisiones de comité (003–044) y reportes de auditoría (con terminales).
- **D.** El teorema de dos puntos y el paquete teórico de Fase 1.

---

## Mapa outline → artefactos del repo (para redacción)
| Sección | Artefactos base |
|---|---|
| 1–2 | `docs/claim_grammar.md`, `docs/preregistration.md`, `README.md`, `CLAUDE.md`, `docs/reuse_check.md` |
| 3 | `docs/preregistration_002{,_result}.md`, `comite_016`, `docs/prereg002_reverification_*`, `comite_027…033` |
| 4 | `comite_042` §4 (tabla), terminales C1–C6 |
| 5, A, B | `comite_043`, `comite_044` |
| 6 | `comite_037`, dossier OP-2.2, `docs/marcador_reentrada_2026-07-19.md` |
| 7 | `biblioteca/derived-md/Towards black-hole horizons…md`, `…/Benincasa_Dowker_2010_…md`, `comite_039` |
| 8 | `comite_042` §7–8 |
| 9 | `docs/estimator_v2_seal.md`, `Makefile` (`verify-seal`), `docs/auditor/*` |

---

## Riesgos de redacción (a vigilar)
1. No dejar que el ledger de negativos suene a "casi lo logramos": son negativos, y su valor es
   precisamente ser negativos limpios.
2. No sobre-atribuir a EGS/BD resultados de transporte/pantalla que no dan.
3. Mantener la frontera 1+1D/patch finito en cada sección, no sólo en la intro.
4. El positivo (§3) arrastra `PRIMARY_ARTIFACT_LOST`: declararlo, no esconderlo.
5. Este outline **no** es el paper ni un claim; cualquier número entra sólo re-verificado bajo sello.
