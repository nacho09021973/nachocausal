# Gate 0 Tier 0 — informe de resultado

Status: **dev, nota de resultado exploratorio, escrita bajo autorización acotada del PI
(2026-07-04) del alcance S1-S5 de `docs/comite/comite_decision_017_r-var-v2-reconvene.md`,
recortado explícitamente por el PI a "Gate 0 Tier 0 únicamente — stop after Gate 0 Tier 0".**
Ningún otro paso de S1-S5 (Tier 1 automatizado a escala, calibración μ, tablas, parches BH) se
ha ejecutado. Ninguna semilla de `EXPLORE_POOL` ni de `VALIDATION_SEEDS` ha sido tocada — este
gate es combinatoria pura sobre posets construidos a mano, no sprinkling.

Spec controladora: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_1.md`, Parte C (testigo de separación) y
Parte D.2.3 (Gate 0, mandato de comité 017).

## Provenance

- Commit HEAD al ejecutar: `6591f5fbbcf875f8a2b1481cdf8a951c1308516b`
- `python3 --version`: Python 3.12.3 (sin dependencia de numpy — combinatoria discreta pura,
  no toca el path sellado ni requiere el `.venv` sellado)
- `captured_utc`: 2026-07-04T09:04:53Z
- Comando: `python3 dev/measure_pr003_rvar_gate0.py`
- Script: `dev/measure_pr003_rvar_gate0.py` (este commit)
- Output crudo: `dev/gate0_tier0_result.json` (este commit)

## Comando y salida exacta

```text
$ python3 dev/measure_pr003_rvar_gate0.py
Witness pair: PASS
16-element DP-vs-brute-force check: PASS
OVERALL Gate 0 Tier 0 STATUS: PASS
Full result written to /home/adnac/nachocausal/dev/gate0_tier0_result.json
```

## Obligación (i) — testigo de separación C.1 (par de posets Hasse-conexos)

**Input:** `P₁` = cadena `x⋖a⋖b` (3 elementos); `P₂` = cadena `x⋖a` (2 elementos). Ambos
individualmente conexos (a diferencia del testigo original de v2, que usaba un poset con
componente aislada — fix de comité 017).

**Output:**

| | `d⁺(x)` | `O(x)=\|↑x\|` | `\|𝒜(C)\|` |
|---|:--:|:--:|:--:|
| P₁ | 1 | 2 | 0 (EMPTY_FAMILY) |
| P₂ | 1 | 1 | 0 (EMPTY_FAMILY) |

**Status: PASS.** `d⁺(x)` coincide (1=1), `O(x)` difiere (2≠1), y ambos posets abstienen
idénticamente vía `EMPTY_FAMILY` — el output expuesto es genuinamente idéntico entre ambos
mientras `O(x)` difiere. Esto es un testigo más limpio de lo que el falsifier pidió: no solo
tienen vecindad de Hasse isomorfa a radio 1, sino que el output COMPLETO del selector coincide
(ambos abstienen igual), cerrando el objeto de prueba correcto (outputs expuestos, per la Parte
C fijada en v2.1) sin depender de un argumento de "vecindad isomorfa" más débil.

## Obligación (ii) — poset de 16 elementos, D.2.1/D.2.2 vs fuerza bruta

**Input:** poset de permutación (orden producto en coordenadas (u,v) tipo null-coordinate,
`dim_DM≤2`, coherente con la estructura 2D que la Parte E asume para la familia generadora),
`N=16`, permutación fijada a mano: `PI = [7,9,5,6,14,10,12,8,1,2,13,15,4,11,0,3]` (encontrada
escaneando permutaciones aleatorias con semilla fija — **no sprinkling, no seeds de
EXPLORE_POOL/VALIDATION_SEEDS**, es una búsqueda determinista de una estructura de poset con
`|𝒜(C)|` no trivial). `Min={0,2,8,14}`, `Max={11,13,15}`, `21` pares de cobertura,
`|𝒜(C)|=4` tras filtrar.

**Hallazgo intermedio (reportado, no oculto):** el sketch de un párrafo de D.2.1 ("DP local
sobre pasos de escalera") no fue directamente implementable como una DP escalar de estado local
— la contribución de una arista de cobertura depende de AMBOS extremos, y aunque toda arista de
cobertura va de menor a mayor posición-u (verificado), plegar esto en un barrido de estado
escalar exige más derivación de la que el sketch da. El algoritmo correcto para esta
optimización exacta es una reducción a **cierre de peso máximo / min-cut (Picard 1976)** —
técnica estándar, pero NO lo que el sketch describe literalmente. Implementado así en el script
(`maxflow_mincut_closure`), verificado contra fuerza bruta.

**Verificación del empate espurio en la frontera:** el cierre de peso máximo sin restringir
(sobre TODOS los down-sets) empata en el valor óptimo entre `D=∅`, `D=C`, y el verdadero óptimo
`D*` — porque `H(∅)=H(C)=∅` da `A=B=0` trivialmente. **Esto confirma que los filtros de
pertenencia a `𝒜(C)` (D≠∅, D≠C, condición-Min, H≠∅) no son decoración: son necesarios incluso
para que el propio algoritmo de optimización identifique el óptimo físicamente significativo.**
Una vez filtrado a `𝒜(C)`, el óptimo del min-cut coincide exactamente con el de fuerza bruta.

**Iteración Dinkelbach completa, paso a paso (no solo en el λ* ya conocido):**

| it | λ_k | D (fuerza bruta) | D (min-cut, filtrado) | coincide |
|--:|--:|---|---|:--:|
| 0 | 0 | {0,1,2,3,5,7,8,9,12,13} | {0,1,2,3,5,7,8,9,12,13} | ✅ |
| 1 | 5/3 | {0..11} | {0..11} | ✅ |
| 2 | 9/4 | {0..13} | {0..13} | ✅ |
| 3 | 3 | {0..13} | {0..13} | ✅ |

Converge a `λ*=3`, coincide con fuerza bruta en los 4 pasos.

**T/E/U resultantes (en `λ*`):** `T={14,15}`, `E={0,...,13}`, `U=∅` — argmax singleton,
confirma en la práctica lo que v2.1 ya admitía por escrito: `INCOHERENT_ARGMAX` no puede
dispararse aquí (T,E ambos no vacíos automáticamente).

**Status: PASS.** Cero discrepancias en los 4 pasos de Dinkelbach, en el óptimo final, y en la
partición T/E/U resultante.

## Veredicto

```text
OVERALL_STATUS = PASS
```

Regla de aceptación congelada (D.2.3): cero discrepancias en cualquiera de los dos niveles.
**Se cumple.** Nada bloquea, por ahora, un futuro paso de Tier 1 automatizado — pero ese paso
**no está autorizado por esta sesión** (el PI acotó explícitamente la autorización a Gate 0
Tier 0, "stop after Gate 0 Tier 0; do not proceed to μ calibration without explicit follow-up
authorization").

## Hallazgo que debe alimentar la próxima revisión de la spec (no aplicado aquí — fuera de alcance)

`dev/PR003_R_VAR_SELECTOR_SPEC_V2_1.md` Parte D.2.1 describe el algoritmo como una "DP local
sobre pasos de escalera" en un párrafo. Este gate confirma que la optimización SÍ es
polinómica y SÍ reproduce fuerza bruta — pero solo bajo la construcción de min-cut / cierre de
peso máximo derivada aquí, no bajo una lectura literal del sketch de un párrafo. Cualquier
implementación futura del tier de juguete completo (Tier 1, y cualquier ejecución sobre
EXPLORE) debe usar la construcción de min-cut (o una derivación igualmente rigurosa), no el
sketch original. Se recomienda que la próxima revisión de la spec (v2.2 o equivalente)
incorpore esta construcción explícitamente en D.2.1, con cita a este informe — pero esa edición
de la spec está fuera del alcance autorizado hoy (solo Gate 0 Tier 0 y su informe).

## Qué NO se ha hecho (explícito, por alcance)

- No se ha calculado la tabla μ (Parte F).
- No se ha sprinkleado ningún parche, MINK ni BH.
- No se ha tocado ninguna semilla de `EXPLORE_POOL` ni `VALIDATION_SEEDS`.
- No se ha ejecutado el Tier 1 automatizado a escala (≥100 posets, N≲14) — solo el Tier 0 a
  mano/hand-checkable (2 posets pequeños del testigo C.1 + 1 poset de 16 elementos).
- Ningún output de este gate se trata como corroboración de PR-003 o del PASS de prereg-002
  (cláusula `NON_CORROBORATION`, v2.1 Parte C.2).
