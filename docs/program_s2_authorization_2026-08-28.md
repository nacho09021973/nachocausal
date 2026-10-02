# Autorización acotada de S2 — y parada inmediata después

```text
ESTADO: FIRMADA — S2 AUTORIZADO, STOP_AFTER_S2
FECHA: 2026-08-28
GOBERNANZA: docs/program_reopening_note_2026-08-28_R4.md §5.3 Nivel 2
LECTURA_S1: docs/s1_closure_reading_2026-08-28.md
ANCLA_S1: 2219f21dea2cbd82ba9d959a6d55e1cf87a0bcf6
NO_REVOCA: docs/program_closure_note_2026-07-30.md
SELLO: intacto — no se toca
SEMILLAS: banda virgen [2,000,000–2,999,999] permanece sin quemar
NATURALEZA: documental y de gobernanza. Cero semillas, cero simulación,
            cero matemática nueva.
```

Esta nota es la decisión explícita del PI que R4 §5.3 Nivel 2 exigía.
No reabre R4. No enmienda `2219f21`. No toca T20.

## 1. Las dos opciones, y la elegida

1. Cerrar el resultado teórico redondo: autorizar S2 y ensamblar el
   teorema autónomo.
2. Parar la rama aquí y volver al objetivo físico de nachocausal.

Se elige **(1), sólo hasta S2**. Después, frontera fuerte y decisión
desde cero sobre qué sirve a nachocausal.

## 2. Qué se autoriza

S2 es **redacción de un teorema autónomo de ensamblaje**, no una
campaña de matemática nueva. El límite Fisher (11.6) ya se sigue de
S1 + Teorema 5 + Teorema 7 + Lema 11.2. S2 eleva esa composición a un
solo enunciado, con hipótesis, experimento estadístico y claim ceiling
formulados de una vez.

Cadena autorizada, y sólo esa:

```text
geometria 1+1
  -> tangente de copula
  -> score de rangos simetrico
  -> teorema combinatorio ya probado
  -> retencion Fisher para Pi_N -> [P_Pi_N]
```

El experimento local está construido sobre un diamante de Minkowski
`1+1` como **punto base**, perturbado conformemente por `g_epsilon`.
El punto `epsilon=0` es plano; las perturbaciones con
`P psi != 0` no tienen por qué serlo.

Claim ceiling: hoja de ruta §3.2 y R4 §6. Entregable: hoja de ruta §3.3.

```text
S2_SCOPE = WRITE_UP_OF_ASSEMBLED_CHAIN
NO_NEW_MATHEMATICS
NO_RATE_IMPROVEMENT
NO_PRIORITY_CLAIM
NO_BENCHMARK_TRANSFER_CLAIM
NO_HORIZON_CLAIM
```

## 3. Frontera fuerte al cerrar S2

```text
S2 cerrado  =>  no S3 automatico
                no S4
                no finite-rank
                no sector asimetrico
                no 2+1
                no 3+1
```

Ninguna de esas extensiones queda autorizada por existir S2, ni por
existir en la hoja de ruta de septiembre. Tras S2 se vuelve a decidir
desde cero qué parte, si alguna, sirve al objetivo físico de
nachocausal.

T20 permanece fuera de S2: higiene documental posterior, no
certificación.

## 4. Firma

**Firmada.** `DECISION_S2 = AUTORIZADO` por decisión explícita del PI.
La única aparición autoritativa de ese token es este §4.

```text
ESTADO_FIRMA: FIRMADA — S2 AUTORIZADO, STOP_AFTER_S2
FIRMADA_POR: Ignacio Martin (PI)
FECHA_FIRMA: 2026-08-28
AUTORISED_SCOPE: S2 (ensamblaje, lista de §2)
DECISION_S2 = AUTORIZADO
STOP_AFTER_S2 = SI
DECISION_S3: NOT_AUTHORIZED_BY_THIS_NOTE
DECISION_S4: NOT_AUTHORIZED_BY_THIS_NOTE
NOT_AUTORIZADO: finite-rank, sector asimetrico, 2+1, 3+1,
                horizonte, benchmark, T20, S3-S7 de la hoja de ruta
CAJAS_DE_TIEMPO: sin cambio (conjunto -> 2026-09-11)
```
