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
