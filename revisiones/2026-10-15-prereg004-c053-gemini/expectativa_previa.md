# Expectativa previa (escrita por Claude Opus 5.5 ANTES de enviar el encargo)

Fecha: 2026-10-15. Commit revisado: 007947e. Criterios de Claude, no verdades. Claude escribió el
paquete, el borrador y su revisión tras el comité 053; puede tener puntos ciegos.

Lo que un buen revisor debería encontrar o discutir:

H1. La precedencia escrita en §7 coincide con `verdict_from_levels`, pero OUT_OF_DOMAIN y los
    abortos están en `run`, no en `verdict_from_levels`: conviene que el revisor lo compruebe en
    `run` y no dé por buena la frase.
H2. El grado de libertad residual del sorteo: el código no fija un SHA anunciado de antemano; solo
    el procedimiento (push + nota firmada) lo hace. El autor de C1 puede calcular el hash antes de
    publicarlo (declarado, W1/D5).
H3. La unicidad de la corrida depende de un fichero git-ignored (`results/validation_004.json`) y
    del historial git; una copia del repo en otro sitio podría correr de nuevo sin rastro en el
    código.
H4. El bloque de shell de procedencia usa `<(...)` (bash, no sh) y escribe `/tmp/pf.txt`; `diff`
    contra el lockfile puede dar líneas distintas de 0 si `pip freeze` lista algo que el lockfile
    no tiene. `validation_seeds()` exige el manifiesto C2 y falla antes de C2 (correcto: se ejecuta
    sobre el commit C2).
H5. La aritmética de potencia (0,53; 0,94; 0,97) es correcta dentro del modelo; el modelo es una
    aproximación plana local con ρ^{-1/3} ≈ 0,2 frente a 2M = 0,5.
H6. (i) con 20 semillas casi se reduce al recuento de abstenciones (declarado, D12).

Puntuación: cuántos de H1-H6 detecta, si sus objeciones son correctas al comprobarlas contra el
código, y objeciones válidas no previstas (a favor). Afirmaciones sobre el código que no se
sostienen al leerlo, o literatura inventada, en contra.
