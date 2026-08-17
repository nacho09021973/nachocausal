# `NC-2A` — escala uniforme interior de la cota Beta `b_n(m)`

> **ESTADO: TEOREMA PROBADO · CANAL `fixed-n`, `d=2` · PURAMENTE DEDUCTIVO ·
> SIN DATOS, SEMILLAS, BARRIDOS NUMÉRICOS, CÓDIGO NI ARTEFACTOS NUMÉRICOS
> NUEVOS.**

Autorización firmada:
`docs/program_reopening_note_2026-08-17_nc2a_beta_uniform_scaling_DRAFT.md`.
El sufijo histórico `_DRAFT` del nombre no describe su estado actual: la firma
consta en la §8 de esa nota.

## 1. Objeto y pregunta

Para `2<=m<=n`, sea

\[
F_{\rm relax}(m,n)=
\{(k,l)\in\mathbb Z^2:
2\le k,l\le n-1,\ k,l\ge m-1,\ k+l\le n+m-2\}.
\]

Si `X_k~Beta(k,n+1-k)` y `Y_l~Beta(l,n+1-l)` son independientes, defínase

\[
v_n(k,l)=\operatorname{Var}(\sqrt{X_kY_l}),
\qquad
b_n(m)=\min_{(k,l)\in F_{\rm relax}(m,n)}v_n(k,l).
\]

El Teorema CV-4.1 de
`emergencia/P1a_count_volume_cota_resolucion_d2.md` ya demuestra

\[
\operatorname{Var}(\ell\mid M=m,n,h,S)\ge b_n(m).
\]

`NC-2A` decide la escala de `b_n(m)` cuando `m/n` permanece lejos de `0` y `1`.
No estudia la ley seleccionada de `M`.

## 2. Identidades importadas

`emergencia/P1a_count_volume_lema_kl_d2.md` §§3–5 demuestra que, con

\[
A(x)=\frac{\Gamma(x+1/2)^2}{x\Gamma(x)^2},
\qquad
R(k,n)=\frac{A(k)}{A(n+1)},
\]

se tiene exactamente

\[
v_n(k,l)=
\frac{kl}{(n+1)^2}\{1-R(k,n)R(l,n)\},
\tag{2.1}
\]

y, uniformemente para `1<=k,l<=n`,

\[
0\le v_n(k,l)\le\frac1n.
\tag{2.2}
\]

La cota superior de `NC2A-U` ya estaba, por tanto, cerrada. Falta una cota inferior
uniforme sobre el politopo `F_relax`.

## 3. Lema telescópico exacto para `R(k,n)`

**Lema 3.1.** Para enteros `1<=k<=n`,

\[
R(k,n)=\prod_{j=k}^{n}
\left(1-\frac1{(2j+1)^2}\right).
\tag{3.1}
\]

**Demostración.** De la definición de `A` y
`Gamma(j+1)=j Gamma(j)`, `Gamma(j+3/2)=(j+1/2)Gamma(j+1/2)`,

\[
\frac{A(j+1)}{A(j)}
=\frac{(j+1/2)^2}{j(j+1)}
=\frac{(2j+1)^2}{4j(j+1)}.
\]

Como `4j(j+1)=(2j+1)^2-1`, resulta

\[
\frac{A(j)}{A(j+1)}=1-\frac1{(2j+1)^2}.
\]

Multiplicar desde `j=k` hasta `j=n` telescopa a
`A(k)/A(n+1)=R(k,n)`. `QED`

Esta identidad es exacta; no usa Stirling ni un desarrollo asintótico de Gamma.

## 4. Lema de déficit de producto

Para `2<=k,l<=n`, defínase

\[
S_{k,l,n}
=\sum_{j=k}^{n}\frac1{(2j+1)^2}
+\sum_{j=l}^{n}\frac1{(2j+1)^2}.
\tag{4.1}
\]

**Lema 4.1.** Para `2<=k,l<=n`,

\[
1-R(k,n)R(l,n)\ge\frac12 S_{k,l,n}.
\tag{4.2}
\]

**Demostración.** Sea `a_j=(2j+1)^{-2}` y considérese el multiconjunto de
factores de los dos productos de (3.1). Como `log(1-a)<=-a` para `0<a<1`,

\[
R(k,n)R(l,n)\le e^{-S_{k,l,n}}.
\]

Además,

\[
S_{k,l,n}
\le 2\sum_{j=2}^{\infty}\frac1{(2j+1)^2}
\le \frac12\sum_{j=2}^{\infty}\frac1{j^2}.
\]

Para la función decreciente `x^{-2}`,

\[
\sum_{j=2}^{\infty}\frac1{j^2}
\le\frac14+\int_2^{\infty}\frac{dx}{x^2}
=\frac34,
\]

luego `0<=S_{k,l,n}<=3/8<1`. En `0<=S<=1`,
`e^{-S}<=1-S+S^2/2<=1-S/2`; por tanto

\[
1-R(k,n)R(l,n)
\ge1-e^{-S_{k,l,n}}
\ge\frac12S_{k,l,n}.
\]

`QED`

## 5. Teorema uniforme interior

**Teorema `NC2A-U`.** Para todo `epsilon in (0,1/2)`, tómese

\[
c_\varepsilon=\frac{\varepsilon^3}{288},
\qquad
n_0(\varepsilon)=\left\lceil\frac4\varepsilon\right\rceil.
\]

Entonces, para todo entero `n>=n_0(epsilon)` y todo entero `m` tal que

\[
\varepsilon n\le m\le(1-\varepsilon)n,
\]

el conjunto `F_relax(m,n)` es no vacío y

\[
\boxed{
\frac{\varepsilon^3}{288n}
\le b_n(m)\le\frac1n.}
\tag{5.1}
\]

**Demostración.** Como `n>=4/epsilon`, se tiene `epsilon n>=4`. De aquí
`m>=4` y `m<=n-4`. El punto `(m-1,m-1)` satisface

```text
2 <= m-1 <= n-1,
(m-1)+(m-1) <= n+m-2  <=>  m <= n,
```

por lo que pertenece a `F_relax(m,n)` y el conjunto es no vacío.

Fíjese ahora cualquier `(k,l) in F_relax(m,n)`. Las cotas inferiores del
politopo dan

\[
k,l\ge m-1\ge\varepsilon n-1\ge\frac{\varepsilon n}{2}.
\]

Como `n+1<=2n`, se sigue

\[
\frac{kl}{(n+1)^2}\ge\frac{\varepsilon^2}{16}.
\tag{5.2}
\]

Los dos sumatorios de (4.1) contienen en total, contando multiplicidad,

\[
(n-k+1)+(n-l+1)=2n-k-l+2
\]

términos. La restricción `k+l<=n+m-2` implica

\[
2n-k-l+2\ge n-m+4\ge\varepsilon n+4\ge\varepsilon n.
\tag{5.3}
\]

Cada índice de esos sumatorios es a lo sumo `n`, y por tanto cada término es al
menos `(2n+1)^{-2}`. Como `2n+1<=3n`, (5.3) da

\[
S_{k,l,n}
\ge\frac{\varepsilon n}{(2n+1)^2}
\ge\frac{\varepsilon}{9n}.
\tag{5.4}
\]

Combinando (2.1), el Lema 4.1, (5.2) y (5.4),

\[
v_n(k,l)
\ge
\frac{\varepsilon^2}{16}\,
\frac12\,
\frac{\varepsilon}{9n}
=\frac{\varepsilon^3}{288n}.
\]

La desigualdad vale para **todo** `(k,l) in F_relax(m,n)`, luego también para su
mínimo `b_n(m)`. La cota superior `b_n(m)<=1/n` se obtiene aplicando (2.2) a
cualquier punto del conjunto no vacío. `QED`

## 6. Lectura para `NC-1`

El resultado cierra la parte geométrica de `NC1-O2` sin conocer `w`:

```text
NC1_GEOMETRIC_SCALE_ON_INTERIOR_WINDOWS = 1/n
NC1_CAN_TAKE_a_n_squared = 1/n
```

En efecto, para cualquier `epsilon` fijo, si posteriormente se demuestra

\[
\Pr\{\varepsilon n\le M\le(1-\varepsilon)n\mid n,h,S\}\ge p>0
\]

en una cola completa, entonces

\[
\mathbb E[b_n(M)\mid n,h,S]
\ge\frac{p\varepsilon^3}{288n}.
\]

Para aplicar la Proposición `NC1-P` aún faltarían, de manera independiente:

1. `NC1-O1`: existencia de la ley condicionada en una cola completa;
2. la parte de selección de `NC1-O2`: masa no evanescente de `M` en alguna ventana
   interior fija;
3. `NC1-O3`: `Var(ell|n,h,S)=O(1/n)`.

`NC-2A` no prueba ninguna de esas tres afirmaciones y, por tanto, no prueba
`liminf T_n^h>0`.

## 7. Alcance y controles negativos

- No se leyó ningún dato sellado para elegir `epsilon`; el teorema cuantifica sobre
  todo `epsilon in (0,1/2)`.
- No se usaron simulaciones ni barridos finitos.
- No se modificaron `b_n`, `F_relax`, `M`, `S` ni `MIN_COVERAGE_LEX`.
- No se resolvió `w`, ni se afirmó concentración seleccionada.
- El resultado es solo para la geometría Beta del canal `fixed-n`, `d=2`.
- No se obtiene un resultado para canales enriquecidos, el poset completo,
  horizontes o `d>=3`.
- No se formula ninguna afirmación de novedad o prioridad.

## 8. Terminal

La identidad telescópica exacta y la geometría de `F_relax` prueban `NC2A-U`
con constantes explícitas. El terminal único es:

```text
NC2A_TERMINAL = NC2A_PROVED_UNIFORM_INTERIOR_N_INV
NC2A_CONSTANT = epsilon^3/288
NC2A_N0 = ceil(4/epsilon)
NC2A_UPPER_BOUND = 1/n
NC2A_SELECTION_MASS = OPEN
NC2A_EVENTUAL_CONDITIONAL_LAW = OPEN
NC2A_TOTAL_VARIANCE_SCALE = OPEN
NC2A_LIMINF_T_N = NOT_PROVED
NC2A_NEW_DATA = NO
NC2A_NEW_CODE = NO
```
