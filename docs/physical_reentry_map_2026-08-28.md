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
Prop. 3.4: este diseño es **no regular** para Fisher
(`docs/manuscript_limits_draft.md:552-558`).

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
| Orden = orden producto de dos nulas | **No.** En `(t*,r)` el orden no es el producto de las coordenadas. | WP6 dicotomía §1; prereg 001 :61 |
| Densidad = factor conforme `Omega` | **No en esas coordenadas.** `det g=-1` ⇒ volumen de Lebesgue en EF; la geometría está en los conos, no en la densidad de sprinkling. | manuscript_limits :235-245, :553 |
| PIT / cópula como isomorfismo de orden | **No.** El PIT exige caja nula con marginales estrictamente crecientes. | WP6 dicotomía Lema A; R4 §7bis |
| Dominio = rectángulo nulo fijo | **No.** El rectángulo EF, en nulas, **mueve el soporte** con el parámetro. | Prop. 3.4 :552-558 |
| Fisher de un tangente conforme en `ε=0` | **No definido** sobre el parche A (QMD falla). | Prop. 3.4 |
| Canal `Pi_N → [P]` sobre permutación de rangos | Solo tiene sentido nativo en parche B o C. | S1 §5.2; Teorema 8 |
| Observable de truncación `O` / futuros | Es el del PASS sellado; **no** es el score Fisher de S2. | prereg 001; prereg 002 result |
| Señal de incompletitud geodésica | Presente en A (PASS vs MINK); falla Hayward. Ausente por construcción en C. | C3-early; EGS |

**Falsificador: se activa para la identificación ingenua S2 = benchmark.**
El cambio de dominio destruye la estructura (producto nulo + PIT + QMD)
que permitía el análisis S1/S2. No se fuerza el puente.

```text
BENCHMARK_COORDINATE_BRIDGE = OPEN
NAIVE_S2_EQUALS_SEALED_BENCHMARK = REFUTED_BY_EXISTING_RECORD
NO_NEW_RUNS_REQUIRED_FOR_THIS_NEGATIVE
```

Este negativo **ya estaba** en R4 §7bis, Prop. 3.4 y el comité 049.
Esta auditoría no lo descubre: lo **nombra como obstáculo de reentrada**.

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
antes el cambio de dominio que Prop. 3.4 dice que no es regular.

## 4. Obstáculo físico siguiente, ya documentado

No es «correr otro estimador». Es este, y ya está escrito:

> El instrumento sellado vive en un rectángulo EF **no regular para
> Fisher** (Prop. 3.4), y su señal `O` es de **truncación / funnel de
> singularidad** (Hayward), no el tangente de cópula de S2. El único
> parche Schwarzschild que *sí* es caja nula es la familia de diamantes
> de límites, que no es el experimento del PASS y cuya lección es un
> suelo, no una retención.

Eso es el obstáculo de reentrada. No hace falta un run para saberlo.

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
PHYSICAL_REENTRY_AUDIT = COMPLETE_NEGATIVE_ON_NAIVE_BRIDGE
NO_FORCED_BRIDGE
NO_NEW_EXECUTION
```
