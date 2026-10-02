# Pendientes después del PR #9 — 2026-10-02

Base comprobada: `main @ d5567eb68bb5c2883d7fb786a0c0d7d64695d826`.
Esta nota ordena el trabajo; no abre simulaciones ni promociona resultados.

## 1. Conciliar el estado operativo — completado documentalmente

El PR #9 está fusionado y B1.5–B1.7 incluidos con sus generadores.
La hoja `docs/hoja_de_ruta_21-27_septiembre_2026.md` del checkout
`research/causal-fidelity-bridge` describe S1 bloqueado y S2 no abierto.
Ese estado no debe transportarse al main integrado:

- `docs/program_reopening_note_2026-08-28_R4.md` §10 registra R4 firmado.
- `docs/program_s2_authorization_2026-08-28.md` §4 registra la autorización
  explícita posterior de S2 y `STOP_AFTER_S2`.
- `research_program/work_packages/wp6_d2_geometric_tangent_classification.md`
  cabecera registra la reparación G1/G2 y la clasificación S1.
- `research_program/work_packages/wp6_d2_geometric_fisher_retention.md`
  cabecera registra `PROVED_BY_ASSEMBLY` y la parada posterior.

Se comprueba el estado documental, no se reauditan aquí esos teoremas.
El comité 051 y la hoja semanal se conservan como registros de sus momentos.
No se reabre S2 ni se deduce autorización de S3.

## 2. Fidelidad causal — prioridad de trabajo actual

Revisar las definiciones antes de buscar el resultado IR. El contrato original
de septiembre permanece intacto; el gate de octubre exige G0–G4.
El addendum `research_program/causal_fidelity/DEFINITION_REPAIR_2026-10-02.md`
separa la invariancia matemática, el reloj operativo y el soporte dinámico.
Incluye un primer candidato analítico y lo descarta para inferir una frontera
por soporte: el soporte resulta idéntico al permitido por construcción.

La continuación `IR_OPERATIONAL_DEFINITION_2026-10-02.md` define el mapa
temporal y los límites de la variante operativa; su primer caso falla en
inclusión estricta. La lectura del atlas QCA identifica un requisito distinto
para el IR físico: sector de baja energía y transferencia de la respuesta.
El mismo documento demuestra que `Q=tau` no determina ni la respuesta de
frecuencia cero ni su primer momento normalizado en una clase finita explícita.
La continuación autorizada `SLOW_PROTOCOL_RESPONSE_2026-10-02.md` propone
ampliar el blanco a la respuesta lineal entre protocolos lentos. Define el
sector común y demuestra suficiencia para sus lecturas y un contraejemplo
de misma llegada con distinta respuesta conservada. Es una propuesta
analítica sin revisión independiente; no reemplaza el contrato histórico.
`GROWING_FAMILY_RESPONSE_2026-10-02.md` fija esos datos para un refinamiento
de dos rutas y deriva un límite fuerte de respuesta no nulo en L2([0,4)).
Las llegadas normalizadas coinciden, pero las respuestas lentas difieren:
la lectura constante las separa en 93/256 para todo n. Esta unidad analítica
queda cerrada; la interpretación física del reloj y de la dinámica, el sector
de energía de estados y la frontera intrínseca siguen pendientes.

DeepSeek revisó la versión 71a5adf y emitió `REQUIERE_CORRECCION`.
Se aclaró el alcance del contraejemplo y se detalló el lema de convergencia,
corrigiendo dos errores de la sugerencia del revisor al contrastarla.
Registro: `reviews/2026-10-02-slow-response-retry/comprobacion.md`.
Las dos objeciones están respondidas, sin declararlas resueltas.

## 3. B4 — aparcado por condición técnica

`research_program/puente_3p1/2026-09-12/B4_n3_local_identifiability_spec.md`
§5 y terminal canónico: `PARKED / N3_RANK_UNRESOLVED`.
Reapertura sólo con cuadratura certificada y resto formal para las integrales
de B4.3, conservando punto, chart, escalado y familia. No se intenta ahora una
biblioteca general de cuadratura, un nuevo punto, n=4 ni diferencias finitas.

## 4. Saturación relativista — backlog conceptual

`dev/RELATIVIDAD_STOP_2026-09-13.md` mantiene la parada. Necesita un frente
intrínseco, no tautológico y distinto del soporte. El candidato de la prioridad
2 no satisface ese criterio ni reabre Gate M, S, E3 o E4.

## Límite de esta unidad

Documentos de trabajo en la rama `research/causal-fidelity-definition-repair`,
publicados por petición del usuario; conservan su estado de borrador.
Cero experimentos nuevos, cero
semillas y cero cambios al instrumento sellado. Los controles B1 históricos
no se usan como evidencia dinámica. No se convoca comité ni se envían textos
a servicios de revisión externos salvo los dos intentos a DeepSeek
expresamente autorizados y registrados; el primero no devolvió informe.
