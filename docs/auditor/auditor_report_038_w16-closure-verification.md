# Auditor Report 038 — w16-closure-verification

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit
`33d712d7fa93816ef862224479bc754e46f6b178` (`git rev-parse HEAD`).

Trigger: narrow follow-up to `docs/auditor/auditor_report_037_wp6-s1-paper-and-lean-evidence.md`,
to determine whether its finding **W-16** is discharged. W-16 was: the ledger token
`THEOREM_C_FINITE_MATRIX_FORM = LEAN_PROVED` was broader than the theorem behind it, because the
manuscript's boxed Theorem C also asserts `dim V_N = rank G_{[P]}^{(N)} = C(N,2)` while no
`finrank` theorem for `DCSymM` existed.

Targets: the remediation commit `bcbeada..33d712d`, the Lean sources under
`formal/HorizonFormal/HorizonFormal/S1Paper/`, and the ledger
`FORMALIZATION_STATUS.md`. Per instruction, literature/priority analysis was **not** reopened,
and W-17 is treated as pre-existing worktree hygiene, not as a mathematical or manuscript defect.
All mandatory mechanical/seal/integrity checks were run regardless of the narrow focus.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code `0`:

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,[…88 further freeze/decision/report files…]
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
WARN: committed data file with no generator reference: evidence/new_geometry_20260719/mink_control_metrics.csv
----------------------------------------
Auditor: 0 error(s), 23 warning(s)
```

(The `ok:` line's file enumeration is elided at `[…]`; nothing else is altered.) The warning set is
**byte-identical to report 037's**: the same 23 pre-existing `data/reports/`+`evidence/` CSVs from
PR-004/PR-005/PR-011 and the 2026-07-19 geometry set. The remediation introduced no new mechanical
finding, and removed none — as expected, since it touched no data path.

## 3. Seal & freeze integrity

- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- Unchanged from report 037 and still recorded at `docs/preregistration_002.md:8` and
  `docs/preregistration_003.md:9`. No drift.
- `git diff --shortstat bcbeada..33d712d` → `2 files changed, 145 insertions(+)`. **Zero
  deletions**: the remediation is purely additive, so no earlier ledger text, no frozen artefact
  and no prior pass's record was rewritten or removed.

## 4. Reproducibility of published numbers — W-16 verification

The nine requested checks, each verified from source or build output, not from the ledger.

**(1) `finrank (DCSymM N) = N.choose 2` — LEAN_PROVED.**
`SpanTheoremC.lean:512` `theorem finrank_DCSymM (N : ℕ) : Module.finrank ℝ (DCSymM N) = N.choose 2`.
The auditor type-checked the statement independently of its name, in a separate file against the
built library: `example (N : ℕ) : Module.finrank ℝ (DCSymM N) = N.choose 2 := finrank_DCSymM N`
elaborates with no error. It rests on `edgeBasis` (`:493`), a genuine
`Module.Basis {p : Fin N × Fin N // p.1 < p.2} ℝ (DCSymM N)` assembled from the first pass's
`edgeLaplacian_linearIndependent` and `DCSymM_eq_sum_edgeLaplacian` — no theory re-derived — and on
`card_pairs` (`:480`). The arithmetic form is also proved (`finrank_DCSymM_eq_half:516`,
`= N*(N-1)/2` via `Nat.choose_two_right`), as the remediation brief required.

**(2) `finrank (span ℝ (ASet N)) = N.choose 2` on the real class-sum span — LEAN_PROVED.**
`SpanTheoremC.lean:526`. Independently type-checked:
`example (N : ℕ) (hN : N ≠ 0) : Module.finrank ℝ (Submodule.span ℝ (ASet N)) = N.choose 2 := finrank_span_classSum_restr hN`.
Crucially, the auditor also restated the underlying span theorem with `ASet` **unfolded**, to
confirm the object is the real class sum and not a stand-in:
`example (N : ℕ) (hN : N ≠ 0) : Submodule.span ℝ (Set.range (fun σ : Equiv.Perm (Fin N) => restr N (classSum σ))) = DCSymM N := span_classSum_restr_eq hN`
elaborates. `ASet` is `Set.range (fun σ => restr N (classSum σ))` (`:435–436`), and `classSum` is
the fiber sum of `ClassSum.lean:43` over `fiber` (`:39`), the real `PosetIsomorphic` fiber.

**Independent numeric confirmation of the asserted value.** Kernel evaluation, not the proof:
`#eval Fintype.card {p : Fin 4 × Fin 4 // p.1 < p.2}` → `6`; `Fin 5` → `10`; `Fin 6` → `15`;
`#eval (Nat.choose 4 2, Nat.choose 5 2, Nat.choose 6 2)` → `(6, 10, 15)`. Consistent with
`appendixC_matrix_check.py`, which independently finds span rank `C(N,2)` for `N = 2..6`.

**(3) `THEOREM_C_CLASS_SUM_SPAN` / `THEOREM_C_CLASS_SUM_SPAN_DIMENSION = LEAN_PROVED` — accurate.**
Operative block at `FORMALIZATION_STATUS.md:279–285`. The first names `span_classSum_restr_eq`
(third pass, re-verified in report 037 §4); the second names the theorems of (1)–(2) above. Both
labels match what exists.

**(4) `THEOREM_C_FINITE_MATRIX_FORM` explicitly RETIRED — confirmed, doubly.**
The third-pass block at `:227–229` is kept verbatim (historical record) but is immediately
followed at `:232–233` by an additive blockquote `**[RETIRED — see the fourth pass below.]**`
naming W-16 as the reason and directing the reader to the new tokens; and the operative block
itself lists `THEOREM_C_FINITE_MATRIX_FORM = RETIRED (too broad; …)` at `:284–285`. A reader
reaching the old token from either direction is told it is not operative.
Repo-wide, the only other occurrence of the old token is
`docs/auditor/auditor_report_037…:228` — the auditor's own remediation recommendation, correctly
left untouched as historical evidence.

**(5) `THEOREM_C_GRAM_RANK = NOT_FORMALIZED` — confirmed, and nothing is represented as checked.**
`FORMALIZATION_STATUS.md:274` and `:282`. `grep -rniE 'gram|rank G'` over
`S1Paper/*.lean` returns **only two docstring lines**, `SpanTheoremC.lean:462–463`, which
themselves state that no Lean theorem identifies the Fisher/Gram rank and that it remains
`NOT_FORMALIZED`. No Lean object for `G_{[P]}^{(N)}` exists. The ledger row states explicitly that
the ordinary-paper inference from the span "is *not* Lean-checked and must not be reported as if
it were" — the exactly correct disposition.

**(6) `BERNSTEIN_TRANSPORT_TO_VN = NOT_FORMALIZED` — confirmed.**
`FORMALIZATION_STATUS.md:283`, unchanged from the third pass (`:229`). No Lean file references
`Λ_N`, `𝔗_N` or a polynomial Hilbert space.

**(7) Manuscript, outline and bibliography unchanged by the remediation — confirmed mechanically.**
`git diff --name-only bcbeada..33d712d -- research_program/` returns **0 files**. The remediation
touched exactly two files, both under `S1Paper/`
(`FORMALIZATION_STATUS.md`, `SpanTheoremC.lean`).

**(8) No manuscript statement strengthened because of Lean — confirmed mechanically.**
At this HEAD the last commits touching the three artefacts are still
`2bd82cd` (manuscript), `ba3f210` (outline), `9f4289b` (bibliography) — all strictly before the
four Lean commits `97d8d5f`, `2d725c4`, `bcbeada`, `33d712d`. `ClaimMap.md`'s last commit is
`97d8d5f`, i.e. the pre-registered planning document is still untouched.

**(9) Zero `sorry`/`admit`/custom axiom; build passes — confirmed.**
`grep -rInE '\bsorry\b|\badmit\b|^\s*axiom\b|\bsorryAx\b|\bpostulate\b'` over
`S1Paper/*.lean` and `S1Paper.lean`: no matches (exit 1). `#print axioms` on `finrank_DCSymM`,
`finrank_span_classSum_restr`, `finrank_span_classSum_restr_eq_half`, `edgeBasis` and
`card_pairs`: each reports exactly `[propext, Classical.choice, Quot.sound]`. `lake build`
(read-only) → `Build completed successfully (4716 jobs)`.

**Verdict on W-16: CLOSED.** Both halves the finding called for were done — the dimension is now a
Lean theorem *on the real class-sum span*, and the over-broad token is retired and replaced by
tokens that cannot be read as covering the Gram rank or the Bernstein transport.

## 5. dev/validation separation & ground-truth leakage

Unchanged from report 037 and re-verified: the remediation touches only two files under
`formal/HorizonFormal/HorizonFormal/S1Paper/`; nothing under `nachocausal/`, `dev/`,
`docs/preregistration_*` or any sealed path. The new Lean content reads no data, no threshold and
no hidden embedding. `audit.sh` reports no gitignored-but-tracked path, so the `dev/` sandbox rule
of `CLAUDE.md` holds at HEAD. The `formula` branch was not touched.

## 6. Claim-boundary check

- No claim-boundary text changed: `research_program/` has zero diff across the remediation, so the
  manuscript's own limits paragraph (`…manuscript.tex:217`, "not a reconstruction of geometry from
  a causet … not a result beyond the 1+1-dimensional S1 model") stands exactly as audited in 037.
- The ledger's boundary is now *narrower*, not wider, than before the remediation: two
  `NOT_FORMALIZED` tokens are stated explicitly where one broad `LEAN_PROVED` token stood.
- No new over-claim was introduced. The new Lean docstrings at `SpanTheoremC.lean:462–463`
  volunteer the limitation rather than hiding it.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Mechanical audit: 0 errors, exit 0; warning set byte-identical to report 037; no new finding introduced | `bash .claude/skills/auditor/audit.sh` (§2) |
| 2 | WARN×23 | Committed `data/reports/`+`evidence/` CSVs with no generator reference — pre-existing, unrelated to S1, carried forward from report 037 | `audit.sh` output, §2 |
| 3 | OK | Seal `6e2c3888…` unchanged and still recorded; remediation is additive-only (145 insertions, 0 deletions) | `make verify-seal`; `git diff --shortstat bcbeada..33d712d` |
| 4 | OK | **W-16 CLOSED (a):** `finrank (DCSymM N) = N.choose 2` Lean-proved, via a real `Module.Basis`; arithmetic form also proved | `SpanTheoremC.lean:512,516,493,480`; independent `example` type-check |
| 5 | OK | **W-16 CLOSED (b):** `finrank (span ℝ (ASet N)) = N.choose 2` Lean-proved on the **real class-sum span**, confirmed by re-stating `ASet` unfolded to `classSum` | `SpanTheoremC.lean:526,435`; `ClassSum.lean:39,43`; independent `example` type-check |
| 6 | OK | Asserted value independently confirmed by kernel evaluation: card = 6/10/15 = `choose(4,2)/(5,2)/(6,2)` | `#eval` (§4) |
| 7 | OK | `THEOREM_C_CLASS_SUM_SPAN` and `…_DIMENSION = LEAN_PROVED` are accurate labels for existing theorems | `FORMALIZATION_STATUS.md:279–281` |
| 8 | OK | Old token explicitly `RETIRED` in two places; only other repo occurrence is inside report 037, correctly untouched | `FORMALIZATION_STATUS.md:232–233,284–285`; `grep -rn THEOREM_C_FINITE_MATRIX_FORM` |
| 9 | OK | `THEOREM_C_GRAM_RANK = NOT_FORMALIZED`; no Lean Fisher/Gram object exists — the only `gram` hits are two docstrings disclaiming it | `FORMALIZATION_STATUS.md:274,282`; `SpanTheoremC.lean:462–463` |
| 10 | OK | `BERNSTEIN_TRANSPORT_TO_VN = NOT_FORMALIZED` unchanged | `FORMALIZATION_STATUS.md:283` |
| 11 | OK | Manuscript, outline, bibliography, `ClaimMap.md` unchanged by the remediation and still predate every Lean commit | `git diff --name-only bcbeada..33d712d -- research_program/` → 0; `git log -1` per artefact |
| 12 | OK | Zero `sorry`/`admit`/custom axiom; `#print axioms` clean on all five new results; `lake build` PASS (4716 jobs) | `grep` exit 1; `#print axioms`; `lake build` |
| 13 | OK | Ledger navigation: the second-pass row `APPENDIX_C_MATRIX_HALF = NOT_FORMALIZED` (`:50`) has no *inline* superseded marker, unlike the third-pass token which got one. Not a mismatch — the third pass names that row explicitly in its "What it supersedes" list (`:176` region), and `THEOREM_C_LEAN = PARTIAL` (`:53`) remains substantively true today. Recorded for symmetry only; recommend, do not require, an inline marker there too. | `FORMALIZATION_STATUS.md:50,53,176` |
| 14 | WARN | **W-17 carried forward** (pre-existing worktree hygiene, explicitly out of scientific scope): working tree unclean — modified `research_program/work_packages/wp6_full_class_sum_rank_theorem.md`, untracked `dev/OCCUPANCY_GENERATING_SYSTEM_3plus1.md`, and both audit reports (`037`, `038`) untracked pending the user's separate documentation commit. None is part of HEAD `33d712d`. | `git status --short` |

AUDIT_ERRORS=0
AUDIT_WARNINGS=24

## 8. Verdict

Zero errors. Twenty-four warnings: the 23 pre-existing, S1-unrelated `data/reports` generator
warnings, plus W-17 carried forward as worktree hygiene. **W-16 is discharged and does not
reappear.**

```text
W16_STATUS            = CLOSED
CLAIM_MISMATCH        = 0
FORMALIZATION_MISMATCH= 0
```

The formalization mismatch that report 037 found is gone: every token in the operative certificate
now names a theorem that exists, and the two things that do **not** exist in Lean — the Fisher/Gram
rank and the Bernstein transport to `V_N = Sym²P_{N-1}` — are marked `NOT_FORMALIZED` and are
explicitly excluded in prose. The ledger can no longer be read as
"Theorem C as stated in the manuscript = Lean proved".

No remediation is recommended for the Lean track. The single non-blocking suggestion is finding 13
(an inline superseded marker on the second-pass row, for symmetry); it asserts nothing false as it
stands. W-17 is the user's to close by committing or reverting the pending worktree items — the
auditor does not act on it, and the two audit reports are deliberately left untracked here.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
