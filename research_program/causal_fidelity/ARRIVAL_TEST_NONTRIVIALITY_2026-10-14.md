# Test de llegada: contenido de la inclusión estricta y cláusulas de no trivialidad

Fecha: 2026-10-14 (rev. 1 el mismo día, tras la revisión ciega de §6). Estado:
`DRAFT / ADDENDUM / NOT_CANONICAL / NO_EXECUTION`.
Base: `main @ 1dbae26`. Addendum a `IR_OPERATIONAL_DEFINITION_2026-10-02.md` (IROD).
No modifica el contrato histórico ni IROD. Autor: Claude Opus 5.5. Revisión ciega de una ronda
(gemini-4-argon, `revisiones/2026-10-14-argon-high-addendum-llegada/`); no es revisión humana.
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
como `d(q,⊥)=2`, existe `N_0` tal que para `n≥N_0` es `d_H(J_D,n,{q})<2`, luego
`J_D,n≠{⊥}`: hay llegada, `J_D,n={q_n}` con `q_n=g_n(τ_D,n)` y, por retardación (IROD §4) y
`θ>0`, `τ_D,n∈L_n`, es decir `q_n∈K_n`. Para `n≥N_0`,
`dist(q,K) ≤ |q−q_n| + dist(q_n,K) ≤ |q−q_n| + d_H(K_n,K) → 0`, y K es cerrado; luego
`q∈K`. (En un número finito de n puede no haber llegada; por eso la cota no vale para todo n.) (iii) Para `{q}⊆K`, `{q}⊊K` si y sólo si K contiene otro punto. ∎

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
- `θ > 1`: ninguna llega; `J_1=J_2={⊥}`; falla por el lema 1(i).

## 3. Cláusulas propuestas

Para una familia admisible y dos dinámicas, además de IROD §7:

- **NT-θ (uniformidad en el umbral).** Se fija antes un intervalo `Θ=[θ_-,θ_+]` con
  `θ_-<θ_+`, y `PASS_FORMAL` se exige para todo `θ∈Θ`. Impide que la igualdad dependa de un
  umbral escogido. En §2, cualquier Θ que entre en `(9/16,1]` da `FAIL`; un Θ dentro de
  `(0,9/16]` no lo impide, así que NT-θ sola no basta.
- **NT-Q (no identidad del escalar a N finito).** Para **todo** `θ∈Θ`, `τ_D1,n(θ) ≠ τ_D2,n(θ)`
  para todo n suficientemente grande, con prueba. La igualdad `q_D1=q_D2` debe ser un efecto
  del límite y no una identidad a todo n. En §2, NT-Q falla para todo θ: el par queda excluido.
  (La versión anterior decía «existe θ», en contradicción con el resumen de abajo. Con «existe»,
  la revisión construye un par con llegadas idénticas en todo `[1/4,1/2)` que sólo difiere en
  `θ=1/2`; comprobado. Con «para todo» queda excluido.)
- **Admisibilidad de la familia.** `H_n→∞`, existencia de K y `|K|≥2` se tratan como
  precondiciones de la familia, comprobables antes de declarar dinámicas. Si fallan, la familia
  es `INADMISSIBLE`, no `FAIL` de las dinámicas. Con esto la cadena de IROD §8 pasaría de
  `FAIL_STRICT_INCLUSION` a `INADMISSIBLE`; **esta reclasificación es una propuesta y no se
  aplica a IROD**.

Con el lema 1 y la admisibilidad, el test de llegada se reduce a: **para todo θ∈Θ, las llegadas
normalizadas de D1 y D2 convergen al mismo punto, siendo distintas a todo n grande.**

## 4. La clase lineal de IROD y lo que el test de llegada puede medir

Clase lineal de IROD: `X_i,n(k+1)=α_i,n A_n X_i,n(k)`, `α_i,n>0`, normalización común `a_n>0`.
La respuesta al impulso es `R_i,n(k)=a_n m_n(k) α_i,n^k`, con `m_n(k)=(A_n^k)[d_n,s_n]` el número
de caminos de cobertura de longitud k; `L_n={k: m_n(k)≥1}`. Resultados de la revisión ciega,
comprobados a mano en esta sesión:

**Teorema 2 (imposibilidad).** Si para n grande `m_n` no crece en `L_n` y `α_i,n∈(0,1]`, ninguna
construcción cumple NT-Q con `J_D1=J_D2≠{⊥}`.
*Prueba.* `R_i,n` es no creciente en `L_n`, así que su máximo está en `k_min=min L_n` y, para todo
`θ>0`, `τ_i,n(θ)∈{k_min,∞}`. Con llegada en ambas, `τ_1,n=τ_2,n=k_min`. ∎
Cubre la cadena de IROD §8 y la familia de dos rutas de §2 (`m_n≡1`).

**Teorema 3 (construcción).** Sea `1≤d_n<n` con `d_n/n→0`. Entre `s_n` y `d_n` (marcas) se unen,
disjuntas salvo extremos, una cadena de `2n` coberturas, ocho de `2n+d_n` y una de `3n`. Entonces
`L_n={2n,2n+d_n,3n}`, `H_n=3n`, `m_n=(1,8,1)`. Con `a_n=1`, `α_1,n=1`, `α_2,n=2^{-1/n}` y
`Θ=[1/3,2/3]`: `R_2,n(2n)=1/4<1/3` y `R_2,n(2n+d_n)=2^{1−d_n/n}≥1`, así que
`τ_1,n(θ)=2n≠2n+d_n=τ_2,n(θ)` para todo n y todo θ∈Θ; ambas llegadas normalizadas tienden a
`2/3`; `K={2/3,1}`. Cumple admisibilidad, NT-θ y NT-Q, y es `PASS_FORMAL` para todo θ∈Θ. ∎
Con `d_n=1` es el retraso de `O(1)` que la versión anterior dejaba como hueco: realizado dentro de
la clase lineal, no sólo con respuestas declaradas a mano.

**Lema 4 (qué mide la igualdad).** Si `τ_1,n/H_n` y `τ_2,n/H_n` convergen, entonces
`q_D1=q_D2 ⟺ (τ_1,n−τ_2,n)/H_n → 0`.
*Prueba.* Por IROD §3, `|g_n(k)−k/H_n| < b_n/H_n → 0` uniformemente en k, así que
`q_Di = lim τ_i,n/H_n`. ∎ Segunda vía: si `|τ_1,n−τ_2,n| ≥ cH_n` con `c>0`, entonces
`|g_n(τ_1,n)−g_n(τ_2,n)| ≥ c−b_n/H_n`, y los límites difieren. Además, si ambas llegadas caen en
la misma celda de bloques (diferencia `< b_n` y mismo `⌊τ/b_n⌋`), `g_n` las identifica ya a n finito.

**Lectura.** Con los lemas 1 y 4, el test de llegada de IROD, con NT-θ, NT-Q y admisibilidad,
equivale a: `|K|≥2`, y para todo θ∈Θ las llegadas difieren a todo n grande pero su diferencia es
`o(H_n)`. Esa es exactamente la información que la normalización por `H_n` borra por
construcción. Dentro de este test no hay una frontera formulable entre «diferencia microscópica
trivial» (teorema 3 con `d_n=1`) y «contenido IR»: ambas son `o(H_n)`. Reforzar NT-Q con un orden
de diferencia mínimo (p. ej. `|τ_1,n−τ_2,n|→∞`) desplaza el hueco sin cerrarlo (teorema 3 con
`d_n=⌊√n⌋`). Esto **no** es un no-go de la fidelidad causal; es un límite del test basado en un
único escalar de llegada normalizado, y apoya la vía de respuesta lenta
(`SLOW_PROTOCOL_RESPONSE`, `GROWING_FAMILY_RESPONSE`), que no depende de él.

Siguen abiertas la elección entre test de llegada y respuesta lenta, y la relevancia de este
frente para 3+1D: son decisiones del PI.

```text
STRICT_INCLUSION_IN_IROD = EQUIVALENT_TO_|K|>=2 (LEMMA_1, DYNAMICS_FREE)
TWO_ROUTE_PAIR_IN_IROD_ARRIVAL_TEST = PASS_FORMAL_TRIVIAL (TAU_EQUAL_AT_ALL_N)
NT_THETA = PROPOSED
NT_Q = PROPOSED_FOR_ALL_THETA
FAMILY_ADMISSIBILITY = PROPOSED_NOT_APPLIED_TO_IROD
NT_Q_IMPOSSIBLE_NONAMPLIFYING_NONINCREASING_PATHS = PROVED (THEOREM_2)
NT_Q_CONSTRUCTION_IN_LINEAR_CLASS = PROVED (THEOREM_3)
ARRIVAL_EQUALITY_IN_IROD = EQUIVALENT_TO_o(H_n)_DIFFERENCE (LEMMA_4)
TRIVIAL_VS_IR_CONTENT_SEPARABLE_IN_ARRIVAL_TEST = NO
INDEPENDENT_REVIEW = ONE_BLIND_ROUND_GEMINI_ARGON; HUMAN_REVIEW_NOT_PERFORMED
CANONICAL_PROMOTION = NONE
```
