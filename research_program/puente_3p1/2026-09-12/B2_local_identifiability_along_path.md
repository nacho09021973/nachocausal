# B2 — Identificabilidad local a lo largo de una curva física congelada

> **STATUS: `PATH_FROZEN / DETERMINISTIC_ANALYSIS / NO_SEARCH / NO_SEEDS`.**
> **TARGET:** `LOCAL_IDENTIFIABILITY_ALONG_FROZEN_PHYSICAL_PATH`.

## 1. Curva congelada antes de `rho`

Se fija, sin consultar ninguna evaluación de `rho`, la interpolación afín

```text
lambda(t) = (1-t) lambda0 + t lambda1,   t in [0,1],
lambda0 = (0.5, 1.0, 1.0, 0.5, 0.1),
lambda1 = (0.2, 0.8, 2.0, 0.9, 0.1).
```

La curva no es tangente a la órbita de boost: sus invariantes
`(v1/v0, u_in/u_out, u_in*v1)` cambian entre los extremos. Además,
`u_in(t)v1(t) <= 0.72 < 0.9 = 1-epsilon_s`, por lo que permanece dentro de la familia
congelada de patches.

## 2. Prueba de variación geométrica

Se calcula `phi(t)` antes de cualquier llamada a la rutina de comparabilidad. La derivada se
estima por diferencia central determinista en `t0=1/2`; esto no es una búsqueda de `t0`, sino el
punto central fijado por la definición de la curva.

## 3. Prueba order-only

Para los mismos valores de `t`, se calculan bandas deterministas para `rho(t)` usando la
caracterización angular de B1.2 y trayectorias explícitas como cotas inferiores. El resultado sólo
puede certificar B2 si las bandas permiten demostrar una pendiente no nula de `rho` en `t0`.

```text
B2_POSITIVE                  dphi/dt != 0 and drho/dt != 0 certified at t0
B2_INCONCLUSIVE_BY_BOUNDS    the rho bands do not certify the derivative
B2_NULL_RHO_DIRECTION        rho is certified locally constant (not a global no-go)
```

Ningún terminal afirma reconstrucción global, identificabilidad en todo el cociente físico,
unicidad frente a isomorfismos arbitrarios ni reconstrucción de Schwarzschild.

La no equivalencia de los extremos de la curva ya está establecida independientemente por B1.4:
`FROZEN_ENDPOINT_ISOMORPHISM = RULED_OUT_BY_POSITIVE_TV`. B2 no vuelve a abrir esa pregunta. Su
pregunta estrictamente adicional es si la ley puede invertirse localmente para recuperar `phi` a
lo largo de esta subfamilia. La variación de `phi` por sí sola no se usa como veto general a
isomorfismos.

## 4. Resultado de la primera evaluación

Para `t0=0.5` y `h=0.1`, la geometría ya varía:

```text
dphi/dt (central) = -0.02059566
```

Las bandas obtenidas para `rho` son:

```text
t=0.4: rho in [0.00500484, 0.01073851]
t=0.5: rho in [0.00542410, 0.01213807]
t=0.6: rho in [0.00585677, 0.01364770]
```

La banda de pendiente central compatible con esos intervalos es
`[-0.06281303, 0.08223597]`; por tanto no certifica `d rho/dt != 0`.

```text
TERMINAL = B2_INCONCLUSIVE_BY_BOUNDS
```

Esto no invalida la curva ni implica que `rho` sea localmente constante. La curva y el punto
`t0` permanecen congelados; no se permite sustituirlos por inspección post-hoc.

**Artefacto:** `verification_b2_frozen_physical_path.json`.

La derivada directa solicitada como B2.2 resolvió este bloqueo para la misma curva y el mismo
`t0`; véase `B2_2_shape_derivative.md`. El estado de B2 pasa a

```text
B2 = POSITIVE_LOCAL_IDENTIFIABILITY_ON_FROZEN_PATH
```

con las limitaciones de alcance declaradas arriba.
