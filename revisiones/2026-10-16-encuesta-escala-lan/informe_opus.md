<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ fbc5b3c984372ec865171c5a727c7f8bb3c3482f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.301 (Claude Code))
inicio: 2026-10-16T08:31:21Z  fin: 2026-10-16T08:33:20Z
documento: /home/ignac/nachocausal/revisiones/2026-10-16-encuesta-escala-lan/dossier.md ; último commit observado: sin versionar ; sha256 de la copia enviada 25484cda4291c63ef60661dbaec0f2a76112a9a3facaba6717ba26118c240334
entrada_opus.txt sha256 07e59b4102723db4466fac2c116356a375405a5fea7cb8aa1ddb8198334a76e6
respuesta sha256 b7ada4ed9ad3ff5ce1c71341b5bb10c8493d7efe837727ceae416a5d01e809a4
-->

VEREDICTO: NO IMPORTA

## 1. ¿Importa la QMD uniforme en escala LAN?

**Lo que demuestro.** La condición que falla en el Teorema B es la linealización en L² de la raíz de la densidad conjunta: ‖s_n(τ+h/√n) − s_n(τ) − (h/√n)ṡ_n(τ)‖ → 0. Esa condición **también falla en el modelo i.i.d. regular**, que sí es LAN.

Sea s_n = s^{⊗n} con s QMD, ρ = 1 − δ²I/8 + o(δ²), δ = h/√n y a = h²I/8. Entonces:

- ‖s_n(τ+δ) − s_n(τ)‖² → 2(1 − e^{−a})
- ‖δṡ_n‖² = 2a
- ⟨s_n(τ+δ) − s_n(τ), δṡ_n⟩ → 2a·e^{−a}

El resto al cuadrado converge a 2 − 2e^{−a} + 2a − 4a·e^{−a} = 3a² + O(a³) ≠ 0. Es O(h²), igual que en el Teorema B. Por tanto esa condición:

- no es necesaria para LAN;
- es, en la práctica, inalcanzable para cualquier experimento con información de orden n.

El dossier ya lo insinúa con el módulo de orden nδ en el caso gaussiano. LAN es un enunciado sobre la log-verosimilitud en probabilidad, no sobre el resto en L² de s_n.

**Qué resultados necesitan LAN (para Π_n) y en qué paso:**

- **Teorema de convolución de Hájek y minimax asintótico local con constante 1/I^Π para Π_n.** El paso que lo exige es la convergencia de los experimentos locales a un desplazamiento gaussiano N(h, 1/I^Π). Para ello hacen falta:
  - (a) I_n^Π/n → I^Π(τ);
  - (b) un TCL para el score normalizado;
  - (c) un resto o_P(1) en la log-verosimilitud.

  El Teorema A solo da una cota superior; no da (a), (b) ni (c).
- **Eficiencia del estimador sellado.** Exige lo anterior más una expansión del estimador. Además depende del puente Fisher→localización, que está abierto.
- **Contigüidad de P_{τ+h/√n} respecto de P_τ.** Una cota sobre H² no basta; hace falta algo del tipo LAN o el primer lema de Le Cam.

**Qué resultados no la necesitan:**

- **Cotas de dos puntos, Le Cam y Assouad sobre el orden de la tasa.** Solo usan H² ≤ (δ²/4)·sup I_n sobre el segmento (ver la pregunta 2).
- **Normalidad asintótica del estimador sellado.** Es un TCL del propio estimador y no requiere LAN del modelo. LAN solo entra si se quiere afirmar que esa varianza es óptima.
- **Una cota minimax local con constante 1/J (gratis, con una condición).** Si J es la información por punto de la muestra i.i.d. regular fuente del Teorema A, todo estimador función de Π_n es también un estimador en el experimento fuente. Ese experimento es LAN por QMD y el segundo lema de Le Cam, de modo que el teorema minimax asintótico local de Hájek–Le Cam aplicado a la fuente da:

  lim_{c→∞} liminf_n sup_{|h|≤c} E[n(T_n − τ − h/√n)²] ≥ 1/J(τ).

  Esta cota es válida pero posiblemente no es ajustada para Π_n.

## 2. ¿Basta el Teorema A para la cota de dos puntos?

**Sí, para Π_n.** Fijo n, s_n es un vector finito y, por el Teorema B, de clase C²; en particular es absolutamente continuo. Por el teorema fundamental del cálculo y Cauchy–Schwarz:

‖s_n(τ+δ) − s_n(τ)‖² ≤ δ ∫₀^δ ‖ṡ_n(τ+t)‖² dt = δ ∫₀^δ I_n^Π/4 ≤ δ²·n·J̄/4,

con J̄ = sup_K J < ∞ por continuidad en un compacto. Con H² = ‖·‖², se tiene TV ≤ H ≤ (|δ|/2)√(nJ̄).

Tomando δ_n = 1/√(nJ̄), para todo T_n = T(Π_n):

max_{τ ∈ {τ₀, τ₀+δ_n}} P_τ(|T_n − τ| ≥ δ_n/2) ≥ (1 − TV)/2 ≥ 1/4.

Esto no requiere tensorización, porque Π_n es una sola observación con información de orden n.

**Para el poset sin etiquetas.** Si el poset es función medible de Π_n (el orden en 1+1D es el orden producto en (u, v) dentro de la caja), la contracción de Hellinger bajo aplicaciones medibles da la misma cota **sin ninguna regularidad adicional**. La parte del Teorema A sobre el poset sobra para este fin. Si esa identificación fallara (por ejemplo, si la caja no es causalmente convexa), habría que usar directamente el enunciado del Teorema A para el poset.

**Huecos menores:**

- **Segmento dentro de K.** Hace falta [τ₀, τ₀+δ_n] ⊂ K, o un entorno donde valgan A y B. Basta con τ₀ interior y n grande.
- **Identificación de la información.** Debe verificarse que ‖ṡ_n‖² = I_n^Π/4, es decir, que el I_n^Π del Teorema A es la información asociada a s_n. Si algún π_σ se anula, esto exige cuidado; doy por hecho que el Teorema B lo excluye en K.
- **Solo n fijo.** El caso de N de Poisson sigue abierto.
- **Sin cota superior.** A diferencia del manuscrito, esto **no** establece que la tasa minimax sea n^{−1/2}: falta una cota superior basada en el orden, y eso es precisamente el puente abierto.

**Opinión.** Esta cota no contradice la cota 1/n de la ley de un punto en (u, v), porque esa ley contiene más información. Sugiere que el orden por sí solo pierde la ventaja del soporte móvil. No es concluyente: 1/n era solo una cota inferior.

**Observación no autorizada (para el caso de Poisson).** En coordenadas EF entrantes 1+1D, √(−g) = 1. Si la caja es un rectángulo en (v, r), la ley de N no depende de τ, y la afinidad de Hellinger del par (N, Π_N) es E_N[ρ_N]. La cota se extendería entonces con E[N] en lugar de n. Hay que verificarlo antes de afirmarlo.

## 3. Recomendación

**No perseguir ahora la QMD uniforme en escala LAN.** Como objetivo está mal planteada: falla incluso en el modelo i.i.d. regular.

1. **Ahora:** redactar el corolario de dos puntos de la pregunta 2 para Π_n y para el poset. Es la contrapartida directa del manuscrito y está esencialmente demostrado.
2. **Opcional y barato:** la cota minimax asintótica local con constante 1/J heredada de la fuente.
3. **Solo si ocurre X**, donde X es que se cierre el puente Fisher→localización con un estimador basado en el orden que alcance n^{−1/2}, y además se quieran constantes óptimas o eficiencia. En ese caso, el lema mínimo sería **LAN para Π_n en τ₀** en forma de log-verosimilitud:

   log dP_{τ₀+h/√n}/dP_{τ₀} = hΔ_n − h²I^Π/2 + o_P(1), con Δ_n ⇒ N(0, I^Π).

   **Cómo se cerraría (opinión, no demostrado):** el score de Π_n es E[Σ_i ℓ̇(X_i) | Π_n], la proyección del score de la fuente. Bastaría con:
   - (a) I_n^Π/n → I^Π(τ) localmente uniformemente en K;
   - (b) un TCL para n^{−1/2}·E[Σℓ̇ | Π_n], por ejemplo mediante una descomposición tipo Hoeffding;
   - (c) control en probabilidad, no en L², del resto de segundo orden.

   Si I^Π < J, la cota 1/J del punto 2 queda estrictamente por debajo de la óptima, y solo este lema daría la constante correcta.
