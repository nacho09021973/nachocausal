# B1.7 — Certificado formal de separación en el control genuino 1+1D

> **STATUS: `FORMAL_SEPARATION_ESTABLISHED / FROZEN_PAIR / DIRECTED_ROUNDING_ENCLOSURE`.**
> El certificado sólo trata el par congelado de B1.5 a (n=2). No abre nuevos pares, (n>2),
> B2 ni B3.

## 1. Modelo y blanco

El modelo conserva el soporte de B1.5 y sustituye la medida esférica `G(UV)` por la medida
natural radial de Schwarzschild en coordenadas de Kruskal,

```text
H(UV) = exp(-s)/s,       (1-s) exp(s) = UV.
```

La causalidad es el orden producto,

```text
x <_rad y  <=>  U_x < U_y and V_x < V_y.
```

Para (n=2), la ley del orden no etiquetado sólo tiene dos clases, cadena y anticadena. Por ello
la separación formal de las fracciones de ordenación implica directamente

```text
TV(P_lambda0,2, P_lambda1,2)
  = |rho_1p1d(lambda0) - rho_1p1d(lambda1)|.
```

El único blanco necesario es construir

```text
rho_1p1d(lambda0) <= U0 < L1 <= rho_1p1d(lambda1).
```

## 2. Monotonicidad escalar

Escribiendo `w=UV`,

```text
w = (1-s) exp(s),       dw/ds = -s exp(s) < 0,
H(s) = exp(-s)/s,       dH/ds = -exp(-s)(1/s + 1/s^2) < 0.
```

Por tanto `H(w)` es estrictamente creciente en `w`. En una celda rectangular

```text
[U_i,U_{i+1}] x [V_k,V_{k+1}],
```

el producto `UV` alcanza sus extremos en las cuatro esquinas. Si `h_lo[i,k]` y `h_hi[i,k]`
son las evaluaciones escalares certificadas en esos extremos, entonces

```text
h_lo[i,k] <= H(UV) <= h_hi[i,k]
```

en toda la celda. La inversión de `(1-s) exp(s)=w` se certifica mediante la monotonicidad de
`f(s)=(1-s) exp(s)` y aritmética intervalar escalar; no se usa Lambert W en el certificado.

## 3. Partición exacta del dominio ordenado

Sean `U_i` y `V_k` nodos racionales uniformes. Para las celdas `i<=j` y `k<=m`, el volumen
ordenado de las coordenadas U y V es exactamente

```text
A_ij = DeltaU_i DeltaU_j             si i<j,
A_ii = DeltaU_i^2 / 2,

B_km = DeltaV_k DeltaV_m             si k<m,
B_kk = DeltaV_k^2 / 2.
```

Esto incluye toda la región `U_x<=U_y, V_x<=V_y` salvo fronteras de volumen cero. La integral
de pares queda acotada por sumas de bloques positivas:

```text
I_lo = sum_{i<=j,k<=m} A_ij B_km h_lo[i,k] h_lo[j,m],
I_hi = sum_{i<=j,k<=m} A_ij B_km h_hi[i,k] h_hi[j,m].
```

La normalización satisface análogamente

```text
Z_lo = sum_{i,k} DeltaU_i DeltaV_k h_lo[i,k],
Z_hi = sum_{i,k} DeltaU_i DeltaV_k h_hi[i,k].
```

Como todo es positivo,

```text
rho_lo = 2 I_lo / Z_hi^2,
rho_hi = 2 I_hi / Z_lo^2.
```

El verificador redondea cada suma, producto, cociente y conversión escalar hacia fuera. No hay
constante de holgura global.

## 4. Resultado certificado

Con 160 celdas uniformes en cada coordenada:

```text
lambda0:
  rho_lower = 0.507539961668160
  rho_upper = 0.519812004386606

lambda1:
  rho_lower = 0.521869256599942
  rho_upper = 0.541275116543632

U0 = 0.519812004386606
L1 = 0.521869256599942
L1-U0 = 0.002057252213336
```

Por tanto,

```text
rho_1p1d(lambda0) < rho_1p1d(lambda1)
```

queda establecido formalmente para el par congelado. En particular,

```text
TV(P_lambda0,2, P_lambda1,2) >= 0.002057252213336 > 0.
```

Una refinación independiente a 192 celdas da `U0=0.518778327792765`, `L1=0.523459493990852`
y gap `0.004681166198087`, sin reversión del terminal.

## 5. Techo del resultado

El certificado prueba la no-degeneración del par congelado en el modelo radial genuino 1+1D.
No prueba la identificabilidad general de la forma del patch, no convierte la separación finita en
una afirmación para todo `n`, y no establece que exista una descomposición aditiva entre los
efectos de medida y causalidad.

La conclusión física defendible es:

```text
La no-degeneración de B1.5 no es exclusiva de 3+1D.
Ya aparece formalmente en el control genuino 1+1D del mismo par.
```

## 6. Artefactos

```text
verificador: verify_b1_7_true_1p1d_formal.py
resultado:   verification_b1_7_true_1p1d_formal.json
```
