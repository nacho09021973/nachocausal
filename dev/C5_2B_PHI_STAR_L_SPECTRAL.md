# C5.2b — Named spectral successor Φ★_L (threshold-free)

STATUS: PATH_A_CONCEPT_DEFINITION / NOT_A_CANDIDATE / CANDIDATE_5_NOT_YET_OPENED  
NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS / NO_FREEZE / NO_RECONSTRUCTION_CLAIM  
DATE: 2026-07-20

BINDS_TO:

- `dev/C5_2_BRITTLENESS_EMISSION.md` (exact-row Φ★ ensemble-rejected)
- `dev/C5_NAMED_MAP_PHI_STAR.md` (primitives `A`, peel, floors)
- Decision 041 (spectral family incomplete then; this document **completes one instance**)
- `dev/C5_NONCOLLAPSE_A_VS_MARGINAL_V.md`
- `dev/C5_LATERAL_ORDER_ONLY_DUAL.md`

This document does **not** revive the incomplete “Family B” of Decision 041. It **names one
operator, one eigen-object, one emission rule, and the same peel wrapper**, so that S2 is no longer
vacuous.

```text
OBJECT = Φ★_L
NOT = CANDIDATE_5
NOT = freeze
NOT = implementation authorization
```

---

## 0. Motivation

Exact row equality dies under counting noise (C5.2). A bipartition read from the **geometry** of
the Gram-like matrix `A` can still be nontrivial when every row is unique: the sign pattern of a
Fiedler-type vector does not require any two rows to coincide.

Zero remains a canonical cut (not a free threshold). Multiplicity and zero components abstain.

---

## 1. Shared primitives with Φ★

Identical to `C5_NAMED_MAP_PHI_STAR.md` §2.1–2.2 and §2.4:

```text
M = Min(C),   m = |M|
A(C)_ij = | J⁺_C(i) ∩ J⁺_C(j) |     ∈ ℕ
peel(C) = C \ Max(C)
m_min = 4
```

No residualization, no kernel width, no row normalization of `A` before forming the operator
beyond what the named Laplacian itself does.

---

## 2. Named operator (every choice fixed)

### 2.1 Weighted graph reading

Interpret `A` as a symmetric nonnegative weight matrix on vertex set `M` (diagonal weights are
allowed as vertex strengths; they enter the degree).

```text
deg(i) := Σ_{j ∈ M} A_ij          # includes diagonal term A_ii = V(i)
D     := diag(deg(i))_{i ∈ M}
```

### 2.2 Combinatorial Laplacian (named)

```text
L(A) := D − A
```

Properties used:

- `L` is real symmetric, positive semidefinite on finite graphs with nonnegative weights.
- `L 1 = 0` when off-diagonal weights define a graph with no extra diagonal handling issues:
  careful note: with **nonzero diagonal in A**, the standard identity `L1 = 0` still holds because
  `(D1)_i = Σ_j A_ij` and `(A1)_i = Σ_j A_ij`. Yes: `L1 = 0` always for `L = D−A` with
  `D_ii = Σ_j A_ij`.
- Spectrum: `0 = λ_1 ≤ λ_2 ≤ ⋯ ≤ λ_m`.

### 2.3 Why this operator and not another

| Choice | Decision |
|---|---|
| `D−A` vs normalized `I−D^{-1/2}AD^{-1/2}` | **Unnormalized `D−A`**: avoids division by zero when `deg(i)=0`, stays rational/integer-friendly if `A` is integer |
| Adjacency-only spectral | Rejected: less standard connectivity semantics; Laplacian is the named default |
| Residualized `A` | Rejected: modeling choice (C5 non-collapse note §5) |
| “The” eigenspace of largest eigenvalue | Rejected: that tracks density concentration more than cuts |

This freezes Decision 041’s open item “which self-adjoint operator”.

---

## 3. Named eigen-object and bipartition

### 3.1 Selection rule

Let `0 = λ_1 ≤ λ_2 ≤ ⋯ ≤ λ_m` be eigenvalues of `L(A)` counted with multiplicity.

```text
IF λ_2 is not simple (λ_2 = λ_3, or geometric multiplicity > 1):
    ABSTAIN_SPECTRAL_MULTIPLICITY
ELSE:
    let v be an eigenvector for λ_2
    (any real eigenvector; sign flip handled below)
```

### 3.2 Sign partition

```text
Z(v) := { i ∈ M | v_i = 0 }
P₊(v) := { i ∈ M | v_i > 0 }
P₋(v) := { i ∈ M | v_i < 0 }
```

Emission requires:

```text
Z(v) = ∅
P₊(v) ≠ ∅
P₋(v) ≠ ∅
|P₊(v)| ≥ 1, |P₋(v)| ≥ 1   # automatic if both nonempty and no zeros
```

Optional discrete floor (same philosophy as Φ★, fixed once):

```text
block_min := 1     # bipartition allows size-1 blocks; see §3.3
```

**Output on success:** unordered bipartition

```text
P = { P₊(v), P₋(v) }
```

Sign flip `v ↦ −v` leaves `P` invariant.  
Relabeling: if `P_σ` permutes indices, `L` conjugates and `v` permutes; `P` conjugates.

### 3.3 Singleton blocks

Unlike exact-row Φ★, a spectral cut **may** isolate a single minimal. That is not “over-refined
equality noise”; it can be a real cut of the weight graph.

Path A choice (named, not calibrated):

```text
ALLOW_SINGLETON_BLOCKS = true
```

If both sides nonempty and `m ≥ m_min`, EMIT is allowed even if one side has size 1.  
Rationale: forbidding singletons would reintroduce a size floor that, for bipartitions, often forces
abstention without improving physics. The scientific object is the **cut**, not equal cluster sizes.

If a later design wants `block_min = 2`, that is a **different named map**, not a silent edit.

### 3.4 Arithmetic policy (definitional; not code)

Two admissible exactness postures (pick one for any future implementation; both are parameter-free):

```text
ARITH_EXACT:
  Treat L as rational/integer matrix; use exact rational nullspace / characteristic polynomial
  methods; compare components to 0 exactly.

ARITH_ABSTAIN_IF_AMBIGUOUS:
  Any floating implementation must abstain unless a certification protocol proves
  sign pattern uniquely (e.g. interval arithmetic separating components from 0 and
  λ_2 from λ_3). If not certified → ABSTAIN_NUMERICAL_UNCERTIFIED.
```

No “choose the nicer split after looking at coordinates”.

---

## 4. Definition of Φ★_L

### 4.1 Terminal alphabet

```text
EMIT(P)                              # unordered bipartition of M
ABSTAIN_TOO_FEW_MINIMALS             # m < m_min
ABSTAIN_EMPTY_OR_DEGENERATE_POSET
ABSTAIN_SPECTRAL_MULTIPLICITY        # λ_2 not simple
ABSTAIN_SPECTRAL_ZERO_COMPONENT      # some v_i = 0
ABSTAIN_SPECTRAL_ONE_SIGN            # all nonzero components same sign (should not occur if 1 ⟂ v
                                     # for connected-type weights; keep as safety)
ABSTAIN_PEEL_UNDEFINED
ABSTAIN_ROOF_UNSTABLE                # bipartition changes under peel
ABSTAIN_NUMERICAL_UNCERTIFIED        # only under ARITH_ABSTAIN_IF_AMBIGUOUS
```

### 4.2 Algorithm (definitional)

Input: finite poset `C`.

1. If empty / no minimals → `ABSTAIN_EMPTY_OR_DEGENERATE_POSET`.
2. If `m < m_min` → `ABSTAIN_TOO_FEW_MINIMALS`.
3. Build `A = A(C)`, `L = D−A`.
4. Compute `λ_2`, multiplicity; if not simple → `ABSTAIN_SPECTRAL_MULTIPLICITY`.
5. Take eigenvector `v` for `λ_2`; if any `v_i = 0` → `ABSTAIN_SPECTRAL_ZERO_COMPONENT`.
6. Build `P = {P₊, P₋}`; if either empty → `ABSTAIN_SPECTRAL_ONE_SIGN`.
7. `C' = peel(C)`; if peel undefined or `Min` changes → `ABSTAIN_PEEL_UNDEFINED`.
8. Repeat steps 3–6 on `C'` to get `P'`.
9. If `P' ≠ P` as unordered partitions of `M` → `ABSTAIN_ROOF_UNSTABLE`.
10. Else → `EMIT(P)`.

### 4.3 Relabeling

```text
Φ★_L(σ·C) = σ · Φ★_L(C)
```

---

## 5. Emission plausibility — why this is not dead like exact rows

### 5.1 Distinct rows are fine

Spectral bipartition never needs `row_i = row_j`. Generic full-rank perturbations of `A` still define
a cut when `λ_2` is simple and `v` has no zeros.

### 5.2 Continuum limit intuition — [PLAUSIBLE]

If `A/ρ → K` a continuum Gram / overlap kernel on a continuum “minimal” measure, `L` approaches a
continuum Laplacian-like operator on that measure class. Two-block structure appears when the
kernel has a dominant Fiedler mode (e.g. spatial bipartition of an initial antichain: left/right
of a box, or interior/horizon-adjacent sector — **geometry unknown**, but **emission** is
structurally possible).

### 5.3 Remaining emission threats

| Threat | Effect on Φ★_L |
|---|---|
| `λ_2` multiplicity (symmetry) | abstain — correct |
| Components near 0 (soft zeros) | exact arith OK; float must abstain if uncertified |
| Peel changes signs | roof-unstable abstain — correct |
| Always-connected kernel, tiny gap | may still emit; gap size is not a threshold we set |
| Cut always aligns with `V` ranks | **C-ens spectral** OPEN (non-collapse note analogue) |
| Cut always aligns with side walls | Env LAT suite (C5.3) |

```text
ENSEMBLE_EMISSION_PLAUSIBILITY = NONTRIVIAL   [unlike exact-row Φ★]
PHYSICS_CONTENT = OPEN
```

---

## 6. Checklist S1–S4 (Decision 041 criteria)

| Criterion | Φ★_L |
|---|---|
| Order-only | Yes |
| No free continuous threshold | Yes (`0` cut; fixed `m_min`) |
| Operator / eigenobject named | **Yes** (`L=D−A`, simple `λ_2`) |
| S1 nontrivial when emits | Yes (bipartition, both sides nonempty) |
| S2 closed ties | Yes: multiplicity → abstain; sign flip irrelevant; no label order |
| S3 degeneracy | Named terminals §4.1 |
| S4 symmetry | Highly symmetric `A` → multiplicity or balanced modes → often abstain |
| S4 roof | Peel stability internal |
| S4 side | **No** — still generative (`C5_LATERAL`) |
| Horizon | **OPEN / not claimed** |

Compared to Decision 041 Family B: the open operator/eigenvalue choices are **closed here**.  
Compared to exact-row Φ★: ensemble emission is **structurally plausible**.

---

## 7. Explicit non-claims

```text
NO_RECONSTRUCTION_CLAIM
NO_GLOBAL_HORIZON
NO_CANDIDATE_5
NO_PREREGISTRATION
NO_SEED_BAND
NO_IMPLEMENTATION_FROM_THIS_NOTE
```

Φ★_L is a **named concept map** on the C5 line after exact-row death. It is not frozen and not a
localizer claim.

---

## 8. Relation to exact-row Φ★

| | Φ★ (exact rows) | Φ★_L (Laplacian) |
|---|---|---|
| Formal closure | Yes | Yes |
| Ensemble emission | Rejected C5.2 | Plausible |
| Output shape | multi-block partition | bipartition only |
| Arithmetic | integer equality | spectral (exact or certified) |
| Role after Path A | diagnostic / symmetry oracle | **active C5 concept object** |

Exact-row Φ★ is **not deleted**; it is demoted to diagnostic. Φ★_L is the Path A continuation object.

---

## 9. Terminal

```text
C5_2B_RESULT = PHI_STAR_L_NAMED
OPERATOR = COMBINATORIAL_LAPLACIAN_D_MINUS_A
EIGENOBJECT = SIMPLE_LAMBDA_2_SIGN_BIPARTITION
PEEL = ONE_MAXIMAL_LAYER_STABILITY
ENSEMBLE_EMISSION = PLAUSIBLE_NOT_PROVED
PHYSICS = OPEN
NEXT = C5_3_ENV_FALSIFIER_CONTRACT
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SEEDS
```
