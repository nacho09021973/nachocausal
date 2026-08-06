# P1a — Ley condicionada por selección para `COUNT_VOLUME` en `d=2` (CV-3, Ruta 1)

> **ESTADO: BORRADOR MATEMÁTICO v1.0 · CV-3 DE `emergencia/HOJA_DE_RUTA.md` ·
> RUTA 1 (FACTORIZACIÓN EXACTA) · RESULTADO PARCIAL · DOCUMENTO PURAMENTE
> DEDUCTIVO · SIN EJECUCIÓN NUMÉRICA.**
>
> Este documento continúa la Ruta 1 fijada en
> `emergencia/P1a_count_volume_experimento_condicionado_d2.md` §6. Obtiene un
> teorema de factorización exacta que separa por completo la parte geométrica
> (cerrada, tipo Beta) de la parte combinatoria (abierta, sobre permutaciones) del
> problema seleccionado por `MIN_COVERAGE_LEX`. No calcula la parte combinatoria
> pendiente, no produce ningún número nuevo y no autoriza simulación.

## 0. Objeto que se quería construir

De CV-1 (§5, cantidades Q4–Q5): la ley conjunta `(m_-,A_-,m_+,A_+)` de la cuádrupla
que gana el argmax de `S_lex`, condicionada a `S`, y de ahí
`E[ell|m,n,side,S]`, `Var[ell|m,n,side,S]`. La nota estructural de esa misma
sección proponía explotar la independencia entre el patrón de rangos y las
magnitudes de los huecos. Este documento desarrolla esa idea hasta un teorema.

## 1. Notación de rangos

Sea `C` el poset de §1.1 de CV-1, equivalente a la permutación uniforme `pi` de
`{1,...,n}` (Fase 2). Para un punto `x`, `rank_u(x)` y `rank_v(x)` son sus rangos
en `u` y en `v`; `pi(rank_u(x)) = rank_v(x)`.

Para una cuádrupla `q=(a,b,c,d) in Q_3(C)`, sean

```text
alpha = rank_u(a), beta = rank_u(b), gamma = rank_u(c), delta = rank_u(d),
alpha' = rank_v(a), beta' = rank_v(b), gamma' = rank_v(c), delta' = rank_v(d).
```

Como `a prec b prec c prec d` es una cadena, `alpha<beta<gamma<delta` y
`alpha'<beta'<gamma'<delta'`. Definimos la **forma** de `q`:

```text
k_-(q) = beta-alpha,      l_-(q) = beta'-alpha',
k_+(q) = delta-gamma,     l_+(q) = delta'-gamma',
shape(q) = (k_-(q), l_-(q), k_+(q), l_+(q)).
```

`shape(q)` es una función puramente combinatoria de `pi` (y de `q`); no involucra
coordenadas. Recordamos las magnitudes continuas ya fijadas en CV-1 §1.4:

```text
Delta u_-(q) = u_b-u_a,   Delta v_-(q) = v_b-v_a,   A_-(q)=Delta u_-(q) Delta v_-(q),
Delta u_+(q) = u_d-u_c,   Delta v_+(q) = v_d-v_c,   A_+(q)=Delta u_+(q) Delta v_+(q),
ell_-(q)=sqrt(A_-(q)),   ell_+(q)=sqrt(A_+(q)).
```

`m_-(q)=n_C(a,b)`, `m_+(q)=n_C(c,d)` (definidos en
`P1a_primer_selector_de_cobertura.md` §2) son también funciones puramente de `pi`.

## 2. CV-3.1 — independencia entre el patrón discreto y las magnitudes

**Lema.** Sean `(U_i,V_i)`, `i=1,...,n`, iid `Uniform([0,1]^2)`. Sea `pi` la
permutación de rangos definida en §1. Entonces `pi` es independiente del par de
vectores de estadísticos de orden `(U_(1),...,U_(n))` y `(V_(1),...,V_(n))`, y estos
dos vectores son independientes entre sí.

**Demostración.** `(U_(1),...,U_(n)) perp (V_(1),...,V_(n))` porque las secuencias
`(U_i)` y `(V_i)` son independientes entre sí (coordenadas independientes de cada
punto, puntos iid). Reordenando los índices por rango de `u`, sea `V'_k` el valor de
`v` del punto cuyo rango de `u` es `k`; como el reordenamiento depende solo de la
secuencia `(U_i)`, que es independiente de `(V_i)`, la secuencia `(V'_1,...,V'_n)`
sigue siendo iid `Uniform(0,1)` e independiente de `(U_(1),...,U_(n))`. Por
definición, `pi` es exactamente el vector de rangos de `(V'_1,...,V'_n)`. Por el
hecho estándar de estadísticos de orden de una muestra iid continua —el vector de
rangos de una muestra iid continua es uniforme en `S_n` e independiente de sus
propios estadísticos de orden, por intercambiabilidad de la muestra—, `pi` es
independiente de `(V_(1),...,V_(n))` (que coincide con los estadísticos de orden de
`(V'_k)`). Como `(V'_k)` y por tanto `pi` son ya independientes de
`(U_(1),...,U_(n))`, los tres objetos son mutuamente independientes. `QED`

## 3. CV-3.2 — huecos de estadísticos de orden uniformes

**Lema (huecos como Dirichlet agregado).** Sean `U_(1)<...<U_(n)` los estadísticos
de orden de `n` iid `Uniform(0,1)`, y sean `D_0=U_(1)`, `D_i=U_(i+1)-U_(i)` para
`i=1,...,n-1`, `D_n=1-U_(n)`. Entonces `(D_0,...,D_n) ~ Dirichlet(1,...,1)`
(`n+1` parámetros). Para cualquier partición de `{0,...,n}` en bloques de tamaños
`k_1,...,k_r` (`sum k_j=n+1`), la suma de huecos dentro de cada bloque,
`(S_1,...,S_r)`, satisface `(S_1,...,S_r) ~ Dirichlet(k_1,...,k_r)`, sin importar
qué índices concretos formen cada bloque.

**Demostración.** La representación `D_i=E_i/sum_j E_j` con `E_0,...,E_n` iid
`Exponential(1)` da la ley `Dirichlet(1,...,1)`, que es simétrica bajo cualquier
permutación de índices. La propiedad de agregación de la distribución Dirichlet
—sumar componentes dentro de bloques de una partición da de nuevo una Dirichlet con
parámetros iguales a las sumas de los parámetros originales— es estándar y se sigue
directamente de la misma representación exponencial: `S_j = sum_{i in bloque j} E_i
/ sum_i E_i`, y las sumas de exponenciales iid disjuntas siguen siendo
independientes Gamma, reproduciendo la construcción de Dirichlet con los nuevos
parámetros. `QED`

**Corolario CV-3.3 (ley de un hueco simple).** Para `i<j`,
`U_(j)-U_(i) ~ Beta(j-i, n-j+i+1)`. Es el caso `r=2` del lema anterior.

**Corolario CV-3.4 (ley conjunta de dos huecos disjuntos).** Para
`i_1<j_1<=i_2<j_2` (bloques disjuntos, en cualquier posición, no necesariamente
adyacentes), sea `S_1=U_(j_1)-U_(i_1)`, `S_2=U_(j_2)-U_(i_2)`, `k_1=j_1-i_1`,
`k_2=j_2-i_2`. Entonces `(S_1,S_2,1-S_1-S_2) ~ Dirichlet(k_1,k_2,n+1-k_1-k_2)`. En
particular, la ley conjunta de `(S_1,S_2)` depende únicamente de `(k_1,k_2,n)`, no
de las posiciones exactas `i_1,j_1,i_2,j_2` ni del tamaño del hueco intermedio.

**Demostración.** Aplicar el lema con la partición en tres bloques: el bloque que
forma `S_1` (tamaño `k_1`), el que forma `S_2` (tamaño `k_2`), y todos los índices
restantes agrupados en un tercer bloque (tamaño `n+1-k_1-k_2`), que por agregación
puede tratarse como un único bloque sin afectar la ley conjunta de los dos primeros.
`QED`

## 4. CV-3.5 — la ley de `A` dado el patrón depende solo de la forma

**Proposición (suficiencia de la forma).** Para todo `p_0` en el soporte de `pi`,

```text
Ley( A_-(q_{p_0}) | pi=p_0 ) = Beta(k_-(p_0), n+1-k_-(p_0)) * Beta(l_-(p_0), n+1-l_-(p_0)),
```

producto de dos Beta independientes, donde `q_{p_0}` es cualquier cuádrupla cuya
forma bajo `p_0` es `(k_-(p_0),l_-(p_0),...)`. Esta ley depende de `p_0`
**únicamente** a través de `shape(q_{p_0})`. Lo mismo vale para `A_+`, y la ley
conjunta `(A_-,A_+) | pi=p_0` depende de `p_0` únicamente a través de
`shape(q_{p_0})` completa, siendo el producto de dos Betas conjuntas
(Corolario CV-3.4, aplicado una vez en `u` y una vez en `v`, independientes entre
sí por CV-3.1).

**Demostración.** Fijado `pi=p_0`, las posiciones `alpha,beta,gamma,delta` (rangos
`u`) y `alpha',beta',gamma',delta'` (rangos `v`) de la cuádrupla ganadora quedan
determinadas como números fijos. Por CV-3.1, condicionar sobre `pi=p_0` no cambia la
ley de `(U_(1),...,U_(n))` ni la de `(V_(1),...,V_(n))`; siguen teniendo su ley
incondicional, evaluada en las posiciones fijas que dicta `p_0`. Por CV-3.3,
`U_(beta)-U_(alpha) ~ Beta(k_-,n+1-k_-)` y, por independencia de las dos
coordenadas (CV-3.1), `V_(beta')-V_(alpha') ~ Beta(l_-,n+1-l_-)` independientemente.
El producto de ambas es `A_-`. La parte conjunta con `A_+` es análoga usando
CV-3.4 una vez en cada coordenada. `QED`

**Corolario (irrelevancia de condicionar sobre eventos `pi`-medibles adicionales).**
Como `S`, `m_-`, `m_+` y el propio `shape` son funciones de `pi` únicamente, para
cualquier evento `E` medible respecto de `pi` que sea consistente con `pi=p_0`
(en particular `E=S`, o `E={m_-=m}`, o su intersección),

```text
Ley( A_- | pi=p_0, E ) = Ley( A_- | pi=p_0 ),
```

porque `{pi=p_0} subseteq E` o `{pi=p_0} cap E = vacio`. La selección no distorsiona
la geometría del hueco una vez que se conoce la forma exacta; solo decide, a través
de `pi`, **qué forma** llega a observarse.

## 5. CV-3.6 — ley exacta de `m` dado la forma

**Proposición.** Fijados `alpha,beta,alpha',beta'` con `k_-=beta-alpha`,
`l_-=beta'-alpha'`, y `pi` uniforme en `S_n` condicionado a
`pi(alpha)=alpha'`, `pi(beta)=beta'`,

```text
m_-(q) - 2 ~ Hypergeometric(N=n-2, K=l_--1, draws=k_--1),
```

y esta ley depende únicamente de `(n,k_-,l_-)`.

**Demostración.** Fijar `pi(alpha)=alpha',pi(beta)=beta'` dejar una biyección
uniforme entre los `n-2` rangos `u` restantes y los `n-2` rangos `v` restantes (la
uniformidad condicional de una permutación uniforme sobre los valores no fijados es
estándar). De los `n-2` rangos `u` restantes, exactamente `k_--1` están en el
intervalo abierto `(alpha,beta)`; de los `n-2` rangos `v` restantes, exactamente
`l_--1` están en `(alpha',beta')`. El número de los `k_--1` primeros que caen entre
los `l_--1` segundos, bajo una biyección uniforme entre poblaciones de tamaño
`n-2`, es por definición `Hypergeometric(n-2,l_--1,k_--1)`. Como
`m_-(q)=2+#{z: rank_u(z) in (alpha,beta), rank_v(z) in (alpha',beta')}`, se sigue el
enunciado. La independencia de la posición exacta es la propiedad estándar de que la
marginal de una celda de una tabla de contingencia inducida por una biyección
uniforme depende solo de los tamaños de la fila y la columna correspondientes, no de
las demás. `QED`

**Ejemplo verificable a mano (`n=4`).** Sea `k_-=2` (una posición interior en `u`,
en `alpha+1`), `l_-=2` (una posición interior en `v`, en `alpha'+1`). Quedan
`n-2=2` puntos libres, uno en cada rango restante de `u` y de `v`; hay exactamente
`2` biyecciones posibles entre ellos, y en exactamente una el punto interior en `u`
recibe el rango interior en `v`. Por tanto `P(m_--2=1)=1/2=P(m_--2=0)`, que coincide
con `Hypergeometric(N=2,K=1,draws=1)`: `P(X=1)=K/N=1/2`. El caso más pequeño no
trivial confirma la fórmula por enumeración exhaustiva hecha en el texto, sin
ejecutar código.

## 6. Ley conjunta `(m_-,m_+)` dado la forma completa — resultado exacto, sin forma cerrada simple

Fijadas las ocho posiciones (equivalentemente, `shape(q)` y las posiciones de `a`),
la asignación de los `n-2` puntos libres a los `n-2` rangos `v` libres sigue siendo
una única biyección uniforme. `m_-(q)-2` y `m_+(q)-2` son los conteos en dos celdas
disjuntas (fila y columna distintas) de la tabla de contingencia `5x5` inducida por
esa biyección, con tamaños de fila `(alpha-1,\,k_--1,\,gamma-beta-1,\,k_+-1,\,n-delta)`
y tamaños de columna análogos en `v`. La ley conjunta exacta de esa tabla es

```text
P({N_ij}) = [ prod_i (fila_i)! * prod_j (columna_j)! ] / [ (n-2)! * prod_{i,j} N_ij! ],
```

la distribución hipergeométrica multivariante estándar de tablas de contingencia con
márgenes fijos. La ley conjunta de las dos celdas `(m_--2,m_+-2)` se obtiene
marginalizando esa tabla y **sí depende**, en general, de los tamaños de los bloques
intermedios (`gamma-beta-1` y los bloques de borde), no solo de `(k_-,l_-,k_+,l_+)`.
Puede calcularse exactamente por un argumento secuencial (asignar primero el bloque
`k_-`, con ley multivariante de 3 categorías sobre las columnas
`{l_-,l_+,\text{resto}}`; luego asignar el bloque `k_+` sobre la población
restante, con ley hipergeométrica condicionada al resultado del primer paso), lo que
da una suma finita computable pero sin forma cerrada simple identificada aquí.

```text
CV3_JOINT_M_LAW = EXACT_COMPUTABLE_NO_SIMPLE_CLOSED_FORM
CV3_JOINT_M_LAW_DEPENDS_ON = (n, k_-, l_-, k_+, l_+, gamma-beta, bordes)
```

Este resultado no es necesario para el teorema central de §7 (que solo requiere la
ley de `A` dado la forma, §4, mezclada con el peso combinatorio de la forma
ganadora). Se deja registrado como respuesta parcial a Q2 de CV-1 §5 y como
herramienta de control para una futura extensión de la enumeración exacta.

## 7. Teorema central de factorización (CV-3.7)

**Teorema.** Para todo `n`, `side in {PAST,FUTURE}` y `m` alcanzable,

```text
L(ell_- | m,n,PAST,S)
  = sum_{s=(k_-,l_-)} w(s | m,n,PAST,S) * L_Beta(ell_- | s),

L_Beta(ell_- | s) = ley de sqrt(X*Y),
  X ~ Beta(k_-,n+1-k_-), Y ~ Beta(l_-,n+1-l_-), X perp Y,

w(s | m,n,PAST,S) = P( shape_-(q*) = s | m_-(q*)=m, n, S ),
```

donde `q*` es la cuádrupla que gana el argmax de `S_lex` y `w` es una probabilidad
condicional **puramente combinatoria**: depende solo de la ley de `pi`, no de
`(U_(1..n)),(V_(1..n))`. El enunciado simétrico vale para `FUTURE`.

**Demostración.** Por la ley de la probabilidad total sobre `pi`,

```text
P(A_- in dx | m,n,PAST,S)
  = sum_{p_0 : m_-(q*(p_0))=m, S(p_0)} P(pi=p_0 | m,n,PAST,S) * P(A_- in dx | pi=p_0),
```

usando el corolario de §4 para sustituir `P(A_- in dx | pi=p_0)` (que ya no depende
de condicionar además sobre `m,S`, por ser estos `pi`-medibles) por
`L_Beta(dx | shape_-(p_0))`. Agrupando el término de la suma por el valor de
`shape_-(p_0)=s` se obtiene exactamente la mezcla enunciada, con
`w(s|m,n,PAST,S) = sum_{p_0: shape_-(p_0)=s,\, m_-(q*(p_0))=m,\, S(p_0)} P(pi=p_0|m,n,PAST,S)`,
que es una suma de probabilidades de `pi`, es decir, un objeto puramente
combinatorio. `QED`

## 8. Qué resuelve este teorema y qué no

**Resuelve:**

1. separa exactamente la ley seleccionada en un factor geométrico cerrado
   (`L_Beta`, Beta-producto, sin aproximación) y un factor combinatorio (`w`);
2. muestra que la selección **no distorsiona la geometría de un hueco de forma
   dada**: toda la acción de `S_lex` ocurre en qué forma se observa, no en cómo se
   ve un hueco de esa forma;
3. da una fórmula exacta y verificable a mano para la ley marginal de `m` dado la
   forma (§5), con ejemplo `n=4` comprobado por enumeración exhaustiva en el texto;
4. reduce el problema pendiente a una única cantidad puramente combinatoria,
   `w(s|m,n,side,S)`, sin integrales continuas.

**No resuelve:**

1. el valor de `w(s|m,n,side,S)`: requiere contar, sobre las permutaciones de
   `S_n`, cuántas producen cada forma ganadora — un problema combinatorio abierto,
   no una integral geométrica;
2. por tanto tampoco calcula `E[ell|m,n,side,S]` ni `Var[ell|m,n,side,S]`
   numéricamente;
3. la ley conjunta exacta `(m_-,m_+)` dado la forma completa quedó sin forma
   cerrada simple (§6);
4. nada de esto se ha ejecutado ni verificado computacionalmente más allá del
   ejemplo `n=4` hecho a mano.

## 9. Relectura de CV-4 (cota de resolución) bajo la factorización

El teorema da una descomposición de varianza inmediata, sin resolverla:

```text
Var(ell_- | m,n,PAST,S)
  = E_s[ Var(ell_- | s) | m,n,PAST,S ] + Var_s[ E(ell_- | s) | m,n,PAST,S ],
```

donde el primer término usa solo momentos de `L_Beta(.|s)` (calculables en forma
cerrada o numérica directa, sin simulación, para cada forma `s`) y el segundo usa
únicamente la distribución combinatoria `w(s|m,n,PAST,S)` de §7. Esto localiza
exactamente qué parte de una futura cota de resolución (CV-4) es geometría cerrada
y cuál es combinatoria pendiente; no calcula ningún valor.

## 10. Relectura de CV-5 (circularidad) bajo la factorización

El corolario de §4 acota con precisión dónde puede vivir la circularidad señalada en
`P1a_resultados_representaciones_alternativas_d2.md` §8: **no puede** provenir de
una distorsión de la ley geométrica de un hueco de forma fija (esa ley es la misma
se seleccione o no, condicionado a la forma). Solo puede provenir de que
`S_lex`, al maximizar sobre `m` (una cantidad `pi`-medible), sesgue la distribución
de la **forma** `w(s|S)` frente a la distribución de forma de un candidato no
seleccionado. La pregunta de CV-5 queda así reducida exactamente a una pregunta
sobre `pi` (comparar `w(s|S)` contra la ley de forma de un candidato típico de
`Q_3(C)` sin argmax), no sobre la geometría. Esto no cierra CV-5; la precisa y la
deja lista para atacarse con la misma maquinaria combinatoria que resolvería `w`.

## 11. Ruta 1 — veredicto parcial

No se cumple el criterio de abandono de Ruta 1 fijado en
`P1a_count_volume_experimento_condicionado_d2.md` §6 (la factorización *sí* admite
forma cerrada para la parte geométrica, y reduce —no elimina— la parte
combinatoria). Tampoco se declara Ruta 1 completa: falta `w(s|m,n,side,S)`.

```text
CV3_ROUTE1_STATUS = PARTIAL_SUCCESS_STRUCTURAL_FACTORIZATION_DERIVED
CV3_ROUTE1_GEOMETRIC_FACTOR = CLOSED_FORM_BETA_PRODUCT
CV3_ROUTE1_COMBINATORIAL_FACTOR = OPEN_REQUIRES_PERMUTATION_COUNT
```

El paso siguiente natural es extender la enumeración exacta ya congelada de Fase 2
(`emergencia/p1a_enumeracion_simulacion.py`,
`emergencia/resultados/p1a_enumeracion_exacta_d2.csv`, `n=6,...,9`) para registrar,
además de vacío/único/empate, la forma `shape(q*)` de la cuádrupla ganadora cuando
existe. Esto computaría `w(s|n,side,S)` exactamente para `n` pequeño (sin condicionar
aún sobre `m`, que es una cantidad derivada de la propia forma más ruido — habría
que agregar sobre las formas compatibles con cada `m` observado). Esa extensión:

- es una modificación de código y una nueva ejecución, por lo que **no se realiza
  en este documento** (separación exploración/confirmación, `CLAUDE.md`);
- requeriría su propio contrato mínimo (qué campo nuevo se registra, qué control de
  integridad lo verifica) antes de ejecutarse, siguiendo el patrón ya usado en todos
  los contratos anteriores de P1a.

## 12. Techo de afirmación

Este documento demuestra un teorema de factorización exacta y sus corolarios. No
establece:

- ningún valor numérico de sesgo, varianza, correlación o cota de resolución;
- que `COUNT_VOLUME` sea o no identificable bajo selección (sigue abierto);
- que la circularidad de CV-5 sea benigna (queda mejor localizada, no descartada);
- resultados fuera del canal `fixed-n`, `d=2`;
- autorización para ejecutar código nuevo o para calcular un cociente
  (`RATIO_STATUS` permanece `CLOSED`).

## 13. Estado de control

```text
CV3_ESTIMAND_UNCHANGED = YES (hereda CV1 Seccion 1.5)
CV3_FACTORIZATION_THEOREM = PROVED
CV3_GEOMETRIC_LAW_CLOSED_FORM = YES (Beta product, Seccion 4 y 7)
CV3_SINGLE_SIDE_M_LAW = PROVED_HYPERGEOMETRIC (Seccion 5)
CV3_JOINT_M_LAW = EXACT_NO_SIMPLE_CLOSED_FORM (Seccion 6)
CV3_COMBINATORIAL_WEIGHT_W = OPEN_NOT_COMPUTED
CV3_NUMERICAL_EXECUTION_AUTHORIZED = NO
CV3_RATIO_AUTHORIZATION = NONE
NOVELTY_CERTIFIED = NO
CV3_STATUS = PARTIAL_COMPLETE_STRUCTURAL_RESULT_ONLY
```

## 14. Próxima acción concreta

Redactar, como documento separado y antes de ejecutar nada, el contrato mínimo de
extensión de la enumeración exacta de Fase 2 para registrar `shape(q*)` junto a los
campos ya congelados, con su propio control de integridad (coincidencia con el
ejemplo de §5 y con enumeración ingenua adicional para `n=4,5`). Solo tras ese
contrato y su ejecución tendría sentido intentar cerrar `w(s|m,n,side,S)` para el
rango exacto `n=6,...,9`, y recién entonces evaluar si el patrón exacto pequeño basta
para conjeturar la forma general (persistiendo en Ruta 1) o si hace falta pasar a
Ruta 2 (cotas analíticas).
