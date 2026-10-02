# B2.2 — Derivada de forma directa de `rho` en `t0=0.5`

> **STATUS: `FROZEN_PATH / FROZEN_T0 / SHAPE_DERIVATIVE_DERIVED / DETERMINISTIC_ENCLOSURES`.**
> No hay diferencias finitas, búsqueda de parámetros, semillas ni Monte Carlo.

## 1. Derivación

Sea `A(t)=integral_{K(t)} w(x) dx` y

```text
B(t)=integral_{K(t)} integral_{K(t)} w(x)w(y) h(x,y) dxdy,
rho(t)=B(t)/A(t)^2,
```

con `w=G(UV)` y `h(x,y)` la probabilidad angular inducida por la relación causal ambiental,
integrada sobre las dos direcciones de `S²`. El núcleo `h` no depende de `t`; sólo se mueve el
dominio rectangular `K(t)`.

La fórmula de transporte de Reynolds da

```text
A' = integral_{boundary K} w v_n dS,
B' = 2 integral_{boundary K} w(x) v_n(x)
       [integral_{K} w(y) h(x,y) dy] dS_x,
rho' = B'/A² - 2 rho A'/A.
```

La segunda igualdad usa la simetría `h(x,y)=h(y,x)`. En coordenadas `(U,V)`, las velocidades de
las caras son `(-u_out)', (u_in)', (v0)', (v1)'` y el factor angular común se cancela.

## 2. Certificación

Para cada integral de cara se propagan las cotas inferior/superior de `h` derivadas en B1.2.
Como las velocidades de las caras pueden tener ambos signos, el extremo correspondiente se
intercambia al multiplicar por una velocidad negativa. Así se obtiene una envolvente directa de
`B'` y, por tanto, de `rho'`, sin aproximar la derivada por `rho(t+h)-rho(t-h)`.

La cuadratura es determinista de Gauss–Legendre y se repite a dos órdenes; la diferencia observada
se reporta como margen numérico conservador. El resultado sólo emite `B2.2_POSITIVE_DERIVATIVE`
si el intervalo final excluye cero.

## 3. Terminales

```text
B2.2_POSITIVE_DERIVATIVE
B2.2_INCONCLUSIVE_BY_BOUNDS
```

La curva, el punto `t0`, el par de B1 y la caracterización causal permanecen congelados. Un
resultado positivo establece sólo variación local de la ley `n=2` en esta subfamilia; no es una
reconstrucción global.

## 4. Resultado

Para la curva afín congelada de B2 y `t0=0.5`, la evaluación directa de los términos de borde da

```text
drho/dt(t0) in [-0.04172860, -0.02039597]
TERMINAL = B2.2_POSITIVE_DERIVATIVE
```

La envolvente excluye cero después de incluir el margen observado entre cuadraturas de órdenes
10 y 14. Junto con `dphi/dt(t0) != 0` de B2, esto establece identificabilidad local de `phi` a
través de `rho` dentro de esta curva física congelada, en el sentido de la función inversa. No
establece identificabilidad global ni reconstrucción del espacio-tiempo.

**Artefacto:** `verification_b2_2_shape_derivative.json`.
