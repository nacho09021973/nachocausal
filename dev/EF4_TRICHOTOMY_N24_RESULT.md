# FORO001-F1 — resultado en `n=24`

> **RETRACTACIÓN PARCIAL — 2026-08-16, mismo día.** El veredicto
> `TRICHOTOMY_REFUTED_AT_N24` de este fichero **vale sólo para el dominio abstracto** y **no**
> para el certificado. Los 560 fallos emparejan filas y columnas prohibidas por la prescripción
> `F_n` — el testigo usa `(11,11)` cuando `F_n` fija `11 -> 7` — así que ninguno es una permutación
> de `F_n`. De las 40 configuraciones realizables donde `small_product` no basta, las 40 caen en
> `loss_case`: `COMPATIBLE_FAILURES=0`. Ver
> `docs/c1_correction_2026-08-16_realizability.md` y
> `dev/ef4_trichotomy_prescription_compatibility_n24.py`. **C1 sigue `INCONCLUSIVE`.**
>
> Todo lo que sigue es correcto **como enunciado sobre el dominio abstracto** y se conserva sin
> tocar: los conteos, los controles y el cross-check escalar no están en cuestión. Lo que estaba
> mal era el dominio sobre el que se cuantificaba.

```text
TEST: FORO001-F1 (foro_decision_001:581-587, allí `R-1`)
AUTORIZACION: docs/scope_note_2026-08-16_foro001_falsification_test.md §3
FECHA: 2026-08-16
VERDICT: TRICHOTOMY_REFUTED_AT_N24
SEMILLAS: ninguna (determinista, sin semillas)
SELLO: intacto — no se toca
TEST_SELLADO_MODIFICADO: NO (tests/test_p1a_entropia_fibras_ef4.py sin tocar)
```

## 1. Qué se ejecutó

- `dev/ef4_trichotomy_exhaustiveness_n24.py` — enumeración exhaustiva vectorizada de las
  `C(24,4)^2 = 112.911.876` tuplas, replicando literalmente los predicados de
  `tests/test_p1a_entropia_fibras_ef4.py:63-154`.
- `dev/ef4_trichotomy_witness_check_n24.py` — cross-check escalar independiente (sin numpy,
  transcripción literal del cuerpo del test sellado).

Entorno: `.venv/bin/python` — Python 3.12.3, numpy 1.26.4.

## 2. Resultado

**560 tuplas de las 112.911.876 falsifican los tres disyuntos a la vez** (`fixed_inner`,
`small_product`, `loss_case`). Por el predicado precomprometido en la nota de alcance §5, la
tricotomía queda **refutada en `n` finito** y `C1` pasa de `INCONCLUSIVE` a `REFUTED`.

Detalle estructural: sólo `1.504` tuplas son no vacuas (`small_product = False`), es decir, sólo
en ésas se evalúan de verdad los otros dos disyuntos. De esas 1.504, **560 fallan** — o sea, más
de un tercio de la región donde el test por fin muerde. Los fallos se concentran en 24 cuádruplas
de fila y 24 de columna distintas.

Testigo mínimo (primero en orden lexicográfico): `rows = (1, 11, 12, 23)`,
`columns = (1, 11, 12, 23)`. Es decir, caja pasada `[1,11]×[1,11]` y caja futura `[12,23]×[12,23]`:
ambas contienen exactamente 9 filas libres y 9 columnas libres, luego
`past_free_product = future_free_product = 81/324 = 0.25 > 0.236111 = threshold`
(`small_product` falso); `past_upper = (11,11) ≠ (12,12)` (`fixed_inner` falso); y el punto de
escalera baja `(11,7)` cae dentro de la caja pasada mientras el de escalera alta `(14,19)` cae
dentro de la futura, luego `past_loses = future_loses = False` y `loss_case` es falso.

## 3. Controles

- **Control `n=12`**: la enumeración vectorizada reproduce exactamente el comportamiento del test
  sellado — `0` fallos y `245025/245025` tuplas con `small_product = True`, que es el diagnóstico
  de vacuidad que el falsificador del foro-001 reportó (`foro_decision_001:295-297`).
- **Equivalencia de implementaciones**: barrido escalar completo en `n=12` (245.025 tuplas), los
  cinco contadores coinciden con la versión vectorizada.
- **Sin falsos positivos**: las 560 tuplas reportadas como fallo se re-evalúan una a una con la
  transcripción escalar literal; las 560 confirman los tres disyuntos falsos.
- **Sin errores de clasificación en la región que decide**: las 1.504 tuplas no vacuas se
  re-evalúan escalarmente; `small_product = False` en todas y el recuento de fallos coincide
  (560). Fuera de esa región `small_product` es verdadero y la tupla pasa trivialmente, así que
  los controles cubren todo el soporte del veredicto.

## 4. Qué NO establece este resultado

- No toca el sello, ni `prereg-001/002/003`, ni el suelo de localización del manuscrito de
  límites (`R1`). EF-4 es la línea de entropía de fibras, que está en
  `docs/backlog_hallazgos.md` como hallazgo fuera de perímetro.
- Este fichero no degrada ni promueve ningún token: sólo registra el hecho. La adjudicación de
  `C-1` (degradación de `EF4_CORRECTED_PRESCRIBED_FAMILY` / `EF4_Q2_ASYMPTOTIC`) se firmó
  después, el mismo día, en `docs/c1_adjudication_2026-08-16_ef4_token_degradation.md`.
- No dice qué parte de EF-4 sobrevive. El fallo es de la **tricotomía como partición exhaustiva
  de casos**; delimitar el alcance restante es trabajo pendiente y necesita autorización.

## 5. Salida verbatim

`.venv/bin/python dev/ef4_trichotomy_exhaustiveness_n24.py`:

```text
[CONTROL n=12] n=12 rho=2
[CONTROL n=12] prescribed        = [(1, 1), (5, 4), (6, 6), (7, 7), (8, 10), (12, 12)]
[CONTROL n=12] free_count        = 6
[CONTROL n=12] threshold         = 0.458333
[CONTROL n=12] lower_stair       = [(5, 4)]
[CONTROL n=12] upper_stair       = [(8, 10)]
[CONTROL n=12] tuples            = 245025
[CONTROL n=12] max_min_ratio     = 0.250000
[CONTROL n=12] small_product=False (non-vacuous tuples) = 0
[CONTROL n=12] loss_case=True    = 216386
[CONTROL n=12] fixed_inner=True  = 625
[CONTROL n=12] FAILURES (all three disjuncts false) = 0
[CONTROL n=12] distinct failing row-quadruples    = 0
[CONTROL n=12] distinct failing column-quadruples = 0
[CONTROL n=12] failing row-quadruples  = []
[CONTROL n=12] first_witness     = None
[CONTROL n=12] elapsed_s = 0.0

[FORO001-F1 n=24] n=24 rho=2
[FORO001-F1 n=24] prescribed        = [(1, 1), (11, 7), (12, 12), (13, 13), (14, 19), (24, 24)]
[FORO001-F1 n=24] free_count        = 18
[FORO001-F1 n=24] threshold         = 0.236111
[FORO001-F1 n=24] lower_stair       = [(11, 7)]
[FORO001-F1 n=24] upper_stair       = [(14, 19)]
[FORO001-F1 n=24] tuples            = 112911876
[FORO001-F1 n=24] max_min_ratio     = 0.250000
[FORO001-F1 n=24] small_product=False (non-vacuous tuples) = 1504
[FORO001-F1 n=24] loss_case=True    = 108617870
[FORO001-F1 n=24] fixed_inner=True  = 14641
[FORO001-F1 n=24] FAILURES (all three disjuncts false) = 560
[FORO001-F1 n=24] distinct failing row-quadruples    = 24
[FORO001-F1 n=24] distinct failing column-quadruples = 24
[FORO001-F1 n=24] failing row-quadruples  = [(1, 11, 12, 23), (1, 11, 12, 24), (1, 11, 13, 23), (1, 11, 13, 24), (1, 11, 14, 23), (1, 11, 14, 24), (1, 12, 13, 23), (1, 12, 13, 24), (1, 12, 14, 23), (1, 12, 14, 24), (1, 13, 14, 23), (1, 13, 14, 24), (2, 11, 12, 23), (2, 11, 12, 24), (2, 11, 13, 23), (2, 11, 13, 24), (2, 11, 14, 23), (2, 11, 14, 24), (2, 12, 13, 23), (2, 12, 13, 24), (2, 12, 14, 23), (2, 12, 14, 24), (2, 13, 14, 23), (2, 13, 14, 24)]
[FORO001-F1 n=24] first_witness     = ((1, 11, 12, 23), (1, 11, 12, 23))
[FORO001-F1 n=24] elapsed_s = 2.0
[FORO001-F1 n=24] wrote EF4_TRICHOTOMY_N24_RESULT.json

VERDICT: TRICHOTOMY_REFUTED_AT_N24
```

`.venv/bin/python dev/ef4_trichotomy_witness_check_n24.py`:

```text
[A scalar n=12] total             = 245025 | vec: 245025
[A scalar n=12] failures          = 0 | vec: 0
[A scalar n=12] small_product=False = 0 | vec: 0
[A scalar n=12] fixed_inner=True   = 625 | vec: 625
[A scalar n=12] loss_case=True     = 216386 | vec: 216386
[A scalar n=12] max_min_ratio      = 0.250000 | vec: 0.250000
[A scalar n=12] IMPLEMENTATIONS_AGREE

[B scalar n=24] re-checking 560 reported failures
[B scalar n=24] ALL_REPORTED_FAILURES_CONFIRMED
[C scalar n=24] re-checking 1504 biting tuples
[C scalar n=24] scalar failures within biting set = 560
[C scalar n=24] CLASSIFICATION_AGREES

[WITNESS] rows    = [1, 11, 12, 23]
[WITNESS] columns = [1, 11, 12, 23]
[WITNESS] past_free_product    = 0.25
[WITNESS] future_free_product  = 0.25
[WITNESS] past_prescribed      = 2
[WITNESS] future_prescribed    = 3
[WITNESS] past_crosses         = False
[WITNESS] future_crosses       = False
[WITNESS] past_loses           = False
[WITNESS] future_loses         = False
[WITNESS] fixed_inner          = False
[WITNESS] small_product        = False
[WITNESS] loss_case            = False
[WITNESS] threshold            = 0.236111

CROSS_CHECK: PASS — the REFUTED verdict does not rest on the vectorisation
```

Las 560 tuplas completas están en `dev/EF4_TRICHOTOMY_N24_RESULT.json` (`failing_tuples`), junto
con las 1.504 no vacuas (`biting_tuples`).
