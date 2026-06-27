# PR-003 Leakage Gate — el contrato order-only de la construcción del horizonte

> **Documento de disciplina, REVISABLE — no congelado.** No es una pre-registración y no fija
> umbrales. Es el **checklist que gobierna todo observable nuevo de PR-003** (construcción de
> escalera, regla de dirección #2, regla de selección #3): ninguno se mide ni se congela hasta
> pasar este gate. Punto 1 de `docs/hoja_de_ruta_23_jun_2026.md`. Reglas fundacionales en
> `CLAUDE.md` y `docs/preregistration.md`.

## Por qué existe

El único valor de PR-003 sobre Eichhorn–Gamito–Stokes (arXiv:2605.06813 §V.B) es ser **ciego**:
ellos *sembraron y seleccionaron* la escalera del horizonte usando el embedding; lo nuestro debe
ser order-only. El modo de fallo dominante —y silencioso— es que la verdad oculta (embedding `r`)
entre a **sembrar** o **seleccionar**, no solo a **puntuar**. El día que pase, deja de ser
reconstrucción ciega y queda una prueba de principio asistida. Este gate hace que ese fallo sea
*imposible de colar* sin que una guarda ejecutable lo detecte.

## Lo que PR-003 hereda (no estrena disciplina — la extiende)

El instrumento sellado ya garantiza, de forma **ejecutable**, la separación observable/scoring:

| Mecanismo existente | Ubicación | Garantía |
|:---|:---|:---|
| Generación separada | `nachocausal/__init__.py:9`, `generator.py:1` | El generador produce `(poset, embedding)` por separado. |
| Estimador order-only | `nachocausal/estimator.py:1-12` | Ve solo la matriz booleana de pasado `C`; no importa nada de `nachocausal.scoring`; sin coordenadas en su ámbito. |
| **Guard-v** | `nachocausal/estimator.py:verify_order_only` | Permuta las etiquetas (conjuga `C`) y recomputa: **RAISES** si el observable cambia → prueba que depende solo del poset abstracto, no de etiquetas/coordenadas. |
| Scoring aislado | `nachocausal/scoring/scorer.py` (*"Never feeds back"*) | Revela `r` solo para **medir** dónde cayó el borde ciego; el umbral se calcula de `O` *antes* de invocar scoring. |
| Guardas ejecutables | `tests/test_leak.py` | (a) importar el estimator no arrastra `scoring`; (b) la fuente del estimator es coordinate-free (sin `embedding`/`Coordinates`/`[:, 1]`/`scoring`); (c) Guard-v puede fallar de verdad. |
| Ciego → revelar | `nachocausal/validate.py:79` | Fase ciega por semilla (solo poset) → *luego* se revela `r` para puntuar. |

## El gate — los 5 contratos

Todo observable nuevo de PR-003 pasa el gate **si y solo si** cumple, mecánicamente, los cinco:

1. **Entrada de puro orden.** Su única entrada es la matriz de pasado `C` y cantidades derivadas
   de ella (`L_fut`, anticadenas, futuros truncados…). Cero `embedding`, cero coordenadas, cero
   `r`.
   - *Cómo se hace fallable:* extender el test coordinate-free de `tests/test_leak.py`
     (`test_estimator_source_is_coordinate_free`) al módulo de construcción.

2. **Sin import de scoring.** El módulo de construcción no importa nada de `nachocausal.scoring`.
   - *Cómo se hace fallable:* extender `test_estimator_import_does_not_pull_in_scoring` al módulo
     nuevo.

3. **Invariancia bajo reetiquetado (Guard-v sobre la construcción).** El **conjunto de elementos
   construido** (escalera / banda) debe ser invariante bajo una permutación aleatoria de las
   etiquetas: misma selección (como conjunto identificado por el orden) al conjugar `C`; RAISES en
   caso contrario. *Es la condición crucial para #3:* una **regla fija de selección** elige la
   misma escalera con independencia del etiquetado.
   - *Cómo se hace fallable:* `nachocausal.selection_guard.verify_selection_order_only` conjuga
     `C`, ejecuta el selector y exige que la selección de etiquetas se conjugue exactamente.
     `tests/test_selection_guard.py` prueba tanto el PASS de un selector order-only como el FAIL
     de un selector dependiente de la etiqueta `0`.

4. **Sembrado order-only, ciego antes de revelar.** Toda la construcción —semilla = el **bracket
   order-only de v2** → dirección (#2) → selección (#3) → banda— ocurre en la fase ciega. `r` se
   revela *solo después*, únicamente para puntuar (`d_⊥`, persistencia, continuidad…). La semilla
   **nunca** es el embedding.
   - *Cómo se hace fallable:* la construcción se ejecuta dentro de la fase ciega de
     `validate.py` (status previo a `"scored"`); el scoring permanece aguas abajo.

5. **El score no realimenta.** Nada medido tras revelar `r` puede cambiar la construcción: nada de
   re-seleccionar la escalera para mejorar `d_⊥`, ni de ajustar la regla tras ver el resultado.
   Eso es la trampa de EGS y es tuning post-hoc (`NO_POST_HOC_TUNING`, `NO_GROUND_TRUTH_LEAKAGE`).
   - *Cómo se hace fallable:* la regla de dirección y la de selección quedan **congeladas** (punto
     2 de la hoja de ruta) antes de cualquier dato *committing*; el comité verifica que el orden
     fue medir → congelar → puntuar, nunca al revés.

## Qué cuenta como FAIL

- Sembrar o seleccionar la escalera con el embedding o cualquier coordenada (EGS §V.B).
- Cualquier coordenada o `r` en el ámbito del módulo de construcción.
- Re-seleccionar / reajustar la regla después de revelar `r`.
- Una selección que dependa del etiquetado (Guard-v de construcción que no es invariante).

## Cómo se vigila

- **`/comite`** antes de congelar #2/#3 (punto 2) y el plan (punto 4): el falsador y el
  *pre-registration warden* juzgan exactamente contra este gate.
- **`/auditor`** (`make audit`) antes de construir sobre cualquier número ya medido.
- Cada regla nueva declara, por escrito, sus entradas y la prueba de que el embedding solo puntúa.
