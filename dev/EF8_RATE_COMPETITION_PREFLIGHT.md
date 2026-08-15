# EF-8 — preflight de competencia entre coste de selección y tasa de desviación

Continuación deductiva: `dev/EF8_PERMUTON_MACRO_EVENT_PREFLIGHT.md`.

```text
ESTADO: PREFLIGHT_DEDUCTIVO_Y_BIBLIOGRAFICO
FECHA: 2026-08-13
EF8_STATUS: NOT_OPENED
SIMULACION_ALEATORIA_NUEVA: NINGUNA
SONDEO_FINITO_AUXILIAR: ENUMERACION_EXHAUSTIVA_n<=8_NO_ASINTOTICA
EF5: NO ABIERTO
d>=3: NO ABIERTO
```

## 0. Veredicto

La comparación de tasas propuesta es correcta para cada desviación fija, pero no
implica en general que una selección de coste exponencial positivo preserve la
consistencia. Si

\[
 \Pr(A_{n,\varepsilon})\le
 \exp[-v_n I_\varepsilon+o(v_n)]
 \quad\text{y}\quad
 \Pr(S_n)\ge \exp[-v_n\alpha+o(v_n)],
\]

entonces

\[
 I_\varepsilon>\alpha
 \quad\Longrightarrow\quad
 \Pr(A_{n,\varepsilon}\mid S_n)\to0.
\]

Esto excluye desviaciones cuyo coste excede el presupuesto entrópico del selector.
Para deducir convergencia a cero hace falta, sin embargo,

\[
 I_\varepsilon>\alpha\qquad\text{para todo }\varepsilon>0.
\]

En los regímenes habituales \(I_\varepsilon\downarrow0\) cuando
\(\varepsilon\downarrow0\). Por tanto, un \(\alpha>0\) fijo deja en general un tubo
residual, no consistencia. El caso \(\alpha=0\) de EF-7 no es meramente el primer
punto de una familia de resultados de consistencia exponencial: es el umbral
genérico de consistencia del argumento que solo divide por \(\Pr(S_n)\).

La generalización deductiva que sí sobrevive es un principio cuantitativo de
**coste de selección frente a resolución**. Una segunda línea, genuinamente más
rica y abierta, consistiría en identificar la nueva ley típica bajo el selector raro
mediante un problema variacional de permutones.

## 1. Lema exacto de presupuesto de tasas

Sean \(v_n\to\infty\), eventos \(S_n\) de probabilidad positiva y eventos de
desviación \(A_{n,\varepsilon}\). Supóngase que

\[
 \limsup_{n\to\infty}\frac1{v_n}
 \log\Pr(A_{n,\varepsilon})\le-I_\varepsilon
\tag{1.1}
\]

y

\[
 \limsup_{n\to\infty}\frac1{v_n}
 \log\frac1{\Pr(S_n)}\le\alpha.
\tag{1.2}
\]

Entonces

\[
 \limsup_{n\to\infty}\frac1{v_n}
 \log\Pr(A_{n,\varepsilon}\mid S_n)
 \le -(I_\varepsilon-\alpha).
\tag{1.3}
\]

La demostración es la misma división elemental usada en EF-7:

\[
 \Pr(A_{n,\varepsilon}\mid S_n)
 \le \frac{\Pr(A_{n,\varepsilon})}{\Pr(S_n)}.
\]

No hay hipótesis de independencia. La desigualdad estricta
\(I_\varepsilon>\alpha\) da decaimiento exponencial. La igualdad no da una
conclusión y \(I_\varepsilon<\alpha\) solo vuelve trivial esta cota; no demuestra
por sí solo que la desviación ocurra después de seleccionar.

### 1.1 Consecuencia de tubo

Si \(D_n\in[0,B]\), \(A_{n,\varepsilon}=\{D_n>\varepsilon\}\) y
\(I_\varepsilon\) es no decreciente, defínase

\[
 \varepsilon_\alpha
 :=\inf\{\varepsilon>0:I_\varepsilon>\alpha\}.
\tag{1.4}
\]

Para todo
\(\varepsilon>\varepsilon_\alpha\) en el que la desigualdad de tasas sea
estricta,

\[
 \Pr(D_n>\varepsilon\mid S_n)\to0.
\]

Si esto vale para toda
\(\varepsilon>\varepsilon_\alpha\), la descomposición

\[
 E[D_n\mid S_n]
 \le \varepsilon+B\Pr(D_n>\varepsilon\mid S_n)
\]

da

\[
 \limsup_n E[D_n\mid S_n]\le\varepsilon_\alpha.
\tag{1.5}
\]

Esta es una garantía de resolución, no de convergencia a cero salvo que
\(\varepsilon_\alpha=0\).

### 1.2 Contraejemplo que impide la lectura fuerte

Sea \(X_n\sim N(0,1/n)\), \(D_n=|X_n|\) y
\(S_n=\{X_n\ge a\}\), con \(a>0\). Para una desviación fija,
\(I_\varepsilon=\varepsilon^2/2\), mientras que el selector tiene coste
\(\alpha=a^2/2\). Por tanto, \(I_\varepsilon>\alpha\) para
\(\varepsilon>a\), pero bajo \(S_n\) se tiene deterministamente \(D_n\ge a\).
La variable no converge a cero. El cociente de tasas localiza correctamente el
suelo \(a\).

## 2. Forma no asintótica y resolución variable

La formulación más útil conserva el coste finito

\[
 b_n:=\log\frac1{\Pr(S_n)}.
\]

Si para \(t>0\)

\[
 \Pr(D_n>t)\le a_n(t)\exp[-v_n\Phi(t)],
\]

entonces

\[
 \Pr(D_n>t\mid S_n)
 \le a_n(t)\exp[-v_n\Phi(t)+b_n].
\tag{2.1}
\]

Así, cualquier sucesión \(t_n\) que satisfaga

\[
 v_n\Phi(t_n)-b_n-\log a_n(t_n)\longrightarrow+\infty
\tag{2.2}
\]

es una escala de resolución condicionada. Para una cola subgaussiana
\(\Phi(t)=ct^2\), la escala genérica es

\[
 t_n\gg\sqrt{\frac{b_n+\log a_n(t_n)}{cv_n}}.
\tag{2.3}
\]

EF-7 corresponde a \(b_n=o(v_n)\), que permite escoger \(t_n\to0\). Si
\(b_n\sim\alpha v_n\), (2.3) deja un radio constante de orden
\(\sqrt{\alpha/c}\).

## 3. Aplicación inmediata a la discrepancia de EF-7

EF-7 ya prueba

\[
 \Pr(\Delta_n>t)\le2n^4e^{-2nt^2}.
\tag{3.1}
\]

Por tanto, para cualquier selector rectangular con coste finito \(b_n\),

\[
 \Pr(\Delta_n>t\mid S_n)
 \le2n^4\exp[-2nt^2+b_n].
\tag{3.2}
\]

Una escala suficiente es

\[
 t_n=
 \sqrt{\frac{b_n+4\log n+c_n}{2n}},
 \qquad c_n\to\infty.
\tag{3.3}
\]

Como

\[
 \left(Z_n-\sqrt{M_n/n}\right)^2
 \le \Delta_n+4/n,
\tag{3.4}
\]

la misma escala controla el error cuadrático de proyección en probabilidad. Si se
escoge además `c_n` de modo que `exp(-c_n)=o(t_n)`, la acotación de `Delta_n`
transfiere ese orden también a su esperanza y al MSE. Los términos que separan
\(\sqrt{M_n/n}\), `COUNT_VOLUME` y la duración continua son \(o(1)\) en MSE y no
cambian el suelo asintótico.

En particular, si

\[
 b_n\le\alpha n+o(n),
\]

entonces, para todo \(t>\sqrt{\alpha/2}\),

\[
 \Pr(\Delta_n>t\mid S_n)\to0,
\]

y la prueba de EF-7 solo entrega

\[
 \limsup_n
 E\!\left[
   \left(Z_n-\sqrt{M_n/n}\right)^2
   \mid S_n
 \right]
 \le \min\{1,\sqrt{\alpha/2}\}.
\tag{3.5}
\]

No entrega cero para
\(\alpha>0\).

Para `MIN_COVERAGE_LEX`, el certificado prescrito de EF-4/EF-7 da crudamente

\[
 b_n=O\!\left(n^{2/3}(\log n)^{4/3}\right),
\]

de modo que (3.3) produce la cota no optimizada

\[
 \Delta_n
 =O_{\Pr(\cdot\mid S_n)}
 \!\left(n^{-1/6}(\log n)^{2/3}\right)
\tag{3.6}
\]

con una constante suficientemente grande. Esta tasa hereda la extrema holgura del
certificado combinatorio de masa y no debe interpretarse como tasa real del
selector.

## 4. Qué pueden aportar los permutones

Borga, Das, Mukherjee y Winkler prueban un LDP de velocidad \(n\) para
permutaciones inducidas por una medida del cuadrado y desarrollan leyes
condicionadas por densidades atípicas de patrones. Para la permutación uniforme, su
Corolario 1.7 recupera un LDP anterior cuya tasa es la entropía relativa

\[
 \mathcal I(\nu)=D(\nu\Vert\lambda)
\]

sobre permutones; el propio artículo atribuye el caso uniforme a Trashorras,
Mukherjee y Kenyon--Král'--Radin--Winkler. Por tanto, la referencia no debe
presentarse como origen del LDP uniforme, aunque sí es una entrada moderna muy
útil a su maquinaria condicionada.

Para la discrepancia rectangular límite

\[
 \delta(\nu)=\sup_R|\nu(R)-\lambda(R)|,
\]

el candidato variacional sería

\[
 J(t)=\inf\{D(\nu\Vert\lambda):\delta(\nu)\ge t\}.
\tag{4.1}
\]

Si se verifican con cuidado la topología del evento y la contracción, el criterio
de tasas se afinaría a \(J(t)>\alpha\). Pinsker ya da

\[
 J(t)\ge2t^2,
\]

porque la discrepancia rectangular no excede la variación total. Esto reproduce,
a nivel exponencial, la tasa elemental \(2t^2\) de (3.1). Calcular \(J\) exactamente
podría mejorar constantes o describir el permutón desviacional típico, pero no
elimina el suelo genérico: perturbaciones arbitrariamente pequeñas de
\(\lambda\) tienen entropía arbitrariamente pequeña, de modo que \(J(t)\to0\)
cuando \(t\downarrow0\).

La aplicación directa al observable adaptativamente seleccionado tiene dos
obligaciones adicionales:

1. demostrar que el evento del selector y el observable normalizado son cerrados,
   abiertos o exponencialmente aproximables en la topología de permutones;
2. controlar la discontinuidad del argmax y de la unicidad. La unicidad exacta de
   un máximo discreto puede depender de información microscópica que un permutón
   límite no conserva.

La versión matemáticamente más rica de EF-8 no sería entonces «todo selector con
\(\alpha<I_\varepsilon\) sigue siendo consistente», sino:

> Para una clase macroscópica bien definida de eventos de selección, identificar
> los minimizadores entrópicos del evento y la ley límite del observable bajo esos
> minimizadores.

Eso permitiría distinguir entre selección rara que solo reduce resolución y
selección rara que desplaza el centro condicionado.

## 5. Auditoría de las otras rutas bibliográficas

### 5.1 Götze--Sambale--Sinulis

El artículo establece una desigualdad log-Sobolev para la permutación uniforme con
un operador construido a partir de transposiciones, y su teorema general exige
controles de diferencias discretas de varios órdenes. Por tanto, la prueba crítica
es correcta: hay que acotar

\[
 |f(\pi)-f(\tau_{ij}\pi)|
\]

y los tensores de diferencias iteradas para la función concreta que se quiera
concentrar.

Para `MIN_COVERAGE_LEX` hay dos problemas previos:

- el observable seleccionado ni siquiera está definido fuera del evento de
  unicidad, por lo que hace falta fijar una extensión total antes de aplicar una
  desigualdad funcional;
- una transposición puede cambiar el estado `UNIQUE/TIE` o el ganador global. Un
  sondeo exhaustivo auxiliar con la implementación congelada encontró 15 de 15
  transposiciones `UNIQUE -> no UNIQUE` desde la única permutación exitosa de
  tamaño 6; para \(n=8\), 14 370 de 18 956 transposiciones dirigidas desde estados
  únicos cambiaron a un estado no único. También aparecen saltos entre ganadores
  únicos. Esto solo demuestra discontinuidad finita, no una obstrucción
  asintótica.

En contraste,
\(\Delta_n\) sí cambia a escala \(O(1/n)\) bajo una transposición,
pero para ella EF-7 ya dispone de (3.1), que es directa y evita pagar el factor
logarítmico de la constante log-Sobolev citada en ese artículo. La vía de
transposiciones solo merece prioridad si se identifica un funcional más informativo
que
\(\Delta_n\) con diferencias verificablemente pequeñas.

### 5.2 Dodos--Tyros--Valettas

El array de relaciones de un sprinkling etiquetado puede escribirse como función de
pares de coordenadas iid y encaja naturalmente en la noción de array disociado. Sin
embargo, sus teoremas controlan la esperanza condicional de una función global al
revelar el subarray sobre un conjunto de índices determinista apropiado. No
condicionan por un evento global adaptativo arbitrario, ni por el resultado de un
argmax. Además, el conjunto de índices que produce el teorema vive en el orden de
las etiquetas, no define por sí mismo una selección intrínseca del poset.

La referencia es útil para formular una comparación negativa precisa, pero no
parece maquinaria directa para EF-7/EF-8 sin un nuevo teorema de estabilidad bajo
subarrays elegidos adaptativamente.

### 5.3 Zou--Xu--Ding--Han

El preprint de 2026 estudia estadísticas de la forma

\[
 \sum_{i,j}w(i,j,\pi(i),\pi(j))
\]

con un tensor fijo y obtiene desigualdades combinatorias de Hanson--Wright y
Bennett. `MIN_COVERAGE_LEX` es un máximo adaptativo sobre candidatos y su salida no
es, de forma inmediata, una estadística doblemente indexada con tensor fijo. La
referencia pasa a prioridad alta solo si se encuentra una representación fija del
score, del margen entre primer y segundo ganador o de un surrogate que controle el
argmax.

### 5.4 Bollobás--Brightwell y LIS

La referencia de 1992 es correcta y directamente relevante para la genealogía
2-order/permutación: identifica la altura en dimensión 2 con la LIS y obtiene
concentración para la altura de órdenes aleatorios (k)-dimensionales. Su
observable y escala de fluctuación son distintos de la discrepancia rectangular y
del rectángulo seleccionado. Es una fuente metodológica, no un antecedente del
principio de condicionamiento de EF-7.

### 5.5 Fewster--Hawkins--Minz--Rejzner e inferencia selectiva

Fewster et al. sí proporcionan el precedente causal directo para la correspondencia
entre sprinklings (1+1) y 2D-orders y para criterios que buscan una selección única.
No contienen el cociente de tasas de EF-7.

Fithian--Sun--Taylor y Tian--Taylor son contexto correcto para insistir en que la
selección y el estadístico no han de ser independientes. Sus resultados persiguen
validez inferencial, pivotes y CLT selectivos bajo estructuras estadísticas
específicas, incluidas versiones aleatorizadas; no sustituyen el certificado de
masa ni la discrepancia uniforme de EF-7.

## 6. Gate propuesto antes de abrir EF-8

```text
EF8_RATE_BUDGET_LEMMA = PROVED_ELEMENTARY_PREFLIGHT
EF8_FIXED_EPSILON_THRESHOLD = VALID
EF8_POSITIVE_ALPHA_PRESERVES_ZERO_CONSISTENCY = FALSE_IN_GENERAL
EF8_POSITIVE_ALPHA_OUTPUT = RESOLUTION_TUBE_OR_SHIFTED_CONDITIONAL_LIMIT
EF8_PERMUTON_DISCREPANCY_VARIATIONAL_RATE = OPEN_TOPOLOGY_AND_OPTIMIZATION
EF8_MIN_COVERAGE_LEX_PERMUTON_EVENT = OPEN_MICROSCOPIC_UNIQUENESS_OBSTRUCTION
EF8_TRANSPOSITION_ROUTE = OPEN_LOW_PRIORITY_WITHOUT_DERIVATIVE_BOUND
EF8_DIPS_ROUTE = OPEN_ONLY_AFTER_FIXED_TENSOR_REPRESENTATION
EF8_STATUS = NOT_OPENED
```

Orden recomendado si se autoriza la línea:

1. promover (2.1)--(3.3) como refinamiento cuantitativo, sin claim de novedad;
2. formalizar y auditar la contracción que conduce a \(J(t)\) en (4.1);
3. decidir si se quiere el rate function del error uniforme
   \(\Delta_n\), que es estable, o la ley post-selección de
   `MIN_COVERAGE_LEX`, que exige resolver el argmax microscópico;
4. solo después intentar una optimización de entropía o una representación por
   diferencias/transposiciones.

No se recomienda abrir todavía \(d\ge3\).

## Referencias primarias inspeccionadas

- J. Borga, S. Das, S. Mukherjee y P. Winkler,
  [*Large deviation principle for random permutations*](https://arxiv.org/abs/2206.04660),
  especialmente Cor. 1.7, Thm. 1.20 y App. A.
- R. Kenyon, D. Král', C. Radin y P. Winkler,
  *Permutations with fixed pattern densities*, Random Structures & Algorithms
  56 (2020), 220--250.
- F. Götze, H. Sambale y A. Sinulis,
  [*Higher order concentration for functions of weakly dependent random variables*](https://arxiv.org/abs/1801.06348),
  Thm. 1.5 y §3.2.
- P. Dodos, K. Tyros y P. Valettas,
  [*Concentration estimates for functions of finite high-dimensional random arrays*](https://arxiv.org/abs/2102.10686),
  Thm. 2.2 y Thm. 6.1.
- M. Zou, J. Xu, P. Ding y F. Han,
  [*Decoupling and randomization for double-indexed permutation statistics*](https://arxiv.org/abs/2601.20018),
  Thm. 1.1 y Thm. 1.2.
- B. Bollobás y G. Brightwell, *The height of a random partial order:
  concentration of measure*, Annals of Applied Probability 2 (1992),
  1009--1018.
- C. J. Fewster, E. Hawkins, C. Minz y K. Rejzner,
  [*Local structure of sprinkled causal sets*](https://arxiv.org/abs/2011.02965).
- W. Fithian, D. Sun y J. Taylor,
  [*Optimal inference after model selection*](https://arxiv.org/abs/1410.2597).
- X. Tian y J. Taylor,
  [*Selective inference with a randomized response*](https://arxiv.org/abs/1507.06739).

## Trazabilidad interna

- `emergencia/P1a_estabilidad_seleccion_subexponencial_d2.md`, §§2--6.
- `emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md`, §§1--2.
- `emergencia/p1a_comparar_selectores_d2.py`, función `evaluate_selectors`.
- `dev/ef8_selector_transposition_probe.py`, ejecutado con
  `.venv/bin/python -m dev.ef8_selector_transposition_probe`: enumera todas las
  permutaciones de \(n=6,7,8\) y todas sus transposiciones, y evalúa
  `MIN_COVERAGE_LEX` con esa función. No se usa como evidencia asintótica ni
  modifica artefactos congelados.
