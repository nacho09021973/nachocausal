# B1.3 — Par `lambda` congelado y comparabilidad a `n=2`

> **STATUS: `FROZEN_PAIR / DETERMINISTIC_QUADRATURE / NO_SEARCH / NO_SEEDS`.**
> **ADVANCES:** `L3` only for the pre-registered pair below, subject to the terminal reported
> by the deterministic interval calculation.

## 1. Regla de congelación

El par se fija antes de calcular `rho`. La selección usa únicamente los invariantes de boost de
B1,

```text
I1 = v1/v0,   I2 = u_in/u_out,   I3 = u_in*v1,
```

y la condición geométrica requerida `phi(lambda0) != phi(lambda1)`. No se usa `rho`, ninguna
cota de `rho`, ni una búsqueda o ranking posterior.

## 2. Par congelado

```text
lambda0 = (v0=0.5, v1=1.0, u_out=1.0, u_in=0.5, epsilon_s=0.1)
lambda1 = (v0=0.2, v1=0.8, u_out=2.0, u_in=0.9, epsilon_s=0.1)
```

Ambos satisfacen `u_in*v1 <= 1-epsilon_s`. Sus invariantes y fracciones interiores son,
calculados antes de cualquier comparabilidad,

```text
lambda0: I=(2.0, 0.5, 0.5),  phi=0.33411969780143397
lambda1: I=(4.0, 0.45, 0.72), phi=0.31131699615030030
```

Por tanto el par no es una órbita de boost y `phi(lambda0) != phi(lambda1)`.

## 3. Evaluación de `rho`

Para dos puntos iid, la separación angular de dos direcciones uniformes en `S²` satisface

```text
Pr(Delta <= a) = (1-cos(a))/2,   0 <= a <= pi.
```

Por simetría de intercambio,

```text
rho(lambda) = 2/Z(lambda)^2 * integral_{x radial <= y radial}
               G(Ux*Vx) G(Uy*Vy) Pr(Delta <= Delta_max(x,y)) dx dy,
Z(lambda) = integral_K G(UV) dU dV.
```

El verificador no optimiza la funcional de B1.2. Usa sus cotas angulares rigurosas, integradas
determinísticamente:

```text
rho_lower <= rho <= rho_upper.
```

La cota inferior usa `q_min*sqrt((Uy-Ux)(Vy-Vx))`; la superior usa
`q_max*sqrt((Uy-Ux)(Vy-Vx))`, ambas truncadas a `pi`. La cuadratura es fija en el sentido
metodológico: no hay semillas, Monte Carlo, ajuste, barrido de `lambda` ni selección adaptativa
del par. Los errores de cuadratura se reportan separadamente.

## 4. Terminales

```text
B1.3_POSITIVE                 si los intervalos de rho quedan separados;
B1.3_INCONCLUSIVE_BY_BOUNDS   si se solapan;
B1.3_NULL_FOR_FROZEN_PAIR     si la igualdad queda certificada.
```

Un terminal no positivo no se interpreta como refutación de L3 y no autoriza cambiar el par.
Este paso tampoco constituye reconstrucción.

## 5. Resultado de la evaluación congelada

La ejecución determinista de `verify_frozen_pair_rho.py` produce:

```text
lambda0: rho in [0.0022589065, 0.0062268026]
lambda1: rho in [0.0042527511, 0.0209269679]

TERMINAL = B1.3_INCONCLUSIVE_BY_BOUNDS
```

Los intervalos se solapan. Esto no prueba igualdad de `rho` ni refuta L3; sólo indica que las
cotas angulares globales empleadas aquí no son suficientemente ajustadas para separar este par.
El par permanece congelado y no se autoriza sustituirlo. Una eventual continuación requeriría una
decisión nueva para evaluar exactamente la funcional variacional, no una búsqueda de otra pareja.

Esa continuación fue abierta como B1.4 y produjo una separación para el mismo par; véase
`B1_4_exact_or_certified_rho.md` y `verification_certified_rho_frozen_pair.json`.

**Artefacto de verificación:** `verification_frozen_pair_rho.json`.
