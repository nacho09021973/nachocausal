# C5.3 — Env(Φ★_L) falsifier and claim envelope (paper contract)

STATUS: PATH_A_CONTRACT_DRAFT / NOT_A_CANDIDATE / CANDIDATE_5_NOT_YET_OPENED  
NO_IMPLEMENTATION / NO_SYNTHETIC_EXECUTION / NO_SEEDS / NO_FREEZE / NO_RECONSTRUCTION_CLAIM  
DATE: 2026-07-20

BINDS_TO:

- Active map: `dev/C5_2B_PHI_STAR_L_SPECTRAL.md` (Φ★_L)
- Demoted: `dev/C5_NAMED_MAP_PHI_STAR.md` (exact-row Φ★; diagnostic only)
- Lateral doctrine: `dev/C5_LATERAL_ORDER_ONLY_DUAL.md`
- Non-collapse: `dev/C5_NONCOLLAPSE_A_VS_MARGINAL_V.md`
- Brittleness: `dev/C5_2_BRITTLENESS_EMISSION.md`
- Decision 040 §9 boundary falsifier list
- Claim grammar `docs/claim_grammar.md`

This document writes the **claim envelope** and **falsifier contracts** for any future physics use
of Φ★_L. It does **not** authorize synthetics, seeds, code, or `CANDIDATE_5`.

```text
Env(Φ★_L) := Φ★_L  +  generative / comparative controls below
```

Without Env, Φ★_L is only a formal map. With Env, a physical claim *shape* exists. Passing Env is
necessary for support testing later; it is never sufficient for horizon identification.

---

## 1. Claim shape admitted by Env (only)

```text
TARGET / OPEN:
In generative family G (to be frozen only if a candidate is ever opened), dimension d,
chart/box class X, density schedule ρ, channel order-only:
the emission law and emitted bipartitions of Φ★_L are not explained by
  (i) marginal volumes/ranks of minimals,
  (ii) roof-only truncation,
  (iii) side-wall-only truncation,
  (iv) density lobes,
  (v) flat same-cloud causality,
and any post-selection geometry (embedding-only scoring) is reported as diagnostic, not as
selection input.
This does not identify the global event horizon.
NO_RECONSTRUCTION_CLAIM.
```

Anything stronger (horizon recovery, metric reconstruction) is forbidden in this envelope.

---

## 2. Units and terminals

### 2.1 Per-poset output of Φ★_L

As in C5.2b: `EMIT({B₊,B₋})` or a named `ABSTAIN_*`.

### 2.2 Envelope-level comparative terminals (design outcomes)

Used when comparing a primary construction to a control construction:

```text
ENV_PASS_UNIT              # control does not reproduce the primary emission pattern
ENV_FAIL_MARGINAL          # control using only V (or L,V) matches primary pattern
ENV_FAIL_ROOF              # roof-only / peel-fail pattern dominates
ENV_FAIL_SIDE_WALL         # lateral-only construction matches primary
ENV_FAIL_DENSITY           # density lobe matches primary
ENV_FAIL_MINK_SAME_CLOUD   # flat same-cloud matches primary
ENV_FAIL_HEIGHT_TRACKING   # height-window shift only translates the pattern
ENV_FAIL_NO_EMISSION       # primary almost never emits in the design regime
ENV_INCONCLUSIVE           # insufficient structure to decide (declared in advance)
```

“Matches primary pattern” must be fixed **before** data. Default order-only notions:

```text
PATTERN_EQ:
  both abstain with the same abstention class, OR
  both emit bipartitions that coincide up to relabeling of the shared index set
  when the control is defined on the same M, OR
  a predeclared conjugacy when control rewrites labels.
```

No coordinate distance between blocks enters `PATTERN_EQ`.

---

## 3. Falsifier battery (paper contracts)

Each contract states: **construction**, **primary vs control**, **fail rule**, **pass rule**.  
No seed counts, no α, no effect floors — those appear only if a candidate is ever opened.

### F1 — Marginal redundancy (C-ens for Φ★_L)

**Construction (control map `Φ_V`).**  
Named, order-only, threshold-free sibling that uses only volumes:

```text
On M, let V(i) = A_ii.
If fewer than 2 distinct V values: ABSTAIN.
Else: bipartition by median split on V is FORBIDDEN (median is a data-dependent threshold).
Instead: exact equality classes of V:
  Π_V = M / (i~j iff V(i)=V(j))
  If Π_V is a bipartition (exactly two cells, both nonempty): emit that unordered pair.
  Else: ABSTAIN.
```

This is exact-value bipartition of volumes only — parallel to “exact” discipline, no free k-means.

**Fail:** On a predeclared synthetic or future generative battery, whenever Φ★_L emits, `Φ_V`
emits the same bipartition (PATTERN_EQ) except on a null set declared impossible by design.  
**Pass:** Exists design units with Φ★_L EMIT and not PATTERN_EQ to `Φ_V`, with same `{V(i)}` list
when required by the unit type (see F1b).

### F1b — Same margins, different overlaps (algebraic separation live)

**Construction:** Two finite posets (hand-built or later synthetic) with identical `(V(i))_{i∈M}`
up to relabeling, different `A`, such that Φ★_L emits different patterns or different
emit/abstain terminals.

**Fail:** No such pair exists in the finite class (would contradict C5 non-collapse lifted to
spectral maps — unexpected).  
**Pass:** At least one explicit pair is written in the design dossier (conceptual pairs allowed
without generator seeds).

**Discharged:** hand witness pair `C_bridge` vs `C_cross` in
`dev/C5_F1B_PHI_STAR_L_SEPARATOR.md` — same `V≡(5,5,5,5)`, peel-stable Φ★_L emits
`{{m1,m2},{m3,m4}}` vs `{{m1,m3},{m2,m4}}` with exact eigenvectors. **Status:** `F1B_PASS`.

### F2 — Roof domination

**Control:** Roof-only (or roof-heavy) poset / generative intervention where reconvergence is
created only by a shared maximal layer.

**Also internal:** Φ★_L already abstains on peel instability.

**Fail:** Primary emits on roof-only units with a “preferred” bipartition that the design would
call a detection.  
**Pass:** Roof-only units yield abstain or explicit `ENV_FAIL_ROOF` labeling; peel-stable emission
absent.

### F3 — Side wall domination (LAT-1, LAT-5)

**Control:** Symmetric lateral truncation only; pure spatial-wall posets (Decision 040 + lateral note).

**Fail:** PATTERN_EQ between wall-only control and primary “BH-like” emission.  
**Pass:** Wall-only does not reproduce primary emission pattern.

### F4 — MINK same-cloud (LAT-2)

**Control:** Same point cloud, Minkowski causality vs BH causality (program’s existing same-cloud
discipline where defined).

**Fail:** Φ★_L patterns PATTERN_EQ across BH and MINK on the same cloud as a rule.  
**Pass:** Systematic difference or systematic primary abstain on MINK with emission on BH (or
other predeclared asymmetric pattern) — still not a horizon claim.

### F5 — Density lobe (LAT-3)

**Control:** Inhomogeneous intensity, no horizon geometry.

**Fail:** Emission tracks the lobe under PATTERN_EQ with a density-only partition oracle if one is
named; or tracks lobe under embedding-only diagnostics in a way the design calls domination.  
**Pass:** No density-only reproduction of the primary pattern.

### F6 — Height / window tracking (LAT-4)

**Control:** Translate or thicken the temporal window / height domain.

**Fail:** Emitted bipartition only tracks the roof or wall in the new window.  
**Pass:** Peel-stable pattern not reducible to window translation.

### F7 — Relabeling

**Control:** Arbitrary permutations of element labels.

**Fail:** Any change of EMIT/ABSTAIN class or non-conjugate bipartition.  
**Pass:** Exact conjugacy always.

### F8 — Chronic non-emission in design regime

**Control:** None; primary only.

**Fail:** In the *eventual* working regime of G (when a candidate defines G), emission rate below a
**predeclared** floor — that floor is **not chosen here** (would be candidate-level). At Path A
paper stage, F8 is a **placeholder kill** that any future candidate must instantiate with a
frozen floor before seeds.  
**Pass:** Emission rate meets the frozen floor with the frozen G.

**Path A note:** C5.2 already killed exact-row Φ★ on theoretical F8-type grounds. Φ★_L is not
killed by F8 until G and a floor exist — but F8 remains mandatory in Env.

### F9 — Diagnostic exact-row Φ★ consistency (optional)

Run exact-row Φ★ as diagnostic.  
If exact-row ever emits a multi-block partition, compare coarsening to Φ★_L bipartition.  
Disagreement is not an automatic fail; it is logged.  
If exact-row always abstains while Φ★_L emits, that matches C5.2 expectations.

---

## 4. What is inside the map vs inside Env

| Piece | Location |
|---|---|
| `A`, `L=D−A`, simple `λ_2`, sign bipartition | Φ★_L |
| One maximal peel stability | Φ★_L |
| Multiplicity / zero / numerical abstain | Φ★_L |
| Side wall, MINK, density, height | **Env only** |
| Marginal oracle `Φ_V` | Env F1 |
| Seed bands, α, n_valid | **Not in Path A** — candidate-only |
| Embedding scores (`d_edge`, `r`, …) | Post-selection diagnostic only, never selection |

---

## 5. Ordering of any future work (still not authorized)

If a future authorization ever leaves paper:

```text
1. Hand / synthetic finite units for F1b, F2, F7  (no real-generator seeds)
2. Only if those pass: define G, freeze floors for F8, open candidate discussion
3. Never: implement Φ★_L and tune operator after seeing BH clouds
```

Path A **stops at paper contracts**. Steps 1–3 require new explicit authorization.

---

## 6. Kill criteria for the Φ★_L line (conceptual)

The line should be marked `C5_LINE_EXHAUSTED` (not merely “needs more seeds”) if any holds:

1. No finite F1b separator for Φ★_L can be exhibited after serious attempt (spectral collapse to `V`).
2. A proof that `sign(v_2(L(A)))` is a.s. a function of ranks of `V` under the intended G.
3. Principle requires internal S4_side and rejects generative Env (lateral note option B).
4. Every named arithmetic posture is judged non-executable without free numerical tolerances
   that effectively calibrate the cut (would require redesign).
5. Future candidate-level F8 fails after being honestly frozen (empirical — later world).

---

## 7. Terminal

```text
C5_3_RESULT = ENV_PHI_STAR_L_CONTRACT_WRITTEN
ACTIVE_MAP = PHI_STAR_L
DEMOTION = PHI_STAR_EXACT_ROW_DIAGNOSTIC_ONLY
S4_SIDE = GENERATIVE_IN_ENV
FALSIFIERS = F1_F1b_F2_F3_F4_F5_F6_F7_F8_F9
CANDIDATE_5_NOT_YET_OPENED
NO_IMPLEMENTATION
NO_SYNTHETIC_EXECUTION
NO_SEEDS
NO_FREEZE
NO_RECONSTRUCTION_CLAIM
```
