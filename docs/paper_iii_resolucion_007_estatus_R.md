# Paper III — Resolución 007: estatus de `R = L⁴/V`

```text
RESOLUTION_ID=PAPER_III_R007
STATUS=APPROVED
DATE=2026-09-10
SIGNED_BY=PI
RESOLVES=G0-5 (estatus futuro; el pasado ya lo derogó R001)
SCOPE=CLAIM_STATUS_ONLY
NUMBERS_MOVED=NONE
GENERATOR_EXECUTED=NO
CODE_TOUCHED=NONE
R_INTERPRETATION=DEFERRED
```

Firma el bloque `APPROVED TEXT — R7` de
[Resoluciones pendientes](paper_iii_resoluciones_pendientes.md), sin
modificarlo.

## 1. Texto aprobado, literal

> `R = L⁴/V` no se interpreta, ni se cita como evidencia, ni se describe como
> calibrador, hasta que se cumplan las tres condiciones: R001 aplicada al
> generador de la pierna de caja, R5 aplicada al reporte, y la pierna reejecutada
> bajo la convención firmada. La afirmación «`R` deriva monótonamente y no
> estabiliza» queda retirada. `median_R_min` no es restituible por aritmética:
> el artefacto guarda la mediana de \(L^4/V\), no las \(L\) por elemento, y la
> mediana de \((L+1)^4/V\) no es función de ella.

## 2. Estado de las tres condiciones

Las tres se cumplen, y están certificadas en
[el contrato](paper_iii_fase0_contrato.md) y por
`dev/verify_3p1_phase0_contract.py`:

| condición del texto firmado | estado | evidencia |
|---|---|---|
| R001 aplicada al generador de la pierna de caja | **cumplida** | `PHASE_0_STEP_2_CONVERSION=DONE`; productor `b5ca8c99…6fb2bb`, commit `3230986` |
| R5 aplicada al reporte | **cumplida** | `RESOLUTION_005=SIGNED_2026-09-10`; predicado `r005_applied()` |
| pierna reejecutada bajo la convención firmada | **cumplida** | `PHASE_0_STEP_3_REEXECUTION=DONE`; artefacto `..._r001_results.json`, `0aa22402…c55b68`, sección `[A2]` |

## 3. Lo que esta firma hace, y lo que deliberadamente no hace

La firma **levanta la prohibición procedimental** que el propio texto imponía:
las tres condiciones que la condicionaban están cumplidas, luego el texto ya no
bloquea por sí mismo.

**El PI no ejerce esa apertura.** El estatus de `R` queda:

```text
R_INTERPRETATION=DEFERRED
```

Esta firma **NO autoriza**, explícitamente:

- **universalidad de `R`** — `R` no es un calibrador universal y no se describe
  como tal;
- **estabilización de `R`** — no se afirma que `R` estabilice, del mismo modo que
  el texto firmado retira la afirmación contraria («deriva monótonamente y no
  estabiliza»). **Ambas direcciones quedan sin afirmar**, que es exactamente lo
  que significa retirar una afirmación y no sustituirla por su negación;
- **interpretación de `R_min`** — sigue sin restituir por aritmética, por la
  razón que da el propio texto firmado;
- **reapertura del canal de minimales** — que además está bloqueada por una
  restricción **independiente y todavía activa**,
  [R004](paper_iii_resolucion_004_lineas_base_minimales.md) y
  [R002 C3](paper_iii_resolucion_002_reescopado_fase1.md): su línea base no se
  cumple. Aunque R007 se hubiera firmado sin reservas, R004 seguiría cerrando ese
  canal por su cuenta.

La decisión sobre `R` como funcional de forma pertenece a la **Fase 3** de
[la hoja de ruta](hoja_de_ruta_paper_iii.md), que no se abre por esta firma ni
por ninguna otra de la Fase 0.

## 4. Efecto

Ninguna cifra se mueve. Ningún generador se ejecuta. Ningún fichero de código se
toca. `median_R_min` sigue sin restituir. La única transición es documental:

```text
RESOLUTION_007=UNSIGNED  ->  RESOLUTION_007=SIGNED_2026-09-10
G0-5 = CLOSED (ya lo estaba por R001 + pasos 2-3; R007 fija el estatus futuro)
R_INTERPRETATION=DEFERRED   (sin cambio)
```

Con R007 firmada, **las siete resoluciones de la Fase 0 están firmadas** y no
queda ninguna pendiente en
[Resoluciones pendientes](paper_iii_resoluciones_pendientes.md).
