# WP5 Paso D — Revisión bibliográfica independiente (descarga del gate de novedad)

> **STATUS: INDEPENDENT_SEARCH_PERFORMED / NOVELTY_NOT_REFUTED / NOT_A_NOVELTY_CERTIFICATE.**
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

### 4.3 Defecto de documentación detectado en WP4 §9

`wp4_fisher_localization_floor.md` §9 se contradice sobre Boguñá-Krioukov: el bullet dedicado dice
"**now locally verified**" (PDF en `biblioteca/PhysRevD.110.024008-accepted.pdf`), pero el párrafo de
cierre dice "Boguñá-Krioukov **and** the memo's broader corpus claims **remain unverified**".
Probablemente la frase de cierre quedó obsoleta al verificarse el PDF. **No se corrige aquí** (no
modificar documentos ajenos al alcance de esta tarea); se registra para que el autor lo resuelva
antes de la consolidación.

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

FUENTE NUEVA A INCORPORAR: Eichhorn-Mack-Le-Wagner 2026 (arXiv:2605.27514) — constructiva, sin cotas
inferiores, sin horizontes; corrobora independientemente la varianza prohibitiva de los invariantes
de curvatura (respaldo externo al terminal de la decisión 046).
```

**Lectura vinculante del veredicto.** El gate de bloqueo del Paso D queda **descargado en el sentido
en que estaba redactado** — la revisión independiente se ha realizado y está documentada. Pero el
resultado es *"no se encontró antecedente"*, que **autoriza a redactar un claim de novedad
cuidadosamente acotado**, y **no** a afirmar novedad como hecho establecido. La diferencia es la
misma que la decisión 046 fija en su `SCOPE_OF_NEGATIVE`, y se aplica aquí a la propia revisión.

## 6. Qué sigue pendiente antes de cualquier envío

1. Incorporar `arXiv:2605.27514` a `biblioteca/` y verificar su texto completo.
2. Resolver la contradicción de WP4 §9 sobre Boguñá-Krioukov (§4.3).
3. Búsqueda en bases indexadas (INSPIRE-HEP como mínimo, por ser la canónica del área) para elevar la
   cobertura por encima de lo que una búsqueda web permite.
4. Redactar el claim de novedad en forma **acotada y comparativa** ("no conocemos antecedente de X;
   el trabajo más próximo es Müller 2025, que difiere en Y"), nunca en forma absoluta.
5. Someterlo a lectura de un experto del área ajeno al proyecto — el repositorio no puede certificar
   su propia novedad, igual que el autor de un claim no es su verificador (regla fundacional).
