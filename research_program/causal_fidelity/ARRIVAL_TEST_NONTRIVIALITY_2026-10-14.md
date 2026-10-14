# Test de llegada: contenido de la inclusión estricta y cláusulas de no trivialidad

Fecha: 2026-10-14. Estado: `DRAFT / ADDENDUM / NOT_CANONICAL / NO_EXECUTION`.
Base: `main @ 1dbae26`. Addendum a `IR_OPERATIONAL_DEFINITION_2026-10-02.md` (IROD).
No modifica el contrato histórico ni IROD. Autor: Claude Opus 5.5; sin revisión independiente.
Derivaciones algebraicas, sin código ejecutado.

Procedencia: cláusulas extraídas del borrador v2.1 del contrato (rama
`research/causal-fidelity-bridge` @ `e5a5476`, no fusionado) y de las revisiones ciegas en
`revisiones/2026-10-13-*` y `revisiones/2026-10-14-argon-high-delta-v2/`. La conciliación con
IROD está en `CONCILIACION_v2.1_vs_main_2026-10-14.md`.

## 1. La inclusión estricta de IROD no depende de la dinámica

Notación de IROD §§2–6: `K_n`, `K` (límite de Hausdorff en `X=[0,1]⊔{⊥}`),
`J_D,n={g_n(τ_D,n)}` o `{⊥}`, `J_D` su límite, `PASS_FORMAL` si `J_D1=J_D2 ⊊ K`.

**Lema 1.** Supóngase que existen `K`, `J_D1`, `J_D2`. Entonces

`PASS_FORMAL  ⟺  J_D1 = J_D2 = {q} con q ≠ ⊥, y |K| ≥ 2.`

*Prueba.* (i) Si `J_D={⊥}`, no está incluido en `K ⊆ [0,1]` (los `K_n` lo están y `[0,1]`
es cerrado y aislado de ⊥ en X); falla. (ii) Si `J_D={q}` con `q∈[0,1]`, entonces
`J_D,n={q_n}` con `q_n→q` y `q_n∈K_n`. Para todo n,
`dist(q,K) ≤ |q−q_n| + dist(q_n,K) ≤ |q−q_n| + d_H(K_n,K) → 0`, y K es cerrado; luego
`q∈K`. (iii) Para `{q}⊆K`, `{q}⊊K` si y sólo si K contiene otro punto. ∎

Segunda vía de (ii): IROD §5 ya da `J_D,n ⊆ K_n` por retardación; la inclusión pasa al
límite de Hausdorff por el mismo argumento de distancia, así que la única obligación que la
dinámica aporta a la inclusión es llegar (`q≠⊥`).

**Consecuencia.** En IROD, la obligación 2 del test («pérdida estricta frente al causal»)
equivale a `|K| ≥ 2`, que es una propiedad de la familia marcada `(C_n;s_n,d_n)` y del mapa de
bloques, **no de las dinámicas**. Todo el contenido dinámico del test está en la obligación 1:
`q_D1 = q_D2`. Es la construcción 2.2 de la revisión `2026-10-13-argon-high-contrato`
(«PASS por cardinalidad»), aquí probada para IROD. IROD §7 («techo lógico») lo anticipa; el
lema lo convierte en una equivalencia.

Comprobación en el caso de IROD §8 (cadena): `L_n={n}`, `K={1}`, `|K|=1`; el lema da `FAIL`,
como IROD.

## 2. Aplicación a la familia de dos rutas

Familia de `GROWING_FAMILY_RESPONSE_2026-10-02.md` §§1–2: dos cadenas de `2n` y `3n`
coberturas, `L_n={2n,3n}`, `H_n=3n`, `B_γ,n=e^{-γ/n}A_n`, `γ_1=0`, `γ_2=log(4/3)`.
Respuesta al impulso: `R_γ,n(2n)=e^{-2γ}`, `R_γ,n(3n)=e^{-3γ}`, cero en otro caso:
`(1,1)` y `(9/16,27/64)`. Lo que sigue aplica el mapa de IROD a esa familia; no está en
ninguno de los dos documentos.

- `K_n={g_n(2n),g_n(3n)}`. Por la cota de IROD §3, `g_n(2n)→2/3` y `g_n(3n)→1`; `K={2/3,1}`,
  `|K|=2`.
- Con `θ=1/2` (el de GROWING §1): `τ_1,n=τ_2,n=2n` para todo n, `J_1=J_2={2/3}`.

Por el lema 1, **el par de GROWING es `PASS_FORMAL` del test de llegada de IROD.** Pero las
llegadas coinciden a todo n: el límite no hace ningún trabajo, y la pérdida estricta sólo dice
que hay dos rutas. Es exactamente el patrón trivial que motivó las cláusulas siguientes.

Dependencia del umbral (segunda comprobación, por casos de θ):
- `θ ≤ 27/64`: ambos llegan en `2n`; igualdad.
- `27/64 < θ ≤ 9/16`: ambos llegan en `2n` (D2 por su ruta corta); igualdad.
- `9/16 < θ ≤ 1`: D1 llega en `2n`; D2 nunca alcanza θ, `J_2={⊥}`; falla.

## 3. Cláusulas propuestas

Para una familia admisible y dos dinámicas, además de IROD §7:

- **NT-θ (uniformidad en el umbral).** Se fija antes un intervalo `Θ=[θ_-,θ_+]` con
  `θ_-<θ_+`, y `PASS_FORMAL` se exige para todo `θ∈Θ`. Impide que la igualdad dependa de un
  umbral escogido. En §2, cualquier Θ que entre en `(9/16,1]` da `FAIL`; un Θ dentro de
  `(0,9/16]` no lo impide, así que NT-θ sola no basta.
- **NT-Q (no identidad del escalar a N finito).** Existe `θ∈Θ` tal que `τ_D1,n(θ) ≠ τ_D2,n(θ)`
  para todo n suficientemente grande, con prueba. La igualdad `q_D1=q_D2` debe ser un efecto
  del límite y no una identidad a todo n. En §2, NT-Q falla para todo θ: el par queda excluido.
- **Admisibilidad de la familia.** `H_n→∞`, existencia de K y `|K|≥2` se tratan como
  precondiciones de la familia, comprobables antes de declarar dinámicas. Si fallan, la familia
  es `INADMISSIBLE`, no `FAIL` de las dinámicas. Con esto la cadena de IROD §8 pasaría de
  `FAIL_STRICT_INCLUSION` a `INADMISSIBLE`; **esta reclasificación es una propuesta y no se
  aplica a IROD**.

Con el lema 1 y la admisibilidad, el test de llegada se reduce a: **para todo θ∈Θ, las llegadas
normalizadas de D1 y D2 convergen al mismo punto, siendo distintas a todo n grande.**

## 4. Lo que queda abierto

- No se sabe si la clase de dinámicas lineales sobre coberturas de IROD admite **alguna**
  construcción que cumpla NT-Q e igualdad a la vez (`[OPEN]`). Si no la admite, el test de
  llegada no tiene casos con contenido en esa clase.
- Hueco conocido: un retraso fijo de `O(1)` actualizaciones entre D1 y D2 cumple NT-Q y da
  igualdad tras normalizar por `H_n`, sin contenido. NT-Q no lo excluye.
- La elección entre test de llegada y respuesta lenta (`SLOW_PROTOCOL_RESPONSE`), y la
  relevancia de este frente para 3+1D, son decisiones del PI.

```text
STRICT_INCLUSION_IN_IROD = EQUIVALENT_TO_|K|>=2 (LEMMA_1, DYNAMICS_FREE)
TWO_ROUTE_PAIR_IN_IROD_ARRIVAL_TEST = PASS_FORMAL_TRIVIAL (TAU_EQUAL_AT_ALL_N)
NT_THETA = PROPOSED
NT_Q = PROPOSED
FAMILY_ADMISSIBILITY = PROPOSED_NOT_APPLIED_TO_IROD
NONTRIVIAL_CONSTRUCTION_IN_IROD_CLASS = OPEN
O1_DELAY_HOLE = OPEN
INDEPENDENT_REVIEW = NOT_PERFORMED
CANONICAL_PROMOTION = NONE
```
