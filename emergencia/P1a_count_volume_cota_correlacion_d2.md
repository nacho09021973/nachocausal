# P1a — Traducción de la cota CV-4 a techo de correlación (`d=2`)

> **ESTADO: BORRADOR v1.0 · CV-4 ÍTEM 1 DE
> `emergencia/P1a_count_volume_cota_resolucion_d2.md` §5 · EVALUACIÓN DETERMINISTA
> DE LECTURA SOBRE DATOS YA SELLADOS · SIN DATOS ESTOCÁSTICOS NUEVOS.**
>
> Ejecuta el ítem 1 pendiente de `P1a_count_volume_cota_resolucion_d2.md` §5:
> pasar de escala de MSE a la métrica que el contrato realmente puertea
> (`bootstrap95_lower(correlación Pearson) >= 0.80`,
> `P1a_contrato_representaciones_alternativas_d2.md` §5). El ítem 2 (apretar
> `F_relax`) y el ítem 3 (`w`) siguen abiertos y **no** se abordan aquí.

## 0. Qué corrige este documento respecto de la lectura anterior

`P1a_count_volume_cota_resolucion_d2.md` §5 reportó `cota/MSE_obs = 0.28–0.33` y lo
describió como que la cota «explica» esa fracción del error. Dos precisiones:

1. `B_n/MSE_obs` **no es una descomposición del error**. `B_n` es una cota inferior
   sobre el MSE alcanzable por cualquier estimador medible respecto de
   `(m,n,side,S)`; el resto no es un residuo atribuido a otra causa. La formulación
   correcta es que la cota **cubre al menos el 28–33 % de la escala del MSE
   observado**.
2. `B_n/MSE_obs` por sí sola no dice nada sobre el gate. El gate es de correlación,
   y la razón que falta para conectarlos es `MSE_obs/Var(Y_n)` (§2, tabla).

```text
CV4_CORR_SUPERSEDES_FRAMING = "cubre la escala de", NO "explica"
```

## 1. Teorema CV-4.2 — techo de correlación implicado por la cota

Sea `Y` el objetivo (`latent_duration`), `G = sigma(m,n,side,S)` la información
observable, y `f` cualquier estimador `G`-medible (en particular
`COUNT_VOLUME = sqrt((m-2)/(n-2))`, que es `sigma(m,n)`-medible y por tanto
`G`-medible).

**Teorema.**

```text
rho(Y,f)^2 <= 1 - B_n / Var(Y),
es decir   rho_max_ub_Bn(n) := sqrt(1 - B_n/Var(Y_n))   es una COTA SUPERIOR de
rho_max, no rho_max.   [rho_max <= rho_max_ub_Bn; la desigualdad es estricta aqui]
```

> **Nota de nomenclatura (obligatoria).** `rho_max_ub_Bn` es una **cota superior**
> de la correlación máxima, no la correlación máxima. `B_n` es una cota inferior de
> `E[Var(Y|G)]`, luego el techo que induce es flojo por construcción. El `rho_max`
> real del canal se calcula en `emergencia/P1a_count_volume_canal_sigma_m_d2.md` y
> vale `0.532–0.568`. En este documento **nunca** debe leerse `rho_max_ub_Bn` como
> correlación máxima real.

**Demostración.** El mejor recalibrado afín de `f` tiene error cuadrático

```text
min_{a,b} E[(Y - a - b f)^2] = Var(Y) (1 - rho(Y,f)^2).
```

`a + b f` es `G`-medible, y la esperanza condicional `E[Y|G]` es la proyección `L2`
sobre las funciones `G`-medibles, luego

```text
Var(Y)(1 - rho^2) >= E[(Y - E[Y|G])^2] = E[Var(Y|G)].
```

Por el Teorema CV-4.1 (`P1a_count_volume_cota_resolucion_d2.md` §3) aplicado fila a
fila y promediado, `E[Var(Y|G)] >= B_n`. Combinando y despejando `rho^2`. `QED`

**Corolarios inmediatos** (mismo `B_n`, misma hipótesis):

```text
NRMSE_sigma,min = sqrt(B_n/Var(Y_n))     (error mínimo normalizado por sigma(Y))

gate rho>=0.80 estructuralmente excluido  <=>  B_n/Var(Y_n) > 1 - 0.80^2 = 0.36

k_necesario = 0.36 * Var(Y_n) / B_n      (factor por el que habria que multiplicar
                                          B_n para excluir el gate)
```

**Invariancia bajo calibración afín (lo que pedía la revisión).** El teorema se
demuestra minimizando *sobre todos* los `(a,b)`, así que `B_n` sigue siendo cota
inferior después de cualquier recalibración afín de `COUNT_VOLUME`. La condición es
que la calibración sea función de la información observable — lo es: `a` y `b`
constantes por estrato `(n,side)`. Una «calibración» que usara la verdad oculta no
sería `G`-medible y quedaría fuera del teorema; ninguna de las usadas aquí lo es.

## 2. Evaluación en el régimen publicado

Determinista, sobre el mismo CSV sellado de Fase 6, con la misma estratificación
`(n,side)` que usa el contrato para la correlación:

```text
PYTHONDONTWRITEBYTECODE=1 python3 emergencia/p1a_count_volume_cota_correlacion_d2.py
```

`Var(Y_n)` es la varianza muestral (`ddof=1`) de `latent_duration` en el estrato.
`MSE_afin = Var(Y_n)(1-rho_obs^2)` es el MSE del mejor recalibrado afín de
`COUNT_VOLUME`.

| `n` | lado | `Var(Y)` | `B_n` | `B_n/Var` | `MSE_obs/Var` | `B_n/MSE_afin` | `rho_max_ub_Bn` | `rho_obs` | `NRMSE_min` | `k_necesario` |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 64 | futuro | 0.004152 | 0.001102 | 0.2654 | 0.9491 | 0.3908 | 0.8571 | 0.5664 | 0.5152 | 1.36 |
| 64 | pasado | 0.004042 | 0.001100 | 0.2722 | 0.9510 | 0.4005 | 0.8531 | 0.5660 | 0.5217 | 1.32 |
| 96 | futuro | 0.002671 | 0.000771 | 0.2885 | 0.9539 | 0.4012 | 0.8435 | 0.5300 | 0.5372 | 1.25 |
| 96 | pasado | 0.002590 | 0.000771 | 0.2977 | 0.9574 | 0.4216 | 0.8380 | 0.5420 | 0.5457 | 1.21 |
| 128 | futuro | 0.001935 | 0.000598 | 0.3087 | 0.9261 | 0.4398 | 0.8314 | 0.5458 | 0.5556 | 1.17 |
| 128 | pasado | 0.002016 | 0.000597 | 0.2960 | 0.9255 | 0.4130 | 0.8390 | 0.5322 | 0.5441 | 1.22 |

`rho_obs` reproduce, con el mismo estimador Pearson y las mismas filas, los valores
ya sellados en `p1a_representaciones_resumen.json`
(`pearson_correlation`: `0.5664 / 0.5660 / 0.5300 / 0.5420 / 0.5458 / 0.5322`).
Coincidencia exacta a 4 decimales en los seis estratos: control de que la traducción
lee la misma población que puertea el contrato.

**Controles internos (falsables, los seis estratos pasan):**

```text
B_n <= MSE_afin        (la cota sobrevive a la calibracion afin: lo pedido)
rho_obs <= rho_max_ub_Bn  (si fallara, el Teorema CV-4.2 o la cota serian falsos)
MSE_afin <= MSE_obs    (identidad de minimizacion; control de aritmetica)
```

El segundo control es la comprobación empírica no trivial: una cota errónea por
exceso habría producido un `rho_max_ub_Bn` por debajo de la correlación ya publicada, y
esto lo habría detectado.

## 3. Lectura

> **RETRACTADA EN PARTE — ver `emergencia/P1a_count_volume_canal_sigma_m_d2.md` §6.**
> Los valores `0.83–0.86` de esta sección **no son `rho_max`**: son una **cota
> superior de `rho_max` derivada de `B_n`** (etiqueta correcta:
> `rho_max_ub_Bn`), y `B_n` resultó floja por un factor `2.27–2.56`.
> El `rho_max` real del canal es `0.532–0.568`, y el gate `0.80` **sí** queda
> excluido exactamente sobre la muestra sellada. En consecuencia, la afirmación de
> más abajo de que «la brecha real es del estimador, no de la información» es
> **falsa en el sentido opuesto**: `COUNT_VOLUME` ya es esencialmente el estimador
> `G`-medible óptimo. Lo retractado es una lectura; ningún número sellado resultó
> incorrecto. Las Secciones 1, 2, 4 y 5 de este documento siguen siendo válidas
> como lo que son: una cota superior conservadora.

**El gate `0.80` NO queda estructuralmente excluido *por esta cota*.** `B_n/Var(Y_n)`
vale `0.27–0.31`, por debajo del umbral `0.36` que haría imposible `rho>=0.80`. La
cota superior implicada es `rho_max_ub_Bn = 0.83–0.86`: con la
información `(m,n,side,S)` y **esta cota**, no se puede descartar que un estimador
ideal alcance el gate. (Con el cálculo directo del canal sí se descarta: §6 de
`P1a_count_volume_canal_sigma_m_d2.md`.)

**Cuánto falta:** `k_necesario = 1.17–1.36`. Basta apretar la cota por un factor
entre `1.2` y `1.4` para que la exclusión estructural del gate quede demostrada.
Esto es lo que convierte al ítem 2 (`F_relax` más apretado, sin necesitar `w`) en
la siguiente acción racional: el objetivo ya no es cualitativo sino un factor
numérico modesto y explícito. El ítem 3 (`w`) no es necesario para intentarlo.

**~~La brecha real es del estimador, no de la información.~~ RETRACTADO.** Se
argumentaba que `rho_obs = 0.53–0.57` frente a un supuesto «techo» de `0.83–0.86`
dejaba mucho margen al estimador. Falso: `0.83–0.86` es `rho_max_ub_Bn`, una cota
superior floja y nunca el máximo real; el `rho_max`
real es `0.532–0.568`. La ganancia de la regresión saturada sobre `m` respecto de
`COUNT_VOLUME` es de `-0.0001` a `+0.0007` en `rho`. **La obstrucción es de la
información, no del estimador.**

**Corrección de escala.** `MSE_obs/Var(Y_n) = 0.93–0.96`: el MSE crudo de
`COUNT_VOLUME` es casi la varianza del objetivo, porque arrastra sesgo (`+0.018` a
`+0.032`) y escala. Contra el MSE del mejor recalibrado afín, la cota cubre
`0.39–0.44`, no `0.28–0.33`. La fracción cubierta crece con `n` en ambas escalas.

**Sobre «calibrable en promedio, no identificable por instancia».** Lo que estos
números respaldan es únicamente la mitad de obstrucción por instancia, y solo
parcialmente: hay un suelo de error por instancia no nulo y no colapsante
(`NRMSE_sigma,min = 0.52–0.56`, es decir, ningún estimador sobre `(m,n,side,S)`
baja de ~`0.52 sigma(Y)` de error típico). La «calibrabilidad en promedio» no se
deduce de CV-4: requiere la evidencia de calibración de Fase 6
(`bias_bootstrap95` y `median_are` ya sellados), que es un resultado distinto.

## 4. Techo de afirmación

No se establece:

- que `(m,n,side,S)` sea insuficiente para `rho>=0.80` (esta cota **no** lo excluye);
- ninguna tendencia asintótica: tres tamaños permiten afirmar «no colapsa en el
  régimen publicado», no una ley en `n`;
- nada sobre `HEIGHT_ONLY`, `HEIGHT_WIDTH` ni híbridos (rama `S5`);
- ninguna reapertura del gate ni de la decisión congelada del contrato §5.

## 5. Estado de control

```text
CV4_METRIC_TRANSLATION = DONE (correlacion; error relativo mediano sigue pendiente)
CV4_THEOREM_CORRELATION_CEILING = PROVED (Seccion 1)
CV4_BOUND_SURVIVES_AFFINE_CALIBRATION = YES (probado y verificado en los 6 estratos)
CV4_RHO_MAX_UB_BN = 0.831_TO_0.857   # COTA SUPERIOR via B_n; NO es rho_max
CV4_RHO_MAX_TRUE_SEALED_CHANNEL = 0.5315_TO_0.5681 (P1a_count_volume_canal_sigma_m_d2.md)
CV4_GATE_0.80_STRUCTURALLY_EXCLUDED_BY_BOUND = NO
CV4_GATE_0.80_EXCLUDED_BY_DIRECT_CHANNEL = YES_ON_SEALED_SAMPLE
CV4_SECTION3_READING = RETRACTED (ver P1a_count_volume_canal_sigma_m_d2.md Seccion 6)
CV4_K_NEEDED_TO_EXCLUDE_GATE = 1.17_TO_1.36
CV4_NRMSE_SIGMA_MIN = 0.515_TO_0.556
CV4_BOUND_COVERS_FRACTION_OF_AFFINE_CALIBRATED_MSE = 0.39_TO_0.44
CV4_TIGHTER_FEASIBLE_SET = DONE_AND_CLOSED (HOJA_DE_RUTA.md Seccion 17)
CV4_W_RESOLVED = NO
CV4_NEW_STOCHASTIC_DATA_GENERATED = NO
NOVELTY_CERTIFIED = NO
```

## 6. Resultado posterior — vía cerrada

La acción de apretar `F_relax(m,n)` ya no está pendiente. El resultado posterior
registrado canónicamente en `emergencia/HOJA_DE_RUTA.md` §17 es:

```text
CV4_TIGHTER_FEASIBLE_SET = DONE_AND_CLOSED
CV4_ITEM2_VERDICT = ABANDON_ROUTE_WITHOUT_RESOLVING_W
```

El techo de cualquier apriete mediante cotas superiores es `1.000017`, por debajo
del factor mínimo `1.17` requerido. El cálculo directo posterior de
`P1a_count_volume_canal_sigma_m_d2.md` excluye el gate exactamente en la muestra
sellada sin resolver `w`; no se deriva de esta sección ninguna acción pendiente.

## 7. Artefactos

```text
emergencia/p1a_count_volume_cota_correlacion_d2.py
```

Determinista, solo lectura. Reutiliza `bound_for_m` del script ya auditado
`emergencia/p1a_count_volume_cota_resolucion_evaluacion_d2.py` (no redefine la
fórmula demostrada). No escribe en `resultados/`, no genera aleatoriedad, no
requiere sidecar `sha256`.
