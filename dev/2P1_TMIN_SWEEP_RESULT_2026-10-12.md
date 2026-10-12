# Frente 2+1D, fase B: barrido de la altura de la caja y regla `t_min`

**Fecha:** 2026-10-12 · **Exploración en `dev`, sin veredicto.** · **Código:** `dev/sweep_2p1_T.py`
→ `dev/2p1_sweep_T_2026-10-12.jsonl` (120 realizaciones); `dev/analyze_2p1_tmin.py` →
`dev/2p1_tmin_analysis_2026-10-12.json` · **Semillas:** `7_000_100..7_000_109` en todas las
celdas, de la banda de exploración 2+1D.

## Diseño

- Fijado **antes** de ejecutar: `T ∈ {6, 8, 10, 12, 16}` y `ρ ∈ {32, 63}`.
- La confirmación de meseta en `T = 20` se declaró después de la primera pasada y **antes** de
  ver cualquier resultado con `T = 20` (`b984d64`). La exige la regla heredada.
- **Regla `t_min`**, la de 1+1D sin cambios (`docs/estimator_v2_decision_spec.md`, Decision 2):
  la menor `T` que cumple:
  1. `|sesgo| <= semianchura media` de la horquilla;
  2. cobertura `>= 0.5`;
  3. que (1) y (2) se mantengan en todo `[T, 2T]`.

## Resultado

| `ρ` | `T` | el agujero negro localiza | Minkowski se abstiene | cobertura | sesgo | semianchura | desviación del punto medio | (1) | (2) |
|---|---|---|---|---|---|---|---|---|---|
| 32 | 6 | 10/10 | 10/10 | 0.30 | +0.0405 | 0.0294 | 0.0164 | no | no |
| 32 | 8 | 10/10 | 10/10 | 0.70 | +0.0107 | 0.0282 | 0.0300 | sí | sí |
| 32 | 10 | 10/10 | 10/10 | 0.70 | +0.0123 | 0.0351 | 0.0197 | sí | sí |
| 32 | 12 | 10/10 | 10/10 | 0.90 | +0.0031 | 0.0287 | 0.0120 | sí | sí |
| 32 | 16 | 10/10 | 10/10 | 1.00 | −0.0037 | 0.0380 | 0.0318 | sí | sí |
| 32 | 20 | 10/10 | 10/10 | 1.00 | −0.0061 | 0.0224 | 0.0116 | sí | sí |
| 63 | 6 | 10/10 | 10/10 | 0.30 | +0.0250 | 0.0187 | 0.0215 | no | no |
| 63 | 8 | 10/10 | 10/10 | **0.40** | +0.0108 | 0.0152 | 0.0109 | sí | **no** |
| 63 | 10 | 10/10 | 10/10 | 0.90 | −0.0046 | 0.0191 | 0.0133 | sí | sí |
| 63 | 12 | 10/10 | 10/10 | 0.80 | +0.0013 | 0.0127 | 0.0069 | sí | sí |
| 63 | 16 | 10/10 | 10/10 | 1.00 | −0.0039 | 0.0224 | 0.0094 | sí | sí |
| 63 | 20 | 10/10 | 10/10 | 1.00 | −0.0021 | 0.0234 | 0.0161 | sí | sí |

```text
t_min(ρ = 32) = 8      meseta [8, 16] confirmada
t_min(ρ = 63) = 10     meseta [10, 20] confirmada
```

En total, el agujero negro localiza en 120 de 120 realizaciones y el control plano se abstiene
en 120 de 120.

## Lectura

- **El sesgo por altura finita existe y se apaga con `T`.** Con `T = 6` es positivo, de `+0.025`
  a `+0.04`: el horizonte efectivo queda por fuera. Desde `T ≈ 10–12` es compatible con cero.
- **`t_min` no es robusta frente a la densidad: crece con `ρ`.** Con `T` fijo, el sesgo apenas
  cambia (`+0.011` en `T = 8` para las dos densidades), mientras la horquilla se estrecha al
  aumentar `ρ`. Por eso, con más densidad, el criterio de cobertura exige más altura. En 1+1D se
  vio lo mismo en forma de cobertura decreciente, y lo resolvió una `t_min` robusta en las dos
  densidades de referencia. Aquí no lo es.
- **Consecuencia para prereg-004.**
  - Si se toma la `t_min` más conservadora de las dos (`T = 10`), solo vale para densidades
    `<= 63`.
  - Las intensidades del preregistro tendrán que quedar dentro del dominio donde `t_min <= T`,
    o bien `T` tendrá que fijarse con margen (por ejemplo `T = 16`, en la meseta de ambas
    densidades).
  - Antes de congelar hace falta medir `t_min` a la densidad más alta que se vaya a usar.
- **Límite estadístico.** Con 10 semillas por celda, la cobertura tiene un error típico de
  alrededor de `±0.15`. El paso de `0.40` a `0.90` entre `T = 8` y `T = 10` con `ρ = 63` está
  claro, pero las coberturas por encima de `0.7` no se distinguen bien entre sí.

## Lo que falta antes de prereg-004

1. Medir `t_min` a una densidad mayor (por ejemplo `ρ = 126`), para ver la tendencia y decidir
   `T` con margen. Es caro: cada realización con `T = 20` tiene `N ≈ 13 000`.
2. Calcular los cinco criterios de prereg-002 en la `T` y las intensidades candidatas:
   significación (i), anchura frente a `θ_loc` con `ℓ = ρ^{-1/3}` (ii), estabilidad (iii),
   falsos positivos LOO (iv) y el guardia (v).

   Observación: con `ℓ = ρ^{-1/3}`, `θ_loc = 2ℓ/2M` vale `≈ 1.0` con `ρ = 63`, mientras que las
   anchuras medidas son `≈ 0.05–0.13 · 2M`. Con ese anclaje, el criterio (ii) sería
   prácticamente vacío. El anclaje de 1+1D se trasladó dimensionalmente, y antes de congelarlo
   conviene pasar por `/comite`.
3. Pasar por `/comite` antes de congelar prereg-004.
