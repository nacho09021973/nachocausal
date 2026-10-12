# B4: el script de ejecución no calcula los momentos de la ley `n=3`

**Fecha:** 2026-10-12 · **Encontrado:** en el control del paso 1 de la fase 0 de B4-R
(`research_program/puente_3p1/2026-10-12/B4R_n3_reopening_spec.md` §5), que manda parar y
explicar si los valores centrales difieren de la referencia regenerada por encima de la anchura
de las envolventes.

## Síntoma

`dev/explore_b4r_phase0.py`, con `M = 32`, da `rho ∈ [0.0162, 0.0250]`. Ese intervalo es
coherente con la compuerta (`B_hi/Z² ≈ 0.0217`) y con las bandas regeneradas de B2.1 en `t0`
(`[0.0195, 0.0347]`). En cambio, `verification_b4_execution.json` da `rho = 0.0523`, fuera de la
envolvente.

## Causa: tres defectos de `research_program/puente_3p1/2026-09-12/verify_b4_execution.py`

1. **`f` y `p` no son masas de futuro y de pasado.** `h_bounds` es simétrica: no se anula ni
   cuando `x ≺ y` ni cuando `y ≺ x` (`ok = f | b`). El script calcula
   `future = Σ_y w·h_hi(x,y)` y `past = Σ_y w·h_lo(x,y)` sobre **todos** los `y`. Por tanto
   `f` es una cota superior de la masa comparable total de `x`, y `p` una cota inferior de esa
   misma masa. Ninguna de las dos es `nu(J±(x) ∩ K)`. En consecuencia,
   `rho = E[f + p] ≈ rho_hi + rho_lo`, que es aproximadamente el doble de `rho`: de ahí sale el
   `0.0523`. Por lo mismo, `E[f²]`, `E[p²]` y `E[pf]` tampoco son los momentos de B4.0.
2. **La «cota inferior» de `h`** evalúa `q` en el punto medio del rectángulo, `q(um·vm)`, que no
   es una cota inferior de `q` sobre la curva.
3. **El jacobiano se calcula por diferencias finitas** (`h = 1e-3`), con una cuadratura de Gauss
   de 10 puntos sobre un integrando no suave. B4.3 lo prohíbe explícitamente
   (`no_finite_difference`).

## Consecuencia

Los números de `verification_b4_execution.json`, `verification_b4_1_rank_certification.json` y
`verification_b4_2_perturbation_certificate.json` **no corresponden a la ley `n=3`**: momentos,
`Dm`, menores y valores singulares `(147.9, 2.6, 0.038)`. Ningún terminal de B4 se apoyaba en
ellos, porque todos eran `INCONCLUSIVE`. Lo que sí se apoyaba en ellos era la expectativa
cuantitativa de B4-R §5, en concreto `σ_min ≈ 0.038` y la precisión relativa necesaria: esa
estimación queda **sin base**, y la sustituye la fase 0.

El objeto de B4 en B4.0 (`f = nu(J+(x) ∩ K)`, `p = nu(J-(x) ∩ K)`) y las fórmulas de B4.3 son
correctos. El error está solo en la implementación preliminar.

## Qué no se hace

No se corrige ni se regenera `verify_b4_execution.py`: es un artefacto histórico de una
ejecución preliminar. La fase 0 de B4-R lo sustituye como referencia, con objetos orientados
(`F` hacia el futuro y `P` hacia el pasado, por pares de celdas) y derivadas de forma directas.
Cuando se reabra B4.1 se anotará este hallazgo en B4, B4.1 y B4.2.
