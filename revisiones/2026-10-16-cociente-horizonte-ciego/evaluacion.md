# Evaluación de la revisión ciega de DeepSeek (deepseek-v4-pro), 2026-10-16

Evaluador: Claude. Informe: `informe_deepseek.md` (COMPLETED, finish_reason=stop,
13 min). Herramientas `fbc5b3c`. La entrada no identificaba a los generadores.

Veredicto del revisor: **correcta con salvedades menores**; no encuentra ningún paso roto.

Por paso:
- L1–L2: exactos salvo empates de probabilidad cero. Revisa los bordes (D=0) y
  el horizonte (D→∞). Coincide con la comprobación numérica C1.
- L3: correcta. La verifica por una segunda vía, la supervivencia
  P(J=j, D>d) = t_d/L, y comprueba la normalización por lado.
- L4: correcta, a condición de escribir la dominación L² explícita. Aporta
  una cota que la nota no tenía: t ≤ L e^{−d/(2τ_max)}, |∂_τ √f| ≤ C(1+d) e^{−d/(4τ_max)}.
  Duda del número del lema de van der Vaart. La biblioteca no tiene el libro, así
  que la cita sigue [UNVERIFIED]; el criterio que usa es estándar.
- L5: correcta; φ no oculta dependencia de τ.
- Compatibilidad: no hay contradicción con el no-QMD de un punto. Lee la frase de
  wp6 §5 (líneas 154-156) como refutada en su lectura fuerte.
- Mejora: la cota es natural en orden n pero no en la constante. La simulación
  ya mostraba un cociente I_n/(nJ) de 0.15 a 0.31 con n ≤ 4.

Frente a `expectativa_previa.md`: coincide ("correcta con salvedades", la salvedad
está en L4). No se materializó ninguno de los dos riesgos de error real.
Riesgo comprobado después del informe: wp6 define Π_n con la convención inversa
(se ordena por U y se toma el rango en V; `wp6_domain_bridge_fixed_ef_box.md:161-163`).
Es la inversa σ⁻¹ de la permutación de la nota, y la inversión es una biyección fija
de S_n que no depende de τ. Por tanto π^wp6_σ = π^nota_{σ⁻¹}, el Fisher es idéntico y
φ determina también la Π_n de wp6. Riesgo cerrado.

Estado: dos familias generaron la idea (Anthropic, OpenAI), una tercera la revisó
(DeepSeek) y la comprobación numérica la apoya. Ninguna persona la ha leído.
Ningún estado del repo cambia sin decisión del PI.
Parte (b), el módulo Ω: no la cubre esta revisión; sigue abierta.
