# WP6 — Auditoría adversarial de la cadena de citantes de Bombelli 2000

> **STATUS: CITATION_CHAIN_SCREENED / CLOSE_POST_BOMBELLI_NEIGHBOR_FOUND /
> FOUR_EXACT_TARGETS_NOT_FOUND / NARROW_PRIORITY_STRENGTHENED_NOT_CERTIFIED /
> N4_REMAINS_ON_HOLD.**

Fecha: 2026-08-29. Este documento continúa, con una pregunta mucho más
estrecha, `wp6_finite_causal_order_fisher_spectrum_priority_audit.md`. No abre
`N=4`, no consume semillas y no convierte ausencia de evidencia en certificado
de novedad.

## 1. Pregunta exacta

Se sometió a falsificación únicamente:

\[
\text{¿algún descendiente de Bombelli calculó explícitamente }
D_g[g\mapsto \Pr(P_N=\cdot)],
\text{ su kernel/rango o su espectro Fisher?}
\tag{1.1}
\]

Los cuatro sinks buscados fueron:

1. distinguishability a `N` finito tratada **infinitesimalmente**;
2. rango o kernel del pullback estadístico sobre perturbaciones geométricas;
3. una perturbación invisible para `N` y visible para `N+1`;
4. autovalores generalizados o cocientes de retención entre el experimento de
   posets y el experimento continuo.

## 2. Reconstrucción de la cadena

Punto de partida: Luca Bombelli, *Statistical Lorentzian geometry and the
closeness of Lorentzian manifolds*, J. Math. Phys. 41 (2000) 6944--6958,
[arXiv:gr-qc/0002053](https://arxiv.org/abs/gr-qc/0002053).

Se consultaron tres rutas de citación enlazadas desde arXiv: INSPIRE,
Semantic Scholar y Google Scholar. Las interfaces de INSPIRE y Semantic
Scholar no devolvieron la lista en esta sesión y Google Scholar no fue
accesible de forma reproducible. Se usó entonces OpenAlex por DOI como
inventario reproducible: `W1987412810`, consulta
`filter=cites:W1987412810`, que devolvió **45 registros** a 2026-08-29.

La lista contiene duplicados bibliográficos —preprint/publicación y capítulos
repetidos—, de modo que 45 no significa 45 trabajos independientes. Se cribó
por título, año, DOI, abstract y disponibilidad de texto. Los candidatos
plausibles se verificaron además en su fuente primaria o PDF completo.

Esta cobertura mejora una búsqueda por palabras clave, pero no es una cadena
perfecta: OpenAlex puede omitir citantes, fusionar mal registros o incluir una
cita sólo bibliográfica. La revisión externa sigue siendo deseable.

## 3. Clasificación de los citantes

### 3.1 Reviews, introducciones y filosofía de CST

El bloque más grande está formado por reviews y textos panorámicos: Sorkin,
Dowker, Surya y trabajos filosóficos sobre reducción/reconstrucción. Entre
ellos están *Causal Sets: Discrete Gravity*, *Introduction to causal sets and
their phenomenology*, [*The causal set approach to quantum gravity*](https://arxiv.org/abs/1903.11544),
*Causal sets and the deep structure of spacetime* y *Recovering General
Relativity from a Planck scale discrete theory of quantum gravity*.

Estos textos citan la función de cercanía de Bombelli como parte de la
Hauptvermutung o de la reconstrucción geométrica. No se encontró en ellos
ninguno de los cuatro sinks de §1. En particular, las apariciones de
`tangent`, `rank`, `kernel` o `generalised eigenvalues` en el review de Surya
2019 pertenecen, respectivamente, a operadores diferenciales/discretos,
rangos causales o problemas espectrales de campos; no al diferencial de
`G -> P_N(.|G)`.

### 3.2 Distancias entre espacios lorentzianos

Noldus y trabajos posteriores desarrollan distancias Lorentzian
Gromov--Hausdorff, espacios métricos-medida parcialmente ordenados y moduli de
espaciotiempos. Son descendientes matemáticos de la pregunta de cercanía, pero
no calculan el pullback infinitesimal de las probabilidades de posets a
cardinalidad fija. No son sinks del resultado WP6.

### 3.3 Observables geométricos concretos

Otro bloque estudia longitudes de caminos, dimensión, topología, estructura
local, intervalos y fenomenología cosmológica. Estos trabajos muestran o usan
sensibilidad de observables particulares a geometría, pero no la forma Fisher
del **poset completo** ni su rango sobre un espacio tangente geométrico.

### 3.4 Citantes incidentales de otras áreas

La lista incluye loop quantum gravity, estados coherentes, algebraic quantum
gravity y otros trabajos donde Bombelli aparece como contexto para una noción
de distancia o discreción. El objeto probabilístico de (1.1) no se desarrolla.

## 4. El candidato realmente próximo: Surya 2025/2026

Sumati Surya, *A Closeness Function on Coarse Grained Lorentzian Geometries*,
[arXiv:2510.19403](https://arxiv.org/abs/2510.19403), Phys. Rev. D 113 (2026),
es el único descendiente localizado que prolonga de forma técnica y directa
la agenda de Bombelli.

En vez del vector completo de probabilidades de posets `P_N`, usa el espectro
de abundancias esperadas de intervalos

\[
\mathcal S_N(M,g)=
\bigl(\langle N_0^{(N)}\rangle,\ldots,
      \langle N_{N-2}^{(N)}\rangle\bigr)
\tag{4.1}
\]

y define distancias `L^r` entre estos vectores. El paper:

- declara su función estrictamente más débil que la de Bombelli;
- estudia degeneración o *interval isospectrality*;
- muestra ejemplos donde añadir invariantes levanta degeneraciones;
- muestra para familias FRW/de Sitter cómo ciertas degeneraciones del espectro
  de intervalos se levantan al aumentar `N`;
- propone una noción de convergencia y compara dimensiones/scale factors.

Esto es un antecedente **material** para cualquier frase informal del tipo
“más elementos abren resolución geométrica”. Obliga a distinguir:

```text
SURYA_2025_OBJECT = L^r distances between expected interval-abundance spectra
                    (a compression of the poset law)
WP6_OBJECT = Fisher pullback of the full unlabeled-poset law on geometric
             tangent perturbations, compared with the continuous iid experiment
```

La lectura a texto completo no localizó `Fisher`, `Hellinger`, `Wootters`,
`infinitesimal`, `tangent`, `derivative`, `information retention` o un problema
generalizado de autovalores aplicado al mapa geométrico-probabilístico. Sus
degeneraciones son igualdades de espectros de abundancias, no kernels del
diferencial de la ley completa. Tampoco exhibe una misma perturbación tangente
con Fisher cero a `N` y positivo a `N+1`.

Veredicto:

```text
SURYA_2025_PRECEDES_GENERIC_RESOLUTION_WITH_N_NARRATIVE = YES
SURYA_2025_PRECEDES_EXACT_TANGENT_FISHER_CLASSIFICATION = NO_EVIDENCE_FOUND
SURYA_2025_REQUIRED_NEAR_NEIGHBOR_CITATION = YES
```

## 5. Resultado de los cuatro tests

| Test adversarial | Resultado en la cadena cribada | Veredicto |
|---|---|---|
| Diferencial explícito `D_g[g -> Pr(P_N=.)]` | No localizado | **NO SINK FOUND** |
| Rango/kernel del pullback sobre perturbaciones geométricas | No localizado | **NO SINK FOUND** |
| Misma perturbación invisible a `N` y visible a `N+1` | Surya levanta degeneraciones de un observable comprimido, pero no en este sentido tangente/Fisher | **NEAR MISS, NO SINK** |
| Espectro generalizado o retención frente al experimento continuo | No localizado | **NO SINK FOUND** |

La tercera fila es la cautela principal: no debe afirmarse que WP6 sea la
primera demostración de que aumentar `N` puede levantar una degeneración
geométrica de **algún observable causal-set**. Surya ya contiene ese relato
para espectros de abundancias de intervalos. Lo defendible es la contracción
del kernel del **pullback Fisher de la ley completa**, con witness tangente y
eficiencias relativas exactas.

## 6. Estado de prioridad actualizado

```text
FRAMEWORK_NOVELTY = NO                         # Bombelli 2000
GENERIC_MORE_N_GIVES_MORE_RESOLUTION = NO      # at least Surya 2025/2026 nearby
EXACT_N2_N3_TANGENT_CLASSIFICATION = PRIORITY_NOT_REFUTED
STRICT_FULL_POSET_FISHER_KERNEL_CONTRACTION = PRIORITY_NOT_REFUTED
GENERALIZED_RETENTION_SPECTRUM = PRIORITY_NOT_REFUTED
NOVELTY_CERTIFICATE = NO
N4 = HOLD
```

La prioridad estrecha queda **más convincente** que antes porque se inspeccionó
el descendiente técnicamente más peligroso y no contiene el objeto exacto. No
queda certificada: la limitación de cobertura de §2 y la posibilidad de un
trabajo no citante o mal indexado permanecen.

## 7. Posicionamiento permitido para una posible nota corta

Una formulación resistente sería:

> Building on Bombelli's statistical geometry of finite causal-order laws,
> and distinguishing our construction from interval-abundance closeness
> spectra, we compute the exact Fisher pullback on an explicit geometric
> tangent class. At cardinalities two and three we determine its visible
> subspaces, prove a strict kernel contraction by an explicit tangent witness,
> and solve the generalized information-retention spectrum at cardinality
> three.

Todavía no debe decirse:

- que WP6 introduce la geometría estadística de causal sets;
- que descubre por primera vez que la resolución puede crecer con `N`;
- que existe ya una teoría general del espectro de resolución;
- que la prioridad estrecha está probada por ausencia de citantes.

## 8. Decisión

La cadena de citantes no obliga a retirar el resultado exacto `N=2,3` ni su
espectro. Sí obliga a citar conjuntamente a Bombelli y Surya, y a formular la
aportación como **clasificación tangente Fisher exacta de la ley completa**, no
como marco informacional ni como narrativa genérica de resolución creciente.

Antes de abrir `N=4`, el siguiente paso de mayor valor ya no es otra búsqueda
automática. Es una lectura/revisión externa del par Bombelli--Surya y del
resultado WP6. Si esa revisión tampoco encuentra un sink, hay base razonable
para evaluar una nota corta centrada exclusivamente en `N=2,3`.
