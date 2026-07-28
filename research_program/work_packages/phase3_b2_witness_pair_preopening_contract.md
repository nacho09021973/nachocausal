# Fase 3 B2 — contrato de preapertura para pares testigo

> **STATUS: PHASE_3_B2_PREOPENING_CONTRACT_READY / WORK_DATE_2026-07-29 /
> TARGET_NOT_ADOPTED / SCIENTIFIC_EXECUTION_NOT_OPENED / NO_CODE / NO_SIMULATION /
> NO_SEEDS / NO_THRESHOLD / NO_FREEZE / DOES_NOT_TOUCH_SEAL.**
>
> Documento de trabajo revisable. Prepara una única adjudicación científica para el
> 29 de julio de 2026; no presenta un teorema, no adopta todavía un target y no
> autoriza una construcción numérica.

## 0. Por qué B2 puede prepararse ahora

Se cumplen los gates documentales de `tarea_grok_2.md`:

1. Fase 1 tiene manuscript interno completo, PI review OK, polish y number audit;
2. las enmiendas posteriores a la revisión externa están aplicadas;
3. Fase 2 e ítem 5 están cerrados sin certificado de novedad;
4. R1 sigue vigente: no se reabre el norte de localizadores order-only de horizonte
   Schwarzschild 3+1;
5. el PI eligió B2 como bifurcación preferida.

Esto permite **preparar** B2. La adopción del target y la apertura del trabajo
matemático siguen siendo pasos separados.

## 1. Pregunta única del 29 de julio

> ¿Es admisible como primer target B2 el funcional binario intrínseco
> \(Q_{\mathrm{FMOTS}}\), y existe una ruta no trivial —con regularidad y canal
> explícitos— para construir un par conforme estilo Müller que cambie
> \(Q_{\mathrm{FMOTS}}\) mientras mantenga próximas las leyes de posets a
> cardinalidad fija?

El resultado de la sesión debe ser una de estas dos cosas:

- una **ficha de target admitida para construcción matemática**, con todas las
  obligaciones de §7 cerradas; o
- un **bloqueo tipado** que explique por qué este target no sirve.

No se pasa a “buscar otro observable” durante la misma sesión.

## 2. Target candidato recomendado

### 2.1 Definición provisional

Sea \(U\) un parche compacto, temporalmente orientado y causalmente convexo de una
variedad Lorentziana \(3{+}1\). Para una clase intrínseca y previamente cerrada
\(\mathcal S_{\mathrm{adm}}(g,U)\) de superficies espaciales compactas, cerradas y
de codimensión dos, se propone

\[
Q_{\mathrm{FMOTS}}(g,U)
=
\mathbf 1\!\left\{
\exists S\in\mathcal S_{\mathrm{adm}}(g,U):
\theta_+^g(S)=0,\ \theta_-^g(S)<0
\right\}.
\]

Aquí `FMOTS` nombra explícitamente la convención más estrecha usada en la
fórmula: marginal exterior \(\theta_+=0\) y future trapped hacia dentro
\(\theta_-<0\). La terminología y la normalización de los nulos forman parte de
la adjudicación, no se heredan de forma implícita.

Es un target:

- **binario y adimensional**;
- **cuasi-local**, no el horizonte de eventos global;
- de **existencia/clasificación**, no de localización de una región;
- definido sobre la completación geométrica latente, no sobre un estimador.

### 2.2 Punto que debe cerrarse antes de adoptarlo

\(\mathcal S_{\mathrm{adm}}(g,U)\) no puede ser “la superficie \(S\) que nosotros
marcamos” ni una familia definida por coordenadas ocultas. Debe especificarse de
forma difeomorfismo-invariante, con orientación exterior y condiciones de borde
cerradas. Si esto no puede hacerse sin importar una etiqueta externa, se emite
`B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`.

### 2.3 Lo que este target no es

- no es \(T_{\mathrm{EH}}\);
- no es la pantalla combinatoria `W(p,q)` de C6;
- no es un mapa `Min(C) -> región`;
- no es una reedición de C1–C6;
- no presupone que un MOTS sea reconstruible;
- no convierte una obstrucción finita en no-go asintótico.

## 3. Familia candidata para el par testigo

La ruta preferida a auditar es una familia conforme:

\[
g_\omega=e^{2\omega}g_0,
\qquad
\omega\in C_c^k(U),
\]

con el mismo \(U\), orientación temporal y condiciones de borde.

Antes de adoptar la familia deben fijarse:

| Objeto | Obligación |
|---|---|
| Dimensión | \(3{+}1\), sin transferir resultados 1+1 |
| Regularidad | un \(k\) y un presupuesto uniforme explícito; no ocultar curvatura creciente |
| Parche | compacto y causalmente convexo |
| Bordes | mismos datos de borde o diferencia declarada |
| Clase métrica | no degenerada; firma Lorentziana preservada |
| Equivalencias | difeomorfismos y reparametrizaciones que no cuentan como cambio de target |
| Target | \(Q_{\mathrm{FMOTS}}\) definido intrínsecamente |

La motivación es estructural: una transformación conforme preserva los conos y
la relación causal del continuo, mientras cambia el elemento de volumen y puede
cambiar las expansiones nulas. **Esta frase es una ruta de prueba, no una prueba.**
La ley de transformación de \(\theta_\pm\), sus convenciones de normalización y
la existencia/no existencia del MOTS deben derivarse o anclarse a fuente primaria
antes de afirmar separación del target.

## 4. Canal y régimen estadístico

### 4.1 Canal primario

```text
CHANNEL = ORDER_ONLY_CONDITIONED_ON_N
OBSERVATION = ISOMORPHISM_CLASS_OF_UNLABELED_FINITE_POSET
SAMPLING = N_IID_POINTS_FROM_NORMALIZED_VOLUME_ON_U
COORDINATES = FORGOTTEN
EMBEDDING_LABELS = FORGOTTEN
CARDINALITY = CONDITIONED_TO_N_EQ_n
```

Para \(g_i\), sea \(\mu_i\) la medida de volumen normalizada en \(U\), y
\(P_{i,n}\) la ley del poset no etiquetado inducido por \(n\) puntos.

### 4.2 Cadena de distancia que debe demostrarse

La prueba debe escribir, con sus hipótesis:

\[
\operatorname{TV}(P_{0,n},P_{1,n})
\le
\operatorname{TV}(\mu_0^{\otimes n},\mu_1^{\otimes n})
\le
1-\bigl(1-\operatorname{TV}(\mu_0,\mu_1)\bigr)^n
\le
n\,\operatorname{TV}(\mu_0,\mu_1).
\]

- la primera desigualdad es data processing bajo el mapa
  muestra \(\to\) poset;
- las dos restantes deben probarse o citarse con el alcance exacto;
- no se declarará `TV=0` salvo igualdad real de las medidas inducidas;
- una cota en el nivel de puntos es solo una cota superior para el canal poset.

### 4.3 Régimen permitido

El primer resultado puede ser únicamente:

```text
FIXED_n_OR_ANNOUNCED_FINITE_n_RANGE
TWO_POINT_MINIMAX_LOWER_BOUND
POSSIBLY_n_DEPENDENT_WITNESS_PAIR
```

Si el soporte del bump, su amplitud o sus derivadas dependen de \(n\), esa
dependencia debe aparecer en el enunciado. Si la regularidad empeora con \(n\),
queda prohibido vender el resultado como obstrucción uniforme sobre una clase
física regular.

## 5. Relación obligatoria con Müller

La construcción debe presentarse como una adaptación explícita, no como una
invención ex nihilo.

| Componente | Müller 2025 | B2 propuesto |
|---|---|---|
| Mecanismo | perturbación geométrica de soporte pequeño | candidato conforme de soporte pequeño |
| Canal | causal sets finitos / distancia entre leyes | order-only a \(N=n\) |
| Target | cantidad geométrica continua de su teorema | existencia MOTS, si queda bien definida |
| Cota | precursor cuantitativo, incluido Thm 3 | cadena TV + lema de dos puntos |
| Hueco real | no debe minimizarse | demostrar cambio de target cuasi-local bajo clase regular |

El trabajo se detiene con `B2_REDUNDANT_WITH_MULLER` si, tras igualar hipótesis,
target y régimen, el supuesto nuevo resultado ya está contenido en su teorema.
Una técnica conocida con target nuevo se describirá como **instanciación/adaptación
acotada**, no como método nuevo.

## 6. Ataques falsadores que deben intentarse primero

1. **Etiqueta externa.** El target cambia solo porque el modelo trae una
   superficie marcada que el canal no observa.
2. **Cambio vacío.** \(g_0\) y \(g_1\) son difeomorfos dentro de la clase y
   \(Q\) no cambia en realidad.
3. **Regularidad degenerada.** Hacer pequeño el soporte fuerza derivadas o
   curvaturas sin cota.
4. **Borde responsable.** El MOTS aparece por cambiar condiciones de borde, no
   por la perturbación interior declarada.
5. **No existencia inicial no probada.** Se construye un MOTS para \(g_1\), pero
   nunca se demuestra que \(Q(g_0,U)=0\).
6. **Cota solo puntual.** Se demuestra cercanía de densidades en coordenadas,
   no de medidas normalizadas ni de leyes de posets.
7. **Asintótica inflada.** Un par dependiente de \(n\) se presenta como un par
   fijo indistinguible cuando \(n\to\infty\).
8. **C1–C6 bajo otro nombre.** Se empieza a diseñar una regla que localice la
   superficie desde `C`; eso queda fuera de B2.

## 7. Gates de admisión del target

Todos son acumulativos:

| ID | Gate | Evidencia mínima |
|---|---|---|
| G1 | Target intrínseco y difeomorfismo-invariante | definición cerrada de \(\mathcal S_{\mathrm{adm}}\) |
| G2 | No global / no teleológico | prueba de que \(Q\neq T_{\mathrm{EH}}\) por definición |
| G3 | No localizador | output binario/funcional, sin mapa a región |
| G4 | Familia cerrada | \(U\), regularidad, bordes, equivalencias y sampling |
| G5 | Separación real | argumento \(Q(g_0,U)\neq Q(g_1,U)\) |
| G6 | Cercanía estadística | cadena TV con constantes y régimen |
| G7 | No trivialidad | diferencia no introducida por etiqueta externa |
| G8 | Prior art | comparación literal con Müller Thm 2–3 y vecinos |
| G9 | Claim ceiling | fixed-\(n\), tasa o alcance asintótico escrito sin promoción |

Fallar cualquier gate impide abrir la construcción matemática bajo este target.

## 8. Entregables exactos para el 29 de julio

La sesión prepara, en este orden:

1. **Ficha Q** de una página: objeto, dominio, invariancias, equivalencias y
   por qué no es EH/localizador.
2. **Proposición candidata** de no más de diez líneas con cuantificadores,
   régimen y claim ceiling.
3. **Tabla del par** \(g_0,g_1\): lo idéntico, lo diferente y lo que debe probarse.
4. **Cadena TV** completa: medida de un punto, producto y data processing.
5. **Ledger de fuentes**: Müller Thm 2–3; transformación conforme de expansiones;
   existencia/no existencia de MOTS en la clase elegida.
6. **Ataque falsador** contra G1, G3, G5 y G7.
7. **Terminal único** de §9.

No se escribe código, no se construyen datos y no se reserva una banda de seeds.

## 9. Terminales de la primera sesión

En orden de precedencia:

```text
B2_BLOCKED_TARGET_NOT_INTRINSIC
B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL
B2_BLOCKED_NO_MATCHED_COMPLETION_FAMILY
B2_BLOCKED_REGULARITY_DEGENERATES
B2_BLOCKED_TARGET_SEPARATION_NOT_PROVED
B2_BLOCKED_NO_SMALL_TV_ROUTE
B2_REDUNDANT_WITH_MULLER
B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION
```

`B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION` autoriza únicamente completar
la prueba matemática del par. No autoriza simulación, código, estimador,
prerregistro empírico, claim de novedad ni publicación.

## 10. Criterio de éxito y parada de B2

### Éxito mínimo

Un par explícito, en una clase nombrada y regular, con:

\[
Q(g_0,U)\neq Q(g_1,U),
\qquad
\operatorname{TV}(P_{0,n},P_{1,n})\le\varepsilon_n,
\]

y el correspondiente lower bound de dos puntos, todo con claim ceiling finito
y comparación honesta con Müller.

### Parada limpia

B2 se aparca si:

- el primer target no puede definirse intrínsecamente;
- separar \(Q\) exige salir de toda clase regular declarada;
- la medida de volumen hace imposible la cercanía requerida en el régimen útil;
- el resultado es solo una reformulación del precursor;
- la única salida práctica vuelve a diseñar un localizador C1–C6.

Un bloqueo documentado de este target no refuta B2 en general y no prueba
identificabilidad. Solo cierra esta instanciación.

## 11. Estado de autorización

```text
PHASE_3_BRANCH = B2
PREOPENING_CONTRACT = READY_FOR_2026_07_29
PRIMARY_TARGET_CANDIDATE = Q_FMOTS
TARGET_ADOPTION = PENDING_SCIENTIFIC_ADJUDICATION
WITNESS_CONSTRUCTION = NOT_AUTHORIZED_YET
CODE = NOT_AUTHORIZED
SIMULATION = NOT_AUTHORIZED
SEEDS = NOT_AUTHORIZED
THRESHOLDS = NOT_APPLICABLE
SEALED_PATH = UNTOUCHED
COMMIT_OR_PUSH = NOT_AUTHORIZED_BY_THIS_DOCUMENT
```
