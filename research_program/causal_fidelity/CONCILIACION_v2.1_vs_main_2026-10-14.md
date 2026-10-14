# Conciliación: borrador v2.1 del contrato frente a la línea de `main` (PR #10)

Fecha: 2026-10-14. Autor: Claude Opus 5.5. Documento de trabajo, no resultado.
Rama: `research/causal-fidelity-bridge` @ `e5a5476`, que **no** contiene el PR #10 (`85e1705`).
Documentos de `main` @ `1dbae26` leídos enteros: `CAUSAL_DYNAMIC_IR_GATE.md`,
`DEFINITION_REPAIR_2026-10-02.md`, `IR_OPERATIONAL_DEFINITION_2026-10-02.md` (IROD),
`SLOW_PROTOCOL_RESPONSE_2026-10-02.md`, `GROWING_FAMILY_RESPONSE_2026-10-02.md`.
Sus pruebas no se han rehecho aquí; lo que se cita de ellas es lo que afirman.

## 1. Situación

El contrato histórico (v1, sha256 `ba99fcb5…`) es el mismo en `main` y en `a77d9d8`. `main`
lo deja intacto y trabaja por addenda. Sobre él hay ahora dos formalizaciones del mismo test
`T_IR^{D1} = T_IR^{D2} ⊊ T_caus`, hechas sin conocerse:

- **IROD (`main`, 2026-10-02)**: sucesión determinista de posets con marcas; reloj de una
  cobertura por actualización; `H_n` = cadena saturada más larga; bloques `b_n = ⌊√H_n⌋`;
  espacio `[0,1] ⊔ {⊥}`; `T_caus = K` = límite de Hausdorff de las longitudes normalizadas de
  caminos de cobertura; `T_IR^D = {límite de τ}` (un punto). Primer caso (cadena): `FAIL_STRICT_INCLUSION`.
- **v2.1 (esta rama, `e5a5476`)**: familias aleatorias, selector equivariante, movimientos
  admisibles `A`, comparación por realización en probabilidad, semirrectas, umbral uniforme en
  `Θ`, admisibilidad ADM1–ADM4, NT1–NT4.

Después de IROD, `main` amplió el blanco a la respuesta lineal lenta (operador `G`), con un par
de dinámicas de igual llegada y distinta respuesta (93/256 para todo n). Esa ampliación no
sustituye el test de llegada.

## 2. Qué aporta v2.1 que `main` no tiene

| Elemento de v2.1 | Estado en `main` | ¿Sobrevive? |
|---|---|---|
| NT2: test para todo θ de un intervalo Θ | IROD fija un θ; §9 reconoce que subir θ cambia el resultado | **sí** — cierra el PASS trivial «iguales hasta el umbral» (comprobado a mano, revisión 2026-10-14) |
| NT3: Q debe diferir a N finito, no sólo Δ | IROD §8: en la cadena τ₁=τ₂=n a todo n (el patrón trivial); falló por otra razón | **sí** |
| ADM4: cono no colapsado | IROD normaliza por `H_n` y toma `K` entero: no hay colapso análogo | **dudoso**: sólo hace falta si el cono es «primer tiempo admisible»; con `K` de IROD no aplica |
| Exclusión del PASS por cardinalidad (punto ⊊ conjunto) | IROD compara un punto con `K`; su «techo lógico» (§7) lo reconoce, no lo excluye | **sí, como objeción a IROD** — es la construcción 2.2 de la revisión AH del 2026-10-13 |
| Familias aleatorias, selector equivariante aleatorizado | `main` toma las marcas como parte de la entrada y dice que seleccionarlas no está resuelto | **sí, como extensión**, pero no es necesaria para el primer caso |
| Modo en probabilidad, comparación por realización | IROD: sucesión determinista, Hausdorff | **sólo si hay familias aleatorias** |
| `INADMISSIBLE` frente a `FAIL` | IROD: «no existencia demostrada de límite es FAIL» | **sí, como precisión** |

## 3. Qué tiene `main` que v2.1 no tiene o hace peor

- Gate G0–G4, en especial **G1** (test negativo que cambia el embedding oculto conservando la
  entrada) y **G2** (dinámica genuina). v2.1 no los menciona.
- **⊥ para ausencia de llegada**, aislado en el espacio ambiente. Es más limpio que el NT1 de v2.1.
- **Soporte tautológico** (DEFINITION_REPAIR §4): con dinámica positiva sobre coberturas, soporte
  dinámico = cinemático por construcción. v2.1 no usa el soporte, pero su `Δ` = probabilidad de
  alcance hereda la misma positividad.
- **G3**: distinguir resolución, volumen y límites conjuntos. v2.1 sólo tiene `N → ∞`.
- **Conflicto de definición:** v2.1 toma `T_caus = [τ_caus, ∞)`. Eso sólo es «tiempos
  admisibles» si `A` permite quedarse quieto. Con el reloj de coberturas de `main` (sin espera),
  los pasos admisibles son el conjunto discreto `L_n`, no una semirrecta. En v2.1 la pérdida
  estricta del control de contrato (paseo perezoso, `τ^IR = 1/p > 1`) viene **de la espera**:
  cualquier dinámica con probabilidad de quedarse es subluminal. Es una pérdida barata.

## 4. Lectura

- v2.1 no debe ser un tercer contrato paralelo. Lo que sobrevive son **cláusulas de no
  trivialidad** (NT2, NT3, objeción de cardinalidad, `INADMISSIBLE`) que valen igual contra IROD.
- La pérdida estricta de v2.1 descansa en la espera; la de IROD, en caminos de longitudes
  distintas. Cuál es el «cono» correcto es una decisión de alcance, no técnica.
- La decisión pendiente más grande no es ésta, sino la que `main` dejó abierta: seguir con el
  test de **llegada** (con su techo lógico) o con el de **respuesta lenta** (donde el par
  declarado ya da distinta respuesta). Esa decisión y la relevancia para 3+1D son del PI.

## 5. Propuesta

1. No revisar ni congelar v2.1.
2. Rama nueva desde `main`. Añadir un addendum `ARRIVAL_TEST_NONTRIVIALITY_<fecha>.md` con
   NT2, NT3, la objeción de cardinalidad a IROD y `INADMISSIBLE`, formulados sobre IROD; traer
   las revisiones `revisiones/2026-10-13-*` y `2026-10-14-*` como registro.
3. v2/v2.1 quedan en esta rama como registro (`505ac49`, `e5a5476`), sin fusionar.
