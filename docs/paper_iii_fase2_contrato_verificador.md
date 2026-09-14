# Paper III — contrato del verificador continuo de d_obs, v1

Fecha: 2026-09-11. Contrato fijado antes de escribir o ejecutar el verificador,
según la opción 2 indicada por el usuario.

    CONTRACT_ID=PAPER_III_D_OBS_NUMERICAL_VERIFIER_V1
    STATUS=FROZEN_PRE_IMPLEMENTATION
    IMPLEMENTATION=NOT_STARTED
    VERDICT=NOT_RUN
    SCOPE=CONTINUUM_NUMERICAL_CHECKS_ONLY
    RANDOMNESS=NONE
    SPRINKLINGS=NONE
    MATCHED_CONTROL=NOT_STARTED
    GATE_2=NOT_EVALUATED

## 1. Entrada e infraestructura inspeccionada

La [hoja de ruta](hoja_de_ruta_paper_iii.md), §Fase 2, exige una construcción
independiente, pero no fija casos, tolerancias ni un criterio numérico de
aceptación. Este contrato completa esos criterios; no modifica las puertas
de fase anteriores.

| Recurso leído | Reutilización prevista |
|---|---|
| [verify_horizon_threshold.py](../dev/verify_horizon_threshold.py) | Comprobaciones deterministas separadas, referencia calculada por una vía distinta y dependencias obligatorias que no se omiten silenciosamente. |
| [verify_3p1_phase0_contract.py](../dev/verify_3p1_phase0_contract.py) | Hashes, identificadores de comprobación, separación entre fallo comprobado y error de ejecución. |
| [verify_3p1_notes_figures.py](../dev/verify_3p1_notes_figures.py) | Residuos y tolerancias visibles por comprobación; no se reutilizan sus tolerancias de redondeo editorial. |
| [requirements.txt](../requirements.txt) | NumPy, SciPy y SymPy ya declarados; sin alterar el entorno sellado. |

La búsqueda en dev/, tests/, nachocausal/ y scripts/ no encontró una
implementación de d_obs ni un verificador de caminos alrededor de obstáculos.
Se reutilizan las convenciones existentes; las rutinas Schwarzschild 1+1,
sus generadores y los tests Monte Carlo sellados no son referencias para
este problema.

Objetos de entrada, conservados sin cambios:

- [Prueba continua](paper_iii_fase2_bloque1_distancia_obstaculo.md):
  SHA-256 1a83b37421248e790f61529b8ea24bd2ee989306671afadf16b13aa9f7adb7d4.
- [Revisión independiente 043](auditor/auditor_report_043_paper_iii_d_obs_independent_review.md):
  SHA-256 04478b3d7359c7eb201629444137a427c8930efe7a134427907b5aceb206633f.

## 2. Magnitud y referencia independiente

Se contrasta la implementación de (2) de la prueba, en
\(X_a=\{x:|x-o|\ge a\}\), con una referencia de **caminos poligonales**.
No se confunde con reconstrucción desde un poset.

Para cada par, normalizar a \(a=1,o=0\) y trabajar en un plano por el centro
y los extremos. En pares colineales se elige como segundo eje la proyección
normalizada del eje cartesiano menos alineado con el primero; los empates se
resuelven por orden de ejes. Usar el teorema ya revisado de existencia de un
minimizador plano es admisible; usar su fórmula para fijar el resultado no lo es.

Construir un polígono convexo inscrito \(P^-\) y otro circunscrito \(P^+\).
Sus direcciones proceden de una malla angular uniforme, añadiendo las
direcciones radiales de ambos extremos. El inscrito es la envolvente convexa
de esos puntos sobre el círculo; el circunscrito es la intersección de los
semiplanos de soporte con normales en esas mismas direcciones.
Así \(P^-\subset B\subset P^+\), y ambos extremos quedan fuera del
**interior** de ambos polígonos, incluso cuando están sobre el círculo.

En cada exterior poligonal, calcular el camino mínimo mediante un grafo de
visibilidad con extremos y vértices: una arista representa un segmento que
no entra en el interior del polígono, y pesa su longitud euclídea.
Las aristas de frontera están permitidas. Resolver el camino mínimo y guardar
su secuencia de vértices. La implementación debe justificar que este grafo
recoge el mínimo poligonal: en espacio libre se enderezan los tramos y los
cambios de dirección necesarios se sitúan en vértices del obstáculo.

Las longitudes obtenidas cumplen, en aritmética exacta,

\[
L^-_n\le d_{\rm obs}\le L^+_n.
\]

La referencia no puede llamar a la fórmula candidata, a sus ángulos de
tangencia, a su selector de rama ni al camino tangente–arco–tangente.
Solo comparte los extremos, el centro y el radio. La visibilidad usa
intersección de segmentos con semiplanos, con implementación separada.
Cada camino superior se comprueba además segmento a segmento contra la
bola mediante la mínima distancia euclídea de un segmento al centro.
No basta comprobar únicamente sus vértices.

Mallas obligatorias: \(n=64,128,256,512,1024,2048\), para dos desfases fijos
\(\phi=0,\pi/17\). Dentro de cada desfase las mallas son anidadas. Se registran
todos los niveles, sin parada anticipada. Se exigen anidamiento geométrico,
\(L^-_n\) no decreciente y \(L^+_n\) no creciente dentro del error aritmético.
La referencia produce cotas numéricas, no intervalos certificados por
aritmética dirigida.

## 3. Casos obligatorios y cobertura

Los casos son deterministas, sin semillas. Las coordenadas se especifican
matemáticamente antes de convertirlas al formato numérico.

| ID | Casos o contraste obligatorio |
|---|---|
| D1 | Todos los pares \(x=(r,0,0)\), \(y=(s\cos\theta,s\sin\theta,0)\), con \(r,s\in\{1,1+2^{-20},2,8\}\) y \(\theta\in\{0,2^{-20},\pi/6,\pi/2,\pi-2^{-20},\pi\}\): 96 casos, todos contra ambas familias de polígonos. |
| D2 | Tangencia construida sin el selector de rama: \(x=(-u,1+\delta,0)\), \(y=(v,1+\delta,0)\), \(u,v\in\{1,4\}\), \(\delta\in\{0,\pm2^{-10},\pm2^{-20},\pm2^{-35}\}\). Todos contra la referencia. El signo de \(\delta\) fija la visibilidad geométrica. |
| D3 | Cercanía a la esfera: D1 con \(r,s\in\{1,1+2^{-40}\}\), \(\theta\in\{0,\pi/2,\pi\}\). Todos contra la referencia. |
| D4 | Coincidencia, simetría y \(d\ge\lVert x-y\rVert\) en todos los pares anteriores. Para \(\delta=0\) en D2, comprobar además \(d=u+v\). Para puntos de la esfera en D1, comprobar la longitud del arco de círculo. |
| D5 | Triangular para todas las ternas ordenadas del conjunto de 42 puntos: radios \(\{1,2,8\}\) por las seis direcciones axiales y las ocho \((\pm1,\pm1,\pm1)/\sqrt3\). Sin muestreo de ternas. |
| D6 | Repetir D1–D3 bajo cada transformación \(x\mapsto aQx+o\), con \(a\in\{2^{-20},1,2^{20}\}\), \(o/a\in\{(0,0,0),(3,-2,5)\}\), \(Q\in\{I,\operatorname{diag}(-1,1,1),\frac13[(-1,2,2),(2,-1,2),(2,2,-1)]\}\). Contrastar covarianza con la referencia canónica escalada; no recalcular una referencia desde la salida candidata. |
| D7 | \(a=0\): distancia euclídea, incluidos centro y coincidencia, con pares del conjunto \(\{0,e_1,e_2,-e_1\}\). Rechazar \(a=-1\); para \(a=1,o=0,y=2e_1\), rechazar \(x=0\) y \(x=(1-2^{-20})e_1\), también intercambiando extremos. Sobre \(a=1,o=0,x=2e_1,y=3e_1\), sustituir de uno en uno cada escalar de entrada por NaN, \(+\infty\) y \(-\infty\): rechazo, sin proyección silenciosa. |
| C1 | Continuidad entre ramas: para cada D2, \(\lvert d_\delta-d_0\rvert\le2\lvert\delta\rvert+\tau\). Para D3 frente a sus extremos radiales en la esfera, cambio de distancia \(\le\lvert r-1\rvert+\lvert s-1\rvert+\tau\). |
| C2 | Causalidad fuera de la zona de incertidumbre y casos saturados según §5; reflexividad, antisimetría y transitividad numéricas. |

Duplicados geométricos conservan sus ID de cobertura. Si se comparte un
cálculo por eficiencia, se registra qué comprobaciones lo reutilizan.
Las identidades simples de D4 complementan la referencia poligonal; no la
sustituyen ni convierten otra evaluación de (2) en referencia independiente.

## 4. Tolerancias fijadas antes del código

Las comprobaciones se hacen tras centrar y normalizar por \(a>0\).
Sea \(S=\max(1,|x|,|y|)\), extendido a todos los extremos de una terna.
Las cotas dimensionales se recuperan multiplicando por \(a\). Para \(a=0\)
se usa \(S=\max(1,|x-o|,|y-o|)\) en unidades de entrada.

| Uso | Tolerancia y criterio |
|---|---|
| Residuos de identidad, simetría, covarianza, triangular y continuidad | \(\tau=10^{-10}S\). Un residuo que supera \(\tau\) falla; no se promedian residuos. |
| Anchura final de referencia | \(L^+_{2048}-L^-_{2048}\le10^{-4}S\) para cada desfase. Si no se alcanza: INCONCLUSIVE, nunca PASS. |
| Comparación candidata–referencia | \(L^-_n-\tau\le d_{\rm candidata}\le L^+_n+\tau\) en todos los niveles y desfases, además de la anchura final. |
| Admisibilidad del testigo superior | Mínima distancia al centro por segmento \(\ge1-10^{-12}S\). Se registra el peor residuo firmado. |
| Margen causal independiente | \(\eta=10^{-3}S\), mayor que la anchura máxima admitida. No se suma a la definición del orden. |

La tolerancia aritmética separa errores de redondeo del error de discretización
poligonal. La anchura exigida fija la resolución de este contraste: no se
presenta como verificación de la fórmula a \(10^{-10}\).

La entrada candidata usa float64; la referencia geométrica resuelve signos
ambiguos y recomputa caminos finales con 80 dígitos mediante las capacidades
ya declaradas de SymPy. Se registran las versiones usadas. La clase exacta de
los casos de frontera procede de su construcción, no de redondear el radio.
Se permite diagnosticar el error de representación de esos casos; no cambiar
su pertenencia al dominio ni desplazar sus coordenadas silenciosamente.
Si a 80 dígitos un predicado necesario sigue sin resolverse, se registra
INCONCLUSIVE. No se adopta por defecto el signo favorable.

Las tolerancias son objetivos de resolución fijados a priori, no una promesa
de que el primer código los satisfaga. No se aumentan ni se extiende la malla
después de ver un resultado para conservar PASS.

## 5. Equivalencia causal: qué puede verificar un cálculo finito

En todos los casos con referencia resuelta, fijar tiempos de viaje
\(T_-=L^-_{2048}-\eta\) y \(T_+=L^+_{2048}+\eta\), para cada desfase.
El predicado candidato debe rechazar el primero y aceptar el segundo.
El camino poligonal superior, parametrizado durante \(T_+\), es el testigo
independiente de existencia. Comprobar sus velocidades y su admisibilidad;
la cota inferior proporciona el contraste de imposibilidad para \(T_-\).

Para igualdad exacta se exigen eventos coincidentes, desplazamiento radial
\((2,0,0)\to(3,0,0)\) con \(T=1\), y tangencia D2 con \(T=u+v\).
Estas longitudes y tiempos son exactamente representables. También se
comprueba el testigo sobre la esfera de ángulo \(\pi/2\), parametrizado con
velocidad uno y duración \(\pi/2\), evaluando sus identidades a alta precisión.
Esta última comprobación no exige que float64 decida un empate trascendente.

Se prohíbe llamar «verificación independiente de igualdad causal» a definir
\(T=d_{\rm candidata}\) y volver a comparar ambos valores. Para pares
generales con \(T\) dentro de la banda de incertidumbre se informa
UNRESOLVED_EQUALITY, sin inventar una etiqueta causal. Esta limitación es
esperada y no sustituye las comprobaciones obligatorias de igualdad exacta;
la equivalencia saturada general sigue respaldada por la prueba analítica.

Para el orden, usar los 42 puntos de D5 con tiempos \(\{-64,0,64\}\), todos
los eventos y ternas ordenadas, y añadir por separado cadenas radiales
exactamente saturadas \((t,x)=(0,2e_1),(1,3e_1),(2,4e_1)\).
Las matrices reflexiva y estricta deben respetar sus axiomas; las
comparaciones booleanas resueltas no admiten tolerancia ni cierre transitivo
posterior. Distinguir eventos diferentes de coincidencias duplicadas.

## 6. Controles negativos, veredicto y registro

El propio verificador debe detectar por separado estas alteraciones
deliberadas: distancia euclídea para todos los pares; supresión del término
de arco; exclusión de extremos sobre la esfera; sustitución de \(\ge\) por
\(>\) en el predicado causal; NaN presentado como resultado válido; omisión
de una familia obligatoria; una arista del testigo superior que cruza la bola.
Cada alteración debe activar una comprobación identificada. Son pruebas
del verificador futuro, no modificaciones de la prueba ni del modelo.

- **PASS, salida 0:** todas las familias obligatorias completas y satisfechas,
  referencias resueltas, controles negativos detectados y procedencia válida.
- **FAIL, salida 2:** una discrepancia resuelta excede la tolerancia, falla un
  axioma o testigo, un control negativo sobrevive o se omite cobertura.
- **INCONCLUSIVE, salida 1:** falta una dependencia o entrada, hay error de
  ejecución, un predicado necesario queda indeterminado o la referencia no
  alcanza la anchura fijada. Si además existe un fallo comprobado, prevalece
  FAIL. Ningún caso omitido se transforma en PASS.

El futuro verificador será un artefacto permanente en dev/, con salida
estructurada persistente que registre contrato y hashes de entrada/código,
comando, versiones, casos, cobertura, cotas por nivel, residuos, tolerancias,
testigos, controles negativos y veredicto. La implementación puede elegir
representaciones internas y optimizaciones que preserven estos criterios.
No puede seleccionar retrospectivamente casos, tolerancias o referencia.

## 7. Congelación y límite

Esta versión queda fijada documentalmente antes de implementar; no equivale
a un commit, un sellado confirmatorio ni una firma PI inventada.
Un cambio científico exige una versión nueva con motivo, conservando v1 y
los resultados que pudieran haberla motivado. Cada ejecución registrará el
hash de la versión exacta que aplica.

El máximo resultado permitido es: «la implementación satisface las
comprobaciones continuas finitas declaradas, a la resolución registrada».
No prueba convergencia universal, equivalencia causal por cálculo para todos
los pares, reconstrucción intrínseca desde el poset ni detección de horizonte.

Este paso crea únicamente el contrato. No implementa el verificador,
no abre el control emparejado ni sprinklings y no evalúa GATE_2.
