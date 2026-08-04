# P1a — Selección intrínseca de dos intervalos y obstrucción por automorfismos

> **ESTADO: BORRADOR MATEMÁTICO v0.1 · RESULTADOS ELEMENTALES INTERNOS ·
> PRIORIDAD NO CERTIFICADA.**
>
> Esta nota abre P1a dentro de la línea **Identificabilidad del tiempo métrico
> desde orden causal finito**. Su alcance es exclusivamente definicional y
> estructural: todavía no afirma que una razón de longitudes de cadenas estime una
> razón de tiempos propios, no autoriza simulaciones y no reclama novedad para la
> maquinaria de acciones de grupos utilizada.

## 0. Pregunta exacta

Sea `C` un poset finito observado únicamente a través de su clase de isomorfía.
Queremos saber cuándo puede obtenerse de `C` un par de intervalos temporales

```text
(J_1(C), J_2(C))
```

sin proporcionar coordenadas, embedding, etiquetas, endpoints o reglas de desempate
dependientes de una representación externa.

Todo intervalo posee matemáticamente dos extremos. La prohibición de endpoints en
P1a significa que esos extremos no se entregan como input: la regla debe seleccionarlos
como parte de su salida usando solo orden y número.

P1a es anterior a la estimación métrica. Primero hay que establecer si el objeto que
se desea medir está bien definido en el poset no etiquetado.

## 1. Convenciones

Sea `C=(V,prec_C)` un poset finito. Escribimos `x <=_C y` para la clausura reflexiva
del orden estricto. Para `x prec_C y`, el intervalo causal cerrado es

```text
[x,y]_C = {z in V : x <=_C z <=_C y}.
```

Representaremos el intervalo por su par de extremos `(x,y)`, que queda determinado
por el subposet cerrado. Sea

```text
I(C) = {(x,y) in V^2 : x prec_C y}
```

el conjunto de intervalos orientados de `C`.

Una condición de admisibilidad puede exigir, por ejemplo:

- cardinalidad mínima `|[x,y]_C| >= k`;
- altura mínima `L_C(x,y) >= ell`;
- o que satisfagan una propiedad order-only previamente congelada.

Denotaremos por `A(C) subseteq I(C)` la familia de intervalos admisibles. Exigimos
que la admisibilidad sea equivariante: todo isomorfismo `phi:C -> C'` debe inducir

```text
(x,y) in A(C)  si y solo si  (phi(x),phi(y)) in A(C').
```

La teoría siguiente no depende de cuál de estas condiciones se adopte.
Las condiciones que involucren simultáneamente a los dos intervalos —ser distintos,
adyacentes, anidados o disjuntos— se incorporarán en el espacio de pares candidato,
no en `A(C)`.

## 2. Tres espacios de salida que no deben confundirse

### 2.1 Par ordenado

Para una razón orientada `tau(J_1)/tau(J_2)`, el espacio candidato básico es

```text
X_ord(C) = {(J_1,J_2) in A(C)^2 : J_1 != J_2}.
```

Si la pregunta científica exige una relación adicional entre ambos intervalos,
`X_ord(C)` se restringirá mediante un predicado de pares igualmente equivariante.

Intercambiar los componentes transforma la razón en su inversa. Por eso el orden de
los dos intervalos forma parte del target.

### 2.2 Par no ordenado

Si el target es simétrico, por ejemplo

```text
max{tau(J_1),tau(J_2)} / min{tau(J_1),tau(J_2)}
```

o `|log tau(J_1)-log tau(J_2)|`, puede usarse

```text
X_unord(C) = {{J_1,J_2} : J_1,J_2 in A(C), J_1 != J_2}.
```

Un automorfismo puede fijar este par como conjunto aunque intercambie sus dos
componentes. Esta posibilidad desaparece para un par ordenado.

### 2.3 Salida conjuntista

Cuando no existe un candidato único, puede conservarse una familia completa

```text
S(C) subseteq X_ord(C)
```

o el multiconjunto de todos los valores de un funcional sobre ella. Esta salida no
selecciona en secreto un representante de una órbita simétrica.

## 3. Definición de selector intrínseco

Sea `D` una clase de posets finitos cerrada bajo isomorfismos. Un selector
determinista equivariante de pares ordenados es una asignación

```text
F_C in X_ord(C),   C in D,
```

tal que para todo isomorfismo `phi:C -> C'`,

```text
F_C' = phi(F_C).
```

La acción sobre un intervalo y sobre un par se define componente a componente:

```text
phi(x,y) = (phi(x),phi(y)),
phi(J_1,J_2) = (phi(J_1),phi(J_2)).
```

Esta condición expresa que cambiar las etiquetas de una presentación del mismo
poset solo cambia las etiquetas de la salida. Para un automorfismo
`alpha in Aut(C)` se reduce a

```text
alpha(F_C) = F_C.
```

Por tanto, una salida determinista válida debe ser un punto fijo de todo el grupo de
automorfismos, no solo un candidato con una puntuación alta.

## 4. Proposición P1a.1 — criterio exacto de punto fijo

### Enunciado

Existe un selector determinista equivariante sobre `D` con valores en `X_ord(C)` si
y solo si, para todo `C in D`,

```text
Fix_Aut(C)(X_ord(C))
  = {u in X_ord(C) : alpha(u)=u para todo alpha in Aut(C)}
```

es no vacío.

El mismo enunciado vale para pares no ordenados o para cualquier otra familia finita
de candidatos definida de manera equivariante.

### Demostración

**Necesidad.** Sea `F` un selector equivariante y sea `alpha` un automorfismo de
`C`. Aplicando equivariancia,

```text
alpha(F_C) = F_C.
```

Luego `F_C` pertenece al conjunto de puntos fijos.

**Suficiencia.** Elegimos un representante `R` de cada clase de isomorfía de `D` y
un punto fijo `u_R` de su espacio candidato. Para cualquier `C` isomorfo a `R`, sea
`phi:R -> C` un isomorfismo y definimos

```text
F_C = phi(u_R).
```

Si `psi:R -> C` es otro isomorfismo, entonces `psi^(-1) phi` es un automorfismo de
`R`. Como `u_R` es fijo bajo todos los automorfismos,

```text
phi(u_R) = psi(u_R).
```

La definición no depende del isomorfismo usado y es equivariante. `QED`

### Alcance del criterio

El criterio caracteriza la **posibilidad de una selección equivariante**. No afirma
que una selección entre varios puntos fijos sea científicamente canónica. Si se
prohíbe además toda convención de desempate, la regla concreta deberá producir un
único ganador o abstenerse.

## 5. Corolarios y contraejemplos mínimos

### 5.1 No existe un selector universal sobre todos los posets finitos

Una anticadena con al menos dos elementos no contiene ningún par comparable, por lo
que `A(C)` y todos los espacios de pares de intervalos están vacíos.

La imposibilidad persiste aunque se restrinja la atención a posets con intervalos.
Considérese la suma disjunta de dos cadenas de dos elementos:

```text
a_0 prec a_1,    b_0 prec b_1.
```

Sus únicos intervalos no degenerados son `[a_0,a_1]` y `[b_0,b_1]`. El automorfismo
que intercambia las dos cadenas intercambia también ambos intervalos. No existe un
intervalo individual fijado por todo `Aut(C)` y, en consecuencia, no puede existir
un selector determinista de un solo intervalo.

El par **no ordenado** formado por ambos intervalos sí es fijo. El par ordenado no lo
es. Este ejemplo demuestra que la orientación del target importa.

### 5.2 Mínimo y máximo únicos no bastan para obtener dos intervalos

Sea `B_k`, con `k >= 2`, el poset acotado

```text
0 prec u_i prec 1,   i=1,...,k,
```

sin otras relaciones entre los `u_i`. Su grupo de automorfismos contiene todas las
permutaciones de los elementos intermedios.

El intervalo total `[0,1]` es fijo, pero los intervalos `[0,u_i]` forman una órbita y
los intervalos `[u_i,1]` forman otra. Ninguno de ellos es fijo individualmente. Así,
`B_k` tiene extremos globales intrínsecos y aun así no admite un par **ordenado de
intervalos distintos** cuyos dos componentes sean fijados por todos los
automorfismos.

Para `k >= 3`, tampoco puede seleccionarse como salida un par no ordenado de dos
miembros de una de esas órbitas: el grupo simétrico no fija ningún subconjunto propio
de exactamente dos miembros.

### 5.3 Rigidez elimina la obstrucción, pero no define por sí sola una regla

Si `Aut(C)` es trivial y `X_ord(C)` no es vacío, todos sus candidatos son puntos
fijos. Por tanto, no existe obstrucción de simetría. Sin embargo, si hay muchos
candidatos, todavía debe congelarse una regla matemática para escoger uno. La frase
“el poset es rígido” no especifica cuál debe ser el par.

## 6. Scores intrínsecos y tratamiento de empates

Sea

```text
Q_C : X_ord(C) -> R^r
```

un score con orden lexicográfico fijado y construido solo con invariantes del poset:
cardinalidades de intervalos, alturas, números de relaciones, perfiles de pasado y
futuro, tipos de isomorfía de subintervalos u otros conteos declarados. Debe cumplir

```text
Q_C'(phi(u)) = Q_C(u)
```

para todo isomorfismo `phi:C -> C'`.

Entonces

```text
Argmax Q_C
```

es un conjunto equivariante. Si el máximo es único, su único elemento es un punto
fijo y define un selector intrínseco. Si hay empate, elegir el primer candidato de
una enumeración o el de menor etiqueta viola P1a.

### Lema P1a.2 — una regla invariante no puede romper una órbita

Si `u` y `v` pertenecen a la misma órbita de `Aut(C)`, todo score invariante satisface

```text
Q_C(u) = Q_C(v).
```

Por tanto, ningún refinamiento construido exclusivamente con invariantes puede
separar dos candidatos que el propio poset hace simétricos. Añadir más conteos puede
separar órbitas distintas; nunca puede separar miembros de una misma órbita. `QED`

## 7. Selector parcial sin desempate

La salida más estricta para P1a es una aplicación parcial:

```text
F_Q(C) =
  el único elemento de Argmax Q_C,  si existe uno;
  UNDEFINED_SYMMETRY_OR_TIE,        en otro caso.
```

Esta regla:

1. es determinista;
2. es equivariante;
3. no usa etiquetas;
4. no rompe empates;
5. y hace observable el dominio exacto en el que puede seleccionarse el par.

No debe confundirse `UNDEFINED_SYMMETRY_OR_TIE` con ausencia de información métrica.
Solo significa que ese selector puntual no está definido para esa realización.

## 8. Primer testigo positivo: intervalo acotado con midpoint único

Sea `C` un poset con mínimo `0` y máximo `1` únicos. Para cada
`m in C \ {0,1}`, definimos

```text
n_-(m) = |[0,m]_C|,
n_+(m) = |[m,1]_C|,
Q_mid(m) = min{n_-(m),n_+(m)}.
```

También podría utilizarse el producto o la media geométrica. La elección entre estas
variantes debe congelarse antes de cualquier comparación.

Sea

```text
M(C) = Argmax_m Q_mid(m).
```

`M(C)` es un subconjunto intrínseco y equivariante. Si `M(C)={m_*}`, entonces

```text
F_mid(C) = ([0,m_*]_C, [m_*,1]_C)
```

es un par ordenado de intervalos seleccionado sin endpoints externos ni desempate.
Los extremos `0`, `m_*` y `1` han sido reconocidos desde el propio orden.

Esta construcción es un testigo de que P1a puede resolverse en una subclase no vacía.
No resuelve todavía P1:

- el poset debe tener mínimo y máximo únicos;
- el midpoint debe ser único;
- y seleccionar por balance hace que la razón entre los dos intervalos tienda a ser
  cercana a `1` por construcción.

Por ese último motivo, `F_mid` es adecuado para estudiar **definibilidad**, pero no
debe usarse sin más para reclamar recuperación de una razón temporal latente no
trivial.

## 9. Salidas legítimas cuando el selector puntual falla

Si `Argmax Q_C` contiene varios elementos, existen tres extensiones honestas:

### 9.1 Salida de órbita o conjunto completo

Conservar `Argmax Q_C` y aplicar después un funcional simétrico. Esta es la opción
preferente si el objetivo científico tolera un multiconjunto de razones.

### 9.2 Selector aleatorizado equivariante en ley

Muestrear uniformemente del conjunto finito `Argmax Q_C`. La distribución resultante
es equivariante, aunque una realización concreta no sea un objeto determinado por el
poset. Requiere declarar una fuente adicional de aleatoriedad y cambia el target.

### 9.3 Abstención

Declarar la realización no seleccionable por esa regla. En un modelo generativo, la
probabilidad de abstención pasa a ser una cantidad que debe acotarse o estimarse.

No es admisible escoger por etiqueta, orden de almacenamiento, canonical labeling
con una elección no invariante posterior, coordenada reconstruida o acceso al
embedding latente.

## 10. Distinción entre cuatro preguntas

P1a solo aborda la primera capa:

1. **Definibilidad:** ¿el poset determina el par o un conjunto de pares?
2. **Observabilidad estadística:** ¿la salida es una función medible de la clase de
   isomorfía observada?
3. **Correspondencia métrica:** ¿las longitudes discretas convergen a tiempos propios
   de regiones latentes bien definidas?
4. **Identificabilidad:** ¿dos modelos con distinta razón temporal inducen leyes
   observacionales diferentes?

Una respuesta positiva a (1) no implica ninguna de las conclusiones métricas de
(3)–(4).

## 11. Programa matemático inmediato

### P1a-A — resultado estructural

Formalizar como resultado reutilizable el criterio de punto fijo, distinguiendo:

```text
EMPTY_CANDIDATE
NO_FIXED_POINT
MULTIPLE_FIXED_POINTS
UNIQUE_INTRINSIC_PAIR
```

Las proposiciones P1a.1–P1a.2 son maquinaria estándar de acciones de grupos. El
resultado puede ser válido y reutilizable sin constituir una novedad.

### P1a-B — dominio midpoint

Definir la clase

```text
D_mid^uniq = {
  C : C tiene minimo y maximo unicos y |M(C)|=1
}.
```

Probar formalmente que `F_mid` es equivariante sobre esa clase y registrar qué ocurre
para todos los empates. Este será el primer selector positivo, no el selector final
de la razón métrica.

### P1a-C — selector no circular

El primer score queda congelado en:

```text
emergencia/P1a_primer_selector_de_cobertura.md
```

Selecciona dos intervalos causalmente ordenados y disjuntos maximizando únicamente
su cobertura total, con soporte mínimo de tres elementos por intervalo. Su criterio
no fuerza el cociente que después podría estimarse mediante alturas. Se mantienen
separados:

```text
estadistico de seleccion != estadistico de estimacion.
```

Esta es solo una separación algebraica; no establece independencia estadística ni
consistencia métrica.
La cobertura usa cardinalidades y el cociente provisional usaría alturas de cadenas;
su validez métrica y el sesgo posterior a la selección quedan para P1b.

### P1a-D — frecuencia de definibilidad

Solo después de congelar familia y selector tendrá sentido estudiar

```text
P_theta(F_Q(C) esta definido | N=n).
```

Esto requerirá un contrato teórico o numérico separado. No se presupone que la
probabilidad de rigidez, unicidad del midpoint o ausencia de empates tienda a uno.

## 12. Antecedentes y techo de prioridad

1. Brightwell, Dowker, Garcia, Henson y Sorkin caracterizan observables covariantes
   como independientes de los etiquetados. Es el antecedente conceptual directo de
   la condición de equivariancia, pero no seleccionan dos intervalos métricos.
2. Reid define midpoint scaling dentro de un intervalo causal cuyos extremos ya
   están dados. Es el precursor directo de `Q_mid`, no una solución del selector
   exterior ni de los empates.
3. Henson y Johnston reconstruyen embeddings comenzando con causal sets que ya son
   intervalos acotados; resuelven etapas posteriores bajo una hipótesis de región.
4. Major, Rideout y Surya construyen engrosamientos covariantes a partir de una
   anticadena inextendible, pero la anticadena actúa como estructura inicial.
5. Glaser y Surya usan abundancias de todos los intervalos. Su estrategia respalda
   conservar una distribución o multiconjunto en vez de imponer un representante.
6. Zalel insiste en que la información física no puede depender de etiquetas o de la
   identidad externa de elementos individuales.

Clasificación provisional:

```text
P1A_PRIORITY_STATUS = PRECURSOR_ONLY_AND_STANDARD_GROUP_ACTION
NOVELTY_CERTIFIED = NO
```

No se ha encontrado en la auditoría acotada una solución que seleccione dos
intervalos distintos en todo poset finito, porque tal solución está excluida por los
contraejemplos anteriores. Permanece abierta la prioridad de formulaciones parciales,
dominios restringidos y funcionales métricos concretos.

## 13. Referencias locales

- `biblioteca/emergencia/gr-qc0210061v2_Brightwell_et_al_Covariant_Observables.pdf`
- `biblioteca/emergencia/gr-qc0207103v2_Reid_Midpoint_Scaling_Dimension.pdf`
- `biblioteca/emergencia/gr-qc0601069v1_Henson_Constructing_Minkowski_Interval.pdf`
- `biblioteca/emergencia/gr-qc0506133v1_Major_Rideout_Surya_Spatial_Hypersurfaces.pdf`
- `biblioteca/emergencia/1309.3403v2_Glaser_Surya_Locality_Interval_Abundance.pdf`
- `biblioteca/emergencia/2008.02607v1_Zalel_Structure_of_Covtree.pdf`
- `biblioteca/emergencia/2502.09701v2_Johnston_Simpler_Embeddings_Causal_Sets.pdf`

Fuentes oficiales:

- <https://arxiv.org/abs/gr-qc/0210061>
- <https://arxiv.org/abs/gr-qc/0207103>
- <https://arxiv.org/abs/gr-qc/0601069>
- <https://arxiv.org/abs/gr-qc/0506133>
- <https://arxiv.org/abs/1309.3403>
- <https://arxiv.org/abs/2008.02607>
- <https://arxiv.org/abs/2502.09701>

## 14. Decisión actual

P1a comienza con un selector **parcial**, no universal:

```text
P1A_PRIMARY_OUTPUT = UNIQUE_ORDERED_PAIR_OR_ABSTAIN
P1A_FALLBACK_OUTPUT = FULL_EQUIVARIANT_CANDIDATE_SET
P1A_EXTERNAL_TIEBREAK = FORBIDDEN
P1A_METRIC_CLAIM = NOT_YET_AUTHORIZED
P1A_STATUS = D2_OPERATIONAL_AVAILABILITY_PASS_METRIC_VALIDITY_OPEN
```

La siguiente decisión consiste en elegir la primera familia generativa para estudiar
la probabilidad de definición, vacío y empate. La puerta teórica para la familia
Minkowski se desarrolla en `emergencia/P1a_puerta_teorica_en_Minkowski.md` y autoriza
solo el diseño de una enumeración exacta bidimensional. Todavía no existe una razón
temporal P1 validada para estimación.

La ejecución exacta y Monte Carlo posterior se recoge en
`emergencia/P1a_resultados_enumeracion_y_monte_carlo_d2.md`: el selector puntual
supera el gate operacional de frecuencia en `d=2`, mientras la validez métrica sigue
abierta.
