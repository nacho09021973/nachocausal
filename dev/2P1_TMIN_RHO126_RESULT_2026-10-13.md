# Frente 2+1D, fase B: `t_min` con `ρ = 126` — deja de crecer con la densidad

**Fecha:** 2026-10-13 · **Exploración en `dev`, sin veredicto.** · **Diseño declarado antes de
ejecutar:** `88a25f6` (`ρ = 126`; `T ∈ {8, 10, 12, 16, 20, 24}`; semillas `7_000_100..7_000_109`).
**Datos:** `dev/2p1_sweep_T_rho126_v2_2026-10-12.jsonl` (GPU, tablas correctas) →
`dev/2p1_tmin_analysis_rho126_v2_2026-10-12.json` (`dev/analyze_2p1_tmin.py`, la regla heredada
de 1+1D).

## Resultado

| `T` | el agujero negro localiza | Minkowski se abstiene | cobertura | sesgo | semianchura | desviación del punto medio | (1) | (2) |
|---|---|---|---|---|---|---|---|---|
| 8 | 10/10 | 10/10 | **0.20** | +0.0116 | 0.0097 | 0.0073 | no | no |
| 10 | 10/10 | 10/10 | 0.90 | −0.0016 | 0.0117 | 0.0080 | sí | sí |
| 12 | 10/10 | 10/10 | 0.90 | +0.0030 | 0.0094 | 0.0073 | sí | sí |
| 16 | 10/10 | 10/10 | 0.90 | +0.0021 | 0.0062 | 0.0034 | sí | sí |
| 20 | 10/10 | 10/10 | 1.00 | −0.0062 | 0.0138 | 0.0097 | sí | sí |
| 24 | 10/10 | 10/10 | 1.00 | +0.0011 | 0.0080 | 0.0046 | sí | sí |

```text
t_min(ρ = 126) = 10     meseta [10, 20] confirmada; T = 24 también cumple
```

**Las tres densidades juntas** (barridos v2, GPU):

```text
t_min(ρ = 32) = 8      t_min(ρ = 63) = 10      t_min(ρ = 126) = 10
el agujero negro localiza 180/180;  el control plano se abstiene 180/180
```

## Lectura

- La preocupación de `594e6bb` era que `t_min` siguiera creciendo con la densidad: con `T`
  fijo el sesgo es casi constante mientras la horquilla se estrecha. **Entre `ρ = 63` y
  `ρ = 126` no crece.** Por encima de `T = 10` el sesgo de altura finita es compatible con cero
  incluso con horquillas de semianchura `~0.006–0.014`.
- **Consecuencia para prereg-004:** se puede congelar una `T` con margen (por ejemplo `T = 16`
  o `T = 20`) dentro de la meseta para las tres densidades.
- **Límites:**
  - con 10 semillas por celda la cobertura tiene un error de unos `±0.1–0.15`;
  - no se ha medido `ρ > 126`;
  - es exploración: la confirmación será la ejecución ciega.

## Comprobación cruzada con la ejecución de CPU interrumpida

Las 23 realizaciones que el barrido de CPU llegó a hacer antes de detenerlo, con tablas
posiblemente viejas (`dev/2P1_NUMBA_CACHE_STALE_TABLES_2026-10-12.md`), son **idénticas** a las de
GPU (`dev/compare_2p1_sweeps_v1_v2.py`): el mismo `N`, los mismos cuartiles de `O`, la misma
horquilla, la misma cobertura y la misma puerta.

## Pendiente antes de prereg-004

1. Pasar por `/comite` con:
   - la `T` con margen;
   - las intensidades;
   - el anclaje de `θ_loc` en 2+1D, porque `2ρ^{-1/3}/2M ≈ 1` es casi vacío frente a anchuras de
     `0.01–0.03·2M`;
   - si la cobertura sigue siendo un suelo de 0.5 o se refuerza;
   - el criterio de falsos positivos LOO.
2. Medir los cinco criterios de prereg-002 en la configuración candidata.
