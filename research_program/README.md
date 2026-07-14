# Research Program — indeterminación geométrica desde orden causal

> **Documento de trabajo REVISABLE, no congelado.** No es pre-registración, no fija umbrales, no
> autoriza cambios en el camino sellado, y no convierte ninguna conjetura conceptual en resultado.
> Su función es separar el objetivo científico general del estado actual de un estimador concreto.

## Estructura de carpeta

Esta carpeta existe para desacoplar el **programa de investigación** de:

- `docs/`: claims, preregistros, cierres de fase, auditorías y documentos con valor de registro;
- `dev/`: exploración reversible, notas de trabajo efímeras y pruebas instrumentales;
- `formal/`: formalización Lean/Alloy.

Convención:

- `research_program/README.md`: mapa maestro del programa;
- `research_program/taxonomy/`: vocabulario, tipos de identificabilidad, claim boundaries;
- `research_program/bibliography/`: matrices de literatura y mapas de soporte/límite;
- `research_program/work_packages/`: paquetes de trabajo activos;
- `research_program/models/`: familias estadísticas y contraejemplos canónicos;
- `research_program/results/`: solo cuando exista un resultado programático estabilizado, todavía
  no apto para `docs/`.

## 0. Pregunta guía

La pregunta del programa no es ya:

> "¿funciona mejor este algoritmo?"

sino:

> "¿qué parte de la geometría continua es identificable desde orden causal solo, y dónde aparece
> una indeterminación estructural que no desaparece al cambiar de estimador dentro de una clase
> razonable de observables?"

En particular, para fronteras de tipo horizonte:

- qué puede recuperarse como estructura causal gruesa;
- qué puede localizarse con precisión que mejora con la densidad;
- qué solo se recupera hasta una vecindad de escala discreta;
- y qué no queda fijado de manera arbitrariamente fina a partir de orden finito.

## 1. Estado de partida (lo ya sabido, sin sobreextenderlo)

1. **Recoverability en parche finito.** `prereg-002` establece que el orden causal solo, bajo el
   protocolo sellado, localiza de manera significativa y estable una frontera asociada al
   horizonte en un modelo Schwarzschild 1+1D de parche finito. Esto es un resultado de
   **recoverability**, no de reconstrucción métrica ni de horizonte global.

2. **Suelo operacional del instrumento sellado.** `prereg-003` congela una **cota operacional
   O(ell)** del estimador v2 sellado. No es una cota minimax sobre todos los funcionales del
   orden, ni un no-go universal sobre toda estadística order-only.

3. **Base conceptual parcial en la literatura.**
   - HKMM respalda la idea de que la estructura causal transporta mucha geometría, pero no cierra
     el caso d=2 ni la traducción discreta general.
   - La Hauptvermutung sigue abierta en general: la reconstrucción geométrica desde causal sets es
     un programa con apoyo parcial, no un teorema cerrado.
   - En el caso actual, parte del signal físico conocido depende del mecanismo de
     **singularity-truncated futures**, por lo que no debe venderse como "horizon-generic"
     mientras no se separe de ese mecanismo.

### 1.1 Estado operativo del frente de observables

PR008 está cerrado como `BASELINE_DOMINATED`. PR009 abrió un canal distinto de expansión
efectiva order-only, pero terminó durante su bloque de referencia con
`FAILED_DATA_CONTRACT`: la cobertura reference-MINK en profundidad 7 quedó por debajo del
mínimo preregistrado. No se publicó ningún artefacto PR009, no se ejecutaron evaluación ni
scorer y no existe resultado científico sobre sensibilidad al horizonte.

PR010 es ahora una fase de diseño de cobertura. Debe usar semillas de desarrollo nuevas y
decidir, antes de una nueva confirmación, entre ampliar el bloque de referencia o limitar
las profundidades puntuables. Los valores internos no publicados y las semillas de PR009
son entradas prohibidas. El nuevo prerregistro, las semillas confirmatorias y la auditoría
permanecen pendientes; esta actualización no autoriza ninguna ejecución.

## 2. Distinciones que no deben mezclarse

Toda afirmación futura debe etiquetarse en una de estas tres capas:

1. **Límite del estimador.**
   El observable o pipeline concreto falla o satura.

2. **Límite de una familia de observables.**
   Falla cualquier observable de cierto tipo: local, basado en minimales, de radio efectivo corto,
   de cierta complejidad, etc.

3. **Límite intrínseco del orden.**
   Ninguna regla order-only en una clase suficientemente amplia puede fijar el observable con
   precisión arbitraria en el régimen considerado.

El objetivo científico fuerte del programa está solo en (3). El estado actual del repo cierra
parcialmente (1) y deja abierto (2)-(3).

## 3. Objetivo principal

Construir una **teoría por niveles de identificabilidad geométrica desde orden causal**:

- observables geométricos recuperables;
- tasas de precisión alcanzables;
- escalas de saturación;
- contraejemplos o familias casi indistinguibles;
- y, si existe, una formulación honesta de una **indeterminación order/geometría**.

El producto final deseable no es "otro algoritmo para el horizonte", sino una tabla del tipo:

| observable | clase de input | evidencia de recoverability | evidencia de no-identificabilidad | estado |
|---|---|---|---|---|
| frontera asociada al horizonte | parche 1+1D Schwarzschild | `prereg-002` | `prereg-003` solo para el estimador sellado | `PARTIAL` |
| proper time / longest chain | regiones sprinkladas fielmente | literatura CST clásica | finito-N y borde siguen abiertos | `PARTIAL` |
| volumen/cardinalidad | ensemble Poisson | correspondencia n~rho V en media | fluctuación sqrt(V) a realización finita | `PARTIAL` |
| horizonte genérico | clase amplia | no cerrado | mecanismo actual depende de singularidad | `OPEN` |

## 4. Hipótesis de trabajo

Hipótesis fuerte, aún no demostrada:

> existen observables geométricos cuya localización fina no es arbitrariamente refinable desde
> orden causal finito, no solo por debilidad de un estimador concreto, sino por una obstrucción
> estructural de identificabilidad.

Versión sobria admisible hoy:

> el programa buscará distinguir entre suelo operacional del instrumento, suelo de familia de
> observables y posible límite intrínseco order/geometría.

## 5. Fases del programa

### Fase A — Marco conceptual y taxonomía

Objetivo:
fijar un vocabulario técnico único para no hablar de "reconstrucción", "localización",
"recoverability" e "indeterminación" de manera intercambiable.

Entregables:

- `research_program/taxonomy/identifiability_taxonomy.md`
- matriz bibliográfica `orden reconstruye / no reconstruye / abierto`

Preguntas:

- qué observables dependen de orden solo;
- cuáles requieren además número/medida;
- cuáles son conformales, métricos, topológicos o de frontera;
- cuáles son ensemble statements y cuáles son single-instance statements.

### Fase B — Reformulación estadística: identificabilidad

Objetivo:
traducir el problema físico a uno de familias de leyes sobre posets finitos.

Núcleo:

- dos geometrías o fronteras cercanas inducen dos leyes `P_n` y `Q_n` sobre órdenes finitos;
- estudiar TV, KL, Hellinger, segundo momento del likelihood ratio, contigüidad;
- clasificar el régimen como:
  - separación total;
  - contigüidad mutua;
  - contigüidad unilateral;
  - complemento residual.

Entregables:

- nota técnica sobre formalización de `P_n(theta)` para familias geométricas;
- catálogo de qué nociones de separación bastan para consistent testing, lower bounds y minimax.

### Fase C — Modelos canónicos de casi indistinguibilidad

Objetivo:
construir ejemplos donde la pregunta de identificabilidad se pueda atacar sin depender del
estimador v2.

Casos candidatos:

- desplazamientos de frontera sub-`ell`, `O(ell)`, `O(ell log ell)`;
- familias donde el borde físico compite con el borde de caja;
- pares de completaciones admisibles que preservan el orden observado pero alteran una propiedad
  geométrica latente;
- casos donde la misma señal causal gruesa admite varias localizaciones geométricas finas.

Entregables:

- `research_program/models/canonical_counterexamples.md`
- uno o dos asientos formales de "same observed order / different latent geometry"

### Fase D — Clases de observables

Objetivo:
subir desde "mi observable falla" a "falla esta clase de observables".

Clases iniciales razonables:

- observables basados en minimales;
- observables locales de radio efectivo acotado;
- observables de score aditivo sobre puntos;
- observables de tipo longest-chain / future-cardinality;
- observables relacionales globales.

Preguntas:

- qué gana una observable global sobre una local;
- qué parte del suelo observado viene de localización física y qué parte de mi score;
- qué clases merecen un lower bound uniforme.

### Fase E — Separar horizonte de truncación singular

Objetivo:
evitar que el programa quede preso de un mecanismo específico del modelo Schwarzschild singular.

Tareas:

- identificar qué parte del signal actual es realmente "horizon-like";
- identificar qué parte depende de futures truncados por singularidad;
- evaluar si la obstrucción observada es de frontera nula, de parche finito, o de singularidad.

Resultado esperado:
una frontera clara entre "recoverability de un singularity imprint" y "recoverability de una
estructura de horizonte" en sentido más amplio.

### Fase F — Resultados analíticos duros

Objetivo:
obtener al menos un resultado no dependiente del pipeline sellado.

Dos rutas:

1. **Upper bound:** exhibir una familia order-only que logra cierta tasa.
2. **Lower bound:** probar que ninguna regla en cierta clase supera cierta escala de error.

Requisito:
si se busca un lower bound genuino, debe trabajar sobre la ley completa del orden observado, no
sobre la salida del estimador sellado.

### Fase G — Generalización geométrica

Objetivo:
salir del caso horizonte como banco de pruebas y extender la tabla de identificabilidad a:

- fronteras causales más generales;
- proper time / geodesic proxies;
- dimensión efectiva;
- invariantes topológicos robustos;
- curvatura o acción efectiva cuando aplique.

## 6. Orden práctico recomendado

Secuencia recomendada de ejecución:

1. escribir el marco conceptual y la taxonomía;
2. extraer de `biblioteca/` una matriz rigurosa de soporte/límite;
3. definir 2-3 modelos canónicos de casi indistinguibilidad;
4. intentar el primer lower bound o resultado de contigüidad fuera del canal sellado;
5. solo después volver a nuevos algoritmos de reconstrucción.

Esto pone el peso en identificabilidad del orden, no en tuning de un pipeline.

## 7. Paquetes de trabajo inmediatos

### WP1 — Taxonomía y claim boundaries

Meta:
escribir una nota corta y usable sobre tipos de recoverability y tipos de límite.

Salida:
`research_program/taxonomy/identifiability_taxonomy.md`

### WP2 — Matriz bibliográfica

Meta:
recorrer `docs/bibliography_claims.md` y ampliarlo hacia una tabla centrada en:

- orden;
- número/volumen;
- conformalidad;
- frontera;
- topología;
- indeterminación / no-identificabilidad.

Salida:
`research_program/bibliography/identifiability_bibliography_matrix.md`

### WP3 — Familias estadísticas

Meta:
especificar familias geométricas `theta -> P_n(theta)` lo bastante simples como para probar algo.

Salida:
nota técnica en `dev/` o `docs/` con 2-3 familias modelo.

### WP4 — Contraejemplos y completaciones

Meta:
aprovechar el trabajo ya hecho en C1/completaciones para aislar ejemplos donde el orden observado
no fija cierta geometría latente.

Salida:
`research_program/models/canonical_counterexamples.md`

### WP5 — Primer lower bound real

Meta:
probar o refutar una afirmación del tipo:

> ninguna regla order-only en la clase X puede localizar la frontera mejor que escala Y en el
> régimen Z.

Salida:
una nota técnica, aunque sea parcial, que ya no dependa del canal `C -> rhat` del estimador v2.

## 8. Riesgos principales

1. **Recaer en tuning de algoritmo.**
   Eso produce mejoras locales pero no responde la pregunta fuerte.

2. **Confundir recoverability con reconstrucción.**
   El repo ya tiene esa frontera bastante bien cuidada; no debe diluirse.

3. **Sobreuniversalizar desde Schwarzschild 1+1D singular.**
   El mecanismo actual no es automáticamente horizonte-genérico.

4. **Intentar un no-go universal demasiado pronto.**
   Antes conviene obtener resultados sobre clases razonables de observables.

5. **Hablar de "principio de incertidumbre" antes de tiempo.**
   Hoy solo está justificado como brújula conceptual, no como claim físico establecido.

## 9. Regla de redacción futura

Hasta nuevo aviso, el lenguaje recomendado es:

- **admisible:** "recoverability", "order-only localisation", "operational floor",
  "identifiability", "indistinguishability", "possible order/geometry indetermination";
- **no admisible todavía como resultado:** "reconstruction", "universal information limit",
  "gravitational uncertainty principle", "no-go theorem" salvo prueba explícita.

## 10. Siguiente paso concreto

El siguiente paso útil no es código nuevo. Es cerrar **WP1 + WP2**:

1. redactar `research_program/taxonomy/identifiability_taxonomy.md`;
2. extraer de `biblioteca/` la primera matriz bibliográfica centrada en identificabilidad;
3. decidir, con esa base, cuál es la primera familia `P_n(theta)` que merece un ataque analítico.

Esa secuencia mantiene el foco en el objetivo final: el límite de la indeterminación geométrica en
general, no el rendimiento aislado del algoritmo actual.
