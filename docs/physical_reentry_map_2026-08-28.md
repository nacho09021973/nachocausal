# Mapa de reentrada física — auditoría, cero ejecución

```text
ESTADO: AUDIT_ONLY — NO_NEW_RUNS
FECHA: 2026-08-28
GOBERNANZA: docs/program_physical_reentry_2026-08-28.md
ANCLA_S2: c0780566d8f42d605e5c3d7dfc59f9327a1425be
SELLO: intacto — no se toca
NATURALEZA: lectura de registro existente. Cero semillas, cero simulacion,
            cero instrumentos modificados.
FALSIFICADOR: si el cambio de dominio destruye la estructura del canal,
              se registra y no se fuerza el puente.
```

Pregunta de esta nota:

> ¿Qué parte del experimento Schwarzschild actual puede ponerse en el mismo
> lenguaje de canal de información que acabamos de cerrar (S1/S2)?

No se afirma que el diamante nulo sea el benchmark.

## 1. Tres parches 1+1 ya en el registro, no uno

Hay que dejarlos separados. El comité 049 ya advirtió que conflacionarlos
es un error (`docs/comite/comite_decision_049_program-closure-adjudication.md`).

**Parche A — benchmark sellado (prereg 001/002).**
Rectángulo EF fijo: `t_edge=6.0`, `r∈[0.1,1.3]`, `r_S=2M=0.5`, área 7.2,
`det g=-1` (`docs/preregistration.md:61-62`,
`docs/preregistration_001_addendum.md:39-40`). Sprinkling uniforme en
`(t*,r)`. Observable `O` (cadena máxima / cardinalidad futura) sobre
minimals. Control: Minkowski con la **misma nube de puntos**.
Resultado: **PASS** acotado en parche finito
(`docs/preregistration_002_result.md:18-75`). No es el horizonte global.
La señal es sensible a truncación de singularidad: C3-early
`REJECTED_HAYWARD` (`docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md:48-53`).
Prop. 3.4 afirma no regularidad para Fisher, pero remite al bosquejo de WP4
Prop. 2; la auditoría 1 no considera cerrada esa prueba
(`docs/physical_reentry_audit_001_2026-08-28.md` §6).

**Parche B — diamantes de límites (Teoremas 3.8–3.9).**
`D_τ = J⁺_τ(p) ∩ J⁻_τ(q)` con esquinas EF fijas, `r_q>0` (singularidad
evitada). En coordenadas nulas `(Ũ,v)` **sí es una caja** que monta el
horizonte (`docs/manuscript_limits_draft.md:246-264`). Ahí hay suelo de
localización order-only y QMD. No es el instrumento sellado.

**Parche C — S1/S2.**
Diamante de Minkowski `1+1` como **punto base**, perturbado conformemente,
caja nula `[0,1]^2`, `mu_0=du dv`, tangente de cópula, score de rangos,
retención Fisher del poset no etiquetado (`c078056`, Teorema 8). Sin
horizonte. Sin singularidad.

```text
SEALED_EF_BOX     !=  LIMITS_NULL_DIAMOND  !=  S2_MINKOWSKI_NULL_BOX
```

## 2. Qué cambia al pasar de la caja nula a `(t*, r)`

| Estructura que S2 usa | ¿Sobrevive en el parche A (sellado)? | Fuente |
|---|---|---|
| Orden = orden producto de dos nulas | **Sí, tras pasar a las nulas globales `(Ũ,v)`.** No es producto en las coordenadas EF originales. | WP4 floor :115-124; auditoría 1 §§5-6 |
| Densidad = factor conforme `Omega` | **No en esas coordenadas.** `det g=-1` ⇒ volumen de Lebesgue en EF; la geometría está en los conos, no en la densidad de sprinkling. | manuscript_limits :235-245, :553 |
| PIT / cópula como isomorfismo de orden | **No transportado literalmente.** Los rangos existen, pero uniformar marginales no convierte el soporte restringido en el cuadrado completo de S1. | WP6 dicotomía Lema A; auditoría 1 §8 |
| Dominio = rectángulo nulo fijo | **No.** El rectángulo EF, en nulas, **mueve el soporte** con el parámetro. | Prop. 3.4 :552-558 |
| Fisher de un tangente conforme en `ε=0` | **No habilitado para el parche A.** No hay puente paramétrico regular; la afirmación adicional de fallo QMD permanece `OPEN`. | auditoría 1 §§6, 9 |
| Canal `Pi_N → [P]` sobre permutación de rangos | **Sí como esqueleto latente a `N=n` fijo.** No identifica por sí mismo la ley paramétrica con S1/S2. | WP4 floor :115-124; auditoría 1 §5 |
| Observable de truncación `O` / futuros | Es el del PASS sellado; **no** es el score Fisher de S2. | prereg 001; prereg 002 result |
| Señal de incompletitud geodésica | Presente en A (PASS vs MINK); falla Hayward. Ausente por construcción en C. | C3-early; EGS |

**Falsificador: se activa para la identificación ingenua S2 = benchmark.**
El orden producto y el cociente por permutación sobreviven, pero el cambio de
dominio no preserva ya demostrado el experimento de soporte fijo, PIT sobre el
cuadrado completo y QMD que S1/S2 necesita. No se fuerza el puente.

```text
DOMAIN_BRIDGE = OPEN
NAIVE_S2_EQUALS_SEALED_BENCHMARK = REFUTED_BY_EXISTING_RECORD
NO_NEW_RUNS_REQUIRED_FOR_THIS_NEGATIVE
MOVING_SUPPORT_QMD_STATUS = OPEN
```

La no rectangularidad ya estaba en R4 §7bis, WP4 Prop. 2 y el comité 049.
La afirmación más fuerte de no-QMD no se promociona: WP4 la presenta como
`sketch` y Prop. 3.4 la repite sin completar la cota Hellinger.

## 3. Qué sí puede ponerse en lenguaje de canal, sin runs nuevos

Sin matemática nueva y sin ejecución:

1. **Parche C (S2)** ya está en ese lenguaje. Cerrado. Herramienta
   estructural, no experimento de horizonte.
2. **Parche B (diamantes `D_τ`)** ya es caja nula. El suelo 3.8/3.9 es un
   teorema de *cuánto no se puede localizar* order-only cerca del
   horizonte, no el PASS de `O`. Traducir S2 a B mezclaría retención
   Fisher de un tangente plano con un suelo de localización en una
   familia que *sí* monta el horizonte. No se hace aquí.
3. **Parche A:** el único canal de información ya medido es
   `O: poset → ℝ` contra el gemelo MINK de la misma nube. Eso es un
   test de truncación, no un Fisher de cópula. El PASS
   (`docs/preregistration_002_result.md:64-75`) permanece lo que era:
   recuperabilidad acotada de una frontera asociada al horizonte en un
   parche finito, no transferencia de S2.

Invariancia marginal / Teorema C (separable ⇔ plano ⇔ invisible a
rangos) vive en **cajas nulas**. Aplicarla al rectángulo EF requiere
antes un puente de dominio y de experimento estadístico que no está en el
registro.

## 4. Obstáculo físico siguiente, ya documentado

No es «correr otro estimador». Es este, y ya está escrito:

> El instrumento sellado vive en un rectángulo EF cuya imagen nula no es
> la caja fija de S1/S2 y cuya regularidad QMD no está cerrada; su señal `O`
> es de **truncación / funnel de
> singularidad** (Hayward), no el tangente de cópula de S2. El único
> parche Schwarzschild que *sí* es caja nula es la familia de diamantes
> de límites, que no es el experimento del PASS y cuya lección es un
> suelo, no una retención.

El primer obstáculo es `DOMAIN_BRIDGE`. No hace falta un run para identificarlo.

## 5. Lo que esta auditoría no decide

Tras el falsificador, las dos vías que R4 y la nota de reingreso
dejaban abiertas siguen abiertas y **no se toman aquí**:

```text
NEXT_PHYSICAL_DECISION = PENDING_PI
  (a) puente matematico al benchmark — teorema nuevo de dominio,
      autorizacion nueva, no es S2, no es S3
  (b) volver al observable de horizonte — otro gate, cero Fisher
      como programa
```

No se abre `2+1`, `3+1`, finite-rank, S3, ni nuevos observables.
T20 sigue fuera.

```text
S2_GEOMETRIC_FISHER_RETENTION = PROVED_BY_ASSEMBLY   (cerrado)
STOP_AFTER_S2 = SI
FISHER_BRANCH_ROLE = STRUCTURAL_TOOL
PHYSICAL_REENTRY = PARTIAL_TRANSPORT_WITH_EXACT_FIRST_OBLIGATION
FIRST_PHYSICAL_OBSTACLE = DOMAIN_BRIDGE
MOVING_SUPPORT_QMD_STATUS = OPEN
NO_FORCED_BRIDGE
NO_NEW_EXECUTION
NEXT_RUN_AUTHORIZED = NO
```
