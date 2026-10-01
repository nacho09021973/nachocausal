# WP6 — Auditoría adversarial de prioridad del espectro Fisher de órdenes causales finitos

> **STATUS: ADVERSARIAL_SEARCH_PERFORMED / CLOSE_PRECURSOR_FOUND /
> BROAD_NOVELTY_CLAIM_REFUTED / NARROW_PRIORITY_NOT_REFUTED /
> NOT_A_NOVELTY_CERTIFICATE.**

Fecha: 2026-08-29. Esta auditoría se abre después del resultado exacto
`rank 1 -> 3` y del espectro `3/8 > 3/40 > 3/200` de
`wp6_d2_geometric_tangent_classification.md` §14. No abre `N=4`, no modifica
ningún instrumento sellado y no emite un claim público de primacía.

## 1. Pregunta sometida a falsificación

Se buscaron antecedentes de alguno de los objetos siguientes:

1. el pullback a deformaciones geométricas de la forma Fisher de la ley de
   posets causales no etiquetados de cardinalidad fija;
2. su rango, kernel o subespacio tangente visible `V_N`;
3. la variación de `V_N` con `N`, en particular una contracción estricta del
   kernel con witness explícito;
4. el espectro generalizado que compara Fisher del poset con Fisher del
   experimento continuo de sprinkling;
5. una familia `N -> V_N` o `N -> {lambda_N,j}` interpretada como resolución
   geométrica de causal sets finitos.

La búsqueda fue deliberadamente adversarial: también se examinaron trabajos
que no usan la palabra *Fisher* pero comparan estadísticamente leyes de posets.

## 2. Método y cobertura

Se cruzó el fondo local de `biblioteca/` y las auditorías WP4--WP6 previas con
búsquedas web/arXiv/INSPIRE en las familias:

```text
causal set x Fisher information / information geometry / likelihood
causal set x parameter estimation / geometric perturbation / tangent space
finite poset x Fisher information / random-poset model
causal set x kernel / rank / spectrum / geometric resolution
Bombelli statistical Lorentzian geometry x Fisher / small variations
P_n(C|G) x tangent / conformal perturbation
```

Se verificaron directamente las páginas primarias de arXiv de Bombelli 2000,
Yazdi--Kempf 2017, Yazdi--Letizia--Kempf 2021 y Janson 2011, además de la
lectura primaria ya registrada en `docs/bibliography_claims.md` §2.5ter y de
los PDFs locales previamente auditados.

Límites: no es una revisión sistemática exhaustiva; no se ejecutó un cribado
completo de MathSciNet, zbMATH, Scopus o Web of Science, ni una búsqueda de
texto completo sobre toda tesis o acta no indexada. Cero hits no certifica
novedad.

## 3. Hallazgo adversarial principal: Bombelli 2000 es el precursor directo

Luca Bombelli, *Statistical Lorentzian geometry and the closeness of
Lorentzian manifolds*, J. Math. Phys. 41 (2000) 6944--6958,
[arXiv:gr-qc/0002053](https://arxiv.org/abs/gr-qc/0002053), construye para cada
`n` el vector completo

\[
G\longmapsto \{P^{(n)}(C\mid G):C\in\mathcal P_n\}
\tag{3.1}
\]

de probabilidades de obtener cada poset no etiquetado mediante sprinkling. Lo
compara con la distancia estadística de Wootters

\[
d_n(G,G')=\frac{2}{\pi}\arccos
\sum_{C\in\mathcal P_n}
\sqrt{P^{(n)}(C\mid G)P^{(n)}(C\mid G')}.
\tag{3.2}
\]

Esta no es sólo una semejanza conceptual. Para una familia regular
`G_epsilon`, la expansión local de la afinidad de Hellinger da

\[
\sum_C\sqrt{p_C(0)p_C(\varepsilon)}
=1-\frac{\varepsilon^2}{8}
  \sum_C\frac{p'_C(0)^2}{p_C(0)}+o(\varepsilon^2),
\tag{3.3}
\]

de modo que el elemento cuadrático local de (3.2) es, salvo la normalización
global de `d_n`, exactamente la forma Fisher `G_[P]^(n)` usada en WP6.

Bombelli también declara que a `n` fijo la lista finita de probabilidades no
puede capturar toda la información de un espacio infinito-dimensional de
geometrías, y propone estudiar analíticamente el efecto de variaciones pequeñas
`g -> g + delta g`, incluidas transformaciones conformes. Por tanto:

```text
BROAD_CLAIM_GEOMETRY_TO_FINITE_POSET_INFORMATION_METRIC_IS_NEW = REFUTED
BROAD_CLAIM_FIXED_N_HAS_INVISIBLE_GEOMETRIC_DIRECTIONS_IS_NEW = REFUTED
BOMBELLI_2000_DIRECT_PRECURSOR = REQUIRED_CITATION
```

La ausencia del término *Fisher information* en título/abstract no reduce esta
precedencia: Fisher es precisamente la geometría infinitesimal de la distancia
estadística que el artículo ya aplica a las leyes de posets.

## 4. Qué no aparece resuelto en Bombelli

El precursor define la geometría estadística global, pero no se encontró en él:

- cálculo del diferencial de (3.1) para una clase geométrica concreta;
- identificación exacta de su rango, kernel o representantes de score;
- comparación de esos rangos para cardinalidades consecutivas;
- witness `f != 0` invisible a una cardinalidad y visible a la siguiente;
- problema generalizado contra el Fisher del experimento continuo;
- autovalores o direcciones preferentes de retención.

Así, WP6 debe presentarse como una **resolución local explícita de una pregunta
planteada por Bombelli**, no como la introducción de la geometría estadística de
los causal sets.

## 5. Vecinos reales que no son sinks del resultado estrecho

### 5.1 Espectros de operadores de un causal set realizado

Yazdi--Kempf, *Towards Spectral Geometry for Causal Sets* (2017),
[arXiv:1611.09947](https://arxiv.org/abs/1611.09947), y
Yazdi--Letizia--Kempf, *Lorentzian Spectral Geometry with Causal Sets* (2021),
[arXiv:2008.02291](https://arxiv.org/abs/2008.02291), estudian espectros de
propagadores, d'Alembertianos y operadores derivados de la matriz causal para
distinguir **causal sets realizados**. El segundo trabajo prueba
computacionalmente poder de clasificación hasta nueve elementos y usa
perturbaciones combinatorias por adición de un elemento y un link.

Son antecedentes obligados para cualquier uso futuro de la palabra
*spectrum*, pero su objeto es diferente:

```text
THEIR_SPECTRUM = eigenvalues of operators attached to one finite causet
WP6_SPECTRUM = generalized Fisher eigenvalues of geometric tangent directions
               after push-forward to the probability law of unlabeled posets
```

No se encontró en esos trabajos un pullback Fisher, un kernel geométrico
tangente ni una comparación `V_N` frente a `V_(N+1)`.

### 5.2 Límites de posets y reconstrucción de la ley completa

Janson, *Poset limits and exchangeable random posets* (2011),
[arXiv:0902.0306](https://arxiv.org/abs/0902.0306), desarrolla la
representación y equivalencia de leyes de todos los posets finitos mediante
kernels de poset. Es el marco global de identificabilidad para la escalera
completa, no una teoría diferencial fixed-`N`. No calcula los rangos o
autovalores de la truncación a una cardinalidad concreta.

### 5.3 Reconstrucción y observables geométricos de CST

La literatura sobre dimensión de Myrheim--Meyer, abundancias de intervalos,
topología, distancias y curvatura muestra que observables combinatorios
concretos retienen información geométrica. No se encontró una descomposición
del espacio tangente por eficiencias Fisher del **poset completo**. Estos
trabajos son contexto constructivo, no precedencia del objeto estrecho.

### 5.4 Falsos positivos de vocabulario

Los trabajos de *quantum Fisher information* con orden causal indefinido
estudian metrología de canales cuánticos y quantum switches. `Causal order` no
significa allí un poset obtenido por sprinkling de una geometría lorentziana.
Tampoco los modelos log-lineales que indexan parámetros por un poset estudian
leyes de causal sets. Se excluyen como falsos positivos.

## 6. Matriz de prioridad

| Afirmación | Antecedente más cercano | Veredicto provisional |
|---|---|---|
| Las leyes de posets finitos inducen una geometría estadística sobre geometrías lorentzianas | Bombelli 2000 | **PRECEDIDA** |
| A `N` fijo puede perderse información geométrica | Bombelli 2000 | **PRECEDIDA** en general |
| Fisher es la forma local de esa comparación | Expansión estándar de Wootters/Hellinger aplicada a Bombelli | **IMPLÍCITA / NO RECLAMAR NOVEDAD** |
| `V_2=span{x tensor x}` y `rank=1` en S1 | Ninguno encontrado | **PRIORIDAD NO REFUTADA** |
| `V_3=span{x tensor x, x tensor q+q tensor x, q tensor q}` y `rank=3` | Ninguno encontrado | **PRIORIDAD NO REFUTADA** |
| Witness `I_2(x tensor q)=0`, `I_3(x tensor q)=1/4800` | Ninguno encontrado | **PRIORIDAD NO REFUTADA** |
| Contracción estricta `ker G^(3) subsetneq ker G^(2)` | Ninguno encontrado | **PRIORIDAD NO REFUTADA** |
| Espectro generalizado `3/8 > 3/40 > 3/200` frente al experimento iid | Ninguno encontrado | **PRIORIDAD NO REFUTADA** |
| Teoría general `N -> V_N, {lambda_N,j}` | No existe todavía ni en WP6 | **PROGRAMA, NO RESULTADO** |

`PRIORIDAD NO REFUTADA` significa sólo que esta auditoría no halló un sink;
no significa `NOVELTY PROVED`.

## 7. Lenguaje permitido y lenguaje prohibido

Permitido:

> Siguiendo la geometría estadística de las leyes de posets introducida por
> Bombelli, calculamos explícitamente su pullback Fisher sobre el sector S1.
> Para `N=2,3` obtenemos los subespacios tangentes visibles, exhibimos una
> contracción estricta del kernel y resolvemos el espectro generalizado de
> retención a `N=3`. No hemos encontrado estos cálculos locales exactos en la
> literatura revisada.

Prohibido sin una auditoría externa más amplia:

> Introducimos la geometría informacional de causal sets.

> Descubrimos que los causal sets finitos tienen direcciones geométricas
> invisibles.

> Somos los primeros en definir un espectro geométrico de causal sets.

También se reserva el nombre **geometric resolution spectrum of finite causal
sets**: puede servir como nombre interno del programa, pero no debe entrar aún
en título, abstract o claim de novedad. Antes exige al menos `N=4` o un teorema
estructural en `N`, y una revisión externa centrada en Bombelli y sus citantes.

## 8. Decisión sobre el siguiente paso

```text
OPEN_N4_NOW = NO
BIBLIOGRAPHIC_GATE = PARTIALLY_PASSED_WITH_MAJOR_DEFLATION
BOMBELLI_CITATION_REQUIRED = YES
EXTERNAL_CITATION_CHAIN_REVIEW = STILL_DUE
NARROW_EXACT_RESULT = WORTH_PRESERVING
GLOBAL_TEST_STATUS = INCOMPLETE_BY_ENVIRONMENT
SCIENTIFIC_FAILURE_FROM_TEST_COLLECTION = NO
```

La colección de la suite global sigue incompleta porque el entorno carece de
`pandas` y `networkx`. Esto es una limitación de validación global del
repositorio, no evidencia contra las identidades exactas de §14; ambas cosas
deben permanecer documentalmente separadas.

El gate correcto antes de decidir sobre `N=4` es una revisión de la cadena de
citantes y descendientes de Bombelli 2000, idealmente por un lector externo al
cálculo. Si no aparece un antecedente del resultado estrecho, `N=4` pasaría a
ser el primer test de una teoría `N -> V_N, {lambda_N,j}`, no una extensión
automática del cálculo.
