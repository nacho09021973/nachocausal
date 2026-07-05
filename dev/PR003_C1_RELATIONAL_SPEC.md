# PR-003 C1 relational specification — closed writing draft

Status: **dev specification, no data, no freeze, no result**.

This document closes the C1 relational definition in writing enough to make the
next review meaningful. It does **not** promote C1, does **not** authorise a
probe, does **not** touch the sealed estimator, and does **not** claim horizon
reconstruction.

## 1. Object

Input is only a finite causal poset represented by its boolean past matrix `C`.
No embedding, coordinates, `r`, `t`, Schwarzschild labels, or scoring module may
enter the construction.

C1 is interpreted through the finite relational interface

```text
H[C; R] = {(x,y) : x in A_R, y in B_R, y covers x}
A_R = down(R)
B_R = C \ A_R
```

`[CORRECCIÓN 2026-07-02 — orientación]` La versión previa (`x in B_R, y in A_R`) es demostrablemente
vacía para todo `R` en todo preorden (`A_R` es down-set ⇒ ningún link sale de `B_R` hacia `A_R`);
ver notas §9.1.1 y el teorema-lápida `relationalHorizonOld_eq_empty` en
`formal/HorizonFormal/HorizonFormal/Horizon.lean`. La interfaz corregida son los links entrantes
(infalling), orientación Dou–Sorkin.

where `R` is an internally selected relational reference subset. In Lean terms:

- `RelationalHorizon R` supplies the finite interface;
- `IdealEnd` is only the provisional ambient-end vocabulary;
- `ChainEnd` is the cofinal-direction vocabulary inside a chosen ambient ideal.

The operational C1 observable is a finite-interface statistic, not an event
horizon.

## 2. Closed rule for selecting `R`

For this draft, `R(C)` is the set of maximal elements of the finite poset:

```text
R(C) = Max(C) = {x : no y satisfies x < y}.
```

Reasoning:

- it is order-only and label-free;
- it is available in every finite causet;
- it gives a concrete reference subset for `H[C;R]`;
- it is intentionally conservative: if this makes `H[C;R]` too boundary-like or
  trivial, C1 fails this draft and must be revised before any probe.

Known risk: maximal elements are strongly coupled to the sampling wall. The
definition therefore cannot pass by detecting a one-level top boundary; it must
also pass the persistence/asymmetry requirements below.

## 3. Interface measured

Given `R = Max(C)`:

```text
A_R = {x : exists r in R, x <= r}
B_R = C \ A_R
H[C;R] = cover edges from A_R into B_R (infalling; corrected orientation, see §1).
```

The measured interface object is the set of ordered cover pairs `(x,y)` in
`H[C;R]`. Any downstream antichain or level summary must be derived from this
set and the order relation alone.

If `H[C;R]` is empty, C1 returns `NO_INTERFACE`, not a physical failure or
success.

## 4. Persistence function

Define intrinsic height

```text
h(x) = longest-chain height from minimal elements to x.
```

For each integer level `k`, define the level slice of the interface:

```text
H_k = {(x,y) in H[C;R] : h(x) <= k < h(y)}.
```

The persistence trace is:

```text
P(k) = 1[H_k is nonempty].
```

C1 records the maximal consecutive run length of `P(k)=1`:

```text
persist(C) = max length of consecutive k with H_k != empty.
```

No threshold is fixed here. Any future threshold on `persist(C)` remains
`OPEN` and must be frozen before data.

## 5. Asymmetry function

For a nonempty interface slice `H_k`, define:

```text
L_in_to_out(k)  = #{(a,b) cover relation : a in A_R-side slice, b in B_R-side future reach}
L_out_to_in(k)  = #{(a,b) cover relation : a in B_R-side slice, b in A_R-side future reach}
```

Because the exact side-slice construction is not yet uniquely fixed, this draft
does **not** freeze a numeric asymmetry score. It fixes only the required shape:
the score must compare two order-defined directed reach/link counts across the
same interface slice, and it must be evaluated by the selection Guard-v before
any data use.

`[CORRECCIÓN 2026-07-03 — vacuidad estructural de una pata, y separación de
tracks]` Si "A_R-side future reach" denota alcance dentro de `A_R`, entonces
`L_out_to_in(k) = 0` idénticamente: `B_R` es up-set, luego ninguna relación
causal (en particular ningún cover) sale de `B_R` hacia `A_R`
(`relationalBlackRegion_no_escape`,
`formal/HorizonFormal/HorizonFormal/Horizon.lean`). La comparación bidireccional
a través de `H` es por tanto inválida: una de sus dos patas es un cero
estructural — guardarraíl que no puede fallar.

Ningún `ASYMMETRY_SCORE` alternativo forma parte actualmente de la definición
cerrada del track event-horizon relativo a `R`. Dado `R`, la separación
`A_R = down(R)` / `B_R = C \ A_R` es temporal y canónica; definir `H[C;R]` y su
propiedad one-way no requiere realizer, orden conjugado, caras izquierda/derecha
ni el lema de dos caras. Un score basado en dos caras laterales pertenece al
track aparente/validador independiente y continúa condicionado al problema
abierto del lema de bipartición (notas §7.4, `III_PENDING_TWO_FACE_LEMMA`); no
bloquea la definición de `H[C;R]` dado `R`. **El bloqueo fundacional de este
track es exclusivamente la selección order-only de `R(C)`** — cuya carga
discriminante es demostrar que el selector no detecta pared, truncación ni
inhomogeneidad, no recuperar dos caras espaciales.

Status: `ASYMMETRY_SCORE = OPEN`.

## 6. C1 output contract

The selection subroutine returns a structured element-label object:

```text
{
  "R": set[element],
  "interface": set[(element, element)]
}
```

`active_levels`, `persistence_run`, asymmetry scores, and other scalar or
ordinal metadata are downstream observables, not selector output. They must be
guarded separately as observables if they become load-bearing.

## 7. Guard-v selection requirement

Before any C1 probe, the implementation must pass:

```text
verify_selection_order_only(C, c1_selector, seed=s)
```

where relabelling the poset must relabel-conjugate:

- the selected `R`;
- the selected interface pairs;
- any selected antichain or argmin/argmax elements.

Failure means C1 fails before physics scoring.

## 8. Explicitly open

- `ASYMMETRY_SCORE`: exact side-slice and directed count formula.
- `PERSISTENCE_THRESHOLD`: no numeric threshold is fixed.
- `BULK_CONTROL`: how to distinguish maximal-wall artefacts from a genuine
  persistent relational partition without coordinates.
- `C1_PROMOTION`: blocked until committee/auditor review of this closed draft.
- `PHYSICAL_INTERPRETATION`: still only a finite apparent/trapping precursor,
  never an event horizon or reconstruction claim.

## 9. Preflight status after comité 009

Comité 009 authorised only a scoped negative preflight: implement the written
`R=Max(C)` selector on synthetic finite posets and assert that it trivialises.

Implemented artefacts:

- `nachocausal/c1_selector.py`
- `tests/test_c1_selector.py`

Verified behavior:

```text
R = Max(C)
A_R = down(R) = C
B_R = empty
H[C;R] = empty
status = NO_INTERFACE
```

This is not a C1 signal and not a probe. It records that the current reference
rule is structurally degenerate on finite posets. Any replacement for `R`, any
fallback after `NO_INTERFACE`, and any persistence/asymmetry/bulk-control score
remain `OPEN` and require fresh review before data.

`[CORRECCIÓN 2026-07-03 — orientación en el código]` La implementación original
de `c1_selector.py` construía la interfaz con la orientación vieja
(`x in B_R, y in A_R`), que es vacía para todo `R` (teorema-lápida
`relationalHorizonOld_eq_empty`) — de modo que la aserción `interface == empty`
del preflight no podía fallar por diseño y no testeaba la regla `R = Max(C)`.
El veredicto del preflight sigue siendo válido: su contenido real es
`down(Max(C)) = C` (⇒ `B_R = ∅`), que el test verifica por separado y que hace
la interfaz vacía también con la orientación corregida. El código está ahora
alineado con la orientación corregida (infalling `A_R → B_R`), con un testigo
ejecutable de no-vacuidad sobre el poset en V del Lean
(`tests/test_c1_selector.py::test_corrected_orientation_nonempty_on_lean_witness`)
para que el guardarraíl pueda fallar.
