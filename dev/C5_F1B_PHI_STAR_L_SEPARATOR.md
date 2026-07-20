# C5 F1b — Hand separator for Φ★_L (same V, different emission)

STATUS: F1B_DISCHARGED_PASS / NOT_A_CANDIDATE / CANDIDATE_5_NOT_YET_OPENED  
NO_GENERATOR_SEEDS / NO_PROJECT_SYNTHETIC_SUITE / NO_IMPLEMENTATION / NO_FREEZE  
DATE: 2026-07-20

BINDS_TO:

- `dev/C5_2B_PHI_STAR_L_SPECTRAL.md` (Φ★_L definition)
- `dev/C5_3_ENV_FALSIFIER_CONTRACT.md` §F1b
- `dev/C5_NONCOLLAPSE_A_VS_MARGINAL_V.md` (C-alg/C-part; this lifts to spectral emission)
- Path A terminal `dev/C5_PATH_A_LINE_TERMINAL.md`

## 0. Verdict

```text
F1B_RESULT = PASS
WITNESS_PAIR = (C_bridge, C_cross)
SAME_MARGINAL_V = (5,5,5,5) on Min
PHI_STAR_L(C_bridge) = EMIT {{m1,m2},{m3,m4}}
PHI_STAR_L(C_cross)  = EMIT {{m1,m3},{m2,m4}}
PEEL_STABLE = YES on both
PHI_V_ORACLE = ABSTAIN on both (all V equal ⇒ not a 2-cell volume partition)
CANDIDATE_5_NOT_YET_OPENED
```

This discharges Env F1b at the **hand finite-poset** level. It is not physics, not an ensemble
result, and not a candidate opening.

---

## 1. What was required

From C5.3 F1b:

> Two finite posets with identical `(V(i))_{i∈M}` up to relabeling, different `A`, such that Φ★_L
> emits different patterns or different emit/abstain terminals.

Φ★_L = spectral sign bipartition of `L = D−A` (simple `λ_2`) **and** stability under one maximal peel.

---

## 2. Witness posets

### 2.1 Common skeleton

Both posets have:

```text
Minimals:  m1, m2, m3, m4
Mid layer: finite bulk elements (constructed below), none maximal
Roof:      single global maximal r
Relations: each mi ≺ every element of its mid-future set Fi
           every mid element ≺ r
           no other relations
```

After `peel = delete Max = {r}`, the induced futures on mid sets are exactly the `Fi`, and
`Min` is unchanged.

### 2.2 Mid future sets — bridge witness `C_bridge`

```text
F1 = {a, b, c, x}
F2 = {a, b, c, y}
F3 = {x, p, q, r_mid}      # r_mid is a mid label, not the roof
F4 = {y, p, q, r_mid}
```

(Rename `r_mid` → `z` in plain text: `F3={x,p,q,z}`, `F4={y,p,q,z}`.)

Mid overlap matrix `A'` (`A'_ij = |Fi ∩ Fj|`):

```text
A' = | 4  3  1  0 |
     | 3  4  0  1 |
     | 1  0  4  3 |
     | 0  1  3  4 |
```

All diagonal `V' = 4`.

### 2.3 Mid future sets — cross witness `C_cross`

```text
G1 = {a, b, c, x}
G2 = {x, p, q, z}
G3 = {a, b, c, y}
G4 = {y, p, q, z}
```

```text
A'_cross = | 4  1  3  0 |
           | 1  4  0  3 |
           | 3  0  4  1 |
           | 0  3  1  4 |
```

All diagonal `V' = 4` again.

### 2.4 Full matrix before peel (add global roof `r`)

Every minimal sees `r`, so

```text
A = A' + J
```

where `J` is the `4×4` all-ones matrix. Explicitly:

**Bridge `A_bridge`:**

```text
| 5  4  2  1 |
| 4  5  1  2 |
| 2  1  5  4 |
| 1  2  4  5 |
```

**Cross `A_cross`:**

```text
| 5  2  4  1 |
| 2  5  1  4 |
| 4  1  5  2 |
| 1  4  2  5 |
```

Marginal volumes on minimals:

```text
V ≡ (5,5,5,5)   on both witnesses.
```

So `{V(i)}` is identical. The matrices `A` differ. The volume oracle `Φ_V` of C5.3 F1
(exact equality classes of `V`) sees a single cell → **abstains** on both.

---

## 3. Spectral computation (exact algebra)

### 3.1 Bridge after peel (`A'`)

```text
deg' ≡ 8,    L' = 8I − A' =
|  4  -3  -1   0 |
| -3   4   0  -1 |
| -1   0   4  -3 |
|  0  -1  -3   4 |
```

Test vector `v = (1,1,−1,−1)^T`:

```text
L' v = 2 v.
```

So `λ = 2` is an eigenvalue with this eigenvector (no zero components, both signs).  
Independent check: `L' 1 = 0`, so `λ_1 = 0` simple in this connected weight pattern; numerical
Jacobi spectrum of `L'` is `{0, 2, 6, 8}` (simple `λ_2 = 2`).

**Sign bipartition:**

```text
P_bridge = { {m1, m2}, {m3, m4} }
```

### 3.2 Bridge before peel (`A = A' + J`)

```text
deg ≡ 12,   L = 12I − A = L' + 4I − J.
```

Same `v = (1,1,−1,−1)^T` is orthogonal to `1`, and

```text
L v = L' v + 4 v − 0 = 6 v.
```

Jacobi spectrum `{0, 6, 10, 12}`; simple `λ_2 = 6`; **same sign bipartition** `P_bridge`.

**Peel stability:** `P(A) = P(A')` ⇒ not `ABSTAIN_ROOF_UNSTABLE`.

```text
Φ★_L(C_bridge) = EMIT {{m1,m2},{m3,m4}}
```

### 3.3 Cross after peel (`A'_cross`)

```text
L'_cross =
|  4  -1  -3   0 |
| -1   4   0  -3 |
| -3   0   4  -1 |
|  0  -3  -1   4 |
```

Test vector `w = (1,−1,1,−1)^T`:

```text
L'_cross w = 2 w.
```

Spectrum `{0, 2, 6, 8}`; simple `λ_2 = 2`.

**Sign bipartition:**

```text
P_cross = { {m1, m3}, {m2, m4} }
```

### 3.4 Cross before peel

Same argument: `L_cross w = 6 w`, same signs, peel-stable.

```text
Φ★_L(C_cross) = EMIT {{m1,m3},{m2,m4}}
```

### 3.5 Separation

```text
P_bridge ≠ P_cross
```

as unordered bipartitions of the same label set `{m1,m2,m3,m4}`.  
Therefore F1b **PASS**.

---

## 4. Relabeling check (spot)

Any simultaneous permutation `σ` of minimals conjugates both `A` and the bipartition. The pair
remains a separator after relabeling: the two emitted partitions stay non-conjugate **to each
other** as combinatorial bipartitions of a fixed labeled set; under a global relabeling applied to
both posets, conjugacy preserves inequality.

---

## 5. What this does and does not prove

| Claim | Status |
|---|---|
| Φ★_L is not a function of `(V(i))` alone on finite posets | **PROVED** by witness pair |
| Spectral emission can be peel-stable and still non-marginal | **PROVED** on this pair |
| Exact-row Φ★ would separate these | Likely abstain (generic distinct rows); irrelevant |
| Ensemble C-ens on sprinklings | Still **OPEN** |
| Horizon / box physics | **Not claimed** |
| Numerical float path without certification | Not used for the exact `v,w` eigenvectors above |

Arithmetic note: the load-bearing eigenvectors and eigenvalues used for EMIT are **exact** rational
(`λ∈{2,6}`, components `±1`). Jacobi floats were only used as a search tool to find candidates;
the witness proof does not depend on them.

---

## 6. Method footprint (discipline)

```text
USED:
  - hand-built finite posets
  - integer set systems for mid futures
  - exact matrix–vector checks for L v = λ v
  - pure-Python Jacobi only as a discovery aid

NOT USED:
  - nachocausal generator
  - BH/MINK seeds
  - evaluation bands
  - project synthetic suite runner
  - coordinates / embeddings
```

---

## 7. Terminal

```text
C5_F1B = PASS
WITNESS = C_bridge_vs_C_cross
SAME_V = (5,5,5,5)
EMIT_BRIDGE = {{m1,m2},{m3,m4}}
EMIT_CROSS  = {{m1,m3},{m2,m4}}
PEEL_STABLE = YES
MARGINAL_ORACLE_PHI_V = ABSTAIN_BOTH
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SEEDS
NO_RECONSTRUCTION_CLAIM
NEXT_MENU = F1-F7_SYNTHETIC_SUITE_OR_STOP_OR_C6
```
