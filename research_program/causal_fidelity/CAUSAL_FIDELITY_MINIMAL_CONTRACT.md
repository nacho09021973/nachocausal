# Contrato mínimo de fidelidad causal

> **Estado:** `NEW_FRONT / MINIMAL_CONTRACT v2.1 / DRAFT / UNPROVED`
> **Fecha:** 2026-10-14 (v1: 2026-09-18, congelada en `a77d9d8`; v2: borrador `505ac49`)
> **Rama:** `research/causal-fidelity-bridge`
> **v2.1 no está congelada.** Corrige la v1 según las revisiones `revisiones/2026-10-13-*` y la
> v2 según `revisiones/2026-10-14-argon-high-delta-v2/` (§11). Para congelarla faltan la revisión
> del delta v2→v2.1 y la relevancia para 3+1D.

Este documento abre un frente nuevo y deliberadamente estrecho. No reutiliza los
artefactos históricos de `research_program/puente_3p1/` ni los controles B1.6/B1.7.
Aquellos quedan como controles negativos históricos: muestran que una separación
estadística puede sobrevivir a un cambio de dimensión u orden sin certificar una
estructura dinámica genuinamente `3+1D`.

El objetivo aquí no es producir otra separación estática, sino comprobar si una
propiedad dinámica inferida del orden causal tiene una relación estrictamente
distinta con el límite infrarrojo.

**Relevancia para el objetivo 3+1D:** `[PENDIENTE — la fija el PI antes de congelar]`.
Este frente sólo continúa si sirve de forma demostrable al puente hacia `3+1D`; un
`PASS` en una familia `1+1D` o en una cadena de juguete no lo demuestra por sí solo.

## 1. Claim ceiling

Una construcción se evalúa en dos pasos. Primero, la **admisibilidad** (§6): si falla, la
construcción es `INADMISSIBLE`, se registra y se descarta; para el frente eso es `OPEN`,
no `FAIL`. Después, para una construcción admisible, el único resultado será uno de:

- `PASS`: la construcción, congelada antes de evaluarla, satisface el test de §7 y las
  cláusulas de no trivialidad de §8, con prueba (no sólo evidencia numérica);
- `FAIL`: se prueba que alguna obligación de §7 o §8 no se cumple. Un `FAIL` es de esa
  construcción, no un no-go del frente;
- `OPEN`: falta una definición, una prueba o una verificación que el contrato exige.

No se autoriza inferir de un `PASS` que se haya reconstruido la geometría,
demostrado una teoría física, identificado de forma única una dinámica, ni
establecido una firma exclusiva de `3+1D`. Tampoco se autoriza una afirmación de
novedad bibliográfica desde este documento.

## 2. Objetos congelados

### 2.1 Familia causal

Para cada \(N\in\mathbb N\), \(\mu_N\) es una **ley** sobre posets finitos
\(c=(E,\prec)\), donde \(\prec\) es un orden parcial **estricto** (irreflexivo y
transitivo). \(C_N\sim\mu_N\) denota una realización aleatoria; \(c\) denota una
instancia fija. Una ley determinista (\(\mu_N=\delta_{c_N}\)) está permitida. No se
supone ningún acoplamiento entre distintos \(N\): por eso el único modo de convergencia
admitido es en probabilidad (§5).

La familia debe especificar antes de cualquier ejecución:

1. la ley \(\mu_N\) y qué controla \(N\) (p. ej. \(|E|=N\) o un parámetro de escala);
2. las invariancias de reetiquetado exigidas a todo observable;
3. el tratamiento de las realizaciones sin par fuente–detector (§2.2), que se registran
   como nulas y no se descartan en silencio.

Ninguna coordenada de una realización, ni la verdad geométrica usada para generarla,
puede entrar en un observable. Las cardinalidades y longitudes de cadena sí son
observables legítimas: *blind to the embedding* no significa *count-free*
(`CLAUDE.md`, «order-only»).

### 2.2 Fuente, detector, movimientos y reloj

- **Par fuente–detector.** Un selector \(\sigma_N\) asigna a cada instancia \(c\) una ley
  sobre pares \((s,d)\in E\times E\) con \(s\prec d\), o el valor «sin par». Se permite que
  sea aleatorizado: un selector determinista y equivariante no existe en general cuando
  \(c\) tiene automorfismos que no fijan ningún par. \(\sigma_N\) se define sólo a partir
  del orden y es equivariante en ley: \(\sigma_N(\phi c)\overset{d}{=}\phi\,\sigma_N(c)\)
  para todo reetiquetado \(\phi\). Su aleatoriedad forma parte del espacio de probabilidad
  de \(C_N\). No hace falta identificar \(s,d\) entre distintos \(N\): el paso al IR (§5)
  se toma sobre escalares, no sobre eventos.
- **Movimientos admisibles.** Una regla \(A\), definida sólo a partir del orden y
  equivariante, fija para cada \(c\) los movimientos de un paso permitidos
  \(A(c)\subseteq\{(x,y):x\preceq y\}\) (p. ej. quedarse o avanzar un enlace de Hasse).
  Todo \(x\in E\) tiene al menos un movimiento en \(A(c)\): ningún proceso queda bloqueado.
  \(A\) es **común** a \(D_1\) y \(D_2\).
- **Reloj.** El tiempo de la dinámica es un número de pasos \(k\in\{0,1,2,\dots\}\). El
  tiempo macroscópico es \(t=k/\lambda(c;s,d)\), con una escala
  \(\lambda(c;s,d)\in[1,\infty)\) definida sólo a partir del orden (p. ej. la longitud de
  la cadena más larga de \(s\) a \(d\)) y fijada antes de evaluar. \(t\) toma valores en la
  malla \(\lambda^{-1}\mathbb Z_{\ge0}\); no es una coordenada reconstruida.

### 2.3 Dos dinámicas

Una dinámica \(D\) asigna a cada \((c,s)\) la ley de un proceso \((X_k)_{k\ge0}\) sobre
\(E\) con \(X_0=s\), cuyas trayectorias usan sólo movimientos de \(A(c)\). La dinámica
**no recibe el detector**: \(d\) es pasivo y sólo entra en la respuesta (§2.4). El
espacio de dinámicas admisibles se parametriza explícitamente; \(D_1\) y \(D_2\) son dos
puntos de ese espacio que difieren **sólo** en un ingrediente nombrado (p. ej. memoria
del incremento) y comparten \(\mu_N,\sigma_N,A,\lambda\) y el conjunto de umbrales
\(\Theta\) (§3).

No se permite cambiar a la vez la familia causal, el selector, los movimientos
admisibles y la dinámica: eso impediría atribuir una diferencia a \(D_1\) frente a
\(D_2\).

### 2.4 Respuesta

Para cada instancia y cada par \((s,d)\), la respuesta es una función determinista
\(\Delta_D(c;s,d,t)\in[0,1]\), definida en la malla de §2.2, que cumple:

1. es no decreciente en \(t\);
2. vale \(0\) para \(t<\tau_{\rm caus}(c;s,d)\) (§5): fuera del cono no hay respuesta;
3. depende sólo de \(c\), \((s,d)\), \(A\), \(\lambda\) y \(D\).

La elección mínima recomendada es la probabilidad de haber alcanzado el detector:
\(\Delta_D(c;s,d,t)=\mathbb P_D\big(\exists k\le t\lambda: X_k=d\big)\),
que cumple 1–3 por construcción. Al ser una probabilidad bajo \(D\), \(\Delta_D\) es
determinista dado \((c,s,d)\); toda la aleatoriedad restante viene de \(C_N\) y
\(\sigma_N\).

## 3. Arrival time

Antes de evaluar se fija un **intervalo de umbrales** \(\Theta=[\theta_-,\theta_+]\subset(0,1)\)
con \(\theta_-<\theta_+\). Para cada \(\theta\in\Theta\),

\[
\tau_{D,\theta}(c;s,d):=\min\{t\in\lambda^{-1}\mathbb Z_{\ge0} :
\Delta_D(c;s,d,t)\ge\theta\}\in[0,\infty],
\]

con \(\min\emptyset=\infty\). Como el reloj es discreto, el mínimo está bien definido y no
hay que aproximar un ínfimo. Es un arrival time **discreto**.

El arrival time es una salida dinámica. No es, por sí mismo, una coordenada
reconstruida ni una identificación de una superficie causal.

## 4. Único escalar \(Q\)

Para cada \(\theta\in\Theta\), el escalar es \(Q^D_\theta(C_N):=\tau_{D,\theta}(C_N;\sigma_N(C_N))\),
definido en el suceso «hay par»; fuera de él la realización es nula (§2.1(3)). No se admite
otra función \(q\): en la v1, una \(q\) que recibe la curva \(\Delta_D(\cdot)\) entera deja
de ser un resumen y vacía §3. La familia \(\{Q_\theta\}_{\theta\in\Theta}\) no es un
segundo score: \(\Theta\) se fija antes y el test se exige para **todo** \(\theta\in\Theta\),
nunca para el \(\theta\) que mejor salga.

## 5. Tiempos causales y paso al IR

**Cono causal por instancia.** Con los mismos movimientos admisibles \(A\),

\[
\tau_{\rm caus}(c;s,d):=\min\{k/\lambda : \text{existe una trayectoria de } A(c)
\text{ de } s \text{ a } d \text{ en } k \text{ pasos}\},\qquad \min\emptyset=\infty.
\]

Es una regla puramente de orden, fijada antes de la dinámica. Por §2.4(2),
\(Q^D_\theta\ge\tau_{\rm caus}\) en toda realización con par.

**Modo de convergencia.** Todos los límites son en probabilidad bajo \(\mu_N\) y
\(\sigma_N\), condicionados al suceso «hay par» (cuya probabilidad tiende a 1 por §6).
Se suprimen la convergencia casi segura (exigiría un acoplamiento entre \(N\) que el
contrato no fija) y la de la esperanza (no es un modo de convergencia de variables
aleatorias, y con \(\tau=\infty\) en un suceso de probabilidad positiva haría
\(\mathbb E[Q]=\infty\)).

**Comparación por realización.** \(Q^{D_1}_\theta\), \(Q^{D_2}_\theta\) y \(\tau_{\rm caus}\)
se evalúan sobre la **misma** realización \((C_N,\sigma_N(C_N))\), así que sus diferencias
son variables aleatorias bien definidas para cada \(N\) sin acoplar distintos \(N\). Los
límites no tienen por qué ser constantes: dos dinámicas pueden converger al mismo tiempo
IR aleatorio.

**Conjuntos, en la misma álgebra.** Por realización, ambos son semirrectas cerradas de
\([0,\infty)\) (bajo §6 y §8, ninguna vacía):

\[
T^D_{\theta}(C_N):=[Q^D_\theta(C_N),\infty),\qquad
T_{\rm caus}(C_N):=[\tau_{\rm caus}(C_N;\sigma_N(C_N)),\infty).
\]

Comparar un punto aislado con una semirrecta queda excluido por tipo. Si los límites en
probabilidad son constantes, \(\tau^{\rm IR}_D\) y \(\tau^{\rm IR}_{\rm caus}\), el test de
§7 se reduce a \([\tau^{\rm IR}_{D_1},\infty)=[\tau^{\rm IR}_{D_2},\infty)\subsetneq
[\tau^{\rm IR}_{\rm caus},\infty)\), es decir, \(\tau^{\rm IR}_{D_1}=\tau^{\rm IR}_{D_2}>
\tau^{\rm IR}_{\rm caus}\).

La notación \(T^D_\theta\) no significa automáticamente una propiedad geométrica ni una
observable universal: esas interpretaciones quedan abiertas hasta una prueba independiente.

## 6. Admisibilidad (precondiciones)

Antes de evaluar el test, la construcción debe probar:

- **ADM1 — par.** \(\mathbb P(\sigma_N(C_N)=\text{«sin par»})\to0\).
- **ADM2 — escala.** \(\lambda(C_N;\sigma_N(C_N))\to\infty\) en probabilidad.
- **ADM3 — conexión.** \(A(C_N)\) conecta \(s\) con \(d\) con probabilidad que tiende a 1,
  es decir, \(\tau_{\rm caus}<\infty\).
- **ADM4 — cono no colapsado.** Existen \(0<a\le b<\infty\) tales que
  \(\mathbb P\big(a\le\tau_{\rm caus}(C_N;\sigma_N(C_N))\le b\big)\to1\).

Si una de ellas falla, la construcción es `INADMISSIBLE` (§1), no `FAIL`. ADM4 excluye
el caso en que el camino admisible más corto tiene \(O(1)\) pasos mientras
\(\lambda\to\infty\): entonces \(\tau_{\rm caus}\to0\) y la pérdida estricta saldría
gratis. Que esto ocurra con enlaces de Hasse y cadena más larga en posets densos es
plausible y está sin comprobar `[UNVERIFIED]`; ADM4 lo excluye sin depender de ello.
Una forma de cumplir ADM4 por construcción es tomar como \(\lambda\) la propia distancia
en pasos de \(A\) de \(s\) a \(d\), con lo que \(\tau_{\rm caus}\equiv1\); entonces ADM2
exige que esa distancia diverja.

## 7. Test exacto

Para una construcción admisible \((\mu_N,\sigma_N,A,\lambda,D_1,D_2,\Theta)\) congelada
antes de evaluar, la hipótesis objetivo es que, **para todo** \(\theta\in\Theta\):

1. **igualdad dinámica en IR:**
   \(Q^{D_1}_\theta(C_N)-Q^{D_2}_\theta(C_N)\to0\) en probabilidad;
2. **pérdida estricta frente al causal:** existe \(\varepsilon>0\) tal que, para
   \(i=1,2\), \(\mathbb P\big(Q^{D_i}_\theta(C_N)\ge\tau_{\rm caus}(C_N;\sigma_N(C_N))
   +\varepsilon\big)\to1\).

En términos de conjuntos: asintóticamente, \(T^{D_1}_\theta\) y \(T^{D_2}_\theta\) coinciden
y quedan estrictamente dentro de \(T_{\rm caus}\), separados de su borde por al menos
\(\varepsilon\). Los tiempos de \([\tau_{\rm caus},\tau_{\rm caus}+\varepsilon)\) son
causalmente admisibles y quedan fuera del conjunto IR común.

\(\varepsilon\) no es una tolerancia elegida a la vista de los datos: la obligación es
probar que existe. Una coincidencia numérica en una escalera finita de \(N\) no es una
demostración de igualdad.

## 8. Cláusulas de no trivialidad

Un `PASS` exige además, con prueba:

- **NT1 — no vacuidad.** Para todo \(\theta\in\Theta\) e \(i=1,2\), \(Q^{D_i}_\theta(C_N)\)
  está acotado en probabilidad (*tight*). Con ADM3–ADM4, excluye el `PASS`
  \(\emptyset=\emptyset\subsetneq T_{\rm caus}\) por umbral inalcanzable.
- **NT2 — uniformidad en el umbral.** El test de §7 se cumple para todo \(\theta\) de un
  intervalo \(\Theta\) no degenerado fijado antes. Excluye que la igualdad se deba a la
  elección de un umbral: dos dinámicas iguales hasta cruzar un \(\theta\) y distintas
  después pasarían en ese \(\theta\) y fallarían en otro.
- **NT3 — no identidad en el escalar.** Existen \(\theta\in\Theta\) y \(\eta>0\) tales que
  \(\mathbb P\big(Q^{D_1}_\theta(C_N)\ne Q^{D_2}_\theta(C_N)\big)\ge\eta\) para todo \(N\)
  suficientemente grande, y esa diferencia se **prueba**, no se afirma. Excluye
  \(D_1=D_2\) y dinámicas que sólo difieren en la curva \(\Delta\) sin que \(Q\) lo note:
  la igualdad del punto 1 de §7 debe ser un efecto del límite, no una identidad a todo
  \(N\). Se informa además el orden de \(|Q^{D_1}_\theta-Q^{D_2}_\theta|\) en \(N\), como
  descripción, no como criterio.
- **NT4 — la regla no se elige por la dinámica.** \(\lambda\), \(A\), \(\sigma_N\) y
  \(\Theta\) no dependen de \(D\). Excluye una regla constante o ajustada a mano.

## 9. Obligaciones de validación

Antes de cualquier resultado se deberá disponer de:

- definiciones ejecutables de \(\mu_N,\sigma_N,A,\lambda,D_1,D_2,\Delta,\tau,\tau_{\rm caus}\);
- una prueba o certificado de que no hay fuga de coordenadas, etiquetas o ground truth
  en \(Q\) ni en la decisión;
- la prueba de ADM1–ADM4;
- **controles negativos:** \(D_1=D_2\) debe ser rechazado por NT3; la construcción
  «iguales hasta el umbral» de `revisiones/2026-10-14-argon-high-delta-v2/` (§2.2.1)
  debe ser rechazada por NT2 o NT3;
- **control de contrato:** una construcción conocida que el contrato admita como `PASS`
  con contenido, para comprobar que el test no es vacío por construcción. Candidata
  `[UNVERIFIED]`: cadena lineal, paseo i.i.d. frente a paseo con memoria markoviana de
  igual deriva \(p<1\) (`revisiones/2026-10-13-argon-high-contrato/`). Su NT3 depende de
  que los \(Q_\theta\) finitos difieran (argumento de TCL con \(\theta\ne1/2\) en
  `revisiones/2026-10-14-argon-high-delta-v2/`, sin comprobar). Es un ejemplo de límite
  hidrodinámico conocido: valida el contrato, **no** es un resultado del frente;
- un registro de realizaciones nulas, de \(\tau=\infty\) y de construcciones `INADMISSIBLE`;
- una tabla previa de \(\Theta\), tamaños y criterio `PASS/FAIL/OPEN/INADMISSIBLE`;
- revisión adversarial del test antes de interpretar cualquier coincidencia.

No se ejecuta un experimento confirmatorio ni se crea una segunda familia de
observables hasta cerrar esta unidad mínima.

## 10. Exclusiones explícitas

Este contrato no incorpora:

- `research_program/puente_3p1/` ni B1.5, B1.6 o B1.7;
- los archivos históricos de control negativo;
- `.webui_secret_key`;
- una afirmación de que la igualdad IR sea ya cierta;
- una afirmación de que la inclusión estricta sea universal;
- promoción al estado canónico, publicación o novedad.

## 11. Cambios y trazabilidad

Ninguna afirmación de las revisiones se adopta sin comprobarla aquí; lo que se adopta son
los defectos señalados, comprobados leyendo la versión revisada.

### 11.1 v1 → v2

Revisiones: `revisiones/2026-10-13-argon-contrato/` (A), `…-argon-high-contrato/` (AH),
`…-pro31-contrato/` (P).

| Defecto de v1 | Señalado por | Cambio en v2 |
|---|---|---|
| `PASS` vacío \(\emptyset=\emptyset\) con \(\tau=\infty\) | A, AH, P | NT1, NT2 |
| \(T_{\rm IR}\) (de dos escalares) frente a \(T_{\rm caus}\) (conjunto): tipos sin casar | A, AH, P | §5: ambos semirrectas; §6 reducido a una desigualdad de escalares |
| `PASS` por cardinalidad (punto \(\subsetneq\) intervalo) | AH | §5: misma álgebra |
| IR con \(C_N\) fijo; \(N\) libre y ligada a la vez | A, AH, P (P de pasada) | §5: límite \(N\to\infty\), \(N\) ligada |
| Cuantificadores ausentes sobre \(N,s\), realizaciones | A, AH, P | §2.1 (ley vs. instancia), §2.2 (selector), §5 (modo \(\mathcal M\)), §6 (construcción congelada) |
| \(C_N\) familia frente a instancia | A, AH, P | §2.1 |
| Detector ausente de la firma | A, AH | §2.2, \(d\) en todas las firmas |
| \(t\) sin sentido intrínseco en un poset | A, AH, P | §2.2: reloj de pasos, \(t=k/\lambda\) con \(\lambda\) de orden |
| `FAIL` trivial por futuro vacío o cono de un paso | AH (futuro vacío); A (N=2, sin sitio para la inclusión estricta) | NT4 |
| \(D_1=D_2\) permitido | A, AH | NT3, control negativo |
| \(q\) sobre la curva entera vacía §3 | AH | §4: \(Q=\tau\) fijo |
| \(\mathcal R_{\rm IR}\) recibía dos escalares, contra «único escalar» | AH | §5: sólo \(Q\) |
| Ínfimo continuo con malla sin interpolación definida | AH | §3: reloj discreto, mínimo |
| \(\Delta\) no monótona | AH (parcial) | §2.4(1) |
| Paréntesis rotos en fórmulas (\((N)\), \((D_1,D_2)\)…) | — | corregidos |

(Las referencias de sección de esta tabla son las de la v2, `505ac49`.)

### 11.2 v2 → v2.1

Revisión: `revisiones/2026-10-14-argon-high-delta-v2/` (AD); evaluación en su `evaluacion.md`.

| Defecto de v2 | Señalado por | Cambio en v2.1 |
|---|---|---|
| `PASS` trivial: dinámicas iguales hasta cruzar \(\theta\), \(Q^{D_1}=Q^{D_2}\) a todo \(N\) (comprobado a mano) | AD | NT2 (todo \(\theta\in\Theta\)), NT3 sobre \(Q\) y no sobre \(\Delta\); control negativo en §9 |
| \(\tau^{\rm IR}_{\rm caus}=0\) en posets densos: pérdida estricta gratis (`[UNVERIFIED]`) | AD; previsto en la expectativa previa | ADM4 |
| Cono degenerado o \(A\) desconectado daba `FAIL` en vez de excluir | AD | §6 admisibilidad, `INADMISSIBLE` en §1 |
| Modo c.s. sin acoplamiento entre \(N\); modo «esperanza» mal definido | AD | §5: sólo en probabilidad, comparación por realización |
| Límites constantes excluyen un límite aleatorio común | AD | §5, §7: diferencias por realización; límite constante como caso particular |
| Selector equivariante determinista inexistente con automorfismos | AD | §2.2: selector aleatorizado, equivariante en ley |
| «Sin par» dejaba \(Q\) fuera de dominio | AD | §4: \(Q\) definido en el suceso «hay par»; ADM1 |
| \(D\) no recibía \(d\) aunque se decía que lo compartía | AD | §2.3: \(d\) pasivo, la dinámica no lo recibe; sólo entra en \(\Delta\) |
| \(A\) sin equivariancia, con bloqueos, sin conexión | AD | §2.2 (equivariante, sin bloqueos), ADM3 |
| Codominio de \(\lambda\) sin fijar; \(\min\emptyset\) en \(\tau_{\rm caus}\) sin declarar; \(k\ge0\) ambiguo | AD | §2.2, §5 |
| \([\infty,\infty)=\emptyset\) llamado semirrecta; equivalencia de §6 sólo bajo NT1 | AD | §5: semirrectas «bajo §6 y §8» |
| NT2/NT3 con argumentos «·» | AD | NT1–NT3 con \(\theta\), \(\sigma_N(C_N)\) explícitos |

Decisiones de v2.1 que **no** vienen de las revisiones y que la revisión del delta debe
atacar: exigir el test para **todo** \(\theta\) de un intervalo \(\Theta\) (AD lo sugiere
como alternativa, la v2.1 lo hace obligatorio); medir la pérdida estricta con un margen
\(\varepsilon\) por realización; tratar ADM4 como precondición y no como cláusula del test;
que la dinámica no reciba \(d\).

**Hueco conocido, sin cerrar:** si \(D_2\) es \(D_1\) con un retraso fijo de \(O(1)\) pasos,
\(Q^{D_2}_\theta=Q^{D_1}_\theta+O(1/\lambda)\) para todo \(\theta\): NT3 se cumple, el punto 1
de §7 también, y la igualdad IR no dice nada. La v2.1 no lo excluye; la propuesta de AD
(«diferencia no atribuible a un retraso de \(O(1)\) pasos») es vaga. Queda para la revisión.

Se mantienen de la v2: \(\Delta\) monótona con valores en
\([0,1]\) y cono definido por \(A\).

El siguiente paso autorizado es revisar el delta v2→v2.1, fijar la relevancia para 3+1D y
congelar. Sólo entonces se formaliza el control de contrato de §9. El estado actual de ambas
partes del test es `OPEN`.
