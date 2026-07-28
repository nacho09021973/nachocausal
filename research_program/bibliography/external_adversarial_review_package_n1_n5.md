# Paquete adversarial para revisión externa — afirmaciones de novedad N1–N5

> **STATUS: REVIEW_PACKAGE / PREPARED_FOR_EXTERNAL_READER / NOT_A_NOVELTY_CERTIFICATE /
> NO_EXTERNAL_REVIEW_HAS_TAKEN_PLACE.**
> Documento de preparación. No ejecuta código, no consume semillas, no toca el sello, no congela
> nada, no emite ningún claim público, y **no** afirma que ninguna revisión externa se haya
> realizado. Su única función es que un investigador independiente pueda **intentar refutar** las
> afirmaciones N1–N5 con el mínimo esfuerzo de contexto.

FECHA: 2026-07-28 · HEAD: `883c6d1` · Árbol: limpio
Sello: `thresholds.py sha256 = 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (intacto)

**Vocabulario epistémico usado en todo el documento (sin excepción):**

| Etiqueta | Significado |
|---|---|
| `ESTABLISHED_BY_PRIMARY_SOURCE` | Verificado leyendo la fuente primaria; se cita con localización |
| `DERIVED_IN_THIS_PROJECT` | Demostrado o calculado dentro del repo, con ancla `file:line` |
| `BOUNDED_NOVELTY_CLAIM` | Afirmación de novedad **acotada y comparativa** que se somete a refutación |
| `POSSIBLE_PRIOR_ART` | Antecedente identificado que podría contener la afirmación, total o parcialmente |
| `NOT_EXTERNALLY_VERIFIED` | Nadie ajeno al proyecto lo ha comprobado |

---

## 1. Carta al revisor

Estimado/a colega:

**No le pedimos que confirme estas afirmaciones. Le pedimos que intente refutarlas.**

Le enviamos cinco afirmaciones (N1–N5) sobre resultados obtenidos en un banco de pruebas de
*recuperabilidad* order-only para estructura tipo horizonte en un parche finito 1+1D de
Schwarzschild. Hemos hecho una búsqueda bibliográfica interna, documentada y con sus límites
declarados, y no hemos encontrado antecedente para ninguna de las cinco. **Sabemos que eso no
establece novedad.** Una búsqueda con resultado cero, hecha por los propios autores, es
exactamente el tipo de guardarraíl que no puede fallar, y por eso no la tratamos como prueba.

Lo que necesitamos de usted es específicamente lo contrario de una validación:

1. **Localizar prioridad anterior.** ¿Existe trabajo publicado que contenga sustancialmente alguna
   de N1–N5, aunque use otro vocabulario?
2. **Detectar equivalencias de formulación.** ¿Alguna de nuestras afirmaciones es una reescritura
   inmediata de un resultado conocido, de modo que enunciarla como aportación sea inflar?
3. **Señalar dónde el contraste con la literatura es más fuerte de lo permitido.** En particular,
   si nuestra comparación con Müller 2025 es infiel o le concede menos de lo que contiene.
4. **Decirnos qué claim retirar, dividir o debilitar.**

Le agradeceríamos especialmente severidad con **N2** y **N5**, que son las dos que nosotros mismos
consideramos más frágiles (§4.2 y §4.5 explican por qué, sin esconderlo).

El material está en §10. El cuestionario y el formulario de veredicto, en §8. No hace falta que
responda a todo: incluso una sola referencia que hunda un claim nos es más útil que un visto bueno
general.

Gracias por el tiempo.

---

## 2. Alcance y límites de la revisión solicitada

**Lo que se somete a revisión:** cinco afirmaciones de novedad **acotadas**, N1–N5, en su
formulación mínima de §4. Nada más.

**Lo que NO se somete a revisión, y no debe leerse como pretendido:**

- No se pide juicio sobre la corrección matemática interna de las demostraciones (aunque si detecta
  un error, dígalo). Se pide juicio sobre **prioridad y solapamiento**.
- No se afirma reconstrucción métrica, ni horizonte de sucesos global, ni resultado 3+1D. El claim
  del proyecto está acotado a **localización order-only en un parche finito 1+1D**
  (`CLAUDE.md`, `docs/claim_grammar.md` §3).
- No se afirma ningún no-go general sobre causal sets. Los negativos del proyecto son de
  construcciones concretas.
- **Ninguna revisión externa se ha realizado hasta la fecha.** Este documento la prepara; no la
  sustituye ni la simula. `NOT_EXTERNALLY_VERIFIED` es el estado de las cinco afirmaciones.

**Sesgo declarado del preparador.** Este paquete lo redacta el mismo proyecto cuyas afirmaciones
somete a examen. Hemos intentado compensarlo marcando explícitamente los puntos débiles (§4.2, §4.5,
§5, §7), pero el sesgo no desaparece por declararlo. Trate cada `BOUNDED_NOVELTY_CLAIM` como
hipótesis del autor, no como resultado.

---

## 3. Resumen ejecutivo de la contribución (en su forma más modesta defendible)

El proyecto es un **banco de recuperabilidad**, no una propuesta de reconstrucción. En un parche
finito 1+1D de Schwarzschild, con canal *order-only* (se observa la clase de isomorfismo del orden
causal, condicionada a cardinalidad `N = n`), el proyecto contiene tres bloques:

1. **Un positivo sellado y pre-registrado** (fuera de N1–N5): un observable order-only de volumen de
   futuro localiza estructura tipo horizonte con un PASS bajo pre-registro congelado
   (`docs/preregistration_002{,_result}.md`).
2. **Un ledger de seis negativos tipados** (fuera de N1–N5): seis vías independientes de
   localización de *región* cerradas, con terminales y anclas (líneas C1–C6, decisiones de comité
   039–046).
3. **Un bloque teórico de cotas de indistinguibilidad** — **este bloque es el que contiene N1–N5**.

La formulación bibliográfica acotada que el proyecto se permite hoy, y que pedimos auditar, es:

> En el corpus primario examinado, los operadores de curvatura causal-set construidos explícitamente
> recuperan el escalar de Ricci y combinaciones de este con sus derivadas. No se verificó una
> construcción explícita de Kretschmann, Riemann² o Weyl² adecuada para Schwarzschild Ricci-flat;
> las fuentes examinadas presentan esa extensión como trabajo no logrado o futuro.

---

## 4. Fichas adversariales N1–N5

### 4.1 N1 — Suelo de localización order-only por dos puntos, con familia regular probada

**(1) Texto exacto propuesto para el paper.**

> Para una familia uniparamétrica de diamantes causales de esquinas Eddington–Finkelstein fijas en
> 1+1D Schwarzschild, probamos regularidad QMD e información de Fisher finita `Ībar < ∞`, y
> derivamos, en el canal order-only condicionado a `N = n`, la cota
> `TV(Q^n_τ, Q^n_{τ+δ}) ≤ (|δ|/2)·sqrt(n·Ībar)`. Por reducción estimación→test, ningún estimador
> order-only —incluidos los aleatorizados— localiza `τ` con precisión `|δ|/2` y confianza `1−ε` en
> ambos extremos si `|δ| < 2(1−2ε)/sqrt(n·Ībar)`. Hasta donde hemos podido comprobar, no conocemos
> un enunciado previo de este tipo —cota inferior de tasa de localización para un parámetro de
> posición de horizonte en el canal order-only de causal sets— y agradeceríamos que se nos señale
> uno.

**(2) Qué afirma.** Que existe un suelo `Ω(1/sqrt(n·Ībar))` para la localización del parámetro `τ`
en esa familia concreta, válido **uniformemente sobre todos los funcionales del poset no etiquetado**
(porque `TV` es por definición el supremo sobre todos ellos).

**(3) Qué NO afirma.** (i) No afirma que la cota sea **ajustada**: se hereda por *data processing*
del nivel de proceso puntual, y el propio anexo dice que "**can therefore be loose for posets, and
it says nothing about what any estimator achieves**"
(`wp4_fisher_localization_floor.md` §5, "What the theorem quantifies over"). (ii) No afirma novedad
de la maquinaria (Le Cam, tensorización de Hellinger, data processing son de libro de texto).
(iii) No afirma nada sobre 3+1D. (iv) No afirma que `Ībar` esté calculado — está probado finito, no
computado para las esquinas de referencia (`wp4_fisher_localization_floor.md` §6, ítem 2).

**(4) Sustento en el repo.** `DERIVED_IN_THIS_PROJECT`.
`research_program/work_packages/wp4_fisher_localization_floor.md` §4 (construcción de la familia y
Lema R), §5 (Teorema y demostración en cuatro pasos: Prop. 4 → tensorización → data processing vía
Lema 1 de `first_witness_pair_candidates.md` → `TV ≤ H`). Chequeos simbólicos commiteados en
`wp4_fisher_localization_floor_symbolic_checks.py` (asserts en `:71`, `:72`).

**(5) Antecedente primario más próximo.** Ninguno en el canal causal-set. Los dos vecinos reales
son: (a) la maquinaria estadística genérica de Le Cam/Hellinger, `ESTABLISHED_BY_PRIMARY_SOURCE`
como técnica de libro; (b) del lado causal-set, Müller 2025 (§5), que produce indistinguibilidad
pero **sin ninguna maquinaria estadística** (verificado a texto completo: `Fisher`, `minimax`,
`Le Cam`, `total variation` = **0 ocurrencias**).

**(6) Diferencia exacta.** Frente a (a): la contribución no es la técnica sino su **instanciación**
con una familia cuya regularidad QMD se prueba, en un canal (poset no etiquetado) donde la
regularidad **no** es automática — dos de las tres familias examinadas en el mismo anexo son
degeneradas o no regulares (§2, §3). Frente a (b): Müller no enuncia tasa alguna.

**(7) Vía de refutación.** Exhibir (i) cualquier trabajo que acote por debajo el error de estimación
de un parámetro geométrico desde órdenes causales finitos; o (ii) literatura de *inferencia
geométrica* / *procesos puntuales en variedades* que cubra este enunciado en generalidad mayor y del
que este sea corolario inmediato; o (iii) mostrar que el paso QMD es estándar para familias de
cópulas y que el resultado es folclore.

**(8) Nivel de confianza actual.** Moderado-alto en que la *instanciación* no está publicada;
**bajo** en que sea profunda. `BOUNDED_NOVELTY_CLAIM`, `NOT_EXTERNALLY_VERIFIED`.

**(9) Evidencia que obligaría a retirar o reducir.** Cualquier cota de tipo Le Cam/van Trees
publicada para estimación de parámetros geométricos desde órdenes parciales aleatorios, o desde
procesos puntuales con estructura de orden. También: una demostración de que la cota es vacua en el
régimen relevante (el prefactor sin calcular es un flanco abierto).

**(10) Pregunta al revisor.** *¿Conoce alguna cota inferior (minimax, Le Cam, van Trees, Fano) para
estimación de un parámetro geométrico a partir del orden causal no etiquetado de un conjunto finito
de puntos? ¿Y en literatura de inferencia geométrica fuera de gravedad cuántica?*

---

### 4.2 N2 — Ceguera exacta de escala (`TV = 0`) — **el claim más frágil, y lo declaramos**

**(1) Texto exacto propuesto para el paper.**

> Para 1+1D Schwarzschild con radio de horizonte `r_s` y parche `P`, y su imagen bajo la dilatación
> `Φ_s` (radio `s·r_s`, parche `Φ_s(P)`), las leyes del poset no etiquetado condicionadas a `N = n`
> coinciden **exactamente**: `TV(P_n(θ), P_n(θ')) = 0` para todo `n` y todo `s > 0`. En consecuencia,
> el orden observado no porta información alguna sobre `r_s` **en unidades absolutas**, a cualquier
> `n` fijo. **Presentamos esto como la formalización exacta de un principio conocido en causal set
> theory —que el orden por sí solo no fija escala ("Order + Number")— no como un descubrimiento
> físico nuevo.**

**(2) Qué afirma.** Un enunciado de ceguera **exacta** (no aproximada), para un par explícito,
válido a todo `n`, con demostración de tres líneas vía covarianza conforme constante.

**(3) Qué NO afirma.** (i) **No afirma novedad física.** El propio repo lo dice, verbatim:
*"This formalizes ... the known CST slogan that order alone carries no scale ('Order + Number' ...).
**It is not a new physical discovery**"* (`first_witness_pair_candidates.md` §2, Remark A1). (ii) No
afirma ceguera a la localización *relativa*: cualquier target en unidades de `ℓ`, del tamaño del
parche o de `sqrt(n)` es invariante bajo `Φ_s` y queda intacto (Remark A2). (iii) **No afirma que el
par sea indistinguible en el canal order+número**: lo es sólo condicionando a `N = n`; con densidad
fundamental conocida, `N ~ Poisson(ρV)` vs `Poisson(ρs²V)` los separa a precisión `~1/sqrt(n)`
(Remark A3).

**(4) Sustento en el repo.** `DERIVED_IN_THIS_PROJECT`.
`research_program/models/first_witness_pair_candidates.md` §2 (Teorema A, demostración completa,
Lemas 0 y 2). Reaparece como Prop. 1 de `wp4_fisher_localization_floor.md` §2 (la caja de Kruskal
fija **es** esta órbita disfrazada).

**(5) Antecedente primario más próximo.** **Doble, y ambos serios.**
(a) `POSSIBLE_PRIOR_ART` **fuerte y admitido por el propio repo**: el principio "Order + Number" es
patrimonio de la disciplina desde sus fundamentos; la afirmación de que el orden no fija escala es
**folclore establecido**. Lo que se ofrece es la formalización como par testigo exacto, no el hecho.
(b) Müller 2025 Teorema 2 (§5): mismo canal, misma métrica salvo factor 2, mismo género de objeto
(par de geometrías con leyes de orden indistinguibles).

**(6) Diferencia exacta.** Frente a (a): sólo la forma —par explícito, `TV` calculada exactamente,
régimen "todo `n` fijo", demostración cerrada—, es decir una diferencia de **rigor y empaquetado**,
no de contenido. Frente a (b), cuatro diferencias verificadas a texto completo (detalle en §5):
`TV = 0` exacto vs `‖·‖₁ < ε` con `ε > 0`; par independiente de `n` vs par que **depende de `K`**;
target `r_s` absoluto vs diámetro temporal / distancia de Gromov–Hausdorff lorentziana; volúmenes
**distintos** (`s²V`) vs volúmenes **iguales** (unidad) — y esta última diferencia **favorece a
Müller**, cuya restricción de volumen unidad es más exigente.

**(7) Vía de refutación.** Localizar cualquier enunciado publicado —incluso informal— de que la
órbita de dilatación de una solución produce leyes de orden idénticas; o mostrar que se sigue en una
línea de la invariancia conforme de la causalidad 2D, que es esencialmente lo que hace nuestra
demostración.

**(8) Nivel de confianza actual.** **Bajo.** Es el claim que menos defenderíamos.
`POSSIBLE_PRIOR_ART`, `NOT_EXTERNALLY_VERIFIED`. Recomendación interna: **no presentarlo como
contribución independiente**, sino como lema instrumental dentro de N1/N3.

**(9) Evidencia que obligaría a retirar o reducir.** Prácticamente cualquier cita explícita del
argumento de dilatación. Consideramos más probable que exista a que no exista.

**(10) Pregunta al revisor.** *¿Es correcto tratar esto como folclore formalizado en vez de como
resultado? ¿Conoce una cita explícita del argumento de órbita de escala en causal sets? ¿Debería
degradarse a lema o eliminarse?*

---

### 4.3 N3 — Diagnóstico de degeneración de la caja de Kruskal

**(1) Texto exacto propuesto para el paper.**

> Sobre una caja de Kruskal fija, la medida de volumen normalizada de la métrica 1+1D de
> Schwarzschild es **independiente del parámetro de masa**: la sustitución `x := r/2M` deja
> `UV = (1−x)e^x` idéntica para toda `M`, y la dependencia en `M` del factor conforme se reduce al
> factor global `16M²`, que se cancela al normalizar. Por tanto la cópula, la ley del poset a todo
> `n`, y la información de Fisher `I(t) ≡ 0` son independientes de la masa: la familia "caja de
> Kruskal fija con parámetro de masa" es degenerada y **coincide con la órbita de escala de N2**.

**(2) Qué afirma.** Que una elección de familia que parecía natural para estudiar localización de
horizonte es **vacía de información**, y por qué exactamente.

**(3) Qué NO afirma.** No afirma nada sobre la geometría de Kruskal que no sea la conocida
invariancia de escala de esas coordenadas. Es un **diagnóstico de diseño experimental**, no un
resultado geométrico.

**(4) Sustento en el repo.** `DERIVED_IN_THIS_PROJECT`.
`wp4_fisher_localization_floor.md` §2, Proposición 1, con demostración completa y la lectura
explícita de que la intuición previa del propio proyecto ("el horizonte se mueve dentro de la caja")
**era falsa**.

**(5) Antecedente primario más próximo.** La invariancia de escala de las coordenadas de Kruskal es
`ESTABLISHED_BY_PRIMARY_SOURCE` en cualquier texto de relatividad general. No hemos encontrado
antecedente de su uso como **diagnóstico de degeneración de una familia estadística** en causal
sets.

**(6) Diferencia exacta.** El hecho geométrico es conocido; su consecuencia estadística —`I ≡ 0`, y
por tanto la inutilidad de esa familia como banco de localización— es lo que se ofrece.

**(7) Vía de refutación.** Mostrar que alguien ya descartó esa familia por esta razón, o que el
punto es obvio para quien conozca las coordenadas.

**(8) Nivel de confianza actual.** Moderado en que no esté escrito; **bajo** en su peso como
contribución. `BOUNDED_NOVELTY_CLAIM` de valor metodológico, no científico.
`NOT_EXTERNALLY_VERIFIED`.

**(9) Evidencia que obligaría a retirar o reducir.** Cualquier trabajo que discuta la elección de
parche para inferencia en causal sets y señale esta degeneración.

**(10) Pregunta al revisor.** *¿Merece esto mención propia, o basta una nota a pie dentro de N1
explicando por qué la familia de diamantes EF sustituyó a la caja de Kruskal?*

---

### 4.4 N4 — Invariancia bajo dilatación de `κ = V·I` y el suelo en unidades intrínsecas

**(1) Texto exacto propuesto para el paper.**

> Para la familia de diamantes EF, `κ(τ) := V(τ)·I(τ)` es **exactamente invariante bajo dilatación**:
> depende sólo de la forma adimensional del diamante y no de su tamaño absoluto. En consecuencia el
> suelo de §5 admite la forma intrínseca `δ_n/ℓ = 1/sqrt(κ̄)` con `ℓ = ρ^{-1/2}` la escala de
> discreción, de modo que el enunciado "suelo `O(ℓ)`" es una propiedad de la **forma**, no un
> artefacto del tamaño del parche elegido.

**(2) Qué afirma.** Que el suelo se puede escribir en unidades de la escala de discreción con una
constante que es un **funcional de forma puro**, y por tanto que el enunciado no degenera al agrandar
o encoger las esquinas.

**(3) Qué NO afirma.** (i) No afirma que `κ̄` esté calculado analíticamente — la referencia numérica
existe (`wp4_kappa_numeric_reference.py`) pero el propio anexo la marca `NUMERICAL, not proved`.
(ii) **No afirma que `κ̄` esté acotado inferiormente al estrechar el diamante**: empíricamente
`κ̄ ~ λ⁶`, es decir el suelo **empeora** hacia diamantes finos cerca del horizonte
(`wp4_fisher_localization_floor.md` §6, ítem 2). (iii) No afirma relación alguna con el `K_LOC`
medido de `prereg-003`, que es otra cantidad.

**(4) Sustento en el repo.** `DERIVED_IN_THIS_PROJECT`.
`wp4_fisher_localization_floor.md` §5a: Lema de covarianza exacta bajo dilatación (5 pasos, con
verificación simbólica commiteada) y Proposición 6.

**(5) Antecedente primario más próximo.** La invariancia de las cópulas bajo reparametrización
monótona por coordenada es el **teorema de Sklar**, `ESTABLISHED_BY_PRIMARY_SOURCE` y textbook. El
análisis dimensional (`[I] = 1/L²`, `[V] = L²`) es elemental.

**(6) Diferencia exacta.** Ninguna en las herramientas. Lo ofrecido es que la combinación
`V·I` es **exactamente** invariante (no sólo asintóticamente) para esta familia, y su lectura física
como "el suelo es una propiedad de forma". Es plausible que un lector experto lo considere inmediato.

**(7) Vía de refutación.** Mostrar que se sigue en dos líneas de Sklar + análisis dimensional para
cualquier familia con `det g = −1`, y que por tanto no merece proposición propia.

**(8) Nivel de confianza actual.** **Bajo-moderado.** Sospechamos que es "inmediato una vez
planteado". `BOUNDED_NOVELTY_CLAIM` débil, `NOT_EXTERNALLY_VERIFIED`.

**(9) Evidencia que obligaría a retirar o reducir.** Un argumento de una línea que lo derive de
covarianza general, o literatura de inferencia con invariancia de escala donde el fenómeno sea
estándar.

**(10) Pregunta al revisor.** *¿Es la invariancia de `V·I` bajo dilatación un corolario inmediato
de Sklar más análisis dimensional? ¿Debería absorberse dentro de N1 como observación?*

---

### 4.5 N5 — El "mapa de ceguera order-only" y la asimetría lógica — **contribución organizativa, no matemática**

**(1) Texto exacto propuesto para el paper.**

> Organizamos los resultados de indistinguibilidad bajo un objeto único —el *mapa de ceguera
> order-only* `B(θ, θ', n)`— y hacemos explícita y vinculante la asimetría lógica que lo gobierna:
> `ℓ·sqrt(n·I_points) ≪ 1 ⟹ ceguera probada`, mientras que la dirección inversa
> `≫ 1 ⟹ señal order-only suficiente` **no está probada** y no puede darse gratis, porque una cota
> superior sobre una divergencia no impone cota inferior sobre la divergencia de una versión
> *coarse-grained* de los mismos datos. En consecuencia, toda región del mapa fuera de la zona ciega
> probada debe rotularse **"candidate visible"**, nunca "visible". **Presentamos esto como
> disciplina de presentación y organización, no como resultado matemático nuevo.**

**(2) Qué afirma.** Que la asimetría debe ser una **regla de redacción vinculante**, y que en este
dominio concreto es fácil violarla sin darse cuenta.

**(3) Qué NO afirma.** **No afirma novedad matemática de ninguna clase.** La monotonía bajo
*coarse-graining* es la desigualdad de *data processing*; el propio documento fuente la califica de
*"hecho de libro de texto, no una proposición nueva de este documento"*
(`wp5_order_only_blindness_map_definition.md` §2).

**(4) Sustento en el repo.** `DERIVED_IN_THIS_PROJECT` sólo en el sentido organizativo.
`wp5_order_only_blindness_map_definition.md` §§1–3, y su §6 lista explícitamente los claims
prohibidos.

**(5) Antecedente primario más próximo.** Data processing (Blackwell / Le Cam), y la práctica
estadística estándar de no confundir "no se ha probado indistinguibilidad" con "es distinguible".
`ESTABLISHED_BY_PRIMARY_SOURCE`, textbook.

**(6) Diferencia exacta.** Ninguna a nivel de teorema. La única diferencia posible es de **aplicación
disciplinar**: convertirlo en criterio de rotulado obligatorio de figuras y regiones en este
subcampo.

**(7) Vía de refutación.** Trivial: señalar cualquier texto de teoría de la información que ya lo
enuncie. Esperamos que existan muchos.

**(8) Nivel de confianza actual.** **Muy bajo como novedad**; alto como práctica útil.
`POSSIBLE_PRIOR_ART` masivo y asumido, `NOT_EXTERNALLY_VERIFIED`.

**(9) Evidencia que obligaría a retirar o reducir.** Ya está reducido al mínimo. Si el revisor lo
considera obvio, se elimina como claim y permanece sólo como nota metodológica.

**(10) Pregunta al revisor.** *¿Tiene sentido mencionarlo siquiera, o es condescendiente con el
lector? Si se menciona, ¿cuál es la cita canónica correcta para la asimetría?*

---

## 5. Comparación con Müller 2025

**Fuente:** Olaf Müller, *On the Hauptvermutung of Causal Set Theory*, arXiv:2503.01719v2
(math.DG, 29 dic 2025). PDF local: `biblioteca/2503.01719v2.pdf`. **Verificado a texto completo en
esta sesión** (3 652 palabras extraídas; conteos y enunciados leídos directamente, no inferidos del
abstract).

**Su Teorema 2, verbatim** (`:124-126`):

> **Theorem 2 (The finite Hauptvermutung is wrong for `d⁻`)** Let `K ∈ N`. Let `ε ∈ (0;1)`. For each
> `D > 0` there are `X, Y ∈ CS` with `vol(X) = 1 = vol(Y)`, `∂±X = ∂±Y`, `d⁻(X,Y) > D` and
> `‖C_K(X) − C_K(Y)‖₁ < ε`.

**Su canal, verbatim** (`:108-110`): `M_K` es el conjunto de medidas de probabilidad sobre `Q_K`
**invariantes bajo permutaciones**; y para la **medida producto** `µ^K` sobre `X^K`,
`C_K(X)(q) := µ^K(A_q(X))`.

| Dimensión | Este trabajo | Müller 2025 | Diferencia potencialmente novedosa | Riesgo de solapamiento |
|---|---|---|---|---|
| **Proceso de muestreo** | Sprinkling de Poisson condicionado a `N=n` ⇒ `n` i.i.d. de la medida de volumen normalizada (FWP Lema 0) | Medida producto `µ^K` sobre `X^K` ⇒ `K` i.i.d. (`:109-110`). `Poisson`/`sprinkl`: **0 ocurrencias** | Ninguna en sustancia: **es el mismo canal**. Sólo difiere el encuadre (él nunca lo llama sprinkling) | **ALTO** |
| **Objeto observado** | Clase de isomorfismo del orden no etiquetado | Medidas invariantes bajo permutación sobre órdenes de `K` puntos (`:108`) | Ninguna | **ALTO** |
| **Métrica de cercanía** | `TV` | Norma `L¹` (`:123`); `TV = ½‖·‖₁` | Ninguna salvo factor 2 | **ALTO** |
| **Grado de indistinguibilidad** | `TV = 0` **exacto** (N2) | `‖·‖₁ < ε` con `ε ∈ (0;1)` arbitrario pero **> 0** | Exacto vs aproximado — diferencia real | Medio |
| **Dependencia del par en el tamaño de muestra** | El par de N2 es **independiente de `n`**: una órbita sirve a todo `n` | El par **depende de `K`**: la prueba elige `v` con `(1−v)^K > ε` (`:133`) | Uniformidad en `n` — diferencia real y a nuestro favor | Medio |
| **Volumen de los dos modelos** | **Distintos** (`V` vs `s²V`); por eso el canal order+número los separa vía `N` (Remark A3) | **Iguales** (`vol = 1 = vol`) | La restricción de Müller es **más exigente**; aquí la diferencia **nos perjudica** | **ALTO (en contra)** |
| **Target geométrico** | Radio de horizonte `r_s` absoluto (N2); parámetro de localización `τ` (N1) | Diámetro temporal / distancia de Gromov–Hausdorff lorentziana `d⁻` (`:121-123`) | Target de horizonte vs target de distancia — diferencia real | Bajo |
| **Mecanismo** | Difeomorfismo de dilatación exacto (factor conforme constante) | Factor conforme tipo *bump* en vecindad delgada de un maximizador (`:135-137`) | Mecanismos distintos | Bajo |
| **Maquinaria estadística** | Fisher / QMD / Hellinger / Le Cam (N1) | **Ninguna**: `Fisher`, `minimax`, `Le Cam`, `total variation` = **0 ocurrencias** cada uno | Toda N1 | **BAJO** |
| **Tasa / cota de localización** | Suelo `Ω(1/sqrt(n·Ībar))` (N1) | No hay enunciado de tasa | Toda N1 | **BAJO** |
| **Horizonte / Schwarzschild** | Es el objeto | `Schwarzschild`, `horizon` = **0 ocurrencias** | Contexto físico distinto | **BAJO** |

**Lectura honesta de la tabla.** El solapamiento con Müller es **alto en el canal y en la métrica, y
bajo en el aparato estadístico y en el target**. Esto perjudica sobre todo a **N2** —que comparte
canal, métrica y género de enunciado, y sólo gana en exactitud y uniformidad en `n`, mientras pierde
en la restricción de volumen— y apenas afecta a **N1**, cuyo contenido (regularidad probada + tasa)
Müller no toca en absoluto.

**No verificado en Müller (`NOT_VERIFIED`, no inferir del resumen ni del título):** su Teorema 1
(Hauptvermutung numerable) no se ha leído en detalle; su categoría `CS` y la definición de `d⁻` se
han leído sólo en la medida necesaria para la tabla; no se ha auditado si algún pasaje suyo contiene
una observación de escala equivalente a N2. **Ese último punto es exactamente lo que pedimos
comprobar al revisor.**

---

## 6. Estado del arte y límites de la búsqueda

Crónica completa y auditable en
`research_program/bibliography/wp5_paso_d_independent_novelty_review.md`. Resumen para no perder el
foco:

**Bases y fuentes consultadas.** (i) Búsqueda web general, 9 formulaciones de consulta en inglés
deliberadamente variadas; (ii) **INSPIRE-HEP** vía su API pública, 8 consultas sobre campo
`abstract`; (iii) lectura a texto completo de tres PDFs primarios
(`2605.27514`, `2301.13525`, `2503.01719`); (iv) el fondo local `biblioteca/` (~156 ficheros).

**Familias de consulta.** causal set × {Fisher information, minimax, Le Cam, lower bound, total
variation, identifiability, estimation}; sprinkling × estimation × geometry; horizonte discreto ×
límite de resolución; invariancia de escala × masa × indistinguibilidad.

**Resultados genuinamente próximos.** Sólo tres: Müller 2025 (§5); Eichhorn–Mack–Le–Wagner 2026
(`arXiv:2605.27514`), constructivo y sin cotas inferiores; de Brito–Eichhorn–Pfeiffer 2023
(`arXiv:2301.13525`, revisado por pares), que construye invariantes de curvatura de orden superior
de la forma **`R² − 2□R`** y explícitamente **no** construye el invariante de Riemann/Weyl².

**Falsos positivos importantes, para que el revisor no los persiga.** Las consultas INSPIRE con
"Fisher information" y "minimax" devuelven `2502.09894` (cono de entropía holográfica) y `2106.12585`
(*Lorentzian threads*): en ambos "causal set" **no denota el objeto de causal set theory**. Es el
único cruce léxico y es espurio.

**Alcance y límites de las 8 consultas INSPIRE.** Se buscó sobre **campo `abstract` únicamente**, no
sobre texto completo ni sobre referencias citantes. Un trabajo que haga esto sin nombrarlo en el
abstract **no aparecería**. Tampoco se consultaron MathSciNet, zbMATH, Scopus, Web of Science, actas
de congresos ni tesis.

**REV Fase 2 (2026-07-28).** Se ejecutó un peinado **abstract-level** adicional de math.ST/PR
(consultas Q1–Q3 en `phase2_novelty_and_item5.md` §2: Le Cam/two-point × Poisson; minimax
intensidad; Fisher × cópula). Resultado: vecinos de **método** (p.ej. Ray–Schmidt-Hieber
arXiv:1608.01824; Polyanskiy–Wu arXiv:1902.05616), **ningún sink** de la instanciación N1
(order-only poset, familia diamante EF / parámetro de localización Schwarzschild 1+1). MathSciNet
completo y lectura a texto completo de la cola ST **siguen abiertos** — flanco del lector Tier B.

> **Advertencia expresa, vinculante.** Cero resultados **no certifica novedad**. Todo lo anterior
> establece únicamente que *nosotros* no encontramos antecedente con *estos* medios. Convertir eso en
> una afirmación de novedad sería precisamente el error que este paquete existe para evitar.

---

## 7. Tabla de antecedentes potenciales

> **REV Fase 2 (2026-07-28).** Anclas V1–V9 de
> `research_program/bibliography/phase2_novelty_and_item5.md` §1
> (`LLM_LEAD_HUMAN_VERIFIED` donde aplica). Adjudicación de programa Fase 0:
> N2=lema, N3=remark, N4=corolario dimensional, N5=retirado como contribución,
> N1=instanciación acotada. Log ST/PR abstract-level: mismo doc §2
> (`NO_N1_SINK_FOUND` / `NOVELTY_NOT_CERTIFIED`).

| Antecedente | Estado de verificación | Afecta a | Riesgo |
|---|---|---|---|
| Folclore "Order + Number" (el orden no fija escala) | `ESTABLISHED_BY_PRIMARY_SOURCE` — **localizadores**: Dowker–Zalel arXiv:1703.07556 §1.1 (V1); Madsen arXiv:2607.05840 intro (V2); Braun arXiv:2507.01907 §§3.3–3.4 (V3); repo FWP Remark A1 | **N2** (ahora **lema**, no contribución) | **Muy alto** como novedad; **bajo** si se presenta como lema |
| Zeeman / Bombelli 1987 PhD (dilataciones en isomorfismos causales Minkowski) | `ESTABLISHED_BY_PRIMARY_SOURCE` en `biblioteca/derived-md/` (V6) | **N2** (precursor continuo de órbita de escala) | Alto sobre el *hecho* continuum; no sustituye TV=0 a `N=n` |
| HKMM 1976; Malament 1977 | `ESTABLISHED_BY_PRIMARY_SOURCE` (V4–V5; vía refs Braun) | **N2** continuum conformal | Alto sobre escala ausente del orden continuum |
| Müller 2025, Teo. 2 (arXiv:2503.01719) | Texto completo leído (V8) | **N2**, marginalmente N1 | Alto para N2 como “único resultado”; contrastar con TV=0 exacto / target distinto |
| Teorema de Sklar + análisis dimensional \(V\cdot I\) | Textbook + deflación Fase 0/2 | **N4** (corolario, no teorema de novedad) | Alto si se vende como novedad |
| Data processing (Blackwell / Le Cam) | Textbook | **N5** (retirado como contribución) | Muy alto si se vende como novedad |
| Le Cam / Tsybakov (método de dos puntos) | Textbook; `biblioteca/Tsybakov_Nonparametric_Estimation.pdf` (V9) | **N1** (maquinaria, no instanciación) | Alto sobre la técnica, bajo sobre la instanciación *salvo* prior ST no hallado aún |
| Invariancia de escala de coordenadas Kruskal | Textbook GR | **N3** (remark de diseño) | Alto sobre el hecho, bajo sobre el uso diagnóstico |
| de Brito–Eichhorn–Pfeiffer 2023 (`R² − 2□R`) | Texto completo + verificación visual del abstract | Contexto de curvatura; no compite con N1–N5 | Bajo |
| Eichhorn–Mack–Le–Wagner 2026 | Texto completo | Contexto; su medida de distinguibilidad es heurística, sin `TV` | Bajo |
| Braun 2025, Madsen 2026, Boguñá–Krioukov 2024 | Verificados en `wp4_fisher_localization_floor.md` §9; B-K también V7 | Lado positivo/constructivo; B-K = anverso de tasas | Bajo como sink de N1 |
| Vecinos ST de método (Ray–Schmidt-Hieber arXiv:1608.01824; Polyanskiy–Wu arXiv:1902.05616; …) | Abstract-level Fase 2 log Q1–Q2 | **N1** técnica | Medio — no son el teorema del canal poset |
| **Literatura minimax / geometric inference / shape / cópulas (profundidad ST)** | **Peinado abstract-level Fase 2** (`phase2_novelty_and_item5.md` §2); **sin sink de N1 hallado**; MathSciNet completo **no** ejecutado | **N1** (e N4 conceptual) | **Desconocido residual — flanco del ítem 5 Tier B** |

---

## 8. Cuestionario y formulario de veredicto

### 8.1 Preguntas

1. ¿Existe un antecedente que contenga **sustancialmente** N1, N2, N3, N4 o N5?
2. ¿Alguna afirmación es una **reformulación inmediata** de un resultado conocido?
3. ¿La comparación con Müller 2025 (§5) es **fiel**? ¿Le concedemos menos de lo que contiene?
4. ¿Qué claim debería **retirarse, dividirse o debilitarse**?
5. ¿Qué **literatura primaria esencial falta** — en particular fuera de gravedad cuántica?
6. ¿Qué afirmación, si alguna, parece **defendible como contribución propia acotada**?

### 8.2 Formulario

Marque una casilla por claim. `APPARENTLY_DISTINCT` = no le consta antecedente (no equivale a
novedad). `PARTIAL_OVERLAP` = coincide en parte. `KNOWN_RESULT` = está publicado o es folclore.
`INSUFFICIENT_EVIDENCE` = no puede juzgar con lo aportado. `NEEDS_REFORMULATION` = puede sostenerse
pero no como está escrito.

| Claim | APPARENTLY_DISTINCT | PARTIAL_OVERLAP | KNOWN_RESULT | INSUFFICIENT_EVIDENCE | NEEDS_REFORMULATION |
|---|:--:|:--:|:--:|:--:|:--:|
| **N1** suelo Fisher/dos puntos | ☐ | ☐ | ☐ | ☐ | ☐ |
| **N2** ceguera exacta de escala | ☐ | ☐ | ☐ | ☐ | ☐ |
| **N3** degeneración de Kruskal | ☐ | ☐ | ☐ | ☐ | ☐ |
| **N4** `κ = V·I` invariante | ☐ | ☐ | ☐ | ☐ | ☐ |
| **N5** mapa de ceguera | ☐ | ☐ | ☐ | ☐ | ☐ |

**Espacio para el revisor** (una entrada por claim que no marque `APPARENTLY_DISTINCT`):

```text
CLAIM:
CITA (autor, año, título, DOI/arXiv, localización exacta — sección/teorema/página):
EXPLICACIÓN (qué contiene esa fuente que solapa, y en qué grado):
RECOMENDACIÓN (retirar / dividir / debilitar / reformular / mantener acotado):
```

**Valoración global** (opcional):

```text
¿Hay algún claim que, en su opinión, sí constituya una contribución acotada publicable?
¿Qué literatura añadiría antes de someter?
Otros comentarios:
```

---

## 9. Consecuencias previstas para §6 del paper

`§6` de `docs/paper_outline_c1c6_plus_prereg002.md` es *"La conclusión estructural transversal"*, con
la adenda **§6.1** que aloja el bloque de cotas de indistinguibilidad. **No se redacta aquí la §6
definitiva.** Se proponen tres estructuras condicionadas, según la respuesta del revisor:

**(A) Si los claims sobreviven** (mayoría `APPARENTLY_DISTINCT`, N1 incluido). §6.1 se escribe como
*tercera contribución* con N1 al frente y una tasa como resultado principal; N2/N3 pasan a lemas
instrumentales; N4 a observación dentro de N1; N5 a nota metodológica en §2. La formulación
bibliográfica acotada de §3 entra literal, con Müller citado y distinguido en el cuerpo, no en nota.

**(B) Si sobreviven parcialmente** (N1 se sostiene, N2/N4/N5 caen o se debilitan). §6.1 se reduce a
un único enunciado —el suelo de localización— con toda la maquinaria presentada explícitamente como
estándar y la contribución declarada como *instanciación en un canal donde la regularidad no es
automática*. El resto pasa a apéndice técnico sin pretensión de novedad. **Este es el escenario que
consideramos más probable.**

**(C) Si se encuentra prioridad anterior** para N1. §6.1 desaparece como contribución y se reescribe
como *sección de posicionamiento*: "estos resultados ya se conocen en la forma X; los reobtenemos en
el canal Y y los usamos para acotar el alcance de nuestro positivo sellado". El paper conserva
intactos sus otros dos bloques —el positivo pre-registrado y el ledger de seis negativos tipados—,
que **no dependen de N1–N5**. Conviene decirlo desde ahora: **el paper no se cae si N1–N5 caen.**

---

## 10. Materiales mínimos a entregar al revisor

Orden de lectura sugerido; total ≈ 25 páginas más tres PDFs externos.

1. **Este documento** (`external_adversarial_review_package_n1_n5.md`) — autocontenido para §§1–8.
2. `research_program/work_packages/wp4_fisher_localization_floor.md` §§2, 4, 5, 5a — sustento de
   N1, N3, N4, con demostraciones.
3. `research_program/models/first_witness_pair_candidates.md` §2 — Teorema A y sus Remarks A1–A3
   (sustento de N2, **incluida la auto-degradación de A1**).
4. `research_program/work_packages/wp5_order_only_blindness_map_definition.md` §§1–3, 6 — N5.
5. `research_program/bibliography/wp5_paso_d_independent_novelty_review.md` — crónica de búsqueda
   con sus límites.
6. **Externos** (no redistribuibles; referencias): Müller arXiv:2503.01719v2;
   de Brito–Eichhorn–Pfeiffer arXiv:2301.13525 (EPJ Plus 138:592);
   Eichhorn–Mack–Le–Wagner arXiv:2605.27514.

**Opcional, sólo si el revisor quiere contexto del proyecto:** `docs/claim_grammar.md` §3 (frontera
de claims) y `docs/paper_outline_c1c6_plus_prereg002.md` (dónde encajarían N1–N5).
