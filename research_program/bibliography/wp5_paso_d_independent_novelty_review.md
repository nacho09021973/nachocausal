# WP5 Paso D — Revisión bibliográfica independiente (descarga del gate de novedad)

> **STATUS: INDEPENDENT_SEARCH_PERFORMED / NOVELTY_NOT_REFUTED / NOT_A_NOVELTY_CERTIFICATE.**
> **REV-1 (2026-07-28, misma sesión):** ampliado con (a) búsqueda en **INSPIRE-HEP** vía su API
> pública, (b) **verificación a texto completo** de `arXiv:2605.27514` tras descargar el PDF a
> `biblioteca/`, y (c) **una fuente adicional descubierta y descargada**, de Brito–Eichhorn–Pfeiffer
> 2023 (revisada por pares), que **ancla Gate A de la decisión 046 en literatura publicada** en vez
> de en una ausencia de resultados de búsqueda. Ver §4.4 y §4.5 — es el hallazgo principal de REV-1.
> Documento de registro. No ejecuta código, no consume semillas, no toca el sello, no congela nada,
> no emite ningún claim público. Su función es **descargar el Paso D** de
> `research_program/work_packages/wp5_order_only_blindness_map_definition.md` §5 dejando constancia
> auditable de **qué se buscó, cómo, qué se encontró y qué NO queda establecido**.

FECHA: 2026-07-28
HEAD en el momento de la revisión: `e954fe2`
Sello: `thresholds.py sha256 = 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (intacto)

## 1. Qué exige el Paso D, literalmente

`wp5_order_only_blindness_map_definition.md` §5:

> **Paso D.** Revisión bibliográfica independiente — más allá de las cuatro fuentes ya verificadas
> localmente en WP4-floor §9 (Braun 2025, Müller 2025, Madsen 2026, Boguñá-Krioukov 2024) — antes de
> cualquier claim público de novedad. **Condición de bloqueo: ningún claim de novedad pública debe
> emitirse antes de completar este paso.**

Y `wp4_fisher_localization_floor.md` §9 cierra con:

> "Boguñá-Krioukov and the memo's broader corpus claims remain unverified; an independent search is
> still due before any public novelty statement."

## 2. Qué se somete a prueba (afirmaciones de novedad ya *estrechadas* por WP4 §9)

WP4 §9 ya redujo honestamente el claim tras leer las tres fuentes primarias. Lo que queda por
contrastar contra literatura externa es exactamente esto, y **nada más amplio**:

| # | Afirmación candidata a novedad | Origen en repo |
|---|---|---|
| N1 | Familia paramétrica regular + expansión QMD/Fisher + suelo de dos puntos `1/sqrt(n·Ībar)` **para un parámetro de localización de horizonte en el canal order-only** | `wp4_fisher_localization_floor.md` §4–§5 |
| N2 | Enunciado exacto de órbita de escala: `TV = 0` con `r_s` distinto (Teorema A, ceguera exacta) | `first_witness_pair_candidates.md` §2 |
| N3 | Diagnóstico de degeneración de Kruskal (`I ≡ 0` en caja de Kruskal fija con parámetro de masa) | `wp4_fisher_localization_floor.md` §2, Prop. 1 |
| N4 | `κ(τ) = V(τ)·I(τ)` exactamente invariante bajo dilatación ⇒ suelo en forma intrínseca `δ_n ~ ℓ/sqrt(κ̄)` | `wp4_fisher_localization_floor.md` §5a, Prop. 6 |
| N5 | El "mapa de ceguera order-only" como objeto organizador + la asimetría lógica ciego⇏visible | `wp5_order_only_blindness_map_definition.md` §1–§3 |

Reconocido de antemano, por WP4 §9: **Müller 2025 (Teorema 2) es el pariente publicado más cercano
del lado de indistinguibilidad** — construcción de par testigo a `K` fijo, leyes de orden
`ε`-próximas, geometría arbitrariamente distinta, para el target "distancia/diámetro lorentziano".
Ese reconocimiento **se mantiene** y no lo altera esta revisión.

## 3. Método (reproducible)

Herramienta: búsqueda web (`WebSearch`) + lectura directa (`WebFetch`), sesión del 2026-07-28.
**Nueve** formulaciones de consulta, deliberadamente variadas para no depender de un solo vocabulario:

1. `Fisher information causal set sprinkling parameter estimation lower bound`
2. `causal set theory Le Cam two-point method minimax lower bound geometry inference`
3. `"causal set" statistical indistinguishability total variation distinct spacetimes finite n`
4. `causal set black hole horizon localization statistical resolution limit discreteness scale`
5. `arxiv causal set "Fisher information" quantum gravity discrete geometry estimation`
6. `Charting causal set configuration space with graph observables arXiv 2605.27514`
7. `Lorentzian Poisson process minimax estimation rate spacetime geometry statistics 2026`
8. `"causal set" estimate black hole mass parameter from causal order statistics`
9. `causal set sprinkling scale invariance dilation different mass identical order law indistinguishable`

Lectura directa a texto completo de metadatos/abstract: `arXiv:2605.27514` (vía `WebFetch`).

**Limitaciones declaradas de este método — vinculantes para la lectura del resultado:**

- La cobertura **no es exhaustiva**. Nueve consultas en inglés, sesgadas hacia arXiv, no equivalen a
  una revisión sistemática con protocolo de cribado.
- Salvo `arXiv:2605.27514`, los hallazgos se basan en **títulos/abstracts/resúmenes de búsqueda**, no
  en lectura de texto completo.
- No se consultaron bases indexadas (INSPIRE-HEP, MathSciNet, Scopus, Web of Science), ni actas de
  congresos, ni tesis no indexadas en arXiv.
- **La ausencia de antecedente encontrado NO es prueba de novedad.** Esta es exactamente la regla
  fundacional del repositorio aplicada a sí misma; ninguna frase de este documento debe citarse como
  si estableciera novedad.

## 4. Hallazgos

### 4.1 Resultado principal (negativo, y es el que importa)

**Ninguna de las nueve consultas devolvió un trabajo que aplique maquinaria de Fisher/Hellinger/QMD,
un argumento de dos puntos de Le Cam, una cota minimax, o un suelo de tasa de localización, al canal
order-only de causal sets.** Las consultas 1, 2, 5 y 7 devolvieron consistentemente **dos corpus
disjuntos**: (a) estadística/teoría de la información genérica (Le Cam, Cramér-Rao, minimax en
espacios de Wasserstein, estimación de intensidad de Poisson), y (b) causal set theory
(fenomenología, entropía de agujero negro, d'Alembertiano, dimensión espectral) — **sin intersección
encontrada**. Esto **confirma** la constatación central del memo `biblioteca/Novedad bibliografica PW4.md`
y la sostiene bajo formulaciones de consulta distintas a las suyas.

Para N2, N3 y N4 (órbita de escala `TV=0`, degeneración de Kruskal, invariancia de `κ` bajo
dilatación) la consulta 9, específicamente dirigida, **no devolvió antecedente alguno**; los
resultados fueron material general sobre invariancia Lorentz del sprinkling, que es un enunciado
distinto (invariancia de la *ley del proceso* bajo boosts, no ceguera del canal a un *parámetro
físico distinto* bajo dilatación).

### 4.2 Fuente nueva relevante, NO presente en `biblioteca/` — debe incorporarse

**Eichhorn, Mack, Le, Wagner (2026), *Charting causal set configuration space with graph
observables*, arXiv:2605.27514** (enviado 26 mayo 2026; Institute for Theoretical Physics +
Scientific Software Center, Heidelberg).

Leído directamente (abstract + metadatos). Contenido: nueve clases de causal sets (manifoldlike con
curvatura de Ricci inhomogénea, retículos, órdenes por capas, cuasicristales lorentzianos…) usadas
como banco de pruebas de observables; encuentran que la distribución de grado de enlace, los
autovalores del laplaciano del diagrama de Hasse simetrizado, y la **abundancia de intervalos
causales** distinguen las clases.

Verificado explícitamente sobre esta fuente:

- **(a) No contiene cota inferior estadística ni resultado de imposibilidad/indistinguibilidad.** Es
  constructivo/diagnóstico. **No compite con N1–N5.**
- **(b) No trata horizontes ni Schwarzschild.**
- **(c) Cuantifica fluctuaciones, pero en clave pragmática** ("small fluctuations… enabling
  classification"), no como cota estadística formal.

**Por qué importa igualmente, y en dos direcciones:**

1. **Corrobora de forma independiente el hallazgo Gate A(iv) de la decisión 046.** Su motivación
   declarada para *evitar* invariantes de curvatura es que "often exhibit large fluctuations and are
   computationally very expensive" — exactamente el defecto que el comité 046 imputó al canal
   BD/BDG como generador de hojas (varianza ≫ media). Que el propio grupo de EGS, de forma
   independiente y por razones metodológicas propias, **abandone los invariantes de curvatura como
   observable práctico** es respaldo externo fuerte para el terminal de la 046.
2. **Es el estado del arte vigente en "qué observable distingue qué"**, y por tanto contexto
   obligado del §6 del paper de consolidación. Su existencia refuerza, no debilita, el
   posicionamiento: ellos cartografían qué **sí** distingue constructivamente; el aporte de este
   repo estaría en el lado de **cotas inferiores**, ausente en su trabajo.

**Acción requerida (no ejecutada aquí):** incorporar el PDF a `biblioteca/` y verificar el texto
completo antes de citarlo en cualquier documento público. Hasta entonces su contenido más allá del
abstract es `[UNVERIFIED]`.

### 4.3b Búsqueda en INSPIRE-HEP (REV-1) — la base canónica del área

Ejecutada contra la API pública (`https://inspirehep.net/api/literature`, campo `ab` = abstract),
2026-07-28. Consultas y totales **literales**:

| Consulta INSPIRE | `total` | Contenido de los hits |
|---|---:|---|
| `ab "causal set" and ab "Fisher information"` | **2** | `2502.09894` (cono de entropía holográfica), `2106.12585` (Lorentzian threads) — **holografía, no CST; falsos positivos léxicos** |
| `ab "causal set" and ab minimax` | **1** | `2502.09894` — mismo falso positivo |
| `ab "causal sets" and ab "lower bound"` | **6** | holografía/información cuántica/contextualidad; **ninguno es una cota inferior de estimación geométrica** |
| `ab "causal set" and ab "Le Cam"` | **0** | — |
| `ab "causal set" and ab identifiability` | **0** | — |
| `ab sprinkling and ab estimation and ab geometry` | **0** | — |
| `ab "causal set" and ab "total variation"` | **2** | agujeros negros primordiales, MERA — no relacionados |
| `ab "causal set" and ab horizon and ab discrete` | **1** | `2605.06813` = EGS, **ya en `biblioteca/`** |

**Lectura.** INSPIRE, que sí indexa exhaustivamente el corpus gr-qc/hep-th, devuelve **cero**
trabajos que crucen causal sets con Le Cam, identificabilidad, o estimación geométrica por
sprinkling. Los únicos cruces léxicos con "Fisher"/"minimax"/"lower bound" son papers de holografía
donde "causal set" no denota el objeto de CST. Esto **eleva sustancialmente** la fuerza del negativo
respecto a la búsqueda web de §3, que no podía descartar un sesgo de indexación.

### 4.4 `arXiv:2605.27514` — verificación a TEXTO COMPLETO (REV-1)

PDF descargado a `biblioteca/2605.27514v1.pdf` (6.4 MB) y extraído a texto (21 350 palabras). El
abstract del PDF **coincide verbatim** con el recuperado por búsqueda web en §4.2 — verificación
cruzada superada. Conteo de términos sobre el texto completo:

| Término | Ocurrencias | Consecuencia |
|---|---:|---|
| Fisher, minimax, Le Cam, Cramér, "lower bound", "total variation", "hypothesis test" | **0** cada uno | **(a) CONFIRMADO a texto completo:** no contiene cota inferior estadística ni maquinaria de imposibilidad. No compite con N1–N5. |
| Schwarzschild, horizon, "black hole" | **0** cada uno | **(b) CONFIRMADO a texto completo:** no trata horizontes. |
| variance (11), fluctuation (5), "curvature invariant" (9), Ricci (11) | — | **(c) CONFIRMADO:** las fluctuaciones se tratan en clave práctica/comparativa, no como cota formal. |
| **Kretschmann (2), Weyl (1)** | — | **hallazgo no anticipado — ver abajo** |

### 4.5 HALLAZGO PRINCIPAL DE REV-1 — Gate A de la decisión 046 queda anclado en literatura publicada

La verificación a texto completo localizó dos pasajes que **no** eran accesibles desde el abstract, y
que convierten el Gate A de la decisión 046 de *"buscamos y no encontramos"* en *"la literatura
publicada afirma que no se ha logrado"*:

> `2605.27514`, §I (`:81-85`): "Of these, only the simplest one, namely the **Ricci scalar**, has been
> constructed [15]; additionally, **□R** can be constructed [16]. It has been conjectured in [16],
> that additional higher-order invariants may be encoded in so-called **stacked order intervals**,
> but **no explicit construction of, e.g., the Kretschmann scalar, has so far been achieved**."

> `2605.27514`, Outlook (`:2789-2792`): "So far, in causal sets only expressions for discrete
> counterparts of **R** [15] and **□R** [16] are known. Therefore, understanding which graph
> observables are sensitive to changes in, e.g., the **Kretschmann scalar**, may provide a hint
> towards the construction of a discrete counterpart of this curvature invariant."

Su referencia [16] es una fuente **revisada por pares** que el comité 046 **no** consideró, ausente
de `biblioteca/` hasta ahora, y directamente en la categoría del trigger de reapertura de 046:

> **de Brito, G. P., Eichhorn, A., Pfeiffer, C. (2023), *Higher-order curvature operators in causal
> set quantum gravity*, Eur. Phys. J. Plus 138 (7) 592, arXiv:2301.13525.** Descargado a
> `biblioteca/2301.13525v2.pdf`, extraído y verificado a texto completo (8 176 palabras).

Lo que ese paper **construye**, del abstract verbatim: *"we generalize the discrete d'Alembertian,
which encodes the Ricci scalar, to higher orders. We prove that curvature invariants of the form
**`R² − □R`** (and similar invariants at higher powers of derivatives) arise in the continuum
limit."*

Y lo que **explícitamente no** construye, de su §1 (`:152-157`): tras enumerar la base de invariantes
—que incluye `R_μνκλ R^μνκλ` (Kretschmann) y señalar que *"The Riemann-invariant can also be traded
for the square of the **Weyl** tensor"*— concluye: *"As we will find, we can construct `R² − □R`"*.
Conteo sobre su texto completo: **Kretschmann 0, vacuum 0, Ricci-flat 0, Schwarzschild 0, horizon 0**.

**Consecuencia para la decisión 046 (corroboración, NO cambio de terminal).** El estado del arte en
operadores de curvatura de orden superior order-only construye **únicamente invariantes derivados del
escalar de Ricci** (`R`, `□R`, `R² − □R`, y potencias superiores de derivadas). **Todos se anulan
idénticamente cuando `R ≡ 0`**, que es exactamente el caso de Schwarzschild en vacío 3+1D. Ninguno de
los dos papers aborda siquiera el caso de vacío (`vacuum`/`Ricci-flat`: cero ocurrencias en ambos).
Por tanto:

- El Gate A de la 046 pasa de apoyarse en **ausencia de hits de búsqueda** a apoyarse en **dos
  fuentes publicadas** (una de ellas revisada por pares, EPJ Plus 2023) que delimitan el estado del
  arte exactamente donde la 046 lo situó. La marca `[UNVERIFIED]` que el brief del físico puso sobre
  este punto **queda descargada**.
- El **trigger de reapertura de la 046 NO se ha disparado**: no existe construcción de Kretschmann
  ni de Weyl². Pero ahora se conoce **la vía concreta por la que podría dispararse**: la conjetura de
  los *stacked order intervals* de de Brito–Eichhorn–Pfeiffer, señalada en `2605.27514` como
  dirección abierta. **Ese es el objeto a vigilar**, y es un blanco mucho más preciso que "que
  aparezca algo en la literatura".
- Como el terminal de la 046 está **firmado y cerrado** (`STATUS_046 = SIGNED_AND_CLOSED`), esta
  corroboración se registra **aquí** y no se edita aquel documento. No cambia su polaridad ni su
  alcance; los refuerza.

**Nota adicional sobre N1/N5.** `2605.27514` §Outlook menciona una *"probabilistic measure of
distinguishability"* propia, basada en distancias entre histogramas normalizadas por la variación
intra-clase. Es una medida **heurística y comparativa entre clases**, sin `TV`, sin cota minimax y
sin garantía; **no compite** con N1/N5, pero es literatura adyacente que cualquier redacción pública
debe citar y distinguir explícitamente.

### 4.3 Defecto de documentación detectado en WP4 §9

`wp4_fisher_localization_floor.md` §9 se contradecía sobre Boguñá-Krioukov: el bullet dedicado dice
"**now locally verified**" (PDF en `biblioteca/PhysRevD.110.024008-accepted.pdf`), pero el párrafo de
cierre decía "Boguñá-Krioukov **and** the memo's broader corpus claims **remain unverified**". La
frase de cierre era un remanente anterior a esa verificación.

**`[RESUELTO en REV-1, 2026-07-28]`** Corregido *in situ* en `wp4_fisher_localization_floor.md` §9
con una nota de corrección fechada que (i) declara B-K verificado, (ii) **mantiene** la advertencia
sobre el corpus más amplio del memo, que sigue sin verificarse pieza a pieza, (iii) apunta a este
documento como la búsqueda independiente ya realizada, y (iv) incorpora la corroboración externa de
§4.5. El texto original no se borró: se conserva citado dentro de la propia nota de corrección,
siguiendo el patrón de corrección acotada de la decisión 043.

## 5. Veredicto

```text
WP5_PASO_D = DISCHARGED_AS_SEARCH / NOVELTY_NOT_REFUTED / NOVELTY_NOT_CERTIFIED

N1 (suelo Fisher/dos puntos order-only para localización de horizonte) — sin antecedente encontrado
N2 (órbita de escala TV=0 exacta)                                      — sin antecedente encontrado
N3 (degeneración de Kruskal, I≡0)                                      — sin antecedente encontrado
N4 (kappa = V*I invariante bajo dilatación)                            — sin antecedente encontrado
N5 (mapa de ceguera + asimetría ciego⇏visible)                         — sin antecedente encontrado

PARIENTE PUBLICADO MÁS CERCANO (reconocido, no desplazado): Müller 2025 Teorema 2 (par testigo a K
fijo, target = distancia/diámetro lorentziano). Sigue siendo el antecedente a citar y distinguir
explícitamente en cualquier redacción pública.

FUENTES NUEVAS INCORPORADAS A biblioteca/ EN REV-1 (ambas verificadas a texto completo):
  - Eichhorn-Mack-Le-Wagner 2026, arXiv:2605.27514 (biblioteca/2605.27514v1.pdf) — constructiva, sin
    cotas inferiores (Fisher/minimax/Le Cam/TV = 0 ocurrencias), sin horizontes (Schwarzschild/
    horizon/black hole = 0). Afirma en texto: "no explicit construction of, e.g., the Kretschmann
    scalar, has so far been achieved".
  - de Brito-Eichhorn-Pfeiffer 2023, Eur.Phys.J.Plus 138:592, arXiv:2301.13525
    (biblioteca/2301.13525v2.pdf) — REVISADA POR PARES. Construye invariantes de orden superior
    SOLO de la forma R^2 - □R, todos derivados del escalar de Ricci; identifica el invariante de
    Riemann/Weyl^2 como elemento de la base que NO construye. vacuum/Ricci-flat = 0 ocurrencias.

EFECTO SOBRE LA DECISIÓN 046 (corroboración, no cambio de terminal): Gate A pasa de apoyarse en
ausencia de resultados de búsqueda a apoyarse en dos fuentes publicadas. Todos los invariantes
order-only construidos hasta hoy se anulan idénticamente si R=0, que es el caso de Schwarzschild en
vacío. La marca [UNVERIFIED] del brief del físico queda descargada. El trigger NO se ha disparado.

INSPIRE-HEP (base canónica del área, 8 consultas): cero antecedentes genuinos. Los únicos cruces
léxicos con Fisher/minimax/lower-bound son papers de holografía donde "causal set" no denota el
objeto de CST.
```

**Lectura vinculante del veredicto.** El gate de bloqueo del Paso D queda **descargado en el sentido
en que estaba redactado** — la revisión independiente se ha realizado y está documentada. Pero el
resultado es *"no se encontró antecedente"*, que **autoriza a redactar un claim de novedad
cuidadosamente acotado**, y **no** a afirmar novedad como hecho establecido. La diferencia es la
misma que la decisión 046 fija en su `SCOPE_OF_NEGATIVE`, y se aplica aquí a la propia revisión.

## 6. Qué sigue pendiente antes de cualquier envío

| # | Ítem | Estado a 2026-07-28 |
|---|---|---|
| 1 | Incorporar `arXiv:2605.27514` a `biblioteca/` y verificar texto completo | ✅ **HECHO** (REV-1 §4.4) — PDF descargado, abstract cotejado, conteos verificados |
| 2 | Resolver la contradicción de WP4 §9 sobre Boguñá-Krioukov | ✅ **HECHO** (REV-1 §4.3) — corregido *in situ* con nota fechada |
| 3 | Búsqueda en base indexada canónica (INSPIRE-HEP) | ✅ **HECHO** (REV-1 §4.3b) — 8 consultas vía API pública, cero antecedentes genuinos |
| 4 | Redactar el claim de novedad en forma **acotada y comparativa** ("no conocemos antecedente de X; lo más próximo es Müller 2025, que difiere en Y"), nunca absoluta | ⬜ pendiente — es tarea de redacción del paper, no de esta revisión |
| 5 | **Lectura de un experto del área ajeno al proyecto** | ⬜ **PENDIENTE — NO DESCARGABLE DESDE DENTRO DEL REPOSITORIO.** Material de entrega *preparado* (2026-07-28): `research_program/bibliography/external_adversarial_review_package_n1_n5.md` — paquete adversarial autocontenido con N1–N5, comparación con Müller 2025 y formulario de veredicto. Preparar el material **no** descarga el ítem: sigue faltando el lector humano ajeno. Candidatos identificados con fuente primaria verificada en `research_program/bibliography/external_reader_candidates_n1_n5.md` (dos tiers por comunidad; su §4 plantea una decisión pendiente del PI sobre la **letra** de este ítem, que dice «competente en causal set theory» y excluiría a los candidatos capaces de examinar el hueco de N1/N4) |

**Sobre el ítem 5, explícitamente.** Este ítem **no puede** descargarse por búsqueda, por agente, ni
por ningún procedimiento interno, y **no debe** marcarse como cumplido por aproximación. El
repositorio no puede certificar su propia novedad: es la misma regla fundacional que impide que el
autor de un claim sea su único verificador, aplicada un nivel más arriba. Simular una revisión
externa con otra instancia del mismo sistema sería precisamente un guardarraíl que no puede fallar,
es decir, decoración. Queda como acción humana: identificar un lector competente en causal set theory
sin implicación en el proyecto, entregarle §2 (las cinco afirmaciones N1–N5), §4.5 (el estado del
arte anclado) y el par más próximo (Müller 2025), y pedirle específicamente que intente **refutar**
la novedad, no que la confirme.

**Vía de vigilancia concreta que REV-1 deja identificada.** El trigger de reapertura de la decisión
046 tiene ahora un blanco preciso en vez de una condición genérica: la conjetura de los **stacked
order intervals** de de Brito–Eichhorn–Pfeiffer 2023, señalada en `2605.27514` como la dirección por
la que podría llegar una construcción discreta del Kretschmann. Vigilar citas a `arXiv:2301.13525` es
el modo más barato y específico de detectar si el trigger se dispara.
