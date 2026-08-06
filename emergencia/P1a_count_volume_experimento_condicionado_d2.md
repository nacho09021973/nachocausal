# P1a — Experimento condicionado por selección para `COUNT_VOLUME` en `d=2`

> **ESTADO: CONTRATO MATEMÁTICO v1.0 · CV-1 + CV-2 DE
> `emergencia/HOJA_DE_RUTA.md` · DOCUMENTO PURAMENTE DEDUCTIVO · SIN
> EJECUCIÓN NUMÉRICA NUEVA AUTORIZADA.**
>
> Este documento congela el experimento estadístico seleccionado para la rama
> `COUNT_VOLUME` (CV-1), deriva el baseline binomial sin selección (CV-2) y traza el
> mapa de dependencias que `MIN_COVERAGE_LEX` introduce sobre ese baseline. No
> calcula la ley condicionada por selección (CV-3), no acota resolución (CV-4) y no
> audita circularidad (CV-5): esas tres piezas quedan explícitamente abiertas y
> ordenadas para el trabajo siguiente. No autoriza ninguna simulación nueva.

## 0. Lugar en la hoja de ruta

Continúa `emergencia/HOJA_DE_RUTA.md`, §5 (CV-1 a CV-5) y es el
`NEXT_DELIVERABLE` fijado en su §11. Da por congelados sin reabrirlos:

```text
selector      = MIN_COVERAGE_LEX  (emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md)
representacion = COUNT_VOLUME     (emergencia/P1a_contrato_representaciones_alternativas_d2.md)
canal          = fixed-n, d=2
```

`COUNT_VOLUME` quedó `OPEN_BELOW_QUALIFICATION_THRESHOLD`: correlación individual
`0.51`–`0.57`, muy por debajo de `0.80`, con sesgo positivo pequeño y sin teoría
condicionada por selección. Este documento abre esa teoría; no repite ni reinterpreta
los números ya publicados en
`emergencia/P1a_resultados_representaciones_alternativas_d2.md`.

## 1. Definición exacta del experimento seleccionado (CV-1)

### 1.1 Ley generativa

Sin cambios respecto de los contratos anteriores:

```text
(u_i,v_i) iid Uniform([0,1]^2), i=1,...,n,
x_i prec x_j iff u_i<u_j y v_i<v_j,
condicionado a N=n.
```

El poset resultante `C` es equivalente a una permutación uniforme `pi` de `{1,...,n}`
(Fase 2, `P1a_puerta_teorica_en_Minkowski.md`): ordenando los puntos por `u`, el
`i`-ésimo punto en ese orden tiene rango `v` igual a `pi(i)`.

### 1.2 Selector y evento de selección `S`

```text
Q_3(C) = {(a,b,c,d) in V^4 : a prec_C b prec_C c prec_C d,
          m_-(q)=n_C(a,b)>=3, m_+(q)=n_C(c,d)>=3},

S_lex(q) = (min(m_-(q),m_+(q)), m_-(q)+m_+(q)), orden lexicografico,

MIN_COVERAGE_LEX(C) =
  q* = argmax_{q in Q_3(C)} S_lex(q),  si el argmax es unico;
  UNDEFINED,                            si Q_3(C)=vacio o hay empate.
```

```text
S = { MIN_COVERAGE_LEX(C) esta definido } = { el argmax de S_lex es unico }.
```

`S` es un evento sobre la realización completa del poset (los `n` puntos), no sobre
un único par candidato: depende de todo `Q_3(C)`, no solo de `q*`.

### 1.3 Observación por intervalo

Cuando `S` ocurre, `q*=(a,b,c,d)` determina dos intervalos observados,
`J_-=[a,b]` (pasado) y `J_+=[c,d]` (futuro). Congelamos, como en el resto de P1a, la
observación **por intervalo**, no la cuádrupla conjunta:

```text
observacion(J) = (m, n, side, S),
  m    = n_C(a,b) o n_C(c,d) segun el lado,
  n    = N(C),
  side in {PAST, FUTURE},
  S    = evento de seleccion unica (implicito: solo se observa si S ocurre).
```

Esta es una elección deliberada de la hoja de ruta (§5, CV-1), no una necesidad
matemática: la cuádrupla completa también fija `m` del otro lado, que la observación
marginal descarta. La §5 de este documento lo registra como cantidad Q4/Q5 a derivar
antes de CV-3, precisamente porque la ley conjunta `(m_-,m_+)` puede llevar
información que la marginal por lado pierde.

### 1.4 Target latente

Para el intervalo `[x,y]` con coordenadas latentes `(u_x,v_x),(u_y,v_y)`:

```text
A(x,y) = (u_y-u_x)(v_y-v_x),
ell(x,y) = sqrt(A(x,y)),
```

con la convención nula ya fijada, `ds^2=du dv`. El target es `ell` del intervalo
observado; la coordenada solo se consulta después de seleccionar (§2 de
`P1a_contrato_gate_altura_duracion_lex_d2.md`).

### 1.5 Estimando congelado

Se fija como estimando primario, para cada `(m,n,side)` con `S` implícito:

```text
L(ell | m,n,side,S) = ley condicional completa,
resumida por:
  mu(m,n,side)    = E[ell | m,n,side,S],
  sigma2(m,n,side) = Var[ell | m,n,side,S].
```

De `L` se derivan, sin ajuste independiente:

- **estimador puntual**: media o mediana de `L` (la elección entre ambas se fija en
  CV-3 según cuál sea tratable, no se ajustan las dos y se elige la que mejor
  correlacione a posteriori);
- **intervalo de predicción**: cuantiles de `L`;
- **cota de resolución** (CV-4): `sigma2(m,n,side)` y su generalización a riesgo
  minimax.

Quedan **explícitamente fuera** de este estimando, y no se calculan en este
documento ni se autorizan en el siguiente:

- ranking individual entre intervalos de una misma muestra;
- `ell_hat_minus/ell_hat_plus` o cualquier razón entre lados (permanece
  `RATIO_STATUS = CLOSED`, `emergencia/HOJA_DE_RUTA.md` §6);
- calibración ensemble-level fuera del canal `fixed-n`.

```text
CV1_ESTIMAND = CONDITIONAL_LAW_L(ell|m,n,side,S)_VIA_MEAN_AND_VARIANCE
CV1_POINT_RANKING_RATIO_MIXING = FORBIDDEN
```

## 2. Baseline binomial sin selección (CV-2)

### 2.1 Enunciado

**Proposición CV-2.1 (recuento binomial a área fija).** Sean `x,y` dos puntos con
coordenadas fijas `u_x<u_y`, `v_x<v_y`, y sean `z_1,...,z_k` iid `Uniform([0,1]^2)`,
independientes entre sí y de `(x,y)`. Sea

```text
M = #{ i : u_x<u_{z_i}<u_y, v_x<v_{z_i}<v_y }.
```

Entonces `M ~ Binomial(k,A)`, con `A=(u_y-u_x)(v_y-v_x)`.

**Demostración.** Cada `z_i` cae en el rectángulo `(u_x,u_y) x (v_x,v_y)` con
probabilidad exactamente su área `A`, por uniformidad marginal en `[0,1]^2`. Los
eventos son independientes porque los `z_i` lo son. `M` es la suma de `k` variables
Bernoulli `(A)` iid. `QED`

### 2.2 Corolario para el canal `N=n`

**Corolario CV-2.2.** Sea `C` generado como en §1.1 con `N=n`, y sean `a,b` dos de
los `n` puntos. Condicionado a `sigma(u_a,v_a,u_b,v_b)` — es decir, a los valores
exactos de las coordenadas de `a` y `b`, sin condicionar además sobre los `n-2`
puntos restantes ni sobre ningún evento que dependa de ellos —, los `n-2` puntos
restantes siguen siendo iid `Uniform([0,1]^2)` e independientes de `(a,b)`. Aplicando
CV-2.1 con `k=n-2`:

```text
m-2 | A ~ Binomial(n-2,A),   m = n_C(a,b) = |[a,b]_C|,   A=ell(a,b)^2.
```

**Demostración.** El muestreo es iid, luego la ley conjunta de los `n` puntos
factoriza. Condicionar sobre las coordenadas de dos de ellos no cambia la ley
marginal de los `n-2` restantes ni introduce dependencia entre ambos grupos: es la
propiedad de independencia de coordenadas iid, no un resultado nuevo. `M=m-2` es
entonces el recuento de CV-2.1 con `k=n-2`. `QED`

### 2.3 Consecuencias inmediatas

```text
E[m-2 | A] = (n-2)A,
Var[m-2 | A] = (n-2)A(1-A),
E[A_hat_count | A] = A,      A_hat_count = (m-2)/(n-2),
Var[A_hat_count | A] = A(1-A)/(n-2).
```

`A_hat_count` es insesgado para `A` **bajo esta condición exacta**: coordenadas de
`a,b` fijas (o condicionadas), y ningún otro evento adicional. Esto reproduce la nota
ya registrada en `P1a_contrato_representaciones_alternativas_d2.md` §1 R1, ahora con
demostración explícita y con la hipótesis exacta bajo la que vale.

### 2.4 Qué NO cubre el baseline

CV-2.2 exige condicionar **únicamente** sobre `sigma(u_a,v_a,u_b,v_b)` (equivalente a
condicionar sobre `A`). No cubre condicionar sobre:

- que `(a,b)` sea un par comparable elegido dentro de `Q_3(C)` (ya es una restricción
  sobre el propio `m`, no solo sobre `A`);
- que `(a,b,c,d)` sea el maximizador de `S_lex` sobre todo `Q_3(C)` (evento `S`, que
  depende de los `n-2` puntos restantes a través de `m` mismo, y de la existencia y
  score de todos los demás candidatos).

Cualquiera de estas dos condiciones rompe la hipótesis de CV-2.2, porque deja de ser
una condición medible respecto de `sigma(u_a,v_a,u_b,v_b)` solamente. El baseline es
por tanto un punto de referencia algebraico, no la ley del experimento seleccionado.
Cuantificar exactamente esa ruptura es el contenido de CV-3.

```text
CV2_BASELINE_LAW = m-2 | A ~ Binomial(n-2,A)
CV2_BASELINE_STATUS = DERIVED_CLOSED_FORM_NO_EXECUTION_NEEDED
CV2_BASELINE_SCOPE = CONDITIONAL_ON_ENDPOINT_COORDINATES_ONLY
```

## 3. Tres fuentes de desviación respecto del baseline

La hoja de ruta (CV-2) pide registrar con precisión qué cambia cuando (i) los
endpoints forman parte de la muestra, (ii) el intervalo es uno entre muchos
candidatos y (iii) la cuádrupla maximiza un score basado en `m`. Se separan aquí
como tres condicionamientos sucesivos, cada uno estrictamente más fuerte que el
anterior.

### 3.1 (i) Los endpoints son parte de la muestra

Por sí sola, esta condición **no** rompe CV-2.2: la demostración de §2.2 ya asume que
`a,b` son dos de los `n` puntos iid. Lo que cambia frente a un experimento con
endpoints verdaderamente exógenos es que `A` deja de ser un parámetro fijado por el
diseño y pasa a ser aleatorio, función de dos order statistics de la misma muestra.
Esto por sí mismo no introduce sesgo en `A_hat_count` (§2.3 vale condicionalmente a
cada valor de `A`, luego también marginalmente), pero sí determina la ley marginal
de `A` para un par "típico", que es la cantidad Q1 de §5.

### 3.2 (ii) El intervalo es uno entre muchos candidatos

Antes de aplicar ningún score, ya se exige `(a,b) prec`-comparables y `m>=3`. La
comparabilidad en sí misma es un evento con probabilidad `A` (para un par fijado);
condicionar sobre ella sesga la ley de `A` hacia valores mayores (un rectángulo más
grande es más fácil de "ganar" como comparable). Condicionar además sobre `m>=3`
sesga adicionalmente por el mismo mecanismo que hace `A_hat_count` no
automáticamente insesgado una vez seleccionado el candidato. Esta capa es más débil
que (iii): no involucra todavía una comparación entre candidatos, solo un filtro por
candidato.

### 3.3 (iii) La cuádrupla maximiza un score basado en `m`

Esta es la capa dominante. `MIN_COVERAGE_LEX` no elige `(a,b,c,d)` por ser
simplemente comparable con soporte mínimo: elige el máximo de `S_lex` sobre **todo**
`Q_3(C)`. Como `m_-` y `m_+` son ellos mismos ruidosos dados `A_-,A_+` (Binomial por
CV-2.1), el argmax favorece realizaciones donde el ruido binomial *también* jugó a
favor, no solo donde `A` era grande. Es exactamente el mecanismo de sesgo de
selección post-hoc: `E[m-2 | A, gano el argmax] != E[m-2 | A] = (n-2)A` en general.
Esta es la razón por la que CV-2.2 no puede aplicarse condicionando además sobre `S`:
`S` no es `sigma(u_a,v_a,u_b,v_b)`-medible, es medible respecto de la configuración
completa.

```text
CV2_DEVIATIONS = {
  (i)   ENDPOINTS_IN_SAMPLE:       no rompe insesgadez condicional, sí aleatoriza A,
  (ii)  ONE_AMONG_MANY_CANDIDATES: sesga la ley marginal de A hacia arriba,
  (iii) ARGMAX_ON_SCORE(m):        sesga m dado A vía seleccion del ruido binomial,
}
```

## 4. Diagrama de dependencias introducido por `MIN_COVERAGE_LEX`

```text
n puntos iid Uniform([0,1]^2), N=n
        |
        v
poset C  <->  permutacion uniforme pi (Fase 2)
        |
        v
Q_3(C) = { q=(a,b,c,d) : a prec b prec c prec d, m_-(q)>=3, m_+(q)>=3 }
        |                                   |
        v                                   v
(a,b) determina A_-=ell_-^2          (c,d) determina A_+=ell_+^2
        |                                   |
        v                                   v
m_-(q) = 2 + Binomial(n-2,A_-)*      m_+(q) = 2 + Binomial(n-2,A_+)*
        |                                   |
        +-----------------+-----------------+
                          |
                          v
        S_lex(q) = ( min(m_-(q),m_+(q)), m_-(q)+m_+(q) )
                          |
                          v
     q* = argmax sobre TODO Q_3(C) (no solo sobre un q fijo)
                          |
            +-------------+--------------+
            |                            |
       unico -> evento S            empate o vacio -> no-S
            |
            v
   observacion = (m_-,n,PAST,S) y (m_+,n,FUTURE,S)
   target = ell_- = sqrt(A_-),  ell_+ = sqrt(A_+)
```

`(*)` La flecha marcada solo es exacta en el sentido de CV-2.1/CV-2.2 **antes** de
condicionar sobre el resultado del argmax. Una vez fijado `S`, `m_-(q)` deja de ser
un Binomial limpio dado `A_-`: su ley pasa a depender de `A_+` y del resto de
`Q_3(C)` a través del propio argmax. Ese es el bucle de realimentación central: `m`
se construye a partir de `A` vía ruido binomial, pero **qué par `(A_-,A_+)` llega a
observarse** depende de ese mismo `m`. Es la razón estructural, no solo empírica, de
que `E[m-2|A]=(n-2)A` no implique `E[A_hat_count | m,n,side,S] = A` — la observación
histórica de sesgo positivo pequeño en
`P1a_resultados_representaciones_alternativas_d2.md` §5 es consistente con esta
lectura, aunque este documento no la deriva cuantitativamente.

## 5. Cantidades que deben derivarse antes de simular (CV-1, ítem 4)

Se listan sin resolver. Cada una alimenta directamente CV-3, CV-4 o CV-5.

```text
Q1  Ley marginal de A para un par (a,b) comparable "tipico" (antes de exigir m>=3):
    necesaria como referencia de cuanto sesga (ii) por si solo.

Q2  Ley conjunta (m,A) para un candidato en Q_3(C), es decir condicionado
    ademas a m>=3, pero SIN argmax: aisla el efecto (ii) del efecto (iii).

Q3  Distribucion de |Q_3(C)| dado n: cuantifica "cuantos candidatos compiten".

Q4  Ley conjunta (m_-,A_-,m_+,A_+) de la cuadrupla q* que maximiza S_lex,
    condicionada a S: el objeto central de CV-3.

Q5  Momentos marginales E[ell|m,n,side,S], Var[ell|m,n,side,S] derivados de Q4:
    alimentan directamente el estimando de la Seccion 1.5 y la cota de CV-4.

Q6  Cota inferior de riesgo (Bayes, Le Cam o informacion) para cualquier
    estimador medible de ell a partir de (m,n,side,S): CV-4.

Q7  Cuanto de la concentracion de min(m_-,m_+)/max(m_-,m_+) hacia 1
    proviene puramente de S_lex, comparado con un control de pares
    comparables sin argmax conjunto: CV-5.
```

**Nota estructural para Q1 y la ruta exacta (§6).** Ordenando los `n` puntos por `u`,
las coordenadas `u` son los order statistics de `n` uniformes en `[0,1]`, las
coordenadas `v` son también order statistics de `n` uniformes, y el patrón discreto
(qué rango de `v` corresponde a cada rango de `u`, es decir `pi`) es independiente de
ambas secuencias de magnitudes. Esta independencia rango/magnitud es la propiedad
estándar de estadísticos de orden de una muestra iid continua: la permutación de
rangos y los valores de los order statistics son variables independientes. Se sigue
que, condicionado a `pi` (es decir, condicionado a *qué* par de rangos define un
candidato), la ley de `A` para ese candidato depende solo de un hueco entre dos pares
de order statistics uniformes — un objeto con ley Beta conocida — y no de la
identidad combinatoria de `pi`. Esto separa el problema en una capa puramente
combinatoria (qué candidato gana el argmax, función solo de `pi`) y una capa
puramente de magnitudes (qué duración latente tiene el ganador, función de gaps de
order statistics dado el rango). Esta separación es la base propuesta para la ruta 1
de §6; no se ha ejecutado ni verificado numéricamente aquí.

## 6. Criterios para elegir cálculo exacto, cota o aproximación

Se fija el orden de intentos, ya enunciado en la hoja de ruta (§5, CV-3) y aquí hecho
operativo con un criterio de abandono explícito por ruta. El tránsito de una ruta a
la siguiente es unidireccional dentro de este contrato: no se revisita una ruta ya
abandonada sin una nota nueva que lo justifique.

```text
RUTA 1 — factorizacion exacta en la representacion por permutaciones
  usa: independencia rango/magnitud (Nota estructural, Seccion 5),
       reduccion de "quien gana el argmax" a un evento puramente
       combinatorio sobre pi.
  se abandona si: la suma sobre configuraciones de pi que ganan S_lex
       no admite forma cerrada ni recurrencia computable en tiempo
       razonable para el rango de n de interes.

RUTA 2 — cotas analiticas para el likelihood ratio seleccionado/no-seleccionado
  usa: comparacion estocastica, argumentos tipo FKG/asociacion entre
       m_-, m_+ y el evento de ser argmax.
  se abandona si: no se obtiene una cota no trivial (ni superior ni
       inferior informativa) sobre sigma2(m,n,side) o sobre el sesgo
       de A_hat_count | S.

RUTA 3 — enumeracion exacta en tamanos pequenos para conjeturar la forma
  usa: la infraestructura ya congelada de Fase 2
       (emergencia/p1a_enumeracion_simulacion.py,
        emergencia/resultados/p1a_enumeracion_exacta_d2.csv, n=6..9),
       extendida para registrar tambien A_-,A_+ ademas de vacio/unico/empate.
  se abandona si: el patron no estabiliza al crecer n dentro del rango
       exacto disponible, o si depende de un ajuste de forma libre no
       derivado (eso violaria el contrato de no ajustar una regresion
       para "descubrir" la rama, ya prohibido en HOJA_DE_RUTA.md §5 CV-3).

RUTA 4 — simulacion calibrada, SOLO despues de congelar una aproximacion
  usa: la aproximacion o cota fijada por una ruta anterior como hipotesis
       a contrastar, no como objetivo de ajuste.
  condicion de entrada: existe ya una prediccion cuantitativa (no un
       rango cualitativo) que la simulacion pueda confirmar o refutar.
```

Este documento no ejecuta ninguna ruta. Fija el orden y el criterio de abandono para
que el intento de CV-3 sea auditable.

## 7. Relación con CV-4 y CV-5 (no ejecutadas aquí)

- **CV-4** (cota de resolución) solo puede formularse con precisión una vez exista
  `Q5` (§5): `sigma2(m,n,side)` derivada de la ley seleccionada, no de la
  binomial base de §2, que sistemáticamente subestimará la varianza real al ignorar
  el sesgo de selección.
- **CV-5** (auditoría de circularidad) depende de `Q7` (§5) y de la ruta elegida en
  §6: cuantificar cuánto de `min(m_-,m_+)/max(m_-,m_+) ≈ 1` es forzado por `S_lex`
  requiere ya tener la ley conjunta `Q4`, no solo el baseline.

Ninguna de las dos se resuelve en este documento. Se mencionan únicamente para que
la dependencia quede registrada antes de intentar CV-3.

## 8. Techo de afirmación

Este documento:

- fija el estimando de CV-1 y prohíbe mezclarlo con ranking o razón (§1.5);
- deriva el baseline binomial de CV-2 con demostración completa (§2);
- identifica y nombra, sin resolver, las tres fuentes de desviación respecto de ese
  baseline (§3) y el bucle de realimentación que introduce el argmax (§4);
- lista las cantidades pendientes antes de simular (§5) y fija el orden de rutas para
  obtenerlas (§6).

No establece, y no debe citarse como si estableciera:

- el valor de `sigma2(m,n,side)` ni ninguna cota de resolución (CV-4, abierta);
- si `COUNT_VOLUME` es o no identificable bajo selección;
- si la circularidad señalada en `P1a_resultados_representaciones_alternativas_d2.md`
  §8 es benigna o dominante (CV-5, abierta);
- ningún resultado numérico nuevo — no se ha ejecutado código en este documento;
- autorización para calcular un cociente (`RATIO_STATUS` permanece `CLOSED`);
- validez fuera de `d=2`, `fixed-n`.

## 9. Estado de control

```text
CV1_ESTIMAND_FROZEN = YES
CV1_BASELINE_BINOMIAL_DERIVED = YES
CV1_DEPENDENCY_MAP = YES
CV1_OPEN_QUANTITIES = Q1,Q2,Q3,Q4,Q5,Q6,Q7 (SECTION_5, NOT_COMPUTED)
CV1_ROUTE_ORDER = EXACT_FACTORIZATION -> ANALYTIC_BOUND -> SMALL_N_ENUMERATION_CONJECTURE -> CALIBRATED_SIMULATION
CV1_NUMERICAL_EXECUTION_AUTHORIZED = NO
CV1_RATIO_AUTHORIZATION = NONE
CV1_HIGHER_DIMENSION_AUTHORIZATION = NONE
CV1_STATUS = COMPLETE
CV1_TERMINAL = CV1_CV2_THEORY_SCOPE_FROZEN_PROCEED_TO_CV3
NOVELTY_CERTIFIED = NO
```

## 10. Próxima acción concreta

Intentar la RUTA 1 de §6 sobre la nota estructural de §5 (independencia
rango/magnitud), primero de forma puramente algebraica y, si es necesario para
conjeturar la forma, extendiendo la enumeración exacta de Fase 2 a `A_-,A_+` para
`n=6,...,9` (RUTA 3, sin adelantarse a ella salvo como apoyo exploratorio explícito y
declarado). El entregable propuesto es

```text
emergencia/P1a_count_volume_ley_condicionada_d2.md
```

y corresponde a CV-3 de `emergencia/HOJA_DE_RUTA.md` §5. No se recomienda todavía
extender `n`, calcular un cociente, ni reabrir `d>=3`.

La Ruta 1 se intentó en
`emergencia/P1a_count_volume_ley_condicionada_d2.md`. Obtuvo un teorema de
factorización exacta que separa la ley seleccionada en un factor geométrico cerrado
(Beta-producto, independiente de la selección una vez fijada la forma del hueco) y
un factor puramente combinatorio (`w(s|m,n,side,S)`, distribución de la forma de la
cuádrupla ganadora) que queda abierto. No se abandona Ruta 1; el paso siguiente es
un contrato de extensión de la enumeración exacta de Fase 2 para registrar esa forma
en `n=6,...,9`, todavía no redactado ni ejecutado.
