# Paper outline — Order-only horizon localization: one in-patch positive + a six-channel negative ledger

STATUS: **MATERIAL_SOURCE_ONLY** / SUPERSEDED_AS_PROGRAM_THESIS /
OUTLINE / PROPOSAL_ONLY / NOT_A_CLAIM / NOT_FROZEN / NO_NEW_RESULT
DATE: 2026-07-21
**SUPERSEDED NORTH (2026-07-28):** la tesis y el orden de pilares del manuscript de
límites los gobierna
`research_program/synthesis/phase1_limits_paper_outline.md` (Fase 1).
Este archivo se conserva como **fuente de material** (ledger C1–C6, prereg-002,
caso C6, adenda TV). No reabre el norte reconstructor abandonado en Fase 0.
ADDENDUM: 2026-07-26 — §6.1 (tercer resultado: cota inferior de TV order-only) y §8.2 (distancia
real a Schwarzschild 3+1). Ambas secciones son **material de outline**, no claims; §6.1 depende de
condiciones aún **no cumplidas** (C3, C4 del acta 045) y lo declara en su propio encabezado.
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

#### 6.1 Adenda 2026-07-26 — un tercer resultado: la primera cota inferior de TV order-only

> **Estado, declarado.** Adjudicado por `docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md`
> (`COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_CAVEATS`, commit `2955bc5`) sobre auditoría
> `auditor_report_026` (`AUDIT_PASS_WITH_WARNINGS`, 0 errores, `4124be2`). **Las etiquetas del acta
> §8.3 NO están adoptadas todavía**: faltan sus condiciones **C3** (fijar `dv` por escrito) y **C4**
> (adoptarlas como bloque). En el árbol, Forma L sigue `[OPEN]`
> (`wp4_comparable_pair_separation.md:381`). Esta sección describe qué *habría* que escribir si el
> PI autoriza; **no** ejerce la autorización.

Material fuera de la línea C1–C6 y fuera del banco sellado: cálculo analítico puro (álgebra
simbólica + cuadratura determinista; no importa nada de `nachocausal/`, no consume semillas, no toca
umbrales). Encaja como **tercera contribución**, distinta del positivo sellado (§3) y del ledger de
negativos (§4).

**Qué se probó.** Para la familia de diamantes 1+1D de WP4 §4 (esquinas EF fijas, lapso nulo `dv`),
el conteo de pares comparables `S_n` —la *ordering fraction* de Myrheim— satisface, en el canal
`fixed_n` y para cada par `tau != tau'` **fijado de antemano**:

```text
Delta_p != 0  (Cor. C6, dv < dv_0 no efectivo)
  + E[S_n] = C(n,2) p(tau)                       exacto
  + Var(S_n) = C(n,2)[2(n-2) zeta_1 + zeta_2]    exacto (Hoeffding, U-estadístico binomial)
  + zeta_1, zeta_2 <= 1/4                        universal
  + data processing (S_n es invariante de isomorfismo)
  + Chebyshev en el punto medio
  ==>  TV(Q^n_tau, Q^n_tau') -> 1   cuando n -> infinito.
```

**Por qué merece sección propia — y no es «hay información geométrica en el orden».** Lo genuinamente
nuevo es **metodológico**: la ficha §2 afirmaba que *no existía en el repo ninguna técnica para acotar
`TV(Q)` por debajo*. Eso es ahora falso. La receta —**estadístico order-only + data processing +
Chebyshev**— no depende de `S_n`: sirve para cualquier funcional order-only con dos momentos
calculables, y por tanto viaja a los candidatos 7.2–7.4 y, en principio, a 3+1. Es la pieza más
transferible del bloque.

**Tres precisiones que el paper debe llevar, porque cambian la lectura.**

1. **No hace falta importar nada.** Ni CLT de Reitzner–Schulte, ni des-Poissonización, ni ajuste
   empírico de exponente. Por FWP Lema 0 los `n` puntos son i.i.d., luego `S_n` es un U-estadístico
   **binomial**, no un funcional de Poisson. Confirmación textual: Reitzner–Schulte declaran ellos
   mismos (p. 23) que no hay puente de des-Poissonización con tasas.
2. **La tasa `n^{-1/2}` es óptima en exponente, por ambos lados.** La cota de WP4 §5 es **no
   asintótica** (Cauchy–Schwarz integrado, no desarrollo QMD) y acota `TV(Q^n)`, que por definición
   es el supremo sobre *toda* función del poset: **ningún** procedimiento order-only separa a
   `delta = o(n^{-1/2})` en esta familia. Consecuencia para §8.2: el exponente **no** es un sitio
   donde ganar; toda mejora futura está confinada a la constante.
3. **El mismo estadístico tiene un punto de ceguera exacta, y está garantizado.** Como
   `Delta_p(0.02) > 0`, `Delta_p(4) < 0` y `p` es continua en `dv`, por el **teorema del valor
   intermedio existe `dv*` con `Delta_p(dv*) = 0` exactamente**: ahí `S_n` es ciego a nivel de medias
   para **todo** `n`. No rompe el teorema (Cor. C6 excluye ceros bajo `dv_0`); lo **acota**, y
   prohíbe extrapolar en `dv`. El comité, por tanto, **subió una etiqueta y bajó otra**: refutó
   `ficha:483-485` («el estadístico nunca es ciego ahí»). Esa simetría es exactamente la viñeta
   metodológica de §5 repetida en otro objeto, y debe contarse así.

**Frontera, en los términos del físico del comité.** En 1+1D Schwarzschild `tau` es simultáneamente
el radio del horizonte **y la única amplitud de curvatura** (`R_tau = -2 tau/r^3`): no hay un segundo
invariante dimensional, luego «discriminar el radio del horizonte» y «discriminar la curvatura media
del parche» son **el mismo acto**. Y `kappa > 0` está probado para todo `0 < r_q < r_p` **sin
ninguna condición sobre `tau`**: no hay estructura de umbral en `r = tau`, ni cambio de signo, ni
nada que se dispare *porque* el diamante cruce el horizonte. Llamar a esto «información de horizonte»
sería una convención de nombre, no un hecho físico. **Prohibido en el paper.**

**Higiene numérica (vinculante).** Las cardinalidades que exige la cota de Chebyshev son de muchos
órdenes de magnitud por encima de cualquier cosa ejecutable, pero **las cifras concretas no tienen
generador commiteado** y sólo existen en prosa de `auditor_report_026:164-166`
`[UNVERIFIED — sin generador; condición C2c del acta 045]`. **No pueden entrar en el paper** hasta que
un script determinista las emita verbatim (precedente vinculante: `auditor_report_024 = AUDIT_FAIL`
por exactamente este defecto). Nótese además que lo enorme es **la cota**, no la TV verdadera, que es
desconocida: por eso el comité rechazó explícitamente la etiqueta `PROVED_BUT_VACUOUS_IN_PRACTICE`
—sobre-afirma en dirección pesimista— igual que rechazó «viabilidad matemática demostrada».

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

#### 8.2 Adenda 2026-07-26 — distancia real a Schwarzschild 3+1 *(la sección de honestidad)*

Sección de discusión, no de resultados. Sirve para que ningún lector —ni ningún autor futuro— lea
§6.1 como un paso hacia la reconstrucción.

**La frase en una línea.** Hemos probado que **cierta** información geométrica sobrevive a olvidar
las etiquetas, y —más útil— hemos construido la primera técnica del repo para demostrarlo. **No**
hemos probado que esa información permita localizar nada; y en 1+1D no puede distinguirse de
información de curvatura (§6.1, frontera).

**Advertencia sobre la vara de medir.** Este proyecto es un *recoverability benchmark* con claim
acotado a localización order-only en un parche finito **1+1D** (`CLAUDE.md`, `docs/claim_grammar.md`
§3). «Reconstruir Schwarzschild 3+1» **nunca fue el objetivo declarado**. Estar lejos de una meta que
no se fijó no es un hallazgo, y el paper no debe redactarse como si lo fuera. La pregunta honesta no
es *«¿cuánto falta para 3+1?»* sino *«¿sigue siendo informativo el benchmark 1+1D, y dónde está su
muro?»*. Lo que sigue enumera la distancia sólo porque el lector la va a preguntar.

**Los peldaños que faltan — son tres, no dos.** El error más fácil es saltar de «distinguir dos
modelos» a «localizar una superficie»:

| # | Peldaño | Estado |
|---|---|---|
| 1 | *Distinguir* dos completions fijadas de antemano | §6.1, acotado |
| 2 | *Estimar* `tau` (conjunto de confianza) | **no probado** — exige error de test uniforme sobre una red, que no existe, y está topado por WP4 §5 de todos modos |
| 3 | *Localizar* una superficie dentro de un causet dado | **no probado**, y es el muro real |

**Qué faltaría de verdad, en orden de dificultad creciente.**

1. **De «distinguir» a «localizar».** `S_n` es global: da un número para todo el parche. No asigna
   posición a los elementos ni produce superficie alguna. La pregunta que responde es *«¿este poset
   viene de `tau` o de `tau'`?»*, no *«¿dónde está el horizonte dentro de este poset?»*.
2. **Una pantalla codimensión 2 intrínseca y estable.** Definible sólo con orden causal, cardinalidad
   y quizá enlaces/intervalos — sin coordenadas, sin embedding, sin `r` previo. **Sigue siendo el
   cuello de botella**, y el ledger C1–C6 documenta seis intentos fallidos: incluso la antichain
   `W(p,q)` (C6) era genuinamente order-only, pero sin transporte canónico ni garantía de representar
   una pantalla física (§5, `BLOCKED_NO_STABLE_CODIM2`).
3. **Separar horizonte de borde artificial.** Un observable debe distinguir truncación por horizonte,
   truncación por borde del parche, fluctuación del sprinkling, densidad/cardinalidad y elección de
   extremos. **En la familia de §6.1 esto no es un riesgo futuro: es la situación actual.** Las
   esquinas están fijas, `kappa > 0` no depende de `tau`, y toda la señal es forma de la región. No
   estamos separando horizonte de borde — estamos midiendo cómo la forma del parche depende de `tau`.
4. **Un banco 3+1 físicamente limpio**, con horizonte realmente incluido, eje de colocación, y target
   definido antes de mirar datos. Es exactamente la condición **(B)** de §8.1, y los bloqueos de
   PR009–PR012 y OP-2.2 muestran que no lo tenemos.
5. **Identificabilidad local.** Aunque se distingan dos geometrías globalmente, podrían existir varias
   localizaciones del horizonte con leyes order-only indistinguibles. Haría falta *posición distinta
   ⟹ ley order-only distinta* para un target local. Nota: en 1+1D hay un análogo **parcial** —la
   rigidez de cópulas de FWP §4 (misma cópula ⟹ isometría salvo escala)— pero es sobre el parche
   entero, no sobre la posición del horizonte, y sigue `[PROSE-REMARK, promoción pendiente]`. Y `d=2`
   es justamente donde falla la rigidez tipo HKMM (ficha `:545`).
6. **Eficiencia finita.** No basta con que el error tienda a cero. **Pero cuidado con dónde se pide la
   mejora:** por §6.1 punto 2 el *exponente* `n^{-1/2}` es óptimo y no mejorable por ningún
   procedimiento order-only. Lo único abierto es la **constante**: prefactor real de `TV(Q^n)`,
   pérdida por comprimir todo el poset en el escalar `S_n` (que reduce la cópula entera a una tau de
   Kendall), robustez frente al sprinkling, y resolución alcanzable. El chequeo de una sola dirección
   `zeta_1 * Ibar >= kappa^2 dv^2 / 54` sigue **enunciado y sin ejecutar** (falta `Ibar` para estas
   esquinas): es un *defeater* vivo, no una premisa satisfecha.

**La metáfora, con la precisión puesta.** Antes cabía temer que el poset no contuviera **ninguna**
huella utilizable de la geometría. Ahora sabemos que en un juguete controlado sí la contiene. Pero
lo construido es un detector que distingue dos habitaciones **sólo si te dicen de antemano cuáles dos
son candidatas**, **sólo si difieren en un parámetro nombrado por anticipado**, y **con un par
concreto (`dv*`) donde marca exactamente cero**. Reconstruir Schwarzschild 3+1 exigiría, dentro de una
habitación a oscuras, dibujar una esfera concreta, localizarla, demostrar que no es una pared falsa y
estimar su radio.

**Conclusión operativa (converge con §8.1).** El programa ha aclarado dónde está la dificultad
verdadera: **no** en demostrar alguna separación asintótica global, **no** en mejorar un
clasificador, sino en encontrar un **objeto local, order-only, codimensión 2, estable y físicamente
identificable** — y en construir el banco que permita validarlo. §6.1 es una pieza teórica útil que
**evita una imposibilidad demasiado fuerte**; no resuelve el problema del horizonte. Un programa que
sabe dónde está su muro, y lo ha documentado con seis terminales tipados, está en mejor sitio que uno
que aún lo busca. Por eso la recomendación viva sigue siendo **consolidar**, no abrir C7.

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
| **6.1** | `research_program/work_packages/wp4_comparable_pair_separation{,_checks.py}.md` (Anexo C §4b), `wp4_fisher_localization_floor.md` §5/§5a, `research_program/models/first_witness_pair_candidates.md` (Lemas 0/1, Teo A), `research_program/bibliography/ficha_se_busca_tv_order_only.md` §§1.3/3/4/6.3/6.4/7.1, `comite_045`, `auditor_report_026` |
| 7 | `biblioteca/derived-md/Towards black-hole horizons…md`, `…/Benincasa_Dowker_2010_…md`, `comite_039` |
| 8 | `comite_042` §7–8 |
| **8.2** | `comite_045` §8 (síntesis, etiquetas) y §9 (condiciones C1–C4), `docs/hoja_de_ruta_27_jul_2026.md` §§2–4 |
| 9 | `docs/estimator_v2_seal.md`, `Makefile` (`verify-seal`), `docs/auditor/*` |

---

## Riesgos de redacción (a vigilar)
1. No dejar que el ledger de negativos suene a "casi lo logramos": son negativos, y su valor es
   precisamente ser negativos limpios.
2. No sobre-atribuir a EGS/BD resultados de transporte/pantalla que no dan.
3. Mantener la frontera 1+1D/patch finito en cada sección, no sólo en la intro.
4. El positivo (§3) arrastra `PRIMARY_ARTIFACT_LOST`: declararlo, no esconderlo.
5. Este outline **no** es el paper ni un claim; cualquier número entra sólo re-verificado bajo sello.
6. *(adenda 2026-07-26)* **§6.1 no es «encontramos información de horizonte».** En 1+1D `tau` es a la
   vez radio del horizonte y única amplitud de curvatura: la separación es una firma de
   **curvatura/forma**. Escribirlo de otro modo es sobre-atribución, y `kappa > 0` sin condición sobre
   `tau` lo delata.
7. *(adenda 2026-07-26)* **No publicar ninguna cifra `n*` ni cota TV numérica** mientras no las emita
   un script determinista commiteado (C2c del acta 045). Hoy sólo existen en prosa de auditoría.
8. *(adenda 2026-07-26)* **No usar `PROVED_BUT_VACUOUS_IN_PRACTICE` ni «viabilidad matemática
   demostrada».** La primera sobre-afirma en dirección pesimista (lo enorme es la cota, no la TV);
   la segunda en dirección optimista. Ambas rechazadas por `comite_045` §8.3.
9. *(adenda 2026-07-26)* **Contar la ceguera en `dv*` junto al positivo, no en una nota al pie.** La
   simetría subir-una-etiqueta/bajar-otra es parte de la viñeta metodológica del paper, igual que el
   043→044 de §5.
10. *(adenda 2026-07-26)* **§6.1 depende de condiciones no cumplidas** (C3: fijar `dv`; C4: adoptar
    las tres etiquetas como bloque). Si se redacta el paper antes de cumplirlas, la sección debe
    llevar su encabezado de estado tal cual, sin suavizarlo.
