# Nota de alcance firmada — EF-4, búsqueda de escalera parcial realizable

> **CORRECCIÓN DE DOMINIO POSTERIOR A LA EJECUCIÓN — 2026-08-16.**
> La notación `F_n` usada para el barrido finito se corrige en §12 a
> `F^{test}_{n,\rho}`. El perímetro y la salida originales se conservan sin reescritura
> como registro del precompromiso; §12 prevalece para toda interpretación científica.


```text
ESTADO: AUTHORISED / EXECUTED / OPEN_AT_COMPUTE_CAP
FECHA: 2026-08-16
NO_SUSTITUYE: docs/program_closure_note_2026-07-30.md
NO_SUSTITUYE: docs/program_reopening_note_2026-07-31.md
NO_REABRE: EF-0--EF-8 salvo el falsificador finito acotado por esta nota
EF4/C1: OUT_OF_SCOPE / INCONCLUSIVE
AUTORIZACIÓN_DE_EJECUCIÓN: CONSUMIDA — ejecución registrada en §11
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

## 11. Registro de ejecución — 2026-08-16

La ejecución autorizada terminó exactamente en el terminal precomprometido:

```text
TERMINAL: OPEN_AT_COMPUTE_CAP
POSITIVE_CONTROL: PASS
CONTROL_REGRESSION_24_2: PASS
CUMULATIVE_COMPATIBLE_BITING_CHAINS: 1000000
COMPATIBLE_FAILURES_OBSERVED: 0
PARTIAL_STAIRCASE_CASES_OBSERVED: 0
LAST_PAIR: (56,3)
LAST_PAIR_EXHAUSTED: NO
C1_AFTER_EXECUTION: INCONCLUSIVE
```

El control realizable reprodujo exactamente `40/40/0/0`. El control positivo reconoció una
intersección estricta no vacía de una escalera sintética de dos puntos y rechazó los casos vacío y
total. Ambos controles pasaron antes de la búsqueda científica.

Pares agotados, en orden, y número de cadenas compatibles que muerden:

```text
(34,3) 40
(36,3) 48
(38,3) 658
(40,3) 1358
(42,3) 5008
(44,3) 10394
(44,4) 40
(46,3) 20730
(46,4) 56
(48,3) 49189
(48,4) 666
(50,3) 81509
(50,4) 1366
(52,3) 176161
(52,4) 5184
(54,3) 261983
(54,4) 10570
```

En todos esos pares: `PARTIAL_STAIRCASE_CASES=0` y `COMPATIBLE_FAILURES=0`, y todas las cadenas
que requirieron los otros disyuntos fueron cubiertas por `fixed_inner` o `loss_case`.

En `(56,3)` se procesaron `375040` cadenas compatibles que muerden, con
`PARTIAL_STAIRCASE_CASES=0` y `COMPATIBLE_FAILURES=0`, antes de alcanzar exactamente el cap
acumulado de `1000000`. El par **no fue agotado**. Por ello no se inspeccionó `(56,4)` y no se
continúa a ningún parámetro posterior.

Esto no demuestra C1, no descarta que exista una contención parcial o un contraejemplo después del
punto de corte y no aporta un resultado sobre recuperabilidad normalizada. El único terminal
válido es `OPEN_AT_COMPUTE_CAP`; C1 permanece `INCONCLUSIVE`.

Artefactos y sellos de reproducción:

```text
SIGNED_SCOPE_COMMIT: 1f449a4bd94735bfc0a85c3bfed2acafd1a0caae
SCRIPT_COMMIT: 83ea6664ecbe60706233ed512538ee8e6c7d3c38
RESULT_COMMIT: e75e763c8fd27813f6eed94cdbe2ff24bab5d952
SCRIPT_SHA256: 5d2e1764aedce2b5967982846180c725edac77b93598387538120591055eb4ff
RESULT_SHA256: 212f9093225b62784ce27cb0d4ac3955d2f20d4b0c1db1d9d77980fd1d801d34
REPEAT_EXECUTION_BYTE_IDENTICAL: YES
SEEDS: NONE
```

## 12. Corrección de dominio tras la auditoría estática — 2026-08-16

~~~text
POST_EXECUTION_DOMAIN_CORRECTION: YES
STATIC_ENUMERATOR_COVERAGE: PROVED_FOR_CODE_DEFINED_TEST_FAMILY
FORMAL_EF4_TARGET: NOT_TESTED
RUN_TERMINAL: OPEN_AT_COMPUTE_CAP — INTACTO
C1_FORMAL: INCONCLUSIVE — INTACTO
~~~

Esta corrección no modifica el código, la salida, el cap ni el terminal de §11. Corrige
exclusivamente el objeto matemático sobre el que puede interpretarse el barrido.

### 12.1 Familia finita realmente enumerada

El evento formal `F_n` de EF-4.1--EF-4.2 no tiene dos parámetros: fija

\[
\rho_n=\left\lceil(n^2\log n)^{1/3}\right\rceil
\]

como función de `n`. El barrido de §3 usa, en cambio, `rho in {3,4}` para
`34 <= n <= 56`; esas parejas no satisfacen `rho=\rho_n`. Por tanto, no pertenecen
literalmente a la sucesión formal `F_n`.

Para identificar sin ambigüedad el dominio que sí recorre el código, defínase
`F^{test}_{n,\rho}`, para `n=2s` y los pares autorizados en §3, como el evento que
prescribe

\[
\begin{aligned}
&\pi(1)=1,\quad \pi(s)=s,\quad \pi(s+1)=s+1,\quad \pi(n)=n,\\
&\pi(s-\rho+j)=\lfloor n/4\rfloor+j,
&&j=1,\ldots,\rho-1,\\
&\pi(s+1+j)=\lfloor 3n/4\rfloor+j,
&&j=1,\ldots,\rho-1.
\end{aligned}
\]

Ésta es la plantilla combinatoria de EF-4.2 con `rho` libre, no la sucesión
asintótica `F_n`. Las expresiones «compatible con `F_n`» de §§2--4 y §11 deben
leerse, para este falsificador finito, como «compatible con
`F^{test}_{n,\rho}`». No se afirma una reducción por simetría ni una equivalencia
con el régimen `rho=\rho_n`.

La auditoría estática establece que el enumerador cubre todas las 4-cadenas estrictas
realizables bajo `F^{test}_{n,\rho}` que satisfacen `small_product=False`, hasta el
cap y con la marca de agotamiento por par registrada en §11. Ese resultado de
cobertura no transfiere por sí solo nada a la sucesión formal `F_n`.

### 12.2 Semántica corregida de los terminales

`REFUTED_BY_COMPATIBLE_WITNESS`, si hubiera aparecido, habría refutado únicamente la
extensión de la tricotomía a la pareja finita
`F^{test}_{n,\rho}` correspondiente. No habría refutado automáticamente C1 para el
`F_n` formal. Para esa transferencia haría falta, por separado:

1. un lema que lleve un testigo de `F^{test}_{n,\rho}` al régimen
   `rho=\rho_n`; o
2. ejecutar un par que satisfaga realmente `rho=\rho_n`.

Ninguna de esas dos piezas está en esta nota. En consecuencia, la frase de §8
«C1 queda refutada en ese punto finito» queda corregida por esta sección a:

~~~text
TEST_FAMILY_TRICHOTOMY_REFUTED_AT_FINITE_PAIR
FORMAL_C1_REMAINS_INCONCLUSIVE
~~~

El terminal observado fue `OPEN_AT_COMPUTE_CAP`, no una refutación. Permanece
válido exactamente como se registró: el millón de cadenas no produjo veredicto
científico ni sobre la familia de prueba más allá del prefijo recorrido ni sobre
el `F_n` formal.

### 12.3 Firma de la corrección

~~~text
AUTHORISED_BY_PI: Ignacio
DATE: 2026-08-16
AUTHORISED_SCOPE: corregir en este único fichero el dominio del falsificador y limitar
  la semántica del terminal de refutación
NOT_AUTHORISED: modificar código o resultados; reejecutar; instrumentar histogramas;
  tocar otros ficheros; promover o degradar tokens científicos
ORIGINAL_PRECOMMIT_AND_EXECUTION_RECORD: PRESERVED
~~~
