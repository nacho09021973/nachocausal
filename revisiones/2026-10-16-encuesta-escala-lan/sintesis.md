# Síntesis de la encuesta sobre la escala LAN, 2026-10-16

Respuestas por separado y a ciegas al mismo `dossier.md`. Herramientas `fbc5b3c`.
Gemini falló con un 402 (créditos de prepago agotados en AI Studio). Grok falló al
primer intento porque el lanzador pide `grok-4.6`, que ya no existe; se repitió con
`GROK_MODEL=grok-4.7` (los fallos están en `fallo_1_*`).

| Modelo | Veredicto | P2 (Teorema A → cota de dos puntos 1/√(nJ̄)) | Recomendación |
|---|---|---|---|
| gpt-6-astra | DEPENDE (cota de tasa frente a eficiencia con constante) | Sí, con QMD a n fijo en el segmento; el poset por contracción | No perseguir LAN ahora; cerrar antes el corolario de A |
| deepseek-v4-pro | DEPENDE (tasa frente a eficiencia o normalidad) | Sí; huecos menores | No ahora; si hiciera falta, LAN por score condicional y CLT condicional |
| grok-4.7 | DEPENDE (orden de la tasa frente a constante gaussiana) | A solo no; A + C¹ a n fijo, sí | No ahora; escribir el corolario |
| claude-opus-5-5 (misma familia que el evaluador) | NO IMPORTA | Sí; el poset por contracción sin regularidad adicional | Escribir ya el corolario; LAN solo si se cierra el puente Fisher–localización y se quieren constantes |

Consenso (4 de 4):
1. Las cotas inferiores sobre el orden de la tasa no necesitan LAN. A, junto con la
   regularidad C¹ a n fijo, da TV(π_τ, π_{τ+δ}) ≤ (|δ|/2)√(n J̄) y, por dos puntos, una
   cota inferior de localización de orden 1/√(n J̄) para Π_n en la caja EF. El poset
   la hereda por contracción. Es la contrapartida del Teorema 3.8 del manuscrito.
   Falta la cota superior, que es el puente abierto.
2. LAN solo importa para constantes óptimas o eficiencia (Hájek–Le Cam), y además
   requiere el puente Fisher–localización, que está abierto.
3. No perseguir la escala LAN ahora.

Corrección a nuestro documento: Opus y Astra muestran, por separado, que el resto
lineal ‖s_n(τ+h/√n) − s_n − (h/√n)ṡ_n‖ tampoco tiende a 0 en el modelo i.i.d.
regular, que sí es LAN (el resto al cuadrado → 3a² con a = h²I/8; lo rehice y
cuadra). El objeto que proponía el §6 de `wp6_uniform_n_horizon_quotient.md` estaba mal
planteado y se corrige. LAN debe enunciarse sobre la log-verosimilitud.
Discrepancia: el "lema mínimo" de Grok (resto ℓ² en o(n^{-1/2})) cae en ese mismo error.

Aportes sueltos, sin comprobar:
- Opus: cota minimax asintótica local con constante 1/J heredada del experimento
  fuente (todo estimador de Π_n es un estimador de la fuente, que es LAN).
- Opus: para N de Poisson en una caja rectangular en (v, r), la ley de N no depende
  de τ (√−g = 1), así que la cota se extendería con E[N]. [UNVERIFIED]
- Astra: ser imagen fija de una muestra regular no garantiza LAN (contraejemplo:
  observar 1{X̄ > 0}).
- DeepSeek y Opus: si se persigue LAN, por el score condicional E[Σℓ̇ | Π_n] y un CLT.

Frente a `expectativa_previa.md`: acertada (mayoría DEPENDE; P2 sí). No anticipé el
error del §6.
