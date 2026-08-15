# Backlog de hallazgos fuera de perímetro

## 2026-08-15 — Línea EF-0–EF-8 sobre entropía de fibras

```text
BACKLOG_STATUS: OUT_OF_SCOPE
SOURCE_PATH: docs/hoja_de_ruta_agosto_2026.md
MOVED_BY_PI_AUTHORIZATION: Ignacio, 2026-08-15
FORUM_VERDICT: REVISE_AND_RECONVENE
ACTIVE_PROGRAM_STATUS: NONE
```

Por autorización explícita del PI, la línea completa EF-0–EF-8 se retira del trabajo
en curso y se conserva a continuación como hallazgo fuera de perímetro, de acuerdo con
`docs/program_reopening_note_2026-07-31.md` §6.2 y
`docs/program_reopening_note_2026-08-05_R3.md` §1. El traslado resuelve únicamente el
punto C-2 de `docs/foro/foro_decision_001_ef4-falsacion-adversarial.md`.

El contenido trasladado se conserva como registro histórico, no como línea autorizada
ni como certificado matemático vigente. En particular, sus tokens internos no prevalecen
sobre `FORO_VERDICT=REVISE_AND_RECONVENE`; C-1, C-3 y C-4 permanecen sin adjudicar, y
este traslado no autoriza ampliar la enumeración ni ejecutar el test no vacuo en `n=24`.

---

# Documento trasladado: Hoja de ruta — agosto de 2026
## Entropía de fibras y ley condicionada de `COUNT_VOLUME`

```text
ESTADO: CIERRE FUERTE EN FIBER_CONCENTRATION; EF-6 Y EF-7 COMPLETADOS
FECHA DE APERTURA: 2026-08-11
ÚLTIMA ACTUALIZACIÓN: 2026-08-12
LÍNEA: emergencia / identificabilidad del tiempo métrico
OBJETO: ley condicionada de Z_n = sqrt(KL)/(n+1)
CANAL: fixed-n, d=2, poset no etiquetado + conteos internos
ÚLTIMA EJECUCIÓN: generalización deductiva EF-7; cero simulaciones y cero semillas
SELLO: intacto; no se toca
```

Esta hoja fija el próximo trabajo de `nachocausal` después del cierre de P5.2. Amplía
de forma acotada el perímetro de trabajo, pero **no revoca**
`docs/program_closure_note_2026-07-30.md`, no reabre reconstrucción de horizonte y no
modifica los terminales de WP7. La nueva línea pertenece al problema independiente de
identificabilidad métrica de `emergencia/`.

## 1. Pregunta única

En el experimento `fixed-n`, `d=2`, condicionado a que `MIN_COVERAGE_LEX` seleccione
una cuádrupla única, ¿la cardinalidad lateral observada

\[
M=|I[a,b]|
\]

determina asintóticamente la duración relativa del intervalo, o la multiplicidad de
formas compatibles con el mismo valor de `M` conserva una dispersión irreducible?

La reducción ya probada muestra que basta decidir la ley condicionada de

\[
Z_n=\frac{\sqrt{KL}}{n+1},
\]

donde `K` y `L` son los gaps de rangos nulos de los extremos seleccionados. El objetivo
no es reconstruir una escala absoluta: `Z_n` es relativo y adimensional.

## 2. Punto de partida probado

Se parte únicamente de los siguientes resultados internos:

1. La permutación de rangos es independiente de las magnitudes de los estadísticos de
   orden. Condicionada a una forma `T=(K,L)`, la duración tiene una ley Beta-producto
   exacta.
2. La ley seleccionada factoriza como

   \[
   \mathcal L(\ell\mid M=m,n,h,S)
   =\sum_s w_n^h(s\mid m,S)\,\mathcal L_{\rm Beta}(\ell\mid s).
   \]

3. El ruido Beta-producto dentro de una forma satisface `P_{1,n}->0` uniformemente.
4. El único término no resuelto es

   \[
   P_{2,n}
   =\mathbb E_M\!\left[\operatorname{Var}_T
     (\mu_n(T)\mid M,n,h,S)\right],
   \]

   y tiene el mismo comportamiento asintótico que

   \[
   Q_{2,n}
   =\mathbb E_M\!\left[\operatorname{Var}
     (Z_n\mid M,n,h,S)\right].
   \]

5. Los artefactos existentes no contienen `K`, `L` ni su producto y, por tanto, no
   permiten decidir `P_{2,n}`.

Anclas:

- `emergencia/P1a_count_volume_ley_condicionada_d2.md` §7;
- `emergencia/P1a_count_volume_lema_kl_d2.md` §7;
- `emergencia/HOJA_DE_RUTA.md` §§5–6.

Nada de esta hoja eleva esos resultados por encima de sus techos actuales.

## 3. Nueva formulación: entropía de la fibra

Sea `\mathfrak S_n` el conjunto de permutaciones de tamaño `n`. Para lado
`h in {PAST,FUTURE}`, evento de selección única `S`, conteo `m` y forma
`s=(k,l)`, se define

\[
\Omega_n^h(s,m;S)
=\#\{\pi\in\mathfrak S_n:
S(\pi),\ M_h(\pi)=m,\ T_h(\pi)=s\}.
\]

Como `pi` es uniforme,

\[
w_n^h(s\mid m,S)
=\frac{\Omega_n^h(s,m;S)}
       {\sum_{s'}\Omega_n^h(s',m;S)}.
\]

Definimos la **entropía de la fibra**

\[
\mathsf S_n^h(s;m,S)=\log\Omega_n^h(s,m;S)
\]

cuando la multiplicidad es positiva. Esta definición no introduce física nueva: es el
logaritmo del número de configuraciones discretas compatibles con la observación. Su
función es aislar la parte combinatoria ya presente en `w_n`.

Para el pushforward mínimo se usará

\[
C_n^h(m,r;S)
=\#\{\pi\in\mathfrak S_n:S(\pi),\ M_h(\pi)=m,\ K_h(\pi)L_h(\pi)=r\}.
\]

La tabla bidimensional completa de `(K,L)` solo se calculará si los conteos por
`r=KL` no bastan para decidir `Q_{2,n}`.

### Fuente de la idea

`biblioteca/2608.09007v1.pdf`, Bucicovschi y Meyer, se usa como **inspiración
metodológica**: allí una multiplicidad de estados modifica la ley del sector dominante
y el condicionamiento cerca de un umbral produce una ley universal. No es una fuente
sobre causal sets, no prueba ningún resultado de esta hoja y no autoriza una conexión
con entropía gravitatoria.

En particular, no se presume que la ley de Gauss–Kuzmin aparezca aquí. Solo podrá
mencionarse de nuevo si una derivación de las multiplicidades o de sus cocientes produce
esa ley sin ajuste.

## 4. Hipótesis rivales y terminales científicos

La investigación debe poder terminar en cualquiera de los estados siguientes:

```text
FIBER_CONCENTRATION
  Q_{2,n} -> 0 y, por las equivalencias ya probadas, P_{2,n} -> 0.
  COUNT_VOLUME es consistente para el estimando lateral relativo declarado.

PERSISTENT_FIBER_DISPERSION
  liminf Q_{2,n} > 0, con masa no evanescente y separación cuantitativa.
  Ninguna función de M sola reconstruye consistentemente la duración relativa
  seleccionada, sin extender el no-go al poset completo.

INTERMEDIATE_OR_SUBSEQUENTIAL_REGIME
  liminf Q_{2,n} = 0 < limsup Q_{2,n}; se refuta la consistencia sobre la
  sucesión completa, pero no se obtiene dispersión persistentemente positiva.

EXACT_FINITE_N_ONLY
  Se obtiene una ley o recurrencia finito-muestral verificable, pero no se cierra
  su asintótica.

OPEN_AFTER_FIBER_AUDIT
  La primera obligación combinatoria no resuelta queda identificada con un
  enunciado exacto y no se fuerza una conclusión.
```

Exhibir dos formas distintas con el mismo `M` no basta para
`PERSISTENT_FIBER_DISPERSION`: se exige masa no evanescente y separación de
`sqrt(KL)/(n+1)`.

## 5. Paquetes de trabajo, en orden obligatorio

### EF-0 — Contrato matemático sellado

Este apartado es el entregable de EF-0. Congela el objeto que deberá estudiar el
trabajo posterior; no contiene un recuento de ninguna fibra y no autoriza
enumeración, simulación ni cambios de código.

#### EF-0.1 Espacio finito y evento de selección

Para cada `n` fijo, el espacio elemental es

\[
\mathfrak S_n=\{\text{permutaciones de }\{1,\ldots,n\}\},
\qquad
\mathbb P_n(\{\pi\})=\frac1{n!}.
\]

Esta es la medida inducida por los rangos de los puntos iid uniformes en el cuadrado.
El condicionamiento `N=n` ya está incorporado al elegir `\mathfrak S_n`; `n` no es
una variable aleatoria dentro de este espacio.
No se usa la medida uniforme sobre clases de isomorfía de posets: si varias
permutaciones producen el mismo poset no etiquetado, conservan la multiplicidad que
les asigna el experimento iid.

La permutación `pi` representa los puntos por su rango en `U`: para el punto `i`,
`rank_U(i)=i` y `rank_V(i)=pi(i)`. El orden es

\[
i\prec_\pi j \quad\Longleftrightarrow\quad i<j\ \text{ y }\ \pi(i)<\pi(j).
\]

Sobre este poset se aplica, sin variantes, `MIN_COVERAGE_LEX`: entre las cadenas
`q=(a,b,c,d)` con `a prec b prec c prec d` y
`|I[a,b]|,|I[c,d]|>=3`, se maximiza lexicográficamente

\[
\bigl(\min\{|I[a,b]|,|I[c,d]|\},\ |I[a,b]|+|I[c,d]|\bigr).
\]

`S(pi)` es el evento de que ese maximizador exista y sea único, y `q*(pi)` denota
la cuádrupla ganadora. Solo se consideran `n` con
`P_n(S)>0`. El lado

\[
h\in\{\mathrm{PAST},\mathrm{FUTURE}\}
\]

se fija antes de condicionar; no se sortea ni se mezcla. Si
`q*=(a,b,c,d)`, se escriben

\[
(x_h,y_h)=
\begin{cases}
(a,b),&h=\mathrm{PAST},\\
(c,d),&h=\mathrm{FUTURE}.
\end{cases}
\]

#### EF-0.2 Fibra de `COUNT_VOLUME` y significado de `M`, `K` y `L`

Para la clausura reflexiva `preceq_pi` del orden anterior, el intervalo causal cerrado
y su cardinalidad lateral son

\[
I_\pi[x_h,y_h]
=\{z:x_h\preceq_\pi z\preceq_\pi y_h\},
\qquad
M_h(\pi)=|I_\pi[x_h,y_h]|.
\]

Los extremos están incluidos en `M`. Para `n` fijo,

\[
\operatorname{COUNT\_VOLUME}_n(m)
=\sqrt{\frac{m-2}{n-2}}
\]

es estrictamente creciente en `m`; por tanto, una fibra de `COUNT_VOLUME` es
exactamente una fibra de `M`, no una fibra de la duración latente ni del producto
`KL`.

Los dos gaps de rangos nulos **del lado fijado de la cuádrupla ganadora** son

\[
K_h(\pi)
=\operatorname{rank}_U(y_h)-\operatorname{rank}_U(x_h),
\qquad
L_h(\pi)
=\operatorname{rank}_V(y_h)-\operatorname{rank}_V(x_h).
\]

`K` y `L` son enteros combinatorios: no son los gaps continuos `Delta U,Delta V`,
no son cardinalidades del intervalo y no incluyen información del otro lado. Tras
fijar `h` se suprime su superíndice y se define

\[
T=(K,L),\qquad r=KL,\qquad
Z_n=\frac{\sqrt{KL}}{n+1}.
\]

Para cada valor alcanzable de `m`, el espacio finito condicionado es

\[
\mathcal F_{n,m}^{h,S}
=\{\pi\in\mathfrak S_n:S(\pi),\ M_h(\pi)=m\}.
\]

Su soporte real de formas es, por definición,

\[
\mathcal T_{n,m}^{h,S}
=\{(K_h(\pi),L_h(\pi)):\pi\in\mathcal F_{n,m}^{h,S}\}.
\]

No se sustituirá este conjunto por una caja rectangular. Las condiciones ya probadas
solo dan el sobre de soporte

\[
n\ge 6,\qquad m\ge3,\qquad
m-1\le K,L\le n-4;
\]

no afirman que todo par entero dentro de ese sobre sea alcanzable después de la
selección global.

#### EF-0.3 Medida condicionada y ley finita exacta

Para `m` tal que `\mathcal F_{n,m}^{h,S}` no sea vacío, la medida condicionada es
uniforme sobre esa fibra:

\[
\mathbb P_{n,m}^{h,S}(A)
=\mathbb P_n(A\mid M_h=m,S)
=\frac{|A\cap\mathcal F_{n,m}^{h,S}|}
       {|\mathcal F_{n,m}^{h,S}|}.
\]

Esta igualdad depende de que la medida base sea uniforme sobre permutaciones. La ley
finita exacta objeto de la pregunta es el `pushforward`

\[
\nu_{n,m}^{h,S}
:=\mathcal L(Z_n\mid M_h=m,n,h,S)
=(Z_n)_\#\mathbb P_{n,m}^{h,S}.
\]

Equivalentemente, con

\[
C_n^h(m,r;S)
=\#\{\pi\in\mathfrak S_n:S(\pi),\ M_h(\pi)=m,
K_h(\pi)L_h(\pi)=r\},
\]

se tiene la identidad definitoria

\[
\nu_{n,m}^{h,S}
=\sum_r
\frac{C_n^h(m,r;S)}{\sum_{r'}C_n^h(m,r';S)}
\,\delta_{\sqrt r/(n+1)}.
\]

Escribir esta identidad no cuenta como haber resuelto los conteos. Solo fija sin
ambigüedad qué ley debería determinar una fórmula, recurrencia o argumento
asintótico posterior.

La masa de cada estrato, bajo la selección única, es

\[
p_n^h(m\mid S)
=\mathbb P_n(M_h=m\mid S)
=\frac{|\mathcal F_{n,m}^{h,S}|}
       {|\{\pi\in\mathfrak S_n:S(\pi)\}|}.
\]

El objetivo primario es el funcional agregado

\[
Q_{2,n}^h
=\sum_m p_n^h(m\mid S)
\left\{
\int z^2\,d\nu_{n,m}^{h,S}(z)
-\left(\int z\,d\nu_{n,m}^{h,S}(z)\right)^2
\right\}.
\]

Una afirmación uniforme en todos los `m` alcanzables es más fuerte y no forma parte
del contrato primario. Toda afirmación por estratos deberá especificar una sucesión
`m=m_n`, una región de valores típicos o una cota uniforme; no se permitirá que un
estrato de masa evanescente decida por sí solo el comportamiento agregado.

#### EF-0.4 Qué significa «decidir la ley condicionada»

Se separan dos niveles que no son equivalentes:

1. **Nivel finito exacto.** Determinar, para los `n`, lados y `m` declarados, los
   pesos de `nu_{n,m}^{h,S}` mediante una fórmula o recurrencia exacta y verificable.
   La definición por cardinalidades anterior, sin resolverlas, no satisface este
   nivel.
2. **Nivel asintótico.** Caracterizar las leyes condicionadas, o directamente sus
   dos primeros momentos, con fuerza suficiente para decidir el comportamiento de
   `Q_{2,n}^h` cuando `n->infinity` por valores con `P_n(S)>0`.

**Decisión de alcance de EF-0:** el nivel asintótico es el objetivo científico
primario. No se exige una fórmula finita cerrada como condición previa ni como parte
obligatoria del cierre. Una prueba asintótica rigurosa que decida `Q_{2,n}^h` basta,
aunque no determine todos los pesos finitos. En sentido inverso, una ley o
recurrencia finita exacta sin control de su asintótica termina en
`EXACT_FINITE_N_ONLY` y no decide la pregunta principal. Obtener ambos niveles es un
resultado más fuerte, no una exigencia del contrato.

Un mero límite débil de la marginal
`L(Z_n|n,h,S)` **no basta**, porque puede borrar precisamente la información que
conserva `M`. Un teorema de ley límite será suficiente solo si mantiene el núcleo
condicional `nu_{n,M_h}^{h,S}` —o entrega control equivalente de sus momentos— y
permite concluir sobre el promedio que define `Q_{2,n}^h`. No es obligatorio que la
ley límite tenga una densidad o un nombre cerrado: cotas rigurosas de momentos pueden
decidir el funcional sin identificar toda la ley.

#### EF-0.5 Resultados positivos, negativos e inconclusos

La clasificación se hace por separado para cada lado `h`; no se transfiere un
resultado entre `PAST` y `FUTURE` hasta que EF-1 pruebe la simetría pertinente.

- **Positivo para identificabilidad (`FIBER_CONCENTRATION`):**
  `Q_{2,n}^h -> 0` a lo largo de la sucesión completa admisible. Por las
  equivalencias ya probadas, esto cierra también `P_{2,n}^h -> 0`.
- **Negativo para consistencia basada solo en `M`:**
  `limsup_{n->infinity} Q_{2,n}^h>0`. El terminal negativo fuerte
  `PERSISTENT_FIBER_DISPERSION` exige además
  `liminf_{n->infinity}Q_{2,n}^h>0`. Si
  `liminf Q_{2,n}^h=0<limsup Q_{2,n}^h`, el resultado refuta la consistencia a lo
  largo de la sucesión completa, pero se registra bajo
  `INTERMEDIATE_OR_SUBSEQUENTIAL_REGIME`, no como dispersión persistentemente
  positiva.
- **Inconcluso:** no se demuestra ni `Q_{2,n}^h->0` ni un `limsup` positivo. En
  particular, son inconclusos para la pregunta principal una tabla para pocos `n`,
  una fórmula finita sin asintótica, un límite marginal que descarte `M`, una sola
  subsecuencia concentrada o la mera existencia de dos formas con el mismo `m`.

Un certificado negativo basado en sectores separados deberá cuantificar tanto una
separación no evanescente en `Z_n` como la masa condicionada de esos sectores y la
masa de los estratos de `M` que contribuyen al promedio. La coexistencia combinatoria
sin control de masas no es una obstrucción estadística.

#### EF-0.6 Prohibición de Gauss–Kuzmin

La ley de Gauss–Kuzmin no puede usarse como hipótesis de partida, `ansatz`, familia
de ajuste, elección de normalización, regularizador ni criterio para seleccionar un
terminal. Ningún paso podrá asumir sus probabilidades, sus cocientes o su forma para
deducir `C_n^h`, `nu_{n,m}^{h,S}` o `Q_{2,n}^h`. Solo cabrá compararla, después de una
derivación independiente, si una identidad o un teorema de convergencia la produce
sin ajuste; una semejanza numérica no contará como derivación.

```text
EF0_CONTRACT = FIXED_IN_THIS_ROADMAP
PRIMARY_OBJECT = CONDITIONAL_KERNEL_nu(n,m,h,S)_AND_AGGREGATE_Q2
FINITE_EXACT_FORMULA = OPTIONAL_STRONGER_RESULT
ASYMPTOTIC_CONTROL_DECIDING_Q2 = REQUIRED_FOR_PRIMARY_CLOSURE
MARGINAL_WEAK_LIMIT_WITHOUT_M = INSUFFICIENT
GAUSS_KUZMIN_AS_STARTING_HYPOTHESIS = FORBIDDEN
EF1_ENUMERATION_SIMULATION_CODE = NOT_AUTHORIZED_BY_EF0
```

**Gate EF-0:** ninguna enumeración ni modificación de código puede comenzar antes
de revisar este contrato contra las definiciones probadas. Un documento separado
posterior podrá reproducirlo, pero no cambiar el espacio, la medida, el
condicionamiento o los criterios sin reabrir explícitamente EF-0.

### EF-1 — Identidades y simetrías exactas

Este apartado cierra la parte deductiva previa a cualquier recuento. Todas las
igualdades siguientes valen para `n` con `P_n(S)>0` y, cuando se condiciona por
`m`, solo para fibras no vacías.

#### EF-1.1 Normalización exacta de `Omega`

Defínase

\[
D_n^h(m;S)
:=|\mathcal F_{n,m}^{h,S}|
=\sum_{s\in\mathcal T_{n,m}^{h,S}}\Omega_n^h(s,m;S).
\]

La segunda igualdad es una partición disjunta de la fibra por el valor de
`T_h=(K_h,L_h)`. Como la medida base asigna masa `1/n!` a cada permutación,

\[
\begin{aligned}
w_n^h(s\mid m,S)
&=\mathbb P_n(T_h=s\mid M_h=m,S)\\
&=\frac{\Omega_n^h(s,m;S)}{D_n^h(m;S)}.
\end{aligned}
\tag{EF1.1}
\]

No interviene un supuesto de equiprobabilidad adicional: la uniformidad dentro de la
fibra es la restricción de la medida uniforme sobre `\mathfrak S_n` fijada en EF-0.

#### EF-1.2 Reducción exacta al producto `r=KL`

Para distinguir una fibra de forma de su agregación por producto, defínase

\[
\mathcal F_{n,m,r}^{h,S}
:=\{\pi\in\mathcal F_{n,m}^{h,S}:K_h(\pi)L_h(\pi)=r\}
=\bigsqcup_{\substack{(k,l)\in\mathcal T_{n,m}^{h,S}\\kl=r}}
\{\pi\in\mathcal F_{n,m}^{h,S}:T_h(\pi)=(k,l)\}.
\]

La unión es disjunta aunque varios pares distintos puedan tener el mismo producto.
Por la definición fijada en EF-0,

\[
C_n^h(m,r;S)
=|\mathcal F_{n,m,r}^{h,S}|
=\sum_{\substack{(k,l)\in\mathcal T_{n,m}^{h,S}\\kl=r}}
  \Omega_n^h((k,l),m;S),
\qquad
D_n^h(m;S)=\sum_r C_n^h(m,r;S).
\tag{EF1.2}
\]

Como la aplicación `r -> sqrt(r)/(n+1)` es inyectiva en los enteros positivos,

\[
\mathbb P_n\!\left(
Z_n=\frac{\sqrt r}{n+1}\,\middle|\,M_h=m,S
\right)
=\frac{C_n^h(m,r;S)}{D_n^h(m;S)}.
\tag{EF1.3}
\]

Por tanto `C_n^h`, sin recuperar qué factor de `r` era `K` y cuál era `L`, determina
exactamente la ley finita de `Z_n`. La tabla bidimensional de formas solo contiene
información adicional que este `pushforward` descarta deliberadamente.
Aquí `n` y `h` son parámetros fijados de la familia: el condicionamiento aleatorio es
por `{M_h=m}\cap S`, no por un sorteo adicional del lado.

#### EF-1.3 Simetría exacta `U<->V`

Sea

\[
\mathsf X(\pi)=\pi^{-1}.
\]

Intercambiar las dos coordenadas manda el punto de rangos `(i,pi(i))` al punto cuyo
nuevo rango `U` es `pi(i)` y cuyo nuevo rango `V` es `i`. La aplicación de puntos
`i -> pi(i)` es un isomorfismo entre los dos posets. En particular:

- induce una biyección entre sus cadenas candidatas;
- conserva por separado `m_-` y `m_+`, y por tanto conserva `S_lex`;
- conserva la existencia y unicidad del ganador `S`;
- mantiene el lado y permuta sus gaps, `(K_h,L_h)->(L_h,K_h)`.

La inversión es una biyección de `\mathfrak S_n` y preserva su medida uniforme. Se
reetiquetan los puntos mediante `i -> pi(i)`; no se conservan punto a punto sus
etiquetas numéricas de rango `U`, pero sí la posición ordenada dentro de la cadena y
la etiqueta lateral `h`. Así se obtienen, para cada lado y cada `m`, las identidades
exactas

\[
\Omega_n^h((k,l),m;S)
=\Omega_n^h((l,k),m;S),
\tag{EF1.4}
\]

\[
(K_h,L_h)\mid(M_h=m,S)
\ \overset{d}{=}\ (L_h,K_h)\mid(M_h=m,S).
\tag{EF1.5}
\]

Esta simetría obliga a cualquier tabla bidimensional posterior a ser simétrica, pero
no obliga a `K=L` en cada realización.

#### EF-1.4 Simetría exacta `PAST<->FUTURE`

Sea `rho(i)=n+1-i` y defínase la involución

\[
\mathsf R(\pi)=\rho\circ\pi\circ\rho.
\]

Geométricamente corresponde a `(U,V)->(1-U,1-V)`. La aplicación de puntos
`i -> rho(i)` invierte el orden: si `i prec_pi j`, entonces
`rho(j) prec_{R(pi)} rho(i)`. Por ello manda cada cadena candidata

\[
q=(a,b,c,d)
\quad\longmapsto\quad
q^{\mathsf R}=(\rho(d),\rho(c),\rho(b),\rho(a)).
\]

Los dos intervalos cambian de lado y conservan sus cardinalidades y sus gaps:

\[
(M_{\rm PAST},T_{\rm PAST},M_{\rm FUTURE},T_{\rm FUTURE})
(\mathsf R\pi)
=
(M_{\rm FUTURE},T_{\rm FUTURE},M_{\rm PAST},T_{\rm PAST})(\pi).
\tag{EF1.6}
\]

El score usa solo el mínimo y la suma de las dos cardinalidades, luego no cambia al
intercambiarlas. La involución induce una biyección entre candidatos, ganadores y
empates; en particular, `S(R(pi))=S(pi)`. Como también preserva la medida uniforme,
no identifica literalmente las fibras PAST y FUTURE como el mismo subconjunto de
`\mathfrak S_n`: su restricción da una biyección

\[
\mathcal F_{n,m}^{\mathrm{PAST},S}
\longleftrightarrow
\mathcal F_{n,m}^{\mathrm{FUTURE},S},
\]

que a su vez se restringe a una biyección entre las fibras de forma `(k,l)`. De la
biyección se sigue la igualdad de cardinalidades

\[
\Omega_n^{\rm PAST}((k,l),m;S)
=\Omega_n^{\rm FUTURE}((k,l),m;S),
\tag{EF1.7}
\]

y, en consecuencia,

\[
C_n^{\rm PAST}(m,r;S)=C_n^{\rm FUTURE}(m,r;S),
\qquad
\nu_{n,m}^{\rm PAST,S}=\nu_{n,m}^{\rm FUTURE,S}.
\tag{EF1.8}
\]

La simetría lateral queda así **probada**, no asumida. Desde este punto puede
suprimirse `h` en cantidades escalares si se cita (EF1.7)–(EF1.8). No se impone
ninguna otra simetría no demostrada.

#### EF-1.5 Soporte y bordes deductivos

El soporte ganador exacto es

\[
\mathcal A_n^{h,S}
:=\{(m,k,l,r):\Omega_n^h((k,l),m;S)>0,\ r=kl\}.
\tag{EF1.9}
\]

Por (EF1.4) y (EF1.7), este conjunto es invariante bajo `(k,l)->(l,k)` y es el mismo
para `PAST` y `FUTURE`.

Para obtener sus restricciones universales, fíjese un elemento del soporte. Si los
rangos de los endpoints laterales son `(alpha,beta)` y `(alpha',beta')`, hay `k-1`
rangos `U` y `l-1` rangos `V` estrictamente interiores. Al retirar los dos endpoints,
la permutación empareja una población de `n-2` rangos `U` con otra de `n-2` rangos
`V`. El número `m-2` cuenta cuántos rangos del bloque interior `U` quedan emparejados
con el bloque interior `V`. Tras identificar ambas poblaciones mediante esa biyección,
las cotas elementales de intersección dan

\[
\max\{0,k+l-n\}
\le m-2\le
\min\{k-1,l-1\}.
\tag{EF1.10}
\]

La cota superior equivale a `m-1<=k,l`; la inferior no trivial equivale a
`k+l<=n+m-2`. Además, el otro lado contiene al menos un punto interior y entre los
dos lados hay un gap estricto en cada coordenada. Sumando esos gaps a lo largo de
los rangos se obtiene `k,l<=n-4`. En conjunto, todo punto del soporte satisface

\[
n\ge6,\qquad
3\le m\le n-3,\qquad
m-1\le k,l\le n-4,
\qquad
k+l\le n+m-2,
\qquad
r=kl.
\tag{EF1.11}
\]

En particular,

\[
(m-1)^2\le r\le
\min\!\left\{(n-4)^2,
\left\lfloor\frac{(n+m-2)^2}{4}\right\rfloor\right\}.
\tag{EF1.12}
\]

No todo entero entre esos dos bordes es candidato a `r`: debe factorizarse como
`r=kl` con `(k,l)` sujeto a (EF1.11). Las cotas (EF1.10) son el soporte exacto del
conteo de celda para un par de endpoints fijado; esto se sigue también del soporte
de la ley hipergeométrica ya probada. No obstante, que una forma localmente factible
sea el **ganador único global** es una condición adicional. Por ello (EF1.11) define
un sobre necesario de `\mathcal A_n^{h,S}`, no una afirmación de que todos sus puntos
tengan `Omega>0`.

Esta distinción cierra la auditoría de bordes que puede hacerse antes de contar: decidir
qué puntos del sobre sobreviven al maximizador global equivale precisamente a decidir
la positividad de `Omega_n^h`, y no se introducirá como una «deducción» encubierta en
EF-1.

#### EF-1.6 `Q_{2,n}` en términos de `C_n^h`

Para cada estrato alcanzable, defínanse las tres sumas exactas

\[
D_{n,m}^h:=\sum_r C_n^h(m,r;S),\qquad
A_{n,m}^h:=\sum_r \sqrt r\,C_n^h(m,r;S),\qquad
B_{n,m}^h:=\sum_r r\,C_n^h(m,r;S),
\tag{EF1.13}
\]

y

\[
D_n^S:=\sum_m D_{n,m}^h.
\]

Por (EF1.7), esta última cantidad no depende del lado
y es exactamente el número de permutaciones para las que ocurre `S`. De (EF1.3),

\[
\mathbb E[Z_n\mid M_h=m,S]
=\frac{A_{n,m}^h}{(n+1)D_{n,m}^h},
\qquad
\mathbb E[Z_n^2\mid M_h=m,S]
=\frac{B_{n,m}^h}{(n+1)^2D_{n,m}^h}.
\tag{EF1.14}
\]

Por tanto,

\[
\operatorname{Var}(Z_n\mid M_h=m,S)
=\frac1{(n+1)^2}
\left[
\frac{B_{n,m}^h}{D_{n,m}^h}
-\left(\frac{A_{n,m}^h}{D_{n,m}^h}\right)^2
\right].
\tag{EF1.15}
\]

Como `P(M_h=m|S)=D_{n,m}^h/D_n^S`, la expresión agregada pedida es

\[
Q_{2,n}^h
=\frac1{(n+1)^2D_n^S}
\left[
\sum_m B_{n,m}^h
-\sum_m\frac{(A_{n,m}^h)^2}{D_{n,m}^h}
\right].
\tag{EF1.16}
\]

Las identidades laterales implican además

\[
Q_{2,n}^{\rm PAST}=Q_{2,n}^{\rm FUTURE}
\quad\text{para todo `n` admisible}.
\tag{EF1.17}
\]

Así, para decidir `Q_{2,n}` bastan `D,A,B`; no es obligatorio materializar la tabla
completa de `C`, y mucho menos la de `Omega(k,l)`, si una recurrencia posterior obtiene
directamente esas tres sumas.

#### EF-1.7 Techo de alcance y veredicto

EF-1 no decide qué valores de `r` tienen multiplicidad positiva ni obtiene una fórmula
cerrada para `C_n^h(m,r;S)`. Tampoco demuestra asintótica, concentración, convergencia
en ley, entropía límite ni un resultado positivo o negativo para `Q_{2,n}^h`. La ley
de Gauss--Kuzmin no interviene. La positividad real de las fibras y cualquier cuestión
posterior de conteo o límite quedan fuera de EF-1.

```text
EF1_VERDICT = EF1_PASS
EF1_OMEGA_NORMALIZATION = PROVED
EF1_PUSHFORWARD_BY_r = PROVED
EF1_U_V_SYMMETRY = PROVED_BY_pi_INVERSE
EF1_PAST_FUTURE_SYMMETRY = PROVED_BY_ORDER_REVERSAL
EF1_SUPPORT_ENVELOPE = PROVED
EF1_GLOBAL_WINNER_ATTAINABILITY = ENCODED_BY_OMEGA_POSITIVITY_NOT_ASSUMED
EF1_Q2_MOMENT_IDENTITY = PROVED
EF1_STATUS = COMPLETE_DEDUCTIVE
EF2_ENUMERATION_SIMULATION_CODE = NOT_AUTHORIZED_BY_EF1
```

**Gate EF-1:** cualquier implementación posterior deberá reproducir (EF1.4),
(EF1.7), (EF1.11) y (EF1.16). Una discrepancia se tratará como fallo de la
implementación o de sus convenciones hasta localizar la causa; no como ruptura
empírica de una identidad exacta.

### EF-2 — Enumeración exacta pequeña

EF-2 se ejecutó sobre todas las permutaciones de `n=6,7,8,9`, sin semillas y sin
sobrescribir ningún artefacto anterior. El ejecutor nuevo es

```text
emergencia/p1a_entropia_fibras_enumeracion_d2.py
```

Para cada permutación evalúa el selector congelado `MIN_COVERAGE_LEX`. Solo cuando el
ganador es único agrega, por lado, los campos fijados en EF-0:

```text
M, K, L, r=KL.
```

No lee magnitudes de coordenadas, no calcula duraciones continuas y no ejecuta Monte
Carlo.

#### EF-2.1 Estados exactos del selector vigente

La partición exacta obtenida es:

| `n` | `n!` | `EMPTY` | `UNIQUE` | `TIE` |
|---:|---:|---:|---:|---:|
| 6 | 720 | 719 | 1 | 0 |
| 7 | 5 040 | 5 003 | 32 | 5 |
| 8 | 40 320 | 39 429 | 677 | 214 |
| 9 | 362 880 | 344 837 | 12 220 | 5 823 |

El `EMPTY` es común a todos los scores porque depende solo de que exista alguna
cuádrupla elegible. `UNIQUE` y `TIE` sí dependen del score. Por eso el control contra
`p1a_enumeracion_exacta_d2.csv` se hizo en un canal paralelo y no imponiendo una
igualdad falsa entre selectores:

- el artefacto histórico usa `COVERAGE`, no `MIN_COVERAGE_LEX`;
- sus seis subtipos se colapsaron a `EMPTY/UNIQUE/TIE`;
- el evaluador nuevo reprodujo exactamente sus conteos en los cuatro tamaños;
- su SHA-256 permaneció
  `650ce526e1e88626ce41d8e9925d5b19fbb94c143c63714c0e51ebd9fcafd224`.

En `n=8` y `n=9`, el score lexicográfico vigente resuelve respectivamente `3` y `144`
empates que permanecían bajo `COVERAGE`. Esto es una diferencia de selector
completamente explicada, no una discrepancia con el artefacto congelado.

#### EF-2.2 Tablas exactas de fibras

Las multiplicidades no nulas producen los siguientes soportes escalares:

| `n` | valores alcanzados de `M` | valores alcanzados de `r=KL` | filas `Omega` | filas `C` |
|---:|---|---|---:|---:|
| 6 | `3` | `4` | 2 | 2 |
| 7 | `3,4` | `4,6,9` | 8 | 6 |
| 8 | `3,4,5` | `4,6,8,9,12,16` | 20 | 14 |
| 9 | `3,4,5,6` | `4,6,8,9,10,12,15,16,20,25` | 40 | 26 |

Las filas cuentan ambos lados. Las igualdades

\[
\Omega_n^h((k,l),m;S)=\Omega_n^h((l,k),m;S),
\qquad
\Omega_n^{\rm PAST}=\Omega_n^{\rm FUTURE}
\]

y la agregación exacta `Omega -> C` pasaron para toda fila no nula. Todos los puntos
observados respetaron el sobre (EF1.11). Estos soportes son resultados finitos para
`n<=9`; no se extrapolan como patrón asintótico.

El número de formas `(k,l)` con multiplicidad positiva, por lado y por estrato, es:

| `n` | formas positivas por `m` |
|---:|---|
| 6 | `m=3: 1` |
| 7 | `m=3: 3`; `m=4: 1` |
| 8 | `m=3: 6`; `m=4: 3`; `m=5: 1` |
| 9 | `m=3: 10`; `m=4: 6`; `m=5: 3`; `m=6: 1` |

La comparación del sobre entero (EF1.11) con el soporte positivo produce exactamente
los siguientes ceros de fibra. La tabla vale por separado para `PAST` y `FUTURE`,
después de verificar exhaustivamente su igualdad:

| `n` | `m` | pares necesarios `(k,l)` con `Omega=0` |
|---:|---:|---|
| 6 | 3 | ninguno |
| 7 | 3 | `(3,3)` |
| 7 | 4 | ninguno |
| 8 | 3 | `(3,4),(4,3),(4,4)` |
| 8 | 4 | `(4,4)` |
| 8 | 5 | ninguno |
| 9 | 3 | `(3,5),(4,4),(4,5),(5,3),(5,4),(5,5)` |
| 9 | 4 | `(4,5),(5,4),(5,5)` |
| 9 | 5 | `(5,5)` |
| 9 | 6 | ninguno |

Estos `0,1,4,10` ceros para `n=6,7,8,9` son hechos finito-muestrales del ganador
global. No convierten el sobre necesario en una caracterización asintótica ni sugieren
por sí solos una regla para tamaños posteriores.

#### EF-2.3 Implementación independiente y controles

El evaluador optimizado se comparó, permutación por permutación, con una segunda
implementación directa que construye todas las cuádruplas y maximiza literalmente

\[
(\min\{m_-,m_+\},m_-+m_+).
\]

La ejecución persistida original comparó estado, número de maximizadores, score y
cuádrupla única en las `720+5 040=5 760` permutaciones de `n=6,7`. La reauditoría
exhaustiva de 2026-08-15 reutilizó esa misma implementación directa, sin crear otro
script ni sobrescribir artefactos, y extendió la comparación a

\[
720+5\,040+40\,320+362\,880=408\,960
\]

permutaciones. Para cada una exigió igualdad exacta de estado, número de
maximizadores, ambos componentes del score y cuádrupla única. La ruta directa calculó
además sus propios `M,K,L`, distribución por `m`, tablas `Omega`, agregación `C` y
soporte positivo. Todo coincidió exactamente con la ruta optimizada y con los CSV
congelados; la regeneración temporal reprodujo byte a byte los cuatro artefactos y sus
SHA-256. El campo `independent_crosscheck_n=[6,7]` del resumen histórico describe la
primera ejecución y no se reescribió para simular que aquel artefacto contenía la
reauditoría posterior. Pasaron:

```text
FACTORIAL_TOTALS = PASS
STATE_PARTITIONS = PASS
LEGACY_COVERAGE_REPRODUCTION = PASS
INDEPENDENT_IMPLEMENTATION_PERSISTED_n6_n7 = PASS
INDEPENDENT_REAUDIT_n6_TO_n9 = PASS
INDEPENDENT_PERMUTATION_SIGNATURES_408960 = PASS
INDEPENDENT_M_K_L_OMEGA_C_n6_TO_n9 = PASS
OMEGA_U_V_SYMMETRY = PASS
OMEGA_PAST_FUTURE_SYMMETRY = PASS
EF1_SUPPORT_ENVELOPE = PASS
OMEGA_TO_C_AGGREGATION = PASS
```

#### EF-2.4 Artefactos nuevos

```text
emergencia/resultados/p1a_entropia_fibras_estados_exactos_d2.csv
  sha256 ce589a5eeaa6fa1606df6064c53255efc8c3c80f52cb166dee6b71aaee175293

emergencia/resultados/p1a_entropia_fibras_omega_exacta_d2.csv
  sha256 03624db88f582c2180b6064deda199fd6735651c8a21d9a8a79c2b3c5b988858

emergencia/resultados/p1a_entropia_fibras_c_exacta_d2.csv
  sha256 1f3c55582690d6bbb32f6a4e0849c51d1599c99033ab9ab9ea7d30ea9e927dd1

emergencia/resultados/p1a_entropia_fibras_resumen.json
  sha256 c97284ff7a610cf55cf2779e3653c8c89d6bd929feaf288bf30f5aead612d38e
```

Cada archivo tiene un sidecar `.sha256` separado. La prueba de regresión fija esos
cuatro hashes y verifica LF, sidecars, terminal y techo de afirmación. EF-2 no
prescribe una entropía de Shannon de los pesos normalizados `C/sum C`; no se calculó
ni se introdujo una normalización adicional. Las multiplicidades exactas ya fijan
`log Omega` en toda fibra positiva conforme a la definición de §3.

```text
EF2_STATUS = COMPLETE_EXACT_N_6_TO_9
EF2_TERMINAL = EXACT_SMALL_N_FIBER_TABLES_VALIDATED
EF2_CLAIM_CEILING = EXACT_N_6_TO_9_ONLY_NO_ASYMPTOTIC_INFERENCE
EF2_MONTE_CARLO = NOT_RUN
EF2_GAUSS_KUZMIN = NOT_USED
EF3_RECURRENCE_OR_GENERATING_FUNCTION = NOT_AUTHORIZED_BY_EF2
```

**Gate EF-2: `PASS`.** Las tablas finitas quedan disponibles como controles de una
recurrencia posterior, no como evidencia de convergencia ni como decisión de
`Q_{2,n}`.

### EF-3 — Recurrencia o función generatriz

Se buscó una descripción combinatoria que evitara enumerar `n!` permutaciones, en el
orden de prioridad fijado:

1. recurrencia directa para los momentos de `r=KL` condicionados por `(M,S)`;
2. función generatriz de `C_n^h(m,r;S)`;
3. cotas de concentración o separación sin obtener la tabla completa;
4. solo en último término, recurrencia para la ley bidimensional de `(K,L)`.

La selección global por `MIN_COVERAGE_LEX` forma parte del problema y no puede
sustituirse silenciosamente por un candidato típico o por endpoints fijados.

No se obtuvo una recurrencia cerrada para `D,A,B` ni una función generatriz de `C`:
el estado `UNIQUE` exige comparar simultáneamente todos los pares de rectángulos
admisibles. Sí se obtuvo una reducción de concentración uniforme que evita esos
conteos, y una recurrencia exacta para separar la inexistencia de candidatos del
verdadero obstáculo de unicidad.

#### EF-3.1 Recurrencia exacta para `EMPTY`

Una permutación tiene al menos una cuádrupla candidata si y solo si su subsecuencia
creciente más larga tiene longitud al menos seis. En efecto, si
`q=(a,b,c,d)` es candidata, cada uno de los dos intervalos de cardinalidad al menos
tres contiene un punto estrictamente interior; esos dos puntos, junto con
`a,b,c,d`, forman una subsecuencia creciente de longitud seis. Recíprocamente, de

\[
i_1<i_2<\cdots<i_6,
\qquad
\pi(i_1)<\pi(i_2)<\cdots<\pi(i_6),
\]

se obtiene la candidata `(i_1,i_3,i_4,i_6)`, cuyos dos intervalos contienen a
`i_2` e `i_5`, respectivamente.

Sea `f^lambda` el número de tableaux estándar de forma `lambda`. La correspondencia
de Robinson--Schensted, donde la primera fila de `lambda` es la longitud de la
subsecuencia creciente más larga, da

\[
E_n:=\#\{\pi:\mathrm{EMPTY}\}
=\sum_{\substack{\lambda\vdash n\\\lambda_1\le5}}(f^\lambda)^2.
\tag{EF3.1}
\]

La fuente primaria usada para esta entrada estándar es C. Schensted, *Longest
increasing and decreasing subsequences*, Canadian Journal of Mathematics 13 (1961),
179--191, DOI `10.4153/CJM-1961-015-3`. El recuento se evalúa sin recorrer
permutaciones mediante la recurrencia de esquinas

\[
f^\varnothing=1,
\qquad
f^\lambda=\sum_{c\in\operatorname{Corners}(\lambda)}f^{\lambda\setminus c}.
\tag{EF3.2}
\]

El verificador compara además cada `f^lambda` con la fórmula independiente de
longitudes de ganchos. Reproduce exactamente los cuatro conteos `EMPTY` de EF-2:

| `n` | `E_n` por (EF3.1)--(EF3.2) | `EMPTY` EF-2 |
|---:|---:|---:|
| 6 | 719 | 719 |
| 7 | 5 003 | 5 003 |
| 8 | 39 429 | 39 429 |
| 9 | 344 837 | 344 837 |

Esta recurrencia también muestra que `EMPTY` no puede ser el cuello asintótico. Las
formas transpuestas tienen a lo sumo cinco filas y el mismo `f^lambda`; codificar la
fila de cada entrada da `f^lambda<=5^n`, y hay a lo sumo `(n+1)^5` formas. Luego

\[
\frac{E_n}{n!}
\le \frac{(n+1)^5 25^n}{n!}
=\exp[-n\log n+O(n)].
\tag{EF3.3}
\]

Queda separado así `EMPTY` de `TIE`: RSK decide la existencia de candidatos, pero
no marca sus cardinalidades rectangulares ni cuál maximiza el score global.

#### EF-3.2 Discrepancia uniforme de rectángulos

Para intervalos deterministas `I,J` de rangos en `{1,...,n}`, defínase

\[
N_\pi(I,J)=\#\{i\in I:\pi(i)\in J\},
\qquad
\Delta_n(\pi)=
\max_{I,J}\left|
\frac{N_\pi(I,J)}n-\frac{|I||J|}{n^2}
\right|.
\tag{EF3.4}
\]

Para `I,J` fijos, `N_pi(I,J)` es hipergeométrica con media `|I||J|/n`. Se usa la
siguiente cola, rederivada aquí para no depender de la referencia no archivada que
aparecía en la antigua §13. Al revelar los `|I|` valores de `pi(I)` sin reemplazo,
el martingala de Doob de `N_pi(I,J)` tiene, en cada paso, rango condicional de
longitud a lo sumo uno. La cota elemental
`E[exp(tD)|pasado]<=exp(t^2/8)` para una diferencia centrada en un intervalo de
longitud uno, iterada y optimizada en `t`, da

\[
\Pr\{|N_\pi(I,J)-|I||J|/n|\ge u\}
\le2\exp(-2u^2/|I|)
\le2\exp(-2u^2/n).
\]

Hay menos de `n^4` pares de intervalos. La unión se toma sobre esos índices
deterministas, antes de que el selector elija endpoints; por tanto conserva toda la
dependencia inducida por `MIN_COVERAGE_LEX` y produce

\[
\Pr\{\Delta_n>\varepsilon\}
\le2n^4e^{-2n\varepsilon^2}.
\tag{EF3.5}
\]

Si ocurre `S` y el lado seleccionado tiene gaps `(K,L)` y cardinalidad `M`, su
rectángulo cerrado usa intervalos de longitudes `K+1,L+1` y contiene exactamente
`M` puntos. Además, uniformemente para `0<=K,L<=n-1`,

\[
0\le
\frac{(K+1)(L+1)}{n^2}-\frac{KL}{(n+1)^2}
\le\frac4n.
\tag{EF3.6}
\]

Por (EF3.4)--(EF3.6), sin fijar ni reemplazar al ganador global,

\[
\left|Z_n^2-\frac Mn\right|
\le\Delta_n+\frac4n.
\tag{EF3.7}
\]

#### EF-3.3 Teorema condicional y coste exacto de `S`

Escríbase `p_n=Pr_n(S)`. La esperanza condicionada minimiza el error cuadrático
entre todas las funciones de `M`; usando como competidor `g_n(M)=sqrt(M/n)` y
`(sqrt x-sqrt y)^2<=|x-y|`, (EF3.7) da

\[
Q_{2,n}
\le E[(Z_n-g_n(M))^2\mid S]
\le E[\Delta_n\mid S]+\frac4n.
\tag{EF3.8}
\]

Para todo `epsilon>0`, dividir solo después de aplicar la cota incondicional
(EF3.5) produce la desigualdad finito-muestral

\[
Q_{2,n}
\le \varepsilon+\frac4n
+\frac{2n^4e^{-2n\varepsilon^2}}{p_n}.
\tag{EF3.9}
\]

En consecuencia queda demostrado el puente exacto

\[
\boxed{\ \log(1/p_n)=o(n)\quad\Longrightarrow\quad Q_{2,n}\to0.\ }
\tag{EF3.10}
\]

La misma hipótesis da algo ligeramente más fuerte que la varianza de fibra. Como

\[
\left(\sqrt{M/n}-\sqrt{(M-2)/(n-2)}\right)^2
\le\frac{2}{n-2},
\]

el `COUNT_VOLUME` congelado tiene error cuadrático absoluto tendente a cero para
`Z_n`. Este enunciado no decide el error normalizado por la varianza total, la razón
de correlación ni el canal absoluto de duración; en particular no contradice la
advertencia de que numerador y denominador pueden colapsar juntos.

La condición entrópica no es un adorno técnico. Si a lo largo de una subsucesión
`Q_{2,n}>=q>0`, tomando `epsilon=q/4` en (EF3.9), para `n` grande se obtiene

\[
p_n\le \frac4q n^4\exp(-nq^2/8).
\tag{EF3.11}
\]

Así, una dispersión absoluta persistente solo es posible si la selección única se
vuelve exponencialmente rara. Las frecuencias finitas de EF-2 no permiten escoger
entre esas posibilidades.

#### EF-3.4 Controles finitos y obligación abierta

El ejecutable determinista, de solo lectura,

```text
emergencia/p1a_entropia_fibras_ef3.py
```

reconstruye (EF1.16) desde el artefacto `C` congelado y obtiene, idénticamente en
ambos lados,

| `n` | `Q_{2,n}` exacto desde `C` |
|---:|---:|
| 6 | 0 |
| 7 | 0.000763763970012 |
| 8 | 0.00130385353147 |
| 9 | 0.00168949426410 |

Estos cuatro valores solo controlan convenciones y la identidad de momentos; su
crecimiento inicial no se extrapola. El script también verifica la recurrencia RSK,
la fórmula de ganchos, la partición `EMPTY/UNIQUE/TIE`, la normalización de `C`, la
simetría lateral y la desigualdad de proyección (EF3.8). No escribe artefactos ni usa
semillas.

La primera obligación combinatoria que queda es ahora exacta:

\[
\text{probar }-\log\Pr_n(S)=o(n),
\quad\text{o controlar directamente }E[\Delta_n\mid S].
\tag{EF3.12}
\]

Por (EF3.3), no basta volver a contar `EMPTY`: el trabajo pendiente está en la
entropía de `UNIQUE` frente a `TIE` para el máximo global. El certificado de familia
prescrita de `P1a_puerta_teorica_en_Minkowski.md` §13 permanece `SKETCH`, fue cerrado
sin reparar por la decisión del PI y no se promociona ni se usa como premisa aquí.
Tampoco se afirma que no exista una recurrencia para `C`; se registra que RSK por sí
solo no conserva las marcas necesarias para obtenerla.

```text
EF3_RSK_EMPTY_RECURRENCE = PROVED_AND_VALIDATED_N_6_TO_9
EF3_UNIFORM_RECTANGLE_TAIL = PROVED
EF3_CONDITIONAL_Q2_BOUND = PROVED
EF3_SUBEXPONENTIAL_SELECTION_IMPLIES_FIBER_CONCENTRATION = PROVED
EF3_SELECTION_ENTROPY = OPEN
EF3_DIRECT_DAB_RECURRENCE = NOT_OBTAINED
EF3_C_GENERATING_FUNCTION = NOT_OBTAINED
EF3_TERMINAL = OPEN_AFTER_FIBER_AUDIT
EF3_CLAIM_CEILING = CONDITIONAL_ASYMPTOTIC_THEOREM_NO_UNCONDITIONAL_Q2_TERMINAL
EF3_MONTE_CARLO = NOT_RUN
EF3_GAUSS_KUZMIN = NOT_USED
```

**Gate EF-3: `PASS` como cierre honesto.** Se evita la enumeración factorial para
`EMPTY` y se reduce la asintótica de `Q_{2,n}` a (EF3.12), pero no se fuerza
`FIBER_CONCENTRATION`: falta una cota demostrada para el coste del condicionamiento
por selección única.

### EF-4 — Asintótica de `Q_{2,n}`

EF-4 cierra la obligación (EF3.12) mediante un certificado nuevo y autocontenido de
selección única. Conserva la idea válida de prescribir una banda de filas, pero no
reabre ni usa como premisa la Proposición 13.12 `SKETCH` de
`P1a_puerta_teorica_en_Minkowski.md`. En particular, la banda se define directamente
como el conjunto discreto prescrito y el caso que perdía una escalera se resuelve con
una desigualdad distinta cuyo margen es `rho/2-o(rho)`, no el margen `rho` refutado
por el comité 050.

#### EF-4.1 Familia prescrita para tamaños pares

Sea `n=2s` y fíjese, sin constantes ajustables,

\[
\rho_n=\left\lceil(n^2\log n)^{1/3}\right\rceil,
\qquad R_n=2\rho_n+2,
\qquad N_n=n-R_n.
\tag{EF4.1}
\]

Para `n` suficientemente grande, `rho_n<n/4`. Sean
`q_1=floor(n/4)` y `q_3=floor(3n/4)`. El evento `F_n` prescribe las siguientes
imágenes, en rangos uno-basados:

\[
\begin{aligned}
&\pi(1)=1,\quad \pi(s)=s,\quad
\pi(s+1)=s+1,\quad \pi(n)=n,\\
&\pi(s-\rho_n+j)=q_1+j,
&&j=1,\ldots,\rho_n-1,\\
&\pi(s+1+j)=q_3+j,
&&j=1,\ldots,\rho_n-1.
\end{aligned}
\tag{EF4.2}
\]

Las dos escaleras de (EF4.2) se denotan `B_-` y `B_+`. Todas las filas del
intervalo discreto `{s-rho_n+1,...,s+rho_n}` quedan prescritas: no se identifica
este conjunto con una banda definida por redondear una desigualdad geométrica. Las
filas y columnas prescritas son distintas para todo `n` grande, luego

\[
\Pr(F_n)=\frac1{(n)_{R_n}}.
\tag{EF4.3}
\]

Condicionado a `F_n`, la aplicación entre las `N_n` filas y columnas libres es una
biyección uniforme. En cada mitad hay exactamente `N_n/2` filas libres y `N_n/2`
columnas libres. La cuádrupla plantada

\[
q_0=((1,1),(s,s),(s+1,s+1),(n,n))
\tag{EF4.4}
\]

contiene `p_0=rho_n+1` puntos prescritos en cada lado. Si `X_-` y `X_+` son sus
conteos libres, la conservación de flujo entre las dos mitades da
`X_-=X_+` para cada completación, no solo en media. Por tanto sus dos cardinalidades
son exactamente iguales.

#### EF-4.2 Evento uniforme de discrepancia

Para conjuntos de filas y columnas libres obtenidos al intersectar intervalos de
rangos con el residual, el conteo tiene media exacta `Nuv`, donde `u,v` son sus
fracciones respecto de `N=N_n`. Aplicando la cola hipergeométrica rederivada en
EF-3 y tomando unión sobre menos de `n^4` pares de intervalos, el evento

\[
G_n=\left\{
|X(I,J)-Nuv|\le\eta_n
\text{ simultáneamente para todo }I,J
\right\},
\qquad
\eta_n=\sqrt{3N\log n},
\tag{EF4.5}
\]

satisface

\[
\Pr(G_n^c\mid F_n)
\le2n^4\exp(-2\eta_n^2/N)
=2n^{-2}.
\tag{EF4.6}
\]

La unión vuelve a hacerse sobre intervalos de índices deterministas. Por ello
(EF4.5) vale simultáneamente para los rectángulos que el selector adaptativo termine
usando.

#### EF-4.3 Lema geométrico para dos rectángulos

Para una cuádrupla rival, sean `u_-,u_+` sus fracciones libres de filas y
`v_-,v_+` las de columnas en los dos lados, y escríbase

\[
f_-=u_-v_-,\qquad f_+=u_+v_+.
\]

Los dos intervalos de filas son disjuntos, y lo mismo ocurre con los de columnas,
de modo que `u_-+u_+<=1` y `v_-+v_+<=1`. Cauchy--Schwarz da la identidad útil

\[
\sqrt{f_-}+\sqrt{f_+}
\le\sqrt{(u_-+u_+)(v_-+v_+)}\le1.
\tag{EF4.7}
\]

Fíjese

\[
\tau_n=\frac18+\frac{\rho_n}{N}.
\tag{EF4.8}
\]

Toda rival distinta de `q_0` cae en al menos uno de estos tres casos:

1. mantiene los endpoints interiores `(s,s)` y `(s+1,s+1)`;
2. `min(f_-,f_+)<=tau_n`;
3. uno de los lados no contiene ningún punto de su escalera asignada, ningún lado
   contiene la escalera contraria, el lado que pierde tiene a lo sumo tres puntos
   prescritos y el otro a lo sumo `p_0+1`.

La clasificación es exacta. Se inspecciona la fila del segundo endpoint `b`. Si
queda por debajo de la banda, el lado pasado pierde `B_-`; si queda por encima, el
futuro pierde `B_+`. Dentro de la banda toda fila está prescrita. Si `b` pertenece
a `B_-`, su rectángulo pasado usa como máximo `N/2` filas libres y menos de
`n/4+rho_n` columnas; si pertenece a `B_+`, el rectángulo futuro obedece la cota
simétrica. Lo mismo ocurre cuando el tercer endpoint `c` pertenece a `B_+`. Estos
casos satisfacen (2), pues

\[
\frac{(N/2)(n/4+\rho_n)}{N^2}
\le\frac18+\frac{\rho_n}{N}.
\tag{EF4.9}
\]

Si el rectángulo pasado contiene un punto de la escalera superior, el futuro queda
con a lo sumo media población libre de filas y aproximadamente un cuarto de las
columnas; si el futuro contiene la escalera inferior ocurre lo simétrico. Las mismas
cotas crudas de (EF4.9), con los pisos enteros solo reduciendo el soporte, vuelven a
dar (2). Excluidos esos cruces, el bloque que pierde su escalera contiene únicamente
los cuatro puntos especiales de (EF4.2); el pasado nunca puede contener `(n,n)` y
el futuro nunca puede contener `(1,1)`, de donde el tope tres. El otro bloque puede
contener su escalera de `rho_n-1` puntos y a lo sumo tres especiales, es decir
`p_0+1`. Finalmente, si `b=(s,s)`, el tercer endpoint es `(s+1,s+1)`, un punto de
`B_+` —caso (2)— o queda por encima de la banda —caso (3)—; el análisis para
`b=(s+1,s+1)` es idéntico. Esto agota las posibilidades.

#### EF-4.4 Margen correcto del caso de pérdida

En el caso (3), renómbrese `f` como el producto libre del lado que pierde. Por
(EF4.7), el producto del otro lado es a lo sumo `(1-sqrt(f))^2`. Antes del error
`eta_n`, el score primario rival está acotado por

\[
\min\left\{
3+Nf,\ p_0+1+N(1-\sqrt f)^2
\right\}.
\tag{EF4.10}
\]

La primera función crece y la segunda decrece. Su intersección ocurre en

\[
\sqrt f=\frac12+\frac{p_0-2}{2N},
\]

y por tanto (EF4.10) es a lo sumo

\[
\frac N4+\frac{p_0}{2}+2+
\frac{(p_0-2)^2}{4N}.
\tag{EF4.11}
\]

La media plantada es `N/4+p_0`. El déficit correcto es así

\[
\gamma_n^{\rm loss}
=\frac{p_0}{2}-2-\frac{(p_0-2)^2}{4N}
=\left(\frac12+o(1)\right)\rho_n.
\tag{EF4.12}
\]

Este es el factor `1/2` observado por el falsador del comité 050. No se usa la
desigualdad inválida que asignaba el producto `<=1/4` al mismo bloque que perdía una
escalera.

En el caso (2), incluso concediendo los `R_n=2p_0` puntos prescritos al bloque que
realiza el mínimo, su déficit respecto de la plantada es al menos

\[
\gamma_n^{\rm small}
=\frac N4+p_0-(2p_0+N\tau_n)
=\frac N8-2\rho_n-1.
\tag{EF4.13}
\]

En el caso (1), cambiar el endpoint exterior pasado elimina `(1,1)` de ese intervalo
y cambiar el futuro elimina `(n,n)`. Como los dos lados plantados son exactamente
iguales, cualquier cambio reduce estrictamente el mínimo al menos en una unidad,
sin usar discrepancia.

Ahora

\[
\eta_n=O(\sqrt{n\log n}),\qquad
\rho_n=\Theta(n^{2/3}(\log n)^{1/3}),
\]

por lo que `eta_n=o(rho_n)`. De (EF4.12)--(EF4.13), para todo `n` par
suficientemente grande,

\[
\gamma_n^{\rm loss}>2\eta_n,
\qquad
\gamma_n^{\rm small}>2\eta_n.
\tag{EF4.14}
\]

Sobre `F_n intersect G_n`, la plantada tiene score al menos
`N/4+p_0-eta_n`; cada rival de los casos (2)--(3) queda estrictamente por debajo por
(EF4.14), y los del caso (1) pierden deterministamente. Además sus cardinalidades
tienden a infinito, luego la plantada es admisible. Es por tanto el único
maximizador de `MIN_ONLY` y, al tener todo rival primer componente estrictamente
menor, también el único maximizador del score lexicográfico congelado. En símbolos,

\[
F_n\cap G_n\subseteq S.
\tag{EF4.15}
\]

#### EF-4.5 Coste entrópico y tamaños impares

De (EF4.3), (EF4.6) y (EF4.15), para tamaños pares grandes,

\[
\begin{aligned}
\Pr_n(S)
&\ge \frac{1-2n^{-2}}{(n)_{R_n}},\\
\log\frac1{\Pr_n(S)}
&\le R_n\log n+o(1)
=O\!\left(n^{2/3}(\log n)^{4/3}\right)
=o(n).
\end{aligned}
\tag{EF4.16}
\]

La sucesión completa se recupera sin rehacer el certificado impar. Para
`sigma in S_{n-1}`, defínase

\[
\pi(i)=\sigma(i)+1\quad(i<n),
\qquad \pi(n)=1.
\tag{EF4.17}
\]

El punto nuevo `(n,1)` es incomparable con todos los anteriores. No crea cadenas,
no altera intervalos ni scores y preserva el ganador único. La aplicación es
inyectiva, luego

\[
\Pr_n(S)\ge\frac1n\Pr_{n-1}(S).
\tag{EF4.18}
\]

Aplicando (EF4.18) a los `n` impares y (EF4.16) al tamaño par anterior,

\[
\boxed{\ \log(1/\Pr_n(S))=o(n)\ }
\tag{EF4.19}
\]

para la sucesión completa.

#### EF-4.6 Terminal para `Q_{2,n}`

Insertando (EF4.19) en (EF3.9), para cada `epsilon>0` fijo el término condicionado
es exponencialmente pequeño y

\[
\limsup_{n\to\infty}Q_{2,n}\le\varepsilon.
\]

Como `epsilon` es arbitrario,

\[
\boxed{Q_{2,n}\longrightarrow0.}
\tag{EF4.20}
\]

Por (7.7)--(7.10) de `P1a_count_volume_lema_kl_d2.md`, también
`P_{2,n}->0`. Junto con el término Beta-producto ya controlado, la predicción basada
en `M` tiene error cuadrático absoluto tendente a cero para el estimando lateral
relativo declarado. El resultado no afirma que el error normalizado por la varianza
total tienda a cero: numerador y denominador pueden colapsar juntos, y no se eleva
(EF4.20) a una afirmación sobre `rho_max`, escala absoluta, el poset completo o
`d>=3`.

El verificador determinista

```text
emergencia/p1a_entropia_fibras_ef4.py
```

comprueba la inyectividad y el balance de (EF4.2), la optimización unidimensional de
(EF4.10) y los márgenes explícitos. Como control no vinculante, el certificado con
estas constantes es todavía preasintótico en `n=10^5,10^6` y satisface (EF4.14) en
`n=10^7`; la prueba usa únicamente que los cocientes asintóticos convergen y no ese
umbral numérico. No se enumeran permutaciones, no se escriben artefactos y no se
generan semillas.

```text
EF4_CORRECTED_PRESCRIBED_FAMILY = PROVED
EF4_UNIQUE_SELECTION_ENTROPY = SUBEXPONENTIAL_PROVED_FULL_SEQUENCE
EF4_Q2_ASYMPTOTIC = Q2_TO_ZERO_PROVED
EF4_TERMINAL = FIBER_CONCENTRATION
EF4_CLAIM_CEILING = ABSOLUTE_MSE_FOR_DECLARED_RELATIVE_LATERAL_ESTIMAND
EF4_NORMALIZED_INFORMATION_RATIO = NOT_DECIDED
EF4_MONTE_CARLO = NOT_RUN
EF4_GAUSS_KUZMIN = NOT_USED
```

**Gate EF-4: `PASS`. Terminal científico: `FIBER_CONCENTRATION`.**

El argumento distingue explícitamente:

- convergencia en promedio sobre `M` frente a uniformidad en `m`;
- masa típica frente a estratos de probabilidad evanescente;
- concentración de `sqrt(KL)` frente a concentración separada de `K` y `L`;
- resultado finito-muestral frente a límite asintótico.

No se promovió una gráfica ni una tendencia para pocos valores de `n`: (EF4.20)
procede de las cotas uniformes (EF3.9) y (EF4.16).

### EF-5 — Sectores dominantes y posible escalera

Solo después de EF-2 se estudiarán las razones entre multiplicidades de sectores
vecinos y la forma de

\[
-\log C_n^h(m,r;S).
\]

Preguntas permitidas:

- ¿el sector modal de `r` cambia por saltos al variar `m` o `n`?;
- ¿existe una escala natural en la que esos cruces converjan?;
- ¿la ley condicionada es universal respecto de variantes admisibles del muestreo o
  conserva dependencia del selector?

Respuestas negativas también cierran EF-5. Quedan prohibidos el ajuste a
Gauss–Kuzmin, la búsqueda de exponentes post hoc y el lenguaje de universalidad sin
convergencia demostrada.

### EF-6 — Bibliografía, auditoría y destino

EF-6 se abrió después del terminal matemático de EF-4 y queda documentado por
separado en
`emergencia/P1a_entropia_fibras_ef6_auditoria_bibliografica.md`. La auditoría
ejecutó las tres obligaciones previstas:

1. verificó precedentes primarios en causal sets y 2-orders, estadísticos de orden,
   LIS/RSK, concentración sin reemplazo, copulas/permutones, scan statistics e
   inferencia pos-selección;
2. separó los ingredientes estándar de la contribución que depende del selector;
3. decidió conservar el resultado como nota técnica autónoma antes de cualquier
   integración en un manuscrito.

Los spacings Beta/Dirichlet, el recuento `EMPTY` por RSK, la cola hipergeométrica y
la proyección cuadrática son `STANDARD_COROLLARY`. El principio número-volumen, los
2-orders, los procesos de rangos, los escaneos adaptativos y la inferencia selectiva
son `PRECURSOR_ONLY`. El puente condicionado de EF-3 más el certificado prescrito de
unicidad de EF-4 se clasifica como `FAMILY_SPECIFIC_RESULT`.

No se encontró el teorema compuesto para `MIN_COVERAGE_LEX`, pero la búsqueda no fue
una revisión sistemática con índices y cadenas de citación completos. Por tanto:

```text
EF6_RESULT_CLASS = FAMILY_SPECIFIC_RESULT
EF6_PRIORITY_STATUS = PRIORITY_NOT_CERTIFIED
EF6_DIRECT_PRECEDENT_FOUND = NO_WITHIN_SEARCHED_CORPUS
EF6_DESTINATION = STANDALONE_TECHNICAL_NOTE_BEFORE_MANUSCRIPT_INTEGRATION
EF6_EF5_DEPENDENCY = NONE
EF6_TERMINAL = COMPLETE
```

La ausencia de un precedente encontrado no se convierte en una afirmación de
novedad. Antes de lenguaje de prioridad o de una entrega externa se requieren una
revisión independiente del certificado combinatorio y una búsqueda bibliográfica
con acceso a índices completos. EF-5 sigue siendo exploración opcional y no forma
parte de esas obligaciones.

### EF-7 — Estabilidad bajo selección subexponencial

La generalización deductiva posterior a EF-6 queda demostrada por separado en
`emergencia/P1a_estabilidad_seleccion_subexponencial_d2.md`. Separa tres capas:

1. un lema abstracto de cambio de medida que preserva concentración exponencial al
   condicionar por eventos de coste `exp[-o(n)]`;
2. un teorema para la clase de selectores adaptativos de rectángulos de rangos en
   `fixed-n`, `d=2`, con la condición adicional `order-only` solo al transferir el
   resultado a la duración continua;
3. el certificado específico de pertenencia de `MIN_COVERAGE_LEX`, formado por la
   familia prescrita, el margen de unicidad y la transferencia par–impar de EF-4.

El terminal más fuerte es `SELECTOR_CLASS_THEOREM`. Intrinsicidad, equivariancia y
unicidad no garantizan por sí solas masa subexponencial; una regla que solo actúa
sobre cadenas totales es un contraejemplo con probabilidad `1/n!`. La clasificación
bibliográfica de EF-6 no se reescribe como una afirmación de prioridad: EF-7 refina
la estructura lógica del resultado, no certifica novedad.

```text
EF7_ABSTRACT_SELECTION_THEOREM = PROVED_AS_INTERMEDIATE_LEMMA
EF7_SELECTOR_CLASS_THEOREM = PROVED
EF7_INTRINSICNESS_ALONE_SUFFICIENT = FALSE
EF7_MIN_COVERAGE_LEX_ROLE = NONTRIVIAL_MEMBERSHIP_CERTIFICATE
EF7_TERMINAL = SELECTOR_CLASS_THEOREM
EF7_EF5_DEPENDENCY = NONE
```

## 6. Papel de WP7

WP7 no forma parte de la prueba de `COUNT_VOLUME` y no se modifica en esta ruta. Su
único papel permitido es motivacional:

> una población subextensiva puede ser casi invisible para un control volumétrico y,
> sin embargo, dominar un observable extremal de cadena.

Esta analogía no implica que la entropía de fibras explique la cadena plantada ni que
F2/F3 determine el comportamiento de `Z_n`. Los dos resultados deben permanecer
lógica y documentalmente separados.

## 7. Separación exploración–confirmación

Esta ruta comienza como matemática deductiva y enumeración exacta de desarrollo.

```text
EF-0 / EF-1: deducción y contrato
EF-2: enumeración exacta de desarrollo, sin semillas
EF-3 / EF-4: combinatoria y asintótica
EF-5: diagnóstico posterior opcional, nunca ajuste
EF-6: auditoría bibliográfica y decisión de destino, completado
EF-7: generalización deductiva a una clase de selectores, completado
```

Una simulación Monte Carlo solo podrá abrirse si EF-3 demuestra que la enumeración
exacta no alcanza el régimen necesario y si antes existe un contrato específico. En ese
caso:

- usará semillas nuevas de desarrollo, fuera de toda banda reservada;
- no reutilizará validación previa para elegir umbrales;
- no tocará la banda virgen `[2,000,000–2,999,999]`;
- no convertirá un piloto en confirmación.

Esta hoja no autoriza una validación ciega ni una nueva pre-registración.

## 8. Alcance negativo

Queda fuera de esta hoja:

- reconstrucción o localización de horizontes;
- escala temporal absoluta y el canal Poisson con densidad conocida;
- `d>=3`;
- nuevos selectores u observables elegidos después de ver resultados;
- cambios en `MIN_COVERAGE_LEX`;
- reapertura de `HEIGHT_ONLY`, `HEIGHT_WIDTH` o cocientes cerrados;
- modificaciones de WP7, del manuscrito de límites o de resultados sellados;
- semillas de validación, hidden embedding o ground truth como entrada;
- afirmaciones de entropía gravitatoria, universalidad o prioridad absoluta.

Una obstrucción para funciones de `M` no será presentada como no-go para el poset
completo ni para `Orden + Número`.

## 9. Criterio de terminado de agosto

La unidad de agosto se considerará cerrada cuando se cumpla una de estas dos rutas:

1. **Cierre fuerte:** EF-0–EF-4 producen uno de los tres primeros terminales de §4,
   con demostración o certificado finito reproducible y techo de afirmación explícito.
2. **Cierre honesto:** EF-0–EF-3 aíslan la primera obligación combinatoria que impide
   decidir la asintótica y terminan en `EXACT_FINITE_N_ONLY` u
   `OPEN_AFTER_FIBER_AUDIT`.

EF-5, EF-6 y EF-7 no pueden retrasar artificialmente el cierre del problema
principal.

EF-4 satisface la primera ruta: el certificado (EF4.1)--(EF4.19) cierra la obligación
entrópica aislada por EF-3 y (EF4.20) produce `FIBER_CONCENTRATION`. El cierre es
fuerte para el funcional absoluto fijado en EF-0; no decide la razón de información
normalizada ni amplía el alcance negativo de §8.

## 10. Estado de los gates EF-0--EF-4, EF-6 y EF-7

EF-0 queda redactado en §5 y revisado documentalmente contra
`emergencia/P1a_count_volume_experimento_condicionado_d2.md`,
`emergencia/P1a_count_volume_ley_condicionada_d2.md` y
`emergencia/P1a_count_volume_lema_kl_d2.md`. La revisión fija la medida sobre
permutaciones, la fibra por `M`, los gaps laterales, la ley condicionada y el
funcional agregado sin elevar ninguno de los resultados abiertos.

EF-1 queda cerrado deductivamente en §5: normalización de `Omega`, `pushforward` por
`r`, simetrías de coordenadas y lados, sobre necesario del soporte ganador e identidad
de momentos para `Q_{2,n}`. La positividad de `Omega` dentro del sobre no se supone:
permanece como la obligación combinatoria global que deberá abordar el trabajo
posterior.

EF-2 queda cerrado para `n=6,...,9`: enumeración exhaustiva, control del artefacto
histórico, doble implementación en `n=6,7`, tablas exactas de `Omega` y `C`, simetrías
y sidecars verificados. El resultado es exclusivamente finito-muestral y no decide
ningún terminal asintótico.

EF-3 queda cerrado como reducción condicional: la recurrencia RSK cuenta `EMPTY` sin
enumeración factorial y reproduce EF-2; la discrepancia uniforme entrega (EF3.9) y
demuestra que `-log Pr(S)=o(n)` bastaría para `Q_{2,n}->0`. No se ha demostrado esa
cota dentro de EF-3, no se usa el certificado `SKETCH` de la antigua §13 y no se
decide allí incondicionalmente ningún terminal asintótico.

EF-4 cierra la obligación de EF-3 con una familia prescrita discreta y una prueba
nueva del margen `rho/2-o(rho)`. Obtiene `-log Pr(S)=o(n)` para tamaños pares y lo
transfiere a impares mediante un punto incomparable; combinado con (EF3.9), demuestra
`Q_{2,n}->0` sobre la sucesión completa. El terminal es `FIBER_CONCENTRATION`, con el
techo explícito de error cuadrático absoluto para el estimando lateral relativo.

EF-6 queda cerrado como auditoría bibliográfica con fecha de corte 2026-08-12. No
encuentra un precedente directo en el corpus revisado, clasifica el contenido como
`FAMILY_SPECIFIC_RESULT` y mantiene cualquier afirmación de prioridad en
`PRIORITY_NOT_CERTIFIED`. Decide nota técnica autónoma antes de integración y no abre
EF-5, Gauss--Kuzmin ni una búsqueda de patrones nuevos.

EF-7 queda cerrado deductivamente con `SELECTOR_CLASS_THEOREM`. El coste del
condicionamiento y la discrepancia uniforme se abstraen de `MIN_COVERAGE_LEX`; para
todo selector de intervalos con `-log Pr(S_n)=o(n)` se obtiene concentración de
`Z_n`, y para la subclase `order-only` se obtiene consistencia absoluta de
`COUNT_VOLUME` para la duración relativa. El score congelado solo reaparece al
certificar que su evento de éxito pertenece a esa clase. No se abre `d>=3`.

## 11. Autorización y parada tras EF-7

```text
LINE_STATUS_2026_08_12: EF-4 FIBER_CONCENTRATION; EF-6 Y EF-7 COMPLETADOS
AUTORISED_TODAY: EF-7; EF-5 Y d>=3 NO ABIERTOS
EXECUTED_TODAY: generalización deductiva a clase de selectores; ningún Monte Carlo
EF0_STATUS: COMPLETE_DOCUMENTARY
EF1_STATUS: COMPLETE_DEDUCTIVE
EF2_STATUS: COMPLETE_EXACT_N_6_TO_9
EF3_STATUS: COMPLETE_REDUCTION_OPEN_SELECTION_ENTROPY
EF4_STATUS: COMPLETE_ASYMPTOTIC
EF4_TERMINAL: FIBER_CONCENTRATION
EF5_STATUS: OPTIONAL_NOT_RUN
EF6_STATUS: COMPLETE_BIBLIOGRAPHIC_AUDIT
EF6_RESULT_CLASS: FAMILY_SPECIFIC_RESULT
EF6_PRIORITY_STATUS: PRIORITY_NOT_CERTIFIED
EF6_DESTINATION: STANDALONE_TECHNICAL_NOTE_BEFORE_MANUSCRIPT_INTEGRATION
EF7_STATUS: COMPLETE_DEDUCTIVE_GENERALIZATION
EF7_TERMINAL: SELECTOR_CLASS_THEOREM
NEXT_ENTRYPOINT: auditoría matemática externa o criterios de pertenencia más amplios
PROGRAM_CLOSURE: no revocado
P5_2_AND_WP7: preservados; no modificados
SEAL_AND_RESERVED_SEEDS: intactos
```
