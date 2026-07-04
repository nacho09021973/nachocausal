# Hoja de ruta — 24 jun 2026 · PR-003: construir un trozo de horizonte tras `BARE_RELOCALISATION`

> **Plan REVISABLE, no congelado.** No es una pre-registración y no fija ningún umbral vinculante.
> Las reglas y los criterios que aquí se nombran se congelan formalmente, cada uno en su documento
> sellado, **antes** de cualquier paso *committing* (reglas fundacionales en `CLAUDE.md` y
> `docs/preregistration.md`). Sucesora de `docs/hoja_de_ruta_23_jun_2026.md`. Avalada por
> `docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md`
> (`COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_CAVEATS`).

## Punto de partida (verificado, 24-jun-2026)

- **prereg-002 `PASS`**, sello `6e2c3888…` (`make verify-seal` = `docs/preregistration_002.md`):
  localización *order-only* del borde asociado al horizonte en un parche finito 1+1D, a ciegas.
  *(Nota 2026-07-04: status actualizado a `PASS [PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED;
  BLINDNESS_DOCUMENTARY_ONLY]` — ver `docs/prereg002_reverification_result.md`.)*
- **Pregunta del 23-jun CERRADA** (exploratoria, 6 semillas; `dev/measure_truncated_head.py`,
  `dev/PR003_NEAR_HORIZON_NOTES.md`): *¿una cabeza truncada order-only es conexa y se queda O(ℓ)?*
  Veredicto **`BARE_RELOCALISATION`**: la cabeza adherente existe (conectividad 100 %) pero es solo
  el vecindario de discreteness de la semilla — k\*=O(1) rungs (3/2/3), k\*·ℓ se halva con ℓ
  (0.134→0.067). El canal de detectabilidad order-only (`rel_phi`) es un **ABSTAIN** (ambiguo;
  greedy sin potencia n=2/8/1).
- **Lo que dice la física (literatura CONFIRMADA, EGS arXiv:2605.06813 md:443,474):** `r_S` es una
  órbita nula **marginalmente inestable** → un trazador *único* hace *peel-off* tras O(1) rungs. Por
  tanto un solo segmento order-only **no puede** alargarse sobre el horizonte; **no es un defecto a
  ajustar, es la cota**. La cola en unidades de ℓ crece de verdad (probado: no es artefacto de
  presupuesto; fracción completa 89/93/87 %); su divergencia *física* (vs ℓ) queda indeterminada.
- **Conclusión de marco:** la meta de PR-003 ("devolver un subconjunto ordenado que *es* un trozo
  de horizonte") **no está refutada; está acotada en escala**. La única vía computable a un objeto
  *extendido* es el **re-sembrado iterativo a trozos** que EGS dejó "para trabajo futuro" (md:443).

## Disciplina que gobierna TODA fase (pre-comprometida, no negociable)

Cada medición de cualquier fase es **dev / reversible**, semillas solo de `EXPLORE_POOL`
(`dev/explore_seeds.py`), nunca toca la banda virgen `RESERVED_002 [2_000_000,2_999_999]`,
`nachocausal/thresholds.py` ni el camino sellado. `make verify-seal` debe seguir dando
`6e2c3888…` antes y después. Toda regla nueva pasa el **leakage gate** (`docs/pr003_leakage_gate.md`,
5 contratos). Antes de poder *llamarse resultado*, cualquier construcción cumple el **test mínimo de
falsación** del comité:

- **(a) sin artefacto de búsqueda:** la agregación *complete-only* coincide con la de todas las
  escaleras (filtrar por `complete==1`, no solo `longest_censored`).
- **(b) invariancia bajo relabel:** un **Guard-v sobre el conjunto construido** (análogo a
  `boundary_minimals_invariant` / `verify_order_only`) no falla.
- **(c) control plano:** el mismo *cloud* en MINK (no-BH) **no** produce un locus adherente
  persistente.

Y la trampa de EGS, explícita: **`r` solo puntúa, nunca siembra ni selecciona**. En el re-sembrado,
la anticadena siguiente se elige solo con cantidades derivadas de `C`; nada de dónde cayó en `r` la
cabeza anterior (contrato #5). Nada se congela sin `/comite` + `/auditor`.

## La cascada (frontera: no sabemos la respuesta; avanzamos y aprendemos)

El orden es **#1 → #2 → #3**, pero con *puertas de decisión* explícitas y ramas de aprendizaje: si
#1 o #2 fallan, lo aprendido puede abrir un modo de seguir distinto al simple "pasar a la siguiente".

### Fase #1 — Re-sembrado iterativo order-only (la apuesta principal)

- **Pregunta:** ¿concatenar brackets order-only sucesivos —cada uno sembrado en una anticadena al
  futuro de la cabeza anterior— produce un locus **a trozos** que se mantiene O(ℓ) **por tramo** y
  cuya cobertura/persistencia **converge** al refinar la densidad?
- **Método (dev):** semilla order-only desde el bracket v2; construir la cabeza adherente (la pieza
  O(ℓ) ya observada); identificar una anticadena futura **solo con `C`**; re-sembrar; repetir.
  `d_⊥` solo puntúa. Medir por tramo: adherencia O(ℓ), conectividad entre piezas, cobertura del
  arco de `r_S` dentro del parche, y su tendencia con densidad. Smoke primero.
- **Éxito:** los tramos cubren un arco de `r_S` mayor que la cabeza sola, cada tramo O(ℓ), y la
  cobertura no se degrada (idealmente mejora) con densidad — pasando (a)(b)(c).
- **Falla:** las piezas no se encadenan (huecos que no cierran), o la unión no cubre más que la
  cabeza, o (b)/(c) falla (depende de etiqueta, o aparece en MINK).
- **Qué aprenderíamos aun fallando:** si las piezas son adherentes pero **inconexas**, el objeto
  natural deja de ser una *curva* y pasa a ser una **banda/antichain order-only** del horizonte →
  abre una vía distinta (reconstruir el horizonte como conjunto, no como escalera) que no estaba en
  la cascada. Registrar y reconsiderar antes de ir a #2.
- **Fase #1-B (24-jun-2026, exploratoria, 6 semillas; `dev/measure_expansion_horizon.py`,
  `dev/PR003_EXPANSION_NOTES.md`) — el diagnóstico CANÓNICo de EGS, a ciegas: PARCIAL.** Pivote
  avalado por `biblioteca/Anticadenas_Benincasa.md` + EGS arXiv:2605.06813. Localiza el horizonte
  aparente por el **cambio de signo de la expansión discreta** (Eq. 14: pares de escaleras difusas,
  cambio logarítmico de una **separación transversal order-only** = √|menor diamante que las
  encierra|); `r` solo puntúa dónde cruza cero. **A 3600 (POSITIVO):** mean(E) negativa dentro de
  R_S y positiva fuera, cruce **r\*=0.491 / por-semilla 0.503**, **d⊥=0.72 ℓ**; control plano MINK
  **PASA** (sin convergencia interior ni cruce → señal específica del BH). Reproduce Θ_out=0 en R_S
  a ciegas — el signo más fuerte de PR-003. **PERO a 7200 DEGRADA:** la negatividad interior
  desaparece (submuestreo del interior), cruce pooled indefinido, d⊥ sube a **1.60 ℓ**, contraste
  +0.134→+0.071. **No cumple "no degradar con densidad"** → la convergencia **no** está establecida.
  dev/v0, puntuado con `r` oculta — no congelado, no validado, no auditado. *Incertidumbre abierta:*
  si la señal interior puede hacerse robusta a densidad (muestreo vs proxy vs intrínseco).
- **v0 previo (volumen-O) — `dev/measure_iterative_reseed.py`, `dev/PR003_ITERATIVE_RESEED_NOTES.md`:
  signo POSITIVO preliminar (validación cruzada independiente del diagnóstico de expansión).** v0 = re-localizar el borde
  v2 sellado en cada frente temporal order-only (niveles de `L_past`, anticadenas genuinas) y apilar
  los puntos. A 3600/7200: **96→146 frentes localizados/semilla** (cobertura ≫ la cabeza, crece con
  densidad), **d_⊥ por pieza 0.52→0.63 ℓ** (O(ℓ); el trazador único derivaba a 4–8 ℓ), **conexo
  90→95 %** (mejora), scatter robusto IQR 0.042→0.031 (baja), **Guard-v relabel 6/6** y **control
  plano MINK PASA** (sin horizonte el localizador da ~4 frentes sueltos a 6–8 ℓ → señal específica
  del agujero negro). Cumple (a)(b)(c) a nivel preliminar. **Caveats:** `covers` R_S 74→65 % (cola
  de outliers, std 0.097→0.071 algo > θ_stab), 2 densidades (no es prueba de convergencia), "conexo"
  es enlace entre frentes adyacentes, y la localización por frente **reutiliza** el localizador v2
  (el avance es el subconjunto ordenado conexo, no un principio nuevo). dev/v0, puntuado con `r`
  oculta — **no congelado, no validado, no auditado**; antes de comprometer: endurecer (3ª densidad
  + tratar frentes no-cubrientes) y `/comite` + `/auditor`.
- **S3 (24-jun-2026, ENDURECIMIENTO de v0; `dev/measure_iterative_reseed_v1.py`,
  `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`, `dev/iterative_reseed_v1.log`) — NO CONVERGE.** 6 semillas,
  3ª densidad 14400 + la puerta `τ(n)` **ya congelada** como regla de parada order-only, contando
  frentes que abstienen/degeneran como *miss* (corrige el sesgo abstain-a-excluir del falsador). Sello
  `6e2c3888…` antes y después. **Veredicto: la cobertura SE DEGRADA con densidad** — HONESTA
  51→48→**44 %**, OPTIMISTA (v0) 74→65→**54 %** (monótona en las 3 densidades); **d⊥/ℓ crece
  0.52→0.63→0.88** (d⊥ físico se estanca ~0.020, no se afila respecto a ℓ). Bajo la vara
  pre-comprometida "no degradar con densidad" (líneas 64,80) esto es **FALLO de convergencia**.
  *Lo que sí sobrevive (honesto, no rescata el veredicto):* anchura crece (96→146→**234** frentes),
  conexo 90→95→93 %, IQR robusto baja 0.042→0.030 (< θ_stab), **Guard-v 6/6** y **control MINK PASA**
  en las 3 densidades, y **`τ(n)` ES una regla de parada order-only que funciona** (los frentes que
  abstiene *cubrirían* solo 40/37/35 %, muy por debajo del 74/65/54 % localizado → descarta la cola
  no-cubriente; responde afirmativamente a la pregunta de Fase #2) — pero **no basta** para hacer
  converger la cobertura. Misma fragilidad a densidad que EGS marca como problema abierto del método
  de escaleras (md:469); el re-sembrado **hereda, no escapa** la truncación interior (igual dirección
  que el expansion S1/S2 NEGATIVO). dev/v0–v1, puntuado con `r` oculta — no congelado/validado/auditado.
  **Consecuencia (pre-comprometida en `comite_decision_002` §9): S3 no aguanta ⇒ PR-003 entra en
  Fase #3** (aceptar la cota `BARE_RELOCALISATION`). Etiqueta honesta del re-sembrado v0+v1:
  **INCONCLUSIVE-como-objeto-extendido / NEGATIVO en convergencia**.

### Fase #2 — ¿Existe una regla de parada order-only? (si #1 no basta)

- **Pregunta:** ¿hay **algún** observable order-only (no solo `rel_phi`) cuyo *breakpoint* coincida,
  de forma robusta a densidad, con el fin geométrico de la cabeza `k*`?
- **Por qué después de #1:** es la precondición para **congelar** cualquier regla de truncación/#3;
  sin ella no hay corte order-only defendible. Si #1 ya da un criterio de parada natural (la pieza
  "se agota" sola, como el greedy pero con potencia), #2 se subsume.
- **Método (dev):** barrer familias order-only (L_fut/L_past, cardinalidades de intervalo,
  volúmenes truncados, `O` a lo largo de la escalera) y medir alineación del breakpoint con `k*`
  bajo el barrido de densidad. `k*` se usa **solo para puntuar** la alineación, nunca para definir
  la regla (si no, es fuga).
- **Éxito:** un observable con breakpoint alineado y estable → candidato a regla #3 congelable.
- **Falla (null limpio):** ningún observable order-only marca el fin de la cabeza de forma robusta.
- **Qué aprenderíamos aun fallando:** un null robusto **es** un resultado: diría que el fin de la
  cabeza **no es detectable desde el orden** a esta escala — refuerza que el objeto reconstruible es
  intrínsecamente la pieza O(ℓ), y empuja hacia #3 con una afirmación más fuerte y honesta.

### Fase #3 — Aceptar la cota y consolidar (si #1 y #2 no extienden) — **ENTRADA 24-jun-2026**

> **Estado: ACTIVA.** La cascada #1/#2 no produjo un objeto extendido *que converja*: expansión
> #1-B PARCIAL → S1/S2 **NEGATIVO** (`dev/PR003_EXPANSION_ROBUSTNESS_NOTES.md`); re-sembrado v0
> POSITIVO preliminar → **S3 NO CONVERGE** (cobertura honesta 51→48→44 %,
> `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md`). La pregunta de #2 quedó respondida de paso: `τ(n)` **sí**
> es una regla de parada order-only que funciona (descarta la cola no-cubriente), pero no extiende el
> objeto. Conclusión: el objeto reconstruible es intrínsecamente la pieza O(ℓ) de
> `BARE_RELOCALISATION`. Se entra en #3.

- **Acción:** tratar `BARE_RELOCALISATION` como **el resultado de escala alcanzable** y dejar de
  perseguir un objeto extendido. Redirigir el esfuerzo a: (i) afirmar la regla de dirección #2
  (`relphi_mean`) **en** la banda del horizonte (hoy solo 1/6/2 salientes) — `docs/hoja_de_ruta_23_jun_2026.md`
  punto 2; y/o (ii) redactar el plan PR-003 (punto 4) como **afirmación de localización a escala
  acotada** (un trozo O(ℓ) de horizonte, no una curva creciente), en forma sellable.
- **Hecho cuando:** el plan PR-003 está escrito en forma congelable, con semillas dev/validación
  disjuntas y banda virgen reservada, listo para `/comite` y, tras su visto bueno, sellar.

## Primeros pasos reversibles (de registro, antes de la primera medición de #1)

- **R1.** Extender el chequeo de completitud a las 6 semillas y añadir fracción-completa por
  densidad + dispersión por semilla a la salida de `dev/measure_truncated_head.py` (hoy solo
  *pooled*; el comité corrió el chequeo a 1 semilla: 89/93/87 %).
- **R2.** Etiquetar en `dev/PR003_NEAR_HORIZON_NOTES.md` el canal order-only como **ABSTAIN**
  (separado del resultado geométrico) y dejar constancia de que la cola no es artefacto de
  presupuesto pero su divergencia física sigue indeterminada con 3 densidades.

## Vigilancia

- **`/comite`** antes de congelar cualquier regla (#2/#3) o el plan (#4).
- **`/auditor`** (`make audit`) antes de construir sobre cualquier número ya medido.
- Toda exploración en `dev/` (scripts commiteados, datos crudos no); la confirmación, en la ruta
  sellada. La separación es de **rutas de código y semillas**, no de git.

## Roadmap global

**localización del borde ✅ → (cota medida: la cabeza adherente es O(ℓ)) → ¿locus a trozos order-only
que cubra un arco de `r_S`? (#1) → regla de parada order-only / o aceptación de la cota (#2/#3) →
convergencia bajo extensión del parche → 3+1D.**
