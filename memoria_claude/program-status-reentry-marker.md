---
name: program-status-reentry-marker
description: Estado vivo del programa — cerrado 2026-07-30 (deóntico) y REABIERTO ACOTADO 2026-07-31 sólo para R1 (paper de límites) y R2 (derivar λ⁶); caja de 6 semanas. Punto de reentrada — LEER PRIMERO antes de proponer cualquier paso
metadata: 
  node_type: memory
  type: project
  originSessionId: ba8e0f66-5e67-49f8-a0fa-d7165b974d41
  modified: 2026-08-16T09:21:13.337Z
---

Sustituye al marcador de pausa del 2026-07-19 (pausa → cierre → reapertura acotada).

**Cierre 2026-07-30.** `docs/program_closure_note_2026-07-30.md`, base
`docs/comite/comite_decision_049_program-closure-adjudication.md §11`, firmado por el PI, tag
`program-closed-2026-07-30` en `bcd4633`. Es **deóntico, no alético**: retira autorización para
ampliar el programa bajo su objetivo fuerte; NO afirma que no exista camino legítimo.

**Reapertura acotada 2026-07-31 (decisión del PI, confirmada por él el 2026-08-01).**
`docs/program_reopening_note_2026-07-31.md` — **vive sólo en la rama
`reopen/r1-r2-limits-writeup`, NO está en `main`** (a 2026-08-01). Estado
`REOPENED_BOUNDED / WRITE_UP_ONLY_PLUS_ONE_DERIVATION`. No revoca el cierre; restaura autorización
para **dos ítems y nada más**:
- **R1** — llevar `docs/manuscript_limits_draft.md` (~1.280 líneas, Teoremas 3.8 suelo de
  localización order-only N1 y 3.9, correcciones `R-A1`–`R-B2` aplicadas) a PDF sometible. Es
  redacción, no investigación.
- **R2** — derivar analíticamente el exponente `λ⁶` de `wp4_fisher_localization_floor.md §5a`
  (ley empírica `κ ~ λ⁶`, exponente 5.9–6.0; vía plausible: expansión near-horizon/Rindler).
  Día 1 (`91a84ac`): exponente derivado y cross-checked, **prefactor aún abierto**.

**Cajas de tiempo (duras, sin prórroga):** R1+R2 seis semanas desde 2026-07-31 → ~2026-09-11.
R2 tiene tope propio de dos semanas → ~2026-08-14; si no sale, se marca abierto y se pasa a R1.
**R2 no puede bloquear R1** (§4.4 de la nota).

**Why:** el cierre acota la prohibición al objetivo de reconstrucción de horizonte; R2 se autoriza
porque es un **límite sobre** la localización cerca del horizonte —dirección opuesta— y su diana
numérica ya existe. El PI declaró esa tensión en la propia nota en vez de disimularla.

**How to apply:**
- Perímetro fijo R1/R2. Nada entra sin nueva nota firmada. Todo hallazgo fuera de perímetro va
  fechado a `docs/backlog_hallazgos.md`, nunca al trabajo en curso.
- **Sigue cerrado:** reconstrucción de horizonte 1+1D/3+1D en cualquier reformulación; PR004;
  localizadores C1–C6; anclas de presente; ladder-braiding; diagnósticos de rescate; `Q_trap` v2
  (`UNADJUDICATED_AT_CLOSURE`, no se reconvoca); nuevos observables/WP fuera de R2; simulaciones;
  validaciones.
- **Semillas: ninguna.** La banda virgen `[2.000.000–2.999.999]` no se toca.
- **Lenguaje de novedad absoluta: prohibido** (cláusula 2 del cierre). `NOVELTY_CERTIFIED = NO`;
  `PRIOR_FOR_N1 = NOT_FOUND_BY_EITHER_READER` **no** es un certificado.
- Reapertura **append-only**: sello, terminales, pruebas e historial no se alteran.
  `nachonumero` pinea `nachocausal@bcd4633` vía `verify_herencia.py` — **ese commit no se toca**.
- Cifras publicadas (`V ≈ 1.4717`, `I ≈ 5.415e-4`, `κ ≈ 7.97e-4`, `δ_τ/ℓ ≈ 35.4`) deben ser salida
  literal de `wp4_kappa_numeric_reference.py` re-ejecutado, con error de cuadratura declarado y no
  presentado como exacto — ver [[numbers-must-come-from-committed-script]].

**Actualización 2026-08-16 (rama `research/f2-f3-chain-distance`).** R2 cerrado como **abierto**:
exponente derivado y cross-checked, **prefactor `OPEN / [UNVERIFIED]`**; caja vencida el
2026-08-14, pasa a R1 (commit `44b0d75`, ítem C-3 del foro-001). Nueva nota firmada
`docs/scope_note_2026-08-16_foro001_falsification_test.md` que levanta la prohibición de ampliar
`n` **sólo** para el test `FORO001-F1` (el `R-1` del foro-001; ojo con la colisión de nombres
`R-1` vs `R1`). Ejecutado (`7b5deec`): 560 de 112.911.876 tuplas falsifican los tres disyuntos → se emitió
`REFUTED` y **se retractó el mismo día** (`0afc16c`,
`docs/c1_correction_2026-08-16_realizability.md`): los 560 emparejan filas/columnas prohibidas por
la prescripción `F_n` (el testigo usa `(11,11)` cuando `F_n` fija `11→7`). Restringido a las
11.639.124 cadenas realizables, sólo 40 de las 1504 no vacuas sobreviven y las 40 caen en
`loss_case` → `COMPATIBLE_FAILURES=0`. **`C1` sigue `INCONCLUSIVE`**, con evidencia positiva
acotada. **Lección:** el test sellado (y el predicado que firmamos a partir de él) cuantifica
sobre cuádruplas **abstractas**, que es el dominio equivocado — precomprometer un predicado no lo
hace correcto. El test sellado no se tocó y sigue pasando (su `n=12` es vacuo, 245025/245025). **`C-1` adjudicado** el mismo día
(`docs/c1_adjudication_2026-08-16_ef4_token_degradation.md`, commits `4c22025`+`c9a891d`):
`EF4_CORRECTED_PRESCRIBED_FAMILY = SKETCH_GEOMETRIC_CORE_REFUTED_AS_STATED`,
`EF4_Q2_ASYMPTOTIC = PROVED_DEDUCTIVE_NO_EXECUTABLE_BACKING_CONDITIONAL_ON_REFUTED_TRICHOTOMY`,
`MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED` restituido — **corregidos** por la retractación:
vigentes son `EF4_CORRECTED_PRESCRIBED_FAMILY = SKETCH_PENDING_INDEPENDENT_AUDIT_COMITE_050`,
`EF4_Q2_ASYMPTOTIC = PROVED_DEDUCTIVE_NO_EXECUTABLE_BACKING`,
`GEOMETRIC_TRICHOTOMY_EF4_3_ABSTRACT_DOMAIN = REFUTED_AT_N24`,
`GEOMETRIC_TRICHOTOMY_EF4_3_ON_F_N = NOT_REFUTED_AT_N24`. La degradación **sobrevive por el motivo
procedimental** (orden vigente del comité 050, nunca levantada), no por el sustantivo. Ningún
token sube. **Reserva clave (backed, `0f1db5e`):** las escaleras del test tienen `rho-1` puntos, así
que a `rho=2` la **contención parcial es imposible para todo `n`** — y la contención parcial es lo
que ejercita los topes de `loss_case`. Luego el `COMPATIBLE_FAILURES=0` de `n=24` no toca el núcleo
del análisis de casos. Sumado a `n=12` vacuo, `n=30` (`rho=2`) y `n=34` (`rho=3`, 0 casos
parciales), **la lógica de escaleras nunca se ha ejercitado**. Los datos de `n=30`/`n=34` están en
`docs/backlog_hallazgos.md` como **`[UNVERIFIED]`** (no salieron de script commiteado). Siguiente
paso propuesto y **no autorizado**: localizar el menor `(n,rho)` no vacuo con un caso compatible de
contención parcial y barrer allí; exige nota firmada por §4 de la nota de alcance.
`C-5` sigue en pie: PR #4 no sale de draft.

**C6 cambió de estado — la nota vieja decía BLOCKED y ya no es cierto.** Entre 2026-07-21 y el
cierre, C6 se cerró y se promovió a **teorema de manuscrito** (`141cccc` cierra el resto uniforme,
`861d5e5` lo promueve), con teorema de separación *dimension-free* a fixed-n y auditoría de
prioridad sobre C6/Teorema 3.9. Aun así, la **línea de localizadores sigue clausurada** por §3 de
la nota de reapertura: C6 es resultado escrito, no vía viva.

Relacionado: [[prereg002-pass-artifact-gap]] (el PASS sellado de 1+1D sigue siendo el activo
positivo), [[pr003-fase3-lecam]], [[estimator-v2-exploration]], [[memoria-claude-sync]].
