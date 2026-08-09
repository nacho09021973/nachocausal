# WP7 — Contrato `F2 => F3` o contraejemplo en `d=2`

```text
ESTADO: CONTRATO FORMAL v1.3 / P1--P4 PROBADAS / P5.2-O1 PROBADA / P5 OPEN
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

`[PROVED — P1--P4; P5 permanece OPEN]`

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
| P5 | `OPEN` | P5.1 prueba estabilidad condicional; P5.2-O1 prueba la admisibilidad causal de de Sitter planar; O2--O5 no auditadas |

Por tanto, el terminal actual es `PRODUCT_ORDER_COUNTEREXAMPLE_PROVED_P5_OPEN`. Todavía
no se declara `COUNTEREXAMPLE_F1_F2_NOT_F3_D2` en el sentido geométrico de Madsen.

## 4. P5.1 — Estabilidad de F2 bajo una cadena mesoscópica plantada

**Estado: PROVED_CONDITIONAL / CYLINDER_SCALE_MISMATCH / P5 permanece OPEN.**

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
una versión de (P5.1-G), y un diamante testigo profundo. Hasta entonces continúa el terminal
PRODUCT_ORDER_COUNTEREXAMPLE_PROVED_P5_OPEN; no se rebaja todavía a
PRODUCT_ORDER_COUNTEREXAMPLE_ONLY, porque ha fallado esta realización, no la existencia
de todo puente geométrico posible.

## 5. P5.2 — Auditoría de de Sitter planar

**Estado: IN_PROGRESS / O1_PROVED / O2--O5_NOT_AUDITED / P5 permanece OPEN.**

La ampliación firmada en
`docs/program_reopening_note_2026-08-09_P5_2.md` autoriza como candidato único

\[
M_\ell=(-\infty,0)_\eta\times\mathbb R_x,
\qquad
g=\frac{\ell^2}{\eta^2}(-d\eta^2+dx^2),
\qquad \ell>0.
\]

Se elige la orientación temporal en la que \(\eta\) crece hacia el futuro. Esta sección
resuelve solo la primera obligación autorizada; en particular, todavía no evalúa el
supremo que define \(\lambda\).

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

**Corte de alcance.** P5.2-O1 queda probada. No se infiere de ello que
\(0<\lambda<\infty\): la inyectividad de \(h_T\), la norma de curvatura que entra en
(1) y el supremo sobre todos los campos unitarios pertenecen a O2. En consecuencia, el
terminal sigue siendo `PRODUCT_ORDER_COUNTEREXAMPLE_PROVED_P5_OPEN`.

## 6. Ruta positiva aparcada

El contraejemplo anterior cierra negativamente la implicación en el modelo producto con
F2-2D tal como fue congelada. No se intenta ahora una desigualdad positiva. Esta ruta solo
podría reabrirse si P5 demuestra que la F2 geométrica exacta impone una restricción adicional
que invalida (3.4); tal restricción deberá escribirse, no suponerse.

## 7. Literatura mínima y función de cada fuente

| Fuente | Aporte permitido | Lo que no licencia |
|---|---|---|
| [N. Madsen, *On the Uniqueness of Embeddings of Causal Sets*](https://arxiv.org/abs/2607.05840), arXiv:2607.05840v1 (2026), Defs. 2.2 y 2.6, Construction 2.3 y nota 1 | fija la clase globalmente hiperbólica, el auxiliar \(h_T\), F1--F3 y declara abierta su dependencia lógica | no prueba F2=>F3 ni evalúa \(\lambda\) para de Sitter planar |
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
2. nota de transferencia P5 contra la Def. 2.6 exacta de Madsen — P5.1 cerrada
   condicionalmente; P5.2-O1 probada para de Sitter planar; O2--O5 no auditadas;
3. ledger bibliográfico de discrepancia local, permutaciones cuasialeatorias y LIS.

Terminales, en orden de precedencia:

```text
COUNTEREXAMPLE_F1_F2_NOT_F3_D2        P1--P5 probadas
PRODUCT_ORDER_COUNTEREXAMPLE_PROVED_P5_OPEN
                                       P1--P4 probadas; P5 no adjudicada
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

Desde el cierre de P1--P4 solo se permite afirmar:

> En el modelo determinista `fixed_n` de orden producto, F2-2D no implica F3-2D. Un fondo
> de Hammersley más una cadena diagonal de tamaño `Theta(sqrt(n))` satisface la tolerancia
> rectangular con cociente que tiende uniformemente a cero, mientras la altura normalizada
> falla por una constante. La transferencia a la F2 geométrica exacta de Madsen sigue abierta
> como P5.

No se afirma todavía un contraejemplo al enunciado geométrico de Madsen, novedad,
extensión a `d>=3`, unicidad de embedding ni conclusión física sobre reconstrucción
métrica general.
