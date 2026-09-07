# Auditoría algebraica del canal normal lateral

**Fecha:** 2026-09-07  
**Estado:** identidades algebraicas cerradas; la justificación de una expansión Mellin/conormal de una reconstrucción global sigue abierta.

## Punto de partida

En `energia_positiva_y_reduccion_de_borde.md`, con
\[
Sf(x)=\int_0^x(x-s)f(s)\,ds-x\int_0^1(1-s)f(s)\,ds,
\quad a=x(1-x),\quad J=a^{-1}S,
\]
se tiene, para \(\Re p>-1\),
\[
S(x^p)=\frac{x^{p+2}-x}{(p+1)(p+2)},\qquad
\boxed{J(x^p)=\frac{x^{p+1}-1}{(1-x)(p+1)(p+2)}}.
\tag{1}
\]
La primera fórmula sigue de dos integrales de Euler elementales; la segunda es división por \(a\).

## Consecuencias exactas

Multiplicar (1) por \(1-x\) da
\[
(1-x)J(x^p)=\frac{x^{p+1}-1}{(p+1)(p+2)}.
\tag{2}
\]
En particular, si \(\kappa=(\beta+1)(\beta+2)\),
\[
(1-y)J(y^\beta)=\frac{y^{\beta+1}-1}{\kappa}.
\]
Para
\[
\mathscr A_\tau h=yh-\kappa(1-y)Jh
\]
queda
\[
\boxed{\mathscr A_\tau(y^\beta)=1.}
\tag{3}
\]

En el canal \(\alpha=-\tfrac12+i\tau\), el término no entero inicial de (1) es
\[
\frac{x^{\alpha+1}}{(\alpha+1)(\alpha+2)}.
\]
Como \(\alpha\notin\mathbb Z\), no se mezcla con la familia analítica al desarrollar
\[
\frac1{1-x}=\sum_{n\ge0}x^n.
\]
La parte normal de
\[
\mathcal X=-c_x\partial_x+c_y\partial_y
]
en \(x=0\) es \(-(1-y)\partial_x\). Junto con el factor 6 de
\(\mathscr A g=(y-x)g+6\mathcal XW_g\), esto da
\[
\boxed{\kappa(\tau)=\frac6{\alpha+2}=
\frac6{3/2+i\tau}.}
\tag{4}
\]

La identidad auxiliar necesaria para la corrección de rango uno es
\[
Lh=(1-y)Jh+m(h),qquad m(h)=\int_0^1(1-y)h(y)\,dy.
\tag{5}
\]
Se obtiene directamente de las definiciones de \(S,J,L\).

## Umbral \(L^2\) de la respuesta forzada

La respuesta formal es \(h=y^{\beta(\tau)}\), con
\[
\beta(\tau)=\frac{-3+\sqrt{w(\tau)}}2,qquad
w=1+\frac{24}{3/2+i\tau},
\]
usando la raíz principal. La condición \(h\in L^2(0,1)\) es
\(\Re\beta>-1/2\), equivalente a \(\Re\sqrt w>2\).

Si \(\sqrt w=u+iv\), \(u\ge0\), entonces
\[
u^2=\frac{|w|+\Re w}{2},
]
por lo que \(u>2\iff |w|+\Re w>8\). Con
\[
s=\frac94+\tau^2,quad \Re w=1+\frac{36}{s},quad |w|^2=1+\frac{648}{s},
\]
la desigualdad es equivalente a
\[
s^2-24s+27<0.
\]
Dado \(s\ge9/4\), resulta
\[
\boxed{\tau^2<\frac{39}{4}+3\sqrt{13}},
\qquad |\tau|<4.5350472794\ldots .
\tag{6}
\]

## Alcance

(1)--(6) son identidades algebraicas y un criterio de integrabilidad de la fibra formal. No prueban que una reconstrucción general admisible admita una expansión que contenga ese canal, ni controlan el resto ni las esquinas. Por ello no prueban una condición global de admisibilidad ni la unicidad del núcleo radial.

El verificador `verify_normal_channel_algebra.py` comprueba simbólicamente las identidades racionales y el polinomio del umbral. La separación de familias de potencias se justifica en el texto, pues requiere \(\alpha\notin\mathbb Z\).
