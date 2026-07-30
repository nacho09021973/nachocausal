# Hoja de trabajo — 30 jul 2026 · auditoría de prioridad de los Teoremas 3.9–3.10

> **Plan REVISABLE, no congelado.** No es una pre-registración ni autoriza código,
> simulaciones, ejecución del banco, cálculo de constantes, apertura de B2 o cambios
> en el sello. Mantener `RESPECT_SEAL_FREEZE`, `NO_RECONSTRUCTION_CLAIM`,
> `NO_GROUND_TRUTH_LEAKAGE`, `NO_POST_HOC_TUNING` y `NO_THRESHOLD_LOOSENING`.
> Esta hoja es el punto de reentrada para el **30 jul 2026** y no sustituye a
> `docs/roadmap.md`, al marcador de pausa ni a las hojas anteriores.

## 0. Punto de partida verificable

Rama de trabajo:

```text
agent/phase3-b2-decision-048
```

Commits de cierre y promoción de C6:

```text
141cccc05c63f48ae540a80c3968268dbf767b51
  docs: close C6 uniform remainder proof

861d5e54f1fc8153a6c8c64d733b34cb3f51d169
  docs: promote C6 to manuscript theorem
```

Estado matemático incorporado al manuscrito:

1. Existe un \(dv_0=dv_0(r_p,r_q,\tau_0,\tau_1)>0\), uniforme para
   \(\tau\in K=[\tau_0,\tau_1]\).
2. Para cada \(0<dv<dv_0\), \(p(\tau)\) es estrictamente creciente y satisface
   \[
   |p(\tau')-p(\tau)|
   \ge
   \frac{\kappa(r_p,r_q)\,dv}{2}|\tau'-\tau|.
   \]
3. Para cada par fijo \(\tau\ne\tau'\),
   \[
   \mathrm{TV}(Q_\tau^n,Q_{\tau'}^n)\to1.
   \]
   El \(n_0\) depende del par; solo es uniforme si
   \(\lvert\tau-\tau'\rvert\ge\eta>0\).
4. Junto con el Teorema 3.8, el exponente \(n^{-1/2}\) queda cerrado en el
   sentido \(o/\omega\), no a nivel de la constante crítica.

Anclas que deben leerse antes de buscar:

- `docs/manuscript_limits_draft.md` §3.3, Teoremas 3.8–3.9 y Corolario 3.10;
- `research_program/work_packages/wp4_comparable_pair_separation.md` §4–§4b;
- `research_program/work_packages/wp4_fisher_localization_floor.md` §4–§5;
- `research_program/bibliography/phase2_novelty_and_item5.md`;
- `research_program/bibliography/ficha_se_busca_tv_order_only.md`;
- `research_program/bibliography/identifiability_bibliography_matrix.md`.

## 1. Única pregunta de mañana

> ¿Existe en la literatura un resultado que contenga, anticipe de forma
> sustantiva o vuelva rutinaria la combinación específica de los Teoremas
> 3.9–3.10: separación `fixed_n` de leyes de posets mediante la fracción de pares
> comparables en la familia diamante de Schwarzschild, con expansión uniforme en
> \(dv\) y frontera estadística \(n^{-1/2}\) cerrada por ambos lados en el sentido
> \(o/\omega\)?

La pregunta **no** es si Hoeffding, Chebyshev, Kendall, Le Cam o la teoría de
U-estadísticos son conocidos. Lo son. La auditoría debe separar la maquinaria
estándar de la instanciación geométrica y del emparejamiento de tasas.

## 2. Descomposición obligatoria del claim

No buscar “el teorema” como una unidad indivisible. Auditar por piezas:

| ID | Componente | Techo inicial |
|---|---|---|
| **T39-A** | \(p(\tau)\) como funcional order-only / fracción de comparabilidad | Maquinaria y observable con precedentes esperables |
| **T39-B** | Expansión \(p(\tau)=1/2+\kappa\tau\,dv+O(dv^2)\) con control \(C^1\) uniforme | Posible aporte específico de la familia |
| **T39-C** | Monotonía uniforme y separación Lipschitz para \(0<dv<dv_0\) | Corolario geométrico específico |
| **T39-D** | Cota inferior de TV mediante \(S_n\), momentos exactos y Chebyshev | Aplicación de estadística estándar al canal `fixed_n` |
| **T39-E** | Frontera \(o(n^{-1/2})/\omega(n^{-1/2})\) al combinar 3.8 y 3.9 | Posible síntesis específica; constantes no cerradas |

Cada fuente candidata recibirá una relación distinta para cada componente:

```text
SUBSUMES
DIRECT_PRECURSOR
TECHNICAL_BACKGROUND
ANALOGUE_OTHER_MODEL
ORTHOGONAL
NO_MATCH_AFTER_FULL_READ
```

## 3. Cotos bibliográficos, en orden

### 3.1 Causal sets y orden fraccionario

- Myrheim–Meyer dimension y ordering fraction;
- abundancias de relaciones y estimadores de dimensión;
- fluctuaciones y consistencia de observables de dos puntos;
- inferencia paramétrica en sprinklings condicionados a cardinalidad.

**Pregunta falsificadora:** ¿algún trabajo convierte explícitamente la fracción
de relaciones en separación de leyes de posets para una familia geométrica
continua y prueba una tasa local?

### 3.2 Posets aleatorios, límites de posets y órdenes intercambiables

- leyes de posets inducidas por muestras i.i.d.;
- poset kernels, poset limits y problemas de identificación;
- estadísticas de densidad de subórdenes de tamaño dos;
- alternativas locales y separación de experimentos observados tras cociente por
  isomorfismo.

**Pregunta falsificadora:** ¿la combinación “densidad de dos-cadenas +
concentración + inyectividad paramétrica” aparece ya como un teorema general que
subsuma T39-D/E?

### 3.3 Cópulas y Kendall

- inferencia paramétrica mediante Kendall's tau;
- U-estadísticos de concordancia bajo alternativas locales;
- monotonicidad de Kendall en familias paramétricas;
- tasas de tests basados en concordancia.

**Pregunta falsificadora:** ¿un teorema general de cópulas convierte las
hipótesis ya probadas para \(c_\tau\) en T39-C/E sin usar la geometría específica?

### 3.4 Geometría aleatoria y modelos latentes

- random geometric graphs;
- latent-space models;
- graphon/poset-kernel parameter testing;
- minimax testing tras observar solo la estructura combinatoria no etiquetada.

Este coto quedó señalado por los lectores externos de la Fase 2 y no debe
declararse agotado mediante búsquedas por título o abstract.

### 3.5 Estadística asintótica general

- U-estadísticos binomiales bajo alternativas contiguas;
- eficiencia de tests de Kendall;
- LAN/QMD y separación \(n^{-1/2}\);
- data processing y pérdida por compresión a una estructura no etiquetada.

Aquí el resultado esperado es principalmente `TECHNICAL_BACKGROUND`. Encontrar
la tasa estándar no subsume por sí solo la expansión geométrica T39-B/C.

## 4. Protocolo de lectura y evidencia

1. Buscar primero revisiones y palabras clave para localizar candidatos.
2. Para toda fuente que parezca cercana, abrir y leer el artículo primario
   completo en las secciones relevantes.
3. Registrar por fuente:

   | Campo | Contenido exigido |
   |---|---|
   | Referencia | autores, año, título, venue, DOI/arXiv |
   | Objeto observado | puntos, grafo etiquetado, poset no etiquetado, estadístico |
   | Canal | `fixed_n`, Poisson, asintótico, otro |
   | Familia / dimensión | hipótesis completas |
   | Teorema exacto | número y páginas |
   | Tasa | objeto, pérdida y cuantificadores |
   | Relación T39-A–E | una etiqueta por componente |
   | Claim permitido | frase que la fuente autoriza |
   | Claim prohibido | inferencia que la fuente no autoriza |

4. No usar `NO PRIOR FOUND` como certificado de novedad.
5. No citar snippets de buscador, abstracts secundarios ni respuestas de modelos
   como prueba final.

Documento de trabajo preferido:

```text
research_program/bibliography/c6_theorem39_priority_audit.md
```

No crearlo hasta iniciar efectivamente la auditoría; esta hoja solo fija el
contrato de mañana.

## 5. Gates de salida

### Gate A — `DIRECT_PRIOR_FOUND`

Existe una fuente que subsume T39-B–E o su combinación esencial.

Acción:

- citarla junto al Teorema 3.9;
- rebajar el wording a especialización o corolario aplicado;
- conservar únicamente como aporte lo que quede fuera de la fuente;
- no debilitar la corrección matemática del teorema.

### Gate B — `PRECURSOR_ONLY`

Hay precedentes directos para el observable o la tasa, pero no para la
instanciación completa.

Acción:

- describirlos con precisión;
- mantener “family-specific instantiation”;
- prohibir “first”, “new method” y equivalentes.

### Gate C — `NO_CONCRETE_SINK_ANCHORED`

La búsqueda exhaustiva de los cotos declarados no encuentra un teorema que
subsuma T39-B–E.

Acción:

- registrar literalmente el alcance de la búsqueda;
- mantener lenguaje acotado, nunca `NOVELTY_CERTIFIED`;
- dejar una lista residual de vecindarios no agotados.

### Gate D — `INCONCLUSIVE_ACCESS_OR_SCOPE`

Faltan textos completos, acceso o competencia temática para decidir.

Acción:

- no tocar el wording de prioridad;
- registrar qué falta;
- mantener el Teorema 3.9 probado pero sin reclamo de novedad.

## 6. Entregables del día

Obligatorios:

1. auditoría `c6_theorem39_priority_audit.md` con matriz T39-A–E;
2. lista de fuentes primarias leídas y fuentes descartadas con razón;
3. veredicto Gate A/B/C/D;
4. parche mínimo de §6.5 y §7.3 del manuscrito **solo si** la evidencia lo exige;
5. revisión adversarial final que compruebe que el wording no excede la evidencia.

Opcional, únicamente si sobra tiempo:

- actualizar `identifiability_bibliography_matrix.md` con las fuentes realmente
  adjudicadas.

No son entregables de mañana:

- calcular \(\bar I\), \(dv_0\) o la constante crítica;
- diseñar o ejecutar un estimador;
- promover maximalidad, coorientación o cintura;
- reorganizar todo el manuscrito;
- abrir B2 o cualquier observable nuevo.

## 7. Orden de trabajo

1. **Preflight documental** — confirmar HEAD, worktree limpio y anclas.
2. **Búsqueda amplia** — cotos 3.1–3.5, sin adjudicar por abstracts.
3. **Lectura primaria** — candidatos cercanos, teoremas y páginas exactas.
4. **Matriz T39-A–E** — relación fuente por componente.
5. **Adjudicación** — Gate A/B/C/D y claim ceiling.
6. **Parche mínimo** — solo si procede.
7. **Revisión adversarial** — cuantificadores, precedencia, canales y wording.
8. **Commit separado** — auditoría primero; parche del manuscrito después, si lo
   hubiera. No mezclar una búsqueda inconclusa con una reescritura de claims.

## 8. Criterio de cierre

La sesión termina en estado limpio solo si:

- cada candidato cercano fue leído en fuente primaria;
- T39-A–E tienen adjudicación explícita;
- `fixed_n` no se mezcló con Poisson no condicionado;
- ninguna ausencia de resultado se convirtió en certificado de novedad;
- el estado matemático de los Teoremas 3.9–3.10 quedó separado de su prioridad;
- no se añadió ningún \(dv\), \(n_0\) o prefactor numérico;
- cualquier cambio documental pasa `git diff --check`;
- código, sello, B2 y banco de experimentos permanecen intactos.

## 9. Siguiente acción única al reentrar

> Abrir `docs/manuscript_limits_draft.md` §6.5 y
> `research_program/bibliography/phase2_novelty_and_item5.md`; convertir el claim
> del Teorema 3.9 en la matriz T39-A–E **antes** de lanzar la primera búsqueda.

## 10. Actualización de cierre — 30 jul 2026 (mismo día)

> Esta sección registra lo que **efectivamente ocurrió** hoy. No sustituye §0–9:
> la auditoría de C6/Teoremas 3.9–3.10 planeada arriba **no se ejecutó** y sigue
> siendo la acción pendiente de §9, sin cambios.

### 10.1 Lo que se hizo en su lugar

Durante la sesión se abrió y cerró un **track lateral distinto** al planificado:
la formulación de un lema abstracto separado,
`research_program/work_packages/wp4_dimension_free_order_statistic_separation.md`
(separación `fixed_n` de leyes de posets no etiquetados vía fracción de pares
comparables, cota de TV vía Hoeffding), seguida de su propia auditoría de
prioridad bibliográfica en

```text
research_program/bibliography/wp4_dimension_free_order_statistic_priority_audit.md
```

Commits (rama `agent/phase3-b2-decision-048`):

```text
1359c0f  docs: add dimension-free fixed-n separation theorem
778a1d5  docs: calibrate dimension-free separation as standard lemma
```

### 10.2 Veredicto de esa auditoría lateral

```text
PRIORITY_GATE = PRECURSOR_ONLY
MATHEMATICAL_CLASSIFICATION = STANDARD_COROLLARY
EXACT_SINGLE_SOURCE_NOT_LOCATED = YES
NOVELTY_CERTIFIED = NO
```

Cadena identificada: Janson (2011) da la capa de posets no etiquetados/patrón
inducido (DFO-A, DFO-B, DFO-E cualitativo); Hoeffding (1963) §4a da la
concentración exponencial (DFO-C); el test a punto medio cierra la cota de TV
(DFO-D). Ninguna fuente única localizada subsume la combinación completa, pero
la cadena la vuelve rutinaria — no se certifica novedad del teorema abstracto.
Prueba interna: `INTERNAL_PROOF_AUDITED` (no reabierta).

### 10.3 Estado real de la pregunta de §1 (C6 geométrico)

**Sin auditar.** `c6_theorem39_priority_audit.md` **no existe todavía**. La
descomposición T39-A–E de §2, los cotos de §3 y los gates de §5 siguen
íntegramente vigentes y no se ha adjudicado ninguno. La única cuestión
científica abierta que queda tras el cierre del lema abstracto es,
explícitamente, **la prioridad específica de C6 geométrico** (Teoremas 3.9–3.10
del manuscrito), independiente del lema `dimension-free` ya cerrado.

### 10.4 Estado del repositorio al cierre

- Rama `agent/phase3-b2-decision-048`, HEAD `778a1d5`.
- `origin/agent/phase3-b2-decision-048` sincronizado al mismo commit (push
  hecho, divergencia `0/0`).
- Sin PR abierta, sin conflictos.
- Archivos no versionados intactos: `docs/hoja_de_ruta_30_jul_2026.md` (este
  archivo) y `research_program/bibliography/wp4_dimension_free_order_statistic_priority_audit.md`.
- Código, sello, B2 y banco de experimentos no tocados.

### 10.5 Siguiente acción única al reentrar (reafirmada)

La acción de §9 sigue siendo la correcta y no ha sido superada por el trabajo
de hoy: abrir `docs/manuscript_limits_draft.md` §6.5 y
`research_program/bibliography/phase2_novelty_and_item5.md`, y convertir el
claim del Teorema 3.9 en la matriz T39-A–E antes de lanzar la primera
búsqueda de la auditoría de C6.
