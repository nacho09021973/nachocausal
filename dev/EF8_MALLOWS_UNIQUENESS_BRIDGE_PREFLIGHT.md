# EF-8 — preflight del puente Mallows a `MIN_COVERAGE_LEX`

```text
ESTADO: COMPLETE_DEDUCTIVE_PREFLIGHT
FECHA: 2026-08-13
TERMINAL: BLOCKED_BY_GLOBAL_RIVAL_CONTROL
EF8_STATUS: NOT_OPENED
MODELO: fixed-n, d=2
MONTE_CARLO: NO EJECUTADO
ENUMERACION: NO EJECUTADA
CODIGO NUEVO O MODIFICADO: NINGUNO
```

## 1. Pregunta

Sea \(\Pi_n\) una permutación uniforme de \(\mathfrak S_n\), sea

\[
 A_n(\delta)
 :=\left\{t_{21}(L_n)\le\delta\right\}
 =\left\{\operatorname{Inv}(\Pi_n)
          \le\delta\binom n2\right\},
 \qquad 0<\delta<\frac12,
\tag{1.1}
\]

y sea

\[
 S_n:=\{\texttt{MIN_COVERAGE_LEX es UNIQUE}\}.
\tag{1.2}
\]

La obligación examinada es

\[
 -\log \Pr(S_n\mid A_n(\delta))=o(n).
\tag{1.3}
\]

El intervalo abierto en (1.1) es deliberado. Es el régimen no degenerado de
lower tails con parámetro de Mallows finito. En el extremo \(\delta=0\), la ley
condicionada está soportada por la identidad. Para \(n\) par la identidad tiene
ganador único, pero para \(n=2s+1\) hay dos particiones óptimas de la cadena, de
tamaños \((s,s+1)\) y \((s+1,s)\); por tanto el selector da `TIE`. No puede
formularse un resultado uniforme en toda la sucesión que incluya ese extremo.

Este documento no abre EF-8. Audita si el certificado prescrito de EF-4 puede
aportar (1.3) y localiza la primera obligación que no cubre la maquinaria
existente.

## 2. Estado previo que se conserva

Se mantienen sin reabrir las conclusiones del preflight anterior:

```text
PREFLIGHT_PREVIO = PASS_SURROGATE_ONLY
EF8_STATUS = NOT_OPENED
```

En particular:

1. `MIN_COVERAGE_LEX/UNIQUE` no es una función del permutón límite;
2. bajo la ley uniforme, \(-\log\Pr(S_n)=o(n)\);
3. condicionado por \(A_n(\delta)\), el permutón típico converge al único
   permutón de Mallows \(\nu_{\theta(\delta)}\);
4. esa convergencia macroscópica no implica (1.3).

La aportación nueva del presente preflight es separar rigurosamente dos hechos:

- la **prescripción parcial** de EF-4 sigue teniendo coste adicional \(o(n)\)
  dentro de \(A_n(\delta)\);
- el evento de **buenas completaciones** usado por EF-4 es, para
  \(\delta<1/2\) fijo, asintóticamente incompatible con \(A_n(\delta)\).

Así, el obstáculo no es plantar el candidato balanceado con masa suficiente. Es
controlar a todos sus rivales bajo la completación de tipo Mallows.

## 3. Traducción exacta del puente a probabilidades

La afirmación deseada equivale a cualquiera de

\[
 \Pr(S_n\mid A_n(\delta))=\exp[-o(n)]
\tag{3.1}
\]

o

\[
 -\log\Pr(S_n\cap A_n(\delta))
 =-\log\Pr(A_n(\delta))+o(n).
\tag{3.2}
\]

No se necesita independencia. Si \(F_n\) es una prescripción parcial y
\(H_{n,\delta}\) un evento de buenas completaciones tal que

\[
 F_n\cap A_n(\delta)\cap H_{n,\delta}\subseteq S_n,
\tag{3.3}
\]

bastaría probar las dos cotas

\[
 -\log\Pr(F_n\mid A_n(\delta))=o(n)
\tag{3.4}
\]

y

\[
 -\log\Pr(H_{n,\delta}\mid F_n,A_n(\delta))=o(n).
\tag{3.5}
\]

En efecto,

\[
 \Pr(S_n\mid A_n(\delta))
 \ge
 \Pr(F_n\mid A_n(\delta))
 \Pr(H_{n,\delta}\mid F_n,A_n(\delta)).
\tag{3.6}
\]

Este preflight demuestra (3.4) para la prescripción exacta de EF-4, pero no
obtiene un \(H_{n,\delta}\) que satisfaga simultáneamente (3.3) y (3.5).

## 4. Auditoría de la construcción EF-4

### 4.1 La prescripción par

Para \(n=2s\), EF-4 fija

\[
 \rho_n=\left\lceil(n^2\log n)^{1/3}\right\rceil,
 \qquad R_n=2\rho_n+2,
 \qquad N_n=n-R_n,
\tag{4.1}
\]

y prescribe las cuatro esquinas

\[
 (1,1),\quad(s,s),\quad(s+1,s+1),\quad(n,n),
\tag{4.2}
\]

junto con dos escaleras de \(\rho_n-1\) puntos, una en las filas
inmediatamente anteriores a \(s\) y columnas próximas a \(n/4\), y otra en las
filas inmediatamente posteriores a \(s+1\) y columnas próximas a \(3n/4\).
El evento resultante es \(F_n\).

La cuádrupla plantada

\[
 q_0=((1,1),(s,s),(s+1,s+1),(n,n))
\tag{4.3}
\]

es admisible sobre toda completación de \(F_n\). Cada lado contiene
\(p_0=\rho_n+1\) puntos prescritos. Además, el número de filas y columnas
libres en cada mitad es \(N_n/2\), y la conservación de flujo de la biyección
residual da

\[
 X_-=X_+
\tag{4.4}
\]

para **cada** completación. El balance bilateral del candidato plantado no es
una afirmación probabilística.

### 4.2 Qué es combinatorio y qué usa la ley uniforme

| Pieza de EF-4 | Naturaleza | Qué deja de estar disponible al condicionar por inversiones |
|---|---|---|
| Filas y columnas prescritas distintas | Combinatoria | Nada; sigue siendo cierto |
| Admisibilidad de \(q_0\) y conteo prescrito \(p_0\) | Combinatoria | Nada |
| Igualdad \(X_-=X_+\) | Combinatoria, válida para toda completación | Nada |
| \(\Pr(F_n)=1/(n)_{R_n}\) | Uniformidad sobre \(\mathfrak S_n\) | No es la probabilidad condicionada |
| Residual uniforme sobre \(\mathfrak S_{N_n}\) dado \(F_n\) | Uniformidad | Falla después de añadir \(A_n(\delta)\) |
| Media rectangular \(Nuv\) y cola hipergeométrica | Residual uniforme | Falla bajo el macroestado de Mallows |
| Tricotomía geométrica de rivales | Combinatoria | Sigue siendo cierta |
| Cauchy \(\sqrt{f_-}+\sqrt{f_+}\le1\) para productos de fracciones | Combinatoria | Sigue siendo cierta, pero ya no aproxima conteos reales |
| Márgenes \(\rho_n/2-o(\rho_n)\) sobre el evento \(G_n\) | Combinatoria una vez supuesto \(G_n\) | No sirve sin un sustituto de \(G_n\) |
| \(F_n\cap G_n\subseteq S_n\) | Implicación determinista | Sigue siendo cierta, pero su lado izquierdo será incompatible con \(A_n(\delta)\) |
| Masa \(1-O(n^{-2})\) de \(G_n\mid F_n\) | Residual uniforme | No se transfiere |
| Inyección par--impar que añade \((n,1)\) | Preservación combinatoria del ganador | No preserva el umbral de inversiones |

La conclusión exacta es que EF-4 no prueba unicidad para toda completación de
\(F_n\). Prueba unicidad para completaciones cuya discrepancia rectangular está
centrada en el producto uniforme.

### 4.3 La transferencia impar tampoco es literal

La inyección de EF-4 envía \(\sigma\in\mathfrak S_{n-1}\) a

\[
 \pi(i)=\sigma(i)+1\ (i<n),
 \qquad \pi(n)=1.
\tag{4.5}
\]

El punto nuevo es incomparable con todos los anteriores y, por ello, no cambia
intervalos, scores ni ganador. Sin embargo,

\[
 \operatorname{Inv}(\pi)
 =\operatorname{Inv}(\sigma)+(n-1).
\tag{4.6}
\]

El aumento permitido al pasar del umbral de tamaño \(n-1\) al de tamaño \(n\)
es solo \(\delta(n-1)\). Para \(\delta<1\), (4.5) exige un buffer adicional

\[
 \operatorname{Inv}(\sigma)
 \le
 \delta\binom{n-1}{2}-(1-\delta)(n-1).
\tag{4.7}
\]

Por tanto, la desigualdad factorial de EF-4 no se puede insertar sin cambios en
el ensemble condicionado. El desplazamiento de (4.7) es solo \(O(n)\) en número
de inversiones y no cambia por sí mismo la tasa macroscópica, pero controlar
`UNIQUE` bajo ese buffer vuelve a requerir el puente que se está intentando
probar.

## 5. Análisis bajo el macroestado y bajo Mallows

### 5.1 Lo que proporciona literalmente el LDP

Para la permutación uniforme, el Corolario 1.7 de Borga--Das--Mukherjee--Winkler
da un LDP de velocidad \(n\) para el permutón empírico, con tasa
\(D(\mu\Vert\lambda)\). El Teorema 1.20 y su Remark 1.21 tratan el
condicionamiento por una densidad atípica de patrones y señalan explícitamente
que el resultado tiene la adaptación análoga a lower tails. En el caso estándar
de inversiones, la unicidad del optimizador de Mallows da, para
\(0<\delta<1/2\), el macroestado único \(\nu_{\theta(\delta)}\).

Es útil escribir la tasa lower-tail como

\[
 J(\delta)
 :=\inf_{\mu:\,t_{21}(\mu)\le\delta}
 D(\mu\Vert\lambda).
\tag{5.1}
\]

En el intervalo abierto considerado, la tasa es continua y

\[
 \log\Pr(A_n(\delta))=-nJ(\delta)+o(n).
\tag{5.2}
\]

El Teorema 1.29(ii) del artículo está formulado para la cola superior de la base
uniforme. El uso aquí de la cola inferior se obtiene por la simetría que envía
inversiones a no inversiones, junto con Remark 1.21; no se atribuye a
Theorem 1.29(ii) una frase lower-tail que no contiene literalmente.

### 5.2 El ensemble duro no es la medida canónica

La Definición 1.10 y la ecuación (1.14) de la misma fuente dan, para
\(\sigma=21\) y base uniforme,

\[
 Q_{n,\theta}(\pi)
 \propto \exp\!\left[n\theta\,t_{21}(\pi)\right]
 =\exp\!\left[
   \frac{n\theta}{\binom n2}\operatorname{Inv}(\pi)
 \right].
\tag{5.3}
\]

Ésta es una medida de Mallows con
\(q_n=\exp(2\theta/(n-1))\). En cambio,
\(\Pr(\cdot\mid A_n(\delta))\) es la medida uniforme sobre un lower tail duro.
Que ambas tengan el mismo permutón típico no es una equivalencia de ensembles a
escala subexponencial. Ningún paso de este preflight identifica esas dos leyes
para eventos microscópicos.

Sí puede comprobarse, como control, que prescribir \(R_n\) pares cuesta a lo
sumo \(\exp[-R_n\log n-O_\theta(R_n)]\) bajo (5.3). Se fuerza la prescripción
mediante a lo sumo \(R_n\) transposiciones de valores; cada una cambia como
máximo \(O(n)\) inversiones, el exponente de (5.3) cambia \(O_\theta(1)\), y
cada imagen tiene a lo sumo \(n^{R_n}\) preimágenes. Como
\(R_n\log n=o(n)\), el coste es subexponencial. Esta observación canónica no se
usa como sustituto de una prueba para el ensemble duro; la prueba directa viene
en la sección siguiente.

## 6. Intento de construcción subexponencial

### 6.1 La prescripción de EF-4 conserva la tasa del macroevento

Sea \(n\) par, \(R=R_n\), \(N=n-R\), y condiciónese solo por \(F_n\). Al
estandarizar las filas y columnas libres, la completación es una permutación
uniforme \(\tau\in\mathfrak S_N\). Toda inversión entre dos puntos libres es
exactamente una inversión de \(\tau\). Las demás inversiones involucran al
menos un punto prescrito, por lo que

\[
 \operatorname{Inv}(\tau)
 \le \operatorname{Inv}(\pi)
 \le \operatorname{Inv}(\tau)+D_n,
\tag{6.1}
\]

donde

\[
 D_n
 =\binom n2-\binom N2
 =Rn-\frac{R(R+1)}2
 =O(Rn)=o(n^2).
\tag{6.2}
\]

En consecuencia,

\[
 \Pr_N\!\left(
   \operatorname{Inv}(\tau)
   \le\delta\binom n2-D_n
 \right)
 \le \Pr(A_n(\delta)\mid F_n)
 \le
 \Pr_N\!\left(
   \operatorname{Inv}(\tau)
   \le\delta\binom n2
 \right).
\tag{6.3}
\]

Los dos umbrales de (6.3), normalizados por \(\binom N2\), convergen a
\(\delta\), porque \(R/n\to0\). El LDP lower-tail y la continuidad de
\(J\) implican, mediante un sandwich por \(\delta\pm\varepsilon\),

\[
 \log\Pr(A_n(\delta)\mid F_n)
 =-nJ(\delta)+o(n).
\tag{6.4}
\]

Combinar (5.2), (6.4) y

\[
 \Pr(F_n)=\frac1{(n)_{R_n}}
\tag{6.5}
\]

da por Bayes

\[
 \begin{aligned}
 -\log\Pr(F_n\mid A_n(\delta))
 &=\log (n)_{R_n}+o(n)\\
 &=O(R_n\log n)+o(n)\\
 &=o(n).
 \end{aligned}
\tag{6.6}
\]

Equivalentemente,

\[
 -\log\Pr(F_n\cap A_n(\delta))
 =-\log\Pr(A_n(\delta))+o(n).
\tag{6.7}
\]

Éste es un resultado positivo del preflight: plantar exactamente las dos
escaleras y la cuádrupla balanceada de EF-4 no altera el coste exponencial del
macroevento de inversiones.

El mismo sandwich, unido a la unicidad del minimizador de (5.1), muestra que las
completaciones condicionadas por \(F_n\cap A_n(\delta)\) conservan el
macroestado \(\nu_{\theta(\delta)}\). Los \(R_n=o(n)\) puntos prescritos
desaparecen en el permutón empírico. Así, \(F_n\) es compatible tanto en tasa
como en macroestado.

### 6.2 Qué no se ha construido

El evento \(F_n\) fuerza un candidato admisible y bilateralmente balanceado,
pero no fuerza `UNIQUE`. Los \(N_n\) puntos libres todavía pueden crear una
cuádrupla con score primario igual o mayor. Por tanto, (6.7) no es todavía una
cota inferior para \(S_n\cap A_n(\delta)\).

## 7. Control de rivales globales

### 7.1 El evento \(G_n\) uniforme es incompatible con el lower tail

EF-4 usa

\[
 G_n=\left\{
 |X(I,J)-Nuv|\le\eta_n
 \text{ para todos los intervalos residuales }I,J
 \right\},
 \qquad
 \eta_n=\sqrt{3N\log n}.
\tag{7.1}
\]

Si una sucesión de completaciones satisface \(F_n\cap G_n\), la discrepancia
rectangular de su permutación residual respecto del producto uniforme es a lo
sumo

\[
 \frac{\eta_n}{N}=O\!\left(\sqrt{\frac{\log n}{n}}\right)\longrightarrow0.
\tag{7.2}
\]

Luego el permutón residual converge a \(\lambda\), y por continuidad de las
densidades de patrones,

\[
 t_{21}(L_N(\tau))\longrightarrow\frac12.
\tag{7.3}
\]

Las inversiones que involucran puntos prescritos son como máximo \(D_n=o(n^2)\),
de modo que (7.3) implica también

\[
 t_{21}(L_n(\pi))\longrightarrow\frac12.
\tag{7.4}
\]

Por consiguiente, para cada \(\delta<1/2\) fijo,

\[
 F_n\cap G_n\cap A_n(\delta)=\varnothing
\tag{7.5}
\]

para todo \(n\) par suficientemente grande. No se trata de que la cota
\(1-2n^{-2}\) deje de estar demostrada bajo Mallows: el propio evento al que se
aplica centra las completaciones en el macroestado equivocado.

### 7.2 Sustituto que haría falta

Sea \(\mathcal Q\) el espacio macroscópico de pares ordenados de rectángulos
causales disjuntos, y defínase el score de población

\[
 \Phi_\theta(R_-,R_+)
 :=\left(
   \min\{\nu_\theta(R_-),\nu_\theta(R_+)\},
   \nu_\theta(R_-)+\nu_\theta(R_+)
 \right),
\tag{7.6}
\]

con orden lexicográfico. La relajación macroscópica de la plantada de EF-4 es

\[
 R_-^0=[0,1/2]^2,
 \qquad R_+^0=[1/2,1]^2.
\tag{7.7}
\]

Una adaptación Mallows del certificado necesita, como mínimo:

1. demostrar que (7.7) es el único maximizador relevante de (7.6), o identificar
   otro par plantable que lo sea;
2. obtener un módulo cuantitativo de separación frente a todos los rectángulos
   macroscópicamente alejados;
3. controlar uniformemente, bajo la ley dura condicionada, los conteos de todos
   los rectángulos a la escala mesoscópica en la que actúan las escaleras;
4. reanalizar los rivales microscópicamente próximos y probar que el margen
   prescrito domina sus fluctuaciones y posibles sesgos Mallows;
5. tratar los tamaños impares sin usar directamente la inyección (4.5).

El LDP de permutones solo resuelve desviaciones macroscópicas cerradas, de orden
\(n\). No proporciona por sí solo los puntos 2--4, ni decide empates exactos de
scores enteros. En particular, la convergencia a \(\nu_{\theta(\delta)}\) no
impide que una nube libre cree un rival global con el mismo mínimo y la misma
cobertura.

La obligación probabilístico-combinatoria exacta que queda abierta puede
escribirse así: construir \(H_{n,\delta}\) tal que

\[
 -\log\Pr(H_{n,\delta}\mid F_n,A_n(\delta))=o(n)
\tag{7.8}
\]

y

\[
 \max_{q\ne q_0}
 \bigl(
   \min\{M_-(q),M_+(q)\},
   M_-(q)+M_+(q)
 \bigr)
 <_{\rm lex}
 \bigl(
   M_-(q_0),
   2M_-(q_0)
 \bigr)
\tag{7.9}
\]

en \(F_n\cap A_n(\delta)\cap H_{n,\delta}\). La desigualdad (7.9) debe ser
simultánea sobre todas las cuádruplas admisibles; controlar solo el valor medio
de la plantada no basta.

## 8. Comparación de tasas

La separación obtenida es

\[
 \underbrace{-\log\Pr(F_n\cap A_n(\delta))}_{
   \text{macroevento + prescripción}}
 =
 \underbrace{-\log\Pr(A_n(\delta))}_{nJ(\delta)+o(n)}
 +o(n).
\tag{8.1}
\]

Ésta es exactamente la comparación de tasas solicitada para el testigo
prescrito, pero no para su unicidad. Para alcanzar el puente habría que añadir

\[
 -\log\Pr(S_n\mid F_n,A_n(\delta))=o(n),
\tag{8.2}
\]

o la versión suficiente (7.8)--(7.9). Entonces

\[
 \begin{aligned}
 -\log\Pr(S_n\cap A_n(\delta))
 &\le -\log\Pr(F_n\cap A_n(\delta))\\
 &\quad-\log\Pr(S_n\mid F_n,A_n(\delta))\\
 &=-\log\Pr(A_n(\delta))+o(n).
 \end{aligned}
\tag{8.3}
\]

La desigualdad elemental inversa da el otro lado, porque
\(S_n\cap A_n(\delta)\subseteq A_n(\delta)\). Así se obtendría (3.2).

No se ha demostrado (8.2), ni tampoco una tasa lineal positiva para su negación.
Por ello no procede `PASS_MALLOWS_SUBEXP_UNIQUENESS`, `PASS_RESTRICTED_DELTA` ni
`FAIL_EXPONENTIAL_UNIQUENESS_COST`.

## 9. Terminal

```text
PRESCRIBED_EF4_FAMILY_CONDITIONAL_COST = SUBEXPONENTIAL_PROVED
PRESCRIBED_EF4_FAMILY_MACROSTATE = MALLOWS_COMPATIBLE
EF4_UNIFORM_GOOD_COMPLETION_EVENT_UNDER_LOWER_TAIL = EVENTUALLY_EMPTY
EF4_ODD_TRANSFER_UNDER_LOWER_TAIL = NOT_PRESERVED_WITHOUT_BUFFER
MALLOWS_GLOBAL_RIVAL_CONTROL = OPEN
CONDITIONAL_UNIQUENESS_MASS = NOT_DECIDED

PREFLIGHT_TERMINAL = BLOCKED_BY_GLOBAL_RIVAL_CONTROL
EF8_STATUS = NOT_OPENED
```

El terminal significa que se ha superado el preflight entrópico de la
prescripción: imponer \(R_n=O(n^{2/3}(\log n)^{1/3})\) puntos no altera la tasa
del lower tail. El bloqueo empieza después, al intentar convertir el candidato
plantado en ganador único frente a todos los rectángulos creados por el bulk de
Mallows.

## 10. Consecuencias para una eventual apertura de EF-8

EF-8 no debe abrirse con el puente como teorema disponible. Antes hace falta una
pieza nueva, no contenida en EF-3/EF-4 ni en el LDP de permutones:

> un teorema de optimización y concentración uniforme de pares de rectángulos
> bajo el lower tail de inversiones, con resolución suficiente para decidir el
> argmax lexicográfico discreto después de plantar una subestructura
> subextensiva.

Una secuencia razonable de obligaciones deductivas sería:

1. resolver el problema variacional (7.6) para
   \(\nu_{\theta(\delta)}\) y determinar para qué \(\delta\) la plantada de
   EF-4, u otra plantada explícita, es el maximizador macroscópico;
2. si hay unicidad macroscópica, demostrar un módulo de estabilidad;
3. obtener una cota de discrepancia centrada en Mallows bajo el ensemble **duro**,
   no solo bajo la medida canónica;
4. cerrar los rivales locales y la paridad;
5. solo entonces combinar esa pieza con (6.6) para probar (1.3).

Si el paso 1 falla para algún rango de \(\delta\), eso produciría una obstrucción
geométrica concreta a la familia EF-4, pero todavía no demostraría que
`UNIQUE` tenga coste exponencial: podría existir otra familia prescrita. Si los
pasos 1--4 pasan en una subregión explícita, el resultado natural sería
`PASS_RESTRICTED_DELTA` y solo entonces habría base para reconsiderar la apertura
de EF-8.

## Referencias auditadas

- `dev/EF8_RATE_COMPETITION_PREFLIGHT.md`.
- `dev/EF8_PERMUTON_MACRO_EVENT_PREFLIGHT.md`.
- `emergencia/P1a_estabilidad_seleccion_subexponencial_d2.md`.
- `docs/hoja_de_ruta_agosto_2026.md`, EF-3 y EF-4.
- `emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md`.
- J. Borga, S. Das, S. Mukherjee y P. Winkler, *Large deviation principle for
  random permutations*, arXiv:2206.04660; Corollary 1.7, Definition 1.10,
  equation (1.14), Theorem 1.20, Remark 1.21 y Theorem 1.29(ii).
