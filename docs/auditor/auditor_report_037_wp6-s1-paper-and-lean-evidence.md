# Auditor Report 037 — wp6-s1-paper-and-lean-evidence

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit
`bcbeadae3432afd0a14f92b7853741758d16bb35` (`git rev-parse HEAD`).

Trigger: user-requested scoped audit of the WP6 S1 paper after the third Lean pass closed
Appendix C (C.12)–(C.21). Targets:

- `research_program/synthesis/wp6_s1_finite_causal_order_manuscript.tex` (345 lines);
- `research_program/bibliography/wp6_s1_finite_causal_order_references.bib`;
- `formal/HorizonFormal/HorizonFormal/S1Paper/` (13 `.lean` modules, `ClaimMap.md`,
  `FORMALIZATION_STATUS.md`, 2 `.py` guardrail scripts) and
  `formal/HorizonFormal/HorizonFormal/S1Paper.lean`.

`FORMALIZATION_STATUS.md` was treated as the **formal-certification ledger under audit**, not as
evidence. Every ledger row asserted below was checked against the Lean sources themselves.

Working-tree state at audit time is **not clean** (see finding W-2); the audit is of HEAD, not of
the working tree.

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

(The `ok:` line's file list is elided at `[…]` for readability; it is the script's single
comma-separated enumeration of the freeze/decision/report files recording the seal. Nothing else
is altered.)

All 23 warnings are **pre-existing repository history unrelated to the S1 paper**: committed
`data/reports/` and `evidence/` CSVs from PR-004/PR-005/PR-011 and the 2026-07-19 geometry
evidence set. No S1-paper artefact appears among them. No CI-failure-swallowing, no
gitignored-but-tracked path, and no missing-test finding was reported.

## 3. Seal & freeze integrity

- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, exit `0`.
- Binding freeze records naming that SHA: `docs/preregistration_002.md:8` and
  `docs/preregistration_003.md:9`. Live SHA and recorded SHA **match**; no drift.
- The S1 paper track touches no sealed artefact: the audited commit `bcbeada` and its predecessor
  `2d725c4` modify only `formal/HorizonFormal/HorizonFormal/S1Paper*` paths
  (`git show --stat`), never `nachocausal/thresholds.py` nor any `docs/preregistration_*`.

## 4. Reproducibility of published numbers

The S1 paper is a mathematics manuscript; its "numbers" are theorem statements, not estimator
outputs. They were checked against the Lean evidence and the two guardrail scripts.

- `lake build` (read-only) at HEAD: `Build completed successfully (4716 jobs)`. This matches the
  count the ledger claims (`FORMALIZATION_STATUS.md`, third-pass Guardrails paragraph).
- `grep -rInE '\bsorry\b|\badmit\b|^\s*axiom\b|\bsorryAx\b|\bpostulate\b'` over
  `formal/HorizonFormal/HorizonFormal/S1Paper/*.lean` and `S1Paper.lean`: **no matches**
  (exit 1). Zero `sorry`, zero `admit`, zero project-introduced axiom in Lean code.
- Independent `#print axioms` re-run by the auditor on `span_classSum_restr_eq`, `span_SSet`,
  `coeffSum_cCoef_eq_sN`, `fiber_eq`, `classSum_isSymm`: each reports exactly
  `[propext, Classical.choice, Quot.sound]`. No custom axiom.
- `formal/HorizonFormal/HorizonFormal/S1Paper/fiber_bruteforce_check.py` → `PASS` for `N = 2..6`.
- `formal/HorizonFormal/HorizonFormal/S1Paper/appendixC_matrix_check.py` → `PASS` for `N = 2..6`,
  reporting span rank `C(N,2)` over all realized poset classes (2, 5, 16, 63, 315 classes).
  Both scripts state in their own docstrings that they participate in no Lean proof; the ledger
  repeats that restriction. Confirmed: neither is imported by any `.lean` file.
- Bibliography cross-check (auditor script, `\cite[tp]` keys vs `@type{key,}`): 20 cited keys, 20
  bib entries, `CITED_BUT_MISSING_FROM_BIB: none`, `IN_BIB_BUT_UNCITED: none`.

### Claim-by-claim verification of the requested items

**(1) Hinge genuinely `LEAN_PROVED` through real fibers/class sums — CONFIRMED.**
`fiber τ := univ.filter (fun σ => PosetIsomorphic σ τ)` (`ClassSum.lean:39`) is the real
isomorphism-class fiber, not a stand-in; `classSum τ := ∑ σ ∈ fiber τ, permM σ`
(`ClassSum.lean:43`) is the manuscript's (3.12); `ASet N := Set.range (fun σ => restr N (classSum σ))`
(`SpanTheoremC.lean:432`); `span_classSum_restr_eq (hN : N ≠ 0) : Submodule.span ℝ (ASet N) = DCSymM N`
(`SpanTheoremC.lean:438`). The `⊇` direction routes through `Sab_nonzero_smul_classSum`
(`ClassSum.lean:74`), i.e. the certified (C.11), and through the (C.12)–(C.21) chain. The
statement is **not vacuous**: `edgeLaplacian_linearIndependent` (`FiniteLinearAlgebra.lean:155`)
exhibits `C(N,2)` linearly independent elements of `DCSymM N`, so the target module is nontrivial
for `N ≥ 2`; the numeric check independently confirms rank `C(N,2)` for `N = 2..6`.

**(2) `V_N = Sym²P_{N-1}` / Theorem C as a whole NOT described as Lean-certified — CONFIRMED.**
The manuscript contains **no reference to Lean, mathlib, formalization, machine-checking or
certification at all** (`grep -niE 'lean|formaliz|machine-check|mechani[sz]|certif|verified|proof assistant|mathlib'`
returns two lines, both false positives: "Laplacian" at `:91` and "a formal consequence" at
`:175`). The ledger states `BERNSTEIN_TRANSPORT_TO_VN = NOT_FORMALIZED` and says explicitly that
the paper is not Lean-certified, only its finite combinatorial core. No Lean file mentions
`Λ_N`/`𝔗_N` or the Bernstein transport.

**(3) Corollary D only `LEAN_PROVED_ABSTRACT_INTERFACE` — CONFIRMED.**
`AbstractQuotient.lean:24` carries `[FiniteDimensional ℝ 𝒳]`, genuinely stronger than the paper's
`𝒳 = H ⊗̂ H`. The ledger row says so and states the S1 instance is not built. No Lean object named
for `𝒞_N`, `R_C^{(N)}` or `μ_{N,0}` exists.

**(4) Theorem F asymptotics / QMD / Bernstein–Durrmeyer / HS density remain ordinary proofs — CONFIRMED.**
`grep -rniE 'asymptot|durrmeyer|qmd|densit|hilbert.schmidt'` over the Lean sources returns a single
hit, a docstring line in `NormVsSOT.lean:6` describing that module as "the one abstract,
cheaply-formalizable piece of Theorem F's asymptotic boundary". No asymptotic-retention,
order-statistic, Bernstein–Durrmeyer or density theorem exists in Lean.

**(5) `N=2,3,4` Fisher statements are exact finite checks only — CONFIRMED.**
`ExactChecks.lean` contains `N2_Fisher_spectrum:48`, `N3_Fisher_spectrum:52`,
`N4_pure_eigenvalues:60`, `N4_cubic_determinant:72`, `N4_cubic_factor_ne_zero:82` — all closed
rational/polynomial identities discharged by `norm_num`/`ring`. Nothing general in `N`.

**(6) Corollary H logic Lean-proved, `N=2` integrals not — CONFIRMED.**
`corollaryH` (`CorollaryH.lean:34`) takes `hw₂ : w₂ ≠ 0` as an explicit **hypothesis**, and
`N2_moment_squares` (`ExactChecks.lean:23`) takes the moment values as hypotheses. The polynomial
integrals producing them are absent, exactly as the ledger's `N2_INTEGRAL_FORMALIZED` row says.

**(7) `r_N(γ_ψ)=2` kept restricted to the one explicit orbit — CONFIRMED.**
Every occurrence carries the restriction: `:56` ("one explicit antisymmetric orbit … not a
classification of the full antisymmetric sector"), `:153` ("for the explicit path (7.3)"), `:189`
("This single orbit … does not classify higher-order behavior"), `:215` ("One admissible orbit …
not a classification"), `:217` ("for the explicit witness"), `:337`.

**(8) SOT vs operator norm correctly stated — CONFIRMED.**
`:127` boxes `F̂_N →^SOT Π_sym`; `:131` states "The convergence in (6.20) is not convergence in
operator norm" and gives the witness with `‖F̂_N − Π_sym‖ ≥ 1` for every `N`; `:185`, `:213`,
`:297` (E.24)/(E.25) repeat both halves together. The manuscript also refuses the stronger
readings ("no rate or threshold uniform over the Hilbert–Schmidt unit sphere").

**(9) No novelty/priority claim strengthened by the Lean work — CONFIRMED, mechanically.**
`git log -- research_program/synthesis/wp6_s1_finite_causal_order_manuscript.tex` shows its last
change is `2bd82cd`, and the `.bib`'s is `9f4289b` — both **strictly before** the Lean commits
`97d8d5f`, `2d725c4`, `bcbeada`. The manuscript's §10 Priority status still reads "that absence is
not itself a priority claim, and our search was not exhaustive. A broader specialist review would
be needed before any affirmative claim of novelty."

**(10) New Lean modules clean — CONFIRMED.** See §4 above (grep, `#print axioms`, `lake build`).

## 5. dev/validation separation & ground-truth leakage

- No leakage path exists: the S1 track is a mathematics manuscript plus a Lean library. The
  audited commits touch only `formal/HorizonFormal/HorizonFormal/S1Paper*`; nothing under
  `nachocausal/`, `dev/`, `docs/preregistration_*` or the sealed path is modified.
- No Lean or manuscript artefact reads a hidden embedding, a ground-truth coordinate, or a
  threshold. The two `.py` guardrail scripts are self-contained enumerations over `S_N` with no
  repository imports and no data files.
- `audit.sh` reported no gitignored-but-tracked path, so the `dev/` sandbox rule
  (`CLAUDE.md`, "Layout") is not violated at HEAD.
- The `formula` branch was not touched, inspected destructively, or checked out.

## 6. Claim-boundary check

- The S1 manuscript explicitly disclaims the boundary the repo cares about, at `:217`: "This is an
  exact, local account of what the finite causal-order channel retains in S1, **not** a
  reconstruction of geometry from a causet, a claim of global or nonlinear identifiability, or a
  result beyond the 1+1-dimensional S1 model; §10 states the full limits."
- No text in the audited manuscript claims metric reconstruction, an asymptotic event horizon,
  3+1D scope, or a PASS coerced from an abstain/OUT_OF_DOMAIN.
- Root `README.md:390–395` describes the Lean track as "Optional Lean formalisation track …
  independent of the sealed Python validation path"; it makes no S1-certification claim.
- One boundary imprecision was found in the **ledger**, not the manuscript: finding W-1 below.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Mechanical audit: 0 errors, exit 0; seal recorded; no CI-swallowing, no gitignored-but-tracked path | `bash .claude/skills/auditor/audit.sh` (§2) |
| 2 | WARN×23 | Committed `data/reports/` and `evidence/` CSVs with no generator reference — pre-existing, all unrelated to S1 | `audit.sh` output, §2 (23 lines) |
| 3 | OK | Seal live SHA `6e2c3888…` matches the freeze records; S1 commits touch no sealed artefact | `make verify-seal`; `docs/preregistration_002.md:8`, `docs/preregistration_003.md:9` |
| 4 | OK | Hinge `span{A_C\|_{E_N}} = Sym(E_N)` genuinely Lean-proved via the real fibers and class sums, and non-vacuous | `SpanTheoremC.lean:438`, `ClassSum.lean:39,43,74`, `FiniteLinearAlgebra.lean:155` |
| 5 | OK | Manuscript makes **no** Lean/formalization/certification claim anywhere; claim mismatch from the Lean work is structurally impossible at HEAD | `grep -niE 'lean\|formaliz\|certif\|mathlib' …manuscript.tex` → 2 false positives (`:91`, `:175`) |
| 6 | OK | Corollary D is only an abstract interface: `[FiniteDimensional ℝ 𝒳]` hypothesis present, S1 instance not built | `AbstractQuotient.lean:24` |
| 7 | OK | Theorem F asymptotics/QMD/Bernstein–Durrmeyer/HS density absent from Lean, as the ledger states | `grep -rniE 'asymptot\|durrmeyer\|qmd\|densit\|hilbert.schmidt'` → 1 docstring hit, `NormVsSOT.lean:6` |
| 8 | OK | `N=2,3,4` Fisher statements are exact finite arithmetic only | `ExactChecks.lean:48,52,60,72,82` |
| 9 | OK | Corollary H logic proved; the `N=2` integrals are hypotheses, not theorems | `CorollaryH.lean:34` (`hw₂`), `ExactChecks.lean:23` |
| 10 | OK | `r_N(γ_ψ)=2` restricted to the single explicit orbit at every occurrence | manuscript `:56,:153,:189,:215,:217,:337` |
| 11 | OK | SOT convergence and `‖F̂_N−Π_sym‖≥1` stated together and correctly | manuscript `:127,:131,:185,:213,:297` |
| 12 | OK | No novelty/priority claim strengthened: manuscript and `.bib` predate every Lean commit | `git log -- …manuscript.tex` → `2bd82cd`; `git log -- …references.bib` → `9f4289b` |
| 13 | OK | Zero `sorry`/`admit`/custom axiom; `#print axioms` clean; `lake build` PASS (4716 jobs) | `grep -rInE` exit 1; `#print axioms` (§4); `lake build` |
| 14 | OK | Bibliography complete and tight: 20 cited, 20 entries, none missing, none unused | auditor cross-check script (§4) |
| 15 | OK | No dev/validation leakage; guardrail scripts import nothing from the repo and feed no Lean proof | §5; `fiber_bruteforce_check.py`, `appendixC_matrix_check.py` |
| 16 | WARN | **Ledger token broader than what is proved.** `THEOREM_C_FINITE_MATRIX_FORM = LEAN_PROVED` names "the finite matrix form of Theorem C", but the manuscript's boxed Theorem C is `V_N = Sym²P_{N-1}` **and** `dim V_N = rank G = C(N,2)`. Only the span equality is a Lean theorem; there is **no** `finrank` theorem for `DCSymM` (`grep -rn finrank` over `S1Paper/` returns only `finrank_EN`). The dimension follows from `edgeLaplacian_linearIndependent` + `DCSymM_eq_sum_edgeLaplacian`, but no Lean term states it. Risk: a future reader or write-up takes the rank half as certified. | `FORMALIZATION_STATUS.md` third-pass status block; `FiniteLinearAlgebra.lean:62` is the only `finrank` |
| 17 | WARN | **Working tree not clean at audit time.** Two uncommitted changes, one of them *inside the audited WP6 scope*: modified `research_program/work_packages/wp6_full_class_sum_rank_theorem.md` (a Discussion TODO about causal compression) and untracked `dev/OCCUPANCY_GENERATING_SYSTEM_3plus1.md`. Neither is part of HEAD `bcbeada`, so neither was audited; the in-scope one could be mistaken for audited content. Its own text already restricts the reading it proposes ("No presentar esta lectura como una afirmación de que el pasado y el futuro determinan universalmente el presente"). | `git status --short` |

AUDIT_ERRORS=0
AUDIT_WARNINGS=25

## 8. Verdict

Zero errors. Twenty-five warnings: the 23 pre-existing, S1-unrelated `data/reports` generator
warnings from the mechanical audit, plus two auditor findings (W-16 ledger token breadth, W-17
unclean working tree). Both auditor warnings are about *labelling and audit hygiene*, not about a
false mathematical claim.

**Claim mismatch: 0.** No sentence of the manuscript states a result more strongly than its
ordinary proof supports, and the manuscript makes no formalization claim at all.
**Formalization mismatch: 0 in the manuscript; 1 imprecision in the ledger** (W-16), where a
summary token is broader than the theorem behind it. **Repo integrity: no new S1-related finding.**

Recommended remediation (auditor does not apply it): narrow the W-16 token, e.g.
`THEOREM_C_FINITE_MATRIX_FORM = LEAN_PROVED (span equality; dimension/rank not stated as a Lean
theorem)`, or add the `finrank (DCSymM N) = N*(N-1)/2` theorem that the two existing results
already imply.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
