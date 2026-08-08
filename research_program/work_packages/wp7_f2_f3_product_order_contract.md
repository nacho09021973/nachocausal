# WP7 — Contrato `F2 => F3` o contraejemplo en `d=2`

```text
ESTADO: CONTRATO FORMAL v1.0 / PREGUNTA ABIERTA / CANDIDATO PLANTED_CHAIN NO PROBADO
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

La versión `d=2` de F2 usada en este contrato es

\[
\tag{F2-2D}
\sup_{R\in\mathcal R_n}
\frac{|N_n(R)-n|R||}{\sqrt{n|R|\log n}}\le K.
\]

Es deliberadamente más fuerte que pedirla solo en los diamantes interiores de Madsen:
un contraejemplo aquí seguirá siéndolo para cualquier subfamilia que contenga el diamante
testigo, una vez cerrado el puente geométrico `P5` de §3.

Ordenando por `u`, los rangos de `v` forman una permutación `pi_n`; la altura de
`P_n cap R` es la LIS de la subpermutación restringida a `R`. Para `x prec y` en `P_n`,
escribimos `R(x,y)=[u_x,u_y] x [v_x,v_y]` y `H_n(x,y)` para la longitud de la cadena
más larga entre ambos, incluidos los extremos. En la convención plana `ds^2=du dv`, el
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

## 3. Primer ataque obligatorio: cadena plantada

Antes de intentar un teorema general se audita la siguiente construcción. Tome
`m_n=ceil(c sqrt(n))` con `c>2`, un fondo de `n-m_n` puntos aproximadamente uniforme y
`m_n` puntos equiespaciados sobre un segmento de la diagonal `u=v`, más dos centinelas
si hacen falta para que el rectángulo testigo sea `R(x_n,y_n)`.

Para la diagonal y todo `R=I x J`, la obligación elemental es

\[
\tag{P2}
|C_{m_n}\cap R|\le m_n|I\cap J|+2
\le m_n\sqrt{|R|}+2.
\]

Por tanto, si el fondo satisface una cota VC relativa con constante `K_0`, la cuenta total
debería obedecer

\[
|N_n(R)-n|R||
\le K_0\sqrt{n|R|\log n}+2m_n\sqrt{|R|}+O(1),
\]

y el segundo término es `o(sqrt(n|R| log n))` uniformemente. A la vez, la cadena plantada
da `H_n(x_n,y_n)>=m_n`; en el rectángulo unidad esto fuerza
`H_n/(2 sqrt(n))>=c/2>1`.

La construcción **no es todavía un resultado**. Deben cerrarse, por escrito, estas cinco
obligaciones:

| ID | Obligación de prueba | Falla que bloquearía la construcción |
|---|---|---|
| P1 | existencia determinista de fondos con la cota relativa, uniforme para `|R|>=a_n` | el término VC excede la tolerancia F2 en la escala mínima |
| P2 | cota de intersección anterior para toda forma/aspect ratio admisible | un rectángulo fino captura demasiada cadena |
| P3 | combinación con cardinalidad total exactamente `n`, posición general y un `K` fijo | el sesgo de mezclar fondo y cadena no se absorbe uniformemente |
| P4 | par causal testigo con error relativo `>=delta` fijo | la normalización o los extremos eliminan la separación |
| P5 | transferencia fiel a los cuantificadores geométricos de F1--F2 de Madsen | borde, densidad, volumen, rango mesoscópico o convención métrica no coinciden |

Si P1--P5 se prueban, el trabajo termina con un contraejemplo fuerte; no se abre una
simulación confirmatoria. Si P1--P4 se prueban y P5 falla, el resultado queda limitado a
`PRODUCT_ORDER_DISCREPANCY_COUNTEREXAMPLE`, no a la pregunta de Madsen.

## 4. Ruta de teorema, solo si el falsador falla

La ruta positiva intentará acotar toda cadena por una partición multiescala de rectángulos
y construir una cadena inferior mediante ocupación de celdas. Debe producir una desigualdad
determinista de la forma

\[
|H_n(x,y)-2\sqrt{n|R(x,y)|}|
\le \varepsilon_n(A,K)\sqrt{n|R(x,y)|},
\qquad \varepsilon_n\to0.
\]

No basta probarla en probabilidad para puntos iid: eso reobtendría F3 para sprinklings,
pero no `F2 => F3`. Tampoco basta que `pi_n` converja al permutón uniforme: la LIS vive en
escala `sqrt(n)` y no es un funcional continuo de las densidades de patrones fijos.

## 5. Literatura mínima y función de cada fuente

| Fuente | Aporte permitido | Lo que no licencia |
|---|---|---|
| [N. Madsen, *On the Uniqueness of Embeddings of Causal Sets*](https://arxiv.org/abs/2607.05840), arXiv:2607.05840v1 (2026), Def. 2.6 y nota 1 | fija F1, F2, F3 y declara abierta su dependencia lógica | no prueba F2=>F3; su resultado usa F3 por separado |
| [B. Bollobás y G. Brightwell, *The height of a random partial order: concentration of measure*](https://doi.org/10.1214/aoap/1177005586), AAP 2 (1992), 1009--1018 | concentración de altura en el modelo aleatorio de orden coordenado | no es una desigualdad determinista desde discrepancia |
| [J. Baik, P. Deift y K. Johansson, *On the Distribution of the Length of the Longest Increasing Subsequence of Random Permutations*](https://arxiv.org/abs/math/9810105), JAMS 12 (1999), 1119--1178 | normalización `2 sqrt(n)` y fluctuaciones de LIS uniforme | no controla permutaciones adversariales con F2 |
| [J. N. Cooper, *Quasirandom Permutations*](https://arxiv.org/abs/math/0211001), JCTA 106 (2004), 123--143 | vocabulario de discrepancia de intervalos/rectángulos y cuasialeatoriedad | `o(n)` y patrones fijos no controlan por sí solos la constante de LIS |

Anclas locales: `docs/bibliography_claims.md` §2.5bis; `biblioteca/2607.05840v1.pdf`;
`emergencia/P1a_contrato_gate_altura_duracion_lex_d2.md` §§2, 5--6. Toda afirmación de
prioridad queda prohibida hasta una auditoría independiente de literatura.

## 6. Entregables y criterios de parada

Orden obligatorio, sin código ni datos:

1. nota de prueba P1--P4, con cada constante y término de borde;
2. nota de transferencia P5 contra la Def. 2.6 exacta de Madsen;
3. si el falsador falla, una sola nota que identifique la desigualdad positiva que falta;
4. ledger bibliográfico de discrepancia local, permutaciones cuasialeatorias y LIS.

Terminales, en orden de precedencia:

```text
COUNTEREXAMPLE_F1_F2_NOT_F3_D2        P1--P5 probadas
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

Hasta cerrar uno de los terminales anteriores, solo se permite afirmar:

> La dependencia `F2 => F3` está explícitamente abierta en Madsen; en `1+1`, se reduce a
> preguntar si una cota local de discrepancia rectangular controla la LIS a escala
> `sqrt(n)`. Una cadena plantada de tamaño `Theta(sqrt(n))` es un candidato concreto a
> separar ambas propiedades, pendiente de las obligaciones P1--P5.

No se afirma todavía contraejemplo, teorema, novedad, extensión a `d>=3`, unicidad de
embedding ni conclusión física sobre reconstrucción métrica general.
