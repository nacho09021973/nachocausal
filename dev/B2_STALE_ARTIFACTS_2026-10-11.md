# B2 — siete artefactos de verificación quedaron obsoletos al corregir el kernel

**Fecha:** 2026-10-11
**Autorizado por:** el PI (control de consistencia de §4 de `dev/B2_STEP1_PAPER_ANALYSIS_2026-10-11.md`)
**Ejecutado:** solo lectura y evaluación de funciones existentes. **Ningún artefacto sobrescrito,
ningún sprinkling, sello intacto.**

```text
ANOMALIA = RESUELTA
CAUSA    = ARTEFACTO_OBSOLETO_POR_DEPENDENCIA_NO_REGENERADA
TERMINAL_B2.1 = SOBREVIVE  (la conclusion era correcta; los numeros no)
FACTORES = PEORES DE LO REPORTADO  -> §3
```

---

## 1. La causa

El 2026-09-13, el commit `6f866a2` corrigió el kernel angular:

```diff
- return np.exp(-0.5 * s) / np.sqrt(s)
+ return 2.0 * np.exp(-0.5 * s) / s ** 1.5
```

Ese commit **regeneró** los artefactos de B1 y dos de B2. **No regeneró otros siete**, que
importan ese mismo kernel directa o transitivamente:

| artefacto | generado | cadena hasta el kernel |
|---|---|---|
| `verification_b2_1_local_injectivity.json` | 09-12 | directa (`G, q`) |
| `verification_b2_2_shape_derivative.json` | 09-12 | directa (`G, q`) |
| `verification_b2_frozen_physical_path.json` | 09-12 | directa (`rho_bounds`) |
| `verification_b3_transverse_n2.json` | 09-12 | via `verify_b2_2_shape_derivative` |
| `verification_b4_execution.json` | 09-12 | via `verify_b2_2_shape_derivative` |
| `verification_b4_1_rank_certification.json` | 09-12 | via `verify_b4_execution` |
| `verification_b4_2_perturbation_certificate.json` | 09-12 | via `verify_b4_execution` |

> **Corregido el mismo dia.** Esta nota decia «cuatro». Son **siete**, y alcanzan B2, B3 y B4.
> Mi barrido manual filtraba por menciones literales del modulo y se perdia las cadenas
> transitivas de dos saltos. Lo encontro `scripts/check_stale_artifacts.py`, que resuelve el
> grafo de imports completo — es decir, lo encontro la herramienta, no yo releyendo.

El script de B2.1 **no cambió nunca**: cambió su dependencia. Por eso el desajuste es silencioso —
no hay diff que lo delate en el fichero que genera el número.

## 2. Comprobación

Evaluando las funciones actuales, sin reescribir nada:

```text
t      JSON lo    JSON hi      ACTUAL lo  ACTUAL hi   factor
0.45  0.005168   0.006976       0.019051   0.032878     4.71x
0.475 0.005272   0.007133       0.019425   0.033651     4.72x
0.50  0.005377   0.007292       0.019802   0.034428     4.72x
0.525 0.005482   0.007452       0.020182   0.035209     4.72x
0.55  0.005589   0.007614       0.020565   0.035993     4.73x
```

`verification_b2_2_shape_derivative.json` también discrepa (p.ej. `-0.0899` actual contra
`-0.0416` registrado). Los otros dos dependen del mismo kernel y preceden a la corrección; no los
he evaluado.

**Control que valida el código actual, no el artefacto:** la misma función `enclosure` de B2.1,
evaluada en los extremos del camino, reproduce las bandas de B1.4:

```text
t=0  ACTUAL [0.012781, 0.020032]   B1.4 [0.012756, 0.018794]
t=1  ACTUAL [0.028004, 0.050370]   B1.4 [0.027931, 0.043835]
```

Las cotas inferiores coinciden a cuatro o cinco cifras; las superiores actuales son algo más
anchas, coherente con una cota superior más burda. **El código está bien; lo obsoleto es el JSON.**

Esto disuelve además la sospecha de §4 del paso 1: `rho` **no** tiene un mínimo interior raro.
Era un artefacto viejo comparado contra bandas nuevas.

## 3. Corrección a lo que yo mismo reporté

Los factores de estrechamiento que di en `dev/B2_RECOST_PROPOSAL_2026-10-11.md` estaban
calculados sobre el JSON obsoleto. Los correctos son **peores**:

| objetivo | reportado | **real** |
|---|---:|---:|
| separar puntos adyacentes | 15.1x | **27.3x** |
| separar extremos `0.45`–`0.55` | 3.8x | **6.9x** |

La descomposición en dos objetivos sigue en pie y el barato sigue siendo ~4 veces más barato que
el caro. Pero **el «3.8x» no existe**: son 6.9x sobre los numeros oficiales regenerados.

## 4. Lo que NO cambia

El terminal `B2.1_INCONCLUSIVE_BY_BOUNDS` **se mantiene**: con los números corregidos las
envolventes siguen solapando entre puntos adyacentes. La conclusión de B2.1 era correcta; lo que
no lo era son las cifras que la acompañan en su `.md` y su `.json`.

Tampoco cambia el análisis del paso 1 (`rho'` es Leibniz puro, `G` nunca se deriva): ese resultado
es estructural y no depende de ningún número.

## 5. Lo que propongo, y no he hecho

Regenerar los cuatro artefactos ejecutando sus `main()` y actualizar la tabla de envolventes de
`B2_1_local_order_law_injectivity.md`. **No lo he hecho porque sobrescribe registros de
verificación**, y eso es decisión del PI, no mía.

## 6. Control permanente — hecho

`scripts/check_stale_artifacts.py` (solo lectura: inspecciona git y el grafo de imports, no
ejecuta nada y no escribe nada). Resuelve la clausura transitiva de modulos locales de cada
`verify_*.py` y compara fechas de commit contra su `verification_*.json`. Sale con codigo 1 si
hay alguno obsoleto, de modo que puede cortar un CI.

Senala ademas un artefacto sin `verify_*.py` correspondiente, que no puede comprobar:
`research_program/radial_3p1/2026-09-07/verification_adjoint_matched_energy_degree_8.json`.
