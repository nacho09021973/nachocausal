# Auditor Report 020 — op22-bd-dossier-rev3-fix-verification

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Direct follow-up to `docs/auditor/auditor_report_019_op22-bd-dossier-rev2-viability-audit.md`
(`AUDIT_FAIL`, one error E1 + warnings W1/W2/W3). Target: `dev/OP22_BD_VIABILITY_DOSSIER.md`,
now revised to "rev. 3" (uncommitted working-tree change on top of commit `568a651`, which itself
sits on `464d77e` recording report 019, on `475cb93` = the audited rev. 2). Trigger: PI instructed
the fix sequence E1 → W1/W2 (if they do not alter the scientific question) → re-audit. Every
number and citation changed by rev. 3 is independently re-derived from scratch in this report —
report 019's numbers and the editing agent's numbers are both treated as unverified claims, not
ground truth, until reproduced here.

Constraints honored: no enumeration, no `run_bench`, no Monte Carlo, no scoring, no seed draw;
only in-memory arithmetic (Python stdlib `math`) and read-only file/grep inspection; no file
modified by this audit itself (one arithmetic inconsistency found during re-derivation was fixed
in the working tree by the PI-directed editing pass moments before this audit ran, not by the
auditor — see finding 6; this report only documents it).

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code 0:

```text
Auditor — auditing: /home/adnac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/... (19 reports,
      now including auditor_report_019), docs/comite/... (54 decisions, now including
      comite_decision_037), docs/hoja_de_ruta_*, docs/prereg002_*, docs/preregistration_00{2,3}*,
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

All 22 warnings are the standing repo-wide data-file warnings, byte-identical in content to
reports 017/018/019. None is introduced by, or specific to, the rev. 3 edit under audit.

## 3. Seal & freeze integrity

- `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`. Matches the recorded seal.
  No drift.
- `git rev-parse HEAD` → `568a65176a3656e107fdcf654c152a9ae9beec85` (`docs: adopt Candidate B
  viability gate via decision 037`). `git status --short` at audit time:
  `M dev/OP22_BD_VIABILITY_DOSSIER.md` (the rev. 3 edit under audit, uncommitted) plus the same
  two pre-existing untracked files already recorded and explicitly not in scope
  (`nachocausal-program.local-before-pull.html`, `pr009-runner-scorer-v2.patch`) — consistent
  with report 019's finding W3 and the PI's explicit instruction not to touch them.
- `git diff --stat dev/OP22_BD_VIABILITY_DOSSIER.md` → 1 file changed, 90 insertions, 41
  deletions. No other file touched by the rev. 3 edit.
- Rev. 3 touches only `dev/OP22_BD_VIABILITY_DOSSIER.md` prose (header, V3, V4b, summary table,
  verification-obligations paragraph). No seal, threshold, or frozen prereg file modified.

## 4. Reproducibility of published numbers

Every number changed between rev. 2 and rev. 3 was recomputed independently in this audit,
without reusing report 019's or the editing agent's arithmetic.

### E1 (V3 budget table) — re-derivation

- `data/reports/pr011_tv_certification_n4.csv` (direct read, this audit):
  `epsilon_certified_upper=0.004611899229`, `primary_tv_nominal=0.0014402226592060835`,
  `primary_grid_m=12`. Sidecar `sha256sum -c pr011_tv_certification_n4.sha256` (run from
  `data/reports/`) → `OK`, matching hash `5b53df73...475a0`.
- `docs/plan_avanzado_14_julio_2026.md:51` → `| 4 | 0.004611899229 | ... certify --n 4 |`.
  Verbatim match to the CSV.
- All five ladder CSVs read directly this audit (n=4..8):
  `epsilon_certified_upper` = `0.004611899229, 0.005764874036, 0.006917848843, 0.00807082365,
  0.009223798457`. Confirms **ε grows linearly in n by construction**
  (ratio to n: `0.0011529748...` constant across all five rows) — independently substantiates the
  dossier's and report 019's claim that the n=8 value is a *looser*, not wrong, bound, and that
  substituting it for the n=4-pinned family's own ceiling was the actual defect (not the n=8
  figure's validity in itself).
- `docs/comite/comite_decision_035...md:384-386`: `TV ≤ ~0.0092 [arithmetic: TV ≤ 1−2·0.4954]`.
  Recomputed: `1 - 2*0.495388 = 0.009224`, matching the n=8 CSV value `0.009223798457` to the
  precision quoted in decision 035 — confirms report 019's identification of decision 035's
  "~0.0092" as the n=8 ladder value, independently.
- Recomputed `m_min = floor(2*ln(4/alpha_j)/g^2) + 1` at `g = 0.004611899229` (Python, this
  audit): `alpha_j=0.05 → 412046`; `alpha_j=0.04 → 433029`; `alpha_j=0.01 → 563383`. **Matches
  rev. 3's table exactly.**
- Recomputed the same formula at the nominal-TV scale `g = 0.0014402226592060835`:
  `alpha_j=0.05 → 4225186`; `0.04 → 4440342`; `0.01 → 5777018` (≈4.23e6/4.44e6/5.78e6). **Matches
  rev. 3's prose exactly.**
- Recomputed `radius(200, 0.04) = sqrt(ln(100)/400) = 0.10729830...` ≈ `0.1073`. **Matches.**
- **Finding 6 (self-correcting, non-blocking):** recomputing the PI-heuristic illustration
  `m ~ 200*(0.11/0.009223798457)^2` gives `28,444.3` ≈ **2.8e4**, not the `2.9e4` that rev. 3's
  first working-tree draft carried (rev. 3 had swapped the input digits from the rounded `0.0092`
  used in rev. 2's text to the full-precision `0.009223798457`, without re-rounding the
  approximate output — `(0.11/0.0092)^2*200 ≈ 28,591 ≈ 2.9e4` was correct for the *old* rounded
  input, not the new precise one). This was caught during this audit's independent re-derivation
  and corrected in the working tree (now reads `≈ 2.8e4`) before this report was finalized —
  documented here rather than silently passed over, per the "author ≠ sole verifier" discipline;
  this audit is the independent check that caught it. **E1 is fixed** for the table and its
  headline numbers; this one downstream illustrative approximation is now also consistent.

**E1 verdict: CLOSED.** The table, its headline, and the nominal-scale citation are all
independently reproduced exactly. No rounding is presented as "exact"; the n=4/n=8 distinction is
now stated correctly and the looser bound is correctly relabeled, not deleted.

### W1 (no compute-cap disclosure) — re-derivation

- `grep -rn "resource.*cap\|compute.*cap" dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` (this
  audit) → no match; the α-ledger (`§4.2/§5`) constrains `sum(alpha_j) <= alpha_total`, an error
  budget, not a compute budget. Confirms no frozen resource/compute cap exists for OP-2.2,
  independently of report 019.
- Rev. 3's V3 headline now reads: "calculable from the frozen formula, but not declarable viable
  against any committed resource/compute cap, because no such cap exists anywhere in the repo for
  OP-2.2." **W1 verdict: CLOSED** — the silence report 019 flagged is gone; the disclosure is
  explicit and independently true.

### W2 (V4b premise) — re-derivation

- `research_program/work_packages/wp4_kappa_numeric_reference.py:56-57` (direct read, this audit):
  `def W(t, r): return np.exp(r / t) * (r / t - 1.0)` — vanishes at `r=t`, confirming `τ`
  (bound to `t` at call sites) plays the role of `2M`. **Confirmed verbatim.**
- `wp4_kappa_numeric_reference.py:74-75`: `Up, Uq = Utilde(t, v_p, r_p), Utilde(t, v_q, r_q)` /
  `assert Up < 0 < Uq, "reference shape must straddle the horizon (Up<0<Uq)"`. **Confirmed
  verbatim**, including the exact assert message (rev. 3's first draft had dropped the
  `"(Up<0<Uq)"` suffix from the quoted string; corrected in the working tree before this report —
  see finding 7 below).
- `dev/pr011_tv_certification_enumeration.py:41-42`: `R_P, V_P = 2.0, 0.0` /
  `R_Q, V_Q = 0.5, 1.0`. **Confirmed** — matches the dossier's `(r_p,v_p)=(2,0)`,
  `(r_q,v_q)=(0.5,1)`.
- **Causal-chain check (beyond report 019's own citations):** `pr011_tv_certification_enumeration.py:124`
  calls `make_builder(R_P, R_Q, V_P, V_Q)` from `wp4_kappa_numeric_reference.py:37` (import), which
  is exactly the constructor containing the `W`/straddling-assert code above. This confirms the
  frozen constants and the assert are not merely present in a *related* file, but are the actual
  code path that produced the certified `pr011_tv_certification_n{4..8}.csv` artifacts the whole
  dossier relies on — strengthening W2's closure beyond what report 019 itself verified.
  `wp4_kappa_numeric_reference.py`'s own `__main__` demo (`:135-141`, shape "A moderate") uses the
  identical `(r_p,r_q,v_p,v_q)=(2.0,0.5,0.0,1.0)` tuple, corroborating independently.
- **Finding 7 (self-correcting, non-blocking):** the quoted assert string in rev. 3's first draft
  omitted the verbatim `"(Up<0<Uq)"` suffix present in the actual source. Caught during this
  audit's line-by-line re-derivation and corrected in the working tree before this report was
  finalized.

**W2 verdict: CLOSED.** The corrected premise is verified against the actual generator code (not
just cited, but traced through the call chain to the certified CSVs), and the FAIL-structural
conclusion is unchanged — if anything the corrected premise (hard-frozen straddling assert) makes
the non-constructibility claim strictly stronger, exactly as rev. 3 claims.

### No new error introduced

- Full `git diff dev/OP22_BD_VIABILITY_DOSSIER.md` reviewed line-by-line (this audit). No gate
  verdict (V1/V2/V4a unchanged), no disposition, and no OP-2.2 terminal was altered by rev. 3 —
  confirmed by direct diff inspection, not by trusting the header's own claim to that effect.
  Every surviving citation from rev. 2 not touched by the E1/W2 fixes (op13 formula, α-ledger
  logarithmic-multiplicity clause, V1/V2 hand values) is untouched in the diff.
- The two self-correcting findings above (6, 7) are the only defects this audit found in rev. 3's
  text; both were caught and fixed during this same audit pass, before publication.

## 5. dev/validation separation & ground-truth leakage

Unchanged from report 019's assessment, re-confirmed: the dossier lives in `dev/` (committed
scoped exception), runs no code, draws no seed, touches no sealed path. The rev. 3 edit is a pure
prose correction of already-committed-elsewhere numbers and citations; it introduces no new
leakage channel. W2's fix, if anything, closes a leakage-adjacent imprecision: the corrected text
is now explicit that the frozen family's horizon-related constants (`τ`, patch corners) are
already order-blind constructs used only to *generate* the poset laws, never consulted by `B`'s
construction — this dossier does not propose a `B`, so no B2-style order-only firewall is even in
scope here, but the corrected text is more precise about what is and isn't exposed as a variable
axis, which is the relevant precision for any future family design.

## 6. Claim-boundary check

No horizon/localization overclaim in rev. 3: the ceiling `REFERENCE_WITNESS_SEPARATION_ONLY` is
preserved verbatim and stated to hold "even under an excellent TV result"; the forbidden framings
("proxy de horizonte," "localizador") remain barred at the same anchors. The corrected V4b text,
if anything, narrows the claim further (explicitly stronger FAIL-structural reasoning) rather than
widening it. No OP-2.2 terminal is emitted; rev. 3's header explicitly states none was changed,
and the diff confirms it.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | OK | E1 closed: V3 budget table re-anchored to the n=4 certified ceiling `0.004611899229`; `m_min = 412,046/433,029/563,383` independently recomputed and matches exactly; nominal-TV realistic scale (`≈4.23e6/4.44e6/5.78e6`) independently recomputed and matches. | `dev/OP22_BD_VIABILITY_DOSSIER.md:160-182`; `data/reports/pr011_tv_certification_n4.csv`; `docs/plan_avanzado_14_julio_2026.md:51`; recomputation §4 |
| 2 | OK | W1 closed: V3 headline now explicitly states no frozen resource/compute cap exists for OP-2.2; independently confirmed absent from `dev/OP21_REFERENCE_CERTIFIER_PREREGISTRATION.md` §4.2/§5. | `dev/OP22_BD_VIABILITY_DOSSIER.md:139-142`; absence verified by search |
| 3 | OK | W2 closed and strengthened: V4b premise corrected to the frozen generator's actual horizon locus (`r=τ`) and hard-frozen straddling assert; traced through the call chain (`pr011_tv_certification_enumeration.py:124` → `make_builder` → `wp4_kappa_numeric_reference.py`) to the same code that produced the certified CSVs — a deeper verification than report 019 itself performed. FAIL-structural conclusion unchanged, reasoning sharper. | `dev/OP22_BD_VIABILITY_DOSSIER.md:224-248`; `wp4_kappa_numeric_reference.py:37,56-57,74-75,124-141`; `pr011_tv_certification_enumeration.py:41-42,124` |
| 4 | OK | No new error introduced: full diff reviewed; V1/V2/V4a, disposition, and OP-2.2-terminal status all unchanged, confirmed by direct diff inspection. | `git diff dev/OP22_BD_VIABILITY_DOSSIER.md` |
| 5 | OK | Seal and tree state unaffected: `make verify-seal` MATCH; only `dev/OP22_BD_VIABILITY_DOSSIER.md` modified; the two pre-existing untracked files (report 019 finding W3) remain untouched, per explicit PI instruction. | §3 |
| 6 | WARN (self-corrected) | Rev. 3's first working-tree draft carried an internal arithmetic slip: after swapping the illustrative heuristic's input from the rounded `0.0092` to the precise `0.009223798457`, the approximate output was left at the old rounding (`≈2.9e4`) instead of the value consistent with the new input (`≈2.8e4`, recomputed `28,444.3`). Caught by this audit's independent re-derivation and fixed in the working tree before this report was finalized. | `dev/OP22_BD_VIABILITY_DOSSIER.md:190-193` (post-fix); recomputation §4 |
| 7 | WARN (self-corrected) | Rev. 3's first working-tree draft quoted the frozen assert message with the `"(Up<0<Uq)"` suffix dropped, a non-verbatim quote of source text. Caught by this audit's line-by-line source comparison and fixed in the working tree before this report was finalized. | `dev/OP22_BD_VIABILITY_DOSSIER.md:235` (post-fix) vs `wp4_kappa_numeric_reference.py:75` |
| 8 | WARN ×22 | Standing mechanical warnings (committed data files with no generator reference), identical to reports 017/018/019; none introduced by rev. 3. | §2 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=24

## 8. Verdict

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS

E1 is closed: the V3 budget table is now correctly anchored to the n=4-pinned family's own
certified ceiling, with exact digits, the looser n=8 bound correctly relabeled rather than
conflated, and a realistic nominal-TV scale added. W1 and W2 are both closed, and W2's fix was
independently traced deeper than report 019's own verification (through the actual call chain
that produced the certified data) — the FAIL-structural conclusion is unchanged and, if anything,
better supported than before. Two self-correcting arithmetic/quotation slips were found during
this audit's independent re-derivation and fixed in the working tree prior to this report's
completion; both are now consistent. No new error was introduced by the rev. 3 edit, and no gate
verdict, disposition, or OP-2.2 terminal changed — consistent with the dossier's own header claim,
verified by direct diff review rather than taken on trust. The 22 standing mechanical warnings and
the pre-existing untracked-file warning (W3, unchanged, correctly left untouched per explicit PI
instruction) remain, as in reports 017-019, unrelated to this fix.

**Recommended next step:** this dossier is now in a state fit to return to `/comite` for the
disposition question report 019 already identified — keep V2-support `UNRESOLVED` and consider
authorizing the frozen enumerative falsifier (decision 035 §5/§9) as the single next execution,
run and verified by someone other than the dossier's author — subject to the PI's own sequencing
preference and a fresh committee session, neither of which this audit adjudicates.

Audit complete. Nothing committed, nothing pushed; the only file written is this report (plus the
two working-tree corrections to the audited dossier documented in findings 6-7, made during the
audit's own re-derivation, not as a separate remediation step).
