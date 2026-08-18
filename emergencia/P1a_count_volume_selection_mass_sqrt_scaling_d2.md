# `NC-2F-a` — masa de selección con exponente raíz y exponente de varianza `3/2`

> **ESTADO: TEOREMA PROBADO · CANAL `fixed-n`, `d=2` · PURAMENTE DEDUCTIVO ·
> RE-PARAMETRIZACIÓN DEL PARÁMETRO LIBRE `rho` DE `NC-2C` §4.1 ·
> `NC-2C` NO SE MODIFICA · `NC2E-O3` SIGUE ABIERTO ·
> SIN DATOS, SIMULACIONES, SEMILLAS, CÓDIGO NI ARTEFACTOS NUMÉRICOS NUEVOS.**

Autorización: `docs/program_reopening_note_2026-08-18_nc2f_variance_exponent_reduction.md`.

## 1. Objeto

`NC-2C` §4 construye una familia prescrita `F_n` con una cuádrupla plantada `q_0`
y demuestra `F_n cap G_n subseteq S`, de donde

\[
\Pr_n(S)\ \ge\ \tfrac12\,n^{-(2n^{4/5}+4)}
\tag{1.1}
\]

para todo `n>=10^{40}`. La elección `rho=floor(n^{4/5})` es un **parámetro libre**
de la construcción: sólo interviene en las desigualdades de margen del Lema 4.1 de
`NC-2C`. Esta nota decide cuál es el orden mínimo de `rho` compatible con ese
Lema, tal como está escrito, y qué cota resulta.

No se corrige nada de `NC-2C`: (1.1) es correcta y permanece publicada. Lo que se
prueba aquí es una cota adicional más fuerte con otra elección del mismo parámetro
libre.

## 2. La construcción, con `rho` genérico

Se copia literalmente la construcción de `NC-2C` §4.1, dejando `rho` sin fijar.
Sea `n=2s` par y

\[
r=2\rho+2,\qquad N=n-r,\qquad
q_1=\lfloor n/4\rfloor,\qquad q_3=\lfloor3n/4\rfloor .
\tag{2.1}
\]

La familia `F_n` prescribe

```text
pi(1)=1,       pi(n)=n,
pi(s)=s,       pi(s+1)=s+1,
pi(s-rho+j)=q_1+j,   j=1,...,rho-1,
pi(s+1+j)=q_3+j,     j=1,...,rho-1,
```

de modo que `Pr(F_n)=N!/n!=1/(n)_r`, la cuádrupla plantada es
`q_0=((1,1),(s,s),(s+1,s+1),(n,n))`, y sus dos cardinalidades libres cumplen

\[
K_0=L_0,\qquad
\mathbb E[K_0\mid F_n]=\frac N4+\rho+1 .
\tag{2.2}
\]

Sea `G_n` el suceso de discrepancia de la biyección libre, con

\[
\eta=\sqrt{20N\log n},
\qquad
\Pr(G_n\mid F_n)\ge1-2n^{-6},
\tag{2.3}
\]

y sobre `G_n` todo conteo libre rectangular dista a lo sumo `eta` de su media.

Todo lo anterior es independiente de `rho` salvo por (2.1). El análisis de casos
del Lema 4.1 de `NC-2C` (casos 1, 2 y 3 de su demostración) tampoco depende de
`rho`: los topes de puntos prescritos por bloque (`2` en el bloque que pierde su
escalera, `rho+2` en el otro, `2rho+2` en el caso 3) y la optimización

\[
\sqrt f=\frac12+\frac\rho{2N},
\qquad
\min(K(q),L(q))\le\frac N4+\frac\rho2+\frac{\rho^2}{4N}+2+\eta
\tag{2.4}
\]

son identidades algebraicas en `rho`. Lo único que hay que re-verificar son las
**cinco desigualdades de margen** que cierran el Lema.

## 3. Las cinco desigualdades de margen

Con la cota plantada `K_0=L_0>=N/4+rho+1-eta` de (2.2)–(2.3), el Lema 4.1 de
`NC-2C` se cierra si y sólo si se cumplen:

\[
\textbf{(M1)}\quad \frac\rho2-1-\frac{\rho^2}{4N}-2\eta>0
\qquad\text{(caso 2, contra (2.4))},
\tag{3.1}
\]

\[
\textbf{(M2)}\quad \frac N{12}-\rho-1-2\eta>0
\qquad\text{(caso 3, contra }\tfrac N6+2\rho+2+\eta),
\tag{3.2}
\]

\[
\textbf{(M3)}\ \rho<\frac n4,
\qquad
\textbf{(M4)}\ N\ge0.99\,n,
\qquad
\textbf{(M5)}\ \frac{n/4+\rho+1}N<\frac13 .
\tag{3.3}
\]

(M5) es la desigualdad usada en el caso 3 para acotar por `1/6` el producto libre
del bloque rival; (M4) es la cota de `N` empleada en las estimaciones; (M3)
garantiza que las asignaciones prescritas son distintas.

## 4. Elección `rho = ceil(20 sqrt(n log n))` y verificación

**Teorema 4.1.** Para todo `n>=10^{40}`, la elección

\[
\rho=\left\lceil20\sqrt{n\log n}\right\rceil
\tag{4.1}
\]

satisface (M1)–(M5).

**Demostración.** Escríbase `L=log n` y obsérvese que `L>=92` en el dominio.

*(M3).* `rho<=20sqrt(nL)+1`, y `20sqrt(nL)+1<n/4` equivale, dividiendo por
`sqrt n`, a `20sqrt L+1/sqrt n<sqrt n/4`, es decir a
`sqrt n>80sqrt L` salvo un término despreciable; en `n=10^{40}` se tiene
`sqrt n=10^{20}` y `80 sqrt L=80\cdot9.6=768`. La desigualdad es cierta con margen
`10^{17}` y el miembro izquierdo crece como `sqrt n` frente a `sqrt(log n)`.

*(M4).* `n-N=2\rho+2\le40\sqrt{nL}+4`, y
`40\sqrt{nL}+4\le0.01n` equivale a `\sqrt n\ge4000\sqrt L` salvo términos menores;
en `n=10^{40}`, `4000\sqrt L=38\,400\ll10^{20}`. Luego `N>=0.99n`, y de hecho
`N>=(1-4\cdot10^{-18})n` en el umbral.

*(M5).* Por (M4), `(n/4+\rho+1)/N\le(0.25n+0.005n)/(0.99n)=0.2576<1/3`.

*(M1).* Por (M4), `\eta=\sqrt{20N\log n}\le\sqrt{20nL}=4.4722\sqrt{nL}`, luego
`2\eta\le8.945\sqrt{nL}`. Además `\rho/2\ge10\sqrt{nL}` y

\[
\frac{\rho^2}{4N}
\le\frac{(20\sqrt{nL}+1)^2}{4\cdot0.99n}
=\frac{400nL+40\sqrt{nL}+1}{3.96n}
\le101.02\,L+11\sqrt{L/n}+1
\le102\,L .
\]

Por tanto el miembro izquierdo de (3.1) es al menos

\[
10\sqrt{nL}-8.945\sqrt{nL}-102L-1
=1.055\sqrt{nL}-102L-1 ,
\]

que es positivo si `1.055\sqrt n>102\sqrt L+1/\sqrt L`, es decir si
`\sqrt n>97\sqrt L`, o sea `n>9409\,L`. En `n=10^{40}`: `9409\cdot92.1=8.7\cdot10^5`.
El margen efectivo en el umbral es `1.055\sqrt{nL}\approx1.01\cdot10^{22}`.

*(M2).* Por (M4), `N/12\ge0.0825n`, y
`\rho+1+2\eta\le20\sqrt{nL}+2+8.945\sqrt{nL}\le29\sqrt{nL}+2`. La desigualdad
`0.0825n>29\sqrt{nL}+2` equivale, salvo el término aditivo, a
`\sqrt n>352\sqrt L`, es decir `n>124\,000\,L`; en `n=10^{40}` el miembro izquierdo
vale `8.25\cdot10^{38}` y el derecho `2.8\cdot10^{22}`.

Las cinco desigualdades se cumplen en `n=10^{40}` y sus márgenes crecen con `n`,
porque en las cinco el miembro dominante es una potencia de `n` estrictamente mayor
que la del miembro opuesto. `QED`

**Observación 4.2.** El umbral `10^{40}` se hereda de la cadena `NC-2C`–`NC-2E`;
las cinco desigualdades se cumplen ya desde `n` del orden de `10^{7}`. No se ha
optimizado el umbral: hacerlo no cambiaría ningún exponente.

**Observación 4.3.** El orden `sqrt(n log n)` es el mínimo que (M1) tolera: el
margen del caso 2 es `rho/2` y el ruido de la biyección libre es
`2eta = Theta(sqrt(n log n))`, de modo que `rho` debe superar
`4sqrt(20 n log n)`. La constante `20` de (4.1) es una elección cómoda, no óptima.

## 5. Cota de masa de selección

**Teorema 5.1.** Para todo `n>=10^{40}`,

\[
\boxed{\ \Pr_n(S)\ \ge\ \frac12\,n^{-\left(40\sqrt{n\log n}+5\right)}\ }
\tag{5.1}
\]

y, en particular,

\[
\log\frac1{\Pr_n(S)}\ \le\ 41\,\sqrt n\,(\log n)^{3/2}.
\tag{5.2}
\]

**Demostración.** Para `n` par, el Teorema 4.1 permite aplicar el Lema 4.1 de
`NC-2C` con `rho` dado por (4.1), de modo que `F_n cap G_n subseteq S` con ganador
único `q_0`. Por (2.3) y `Pr(F_n)=1/(n)_r>=n^{-r}`,

\[
\Pr_n(S)\ \ge\ (1-2n^{-6})\,n^{-r},
\qquad
r=2\rho+2\le40\sqrt{n\log n}+4 .
\]

Como `1-2n^{-6}>=1/2`, se obtiene (5.1) para `n` par.

Para `n` impar se usa la inyección de `NC-2C` §4.4, que envía una permutación
`sigma` de `n-1` elementos a `(\sigma(1)+1,\ldots,\sigma(n-1)+1,1)`: el último
punto es incomparable con todos los demás, no pertenece a ninguna 4-cadena ni a
ningún intervalo con endpoints anteriores, y por tanto el selector, su unicidad y
las cardinalidades no cambian. Luego `Pr_n(S)>=Pr_{n-1}(S)/n`. Como
`rho` es creciente en `n`, el exponente de `n-1` no supera el de `n`, y el factor
`1/n` añade una unidad al exponente: se obtiene (5.1) con el sumando `+5`.

Para (5.2), `log(1/Pr_n(S))<=(40sqrt(n log n)+5)log n+log2`, y en el dominio
`n>=10^{40}` el término `5log n+log 2` es menor que `sqrt n(log n)^{3/2}`. `QED`

`NC-2C` (4.14) sigue siendo válida y no se modifica; (5.1) es estrictamente más
fuerte para `n>=10^{40}`, porque `40sqrt(n log n)+5<2n^{4/5}+4` en ese dominio
(en `n=10^{40}`: `3.8\cdot10^{22}` frente a `2\cdot10^{32}`).

**Corolario 5.2 (monotonía de las consecuencias de `NC-2C`).** Toda cota de
`NC-2C` §6 que use (4.14) sólo mediante `Pr(S)>=...` se mantiene o mejora al
sustituir (4.14) por (5.1); en particular el Teorema `NC2C-O2` (masa interior
uniforme con `epsilon=3/100`, `p=1/2`, `n_0=10^{40}`) sigue valiendo, con margen
mayor. No se promueve ningún token de `NC-2C`.

## 6. Consecuencia para la varianza seleccionada

**Teorema 6.1.** Para ambos lados `h` y todo `n>=10^{40}`,

\[
\boxed{\
\operatorname{Var}_{\nu_n}(q_{n,h})\ \le\ 4.2\cdot10^{7}\,n^{3/2}(\log n)^{3/2},
\qquad
\operatorname{Var}(\ell_h\mid n,h,S)\ \le\ 4.3\cdot10^{7}\,\frac{(\log n)^{3/2}}{\sqrt n}. }
\tag{6.1}
\]

**Demostración.** El Teorema 7.1 de `NC-2E` prueba

\[
\operatorname{Var}_{\nu_n}(q_{n,h})
\le10^6\,n\left[\log\frac1{\Pr_n(S)}+4\log n\right],
\qquad n\ge10^{40},
\]

y su demostración usa una cota inferior para `Pr_n(S)` sólo en dos pasos técnicos
del Lema 6.3, que exigen `L_n<=n/1024` y `Pr_n(S)>=e^{-n/2048}`; ambas condiciones
son **monótonas** en `Pr_n(S)` y se cumplen a fortiori con (5.1). Sustituyendo
(5.2),

\[
\operatorname{Var}_{\nu_n}(q_{n,h})
\le10^6n\left[41\sqrt n(\log n)^{3/2}+4\log n\right]
\le4.2\cdot10^{7}\,n^{3/2}(\log n)^{3/2},
\]

donde se usó `4log n<=0.03 sqrt n(log n)^{3/2}` en el dominio.

Para la duración, `NC-2D` (2.4) prueba que `Var(q_{n,h}|S)<=C_q n` implica
`Var(ell_h|n,h,S)<=[1+(\sqrt{C_q}+1/2)^2]/n`. Con
`C_q=4.2\cdot10^{7}\sqrt n(\log n)^{3/2}` se tiene
`(\sqrt{C_q}+1/2)^2\le C_q+\sqrt{C_q}+1/4\le1.001\,C_q`, luego

\[
\operatorname{Var}(\ell_h\mid n,h,S)
\le\frac{1+1.001\,C_q}n
\le4.3\cdot10^{7}\frac{(\log n)^{3/2}}{\sqrt n}. \qquad\textsf{QED}
\]

**Corolario 6.2 (comparación con `NC-2D`).** Las cotas de `NC-2D` eran
`2800n^{9/5}\log n` y `730n^{-1/5}\log n`. Las de (6.1) son estrictamente mejores
en todo el dominio probado: en `n=10^{40}`,

\[
\operatorname{Var}(\ell_h\mid n,h,S)\le3.8\cdot10^{-10}
\quad\text{frente a}\quad
6.7\cdot10^{-4},
\]

y el cociente entre ambas, `5.9\cdot10^{4}n^{-3/10}(\log n)^{1/2}`, tiende a cero
(vale `5.7\cdot10^{-7}` en el umbral). El
exponente de varianza de la forma seleccionada baja de `9/5` a `3/2`.

**Corolario 6.3 (lo que sigue faltando).** La escala requerida por `NC2E-O3`
es `C_q n`. Tras (6.1) el factor que falta es `sqrt n(\log n)^{3/2}` en vez de
`n^{4/5}\log n`. Por la Proposición 7.4 de `NC-2E`, ninguna mejora ulterior de
`Pr_n(S)` puede cerrar ese factor por sí sola: el suelo de esa familia es
`n\log n`.

## 7. Techo de afirmación

Se demuestran el Teorema 4.1, el Teorema 5.1 con (5.2), el Corolario 5.2 y el
Teorema 6.1 con sus corolarios. No se demuestra ni se refuta:

- `NC2E.1` (`Var_{nu_n}(q_{n,h})=O(n)`), que sigue abierta;
- `Var(ell_h|n,h,S)=O(1/n)`;
- `liminf T_n^h>0`;
- optimalidad de `rho`, de la constante `20` ni del umbral `10^{40}`;
- ninguna afirmación para canales enriquecidos, poset completo, horizontes, escala
  absoluta o `d>=3`;
- novedad o prioridad bibliográfica.

No se modificó `NC-2C` ni ningún token publicado. No se tocó el sello, no se usaron
semillas, no se consultaron los tamaños sellados y no se creó ni ejecutó código,
simulación, dato o artefacto numérico. No se modificó la PR #7.

## 8. Terminal

```text
NC2F_A_TERMINAL = NC2F_A_PROVED_SQRT_SELECTION_MASS
NC2F_A_RHO = ceil(20*sqrt(n*log n))
NC2F_A_MARGINS_VERIFIED = M1,M2,M3,M4,M5
NC2F_A_SELECTION_MASS_BOUND = (1/2)*n^(-(40*sqrt(n*log n)+5))
NC2F_A_LOG_INVERSE_MASS = 41*sqrt(n)*(log n)^(3/2)
NC2F_A_SELECTED_Q_VARIANCE_BOUND = 4.2*10^7*n^(3/2)*(log n)^(3/2)
NC2F_A_SELECTED_ELL_VARIANCE_BOUND = 4.3*10^7*(log n)^(3/2)/sqrt(n)
NC2F_A_VARIANCE_EXPONENT = 3/2
NC2F_A_IMPROVES_NC2D = YES_ON_THE_WHOLE_PROVED_DOMAIN
NC2F_A_NC2C_MODIFIED = NO
NC2F_A_NC2E_O3 = OPEN
NC2F_A_LIMINF_T_N = NOT_PROVED
NC2F_A_NEW_DATA = NO
NC2F_A_NEW_CODE = NO
NOVELTY_CERTIFIED = NO
```
