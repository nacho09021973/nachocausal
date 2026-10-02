# B1.7 — Control radial genuino (1+1)D

> **STATUS: `FORMAL_SEPARATION_ESTABLISHED / FROZEN_PAIR / NO_SEARCH / NO_SEEDS`.**
> Este paso conserva el par y el soporte de B1.5, pero sustituye también el peso radializado
> (3+1)D por la medida natural del problema radial (1+1)D.

## 1. Contrato

Se mantienen exactamente

```text
lambda0 = (v0=0.5, v1=1.0, u_out=1.0, u_in=0.5, epsilon_s=0.1)
lambda1 = (v0=0.2, v1=0.8, u_out=2.0, u_in=0.9, epsilon_s=0.1)
```

y el orden producto

```text
x <_rad y  <=>  U_x < U_y  and  V_x < V_y.
```

La medida ya no es la densidad esférica de B1.6,

```text
G(UV) = s exp(-s),
```

sino

```text
H(UV) = exp(-s)/s,       (1-s) exp(s) = UV.
```

La forma de `H` se obtiene al suprimir las esferas `S^2` de la métrica de Schwarzschild. En
coordenadas radiales nulas (u,v),

```text
ds_1p1^2 = -f(r) du dv,
f(r) = 1 - 1/s,
U = -exp(-u/(4M)),  V = exp(v/(4M)),
```

y el jacobiano de Kruskal da, salvo una constante global que se cancela al normalizar,

```text
sqrt(-det g_1p1) dU dV  ∝  exp(-s)/s dU dV.
```

No se usa `q_true`, ni ángulos, ni una condición de alcance angular.

## 2. Evaluación

Se calcula

```text
rho_1p1d(lambda)
  = (2/Z(lambda)^2)
    integral_{Ux <= Uy, Vx <= Vy}
      H(Ux Vx) H(Uy Vy) dUx dUy dVx dVy.
```

Las dos regiones triangulares se transforman exactamente al cuadrado unitario y se evalúan con
la misma escalera determinista de Gauss–Legendre que B1.6. No hay semillas, Monte Carlo, búsqueda
de pares, ajuste ni barrido de $n$. La escalera mide estabilidad numérica; no constituye una
enclosure dirigida.

## 3. Resultado

```text
rho_1p1d(lambda0) = 0.513640160548670
rho_1p1d(lambda1) = 0.531483520752497
gap 1+1D          = 0.017843360203827
```

El gap permanece estable entre los órdenes 20 y 40. El terminal es

```text
B1.7_TRUE_1P1D_NUMERICALLY_SEPARATED
```

## 4. Lectura física

La separación persiste, y con un gap mayor, cuando se eliminan tanto la causalidad angular como
el peso transversal `r^2` de la medida `(3+1)D`. Para este par congelado, la no-degeneración
básica ya está presente en el problema radial genuino `(1+1)D`.

La comparación correcta queda así:

```text
TRUE 1+1D:       H(UV) + orden producto       gap ≈ 1.7843e-2
RADIALIZED 3+1D: G(UV) + orden producto       gap ≈ 3.3244e-4
FULL 3+1D:       G(UV) + alcance angular     gap ≥ 2.9182e-3 (certificado)
```

Esto descarta que la no-degeneración del par sea específicamente causada por el sector angular o
por el peso esférico `r^2`. El sector `(3+1)D` sí cambia sustancialmente la magnitud de la
separación en este ejemplo, pero ese cambio cuantitativo no debe confundirse con la fuente de la
separación básica.

## 5. Techo de afirmación

La primera evaluación fue numérica, pero ya ha sido sustituida por una enclosure dirigida en
`B1_7_formal_separation_certificate.md`. El certificado obtiene

```text
rho_1p1d(lambda0) <= U0 = 0.519812004386606
                   < L1 = 0.521869256599942
                   <= rho_1p1d(lambda1)
```

con gap formal `0.002057252213336` a 160 celdas por coordenada. No establece una equivalencia
general entre separabilidad radial y forma del patch, ni una ley asintótica en $n$.

No se abre $n>2$, B2 ni B3. El certificado formal se refiere sólo al par congelado.

## 6. Artefactos

```text
verificador: verify_b1_7_true_1p1d_control.py
resultado:   verification_b1_7_true_1p1d_control.json
certificado: B1_7_formal_separation_certificate.md
verificador formal: verify_b1_7_true_1p1d_formal.py
resultado formal: verification_b1_7_true_1p1d_formal.json
```
