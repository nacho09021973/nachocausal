# Caracterización analítica del canal físico y del observable `O`

```text
FECHA: 2026-09-12
NATURALEZA: derivación analítica; cero semillas, cero runs, cero validación
ALCANCE: caja EF fija, Schwarzschild 1+1D, cardinalidad N=n fija
NO_3PLUS1D
NO_RECALIBRACION_PREREG002
NO_NUEVO_OBSERVABLE
```

## 1. Experimento físico

Sea

\[
B=[0,T]\times[r_a,r_b],\qquad 0<r_a<r_b,
\]

la caja fija en coordenadas Eddington--Finkelstein `(v,r)`. Para un valor del
parámetro `\tau`, el orden causal en el parche se expresa mediante

\[
u_\tau(v,r)=-e^{-v/(2\tau)}W_\tau(r),
\qquad
W_\tau(r)=e^{r/\tau}(r/\tau-1),
\]

con

\[
(v,r)\prec_\tau(v',r')
\iff
v<v'\ \text{y}\ u_\tau(v,r)<u_\tau(v',r').
\]

La medida de sprinkling condicionada a `N=n` es uniforme en `B`, porque
`det(g_EF)=-1`. Por tanto, si

\[
X=(X_1,\ldots,X_n),\qquad X_i=(V_i,R_i),
\]

entonces `X` tiene densidad `|B|^{-n}` respecto de `dv\,dr`, independiente de
`\tau`; la dependencia paramétrica está en el mapa de orden
`T_{\tau,n}`.

## 2. Canal físico completo a poset

Definimos el canal etiquetado

\[
T_{\tau,n}:B^n\longrightarrow \mathsf{Pos}^{\mathrm{lab}}_n,
\qquad
T_{\tau,n}(x)_{ij}=1\{x_i\prec_\tau x_j\},
\]

y el cociente order-only

\[
\mathcal C_n:\mathsf{Pos}^{\mathrm{lab}}_n
\longrightarrow \mathsf{Pos}^{\mathrm{unlab}}_n,
\qquad
\mathcal C_n(P)=[P].
\]

El canal físico observable es, por tanto,

\[
K_{\tau,n}=\mathcal C_n\circ T_{\tau,n},
\qquad
Y_n=K_{\tau,n}(X)=[P_n].
\]

Para cada poset realizable `y`, su probabilidad es explícitamente

\[
q_{n,y}(\tau)
 =\Pr_\tau(Y_n=y)
 =\frac{1}{|B|^n}
   \int_{B^n}
   1\{K_{\tau,n}(x)=y\}\,dx.
\tag{2.1}
\]

Equivalente en coordenadas nulas, si `S_\tau` es la imagen de `B` y
`p_\tau` la densidad móvil indicada en
`wp6_domain_bridge_fixed_ef_box.md`,

\[
q_{n,y}(\tau)
 =\int_{S_\tau^n}
   1\{\mathcal C_n(T_n(z))=y\}
   \prod_{i=1}^n p_\tau(z_i)\,dz.
\tag{2.2}
\]

Las dos expresiones describen el mismo canal. La primera hace visible que el
soporte físico es fijo y que el mapa causal depende de `\tau`; la segunda hace
visible que, después del cambio a coordenadas nulas, el mapa order-only es fijo
pero la densidad tiene soporte móvil.

Para `n` fijo, el conjunto de posets realizables es finito. El soporte total
del canal de permutaciones y el push-forward finito establecidos en
`wp6_domain_bridge_fixed_ef_box.md` implican que cada `q_{n,y}` realizable es
positiva y `C^1` localmente. Luego la ley `q_n(\tau)` es una familia
categórica de soporte fijo y es QMD unilateralmente en los extremos del
intervalo y bilateralmente en su interior.

## 3. El observable congelado como segundo push-forward

Sea `P` un poset finito. Definimos su conjunto de mínimos

\[
\operatorname{Min}(P)=\{i:\nexists j\text{ con }j\prec_P i\},
\]

y, para `i\in\operatorname{Min}(P)`, su volumen futuro discreto

\[
O_P(i)=|\operatorname{Future}_P(i)|
       =|\{j:i\prec_P j\}|.
\tag{3.1}
\]

El observable de `prereg-002` no recibe `(v,r)`, `\tau`, ni etiquetas
geométricas. Es el mapa fijo

\[
A_n:\mathsf{Pos}^{\mathrm{unlab}}_n
\longrightarrow \mathsf A_n,
\qquad
A_n(P)=\operatorname{sort}\{O_P(i):i\in\operatorname{Min}(P)\},
\tag{3.2}
\]

donde `\mathsf A_n` es el conjunto finito de multisets admisibles. La
implementación sellada usa exactamente (3.1): `O_P(i)` es la suma de la
columna `i` de la matriz de orden; la posterior partición 1-D por 2-means y
el bracket son funciones deterministas adicionales del mismo `A_n(P)`.

La ley order-only del observable es, por tanto,

\[
r_{n,a}(\tau)
 =\Pr_\tau(A_n(Y_n)=a)
 =\sum_{y:A_n(y)=a}q_{n,y}(\tau).
\tag{3.3}
\]

Ésta es la relación analítica exacta entre el canal físico y el observable
concreto. En particular, para `n` fijo:

\[
r_n(\tau)=(A_n)_\#q_n(\tau),
\qquad
I_n^{A}(\tau)\le I_n^{[P]}(\tau)\le I_n^{\Pi}(\tau),
\tag{3.4}
\]

donde la segunda línea es sólo la contracción de Fisher entre canales fijos
posteriores al poset. No se afirma que ninguna desigualdad sea estricta ni
que `I_n^A(\tau)>0`.

## 4. Qué cambia en el protocolo Poisson

El benchmark usa una intensidad fija y `N` aleatorio. Si `\Lambda=\lambda|B|`
es independiente de `\tau`, la ley formal del observable es

\[
r_a^{\mathrm{Pois}}(\tau)
 =\sum_{n\ge0}e^{-\Lambda}\frac{\Lambda^n}{n!}
   r_{n,a}(\tau).
\tag{4.1}
\]

Para un truncamiento `n\le m`, (4.1) es una suma finita de familias `C^1`.
Para pasar a la suma infinita y derivar término a término hace falta una cota
dominante para `r'_{n,a}(\tau)` —o una condición equivalente de continuidad
en norma Hellinger— uniforme en `n`. Esa cota no está demostrada aquí ni en
el cierre fixed-`n`.

Por ello el canal físico queda caracterizado de manera completa a cardinalidad
fija, mientras que la ley Poisson no condicionada permanece como una obligación
analítica separada.

## 5. Relación exacta y límite de la relación con Fisher

La cadena correcta es

\[
X\xrightarrow{\ K_{\tau,n}\ }Y_n=[P_n]
 \xrightarrow{\ A_n\ }A_n(Y_n).
\tag{5.1}
\]

El primer mapa depende de `\tau`, porque el orden físico EF cambia con el
parámetro. El segundo mapa es fijo, order-only y coincide con el observable
congelado. Por eso la contracción

\[
I_n^A\le I_n^{[P]}
\]

es legítima, pero no se puede aplicar una desigualdad de procesamiento desde
la muestra EF latente hacia el poset usando un kernel fijo independiente de
`\tau`. Esto es exactamente la obstrucción de dominio ya registrada: la
regularidad del canal fixed-`n` no convierte automáticamente el observable en
un localizador Fisher del parámetro físico.

La afirmación observable que sí queda probada analíticamente es únicamente:

> Para cada `n` fijo, el benchmark order-only `O(i)=|future(i)|` es un
> push-forward bien definido de la ley física del poset no etiquetado, con una
> ley categórica `C^1`/QMD de soporte fijo.

No queda probado que `A_n` sea informativo sobre `\tau`, que su Fisher sea
positivo, que el bracket estime `r=2M`, ni que la mezcla Poisson preserve una
regularidad uniforme. Esas afirmaciones requerirían obligaciones nuevas y no
autorizan una validación adicional.

## 6. Estado resultante

```text
PHYSICAL_EF_TO_UNLABELED_POSET_FIXED_N = EXPLICIT
UNLABELED_POSET_TO_FUTURE_VOLUME_FIXED_N = EXPLICIT
FIXED_N_OBSERVABLE_LAW_C1_QMD = PROVED
FIXED_N_OBSERVABLE_FISHER_FINITE = PROVED
FIXED_N_OBSERVABLE_FISHER_POSITIVITY = NOT_ESTABLISHED
POISSON_MIXTURE_REGULARITY = OPEN
FISHER_TO_LOCALISATION = OPEN
PREREG002_CONTRACT = UNCHANGED
NEXT_RUN_AUTHORIZED = NO
```

## 7. Clasificación de T12 después de `A_n`

T12 (`INFINITE_RANK_SYMMETRIC_RETENTION`) es un resultado sobre el canal

\[
\Pi_n\longmapsto[P_{\Pi_n}],
\]

no sobre el resumen `A_n`. Su contenido es que, para una tangente simétrica
no nula `f` y cardinalidades suficientemente grandes,

\[
\frac{I_n^{[P]}(f)}{I_n^\Pi(f)}\longrightarrow1.
\tag{7.1}
\]

Por tanto T12 establece **visibilidad de primer orden en el poset completo**
si el Fisher de `\Pi_n` en esa dirección es positivo. No establece la misma
conclusión después del segundo push-forward:

\[
[P]\longmapsto A_n(P).
\]

La implicación que sí sería suficiente para el observable sería la existencia
de algún evento `B\subseteq\mathsf A_n` con

\[
\partial_\tau\Pr_\tau(A_n(Y_n)\in B)\ne0.
\tag{7.2}
\]

Pero (7.1) no proporciona (7.2): una función estadística puede conservar el
score completo del poset o una parte de él, y `A_n` puede eliminar exactamente
esa componente. En términos de scores,

\[
\dot\ell_{A_n(Y_n)}
 =\mathbb E_\tau[\dot\ell_{Y_n}\mid A_n(Y_n)],
\]

de modo que `I_n^O>0` exige que el score del poset tenga una componente no nula
visible en la sigma-álgebra generada por `A_n`. T12 no calcula esta
proyección.

La misma separación vale para la rama de segundo orden. La paridad o la
insensibilidad de primer orden de una dirección antisimétrica puede dar

\[
\partial_\tau q_{n,y}(\tau_0)=0,
\qquad
\partial_\tau^2 q_{n,y}(\tau_0)\ne0
\]

para algunos eventos del poset completo. Después de `A_n`, lo único que se
puede escribir sin una prueba adicional es

\[
\partial_\tau^2 r_{n,a}(\tau_0)
 =\sum_{y:A_n(y)=a}\partial_\tau^2q_{n,y}(\tau_0),
\]

y esta suma puede cancelarse. Por ello la visibilidad de segundo orden en
`[P]` tampoco implica visibilidad de segundo orden en `O_n`.

```text
T12_AT_UNLABELED_POSET_LEVEL = FIRST_ORDER_FISHER_VISIBILITY
T12_AT_FUTURE_COUNT_LEVEL     = NOT_ESTABLISHED
SECOND_ORDER_AT_POSET_LEVEL   = PROVED_FOR_SPECIFIED_ANTISYMMETRIC_WITNESS
SECOND_ORDER_AT_O_LEVEL       = PROVED_FOR_N2_CHAIN_ANTICHAIN_WITNESS
OBSERVABLE_FISHER_POSITIVITY  = OPEN
```

Ésta es la clasificación decisiva: **T12 mantiene viva la rama Fisher del
poset no etiquetado, pero no demuestra que el observable congelado de
`prereg-002` tenga Fisher positivo**. La siguiente obligación analítica queda
reducida a probar (7.2), o a demostrar que todas las derivadas primeras se
anulan y estudiar entonces la primera derivada de orden superior que sobreviva
tras `A_n`. No se abre todavía la mezcla Poisson ni se autoriza una nueva
validación.

## 8. Excepción ya cerrada: el witness de segundo orden en `N=2`

La última frase de §7 sería demasiado fuerte para el witness antisimétrico
concreto ya calculado en el Teorema 19 de la hoja de ruta. Para `n=2`, las dos
clases de poset son:

\[
\text{cadena}\ \longmapsto\ A_2=[1],
\qquad
\text{anticadena}\ \longmapsto\ A_2=[0,0].
\]

Por tanto `A_2` separa exactamente las dos clases que usa el testigo. El
resultado analítico existente

\[
\left.\frac{d^2}{d\varepsilon^2}
 \Pr_\varepsilon([P_2]=\text{anticadena})\right|_{0}=\frac85,
\qquad
\left.\frac{d^2}{d\varepsilon^2}
 \Pr_\varepsilon([P_2]=\text{cadena})\right|_{0}=-\frac85
\]

se transfiere literalmente a `A_2`. Luego existe un observable `O_2` con
visibilidad estrictamente de segundo orden y sin visibilidad de primer orden
para ese witness. Esto no da Fisher positivo en `\varepsilon=0`; da
identificabilidad local de `|\varepsilon|` y es compatible con la QMD
unilateral en `\theta=\varepsilon^2`.

La distinción final queda así:

```text
T12 -> O_n FIRST_ORDER_FISHER_POSITIVITY       = NOT_IMPLIED
T19_witness -> O_2 SECOND_ORDER_VISIBILITY     = PROVED
T19_witness -> O_2 FIRST_ORDER_FISHER_POSITIVE = NO
T19_witness -> O_2 ABS_EPSILON_IDENTIFIABILITY = PROVED
```

El resultado no alcanza todavía al observable `O(i)=|future(i)|` en el
benchmark Poisson de `prereg-002` para intensidades grandes: sólo certifica el
caso finito `N=2` y el testigo geométrico especificado. Pero sí resuelve la
clasificación conceptual solicitada: **hay una rama de segundo orden que
sobrevive a `A_n`, mientras que T12 por sí solo no certifica una rama Fisher
de primer orden para ese observable**.

## 9. Mezcla Poisson: pesos y canal condicionado

En el benchmark físico la caja EF `B` es fija y
`det(g_EF)=-1`. Para intensidad conocida `\rho`,

\[
\Lambda=\rho |B|,
\qquad
\pi_n=\Pr(N=n)=e^{-\Lambda}\frac{\Lambda^n}{n!},
\tag{9.1}
\]

no depende de `\tau`. Por tanto

\[
\pi_n'(\tau)=0,
\qquad
\pi_n''(\tau)=0.
\tag{9.2}
\]

Para el observable conjunto que conserva la cardinalidad, la ley exacta es

\[
Q_\tau(n,a)=\pi_n r_{n,a}(\tau),
\tag{9.3}
\]

y su score, cuando la mezcla es QMD, es puramente condicional:

\[
\dot\ell_Q(n,a)=\dot\ell_{n,a}(\tau).
\tag{9.4}
\]

No hay término de número ni información Fisher de cardinalidad. En particular,
para cualquier evento que retenga `N=2`, el witness de T19 sobrevive sin
atenuación conceptual:

\[
\left.\frac{d^2}{d\varepsilon^2}
 Q_\varepsilon(2,\text{anticadena})\right|_0
=\pi_2\frac85\ne0.
\tag{9.5}
\]

Esto es una señal del observable conjunto `(N,O_N)`, no una afirmación sobre
el marginal que olvida `N`.

Si se olvida la cardinalidad, la ley es

\[
R_a(\tau)=\sum_{n\ge0}\pi_n r_{n,a}(\tau).
\tag{9.6}
\]

Para derivar (9.6) término a término hace falta justificar una cota dominante
para las derivadas de `r_{n,a}`. El cierre fixed-`n` sólo da `C^1` y Fisher
finita para cada `n`; no da todavía una cota sumable uniforme en `n`. La ley
Poisson tiene momentos exponenciales, de modo que una cota de la forma

\[
|r_{n,a}'(\tau)|+|r_{n,a}''(\tau)|
\le C(1+n)^k e^{cn}
\tag{9.7}
\]

cerraría el intercambio, pero (9.7) no está demostrada para la caja EF móvil.

La consecuencia es una separación exacta de tres niveles:

```text
POISSON_WEIGHTS_DEPEND_ON_TAU              = NO (EF fixed box)
CARDINALITY_FIRST_ORDER_SIGNAL            = NONE
POISSON_ORDER_NUMBER_FACTORISATION        = PROVED
POISSON_MIXTURE_QMD_FIXED_N_CONDITIONALS  = OPEN_UNIFORM_BOUND
T19 -> (N,O_N) SECOND_ORDER SIGNAL        = PROVED (N=2 witness)
T19 -> marginal O_N SECOND_ORDER SIGNAL    = NOT_ESTABLISHED
```

Así, el único residuo analítico de `POISSON_MIXTURE_BRIDGE` no es una posible
señal espuria de cardinalidad: es la regularidad/intercambio de la mezcla
infinita y, para el marginal que descarta `N`, la posible cancelación entre
cardinalidades. `prereg-002` conserva `|C|` como parte de la entrada, pero su
observable congelado sigue siendo el push-forward `O_N`; no se modifica el
contrato para explotar (9.5).

## 10. Auditoría de la ruta propuesta `I_n^\Pi=nI_1^\Pi`

La ruta de cierre basada en

\[
I_n^\Pi(\tau)=nI_1^\Pi(\tau)
\tag{10.1}
\]

no está disponible para el canal físico EF y no puede añadirse como identidad
sin una hipótesis nueva.

Hay dos razones independientes.

1. `\Pi_n` es la permutación de rangos de una muestra iid, no el producto de
   `n` observaciones categóricas independientes. Su Fisher no es, por
   definición, `n` veces el Fisher de un objeto de un punto. En la rama S1 de
   la cópula, lo que sí está probado es una fórmula específica para
   `I_n^\Pi` y su escala asintótica en ciertos scores; no la identidad (10.1).

2. En la caja EF, los puntos `X_i=(V_i,R_i)` tienen ley uniforme
   independiente de `\tau`, pero el mapa que produce el orden causal sí es
   `T_{\tau,n}`-dependiente. Por tanto no existe un kernel de Markov fijo
   `X\mapsto\Pi_n` al que aplicar procesamiento de Fisher. En coordenadas
   nulas el mapa de rangos es fijo, pero la ley `p_\tau` tiene soporte móvil y
   el experimento puntual no es QMD; no proporciona un Fisher de un punto
   finito que pueda servir como `\bar I`.

La desigualdad

\[
I_n^{O}(\tau)\le I_n^{[P]}(\tau)\le I_n^\Pi(\tau)
\]

sí es válida porque los dos últimos push-forwards son canales fijos una vez
obtenido `\Pi_n`. Pero no suministra por sí sola una cota `O(n)` para
`I_n^\Pi` en la familia física EF.

En consecuencia, la sugerencia de dominación Poisson sería válida si se
demostrase separadamente una cota física uniforme, por ejemplo

\[
\sup_{\tau\in U} I_n^\Pi(\tau)\le C_U(1+n)^k,
\tag{10.2}
\]

o una cota equivalente sobre el módulo QMD de las leyes `Q_{n,\tau}`. Pero
`(10.2)` no se sigue de T12 ni de la regularidad categórica fixed-`n`.

```text
POISSON_WEIGHT_DERIVATIVE_TERM          = ZERO (EF fixed box)
I_n_PI_EQUALS_n_I_1_PI                  = NOT_ESTABLISHED / NOT_GENERIC
FISHER_PROCESSING_FROM_EF_POINTS        = NOT_APPLICABLE
SUMMABLE_POISSON_QMD_BOUND              = OPEN
POISSON_MIXTURE_QMD                     = OPEN_UNIFORM_BOUND
```

La ruta propuesta reduce correctamente el problema a una cota sumable si tal
cota existiera, pero no la demuestra en el modelo físico vigente. Por tanto no
se eleva todavía `POISSON_MIXTURE_QMD` a `PROVED`.

## 11. Auditoría del lema `POISSON_QMD_REMAINING_LEMMA`

Las fórmulas ya existentes sí proporcionan una primera envolvente explícita
para el canal de permutaciones:

\[
I_n^{[P]}(\tau)\le I_n^\Pi(\tau)
\le \frac{n!}{a_K^n}\,n(n-1)^2\kappa_K^2,
\tag{11.1}
\]

uniforme en `\tau\in K` (`wp6_domain_bridge_fixed_ef_box.md`, (15.10)). Al
multiplicar por la ley Poisson se obtiene solamente

\[
\pi_n B_n
\le e^{-\Lambda}\,n(n-1)^2\kappa_K^2
\left(\frac{\Lambda}{a_K}\right)^n.
\tag{11.2}
\]

Esta serie es útil si `\Lambda<a_K`, pero el cierre no establece esa condición
para el benchmark y `a_K` procede de una probabilidad mínima de celda local,
que puede ser muy pequeña. Por tanto (11.1) no satisface el lema solicitado en
el régimen general.

La propia auditoría del dominio identifica el paso faltante: sustituir el
mínimo global de celda por una cota de flujo ponderado/subfactorial. En la
notación existente, siguen abiertos el control de `C_{n,K}` en (16.7), el
`ACTIVE_ENDPOINT_TO_MEAN_THICKNESS_LEMMA` y el `UNIFORM_SQRT_SCORE_MODULUS`.
No hay en los Teoremas 12--19 una cota física adicional que cierre esos
sublemas: esos teoremas trabajan en la familia de cópula/poset de S1 y no
controlan las interfaces móviles del canal EF al crecer `n`.

```text
POISSON_QMD_REMAINING_LEMMA       = NOT_CLOSED
AVAILABLE_BOUND                   = FACTORIAL_OVER_EXPONENTIAL (15.10)
POISSON_SUMMABILITY_FROM_15_10    = CONDITIONAL_ON_LAMBDA_LT_AK
SUBFACTORIAL_FISHER_BOUND         = OPEN
UNIFORM_SQRT_SCORE_MODULUS        = OPEN
POISSON_MIXTURE_QMD               = OPEN_UNIFORM_BOUND
```

Conclusión: el objetivo queda aislado y su primer intento analítico ya está
agotado con las cotas existentes. No se cambia el estado a `PROVED`, no se
abre una hipótesis nueva y no se autoriza ningún run. El único progreso
admisible posterior sería demostrar una cota subfactorial de flujo ponderado o
un módulo QMD uniforme en `n`; de no aparecer tal lema, el puente Poisson se
mantiene correctamente aparcado.

## 12. Resultado del intento `GLOBAL_WEIGHTED_ORDER_CELL_FLUX_BOUND`

La auditoría del material existente confirma que esta es la reducción correcta
y que ya está formulada sin usar la celda mínima global. Si `J_{\sigma,\eta}`
es el flujo firmado entre celdas adyacentes y `Q_{\sigma,\eta}` su flujo
absoluto, entonces

\[
\pi_\sigma'=\sum_{\eta\sim\sigma}J_{\sigma,\eta},
\qquad
\sum_{\{\sigma,\eta\}}Q_{\sigma,\eta}
\le \binom n2\kappa_K.
\]

La única pieza que falta es una comparación local o integrada entre flujo y
masa. En la notación del preflight existente, basta probar

\[
Q_\sigma\le C_{n,K}\pi_\sigma,
\qquad
C_{n,K}\le C_K^n\operatorname{poly}(n),
\tag{12.1}
\]

porque entonces la desigualdad de Cauchy--Schwarz sobre las interfaces daría

\[
I_n^\Pi(\tau)
\le C_{n,K}\sum_{\sigma,\eta\sim\sigma}Q_{\sigma,\eta}
\le C_K^n\operatorname{poly}(n).
\]

El slicing radial ya reduce (12.1) al `INTEGRATED_ADJACENT_GAP_HAZARD_LEMMA`:
la masa contiene la longitud de un intervalo factible `\ell`, mientras que el
flujo contiene la velocidad `w` en un extremo activo. Las cotas actuales
controlan `w` superiormente y el flujo total, pero no controlan la medida
agregada de los slices con `\ell` pequeño. Tampoco hay una familia de celdas
raras que pruebe una obstrucción.

Por tanto, tras revisar la ruta positiva y su ataque adversarial, no aparece
un cierre analítico adicional en T12--T19 ni en las fórmulas ya existentes:

```text
GLOBAL_WEIGHTED_ORDER_CELL_FLUX_BOUND = OPEN_REDUCED
INTEGRATED_ADJACENT_GAP_HAZARD        = OPEN_REDUCED
SUBFACTORIAL_C_NK                     = NOT_PROVED
RARE_CELL_OBSTRUCTION                 = NOT_PROVED
POISSON_QMD_REMAINING_LEMMA           = NOT_CLOSED
```

Éste es un aparcamiento matemático genuino, no una falta de elección del
objetivo: el obstáculo restante es exactamente la distribución de masa de los
gaps radiales delgados. No se abre ninguna hipótesis, validación o run.

## 13. ¿Puede T19 producir una consecuencia falsable para `prereg-002`?

La respuesta es **no dentro del contrato congelado**. La comparación de los
dos experimentos separa cuatro incompatibilidades independientes:

| Eje | T19 | `prereg-002` |
|---|---|---|
| Familia | deformación conforme alrededor de un diamante Minkowski `1+1` | Schwarzschild `1+1` en caja EF fija, con control Minkowski |
| Parámetro | `\varepsilon`, con ley par y señal en `\varepsilon^2` | parámetro físico de localización asociado a `r=2M` |
| Cardinalidad | testigo exacto en `N=2` (también `N=3`) | Poisson, intensidades `1500,3000,6000,12000` |
| Claim | separación de leyes de cadena/anticadena | bracket de localización basado en `O(i)=|future(i)|`, estabilidad y falso positivo |

T19 sí prueba una afirmación falsable autónoma: para su witness y `N=2`,
`A_2` distingue cadena y anticadena a segundo orden en `|\varepsilon|`. Pero
no proporciona una aplicación `\varepsilon\mapsto\tau`, no identifica la
frontera `r=2M`, no controla la mezcla Poisson física y no demuestra que la
señal de `O_N` a intensidades grandes produzca el bracket congelado.

Convertir T19 en una predicción de `prereg-002` exigiría cambiar al menos uno
de los elementos sellados: familia geométrica, parámetro, cardinalidad,
endpoint o protocolo de análisis. Eso sería una nueva validación o un nuevo
benchmark, no una consecuencia del preregistro vigente.

```text
T19_TO_PREREG002_FALSIFIABLE_TRANSFER = NOT_ESTABLISHED
T19_STRUCTURAL_RESULT                 = CLOSED_AUTONOMOUSLY
POISSON_QMD_BRANCH                    = PARKED_OPEN_REDUCED
POISSON_REOPEN_CRITERION              = HAZARD_BOUND_OR_SUBFACTORIAL_C_NK_OR_RARE_CELL_OBSTRUCTION
PREREG_002                            = UNCHANGED
NEW_VALIDATION_RUNS                   = NOT_AUTHORIZED
SCHWARZSCHILD_3P1                     = NOT_AUTHORIZED
```

El criterio de reapertura queda objetivo: una nueva desigualdad sobre el
`INTEGRATED_ADJACENT_GAP_HAZARD`, una cota subfactorial para `C_{n,K}`, o una
obstrucción demostrada por rare cells. Hasta entonces, T19 permanece como
resultado estructural de identificabilidad de segundo orden y no como soporte
del benchmark físico.
