# Auditor Report 033 — emergencia-viz-remediacion-032-reauditoria

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit `ec51f44`
(`viz: repara el umbral de fig02 y aplica la auditoria 032 completa`), parent `c87d302`. Working
tree clean.

**Targeted re-audit**, scope fixed by the user: verify *only* the remediation of the one error
and the three manual warnings of `docs/auditor/auditor_report_032_emergencia-viz-figuras-del-fracaso.md`.
The 23 pre-existing mechanical warnings (`data/reports/`, `evidence/`) are explicitly **out of
scope** and are not re-litigated.

**Declared deviation from the skill's counting rule.** §7 counts only findings inside the
remediation scope. The 23 mechanical warnings are reproduced verbatim in §2 and remain open
repo-wide; excluding them from the counts is what makes the verdict a statement about the
remediation rather than about the repository. Report 032 remains the standing repo-wide record.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh` — exit code `0`, output unchanged from report 032:
`0 error(s), 23 warning(s)`, all 23 under `data/reports/` and `evidence/`. Tail, verbatim:

```text
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
WARN: committed data file with no generator reference: evidence/new_geometry_20260719/mink_control_metrics.csv
----------------------------------------
Auditor: 0 error(s), 23 warning(s)
```

`ec51f44` introduced **no new mechanical warning**: the count is identical to the one recorded at
`c87d302` in report 032 §2, and no warning names a path under `emergencia/`.

## 3. Seal & freeze integrity

```text
$ make verify-seal
thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
```

Matches `docs/preregistration_002.md:8` and `docs/preregistration_003.md:9`. `git diff --stat
c87d302 ec51f44` touches nothing under `nachocausal/`. No drift.

## 4. Reproducibility of published numbers

**4.1 Error 1 — REMEDIATED, verified.** `emergencia/viz/datos.py:36-37` now declares
`APARCADO_FUERTE = 0.50` and `UMBRAL_ERROR_RELATIVO = 0.30` on separate, labelled axes;
`fig02_el_gate.py:90-91` draws `GATE` and `APARCADO_FUERTE` only. `grep` for
`UMBRAL_FUERTE|"umbral fuerte secundario"` over `emergencia/viz/` and `HOJA_DE_RUTA.md` returns
**no occurrences**. The `0.30` no longer appears on the correlation axis anywhere.

The replacement is the *correct* threshold and it carries real content, as the user required:
recomputed from the sealed CSV in this audit,

| representación | `sup IC95(ρ)` | `< 0.50` | terminal sellado |
| --- | --- | --- | --- |
| `HEIGHT_ONLY` | `0.2897` | sí | (benchmark, aparcado por el gate anterior) |
| `HEIGHT_WIDTH` | `0.4838` | sí | `HEIGHT_WIDTH_STRONGLY_PARKED = TRUE` |
| `COUNT_VOLUME` | `0.5824` | no | `COUNT_VOLUME_STRONGLY_PARKED = FALSE` |

matching `P1a_resultados_representaciones_alternativas_d2.md` §5–§6. The figure recomputes this
and refuses to draw otherwise (`fig02_el_gate.py:83-88`); **verified to fire** — forcing
`datos.APARCADO_FUERTE = 0.60` raises `ValueError` instead of producing a figure.

**4.2 Warning 2 — REMEDIATED, citations exact.** `datos.py:22-34` now names
`P1a_contrato_representaciones_alternativas_d2.md` and tabulates the three thresholds by axis.
The three cited lines were read and are exactly as claimed:

```text
:145  bootstrap95_upper(mediana error relativo absoluto) <= 0.30,
:146  bootstrap95_lower(correlacion Pearson) >= 0.80.
:156  bootstrap95_upper(correlacion) < 0.50,
```

**4.3 Warning 3 — REMEDIATED in form; see finding 1 for a residue.** `viz/README.md` and
`HOJA_DE_RUTA.md` §22.4 no longer assert what the source does not say. Both now state
`Delta_A = rho_max - rho_obs = +0.0015` to `+0.0026` as the exact Bloque A identity, give the
derivation `Delta_B = sqrt(1 - T_corr) - rho_obs` explicitly, and say the reconstruction is
*derived and checked*, not quoted. Reproduced independently in this audit: `-0.000045` to
`+0.000703` over the six strata.

**4.4 Warning 4 — REMEDIATED, self-checking.** `fig06_mapa_del_fracaso.py:158-166` counts stages
and phases over its own list and raises if the title stops describing the diagram. **Verified to
fire**: injecting a twelfth stage yields `ValueError: el recuento del título no describe el
diagrama: 12 etapas, 8 fases, 3 del ramal`. The drawn title reads `11 etapas — 7 fases y el ramal
COUNT_VOLUME`, and `dibujar()` reports `etapas dibujadas = 11`.

**4.5 Regression — clean.** `git diff --stat c87d302 ec51f44 -- emergencia/viz/output/` shows
exactly three PNGs changed (`fig02`, `fig04`, `fig06`); `fig01`, `fig03`, `fig05` are untouched,
as the commit message claims. Re-running `hacer_figuras.py` reproduces all six byte-identically.
The SHA-256 sidecar guardrail still fires on a one-byte perturbation.

## 5. dev/validation separation & ground-truth leakage

Unchanged from report 032 §5 and re-checked: no import from `dev/`, no write to
`emergencia/resultados/`, no touch of `nachocausal/`. `ec51f44` adds no RNG call — the single
`default_rng(20260807)` in `fig03` is unchanged and outside the reserved band
`[2000000, 2999999]` (`docs/program_closure_note_2026-07-30.md:136`). Ground truth
(`latent_duration`) still appears only as the response, never as a predictor or selector.

## 6. Claim-boundary check

No over-claim introduced. The scan for `reconstru|recuperabilidad|3+1` over the changed files
returns the same two negations as before (`hacer_figuras.py:11`, `README.md:5`). §22.5 states
plainly that the material remains `AUDIT_FAIL` until a re-audit is issued, which is the correct
posture.

**Finding 1 — WARN. The published bound `|Delta_B| < 0.00071` is tighter than its input
precision supports.** `T_corr` is available only to four decimals from the printed Bloque B table
of `emergencia/p1a_count_volume_canal_sigma_m_d2.py`. Propagating the `±5e-5` rounding of that
input through `Delta_B = sqrt(1 - T_corr) - rho_obs` gives, for `(64, PAST)`, a range
`[+0.000659, +0.000747]` — i.e. the true `Delta_B` may be as large as `0.000747`, which
**violates the published bound**. Worst case over the six strata: `0.000747`. A bound the input
precision does support is `|Delta_B| < 0.0008`; the quoted interval `-0.000045` … `+0.000703`
should likewise be labelled a point evaluation at the printed precision, not a certified
interval. Anchors: `emergencia/viz/README.md` ("Cota honesta: `|Delta_B| < 0.00071`"),
`emergencia/HOJA_DE_RUTA.md` §22.4, `emergencia/viz/fig04_anatomia_del_error.py` (nota al pie,
`$|\Delta| < 0.00071$`). This is the same *class* of defect that report 032 flagged — a number
stated more precisely than its backing — reappearing inside the remediation for it.

**Finding 2 — WARN. The `fig02` guardrail encodes a stronger predicate than the contract's.**
`P1a_contrato_representaciones_alternativas_d2.md:152-157` parks a representation if **for every
`n`, at least one side** has `bootstrap95_upper(rho) < 0.50`, **or** the median-relative-error
disjunct holds. `fig02_el_gate.py:76,83` instead computes the maximum of `sup IC95` over all six
strata and tests `max < 0.50`, ignoring the second disjunct. Evaluated in this audit, both
predicates agree on all three representations in the sealed sample (`3/3`), so no drawn claim is
wrong today; and for the positive branch the figure's condition *implies* the contract's, so
`HEIGHT_WIDTH_STRONGLY_PARKED` is soundly certified. The negative branch is not implied: a CSV
with `sup` mixed across sides could satisfy the contract while failing `max < 0.50`, and the
guardrail would then certify the wrong terminal. As a guardrail it should test the contract's
predicate, not a proxy for it.

**Finding 3 — WARN. The ledger now states the same quantity at two precisions without a
cross-reference.** `emergencia/HOJA_DE_RUTA.md:662` (§16) and `:747` (§18) still read
"`COUNT_VOLUME` está a `<=0.0007` en `rho` del óptimo", while the new §22.4 establishes that the
exact Bloque A distance is `+0.0015`–`+0.0026` and that `0.0007` is the intrabin-corrected
`Delta_B`. Both sections are pre-existing historical record and correcting them is not proposed;
but a reader of §16/§18 now has no pointer to the distinction that §22.4 makes. A one-line
cross-reference from §16 and §18 to §22.4 would close it without rewriting the record.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | WARN | `\|Delta_B\| < 0.00071` is tighter than the 4-dp precision of `T_corr` supports; worst case `0.000747` at `(64, PAST)`. Honest bound `< 0.0008` | `emergencia/viz/README.md` §"Dos precisiones"; `HOJA_DE_RUTA.md` §22.4; `fig04_anatomia_del_error.py` nota al pie |
| 2 | WARN | `fig02` guardrail tests `max(sup IC95) < 0.50` instead of the contract's "para todo `n`, al menos un lado", and ignores the second disjunct; agrees `3/3` today, not equivalent in general | `emergencia/viz/fig02_el_gate.py:76,83-88` vs `P1a_contrato_representaciones_alternativas_d2.md:152-157` |
| 3 | WARN | §16 and §18 still say "`<=0.0007` del óptimo" with no cross-reference to the §22.4 distinction between `Delta_A` and `Delta_B` | `emergencia/HOJA_DE_RUTA.md:662`, `:747` vs §22.4 |
| 4 | OK | Error 1 remediated: `0.30` gone from the correlation axis; `0.50` drawn; grep returns no `UMBRAL_FUERTE` anywhere | `datos.py:36-37`, `fig02_el_gate.py:90-91` |
| 5 | OK | The `0.50` line reproduces the sealed terminals: `HEIGHT_WIDTH` `0.4838` parked, `COUNT_VOLUME` `0.5824` not | §4.1; `P1a_resultados_representaciones_alternativas_d2.md` §5–§6 |
| 6 | OK | The new `fig02` terminal check fires (`APARCADO_FUERTE = 0.60` → `ValueError`) | §4.1 |
| 7 | OK | Warning 2 remediated: correct contract cited, three lines verified verbatim | `datos.py:22-34`; contract `:145,:146,:156` |
| 8 | OK | Warning 3 remediated in form: `Delta_B` derived with formula, no longer attributed to the source | `viz/README.md`; `HOJA_DE_RUTA.md` §22.4 |
| 9 | OK | Warning 4 remediated and self-checking; count check fires on an injected stage | `fig06_mapa_del_fracaso.py:158-166` |
| 10 | OK | Regression clean: only `fig02`, `fig04`, `fig06` PNGs changed; all six reproduce byte-identically; SHA guardrail still fires | `git diff --stat c87d302 ec51f44`; §4.5 |
| 11 | OK | Seal `6e2c3888…` intact; no new mechanical warning; seed band untouched; ground truth still scoring-only; no over-claim | §3, §2, §5, §6 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=3

## 8. Verdict

One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error). Must match the counts in §7.
AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS

**The error of report 032 is closed.** The `0.30` is gone from the correlation axis, the `0.50`
that replaced it is the contract's own parking threshold, and it now carries the sealed
`HEIGHT_WIDTH` / `COUNT_VOLUME` distinction that the previous version erased — verified against
the sealed record and protected by a check that was demonstrated to fire. Warnings 2 and 4 are
closed. Warning 3 is closed in form, with one residue.

Three warnings remain, all in prose or in guardrail fidelity, none affecting a drawn number.
Recommended remediation — **not applied; the user's call**:

1. Relax `|Delta_B| < 0.00071` to `< 0.0008` in `viz/README.md`, `HOJA_DE_RUTA.md` §22.4 and the
   `fig04` footnote, and label `-0.000045`…`+0.000703` as a point evaluation at printed
   precision. Alternatively, obtain `T_corr` at full precision and state a bound that follows
   from it.
2. Make the `fig02` check evaluate the contract's predicate literally ("para todo `n`, al menos
   un lado", plus the second disjunct), so the guardrail and the contract cannot diverge.
3. Add a one-line cross-reference from §16 and §18 to §22.4. Do not rewrite either section:
   they are historical record.

Scope note: this verdict covers the remediation of report 032 only. Repo-wide, the 23 mechanical
warnings of §2 remain open and report 032 stands as their record.
