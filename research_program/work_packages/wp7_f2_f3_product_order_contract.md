# WP7 — Contrato `F2 => F3` o contraejemplo en `d=2`

```text
ESTADO: CONTRATO FORMAL v1.1 / PRODUCT_ORDER_COUNTEREXAMPLE PROBADO / P1--P4 PROBADAS / P5 OPEN
FECHA: 2026-08-08
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
| P5 | `OPEN` | falta casar borde, densidad, volumen, rango mesoscópico y normalización con Madsen |

Por tanto, el terminal actual es `PRODUCT_ORDER_COUNTEREXAMPLE_PROVED_P5_OPEN`. Todavía
no se declara `COUNTEREXAMPLE_F1_F2_NOT_F3_D2` en el sentido geométrico de Madsen.

## 4. Ruta positiva aparcada

El contraejemplo anterior cierra negativamente la implicación en el modelo producto con
F2-2D tal como fue congelada. No se intenta ahora una desigualdad positiva. Esta ruta solo
podría reabrirse si P5 demuestra que la F2 geométrica exacta impone una restricción adicional
que invalida (3.4); tal restricción deberá escribirse, no suponerse.

## 5. Literatura mínima y función de cada fuente

| Fuente | Aporte permitido | Lo que no licencia |
|---|---|---|
| [N. Madsen, *On the Uniqueness of Embeddings of Causal Sets*](https://arxiv.org/abs/2607.05840), arXiv:2607.05840v1 (2026), Def. 2.6 y nota 1 | fija F1, F2, F3 y declara abierta su dependencia lógica | no prueba F2=>F3; su resultado usa F3 por separado |
| [B. Bollobás y G. Brightwell, *The height of a random partial order: concentration of measure*](https://doi.org/10.1214/aoap/1177005586), AAP 2 (1992), 1009--1018 | concentración de altura en el modelo aleatorio de orden coordenado | no es una desigualdad determinista desde discrepancia |
| [J. Baik, P. Deift y K. Johansson, *On the Distribution of the Length of the Longest Increasing Subsequence of Random Permutations*](https://arxiv.org/abs/math/9810105), JAMS 12 (1999), 1119--1178 | normalización `2 sqrt(n)` y fluctuaciones de LIS uniforme | no controla permutaciones adversariales con F2 |
| [J. N. Cooper, *Quasirandom Permutations*](https://arxiv.org/abs/math/0211001), JCTA 106 (2004), 123--143 | vocabulario de discrepancia de intervalos/rectángulos y cuasialeatoriedad | `o(n)` y patrones fijos no controlan por sí solos la constante de LIS |
| [J. Dick y F. Pillichshammer, *Digital Nets and Sequences*](https://web.maths.unsw.edu.au/~josefdick/preprints/DP_book_preprint.pdf), CUP (2010), Thm. 3.46 | fondo determinista con `N D_N^*<=log_2 N+4` en `d=2` | no dice nada por sí solo sobre LIS |
| [V. Dubach, *Locally uniform random permutations with large increasing subsequences*](https://arxiv.org/abs/2301.07658), *Combinatorial Theory* 3(3) (2023), arXiv v2 (2024) | densidades divergentes en un punto o a lo largo de la diagonal pueden producir LIS de orden `N^beta`, `beta>1/2`, salvo factores logarítmicos | una densidad fija no uniforme tiene sesgo rectangular `Theta(n)` y no satisface nuestra F2 respecto de Lebesgue |

Anclas locales: `docs/bibliography_claims.md` §2.5bis; `biblioteca/2607.05840v1.pdf`;
`emergencia/P1a_contrato_gate_altura_duracion_lex_d2.md` §§2, 5--6. Toda afirmación de
prioridad queda prohibida hasta una auditoría independiente de literatura.

**Adjudicación de Dubach.** `DIRECT_PRECURSOR_OF_MECHANISM / DOES_NOT_SUBSUME`. Su objeto
es una muestra iid de una densidad fija, absolutamente continua pero divergente. Si esa ley
`mu` no es Lebesgue, existe un rectángulo de ejes `R` con `mu(R)!=|R|`; por la ley fuerte,
la discrepancia respecto de `n|R|` es `Theta(n)` casi seguramente, frente al techo
`O(sqrt(n log n))` de F2 para ese rectángulo fijo. Nuestro mecanismo es distinto: la masa
plantada es `k/n=Theta(n^{-1/2})` y desaparece con `n`.

## 6. Entregables y criterios de parada

Orden obligatorio, sin código ni datos:

1. ~~nota de prueba P1--P4, con cada constante y término de borde~~ — cerrada en §3;
2. nota de transferencia P5 contra la Def. 2.6 exacta de Madsen;
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

## 7. Techo de afirmación

Desde el cierre de P1--P4 solo se permite afirmar:

> En el modelo determinista `fixed_n` de orden producto, F2-2D no implica F3-2D. Un fondo
> de Hammersley más una cadena diagonal de tamaño `Theta(sqrt(n))` satisface la tolerancia
> rectangular con cociente que tiende uniformemente a cero, mientras la altura normalizada
> falla por una constante. La transferencia a la F2 geométrica exacta de Madsen sigue abierta
> como P5.

No se afirma todavía un contraejemplo al enunciado geométrico de Madsen, novedad,
extensión a `d>=3`, unicidad de embedding ni conclusión física sobre reconstrucción
métrica general.
