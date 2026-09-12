# B4.3 — Derivadas de forma directas de los momentos `n=3`

> **STATUS: `PARKED / ANALYTIC_DERIVATION_AVAILABLE / N3_RANK_UNRESOLVED`.**
> El objetivo es reemplazar la diferenciación numérica de los momentos de B4.1/B4.2.

## 1. Núcleo y normalización

Sea `w(z)=G(UV)`, `Z=integral_K w(z) dz` y `h(x,y)` la probabilidad angular causal obtenida de
B1.2. El núcleo ambiental `h` no depende del parámetro de forma; sólo se mueve `K`.

Definimos

```text
F(x) = integral_K w(y) h(x,y) dy,
P(x) = integral_K w(y) h(y,x) dy,
f(x)=F(x)/Z,  p(x)=P(x)/Z.
```

La simetría causal no se impone entre `F` y `P`; sí se tiene `integral_K w F = integral_K w P`.

## 2. Derivada de los conos truncados

Para una velocidad de deformación `a` de las cuatro caras de `K`, la derivada de forma de `F`
para un punto interior fijo es

```text
DF[a](x) = integral_{boundary K} w(y) h(x,y) a_n(y) dS_y.
```

Análogamente,

```text
DP[a](x) = integral_{boundary K} w(y) h(y,x) a_n(y) dS_y.
```

No aparece una derivada del argmax angular: `h` se considera el núcleo causal fijo del ambiente;
la evaluación de sus cotas se hace antes de integrar. Esto es la separación correcta entre
movimiento de dominio y causalidad ambiental.

La normalización da

```text
Df[a](x) = (DF[a](x) Z - F(x) DZ[a]) / Z²,
Dp[a](x) = (DP[a](x) Z - P(x) DZ[a]) / Z²,
DZ[a] = integral_{boundary K} w a_n dS.
```

## 3. Derivadas de los tres momentos nuevos

Para `M_ff=E[f²]`, `M_pp=E[p²]` y `M_fp=E[f p]`, la fórmula de transporte completa es

```text
DM_ff[a] = Z^(-1) integral_boundary w f² a_n dS
           + 2 Z^(-1) integral_K w f Df[a] dz
           - M_ff DZ[a]/Z;

DM_pp[a] = Z^(-1) integral_boundary w p² a_n dS
           + 2 Z^(-1) integral_K w p Dp[a] dz
           - M_pp DZ[a]/Z;

DM_fp[a] = Z^(-1) integral_boundary w f p a_n dS
           + Z^(-1) integral_K w (Df[a] p + f Dp[a]) dz
           - M_fp DZ[a]/Z.
```

Estas expresiones separan explícitamente:

1. movimiento de `partial K` en el primer término;
2. variación de los conos `F,P` en `Df,Dp`;
3. normalización de la medida en el último término.

Junto con la fórmula ya cerrada de `D rho`, producen las doce entradas de `Dm` directamente.

## 4. Certificación prevista

La implementación siguiente debe integrar sólo estos términos con aritmética intervalar o
envolventes rigurosas de B1.2. El escalado queda fijado como en B4.1:

```text
R=diag(1,10000,10000,10000), C=I_3.
```

Terminales:

```text
B4_STRONG_POSITIVE          menor certificado != 0 o sigma_min certificado > 0;
B4_INCONCLUSIVE_BY_BOUNDS   la envolvente de Dm no alcanza el gap;
B4_NEGATIVE_EXACT_RANK      sólo con dependencia exacta demostrada.
```

## 5. Stop de gobernanza

Si la evaluación directa de estas fórmulas no produce una envolvente suficiente, B4 se aparca
como `N3_RANK_UNRESOLVED`. No se aumenta el orden estadístico, no se busca otro punto y no se
optimiza el escalado.

## 6. Intento de certificación

El backend puntual `mpmath.iv` está disponible, pero el repositorio todavía no contiene una capa
de cuadratura intervalar con resto formal para las integrales anidadas de `F/P` y sus derivadas.
El intento se detiene explícitamente en
`B4.3_IMPLEMENTATION_FAILURE`; no convierte diferencias de convergencia en cotas rigurosas.

```text
B4.3_IMPLEMENTATION_FAILURE
N3_RANK_UNRESOLVED
```

El artefacto de auditoría es `verification_b4_3_certified_enclosure.json`. B4 queda aparcado
hasta que exista esa capa formal; no se pasa a `n=4` ni se reabre ninguna elección física.

```text
B4_REOPEN_ONLY_IF = certified quadrature with formal remainder
```
