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

El experimento congelado (`P1a_count_volume_lema_kl_d2.md` §1) es el de `n` puntos
`X_1,\ldots,X_n` iid uniformes en `[0,1]^2` condicionados a `N=n`, con
\(\Pi_n\) la permutación de rangos. Por tanto \(\Pi_n\) **es** el mapa de rangos de
`n` puntos iid uniformes, y basta trabajar con éstos. Sea

\[
P_n=\frac1n\sum_{i=1}^n\delta_{X_i},
\qquad
Z(x,y)=P_n([0,x]\times[0,y])-xy,
\qquad
W=\sup_{(x,y)\in[0,1]^2}|Z(x,y)| .
\tag{3.1}
\]

**Lema 3.1.** `D^* <= 3nW`, y por tanto `Delta_n<=12W`.

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

**Lema 5.1.** Sean `Y_1,\ldots,Y_m` variables (no necesariamente independientes)
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
\le\sqrt{\frac6n}\cdot1.183\sum_{k\ge1}\sqrt{(k+1.5)2^{-k}}
\le\sqrt{\frac6n}\cdot1.183\cdot5.2
\le\frac{15.1}{\sqrt n},
\]

donde la serie numérica se acota sumando sus quince primeros términos
(`1.118,0.935,0.750,0.586,0.451,0.342,0.258,0.193,0.143,0.106,0.078,0.057,0.042,`
`0.030,0.022`, con suma `5.111`) y su cola por
`\sum_{k\ge16}\sqrt{(k+1.5)2^{-k}}<0.06`, pues sus términos decrecen por un factor
menor que `0.72` a partir de `k=16`, donde valen `0.0163`. La segunda parte es

\[
\sum_{k=1}^{K}\frac{L_k}{3n}
\le\frac{1.4}{3n}\left[\frac{K(K+1)}2+1.5K\right]
\le\frac{0.234K^2+0.93K}n,
\]

y con `K\le4.33\ln n+1` esto es a lo sumo
`(4.4(\ln n)^2+6\ln n+2)/n`, que para `n\ge10^{6}` es menor que `1/\sqrt n`
(en `n=10^{6}`: `9.3\cdot10^{-4}<10^{-3}`, y el cociente decrece).

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

**Corolario 8.1 (cierre del objeto (B) de `NC-2E`).** La condición **(B)** del
Corolario 8.2 de `NC-2E` queda demostrada con `c_1=4.2\cdot10^{4}`. En
consecuencia, si además existiera `c>0` con `Pr_n(S)>=c` para todo `n` grande,
entonces

\[
\operatorname{Var}_{\nu_n}(q_{n,h})\le\frac{3.4\cdot10^{9}}c\,n ,
\]

es decir `NC2E.1` con `C_q=3.4\cdot10^{9}/c`, y se promoverían (4.1) y (4.2) de la
nota `NC-2E`.

**Corolario 8.2 (qué queda exactamente).** Tras esta nota, la única obligación que
separa a `NC2E-O3` de su cierre es de naturaleza selectiva:

\[
\sum_{\pi\in\mathcal S_n}\Delta_n(\pi)^2\ \le\ \frac Cn\,|\mathcal S_n|
\tag{8.1}
\]

—que la selección no infle el segundo momento de la discrepancia por encima de su
valor incondicional (1.2)—, junto con la parte de anclaje, ya probada incondicional
y libre de logaritmo en `NC-2E` Lema 6.1. La cota trivial
`\sum_{\pi\in\mathcal S_n}\Delta_n^2\le n!\,E[\Delta_n^2]` sólo da (8.1) con
`C=4.2\cdot10^{4}/\Pr_n(S)`, que es exactamente el paso de división que esta nota
**no** mejora.

## 9. Techo de afirmación

Se demuestran los Lemas 2.1, 3.1, 4.1, 5.1, 7.1, el Corolario 5.2, la Proposición
6.1 y el Teorema 1.1. No se demuestra ni se refuta:

- `NC2E.1` ni `NC2E-O3`, que siguen abiertos;
- (8.1) ni ninguna cota inferior para `Pr_n(S)` mejor que la de `NC-2F-a`;
- `liminf T_n^h>0`;
- optimalidad de la constante `4.2\cdot10^4` ni del umbral `10^6`;
- nada sobre canales enriquecidos, poset completo, horizontes, escala absoluta o
  `d>=3`;
- novedad o prioridad bibliográfica: el enunciado (1.2) es del tipo clásicamente
  asociado al proceso empírico bidimensional, y aquí sólo se afirma que **esta**
  demostración es autocontenida y que la cota no estaba disponible en el
  repositorio.

No se tocó el sello, no se usaron semillas, no se consultaron los tamaños sellados
y no se creó ni ejecutó código, simulación, dato o artefacto numérico. No se
modificó la PR #7 ni ningún token publicado.

## 10. Terminal

```text
NC2F_B_TERMINAL = NC2F_B_PROVED_L2_DISCREPANCY
NC2F_B_BOUND = E[Delta_n^2] <= 4.2*10^4/n
NC2F_B_DOMAIN = n >= 10^6
NC2F_B_UNCONDITIONAL = YES
NC2F_B_SELF_CONTAINED = YES_NO_EXTERNAL_CITATIONS
NC2F_B_CORNER_REDUCTION = n*Delta_n <= 4*D*
NC2F_B_IID_REDUCTION = D* <= 3*n*W
NC2F_B_CHAINING_FIRST_MOMENT = E[W] <= 17/sqrt(n)
NC2F_B_VARIANCE = Var(W) <= 1/n
NC2F_B_CLOSES_NC2E_OBJECT_B = YES
NC2F_B_CONDITIONAL_CLOSURE = IF_PR_S_BOUNDED_BELOW_THEN_C_q = 3.4*10^9/c
NC2F_B_REMAINING_OBLIGATION = RELATIVE_DISCREPANCY_SUM_OVER_S_n
NC2F_B_NC2E_O3 = OPEN
NC2F_B_LIMINF_T_N = NOT_PROVED
NC2F_B_NEW_DATA = NO
NC2F_B_NEW_CODE = NO
NOVELTY_CERTIFIED = NO
```
