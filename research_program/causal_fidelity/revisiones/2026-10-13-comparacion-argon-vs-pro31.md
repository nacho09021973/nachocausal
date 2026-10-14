# gemini-4-argon (por defecto y thinkingLevel=high) frente a gemini-3.1-pro-preview: mismo encargo

Fecha: 2026-10-13. Evaluador: Claude Opus 5.5 (un solo encargo, una ronda: anecdótico, no un benchmark).
Encargo idéntico (cuerpo enviado comprobado con diff) sobre CAUSAL_FIDELITY_MINIMAL_CONTRACT.md, criterios
fijados antes en expectativa_previa.md. Informes: 2026-10-13-argon-contrato/ (Argon por defecto), 2026-10-13-argon-high-contrato/
(Argon, GEMINI_THINKING=high), 2026-10-13-pro31-contrato/.
Herramienta: revision-ciega @ ~/herramientas 6d7ba21 (Argon por defecto, Pro 3.1); la corrida high, con la
opción GEMINI_THINKING añadida después (ver cabecera de su informe).

| | Argon por defecto | Argon high | Pro 3.1 |
|---|---|---|---|
| Tiempo | 43 s | 105 s | 64 s |
| Tokens de salida / de razonamiento declarados | 4340 / no declarado | 3978 / 7365 | 2385 / 5242 |
| Límite de 1500 palabras | lo excede (~1860) | lo excede | lo respeta (~1090) |
| E1 test trivial | sí; tres vías (τ=∞, IR constante, D1=D2) | sí; τ=∞, tautología de cardinalidad (singulete), FAIL por futuro vacío | sí; una vía (τ=∞) |
| E2 tipado de T_IR | sí | sí | sí |
| E3 cuantificadores | sí | sí | sí |
| E4 Δ no monótona | no | parcial (interpolación del ínfimo) | no |
| `t` sin sentido intrínseco en un poset | sí | sí | sí |
| IR con C_N fijo, sin N→∞ | sí, como error de firma | sí: N ligada por IR, no libre | sólo al final, de pasada |
| Detector ausente de la firma | sí | sí | no |
| C_N familia vs instancia | sí | sí | sí |
| Cláusulas correctoras | tres, específicas | cuatro, específicas (incl. misma álgebra de conjuntos: semirrectas) | una, más genérica |
| §3 caso concreto: aritmética | errores (poset mal cerrado transitivamente, cuenta mal caminos) | correcta en lo comprobado (π(1)=p, cotas α≤p, monotonía de Δ, τ_N→1/p) | correcta |
| §3 caso concreto: honestidad | lo vende como "no trivial, PASS demostrado" aunque repite el patrón trivial que él mismo señaló | caso con contenido y con N→∞ real; afirma sin probar que Δ_D1≠Δ_D2 para todo N finito | admite que es ad hoc: Δ no depende de C_N y el PASS no tiene contenido causal |

Lectura:
- Argon por defecto razona poco (no declara tokens de razonamiento en este encargo; 62 en una prueba
  mínima, 580 con thinkingLevel=high). Pro 3.1 razona más por defecto. La comparación justa es Argon high
  frente a Pro 3.1.
- Argon high es el mejor de los tres en crítica y en construcción. Su §3 es el único caso con contenido:
  cadena C_N con N→∞, dos paseos causales con la misma deriva p y distinta memoria; por la ley de grandes
  números el frente IR es [1/p,∞) en ambos, estrictamente dentro del cono [1,∞). Es decir: el IR sólo ve
  la velocidad media y la pérdida estricta es la subluminalidad (p<1). Correcto, pero es un ejemplo de
  juguete conocido en forma (límite hidrodinámico), no un resultado; y cambia el contrato (añade detector y
  reescalado t=k/N), cosa que declara.
- Argon por defecto: buena crítica, construcción con errores elementales y tono de certeza.
- Pro 3.1: crítica correcta y menos detallada; construcción correcta pero vacía, y lo reconoce.
- Recomendación: usar Argon con GEMINI_THINKING=high para revisiones; comprobar a mano toda construcción.
- Un encargo, una ronda: anecdótico. No generaliza a otros tipos de tarea.
