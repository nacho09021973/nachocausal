# EF-8 — preflight de visibilidad macroscópica de rivales bajo Mallows

```text
ESTADO: COMPLETE_DEDUCTIVE_PREFLIGHT
FECHA: 2026-08-13
TERMINAL: PASS_MACROSCOPIC_STRONG_RIVAL_ONLY
EF8_STATUS: NOT_OPENED
MODELO: fixed-n, d=2
CODIGO NUEVO O MODIFICADO: NINGUNO
ENUMERACION_O_SIMULACION: NINGUNA
```

## 1. Pregunta

Para \(n=2s\), sea \(F_n\) la prescripción par de EF-4, sea

\[
 q_\star=((1,1),(s,s),(s+1,s+1),(n,n))
\tag{1.1}
\]

y sea

\[
 A_n(\delta)=\{t_{21}(L_n)\le\delta\},
 \qquad 0<\delta<\frac12.
\tag{1.2}
\]

La pregunta es si la existencia de una cuádrupla que empate o supere a
\(q_\star\) obliga a que \(L_n\) se separe macroscópicamente del permutón
condicionado de Mallows \(\nu_{\theta(\delta)}\).

El preflight separa dos respuestas:

1. un rival con ventaja de orden \(n\) sí fuerza una desviación macroscópica y
   tiene probabilidad condicionada exponencialmente pequeña;
2. un empate exacto, una ventaja entera o una diferencia \(o(n)\) no queda
   decidida por esa geometría. No se ha construido la pareja asintótica exacta
   `UNIQUE/TIE` exigida para declarar no-medibilidad del evento de rivalidad.

Por ello el terminal es parcial y no cierra el puente de unicidad.

## 2. Estado heredado

Se preserva íntegramente:

```text
PREVIOUS_TERMINAL = BLOCKED_BY_GLOBAL_RIVAL_CONTROL
EF8_STATUS = NOT_OPENED
```

El preflight anterior demostró, para cada \(\delta\in(0,1/2)\) fijo,

\[
 -\log\Pr(F_n\mid A_n(\delta))=o(n),
\tag{2.1}
\]

y, equivalentemente,

\[
 -\log\Pr(F_n\cap A_n(\delta))
 =-\log\Pr(A_n(\delta))+o(n).
\tag{2.2}
\]

También demostró que el evento uniforme \(G_n\) de EF-4 no puede reutilizarse:

\[
 F_n\cap G_n\cap A_n(\delta)=\varnothing
\tag{2.3}
\]

para todo \(n\) par suficientemente grande. Este documento no vuelve a intentar
transportar \(G_n\).

## 3. Definición formal de \(R_n\)

Para una cuádrupla admisible \(q=(a,b,c,d)\), escríbase

\[
 M_-(q)=|[a,b]|,
 \qquad
 M_+(q)=|[c,d]|,
\tag{3.1}
\]

y

\[
 S_{\rm lex}(q)
 =\bigl(m(q),c(q)\bigr)
 :=\left(
   \min\{M_-(q),M_+(q)\},
   M_-(q)+M_+(q)
 \right),
\tag{3.2}
\]

ordenado lexicográficamente. Sobre \(F_n\), la conservación de flujo entre las
dos mitades da

\[
 M_-(q_\star)=M_+(q_\star)=:M_n^\star,
 \qquad
 S_{\rm lex}(q_\star)=(M_n^\star,2M_n^\star)
\tag{3.3}
\]

para toda completación, no solo en promedio.

El evento de rivalidad exacta es

\[
 R_n=\left\{
 \exists q\ne q_\star:
 S_{\rm lex}(q)\ge_{\rm lex}S_{\rm lex}(q_\star)
 \right\}.
\tag{3.4}
\]

Por (3.2)--(3.3), ocurre si y solo si existe \(q\ne q_\star\) tal que

\[
 m(q)>M_n^\star,
\tag{3.5}
\]

o bien

\[
 m(q)=M_n^\star,
 \qquad c(q)\ge2M_n^\star.
\tag{3.6}
\]

La igualdad en (3.6) incluye tanto un empate exacto de ambos componentes como un
rival que gana por cobertura después de empatar el mínimo.

## 4. Geometría necesaria de un rival

### 4.1 Dominación por rectángulos de esquina

Normalícense los rangos por \(n\). Si los endpoints interiores de una candidata
son

\[
 b=(x_b,y_b),
 \qquad c=(x_c,y_c),
 \qquad x_b<x_c,\quad y_b<y_c,
\tag{4.1}
\]

elíjanse \(x\in[x_b,x_c]\) e \(y\in[y_b,y_c]\). Entonces

\[
 [a,b]\subseteq[0,x]\times[0,y],
 \qquad
 [c,d]\subseteq[x,1]\times[y,1].
\tag{4.2}
\]

Para un permutón \(\mu\), defínanse

\[
 C_\mu(x,y)=\mu([0,x]\times[0,y]),
\tag{4.3}
\]

\[
 U_\mu(x,y)
 =\mu([x,1]\times[y,1])
 =1-x-y+C_\mu(x,y),
\tag{4.4}
\]

y

\[
 H_\mu(x,y)=\min\{C_\mu(x,y),U_\mu(x,y)\}.
\tag{4.5}
\]

La segunda igualdad de (4.4) usa los márgenes uniformes del permutón. La
inclusión (4.2) implica que el score primario normalizado de cualquier candidata
está dominado, salvo el error de discretización \(O(1/n)\), por

\[
 V(\mu):=\max_{(x,y)\in[0,1]^2}H_\mu(x,y).
\tag{4.6}
\]

Para \(q_\star\), los dos intervalos son precisamente los cuadrados de esquina
separados en \((1/2,1/2)\), de modo que

\[
 \frac{M_n^\star}{n}
 =H_{L_n}(1/2,1/2)+o(1).
\tag{4.7}
\]

### 4.2 Qué parte de EF-4 dejó de ser compatible

La tricotomía de rivales de EF-4 y la igualdad (3.3) son combinatorias. Lo que
dejó de estar disponible fue la sustitución simultánea

\[
 \frac{X(I,J)}N=uv+o(1)
\tag{4.8}
\]

para todos los rectángulos residuales. Bajo \(A_n(\delta)\), el término correcto
de primer orden es la masa del permutón de Mallows, no el área \(uv\). El evento
que imponía (4.8) centra el bulk en \(\lambda\) y contradice \(\delta<1/2\).

## 5. Análisis de visibilidad por permutones

### 5.1 El funcional de esquina es continuo

Los permutones tienen márgenes atomless. Por ello, la convergencia débil de
permutones implica convergencia uniforme de sus funciones de distribución
\(C_\mu\). En particular,

\[
 \mu\longmapsto H_\mu,
 \qquad
 \mu\longmapsto V(\mu)
\tag{5.1}
\]

son continuas para la topología usual de permutones.

Esto conserva:

- masas de rectángulos de tamaño macroscópico;
- la mejor ventaja de orden \(n\) entre pares de rectángulos;
- separaciones positivas entre cortes macroscópicamente distintos.

No conserva:

- que los bordes de un rectángulo sean puntos concretos de la permutación;
- los \(R_n=o(n)\) puntos prescritos de las escaleras;
- diferencias enteras o \(o(n)\) entre cardinalidades;
- la igualdad exacta de los dos componentes de un score lexicográfico;
- el número de cuádruplas discretas que realizan un mismo valor límite.

Estas últimas son exactamente las piezas que pueden decidir `UNIQUE/TIE`.

### 5.2 Máximo estricto para el permutón de Mallows

La ecuación (5.3) de Borga--Das--Mukherjee--Winkler da la densidad explícita del
permutón estándar de Mallows. Para el lower tail, póngase

\[
 \alpha=-\theta(\delta)>0.
\tag{5.2}
\]

La integración de esa densidad da el copulón de Frank

\[
 C_\alpha(x,y)
 =-\frac1\alpha
 \log\left[
  1+
  \frac{(e^{-\alpha x}-1)(e^{-\alpha y}-1)}{e^{-\alpha}-1}
 \right].
\tag{5.3}
\]

No se atribuye al artículo el análisis de `MIN_COVERAGE_LEX`; (5.3) se usa solo
para resolver el problema elemental de masas de esquina.

Si \(x+y\le1\), entonces \(U_\alpha(x,y)\ge C_\alpha(x,y)\) y

\[
 H_\alpha(x,y)=C_\alpha(x,y).
\tag{5.4}
\]

Como \(C_\alpha\) es estrictamente creciente en cada coordenada, el máximo en
ese semicuadrado está sobre \(x+y=1\). Si \(x+y\ge1\), la simetría por rotación
de \(180\) grados reduce el problema al mismo borde.

Escríbase \(z=e^{-\alpha x}\) y \(k=e^{-\alpha}\). Sobre \(y=1-x\), el
argumento del logaritmo en (5.3) es

\[
 \frac{z+k/z-2k}{1-k}.
\tag{5.5}
\]

La desigualdad aritmético--geométrica da

\[
 z+\frac{k}{z}\ge2\sqrt{k},
\tag{5.6}
\]

con igualdad única en \(z=\sqrt{k}\), es decir, \(x=y=1/2\). Como el signo en
(5.3) es negativo,

\[
 \boxed{
 V(\nu_{\theta(\delta)})
 =H_{\nu_{\theta(\delta)}}(1/2,1/2)
 }
\tag{5.7}
\]

y el maximizador es único para cada \(\delta\in(0,1/2)\).

Por compacidad, para cada \(\varepsilon>0\) existe
\(g_{\delta}(\varepsilon)>0\) tal que

\[
 \|(x,y)-(1/2,1/2)\|\ge\varepsilon
 \quad\Longrightarrow\quad
 H_{\nu_{\theta(\delta)}}(x,y)
 \le H_{\nu_{\theta(\delta)}}(1/2,1/2)
      -g_\delta(\varepsilon).
\tag{5.8}
\]

Ésta es la separación macroscópica que no estaba disponible en el preflight
anterior.

## 6. Intento de falsificador

### 6.1 Candidato cercano invisible a escala de permutón

La banda prescrita ocupa las filas
\(s-\rho_n+1,\ldots,s+\rho_n\). Las filas \(s-\rho_n\) y
\(s+\rho_n+1\), y las columnas del mismo nombre, son libres para todo \(n\)
grande. Por tanto, \(F_n\) es compatible con prescribir adicionalmente

\[
 b_n'=(s-\rho_n,s-\rho_n),
 \qquad
 c_n'=(s+\rho_n+1,s+\rho_n+1),
\tag{6.1}
\]

y con la candidata

\[
 q_n'=((1,1),b_n',c_n',(n,n)).
\tag{6.2}
\]

Añadir esas dos asignaciones a \(F_n\) conserva (2.1): el mismo sandwich de
inversiones del preflight anterior solo reemplaza el número de asignaciones
\(2\rho_n+2\) por \(2\rho_n+4\), y el coste factorial adicional es
\(O(\log n)=o(n)\). También conserva el límite
\(\nu_{\theta(\delta)}\). Como los dos cuadrados de (6.2) tienen masa positiva,
\(q_n'\) es admisible en toda sucesión de esas completaciones que converja al
macroestado.

Sus dos cuadrados de esquina tienen cortes a distancia
\(\rho_n/n=o(1)\) del corte central. Como la densidad de Mallows es continua y
positiva para \(\delta\in(0,1/2)\),

\[
 H_{\nu_{\theta(\delta)}}(1/2,1/2)
 -\min\left\{
   \nu_{\theta(\delta)}([0,1/2-\rho_n/n]^2),
   \nu_{\theta(\delta)}([1/2+\rho_n/n,1]^2)
 \right\}
 =O(\rho_n/n).
\tag{6.3}
\]

Así, su déficit esperado de cardinalidad es solo

\[
 O(\rho_n)=o(n).
\tag{6.4}
\]

Este cálculo localiza una familia explícita de **casi rivales** que el permutón
límite no separa de \(q_\star\) por una constante. Alterar \(o(n)\) puntos puede
cambiar un déficit de esa escala sin cambiar el límite de permutón.

### 6.2 Por qué esto no es todavía el falsificador exigido

Para declarar

```text
RIVAL_EVENT_NOT_PERMUTON_MEASURABLE
```

haría falta construir dos completaciones explícitas de \(F_n\), ambas con
límite \(\nu_{\theta(\delta)}\) y compatibles con el lower tail, tales que
\(q_\star\) fuese ganador único en una y (6.2), u otra cuádrupla, empatase o
ganase en la otra. Además habría que controlar simultáneamente todas las demás
cuádruplas.

(6.1)--(6.4) solo muestran que el coste de ajustar el score de una candidata
cercana es subextensivo. No prueban que una modificación concreta produzca el
empate exacto sin crear un tercer rival, ni construyen la completación `UNIQUE`
de partida. Por tanto, el falsificador exacto no queda demostrado y ese terminal
no se usa.

## 7. Análisis variacional y LDP

### 7.1 Dos eventos macroscópicos de rival fuerte

Fíjese \(\eta>0\). Sepárense:

\[
 R_{n,\eta}^{(1)}
 =\left\{
   \exists q\ne q_\star:
   m(q)\ge M_n^\star+\eta n
  \right\},
\tag{7.1}
\]

y

\[
 R_{n,\eta}^{(2)}
 =\left\{
   \exists q\ne q_\star:
   m(q)\ge M_n^\star,\quad
   c(q)\ge2M_n^\star+\eta n
  \right\}.
\tag{7.2}
\]

El primero da una ventaja macroscópica en el componente primario. El segundo
permite empate primario pero exige una ventaja macroscópica en el secundario.

Por (4.2), (7.1) implica, con un error \(o(1)\),

\[
 V(L_n)
 \ge H_{L_n}(1/2,1/2)+\eta.
\tag{7.3}
\]

Para (7.2), existen \((x,y)\) tales que, salvo \(o(1)\),

\[
 H_{L_n}(x,y)\ge H_{L_n}(1/2,1/2),
\tag{7.4}
\]

y

\[
 C_{L_n}(x,y)+U_{L_n}(x,y)
 \ge2H_{L_n}(1/2,1/2)+\eta.
\tag{7.5}
\]

Para el primer evento defínase el conjunto cerrado

\[
 \mathcal B_{\eta}^{(1)}
 =\left\{\mu:
   V(\mu)\ge H_\mu(1/2,1/2)+\eta/2
  \right\}.
\tag{7.6}
\]

Para el segundo hace falta conservar el error finito de (7.4). La unicidad de
(5.7), la continuidad y la compacidad de \([0,1]^2\) implican que, para cada
\(\eta>0\), existe \(\gamma_{\delta,\eta}>0\) tal que
\(\nu_{\theta(\delta)}\) no satisface simultáneamente

\[
 H_\mu(x,y)\ge H_\mu(1/2,1/2)-\gamma_{\delta,\eta}
\tag{7.7}
\]

y

\[
 C_\mu(x,y)+U_\mu(x,y)
 \ge2H_\mu(1/2,1/2)+\eta/2.
\tag{7.8}
\]

Sea \(\mathcal B_{\delta,\eta}^{(2)}\) el conjunto de permutones para los que
existe un corte que satisface (7.7)--(7.8). Es cerrado: se extrae una
subsucesión convergente de los cortes testigo. Para \(n\) grande, (7.3) incluye
\(R_{n,\eta}^{(1)}\) en \(\mathcal B_{\eta}^{(1)}\), y (7.4)--(7.5) incluyen
\(R_{n,\eta}^{(2)}\) en \(\mathcal B_{\delta,\eta}^{(2)}\).

Por construcción y por (5.7), \(\nu_{\theta(\delta)}\) no pertenece a ninguno
de esos conjuntos. En el segundo caso, al hacer
\(\gamma_{\delta,\eta}\downarrow0\), todo corte casi maximizador converge a
\((1/2,1/2)\), donde las dos masas valen lo mismo y su suma es exactamente el
doble del mínimo.

### 7.2 Gap variacional positivo

Sea

\[
 J(\delta)
 =\inf_{\mu:\,t_{21}(\mu)\le\delta}
 D(\mu\Vert\lambda)
 =D(\nu_{\theta(\delta)}\Vert\lambda).
\tag{7.9}
\]

El Corolario 1.7 de Borga--Das--Mukherjee--Winkler da el LDP uniforme. El
Teorema 1.20, Remark 1.21 y la unicidad estándar de Mallows identifican el único
minimizador lower-tail. Como \(D(\cdot\Vert\lambda)\) es una tasa buena y los
conjuntos \(\mathcal B_{\eta}^{(1)}\) y
\(\mathcal B_{\delta,\eta}^{(2)}\) son cerrados y no contienen al único
minimizador,

\[
 c_{\delta,\eta}^{(i)}
 :=
 \inf_{\substack{
      \mu\in\mathcal B_{\delta,\eta}^{(i)}\\
      t_{21}(\mu)\le\delta}}
 D(\mu\Vert\lambda)-J(\delta)
 >0,
 \qquad i=1,2.
\tag{7.10}
\]

Aquí se usa la abreviatura
\(\mathcal B_{\delta,\eta}^{(1)}:=\mathcal B_{\eta}^{(1)}\). El resultado
heredado (2.2) da el denominador correcto, mientras que en el
numerador puede olvidarse \(F_n\):

\[
 \Pr(\mathcal B,F_n,A_n(\delta))
 \le\Pr(\mathcal B,A_n(\delta)).
\tag{7.11}
\]

La cota superior del LDP, (2.2) y (7.10) producen

\[
 \Pr\left(
   R_{n,\eta}^{(i)}
   \mid F_n,A_n(\delta)
 \right)
 \le
 \exp[-n c_{\delta,\eta}^{(i)}+o(n)],
 \qquad i=1,2.
\tag{7.12}
\]

En particular, para todo \(\eta>0\),

\[
 \Pr\left(
   R_{n,\eta}^{(1)}\cup R_{n,\eta}^{(2)}
   \mid F_n,A_n(\delta)
 \right)\longrightarrow0.
\tag{7.13}
\]

Esto es una supresión macroscópica genuina y vale para todo
\(\delta\in(0,1/2)\) fijo. No usa equivalencia entre el ensemble duro y la
medida canónica de Mallows.

## 8. Rival macroscópico frente a empate microscópico

La clasificación relevante es:

| Tipo de rival | Diferencia de score | Visibilidad por permutón | Resultado |
|---|---:|---|---|
| Ventaja primaria fuerte | \(\ge\eta n\) | Sí | Supresión exponencial por (7.12) |
| Empate primario y ventaja secundaria fuerte | \(\ge\eta n\) en cobertura | Sí | Supresión exponencial por (7.12) |
| Ventaja primaria subextensiva | \(o(n)\) | No decidida | Fuera de la resolución LDP |
| Empate exacto | \(0\) | No decidida | Fuera de la resolución LDP |
| Ventaja secundaria subextensiva tras empate | \(o(n)\) | No decidida | Fuera de la resolución LDP |

Al poner \(\eta=0\), los conjuntos macroscópicos usados arriba contienen al
propio estado típico: (5.7) es una igualdad. En consecuencia, el gap
variacional de (7.10) colapsa a cero. El LDP de velocidad \(n\) no puede decidir
si la diferencia entera es \(-1\), \(0\) o \(+1\), ni si dos cuádruplas
distintas realizan el mismo score.

La obligación microscópica que permanece es demostrar, mediante control
mesoscópico de conteos bajo el ensemble duro, una de las dos alternativas:

\[
 \Pr(R_n\mid F_n,A_n(\delta))\longrightarrow0,
\tag{8.1}
\]

o construir la pareja asintótica exacta descrita en §6.2. El primer objeto no
puede sustituirse por la sola convergencia de \(L_n\) a
\(\nu_{\theta(\delta)}\).

## 9. Terminal

```text
MALLOWS_CORNER_MASS_MAXIMIZER = UNIQUE_AT_HALF_CUT
MACROSCOPIC_PRIMARY_RIVAL = EXPONENTIALLY_SUPPRESSED
MACROSCOPIC_SECONDARY_RIVAL_AFTER_PRIMARY_TIE = EXPONENTIALLY_SUPPRESSED
EXACT_TIE_OR_o(n)_RIVAL = NOT_DECIDED
ASYMPTOTIC_UNIQUE_TIE_FALSIFIER = NOT_CONSTRUCTED
MALLOWS_TO_MIN_COVERAGE_LEX_BRIDGE = NOT_CLOSED

PREFLIGHT_TERMINAL = PASS_MACROSCOPIC_STRONG_RIVAL_ONLY
EF8_STATUS = NOT_OPENED
```

No procede `PASS_MACROSCOPIC_RIVAL_SUPPRESSION`, porque (7.12) requiere
\(\eta>0\). Tampoco procede `RIVAL_EVENT_NOT_PERMUTON_MEASURABLE`, porque
§6 no construye las dos sucesiones exactas exigidas. El contenido positivo es
precisamente el terminal parcial permitido: los rivales fuertes son visibles y
raros; los empates y rivales cercanos permanecen abiertos.

## 10. Consecuencia exacta para el puente Mallows → `MIN_COVERAGE_LEX`

El bloqueo heredado se reduce de “rivales globales arbitrarios” a una obligación
mesoscópica:

> controlar cuádruplas cuyos cortes convergen a \((1/2,1/2)\) y cuyo score
> difiere del plantado en \(o(n)\), incluyendo la igualdad exacta de ambos
> componentes lexicográficos.

Una eventual prueba del puente ya no necesita excluir desviaciones
macroscópicas: eso queda cubierto por (7.12). Necesita una concentración uniforme
de incrementos de masas entre rectángulos cercanos, a una escala al menos tan
fina como la banda \(\rho_n\), y después un argumento anti-empate para scores
enteros. Borga--Das--Mukherjee--Winkler no proporcionan ese control
microscópico y aquí no se les atribuye.

EF-8 sigue sin abrirse.

## Referencias auditadas

- `dev/EF8_RATE_COMPETITION_PREFLIGHT.md`.
- `dev/EF8_PERMUTON_MACRO_EVENT_PREFLIGHT.md`.
- `dev/EF8_MALLOWS_UNIQUENESS_BRIDGE_PREFLIGHT.md`.
- `emergencia/P1a_estabilidad_seleccion_subexponencial_d2.md`.
- `docs/hoja_de_ruta_agosto_2026.md`, EF-3 y EF-4.
- `emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md`.
- J. Borga, S. Das, S. Mukherjee y P. Winkler,
  *Large deviation principle for random permutations*,
  https://arxiv.org/abs/2206.04660; Corollary 1.7, Theorem 1.20,
  Remark 1.21, Theorem 1.29(ii) y ecuación (5.3).
