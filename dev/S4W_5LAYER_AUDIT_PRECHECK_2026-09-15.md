# S4W — auditoría adversarial preliminar del candidato de cinco capas

**Fecha:** 2026-09-15  
**Objeto auditado:** `dev/S4W_5LAYER_KRETSCHMANN_CANDIDATE.md`  
**Commit candidato:** `15eb7a500f18abc401f3671edecc65a995ef3e89`  
**Estado:** `INTERNAL_ADVERSARIAL_PRECHECK / NOT_AN_INDEPENDENT_AUDIT`

> Esta revisión se hace después de congelar el candidato y en un commit separado. No debe etiquetarse como auditoría independiente multi-modelo o multi-sesión. Su función es detectar fallos antes de gastar una auditoría independiente.

## Veredicto

```text
S4W_5LAYER_OPERATOR_ALGEBRA = PASS_EXACT
S4W_W2_EXTRA_ROOT = PASS_EXACT
S4W_W2_ASYMPTOTIC_IMPROVEMENT = CONDITIONAL / PROOF_MISSING
S4W_LOCAL_C2_COEFFICIENT = FAIL_AS_DERIVED
S4W_KRETSCHMANN_ESTIMATOR = NOT_ESTABLISHED
AUDIT_PRECHECK_VERDICT = REQUIRES_MAJOR_FIX
MERGE_TO_RELATIVIDAD = NOT_AUTHORIZED
SIMULATION = NOT_AUTHORIZED
```

El fallo afecta al coeficiente local y al estimador Kretschmann propuesto. No invalida la existencia exacta del operador generalizado de cinco capas ni su raíz adicional `H=-2`.

## 1. Algebra GCD 4D — PASS exacto

Fuente primaria: A. Belenchia, arXiv:1510.04665, ecuaciones de la familia GCD en dimensión par.

Para D=4 (`N=1`) se reprodujeron las tres condiciones homogéneas sobre `b_n` con exponentes Gamma `1/2`, `1`, `3/2`, la condición digamma de normalización en `3/2` y la ecuación

\[
a+3\sum_n b_n\psi(n+1)=0.
\]

Para

\[
\delta b=(3,-47,148,-168,64)
\]

se verifica exactamente

\[
\sum_{n=0}^4\frac{\delta b_n}{n!}\Gamma(n+1/2)=0,
\]
\[
\sum_{n=0}^4\frac{\delta b_n}{n!}\Gamma(n+1)=0,
\]
\[
\sum_{n=0}^4\frac{\delta b_n}{n!}\Gamma(n+3/2)=0,
\]
\[
\sum_{n=0}^4\frac{\delta b_n}{n!}\Gamma(n+3/2)\psi(n+3/2)=0,
\]

y

\[
\sum_{n=0}^4\delta b_n\psi(n+1)=\frac13,
\]

por lo que `delta a=-1` es correcto.

También se reprodujo

\[
M_2(b_{BD})=-\frac{2\sqrt6}{3},
\qquad
M_2(\delta b)=1,
\]

de donde

\[
\lambda_*=\frac{2\sqrt6}{3}.
\]

Así se obtienen exactamente

\[
a_*=-\frac{4\sqrt6}{3},
\]

\[
b_*=\frac{8\sqrt6}{3}(1,-14,41,-44,16).
\]

## 2. Factorización del kernel — PASS exacto

Con `H=rho d/drho` y `H_n=rho^n d^n/drho^n`, la combinación normalizada satisface

\[
\sum_{n=0}^{4}\frac{c_n}{n!}(-1)^nH_n
=
\frac23(H+1/2)(H+1)(H+3/2)(H+2),
\]

para `c=(1,-14,41,-44,16)`.

Para BD,

\[
\widehat{\mathcal O}_{BD}
=\frac43(H+1/2)(H+1)(H+3/2),
\]

y por tanto

\[
\widehat{\mathcal O}_*=\frac12(H+2)\widehat{\mathcal O}_{BD}.
\]

La raíz nueva `H=-2` y la anulación algebraica de una potencia pura `rho^{-2}` son correctas.

## 3. Sector W2 — plausible, pero aún no probado

Belenchia–Benincasa–Dowker, arXiv:1510.04656, demuestran para el operador mínimo 4D que la contribución `I_2` de la región pegada al cono nulo satisface `O(rho^-2)`. Su operador anula exactamente `rho^-1/2`, `rho^-1` y `rho^-3/2`.

La raíz adicional `H=-2` hace plausible que, si la integral previa a `O_*` admite una expansión asintótica uniforme en semipotencias,

\[
F(\rho)\sim\sum_{j\ge1}c_j\rho^{-j/2},
\]

los cuatro primeros términos sean eliminados y quede `O(rho^-5/2)`.

Pero la prueba publicada del caso mínimo no se reduce a invocar formalmente una serie: usa cotas separadas y una parametrización curva de `W2`. Por tanto, de

\[
\widehat{\mathcal O}_*\rho^{-2}=0
\]

NO se sigue todavía, sin un lema uniforme adicional,

\[
I_{2,*}=O(\rho^{-5/2}).
\]

### Proof obligation exacta

Probar un Watson/Laplace lemma uniforme sobre el dominio compacto longitudinal de `W2`, con mínimo cuadrático no degenerado en el coordenado transversal y amplitud suficientemente regular, controlando el resto hasta orden `rho^-5/2` y mostrando que no aparecen términos `rho^-2 log rho` u otros que sobrevivan a `H+2`.

Hasta entonces:

```text
S4W_W2_IMPROVEMENT = CONDITIONAL
```

## 4. Fallo decisivo en el coeficiente local — FAIL

La derivación preliminar especializó la ecuación (79) de Wang, arXiv:1904.01034, a Schwarzschild usando `H=0`, `D^2=4E^2` y `K=8E^2`, obteniendo correctamente **para un ACD cuyo eje temporal coincide con el observador estático**

\[
V_4(l)=\frac{2\pi}{3}l^4+
\frac{127\pi}{56700}K l^8+O(l^9).
\]

El problema es que ése NO es el objeto que puede insertarse como una corrección escalar fija en toda la integral `W1`.

### 4.1 Dependencia de observer/orientation en Wang

Wang define

\[
E_{ij}=C_{0i0j},\qquad H_{ijk}=C_{0ijk},\qquad D_{ijkl}=C_{ijkl}
\]

respecto de un vector temporal unitario `U`. Para el Alexandrov causal diamond, `U` es la tangente de la geodésica temporal que une los extremos del diamante.

En la integral de Belenchia–Benincasa–Dowker, el punto pasado `y` recorre **todas** las direcciones temporales dentro del cono. Por tanto el ACD `I(y,x)` posee una orientación `U_y` que depende de `y`; no coincide en general con el observador estático de Schwarzschild fijado en `x`.

Schwarzschild es puramente eléctrico (`B_ij=0`) para los observadores estáticos, pero un boost genérico produce parte magnética no nula. No es lícito fijar `H=0` para todos los intervalos `I(y,x)` de la integral.

### 4.2 La propia fórmula de Wang exhibe el problema

Para `d=4`, usando sólo la identidad dimensional `D^2=4E^2`, la corrección de Wang contiene

\[
2032 E^2+360H^2,
\]

antes de especializar el observador. En 4D `H^2` es proporcional a `B^2`; por tanto la corrección de volumen depende de la descomposición eléctrica/magnética relativa a `U_y`, no sólo del escalar `C^2`, punto a punto en el dominio de integración.

La reducción

\[
2032E^2+360H^2\longrightarrow 2032E^2
\longrightarrow \text{constante}\times K
\]

sólo es válida en el frame puramente eléctrico, no uniformemente sobre los `y` integrados.

### 4.3 Consecuencia

Quedan invalidados como derivación establecida:

\[
A_{33}=\frac{584\pi}{1575}e^2,
\]

\[
\mathbb E[B_*1]
=-\frac{73\sqrt6}{1575\pi}K\rho^{-1/2}+o(\rho^{-1/2}),
\]

y el estimador normalizado construido con ese coeficiente.

No se concluye que el coeficiente real sea cero ni que la ruta de cinco capas falle. Se concluye sólo que el valor anunciado NO ha sido derivado correctamente.

## 5. Qué debe hacerse para reparar el cálculo local

Hay dos rutas admisibles:

1. **Ruta covariante:** reescribir la corrección de volumen ACD de Wang en términos de contracciones covariantes de `C_{abcd}` con el vector unitario `U_y=y/tau`, mantener esa dependencia dentro de la integral `W1`, combinarla con la expansión RNC de `sqrt(-g)` y sólo entonces efectuar las integraciones angular y `u,v`.
2. **Ruta tensorial directa:** derivar desde cero `V(x,y)` y `sqrt(-g(y))` en RNC a orden `C^2 y^4`, insertar en la integral media del GCD y hacer las contracciones isotrópicas antes de especializar a Schwarzschild.

La simetría/Lorentz-invariancia sugiere que, si existe una corrección local parity-even de dimensión cuatro en vacío, el resultado final debe ser proporcional a `C_{abcd}C^{abcd}`. Eso NO fija el coeficiente y no sustituye la integración.

## 6. Prior art — estado acotado

Una búsqueda académica independiente del cálculo encuentra como antecedente directo establecido de operadores de curvatura superior a de Brito–Eichhorn–Pfeiffer (EPJ Plus 2023), que obtiene `R^2-2 Box R` y análogos iterados. También confirma la familia generalizada de d'Alembertianos como prior art.

No se ha certificado prioridad para el vector concreto de cinco capas ni para un eventual coeficiente `C^2`; ausencia en una búsqueda no equivale a novedad.

## 7. Estado después del precheck

```text
KEEP:
  exact five-layer GCD direction D5
  lambda_* = 2 sqrt(6) / 3
  coefficients (-1/2; 1,-14,41,-44,16) up to common factor
  extra operator root H=-2

DO_NOT_KEEP_AS_RESULT:
  W2 = O(rho^-5/2) until uniform proof exists
  coefficient -73 sqrt(6)/(1575 pi)
  normalized K-hat formula

NEXT_SINGLE_STEP:
  repair the W1 tensor/orientation calculation analytically;
  no simulation.
```

**Una auditoría realmente independiente sigue pendiente.** Este precheck no puede sustituirla porque fue realizado en la misma línea de trabajo que generó el candidato.
