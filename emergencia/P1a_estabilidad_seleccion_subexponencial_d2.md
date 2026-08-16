# P1a — Estabilidad de la concentración bajo selección subexponencial

```text
ESTADO: COMPLETE_DEDUCTIVE_GENERALIZATION
FECHA: 2026-08-12
TERMINAL: SELECTOR_CLASS_THEOREM
MODELO DE LA APLICACIÓN: fixed-n, d=2
EJECUCIÓN NUMÉRICA: NINGUNA
CÓDIGO NUEVO: NINGUNO
EF-5: NO ABIERTO
d>=3: NO ABIERTO
```

## Resumen técnico

La prueba de EF-4 no es esencialmente una prueba exclusiva de
`MIN_COVERAGE_LEX`. Se descompone en tres capas rigurosas:

1. un lema probabilístico, independiente del modelo y del selector: una
   concentración con velocidad exponencial se conserva al condicionar por un evento
   cuyo coste logarítmico es subexponencial a esa velocidad;
2. un teorema de clase en el modelo `fixed-n`, `d=2`: cualquier selector adaptativo
   que entregue intervalos causales y cuyo evento de éxito satisfaga
   `-log Pr(S_n)=o(n)` tiene concentración de fibras para
   `Z_n=sqrt(KL)/(n+1)`; si además el selector es `order-only`, el estimador
   `COUNT_VOLUME` tiene MSE absoluto tendente a cero para la duración lateral
   relativa;
3. un certificado de pertenencia: la familia prescrita, el margen frente a rivales
   y la transferencia par–impar de EF-4 prueban que `MIN_COVERAGE_LEX` pertenece a
   esa clase.

Por tanto, el terminal más fuerte de esta nota es

```text
SELECTOR_CLASS_THEOREM
```

El lema `ABSTRACT_SELECTION_THEOREM` queda demostrado como pieza intermedia. Se
descarta `ESSENTIALLY_MIN_COVERAGE_LEX_SPECIFIC`: lo específico del selector es el
certificado de masa de su evento de éxito, no el mecanismo que convierte esa masa
en consistencia.

La generalización tiene un límite preciso. Ser intrínseco, equivariante o único no
implica por sí solo `-log Pr(S_n)=o(n)`. Esa propiedad necesita una hipótesis de masa
o un certificado combinatorio separado.

## 1. Experimento y clase de selectores

Sean `(U_i,V_i)`, `i=1,...,n`, iid uniformes en `[0,1]^2`, condicionado el canal a
`N=n`. Al ordenar por la primera coordenada, los rangos de la segunda forman una
permutación uniforme `Pi_n` de `{1,...,n}`.

Un **selector rectangular adaptativo** `A_n` es una regla, posiblemente parcial,
que en un evento de éxito `S_n` devuelve uno o varios pares comparables de puntos.
Para uno de los lados devueltos, con extremos `x prec y`, se definen

\[
K_n=\operatorname{rank}_u(y)-\operatorname{rank}_u(x),\qquad
L_n=\operatorname{rank}_v(y)-\operatorname{rank}_v(x),
\]

\[
M_n=|I[x,y]|,\qquad
Z_n=\frac{\sqrt{K_nL_n}}{n+1}.
\tag{1.1}
\]

La regla puede examinar toda la realización antes de elegir el rectángulo. No se
exige que sus endpoints sean deterministas, que maximice un score concreto ni que
el lado seleccionado tenga una posición prefijada.

Se distinguen dos clases:

- `SUBEXPONENTIAL_RANK_RECTANGLE`: el selector devuelve el rectángulo sobre `S_n`,
  `p_n=Pr(S_n)>0` y `log(1/p_n)=o(n)`;
- `SUBEXPONENTIAL_ORDER_ONLY`: además, el evento y los endpoints elegidos son
  medibles respecto de `Pi_n` y, si existe, de aleatoriedad auxiliar independiente
  de las magnitudes ordenadas.

La segunda clase contiene, en particular, cualquier selector intrínseco del poset
que satisfaga la condición de masa. La primera es más amplia: para concentrar
`Z_n` ni siquiera hace falta que la regla ignore las magnitudes continuas.

## 2. Teorema abstracto de condicionamiento

### Teorema 2.1 — selección subexponencial preserva concentración exponencial

Sean espacios de probabilidad `(Omega_n,F_n,P_n)`, eventos `S_n` con
`p_n=P_n(S_n)>0`, una velocidad `v_n -> infinity` y variables
`0<=D_n<=B`, donde `B<infinity` no depende de `n`. Supóngase que, para cada
`epsilon>0`, existen `c_epsilon>0` y `a_n(epsilon)` tales que

\[
P_n(D_n>\varepsilon)
\le a_n(\varepsilon)e^{-c_\varepsilon v_n},
\qquad
\log a_n(\varepsilon)=o(v_n).
\tag{2.1}
\]

Si

\[
\log\frac1{p_n}=o(v_n),
\tag{2.2}
\]

entonces

\[
D_n\longrightarrow0
\quad\text{en probabilidad bajo }P_n(\,\cdot\mid S_n),
\tag{2.3}
\]

y

\[
E_n[D_n\mid S_n]\longrightarrow0.
\tag{2.4}
\]

No se supone independencia entre `D_n` y `S_n`.

De hecho, (2.1)–(2.2) conservan la velocidad exponencial:

\[
\limsup_{n\to\infty}\frac1{v_n}
\log P_n(D_n>\varepsilon\mid S_n)
\le -c_\varepsilon.
\]

**Demostración.** Para cada `epsilon>0`,

\[
P_n(D_n>\varepsilon\mid S_n)
\le \frac{P_n(D_n>\varepsilon)}{p_n}
\le a_n(\varepsilon)
   \exp\!\left[-c_\varepsilon v_n+\log(1/p_n)\right]
\longrightarrow0.
\tag{2.5}
\]

Además,

\[
E_n[D_n\mid S_n]
\le \varepsilon+B\,P_n(D_n>\varepsilon\mid S_n).
\tag{2.6}
\]

Tomando primero `n -> infinity` y después `epsilon downarrow 0` se obtiene
(2.4). `QED`

Este teorema es un cambio de medida elemental, no una reivindicación de novedad. Su
contenido útil aquí es explicitar la escala correcta: una penalización
`exp[o(v_n)]` no puede cancelar una cola `exp[-c v_n+o(v_n)]`.

### Observación 2.2 — la escala no puede eliminarse en general

La condición subexponencial es suficiente, no necesaria para cada problema
particular. Sin alguna comparación de escalas, sin embargo, el enunciado abstracto
es falso. Si `D_n` vale uno con probabilidad `e^{-cn}` y cero en otro caso, y se
condiciona en `S_n={D_n=1}`, entonces `D_n` tiene concentración exponencial
incondicionada pero

\[
E[D_n\mid S_n]=1,
\qquad -\log P(S_n)=cn.
\]

Un evento de selección exponencialmente raro puede seleccionar precisamente la
cola que se intentaba descartar.

## 3. La discrepancia uniforme elimina la adaptatividad del selector en `d=2`

Para intervalos deterministas de rangos
\(I,J\subseteq\{1,\ldots,n\}\), sea

\[
N_{\Pi_n}(I,J)=\#\{i\in I:\Pi_n(i)\in J\},
\]

\[
\Delta_n=
\max_{I,J}\left|
\frac{N_{\Pi_n}(I,J)}n-
\frac{|I||J|}{n^2}
\right|.
\tag{3.1}
\]

La cota hipergeométrica y la unión sobre menos de `n^4` pares de intervalos,
rederivadas en EF-3, dan para todo `epsilon>0`

\[
P(\Delta_n>\varepsilon)
\le 2n^4e^{-2n\varepsilon^2}.
\tag{3.2}
\]

La unión de (3.2) se toma antes de seleccionar endpoints. Por eso vale
simultáneamente para el rectángulo que cualquier regla adaptativa termine eligiendo.
Si el rectángulo seleccionado tiene gaps `(K_n,L_n)` y contiene `M_n` puntos,
entonces deterministamente

\[
\left|Z_n^2-\frac{M_n}{n}\right|
\le \Delta_n+\frac4n.
\tag{3.3}
\]

Ni (3.2) ni (3.3) contienen `MIN_COVERAGE_LEX`, su score, una política de empate o
una hipótesis de independencia entre selección y discrepancia.

## 4. Teorema de clase para fibras de rectángulos seleccionados

### Teorema 4.1 — `SELECTOR_CLASS_THEOREM`

Sea `A_n` cualquier selector de la clase `SUBEXPONENTIAL_RANK_RECTANGLE` y
considérese uno de sus lados de salida. Bajo la ley condicionada por `S_n`, defínase

\[
Q_{2,n}^{A}
=E\!\left[
\operatorname{Var}(Z_n\mid M_n,S_n)
\mid S_n
\right].
\tag{4.1}
\]

Entonces

\[
\boxed{Q_{2,n}^{A}\longrightarrow0.}
\tag{4.2}
\]

Más aún, con `g_n(m)=sqrt(m/n)`, para cada `epsilon>0`,

\[
\begin{aligned}
Q_{2,n}^{A}
&\le E[(Z_n-g_n(M_n))^2\mid S_n]\\
&\le \varepsilon+\frac4n
+\frac{2n^4e^{-2n\varepsilon^2}}{p_n}.
\end{aligned}
\tag{4.3}

Por tanto, el estimador congelado

\[
\widehat\ell_{\rm CV}(M_n,n)
=\sqrt{\frac{M_n-2}{n-2}}
\tag{4.4}
\]

satisface

\[
E[(Z_n-\widehat\ell_{\rm CV})^2\mid S_n]\longrightarrow0.
\tag{4.5}

**Demostración.** La esperanza condicionada de `Z_n` dado `M_n` minimiza el error
cuadrático entre las funciones de `M_n`, lo que da la primera desigualdad de
(4.3). Como `(sqrt(x)-sqrt(y))^2<=|x-y|`, (3.3) implica

\[
(Z_n-g_n(M_n))^2\le\Delta_n+\frac4n.
\]

Además, `0<=Delta_n<=1`, de modo que (3.2), dividida por `p_n` solo después de
aplicar la cota incondicionada, produce (4.3). La hipótesis
`log(1/p_n)=o(n)` hace que su último término tienda a cero para cada `epsilon`
fijo; después se toma `epsilon downarrow 0`.

Finalmente,

\[
\left(
\sqrt{\frac{M_n}{n}}-
\sqrt{\frac{M_n-2}{n-2}}
\right)^2
\le
\left|
\frac{M_n}{n}-\frac{M_n-2}{n-2}
\right|
\le\frac2{n-2}.
\tag{4.6}
\]

La desigualdad triangular en `L^2`, (4.3) y (4.6) prueban (4.5). `QED`

### Corolario 4.2 — un selector total no paga coste de selección

Si una regla siempre devuelve un intervalo mediante una política medible de
desempate, entonces `S_n=Omega_n` y `p_n=1`. Siempre que esa modificación del
protocolo esté permitida, (4.2)–(4.5) son inmediatas. Esto no autoriza a cambiar la
política congelada de abstención de `MIN_COVERAGE_LEX`; solo muestra que el coste
entrópico pertenece al evento de selección, no a la adaptatividad del rectángulo.

## 5. De los rangos a la duración continua: aquí entra `order-only`

El teorema 4.1 concentra el objeto discreto `Z_n` y no necesita independencia entre
el selector y las magnitudes continuas. Para concluir sobre

\[
\ell_n=\sqrt{(U_y-U_x)(V_y-V_x)},
\tag{5.1}
\]

sí hace falta que la selección sea `order-only`.

### Teorema 5.1 — consistencia absoluta de `COUNT_VOLUME` para la clase `order-only`

Si `A_n` pertenece a `SUBEXPONENTIAL_ORDER_ONLY`, entonces

\[
\boxed{
E[(\ell_n-\widehat\ell_{\rm CV}(M_n,n))^2\mid S_n]
\longrightarrow0.
}
\tag{5.2}

También se anulan el riesgo de Bayes condicionado por `M_n` y su término de
dispersión entre formas. Con
\(\mu_n(t)=E[\ell_n\mid T_n=t,S_n]\), este último es

\[
P_{2,n}^{A}
:=E\!\left[
\operatorname{Var}(\mu_n(T_n)\mid M_n,S_n)
\mid S_n
\right].
\]

\[
E[\operatorname{Var}(\ell_n\mid M_n,S_n)\mid S_n]\to0,
\qquad P_{2,n}^{A}\to0.
\tag{5.3}

**Demostración.** La permutación de rangos es independiente de los dos vectores de
estadísticos de orden. Al ser el selector y `S_n` medibles respecto de los rangos,
condicionar por ellos no altera las leyes de los gaps. Dado
`T_n=(K_n,L_n)`, los dos gaps continuos tienen las leyes Beta correspondientes y
son independientes entre coordenadas. Los controles uniformes ya probados dan

\[
E[\operatorname{Var}(\ell_n\mid T_n,S_n)\mid S_n]\le\frac1n,
\tag{5.4}
\]

y

\[
0\le Z_n-\mu_n(T_n)\le\frac1{2\sqrt n}.
\tag{5.5}
\]

Por la varianza total,

\[
E[(\ell_n-Z_n)^2\mid S_n]
\le\frac1n+\frac1{4n}.
\tag{5.6}

Combinar (5.6) con (4.5) prueba (5.2). Además, la proyección condicionada sobre
`sigma(M_n)` y (5.5) dan

\[
|\sqrt{P_{2,n}^{A}}-\sqrt{Q_{2,n}^{A}}|
\le\frac1{2\sqrt n},
\tag{5.7}

por lo que (4.2) implica (5.3). `QED`

La conclusión (5.2) es exactamente de MSE absoluto para el estimando lateral
relativo declarado. No es una conclusión sobre escala absoluta ni sobre un error
normalizado por la varianza total.

## 6. Certificados generales de pertenencia a la clase

El teorema 4.1 usa `log(1/p_n)=o(n)` como hipótesis. Para evitar que esta condición
sea solo una reformulación del objetivo, se separan dos mecanismos generales para
certificarla.

### Lema 6.1 — certificado por permutación parcial prescrita

Sea `F_n` el evento de que una permutación uniforme contiene `r_n` asignaciones
fila–columna prescritas, con filas y columnas todas distintas. Entonces

\[
P(F_n)=\frac1{(n)_{r_n}}.
\tag{6.1}
\]

Supóngase que existe un evento de buenas completaciones `G_n` tal que

\[
F_n\cap G_n\subseteq S_n,
\qquad
-\log P(G_n\mid F_n)=o(n),
\tag{6.2}
\]

y que

\[
r_n\log n=o(n).
\tag{6.3}
\]

Entonces

\[
-\log P(S_n)=o(n).
\tag{6.4}
\]

**Demostración.** De (6.1)–(6.2),

\[
P(S_n)\ge\frac{P(G_n\mid F_n)}{(n)_{r_n}},
\]

y por tanto

\[
\log\frac1{P(S_n)}
\le r_n\log n+\log\frac1{P(G_n\mid F_n)}=o(n).
\quad QED
\]

El lema no exige escaleras, balance bilateral ni un score lexicográfico. Es un
criterio de pertenencia para cualquier selector cuyo éxito pueda forzarse con una
cantidad sublineal, en la escala (6.3), de información prescrita.

### Lema 6.2 — transferencia entre tamaños con coste subexponencial

Sea \(\mathcal S_n\subseteq\mathfrak S_n\) el conjunto de permutaciones donde el
selector tiene éxito, y sea
\(p_n=|\mathcal S_n|/n!\). Si existe una inyección

\[
\iota_n:\mathcal S_{m_n}\hookrightarrow\mathcal S_n,
\tag{6.5}
\]

entonces

\[
p_n\ge p_{m_n}\frac{m_n!}{n!}.
\tag{6.6}
\]

En consecuencia, una cota subexponencial en los tamaños `m_n` se transfiere a `n`
si

\[
\log\frac{n!}{m_n!}=o(n).
\tag{6.7}
\]

Para `m_n=n-1`, el coste adicional es solo `log n`.

## 7. Qué parte de EF-4 es general y qué parte es específica

| Pieza lógica | Nivel de generalidad | Dependencia real |
|---|---|---|
| Dividir una cola por `Pr(S_n)` | Abstracto | Ninguna dependencia del selector ni del modelo |
| Discrepancia uniforme antes de elegir endpoints | Clase `fixed-n`, `d=2` | Rectángulos de rangos de una permutación uniforme |
| Cota de proyección que define `Q_{2,n}` | Clase de selectores | Solo que `M_n` sea la observación y el lado elegido sea un rectángulo causal |
| Ley Beta de gaps y control de `P_{1,n}` | Clase `order-only`, `d=2` | Selección medible en rangos e independencia rango–magnitud |
| Lema de permutación parcial | Certificado de pertenencia | Una familia prescrita de tamaño `r_n` y buenas completaciones |
| Principio de transferencia inyectiva | Certificado de pertenencia | Una inyección que preserve el éxito con coste factorial subexponencial |
| Dos escaleras de anchura `rho_n` | Aplicación `MIN_COVERAGE_LEX` | Construcción concreta de EF-4 |
| Balance exacto de la cuádrupla plantada | Aplicación `MIN_COVERAGE_LEX` | Geometría de las dos mitades prescritas |
| Tricotomía de rivales y margen `rho_n/2-o(rho_n)` | Aplicación `MIN_COVERAGE_LEX` | Score bilateral y orden lexicográfico congelados |
| Añadir `(n,1)` para pasar de par a impar | Aplicación `MIN_COVERAGE_LEX` | Preservación concreta de candidatos, scores y ganador único |

En EF-4,

\[
r_n=2\rho_n+2
=\Theta\!\left(n^{2/3}(\log n)^{1/3}\right),
\]

de modo que

\[
r_n\log n
=\Theta\!\left(n^{2/3}(\log n)^{4/3}\right)
=o(n).
\]

El evento uniforme de buenas completaciones tiene probabilidad condicionada
`1-O(n^{-2})`. La tricotomía y los márgenes demuestran
\(F_n\cap G_n\subseteq S_n\), por lo que el lema 6.1 certifica los tamaños
pares. La inyección que añade el punto incomparable `(n,1)` es el caso
`m_n=n-1` del lema 6.2 y completa la sucesión.

Así, `MIN_COVERAGE_LEX` es una aplicación no trivial del teorema de clase. Su
aportación específica consiste en demostrar pertenencia, no en crear el principio
de estabilidad bajo selección.

## 8. Por qué “selector intrínseco” no basta

Considérese la regla parcial que solo actúa cuando el poset es una cadena total y,
en ese caso, elige endpoints por sus posiciones únicas en la cadena. La regla es
intrínseca, equivariante y produce una salida única.

En la representación por permutaciones de un 2-order, el poset es una cadena total
si y solo si `Pi_n` es la permutación creciente. Por tanto

\[
P(S_n)=\frac1{n!},
\qquad
-\log P(S_n)=\log(n!)
=n\log n-n+O(\log n),
\tag{8.1}
\]

que no es `o(n)`.

Este ejemplo demuestra que ninguna combinación de las etiquetas
“intrínseco”, “order-only”, “equivariante” y “salida única” garantiza por sí sola la
masa requerida. Para selectores parciales hay que añadir una condición probabilística
o un certificado entrópico. Una regla total sí tiene `p_n=1`, pero eso es otra
política de selección.

Tampoco se afirma que `-log P(S_n)=o(n)` sea necesario para que un selector concreto
sea consistente. Es la condición uniforme suficiente que permite heredar la
concentración exponencial sin conocer correlaciones más finas entre `S_n` y
`Delta_n`.

## 9. Terminal y techo de afirmación

La decisión es:

```text
ABSTRACT_SELECTION_THEOREM = PROVED_AS_INTERMEDIATE_LEMMA
SELECTOR_CLASS_THEOREM = PROVED
ESSENTIALLY_MIN_COVERAGE_LEX_SPECIFIC = REJECTED

GENERAL_SELECTOR_PROPERTY_SUFFICIENT_FOR_Q2 =
  SUBEXPONENTIAL_SUCCESS_MASS_PLUS_SELECTED_RANK_RECTANGLE

ADDITIONAL_PROPERTY_FOR_CONTINUOUS_DURATION = ORDER_ONLY

MIN_COVERAGE_LEX_ROLE = NONTRIVIAL_MEMBERSHIP_CERTIFICATE
INTRINSICNESS_ALONE_IMPLIES_SUBEXPONENTIAL_MASS = FALSE
```

El resultado permite afirmar:

> En el canal `fixed-n`, `d=2`, todo selector `order-only` de intervalos causales
> cuyo evento de éxito tenga coste logarítmico `o(n)` preserva la concentración de
> fibras y hace consistente en MSE absoluto a `COUNT_VOLUME` para la duración
> lateral relativa. `MIN_COVERAGE_LEX` satisface esa hipótesis por el certificado de
> EF-4.

No demuestra:

- que `1-rho_max^2 -> 0`;
- consistencia relativa o normalizada cuando la varianza total también colapsa;
- recuperación de escala temporal absoluta;
- recoverability desde todo el poset;
- que todo selector intrínseco tenga éxito con probabilidad subexponencial;
- una extensión a `d>=3`;
- prioridad o novedad del lema abstracto o del teorema de clase.

## 10. Relación con precedentes y siguiente obligación legítima

La conexión con inferencia selectiva es conceptual: esa literatura estudia cómo el
condicionamiento por una regla de selección modifica límites y procedimientos. El
teorema 2.1 no depende de sus resultados y se ha probado aquí directamente. En
particular, la analogía no convierte el certificado combinatorio de
`MIN_COVERAGE_LEX` en un corolario de inferencia selectiva.

La restricción a `d=2` tampoco es cosmética en los teoremas 4.1 y 5.1: se usan una
permutación uniforme, rectángulos de rangos y gaps Beta en dos coordenadas. La
literatura sobre causal sets dimensionalmente restringidos trata los 2-orders como
una clase especialmente estructurada; esta nota no extrapola esas herramientas a
dimensión superior.

El siguiente trabajo matemático legítimo, si se abre, no es EF-5 ni una búsqueda de
patrones. Es auditar independientemente el teorema de clase y estudiar criterios de
pertenencia más amplios que el lema 6.1. Cualquier afirmación de prioridad sigue
sujeta a la auditoría bibliográfica externa ya exigida por EF-6.

## Referencias internas y externas mínimas

- `docs/hoja_de_ruta_agosto_2026.md`, EF-3 y EF-4: discrepancia uniforme, cota
  condicionada y certificado prescrito.
- `emergencia/P1a_count_volume_lema_kl_d2.md`, §§5–7: control uniforme de la ley
  Beta-producto, definición de `P_{2,n}`, `Q_{2,n}` y cota de proyección.
- `emergencia/P1a_count_volume_ley_condicionada_d2.md`, §§2–5: independencia entre
  rangos y magnitudes y ley de los gaps.
- W. J. Cunningham y S. Surya, *Dimensionally Restricted Causal Set Quantum
  Gravity: Examples in Two and Three Dimensions*,
  [arXiv:1908.11647](https://arxiv.org/abs/1908.11647).
- X. Tian y J. Taylor, *Selective inference with a randomized response*,
  [arXiv:1507.06739](https://arxiv.org/abs/1507.06739).
