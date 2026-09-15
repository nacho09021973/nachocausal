# S4W — candidato analítico de cinco capas para curvatura Weyl/Kretschmann

**Fecha:** 2026-09-15  
**Rama:** `s4w-5layer-candidate`  
**Base:** `relatividad @ 008918b65d4e800b05ce8fec6908d8022e350482`  
**Estado:** `DERIVATION_CANDIDATE_FROZEN / INDEPENDENT_AUDIT_REQUIRED / NO_PHYSICAL_CLAIM / NO_SIMULATION`

Este documento congela una derivación candidata para auditoría. No establece un teorema, no reabre por sí solo el programa de saturación de `relatividad`, no localiza un horizonte y no autoriza simulaciones.

## 1. Pregunta acotada

En 4D Ricci-flat, ¿puede una combinación finita de capas causales, construida sólo con `order+number` y densidad de sprinkling conocida, tener una corrección local subdominante proporcional a

\[
C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}
\]

sin alterar el límite principal conocido

\[
\Box-\frac12R\,?
\]

El objetivo inmediato no es Page–Shoom ni reconstrucción de horizonte. Es aislar si existe un canal escalar 4D Weyl-sensitive dentro de la familia de generalized causal-set d'Alembertians.

## 2. Fuentes primarias usadas

- Benincasa–Dowker, *The Scalar Curvature of a Causal Set*, arXiv:1001.2725.
- Aslanbeigi–Saravani–Sorkin, *Generalized Causal Set d'Alembertians*, arXiv:1403.1622.
- Belenchia–Benincasa–Dowker, *The continuum limit of a 4-dimensional causal set scalar d'Alembertian*, arXiv:1510.04656.
- Belenchia, *Universal behaviour of generalized Causal set d'Alembertians in curved spacetime*, arXiv:1510.04665.
- de Brito–Eichhorn–Pfeiffer, *Higher-order curvature operators in causal set quantum gravity*, arXiv:2301.13525.
- Wang, *On the geometry of small causal diamonds*, arXiv:1904.01034.

La prioridad bibliográfica de cualquier observable Weyl/Kretschmann nuevo NO queda certificada por esta lista.

## 3. Familia GCD 4D y restricciones

Para D=4,

\[
(B_\rho\phi)(x)=\rho^{1/2}\left(a\phi(x)+\sum_{n=0}^{L_{\max}}b_n\sum_{y\in I_n(x)}\phi(y)\right).
\]

Las condiciones de Belenchia para conservar el límite IR imponen, sobre los `b_n`, los tres momentos homogéneos

\[
\sum_n\frac{b_n}{n!}\Gamma\!\left(n+\frac12\right)=0,
\]
\[
\sum_n\frac{b_n}{n!}\Gamma(n+1)=0,
\]
\[
\sum_n\frac{b_n}{n!}\Gamma\!\left(n+\frac32\right)=0,
\]

y una normalización digamma en el mismo exponente `3/2`. La ecuación restante fija `a` mediante

\[
a+3\sum_n b_n\psi(n+1)=0.
\]

El operador mínimo BD usa cuatro capas:

\[
a_{BD}=-\frac4{\sqrt6},
\qquad
b_{BD}=\frac4{\sqrt6}(1,-9,16,-8,0).
\]

## 4. Dirección nula exacta al añadir una quinta capa

Para cinco capas `n=0,...,4`, el sistema deja una dirección libre. La siguiente perturbación satisface exactamente las cuatro restricciones homogéneas/normalización de los `b_n`:

\[
\delta b=(3,-47,148,-168,64).
\]

Además,

\[
\sum_{n=0}^{4}\delta b_n\psi(n+1)=\frac13,
\]

por lo que la ecuación de `a` exige

\[
\delta a=-1.
\]

Así,

\[
B_\lambda=B_{BD}+\lambda D_5,
\qquad
D_5=(-1;3,-47,148,-168,64)
\]

conserva el mismo límite principal `Box-R/2` para todo `lambda` dentro de la familia GCD.

## 5. Elección que añade la raíz H=-2

Defínase

\[
M_2(b)=\sum_{n=0}^{4}\frac{b_n}{n!}\Gamma(n+2).
\]

Se obtiene exactamente

\[
M_2(b_{BD})=-\frac{2\sqrt6}{3},
\qquad
M_2(\delta b)=1.
\]

Por tanto,

\[
\lambda_*=\frac{2\sqrt6}{3}
\]

anula `M_2`. El operador resultante es

\[
\boxed{
B_*\phi(x)=\frac{8\sqrt6}{3}\rho^{1/2}
\left[-\frac12\phi(x)
+\sum_{L_1}\phi
-14\sum_{L_2}\phi
+41\sum_{L_3}\phi
-44\sum_{L_4}\phi
+16\sum_{L_5}\phi\right].
}
\]

Con `H=rho d/drho`, el operador diferencial que actúa sobre el kernel Poisson factoriza como

\[
\boxed{
\widehat{\mathcal O}_*
=\frac23\left(H+\frac12\right)(H+1)
\left(H+\frac32\right)(H+2)
=\frac12(H+2)\widehat{\mathcal O}_{BD}.
}
\]

Por construcción anula potencias `rho^{-1/2}`, `rho^{-1}`, `rho^{-3/2}` y `rho^{-2}`.

El kernel polinómico correspondiente es

\[
P_*(z)=1-14z+\frac{41}{2}z^2-\frac{22}{3}z^3+\frac23z^4.
\]

## 6. Candidato de supresión del sector down-the-light-cone

Belenchia–Benincasa–Dowker prueban para el operador mínimo que la región `W2`, pegada al cono nulo pero alejada del origen, deja `I_2=O(rho^{-2})`, suficiente para desaparecer tras el prefactor `rho^{3/2}` en el límite principal.

**Candidato a demostrar:** bajo regularidad suficiente para una expansión uniforme de Laplace en el coordenado transversal `U` de `W2`, la raíz adicional `H=-2` debe eliminar también el término `rho^{-2}`, dejando

\[
I_{2,*}=O(\rho^{-5/2}),
\qquad
\rho^{3/2}I_{2,*}=O(\rho^{-1}).
\]

Este paso NO se marca como probado aquí. La auditoría debe verificar uniformidad, regularidad, ausencia de términos logarítmicos relevantes y compatibilidad con la parametrización curva de `W2`.

## 7. Candidato local Weyl/Kretschmann — NO ESTABLECIDO

Wang obtiene para un pequeño intervalo de Alexandrov 4D en vacío una corrección de volumen de orden curvatura-cuadrada. Para Schwarzschild, si el eje temporal del diamante coincide con el observador estático, su especialización da

\[
V_4(l)=\frac{2\pi}{3}l^4+
\frac{127\pi}{56700}K\,l^8+O(l^9),
\qquad
K=C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}.
\]

Una derivación preliminar, todavía NO auditada, propuso a partir de la contribución local `W1`

\[
\mathbb E[B_*1(x)]\stackrel{?}{=}
-\frac{73\sqrt6}{1575\pi}K(x)\rho^{-1/2}
+o(\rho^{-1/2}),
\]

y por tanto el estimador candidato

\[
\widehat K_\rho(x)\stackrel{?}{=}
-\frac{1575\pi}{73\sqrt6}\rho^{1/2}B_*1(x).
\]

En conteos de capas esto sería

\[
\widehat K_\rho(x)\stackrel{?}{=}
-\frac{4200\pi}{73}\rho
\left[-\frac12+N_1-14N_2+41N_3-44N_4+16N_5\right].
\]

**Estas tres fórmulas llevan signo de interrogación de forma vinculante.** No son resultado del proyecto hasta que una auditoría independiente reproduzca el desarrollo tensorial completo.

## 8. Claims prohibidos mientras el audit esté pendiente

No afirmar:

- `KRETSCHMANN_ESTIMATOR_ESTABLISHED`;
- primer observable causal-set sensible a Weyl;
- consistencia realización-por-realización;
- varianza controlada;
- localización de horizonte;
- reconstrucción 3+1D;
- emergencia del cono causal.

Sí queda congelado como resultado algebraico candidato auditable:

```text
S4W_5LAYER_OPERATOR_ALGEBRA = EXACT_CANDIDATE
S4W_W2_IMPROVEMENT = PROOF_OBLIGATION
S4W_LOCAL_C2_COEFFICIENT = UNVERIFIED
S4W_PHYSICAL_ESTIMATOR = NOT_ESTABLISHED
```

## 9. Audit mínimo requerido

1. Reproducir exactamente las restricciones GCD 4D, la dirección nula `D5`, `lambda_*` y la factorización de `O_*`.
2. Probar o refutar `I_{2,*}=O(rho^{-5/2})` bajo hipótesis explícitas.
3. Rehacer desde cero la expansión `W1` a orden `rho^{-1/2}` en vacío, manteniendo correctamente la dependencia angular/observer-dependent de la descomposición eléctrica-magnética de Weyl.
4. Verificar la normalización completa y el coeficiente numérico; un desacuerdo en el coeficiente invalida el estimador propuesto, no el operador de cinco capas.
5. Separar prioridad bibliográfica de corrección matemática.

**STOP:** no simulación ni merge antes de audit independiente.
