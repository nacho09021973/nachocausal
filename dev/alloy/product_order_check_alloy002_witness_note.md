# Product-Order Admissibility Check — Alloy 002 Witness

> Minimal falsification test ordered by comité 010 §9 step 1.
> Produced by `dev/alloy/product_order_check_alloy002_witness.py`.
> This is a dev note (exploration track); no sealed path, no seeds.

## 1. Context

Comité 010 (`docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md`)
returned `RECOMMEND_REVISE_AND_RECONVENE` with the following highest-priority reversible step:

> "For the Alloy 002 witness lt-relations, perform an explicit product-order embedding check:
> do there exist two total orders on {Element$0…$3} whose intersection (= 2D product order)
> contains the completion A and B lt-relations respectively, respecting convexity?
> If neither completion passes this check… update the Alloy summary from PHYSICAL_LAYER_OPEN to
> PHYSICAL_LAYER_EMPTY_EVIDENCE."

## 2. Witness (from Alloy 002 trace, §4)

| Object | Elements | lt pairs (direct, already TC-closed) |
|---|---|---|
| Observation | {E2, E3} | {(E2, E3)} |
| Completion A | {E1, E2, E3} | {(E2,E1), (E2,E3), (E3,E1)} — chain E2 < E3 < E1 |
| Completion B | {E0, E2, E3} | {(E0,E3), (E2,E0), (E2,E3)} — chain E2 < E0 < E3 |
| Skolem | — | E3: `isInterface[B,E3] ∧ ¬isInterface[A,E3]` |

## 3. Checks performed

For each completion the script verifies:

1. **Transitive closure** — lt is already transitively closed (no extension needed).
2. **Valid strict partial order** — irreflexive and transitively closed. Both: ✓
3. **2D product-order realizability** (dim_DM ≤ 2) — brute-force search over all pairs of
   linear extensions for a pair (L1, L2) such that x <_P y iff x <_L1 y ∧ x <_L2 y.
4. **Convexity of observation** — for all x, y ∈ obs, for all hidden h: ¬(x < h < y in
   completion). This is the physically admissible condition: a hidden element cannot lie causally
   inside the observed region.

## 4. Results

### Completion A (chain E2 < E3 < E1, hidden E1 above observation)

| Check | Result |
|---|---|
| Valid strict partial order | ✓ |
| 2D product-order realizable | ✓ L1 = L2 = (E2, E3, E1) |
| Observation convex | ✓ (E1 is above all observed elements, not between them) |
| **Admissible** | **YES** |
| Interface decision | ∅ (E3 is not maximal in A; E1 is above it) |

### Completion B (chain E2 < E0 < E3, hidden E0 inside observation)

| Check | Result |
|---|---|
| Valid strict partial order | ✓ |
| 2D product-order realizable | ✓ L1 = L2 = (E2, E0, E3) |
| Observation convex | **✗** — hidden E0 satisfies E2 < E0 < E3 in the completion |
| **Admissible** | **NO** |
| Interface decision | {E3} (E3 is maximal in B; this is the positive side of the counterexample) |

## 5. Verdict

**PHYSICAL_LAYER_EMPTY_EVIDENCE**

The Alloy 002 counterexample achieves the differing interface decisions for E3 (interface in B,
not interface in A) *only* by using Completion B, which fails the convexity constraint: the
hidden element E0 is placed **causally between** the two observed elements E2 and E3.

A physically admissible completion — one consistent with a convex region of a 2D product order
(Prop 7.3: Kruskal–Szekeres) — cannot have a hidden element inside the causal interior of the
observed subposet. In any Poisson sprinkling of a manifoldlike 1+1D patch, all elements causally
between two observed elements are themselves in the observable region (assuming the observation is
a down-set or convex region, as physically modelled).

Consequence:

- The Alloy 002 witness **does NOT demonstrate physical non-identifiability**.
- It demonstrates only *logical* non-identifiability under an unconstrained completion class.
- The update to the Alloy 002 summary is:

  ```
  PHYSICAL_LAYER_OPEN  →  PHYSICAL_LAYER_EMPTY_EVIDENCE
  ```

- The physical non-identifiability proposition
  `COMPLETION_AND_TRUNCATION_NONIDENTIFIABILITY` remains `NEEDS_PRECISE_COMPLETION_CLASS`
  (comité 010 verdict). The absence of a valid physical witness strengthens that verdict.

## 6. What this does and does not establish

**Does establish:**
- No physically admissible 1-element extension of a 2-element observed order produces
  incompatible interface decisions (under the convexity constraint).
- The Alloy 002 witness is a purely combinatorial artefact with no manifoldlike realisation.

**Does NOT establish:**
- That physical non-identifiability is impossible for larger or differently structured
  completions (e.g., the Schwarzschild-vs-Hayward case noted by the physicist in comité 010).
- That the C1 reference rule R=Max(C) is adequate (it remains trivially NO_INTERFACE).
- Any change to the five open definitions or to the C1 selector status.

## 7. Next steps (per comité 010 §9)

1. ✅ **This check** — completed; result: PHYSICAL_LAYER_EMPTY_EVIDENCE.
2. ⬜ **Close the five definitions** (`dev/PR003_C1_COMPLETION_CLASS_DEFINITIONS.md`):
   observed subposet class, admissible completion class 𝔄, induced reference rule (order-only,
   no r=2M), pullback rule, incompatibility predicate.
3. ⬜ **Reconvene comité 011** with closed proposition + this check result in the dossier.

## 8. Provenance

- Git HEAD at run time: `16e04e4` (tree clean)
- Script: `dev/alloy/product_order_check_alloy002_witness.py`
- Python: system python3 (no seeds, no BH/MINK data, no thresholds read)
- Alloy source: `formal/alloy/completion_nonidentifiability_interface_counterexample.als`
- Seal SHA (thresholds.py): `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (unchanged)
- Date: 2026-06-29
