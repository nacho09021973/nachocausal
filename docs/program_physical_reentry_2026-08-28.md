# Reingreso físico controlado — opción 1

```text
ESTADO: FIRMADA — PHYSICAL_REENTRY OPTION_1
FECHA: 2026-08-28
GOBERNANZA: docs/program_s2_authorization_2026-08-28.md (STOP_AFTER_S2)
            docs/program_reopening_note_2026-08-28_R4.md
ANCLA_S2: c0780566d8f42d605e5c3d7dfc59f9327a1425be
ANCLA_S1: 2219f21dea2cbd82ba9d959a6d55e1cf87a0bcf6
NO_REVOCA: docs/program_closure_note_2026-07-30.md
SELLO: intacto — no se toca
SEMILLAS: banda virgen [2,000,000–2,999,999] permanece sin quemar
NATURALEZA: documental. Cero semillas, cero simulacion, cero ejecucion,
            cero instrumentos modificados.
```

La rama Fisher queda **cerrada como herramienta estructural**. No se abre
S3, S4, finite-rank, sector asimétrico, `2+1` ni `3+1`.

La pregunta deja de ser «qué más demostrar sobre retención Fisher» y
vuelve a ser:

> qué información sobre geometría y horizonte sobrevive realmente en
> order+number cuando se abandona el diamante idealizado y se acerca a
> geometrías físicamente relevantes.

## 1. Opción elegida

**Opción 1 — puente físico controlado** (elegida). Preguntar hasta qué
punto cópula, pérdida de información, Fisher e invariancias marginales
pueden decir algo verificable sobre el benchmark Schwarzschild
**existente**, sin afirmar que el diamante nulo ya sea el benchmark.

El primer objeto: caracterizar qué cambia al pasar de la caja nula
`[0,1]^2` con `mu_0=du dv` al dominio Eddington–Finkelstein `(t*, r)`.

**Opción 2** — volver directo al localizador de horizonte — queda
registrada y no se toma.

```text
PHYSICAL_REENTRY = OPTION_1_CONTROLLED_BRIDGE
STOP_AFTER_S2 = SI
S3_NOT_OPENED
NO_NEW_RUNS
NO_SEAL_TOUCH
NO_NEW_OBSERVABLES
NO_2PLUS1
NO_3PLUS1
NO_FINITE_RANK
NO_BENCHMARK_IS_NULL_DIAMOND
```

## 2. Primer paso: auditoría, no cálculo

```text
PHYSICAL_REENTRY:
¿qué parte del experimento Schwarzschild actual puede ponerse en el
mismo lenguaje de canal de información que acabamos de cerrar?
```

Falsificador precomprometido: si el cambio de dominio/coordenadas
destruye la estructura que permitía el análisis, se registra y **no se
fuerza el puente**.

Nada de correr cosas nuevas hasta saber si la respuesta ya está en los
runs. Después de esta auditoría se decide si merece un puente
matemático al benchmark o volver al observable de horizonte.

## 3. Firma

```text
ESTADO_FIRMA: FIRMADA — PHYSICAL_REENTRY OPTION_1
FIRMADA_POR: Ignacio Martin (PI)
FECHA_FIRMA: 2026-08-28
DECISION_S3: NOT_AUTHORIZED
DECISION_PHYSICAL_REENTRY = OPTION_1
NO_NEW_EXECUTION = SI
```

## 4. Resultado de la auditoría 1

La auditoría documental posterior está en
`docs/physical_reentry_audit_001_2026-08-28.md` y sustituye cualquier lectura
negativa automática basada sólo en soporte móvil.

```text
PHYSICAL_REENTRY = PARTIAL_TRANSPORT_WITH_EXACT_FIRST_OBLIGATION
FIRST_PHYSICAL_OBSTACLE = DOMAIN_BRIDGE
MOVING_SUPPORT_QMD_STATUS = OPEN
NEXT_RUN_AUTHORIZED = NO
```

Transporte exacto ya disponible: orden producto en coordenadas nulas y, en
cada estrato `N=n`, representación latente `Pi_n -> [P_{Pi_n}]`. No está
demostrado el transporte de la familia física a un experimento paramétrico
regular de S1/S2. WP4 Prop. 2 sólo bosqueja la cota Hellinger lineal; no cierra
la no-QMD para los extremos sellados.
