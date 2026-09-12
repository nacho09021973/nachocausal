# B3 — Auditoría transversal de identificabilidad a `n=2`

> **STATUS: `FROZEN_POINT / GAUGE_QUOTIENTED_CHART / DIRECT_SHAPE_DERIVATIVES`.**
> No se buscan curvas, puntos testigo ni nuevos parámetros.

## Punto y coordenadas físicas

Se usa exactamente el punto `lambda(t0)` de B2, con `t0=0.5`:

```text
lambda* = (0.35, 0.9, 1.5, 0.7, 0.1)
x* = (I1,I2,I3) = (v1/v0, u_in/u_out, u_in*v1)
   = (2.5714285714, 0.4666666667, 0.63).
```

El chart local fija el gauge `v0=0.35` y reconstruye

```text
v1 = v0*x1,  u_in = x3/v1,  u_out = u_in/x2.
```

## Cálculo

Se calculan `dphi` y `drho` en las tres direcciones `x1,x2,x3` mediante derivadas de forma
directas. Para `rho` se usa la fórmula de términos de borde de B2.2, propagando las cotas
angulares de B1.2; no se usan diferencias finitas. Para `phi` se usa la derivada de borde de sus
integrales interior/exterior.

La condición necesaria para que `phi` sea localmente recuperable de la única escalar `rho` es

```text
ker(d rho) subset ker(d phi),  equivalent to  dphi parallel drho.
```

## Terminales

```text
B3_POSITIVE_N2_COMPATIBLE       dphi || drho (necesario, no suficiente)
B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY
                                dphi wedge drho != 0 in the physical chart
B3_INCONCLUSIVE_BY_BOUNDS        las envolventes no deciden la proporcionalidad
```

Un terminal negativo justifica pasar a la ley `n=3`; ninguno de los terminales es una afirmación
de reconstrucción global.

## Resultado en el punto congelado

La evaluación directa da

```text
dphi/dx = (-9.4276e-05, 4.5716e-01, -1.8642e-04)
```

Dos componentes del producto cruzado excluyen cero, pero la componente `(x1,x3)` conserva una
envolvente estrecha que todavía contiene cero:

```text
cross(x1,x2) in [ 8.3573e-04,  7.3400e-03]
cross(x1,x3) in [-4.3322e-07,  1.2257e-06]
cross(x2,x3) in [-1.2413e-02, -7.5961e-03]

CHART_RANK = 3
D_RHO_NONZERO = CERTIFIED
D_PHI_WEDGE_D_RHO = CERTIFIED_NONZERO
TERMINAL = B3_NEGATIVE_FOR_N2_FULL_LOCAL_IDENTIFIABILITY
```

Ya que basta una sola componente del wedge separada de cero, las componentes `(x1,x2)` y
`(x2,x3)` certifican `dphi wedge drho != 0`; no es necesario resolver la componente `(x1,x3)`.
Como el chart tiene rango 3 y `drho != 0`, existe una dirección física `v` con
`drho(v)=0` y `dphi(v)!=0`. Por tanto `n=2` no puede reconstruir localmente `phi` en toda la
familia física tridimensional. Esto justifica proponer el paso a `n=3`, pero no lo autoriza.

**Artefacto:** `verification_b3_transverse_n2.json`.
