# plan_julio_2026_v3.md — Plan interno de trabajo tras el cierre de R-VAR

> **DOCUMENTO INTERNO DE TRABAJO — 2026-07-05.** No constituye pre-registración, no fija umbrales
> y no autoriza freeze, validación ciega, publicación ni cambios de geometría. Todo paso one-way
> exige `/comite` y autorización explícita del PI. Se mantienen sin cambio:
> `RESPECT_SEAL_FREEZE`, `NO_RECONSTRUCTION_CLAIM`, `NO_GROUND_TRUTH_LEAKAGE`,
> `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`, `R_VAR_STATUS = CLOSED_NEGATIVE_RESULT`.

## Alcance

Este documento organiza el trabajo posterior al cierre de R-VAR sin reabrirlo ni reinterpretarlo
como reparación. El cierre negativo se toma como resultado establecido. La estructura separa cuatro
frentes que no deben mezclarse:

1. consolidación del resultado existente y preparación de Paper I;
2. deuda bibliográfica y limpieza del árbol de trabajo;
3. exploración dev futura de la ruta 2;
4. eventual prereg-004, solo si existe una señal dev nueva y suficiente.

La prioridad operativa de julio sigue siendo Paper I. Ninguna línea exploratoria desplaza ese orden.

## 1. Paper I

Paper I es la línea principal de consolidación. Su función es fijar, con lenguaje trazable, lo que
ya quedó congelado y auditado. No consume semillas, no altera el sello y no requiere cambios de
geometría.

Contenido previsto:

1. Benchmark de recuperabilidad, no claim de reconstrucción.
2. Protocolo: pre-registración congelada, sello SHA-256, separación dev/validación, semillas
   quemadas, comité adversarial y auditoría de integridad.
3. Resultado negativo 1: prereg-001 FAIL y su diagnóstico.
4. Resultado positivo: estimator-v2 y `prereg-002 PASS [etiqueta completa]`.
5. Límite operacional: prereg-003 y su suelo `O(\ell)` con los `NOT` intactos.
6. Resultados negativos acotados: cascada de objeto extendido y cierre R-VAR como resultados
   documentados, no como derrota del proyecto.
7. Límites y trabajo abierto: minimax sobre `C`, caveat regular-BH y finitud del parche.

Pasos:

- E1.1 Resolver la deuda O4: Tsybakov 2009 y Bretagnolle-Huber, con nota derivada.
- E1.2 Redactar el borrador en `docs/paper/`.
- E1.3 Someter cada afirmación a auditoría documental.
- E1.4 Elevar el borrador a `/comite` para decisión de publicación.

## 2. Deuda y limpieza

La deuda bibliográfica y la higiene del working tree son tareas de soporte. Deben completarse sin
mezclar reparación con exploración.

Incluye:

- incorporación de las referencias O4 cuando corresponda;
- revisión de `INSTRUCCIONES.md` si sigue pendiente;
- gestión explícita de los `.als` sueltos;
- revisión de `Esquema completo.png` y de `memoria_claude/` con alcance delimitado.

Este frente no autoriza nuevas preguntas ni modifica el estado de R-VAR.

## 3. Ruta 2 en dev

La ruta 2 de horizonte aparente con expansión discreta `E` permanece como candidata de exploración.
No es una reparación de R-VAR ni una continuación encubierta del cierre negativo. Debe tratarse como
una pregunta nueva.

Lenguaje admitido:

- podría ofrecer una alineación más natural con horizontes aparentes;
- podría depender menos de una singularidad física que la ruta 1;
- requiere validación antes de cualquier afirmación fuerte;
- incorpora un control obligatorio contra el modo de fallo observado en R-VAR.

Lenguaje no admitido todavía:

- “resuelve” el fallo de R-VAR;
- “garantiza” robustez;
- “superior” sin validación;
- cualquier formulación que convierta la ruta 2 en argumento de reparación retroactiva.

La geometría nueva solo puede elegirse dentro de una pregunta nueva, antes de freeze, y no como
retuning de semillas vistas. Esa decisión pertenece a la fase dev, no a una recuperación sobre
material ya observado.

Pasos:

- E3.1 Exploración dev con `EXPLORE_POOL` y medición de la señal.
- E3.2 Fijación de geometría solo dentro del diseño de la pregunta nueva.
- E3.3 Si existe señal nueva y suficiente, elevar el caso a `/comite`.
- E3.4 Solo después, si procede, definir una prereg-004 con semillas nuevas y disjuntas.

## 4. Posible prereg-004

prereg-004 no forma parte del plan operativo inmediato. Solo puede considerarse después de que la
ruta 2 produzca una señal dev clara, documentada y separada de R-VAR.

Condiciones de referencia:

- no usar geometría heredada por inercia;
- no reutilizar semillas vistas para reinterpretarlas como nueva hipótesis;
- no convertir un negativo previo en justificación de una autorización posterior;
- no confundir exploración dev con freeze.

## Secuencia

1. Paper I.
2. Deuda bibliográfica y limpieza.
3. Exploración dev de la ruta 2.
4. Eventual comité para definir si existe base suficiente para prereg-004.

## Decision status

- `PLAN_STATUS = INTERNAL_WORKING_PLAN`
- `PREREGISTRATION_STATUS = NOT_FROZEN`
- `R_VAR_STATUS = CLOSED_NEGATIVE_RESULT`
- `PAPER_I_PRIORITY = YES`
- `PHASE2_STATUS = DEV_ONLY_PENDING_AUTHORIZATION`
