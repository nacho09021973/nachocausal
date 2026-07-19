# Marcador de reentrada — pausa del programa (2026-07-19)

ESTADO: PROGRAMA_EN_PAUSA_LIMPIA / NINGUNA_EJECUCION_PENDIENTE / NADA_ABANDONADO
FIRMADO: P.I. / Nacho, 2026-07-19

## Punto de parada

El programa se detiene voluntariamente en un punto limpio, por decisión del PI. No es un cierre
científico ni un abandono: todos los frentes quedan tipados, auditados y commiteados.

Estado al pausar (HEAD en la rama `main`):

- **Gate de viabilidad de Candidate B**: `ADOPTED_AS_GATE_DEFINITION` como filtro precondicional
  (enmiendas A1–A6 + ítems advisory aplicados; decisión 037 firmada §11;
  `research_program/work_packages/candidate_b_viability_gate.md`). Ningún Candidate B abierto.
- **Dossier OP-2.2 BD**: rev. 3, correcciones E1/W1/W2 aplicadas y re-auditadas
  (`docs/auditor/auditor_report_020_...md`, `AUDIT_PASS_WITH_WARNINGS`). Sin terminal OP-2.2;
  V2-support sigue `UNRESOLVED` por diseño; techo `REFERENCE_WITNESS_SEPARATION_ONLY` intacto.
- **Sello**: `make verify-seal` MATCH (`6e2c3888…bfefd4`), sin drift en toda la secuencia.
- **Limpieza**: `pr009-runner-scorer-v2.patch` borrado (verificado superseded — su contenido ya
  está commiteado como §16 del prereg PR009 y los scripts que creaba ya existen).
  `nachocausal-program.local-before-pull.html` se conserva intacto por instrucción del PI.

## Siguiente paso autorizado a considerar (si el programa se retoma)

> Si el programa se retoma, el siguiente paso autorizado a considerar es convocar `/comite` para
> adjudicar una única ejecución del falsifier enumerativo congelado de OP-2.2
> (decisión 035 §5/§9: corrida read-only sobre el código dev ya congelado
> `dev/pr011_tv_certification_enumeration.py`, ejecutada y verificada por alguien distinto del
> autor del dossier). Esa única corrida descargaría V1b (rango numérico `[S_min,S_max]`),
> resolvería V2-support empíricamente, y fijaría el gap real `g` para un V3b honesto.

Este marcador no autoriza esa ejecución ni la convocatoria; solo la identifica. Todo lo demás
(abrir Candidate B, micro-pilot, familia horizon-bearing, reabrir A/PR009/PR010, shadows/`H_A`)
sigue exactamente donde lo dejan las decisiones 035/036/037: cerrado salvo decisión de comité
dedicada + autorización explícita del PI.

## Qué contiene ya el programa, por si no se retoma

Resultados y límites honestos suficientes para justificar el esfuerzo realizado: el PASS de
prereg-002 (localización in-patch del observable de volumen, con sus caveats documentados), el
paquete teórico de Fase 1 y el teorema de dos puntos, la gramática de claims, la cadena completa
de negativos tipados a nivel de banco (R-VAR, PR009/PR010, techo estructural V4b de PR011), y
20 reportes de auditoría con dientes reales. La conclusión estructural que todos los negativos
señalan — que la validación de fidelidad de horizonte exige una familia horizon-bearing con eje
de colocación que este banco no tiene — queda registrada en el dossier OP-2.2 (V4b) y en la
decisión 037.
