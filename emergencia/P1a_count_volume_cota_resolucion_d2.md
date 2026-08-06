# P1a — Cota inferior de resolución para `COUNT_VOLUME` en `d=2` (CV-4, intento 1)

> **ESTADO: BORRADOR MATEMÁTICO v1.0 · CV-4 DE `emergencia/HOJA_DE_RUTA.md` ·
> COTA CONSERVADORA, NO EL VALOR EXACTO · DOCUMENTO PURAMENTE DEDUCTIVO · SIN
> EJECUCIÓN NUMÉRICA NUEVA.**
>
> Continúa `emergencia/P1a_count_volume_ley_condicionada_d2.md` §9. Ese documento
> dejó abierto el peso combinatorio `w(s|m,n,side,S)` como pieza pendiente para
> CV-3, CV-4 y CV-5. Este documento muestra que **CV-4 no necesita esperar a `w`**:
> se puede obtener una cota inferior válida, aunque conservadora, usando solo la
> parte geométrica ya cerrada (Beta-producto) y una restricción de soporte
> combinatoria elemental. No calcula el valor exacto de la varianza seleccionada.

## 0. Por qué esta cota no necesita `w`

`emergencia/P1a_count_volume_ley_condicionada_d2.md` §9 dio

```text
Var(ell_- | m,n,side,S)
  = E_s[ Var(ell_- | s) | m,n,side,S ] + Var_s[ E(ell_- | s) | m,n,side,S ].
```

El segundo término es no negativo, así que

```text
Var(ell_- | m,n,side,S) >= E_s[ Var(ell_- | s) | m,n,side,S ].            (*)
```

El lado derecho es un promedio ponderado de `Var(ell_-|s)` sobre la ley posterior
`w(s|m,n,side,S)` (soporte desconocido, subconjunto de las formas que de verdad
pueden ganar el argmax). Un promedio ponderado es siempre `>=` el mínimo de la
función sobre el soporte de la ponderación, y el mínimo sobre un subconjunto es
`>=` el mínimo sobre cualquier superconjunto que lo contenga. Por tanto, para
**cualquier** conjunto `F superset soporte(w(.|m,n,side,S))`,

```text
Var(ell_- | m,n,side,S) >= min_{s in F} Var(ell_- | s).                  (**)
```

Basta encontrar un superconjunto `F` computable **sin conocer `w`**. La Sección 2
construye uno usando solo la restricción de que `s` sea compatible con haber
observado ese `m` — una condición necesaria, no la condición completa de ganar el
argmax, por lo que `F` es en efecto un superconjunto válido, generalmente amplio.
La cota resultante es conservadora por construcción: puede infraestimar la
resolución real de la ley seleccionada, nunca sobreestimarla.

```text
CV4_STRATEGY = LOWER_BOUND_VIA_RELAXED_SHAPE_SUPPORT
CV4_REQUIRES_W = NO
```

## 1. Ley exacta de `Var(ell_-|s)`

Para `s=(k,l)`, `X~Beta(k,n+1-k)`, `Y~Beta(l,n+1-l)` independientes
(`P1a_count_volume_ley_condicionada_d2.md` §4), `ell_-=sqrt(X)sqrt(Y)` casi
seguramente (ambos no negativos), así:

```text
Var(ell_- | s) = E[X]E[Y] - (E[sqrt(X)] E[sqrt(Y)])^2,
E[X] = k/(n+1).
```

**Lema (momento de orden 1/2 de una Beta entera).** Para `X~Beta(a,b)`, `a,b`
enteros positivos,

```text
E[sqrt(X)] = 4^b * (2a)! * (a+b)! * (a+b-1)! / [ a! * (a-1)! * (2a+2b)! ].
```

**Demostración.** `E[X^{1/2}]=B(a+1/2,b)/B(a,b)=Gamma(a+1/2)Gamma(a+b)/[Gamma(a)Gamma(a+b+1/2)]`.
Usando `Gamma(m+1/2)=sqrt(pi)(2m)!/(4^m m!)` para `m` entero no negativo en
`Gamma(a+1/2)` y `Gamma(a+b+1/2)`, el factor `sqrt(pi)` se cancela entre numerador y
denominador porque ambos son argumentos semienteros; sustituyendo
`Gamma(a+b)=(a+b-1)!` y `Gamma(a)=(a-1)!` (enteros) da la fórmula. `QED`

**Verificación (dos casos elementales).**

```text
a=1,b=1 (Uniforme(0,1)): formula = 4*2!*2!*1!/(1!*0!*4!) = 4*2*2*1/24 = 16/24 = 2/3.
Directo: integral_0^1 sqrt(x) dx = 2/3.  Coincide.

a=2,b=1: formula = 4*4!*3!*2!/(2!*1!*6!) = 4*24*6*2/(2*1*720) = 1152/1440 = 4/5.
Directo: densidad 2x, integral_0^1 sqrt(x)*2x dx = 2*(2/5) = 4/5.  Coincide.
```

De aquí, para el hueco de la Sección anterior con `a=k,b=n+1-k` (`a+b=n+1`):

```text
E[sqrt(X_-)] = 4^{n+1-k} (2k)! (n+1)! n! / [ k! (k-1)! (2n+2-2k)! ],
```

y análogamente para `Y` con `l`.

## 2. Región de formas compatibles con un `m` observado

`m-2` debe estar en el soporte de `Hypergeometric(n-2,l-1,k-1)`
(`P1a_count_volume_ley_condicionada_d2.md` §5):

```text
max(0, k+l-n) <= m-2 <= min(k-1,l-1).
```

De la cota superior, `k>=m-1` y `l>=m-1`. Definimos

```text
F_relax(m,n) = {
  (k,l) in Z^2 : 2<=k,l<=n-1,
  k>=m-1, l>=m-1,
  k+l <= n+m-2
}.
```

`F_relax(m,n)` es un superconjunto válido del soporte real de `w(.|m,n,side,S)`:
la restricción usada (compatibilidad con `m`) es necesaria para ganar el argmax,
pero no suficiente, así que el conjunto verdadero de formas ganadoras es un
subconjunto de `F_relax(m,n)`. La cota superior `k,l<=n-1` es la más débil posible
(solo usa que los rangos caben en `1..n`); no usa que el lado opuesto de la
cuádrupla también necesita espacio, lo que hace `F_relax` deliberadamente más
amplio de lo necesario — y por tanto la cota derivada, más conservadora.

```text
CV4_FEASIBLE_SET = F_relax(m,n) = {(k,l): k,l>=m-1, k+l<=n+m-2, k,l<=n-1}
CV4_FEASIBLE_SET_IS_SUPERSET = YES (no usa la existencia del lado opuesto)
```

## 3. Teorema CV-4.1 — cota inferior computable sin `w`

**Teorema.**

```text
Var(ell_- | m,n,side,S) >= min_{(k,l) in F_relax(m,n)} [
  kl/(n+1)^2 - (E[sqrt(X_k)] * E[sqrt(Y_l)])^2
],
```

con `E[sqrt(X_k)]`, `E[sqrt(Y_l)]` dados por la fórmula de la Sección 1.

**Demostración.** Combinar (**) de la Sección 0 con la Sección 1 para la forma del
objetivo y con la Sección 2 para el conjunto de minimización. `QED`

Esta cota es exacta en su lógica (no aproximada) y conservadora en su alcance (usa
un superconjunto del soporte real). Puede ser floja; no puede ser optimista.

## 4. Ejemplo verificado a mano (`n=4,m=3`)

Caso más pequeño no trivial: `m=3` requiere `k,l>=2`. Con `n=4`:
`k+l<=n+m-2=5`, `k,l<=3`. Candidatos: `(2,2)`, `(2,3)`, `(3,2)` (`(3,3)` excluido,
suma `6>5`). Por simetría del objetivo en `(k,l)<->(l,k)`, basta `(2,2)` y `(2,3)`.

**Caso `(2,2)`.** `X,Y~Beta(2,3)` iid. `E[X]=E[Y]=2/5=0.4`.
`E[sqrt(X)]`: verificación directa, densidad `12x(1-x)^2`,
`integral_0^1 x^{1/2}*12x(1-x)^2 dx = 12(2/5-4/7+2/9) = 12*(0.4-0.571429+0.222222)
= 12*0.050794 = 0.609524 = 64/105`.

```text
Var(ell_-|(2,2)) = 0.4*0.4 - (64/105 * 64/105)^2
                 = 0.16 - (0.609524^2)^2
                 = 0.16 - 0.371519^2
                 = 0.16 - 0.138026
                 = 0.021974.
```

**Caso `(2,3)`.** `X~Beta(2,3)` (como arriba, `E[X]=0.4`, `E[sqrt(X)]=64/105
=0.609524`). `Y~Beta(3,2)`, densidad `12y^2(1-y)`, `E[Y]=3/5=0.6`,
`E[sqrt(Y)] = integral_0^1 y^{1/2}*12y^2(1-y) dy = 12(2/7-2/9) = 12*(4/63)
= 48/63 = 16/21 = 0.761905`.

```text
Var(ell_-|(2,3)) = E[X]E[Y] - (E[sqrt(X)]*E[sqrt(Y)])^2
                 = (2/5)(3/5) - (64/105 * 16/21)^2
                 = 6/25 - (1024/2205)^2
                 = 0.24 - 0.464399^2
                 = 0.24 - 0.215666
                 = 0.024334.
```

```text
min( Var(ell_-|(2,2)), Var(ell_-|(2,3)), Var(ell_-|(3,2)) )
  = min(0.021974, 0.024334, 0.024334) = 0.021974.
```

```text
Var(ell_- | m=3,n=4,side,S) >= 0.0220  (desviacion tipica >= 0.148).
```

`n=4` es un caso de juguete muy por debajo del régimen publicado (`n=64,96,128`),
no comparable a los números de
`P1a_resultados_representaciones_alternativas_d2.md`. Su único papel es demostrar
que la maquinaria produce una cota bien definida, positiva y no vacía, calculada y
verificada enteramente a mano.

## 5. Evaluación numérica en el régimen publicado

Se evaluó `min_{(k,l) in F_relax(m,n)} Var(ell_-|(k,l))` (Sección 3) para cada valor
de `m` (columna `interval_size`) observado en la muestra ya sellada de
`P1a_resultados_representaciones_alternativas_d2.md`, y se comparó, fila a fila,
contra el error cuadrático observado del estimador `COUNT_VOLUME` ya publicado
(`signed_error_count_volume`). Es una evaluación **determinista** de la fórmula
cerrada de la Sección 1 sobre un conjunto finito de enteros —no una simulación
estocástica, no genera datos nuevos, solo lee el CSV ya sellado y evalúa una
fórmula ya demostrada—, ejecutada con:

```text
PYTHONDONTWRITEBYTECODE=1 python3 emergencia/p1a_count_volume_cota_resolucion_evaluacion_d2.py
```

Control interno: la evaluación reproduce el ejemplo a mano de la Sección 4
(`n=4,m=3` da `0.021973`, frente a `0.021974` calculado a mano; diferencia por
redondeo de coma flotante en la evaluación de `Gamma` vía `lgamma`, no un error).

| `n` | lado | `m` medio | cota media `E_m[bound]` | MSE observado `COUNT_VOLUME` | cota/MSE |
|---:|---|---:|---:|---:|---:|
| 64 | pasado | 12.64 | 0.001100 | 0.003844 | 0.286 |
| 64 | futuro | 12.67 | 0.001102 | 0.003941 | 0.280 |
| 96 | pasado | 19.18 | 0.000771 | 0.002480 | 0.311 |
| 96 | futuro | 19.17 | 0.000771 | 0.002548 | 0.302 |
| 128 | pasado | 25.96 | 0.000597 | 0.001866 | 0.320 |
| 128 | futuro | 26.00 | 0.000598 | 0.001793 | 0.333 |

`bound_avg` es el promedio muestral de `bound(m_i,n)` sobre las mismas filas
(mismo `m` que realmente ocurrió en cada intervalo seleccionado), no un valor en un
único `m` representativo. `mse_observed` es `mean(signed_error_count_volume^2)`
sobre las mismas filas.

**Lectura.** La cota, siendo conservadora (soporte relajado, sin `w`, sin la
restricción del lado opuesto), ya **cubre al menos entre el `28%` y el `33%` de la
escala del error cuadrático observado**, de forma consistente en los tres tamaños y
ambos lados, y la fracción crece ligeramente con `n` en vez de colapsar.

`B_n/MSE_obs` **no** es una descomposición del error: `B_n` es una cota inferior
sobre el MSE alcanzable por cualquier estimador medible respecto de `(m,n,side,S)`,
y el `67%-72%` restante no es un residuo atribuible a otra causa identificada.
Podría cerrarse apretando `F_relax` (ítem 2 abajo), o podría reflejar que
`E_s[Var(ell|s)|m,n,side,S]` real, con el `w` verdadero, es bastante mayor que el
mínimo relajado usado aquí.

Lo que la cota respalda es la **obstrucción a la identificación por instancia**: hay
un suelo de error individual no nulo dado solo `m,n,side,S`. No respalda por sí sola
la «calibrabilidad en promedio» — eso requiere además la evidencia de calibración de
Fase 6 (sesgo y error relativo mediano ya sellados), que es un resultado distinto y
no se deduce de CV-4.

> **Actualizado por `emergencia/P1a_count_volume_cota_correlacion_d2.md`** (ítem 1
> de abajo, ya ejecutado): contra el MSE del mejor recalibrado afín la cota cubre
> `0.39–0.44`, y la **cota superior** que induce es
> `rho_max_ub_Bn = 0.83–0.86` — **no** es la correlación máxima real. Con esa cota
> el gate `0.80` no queda excluido; faltaría un factor `1.17–1.36` sobre `B_n`.
>
> **Superado por `emergencia/P1a_count_volume_canal_sigma_m_d2.md`:** el `rho_max`
> real del canal es `0.532–0.568` y el gate `0.80` **sí** queda excluido
> exactamente sobre la muestra sellada. `B_n` resultó floja por un factor
> `2.27–2.56`; sigue siendo una cota inferior válida (`B_n <= E[Var(Y|G)]` en los
> seis estratos), solo que no en el camino crítico.

**Estado de estos ítems tras los resultados posteriores:**

1. La traducción a correlación quedó completada en
   `P1a_count_volume_cota_correlacion_d2.md`.
2. El apriete de `F_relax` quedó `DONE_AND_CLOSED`: `P1a_count_volume_techo_apriete_d2.md`
   y `HOJA_DE_RUTA.md` §17 muestran que las cotas superiores no aportan el factor
   requerido.
3. `w(s|m,n,side,S)` sigue sin resolverse, pero el cálculo directo de
   `P1a_count_volume_canal_sigma_m_d2.md` demuestra que es innecesario para el gate
   empírico del canal sellado `G=sigma(m)`.

```text
CV4_NUMERIC_EVALUATION_FOR_PUBLISHED_REGIME = DONE
CV4_BOUND_COVERS_FRACTION_OF_OBSERVED_MSE_SCALE = 0.28_TO_0.33
CV4_METRIC_TRANSLATION = DONE (P1a_count_volume_cota_correlacion_d2.md)
CV4_TIGHTER_FEASIBLE_SET = DONE_AND_CLOSED (HOJA_DE_RUTA.md Seccion 17)
```

## 6. Techo de afirmación

Este documento demuestra una cota inferior *conservadora* y la ilustra en un caso
de juguete verificado a mano. No establece:

- ~~el valor de la cota para `n=64,96,128` (pendiente, requiere ejecución)~~
  **obsoleto:** ya calculado en §5 (`CV4_PUBLISHED_REGIME_NUMBER = COMPUTED`);
- si esa cota **explica** la resolución observada de `COUNT_VOLUME` — no la explica:
  `B_n/MSE_obs` no es una descomposición del error (§5), y el cálculo directo del
  canal (`P1a_count_volume_canal_sigma_m_d2.md`) mostró que `B_n` era floja por un
  factor `2.27–2.56`;
- ninguna afirmación sobre `HEIGHT_ONLY` o cualquier híbrido cadena+volumen (ver
  `emergencia/HOJA_DE_RUTA.md` §7, rama `S5`, añadida junto con este documento);
- autorización para ejecutar código nuevo.

## 7. Estado de control

```text
CV4_BOUND_THEOREM = PROVED (Seccion 3)
CV4_BOUND_TYPE = CONSERVATIVE_LOWER_BOUND_NOT_EXACT_VALUE
CV4_REQUIRES_COMBINATORIAL_WEIGHT_W = NO
CV4_TOY_EXAMPLE = VERIFIED_BY_HAND (n=4, m=3, bound=0.0220)
CV4_PUBLISHED_REGIME_NUMBER = COMPUTED (Seccion 5)
CV4_BOUND_COVERS_FRACTION_OF_OBSERVED_MSE_SCALE = 0.28_TO_0.33
CV4_GATE_0.80_STRUCTURALLY_EXCLUDED_BY_BOUND = NO (ver documento de correlacion)
CV4_NUMERICAL_EXECUTION_AUTHORIZED = YES_READ_ONLY_DETERMINISTIC_ON_SEALED_DATA
CV4_NEW_STOCHASTIC_DATA_GENERATED = NO
NOVELTY_CERTIFIED = NO
CV4_STATUS = PARTIAL_STRUCTURAL_BOUND_EVALUATED_ON_PUBLISHED_REGIME
```

## 8. Estado posterior — acciones obsoletas retiradas

La antigua «próxima acción» de traducir la cota y apretar `F_relax` queda obsoleta:
ambos pasos se completaron y la segunda vía quedó `DONE_AND_CLOSED`
(`emergencia/HOJA_DE_RUTA.md` §§16–17). El cálculo directo posterior del canal
`G=sigma(m)` (`P1a_count_volume_canal_sigma_m_d2.md`) fija la lectura vigente.

El `67%-72%` es la fracción residual del canal sellado basado en `m`, no «MSE
inexplicado» en sentido general. Dentro de ese mismo canal no queda abierta una
alternativa entre límite informacional y margen del estimador: la media condicionada
por bin alcanza el óptimo empírico. Esto no excluye mejoras mediante un canal
enriquecido; cualquier rescate no lineal fuera de `sigma(m)` permanece fuera de
alcance.

## 9. Artefactos

```text
emergencia/p1a_count_volume_cota_resolucion_evaluacion_d2.py
```

Script determinista de verificación: reproduce el ejemplo a mano de la Sección 4 y
evalúa la cota sobre `emergencia/resultados/p1a_representaciones_intervalos_d2.csv`
(datos ya sellados de Fase 6, leídos sin modificar). No genera aleatoriedad nueva,
no escribe artefactos nuevos en `resultados/`, no requiere sidecars `sha256`: es una
evaluación de una fórmula ya demostrada sobre datos ya publicados, no un experimento
nuevo.
