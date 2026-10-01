# Puente a Schwarzschild 3+1D — análisis de admisibilidad del primer blanco

> **STATUS: `BLOCK_OPENED_VIA_B / PI_SIGN_OFF_RECORDED / THEORY_ONLY / NO_NEW_RUNS / NO_SEAL_TOUCHED`.**
> Abre el bloque **puente 3+1D** como programa nuevo con claim grammar propio.
> No autoriza simulación, semillas ni preregistro. No modifica `prereg-002` ni ningún
> artefacto congelado. `PHASE_0_R1` queda **intacto y vigente** (§2).

**Fecha:** 2026-09-12 · **HEAD al redactar:** `a295311`

```text
PI_SIGN_OFF          = 2026-09-12 (Nacho / PI)
APERTURA             = VIA_B_PROGRAMA_NUEVO
PHASE_0_R1           = UNCHANGED_IN_FORCE
BLANCO_CONGELADO     = phi(lambda) = mu(K ∩ {r<2M}) / mu(K)
PARAMETRO_OBSERVABLE = lambda (forma del patch); M es gauge a fixed_n
NEW_VALIDATION_RUNS  = NOT_AUTHORIZED
```

---

## 1. Línea roja registrada (sin trabajo pendiente)

El estado canónico ya coincide con la línea roja pedida. No hay que cambiar nada:

```text
T19_STRUCTURAL_RESULT        = CLOSED_AUTONOMOUSLY
POISSON_QMD_BRANCH           = PARKED_OPEN_REDUCED
PREREG_002                   = UNCHANGED
NEW_VALIDATION_RUNS          = NOT_AUTHORIZED
SCHWARZSCHILD_3P1            = NOT_AUTHORIZED
```

Anclaje: `research_program/README.md` (bloque de estado 2026-09-12) y
`docs/hoja_de_ruta_septiembre_2026.md`. La prohibición de runs se mantiene.

---

## 2. Colisión de gobernanza — `PHASE_0_R1` sigue vigente

El bloque propuesto («puente a Schwarzschild 3+1D», reconstruir «una localización relativa del
horizonte») recae **literalmente** sobre lo que el propio programa abandonó como norte:

```text
ABANDONED_AS_PROGRAM_NORTH:
  localizar o reconstruir estructura de horizonte de Schwarzschild 3+1
  (evento global, región atrapada, codim-2, trapping, o proxy de los mismos)
  mediante un nuevo observable order-only en la línea de la matriz post-PR008.
```

`research_program/synthesis/phase0_program_north_decision.md:43-55`, firmado por el PI
**sin enmiendas** el 2026-07-28 (`:167-174`). No ha sido revocado: los `R1` de
`docs/program_reopening_note_2026-07-31.md` y `_2026-08-28_R4.md` son **otro** `R1`
(paper de límites), no éste.

Lo prohibido sin nuevo `PI_SIGN_OFF` que revoque R1 (`:64-68`):

- kill tests o preregistros de **nuevos localizadores de horizonte order-only**;
- abstracts tipo *«towards reconstructing BH horizons from causal sets»* sin la negación
  explícita del paquete finito order-only.

Lo que R1 **sí** deja abierto (`:57-62`):

- abrir **un programa nuevo** (Order+Number, clasificación) **con claim grammar propio**,
  *no* como continuación del reconstructor.

**Decisión del PI (2026-09-12): VÍA B.** El bloque se abre como **programa nuevo con claim
grammar propio**, parametrizado por la forma del patch `λ`. `R1` **no** se revoca y sigue
vigente. R1 no se abandonó por desánimo sino por una conjunción fallida target+canal+dimensión
que sigue siendo cierta (§3); revocarlo sin cambiar el target habría repetido el mismo fallo.

Obligaciones que esta vía impone a todo texto del bloque:

1. No nombrarse ni redactarse como continuación del norte reconstructor de horizonte.
2. No proponer kill tests ni preregistros de localizadores de horizonte order-only
   de la línea post-PR008 (seguiría prohibido: `phase0:64-68`).
3. Ningún abstract «towards reconstructing BH horizons from causal sets» sin la negación
   explícita del paquete finito order-only.
4. El parámetro del programa es `λ`, y el blanco `φ(λ)`; `M` no es blanco en ningún canal.

---

## 3. El blanco no es libre: la dilatación es gauge puro a `fixed_n`

La pregunta «¿cuál es el primer objeto geométrico 3+1D?» está **más restringida de lo que
parece**. Verificado simbólicamente en
`research_program/puente_3p1/2026-09-12/verify_dilation_gauge.py`
(salida `verification_dilation_gauge.json`, `CONCLUSION = DILATION_IS_PURE_GAUGE_AT_FIXED_N`):

Sobre la carta Kruskal congelada en `op11_spherical_dual_target.md` §2:

- **C1.** `f(s) = (s-1)e^s` tiene `f'(s) = s e^s > 0` en `s>0`, luego `-UV = f(r/2M)` determina
  `s = r/(2M)` a partir del producto `UV` **sin M explícito**.
- **C2.** `sqrt(-det g) = 32 M^4 · s e^{-s} · |sin θ|`: la dependencia en `M` del elemento de
  volumen factoriza **exactamente** como `M^4`.
- **C3.** Con `λ` fijo el patch es M-independiente en coordenadas Kruskal, luego
  `μ_M(K) = M^4 μ_1(K)` y la medida normalizada `μ_M/μ_M(K)` **no depende de M**.

Lectura física, que es la que importa:

> A `fixed_n` y con patch coescalado, el experimento 3+1D **no es una familia parametrizada por
> M**. Es un único experimento cuyos únicos parámetros son la forma del patch `λ` y el sector `σ`.
> `M` es una dirección gauge, no un parámetro observable.

Esto reproduce y explica `TV=0` de `op12_tv_zero_3p1.md` §3, y sube el terminal
`TARGET_NONIDENTIFIABLE_TV_ZERO` (`op12:§8`) de resultado a **restricción de diseño**.

Además, el escalar de localización de OP-1.1, `h_M(x) = r(x)/(2M) - 1`, es por C1 una función
**sólo de `UV`**: es idéntico para todo `M`. Es decir, la localización relativa del horizonte
sobrevive intacta a la degeneración de escala — pero por la misma razón por la que `M` muere:
porque en esta familia toda la información dilatación-invariante del horizonte está en `λ`.

---

## 4. Filtro de admisibilidad (cualquier blanco 3+1D debe pasar los cuatro)

| # | Criterio | Falla si |
|---|---|---|
| A1 | **Invariancia de dilatación.** El blanco es constante en la órbita `M → aM` con patch coescalado. | `TARGET_NONIDENTIFIABLE_TV_ZERO` |
| A2 | **No fuga de cardinalidad.** El blanco no se lee de `E[N]` ni de ninguna marginal de conteo global. | `CARDINALITY_LEAK` |
| A3 | **Intrínseco al poset.** Definible sobre la clase de isomorfismo no etiquetada (más, si acaso, elementos distinguidos como direcciones). El embedding sólo puntúa. | `EMBEDDING_ONLY_SCORES_VIOLATION` |
| A4 | **No es un localizador order-only de la línea post-PR008.** | `PHASE_0_R1_COLLISION` |

### Cribado de los candidatos sobre la mesa

| Candidato | A1 | A2 | A3 | A4 | Veredicto |
|---|---|---|---|---|---|
| `τ = 2M` absoluto, canal `fixed_n` | ✗ | — | ✓ | ✓ | **Muerto por C3**; ya tipado `DOES_NOT_TRANSFER` (`survival_matrix_1p1_to_3p1.md` §2) |
| `M`, canal `order+number` con `ρ` conocida | ✓ | ✗ | ✓ | ✓ | **Trampa**: la identificabilidad de `op12` §5 entra por la media Poisson `ρM^4μ_1`. Se estaría leyendo `M` del conteo, no del orden |
| Carácter sectorial `Chi` (BH/WH) | ✓ | ✓ | ✓ | ✓ | Admisible, pero es **binario**: no es reconstrucción geométrica, y `op12` §6 deja abierta la dual-invariancia |
| **Funcional dimensional de `λ` que localiza el corte del horizonte dentro del patch** | ✓ | ✓ | ✓ | ✓ | **Recomendado** (§5) |

---

## 5. Blanco congelado — `φ(λ)`, fracción de volumen interior

> **Congelado por `PI_SIGN_OFF` 2026-09-12.** Cambiar el blanco exige nueva firma.

```text
φ(λ) = μ_M(K_{M,λ} ∩ {h_M < 0}) / μ_M(K_{M,λ})
```

Por C2–C3 el prefactor `M^4` se cancela: `φ` depende **sólo de `λ`**, y es exactamente la
fracción de la región observada que cae dentro del horizonte.

Por qué es el primer blanco correcto:

1. **Pasa A1 por construcción**, no por suerte: es un cociente de medidas coescaladas.
2. **Pasa A2**: es una fracción, invariante bajo reescalado de `N`; no sobrevive ninguna
   información de escala global en ella.
3. **Es inequívocamente geométrico y físico**: «qué parte de lo que veo está dentro del
   horizonte», sin depender de foliación ni de horizonte aparente (`op11` §4).
4. **Ataca terreno declarado abierto**, no cerrado: `op12` §7 lista *«variar la forma del patch
   λ»* y *«patches no coescalados con M»* entre los puntos abiertos de la clasificación `TV=0`.
5. **Es un programa nuevo con claim grammar propio** (VÍA B): el parámetro es `λ`, no un
   localizador de horizonte de la matriz post-PR008 — pasa A4.

### Cadena contractual a demostrar

```text
geometría 3+1D        g_{M,λ}^σ  (Kruskal, patch λ, sector σ)   [congelado: op11 §2]
        ↓ L1
ley del causal set    P^K_{λ,σ,n} sobre posets no etiquetados   [canal fixed_n, op11 §5]
        ↓ L2
observable intrínseco O: [P] → R                                 [POR DEFINIR]
        ↓ L3
parámetro geométrico  φ(λ) ∈ (0,1)                               [POR DEMOSTRAR]
```

Obligación por eslabón, con su terminal:

| Eslabón | Obligación | Terminal si falla |
|---|---|---|
| L1 | El muestreo de `μ/μ(K)` induce `P^K_{λ,σ,n}` bien definida; `λ` congelado antes de ver nada | `FAILED_DATA_CONTRACT` |
| L2 | `O` definible sobre la clase de isomorfismo; el embedding sólo puntúa | `EMBEDDING_ONLY_SCORES_VIOLATION` |
| L3 | **Separación**: `φ(λ) ≠ φ(λ')` ⟹ `TV(P_{λ,n}, P_{λ',n}) > 0` a algún `n` tratable | `TARGET_NONIDENTIFIABLE_TV_ZERO` |

**L3 es la frontera real y es una pregunta de teoría pura**, sin simulación: ¿separa la ley del
poset no etiquetado dos formas de patch con distinta fracción interior? La dirección de garantía
debe declararse antes: una cota `TV ≥ ·` (positiva, difícil) o una cota `TV ≤ ·` (ceguera, el
patrón que este programa ya sabe certificar). Precedente metodológico: PR011 §1.

---

## 6. Primer paso propuesto (teoría, sin cálculo)

`B1` — **Par testigo mínimo en `λ`.** Exhibir dos formas de patch `λ_0 ≠ λ_1` con
`φ(λ_0) ≠ φ(λ_1)` y decidir, analíticamente, si el lema de biyección bimedible de
`op12_tv_zero_3p1.md` §2 las acopla (⟹ `TV=0`, blanco muerto otra vez) o si existe una
obstrucción. Es el análogo 3+1D de `wp4_two_point_theorem.md` y no requiere ejecutar nada.

Regla de admisión del bloque, tal como se pidió: **todo trabajo nuevo declara en una frase qué
eslabón (L1/L2/L3) avanza. Si no puede, no entra.**

---

## 7. Qué queda explícitamente fuera

- Reconstruir «el espacio-tiempo» o el horizonte global: `claim_grammar.md` §3 (teleología).
- `M` absoluto en cualquier canal, como blanco de este bloque.
- Cualquier ejecución: `NEW_VALIDATION_RUNS = NOT_AUTHORIZED` se mantiene.
- Desaparcar la rama Poisson y tocar `prereg-002`.

## 8. Fuentes

- `research_program/synthesis/phase0_program_north_decision.md` §2, §7 (R1, firma PI)
- `research_program/synthesis/op11_spherical_dual_target.md` §2, §4, §5 (carta, target, canal)
- `research_program/synthesis/op12_tv_zero_3p1.md` §3, §5, §7, §8 (órbita, Poisson, abiertos)
- `research_program/synthesis/survival_matrix_1p1_to_3p1.md` §2 (`τ = DOES_NOT_TRANSFER`)
- `research_program/synthesis/pr011_mass_distinguishability_viability.md` §1 (patrón de viabilidad)
- `docs/claim_grammar.md` §1, §2, §3 (requisitos de claim, etiquetas, teleología)
- `research_program/puente_3p1/2026-09-12/verify_dilation_gauge.py` (C1–C3, verificado)
