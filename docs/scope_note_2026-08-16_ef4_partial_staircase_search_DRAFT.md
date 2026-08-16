# Nota de alcance firmada — EF-4, búsqueda de escalera parcial realizable

```text
ESTADO: AUTHORISED / BOUNDED_EF4_PARTIAL_STAIRCASE_FALSIFIER
FECHA: 2026-08-16
NO_SUSTITUYE: docs/program_closure_note_2026-07-30.md
NO_SUSTITUYE: docs/program_reopening_note_2026-07-31.md
NO_REABRE: EF-0--EF-8 salvo el falsificador finito acotado por esta nota
EF4/C1: OUT_OF_SCOPE / INCONCLUSIVE ANTES DE LA EJECUCIÓN
AUTORIZACIÓN_DE_EJECUCIÓN: SÍ — exclusivamente §§3–9 de esta nota
PI_SIGNATURE: Ignacio
```

## 1. Motivo y dependencia previa

R1 ha superado su completion test en la rama autorizada `reopen/r1-r2-limits-writeup`.
El estado remoto final de esa rama es `591cf536653d9502cb591f4e31d24200dbca1963`; el
manuscrito exacto compilado e inspeccionado fue
`265a9538d16171b0403fdd63a7e6f3a530d3878e`.

Esta nota implementa únicamente el siguiente gate documental de
`docs/hoja_de_ruta_agosto_2026.md`. La autorización del PI recibida el 2026-08-16 cruza ese gate
sólo para el falsificador finito descrito aquí.

La razón científica del test autorizado es estrecha: con `rho=2` cada escalera tiene un solo
punto y la contención parcial es estructuralmente imposible para todo `n`. Por tanto, aumentar
`n` manteniendo `rho=2` no puede ejercitar la rama delicada de EF-4.3. C1 parte de
`INCONCLUSIVE`.

## 2. Pregunta autorizada

Falsar, o dejar no refutada dentro de un primer par informativo finito, la tricotomía de EF-4.3
**sobre cadenas realizables bajo `F_n`** cuando existe al menos un caso compatible que muerde y
contiene una fracción estricta no vacía de una escalera.

Este test no intenta:

- demostrar recuperabilidad normalizada;
- decidir `liminf T_n > 0`;
- convertir `Q_{2,n} -> 0` en una afirmación de recuperabilidad;
- promover ningún token científico de EF-4;
- reabrir EF-0--EF-8 fuera de este falsificador finito.

## 3. Perímetro autorizado — lista cerrada

El perímetro es exclusivamente:

1. `rho in {3,4}`;
2. para cada `rho`, sólo `n` par con
   `n >= n_min(rho) = 10*rho + 4`;
3. recorrer pares en orden determinista por `n` creciente y, a igual `n`, `rho` creciente;
4. enumerar **directamente** 4-cadenas compatibles con `F_n`, no barrer `C(n,4)^2` y filtrar
   después;
5. dentro de las compatibles, evaluar sólo las que muerden para el predicado científico;
6. detener la búsqueda de parámetros al terminar el primer `(n,rho)` que contenga al menos una
   cadena compatible que muerda y presente contención parcial estricta de una escalera;
7. en ese primer par, completar todas las cadenas compatibles que muerden, salvo que aparezca un
   fallo compatible o se alcance el cap fijado en §6.

La aritmética de `small_product` debe ser entera y exacta:

\[
8\min(a_-b_-,a_+b_+) \le N(N+8\rho),
\qquad N=n-2\rho-2.
\]

La compatibilidad se impone antes del veredicto:

```text
r_i prescrita  => c_i = P(r_i)
c_i prescrita  => r_i = P^{-1}(c_i)
```

## 4. Controles obligatorios antes de interpretar resultados

### 4.1 Control de regresión realizable

El enumerador debe reproducir exactamente el control commiteado de `(24,2)`:

```text
REQUIRES_LOSS_CASE=40
LOSS_CASE_PASS=40
COMPATIBLE_FAILURES=0
PARTIAL_STAIRCASE_CASES=0
```

Si falla cualquiera de esos cuatro valores, terminal inmediato:

```text
CONTROL_REGRESSION_FAILED
```

sin interpretar ningún resultado de `rho>=3`.

### 4.2 Control positivo del camino de escalera parcial

Antes de la búsqueda científica, el código debe ejecutar un self-check determinista del predicado
`partial_staircase`: una configuración sintética mínima, usada **sólo como test de software**, debe
contener una intersección no vacía y propia con una escalera de al menos dos puntos y ser
reconocida como parcial. Debe incluir también los dos controles negativos: intersección vacía y
contención total.

Este control no cuenta como evidencia sobre `F_n`; únicamente certifica que el camino lógico que
queremos ejercitar no está muerto por un error de implementación.

Si falla, terminal inmediato:

```text
POSITIVE_CONTROL_FAILED
```

## 5. Artefactos autorizados

La firma autoriza únicamente:

- `dev/ef4_partial_staircase_search.py` — script determinista nuevo;
- `dev/ef4_partial_staircase_search_result.txt` — salida verbatim y resumen de contadores;
- actualización documental de esta nota tras la ejecución, sólo para registrar el terminal y los
  hashes/contadores resultantes.

No se modifica ningún test sellado ni ningún fichero de manuscrito.

## 6. Tope de cómputo firmado

```text
COMPUTE_CAP_COMPATIBLE_BITING_CHAINS = 1000000
CAP_SCOPE = acumulado en la ejecución autorizada
```

El cap es un límite de gobernanza, no un umbral científico. Alcanzarlo no produce evidencia
negativa ni positiva; produce únicamente:

```text
OPEN_AT_COMPUTE_CAP
```

El número queda congelado por esta firma y no se cambia durante la ejecución.

## 7. Contadores mínimos por par

La salida debe registrar, como mínimo:

```text
N
RHO
COMPATIBLE_CHAINS
COMPATIBLE_BITING_CHAINS
PARTIAL_STAIRCASE_CASES
REQUIRES_LOSS_CASE
LOSS_CASE_PASS
COMPATIBLE_FAILURES
CUMULATIVE_COMPATIBLE_BITING_CHAINS
```

Ante un fallo compatible debe conservarse el testigo completo suficiente para reconstruir filas,
columnas, prescripciones y valores de los tres disyuntos.

## 8. Terminales precomprometidos

Tras pasar ambos controles de §4, sólo se permiten estos terminales científicos/de ejecución:

```text
REFUTED_BY_COMPATIBLE_WITNESS
FIRST_PARTIAL_PAIR_EXHAUSTED_NO_FAILURE
OPEN_AT_COMPUTE_CAP
```

Y estos terminales de control, que bloquean toda interpretación científica:

```text
CONTROL_REGRESSION_FAILED
POSITIVE_CONTROL_FAILED
```

Lectura:

- `REFUTED_BY_COMPATIBLE_WITNESS`: existe una cadena realizable que falla los tres disyuntos;
  C1 queda refutada en ese punto finito, pero cualquier consecuencia posterior requiere
  adjudicación separada.
- `FIRST_PARTIAL_PAIR_EXHAUSTED_NO_FAILURE`: se ejercitó realmente la rama parcial y el primer par
  informativo fue exhaustado sin contraejemplo; C1 **sigue sin quedar demostrada**.
- `OPEN_AT_COMPUTE_CAP`: no hay veredicto científico.

## 9. Prohibiciones expresas

Aunque esta nota está firmada, quedan fuera salvo nueva nota:

- modificar `tests/test_p1a_entropia_fibras_ef4.py` o cualquier test sellado;
- usar semillas o aleatoriedad;
- ampliar `rho` fuera de `{3,4}`;
- ejecutar otros barridos EF;
- promover `EF4_CORRECTED_PRESCRIBED_FAMILY`, `EF4_Q2_ASYMPTOTIC`, C1 o cualquier otro token;
- modificar el manuscrito de límites;
- sacar PR #4 de draft por efecto de este test;
- interpretar el resultado como decisión de recuperabilidad normalizada.

## 10. Firma

```text
AUTHORISED_BY_PI: Ignacio
DATE: 2026-08-16
AUTHORISED_SCOPE: falsificador EF-4 de escalera parcial realizable definido en §§3–8; sólo artefactos de §5
COMPUTE_CAP_COMPATIBLE_BITING_CHAINS: 1000000
NOT_AUTHORISED: todo lo listado en §9; ninguna promoción científica automática
OVERRIDING_NOTES: levanta NO_EXECUTION_AUTHORISED de docs/hoja_de_ruta_agosto_2026.md únicamente para este falsificador
```
