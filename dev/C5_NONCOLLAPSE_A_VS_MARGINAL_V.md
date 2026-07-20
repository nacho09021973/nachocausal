# C5 — Non-collapse of the common-future matrix against marginal future volumes

STATUS: THEORETICAL_ARGUMENT_ONLY / NOT_A_CANDIDATE / CANDIDATE_5_NOT_YET_OPENED  
NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS / NO_FREEZE / NO_RECONSTRUCTION_CLAIM  
DATE: 2026-07-20

BINDS_TO:

- `dev/C5_NAMED_MAP_PHI_STAR.md` (named map Φ★ uses raw `A`)
- `dev/C5_ORDER_ONLY_THRESHOLD_FREE_MAP_EXISTENCE.md`
- `dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md` §11 (finite non-redundancy toy)
- Decision 040–041
- Claim grammar teleology: finite order does not identify the global event horizon

This note answers option (1) from the C5 continuation fork:

> Is there a continuum / causal-set reason to expect that the raw common-future matrix  
> `A_ij = |J⁺(i) ∩ J⁺(j)|` on minimals is **not** a function of the marginal volumes  
> `{V(i) = |J⁺(i)| : i ∈ Min(C)}` (and related marginals),  
> so that Φ★ is not secretly a re-encoding of C3?

It does **not** prove that Φ★ detects anything physical. It only grades **non-marginality**.

---

## 0. Three collapse claims (must be separated)

Write `M = Min(C)`, `V(i) = |J⁺(i)|`, and `A_ij = |J⁺(i) ∩ J⁺(j)|`.

| ID | Collapse claim | Strength needed to kill Φ★ as non-marginal |
|---|---|---|
| **C-alg** | For every finite poset, `A` is a function of the list `(V(i))_{i∈M}` alone | If true, Φ★ is definitionally marginal. |
| **C-part** | For every finite poset, the row-partition `Π_row(A)` is a function of `(V(i))` alone | If true, Φ★’s emission is definitionally marginal even if raw `A` is not. |
| **C-ens** | On a design ensemble `E` (e.g. sprinklings of boxed Schwarzschild / Minkowski), `Π_row(A)` is a.s. equal to a fixed function of ranks/values of `V` | If true **on E**, Φ★ is empirically redundant with C3-type marginals on that ensemble, even if C-alg is false in general. |

Φ★ dies as a *joint* object only if C-alg or C-part holds in general, or if C-ens holds on the intended family.

**Results of this note:**

```text
C-alg : FALSE   [PROVED, finite combinatorial]
C-part: FALSE   [PROVED, finite combinatorial]
C-ens : OPEN    [not proved; not tested; no seeds]
```

Continuum Lorentzian geometry supplies a **reason to expect** C-ens false in bulk continuum limits, but boxed finite sprinklings of Schwarzschild remain `OPEN`.

---

## 1. What “determined by marginals” would mean

A map `F` from posets to matrices **collapses to volumes** if there exists a function `g` such that for all finite posets `C` in the class,

```text
A(C) = g( (V(i))_{i ∈ M} )
```

up to simultaneous relabeling of `M`. Equivalently: whenever two posets induce the same volume list on minimals (up to order-isomorphism of the index set), they induce the same overlap matrix.

Weaker collapse for Φ★: same hypothesis, but only

```text
Π_row(A(C)) = g_Π( (V(i))_{i ∈ M} ).
```

Even weaker (ensemble): equality in probability under a generative law.

---

## 2. Algebraic non-determination — [PROVED]

### 2.1 Set-theoretic core

Futures of minimals are subsets of the non-minimal set (or of `E \ M`). Write

```text
F_i := J⁺(i) ⊆ E \ M.
```

Then

```text
V(i) = |F_i|,
A_ij = |F_i ∩ F_j|.
```

**Fact (elementary).** The family of cardinalities `(|F_i|)_i` does not determine the family of pairwise intersections `(|F_i ∩ F_j|)_{i,j}`.

This is standard: intersection numbers are the off-diagonal entries of the Gram matrix of indicator vectors in `ℓ²(E \ M)`, while volumes are squared norms. Many configurations of vectors share norms and differ in angles.

### 2.2 C4 two-pair toy (repository anchor)

From `dev/PR003_C4_COMMON_FUTURE_CONVERGENCE_NOTES.md` §11, universe `{x,y,z,w}`:

```text
Pair A:  F_i = {x,y}, F_j = {x,y}   →  V=2,2  and  |F_i ∩ F_j| = 2
Pair B:  F_p = {x,y}, F_q = {z,w}   →  V=2,2  and  |F_p ∩ F_q| = 0
```

Same marginal volumes (and, with those four points maximal, same `L=1`), different overlaps.  
Hence **C-alg is false** already for a single off-diagonal entry.

### 2.3 Whole-matrix and row-partition lift — [PROVED]

The same idea lifts to a single finite poset with four minimals and controlled futures.

**Construction `C_sameV_diffA` (conceptual finite poset; not executed, not a seed).**

Elements:

```text
Minimals:  m1, m2, m3, m4
Bulk:      a, b, c, d     (all maximal; no further relations among bulk)
```

Relations (only minimal → bulk):

```text
m1 ≺ a, b
m2 ≺ a, b
m3 ≺ a, c
m4 ≺ b, d
```

Then every minimal has `V = 2`, and if each bulk point is maximal with no chains through them, every minimal has link-depth `L = 1`.

Overlap matrix on `(m1,m2,m3,m4)`:

```text
        m1  m2  m3  m4
m1       2   2   1   1
m2       2   2   1   1
m3       1   1   2   0
m4       1   1   0   2
```

Row of `m1` equals row of `m2`: `(2,2,1,1)` up to index order.  
Rows of `m3` and `m4` are each unique.

So

```text
Π_row = { {m1,m2}, {m3}, {m4} }
```

Now the second poset `C'_sameV_samePartitionShape` is not even needed for disproof of C-part. Compare instead to the **volume-only** candidate partition: the only partition deterministically readable from the constant list `V≡2` is the **trivial** one-cell partition (all volumes equal). But `Π_row` above is **not** one cell (and after Φ★’s singleton rule would abstain as overrefined — still, the raw partition is not a function of `V` alone, because `V` is constant while other same-`V` posets have different row partitions).

**Cleaner C-part counterexample:** two posets, same `V` vector up to relabeling, different `Π_row`.

Poset `P_close`:

```text
m1 ≺ a,b
m2 ≺ a,b
m3 ≺ c,d
m4 ≺ c,d
```

All `V=2`. Overlaps: `A_12=A_34=2`, cross pairs `0`. Rows:

```text
m1 ~ m2   (both see one twin with overlap 2 and two zeros)
m3 ~ m4
Π_row = { {m1,m2}, {m3,m4} }
```

Poset `P_cross` (same four minimals, same four bulk maximals, same all `V=2`):

```text
m1 ≺ a,b
m2 ≺ c,d
m3 ≺ a,c
m4 ≺ b,d
```

All pairwise intersections among distinct minimals can be arranged as `0` or `1` without repeating the twin pattern of `P_close`. Concretely:

```text
A_12=0, A_13=1, A_14=1,
A_23=1, A_24=1,
A_34=0
```

Rows of `m1` and `m2` both have signature “one 0 to the opposite, two 1’s” depending on labeling — one can check that under a suitable wiring all four rows are equal (complete multipartite pattern) or that the partition differs from `{{m1,m2},{m3,m4}}`.

A minimal fully checked wiring for **different partitions, identical V**:

```text
P_close as above:   Π_row = {{m1,m2},{m3,m4}}   (two blocks of size 2)
P_flat:
  m1 ≺ a,b
  m2 ≺ a,b
  m3 ≺ a,b
  m4 ≺ a,b
  Π_row = {{m1,m2,m3,m4}}   (one block)
  all V=2
```

Same volume list `(2,2,2,2)`, different row partitions (two twin cells vs one cell).  
**C-part is false.**

### 2.4 Corollary for Φ★

Because `Π_row` is not a function of `(V(i))` on the class of all finite posets, Φ★ is **not definitionally** a repackaging of C3’s volume ranks.

```text
DEFINITIONAL_MARGINAL_COLLAPSE_OF_PHI_STAR = FALSE  [PROVED]
```

This is the theorem-level content of the note. It does not mention Schwarzschild.

---

## 3. Continuum Lorentzian reason — [PLAUSIBLE / STANDARD GEOMETRY]

### 3.1 Continuum analogues

In a Lorentzian manifold with a finite observation region `R` (the “box”), for continuum points `p,q ∈ R`,

```text
V_cont(p)   ∼  vol( J⁺(p) ∩ R )
A_cont(p,q) ∼  vol( J⁺(p) ∩ J⁺(q) ∩ R )
```

For Poisson sprinklings at density `ρ`, the discrete counts concentrate around `ρ` times these volumes (law of large numbers in causal diamonds / regions of fixed continuum volume), with relative fluctuations `O(ρ^{-1/2})` in bulk regimes.

### 3.2 Why volumes do not fix overlaps in the continuum

Fix two pairs of points with the **same** individual future volumes inside `R` but **different** mutual separations.

Classic Minkowski intuition (any dimension `d≥1+1`):

- Future volume of a point inside a fixed box depends primarily on **proper time to the future boundary** (and local geometry).
- Common future volume of a pair depends on **both** their times-to-boundary **and** their spacelike separation (and relative placement): closer spacelike pairs share larger common futures, all else equal.

So one can hold `V_cont(p)=V_cont(q)=V_cont(p')=V_cont(q')` while

```text
vol(J⁺(p)∩J⁺(q)∩R)  ≠  vol(J⁺(p')∩J⁺(q')∩R).
```

This is the continuum shadow of §2. It is standard causal geometry, not a new theorem of this repository. Label: `[PLAUSIBLE-TRANSFER]` from continuum Lorentzian reasoning to high-density sprinklings in regions where continuum volumes are good predictors of counts.

### 3.3 Schwarzschild / boxed chart — what changes, what does not

In a finite chart of Schwarzschild (or `SQUARE_BOX`-type BH embeddings used in the program):

- **Near the horizon / singularity truncation:** future volumes and depths of points become strongly position-dependent (C3 physics). That drives **marginal** signals.
- **Joint overlaps** still carry an extra dependence on **relative** placement of pairs: two minimals with the same future volume can sit at similar “depth” but different angular / spacelike separation, or on different sides of a geometric feature, and then share different common futures inside the box.

So the continuum argument for non-determination of `A_cont` by `{V_cont}` **does not rely on asymptotic flatness** and **does not require** identifying the global horizon. It only needs that the map

```text
(p,q) ↦ vol(J⁺(p)∩J⁺(q)∩R)
```

is not a function of `(vol(J⁺(p)∩R), vol(J⁺(q)∩R))` alone on the chart. That fails as soon as the chart has a spacelike direction of nontrivial width — which every 1+1 or higher boxed region used in the program has.

**Caveat [OPEN]:** near walls and in very thin boxes, times-to-boundary can dominate so hard that overlaps become nearly monotone in volumes. That would push **C-ens** toward true even though C-alg is false. Edge-dominated C3 behavior is a warning that the ensemble may live in that regime.

---

## 4. What would still make Φ★ “effectively marginal” on an ensemble

Even with C-alg and C-part false, Φ★ can fail non-marginality **in practice** on ensemble `E` if any of the following holds.

### 4.1 Almost-sure over-refinement

If for sprinklings in `E`, all rows of `A` are a.s. distinct, then

```text
Π_row = all singletons  a.s.  →  Φ★ always ABSTAIN_OVERREFINED.
```

Then Φ★ never emits. It is non-marginal as a formal object but **empty as a signal**.  
Probability of exact integer row equality decays as counts grow unless a symmetry forces equality. In generic Poisson noise, **exact** row equality is rare for large `ρ`.

This is a structural tension inside Φ★:

```text
exact row equality  ⇒  brittle under Poisson fluctuations
threshold-free      ⇒  no ε-tolerance to restore blocks
```

So the same rigidity that closed S2 may force chronic abstention on manifoldlike sprinklings. That does not revive C-alg; it is a different death mode:

```text
DEATH_MODE_ALWAYS_ABSTAIN  (possible)
≠ DEATH_MODE_MARGINAL_COLLAPSE (ruled out definitionally)
```

### 4.2 Partition equal to a volume discretization

If on `E` one has with high probability

```text
Π_row(A) = Π_bins(V)
```

for some fixed binning of volumes (including “all equal V → one cell”), then emissions, when they occur, carry no joint information.  
**C-ens** would be true. **Status: OPEN** (needs generative analysis or authorized synthetics — neither done here).

### 4.3 Monotone coupling through the box

If the box geometry forces a near-deterministic coupling

```text
large V(i), V(j)  ⇒  large A_ij
```

with small residual scatter, then eigenvectors / rows of `A` align with ranks of `V`. Exact row classes may still differ from volume classes, but any stable coarse structure could be volume-driven.  
Again **OPEN** on Schwarzschild box ensembles; **PLAUSIBLE threat** near a single dominating roof.

---

## 5. Residualization remark (why Φ★ deliberately stays raw)

C4 considered hypergeometric residuals of overlaps given margins. That is the classical way to **partial out** `V`. Φ★ **does not** residualize:

- residualization needs a model of the ambient universe set and a null for random subsets;
- that model is an extra choice (not forced by the order alone);
- Decision 041-style closure preferred zero free modeling choices.

Consequence:

```text
Φ★ non-marginality is only "A is not a function of V" [PROVED in general],
not "A is independent of V" [false — intersections and volumes are coupled],
not "Π_row is independent of V on ensemble E" [OPEN].
```

Dependence is expected and harmless. **Functional determination** is what would kill the joint claim. That is what §2 refutes in general.

---

## 6. Schwarzschild-specific proposition (only admissible shape)

Following claim grammar, the only honest continuum/causet proposition is:

```text
TARGET / OPEN:
In generative family G = (sprinklings of a fixed finite chart class X of
Schwarzschild vs Minkowski, dimension d, box/patch P, density schedule ρ),
the law of Π_row(A) is not equal to the law of any fixed function of the
minimal volume list (V(i))_{i∈M} (or its ranks),
and Φ★ emission events are not a.s. identical to emission events of that
volume function.
This does not identify the global event horizon.
NO_RECONSTRUCTION_CLAIM.
```

**Status of that proposition:** `OPEN`.  
**What this note contributes:** it is not blocked by a general algebraic identity; C-alg and C-part cannot kill it a priori.

---

## 7. Hierarchical summary

```text
[PROVED]
  A is not a function of (V(i)) on finite posets.
  Π_row(A) is not a function of (V(i)) on finite posets.
  Therefore Φ★ is not definitionally C3-in-disguise.

[PLAUSIBLE-TRANSFER]
  In continuum Lorentzian regions with spacelike width, common-future volumes
  are not functions of individual future volumes alone; high-ρ sprinklings
  inherit this at leading order away from extreme wall regimes.

[OPEN]
  On the program's boxed Schwarzschild / MINK ensembles:
    - whether C-ens holds;
    - whether Φ★ almost always abstains (exact-row brittleness);
    - whether residual joint information, if any, is wall/density dominated;
    - whether any of this tracks a quasi-local horizon proxy.

[NOT CLAIMED]
  Horizon detection, metric recovery, quantum-gravity theorem.
```

---

## 8. Implications for the program

1. **Keep Φ★ on the table as a joint formal object.** The definitional collapse objection is answered.
2. **Do not confuse that answer with physics.** The sharp threat shifts from “is it just V?” to “does it ever emit?” and “when it emits, is it the box?”
3. **Exact row equality may be the wrong base partition for manifoldlike noise** even though it is the right base for closure. Equitable refinement and named spectral bipartition face related robustness issues; ε-tolerances reintroduce thresholds and are forbidden in the present discipline.
4. **C-ens is the next theoretical/synthetic battleground**, not more abstract existence.
5. Still:

```text
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
NO_FREEZE
NO_RECONSTRUCTION_CLAIM
```

---

## 9. One-sentence verdict

**Marginal volumes do not algebraically determine common-future overlaps or their exact row-partition — so Φ★ is not secretly C3 — but whether that extra joint information survives Poisson noise, finite boxes, and Schwarzschild charts as a non-abstaining, non-wall signal remains open and is now the real question.**
