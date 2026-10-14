# Evaluación de la revisión del addendum de llegada (gemini-4-argon, thinkingLevel=high)

Fecha: 2026-10-14. Evaluador: Claude Opus 5.5, autor del addendum (no es evaluación independiente).
Herramienta: revision-ciega @ ~/herramientas c12c10e. Documentos: addendum @ 98c5742, IROD, GROWING.
Una ronda. Todo lo marcado «comprobado» se rehízo a mano en esta sesión.

## Contra la expectativa previa

| | Detectado | Comprobación |
|---|---|---|
| H1 Lema 1 correcto | sí, con reparo de cuantificador en (ii) | **comprobado**: la cota vale para n ≥ N0 (J_{D,n} puede ser ⊥ en finitos n); enunciado intacto |
| H2 aplicación §2 | sí; añade θ>1 (ambos ⊥) | **comprobado** |
| H3 diferencias o(H_n) son el hueco real | sí (3.2), más fuerte: misma celda de bloque ⇒ J_{1,n}=J_{2,n} a todo n | **comprobado** |
| H4 pregunta abierta §4 | **resuelta** (T4.1, T4.2) | **comprobado**, ver abajo |

## Objeciones no previstas

- **3.1** Inconsistencia en el addendum: NT-Q con «existe θ» frente al resumen de §3 con «para todo θ».
  Construcción con L_n={2n, 2n+⌊√n⌋, 3n}, R_2(2n)=½(1−1/n): las llegadas coinciden en todo
  θ∈[1/4,1/2) y difieren sólo en θ=1/2. **Comprobada.** Usa respuestas retardadas generales (IROD §4),
  no la clase lineal.

## Resultados sobre la clase lineal (R_{i,n}(k)=a_n m_n(k) α_{i,n}^k, m_n = nº de caminos de cobertura)

- **T4.1 (imposibilidad).** Si α_{i,n}∈(0,1] y m_n no crece en L_n, R es no creciente en L_n, así que
  τ∈{k_min, ∞}; con llegada finita en ambos, τ_1=τ_2: NT-Q imposible. **Comprobado.** Cubre la cadena
  de IROD §8 y la familia de dos rutas (m_n≡1).
- **T4.2 (construcción).** 1 cadena de 2n, 8 de 2n+d_n, 1 de 3n; α_1=1, α_2=2^{-1/n}, Θ=[1/3,2/3].
  R_2(2n)=1/4<1/3, R_2(2n+d_n)=2^{1−d_n/n}≥1; τ_1=2n≠τ_2=2n+d_n a todo n; ambos →2/3; K={2/3,1}.
  **Comprobado** (requiere d_n<n para que 2n+d_n≠3n). Con d_n=1 realiza el hueco del retraso O(1).

## Lectura

En IROD, si |τ_1−τ_2| ≥ cH_n entonces los límites difieren; luego **toda** igualdad de llegadas
límite viene de diferencias o(H_n), y la normalización por H_n las borra por construcción. Con el
Lema 1, el test de llegada de IROD equivale a: τ_1/H_n y τ_2/H_n convergen al mismo límite y |K|≥2.
NT-Q sólo separa «idénticas a todo n» de «iguales a primer orden»; no hay, dentro del test de
llegada, una frontera formulable entre diferencia microscópica trivial y contenido IR. Esto apoya la
vía de respuesta lenta (SLOW_PROTOCOL/GROWING), que no depende de un único escalar normalizado.

Correcciones al addendum que se derivan: cuantificador de (ii); NT-Q con «para todo θ∈Θ»;
incorporar T4.1 y T4.2; reescribir §4 con la lectura anterior.
