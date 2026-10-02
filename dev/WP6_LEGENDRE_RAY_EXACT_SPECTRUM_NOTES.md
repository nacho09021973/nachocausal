# WP6 — espectro exacto exploratorio del rayo de Legendre

```text
STATUS = EXPLORATORY_EXACT_ARITHMETIC
DENOMINATOR = I_N^Pi
N = 4,5,6
ASYMPTOTIC_CLAIM = NONE
K1_EXACT_VISIBILITY_STATUS = PROBADO_FOR_ALL_N_GE_2
```

Backend reproducible:
`dev/wp6_legendre_ray_exact_spectrum.py`.

Comando:

```bash
.venv/bin/python dev/wp6_legendre_ray_exact_spectrum.py --n 4 5 6
```

Se usan los modos de Legendre desplazados ortonormales `e_k` y el rayo

\[
f^{(M)}=\sum_{k=1}^M k^{-2}e_k\otimes e_k.
\]

## Retención diagonal por modo

| `N` | `k=1` | `k=2` | `k=3` | `k=4` | `k=5` |
|---:|---:|---:|---:|---:|---:|
| 4 | 1 | 11/12 | 11/12 | — | — |
| 5 | 1 | 41/45 | 293/360 | 439/504 | — |
| 6 | 1 | 353/384 | 228517/279936 | 3489/4480 | 1191689/1399680 |

En decimales:

| `N` | `k=1` | `k=2` | `k=3` | `k=4` | `k=5` |
|---:|---:|---:|---:|---:|---:|
| 4 | 1.000000 | 0.916667 | 0.916667 | — | — |
| 5 | 1.000000 | 0.911111 | 0.813889 | 0.871032 | — |
| 6 | 1.000000 | 0.919271 | 0.816319 | 0.778795 | 0.851401 |

## Retención del rayo truncado

| `N` | `M=1` | `M=2` | `M=3` | `M=4` | `M=5` |
|---:|---:|---:|---:|---:|---:|
| 4 | 1 | 1739/1740 | 6901763/6906252 | — | — |
| 5 | 1 | 3961/3965 | 3593167/3597552 | 919851671/920973816 | — |
| 6 | 1 | 24929/24960 | 92736646399/92884724352 | 26496261416069/26538606046080 | 14026457732044403003/14048874778809951360 |

Los agregados decimales a truncamiento máximo son `0.9993500` (`N=4`),
`0.9987816` (`N=5`) y `0.9984044` (`N=6`). La cercanía a uno está dominada
por el peso `k^(-4)` del primer modo, que tiene retención exacta uno; no es
evidencia por sí sola de uniformidad HS.

## Gram y lectura

El backend imprime las matrices racionales completas `I_N^Pi` e `I_N^[P]`.
En esta base `I_N^Pi` resulta diagonal para `N=4,5,6`; `I_N^[P]` tiene términos
cruzados entre los modos `k>=2`. Por tanto la fórmula del rayo debe usar la
forma cuadrática completa del numerador y no solo una media de eficiencias
diagonales.

El modo `k=1` tiene retención exacta uno en los tres tamaños. Los modos fijos
`k=2,3` no muestran monotonía entre `N=4,5,6`; esto no contradice el teorema
de rango finito, que es asintótico, pero impide usar estos tres puntos para
justificar el intercambio `M <-> N`. El rango infinito HS estaba abierto al escribirse esta nota; quedo cerrado en la hoja de ruta de septiembre 2026 §5.3 (Teorema 12), por una via que no usa este rayo ni ningun dato de N=4,5,6.

## Lema del primer modo

**Lema (formulado como candidato).** Para todo `N>=4`,

\[
\eta_N(e_1^{\otimes2})=1.
\]

Equivalentemente, `s_N^(1)` es constante en cada clase de isomorfismo de
`P_sigma`.

```text
K1_EXACT_VISIBILITY_STATUS = PROBADO
```

De hecho la prueba vale para todo `N>=2`. Numeremos posiciones y valores desde
uno. Para el modo de Legendre desplazado ortonormal

\[
e_1(u)=\sqrt3(2u-1),
\]

la media en el estadístico de orden `i` es

\[
a_{i,N}:=\mathbb E[e_1(U_{(i)})]
=\frac{\sqrt3}{N+1}(2i-N-1).
\]

Por tanto el score de rangos de la dirección diagonal es

\[
\begin{aligned}
s_N^{(1)}(\sigma)
&=2\sum_{i=1}^N a_{i,N}a_{\sigma(i),N}\\
&=\frac{24}{(N+1)^2}\sum_{i=1}^N i\sigma(i)-6N\\
&=\frac{2N(N-1)}{N+1}
  -\frac{12}{(N+1)^2}\sum_{i=1}^N(i-\sigma(i))^2.
\end{aligned}
\tag{1}
\]

Es, salvo el factor `2N(N-1)/(N+1)`, la rho de Spearman de la permutación:

\[
s_N^{(1)}(\sigma)
=\frac{2N(N-1)}{N+1}\,\rho_{\rm Sp}(\sigma).
\tag{2}
\]

Falta ver por qué esta cantidad, que no es un invariante de permutaciones
arbitrarias bajo conjugación, sí es invariante de la clase del poset de
permutación. Sea `G_sigma` el grafo de incomparabilidad de `P_sigma`: sus
aristas son exactamente las inversiones `{i,j}`. Orientemos cada arista desde
la menor posición hacia la mayor. Si `d^+(i)` y `d^-(i)` son los grados de
salida y entrada en esta orientación, entonces

\[
\sigma(i)-i=d^+(i)-d^-(i).
\tag{3}
\]

La orientación es transitiva. En cualquier orientación transitiva de un grafo
de comparabilidad, cada par formado por una arista entrante y otra saliente en
un vértice cierra un triángulo, y cada triángulo tiene un único vértice
intermedio. En consecuencia,

\[
\sum_i d^+(i)d^-(i)=t(G_\sigma),
\tag{4}
\]

donde `t(G)` es el número de triángulos. Usando
`d(i)=d^+(i)+d^-(i)`, (3)--(4) dan

\[
\boxed{
\sum_{i=1}^N(i-\sigma(i))^2
=\sum_{v\in G_\sigma}d(v)^2-4t(G_\sigma).
}
\tag{5}
\]

El lado derecho depende sólo del grafo de incomparabilidad no etiquetado, que
a su vez está determinado por el poset no etiquetado. Así (1) es constante en
cada fibra `Gamma_C`. La varianza condicional es cero y, como
`I_N^Pi(e_1^tensor2)>0` para `N>=2`, se concluye
`eta_N(e_1^tensor2)=1`.

## Contraejemplos para los modos 2 y 3

Ya en `N=4`, tómense, en notación uno-basada,

\[
\sigma=(3,4,2,1),\qquad \tau=(4,2,3,1).
\tag{6}
\]

`P_sigma` tiene como única relación estricta `1<2`, mientras `P_tau` tiene
como única relación estricta `2<3`. El mapa

\[
1\mapsto2,\quad2\mapsto3,\quad3\mapsto1,\quad4\mapsto4
\tag{7}
\]

es un isomorfismo. Sin embargo, el backend racional exacto obtiene

\[
\begin{array}{c|cc}
 &s_4^{(2)}&s_4^{(3)}\\ \hline
\sigma&0&-8/175\\
\tau&8/5&32/175.
\end{array}
\tag{8}
\]

Por tanto ninguno de esos scores es constante en fibras, coherentemente con
`eta_4=11/12<1` en ambos modos. Como ejemplo de mezcla modal ya calculado,

\[
I_4^{[P]}(e_2^{\otimes2},e_3^{\otimes2})=-\frac{16}{1575},
\qquad
I_4^\Pi(e_2^{\otimes2},e_3^{\otimes2})=0.
\tag{9}
\]

No se ejecutó `N=7`: la canonización actual prueba todas las reetiquetaciones
y cuesta `O((N!)^2)`. En el entorno activo no está disponible un backend de
canonización de grafos (`nauty`, `pynauty`, `igraph` o `networkx`). Un cuarto
tamaño exige primero sustituir esa canonización, no simplemente retirar el
límite de seguridad `N<=6`.

## Corrección del control `N=4`

Los valores `12/25`, `1739/3825` y `6901763/15357825` calculados previamente
comparaban el poset con la Gram del score continuo completo de §15, no con
`I_N^Pi`. No son valores de la retención definida en (5.3a). El backend nuevo
reproduce las 16 clases de posets a `N=4` y hace esta diferencia de
denominadores explícita.
