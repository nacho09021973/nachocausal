# Expectativa previa (escrita por Claude Opus 5.5 ANTES de enviar el encargo)

Fecha: 2026-10-15. Delta auditado: 782d031..616c55d. Criterios de Claude, no verdades. Claude
escribió todo el delta salvo los informes de Codex y Gemini que contiene.

Lo que un buen auditor debería encontrar o discutir:

A1. El cambio de `seed_manifest.py` toca una ruta sellada después de la auditoría 046; es el
    motivo de esta auditoría. Debería confirmar que es el único cambio en `nachocausal2p1/`.
A2. Con `--full-history`, en un repo lineal o tras un merge normal, el commit que añade el fichero
    sigue siendo uno solo: el caso legítimo no se rompe.
A3. El resquicio residual sigue siendo procedimental: el autor de C1 puede calcular el hash antes
    de publicarlo (declarado), y nada del código ata C1 a un SHA anunciado de antemano.
A4. `mecanica.txt` lo capturó el autor; el auditor no puede comprobarlo. Un buen informe lo marca
    como límite y no lo usa como prueba propia.
A5. Las cifras de potencia del §7 son aritmética en forma cerrada sin script comprometido; están
    marcadas `[UNVERIFIED]`. Un auditor estricto puede pedir un script.
A6. El informe del comité 053 contiene una afirmación del falsador corregida por el presidente
    (045 fue Codex, no Claude): debería verse como corregida, no como error.

Puntuación: cuántos de A1-A6 detecta, si sus hallazgos son correctos al comprobarlos contra el
código, y hallazgos válidos no previstos (a favor). Afirmaciones sobre el código que no se
sostienen al leerlo, en contra.
