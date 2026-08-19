# `NC-2F-b` — discrepancia rectangular en `L^2`: cota incondicional `O(1/n)`

> **ESTADO: TEOREMA PROBADO · INCONDICIONAL, SIN SELECTOR · AUTOCONTENIDO ·
> CIERRA EL OBJETO (B) DE `NC-2E` §8 · `NC2E-O3` SIGUE ABIERTO ·
> SIN DATOS, SIMULACIONES, SEMILLAS, CÓDIGO NI ARTEFACTOS NUMÉRICOS NUEVOS.**

Autorización: `docs/program_reopening_note_2026-08-18_nc2f_variance_exponent_reduction.md`.

## 1. Objeto y resultado

Para una permutación uniforme \(\Pi_n\in\mathfrak S_n\) y pares de intervalos de
rangos `I,J`, sea

\[
\Delta_n=\max_{I,J}
\left|\frac{N_{\Pi_n}(I,J)}n-\frac{|I||J|}{n^2}\right|
\tag{1.1}
\]

la discrepancia rectangular usada en `NC-2C` §5, `NC-2D` §4.2 y `NC-2E` §2.5.
Todas las cotas anteriores para \(\Delta_n\) proceden de una unión sobre menos de
`n^4` pares de intervalos, que produce la escala
`sqrt(log n/n)`. `NC-2E` §8 aisló como objeto **(B)** la cota sin ese factor.

**Teorema 1.1.** Para todo `n>=10^{6}`,

\[
\boxed{\ \mathbb E[\Delta_n^2]\ \le\ \frac{4.2\cdot10^{4}}n\ }
\tag{1.2}
\]

donde la esperanza es respecto de la ley **uniforme** de \(\Pi_n\), sin
condicionar por `S`.

La prueba es autocontenida: sólo usa la desigualdad exponencial elemental de
Chernoff–Bernstein (demostrada en §4), una desigualdad maximal sub-gamma
(demostrada en §5), encadenamiento diádico (§6) y la descomposición de Doob para
diferencias acotadas (§7). No se usa ninguna cita externa.

## 2. Reducción a la discrepancia de esquinas

Para `0<=a,b<=n` sea

\[
F(a,b)=\#\{i\le a:\Pi_n(i)\le b\},
\qquad
D(a,b)=F(a,b)-\frac{ab}n,
\qquad
D^*=\max_{0\le a,b\le n}|D(a,b)| .
\tag{2.1}
\]

**Lema 2.1.** `n Delta_n <= 4 D^*`.

**Demostración.** Si `I={a_1+1,\ldots,a_2}` y `J={b_1+1,\ldots,b_2}`, la
inclusión–exclusión sobre los cuatro cuadrantes da

\[
N_{\Pi_n}(I,J)=F(a_2,b_2)-F(a_1,b_2)-F(a_2,b_1)+F(a_1,b_1),
\]

mientras que
`|I||J|/n=[a_2b_2-a_1b_2-a_2b_1+a_1b_1]/n`. Restando término a término,

\[
N_{\Pi_n}(I,J)-\frac{|I||J|}n
=D(a_2,b_2)-D(a_1,b_2)-D(a_2,b_1)+D(a_1,b_1),
\]

cuyo valor absoluto es a lo sumo `4D^*`. Dividiendo por `n` se obtiene el enunciado,
porque `Delta_n=n^{-1}\max_{I,J}|N-|I||J|/n|`. `QED`

## 3. Reducción al proceso empírico de puntos independientes

El experimento congelado (`P1a_count_volume_lema_kl_d2.md` §1, y §2.1 para la
propiedad que aquí carga la reducción) es el de `n` puntos `X_1,\ldots,X_n` iid
uniformes en `[0,1]^2` condicionados a `N=n`, con \(\Pi_n\) la permutación de
rangos. Condicionar el proceso de Poisson a `N=n` deja exactamente `n` puntos iid
uniformes, sin dependencia residual; y `lema_kl` §2.1 (`:95-107`) demuestra que su
permutación de rangos `\Pi=R_V\circ R_U^{-1}` es **uniforme** en \(\mathfrak S_n\) e
independiente de los estadísticos de orden. Por tanto \(\Pi_n\) **es** el mapa de
rangos de `n` puntos iid uniformes, y basta trabajar con éstos.

**Convención de nulidad.** Los empates entre coordenadas tienen probabilidad cero;
fuera de ese suceso nulo el mapa de rangos está bien definido y los órdenes
estrictos de más abajo son legítimos. Como `0\le\Delta_n\le1`, un suceso nulo no
altera `\mathbb E[\Delta_n^2]`, de modo que todas las afirmaciones de esta sección
se entienden **casi seguramente**.

**Transporte a la ley uniforme.** `\Delta_n` es, por su definición (1.1), función
medible de \(\Pi_n\) y de nada más. Por tanto una cota puntual para `\Delta_n`
probada en el espacio acoplado de los `X_i` es una cota puntual para la misma
función bajo la ley uniforme de \(\Pi_n\), y sus esperanzas coinciden. Ésta es la
razón por la que el Teorema 1.1, enunciado para una permutación uniforme, se
demuestra trabajando con los puntos.

Sea

\[
P_n=\frac1n\sum_{i=1}^n\delta_{X_i},
\qquad
Z(x,y)=P_n([0,x]\times[0,y])-xy,
\qquad
W=\sup_{(x,y)\in[0,1]^2}|Z(x,y)| .
\tag{3.1}
\]

**Medibilidad de `W`.** Para cada `\omega`, la función `(x,y)\mapsto Z(x,y)` es
continua por la derecha en ambas coordenadas (continuidad desde arriba de una
medida finita), luego el supremo de `|Z|` sobre `[0,1]^2` coincide con el supremo
sobre el conjunto numerable `(\{\text{diádicos}\}\cup\{1\})^2`. Así `W` es una
variable aleatoria genuina y `\mathbb E[W]` no es una esperanza exterior.

**Convención de logaritmo.** En esta nota `\log` y `\ln` designan siempre el
logaritmo **natural**; los únicos logaritmos en otra base se escriben `\log_2` y
aparecen sólo en la elección de `K` en §6.

**Lema 3.1.** `D^* <= 3nW`, y por tanto `Delta_n<=12W`.

*(Aviso de nomenclatura: `NC-2C` tiene un lema distinto, también numerado 3.1, que
es una desigualdad de Azuma para muestreo sin reemplazo. Ese lema no se usa en esta
nota; las dos numeraciones coinciden por accidente.)*

**Demostración.** Sean `U_{(1)}<\cdots<U_{(n)}` y `V_{(1)}<\cdots<V_{(n)}` los
estadísticos de orden de las dos coordenadas. Para `1<=a,b<=n`,

\[
F(a,b)=\#\{i:U_i\le U_{(a)},\,V_i\le V_{(b)}\}
=n\,P_n\bigl([0,U_{(a)}]\times[0,V_{(b)}]\bigr),
\]

y `F(a,b)=0` si `a=0` o `b=0`, en cuyo caso `D(a,b)=0`. Para `a,b>=1`,

\[
D(a,b)
=n\Bigl[P_n(Q)-U_{(a)}V_{(b)}\Bigr]
+n\Bigl[U_{(a)}V_{(b)}-\frac an\frac bn\Bigr],
\qquad Q=[0,U_{(a)}]\times[0,V_{(b)}].
\]

El primer corchete es `Z(U_{(a)},V_{(b)})`, de módulo `<=W`. Para el segundo,
tomando `y=1` en (3.1) se obtiene
`|P_n([0,x]\times[0,1])-x|\le W` para todo `x`; evaluando en `x=U_{(a)}`, donde la
función de distribución empírica de la primera coordenada vale exactamente `a/n`,
resulta `|U_{(a)}-a/n|\le W`, y análogamente `|V_{(b)}-b/n|\le W`. Luego

\[
\left|U_{(a)}V_{(b)}-\frac{ab}{n^2}\right|
\le\left|U_{(a)}-\frac an\right|V_{(b)}
+\frac an\left|V_{(b)}-\frac bn\right|
\le2W .
\]

Sumando, `|D(a,b)|<=3nW`. Con el Lema 2.1, `Delta_n<=4D^*/n<=12W`. `QED`

Por el Lema 3.1 basta probar `E[W^2]<=290/n`, ya que
`144\cdot290=41\,760\le4.2\cdot10^4`.

## 4. Desigualdad exponencial elemental

**Lema 4.1.** Sea `A subseteq[0,1]^2` boreliano con `p=\lambda(A)` y sea
`S_A=\sum_{i=1}^n(\mathbf 1_A(X_i)-p)`. Para todo `0<\theta<3`,

\[
\mathbb E\bigl[e^{\theta S_A}\bigr]
\le\exp\left(\frac{np\,\theta^2}{2(1-\theta/3)}\right).
\tag{4.1}
\]

**Demostración.** Para una sola variable,
\(\mathbb E e^{\theta(\mathbf 1_A-p)}=e^{-\theta p}\bigl(1+p(e^\theta-1)\bigr)
\le e^{-\theta p}e^{p(e^\theta-1)}=e^{p(e^\theta-1-\theta)}\), usando
`1+u<=e^u`. Por independencia,
\(\mathbb E e^{\theta S_A}\le e^{np(e^\theta-1-\theta)}\). Finalmente,

\[
e^\theta-1-\theta=\sum_{j\ge2}\frac{\theta^j}{j!}
\le\frac{\theta^2}2\sum_{j\ge0}\left(\frac\theta3\right)^{j}
=\frac{\theta^2}{2(1-\theta/3)},
\]

porque `j!\ge2\cdot3^{j-2}` para `j>=2`.

La misma cota vale para `-S_A`: en efecto,
\(\mathbb E e^{-\theta(\mathbf 1_A-p)}\le e^{p(e^{-\theta}-1+\theta)}\) y
`e^{-\theta}-1+\theta\le\theta^2/2\le\theta^2/(2(1-\theta/3))`. `QED`

## 5. Desigualdad maximal sub-gamma

**Lema 5.1.** Sea `m\ge2` y sean `Y_1,\ldots,Y_m` variables (no necesariamente independientes)
con \(\mathbb E e^{\theta Y_j}\le\exp\bigl(v\theta^2/(2(1-c\theta))\bigr)\) para
todo `0<\theta<1/c`. Entonces

\[
\mathbb E\left[\max_{j\le m}Y_j\right]
\le\sqrt{2v\log m}+c\log m .
\tag{5.1}
\]

**Demostración.** Sea `L=log m` y `0<\theta<1/c`. Por la desigualdad de Jensen
aplicada a `exp`,

\[
\mathbb E\max_jY_j
\le\frac1\theta\log\sum_{j}\mathbb E e^{\theta Y_j}
\le\frac1\theta\left[L+\frac{v\theta^2}{2(1-c\theta)}\right].
\]

Tómese `t=\sqrt{2L/v}` y `\theta=t/(1+ct)`, que cumple `0<\theta<1/c`. Entonces
`1-c\theta=1/(1+ct)` y

\[
\frac{v\theta^2}{2(1-c\theta)}
=\frac{v t^2}{2(1+ct)}=\frac L{1+ct},
\]

de modo que la cota vale

\[
\frac{1+ct}t\left[L+\frac L{1+ct}\right]
=\frac Lt(2+ct)
=\sqrt{2vL}+cL . \qquad\textsf{QED}
\]

La hipótesis `m\ge2` garantiza `L=\log m>0` y por tanto `t>0`, `\theta>0`. El caso
`m=1` queda excluido y no se usa en ninguna parte: el Corolario 5.2 aplica el lema
a `2m\ge2` variables.

**Corolario 5.2.** Si `A_1,\ldots,A_m` son borelianos con
`\lambda(A_j)\le p` para todo `j`, entonces

\[
\mathbb E\left[\max_{j\le m}\bigl|(P_n-\lambda)(A_j)\bigr|\right]
\le\sqrt{\frac{2p\log(2m)}n}+\frac{\log(2m)}{3n}.
\tag{5.2}
\]

**Demostración.** Aplíquese el Lema 5.1 a las `2m` variables `\pm S_{A_j}`, que por
el Lema 4.1 son sub-gamma con `v=np` y `c=1/3` (la cota (4.1) es monótona en `p`),
y divídase por `n`. `QED`

## 6. Encadenamiento diádico

**Proposición 6.1.** Para todo `n>=10^{6}`, `E[W]<=17/\sqrt n`.

**Demostración.** Sea `K=\lceil3\log_2n\rceil`, de modo que `2^K>=n^3`. Para
`k=0,1,\ldots,K` y `x\in[0,1]` sea `x_k=2^{-k}\lfloor2^kx\rfloor` (y `x_k=1` si
`x=1`); análogamente `y_k`. Se tiene `x_{k-1}\le x_k\le x` y
`x_k-x_{k-1}\in\{0,2^{-k}\}`.

Aquí `Q(x,y)=[0,x]\times[0,y]` designa siempre el cuadrante **cerrado**, como en
(3.1).

*Cadena.* Como `x_0,y_0\in\{0,1\}` y `Z` se anula en los bordes `x=0`, `y=0` y en
`(1,1)`, resulta `Z(x_0,y_0)=0`, luego

\[
Z(x,y)=\sum_{k=1}^{K}
\bigl[Z(x_k,y_k)-Z(x_{k-1},y_{k-1})\bigr]
+\bigl[Z(x,y)-Z(x_K,y_K)\bigr].
\tag{6.1}
\]

*Incrementos.* Como `Q(x_{k-1},y_{k-1})\subseteq Q(x_k,y_k)`, el `k`-ésimo
sumando es `(P_n-\lambda)(A)` con
`A=Q(x_k,y_k)\setminus Q(x_{k-1},y_{k-1})` y

\[
\lambda(A)=x_ky_k-x_{k-1}y_{k-1}
\le2^{-k}(x_{k-1}+y_{k-1})+4^{-k}
\le3\cdot2^{-k}=:p_k .
\]

Como `x_{k-1}` queda determinado por `x_k`, el número de regiones `A` posibles en
el nivel `k` es a lo sumo `m_k=(2^k+1)^2\le4^{k+1}`. Por el Corolario 5.2, con
`L_k=\log(2m_k)\le\log2+(k+1)\log4\le1.4(k+1.5)`,

\[
\mathbb E\Bigl[\max_A\bigl|(P_n-\lambda)(A)\bigr|\Bigr]
\le\sqrt{\frac{6\cdot2^{-k}L_k}n}+\frac{L_k}{3n}.
\]

Sumando en `k`, la primera parte es

\[
\sqrt{\frac6n}\sum_{k\ge1}\sqrt{2^{-k}L_k}
\le\sqrt{\frac6n}\cdot1.1833\sum_{k\ge1}\sqrt{(k+1.5)2^{-k}}
\le\sqrt{\frac6n}\cdot1.1833\cdot5.2
\le\frac{15.1}{\sqrt n},
\]

donde `1.1833\ge\sqrt{1.4}` y la serie numérica se acota sumando sus quince
primeros términos, cada uno redondeado **hacia arriba** a tres decimales,

```text
1.119, 0.936, 0.750, 0.587, 0.451, 0.343, 0.258, 0.193,
0.144, 0.106, 0.079, 0.058, 0.043, 0.031, 0.023
```

cuya suma es `5.121`, y su cola por

\[
\sum_{k\ge16}\sqrt{(k+1.5)2^{-k}}<0.061 .
\]

Esta última se justifica así: `t_k=\sqrt{(k+1.5)2^{-k}}` cumple
`t_{16}\le0.01635`, y el cociente

\[
\frac{t_{k+1}}{t_k}=\sqrt{\frac{k+2.5}{2(k+1.5)}}
\]

es decreciente en `k` con valor `\sqrt{18.5/35}\le0.7271` en `k=16`; por tanto la
cola está dominada por la serie geométrica `0.01635/(1-0.7271)<0.060<0.061`. El
total es `5.121+0.061=5.182\le5.2`.

Todos los redondeos de este paso son **hacia arriba**, en la dirección segura para
una cadena de cotas superiores. Con ellos,
`\sqrt6\cdot1.1833\cdot5.2\le15.073\le15.1`.

La segunda parte es

\[
\sum_{k=1}^{K}\frac{L_k}{3n}
\le\frac{1.4}{3n}\left[\frac{K(K+1)}2+1.5K\right]
\le\frac{0.234K^2+0.93K}n
\qquad(K\ge5),
\]

donde la última desigualdad usa `1.4/6\le0.234` y requiere `K\ge5` para absorber el
redondeo a la baja de `1.4\cdot2/3=0.9333\ldots` en `0.93`. La condición es exacta,
no conservadora: la diferencia entre ambos miembros es `K(K-5)/1500`, nula en `K=5`
y negativa para `K\le4`. En todo el dominio `n\ge10^{6}` se tiene `K\ge60`.

Finalmente, con `K\le4.33\ln n+1` —que usa `3/\log2\le4.33`— el miembro derecho es a
lo sumo `(4.4(\ln n)^2+6\ln n+2)/n`, que para `n\ge10^{6}` es menor que `1/\sqrt n`
(en `n=10^{6}`: `9.3\cdot10^{-4}<10^{-3}`, y el cociente decrece). Aquí el
coeficiente `6` está por debajo del valor exacto `6.054`, pero el término
independiente lo compensa con margen: el desarrollo exacto es
`4.3873(\ln n)^2+6.054\ln n+1.164`, y la diferencia
`0.0127(\ln n)^2-0.054\ln n+0.836` tiene discriminante
`0.054^2-4\cdot0.0127\cdot0.836<0`, luego es positiva para todo `n>1`.

*Resto de resolución.* Si `x_K\le x<x_K+2^{-K}` y `y_K\le y<y_K+2^{-K}`, entonces
`Q(x_K,y_K)\subseteq Q(x,y)` y la diferencia de cuadrantes está contenida en la
unión de dos bandas de anchura `2^{-K}`, luego

\[
|Z(x,y)-Z(x_K,y_K)|
\le P_n(S_x)+P_n(S_y)+3\cdot2^{-K},
\]

con `S_x` la banda vertical diádica de anchura `2^{-K}` que contiene a `x` y `S_y`
la horizontal correspondiente. Si `N_1,\ldots,N_{2^K}` son los conteos de las
bandas verticales diádicas, entonces
`\max_jN_j\le1+\sum_j(N_j-1)^+\le1+\sum_j\binom{N_j}2`, y

\[
\mathbb E\left[\sum_j\binom{N_j}2\right]
=2^K\binom n2 4^{-K}
\le\frac{n^2}{2\cdot2^K}\le\frac1{2n},
\]

porque `2^K>=n^3`. Luego
`E[\sup_xP_n(S_x)]\le(1+1/(2n))/n\le1.1/n`, e igual para las horizontales; el
resto de resolución aporta a lo sumo `2.2/n+3n^{-3}\le3/n`.

Sumando las tres contribuciones,
`E[W]\le15.1/\sqrt n+1/\sqrt n+3/n\le17/\sqrt n` para `n>=10^{6}`; en `n=10^{6}`
el miembro izquierdo vale `1.61\cdot10^{-2}` y el derecho `1.7\cdot10^{-2}`. `QED`

## 7. Del primer momento al segundo

**Lema 7.1.** `Var(W)<=1/n`.

**Demostración.** `W=f(X_1,\ldots,X_n)` con `X_i` independientes. Si se cambia un
solo punto, cada valor `P_n(A)` cambia a lo sumo en `1/n`, luego el supremo `W`
cambia a lo sumo en `1/n`. Sea \(\mathcal F_i=\sigma(X_1,\ldots,X_i)\) y
`M_i=E[W\mid\mathcal F_i]`, de modo que `M_n=W` y `M_0=E[W]`. Si `X_i'` es una
copia independiente de `X_i` y `W^{(i)}` es `W` con `X_i` sustituido por `X_i'`,
entonces

\[
M_i-M_{i-1}=\mathbb E\bigl[W-W^{(i)}\mid\mathcal F_i\bigr],
\qquad |M_i-M_{i-1}|\le\frac1n .
\]

Las diferencias de martingala son ortogonales en `L^2`, luego

\[
\operatorname{Var}(W)=\sum_{i=1}^n\mathbb E\bigl[(M_i-M_{i-1})^2\bigr]
\le n\cdot\frac1{n^2}=\frac1n . \qquad\textsf{QED}
\]

**Corolario 7.2.** Para `n>=10^{6}`,
`E[W^2]=(E W)^2+Var(W)\le289/n+1/n=290/n`.

Obsérvese que aquí sí se dispone de estructura producto: los `X_i` son
independientes. Ésta es exactamente la estructura que **no** existe bajo la medida
seleccionada \(\nu_n\), como se hizo constar en `NC-2E` §9.2.

## 8. Demostración del Teorema 1.1 y consecuencia

Por el Lema 3.1 y el Corolario 7.2,

\[
\mathbb E[\Delta_n^2]\le144\,\mathbb E[W^2]
\le\frac{144\cdot290}n=\frac{41\,760}n\le\frac{4.2\cdot10^{4}}n ,
\]

lo que prueba (1.2). `QED`

**Corolario 8.1 (CONDICIONAL — cierre del objeto (B) de `NC-2E`).** La condición
**(B)** del Corolario 8.2 de `NC-2E` queda demostrada, incondicionalmente, con
`c_1=4.2\cdot10^{4}`. La consecuencia siguiente es en cambio **condicional** y su
hipótesis **no está demostrada**: si además existiera `c>0` con `Pr_n(S)>=c` para
todo `n` grande, entonces, para `n\ge10^{40}`,

\[
\operatorname{Var}_{\nu_n}(q_{n,h})\le\frac{3.4\cdot10^{9}}c\,n ,
\]

es decir `NC2E.1` con `C_q=3.4\cdot10^{9}/c`, y se promoverían (4.1) y (4.2) de la
nota `NC-2E`.

Sobre el dominio: la cadena deductiva de este corolario pasa por el Corolario 8.2 y
el Teorema 8.1 de `NC-2E`, que exigen `n\ge\max(n_1,n_2)`, donde `n_1` es el umbral
absoluto del Lema 5.1 de `NC-2E` —declarado existente pero **no cuantificado allí**—
y `n_2` el de la hipótesis. El dominio honesto es por tanto
`n\ge\max(n_1,10^{6})`, y la elección conservadora `n\ge10^{40}` lo cubre con
holgura, ya que ése es el umbral que gobierna toda la cadena `NC-2C`–`NC-2E`.
Restringir el dominio de una consecuencia condicional sólo la debilita, nunca la
falsea. El Teorema 1.1 de esta nota, en cambio, vale desde `n\ge10^{6}`.

La hipótesis `Pr_n(S)\ge c>0` está **abierta en ambos sentidos**. Lo mejor que se
sabe es la cota inferior de `NC-2F(a)` (`P1a_count_volume_selection_mass_sqrt_scaling_d2.md`,
Teorema 5.1), `Pr_n(S)\ge\frac12n^{-(40\sqrt{n\log n}+5)}`, que decae; una cota
inferior que decae **no** refuta la hipótesis, y no existe en el repositorio ninguna
cota superior incondicional para `Pr_n(S)`. Este corolario no debe citarse como si
el cierre estuviera conseguido.

**Corolario 8.2 (qué queda exactamente).** Tras esta nota, la obligación que separa
a `NC2E-O3` de su cierre por la vía del Teorema 8.1 de `NC-2E` es de naturaleza
selectiva y afecta a **los dos** términos de aquel enunciado:

\[
\sum_{\pi\in\mathcal S_n}\bigl(R(\pi)+\Delta_n(\pi)\bigr)^2
\ \le\ \frac Cn\,|\mathcal S_n|
\tag{8.1}
\]

—que la selección no infle el segundo momento ni del radio de anclaje ni de la
discrepancia por encima de sus valores incondicionales. Lo que esta nota aporta es
**una mitad**: el término `\Delta_n` ya está a escala `1/n` sin condicionar (1.2),
igual que `R` lo estaba por el Lema 6.1 de `NC-2E` (`E[R^2]\le65/n`).

Debe subrayarse que ese Lema 6.1 es **incondicional, no relativo a
\(\mathcal S_n\)**: la única cota relativa disponible para `R` es el Lema 6.3 de
`NC-2E`, `E_{\nu_n}[R^2]\le17L_n/n`, que con el `L_n` de `NC-2F(a)` da
`O((\log n)^{3/2}/\sqrt n)` y **no** alcanza la escala `1/n`. Por tanto `R` y
`\Delta_n` están hoy exactamente en la misma situación —ambos controlados sin
condicionar, ninguno relativamente— y sería un error contabilizar la obligación
restante usando sólo `\Delta_n`.

La cota trivial `\sum_{\pi\in\mathcal S_n}(R+\Delta_n)^2\le n!\,E[(R+\Delta_n)^2]`
sólo da (8.1) con `C=O(1/\Pr_n(S))`, que es exactamente el paso de división que esta
nota **no** mejora.

Finalmente, `NC-2E` §8 hace constar que (8.1) es **suficiente y no se ha probado
necesaria**: no existe implicación recíproca demostrada. Este corolario describe qué
falta por la ruta del Teorema 8.1, no afirma que sea la única ruta posible.

## 9. Techo de afirmación

Se demuestran los Lemas 2.1, 3.1, 4.1, 5.1, 7.1, el Corolario 5.2, la Proposición
6.1, el Corolario 7.2, el Teorema 1.1 y —con el estatuto que se indica— los
Corolarios 8.1 y 8.2. De ellos, el Corolario 8.1 es **condicional**: su hipótesis
`Pr_n(S)\ge c>0` no está demostrada. El Corolario 8.2 es una **descripción** de lo
que falta por la ruta del Teorema 8.1 de `NC-2E`, no un teorema nuevo.

No se demuestra ni se refuta:

- `NC2E.1` ni `NC2E-O3`, que siguen abiertos;
- (8.1) ni ninguna cota inferior para `Pr_n(S)` mejor que la de `NC-2F-a`;
- la hipótesis `Pr_n(S)\ge c>0`, que sigue abierta en ambos sentidos: no se
  demuestra, y tampoco se refuta;
- `liminf T_n^h>0`;
- optimalidad de la constante `4.2\cdot10^4` ni del umbral `10^6`;
- nada sobre canales enriquecidos, poset completo, horizontes, escala absoluta o
  `d>=3`;
- novedad o prioridad bibliográfica. Aquí sólo se afirma que **esta** demostración
  es autocontenida y que la cota no estaba disponible en el repositorio. La
  impresión de que un enunciado como (1.2) pertenece al acervo clásico del proceso
  empírico bidimensional se registra como `[UNVERIFIED]`: no se ha comprobado
  ninguna fuente bibliográfica, y de la ausencia de comprobación no se sigue ni
  novedad ni anterioridad.

No se tocó el sello, no se usaron semillas, no se consultaron los tamaños sellados
y no se creó ni ejecutó código, simulación, dato o artefacto numérico. No se
modificó la PR #7 ni ningún token publicado.

## 10. Terminal

```text
NC2F_B_TERMINAL = NC2F_B_PROVED_L2_DISCREPANCY
NC2F_B_BOUND = E[Delta_n^2] <= 4.2*10^4/n
NC2F_B_DOMAIN = n >= 10^6
NC2F_B_UNCONDITIONAL = YES
NC2F_B_SELF_CONTAINED = NO_EXTERNAL_BIBLIOGRAPHY_INTERNAL_DEPENDENCIES_DECLARED
NC2F_B_CORNER_REDUCTION = n*Delta_n <= 4*D*
NC2F_B_IID_REDUCTION = D* <= 3*n*W
NC2F_B_CHAINING_FIRST_MOMENT = E[W] <= 17/sqrt(n)
NC2F_B_VARIANCE = Var(W) <= 1/n
NC2F_B_CLOSES_NC2E_OBJECT_B = YES
NC2F_B_CONDITIONAL_CLOSURE = IF_PR_S_BOUNDED_BELOW_THEN_C_q = 3.4*10^9/c
NC2F_B_CONDITIONAL_CLOSURE_DOMAIN = n >= 10^40
NC2F_B_PR_S_LOWER_BOUND_HYPOTHESIS = OPEN_NOT_REFUTED
NC2F_B_REMAINING_OBLIGATION = RELATIVE_SUM_OF_(R+Delta_n)^2_OVER_S_n
NC2F_B_HALF_OF_REMAINING_OBLIGATION_SUPPLIED = DELTA_TERM_UNCONDITIONAL_ONLY
NC2F_B_NC2E_O3 = OPEN
NC2F_B_LIMINF_T_N = NOT_PROVED
NC2F_B_NEW_DATA = NO
NC2F_B_NEW_CODE = NO
NC2F_B_ADVERSARIAL_AUDIT = FORO_002_REVISE_AND_RECONVENE
NC2F_B_AUDIT_CORRECTIONS_APPLIED = TAIL_RATIO, ROUNDING_DIRECTION, R_TERM_RESTORED,
                                   COR_8_1_LABELLED_CONDITIONAL, AS_CONVENTIONS,
                                   MEASURABILITY, LOG_CONVENTION, M_GE_2, K_GE_5
NOVELTY_CERTIFIED = NO
```

## 11. Registro de auditoría adversarial

Este documento fue sometido a un foro adversarial de dos olas
(`docs/foro/foro_decision_002_nc2fb-auditoria-adversarial.md`, veredicto
`REVISE_AND_RECONVENE`) que confirmó el Teorema 1.1 y su constante mediante
recómputo independiente, y localizó los defectos corregidos arriba. Los tres más
graves eran: una desigualdad publicada literalmente falsa en la justificación de la
cola de la serie (`factor <0.72`, siendo el cociente real `0.7270292`); la omisión
del término `R` en el Corolario 8.2, que contabilizaba de menos la obligación
restante; y la ausencia de etiqueta CONDICIONAL en el Corolario 8.1. Ninguno de los
tres afectaba a la validez del Teorema 1.1 ni a la constante `4.2\cdot10^4`.

Quedan tres puntos registrados como **no resueltos** por el foro, ninguno de los
cuales invalida lo demostrado, y los tres pendientes de auditoría futura si alguien
vuelve sobre esta nota:

1. el recuento `m_k=(2^k+1)^2` del nivel `k` en §6 no fue re-derivado de forma
   independiente desde la construcción del encadenamiento;
2. la exactitud iid bajo el condicionamiento a `N=n` quedó anclada en §3 a
   `lema_kl` §2.1 durante la corrección posterior, pero ningún rol distinto del que
   escribió esa sección ha certificado el paso completo;
3. no está fijado por escrito si las constantes deductivas de una prueba quedan
   fuera de la regla `numbers-must-come-from-committed-script`; el precedente
   uniforme de la familia `P1a_*` sugiere que sí, pero la regla no lo dice.
