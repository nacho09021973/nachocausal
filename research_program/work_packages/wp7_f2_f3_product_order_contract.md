# WP7 — Contrato `F2 => F3` o contraejemplo en `d=2`

```text
ESTADO: CONTRATO FORMAL v1.5 / P1--P4 PROBADAS / P5.2-O1--O5 CERRADAS / P5.2 PASS_WITH_SCOPE
PENDIENTE LITERAL: CURVATURE_NORM_UNDEFINED + REGIONAL_SCOPE_NOT_LITERAL; O4--O5 cerradas
FECHA: 2026-08-09
RAMA: research/f2-f3-chain-distance
NATURALEZA: combinatoria + bibliografía; cero simulación, cero semillas, sello intacto
NO ABRE: order-number-scale-limits, localizadores de horizonte ni una línea Weyl
```

## 0. Pregunta única y resultado admisible

Madsen separa en un embedding bien condicionado: **F1**, preservación exacta del
orden; **F2**, control uniforme de cuentas en diamantes mesoscópicos; y **F3**,
aproximación de tiempo propio por cadenas máximas. Declara abierta la relación lógica
entre F1--F2 y F3. Este WP decide primero la especialización plana `1+1`:

> ¿El orden producto y la discrepancia rectangular de F2 fuerzan la escala correcta de
> la cadena creciente más larga, o existe una sucesión con F2 y distancias de cadena
> macroscópicamente equivocadas?

Solo son terminales científicos válidos una demostración con cuantificadores, un
contraejemplo con cuantificadores o un bloqueo matemático tipado. No se sustituye la
pregunta por la observación trivial de que `N` fija volumen cuando la densidad es conocida.

## 1. Modelo combinatorio y cuantificadores congelados

Sea `Q=[0,1]^2` y sea `P_n` un conjunto de `n` puntos en posición general. Se fija

\[
(u,v)\prec(u',v')\quad\Longleftrightarrow\quad u<u'\ \text{y}\ v<v'.
\]

La inclusión de `P_n` en `Q` induce exactamente este orden, de modo que F1 es automática
en el modelo reducido.

Para un rectángulo de ejes \(R=I\times J\), sean \(|R|=|I||J|\) y
\(N_n(R)=|P_n\cap R|\). Fijados \(A>0\) y \(K<\infty\), se define

\[
a_n=A\frac{(\log n)^2}{n},\qquad
\mathcal R_n=\{R\subseteq Q:\ |R|\ge a_n\}.
\]

Para F2 se adopta la convención estándar de discrepancia: `I` y `J` son intervalos
semiabiertos. Como `P_n` está en posición general, cambiar a intervalos cerrados altera
la cuenta de cualquier rectángulo en a lo sumo cuatro puntos; §3 absorbe también esa
convención. En F3, `R(x,y)` sí incluye sus dos extremos.

La versión `d=2` de F2 usada en este contrato es

\[
\tag{F2-2D}
\sup_{R\in\mathcal R_n}
\frac{|N_n(R)-n|R||}{\sqrt{n|R|\log n}}\le K.
\]

Es deliberadamente más fuerte que pedirla solo en los diamantes interiores de Madsen:
un contraejemplo aquí seguirá siéndolo para cualquier subfamilia que contenga el diamante
testigo, una vez cerrado el puente geométrico `P5` de §3.

Ordenando por \(u\), los rangos de \(v\) forman una permutación \(\pi_n\); la altura de
\(P_n\cap R\) es la LIS de la subpermutación restringida a \(R\). Para \(x\prec y\) en
\(P_n\), escribimos \(R(x,y)=[u_x,u_y]\times[v_x,v_y]\) y \(H_n(x,y)\) para la
longitud de la cadena más larga entre ambos, incluidos los extremos. En la convención
plana `ds^2=du dv`, el
benchmark `fixed_n` es `2 sqrt(n|R|)`.

La conclusión cualitativa que se intentaría deducir es

\[
\tag{F3-2D}
E_n(P_n):=
\sup_{\substack{x\prec y\\R(x,y)\in\mathcal R_n}}
\left|\frac{H_n(x,y)}{2\sqrt{n|R(x,y)|}}-1\right|\longrightarrow0.
\]

El problema queda formalmente partido en alternativas exhaustivas:

- **Implicación:** para todo `A,K` existe `eta_n(A,K)->0` tal que toda sucesión que
  satisface `F2-2D(A,K)` cumple `E_n<=eta_n` para `n` suficientemente grande.
- **Contraejemplo fuerte:** existen `A,K,delta>0`, una subsucesión `n_j->infty`,
  configuraciones `P_{n_j}` que satisfacen F2-2D y pares `x_j prec y_j` admisibles con
  `E_{n_j}(P_{n_j})>=delta`.

La tasa cuantitativa exacta de F3 en Madsen es un segundo problema. Una violación de esa
tasa con `E_n->0` se etiquetará `RATE_ONLY`; no se venderá como distancia asintóticamente
equivocada.

## 2. Reducción `diamante <-> rectángulo <-> LIS`

En coordenadas nulas planas:

| Geometría `1+1` | Combinatoria |
|---|---|
| relación causal | orden producto |
| diamante de Alexandrov | rectángulo de ejes |
| volumen del diamante | área del rectángulo, salvo convención fija |
| F2 | discrepancia uniforme de cuentas rectangulares |
| cadena causal máxima | LIS de la permutación de rangos |
| tiempo propio | `sqrt(area)` en la convención fijada |

El contrato trabaja primero en `fixed_n`. Poissonizar, ajustar la constante de volumen y
colocar el testigo en el interior profundo de una variedad globalmente hiperbólica forman
el puente `P5`; no se dan por automáticos.

## 3. Lema de cadena plantada bajo la tolerancia exacta de F2-2D

`[PROVED — P1--P4; P5 probado bajo lectura regional / alcance literal abierto]`

> **Lema.** Para todo `A>0`, `K>0` y `a>2` existen una subsucesión
> `n_m -> infinity` y configuraciones `P_{n_m}` en posición general que satisfacen
> `F2-2D(A,K)` para todo `m` suficientemente grande, pero para las que
>
> \[
> E_{n_m}(P_{n_m})\ge \delta_a:=\frac{a-2}{4}>0.
> \]
>
> De hecho, el cociente de discrepancia de F2 tiende uniformemente a cero sobre
> `mathcal R_{n_m}` aunque la configuración contiene una cadena de longitud
> `(a+o(1)) sqrt(n_m)` entre dos elementos comparables.

### 3.1 Construcción y fondo cuasiuniforme — P1

Sea `N_m=4^m`. Tome el conjunto de Hammersley en base dos

\[
\mathsf H_N=
\left\{\left(\frac{j}{N},\phi_2(j)\right):0\le j<N\right\},
\]

donde `phi_2` es la inversa radical binaria. El Teorema 3.46 de
Dick--Pillichshammer, especializado a `s=2`, `b_1=2`, da

\[
N D_N^*(\mathsf H_N)\le \log_2N+4.
\]

Por inclusión--exclusión de cuatro rectángulos anclados, para todo rectángulo de ejes
`R` de área `r` se sigue

\[
\tag{3.1}
\bigl|\#(\mathsf H_N\cap R)-Nr\bigr|
\le 4\log_2N+16.
\]

Retire el punto `(0,0)` y escriba
\(B_N=\mathsf H_N\setminus\{(0,0)\}\). Entonces

\[
\tag{3.2}
\bigl|\#(B_N\cap R)-(N-1)r\bigr|
\le 4\log_2N+17.
\]

Esto cierra P1 de forma determinista y con margen `O(log N)`, sin cota VC, aleatoriedad
ni selección posterior.

### 3.2 Todos los rectángulos, incluidos los alargados — P2

Fije un irracional `theta` con `-1/2 < theta < 1/2`, ponga
\(k_m=\lceil a\sqrt{N_m}\rceil\) y, para un `m` fijo, abrevie
\(N=N_m\), \(k=k_m\). Defina

\[
t_j=\frac{j-1/2+\theta}{k},\qquad
\mathsf D_k=\{(t_j,t_j):1\le j\le k\}.
\]

Para \(R=I\times J\), sea \(L=I\cap J\). La discrepancia unidimensional de esta rejilla
trasladada cumple

\[
\bigl|\#\{j:t_j\in L\}-k|L|\bigr|\le2.
\]

Si `r=|I||J|`, tanto `|L|` como `r` pertenecen a `[0,sqrt(r)]`; por tanto
`||L|-r|<=sqrt(r)` y

\[
\tag{3.3}
\boxed{
\bigl|\#(\mathsf D_k\cap R)-kr\bigr|
\le k\sqrt r+2.}
\]

Con el tamaño total \(n=N+k+1\) de §3.3 y
\(k=\lceil a\sqrt N\rceil\le a\sqrt n+1\), esto da precisamente

\[
\tag{3.3a}
\boxed{
\bigl|\#(\mathsf D_k\cap R)-k|R|\bigr|
\le a\sqrt{n|R|}+3.}
\]

La cota no usa una razón de aspecto mínima: cubre simultáneamente rectángulos cuadrados,
pequeños y arbitrariamente alargados.

### 3.3 Combinación, constantes y escala mínima — P3

Añada los centinelas `S={(0,0),(1,1)}` y defina

\[
P_{n_m}=B_{N_m}\cup\mathsf D_{k_m}\cup S,
\qquad n_m=(N_m-1)+k_m+2=N_m+k_m+1.
\]

En las cotas siguientes se abrevian de nuevo `N=N_m`, `k=k_m`, `n=n_m`.

Las coordenadas de `B_N` son racionales y distintas por eje; las de `D_k` son
irracionales y distintas; los centinelas están en el borde. Luego `P_n` está en posición
general. Además \(|\#(S\cap R)-2r|\le2\). Sumando (3.2), (3.3) y esta última cota,
y usando \(k\le a\sqrt n+1\), se obtiene para **todo** rectángulo `R`, con cualquiera
de las convenciones de borde anteriores:

\[
\tag{3.4}
\bigl|\#(P_n\cap R)-nr\bigr|
\le 4\log_2 n+26+a\sqrt{nr}.
\]

Si `r>=A(log n)^2/n`, entonces

\[
\tag{3.5}
\frac{|\#(P_n\cap R)-nr|}{\sqrt{nr\log n}}
\le
\underbrace{\frac{a+4/(\sqrt A\log 2)}{\sqrt{\log n}}
+\frac{26}{\sqrt A(\log n)^{3/2}}}_{=:~\Psi_{A,a}(n)}.
\]

La cota es uniforme en `R` y `Psi_{A,a}(n)->0`. Para el `K>0` fijado en el lema,
tómese `m_0` tal que, para `m>=m_0`, se cumplan

\[
A(\log n_m)^2\le n_m,
\qquad \Psi_{A,a}(n_m)\le K.
\]

Ese es el rango admisible exacto: desde `m_0`, F2-2D vale con el mismo `K` fijo. En la
escala mínima, tanto el fondo `O(log n)` como la cadena `O(log n)` quedan por debajo de la
tolerancia `sqrt(A)(log n)^{3/2}` por el factor `O(1/sqrt(log n))`.

### 3.4 Fallo de F3 por factor constante — P4

Para `x=(0,0)` e `y=(1,1)`, `R(x,y)=Q` y la cadena que pasa por `D_k` tiene longitud
al menos `k+2`. Como `n=N+k+1` y `k=ceil(a sqrt(N))`, se tiene

\[
\liminf_{m\to\infty}\frac{H_{n_m}(x,y)}{2\sqrt{n_m}}
\ge\frac a2>1.
\]

Por la definición `delta_a=(a-2)/4`, para `m` suficientemente grande
`E_{n_m}(P_{n_m})>=delta_a`. Esto cierra P4 y prueba el lema. No se ha usado simulación.

### 3.5 Estado de las obligaciones

| ID | Estado | Evidencia |
|---|---|---|
| P1 | `PROVED` | Hammersley + (3.1)--(3.2) |
| P2 | `PROVED` | reducción exacta a \(I\cap J\), (3.3), sin restricción de aspecto |
| P3 | `PROVED` | posición general, cardinalidad exacta y cota uniforme (3.4)--(3.5) |
| P4 | `PROVED` | par de centinelas y límite inferior `a/2` |
| P5 | `PROVED_UNDER_SCOPED_READINGS / LITERAL_SCOPE_OPEN` | P5.1 da la estabilidad; P5.2-O1--O5 realizan todas sus hipótesis en de Sitter planar. Las reservas literales son la norma de curvatura no especificada y la versión regional incompleta de la Def. 2.6 |

Tras la auditoría P5.2, el terminal literal continúa siendo
`PRODUCT_ORDER_COUNTEREXAMPLE_PROVED_P5_OPEN`, pero solo por dos cuestiones de alcance
de la fuente: la norma de curvatura no está especificada y la versión regional completa de
la Def. 2.6 no está formulada literalmente en Madsen. Bajo cualquiera de las dos normas
estándar auditadas y la lectura regional explícita de §5, P5 queda matemáticamente probado.
No se declara `COUNTEREXAMPLE_F1_F2_NOT_F3_D2` sin esos sufijos de alcance.

## 4. P5.1 — Estabilidad de F2 bajo una cadena mesoscópica plantada

**Estado histórico de esta etapa: PROVED_CONDITIONAL / CYLINDER_SCALE_MISMATCH.**

Esta sección audita únicamente el mecanismo de perturbación contra la Def. 2.6 y el
Lema 5.2 de Madsen. No prueba todavía que exista una geometría que satisfaga simultáneamente
todos sus cuantificadores.

### 4.1 Lectura regional y margen del fondo

La Def. 2.6 usa \(V_M<\infty\). Para un espaciotiempo no compacto, la Remark 5.4 fija una
región precompacta \(K\subset M\), restringe el causal set a \(C_K\) y reemplaza \(V_M\)
por \(V_K\). Adoptamos provisionalmente esa lectura regional y ponemos

\[
\mathcal N_\rho:=\rho V_K,\qquad
\tau_{\min}=c_*^{-1}\rho^{-1/2}\log\mathcal N_\rho
\quad(d=2).
\]

El Lema 5.2 permite elegir una realización Poisson \(\Pi_\rho\) que satisface F1--F2 con
una constante fija \(K_{\rm bg}\), para \(\rho\) suficientemente grande. La perturbación
necesita margen: se fija desde el principio otra constante

\[
K_2>K_{\rm bg}.
\]

No basta partir de una realización que solo se sabe situada exactamente en el borde
\(K_2\).

### 4.2 Lema condicional de estabilidad

Suponga que la región contiene un diamante interior \(D_0\) de altura propia fija
\(\tau_0\in(0,c_*\lambda)\) y una geodésica timelike \(\gamma\) entre sus puntas. Suponga
además que todo diamante F2-admisible \(D\) satisface la cota de traza plana

\[
\tag{P5.1-G}
\operatorname{len}_g(\gamma\cap D)
\le \sqrt{2\,\operatorname{Vol}_g(D)}.
\]

En Minkowski \(1+1\), antes de cualquier envolvimiento espacial, esto es exacto:
\(\operatorname{Vol}(D)=\tau(D)^2/2\) y la intersección con una recta timelike es un
intervalo de longitud a lo sumo \(\tau(D)\).

Fije \(A>1\), ahora como amplitud de la cadena y sin relación con el parámetro \(A\)
de §1, y plante sobre \(\gamma\), incluidos sus extremos,

\[
k_\rho=\left\lceil A\sqrt{m_2\rho}\,\tau_0\right\rceil
\]

puntos equiespaciados, y llame \(\Gamma_\rho\) a ese conjunto. Para cualquier diamante
admisible \(D\), la discrepancia de una rejilla unidimensional da

\[
\begin{aligned}
\#(\Gamma_\rho\cap D)
&\le A\sqrt{m_2\rho}\,
       \operatorname{len}_g(\gamma\cap D)+2\\
&\le A\sqrt{2m_2}\,
       \sqrt{\rho\,\operatorname{Vol}_g(D)}+2.
\end{aligned}
\tag{P5.1-1}
\]

Sea \(P_\rho=\Pi_\rho\cup\Gamma_\rho\), con el orden causal inducido. F1 sigue siendo
exacta. Sumando la cota F2 del fondo y (P5.1-1),

\[
\frac{\bigl|\#(P_\rho\cap D)-\rho\operatorname{Vol}_g(D)\bigr|}
{\sqrt{\rho\operatorname{Vol}_g(D)\log\mathcal N_\rho}}
\le K_{\rm bg}
+\frac{A\sqrt{2m_2}}{\sqrt{\log\mathcal N_\rho}}
+\frac{2}{\sqrt{\rho\operatorname{Vol}_g(D)\log\mathcal N_\rho}}.
\tag{P5.1-2}
\]

En la escala mínima, usando
\(\operatorname{Vol}_g(D)=\tau(D)^2/2\) en la región plana,

\[
\rho\operatorname{Vol}_g(D)
\ge \frac{\log^2\mathcal N_\rho}{2c_*^2}.
\]

Por tanto el último término de (P5.1-2) es a lo sumo
\(2\sqrt2\,c_*/\log^{3/2}\mathcal N_\rho\), y

\[
\Xi_A(\rho):=
\frac{A\sqrt{2m_2}}{\sqrt{\log\mathcal N_\rho}}
+\frac{2\sqrt2\,c_*}{\log^{3/2}\mathcal N_\rho}
\longrightarrow0.
\tag{P5.1-3}
\]

Elegir \(\rho_0\) con
\(\Xi_A(\rho)\le K_2-K_{\rm bg}\) para \(\rho\ge\rho_0\) prueba, bajo
(P5.1-G) y la lectura regional anterior, que \(P_\rho\) satisface F2 con la misma
constante final \(K_2\). El factor decisivo vuelve a ser
\(1/\sqrt{\log\mathcal N_\rho}\), uniformemente hasta \(\tau_{\min}\).

### 4.3 Testigo F3 y convenciones de \(m_2\)

Tome como \(x_\rho,y_\rho\) los extremos plantados. Tanto si la longitud de cadena cuenta
vértices como si cuenta enlaces, la diferencia es a lo sumo uno y

\[
\frac{\ell_{P_\rho}(x_\rho,y_\rho)}{\sqrt{m_2\rho}}
\ge A\tau_0-o(1).
\tag{P5.1-4}
\]

En la normalización estándar de Minkowski \(1+1\),
\(\operatorname{Vol}(D_\tau)=\tau^2/2\) y la altura asintótica es
\(2\sqrt{\rho\operatorname{Vol}(D_\tau)}=\sqrt{2\rho}\,\tau\). Comparando con la
ecuación (45) de Madsen se obtiene \(m_2=2\). La convención vértices/enlaces solo altera
(P5.1-4) en \(O(\rho^{-1/2})\).

Si \(\tau_0=\varepsilon\lambda\), \(0<\varepsilon<c_*\), el lado derecho de F3 para
este par es

\[
C_2\left(
\varepsilon^2+
\frac{\log^{3/2}\mathcal N_\rho}{\mathcal N_\rho^{1/4}}
\right)\tau_0.
\]

Así, siempre que

\[
\tag{P5.1-5}
A-1>C_2\varepsilon^2,
\]

la desigualdad F3 completa falla para \(\rho\) suficientemente grande. El término
estadístico tiende a cero y el margen estricto absorbe la ambigüedad \(O(1)\) en la
longitud de cadena.

### 4.4 Auditoría binaria de la realización cilíndrica

| Condición | Veredicto | Razón |
|---|---|---|
| región precompacta | PASS_WITH_SCOPE | la Remark 5.4 autoriza \(K\) y \(V_K\), pero no reescribe literalmente todos los cuantificadores de la Def. 2.6; P5 debe fijar que solo se exigen diamantes completos en el interior regional |
| \(\lambda=L/2\) en \(\mathbb R\times S^1_L\) | FAIL_AS_STATED | \(L/2\) es la inyectividad del auxiliar estándar, no el supremo de la ecuación (1) |
| \(m_2\) y longitud de cadena | PASS_ASYMPTOTIC | \(m_2=2\) con \(\operatorname{Vol}(D_\tau)=\tau^2/2\); contar vértices o enlaces cambia \(O(1)\) |

El fallo de la segunda fila es literal. Para
\(g=-dt^2+dx^2\) y el campo constante
\(T_\eta=(\cosh\eta,\sinh\eta)\), la métrica auxiliar satisface

\[
h_{T_\eta}(\partial_x,\partial_x)
=1+2\sinh^2\eta=\cosh(2\eta).
\]

Si \(L\) denota la circunferencia espacial, entonces

\[
\operatorname{inj}(M,h_{T_\eta})
=\frac L2\sqrt{\cosh(2\eta)}\longrightarrow\infty.
\]

Como la curvatura del cilindro plano es nula y la Def. 2.6 toma el supremo sobre todos
los campos timelike unitarios, su \(\lambda\) literal es infinito, no \(L/2\). Esto vuelve
inservible la elección \(\tau_0=\varepsilon\lambda\) y no permite identificar el rango
local no envuelto con \([\tau_{\min},c_*\lambda]\).

**Estado de P5.1.** La estabilidad F2 y el mecanismo de violación F3 están probados
condicionalmente por (P5.1-1)--(P5.1-5). La realización propuesta en el cilindro plano no
cierra P5 bajo la definición literal. El siguiente subproblema queda reducido a una elección
geométrica con \(0<\lambda<\infty\), región plana o uniformemente controlada que satisfaga
una versión de (P5.1-G), y un diamante testigo profundo. Ese era el bloqueo antes de P5.2;
§5 lo resuelve con de Sitter planar, sujeto al alcance regional allí tipado.

## 5. P5.2 — Auditoría de de Sitter planar

**Estado: P5_2_PASS_WITH_SCOPE / O1_PROVED / O2_PASS_WITH_NORM_SCOPE /
O3_PASS_WITH_REGIONAL_SCOPE / O4_PROVED / O5_PROVED.**

La ampliación firmada en
`docs/program_reopening_note_2026-08-09_P5_2.md` autoriza como candidato único

\[
M_\ell=(-\infty,0)_\eta\times\mathbb R_x,
\qquad
g=\frac{\ell^2}{\eta^2}(-d\eta^2+dx^2),
\qquad \ell>0.
\]

Se elige la orientación temporal en la que \(\eta\) crece hacia el futuro. Las
subsecciones siguientes resuelven O1--O5. El valor numérico exacto de \(\lambda\) queda
condicionado por una convención de norma ausente en Madsen, y O3 conserva por separado
el alcance regional que la Remark 5.4 no formula con todos los cuantificadores.

### 5.1 O1 — Hiperbolicidad global y campo auxiliar admisible

> **Lema P5.2-O1.** El parche \((M_\ell,g)\) es globalmente hiperbólico. La función
>
> \[
> t(\eta,x)=-\ell\log(-\eta/\ell)
> \]
>
> es un tiempo de Cauchy suave y el campo
>
> \[
> T=-\nabla t=-\frac{\eta}{\ell}\,\partial_\eta
> \]
>
> es suave, futuro, timelike y unitario. Por tanto es una elección admisible en la
> Construction 2.3 y en la ecuación (1) de la Def. 2.6 de Madsen. Su métrica auxiliar es
>
> \[
> h_T=g+2T^\flat\otimes T^\flat
> =\frac{\ell^2}{\eta^2}(d\eta^2+dx^2)
> =dt^2+e^{2t/\ell}dx^2.
> \]

**Prueba.** El factor conforme \(\ell^2/\eta^2\) es suave y positivo, de modo que
\((M_\ell,g)\) tiene los mismos conos y las mismas curvas causales que el semiplano
\(\eta<0\) de Minkowski. Para una curva causal futura, parametrizada por \(\eta\) donde
sea regular,

\[
\left|\frac{dx}{d\eta}\right|\le1.
\tag{P5.2-1}
\]

Si una curva causal inextendible tuviera un extremo de su rango de \(\eta\) en un valor
finito interior \(\eta_*<0\), (P5.2-1) haría que \(x\) tuviera un límite finito al
aproximarse a \(\eta_*\). La curva podría entonces prolongarse hasta
\((\eta_*,x_*)\in M_\ell\), contradicción. Por tanto el rango de \(\eta\) de toda curva
causal inextendible es \((-\infty,0)\). Como \(\eta\) es estrictamente creciente en toda
curva causal futura no constante, cada hipersuperficie
\(\Sigma_{\eta_0}=\{\eta=\eta_0\}\) la corta exactamente una vez. Estas
\(\Sigma_{\eta_0}\) son superficies de Cauchy.

Además, para \(p=(\eta_p,x_p)\preceq q=(\eta_q,x_q)\), el diamante causal es

\[
\begin{split}
J^+(p)\cap J^-(q)=\{(\eta,x):\;&\eta_p\le\eta\le\eta_q,\\
&|x-x_p|\le\eta-\eta_p,\quad
|x-x_q|\le\eta_q-\eta\}.
\end{split}
\tag{P5.2-2}
\]

Es cerrado y acotado en \(\mathbb R^2\), y queda separado de \(\eta=0\) porque
\(\eta\le\eta_q<0\); luego es compacto y está contenido en \(M_\ell\). Esto verifica
literalmente los dos requisitos de hiperbolicidad global usados en la Def. 2.2 de
Madsen.

Finalmente,

\[
\frac{dt}{d\eta}=-\frac\ell\eta,
\qquad
g^{-1}(dt,dt)=-1,
\qquad
\nabla t=\frac\eta\ell\partial_\eta.
\]

Así, \(T=-\nabla t=-(\eta/\ell)\partial_\eta\) es unitario y futuro, y
\(T^\flat=(\ell/\eta)d\eta\). La expresión anunciada para \(h_T\) se obtiene por
sustitución directa; es suave y definida positiva en todo el parche. Como sus niveles
de \(t\) son precisamente las superficies de Cauchy anteriores, esta elección es del
tipo exigido por la Construction 2.3. \(\square\)

| Subobligación de O1 | Estado | Evidencia |
|---|---|---|
| superficie de Cauchy global | `PROVED` | argumento de extensión mediante (P5.2-1) |
| diamantes causales compactos | `PROVED` | descripción cerrada y acotada (P5.2-2) |
| campo timelike unitario admisible | `PROVED` | \(T=-\nabla t\), con \(g(T,T)=-1\) |
| métrica auxiliar global | `PROVED` | \(h_T=\ell^2\eta^{-2}(d\eta^2+dx^2)\) |

**Corte de O1.** P5.2-O1 queda probada. La inyectividad de \(h_T\), la norma de
curvatura que entra en (1) y el supremo sobre todos los campos unitarios se auditan
separadamente en O2.

### 5.2 O2 — Escala de curvatura y máximo sobre campos timelike

**Veredicto: `PASS_WITH_NORM_SCOPE`.** La v1 de Madsen define

\[
\tag{P5.2-3}
\lambda=\sup_S\min\!\left(
\operatorname{inj}(M_\ell,h_S),
|\operatorname{Rm}[g]|^{-1/2}
\right),
\]

con \(S\) recorriendo los campos timelike unitarios suaves. No define, ni en la Def. 2.6
ni en su glosario, la norma tensorial o el supremo espacial implícitos en
\(|\operatorname{Rm}[g]|\). La Remark 4.7 distingue expresamente
\(\operatorname{Rm}[g]\) de \(\operatorname{Rm}[h_S]\), pero tampoco fija esa
convención. Por ello no se asigna a \(\lambda\) una constante numérica única.

> **Lema P5.2-O2.** Bajo cualquiera de las dos lecturas estándar siguientes,
>
> 1. norma Hilbert--Schmidt positiva de \(\operatorname{Rm}[g]\) inducida por \(h_S\), o
> 2. norma de operador, equivalentemente la cota de curvatura seccional en este caso,
>
> la magnitud \(|\operatorname{Rm}[g]|\) es positiva, finita y no depende de \(S\).
> El campo \(T\) de O1 realiza el supremo de (P5.2-3), que es por tanto un máximo, y
>
> \[
> \lambda=|\operatorname{Rm}[g]|^{-1/2}
> =c_{\rm norm}\ell,
> \qquad 0<c_{\rm norm}<\infty.
> \]
>
> En concreto, \(c_{\rm norm}=1/\sqrt2\) para Hilbert--Schmidt y
> \(c_{\rm norm}=1\) para la norma de operador.

**Prueba.** Escribiendo \(y=-\eta>0\), el auxiliar construido en O1 es

\[
h_T=\frac{\ell^2}{y^2}(dy^2+dx^2),
\tag{P5.2-4}
\]

la métrica completa y simplemente conexa del semiplano hiperbólico, con curvatura
seccional \(-1/\ell^2\). Por Cartan--Hadamard su aplicación exponencial es un
difeomorfismo en cada punto, no hay cut locus y

\[
\operatorname{inj}(M_\ell,h_T)=\infty.
\tag{P5.2-5}
\]

La métrica lorentziana de de Sitter tiene curvatura seccional constante
\(+1/\ell^2\), luego

\[
R_{abcd}=\frac1{\ell^2}
\left(g_{ac}g_{bd}-g_{ad}g_{bc}\right).
\tag{P5.2-6}
\]

Para cualquier campo timelike unitario \(S\), complete \(e_0=S\) a una base
\(g\)-ortonormal \((e_0,e_1)\). Esa misma base es \(h_S\)-ortonormal. La forma
(P5.2-6) tiene en toda base adaptada los mismos cuatro componentes no nulos, de módulo
\(1/\ell^2\). Por tanto

\[
|\operatorname{Rm}[g]|_{h_S}^2
=\frac4{\ell^4},
\qquad
|\operatorname{Rm}[g]|_{h_S}=\frac2{\ell^2},
\tag{P5.2-7}
\]

independientemente de \(S\). En la lectura de operador, la magnitud es en cambio
\(1/\ell^2\), también independiente de \(S\).

Llame \(q_\ell\) a cualquiera de esas dos magnitudes. Para todo \(S\),

\[
\min\!\left(\operatorname{inj}(M_\ell,h_S),q_\ell^{-1/2}\right)
\le q_\ell^{-1/2}.
\tag{P5.2-8}
\]

Por (P5.2-5), el campo \(T\) de O1 alcanza la igualdad. Así se elimina el supremo sin
necesidad de controlar ningún otro campo: es un máximo y vale \(q_\ell^{-1/2}\).
Las dos convenciones dan respectivamente \(\ell/\sqrt2\) y \(\ell\). \(\square\)

| Subobligación de O2 | Estado | Evidencia |
|---|---|---|
| completitud e inyectividad del auxiliar de O1 | `PROVED` | (P5.2-4)--(P5.2-5), Cartan--Hadamard |
| curvatura lorentziana positiva y finita | `PROVED` | forma de espacio constante (P5.2-6) |
| independencia respecto de \(S\) en las dos normas estándar | `PROVED` | base adaptada y (P5.2-7) |
| el supremo es un máximo | `PROVED` | cota (P5.2-8), alcanzada por \(T\) |
| constante numérica única | `UNDEFINED_IN_SOURCE` | Madsen v1 no especifica la norma de \(\operatorname{Rm}[g]\) |

**Corte tras O2.** La obligación autorizada \(0<\lambda<\infty\) queda satisfecha y la
optimización sobre campos queda cerrada. El alcance `WITH_NORM_SCOPE` conserva la única
ambigüedad real: \(\lambda=\ell/\sqrt2\) o \(\ell\) bajo las dos convenciones auditadas.
O3--O5 se auditan en las subsecciones siguientes.

### 5.3 O3 — Región precompacta y diamante testigo profundo

**Veredicto: `O3_PASS_WITH_REGIONAL_SCOPE`.** La existencia geométrica, la profundidad
y el rango mesoscópico se prueban con todos sus cuantificadores. El sufijo de alcance es
necesario porque la Remark 5.4 de Madsen sustituye explícitamente \(V_M\) por \(V_K\) y
restringe el causal set a \(C_K\), pero no reescribe literalmente el dominio universal
de diamantes de la Def. 2.6 ni su referencia a \(M\) y \(\partial M\).

> **Lema P5.2-O3.** Fije \(\ell>0\), una constante de norma
> \(c_{\rm norm}\in(0,\infty)\),
> \(\lambda=c_{\rm norm}\ell\), \(c_*\in(0,1)\) y
> \(\varepsilon\in(0,c_*)\). En coordenadas cósmicas considere
>
> \[
> g=-dt^2+e^{2t/\ell}dx^2,
> \qquad
> h_T=dt^2+e^{2t/\ell}dx^2,
> \qquad z_0=(0,0).
> \]
>
> Ponga
>
> \[
> \tau_0=\varepsilon\lambda,
> \qquad p=(-\tau_0/2,0),
> \qquad q=(\tau_0/2,0),
> \qquad D_0=J^+(p)\cap J^-(q).
> \]
>
> Entonces \(\gamma(s)=(s,0)\),
> \(s\in[-\tau_0/2,\tau_0/2]\), es una geodésica timelike unitaria
> maximizante, \(\tau_g(p,q)=\tau_0\), \(D_0\) es compacto y
>
> \[
> r_0:=\max_{z\in D_0}d_{h_T}(z,z_0)<\infty.
> \]
>
> Para todo \(R>r_0+c_*\lambda\), la región
> \(K=B_R^{h_T}(z_0)\) cumple
>
> \[
> \overline K\ \text{compacta},\qquad
> 0<V_K:=\operatorname{Vol}_g(K)<\infty,\qquad
> D_0\subset K,
> \qquad
> d_{h_T}(D_0,\partial K)>c_*\lambda.
> \]
>
> Fijados tal \(R\) y \(K\), existe \(\rho_0<\infty\) tal que, para
> todo \(\rho\ge\rho_0\),
>
> \[
> 0<\tau_{\min}(\rho)
> :=c_*^{-1}\rho^{-1/2}\log(\rho V_K)
> \le\tau_0<c_*\lambda.
> \]
>
> Por tanto \([\tau_{\min}(\rho),c_*\lambda]\) es no vacío y \(D_0\)
> es un diamante testigo profundo y admisible bajo la lectura regional que reemplaza
> \((M,V_M,\partial M)\) por \((K,V_K,\partial K)\).

**Prueba.** En las coordenadas dadas, \(g_{tt}=-1\),
\(g_{xx}=e^{2t/\ell}\) y todos los símbolos de Christoffel
\(\Gamma^\mu_{tt}\) se anulan. Por ello
\(\nabla_{\dot\gamma}\dot\gamma=0\) y
\(g(\dot\gamma,\dot\gamma)=-1\): la curva vertical es una geodésica timelike
unitaria y su longitud propia entre \(p\) y \(q\) es \(\tau_0\).

Falta justificar que esa longitud es la distancia propia máxima. Para toda curva causal
futura, localmente Lipschitz, \(\sigma(u)=(t(u),x(u))\) de \(p\) a \(q\), la
causalidad y la orientación temporal dan, casi en todo punto,

\[
\dot t\ge e^{t/\ell}|\dot x|,
\qquad
\sqrt{\dot t^{\,2}-e^{2t/\ell}\dot x^{\,2}}\le\dot t.
\tag{P5.2-9}
\]

Integrando (P5.2-9),

\[
L_g(\sigma)
\le\int\dot t\,du
=t(q)-t(p)=\tau_0.
\tag{P5.2-10}
\]

La curva \(\gamma\) alcanza la cota, luego el supremo que define la separación
lorentziana se alcanza y \(\tau_g(p,q)=\tau_0\). En particular, no se ha identificado
la longitud de una curva cualquiera con la distancia sin probar maximalidad.

Por O1 el parche es globalmente hiperbólico. Como \(p\preceq q\), la definición de
hiperbolicidad global aplicada al diamante completo da que \(D_0\) es compacto. La
función \(z\mapsto d_{h_T}(z,z_0)\) es continua, de modo que alcanza en \(D_0\) un
máximo finito; este es \(r_0\) (y coincide con el supremo solicitado).

Por O2, \((M_\ell,h_T)\) es el plano hiperbólico completo de curvatura
\(-1/\ell^2\). Hopf--Rinow implica que la bola cerrada
\(\overline B_R^{h_T}(z_0)\) es compacta; además es la clausura de \(K\). Los elementos
de volumen lorentziano y riemanniano coinciden:

\[
d\operatorname{Vol}_g=e^{t/\ell}\,dt\,dx
=d\operatorname{Vol}_{h_T}.
\tag{P5.2-11}
\]

En particular, usando el área de una bola hiperbólica,

\[
V_K=2\pi\ell^2\bigl(\cosh(R/\ell)-1\bigr),
\tag{P5.2-12}
\]

que es estrictamente positiva y finita. Para todo \(z\in D_0\),
\(d_{h_T}(z,z_0)\le r_0<R\), así que \(D_0\subset K\). Si
\(w\in\partial K\), entonces \(d_{h_T}(z_0,w)=R\), y la desigualdad triangular da

\[
d_{h_T}(z,w)
\ge R-d_{h_T}(z,z_0)
\ge R-r_0>c_*\lambda.
\tag{P5.2-13}
\]

Tomando el ínfimo en \(z\in D_0\), \(w\in\partial K\), se obtiene el margen estricto
anunciado, que en particular implica la desigualdad no estricta exigida por la Def. 2.6.

Finalmente, para el \(V_K\) fijo y positivo de (P5.2-12),

\[
c_*^{-1}\rho^{-1/2}\log(\rho V_K)
=c_*^{-1}\frac{\log\rho+\log V_K}{\sqrt\rho}
\longrightarrow0.
\tag{P5.2-14}
\]

Elija primero \(\rho_1>V_K^{-1}\), para que \(\tau_{\min}(\rho)>0\) cuando
\(\rho\ge\rho_1\). Por (P5.2-14) existe \(\rho_2<\infty\) tal que
\(\tau_{\min}(\rho)\le\tau_0\) para todo \(\rho\ge\rho_2\). Con
\(\rho_0=\max(\rho_1,\rho_2)\), y usando
\(\tau_0=\varepsilon\lambda<c_*\lambda\), quedan probados simultáneamente todos los
cuantificadores sobre \(\rho\) y la no vacuidad del rango mesoscópico. \(\square\)

#### Auditoría literal del alcance regional

La Def. 2.6 de Madsen cuantifica F2 sobre **todo** diamante causal
\(D=J_g^+(p)\cap J_g^-(q)\subset M\) en el rango admisible, usa \(V_M\) en
\(\tau_{\min}\) y en la tolerancia, y mide la profundidad respecto de
\(\partial M\). La Remark 5.4, para un \(M\) no compacto, dice explícitamente que se
fije una región precompacta \(K\subset M\) de volumen \(V_K\), se restrinja el causal
set a \(C_K=f^{-1}(K)\) y se aplique el Theorem 4.18 con \(V_M\) reemplazado por
\(V_K\). También formula una conclusión sobre \(K^\circ\).

La Remark 5.4 **no** dice literalmente que se reemplace \(M\) por \(K\) en la
Def. 2.6, que \(\partial M\) pase a ser \(\partial K\), ni que el cuantificador
universal de F2 se restrinja a diamantes completos contenidos en \(K\); tampoco indica
que \(\lambda\) deba recalcularse para \(K\) en vez de conservar la escala ambiente de
\(M_\ell\). Mantener ese cuantificador sobre todo \(M_\ell\) mientras se cuenta solo
\(C_K\) produciría, de hecho, diamantes exteriores sin puntos de \(C_K\); por tanto la
lectura regional exige alguna restricción de dominio, pero el texto citado no especifica
literalmente cuál. No se completa esa omisión por inferencia silenciosa.

| Subobligación de O3 | Estado | Evidencia |
|---|---|---|
| geodésica vertical timelike y unitaria | `PROVED` | \(\Gamma^\mu_{tt}=0\) y normalización de \(\dot\gamma\) |
| maximalidad y \(\tau_g(p,q)=\tau_0\) | `PROVED` | cota para toda curva causal (P5.2-9)--(P5.2-10) |
| compacidad de \(D_0\) y finitud de \(r_0\) | `PROVED` | hiperbolicidad global de O1 y continuidad de \(d_{h_T}\) |
| precompacidad de \(K\) | `PROVED` | completitud de \(h_T\) y Hopf--Rinow |
| \(0<V_K<\infty\) | `PROVED` | (P5.2-11)--(P5.2-12) |
| \(D_0\subset K\) y margen de frontera | `PROVED` | elección de \(R\) y (P5.2-13) |
| \(\exists\rho_0<\infty\;\forall\rho\ge\rho_0\): rango no vacío | `PROVED` | límite (P5.2-14) y \(\varepsilon<c_*\) |
| sustitución \(V_M\mapsto V_K\) y restricción \(C\mapsto C_K\) | `LITERAL_IN_REMARK_5.4` | texto expreso de la Remark 5.4 |
| sustitución \((M,\partial M)\mapsto(K,\partial K)\), escala \(\lambda\) y dominio de todos los diamantes | `REGIONAL_SCOPE_NOT_LITERAL` | esos cuantificadores no se reescriben en la Remark 5.4 |

**Corte tras O3.**

```text
O3_PASS_WITH_REGIONAL_SCOPE
P5_AT_THIS_CUT: OPEN
O4--O5_AT_THIS_CUT: NOT_AUDITED
```

La construcción geométrica de O3 no falla: lo único condicionado es llamarla
literalmente una instancia de todos los cuantificadores regionales de la Def. 2.6. En este
corte intermedio aún no se promovía P5; O4--O5 se resuelven a continuación.

### 5.4 O4 — Volumen de diamantes y traza sobre la geodésica plantada

**Veredicto: `O4_PROVED`.** La cota necesaria no requiere aproximar la métrica por
Minkowski: en de Sitter planar el volumen de un diamante admite una fórmula exacta, y la
cota de intersección se sigue de la desigualdad triangular inversa para la distancia
lorentziana.

> **Lema P5.2-O4.** Sea
>
> \[
> \beta:=\frac{c_*\lambda}{2\ell}>0,
> \qquad
> \kappa_\beta:=\frac{\log\cosh \beta}{\beta^2}\in(0,1/2).
> \]
>
> Para todo diamante causal timelike completo
> \(D=J^+(a)\cap J^-(b')\subset M_\ell\), de altura
> \(\tau=\tau_g(a,b')\in(0,c_*\lambda]\), se tiene
>
> \[
> \operatorname{Vol}_g(D)
> =4\ell^2\log\cosh\!\left(\frac{\tau}{2\ell}\right),
> \tag{P5.2-15}
> \]
>
> y, uniformemente en la posición y la inclinación de \(D\),
>
> \[
> \boxed{
> \kappa_\beta\tau^2
> \le \operatorname{Vol}_g(D)
> \le \frac{\tau^2}{2}.}
> \tag{P5.2-16}
> \]
>
> Si \(\gamma_0=\gamma|_{[-\tau_0/2,\tau_0/2]}\) es el segmento plantado de O3,
> entonces
>
> \[
> \boxed{
> \operatorname{len}_g(\gamma_0\cap D)
> \le \tau
> \le \kappa_\beta^{-1/2}\sqrt{\operatorname{Vol}_g(D)}.}
> \tag{P5.2-17}
> \]

**Prueba de la fórmula de volumen.** Use las coordenadas nulas
\(u=\eta+x\), \(v=\eta-x\). Para \(a=(u_a,v_a)\ll
b'=(u_{b'},v_{b'})\), el diamante es el rectángulo

\[
D=[u_a,u_{b'}]\times[v_a,v_{b'}],
\qquad
d\operatorname{Vol}_g=\frac{2\ell^2}{(u+v)^2}\,du\,dv.
\]

Todo el rectángulo satisface \(u+v=2\eta<0\), de modo que la integral es regular. Si
\(a=(\eta_a,x_a)\), \(b'=(\eta_{b'},x_{b'})\) y
\(\Delta x=x_{b'}-x_a\), la integración directa da

\[
\operatorname{Vol}_g(D)
=2\ell^2\log\!\left(
\frac{\bigl((\eta_a+\eta_{b'})^2-(\Delta x)^2\bigr)}
{4\eta_a\eta_{b'}}
\right).
\tag{P5.2-18}
\]

Para fijar también la relación con la distancia propia, embeba el parche en
\(\mathbb R^{1,2}\), con producto de signo \((-++)\), mediante

\[
X^0=\frac{\eta^2-x^2-\ell^2}{2\eta},
\qquad
X^1=-\frac{\ell x}{\eta},
\qquad
X^2=\frac{\eta^2-x^2+\ell^2}{2\eta}.
\]

Entonces \(-\left(X^0\right)^2+\left(X^1\right)^2+
\left(X^2\right)^2=\ell^2\), la métrica inducida es \(g\), y el producto
ambiente normalizado de los dos extremos es

\[
Z(a,b')
=1+\frac{(\eta_{b'}-\eta_a)^2-(\Delta x)^2}
{2\eta_a\eta_{b'}}
=\cosh(\tau/\ell).
\]

La última igualdad es la parametrización por longitud propia de la geodésica timelike
obtenida al cortar el hiperboloide con el plano de los dos extremos y el origen. El arco
entre ellos es una combinación lineal de \(X(a)\) y \(X(b')\) con coeficientes positivos;
como el parche se caracteriza por \(X^0-X^2=-\ell^2/\eta>0\), el arco completo queda en
\(M_\ell\). Es el maximizante del modelo de hiperboloide y, al estar contenido en el
parche, realiza también su distancia intrínseca. Esto prueba la igualdad con
\(\cosh(\tau/\ell)\).

El argumento del logaritmo en (P5.2-18) es
\((1+Z)/2=\cosh^2(\tau/(2\ell))\), lo que prueba (P5.2-15) sin una
hipótesis de centrado ni de razón de aspecto.

**Comparación uniforme.** Para \(x\ge0\),
\(\log\cosh x\le x^2/2\), pues \(\tanh x\le x\). Además,
\(x\mapsto\log\cosh(x)/x^2\) es decreciente en \((0,\infty)\). En efecto,

\[
2\log\cosh x-x\tanh x\ge0,
\]

porque su derivada es \(\tanh x-x\operatorname{sech}^2x\), una función que parte de
cero y cuya derivada es \(2x\operatorname{sech}^2x\tanh x\ge0\). Aplicando estas dos
propiedades a \(x=\tau/(2\ell)\in(0,\beta]\) se obtiene (P5.2-16).

**Cota de traza.** La intersección de una curva causal con el conjunto causalmente
convexo \(D\) es un intervalo, posiblemente vacío o degenerado. Sean \(r\preceq s\)
sus extremos no degenerados sobre \(\gamma_0\). Entonces
\(a\preceq r\preceq s\preceq b'\), y la desigualdad triangular inversa da

\[
\tau_g(a,b')
\ge \tau_g(a,r)+\tau_g(r,s)+\tau_g(s,b')
\ge \tau_g(r,s).
\]

Por (P5.2-9)--(P5.2-10), cada subsegmento vertical de \(\gamma_0\) es maximizante, así
que \(\operatorname{len}_g(\gamma_0\cap D)=\tau_g(r,s)\le\tau\). La segunda
desigualdad de (P5.2-17) es (P5.2-16). Los casos vacío y degenerado son inmediatos.
\(\square\)

La constante \(\kappa_\beta\) es fija e independiente de \(\rho\), de \(D\) y de su
posición. Bajo las dos normas de O2,
\(\beta=c_*c_{\rm norm}/2\) vale respectivamente
\(c_*/(2\sqrt2)\) o \(c_*/2\); la ambigüedad de norma cambia la constante, no la
validez ni la uniformidad de O4.

### 5.5 O5 — Sustitución en F2 y violación de la desigualdad F3

**Veredicto matemático: `O5_PROVED`. Terminal de P5.2:
`P5_2_PASS_WITH_SCOPE`.** La sustitución cierra para cualquiera de las dos constantes de
norma de O2. El sufijo no procede de O4--O5: conserva la convención de norma no definida
en la fuente, tipada en O2, y la falta de una Def. 2.6 regional literal identificada en O3.

Fije \(\varepsilon\in(0,c_*)\), \(\tau_0=\varepsilon\lambda\), y denote por
\(C_2\) la constante dimensional de F3. Elija una amplitud fija

\[
A>1+C_2\varepsilon^2.
\tag{P5.2-19}
\]

Fije la región \(K\) de O3, escriba
\(\mathcal N_\rho=\rho V_K\), y adopte la lectura regional explícita allí declarada:
F2 se exige para los diamantes completos contenidos en el interior regional y con margen
respecto de \(\partial K\). Por la aplicación regional del Lema 5.2 de Madsen, para todo
\(\rho\) suficientemente grande se puede elegir una realización de fondo
\(\Pi_\rho\subset K\) que satisface F1--F2 con una constante fija
\(K_{\rm bg}\). Fije también \(K_2>K_{\rm bg}\).

Sobre \(\gamma_0\), incluidos \(p\) y \(q\), coloque

\[
k_\rho=\left\lceil A\sqrt{m_2\rho}\,\tau_0\right\rceil
\]

puntos equiespaciados y llame \(\Gamma_\rho\) al conjunto resultante. La realización
Poisson puede escogerse sin puntos sobre \(\gamma_0\), evento de probabilidad uno, así que
la unión \(P_\rho=\Pi_\rho\cup\Gamma_\rho\) no tiene colisiones. Se dota a
\(P_\rho\) del orden causal inducido; F1 es entonces exacta.

Para cualquier diamante F2-admisible \(D\), la discrepancia de una rejilla en un intervalo
y (P5.2-17) dan

\[
\begin{aligned}
\#(\Gamma_\rho\cap D)
&\le A\sqrt{m_2\rho}\,
       \operatorname{len}_g(\gamma_0\cap D)+2\\
&\le A\sqrt{\frac{m_2}{\kappa_\beta}}
       \sqrt{\rho\operatorname{Vol}_g(D)}+2.
\end{aligned}
\tag{P5.2-20}
\]

Sumando esta cota a F2 para el fondo,

\[
\frac{\left|\#(P_\rho\cap D)-\rho\operatorname{Vol}_g(D)\right|}
{\sqrt{\rho\operatorname{Vol}_g(D)\log\mathcal N_\rho}}
\le K_{\rm bg}
+\frac{A\sqrt{m_2/\kappa_\beta}}{\sqrt{\log\mathcal N_\rho}}
+\frac{2}{\sqrt{\rho\operatorname{Vol}_g(D)
                 \log\mathcal N_\rho}}.
\tag{P5.2-21}
\]

En la escala mínima, (P5.2-16) y la fórmula de \(\tau_{\min}\) implican

\[
\rho\operatorname{Vol}_g(D)
\ge \kappa_\beta\rho\tau_{\min}^2
=\frac{\kappa_\beta}{c_*^2}\log^2\mathcal N_\rho.
\]

Por tanto el exceso uniforme sobre \(K_{\rm bg}\) queda acotado por

\[
\Xi_A^{\rm dS}(\rho):=
\frac{A\sqrt{m_2/\kappa_\beta}}{\sqrt{\log\mathcal N_\rho}}
+\frac{2c_*}{\sqrt{\kappa_\beta}\,\log^{3/2}\mathcal N_\rho}
\longrightarrow0.
\tag{P5.2-22}
\]

Existe, pues, \(\rho_1<\infty\) tal que
\(\Xi_A^{\rm dS}(\rho)\le K_2-K_{\rm bg}\) para todo
\(\rho\ge\rho_1\). Esto prueba F2 con la misma constante final fija \(K_2\),
uniformemente hasta la escala mínima exacta de Madsen.

Resta F3. Sean \(x_\rho,y_\rho\) los elementos plantados en \(p,q\). El diamante
\(D_0\) es admisible y profundo por O3. Como \(\Gamma_\rho\) es una cadena,
y recordando \(m_2=2\), cualquier convención vértices/enlaces solo introduce un
término \(O(1)\), de modo que

\[
\frac{\ell_{P_\rho}(x_\rho,y_\rho)}{\sqrt{m_2\rho}}-\tau_0
\ge (A-1)\tau_0-o(1).
\tag{P5.2-23}
\]

En cambio, el lado derecho permitido por (5) de Madsen para este par es

\[
C_2\left(
\varepsilon^2+
\frac{\log^{3/2}\mathcal N_\rho}{\mathcal N_\rho^{1/4}}
\right)\tau_0.
\tag{P5.2-24}
\]

Ponga \(\mu=A-1-C_2\varepsilon^2>0\). El segundo término de (P5.2-24) tiende a
cero, y el \(o(1)\) de (P5.2-23), dividido por el \(\tau_0>0\) fijo, también. Para
\(\rho\) suficientemente grande, (P5.2-23) supera (P5.2-24) por un margen, por ejemplo,
de al menos \(\mu\tau_0/3\). Por consiguiente \(P_\rho\) viola la desigualdad F3
completa, no solo su tasa, mientras satisface F1--F2 con \(K_2\) fijo. \(\square\)

Todos los umbrales usados son simultáneos y finitos: se toma \(\rho\) por encima del
umbral de O3, de la separación de escalas
\(\rho\lambda^2\ge c_*^{-4}\log^2\mathcal N_\rho\), de la existencia del fondo F2,
de (P5.2-22) y del margen F3 anterior. Por tanto la conclusión vale a lo largo de una
sucesión no acotada de densidades, con \(A,K_2,K_{\rm bg},K,\ell,c_*\) y
\(\varepsilon\) fijados de antemano.

#### Terminal exacto de P5.2

| Obligación | Estado final | Evidencia |
|---|---|---|
| O1 — geometría causal y auxiliar | `PROVED` | §5.1 |
| O2 — \(0<\lambda<\infty\) | `PASS_WITH_NORM_SCOPE` | §5.2; las dos normas dan constantes finitas |
| O3 — región y testigo | `PASS_WITH_REGIONAL_SCOPE` | §5.3 |
| O4 — volumen y traza uniforme | `PROVED` | (P5.2-15)--(P5.2-17) |
| O5 — F2 final y fallo F3 | `PROVED` | (P5.2-19)--(P5.2-24) |

```text
P5_2_PASS_WITH_SCOPE
MATHEMATICAL_O1_O5: CLOSED
CURVATURE_NORM: UNDEFINED_IN_SOURCE / BOTH_STANDARD_READINGS_PASS
REGIONAL_DEFINITION_2_6: NOT_LITERAL_IN_MADSEN_REMARK_5_4
WP7_LITERAL_TERMINAL: PRODUCT_ORDER_COUNTEREXAMPLE_PROVED_P5_OPEN
```

Así, bajo la lectura regional natural y explícita, de Sitter planar realiza un
contraejemplo F1--F2-no-F3 con todas las constantes uniformes. Conforme al criterio de
parada de la nota de ampliación, no se promueve el terminal literal a
`COUNTEREXAMPLE_F1_F2_NOT_F3_D2`: esa promoción estaba reservada a `P5_2_PASS`, y la
ambigüedad de norma de O2 junto con la omisión regional de la Remark 5.4 obligan al
terminal `PASS_WITH_SCOPE`.

## 6. Ruta positiva aparcada

El contraejemplo anterior cierra negativamente la implicación en el modelo producto con
F2-2D tal como fue congelada. No se intenta ahora una desigualdad positiva. Esta ruta solo
podría reabrirse si P5 demuestra que la F2 geométrica exacta impone una restricción adicional
que invalida (3.4); tal restricción deberá escribirse, no suponerse.

## 7. Literatura mínima y función de cada fuente

| Fuente | Aporte permitido | Lo que no licencia |
|---|---|---|
| [N. Madsen, *On the Uniqueness of Embeddings of Causal Sets*](https://arxiv.org/html/2607.05840v1), arXiv:2607.05840v1 (2026), Defs. 2.2 y 2.6, Construction 2.3, Remark 4.7, Remark 5.4 y nota 1 | fija la clase globalmente hiperbólica, el auxiliar \(h_T\), la forma de \(\lambda\), F1--F3; para \(M\) no compacto restringe a \(C_K\) y reemplaza \(V_M\) por \(V_K\); declara abierta la dependencia lógica F1--F3 | no prueba F2=>F3, no evalúa \(\lambda\) para de Sitter planar, no define la norma exacta de \(\operatorname{Rm}[g]\) y no reescribe literalmente \((M,\partial M)\), la escala \(\lambda\) ni el dominio universal de diamantes como objetos regionales de \(K\) |
| [A. N. Bernal y M. Sánchez, *Smoothness of time functions and the metric splitting of globally hyperbolic spacetimes*](https://arxiv.org/abs/gr-qc/0401112), *Commun. Math. Phys.* 257 (2005), 43--50 | garantiza tiempos de Cauchy suaves en el caso general y es la fuente primaria invocada por Madsen | no sustituye la verificación explícita de \(t\), \(T\) y \(h_T\) en P5.2-O1 |
| [B. Bollobás y G. Brightwell, *The height of a random partial order: concentration of measure*](https://doi.org/10.1214/aoap/1177005586), AAP 2 (1992), 1009--1018 | concentración de altura en el modelo aleatorio de orden coordenado | no es una desigualdad determinista desde discrepancia |
| [J. Baik, P. Deift y K. Johansson, *On the Distribution of the Length of the Longest Increasing Subsequence of Random Permutations*](https://arxiv.org/abs/math/9810105), JAMS 12 (1999), 1119--1178 | normalización `2 sqrt(n)` y fluctuaciones de LIS uniforme | no controla permutaciones adversariales con F2 |
| [J. N. Cooper, *Quasirandom Permutations*](https://arxiv.org/abs/math/0211001), JCTA 106 (2004), 123--143 | vocabulario de discrepancia de intervalos/rectángulos y cuasialeatoriedad | `o(n)` y patrones fijos no controlan por sí solos la constante de LIS |
| [J. Dick y F. Pillichshammer, *Digital Nets and Sequences*](https://web.maths.unsw.edu.au/~josefdick/preprints/DP_book_preprint.pdf), CUP (2010), Thm. 3.46 | fondo determinista con `N D_N^*<=log_2 N+4` en `d=2` | no dice nada por sí solo sobre LIS |
| [V. Dubach, *Locally uniform random permutations with large increasing subsequences*](https://arxiv.org/abs/2301.07658), *Combinatorial Theory* 3(3) (2023), arXiv v2 (2024) | densidades divergentes en un punto o a lo largo de la diagonal pueden producir LIS de orden `N^beta`, `beta>1/2`, salvo factores logarítmicos | una densidad fija no uniforme tiene sesgo rectangular `Theta(n)` y no satisface nuestra F2 respecto de Lebesgue |

Anclas locales versionadas: `docs/bibliography_claims.md` §2.5bis y
`emergencia/P1a_contrato_gate_altura_duracion_lex_d2.md` §§2, 5--6. El PDF
`biblioteca/2607.05840v1.pdf`, citado en el historial del WP, no está versionado en este
checkout; P5.2-O1 se contrastó por ello contra la versión primaria enlazada de arXiv.
Toda afirmación de prioridad queda prohibida hasta una auditoría independiente de
literatura.

**Adjudicación de Dubach.** `DIRECT_PRECURSOR_OF_MECHANISM / DOES_NOT_SUBSUME`. Su objeto
es una muestra iid de una densidad fija, absolutamente continua pero divergente. Si esa ley
`mu` no es Lebesgue, existe un rectángulo de ejes `R` con `mu(R)!=|R|`; por la ley fuerte,
la discrepancia respecto de `n|R|` es `Theta(n)` casi seguramente, frente al techo
`O(sqrt(n log n))` de F2 para ese rectángulo fijo. Nuestro mecanismo es distinto: la masa
plantada es `k/n=Theta(n^{-1/2})` y desaparece con `n`.

## 8. Entregables y criterios de parada

Orden obligatorio, sin código ni datos:

1. ~~nota de prueba P1--P4, con cada constante y término de borde~~ — cerrada en §3;
2. ~~nota de transferencia P5 contra la Def. 2.6 exacta de Madsen~~ — P5.1 cerrada
   condicionalmente; P5.2-O1--O5 cerradas; terminal
   `P5_2_PASS_WITH_SCOPE` por las reservas de fuente tipadas en O2--O3;
3. ledger bibliográfico de discrepancia local, permutaciones cuasialeatorias y LIS.

Terminales, en orden de precedencia:

```text
COUNTEREXAMPLE_F1_F2_NOT_F3_D2        P1--P5 probadas
PRODUCT_ORDER_COUNTEREXAMPLE_PROVED_P5_OPEN
                                       P1--P4 probadas; P5 literal no cerrado
PRODUCT_ORDER_COUNTEREXAMPLE_ONLY     P1--P4 probadas; P5 falla
COUNTEREXAMPLE_TO_MADSEN_RATE_ONLY    F3 cualitativa vale; la tasa no
IMPLICATION_F2_TO_F3_D2               desigualdad determinista probada
REDUCTION_SCOPE_MISMATCH              la traducción 1+1 no representa F2/F3
OPEN_AFTER_TWO_PROOF_ROUTES           ninguna rama cierra con obligaciones explícitas
```

Parada dura: no se pasa a simulación, búsqueda masiva de permutaciones, dimensión mayor,
curvatura de Weyl ni diseño de estimadores. Un bloqueo debe nombrar la primera obligación
P1--P5 que falla y el enunciado residual que aún sería correcto.

## 9. Techo de afirmación

Tras P5.2 se permite afirmar:

> En el modelo determinista `fixed_n` de orden producto, F2-2D no implica F3-2D. Además,
> bajo la lectura regional explícita de la Remark 5.4 adoptada en §5, el parche planar de
> de Sitter admite configuraciones finitas con F1--F2 y constante de tolerancia fija que
> violan por una constante la desigualdad F3 completa. O1--O5 están cerradas; la única
> reserva es de formulación: Madsen no fija la norma de curvatura de \(\lambda\) ni
> reescribe literalmente todos los cuantificadores de su Def. 2.6 para una región
> precompacta; las dos normas estándar auditadas producen constantes finitas y la misma
> conclusión.

No se afirma un contraejemplo sin esos calificadores de alcance, prioridad o novedad, extensión a
`d>=3`, unicidad de embedding ni conclusión física sobre reconstrucción métrica general.
