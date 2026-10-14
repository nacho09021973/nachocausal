# Contrato mínimo de fidelidad causal

> **Estado:** `NEW_FRONT / MINIMAL_CONTRACT v2 / DRAFT / UNPROVED`
> **Fecha:** 2026-10-14 (v1: 2026-09-18, congelada en `a77d9d8`)
> **Rama:** `research/causal-fidelity-bridge`
> **v2 no está congelada.** Corrige los defectos que encontraron las revisiones ciegas de la v1
> (`revisiones/2026-10-13-*`). Antes de usarla hace falta revisar el delta v1→v2 (§10).

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

El único resultado admisible de esta primera unidad será uno de:

- `PASS`: existe una construcción explícita, congelada antes de evaluarla, que
  satisface el test de §6 con los cuantificadores de §6 y las cláusulas de no
  trivialidad de §7, con prueba (no sólo evidencia numérica);
- `FAIL`: para la construcción congelada, se prueba que alguna obligación de §6 o §7
  no se cumple. Un `FAIL` es de esa construcción, no un no-go del frente;
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
instancia fija. Una ley determinista (\(\mu_N=\delta_{c_N}\)) está permitida.

La familia debe especificar antes de cualquier ejecución:

1. la ley \(\mu_N\) y qué controla \(N\) (p. ej. \(|E|=N\) o un parámetro de escala);
2. las invariancias de reetiquetado exigidas a todo observable;
3. el tratamiento de las realizaciones sin par fuente–detector admisible (§2.2), que se
   registran como nulas y no se descartan en silencio.

Ninguna coordenada de una realización, ni la verdad geométrica usada para generarla,
puede entrar en un observable. Las cardinalidades y longitudes de cadena sí son
observables legítimas: *blind to the embedding* no significa *count-free*
(`CLAUDE.md`, «order-only»).

### 2.2 Fuente, detector y reloj

- **Par fuente–detector.** Un selector \(\sigma_N\) asigna a cada instancia \(c\) un par
  \((s,d)\in E\times E\) con \(s\prec d\), o «sin par». \(\sigma_N\) se define sólo a
  partir del orden y es equivariante bajo reetiquetado. No hace falta identificar
  \(s,d\) entre distintos \(N\): el paso al IR (§5) se toma sobre escalares, no sobre
  eventos.
- **Movimientos admisibles.** Una regla \(A\), definida sólo a partir del orden, fija
  para cada \(c\) el conjunto de movimientos de un paso permitidos
  \(A(c)\subseteq\{(x,y):x\preceq y\}\) (p. ej. quedarse o avanzar un enlace de Hasse).
  \(A\) es **común** a \(D_1\) y \(D_2\).
- **Reloj.** El tiempo de la dinámica es un número de pasos \(k\in\mathbb N\). El tiempo
  macroscópico es \(t=k/\lambda(c;s,d)\), con una escala \(\lambda\) definida sólo a
  partir del orden (p. ej. la longitud de la cadena más larga de \(s\) a \(d\)) y fijada
  antes de evaluar. \(t\) no es una coordenada reconstruida.

### 2.3 Dos dinámicas

Una dinámica \(D\) asigna a cada \((c,s)\) la ley de un proceso \((X_k)_{k\ge0}\) sobre
\(E\) con \(X_0=s\), cuyas trayectorias usan sólo movimientos de \(A(c)\). El espacio de
dinámicas admisibles se parametriza explícitamente; \(D_1\) y \(D_2\) son dos puntos de
ese espacio que difieren **sólo** en un ingrediente nombrado (p. ej. memoria del
incremento) y comparten \(\mu_N,\sigma_N,A,\lambda\), el detector y el umbral.

No se permite cambiar a la vez la familia causal, el selector, los movimientos
admisibles y la dinámica: eso impediría atribuir una diferencia a \(D_1\) frente a
\(D_2\).

### 2.4 Respuesta

Para cada instancia, la respuesta es una función \(\Delta_D(c;s,d,t)\in[0,1]\) que
cumple:

1. es no decreciente en \(t\);
2. vale \(0\) para \(t<\tau_{\rm caus}(c;s,d)\) (§5): fuera del cono no hay respuesta;
3. depende sólo de \(c\), \(\sigma_N\), \(A\), \(\lambda\) y \(D\).

La elección mínima recomendada es la probabilidad de haber alcanzado el detector:
\(\Delta_D(c;s,d,t)=\mathbb P_D\big(\exists k\le\lfloor t\lambda\rfloor: X_k=d\big)\),
que cumple 1–3 por construcción.

## 3. Arrival time

Fijado un umbral \(\theta\in(0,1)\) antes de evaluar,

\[
\tau_D(c;s,d):=\min\{k/\lambda : \Delta_D(c;s,d,k/\lambda)\ge\theta\}\in[0,\infty],
\]

con \(\tau_D=\infty\) si el conjunto es vacío. Como el reloj es discreto, el mínimo está
bien definido y no hay que aproximar un ínfimo. Es un arrival time **discreto**.

El arrival time es una salida dinámica. No es, por sí mismo, una coordenada
reconstruida ni una identificación de una superficie causal.

## 4. Único escalar \(Q\)

El escalar es \(Q^D(c):=\tau_D(c;\sigma_N(c))\). No se admite otra función \(q\): en la
v1, una \(q\) que recibe la curva \(\Delta_D(\cdot)\) entera deja de ser un resumen y vacía
§3. No se autoriza combinar \(Q\) con un segundo score para decidir el resultado.

## 5. Tiempos causales y tiempos IR

**Cono causal por instancia.** Con los mismos movimientos admisibles \(A\),

\[
\tau_{\rm caus}(c;s,d):=\min\{k/\lambda : \text{existe una trayectoria de } A(c)
\text{ de } s \text{ a } d \text{ en } k \text{ pasos}\}.
\]

Es una regla puramente de orden, fijada antes de la dinámica. Por §2.4(2),
\(\tau_D\ge\tau_{\rm caus}\) en toda instancia.

**Paso al IR.** Antes de comparar se declara un único modo de convergencia \(\mathcal M\)
(casi segura, en probabilidad bajo \(\mu_N\), o de la esperanza), común a todo lo que
sigue. Se definen

\[
\tau^{\rm IR}_D:=\lim_{N\to\infty}Q^D(C_N),\qquad
\tau^{\rm IR}_{\rm caus}:=\lim_{N\to\infty}\tau_{\rm caus}(C_N;\sigma_N(C_N)),
\]

ambos límites en el modo \(\mathcal M\), y se exige que sean **constantes** en
\([0,\infty]\). Si un límite no existe o es aleatorio, el resultado es `OPEN` (o `FAIL`
si se prueba que no existe). \(N\) queda ligada por el límite: ningún objeto IR depende
de \(N\).

**Conjuntos, en la misma álgebra.** Ambos son semirrectas cerradas de \([0,\infty)\):

\[
T^D_{\rm IR}:=[\tau^{\rm IR}_D,\infty),\qquad
T_{\rm caus}:=[\tau^{\rm IR}_{\rm caus},\infty).
\]

Comparar un punto aislado con una semirrecta queda excluido por tipo.

La notación \(T^D_{\rm IR}\) no significa automáticamente una propiedad geométrica ni una
observable universal: esas interpretaciones quedan abiertas hasta una prueba independiente.

## 6. Test exacto

Para una construcción \((\mu_N,\sigma_N,A,\lambda,D_1,D_2,\theta,\mathcal M)\)
congelada antes de evaluar, la hipótesis objetivo es

\[
\boxed{
T^{D_1}_{\rm IR}=T^{D_2}_{\rm IR}\subsetneq T_{\rm caus}
}
\quad\Longleftrightarrow\quad
\tau^{\rm IR}_{D_1}=\tau^{\rm IR}_{D_2}>\tau^{\rm IR}_{\rm caus}.
\]

La equivalencia vale porque los tres conjuntos son semirrectas de \([0,\infty)\). La
evaluación separa las dos obligaciones:

1. **igualdad dinámica en IR:** probar que ambos límites existen en el modo
   \(\mathcal M\) y coinciden;
2. **pérdida estricta frente al causal:** probar \(\tau^{\rm IR}_{\rm caus}<\tau^{\rm IR}_{D_i}\),
   es decir, exhibir los tiempos \(t\in[\tau^{\rm IR}_{\rm caus},\tau^{\rm IR}_{D_i})\)
   causalmente admisibles y fuera del conjunto IR común.

Una coincidencia numérica en una escalera finita de \(N\) no es una demostración de
igualdad. Las tolerancias, si las hay, se fijan antes de ver la separación.

## 7. Cláusulas de no trivialidad

Un `PASS` exige además, con prueba:

- **NT1 — no vacuidad.** \(\tau^{\rm IR}_{D_1},\tau^{\rm IR}_{D_2},\tau^{\rm IR}_{\rm caus}<\infty\).
  Excluye el `PASS` \(\emptyset=\emptyset\subsetneq T_{\rm caus}\) por umbral inalcanzable
  (las tres revisiones lo construyen).
- **NT2 — umbral no degenerado.** \(\theta\in(0,1)\) fijo, y para cada \(D_i\) existe
  \(t\) con \(\lim_N\Delta_{D_i}(C_N;\cdot,t)>\theta\) en el modo \(\mathcal M\). Excluye
  que \(\tau_D\) colapse a \(\infty\) o al primer paso por elección del umbral.
- **NT3 — no identidad microscópica.** Para todo \(N\) suficientemente grande, las leyes
  de \(\Delta_{D_1}(C_N;\cdot)\) y \(\Delta_{D_2}(C_N;\cdot)\) difieren, y esa diferencia
  se **prueba**, no se afirma. Excluye \(D_1=D_2\).
- **NT4 — cono no degenerado.** Con probabilidad que tiende a 1 bajo \(\mu_N\), \(\sigma_N\)
  devuelve un par y \(\lambda\to\infty\). Excluye el `FAIL` trivial por futuro causal vacío
  (anticadena, \(s\) maximal) y los casos de un solo paso.
- **NT5 — la regla IR no se elige por la dinámica.** \(\lambda\), \(A\), \(\mathcal M\) y
  \(\theta\) no dependen de \(D\). Excluye una regla constante o ajustada a mano.  (P pide una cláusula equivalente.)

## 8. Obligaciones de validación

Antes de cualquier resultado se deberá disponer de:

- definiciones ejecutables de \(\mu_N,\sigma_N,A,\lambda,D_1,D_2,\Delta,\tau,\tau_{\rm caus}\);
- una prueba o certificado de que no hay fuga de coordenadas, etiquetas o ground truth
  en \(Q\) ni en la decisión;
- **control negativo:** \(D_1=D_2\) debe ser rechazado por NT3;
- **control de contrato:** una construcción conocida que el contrato admita como `PASS`
  con contenido, para comprobar que el test no es vacío por construcción. Candidata
  `[UNVERIFIED]`: cadena lineal, paseo i.i.d. frente a paseo con memoria markoviana de
  igual deriva \(p<1\) (propuesta en `revisiones/2026-10-13-argon-high-contrato/`). Es un
  ejemplo de límite hidrodinámico conocido: valida el contrato, **no** es un resultado
  del frente, y su NT3 está afirmado sin prueba en la revisión;
- un registro de realizaciones nulas, de \(\tau=\infty\) y de pares ausentes;
- una tabla previa de cuantificadores, modo \(\mathcal M\), tamaños y criterio
  `PASS/FAIL/OPEN`;
- revisión adversarial del test antes de interpretar cualquier coincidencia.

No se ejecuta un experimento confirmatorio ni se crea una segunda familia de
observables hasta cerrar esta unidad mínima.

## 9. Exclusiones explícitas

Este contrato no incorpora:

- `research_program/puente_3p1/` ni B1.5, B1.6 o B1.7;
- los archivos históricos de control negativo;
- `.webui_secret_key`;
- una afirmación de que la igualdad IR sea ya cierta;
- una afirmación de que la inclusión estricta sea universal;
- promoción al estado canónico, publicación o novedad.

## 10. Cambios respecto a v1 y trazabilidad

Revisiones: `revisiones/2026-10-13-argon-contrato/` (A), `…-argon-high-contrato/` (AH),
`…-pro31-contrato/` (P). Ninguna afirmación de esas revisiones se adopta sin comprobarla
aquí; lo que se adopta son los defectos señalados, que se comprueban leyendo la v1.

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

Decisiones de v2 que **no** vienen de las revisiones y que la revisión del delta debe
atacar: restringir \(\Delta\) a respuestas monótonas con valores en \([0,1]\); definir el
cono por los movimientos admisibles \(A\) (y no por la cadena más corta del diagrama de
Hasse, que en posets densos no mide nada útil `[UNVERIFIED]`); exigir límites
constantes.

El siguiente paso autorizado es revisar el delta v1→v2 (`git diff a77d9d8 --
CAUSAL_FIDELITY_MINIMAL_CONTRACT.md`), fijar la relevancia para 3+1D y congelar la v2.
Sólo entonces se formaliza el control de contrato de §8. El estado actual de ambas
partes del test es `OPEN`.
