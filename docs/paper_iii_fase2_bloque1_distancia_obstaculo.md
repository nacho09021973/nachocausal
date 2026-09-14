# Paper III — Fase 2, bloque 1: distancia de obstáculo y orden causal

Fecha: 2026-09-11.

```text
DOCUMENT_ID=PAPER_III_PHASE_2_BLOCK_1_OBSTACLE_METRIC
SCOPE=CONTINUUM_DERIVATION_METRIC_AXIOMS_CAUSAL_TRANSITIVITY
BLOCK_1=PROOFS_WRITTEN
DOMAIN=CLOSED_EXTERIOR_OF_OPEN_SPATIAL_BALL
INDEPENDENT_REVIEW=NOT_PERFORMED
GATE_2=NOT_EVALUATED
NUMERICAL_VERIFIER=NOT_STARTED
SIMULATIONS=NONE
INTRINSIC_POSET_RECONSTRUCTION=NOT_CLAIMED
HORIZON_CLAIM=NONE
```

Este documento desarrolla los tres entregables matemáticos del
[bloque 1 de la hoja de ruta]\(hoja_de_ruta_paper_iii.md#fase-2--bloque-1-y-sólo-el-bloque-1\).
La derivación es autocontenida. No utiliza ajustes, datos de sprinkling ni
resultados numéricos. El estado anterior `NOT_STARTED` de la hoja de ruta
describe el punto de entrada del 2026-09-10; este documento registra el trabajo
matemático posterior, sin adjudicar la puerta de salida de la Fase 2.

## 1. Dominio, frontera y significado de la distancia

Fijamos un centro espacial \(o\in\mathbb R^3\) y un radio \(a>0\). Se excinde
la **bola abierta** y se conserva su esfera:

\[
X_a=\{x\in\mathbb R^3:|x-o|\ge a\}.
\]

Esta convención permite curvas sobre la frontera. Es parte del modelo, no una
elección numérica. La expresión previa «bola excindida» no fijaba si la esfera
se conservaba; la distinción es necesaria para que el mínimo se alcance y la
condición causal con igualdad tenga el significado de existencia de curva.
El exterior abierto se trata por separado en §7.

Para \(x,y\in X_a\), sea \(\Gamma_a(x,y)\) el conjunto de curvas absolutamente
continuas \(\gamma:[0,1]\to X_a\) que unen \(x\) e \(y\). Definimos

\[
\ell(\gamma)=\int_0^1|\dot\gamma(v)|\,dv,
\qquad
d_a(x,y):=\inf_{\gamma\in\Gamma_a(x,y)}\ell(\gamma).
\tag{1}
\]

Toda curva rectificable continua admite una parametrización Lipschitz con la
misma longitud, de modo que esta clase incluye los caminos rectificables
pertinentes. Es no vacía: se puede ir radialmente de cada extremo a una esfera
de radio \(R\ge\max(|x-o|,|y-o|)\) y unir allí las direcciones por un arco.
Por tanto \(d_a\) es finita. Escribiremos \(d_{\rm obs}=d_a\).

La estructura admitida aquí es la geometría euclídea espacial y la bola
estática prescrita. Cambiar de coordenadas por una isometría que transporte
también \(o\) conserva (1). **Esto no constituye una reconstrucción desde un
poset finito:** \(d_a\) define la causalidad del modelo generador.

## 2. Fórmula exacta y criterio de visibilidad

Pongamos

\[
r=|x-o|,\quad s=|y-o|,\quad
\theta=\arccos\!\frac{(x-o)\cdot(y-o)}{rs}\in[0,\pi],
\]
\[
\alpha=\arccos(a/r),\qquad \beta=\arccos(a/s).
\]

Como \(r,s\ge a>0\), todas estas expresiones están definidas, incluso sobre
la esfera. El resultado es

\[
\boxed{
d_a(x,y)=
\begin{cases}
\sqrt{r^2+s^2-2rs\cos\theta},
  &\theta\le\alpha+\beta,\\[2mm]
\sqrt{r^2-a^2}+\sqrt{s^2-a^2}
  +a(\theta-\alpha-\beta),
  &\theta>\alpha+\beta.
\end{cases}}
\tag{2}
\]

El primer caso es exactamente aquel en que el segmento \([x,y]\) permanece
en \(X_a\). La igualdad incluye el contacto tangente con la esfera.

**Prueba del criterio.** Si \(x=y\), es inmediato. Para \(x\ne y\), trasladamos
\(o\) al origen y consideramos el punto del segmento más próximo al origen.
Si es un extremo, por ejemplo \(x\), entonces

\[
x\cdot(y-x)\ge0,
\quad s\cos\theta\ge r,
\quad \theta\le\arccos(r/s)\le\arccos(a/s)\le\alpha+\beta.
\]

Además todo el segmento queda fuera de la bola abierta. El caso del extremo
\(y\) es simétrico.

Si el pie de la perpendicular está en el interior del segmento y su distancia
al origen es \(h>0\), los dos triángulos rectángulos dan

\[
\theta=\arccos(h/r)+\arccos(h/s).
\]

El miembro derecho es estrictamente decreciente en \(h\). En consecuencia,
\(h\ge a\) equivale a \(\theta\le\alpha+\beta\). Si \(h=0\), los extremos
están en direcciones opuestas, \(\theta=\pi>\alpha+\beta\), y el segmento
atraviesa la bola. Esto agota los casos. ∎

Si el segmento es admisible, toda curva entre sus extremos satisface
\(\ell(\gamma)\ge|x-y|\), y el segmento alcanza esa cota. Queda probado el
primer renglón de (2).

## 3. Caso obstruido: construcción que alcanza la fórmula

Supongamos \(\theta>\alpha+\beta\). Elegimos un plano por \(o,x,y\). Cuando
las direcciones son opuestas hay múltiples planos posibles; cualquiera sirve.
En ese plano tomamos el arco angular menor entre las direcciones de los
extremos, de amplitud \(\theta\), y parametrizamos sus direcciones mediante
un vector unitario \(u(\varphi)\), \(0\le\varphi\le\theta\).

Los puntos de contacto son

\[
b_x=o+a\,u(\alpha),\qquad
b_y=o+a\,u(\theta-\beta).
\]

El camino propuesto concatena \([x,b_x]\), el arco esférico de \(b_x\) a
\(b_y\), y \([b_y,y]\). En efecto,

\[
(x-b_x)\cdot(b_x-o)=ar\cos\alpha-a^2=0,
\]

y análogamente en \(b_y\). Los segmentos son tangentes, permanecen en \(X_a\)
y tienen longitudes \(\sqrt{r^2-a^2}\) y \(\sqrt{s^2-a^2}\). El arco tiene
longitud \(a(\theta-\alpha-\beta)>0\). Así se alcanza el segundo renglón
de (2) como cota superior. Si un extremo está en la esfera, su segmento
tangente tiene longitud cero y se omite.

Falta demostrar que ninguna curva espacial, ni siquiera una no plana, es más
corta. Esa es la función de la siguiente cota inferior.

## 4. Cota inferior para toda curva en tres dimensiones

Sea \(\gamma\in\Gamma_a(x,y)\). Escribamos

\[
\gamma(v)-o=R(v)U(v),\quad |U(v)|=1,\quad
m=\min_{v\in[0,1]}R(v)\ge a.
\]

La continuidad garantiza el mínimo; \(m\le\min(r,s)\). Como \(R\ge a>0\),
\(R\) y \(U\) son absolutamente continuas, y casi en todo punto

\[
|\dot\gamma|^2=\dot R^2+R^2|\dot U|^2.
\]

Aplicando Cauchy–Schwarz con el vector unitario
\((\sqrt{1-m^2/R^2},m/R)\), obtenemos

\[
|\dot\gamma|
\ge \sqrt{1-m^2/R^2}\,|\dot R|+m|\dot U|.
\tag{3}
\]

La longitud angular de \(U\) es al menos \(\theta\). Para justificarlo sin
suponer que \(U\) sea un arco máximo, fijemos \(e=U(0)\),
\(z(v)=e\cdot U(v)\) y \(f_\delta(v)=\arccos((1-\delta)z(v))\),
\(0<\delta<1\). Como \(U\cdot\dot U=0\),
\(|\dot z|\le\sqrt{1-z^2}|\dot U|\); por ello

\[
|\dot f_\delta|
\le\frac{(1-\delta)\sqrt{1-z^2}}
{\sqrt{1-(1-\delta)^2z^2}}|\dot U|
\le|\dot U|.
\]

Integrando y haciendo \(\delta\downarrow0\), resulta
\(\theta\le\int_0^1|\dot U|\,dv\), incluidos extremos antipodales.

Definamos, para \(z\ge m\),

\[
H_m(z)=\sqrt{z^2-m^2}-m\arccos(m/z).
\]

Esta función es \(C^1\) por la derecha en \(m\), con
\(H_m(m)=0\) y \(H'_m(z)=\sqrt{1-m^2/z^2}\ge0\). Dividiendo la integral
radial en un punto donde \(R=m\), la variación total da

\[
\int_0^1H'_m(R)|\dot R|\,dv
\ge H_m(r)+H_m(s).
\]

Por (3), cualquier curva satisface

\[
\ell(\gamma)\ge G(m):=
\sqrt{r^2-m^2}+\sqrt{s^2-m^2}
+m\bigl[\theta-\arccos(m/r)-\arccos(m/s)\bigr].
\tag{4}
\]

Para \(a<m<\min(r,s)\), la derivación explícita y cancelación de términos da

\[
G'(m)=\theta-\arccos(m/r)-\arccos(m/s).
\]

En el caso obstruido,

\[
G'(m)\ge\theta-\alpha-\beta>0.
\]

La continuidad de \(G\) extiende la monotonía a los extremos del intervalo.
Así \(G(m)\ge G(a)\). Si \(\min(r,s)=a\), necesariamente \(m=a\), y la
conclusión es directa. El valor \(G(a)\) es precisamente el segundo renglón
de (2). La construcción de §3 lo alcanza, de modo que (2) queda probada
para **todas** las curvas admisibles. No se ha supuesto planitud ni unicidad
del minimizador. ∎

## 5. Axiomas métricos

La definición (1) y la prueba de (2) permiten verificar los cuatro axiomas sin
una comprobación por casos de la fórmula cerrada.

1. **Finitud y no negatividad.** Hay caminos de longitud finita \(§1 o §3\), y
   toda longitud es no negativa: \(0\le d_a(x,y)<\infty\).
2. **Identidad de los indiscernibles.** La curva constante prueba
   \(d_a(x,x)=0\). Para cualquier curva entre \(x\) e \(y\),
   \(\ell(\gamma)\ge|x-y|\); luego \(d_a(x,y)\ge|x-y|\). Si
   \(d_a(x,y)=0\), entonces \(x=y\).
3. **Simetría.** Invertir la parametrización establece una correspondencia
   entre \(\Gamma_a(x,y)\) y \(\Gamma_a(y,x)\) que conserva longitudes.
   Por tanto \(d_a(x,y)=d_a(y,x)\).
4. **Desigualdad triangular.** Dados \(x,y,z\in X_a\) y \(\varepsilon>0\),
   elegimos caminos \(x\to y\) e \(y\to z\) con longitudes menores que
   \(d_a(x,y)+\varepsilon/2\) y \(d_a(y,z)+\varepsilon/2\). Su concatenación,
   reparametrizada en \([0,1]\), pertenece a \(\Gamma_a(x,z)\). Por ello
   \(d_a(x,z)\le d_a(x,y)+d_a(y,z)+\varepsilon\). Al tomar
   \(\varepsilon\downarrow0\), resulta la desigualdad triangular.

Por tanto **\(d_a\) es una métrica genuina en \(X_a\)**. Además es geodésica:
para todo par existe un camino que alcanza la distancia, por §§2–4.

## 6. Tangencias y degeneraciones

| Caso | Valor y tratamiento |
|---|---|
| \(x=y\) | \(\theta=0\), rama visible, \(d_a=0\); se usa la curva constante. |
| Misma dirección, \(\theta=0\) | Segmento radial exterior; \(d_a=\lvert r-s\rvert\). |
| Tangencia, \(\theta=\alpha+\beta\) | El arco tiene longitud cero. Los dos segmentos tangentes forman el segmento recto admisible. Ambas ramas dan \(\sqrt{r^2-a^2}+\sqrt{s^2-a^2}=\lvert x-y\rvert\). |
| Un extremo en la esfera, por ejemplo \(r=a\) | \(\alpha=0\); si \(\theta\le\beta\), segmento visible; si \(\theta>\beta\), \(d_a=\sqrt{s^2-a^2}+a(\theta-\beta)\). |
| Ambos extremos en la esfera | \(\alpha=\beta=0\), y \(d_a=a\theta\), también cuando \(\theta=0\). |
| Direcciones opuestas, \(\theta=\pi\) | Rama obstruida. Los planos posibles dan caminos de la misma longitud; no se requiere unicidad. |
| Mínimo radial igual a \(a\) o a un radio de extremo | (4) sigue definida; la monotonía se extiende por continuidad, sin dividir por \(\sqrt{r^2-m^2}\) en ese extremo. |
| Radio de obstáculo cero | Es una extensión separada: \(X_0=\mathbb R^3\), \(d_0(x,y)=\lvert x-y\rvert\). No se evalúan ángulos con un extremo en \(o\). |

En la tangencia, la identidad entre ambas ramas también se obtiene de

\[
\cos(\alpha+\beta)
=\frac{a^2-\sqrt{r^2-a^2}\sqrt{s^2-a^2}}{rs}.
\]

La fórmula es continua al pasar entre las ramas y al llevar uno o ambos
extremos a la esfera. Para extremos fijos distintos de \(o\), al tomar
\(a\downarrow0\) se recupera la distancia euclídea: la rama visible ya la da;
en direcciones opuestas la rama obstruida tiende a \(r+s=|x-y|\).

## 7. Qué cambia si se excluye también la esfera

Sea \(X_a^\circ=\{x:|x-o|>a\}\), con extremos en ese dominio, y definamos la
distancia como el ínfimo de longitudes de curvas contenidas en él. Su valor es
la restricción de (2), pero el mínimo puede no alcanzarse.

**Prueba de la igualdad de ínfimos.** La inclusión de clases de curvas da
\(d_{X_a^\circ}\ge d_a\). Para la desigualdad inversa, tomemos un minimizador
en \(X_a\), dilatémoslo por \(1+\varepsilon\) respecto a \(o\), y añadamos
segmentos radiales desde los extremos originales a los dilatados. Todo el
camino está en \(X_a^\circ\), y su longitud es

\[
(1+\varepsilon)d_a(x,y)+\varepsilon(r+s)\longrightarrow d_a(x,y).
\]

Si el segmento recto está estrictamente fuera de la esfera, sigue alcanzando
el mínimo. Si es tangente, la igualdad con la distancia euclídea obligaría a
recorrer ese segmento, que contiene un punto excluido. Si está obstruido,
cualquier curva en el exterior abierto tiene mínimo radial \(m>a\), y (4)
da \(\ell(\gamma)\ge G(m)>G(a)=d_a(x,y)\). En estos dos últimos casos no
existe minimizador.

En consecuencia, para tangencias u obstrucciones en el exterior abierto,
el tiempo de viaje \(d_a(x,y)\) es un **ínfimo no alcanzado**. La condición
\(\Delta t\ge d_a\) sigue definiendo un orden abstracto, pero no coincide
con existencia de curva causal en ese dominio cuando hay igualdad. La
convención de exterior cerrado de §1 evita esta discrepancia.

## 8. Orden causal inducido y transitividad

Trabajamos en \(M_a=\mathbb R\times X_a\), con velocidad de la luz igual a
uno. Una curva futura admisible \(v\mapsto(t(v),x(v))\) es absolutamente
continua, permanece en \(M_a\) y satisface

\[
\dot t(v)\ge|\dot x(v)|\quad\text{casi en todo punto}.
\tag{5}
\]

Se permite recorrer la frontera. Allí la métrica inducida es
\(-dt^2+a^2d\Omega^2\), de firma lorentziana: la frontera es **timelike**.
Las curvas admisibles no tienen que ser geodésicas del Minkowski ambiente;
en particular, el arco de §3 pertenece a la causalidad del dominio con frontera.

Para eventos \(p=(t_p,x_p)\) y \(q=(t_q,x_q)\), definimos

\[
p\preceq_a q\quad\Longleftrightarrow\quad
t_q-t_p\ge d_a(x_p,x_q).
\tag{6}
\]

**Equivalencia con existencia de curva.** Integrando (5), cualquier curva
causal entre \(p\) y \(q\) da

\[
t_q-t_p\ge\ell(x)\ge d_a(x_p,x_q).
\]

Recíprocamente, si \(\Delta t\ge d_a(x_p,x_q)=d>0\), parametrizamos el
minimizador espacial de §§2–4 a velocidad constante \(d/\Delta t\le1\)
durante el intervalo temporal disponible. Esto produce una curva que cumple
(5), incluso si \(\Delta t=d\). Si \(d=0\), los extremos espaciales coinciden
y basta la curva vertical, constante cuando también \(\Delta t=0\). ∎

**Reflexividad.** \(d_a(x_p,x_p)=0\), luego \(p\preceq_a p\).

**Antisimetría.** Si \(p\preceq_a q\) y \(q\preceq_a p\), la simetría de la
métrica implica \(0\ge2d_a(x_p,x_q)\ge0\). Por identidad de indiscernibles,
\(x_p=x_q\); las dos desigualdades temporales fuerzan \(t_p=t_q\). Así \(p=q\).

**Transitividad.** Si \(p\preceq_a q\preceq_a w\), entonces

\[
\begin{aligned}
t_w-t_p
&=(t_w-t_q)+(t_q-t_p)\\
&\ge d_a(x_q,x_w)+d_a(x_p,x_q)\\
&\ge d_a(x_p,x_w).
\end{aligned}
\]

Por (6), \(p\preceq_a w\). La prueba incluye relaciones saturadas, tangencias,
extremos sobre la frontera y eventos con igual posición espacial. ∎

Por tanto \(\preceq_a\) es un **orden parcial**. Su versión estricta es

\[
p\prec_a q\quad\Longleftrightarrow\quad
p\ne q\ \text{y}\ t_q-t_p\ge d_a(x_p,x_q).
\tag{7}
\]

Es irreflexiva y transitiva: si \(p\prec_a q\prec_a w\), (6) da
\(p\preceq_a w\); \(p=w\) contradiría la antisimetría aplicada a \(p,q\).
Además \(p\prec_a q\) implica \(t_q>t_p\). La notación previa con
`p ≺ q iff Δt ≥ d_obs` necesitaba excluir \(p=q\) para ser estricta.
No debe sustituirse por `Δt > d_obs`, porque eso eliminaría las relaciones
causales saturadas entre eventos distintos.

La restricción de este orden a cualquier conjunto finito de eventos distintos
es un poset. Esta es una consecuencia combinatoria exacta; no es una prueba
de convergencia de observables discretos. El dominio usado para decidir la
relación sigue siendo \(M_a\): restringir los eventos observados no equivale
a imponer nuevas paredes a las curvas causales.

## 9. Resultado y límite del bloque

Quedan demostrados, para \(a>0\) y el exterior cerrado especificado:

1. la fórmula (2), con un camino minimizador y una cota inferior para cualquier
   curva tridimensional;
2. los axiomas métricos, incluidos tangencias y casos degenerados;
3. la equivalencia de (6) con causalidad por curvas y los axiomas del orden
   parcial, junto con su versión estricta (7).

Son pruebas matemáticas escritas en este documento, no una formalización en
Lean ni una revisión independiente. No se ha construido el verificador
numérico, elegido una región observada, definido controles emparejados ni
ejecutado sprinklings. Tampoco se ha definido un estimador espacial a partir
del poset. La puerta `GATE_2`, que exige además esos controles del modelo y del
muestreo, no se evalúa con este bloque.
