# Nota de ampliación acotada del perímetro — R3

```text
ESTADO: FIRMADA — R3 AUTORIZADO (ver §7)
FECHA: 2026-08-05
AMPLIA: docs/program_reopening_note_2026-07-31.md (perímetro R1, R2)
NO_REVOCA: docs/program_closure_note_2026-07-30.md, que permanece íntegra
SELLO: intacto — no se toca
SEMILLAS: banda virgen [2,000,000–2,999,999] permanece sin quemar
```

## 1. Por qué hace falta esta nota

La regla §6.1 de la nota de reapertura del 31 de julio dice literalmente: *«Perímetro
fijo: R1 y R2. Nada entra sin una nueva nota firmada.»* El trabajo de
`research_program/work_packages/wp6_d2_null_copula_dichotomy.md` **no es R1 ni R2**. Sin
esta nota firmada, ese work package queda como hallazgo fuera de perímetro y su destino
correcto sería `docs/backlog_hallazgos.md`, no el trabajo en curso.

Esta nota no revoca el cierre ni amplía el objetivo clausurado. Añade **un** ítem.

## 2. Qué se añade — un solo ítem

**R3 — La dicotomía de cópula nula en `d=2`.** Establecer, sobre parches que son caja de
coordenadas nulas, que el orden causal de un sprinkling condicionado a `N=n` ve
exactamente la cópula de la medida de volumen, que esa cópula es trivial si y solo si el
parche es plano, y que la clase de invisibilidad es exactamente la órbita del grupo
infinito-dimensional de reparametrizaciones nulas.

Estado a fecha de esta nota, según el work package §8: Lema A, Prop. B, Teorema C y el
corolario de órbita **probados**; Teorema D **probado módulo dos fuentes ya verificadas por
el PI** (HKMMRS 2013; Grübel 2024); un único hueco abierto, el **puente E**.

**Trabajo autorizado bajo R3, lista cerrada:**

1. Cerrar el puente E — que las densidades de patrones de poset determinen las de
   permutación salvo transposición `U <-> V` — por vía directa (combinatoria finita) o
   bibliográfica (OCR de Kelly–Trotter 1982 / Trotter 1995, ya físicos en `biblioteca/`).
2. Redactar el resultado como nota sometible independiente, o como sección del manuscrito
   de límites, a decisión posterior del PI.
3. La auditoría de novedad obligatoria antes de cualquier afirmación de prioridad.

## 3. Por qué es admisible bajo el cierre

La cláusula 1 del cierre acota la prohibición a lo que se abra *«dentro del objetivo de
reconstrucción de horizonte 1+1D/3+1D que este programa perseguía»*. R3 va en dirección
**opuesta**: es un enunciado de identificabilidad y de invisibilidad exacta, no un intento
de reconstruir ni de localizar un horizonte. Su mitad no-go (Teorema C) es un límite; su
mitad positiva identifica la clase conforme **módulo un grupo infinito-dimensional**, que
es precisamente la afirmación de que no se puede hacer más.

Es además puramente deductivo y bibliográfico: **cero semillas, cero simulación, cero
ejecución nueva, sello intacto**. No hay superficie de ajuste post-hoc porque no hay
números que ajustar.

## 4. Tensión declarada, no disimulada

**Con el gate de WP5.** Existe una decisión previa según la cual el trabajo en `1+1D` es
puramente instrumental y solo debe continuarse si sirve demostrablemente al objetivo
`3+1D`. **R3 rompe ese gate a propósito.** El motivo es que el valor de R3 no está en
transferir a `3+1D` —el work package §7.3 declara explícitamente que no se afirma
transferencia— sino en que `d=2` es exactamente la dimensión que HKMM (`d>2`), Braun
(`d>=3`) y Madsen (`d>2`) excluyen. Bajo el gate de WP5, R3 no se haría; el PI debe
decidir si ese gate cede aquí. Si no cede, R3 decae y esta nota no procede.

**Con el estado del programa.** Autorizar R3 significa que el repositorio tiene tres
ítems vivos (R1, R2, R3) en lugar de dos, con R2 venciendo el 14 de agosto y la caja
conjunta el 11 de septiembre. R3 no debe usarse como razón para prorrogar ninguna de las
dos fechas.

## 5. Qué sigue cerrado

Sin cambios respecto de §3 de la nota del 31 de julio, y en particular: reconstrucción de
horizonte en cualquier reformulación; PR004, localizadores C1–C6, anclas de presente,
ladder-braiding; `Q_trap` v2, que sigue `UNADJUDICATED_AT_CLOSURE`; observables nuevos;
extracción de semillas —**ninguna**—; y **lenguaje de novedad absoluta: prohibido**.
`NOVELTY_CERTIFIED = NO` para todo lo de R3 hasta auditoría independiente.

## 6. Test de terminado

R3 está terminado cuando, y solo cuando:

1. el puente E está **cerrado con fuente leída en primaria o con demostración escrita**, o
   **declarado abierto en el texto** con su consecuencia exacta (la dicotomía queda
   completa a nivel de permutación y condicional a nivel de poset);
2. ninguna afirmación de prioridad aparece sin auditoría de novedad;
3. el alcance de §7 del work package —solo cajas nulas, planitud local, solo `d=2`, no es
   reconstrucción— está reproducido literalmente en cualquier texto derivado.

El punto 1 es deliberado: **el puente E no puede bloquear la publicación de la mitad
probada.** El Teorema C es un no-go exacto y se sostiene solo.

## 7. Firma

```text
FIRMADA_POR: Ignacio (PI)
FECHA: 2026-08-05
AUTORISED_SCOPE: R3 (lista cerrada de §2)
DECISION_R3: AUTORIZADO
DECISION_PUENTE_E: AUTORIZADO EL ATAQUE
GATE_WP5_CEDE_AQUI: SI — el valor de R3 está en que d=2 es lo que la
                    literatura excluye, no en transferir a 3+1D (ver §4)
NOT_AUTORIZADO: todo lo listado en §5
CAJAS_DE_TIEMPO: sin cambio (R2 -> 2026-08-14, conjunto -> 2026-09-11)
```
