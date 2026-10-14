# Expectativa previa (escrita por Claude Opus 5.5 ANTES de enviar el encargo a gemini-4-argon)

Fecha: 2026-10-13. Sirve para puntuar la respuesta contra criterios fijados de antemano.
Son criterios de Claude, no verdades: Claude puede estar equivocado en cualquiera de ellos.

Lo que un buen revisor debería encontrar:

E1. Trivialidad: el §6 se satisface vacuamente. Basta D_1, D_2 que difieran en un ingrediente
    que no altere Δ (o lo reescale sin cambiar el cruce de θ) y una regla IR que devuelva un
    conjunto pequeño (p. ej. {τ}) frente a un T_caus con más de un elemento. Igualdad + inclusión
    estricta salen gratis. Falta exigir que D_1, D_2 sean distinguibles fuera de IR (o en la
    respuesta completa) y que la regla IR no sea degenerada.
E2. Tipado: T_IR^D se define como IR(Q_s, τ; R_IR) — una función de escalares que debe devolver
    un conjunto de tiempos; ni su codominio ni su relación con T_caus están fijados. Sin eso,
    "⊊ T_caus" puede no tener sentido.
E3. Cuantificadores ausentes: §6 no dice si es ∀N, para N grande, casi seguro, en esperanza,
    ∀s o ∃s. "C_N" es aleatorio (ley μ_N), así que la igualdad de conjuntos necesita un modo
    de convergencia/probabilidad.
E4. "Arrival time": con Δ no monótona, τ como ínfimo puede no ser un "tiempo de llegada";
    convención en malla/empates abierta.
E5. Construcción concreta en el punto 3, verificable a mano.

Puntuación: cuántos de E1–E5 detecta, si sus construcciones son correctas al comprobarlas, y si
añade objeciones válidas que Claude no previó (eso cuenta a favor). Errores matemáticos o
literatura inventada cuentan en contra.
