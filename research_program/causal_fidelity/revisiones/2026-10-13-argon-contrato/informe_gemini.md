<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 6d7ba21c9bde4a78e13bedee91d56d0c09fbc8b5; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 5d0238617a33304b24407be0bd817fe5cd2ec3938fbc3a696e5bb8ee0a4ff965; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 28bcaef78f6477cb70f77b3e199bc53226ea79810cd11fe06d96aa36d3527a0c
inicio: 2026-10-13T16:40:46Z  fin: 2026-10-13T16:41:29Z
documento: /home/ignac/nachocausal/research_program/causal_fidelity/CAUSAL_FIDELITY_MINIMAL_CONTRACT.md ; último commit observado: sin versionar ; sha256 de la copia enviada ba99fcb5ed7cbc160cca29b35c57120ad17f8618ed144192e1598831f8442957
entrada_gemini.txt sha256 430db67671f19a0bfbc1c7f61701c9c7f1b57067476ddea0a78836fb2036e7cf
respuesta sha256 db156d38e6a618a59655d4f0dd07cd77e092a215fc0e78ad5337100fc2b3ccbc
-->

Como revisor matemático adversarial, presento la auditoría formal del documento `CAUSAL_FIDELITY_MINIMAL_CONTRACT.md`. Distingo explícitamente entre **Demostración** (deducción lógica directa de las definiciones del texto), **Diagnóstico de tipado** (errores formales en el contrato) y **Construcción/Propuesta**.

---

### 1. ¿Está bien planteado el test de §6? Auditoría de tipos y cuantificadores

**Diagnóstico global:** **NO.** El test de §6 está **mal tipado y sub-especificado**. Contiene colisiones de tipos entre escalares y conjuntos, variables libres sin cuantificar ($N, s$, realizaciones aleatorias) y una contradicción estructural entre la noción de "límite infrarrojo" ($N\to\infty$) y la dependencia explícita de un $N$ fijo en la ecuación de §6.

A continuación se audita cada objeto:

1. **$C_N = (E_N, \prec_N, \mu_N)$ [Ambiguo / Cuantificador ausente]:**
   * *Problema de tipo:* §2.1 oscila entre definir $C_N$ como una realización fija (donde $\mu_N$ es un peso sobre $E_N$) y una "familia de configuraciones" con un "espacio de realizaciones y su ley de muestreo". Si $C_N$ es aleatorio, todo objeto derivado ($\Delta_D, \tau_D, Q_s^D, T_{\rm IR}^D$) es una variable aleatoria, pero §6 compara conjuntos deterministas sin especificar si la igualdad es casi segura (a.s.), en probabilidad, o sobre esperanzas.
   * *Relación de orden:* No se especifica si $\prec_N$ es irreflexiva o reflexiva (afecta a longitudes de cadenas en $t=0$).

2. **Fuente $s$ y Detector [Mal tipados / Argumentos ocultos]:**
   * *Problema de tipo:* No se declara el tipo de $s$ (¿$s \in E_N$? ¿$s \subset E_N$?). En §2.2 se menciona "el detector" en singular, pero este no aparece como argumento en $\Delta_D(C_N; s, t)$ ni en $\tau_D(C_N; s)$.
   * *Fuga de coordenadas en el tiempo $t$:* Un conjunto causal puro $(E_N, \prec_N)$ carece de reloj global $t \in \mathbb{R}$ sin introducir etiquetas geométricas prohibidas por §2.1. Para que $t$ sea intrínseco y auditable, debe ser un funcional de orden respecto a un evento detector $x \in E_N$ (p. ej., longitud de cadena entre $s$ y $x$), o bien $t$ indexa los propios eventos detectores ($t \in E_N$). El contrato no define qué es $t$.

3. **$D_1, D_2$ y $\Delta_D(C_N; s, t)$ [Sub-especificados]:**
   * *Tipo:* $\Delta_D: \mathcal{C}_N \times S \times I_s \to \mathbb{R} \cup \{\text{NaN}, \pm\infty\}$.
   * *Defecto:* No se exige que $D_1 \neq D_2$ en el nivel microscópico, lo que permite dinámicas idénticas.

4. **$\tau_D(C_N; s)$ y $Q_s^D(C_N)$ [Bien tipados como escalares, pero colisionan con §5]:**
   * *Tipos:* $\tau_D(C_N; s) \in I_s \cup \{\infty\} \subset \mathbb{R} \cup \{\infty\}$, y $Q_s^D(C_N) \in \mathbb{R} \cup \{\infty\}$.
   * *Defecto grave:* Para $C_N$ y $s$ fijos, $\tau_D$ y $Q_s^D$ son **un único punto** (un escalar), no una familia de tiempos ni una distribución.

5. **$T_{\rm caus}(C_N; s)$, $T_{\rm IR}^D(C_N; s)$ y la regla $\mathcal{R}_{\rm IR}$ [Error grave de tipos y firma]:**
   * *Error de firma (Infrarrojo vs. $N$ finito):* En física matemática, el régimen infrarrojo (IR) es un límite de gran escala ($N \to \infty$ o reescalado asintótico). Sin embargo, en §5 la firma es $T_{\rm IR}^D(C_N; s) := \operatorname{IR}(Q_s^D(C_N), \tau_D(C_N; s); \mathcal{R}_{\rm IR})$ para un **$C_N$ fijo**, y la ecuación de §6 retiene $C_N$ como argumento libre. Una función evaluada en un único $N$ finito no puede calcular un límite $N \to \infty$.
   * *Incompatibilidad escalar-conjunto:* Si $Q_s^D(C_N)$ y $\tau_D(C_N; s)$ son dos escalares en $\mathbb{R}\cup\{\infty\}$, entonces $\operatorname{IR}(\cdot, \cdot; \mathcal{R}_{\rm IR})$ es simplemente una aplicación de $(\mathbb{R}\cup\{\infty\})^2$ en el conjunto potencia $\mathcal{P}(I_s)$. Si en la versión recomendada $Q_s^D = \tau_D$, entonces $T_{\rm IR}^D$ es el resultado de aplicar una función fija a un único número real.

6. **Cuantificadores en §6 [Ausentes]:**
   En $T_{\rm IR}^{D_1}(C_N;s) = T_{\rm IR}^{D_2}(C_N;s) \subsetneq T_{\rm caus}(C_N;s)$, no se declara si esto debe cumplirse $\forall N \ge N_0$, en el límite $N\to\infty$, $\forall s \in S_N$ o $\exists s \in S_N$.

---

### 2. Trivialidad y vacuidad del test

**Demostración:** El contrato actual permite tanto un `PASS` completamente trivial/vacío como un `FAIL` trivial, sin violar ninguna regla de §1–§7.

#### A. Construcción explícita de `PASS` trivial (Colapso por umbral / Regla IR degenerada)
1. **Familia causal:** Para cualquier $N \ge 2$, sea $C_N$ una cadena total determinista de $N$ elementos: $E_N = \{e_1, \dots, e_N\}$ con $e_1 \prec_N e_2 \prec_N \dots \prec_N e_N$ y pesos $\mu_N \equiv 1$. Fuente $s = e_1$.
2. **Tiempos causales:** Definimos el tiempo intrínseco $t \in I_s = \{1, 2, \dots, N-1\}$ como la distancia de orden desde $s$ (es decir, el evento $e_{t+1}$ está a tiempo $t$). Todos son causalmente admisibles: $T_{\rm caus}(C_N; s) = \{1, 2, \dots, N-1\}$ (no vacío para $N \ge 2$).
3. **Dinámicas y Respuestas:** Fijamos el umbral $\theta = 2$.
   * $D_1$ propaga amortiguado: $\Delta_{D_1}(C_N; s, t) = 2^{-t}$.
   * $D_2$ propaga constante sub-umbral: $\Delta_{D_2}(C_N; s, t) = 1$.
   *(Ambas son no nulas, difieren sólo en la ley dinámica sobre el cono causal, y son cero fuera de él).*
4. **Arrival time y Escalar:** Como $\Delta_{D_i} < \theta = 2$ para todo $t \in I_s$, ambos conjuntos de llegada son vacíos:
   $$\tau_{D_1}(C_N; s) = \tau_{D_2}(C_N; s) = \infty, \quad Q_s^{D_1}(C_N) = Q_s^{D_2}(C_N) = \infty.$$
5. **Regla IR:** Definimos $\mathcal{R}_{\rm IR}$ como la proyección del arrival time al conjunto de tiempos finitos alcanzados: $\operatorname{IR}(Q, \tau) := \{\tau\} \cap \mathbb{R}$.
6. **Evaluación de §6:**
   $$T_{\rm IR}^{D_1}(C_N; s) = \emptyset = T_{\rm IR}^{D_2}(C_N; s) \subsetneq \{1, \dots, N-1\} = T_{\rm caus}(C_N; s).$$
   ¡El test hace `PASS` de forma exacta para todo $N \ge 2$ sin que ninguna señal haya llegado jamás al detector! *(Nota: incluso si se prohibiera $\tau_D = \infty$, elegir $\mathcal{R}_{\rm IR}$ como una función constante $\operatorname{IR}(Q,\tau) = \{1\}$ para $N \ge 3$, o elegir $D_1 = D_2$, produce el mismo `PASS` espurio).*

#### B. Construcción explícita de `FAIL` trivial
En la misma cadena $C_N$ con $N=2$, $T_{\rm caus}(C_2; s) = \{1\}$. Si $\theta = 1/2$, entonces $\tau_{D_1} = \tau_{D_2} = 1$. Con $\operatorname{IR}(Q,\tau) = \{\tau\}$, obtenemos $T_{\rm IR}^{D_1} = T_{\rm IR}^{D_2} = \{1\} = T_{\rm caus}$, violando la inclusión estricta ($\subsetneq$) por falta de espacio de estados en $T_{\rm caus}$.

#### C. Cláusulas que deben añadirse al contrato para impedirlo
1. **No vacuidad y finitud:** Exigir $\tau_D(C_N; s) < \infty$ (con probabilidad $\ge 1-\epsilon_N$) y $\emptyset \neq T_{\rm IR}^D \subsetneq T_{\rm caus}$ (lo que obliga a $|T_{\rm caus}| \ge 2$).
2. **Separación microscópica (No degeneración de $D_1, D_2$):** Exigir que exista un régimen pre-IR (o al menos un $t \in I_s$) donde $\Delta_{D_1}(C_N; s, t) \neq \Delta_{D_2}(C_N; s, t)$, e idealmente que la distribución o valor de $\tau_{D_1}$ y $\tau_{D_2}$ difieran para $N$ pequeño o para umbrales de alta resolución, convergiendo sólo tras aplicar $\mathcal{R}_{\rm IR}$.
3. **Inyectividad / Fidelidad de $\mathcal{R}_{\rm IR}$:** Prohibir que $\operatorname{IR}(\cdot)$ sea una aplicación constante o contractiva artificial; debe ser el conjunto de tiempos admisibles a partir del umbral asintótico reescalado $\tau_D$.

---

### 3. Caso mínimo no trivial con contenido matemático

Para que el test tenga contenido real (distinguir propagación balística/borde del cono frente a retardos internos sin usar coordenadas), corrijo implícitamente el tipado de $t$ como longitud de cadena causal y defino el conjunto IR como la clausura de tiempos alcanzables a partir de $\tau_D$.

#### Definición del caso mínimo ("Diamante Causal con Camino Lento y Camino Rápido", $N=4$)
* **Configuración causal $C_4$:** Conjunto determinista de $N=4$ eventos $E_4 = \{s, a, b, x\}$ con el orden parcial estricto generado por las relaciones de recubrimiento:
  $$s \prec a \prec x, \qquad s \prec b \prec x, \qquad a \prec b.$$
  *(Es decir, existen dos caminos dirigidos maximales o cadenas de $s$ a $x$: el camino directo $s \prec a \prec x$ de longitud $2$, y el camino desviado $s \prec a \prec b \prec x$ de longitud $3$. Pesos $\mu_4 \equiv 1$).*
* **Fuente y Detector:** Fuente $s$, detector fijo $x$.
* **Reloj intrínseco $t$ y $T_{\rm caus}$:** Una señal que viaja de $s$ a $x$ a lo largo de una cadena causal $s = e_0 \prec e_1 \prec \dots \prec e_k = x$ tarda un tiempo intrínseco igual a la longitud $k$ de la cadena. Por tanto, el conjunto de tiempos de llegada causalmente admisibles en $x$ desde $s$ es el conjunto de longitudes de todas las cadenas dirigidas de $s$ a $x$:
  $$T_{\rm caus}(C_4; s) = \{2, 3\} \subset I_s = \{1, 2, 3\}.$$
* **Dos dinámicas ($D_1$: Balística con disipación; $D_2$: Difusiva / Promedio de caminos):**
  Una perturbación unitaria en $s$ en $t=0$ induce en $x$ a tiempo $t$ la suma sobre cadenas de longitud $t$:
  * En $D_1$, cada salto atenúa la amplitud por un factor $\alpha \in (0,1)$: $\Delta_{D_1}(C_4; s, t) = \sum_{\text{cadenas } \gamma: |\gamma|=t} \alpha^t$. Como hay exactamente una cadena de longitud $2$ ($s\prec a\prec x$) y una de longitud $3$ ($s\prec a\prec b\prec x$), tenemos:
    $$\Delta_{D_1}(C_4; s, 1) = 0, \quad \Delta_{D_1}(C_4; s, 2) = \alpha^2, \quad \Delta_{D_1}(C_4; s, 3) = \alpha^3.$$
  * En $D_2$ (modelo de caminante aleatorio causal sobre el DAG), la probabilidad se divide equitativamente entre las aristas salientes directas del grafo de Hasse ($s$ tiene aristas a $a,b$; $a$ tiene aristas a $b,x$; $b$ tiene arista a $x$). Las respuestas en $x$ por longitud de camino son:
    $$\Delta_{D_2}(C_4; s, 1) = 0, \quad \Delta_{D_2}(C_4; s, 2) = \tfrac{1}{2}\cdot\tfrac{1}{2} + \tfrac{1}{2}\cdot 1 = \tfrac{3}{4}, \quad \Delta_{D_2}(C_4; s, 3) = \tfrac{1}{2}\cdot\tfrac{1}{2}\cdot 1 = \tfrac{1}{4}.$$
  *(Fijamos $\alpha = 1/\sqrt{2}$, de modo que $\Delta_{D_1}(2) = 1/2 \neq 3/4 = \Delta_{D_2}(2)$ y $\Delta_{D_1}(3) = 2^{-3/2} \neq 1/4 = \Delta_{D_2}(3)$; las dinámicas son estrictamente distintas en todo $t \in T_{\rm caus}$).*
* **Umbral $\theta$ y Escalar $Q_s$:** Fijamos $\theta = 1/2$ y la elección recomendada $Q_s^D = \tau_D$.
* **Regla IR ($\mathcal{R}_{\rm IR}$):** En el límite de grano grueso (frente de onda inicial), el conjunto IR asociado al escalar de primera llegada $Q_s^D$ se define como el soporte del frente de primera llegada: $\operatorname{IR}(Q_s^D, \tau_D) := \{Q_s^D\} \cap I_s$.

#### Resultado y Demostración para este caso mínimo
**Estado:** **PASS (Demostrado bajo las definiciones anteriores).**

**Demostración:**
1. Calculamos el arrival time $\tau_D(C_4; s) = \inf\{t \in \{1,2,3\} : \Delta_D(C_4; s, t) \ge 1/2\}$:
   * Para $D_1$: $\Delta_{D_1}(1) = 0 < 1/2$ y $\Delta_{D_1}(2) = (\1/\sqrt{2})^2 = 1/2 \ge 1/2 \implies Q_s^{D_1}(C_4) = \tau_{D_1}(C_4; s) = 2$.
   * Para $D_2$: $\Delta_{D_2}(1) = 0 < 1/2$ y $\Delta_{D_2}(2) = 3/4 \ge 1/2 \implies Q_s^{D_2}(C_4) = \tau_{D_2}(C_4; s) = 2$.
2. Aplicando la regla $\mathcal{R}_{\rm IR}$:
   $$T_{\rm IR}^{D_1}(C_4; s) = \{2\} = T_{\rm IR}^{D_2}(C_4; s).$$
   Esto certifica la **Obligación 1 (igualdad dinámica en IR)** a pesar de que $\Delta_{D_1} \neq \Delta_{D_2}$ punto a punto en $T_{\rm caus}$.
3. Comparamos con $T_{\rm caus}(C_4; s) = \{2, 3\}$:
   $$T_{\rm IR}^{D_1}(C_4; s) = T_{\rm IR}^{D_2}(C_4; s) = \{2\} \subsetneq \{2, 3\} = T_{\rm caus}(C_4; s).$$
   El tiempo causal $t = 3 \in T_{\rm caus}$ (correspondiente al camino causal interior/lento $s \prec a \prec b \prec x$) queda estrictamente fuera del conjunto IR común, porque el operador $\inf$ en $\tau_D$ proyecta ambas dinámicas sobre la geodésica nula mínima ($t=2$), borrando la estructura de caminos interiores más largos. Esto certifica la **Obligación 2 (pérdida estricta frente al causal)**.

*(Observación adicional demostrada: Si hubiésemos fijado $\theta = 0.6$, entonces $\tau_{D_1} = \infty$ mientras $\tau_{D_2} = 2$, dando `FAIL` en la Obligación 1. Esto prueba que el caso $N=4$ no es tautológico: el éxito depende genuinamente del acoplamiento entre la atenuación dinámica y el umbral $\theta$).*
