# Auditoría de prioridad (provisional): manuscrito §3.5, caja EF fija

```text
FECHA: 2026-10-16
AUDITOR: Claude (Opus 5.5), autor de §3.5; no es independiente
ALCANCE: búsqueda limitada (índice local y alphaXiv); no exhaustiva
VEREDICTO: NO_OVERLAP_FOUND_IN_LIMITED_SEARCH — PROVISIONAL
```

## 1. Afirmaciones auditadas

| # | Afirmación de §3.5 | Riesgo de prioridad |
|---|---|---|
| A | El canal de orden (permutación o poset) de una familia con soporte móvil es regular y uniforme en \(n\) (Lema 3.11 y Teorema 3.12) | Medio: puede existir en estadística de rangos con otra forma |
| B | Tasa minimax \(n^{-1/2}\) para estimar \(\tau\) solo con el orden en la caja EF (Teoremas 3.13 y 3.15) | Bajo-medio: la literatura de causets sobre estimación no da tasas para \(M\) en una caja fija |
| C | Monotonía de la relación en \(M\) por comparación de conos (Lema 3.14 y M1) | Alto como técnica (es estándar); bajo como aplicación |
| D | Estimador: fracción de pares relacionados | Ya reconocido como clásico (Myrheim–Meyer) en el manuscrito (§3.3, línea de \(\widehat p_n\)) |

## 2. Búsquedas hechas

- `biblioteca/INDICE.md` (grep: estimat, minimax, fisher, statistic, rank, copula,
  permut, mass, curvature, identif). Lo pertinente ya está citado en el manuscrito:
  Bombelli, *Statistical Lorentzian geometry* (gr-qc/0002053); Braun, arXiv:2507.01907;
  Benincasa–Dowker. También hay `Tsybakov` y *Minimax distinguishability*, que son
  maquinaria estándar. Auditorías previas del repo: `No-Go De Identificabilidad Local.md`
  y `Auditoria Retencion Fisher.md`.
- alphaXiv, tres búsquedas:
  1. Estimación de parámetros (masa, curvatura, horizonte) a partir del orden de un
     causet, con tasas o información de Fisher. Resultados: 2407.03395 (fluctuaciones de
     la acción), 2007.03835 (cadenas para curvatura y dimensión) y otros sin tasas
     minimax. **Sin solapamiento con B.**
  2. Estadísticos de rangos en familias no regulares con soporte dependiente del
     parámetro. Resultados: 2607.10435 (comparación de información de estadísticos de
     orden), 2605.13710 (tests de patrones para cópulas), 2111.00559 (canales de
     permutación). **Sin solapamiento con A.**
  3. Experimentos de rangos con soporte móvil e invariante maximal. Leído 2606.25790
     (Nielsen y Okamura, invariancia de f-divergencias bajo grupos): es el marco
     general de reducción por invariante maximal (Eaton, Wijsman). **Es contexto, no
     un antecedente de A.**

## 3. Lectura

- **A** es, en forma, una reducción por invariante maximal: los rangos son el
  invariante maximal bajo transformaciones monótonas coordenada a coordenada (clásico).
  Lo específico es que el representante \((\varepsilon,D,v)\) tiene soporte fijo y
  densidad suave, aunque la ley de un punto no la tenga. No se ha encontrado un
  enunciado previo de "el canal de rangos regulariza una familia de soporte móvil",
  pero la búsqueda no cubre la literatura clásica de tests de rangos (Hájek–Šidák,
  Lehmann). [UNVERIFIED]
- **C**: la comparación de conos (\(g_1\le g_2\) implica \(J^+_1\subseteq J^+_2\)) es
  estándar en teoría de la causalidad (Hawking–Ellis; Minguzzi–Sánchez, *The causal
  hierarchy of spacetimes*). Hay que citarla, no reclamarla. Ninguna de esas fuentes
  está en `biblioteca/`; la cita queda [UNVERIFIED] hasta leerla.

## 4. Redacción recomendada para el manuscrito

- No usar "nuevo" ni "primero" para A, B o C. El manuscrito actual no lo hace (el
  abstract dice "A horizon-side reparametrization nevertheless writes…").
- En §3.5, añadir una frase: "The representation is an instance of reduction to a
  maximal invariant (ranks under coordinatewise monotone maps); what is specific
  here is that the representative has fixed support."
- Para el Lema 3.14 y para M1 (si entra 3+1D), citar la comparación de conos como
  estándar.

## 5. Pendiente antes de enviar

1. Leer Hájek–Šidák (*Theory of Rank Tests*) y Lehmann (*Testing Statistical
   Hypotheses*, capítulo de invariancia), buscando experimentos de rangos con soporte
   móvil.
2. Leer y citar una fuente primaria de la comparación de conos.
3. Hacer una búsqueda con evidencia por otra vía: `investigacion-gemini`, cuando haya
   créditos, o `sanedrin --hibrido`. Las dos envían texto a terceros: requieren
   permiso del PI.
4. Pedir la opinión de una persona experta en estadística de rangos o en causets.

## 6. Fuentes conseguidas (2026-10-16, arXiv, acceso legal)

- `biblioteca/Minguzzi_Sanchez_2008_Causal_Hierarchy_arXiv_gr-qc0609119v3.pdf`
  (identificador verificado en la API de arXiv). §3.8, p. 36: "A partial (strict)
  ordering < is defined in Lor(M): g < g′ if and only if all the causal vectors for g
  are timelike for g′." Ya se usa en p. 9 (Lema 2.13). Nuestro caso
  \(g_{M'}-g_M=2(M'-M)\dot v^2/r\ge0\) es la **versión no estricta**, porque \(-\partial_r\)
  es nulo para todo \(M\). Los futuros causales anidados se siguen directamente. Es la cita
  para el Lema 3.14 y para M1.
- `biblioteca/Bleybel_2024_Conformal_Group_Globally_Hyperbolic_arXiv2407.12946.pdf`.
  p. 1: en dimensión > 2, los automorfismos causales de Minkowski son Lorentz
  ortócronas, traslaciones y dilataciones (**Zeeman**). En una variedad lorentziana
  general de dimensión > 2, todo automorfismo causal que distinga pasado y futuro es
  conforme (**Levichev**). En 2D aparecen grandes grupos de reparametrización (Kim; el
  propio Bleybel). **Corrección:** la rigidez de 3+1D que se usa en
  `puente_3p1/2026-10-16/` y en la prueba 3 de CREATE se había atribuido a "Malament";
  corresponde a Zeeman y Levichev. Las fuentes primarias (Zeeman 1964, Levichev) no
  están descargadas.

No conseguidos (con derechos de autor, sin copia abierta legal): Hájek–Šidák, *Theory
of Rank Tests*; Lehmann–Romano, *Testing Statistical Hypotheses*. Hay que obtenerlos
por una biblioteca o comprándolos. Sustituto parcial buscado en arXiv (experimentos de
rangos con soporte móvil): sin resultados que se solapen.

**Catálogo.** `biblioteca/INDICE.md` se genera desde `scripts/biblioteca_catalog/curated.csv`,
que solo existe en la rama `research/causal-fidelity-bridge`, no en `main`. No se ha
regenerado el índice, para no perder las etiquetas curadas. Los dos PDFs nuevos están en
`biblioteca/` pero todavía no en el índice.

## 7. Libros aportados por el PI (2026-10-16)

- `biblioteca/Testing-statistical-hypotheses.epub`: Lehmann–Romano, 4.ª ed. Leído por
  búsqueda de texto en la conversión del EPUB (el EPUB no tiene páginas fijas; se cita
  por sección o ejemplo).
  - §6.8, *Rank Tests*: "Any invariant test is thus a rank test, that is, it depends only
    on the ranks of the observations". Los rangos son el invariante maximal bajo
    transformaciones monótonas. Es la cita para la frase de reducción por invariante
    maximal de la §3.5.
  - Ejemplo 14.2.8 (*Uniform Family*): la familia uniforme no es QMD, porque
    \(n\int[p_{\theta_0}^{1/2}-p_{\theta_0+hn^{-1/2}}^{1/2}]^2\to\infty\). A continuación:
    "it is quite typical that families whose support depends on unknown parameters will
    not be q.m.d., though Example 14.2.7 is an exception". Es la cita para la
    Observación 3.4 (la ley de un punto en la caja EF no es QMD).
  - Ningún pasaje del libro trata que el experimento de rangos de una familia con soporte
    móvil sea regular. Búsquedas: "maximal invariant" (24 apariciones), "rank test" (14),
    "quadratic mean" (25), dependencia del soporte (1, la del Ejemplo 14.2.8), "local
    asymptotic normality" (3). **No se encuentra antecedente de A en Lehmann–Romano.**
- `biblioteca/the-asymptotic-theory-of-extreme-order-statistics.pdf`: **es Galambos**,
  *The Asymptotic Theory of Extreme Order Statistics*, 2.ª ed., no Hájek–Šidák como dice
  `Libros.txt`. Sirve para el lado de la frontera (tasa \(1/n\) de los extremos). No cubre
  los tests de rangos. **Hájek–Šidák sigue sin estar disponible.**

Veredicto actualizado: NO_OVERLAP_FOUND (biblioteca, alphaXiv y Lehmann–Romano) —
PROVISIONAL mientras no se consulte Hájek–Šidák ni a una persona experta.
