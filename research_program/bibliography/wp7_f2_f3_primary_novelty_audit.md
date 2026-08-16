# WP7 — Auditoría primaria de novedad para `F1+F2 \not\Rightarrow F3` en `1+1`

> **STATUS: PRIMARY_SEARCH_PERFORMED / NOVELTY_NOT_REFUTED /
> NOT_A_NOVELTY_CERTIFICATE.**
>
> Documento bibliográfico separado. No modifica ni reabre la prueba de WP7, no amplía la
> geometría y no autoriza por sí solo un claim público de prioridad.

FECHA DE CORTE: 2026-08-09
RAMA: `research/f2-f3-chain-distance`
COMMIT CONGELADO: `68c9f29`
WP7 auditado: `research_program/work_packages/wp7_f2_f3_product_order_contract.md`
SHA-256 de WP7 al iniciar esta auditoría:
`0466fd19f4fb1e077588945ed5456eb7d25cc5c3bb87a0c8b9c85e541851f815`

## 1. Claim exacto sometido a auditoría

El resultado congelado que se contrasta con la literatura es el siguiente:

> Bajo la lectura regional explícita de la Remark 5.4 de Madsen y cualquiera de las dos
> convenciones estándar de norma de curvatura auditadas en WP7, existen en dimensión `1+1`
> configuraciones finitas de alta densidad con preservación exacta del orden causal (F1) y la
> cota uniforme de cuentas en diamantes mesoscópicos de Madsen (F2), con constante fija, que
> violan por un margen de factor constante la desigualdad completa de cadena–distancia F3.

En forma abreviada y con esos sufijos de alcance:

```text
F1 + F2  does not imply  F3   in 1+1 dimensions.
```

La comparación exige simultáneamente estos cinco componentes:

1. configuraciones finitas deterministas o una sucesión triangular explícita;
2. orden producto/causal exacto (F1);
3. discrepancia uniforme en **todos** los diamantes admisibles hasta la escala mesoscópica
   mínima de Madsen, con constante F2 independiente de la densidad;
4. una cadena plantada que viola la **desigualdad F3 completa por factor constante**, no solo
   una tasa asintótica o una estadística de cadenas distinta;
5. transferencia rigurosa a un parche lorentziano `1+1`, con el alcance regional y la
   convención de curvatura declarados.

No se auditan —porque WP7 no los afirma— “independencia lógica” sin calificativos, necesidad de
F3 para la conclusión final de unicidad, falsedad del teorema de Madsen, ni una construcción
nueva de cadenas largas en abstracto.

## 2. Protocolo y cobertura

Se efectuó una búsqueda adversarial en inglés sobre tres corpus complementarios:

- arXiv y páginas primarias de revistas, para combinatoria, probabilidad, geometría lorentziana
  y causal sets;
- INSPIRE-HEP, incluida su API pública, para el corpus `gr-qc`/`hep-th` y grafos de citas;
- búsqueda de frases y conceptos cruzados para localizar trabajos que pudieran formular el
  mismo fenómeno sin usar la notación F1–F3.

Familias de consultas empleadas:

```text
"On the Uniqueness of Embeddings of Causal Sets"
"F1" "F2" "F3" causal sets Madsen
causal set Lorentzian lattice longest chain number volume correspondence
causal set number-volume correspondence longest chain discrepancy
causal set non-Poisson sprinkling longest chain
causal set Planck-scale uniform longest chain
quasirandom permutation longest increasing subsequence discrepancy
permutation rectangle discrepancy longest increasing subsequence
uniform permuton longest increasing subsequence
permuton convergence LIS discontinuity
low-discrepancy permutation increasing subsequence
rectangular discrepancy approximation permuton
```

Se revisaron además:

- la historia de versiones y el grafo de citas de Madsen;
- el grafo de citas de Saravani–Aslanbeigi, buscando descendientes que combinaran sus retículos
  lorentzianos con cadenas o tiempo propio;
- los resultados recientes sobre aproximación rectangular de permutones, para no confundir
  novedad causal con novedad de discrepancia.

Se leyó texto completo primario de Madsen, Müller, Braun, Saravani–Aslanbeigi, Cooper, Dubach
`2301.07658`, Maga y Surya. Para Sjöstrand, Dubach `2307.05768` y Aghili–Bombelli–Pilgrim se
contrastaron el abstract primario y las declaraciones de resultado; no se usan para sostener el
veredicto negativo central. También se leyó el contexto de la única cita de Madsen registrada por
INSPIRE en la fecha de corte.

## 3. Matriz de precedentes primarios

| Fuente | Resultado relevante | Diferencia decisiva respecto de WP7 | Adjudicación |
|---|---|---|---|
| [Madsen, arXiv:2607.05840v1](https://arxiv.org/html/2607.05840v1), Def. 2.6, nota 1 y Remark 5.4 | Define F1–F3 y declara abierta la relación entre F1–F2 y F3; dice no conocer contraejemplo | Es la fuente de la pregunta, no una solución. La Remark 5.4 tampoco reescribe literalmente todos los cuantificadores regionales | `EXACT_OPEN_QUESTION_SOURCE` |
| [Müller, arXiv:2503.01719v2](https://arxiv.org/abs/2503.01719), Thms. 2–4 | La Hauptvermutung finita falla para una distancia lorentziana `d^-`; el mecanismo de Thm. 2 persiste bajo “Planck-scale uniformness” por sí sola. Para otra distancia `d^×`, una versión uniforme sí funciona | Compara leyes de órdenes de tamaño fijo y pares de espaciotiempos; su uniformidad no es la F2 cuantitativa de Madsen en una sucesión de alta densidad y no prueba una violación de F3 por una cadena | `CLOSEST_CAUSAL_NEGATIVE_PRECURSOR / DOES_NOT_SUBSUME` |
| [Saravani–Aslanbeigi, arXiv:1403.6429](https://arxiv.org/abs/1403.6429), §3 | En `1+1` ciertos retículos lorentzianos muestran por simulación una correspondencia número–volumen mucho menos ruidosa que Poisson para volúmenes grandes | Usa 1000 diamantes de centro y forma aleatorios. No demuestra un supremo determinista sobre todos los diamantes admisibles, no alcanza la escala exacta de Madsen y no analiza longest chains/F3 | `DIRECT_PRECURSOR_OF_F2_SIDE / DOES_NOT_SUBSUME` |
| [Cooper, arXiv:math/0211001](https://arxiv.org/abs/math/0211001) | Introduce discrepancia de intervalos/rectángulos para permutaciones y equivalencias de cuasialeatoriedad con densidades de patrones fijos | `o(n)` y patrones de tamaño fijo no controlan la constante de una LIS de tamaño creciente; no contiene cadena plantada ni transferencia causal | `DIRECT_DISCREPANCY_PRECURSOR / DOES_NOT_SUBSUME` |
| [Maga, arXiv:2605.02298](https://arxiv.org/abs/2605.02298), Thm. 1.1 | Estudia la mejor aproximación de permutones por permutaciones finitas en discrepancia rectangular; obtiene `O(log^(3/2)n/n)` universal y cotas específicas | Es un resultado más fuerte en el eje de aproximación/discrepancia, pero no impone ni estudia una LIS anómala y no contiene geometría lorentziana | `CURRENT_DISCREPANCY_STATE_OF_ART / ORTHOGONAL_TO_F3` |
| [Dubach, arXiv:2301.07658v2](https://arxiv.org/abs/2301.07658) | Densidades con singularidades pueden producir LIS de orden `N^β`, `β>1/2`, salvo factores logarítmicos | Una densidad fija no uniforme/singular tiene sesgo macroscópico en algún rectángulo respecto de Lebesgue: discrepancia de cuentas `Theta(N)`, incompatible con F2. No es una sucesión triangular que se vuelva uniforme a la tasa de Madsen | `DIRECT_PRECURSOR_OF_LONG_CHAIN_MECHANISM / DOES_NOT_SUBSUME` |
| [Dubach, arXiv:2307.05768v2](https://arxiv.org/abs/2307.05768) | Define tableaux de Robinson–Schensted para permutones y obtiene LIS lineal cuando el tableau del permutón es no trivial | El fenómeno lineal procede de masa no nula sobre conjuntos crecientes del permutón límite, no de una perturbación de masa evanescente compatible con F2 respecto de Lebesgue | `LIS_PERMUTON_PRECURSOR / DOES_NOT_SUBSUME` |
| [Sjöstrand, arXiv:2207.11505v2](https://arxiv.org/abs/2207.11505) | Obtiene formas límite para subsecuencias monótonas de muestras iid de una densidad absolutamente continua fija | Modelo iid de densidad fija; no discrepancia determinista uniforme, no sucesión triangular F2 y no transferencia causal | `FIXED_DENSITY_LIS_BACKGROUND` |
| [Aghili–Bombelli–Pilgrim, arXiv:1805.07312](https://arxiv.org/abs/1805.07312) | Usa distribuciones de longitudes de cadenas maximales como diagnóstico de embebibilidad en `1+1` | Confirma que la información de cadenas es un observable separado, pero parte de sprinklings uniformes y no construye F2 sin F3 | `CHAIN_DIAGNOSTIC_PRECURSOR / DOES_NOT_SUBSUME` |
| [Braun, arXiv:2507.01907](https://arxiv.org/abs/2507.01907), Thm. 1.4 | Las leyes de las matrices de adyacencia para todo tamaño `k` reconstruyen suavemente el espaciotiempo: “order + number = geometry” en sentido probabilístico | Resultado de identificación exacta de leyes para **todo** `k`, no una garantía finita cuantitativa desde F2 ni una implicación hacia F3 | `ENSEMBLE_RECONSTRUCTION / DIFFERENT_QUANTIFIERS` |
| [Surya, arXiv:2510.19403](https://arxiv.org/abs/2510.19403) | Define funciones de cercanía por abundancias de intervalos y una convergencia débil de geometrías lorentzianas coarse-grained | Usa espectros de intervalos/valores esperados y declara que es más débil que una distancia lorentziana; no relaciona F2 con longest-chain distance | `COARSE_CLOSENESS_BACKGROUND` |

### 3.1 El antecedente causal negativo que no debe omitirse

Müller es bibliográficamente más cercano al mensaje físico que Dubach: demuestra que “orden +
uniformidad de cuentas” finitos no bastan, en general, para controlar una noción fuerte de distancia
lorentziana. Por ello debe citarse en cualquier nota.

No anticipa, sin embargo, el teorema congelado. Sus cuantificadores son `K` fijo y proximidad de
distribuciones de órdenes, su objeto de salida es una distancia entre espaciotiempos y su
construcción no contiene el certificado interno que aquí es decisivo:

```text
misma configuración + F1 exacta + F2 uniforme de Madsen
                    + cadena testigo que viola su F3 completa.
```

Que Madsen cite a Müller y aun así declare expresamente abierta F1–F2 versus F3 refuerza esta
distinción; no la sustituye por una prueba de prioridad.

### 3.2 El antecedente `1+1` que no debe omitirse

Saravani–Aslanbeigi es el precedente causal-set específico más cercano al lado F2. Ya en 2014
identifica retículos lorentzianos `1+1` con excelente correspondencia número–volumen para regiones
macroscópicas. Pero la evidencia publicada es una simulación sobre una muestra finita de diamantes,
incluidos diamantes estirados; no contiene una cota uniforme para todos los diamantes ni estudia la
escala de longest chain.

Por tanto, la afirmación novedosa defendible no es que una configuración no-Poisson pueda tener
buenas cuentas en `1+1`. Es que una configuración puede satisfacer **la tolerancia uniforme exacta
de F2 usada por Madsen** y, simultáneamente, violar **su F3 completa**.

### 3.3 El antecedente combinatorio que no debe omitirse

Dubach muestra que la uniformidad local informal no evita LIS grandes. Cooper y Maga muestran que
las permutaciones pueden aproximar muy bien la medida uniforme en discrepancia rectangular. Ninguna
de esas fuentes combina ambos ejes con la escala cuantitativa concreta de Madsen.

La novedad potencial reside, por tanto, en la compatibilidad demostrada entre:

```text
masa plantada suficientemente pequeña para F2
        +
cadena suficientemente larga para romper F3 por margen constante
        +
transferencia lorentziana regional con constantes uniformes.
```

No reside en haber inventado por separado discrepancia baja, retículos lorentzianos o LIS grandes.

## 4. Auditoría de actualidad de Madsen

- arXiv registra únicamente `v1`, enviada el 7 de julio de 2026.
- En la fecha de corte, INSPIRE registra una sola cita posterior:
  [Xu, arXiv:2607.26672](https://arxiv.org/abs/2607.26672).
- El contexto de esa cita dice que el trabajo cuantitativo de embedding conserva una condición
  separada de longest-chain/proper-time. No propone contraejemplo, no prueba F2⇒F3 y no contiene
  una adjudicación de la pregunta abierta.
- Las búsquedas exactas por título, por la notación F1–F3 y por la frase del problema no localizaron
  otra respuesta pública anterior a esta fecha.

Esto es evidencia útil de actualidad, no una garantía de que no exista un manuscrito no indexado o
un resultado conocido privadamente.

## 5. Resultado de la auditoría

```text
WP7_PRIMARY_NOVELTY_AUDIT =
    PRIMARY_SEARCH_PERFORMED
    / NOVELTY_NOT_REFUTED
    / NO_EQUIVALENT_PRIMARY_RESULT_FOUND
    / NOT_A_NOVELTY_CERTIFICATE
```

No se encontró una fuente primaria que pruebe, con cuantificadores equivalentes, la no-implicación
`F1+F2 not=> F3` de Madsen en `1+1` mediante una violación constante de su desigualdad completa.

El resultado sobrevive la auditoría con este techo de claim:

> **A nuestro leal saber y entender, tras revisar los precedentes causales, de discrepancia y de
> longest increasing subsequences indicados arriba, esta construcción da el primer contraejemplo
> publicado/propuesto a la implicación F1–F2⇒F3 bajo la lectura regional declarada de Madsen en
> dimensión `1+1`.**

Para una primera versión pública es más seguro evitar incluso “primero” y escribir:

> **We answer negatively the question left open in Madsen's Remark/footnote: under the stated
> regional interpretation in `1+1` dimensions, F1 and F2 do not imply F3.**

Debe añadirse inmediatamente que:

- el resultado es una **no-implicación**, no “independencia lógica” sin matiz;
- no demuestra que F3 sea necesaria para toda posible prueba de unicidad;
- no refuta el teorema de Madsen, sino que muestra que F3 no es redundante respecto de F1–F2 en
  este régimen;
- Müller, Saravani–Aslanbeigi, Cooper, Maga y Dubach son antecedentes obligatorios y delimitan qué
  parte de la combinación puede aspirar a novedad.

## 6. Limitaciones y siguiente gate

Esta revisión es fuerte pero no sistemática en sentido PRISMA y no consulta MathSciNet, zbMATH,
Scopus o Web of Science con acceso institucional. Tampoco puede detectar manuscritos privados,
tesis no indexadas o resultados comunicados informalmente. La ausencia de un hit no certifica
prioridad.

Antes de una afirmación pública de “first known”, el siguiente gate recomendable es una lectura
externa breve por dos perfiles independientes:

1. causal set theory/Hauptvermutung, con atención especial a Müller y retículos lorentzianos;
2. permutones/LIS/discrepancia, con atención especial a si la combinación cuantitativa aparece
   bajo otra terminología.

Hasta ese gate, la formulación defendible es el resultado matemático directo sin claim de prioridad.
