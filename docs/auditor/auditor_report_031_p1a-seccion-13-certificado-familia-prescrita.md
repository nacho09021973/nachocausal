# Auditor Report 031 — p1a-seccion-13-certificado-familia-prescrita

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, HEAD `8af8f40`
(pushed, in sync with `origin/emergencia/p1a-canal-sigma-m`).

Target, per the invoking scope hint: §13 of `emergencia/P1a_puerta_teorica_en_Minkowski.md`
(commits `2ae955b`, `26b5397`, `dbeb5da`) and the documentation commit `8af8f40`
(`docs/bibliography_claims.md` entries 1.3 and 2.5bis, `docs/manuscript_limits_draft.md`).

Four focus questions were set: (1) traceability of the `SSW`/`SST`/`T_emp` figures in
Advertencia 13.16; (2) whether the `PROVED` labels in the §13.7 flag table over-claim, in
particular `PRESCRIBED_BAND_UNIQUENESS_CERTIFICATE` and `GLOBAL_DISCREPANCY_LEMMA`;
(3) whether every `file:line` citation in §13 and in the new dossier entries resolves to the
content attributed to it; (4) whether `EMPTY_FRAME_UNIQUENESS_CERTIFICATE = SUPERSEDED` erases a
prior `OPEN` without a note.

**Independence limitation, stated up front and not mitigated.** §13 was authored in the same
session that produced this audit, by the same agent. This audit therefore has genuine force only
on the *mechanically checkable* surface: number provenance, citation resolution, flag consistency,
claim boundary. It has **no** independent force on the mathematical correctness of the proofs.
Everything in that category is listed in §7 as `NOT VERIFIED` rather than `OK`, and the verdict
below should not be read as mathematical endorsement.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code `0`:

```text
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,[…78 further freeze/decision records elided for length…],docs/rvar_closure_negative_result.md
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

The 23 warnings are pre-existing and lie entirely outside the audited scope (`data/reports/`,
`evidence/`); none is introduced by the audited commits. They are carried into the count per the
skill's counting rule, not because §13 caused them.

## 3. Seal & freeze integrity

`make verify-seal` prints
`thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.

That value is the one named in the current freeze record at
`docs/preregistration_003.md:9` and, for the prior stage, `docs/preregistration_002.md:8`. No
drift. The audited work does not touch `nachocausal/thresholds.py` and does not enter the sealed
path.

Separately, the sealed input consumed by the figures audited in §4 is intact:
`emergencia/resultados/p1a_representaciones_intervalos_d2.csv` hashes to
`5110688b89142bf06e738a6f66bb41fa7c248e29352392b8bc763480ebd3ab08`, matching its committed
`.sha256` sidecar byte for byte, and `git status --porcelain` reports it unmodified.

## 4. Reproducibility of published numbers

**Traceable and reproduced.** `emergencia/p1a_count_volume_canal_sigma_m_d2.py` is committed
(first at `0992277`), declares at its head that it reads the sealed CSV and
"No genera aleatoriedad, no remuestrea, no escribe en `resultados/`", and emits its table to
stdout. Re-running it (`python3 emergencia/p1a_count_volume_canal_sigma_m_d2.py`, read-only, no
sealed validation path entered) reproduces the BLOQUE A table of
`emergencia/P1a_count_volume_canal_sigma_m_d2.md:109-114` **exactly**, to all six printed
decimals, together with `BLOQUE_A_CONSISTENCIA = PASS` and
`CV4_SEALED_SAMPLE_STATUS = GATE_EXCLUDED_EXACTLY`.

**The figures re-used in Advertencia 13.16 are arithmetically correct.** Checking the derived
columns against the reproduced output: `19.724621/7014 = 2.812e-3`, `29.117250/7014 = 4.151e-3`;
`15.173923/7918 = 1.916e-3`, `21.147076/7918 = 2.671e-3`; `11.281520/8334 = 1.354e-3`,
`16.128481/8334 = 1.935e-3`. All six match the rounded values printed in §13.16, and `T_emp` and
`rho_max_emp` are transcribed verbatim.

**But the transcription is selective and unlabelled (W1).** The sealed table has **six** strata
(`futuro`/`pasado` × `n ∈ {64,96,128}`, lines 109-114). The §13.16 table has three rows, no
`lado` column, and no stated selection rule; the values are the `futuro` rows throughout. The
`pasado` rows carry different figures (`T_emp` 0.6773, 0.7041, 0.7139). The scientific conclusion
drawn — that the ratio is flat while numerator and denominator both decay — holds on all six
strata, so the claim is not damaged; the transcription is nonetheless not faithful to the source
table and a reader cannot tell which half was used.

**Population/sample conflation (W2).** §13.16 writes "`SSW = E[Var(ell|M)]`". `SSW` is the
empirical within-level-set sum of squares on one sealed sample; `E[Var(ell|M,n,h,S)]` is the
population quantity `P_{1,n}+P_{2,n}`. The identification is legitimate as an estimate — the
script's own controls confirm the bins are the level sets of `M` (`biyectiva=True`,
`monotona=True`, `media_bin_alcanza_rho_max=True`) — but it is stated as an equality.

**Rounding, noted not charged.** §13.16 and the §13.7 flag table describe the ratio as
"`0.68-0.72`". The true BLOQUE A range is `[0.6773, 0.7175]`. The quoted interval is the correct
two-decimal rounding and does not mislead; a tighter statement would be `0.677-0.718`.

**Citation anchor imprecision (W5).** §13.16 cites the sealed table as
`P1a_count_volume_canal_sigma_m_d2.md:104-113`. The table rows are at **109-114**: the cited range
opens on five lines of preceding prose and omits the final row (`128 | pasado`). The Lema 3 anchor
in the same paragraph, `:65-73`, resolves correctly.

## 5. dev/validation separation & ground-truth leakage

No finding. §13 is a analytical text; it introduces no script, no seed, no ensemble, and no
threshold. The one script executed during this audit is read-only by its own declaration and was
run only to reproduce an already-published table, not to generate a new number. `emergencia/` is
tracked (70 files under `git ls-files emergencia/`) and is a separate line from the sealed
PR003 estimator; nothing in the audited commits touches `nachocausal/`, `dev/`, or any frozen
artefact.

Ground-truth usage: §13 reasons about a planted quadruple inside a prescribed family of
permutations. The planting is a construction internal to the probability argument, not an
estimator that consults a hidden embedding; the selector under analysis
(`MIN_COVERAGE_LEX`/`MIN_ONLY`) is the frozen, embedding-blind one from
`P1a_contrato_comparacion_selectores_balanceados_d2.md:47-58`. No leakage path found.

## 6. Claim-boundary check

The audited commits **improve** the claim boundary rather than stress it, and this is the
strongest positive finding of the audit.

`dbeb5da` adds Advertencia 13.16, which explicitly blocks the inference from
`P_{1,n}+P_{2,n} → 0` to recoverability, and states: "Ningún texto de este repositorio debe
encadenar `P_{1,n}->0` y `P_{2,n}->0` con la conclusión «reconstrucción consistente» sin exhibir
además `Var(ell|n,h,S)`". `8af8f40` propagates the `d≥3` scope of Braun (arXiv:2507.01907, p.2)
and the `d>2` scope of Madsen (arXiv:2607.05840, Thm 4.18) into
`docs/manuscript_limits_draft.md`, where both were previously cited as background without a
dimensional caveat, and records in `docs/bibliography_claims.md` §1.3 that Braun's theorem
consumes the full adjacency matrix at all `k` and supplies no estimator, rate, or finite-`n` risk
bound.

`emergencia/P1a_puerta_teorica_en_Minkowski.md:1494-1497` (OPEN item 5) explicitly declines to
claim transfer to 3+1D and records the question as unexamined. No text in the audited range
claims metric reconstruction, an asymptotic event horizon, 3+1D coverage, or a PASS coerced from
an abstain.

**One over-claim mechanism found (W3).** `GLOBAL_DISCREPANCY_LEMMA = PROVED`
(`:1457`) rests on step (b) of Lemma 13.10, which invokes Hoeffding (1963) §6 for the convex-order
domination of sampling without replacement. `find biblioteca -iname "*hoeffding*"` returns
nothing: the source is **not** in the local library and was not read this session. The founding
rule accepts a citation as backing, so this is not a rule breach; but `docs/bibliography_claims.md`
§1.1 sets the repo's own precedent of appending `[UNVERIFIED against primary sources]` when a
load-bearing claim rests on a source not actually read, and §13 carries no such marker while
asserting `PROVED`.

**One internal tension found (W4).** The §13.7 flag table row "plantada en el máximo del paisaje
libre | `PROVED` | `u=v=1/2` exacto (par); producto exacto (impar)" asserts proof for the odd
case, while §13.8 OPEN item 3 (`:1489-1492`) concedes that Def. 13.2's auxiliary prescriptions are
"descritas" rather than listed and that the count `2ρ+5` is not yet "comprobable línea a línea".
A `PROVED` label should not rest on bookkeeping the same document declares not yet checkable.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | ERROR | Two live, contradictory values for the same flag family in one file, in machine-readable blocks. §12.8 still asserts `SUBEXPONENTIAL_UNIQUENESS_COROLLARY = OPEN`, but §13.14 proves `Pr(S) ≥ e^{-o(n)}` and §13.7 asserts `SUBEXPONENTIAL_LOWER_BOUND_ON_PR_S = PROVED` — the §12.8 value is now false, not merely stale. Likewise `EMPTY_FRAME_UNIQUENESS_CERTIFICATE = OPEN` vs `= SUPERSEDED`. The supersession is explained in §13.7 prose but the §12.8 block carries no forward pointer, so any grep-based flag read returns a contradiction. | `emergencia/P1a_puerta_teorica_en_Minkowski.md:901,904,905` vs `:1458,1464,1470-1473` |
| 2 | WARN | Advertencia 13.16 transcribes only the `futuro` half of a six-stratum sealed table, with no `lado` column and no stated selection rule. Values verified correct; faithfulness of transcription is not. | `emergencia/P1a_puerta_teorica_en_Minkowski.md` §13.16 table vs `P1a_count_volume_canal_sigma_m_d2.md:109-114` |
| 3 | WARN | `SSW` stated as an equality with the population quantity `E[Var(ell|M)]` rather than as its empirical estimate on one sealed sample. | `emergencia/P1a_puerta_teorica_en_Minkowski.md` §13.16, "con `SSW = E[Var(ell|M)]`" |
| 4 | WARN | `GLOBAL_DISCREPANCY_LEMMA = PROVED` rests on Hoeffding (1963) §6, which is absent from `biblioteca/` and unread this session, with no `[UNVERIFIED]` marker — contrary to the precedent set for HKMM. | `:1457`, Lemma 13.10 step (b); `find biblioteca -iname "*hoeffding*"` → empty; precedent `docs/bibliography_claims.md:76-78` |
| 5 | WARN | Odd case labelled `PROVED` in the flag table while OPEN item 3 declares its count not yet line-by-line checkable. | `emergencia/P1a_puerta_teorica_en_Minkowski.md:1439` vs `:1489-1492` |
| 6 | WARN | Citation anchor `canal_sigma_m_d2.md:104-113` is off: the table is at 109-114; the range starts on prose and omits the last row. | `emergencia/P1a_puerta_teorica_en_Minkowski.md` §13.16 |
| 7 | OK | Seal intact; live SHA `6e2c3888…` matches `docs/preregistration_003.md:9`. | `make verify-seal` |
| 8 | OK | Sealed input CSV unmodified and matching its committed `.sha256`. | `sha256sum emergencia/resultados/p1a_representaciones_intervalos_d2.csv` |
| 9 | OK | Sealed table reproduced bit-for-bit from the committed deterministic script; derived columns in §13.16 arithmetically correct. | `python3 emergencia/p1a_count_volume_canal_sigma_m_d2.py` |
| 10 | OK | Selector-semantics and counting-convention citations in §13 all resolve as attributed. | `experimento_condicionado_d2.md:162`; `p1a_enumeracion_simulacion.py:174-178`; `resultados_comparacion_selectores_balanceados_d2.md:133-141`; `contrato_comparacion_selectores_balanceados_d2.md:36`; `lema_kl_d2.md:475-477,563-565,592` |
| 11 | OK | Claim boundary strengthened, not stressed: 13.16 blocks the absolute-risk→recoverability inference; `8af8f40` propagates the `d≥3`/`d>2` scope of Braun and Madsen into the manuscript; 3+1D transfer explicitly declined. | `:1389-1428`, `docs/manuscript_limits_draft.md` §3.1/§6.1, `:1494-1497` |
| 12 | OK | No dev/validation leakage and no ground-truth path; §13 introduces no script, seed, ensemble, or threshold. | §5 above |
| 13 | NOT VERIFIED | Mathematical correctness of Lemmas 13.5, 13.7, 13.8, 13.9, 13.11 and Proposition 13.12 — including the exact `N/2` free-row/column count and the exhaustiveness of the trichotomy. Authored in the session that produced this audit; no independent check performed. This is the load-bearing content of `PRESCRIBED_BAND_UNIQUENESS_CERTIFICATE = PROVED`. | `emergencia/P1a_puerta_teorica_en_Minkowski.md` §§13.2-13.5 |
| 14 | NOT VERIFIED | Page-level citations to Braun and Madsen in the new dossier entries derive from an alphaXiv read in this session, not from a page-by-page check against the local PDFs. | `docs/bibliography_claims.md` §1.3, §2.5bis |

AUDIT_ERRORS=1
AUDIT_WARNINGS=28

## 8. Verdict

One error and twenty-eight warnings (23 pre-existing mechanical, 5 raised here). The error is a
flag-consistency defect, not a fabricated result: no number in scope failed its generator, the
seal is intact, and the claim boundary was tightened rather than breached. It is nonetheless a
real failure of the flag discipline the repo depends on, since one live value is now false.

Recommended remediation, for the user to apply or decline — the auditor does not act: annotate the
§12.8 flag block as superseded with a forward pointer to §13.7 (finding 1); label the stratum in
the §13.16 table or restore all six rows (2); soften the `SSW` equality to an estimate (3); add an
`[UNVERIFIED]` marker on the Hoeffding step or acquire the source (4); reconcile the odd-case label
with OPEN item 3 (5); correct the anchor to `:109-114` (6).

Findings 13 and 14 are not remediable by any audit run in this session. The mathematical core of
§13 requires an adversarial reading in an independent session — the falsifier role of `/comite` —
before `PRESCRIBED_BAND_UNIQUENESS_CERTIFICATE = PROVED` is cited anywhere outside this file.

AUDIT_VERDICT=AUDIT_FAIL
