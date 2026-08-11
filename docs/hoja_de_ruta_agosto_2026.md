# Hoja de ruta — agosto de 2026
## Entropía de fibras y ley condicionada de `COUNT_VOLUME`

```text
ESTADO: HOJA DE RUTA AUTORIZADA COMO PRÓXIMO TRABAJO
FECHA: 2026-08-11
LÍNEA: emergencia / identificabilidad del tiempo métrico
OBJETO: ley condicionada de Z_n = sqrt(KL)/(n+1)
CANAL: fixed-n, d=2, poset no etiquetado + conteos internos
HOY: solo documento; cero simulaciones, cero semillas, cero cambios de resultados
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

Las clases de formas con el mismo producto dan la partición

\[
C_n^h(m,r;S)
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
obtienen, para cada lado y cada `m`, las identidades exactas

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

```text
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

#### EF-2.3 Implementación independiente y controles

El evaluador optimizado se comparó, permutación por permutación, con una segunda
implementación directa que construye todas las cuádruplas y maximiza literalmente

\[
(\min\{m_-,m_+\},m_-+m_+).
\]

La igualdad de estado, número de maximizadores, score y cuádrupla única pasó en las
`720+5 040=5 760` permutaciones de `n=6,7`. También pasaron:

```text
FACTORIAL_TOTALS = PASS
STATE_PARTITIONS = PASS
LEGACY_COVERAGE_REPRODUCTION = PASS
INDEPENDENT_IMPLEMENTATION_n6_n7 = PASS
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
cuatro hashes y verifica LF, sidecars, terminal y techo de afirmación.

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

Buscar una descripción combinatoria que evite enumerar `n!` permutaciones. Prioridad:

1. recurrencia directa para los momentos de `r=KL` condicionados por `(M,S)`;
2. función generatriz de `C_n^h(m,r;S)`;
3. cotas de concentración o separación sin obtener la tabla completa;
4. solo en último término, recurrencia para la ley bidimensional de `(K,L)`.

La selección global por `MIN_COVERAGE_LEX` forma parte del problema y no puede
sustituirse silenciosamente por un candidato típico o por endpoints fijados.

### EF-4 — Asintótica de `Q_{2,n}`

Con la maquinaria de EF-1–EF-3, intentar uno de los terminales de §4. Todo argumento
deberá distinguir:

- convergencia en promedio sobre `M` frente a uniformidad en `m`;
- masa típica frente a estratos de probabilidad evanescente;
- concentración de `sqrt(KL)` frente a concentración separada de `K` y `L`;
- resultado finito-muestral frente a límite asintótico.

No se promoverá una gráfica o una tendencia para pocos valores de `n` a teorema
asintótico.

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

Solo después de obtener un terminal matemático:

1. auditar precedentes en permutaciones aleatorias, estadísticos de orden,
   combinatoria enumerativa y sesgo por selección;
2. clasificar el resultado como `STANDARD_COROLLARY`, `PRECURSOR_ONLY`,
   `FAMILY_SPECIFIC_RESULT` o `PRIORITY_NOT_CERTIFIED`;
3. decidir mediante una nota separada si el resultado merece integrarse en un texto,
   permanecer como nota técnica o cerrarse sin publicación.

La ausencia de un precedente encontrado no certifica novedad.

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
EF-5: diagnóstico posterior, nunca ajuste
EF-6: auditoría bibliográfica y decisión de destino
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

EF-5 y EF-6 no pueden retrasar artificialmente el cierre del problema principal.

## 10. Estado de los gates EF-0, EF-1 y EF-2

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

No se ha ejecutado EF-3. Toda reentrada posterior deberá partir de las tablas y
controles de EF-2 y necesitará autorización separada para buscar una recurrencia,
función generatriz o cota asintótica.

## 11. Autorización y parada tras EF-2

```text
LINE_STATUS_2026_08_11: EF-2 COMPLETADO PARA n=6,...,9; LÍNEA ASINTÓTICA NO ABIERTA
AUTORISED_TODAY: EF-2 Y SOLO EF-2
EXECUTED_TODAY: enumerador nuevo, pruebas, tablas exactas Omega/C y sidecars; ningún Monte Carlo
EF0_STATUS: COMPLETE_DOCUMENTARY
EF1_STATUS: COMPLETE_DEDUCTIVE
EF2_STATUS: COMPLETE_EXACT_N_6_TO_9
NEXT_ENTRYPOINT: EF-3, NO AUTORIZADO EN ESTA SESIÓN
PROGRAM_CLOSURE: no revocado
P5_2_AND_WP7: preservados; no modificados
SEAL_AND_RESERVED_SEEDS: intactos
```
