<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ c12c10eb4de36669f2048754d2df20a9747adf1f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: STOP (estado operativo, no validación del contenido)
modelo: gemini-4-argon, esfuerzo: maxOutputTokens=32768, thinkingLevel=high, vía: API generativelanguage.googleapis.com generateContent, sin herramientas
modelo devuelto por API: gemini-4-argon
gemini.json sha256 002e0df62550c150a2c01dc46d10966e8c6274a3da54aed3bd366f1e303945b1
inicio: 2026-10-14T06:57:46Z  fin: 2026-10-14T07:01:00Z
documento: /home/ignac/nachocausal/research_program/causal_fidelity/CAUSAL_FIDELITY_MINIMAL_CONTRACT.md ; último commit observado: 505ac49 ; sha256 de la copia enviada 5590e21c766cc989adc6fcefe845e830f2f6c01d7209e34fb9d36007c9614cbd
documento: /home/ignac/nachocausal/research_program/causal_fidelity/revisiones/2026-10-14-argon-high-delta-v2/delta_v1_v2.diff ; último commit observado: 31bc7b5 ; sha256 de la copia enviada ca648e4fe9562bb3e774b5b4ae09a826cb4762e2e6f9b828fd76e6c1dd2b62f6
entrada_gemini.txt sha256 505dfd6af9539e41ad0708ab85b4cc2884e89027ffa4fc7aef807402ed495fda
respuesta sha256 046ce28d3290eeb7b471af04c37627081d83b5292ebb8a25d10d8d601ba3c139
-->

### Tarea 1: Evaluación de la tabla de §10 (fila por fila)

1. **`PASS` vacío $\emptyset=\emptyset$ con $\tau=\infty$:** **Cerrado.** NT1 exige $\tau^{\rm IR}_{D_1},\tau^{\rm IR}_{D_2},\tau^{\rm IR}_{\rm caus}<\infty$, lo que impide $T^D_{\rm IR}=[\infty,\infty)=\emptyset$.
2. **$T_{\rm IR}$ (de dos escalares) frente a $T_{\rm caus}$ (conjunto): tipos sin casar:** **Cerrado** (bajo NT1). §5 define ambos como subconjuntos $[\tau,\infty)\subseteq[0,\infty)$ y §6 los reduce a escalares.
3. **`PASS` por cardinalidad (punto $\subsetneq$ intervalo):** **Cerrado.** En §5 tanto $T^D_{\rm IR}$ como $T_{\rm caus}$ son intervalos de la forma $[\tau,\infty)$, impidiendo comparar puntos con semirrectas.
4. **IR con $C_N$ fijo; $N$ libre y ligada a la vez:** **Cerrado.** §5 define $\tau^{\rm IR}_D$ y $\tau^{\rm IR}_{\rm caus}$ mediante $\lim_{N\to\infty}$, ligando $N$ en todos los objetos IR.
5. **Cuantificadores ausentes sobre $N,s$, realizaciones:** **Parcial.** Faltan el acoplamiento conjunto entre medidas $\mu_N$ (necesario para la convergencia casi segura en §5) y la definición de $Q^D(c)$ cuando $\sigma_N(c)=\text{«sin par»}$.
6. **$C_N$ familia frente a instancia:** **Cerrado.** §2.1 separa explícitamente la ley $\mu_N$, la variable aleatoria $C_N\sim\mu_N$ y la instancia fija $c$.
7. **Detector ausente de la firma:** **Parcial.** $d$ se incorpora en $\lambda,\Delta_D,\tau_D,\tau_{\rm caus}$, pero se omite en la firma de la dinámica $D(c,s)$ (§2.3) y se reemplaza por un comodín ambiguo `·` en NT2 y NT3.
8. **$t$ sin sentido intrínseco en un poset:** **Parcial.** Se define $t=k/\lambda(c;s,d)$, pero §2.2 no restringe el codominio de $\lambda$ a $(0,\infty)$ (permitiendo $\lambda=0$) y §2.4/NT2 tratan $t$ como continuo mientras §2.2 lo define como discreto.
9. **`FAIL` trivial por futuro vacío o cono de un paso:** **No cerrado.** Por §1, incumplir cualquier cláusula de §7 *produce* un `FAIL`; ubicar NT4 en §7 convierte el futuro vacío en un `FAIL` automático en vez de excluirlo, y además $A(c)$ puede desconectar $s$ de $d$ aun cumpliendo NT4.
10. **$D_1=D_2$ permitido:** **Parcial.** NT3 impide $D_1=D_2$, pero permite dinámicas idénticas hasta cruzar el umbral $\theta$ (dando $Q^{D_1}(C_N)\equiv Q^{D_2}(C_N)$ para todo $N$) y se vuelve ambigua cuando $\mu_N=\delta_{c_N}$.
11. **$q$ sobre la curva entera vacía §3:** **Cerrado.** §4 elimina $q$ y fija $Q^D(c):=\tau_D(c;\sigma_N(c))$.
12. **$\mathcal R_{\rm IR}$ recibía dos escalares, contra «único escalar»:** **Cerrado.** §5 define $\tau^{\rm IR}_D$ exclusivamente a partir del escalar $Q^D(C_N)$.
13. **Ínfimo continuo con malla sin interpolación definida:** **Cerrado.** §3 restringe el conjunto a $\{k/\lambda : k\in\mathbb N\}$, donde el mínimo está bien definido.
14. **$\Delta$ no monótona:** **Cerrado.** §2.4(1) impone explícitamente que $\Delta_D(c;s,d,t)$ sea no decreciente en $t$.
15. **Paréntesis rotos en fórmulas ($(N)$, $(D_1,D_2)$…):** **Cerrado.** El diff confirma que los delimitadores LaTeX rotos de la v1 fueron corregidos.

---

### Tarea 2: Defectos nuevos en v2, tipos, cuantificadores, equivalencia de §6 y trivialidad

#### 2.1 Auditoría de tipos y cuantificadores (Demostrado sobre el texto)

* **$\mu_N, C_N$ y modo $\mathcal M$:** §2.1 define una ley marginal $\mu_N$ para cada $N$, sin especificar un espacio de probabilidad conjunto para la sucesión $(C_N)_{N\in\mathbb N}$. Sin acoplamiento inter-$N$, el modo de convergencia «casi segura» de §5 **no está matemáticamente definido**. Además, «convergencia de la esperanza» ($\lim_N \mathbb E[Q^D(C_N)]$) no es un modo de convergencia de variables aleatorias y colisiona con NT2 ($\lim_N \Delta_{D_i}(C_N;\cdot,t)>\theta$ «en el modo $\mathcal M$»).
* **$\sigma_N$ (equivariancia y valor nulo):**
  1. Si $c$ posee automorfismos no triviales $\phi\in\mathrm{Aut}(c)$ sin pares fijos $(s,d)$ con $s\prec d$, **no existe ningún selector determinista equivariante** $\sigma_N(c)$ que devuelva un par.
  2. Cuando $\sigma_N(c)=\text{«sin par»}$ (permitido con probabilidad $p_N\to 0$ bajo NT4), las funciones $\lambda(c;s,d)$, $\Delta_D(c;s,d,t)$, $\tau_D(c;s,d)$, $Q^D(c)$ y $\tau_{\rm caus}(c;s,d)$ **quedan fuera de dominio**. Si a «sin par» se le asigna $\tau_D=\infty$ y $p_N>0$, entonces en el modo $\mathcal M=\text{esperanza}$ se tiene $\mathbb E[Q^D(C_N)]=\infty$ para todo $N$, haciendo imposible cumplir NT1 aunque $Q^D(C_N)$ converja en probabilidad a una constante finita.
* **$A$ y $\lambda$:** §2.2 no exige que $A(c)$ sea equivariante, ni que $(x,y)\in A(c)$ sea total en $x$ (sin bloqueos para $(X_k)_{k\ge 0}$), ni que exista camino en $A(c)$ de $s$ a $d$. Tampoco restringe el codominio de $\lambda$ a $(0,\infty)$, dejando $k/\lambda$ expuesto a división por cero. En NT4, $\lambda\to\infty$ omite sus argumentos $\lambda(C_N;\sigma_N(C_N))$ y el modo de divergencia.
* **$D_1, D_2$ y $\Delta_D$:** En §2.3 $D$ asigna una ley a $(c,s)$ sin recibir $d$, contradiciendo que $D_1,D_2$ «comparten el detector». En §2.4, $\Delta_D(c;s,d,t)$ ya promedia sobre el proceso $X_k\sim D$, por lo que para $c$ fijo es una función determinista. Así, en NT3, «la ley de $\Delta_{D_i}(C_N;\cdot)$» depende sólo de la aleatoriedad de $\mu_N$: si $\mu_N=\delta_{c_N}$ (permitido en §2.1), es una masa puntual determinista.
* **$\tau_D, \tau_{\rm caus}$:** No se precisa si $k\in\mathbb N$ incluye el $0$ (en §2.3 se escribe $k\ge 0$). En §5 falta declarar $\min\emptyset=\infty$ para $\tau_{\rm caus}$.
* **Equivalencia de §6 y tipos de $T^D_{\rm IR}, T_{\rm caus}$:** En §5, $\tau^{\rm IR}_D, \tau^{\rm IR}_{\rm caus}\in[0,\infty]$. Si $\tau^{\rm IR}_{D_1}=\tau^{\rm IR}_{D_2}=\infty$ y $\tau^{\rm IR}_{\rm caus}=1$, entonces en $[0,\infty)$ se tiene $T^{D_1}_{\rm IR}=T^{D_2}_{\rm IR}=[\infty,\infty)=\emptyset$, que **no es una semirrecta cerrada de $[0,\infty)$** (contra §5), aunque satisface $\emptyset=\emptyset\subsetneq[1,\infty)$ en §6. La afirmación de §5 y la equivalencia de §6 sólo son válidas condicionadas a NT1 ($\tau^{\rm IR}<\infty$).

#### 2.2 Construcciones explícitas de `PASS` trivial y `FAIL` trivial pese a NT1–NT5 (Demostrado)

**1. `PASS` trivial (dinámicas idénticas hasta el umbral $\theta$):**
* **Construcción:** Sea $\mu_N=\delta_{c_N}$ donde $c_N$ es la cadena $0\prec 1\prec\dots\prec N$; $\sigma_N(c_N)=(0,N)$; $\lambda(c_N;0,N)=N$; $A(c_N)=\{(x,x),(x,x+1)\}$; $\theta=1/2$; modo $\mathcal M$ en probabilidad. Entonces $\tau_{\rm caus}(c_N;0,N)=1=\tau^{\rm IR}_{\rm caus}$.
  Defínanse $D_1, D_2$ así: desde $X_0=0$, con probabilidad $3/4$ ambas dinámicas avanzan determinísticamente a velocidad $1/2$ (alternando 1 paso de espera y 1 de avance), alcanzando $N$ exactamente en $k=2N$ ($t=2$). Con la probabilidad restante $1/4$, la partícula entra en un modo lento que bajo $D_1$ avanza a velocidad $1/3$ (llega en $t=3$) y bajo $D_2$ a velocidad $1/4$ (llega en $t=4$).
* **Verificación:** Para todo $N$, $\Delta_{D_i}(c_N;0,N,t)$ vale $0$ si $t<2$ y salta a $3/4>\theta$ en $t=2$. Por tanto, **$Q^{D_1}(c_N)=Q^{D_2}(c_N)=2$ idénticamente para todo $N$**. En $t=3.5$, $\Delta_{D_1}=1\neq 3/4=\Delta_{D_2}$, cumpliendo NT3. Se cumplen §6 ($2=2>1$) y NT1–NT5 sin que el límite IR haga ningún trabajo, pues el observable $Q^D$ jamás distinguió $D_1$ de $D_2$ a escala finita.
* **Cláusula que lo impediría:** Sustituir NT3 por **NT3'**: *Para todo $N$ suficientemente grande, las distribuciones de $Q^{D_1}(C_N)$ y $Q^{D_2}(C_N)$ difieren (o $\tau_{D_1}(c_N)\neq\tau_{D_2}(c_N)$ con diferencia $\ge \Omega(N^{-\alpha})$ no atribuible a un retraso de $O(1)$ pasos), o bien exigir que $\tau^{\rm IR}_{D_1}=\tau^{\rm IR}_{D_2}$ se cumpla para todo $\theta\in(0,1)$.*

**2. `FAIL` trivial pese a NT4:**
* **Construcción:** En la misma cadena $c_N$ con $\sigma_N(c_N)=(0,N)$ y $\lambda=N\to\infty$ (cumple NT4), tómese $A(c_N)=\{(x,x):x\in E\}\subseteq\{(x,y):x\preceq y\}$. Entonces $\tau_{\rm caus}(c_N)=\tau_{D_i}(c_N)=\infty$, violando NT1 y arrojando un `FAIL` trivial por §1. Además, como §1 define `FAIL` como el incumplimiento de §6 **o §7**, cualquier familia degenerada que viole NT4 produce automáticamente un `FAIL` en vez de quedar excluida.
* **Cláusula que lo impediría:** Convertir NT4 y la condición $\tau^{\rm IR}_{\rm caus}\in(0,\infty)$ en **precondiciones de admisibilidad del protocolo** (cuyo fallo declara el experimento `OPEN`/inválido, no `FAIL`).

---

### Tarea 3: Ataque a las tres decisiones propias de la v2 (§10)

1. **$\Delta_D$ monótona con valores en $[0,1]$:** Excluye observables locales no acumulados (funciones de Green, conmutadores causales o densidades puntuales $\mathbb P_D(X_k=d)$ que decaen tras el paso del frente). No vacía el contrato porque el primer alcance siempre puede codificarse como probabilidad acumulada, pero impide definir tiempos de llegada mediante máximos o cruces de fase de ondas oscilatorias.
2. **Cono $\tau_{\rm caus}$ definido por los movimientos admisibles $A$:** **Desvirtúa la parte causal del test en posets continuos/densos (Demostrado).** Si $\lambda(C_N;s,d)\to\infty$ es la cadena más larga (tiempo propio en un rociado tipo Minkowski) y $A(c)$ permite cualquier salto causal $x\preceq y$ (o enlaces de Hasse, donde entre $s$ y $d$ suelen existir cadenas maximales de pocos pasos casi lumínicos), el camino de menos pasos en $A(C_N)$ tiene longitud $k_{\min}=O(1)$ mientras $\lambda\to\infty$. Entonces $\tau_{\rm caus}(C_N)=k_{\min}/\lambda\to 0$, colapsando $\tau^{\rm IR}_{\rm caus}=0$. La obligación $\tau^{\rm IR}_{D_i}>\tau^{\rm IR}_{\rm caus}$ se reduce trivialmente a $\tau^{\rm IR}_{D_i}>0$, perdiendo toda relación con el cono de luz geométrico.
3. **Exigir límites constantes ($\tau^{\rm IR}_D, \tau^{\rm IR}_{\rm caus}\in[0,\infty]$):** **Es la decisión que excluye casos legítimos que el contrato debería admitir.** En posets aleatorios donde $\sigma_N$ selecciona pares $(s,d)$ sólo por el orden y $\lambda$ es una escala global del poset (p. ej. $|E|^{1/d}$), o en leyes $\mu_N$ no ergódicas (mezclas de geometrías macroscópicas), $Q^{D_1}(C_N)$ y $Q^{D_2}(C_N)$ pueden converger en probabilidad o c.s. a la **misma variable aleatoria no degenerada** $\tau^{\rm IR}>\tau^{\rm IR}_{\rm caus}$ (universalidad IR realización a realización), caso que la v2 descarta artificialmente como `OPEN`/`FAIL`.

---

### Tarea 4: ¿Test vacío por construcción o admisión de un `PASS` con contenido?

**Demostrado:** El contrato v2 **no es vacío por construcción**; admite un `PASS` riguroso y con contenido dinámico real.

**Argumento:** Considérese la construcción candidata de §8 sobre la cadena lineal determinista $c_N=(0\prec 1\prec\dots\prec N)$ con $\sigma_N(c_N)=(0,N)$, $\lambda=N$, $A(c_N)=\{(x,x),(x,x+1)\}$ y $\theta\in(0,1)\setminus\{1/2\}$. Aquí $\tau_{\rm caus}(c_N)=1=\tau^{\rm IR}_{\rm caus}$. Sea $D_1$ el paseo perezoso i.i.d. con probabilidad de avance $p\in(0,1)$ y $D_2$ una cadena de Markov de memoria de 1 paso sobre los incrementos con la **misma deriva estacionaria** $p$, pero correlación no nula ($\rho\neq 0$).
1. Por la ley de los grandes números para procesos ergódicos, el tiempo de alcance $T_N^{D_i}$ cumple $T_N^{D_i}/N\to 1/p$ en probabilidad cuando $N\to\infty$. Por tanto, para cualquier $\theta\in(0,1)$, $\tau^{\rm IR}_{D_1}=\tau^{\rm IR}_{D_2}=1/p > 1=\tau^{\rm IR}_{\rm caus}$ (§6, NT1, NT2, NT4, NT5 se cumplen).
2. A tamaño finito $N$, por el teorema central del límite, $T_N^{D_i} = N/p + \sqrt{N}\,\sigma_i Z_N + o(\sqrt{N})$ con varianzas asintóticas distintas $\sigma_1^2\neq\sigma_2^2$. Para $\theta\neq 1/2$ ($\Phi^{-1}(\theta)\neq 0$), no sólo difieren las curvas $\Delta_{D_1}(c_N;\cdot)\neq\Delta_{D_2}(c_N;\cdot)$ (cumpliendo NT3), sino que los propios escalares finitos $Q^{D_1}(c_N)$ y $Q^{D_2}(c_N)$ difieren en orden $\Theta(N^{-1/2})$ y sólo colapsan en el límite IR $N\to\infty$.
