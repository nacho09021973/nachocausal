# P1a — Programa estructural del grafo de reparación order-only

## 1. Estado, alcance y provenance

```text
DOCUMENT_KIND = FORMALIZATION_AND_STATIC_AUDIT
SCIENTIFIC_STATUS = STRUCTURAL_PROGRAM_OPENED_WITH_EVIDENCE_GAPS
NEW_NUMERICAL_CAMPAIGN = NO
NEW_ASYMPTOTIC_THEOREM = NO
CONDUCTANCE_DEFINED = NO
THINNING_RG_OPENED = NO
SELECTOR_CHANGED = NO
STATE_SEMANTICS_CHANGED = NO
```

Este documento abre un lenguaje común para estudiar la geometría de la ambigüedad
`order-only`. Reinterpreta únicamente resultados ya respaldados por código,
artefactos o demostraciones locales. Una familia sometida solo a probes finitos se
registra como evidencia finita, no como teorema asintótico.

Estado Git observado antes de escribir el documento, el 25 de agosto de 2026:

```text
PWD = /home/ignac/nachocausal
BRANCH = emergencia/p1a-canal-sigma-m
HEAD = a716bc128abef12f47b403fede1867c1d85bea2c
```

El worktree ya contenía cambios locales. Se preservaron sin modificación:

```text
MM docs/manuscript_limits_draft.md
 M emergencia/HOJA_DE_RUTA.md
?? emergencia/P1a_tie_aut_abundancia_nucleos_resistentes.md
?? emergencia/P1a_tie_aut_abundancia_nucleos_resistentes.md.sha256
?? emergencia/P1a_tie_aut_contraejemplo_transposiciones.md
?? emergencia/P1a_tie_aut_contraejemplo_transposiciones.md.sha256
?? emergencia/P1a_ventana_finita_atenuacion.md
?? emergencia/p1a_tie_aut_factorial_family_probe.py
?? emergencia/p1a_tie_aut_generic_cross.py
?? emergencia/p1a_tie_aut_generic_cross_exact.py
?? emergencia/p1a_tie_aut_interior_inflation_probe.py
?? emergencia/p1a_tie_aut_known_b_family_probe.py
?? emergencia/p1a_tie_aut_repeated_block_probe.py
?? emergencia/p1a_tie_aut_resistant_fibers_n8.py
?? emergencia/p1a_tie_aut_twin_inflation_probe.py
?? emergencia/p1a_ventana_finita_atenuacion_d2.py
?? emergencia/resultados/p1a_tie_aut_generic_cross_exact_n7_n9.json
?? emergencia/resultados/p1a_tie_aut_generic_cross_exact_n7_n9.json.sha256
?? emergencia/resultados/p1a_tie_aut_resistant_fibers_n8.json
?? emergencia/resultados/p1a_tie_aut_resistant_fibers_n8.json.sha256
?? tests/test_p1a_tie_aut_generic_cross.py
?? tests/test_p1a_tie_aut_resistant_fibers_n8.py
```

Los tres JSON TIE/Aut y los dos documentos con sidecar revisados coinciden con sus
SHA-256. No se ejecutaron sus generadores ni sus tests, porque al menos un test
regenera la enumeración exacta completa hasta `n=9`
(`tests/test_p1a_tie_aut_diagnostic.py:156-177`).

## 2. Espacio de vértices, ensemble y mapa al orden

Para cada `n` se fija

\[
V_n:=S_n,
\qquad
\mu_n:=\operatorname{Unif}(S_n).
\]

Una permutación etiquetada

\[
\sigma=(\sigma(0),\ldots,\sigma(n-1))
\]

determina el 2-order estricto `C_sigma` mediante

\[
i<_{C_\sigma}j
\quad\Longleftrightarrow\quad
i<j\ \text{ y }\ \sigma(i)<\sigma(j).
\]

Ésta es exactamente la convención implementada por
`emergencia/p1a_enumeracion_simulacion.py:173-199`. Se registran los mapas

\[
S_n\longrightarrow\{\text{2-orders etiquetados}\}
\longrightarrow\{\text{clases de isomorfismo}\},
\qquad
\sigma\longmapsto C_\sigma\longmapsto[C_\sigma].
\]

No se cocienta `V_n` por isomorfismos ni por órbitas. Las multiplicidades de
realizadores pertenecen a la medida inicial y pueden variar dentro de una fibra;
de hecho, el coeficiente finito `a(kappa)` no es invariante de isomorfismo
(`emergencia/P1a_tie_aut_abundancia_nucleos_resistentes.md:17-27,48-69`).

## 3. Maximizers, automorfismos y número orbital

Sea `M(C)` el conjunto completo de cuádruplas `q=(a,b,c,d)` que maximizan el score
congelado `MIN_COVERAGE_LEX`:

\[
S(C,q)=\bigl(\min(C_{ab},C_{cd}),\ C_{ab}+C_{cd}\bigr),
\qquad C_{ab},C_{cd}\ge K_0=3,
\]

en orden lexicográfico. La materialización directa está en
`emergencia/p1a_tie_aut_diagnostic.py:266-293` y se contrasta con el selector
optimizado en `emergencia/p1a_tie_aut_diagnostic.py:366-428`.

El grupo `Aut(C)` contiene todos los relabelings de los elementos que preservan la
relación estricta. Actúa componente a componente:

\[
\alpha\cdot(a,b,c,d)
=(\alpha(a),\alpha(b),\alpha(c),\alpha(d)).
\]

La instrumentación comprueba que esta acción preserva `M(C)` y construye su
partición orbital exacta
(`emergencia/p1a_tie_aut_diagnostic.py:253-263,334-363`). Se define

\[
r(C):=|M(C)/\operatorname{Aut}(C)|.
\]

Para `M(C)=emptyset` se adopta la convención natural `r(C)=0`, coherente con el
artefacto y sus guards (`emergencia/p1a_tie_aut_diagnostic.py:102-120,431-473`).

## 4. Partición EMPTY / GOOD / BAD

Para evitar la colisión con notaciones históricas de resistencia, los estados
vacíos se denotan por

\[
Z_n:=\{\sigma\in S_n:M(C_\sigma)=\varnothing\}.
\]

Las regiones buena y mala son

\[
G_n:=\{\sigma\in S_n:M(C_\sigma)\ne\varnothing,\ r(C_\sigma)=1\},
\]

\[
B_n:=\{\sigma\in S_n:r(C_\sigma)\ge2\}.
\]

La instrumentación congelada implica exactamente

\[
\begin{aligned}
Z_n&=\mathrm{EMPTY},\\
G_n&=\mathrm{UNIQUE}\ \dot\cup\ \mathrm{TIE\_AUT\_ONLY},\\
B_n&=\mathrm{TIE\_NONAUT}.
\end{aligned}
\]

En particular, `GOOD` no significa necesariamente que `|M|=1`: también contiene
empates cuyos maximizers forman una única órbita. La equivalencia se verifica en
`emergencia/p1a_tie_aut_diagnostic.py:398-417,438-473`; las definiciones publicadas
están asimismo en
`emergencia/resultados/p1a_tie_aut_exacto_d2.json:284-302`.

Por tanto

\[
S_n=Z_n\ \dot\cup\ G_n\ \dot\cup\ B_n.
\]

No se cambia la semántica histórica `EMPTY/UNIQUE/TIE`; `GOOD/BAD` es una capa
orbital paralela.

## 5. Movimiento elemental y grafo de reparación

La operación histórica intercambia los **valores alojados en dos posiciones**.
Para `0<=i<j<n`, si `t_ij` es la transposición de los índices, se define

\[
\tau=\sigma\circ t_{ij},
\]

es decir,

\[
\tau(i)=\sigma(j),\qquad \tau(j)=\sigma(i),
\]

y `tau(h)=sigma(h)` para las demás posiciones. Esto es lo que hacen, entre otros,
`emergencia/p1a_tie_aut_known_b_family_probe.py:81-89` y
`emergencia/p1a_tie_aut_factorial_family_probe.py:53-64`. Se usan **todas** las
transposiciones, no solo las adyacentes.

Se congela

\[
\mathscr G_n=(S_n,E_n^{\mathrm{tr}}),
\qquad
\sigma\sim\tau
\Longleftrightarrow
\tau=\sigma\circ t_{ij}\text{ para algún }i<j.
\]

Es un grafo simple, no dirigido y regular de grado

\[
d_n=\binom n2.
\]

Intercambiar posiciones y renombrar valores no son literalmente la misma arista en
un vértice fijo. Las dos convenciones globales son isomorfas por inversión, pues

\[
(\sigma\circ t_{ij})^{-1}=t_{ij}\circ\sigma^{-1},
\]

y el intercambio de las dos coordenadas del diagrama de permutación identifica
`C_sigma` con `C_(sigma^{-1})`. En este estudio se mantiene la convención histórica
de intercambio de posiciones.

## 6. Dos fronteras y grado puntual de reparación

Para `A subseteq B_n` se define la frontera exterior orientada ordinaria

\[
\partial A
:=\{(\sigma,\tau):\sigma\in A,\ \tau\in S_n\setminus A,\ \sigma\sim\tau\},
\]

y la frontera de reparación exitosa

\[
\partial_G A
:=\{(\sigma,\tau):\sigma\in A,\ \tau\in G_n,\ \sigma\sim\tau\}.
\]

Como `A subseteq B_n` y `G_n` es disjunto de `B_n`, se tiene
`partial_G A subseteq partial A`. Salir de `A` no equivale a llegar a `G_n`: el
vecino puede permanecer en `B_n` o llegar a `Z_n`.

El grado puntual de reparación es

\[
g_n(\sigma):=\#\{\tau\in G_n:\sigma\sim\tau\},
\qquad \sigma\in B_n.
\]

Esta definición coincide con el `g_n` histórico
(`emergencia/P1a_tie_aut_contraejemplo_transposiciones.md:19-40`): cada par `i<j`
produce un vecino distinto y los probes consideran bueno exactamente un estado no
vacío con una órbita.

Con la frontera de aristas orientadas aquí adoptada existe la identidad definicional

\[
|\partial_G A|=\sum_{\sigma\in A}g_n(\sigma).
\]

Por tanto, la advertencia correcta no es que toda la colección de grados puntuales
sea incapaz de determinar la frontera de aristas. Lo que **no** basta es un solo
testigo, el mínimo, el máximo o una cota sobre una configuración para controlar una
población completa, una frontera de vértices, una normalización de expansión, una
conductancia no definida o un tiempo de escape multistep.

Se conserva así la jerarquía de preguntas sin afirmar implicaciones no demostradas:

\[
\text{resistencia de un vértice}
\longrightarrow
\text{distribución de }g_n\text{ en }A
\longrightarrow
\text{frontera normalizada de }A
\longrightarrow
\text{dinámica multistep}.
\]

Solo la igualdad no normalizada anterior queda congelada en esta fase. No se define
conductancia ni cadena de Markov.

## 7. Masa, entropía y déficit entrópico

Para `A subseteq S_n`,

\[
\mu_n(A)=\frac{|A|}{n!}.
\]

Se define el déficit entrópico

\[
\Delta_n(A):=\log(n!)-\log|A|.
\]

La igualdad solicitada se verifica algebraicamente:

\[
-\log\mu_n(A)
=-\log\left(\frac{|A|}{n!}\right)
=\log(n!)-\log|A|
=\Delta_n(A).
\]

No son dos términos que deban sumarse. Tampoco se identifican los regímenes

\[
\log|A_n|=\Theta(n\log n),
\qquad
\Delta_n(A_n)=O(n),
\qquad
\Delta_n(A_n)=o(n\log n),
\qquad
\liminf_n\mu_n(A_n)>0.
\]

La primera condición solo fija una escala gruesa de cardinalidad. Las siguientes
controlan déficits progresivamente más informativos para la medida uniforme.

## 8. Resistencia sublineal sin colisión de notación

El documento histórico usa

\[
R_n^{\mathrm{hist}}
=\{\kappa\in B_n:a(\kappa)=0\},
\]

donde `a(kappa)` pertenece a una cirugía genérica de núcleo y no es el grado total
`g_n` (`emergencia/P1a_tie_aut_abundancia_nucleos_resistentes.md:17-27`). Para no
reutilizar `E_n` —reservado aquí al conjunto de aristas—, ni `Z_n`, ni ese `R_n`
histórico, se propone la notación inequívoca

\[
\operatorname{LowRep}_n(\varepsilon)
:=\{\sigma\in B_n:g_n(\sigma)\le\varepsilon n\}.
\]

No se cambia ningún fichero ni símbolo histórico.

## 9. Resultados existentes reinterpretados

| Objeto | Estatus auditable en este worktree | Traducción al repair graph | Soporte local |
|---|---|---|---|
| Enumeración `n=6` | Exacta y congelada | `EMPTY=719`, `G=1`, `B=0` | `emergencia/resultados/p1a_tie_aut_exacto_d2.json:1-42` |
| Enumeración `n=7` | Exacta y congelada | `EMPTY=5003`, `UNIQUE=32`, `TIE_AUT_ONLY=4`, `B=1` | `emergencia/resultados/p1a_tie_aut_exacto_d2.json:43-100` |
| Enumeración `n=8` | Exacta y congelada | `EMPTY=39429`, `UNIQUE=677`, `TIE_AUT_ONLY=143`, `B=71` | `emergencia/resultados/p1a_tie_aut_exacto_d2.json:101-167` |
| Enumeración `n=9` | Exacta y congelada | `EMPTY=344837`, `UNIQUE=12220`, `TIE_AUT_ONLY=3203`, `B=2620` | `emergencia/resultados/p1a_tie_aut_exacto_d2.json:168-239` |
| Secuencia antichain-padded `sigma_(8+k)` | Teorema analítico apoyado en núcleo finito | `sigma_(8+k) in B_(8+k)` y `g_(8+k)(sigma_(8+k))<=108` para todo `k>=0` | `emergencia/P1a_tie_aut_contraejemplo_transposiciones.md:78-100,102-209` |
| Fibra isomorfa `C_kappa disjoint_union A_k` | Lema analítico | Tiene exactamente `2(k+1)` realizadores en `S_(8+k)` y está contenida en `B_(8+k)`; no se demuestra que todos sus realizadores tengan `g<=108` | `emergencia/P1a_tie_aut_abundancia_nucleos_resistentes.md:71-115` |
| Decoraciones binarias conocidas | Pertenencia y cardinalidad demostradas | Producen `2^floor(k/2)` elementos de `B_(8+k)` | `emergencia/P1a_tie_aut_abundancia_nucleos_resistentes.md:116-132` |
| Grado `g=6` en la familia binaria | Solo probe acotado | Verificado por código para `1..3` celdas, ambos residuos y todas las palabras binarias de ese dominio; no es todavía `g_(8+k) identically 6` para todo `k` | `emergencia/p1a_tie_aut_known_b_family_probe.py:1-7,18-28,72-108` |
| Familia chain-dominant factorial | Solo falsificador acotado localizado | Para `k=2,3,4` y tres bloques fijos comprueba la pertenencia a `B` y el rectángulo de reparaciones cross; no enumera `pi in S_k` | `emergencia/p1a_tie_aut_factorial_family_probe.py:1-5,16-31,42-74,84-88` |
| Cota factorial `|B_n|>=k_n!` | No respaldada por una prueba local localizada | No se eleva a resultado | El probe anterior no demuestra uniformidad en `pi` ni una extensión para todo `n` |
| `log|B_n|=Theta(n log n)` | No respaldado todavía por los ficheros localizados | El resultado local demostrado es solo `|B_(8+k)|>=2^floor(k/2)`; junto con `|B_n|<=n!` da límites de escalas distintas | Documento de abundancia, líneas 116-153 |
| Fibras resistentes en `n=8` | Exacto, finito, no asintótico | `|B_8|=71`, catorce realizadores con `a=0`, repartidos en ocho fibras; `a` no es invariante de isomorfismo | `emergencia/P1a_tie_aut_abundancia_nucleos_resistentes.md:29-69` |
| Inflaciones y bloques repetidos | Probes acotados | Falsadores y casos de prueba, no teoremas asintóticos | docstrings y dominios de `p1a_tie_aut_repeated_block_probe.py`, `p1a_tie_aut_twin_inflation_probe.py`, `p1a_tie_aut_interior_inflation_probe.py` |

### 9.1 Resultado resistente realmente demostrado

La afirmación asintótica segura es la existencia de una secuencia, una configuración
por cada `n=8+k`, tal que

\[
\sigma_{8+k}\in B_{8+k},
\qquad
g_{8+k}(\sigma_{8+k})\le108.
\]

La constante `108` se descompone en `28+0+80` para las tres clases de
transposiciones. Solo acota la operación elemental aquí congelada. No demuestra una
familia exponencial de bajo grado ni resistencia frente a otras operaciones.

### 9.2 Familia binaria: separación entre abundancia y resistencia

Sí está demostrada una familia ambigua de cardinalidad

\[
2^{\lfloor k/2\rfloor}.
\]

El claim adicional

\[
g_{8+k}\equiv6
\]

solo está protegido por un probe finito para decoraciones de longitud `k=2,...,7`.
No se encontró un documento EF ni otra demostración local que cierre el dominio
asintótico. Por tanto no hay todavía una **familia resistente exponencial** auditada.

### 9.3 Familia factorial: estatus exacto

El código propone, sobre la subsecuencia `n=3k+3`, una cadena de longitud

\[
L=2k+3
\]

en skew sum con un bloque arbitrario de longitud `k`. El probe comprueba nueve casos:
`k=2,3,4` por tres realizadores fijos. En esos casos exige al menos el rectángulo

\[
k(L-4)
\]

de reparaciones chain--block. No prueba localmente, para todo `pi in S_k`, ni

\[
|\mathcal H_n|=k!,
\qquad
g_n(\sigma)\ge k(L-4),
\qquad
\log|B_n|=\Theta(n\log n).
\]

Estas fórmulas quedan como obligaciones documentales/matemáticas abiertas, no como
resultados reinterpretados.

### 9.4 Qué se sabe sobre `LowRep_n(epsilon)`

Para cada `epsilon>0`, la secuencia con `g<=108` demuestra únicamente que
`LowRep_n(epsilon)` es no vacío para tamaños suficientemente grandes de esa
secuencia. No existe en los ficheros auditados una cota asintótica para

\[
|\operatorname{LowRep}_n(\varepsilon)|,
\qquad
\mu_n(\operatorname{LowRep}_n(\varepsilon)),
\qquad\text{o}\qquad
\frac{|\operatorname{LowRep}_n(\varepsilon)|}{|B_n|}.
\]

Las frecuencias `a=0` en `n=8,9` y los probes de inflaciones no autorizan ninguna de
esas conclusiones.

## 10. Falsadores conceptuales del marco

El repair graph distingue los casos de prueba disponibles:

- `EMPTY` pertenece a `Z_n`, no a `G_n` ni a `B_n`.
- `UNIQUE` pertenece a `G_n` porque `r=1` y `|M|=1`.
- `TIE_AUT_ONLY` pertenece a `G_n` porque `r=1` aunque `|M|>1`.
- `TIE_NONAUT` pertenece a `B_n` porque `r>=2`.
- la secuencia antichain-padded da vértices puntualmente resistentes con `g<=108`;
- la familia factorial propuesta da casos finitos con muchas puertas, pero todavía
  no un teorema factorial uniforme.

No se localizó una identificación errónea entre estos cinco fenómenos. El marco
supera el falsador semántico, pero la evidencia local no llena aún los dos extremos
asintóticos presupuestos en la motivación.

## 11. Cuadrante desconocido

La pregunta estructural queda abierta. Se busca decidir si existe una sucesión

\[
A_n\subseteq B_n
\]

que combine:

1. ambigüedad interorbital genuina, ya impuesta por `A_n subseteq B_n`;
2. alta entropía o masa bajo una condición cuantitativa todavía por escoger;
3. frontera normalizada de reparación pequeña.

Entre las normalizaciones candidatas para una fase posterior está

\[
\frac{|\partial_G A_n|}{|A_n|}
=\frac1{|A_n|}\sum_{\sigma\in A_n}g_n(\sigma).
\]

No se congela todavía como criterio definitivo. Tampoco se introduce `Phi_G`, pues
primero deben fijarse si se normaliza por volumen de grado, masa uniforme, frontera
de aristas o frontera de vértices y qué se considera escape exitoso.

## 12. Formulación WALL

`WALL` significaría la existencia de una población `A_n subseteq B_n` con
ambigüedad interorbital, alta masa/entropía en un régimen explícitamente cuantificado
y frontera o capacidad de reparación pequeña bajo una dinámica congelada.

Esta fase no afirma que tal población exista. En particular, ni una secuencia de
vértices con `g=O(1)` ni una familia grande contenida en `B_n` satisfacen por sí
solas la formulación.

## 13. Formulación NO-WALL

`NO-WALL` significaría una desigualdad isoperimétrica demostrada que obligase a una
población interorbitalmente ambigua suficientemente abundante a tener frontera de
reparación grande, con todos los cuantificadores y normalizaciones declarados.

Esta fase no propone todavía una desigualdad concreta ni afirma que exista. WALL y
NO-WALL se conservan como desenlaces simétricos.

## 14. Obligaciones matemáticas abiertas

1. Escribir o localizar una prueba uniforme de pertenencia, cardinalidad y grado
   para la familia binaria; el probe finito no basta.
2. Escribir o localizar una prueba uniforme de la familia factorial para todo
   bloque `pi`, incluida la acción de automorfismos y la cota de reparaciones.
3. Precisar el dominio en `n` de la construcción factorial y justificar cualquier
   extensión desde la subsecuencia `n=3k+3`.
4. Solo después de 2--3, decidir si `log|B_n|=Theta(n log n)` vale para todo `n`,
   para una subsecuencia o bajo otra convención.
5. Elegir un régimen de abundancia: escala factorial gruesa, déficit `O(n)`, déficit
   `o(n log n)` o masa uniformemente positiva.
6. Elegir frontera de aristas o de vértices y una normalización que no confunda
   escape de `A_n`, escape de `B_n` y llegada a `G_n`.
7. Estudiar la distribución de `g_n` en poblaciones, no inferirla de un testigo de
   grado mínimo.
8. Decidir en una fase separada si las transposiciones son la dinámica adecuada o
   si switchings o thinning requieren otros grafos o kernels.
9. Solo tras esas decisiones considerar conductancia, capacidad o tiempos de
   escape multistep.

## 15. NON-CLAIMS

No está demostrado en los materiales auditados:

- que exista una población resistente de peso positivo;
- que `LowRep_n(epsilon)` sea negligible;
- que exista una desigualdad isoperimétrica No-Wall;
- que la familia resistente conocida sea representativa de `B_n`;
- que exista ya una familia exponencial con `g=O(1)`;
- que la familia binaria tenga `g identically 6` fuera del dominio finito probado;
- que la familia factorial propuesta cubra todo `pi in S_k` asintóticamente;
- que `|B_n|>=k_n!` o `log|B_n|=Theta(n log n)` esté demostrado por los ficheros
  localizados;
- que `g_n` controle una conductancia todavía no definida;
- que una conductancia controle tiempo de reparación;
- que las transposiciones sean la dinámica definitiva;
- que thinning-RG cierre globalmente;
- que el coeficiente principal de `log|B_n|/(n log n)` sea `1/3`;
- que exista un Wall;
- que no exista un Wall;
- que The Wall esté resuelto.

Techo de afirmación de esta pasada:

> Se ha definido y auditado estáticamente un marco mínimo de grafo de reparación
> compatible con la semántica TIE/Aut y con el grado por transposiciones ya
> demostrado; dos claims asintóticos usados para motivar los extremos —resistencia
> exponencial y familia factorial uniforme— requieren todavía soporte local.
