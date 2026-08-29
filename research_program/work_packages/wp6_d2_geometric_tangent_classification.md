# WP6 — Primer puente de tangente geométrico a score de rangos

```text
ESTADO: GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
ALCANCE: d=2, diamante plano de Minkowski en coordenadas nulas,
         sector rank-one simétrico. No es reconstrucción. No es horizonte.
NATURALEZA: deductivo. Cero semillas, cero simulación, cero ejecución, sello intacto.
GOBERNANZA: docs/program_reopening_note_2026-08-28_R4.md (firmada 2026-08-28)
FECHA: 2026-08-28
SELLO: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4 intacto
SEMILLAS: banda virgen [2,000,000–2,999,999] sin quemar
GATE_AUDIT: comite 051 — T1-T19 en 0e3a997; G1 en b0694dc; G2 en 0290d99
OBLIGACION_EXACTA: SATISFIED_IN_HISTORY
NO_HORIZON_CLAIM
MINKOWSKI_DIAMOND_PERTURBATIVE
S2_NOT_OPENED
```

## 0. Estado y alcance de la fase S1

Este documento cubre la fase S1 completa de
`GEOMETRIC_TANGENT_CLASSIFICATION`. Determina el mapa diferencial exacto

```text
generador conforme psi
  -> tangente logarítmico de la densidad normalizada t_psi
  -> tangente de cópula h_psi
  -> score S_{N,psi} de la permutación de rangos,
```

audita el factor `2` de la subclase rank-one simétrica (§§1–8), clasifica
exactamente las `psi` cuya proyección de interacción es rank-one simétrica
(§9), verifica el factor por una diferenciación independiente en forma cerrada
(§10) y prueba sin simulación las tres hipótesis del teorema congelado para los
perfiles `a_{i,N}=E[f(U_{(i)})]` (§11).

No abre scores bilineales genéricos ni finite-rank, no promueve el sector
asimétrico `f tensor g`, no prueba el teorema geométrico asintótico y no abre
la fase S2.

Se reutilizan sin redemostrarlos:

1. el condicionamiento a cardinalidad fija y el PIT que preserva el orden de
   `wp6_d2_null_copula_dichotomy.md`, §§1–2;
2. la derivada implícita de cuantiles y el score a rangos fijos de
   `wp4_ibar_direct_score_derivation.md`, §§5–6;
3. el teorema combinatorio para scores
   `2 sum_i a_{i,N}a_{pi(i),N}` de
   `wp6_d2_modular_fiber_score.md`, §7.

```text
GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
S2_NOT_OPENED
S1_GEOMETRIC_TO_COPULA_BRIDGE = PROVED
ROADMAP_NORMALIZATION_MISMATCH = CONFIRMED
SYMMETRIC_RANK_ONE_SECTOR_ONLY
NO_HORIZON_CLAIM
MINKOWSKI_DIAMOND_PERTURBATIVE
NO_UNIVERSALITY_CLAIM
```

Los teoremas internos (Teorema 6, Teorema 7, Lema 9.2, Proposición 9.4) se
afirman probados en su propio enunciado. El marcador de fase es `PROVED`
porque G1, la prueba S1 y G2 ya están en historia (`b0694dc`, `0e3a997`,
`0290d99`). S2 no se abre.

## 1. Experimento exacto y cuatro objetos distintos

### 1.1 Dominio, métrica y medida de referencia

Un diamante causal de Minkowski en `1+1` es una caja en coordenadas nulas.
Como en `wp6_d2_null_copula_dichotomy.md`, aplicamos una reparametrización
creciente separada de las dos coordenadas y trabajamos en

\[
D=[0,1]^2,
\qquad
(u,v)\preceq(u',v')\Longleftrightarrow u\le u',\ v\le v'.
\]

La reparametrización preserva el orden punto a punto. Elegimos las coordenadas
de referencia de modo que la medida de volumen **normalizada** de la métrica
plana `g_0` sea

\[
\mu_0(du\,dv)=du\,dv.
\]

Si `V_0=vol_{g_0}(D)`, esto significa
`mu_0=dvol_{g_0}/V_0`; no requiere fijar el factor convencional que se escriba
delante de `du dv` en la métrica nula.

Sea `psi in C(D;R)`. La continuidad sobre el compacto es la hipótesis mínima
conveniente usada aquí: garantiza acotación, diferenciación dominada uniforme,
marginales positivas para `epsilon` pequeño y expansiones puntuales de los
cuantiles. Para el tangente de densidad en `L^1` bastaría `psi in L^infty`,
pero no necesitamos esa extensión. Regularidad geométrica adicional para
definir curvatura no interviene en este subpaso.

Definimos

\[
Z(\varepsilon)
:=\int_D e^{2\varepsilon\psi(u,v)}\,d\mu_0(u,v),
\qquad
g_\varepsilon
:=\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}g_0.
\tag{1.1}
\]

Así `Z(0)=mu_0(D)=1`. En dimensión dos, si `m>0`, entonces

\[
dvol_{m g_0}=m\,dvol_{g_0},
\]

porque el determinante de la matriz métrica se multiplica por `m^2` y su raíz
absoluta por `m`. Por tanto (1.1) conserva exactamente el volumen total:

\[
dvol_{g_\varepsilon}
=\frac{e^{2\varepsilon\psi}}{Z(\varepsilon)}dvol_{g_0},
\qquad
vol_{g_\varepsilon}(D)=V_0.
\]

Un sprinkling de Poisson condicionado a `N` puntos consiste, por el lema de
condicionamiento ya registrado, en `N` puntos iid con ley de volumen
normalizada

\[
\mu_\varepsilon(du\,dv)
=q_\varepsilon(u,v)\,du\,dv,
\qquad
q_\varepsilon(u,v)
=\frac{e^{2\varepsilon\psi(u,v)}}{Z(\varepsilon)}.
\tag{1.2}
\]

Como `Z(\varepsilon)>0` para todo `varepsilon` y el numerador es una
exponencial, `q_\varepsilon>0` **para todo** `varepsilon`, no sólo cerca
del nulo. El PIT es por tanto estrictamente creciente a cada `varepsilon`,
y la invariancia de rangos de §5.1 compara leyes al mismo `varepsilon`.

Todo lo que sigue deriva respecto de `epsilon` en `epsilon=0`, manteniendo
fijos el dominio, `g_0`, `psi` y `N`. La derivada es puntual y uniforme bajo la
hipótesis anterior y, por tanto, también vale en `L^1(mu_0)`.

### 1.2 Notación que separa los cuatro niveles

Usaremos letras distintas:

- `psi`: generador de la perturbación **geométrica** en la métrica;
- `dot g_0`: tangente de la métrica normalizada;
- `t_psi`: tangente logarítmico de la **densidad conjunta normalizada**;
- `h_psi`: tangente de la **densidad de cópula** tras uniformizar ambas
  marginales;
- `S_{N,psi}(pi)`: score del likelihood discreto de la **permutación de
  rangos**.

Como la densidad conjunta y la densidad de cópula valen `1` en el nulo, sus
tangentes de densidad y sus tangentes logarítmicos coinciden allí. Esto no
identifica los objetos: `t_psi` y `h_psi` difieren por los dos términos
marginales calculados abajo.

La tangente métrica propiamente dicha se obtiene ya de (1.1):

\[
\dot g_0
:=\left.\partial_\varepsilon g_\varepsilon\right|_0
=2(\psi-\bar\psi)g_0.
\tag{1.3}
\]

Por tanto `psi` es el generador conforme elegido, mientras que `dot g_0` es
la variación geométrica de la familia normalizada. Una constante añadida a
`psi` no cambia (1.1), como refleja el centrado de (1.3).

## 2. Tangente de la densidad normalizada

Definimos la media respecto de la medida de referencia:

\[
\bar\psi
:=\int_0^1\int_0^1\psi(u,v)\,du\,dv.
\tag{2.1}
\]

Por diferenciación dominada,

\[
Z'(0)=\int_D2\psi\,d\mu_0=2\bar\psi.
\]

Tomando logaritmos en (1.2),

\[
\log q_\varepsilon(u,v)
=2\varepsilon\psi(u,v)-\log Z(\varepsilon),
\]

y en consecuencia

\[
\boxed{
t_\psi(u,v)
:=\left.\partial_\varepsilon\log q_\varepsilon(u,v)
\right|_{\varepsilon=0}
=2[\psi(u,v)-\bar\psi].
}
\tag{2.2}
\]

Equivalentemente,

\[
q_\varepsilon=1+\varepsilon t_\psi+o(\varepsilon)
\]

uniformemente, y `int_D t_psi=0`, como exige la normalización.

## 3. Tangente de cópula y movimiento de las marginales

### 3.1 Marginales y sus cuantiles

Definimos

\[
\psi_U(u):=\int_0^1\psi(u,v)\,dv,
\qquad
\psi_V(v):=\int_0^1\psi(u,v)\,du.
\tag{3.1}
\]

Las densidades marginales de (1.2) satisfacen

\[
\begin{aligned}
q_{U,\varepsilon}(u)
&=1+\varepsilon t_U(u)+o(\varepsilon),
&t_U(u)&=2[\psi_U(u)-\bar\psi],\\
q_{V,\varepsilon}(v)
&=1+\varepsilon t_V(v)+o(\varepsilon),
&t_V(v)&=2[\psi_V(v)-\bar\psi].
\end{aligned}
\tag{3.2}
\]

Pongamos

\[
A(x):=\int_0^x t_U(s)\,ds,
\qquad
B(y):=\int_0^y t_V(s)\,ds.
\]

Las CDF marginales y sus inversas tienen las expansiones

\[
\begin{aligned}
F_{U,\varepsilon}(u)&=u+\varepsilon A(u)+o(\varepsilon),
&Q_{U,\varepsilon}(x)&=x-\varepsilon A(x)+o(\varepsilon),\\
F_{V,\varepsilon}(v)&=v+\varepsilon B(v)+o(\varepsilon),
&Q_{V,\varepsilon}(y)&=y-\varepsilon B(y)+o(\varepsilon).
\end{aligned}
\tag{3.3}
\]

Los signos de las inversas se obtienen sustituyendo, por ejemplo,
`Q_U=x+epsilon qdot+o(epsilon)` en
`F_U(Q_U)=x`: resulta `qdot=-A(x)`.

### 3.2 Diferenciación de la densidad de cópula

La transformación PIT dependiente de `epsilon` es

\[
(u,v)\longmapsto
(x,y)=(F_{U,\varepsilon}(u),F_{V,\varepsilon}(v)).
\]

Su densidad de cópula es exactamente

\[
c_\varepsilon(x,y)
=\frac{
q_\varepsilon(Q_{U,\varepsilon}(x),Q_{V,\varepsilon}(y))
}{
q_{U,\varepsilon}(Q_{U,\varepsilon}(x))
q_{V,\varepsilon}(Q_{V,\varepsilon}(y))
}.
\tag{3.4}
\]

La contribución del movimiento de los cuantiles no se omite. Al derivar el
logaritmo del numerador, la regla de la cadena da

\[
\left.\partial_\varepsilon\log q_\varepsilon\right|_0
-A(x)\,\partial_u\log q_0
-B(y)\,\partial_v\log q_0.
\]

La regla de la cadena se justifica sin subir `psi` a `C^1`: el mapa
`(\varepsilon,u,v)\mapsto 2\varepsilon\psi(u,v)-\log Z(\varepsilon)` es
conjuntamente diferenciable en `(0,x,y)` y su parte espacial se anula en el
nulo por continuidad uniforme de `psi` sobre el compacto `D`. (Si se prefiere
una hipótesis puntual, basta `psi\in C^1`.) Como el nulo es el producto
uniforme, `q_0=1` y las dos derivadas espaciales son cero. El resultado es `t_psi(x,y)`. En los dos denominadores ocurre lo
mismo: las velocidades `-A(x)` y `-B(y)` multiplican derivadas espaciales de
`log 1`, mientras sus derivadas paramétricas son `t_U(x)` y `t_V(y)`.
Por tanto,

\[
\begin{aligned}
h_\psi(x,y)
&:=\left.\partial_\varepsilon\log c_\varepsilon(x,y)
\right|_{\varepsilon=0}\\
&=t_\psi(x,y)-t_U(x)-t_V(y)\\
&=2[\psi(x,y)-\bar\psi]
  -2[\psi_U(x)-\bar\psi]
  -2[\psi_V(y)-\bar\psi].
\end{aligned}
\]

Así queda derivada la fórmula, incluidos factor, signo y constante:

\[
\boxed{
h_\psi(u,v)
=2[\psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi].
}
\tag{3.5}
\]

Además, al diferenciar las marginales uniformes de `c_epsilon`,

\[
\int_0^1h_\psi(u,v)\,dv=0
\quad\text{para todo }u,
\qquad
\int_0^1h_\psi(u,v)\,du=0
\quad\text{para todo }v,
\]

lo que también se comprueba directamente en (3.5).

## 4. Falsificador marginal exacto

Sea

\[
\psi(u,v)=\alpha(u)+\beta(v)+c,
\]

con `alpha,beta` continuas. Si
`bar alpha=int_0^1 alpha` y `bar beta=int_0^1 beta`, entonces

\[
\begin{aligned}
\psi_U(u)&=\alpha(u)+\bar\beta+c,\\
\psi_V(v)&=\bar\alpha+\beta(v)+c,\\
\bar\psi&=\bar\alpha+\bar\beta+c.
\end{aligned}
\]

La expresión entre corchetes de (3.5) es exactamente cero, término a término.
Luego

\[
\boxed{h_\psi=0.}
\]

El falsificador marginal pasa. Geométricamente, estas son precisamente las
direcciones separables que las reparametrizaciones nulas eliminan en el canal
de rangos, en acuerdo con el Teorema C del WP6 de dicotomía nula.

## 5. Score condicionado a la permutación de rangos

### 5.1 Identidad de score condicional

Para cada `epsilon`, el PIT es creciente en cada coordenada y no altera la
permutación de rangos. Por ello la ley de `Pi_N` calculada desde `q_epsilon`
es exactamente la calculada desde su cópula `c_epsilon`, aunque el PIT dependa
del parámetro.

Sean `(U_k,V_k)`, `1<=k<=N`, iid con densidad de cópula `c_epsilon`, y sea
`Pi_N` la permutación definida ordenando los puntos por `U` y registrando el
rango de `V`: si el punto de rango `i` en `U` tiene rango `j` en `V`, entonces
`Pi_N(i)=j`.

La densidad nula es producto y el score de la muestra completa es

\[
T_{N,\psi}
=\left.\partial_\varepsilon
\sum_{k=1}^N\log c_\varepsilon(U_k,V_k)
\right|_0
=\sum_{k=1}^Nh_\psi(U_k,V_k).
\tag{5.1}
\]

Sea `C_pi` la cámara de muestras que inducen `Pi_N=pi`. La cámara está
definida por rangos en coordenadas de cópula y **no depende de**
`varepsilon`; no hay término de borde de dominio móvil. Además `c_epsilon`
y `partial_epsilon c_epsilon` son conjuntamente continuas sobre el compacto
`[-epsilon_0,epsilon_0] times D` (porque `psi` es continua y `q_epsilon>0`
para todo `epsilon`), luego uniformemente acotadas: la derivación bajo la
integral es por dominación uniforme en un entorno de `epsilon=0`, no sólo
por la acotación del tangente en el nulo. Como
`p_epsilon(pi)=int_{C_pi} product_k c_epsilon` y
`p_0(pi)=1/N!`, tenemos

\[
\begin{aligned}
S_{N,\psi}(\pi)
&:=\left.\partial_\varepsilon\log p_\varepsilon(\pi)\right|_0\\
&=\frac{1}{p_0(\pi)}
  \int_{C_\pi}\left(\sum_{k=1}^Nh_\psi(u_k,v_k)\right)
  \prod_{k=1}^Ndu_k\,dv_k\\
&=\mathbb E_0[T_{N,\psi}\mid\Pi_N=\pi].
\end{aligned}
\tag{5.2}
\]

No se ha supuesto independencia después de ordenar: (5.2) es la identidad de
score condicional derivada directamente del likelihood.

### 5.2 Especialización rank-one

Bajo el producto uniforme, dados los rangos, los vectores de estadísticos de
orden

\[
(U_{(1)},\ldots,U_{(N)})
\quad\text{y}\quad
(V_{(1)},\ldots,V_{(N)})
\]

son independientes entre sí y de la permutación de rangos (independencia
clásica rango ⊥ estadísticos de orden bajo el nulo uniforme), y la cámara
`Pi_N=pi` empareja `U_(i)` con `V_(pi(i))`. `Pi_N` **depende del
realizador** (el orden lineal de `U` y el de `V`); el dato order-only es
la clase `[P_{Pi_N}]`. Para una constante `kappa` y

\[
h_\psi(u,v)=\kappa f(u)f(v),
\qquad
a_{i,N}:=\mathbb E[f(U_{(i)})],
\]

(5.2) factoriza exactamente:

\[
\boxed{
S_{N,\psi}(\pi)
=\kappa\sum_{i=1}^Na_{i,N}a_{\pi(i),N}.
}
\tag{5.3}
\]

No aparece ningún factor adicional al condicionar a rangos. Todo factor `2`
de (5.3) debe proceder del coeficiente del **tangente de cópula**.

## 6. Auditoría de las dos convenciones de `lambda`

### 6.1 Convención A: `lambda` parametriza el tangente de cópula

Si se define

\[
h_\psi(u,v)=\lambda f(u)f(v),
\]

entonces (5.3) da necesariamente

\[
\boxed{
S_{N,\psi}(\pi)
=\lambda\sum_i a_{i,N}a_{\pi(i),N}.
}
\tag{6.1}
\]

### 6.2 Convención B: `lambda` parametriza la proyección geométrica

Definamos el doble centrado geométrico

\[
\mathcal P\psi
:=\psi-\psi_U-\psi_V+\bar\psi.
\]

Si se define

\[
\mathcal P\psi(u,v)=\lambda f(u)f(v),
\]

entonces (3.5) dice `h_psi=2 lambda f f`, y (5.3) da

\[
\boxed{
S_{N,\psi}(\pi)
=2\lambda\sum_i a_{i,N}a_{\pi(i),N}.
}
\tag{6.2}
\]

### 6.3 Comparación con el teorema combinatorio congelado

El score congelado

\[
S_N(\pi)=2\sum_i a_{i,N}a_{\pi(i),N}
\]

corresponde a la Convención B con `lambda=1`, es decir,
`mathcal P psi=f tensor f` y `h_psi=2 f tensor f`. Equivalentemente, bajo la
Convención A corresponde a un coeficiente de cópula igual a `2`.

**El mismatch no es un error matemático.** Ninguna de las dos fórmulas es
falsa: `h_psi=lambda f tensor f` define legítimamente `lambda` en el nivel del
tangente de cópula, y `S_N=2 lambda sum_i a_i a_{pi(i)}` es legítima con
`lambda` definida en el nivel de la proyección geométrica. Lo incompatible es
**usar el mismo símbolo `lambda` para ambos niveles**, que difieren por el
factor `2` de (3.5).

La hoja de ruta §2.2 escribe la Convención A, pero §2.3 usa el score de la
Convención B con el mismo símbolo `lambda`, sin una redefinición intermedia.
No existe en los documentos leídos una convención previa que absorba ese
factor. Por tanto,

```text
ROADMAP_NORMALIZATION_MISMATCH = CONFIRMED
```

La corrección mínima que mantiene intacta §2.3 y alinea el parámetro con la
perturbación geométrica es sustituir en §2.2:

```diff
- h_\psi(u,v)=\lambda f(u)f(v),
+ \psi(u,v)-\psi_U(u)-\psi_V(v)+\bar\psi
+   =\lambda f(u)f(v),
+ \qquad\text{equivalentemente}\qquad
+ h_\psi(u,v)=2\lambda f(u)f(v),
```

La convención adoptada en todo este documento es la **B**, porque alinea el
parámetro directamente con la perturbación geométrica y deja el score en la
forma literal del teorema congelado. No se modifica la hoja de ruta en este
artefacto: la corrección de §2.2 es G2, commit propio.

## 7. Testigo no sinusoidal de no-vacuidad

Tomemos

\[
f(u)=u-\frac12.
\]

Es polinómica, por tanto suave, y satisface

\[
\int_0^1f(u)\,du=0,
\qquad
\int_0^1f(u)^2\,du=\frac1{12}>0,
\qquad
\|f\|_\infty=\frac12.
\]

Para cualquier `lambda in R`, definimos explícitamente

\[
\boxed{
\psi_\lambda(u,v)
=\lambda f(u)f(v)
=\lambda\left(u-\frac12\right)\left(v-\frac12\right).
}
\]

Como `f` es centrada,

\[
(\psi_\lambda)_U=(\psi_\lambda)_V=0,
\qquad
\bar\psi_\lambda=0.
\]

Luego `mathcal P psi_lambda=lambda f tensor f` y

\[
h_{\psi_\lambda}(u,v)=2\lambda f(u)f(v),
\qquad
S_{N,\psi_\lambda}(\pi)
=2\lambda\sum_i a_{i,N}a_{\pi(i),N}.
\]

Este testigo demuestra sólo que la subclase objetivo no está vacía. No es una
clasificación de todas las perturbaciones que producen un tangente rank-one.

## 8. Veredicto del puente diferencial

La cadena de primer orden queda cerrada, en las normalizaciones explícitas de
§1:

\[
\boxed{
\psi
\longmapsto
t_\psi=2(\psi-\bar\psi)
\longmapsto
h_\psi=2(\psi-\psi_U-\psi_V+\bar\psi)
\longmapsto
S_{N,\psi}(\pi)
=\mathbb E_0\!\left[\sum_kh_\psi(U_k,V_k)\mid\Pi_N=\pi\right].
}
\]

En el sector simétrico rank-one, si `mathcal P psi=lambda f tensor f`, el
último miembro es exactamente `2 lambda sum_i a_i a_pi(i)`.

Este veredicto es sólo el del puente diferencial. La caracterización completa
de las `psi` que producen ese tangente se cierra en §9, el factor se
contrasta por una vía independiente en §10 y el límite de energía de los
perfiles se prueba en §11. El teorema geométrico asintótico (fase S2) queda
fuera de alcance.

## 9. Clasificación exacta de la subclase rank-one simétrica

### 9.1 El doble centrado es una proyección lineal

Sobre `C(D;R)` con la norma del supremo definimos los dos promedios
parciales

\[
(\mathcal M_v\psi)(u,v):=\int_0^1\psi(u,v')\,dv'=\psi_U(u),
\qquad
(\mathcal M_u\psi)(u,v):=\int_0^1\psi(u',v)\,du'=\psi_V(v).
\tag{9.1}
\]

El subíndice nombra la variable que se promedia. Ambos son lineales, envían
funciones continuas en funciones continuas, tienen norma `<=1`, son
idempotentes y conmutan, con

\[
(\mathcal M_u\mathcal M_v)\psi
=(\mathcal M_v\mathcal M_u)\psi
=\bar\psi\cdot\mathbf 1
\qquad\text{para todo }\psi\in C(D).
\]

Por tanto el operador de §6.2 se factoriza:

\[
\boxed{
\mathcal P
=(\mathbb I-\mathcal M_u)(\mathbb I-\mathcal M_v)
=\mathbb I-\mathcal M_u-\mathcal M_v+\mathcal M_u\mathcal M_v,
}
\tag{9.2}
\]

y `P^2=P` porque cada factor es idempotente y ambos conmutan. `P` es la
**proyección de interacción**: no es una notación abreviada, es un proyector
de rango infinito con núcleo y rango identificables.

### 9.2 Núcleo, rango y descomposición

Definimos

\[
\mathcal A
:=\{(u,v)\mapsto\alpha(u)+\beta(v)\ :\ \alpha,\beta\in C[0,1]\},
\]
\[
\mathcal R
:=\left\{\varphi\in C(D)\ :\
\int_0^1\varphi(u,v)\,dv=0\ \forall u,\quad
\int_0^1\varphi(u,v)\,du=0\ \forall v\right\}.
\]

**Proposición 9.1.**
`ker P = A`, `ran P = R`, y `C(D;R)=A (+) R` como suma directa.

*Prueba.*

1. `A subset ker P`: es exactamente el cálculo de §4, con la constante
   absorbida en `alpha`.
2. `ker P subset A`: si `P psi=0`, entonces
   `psi=psi_U+psi_V-bar psi`, y el miembro derecho es de la forma
   `alpha(u)+beta(v)`.
3. `ran P subset R`: para todo `u`,
   `int_0^1 (P psi)(u,v)dv = psi_U(u)-psi_U(u)-bar psi+bar psi=0`,
   y simétricamente en la otra variable. Es la propiedad ya registrada tras
   (3.5), dividida por `2`.
4. `R subset ran P`: si `phi in R` entonces `phi_U=phi_V=0` y
   `bar phi=0`, luego `P phi=phi`.
5. `A cap R={0}`: si `alpha(u)+beta(v) in R`, integrando en `v` se obtiene
   `alpha(u)+bar beta=0` para todo `u`, luego `alpha` es constante; por
   simetría `beta` es constante; una constante en `R` es cero.
6. Suma: `psi=(psi-P psi)+P psi`, con
   `psi-P psi=psi_U+psi_V-bar psi in A` y `P psi in R`. `∎`

La descomposición es la lectura estructural del falsificador de §4: `A` es
exactamente el subespacio que el canal de rangos no ve. Es la descomposición
clásica ANOVA / Hoeffding de `C([0,1]^2)` (Hoeffding 1948; proyección de
Hájek), ya usada bajo ese nombre en
`wp4_ibar_direct_score_derivation.md:300-312`. No se presenta como
matemática nueva.

Geométricamente, `ker P = A` son las direcciones **planas**, no meramente
marginales: separable ⟺ plano por la Proposición B de
`wp6_d2_null_copula_dichotomy.md` §3.

### 9.3 Lema de solubilidad: `int f = 0` no es una comodidad

**Lema 9.2.** Sean `f in C[0,1]` con `f != 0` y `lambda != 0`. Entonces

\[
\lambda\,f\otimes f\in\operatorname{ran}\mathcal P
\iff
\int_0^1f(u)\,du=0.
\]

*Prueba.* `int_0^1 lambda f(u)f(v)dv = lambda f(u) int_0^1 f`. Esto se anula
para todo `u` si y sólo si `int f=0`, ya que `lambda != 0` y `f != 0`. El
caso de la otra variable es idéntico por simetría. Se concluye con los puntos
3 y 4 de la Proposición 9.1. `∎`

**Corolario 9.3.** Si `int f != 0` y `lambda != 0`, la ecuación
`P psi = lambda f tensor f` **no tiene ninguna solución** `psi in C(D;R)`.

La hipótesis `int_0^1 f=0` de la hoja de ruta §2.2 queda así reinterpretada:
no es una normalización conveniente del perfil, es exactamente la condición
de solubilidad del problema geométrico inverso.

### 9.4 Teorema de clasificación

**Teorema 6 (`GEOMETRIC_TANGENT_CLASSIFICATION`, sector rank-one simétrico).**
Sean `lambda in R` y `f in C[0,1]` con

\[
\int_0^1f=0,
\qquad
\int_0^1f^2>0.
\]

Para `psi in C(D;R)` son equivalentes:

\[
\text{(a)}\quad\mathcal P\psi=\lambda\,f\otimes f;
\qquad
\text{(b)}\quad h_\psi=2\lambda\,f\otimes f;
\]
\[
\text{(c)}\quad
\boxed{
\exists\,\alpha,\beta\in C[0,1]:\quad
\psi(u,v)=\alpha(u)+\beta(v)+\lambda f(u)f(v).
}
\tag{9.3}
\]

Cuando se cumplen, el score de rangos es exactamente

\[
S_{N,\psi}(\pi)
=2\lambda\sum_{i=1}^Na_{i,N}a_{\pi(i),N},
\qquad
a_{i,N}=\mathbb E[f(U_{(i)})].
\]

*Prueba.*
`(a) <=> (b)` es (3.5), que dice `h_psi = 2 P psi`, más `2 != 0`.
`(c) => (a)`: por el punto 1 de la Proposición 9.1, `P` anula
`alpha(u)+beta(v)`. Por el punto 4 de la Proposición 9.1, `int f=0` implica
`(f\otimes f)_U=(f\otimes f)_V=0` y `bar(f\otimes f)=0`, luego
`f\otimes f\in R\subset\operatorname{ran}P` y
`P(\lambda f\otimes f)=\lambda f\otimes f` para **todo** `lambda in R`,
incluido `lambda=0`, donde ambos miembros se anulan. Se suma por linealidad.
(El Lema 9.2 no se invoca: sus hipótesis `lambda != 0` y `f != 0` no cubren
el caso degenerado.)
`(a) => (c)`: sea `varphi := psi - lambda f tensor f`. Entonces, de nuevo
por el punto 4, `P varphi = P psi - lambda f tensor f = 0`, luego
`varphi in ker P = A` por la Proposición 9.1, es decir
`varphi(u,v)=alpha(u)+beta(v)`.
La última afirmación es (5.3) con `kappa=2 lambda`.
La hipótesis `int f^2>0` **no se usa** en `(a)<=> (b)<=> (c)`; se arrastra
para §9.5(ii) y para el Teorema 7 (H3). `∎`

La clase geométrica queda pues **explícita, no vacía, cerrada y
infinito-dimensional como coset; rank-one módulo el núcleo plano**: es
exactamente el coset afín

\[
\lambda\,f\otimes f+\mathcal A
\subset C(D;R).
\]

Toda `psi` del coset produce **literalmente el mismo** `h_psi` y el mismo
score de rangos, para todo `N` y toda `pi`.

### 9.5 Gauge exacto: qué libertad queda y cuál no

**(i) Redundancia aditiva.** En (9.3) la pareja `(alpha,beta)` está
determinada sólo módulo `(alpha+c,\ beta-c)`, y nada más: si
`alpha_1+beta_1=alpha_2+beta_2`, entonces `alpha_1-alpha_2=beta_2-beta_1` es a
la vez función sólo de `u` y sólo de `v`, luego constante.

**(ii) Redundancia de escala, restringida a `lambda != 0`.** Para `c != 0`,
la pareja `(lambda/c^2, c f)` produce el mismo `lambda f tensor f`.
Normalizando `int_0^1 f^2=1` y suponiendo `lambda != 0`, el parámetro
`lambda` queda unívocamente determinado y `f` queda determinada salvo el
signo global, bajo el cual `f tensor f` es invariante: si
`lambda f\otimes f=lambda' g\otimes g` con `||f||_2=||g||_2=1`, el producto
interno contra `f\otimes f` da `lambda=lambda'<g,f>^2`, luego
`|lambda|=|lambda'|` y `|<g,f>|=1`, de donde `g=\pm f` y `lambda=lambda'`.
Con esa normalización, `(lambda, [f])` es una coordenada fiel de la clase
**cuando** `lambda != 0`. En `lambda=0` la afirmación es falsa: todo `f`
produce el mismo coset `A`.

**(iii) Fibra exacta sobre el tangente; no hay unicidad irrestricta de
equivalencias.**

**Proposición 9.4.** Sean `phi,chi:[0,1]->[0,1]` biyecciones estrictamente
crecientes. Si la reparametrización separada
`(u,v) |-> (phi(u),chi(v))` preserva la medida de referencia
`mu_0=du\,dv` fijada en §1.1, entonces `phi=chi=id`.

*Prueba.* La preservación de la medida en rectángulos
`[0,s]\times[0,t]` exige `phi^{-1}(s)\,chi^{-1}(t)=st` para todo
`s,t\in[0,1]`. Tomando `t=1` (y `chi^{-1}(1)=1`) queda `phi^{-1}(s)=s`;
simétricamente `chi=\mathrm{id}`. No se usa absoluta continuidad. `∎`

El enunciado de fibra que el Teorema 6 prueba, y el que la puerta necesita,
es

\[
\{\psi:\ h_\psi=h\}=\psi_0+\mathcal A
\]

para cualquier `psi_0` con `h_{psi_0}=h`. Eso es exactamente la
estabilidad bajo `ker P=A`. La Proposición 9.4 cierra el gauge **separado**
de reparametrizaciones nulas crecientes que preservan `mu_0`. No cubre el
intercambio `(u,v)\mapsto(v,u)`, automorfismo de orden que preserva
`du\,dv` y actúa no trivialmente sobre `A`
(`alpha(u)+beta(v)\mapsto alpha(v)+beta(u)`), ni la reflexión
`(u,v)\mapsto(1-u,1-v)`, anti-automorfismo de orden que preserva `mu_0`.
Ninguno de los dos perturba el sector rank-one **simétrico**; ambos
falsifican cualquier lectura irrestricta de «única equivalencia marginal».
La lista de equivalencias pertinentes queda así: el coset de `A` sobre
`h_psi`, más esas dos simetrías del cuadrado, que no se cocientan aquí.

Regularidad (desviación respecto de la hoja de ruta §2.2): todo lo anterior
se prueba para `f\in C[0,1]`, clase estrictamente mayor que el «`f` suave»
nombrado en el plan. La lectura geométrica puntual
`partial_u partial_v psi = lambda f' f'` exige además `f\in C^1`; ambos
testigos de §§7 y 10 la cumplen.

### 9.6 Lo que deliberadamente no se promueve

El argumento de §9.4 se traslada palabra por palabra al caso asimétrico: si
`f,g in C[0,1]` con `int f=int g=0`, entonces
`P psi = lambda f tensor g` si y sólo si
`psi=alpha(u)+beta(v)+lambda f(u)g(v)`.

Esto **no se promueve**. El Teorema 5 congelado cubre únicamente el score
simétrico `2 sum_i a_{i,N}a_{pi(i),N}`, y la hoja de ruta §2.4 prohíbe
expresamente la promoción del sector `f != g`. Queda registrado como
observación fuera de alcance:

```text
ASYMMETRIC_RANK_ONE_SECTOR = CLASSIFIED_BUT_NOT_PROMOTED
```

## 10. Falsificador independiente del factor `2`, del signo y de `bar psi`

La hoja de ruta §2.4 exige verificar el factor `2`, el signo y el término
`bar psi` mediante una **diferenciación independiente**. El testigo de §7 es
insuficiente para ese fin: al ser doblemente centrado, sus tres términos
sustraídos se anulan y no pueden discriminar la fórmula (3.5) de otras.

Tomamos por ello un generador con marginales y media **no nulas**:

\[
\psi(u,v)=uv.
\]

Predicción de (3.5), sin usarla todavía:
`psi_U(u)=u/2`, `psi_V(v)=v/2`, `bar psi=1/4`, luego

\[
\mathcal P\psi
=uv-\frac u2-\frac v2+\frac14
=\left(u-\frac12\right)\left(v-\frac12\right),
\qquad
h_\psi\overset{?}{=}2\left(u-\frac12\right)\left(v-\frac12\right).
\tag{10.1}
\]

**Verificación directa, sin invocar (3.5).** Todo lo que sigue es cálculo
cerrado a primer orden a partir de (1.2). La fórmula (3.4) es el cambio de
variables estándar de la densidad de cópula, no el resultado derivado (3.5).

Normalización:

\[
Z(\varepsilon)
=\int_0^1\!\!\int_0^1e^{2\varepsilon uv}\,du\,dv
=1+2\varepsilon\cdot\tfrac14+O(\varepsilon^2)
=1+\frac\varepsilon2+O(\varepsilon^2),
\]
\[
q_\varepsilon(u,v)
=\frac{1+2\varepsilon uv}{1+\varepsilon/2}+O(\varepsilon^2)
=1+\varepsilon\left(2uv-\frac12\right)+O(\varepsilon^2).
\]

Marginal en `u`, integrando exactamente:

\[
\int_0^1e^{2\varepsilon uv}\,dv
=\frac{e^{2\varepsilon u}-1}{2\varepsilon u}
=1+\varepsilon u+O(\varepsilon^2),
\qquad
q_{U,\varepsilon}(u)
=1+\varepsilon\left(u-\frac12\right)+O(\varepsilon^2),
\]

y por simetría `q_{V,eps}(v)=1+eps(v-1/2)+O(eps^2)`. Esto ya confirma
`t_U(u)=u-1/2=2[psi_U(u)-bar psi]`, con el `bar psi=1/4` en su sitio.

Cuantiles: `A(x)=int_0^x(s-1/2)ds=x(x-1)/2`, luego
`Q_{U,eps}(x)=x-eps A(x)+O(eps^2)`, y análogamente en `y`. Como
`q_eps=1+O(eps)` y `q_{U,eps}=1+O(eps)`, el desplazamiento `O(eps)` del
cuantil sólo contribuye a `O(eps^2)` en (3.4). Sustituyendo en (3.4):

\[
c_\varepsilon(x,y)
=\frac{1+\varepsilon\left(2xy-\frac12\right)}
       {\left[1+\varepsilon\left(x-\frac12\right)\right]
        \left[1+\varepsilon\left(y-\frac12\right)\right]}
+O(\varepsilon^2)
=1+\varepsilon\left[2xy-x-y+\frac12\right]+O(\varepsilon^2).
\]

Y como `2xy-x-y+1/2=2(x-1/2)(y-1/2)`,

\[
\boxed{
h_\psi(x,y)
=\left.\partial_\varepsilon\log c_\varepsilon\right|_0
=2\left(x-\frac12\right)\left(y-\frac12\right),
}
\tag{10.2}
\]

que coincide exactamente con la predicción (10.1). El cálculo ejercita los
tres términos sustraídos: el `-1/2` procede de `Z'(0)=2 bar psi`, los dos
`-(x-1/2)`, `-(y-1/2)` de las marginales, y sólo su combinación produce el
doble centrado. Un error de signo o un factor `2` espurio en cualquiera de
ellos rompería la identidad `2xy-x-y+1/2=2(x-1/2)(y-1/2)`.

```text
FACTOR_TWO_INDEPENDENT_CHECK = PASS
```

**Segundo testigo no sinusoidal.** Por el Teorema 6, `psi=uv` pertenece a la
clase con `lambda=1` y `f(t)=t-1/2`, en la descomposición

\[
uv=\underbrace{\frac u2}_{\alpha(u)}
  +\underbrace{\left(\frac v2-\frac14\right)}_{\beta(v)}
  +\left(u-\frac12\right)\left(v-\frac12\right),
\]

de modo que `psi=uv` y `psi_1=(u-1/2)(v-1/2)` son dos generadores
geométricamente distintos, con marginales distintas, que producen el mismo
score de rangos para todo `N`. Es la ceguera a `A` hecha explícita.

## 11. Las tres hipótesis del teorema congelado para `a_{i,N}=E[f(U_{(i)})]`

Sea `f in C[0,1]` con `int_0^1 f=0` y `c:=int_0^1 f^2>0`, y sean
`U_{(1)}<...<U_{(N)}` los estadísticos de orden de `N` uniformes iid en
`[0,1]`. Ponemos

\[
a_{i,N}:=\mathbb E[f(U_{(i)})],
\qquad
p_{i,N}:=\frac{i}{N+1}.
\]

Se reutilizan de §7.7 del WP6 modular los dos hechos elementales

\[
\mathbb E[U_{(i)}]=p_{i,N},
\qquad
\operatorname{Var}(U_{(i)})
=\frac{i(N+1-i)}{(N+1)^2(N+2)}
\le\frac1{4(N+2)}.
\tag{11.1}
\]

**Teorema 7.** Con las hipótesis anteriores, el array triangular
`a_{i,N}` satisface las tres condiciones del Teorema 5:

\[
\text{(H1)}\quad
M_*:=\sup_N\max_{1\le i\le N}|a_{i,N}|\le\|f\|_\infty<\infty;
\]
\[
\text{(H2)}\quad
\sum_{i=1}^Na_{i,N}=0
\quad\text{exactamente, para todo }N\ge1;
\]
\[
\text{(H3)}\quad
\frac1N\sum_{i=1}^Na_{i,N}^2
\longrightarrow
\int_0^1f(u)^2\,du=c>0.
\]

### 11.1 (H1) Acotación uniforme

`f` es continua sobre el compacto `[0,1]`, luego `‖f‖_inf<infty`. Por la
desigualdad de Jensen para el valor absoluto,

\[
|a_{i,N}|=|\mathbb E[f(U_{(i)})]|\le\mathbb E|f(U_{(i)})|\le\|f\|_\infty,
\]

uniformemente en `i` y en `N`. `∎`

### 11.2 (H2) Centrado exacto

Los estadísticos de orden son una reordenación de la muestra, luego
`sum_i f(U_{(i)}) = sum_k f(U_k)` puntualmente. Por linealidad de la
esperanza,

\[
\sum_{i=1}^Na_{i,N}
=\mathbb E\!\left[\sum_{i=1}^Nf(U_{(i)})\right]
=\sum_{k=1}^N\mathbb E[f(U_k)]
=N\int_0^1f
=0.
\]

La identidad es exacta para todo `N`, no asintótica, y usa exactamente la
hipótesis `int f=0` del Lema 9.2. `∎`

### 11.3 (H3) Energía del perfil

Sea `omega_f(delta):=sup\{|f(x)-f(y)| : |x-y|<=delta\}` el módulo de
continuidad de `f`. Por continuidad uniforme sobre el compacto,
`omega_f(delta) -> 0` cuando `delta -> 0^+`.

**Paso 1 (aproximación uniforme del perfil).** Para todo `delta>0`, cortando
el suceso según `|U_{(i)}-p_{i,N}|` y usando Chebyshev con (11.1),

\[
\begin{aligned}
|a_{i,N}-f(p_{i,N})|
&\le\mathbb E\big|f(U_{(i)})-f(p_{i,N})\big|\\
&\le\omega_f(\delta)
   +2\|f\|_\infty\,
   \Pr\!\left(|U_{(i)}-p_{i,N}|>\delta\right)\\
&\le\omega_f(\delta)
   +\frac{2\|f\|_\infty}{\delta^2}\operatorname{Var}(U_{(i)})
\le\omega_f(\delta)+\frac{\|f\|_\infty}{2(N+2)\delta^2}.
\end{aligned}
\]

Eligiendo `delta=delta_N:=(N+2)^{-1/4}`, que tiende a cero, se obtiene

\[
\boxed{
\epsilon_N
:=\max_{1\le i\le N}\big|a_{i,N}-f(p_{i,N})\big|
\le\omega_f\!\left((N+2)^{-1/4}\right)
  +\frac{\|f\|_\infty}{2\sqrt{N+2}}
\xrightarrow[N\to\infty]{}0.
}
\tag{11.2}
\]

**Paso 2 (transferencia a los cuadrados).** Como
`|a_{i,N}|,|f(p_{i,N})| <= ‖f‖_inf`,

\[
\left|
\frac1N\sum_{i=1}^Na_{i,N}^2
-\frac1N\sum_{i=1}^Nf(p_{i,N})^2
\right|
\le\frac1N\sum_{i=1}^N
  |a_{i,N}-f(p_{i,N})|\,\big(|a_{i,N}|+|f(p_{i,N})|\big)
\le2\|f\|_\infty\,\epsilon_N.
\tag{11.3}
\]

**Paso 3 (suma de Riemann).** Sea `g:=f^2`, continua. La suma
`(N+1)^{-1} sum_{i=1}^{N+1} g(i/(N+1))` es la suma de Riemann por extremos
derechos de la partición uniforme de `[0,1]` con paso `1/(N+1)`, luego dista
de `int_0^1 g` a lo sumo `omega_g(1/(N+1))`. Quitando el término `i=N+1`, de
peso `g(1)/(N+1)`, y corrigiendo el peso por `(N+1)/N`,

\[
\left|
\frac1N\sum_{i=1}^Ng(p_{i,N})-\int_0^1g
\right|
\le
\frac{N+1}{N}\left[
\omega_g\!\left(\frac1{N+1}\right)+\frac{\|g\|_\infty}{N+1}
\right]
+\frac1N\int_0^1g
\xrightarrow[N\to\infty]{}0.
\tag{11.4}
\]

Combinando (11.3) y (11.4) se obtiene (H3) con límite `c=int_0^1 f^2>0`. `∎`

### 11.4 Tasa para perfiles Lipschitz y control exacto del testigo

Si además `f` es Lipschitz de constante `L`, Cauchy–Schwarz y (11.1) dan
directamente

\[
|a_{i,N}-f(p_{i,N})|
\le L\,\mathbb E\big|U_{(i)}-p_{i,N}\big|
\le L\sqrt{\operatorname{Var}(U_{(i)})}
\le\frac{L}{2\sqrt{N+2}},
\]

luego `epsilon_N=O(N^{-1/2})` y, por (11.3)–(11.4),

\[
\left|\frac1N\sum_ia_{i,N}^2-\int_0^1f^2\right|=O(N^{-1/2}),
\]

la misma tasa que el corolario sinusoidal §7.7 del WP6 modular.

Para el testigo congelado `f(u)=u-1/2` todo es **exacto**, sin
aproximaciones. En efecto `a_{i,N}=E[U_{(i)}]-1/2=p_{i,N}-1/2`, de donde

\[
\max_i|a_{i,N}|<\frac12,
\qquad
\sum_{i=1}^Na_{i,N}
=\frac{1}{N+1}\cdot\frac{N(N+1)}{2}-\frac N2=0,
\]

y, con `m=N+1`,

\[
\sum_{i=1}^N\left(\frac im-\frac12\right)^2
=\frac1{m^2}\sum_{i=1}^{m-1}\left(i-\frac m2\right)^2
=\frac{(m-1)m(m-2)}{12m^2},
\]

es decir

\[
\boxed{
\frac1N\sum_{i=1}^Na_{i,N}^2
=\frac{N-1}{12(N+1)}
=\frac1{12}-\frac1{6(N+1)}
\longrightarrow
\frac1{12}
=\int_0^1\left(u-\frac12\right)^2du.
}
\tag{11.5}
\]

La convergencia es monótona creciente y de orden `O(N^{-1})`, mejor que la
cota genérica. Los parámetros del Teorema 5 para este testigo son, por tanto,
`M_* = 1/2` y `c = 1/12`.

### 11.5 Invariancia de escala en `lambda` y corolario condicional

**Lema 11.1.** La fracción de información `q_N=1-L_N/I_N^Pi` es invariante
bajo el reescalado del score `dot ell -> kappa dot ell` con `kappa != 0`.

*Prueba.* Por (7.4) de §7.4 del WP6 modular,
`I_N^Pi=E[(dot ell_N^Pi)^2]`. Por §7.5 del mismo WP,
`L_N=E[Var(dot ell_N^Pi | [P])]`. Ambos funcionales son homogéneos de grado
`2` en el score, luego su cociente es invariante. `∎`

**Lema 11.2 (identidad de proyección).** En el nulo, con score de media
cero,

\[
I_N^{[P]}
:=\mathbb E\bigl[(\partial_\varepsilon\log p_\varepsilon([P])|_0)^2\bigr]
=I_N^\Pi-L_N.
\]

*Prueba.* La derivada del log-likelihood de una clase finita es
`partial_eps log p_eps([P])|_0 = E_0[S | [P]]` (la fibra es finita). El
score de `Pi_N` tiene media nula, luego `I_N^Pi=Var(S)`. La ley de la
varianza total da `Var(S)=E[Var(S|[P])]+Var(E[S|[P]])`, es decir
`I_N^Pi=L_N+I_N^{[P]}`. `∎`

Por el Teorema 6, si `P psi = lambda f tensor f` con `lambda != 0`, el score
de rangos es `S_{N,psi}=lambda cdot (2 sum_i a_{i,N}a_{pi(i),N})`. Por el
Lema 11.1 basta aplicar el Teorema 5 al array `a_{i,N}`, cuyas tres hipótesis
son el Teorema 7. El Teorema 5 se enuncia para `q_N=1-L_N/I_N^Pi` y para
`N\ge N_A`, con `M_*` en el numerador. Como `M_*\le\|f\|_\infty` por (H1) y
la cota crece en `M_*`, sustituir `M_*` por `\|f\|_\infty` es una
debilitación válida. Con el Lema 11.2, `1-I_N^{[P]}/I_N^Pi=1-q_N`. Se
concluye el corolario condicional siguiente, **que no es el entregable de
S2** (hoja de ruta §3.3) ni abre esa fase:

\[
\boxed{
1-\frac{I_N^{[P]}}{I_N^\Pi}
\le
\left(
\frac{\sqrt{240C_A}\,\|f\|_\infty^4}{4\left(\int_0^1f^2\right)^2}+o(1)
\right)N^{-1/2},
\qquad N\ge N_A,
}
\tag{11.6}
\]

con `C_A` y `N_A` las constantes externas de (7.5) del WP6 modular, no
inventadas aquí. La cota no depende de `lambda`, ni de `alpha`, ni de
`beta`. `Pi_N` depende del realizador; **sólo** (11.6), a través del canal
congelado `Pi_N\to[P_{Pi_N}]`, es order-only.

## 12. Veredicto de la fase S1

Las cinco obligaciones de prueba de la hoja de ruta §2.3 quedan cubiertas:
(1) score de la muestra condicionada a `N` en (5.1); (2) score condicionado a
la permutación de rangos en (5.2); (3) forma rank-one `2 lambda sum_i a_i
a_{pi(i)}` en (5.3)/(6.2), con la convención de escala registrada en §6;
(4) las tres hipótesis sobre `a_{i,N}`, sin simulación, en el Teorema 7;
(5) los cuatro objetos separados por notación distinta en §1.2.

Los cuatro falsificadores de §2.4 quedan ejecutados: la perturbación puramente
marginal se anula (§4, y estructuralmente `ker P = A` en la Proposición 9.1);
el factor `2`, el signo y `bar psi` se confirman por diferenciación
independiente en forma cerrada con marginales no triviales (§10); se exhiben
dos testigos no sinusoidales, `psi_lambda` (§7) y `psi=uv` (§10); y el sector
asimétrico `f tensor g` se clasifica pero **no** se promueve (§9.6).

La caracterización es exacta y bilateral (Teorema 6), la clase es explícita,
no vacía, infinito-dimensional como coset y rank-one módulo el núcleo plano,
estable bajo `A` al nivel de `h_psi` (fibra `psi_0+A`), sin gauge separado
residual (Proposición 9.4). El intercambio y la reflexión del cuadrado no se
cocientan; no perturban el sector simétrico.

No se abre la fase S2, no se afirma ningún principio universal de causal sets,
no se toca ningún instrumento sellado, no se consume ninguna semilla y no se
modifica la hoja de ruta **en este artefacto**: la corrección de §6.3 es G2,
commit propio. (11.6) es un corolario condicional; no es el entregable
modular de S2.

```text
GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
S2_NOT_OPENED
S1_GEOMETRIC_TO_COPULA_BRIDGE = PROVED
FACTOR_TWO_INDEPENDENT_CHECK = PASS
RANK_PROFILE_HYPOTHESES = PROVED
ROADMAP_NORMALIZATION_MISMATCH = CONFIRMED
ASYMMETRIC_RANK_ONE_SECTOR = CLASSIFIED_BUT_NOT_PROMOTED
SYMMETRIC_RANK_ONE_SECTOR_ONLY
GENERIC_BILINEAR_SEPARABLE_EXTENSION = OPEN_NOT_ASSUMED
NO_HORIZON_CLAIM
MINKOWSKI_DIAMOND_PERTURBATIVE
NO_UNIVERSALITY_CLAIM
PRIORITY = PROVISIONAL_NOT_SEALED
```

## 13. Visibilidad exacta y dirección preferente para \(N=2\)

```text
N2_S1_VISIBLE_SUBSPACE_AND_PREFERRED_DIRECTION = PROVED_RANK_ONE
FIXED_N_ONLY = 2
NO_N_GREATER_THAN_2_CLAIM
NO_ASYMPTOTIC_CLAIM
REFERENCE_EXPERIMENT = TWO_IID_COPULA_OBSERVATIONS
```

Esta sección usa una convención local para evitar confundir objetos: aquí

\[
f:=\mathcal P\psi\in\operatorname{Ran}\mathcal P
\tag{13.1}
\]

es el tangente de interacción **bivariado**. No es el perfil univariado
denotado por \(f\) en el sector simétrico rank-one de §§5--11. Definimos

\[
\chi(u,v):=\left(u-\frac12\right)\left(v-\frac12\right).
\tag{13.2}
\]

Por (3.5), el score de una observación de la cópula en el nulo es

\[
h_\psi=2\mathcal P\psi=2f.
\tag{13.3}
\]

### 13.1. Derivadas de las dos probabilidades

En \(N=2\), \(p_{12}(0)=p_{21}(0)=1/2\). Condicionado a
\(\Pi_2=12\), los dos puntos emparejan mínimo con mínimo y máximo con
máximo. Las densidades de los estadísticos de orden de dos uniformes son
\(2(1-u)\) y \(2u\). La identidad de score condicional (5.2) da

\[
\begin{aligned}
S_{2,\psi}(12)
&=2\int_D f(u,v)
  \left[4(1-u)(1-v)+4uv\right] \,du\,dv\\
&=8\int_D f(u,v)[1-u-v+2uv] \,du\,dv.
\end{aligned}
\tag{13.4}
\]

Como \(f\in\operatorname{Ran}\mathcal P\), sus dos marginales se anulan.
Por tanto los términos \(1,u,v\) de (13.4) no contribuyen y

\[
S_{2,\psi}(12)
=16\int_D f(u,v)uv \,du\,dv
=16\langle f,\chi\rangle_{L^2(D)}.
\tag{13.5}
\]

La última igualdad vuelve a usar las marginales nulas de \(f\). Como
\(p'_\sigma(0)=p_\sigma(0)S_{2,\psi}(\sigma)\), resulta

\[
\boxed{p'_{12}(0)=8\langle f,\chi\rangle.}
\tag{13.6}
\]

Las dos probabilidades suman uno para todo \(\varepsilon\). Derivando esa
identidad,

\[
\boxed{p'_{21}(0)=-8\langle f,\chi\rangle.}
\tag{13.7}
\]

### 13.2. Forma Fisher del poset y kernel físico

Con las dos probabilidades nulas iguales a \(1/2\), (13.6)--(13.7) dan

\[
\boxed{
I_2^\Pi(f)
=\sum_{\sigma\in\mathfrak S_2}
  \frac{p'_\sigma(0)^2}{p_\sigma(0)}
=256\langle f,\chi\rangle^2.
}
\tag{13.8}
\]

La convención de \(\Pi_2\) de §5 envía \(12\) al poset cadena de dos
elementos y \(21\) a la anticadena de dos elementos. Son las dos clases de
isomorfismo posibles y el mapa es biyectivo. Por tanto no hay pérdida
adicional en este push-forward concreto:

\[
\boxed{I_2^{[P]}(f)=I_2^\Pi(f)=256\langle f,\chi\rangle^2.}
\tag{13.9}
\]

Por polarización, la forma bilineal es

\[
G_{[P]}^{(2)}(f,g)
=256\langle f,\chi\rangle\langle g,\chi\rangle.
\tag{13.10}
\]

Tiene rango uno sobre \(\operatorname{Ran}\mathcal P\), y su kernel físico
es exactamente

\[
\boxed{
\ker G_{[P]}^{(2)}
=\operatorname{Ran}\mathcal P\cap\chi^\perp.
}
\tag{13.11}
\]

Esto no es el gauge original. En el espacio de generadores geométricos,
\(\ker\mathcal P\) ni siquiera alcanza el sector \(f\): produce \(f=0\).
En cambio, (13.11) contiene direcciones no-gauge \(f\ne0\). Por ejemplo,

\[
f_0(u,v)
=\left(u-\frac12\right)
 \left[\left(v-\frac12\right)^2-\frac1{12}\right]
\tag{13.12}
\]

tiene ambas marginales nulas, no es cero y satisface
\(\langle f_0,\chi\rangle=0\). Es, por tanto, una dirección física de forma
volumétrica exactamente invisible para el poset de dos elementos.

### 13.3. Problema generalizado y eficiencia máxima

La referencia estadística es exclusivamente el experimento de **dos
observaciones iid de la cópula S1**. No es el embedding geométrico completo
ni el experimento de coordenadas anterior al PIT. Por (13.3), el Fisher de
una observación es \(4\lVert f\rVert_2^2\); la aditividad iid da

\[
I_2^{\mathrm{full}}(f)=8\lVert f\rVert_2^2,
\qquad
G_{\mathrm{full}}^{(2)}(f,g)=8\langle f,g\rangle.
\tag{13.13}
\]

Para \(f\ne0\), la retención relativa es

\[
\eta_2(f)
:=\frac{I_2^{[P]}(f)}{I_2^{\mathrm{full}}(f)}
=32\frac{\langle f,\chi\rangle^2}{\lVert f\rVert_2^2}.
\tag{13.14}
\]

Además,

\[
\lVert\chi\rVert_2^2
=\left[\int_0^1\left(u-\frac12\right)^2du\right]^2
=\frac1{144}.
\tag{13.15}
\]

Cauchy--Schwarz en (13.14) implica

\[
\boxed{
\eta_2(f)\le32\lVert\chi\rVert_2^2=\frac29,
}
\tag{13.16}
\]

con igualdad si y sólo si \(f=c\chi\) casi en todo punto para algún
\(c\ne0\). Como los tangentes considerados son continuos, la igualdad casi
en todo punto equivale a igualdad puntual. La dirección preferente es única
módulo escala y signo.

Equivalentemente, el problema generalizado

\[
G_{[P]}^{(2)}(v,g)
=\lambda G_{\mathrm{full}}^{(2)}(v,g)
\qquad\text{para todo }g\in\operatorname{Ran}\mathcal P
\tag{13.17}
\]

tiene un único autovalor no nulo y el resto del espacio es su kernel:

\[
\boxed{
\lambda_1=\frac29,
\qquad v_1\in\operatorname{span}\{\chi\}\setminus\{0\},
\qquad
\lambda=0\text{ sobre }\chi^\perp\cap\operatorname{Ran}\mathcal P.
}
\tag{13.18}
\]

### 13.4. Techo de interpretación

Para \(N=2\), el poset abstracto ve exactamente la componente del tangente
de interacción S1 sobre \(\chi\). En particular,

```text
GAUGE_KERNEL = ker P
NON_GAUGE_N2_INVISIBLE_DIRECTIONS = ran P intersect chi^perp
N2_VISIBLE_SUBSPACE = span{chi}
N2_MAX_COPULA_FISHER_RETENTION = 2/9
```

El cociente \(2/9\) compara el poset con dos observaciones continuas de la
cópula S1. No mide una fracción de la geometría total, no usa el embedding
continuo completo y no es una afirmación sobre EF, Schwarzschild, Kerr,
\(N>2\), Poisson, localización o ningún límite asintótico.
