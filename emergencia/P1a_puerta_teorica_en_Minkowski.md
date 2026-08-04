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
