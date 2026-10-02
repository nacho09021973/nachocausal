# P1a — Contrato post-hoc de multiplicidad orbital exacta del máximo en `d=2`

```text
ESTADO = CONGELADO_ANTES_DE_EJECUCION
FECHA = 2026-08-27
PHASE = POST_HOC_EXPLORATORY_ORBITAL_MULTIPLICITY
SELECTOR = MIN_COVERAGE_LEX
K0 = 3 (INVARIABLE)
CLAIM_CEILING = FINITE_N_POST_HOC_DESCRIPTIVE_THROUGH_N40
```

## 1. Pregunta única y población

Para la permutación uniforme `sigma in S_n`, sea `M(C_sigma)` el argmax completo
del selector congelado y

`R(C_sigma) = |M(C_sigma) / Aut(C_sigma)|`.

La pregunta es si, entre los casos con rivalidad, la distribución de `R` se ensancha
en la región del mínimo observado de `U_n^star`, o si la masa perdida por `R=1`
pasa esencialmente a `R=2`. `EMPTY` es una categoría separada: nunca se introduce
como `R=0` en una distribución condicionada.

La malla científica principal queda fijada en

`n = 20,22,24,26,28,30,32,34,36,38,40`.

`n=6,7,8,9` se incluye sólo como control exacto y contexto. No se ejecuta `n>40`,
no se varía `K0` y no se usa thinning.

## 2. Distribuciones y observables congelados

Para cada `n`:

- `E_n = P(M != empty)`;
- `p_n(r) = P(R=r | M != empty)`, `r>=1`;
- `U_n^star = p_n(1)`;
- `q_n(r) = P(R=r | R>=2)`, `r>=2`;
- `Sbar_n = E[ln R | M != empty]`;
- `Sbar_n_tie = E[ln R | R>=2]`;
- `H_n = -sum_r p_n(r) ln p_n(r)`;
- `H_tie_n = -sum_{r>=2} q_n(r) ln q_n(r)`.

Todos los logaritmos son naturales. `ln R` se denomina operacionalmente
«entropía residual del máximo»; no se identifica con entropía termodinámica ni
con una causa física.

Se conserva la distribución completa en formato largo. Las categorías descriptivas
predefinidas son `R=1`, `R=2`, `R=3-4` y `R>=5`; no sustituyen a `p_n(r)`.

Los cuantiles empíricos congelados son `0.50,0.75,0.90,0.95,0.99`, con definición
`inverted_cdf` (menor `r` cuya CDF empírica alcanza el nivel), tanto bajo
`M!=empty` como bajo `R>=2`.

Se verificarán, con tolerancia absoluta `1e-12`:

`p_n(1) = U_n^star`,

`p_n(r) = U_n^star delta_{r,1} + (1-U_n^star) q_n(r)` para `r>=2`, y

`H_n = h(U_n^star) + (1-U_n^star) H_tie_n`,

donde `h(u)=-u ln u-(1-u)ln(1-u)` con la convención `0 ln 0=0`.

`H_n` es diagnóstico secundario: su máximo puede ser una consecuencia mecánica
del mínimo de `U_n^star`. La información no trivial está en `q_n`,
`Sbar_n_tie`, los cuantiles y la cola.

## 3. Diseño de muestreo congelado

Los controles `n=6..9` enumeran exactamente `S_n` y deben reproducir
`p1a_tie_aut_exacto_d2.json`, incluida la distribución completa de `R`.

Para la malla principal se reproduce exactamente la campaña anterior:

```text
N_MC = 100000 por n
GENERATOR = numpy.random.Generator(PCG64)
SEED(n) = 260828000 + n
INSTANCE_TIMEOUT = 5 s
```

Las permutaciones individuales no quedaron materializadas. Se regeneran de forma
determinista y los conteos `EMPTY`, `R=1`, `R>=2` deben coincidir exactamente con
`p1a_orbital_curve_refinement_d2.csv` antes de aceptar cualquier resultado nuevo.
No hay pooling con la baseline anterior.

El backend es `evaluate_orbital_backend()` byte a byte idéntico al validado
exhaustivamente en `n=6..9`. Se usa `n_orbits_on_m`; cualquier timeout, excepción,
órbita incompleta o inconsistencia produce `BACKEND_FAILURE` y aborta sin clasificar
la instancia.

## 4. Incertidumbre congelada

Las probabilidades y categorías usan Wilson 95 %, como la campaña anterior.

Para `Sbar_n`, `Sbar_n_tie`, `H_n`, `H_tie_n` y los cuantiles se reutiliza el
bootstrap percentil iid ya empleado y probado en P1a:

```text
BOOTSTRAP_REPLICATES = 1000
BOOTSTRAP_INTERVAL = percentiles 2.5 %, 97.5 %; quantile method=linear
BOOTSTRAP_SEED_BASE = 2608275000
SEED_NONEMPTY(n) = BOOTSTRAP_SEED_BASE + 10*n + 1
SEED_TIE(n)     = BOOTSTRAP_SEED_BASE + 10*n + 2
```

El remuestreo no paramétrico se ejecuta sobre los conteos observados mediante su
forma multinomial, exactamente equivalente a remuestrear con reemplazo las
observaciones iid. Los intervalos son descriptivos, no corregidos por sesgo y no
constituyen teoría asintótica. Para los tamaños exactos se reporta el punto exacto,
sin bootstrap.

## 5. Hipótesis exploratorias

Patrón compatible con multiplicidad entrópica: además de caer `P(R=1)`, crecen
`Sbar_n`, `Sbar_n_tie`, la masa `R>=3`, la cola `R>=5`, cuantiles superiores o
`H_tie_n` alrededor de la región observada.

Patrón compatible con más empates sin ensanchamiento: la masa sale principalmente
de `R=1` hacia `R=2`, mientras `q_n`, `Sbar_n_tie`, cuantiles y cola permanecen
aproximadamente estables. No se fijan umbrales ni terminales PASS/FAIL.

## 6. Contrato de figuras fijado antes de los resultados

Se producirán tres PNG estáticos reproducibles con el estilo existente:

1. **Composición `p_n`**: barras apiladas al 100 % para `R=1`, `R=2`, `R=3-4`,
   `R>=5`, sólo `n=20..40`. Paleta multiclase de cuatro raíces y etiquetas no
   dependientes sólo del color.
2. **Entropía residual**: dos líneas con marcadores para `Sbar_n` y
   `Sbar_n_tie`, intervalos bootstrap 95 %, y línea vertical en `n=22` rotulada
   únicamente «mínimo observado de `U_n^star` en la malla».
3. **Distribución entre ties**: heatmap de CCDF condicional
   `P(R>=t | R>=2)` en los umbrales fijos `t=2,3,4,5,6,8,10,15,20`, más una
   columna explícita `R>20`. Esta regla se fija para no ocultar la cola ni elegir
   la vista después de conocer la señal.

Cada figura llevará fase, denominador, tamaño muestral y techo finito. No se usarán
ejes duales, 3D, ajustes, exponentes ni anotaciones causales.

## 7. Guardas y salidas

Guardas obligatorias: sumas de conteos, `p_n(1)=U_n^star`, `E_n U_n^star=U_n`,
`Sbar_n>=0`, `Sbar_n_tie>=ln 2` cuando hay ties, definición directa de las medias,
descomposición de Shannon, coincidencia exacta `n=6..9`, reproducción exacta de la
campaña `n=20..40` y cero fallos de backend.

Salidas nuevas, sin sobrescritura:

- CSV resumen con una fila por `n`;
- CSV largo con una fila por `(n,r)`;
- JSON de diseño, procedencia, controles y resultados;
- sidecars SHA-256;
- un script de visualización y las tres figuras anteriores;
- tests acotados del instrumento nuevo.

## 8. Prohibiciones y terminal

No se vuelve a `Xi`, `q_p`, thinning, near-maximizers, gaps, temperatura,
coarse-graining, variación de `K`, `n>40`, collapse, leyes de potencia, RG,
transiciones ni contratos anteriores. No se hace `git add`, commit, push, checkout
ni cambio de rama.

El único terminal permitido es `ORBITAL_MULTIPLICITY_PROFILE_COMPLETED` o
`ORBITAL_MULTIPLICITY_PROFILE_BLOCKED`. Tras emitirlo no se abre otro frente.
