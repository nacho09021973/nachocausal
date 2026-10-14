# Comprobación matemática de las respuestas O1 y O2

Fecha: 2026-10-02. Base comprobada: `3387f35`.
Estado: `AUTHOR_CHECKED / EXTERNAL_CLOSURE_PENDING`.
Objeto: reunir la evidencia de las dos respuestas sin otra ronda de modelos.
Las pruebas siguientes son algebraicas; no se ejecutó código científico.
El informe de DeepSeek se usa para identificar objeciones, no como prueba.

## 1. O1: enunciado exacto y contraejemplo

Para cada n>=1, C_n tiene dos cadenas saturadas de 2n y 3n coberturas,
con extremos comunes s,d e interiores disjuntos. A_n es la matriz de
cobertura, con A_n[y,x]=1 si x está cubierto por y. Se fija
`B_(gamma,n)=exp(-gamma/n) A_n`, con gamma=0 o gamma=log(4/3).
La respuesta fuente-detector al impulso unitario es

`R_(gamma,n)(l)=exp(-2gamma) 1_{l=2n}+exp(-3gamma) 1_{l=3n}`.

Esto se obtiene contando el único camino de cada longitud o multiplicando
los pesos de sus coberturas. Para theta=1/2, ambas primeras llegadas son
2n: sus primeras amplitudes son 1 y 9/16, ambas mayores que el umbral.
La llegada normalizada es 2 para ambas.

En una ventana T=4n, K_(gamma,n) es la convolución retardada por R.
Sea c_n(k)=1/sqrt(4n), un vector de norma uno, constante y retenido por
todo proyector de bajas diferencias que incluya el autovalor cero.
Cada retardo l contribuye (T-l)/T a su lectura. Por tanto

`ell_(gamma,n)=<c_n,K_(gamma,n)c_n>
              =exp(-2gamma)/2+exp(-3gamma)/4`.

Las lecturas son `3/4=192/256` y `99/256`; difieren en `93/256`.
Segunda comprobación: en [0,4), el protocolo h(t)=1/2 produce lecturas
integradas de exp(-2gamma)/4 sobre [2,4) y de exp(-3gamma)/4 sobre [3,4),
lo que reproduce exactamente la misma fórmula. El caso n=1 ya basta.

**Proposición O1.** No existe una función única F de los datos comunes
I_n=(C_n,s,d,n,theta,T,normalización) y de tau que reproduzca ell_(gamma,n)
para las dos dinámicas, sin recibir información dinámica adicional.

**Prueba.** Para n fijo, las entradas (I_n,tau) son idénticas. F devuelve
el mismo valor sobre la misma entrada, pero las lecturas difieren. Contradicción.
Usar tau/n en vez de tau conserva el argumento. Incluir gamma como nueva
entrada elimina esta obstrucción, porque cambia el problema de reconstrucción.

La proposición es una afirmación de no determinación de ell por tau.
Es compatible con que el test histórico de igualdad de llegada dé igualdad.
No demuestra imposibilidad para todos los escalares Q, no invalida otras
funciones q del contrato histórico y no necesita considerar ell un observable
autorizado por ese contrato. Su dominio es el blanco ampliado declarado.
En particular, si el único blanco fuese comparar tau, este contraejemplo
no sería una objeción a cumplirlo. Esto comprueba el alcance por caso límite.

## 2. O2: datos comunes y retención de cada modo

Sea H=L2([0,4)), con norma de integración dt. Para T=4n se define
`(D_T f)(k)=f(k+1)-f(k)`, `L_T=D_T^*D_T`,
`P_n=1_[0,1/(4n)](L_T)`.
La isometría E_n:C^(4n)->H toma el valor sqrt(n) f(k) en la celda
I_(k,n)=[k/n,(k+1)/n). Su adjunto toma el valor
`sqrt(n) integral_I_(k,n) h(t)dt`. La integral por celda prueba E_n^*E_n=I.
Entonces `Pi_n=E_n P_n E_n^*` es un proyector ortogonal.

Los modos discretos cos(pi j(k+1/2)/T), j=0,...,T-1, tienen autovalores
`lambda_j=4 sin^2(pi j/(2T))`. En filas interiores se verifica mediante
`2 cos(x)-cos(x-a)-cos(x+a)=4 sin^2(a/2)cos(x)`.
En los extremos se usa la reflexión c_(-1)=c_0 y c_T=c_(T-1), que
cumplen esos cosenos. Los T autovalores son distintos; estos modos
constituyen una base propia de la matriz simétrica L_T.

En H se consideran phi_0(t)=1/2 y phi_j(t)=cos(pi j t/4)/sqrt(2), j>=1.
Su normalización y ortogonalidad se verifican integrando productos de cosenos.
Defínase `v_(j,n)(k)=phi_j((k+1/2)/n)/sqrt(n)`.
Para j>=1 fijo y `n>=max(1,ceil(pi^2 j^2/4))`, j<4n y

`lambda_(j,n)=4 sin^2(pi j/(8n))
             <=pi^2 j^2/(16n^2)<=1/(4n)`.

Así P_n v_(j,n)=v_(j,n), con el corte cuadrado correcto. Para j=0
la retención vale para todo n. La elección de n es suficiente, no mínima.

## 3. O2: dos comprobaciones del error de aproximación

**Vía A: valores en centros de celda.** E_n v_(j,n) coincide con phi_j
en el centro de cada celda. El máximo de |phi_j'| es a lo sumo
pi j/(4sqrt(2)); la distancia al centro es <=1/(2n). Integrar la cota
puntual sobre un intervalo de longitud 4 da

`||E_n v_(j,n)-phi_j||_H <= pi j/(4sqrt(2)n)`.

Como E_n v_(j,n) pertenece a ran Pi_n, la mejor aproximación ortogonal
implica la misma cota para `||(I-Pi_n)phi_j||_H`.

**Vía B: promedio exacto por celda.** Sea Q_n=E_n E_n^* y sinc(x)=sin(x)/x,
con sinc(0)=1. Integrando directamente el coseno en cada celda se obtiene

`E_n^* phi_j = sinc(pi j/(8n)) v_(j,n)`.

Para cada modo retenido, `Pi_n phi_j=Q_n phi_j` exactamente. Para
1<=j<4n, la suma geométrica de exp(2pi i j(k+1/2)/(4n)) es cero;
por cos^2(x)=(1+cos(2x))/2, esto da ||v_(j,n)||_2=1.
También ||v_(0,n)||_2=1. La identidad pitagórica del proyector Q_n da,
para los modos retenidos j>=1,

`||(I-Pi_n)phi_j||_H^2=1-sinc^2(pi j/(8n)) -> 0`.

Para j=0 el error es exactamente cero. Esta segunda vía no usa la cota
de derivada. Sin 1/sqrt(n) en v, el modo cero se interpolaría a sqrt(n)/2
y el error sería |sqrt(n)-1|; ese caso detecta el factor omitido en la
sugerencia del revisor. Las dos vías utilizan el corte 1/(4n), no su raíz.

## 4. O2: densidad, cuantificadores y respuesta

Las combinaciones finitas de phi_j son densas en H. Puede justificarse
sin asumir regularidad de h: t->cos(pi t/4) es un homeomorfismo de [0,4]
sobre [-1,1]; aproximación polinómica uniforme de funciones continuas y
las identidades de potencias de coseno dan densidad de estas combinaciones
en C([0,4]). La densidad de continuas en L2 completa el paso.
Estos son los hechos estándar de aproximación utilizados en la prueba.

Dado h en H y eta>0, elíjase primero una suma finita
`p=sum_(j=0)^J a_j phi_j` con ||h-p||<eta/2. Después elíjase n
suficientemente grande para retener todos los j<=J y para que
`sum_(j=1)^J |a_j| pi j/(4sqrt(2)n)<eta/2`.
Como ||I-Pi_n||<=1,

`||(I-Pi_n)h|| <= ||h-p||+||(I-Pi_n)p|| < eta`.

La condición vale para todo n posterior a ese umbral; es convergencia
fuerte de la sucesión completa. No requiere subespacios anidados.

Defínase el operador retardado
`(K_gamma h)(t)=exp(-2gamma)h(t-2)1_(t>=2)
               +exp(-3gamma)h(t-3)1_(t>=3)`, con ||K_gamma||<=2.
Los retardos son múltiplos de la celda: celda a celda,
`K_gamma E_n=E_n K_(gamma,n)`. Por ello
`Ghat_(gamma,n)=E_n P_n K_(gamma,n) P_n E_n^*=Pi_n K_gamma Pi_n`.
Para h fijo,

`||Ghat_(gamma,n)h-K_gamma h||
 <=2||Pi_n h-h||+||(Pi_n-I)K_gamma h|| -> 0`.

Ambos argumentos a los que se aplica la convergencia fuerte son fijos:
h y K_gamma h. No se intercambia un límite con un supremo sobre fuentes
variables con n. Control de alcance: ||I-Pi_n||=1 para todo n, ya que
ran Pi_n es finito dimensional y tiene complemento ortogonal no trivial
en H. Por tanto ni siquiera los proyectores convergen en norma a I.
Este control no afirma por sí solo nada sobre la convergencia en norma de Ghat.

## 5. Estado y criterio para seguir

| Objeción | Evidencia técnica del autor | Estado del registro externo |
| --- | --- | --- |
| O1 | Proposición con entradas y cuantificadores; contradicción por 93/256; alcance histórico comprobado | respondida |
| O2 | Espectro con bordes; retención; dos vías de error; densidad y transferencia acotada | respondida |

Las respuestas quedan demostradas y comprobadas por el autor dentro de las
hipótesis declaradas. El cierre externo de las objeciones sigue pendiente;
no se modifica el veredicto histórico de DeepSeek. No hay una dependencia
matemática de otra ronda de modelos para usar estas derivaciones como base
de exploración explícitamente provisional. El siguiente problema de esa
exploración sería la interpretación del reloj y de la regla dinámica;
este documento no lo resuelve ni abre una nueva unidad de trabajo.
