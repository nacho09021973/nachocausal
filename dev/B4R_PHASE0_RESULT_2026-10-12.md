# B4-R, fase 0: la compuerta de viabilidad falla — B4 vuelve a `PARKED`

**Fecha:** 2026-10-12 · **Especificación:**
`research_program/puente_3p1/2026-10-12/B4R_n3_reopening_spec.md` §5 (firmada) · **Script:**
`dev/explore_b4r_phase0.py` → `dev/B4R_phase0_output_2026-10-12.json`
(`.venv/bin/python dev/explore_b4r_phase0.py 64 128`). Es exploración en flotante, con las mismas
cotas por celdas que usaría un certificado, y **no emite terminal de B4**.

## Resultado

| `M` | `σ_min(R·Dm_centro)` | `‖R·E_M‖_F` | `σ_pred(M)` | semianchura relativa por fila `(ρ, E[f²], E[p²], E[pf])` |
|---|---|---|---|---|
| 64 | `0.0016165` | `12.4888` | `−12.4872` | `0.54, 0.72, 0.51, 0.84` |
| 128 | `0.00072194` | `7.8392` | `−7.8385` | `0.33, 0.46, 0.32, 0.47` |

(Son estimaciones en flotante, no cotas certificadas. Las cifras se muestran truncadas; los
valores completos están en el JSON.)

**Compuerta, congelada en §5:** `σ_pred(128) > 0`. **Falla**, con `σ_pred(128) ≈ −7.84`. Según la
regla escrita, B4 vuelve a `PARKED` con `N3_RANK_UNRESOLVED_BY_RESOLUTION`. No se extrapola en
`M`, no se cambia el escalado y no se eligen otros menores ni filas.

## Por qué no tiene arreglo con esta maquinaria

- Para pasar, `‖R·E‖_F` tendría que bajar de `7.84` a menos de `σ_min ≈ 7e-4`, es decir, un
  factor de unos `10⁴`. De `M = 64` a `M = 128` solo baja un factor `0.63`.
- `M = 128` es el techo de memoria (§5). El error relativo de las filas de momentos, del 32 al
  47 %, es del mismo orden que el de `S` en la compuerta, como se esperaba. Las derivadas de
  momentos de segundo orden no son más precisas que las cotas de `h` de las que salen.

## Lo que esto NO dice

- **No** dice que `rank Dm < 3`. Las `σ_min` centrales son pequeñas y bajan al aumentar `M`
  (`0.0016 → 0.00072`, frente a `σ_max ≈ 16.6`). Eso sugiere una casi-degeneración, pero
  B4.1 lo establece explícitamente: «un determinante numéricamente pequeño no es evidencia de
  rango menor». Además, el centro de la envolvente no es el valor verdadero.
- **No** dice nada sobre `phi` a `n=3`.

## Control del paso 1 y hallazgo

El control del paso 1 saltó: el `rho` de referencia de B4, `0.0523`, cae fuera de la envolvente
de la fase 0. La causa es un error del script antiguo de B4 y está documentada en
`dev/B4_EXECUTION_WRONG_MOMENTS_2026-10-12.md`. La fase 0 continuó una vez explicada la
diferencia, como manda §5.

## Estado

```text
B4_REOPEN_ONLY_IF            = aceptada por el PI (maquinaria de envolventes)
B4-R fase 0                  = ejecutada; compuerta FALLA
B4                           = PARKED, N3_RANK_UNRESOLVED_BY_RESOLUTION
B4-R fase 1 (certificado)    = no procede
```

Para reabrir otra vez haría falta una maquinaria de cotas de `h` con un orden de convergencia
mucho mejor, alrededor de 10⁴ veces más precisa con la misma memoria. Esta especificación no la
propone.
