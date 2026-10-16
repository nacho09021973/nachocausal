# Dossier: ¿importa la escala LAN para el canal de permutaciones de la caja EF?

## 1. Programa (contexto)

El programa estudia qué se puede recuperar de la geometría de un parche de
Schwarzschild 1+1D (en particular, información asociada al horizonte) a partir solo
del orden causal y de conteos de un sprinkling de Poisson ("causal set"). El
observable es el poset sin etiquetas con n elementos, o su esqueleto de
permutación Π_n ∈ S_n. El parámetro es τ = 2M en un compacto K.

Resultados ya establecidos:

- **Manuscrito, familia "diamante de esquinas EF fijas"** (otra familia, regular):
  la ley de un punto (densidad de cópula c_τ) es QMD con Fisher I(τ) ≤ Ī. Con la cota
  de dos puntos TV(Q^n_τ, Q^n_{τ+δ}) ≤ (|δ|/2)·√(n Ī), ninguna regla basada solo en
  el orden localiza τ con precisión mejor que del orden de 1/√(n Ī). Hay una cota
  superior que la iguala: la tasa minimax es n^{−1/2}. La prueba solo usa la
  desigualdad integrada de Hellinger, no la expansión LAN.
- **Familia "caja EF fija"** (la de este dossier): la ley de un punto en coordenadas
  nulas (u, v) tiene soporte móvil y no es QMD, con H²(p_τ, p_{τ+δ}) ≥ c|δ|. Para
  esa ley de un punto solo se tenía una cota inferior más débil, de orden 1/n.
  A n fijo, la ley de Π_n es QMD.
- **Nuevo (2026-10-16), Teorema A:** I_n^Π(τ) ≤ n J(τ), uniforme en n, con J
  finita y continua en K, mediante un cociente por lado del horizonte que expresa
  Π_n como imagen fija de una muestra i.i.d. regular. Lo mismo vale para el poset
  sin etiquetas.
- **Nuevo, Teorema B:** ‖s̈_n‖ ≤ C_K n, con s_n = (√π_σ)_σ. Por tanto el módulo
  Ω_{n,K}(η) de la raíz-score cumple Ω ≤ C_K n η, y el resto QMD es uniforme en
  ventanas con n δ_n → 0. **No** se obtiene QMD uniforme en la escala LAN
  δ_n = h/√n: el resto (δ²/2) sup ‖s̈‖ es O(h²), no o(1). En el modelo gaussiano
  producto, el módulo también es del orden de n δ.
- Abierto y no autorizado: el puente entre Fisher y la localización real de un
  estimador basado en el orden (el estimador sellado localiza una frontera), la
  mezcla de Poisson (N aleatorio) y cualquier afirmación en 3+1D.

## 2. Preguntas

1. **¿Importa la QMD uniforme en la escala LAN para este programa?** Di qué
   resultados siguientes concretos la necesitarían (por ejemplo: LAN y teorema de
   convolución o minimax asintótico local de Hájek–Le Cam con constante óptima;
   normalidad asintótica de un estimador; eficiencia del estimador sellado) y
   cuáles no (por ejemplo: cotas inferiores de dos puntos o de Le Cam sobre el orden
   de la tasa).
2. **¿Basta el Teorema A para dar en la caja EF una cota inferior de dos puntos de
   orden 1/√(n J̄)**, análoga a la del manuscrito, para Π_n y para el poset sin
   etiquetas? Si hay un hueco (regularidad necesaria para la desigualdad integrada
   de Hellinger, uniformidad en K, el paso al poset), dilo.
3. **Recomendación:** perseguir la escala LAN ahora, no perseguirla, o solo si
   ocurre X. Si recomiendas perseguirla, di cuál es el siguiente lema mínimo y qué lo
   cerraría.
