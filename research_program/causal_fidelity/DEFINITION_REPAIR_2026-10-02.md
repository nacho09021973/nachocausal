# Fidelidad causal — revisión de definiciones y primer candidato

Fecha: 2026-10-02. Estado: `DRAFT / TARGET_OPEN / NO_CONFIRMATORY_EXECUTION`.
Base: `main @ d5567eb`. No modifica el contrato histórico de septiembre.
No es un resultado canónico ni una revisión independiente.

## 1. Procedencia y obligación

El contrato original se copia sin cambios desde el WIP del usuario:
`CAUSAL_FIDELITY_MINIMAL_CONTRACT.md`, SHA-256
`ba99fcb5ed7cbc160cca29b35c57120ad17f8618ed144192e1598831f8442957`.
El gate de octubre se copia sin cambios desde `172cde7`:
`CAUSAL_DYNAMIC_IR_GATE.md`, SHA-256
`fa32fff857a5ef2b76e1cdd840ebdbc8fd834c355281ce8b71859d27a7320d57`.

El original deja por especificar familia, dinámica, tiempo, detector y regla IR.
Prohibir coordenadas en el código no sustituye una definición invariante.
Un arrival time tampoco constituye por sí solo un coarse-graining ni un límite.

Lo siguiente es una propuesta explícita para comprobar esas distinciones.
No se escoge una dinámica para obtener el resultado deseado.

## 2. Entrada intrínseca y alcance del reloj

Sea `(E,prec;s,d)` un poset finito estricto con fuente y detector distinguidos.
Los datos son su clase de isomorfismo con ambas marcas. No se afirma que
seleccionar las marcas desde un poset sin marcas esté resuelto; aquí forman
parte de la entrada declarada. La medida es conteo, no pesos de embedding.

Una biyección `pi:E->E'` transporta orden, fuente y detector. Para cada salida
escalar se exige

`R(pi C; pi s, pi d; k) = R(C; s,d; k)`.

Las salidas vectoriales deben transportarse con la matriz de permutación `P`.
Ésta es la obligación matemática; un test finito de relabeling no la reemplaza.

El índice `k` cuenta actualizaciones de una regla discreta. No es tiempo propio,
tiempo de coordenadas ni una duración física reconstruida. La sincronización
es una hipótesis del modelo. Invariancia ante etiquetas no convierte ese reloj
en una propiedad única del orden ni establece invariancia Lorentz.

## 3. Primer candidato completamente finito

Se consideran todos los posets finitos con `N>=2` y `s!=d`. No se propone ley
de sprinkling ni experimento estadístico: las afirmaciones siguientes son
deterministas para cada entrada. La cuestión IR permanece sin especificar.

Defínase la relación de cobertura

`x lessdot y <=> x prec y and no z satisfies x prec z prec y`.

La matriz `A` tiene `A[y,x]=1` para coberturas y cero en otro caso. La elección
de etiquetas sólo representa el operador. Para un parámetro `alpha>0`, sea

`X_alpha(0;epsilon) = epsilon e_s`,
`X_alpha(k+1;epsilon) = alpha A X_alpha(k;epsilon)`.

Estado base: cero. Perturbación: impulso de amplitud epsilon en la fuente,
una sola vez. Espacio de estados: `R^E`. Detector: componente d. Dominio:
`k=0,...,N-1`; fuera de él la respuesta es cero por nilpotencia.

La susceptibilidad respecto de la amplitud inicial queda definida exactamente:

`R_alpha(C;s,d;k) = d/d epsilon X_alpha(k;epsilon)[d] at epsilon=0`
`                 = alpha^k (A^k)[d,s]`.

Para dos dinámicas se mantienen todos los datos y protocolos, cambiando sólo
`alpha_1` frente a `alpha_2`. No se supone conservación de norma, reversibilidad
ni unitariedad. El detector observa una evolución de estados, no una etiqueta
estática rebautizada como respuesta.

El transporte `A'=P A P^-1`, `e_s'=P e_s` prueba la invariancia de la respuesta.
Esta prueba depende también de transportar el detector.

## 4. Qué es cinemático y qué es dinámico en este modelo

El objeto causal sin reloj es

`K(C) = {(x,y): x prec y}`.

Una vez declarado el reloj de actualizaciones, el conjunto de pasos permitidos
por la regla de cobertura, para la pareja fijada, es

`K_step(C;s,d) = {k in {1,...,N-1}: a directed cover path of length k joins s to d}`.

Esto es una cinemática del modelo de actualización elegido, no un conjunto de
tiempos físicos determinado exclusivamente por el orden sin ese postulado.

El soporte dinámico temporal es

`S_alpha(C;s,d) = {k: R_alpha(C;s,d;k) != 0}`.

**Deducción para el candidato:** para todo `alpha>0`,

`S_alpha(C;s,d) = K_step(C;s,d)`.

Prueba: `(A^k)[d,s]` cuenta los caminos de cobertura de longitud k, por
multiplicación de matrices con entradas no negativas. El factor `alpha^k`
es estrictamente positivo. La respuesta es no nula exactamente cuando hay
algún camino. Sumando sobre k y usando que cualquier par comparable de un
poset finito admite una cadena saturada, el soporte agregado sobre parejas
coincide exactamente con K.

Segunda derivación: un impulso sólo puede avanzar una cobertura por
actualización. Por inducción, en el paso k recibe una contribución positiva
por cada camino de longitud k, y ninguna otra contribución. No hay cancelación.

Casos límite: si `s` y `d` son incomparables no hay respuesta; si `alpha=0`
no hay propagación entre marcas distintas (queda fuera de la clase positiva).
Permitir pesos con signo abriría cancelaciones y sería otro contrato.

**Consecuencia:** la igualdad del soporte entre especies aquí es tautológica
respecto de la positividad y la regla de cobertura. El candidato queda
descartado como prueba de una característica dinámica no trivial o de saturación
relativista. No proporciona el `Char_C[G]` que exige el documento de parada.

## 5. Arrival time y control de pérdida de información

Para este modelo, un umbral diagnóstico declarado `theta>0` permitiría definir

`tau_alpha = min {k in {1,...,N-1}: R_alpha(k)>=theta}`,

con valor infinito si el conjunto es vacío. Igualdad en el umbral cuenta como
llegada. No se interpola, no se introduce tolerancia y no se llama frente.
`Q=tau` es sólo un resumen escalar de la historia dinámica.

Comprobación manual: en la cadena de tres elementos `s lessdot m lessdot d`,
la respuesta del detector sólo existe en k=2 y vale `alpha^2`.
Por tanto `tau=2` si `alpha^2>=theta`, e infinito en otro caso, aunque el
soporte no nulo sea el mismo para todos los alpha positivos. Dos amplitudes
distintas también pueden tener exactamente el mismo tau. Esto comprueba por
una segunda vía que arrival, amplitud y soporte no son intercambiables.

No se ejecutó código para esta deducción. No se fijan theta o alpha después de
observar datos, ni se usa el ejemplo como evidencia física.

## 6. Reparación necesaria del test IR

Antes de escribir una inclusión hay que declarar un espacio ambiente común:

- Si `T_caus` contiene parejas de eventos, `T_IR` también debe contener parejas
  o clases de parejas con un mapa explícito que haga comparable la afirmación.
- Si contiene pasos de actualización, ambos conjuntos deben referirse al mismo
  reloj, fuente, detector y dominio. El límite puede cambiar el espacio ambiente;
  en ese caso hay que declarar los mapas de transporte.
- Un límite de escala exige una sucesión especificada, su normalización,
  la regla de coarse-graining, el modo de convergencia y el orden de límites.
  Los tiempos de una sola realización finita no definen por sí solos ese límite.

`Q=tau` no conserva necesariamente amplitudes ni la historia de soporte.
Construir un conjunto desde ese escalar exige una regla adicional; no puede
inferirse una pérdida causal estricta sólo porque el resumen tiene dimensión uno.
Si la regla devuelve una constante o selecciona de antemano un subconjunto de
K, la igualdad IR o la inclusión estricta pueden estar codificadas en ella.

No se introduce una regla IR para forzar el blanco. No se identifica el
coarse-graining con recortar una lista de tiempos. Para el candidato finito
de §§3–5, `IR_RULE`, `LIMIT_PATH` y `TARGET_IR_EQUALITY` permanecen OPEN.

## 7. Salida y próximo requisito

```text
INPUT_EQUIVARIANCE = DERIVED_FOR_DECLARED_POINTED_INPUT
OPERATIONAL_CLOCK = EXPLICIT_NOT_PHYSICAL_TIME
STATE_DYNAMICS = EXPLICIT_FINITE_LINEAR_CANDIDATE
SUPPORT_EQUALITY = BY_POSITIVE_COVER_PATH_CONSTRUCTION
NONTAUTOLOGICAL_CHARACTERISTIC = NOT_SUPPLIED
IR_RULE = OPEN
LIMIT_PATH = OPEN
EXACT_TARGET = OPEN
INDEPENDENT_REVIEW = NOT_PERFORMED
CANONICAL_PROMOTION = NONE
```

La unidad cierra una distinción de definiciones y elimina un candidato trivial.
El siguiente paso útil es formular una regla IR con motivación independiente
de la igualdad deseada, o registrar que sigue faltando. No procede ejecutar
simulaciones, ensayar umbrales, abrir B4 o promover universalidad.

## 8. Continuación del mismo día

`IR_OPERATIONAL_DEFINITION_2026-10-02.md` completa una propuesta de mapa
mesoscópico común, espacio ambiente, ausencia de llegada y límite Hausdorff.
El primer caso de cadenas refinadas falla por ausencia de inclusión estricta.
La lectura del atlas QCA y de Farrelly–Short p.3 mantiene separada esa propuesta
de un IR de baja energía. El ejemplo de dos caminos de longitudes 2 y 3
muestra exactamente que `Q=tau` no determina la respuesta temporal de baja
frecuencia. El IR físico y cualquier cambio de observable permanecen OPEN.
