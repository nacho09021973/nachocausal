[INFERENCE] El argumento analítico resiste los ataques de signos, normalización y rango. La concesión queda condicionada por una dependencia ejecutable ausente y por la distinción entre los intervalos internos y su serialización.

1. **§5.1 — Sustitución de `VN_FR`: `SE_SOSTIENE`.**

   [SOURCE] En el `run()` adjunto, `VN_FR` se consulta únicamente para obtener las velocidades normales. Las tablas, los pesos, `Z` y `B_hi` no dependen de ella. Las dos velocidades U de `e3` son positivas y las dos V son exactamente cero.

   [INFERENCE] La rama elegida para cero es válida **en este caso concreto**. Con `vn_lo = −ε`, multiplicar una cota superior no negativa de la integral de cara produce una contribución inferior a la contribución verdadera, que es cero. Para `Zprime`, el extremo inferior es negativo y el superior calculado con `vn_hi = +ε` es no negativo: ambos encierran cero.

   [INFERENCE] Esto no convierte esa rama en aritmética intervalar válida para cualquier velocidad cuyo intervalo cruce cero: usar `vn_hi` positivo con el peso inferior podría fallar para una velocidad verdadera positiva. Aquí salva el argumento conocer exactamente que la velocidad es cero.

   **Condición mínima de concesión:** [INFERENCE] que el objeto `gate` realmente ejecutado sea el adjunto, con esas velocidades exactas; véase el punto 6.

2. **§5.2 — Fórmula y signos de `dphi`: `SE_SOSTIENE`.**

   [SOURCE] El histórico define \(s(w)=1+W_0(-w/e)\), usa \(G(w)=s(w)e^{-s(w)}\) en las caras y las primitivas cúbicas indicadas para `fin` y `fout`.

   [INFERENCE] La equivalencia entre esas primitivas y las integrales de volumen se verifica algebraicamente:
   \[
   w=(1-s)e^s,\qquad dw=-s e^s\,ds,\qquad G(w)\,dw=-s^2\,ds.
   \]
   Por tanto, `fin` y `fout` son precisamente las integrales de ese \(G(UV)\) sobre las regiones interior y exterior. No falta un factor de normalización.

   [INFERENCE] En \(U=-u_{\rm out}\), desplazar el límite inferior con velocidad \(-du_{\rm out}\) aporta \(+du_{\rm out}J_{\rm uout}\). En \(U=u_{\rm in}\), el aporte es \(+du_{\rm in}J_{\rm uin}\). Los términos V llevan los signos superior positivo e inferior negativo. La interfaz \(U=0\) permanece fija, por lo que no aporta transporte. La regla del cociente da exactamente la fórmula implementada.

   **Condición mínima de concesión:** [INFERENCE] identidad del `G` importado con el usado en esta definición y aplicación de H4 a las operaciones intervalares nuevas. La coincidencia con valores flotantes históricos es un control, no su demostración.

3. **§5.3 — Cota burda de `|S(e2)|`: `SE_SOSTIENE`.**

   [SOURCE] H2 define el núcleo simétrico mediante \(p\), extendido por cero a pares incomparables, y H3 proporciona la fórmula de borde.

   [INFERENCE] Se tiene \(0\le h\le1\), luego
   \[
   0\le H(x)\le Z,\qquad
   0\le I_f=\int_f G H\le J_f Z.
   \]
   El núcleo simétrico no introduce aquí un factor 2: las orientaciones causales son excluyentes para pares estrictamente comparables.

   [INFERENCE] Como `e2` mueve una sola cara,
   \[
   S(e_2)=2v\left(I_f-\frac{J_fB}{Z}\right),
   \]
   y, usando positividad,
   \[
   |S(e_2)|\le2|v|J_f
   \left(Z_{\rm hi}+\frac{B_{\rm hi}}{Z_{\rm lo}}\right).
   \]
   Dividir por \(Z_{\rm lo}^2\) proporciona la cota implementada. La posible sobreestimación de `B_hi` sólo la debilita.

   **Condición mínima de concesión:** [INFERENCE] las envolventes heredadas, \(Z_{\rm lo}>0\) y la integral de cara superior certificada. No encuentro una hipótesis analítica adicional.

4. **§5.4 — Producto exterior e identificabilidad: `SE_SOSTIENE`.**

   [SOURCE] El código exige simultáneamente `d2.a > 0`, `drho3_lo.a > 0` y `W23_lo > 0`.

   [INFERENCE] Con esas positividades,
   \[
   W_{23}\ge
   \underline{\phi_2}\,\underline{\rho_3}
   -\overline{|\phi_3|}\,\overline{|\rho_2|}.
   \]
   No se emparejan indebidamente extremos ni se necesita conocer el signo de \(\rho_2\).

   [INFERENCE] Un testigo algebraico explícito es
   \[
   v=\rho_3\partial_{x_2}-\rho_2\partial_{x_3}.
   \]
   Entonces \(d\rho(v)=0\) y \(d\phi(v)=W_{23}>0\). El rango de la carta lo convierte en una dirección física. Además, la regularidad continua de las derivadas y \(d\rho\ne0\) permiten aplicar el teorema de la función implícita: hay una superficie local de nivel de \(\rho\) sobre la que \(\phi\) varía. Esto excluye reconstrucción local incluso sin presuponer una función reconstructora diferenciable.

   **Condición mínima de concesión:** [INFERENCE] las cotas anteriores y la regularidad heredada de H3.

5. **§5.5 — Carta y H5: `SE_SOSTIENE`.**

   [SOURCE] La reconstrucción es \(v_1=v_0x_1\), \(u_{\rm in}=x_3/v_1\), \(u_{\rm out}=u_{\rm in}/x_2\).

   [INFERENCE] Su diferenciación reproduce las columnas suministradas y da
   \[
   \det=-\frac{v_0u_{\rm out}}{x_2v_1}
   =-\frac{10133099161583616}{8106479329266893}\ne0.
   \]
   Los racionales exactos representan la carta matemática en el punto binary64. No deben confundirse con derivadas de un algoritmo de reconstrucción redondeado.

   [SOURCE] El histórico usa los mismos literales de `LSTAR`; H5 fija expresamente `path(0.5)` binary64.

   **Condición mínima de concesión:** [INFERENCE] mantener ese objeto y la quinta componente fija. No se concede transferencia al punto medio real.

6. **Pieza adicional — dependencia ejecutada y salida numérica.**

   **`REQUIERE_CORRECCIÓN` de trazabilidad.** [SOURCE] B3 obtiene `gate`, `b15` y `executed_ir` de `verify_b2_1_box_certificate`, cuyo cuerpo no está adjunto.

   [UNVERIFIED] No puede comprobarse aquí que ese módulo exporte exactamente la compuerta mostrada, preserve sus funciones o imponga efectivamente la caché vacía y la inspección del IR ejecutado. Una discrepancia permitiría que el código certificase otro integrando u otro ejecutable. El JSON declara el éxito, pero no cierra esa conexión.

   **Condición mínima de concesión:** [INFERENCE] acreditar esas identidades y las garantías efectivas del control B2.1, sin reabrir B1.5.

   **`MENOR` en la serialización.** [SOURCE] Los extremos intervalares se convierten mediante `float(...)`, sin conversión dirigida explícita.

   [INFERENCE] H4 no garantiza que esa conversión conserve el sentido de cada cota. Esto afecta a los últimos dígitos del JSON; no al test interno de positividad. Las cifras abreviadas de la nota tienen margen suficiente para absorber ese redondeo.

   **Condición mínima de concesión:** [INFERENCE] conceder las cifras exteriores abreviadas; no atribuir certificación dirigida a todos los dígitos serializados.

Veredicto: AUDIT_PASS_CONDITIONAL_B21_BINDING_AND_EXECUTED_IR