# Sector de protocolos lentos y respuesta conservada

Fecha: 2026-10-02. Estado: `DRAFT / ANALYTICAL_PROPOSAL`.
Base: `main @ d5567eb`. Desarrollo autorizado por el usuario tras discutir
qué conservar además de la llegada. Sin revisión independiente ni promoción
al contrato físico. Las demostraciones son algebraicas, sin código ejecutado.

## 1. Alcance y cambio explícito de blanco

Se propone conservar el operador de respuesta accesible a fuentes y detectores
que varían lentamente en el reloj de actualizaciones. La primera llegada tau
queda como diagnóstico adicional. Esto amplía expresamente el blanco de un
único escalar del contrato histórico; no modifica ese documento ni afirma
haber satisfecho su gate físico.

Se parte de un poset finito marcado `(C;s,d)`, su matriz de cobertura A y
la dinámica `B=alpha A` de `DEFINITION_REPAIR_2026-10-02.md`.
Para esta nota se mantiene fijo C y alpha mientras crece la ventana T.
No es el límite conjunto de posets crecientes del documento IR operativo.

## 2. Fuentes, detector y respuesta retardada

En la ventana k=0,...,T-1 se declara la inyección

`x(0)=f(0)e_s`,
`x(k)=B x(k-1)+f(k)e_s` para k>=1,
`y(k)=e_d^dagger x(k)`.

Por iteración,

`y(t)=sum_{u=0}^t R(t-u) f(u)`,
`R(l)=e_d^dagger B^l e_s` para l>=0.

Así `K_T(t,u)=R(t-u)` si t>=u, y cero si t<u. Esta
convención incluye la respuesta al impulso de los documentos anteriores:
f(0)=1 y f(k)=0 para k>0. Las marcas son distintas, por lo que R(0)=0.
Como B es nilpotente, R tiene soporte finito para cada C fijo.

Una segunda derivación usa superposición: cada inyección en u contribuye
`B^(t-u)e_s f(u)` en t>=u; la suma da exactamente la misma matriz.
Los protocolos pueden ser complejos para tratar fase; con entradas y
salidas reales, se restringen las mismas fórmulas a espacios reales.

## 3. Sector lento común

La norma de protocolos es la euclídea en C^T. Sea

`(D_T f)(k)=f(k+1)-f(k)`, k=0,...,T-2,
`L_T=D_T^dagger D_T`,
`epsilon_T=T^(-1/2)`,
`P_T=1_[0,epsilon_T^2](L_T)`, `S_T=ran P_T`.

Para T=1, D_T es el operador vacío y P_T=I. La elección de corte
es parte de esta propuesta, común a todas las dinámicas; no se ajusta
tras comparar sus respuestas. No utiliza coordenadas del embedding.
El reloj y las marcas siguen siendo datos declarados del modelo.

Para f en S_T, el teorema espectral da

`||D_T f||^2=<f,L_T f> <= epsilon_T^2 ||f||^2`.

La lentitud se mide en diferencias internas a la ventana. No controla
el salto al encender o apagar el protocolo fuera de ella. Si se exige
una preparación suave fuera de la ventana, hay que declarar otra
condición de borde y volver a comprobar el ejemplo de esta nota.

Segunda vía: los autovectores de L_T son proporcionales a
`cos(pi j (k+1/2)/T)`, j=0,...,T-1, con autovalores
`lambda_j=4 sin^2(pi j/(2T))`.
Sustituir en las filas interiores y en los dos extremos de L_T verifica
la fórmula. Para T>=2, el número de modos conservados es

`rank P_T = 1+floor((2T/pi) arcsin(1/(2 sqrt(T))))`.

Por tanto `rank P_T ~ sqrt(T)/pi`, mientras `rank P_T/T -> 0`.
Se conservan modos cada vez más numerosos, con frecuencia por actualización
cada vez menor. La constante pertenece siempre al sector. Este control
define protocolos lentos, sin atribuir energía física a L_T.

## 4. Información conservada y suficiencia exacta

Defínase, como operador sobre S_T,

`G_T=(P_T K_T P_T)|_{S_T}`.

Para toda fuente f y todo perfil de lectura g en S_T,

`<g,K_T f>=<g,G_T f>`.

La identidad sigue de P_T f=f, P_T g=g y P_T=P_T^dagger.
Conserva exactamente todas las lecturas lineales de esos protocolos:
amplitud, signo o fase y la dependencia temporal que detectan sus modos.
No reconstruye necesariamente la historia completa del impulso ni tau.

Esta representación es única para tales lecturas. Si H actúa sobre S_T
y reproduce todas las mismas formas bilineales, entonces
`<g,(H-G_T)f>=0` para todo f,g en S_T; tomando g=(H-G_T)f
se obtiene H=G_T. Equivalentemente, las lecturas sobre pares de vectores
de una base de S_T determinan todas las entradas de G_T.
Ésta es una suficiencia operacional exacta, sin afirmar minimalidad de
una codificación numérica ni suficiencia para mediciones no lineales.

## 5. Comparación verificable entre dinámicas

Sobre la misma entrada, ventana, normas y proyector, sea

`Delta_T=||G_1,T-G_2,T||_op`.

Por dualidad de la norma euclídea,

`Delta_T=sup_{f,g in S_T; ||f||=||g||=1}
 |<g,(K_1,T-K_2,T)f>|`.

La cota superior es Cauchy–Schwarz. Para la igualdad se elige un vector
singular derecho de la diferencia y el correspondiente vector izquierdo;
si la diferencia es cero, ambos lados son cero.
Así Delta_T mide la mayor discrepancia de lectura permitida. No se
presupone igualdad ni convergencia de G_T por definir el sector.

Se fija aquí normalización de amplitud igual a uno para ambas dinámicas,
y protocolos de norma uno. No se divide cada respuesta por su propia
masa ni se introduce un factor decreciente para hacer desaparecer Delta_T.
En una futura familia creciente habrá que declarar normalización común
y una respuesta límite no nula antes de examinar los resultados.

## 6. Misma llegada, diferencia que permanece en el sector lento

Úsese el poset con cadenas saturadas `s-a-d` y `s-b-c-d`,
sin otras coberturas, de §12 del documento IR operativo.
Con alpha_1=1, alpha_2=3/4 y theta=1/2:

`R_1(2)=1`, `R_1(3)=1`,
`R_2(2)=9/16`, `R_2(3)=27/64`,
`tau_1=tau_2=2`.

Para T>=4, sean f=g el vector constante de entradas 1/sqrt(T).
Tiene norma uno y pertenece a S_T. Contando las T-l entradas de cada
diagonal retardada de K_T se obtiene exactamente

`<g,(G_1,T-G_2,T)f>
 = (7/16)(T-2)/T + (37/64)(T-3)/T
 = 65/64 - 167/(64T)`.

Segunda comprobación: para cada t la salida constante es
`T^(-1/2) sum_{l<=t} R(l)`; sumar la lectura en t cuenta cada
retardo l exactamente T-l veces y reproduce la fórmula.
En particular,

`liminf_{T->infinity} Delta_T >= 65/64`.

El sector lento distingue estas dos dinámicas aunque tau coincida.
El límite de la lectura coincide con la diferencia de respuestas de
frecuencia cero: `2-63/64=65/64`. Esto prueba no trivialidad de la
comparación y la insuficiencia de tau para estas lecturas. No establece
convergencia de operadores entre espacios de dimensión creciente.

Control de borde: T=4 da 93/256, positivo; la corrección finita se
anula al crecer T con el poset fijo. El impulso puntual usado para
definir tau no es, en general, un protocolo del sector lento.

## 7. Causalidad y obligaciones físicas pendientes

K_T es retardado por definición. P_T mezcla tiempos de toda la ventana;
el soporte de P_T K_T P_T no define un cono causal ni una primera llegada.
La lectura con g se interpreta como procesamiento de un registro completo,
disponible después de adquirir la ventana, no como detector instantáneo.
La preparación de f es un protocolo temporal distribuido.

La propuesta no produce un subespacio lento invariante de estados de B.
Todos los autovalores de B son cero, lo que no suministra una separación
de energías. Faltan una interpretación física del reloj, la familia de
refinamiento, la identificación entre espacios y una aproximación dinámica
controlada en esa familia. El límite T->infinity con C fijo no cubre esas
obligaciones ni se intercambia con un límite C_n creciente.

El antecedente QCA se comprobó en la fuente primaria local
`/home/ignac/qca-causal-cones/biblioteca/1312.2852v1.pdf`, p.3,
Farrelly–Short, Ecs.12–16, https://arxiv.org/abs/1312.2852.
Allí el sector se define por momento y se controla la diferencia de
evoluciones mediante una cota y un escalado conjunto. Ese resultado
no se aplica a este B: sirve para precisar las obligaciones aún abiertas.
Las identidades de §§2–6 se derivan aquí de las definiciones declaradas;
los documentos del atlas no se usan como prueba de ellas.

```text
SLOW_PROTOCOL_SECTOR = DEFINED
LINEAR_SLOW_READOUT_SUFFICIENCY = PROVED_ALGEBRAICALLY
ARRIVAL_SUFFICIENCY_FOR_THOSE_READOUTS = REFUTED_IN_FINITE_EXAMPLE
GROWING_POSET_RESPONSE_LIMIT = OPEN
PHYSICAL_LOW_ENERGY_SECTOR = OPEN
INDEPENDENT_REVIEW = NOT_PERFORMED
```

La unidad termina con esta definición y el contraejemplo. Antes de buscar
un límite físico debe fijarse una única familia, su reloj, la escala de
ventana y la normalización común, con un criterio de respuesta no trivial.

## 8. Continuación: familia creciente fijada

`GROWING_FAMILY_RESPONSE_2026-10-02.md` fija, a petición del usuario,
el refinamiento de las dos rutas, reloj k/n, ventana 4n y normalización
común. Identifica los protocolos en L2([0,4)) y deriva un límite fuerte
no nulo de respuesta. La distinción entre las dinámicas persiste.
Es un límite diferente al de §6, que mantiene fijo el poset, y no cierra
la interpretación física ni la definición de un sector de energía.
