**El lema E1 se sostiene; la identificación incondicional de §3 con la fórmula de B1.2 necesita corrección.** Distingo la equivalencia geométrica, válida para cualquier dominio producto, del criterio mediante un supremo, que exige justificar dominio, alcanzabilidad y casos degenerados.

1. **Antípodas — `SE_SOSTIENE`.**

   [SOURCE] E1 toma `Δ ∈ [0,π]` y permite elegir cualquiera de los dos sentidos cuando `Δ=π`.

   Ambos semicírculos ecuatoriales unen los extremos y tienen longitud π. La desigualdad `ℓ(1)≥π` garantiza que la construcción llega al extremo correcto; no necesita unicidad del arco mínimo. Para `Δ=0`, la componente angular queda constante.

   **Condición mínima de concesión:** ninguna adicional.

2. **Regularidad — `SE_SOSTIENE`.**

   Para una curva absolutamente continua en la esfera, la velocidad intrínseca existe casi por doquier, es integrable y su integral define la longitud recorrida. Por tanto, `ℓ` es absolutamente continua. La función real `t↦min(t,Δ)` es Lipschitz; su composición con `ℓ` conserva la continuidad absoluta y satisface `|α′|≤|ω′|` casi por doquier.

   Para curvas localmente Lipschitz, el mismo argumento funciona localmente; sobre el intervalo compacto indicado también proporciona longitud finita. La expresión angular debe entenderse como un punto de `S¹`, mediante `e^{iα}`, sin exigir una coordenada global `φ`.

   **Condición mínima de concesión:** interpretar la regularidad y la velocidad en sentido intrínseco, como corresponde a curvas en una variedad.

3. **Orientación y dominio — `SE_SOSTIENE`.**

   [SOURCE] La construcción conserva exactamente `U(λ)` y `V(λ)`.

   Así conserva su monotonía futura y todos los puntos de la proyección radial. La reducción de velocidad angular mantiene la desigualdad causal. Esto funciona incluso si `D` tiene agujeros o carece de convexidad: se reutiliza una curva existente, sin sustituir su recorrido radial.

   **Condición mínima de concesión:** `D` pertenece al sector regular donde `C,r>0`, y la restricción angular es el ecuador completo. No necesita convexidad de `D`.

4. **Ley angular y volumen — `SE_SOSTIENE`.**

   Para dos ángulos independientes uniformes, su diferencia módulo `2π` es uniforme. Al plegarla mediante la distancia mínima se obtiene densidad `1/π` en `[0,π]`; por tanto, para `b≥0`,
   `P(Δ≤b)=min(b,π)/π`.

   El bloque radial tiene `gUV=−C/2`, de modo que las densidades de volumen son `Cr/2` en el ecuador y `Cr² sinθ/2` en cuatro dimensiones. Con las expresiones suministradas resultan los pesos normalizados `e^{−s}` y `s e^{−s}`, respectivamente.

   **Condición mínima de concesión:** conservar las hipótesis declaradas de uniformidad e independencia angular y absorber únicamente constantes en la normalización.

5. **Puente entre B1.2 y existencia causal — `REQUIERE_CORRECCIÓN`.**

   **Caso degenerado concreto.** Tómense `Ux<Uy`, `Vx=Vy>0` y ángulos iguales, dentro del sector regular. Existe la curva nula radial con `V` constante. Sin embargo, ninguna función `U(V)` puede satisfacer dos valores distintos en el mismo argumento: la familia variacional escrita en B1.2 está vacía.

   [SOURCE] B1.2 §3 declara cero las cotas cuando `dV=0`, pero §2 no introduce una definición especial que repare esa familia vacía.

   Si `dU=0<dV`, sí existe la gráfica constante y su capacidad angular es cero. Cuando cualquiera de los incrementos es cero, la causalidad fuerza movimiento angular nulo. También hace falta que el segmento radial esté contenido en el dominio.

   **Igualdad y supremo.** De un supremo positivo se obtiene alcanzabilidad para `Δ<sup L`; la igualdad no se deduce sin más. En un rectángulo causal compacto íntegramente admisible, con `q` suave y positivo y ambos incrementos positivos, la métrica auxiliar `h=−q²dU dV` admite una geodésica temporal maximizadora. Esta tiene `V` estrictamente creciente y proporciona una gráfica admisible: allí queda justificada la igualdad.

   Para un `D` arbitrario, puede fallar. Considérese un pequeño diamante causal con maximizadora temporal única, de longitud `T<π`, y elimínese un punto interior de ella. Curvas que evitan ese punto aproximan longitud `T`, pero ninguna la alcanza. Con extremos ecuatoriales separados angularmente por `T`, el criterio `Δ≤sup L` acepta el par aunque no existe curva causal. E1 sigue siendo válido: no existe en ninguna de las dos dimensiones.

   Además, si `sup L>π`, la igualdad `Δ=Delta_max=π` puede admitir curvas temporales; el recorte en π no identifica una frontera nula.

   **Condición mínima de concesión:** tratar explícitamente los incrementos nulos y limitar la fórmula exacta a dominios con alcanzabilidad justificada y trayectorias admisibles. E1, por sí solo, no acredita esas condiciones para el parche citado.

Veredicto: AUDIT_PASS_CONDITIONAL_DOMINIO_ALCANZABILIDAD_Y_DEGENERADOS