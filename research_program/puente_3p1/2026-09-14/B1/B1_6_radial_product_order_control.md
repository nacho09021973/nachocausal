# B1.6 — Control radial de orden producto para el par congelado

> **STATUS: `DETERMINISTIC_NUMERICAL_CONTROL / FROZEN_PAIR / NO_SEARCH / NO_SEEDS`.**
> Este control responde a la pregunta de si la separación de B1.5 necesita el alcance angular.
> No modifica el certificado B1.5 y no abre $n>2$.

## 1. Contrato

Se reutiliza exactamente el par congelado de B1.3--B1.5,

```text
lambda0 = (v0=0.5, v1=1.0, u_out=1.0, u_in=0.5, epsilon_s=0.1)
lambda1 = (v0=0.2, v1=0.8, u_out=2.0, u_in=0.9, epsilon_s=0.1)
```

También se conserva la medida radial del B1.5,

```text
G(UV) = s exp(-s),       (1-s) exp(s) = UV,
```

y se cambia solamente el predicado causal por el orden producto radial,

```text
x <_rad y  <=>  U_x < U_y  and  V_x < V_y.
```

Por tanto el control no usa el alcance angular, la separación angular de dos direcciones ni el
kernel

```text
q_true(s) = 2 exp(-s/2) s^(-3/2).
```

La comparación a $n=2$ sigue siendo exacta en su reducción: la ley no etiquetada sólo tiene la
cadena y la anticadena, de modo que

```text
TV(P_lambda0,2^rad, P_lambda1,2^rad)
  = |rho_rad(lambda0) - rho_rad(lambda1)|.
```

## 2. Evaluación

La probabilidad radial se calcula como

```text
rho_rad(lambda)
  = (2/Z(lambda)^2)
    integral_{Ux <= Uy, Vx <= Vy}
      G(Ux Vx) G(Uy Vy) dUx dUy dVx dVy.
```

Las dos regiones triangulares se transforman exactamente en el cuadrado unitario mediante

```text
Uy = Umin + L_U y,       Ux = Umin + (Uy-Umin) x,
Vy = v0 + L_V z,         Vx = v0 + (Vy-v0) t,
```

con jacobiano `L_U^2 y L_V^2 z`. El script
`verify_b1_6_radial_product_order.py` evalúa esa integral con una escalera de órdenes de
Gauss–Legendre determinista. No hay semillas, Monte Carlo, búsqueda de pares, ajuste ni barrido
de $n$. La escalera es una comprobación de estabilidad numérica, no una envolvente formal.

## 3. Resultado

La ejecución produce:

```text
rho_rad(lambda0) = 0.500272738883214
rho_rad(lambda1) = 0.500605177052498
gap radial       = 0.000332438169284
```

El gap permanece estable al subir el orden de cuadratura de 12 a 32. Es aproximadamente un
11.4 % del gap certificado angular de B1.5,

```text
gap B1.5 angular = 0.002918225282557
```

El terminal correcto es:

```text
B1.6_RADIAL_NUMERICALLY_SEPARATED
```

## 4. Lectura física y techo de la afirmación

Para este par congelado, la separación persiste después de amputar el alcance angular y usar el
orden radial producto. Por tanto, la no-degeneración de B1.5 no puede atribuirse exclusivamente
a la causalidad angular esférica.

El sector angular sí aumenta mucho la separación observada: el gap pasa de aproximadamente
`3.32e-4` a `2.92e-3`. La interpretación actual es, por tanto,

```text
separación radial ya presente;
causalidad angular 3+1D = amplificador cuantitativo en este par.
```

El resultado es numérico porque la integral se ha evaluado mediante estabilidad de cuadratura,
sin una enclosure dirigida ni una cota formal del error. El uso de `G(UV)` es una cuestión
distinta: fija la interpretación física del control y deja pendiente separar la medida heredada
del modelo esférico de la medida natural de un modelo radial genuino. Antes de abrir B2, B3 o
$n>2$, se ejecutará ese control 1+1D.

## 5. Artefactos y procedencia

```text
verificador: verify_b1_6_radial_product_order.py
par B1.5 de referencia: 6633ebd2da81188ecc492f59b44b75e0e2c59cd2
```

El resultado numérico no altera ningún archivo congelado de B1.5.
