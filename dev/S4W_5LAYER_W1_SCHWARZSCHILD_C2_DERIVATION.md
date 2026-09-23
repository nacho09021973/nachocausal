# S4W — derivación covariante W1 del término Schwarzschild Weyl/Kretschmann

**Fecha:** 2026-09-15  
**Rama:** `s4w-5layer-candidate`  
**Base inmediata:** `8fedec4812b0d71653893c17d982d60b4325b40d`  
**Estado:** `DERIVATION_CANDIDATE_FROZEN / INDEPENDENT_AUDIT_REQUIRED / NO_GLOBAL_PHI1_CLAIM / NO_SIMULATION`

Este documento congela una derivación candidata para la contribución local `W1` del operador GCD de cinco capas. No constituye todavía un teorema del proyecto. En particular, el coeficiente final debe ser reproducido en una auditoría independiente antes de cualquier merge a `relatividad` o de cualquier simulación.

Fuentes primarias de referencia:

- Belenchia–Benincasa–Dowker, arXiv:1510.04656 — región local `W1`, coordenadas nulas y estructura del límite continuo 4D.
- Wang, arXiv:1904.01034 — expansión del volumen de pequeños Alexandrov causal diamonds y descomposición eléctrica/magnética de Weyl respecto a la orientación temporal del diamante.
- Belenchia, arXiv:1510.04665 — familia de generalized causal-set d'Alembertians.

## 1. Objeto

Para el operador de cinco capas

\[
B_*\phi(x)=\frac{8\sqrt6}{3}\rho^{1/2}
\left[-\frac12\phi(x)+\sum_{L_1}\phi-14\sum_{L_2}\phi+41\sum_{L_3}\phi-44\sum_{L_4}\phi+16\sum_{L_5}\phi\right],
\]

con

\[
\widehat{\mathcal O}_*
=\frac23(H+\tfrac12)(H+1)(H+\tfrac32)(H+2),
\qquad H=\rho\partial_\rho,
\]

queremos aislar, en Schwarzschild 4D Ricci-flat y con regulador compacto fijo que vale 1 en una vecindad de `x`, la contribución local de orden

\[
C_{abcd}C^{abcd}\rho^{-1/2}.
\]

El resultado candidato que se deriva abajo es

\[
\boxed{
\mathbb E[B_*1(x)]_{W1}
=
-\frac{73\sqrt6}{1575\pi}
C_{abcd}C^{abcd}(x)\rho^{-1/2}
+o(\rho^{-1/2}).
}
\]

La etiqueta `candidate` es vinculante hasta auditoría independiente.

## 2. Geometría local W1

En la región RNC local de BBD usamos

\[
0\le u\le v\le a,
\]

\[
V_0(y)=\frac\pi6u^2v^2,
\qquad
\sigma=\frac{\pi\rho}{6},
\]

y el jacobiano plano

\[
d^4y=\frac12(v-u)^2\,du\,dv\,d\Omega.
\]

Las coordenadas temporal y radial son

\[
t=-\frac{u+v}{\sqrt2},
\qquad
r=\frac{v-u}{\sqrt2},
\qquad
\tau^2=t^2-r^2=2uv.
\]

Para `phi=1` localmente y en vacío Ricci-flat, el primer término de curvatura relevante es cuadrático en Weyl:

\[
J_{C^2}
=
\int_{W1}d^4y\,e^{-\rho V_0}
\left[
\delta\sqrt{-g}
-
\rho\,\delta V
\right].
\]

No se usa una fijación global del frame estático dentro de `\delta V`: la orientación temporal del ACD `I(y,x)` se mantiene como `U_y` hasta después de reescribir el resultado covariantemente.

## 3. Corrección de volumen ACD en forma covariante

La expansión de Wang en `d=4` y vacío contiene, después de usar `D^2=4E^2`, la combinación

\[
2032E(U)^2+360H(U)^2.
\]

En cuatro dimensiones, con `H^2=2B^2`, definimos

\[
K=C_{abcd}C^{abcd}=8(E^2-B^2)
\]

y la densidad de Bel–Robinson

\[
W(U)=E^2+B^2=T_{abcd}U^aU^bU^cU^d.
\]

La identidad algebraica exacta es

\[
2032E^2+360H^2
=82K+1376W(U).
\]

La corrección del volumen puede escribirse entonces como

\[
\delta V
=
\frac{\pi l^8}{113400}
\left[82K+1376W(U_y)\right].
\]

Como `\tau=2l` y

\[
U_y^a=\frac{y^a}{\tau},
\]

se obtiene

\[
\boxed{
\delta V(y)
=
\frac{\pi}{29030400}
\left[
82K\tau^8
+1376\tau^4T_{abcd}y^ay^by^cy^d
\right].
}
\]

Esta forma conserva explícitamente la dependencia de orientación que invalidó la primera derivación preliminar.

## 4. Especialización a Schwarzschild sólo después de covariantizar

En la tétrada estática de Schwarzschild,

\[
B_{ij}=0,
\qquad
T_{0000}=E^2=\frac K8.
\]

El tensor de Bel–Robinson es totalmente simétrico y sin traza. El promedio angular de la contracción cuártica es

\[
\boxed{
\left\langle T_{abcd}y^ay^by^cy^d\right\rangle_\Omega
=
\frac K8
\left(
 t^4+2t^2r^2+\frac15r^4
\right).
}
\]

Así,

\[
\boxed{
\left\langle\delta V\right\rangle_\Omega
=
\frac{\pi K}{29030400}
\left[
82\tau^8
+172\tau^4
\left(
 t^4+2t^2r^2+\frac15r^4
\right)
\right].
}
\]

Este resultado es compatible con el chequeo simbólico separado en boosts arbitrarios: la dependencia aparentemente creciente en rapidez queda absorbida aquí en el polinomio regular `T_{abcd}y^ay^by^cy^d` dentro de la región local `W1`.

## 5. Corrección del elemento de volumen RNC

A orden cuadrático en Weyl, la expansión RNC relevante es

\[
\sqrt{-g}
=
1-rac1{180}
C^\gamma{}_{\mu}{}^\alpha{}_{\nu}
C_{\gamma\rho\alpha\sigma}
 y^\mu y^\nu y^\rho y^\sigma+\cdots.
\]

Para Schwarzschild, tras la contracción y promedio angular,

\[
\boxed{
\left\langle\delta\sqrt{-g}\right\rangle_\Omega
=
-K\left(
\frac{t^4}{1440}
+
\frac{r^4}{2400}
\right).
}
\]

Esta fórmula debe ser reproducida de forma independiente en el audit; un error aquí cambiaría el coeficiente final.

## 6. Reducción a los monomios diagonales

Sustituyendo

\[
t=-\frac{u+v}{\sqrt2},
\qquad
r=\frac{v-u}{\sqrt2},
\qquad
\tau^2=2uv,
\]

y multiplicando por el jacobiano

\[
\frac12(v-u)^2,
\]

el término de medida tiene grado total 6. Su coeficiente diagonal es

\[
\boxed{
\left[
\frac12(v-u)^2
\left\langle\delta\sqrt{-g}\right\rangle_\Omega
\right]_{u^3v^3}
=
\frac K{720}u^3v^3.
}
\]

El término de volumen tiene grado total 10 y satisface

\[
\boxed{
\left[
\frac12(v-u)^2
\left\langle\delta V\right\rangle_\Omega
\right]_{u^5v^5}
=
-\frac{41\pi K}{907200}u^5v^5.
}
\]

Todos los demás monomios relevantes son off-diagonal `u^p v^q` con `p\ne q`.

## 7. Integrales Z_pq y por qué sólo sobreviven los diagonales

Definimos

\[
Z_{pq}(\sigma)
=
\int_0^a dv\int_0^vdu\,
 u^pv^q e^{-\sigma u^2v^2}.
\]

Para `p\ne q`, la expansión contiene sólo potencias puras de `\sigma`, esquemáticamente

\[
Z_{pq}
=
\frac1{q-p}
\left[
 a^{q-p}\frac{\Gamma((p+1)/2)}2\sigma^{-(p+1)/2}
-
\frac{\Gamma((p+q+2)/4)}2\sigma^{-(p+q+2)/4}
\right]
+
O(e^{-c\sigma}).
\]

Las raíces

\[
-\frac12,-1,-\frac32,-2
\]

de `\widehat{\mathcal O}_*` anulan las potencias que podrían contribuir hasta el orden buscado.

Cuando `p=q=m` aparece el logaritmo:

\[
Z_{mm}
=
\frac18\Gamma\!\left(\frac{m+1}{2}\right)
\sigma^{-(m+1)/2}\log\sigma
+O(\sigma^{-(m+1)/2}).
\]

En particular,

\[
Z_{33}
=
\frac18\sigma^{-2}\log\sigma+\cdots,
\]

\[
Z_{55}
=
\frac14\sigma^{-3}\log\sigma+\cdots.
\]

Por ello los dos coeficientes diagonales de la sección anterior determinan el término `\sigma^{-2}\log\sigma` completo a este orden.

## 8. Contribución del elemento de volumen

Después de integrar `d\Omega`, el monomio `u^3v^3` produce

\[
4\pi\frac K{720}Z_{33}.
\]

Por tanto,

\[
\boxed{
J_{\sqrt{-g}}
=
\frac{\pi K}{1440}
\sigma^{-2}\log\sigma
+\text{potencias anuladas}
+o(\sigma^{-2}).
}
\]

## 9. Contribución de `-rho delta V`

El monomio diagonal de `\delta V` da, tras el factor `-\rho` y la integración angular,

\[
-\rho\,4\pi
\left(-\frac{41\pi K}{907200}\right)Z_{55}.
\]

Usando

\[
\rho=\frac{6\sigma}{\pi},
\]

resulta

\[
\boxed{
J_{\delta V}
=
\frac{41\pi K}{151200}
\sigma^{-2}\log\sigma
+\text{potencias anuladas}
+o(\sigma^{-2}).
}
\]

## 10. Suma W1 previa al operador de densidad

Sumando ambos términos,

\[
\frac1{1440}+\frac{41}{151200}
=
\frac{73}{75600},
\]

de modo que

\[
\boxed{
J_{C^2}
=
\frac{73\pi K}{75600}
\sigma^{-2}\log\sigma
+
\text{potencias anuladas}
+
o(\sigma^{-2}).
}
\]

## 11. Acción de la raíz adicional H=-2

Como `\sigma` es proporcional a `\rho`, el operador `H=\rho\partial_\rho` actúa también como `\sigma\partial_\sigma`. Se verifica exactamente

\[
\boxed{
\widehat{\mathcal O}_*
\left(\sigma^{-2}\log\sigma\right)
=
-\frac12\sigma^{-2}.
}
\]

Por tanto,

\[
\boxed{
I_{1,*}^{(C^2)}
=
-\frac{73\pi K}{151200}
\sigma^{-2}
+
o(\sigma^{-2}).
}
\]

## 12. Prefactor del operador discreto

El término integral en `B_*` lleva

\[
\frac{8\sqrt6}{3}\rho^{3/2}.
\]

Además,

\[
\sigma^{-2}
=
\frac{36}{\pi^2\rho^2}.
\]

Entonces

\[
\frac{8\sqrt6}{3}\rho^{3/2}
\left(-\frac{73\pi K}{151200}\right)
\frac{36}{\pi^2\rho^2}
=
-\frac{73\sqrt6}{1575\pi}
K\rho^{-1/2}.
\]

Resultado candidato final:

\[
\boxed{
\mathbb E[B_*1(x)]_{W1}
=
-\frac{73\sqrt6}{1575\pi}
C_{abcd}C^{abcd}(x)\rho^{-1/2}
+o(\rho^{-1/2}).
}
\]

## 13. Combinación con el lema W2 ya congelado

El commit inmediatamente anterior prueba, para `W2` compacto fijo y bajo sus hipótesis de uniformidad,

\[
\langle B_*\rangle_{W2}=O(\rho^{-1})
=o(\rho^{-1/2}).
\]

Por tanto, **condicionado a que esta derivación W1 pase la auditoría independiente**, `W2` no contamina el coeficiente local `C^2\rho^{-1/2}` en el problema regulado compacto.

La combinación candidata sería

\[
\boxed{
\mathbb E[B_*1(x)]
=
-\frac{73\sqrt6}{1575\pi}
C_{abcd}C^{abcd}(x)\rho^{-1/2}
+o(\rho^{-1/2})
}
\]

para un regulador compacto fijo igual a 1 cerca de `x`.

## 14. Estimador regulado candidato

Si el coeficiente sobrevive al audit, puede definirse formalmente

\[
\boxed{
\widehat K_\rho(x)
=
-\frac{1575\pi}{73\sqrt6}
\rho^{1/2}B_*1(x),
}
\]

con media asintótica candidata

\[
\mathbb E[\widehat K_\rho(x)]\to
C_{abcd}C^{abcd}(x)
\]

en Schwarzschild Ricci-flat bajo el esquema regulado.

Este estimador **NO está establecido** hasta auditoría independiente.

## 15. Frontera de claims

Estado permitido tras congelar esta derivación:

```text
S4W_5LAYER_ALGEBRA = PASS_EXACT
S4W_W2_FIXED_COMPACT = PROVED_O_RHO_MINUS_1
S4W_W1_SCHWARZSCHILD_C2 = DERIVED_COVARIANTLY / INDEPENDENT_AUDIT_PENDING
S4W_W1_CANDIDATE_COEFFICIENT = -73*sqrt(6)/(1575*pi)
S4W_COMPACT_REGULATED_K_ESTIMATOR = ANALYTIC_CANDIDATE
S4W_GLOBAL_PHI_EQUALS_1 = OPEN
S4W_UNIFORM_LONGITUDINAL_CUTOFF_REMOVAL = OPEN
S4W_VARIANCE = OPEN
S4W_REALIZATION_LEVEL_CONSISTENCY = OPEN
S4W_HORIZON_LOCALIZATION = NOT_CLAIMED
S4W_NOVELTY = NOT_CERTIFIED
```

No autoriza:

- merge a `relatividad`;
- simulaciones;
- claim global con `phi=1` en pasado no compacto;
- varianza controlada;
- consistencia realización por realización;
- localización de horizonte/Page–Shoom;
- reconstrucción de Schwarzschild;
- prioridad o novedad.

## 16. Audit mínimo requerido

La auditoría independiente debe reproducir, sin copiar números de este documento:

1. la identidad `2032 E^2 + 360 H^2 = 82 K + 1376 W(U)` con las convenciones exactas de Wang;
2. el paso `tau=2l` y la normalización `pi/29030400`;
3. el promedio angular del Bel–Robinson en Schwarzschild;
4. la contracción RNC que produce
   `-K(t^4/1440 + r^4/2400)`;
5. los coeficientes diagonales `K/720` y `-41*pi*K/907200`;
6. las fórmulas `Z_33`, `Z_55` y la exclusión de otros términos al orden relevante;
7. la acción exacta de `O_*` sobre `sigma^-2 log sigma`;
8. la normalización final `-73*sqrt(6)/(1575*pi)`.

Cualquier fallo en 3–8 invalida el coeficiente físico aunque no invalide el operador de cinco capas ni el teorema compacto W2.
