# WP6 — Control modular exacto del score de fibra

## 0. Estado y alcance

Se conserva, sin redemostrarlo aquí, el tablero global fijado antes de este
paso:

```text
FAMILY_FROZEN
FINITE_N_POSET_LOSS_PROVED
MODULAR_SCORE_RECURSION = PROVED
PRIME_WHOLE_GRAPH_ZERO_LOSS = PROVED
TYPICAL_PRIME_ROOT_TWIN_FIBER = PROVED
TYPICAL_FIBER_ZERO_LOSS = PROVED
INDEPENDENT_TWIN_FLIPS_IN_ORIENTED_FIBER = REFUTED
PERMUTATION_SCORE_FOURTH_MOMENT = PROVED
ASYMPTOTIC_POSET_FISHER_EFFICIENCY_FOR_BOUNDED_SEPARABLE_SCORES = PROVED
THEOREM_PROVED_PRIORITY_AUDIT_PASSED_PROVISIONALLY
POTENTIALLY_NOVEL_THEOREM_NOT_NOVEL_FRAMEWORK
GEOMETRIC_TANGENT_CLASSIFICATION = OPEN
NO_UNIVERSALITY_CLAIM
NEXT_TARGET = GEOMETRIC_TANGENT_CLASSIFICATION
TARGET_SUBCLASS = SYMMETRIC_RANK_ONE_COPULA_TANGENTS
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
RATE_IMPROVEMENT = DEFERRED
PRIORITY = PROVISIONAL_NOT_SEALED
```

No se usa aquí la falsa unicidad general del realizador de un poset de dimensión
dos. El contraejemplo mínimo y el estado documental de ese problema están en
`research_program/work_packages/wp6_d2_null_copula_dichotomy.md`, §5.2bis, y
`docs/bibliography_claims.md`, §5.3.

Todo el argumento es exacto para permutaciones finitas. No requiere aleatoriedad
ni límite asintótico. Los resultados externos usados son el teorema primario de
Gallai sobre orientaciones transitivas de grafos primos, registrado con su
enunciado y paginación en §6.4, y la correspondencia exacta entre módulos
fuertes e intervalos comunes fuertes, registrada en el Apéndice A.1.

## 1. Definiciones del canal, los grafos y el score

### 1.1 Poset orientado

Para `pi in S_N`, el poset estricto etiquetado `P_pi` tiene conjunto base
`[N]={1,...,N}` y relación

\[
i<_{P_\pi}j
\quad\Longleftrightarrow\quad
i<j\ \text{ y }\ \pi(i)<\pi(j).
\]

La clase `[P_pi]` olvida las etiquetas, pero no la orientación temporal: dos
permutaciones tienen la misma observación sii existe una biyección `f:[N]->[N]`
tal que

\[
i<_{P_\sigma}j
\quad\Longleftrightarrow\quad
f(i)<_{P_\pi}f(j).
\]

### 1.2 Comparabilidad e incomparabilidad

El grafo de comparabilidad `C_pi` tiene una arista no orientada `{i,j}` sii `i`
y `j` son comparables en `P_pi`. Para `i<j`, esto equivale a
`pi(i)<pi(j)`. El grafo de incomparabilidad es

\[
G_\pi^{\mathrm{inc}}:=\overline{C_\pi};
\]

por tanto, para `i<j`,

\[
\{i,j\}\in E(G_\pi^{\mathrm{inc}})
\quad\Longleftrightarrow\quad
\pi(i)>\pi(j).
\]

Es exactamente el inversion graph de `pi`, que es un permutation graph. La
orientación de las aristas de `C_pi` inducida por `<_{P_pi}` recupera el poset
etiquetado por clausura transitiva. El grafo no orientado `C_pi` olvida esa
dirección. Pasar a `G_pi^inc` sólo complementa el conjunto de aristas y no
recupera la dirección perdida. Pasar finalmente a `[P_pi]` olvida además las
etiquetas, pero conserva la relación orientada hasta isomorfismo.

### 1.3 Módulos y primalidad

Sea `G=(V,E)` un grafo simple. Un conjunto `M subseteq V` es un **módulo** si
todo vértice `v` exterior a `M` es adyacente a todos los elementos de `M` o a
ninguno:

\[
\forall v\in V\setminus M,
\qquad
N_G(v)\cap M\in\{\varnothing,M\}.
\]

Los módulos triviales son `emptyset`, los singletons y `V`. El grafo es
**primo** sii no tiene módulos no triviales. Un conjunto es módulo de `G` sii es
módulo de su complemento, pues al complementar se intercambian las alternativas
«todos» y «ninguno».

Usamos esta definición literalmente, incluyendo los casos vacuos `N<=2`. Para
`N>=4`, un grafo primo y su complemento son conexos. Los tamaños `N<=3` se
tratan directamente en §6.5 y no se cargan sobre el teorema de Gallai.

### 1.4 Dos órdenes lineales: dos usos que no se confunden

Definimos sobre `[N]` los órdenes lineales

\[
L_1^\pi:\ 1<2<\cdots<N,
\qquad
L_2^\pi:\
\pi^{-1}(1)<\pi^{-1}(2)<\cdots<\pi^{-1}(N).
\]

El par `(L_1^pi,L_2^pi)` tiene simultáneamente dos propiedades distintas:

1. es un **realizador de dimensión dos del poset**, porque
   \[
   P_\pi=L_1^\pi\cap L_2^\pi;
   \]
2. es una **representación por dos órdenes del permutation graph**
   `G_pi^inc`, porque dos vértices son adyacentes exactamente cuando los dos
   órdenes discrepan sobre ellos.

En esta nota, *realizador del poset* designa sólo la primera propiedad y
*representación del permutation graph* sólo la segunda.

Sobre las aristas de `G_pi^inc` definimos la orientación conjugada

\[
i<_{Q_\pi}j
\quad\Longleftrightarrow\quad
i<j\ \text{ y }\ \pi(i)>\pi(j).
\]

Es una orientación transitiva de `G_pi^inc`. Las dos linealizaciones anteriores
se descomponen exactamente como

\[
L_1^\pi=P_\pi\cup Q_\pi,
\qquad
L_2^\pi=P_\pi\cup Q_\pi^{\mathrm{op}}.
\]

Así se ve qué olvida el poset: conserva la orientación `P_pi` sobre las aristas
de comparabilidad, pero olvida cuál de `Q_pi,Q_pi^op` se usó para ordenar cada
par incomparable.

### 1.5 Score bilineal

Trabajamos con índices en `1,...,m`. Para `tau in S_m` y dos perfiles de pesos
`x,y in R^m`, definimos

\[
B_{x,y}(\tau)
:=
\sum_{s=1}^m x_s y_{\tau(s)}
=x^{\mathsf T}P_\tau y,
\]

donde `(P_tau)_{s,t}=1` sii `t=tau(s)`. En particular,

\[
X_N(\pi):=B_{a^{(N)},a^{(N)}}(\pi).
\]

Cuando se restringe un perfil a un intervalo, sus coordenadas se conservan en
orden creciente. Por ejemplo, si `I={p+1,...,p+m}`, entonces

\[
x|_I=(x_{p+1},\ldots,x_{p+m})\in\mathbb R^m.
\]

Sea

\[
\pi=\sigma[\tau_1,\ldots,\tau_k],
\qquad
\sigma\in S_k,
\qquad
\tau_r\in S_{n_r},
\qquad
N=\sum_{r=1}^k n_r.
\]

Los offsets de posiciones y valores del bloque `r` son

\[
p_r=\sum_{t<r}n_t,
\qquad
q_r=\sum_{t:\,\sigma(t)<\sigma(r)}n_t.
\]

Por tanto,

\[
I_r=\{p_r+1,\ldots,p_r+n_r\},
\qquad
J_r=\{q_r+1,\ldots,q_r+n_r\},
\]

y la definición de inflación dice exactamente que

\[
\pi(p_r+s)=q_r+\tau_r(s),
\qquad 1\le s\le n_r.
\]

## 2. Primer lema constructivo: identidad bilineal de inflación

**Lema 1 (recursión bilineal exacta).** Para cualesquiera `x,y in R^N`,

\[
\boxed{
B_{x,y}(\pi)
=
\sum_{r=1}^k
B_{\,x|_{I_r},\,y|_{J_r}}(\tau_r).
}
\]

En particular,

\[
\boxed{
X_N(\pi)
=
\sum_{r=1}^k
B_{\,a^{(N)}|_{I_r},\,a^{(N)}|_{J_r}}(\tau_r).
}
\]

**Demostración.** Los `I_r` forman una partición de `1,...,N`. Separando la
suma que define `B` según esa partición y usando la identidad de inflación,

\[
\begin{aligned}
B_{x,y}(\pi)
&=\sum_{r=1}^k\sum_{s=1}^{n_r}
  x_{p_r+s}\,y_{\pi(p_r+s)}\\
&=\sum_{r=1}^k\sum_{s=1}^{n_r}
  x_{p_r+s}\,y_{q_r+\tau_r(s)}\\
&=\sum_{r=1}^k
  B_{\,x|_{I_r},\,y|_{J_r}}(\tau_r).
\end{aligned}
\]

La especialización `x=y=a^(N)` da la segunda identidad. ∎

**Consecuencia.** No hay productos que mezclen coordenadas de dos bloques
distintos en el score. El cociente determina qué ventana de posiciones se
empareja con qué ventana de valores; el realizador interno determina cómo se
emparejan las coordenadas dentro de esas dos ventanas.

## 3. La recursión correcta sobre el árbol

El estado que debe propagarse hacia un hijo no es un escalar. Es el par ordenado
de perfiles

\[
(x^{(r)},y^{(r)})
=
(x|_{I_r},y|_{J_r}).
\]

Para un nodo `v` del árbol de sustitución, definimos recursivamente

\[
S_v(x,y)=
\begin{cases}
x_1y_1, & v\text{ hoja},\\[2mm]
\displaystyle\sum_{r=1}^k
S_{v_r}(x|_{I_r},y|_{J_r}), &
v=\sigma_v[v_1,\ldots,v_k].
\end{cases}
\]

Por inducción inmediata sobre la altura del árbol,

\[
S_v(x,y)=B_{x,y}(\pi_v).
\]

Así, la recursión modular exacta tiene tipo

```text
(node, position_profile, value_profile) -> scalar,
```

no `node -> X_m` con un único perfil estándar reciclado en todos los nodos.

## 4. Transformaciones exactas dentro de un nodo

Sea `r_m(s)=m+1-s` y sea `R_m` el operador que invierte coordenadas,

\[
(R_mx)_s=x_{r_m(s)}.
\]

**Lema 2 (tabla local de las cuatro simetrías).** Para toda `tau in S_m`,

\[
\boxed{
\begin{array}{c|c}
\text{realizador local} & \text{score con perfiles fijos }(x,y)\\
\hline
\tau & B_{x,y}(\tau)\\
\tau^{-1} & B_{y,x}(\tau)\\
r_m\tau r_m & B_{R_mx,R_my}(\tau)\\
r_m\tau^{-1}r_m & B_{R_my,R_mx}(\tau)
\end{array}}
\]

**Demostración.** Para la inversión, el cambio de índice `s=tau(t)` da

\[
B_{x,y}(\tau^{-1})
=\sum_t x_{\tau(t)}y_t
=B_{y,x}(\tau).
\]

Para reversión a derecha y a izquierda, respectivamente,

\[
B_{x,y}(\tau r_m)=B_{R_mx,y}(\tau),
\qquad
B_{x,y}(r_m\tau)=B_{x,R_my}(\tau).
\]

Componiendo ambas identidades se obtiene la tercera fila; combinándolas con la
identidad de inversión se obtiene la cuarta. ∎

Por tanto, los tres incrementos locales respecto de `tau` son exactamente

\[
\begin{aligned}
\Delta_{\mathrm{inv}}
&=B_{y,x}(\tau)-B_{x,y}(\tau),\\
\Delta_{\mathrm{rc}}
&=B_{R_mx,R_my}(\tau)-B_{x,y}(\tau),\\
\Delta_{\mathrm{rc\mbox{-}inv}}
&=B_{R_my,R_mx}(\tau)-B_{x,y}(\tau).
\end{aligned}
\]

Globalmente, `x=y=a^(N)` anula siempre `Delta_inv`. Si además el perfil global
tiene paridad de reversión

\[
R_Na^{(N)}=\varepsilon_Na^{(N)},
\qquad \varepsilon_N\in\{-1,+1\},
\]

también se anulan los otros dos incrementos. Localmente, en cambio,

\[
x=a^{(N)}|_I,
\qquad
y=a^{(N)}|_J
\]

normalmente son perfiles distintos y no satisfacen una relación de reversión
común. Ninguna fila no trivial de la tabla tiene entonces por qué conservar el
score. Esto demuestra la afirmación precisa:

> que un nodo interno sea primo no implica por sí solo pérdida nula del score;
> una simetría del realizador primo actúa sobre dos perfiles locales distintos.

La tabla es una identidad algebraica. No afirma que las cuatro transformaciones
sean realizadores admisibles del mismo poset orientado en cualquier nodo dado.

## 5. Especialización por tipo de nodo de sustitución

### 5.1 Nodo creciente

Si el cociente es `id_k`, entonces `q_r=p_r` y

\[
B_{x,y}(\pi)
=\sum_{r=1}^k
B_{\,x|_{I_r},\,y|_{I_r}}(\tau_r).
\]

Las ventanas tienen los mismos extremos, aunque los perfiles restringidos siguen
siendo distintos si `x != y` en el nodo padre.

### 5.2 Nodo decreciente

Si el cociente es `r_k`, entonces

\[
q_r=\sum_{t>r}n_t
\]

y

\[
B_{x,y}(\pi)
=\sum_{r=1}^k
B_{\,x|_{I_r},\,y|_{J_r}}(\tau_r),
\qquad
J_r=
\left\{
1+\sum_{t>r}n_t,\ldots,\sum_{t\ge r}n_t
\right\}.
\]

El nodo empareja las ventanas de posiciones de izquierda a derecha con las
ventanas de valores de derecha a izquierda. No invierte por sí mismo el orden
interno de cada `J_r`; esa reorganización sigue siendo `tau_r`.

### 5.3 Nodo primo

Si el cociente `sigma` es simple —el nodo primo del árbol de sustitución—, no
hay simplificación adicional de los offsets:

\[
q_r=\sum_{t:\,\sigma(t)<\sigma(r)}n_t.
\]

Una vez fijados la correspondencia entre módulos y los intervalos `I_r,J_r`, el
efecto de sustituir un realizador interno por una de sus cuatro simetrías es
exactamente el del Lema 2. En particular, el efecto de inversión interna es la
forma antisimétrica

\[
\Delta_{\mathrm{inv}}
=\sum_{s=1}^{n_r}
\left(y_sx_{\tau_r(s)}-x_sy_{\tau_r(s)}\right),
\]

que puede ser no nula cuando `x != y`.

### 5.4 Separación exacta de las dos fuentes de variación

Consideremos dos realizadores de la misma fibra y transportemos una
correspondencia entre módulos del mismo tamaño. En el bloque `r`, escribamos sus
datos como

\[
(x_r,y_r,\tau_r)
\quad\text{y}\quad
(\widehat x_r,\widehat y_r,\widehat\tau_r).
\]

El cambio total de score es

\[
\Delta X
=\sum_r
\left[
B_{\widehat x_r,\widehat y_r}(\widehat\tau_r)
-B_{x_r,y_r}(\tau_r)
\right].
\]

Añadiendo y restando
`B_{hat x_r,hat y_r}(tau_r)` se obtiene la descomposición exacta

\[
\boxed{
\Delta X
=
\underbrace{\sum_r
\left[
B_{\widehat x_r,\widehat y_r}(\tau_r)
-B_{x_r,y_r}(\tau_r)
\right]}_{\text{reasignación de ventanas}}
+
\underbrace{\sum_r
\left[
B_{\widehat x_r,\widehat y_r}(\widehat\tau_r)
-B_{\widehat x_r,\widehat y_r}(\tau_r)
\right]}_{\text{reorganización interna}}.
}
\]

La primera suma mide cómo el cociente cambia los perfiles recibidos por los
módulos. La segunda mantiene fijos esos perfiles nuevos y mide sólo el cambio del
realizador interno. Para una simetría prima, la segunda suma se evalúa con la
tabla del Lema 2.

Esta identidad no presupone que toda reasignación o toda simetría sea admisible:
se aplica a cada par de realizadores que pertenezca realmente a la fibra.

## 6. Qué se ha demostrado y qué sigue abierto

### 6.1 Resultado cerrado

Para cualquier árbol de sustitución ya dado, el score se computa exactamente
propagando dos perfiles. Dados dos realizadores y una correspondencia entre sus
módulos, su diferencia de score se separa mecánicamente en reasignación de
ventanas y reorganización interna. No quedan términos cruzados ocultos en el
propio score.

### 6.2 Precaución para la pérdida de Fisher

La ausencia de términos cruzados en `X_N` no implica una suma automática de
pérdidas por nodo. Si, condicionalmente a una fibra `P`, se escribe

\[
X_N=\sum_r Z_r,
\]

entonces

\[
\operatorname{Var}(X_N\mid P)
=\sum_r\operatorname{Var}(Z_r\mid P)
+2\sum_{r<s}\operatorname{Cov}(Z_r,Z_s\mid P).
\]

Controlar `L_N` exige por tanto la ley condicional conjunta de las decisiones
modulares, no sólo el diámetro de la fibra ni los incrementos nodo a nodo.

### 6.3 Auditoría de orientación y dualidad

Sea `r(i)=N+1-i`. Las cuatro transformaciones candidatas no tienen todas el
mismo efecto sobre el poset orientado:

\[
\begin{array}{c|c|c}
\text{permutación} & \text{relación con }P_\pi & \text{mapa explícito}\\
\hline
\pi & P_\pi\text{ mismo} & \mathrm{id}\\
\pi^{-1} & P_{\pi^{-1}}\cong P_\pi & i\mapsto\pi(i)\\
r\pi r & P_{r\pi r}\cong P_\pi^{\mathrm{op}} & i\mapsto r(i)\\
r\pi^{-1}r & P_{r\pi^{-1}r}\cong P_\pi^{\mathrm{op}}
& i\mapsto r(\pi(i))
\end{array}
\]

Para la segunda fila, si `i <_{P_pi} j`, entonces
`pi(i)<pi(j)` y `pi^{-1}(pi(i))<pi^{-1}(pi(j))`, de modo que
`pi(i)<_{P_{pi^{-1}}}pi(j)`. Para la tercera, la misma hipótesis equivale a

\[
r(j)<r(i),
\qquad
(r\pi r)(r(j))=r(\pi(j))<r(\pi(i))=(r\pi r)(r(i)),
\]

lo que invierte la relación. La cuarta fila compone las dos transformaciones
anteriores.

Por tanto,

\[
\pi,\pi^{-1}\in\mathcal F_N([P_\pi])
\]

siempre, mientras que `r pi r` y `r pi^{-1} r` pertenecen en general a la fibra
dual. No se usa ni se supone \(P_\pi\cong P_\pi^{\mathrm{op}}\). La órbita de
cuatro es un superconjunto natural para el puente, no una fibra garantizada.

### 6.4 Teorema primario usado

La referencia primaria es:

> T. Gallai, “Transitiv orientierbare Graphen”, *Acta Mathematica Academiae
> Scientiarum Hungaricae* **18** (1967), 25–66,
> DOI [`10.1007/BF02020961`](https://doi.org/10.1007/BF02020961). Escaneo del
> volumen primario: [`real-j.mtak.hu/7414`](https://real-j.mtak.hu/7414/).

El objeto del artículo es un grafo simple finito **etiquetado/fijado** y sus
orientaciones transitivas; no son clases de isomorfismo de posets. Gallai
construye la descomposición canónica en (1.2)–(1.8). En (1.8)(5), pp. 28–29, el
cociente irreducible tiene al menos cuatro vértices, él y su complemento son
conexos y todas sus aristas forman una sola clase. En (1.10), p. 29, afirma que
cada uno de esos cocientes, cuando es transitivamente orientable, posee
**exactamente dos orientaciones transitivas**. Son una orientación y su reversa,
pues revertir todas las aristas conserva transitividad.

El transporte desde la terminología primaria a «primo» no se presupone. Los
bloques `A_i` de la descomposición de Gallai son módulos por (1.2)(3a): cada
vértice de otro bloque es adyacente a todos los elementos de `A_i` o a ninguno.
Si `G` es primo, esos bloques sólo pueden ser singletons y el cociente de Gallai
es el propio `G`. Además, para al menos cuatro vértices, `G` y `complement(G)`
son conexos: una componente propia sería un módulo; si todas las componentes
fueran singletons, cualquier par de vértices sería un módulo. El mismo argumento
se aplica al complemento. Así, el grafo primo cae exactamente en el caso
(1.8)(5), no sólo por una analogía terminológica. Por tanto, la consecuencia
exacta que usamos es:

> **Gallai, consecuencia de (1.8)(5), (1.9) y (1.10).** Un grafo de
> comparabilidad primo con al menos cuatro vértices tiene exactamente dos
> orientaciones transitivas, una opuesta a la otra.

Esto recupera también, sin importarlo como una caja negra, el grupo de cuatro
simetrías de una representación prima. Como `G` y `complement(G)` tienen los
mismos módulos, ambos son primos; si ambos son grafos de comparabilidad, sus
orientaciones transitivas `Q` y `P` sólo pueden revertirse. Las cuatro parejas
de órdenes resultantes son

\[
(L_1,L_2),\quad
(L_2,L_1),\quad
(L_1^{\mathrm{op}},L_2^{\mathrm{op}}),\quad
(L_2^{\mathrm{op}},L_1^{\mathrm{op}}).
\]

Tras normalizar el primer orden como `1<...<N`, corresponden exactamente a

\[
\pi,\quad \pi^{-1},\quad r\pi r,\quad r\pi^{-1}r.
\]

Es el grupo de Klein generado por intercambiar los dos órdenes y revertir ambos.
Pero un isomorfismo del **poset orientado** fija la orientación `P` del grafo de
comparabilidad, así que en el transporte de §6.5 sólo queda la elección
`Q` frente a `Q^op`.

Esto es unicidad de una orientación sobre el mismo conjunto de vértices. No
identifica representaciones geométricas ni cocienta por automorfismos. Esa
característica es precisamente la adecuada: cualquier isomorfismo del poset se
transporta primero al conjunto de vértices fijo y sólo entonces se aplica el
teorema. Un automorfismo puede preservar o intercambiar las dos orientaciones,
pero no crea una tercera.

### 6.5 Teorema del puente, con transporte explícito

**Teorema 3 (puente primo orientado; versión fuerte).** Para `pi,sigma in S_N`,

\[
\boxed{
[P_\sigma]=[P_\pi]
\ \land\
G_\pi^{\mathrm{inc}}\text{ primo}
\quad\Longrightarrow\quad
\sigma\in\{\pi,\pi^{-1}\}.
}
\]

En particular, la conclusión original

\[
\sigma\in
\mathcal O(\pi)
=\{\pi,\pi^{-1},r\pi r,r\pi^{-1}r\}
\]

es cierta.

**Demostración para `N>=4`.** Sea

\[
f:P_\sigma\longrightarrow P_\pi
\]

un isomorfismo de posets. Para un orden `L` sobre el dominio, escribimos
`f_*L` para el orden transportado:

\[
u<_{f_*L}v
\quad\Longleftrightarrow\quad
f^{-1}(u)<_L f^{-1}(v).
\]

Pongamos

\[
A=f_*L_1^\sigma,
\qquad
B=f_*L_2^\sigma.
\]

Entonces `A` y `B` son órdenes lineales sobre el conjunto etiquetado `[N]`,

\[
A\cap B=f_*P_\sigma=P_\pi,
\]

y discrepan exactamente sobre las aristas de `G_pi^inc`. Orientemos cada una
de esas aristas según `A` y llamemos `Q'` a la orientación resultante. Es
transitiva: si `u <_A v <_A w` y `uv,vw` son aristas de incomparabilidad,
entonces `v <_B u` y `w <_B v`; por transitividad de `B`, `w <_B u`, mientras
`u <_A w`, luego `uw` también es arista y queda orientada `u -> w`.

Así, `Q'` es una orientación transitiva del grafo primo
`G_pi^inc`. La orientación `Q_pi` de §1.4 es otra. Por Gallai,

\[
Q'=Q_\pi
\quad\text{o}\quad
Q'=Q_\pi^{\mathrm{op}}.
\]

Sobre cada arista de comparabilidad, tanto `A` como `B` tienen la orientación
fijada por `P_pi`. Sobre cada arista de incomparabilidad son opuestos. Por las
identidades de §1.4 se sigue, respectivamente,

\[
(A,B)=(L_1^\pi,L_2^\pi)
\quad\text{o}\quad
(A,B)=(L_2^\pi,L_1^\pi).
\]

No queda libertad de relabeling oculta. En el primer caso, `f` es el único
isomorfismo entre los órdenes lineales `L_1^sigma` y `L_1^pi`; por rangos,
`f(i)=i`, y la igualdad de los segundos órdenes da `sigma=pi`. En el segundo,
`f` manda el elemento de rango `i` en `L_1^sigma` al de rango `i` en
`L_2^pi`, luego

\[
f(i)=\pi^{-1}(i).
\]

La igualdad `f_*L_2^sigma=L_1^pi` implica, para cada rango `t`,

\[
f(\sigma^{-1}(t))=t,
\]

y por tanto

\[
\pi^{-1}(\sigma^{-1}(t))=t,
\qquad
\sigma^{-1}=\pi,
\qquad
\sigma=\pi^{-1}.
\]

Esto incluye cualquier posible automorfismo: se empezó con un `f` arbitrario y
la unicidad de las dos orientaciones, seguida de la normalización por rangos, lo
forzó a uno de los dos mapas indicados. ∎

**Tamaños pequeños.** Para `N=1` hay una sola permutación. Para `N=2`, las dos
permutaciones producen clases distintas (cadena y antichain) y ambas son
autoinversas. Para `N=3` no existe ningún grafo primo bajo la definición de
§1.3: con cero o tres aristas cualquier par es módulo; con una arista sus dos
extremos forman un módulo; con dos aristas los dos extremos del camino forman
un módulo. Por tanto, el teorema vale para todo `N>=1`.

La conclusión describe la fibra completa:

\[
\boxed{
G_\pi^{\mathrm{inc}}\text{ primo}
\quad\Longrightarrow\quad
\mathcal F_N([P_\pi])=\{\pi,\pi^{-1}\},
}
\]

entendiendo el lado derecho como conjunto, de tamaño uno si `pi=pi^{-1}`.

### 6.6 Falsificador exhaustivo finito

Se ejecutó una enumeración determinista para `1<=N<=8`. Para cada permutación:

1. se construyó la matriz exacta de la relación estricta con
   `dev/r3_bridge_e_fibers.py:relation_matrix`;
2. se canonizó la clase de isomorfismo mediante
   `dev/r3_bridge_e_fibers.py:canonical_form`, que refina colores y enumera
   exactamente las reetiquetaciones restantes;
3. se enumeraron todos los subconjuntos propios de vértices y se aplicó
   literalmente la definición de módulo de §1.3;
4. se agruparon todas las permutaciones primas por clase canónica y se comparó
   cada fibra con `O(pi)` y con `{pi,pi^{-1}}`.

Filtrar primero por primalidad no omite miembros de una fibra: un isomorfismo de
posets induce un isomorfismo de sus grafos de incomparabilidad y la primalidad es
invariante por isomorfismo.

El resultado fue:

| `N` | permutaciones primas | clases de poset | histograma de tamaños de fibra | violaciones |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | `1:1` | 0 |
| 2 | 2 | 2 | `1:2` | 0 |
| 3 | 0 | 0 | — | 0 |
| 4 | 2 | 1 | `2:1` | 0 |
| 5 | 6 | 4 | `1:2, 2:2` | 0 |
| 6 | 46 | 25 | `1:4, 2:21` | 0 |
| 7 | 338 | 174 | `1:10, 2:164` | 0 |
| 8 | 2926 | 1481 | `1:36, 2:1445` | 0 |

En las `1688` clases primas acumuladas, cada fibra fue exactamente
`{pi,pi^{-1}}`. La columna «violaciones» cuenta fallos de la inclusión en
`O(pi)`. El chequeo finito concuerda con el Teorema 3, pero no forma parte de su
prueba.

### 6.7 Corolario de pérdida Fisher exactamente nula

Para cualquier perfil real `a` —en particular para el perfil sinusoidal—,

\[
X_N(\pi^{-1})
=a^{\mathsf T}P_{\pi^{-1}}a
=a^{\mathsf T}P_\pi^{\mathsf T}a
=X_N(\pi),
\]

pues un escalar coincide con su transpuesto. Por el Teorema 3, `X_N` es
constante sobre toda fibra cuyo grafo de incomparabilidad sea primo. Para
`Pi_N` uniforme —y, de hecho, para cualquier ley que dé probabilidad positiva a
la fibra—,

\[
\boxed{
G_\pi^{\mathrm{inc}}\text{ primo}
\quad\Longrightarrow\quad
\operatorname{Var}\!\left(
X_N(\Pi_N)\mid[P_{\Pi_N}]=[P_\pi]
\right)=0.
}
\]

El cierre es estrictamente de grafo completo y tamaño finito. No implica
`L_N=o(N)`, no usa probabilidades de raíz prima y no introduce una afirmación de
universalidad.

```text
BRIDGE_VERDICT = PROVED
EXACT_PRIME_FIBER = {pi, pi^{-1}}
PRIME_WHOLE_GRAPH_ZERO_LOSS = PROVED
ASYMPTOTIC_POSET_EFFICIENCY = CLOSED_IN_SECTION_7_FOR_BOUNDED_SEPARABLE_SCORES
```

## 7. Cuarto momento y eficiencia en el evento excepcional

Esta sección conserva sin redemostrarlos el Teorema 4 y la cota probabilística
del evento excepcional. Su única entrada aleatoria nueva es una permutación
uniforme `Pi_N`; no se introducen simulaciones ni observables adicionales.
Aquí `A_N` denota el evento «raíz prima y todos sus hijos son hojas o twins»;
su definición y el argumento estructural congelado se conservan en el
Apéndice A.

### 7.1 Primer y segundo momentos exactos

Sea

\[
X_N=\sum_{i=1}^N a_i a_{\Pi_N(i)},
\qquad
\sum_{i=1}^N a_i=0,
\qquad
|a_i|\le M,
\]

y escribamos

\[
S_r:=\sum_{i=1}^N a_i^r.
\]

Para cada `i`, `Pi_N(i)` es uniforme en `[N]`; por tanto

\[
\mathbb E[X_N]
=\sum_i a_i\frac{\sum_j a_j}{N}=0.
\]

No se usa independencia para el segundo momento. Si `i != j`, el par ordenado
`(Pi_N(i),Pi_N(j))` es uniforme entre los `N(N-1)` pares distintos, y

\[
\mathbb E[a_{\Pi_N(i)}^2]=\frac{S_2}{N},
\qquad
\mathbb E[a_{\Pi_N(i)}a_{\Pi_N(j)}]
=\frac{\sum_{u\ne v}a_ua_v}{N(N-1)}
=-\frac{S_2}{N(N-1)}.
\]

Como `sum_{i ne j} a_i a_j=-S_2`, resulta

\[
\boxed{
\mathbb E[X_N^2]
=\frac{S_2^2}{N-1}
}
\qquad(N\ge2).
\]

Para `N=1`, el centrado obliga a `a_1=0` y ambos momentos son cero.

### 7.2 Expansión combinatoria exacta del cuarto momento

Definimos el factorial descendente

\[
(N)_r=N(N-1)\cdots(N-r+1).
\]

En cada patrón de coincidencias, las imágenes de los índices distintos son una
muestra ordenada uniforme sin reemplazo. Las sumas ordenadas necesarias en el
lado de los índices son

\[
\begin{array}{rcl}
D_4&:=&\displaystyle\sum_i a_i^4=S_4,\\[1mm]
D_{31}&:=&\displaystyle\sum_{i\ne j}a_i^3a_j=-S_4,\\[1mm]
D_{22}&:=&\displaystyle\sum_{i\ne j}a_i^2a_j^2=S_2^2-S_4,\\[1mm]
D_{211}&:=&\displaystyle\sum_{\substack{i,j,k\ \mathrm{distintos}}}
             a_i^2a_ja_k=2S_4-S_2^2,\\[1mm]
D_{1111}&:=&\displaystyle\sum_{\substack{i,j,k,\ell\ \mathrm{distintos}}}
             a_ia_ja_ka_\ell=3S_2^2-6S_4.
\end{array}
\]

Las dos primeras identidades usan `sum_j a_j=0`. Para la cuarta, fijando `i`,

\[
\sum_{\substack{j,k\ne i\\j\ne k}}a_ja_k
=\left(\sum_{j\ne i}a_j\right)^2-\sum_{j\ne i}a_j^2
=2a_i^2-S_2.
\]

La última es `4!` veces la cuarta suma elemental simétrica. La identidad de
Newton con `S_1=0` da

\[
24e_4=3S_2^2-6S_4.
\]

Los números de colocaciones de los patrones `4`, `3+1`, `2+2`, `2+1+1` y
`1+1+1+1`, usando las sumas ordenadas anteriores, son respectivamente
`1,4,3,6,1`. La suma sobre las imágenes tiene el mismo `D` que la suma sobre
los índices y se divide por `(N)_r`. Se obtiene así, para `N>=4`,

\[
\boxed{
\begin{aligned}
\mathbb E[X_N^4]
={}&\frac{S_4^2}{N}
+\frac{4S_4^2}{(N)_2}
+\frac{3(S_2^2-S_4)^2}{(N)_2}\\
&+\frac{6(2S_4-S_2^2)^2}{(N)_3}
+\frac{9(S_2^2-2S_4)^2}{(N)_4}.
\end{aligned}}
\tag{7.1}
\]

Para `N=1,2,3`, la misma fórmula vale omitiendo los patrones con más de `N`
índices distintos. En particular, (7.1) no contiene un término `S_3`: el
centrado y el uso del mismo perfil en ambos lados convierten cada contribución
en el cuadrado de una suma de patrón.

### 7.3 Cota uniforme con constante universal

Para `N>=4`, usamos

\[
S_2\le NM^2,
\qquad
S_4\le NM^4,
\qquad
0\le S_4\le S_2^2.
\]

Además,

\[
0\le S_2^2-S_4
=\sum_{i\ne j}a_i^2a_j^2
\le N(N-1)M^4,
\]

y tanto `|2S_4-S_2^2|` como `|S_2^2-2S_4|` son a lo sumo
`S_2^2<=N^2M^4`. Los cinco términos de (7.1) quedan acotados, en su orden, por

\[
N^2M^8,
\quad
N^2M^8,
\quad
3N^2M^8,
\quad
4N^2M^8,
\quad
6N^2M^8.
\]

En los dos últimos se usaron, para `N>=4`,

\[
\frac{6N^3}{(N-1)(N-2)}\le4N^2,
\qquad
\frac{9N^3}{(N-1)(N-2)(N-3)}\le6N^2;
\]

ambas desigualdades son igualdades en `N=4` y su margen crece después. Así,

\[
\mathbb E[X_N^4]\le15N^2M^8
\qquad(N\ge4).
\]

Para `N<=3`, la cota elemental `|X_N|<=NM^2` da
`E[X_N^4]<=N^4M^8<=15N^2M^8`. Por tanto, para todo `N>=1`,

\[
\boxed{
\mathbb E[X_N^4]\le15N^2M^8.
}
\tag{7.2}
\]

La constante universal demostrada es, pues, `C=15`. No se invoca ninguna
desigualdad de concentración.

### 7.4 Cuarto momento del score Fisher

Como el score de la permutación de rangos es

\[
\dot\ell_N^\Pi=2X_N,
\]

(7.2) implica directamente

\[
\boxed{
\mathbb E[(\dot\ell_N^\Pi)^4]
\le240N^2M^8.
}
\tag{7.3}
\]

También, por §7.1,

\[
I_N^\Pi
=\mathbb E[(\dot\ell_N^\Pi)^2]
=4\frac{S_2^2}{N-1}.
\tag{7.4}
\]

### 7.5 Combinación con el evento excepcional

Sea `B_N=A_N^c`. La prueba del Teorema 2 de Bouvel, Chauve, Mishna y Rossin
aplica su Lema 1 con `c=1` y afirma exactamente que la proporción de
permutaciones fuera de `A_N` es `O(N^{-1})`: véanse pp. 318–319 de
[“Average-case analysis of perfect sorting by reversals”](https://www.cecm.sfu.ca/~cchauve/Publications/CPM09.pdf).
Fijamos, sin inventar una constante que la fuente no publica, constantes
finitas `C_A>0` y `N_A` tales que

\[
\Pr(B_N)\le\frac{C_A}{N}
\qquad(N\ge N_A).
\tag{7.5}
\]

El evento `A_N` es medible respecto de `[P]`: depende del árbol modular
canónico del inversion graph, que queda determinado hasta isomorfismo por el
poset. Por el Teorema 4, la varianza condicional del score es cero en `A_N`.
Si

\[
L_N:=\mathbb E[\operatorname{Var}(\dot\ell_N^\Pi\mid[P])],
\]

entonces

\[
L_N
=\mathbb E[\operatorname{Var}(\dot\ell_N^\Pi\mid[P])
             \mathbf1_{B_N}].
\]

Punto a punto,
`Var(dot ell_N^Pi | [P]) <= E[(dot ell_N^Pi)^2 | [P]]`. Como `B_N` es
`[P]`-medible, la propiedad de torre da

\[
L_N
\le
\mathbb E[(\dot\ell_N^\Pi)^2\mathbf1_{B_N}].
\]

Cauchy–Schwarz, (7.3) y (7.5) producen, sin ocultar la dependencia de la
constante externa,

\[
\boxed{
L_N
\le\sqrt{240C_A}\,M^4\sqrt N
\qquad(N\ge N_A).
}
\tag{7.6}
\]

En particular, si `M=O(1)`, entonces `L_N=O(sqrt(N))=o(N)`.

### 7.6 Teorema de eficiencia para scores separables acotados

Sea ahora un array triangular determinista `a_{i,N}` tal que

\[
M_*:=\sup_N\max_{1\le i\le N}|a_{i,N}|<\infty,
\qquad
\sum_{i=1}^N a_{i,N}=0,
\qquad
\frac1N\sum_{i=1}^N a_{i,N}^2\longrightarrow c>0.
\]

Por (7.4),

\[
I_N^\Pi
=4\frac{(\sum_i a_{i,N}^2)^2}{N-1}
=4c^2N+o(N).
\]

Usando (7.6) con `M=M_*` y
`q_N=1-L_N/I_N^Pi`, obtenemos la cota con constantes visibles

\[
0\le1-q_N
\le
\left(
\frac{\sqrt{240C_A}\,M_*^4}{4c^2}+o(1)
\right)N^{-1/2}.
\]

Por consiguiente,

\[
\boxed{
1-q_N=O(N^{-1/2}),
\qquad
q_N\longrightarrow1.
}
\tag{7.7}
\]

**Teorema 5 (`ASYMPTOTIC_POSET_FISHER_EFFICIENCY_FOR_BOUNDED_SEPARABLE_SCORES`).**
Para la permutación uniforme, el canal exacto `Pi_N -> [P_Pi_N]` y cualquier
array triangular que satisfaga las tres hipótesis anteriores, el poset no
etiquetado retiene una fracción de información Fisher que converge a uno, con
la tasa (7.7).

El alcance es exclusivamente la clase de scores separables acotados indicada.
No se afirma que todo perfil de esa clase proceda de un tangente geométrico, ni
se formula un principio universal de causal sets.

### 7.7 Corolario sinusoidal

Para

\[
a_{i,N}=\mathbb E[\sin(2\pi U_{(i)})],
\]

la primera hipótesis es inmediata:

\[
|a_{i,N}|\le\mathbb E|\sin(2\pi U_{(i)})|\le1.
\]

Para el centrado, los order statistics sólo reordenan una muestra uniforme
`U_1,...,U_N`; por linealidad,

\[
\sum_{i=1}^N a_{i,N}
=\mathbb E\!\left[\sum_{i=1}^N\sin(2\pi U_{(i)})\right]
=\sum_{j=1}^N\mathbb E[\sin(2\pi U_j)]
=0.
\]

Finalmente, `E[U_(i)]=i/(N+1)` y

\[
\operatorname{Var}(U_{(i)})
=\frac{i(N+1-i)}{(N+1)^2(N+2)}
\le\frac1{4(N+2)}.
\]

La propiedad `2pi`-Lipschitz del seno y Cauchy–Schwarz dan uniformemente

\[
\left|a_{i,N}-\sin\!\left(\frac{2\pi i}{N+1}\right)\right|
\le2\pi\,\mathbb E\left|U_{(i)}-\frac{i}{N+1}\right|
\le\frac{\pi}{\sqrt{N+2}}.
\tag{7.8}
\]

Como ambos términos están en `[-1,1]`, (7.8) implica que la diferencia entre
sus cuadrados es a lo sumo `2pi/sqrt(N+2)`. Para `N>=2`, la suma geométrica de
las raíces `(N+1)`-ésimas da

\[
\frac1N\sum_{i=1}^N
\sin^2\!\left(\frac{2\pi i}{N+1}\right)
=\frac{N+1}{2N}.
\]

Por tanto,

\[
\left|
\frac1N\sum_{i=1}^Na_{i,N}^2-\frac{N+1}{2N}
\right|
\le\frac{2\pi}{\sqrt{N+2}},
\]

y en particular

\[
\boxed{
\frac1N\sum_{i=1}^Na_{i,N}^2\longrightarrow\frac12.
}
\]

El Teorema 5 se aplica con `M_*=1` y `c=1/2`. En consecuencia, para la
dirección geométrica sinusoidal congelada,

\[
\boxed{
L_N\le\sqrt{240C_A}\sqrt N,
\qquad
1-q_N=O(N^{-1/2}),
\qquad
q_N\longrightarrow1.
}
\]

Más precisamente, la constante asintótica superior obtenida por este argumento
es

\[
1-q_N
\le(\sqrt{240C_A}+o(1))N^{-1/2},
\]

porque `4c^2=1`.

### 7.8 Falsificador finito del cuarto momento

Se verificó (7.1) con aritmética racional exacta por enumeración completa de
`S_N` para `1<=N<=8`. Para cada tamaño se construyeron determinísticamente
cinco perfiles enteros no constantes y se restó su media racional, produciendo
cinco perfiles racionales centrados. Para cada uno se compararon exactamente:

1. la media de `X_N^4` sobre las `N!` permutaciones;
2. la expresión por patrones de §7.2, omitiendo los patrones imposibles si
   `N<4`;
3. la desigualdad `E[X_N^4]<=15N^2M^8`.

Los `40` casos dieron igualdad entre 1 y 2 y satisficieron 3. El mayor espacio
enumerado fue `S_8`, con `40320` permutaciones por perfil. Este chequeo es un
falsificador de errores de coeficientes, signos y casos pequeños; no interviene
en la prueba de (7.1) ni de (7.2).

### 7.9 Estado cerrado y límites del resultado

La fórmula (7.1) es una identidad finita; el chequeo exhaustivo de §7.8
es sólo un falsificador. El resultado asintótico usa además la cota primaria
(7.5), pero no usa simulación.

```text
FOURTH_MOMENT_VERDICT = FOURTH_MOMENT_PROVED
PERMUTATION_SCORE_FOURTH_MOMENT = PROVED_WITH_C_15
TYPICAL_FIBER_ZERO_LOSS = PROVED
EXCEPTIONAL_EVENT_PROBABILITY = PROVED_FROM_PRIMARY_THEOREM
ASYMPTOTIC_POSET_FISHER_EFFICIENCY_FOR_BOUNDED_SEPARABLE_SCORES = PROVED
SINUSOIDAL_POSET_FISHER_EFFICIENCY = PROVED
GEOMETRIC_TANGENT_CLASSIFICATION = OPEN
NO_UNIVERSALITY_CLAIM
```

## Apéndice A — Raíz prima con hojas y twins

Esta sección es enteramente determinista. No usa la distribución de una
permutación uniforme, el teorema probabilístico sobre el árbol de intervalos
fuertes ni ninguna estimación del evento excepcional.

### A.1 Definición exacta de la clase finita

Un subconjunto no vacío `B subseteq [N]` es un **intervalo común** de `pi` si
es simultáneamente un intervalo de posiciones y su imagen es un intervalo de
valores:

\[
B=\{p+1,\ldots,p+m\},
\qquad
\pi(B)=\{q+1,\ldots,q+m\}.
\]

Dos subconjuntos se solapan si su intersección es no vacía y ninguno contiene
al otro. Un intervalo común es **fuerte** si no se solapa con ningún otro
intervalo común. Los intervalos fuertes, ordenados por inclusión, forman el
árbol de intervalos fuertes: la raíz es `[N]` y los hijos de un nodo son sus
intervalos fuertes propios maximales. Si los hijos de la raíz son
`B_1,...,B_m` en orden de posiciones, cada `B_s` es también una ventana de
valores. Existe entonces una única permutación cociente `alpha in S_m` y
permutaciones internas `tau_s in S_|B_s|` tales que

\[
\pi=\alpha[\tau_1,\ldots,\tau_m].
\]

La raíz es **prima** cuando su cociente es un nodo primo de la descomposición
modular, no un nodo creciente ni decreciente. Equivalentemente en esta
representación, `alpha` es simple y su inversion graph es primo.

No se identifica por decreto la terminología de intervalos con la de módulos.
La representación `(L_1^pi,L_2^pi)` de §1.4 permite aplicar el siguiente
resultado exacto:

> M. Habib y C. Paul, “A survey of the algorithmic aspects of modular
> decomposition”, *Computer Science Review* **4** (2010), 41–59, §7.1,
> Lemma 20, p. 55: en una representación de un permutation graph, los módulos
> fuertes del grafo son exactamente los intervalos comunes fuertes de los dos
> órdenes. [Texto del artículo](https://www.irif.fr/~habib/Documents/HP10.pdf).

En nuestra convención, ser intervalo de `L_1^pi` significa ser intervalo de
posiciones y ser intervalo de `L_2^pi` significa que `pi(B)` es un intervalo de
valores. Por tanto, el lema identifica exactamente —sobre el mismo conjunto de
vértices— los nodos del árbol anterior con los módulos fuertes de
`G_pi^inc`. Además, si el cociente de la raíz no fuese primo como grafo, su
descomposición modular tendría un módulo fuerte propio, o sería un cociente
completo/vacío; por el mismo lema aparecería un intervalo fuerte intermedio, o
la raíz sería decreciente/creciente. Esto prueba la equivalencia usada en el
párrafo anterior.

Definimos finalmente

\[
\boxed{
A_N(\pi):\quad
\begin{array}{l}
\text{la raíz del árbol de intervalos fuertes es prima, y}\\
\text{cada hijo de la raíz tiene tamaño uno o dos.}
\end{array}}
\]

Un hijo `B_s` de tamaño dos es un módulo porque es un intervalo común; sus dos
vértices tienen el mismo vecindario fuera de `B_s` y son por ello **twins**.
Su patrón interno sólo puede ser `tau_s=12` o `tau_s=21`. En el primer caso
los dos elementos forman una cadena en `P_pi` y son twins no adyacentes en el
inversion graph; en el segundo forman una anticadena y son twins adyacentes.
Es el nodo lineal de tamaño dos del árbol. Así queda demostrado el puente entre
los cuatro lenguajes usados aquí: bloque de inflación, intervalo fuerte, módulo
fuerte y twin de tamaño dos.

### A.2 Caracterización exacta de la fibra

La parametrización tentativa por flips independientes es falsa como libertad
de la fibra orientada. El resultado exacto es más rígido.

**Teorema 4 (fibra de raíz prima con hojas y twins).** Si `A_N(pi)`, entonces

\[
\boxed{
\mathcal F_N([P_\pi])=\{\pi,\pi^{-1}\}.
}
\]

**Demostración.** Sea `sigma` tal que `[P_sigma]=[P_pi]` y sea `f` un
isomorfismo orientado de `P_sigma` sobre `P_pi`. El mapa `f` induce un
isomorfismo de los inversion graphs y, por tanto, lleva módulos fuertes
maximales propios a módulos fuertes maximales propios. Por el puente de §A.1,
lleva exactamente los hijos de la raíz de `sigma` a los de `pi`. En
particular conserva sus tamaños y el poset inducido en cada hijo.

Entre dos bloques distintos, los intervalos de posiciones están totalmente
ordenados y los intervalos de valores también; por ello todos los pares
cruzados tienen la misma relación de comparabilidad y la contracción orientada
está bien definida. Contraer esos hijos da posets cociente isomorfos. Escribamos

\[
\pi=\alpha[\tau_1,\ldots,\tau_m],
\qquad
\sigma=\beta[\upsilon_1,\ldots,\upsilon_m],
\]

con los bloques ordenados por posiciones. El inversion graph de `alpha` es
primo. El Teorema 3, aplicado al isomorfismo orientado entre los cocientes,
implica

\[
\beta\in\{\alpha,\alpha^{-1}\}.
\]

Este paso ya incluye cualquier automorfismo del cociente: el Teorema 3 parte de
un isomorfismo arbitrario y normaliza después ambos órdenes por rangos.

Si `beta=alpha`, esa normalización identifica el bloque de rango de posición
`s` con `B_s`. Un singleton no tiene libertad. En tamaño dos, preservar el
poset inducido obliga a `upsilon_s=12` cuando `tau_s=12`, y a
`upsilon_s=21` cuando `tau_s=21`: cadena y anticadena no son isomorfas. Luego
`sigma=pi`.

Si `beta=alpha^{-1}`, el bloque de rango de posición `t` corresponde al bloque
original `s=alpha^{-1}(t)`, y la inversión global invierte también el patrón
interno. La fórmula exacta de inversión de una inflación es

\[
\pi^{-1}
=\alpha^{-1}
 [\tau_{\alpha^{-1}(1)}^{-1},\ldots,
  \tau_{\alpha^{-1}(m)}^{-1}].
\]

Todos los patrones permitidos, `1`, `12` y `21`, son involuciones. La
preservación del poset inducido fuerza por tanto esos mismos patrones en los
bloques correspondientes y da `sigma=pi^{-1}`. La inclusión inversa ya fue
probada en §6.3. ∎

La expresión «flips de twins» puede referirse a permutar los dos vértices de un
módulo anticadena como automorfismo del poset no etiquetado. Tras renormalizar
los rangos de los dos órdenes, ese automorfismo sigue dando el mismo patrón
numérico `21`, no una nueva permutación. Si por *flip* se entiende cambiar
`12` por `21` o viceversa, se cambia cadena por anticadena y se sale de la
fibra. Ésta es la falsación exacta de la parametrización tentativa como cubo
no trivial de elecciones internas.

### A.3 Auditoría de automorfismos y normalización

Las ocho fuentes de posible libertad quedan resueltas así:

1. **Automorfismos del cociente primo.** Están incluidos en el isomorfismo
   arbitrario al que se aplica el Teorema 3; tras normalizar rangos sólo dejan
   `alpha` o `alpha^{-1}`.
2. **Permutación de módulos isomorfos.** Un automorfismo puede permutarlos sólo
   si induce un automorfismo del cociente. No crea una tercera permutación por
   el punto anterior; los tamaños y tipos internos viajan con el módulo.
3. **Dualidad.** No interviene: `[P_sigma]=[P_pi]` exige preservar la
   orientación. Las transformaciones `r pi r` y `r pi^{-1}r` representan en
   general el dual, como se auditó en §6.3.
4. **Inversión global.** Intercambia los dos órdenes del mismo realizador del
   poset y produce exactamente `pi^{-1}`.
5. **Orientación de cada twin.** No es libre: `12` es cadena y `21` es
   anticadena.
6. **Twin creciente/decreciente.** Ambos están permitidos en `A_N`, pero su
   tipo es un invariante del poset inducido y debe preservarse.
7. **Tamaños de bloque.** Son cardinalidades de módulos fuertes canónicos; un
   isomorfismo los conserva.
8. **Normalización por rangos.** Convierte cualquier par de órdenes sobre un
   conjunto abstracto en una única permutación numérica. Los automorfismos
   internos que sólo cambian nombres desaparecen en esta normalización.

### A.4 Falsificador exhaustivo finito

Se ejecutó un falsificador independiente para todas las permutaciones hasta
`N=9`. Para cada `pi` enumeró todos sus intervalos comunes, seleccionó los
fuertes mediante el criterio de no solapamiento, obtuvo los hijos maximales de
la raíz, construyó su cociente y comprobó literalmente la primalidad de su
inversion graph por enumeración de módulos. Retuvo exactamente los casos con
raíz prima y bloques de tamaños uno o dos. La clase de poset se canonizó con la
matriz de relación estricta y enumeración exacta de las reetiquetaciones que
quedaban tras refinamiento de colores. Finalmente se comparó cada fibra
completa con `{pi,pi^{-1}}`.

No se perdió ningún miembro al filtrar por `A_N`: la propiedad se expresa en
el árbol modular canónico del inversion graph y, por tanto, es invariante bajo
isomorfismos de posets.

Los resultados fueron:

| `N` | permutaciones en `A_N` | clases | `k` twins: permutaciones | `k` twins: clases | tamaños de fibra | violaciones |
|---:|---:|---:|:---|:---|:---|---:|
| 1 | 0 | 0 | — | — | — | 0 |
| 2 | 0 | 0 | — | — | — | 0 |
| 3 | 0 | 0 | — | — | — | 0 |
| 4 | 2 | 1 | `0:2` | `0:1` | `2:1` | 0 |
| 5 | 22 | 12 | `0:6, 1:16` | `0:4, 1:8` | `1:2, 2:10` | 0 |
| 6 | 154 | 81 | `0:46, 1:60, 2:48` | `0:25, 1:32, 2:24` | `1:8, 2:73` | 0 |
| 7 | 1194 | 612 | `0:338, 1:552, 2:240, 3:64` | `0:174, 1:282, 2:124, 3:32` | `1:30, 2:582` | 0 |
| 8 | 10930 | 5518 | `0:2926, 1:4732, 2:2760, 3:480, 4:32` | `0:1481, 1:2378, 2:1395, 3:248, 4:16` | `1:106, 2:5412` | 0 |
| 9 | 111194 | 55779 | `0:28146, 1:46816, 2:28392, 3:7360, 4:480` | `0:14136, 1:23464, 2:14231, 3:3704, 4:244` | `1:364, 2:55415` | 0 |

En las `62003` clases acumuladas para `4<=N<=9`, no apareció libertad sin
explicar. Las fibras singleton corresponden a `pi=pi^{-1}` y las restantes
tienen tamaño dos. La enumeración falsó activamente la hipótesis de flips
internos como nuevas permutaciones de la fibra y concuerda con el Teorema 4,
pero no se usa en su demostración.

El primer test no trivial de un flip aparece en `N=5`:

\[
\pi=23514=2413[12,1,1,1],
\qquad
\widetilde\pi=32514=2413[21,1,1,1].
\]

El bloque ocupa las posiciones `1,2` y los valores `2,3`. En `P_pi` sus dos
elementos son comparables y en `P_tildepi` son incomparables; todas sus
relaciones exteriores coinciden. En particular, el número total de pares
comparables difiere en uno, de modo que los posets no son isomorfos. Éste es el
contraejemplo mínimo a interpretar el flip local como libertad de la fibra; no
es un contraejemplo al Teorema 4.

### A.5 Cambio exacto de score en un twin

Aunque el cambio de orientación interna no permanece en la misma fibra, su
coste algebraico es exacto. Para ventanas

\[
I=\{i,i+1\},\qquad J=\{j,j+1\},
\]

se tiene

\[
X_{12}=a_i a_j+a_{i+1}a_{j+1},
\qquad
X_{21}=a_i a_{j+1}+a_{i+1}a_j,
\]

y, con la convención «nuevo menos antiguo» para el flip `12 -> 21`,

\[
\boxed{
X_{21}-X_{12}
=(a_i-a_{i+1})(a_{j+1}-a_j)
=-(a_i-a_{i+1})(a_j-a_{j+1}).
}
\]

El flip inverso cambia el signo.

### A.6 Cota con `k` twins y perfil de pendiente acotada

Supongamos

\[
D_N:=\max_{1\le i<N}|a_{i+1}-a_i|.
\]

La identidad anterior da para cada cambio interno contrafactual

\[
|X_{21}-X_{12}|\le D_N^2.
\]

Por el camino de Hamming entre dos configuraciones de un cubo artificial de
`k` flips independientes,

\[
\operatorname{osc}X_N\le kD_N^2.
\]

La constante es exactamente `1` por la desigualdad triangular. Esta cota es
útil como identidad algebraica, pero no debe confundirse con la fibra del
poset: por el Teorema 4 esos flips no son elecciones dentro de ella. En la
fibra real se obtiene la cota estrictamente más fuerte

\[
\boxed{
\operatorname{osc}_{\mathcal F_N([P_\pi])}X_N=0.
}
\]

### A.7 Pendiente discreta del perfil sinusoidal

Para el perfil congelado

\[
a_{i,N}=\mathbb E[\sin(2\pi U_{(i)})],
\]

acoplamos `U_(i)` y `U_(i+1)` en la misma muestra uniforme. Como `sin(2 pi u)`
es `2 pi`-Lipschitz y
`E[U_(i+1)-U_(i)]=(i+1)/(N+1)-i/(N+1)=1/(N+1)`,

\[
\begin{aligned}
|a_{i+1,N}-a_{i,N}|
&\le
\mathbb E|\sin(2\pi U_{(i+1)})-\sin(2\pi U_{(i)})|\\
&\le 2\pi\,\mathbb E[U_{(i+1)}-U_{(i)}]
=\frac{2\pi}{N+1}.
\end{aligned}
\]

Por tanto,

\[
\boxed{D_N\le\frac{2\pi}{N+1}.}
\]

En el cubo contrafactual, un flip costaría a lo sumo
`4 pi^2/(N+1)^2` y `k` flips tendrían oscilación a lo sumo
`4 pi^2 k/(N+1)^2`. Sobre la fibra orientada real, la oscilación sigue siendo
exactamente cero.

### A.8 Varianza condicional y veredicto

Por Popoviciu, cualquier variable soportada en un intervalo de longitud `R`
tiene varianza a lo sumo `R^2/4`. El cubo contrafactual satisfaría así

\[
\operatorname{Var}(X_N)\le \frac{k^2D_N^4}{4}
\le \frac{4\pi^4k^2}{(N+1)^4}
\]

para el perfil sinusoidal. De nuevo, ésta no es la descripción de la fibra. El
resultado exacto para el canal observado es, para cualquier perfil real,

\[
\boxed{
A_N(\pi)
\quad\Longrightarrow\quad
\operatorname{Var}\!\left(
X_N(\Pi_N)\mid[P_{\Pi_N}]=[P_\pi]
\right)=0.
}
\]

No queda obligación estructural o analítica dentro de la clase determinista
`A_N`. Este apéndice, por sí solo, no usa la probabilidad de `A_N` ni controla
el evento excepcional; esas entradas y las conclusiones `L_N=o(N)` y
`q_N -> 1` quedan demostradas separadamente en §7.

```text
TYPICAL_FIBER_VERDICT = PROVED
EXACT_TYPICAL_FIBER = {pi, pi^{-1}}
INDEPENDENT_TWIN_FLIPS_IN_ORIENTED_FIBER = REFUTED
TYPICAL_PRIME_ROOT_TWIN_ZERO_LOSS = PROVED
ASYMPTOTIC_POSET_EFFICIENCY = CLOSED_IN_SECTION_7_FOR_BOUNDED_SEPARABLE_SCORES
```
