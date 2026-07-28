# Instrucción para Grok — búsqueda adversarial de prioridad sobre N1–N5

> **STATUS: SEARCH_INSTRUMENT / NOT_AN_EXTERNAL_REVIEW / DOES_NOT_DISCHARGE_ITEM_5 /
> OUTPUT_IS_LEADS_NOT_VERDICTS.**
> Documento de instrucción para un modelo de lenguaje. Su salida son **pistas bibliográficas a
> verificar**, nunca un veredicto de novedad. No congela nada, no toca el sello, no descarga el ítem 5
> de `research_program/bibliography/wp5_paso_d_independent_novelty_review.md` §6.
>
> FECHA: 2026-07-28 · HEAD `e9744d8`

---

## 0. Nota para el operador (Ignacio) — leer antes de pegar nada

**Qué es esto y qué no es.** El ítem 5 del paso D exige un **lector humano independiente**, y ese
requisito **no lo satisface ningún modelo de lenguaje**, incluido Grok. La regla ya está escrita en el
repo: simular la revisión externa con un sistema automático sería «un guardarraíl que no puede
fallar, es decir, decoración». Este documento **no** intenta esa sustitución.

Lo que Grok sí puede hacer, y un humano ocupado probablemente no hará: **barrer un corpus de
entrenamiento distinto al de la búsqueda interna** y devolver referencias candidatas. Es un
instrumento de *recall*, no de juicio. Por eso la tarea que se le da aquí no es «revise N1–N5» sino
**«encuentre prioridad y dígame qué literatura no hemos peinado»**.

**La asimetría que gobierna el uso de su salida, y que no es negociable:**

| Salida de Grok | Valor evidencial |
|---|---|
| Encuentra una referencia real que contiene un claim | **Alto** — si se verifica en fuente primaria, hunde el claim |
| Nombra una literatura/comunidad sin peinar | **Alto** — cierra el hueco de §3.1 de `external_reader_candidates_n1_n5.md` |
| No encuentra nada | **Cero.** No es evidencia de novedad, exactamente igual que la búsqueda interna |
| Dice que los claims parecen novedosos | **Cero, y es la respuesta peligrosa** — descartarla sin registrarla |

**Riesgo principal: citas inventadas.** El fallo característico de un LLM aquí es producir una
referencia plausible, con autores plausibles y un DOI plausible, que no existe. Una cita inventada
que se cuele en el paquete es **peor que no haber preguntado**, porque contamina un documento que hoy
tiene toda su bibliografía verificada a fuente primaria. De ahí el §3 (protocolo anti-invención) y el
§6 (qué hacer con la salida). **Ninguna referencia que devuelva Grok entra en el repo sin verificarse
contra el PDF.**

**Cómo usarlo:** pegar de §1 a §5 (todo lo que va tras la línea de corte). No pegar esta sección 0.

---8<--- CORTAR AQUÍ: pegar a partir de la línea siguiente ---8<---

## 1. Tu tarea

Eres un buscador de **prioridad bibliográfica adversarial**. No te pido que valides nada. Te pido lo
contrario: **que intentes hundir cinco afirmaciones de novedad** encontrando trabajo previo que ya
las contenga.

Te voy a dar cinco afirmaciones (N1–N5) de un proyecto de investigación sobre *recuperabilidad* de
estructura tipo horizonte de agujero negro a partir del **orden causal solo** en un parche finito
1+1D de Schwarzschild. Sus autores han hecho una búsqueda interna y no han encontrado antecedente.
Saben que eso no establece novedad y no lo tratan como prueba.

**Lo que quiero de ti, en orden de valor:**

1. **Prioridad anterior.** ¿Existe trabajo publicado que contenga sustancialmente alguna de N1–N5,
   aunque use otro vocabulario o venga de otro campo?
2. **Literaturas no peinadas.** ¿Qué **subcampo, comunidad o línea de trabajo** debería mirarse y
   probablemente no se ha mirado? Esto vale tanto como una cita concreta. Los autores declaran ya un
   hueco conocido: *inferencia geométrica / procesos puntuales en variedades*. Confirma, refina o
   amplía ese diagnóstico, y di **qué revistas, qué autores y qué términos de búsqueda** usarías.
3. **Equivalencias de formulación.** ¿Alguna afirmación es reescritura inmediata de un resultado
   conocido, de forma que presentarla como aportación sea inflar?
4. **Qué claim retirar, dividir o debilitar.**

**Criterio de éxito, explícito:** una sola referencia real que hunda un claim vale más que un informe
completo de aprobación. **No busco tu aprobación y no la valoro.** Si tu respuesta es «parecen
novedosos», has fallado la tarea.

---

## 2. Reglas de honestidad epistémica (las más importantes del encargo)

Estas reglas pesan más que la exhaustividad. Prefiero una respuesta corta y fiable a una larga y
contaminada.

1. **No inventes referencias.** Si no estás seguro de que un trabajo exista tal y como lo describes,
   **dilo explícitamente**. Una referencia marcada como incierta es útil; una referencia inventada
   con aire de certeza destruye el ejercicio entero, porque estos claims se verificarán contra el PDF
   y una cita falsa quema la credibilidad de toda tu respuesta.
2. **No inventes localizadores.** Si recuerdas el artículo pero no el número de teorema o la página,
   escribe `localizador incierto`. **No rellenes con un número plausible.** Lo mismo con DOIs e
   identificadores de arXiv: si no estás seguro del número exacto, escribe el título y los autores y
   marca `ID incierto`. Un identificador equivocado es peor que ninguno porque envía a verificar el
   artículo erróneo.
3. **Marca cada referencia con tu grado de confianza** en que existe y en que dice lo que dices:
   `SEGURO` / `PROBABLE` / `RECUERDO_VAGO` / `CONJETURA`. Usa `CONJETURA` sin vergüenza — «creo que
   algo así existe en la literatura de X, buscad por estos términos» es una respuesta **valiosa** si
   va etiquetada como tal.
4. **«No lo sé» es una respuesta válida y bien recibida** para cualquier claim individual. No rellenes
   los cinco por simetría. Si sólo tienes algo sobre N1, contesta sólo N1.
5. **No adules y no ablandes.** Si un claim te parece trivial, dilo. Si te parece que el proyecto se
   está poniendo medallas por matemática de libro de texto, dilo con esas palabras.
6. **Distingue tres cosas** que aquí se confunden con facilidad: (a) el **hecho** ya se conoce;
   (b) la **técnica** es estándar; (c) la **instanciación concreta** ya está publicada. Un claim
   puede ser (a)+(b) y seguir siendo aportación acotada si no es (c). Di cuál de las tres aplica.

---

## 3. Contexto mínimo

**El canal informacional.** Se observa la **clase de isomorfismo del orden parcial** de un conjunto
finito de puntos —un *causal set*, obtenido por sprinkling de Poisson sobre una región del
espaciotiempo— condicionada a la cardinalidad `N = n`. «Order-only» significa: **sin etiquetas, sin
coordenadas, sin volúmenes**, sólo el poset desnudo. El embedding real existe pero sólo se usa para
puntuar, nunca para definir el observable.

**El objetivo.** Localizar estructura tipo horizonte de sucesos en un parche **finito** de
Schwarzschild **1+1D**. No hay claim de reconstrucción métrica, ni de horizonte global, ni de 3+1D.

**Notación.** `TV` = distancia de variación total. `I` = información de Fisher. `Ībar` = información
de Fisher promediada de la familia. `ℓ = ρ^{-1/2}` = escala de discreción. `τ` = parámetro de
posición de un diamante causal. `QMD` = quadratic mean differentiability. EF = Eddington–Finkelstein.

**El pariente publicado más cercano que los autores YA conocen** (no hace falta que lo redescubras):
Olaf Müller, *On the Hauptvermutung of Causal Set Theory*, arXiv:2503.01719, Teorema 2 — construye
pares de geometrías con leyes de orden a `K` puntos indistinguibles (`‖·‖₁ < ε`) vía un bump conforme
de volumen pequeño, con diámetro temporal arbitrariamente distinto. Otros conocidos: Mathias Braun
arXiv:2507.01907 (reconstrucción por orden y número, matrices **etiquetadas**, `d ≥ 3`);
Boguñá–Krioukov PRD 110, 024008 (distancias espaciales vía solapamientos causales, error `~1/√(ρV)`);
Trauthwein–Yukich arXiv:2605.23292 (localización en el espacio de Poisson).

---

## 4. Las cinco afirmaciones

### N1 — Suelo de localización order-only por dos puntos, con familia regular probada

> Para una familia uniparamétrica de diamantes causales de esquinas Eddington–Finkelstein fijas en
> 1+1D Schwarzschild, se prueba regularidad QMD e información de Fisher finita `Ībar < ∞`, y se
> deriva, en el canal order-only condicionado a `N = n`, la cota
> `TV(Q^n_τ, Q^n_{τ+δ}) ≤ (|δ|/2)·√(n·Ībar)`. Por reducción estimación→test, ningún estimador
> order-only —incluidos los aleatorizados— localiza `τ` con precisión `|δ|/2` y confianza `1−ε` en
> ambos extremos si `|δ| < 2(1−2ε)/√(n·Ībar)`.

*Lo que NO afirma:* que la cota sea ajustada (se hereda por *data processing* del nivel de proceso
puntual y puede ser floja para posets); que la maquinaria sea nueva (Le Cam, tensorización de
Hellinger, data processing son de libro); nada sobre 3+1D; que `Ībar` esté calculado (probado finito,
no computado).

*La aportación que se reclama* no es la técnica sino su **instanciación** con una familia cuya
regularidad QMD se **prueba**, en un canal donde la regularidad **no** es automática — dos de las tres
familias que los autores examinaron son degeneradas o no regulares.

**Pregunta directa:** ¿conoces alguna **cota inferior** (minimax, Le Cam, van Trees, Fano, Assouad)
para la estimación de un parámetro **geométrico** a partir del **orden causal no etiquetado** de un
conjunto finito de puntos? ¿Y en literatura de inferencia geométrica **fuera** de gravedad cuántica
—geometría estocástica, grafos aleatorios geométricos, inferencia sobre variedades, procesos
puntuales determinantales, reconstrucción de posets aleatorios?

---

### N2 — Ceguera exacta de escala (`TV = 0`) — *los autores lo declaran como su claim más frágil*

> Para 1+1D Schwarzschild con radio de horizonte `r_s` y parche `P`, y su imagen bajo la dilatación
> `Φ_s` (radio `s·r_s`, parche `Φ_s(P)`), las leyes del poset no etiquetado condicionadas a `N = n`
> coinciden **exactamente**: `TV = 0` para todo `n` y todo `s > 0`. Luego el orden no porta
> información alguna sobre `r_s` **en unidades absolutas**, a cualquier `n` fijo.

*Los autores lo presentan explícitamente como **formalización de folclore conocido*** («Order +
Number»: el orden solo no fija escala), **no** como descubrimiento físico. La demostración son tres
líneas vía covarianza conforme constante. No afirma ceguera a localización *relativa*, ni
indistinguibilidad en el canal order+**número** (con densidad conocida, `N ~ Poisson(ρV)` vs
`Poisson(ρs²V)` los separa a `~1/√n`).

**Pregunta directa:** ¿es correcto tratar esto como folclore formalizado en vez de como resultado?
¿Conoces una **cita explícita** del argumento de órbita de dilatación en causal sets —incluso
informal, en un review, unas notas de curso o una tesis? Los autores consideran **más probable que
exista a que no exista**. ¿Debería degradarse a lema instrumental o eliminarse?

---

### N3 — Diagnóstico de degeneración de la caja de Kruskal

> Sobre una caja de Kruskal **fija**, la medida de volumen normalizada de la métrica 1+1D de
> Schwarzschild es **independiente del parámetro de masa**: con `x := r/2M`, la relación
> `UV = (1−x)e^x` es idéntica para toda `M`, y la dependencia en `M` del factor conforme se reduce al
> factor global `16M²`, que se cancela al normalizar. Por tanto la cópula y la ley del poset a todo
> `n` son independientes de `M`, y la información de Fisher es **idénticamente nula** en forma
> cerrada.

Se reclama como **diagnóstico**: explica por qué la familia «natural» que uno elegiría primero (fijar
una caja de Kruskal y variar la masa) es **estéril**, y por qué el error es fácil de cometer.

**Pregunta directa:** ¿está publicado en algún sitio que las coordenadas de Kruskal fijan el horizonte
en `U = 0` y con ello destruyen la dependencia en la masa de la ley del sprinkling? Es un hecho de
libro de relatividad general; la pregunta es si su **uso como diagnóstico de esterilidad de una
familia estadística** aparece en alguna parte.

---

### N4 — Invariancia bajo dilatación de `κ = V·I` y el suelo en unidades intrínsecas

> Para la familia de diamantes EF, `κ(τ) := V(τ)·I(τ)` es **exactamente invariante bajo dilatación**:
> depende sólo de la forma adimensional del diamante, no de su tamaño absoluto. Luego el suelo admite
> la forma intrínseca `δ_n/ℓ = 1/√(κ̄)` con `ℓ = ρ^{-1/2}`, de modo que «suelo `O(ℓ)`» es una
> propiedad de la **forma**, no un artefacto del tamaño del parche elegido.

*Lo que NO afirma:* que `κ̄` esté calculado analíticamente (hay referencia numérica, marcada
`NUMERICAL, not proved`); que `κ̄` esté acotado inferiormente al estrechar el diamante —empíricamente
`κ̄ ~ λ⁶`, o sea el suelo **empeora** hacia diamantes finos cerca del horizonte.

**Pregunta directa:** el patrón «volumen × información de Fisher = invariante de escala adimensional»
tiene aire de ser un caso particular de algo estándar —geometría de la información, invariancia de
cópulas (teorema de Sklar), análisis dimensional de la métrica de Fisher. ¿Es un corolario inmediato
de un resultado conocido? ¿Existe la combinación `V·I` con nombre propio en alguna literatura?

---

### N5 — «Mapa de ceguera order-only» y la asimetría lógica — *contribución organizativa, no matemática*

> Se organizan los resultados de indistinguibilidad bajo un objeto único, el *mapa de ceguera
> order-only* `B(θ, θ', n)`, y se hace explícita y vinculante la asimetría que lo gobierna:
> `ℓ·√(n·I_points) ≪ 1 ⟹ ceguera probada`, mientras que la dirección inversa
> `≫ 1 ⟹ señal order-only suficiente` **no está probada** y no puede darse gratis, porque una cota
> superior sobre una divergencia no impone cota inferior sobre la divergencia de una versión
> *coarse-grained* de los mismos datos. Luego toda región fuera de la zona ciega probada debe
> rotularse **«candidate visible»**, nunca «visible».

*Los autores declaran que esto **no tiene novedad matemática de ninguna clase***: la monotonía bajo
coarse-graining es la desigualdad de *data processing*, hecho de libro. Lo que se reclama es
**disciplina de presentación**: que la asimetría sea regla vinculante de redacción.

**Pregunta directa:** ¿tiene sentido presentar una disciplina de presentación como contribución en un
paper, o debería ser sólo una nota metodológica de dos frases? ¿Conoces algún trabajo que haya
construido un «mapa» de indistinguibilidad análogo, en cualquier campo, con esta asimetría hecha
explícita?

---

## 5. Formato de respuesta que necesito

Para **cada** referencia que propongas, exactamente estos campos:

```text
CLAIM AFECTADO: N1 / N2 / N3 / N4 / N5
CONFIANZA EN QUE LA FUENTE EXISTE: SEGURO / PROBABLE / RECUERDO_VAGO / CONJETURA
CITA: autor(es), año, título, revista o arXiv (marca «ID incierto» si no estás seguro del número)
LOCALIZACIÓN: sección / teorema / página (marca «localizador incierto» si no lo recuerdas)
QUÉ CONTIENE QUE SOLAPA: y en qué grado — ¿el hecho, la técnica, o la instanciación concreta?
GRADO DE SOLAPAMIENTO: TOTAL / PARCIAL / SÓLO_LA_TÉCNICA / SÓLO_EL_HECHO
RECOMENDACIÓN: retirar / dividir / debilitar / reformular / mantener acotado
```

Y al final, tres bloques breves:

```text
LITERATURAS NO PEINADAS: qué subcampos mirar, con autores, revistas y términos de búsqueda concretos.
Ordena por probabilidad de contener antecedente. Éste es el bloque que más me interesa si no
encuentras citas concretas.

CLAIM MÁS DÉBIL Y CLAIM MÁS FUERTE: tu juicio, con una frase de razón cada uno. Los autores creen
que los más frágiles son N2 y N5 — ¿coincides, o hay uno peor que no han visto?

QUÉ NO PUEDES JUZGAR: dónde se te acaba el conocimiento fiable. Sé concreto; esto me dice a quién
tengo que preguntar de verdad.
```

**Última instrucción, y la más importante de todas:** si en algún punto no tienes conocimiento fiable,
**dilo en vez de rellenar**. La utilidad de tu respuesta se mide por cuántas pistas verificables
produce, no por su extensión, y una sola cita falsa me obliga a descartar el resto.

---8<--- FIN DE LO QUE SE PEGA ---8<---

## 6. Protocolo de tratamiento de la salida (para el operador)

Obligatorio, y en este orden. Ninguna respuesta de Grok entra en el repositorio sin pasar por aquí.

1. **Archivar la respuesta cruda** fuera del repo (es material no verificado), con fecha y versión del
   modelo.
2. **Descartar sin registrar** todo lo que sea aprobación, elogio o «parecen novedosos». Valor
   evidencial cero, por la asimetría del §0.
3. **Para cada referencia propuesta, verificar en fuente primaria antes de cualquier otra cosa:**
   - ¿existe el artículo? (arXiv / DOI / INSPIRE-HEP)
   - ¿son ésos los autores y ese el título?
   - ¿dice en el localizador indicado lo que Grok afirma que dice?
   - **Si falla cualquiera de las tres: descartar la referencia entera y anotar el fallo.** Un patrón
     de citas inventadas es información sobre la fiabilidad de toda la tanda.
4. **Sólo las referencias que sobrevivan los tres filtros** se incorporan, con su localizador
   verificado, a la tabla §7 del paquete adversarial, y obligan a re-evaluar la ficha del claim
   afectado.
5. **El bloque «literaturas no peinadas» se trata aparte**: no necesita verificación de existencia
   porque no es una cita, sino una dirección de búsqueda. Alimenta §3.1 de
   `research_program/bibliography/external_reader_candidates_n1_n5.md`, que hoy declara ese hueco
   abierto por falta de candidato verificado en estadística minimax.
6. **Registro honesto de la procedencia.** Si algo de esta tanda cambia el paquete, el paquete debe
   decir que la pista vino de una búsqueda asistida por LLM y que la fuente se verificó a mano. No se
   presenta como hallazgo bibliográfico propio.

**Lo que este procedimiento NO produce, dicho por última vez:** no produce revisión externa, no
descarga el ítem 5, y un resultado vacío de Grok **no** añade ni un gramo de evidencia a favor de la
novedad de N1–N5. El estado de las cinco afirmaciones sigue siendo `NOT_EXTERNALLY_VERIFIED` pase lo
que pase con esta consulta.
