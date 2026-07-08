# WP5 — Mapa de ceguera informacional order-only (definition draft)

> **Status: DEFINITION_ONLY / NO_NEW_NUMERICS / NOT_A_PUBLIC_NOVELTY_CLAIM.** Este documento no
> ejecuta código, no genera datos, no modifica ningún seal, y no añade ninguna proposición
> matemática nueva a `research_program/work_packages/wp4_fisher_localization_floor.md` (en
> adelante, "WP4-floor") ni a `research_program/work_packages/wp4_two_point_theorem.md` (en
> adelante, "WP4-twopoint"). Su único contenido es organizativo: define el objeto "mapa de ceguera
> order-only", enuncia (sin demostrar nada nuevo) la asimetría lógica que gobierna su uso, y
> reorganiza los tres regímenes ya probados en WP4 bajo ese marco.
>
> **Relación con el WP5 del roadmap original.** `research_program/README.md` §7 ya reservaba la
> etiqueta "WP5 — Primer lower bound real" para *"ninguna regla order-only en la clase X puede
> localizar la frontera mejor que escala Y en el régimen Z"*. Ese lower bound ya existe: es el
> teorema de §5 de WP4-floor (régimen 3 más abajo). Este documento no es un WP5 distinto que
> compita con esa etiqueta; es la nota de síntesis que ordena ese resultado (y sus dos vecinos
> degenerados) en un mapa único, y fija el vocabulario para los pasos que siguen. Este documento
> **no cierra WP5**: solo organiza, bajo un vocabulario común, una consecuencia ya probada de
> WP4-floor; el paquete de trabajo WP5 en sí sigue abierto y no queda redefinido — ver el roadmap
> de §5 (Pasos B-D, ninguno iniciado). No se ha encontrado ningún fichero WP5 previo con este
> contenido (`wp4_two_point_theorem.md` lleva "WP4/WP5"
> en el título pero es el teorema de dos puntos, no el mapa); este es el único fichero de definición
> de WP5 en el repo.

## 1. Definición: la barrera informacional order-only

**Objeto.** Para una familia paramétrica `theta -> P_n(theta)` de leyes sobre configuraciones de
puntos (con coordenadas/embedding) y su canal order-only inducido `theta -> Q_n(theta)` (ley del
poset no etiquetado, WP4-twopoint §1), la **barrera informacional order-only** es el mapa

`B(theta, theta', n) := "¿son Q_n(theta) y Q_n(theta') indistinguibles a confianza dada, con
todos los estimadores order-only posibles?"`

Es decir: `B` no es un número, es un **objeto unilateral de indistinguibilidad/ceguera** — un
predicado de "no se puede ver", certificado por una cota superior verificable (`TV`, `H^2`, o
`I`), nunca un predicado positivo de "sí se puede ver" (eso requeriría exhibir el estimador, no
solo acotar una divergencia).

**Universal como definición, no universal como cómputo.** `B` está bien definido para *cualquier*
par `(theta, theta')` y *cualquier* `n` — no depende de la familia concreta ni de si es regular en
el sentido de WP4-floor §1. En ese sentido es **medible universalmente**. Pero **no es
universalmente computable**: evaluarlo exige (a) tener una cota manejable de `TV(Q_n(theta),
Q_n(theta'))` (o de un sustituto como `H^2` vía Le Cam, WP4-twopoint §5.3), lo cual solo se sabe
hacer hoy para las familias concretas instanciadas en WP4-floor, y (b) que dicha cota sea
efectivamente pequeña — nada garantiza que lo sea en general. "Universal" describe el dominio de la
definición, no el alcance de lo que hoy se sabe calcular sobre él.

**Dos regiones que no deben confundirse.**

a. **Mapa de ceguera probada** — el conjunto de pares `(theta, theta', n)` para los que existe una
   cota superior *demostrada* de `TV(Q_n(theta), Q_n(theta'))` (o de `H^2`) suficientemente
   pequeña para activar WP4-twopoint Teorema 2. Esta región es la única que este programa puede
   llamar "resultado".
b. **Región candidata a visibilidad** — el complemento, es decir, todo par para el que *no* se ha
   probado una cota de ceguera pequeña. Esta región **no está demostrada visible**: la ausencia de
   una prueba de ceguera no es una prueba de distinguibilidad. Cualquier mapa o figura que se
   produzca a partir de este documento debe rotular esa región como **"candidate visible"** (o
   equivalente explícito), nunca como "visible" o "identificable" a secas — salvo que se exhiba un
   estimador order-only explícito que la alcance (§3 abajo explica por qué eso es un problema
   distinto).

## 2. Lema central: monotonía bajo coarse-graining (points → poset)

**Enunciado (sin demostración nueva; consecuencia de resultados ya usados en WP4).** El canal que
pasa de una configuración de puntos etiquetados con coordenadas a su poset no etiquetado inducido
es una función determinista de los datos (un *estadístico*, en el sentido usual): dado un patch
`(P, g)` que es una caja de coordenadas nulas globales, la Lema 1 de
`research_program/models/first_witness_pair_candidates.md` establece que la ley del poset a
tamaño `n` es función exclusivamente de la cópula de la medida de muestreo normalizada — es decir,
del proceso de puntos "olvidando" todo salvo el orden de rangos.

Por la desigualdad de *data processing* (estándar; ya invocada en WP4-floor §5 — "the poset is a
function of the `n` copula samples ... by data processing" — y en WP4-twopoint §5.3 para las cotas
`TV`/`H^2`/Le Cam), cualquier estadístico de los datos solo puede *contraer* divergencias
estadísticas, nunca expandirlas:

`TV( Q_n(theta), Q_n(theta') ) <= TV( P_n(theta), P_n(theta') )`,

y análogamente para Hellinger, `H^2(Q_n) <= H^2(P_n)` (mismo argumento; usado explícitamente en la
cadena de WP4-floor §5, prueba de (1): `TV(Q^n) <= H_n <= sqrt(n) * (|delta|/2) sqrt(Ibar)`, donde
`Ibar` es información de Fisher **a nivel de punto**, no de poset). Cuando el canal order-only
admite además una expansión QMD propia (no garantizado en general — ver Régimen 2 más abajo, donde
falla incluso a nivel de puntos), la misma contracción vale para la información de Fisher inducida:

`I_ord(theta) <= I_points(theta)`

(monotonía de Fisher/Le Cam bajo estadísticos no suficientes; hecho de libro de texto, no una
proposición nueva de este documento).

**Consecuencia.** Toda cota de Fisher o de `TV` calculada al nivel de puntos (como el `Ibar` de
WP4-floor Proposición 4, o el `kappa = V*Ibar` de la Proposición 6) es **optimista** para el canal
order-only: acota el poset por arriba, nunca por abajo. Esto es exactamente lo que WP4-floor ya
advierte en su propio enunciado ("What the theorem quantifies over", §5): *"The bound holds a
fortiori because it already holds at the point-process level; it can therefore be loose for
posets, and it says nothing about what any estimator achieves."* El Lema central de este documento
no añade nada a esa frase — solo la nombra como principio general y la separa explícitamente de la
dirección opuesta (§3).

## 3. Asimetría lógica obligatoria

La cadena de razonamiento que WP4-floor sí prueba (§5, régimen 3 abajo) da, en unidades físicas
(`ell` = escala de discreteness, WP4-floor §5a):

`ell * sqrt( n * I_points ) << 1  ==>  zona ciega probada`

(vía el Lema central de §2: si el nivel de puntos ya está ciego, el poset —una contracción de esa
información— lo está *a fortiori*).

Pero la cadena **no da, y no puede darse gratis**, la dirección inversa:

`ell * sqrt( n * I_points ) >> 1  ==>  señal order-only suficiente`  — **NO PROBADO.**

La razón estructural es la misma asimetría de la desigualdad de data processing: una cota superior
sobre una divergencia no impone ninguna cota *inferior* sobre la divergencia de una versión
coarse-grained de los mismos datos. Es perfectamente consistente con todo lo probado en WP4 que
`I_points` sea grande y aun así `I_ord = 0` o `TV(Q_n) = 0` — el canal order-only podría destruir
toda la información que distingue `theta` de `theta'`, incluso cuando el nivel de puntos las separa
con holgura. Esto no es una posibilidad remota inventada aquí: es exactamente el "problema de
tightness a nivel poset" que WP4-floor ya deja abierto en dos lugares distintos:

- §6, item 3 ("Poset-level tightness: all distance control is inherited from the point level; a
  technique for bounding poset-law distances *below* the point-level bound ... is still missing");
- §3, "Honesty note" (para el régimen no regular): "whether the poset-level channel attains it is
  unknown".

**Consecuencia obligatoria para cualquier mapa producido bajo WP5.** El lado `ell*sqrt(n*I_points)
>> 1` de cualquier diagrama debe rotularse **"candidate visible"** (§1.b) o con una advertencia
equivalente — nunca "visible", "identificable" o "recuperable" sin calificar. Cerrar esa etiqueta a
"visible" exigiría exhibir un estimador order-only explícito que efectivamente alcance esa
precisión (o una cota inferior de `TV`/`H^2` a nivel de poset, no de puntos) — ninguna de las dos
cosas existe hoy en este repo.

## 4. Reorganización de WP4: los tres regímenes ya probados

Ninguna proposición nueva. Lo siguiente es un índice, no una repetición de las pruebas — ver
WP4-floor para el enunciado y demostración completos de cada una.

**Régimen 1 — Degenerado (`I ≡ 0` / órbita de escala / `TV = 0`).** Familia de récord: caja de
Kruskal fija, parámetro de masa. WP4-floor Proposición 1 (§2): la medida de muestreo normalizada es
*exactamente* independiente de la masa (las coordenadas de Kruskal son ya covariantes de escala),
de modo que `I(t) = 0` idénticamente y la familia es, de hecho, un continuo `TV = 0` exacto — más
fuerte que "ceguera aproximada", ceguera *exacta*. Lectura para el mapa: esta región no necesita
Fisher ni `TV` aproximada; el punto entero (Teorema A, `first_witness_pair_candidates.md`) es un
witness pair exacto.

**Régimen 2 — No regular (movimiento de soporte / QMD falla / suelo vía `TV` directo).** Familia
reparada ingenuamente: caja fija en coordenadas Eddington-Finkelstein. WP4-floor Proposición 2
(§3): la frontera del soporte se mueve a velocidad no nula en `tau`, de modo que
`H^2(p_tau, p_{tau+delta}) >= c_1 |delta|` — Hellinger es de **primer orden**, no de segundo; la
expansión QMD de §1 es falsa y no existe información de Fisher finita en el sentido usual. WP4-floor
Proposición 3 obtiene en su lugar un suelo más débil, de orden `1/n`, directamente por `TV`
(fenómeno clásico de parámetro de soporte, tipo `Uniform[0,theta]`) — no por Fisher, porque Fisher
no está definido aquí. Honestidad ya señalada en WP4-floor: a nivel de punto ese suelo `1/n` podría
no ser ajustado (estimadores de estadístico de orden extremo suelen lograr `1/n`); si el canal
order-only lo alcanza es desconocido.

**Régimen 3 — Regular QMD/Fisher (`I` finita / suelo `1/sqrt(n I)` / `kappa` invariante de
escala).** Familia corregida: diamantes causales con esquinas EF fijas. WP4-floor Lema R + 
Proposición 4 (§4): QMD se cumple, `I(tau)` es finita y continua, `Ibar := sup I(tau) < infinity`.
Proposición 5 (rigidez global): `tau -> c_tau` es inyectiva — `I ≡ 0` en ningún subintervalo. El
Teorema de §5 da el suelo de localización `TV(Q^n) <= (|delta|/2) sqrt(n*Ibar)`, de orden
`1/sqrt(n*Ibar)` — enunciado ya **a nivel de poset** (`Q^n` es la ley del poset, no del proceso de
puntos), obtenido encadenando la cota de Hellinger a nivel de puntos con `Ibar` vía data processing
(§2). Es una cota superior sobre `TV(Q^n)`, no necesariamente ajustada: no implica que ningún
estimador order-only alcance esa precisión (§3).
Proposición 6 (§5a): `kappa(tau) := V(tau)*I(tau)` es **exactamente invariante bajo dilatación** —
depende solo de la forma adimensional del diamante, nunca de su tamaño absoluto — lo que da al
suelo la forma intrínseca `delta_n ~ ell / sqrt(kappa_bar)`.

**Sobre `kappa ~ lambda^6`.** `research_program/work_packages/wp4_kappa_numeric_reference.py` da
una referencia numérica (cuadratura determinista, sin aleatoriedad, sin sprinkling, sin
estimador) de `kappa_bar ~ 8e-4` para una forma de referencia moderada (`~35 ell`), y un ajuste
empírico `kappa_bar ~ lambda^6` (exponente estable `5.9`–`6.0`) al estrechar el diamante hacia el
horizonte. Este documento **no convierte esa observación en teorema**: sigue siendo, exactamente
como la caracteriza WP4-floor §5a/§6, una **observación numérica sobre un ajuste empírico de una
familia concreta de formas**, con una **ruta analítica pendiente** (expansión tipo Rindler cerca
del horizonte), no una derivación. No se ha comparado con ninguna forma real de ningún diagnóstico
de PR004 (WP4-floor ya lo señala como no verificado en ambas direcciones).

## 5. WP5 roadmap

- **Paso A (este documento).** Definición del mapa, del lema de monotonía, y de la asimetría
  lógica. Sin código, sin datos nuevos. **Completado por este commit.**
- **Paso B.** Escáner determinista de formas, extendiendo el método ya existente y verificado de
  `wp4_kappa_numeric_reference.py` (misma cuadratura, mismos chequeos de estabilidad) a una grilla
  sistemática de formas de diamante, en vez de las 3-6 formas puntuales actuales. No es física
  nueva: es cobertura sistemática del mismo cálculo ya validado. **No iniciado.**
- **Paso C.** Derivación analítica del exponente `lambda^6` (ruta sugerida en WP4-floor §5a: 
  expansión cerca del horizonte / tipo Rindler de `I(tau)`). **Abierto, no iniciado.**
- **Paso D.** Revisión bibliográfica independiente — más allá de las cuatro fuentes ya verificadas
  localmente en WP4-floor §9 (Braun 2025, Müller 2025, Madsen 2026, Boguñá-Krioukov 2024) — antes de
  cualquier claim público de novedad. **Condición de bloqueo: ningún claim de novedad pública debe
  emitirse antes de completar este paso.**

## 6. Claims explícitamente prohibidos o marcados como abiertos

**Prohibido afirmar (fuera de alcance de lo probado):**

- Que `ell*sqrt(n*I_points) >> 1` implica señal order-only suficiente o recuperabilidad — solo la
  dirección `<<1 => ciego` está probada (§3).
- Que `kappa ~ lambda^6` es un teorema o una derivación — es observación numérica de un ajuste
  empírico sobre una familia concreta (§4, WP4-floor §5a/§6).
- Que el mapa de ceguera es "universal" sin la aclaración de que es universal *como definición
  medible*, no *como cómputo* (§1).
- Cualquier claim de novedad pública, antes de completar el Paso D del roadmap (§5).
- Que este mapa, `kappa_bar`, o el exponente `lambda^6` corresponden a las formas concretas
  probadas por ningún diagnóstico de PR004 — no verificado en ninguna dirección (WP4-floor §5a,
  "What this suggests, stated carefully").

**Explícitamente abierto (no prohibido, pendiente):**

- `I(tau) > 0` en cada `tau` individual del régimen 3 (fuera de un posible conjunto discreto
  excepcional) — WP4-floor §6 item 1.
- Tightness a nivel de poset: si algún estimador order-only alcanza el suelo `1/sqrt(n*Ibar)` de
  puntos, o si el canal order-only es estrictamente más ciego — WP4-floor §6 item 3; este es
  también el contenido central de la asimetría de §3 de este documento.
- Si el canal order-only alcanza el suelo `1/n` del régimen 2 (familias de soporte) — WP4-floor §6
  item 4.
- Derivación analítica del exponente `lambda^6` (Paso C del roadmap).
- Verificación bibliográfica independiente más allá de las cuatro fuentes ya cotejadas (Paso D).
