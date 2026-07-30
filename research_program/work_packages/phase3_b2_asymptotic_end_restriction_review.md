# Fase 3 B2 — exploración falsificable: restricción a geometrías de extremo asintótico único

> **STATUS: FALSIFIABLE_EXPLORATION / WORK_DATE_2026-07-29 / NOT_A_COMITE_ACTA /
> DOES_NOT_MODIFY_DECISION_048 / DOES_NOT_MODIFY_PREOPENING_CONTRACT / TARGET_NOT_ADOPTED /
> WITNESS_PAIR_NOT_CONSTRUCTED / NO_CODE / NO_SIMULATION / NO_SEEDS / PR_1_UNTOUCHED /
> COMITE_NOT_RECONVENED.**
>
> Revisión de trabajo del chair, separada de
> `research_program/work_packages/phase3_b2_decision048_conditions_review.md` (que queda intacto,
> ya versionado en el commit `5924b6b`). Evalúa una única propuesta de reparación de la condición 1:
> restringir \(S_{\rm adm}(g,U)\) a geometrías con un único extremo asintótico, como la mejor
> tentativa antes de abandonar \(Q_{\mathrm{FMOTS}}\). No modifica
> `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md` ni
> `docs/comite/comite_decision_048_q-fmots-target-adjudication.md`. No construye el par testigo, no
> escribe código, no ejecuta simulaciones ni reserva semillas.

## 0. La propuesta

Para cada \(S\in S_{\rm adm}(g,U)\), exigir que exista una loncha \(\Sigma\) con

\[
\Sigma\setminus S = \Omega_{\rm in}\ \dot\cup\ \Omega_{\rm out},
\qquad \overline{\Omega_{\rm in}}\text{ compacta},\qquad
\Omega_{\rm out}\text{ contiene el único extremo asintótico},
\]

y definir el rayo nulo exterior como el que apunta hacia \(\Omega_{\rm out}\). El objetivo es
excluir estructuralmente el contraejemplo \(S^3\) de
`phase3_b2_decision048_conditions_review.md` (donde ambos lados son compactos y no hay asimetría
topológica que rompa el empate) sin recurrir a una componente distinguida de \(\partial U\), que el
PI señaló como más riesgosa ("convierte 'exterior' en 'hacia el borde artificial de observación'").

**Pregunta decisiva planteada por el PI:** ¿ese extremo pertenece realmente a la estructura
geométrica declarada de \((g,U)\), o introducirlo convierte \(Q(g,U)\) en un target dependiente de
información exterior a \(U\)?

## 1. Primer obstáculo, previo a cualquier comprobación: un extremo es una noción de espacio no compacto

La formulación de \(S_{\rm adm}\) ya vigente (la refutada en el dossier de condiciones, pero cuya
hipótesis de base sigue siendo el punto de partida) exige explícitamente \(\Sigma\subset U\)
**compacta**. Un extremo topológico (\emph{end}, en el sentido estándar: una clase de equivalencia
de componentes no acotadas del complemento de compactos crecientes) es, por definición, una noción
que solo tiene contenido no vacío para **espacios no compactos**. Una variedad compacta tiene
exactamente cero extremos. Por tanto, tal como está escrita, la propuesta es **vacía** para
cualquier \(\Sigma\) que satisfaga la hipótesis de compacidad ya vigente: no hay ningún extremo que
\(\Omega_{\rm out}\) pueda contener.

Para que la propuesta tenga contenido, hay que decidir **cuál de las dos hipótesis se abandona**:
o bien se permite que \(\Sigma\) sea no compacta (con \(U\) compacto conteniéndola solo
parcialmente), o bien se reinterpreta "extremo" como otra cosa. Solo se ven dos maneras honestas de
dar contenido a la propuesta, y ninguna es gratuita:

### 1.1 Ruta A — \(\Sigma\) se extiende más allá de \(U\), hacia el espaciotiempo ambiente \(N\)

Si \(\Sigma\) es una loncha de un espaciotiempo ambiente \(N\supset U\) (con \(U\) un parche
compacto causalmente convexo dentro de \(N\), como ya contempla el contrato en su lenguaje de
"parche"), y \(\Sigma\) se extiende fuera de \(U\) hasta alcanzar un extremo genuino de \(N\),
entonces \(\Omega_{\rm out}\) vive, en su mayor parte, **fuera de \(U\)**. Determinar cuál de los
dos lados de \(S\) contiene "el" extremo requiere conocer la extensión de \(N\) más allá de \(U\)
— información que **no está contenida en el par \((g,U)\)**, por definición de que \(U\) es solo
un parche compacto de \(N\). Esto contesta la pregunta decisiva de forma directa: **sí, introducir
el extremo por esta ruta hace que \(Q\) dependa de información exterior a \(U\)**.

### 1.2 Ruta B — \(\Sigma\) permanece dentro de \(U\) pero se permite incompleta (no cerrada)

La única manera de que \(\Sigma\) tenga un extremo **sin salir de \(U\)** es que \(\Sigma\) no sea
cerrada en \(U\) — que le falten sus propios puntos límite, típicamente porque estos límites caen
sobre \(\partial U\) (o sobre algún subconjunto de medida cero de \(U\) removido a mano, una
variante todavía más artificial). En ese caso, "el extremo de \(\Sigma\)" es, geométricamente,
"la dirección en que \(\Sigma\) se aproxima a \(\partial U\)" — que es exactamente, salvo
disfraz notacional, **la componente distinguida de \(\partial U\)** que el PI ya identificó como la
opción más riesgosa. Esta ruta no introduce información *externa* a \(U\) en sentido estricto, pero
sí reintroduce la dependencia en el borde artificial de observación que se quería evitar, ahora
escondida detrás de la palabra "extremo".

### 1.3 Consecuencia

No existe una tercera lectura que mantenga \(\Sigma\) compacta, cerrada, íntegramente dentro de
\(U\), y aun así posea un extremo genuino: eso es una contradicción topológica directa (compacta
\(\Rightarrow\) cero extremos). La propuesta, para tener contenido, colapsa necesariamente en la
Ruta A (dependencia de información exterior a \(U\)) o en la Ruta B (la componente de \(\partial U\)
que el PI quería evitar). **Esta sesión evalúa la Ruta A**, por ser la que el PI describió
literalmente ("el único extremo asintótico", en el sentido estándar de relatividad general, no "el
borde de observación") y la que more se distingue de la idea ya descartada.

## 2. Las cinco comprobaciones, bajo la Ruta A

### 2.1 Independencia respecto de la loncha \(\Sigma\)

Bajo la hipótesis de que \(N\) tiene **un único extremo**, cualquier loncha \(\Sigma\subset N\) que
contenga a \(S\) como frontera de una región compacta \(\overline{\Omega_{\rm in}}\) tiene, como
mínimo, una única clase de extremos disponible a la que \(\Omega_{\rm out}\) puede pertenecer — pero
**la unicidad del extremo, por sí sola, no basta para garantizar que todas las lonchas asignen el
mismo lado a ese extremo.** Un extremo es una clase de equivalencia de colas no acotadas del
complemento de compactos crecientes; que exista una sola clase para \(N\) en su conjunto no implica
automáticamente que una loncha \(\Sigma\) arbitraria, o una sucesión de compactos crecientes
arbitraria dentro de ella, "vea" esa clase de forma consistente — hace falta, además, restringir
las extensiones consideradas a **lonchas propias** (asintóticamente compatibles, en el sentido de
aproximarse al extremo de forma controlada, sin oscilar entre acotado y no acotado ni degenerar) y
**demostrar** que dos lonchas propias cualesquiera que contengan a \(S\) efectivamente representan
el mismo extremo espacial — un lema adicional, no automático, que esta sesión no intentó probar (ni
refutar) por estar fuera de su alcance. **Esta comprobación queda, por tanto, plausible pero no
cerrada, no "satisfecha limpiamente"**: la premisa que la haría funcionar (unicidad del extremo de
\(N\), más el lema de representación consistente entre lonchas propias) es, en cualquier caso,
exactamente el dato que vive fuera de \(U\).

### 2.2 Invariancia bajo difeomorfismos

Los extremos son invariantes topológicos, así que un difeomorfismo de \(N\) que se restringe a un
difeomorfismo de \(U\) preserva trivialmente cuál extremo es cuál. **Pero surge una asimetría
nueva:** el Lema 2 del dossier de condiciones prueba covariancia para difeomorfismos de \(U\) hacia
\(U'\) — aquí necesitamos, en cambio, covariancia bajo difeomorfismos de \(N\) que se restringen a
\(U\), y un difeomorfismo definido solo en \(U\) (sin extensión canónica a \(N\)) no tiene por qué
actuar de forma coherente sobre el extremo, que vive fuera de su dominio. La invariancia por
difeomorfismos de \((g,U)\) **por sí solo** (sin datos de \(N\)) no está garantizada por este
argumento; solo lo está la invariancia por difeomorfismos de \((g,N)\) en su conjunto — un enunciado
de dominio distinto, no una simple mejora del Lema 2.

### 2.3 Preservación bajo perturbaciones conformes de soporte compacto

Aquí la propuesta funciona con más limpieza que en cualquier variante anterior: si
\(\omega\in C_c^k(U)\) tiene soporte compacto **dentro** de \(U\), y \(U\subsetneq N\), entonces la
perturbación no toca \(N\setminus U\) en absoluto. El extremo de \(N\) —y por tanto la
coorientación que induce sobre cualquier \(S\subset U\)— **permanece exactamente igual** entre
\(g_0\) y \(g_1=e^{2\omega}g_0\). Esta es una propiedad de estabilidad genuina y deseable: la
convención de "exterior" no se mueve bajo la perturbación que B2 necesita construir.

### 2.4 Compatibilidad con el modelo `fixed_n` observado solo en \(U\)

Aquí aparece la tensión de fondo, ya anticipada por la pregunta decisiva — pero conviene precisar
qué falla exactamente y qué no. El canal de observación (contrato §4.1) muestrea \(n\) puntos i.i.d.
de la medida de volumen normalizada **en \(U\)**, y olvida coordenadas y etiquetas de encaje — el
dato observado nunca ve nada de \(N\setminus U\). **Esto no es, en sí mismo, una incompatibilidad
con el modelo `fixed_n`**: nada impide ampliar el modelo estadístico para que su universo de
objetos sea geometrías ambiente \((N,g,U;e)\) en vez de patches \((g,U)\) sueltos, manteniendo
intacto que el dato efectivamente observado —la muestra— siga restringido a \(U\); el canal de
muestreo y la cadena de TV del contrato §4.2 no usan en ningún paso que el objeto muestreado sea
"todo" lo que existe, solo que la ley del poset se derive de un muestreo en \(U\). Lo que realmente
falla no es la compatibilidad estadística sino la **fidelidad al dominio declarado**: el contrato
(§1, §2, §7 G1) escribe \(Q\) explícitamente como funcional del par \((g,U)\) solo, y bajo la Ruta A
eso deja de ser cierto — el objeto que se estaría evaluando es \(Q(g,N,U;e)\) o similar, no
\(Q(g,U)\), aunque el canal de observación pueda, sin cambio alguno, seguir muestreando solo de
\(U\). Ver hallazgo adicional en §3 para la relación (no equivalencia) de esto con \(T_{\rm EH}\).

**Matiz importante, encontrado en esta sesión:** para la comparación específica que B2 necesita
—\(g_0\) y \(g_1=e^{2\omega}g_0\) con \(\omega\) de soporte compacto en \(U\)— ambas geometrías
comparten **la misma extensión \(N\setminus U\)** sin cambios (§2.3). Si \(N\) se declara **una
sola vez**, como dato auxiliar fijo y compartido para todo el par testigo (no derivado de \((g,U)\)
sino declarado junto con la construcción), la coorientación queda bien definida y estable para *esa
comparación concreta*, aunque \(Q\) no sea, en general, un funcional de \((g,U)\) solo. Esto es
importante porque muestra que la Ruta A **no es una idea muerta** — es implementable — pero exige
reconocer que el dominio real del target pasa a ser \((g,U;N)\) o \((g,U;\text{convención de
extremo declarada})\), no \((g,U)\).

### 2.5 Defendibilidad física

Aquí la propuesta es genuinamente sólida, mejor que cualquier alternativa considerada hasta ahora:
exigir un único extremo asintótico (asintóticamente plano, en el caso típico) es **exactamente** la
hipótesis estándar bajo la cual se estudian MOTS, horizontes aparentes, masa ADM, y los teoremas de
masa positiva en relatividad matemática — no es una restricción inventada para esquivar \(S^3\); es
el marco habitual de la literatura de superficies atrapadas (aunque, como ya se registró en la
Decisión 048 y en el dossier de condiciones, `biblioteca/` no contiene ninguno de esos textos para
anclar esto con cita primaria). Esta comprobación se satisface mejor que las cuatro anteriores.

## 3. Hallazgo adicional — la Ruta A comparte con \(T_{\rm EH}\) el mismo tipo de obstrucción, sin ser el mismo target ni un corolario del Teorema 3.2

El contrato (§2.3) es explícito: \(Q_{\mathrm{FMOTS}}\) "no es \(T_{\rm EH}\)" y "no es el horizonte
de eventos global" — precisamente porque \(T_{\rm EH}\) requiere conocer la continuación causal
completa del espaciotiempo (vía \(\mathscr I^+\)), mientras que B2 se propuso como una alternativa
cuasi-local, evaluable en un parche compacto. La Teorema 3.2 del manuscrito
(`docs/manuscript_limits_draft.md:455-483`, ya citado en la Decisión 048 y en el dossier de
condiciones) prueba que \(T_{\rm EH}\) **no** es medible respecto de los datos de un parche
causalmente convexo finito — un resultado específico sobre \(T_{\rm EH}\), no sobre
\(Q_{\mathrm{FMOTS}}\) ni sobre la Ruta A, y esta sesión no intenta extenderlo formalmente a este
caso. Lo que sí puede afirmarse, sin apelar a ese teorema ni a una equivalencia de targets, es una
analogía estructural: **la Ruta A introduce, para \(Q_{\mathrm{FMOTS}}\), el mismo *tipo* de
obstrucción por información exterior al parche que motivó originalmente evitar \(T_{\rm EH}\)** —
ambos casos comparten la forma "el valor del target en \(U\) depende de datos de fuera de \(U\)",
no el contenido, la definición, ni el mecanismo concreto (uno vía \(\mathscr I^+\) y la
estructura causal global; el otro vía la extensión \(N\setminus U\) y su extremo). No se afirma que
\(Q_{\mathrm{FMOTS}}\) bajo la Ruta A **sea** \(T_{\rm EH}\), ni que el Teorema 3.2 se aplique
directamente a él. Esto no refuta la propuesta —la comparación §2.3/§2.4 muestra que sigue siendo
utilizable si se declara \(N\) (y su extremo) como dato auxiliar fijo y compartido— pero sí
significa que aceptarla equivale a renunciar, en la práctica, a la promesa central de B2 (un target
evaluable a partir de \((g,U)\) solo), sustituyéndola por una promesa más débil y de otro tipo (un
target evaluable a partir de \((g,U)\) más una convención de extensión/extremo declarada
externamente y compartida por todo el par testigo) — la misma clase de obstrucción, no el mismo
target.

## 4. Veredicto

**`REQUIRES_TARGET_CHANGE`**

No es `VIABLE_AS_CLASS_RESTRICTION`: la propuesta, hecha precisa, no puede formularse usando solo
\((g,U)\) — un extremo asintótico es una noción vacía para la \(\Sigma\) compacta que la propia
clase ya exige, y darle contenido obliga a salir de \(U\) (Ruta A, información externa) o a
colapsar en la componente-de-\(\partial U\) que el PI ya quería evitar (Ruta B). No es `REFUTED`
sin más: la Ruta A es matemáticamente coherente, es plausible (aunque no cerrada: §2.1 deja
pendiente el lema de que lonchas propias distintas representen el mismo extremo) en la
independencia de \(\Sigma\), pasa limpiamente la preservación bajo perturbaciones de soporte
compacto (§2.3) y la defendibilidad física (§2.5) — es, con diferencia, la más limpia de las tres
candidatas evaluadas hasta ahora (borde-de-región-compacta, libre-de-orientación, extremo único).
Su fallo no es de coherencia matemática sino de **alcance declarado**: el extremo no repara el
target ya adoptado \(Q(g,U)\); define uno distinto,

\[
Q_{\mathrm{end}}(N,g,U;e),
\]

donde la extensión ambiente \(N\) —y posiblemente el propio extremo \(e\)— pasa a formar parte de
los datos geométricos declarados, no derivados de \((g,U)\). Esto es, precisamente, un cambio del
target (de su firma/dominio), no una restricción de la clase geométrica dentro del target ya
adoptado. La relación con \(T_{\rm EH}\) (§3) es de **analogía estructural** —la misma obstrucción
por información exterior al parche— y no una equivalencia de targets ni un corolario del
Teorema 3.2, que sigue siendo un resultado específico sobre \(T_{\rm EH}\).

Este veredicto no cierra la condición 1 ni la reabre en otra forma: registra que **esta** vía de
reparación, evaluada con honestidad, exige modificar qué tipo de objeto es \(Q_{\mathrm{FMOTS}}\),
no solo cómo se define \(S_{\rm adm}\) dentro de él.

## 5. Estado de autorización

```text
PROPOSAL = SINGLE_ASYMPTOTIC_END_RESTRICTION
VERDICT = REQUIRES_TARGET_CHANGE
CONDITION_1_STATUS = OPEN (sin cambios; ver phase3_b2_decision048_conditions_review.md)
TARGET_ADOPTION = NOT_AUTHORIZED
WITNESS_CONSTRUCTION = NOT_AUTHORIZED
CODE = NOT_AUTHORIZED
SIMULATION = NOT_AUTHORIZED
SEEDS = NOT_AUTHORIZED
COMITE_RECONVENED = NO
COMMIT_OR_PUSH = NOT_AUTHORIZED_BY_THIS_DOCUMENT
```

`NOT_READY_TO_RECONVENE` se mantiene (ver
`research_program/work_packages/phase3_b2_decision048_conditions_review.md`, ya versionado en el
commit `5924b6b`). Este documento queda sin commit ni push, a la espera de revisión.
