# Expectativa previa (escrita por Claude Opus 5.5 ANTES de enviar el encargo)

Fecha: 2026-10-14. Criterios de Claude, no verdades. Claude escribió buena parte del paquete y del
borrador y puede tener puntos ciegos (por eso la revisión es de otra familia).

Lo que un buen revisor debería encontrar o discutir:

G1. El registro de progreso lleva `abstained_BH` por semilla: es información parcial sobre (i)
    visible durante la corrida. Con la regla de caídas, alguien que lo vea podría preferir que
    una corrida se caiga. Sólo es inocuo si el relanzamiento reproduce bit a bit el mismo
    resultado, y eso no está comprobado (O2).
G2. Determinismo de una corrida a otra con 20 hilos: tampoco se ha comprobado; la paridad con la
    GPU en una semilla no lo prueba.
G3. (i) casi se reduce al recuento de abstenciones: con el control plano abstenido
    (`sep_MINK = 0`) y `sep_BH >= 0`, `d >= 0` siempre y la prueba de cambio de signo da
    p = 2^-k con k semillas de d > 0; con 20 semillas y pocas abstenciones pasa por construcción.
    Es igual en 1+1, pero conviene que se diga.
G4. Los tres niveles de ρ usan las mismas 20 semillas: los niveles no son independientes, y la
    holgura de convergencia compara medianas correlacionadas.
G5. Mediana de anchuras sobre las horquillas «limpias» y cobertura sobre las válidas:
    denominadores distintos; un descarte de horquillas no limpias podría mejorar la mediana.
G6. El anclaje θ se eligió conociendo las anchuras de dev (declarado).
G7. `STATUS = "FROZEN"` es una cadena en un fichero: el candado de la etiqueta de validación lo
    abre un commit; la unicidad depende de que `results/validation_004.json` exista y del
    historial git, no del código.

Puntuación: cuántos de G1-G7 detecta, si sus objeciones son correctas al comprobarlas contra el
código, y objeciones válidas no previstas (a favor). Afirmaciones sobre el código que no se
sostienen al leerlo, o literatura inventada, en contra.
