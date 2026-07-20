# C5 — Existence of an order-only, threshold-free matrix→block map

STATUS: DOCUMENTARY_EXISTENCE_NOTE / CANDIDATE_5_NOT_YET_OPENED / NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS  
DATE: 2026-07-20  
BINDS_TO: `docs/comite/comite_decision_040_c5-search-space-adjudication.md` (`d5759e6`),  
`docs/comite/comite_decision_041_c5-1-matrix-to-block-map-adjudication.md` (`bb3d1a7`)

This note answers one question only:

```text
Does there exist a deterministic, order-only, relabel-invariant map
  (finite poset / common-future matrix) → block/partition or abstention
without any calibrable free parameter (threshold, k, learned rank, seed-tuned cut),
that can satisfy the simultaneous criteria S1–S4 of Decision 041?
```

It does **not** open `CANDIDATE_5`, freeze an observable, authorize code, seeds, or runs.

---

## 1. Three different questions (must not be mixed)

| ID | Question | Answer in this note |
|---|---|---|
| Q0 | Do incomplete *families* (exact / spectral / hierarchical) pass C5.1 as written? | **No** — Decision 041, terminal `C5_1_NO_CLOSED_MAP`. |
| Q1 | Does there exist **some fully specified** order-only, parameter-free map of the right type? | **Yes for formal maps of the poset** (not of the matrix alone). See §3–§5. |
| Q2 | Does that existence give a horizon localizer or `CANDIDATE_5`? | **No.** Existence ≠ physics ≠ candidate. |

Decision 041 correctly rejected unfinished families. That is compatible with Q1 being yes for a *completed instance*.

---

## 2. What “without threshold” means here

**Allowed (not free calibration):**

- Fixed combinatorial constants chosen once in the definition (e.g. “at least two cells”, “cell size ≥ 2”, “one maximal peel”).
- Canonical algebraic cuts that are not free numbers: exact equality; sign relative to **0** of a **named** eigenvector; “edge present iff weight equals the matrix-wide maximum”.
- Mandatory abstention on ties, multiplicities, zeros, total symmetry.

**Forbidden (calibrable / free):**

- Continuous cut heights, target cluster counts, gap statistics chosen after data.
- Operator / rank / normalization left open “to be chosen later”.
- Label-order or input-order defaults for ties.
- Seed-tuned floors, alphas, or effect sizes.

---

## 3. Pure matrix maps: what exists and what cannot

Let `A` be a symmetric matrix on `M = Min(C)` built order-only (e.g. `A_ij = |J⁺(i) ∩ J⁺(j)|`). A **pure matrix map** is any `f(A) → partition/abstention`.

### 3.1 Formal maps without free parameters exist (S1–S3 shape)

Examples (definitions only; none frozen as candidates):

1. **Exact row partition + emission rule**  
   Cells = equivalence classes of identical rows (fixed diagonal convention).  
   Emit the unordered partition iff it has at least two cells and no cell is a singleton; else abstain.  
   - Deterministic, order-only if `A` is, relabel-invariant, no free continuous threshold.  
   - Ties of “which block is special” do not arise if the **output is the whole partition**, not a single preferred cell.

2. **Equitable refinement (color refinement) + same emission rule**  
   Same story; strictly finer than exact rows when weights require it.

3. **Fixed spectral instance** (only if operator is **named**, not left open)  
   e.g. combinatorial Laplacian `L = D − A` with `D_ii = Σ_j A_ij`; if the second-smallest eigenvalue is simple and the corresponding eigenvector has no zero entry and both signs, emit the unordered sign bipartition; else abstain.  
   Sign flip does not change the unordered bipartition. Zero is not a calibrated threshold; it is the unique neutral of a real line.

4. **Maximal-weight support graph**  
   Put an undirected edge `{i,j}` iff `A_ij = max_{p≠q} A_pq`. Connected components of that graph; abstain if the max is achieved in a way that leaves the rule ambiguous under a predeclared tie policy (or always take the full argmax graph — still parameter-free). Partition = components if nontrivial; else abstain.

So: **“no order-only map without threshold exists at all” is false** for S1–S3-style combinatorial emission.

### 3.2 Pure matrix maps cannot carry physical boundary control (S4)

**Indistinguishability lemma (conceptual).**  
If two finite posets `C_roof` and `C_phys` induce the **same** matrix `A` on their minimal sets (same sizes, same entries up to simultaneous relabeling), then **every** pure map `f(A)` returns the same output on both.

Therefore no function of `A` alone can:

- emit a “horizon block” on `C_phys`, and  
- abstain / reject as roof-dominated on `C_roof`,  

whenever those two situations share `A`.

Roof-only, side-wall-only, density-lobe, and horizon-like configurations are not known to be separated by `A` as a complete invariant. Even if some pairs differ in `A`, S4 as **direct boundary discipline** is not guaranteed by an arbitrary `f(A)`; and when they do **not** differ, S4 is impossible for pure `f`.

**Conclusion for pure matrix maps:**

```text
S1 ∧ S2 ∧ S3 : achievable by fully named combinatorial/spectral instances
S4 (physical roof/side boundary) : NOT achievable from A alone
S1 ∧ S2 ∧ S3 ∧ S4 via f(A) only : NO
```

This is the load-bearing negative for “matrix-only localizer maps”.

---

## 4. Order-enriched maps: domain must be the poset, not only `A`

S4 can only be attempted if the domain includes order operations beyond a single static `A`, still order-only, still parameter-free. The natural enrichment already listed in Decision 040 is **maximal peeling**.

### 4.1 Existence sketch (not a freeze, not a candidate)

Fix, entirely in advance:

```text
A(C)_ij := |J⁺_C(i) ∩ J⁺_C(j)|          # named overlap, no free norm
peel(C)  := C \ Max(C)                   # one fixed maximal layer removal
Π(A)     := equitable-refinement partition of rows of A
```

Map `Φ(C)`:

1. If `|M| < 4` or `A` non-symmetric/nonfinite → `TOO_FEW_OR_BAD_MATRIX_ABSTAIN`.
2. Let `P = Π(A(C))`. If `P` is one cell, or all singletons, or any cell size `< 2` → `TRIVIAL_OR_OVERREFINED_ABSTAIN`.
3. Let `C' = peel(C)`. Recompute `A' = A(C')` on the **same** index set `M = Min(C)` (minimals are unchanged by removing maximals in a finite poset with at least one non-minimal). If `Min(C') ≠ M`, apply a fixed rule: abstain `MINIMALS_CHANGED_ABSTAIN` (should not occur under standard finite poset peel of only maximals when non-minimals exist; if the poset is only minimals, peel empties structure → abstain).
4. Let `P' = Π(A')`. If `P ≠ P'` as partitions of `M` → `ROOF_UNSTABLE_ABSTAIN` (built-in top-boundary control).
5. If the automorphism group of `A(C)` permutes two or more cells of `P` nontrivially so that no conjugacy-closed single block is defined — **and** the design asks for a single block rather than the full partition — → `AUTOMORPHISM_AMBIGUITY_ABSTAIN`. If the design emits the **full unordered partition** `P`, this step is vacuous.
6. Else emit `P` (unordered partition of minimals).

Properties:

| Criterion | Status for this sketch |
|---|---|
| Order-only | Yes: only `≺`, `Min`, `Max`, set cardinalities of futures. |
| No calibrable threshold | Yes: all constants discrete and fixed; no free cut height. |
| Deterministic + relabel-invariant | Yes if partitions are unordered and no label-order ties. |
| S1 | Yes **when it emits**: multi-cell, no singletons. May abstain often. |
| S2 | Yes if output is the full partition; fails again if one later demands a single “winning” cell without a closed rule. |
| S3 | Yes with the named abstentions above. |
| S4 (symmetry) | Yes for total symmetry / automorphic cell swap if designed as abstention or full-partition emission. |
| S4 (roof) | **Partial, built-in:** instability under one maximal peel is inside the map, not an external test suite. |
| S4 (side wall / density / MINK) | **Not solved** by one top-peel. Lateral and flat-same-cloud controls need other order-only duals or remain external falsifiers. |

So even the enriched sketch does **not** claim full Decision-040 boundary suite as internal control. It only shows:

```text
S1 ∧ S2 ∧ S3 ∧ S4_roof-stability  can exist as a fully named order-only map
S4_full-boundary-suite            is not obtained for free
```

### 4.2 Matching / peel subtlety (honest limit)

Decision 040 already noted that peeling-as-primary object fails without a matching rule. The sketch above **avoids matching deleted elements** by:

- indexing always on the original minimal set `M`;
- comparing two partitions of the **same** `M` from `A(C)` and `A(peel(C))`.

That is closed. It does not claim that peel stability equals “horizon”. It only encodes “do not emit structure that dies when the roof layer is removed”.

---

## 5. Direct answers

### Does an order-only map without calibrable threshold exist?

**Yes.** Many do (row equality, equitable refinement, named Laplacian sign bipartition, max-weight support components, and peel-stable variants).

### Does one exist that emits a nontrivial block/partition with closed ties and degeneracy abstention?

**Yes**, if:

- the output is allowed to be an **unordered partition** (not a single preferred cell), and  
- all ties/multiplicities/zeros abstain, and  
- discrete emission floors are fixed in the definition.

### Does one exist as a pure function of the common-future matrix alone with full S4 boundary control?

**No.** Pure `f(A)` cannot implement physical roof/side discrimination when distinct mechanisms share `A` (indistinguishability). S4 forces the domain to be the **poset** (or a peel sequence), not `A` alone.

### Does a peel-enriched, fully named map exist that hits S1–S3 and built-in roof stability?

**Yes, as a definitional sketch** (§4.1). It is not frozen, not implemented, and not shown to be horizon-sensitive.

### Does any of this open `CANDIDATE_5`?

**No.**

```text
EXISTENCE_OF_SOME_ORDER_ONLY_THRESHOLD_FREE_MAP = YES
EXISTENCE_OF_PURE_MATRIX_MAP_WITH_FULL_S4 = NO
EXISTENCE_OF_CLOSED_HORIZON_LOCALIZER = UNRESOLVED / NOT CLAIMED
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
```

---

## 6. Relation to Decision 041

Decision 041 asked whether the **three unfinished families** simultaneously closed S1–S4. Answer: no.

This note asks whether **any completely named map** can exist under order-only + no free threshold. Answer: yes formally; no for pure-matrix full S4; peel-stable partition maps are the only natural place left if one continues C5 theoretically.

041’s negative terminal stands. This note does not reopen a surviving C5.1 family and does not replace 041 with `C5_1_MAP_SPACE_NARROWED`.

---

## 7. If work continues later (not authorized now)

The only intellectually honest next **conceptual** move, if ever authorized, is not “pick spectral vs equitable” as vibes, but:

1. Fix the domain as the **poset** (matrix + named peel or other order duals).  
2. Fix **one** named base partition rule (exact / equitable / named Laplacian).  
3. Fix emission = full unordered partition or a **closed** single-block rule.  
4. Build S4 pieces that are internal (peel, and any other order-only duals that can be named without thresholds).  
5. Only then ask whether physics could care — still without seeds.

Until that full naming is written and authorized, the operational posture remains:

```text
C5_MAP_BOTTLENECK_REMAINS_OPEN_FOR_PHYSICS
FORMAL_THRESHOLD_FREE_MAPS_EXIST
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SEEDS
```

**Follow-up (same session):** a fully named instance is written in
`dev/C5_NAMED_MAP_PHI_STAR.md` as `Φ★` (exact row partition + one maximal peel). That instance is
formally closed for S1–S3 and roof-one-peel; it is still not `CANDIDATE_5` and does not claim
horizon physics.
