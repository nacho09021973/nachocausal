# Auditor Report 039 — wp6-s1-manuscript-v1-post-referee

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit
`f752bab1eb02df4cfa5da4336f6b1c06514dbaa7` (`git rev-parse HEAD`). The audited commit is
`495429b4143d248c38e5161020a4b00250d3b9c2..f752bab1eb02df4cfa5da4336f6b1c06514dbaa7`,
with subject `Revise WP6 S1 manuscript after referee review`.

Trigger: user-requested post-referee scoped integrity audit of
`research_program/synthesis/wp6_s1_finite_causal_order_manuscript.tex`. The scientific focus is
limited to the two repairs introduced by V1:

1. the distinction between Kure\v{c}ka's permutation-level map (T_N) and its restriction through
   the fiber embedding (J_N);
2. the exact Bouvel--Chauve--Mishna--Rossin event and the separate deterministic
   Bouvel/modular-decomposition/Gallai implication used in (E.15).

The downstream chain (E.15)--(E.19), global renumbering, claim ceiling, and correspondence with
the Lean ledger were also checked. The audit is of the frozen HEAD manuscript: its SHA256 is
`a357cdf2b54f6346d0d09aca80499f95b44a78c2c0fa7125d0a69c2c630f659f`, identical for the
worktree file, `HEAD:<path>`, and the named commit's blob.

The pre-existing modified work package and untracked `dev/` note are excluded from scientific
scope and recorded only as W-17 worktree hygiene. The only file this auditor writes is this report;
there is no remediation, commit, or push.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code `0`; verbatim output:

```text
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/auditor/auditor_report_003_bibliography-claims-vs-biblioteca.md,docs/auditor/auditor_report_004_bibliography-followup-verification.md,docs/auditor/auditor_report_005_prereg002-pass-raw-artifact-integrity.md,docs/auditor/auditor_report_006_rvar-mu-freeze-addendum-preflight.md,docs/auditor/auditor_report_007_pr011-viability-freeze-text.md,docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md,docs/auditor/auditor_report_009_pr011-tier1-hellinger-certification.md,docs/auditor/auditor_report_010_pr011-ladder-closure-n6-n8.md,docs/auditor/auditor_report_011_pr011-terminal-semantics.md,docs/auditor/auditor_report_012_pr012-draft-scope-preflight.md,docs/auditor/auditor_report_013_op01-survival-matrix.md,docs/auditor/auditor_report_014_op02-claim-grammar.md,docs/auditor/auditor_report_015_phase1-theory-package.md,docs/auditor/auditor_report_016_phase1-provenance-reaudit.md,docs/auditor/auditor_report_017_op21-terminal-run.md,docs/auditor/auditor_report_018_op21-terminal-second-pass.md,docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md,docs/auditor/auditor_report_020_op22-bd-dossier-rev3-fix-verification.md,docs/auditor/auditor_report_021_truncated-futures-freeze-preflight.md,docs/auditor/auditor_report_022_freeze-commit-scoped-audit.md,docs/auditor/auditor_report_023_ficha-tv-order-only-precommit.md,docs/auditor/auditor_report_024_wp4-annex-c-comparable-pair-separation-precommit.md,docs/auditor/auditor_report_025_wp4-annex-c-remediation-reaudit.md,docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md,docs/auditor/auditor_report_027_wp4-ibar-interval-design-precommit.md,docs/auditor/auditor_report_028_wp4-ibar-executable-contract-precommit.md,docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md,docs/auditor/auditor_report_032_emergencia-viz-figuras-del-fracaso.md,docs/auditor/auditor_report_033_emergencia-viz-remediacion-032-reauditoria.md,docs/auditor/auditor_report_034_emergencia-viz-cierre-e1-y-avisos-033.md,docs/auditor/auditor_report_035_viz-figuras-generales-6-agosto.md,docs/auditor/auditor_report_036_viz-cierre-e1-y-avisos-035.md,docs/auditor/auditor_report_037_wp6-s1-paper-and-lean-evidence.md,docs/auditor/auditor_report_038_w16-closure-verification.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/comite/comite_decision_015_r-var-selector-adjudication.md,docs/comite/comite_decision_016_prereg002-supervised-reverification.md,docs/comite/comite_decision_017_r-var-v2-reconvene.md,docs/comite/comite_decision_018_rvar-mu-empty-family-object-choice.md,docs/comite/comite_decision_019_rvar-partF-execution-feasibility.md,docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md,docs/comite/comite_decision_021_rvar-egs-truncation-object.md,docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md,docs/comite/comite_decision_023_pr012-scope-adjudication.md,docs/comite/comite_decision_024_op02-claim-grammar-adoption.md,docs/comite/comite_decision_025_op02-claim-grammar-reconvene.md,docs/comite/comite_decision_026_op02-claim-grammar-final-adoption.md,docs/comite/comite_decision_027_phase1-theory-package-first-review.md,docs/comite/comite_decision_028_phase1-theory-package-second-review.md,docs/comite/comite_decision_029_phase1-theory-package-third-review.md,docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md,docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md,docs/comite/comite_decision_032_phase1-theory-closure-handoff.md,docs/comite/comite_decision_033_phase1-theory-ready-final-handoff.md,docs/comite/comite_decision_034_op21-certifier-opening.md,docs/comite/comite_decision_035_op22-witness-candidate-adjudication.md,docs/comite/comite_decision_036_pr009-pr010-sequencing-adjudication.md,docs/comite/comite_decision_037_candidate-b-viability-gate-review.md,docs/comite/comite_decision_038_truncated-futures-freeze-adjudication.md,docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md,docs/comite/comite_decision_044_c6-waist-screen-adjudication-review.md,docs/comite/comite_decision_045_candidate-7-1-fixed-n-logical-status.md,docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md,docs/comite/comite_decision_047_phase2-b2-documentation-publication.md,docs/comite/comite_decision_048_q-fmots-target-adjudication.md,docs/comite/comite_decision_049_program-closure-adjudication.md,docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md,docs/comite/comite_decision_051_s1-gate-geometric-tangent-classification.md,docs/hoja_de_ruta_03_jul_2026.md,docs/hoja_de_ruta_24_jul_2026.md,docs/hoja_de_ruta_25_jul_2026.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jul_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/manuscript_limits_draft.md,docs/physical_reentry_audit_001_2026-08-28.md,docs/prereg002_reverification_declaration.md,docs/prereg002_reverification_result.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md,docs/program_closure_note_2026-07-30.md,docs/program_reopening_note_2026-08-28_R4.md,docs/rvar_closure_negative_result.md
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

The warning set is the same pre-existing set recorded in reports 037--038. No warning names an S1
manuscript, Lean, bibliography, outline, work-package, or `dev/` artifact. The repository regression
suite also completes: `make test` gives `441 passed, 1 warning in 407.45s`; the sole warning is the
environmental Matplotlib `Axes3D` import warning in `tests/test_emergencia_viz.py`, unrelated to V1.

## 3. Seal & freeze integrity

- `make verify-seal` and an independent `sha256sum nachocausal/thresholds.py` both give
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
- The same full SHA is recorded in `docs/preregistration_002.md:8` and
  `docs/preregistration_003.md:9`; there is no seal drift.
- `git diff-tree --no-commit-id --name-status -r f752bab` lists one path only, the manuscript.
  The commit changes neither `nachocausal/thresholds.py` nor a freeze record.

## 4. Reproducibility of published numbers

This is a mathematics-manuscript revision, not a new data-result commit. Its changed claims were
traced to source statements and checked algebraically rather than accepted from the new prose.

### 4.1 Commit scope — manuscript only

`git show --stat f752bab` reports `1 file changed, 89 insertions(+), 35 deletions(-)` and
`git diff-tree -r` names only
`research_program/synthesis/wp6_s1_finite_causal_order_manuscript.tex`. A path-limited diff from
the parent over `formal/`, the bibliography, the outline, `docs/auditor/`, work packages, and
`dev/` returns zero paths. Lean evidence, bibliography, outline, audit history, work packages, and
`dev/` are therefore unchanged by V1.

### 4.2 Kure\v{c}ka positioning

Primary source checked: M. Kure\v{c}ka, *Lower bound on the size of a quasirandom forcing set of
permutations*, CPC 31 (2022), DOI
[`10.1017/S0963548321000298`](https://doi.org/10.1017/S0963548321000298), Cambridge PDF SHA256
`1603e0e1c8f83d0b319f02a41ce84f4723ad351f88b2326dd2011673651ee2b3`.

- On printed p. 312, the vectors (b_2,ldots,b_N) span (mathbf1^perp), and Lemma 9 states
  (c_{ij}(P_\pi)=K_{ij}b_{i+2}^{T}A_\pi b_{j+2}), with (K_{ij}\ne0) for the full coefficient
  range. Therefore a same-order linear combination of gradient polynomials is zero iff all matrix
  coefficients on (E_N\times E_N) vanish.
- Every linear combination (M(t)=\sum_\pi t_\pi P_\pi) has constant row and column sum
  (s=\sum_\pi t_\pi), so (E_N) is invariant. Hence the preceding bilinear vanishing is exactly
  (T_N(t)=M(t)|_{E_N}=0). This proves the manuscript's (8.1),
  `ker(gradient-polynomial map) = ker T_N`.
- Lemma 12 (printed p. 315), using Lemma 11, says that if a same-order combination of gradient
  polynomials is zero, its cover matrix is constant. Conversely, a constant matrix kills (E_N),
  and Lemma 9 kills every coefficient. Thus the manuscript's constant-cover-matrix characterization
  is accurate; it does not silently generalize across mixed permutation orders.
- A full-text search of the source for `poset`, `fiber`/`fibre`, `isomorph`, `unlabeled`, and
  `class sum` returns no occurrence. More importantly, the source contains no fiber embedding
  (J_N) and no restricted-image calculation. From rank--nullity,
  
  \[
  \operatorname{rank}(T_NJ_N)=\dim(\operatorname{im}J_N)
  -\dim(\operatorname{im}J_N\cap\ker T_N),
  \]
  
  so knowledge of the ambient kernel does not determine that intersection or
  (T_N(\operatorname{im}J_N)). V1 states this distinction explicitly at manuscript
  `:37--59` and `:189--208`.

Kure\v{c}ka is credited for the ambient differential, Bernstein basis, compression, cover matrix,
and kernel. V1 claims only that the near-chain argument supplies the reverse inclusion after the
fiber restriction. The priority language remains conservative (`:61`, `:208`, `:246`): absence of
an exact counterpart is not called a novelty certificate. Therefore
`KURECKA_POSITIONING=PASS` and `KURECKA_PRIORITY_GATE=CLOSED_NOT_REFUTED`.

### 4.3 External event in (E.15)

Primary source checked: M. Bouvel, C. Chauve, M. Mishna, D. Rossin, *Average-case analysis of
perfect sorting by reversals*, CPM 2009, author-hosted proceedings PDF
[`CPM09.pdf`](https://www.cecm.sfu.ca/~cchauve/Publications/CPM09.pdf), SHA256
`4b401a95588a1ccfc30697ab5f95626c8b79b226177563582493342deb576290`.

- The source defines a twin as a degree-two strong-interval-tree vertex with two leaf children,
  and notes that it is linear.
- Its Theorem 2 states precisely that, asymptotically with probability one, the strong interval
  tree has a prime root and every root child is a leaf or a twin.
- The proof immediately following Lemma 1 applies that lemma with (c=1): the proportion of
  non-simple permutations having a common interval of size at least three is (O(n^{-1})), and
  the source then identifies the complement exactly with the prime-root/leaves-or-twins shape.
  Therefore the stronger quantitative form used by V1,
  (\mathbb P(\mathcal G_N^c)=O(N^{-1})), is supported by the proof, not inferred merely from
  the words "with probability one".
- Remark 1 identifies the strong interval tree of an unsigned permutation with the modular
  decomposition tree of its labeled permutation graph. V1 correctly avoids the false earlier
  replacement of this event by "the whole incomparability graph is prime" and explicitly allows
  twins (`:330`).

Thus `E15_EXTERNAL_EVENT_MATCH=PASS`.

### 4.4 Deterministic fiber implication

The proof at manuscript `:332--341` was checked independently of the probability estimate.

1. For (P_\pi), the permutation/inversion graph is its incomparability graph: two elements are
   adjacent exactly when the identity and (\pi)-orders disagree. A poset isomorphism therefore
   induces an isomorphism of these graphs.
2. Strong modules are canonical under graph isomorphism. The bridge to the strong interval tree is
   not an assumption invented by V1: Habib--Paul, *A survey of the algorithmic aspects of modular
   decomposition*, CSR 4 (2010), [Lemma 20, author PDF](https://www.irif.fr/~habib/Documents/HP10.pdf),
   states that for a permutation graph a set is a strong module iff it is a strong common interval
   of the two realizing permutations; the same passage says their trees are isomorphic. The checked
   PDF has SHA256 `054b3f7daa9ea4eb89e4799957bf0e8dec34e75fd31762e139543dcd2ec34dc4`.
3. On (\mathcal G_N), maximal proper strong modules are exactly the root children and have size
   one or two. Their contraction gives the prime quotient (\alpha); an isomorphism preserves
   module size and induced poset type, so it gives an isomorphism of the contracted quotient posets.
4. Gallai's consequence used here is exact: a prime comparability graph has precisely two
   transitive orientations, one the reverse of the other. The original citation is T. Gallai,
   *Transitiv orientierbare Graphen*, Acta Math. Acad. Sci. Hung. 18 (1967), 25--66,
   [DOI](https://doi.org/10.1007/BF02020961), §§(1.8)--(1.10). It is independently restated with
   attribution in Klav\'ik--Zeman, *Automorphism Groups of Comparability Graphs*,
   [arXiv:1506.05064](https://arxiv.org/abs/1506.05064), §3; checked PDF SHA256
   `5a4a7e3908f6633425d0049f23f32a42d24c438dc2ef5dd166e4c46a46d31153`.
5. Applying that uniqueness to the incomparability graph's two transitive orientations while the
   quotient-poset orientation is fixed leaves only the original ordered realizer pair or its swap.
   Rank normalization gives quotient permutation (\alpha) or (\alpha^{-1}); arbitrary quotient
   automorphisms are already included in the transported isomorphism and cannot create a third
   orientation.
6. Internally, the permitted patterns are (1,12,21). The two size-two patterns induce respectively
   a chain and an antichain, so a poset isomorphism cannot exchange them. The standard identity
   
   \[
   \bigl(\alpha[\tau_1,\ldots,\tau_m]\bigr)^{-1}
   =\alpha^{-1}[\tau_{\alpha^{-1}(1)}^{-1},\ldots,
                  \tau_{\alpha^{-1}(m)}^{-1}]
   \]
   
   then gives (\pi^{-1}) in the swapped case, since all three internal patterns are involutions.
   An internal relabeling of a two-element antichain changes names, not the normalized numeric
   pattern. The set notation in (E.15) correctly removes multiplicity when (\pi=\pi^{-1}).

No hidden assumption about independent twin flips survives this check, and the
comparability/incomparability roles are consistent. The manuscript gives a compressed proof rather
than re-developing modular decomposition, but every invoked bridge is exact and sufficient.
Therefore `E15_DETERMINISTIC_FIBER_ARGUMENT=PASS`.

### 4.5 (E.15) through Fisher retention

- (\mathcal G_N) is measurable with respect to the unlabeled poset because it is an isomorphism
  property of the canonical modular decomposition of the poset's incomparability graph.
- For symmetric (f), (H^{(N)}(f)) is symmetric, so the rank-permutation score has the same value
  at (\sigma) and (\sigma^{-1}). The conditional variance in (E.10) is therefore zero on every
  fiber in (\mathcal G_N), including singleton involution fibers.
- Measurability and conditional variance give
  (0\le\Delta_N(f,f)\le\mathbb E[S_N^\Pi(f)^2\mathbf1_{\mathcal G_N^c}]). Combining
  (\mathbb P(\mathcal G_N^c)=O(N^{-1})) with (E.14),
  (\mathbb E[S_N^\Pi(f)^4]=o(N^3)), gives (E.16), (\Delta_N(f,f)=o(N)), by
  Cauchy--Schwarz.
- The uniform bound (E.17) and the fixed-rank-first approximation (E.18) extend the result to the
  symmetric Hilbert--Schmidt closure in (E.19). Combined with the separately established rank-law
  limit (E.9), this is exactly the Fisher-retention portion of Theorem 4.

No uniform rate, operator-norm convergence, or stronger typical-fiber event is inferred.
`THEOREM4_RETENTION_CHAIN=PASS`.

### 4.6 Lean/formalization boundary

The operative ledger at
`formal/HorizonFormal/HorizonFormal/S1Paper/FORMALIZATION_STATUS.md:268--291` says:

```text
THEOREM_C_CLASS_SUM_SPAN            = LEAN_PROVED
THEOREM_C_CLASS_SUM_SPAN_DIMENSION  = LEAN_PROVED
THEOREM_C_GRAM_RANK                 = NOT_FORMALIZED
BERNSTEIN_TRANSPORT_TO_VN           = NOT_FORMALIZED
THEOREM_C_FINITE_MATRIX_FORM        = RETIRED
```

This matches the Lean sources: `span_classSum_restr_eq` is at `SpanTheoremC.lean:441`,
`finrank_DCSymM` at `:512`, and `finrank_span_classSum_restr` at `:526`. There is no Lean object for
the Fisher/Gram rank or the Bernstein transport. The V1 commit changes no path under `formal/`, and
the manuscript makes no Lean/formalization/certification statement; the two textual matches from a
broad search are only `Laplacian` (`:113`) and `mechanisms` (`:216`). Kure\v{c}ka adjudication,
QMD/Bernstein transport, Fisher asymptotics, and the repaired Bouvel/Gallai implication remain
ordinary mathematical/source arguments, not machine-certified claims.

`lake build` completes successfully with `Build completed successfully (4716 jobs)`; a corrected
source-path search finds zero `sorry`, `admit`, project `axiom`, `sorryAx`, or `postulate` in the S1
Lean modules. The build's existing linter warnings are unchanged and do not alter the ledger.
Accordingly `V1_FORMALIZATION_MISMATCH=0`.

### 4.7 Renumbering and TeX/static integrity

- Result headings occur globally in the requested sequence: Theorem 1 (`:107`), Corollary 2
  (`:117`), Corollary 3 (`:127`), Theorem 4 (`:145`), Theorem 5 (`:163`), Corollary 6 (`:173`).
- Searches for stale `Theorem C`, `Corollary D/E`, `Theorem F/G`, and `Corollary H` return no hit.
- (J_N) is used only for the fiber embedding (`:40--56`, `:107`, `:189--205`); the quotient
  isomorphism is (U_N) (`:127--129`, `:308`). There is no collision.
- Citation cross-check: 20 cited keys, 20 bibliography entries, none missing and none unused.
- There are 204 equation tags, zero duplicates, and all 52 distinct parenthesized equation
  references resolve to an existing tag. `begin`/`end` multisets match, brace depth finishes at
  zero, and `git diff --check HEAD^ HEAD` passes.
- No `latexmk`, `pdflatex`, `lualatex`, `xelatex`, or `tectonic` executable is installed. A real
  TeX/PDF compilation was therefore not performed. This is an outstanding presentation check, not
  a mathematical or static-error finding.

Thus `RENUMBERING=PASS`, `TEX_STATIC_CHECK=PASS`, and `PDF_COMPILED=NO`.

## 5. dev/validation separation & ground-truth leakage

The V1 commit changes one prose/math manuscript only. It reads no data, validation seed, hidden
embedding, threshold, or `dev/` artifact and cannot create a leakage path. `audit.sh` reports no
gitignored-but-tracked contradiction. The frozen validation path and the `formula` branch were not
run, edited, checked out, committed, or pushed.

W-17 remains separate: before this report was written, `git status --short` showed modified
`research_program/work_packages/wp6_full_class_sum_rank_theorem.md` and untracked
`dev/OCCUPANCY_GENERATING_SYSTEM_3plus1.md`. Neither path is in `f752bab`; neither was used as
evidence for a V1 claim or modified by the auditor. This new report is the expected sole audit
output and is intentionally uncommitted.

## 6. Claim-boundary check

The V1 claim ceiling is explicit and internally consistent:

- S1, (1+1), local/differential, independent reference: manuscript `:27`, `:35`, `:68`, `:238`.
- No finite-distance/global/nonlinear reconstruction or arbitrary geometric realizability:
  `:63`, `:93`, `:131`, `:153`, `:230--242`, `:274`, `:312`, `:351`.
- Strong-operator, pointwise retention rather than operator-norm or uniform convergence:
  `:147--151`, `:226`, `:244`, `:254`, `:351`.
- (r_N=2) only for the explicit antisymmetric orbit, never the whole antisymmetric sector:
  `:74`, `:159--177`, `:216`, `:230`, `:242`, `:256--258`, `:393`.
- Priority remains `PRIORITY_NOT_REFUTED`, not an affirmative novelty certificate: `:61`, `:208`,
  `:246`.

No sentence crosses the requested scope boundary. `SCOPE_CEILING=PASS` and
`V1_CLAIM_MISMATCH=0`.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | Mechanical auditor exits 0 with zero errors | `bash .claude/skills/auditor/audit.sh` (§2) |
| 2 | WARN×23 | Same pre-existing committed data files without generator references; none belongs to the S1 track | Verbatim `audit.sh` output (§2) |
| 3 | OK | Seal hash matches both binding preregistrations; no drift | `make verify-seal`; `docs/preregistration_002.md:8`, `003.md:9` |
| 4 | OK | V1 commit changes only the manuscript; Lean, bib, outline, audit history, work packages, and `dev/` untouched | `git diff-tree -r f752bab`; parent-scoped path diff (§4.1) |
| 5 | OK | Kure\v{c}ka Lemma 9 plus the (E_N) basis gives `ker gradient = ker T_N`; Lemma 12 supports constant cover matrix | Kure\v{c}ka DOI, pp. 312, 314--315; manuscript `:189--194` |
| 6 | OK | Ambient-kernel result does not determine the restricted image through (J_N); priority ceiling remains conservative | manuscript `:37--61`, `:196--208`, `:246`; source full-text search |
| 7 | OK | Bouvel et al. Theorem 2 and Lemma 1 with (c=1) give exactly the V1 event with (O(N^{-1})) complement | CPM09 Theorem 2 and its proof; manuscript `:330` |
| 8 | OK | Canonical modules, contraction, Gallai uniqueness, rank normalization, and involutive internal patterns suffice for the exact two-element fiber | manuscript `:332--341`; Habib--Paul Lemma 20; Gallai (1.8)--(1.10) |
| 9 | OK | (E.15) is precisely sufficient for (E.16), and (E.17)--(E.19) preserve the stated Theorem 4 ceiling | manuscript `:343--351` |
| 10 | OK | Renumbering, (J_N/U_N) separation, citations, equation references, environments, braces, and whitespace checks pass | §4.7 commands |
| 11 | OK | Scope ceiling passes: S1/1+1/local, SOT not norm, explicit orbit only, no reconstruction/novelty certificate | manuscript anchors in §6 |
| 12 | OK | Lean ledger remains exact; new external-source arguments are not represented as Lean-certified | `FORMALIZATION_STATUS.md:268--291`; manuscript formalization search |
| 13 | OK | Lean build and repository tests pass | `lake build` → 4716 jobs; `make test` → 441 passed |
| 14 | OK | TeX static checks pass; PDF compilation correctly remains unperformed because no engine is installed | §4.7 tool and static-check outputs |
| 15 | WARN | W-17 carried forward as pre-existing worktree hygiene, separate from V1 correctness; no remediation performed | `git status --short` before report write (§5) |

AUDIT_ERRORS=0
AUDIT_WARNINGS=24

## 8. Verdict

The two post-referee repairs are exact. Kure\v{c}ka is neither under-credited nor made to imply the
fiber-restricted image theorem; Bouvel's actual typical event supplies the stated (O(N^{-1}))
exceptional probability, while the separate deterministic modular/Gallai argument supplies the
fiber equality needed for Fisher retention. There is no claim or formalization mismatch.

The 24 warnings are the 23 pre-existing mechanical data-generator warnings plus W-17. None is a V1
scientific defect. Lack of a local TeX engine is recorded as an outstanding compilation control and
is not counted as an audit warning or mathematical error.

```text
V1_CLAIM_MISMATCH=0
V1_FORMALIZATION_MISMATCH=0
KURECKA_POSITIONING=PASS
KURECKA_PRIORITY_GATE=CLOSED_NOT_REFUTED
E15_EXTERNAL_EVENT_MATCH=PASS
E15_DETERMINISTIC_FIBER_ARGUMENT=PASS
THEOREM4_RETENTION_CHAIN=PASS
RENUMBERING=PASS
SCOPE_CEILING=PASS
TEX_STATIC_CHECK=PASS
PDF_COMPILED=NO
AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
AUDIT_ERRORS=0
AUDIT_WARNINGS=24
```

No scientific remediation is recommended before the final adversarial referee pass. The remaining
technical publication control is a real TeX build and PDF inspection in a clean external build
directory.
