# P1a — Contrato de comparación de selectores balanceados en `d=2`

> **ESTADO: CONTRATO CONGELADO v1.0 · EJECUCIÓN AUTORIZADA POR EL USUARIO ·
> MUESTRA NUEVA · COCIENTE DE ALTURAS FUERA DE ALCANCE.**
>
> Este contrato se fija después de diagnosticar la degeneración de `F_cov,3`, pero
> antes de observar ningún resultado de los dos scores nuevos. Compara reglas de
> selección order-only; no modifica retroactivamente el selector anterior.

## 1. Pregunta

El selector de cobertura total es estable bajo thinning, pero deja uno de los dos
intervalos en `k_0=3` en aproximadamente tres cuartas partes de las selecciones del
régimen alto estudiado. Se compararán dos alternativas que protegen primero el
soporte menor:

```text
S_min(q) = min(m_minus(q),m_plus(q)),

S_lex(q) = (
  min(m_minus(q),m_plus(q)),
  m_minus(q)+m_plus(q)
),
```

donde `S_lex` se maximiza lexicográficamente. El selector anterior

```text
S_cov(q)=m_minus(q)+m_plus(q)
```

se repite como benchmark contemporáneo sobre exactamente los mismos posets.

## 2. Dominio común y política de empate

Los tres scores usan el mismo conjunto:

```text
Q_3(C) = {
  (a,b,c,d):
  a prec b prec c prec d,
  |[a,b]|>=3,
  |[c,d]|>=3
}.
```

Nombres congelados:

```text
COVERAGE          = maximiza S_cov;
MIN_ONLY          = maximiza S_min;
MIN_COVERAGE_LEX  = maximiza S_lex.
```

Cada regla produce la única cuádrupla maximizadora o se abstiene. No hay desempate
por etiqueta, coordenadas, altura, orden de almacenamiento ni aleatoriedad. En
particular, `MIN_COVERAGE_LEX` es un selector distinto, no un desempate aplicado
después de ejecutar `MIN_ONLY`.

## 3. Ley, muestra y semillas

La ley sigue siendo el poset producto de un sprinkling condicionado a `N=n`:

```text
(u_i,v_i) iid Uniform([0,1]^2),
x_i prec x_j iff u_i<u_j y v_i<v_j.
```

Se usa una muestra nueva, independiente de los dos experimentos anteriores:

```text
BASE_N = (32,48,64,96,128)
GATE_N = (64,96,128)
BASE_REPLICATES_PER_N = 12000
BASE_BATCHES = 8
BASE_REPLICATES_PER_BATCH = 1500
RETENTION = (0.90,0.80)
RNG = numpy.random.Generator(numpy.random.PCG64)

COORDINATE_SEED_BASE = 2608038000
COORDINATE_SEED(n,batch) = COORDINATE_SEED_BASE + 100*n + batch

THINNING_SEED_BASE = 2608039000
THINNING_SEED(n,batch) = THINNING_SEED_BASE + 100*n + batch
```

Los tres selectores reciben la misma permutación en cada réplica y el mismo subposet
inducido en cada thinning. Esta aleatoriedad común permite comparaciones pareadas.
No hay parada temprana ni adaptación del presupuesto.

## 4. Magnitudes primarias

Para cada `(selector,n)` se registran:

```text
p_empty,
p_unique,
p_tie,
p_floor = P(min(m_minus,m_plus)=3 | unique),
media y mediana de min(m_minus,m_plus),
media y mediana de min(m_minus,m_plus)/max(m_minus,m_plus).
```

Se reportan intervalos Wilson bilaterales del 95 % para los estados y para
`p_floor`. Los intervalos son descriptivos marginales, no una familia de tests
simultáneos.

## 5. Estabilidad

Para cada selector y retención se estima:

```text
p_same(n,p) = P(
  el subposet selecciona exactamente los mismos (a,b,c,d)
  | la base es unique y sobreviven los cuatro extremos
).
```

Como control de implementación, para cada `(selector,n,p)`:

```text
|p_hat_survive-p^4|
  <= 6 sqrt(p^4(1-p^4)/U)+1/U,
```

donde `U` es el número de salidas únicas base. El control se omite solo si `U=0`,
caso que por sí mismo impide cualificar al selector. Cualquier control ejecutable
que falle produce `IMPLEMENTATION_INVALID`.

## 6. Frontera latente

Después de seleccionar se evalúa, sin realimentar la regla:

```text
clearance(x)=min(u,1-u,v,1-v),
BOUNDARY_DELTA=0.05,
near_boundary(x)=1{clearance(x)<=0.05}.
```

Se reportan fracción de extremos cercanos, clearance medio y enriquecimiento frente
a la referencia uniforme `0.19`. Este diagnóstico no entra en el terminal porque no
separa el efecto de ser extremo causal del efecto propio del score.

## 7. Comparación pareada

Para cada par de selectores se registran:

- número de realizaciones donde ambos son únicos;
- número donde solo uno es único;
- coincidencia exacta de cuádruplas condicionada a unicidad de ambos.

No se construye un p-valor ni un ranking continuo post hoc. La selección final usa
únicamente el gate preespecificado.

## 8. Gate de cualificación

`COVERAGE` es benchmark y no puede ser elegido. Un candidato nuevo cualifica si,
para cada `n` en `(64,96,128)`:

```text
Wilson95_lower(p_unique) >= 0.10,
Wilson95_lower(p_same(n,0.90)) >= 0.50,
Wilson95_lower(p_same(n,0.80)) >= 0.25,
Wilson95_upper(p_floor) < 0.25.
```

Los umbrales de disponibilidad y estabilidad son los ya usados en los gates
anteriores. El umbral de suelo exige que el defecto que motivó el rediseño no sea
dominante.

Decisión congelada:

```text
si MIN_ONLY cualifica:
  terminal = SELECT_MIN_ONLY_FOR_HEIGHT_BIAS_GATE

si MIN_ONLY no cualifica y MIN_COVERAGE_LEX cualifica:
  terminal = SELECT_MIN_COVERAGE_LEX_FOR_HEIGHT_BIAS_GATE

si ninguno cualifica:
  terminal = NO_BALANCED_SELECTOR_QUALIFIES
```

La prioridad de `MIN_ONLY` se fija por parsimonia: si la regla primaria basta, no se
añade cobertura total como segundo componente. El terminal autoriza diseñar un gate
de alturas y target latente para el selector elegido; no autoriza todavía calcular
un cociente métrico.

## 9. Validación obligatoria

Antes de ejecutar la muestra completa:

- los tres argmax deben coincidir con una enumeración ingenua de cuádruplas para
  todas las permutaciones de `n=6,7`;
- `COVERAGE` debe coincidir con el clasificador sellado;
- los estados deben formar una partición exacta;
- el thinning debe preservar comparabilidades;
- y deben probarse casos de cadena total con empate y unicidad conocidos.

## 10. Artefactos

```text
emergencia/p1a_comparar_selectores_d2.py
tests/test_p1a_comparar_selectores_d2.py
emergencia/resultados/p1a_comparacion_selectores_d2.csv
emergencia/resultados/p1a_comparacion_thinning_d2.csv
emergencia/resultados/p1a_comparacion_pareada_selectores_d2.csv
emergencia/resultados/p1a_comparacion_selectores_resumen.json
emergencia/resultados/*.sha256
emergencia/P1a_resultados_comparacion_selectores_balanceados_d2.md
```

Los artefactos usarán LF, escritura atómica y rechazo de sobrescritura salvo opción
explícita. Una segunda ejecución deberá producir resultados byte a byte idénticos.

## 11. Techo de afirmación

Esta comparación puede elegir una regla para el siguiente gate interno en la familia
bidimensional congelada. No demuestra:

- que la regla elegida mida tiempo propio;
- que una razón de alturas sea consistente o identificable;
- que el target latente sea estable;
- validez en `d>=3`;
- optimalidad entre todos los scores intrínsecos;
- ni novedad certificada.

```text
P1A_BALANCED_SELECTOR_EXECUTION_AUTHORIZED = YES
P1A_DIMENSION = 2
P1A_COMMON_RANDOM_NUMBERS = YES
P1A_HEIGHT_RATIO_AUTHORIZED = NO
P1A_HIGHER_DIMENSIONS_AUTHORIZED = NO
P1A_BALANCED_SELECTOR_CONTRACT_STATUS = FROZEN_BEFORE_RESULTS
```
