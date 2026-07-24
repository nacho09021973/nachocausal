# Hoja de ruta — 24 jul 2026 · ficha bibliográfica TV order-only y próximos pasos

> **Plan REVISABLE, no congelado.** No es pre-registración, no fija umbrales, no autoriza
> ejecuciones ni implementaciones por sí mismo. Mantener `RESPECT_SEAL_FREEZE`,
> `NO_RECONSTRUCTION_CLAIM`, `NO_GROUND_TRUTH_LEAKAGE`, `NO_POST_HOC_TUNING` y
> `NO_THRESHOLD_LOOSENING`. No es una `hoja de ruta` sustituta de las anteriores
> (`docs/hoja_de_ruta_23_jun_2026.md` a `docs/hoja_de_ruta_27_jun_2026.md`, `docs/roadmap.md`) ni
> del marcador de pausa; es un registro de sesión, siguiendo la misma convención (una por fecha).

## 0. Relación con la pausa del programa

El programa sigue en `PROGRAMA_EN_PAUSA_LIMPIA` desde `docs/marcador_reentrada_2026-07-19.md`
(firmado PI, 2026-07-19): sin ejecución pendiente, nada abandonado, único siguiente paso
*autorizado a considerar* si se retoma es convocar `/comite` para la corrida del falsifier
enumerativo de OP-2.2 — **no autorizado aún**. El trabajo de esta sesión (§1-§2 abajo) es
**bibliografía y matemática de búsqueda, no una reapertura del programa**: no toca
`nachocausal/thresholds.py`, no ejecuta ningún script, no genera datos de validación, no
reabre Candidate B ni C1-C7. Es exploración documental en `research_program/bibliography/`,
compatible con la pausa tal como está.

## 1. Qué se hizo hoy

1. **Ficha bibliográfica** `research_program/bibliography/ficha_se_busca_tv_order_only.md`
   (v1→v3): especificación de la búsqueda de un teorema o puente que dé Forma L (cota inferior),
   Forma U (barrera uniforme) o Forma D (comparación de experimentos) para
   `TV(Q_{lambda,theta}, Q_{lambda,theta'})` en el canal order-only. Ancla en WP4,
   `first_witness_pair_candidates.md` §4, OP-1.2 y PR012.
2. **Auditoría** `docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md`:
   `AUDIT_PASS_WITH_WARNINGS` (0 errores, 3 warnings propios de la ficha + 23 mecánicos
   preexistentes del repo). Los 3 warnings — resumen de PR012 omitiendo las filas
   `GRID_RESOLUTION_ABSTAIN`, matemática elemental inline sin respaldo, inconsistencia de
   etiquetas `CONFIRMED_TOOL_ONLY`/`NOT_APPLICABLE` — corregidos en la misma sesión (v2).
3. **Primer disparo del coto 1** (Malliavin–Stein / Poisson), dos resultados leídos íntegros y
   guardados en `biblioteca/` (git-ignorada, no commiteada):
   - **Janson 2011** (arXiv:0902.0306, Teorema 7.1 + Lema 6.6): da la recíproca general que
     OP-1.2 §7 marca como no usada — igualdad de leyes de poset **para todo `n`** ⟺ distancia de
     corte `delta_□ = 0` ⟺ (con hipótesis extra de no-gemelos) isomorfismo módulo nulos. Candidato
     a promover la rigidez de cópulas de FWP §4 a lema citado (lo que pedía PR012 §9), en un
     régimen («toda la escalera») distinto del `n` fijo o `lambda->infinito` de esta ficha.
   - **Reitzner–Schulte 2013** (Ann. Probab. 41(6), arXiv:1104.1039, Lema 3.5 + Teoremas 4.7/5.2):
     CLT cuantitativo para U-estadísticos de Poisson de orden 2 con tasa explícita
     `d_W <= C_f*lambda^{-1/2}`, uniforme en el parámetro cuando el kernel no depende de él —
     exactamente el caso del candidato 7.1 (número de pares comparables, kernel
     `f(x,y)=1[x prec y]` fijo). Reduce ese candidato a una única desigualdad escalar por
     verificar, `p(theta) != p(theta')`, sin resolverla.
4. Ficha actualizada a v3 con ambos hallazgos (§2.1, candidato 7.1, tabla §8), commiteada.

## 2. Próximos pasos (ninguno ejecutado ni autorizado por este documento)

Orden de prioridad, uno cada vez:

1. **Verificar `p(theta) != p(theta')` para un par concreto** (candidato 7.1). Es un cálculo
   simbólico/analítico — una integral doble sobre una cópula ya definida en el repo (candidato
   natural: la familia diamante de WP4 §4, o los pares de OP-1.1/1.2) — **no una ejecución ni una
   implementación de estimador**. Si `p(theta) != p(theta')` se confirma, la cadena de Forma L
   para 7.1 queda cerrada salvo redacción; si `p(theta) = p(theta')`, el candidato quedaría ciego
   para ese par y habría que probar otro (altura/LIS, §7.2) o cambiar de par.
2. **Promoción de la rigidez de cópulas a lema citado** (pedida por PR012 §9): evaluar si el
   Teorema 7.1 de Janson (hipótesis de Borel + no-gemelos) cubre nuestra clase de familias, o si
   conviene mantener el argumento diferencial-geométrico propio (FWP §4, vía escalar de Ricci)
   como razón independiente — son complementarios, no intercambiables.
3. **Cotos de caza 2-4 de la ficha** (LIS/récords no uniformes; límites de posets y conjetura de
   Bombelli; procesos parcialmente observados), en ese orden, solo si (1) no cierra o se busca
   redundancia.
4. Cualquier resultado que emerja de (1)-(3) que parezca cerrar una Forma L/U/D debe pasar por
   `/auditor` antes de tocarse el estado `[PROVED]`/`[OPEN]` de la ficha, y por `/comite` antes de
   promoverse a una decisión que afecte al programa (nueva prereg, reapertura de C7, etc.) — nunca
   directamente a un commit de resultado.

## 3. No hacer

- No ejecutar `dev/pr011_tv_certification_enumeration.py` ni ningún script del banco sellado.
- No tocar `nachocausal/thresholds.py` ni ningún umbral congelado.
- No convocar `/comite` para retomar el programa sin que el PI lo decida explícitamente (el único
  paso que el marcador de reentrada autoriza a *considerar*, no a ejecutar, es el falsifier de
  OP-2.2 — no relacionado con esta ficha).
- No presentar el paso 1 de §2 (verificación de `p(theta)!=p(theta')`) como completado hasta que
  se haga y se audite; hasta entonces sigue `[OPEN por par]` en la ficha.

## 4. Checklist antes de cerrar la sesión

1. `git status --short` debe mostrar solo la ficha, el reporte de auditoría 023 y este documento.
2. `make verify-seal` debe seguir dando `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
3. Los dos PDFs nuevos (`biblioteca/0902.0306v1.pdf`, `biblioteca/1104.1039v3.pdf`) son locales,
   git-ignorados; no deben aparecer en `git status`.
