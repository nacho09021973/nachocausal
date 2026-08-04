# P1a — El canal `G` es `sigma(m)`: exclusión exacta del gate `0.80` en la muestra sellada

> **ESTADO: PROPUESTA DE SUSTITUCIÓN DEL CIERRE DE CV-4 · RONDA 1 DE AUDITORÍA =
> `FAIL_MATERIAL`, TRES INCIDENCIAS CORREGIDAS · PENDIENTE DE RE-AUDITORÍA
> INDEPENDIENTE (RONDA 2) · EVALUACIÓN DETERMINISTA DE LECTURA SOBRE DATOS YA
> SELLADOS · SIN DATOS ESTOCÁSTICOS NUEVOS.**
>
> Sustituye a `emergencia/P1a_count_volume_cota_correlacion_d2.md` §3 en la lectura
> de `rho_max` (ver §6, retractación). No sustituye a
> `P1a_count_volume_cota_resolucion_d2.md` (CV-4.1) ni a
> `P1a_count_volume_techo_apriete_d2.md` (CV-4.3): ambos siguen siendo correctos y
> no quedan contradichos, solo dejan de estar en el camino crítico.

## 0. Resumen

`B_n` atacaba la resolución del canal a través de la descomposición en formas de
CV-3.7, que exige el peso combinatorio `w`. Esa vía era innecesaria. Dentro de un
estrato, el canal `G` está generado por **una única variable discreta `m`**, y
`COUNT_VOLUME` es una biyección creciente de `m`. La correlación máxima alcanzable
es entonces una **identidad finito-muestral exacta** sobre la muestra ya sellada.

```text
CV4_SEALED_SAMPLE_STATUS = GATE_EXCLUDED_EXACTLY
CV4_POPULATION_STATUS = STRONGLY_SUPPORTED_UNDER_IID_NOT_CLOSED_FORM_THEOREM
CV4_POPULATION_INTERVAL_CLAIMED = NO
OLD_BN_RHO_MAX_LABEL = RETRACTED_AND_RENAMED_rho_max_ub_Bn
W_STATUS = UNNECESSARY_FOR_SEALED_G_CHANNEL
```

> **Ronda de auditoría 2 (`FAIL_MATERIAL`) — dos residuos de denominación,
> corregidos.** La ronda 2 confirmó completas las correcciones de `T_xfit`, de la
> hoja de ruta y del Bloque A (regresión: ningún número cambió), pero detectó que la
> renominación no alcanzaba dos superficies auditables: la **cabecera de salida** del
> ejecutable secundario decía `rhomax_ubBn` (abreviatura por ancho de columna) y el
> **estado de control** documental decía `CV4_RHO_MAX_UPPER_BOUND_VIA_BN`. Ambas
> corregidas a la denominación exacta `rho_max_ub_Bn` / `CV4_RHO_MAX_UB_BN`. No
> materiales de la ronda 2: recuento de controles actualizado a seis (§9), y retirada
> la contradicción del techo de afirmación de
> `P1a_count_volume_cota_resolucion_d2.md` §6 (decía pendiente un valor que su propia
> §5 ya había calculado).
>
> **Ronda de auditoría 1 (`FAIL_MATERIAL`) — correcciones aplicadas.** (i) `T_xfit`
> ya no se presenta como cota superior poblacional y **se retira** el intervalo
> `[0.679,0.721]`, que no estaba demostrado: la desigualdad disponible es de
> esperanza condicional dado el predictor entrenado, no vale para una realización.
> (ii) La retractación de `0.83–0.86` se aplica ahora **de forma consistente en todo
> el repositorio**, renombrado a `rho_max_ub_Bn` también en `HOJA_DE_RUTA.md` §16,
> `P1a_count_volume_cota_resolucion_d2.md`, `P1a_count_volume_techo_apriete_d2.md` y
> en el ejecutable `p1a_count_volume_cota_correlacion_d2.py`. (iii) Se retira de
> `HOJA_DE_RUTA.md` §16 la afirmación histórica «brecha del estimador >> brecha
> techo-gate». No materiales: `SST` directo, `|rho_obs|`, influencia centrada,
> `CV4_RICHER_CHANNEL_STATUS` impreso.

## 1. Reducción del canal (tres lemas, sin datos)

**Lema 1.** Condicionado a `S`, con `n` y `side` fijos, `G = sigma(m,n,side,S) = sigma(m)`.
*Prueba.* `n` y `side` son constantes del estrato; `S` es el espacio total del modelo
condicionado, luego `sigma(S) = {vacio, Omega}`. `QED`

**Lema 2.** `COUNT_VOLUME = sqrt((m-2)/(n-2))` es estrictamente creciente en `m>2`,
luego inyectiva en el soporte de `m`, luego `sigma(COUNT_VOLUME) = sigma(m) = G`.
*Consecuencia:* la clase de estimadores `G`-medibles **es exactamente** la clase de
funciones de `COUNT_VOLUME`.

**Lema 3 (razón de correlación = correlación máxima).** Para toda `f` `G`-medible con
varianza finita, `Cov(Y,f) = Cov(E[Y|G],f)` por la torre, y por Cauchy–Schwarz

```text
corr(Y,f)^2 = Cov(Y,f)^2 / (Var(Y) Var(f)) <= Var(E[Y|G]) / Var(Y) = eta^2,
```

con igualdad en `f = E[Y|G]`. Luego `rho_max = eta`, y por varianza total
`1 - eta^2 = E[Var(Y|G)] / Var(Y)`. Esto **contiene** el contrato afín de CV-4.2
como caso particular y lo extiende a toda transformación medible, lineal o no.

### 1.1 Verificación literal de `S` (pieza de auditoría 1)

`S` es literalmente el evento de ganador único de `MIN_COVERAGE_LEX`:

- `emergencia/p1a_comparar_selectores_d2.py:346-357` — `lex_nmax == 1` (número de
  cuádruplas que alcanzan el óptimo lexicográfico) `-> STATE_UNIQUE`, en otro caso
  `STATE_TIE` con `selection = None`.
- `emergencia/p1a_representaciones_alternativas_d2.py:177-183` — `_selected_lex`
  devuelve la selección **si y solo si** `state == STATE_UNIQUE`.
- `emergencia/p1a_representaciones_alternativas_d2.py:197-231` — se emiten filas solo
  si `selected is not None`, exactamente dos por réplica seleccionada (`PAST`,
  `FUTURE`), con `interval_size` = `m` de ese lado (aserción interna
  `size != expected_size -> RuntimeError`) y `estimate_count_volume(size, n)`
  calculado del mismo `m`.

No hay condicionamiento oculto adicional. La verificación estructural
`una_fila_por_replica` pasa en los seis estratos.

## 2. Bloque A — identidad finito-muestral exacta

Sobre la distribución empírica de la muestra sellada, con bins `j` = valores
distintos de `m`:

```text
T_emp = SSW/SST,     rho_max_emp = sqrt(SSB/SST),     T_emp = 1 - rho_max_emp^2.
```

**No requiere iid, ni error estándar, ni bootstrap, ni `w`, ni ejecución nueva.**
Es la afirmación de que, *dentro de los seis estratos sellados*, ninguna
transformación de `COUNT_VOLUME` —lineal o no— alcanza `0.80`.

| `n` | lado | `N` | `K` | `SSW` | `SSB` | `SST` | `T_emp` | `>0.36` | `rho_max_emp` | `rho_obs` |
|---:|---|---:|---:|---:|---:|---:|---:|:--:|---:|---:|
| 64 | futuro | 7014 | 19 | 19.724621 | 9.392629 | 29.117250 | 0.6774 | sí | 0.5680 | 0.5664 |
| 64 | pasado | 7014 | 20 | 19.198086 | 9.146390 | 28.344476 | 0.6773 | sí | 0.5681 | 0.5660 |
| 96 | futuro | 7918 | 24 | 15.173923 | 5.973153 | 21.147076 | 0.7175 | sí | 0.5315 | 0.5300 |
| 96 | pasado | 7918 | 23 | 14.437885 | 6.066854 | 20.504739 | 0.7041 | sí | 0.5439 | 0.5420 |
| 128 | futuro | 8334 | 27 | 11.281520 | 4.846961 | 16.128481 | 0.6995 | sí | 0.5482 | 0.5458 |
| 128 | pasado | 8334 | 29 | 11.994438 | 4.806077 | 16.800515 | 0.7139 | sí | 0.5349 | 0.5322 |

`SST` se calcula **directamente** sobre las observaciones, no como `SSB+SSW`: la
descomposición ANOVA se **verifica** (`|SST-(SSB+SSW)|/SST < 1e-12`, aserción dura),
no se impone.

**Controles de identidad (los seis estratos, todos `True`):** `COUNT_VOLUME`
biyectiva y monótona en `m`; la media por bin alcanza `rho_max_emp` exactamente
(`|diff| < 1e-12`); `|rho_obs| <= rho_max_emp` (con valor absoluto, aunque todos los
`rho_obs` sean aquí positivos); una fila por réplica; `SST = SSB+SSW` verificado.

`rho_obs` reproduce a 4 decimales los `pearson_correlation` sellados en
`p1a_representaciones_resumen.json`.

## 3. Bloque B — inferencia poblacional (separada, y con menos garantías)

Requiere que las filas sean iid dentro del estrato (verificado estructuralmente: una
fila por réplica; réplicas independientes por construcción del contrato).

`T_corr` es el **estimador con corrección intrabin**
`sum_j (n_j/N) s_j^2 / (SST/(N-1))`, sobre bins con `n_j >= 2` (los singleton se
omiten, contribuyendo cero). **No es un estimador insesgado de `T`**: es un cociente
de estimadores, no un estimador del cociente. `SE_infl` es analítico por función de
influencia — determinista, sin remuestreo — y de primer orden.

| `n` | lado | `T_corr` | `SE_infl` | `T_corr − 3·SE` | holgura/`SE` | `T_xfit` | `T` solo bins ≥30 | `B_n/Var` |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 64 | futuro | 0.6789 | 0.00919 | 0.6513 | 34.7 | 0.6814 | 0.6776 | 0.2654 |
| 64 | pasado | 0.6789 | 0.00937 | 0.6508 | 34.1 | 0.6875 | 0.6757 | 0.2722 |
| 96 | futuro | 0.7192 | 0.00862 | 0.6934 | 41.7 | 0.7218 | 0.7158 | 0.2885 |
| 96 | pasado | 0.7059 | 0.00867 | 0.6799 | 39.9 | 0.7095 | 0.7012 | 0.2977 |
| 128 | futuro | 0.7017 | 0.00852 | 0.6761 | 40.1 | 0.7071 | 0.6921 | 0.3087 |
| 128 | pasado | 0.7161 | 0.00850 | 0.6906 | 41.9 | 0.7202 | 0.7109 | 0.2960 |

**`T_xfit` NO es una cota superior.** Es el error cross-fitted **realizado** de la
validación cruzada determinista par/impar. La desigualdad disponible,

```text
E_eval[ (Y - mu_hat_M)^2 | mu_hat ] = A + E[(mu_M - mu_hat_M)^2] >= A,
```

es de **esperanza condicional** dado el predictor entrenado: una realización concreta
puede quedar por encima o por debajo, y dividirla por la varianza muestral global
tampoco la convierte en cota poblacional. Su denominador usa además la muestra
completa, luego ni siquiera es una razón enteramente out-of-sample. Se reporta como
**diagnóstico de sobreajuste**, y su cercanía a `T_corr` (`+0.0025` a `+0.0086`)
indica que el ajuste de las medias por bin no está inflando `T_corr` de forma
apreciable. **No se deriva de aquí ningún intervalo poblacional.**

`SE_infl` es la función de influencia de **primer orden** del cociente plug-in,
centrada antes de tomar el segundo momento. No incorpora las correcciones `(n_j-1)`,
los bins omitidos ni el efecto de estimar las medias por bin. Los múltiplos de `SE`
son por tanto **distancias asintóticas bajo iid, no cotas exactas ni un intervalo
demostrado**.

`T` restringido a bins con `n_j >= 30` (descartando el 0.33–1.21 % de masa en bins
pequeños, suponiéndolos predichos perfectamente) no baja de `0.6757`.

**`B_n <= E[Var(Y|G)]` en los seis estratos**: CV-4.1 no queda contradicha, solo era
floja por un factor `2.27–2.56`.

## 4. Consistencia con CV-4.1 y CV-4.3

El factor `1.17–1.36` que faltaba **sí estaba disponible** — pero no apretando
`F_relax`, donde CV-4.3 probó que el techo es `1.000017`, sino no pasando por la
descomposición en formas. Toda la flojedad de `B_n` estaba en el paso
`min_{F_relax(m,n)}`, no en descartar el término entre formas.

## 5. Lo que `w` deja de ser

`w(s|m,n,side,S)` es **innecesario para la pregunta del gate en el canal sellado**.
Sigue siendo el objeto pendiente para (a) una forma cerrada poblacional en `n`, y
(b) cualquier afirmación asintótica. No está resuelto y no se aborda aquí.

## 6. Retractación

`emergencia/P1a_count_volume_cota_correlacion_d2.md` §3 afirmaba
*«la brecha real es del estimador, no de la información»*, sobre la base de
`rho_max = 0.83-0.86` frente a `rho_obs = 0.53-0.57`. **Queda retractado.**

1. Aquellos `0.83–0.86` **no eran `rho_max`**: eran una **cota superior de `rho_max`
   derivada de `B_n`**, y `B_n` era floja por un factor `2.27–2.56`. Etiqueta
   correcta: `rho_max_ub_Bn`.
2. La conclusión que se extrajo de ellos es **falsa en el sentido opuesto**: la
   ganancia de la regresión saturada sobre `m` respecto de `COUNT_VOLUME` es de
   `-0.0001` a `+0.0007` en `rho`. `COUNT_VOLUME` ya es esencialmente el estimador
   `G`-medible óptimo. **La obstrucción es de la información, no del estimador.**

Ningún número sellado resultó incorrecto; lo retractado es una lectura.

## 7. Techo de afirmación

**Demostrado exactamente:** Lemas 1–3 (poblacionales, sin datos) y el Bloque A
(identidad finito-muestral sobre la muestra sellada).

**No demostrado:**

- ninguna forma cerrada poblacional en `n`: el Bloque B es inferencia bajo iid, no
  teorema;
- nada asintótico — tres tamaños dan «no colapsa en el régimen publicado»;
- **nada sobre sigma-álgebras más ricas.** El control con `sigma(m,H,W)` (ganancia
  `+0.0011` a `+0.0077` en `rho`) descarta el rescate **solo para la familia lineal
  cross-fitted ensayada**, no para toda función medible del canal enriquecido. El
  canal `HEIGHT_WIDTH`, el poset completo y cualquier estimador order-only fuera de
  `sigma(m)` quedan fuera del alcance;
- nada fuera de `d=2`, canal `fixed-n`, selector `MIN_COVERAGE_LEX`.

## 8. Estado de control

```text
CV4_CHANNEL_REDUCTION_LEMMAS = PROVED (Seccion 1)
CV4_S_DEFINITION_VERIFIED_LITERALLY = YES (Seccion 1.1, file:line)
CV4_SEALED_SAMPLE_STATUS = GATE_EXCLUDED_EXACTLY
CV4_POPULATION_STATUS = STRONGLY_SUPPORTED_UNDER_IID_NOT_CLOSED_FORM_THEOREM
CV4_T_EMP_RANGE = 0.6773_TO_0.7175
CV4_RHO_MAX_EMP_RANGE = 0.5315_TO_0.5681
OLD_BN_RHO_MAX_LABEL = RETRACTED_AND_RENAMED_rho_max_ub_Bn
CV4_POPULATION_INTERVAL_CLAIMED = NO
CV4_OBSTRUCTION_LOCATED_IN = INFORMATION_NOT_ESTIMATOR
W_STATUS = UNNECESSARY_FOR_SEALED_G_CHANNEL
CV4_RICHER_CHANNEL_STATUS = OUT_OF_SCOPE_ONLY_LINEAR_FAMILY_TESTED
CV4_NEW_STOCHASTIC_DATA_GENERATED = NO
NOVELTY_CERTIFIED = NO
CV4_AUDIT_ROUND_1 = FAIL_MATERIAL (3 incidencias, todas corregidas)
CV4_AUDIT_ROUND_2 = FAIL_MATERIAL (2 residuos de denominacion, ambos corregidos)
CV4_AUDIT_ROUND_3 = FAIL_MATERIAL (CV-4.1 Seccion 8 reactivaba una lectura refutada)
CV4_AUDIT_STATUS = PENDING_INDEPENDENT_RE_AUDIT_ROUND_4
```

## 9. Punto único de auditoría

```text
emergencia/p1a_count_volume_canal_sigma_m_d2.py
```

Determinista, solo lectura. Ejecuta ambos bloques por separado y emite los controles.
Comando:

```text
PYTHONDONTWRITEBYTECODE=1 python3 emergencia/p1a_count_volume_canal_sigma_m_d2.py
```

La auditoría independiente debe comprobar **conjuntamente** las tres piezas:

1. **Definición literal de `S`** — §1.1, contra `p1a_comparar_selectores_d2.py:346-357`
   y `p1a_representaciones_alternativas_d2.py:177-183,197-231`.
2. **ANOVA empírico exacto** — Bloque A: `SSW`, `SSB`, `SST`, `T_emp`,
   `rho_max_emp`, `SST` calculado directamente con aserción dura del gap ANOVA, y
   los **seis** controles de identidad que emite el script (biyección, monotonía,
   media por bin alcanza `rho_max_emp`, `|rho_obs| <= rho_max_emp`, una fila por
   réplica, `SST = SSB+SSW`).
3. **Función de influencia** — Bloque B: que `SE_infl` corresponde a la función de
   influencia de **primer orden** del cociente `A/B`, centrada antes del segundo
   momento; que `T_corr` está etiquetado como estimador con corrección intrabin,
   **no** como insesgado; y que **no se deriva ningún intervalo poblacional** ni de
   `SE_infl` ni de `T_xfit`.

CV-4.4 (lema poblacional en forma cerrada) **no se aborda** hasta que esta auditoría
pase.
