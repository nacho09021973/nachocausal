# Identificabilidad del tiempo métrico desde orden causal finito

> **ESTADO: BORRADOR PROGRAMÁTICO v0.2 · LÍNEA INDEPENDIENTE · REVISABLE.**
>
> Este documento abre una línea de investigación dentro del laboratorio `nachocausal`.
> No es una preregistración, no contiene un resultado, no autoriza simulaciones y no
> reabre ni prolonga la línea de reconstrucción de horizontes. Su primera función es
> formular correctamente el problema antes de elegir modelos, observables o métodos.

La secuencia de resultados, decisiones cerradas y próximos gates se mantiene en:

```text
emergencia/HOJA_DE_RUTA.md
```

## 1. Posición dentro del laboratorio

`nachocausal` se entiende como un laboratorio con varias líneas de investigación que
comparten herramientas conceptuales y matemáticas, pero no necesariamente objetivos,
contratos ni techos de afirmación.

Esta línea estudia una pregunta independiente:

> ¿Qué información sobre duración, tiempo propio y geometría temporal puede
> identificarse a partir de un orden causal finito, y qué parte permanece
> indeterminada por razones estructurales del canal de observación?

La línea es deliberadamente más ambiciosa y difícil que las investigaciones acotadas a
un observable o una geometría concreta. El objetivo no es encontrar rápidamente un nuevo
estimador, sino separar con rigor:

1. la orientación causal `antes/después`;
2. la duración métrica entre eventos;
3. la escala temporal absoluta;
4. las razones temporales adimensionales;
5. una coordenada o función de tiempo;
6. y la posible reconstrucción de una geometría lorentziana.

Estas seis nociones no son intercambiables. En un causal set, el orden parcial ya
contiene una orientación causal. Lo que debe demostrarse, y no suponerse, es cuándo de
ese orden y de la información de conteo emerge una noción métrica de tiempo.

## 2. Objeto matemático inicial

Sea `C` un poset finito no etiquetado interpretado como orden causal observado. Cuando
exista una geometría latente, escribiremos

```text
(M, g, mu, rho) -> muestra finita -> C
```

donde:

- `(M,g)` es una región lorentziana admisible;
- `mu` es la medida de volumen inducida o una medida de muestreo expresamente fijada;
- `rho` es la densidad, cuando forme parte del modelo;
- las coordenadas, etiquetas y el embedding se olvidan al construir la observación
  order-only.

Para elementos comparables `x prec y`, sea `L_C(x,y)` la longitud de una cadena máxima
entre ambos. En familias manifold-like, un candidato clásico a tiempo propio discreto es

```text
tau_hat(x,y) = L_C(x,y) / (m_d rho)^(1/d),
```

con dimensión `d`, densidad `rho` y constante dimensional `m_d` conocidas. Esta fórmula
es un punto de partida bibliográfico, no una conclusión de esta línea. Sus hipótesis, sesgo,
fluctuaciones, dependencia de borde y validez en curvatura deben tratarse como parte del
problema.

### 2.1 Canales de observación que no deben mezclarse

1. **Poset + cardinalidad condicionada a `N=n`.** Se observa la clase de isomorfía
   del poset y se conoce `n`, pero su valor fue fijado por diseño. La escala absoluta
   puede desaparecer al eliminar la ley de muestreo de `N`.
2. **Poset + conteo aleatorio, con densidad desconocida.** Se observa el poset y el
   valor aleatorio de `N`, pero el conteo puede identificar solo una combinación de
   volumen y densidad.
3. **Poset + conteo aleatorio, con densidad conocida.** La ley de `N` puede portar
   volumen y restaurar una escala física dentro de una familia geométrica fijada.
4. **Orden + input geométrico externo.** Se proporcionan anclas, coordenadas, una
   frontera, un embedding parcial u otra calibración. Es un canal reforzado y no debe
   presentarse como order-only.

Toda afirmación futura deberá nombrar su canal.

## 3. Las tres preguntas fundacionales

### P1. ¿Qué razones de tiempos propios son identificables desde un poset a cardinalidad fija?

La ceguera de escala absoluta no implica automáticamente ceguera sobre toda estructura
temporal. Cantidades invariantes bajo una dilatación global pueden seguir estando presentes
en la ley del orden.

El primer target candidato es una razón adimensional

```text
R(g) = tau_g(p1,q1) / tau_g(p2,q2),
```

para dos pares temporales comparables definidos mediante una regla que no utilice las
coordenadas latentes. Una versión basada en cadenas sería

```text
R_hat(C) = L_C(x1,y1) / L_C(x2,y2).
```

La dificultad principal aparece antes de estudiar la consistencia de `R_hat`: hay que
definir los pares `(x1,y1)` y `(x2,y2)` de forma intrínseca, covariante y no circular.
Seleccionar los extremos usando el embedding oculto convertiría el problema en un canal
con input geométrico externo.

Preguntas subordinadas:

- ¿Qué reglas order-only pueden seleccionar pares o intervalos comparables?
- ¿La razón de cadenas converge a una razón de tiempos propios bajo hipótesis verificables?
- ¿Qué información se pierde al pasar de un causal set etiquetado a su clase de
  isomorfía no etiquetada?
- ¿Existen familias distintas con la misma ley condicionada a `N=n` pero diferentes razones de
  tiempos propios?
- ¿El target es identificable para un ensemble pero no para una sola realización finita?

Estado inicial:

```text
P1_STATUS = P1A_D2_COUNT_VOLUME_OPEN_HEIGHT_WIDTH_PARKED_RATIO_CLOSED
```

La capa definicional se desarrolla en:

```text
emergencia/P1a_seleccion_intrinseca_y_automorfismos.md
```

P1a demuestra que la selección puntual está condicionada por los automorfismos del
poset y adopta como salida primaria un par ordenado único o abstención. Esto no resuelve
todavía la correspondencia entre razones de cadenas y razones de tiempos propios.
El primer selector concreto se congela en:

```text
emergencia/P1a_primer_selector_de_cobertura.md
```

La regla maximiza la cobertura total de dos intervalos ordenados y disjuntos, sin
optimizar su balance ni su futuro cociente de alturas.
La primera puerta teórica en la familia Minkowski se documenta en:

```text
emergencia/P1a_puerta_teorica_en_Minkowski.md
```

Allí el evento vacío se cierra mediante la altura del poset y el caso `d=2` se reduce
a conteos exactos sobre permutaciones; Monte Carlo y evaluación métrica permanecen
cerrados.
La ejecución autorizada y sus límites se registran en
`emergencia/P1a_resultados_enumeracion_y_monte_carlo_d2.md`.
El gate posterior de estabilidad, frontera, tamaños y altura se registra en:

```text
emergencia/P1a_contrato_estabilidad_y_sesgo_d2.md
emergencia/P1a_resultados_estabilidad_y_sesgo_d2.md
```

La identidad de la cuádrupla resulta estable bajo thinning, pero uno de los dos
intervalos cae en `k_0=3` en aproximadamente tres cuartas partes de las selecciones
del régimen alto estudiado. Por ello no se abre todavía la ejecución del cociente de
alturas: P1a debe comparar nuevos scores order-only que protejan el soporte mínimo
sin usar la magnitud que después se pretende estimar.

Esa comparación posterior se congeló y completó en:

```text
emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md
emergencia/P1a_resultados_comparacion_selectores_balanceados_d2.md
```

El gate selecciona `MIN_COVERAGE_LEX`, que maximiza primero el tamaño del intervalo
menor y después la cobertura total. En la nueva muestra elimina el suelo observado,
mantiene disponibilidad y supera el gate de thinning. La elección autoriza diseñar
un gate de sesgo de alturas por intervalo; no autoriza todavía ejecutar ni
interpretar un cociente temporal.

El gate autorizado se congeló y completó en:

```text
emergencia/P1a_contrato_gate_altura_duracion_lex_d2.md
emergencia/P1a_resultados_gate_altura_duracion_lex_d2.md
```

La altura `H/(2 sqrt(n))` reproduce razonablemente la escala media y el target
latente es estable bajo thinning, pero la correlación individual altura–duración
queda entre 0.22 y 0.29. El terminal fuerte es
`PARK_LEX_HEIGHT_REPRESENTATION`; por tanto no se preregistra ni ejecuta el cociente
de alturas. Permanecen abiertas otras representaciones, densidades y targets.

Dos representaciones alternativas se congelaron y evaluaron en:

```text
emergencia/P1a_contrato_representaciones_alternativas_d2.md
emergencia/P1a_resultados_representaciones_alternativas_d2.md
```

La media altura–anchura queda fuertemente aparcada. La representación de volumen por
conteo `sqrt((m-2)/(n-2))` mejora la correlación individual hasta aproximadamente
`0.53–0.57`, pero no alcanza el umbral `0.80`. Esa rama permanece abierta para una
teoría condicionada por selección; ningún cociente queda autorizado.

### P2. ¿Qué información temporal absoluta reaparece al observar `N` con `rho` conocida?

En el canal condicionado a `N=n`, una dilatación global puede preservar exactamente la
ley del poset no etiquetado y destruir la identificabilidad de la escala absoluta. Cuando
se conserva la ley aleatoria de `N` y `rho` es conocida, el conteo contiene información de
volumen. La pregunta es cuánta de esa escala volumétrica puede convertirse rigurosamente
en escala temporal.

El target candidato es

```text
T(g) = tau_g(p,q)
```

en unidades absolutas y bajo una familia geométrica congelada. No basta con observar que
`E[N] = rho Vol_g(M)`: volumen total, dimensión, forma de la región y tiempo propio no son
la misma magnitud.

Preguntas subordinadas:

- ¿Qué hipótesis convierten `orden + número` en una calibración temporal y no solo
  volumétrica?
- ¿La densidad debe conocerse exactamente o puede estimarse dentro del mismo canal?
- ¿Qué degeneraciones sobreviven aunque se conozca `rho`?
- ¿Qué tasa de error finito impone la fluctuación de Poisson de `N`?
- ¿Es posible separar error de conteo, error de cadena, curvatura y efectos de borde?
- ¿Qué cambia entre regiones de Minkowski, diamantes causales curvos y familias
  lorentzianas más generales?

Estado actual:

```text
P2_STATUS = MINIMAL_FAMILY_CLOSED_GENERAL_PROBLEM_OPEN
```

### P3. ¿Qué cotas finitas separan los teoremas asintóticos del régimen realmente observable?

Los resultados de reconstrucción o unicidad en alta densidad no determinan por sí solos
qué puede inferirse de un poset finito de tamaño moderado. Esta pregunta busca convertir
la afirmación cualitativa `el error tiende a cero` en una teoría cuantitativa de resolución
temporal.

La unidad estadística será una familia de leyes `P_n(theta)` o `P_rho(theta)` sobre
posets finitos. Para un target temporal `T(theta)` deben distinguirse dos direcciones:

```text
upper bound: existe un estimador con riesgo <= a_n;
lower bound: ningún estimador medible puede tener riesgo < b_n.
```

Solo cuando `a_n` y `b_n` estén controlados en una familia común podrá hablarse de una
escala de resolución temporal del canal.

Preguntas subordinadas:

- ¿Qué error finito tiene el estimador de cadena máxima en cada familia admisible?
- ¿Qué condiciones de `well-conditioned embedding` pueden verificarse desde el dato
  observado y cuáles son hipótesis externas?
- ¿Cuál es la dependencia explícita del error respecto de `n`, `rho`, dimensión,
  curvatura, volumen y distancia al borde?
- ¿Pueden construirse pares de geometrías con targets temporales separados pero leyes
  de posets próximas en TV, Hellinger o KL?
- ¿Existe una frontera entre recoverability asintótica y no-identificabilidad práctica
  a densidades finitas?
- ¿Qué resultados son ensemble-level y cuáles garantizan algo para una realización
  individual?

Estado inicial:

```text
P3_STATUS = OPEN_FINITE_SAMPLE_THEORY
```

## 4. Por qué esta línea es especialmente difícil

1. **El orden ya presupone orientación causal.** No se puede presentar la recuperación
   de `antes/después` como emergencia del tiempo métrico.
2. **La escala puede ser invisible.** Cardinalidad condicionada, conteo aleatorio con
   densidad desconocida y conteo aleatorio con densidad conocida son experimentos
   estadísticos diferentes. Todos observan el número; no todos conservan su información
   de muestreo ni permiten calibrarlo.
3. **Los endpoints no vienen dados.** Medir tiempo propio entre puntos seleccionados por
   coordenadas ocultas no resuelve el problema order-only.
4. **Manifold-likeness no está garantizada.** La mayoría de los posets finitos no se
   parecen a un espacio-tiempo lorentziano suave.
5. **El borde puede dominar.** Una región finita puede producir señales temporales que
   pertenecen al recorte de observación y no a la geometría interior.
6. **Asintótico no significa operativo.** Una unicidad en el límite de alta densidad
   puede coexistir con un problema estadísticamente intratable a los `n` accesibles.
7. **Tiempo, volumen y dimensión están acoplados.** El conteo no calibra una duración
   sin hipótesis adicionales.
8. **Una realización no es una ley.** La identificabilidad del modelo y la estimación
   desde un solo causal set son niveles distintos.
9. **La extensión cuántica es otra capa.** Este primer programa es clásico-estadístico;
   Page–Wootters, POVM, superposición de órdenes y back-reaction no se incorporan sin
   una reformulación expresa.

## 5. Relación con otras líneas de `nachocausal`

Esta investigación puede reutilizar infraestructura intelectual del laboratorio:

- leyes `P_n(theta)` sobre posets no etiquetados;
- separación estricta de canales de observación;
- TV, Hellinger, KL, contigüidad y cotas de dos puntos;
- distinción entre recoverability, localización, reconstrucción e identificabilidad;
- separación entre límite de estimador, límite de familia y límite intrínseco.

No puede heredar automáticamente:

- conclusiones físicas sobre horizontes;
- constantes o tasas probadas en una familia geométrica distinta;
- resultados de un estimador como si fueran propiedades del orden completo;
- afirmaciones condicionadas a `N=n` como si cubrieran el canal de conteo Poisson;
- ni teoremas asintóticos como garantías numéricas para `n` moderado.

La independencia de la línea significa que su éxito o fracaso no rescata ni refuta otras
investigaciones del laboratorio.

## 6. Secuencia de trabajo propuesta

### Fase T0 — Auditoría conceptual y bibliográfica

- fijar una taxonomía de tiempo causal, tiempo métrico, escala y reloj interno;
- extraer los teoremas exactos sobre cadenas máximas, proper time, reconstrucción y
  unicidad de embeddings;
- registrar hipótesis, dimensión, canal y naturaleza asintótica o finita de cada resultado;
- separar artículos revisados por pares de preprints recientes.

### Fase T1 — Definición de targets y canales

- escoger una primera familia lorentziana controlada;
- definir endpoints o intervalos de forma order-only;
- congelar por separado un target adimensional y uno absoluto;
- declarar la pérdida usada y la clase de estimadores.

### Fase T2 — Teoría de identificabilidad

- buscar equivalencias exactas y órbitas de escala;
- construir pares adversariales;
- obtener cotas de TV, Hellinger o KL;
- estudiar consistencia y tasas del funcional de cadena máxima.

### Fase T3 — Puente finito/asintótico

- hacer explícitas las constantes y escalas de los teoremas;
- separar interior, borde y curvatura;
- determinar si las cotas son informativas en algún régimen finito.

### Fase T4 — Ejecución, solo tras contrato independiente

No se propone todavía un experimento. Cualquier simulación futura requerirá una
preregistración propia con familia, canal, seeds, tamaños, estimadores, controles,
presupuesto y terminales congelados.

## 7. Techo de afirmación inicial

Hasta que existan teoremas o evidencia bajo contratos expresos:

### Lenguaje admisible

- `candidate temporal observable`;
- `order-only temporal ratio`;
- `scale blindness at fixed cardinality` cuando se cite el teorema aplicable;
- `order+number temporal calibration question`;
- `finite-density temporal resolution`;
- `identifiability remains open`.

### Lenguaje no admisible

- `el tiempo emerge de los causal sets` como conclusión general;
- `reconstrucción del tiempo` sin target, canal y pérdida;
- `principio de incertidumbre temporal` sin una formulación matemática nueva;
- `límite fundamental` inferido del fracaso de un estimador;
- `confirmación de gravedad cuántica`;
- `unicidad geométrica a n finito` deducida de un resultado asintótico.

## 8. Fuentes iniciales para la auditoría T0

Estas referencias abren el mapa; su inclusión no significa que sus resultados hayan sido
transferidos a una familia de `nachocausal`.

1. Sumati Surya, *The causal set approach to quantum gravity*, Living Reviews in
   Relativity 22 (2019), arXiv:1903.11544.
2. Joachim Kambor y Nomaan X, *Manifold Properties from Causal Sets using Chains*,
   Class. Quantum Grav. 37 (2020), arXiv:2007.03835.
3. Steven Johnston, *Simpler embeddings of causal sets into Minkowski spacetime*,
   Phys. Rev. D 111 (2025), arXiv:2502.09701.
4. Mathias Braun, *Spacetime reconstruction by order and number*, arXiv:2507.01907
   (preprint).
5. Nathan Madsen, *On the Uniqueness of Embeddings of Causal Sets*, arXiv:2607.05840
   (preprint).
6. Stav Zalel, *Covariant Growth Dynamics*, arXiv:2302.10582, como frontera con una
   futura pregunta distinta sobre devenir y dinámica.

## 9. Primera decisión resuelta y siguiente decisión pendiente

La primera decisión se ha resuelto mediante el modelo mínimo desarrollado en:

```text
emergencia/T0_modelo_minimo_y_proposicion_cero.md
```

La familia inicial son diamantes causales completos de Minkowski con dimensión y forma
conocidas. El primer contraste enfrenta cardinalidad condicionada a `N=n` con conteo
Poisson a densidad conocida. El target es la duración total del diamante latente, por lo
que no requiere seleccionar endpoints dentro del poset observado.

La decisión pendiente siguiente pertenece a P1:

> ¿Cómo definir dos intervalos temporales mediante una regla equivariante e intrínseca
> del poset no etiquetado, sin introducir coordenadas, extremos externos ni desempates
> dependientes de etiquetas?

El primer avance sobre esa decisión queda fijado en
`emergencia/P1a_seleccion_intrinseca_y_automorfismos.md`: criterio de punto fijo,
contraejemplos universales y selector parcial sin desempate. Permanece abierta la
elección de un score no circular y la posterior identificabilidad métrica.
