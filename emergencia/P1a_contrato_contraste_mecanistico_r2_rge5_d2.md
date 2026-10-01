# P1a — Contrato post-hoc del contraste combinatorio `R=2` frente a `R>=5`

```text
ESTADO = CONGELADO_ANTES_DE_EJECUCION
FECHA = 2026-08-27
PHASE = POST_HOC_EXPLORATORY_R2_VS_RGE5_MECHANISTIC_CONTRAST
SELECTOR = MIN_COVERAGE_LEX
K0 = 3 (INVARIABLE)
N = 22,24,40 (INVARIABLE)
GROUPS = R_EQ_2, R_GE_5 (INVARIABLE)
CLAIM_CEILING = FINITE_N_POST_HOC_DESCRIPTIVE_MECHANISTIC_CONTRAST
```

## 1. Pregunta única y población

Para cada permutación uniforme `sigma in S_n`, el backend orbital validado calcula
el argmax completo `M(C_sigma)`, su partición en órbitas bajo `Aut(C_sigma)` y

`R(C_sigma) = |M(C_sigma)/Aut(C_sigma)|`.

La única pregunta es si alguna propiedad combinatoria predefinida separa más los
casos `R=2` y `R>=5` en la ventana observada `n=22,24` que en el control de
reconcentración `n=40`.

Se excluyen exactamente `EMPTY`, `R=1` y `R=3,4`. No se reagruparán tras observar
los resultados. El control `n=40` no podrá cambiarse.

La unidad estadística y de bootstrap es siempre una configuración/permutación.
Los candidatos y órbitas internos de una misma configuración nunca se tratan como
observaciones independientes.

## 2. Fuentes exactas reutilizadas

No se modifica ningún instrumento previo. Se reutilizan:

- `p1a_orbital_backend_preflight_d2.evaluate_orbital_backend`, con
  `complete_orbits=False`; para todo `R>1` la enumeración completa de
  automorfismos y la partición completa en órbitas son obligatorias;
- `p1a_orbital_backend_preflight_d2.materialize_lex_maximizers`, que devuelve el
  mismo `M(C)` y el score máximo exacto;
- las definiciones `ScoreLevel.candidate_count`, `orbit_count` y `orbit_sizes` de
  `p1a_paisaje_niveles_d2.py`;
- el muestreo PCG64 y las semillas de la campaña de multiplicidad orbital;
- el bootstrap percentil iid ya usado en esa campaña.

La tabla de multiplicidad previa sólo conserva conteos por `(n,R)` y no contiene
descriptores por configuración. Por ello se reproduce determinísticamente la misma
muestra; no se genera un diseño muestral nuevo.

## 3. Observables congelados

La lista queda cerrada en los seis escalares siguientes. Todos son por configuración.

### X1 — `n_maximizers`

`X1(C)=|M(C)|`.

Se obtiene de `BackendResult.n_maximizers`, equivalente al `candidate_count` del
nivel superior del paisaje exacto. Describe cuántos candidatos empatan antes del
cociente orbital.

### X2 — `n_automorphisms`

`X2(C)=|Aut(C)|`.

Se obtiene de `BackendResult.n_automorphisms`. Sólo se acepta cuando
`automorphism_enumeration_complete=True`. Describe el tamaño exacto del grupo que
actúa sobre los maximizadores.

### X3 — `primary_score`

Para todo `(a,b,c,d) in M(C)`, sea `C_xy=|[x,y]|`. Entonces

`X3(C)=min(C_ab,C_cd)`.

Es la primera coordenada del score lexicográfico máximo devuelto por
`materialize_lex_maximizers`.

### X4 — `secondary_score`

Para todo `(a,b,c,d) in M(C)`,

`X4(C)=C_ab+C_cd`.

Es la segunda coordenada del mismo score máximo. `X3` y `X4` describen la geometría
de cobertura del nivel ganador, no niveles cercanos ni gaps.

### X5 — `mean_orbit_size`

Si las órbitas del máximo son `O_1,...,O_R`,

`X5(C)=R^{-1} sum_i |O_i| = |M(C)|/R`.

Es la media aritmética de `ScoreLevel.orbit_sizes`, reducida a un escalar por
configuración. Describe cuántos candidatos equivalentes contiene una órbita típica.

### X6 — `max_orbit_size`

`X6(C)=max_i |O_i|`.

Se obtiene de la misma distribución exacta `orbit_sizes`. Describe la órbita ganadora
de mayor cardinalidad sin crear una distancia, solapamiento o geometría nueva.

No se incorporarán otros observables después del run. En particular no se crearán
medidas de solapamiento, separación, gap, near-maximizers, temperatura ni `Xi`.

## 4. Muestreo y clasificación congelados

```text
N_MC = 100000 por n
N_VALUES = 22,24,40
GENERATOR = numpy.random.Generator(PCG64)
SCIENTIFIC_SEED(n) = 260828000 + n
INSTANCE_TIMEOUT = 5 s
```

Para cada configuración se ejecuta el backend una vez. Sólo si su estado es no vacío
se recupera de nuevo el score mediante la primitiva exacta y se exige igualdad exacta
del conjunto de maximizadores. Los descriptores nunca alteran `R` ni su clasificación.

Los conteos `EMPTY`, `R=1`, `R=2`, `R=3,4`, `R>=5` deben reproducir exactamente la
campaña sellada anterior antes de aceptar los resultados descriptivos.

## 5. Estadísticos congelados

Para cada observable `X`, cada `n` y los grupos fijos `G2={R=2}` y `G5={R>=5}`:

`mu_2(n)=E[X | R=2,n]`,

`mu_5(n)=E[X | R>=5,n]`,

`Delta_X(n)=mu_5(n)-mu_2(n)`.

Para hacer comparables escalas que cambian con `n`, se reporta además Cohen `d`:

`d_X(n)=Delta_X(n)/s_pooled(n)`,

donde

`s_pooled^2=((N2-1)s2^2+(N5-1)s5^2)/(N2+N5-2)`

y `s2^2,s5^2` son varianzas muestrales con denominador `N-1`. Si la varianza pooled
es cero, `d` se reporta `NA`; nunca se sustituye por cero.

No habrá p-valores, corrección múltiple, ranking por significación ni selección del
«mejor» observable. La comparación de ventana frente a control será descriptiva a
partir de `Delta_X`, `d_X` y sus intervalos. No se fija un PASS/FAIL artificial.

## 6. Incertidumbre congelada

```text
BOOTSTRAP_REPLICATES = 1000
BOOTSTRAP_UNIT = configuration/permutation
BOOTSTRAP_INTERVAL = percentile 2.5%,97.5%; quantile method=linear
BOOTSTRAP_SEED(n) = 2608276000 + n
```

En cada réplica se remuestrea con reemplazo e independientemente dentro de `G2` y
`G5`, conservando sus tamaños observados. Los mismos índices remuestreados se usan
para los seis observables de una configuración, preservando su dependencia interna.
Se obtienen IC 95 % para `mu_2`, `mu_5`, `Delta_X` y Cohen `d`.

Los intervalos son descriptivos post-hoc, no teoría asintótica ni tests confirmatorios.

## 7. Figuras congeladas antes del run

Se producirán exactamente dos PNG estáticos:

1. **Figura A — medias por grupo**: matriz `2x3` de dot-and-interval plots, una faceta
   por observable. Eje x discreto `n=22,24,40`; dos marcadores desplazados para
   `R=2` y `R>=5`, con medias e IC bootstrap 95 %. Paleta de dos raíces y formas de
   marcador distintas; cada faceta usa su propia escala y explicita la unidad.
2. **Figura B — diferencias**: matriz `2x3` de dot-and-interval plots de
   `Delta_X(n)=mu_5-mu_2`, con línea horizontal cero e IC bootstrap 95 %. Una sola
   raíz cromática más neutros. No se ordenarán las facetas por tamaño del efecto.

Ambas figuras mantendrán el orden preregistrado `X1,...,X6`, títulos descriptivos,
fase post-hoc, grupos, tamaños muestrales y control `n=40`. No se añadirán figuras.

## 8. Guardas y artefactos

Guardas obligatorias:

- `R` procede exclusivamente de `n_orbits_on_m`;
- `BACKEND_FAILURES=0`;
- `EMPTY+R1+R2+R3_4+RGE5=N_total` en cada `n`;
- para cada caso usado, enumeración completa, `sum(orbit_sizes)=|M|`,
  `len(orbit_sizes)=R`, score no nulo y maximizers idénticos en ambos accesos;
- los observables son deterministas y no cambian la clasificación;
- los cinco conteos reproducen exactamente el JSON de multiplicidad previo;
- recomposición independiente desde el CSV largo reproduce la tabla resumen.

Salidas nuevas, sin sobrescritura:

- CSV resumen por `(n,observable)`;
- CSV largo por `(n,sample_index,group,observable)` para las configuraciones usadas;
- JSON de diseño, procedencia, conteos, controles y resultados;
- sidecars SHA-256;
- un script de visualización y exactamente dos figuras;
- tests focalizados del instrumento.

## 9. Claim ceiling y terminal

Sólo se permiten afirmaciones `POST_HOC_EXPLORATORY` sobre si un descriptor distingue
alta multiplicidad en general o si su separación observada parece reforzada en
`n=22,24` respecto de `n=40`. Una separación comparable en `n=40` se clasificará
como `SEPARATION_PRESENT_BUT_NOT_WINDOW_SPECIFIC`; la ausencia de una separación
descriptiva como `NO_MECHANISTIC_SEPARATOR_FOUND`.

No se permite causalidad, mecanismo demostrado, transición, escala crítica, RG,
universalidad, termodinámica, ley de escala ni comportamiento asintótico.

El terminal operativo es `R2_RGE5_COMBINATORIAL_CONTRAST_COMPLETED` o
`R2_RGE5_COMBINATORIAL_CONTRAST_BLOCKED`. Tras él no se abre otro frente.
