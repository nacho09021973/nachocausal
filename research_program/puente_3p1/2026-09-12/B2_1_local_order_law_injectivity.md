# B2.1 — Inyectividad local de la ley order-only en `t0` congelado

> **HISTÓRICO / SUPERSEDED BY CORRECTED-KERNEL B2.** Este artefacto usa el kernel angular
> pre-corrección y no es evidencia para el resultado con el kernel físico actual.

> **STATUS: `FROZEN_PATH / FROZEN_T0 / DETERMINISTIC_ENCLOSURES / NO_SEARCH`.**
> No se modifica la curva de B2 ni el punto `t0=0.5`.

## Objetivo

Certificar que `t -> rho(lambda(t))` es localmente inyectiva cerca de `t0`, mediante una de dos
rutas: (i) una envolvente de derivada que excluya cero, o (ii) control riguroso del signo de las
diferencias en todo un vecindario. Una diferencia entre sólo dos puntos no se acepta como prueba.

## Método

Se evalúan bandas deterministas de `rho` en una malla fija alrededor de `t0`. La cota superior
usa `q_max` del rectángulo causal de cada par radial, en lugar del `q_max` global del patch. La
cota inferior maximiza una familia fija de trayectorias causales explícitas de dos tramos. Ambas
son cotas punto a punto de la funcional angular de B1.2. La integración radial usa cuadratura de
Gauss–Legendre determinista y se reporta estabilidad al cambiar el orden.

No hay Monte Carlo, semillas, ajuste, búsqueda de `t`, búsqueda de curvas, ni selección de una
nueva pareja. La curva sigue siendo la interpolación congelada de B2.

## Terminales

```text
B2.1_POSITIVE_DERIVATIVE
B2.1_POSITIVE_LOCAL_MONOTONICITY
B2.1_INCONCLUSIVE_BY_BOUNDS
```

La primera evaluación sólo puede emitir uno de los dos terminales positivos si las envolventes
certifican el signo; en caso contrario conserva la inconclusión sin interpretar el resultado como
estacionariedad real.

El terminal `B2.1_INCONCLUSIVE_BY_BOUNDS` es únicamente inconclusión sobre la inyectividad local
de `rho` cerca de `t0`. No afecta al resultado de B1.4: los extremos congelados ya satisfacen
`FROZEN_ENDPOINT_ISOMORPHISM = RULED_OUT_BY_POSITIVE_TV`. Tampoco afirma nada sobre un posible
isomorfismo entre puntos cercanos de la curva.

## Resultado de la primera evaluación

En la malla fija `t={0.45,0.475,0.5,0.525,0.55}`, las envolventes de `rho` fueron:

```text
t=0.45: [0.01880969, 0.03311921]
t=0.475: [0.01917781, 0.03389783]
t=0.50: [0.01954878, 0.03468095]
t=0.525: [0.01992260, 0.03546824]
t=0.55: [0.02029930, 0.03625938]
```

Las bandas muestran una tendencia creciente, pero se solapan entre puntos adyacentes. No permiten
certificar monotonicidad local ni excluir cero de una envolvente de derivada.

```text
TERMINAL = B2.1_INCONCLUSIVE_BY_BOUNDS
```

Esto no demuestra estacionariedad de `rho`, ni invalida la curva. El siguiente paso, si se
autoriza, debe estrechar la certificación de la misma curva y del mismo `t0`, no seleccionar una
alternativa.

**Artefacto:** `verification_b2_1_local_injectivity.json`.

> **Regenerado el 2026-10-11.** Estas envolventes son ~4.7x mayores que las que esta nota
> registraba. Las anteriores se calcularon el 2026-09-12 con el kernel angular **previo** a la
> correccion de `6f866a2` (`q`: de `exp(-s/2)/sqrt(s)` a `2exp(-s/2)/s^1.5`), y el artefacto no
> se regenero entonces. **El terminal no cambia:** las bandas adyacentes siguen solapando y
> `B2.1_INCONCLUSIVE_BY_BOUNDS` se mantiene. Ver `dev/B2_STALE_ARTIFACTS_2026-10-11.md`.

> **Actualización 2026-10-12.** El terminal de esta nota, incluso tras regenerarla el 2026-10-11
> con el kernel corregido, queda superado por un método más fino: bandas de `rho` por cuadratura
> frente a cotas directas de `S` por cajas con la maquinaria de la compuerta. B2.1 es ahora
> `B2.1_POSITIVE_DERIVATIVE`: `drho/dt > 0` en todo `[0.45, 0.55]`, por cajas, auditado por ASTRA
> y promocionado por el PI. Ver `research_program/puente_3p1/2026-10-12/B2_1_box_certificate.md`.
