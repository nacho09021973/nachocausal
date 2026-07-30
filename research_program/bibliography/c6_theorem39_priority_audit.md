# C6 / Teoremas 3.9–3.10 — auditoría de prioridad (registro parcial)

> **STATUS: PRIORITY_AUDIT_IN_PROGRESS / SCOPED_SEARCH_ROUND_1_COMPLETE /
> NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH / PRIORITY_NOT_YET_CERTIFIED /
> NOT_A_NOVELTY_CERTIFICATE / NO_MANUSCRIPT_CHANGE / NO_CODE / NO_SIMULATION /
> NO_PR.**
>
> Registra la primera ronda de lectura primaria del punto de reentrada fijado en
> `docs/hoja_de_ruta_30_jul_2026.md` §1–§9. No cierra ningún gate de §5 de esa
> hoja de ruta. Es el acta de evidencia que `/auditor` debe usar como punto de
> partida, no una adjudicación.

FECHA: 2026-07-30

RAMA: `agent/phase3-b2-decision-048`

HEAD al registrar este acta: `c1a14a4074116590710f012035f75b922e8addc3`

## 1. Pregunta exacta pendiente de adjudicación

> ¿La combinación concreta de la expansión Schwarzschild con \(\kappa(r_p,r_q)\)
> en forma cerrada y la monotonía uniforme en \(\tau\) (Teorema 3.9, componentes
> T39-B/C) constituye una especialización publicable no anticipada, pese al
> antecedente técnico de Roy–Sinha–Surya (2013) y al coto bibliográfico de
> grafos geométricos/modelos latentes que sigue abierto?

### Veredicto provisional de esta ronda

```text
ROUND_1_SEARCH = EXECUTED_TARGETED_PRIMARY_READ
T39-A = TECHNICAL_BACKGROUND (Janson 2011; Reid 2004 / McGough 2021)
T39-B = PRECURSOR_ONLY_AT_TECHNIQUE_LEVEL / NO_EXACT_INSTANTIATION_SINK_FOUND
T39-C = NO_MATCH_AFTER_FULL_READ
T39-D = DISCHARGED_BY_WP4_AUDIT (no novedad; ver
        wp4_dimension_free_order_statistic_priority_audit.md)
T39-E = TECHNICAL_BACKGROUND (anclas V9 / Fase 2)

NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH = YES
PRIORITY_CERTIFIED = NO
RESIDUAL_GAP_DECLARED = random_geometric_graphs / latent_space_models
                        (heredado sin cerrar de phase2_novelty_and_item5.md §2.4)
```

`NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH` describe el resultado del barrido
descrito en §3, no una prueba de ausencia en la literatura. No certifica
novedad de T39-B/C; certifica únicamente que, tras esta ronda, la instanciación
geométrica concreta no tiene un sumidero localizado, a diferencia de T39-D
(discharged como corolario estándar en la auditoría del lema WP4).

## 2. Descomposición T39-A–E (heredada de la hoja de ruta §2)

| ID | Componente | Techo inicial | Veredicto tras Ronda 1 |
|---|---|---|---|
| **T39-A** | \(p(\tau)\) como funcional order-only / fracción de comparabilidad | Maquinaria y observable con precedentes esperables | `TECHNICAL_BACKGROUND` |
| **T39-B** | Expansión \(p(\tau)=1/2+\kappa\tau\,dv+O(dv^2)\) con control \(C^1\) uniforme | Posible aporte específico de la familia | `PRECURSOR_ONLY` (técnica); sin sumidero exacto |
| **T39-C** | Monotonía uniforme y separación Lipschitz para \(0<dv<dv_0\) | Corolario geométrico específico | `NO_MATCH_AFTER_FULL_READ` |
| **T39-D** | Cota inferior de TV mediante \(S_n\), momentos exactos y Chebyshev | Aplicación de estadística estándar al canal `fixed_n` | `DISCHARGED` — caso \(m=2\) del lema WP4 ya auditado |
| **T39-E** | Frontera \(o(n^{-1/2})/\omega(n^{-1/2})\) al combinar 3.8 y 3.9 | Posible síntesis específica; constantes no cerradas | `TECHNICAL_BACKGROUND` |

Relaciones usadas:

```text
SUBSUMES
DIRECT_PRECURSOR
TECHNICAL_BACKGROUND
ANALOGUE_OTHER_MODEL
ORTHOGONAL
NO_MATCH_AFTER_FULL_READ
```

## 3. Método y límites de la búsqueda (Ronda 1)

Lectura primaria dirigida sobre:

1. Candidatos locales en `biblioteca/derived-md/` identificados por grep de
   términos (`Myrheim`, `ordering fraction`, `comparable pair`) como
   potencialmente relevantes al coto 3.1 de la hoja de ruta (causal sets y
   orden fraccionario).
2. Dos búsquedas externas dirigidas (`WebSearch`) para verificar una fecha
   sospechosa y perseguir dos leads que aparecieron en esa verificación.

Límites vinculantes (iguales en espíritu a los de la auditoría WP4 y a los de
Fase 2):

- no es una revisión sistemática ni exhaustiva de citas;
- no se consultaron MathSciNet, zbMATH, Scopus o Web of Science con acceso de
  suscripción;
- el coto 3.4 de la hoja de ruta (grafos geométricos aleatorios / modelos de
  espacio latente), ya señalado como residual por el lector Tier B de Fase 2
  para el Teorema 3.8, **no se persiguió en esta ronda** — ver §6;
- `NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH` no equivale a
  `NOVELTY_CERTIFIED`.

## 4. Fuentes primarias leídas y veredicto por fuente

### 4.1 Hoeffding (1963) y Janson (2011) — ya discharged vía WP4

Ambos ya fueron leídos a fuente primaria en
`wp4_dimension_free_order_statistic_priority_audit.md` §4.1–4.2. Cubren
íntegramente T39-D (Chebyshev/TV vía \(S_n\) es el caso \(m=2\) del lema
general ya auditado) y aportan `TECHNICAL_BACKGROUND` para T39-A (marco de
posets no etiquetados de Janson). No se releyeron en esta ronda; se referencian
por número de sección.

### 4.2 Reid (2004) — estimador de dimensión Myrheim-Meyer en espaciotiempos curvos

D. D. Reid, "The Manifold Dimension of a Causal Set: tests in conformally flat
spacetimes", *Phys. Rev. D* **67**, 024034 (2003),
[arXiv:gr-qc/0207103](https://arxiv.org/abs/gr-qc/0207103).

Usa \(f(d)=\langle S_2\rangle/\langle N\rangle^2\) (fracción de orden) para
estimar la dimensión, pero la extensión a espaciotiempos curvos es puramente
**numérica**: compara, vía test \(\chi^2\), el comportamiento de subintervalos
pequeños contra sprinklings de Minkowski en 2, 3 y 4 dimensiones. No hay
expansión analítica de \(f\) en un parámetro de curvatura, ni monotonía
demostrada en un parámetro de familia.

**Relación:** `TECHNICAL_BACKGROUND DFO-A/T39-A` (uso CST de la fracción de
orden como observable). `NO_MATCH T39-B/C` (sin expansión analítica ni
monotonía).

### 4.3 McGough / Bhandari (2021, honors thesis)

S. Bhandari (McGough), "Exploring Manifoldlike Causal Sets and their
Dimensions", Honors Thesis, Univ. of Mississippi (2021).

Aplica numéricamente el estimador Myrheim-Meyer y discute expansión RNC citando
directamente a Roy–Sinha–Surya (su referencia [6], ver §4.4) y a Reid (su
referencia [7]). No añade instanciación nueva sobre sus fuentes.

**Relación:** `TECHNICAL_BACKGROUND`, redundante con 4.2 y 4.4.

### 4.4 Roy, Sinha, Surya — expansión RNC de la fracción de orden (hallazgo central)

M. Roy, D. Sinha, S. Surya, "The Discrete Geometry of a Small Causal Diamond",
*Phys. Rev. D* **87**, 044046 (2013),
[arXiv:1212.0631](https://arxiv.org/abs/1212.0631).

**Corrección documental:** el derived-md local
(`biblioteca/derived-md/Discrete geometry of a small causal diamond.md`) trae
en su cabecera la fecha "March 21, 2024", que es un artefacto de OCR/metadata
del pipeline `marker-pdf`, no la fecha real de publicación. Verificado por
búsqueda externa (WebSearch, 2026-07-30): el paper es de 2012/2013
(arXiv:1212.0631, *Phys. Rev. D* 87, 044046, 21 feb. 2013). Esta corrección
debe registrarse si el documento se cita en el futuro.

**Contenido relevante.** Vía coordenadas normales de Riemann (RNC) alrededor de
un punto, derivan la expansión a primer orden en el parámetro de pequeñez \(T\)
(medio-ancho temporal del diamante) de la fracción de orden de Myrheim-Meyer:
\[
f(n) = f_0(n)\left[1 + T^2(\alpha_2-2\alpha_1)R(0) + T^2(\beta_2-2\beta_1)R_{00}(0)\right] + O(T^3),
\]
con \(R(0)\), \(R_{00}(0)\) invariantes de curvatura locales en el origen RNC,
para dimensión \(n\) y espaciotiempo genéricos.

**Comparación estructural con T39-B.** La forma funcional es análoga: fracción
de orden = valor plano + término lineal en un parámetro de pequeñez ×
coeficiente geométrico + resto de orden superior. Sin embargo:

1. Su expansión es **local** (RNC alrededor de un único punto, curvatura
   evaluada en el origen) y para un diamante que se **encoge a un punto**
   (\(T\to0\)); T39-B es una expansión **exacta** para la familia diamante EF
   de Schwarzschild con esquinas fijas \(r_p,r_q\), expandida en el ancho de
   coordenada nula \(dv\) (no en un parámetro de proximidad a un punto), con
   \(\kappa(r_p,r_q)\) en forma cerrada que integra la geometría exacta, no
   solo invariantes de curvatura locales.
2. No tratan una **familia** parametrizada por una variable como \(\tau\); su
   \(R(0)\) es fijo para un diamante dado. No hay, por tanto, antecedente de
   T39-C (monotonía uniforme en \(\tau\), separación Lipschitz).

**Relación:** `DIRECT_PRECURSOR` de la **técnica** de T39-B (expansión de
curvatura de la fracción de orden); **`NO_MATCH` de la instanciación exacta**
de T39-B (familia Schwarzschild-EF, \(\kappa(r_p,r_q)\) cerrada) y **`NO_MATCH`
de T39-C** (sin familia paramétrica ni monotonía).

### 4.5 Eichhorn, Gamito, Stokes — horizontes y enfoque geodésico

A. Eichhorn, P. Gamito, N. Stokes, "Towards black-hole horizons and geodesic
focusing in causal sets" (`biblioteca/derived-md/Towards black-hole horizons
and geodesic focusing in causal sets.md`).

Observable completamente distinto: expansión geodésica discreta vía
"escaleras" (ladders) y longitud de cadenas más largas, no fracción de pares
comparables. Única mención de Myrheim es una cita bibliográfica sin contenido
sustantivo.

**Relación:** `ORTHOGONAL` a T39-A–E.

### 4.6 Glaser–Surya (2013), Benincasa PhD (2013), *A Causal Set Black Hole*

Grep dirigido por "ordering fraction" / "comparable pair" / "curvature
correction" no produjo coincidencias en ninguno de los tres documentos. Todos
trabajan con abundancias de **intervalos inclusivos-\(k\)** (acción
Benincasa–Dowker) u otras observables, que Roy–Sinha–Surya (2013, §4) señalan
explícitamente como order-teóricamente distintas de las \(k\)-cadenas usadas
para la fracción de orden.

**Relación:** `ORTHOGONAL` (objeto order-teórico distinto).

### 4.7 Dos candidatos externos residuales — verificados y descartados

Identificados en la verificación de fecha de §4.4; no están en `biblioteca/`
local.

- **Kambor & Nomaan X (2020)**, "Manifold Properties from Causal Sets using
  Chains", [arXiv:2007.03835](https://arxiv.org/abs/2007.03835). Estudio
  **numérico** de cadenas para estimar curvatura/tiempo propio/dimensión en
  dS₂ y FLRW₃. Sin expansión analítica de fracción de orden, sin Schwarzschild,
  sin monotonía en un parámetro de familia.
  **Relación:** `ANALOGUE_OTHER_MODEL`.

- **J. Wang (2019)**, "Geometry of small causal diamonds", *Phys. Rev. D*
  **100**, 064020, [arXiv:1904.01034](https://arxiv.org/abs/1904.01034).
  Coincidencia de título engañosa: es **geometría de continuo pura** (bola
  geodésica, intervalo de Alexandrov, corte de cono de luz; tensor de
  Bel-Robinson), sin causal sets ni fracción de orden.
  **Relación:** `ORTHOGONAL` — campo distinto.

## 5. Matriz de prioridad (Ronda 1)

| Fuente | T39-A | T39-B | T39-C | T39-D | T39-E |
|---|---|---|---|---|---|
| Hoeffding 1963 (vía WP4) | — | — | — | `SUBSUMES` | — |
| Janson 2011 (vía WP4) | `TECHNICAL_BACKGROUND` | — | — | `DIRECT_PRECURSOR` | — |
| Reid 2004 | `TECHNICAL_BACKGROUND` | `NO_MATCH` | `NO_MATCH` | — | — |
| McGough/Bhandari 2021 | `TECHNICAL_BACKGROUND` | `TECHNICAL_BACKGROUND` | `NO_MATCH` | — | — |
| Roy–Sinha–Surya 2013 | — | `DIRECT_PRECURSOR` (técnica) | `NO_MATCH` | — | — |
| Eichhorn–Gamito–Stokes | — | `ORTHOGONAL` | `ORTHOGONAL` | — | — |
| Glaser–Surya 2013 / Benincasa PhD / *Causal Set Black Hole* | `ORTHOGONAL` | `ORTHOGONAL` | `ORTHOGONAL` | — | — |
| Kambor–Nomaan 2020 | — | `ANALOGUE_OTHER_MODEL` | `NO_MATCH` | — | — |
| Wang 2019 | — | `ORTHOGONAL` | `ORTHOGONAL` | — | — |
| Tsybakov / Ray–Schmidt-Hieber / Polyanskiy–Wu (anclas V9, Fase 2) | — | — | — | — | `TECHNICAL_BACKGROUND` |

No se identificó ninguna fuente que subsuma T39-B o T39-C. La cadena más
cercana (Roy–Sinha–Surya) cubre la **forma** de la técnica, no la
**instanciación**.

## 6. Limitación expresa: hueco de grafos geométricos / modelos latentes

`phase2_novelty_and_item5.md` §2.4 ya señaló, para el Teorema 3.8 (N1), que el
coto de grafos geométricos aleatorios y modelos de espacio latente (con la
pista `Bubeck–Ding–Eldan–Rácz`, marcada `READER_LEAD_UNVERIFIED`) queda
residual y no debe declararse agotado por búsquedas de título/abstract. La
hoja de ruta (`docs/hoja_de_ruta_30_jul_2026.md` §3.4) señala el mismo coto
explícitamente para T39-A–E:

> "Este coto quedó señalado por los lectores externos de la Fase 2 y no debe
> declararse agotado mediante búsquedas por título o abstract."

Esta ronda **no lo persiguió**. Se declara aquí, expresamente, como limitación
abierta — no como `NO_MATCH` ni como gate cerrado.

## 7. Techo de claims (provisional)

### Formulación permitida ahora

> Roy–Sinha–Surya (2013) establecen la técnica de expansión RNC de la fracción
> de orden en curvatura local; el Teorema 3.9 instancia una expansión análoga,
> pero exacta y para una familia paramétrica concreta de diamantes
> Schwarzschild-EF, con monotonía uniforme demostrada. Un barrido acotado (no
> sistemático, sin acceso a MathSciNet/Scopus, con el coto de grafos
> geométricos/modelos latentes aún sin agotar) no localizó un antecedente para
> esta instanciación.

### Formulaciones prohibidas

- "primer resultado" / "nuevo teorema" sin calificar el alcance del barrido;
- inferir `PRIORITY_CERTIFIED = YES` de `NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH`;
- afirmar que el hueco de grafos geométricos/modelos latentes está agotado;
- atribuir a Roy–Sinha–Surya la instanciación Schwarzschild-EF, la monotonía en
  \(\tau\) o el uso de la fecha "2024" (error de metadata corregido en §4.4).

## 8. Cierre provisional

```text
NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH
PRIORITY_NOT_YET_CERTIFIED
T39-D_DISCHARGED_NO_NOVELTY_CLAIM
T39-B/C_SURVIVING_CANDIDATE_FOR_ORIGINAL_CONTRIBUTION
RESIDUAL_GAP_OPEN: random_geometric_graphs / latent_space_models
```

Este acta no adjudica Gate A/B/C/D de `docs/hoja_de_ruta_30_jul_2026.md` §5. Esa
adjudicación, y la pregunta de §1 de este documento, quedan para `/auditor` en
sesión independiente. No se ha tocado el manuscrito, el código, el sello ni el
banco de experimentos.
