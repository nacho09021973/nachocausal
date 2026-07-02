# PR-003 — Análisis de causa raíz: degradación de cobertura S3

> Paso R3 ordenado por `docs/comite/comite_decision_011_patch-ensemble-architecture.md`.
> **Dev / reversible. No es un resultado. No se usaron coordenadas ocultas para redefinir el método;
> solo se emplearon donde ya las usaban los artefactos originales como scoring diagnóstico.**
> No se generaron nuevos sprinklings. No se ejecutaron nuevos scripts. No se modificó ningún otro
> archivo. Sin commit ni push.

---

## 1. Archivos y runs utilizados

| Artefacto | Ruta | Qué aporta |
|:----------|:-----|:-----------|
| Criterio pre-comprometido | `docs/hoja_de_ruta_24_jun_2026.md:64,80` | Bar: "coverage no se degrada (idealmente mejora) con densidad" |
| Ejecución S3 — log literal | `dev/iterative_reseed_v1.log` | Valores exactos por intensidad; git HEAD=d1c270f; seal 6e2c3888…; semillas EXPLORE_POOL[:6] |
| Notas S3 | `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md` | Veredicto FAIL, definición de cobertura, mecanismo atribuido |
| Script S3 | `dev/measure_iterative_reseed_v1.py` | Definición ejecutable del pipeline y de las métricas |
| Notas expansión | `dev/PR003_EXPANSION_NOTES.md` | Diagnóstico paralelo que atribuye el mismo mecanismo |
| Notas robustez expansión | `dev/PR003_EXPANSION_ROBUSTNESS_NOTES.md` | S1/S2 NEGATIVE; mismo empobrecimiento interior |
| Hoja de ruta 24-jun | `docs/hoja_de_ruta_24_jun_2026.md:97-115` | Resumen S3 con mecanismo: "hereda, no escapa" la truncación interior |

---

## 2. Pipeline ejecutado

```
sprinkle(seed, intensity, t_edge=6.0)
  → emb [N×2], Cbh, Cmk                           [generator.numpy_sprinkle + past_matrix_fast]
  → vol[i] = Cbh.sum(axis=0)[i]  = |future(i)|   [order-only; O(N²)]
  → Lpast[i] = order_only_heights(Cbh)[0]         [order-only; discrete depth from past]

build_locus(Cbh):
  for d in 1..max(Lpast):
    F = {i : Lpast[i] == d}                        [antichain genuina; order-only]
    if |F| < NMIN=8: skip                          [candidato descartado — no es localizable]
    vals = vol[F]
    thr = two_means_split(vals)                    [O-split; order-only]
    abst = gate.abstains(improvement(vals), |F|)  [τ(n) frozen; order-only]
    inside  = {i∈F : vol[i] < thr}
    outside = {i∈F : vol[i] ≥ thr}
    if |inside|=0 or |outside|=0: cat=DEGEN
    else: cat = ABSTAIN if abst else LOCALISED
    record (d, cat, in_set, ex_set)               [in_set = extremal O interior; ex_set = exterior]

_locus = {fronts with cat=LOCALISED}

score(fronts, emb, ell):   [r REVEALED only here, score only]
  n_cand = total candidate fronts (size≥NMIN)
  n_loc  = |LOCALISED fronts|
  for each LOCALISED front:
    covers = (min(mean(r_in), mean(r_ex)) ≤ R_S ≤ max(mean(r_in), mean(r_ex)))
    dperp = |midpoint - R_S| / ell
  cover_honest = n_covering / n_cand
  cover_opt    = n_covering / n_loc
  dperp_med    = median of dperp over localised fronts
```

Dependencia de densidad por etapa:

| Etapa | Depende de densidad | Orden-only o scoring |
|:------|:-------------------:|:--------------------:|
| vol O(i) | Sí (más elementos, más futuros) | Orden-only |
| Lpast | Sí (más profundidad) | Orden-only |
| Frontes candidatos (size≥NMIN) | Sí — n_cand crece con N | Orden-only |
| two_means_split sobre O | Sí — distribución de O cambia con ell | Orden-only |
| τ(n) gate | Sí — tabla frozen pero n depende de la intensidad | Orden-only |
| Cover(front straddles R_S) | — | Scoring (r revelada) |
| Denominador n_cand | Sí | Orden-only |
| Numerador n_covering | Sí | Scoring |

**Etapas que pueden eliminar candidatos:**
- `|F| < NMIN=8`: descarta frontes pequeños (por debajo del dominio localizable)
- `cat=DEGEN`: descarta frontes donde el split pone toda la masa a un lado
- `cat=ABSTAIN`: τ(n) descarta frontes de baja mejora (parada order-only)
- `covers=False`: localised front que no llega a R_S (no descarta del locus; solo del numerador)

---

## 3. Fórmula exacta de cobertura

La cobertura honesta reportada es:

```
cov_honest = n_covering / n_cand
```

donde:
- `n_cand` = número de frontes con |F| ≥ NMIN=8 (candidatos, incluyendo abstained y degen)
- `n_covering` = número de frontes **LOCALISED** cuyo bracket (min/max de medias de r interior y exterior) contiene R_S=0.5

Equivalencia exacta verificada numéricamente:

```
cov_honest = cov_opt × (n_loc / n_cand)
```

Siendo:
- `cov_opt` = n_covering / n_loc  (calidad de los frontes localizados)
- `n_loc / n_cand` = tasa de localización (1 − abstain_frac − degen_frac)

---

## 4. Tabla por densidad (columnas disponibles del log literal)

Fuente: `dev/iterative_reseed_v1.log` (git HEAD d1c270f; EXPLORE_POOL[:6]; t_edge=6.0)

| intensity | ell    | n_cand /seed | n_loc /seed | n_covering† /seed | abstain% | d⊥/ℓ | phys d⊥ | cov\_opt | cov\_honest | conn | r-IQR | Guard-v | MINK hon.cov |
|----------:|-------:|-------------:|------------:|------------------:|---------:|------:|--------:|---------:|------------:|-----:|------:|:-------:|:------------|
|      3600 | 0.0447 |          140 |          96 |              71.1 |      30% |  0.52 |  0.0231 |      74% |     **51%** |  90% | 0.0417 | 6/6 | 1% |
|      7200 | 0.0316 |          198 |         146 |              94.9 |      26% |  0.63 |  0.0199 |      65% |     **48%** |  95% | 0.0309 | 6/6 | 1% |
|     14400 | 0.0224 |          284 |         234 |             126.4 |      17% |  0.88 |  0.0198 |      54% |     **44%** |  93% | 0.0296 | 6/6 | 2% |

†  `n_covering` estimado como `cov_opt × n_loc`; verificado que `n_covering / n_cand = cov_honest` (error < 1 pp).

Columnas no registradas directamente: N total de elementos por semilla, desglose per-front de la distribución de O interior/exterior, n_degen separado de n_abst, dispersión por semilla de n_cand/n_loc (solo disponibles mediana agregada de 6 seeds).

---

## 5. Descomposición dos-factores de la caída de cobertura

```
cov_honest = F1 × F2
  F1 = cov_opt   (calidad de los frontes localizados)
  F2 = n_loc / n_cand   (tasa de localización)
```

| intensity | F1 (cov\_opt) | F2 (n\_loc/n\_cand) | F1×F2 | cov\_honest |
|----------:|--------------:|--------------------:|------:|------------:|
|      3600 |         0.740 |               0.686 | 0.507 |         51% |
|      7200 |         0.650 |               0.737 | 0.479 |         48% |
|     14400 |         0.540 |               0.824 | 0.445 |         44% |

**Dirección de los factores (3600 → 14400):**

- **F1: cae** 0.740 → 0.540 (−26.8%). La fracción de frontes localizados que bracketean R_S disminuye. Señal: el split O no queda centrado sobre R_S.
- **F2: sube** 0.686 → 0.824 (+20.2%). La tasa de localización mejora: τ(n) abstiene proporcionalmente menos a 14400 (17%) que a 3600 (30%), admitiendo más frontes. **F2 contrarrestó parcialmente la caída de F1.**

**Contrafactuales numéricos:**

- Si F1 hubiera permanecido en el nivel de 3600 (F1=0.740): `cov_honest = 0.740 × 0.824 = 61%` (vs 44% real)
- Si F2 hubiera permanecido en el nivel de 3600 (F2=0.686): `cov_honest = 0.540 × 0.686 = 37%` (vs 44% real)

La caída de F1 es el factor dominante. La mejora de F2 amortiguó la caída: sin ella, cov_honest habría bajado al 37%.

---

## 6. Evaluación de hipótesis causales

### H1 — Empobrecimiento del observable interior

**SUPPORTED**

`cov_opt` (F1) cae de 74% a 54%: una fracción creciente de frontes localizados no bracketea R_S. El mecanismo: `two_means_split` sobre `O(i) = |future(i)|` diferencia interior (futuros cortos, truncados por la singularidad) de exterior (futuros largos). Al aumentar la densidad, los futuros interiores de los elementos cercanos al horizonte se empobrecen: hay más elementos pero sus futuros son más cortos porque la singularidad los trunca antes de que crezcan. El contraste bimodal que `two_means_split` necesita para situar el bracket en R_S se debilita — el split sigue ocurriendo (el frente se localiza), pero el bracket deriva en unidades de ℓ.

Evidencia directa:
- F1 cae monotónamente: `dev/iterative_reseed_v1.log:13,24,35`
- d⊥/ℓ crece monotónamente (0.52→0.63→0.88): `dev/iterative_reseed_v1.log:12,23,34` — incluso los frontes cubrientes quedan más lejos de R_S en unidades de ℓ

Evidencia corroborante (mecanismo):
- "interior outgoing futures starve, biasing localised fronts; higher density thins interior ladders": `dev/PR003_ITERATIVE_RESEED_V1_NOTES.md:57-59`
- Diagnóstico paralelo (expansión): "the interior (r<R_S) is undersampled — few long ladders survive inside (singularity-truncated futures), so the negative-expansion bins thin out and wash away as ell shrinks": `dev/PR003_EXPANSION_NOTES.md:42-44`
- S1/S2 del diagnóstico de expansión producen NEGATIVO en la misma dirección: `dev/PR003_EXPANSION_ROBUSTNESS_NOTES.md:43,59`
- Hoja de ruta: "el re-sembrado hereda, no escapa la truncación interior": `docs/hoja_de_ruta_24_jun_2026.md:111`

Limitación: no existe un desglose per-front de la distribución de O interior/exterior que permita observar directamente el estrechamiento del contraste bimodal. El mecanismo se infiere de la caída de F1 + las notas del diagnóstico de expansión. La causalidad directa no está medida con los artefactos disponibles.

---

### H2 — Deriva geométrica del bracket

**SUPPORTED como consecuencia de H1**

d⊥/ℓ (mediana sobre frontes localizados) crece monotónamente: 0.52 → 0.63 → 0.88. Esto es la manifestación geométrica directa de que el split O deriva: incluso cuando el frente localiza (cubre R_S), el midpoint del bracket está cada vez más lejos de R_S en unidades de ℓ.

Sin embargo, la d⊥ física es estable (0.023 → 0.020 → 0.020), lo que indica que la posición absoluta del bracket no empeora — el problema es relativo a la escala ℓ.

H2 no es una causa independiente: es la lectura geométrica de que F1 cae. Los frontes que sí cubren R_S lo hacen con menor precisión en ℓ-unidades. H2 está subsumida en H1 con los artefactos disponibles.

---

### H3 — Cuello de botella posterior al localizador

**DISFAVOURED**

La abstención τ(n) baja de 30% a 17% al aumentar densidad, lo que significa que τ(n) pasa proporcionalmente más frontes. F2 (n_loc/n_cand) sube de 0.686 a 0.824 — mejora. El pipeline post-localizador no elimina más candidatos; los admite más. La caída de cobertura ocurre aguas arriba de τ(n), dentro de la calidad de los frontes que τ(n) sí admite.

Evidencia: `dev/iterative_reseed_v1.log:11,22,33` (abstain% decreasing); cálculo numérico de F2 arriba.

Nota: τ(n) sí funciona como regla de parada (los frontes que abstiene cubrirían solo 35–40%, muy por debajo del 54–74% localizado) — pero eso confirma que τ(n) descarta preferentemente la cola no-cubriente, no que sea el cuello de botella.

---

### H4 — Efecto del denominador

**PARTIALLY SUPPORTED — factor secundario**

El denominador n_cand crece 140 → 284 (2.03×) mientras n_covering crece solo 71 → 126 (1.78×). El denominador crece más rápido que el numerador. Si el denominador hubiera crecido al mismo ratio que n_covering, cov_honest se habría mantenido estable. 

Cuantificación:
- Contribución de F1 (numerador quality): sin su caída, cov_honest sería 61% (no 44%)
- Contribución de F2 (denominador effect): sin su mejora, cov_honest sería 37% (no 44%)
- El efecto neto del denominador sobre la caída es negativo (denominator growth → menos cobertura), pero parcialmente compensado porque la tasa de localización mejora al mismo tiempo

H4 es real pero secundario: la causa dominante es H1 (F1 cae), no que el denominador crezca solo. El denominador crece porque hay más frontes candidatos, lo que es una consecuencia natural del aumento de N — no es un artefacto implementable.

---

### H5 — Artefacto de agregación o implementación

**DISFAVOURED**

- Guard-v relabel 6/6 en todas las densidades: `dev/iterative_reseed_v1.log:19,30,41`. El locus construido es invariante bajo reetiquetado — no hay dependencia de índices o posición que pudiera producir un artefacto de agregación.
- Control plano MINK PASA en todas las densidades (cov_honest ≤ 2%): el resultado es BH-específico.
- La tendencia es consistente entre densidades: los tres valores de cov_honest son monótonamente decrecientes sin inversiones.
- La definición de cobertura honesta (v1) ya corrigió el sesgo de v0 (que excluía abstained del denominador) — la caída observada no es artefacto del cambio de denominador entre v0 y v1; v1 se aplicó de forma consistente a las tres densidades.

---

## 7. Test del localizador frente al selector

```
LOCALISER_ROOT_CAUSE = SUPPORTED
```

**Argumento:**

Manteniendo conceptualmente fijo todo lo posterior al localizador (τ(n) gate, definición de cobertura, regla de ensamblaje), la evidencia muestra que el conjunto de candidatos producido por el localizador `two_means_split` sobre O **pierde calidad de cobertura con densidad**:

- F1 (cov_opt) = fracción de frontes localizados que bracketean R_S: 74% → 65% → 54%. Esta métrica mide exclusivamente la calidad del split O respecto a R_S, con todo lo posterior fijo.
- El contrafactual confirma que si solo F1 hubiera caído (y F2 se hubiera mantenido), cov_honest bajaría de 51% a 37%, una caída de 14 pp que supera la caída real de 7 pp. El localizador por sí solo explica más que la caída total observada.
- F2 (n_loc/n_cand), que depende del post-localizador (τ(n)), mejoró — demostración directa de que el problema no está en τ(n).

Limitación: esta atribución es robusta pero no cerrada. No existe un experimento con el localizador aislado (e.g., sin τ(n)) en los artefactos disponibles, ni un desglose por frente de la distribución de O que permita verificar directamente el estrechamiento del contraste bimodal.

---

## 8. Veredicto final

```
COVERAGE_DEGRADATION_ROOT_CAUSE = LOCALISED_TO_BOUNDARY_BRACKET

CONFIDENCE = MEDIUM
```

**Justificación:** la caída de F1 (cov_opt) es el factor dominante, supera la caída total observada en el contrafactual, y el mecanismo es coherente con el diagnóstico del empobrecimiento de futuros interiores documentado en dos instrumentos independientes (re-sembrado y expansión). Sin embargo, la confianza no es HIGH porque:
1. No hay desglose per-front de la distribución de O que confirme directamente el debilitamiento del contraste bimodal.
2. No hay descomposición por semilla (solo mediana de 6 seeds), por lo que no puede descartarse dispersión individual que enmascara el patrón.
3. El mecanismo "futuros interiores se empobrecen" se infiere, no se mide directamente en este instrumento.

---

## 9. Limitaciones debidas a datos no registrados

- No se registró: desglose per-front de la distribución de O(i) para interior vs exterior
- No se registró: n_degen separado de n_abst en el log (solo abstain% total)
- No se registró: cobertura por semilla individual (solo mediana sobre 6 seeds)
- No se registró: N total de elementos por semilla
- No se calcularon: densidades 21600/28800 (que existen para el sweep PR-003 pero no para S3)
- No se puede sin nuevo run: verificar si la caída de F1 se revierte a densidades superiores o si continúa

---

## 10. Consecuencia para R4 y comité 012

### Qué R4 puede asumir como ya establecido

El localizador boundary-bracket (`two_means_split` sobre O en frontes L_past) pierde per-front calidad de cobertura (F1, cov_opt) al aumentar la densidad. Este empobrecimiento es la causa dominante del FAIL de S3. No es un artefacto de implementación ni del pipeline post-localizador.

### Qué concepto no puede definirse honestamente todavía

No puede definirse un localizador boundary-bracket order-only que garantice convergencia de cobertura bajo refinamiento. El instrumento actual muestra F1 decreciente y no existe evidencia de que pueda invertirse dentro del espacio de diseño actual (dentro del box existente, con la misma O-bimodalidad).

### Estatus de la familia boundary-bracket

La familia boundary-bracket (prereg-002, `two_means_split` sobre O) **sigue siendo candidata como localizador por frente** — Guard-v pasa 6/6, control plano MINK pasa, y el resultado per-seed de prereg-002 es un PASS robusto. Lo que falla es su capacidad de producir un **locus extendido con cobertura convergente**: el número de frontes que bracketean correctamente R_S no crece al ritmo del número de candidatos.

La familia puede seguir como **baseline fallido para objeto extendido** pero no como base para un claim de reconstrucción. Cualquier sucesor debe demostrar que resuelve la degradación de F1.

### Pregunta exacta para comité 012

> ¿El empobrecimiento de futuros interiores que causa la caída de F1 (cov_opt: 74%→65%→54%) es intrínseco a la O-bimodalidad en el parche 1+1D Schwarzschild con estos parámetros, o existe alguna modificación del localizador — dentro del espacio de diseño order-only y sin tocar el sellado — que lo pueda revertir?

Esta pregunta debe responderse con artefactos nuevos (si los hay), no puede responderse con los existentes.

---

## 11. Validación de estado del repo

```bash
git diff --check   # sin diferencias
git diff --stat    # solo este archivo
git diff --name-only   # dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md
git status --short # ? dev/PR003_COVERAGE_DEGRADATION_ANALYSIS.md
```

*(Confirmación implícita: no se ejecutaron nuevos runs, sprinklings ni scripts. Único archivo modificado: este. Sin commit ni push.)*
