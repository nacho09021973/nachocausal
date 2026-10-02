# Familia creciente, reloj y normalización de la respuesta

Fecha: 2026-10-02. Estado: `DRAFT / ANALYTICAL_MODEL`.
Base: `main @ d5567eb`. Continuación de `SLOW_PROTOCOL_RESPONSE_2026-10-02.md`.
Encargo: fijar familia creciente, reloj, ventana y normalización común.
Construcción explícita y derivaciones algebraicas; sin ejecución numérica
ni revisión independiente. No es una preinscripción confirmatoria.

## 1. Elecciones fijadas para esta construcción

| Objeto | Elección común |
| --- | --- |
| Familia C_n | Dos cadenas saturadas de 2n y 3n coberturas, con extremos comunes |
| Marcas | Fuente s y detector d, parte de la entrada |
| Reloj | t=k/n; una actualización dura 1/n en unidades operativas |
| Ventana | T_n=4n muestras k=0,...,4n-1; intervalo macroscópico [0,4) |
| Sector | P_n=1_[0,1/(4n)](D_(4n)^dagger D_(4n)) |
| Recursos | Norma euclídea uno para fuente y perfil de lectura discretos |
| Amplitud | Factor de normalización de la respuesta a_n=1 |
| Espacio común | H=L^2([0,4),dt), con interpolación isométrica E_n |
| Comparación | gamma_1=0 y gamma_2=log(4/3), constantes en n |
| Dinámica | B_(gamma,n)=exp(-gamma/n) A_n |
| Llegada auxiliar | Umbral theta=1/2 sobre la respuesta a impulso unitario |

Se elige esta familia para refinar exactamente el ejemplo finito anterior,
sin multiplicar el número de rutas. Es un modelo analítico de dos rutas;
no se postula que represente un sprinkling ni una geometría lorentziana.
La ventana 4 deja tiempo de observación después del retardo máximo 3.
Estas elecciones pertenecen a la construcción y no se presentan como
selección ciega respecto del contraejemplo que la motivó.

## 2. Familia y regla dinámica

Para cada entero n>=1, se toman dos cadenas con 2n y 3n aristas dirigidas
respectivamente; sólo comparten s y d. El orden es su clausura transitiva.
Los elementos interiores de ramas distintas son incomparables. Entonces

`N_n=5n`, `H_n=3n`, `L_n={2n,3n}`.

Aquí H_n es la longitud máxima de cadena saturada entre las marcas, y L_n
el conjunto de longitudes posibles. Para n=1 se recuperan los cinco eventos.
Si m=rn, C_m se obtiene subdividiendo cada cobertura de C_n en r coberturas.
No se necesita suponer inclusiones canónicas para n consecutivos.

El valor n es recuperable dentro de esta familia por N_n/5 o H_n/3.
El reloj t=k/n sigue siendo una elección de unidad operativa: esa fórmula
no demuestra que sea tiempo propio ni reconstruye una escala física absoluta.
Las etiquetas de los eventos no intervienen; un isomorfismo marcado
conjuga A_n y deja la respuesta fuente-detector invariante.

Para gamma>=0 se conserva la regla de inyección de la nota anterior:

`x(0)=f(0)e_s`,
`x(k)=B_(gamma,n)x(k-1)+f(k)e_s`,
`y(k)=e_d^dagger x(k)`.

Hay un único camino de cada longitud, por lo que la respuesta al impulso es

`R_(gamma,n)(l)=exp(-2gamma) 1_{l=2n}
                 +exp(-3gamma) 1_{l=3n}`.

Verificación por otra vía: cada ruta multiplica el factor exp(-gamma/n)
tantas veces como coberturas tiene, dando exp(-2gamma) y exp(-3gamma).
Bajo subdivisión m=rn, r factores exp(-gamma/m) reproducen exp(-gamma/n).
La ley de atenuación es así compatible con el refinamiento declarado.

Escalar alpha con n es parte de la dinámica: mantener alpha=3/4 fijo
haría tender ambas amplitudes a cero. No se corrige ese efecto dividiendo
posteriormente por una amplitud medida.

## 3. Ventana, recursos y unidades de la respuesta

En C^(4n), K_(gamma,n) es la matriz retardada

`(K_(gamma,n) f)(k)=exp(-2gamma) f(k-2n)
                    +exp(-3gamma) f(k-3n)`,

con f(j)=0 para j<0. No se usan índices fuera de la ventana por el futuro.
Los perfiles f y g tienen norma euclídea uno y se lee <g,Kf>.

Para comparar diferentes n, defínase

`(E_n f)(t)=sqrt(n) f(k)` para t en [k/n,(k+1)/n),
`(E_n^* h)(k)=sqrt(n) integral_[k/n,(k+1)/n) h(t) dt`.

Entonces E_n^*E_n=I y ||E_n f||_(L2)=||f||_2.
Q_n=E_n E_n^* es el promedio ortogonal por celdas. Así se fija un recurso
integrado común: una fuente macroscópica constante de norma uno tiene
amplitud 1/2, y su versión discreta tiene entradas 1/sqrt(4n).
El factor sqrt(n) convierte unidades de protocolos; la respuesta no recibe
ninguna normalización dependiente de gamma, de su masa ni de su máximo.

Equivalentemente, la medida de respuesta sobre retardos es exactamente

`mu_gamma=exp(-2gamma) delta_2 + exp(-3gamma) delta_3`.

No se identifica R con una densidad regular ni se añade un factor 1/n
a sus masas: la identidad isométrica del apartado siguiente fija esta
convención sin ambigüedad. El impulso unitario que define tau es otro
protocolo y no tiene un límite de norma uno como función delta en L2.

## 4. Operador macroscópico y transferencia exacta

Sobre H, con extensión por cero a tiempos negativos, defínase

`(K_gamma h)(t)=exp(-2gamma) h(t-2) 1_{t>=2}
                +exp(-3gamma) h(t-3) 1_{t>=3}`.

Los desplazamientos son contracciones; por la desigualdad triangular,
`||K_gamma|| <= exp(-2gamma)+exp(-3gamma) <= 2`.
Como los retardos 2 y 3 son múltiplos exactos de 1/n,

`K_gamma E_n = E_n K_(gamma,n)`.

Se verifica celda a celda: t en la celda k implica que t-2 y t-3
están en las celdas k-2n y k-3n, respectivamente. Es una transferencia
exacta para funciones constantes por celdas; el error posterior procede
de restringir los protocolos, no de aproximar la regla de retardo.

## 5. Sector lento y sentido del límite

Se mantiene sin reajuste la regla epsilon_T=T^(-1/2) de la nota anterior.
Con T=4n, los modos discretos son cos(pi j(k+1/2)/(4n)), con

`lambda_(j,n)=4 sin^2(pi j/(8n))`,
`rank P_n = 1+floor((8n/pi) arcsin(1/(4 sqrt(n))))
          ~ 2 sqrt(n)/pi`.

Todo f en ran P_n satisface `||D_(4n) f|| <= (4n)^(-1/2)||f||`.
En el reloj macroscópico, la frecuencia angular del modo j es pi j/4;
el corte crece aproximadamente como sqrt(n)/2, frente a una escala
microscópica de orden n. Cada frecuencia macroscópica fija entra finalmente
en el sector. Por ello éste no es una banda física fija de baja energía.
La lentitud se refiere a variación por actualización y conserva la misma
convención de bordes: no controla encendido y apagado fuera de la ventana.

Sobre el espacio común H sean

`Pi_n=E_n P_n E_n^*`,
`G_(gamma,n)=P_n K_(gamma,n) P_n`,
`Ghat_(gamma,n)=E_n G_(gamma,n) E_n^*`.

Pi_n es un proyector ortogonal y Pi_n -> I fuertemente. Para comprobarlo,
considérese la base coseno normalizada de L2([0,4)): phi_0=1/2 y
phi_j(t)=cos(pi j t/4)/sqrt(2), j>=1. Para j fijo y n suficientemente
grande, su versión discreta muestreada en los centros de celda está
retenida por P_n. Su interpolación isométrica converge en L2 a phi_j,
por continuidad de phi_j. La distancia de phi_j a ran Pi_n tiende a cero.
Por densidad de las combinaciones finitas de esa base y ||Pi_n||<=1,
la convergencia se extiende a todo h en H. Esta prueba no exige que los
subespacios sean anidados.

La transferencia exacta implica

`Ghat_(gamma,n)=Pi_n K_gamma Pi_n`.

Para cada h fijo,

`||Ghat_(gamma,n)h-K_gamma h||
 <= ||K_gamma|| ||Pi_n h-h|| + ||(Pi_n-I)K_gamma h|| -> 0`.

Se obtiene convergencia fuerte de la respuesta comprimida a K_gamma.
Consecuentemente convergen las lecturas de cualquier par fijo h,q en H.
No se afirma convergencia en norma de operador ni uniformidad sobre
protocolos que cambian arbitrariamente con n. La suficiencia exacta entre
protocolos retenidos sigue siendo válida a cada n finito.

## 6. Comprobación de respuesta no trivial y misma llegada

Con gamma_1=0 y gamma_2=log(4/3), las dos parejas de amplitudes son
`(1,1)` y `(9/16,27/64)`, para todo n. Con theta=1/2 ambas llegan en
`tau_n=2n`, o `tau_n/n=2` en el reloj declarado.

El perfil constante c_n(k)=1/sqrt(4n) está retenido exactamente y tiene
norma uno. Contar las diagonales retardadas da

`<c_n,G_(gamma,n)c_n>
 = (1-2n/(4n)) exp(-2gamma) + (1-3n/(4n)) exp(-3gamma)
 = exp(-2gamma)/2 + exp(-3gamma)/4`.

Por tanto las lecturas son 3/4 y 99/256, con diferencia **93/256**,
independiente de n. En particular,

`||G_(gamma_1,n)-G_(gamma_2,n)|| >= 93/256 > 0`.

Segunda comprobación: E_n c_n es exactamente h(t)=1/2. Integrando
<h,K_gamma h> sobre los tramos [2,4) y [3,4) se obtiene
exp(-2gamma)/2+exp(-3gamma)/4. Esto verifica simultáneamente las unidades,
la ventana y la ausencia de desaparición de la respuesta.

La lectura de cada dinámica es positiva y su norma está acotada por 2.
El caso n=1 reproduce la ventana T=4 del ejemplo previo, incluida la
diferencia 93/256. Esta constante difiere del 65/64 de aquella nota porque
allí la ventana crecía con el poset fijo; aquí el cociente ventana/retardo
permanece fijo. Son límites distintos y sus factores de borde son explícitos.

## 7. Resultado acotado y cierre de esta unidad

Quedan definidos familia, reloj, ventana, recurso y normalización común,
y se obtiene un operador límite retardado no nulo con una prueba de
convergencia fuerte. La igualdad de llegada normalizada no determina
su respuesta lineal lenta en esta familia. No se obtiene igualdad IR
de ambas dinámicas: el test de igualdad de respuesta falla explícitamente.

El soporte de Pi_n K_gamma Pi_n no se usa para inferir causalidad:
Pi_n mezcla tiempos; el operador retardado previo a la proyección es K_gamma.
Siguen abiertos el origen físico de la regla, la interpretación del reloj,
un sector de energía de estados y una frontera intrínseca no tautológica.
No se deduce invariancia Lorentz, velocidad física ni reconstrucción geométrica.

```text
GROWING_FAMILY = FIXED_TWO_ROUTE_SUBDIVISION
CLOCK_WINDOW_COMMON_NORMALIZATION = DEFINED
COMMON_RESPONSE_SPACE = L2_0_4
RESPONSE_TRANSFER = EXACT_ON_CELL_SUBSPACES
COMPRESSED_RESPONSE_LIMIT = STRONG_NONZERO_LIMIT_DERIVED
EQUAL_NORMALIZED_ARRIVAL = YES_IN_DECLARED_PAIR
EQUAL_SLOW_RESPONSE = NO_IN_DECLARED_PAIR
PHYSICAL_IR_INTERPRETATION = OPEN
INDEPENDENT_REVIEW = NOT_PERFORMED
```

Procedencia: las afirmaciones de esta nota se deducen de sus reglas
explícitas mediante las comprobaciones indicadas; no se atribuyen a un paper
ni se apoyan en un resumen generado por IA. El índice local de biblioteca
se consultó antes de la construcción. No se ejecutaron generadores científicos.
