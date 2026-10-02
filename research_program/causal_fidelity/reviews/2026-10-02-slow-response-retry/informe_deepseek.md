<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ f1b54d7; lo que sigue a la cabecera es la respuesta sin editar)
modelo: deepseek-v4-pro, esfuerzo: thinking=disabled, max_tokens=8192, vía: API api.deepseek.com/chat/completions, sin herramientas
inicio: 2026-10-02T12:25:54Z  fin: 2026-10-02T12:26:32Z
documento: /home/ignac/nachocausal/.worktrees/causal-fidelity-definition-repair/research_program/causal_fidelity/CAUSAL_FIDELITY_MINIMAL_CONTRACT.md ; último commit que lo cambió: 71a5adf ; sha256 al enviar ba99fcb5ed7cbc160cca29b35c57120ad17f8618ed144192e1598831f8442957
documento: /home/ignac/nachocausal/.worktrees/causal-fidelity-definition-repair/research_program/causal_fidelity/SLOW_PROTOCOL_RESPONSE_2026-10-02.md ; último commit que lo cambió: 71a5adf ; sha256 al enviar b612bdc22302cc8133972e70ab449bbec56fb904d790bb24437f2e84c319c607
documento: /home/ignac/nachocausal/.worktrees/causal-fidelity-definition-repair/research_program/causal_fidelity/GROWING_FAMILY_RESPONSE_2026-10-02.md ; último commit que lo cambió: 71a5adf ; sha256 al enviar ce57b69f17506f833b9e642f380c4813f4810c08b5a0fdb92658ee33580b1c83
entrada_deepseek.txt sha256 1ca2dec8208ae1bf4df9a21dcfbbe651972eef8ae39f1486b278eeeb122c9fef
respuesta sha256 f0dddf13cb611c699f084ab78c23d24a8994925ce7c79606fff0091327b540e0
-->

Claro, aquí está el informe de revisión crítica de los tres documentos, elaborado según el objetivo y los criterios solicitados.

---

### Informe de Revisión Crítica de Borrador Matemático

**Documentos Revisados:**
1.  `CAUSAL_FIDELITY_MINIMAL_CONTRACT.md` (en adelante, **Doc 1**)
2.  `SLOW_PROTOCOL_RESPONSE_2026-10-02.md` (en adelante, **Doc 2**)
3.  `GROWING_FAMILY_RESPONSE_2026-10-02.md` (en adelante, **Doc 3**)

**Veredicto:** `REQUIERE_CORRECCION`

**Resumen General:** La propuesta matemática está, en su mayoría, bien definida y las derivaciones algebraicas presentadas son correctas dentro del alcance explícitamente autolimitado de los Documentos 2 y 3. Sin embargo, se han detectado objeciones críticas que impiden un veredicto de `SIN_ERROR_DETECTADO_EN_EL_ALCANCE`. Estas objeciones se centran en (a) la validez del contraejemplo central bajo las restricciones del contrato histórico, y (b) un matiz técnico en la prueba de convergencia fuerte, que excede la afirmación estrictamente demostrada sin invalidar el resultado principal.

---

### Objeciones Detalladas

#### Objeción 1: El contraejemplo central excede el alcance del contrato histórico al usar un observable no autorizado.

*   **Documento y Sección:** Documento 2, Secciones 1, 2, 3 y 6; Documento 3, Secciones 1, 3, 6 y 7.
*   **Afirmación Precisa:** "El sector lento distingue estas dos dinámicas aunque tau coincida... Esto prueba... la insuficiencia de tau para estas lecturas." (Doc 2, §6) y "La igualdad de llegada normalizada no determina su respuesta lineal lenta en esta familia." (Doc 3, §7). La afirmación es que para las dos dinámicas \(D_1\) y \(D_2\), el arrival time \(\tau\) es insuficiente como observable.
*   **Derivación o Contraejemplo:**
    1.  El **Doc 1** (§4) establece que "El contrato permite un único escalar IR asociado a la fuente \(s\): \(Q_s^D(C_N):=q\left(\tau_D(C_N;s),\Delta_D(C_N;s,\cdot)\right)\)" y que "No se autoriza seleccionar entre varios \(Q\)'s después de inspeccionar los datos, ni combinar \(Q_s\) con un segundo score para decidir el resultado."
    2.  El **Doc 2** (§1) declara explícitamente que "Esto amplía expresamente el blanco de un único escalar del contrato histórico; no modifica ese documento ni afirma haber satisfecho su gate físico."
    3.  El contraejemplo de los **Docs 2 y 3** construye dos dinámicas \(D_1, D_2\) que producen el mismo \(\tau\) (por lo tanto, la función \(q=\tau\) daría \(Q_s^{D_1} = Q_s^{D_2}\)), pero diferencias en un funcional lineal \(\langle g, K_T f \rangle\) para \(f, g\) en un sector lento.
    4.  La conclusión de que \(\tau\) es insuficiente para distinguir las dinámicas se basa en la existencia de un observable (el funcional \(\langle g, K_T f \rangle\)) que las distingue. Sin embargo, este observable no es el único escalar \(Q_s\) permitido por el contrato histórico; es otra magnitud basada en la respuesta completa \(\Delta_D\).
*   **Gravedad:** **Alta.** Aunque el Doc 2 declara explícitamente que amplía el blanco del contrato, la afirmación de que ha *refutado* la suficiencia de \(\tau\) ("ARRIVAL_SUFFICIENCY_FOR_THOSE_READOUTS = REFUTED_IN_FINITE_EXAMPLE") es lógicamente inválida *dentro del marco del contrato original*. El hecho de que dos dinámicas puedan distinguirse por un observable no autorizado por el contrato no refuta la capacidad del observable autorizado para ser el único descriptor IR. El resultado es matemáticamente correcto pero la interpretación de "insuficiencia de tau" es una conclusión que excede lo que se demuestra en relación con el Doc 1.
*   **Corrección Mínima:** Reformular la conclusión para reflejar con precisión el alcance ampliado. En lugar de afirmar que \(\tau\) es insuficiente en el marco del contrato original, se debe decir: "Se demuestra que \(\tau\), como observable único, es insuficiente para distinguir las dinámicas *si el contrato se amplía para incluir lecturas lineales lentas del perfil de respuesta completo*. Por tanto, si el objetivo es distinguir estas dinámicas, el contrato original es demasiado restrictivo y debe ser modificado." Esto transforma el resultado de una refutación a una demostración de necesidad de un contrato más rico, que es la ambición declarada en Doc 2.

#### Objeción 2: La prueba de la convergencia fuerte de \(\Pi_n\) esboza un argumento por densidad, pero no formaliza todos los pasos de manera constructiva.

*   **Documento y Sección:** Documento 3, Sección 5.
*   **Afirmación Precisa:** "Para j fijo y n suficientemente grande, su versión discreta muestreada en los centros de celda está retenida por \(P_n\). Su interpolación isométrica converge en \(L^2\) a \(\phi_j\), por continuidad de \(\phi_j\). La distancia de \(\phi_j\) a ran \(\Pi_n\) tiende a cero. Por densidad de las combinaciones finitas de esa base y \(||\Pi_n|| \le 1\), la convergencia se extiende a todo \(h\) en \(H\)."
*   **Derivación o Contraejemplo:**
    1.  La afirmación clave es "la distancia de \(\phi_j\) a ran \(\Pi_n\) tiende a cero".
    2.  **Vía 1 (Inclusión Directa):** Para que esto sea cierto, se necesita demostrar que la proyección de la versión muestreada de \(\phi_j\) es exactamente la versión muestreada, o al menos que su diferencia proyectada tiende a cero. Es decir, se debe probar que \(\phi_j^{(n)} \in \text{ran } P_n\) para \(n\) suficientemente grande.
        *   \(\phi_j^{(n)}(k) = \phi_j((k+1/2)/n)\) es el muestreo en los centros de celda.
        *   La afirmación es que \(\phi_j^{(n)}\) es autovector de \(L_{4n}\) cuyo autovalor \(\lambda_{j,n}\) satisface \(\lambda_{j,n} \le (4n)^{-1/2}\).
        *   **Inclusión Directa:** La fórmula en Doc 3, §5 dice que los autovectores de \(L_T\) son proporcionales a \(\cos(\pi j (k+1/2)/T)\). Para \(T=4n\), un autovector es \(\cos(\pi j (k+1/2) / (4n))\).
        *   La función \(\phi_j(t) = \cos(\pi j t / 4) / \sqrt{2}\) (para \(j \ge 1\)), muestreada en \(t = (k+1/2)/n\), da \(\cos(\pi j (k+1/2) / (4n)) / \sqrt{2}\).
        *   Este vector es *exactamente proporcional* al autovector de \(L_{4n}\), y por lo tanto pertenece a \(\text{ran } P_n\), **siempre que** su autovalor asociado \(\lambda_{j,n} \le (4n)^{-1/2}\). La condición es \(4 \sin^2(\pi j / (8n)) \le (4n)^{-1/2}\), que es verdadera para \(n\) suficientemente grande con \(j\) fijo.
        *   La prueba completa requiere establecer la inclusión directa \(\phi_j^{(n)} \in \text{ran } P_n\) para \(n\) suficientemente grande. El documento lo sugiere pero no lo formaliza. Sin embargo, esta formalización es directa y subsana la objeción.
    3.  **Vía 2 (Convergencia del Error de Proyección):** Incluso si la inclusión directa no fuera exacta, se podría demostrar que la norma de la componente de \(\phi_j^{(n)}\) con autovalores altos tiende a cero. Esto sería una prueba más débil pero igualmente válida. El documento no presenta este cálculo.
    4.  Dado que el paso crítico de la prueba por densidad ("la distancia tiende a cero") se basa en un hecho que es plausible y verificable, pero no está formalmente escrito, la demostración tal como está es un esbozo de prueba. No es un error matemático, sino una omisión en el rigor de la presentación.
*   **Gravedad:** **Media.** El resultado (convergencia fuerte) es, con toda probabilidad, matemáticamente verdadero y la vía de la "inclusión directa" es sencilla de formalizar. La gravedad radica en que la prueba presentada en el documento se apoya en una afirmación no demostrada, que en una revisión estricta de un texto matemático debe ser subsanada para que la prueba sea considerada completa. La distinción entre "convergencia fuerte" y "convergencia en norma" se maneja correctamente, pero la prueba de la primera queda formalmente incompleta.
*   **Corrección Mínima:** Añadir un párrafo o lema explícito que demuestre la inclusión directa. Por ejemplo:
    > **Lema:** Para \(j \in \mathbb{N}_0\) fijo, sea \(\phi_j^{(n)}\) el vector definido por \(\phi_j^{(n)}(k) = \phi_j((k+1/2)/n)\). Entonces, para \(n\) suficientemente grande tal que \(4 \sin^2(\pi j / (8n)) \le (4n)^{-1/2}\), se tiene \(P_n \phi_j^{(n)} = \phi_j^{(n)}\), y por lo tanto, la distancia de \(\phi_j\) a \(\text{ran } \Pi_n\) está acotada por \(||\phi_j - E_n\phi_j^{(n)}||_{L^2}\), que tiende a cero.

---

### Comprobación de Puntos Específicos

1.  **Orientación, inyección, retardación y transporte:** Las definiciones son consistentes y conformes a la convención estándar. La matriz \(A_n\) actúa sobre estados y la retardación se verifica al iterar la inyección. La compatibilidad con isomorfismos marcados es una propiedad básica de la construcción.
2.  **Espectro del Laplaciano temporal:** El espectro, los modos y el rango del proyector \(P_n\) están computados correctamente. El cálculo del rango como \(1+\lfloor \frac{2T}{\pi}\arcsin(\frac{1}{2\sqrt{T}}) \rfloor\) y su asintótica \(\sim \sqrt{T}/\pi\) y \(\sim 2\sqrt{n}/\pi\) son correctos. La interpretación macroscópica de la lentitud como variación por actualización es clara y no se confunde con una energía física de estados.
3.  **Suficiencia de \(P K P\):** La suficiencia para lecturas lineales está demostrada correcta y elegantemente. El documento explícitamente limita su aplicabilidad a lecturas lineales y no afirma suficiente para mediciones no lineales. Faltan los marcos físicos, como se declara.
4.  **Conteo de eventos y rutas:** Los conteos son exactos. La familia con dos rutas de longitud \(2n\) y \(3n\) da \(N_n = 5n\) y \(H_n=3n\), como se declara. La elección de ventana \(T=4n\) y reloj \(t=k/n\) es consistente y la normalización de recursos está bien definida por la isometría \(E_n\). No se detectan normalizaciones implícitas que cambien el protocolo.
5.  **Isometría, adjunto y transferencia:** Las definiciones de \(E_n\) y \(E_n^*\) son correctas y se verifica \(E_n^*E_n = I\). La transferencia \(K_\gamma E_n = E_n K_{\gamma,n}\) es exacta como se describe. La identidad \(\hat{G}_{\gamma,n} = \Pi_n K_\gamma \Pi_n\) se sigue directamente. La prueba de \(\Pi_n \to I\) fuertemente esbozada es formalmente incompleta como se detalla en la Objeción 2.
6.  **Contraejemplo con \(\theta=1/2\) y discrepancia \(93/256\):** Los cálculos son verificados. La respuesta al impulso es \(R_1(2)=1, R_1(3)=1\) y \(R_2(2)=9/16, R_2(3)=27/64\), dando \(\tau_1=\tau_2=2\) para \(\theta=1/2\). La lectura del estado constante \(c_n\) es \((1/2)\exp(-2\gamma) + (1/4)\exp(-3\gamma)\), que para \(\gamma_1=0\) y \(\gamma_2=\log(4/3)\) da \(3/4\) y \(99/256\), respectivamente, con diferencia \(93/256\). Este resultado es robusto e independiente de \(n\), y se verifica por una segunda vía mediante integración en el límite.
7.  **Afirmaciones que exceden lo demostrado o dependencia circular:**
    *   La principal excedencia es la ya descrita en la Objeción 1: la interpretación del contraejemplo como una refutación de la suficiencia de \(\tau\) dentro del contrato original.
    *   No se encuentra una dependencia circular entre la elección del modelo y la conclusión de insuficiencia. La elección del modelo (dos rutas) está motivada por el ejemplo previo (Doc 2, §6 y §8), y los autores son transparentes al respecto (Doc 3, §1: "no se presentan como selección ciega respecto del contraejemplo que la motivó"). El resultado de que \(\tau\) es insuficiente es una consecuencia matemática del modelo, no un presupuesto para su elección. La circularidad no existe; la motivación es histórica y no lógica.

### Conclusión Final

Los Documentos 2 y 3 presentan un trabajo matemático generalmente correcto y bien definido. El cálculo central, la construcción de la familia y la verificación del contraejemplo son sólidos y han sido comprobados por vías independientes en el texto.

El veredicto `REQUIERE_CORRECCION` se emite por dos razones específicas y subsanables:

1.  **Interpretación del Resultado (Gravedad Alta):** El resultado debe ser reenmarcado como una demostración de que el contrato original es *insuficiente* para el objetivo de los autores (distinguir las dinámicas), y no como una refutación de la capacidad de \(\tau\) para ser un escalar IR *dentro* de las reglas de ese contrato. La lógica interna del Doc 1 no se ve afectada por la existencia de un observable externo que distinga las dinámicas.
2.  **Prueba de Convergencia Fuerte (Gravedad Media):** La demostración es válida en espíritu, pero el paso clave que justifica la aplicación del teorema de densidad está esbozado y no formalmente demostrado. Requiere la adición de un lema que pruebe la inclusión de los vectores muestreados en el sector lento.

En resumen, el núcleo matemático es válido y no se detectan errores en las derivaciones de las fórmulas o en los cálculos. Las objeciones son de rigor lógico e interpretación, no de cálculo, y son fácilmente corregibles con las modificaciones indicadas.
