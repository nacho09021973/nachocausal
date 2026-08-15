# EF-8 — preflight de representación macroscópica del evento selector

ESTADO: COMPLETE_DEDUCTIVE_PREFLIGHT
FECHA: 2026-08-13
EF8_STATUS: NOT_OPENED
SIMULACION_ALEATORIA_NUEVA: NINGUNA
MODELO: fixed-n, d=2

## 0. Terminal

El preflight separa dos respuestas:

1. El evento exacto de éxito de MIN_COVERAGE_LEX —unicidad del argmax
   discreto— no es una función del permutón límite. Hay sucesiones a distancia
   macroscópica nula y con el mismo límite para las que el selector alterna entre
   UNIQUE y TIE.
2. Sí existe una clase simplificada, intrínseca y no trivial de selectores con
   evento de éxito macroscópico: los selectores activados por densidades de
   patrones continuas. Para el gate de densidad de inversiones/incomparabilidades,
   el coste y el macroestado condicionado están caracterizados por el problema
   entrópico de Mallows.

El terminal es, por tanto,

    MIN_COVERAGE_LEX_EXACT_MACRO_EVENT = REJECTED_AS_LIMIT_FUNCTIONAL
    MIN_COVERAGE_LEX_SPEED_N_SELECTION_COST = ZERO
    MIN_COVERAGE_LEX_CONDITIONAL_MACROSTATE = LEBESGUE_PERMUTON
    PATTERN_GATED_SELECTOR_CLASS = MACRO_REPRESENTABLE
    INVERSION_GATE_COST = VARIATIONAL_AND_ONE_PARAMETER_COMPUTABLE
    INVERSION_GATE_CONDITIONAL_MACROSTATE = UNIQUE_MALLOWS_PERMUTON
    PREFLIGHT_TERMINAL = PASS_SURROGATE_ONLY
    EF8_STATUS = NOT_OPENED

No se abre EF-8 porque el gate positivo pertenece a una clase surrogate. Abrirlo
requiere decidir si ese es el alcance científico deseado o si se exige primero un
puente adicional hacia MIN_COVERAGE_LEX.

## 1. Pregunta exacta

Sea \(\Pi_n\) una permutación uniforme y \(L_n=L(\Pi_n)\) su permutón
empírico. La pregunta de preflight es si el evento

\[
 S_n=\{\text{MIN_COVERAGE_LEX tiene un argmax único}\}
\tag{1.1}
\]

puede escribirse o aproximarse a velocidad \(n\) mediante un conjunto fijo
\(\mathcal S\) del espacio de permutones, de modo que el LDP

\[
 \Pr(L_n\simeq\mu)
 \asymp \exp[-nD(\mu\Vert\lambda)]
\tag{1.2}
\]

calcule el coste de \(S_n\) y los minimizadores de la ley condicionada.

Se distinguen tres nociones:

- representación exacta secuencial: el éxito eventual queda determinado por el
  límite de \(L_n\);
- equivalencia exponencial bajo una ley concreta: la diferencia simétrica entre
  el evento discreto y un evento macroscópico es despreciable a velocidad \(n\);
- surrogate macroscópico: se cambia explícitamente el gate por una función
  continua del permutón.

El primer punto falla para MIN_COVERAGE_LEX. El segundo no se deduce ni se refuta
solo con ese fallo. El tercero sí puede cerrarse.

## 2. El evento UNIQUE es microscópico

### 2.1 Dos sucesiones con el mismo permutón límite y distinto estado

Fíjese \(n=2m\ge8\). Considérense

\[
 \pi_n^{\mathrm{id}}=(0,1,\ldots,n-1)
\]

y

\[
 \pi_n^{\mathrm{swap}}=(1,0,2,\ldots,n-1).
\]

Sus permutones empíricos convergen al mismo permutón diagonal. Además, una
transposición cambia solo dos de los \(n\) átomos, de modo que su distancia de
discrepancia es a lo sumo \(2/n\).

Para la identidad, el poset es una cadena y

\[
 |[a,b]|=b-a+1.
\]

Si \(a<b<c<d\), entonces

\[
 |[a,b]|+|[c,d]|
 =d-a-(c-b)+2
 \le n.
\tag{2.1}
\]

Por tanto, el primer componente del score lexicográfico es a lo sumo \(m\).
La igualdad solo puede ocurrir si

\[
 a=0,\qquad b=m-1,\qquad c=m,\qquad d=n-1,
\]

y ambos intervalos tienen cardinalidad \(m\). El ganador es único.

Para \(\pi_n^{\mathrm{swap}}\), los elementos 0 y 1 son incomparables y todos
los elementos posteriores forman una cadena por encima de ambos. Si
\(a\in\{0,1\}\) y \(b\ge2\),

\[
 |[a,b]|=b,
\]

mientras que para \(a\ge2\) se conserva \(b-a+1\). Todo candidato satisface

\[
 |[a,b]|+|[c,d]|\le n-1.
\tag{2.2}
\]

El mejor score es

\[
 (m-1,\,2m-1).
\]

Lo alcanzan cuatro cuádruplas: se puede tomar \(a=0\) o \(a=1\), y repartir
las cardinalidades como \((m-1,m)\) o \((m,m-1)\). Por tanto, el estado es TIE.

Así,

\[
 L(\pi_n^{\mathrm{id}})\Longrightarrow\mu_{\mathrm{diag}},
\qquad
 L(\pi_n^{\mathrm{swap}})\Longrightarrow\mu_{\mathrm{diag}},
\]

pero

\[
 \mathbf 1_{S_n}(\pi_n^{\mathrm{id}})=1,
\qquad
 \mathbf 1_{S_n}(\pi_n^{\mathrm{swap}})=0.
\tag{2.3}
\]

Esto prueba que la unicidad exacta no está determinada por el permutón límite.
No existe una función \(s:\mathcal M\to\{0,1\}\) que reproduzca
secuencialmente el estado exacto para toda aproximación de un mismo permutón.

La conclusión es limitada pero suficiente para el preflight: aplicar
directamente el principio de contracción al indicador UNIQUE no está
justificado. No se afirma que sea imposible construir una equivalencia
exponencial específica bajo la ley uniforme.

### 2.2 A velocidad n, el coste real ya es cero

EF-4/EF-7 prueban

\[
 -\log\Pr(S_n)=o(n).
\tag{2.4}
\]

Por tanto,

\[
 \alpha_S
 :=\limsup_n-\frac1n\log\Pr(S_n)
 =0.
\tag{2.5}
\]

El LDP uniforme tiene tasa \(D(\mu\Vert\lambda)\), cuyo único cero es el
permutón de Lebesgue \(\lambda\). Sea \(U\) cualquier vecindad de \(\lambda\).
La bondad de la tasa da

\[
 c_U:=\inf_{\mu\notin U}D(\mu\Vert\lambda)>0
\]

y, por la cota superior del LDP,

\[
 \Pr(L_n\notin U)\le \exp[-nc_U+o(n)].
\]

Dividiendo por (2.4),

\[
 \Pr(L_n\notin U\mid S_n)
 \le
 \exp[-nc_U+o(n)]
 \longrightarrow0.
\tag{2.6}
\]

En consecuencia,

\[
 L_n\mid S_n
 \xrightarrow{\Pr}\lambda.
\tag{2.7}
\]

El evento real de éxito de MIN_COVERAGE_LEX no desplaza el macroestado a
velocidad \(n\). Su contenido sigue siendo microscópico/subexponencial. Esto no
prueba un LDP condicionado completo —faltaría una cota inferior para
intersecciones con \(S_n\)—, pero sí identifica inequívocamente el único
macroestado típico condicionado.

## 3. Clase que sí admite un evento selector macroscópico

### 3.1 Teorema de gates por densidades de patrones

Sean \(\sigma_1,\ldots,\sigma_k\) patrones fijos y

\[
 T(\mu)=
 \bigl(t_{\sigma_1}(\mu),\ldots,t_{\sigma_k}(\mu)\bigr).
\]

Las densidades de patrones son continuas en la topología de permutones. Sea
\(C\subseteq[0,1]^k\) un conjunto de condicionamiento regular en el sentido

\[
 \inf_{\mu:T(\mu)\in C^\circ}D(\mu\Vert\lambda)
 =
 \inf_{\mu:T(\mu)\in\overline C}D(\mu\Vert\lambda)
 =:\alpha_C.
\tag{3.1}
\]

Defínase un selector parcial cuyo evento de activación sea

\[
 S_n^C=\{T(L_n)\in C\}.
\tag{3.2}
\]

La regla que produce el objeto seleccionado después del gate puede ser
determinista o usar aleatoriedad auxiliar; siempre que sea total sobre el gate,
no interviene en su coste.
El principio de contracción y el LDP condicionado dan

\[
 -\frac1n\log\Pr(S_n^C)\longrightarrow\alpha_C
\tag{3.3}
\]

y la tasa condicionada

\[
 \mathcal I_C(\mu)=
 \begin{cases}
 D(\mu\Vert\lambda)-\alpha_C,
   &T(\mu)\in\overline C,\\
 +\infty,&\text{en otro caso},
 \end{cases}
\tag{3.4}
\]

con las precisiones usuales de interior/cierre. Si el conjunto

\[
 \operatorname*{argmin}_{\mu:T(\mu)\in\overline C}
 D(\mu\Vert\lambda)
\tag{3.5}
\]

tiene un único elemento \(\mu_C\), entonces

\[
 L_n\mid S_n^C\xrightarrow{\Pr}\mu_C.
\tag{3.6}
\]

Esto realiza exactamente el segundo nivel propuesto para EF-8: coste positivo,
resolución condicionada y posible cambio de macroestado.

No todo gate de patrones es intrínseco como función del poset. El siguiente caso
sí lo es.

### 3.2 Gate intrínseco por densidad de incomparabilidades

Para una permutación \(\pi\), defínase

\[
 \iota_n(\pi)
 :=
 \frac1{\binom n2}
 \#\{i<j:\pi(i)>\pi(j)\}.
\tag{3.7}
\]

En el 2-order, una inversión corresponde exactamente a un par incomparable. Por
tanto, \(\iota_n\) es la fracción de pares incomparables del poset y no depende
de etiquetas ni de la embedding.

Fíjese \(\delta\in(0,1/2)\) y considérese el evento raro

\[
 S_n^-(\delta)=\{\iota_n\le\delta\}.
\tag{3.8}
\]

Sobre ese evento puede definirse, por ejemplo, una regla order-only y
equivariante que elija uniformemente, mediante aleatoriedad auxiliar
independiente, uno de los pares comparables y devuelva su intervalo causal. Como
\(\delta<1\), el conjunto de pares comparables no es vacío. El evento de éxito
de esta regla es exactamente (3.8).

A escala de permutón,

\[
 \mathcal S_\delta^-=
 \{\mu:t_{21}(\mu)\le\delta\}.
\tag{3.9}
\]

El coste es

\[
 \alpha_-(\delta)
 =
 \inf_{\mu:t_{21}(\mu)\le\delta}
 D(\mu\Vert\lambda)
 >0.
\tag{3.10}
\]

Para la base uniforme, la ausencia de transición de fase del modelo de Mallows
implica que el minimizador es único. Es el permutón
\(\nu_{\theta(\delta)}\), donde \(\theta(\delta)<0\) es el único parámetro que
satisface

\[
 t_{21}(\nu_{\theta(\delta)})=\delta.
\tag{3.11}
\]

La densidad de \(\nu_\theta\), para \(\theta\ne0\), es

\[
 \Phi_\theta(x,y)=
 \frac{
   \frac{\theta}{2}\sinh(\theta/2)
 }{
   \left[
     e^{-\theta/4}\cosh\!\left(\frac{\theta(x-y)}2\right)
     -
     e^{\theta/4}\cosh\!\left(\frac{\theta(x+y-1)}2\right)
   \right]^2
 }.
\tag{3.12}
\]

Por tanto,

\[
 \alpha_-(\delta)
 =
 D(\nu_{\theta(\delta)}\Vert\lambda)
\tag{3.13}
\]

y

\[
 L_n\mid S_n^-(\delta)
 \xrightarrow{\Pr}
 \nu_{\theta(\delta)}.
\tag{3.14}
\]

El coste también es reducible a una optimización unidimensional. Si

\[
 \psi(\theta)
 =
 \sup_{\mu\in\mathcal M}
 \{\theta t_{21}(\mu)-D(\mu\Vert\lambda)\},
\]

entonces

\[
 \alpha_-(\delta)
 =
 \theta(\delta)\delta-\psi(\theta(\delta)),
\qquad
 \psi'(\theta(\delta))=\delta.
\tag{3.15}
\]

El gate superior \(\{\iota_n\ge\delta\}\), con \(\delta>1/2\), es análogo y
usa \(\theta(\delta)>0\).

Así, la clase surrogate no solo existe: contiene un ejemplo intrínseco con coste
positivo, minimizador único y macroestado condicionado explícito.

## 4. Qué falta para volver a MIN_COVERAGE_LEX

Hay dos puentes posibles, ninguno probado aquí.

### Puente A — gate macroscópico seguido del selector congelado

Puede intersectarse un gate como (3.8) con el éxito exacto del selector:

\[
 \widetilde S_n(\delta)
 =
 S_n^-(\delta)\cap
 \{\text{MIN_COVERAGE_LEX es UNIQUE}\}.
\tag{4.1}
\]

Para conservar el coste y el macroestado de (3.8) bastaría demostrar

\[
 -\log
 \Pr(
   \text{MIN_COVERAGE_LEX es UNIQUE}
   \mid S_n^-(\delta)
 )
 =o(n).
\tag{4.2}
\]

El certificado de EF-4 prueba esa propiedad bajo la ley uniforme, no bajo el
macroestado de Mallows condicionado. (4.2) es un nuevo problema combinatorio.

### Puente B — surrogate continuo del score

Puede reemplazarse la unicidad discreta por estabilidad macroscópica. Para una
familia compacta \(\Theta\) de pares de rectángulos y un score escalar continuo
\(F(\mu,\theta)\), el valor

\[
 M(\mu)=\max_{\theta\in\Theta}F(\mu,\theta)
\]

es continuo. Eventos de umbral \(M(\mu)\ge q\), o eventos con un margen positivo
fuera de una vecindad fija del conjunto de maximizadores, son candidatos
compatibles con el LDP.

Esto exige cambiar dos rasgos de MIN_COVERAGE_LEX:

- los endpoints muestreados y la restricción de pertenencia al soporte deben
  sustituirse por parámetros compactos o aproximaciones exponencialmente buenas;
- el score lexicográfico debe reemplazarse por un funcional continuo o por un
  procedimiento jerárquico con márgenes macroscópicos.

Tal surrogate puede ser científicamente útil, pero no es el selector congelado y
no debe recibir su nombre.

## 5. Decisión de preapertura

La pregunta de preflight queda resuelta:

- existe una clase no vacía de eventos selectores macroscópicos para la cual el
  LDP calcula \(\alpha\) y caracteriza los minimizadores;
- existe además un ejemplo intrínseco de 2-orders, el gate por densidad de
  incomparabilidades, cuyo macroestado condicionado es un permutón de Mallows;
- el evento UNIQUE de MIN_COVERAGE_LEX no pertenece directamente a esa clase;
- para el selector congelado, \(\alpha=0\) y el macroestado condicionado sigue
  siendo \(\lambda\).

Por ello:

    MACRO_EVENT_EXISTENCE_GATE = PASS
    INTRINSIC_SURROGATE_GATE = PASS
    FROZEN_SELECTOR_MACRO_BRIDGE = FAIL_NOT_LIMIT_FUNCTIONAL
    FROZEN_SELECTOR_CONDITIONAL_MACROSTATE_SHIFT = ABSENT_AT_SPEED_n
    EF8_OPENING_RECOMMENDATION = REQUIRE_SCOPE_DECISION
    EF8_STATUS = NOT_OPENED

Si EF-8 se abre como teoría de selectores activados por observables
macroscópicos, el preflight ha pasado. Si su definición exige que el protagonista
sea el evento exacto UNIQUE de MIN_COVERAGE_LEX, aún no ha pasado: primero hace
falta (4.2) bajo un macroestado condicionado o un surrogate explícitamente
renombrado.

## Referencias y trazabilidad

- J. Borga, S. Das, S. Mukherjee y P. Winkler,
  Large deviation principle for random permutations,
  https://arxiv.org/abs/2206.04660; Cor. 1.7, Thm. 1.20, Thm. 1.29(ii),
  Ec. (5.3) y App. A.
- R. Kenyon, D. Král', C. Radin y P. Winkler,
  Permutations with fixed pattern densities,
  Random Structures & Algorithms 56 (2020), 220–250.
- emergencia/P1a_estabilidad_seleccion_subexponencial_d2.md, §§2–7.
- dev/EF8_RATE_COMPETITION_PREFLIGHT.md.
- dev/ef8_selector_transposition_probe.py.
- La familia determinista de §2.1 fue además comprobada con
  emergencia.p1a_comparar_selectores_d2.evaluate_selectors para todos los
  tamaños pares \(8\le n\le40\). La demostración de §2.1, no ese sondeo finito,
  sostiene el claim general.
