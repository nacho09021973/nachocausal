# Expectativa previa (escrita por Claude Opus 5.5 ANTES de enviar el encargo)

Fecha: 2026-10-14. Criterios de Claude, no verdades; Claude redactó la v2 y puede tener puntos ciegos
sobre ella (por eso la revisión es de otra familia).

Lo que un buen revisor debería encontrar o discutir:

F1. Δ con valores en [0,1] y τ_D ≥ τ_caus por instancia: con Δ = probabilidad de alcance y θ>0, la
    inclusión T_IR ⊆ T_caus es automática; el contenido está sólo en la desigualdad estricta y en la
    igualdad. ¿Lo señala, y ve que eso es buscado y no un defecto?
F2. Límites constantes: excluye familias donde τ^IR es aleatorio (p. ej. posets aleatorios con
    fluctuaciones que no se autopromedian). Posible estrechamiento excesivo.
F3. λ = cadena más larga y A = enlaces de Hasse: en posets densos (sprinkling) la cadena más larga
    crece como N^{1/d} y los caminos de Hasse más cortos son muy cortos; τ_caus^IR podría ser 0 y
    la pérdida estricta salir gratis (τ^IR > 0 = τ_caus^IR). Esto sería un PASS barato no excluido
    por NT1–NT5.
F4. NT3 pide diferencia de leyes de Δ para N grande, pero no que la diferencia sea "en el ingrediente":
    dos dinámicas que difieren en algo irrelevante pasan NT3.
F5. Modo M "de la esperanza" mezclado con τ (función no lineal): lim E[τ] ≠ τ de lim E[Δ].
    Ambigüedad de qué se promedia.

Puntuación: cuántos de F1–F5 detecta, si sus construcciones son correctas al comprobarlas, y objeciones
válidas no previstas (a favor). Errores matemáticos o literatura inventada, en contra.
