# plan_genial.md — Plan de continuación tras el cierre de R-VAR

> **PLAN REVISABLE — 2026-07-05.** No es pre-registración, no fija umbrales, no autoriza por sí
> mismo ningún paso comprometedor. Todo paso one-way (freeze, validación ciega, publicación)
> pasa por `/comite` + autorización explícita del PI. Vigentes sin cambio:
> `RESPECT_SEAL_FREEZE`, `NO_RECONSTRUCTION_CLAIM`, `NO_GROUND_TRUTH_LEAKAGE`,
> `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`, `R_VAR_STATUS = CLOSED_NEGATIVE_RESULT`.

## 0. Por qué la opción A ("rendirse") es objetivamente errónea

El proyecto no está bloqueado; está en su punto de mayor valor acumulado:

- **La pregunta central ya tiene respuesta positiva congelada.** Prereg-002 = **PASS
  [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY]**
  (`docs/preregistration_002_result.md`): el estimador v2 sellado localiza la estructura de
  horizonte 1+1D desde el orden solo, ciego, con los 6 checks congelados en verde en el
  endpoint primario. Ese era el benchmark de recuperabilidad. Está conseguido.
- **El límite del instrumento está caracterizado y congelado.** Prereg-003 (FROZEN 2026-06-25,
  `docs/preregistration_003.md`): suelo de resolución operacional `Error ≳ K·ℓ = K·ρ^(-1/2)`,
  con `K_LOC=2` techo conservador, tres patas de evidencia (ancla + O3 numérico + O1/O2
  analítico).
- **Los negativos están acotados, no son derrotas del proyecto.** Prereg-001 FAIL → diagnóstico
  → v2 → PASS (el ciclo funcionó exactamente como debía). R-VAR
  (`docs/rvar_closure_negative_result.md`, `47be5c7`) está explícitamente acotado a esta
  geometría de caja y a los dos objetos probados — `GEOMETRY_SPECIFIC;
  PRIMARY_TRACK_UNAFFECTED`.
- **El proceso mismo es un resultado.** 21 decisiones de comité, 6 auditorías, un sello
  verificado en cada paso, un artefacto perdido detectado y re-verificado bajo supervisión, dos
  cascadas negativas documentadas sin maquillaje. En 2026 eso es metodológicamente publicable
  por sí solo.

Rendirse ahora sería abandonar un proyecto que ya ganó su apuesta principal porque perdió una
apuesta lateral.

## Eje 1 — Consolidación: el preprint (Paper I) ← PRIORIDAD

**Racional:** todo lo que necesita el paper ya está congelado y commiteado; escribirlo no
consume semillas, no toca el sello y asegura el valor contra cualquier riesgo futuro. Los
resultados no escritos se degradan; los congelados y publicados no.

**Contenido (esqueleto):**
1. Framing: benchmark de recuperabilidad, nunca claim de reconstrucción
   (`docs/preregistration.md:69-72`).
2. Protocolo: pre-registración congelada, sellado SHA-256, separación dev/validación, semillas
   quemadas, comité adversarial de 7 roles, auditor de integridad — el pipeline anti-autoengaño
   como contribución metodológica explícita (era AI: nadie más pre-registra así todavía).
3. Resultado negativo 1: prereg-001 FAIL (cobertura 0.30, fp 0.10) y su diagnóstico.
4. Resultado positivo: estimator-v2 (observable de volumen futuro + gate de abstención con
   τ(n) anclado a nulo abstracto) → prereg-002 **PASS [etiqueta completa, nunca desnudo]**.
5. Resultado de límite: el suelo O(ℓ) de prereg-003, con sus NOT vinculantes (§2) intactos.
6. Resultados negativos 2: cascada de objeto extendido (expansión S1/S2, reseed S3) y cierre
   R-VAR — dos objetos independientes contra el mismo muro geométrico, con la lección
   (nulo MINK degenerado en caja alta) como hallazgo, no como vergüenza.
7. Límites y trabajo abierto: minimax sobre `C` (dirección DPI equivocada, prereg-003 §7),
   caveat regular-BH de la ruta 1, finitud del parche.

**Pasos:**
- E1.1 Descarga de deuda O4 (ver Eje 3): meter Tsybakov 2009 y Bretagnolle–Huber en
  `biblioteca/` antes de citar el marco Le Cam (prereg-003 §7 lo exige explícitamente).
- E1.2 Borrador en `docs/paper/` (no commiteado hasta revisión).
- E1.3 Pase de `/auditor` sobre el borrador: cada número del texto → file:line/commit, o
  `[UNVERIFIED]`.
- E1.4 `/comite` para la decisión de publicación (arXiv es one-way).

## Eje 2 — Fase 2 del roadmap: horizonte aparente (ruta 2 de EGS) → prereg-004

**Racional — por qué este es el experimento correcto ahora y no otro:**
- Es literalmente la fase 2 ya planificada en `docs/roadmap.md` ("Phase 2 — apparent horizon"):
  no es un giro improvisado post-derrota, es retomar el plan maestro donde la rama PR-003 lo
  dejó.
- Físicamente superior a la ruta 1: la expansión discreta `E` cambia de signo en r=2M, es
  **local**, y **sobrevive a agujeros negros regulares** — elimina de raíz el caveat
  singularity-specific que limita todo lo conseguido hasta ahora.
- **Incorpora la lección de R-VAR por diseño, no por parche:** la definición de la ruta 2 exige
  sustracción de baseline Minkowski obligatoria (roadmap, ruta 2). El modo de fallo que mató
  R-VAR dos veces (nulo MINK cuasi-degenerado en la caja alta) está tratado estructuralmente
  en el protocolo del observable.
- Infraestructura parcialmente construida: reducción transitiva + links en GPU ya existen del
  trabajo K-beam (`dev/measure_kbeam_peeloff.py`), backend GPU operativo, higiene de semillas
  con bandas ya establecida.

**Pasos (dev primero, congelar después — como siempre):**
- E2.1 Exploración dev (semillas EXPLORE_POOL): links → detección de ladders → expansión
  discreta `E` → medir el cambio de signo en BH vs baseline MINK. Riesgo conocido: la
  convergencia de mean(E) necesita muchos sprinklings (roadmap lo avisa); el GPU lo mitiga.
- E2.2 **La geometría del parche es variable de diseño declarada** (caja vs diamante causal),
  decidida en dev con anclaje físico ANTES de cualquier freeze. Esta es la aplicación legítima
  de la lección R-VAR: una prereg nueva puede elegir geometría nueva con base de principios;
  lo prohibido era re-tunear la vieja sobre semillas vistas. Nota: esta decisión puede
  subsumir el ítem C2 (caja alta `t*/r_S∈[0,50]`) aparcado en prereg-003 §7.
- E2.3 `/comite`: definir el objeto (criterio falsable = "el cambio de signo de E localiza
  r_S dentro de K·ℓ"), umbrales anclados a bases de principio, gate de falsación.
- E2.4 Congelar prereg-004 con banda de semillas virgen nueva (disjunta de DEV, de las 20
  quemadas de 001 y de la banda 002 consumida).
- E2.5 Validación ciega única. Verdicto congelado, sea cual sea.

## Eje 3 — Deuda barata, en paralelo

- **O4 (bloquea E1.1):** conseguir Tsybakov 2009 (Thm 2.2) y Bretagnolle–Huber a
  `biblioteca/` + nota derivada. Horas, no días.
- **Minimax sobre `C`:** se mantiene como problema abierto declarado en el paper. Solo sketch
  dev si alguien tiene una idea concreta; no es camino crítico.
- **Higiene del working tree (minutos, hoy):** `INSTRUCCIONES.md` modificado (1 línea) —
  revisar y commitear o revertir; decidir destino de los `.als` sueltos en raíz
  (`completion_maximality_smoke.als`, `poset_smoke.als`, `modelo contraejemplo.als` →
  `docs/alloy/` o borrar), `Esquema completo.png` (+ borrar el `:Zone.Identifier`), y
  commitear o ignorar `.claude/skills/alloy_verifier/`.

## Orden recomendado

1. **Hoy:** higiene del working tree (E3, minutos).
2. **Esta semana:** O4 (E1.1) + arranque del borrador del paper (E1.2). El paper es el
   entregable de julio: consolida todo lo ganado sin riesgo nuevo.
3. **En paralelo o después:** exploración dev de la Fase 2 (E2.1-E2.2) — reversible, sin
   comité hasta tener señal medida en dev.
4. **Cuando haya señal dev:** comité de definición (E2.3) → prereg-004 (E2.4-E2.5).

Cada paso marcado `/comite` o "congelar" requiere autorización explícita del PI; nada de este
plan la sustituye.
