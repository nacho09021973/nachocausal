# P1a — Puerta teórica del selector de cobertura en Minkowski

> **ESTADO: ANÁLISIS TEÓRICO v0.1 · SIN SIMULACIÓN · PUERTA PARA ENUMERACIÓN
> EXACTA.**
>
> Esta nota estudia las probabilidades de candidato vacío, empate y selección única
> para `F_cov,3`, antes de autorizar una ejecución. Cierra analíticamente el evento
> vacío, reduce exactamente los empates a tres fuentes combinatorias y decide que el
> selector merece únicamente una enumeración exacta inicial en `1+1` dimensiones.
> No autoriza Monte Carlo, dimensiones superiores ni inferencia métrica.

## 0. Pregunta de la puerta

Para el selector congelado en
`emergencia/P1a_primer_selector_de_cobertura.md`, queremos estudiar

```text
p_empty(n,d) = P(Q_3(C_n)=vacio | N=n,d),
p_def(n,d)   = P(|M_cov(C_n)|=1 | N=n,d),
p_tie(n,d)   = P(|M_cov(C_n)|>1 | N=n,d).
```

La familia generativa es la de `T0_modelo_minimo_y_proposicion_cero.md`: `n` puntos
iid según volumen normalizado en un diamante causal de Minkowski de dimensión `d`
conocida. Se observan únicamente orden y cardinalidad.

Por construcción,

```text
p_empty(n,d) + p_def(n,d) + p_tie(n,d) = 1.
```

## 1. La escala temporal no interviene

Condicionado a `N=n`, una dilatación del diamante preserva todas las
comparabilidades y transporta la medida de volumen normalizada. Por la proposición
cero,

```text
Law(C_n | N=n,d,tau) = Q_(n,d)
```

no depende de `tau`. En consecuencia, las tres probabilidades de esta nota son
funciones de `(n,d)`, no de la duración absoluta del diamante.

Esto no es un defecto del selector: cualquier estadístico order-only condicionado a
`N=n` comparte la misma ceguera de escala. Tampoco demuestra nada sobre una futura
razón temporal adimensional.

## 2. Proposición P1a-M.1 — caracterización exacta del vacío

Sea

```text
H(C) = max{|K| : K es una cadena de C}
```

la altura de `C`, contando elementos. Entonces

```text
Q_3(C) != vacio  si y solo si  H(C) >= 6.
```

Por tanto,

```text
p_empty(n,d) = P(H(C_n) <= 5 | N=n,d).
```

### Demostración

Si `(a,b,c,d) in Q_3(C)`, la condición `|[a,b]|>=3` proporciona un elemento
`x` con `a prec x prec b`; de igual modo existe `y` con `c prec y prec d`. Luego

```text
a prec x prec b prec c prec y prec d
```

es una cadena de seis elementos.

Recíprocamente, dada una cadena

```text
z_1 prec z_2 prec z_3 prec z_4 prec z_5 prec z_6,
```

la cuádrupla `(z_1,z_3,z_4,z_6)` pertenece a `Q_3(C)`. `QED`

Esta equivalencia elimina la necesidad de estudiar `p_empty` mediante el algoritmo
completo del selector.

## 3. Cota elemental en toda dimensión fija

Sea

```text
r_(6,d) = P(seis puntos iid del diamante forman una cadena total).
```

Para cada `d` finita, `r_(6,d)>0`: existe una región abierta de configuraciones
estrictamente ordenadas con volumen positivo.

Dividamos los `n` puntos iid en `floor(n/6)` bloques disjuntos de seis. Los eventos
“el bloque forma una cadena” son independientes. Si alguno ocurre, el poset completo
tiene altura al menos seis. Por tanto,

```text
p_empty(n,d)
  <= (1-r_(6,d))^floor(n/6).
```

En particular,

```text
lim_(n->infinito) p_empty(n,d) = 0
```

para toda dimensión fija. La cota no pretende ser óptima; basta para demostrar que
la ausencia de candidatos no es una obstrucción asintótica del selector.

## 4. Reducción exacta en `1+1` dimensiones

### 4.1 Del diamante al orden producto

En coordenadas de cono de luz

```text
u = t+x,
v = t-x,
```

un diamante causal bidimensional se transforma, salvo reescala, en un rectángulo y
la causalidad se convierte en el orden producto:

```text
(u_i,v_i) prec (u_j,v_j)
  si y solo si
u_i < u_j y v_i < v_j.
```

Como las coordenadas son continuas, no hay empates con probabilidad uno. Ordenando
los puntos por `u`, los rangos de sus coordenadas `v` forman una permutación uniforme

```text
pi in S_n.
```

Las cadenas del causal set son exactamente las subsecuencias crecientes de `pi`. Por
ello,

```text
H(C_n) = LIS(pi)
```

y

```text
p_empty(n,2) = P(LIS(pi) <= 5).
```

### 4.2 Fórmula exacta por RSK

La correspondencia Robinson–Schensted asocia a cada permutación una partición
`lambda` de `n`; la longitud de la primera fila `lambda_1` es la longitud de la
subsecuencia creciente más larga. Si `f^lambda` es el número de tableaux estándar de
forma `lambda`, entonces

```text
p_empty(n,2)
  = (1/n!) sum_(lambda partition n, lambda_1<=5) (f^lambda)^2,

f^lambda = n! / product_(c in lambda) h(c),
```

donde `h(c)` es la longitud de gancho de la celda `c`.

La fórmula es finita y exacta. No requiere sprinklings ni Monte Carlo.

### 4.3 Casos iniciales exactos

```text
n <= 5:
  p_empty(n,2)=1,
  p_def(n,2)=0,
  p_tie(n,2)=0.
```

Para `n=6`, un candidato solo puede existir si los seis elementos forman una cadena
total. En la representación por permutaciones esto ocurre únicamente para la
permutación creciente. La cuádrupla seleccionada es única. Por tanto,

```text
p_empty(6,2) = 719/720,
p_def(6,2)   =   1/720,
p_tie(6,2)   =   0.
```

Como comprobación adicional de la fórmula RSK, para `n=7` las únicas formas con
`lambda_1>=6` son `(7)` y `(6,1)`, con dimensiones `1` y `6`. Así,

```text
p_empty(7,2) = 1 - (1^2+6^2)/7!
             = 5003/5040.
```

Esta igualdad no separa todavía selección única y empate entre las 37 permutaciones
no vacías.

### 4.4 Decaimiento del vacío

En `d=2`, la probabilidad de que seis puntos de un bloque formen una cadena es
`1/6!`. La cota de §3 se especializa a

```text
p_empty(n,2) <= (719/720)^floor(n/6).
```

La teoría de la subsecuencia creciente más larga proporciona resultados mucho más
finos: `LIS(pi)` se concentra alrededor de `2 sqrt(n)` y, tras el reescalado
adecuado, tiene el límite de Baik–Deift–Johansson. Para P1a solo necesitamos la
conclusión más débil, ya probada elementalmente, de que el umbral fijo seis se supera
con probabilidad tendente a uno.

## 5. Proposición P1a-M.2 — descomposición exacta de los empates

Para cada posible extremo derecho `b` del intervalo anterior, definimos

```text
A_3(b) = {a : a prec b y n_C(a,b)>=3},

ell_3(b) = max_{a in A_3(b)} n_C(a,b),
U_3(b)   = Argmax_{a in A_3(b)} n_C(a,b).
```

Si `A_3(b)` es vacío, `ell_3(b)` queda indefinido y `U_3(b)=vacio`.

Simétricamente, para cada posible extremo izquierdo `c` del intervalo posterior,

```text
D_3(c) = {d : c prec d y n_C(c,d)>=3},

r_3(c) = max_{d in D_3(c)} n_C(c,d),
V_3(c) = Argmax_{d in D_3(c)} n_C(c,d).
```

Definimos los puentes admisibles

```text
B_3(C) = {
  (b,c) : b prec c, U_3(b)!=vacio, V_3(c)!=vacio
}
```

y su score reducido

```text
T_C(b,c) = ell_3(b) + r_3(c).
```

Sea

```text
B_3^*(C) = Argmax_{(b,c) in B_3(C)} T_C(b,c),
```

con valor vacío cuando `B_3(C)` es vacío.

Entonces el conjunto completo de cuádruplas maximizadoras es exactamente

```text
M_cov(C) = {
  (a,b,c,d) :
  (b,c) in B_3^*(C),
  a in U_3(b),
  d in V_3(c)
}.
```

En particular,

```text
|M_cov(C)|
  = sum_((b,c) in B_3^*(C)) |U_3(b)| |V_3(c)|.
```

### Demostración

Fijados `b,c`, el score de cobertura se separa como

```text
n_C(a,b) + n_C(c,d).
```

Por ello se maximiza el primer sumando escogiendo `a in U_3(b)` y el segundo
escogiendo `d in V_3(c)`. Después solo queda maximizar la suma de los dos valores
óptimos sobre los puentes `b prec c`. Las cuádruplas correspondientes a puentes o
endpoints distintos son distintas, lo que da la fórmula de cardinalidad. `QED`

### Criterio de unicidad

`F_cov,3(C)` está definido si y solo si se cumplen simultáneamente:

1. existe un único puente maximizador `(b_*,c_*)`;
2. `|U_3(b_*)|=1`;
3. `|V_3(c_*)|=1`.

Los empates quedan así separados en tres mecanismos auditables:

```text
BRIDGE_TIE,
PAST_ENDPOINT_TIE,
FUTURE_ENDPOINT_TIE.
```

Esta reducción es exacta para cualquier poset finito y evita tratar la lista de
cuádruplas como una caja negra.

## 6. Probabilidades exactas como conteos de permutaciones

En `d=2`, sea `C(pi)` el poset producto inducido por `pi in S_n` y sea

```text
m(pi) = |M_cov(C(pi))|.
```

Entonces

```text
p_empty(n,2) = #{pi in S_n : m(pi)=0}/n!,
p_def(n,2)   = #{pi in S_n : m(pi)=1}/n!,
p_tie(n,2)   = #{pi in S_n : m(pi)>=2}/n!.
```

Estas identidades convierten el primer estudio computacional en enumeración exacta
de objetos finitos. No se necesita generar coordenadas continuas, elegir seeds ni
estimar errores Monte Carlo.

## 7. Ningún estado desaparece estructuralmente

### 7.1 Selección única tiene probabilidad positiva

Para todo `n>=6`, considérese la permutación

```text
pi_n = (n,n-1,...,7,1,2,3,4,5,6).
```

Los primeros `n-6` elementos forman una anticadena y son incomparables con la cadena
final de seis elementos. Esta cadena contiene la única cuádrupla admisible de
cobertura máxima. Por tanto,

```text
p_def(n,2) >= 1/n! > 0.
```

Esta cota solo prueba posibilidad; decrece demasiado rápido para demostrar utilidad.

### 7.2 Vacío tiene probabilidad positiva a tamaño finito

La permutación decreciente es una anticadena, luego

```text
p_empty(n,2) >= 1/n! > 0
```

para todo `n` finito.

### 7.3 Empate tiene probabilidad positiva desde `n=7`

La permutación creciente produce la cadena total `C_n`. Para `n>=7` posee
`n-5>=2` cortes de cobertura máxima. Así,

```text
p_tie(n,2) >= 1/n! > 0,   n>=7.
```

En consecuencia, para `n>=7` los tres terminales tienen probabilidad estrictamente
positiva. Ningún argumento puramente de existencia decide si `p_def` domina o
desaparece asintóticamente.

## 8. Canal Poisson

Si se conserva el conteo Poisson con

```text
lambda_tau = rho kappa_d tau^d,
```

las probabilidades no condicionadas son mezclas:

```text
P_s^(Pois)(tau)
  = sum_(n>=0) Poisson(lambda_tau){n} p_s(n,d),

s in {empty,def,tie}.
```

La dependencia respecto de `tau` entra únicamente a través de `N`. En particular,

```text
P_empty^(Pois)(tau) >= P(Poisson(lambda_tau)<=5).
```

Cuando `lambda_tau -> infinito`, la cota exponencial condicionada y la concentración
de `N` implican `P_empty^(Pois)(tau)->0`. Esto no informa por sí solo sobre selección
única frente a empate.

## 9. Qué queda resuelto y qué no

### Cerrado teóricamente

- `EMPTY` equivale exactamente a altura menor que seis.
- `p_empty(n,d)->0` para toda dimensión fija.
- en `d=2`, `p_empty` posee una fórmula RSK exacta;
- los empates se descomponen exactamente en puente, extremo pasado y extremo futuro;
- en `d=2`, las tres probabilidades son conteos uniformes sobre `S_n`;
- vacío, selección única y empate son todos posibles a tamaño finito.

### Abierto

- el comportamiento asintótico de `p_def(n,2)` y `p_tie(n,2)`;
- si la unicidad es frecuente en el rango finito de interés;
- cuál de los tres mecanismos domina los empates;
- estabilidad del par seleccionado bajo borrado o adición de elementos;
- concentración en el borde;
- y correspondencia de la salida con una razón de tiempos propios.

## 10. Decisión de la puerta

El selector supera el no-go estructural mínimo:

1. la ausencia de candidatos desaparece asintóticamente;
2. la selección única tiene probabilidad positiva para todo `n>=6`;
3. existe una representación exacta y libre de ruido Monte Carlo en `d=2`;
4. y los empates tienen una taxonomía computable.

Esto justifica diseñar una **enumeración exacta acotada de permutaciones en `d=2`**.
No justifica todavía sprinklings Monte Carlo, dimensiones superiores ni medición de
`R_L`.

```text
P1A_THEORY_GATE = PASS_TO_PREREGISTERED_EXACT_2D_ENUMERATION
P1A_EMPTY_EVENT = ANALYTICALLY_CLOSED
P1A_UNIQUENESS_VS_TIE = EXACT_FINITE_COUNT_OPEN
P1A_MONTE_CARLO = NOT_AUTHORIZED
P1A_HIGHER_DIMENSIONS = NOT_AUTHORIZED
P1A_METRIC_RATIO_EXECUTION = NOT_AUTHORIZED
```

La enumeración deberá contar, para cada `n` aprobado:

```text
EMPTY,
UNIQUE,
TIE_BRIDGE_ONLY,
TIE_PAST_ENDPOINT,
TIE_FUTURE_ENDPOINT,
TIE_MIXED,
```

y verificar exactamente que las frecuencias suman `n!`. El rango de `n`, la
implementación, los invariantes y los terminales deberán fijarse en un contrato de
ejecución separado.

La ejecución posterior se congeló y completó en:

```text
emergencia/P1a_contrato_enumeracion_y_monte_carlo_d2.md
emergencia/P1a_resultados_enumeracion_y_monte_carlo_d2.md
```

El cruce exacto–Monte Carlo pasó y el terminal operacional fue
`POINT_SELECTOR_OPERATIONALLY_VIABLE`. La conclusión se limita a disponibilidad del
selector en `d=2`; la razón métrica permanece fuera de alcance.

La evaluación posterior de estabilidad y sesgo se congeló y completó en:

```text
emergencia/P1a_contrato_estabilidad_y_sesgo_d2.md
emergencia/P1a_resultados_estabilidad_y_sesgo_d2.md
```

El selector reselecciona con alta frecuencia la misma cuádrupla tras thinning, pero
concentra el intervalo menor en `k_0=3`. El terminal compuesto fue
`INCONCLUSIVE_STABILITY_GATE`; no se abre por ello la ejecución métrica de `R_L`.

El rediseño comparativo posterior se documenta en:

```text
emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md
emergencia/P1a_resultados_comparacion_selectores_balanceados_d2.md
```

El terminal seleccionó `MIN_COVERAGE_LEX` para un gate posterior de sesgo de alturas.
Esta regla protege primero el soporte menor y usa cobertura solo como segundo
componente. No se ha ejecutado todavía `R_L`.

El gate posterior se congeló y completó en:

```text
emergencia/P1a_contrato_gate_altura_duracion_lex_d2.md
emergencia/P1a_resultados_gate_altura_duracion_lex_d2.md
```

El terminal fue `PARK_LEX_HEIGHT_REPRESENTATION`: la altura conserva calibración de
escala media, pero no resolución individual suficiente dentro de la banda de
duraciones inducida por el selector. `R_L` no fue calculado.

La comparación posterior de conteo y altura–anchura se documenta en:

```text
emergencia/P1a_contrato_representaciones_alternativas_d2.md
emergencia/P1a_resultados_representaciones_alternativas_d2.md
```

`HEIGHT_WIDTH` queda aparcada y `COUNT_VOLUME` permanece abierta sin cualificar. La
representación por conteo exige ahora una teoría explícita de condicionamiento por
selección y circularidad antes de considerar un cociente.

## 11. Fuentes y prioridad

La reducción del causal set bidimensional a una permutación uniforme y la conexión
altura–subsecuencia creciente pertenecen a maquinaria clásica. La distribución
asintótica de la subsecuencia creciente más larga es el resultado de
Baik–Deift–Johansson. Aghili, Bombelli y Pilgrim estudian distribuciones de longitudes
de paths en causal sets bidimensionales, una cuestión cercana pero distinta del
selector de cobertura.

Las proposiciones P1a-M.1 y P1a-M.2 son deducciones elementales del selector
congelado. No se ha realizado una auditoría de prioridad exhaustiva sobre esta
factorización concreta.

```text
P1A_MINKOWSKI_PRIORITY_STATUS = STANDARD_MACHINERY_PLUS_INTERNAL_REDUCTION
NOVELTY_CERTIFIED = NO
```

Referencias locales:

- `biblioteca/emergencia/math9810105v2_Baik_Deift_Johansson_Longest_Increasing_Subsequence.pdf`
- `biblioteca/emergencia/1805.07312v1_Aghili_Bombelli_Pilgrim_Path_Length_2D_Causal_Sets.pdf`
- `biblioteca/emergencia/1903.11544v2_Surya_Causal_Set_Approach_to_Quantum_Gravity.pdf`

Fuentes oficiales:

- <https://arxiv.org/abs/math/9810105>
- <https://arxiv.org/abs/1805.07312>
- <https://arxiv.org/abs/1903.11544>

## 12. Auditoría del certificado de unicidad por marco vacío

> **ESTADO DE ESTA SECCIÓN: BORRADOR ANALÍTICO · SIN EJECUCIÓN.** Cada lema y
> cada conclusión llevan una etiqueta `PROVED`, `SKETCH` u `OPEN`. La sección no
> modifica ningún gate congelado.

### 12.1 Gate semántico del selector

**Lema 12.1 (`PROVED`: dominio admisible).** El experimento seleccionado no permite
`b=c`. Su definición es

```text
Q_3(C) = {(a,b,c,d): a prec_C b prec_C c prec_C d,
          n_C(a,b)>=3, n_C(c,d)>=3}.
```

Esto consta en
`P1a_count_volume_experimento_condicionado_d2.md:47-57`. Por tanto, el óptimo
continuo de la clausura, que tiene `b=c=(1/2,1/2)`, debe realizarse en el poset por
dos puntos centrales distintos y comparables. En rangos de la permutación, la
separación discreta mínima es un incremento de uno en ambos rangos.

**Lema 12.2 (`PROVED`: significado de `S`).** En el experimento condicionado,

```text
S = {el argmax de S_lex sobre Q_3(C) es una única cuádrupla}.
```

No es unicidad del valor, no es unicidad módulo `(K,L)<->(L,K)` y no existe regla de
desempate: si dos cuádruplas maximizan, el selector queda `UNDEFINED`. Véanse
`P1a_count_volume_experimento_condicionado_d2.md:53-65`.

**Observación 12.3 (`OPEN` en la ubicación solicitada; `PROVED` en el contrato
operativo).** El fichero anterior no define `MIN_ONLY`: allí se congela
`MIN_COVERAGE_LEX`. La definición de `MIN_ONLY` aparece en
`P1a_contrato_comparacion_selectores_balanceados_d2.md:34-58`: maximiza
`S_min(q)=min(m_-(q),m_+(q))`, entrega una única cuádrupla o se abstiene, y no usa
desempate. La implementación cuenta todas las cuádruplas que alcanzan el valor
máximo y solo devuelve una selección cuando ese conteo es uno
(`p1a_comparar_selectores_d2.py:280-306`). La ausencia de la definición en el
fichero indicado queda registrada como `SOURCE_AT_REQUESTED_LOCATION = OPEN`; la
semántica operativa no queda indeterminada porque contrato e implementación
coinciden.

**Lema 12.4 (`PROVED`: puente hacia `S`).** Si `MIN_ONLY` posee una única cuádrupla
maximizadora, esa misma cuádrupla es el único máximo de `MIN_COVERAGE_LEX`: todo
competidor tiene menor primer componente, de modo que el segundo componente no
puede desplazar al ganador ni crear un empate. Esta implicación está demostrada
también en `P1a_resultados_comparacion_selectores_balanceados_d2.md:128-145`.

### 12.2 Score continuo y direcciones de pérdida

Sean

```text
x_1+x_2=s_x=1-r_x,   y_1+y_2=s_y=1-r_y,
x_1=s_x/2+p,         y_1=s_y/2+q,
T=s_x q+s_y p.
```

**Lema 12.5 (`PROVED`: identidad algebraica).** Si
`A=x_1y_1` y `B=x_2y_2`, entonces

```text
A = s_x s_y/4 + p q + T/2,
B = s_x s_y/4 + p q - T/2.
```

Como `min(A,B)=(A+B-|A-B|)/2`, se obtiene exactamente

```text
F=min(x_1y_1,x_2y_2)
 = s_x s_y/4 + p q - |T|/2.
```

Sobre `T=0`, es decir, `q=-(s_y/s_x)p`, queda

```text
F=s_x s_y/4-(s_y/s_x)p^2.
```

Por tanto, la única dirección cuadráticamente plana es la tangente `T=0`; los
restos `r_x,r_y` y la dirección transversal `T` tienen pérdida lineal.

**Lema 12.6 (`PROVED`: coercividad local).** En la caja
`s_x,s_y>=3/4`, `|p|<=1/4`, sea `D=1/4-F`. Sustituyendo
`q=-(s_y/s_x)p+T/s_x` en la identidad anterior,

```text
D = (1-s_xs_y)/4 +(s_y/s_x)p^2 -(p/s_x)T + |T|/2
  >= (r_x+r_y)/8 +(3/4)p^2 + |T|/6.
```

La primera cota usa
`1-s_xs_y=r_x+r_y-r_xr_y >= (r_x+r_y)/2`; las otras usan
`s_y/s_x>=3/4` y `|p|/s_x<=1/3`. Fuera de una vecindad fija de esta caja, la
unicidad del máximo continuo y la compacidad dan una pérdida positiva uniforme.

### 12.3 Cuádrupla plantada y paridad

Identificamos los puntos con sus dos rangos en `{1,...,n}^2` y normalizamos cada
rango mediante `(j-1)/(n-1)`.

**Construcción 12.7 (`PROVED`: caso par).** Para `n=2s`, se prescriben

```text
a_0=(1,1), b_0=(s,s), c_0=(s+1,s+1), d_0=(n,n).
```

Son cuatro puntos distintos con `a_0 prec b_0 prec c_0 prec d_0`. Si `L={1,...,s}`
y `H={s+1,...,n}`, la conservación del flujo de una permutación entre los dos
bloques da

```text
#{i in L: pi(i) in L} = #{i in H: pi(i) in H}.
```

Es decir, los dos intervalos plantados tienen exactamente la misma cardinalidad,
sin aproximación probabilística.

**Construcción 12.8 (`PROVED`: caso impar asintótico).** Para `n=2s+1`, `s>=3`, se
prescriben

```text
a_0=(1,1), b_0=(s,s), c_0=(s+2,s+2), d_0=(n,n),
pi(2)=s+1, pi(s+1)=n-1.
```

Los dos últimos puntos no están entre `b_0` y `c_0`. Con bloques de filas y columnas
`L={1,...,s}`, `M={s+1}` y `H={s+2,...,n}`, hay un flujo prescrito `L->M`, uno
`M->H`, ninguno `M->L` ni `H->M`; las ecuaciones de conservación implican de nuevo
`#(L->L)=#(H->H)`. Así se evita plantar un punto entre `b_0` y `c_0`, que generaría
puentes centrales alternativos. Los tamaños finitos excluidos no afectan al
enunciado asintótico.

**Lema 12.9 (`PROVED`: coste de la plantación).** Las prescripciones anteriores
cuestan exactamente `1/(n)_4` en el caso par y `1/(n)_6` en el impar, donde
`(n)_j=n(n-1)...(n-j+1)`. Condicionada a ellas, la biyección entre las filas y
columnas no prescritas sigue siendo uniforme.

### 12.4 Geometría y coste del marco

Fijamos `Lambda_n=Theta(log n)`,

```text
mu_n = C (Lambda_n/n)^(1/3),
nu_n = C' Lambda_n/n.
```

El marco central es la bola perforada en norma `L_infinity` de radio `c_mu mu_n`
alrededor de `(1/2,1/2)`, dejando únicamente los puntos centrales plantados. Los
marcos de esquina son las bolas `L_infinity` de radio `c_nu nu_n` alrededor de
`(0,0)` y `(1,1)`, dejando únicamente `a_0,d_0`. Las constantes geométricas
`c_mu,c_nu` son absolutas y se absorben en `C,C'`.

**Lema 12.10 (`PROVED`: una bola basta).** No hace falta una banda de área
`Theta(mu_n)`. En efecto,

```text
b_x-1/2 = p+a_x-r_x/2,
b_y-1/2 = q+a_y-r_y/2,
q=-(s_y/s_x)p+T/s_x,
c-b <= (r_x,r_y) coordenada a coordenada.
```

Por tanto, si `r_x+r_y+|T|=O(nu_n)` y `|p|=O(mu_n)`, tanto `b` como `c` caen en
una bola central de radio `O(mu_n)`; `a` y `d` caen en las bolas de esquina de
radio `O(nu_n)`. El marco formado por tres cuadrados perforados elimina todos los
extremos posibles en esa región local. Una banda macroscópica sería un
sobre-certificado de coste innecesario.

**Lema 12.11 (`PROVED`: conteo exacto del marco).** Tras retirar las `p_n` parejas
prescritas (`p_n=4` o `6`), sea `N=n-p_n`. Sean `k_0,k_c,k_1` los números de filas
y columnas no prescritas de los tres cuadrados y sea `B_n` la unión disjunta de
los tres bloques prohibidos `k_j por k_j`. Su polinomio de torres es

```text
R_B(z) = product_(j in {0,c,1})
         sum_(r=0)^(k_j) binom(k_j,r)^2 r! z^r.
```

Por inclusión-exclusión, la probabilidad condicional exacta de no contener ningún
punto no plantado en el marco es

```text
A_N(B_n)
 = sum_(r=0)^N (-1)^r [z^r]R_B(z)/(N)_r.
```

En consecuencia, para el evento de plantación más marco vacío `E_n^0`,

```text
Pr(E_n^0) = A_N(B_n)/(n)_(p_n).
```

Además, `k_c=Theta(n mu_n)`, `k_0+k_1=O(n nu_n)`. Exponiendo las filas de los
bloques, la probabilidad de evitar todas las casillas prohibidas está acotada por
debajo por

```text
(1-k_max/(N-k_0-k_c-k_1))^(k_0+k_c+k_1)
 = exp[-O(n mu_n^2)].
```

Evitar solo el bloque central tiene probabilidad

```text
binom(N-k_c,k_c)/binom(N,k_c)
 = exp[-Theta(k_c^2/N)],
```

y proporciona la cota superior correspondiente. Así,

```text
Pr(E_n^0)
 = exp[-Theta(n mu_n^2)-O(log n)]
 = exp[-Theta(n^(1/3) Lambda_n^(2/3))]
 = exp[-o(n)].
```

El coste de las esquinas es de orden `n nu_n^2=O(Lambda_n^2/n)` y no altera el
exponente central.

### 12.5 Exclusión determinista local

**Lema 12.12 (`PROVED` en `E_n^0`).** Toda cuádrupla admisible cuyos cuatro
extremos estén en la región local de Lema 12.10 coincide con la plantada. Los marcos
de esquina solo contienen `a_0,d_0`; el marco central solo contiene `b_0,c_0`, en
ese orden estricto. En el caso impar, las dos prescripciones auxiliares están fuera
de los tres marcos y no pueden intercambiar papeles con `b_0,c_0`.

Cuando la cuádrupla plantada es admisible, sus dos conteos son iguales por
Construcciones 12.7-12.8. Manteniendo `b_0,c_0`, sustituir `a_0` por cualquier
extremo posterior elimina al menos `a_0` del intervalo pasado; sustituir `d_0` por
un extremo anterior elimina al menos `d_0` del intervalo futuro. En ambos casos el
mínimo disminuye al menos en uno. Por tanto tampoco aparece un empate de endpoints.

### 12.6 Peeling fuera del marco

Sea `G_n` el evento de discrepancia uniforme local establecido para diferencias de
rectángulos de grosor normalizado `delta`:

```text
error(delta) <= A_0 min(n delta, sqrt(n delta Lambda_n)+Lambda_n),
```

simultáneamente para las dos caras de todas las cuádruplas. Aquí `A_0` es la
constante absoluta de esa desigualdad.

**Lema 12.13 (`PROVED` condicionado a la entrada de discrepancia).** Puede tomarse,
por ejemplo,

```text
c_0=1/8,
C  >= (32 A_0)^(2/3),
C' >= (128 A_0)^2.
```

Para los shells planos `delta_j=2^j mu_n`, Lema 12.6 da pérdida al menos
`c_0 n delta_j^2`, mientras el error es a lo sumo
`A_0(sqrt(n delta_j Lambda_n)+Lambda_n)`. La razón entre el término principal de
pérdida y el ruido crece como `delta_j^(3/2)` y ya es al menos cuatro en el primer
shell por la elección de `C`.

Para los shells lineales `delta_j=2^j nu_n`, la pérdida es al menos
`c_0 n delta_j`; la razón frente a
`A_0(sqrt(n delta_j Lambda_n)+Lambda_n)` crece como `sqrt(delta_j)` y ya es al
menos cuatro en el primer shell por la elección de `C'`.

La partición anterior no trata las coordenadas como si varias direcciones no
pudieran moverse a la vez. Si `b,c` son los plantados y cambia `a` o `d`, la
inclusión estricta de intervalos del Lema 12.12 decide la comparación sin ruido. Si
alguno de `b,c` no es plantado, está fuera de la bola central. Las identidades del
Lema 12.10 implican entonces, ajustando las constantes geométricas, que o bien
`|p|>=mu_n` —caso plano— o bien
`r_x+r_y+|T|>=c mu_n` —caso lineal, cuyo primer shell real está aún más lejos que
`nu_n`. Si ambas magnitudes son grandes, se asigna el rival a la que aporta el mayor
término en la cota coerciva. Escribiendo `L=r_x+r_y+|T|`, si `p^2>=L` la diferencia
geométrica es `O(|p|)` y se aplica el shell plano. Si `L>p^2`, dicha diferencia es
`O(sqrt(L))`; el cociente entre el drift `nL` y el ruido correspondiente
`sqrt(n sqrt(L) Lambda_n)` es

```text
sqrt(n/Lambda_n) L^(3/4),
```

que tiende a infinito uniformemente para `L>=c mu_n`. Esto cubre los movimientos
mixtos y evita aplicar indebidamente el perfil lineal a una diferencia rectangular
dominada por un desplazamiento tangencial. Para `delta=Theta(1)`, la pérdida
determinista es `Theta(n)` y la discrepancia global es `o(n)`.

Con `Lambda_n=L log n` y `L>8`, una cola de Bernstein de orden
`exp(-Lambda_n)` permite unir sobre `O(log n)` shells y a lo sumo `n^4`
cuádruplas por shell:

```text
Pr(G_n^c | puntos plantados) = O(n^(4-L) log n)=o(1).
```

En `E_n^0 intersect G_n`, la cuádrupla plantada es, por tanto, la única ganadora de
`MIN_ONLY`, y por Lema 12.4 también ocurre `S` con la misma cuádrupla.

### 12.7 El hueco de transferencia

**Proposición 12.14 (`OPEN`: frecuencia relativa dentro del marco).** Lo anterior no
demuestra todavía

```text
Pr(G_n | E_n^0) -> 1.
```

La cota incondicional del Lema 12.13 no puede dividirse por `Pr(E_n^0)`: su error es
polinómico en `n`, mientras
`Pr(E_n^0)=exp[-Theta(n^(1/3)(log n)^(2/3))]` es menor que toda potencia. Tras
condicionar a que un bloque central grande esté vacío, la permutación residual es
uniforme sobre biyecciones que evitan un tablero, no una permutación uniforme sin
restricciones. Hace falta una desigualdad de discrepancia relativa para ese modelo,
o un conteo directo de `E_n^0 intersect G_n`, con el mismo exponente que `E_n^0`.

Este es un hueco lógico único y localizado. Las comprobaciones finitas, la cota
incondicional de Bernstein y la mera rareza subexponencial del marco no lo reparan.

**Corolario 12.15 (`OPEN`).** Si se prueba
`Pr(G_n|E_n^0)=1-o(1)`, entonces

```text
Pr(S) >= Pr(E_n^0 intersect G_n)
      = (1-o(1)) Pr(E_n^0)
      = exp[-Theta(n^(1/3)(log n)^(2/3))]
      = exp[-o(n)].
```

Sin ese lema condicionado, la conclusión subexponencial sobre `Pr(S)` no está
demostrada.

### 12.8 Veredicto y flags

| Objeto | Estado | Alcance exacto |
| --- | --- | --- |
| dominio estricto y semántica de unicidad | `PROVED` | unicidad de cuádrupla, sin desempate |
| identidad y coercividad de `F` | `PROVED` | score continuo en `d=2` |
| dos puntos centrales y balance por paridad | `PROVED` | construcción de rangos plantados |
| bola perforada frente a banda | `PROVED` | la bola `L_infinity` basta; la banda no es necesaria |
| coste del marco vacío | `PROVED` | `exp[-Theta(n^(1/3)(log n)^(2/3))]` |
| exclusión de rivales locales | `PROVED` | dentro del marco vacío |
| peeling de rivales externos | `PROVED` condicionado a `G_n` | constantes explícitas en `A_0` |
| discrepancia relativa bajo marco vacío | `OPEN` | único lema probabilístico faltante |
| certificado completo y cota subexponencial de `Pr(S)` | `OPEN` | depende del lema anterior |
| comportamiento de `P_{2,n}` | `OPEN` | no se modifica en esta sección |

```text
EMPTY_FRAME_UNIQUENESS_CERTIFICATE = OPEN
EMPTY_FRAME_GEOMETRY = PROVED
EMPTY_FRAME_ENTROPIC_COST = PROVED
EMPTY_FRAME_CONDITIONAL_DISCREPANCY = OPEN
SUBEXPONENTIAL_UNIQUENESS_COROLLARY = OPEN
P2_STATUS = OPEN
```

**Próximo paso único (`OPEN`).** Probar una Bernstein/Freedman uniforme para conteos
de rectángulos bajo la permutación condicionada a evitar los tres bloques del marco,
con perfil local
`min(n delta,sqrt(n delta Lambda_n)+Lambda_n)` y pérdida relativa `o(1)`; de forma
equivalente, contar directamente las permutaciones del marco que satisfacen `G_n`.
No se autoriza sustituir este lema por una simulación ni por una nueva representación.
