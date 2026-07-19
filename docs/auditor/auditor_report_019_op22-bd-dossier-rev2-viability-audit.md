# Auditor Report 019 — op22-bd-dossier-rev2-viability-audit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Independent re-derivation audit of `dev/OP22_BD_VIABILITY_DOSSIER.md` (rev. 2) at HEAD
`475cb93` on `main`, requested by the PI before the dossier returns to `/comite`. Expected state
verified:

- HEAD is `475cb93d501bafbf2506328a44df9733739fba24` (`git rev-parse HEAD`). ✓
- Tracked tree clean; **two pre-existing untracked files present**
  (`nachocausal-program.local-before-pull.html`, `pr009-runner-scorer-v2.patch`), unrelated to
  the dossier — the literal claim "clean tree" is therefore only true for tracked content
  (finding W3). ✓ with caveat
- `e5f2961` = decision 036 + matrix §6 amendment + work_packages README re-sync (3 files). ✓
- `f57b13e` = dossier v1 (`dev/OP22_BD_VIABILITY_DOSSIER.md`, 189 insertions). ✓
- `475cb93` = dossier rev. 2 (same file only). ✓
- No Candidate B opening, no preregistration, no OP-2.2 terminal anywhere in the three commits
  (checked §6 below). ✓

Constraints honored: no enumeration, no `run_bench`, no Monte Carlo, no scoring, no seed draw;
only in-memory arithmetic (stdlib `math`, printed to stdout, no artifacts written); no file
modified except this report.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh` — exit code 0. Verbatim findings (header + tail):

```text
Auditor — auditing: /home/adnac/nachocausal
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/... (18 reports),
      docs/comite/... (53 decisions), docs/hoja_de_ruta_*, docs/prereg002_*, docs/preregistration_00{2,3}*,
      docs/rvar_closure_negative_result.md
WARN: committed data file with no generator reference: data/reports/kbeam_braiding_diagnostic_per_survivor.csv
WARN: committed data file with no generator reference: data/reports/pr004_braiding_v2_per_lineage.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K16.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K2.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K32.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K4.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K64.csv
WARN: committed data file with no generator reference: data/reports/pr005_k_stability_heldout_K8.csv
WARN: committed data file with no generator reference: data/reports/pr005_population_depth_barrier_slices.csv
WARN: committed data file with no generator reference: data/reports/pr005_population_depth_barrier_slices_heldout.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n4.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n4.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n5.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n5.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n6.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n6.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n7.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n7.sha256
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.csv
WARN: committed data file with no generator reference: data/reports/pr011_tv_certification_n8.sha256
WARN: committed data file with no generator reference: data/reports/present_anchor_clean_v3_kill_test.csv
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
----------------------------------------
Auditor: 0 error(s), 22 warning(s)
```

All 22 warnings are the standing repo-wide data-file warnings already carried (with identical
content) by reports 017/018; none is introduced by, or specific to, the audited commits.

## 3. Seal & freeze integrity

- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
  Matches the recorded SHA per the mechanical audit's seal check (recorded across the freeze
  docs listed verbatim in §2). No drift.
- The three audited commits touch only `docs/comite/`, `research_program/work_packages/`
  (matrix + README text), and `dev/OP22_BD_VIABILITY_DOSSIER.md` — no seal, no threshold, no
  frozen prereg text modified (`git show --stat e5f2961 f57b13e 475cb93`).

## 4. Reproducibility of published numbers

Every number in the dossier was re-derived independently from frozen sources. Result per gate:

### V1 — BD formula and convention: CONFIRMED

- Primary source check: `S^(2)[C]/ħ = N − 2N₁ + 4N₂ − 2N₃`, with `N_i` = number of
  **(i+1)-element inclusive order intervals**, confirmed verbatim at
  `biblioteca/derived-md/Benincasa_Dowker_2010_Scalar_Curvature_Causal_Set_arXiv1001.2725.md:117`
  (Eq. 13) and `:123` (interval definition), and independently at
  `biblioteca/derived-md/Bhatnagar_2021_Causal_Set_Theory_and_Benincasa_Dowker_Conjecture.md:519,523`
  (Eq. 3.11). BD2010 states the 2D form "up to factors of order one" with an `ħ` prefactor
  (`…:115-117`); the dossier's treatment (drop dimensionful prefactors as an affine
  reparametrization absorbed by the `[0,1]` map, stated explicitly) is faithful and declared,
  not hidden (dossier:52-55).
- The dossier correctly separates (a) formula/convention — claimed PASS; (b) the `[S_min,S_max]`
  normalization *rule* (no clipping, exact theoretical range) — claimed PASS; (c) the numeric
  endpoints — explicitly excluded from the PASS and deferred to a not-yet-authorized enumeration
  (dossier:37-39, 56-64). No clipping and no free tuning parameter anywhere in the frozen text;
  matches decision 035 §9 binding rule ("enumerated theoretical range; no clipping").
- Hand sanity values re-derived: 4-chain `S = 4 − 2·3 + 4·2 − 2·1 = 4` ✓; 4-antichain `S = 4` ✓.

### V2-global — counterexample pair: CONFIRMED

Independent recount (this auditor, from the cover relations written in the dossier):

- P1 (diamond): transitive closure gives relations `(a,b),(a,c),(a,d),(b,d),(c,d)` →
  `|relations| = 5`. Intervals: `[a,b]`, `[a,c]`, `[b,d]`, `[c,d]` all 2-element (b∥c);
  `[a,d] = {a,b,c,d}` 4-element. `N1=4, N2=0, N3=1` → `S = 4 − 8 + 0 − 2 = −6`. ✓
- P2 (Y): relations `(a,b),(d,b),(b,c),(a,c),(d,c)` → `|relations| = 5`. Intervals: `[a,b]`,
  `[d,b]`, `[b,c]` 2-element; `[a,c] = {a,b,c}`, `[d,c] = {d,b,c}` 3-element (a∥d). `N1=3,
  N2=2, N3=0` → `S = 4 − 6 + 8 − 0 = +6`. ✓
- Identity `Σ_{m≥1} N_m = |relations|`: P1 `4+0+1=5` ✓, P2 `3+2+0=5` ✓.
- Conclusion re-affirmed: same `n`, same `|relations|`, `S` differs ⇒ `S` is not a function of
  `|relations|` on 4-element posets; a fortiori not an affine/monotone reparametrization of the
  barred `f_bench = |relations|/6` (`dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md:130-131`).

### V2-support — analytic attempt by inspection of the frozen construction: UNRESOLVED (one identified premise short of PASS)

Inspection only — nothing executed. The frozen law construction
(`dev/pr011_tv_certification_enumeration.py`) is:

1. `poset_signature_from_permutation` (`:141-146`): the support consists exactly of
   **permutation-pattern (2-dimensional) posets** — `(i,j)` related iff `i<j` in x-order and
   `σ_i < σ_j` in y-order.
2. Both counterexample posets are permutation-realizable (hand check, this audit): P1 (diamond)
   = pattern `σ = (1,3,2,4)`; P2 (Y) = pattern `σ = (2,1,3,4)`. So both lie in the support
   **iff** their permutation classes receive strictly positive mass.
3. `permutation_mass` (`:148-162`) sums `C(grid_m, n)²` products of grid values times a positive
   cell factor; `poset_law_from_grid` (`:164-176`) accumulates per pattern; `normalize_law`
   (`:190-197`) divides by a positive total. Hence: **if every grid entry is strictly positive,
   every permutation pattern — including P1 and P2 — has strictly positive mass under every τ.**
4. Grid entries are `copula_density` midpoint evaluations
   (`research_program/work_packages/wp4_kappa_numeric_reference.py:98-104`):
   `c = A·h/(m1(U)·m2(v))` with `h = e^{v/2t}/W′(t,r)`, `W′(t,r) = r·e^{r/t}/t² > 0` on the
   brentq bracket `r ∈ (10⁻¹⁰, 60)` (`wp4:60-62,69-71`). Numerator and `A` strictly positive by
   closed form; the sign precondition `Up < 0 < Uq` holds by hand arithmetic at the frozen
   constants (`R_P,V_P = 2,0; R_Q,V_Q = 0.5,1`, enumeration `:41-44`): `2/τ > 1 > 0.5/τ` for
   both τ ∈ {0.95, 1.05}, so `W(t,r_p) > 0 > W(t,r_q)`, matching the assert at `wp4:74-75`.
   Existence/uniqueness of the brentq root follows from strict monotonicity of `Ũ` in `r`
   (`W′ > 0`).
5. **The single remaining premise** — strict positivity of the PCHIP-interpolated marginals
   `m1(U)`, `m2(v)` (and in-domain evaluation via `Finv`, `Ginv`) — is a property of scipy's
   `PchipInterpolator` (Fritsch–Carlson monotone-per-subinterval, no overshoot: on each
   subinterval the interpolant stays between the two endpoint data values, all of which are
   strictly positive trapezoid sums of positive integrands, `wp4:76-92`). This property is
   documented upstream but **written nowhere in this repository**, and the evaluation is
   floating-point, not exact arithmetic.

Per the PI's gate rule ("if the proof requires unwritten assumptions about realizability,
positive density or geometric domain, keep UNRESOLVED"), V2-support therefore **remains
`UNRESOLVED`** — but the audit reduces the open question to exactly that one citable premise.

**Quantifier specification (required by the audit charge).** For the counterexample to bind on
the relevant domain, P1 and P2 must both receive strictly positive mass in
`supp(P_4(0.95)) ∪ supp(P_4(1.05))` computed at the frozen parameters `n = 4`, `grid_m = 12`
(the CELL-PR011 laws, `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` §4.2; `grid_m ≥ n`
required by `poset_law_from_grid:167-169`). The union suffices for "S does not collapse to a
function of `|relations|` on the relevant domain." The inspection argument above, if the PCHIP
premise is accepted, delivers the strictly stronger conclusion: positive mass under **every**
τ — i.e. membership in the **intersection** of the two supports — for every `grid_m ≥ 4`.

**Caveat either way:** even a successful analytic support proof would NOT discharge decision 035
§9's binding rule that non-collinearity with `f_bench` "must be proved by **enumeration** on the
frozen n=4 family before freeze, not asserted" — the enumerative falsifier remains mandatory
pre-freeze regardless of how V2-support is resolved on paper.

### V3 — budget: formula CONFIRMED; the tabulated instantiation is MIS-ANCHORED (error E1)

- Frozen contract re-derived: radii `r = sqrt(log(4/α_j)/(2m))` and
  `TV_lower = max(0, |μ̂_P − μ̂_Q| − r_P − r_Q − ε_P − ε_Q)` confirmed at
  `research_program/work_packages/op13_positive_evidence_protocol.md:59-62,68-76` and
  `certifier/bench.py:97-98,120`. With `ε = 0`, `m_P = m_Q = m`, `BOUND_POSITIVE` attainable at
  expected means requires `2·sqrt(ln(4/α_j)/(2m)) < g`, i.e. `m > 2·ln(4/α_j)/g²` — the
  dossier's algebra (dossier:143-150) is **correct**, as is its ~3.8× correction of the PI's
  1/√m scaling heuristic and the CELL-PR011 cross-check
  (`radius(200, 0.04) = 0.10729830…`, recomputed; "0.11" is that value rounded).
- Strict-inequality integers at the dossier's chosen `g = 0.0092` recomputed exactly:
  `⌊2·ln(80)/0.0092²⌋+1 = 103,546`; `⌊2·ln(100)/0.0092²⌋+1 = 108,818`;
  `⌊2·ln(400)/0.0092²⌋+1 = 141,576`. The dossier's integers are arithmetically right **for that
  input**.
- **E1 — the input `g = 0.0092` does not have the status the dossier assigns it.** Three
  committed facts contradict the label "the ceiling … (best case)" (dossier:141-152):
  1. `0.0092` is a **rounded** value. The exact certified bound behind decision 035's "~0.0092"
     (`comite_decision_035…md:385`, arithmetic `1 − 2·0.495388`) is `ε ≤ 0.009223798457` — and
     it is the **n=8** ladder value (`data/reports/pr011_tv_certification_n8.csv`;
     `docs/plan_avanzado_14_julio_2026.md:51-55`). Exact instantiation at n=8 gives
     `m_min = 103,012 / 108,258 / 140,846` — already ≠ the dossier's table.
  2. The dossier pins the candidate family at **n = 4** throughout (V1, V2, V3, CELL-PR011,
     decision 035 §9's binding enumeration rule). The committed certified bound at n=4 is
     `ε ≤ 0.004611899229` (`data/reports/pr011_tv_certification_n4.csv`;
     `docs/plan_avanzado_14_julio_2026.md:51`). The binding best case is therefore
     `g = 0.004611899229`, giving `m_min = 412,046 / 433,029 / 563,383` per stream at
     `α_j = 0.05 / 0.04 / 0.01` — **≈ 4× the dossier's table**, in the anti-conservative
     direction (the dossier makes the MC route look ~4× cheaper than the committed data allow).
  3. The committed **nominal** TV at the exact CELL-PR011 parameters (n=4, `grid_m=12`) is
     `primary_tv_nominal = 0.0014402226592060835` (same CSV, annotation field — nominal, not
     certified). If the true gap is at that scale, `m_min ≈ 4.23e6 / 4.44e6 / 5.78e6` per
     stream — supporting the dossier's own qualitative warning that the MC route may be
     outright infeasible, far more strongly than its table suggests.
  The dossier's parametric caveat ("the true enumerated gap can only be smaller, inflating m by
  `(0.0092/g_true)²`", dossier:151-152) states the correction rule but does not cure the
  mislabel: for the n=4-pinned family, `g = 0.0092` is not attainable, so the table is not a
  "best case" — and a table headed "**Exact** (m,α) budget" built on a 2-significant-figure
  rounded, n-mismatched input conflicts with this repo's exactness discipline (cf.
  `auditor_report_010`'s "no rounding" standard) and with the PI's explicit audit instruction.
  **Required fix before /comite reliance** — see §7. The dossier's *conclusions* (exact
  enumeration route preferred; MC route doubtful) are unchanged and in fact strengthened by the
  corrected numbers.
- CELL-PR011 allocation and ledger re-verified: `m = 200`, `α_j = 0.04`
  (`dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` §4.2 cell table);
  `Σα_j = 0.01+0.01+0.25+0.10+0.05+0.04 = 0.46 ≤ alpha_total_bench = 0.50` ✓; overdraft raises
  (prereg §5 G4).
- Requested cost decomposition: per-stream size `m` (table above); streams per cell = 2 (total
  draws `2m` per cell — dossier states this); number of cells `K` and multiplicity via the
  frozen α-ledger, `α_j = alpha_total/K` ⇒ `m_min = 2·ln(4K/alpha_total)/g²` (logarithmic in K
  — dossier states this correctly). **No frozen resource/compute cap for OP-2.2 exists anywhere
  in the repo** (the α-ledger budgets error probability, not compute; decision 035 §9 requires
  a feasibility check but freezes no resource limit). Therefore V3 is **calculable but cannot
  be declared viable** against any committed limit; the dossier's "CONDITIONAL PASS" headline
  should say so explicitly (finding W1).

### V4 — physical scope

- **V4a (`ALGEBRAIC_NONREDUNDANCY`): CONFIRMED.** At fixed n=4, `N` is constant, so the
  regression on `(N, |relations|)` degenerates to conditioning on `|relations|`; the residual
  proves only that `S_BD` carries information beyond size and ordering fraction. The dossier
  states — correctly and repeatedly — that this is silent on horizon relevance and may never be
  laundered into a horizon claim (dossier:184-198). Physically correct: the control compares
  the same abstract laws; no horizon object is varied.
- **V4b (`HORIZON_FIDELITY`): conclusion CONFIRMED, stated premise IMPRECISE (warning W2).**
  The audited claim "the PR011 family is parametrized only by `(R, V, τ)` … no embedding, no
  `r=2M`, no patch placement recorded" (dossier:200-202, 208; inherited verbatim from decision
  035's falsifier, leakage channel (i), `comite_decision_035…md:410-415`) is **imprecise at the
  generator level**: the frozen builder is an EF-Schwarzschild-derived construction in which
  `W(t,r) = e^{r/t}(r/t − 1)` vanishes at `r = t` — i.e. **τ itself plays the role of `2M` and
  the horizon locus `r = τ` is in the construction** (`wp4_kappa_numeric_reference.py:56-57`);
  the patch corners ARE recorded as frozen constants (`(r_p,v_p) = (2,0)`, `(r_q,v_q) =
  (0.5,1)`, enumeration `:41-44`); and placement is not merely unrecorded but **hard-frozen to
  straddling** by `assert Up < 0 < Uq, "reference shape must straddle the horizon"`
  (`wp4:74-75`). What is true — and is the load-bearing point — is that none of this is exposed
  as a *family axis*: the poset laws are abstract unlabeled posets, the only variable parameter
  is τ, and an exterior-only member is not expressible without modifying frozen code (the
  assert rejects it) or designing a new family. So the exterior-vs-straddling contrast is
  indeed **not constructible within PR011-as-frozen** — the FAIL-structural verdict stands and
  is, if anything, *strengthened* (the family forbids non-straddling members outright; and
  since the two laws differ exactly by moving the horizon locus inside a fixed patch,
  τ-separation is inseparable from mass/global-curvature response without placement variation).
  The dossier (and, upstream, decision 035) should restate the premise precisely; see §7.
- **Ceiling: CONFIRMED.** `REFERENCE_WITNESS_SEPARATION_ONLY` as the maximum admissible
  terminal, explicitly held "even under an excellent TV result" (dossier:215-218, 231-238);
  forbidden vocabulary re-anchored and verified: "no llamarlo proxy de horizonte si solo
  discrimina masas" (`docs/plan_operativo_15_julio_2026.md:356`), forbidden identification
  "existe un test" = "existe un localizador" (`docs/claim_grammar.md:336`).

## 5. dev/validation separation & ground-truth leakage

- The dossier lives in `dev/` (committed as a scoped exception per `CLAUDE.md`), runs nothing,
  draws no seed, and touches no sealed path. The three audited commits modify no threshold, no
  frozen prereg, no validation artifact (§3).
- Leakage posture verified against op13 §4 (`op13…md:98-104`, `FAILED_DEVELOPMENT_PROVENANCE`):
  the dossier's V4b correctly refuses to import Schwarzschild geometry into a dev promotion
  decision, and its `[0,1]` normalization is defined from prior enumeration of the theoretical
  range, not from dev scoring distributions — closing leakage channels (i) and (ii) of decision
  035's falsifier. Channel (iii) (geometry co-deciding "the" witness) is not exercised: no
  witness is selected.
- No RNG anywhere in the audited change; the analytic V2 pair was derived by hand and is
  re-derived by hand here (author ≠ sole verifier obligation of decision 035 §5/§9: the P1/P2
  arithmetic and the V1 sanity values are hereby independently re-derived; the V3 integers are
  re-derived and one input mislabel found, §4).

## 6. Claim-boundary check

- No horizon/localization overclaim found in the dossier: the forbidden framings are barred
  twice (dossier:31-34, 215-218), V4a is fenced off from horizon claims (dossier:195-198), and
  the disposition caps at `SEPARATION_ONLY` with no scientific terminal emitted.
- Normative compliance, each verified against source:
  - **Does not open Candidate B**: decision 036's mandatory Candidate-B feasibility precondition
    (matrix §6 step 5 third branch, `next_observable_candidate_matrix.md:159-169`, REVISION note
    line 6) is not claimed to be discharged; the dossier's header states 036 "does NOT enable
    this candidate by itself" and its disposition opens nothing (dossier:239-242). Consistent
    with 035's falsifier point 3 (the BD scalar "is not even Candidate B") — the dossier never
    styles itself Candidate B. ✓
  - **Does not reopen PR009/PR010**: no such language; 036 §9's "no reopening" boundary
    respected. ✓
  - **Emits no OP-2.2 terminal**: explicit at dossier:36 and 238. ✓
  - **Authorizes no enumeration / Monte Carlo / scoring / freeze / PR013**: explicit at
    dossier:36-37 and 239-242; matches 035 §9 (every such step needs its own PI authorization
    + committee decision) and 036 §9. ✓
  - Gate-rule provenance: the rev-2 gate semantics (V2 `UNRESOLVED` without execution; V4
    split; no terminal) are attributed to a PI instruction of 2026-07-17 (dossier:5-7, 18-37).
    This is a PI-tier instruction layered on top of 035 §9's binding rules; no conflict found —
    the strictest reading of both is what the dossier implements (with the E1/W1/W2 fixes
    below). ✓

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | **ERROR (E1)** | V3 budget table presented as "Exact (m,α) budget … at the ceiling g = 0.0092 (best case)" uses a rounded (0.0092 vs exact 0.009223798457), **n=8-derived** input for a family the dossier itself pins at **n=4**, whose committed certified ceiling is `0.004611899229` → binding best-case `m_min = 412,046 / 433,029 / 563,383` per stream (α_j = 0.05/0.04/0.01), ≈4× the published `103,546 / 108,818 / 141,576`; anti-conservative for MC feasibility. Committed nominal TV at the exact CELL-PR011 parameters (`0.0014402226592060835`) puts the realistic scale at ≈4.2–5.8e6 per stream. Required fix: re-anchor the table to the n=4 certified value with exact digits; keep 0.009223798457 only as the loose family-wide bound; cite the nominal-TV scale as committed annotation; drop the word "exact" for any rounded input. Conclusions of the dossier survive the fix (strengthened). | `dev/OP22_BD_VIABILITY_DOSSIER.md:141-158` vs `data/reports/pr011_tv_certification_n4.csv`, `docs/plan_avanzado_14_julio_2026.md:51-55`, `comite_decision_035…md:385`; recomputation §4 |
| 2 | WARN (W1) | V3 "CONDITIONAL PASS" does not state that **no frozen resource/compute cap exists** for OP-2.2: the α-ledger budgets error probability, not compute. V3 is calculable but cannot be *declared viable* against any committed limit; the dossier should say so explicitly. | `dev/OP22_BD_VIABILITY_DOSSIER.md:135-176`; `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` §4.2/§5; absence verified by search |
| 3 | WARN (W2) | V4b premise "no embedding, no r=2M, no patch placement recorded" (inherited verbatim from decision 035 falsifier channel (i)) is imprecise: the frozen generator contains the horizon locus `r = τ` (τ ↔ 2M), records the patch corners as frozen constants, and hard-asserts straddling placement. The correct premise — placement is a frozen constant, not a family axis, and non-straddling members are rejected by the assert — *strengthens* the FAIL-structural conclusion. Wording fix needed in the dossier; an erratum-style note upstream to 035 is for /comite to decide. | `dev/OP22_BD_VIABILITY_DOSSIER.md:200-208`; `research_program/work_packages/wp4_kappa_numeric_reference.py:56-57,74-75`; `dev/pr011_tv_certification_enumeration.py:41-44`; `comite_decision_035…md:410-415` |
| 4 | WARN (W3) | Expected state said "clean tree"; two pre-existing untracked files are present (`nachocausal-program.local-before-pull.html`, `pr009-runner-scorer-v2.patch`). Unrelated to the dossier; should be cleaned or gitignored. | `git status` at HEAD `475cb93` |
| 5 | OK | V1 formula/convention verified against both primary sources; formula-vs-normalization-vs-numerics separation correct; no clipping, no hidden tuning freedom. | §4 V1; BD2010 md:117,123; Bhatnagar md:519,523 |
| 6 | OK | V2-global counterexample independently recounted and confirmed (P1: `|rel|=5, S=−6`; P2: `|rel|=5, S=+6`; `ΣN_m=|relations|` both). Discharges the author≠verifier obligation for these hand values. | §4 V2-global |
| 7 | OK | V2-support analytic route inspected: reduces to a single unwritten external premise (scipy PCHIP no-overshoot positivity); per the PI's rule it stays `UNRESOLVED`. Quantifier specified (union of supports at n=4, grid_m=12 suffices; inspection argument would give the intersection, every τ, every grid_m ≥ 4). Even a support PASS would not waive 035 §9's mandatory pre-freeze enumeration. | §4 V2-support; enumeration `:141-197`; `wp4:56-104` |
| 8 | OK | V4a physically correct: residual conditioning on `|relations|` proves algebraic non-redundancy only, never horizon fidelity; ceiling `SEPARATION_ONLY` held even under excellent TV; forbidden vocabulary anchored and verified. | §4 V4; plan:356; claim_grammar:336 |
| 9 | OK | Normative compliance: no Candidate B opening, no PR009/PR010 reopening, no OP-2.2 terminal, no execution authorization; seal intact; audited commits touch no frozen artifact. | §3, §6 |
| 10 | WARN ×22 | Standing mechanical warnings (committed data files with no generator reference), identical to reports 017/018; none introduced by the audited commits. | §2, `bash .claude/skills/auditor/audit.sh` |

AUDIT_ERRORS=1
AUDIT_WARNINGS=25

## 8. Verdict

One error (E1: mis-anchored "exact" V3 budget) and 25 warnings (22 standing mechanical + W1
resource-cap silence + W2 V4b premise imprecision + W3 untracked files).

AUDIT_VERDICT=AUDIT_FAIL

In the PI's requested vocabulary: **BLOCKED_WITH_REQUIRED_FIXES** — the dossier is
mathematically sound in structure and normatively clean, but is **not ready to return to
/comite as committed**: E1 must be corrected (and W1/W2 should be) first. The required fixes are
textual, dev-tier, and small; no conclusion of the dossier is overturned by them — the
corrected numbers make its own preference for the exact-enumeration route *stronger*.

### Gate table (post-audit, re-derived)

| Gate | Audit outcome | Evidence | Effect on disposition |
| --- | --- | --- | --- |
| V1 | **PASS** (formula + normalization convention exactly fixed; numerics correctly excluded) | BD2010 md:117,123; Bhatnagar md:519,523; dossier:37-64 | Freeze-able wording exists; V1b still needs the authorized enumeration |
| V2-global | **PASS** (analytic counterexample independently re-derived) | §4 V2-global | Global non-equivalence with `f_bench` proven |
| V2-soporte | **UNRESOLVED** (analytic route one unwritten premise short; enumerative test correctly not run) | §4 V2-support | Decisive open question; enumeration remains mandatory pre-freeze per 035 §9 regardless |
| V3 | **FAIL as published / PASS after E1 fix** (formula correct; instantiation mis-anchored; no frozen resource cap → calculable, not declarable viable) | §4 V3; n=4 CSV | MC route almost certainly infeasible (m ≈ 4.1e5–5.8e6 per stream); exact-enumeration route trivial and preferred |
| V4a | **PASS as a control of algebraic non-redundancy only** | §4 V4a | Mandatory control per 035 §9; proves nothing about horizon |
| V4b | **FAIL-structural, confirmed and strengthened** (placement hard-frozen to straddling; contrast inexpressible in frozen family) | `wp4:74-75` | Ceiling `REFERENCE_WITNESS_SEPARATION_ONLY` stands even with excellent TV |

### Justified next `/comite` outcome

**D — return the dossier for corrections (E1 mandatory; W1, W2 recommended), then B.** After
the fixes, the state of evidence supports **B**: keep V2-soporte `UNRESOLVED` and authorize the
frozen enumerative falsifier (decision 035 §5/§9 minimal test — one read-only run over the
already-frozen dev code, run and verified by someone other than the dossier's author) as the
single next execution. That run simultaneously discharges V1b (numeric `[S_min,S_max]`),
resolves V2-soporte empirically, and fixes the true gap `g` for an honest V3b — and it is
mandatory before any freeze anyway. **A** is not yet justified (V2-soporte unresolved; V3
published on a mis-anchored budget); **C** is not justified (no committed evidence of
support-restricted collapse — the analytic inspection in §4, as far as it goes, points the
other way).

Audit complete. Nothing committed, nothing pushed; the only file written is this report.
