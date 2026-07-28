# Taxonomía de identificabilidad geométrica desde orden causal

> **Documento de trabajo REVISABLE, no congelado.** Esta taxonomía fija vocabulario para el
> programa de investigación y busca evitar saltos ilegítimos entre recoverability empírica,
> límites instrumentales y no-go intrínsecos del orden.

## 0. Propósito

En este repo ya conviven varias capas de afirmación:

- un resultado empírico de **recoverability** en parche finito;
- un **operational floor** del estimador sellado;
- preguntas abiertas sobre minimax, contigüidad e identificabilidad del orden completo.

Sin una taxonomía explícita, es fácil deslizarse desde:

> "este observable satura"

a

> "el orden no puede hacerlo mejor",

que son afirmaciones de naturaleza muy distinta.

Este documento fija esas distinciones.

## 1. Objetos básicos

### 1.1 Orden observado

El dato primario es un poset finito observado `C_obs`, entendido como estructura causal discreta
disponible sin coordenadas ocultas.

### 1.2 Geometría latente

La "geometría" que se quiere recuperar puede significar cosas distintas:

- clase causal/conformal;
- volumen o escala discreta;
- frontera u objeto tipo horizonte;
- distancia/proper time;
- dimensión efectiva;
- topología u homología;
- curvatura o acción efectiva.

La primera regla es no usar "geometría" como sustantivo indiferenciado. Toda afirmación debe
nombrar el observable geométrico concreto.

### 1.3 Observable geométrico

Un observable geométrico es cualquier funcional o propiedad `G` del objeto latente que se quiera
inferir a partir del orden.

Ejemplos:

- posición de una frontera `r_*`;
- pertenencia a una región interior/exterior;
- ancho de una banda near-horizon;
- tiempo propio entre dos clases de eventos;
- dimensión local;
- número de componentes o estructura homológica.

## 2. Tipos de tarea inferencial

### 2.1 Recoverability

Diremos que hay **recoverability** cuando existe una regla order-only que recupera una señal
geométrica útil y verificable en un régimen bien definido.

Forma canónica:

> existe una regla `T(C_obs)` que produce un objeto o estimación ligado a `G`, y esa salida supera
> controles relevantes bajo un protocolo congelado.

Esto es deliberadamente más débil que reconstrucción.

### 2.2 Localización

Hay **localización** cuando la salida buscada es una posición, frontera, banda o vecindad dentro
de una geometría oculta.

No toda recoverability es localización. Por ejemplo, clasificar interior/exterior y localizar una
frontera no son el mismo problema.

### 2.3 Reconstrucción

Reservamos **reconstrucción** para afirmaciones donde el orden fija el objeto geométrico de forma
suficientemente rica como para hablar de recuperación estructural, no solo de una señal parcial o
de una localización acotada.

En este programa, "reconstrucción" es lenguaje fuerte y debe evitarse salvo prueba explícita.

### 2.4 Detección

Hay **detección** cuando el objetivo es decidir presencia/ausencia de una estructura, no
localizarla ni reconstruirla.

Ejemplo:

- "hay imprint de truncación singular" es un problema de detección;
- "la frontera está en esta banda" es uno de localización.

## 3. Tipos de evidencia

### 3.1 Evidencia de instrumento

La evidencia de instrumento dice algo sobre una regla concreta `T`.

Ejemplo:

> el estimador sellado v2 alcanza recoverability en `prereg-002`;
> el mismo estimador exhibe un suelo operacional `O(ell)` en `prereg-003`.

Esto no autoriza afirmaciones sobre toda regla order-only.

### 3.2 Evidencia de familia de observables

La evidencia de familia dice algo sobre una clase `F` de reglas:

- observables basados en minimales;
- observables locales;
- scores aditivos;
- observables tipo longest-chain/future-cardinality;
- observables relacionales globales.

Este nivel es más fuerte que el instrumental y más débil que un no-go intrínseco.

### 3.3 Evidencia intrínseca del orden

La evidencia intrínseca apunta a propiedades de la ley del orden observado, no de un pipeline
concreto.

Se expresa de manera natural mediante:

- TV;
- KL;
- Hellinger;
- likelihood-ratio;
- contigüidad;
- lower bounds minimax o de dos puntos.

Aquí la unidad relevante deja de ser `T(C_obs)` y pasa a ser la familia de leyes sobre `C_obs`.

## 4. Tres niveles de límite

## 4.1 Límite del estimador

Un **límite del estimador** ocurre cuando una regla concreta falla, satura o no mejora con
densidad.

Forma típica:

> `T` no localiza mejor que escala `a_n` en el régimen `R`.

Esto puede deberse a:

- mal diseño del observable;
- ruido/varianza;
- sensibilidad a borde;
- score subóptimo;
- horizonte de caja insuficiente;
- falta de información en la propia salida, pero no necesariamente en `C_obs`.

### 4.2 Límite de familia

Un **límite de familia** ocurre cuando toda regla en una clase `F` comparte una obstrucción.

Forma típica:

> ninguna regla en `F` logra error mejor que `a_n` en el régimen `R`.

Este es un objetivo programático razonable a medio plazo.

### 4.3 Límite intrínseco del orden

Un **límite intrínseco del orden** ocurre cuando la obstrucción no depende de la elección de
estimador dentro de una clase amplia de reglas order-only.

Forma típica:

> las leyes inducidas por dos geometrías cercanas son demasiado próximas sobre `C_obs` como para
> permitir identificación consistente con precisión arbitraria.

Este es el nivel al que apuntaría, si llegara a cerrarse, una auténtica "indeterminación
order/geometría".

### 4.4 Etiquetas operativas Fase 0 (2026-07-28)

Ancla normativa de programa:
`research_program/synthesis/phase0_program_north_decision.md` §3.
No sustituyen §4.1–§4.3; las **rotulan** para redacción y comités.

| Etiqueta | Significado | No confundir con |
|---|---|---|
| `EMPIRICAL_FAILURE_OF_CLASS_L` | Toda regla en una lista/clase **nombrada** `L` falla bajo un protocolo fijado | Imposibilidad para todo estimador medible del canal |
| `PROVED_NON_IDENTIFIABILITY` | Ningún estimador medible del canal alcanza riesgo arbitrariamente bajo (par testigo con leyes iguales o TV/Hellinger/Fisher ⇒ suelo minimax; o target no funcional de los datos) | “No encontramos un observable que funcione” |

**Regla R3 (vinculante mientras rija la Fase 0 / paper de límites):** el ledger C1–C6 y los
terminales de la matriz post-PR008 se citan como `EMPIRICAL_FAILURE_OF_CLASS_L`, nunca como
prueba de `PROVED_NON_IDENTIFIABILITY`. Los lemas de ceguera de escala (Teorema A, OP-1.2), el
suelo de dos puntos en familia regular y la no-funcionalidad del horizonte global en un patch
finito son el tipo de resultado que **sí** puede llevar la segunda etiqueta.

Mapeo rápido:

- §4.1 límite del estimador → `EMPIRICAL_FAILURE_OF_CLASS_L` con `|L|=1`
- §4.2 límite de familia → `EMPIRICAL_FAILURE_OF_CLASS_L` si la clase se agota por protocolo;
  `PROVED_NON_IDENTIFIABILITY` solo si hay cota sobre todas las reglas medibles de esa clase
- §4.3 límite intrínseco del orden → solo `PROVED_NON_IDENTIFIABILITY`

## 5. Escalas de error e interpretaciones

### 5.1 Escala discreta

La escala `ell` representa la resolución discreta natural del régimen.

Decir que un error es `O(ell)` puede significar dos cosas muy distintas:

1. **solo** que el instrumento actual se queda en esa escala;
2. que **ninguna** regla razonable puede superar esa escala.

No deben confundirse.

### 5.2 Saturación

Hay **saturación** cuando la mejora con densidad deja de seguir la escala esperada.

Interpretaciones posibles:

- limitación instrumental;
- mezcla de señal física y artefacto de caja;
- observable mal alineado con el objeto geométrico;
- verdadero límite de identificabilidad.

La mera saturación no decide entre estas posibilidades.

### 5.3 Divergencia o peel-off

Si una cantidad transversal crece en unidades de `ell`, eso puede significar:

- que el objeto perseguido deja de ser adherente al horizonte;
- que el criterio de selección optimiza otra cosa;
- que la estructura buscada no está bien definida order-only;
- o que el observable mezcla frontera con región profunda.

De nuevo: no basta para un no-go universal.

## 6. Régimen estadístico de identificabilidad

## 6.1 Separación total

Si `||P_n - Q_n||_TV -> 1`, existe test consistente. La estructura es asintóticamente
identificable al menos como problema de testing.

### 6.2 Contigüidad mutua

Si `P_n ◁ Q_n` y `Q_n ◁ P_n`, no hay test consistente. Este es el régimen más limpio de
no-identificabilidad asintótica.

### 6.3 Contigüidad unilateral

Si solo una de las dos contigüidades vale, sigue sin haber testing consistente simétrico, pero la
asimetría puede tener contenido geométrico o inferencial.

### 6.4 Complemento residual

Puede haber regímenes intermedios donde no hay separación total ni contigüidad limpia. Esos casos
también cuentan como resultados y no deben forzarse a una dicotomía falsa.

## 7. Tipos de claim admisibles

### 7.1 Claim empírico acotado

Admisible cuando:

- el régimen está especificado;
- el observable está nombrado;
- el protocolo está cerrado;
- los controles están definidos.

Ejemplo de forma correcta:

> "order-only localisation of the horizon-associated boundary within a finite patch"

### 7.2 Claim instrumental

Admisible cuando se habla explícitamente del canal o instrumento concreto.

Ejemplo:

> "operational floor of the sealed estimator"

### 7.3 Claim de familia

Admisible solo cuando se ha definido la clase de reglas `F` y la cuantificación sobre `F` está
realmente justificada.

### 7.4 Claim intrínseco

Admisible solo con argumentos sobre la ley completa del orden observado o un lower bound
equivalente.

Ejemplos de lenguaje que **no** debe usarse sin eso:

- "universal no-go";
- "information limit of order";
- "no order-only estimator can...";
- "principio de incertidumbre gravitacional".

## 8. Tipos de claim no admisibles todavía

Hasta nuevo aviso, en este programa no son admisibles como resultados establecidos:

- reconstrucción métrica general;
- límite minimax universal sobre todos los `f(C_obs)`;
- no-go asintótico universal;
- claim 3+1D a partir del parche actual 1+1D;
- claim de horizonte genérico si el mecanismo sigue dependiendo de truncación singular;
- "uncertainty principle" como resultado físico ya demostrado.

## 9. Niveles de pregunta científica

### Nivel I — ¿hay señal?

Pregunta de detección.

### Nivel II — ¿hay recoverability útil?

Pregunta empírica/instrumental.

### Nivel III — ¿qué escala de localización se logra?

Pregunta de tasa o resolución.

### Nivel IV — ¿la tasa depende del observable o de la clase?

Pregunta de familia.

### Nivel V — ¿hay obstrucción intrínseca del orden?

Pregunta estructural fuerte.

El programa debe avanzar en ese orden. Saltar de II o III a V sin cerrar IV es exactamente el
tipo de sobreextensión que esta taxonomía quiere evitar.

## 10. Regla de escritura

Cada nuevo documento del programa debería incluir explícitamente:

1. **objeto geométrico** estudiado;
2. **tipo de tarea**: detección / localización / reconstrucción;
3. **nivel de evidencia**: instrumento / familia / intrínseco;
4. **tipo de claim**: empírico acotado / instrumental / familia / intrínseco;
5. **qué NO demuestra**.

## 11. Definición operativa provisional de indeterminación order/geometría

Propuesta de trabajo, no resultado:

> Hay indeterminación order/geometría para un observable `G` en un régimen `R` si familias
> geométricamente distintas inducen leyes sobre el orden observado que impiden fijar `G` con
> precisión arbitraria mediante reglas order-only, y esa obstrucción persiste al pasar de un
> instrumento concreto a una clase suficientemente amplia de observables.

Esta definición tiene dos ventajas:

- no confunde fallo de instrumento con límite intrínseco;
- no exige hablar todavía de un "principio" físico.

## 12. Siguiente uso de esta taxonomía

Los siguientes documentos del programa deberían usar este vocabulario:

- `research_program/bibliography/identifiability_bibliography_matrix.md`
- `research_program/models/canonical_counterexamples.md`
- cualquier nota futura sobre familias `P_n(theta)` y lower bounds.
