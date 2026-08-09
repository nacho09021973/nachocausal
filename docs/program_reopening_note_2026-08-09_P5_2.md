# Nota de ampliación acotada del perímetro — P5.2

```text
ESTADO: FIRMADA — P5.2 AUTORIZADO (ver §6)
FECHA: 2026-08-09
AMPLIA: docs/program_reopening_note_2026-08-05_R3.md
NO_REVOCA: docs/program_closure_note_2026-07-30.md, que permanece íntegra
RAMA: research/f2-f3-chain-distance
SELLO: intacto — no se toca
SEMILLAS: ninguna; no se extraen ni se consumen
```

## 1. Por qué hace falta esta nota

La nota R3 autoriza una lista cerrada centrada en la dicotomía de cópula nula y el
puente E. El trabajo de
`research_program/work_packages/wp7_f2_f3_product_order_contract.md` no forma parte de
esa lista. P1--P4 y la estabilidad condicional P5.1 quedan registrados como trabajo ya
realizado, pero continuar hacia P5.2 exige una ampliación expresa del perímetro.

Esta nota no reabre reconstrucción ni localización de horizonte. Autoriza un único
problema teórico de límites de recuperabilidad.

## 2. Único trabajo autorizado

**P5.2 — Auditoría de la geometría planar de de Sitter en `d=2`.** Decidir si el
mecanismo de cadena plantada probado condicionalmente en P5.1 puede realizarse bajo los
cuantificadores geométricos de la Def. 2.6 de Madsen usando como candidato único

\[
M_\ell=\{(\eta,x):\eta<0\},\qquad
g=\frac{\ell^2}{\eta^2}(-d\eta^2+dx^2).
\]

La auditoría deberá resolver, sin dar ninguna pieza por automática:

1. hiperbolicidad global del parche y elección admisible del campo timelike auxiliar;
2. prueba de `0 < lambda < infinity` bajo la ecuación (1) de Madsen, declarando cualquier
   ambigüedad de norma que impida una lectura literal;
3. existencia de una región precompacta y de un diamante testigo profundo en el rango
   mesoscópico;
4. comparación uniforme entre volumen y tiempo propio, y cota uniforme para la longitud
   de la intersección de la geodésica plantada con todo diamante F2-admisible;
5. sustitución de esas constantes en P5.1 y comprobación de la desigualdad F3 completa.

**Superficie de escritura autorizada:** únicamente
`research_program/work_packages/wp7_f2_f3_product_order_contract.md`.

## 3. Método y límites

- Deducción y bibliografía primaria únicamente.
- Cero simulaciones, cero semillas y cero nuevos estimadores.
- Un solo fichero científico modificado durante P5.2.
- El manuscript `docs/manuscript_limits_draft.md` no se toca.
- No se abre otra geometría si de Sitter planar falla: el fallo se tipa antes de decidir
  cualquier ampliación posterior.
- No se trabaja en paralelo sobre `(E')`, Alloy, enumeraciones de posets, localizadores de
  horizonte, `order-number-scale-limits` ni dimensión superior.
- No se afirma prioridad o novedad sin una auditoría bibliográfica independiente posterior.

## 4. Terminales y criterio de parada

P5.2 termina en exactamente uno de estos estados:

```text
P5_2_PASS
  La geometría satisface todas las obligaciones de §2 y cierra P5 bajo el alcance
  regional exacto adoptado de Madsen.

P5_2_PASS_WITH_SCOPE
  El argumento matemático cierra, pero la formulación regional de Madsen no permite
  identificar literalmente todos los cuantificadores de la Def. 2.6.

P5_2_FAIL_TYPED
  Falla la primera obligación concreta de §2 que no pueda demostrarse.

P5_2_OPEN_AFTER_EXACT_AUDIT
  Una ambigüedad definicional o una obligación matemática queda aislada con enunciado
  preciso y sin promover P5 a probado.
```

Solo `P5_2_PASS` permite cambiar el terminal de WP7 a
`COUNTEREXAMPLE_F1_F2_NOT_F3_D2`. Ningún otro estado autoriza esa afirmación.

## 5. Qué queda aplazado

R3 y `(E')` no se cierran ni se revocan, pero quedan aparcados durante P5.2. La posible
integración de WP7 en el paper de límites, su conversión en nota independiente y toda
decisión de publicación se tomarán únicamente después del terminal de §4. Esta nota no
autoriza ninguna de esas acciones.

Las cajas de tiempo ya firmadas no se prorrogan por esta ampliación.

## 6. Firma

```text
FIRMADA_POR: Ignacio (PI)
FECHA: 2026-08-09
AUTORISED_SCOPE: P5.2 (lista cerrada de §2)
DECISION_P5_2: AUTORIZADO
SOLE_ACTIVE_EXECUTION: P5.2
R3_E_PRIMA: APARCADO, NO REVOCADO
MANUSCRIPT_LIMITS: NO TOCAR
SIMULACIONES: NO
SEMILLAS: NO
SELLO: INTACTO
PUBLICACION_O_INTEGRACION: NO AUTORIZADA EN ESTA NOTA
CAJAS_DE_TIEMPO: sin cambio
```
