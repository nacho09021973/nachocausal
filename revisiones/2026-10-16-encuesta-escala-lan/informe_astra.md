<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ fbc5b3c984372ec865171c5a727c7f8bb3c3482f; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 d4f0628a26b0e2ed64c6bd6312fb2b767a773037127a0384c8eea40872c47013; biblioteca sha256 054386f420bdcb2b90f0cdff79e3c0ca76369dc6dcabaa1d849bda2cc06b1356
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: gpt-6-astra, esfuerzo: high, vía: codex exec sellado (codex-cli 0.162.1)
inicio: 2026-10-16T08:31:21Z  fin: 2026-10-16T08:32:44Z
documento: /home/ignac/nachocausal/revisiones/2026-10-16-encuesta-escala-lan/dossier.md ; último commit observado: sin versionar ; sha256 de la copia enviada 25484cda4291c63ef60661dbaec0f2a76112a9a3facaba6717ba26118c240334
entrada_astra.txt sha256 07e59b4102723db4466fac2c116356a375405a5fea7cb8aa1ddb8198334a76e6
respuesta sha256 e8c001dab01bfa7d8002d1019a94dbf101c9f3c64219979122d2ac90e5264a1b
-->

VEREDICTO: DEPENDE (de si se busca una cota inferior de tasa o una teoría de eficiencia con constante óptima)

**1. Qué importa de la escala LAN**

Hay que separar dos propiedades: LAN y una aproximación lineal QMD de la raíz de la densidad del experimento completo, con resto que desaparezca para δ = h/√n. **La segunda no es necesaria para la primera.**

Esto se comprueba directamente en una muestra normal de media τ y varianza uno. Bajo τ, con Z = √n(X̄−τ), la raíz de la razón de verosimilitudes para τ+h/√n es
\[
\exp(hZ/2-h^2/4).
\]
Su aproximación QMD lineal es \(1+hZ/2\). Para h fijo distinto de cero, la distancia L² entre ambas es positiva e independiente de n. Sin embargo, la expansión LAN es exacta. Por tanto, el resultado del Teorema B **no demuestra un obstáculo para LAN**; muestra que esa aproximación lineal no resuelve la cuestión.

Las necesidades concretas son:

- **Cotas inferiores de dos puntos y orden de la tasa:** no necesitan LAN ni ese resto uniforme. El paso decisivo es controlar la distancia entre dos leyes próximas; la integración de la cota de Fisher basta bajo las condiciones del apartado 2.
- **Convolución de Hájek–Le Cam y cota minimax local con constante gaussiana óptima:** su aplicación habitual necesita LAN, información límite positiva y las condiciones del teorema correspondiente —en particular, regularidad del estimador para convolución—. LAN interviene al identificar el experimento límite gaussiano del que procede la cota. No exige la aproximación QMD lineal anterior del experimento completo.
- **Normalidad asintótica de un estimador:** puede demostrarse mediante una representación asintóticamente lineal y un CLT, sin LAN. LAN por sí sola tampoco demuestra la normalidad de un estimador concreto.
- **Eficiencia del estimador sellado:** primero requiere identificar su parámetro objetivo y probar el puente entre frontera y τ. Después necesita una distribución límite y una cota óptima comparable. A y B no proporcionan esos pasos.

Además, ser una imagen fija de una muestra regular no garantiza LAN del canal observado. Como contraejemplo, observar únicamente \(\mathbf1\{\bar X>0\}\) en la muestra normal anterior produce, alrededor de τ=0, una Bernoulli de probabilidad Φ(h): el experimento local conserva un solo bit y no es un desplazamiento gaussiano.

**2. Qué permite demostrar A**

**Sí, combinando A con la QMD a n fijo declarada en el dossier**, siempre que ambas valgan en todo el segmento entre los parámetros comparados.

Escribamos \(P_{n,\tau}=\mathcal L_\tau(\Pi_n)\) y \(s_n(\tau)=\sqrt{P_{n,\tau}}\). La QMD proporciona
\[
\|s_n'(\tau)\|_2^2=\tfrac14 I_n^\Pi(\tau)
\le \tfrac14 n\bar J,
\qquad \bar J=\sup_KJ<\infty.
\]
Como \(S_n\) es finito, la diferenciabilidad en todo el segmento y esta cota implican que \(s_n\) es Lipschitz, por el teorema del valor medio aplicado a sus proyecciones escalares. En particular,
\[
\|s_n(\tau+\delta)-s_n(\tau)\|_2
\le \frac{|\delta|}{2}\sqrt{n\bar J}.
\]
Con la convención \(H=\|\sqrt P-\sqrt Q\|_2\), Cauchy–Schwarz da \(\mathrm{TV}\le H\), y por tanto
\[
\mathrm{TV}(P_{n,\tau},P_{n,\tau+\delta})
\le \frac{|\delta|}{2}\sqrt{n\bar J}.
\]

Para \(0<\bar J<\infty\), eligiendo \(\delta=a/\sqrt{n\bar J}\), con \(0<a<2\), cualquier estimador satisface
\[
\max_{t\in\{\tau,\tau+\delta\}}
P_{n,t}\{|\widehat\tau-t|\ge\delta/2\}
\ge \frac{1-a/2}{2}.
\]
Esta es la cota inferior solicitada. También implica cotas para pérdidas absoluta y cuadrática.

Las condiciones que deben quedar explícitas son:

- Los segmentos deben estar dentro de la región donde valen QMD y A. Para obtener pares separados a esa escala, basta que el espacio paramétrico contenga un intervalo; un compacto arbitrario no basta.
- Una cota numérica sobre Fisher sin regularidad de la curva de leyes no justificaría la integración. Aquí la QMD en cada punto del segmento resuelve ese paso.
- El paso al poset requiere una aplicación o núcleo de Markov independiente de τ desde Πₙ. Entonces TV se contrae y la misma cota vale.

Esto demuestra una **cota inferior**, no la tasa minimax exacta: falta una cota superior para el mismo objetivo.

**3. Recomendación**

Mi recomendación es **no perseguir ahora el resto QMD lineal en ventanas LAN**. Cerraría primero la consecuencia anterior de A.

Perseguiría LAN solo si se autoriza estudiar eficiencia o constantes óptimas. El siguiente objetivo mínimo sería probar directamente
\[
\log\frac{dP_{n,\tau+h/\sqrt n}}{dP_{n,\tau}}
=h\Delta_n-\tfrac12h^2I_\Pi(\tau)+o_P(1),
\quad
\Delta_n\Rightarrow N(0,I_\Pi(\tau)).
\]
Lo cerrarían la convergencia normal del score normalizado y el control del resto de la **log-verosimilitud**. A solo acota su varianza; B no aporta esos controles.