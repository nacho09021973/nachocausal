# Corrección de la adjudicación de C-1 — el contraejemplo de `n=24` no es realizable

```text
ESTADO: C1_ADJUDICATION_PARTIALLY_RETRACTED
FECHA: 2026-08-16
CORRIGE: docs/c1_adjudication_2026-08-16_ef4_token_degradation.md (mismo día)
CORRIGE: dev/EF4_TRICHOTOMY_N24_RESULT.md — veredicto REFUTED
EVIDENCIA: dev/ef4_trichotomy_prescription_compatibility_n24.py
SELLO: intacto; SEMILLAS: ninguna
```

## 1. Qué estaba mal

`FORO001-F1` barrió el dominio **abstracto** que enumera
`tests/test_p1a_entropia_fibras_ef4.py:63-154`: toda 4-combinación de filas cruzada con toda
4-combinación de columnas, sin ninguna atadura entre ambas. Encontró 560 tuplas que falsifican los
tres disyuntos, y de ahí se emitió `TRICHOTOMY_REFUTED_AT_N24`.

Ese dominio es **más grande** que el conjunto de configuraciones que el certificado tiene que
cubrir. Una cuádrupla corresponde a cuatro puntos `(r_i, c_i)` de una permutación de `F_n`, así
que una cuádrupla *realizable* debe respetar la prescripción: una fila prescrita sólo puede ir con
su columna prescrita, y viceversa.

El testigo que se publicó ayer, `rows = (1,11,12,23)`, `columns = (1,11,12,23)`, empareja la fila
`11` con la columna `11` cuando `F_n` prescribe `11 -> 7`. **No es una permutación de `F_n`.**
No refuta nada sobre la familia.

## 2. El chequeo

Toda cuádrupla compatible con `F_n` es también una cuádrupla abstracta, así que los contraejemplos
realizables son exactamente los miembros compatibles de los conjuntos ya calculados. No hace falta
un segundo barrido.

```text
[FP] threshold                = 17/72 = 0.236111
[FP] threshold * free_count^2 = 153/2
[FP] exact ties possible      = False
[FP] no comparison can tie, so the float sweep is exact at n=24

[F_n] prescription = [(1, 1), (11, 7), (12, 12), (13, 13), (14, 19), (24, 24)]
[F_n] realizable 4-chains  = 11639124
[F_n] abstract quadruples  = 112911876

[n=24] abstract biting     = 1504
[n=24] abstract failures   = 560
REQUIRES_LOSS_CASE=40
LOSS_CASE_PASS=40
COMPATIBLE_FAILURES=0

[witness] rows    = (1, 11, 12, 23)
[witness] columns = (1, 11, 12, 23)
[witness] INCOMPATIBLE: row 11 is prescribed to column 7, not 11

VERDICT: NO_COMPATIBLE_COUNTEREXAMPLE_AT_N24_RHO2
```

De las 1.504 tuplas donde `small_product` no basta, sólo **40** son realizables, y **las 40** caen
en `loss_case`. Cero contraejemplos compatibles.

Sobre coma flotante: en `n=24` los productos son `k/324` con `k` entero y el umbral escalado es
`153/2 = 76.5`, que no es entero, luego **ningún empate exacto es posible** y el barrido en coma
flotante es exacto aquí. (En `n=30` el umbral escalado sí es entero — `120` — y ahí la aritmética
racional es obligatoria.)

## 3. Tokens corregidos

```text
GEOMETRIC_TRICHOTOMY_EF4_3_ABSTRACT_DOMAIN = REFUTED_AT_N24
GEOMETRIC_TRICHOTOMY_EF4_3_ON_F_N = NOT_REFUTED_AT_N24 / INCONCLUSIVE
EF4_CORRECTED_PRESCRIBED_FAMILY = SKETCH_PENDING_INDEPENDENT_AUDIT_COMITE_050
EF4_Q2_ASYMPTOTIC = PROVED_DEDUCTIVE_NO_EXECUTABLE_BACKING
MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO_TWO_BREAKS_CONFIRMED_BY_COMITE_050
```

Qué cambia respecto de la nota de ayer y qué no:

- **`GEOMETRIC_TRICHOTOMY_EF4_3 = REFUTED_AT_N24` se retira** y se parte en dos, porque las dos
  cosas son verdad y se estaban confundiendo: la tricotomía **sí** es falsa como enunciado sobre
  cuádruplas arbitrarias, y **no** está refutada sobre `F_n`, que es lo que importa.
- **`EF4_CORRECTED_PRESCRIBED_FAMILY` sigue sin poder llevar `PROVED`.** El motivo sustantivo se
  cae entero; el **procedimental no se toca**: la orden del comité 050 (`:485,496-497`) sigue
  vigente y ningún comité posterior la levanta. Sigue en `SKETCH`, ahora por la razón correcta.
- **`EF4_Q2_ASYMPTOTIC` pierde el sufijo `CONDITIONAL_ON_REFUTED_TRICHOTOMY`**, que ya no
  describe nada. Conserva `PROVED_DEDUCTIVE_NO_EXECUTABLE_BACKING`, que es el hallazgo C9 del foro
  y no depende de esto.
- **`MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED` no cambia.**
- **`EF4_UNIQUE_SELECTION_ENTROPY`, `EF4_TERMINAL` y `Gate EF-4: PASS`**: la marca de "afectados"
  se retira. Su justificación era la refutación, que ya no existe.

Ningún token sube de nivel: `SKETCH` sigue siendo `SKETCH`. Lo que se retira es un calificativo
falso, no un requisito de auditoría.

## 4. El estado real de C1

`C1` (¿es la tricotomía una partición exhaustiva de los casos realizables?) vuelve a
**`INCONCLUSIVE`**, que es donde el foro-001 la dejó. Pero con más evidencia que antes: en `n=24`
las 40 configuraciones realizables donde `small_product` no basta caen todas en `loss_case`. Eso
es evidencia positiva acotada a un tamaño, no una prueba.

## 5. Hallazgo colateral sobre el test sellado

`test_geometric_trichotomy_exhausts_all_abstract_n12_chains` no sólo es vacuo en `n=12`: su
dominio es el equivocado. En cualquier `n` donde dejara de ser vacuo, **fallaría** por
configuraciones irrealizables, sin que eso dijera nada sobre el certificado. El test no puede
certificar la tricotomía ni ampliándolo. Un test con capacidad de morder tendría que enumerar
cadenas compatibles con `F_n`, no cuádruplas abstractas. Queda registrado, no reparado: reparar un
test sellado no está autorizado.

## 6. Dónde estuvo el fallo de proceso

No en la ejecución, que fue correcta y con cross-check escalar. En el **predicado**: la nota de
alcance `docs/scope_note_2026-08-16_foro001_falsification_test.md` §5 precomprometió un criterio de
refutación sobre `C(24,4)^2` tuplas abstractas, heredado literalmente de
`foro_decision_001:581-587`. Precomprometerlo no lo hizo correcto. Un predicado precomprometido
sobre el dominio equivocado da un veredicto limpio, reproducible y falso.

El error se detectó por una comprobación independiente en `(n=30, rho=2)` que llegó a
`COMPATIBLE_FAILURES=0` por la misma vía, con el mismo diagnóstico: los fallos usan pares
prohibidos por la prescripción.

## 7. Pendiente

- Los números de `(n=30, rho=2)` (`751.034.025` abstractas, `6.003` fallos racionales,
  `43.858` comparaciones fronterizas, `126.461.791` cadenas compatibles,
  `REQUIRES_LOSS_CASE=1157`) están **`[UNVERIFIED]`** en el sentido del repositorio: no proceden de
  un script commiteado. Reproducirlos requiere ampliar `n` más allá de 24, que
  `docs/scope_note_2026-08-16_foro001_falsification_test.md` §4 prohíbe sin otra nota firmada.
- Queda abierto si el dominio realizable correcto son exactamente las cadenas de 4 puntos de una
  permutación de `F_n`, o si el enunciado real de EF-4.3 cuantifica sobre algo ligeramente más
  ancho. No se ha releído EF-4.3 completo en esta sesión.
