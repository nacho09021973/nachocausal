# Frente 2+1D, fase B (provisional): el estimador-v2 localiza el horizonte si la caja es lo bastante alta

**Fecha:** 2026-10-12 · **Exploración en `dev`, sin veredicto.** · **Código:** `dev/gen2p1_efbox.py`
(generador sobre la caja EF alta) y `dev/explore_2p1_estimator.py` (estimador-v2 portado) ·
**Datos:** `dev/2p1_phaseB_estimator_runs_2026-10-12.jsonl` · **Semillas:** solo de la banda de
exploración 2+1D `7_000_000..7_000_999`.

## Montaje

- **Geometría:** la de 1+1D (`r ∈ [0.1, 1.3]`, `2M = 0.5`) con `φ ∈ S¹` y `t* ∈ [0, T]`. El
  sembrado es uniforme en `(t*, φ)` con densidad `∝ r`.
- **Orden:** el lema E1, con el generador de `6e19328`. Controles: coincidencia exacta con la
  relación cerrada sellada de 1+1D en los pares con el mismo ángulo, transitividad y auditorías.
- **Estimador:** la lógica de la v2 sellada, sin cambios. `O = |futuro|` de los elementos
  mínimos, partición por 2-medias, y puerta `improvement >= τ(n)` con el mismo Montecarlo de
  `τ`. Para `n > 128`, `τ` se calcula en `dev`, porque la tabla sellada llega hasta 128.
- **Puntuación:** horquilla `[máx r de O bajo, mín r de O alto]`. El control de falsos
  positivos es Minkowski 2+1D sobre la misma nube.

## Resultados

| `T` | `N` | semillas | el agujero negro localiza | Minkowski se abstiene | horquilla cubre `2M` | horquillas |
|---|---|---|---|---|---|---|
| 6 | 2000 | 7000010–14 | 5/5 (`improvement` 0.83–0.94 frente a `τ` ≈ 0.81) | 5/5 | **0/5** | `r` ≈ 0.51–0.57, una invertida |
| 12 | 4000 (misma densidad) | 7000020–22 | 3/3 (`improvement` 0.98–0.99) | 3/3 | **3/3** | [0.493, 0.509], [0.493, 0.503], [0.442, 0.525] |

**Lectura.**
- Con `T = 6`, el estimador localiza un **horizonte efectivo desplazado hacia fuera** (`r ≈ 0.53`).
  Un punto justo fuera de `2M` tarda un tiempo logarítmicamente divergente en escapar, así que
  dentro de una caja de altura finita su futuro sigue siendo pequeño.
- Con `T = 12` el desplazamiento desaparece en las tres semillas y la separación es más nítida.
- El control plano no da ningún falso positivo con ninguna de las dos alturas.

## Lo que NO es

- **No es un resultado.** Son 8 realizaciones en `dev`, con `T` y `N` elegidos sobre la marcha.
- **Elegir `T` a la vista de estos datos es exploración.** prereg-004 tendrá que fijar `T` con un
  criterio de principio y congelado, como el `t_min` de 1+1D: la menor altura que cumpla una
  meseta de cobertura y estabilidad, con densidad robusta.
- **No se han medido aún los criterios de prereg-002:** significación, anchura frente a `θ_loc`
  con `ℓ = ρ^{-1/3}`, estabilidad y falsos positivos LOO. Tampoco la dependencia con la
  densidad.

## Semillas de exploración usadas

`7000000–7000002`, `7000010–7000014` y `7000020–7000022`.
