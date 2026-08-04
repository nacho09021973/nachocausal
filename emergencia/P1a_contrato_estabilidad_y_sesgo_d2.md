# P1a — Contrato de estabilidad y sesgo post-selección en `d=2`

> **ESTADO: CONTRATO CONGELADO v1.0 · EJECUCIÓN AUTORIZADA POR EL USUARIO ·
> P1b MÉTRICO TODAVÍA CERRADO.**
>
> Este documento se fija antes de observar los resultados del experimento. Evalúa
> el selector puntual `F_cov,3` ya congelado, sin modificar su score ni añadir un
> desempate. Las coordenadas y las alturas se usan después de seleccionar y nunca
> como entrada del selector.

## 1. Pregunta

El gate de disponibilidad anterior estableció que `F_cov,3` produce una salida
única con frecuencia operacional en la familia mínima de Minkowski. Antes de abrir
un estimador métrico se estudiarán cuatro riesgos:

1. inestabilidad de la cuádrupla bajo thinning independiente;
2. atracción de sus extremos hacia la frontera del diamante latente;
3. degeneración de alguno de los dos intervalos hacia `k_0=3`;
4. sesgo de sus alturas respecto de intervalos `1+1` no seleccionados del mismo
   tamaño.

La ley base es un sprinkling iid condicionado a `N=n` en coordenadas nulas
normalizadas:

```text
(u_i,v_i) iid Uniform([0,1]^2),
x_i prec x_j iff u_i<u_j y v_i<v_j.
```

Ordenar por `u` y reemplazar `v` por sus rangos produce una permutación uniforme.
Solo esa permutación entra en `F_cov,3`.

## 2. Selector inalterado

```text
k_0 = 3
candidate = (a,b,c,d) con a prec b prec c prec d
minimum_support = |[a,b]|>=3 y |[c,d]|>=3
score = |[a,b]| + |[c,d]|
point_output = unique maximizer or abstain
```

La implementación detallada debe coincidir con el clasificador sellado en
`p1a_enumeracion_simulacion.py`. No se admite score secundario, etiqueta natural ni
coordenada para resolver empates.

## 3. Presupuesto y semillas

```text
BASE_N = (32,48,64,96,128)
GATE_N = (64,96,128)
BASE_REPLICATES_PER_N = 12000
BASE_BATCHES = 8
BASE_REPLICATES_PER_BATCH = 1500
RNG = numpy.random.Generator(numpy.random.PCG64)

COORDINATE_SEED_BASE = 2608035000
COORDINATE_SEED(n,batch) = COORDINATE_SEED_BASE + 100*n + batch

THINNING_SEED_BASE = 2608036000
THINNING_SEED(n,batch) = THINNING_SEED_BASE + 100*n + batch

BASELINE_SEED_BASE = 2608037000
BASELINE_SEED(m) = BASELINE_SEED_BASE + m
BASELINE_REPLICATES_PER_SIZE = 4000
```

No hay parada temprana ni adaptación del presupuesto a resultados intermedios. Las
semillas de thinning están separadas de las coordenadas para que este diagnóstico no
cambie la muestra base.

## 4. Estabilidad bajo thinning order-only

Se congelan dos retenciones independientes:

```text
RETENTION = (0.90,0.80).
```

Para cada realización base y cada retención se genera una máscara Bernoulli iid. El
poset inducido por los elementos retenidos se vuelve a entregar a `F_cov,3`, sin
coordenadas ni etiquetas externas. Sus índices se traducen después a los elementos
originales únicamente para comparar salidas.

La magnitud primaria es

```text
p_same(n,p) = P(
  F_cov,3(C_thin) selecciona exactamente (a,b,c,d)
  | F_cov,3(C)=(a,b,c,d), los cuatro extremos sobreviven
).
```

También se registran:

- supervivencia de los cuatro extremos;
- existencia de cualquier salida única tras thinning;
- reselección exacta sin condicionar por supervivencia;
- Wilson bilateral del 95 % para las proporciones binomiales.

Como control de implementación, la frecuencia de supervivencia debe satisfacer

```text
|p_hat_survive - p^4|
  <= 6 sqrt(p^4(1-p^4)/U) + 1/U,
```

donde `U` es el número de selecciones únicas base. Un fallo produce
`IMPLEMENTATION_INVALID`.

## 5. Tamaños individuales

Para cada selección única se registran

```text
m_minus = |[a,b]|,
m_plus  = |[c,d]|,
m_min   = min(m_minus,m_plus),
balance = m_min / max(m_minus,m_plus).
```

El diagnóstico primario de degeneración es

```text
p_floor(n) = P(m_min=3 | seleccion unica).
```

Se reporta su intervalo Wilson del 95 %, además de medias y medianas descriptivas.

## 6. Frontera latente

Este bloque es exclusivamente diagnóstico. Para un punto `x=(u,v)` se define

```text
clearance(x) = min(u,1-u,v,1-v),
BOUNDARY_DELTA = 0.05,
near_boundary(x) = 1{clearance(x)<=BOUNDARY_DELTA}.
```

Se evalúan los cuatro extremos seleccionados y se reportan la holgura media y la
fracción cercana a frontera. Como referencia analítica, un punto uniforme no
seleccionado tiene

```text
P(near_boundary) = 1-(1-2*BOUNDARY_DELTA)^2 = 0.19.
```

Estas coordenadas no participan en la selección ni en el gate.

## 7. Alturas y baseline condicionado al tamaño

Para cada intervalo seleccionado se calcula su altura `H`, es decir, la cardinalidad
de su cadena más larga incluidos los extremos. En `d=2` se obtiene como una LIS.

El baseline de un intervalo no seleccionado de tamaño total `m` es:

```text
H_0(m) = 2 + LIS(Pi_{m-2}),
Pi_{m-2} uniforme en S_{m-2}.
```

Para cada tamaño observado se generan 4000 réplicas independientes y se estima
`mu_0(m)=E[H_0(m)]`. El residuo post-selección es

```text
R_H = H_selected - mu_0(m).
```

Se reportan medias por tamaño, por `n` y por posición anterior/posterior. No se
calcula un cociente entre alturas, no se interpreta `R_H` como tiempo y este bloque
no entra en el terminal.

## 8. Gate congelado

El terminal se decide solo con `p_same` y `p_floor` para

```text
GATE_N = (64,96,128).
```

Después de superar todos los controles de implementación:

```text
si, para cada n en GATE_N:
  Wilson95_lower(p_same(n,0.90)) >= 0.50,
  Wilson95_lower(p_same(n,0.80)) >= 0.25,
  Wilson95_upper(p_floor(n)) < 0.25:
    terminal = PASS_STABILITY_TO_P1B_DESIGN

si, para cada n en GATE_N, ocurre al menos una de estas dos condiciones:
  Wilson95_upper(p_same(n,0.90)) < 0.25,
  Wilson95_lower(p_floor(n)) > 0.75:
    terminal = PARK_POINT_SELECTOR_INSTABILITY

en otro caso:
    terminal = INCONCLUSIVE_STABILITY_GATE
```

Los umbrales son operacionales y deliberadamente exigentes. Un resultado
`INCONCLUSIVE` no autoriza a relajar umbrales después de observar los datos. La
segunda condición es un terminal de aparcamiento fuerte, no la negación de P1.

## 9. Artefactos

```text
emergencia/p1a_estabilidad_d2.py
tests/test_p1a_estabilidad_d2.py
emergencia/resultados/p1a_estabilidad_d2.csv
emergencia/resultados/p1a_thinning_d2.csv
emergencia/resultados/p1a_alturas_baseline_d2.csv
emergencia/resultados/p1a_estabilidad_resumen.json
emergencia/resultados/*.sha256
emergencia/P1a_resultados_estabilidad_y_sesgo_d2.md
```

Los CSV usarán LF. La escritura será atómica y rechazará sobrescrituras salvo opción
explícita. Una segunda ejecución deberá producir artefactos byte a byte idénticos.

## 10. Techo de afirmación

La ejecución podrá describir robustez de la cuádrupla, localización latente, tamaños
y sesgo de altura en la familia bidimensional congelada. No podrá sostener:

- identificabilidad de tiempo métrico;
- consistencia de un cociente de alturas;
- independencia entre los dos intervalos;
- validez en `d>=3`;
- universalidad frente a otras regiones o sprinklings;
- ni novedad certificada.

```text
P1A_STABILITY_EXECUTION_AUTHORIZED = YES
P1A_DIMENSION = 2
P1A_METRIC_RATIO_AUTHORIZED = NO
P1A_HIGHER_DIMENSIONS_AUTHORIZED = NO
P1A_STABILITY_CONTRACT_STATUS = FROZEN_BEFORE_RESULTS
```
