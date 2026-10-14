<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 6d7ba21c9bde4a78e13bedee91d56d0c09fbc8b5; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 6b936b581d5cc529f2b412546a56a5796c670a76d5c371e241a59c13b0212e44; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=high, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 47c62a22fb694510bbc800f986c513e520ee96d7a47293639f7ef998256742d6
inicio: 2026-10-13T16:45:22Z  fin: 2026-10-13T16:47:07Z
documento: /home/ignac/nachocausal/research_program/causal_fidelity/CAUSAL_FIDELITY_MINIMAL_CONTRACT.md ; último commit observado: sin versionar ; sha256 de la copia enviada ba99fcb5ed7cbc160cca29b35c57120ad17f8618ed144192e1598831f8442957
entrada_gemini.txt sha256 430db67671f19a0bfbc1c7f61701c9c7f1b57067476ddea0a78836fb2036e7cf
respuesta sha256 42de361c8a5aa53f2ddde8ad662f4c4b6accd20ba5d7d9b99d909cb8844116a9
-->

### 1. Auditoría formal del test de §6: tipos, cuantificadores y ambigüedades

**Diagnóstico (Demostrado):** Tal como está redactado, el test de §6 **no está bien planteado**. Presenta colisiones entre variables libres y ligadas, errores de tipo (escalares frente a conjuntos) y objetos subdeterminados.

#### Tabla de auditoría de objetos

1. **$C_N = (E_N, \prec_N, \mu_N)$ (§2.1):**
   * *Cuantificador aparente:* $\forall N \in \mathbb{N}$ (¿fijo o en límite $N\to\infty$?).
   * *Defectos de tipo:* (a) No se especifica si $\prec_N$ es un orden parcial estricto (irreflexivo, asimétrico, transitivo) ni si $|E_N| = N$. (b) **Ambigüedad crítica en $\mu_N$**: el texto oscila entre tratar $C_N$ como un único poset determinista con pesos de vértice $\mu_N: E_N \to \mathbb{R}_{\ge 0}$, o como una variable aleatoria sobre un espacio de realizaciones con ley de muestreo $\mu_N$.
2. **Fuente $s$, detector y tiempo $t$ (§2.1–§2.3):**
   * *Defectos de tipo:* Un conjunto causal finito $(E_N, \prec_N)$ carece de coordenada temporal real intrínseca $t \in \mathbb{R}$, y §2.1 prohíbe usar coordenadas de inmersión. No se define de dónde emerge el dominio temporal $I_s$ (¿pasos discretos de una cadena $k \in \mathbb{N}$ reescalados como $t = k/N$?). Además, el detector $d$ se menciona en §2.1–2.2 pero **desaparece de la signatura** de $\Delta_D(C_N; s, t)$, $\tau_D$, $Q_s$ y $T_{\rm caus}$. Tampoco se explica cómo se identifican $s$ y $d$ a través de distintos $N$ respetando la invariancia bajo reetiquetado.
3. **$D_1, D_2$ (§2.2):**
   * *Defecto de tipo:* No se declara el tipo matemático de una «dinámica» (¿semigrupo de Markov sobre $E_N$, operador en $\ell^2(E_N)$, sistema hiperbólico discreto?). Decir que «sólo pueden diferir en el ingrediente dinámico» es circular si no se parametriza el espacio de dinámicas admisibles.
4. **$\Delta_D(C_N; s, t)$ (§2.3):**
   * *Tipo:* $(C_N, s, t) \mapsto \mathbb{R} \cup \{\pm\infty, \text{NaN}\}$. Si $C_N$ es aleatorio bajo $\mu_N$, no se especifica si $\Delta_D$ es una variable aleatoria por realización o una esperanza $\mathbb{E}_{\mu_N}[\cdot]$.
5. **$\tau_D(C_N; s)$ (§3):**
   * *Tipo:* $\inf\{t \in I_s : \Delta_D(C_N; s, t) \ge \theta\} \in \mathbb{R} \cup \{\pm\infty\}$.
   * *Defecto:* Si $I_s \subset \mathbb{R}$ es continuo y $\Delta_D$ se evalúa en malla finita, el ínfimo depende del operador de interpolación no especificado. La frase «convención de igualdad» es redundante una vez escrito $\ge \theta$.
6. **$Q_s^D(C_N)$ (§4):**
   * *Tipo:* $q(\tau_D(C_N; s), \Delta_D(C_N; s, \cdot)) \in \mathbb{R} \cup \{\infty\}$.
   * *Defecto:* Si $q$ recibe como segundo argumento la trayectoria completa $\Delta_D(C_N; s, \cdot)$, entonces $Q_s^D$ no es un resumen a través de $\tau_D$, sino un funcional arbitrario de toda la curva de respuesta, vaciando de rol a §3.
7. **$T_{\rm caus}(C_N; s)$ (§5):**
   * *Tipo esperado:* $\mathcal{P}(I_s)$ (subconjunto de tiempos).
   * *Defecto:* Indeterminado. En un poset sin detector explícito $d$, «tiempos causalmente admisibles» carece de definición (¿longitudes de cadenas dirigidas de $s$ a $d$? ¿semirrecta a partir de la distancia gráfica mínima?).
8. **$T_{\rm IR}^D(C_N; s)$ y la regla $\mathcal{R}_{\rm IR}$ (§5–§6):**
   * *Dos errores estructurales graves:*
     1. **Incompatibilidad de tipos (escalar vs. conjunto):** Para $(C_N, s)$ fijos, tanto $Q_s^D(C_N)$ como $\tau_D(C_N; s)$ son **escalares únicos** en $\mathbb{R} \cup \{\infty\}$. Sin embargo, §6 exige que $T_{\rm IR}^D$ sea un **conjunto de tiempos** comparable mediante $\subsetneq$ con $T_{\rm caus}$. Además, §5 pasa *ambos* $(Q_s^D, \tau_D)$ a $\operatorname{IR}(\cdot)$, violando §4 («único escalar IR»).
     2. **Colisión de cuantificador en $N$:** Un límite infrarrojo ($\mathcal{R}_{\rm IR}$) toma el límite de escala $N \to \infty$ sobre la sucesión $\{C_N\}_{N \in \mathbb{N}}$. Por tanto, $N$ es una variable **ligada** por el operador $\operatorname{IR}$ y no puede aparecer como variable libre en $T_{\rm IR}^D(C_N; s)$ ni en $T_{\rm caus}(C_N; s)$.

---

### 2. Vulnerabilidades: `PASS` y `FAIL` triviales o vacíos

**Afirmación (Demostrado):** Con las reglas actuales de §1–§6, el test puede superarse de forma vacía, superarse por tautología de cardinalidad o fallar trivialmente sin poner a prueba propiedad dinámica alguna.

#### Construcción 2.1: `PASS` vacío por umbral alto ($\emptyset = \emptyset \subsetneq T_{\rm caus}$)
* **Construcción explícita:** Sea $E_2 = \{s, d\}$ con $s \prec d$, $I_s = \{1\}$, $T_{\rm caus} = \{1\}$. Fíjese $\theta = 2$. Sean $D_1, D_2$ cualesquiera dinámicas normalizadas tales que $|\Delta_{D_i}| \le 1 < \theta$. Entonces $\tau_{D_1} = \tau_{D_2} = \infty$ y $Q_s^{D_1} = Q_s^{D_2} = \infty$. Si $\mathcal{R}_{\rm IR}$ interpreta $\tau = \infty$ como el conjunto vacío de tiempos de llegada en $I_s$ ($T_{\rm IR}^{D_i} = \emptyset$), se obtiene:
  $$T_{\rm IR}^{D_1} = \emptyset = T_{\rm IR}^{D_2} \subsetneq \{1\} = T_{\rm caus}.$$
  Ambas obligaciones de §6 se cumplen literalmente (igualdad $\emptyset = \emptyset$, y $1 \in T_{\rm caus} \setminus \emptyset$).

#### Construcción 2.2: `PASS` trivial por tautología de cardinalidad
* **Construcción explícita:** Supóngase que $\tau_{D_i} < \infty$ y que $\mathcal{R}_{\rm IR}$ define el conjunto IR como el singulete del escalar límite $T_{\rm IR}^D := \{\lim_{N\to\infty} Q_s^D(C_N)\}$. En cualquier configuración donde $T_{\rm caus}$ tenga al menos dos tiempos (o un intervalo $[t_0, \infty)$), todo singulete $\{t_*\} \subset T_{\rm caus}$ cumple $|T_{\rm IR}^D| = 1 < |T_{\rm caus}|$, por lo que **la inclusión estricta $\subsetneq$ (Obligación 2) se satisface automáticamente por tipo**, incluso si la dinámica viaja exactamente sobre el borde del cono de luz ($t_* = t_0$). Y si el primer paso causal tiene amplitud $\ge \theta$ para ambas dinámicas, $\tau_{D_1} = \tau_{D_2} = t_0$, cumpliendo también la Obligación 1.

#### Construcción 2.3: `FAIL` trivial por futuro causal vacío
* **Construcción explícita:** Sea $C_N$ una anticadena ($\prec_N = \emptyset$) o $s$ un elemento maximal, de modo que $T_{\rm caus}(C_N; s) = \emptyset$. Como no existe ningún conjunto $A$ tal que $A \subsetneq \emptyset$, el test falla para cualesquiera $D_1, D_2$.

#### Cláusulas correctoras que deben añadirse al contrato
1. **No vacuidad dinámica:** Exigir $\tau_{D_i}(C_N; s) < \infty$ (para $N$ grande) y $T_{\rm IR}^{D_i} \neq \emptyset$.
2. **Homogeneidad de tipos (rayos temporales):** Definir tanto $T_{\rm caus}$ como $T_{\rm IR}^D$ en la misma álgebra de conjuntos (específicamente, semirrectas cerradas $[t, \infty) \subset I_s$), prohibiendo comparar un singulete puntual $\{t_*\}$ contra un intervalo continuo $[t_{\rm min}, \infty)$.
3. **No degeneración del umbral:** Exigir $\inf_{t} \Delta_D(C_N; s, t) < \theta < \sup_{t} \liminf_{N\to\infty} \Delta_D(C_N; s, t)$, impidiendo que $\tau_D$ colapse trivialmente a $0$ o a $\infty$.
4. **No identidad en UV:** Exigir que exista $N < \infty$ y $t \in I_s$ tales que $\Delta_{D_1}(C_N; s, t) \neq \Delta_{D_2}(C_N; s, t)$.

---

### 3. Caso mínimo no trivial con contenido matemático

Para que el test tenga contenido genuino y respete la prohibición de §6 de usar coincidencias en una sola talla finita, el caso mínimo requiere una cadena causal finita de tamaño $N$ con paso al límite IR $N \to \infty$.

#### Especificación cerrada de objetos
* **Familia causal $C_N$:** Para cada $N \in \mathbb{N}_{\ge 2}$, sea la cadena lineal $E_N = \{0, 1, \dots, N\}$ con orden causal estricto $i \prec_N j \iff i < j$, medida determinista $\mu_N = \delta_{C_N}$, fuente $s = 0$ y detector $d = N$. (Para $N$ fijo, el motivo mínimo con dos longitudes de trayectoria causal es $N=2$, donde $0 \prec 2$ tiene longitud 1 y $0 \prec 1 \prec 2$ tiene longitud 2).
* **Tiempo macroscópico y $T_{\rm caus}$:** Una trayectoria causal en $k \in \mathbb{N}$ pasos de reloj discreto es una sucesión monótona $0 = x_0 \preceq_N x_1 \preceq_N \dots \preceq_N x_k = N$ que avanza a lo sumo un eslabón de Hasse por paso ($x_{m+1} - x_m \in \{0, 1\}$). Reescalando el tiempo macroscópico como $t = k/N \in I_s := [0, \infty)$, el detector $d=N$ es causalmente alcanzable si y sólo si $k \ge N$, lo que define en el límite IR:
  $$T_{\rm caus}(s, d) := [1, \infty).$$
* **Dos dinámicas $D_1, D_2$:** Caminatas aleatorias causales en tiempo discreto $k = \lfloor tN \rfloor$ que parten de $X_0 = 0$:
  * *$D_1$ (Bernoulli i.i.d.):* En cada paso, avanza un eslabón ($x \to x+1$) con probabilidad $p \in (0, 1)$ y permanece en $x$ con probabilidad $1-p$.
  * *$D_2$ (Markov correlacionada / con inercia):* Fijado $p \in (0, 1)$ y un parámetro de correlación $\alpha \in (0, \min(p, 1-p))$, el incremento $\eta_k := X_k - X_{k-1} \in \{0, 1\}$ sigue una cadena de Markov de dos estados con matriz de transición $P(\eta_{k}=1 \mid \eta_{k-1}=1) = p + (1-p)\frac{\alpha}{p}$ y $P(\eta_{k}=1 \mid \eta_{k-1}=0) = p - \alpha$, inicializada en su distribución estacionaria $\mathbb{P}(\eta_1 = 1) = p$.
  *(Nota: $D_1$ y $D_2$ difieren en su memoria microscópica y varianza $\sigma_1^2 \neq \sigma_2^2$, pero comparten deriva media $p$).*
* **Respuesta $\Delta_D$, umbral $\theta$ y escalar $Q_s^D$:**
  $$\Delta_D(C_N; s, t) := \mathbb{P}_D(X_{\lfloor tN \rfloor} = N) = \mathbb{P}_D\!\left(\sum_{m=1}^{\lfloor tN \rfloor} \eta_m \ge N\right), \quad \theta := \frac{1}{2}, \quad Q_s^D(C_N) := \tau_D(C_N; s).$$
* **Regla $\mathcal{R}_{\rm IR}$:** Define el conjunto de tiempos activos en el infrarrojo como la semirrecta a partir del límite de escala del arrival time:
  $$T_{\rm IR}^D(s, d) := \left[\lim_{N \to \infty} Q_s^D(C_N),\, \infty\right).$$

#### Veredicto y demostración en este caso mínimo

**Resultado (Demostrado): `PASS` si $p_1 = p_2 = p \in (0, 1)$; `FAIL` si $p_1 \neq p_2$ o si $p = 1$.**

*Demostración:*
1. Para cada dinámica $D_i \in \{D_1, D_2\}$, la posición al paso $k = \lfloor tN \rfloor$ es $S_k = \sum_{m=1}^k \eta_m$. En $D_1$, los $\eta_m$ son i.i.d. con $\mathbb{E}[\eta_m] = p$. En $D_2$, $(\eta_m)_{m \ge 1}$ es una cadena de Markov finita, irreducible y aperiódica con medida invariante $\pi(1) = p$.
2. Por la Ley Fuerte de los Grandes Números para cadenas de Markov ergódicas, $S_{\lfloor tN \rfloor} / N \to p t$ casi seguramente cuando $N \to \infty$. En consecuencia:
   $$\lim_{N \to \infty} \Delta_{D_i}(C_N; s, t) = \begin{cases} 0 & \text{si } t < 1/p, \\ 1 & \text{si } t > 1/p. \end{cases}$$
3. Para $\theta = 1/2 \in (0, 1)$, se sigue que $\lim_{N \to \infty} \tau_{D_1}(C_N; s) = \lim_{N \to \infty} \tau_{D_2}(C_N; s) = 1/p$ (aunque para todo $N$ finito $\Delta_{D_1} \neq \Delta_{D_2}$ por tener varianzas asintóticas distintas $\sigma_1^2 = p(1-p) \neq \sigma_2^2$).
4. Aplicando $\mathcal{R}_{\rm IR}$ con $p \in (0, 1)$, se tiene $1/p > 1$, luego:
   $$T_{\rm IR}^{D_1}(s, d) = \left[\frac{1}{p}, \infty\right) = T_{\rm IR}^{D_2}(s, d) \subsetneq [1, \infty) = T_{\rm caus}(s, d).$$
   * **Obligación 1 (Igualdad IR):** Se cumple exactamente porque el límite hidrodinámico borra la correlación microscópica $\alpha$.
   * **Obligación 2 (Pérdida estricta):** Todo tiempo macroscópico $t \in [1, 1/p)$ es causalmente admisible (existen cadenas causales de longitud $k \ge N$), pero tiene probabilidad exponencialmente nula de activación bajo ambas dinámicas en el límite IR. $\blacksquare$
