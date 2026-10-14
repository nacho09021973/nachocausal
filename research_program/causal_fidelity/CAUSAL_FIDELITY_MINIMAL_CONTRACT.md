# Contrato mínimo de fidelidad causal

> **Estado:** `NEW_FRONT / MINIMAL_CONTRACT / UNPROVED`
> **Fecha:** 2026-09-18
> **Rama:** `research/causal-fidelity-bridge`

Este documento abre un frente nuevo y deliberadamente estrecho. No reutiliza los
artefactos históricos de `research_program/puente_3p1/` ni los controles B1.6/B1.7.
Aquellos quedan como controles negativos históricos: muestran que una separación
estadística puede sobrevivir a un cambio de dimensión u orden sin certificar una
estructura dinámica genuinamente `3+1D`.

El objetivo aquí no es producir otra separación estática, sino comprobar si una
propiedad dinámica inferida del orden causal tiene una relación estrictamente
distinta con el límite infrarrojo.

## 1. Claim ceiling

El único resultado admisible de esta primera unidad será uno de:

- `PASS`: existe una construcción explícita que satisface el test exacto de §6,
  con todas las cuantificaciones y tolerancias fijadas antes de observar los
  resultados;
- `FAIL`: alguna obligación matemática del contrato es imposible o el test
  falla;
- `OPEN`: faltan una definición, una prueba o una verificación que el contrato
  exige.

No se autoriza inferir de un `PASS` que se haya reconstruido la geometría,
demostrado una teoría física, identificado de forma única una dinámica, ni
establecido una firma exclusiva de `3+1D`. Tampoco se autoriza una afirmación de
novedad bibliográfica desde este documento.

## 2. Objetos congelados

### 2.1 Familia causal

Para cada \(N\in\mathbb N\), sea

\[
C_N=(E_N,\prec_N,\mu_N)
\]

una familia de configuraciones causales finitas, donde \(E_N\) es el conjunto de
eventos, \(\prec_N\) el orden causal y \(\mu_N\) la medida o pesos de muestreo
cuando sean necesarios. El canal de entrada de ambos modelos es el mismo
\(C_N\); ninguna coordenada de una realización, ni la verdad geométrica usada
para generarla, puede entrar en el observable.

La familia debe especificar antes de cualquier ejecución:

1. el espacio de realizaciones y su ley de muestreo;
2. el régimen de (N) y cualquier límite de escala;
3. el soporte temporal de las fuentes y detectores;
4. las invariancias de relabeling exigidas al observable;
5. los casos de borde, empates y ausencia de respuesta.

### 2.2 Dos dinámicas

Sean (D_1,D_2) dos dinámicas definidas sobre la misma familia (C_N). Deben
compartir la fuente (s), el protocolo de perturbación, la unidad temporal, el
detector y todos los parámetros declarados comunes. Sólo pueden diferir en el
ingrediente dinámico que el contrato pretende poner a prueba.

No se permite cambiar simultáneamente la familia causal, el soporte, el
muestreo y la dinámica: eso impediría atribuir una diferencia a (D_1\) frente a
\(D_2\).

### 2.3 Respuesta

Para (D\in\{D_1,D_2\}), la respuesta observable es una función escalar

\[
\Delta_D(C_N;s,t),
\]

definida en el dominio temporal congelado. Deben fijarse explícitamente su
normalización, signo, regularidad mínima, valor fuera del cono causal y regla
para respuestas nulas o no finitas. La respuesta sólo puede depender de la
información autorizada por el contrato; el código de evaluación no puede leer
coordenadas ni etiquetas geométricas ocultas.

## 3. Arrival time

Fijados un umbral \(\theta\) y una convención de igualdad, el arrival time de
una fuente \(s\) bajo \(D\) es

\[
\tau_D(C_N;s)
 := \inf\{t\in I_s:\Delta_D(C_N;s,t)\geq\theta\},
\]

con el valor especial `\(\infty\)` si el conjunto es vacío. El intervalo
\(I_s\), la malla o interpolación temporal, la resolución y la tolerancia
numérica deben quedar fijados antes de evaluar \(D_1,D_2\). Si se usa una
definición continua, la implementación deberá certificar cómo aproxima el
ínfimo; si se usa una malla, el resultado sólo podrá llamarse arrival time
discreto.

El arrival time es una salida dinámica. No es, por sí mismo, una coordenada
reconstruida ni una identificación de una superficie causal.

## 4. Único escalar \(Q_s\)

El contrato permite un único escalar IR asociado a la fuente (s):

\[
Q_s^D(C_N):=q\!\left(\tau_D(C_N;s),\Delta_D(C_N;s,\cdot)\right)\in\mathbb R\cup\{\infty\},
\]

donde (q) debe especificarse una sola vez antes de la ejecución. No se
autoriza seleccionar entre varios (Q)'s después de inspeccionar los datos, ni
combinar (Q_s) con un segundo score para decidir el resultado.

La versión mínima recomendada es (q(\tau,\Delta)=\tau), de modo que

\[
Q_s^D(C_N)=\tau_D(C_N;s).
\]

Si se escoge otra (q), el contrato derivado deberá justificar por qué sigue
siendo un único observable escalar y deberá conservar separadas la respuesta
completa, el arrival time y el resumen (Q_s).

## 5. Conjuntos de tiempos

Sea (T_{\rm caus}(C_N;s)) el conjunto de tiempos causalmente admisibles bajo
la convención fijada para (C_N), antes de aplicar la dinámica. Debe definirse
por una regla puramente causal y auditable; no puede definirse a posteriori como
la unión de resultados favorables.

Para cada dinámica, sea

\[
T_{\rm IR}^{D}(C_N;s)
 := \operatorname{IR}\!\left(Q_s^D(C_N),\tau_D(C_N;s);\,\mathcal R_{\rm IR}\right),
\]

donde \(\mathcal R_{\rm IR}\) es una única regla de paso al régimen infrarrojo,
con escala, límite, tolerancia y tratamiento de \(\infty\) congelados antes de
comparar (D_1) y (D_2). La misma regla debe usarse para ambas dinámicas.

La notación (T_{\rm IR}^{D}) no significa automáticamente una propiedad
geométrica ni una observable universal: esas interpretaciones quedan abiertas
hasta una prueba independiente.

## 6. Test exacto

La hipótesis objetivo de este frente es la conjunción exacta

\[
\boxed{
T_{\rm IR}^{D_1}(C_N;s)
=T_{\rm IR}^{D_2}(C_N;s)
\subsetneq
T_{\rm caus}(C_N;s).
}
\]

La evaluación debe separar las dos obligaciones:

1. **igualdad dinámica en IR:** demostrar o certificar, con los cuantificadores
   declarados, que ambos conjuntos son iguales;
2. **pérdida estricta frente al causal:** exhibir al menos un tiempo causal
   admisible que queda fuera del conjunto IR común, y probar la inclusión
   correspondiente.

Una coincidencia numérica en una escalera finita no es una demostración de
igualdad. Una diferencia observada fuera de IR no refuta el test si no se había
congelado que ese régimen pertenecía a la afirmación. Las tolerancias no podrán
ser elegidas después de ver la separación.

## 7. Obligaciones de validación

Antes de cualquier resultado se deberá disponer de:

- definiciones ejecutables de (C_N,D_1,D_2,\Delta,\tau,Q_s,T_{\rm caus}) y
  (\mathcal R_{\rm IR});
- una prueba o certificado de que no hay fuga de coordenadas, etiquetas o
  ground truth en \(Q_s\) ni en la decisión;
- un control de identidad que cambie sólo el ingrediente dinámico;
- un análisis de estabilidad frente a la discretización temporal y los empates;
- un registro de casos nulos, divergentes y fuera de soporte;
- una tabla previa de cuantificadores, tolerancias, tamaños y criterio
  `PASS/FAIL/OPEN`;
- revisión adversarial del test antes de interpretar cualquier coincidencia.

No se ejecuta un experimento confirmatorio ni se crea una segunda familia de
observables hasta cerrar esta unidad mínima.

## 8. Exclusiones explícitas

Este contrato no incorpora:

- `research_program/puente_3p1/` ni B1.5, B1.6 o B1.7;
- los archivos históricos de control negativo;
- `.webui_secret_key`;
- una afirmación de que la igualdad IR sea ya cierta;
- una afirmación de que la inclusión estricta sea universal;
- promoción al estado canónico, publicación o novedad.

El siguiente paso autorizado, una vez revisado este contrato, es formalizar sus
definiciones y buscar un primer caso mínimo. El estado actual de ambas partes
del test es `OPEN`.
