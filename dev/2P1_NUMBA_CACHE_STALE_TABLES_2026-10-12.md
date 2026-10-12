# Frente 2+1D: el generador de CPU usó tablas de otra `T` por la caché de numba

**Fecha:** 2026-10-12 · **Afecta a:** el barrido de `T` (`594e6bb`, `dev/2p1_sweep_T_2026-10-12.jsonl`)
y al barrido de `ρ = 126` (detenido con 14 de 60 realizaciones,
`dev/2p1_sweep_T_rho126_2026-10-12.jsonl`). **No afecta** a la fase A (`dev/gen2p1_equatorial.py`,
parche fijo) ni a las ejecuciones aisladas con `T = 6` y `T = 12` del informe provisional, pero
eso no se ha verificado una a una.

## Qué pasó

`dev/gen2p1_efbox.py` define tablas globales que **dependen de `T`**: `QT`, `DLNF`, `ZMIN`,
`ZMAX`, `DZ` y `NZ`, a través de `NC2P1_T_EDGE`. Sus kernels se declaraban con
`@njit(cache=True)`. **numba congela los globales como constantes al compilar, y su caché no se
invalida cuando cambian**, solo cuando cambia el fichero fuente. Prueba mínima:

```text
XVAL=1.0 -> 2.0     XVAL=5.0 -> 2.0     XVAL=9.0 -> 2.0     (con cache=True)
```

El barrido lanza un subproceso por cada `(T, ρ, semilla)`. A partir de la primera compilación,
**todas las `T` usaban las tablas de la `T` que compiló primero**, hasta la siguiente edición del
fichero. Con una tabla de `T` menor, el rango en `z` se queda corto, la `q` de los `w` muy
negativos queda congelada en el último nodo (sobrestimada), y pueden aparecer **cotas inferiores
no válidas y relaciones espurias**.

## Por qué no lo detectó ningún control

- La transitividad, la auditoría contra el disparo fino y el control radial usan las mismas
  tablas: son coherentes entre sí aunque sean de otra `T`. El control radial ni siquiera usa las
  tablas.
- Lo destapó la comparación con la versión GPU, que recibe las tablas como argumentos. Hubo 6
  pares distintos en una validación con `T = 12`, que desaparecieron al recompilarse la caché con
  esa misma `T`.

Es el **segundo** fallo del día ligado a la caché de numba. El primero fue el control de
fast-math, que pasaba en vacío (`dev/B2_FASTMATH_GUARD_CACHE_FINDING_2026-10-12.md`).

## Corrección

- `gen2p1_efbox.py` pasa a `cache=False` en todos sus kernels, y se borró su caché. La CPU
  corregida y la GPU coinciden exactamente con `T = 16` (2 919 871 relaciones, 0 desacuerdos).
- `dev/gen2p1_gpu.py` (CuPy, doble precisión) recibe las tablas como argumentos. Coincide con la
  CPU corregida con `T = 6`, `12` y `16`. Usa además una **escalera de Richardson par a par**:
  disparos de 64 y 128 pasos. En 300 000 pares, el error real nunca supera `0.2·e`, y el criterio
  usa `20·e + 1e-3`. Solo pasa al disparo fino entre el 0.15 % y el 0.4 % de los pares.
- **Los dos barridos se repiten íntegros en GPU** con las mismas semillas:
  `dev/2p1_sweep_T_v2_2026-10-12.jsonl` y `dev/2p1_sweep_T_rho126_v2_2026-10-12.jsonl`. Las nubes
  de puntos son idénticas, porque dependen solo de `(T, semilla)`, así que la comparación por
  semilla mide el impacto del error.

## Estado del resultado `t_min`

`594e6bb` (`t_min = 8` con `ρ = 32` y `t_min = 10` con `ρ = 63`) queda **en suspenso** hasta
comparar con los barridos v2.

## Resultado de la repetición (barrido de `ρ = 32, 63`)

`python3 dev/compare_2p1_sweeps_v1_v2.py dev/2p1_sweep_T_2026-10-12.jsonl dev/2p1_sweep_T_v2_2026-10-12.jsonl`:
en las **120 de 120** realizaciones, v1 (CPU con tablas posiblemente viejas) y v2 (GPU con tablas
correctas) dan el mismo `N`, los mismos cuartiles de `O`, la misma horquilla, la misma cobertura
y la misma puerta de Minkowski. `dev/analyze_2p1_tmin.py` sobre v2
(`dev/2p1_tmin_analysis_v2_2026-10-12.json`) da **las mismas celdas** y
**`t_min = 8` con `ρ = 32` y `t_min = 10` con `ρ = 63`**. El resultado de `594e6bb` se sostiene.

**Lectura.** Las tablas viejas solo cambiaban `q` en `w` muy negativos, más allá del rango de la
tabla compilada. Esos `w` aparecen en pares con alcance `≫ π`, cuya decisión no depende de esa
cifra. No es una garantía para cualquier configuración, así que el generador de CPU queda
corregido igualmente.

El barrido de `ρ = 126` se repite entero en v2 (`dev/2p1_sweep_T_rho126_v2_2026-10-12.jsonl`).
