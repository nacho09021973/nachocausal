# Auditor Report 008 — pr011-g2b-pre-execution-epsilon

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

**Trigger:** User authorization of **G2b** — pre-execution audit on any reported `ε` for PR011 TV
certification at `n=4`, `(τ_0, τ_1)=(0.95, 1.05)`, after G0b discharge (PR010 closed).

**Target:** `dev/pr011_tv_certification_enumeration.py`, falsifier stdout at `grid_m=20`,
convergence sweep `M ∈ {12, 16, 20, 24}`, harness
`tests/test_pr011_tv_certification_enumeration.py`, `tests/test_pr011_freeze_sanity.py`.

**Commit audited:** `873573fca7a98702244dd7450a466e3aa03f811c` (branch `main`).

**Out of scope:** Sealed validation path; emission of PR011 viability terminal;
`data/reports/pr011_*` artifacts; `n > 4` ladder.

## 2. Mechanical audit

Verbatim output of `bash .claude/skills/auditor/audit.sh`:

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/rvar_closure_negative_result.md
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
WARN: committed data file with no generator reference: data/reports/present_anchor_clean_v3_kill_test.csv
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
----------------------------------------
Auditor: 0 error(s), 12 warning(s)
```

Exit code: `0`.

## 3. Seal & freeze integrity

- **Live seal:** `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
- **Frozen record:** unchanged; matches `docs/preregistration_002.md:8`,
  `docs/preregistration_003.md:9`.
- **`nachocausal/`:** clean at HEAD (`git status` — no modified sealed files).
- **PR011 spec:** `FROZEN_VIABILITY_SPEC`; no change to `thresholds.py` or prereg frozen files.

## 4. Reproducibility of published numbers

**Generator:** `dev/pr011_tv_certification_enumeration.py` (commit `873573f`).

**Falsifier reproduction** (`python3 dev/pr011_tv_certification_enumeration.py falsifier --grid-m 20`,
this session, wall ~70 s):

```
PR011_ENUM_FALSIFIER=OK
n=4 grid_m=20
tau_pair=(0.95, 1.05)
raw_mass_sum=(0.527706552060, 0.527925458372)
mass_sum=(1.000000000000, 1.000000000000)
n_poset_classes=24
TV=0.001330364764505
TV_certified_upper=0.001330364765
falsifier_verdict=PAIR_DISTINGUISHABLE_TV_POSITIVE
```

**Convergence sweep** (same module, `n=4`, this session):

| `grid_m` | `raw_mass_sum` (τ₀) | `TV_norm` | `TV_certified_upper` | wall (s) |
|---|---|---|---|---|
| 12 | 0.3280750728 | 0.001440222659206 | 0.001440222660 | 2.6 |
| 16 | 0.4438067329 | 0.001376475994438 | 0.001376475995 | 8.8 |
| 20 | 0.5277065521 | 0.001330364764505 | 0.001330364765 | 82.7 |
| 24 | 0.5903706829 | 0.001306195179832 | 0.001306195180 | 362.8 |

Relative drift `TV_norm`: M=12→M=24 ≈ **9.3%**; M=20→M=24 ≈ **1.8%**.

**Harness:** `PYTHONPATH=. pytest tests/test_pr011_tv_certification_enumeration.py
tests/test_pr011_freeze_sanity.py -q` → **7 passed** (14.1 s).

**Provisional ε (audit session only, not committed to spec/README):**
`TV_certified_upper = 0.001330364765` at `(n, grid_m)=(4, 20)`.

**Not reproduced / not claimed:** `n ≥ 5`; copula Hellinger fallback (§6.1); any
`data/reports/pr011_*` file.

## 5. dev/validation separation & ground-truth leakage

- Channel remains order-only unlabeled posets; no embedding in estimator class.
- Pair `(0.95, 1.05)` from frozen `MIDPOINT_QUARTER_SPAN`; no PR009/PR010 scientific inputs.
- Script writes **no** `data/reports/pr011_*`; no `validate.run()`; no sealed seeds.
- Falsifier is dev pre-flight only — no viability terminal emitted (spec §8, §13).

## 6. Claim-boundary check

- **OK:** Falsifier correctly reports `TV > 0` (not Theorem A degeneracy).
- **OK:** No text in committed docs claims tier-1 certified `ε` or
  `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` terminal.
- **WARN:** Implementing script docstring says "exact enumeration" but runtime path is
  **midpoint copula grid quadrature** with **post-hoc renormalization** when `raw_mass_sum < 1`
  (`dev/pr011_tv_certification_enumeration.py:150-169`). This is weaker than spec §6.1 primary
  route ("exact rational masses … gap `> 1e-12` on any checked `n`").
- **OK:** No metric-reconstruction or 3+1D over-claim.

## 7. Findings

| # | Severity | Finding | Anchor |
|---|---|---|---|
| 1 | OK | Seal intact; `nachocausal/` clean | `make verify-seal`; `git status` |
| 2 | OK | Falsifier reproduces at M=20; `TV > 0` | command stdout (§4) |
| 3 | OK | Tests 7/7 pass | `pytest` stdout (§4) |
| 4 | OK | No `pr011_*` report artifacts; no viability terminal | `glob data/reports/pr011_*` empty |
| 5 | WARN | `raw_mass_sum` only **0.59** at M=24 — quadrature under-coverage; laws renormalized | §4 table |
| 6 | WARN | `TV_norm` drifts **~1.8%** (M=20→24) and **~9%** (M=12→24); convergence not closed | §4 table |
| 7 | WARN | Method is grid quadrature + renormalization, not §6.1 exact enumeration tier | `pr011 spec §6.1`; `dev/pr011_tv_certification_enumeration.py:96-169` |
| 8 | WARN | Provisional `ε ≈ 0.00133 < 1` supports **non-degeneracy** only; **not** a certified upper bound for terminal emission | §4; spec §8 `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` |
| 9 | WARN | Mechanical audit: 12 legacy CSV files without generator reference (pre-existing) | `audit.sh` §2 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=5

## 8. Verdict

**G2b pre-execution audit:** the falsifier result (`TV > 0` at `n=4`) is **reproducible** and
**honestly scoped** as dev pre-flight. The reported `ε` is a **provisional quadrature estimate**,
not a tier-1 certified bound: discretization error is orders of magnitude above the frozen
`1e-12` budget, and mesh convergence is not closed at `M=24`.

**Do not emit** `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` or any PR011 viability terminal on this `ε`
until quadrature converges (or §6.1 fallback with its own stability audit) and a follow-up G2b
pass certifies the bound.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS