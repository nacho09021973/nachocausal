# Formula Branch — cierre exploratorio

Esta carpeta documenta la rama independiente `formula`.

La pregunta de la rama era si el PASS de `prereg-002` permitía extraer una ley de
convergencia a densidad finita para la anchura del bracket reconstruido del
horizonte.

La conclusión es positiva pero limitada:

```text
W_H, sigma_rhat, median center error = O(ell) ~= O(rho^(-1/2))
```

Esto debe leerse como una ley empírica de escala de discreción dentro del
protocolo estudiado, no como una fórmula fundamental nueva.

## Hipótesis

En un sprinkling de Poisson 1+1D, la escala microscópica de discreción es

```text
ell(rho) ~ rho^(-1/2)
```

La hipótesis de la rama `formula` fue que la resolución radial del estimador
order-only queda limitada por esa escala:

```text
W_H(rho) ~ O(ell)
```

También se midieron dos cantidades relacionadas:

```text
sigma_rhat(rho)
median |rhat_H - r_H|
```

La predicción conservadora era que las tres magnitudes deberían escalar cerca de
`rho^(-1/2)` si el bracket realmente converge hacia la escala de discreción.

## Qué se hizo

1. Se extrajeron primero los agregados ya existentes del resultado `prereg-002`.
2. Se creó una cartela de investigación separada para no mezclar esta rama con
   el protocolo sellado.
3. Se corrió una barrida nueva con 40 semillas por densidad:

   ```text
   lambda = 1500, 3000, 6000, 12000, 24000
   ```

4. Se añadió un kernel C++ para empujar densidades más altas sin materializar la
   matriz causal `N x N`.
5. Con el kernel C++ se añadieron:

   ```text
   lambda = 48000, 96000
   ```

6. Se transcribieron los resultados agregados en:

   ```text
   docs/formula_density_sweep_result.md
   ```

Los artefactos completos por semilla quedan en `results/`, que está ignorado por
git.

## Resultado numérico

Con las siete densidades:

```text
median width/2M      gamma = -0.461
std midpoint         gamma = -0.551
median center error  gamma = -0.463
```

Los dos puntos de densidad alta fueron:

```text
lambda=48000:
  width=0.036170
  sigma=0.004878
  E_med=0.003399
  coverage=0.775

lambda=96000:
  width=0.022842
  sigma=0.003109
  E_med=0.003106
  coverage=0.550
```

La lectura razonable es que las tres cantidades permanecen cerca del exponente
`1/2`, con dispersión local y efectos de densidad finita. El resultado apoya
`O(ell)`, pero no justifica una ley exacta del tipo

```text
W_H = A*rho^(-1/2)
```

con prefactor universal.

## Tensión importante

La precisión mejora al subir la densidad, pero la cobertura cae:

```text
coverage(lambda=96000) = 0.55
```

Esto es científicamente útil. Indica que el bracket funciona como localizador de
frontera, no como intervalo de confianza calibrado. A densidad alta el bracket se
estrecha, pero deja de cubrir de forma robusta si el centro conserva un sesgo o
fluctuación residual.

Por tanto, no conviene seguir empujando densidad como si eso fuera a producir una
fórmula exacta. Más densidad probablemente tensará todavía más la cobertura.

## Qué no afirmar

No afirmar:

```text
W_H = A*rho^(-1/2)
```

como ley estable demostrada.

No afirmar que `-0.523` sea un exponente especial. Fue una pendiente inicial de
cuatro puntos; las corridas extendidas muestran que la lectura correcta es
compatibilidad con `1/2`, no descubrimiento de `0.523`.

No afirmar una fórmula fundamental nueva. Esta rama muestra una escala empírica
de resolución del estimador bajo el protocolo actual.

## Estado de cierre

La vía `formula` queda cerrada como:

```text
exploración positiva para convergencia O(ell)
```

No queda justificado continuar con densidades todavía más altas dentro de esta
misma vía. El siguiente avance ya no es "más corrida", sino física/geométrica.

## Siguientes pasos recomendados

Abrir una vía nueva, separada de `formula`, centrada en el volumen causal futuro
continuo:

```text
continuous_volume
```

Objetivo:

```text
V_+(r) = Vol(J^+(x) cap patch)
```

La pregunta física sería si cerca del horizonte el observable continuo tiene un
término transversal lineal:

```text
V_+(r) - V_+(r_H) ~ c |r-r_H|
```

Si eso se deriva o se verifica geométricamente, entonces el exponente `1/2` deja
de ser solo un ajuste empírico y pasa a tener una explicación física:

```text
observable volume has a linear horizon-scale feature
+ Poisson discreteness scale ell ~ rho^(-1/2)
=> radial resolution O(ell)
```

Esa es la vía correcta para transformar esta observación empírica en un argumento
físico defendible.
