[INFERENCE] El ensamblado geométrico y las orientaciones se sostienen. Encuentro dos reservas: el control `fresh_ir` no demuestra por sí solo la inspección del código ejecutado, y la cota decimal del acta está redondeada en la dirección incorrecta. No encuentro un contraejemplo al signo positivo.

1. **§7.1 — Inclusiones, franjas y extensiones. Clasificación: SE_SOSTIENE.**

   [SOURCE] `coord_range` calcula extremos racionales sobre ambas curvas y ambos extremos temporales, y aplica `dn` al mínimo convertido a binary64 y `up` al máximo.

   [INFERENCE] Eso encierra cada coordenada durante toda la caja. La negación de `u_out` invierte correctamente los extremos: el lado izquierdo interior es `−uo_lo`, y el exterior, `−uo_hi`. Los demás lados tienen también la dirección correcta.

   Las caras verticales reales contienen la extensión tangencial `[v0_hi,v1_lo]` y están contenidas en `[v0_lo,v1_hi]`; para las horizontales ocurre lo correspondiente con `[-uo_lo,ui_lo]` y `[-uo_hi,ui_hi]`. Las cuatro franjas encierran sus respectivas posiciones normales.

   **Condición de concesión:** [INFERENCE] Ninguna adicional a las hipótesis aceptadas y las comprobaciones de orden del código.

2. **§7.2 — Vértices, orientaciones y kernels nuevos. Clasificación: SE_SOSTIENE.**

   [SOURCE] Para las cotas inferiores, `run_box` pasa `c_top` como extremo pasado a `lb_rows_xy` y `c_bot` como extremo futuro. `face_h_cells` selecciona respectivamente `Q_bot` y `Q_top`.

   [INFERENCE] Son exactamente los enlaces
   \[
   c_{\rm top}\to Q_{\rm bot},\qquad Q_{\rm top}\to c_{\rm bot},
   \]
   que reducen cada intervalo causal y dan cotas inferiores. Si un enlace no es estrictamente causal, devolver cero es válido. Los dos enlaces no pueden ser simultáneamente estrictos.

   Para la cota superior se usan
   \[
   c_{\rm bot}\to Q_{\rm top},\qquad Q_{\rm bot}\to c_{\rm top}.
   \]
   Cada término domina su orientación. Ambos pueden resultar positivos como envolventes; sumarlos sigue siendo conservador.

   `lb_rows_xy` conserva la aritmética de la recta y no necesita que la fuente sea un nodo. `N_TAU=64` hace exactos los extremos diádicos de la partición. `strip_weights` integra longitud tangencial y toma una envolvente sobre el espesor normal: no falta ningún factor de espesor. `face_h_cells` usa las esquinas y direcciones de redondeo correspondientes.

   **Condición de concesión:** [INFERENCE] La garantía de compilación indicada en el punto 6; ninguna hipótesis analítica nueva.

3. **§7.3 — Retícula exterior y fila superior. Clasificación: SE_SOSTIENE.**

   [SOURCE] `Vg_o` tiene `M+1` nodos, con `Vg_o[M−1]=v1_lo` y `Vg_o[M]=v1_hi`. La numeración es `i*(M+1)+j`.

   [INFERENCE] Por tanto, `cbot=i*n1+(M−1)` y `ctop=(i+1)*n1+M` son las esquinas inferior izquierda y superior derecha correctas. `pub[:,ctop].T` proporciona, para cada franja, las filas de la orientación pasada.

   Los cuatro kernels señalados usan diferencias entre nodos, teselados locales o índices de orden; no presuponen espaciado uniforme. La fila delgada no rompe esas propiedades mientras los nodos y subteselados sean estrictamente crecientes, lo que se comprueba.

   **Condición de concesión:** [INFERENCE] Ninguna adicional para `M=128`. La frase «cualquier valor» debe entenderse restringida a parámetros que permitan construir la retícula y superar sus comprobaciones.

4. **§7.4 — `Z'` y ensamblado de `S`. Clasificación: SE_SOSTIENE.**

   [INFERENCE] Para velocidad positiva, `vn_hi·J_hi` es una cota superior. Para la cara superior, con velocidad negativa y `J≥0`,
   \[
   vJ\le v_{\rm hi}J\le v_{\rm hi}J_{\rm lo}.
   \]
   El signo negativo del producto es correcto. La cota inferior complementaria usa correctamente `vn_lo·J_hi`.

   [SOURCE] B2.1 exige `Zp_hi>0`, mientras que la compuerta exigía `Zp_lo>0`.

   [INFERENCE] Esa relajación es válida: con `Z≥Z_lo>0`,
   \[
   \frac{Z'}Z\le\frac{Z'_{\rm hi}}Z\le\frac{Z'_{\rm hi}}{Z_{\rm lo}}.
   \]
   No hace falta demostrar `Z'>0`. Como `k_hi>0` y `0≤B≤B_hi`, la resta `Bprime_lo−k_hi·B_hi` conserva la dirección. Para `S_lo>0`, dividir por una cota superior de `Z²` también es correcto.

   **Condición de concesión:** [INFERENCE] Positividad de `Z_lo`, satisfecha por los pesos positivos de estos rectángulos bajo las dependencias aceptadas.

5. **§7.5 — Ambas curvas y velocidades. Clasificación: SE_SOSTIENE.**

   [SOURCE] `CURVES` contiene los extremos binary64 convertidos exactamente a racionales y los extremos decimales racionales. `vn_range` toma diferencias exactas en ambas curvas.

   [INFERENCE] Las velocidades exteriores son encerramientos de `+1`, aproximadamente `+0.4`, aproximadamente `+0.3` y aproximadamente `−0.2`. El signo de la cara izquierda es positivo porque su coordenada se mueve hacia valores negativos. La afinidad garantiza que basta evaluar ambos extremos temporales. La partición racional cubre todo el intervalo sin huecos.

   **Condición de concesión:** [INFERENCE] Interpretar la curva binary64 como la curva afín real de extremos binary64, tal como hace el código.

6. **Acta 6 — Vacuidad de `fresh_ir`. Clasificación: REQUIERE_CORRECCIÓN en la garantía del control.**

   [SOURCE] El control exige por separado que aparezcan `"define "` y el nombre Python en alguna parte del módulo. No exige que ese nombre corresponda a la definición del cuerpo numérico. Recompila otro dispatcher; los cálculos anteriores utilizaron los originales con `cache=True`.

   [INFERENCE] La ausencia de firmas no permite un pase global vacío: `uncompiled` hace fallar `ok`. Sin embargo, las dos búsquedas textuales admiten estructuralmente un módulo con una definición auxiliar y el nombre buscado solamente en una declaración o metadatos. Tampoco prueban cobertura de cuerpos delegados, incluidos los paralelos, ni equivalencia con el código previamente ejecutado desde caché.

   [UNVERIFIED] No consta que tales omisiones hayan ocurrido en esta ejecución. Los 4556 caracteres y el mutante detectado no las descartan por sí solos.

   **Condición de concesión:** [INFERENCE] Acreditar correspondencia con el código ejecutado y cobertura de sus cuerpos numéricos; alternativamente, mantener explícitamente esa correspondencia como condición del pase.

7. **Acta 7 — Dependencia puntual oculta y precisión publicada.**

   **Clasificación: SE_SOSTIENE respecto a la uniformidad.** [INFERENCE] No encuentro uso de `gate.LAM`, `V0`, `V1`, `UOUT` o `UIN` como valores uniformes. Pesos, logaritmos, calibraciones y tablas de pares se reconstruyen sobre los rectángulos de cada caja. Las tablas escalares globales dependen de `w`, y las velocidades son constantes por afinidad.

   **Hallazgo adicional: MENOR.** [SOURCE] El mínimo publicado es `0.006648095518840022`, pero el acta afirma `drho/dt≥0.0066481`.

   [INFERENCE] La segunda cifra es mayor: esa desigualdad más fuerte no está certificada. Esto no afecta al signo.

   **Condición de concesión:** [INFERENCE] Publicar una cota truncada hacia abajo, por ejemplo `drho/dt≥0.00664809>0`.

Veredicto: AUDIT_PASS_CONDITIONAL_IR_EJECUTADO_Y_COTA_DECIMAL