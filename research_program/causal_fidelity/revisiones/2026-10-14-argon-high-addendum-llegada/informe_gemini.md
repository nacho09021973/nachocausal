<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ c12c10eb4de36669f2048754d2df20a9747adf1f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=high, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 0d5f1f7756f147604f557888707372daf8a61122473574e3813cba8894cf64f9
inicio: 2026-10-14T07:18:22Z  fin: 2026-10-14T07:22:08Z
documento: /home/ignac/nachocausal/.worktrees/causal-fidelity-nontriviality/research_program/causal_fidelity/ARRIVAL_TEST_NONTRIVIALITY_2026-10-14.md ; último commit observado: 98c5742 ; sha256 de la copia enviada b38fe93a507b0215ff2d574dee326d0652d51e96ba53b0bdcc3e1faef155f493
documento: /home/ignac/nachocausal/.worktrees/causal-fidelity-nontriviality/research_program/causal_fidelity/IR_OPERATIONAL_DEFINITION_2026-10-02.md ; último commit observado: 71a5adf ; sha256 de la copia enviada 50386219994d9e8a84e93336f701562a7f149c7ba080ae57c94b7e0d3c47f585
documento: /home/ignac/nachocausal/.worktrees/causal-fidelity-nontriviality/research_program/causal_fidelity/GROWING_FAMILY_RESPONSE_2026-10-02.md ; último commit observado: 3387f35 ; sha256 de la copia enviada 9f12cf8cd03487164d2cd90d3d28042e9aa38fb02754b415828edf690514979d
entrada_gemini.txt sha256 83ba8bb317acf4d42e2d3d587706b1ad2f92e5a925df5b45a2529d808bd3684b
respuesta sha256 c0876c87c3fa69404920f54ffe53e9b6f2b8083420a45149b365b0748f02c948
-->

### 1. Revisión del Lema 1 (§1)

**Veredicto (Demostrado):** El enunciado del Lema 1 es **correcto** bajo las definiciones exactas de IROD §§2–7, pero el paso (ii) de la prueba contiene una imprecisión de cuantificador que conviene corregir.

**Verificación paso a paso con IROD:**
1. **Estructura de $K$ y $J_D$:** En IROD §5, $X = [0,1] \sqcup \{\perp\}$ con $d(x,y)=|x-y|$ en $[0,1]$, $d(x,\perp)=2$ y $d(\perp,\perp)=0$. Como $L_n \subseteq \{1,\dots,H_n\}$ es no vacío ($H_n = \max L_n$) y $0 \le g_n(k) = \frac{b_n \lfloor k/b_n \rfloor}{H_n} \le \frac{k}{H_n} \le 1$, se tiene $K_n \subseteq [0,1]$ compacto no vacío. Al estar $[0,1]$ a distancia $2$ de $\perp$, la convergencia de Hausdorff $d_H(K_n, K) \to 0$ obliga a que $K \subseteq [0,1]$ sea compacto no vacío (para $n$ con $d_H(K_n,K) < 2$, ningún punto de $K$ puede ser $\perp$). Análogamente, cada $J_{D,n}$ es un singleton; como $\operatorname{diam}(J_{D,n}) = 0$, la convergencia de Hausdorff $J_{D,n} \to J_D$ implica $\operatorname{diam}(J_D)=0$, luego $J_D = \{q_D\}$ con $q_D \in X$ (IROD §6).
2. **Paso (i):** Si $J_D = \{\perp\}$, entonces $\perp \notin K \subseteq [0,1]$, por lo que $J_D \not\subseteq K$ y falla `PASS_FORMAL` (coincidiendo con IROD §7). Correcto.
3. **Paso (ii) y hueco de cuantificador:** El addendum afirma: *«Si $J_D=\{q\}$ con $q\in[0,1]$, entonces $J_{D,n}=\{q_n\}$ con $q_n\to q$ y $q_n\in K_n$. Para todo $n$, $\operatorname{dist}(q,K) \le |q-q_n| + \operatorname{dist}(q_n,K) \dots$»*.
   * **Reparo:** Esto **no tiene por qué cumplirse para todo $n$**, sino sólo **para todo $n$ suficientemente grande**.
   * **Contraejemplo al paso intermedio «para todo $n$»:** Sea una dinámica con $\tau_{D,1} = \infty$ (luego $J_{D,1} = \{\perp\} \not\subseteq K_1$) y $\tau_{D,n} \in L_n$ con $g_n(\tau_{D,n}) \to q \in [0,1]$ para $n \ge 2$. Entonces $d_H(J_{D,n}, \{q\}) \to 0$, por lo que $J_D = \{q\}$ existe, pero en $n=1$ no existe $q_1 \in K_1$ ni está definido $|q - q_1|$.
   * **Reparación (Demostrado):** Como $d(q,\perp)=2$, existe $N_0$ tal que para todo $n \ge N_0$ es $d_H(J_{D,n},\{q\}) < 2$, lo cual fuerza $J_{D,n} \neq \{\perp\}$, es decir, $\tau_{D,n} \le H_n$ finito y $J_{D,n} = \{q_n\}$ con $q_n = g_n(\tau_{D,n}) \in [0,1]$. Por la condición de retardación de IROD §4 ($R_{D,n}(k)=0$ si $k \notin L_n$) y $\theta > 0$, necesariamente $\tau_{D,n} \in L_n$, luego $q_n \in K_n$ para todo $n \ge N_0$. Tomando el límite $n \to \infty$ para $n \ge N_0$:
     $$\operatorname{dist}(q,K) \le |q - q_n| + \operatorname{dist}(q_n,K) \le d_H(J_{D,n},\{q\}) + d_H(K_n,K) \xrightarrow[n\to\infty]{} 0.$$
     Como $K$ es cerrado, $q \in K$.
4. **Paso (iii):** Al ser $\{q\} \subseteq K$ automático cuando $q \neq \perp$, la inclusión estricta $\{q\} \subsetneq K$ equivale a $K \setminus \{q\} \neq \emptyset$, es decir, $|K| \ge 2$. Correcto.

---

### 2. Revisión de la aplicación a la familia de dos rutas (§2)

**Veredicto (Demostrado):** Todos los cálculos de §2 son **exactos** (con la única observación menor de que el barrido en $\theta$ omite el rango $\theta > 1$).

**Recálculo explícito:**
* **Conjunto causal límite $K$:** En GROWING §§1–2, $L_n = \{2n, 3n\}$ y $H_n = 3n$, luego $b_n = \lfloor \sqrt{3n} \rfloor$. Por la cota de IROD §3 ($0 \le k/H_n - g_n(k) < b_n/H_n \le 1/\sqrt{3n}$):
  $$\lim_{n\to\infty} g_n(2n) = \frac{2}{3}, \qquad \lim_{n\to\infty} g_n(3n) = 1 \implies K = \left\{\frac{2}{3}, 1\right\}, \quad |K| = 2.$$
* **Amplitudes:** Con $\gamma_1 = 0$ y $\gamma_2 = \log(4/3)$ ($e^{-\gamma_2} = 3/4$), la respuesta al impulso $R_{\gamma,n}(k) = e^{-2\gamma}\mathbf{1}_{k=2n} + e^{-3\gamma}\mathbf{1}_{k=3n}$ vale:
  * $D_1$: $R_{1,n}(2n) = 1$, $R_{1,n}(3n) = 1$, y $0$ fuera de $L_n$.
  * $D_2$: $R_{2,n}(2n) = (3/4)^2 = 9/16 = 36/64$, $R_{2,n}(3n) = (3/4)^3 = 27/64$, y $0$ fuera de $L_n$.
* **Caso $\theta = 1/2 = 32/64$:** Como $R_{1,n}(2n) = 1 \ge 1/2$ y $R_{2,n}(2n) = 36/64 \ge 32/64$, ambos mínimos en IROD §4 se alcanzan en $\tau_{1,n} = \tau_{2,n} = 2n$ para todo $n \ge 1$. Por tanto $J_1 = J_2 = \{2/3\} \subsetneq \{2/3,1\} = K$ (`PASS_FORMAL`).
* **División por casos de $\theta > 0$:** Como $R_{2,n}(2n) = 9/16 > 27/64 = R_{2,n}(3n)$, la primera llegada de $D_2$ está gobernada únicamente por el pico en $2n$:
  * $0 < \theta \le 27/64$: ambos alcanzan $\theta$ en $k=2n \implies \tau_{1,n}=\tau_{2,n}=2n$, $J_1=J_2=\{2/3\}$ (`PASS_FORMAL`).
  * $27/64 < \theta \le 9/16$: en $k=2n$ sigue siendo $R_{2,n}(2n) = 9/16 \ge \theta \implies \tau_{1,n}=\tau_{2,n}=2n$, $J_1=J_2=\{2/3\}$ (`PASS_FORMAL`).
  * $9/16 < \theta \le 1$: $\tau_{1,n} = 2n$ ($J_1=\{2/3\}$), pero $\max_k R_{2,n}(k) = 9/16 < \theta$, luego $\tau_{2,n} = \infty$ y $J_2 = \{\perp\}$ (`FAIL`).
  * *(Omitido en §2)* $\theta > 1$: ninguno llega, $\tau_{1,n}=\tau_{2,n}=\infty$, $J_1=J_2=\{\perp\}$ (`FAIL` por Lema 1(i)).

---

### 3. Revisión de NT-$\theta$, NT-Q y admisibilidad (§3)

**Veredicto (Demostrado):** Las tres cláusulas cierran los casos triviales diagnosticados en §§1–2 (la cadena $|K|=1$, el ajuste puntual de $\theta$ y el par de GROWING con $\tau_{1,n}\equiv \tau_{2,n}$). Sin embargo, **quedan al menos dos familias de `PASS_FORMAL` triviales distintas del retraso de $O(1)$**:

#### Hueco 3.1 (Demostrado): Contradicción de cuantificador en NT-Q ($\exists\theta$ frente a $\forall\theta$)
El enunciado formal de NT-Q exige sólo que **exista** un $\theta \in \Theta$ con $\tau_{D1,n}(\theta) \neq \tau_{D2,n}(\theta)$ para $n$ grande, contradiciendo el resumen final de §3 (*«para todo $\theta \in \Theta$… siendo distintas a todo $n$ grande»*). Bajo el cuantificador $\exists\theta$, dos dinámicas pueden tener $\tau_{1,n}(\theta) = \tau_{2,n}(\theta)$ idénticos en casi todo $\Theta$ y diferir en un único punto.

* **Construcción explícita:** Sea $L_n = \{2n, 2n + \lfloor \sqrt{n} \rfloor, 3n\}$ ($H_n = 3n$, $K = \{2/3, 1\}$) y $\Theta = [1/4, 1/2]$. Declárense respuestas retardadas:
  $$R_{1,n}(2n) = \frac{1}{2}, \quad R_{2,n}(2n) = \frac{1}{2}\left(1 - \frac{1}{n}\right), \quad R_{i,n}(2n+\lfloor\sqrt{n}\rfloor) = R_{i,n}(3n) = 1 \quad (i=1,2).$$
  Para todo $\theta \in [1/4, 1/2)$ y todo $n > (1-2\theta)^{-1}$, se tiene $\tau_{1,n}(\theta) = \tau_{2,n}(\theta) = 2n$ (identidad trivial a $n$ finito en todo el interior de $\Theta$). Sólo en el extremo $\theta = 1/2$ es $\tau_{1,n}(1/2) = 2n \neq 2n + \lfloor \sqrt{n} \rfloor = \tau_{2,n}(1/2)$ para todo $n \ge 1$. Cumple Admisibilidad, NT-$\theta$ y NT-Q (y el retraso en $\theta=1/2$ ni siquiera es $O(1)$).

#### Hueco 3.2 (Demostrado): Retraso sublineal divergente $\Delta\tau_n \to \infty$ con colisión exacta de bloque a $n$ finito ($J_{D1,n} = J_{D2,n}$)
Incluso reforzando NT-Q a $\forall \theta \in \Theta$ y prohibiendo retrasos $O(1)$ exigiendo $|\tau_{1,n}(\theta) - \tau_{2,n}(\theta)| \to \infty$, cualquier diferencia sublineal $\Delta\tau_n = o(H_n)$ produce $J_1 = J_2$. Más aún, como el tamaño de bloque es $b_n = \lfloor \sqrt{H_n} \rfloor$, si $\tau_{1,n}$ y $\tau_{2,n}$ caen en el **mismo bloque**, entonces $g_n(\tau_{1,n}) = g_n(\tau_{2,n})$ **exactamente para todo $n$ finito**: el límite $n \to \infty$ sigue sin hacer ningún trabajo.

* **Construcción explícita:** Sea $H_n = 3n$, $b_n = \lfloor \sqrt{3n} \rfloor$, $k_{1,n} = b_n \lfloor 2n/b_n \rfloor$, $d_n = \lfloor b_n / 2 \rfloor \sim \frac{\sqrt{3}}{2}\sqrt{n} \to \infty$, y $k_{2,n} = k_{1,n} + d_n$. Como $k_{1,n}$ es múltiplo de $b_n$ y $0 \le d_n < b_n$, para todo $n \ge 2$ se tiene:
  $$B_n(k_{2,n}) = b_n \left\lfloor \frac{k_{1,n} + d_n}{b_n} \right\rfloor = k_{1,n} = B_n(k_{1,n}) \implies g_n(k_{1,n}) = g_n(k_{2,n}).$$
  Tomando $L_n = \{k_{1,n}, k_{2,n}, 3n\}$ y dinámicas que lleguen en $\tau_{1,n}(\theta) = k_{1,n}$ y $\tau_{2,n}(\theta) = k_{2,n}$ para todo $\theta \in \Theta$ (véase §4 abajo para una realización lineal exacta), se obtiene $\tau_{2,n} - \tau_{1,n} = d_n \to \infty$ (no es $O(1)$), pero $J_{1,n}(\theta) = J_{2,n}(\theta)$ es **idéntico a todo $n$ finito**.

---

### 4. Resolución del problema abierto de §4 (dinámicas lineales sobre coberturas)

En la clase lineal de IROD §8 y GROWING §§1–2, con actualización $X_{i,n}(k+1) = \alpha_{i,n} A_n X_{i,n}(k)$ ($\alpha_{i,n} > 0$) y normalización común $a_n > 0$, la respuesta al impulso en el detector es:
$$R_{i,n}(k) = a_n \, m_n(k) \, \alpha_{i,n}^k, \qquad m_n(k) := (A_n^k)_{d_n, s_n},$$
donde $m_n(k)$ es el número de cadenas saturadas de longitud $k$ entre $s_n$ y $d_n$, de modo que $L_n = \{k \ge 1 : m_n(k) \ge 1\}$. Resolvemos el problema abierto separando dos teoremas exactos.

#### Teorema 4.1 (Demostrado — Imposibilidad con atenuación y multiplicidad no creciente)
*Si para todo $n$ grande la multiplicidad $k \mapsto m_n(k)$ es no creciente en $L_n$ (en particular, si hay una única cadena saturada por cada longitud $k \in L_n$, $m_n(k)=1$, como en IROD §8 y GROWING §2) y ambas especies son no amplificadoras ($\alpha_{i,n} \in (0,1]$), entonces **ninguna** construcción cumple NT-Q junto con $J_{D1} = J_{D2} \neq \{\perp\}$.*

*Prueba.* Para todo $k \in L_n$, como $k \ge k_{\min,n} := \min L_n$, $\alpha_{i,n} \in (0,1]$ y $m_n(k) \le m_n(k_{\min,n})$, se tiene $R_{i,n}(k) = a_n m_n(k)\alpha_{i,n}^k \le R_{i,n}(k_{\min,n})$. Luego el máximo de $R_{i,n}$ en $L_n$ se alcanza siempre en $k_{\min,n}$. Por definición de primera llegada, para cualquier $\theta > 0$:
$$\tau_{i,n}(\theta) = \begin{cases} k_{\min,n} & \text{si } R_{i,n}(k_{\min,n}) \ge \theta, \\ \infty & \text{si } R_{i,n}(k_{\min,n}) < \theta. \end{cases}$$
Para que existan límites $J_{D1}(\theta) = J_{D2}(\theta) = \{q\} \neq \{\perp\}$, ambos tiempos deben ser finitos para todo $n$ grande, lo cual fuerza $\tau_{1,n}(\theta) = \tau_{2,n}(\theta) = k_{\min,n}$, violando NT-Q. ∎

#### Teorema 4.2 (Demostrado — Construcción explícita en la clase lineal general de IROD)
*La clase general de dinámicas lineales sobre coberturas de IROD **sí admite** construcciones que cumplen Admisibilidad, NT-$\theta$, NT-Q (incluso para todo $\theta \in \Theta$ y con $\tau_{2,n}-\tau_{1,n} \to \infty$) e igualdad de llegadas límite.*

*Construcción y prueba.* Fíjese cualquier sucesión entera $1 \le d_n \le n$ con $d_n/n \to 0$ (por ejemplo $d_n = 1$, o $d_n = \lfloor \sqrt{n} \rfloor \to \infty$). Para cada $n \ge 1$, defínase el poset marcado $(C_n; s_n, d_n)$ uniendo entre $s_n$ y $d_n$ cadenas saturadas disjuntas salvo en sus extremos:
* $1$ cadena de longitud $2n$,
* $8$ cadenas de longitud $2n + d_n$,
* $1$ cadena de longitud $3n$,

siendo el orden parcial su clausura transitiva. Como $2n \ge 2$, los vértices interiores de cadenas distintas son incomparables y ninguna arista deja de ser cobertura; por tanto:
$$L_n = \{2n,\, 2n+d_n,\, 3n\}, \quad H_n = 3n, \quad m_n(2n)=1, \quad m_n(2n+d_n)=8, \quad m_n(3n)=1.$$
Con $a_n = 1$ y las dos especies de IROD §8, $\alpha_{1,n} = 1$ ($\gamma_1 = 0$) y $\alpha_{2,n} = 2^{-1/n}$ ($\gamma_2 = \log 2$):
* $R_{1,n}(2n) = 1$, $R_{1,n}(2n+d_n) = 8$, $R_{1,n}(3n) = 1$;
* $R_{2,n}(2n) = 2^{-2} = \frac{1}{4}$, $R_{2,n}(2n+d_n) = 8 \cdot 2^{-(2 + d_n/n)} = 2^{1 - d_n/n} \ge 1$, $R_{2,n}(3n) = \frac{1}{8}$.

Fíjese $\Theta = [1/3, 2/3]$. Para todo $\theta \in \Theta$ y todo $n \ge 1$:
1. $R_{1,n}(2n) = 1 \ge \theta \implies \tau_{1,n}(\theta) = 2n$.
2. $R_{2,n}(2n) = 1/4 < 1/3 \le \theta$ y $R_{2,n}(2n+d_n) \ge 1 \ge \theta \implies \tau_{2,n}(\theta) = 2n + d_n$.
3. Luego $\tau_{1,n}(\theta) \neq \tau_{2,n}(\theta)$ para todo $n \ge 1$ y todo $\theta \in \Theta$ (cumple NT-Q fuerte).
4. Como $d_n/n \to 0$, por la cota de IROD §3 se tiene $g_n(2n) \to 2/3$, $g_n(2n+d_n) \to 2/3$ y $g_n(3n) \to 1$. Así, $K_n \to K = \{2/3, 1\}$ ($|K|=2$) y $J_1(\theta) = J_2(\theta) = \{2/3\} \subsetneq K$ para todo $\theta \in \Theta$. ∎

**Observación de diseño (Conjeturado / diagnóstico):** El Teorema 4.2 funciona porque la multiplicidad $m_n(k)$ compensa la atenuación a distancia microscópica $d_n = o(n)$ de $2n$; por tanto, sigue siendo un fenómeno de borde sublineal sin equivalencia de operadores lentos. Si se exigiera además que las llegadas antes de dividir por $H_n$ difieran a escala macroscópica ($|\tau_{1,n}-\tau_{2,n}| = \Omega(H_n)$), entonces $|g_n(\tau_{1,n}) - g_n(\tau_{2,n})| \ge \Omega(1) - 2b_n/H_n$ impediría directamente $J_1 = J_2$. Por consiguiente, **toda** igualdad $J_1 = J_2$ en IROD proviene necesariamente de diferencias $\Delta\tau_n = o(H_n)$.
