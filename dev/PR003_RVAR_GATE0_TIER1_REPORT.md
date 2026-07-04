# Gate 0 Tier 1 — informe de resultado

Status: **dev, nota de resultado exploratorio, ejecutada bajo autorización acotada del PI
(2026-07-04, bloque "f4ljlu") con precondición verificada: R-VAR v2.2
(`dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md`) ya estaba commiteado en limpio (commit `6687357`)
antes de correr este Tier 1 — no hizo falta commit documental previo.**

Alcance autorizado (no excedido): Gate 0 Tier 1 únicamente. Sin S2-S5, sin cómputo de μ, sin
tablas de calibración, sin tocar `VALIDATION_SEEDS`, sin pistas de producción/parche-BH. Semillas
usadas exclusivamente de `EXPLORE_POOL` (`dev/explore_seeds.py`).

Spec controladora: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_2.md`, Parte D.2.1-D.2.3.

## Provenance

- Commit HEAD al ejecutar: `66873577f28b184059de63ff8d2cdd68c63e0202`
- `python3 --version`: Python 3.12.3, numpy 1.26.4 (venv sellado `.venv/`, usado por disponibilidad
  aunque el pin de numpy no es load-bearing aquí — esto es combinatoria de juguete a N≤14, no el
  path de validación sellado)
- `captured_utc`: 2026-07-04T20:51:41Z
- Comando: `.venv/bin/python dev/measure_pr003_rvar_gate0_tier1.py`
- Script: `dev/measure_pr003_rvar_gate0_tier1.py` (este commit)
- Output crudo: `dev/gate0_tier1_result.json` (este commit; incluye los 382 registros individuales)

## Comando y salida exacta

```text
$ .venv/bin/python dev/measure_pr003_rvar_gate0_tier1.py
Generated: 382 posets total (7 skipped N>14)
  EMPTY_FAMILY: 282   non-empty tested: 100
  degenerate raw ties (D=empty or D=C at unfiltered optimum): 83
  mismatches: 0
OVERALL Gate 0 Tier 1 STATUS: GATE0_TIER1_PASS
Full result written to /home/adnac/nachocausal/dev/gate0_tier1_result.json
```

## Semillas

- Pool: `EXPLORE_POOL` (`dev/explore_seeds.py`, `1000000..1000039`). Ninguna semilla de
  `VALIDATION_SEEDS` fue referenciada por el script (no se importa ese nombre).
- Receta: `numpy.random.SeedSequence(root).spawn(K)` por cada raíz de `EXPLORE_POOL`, consumida en
  orden, con `K ≤ MAX_CHILDREN_PER_ROOT = 400` como válvula de seguridad.
- En la práctica, alcanzar el objetivo (100 posets con `𝒜(C)` no vacío) solo requirió la
  **primera** raíz (`1000000`) y sus primeros 191 hijos — las 39 raíces restantes de
  `EXPLORE_POOL` no se tocaron.
- Intensidad de sprinkling: `TOY_INTENSITY = 9.0` (media de Poisson), elegida únicamente para que
  `N` caiga en `[0,14]` con probabilidad razonable — **no** es uno de los valores sellados de
  `thresholds.INTENSITIES` y no tiene significado estadístico/de calibración.
- Ambas cajas causales sobre el mismo embedding, como exige la autorización ("cajas MINK y BH
  ambas") y como está diseñado el generador sellado (`nachocausal/generator.py`: "the SAME
  embedding is used to build both the BH and MINK posets").

## Número de posets y rango de tamaño

- Total generado: 382 (191 embeddings × 2 cajas). 7 embeddings adicionales fueron descartados por
  `N > 14`.
- `EMPTY_FAMILY` (𝒜(C) = ∅, sin nada que comparar): 282 — desglosado por caja: MINK 190/191,
  BH 92/191. Esta asimetría es geométricamente esperable: la caja alta (T_EDGE=6.0 ≫ R_EDGE=1.2)
  hace que MINK a baja intensidad sea casi un orden total (una sola cadena), cuyo único elemento
  maximal colapsa la familia `𝒜(C)` a vacía casi siempre; BH cerca del horizonte produce
  estructura de Hasse más ancha con más frecuencia.
- **Probados con `𝒜(C) ≠ ∅` (el conjunto que realmente ejercita D.2.1/D.2.2): 100** — MINK 1,
  BH 99. Este es el número vinculante frente al objetivo "≥100 posets" de la autorización (ver
  nota de interpretación abajo).
- Rango de tamaño `N`: `[2, 14]` sobre los 382 generados.

**Nota de interpretación (declarada, no silenciosa):** "≥100 posets" se interpretó como ≥100
posets con `𝒜(C)` no vacío, porque solo esos pueden ejercitar (y por tanto falsar) la maquinaria
de D.2.1/D.2.2 — un poset `EMPTY_FAMILY` no da a ninguna de las dos implementaciones nada sobre lo
que discrepar. El total generado (incluyendo `EMPTY_FAMILY` y los descartados por `N>14`) se
reporta de todos modos para transparencia completa.

## Predicado de comparación

Por cada uno de los 100 posets con familia no vacía, exactamente el mismo predicado que Tier 0
verificó a mano una vez, ahora automatizado:

1. **Traza de Dinkelbach completa:** en cada paso, el argmax de fuerza bruta
   (`bf_argmax_at(p,q) := argmax_{D∈𝒜(C)} [qA(D)-pB(D)]`, escaneo directo) se compara contra el
   argmax obtenido vía la reducción de cierre de peso máximo / min-cut (`mincut_argmax_at`,
   Picard 1976, flujo máximo por Edmonds-Karp) filtrado por pertenencia a `𝒜(C)`. **Acuerdo exigido
   en TODOS los pasos, sin excepción.**
2. **Convergencia:** el `λ` final de la traza de Dinkelbach debe coincidir exactamente (como
   `Fraction`) con el óptimo global `λ* = A*/B*` computado independientemente por
   `brute_force_argmax` (enumeración directa de toda la familia).
3. **Óptimo filtrado vs. fuerza bruta (con empates):** el conjunto COMPLETO de down-sets empatados
   en el óptimo según el escaneo min-cut (`tied_in_fam`) debe coincidir, como conjunto, con el
   conjunto COMPLETO de down-sets empatados en el óptimo según fuerza bruta directa
   (`{D : Fraction(A(D),B(D)) = λ*}`) — no solo con un único representante.
4. **Empate degenerado (D.2.1, hallazgo normativo):** se registra si el óptimo SIN filtrar por
   `𝒜(C)` (el cierre de peso máximo crudo sobre TODOS los down-sets) cae en `D=∅` o `D=C`.

Aritmética exacta (`fractions.Fraction`) en todo momento — cero coma flotante en cualquier
comparación de razones, per F1.

`T(C)/E(C)/U(C)` se reportan vía la fórmula congelada de D.2.2 (`brute_force_TEU`), evaluada en el
`λ*` ya cruzado contra min-cut — exactamente la misma limitación de alcance que Tier 0 (que
tampoco re-derivó T/E/U vía una segunda instancia de min-cut forzado independiente). Esto se
declara explícitamente como limitación de alcance, no como brecha silenciosa: inventar una
construcción de min-cut-forzado nueva, no verificada aún por el comité 017, habría excedido la
autorización de este paso.

## Hallazgo intermedio (falso positivo del arnés de prueba, corregido antes del veredicto)

La primera ejecución del script arrojó **58/100 discrepancias** (`GATE0_TIER1_FAIL` preliminar).
Investigación manual de la primera discrepancia (`root=1000000, child=1, kind=BH, N=8`) mostró que
el óptimo verdadero (`λ*=3`) tiene **12 down-sets distintos empatados** en `𝒜(C)` (tamaño de
familia 14), y que el escaneo min-cut (`tied_in_fam`) **identificaba correctamente los 12**,
coincidiendo exactamente con el conjunto de empates de fuerza bruta. El check original comparaba
`set(tied_in_fam) == {Dstar_bf}`, donde `Dstar_bf` es un único representante arbitrario devuelto
por `max()` — una comparación demasiado estricta que declaraba "discrepancia" cada vez que existía
más de un down-set empatado en el óptimo (algo que la única instancia hecha a mano de Tier 0 no
tenía, así que el defecto del arnés nunca se manifestó hasta la automatización). Corregido
comparando contra el conjunto COMPLETO de empates de fuerza bruta (`full_tie_set_bf`, ítem 3 de la
sección anterior). Tras el fix, re-ejecución **determinista** (mismas semillas, mismos 382
registros) → **0/100 discrepancias**. Se documenta aquí en vez de omitirse, per la regla
fundacional del proyecto de que ningún guardrail que no pueda fallar es decoración: este SÍ falló,
y la causa raíz (arnés, no algoritmo) quedó verificada a mano antes de aceptar el fix.

## Empates degenerados (D.2.1, hallazgo normativo — confirmación cuantitativa)

`n_degenerate_raw_ties = 83` de 100 (83%): en la gran mayoría de los posets probados, el cierre de
peso máximo **sin filtrar por `𝒜(C)`** converge trivialmente a `D=∅` o `D=C` — no es un caso
aislado, es el caso típico. Esto es una consecuencia estructural universal, no un artefacto de
estos datos en particular: `H(∅)=H(C)=∅` siempre, y el down-set óptimo `D*` dentro de `𝒜(C)`
también alcanza puntaje crudo exactamente `0` en la fórmula `qA(D)-pB(D)` evaluada en
`(p,q)=(A*,B*)` — un empate a tres (o más) bandas es matemáticamente forzoso en cada poset, y cuál
de los empatados devuelve el recorrido BFS del flujo depende de detalles de implementación, no de
estructura causal. En los 100 casos, el filtro de pertenencia a `𝒜(C)` (aplicado ANTES del argmax,
como exige D.2.1) excluyó correctamente `∅` y `C` en el 100% de los casos, dejando el óptimo
filtrado consistente con fuerza bruta (ítem 3 arriba). Esto pasa de ser "una advertencia normativa
verificada en un ejemplo" a "un fenómeno mayoritario, cuantificado a escala" — refuerza que el
filtro no es limpieza cosmética sino una restricción dura de admisibilidad, tal como D.2.1 ya lo
declaraba.

## Veredicto

```text
OVERALL_STATUS = GATE0_TIER1_PASS
  total_posets_generated = 382
  n_nonempty_family_tested = 100  (>= objetivo de 100)
  n_mismatches = 0
  n_degenerate_raw_ties = 83  (filtrados correctamente en el 100% de los casos)
```

Regla de aceptación congelada (D.2.3): CERO discrepancias. Cumplida. **Tier 1 = PASS.**

Per la autorización: este resultado se detiene aquí. No autoriza μ, calibración, Tier 2+, ni
ningún paso S2-S5. Doblar este hallazgo en el texto de la spec (como se hizo con Tier 0 → v2.2)
requeriría una autorización explícita separada, igual que la vez anterior.
