# `NC-2D` — segundo momento de la forma seleccionada

> **ESTADO: AVANCE ANALÍTICO PARCIAL · CONSISTENCIA `L2` SELECCIONADA PROBADA
> PARA `Z_(n,h)` · LA COTA `O(n^(9/5) log n)` PARA `sqrt(K_h L_h)` ES SOLO SU
> REESCALADO · `NC2D-O3` SIGUE ABIERTO ·
> SIN DATOS, SIMULACIONES, SEMILLAS, CÓDIGO NI ARTEFACTOS NUMÉRICOS NUEVOS.**

Autorización firmada:
`docs/program_reopening_note_2026-08-17_nc2d_selected_second_moment_DRAFT.md`.

## 1. Objeto y resultado

Sea \(\Pi_n\) una permutación uniforme en el grupo simétrico \(\mathfrak S_n\), sea
\(S\) el evento de que
`MIN_COVERAGE_LEX` tenga un ganador único y, para el lado
`h in {PAST,FUTURE}` de ese ganador, sean `(K_h,L_h)` los gaps entre rangos de sus
endpoints. Se escriben

\[
q_{n,h}=\sqrt{K_hL_h},
\qquad
Z_{n,h}=\frac{q_{n,h}}{n+1}.
\tag{1.1}
\]

`NC-2B` garantiza `Pr_n(S)>0` para todo `n>=6`. El objetivo firmado de esta nota es
decidir si

\[
\operatorname{Var}(q_{n,h}\mid n,h,S)=O(n).
\tag{1.2}
\]

No se alcanza esa tasa. Sí se demuestra el siguiente resultado nuevo.

**Teorema 1.1 — concentración parcial seleccionada.** Para ambos lados y todo
`n>=10^40`,

\[
\boxed{
\mathbb E[(Z_{n,h}-1/2)^2\mid n,h,S]
\le 700\,n^{-1/5}\log n,}
\tag{1.3}
\]

y, por tanto, la misma cota vale para
`Var(Z_{n,h}|n,h,S)`. La identidad (1.1) da exactamente

\[
\boxed{
\begin{aligned}
\operatorname{Var}(q_{n,h}\mid n,h,S)
&=(n+1)^2\operatorname{Var}(Z_{n,h}\mid n,h,S)\\
&\le 700(n+1)^2n^{-1/5}\log n\\
&\le 2800\,n^{9/5}\log n.
\end{aligned}}
\tag{1.4}
\]

Así, (1.4) no es una segunda estimación independiente: es el reescalado exacto de
la cota de varianza para `Z` implicada por (1.3), seguido de
`(n+1)^2<=4n^2`.

En particular, bajo la ley seleccionada,

\[
Z_{n,h}\longrightarrow\frac12
\quad\text{en }L^2,
\tag{1.5}
\]

uniformemente respecto del lado. La cota actualmente demostrada pierde un factor
`n^(4/5) log n` respecto de la escala requerida por (1.2), de modo que no cierra
`NC2D-O3`. Esta comparación es entre cotas o escalas de prueba; no afirma que la
varianza real tenga necesariamente orden `n^(9/5) log n`.

## 2. Auditoría de la reducción de O3

La independencia rango–magnitud y la ley Beta-producto están probadas en
`P1a_count_volume_lema_kl_d2.md`. Si

\[
\mu_n(k,l)=\mathbb E[\ell_h\mid K_h=k,L_h=l,n,h,S],
\qquad
v_n(k,l)=\operatorname{Var}(\ell_h\mid K_h=k,L_h=l,n,h,S),
\]

entonces

\[
V_n^h:=\operatorname{Var}(\ell_h\mid n,h,S)
=\mathbb E[v_n(K_h,L_h)\mid n,h,S]
+\operatorname{Var}(\mu_n(K_h,L_h)\mid n,h,S),
\tag{2.1}
\]

con las cotas uniformes

\[
\mathbb E[v_n(K_h,L_h)\mid n,h,S]\le\frac1n,
\qquad
|\mu_n(K_h,L_h)-Z_{n,h}|\le\frac1{2\sqrt n}.
\tag{2.2}
\]

En el espacio ya condicionado por `(n,h,S)`, la proyección
`X -> X-E[X]` es una contracción en `L2`. Por la desigualdad triangular,

\[
\left|
\sqrt{\operatorname{Var}(\mu_n(K_h,L_h))}
-\sqrt{\operatorname{Var}(Z_{n,h})}
\right|
\le\frac1{2\sqrt n}.
\tag{2.3}
\]

Así, si `Var(q_{n,h}|S)<=C_q n`, entonces

\[
V_n^h
\le\frac{1+(\sqrt{C_q}+1/2)^2}{n}.
\tag{2.4}
\]

Recíprocamente, si `V_n^h<=C/n`, (2.1) da
`Var(mu_n(K_h,L_h))<=C/n`, y (2.3) implica

\[
\operatorname{Var}(q_{n,h}\mid n,h,S)
\le(\sqrt C+1/2)^2\frac{(n+1)^2}{n}=O(n).
\tag{2.5}
\]

Por tanto (1.2) y `NC2D-O3` son equivalentes, salvo constantes explícitas. La
rotación de 180 grados probada en `NC-2C` preserva `S`, intercambia PAST/FUTURE y
preserva los gaps correspondientes; también reduce exactamente ambos lados a uno.

## 3. Por qué no existe una cota determinista de anchura `sqrt(n)`

La selección única no fuerza por sí sola que `q_{n,h}` esté cerca de `n/2`.

1. Para `n=2r`, la permutación identidad induce una cadena total. Su ganador único
   usa dos intervalos de cardinalidad `r`, con
   \[
   K_h=L_h=r-1,
   \qquad q_{n,h}=\frac n2-1.
   \]
2. La permutación
   \[
   (n,n-1,\ldots,7,1,2,3,4,5,6)
   \]
   induce una cadena aislada de seis puntos y también pertenece a `S`; su ganador
   satisface
   \[
   K_h=L_h=2,
   \qquad q_{n,h}=2.
   \]

La oscilación dentro de `S` es, pues, de orden `n`. Toda prueba de (1.2) debe ser
relativa al número de configuraciones seleccionadas; no puede sustituirse por una
cota de soporte.

## 4. Dos eventos uniformes de regularidad

Se reutilizan la discrepancia y la masa de selección ya demostradas en `NC-2C`, y
se añade una cota elemental para cuatro cajas ancla. Defínase

\[
a_n=n^{-1/10}\sqrt{\log n},
\qquad
r_n=4a_n,
\qquad
\delta_n=\sqrt8\,a_n.
\tag{4.1}
\]

Para `n>=10^40`, estas cantidades decrecen, `r_n<1/4` y todas las expresiones de
esta sección son positivas.

### 4.1 Cajas ancla

Sea `m=floor(r_n n)`. En cada eje de rangos tómense los cuatro bloques

\[
\begin{aligned}
B_1&=\{1,\ldots,m\},\\
B_2&=\{\lfloor n/2\rfloor-m+1,\ldots,\lfloor n/2\rfloor\},\\
B_3&=\{\lfloor n/2\rfloor+1,\ldots,\lfloor n/2\rfloor+m\},\\
B_4&=\{n-m+1,\ldots,n\}.
\end{aligned}
\tag{4.2}
\]

Sea `A_n` el evento de que cada caja diagonal `B_j x B_j` contenga un punto de la
permutación. Para un bloque de `m` filas y `m` columnas, la probabilidad de que no
haya ningún punto es

\[
\frac{\binom{n-m}{m}}{\binom nm}
\le\left(1-\frac mn\right)^m
\le e^{-m^2/n}.
\]

Como `m>=r_n n/2` en la cola considerada, la unión sobre las cuatro cajas da

\[
\Pr(A_n^c)\le4\exp(-nr_n^2/4).
\tag{4.3}
\]

### 4.2 Discrepancia rectangular

Para intervalos de rangos `I,J`, sea

\[
\Delta_n=
\max_{I,J}
\left|
\frac{N_{\Pi_n}(I,J)}n-
\frac{|I||J|}{n^2}
\right|.
\tag{4.4}
\]

El Lema 3.1 de `NC-2C`, con `t=n delta`, y la unión sobre menos de `n^4` pares de
intervalos prueban, para todo `delta>0`,

\[
\Pr(\Delta_n>\delta)
\le2n^4\exp(-n\delta^2/2).
\tag{4.5}
\]

Sea `D_n={Delta_n<=delta_n}`.

### 4.3 Condicionamiento por selección

`NC-2C` demostró para todo `n>=10^40` la cota

\[
\Pr_n(S)\ge\frac12 n^{-(2n^{4/5}+4)}.
\tag{4.6}
\]

Como `nr_n^2/4=4n^{4/5}log n`, (4.3)--(4.6) dan

\[
\Pr(A_n^c\mid S)
\le8n^{-2n^{4/5}+4}.
\tag{4.7}
\]

Del mismo modo, `n delta_n^2/2=4n^{4/5}log n`, luego

\[
\Pr(D_n^c\mid S)
\le4n^{-2n^{4/5}+8}.
\tag{4.8}
\]

Estas cotas son simultáneas para ambos lados porque `A_n`, `D_n` y `S` pertenecen a
la permutación completa y no dependen de elegir PAST o FUTURE.

## 5. Estabilidad geométrica del ganador

Supóngase `A_n cap D_n`. Elíjase un punto en cada caja diagonal de (4.2). Los cuatro
puntos están estrictamente ordenados en ambas coordenadas y forman una 4-cadena.
Cada uno de sus dos rectángulos laterales tiene longitudes de rangos al menos

\[
n(1/2-2r_n)
\]

en ambos ejes. Por (4.4), sus cardinalidades satisfacen

\[
\frac{M_-}n,\frac{M_+}n
\ge(1/2-2r_n)^2-\delta_n.
\tag{5.1}
\]

Para `n>=10^40` el lado derecho es mayor que `3/n`, así que la cuádrupla pertenece a
`Q_3(C)`. El ganador de `MIN_COVERAGE_LEX`, si es único, tiene por tanto ambos lados
al menos tan grandes como (5.1).

Fijado uno de sus lados, su rectángulo cerrado tiene longitudes de rangos
`K_h+1,L_h+1`. Aplicando de nuevo la discrepancia, ahora en el sentido superior para
su cardinalidad,

\[
\frac{(K_h+1)(L_h+1)}{n^2}
\ge(1/2-2r_n)^2-2\delta_n.
\tag{5.2}
\]

Póngase

\[
x_h=\frac{\sqrt{(K_h+1)(L_h+1)}}n.
\]

La parte derecha de (5.2) es mayor que `1/5` en toda la cola. Como
`K_h+L_h+1<=2n+1`, racionalizar la diferencia de raíces da

\[
0\le x_h-Z_{n,h}\le\frac7n.
\tag{5.3}
\]

Además, si `u=1/2-2r_n`, entonces `u>=1/3` y

\[
\sqrt{u^2-2\delta_n}
\ge u-\frac{2\delta_n}{u}
\ge u-6\delta_n.
\tag{5.4}
\]

Por (5.2)--(5.4), cada lado del ganador satisface

\[
Z_{n,h}\ge\frac12-2r_n-6\delta_n-\frac7n.
\tag{5.5}
\]

Para la misma 4-cadena, los gaps de ambos lados cumplen

\[
K_-+K_+\le n-2,
\qquad
L_-+L_+\le n-2.
\]

Cauchy--Schwarz implica

\[
Z_{n,-}+Z_{n,+}
=\frac{\sqrt{K_-L_-}+\sqrt{K_+L_+}}{n+1}
\le\frac{n-2}{n+1}<1.
\tag{5.6}
\]

La cota inferior (5.5) para el lado opuesto convierte (5.6) en la cota superior
simétrica. En consecuencia, simultáneamente para ambos lados,

\[
|Z_{n,h}-1/2|
\le2r_n+6\delta_n+7/n
\le26a_n
\quad\text{en }A_n\cap D_n\cap S.
\tag{5.7}
\]

## 6. Segundo momento seleccionado

Siempre `0<=Z_{n,h}<1`, luego `(Z_{n,h}-1/2)^2<=1/4`. Separando el evento bueno y
su complemento, y usando (4.7)--(4.8) y (5.7),

\[
\begin{aligned}
\mathbb E[(Z_{n,h}-1/2)^2\mid n,h,S]
&\le676a_n^2
 +2n^{-2n^{4/5}+4}
 +n^{-2n^{4/5}+8}\\
&\le700n^{-1/5}\log n.
\end{aligned}
\tag{6.1}
\]

La media condicionada minimiza el error cuadrático sobre las constantes, por lo que

\[
\operatorname{Var}(Z_{n,h}\mid n,h,S)
\le\mathbb E[(Z_{n,h}-1/2)^2\mid n,h,S].
\]

Esto prueba (1.3) y la cota de varianza para `Z`. La igualdad y las dos
desigualdades de (1.4) se siguen, respectivamente, de (1.1), de la cota de
varianza para `Z` y de `(n+1)^2<=4n^2`. `QED`

La cota es además no trivial en todo el dominio demostrado. En efecto,
`n^(-1/5)log n` es decreciente cuando `log n>5`, en particular para
`n>=10^40`, y

\[
700(10^{40})^{-1/5}\log(10^{40})
=700\cdot10^{-8}\cdot40\log 10
<6.45\times10^{-4}<\frac14.
\tag{6.2}
\]

Esto mejora desde el umbral explícito `n>=10^40` la cota trivial
`Var(Z_{n,h}|n,h,S)<=1/4`, y por reescalado exacto mejora también
`Var(q_{n,h}|n,h,S)<=(n+1)^2/4`.

En forma de conteo relativo, si

\[
\mathcal S_n=\{\pi\in\mathfrak S_n:S(\pi)\},
\qquad
\bar q_{n,h}=|\mathcal S_n|^{-1}
\sum_{\pi\in\mathcal S_n}q_{n,h}(\pi),
\]

entonces se ha demostrado

\[
\sum_{\pi\in\mathcal S_n}
(q_{n,h}(\pi)-\bar q_{n,h})^2
\le2800n^{9/5}\log n\,|\mathcal S_n|.
\tag{6.3}
\]

Aquí \(\mathfrak S_n\) designa siempre el grupo simétrico, \(S\) el suceso de
selección y \(\mathcal S_n\) el subconjunto seleccionado; el grupo no se abrevia.
La desigualdad (6.3) es relativa, con denominador `|mathcal S_n|`; no es una cota
incondicional presentada como si sobreviviera gratuitamente a la selección.

## 7. Consecuencia para la duración y límite exacto de la ruta

De (2.3), (1.3) y `1/(2sqrt(n))<=a_n/2`,

\[
\operatorname{Var}(\mu_n(K_h,L_h)\mid n,h,S)
\le727n^{-1/5}\log n.
\]

El término Beta de (2.1) es a lo sumo `1/n`, que en esta cola es menor que
`n^(-1/5)log n`. Por tanto

\[
\boxed{
V_n^h=\operatorname{Var}(\ell_h\mid n,h,S)
\le730n^{-1/5}\log n.}
\tag{7.1}
\]

En particular `V_n^h->0`. Este resultado no basta para el cociente normalizado: con
la cota inferior disponible `A_n^h>=3/(64,000,000 n)`, (7.1) solo produce una cota
que puede decaer como `n^(-4/5)/log n`.

El factor perdido tiene una localización exacta. Las colas incondicionales de cajas
y discrepancia son exponenciales, pero dividirlas por la cota vigente

\[
\Pr(S)\ge\exp\{-O(n^{4/5}\log n)\}
\]

impide alcanzar la anchura raíz-`n` necesaria y solo permite demostrar
`a_n=n^(-1/10)sqrt(log n)` para `Z_{n,h}`. Para cerrar O3 hace falta una comparación
relativa dentro de `S` que evite esa pérdida. Una formulación suficiente y más
fuerte que el mero segundo momento sería, para constantes `A,b>0`,

\[
\frac{
|\{\pi\in\mathcal S_n:
|q_{n,h}(\pi)-n/2|\ge t\sqrt n\}|}
{|\mathcal S_n|}
\le A e^{-bt^2},
\tag{7.2}
\]

con una cola integrable uniforme. No es necesario demostrar (7.2): la desigualdad
de segundo momento `O(n)` de la nota firmada sigue siendo el objetivo mínimo.

No existe en el repositorio una inyección, recurrencia, desigualdad de Poincaré para
la medida uniforme sobre `mathcal S_n` ni comparación relativa de conteos que cierre
ese factor. Probar una cota marginal más fuerte para `Pr(S)` sería otra ruta
suficiente, pero más fuerte que el objetivo y no se presupone necesaria.

## 8. Techo de afirmación

Esta nota demuestra (1.3)--(1.5), (6.3) y (7.1). No demuestra ni refuta:

- `Var(q_{n,h}|n,h,S)=O(n)`;
- `Var(ell_h|n,h,S)=O(1/n)`;
- `liminf T_n^h>0`;
- ninguna afirmación para canales enriquecidos, poset completo, horizontes, escala
  absoluta o `d>=3`;
- novedad o prioridad bibliográfica.

El bloqueo de la tasa suficiente no es una refutación del objetivo final: numerador
y denominador podrían conservar la misma escala por una ruta más fina no capturada
por la cota inferior actual.

No se consultaron los tamaños sellados para elegir constantes. No se ejecutó ni creó
código, simulación, semilla, dato o artefacto numérico.

## 9. Terminal

Se obtuvo una cota relativa nueva y explícita, pero no la escala `O(n)` firmada. El
terminal único es:

```text
NC2D_TERMINAL = NC2D_PARTIAL_RELATIVE_MOMENT_REDUCTION
NC2D_EQUIVALENCE_O3_TO_SELECTED_Q_VARIANCE = PROVED
NC2D_SELECTED_Z_L2_LIMIT = 1/2
NC2D_SELECTED_Z_MSE_BOUND = 700*n^(-1/5)*log(n)
NC2D_SELECTED_Z_VARIANCE_BOUND = 700*n^(-1/5)*log(n)
NC2D_SELECTED_Q_VARIANCE_BOUND = 2800*n^(9/5)*log(n)
NC2D_SELECTED_Q_BOUND_STATUS = EXACT_RESCALE_OF_Z_VARIANCE_BOUND
NC2D_NONTRIVIAL_FROM_N = 10^40
NC2D_TOTAL_VARIANCE_BOUND = 730*n^(-1/5)*log(n)
NC2D_MISSING_FACTOR_TO_O3 = n^(4/5)*log(n)
NC2D_EXACT_MISSING_OBJECT = RELATIVE_SECOND_MOMENT_ON_SELECTION_EVENT_S_AT_ORDER_N
NC2D_O3 = OPEN
NC2D_LIMINF_T_N = NOT_PROVED
NC2D_NEW_DATA = NO
NC2D_NEW_CODE = NO
NC2D_PR7_MODIFIED = NO
```
