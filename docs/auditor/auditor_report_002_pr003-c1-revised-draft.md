# Auditor Report 002 — pr003-c1-revised-draft

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target
C-1 re-audit (comité-004 §9 C-1) of the **REVISED** `docs/preregistration_003_draft.md` after the
B1–B8 revisions and the R-1 sealed-numpy re-run. This is the freeze-gate audit of the revised
frozen-text candidate; it grounds C-2 (lightweight reconvene) and the user's C-3 freeze decision.
- Repo root `/home/ignac/nachocausal`, branch `main`, working tree: only `docs/preregistration_003_draft.md`
  modified; `docs/auditor/` and `docs/comite/comite_decision_004…` untracked (the review artefacts).
  No `M nachocausal/`.
- Supersedes nothing; complements `auditor_report_001` (which flagged W1 — now discharged here).

## 2. Mechanical audit
Verbatim output of `bash .claude/skills/auditor/audit.sh` (exit code `0`):

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/hoja_de_ruta_25_jun_2026.md,docs/preregistration_002.md,docs/preregistration_003_draft.md
----------------------------------------
Auditor: 0 error(s), 0 warning(s)
```
No CI-swallowing, untested-code, seal drift, gitignored-but-tracked path, or ungenerated `results/`
data flagged.

## 3. Seal & freeze integrity
- `make verify-seal` → `nachocausal/thresholds.py sha256 =
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` — unchanged; matches the
  prereg-002 record (`docs/preregistration_002_result.md:10`) and the draft (`:14-15`).
- `git status --short` shows no `M nachocausal/`: the B1–B8 revisions touched only the draft text.
  The freeze remains doc-only; `K_LOC=2` (`thresholds.py:98`) unchanged; no new constant.

## 4. Reproducibility of published numbers — **W1 (from report 001) now DISCHARGED**
The R-1 sealed-environment re-run actually happened and reproduces the §3 figures. Both logs verified
this session:
- **O3** (`dev/o3_sealed_numpy_rerun.log`): header `python 3.12.3 numpy 1.26.4` (`:3`), `backend device
  = cpu` (`:5`), seal `6e2c3888…` `[pre]` (`:4`) and `[post]` (`:80`), `no seed in RESERVED_002 touched`
  (`:81`). Scatter `sd(r̂)/ℓ` = **0.34** (`:12`) / **0.45** (`:29`) / **0.39** (`:46`) / **0.40**
  (`:63`); resolvable `2s/ℓ` = **0.60** (`:26`) / **0.47** (`:43`) / **0.62** (`:60`) / **0.71** (`:77`)
  — identical to the GPU-recorded notes table to 2 decimals.
- **R2** (`dev/kbeam_sealed_numpy_rerun.log`): `numpy 1.26.4` + `device = cpu` (`:3,6`), seal pre/post
  (`:4,44`), RESERVED_002 untouched (`:45`). Intensity 7200: top-1 `d⊥/ℓ@k=8` K=1→**3.21** (`:24`),
  K=64→**6.63**, `n` 8→**147**, reach **23%** (`:30`) — matches the recorded table.
- Interpretation matches the revised draft's honesty (§3 leg 2): the **integer** `O`-multiset is
  GPU≡CPU bit-identical (`maxdiff=0`); the **float** figures reproduce statistically/to the reported
  precision, NOT claimed bit-level. The constant `≈0.4·ℓ` is **not** a GPU-venv artefact.
- The raw re-run logs are git-ignored (regenerable) per `CLAUDE.md`; the figures they contain are
  also recorded in the committed `dev/PR003_*_NOTES.md` and the revised draft §3.

## 5. dev/validation separation & ground-truth leakage
- Unchanged and intact. The R-1 re-runs used `--device cpu` on EXPLORE_POOL seeds only; both scripts'
  runtime guards refuse non-EXPLORE_POOL and RESERVED_002 seeds (`measure_info_bound_o3.py:114-116`,
  `measure_kbeam_peeloff.py:94-96`), and both logs print `no seed in RESERVED_002 touched`.
- No-new-constant rule respected: the revised §4 still reports the measured `O(1)<2` as a consistency
  statement about the sealed `K_LOC=2`, not a recalibration (`docs/preregistration_003_draft.md`).
- The hidden embedding is used only to score (bracket edges), never to guide the observable.

## 6. Claim-boundary check — revised wording verified, no over-claim
Every `minimax`/`universal`/`no estimator`/`information floor` occurrence in the revised draft sits
under a **NOT**, **OPEN**, or explicit **guard** heading — none presented as established:
- §2 `:50-57` "NOT a Le Cam minimax lower bound…"; `:67` "NOT a universal/asymptotic no-go"; `:105`
  "explicitly NOT a minimax statement"; `:166` "OPEN — minimax floor over `C`".
- **B6 (your stressed point) present:** `:59` "**NOT an order-theoretic universal over estimators —
  it is the limit of OUR sealed tool**", with the future-volume "sibling of EGS longest-chain" note
  (`:63`).
- **B1 positive falsification criterion present:** §6 `:143-145` — (★) is FALSIFIED if the sealed
  estimator's blind `median|r̂−r_S|` < **0.2·ℓ** (half the measured ≈0.4·ℓ) at any frozen intensity;
  the "faster method ⇒ leakage" asymmetry is declared in advance (`:146-149`), and a different
  order-only estimator beating it resolves the OPEN minimax-over-`C` item, not a refutation of (★).
- **B2 absent-citation guard present:** §7 O4 `:171-173` — Tsybakov 2009 / Bretagnolle–Huber are
  PHYSICALLY ABSENT from `biblioteca/`; the frozen text MUST NOT cite them as support; (★) does not
  depend on them.
- **B3** honest scaling `:95` (×8 density = ×2.83 in ℓ; ~30%); **B5** criterion-specific PHYSICAL
  qualifier `:113` (interval-cardinality regularity); **B4** 14400 single-ladder datum marked
  anecdotal / not load-bearing; **B8** no bit-level float-reproducibility claim (`:90` scopes
  bit-identity to the integer observable only).
- The line-156 occurrence of "no estimator of `C` can do better" is the **guard** instruction (the
  frozen text must *never* say it) — correct, not an over-claim.
- The draft remains a DRAFT; the frozen `docs/preregistration_003.md` must be created from this
  audited text (C-3, user's call) and re-pass `verify-seal` before+after.

## 7. Findings
| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Mechanical audit clean 0/0; seal recorded incl. in the draft | `bash audit.sh` → exit 0 |
| 2 | OK | Seal `6e2c3888…` unchanged; no `M nachocausal/`; doc-only freeze, no new constant | `make verify-seal`; `git status --short`; `thresholds.py:98` |
| 3 | OK | **W1 DISCHARGED** — O3/R2 reproduce on sealed numpy 1.26.4 (CPU), seal pre/post, RESERVED_002 untouched | `dev/o3_sealed_numpy_rerun.log:3-5,12,29,46,63,80-81`; `dev/kbeam_sealed_numpy_rerun.log:3-6,24,30,44-45` |
| 4 | OK | dev/validation separation intact in the re-runs (EXPLORE_POOL only; RESERVED_002 refused) | `measure_info_bound_o3.py:114-116`; `measure_kbeam_peeloff.py:94-96` |
| 5 | OK | B1 positive falsification criterion added (FAIL if sealed median\|r̂−r_S\| < 0.2·ℓ) | `docs/preregistration_003_draft.md:143-149` |
| 6 | OK | B6 "limit of OUR tool, not universal over estimators" added; B2 absent-citation guard; B3/B4/B5/B8 wording fixes | draft `:59-65,171-173,95,113,90` |
| 7 | OK | No residual minimax/universal phrasing presented as established | draft grep §6 above |

AUDIT_ERRORS=0
AUDIT_WARNINGS=0

## 8. Verdict
One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error). Must match the counts in §7.
AUDIT_VERDICT=AUDIT_PASS
