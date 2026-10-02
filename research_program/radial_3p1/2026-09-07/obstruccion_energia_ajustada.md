# La energia ajustada al adjunto tampoco es positiva

Fecha: 2026-09-07. Nota exploratoria con contraejemplos exactos.

**Resultado:** se descarta una desigualdad auxiliar en ambos sectores de
paridad, incluso con condicion diagonal exacta y normalizacion temporal.
**No se demuestra ni se refuta el limite cero de las capacidades.**
Los resultados congelados no se modifican.

## 1. La desigualdad que se comprueba

Con las convenciones del criterio conjunto, sean
\[
d=y-x,\quad m=x+y-1,\quad
\omega=x(1-x)y(1-y),\quad
\chi=2((1-x)(1-y)+xy).
\]
Si \(S\) es la inversa de la segunda derivada con condiciones de Dirichlet,
\[
S(z^j)=\frac{z^{j+2}-z}{(j+1)(j+2)},\qquad
W_g=\omega^{-1}(S\otimes S)g.
\]
Para polinomios antisimetricos reales definimos
\[
q_\chi(g)=\left\langle Kg,\frac{\chi W_g}{d}\right\rangle_{L^2(Q)}.
\tag{1}
\]
En esta clase \(W_g\) es polinomico y divisible por \(d\), por lo que
(1) no requiere interpretar ninguna singularidad ni integrar por partes
en un borde singular. No se afirma aqui una extension acotada de (1) a
todo \(L^2\).

La motivacion no era arbitraria: \(g_t=dm\), \(W_{g_t}=g_t/24\), y el
[modo exacto del adjunto](levantamiento_polinomico_dual.md) satisface
\[
\frac{\chi W_{g_t}}d=\frac{m\chi}{24},\qquad K^*(m\chi)=0.
\tag{2}
\]
Por tanto, para todo polinomio antisimetrico \(g\) y escalar real \(c\),
\[
q_\chi(g-cg_t)=q_\chi(g).
\tag{3}
\]
En efecto, \(K(g-cg_t)=Kg\) y el cambio en la funcion de prueba es un
multiplo de \(m\chi\), ortogonal al rango de \(K\).

Se queria comprobar si la condicion necesaria de diagonal
\[
(Kg)(z,z)=0
\tag{4}
\]
hacia no negativa esta forma. La respuesta es **no**, en ambas paridades.

## 2. Contraejemplo en el sector de dato par

Sea
\[
g_{\mathrm e}=\frac d{15}
\left(51d^4-2610d^2m^2-70d^2-465m^4+270m^2+43\right).
\tag{5}
\]
Es antisimetrico, de grado cinco, y satisface
\[
g_{\mathrm e}(1-x,1-y)=-g_{\mathrm e}(x,y),\qquad
(Kg_{\mathrm e})(z,z)=0,
\]
\[
\boxed{q_\chi(g_{\mathrm e})=-\frac{22094}{35083125}<0.}
\tag{6}
\]
Como \(B\rho=-\mathcal R B\), el dato \(Bg_{\mathrm e}\) es par y
\(v_1(Bg_{\mathrm e})=0\) automaticamente.

## 3. Contraejemplo en el sector de dato impar

Definamos
\[
\begin{aligned}
p(d,m)={}&18075d^6+140175d^4m^2-20559d^4
 +11025d^2m^4\\
&-60550d^2m^2+4545d^2+10725m^6-20139m^4+9585m^2,\\
g_{\mathrm o}={}&\frac{4dm}{105}p(d,m).
\end{aligned}
\tag{7}
\]
Este polinomio antisimetrico de grado ocho satisface
\[
g_{\mathrm o}(1-x,1-y)=g_{\mathrm o}(x,y),\qquad
(Kg_{\mathrm o})(z,z)=0,
\]
\[
\boxed{q_\chi(g_{\mathrm o})=-\frac{2035318048}{2659406124375}<0.}
\tag{8}
\]
La correccion
\[
\widetilde g_{\mathrm o}=g_{\mathrm o}-\frac{19132}{1155}g_t
\tag{9}
\]
cumple \(v_1(B\widetilde g_{\mathrm o})=0\). Por (3), conserva exactamente
la energia negativa (8), la condicion diagonal y la paridad.

## 4. Certificacion y alcance

Las identidades anteriores se obtienen aplicando la formula integral
polinomica de \(K\), la formula de \(S\) y la formula de los dos marginales
de \(B\). No dependen de autovalores calculados en coma flotante.
Como comprobacion independiente de las integrales finales se usa
\[
\int_Q d^{2r}m^{2s}\,dx\,dy
=\frac{2(2r)!(2s)!}{(2r+2s+2)!}.
\tag{10}
\]
Si algun exponente es impar, la integral es cero. Esto se sigue del cambio
\((x,y)\mapsto(m,d)\), con jacobiano absoluto \(1/2\), cuya imagen es
\(\{|m|+|d|<1\}\), y de una integral beta elemental en cada cuadrante.

El verificador conserva el argumento de grado seis y comprueba por separado
el de grado ocho:

```text
python3 research_program/radial_3p1/2026-09-07/verify_adjoint_matched_energy.py --degree 6
python3 research_program/radial_3p1/2026-09-07/verify_adjoint_matched_energy.py --degree 8
```

Codigo: [verify_adjoint_matched_energy.py](verify_adjoint_matched_energy.py).
Salidas: [grado seis](verification_adjoint_matched_energy.json) y
[grado ocho](verification_adjoint_matched_energy_degree_8.json).
Se verifican los hashes de los tres archivos congelados antes y despues.

En el sector impar, la restriccion diagonal de grado a lo sumo seis tiene
dimension cuatro, rango tres y forma semidefinida positiva. A grado ocho
tiene dimension siete, rango seis y ya contiene (7). Este cambio muestra
concretamente por que la positividad de truncamientos no prueba una
desigualdad para todos los grados.

Los testigos no son soluciones de \(Kg=0\): su energia negativa implica
\(Kg\ne0\). Tampoco se afirma que sean reconstrucciones admisibles
\(g=Gb\). Se refuta la positividad sobre la clase definida por paridad,
condicion diagonal y normalizacion; no una desigualdad sobre una clase
mas estrecha que incorpore otras restricciones exactas de admisibilidad.

La energia conjunta \(\widehat Q_N\), que es positiva por construccion,
no es la forma (1). Ningun resultado sobre ella se invalida. El objetivo
pendiente sigue siendo construir los aproximantes de la ecuacion (15) de
[capacidades como distancias](capacidades_como_distancias.md), o demostrar
por otra via que sus residuos tienden a cero. Esta nota descarta un
intento de positividad; no aporta esa construccion.
