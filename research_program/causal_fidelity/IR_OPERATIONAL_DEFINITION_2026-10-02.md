# Fidelidad causal — definición mesoscópica de tiempos y prueba mínima

Fecha: 2026-10-02. Estado: `DRAFT / OPERATIONAL_DEFINITION / NOT_CANONICAL`.
Continuación de `DEFINITION_REPAIR_2026-10-02.md`.
Resultado del caso mínimo: `FAIL_STRICT_INCLUSION`.
No se ejecutan simulaciones, código científico ni nuevos experimentos.

**Lectura posterior del atlas QCA:** §§11–12 distinguen esta definición
operativa de un límite de baja energía y localizan una obstrucción al uso
de `Q=tau` como entrada suficiente. Esta propuesta no cierra el IR físico
del contrato original.

## 1. Qué se define y qué no

Se completa una interpretación **operativa** del test

`T_IR^D1 = T_IR^D2 subsetneq T_caus`.

El único escalar dinámico sigue siendo `Q=tau`, la primera llegada a un umbral
declarado. La regla común pierde resolución temporal mediante bloques de
actualizaciones. No añade un segundo score dinámico, ni obtiene las escalas
de la salida de una dinámica.

Esta definición describe coarse-graining temporal y un límite mesoscópico
del reloj de actualización. No demuestra que ese reloj sea tiempo físico,
que el límite sea un RG de campos, ni que la llegada determine una característica.
La denominación `IR` del test original se interpreta aquí exclusivamente
como este coarse-graining operativo. Su lectura física permanece OPEN.

La elección del esquema siguiente es una propuesta nueva de contrato, no
una definición canónica que ya estuviera en el repositorio. No se afirma que
sea única. Debe revisarse antes de usarla en un resultado confirmatorio.

## 2. Familia y reloj comunes

Antes de evaluar el test se declara una sucesión determinista de posets
finitos con marcas `(C_n;s_n,d_n)`. Se exige `s_n prec d_n`.
Se usa la relación de cobertura y el reloj de una cobertura por actualización
del addendum anterior, con impulso inicial y detector puntual comunes.

Sea

`L_n = {k>=1: exists a saturated chain of k covers from s_n to d_n}`,
`H_n = max L_n`.

La escala de referencia se obtiene sólo de la entrada causal marcada y
se exige `H_n -> infinity`. Un crecimiento de N sin crecimiento de H no
satisface este régimen. Se normaliza por el mismo H para ambas dinámicas.
H no es una longitud física y no utiliza coordenadas de un embedding.

Los conjuntos L_n son el objeto causal temporal **de esta regla de actualización**.
No se identifican con todos los tiempos admisibles de una teoría física.

## 3. Escala de bloques y mapa común

Se fija una sola vez

`b_n = max(1, floor(sqrt(H_n)))`.

Para el paso k se define

`B_n(k) = b_n floor(k/b_n)`,
`g_n(k) = B_n(k)/H_n`.

Todos los pasos de un mismo bloque tienen la misma imagen. El bloque de la
primera llegada se representa por su extremo izquierdo; esa convención no
puede modificarse después de comparar dinámicas. La imagen cero significa
primer bloque, no una respuesta anterior al impulso.

Esta elección satisface `b_n -> infinity` y `b_n/H_n -> 0`: se descarta el
detalle de pocos pasos sin colapsar de antemano toda la escala H a un punto.
El motivo de esta separación de escalas es independiente de la igualdad
buscada. No se calibra b con las respuestas.

La cota uniforme

`0 <= k/H_n - g_n(k) < b_n/H_n`

vale para todos los k admisibles. Elegir otra sucesión entera de bloques con
esas dos propiedades produciría los mismos límites de tiempos normalizados,
si éstos existen. Esto es una estabilidad de este esquema, no una licencia
para seleccionar a posteriori el mejor bloque en una ejecución.

## 4. Respuesta, llegada y ausencia de respuesta

Cada dinámica debe declarar una respuesta real finita `R_D,n(k)` y su
normalización antes de evaluar. Se exige retardación respecto del modelo
de cobertura:

`R_D,n(k)=0 for k not in L_n`,

incluyendo k=0 para marcas distintas y k>H_n. En el candidato lineal del
addendum esto se cumple por construcción. Para otra dinámica sería una
obligación adicional, no un hecho heredado automáticamente.

Se fija `theta>0`, común a las dinámicas, y

`tau_D,n = min {k in {1,...,H_n}: R_D,n(k)>=theta}`,

con valor infinito si no hay llegada. La igualdad con theta cuenta como
llegada. No hay interpolación ni tolerancia numérica; el test es exacto.
Para respuesta no finita, el contrato de evaluación falla antes de emitir
un resultado de igualdad IR.

La entrada dinámica al coarse-graining es sólo `Q_D,n=tau_D,n`.
No se cambia el umbral con n salvo que otro contrato se formule previamente.

## 5. Espacio ambiente y conjuntos finitos

Se usa el espacio compacto

`X = [0,1] disjoint_union {bottom}`,

con distancia euclídea dentro de [0,1], distancia 2 entre bottom y cualquier
punto de [0,1], y distancia cero de bottom a sí mismo. Bottom representa
ausencia de llegada; no es un tiempo causal admisible.

Los objetos comparables son

`K_n = {g_n(k): k in L_n}`,
`J_D,n = {g_n(tau_D,n)}` if tau_D,n is finite,
`J_D,n = {bottom}` otherwise.

No se sustituye ausencia de respuesta por conjunto vacío: eso permitiría
que dos respuestas nulas aparentasen una igualdad e inclusión vacuas.

Si hay llegada, `J_D,n subseteq K_n` porque theta es positivo y la respuesta
es cero fuera de L_n. No se presupone inclusión estricta.
Esta inclusión es consecuencia de la hipótesis de retardación declarada.

## 6. Límite: cuantificadores y orden

El único límite es `n -> infinity` en la familia previamente declarada;
b_n está fijado como función de H_n. No se toma un segundo límite independiente
de bloque o resolución después de inspeccionar datos. Se distingue en el
contrato si el crecimiento de H representa refinamiento, expansión del
dominio u otra construcción: el significado no lo determina N por sí solo.

Se exige convergencia Hausdorff

`K_n -> K` and `J_D,n -> J_D`,

en los subconjuntos compactos no vacíos de X. Hausdorff se calcula con la
métrica de §5: es el máximo de las dos distancias dirigidas entre conjuntos.
K existe sólo si se demuestra su convergencia. La compacidad da subsucesiones,
no permite reemplazar la sucesión por una subsucesión favorable.

Cada J_D,n es un singleton. Si converge, su límite también es un singleton:
`J_D={q_D}`. Una sucesión con infinitas llegadas y ausencias de llegada no
converge en X; no se promedian esos casos para simular una llegada.

La notación **propuesta para la variante operativa**, sin sustituir el
contrato original, es

`T_caus := K`,
`T_IR^D := J_D`.

Ambos son conjuntos del mismo espacio límite. No se compara directamente
J_D con el L_n de una realización finita ni con parejas de eventos.

## 7. Regla exacta PASS / FAIL / OPEN

Para la familia y las dos dinámicas declaradas:

- `PASS_FORMAL`: existen los tres límites, `J_D1=J_D2` y el conjunto común
  es un subconjunto propio de K. Se prueba cada obligación por separado.
- `FAIL`: una obligación del test se refuta en esa familia. Incluye límites
  diferentes, inclusión no válida o igualdad con todo K.
- `OPEN`: falta especificación, prueba de existencia de límite, igualdad,
  inclusión o testigo de estrictitud.

La no existencia demostrada de un límite es FAIL para este contrato;
no disponer aún de una demostración de existencia es OPEN.

Una igualdad exacta no se certifica por proximidad numérica. Un testigo de
estrictitud es un `z in K` con `z not in J_D`, acompañado de su prueba.
Si J_D contiene bottom, no está incluido en K y el test falla.

**Techo lógico:** dado Q=tau, un límite no nulo sólo devuelve un tiempo.
PASS_FORMAL equivale aquí a un tiempo límite común que no agota K. Esa
pérdida puede venir de resumir la historia por su primera llegada; no prueba
que la dinámica haya perdido acceso causal, que las respuestas completas
coincidan en IR, ni que exista una velocidad o frontera universal.
G0–G4 del gate original deben evaluarse además; PASS_FORMAL no certifica
automáticamente esas obligaciones ni su interpretación física.

## 8. Primer caso fijo: refinamiento de una cadena

Se declara la familia `C_n` formada por la cadena de n+1 eventos, con fuente
en el mínimo y detector en el máximo. Es refinamiento del mismo trayecto
operativo con paso normalizado 1/n; no se afirma refinamiento de una métrica.
No hay muestreo ni semillas. `L_n={n}`, `H_n=n`.

Sobre la matriz A_n de cobertura se usa

`X_i,n(0;epsilon)=epsilon e_s`,
`X_i,n(k+1;epsilon)=alpha_i,n A_n X_i,n(k;epsilon)`.

Se fija `theta=1/2`, y las dos especies

`alpha_1,n=1`,
`alpha_2,n=2^(-1/n)`.

El escalado de alpha_2 mantiene la atenuación total a lo largo del trayecto:
`alpha_2,n^n=1/2` para todo n. Cambian sólo los pesos dinámicos, conservando
entrada, fuente, detector, unidad de actualización y normalización de amplitud.
La motivación del escalado es mantener una atenuación finita al refinar.

En el detector la respuesta sólo existe en k=n y vale 1 para D1 y 1/2
para D2. Ambas alcanzan theta exactamente según la convención congelada,
por lo que `tau_1,n=tau_2,n=n`. Las dinámicas tienen respuestas diferentes,
pero el resumen de llegada ya coincide antes del coarse-graining.

Sea `q_n=b_n floor(n/b_n)/n`. Por la cota de §3, `q_n -> 1`. Luego

`K_n=J_1,n=J_2,n={q_n}`,
`K=J_1=J_2={1}`.

**Resultado por deducción:** igualdad de los límites, pero ninguna inclusión
estricta. El test falla en esta familia: `FAIL_STRICT_INCLUSION`.
No es un no-go para otras familias o dinámicas.

## 9. Segunda vía y controles límite

Sin matrices: en una cadena el impulso tarda exactamente n coberturas en
alcanzar el detector. Sólo hay un camino. Su amplitud es el producto de n
pesos, respectivamente 1 y `2^(-n/n)=1/2`. El conjunto causal temporal y
ambas llegadas contienen el mismo único paso. Aplicarles el mismo mapa de
bloques mantiene la igualdad a todo n; cualquier límite existente conserva
esa igualdad. Esto verifica el fallo sin usar una aproximación de amplitudes.

Control de ausencia de respuesta: si se declarara otra especie
`alpha_3,n=4^(-1/n)`, su amplitud final sería 1/4<theta. Entonces
`J_3,n={bottom}`, la inclusión en K falla y no se obtiene un PASS vacío.
Este control es una deducción de borde, no una tercera especie añadida al
test principal después de ver un resultado.

La comparación con D2 también depende del detector/umbral: elevar theta por
encima de 1/2 haría desaparecer su llegada. El umbral no se reajusta; ese
hecho muestra por qué la salida no puede llamarse frente canónico.

## 10. Estado resultante

```text
COMMON_AMBIENT_SPACE = DEFINED
MESOSCOPIC_TIME_MAP = DEFINED
SCALE_PATH = H_TO_INFINITY_B_EQUAL_FLOOR_SQRT_H
LIMIT_MODE = FULL_SEQUENCE_HAUSDORFF
NULL_ARRIVAL = ISOLATED_BOTTOM
SINGLE_DYNAMIC_SCALAR = TAU
FIRST_CHAIN_FAMILY = FAIL_STRICT_INCLUSION_BY_EXACT_DERIVATION
PHYSICAL_IR_INTERPRETATION = OPEN
GENERAL_EQUALITY_AND_STRICTNESS = OPEN
INDEPENDENT_REVIEW = NOT_PERFORMED
CANONICAL_PROMOTION = NONE
```

La definición elimina la ambigüedad de tipos y del orden de límites en esta
propuesta. El caso mínimo la somete a un resultado negativo explícito.
No se elige otra familia para fabricar un PASS ni se modifica el test.
Para investigar una pérdida dinámica genuina, sigue siendo necesario
justificar por qué un único arrival time sería suficiente para ese claim;
el contrato original no contiene esa justificación.

## 11. Qué aporta el atlas QCA y qué puede trasladarse

Repositorio leído sin cambios: `/home/ignac/qca-causal-cones`, commit
`0a4606c61a3f75e5516a245f3837ed009b0a56b4`.
Se consultaron AGENTS, PROJECT_INSTRUCTIONS, el estado canónico en las
secciones aplicables, el índice bibliográfico, FAMILY_BIBLE, PROJECT_NAVIGATION,
F13, THREE_VELOCITIES, SCALED_IR_SIGNALING_GATE y el contrato C2a.

El atlas localiza el antecedente; la afirmación sobre el límite se comprobó
en la fuente primaria `biblioteca/1312.2852v1.pdf`, Farrelly–Short, p.3,
Ecs.12–16. Allí se comparan evoluciones unitaria discreta y continua sobre
estados de momento acotado, con una cota de error que tiende a cero bajo
un escalado declarado de a, delta t y el corte de momento. No es una
comparación de primeras llegadas ni una partición de tiempos.
El corte físico puede crecer mientras el momento respecto de la escala
de red permanece pequeño: no debe copiarse literalmente como un corte
Lambda decreciente sin traducir unidades y régimen.

El contrato propio de QCA `theory/SCALED_IR_SIGNALING_GATE.md` §§1–4
declara conjuntamente corte de momentos, tiempos, regiones, recurso,
encoder y detector. Su versión C2a exige controlar el error dentro del
funcional de respuesta completo. Estos son contratos de otro modelo;
se usa su disciplina de definición, no se transfiere su resultado al poset.

En la propuesta actual faltan un sector de baja energía intrínsecamente
definido y una transferencia controlada de la respuesta a ese sector.
La matriz de cobertura es nilpotente: A^N=0 implica que todos sus
autovalores son cero. Sus autovalores no distinguen por sí solos modos
de baja y alta energía. Tampoco es legítimo introducir Fourier espacial
sin homogeneidad, coordenadas autorizadas o una estructura alternativa
especificada. Un operador de modos adicional sería una nueva obligación.

Conclusión acotada: el atlas no suministra automáticamente esa estructura
para causal sets; ayuda a detectar que §§2–7 sólo definen coarse-graining
del resumen de llegada. `PHYSICAL_IR_INTERPRETATION` permanece OPEN.

## 12. Obstrucción exacta: el arrival time no determina la respuesta espectral

La pérdida no es sólo una advertencia verbal. Considérese el poset de cinco
eventos con dos cadenas saturadas disjuntas salvo extremos:

`s lessdot a lessdot d`,
`s lessdot b lessdot c lessdot d`.

El orden es la clausura transitiva de esas coberturas. Sólo hay un camino
de longitud 2 y uno de longitud 3 entre las marcas.
Con la dinámica ya declarada `X(k+1)=alpha A X(k)`, las únicas respuestas
del detector son

`R_alpha(2)=alpha^2`, `R_alpha(3)=alpha^3`.

Fíjense theta=1/2, alpha_1=1 y alpha_2=3/4. Entonces

`tau_1=tau_2=2`,

pero las respuestas completas son `(1,1)` y `(9/16,27/64)`.
La transformada temporal finita

`F_alpha(omega)=sum_k R_alpha(k) exp(-i omega k)`

tiene en frecuencia cero los valores

`F_1(0)=2`, `F_2(0)=63/64`.

Ninguna función sólo de tau, aplicada con los mismos datos causales y
parámetros comunes, puede recuperar ambos valores: recibe exactamente
la misma entrada. Incluir alpha como dato extra eludiría la obstrucción,
pero dejaría de ser una regla aplicada únicamente al escalar Q y a los
datos comunes. Un filtro que conserve la componente de frecuencia cero
no puede reproducirla universalmente a partir de tau en esta clase.

Segunda vía, incluso normalizando cada historia a masa total uno:
las medias temporales son `5/2` y `17/7`. Por tanto las derivadas en cero
de sus transformadas normalizadas son distintas, aunque tau coincide.
Eliminar la amplitud global no convierte tau en historia espectral suficiente.

Estas son dos deducciones algebraicas exactas de la regla declarada, sin
ejecutar código. La transformada es temporal en el reloj operativo:
no se presenta como espectro de energía físico ni como velocidad de grupo.
La obstrucción se refiere a **Q=tau** y a la reconstrucción universal de
esas respuestas. No afirma que cualquier escalar imaginable sea insuficiente,
ni refuta la igualdad de llegadas para una familia más estrecha.

```text
OPERATIONAL_TIME_LIMIT = DEFINED
PHYSICAL_LOW_ENERGY_SECTOR = NOT_SPECIFIED
RESPONSE_TRANSFER_TO_IR = NOT_SPECIFIED
TAU_SUFFICIENCY_FOR_DC_RESPONSE = REFUTED_IN_DECLARED_FINITE_CLASS
TAU_SUFFICIENCY_FOR_NORMALIZED_FIRST_MOMENT = REFUTED_IN_SAME_CLASS
PHYSICAL_IR_CONTRACT = OPEN
```

Si el objetivo es sólo igualdad de primeras llegadas normalizadas, la variante
operativa queda bien tipada y tiene su primer caso negativo. Si el objetivo
es igualdad de respuestas dinámicas en IR, el contrato debe decidir qué
información de la respuesta conserva y definir su sector lento. Esa ampliación
no se introduce silenciosamente: afecta a la restricción de un único escalar
Q=tau y se registra como decisión de alcance pendiente.

## 13. Continuación autorizada: protocolos lentos

Tras discutir la ampliación, el usuario autorizó su desarrollo con «adelante».
`SLOW_PROTOCOL_RESPONSE_2026-10-02.md` define un sector temporal común
de fuentes y perfiles de lectura y conserva su operador de respuesta lineal.
Demuestra suficiencia exacta para esas lecturas y que el ejemplo de §12
sigue distinguiéndose en el sector lento. El límite de ventana allí mantiene
el poset fijo; no reemplaza el límite de familia de este documento.
La ampliación se propone en un addendum; el contrato histórico permanece
intacto y el sector físico de baja energía sigue abierto.
