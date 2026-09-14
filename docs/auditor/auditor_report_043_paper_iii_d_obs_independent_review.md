# Auditor Report 043 — revisión independiente de d_obs, Paper III

Fecha: 2026-09-11.

    REVIEW_ID=PAPER_III_PHASE_2_BLOCK_1_INDEPENDENT_REVIEW
    REVIEW_METHOD=SEPARATE_AGENT_SYMBOLIC_ADVERSARIAL_REVIEW
    REVIEWER=/root/revision_independiente
    VERDICT=NO_INVALIDATING_FAILURE_FOUND
    NECESSARY_MATHEMATICAL_GAPS_FOUND=NONE
    INDEPENDENT_REVIEW=PERFORMED
    NUMERICAL_VERIFIER=NOT_STARTED
    SIMULATIONS=NONE
    GATE_2=NOT_EVALUATED
    SOURCE_MODIFIED=NO
    NEXT_BLOCK_EXECUTED=NO

## 1. Objeto, independencia y procedencia

Se revisó exclusivamente
[la derivación del bloque 1](../paper_iii_fase2_bloque1_distancia_obstaculo.md),
en sus 407 líneas, sobre el exterior cerrado de una bola abierta euclídea de
radio positivo y la causalidad producto definida en ese documento.

Identificación del fichero efectivamente leído:

    SHA256=1a83b37421248e790f61529b8ea24bd2ee989306671afadf16b13aa9f7adb7d4
    BASE_HEAD=6b59f62857fea559d501d4fd068eff55e10a7a96
    SOURCE_GIT_STATE=UNTRACKED

El hash fue calculado por el agente principal y comunicado al revisor. El
commit identifica la base del repositorio; **no contiene el fichero revisado**.

El usuario solicitó una revisión independiente, adversarial y sin código ni
sprinklings, concentrada en §4, los casos límite y §8. Se encargó a un agente
separado, sin heredar el historial de elaboración ni la valoración favorable
del autor o del usuario. Recibió el fichero, las instrucciones aplicables y
la tarea de intentar falsificarlo. Reconstruyó los argumentos mediante lectura
y razonamiento simbólico; no editó el documento.

Este informe archiva su dictamen y resume los ataques examinados. El agente
principal, autor del fichero, solo comprueba la procedencia y registra el
informe. La independencia corresponde al agente revisor: **no es revisión por
una persona, formalización mecánica ni certificación externa**.

## 2. Dictamen del revisor

> No he encontrado un fallo invalidante ni un hueco matemático que impida
> sostener los resultados del bloque 1.

El dictamen está condicionado al dominio y a la clase de curvas escritos.
No afirma infalibilidad de la revisión. No se necesitó reparar ninguna prueba
para llegar a este resultado.

## 3. Ataques sobre la cota global de §4

### Curvas no planas, retrocesos radiales y vueltas angulares

**Referencia: líneas 154–175 y 193–215 del fichero revisado.**

La descomposición de velocidad es ortogonal porque
\(U\cdot\dot U=0\) casi por doquier. El vector
\((\sqrt{1-m^2/R^2},m/R)\) tiene norma uno y componentes no negativas.
Cauchy–Schwarz aplicado a \((|\dot R|,R|\dot U|)\) produce exactamente (3),
incluido \(R=m\). No presupone planitud ni monotonía angular.

Si \(v_*\) alcanza el mínimo radial, la variación de \(H_m(R)\) en
\([0,v_*]\) es al menos \(H_m(r)\), y en \([v_*,1]\) es al menos \(H_m(s)\).
Los retrocesos radiales no reducen esa cota. El intento de mejorar el camino
mediante una excursión tridimensional no invalida el argumento.

### Antípodas y singularidades de arccos

**Referencia: líneas 177–191.**

Para cada \(\delta>0\), la composición regularizada es absolutamente continua.
La cota sobre su derivada da

\[
|f_\delta(1)-f_\delta(0)|\le\int_0^1|\dot U|.
\]

Los valores extremos convergen a \(\theta\) y \(0\). La cota angular incluye
\(\theta=\pi\), sin diferenciar directamente arccos en sus polos.

### Monotonía de G y extremos radiales singulares

**Referencia: líneas 217–234.**

En el intervalo interior, los términos aparentemente singulares se cancelan
al derivar y queda

\[
G'(m)=\theta-\arccos(m/r)-\arccos(m/s)>0
\]

en el caso obstruido. La continuidad extiende la desigualdad a
\(m=\min(r,s)\). Si un extremo pertenece a la esfera, necesariamente \(m=a\):
no se necesita derivar en ese extremo. No se encontró una escapatoria en la
cota \(\ell(\gamma)\ge G(m)\ge G(a)\).

## 4. Tangencias, esfera y degeneraciones

**Referencia: líneas 92–115, 123–147 y 260–283.**

El criterio de visibilidad distingue correctamente entre mínimo del segmento
en un extremo, pie perpendicular interior y paso por el origen.
En el caso obstruido, \(\theta>\alpha+\beta\) sitúa los contactos en el orden
correcto sobre el arco. Los segmentos tangentes permanecen en el exterior.

La revisión comprobó la coincidencia de las dos fórmulas en la tangencia, los
segmentos de longitud cero cuando un extremo llega a la esfera y el valor
\(a\theta\) para ambos extremos sobre ella. En antípodas, la multiplicidad de
planos y minimizadores no afecta la distancia. El caso \(a=0\) se define
separadamente, sin evaluar ángulos indefinidos en el centro.

No se encontró discontinuidad ni construcción inexistente que invalidase
los casos declarados.

## 5. Equivalencia causal y orden

### Igualdad temporal

**Referencia: líneas 316–349.**

El revisor reconstruyó explícitamente el paso de suficiencia. Si
\(\sigma:[0,d]\to X_a\) es un minimizador por longitud de arco y \(d>0\),
la curva

\[
v\longmapsto
\bigl(t_p+\Delta t\,v,\ \sigma(dv)\bigr),\qquad 0\le v\le1,
\]

satisface \(\dot t=\Delta t\ge d=|\dot x|\) casi por doquier.
Cuando \(\Delta t=d\), sigue siendo causal admisible, incluidos los tramos
sobre la esfera. No se exige que sea geodésica del Minkowski ambiente.
Para \(d=0\), sirve la curva vertical, incluida la constante.

La parametrización explícita sería una ampliación expositiva opcional; el
revisor no la considera una reparación necesaria del argumento existente.

### Exterior abierto

**Referencia: líneas 285–312.**

El potencial contraejemplo al eliminar la esfera está ya separado
correctamente: tangencias y obstrucciones conservan el ínfimo, pero pierden
el minimizador y la existencia causal saturada. No contradice el teorema
para el exterior cerrado.

### Axiomas métricos y transitividad

**Referencia: líneas 238–258 y 351–390.**

La concatenación mediante reparametrizaciones afines conserva la clase de
curvas absolutamente continuas y prueba la desigualdad triangular.
Esta implica transitividad causal también en relaciones saturadas.
Antisimetría y exclusión de \(p=q\) en la versión estricta son correctas.

## 6. Clasificación de hallazgos

| Clase | Resultado del revisor independiente |
|---|---|
| Error matemático invalidante | Ninguno encontrado |
| Hueco matemático que requiera subsanación | Ninguno encontrado |
| Precisión editorial matemática necesaria | Ninguna identificada |
| Detalle expositivo opcional | Escribir la parametrización causal explícita de §5 de este informe |

**Observación documental del agente principal, separada del dictamen
matemático:** el enlace de la línea 19 del fichero tiene sus paréntesis
escapados como delimitadores matemáticos y no está escrito como un enlace
Markdown normal. Es un defecto de formato, sin incidencia en las pruebas.
Se registra sin modificar el objeto de esta revisión.

## 7. Estado y alcance después de la revisión

La revisión independiente queda realizada y documentada en este informe.
El token anterior de revisión pendiente en el fichero fuente pertenece a la
instantánea conservada; no se ha reescrito el fichero ni cambiado su hash.

El resultado se limita a la fórmula de distancia, sus axiomas métricos y
la causalidad producto del dominio con frontera admitida. No establece
reconstrucción desde un poset, convergencia discreta, identificación de
horizontes ni novedad bibliográfica.

No se escribió ni ejecutó código de cálculo o verificación científica; no
se realizaron simulaciones, sprinklings, cálculos numéricos ni pruebas Lean.
Las herramientas locales se limitaron a lectura, procedencia y registro
documental. No se ejecutó el auditor general del repositorio.

El verificador numérico y los controles posteriores siguen pendientes.
Este dictamen **no adjudica GATE_2 ni autoriza o ejecuta el siguiente bloque**.
