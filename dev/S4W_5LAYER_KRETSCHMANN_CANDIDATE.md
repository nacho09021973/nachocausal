# S4W — candidato analítico de cinco capas para curvatura Weyl/Kretschmann

**Fecha:** 2026-09-15  
**Rama:** `s4w-5layer-candidate`  
**Base:** `relatividad @ 008918b65d4e800b05ce8fec6908d8022e350482`  
**Estado:** `DERIVATION_CANDIDATE_FROZEN / AUDITED_2026-10-10 / NO_PHYSICAL_CLAIM / NO_SIMULATION`

> **ENMENDADO EL 2026-10-10 tras la auditoría independiente.** El texto de 1 a 9 se conserva tal
> como se congeló el 2026-09-15; las enmiendas van al final, en el §10, y afectan a **§3** (falta
> una cita), **§6** (la conclusión es correcta pero la justificación no, y además no está
> probada) y **§7** (las tres fórmulas con interrogación: la primera es **correcta como
> coeficiente local**, el estimador no está establecido). Cadena de la auditoría:
> `1e03a54` → `e4d9365` → `30f7fda` → `0c3f07f` → `38cfd39`, y nota de cierre en
> `dev/S4W_NOTA_DE_CIERRE_2026-10-10.md`.

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

> **§3, enmienda R2.** Falta la cita que convierte todo este §3 y el §4 en un caso particular:
> la ec. (13) de **Dowker–Glaser, arXiv:1305.2588**, `O_{2n} = (H+2)(H+4)...(H+2n+2)/[2^{n+1}(n+1)!]`
> con `H = -l ∂/∂l`. Ver §10.1.

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

> **§6, enmienda R2′.** La auditoría lo verificó y el resultado tiene dos partes. La
> justificación escrita arriba —«expansión uniforme de Laplace»— **no es el mecanismo**; el
> mecanismo es el factor `A_{lambda,l}(n)` de Pfeiffer 2022 (3.28), que se anula si y sólo si
> `k <= n`. Pero la conclusión **tampoco queda probada**: ese factor aniquila la integral de un
> monomio, no una cota de norma suprema, y la vía de Pfeiffer (3.15)–(3.22) pasa cotas por un
> operador diferencial. Ver §10.2.

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

> **§7, enmienda R1.** Reproducido, y por tres casas. El **coeficiente local** es correcto:
> `-73 sqrt6/(1575 pi)` por `C_abcd C^abcd`, a orden algebraico `R^2` en el canal `rho^{-1/2}`,
> y la pieza dependiente del observador se cancela exactamente en ese canal. Pero la **primera**
> fórmula, tal como está escrita —con `+ o(rho^{-1/2})`—, afirma más que eso: el control del
> resto no está probado. Y las otras dos, el estimador, **no están establecidas**. Ver §10.3.

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

---

## 10. Enmiendas de la auditoría independiente (2026-10-10)

Añadidas tras la auditoría y cuatro rondas de revisión ciega a tres casas. El texto de 1 a 9 no
se ha modificado salvo por los punteros marcados `>`. Detalle completo y procedencia en
`dev/S4W_NOTA_DE_CIERRE_2026-10-10.md`.

### 10.1 §3 y §4 — prioridad (`R2`)

`Ô_*` **es** el operador `O_6` de la ec. (13) de Dowker–Glaser (arXiv:1305.2588), evaluado con
la relación de `d = 4`, `H_DG = 4 rho ∂_rho`:

```
O_{2n} = (H_DG+2)(H_DG+4)...(H_DG+2n+2) / [2^{n+1}(n+1)!]        con  n = 3
O_6 |_{H_DG = 4 theta}  =  (2/3)(theta+1/2)(theta+1)(theta+3/2)(theta+2)   ==  Ô_*
y aplicado a e^{-w} devuelve exactamente (1,-14,41,-44,16)
```

Verificado, con control: la misma fórmula reproduce las filas `d=4` y `d=6` de su Tabla 1.
Luego «añadir una quinta capa y ajustar `lambda_*`» es, término a término, **usar el siguiente
operador de una torre publicada en 2013**. La quinta capa no es un hallazgo; el vector
`(1,-14,41,-44,16)` en `d=4` no aparece en su Tabla 1, pero la construcción sí está.

Y el **programa** está publicado: de Brito–Eichhorn–Pfeiffer (arXiv:2301.13525) lo enuncia como
dirección abierta en sus conclusiones. No hay antecedente exacto del coeficiente —la tesis de
Pfeiffer 2022, leída completa, no contiene Weyl, ni Kretschmann, ni la familia GCD no mínima—
pero no cabe reclamar novedad conceptual.

### 10.2 §6 — la mejora de `W2` (`R2'`)

Sustituir la justificación por el mecanismo correcto, **y rebajar el estado**:

```
mecanismo:  A_{lambda,l}(n) = prod_{zeta=0}^{n} ( d(l-lambda) + 2 zeta + 2 ) = prod 2(zeta-k)
            Pfeiffer 2022 (3.28);  se anula si y solo si k <= n, condicion que NO involucra l.
            El canal (3,3) tiene k=3: con cinco capas (n=3) queda aniquilado para todo l.

estado:     NO PROBADO.  Ese factor aniquila la integral exacta de un monomio.  La via de
            Pfeiffer (3.15)-(3.22) lo aplica a una cantidad donde las funciones ya se han
            sustituido por sus normas supremas, y un operador diferencial no preserva
            desigualdades.  La cota VALIDA es la de BBD ec.(25) --que acota primero y luego
            usa una identidad con el operador de signos invertidos, no con Ô-- y da
            O(rho^{-2}), es decir O(rho^{-1/2}) en B_bar: el orden de la senal.
```

Es decir: `I_{2,*} = O(rho^{-5/2})` **no está establecido**, y el `F2` de la auditoría —`W2`
vive en el orden de la señal— sigue en pie.

### 10.3 §7 — el coeficiente (`R1`)

```
ESTABLECIDO (tres casas):
    coeficiente local algebraico, orden R^2, canal rho^{-1/2}:
        -(73 sqrt6 / (1575 pi)) · C_abcd C^abcd
    con la pieza dependiente del observador EXACTAMENTE CERO en ese canal.

NO ESTABLECIDO:
    la primera formula del §7 tal como esta escrita, con "+ o(rho^{-1/2})": el control del
    resto depende de §10.2 y no esta probado.
    El estimador K_hat_rho y su version en conteos de capas: NO ESTABLECIDOS.
```

El mecanismo de la cancelación, que el candidato no tenía: las dos formas cuárticas reparten la
densidad de Bel–Robinson con coeficiente **uniforme** sobre `u^4, u^3v, u^2v^2, uv^3, v^4`, y la
medida `(v-u)^{d-2}` tiene coeficientes `1,-2,1` que suman cero. Sobrevive sólo el exceso no
uniforme, que es puro invariante. Equivalente: `Q = T(y^4)/2 + K (y·y)^2/16`.

### 10.4 §8 — los claims prohibidos siguen prohibidos

La lista del §8 del candidato se mantiene **entera**. Nada de lo auditado toca las
fluctuaciones, que no se han estudiado en absoluto, ni la varianza, ni la convergencia
realización por realización, ni la localización de horizonte.

Los tokens del §8 quedan así:

```
S4W_5LAYER_OPERATOR_ALGEBRA   = PASS_EXACT / INDEPENDENTLY_REPRODUCED / PRIOR_ART_DOWKER_GLASER
S4W_W2_IMPROVEMENT            = NOT_PROVEN (mecanismo identificado, prueba invalida)
S4W_LOCAL_C2_COEFFICIENT      = ESTABLISHED_LOCAL = -73 sqrt6/(1575 pi)
S4W_GLOBAL_MEAN               = NOT_ESTABLISHED (falta el control del resto)
S4W_PHYSICAL_ESTIMATOR        = NOT_ESTABLISHED
MERGE_TO_RELATIVIDAD          = NOT_AUTHORIZED
SIMULATION                    = NOT_AUTHORIZED
```
