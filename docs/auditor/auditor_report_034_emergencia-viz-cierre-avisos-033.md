# Auditor Report 034 — emergencia-viz-cierre-avisos-033

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/ignac/nachocausal`, branch `emergencia/p1a-canal-sigma-m`, commit `752cf04`
(`viz: cierra los tres avisos de la reauditoria 033`), parent `ec51f44`, grandparent `c87d302`.
Working tree clean.

**Focused re-audit**, scope fixed by the user: verify only the closure of the three warnings of
`docs/auditor/auditor_report_033_emergencia-viz-remediacion-032-reauditoria.md` — the
`|Delta_B|` bound, the literal parking predicate with tests in both directions, and the
qualification notes in §16/§18 — plus absence of regression in what report 033 already closed.
The 23 pre-existing mechanical warnings are **out of scope**.

Same declared deviation as report 033: §7 counts only findings inside this scope. Report 032
remains the repo-wide record for the 23.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh` — exit code `0`. Tail, verbatim:

```text
WARN: committed data file with no generator reference: evidence/new_geometry_20260719/mink_control_metrics.csv
----------------------------------------
Auditor: 0 error(s), 23 warning(s)
```

Unchanged from reports 032 and 033: `0 errors, 23 warnings`, none under `emergencia/` or
`tests/`. Adding `tests/test_emergencia_viz.py` introduced no mechanical finding.

## 3. Seal & freeze integrity

```text
$ make verify-seal
thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
```

Matches `docs/preregistration_002.md:8` and `docs/preregistration_003.md:9`. `752cf04` touches
nothing under `nachocausal/`. No drift.

## 4. Reproducibility of published numbers

**4.1 Warning 1 — CLOSED, and the new bound is sustainable.** `|Delta_B| < 0.00071` is gone from
every live claim. Recomputed here: propagating the `±5e-5` rounding of the 4-decimal `T_corr`
through `Delta_B = sqrt(1 - T_corr) - rho_obs` gives a worst case of `0.000747` at `(64, PAST)`;
the published bound is now `0.0008`, leaving a margin of `5.29e-05`. `rho_obs` carries no
comparable rounding — it is computed at full precision from the sealed CSV — so `0.000747` is the
true worst case and the bound holds. Present at all three sites:
`emergencia/viz/README.md:126`, `emergencia/HOJA_DE_RUTA.md:1167`,
`emergencia/viz/fig04_anatomia_del_error.py:171`. Both surviving mentions of `0.00071`
(`README.md:125`, `HOJA_DE_RUTA.md:1174`) are explicit historical notes explaining the change,
not live claims. The interval `-0.000045`…`+0.000703` is now labelled "evaluación puntual a la
precisión de la entrada", not a certified interval.

**4.2 Warning 2 — CLOSED in code, and the tests bind it.** `emergencia/viz/datos.py`
`aparcada_fuerte` implements the contract verbatim — read side by side with
`P1a_contrato_representaciones_alternativas_d2.md:152-157`, the quantifiers ("para todo `n`", "al
menos un lado") and **both** disjuncts (`pearson_bootstrap95_high < 0.50`,
`median_are_bootstrap95_low > 0.50`) are present and the column mapping is correct.
`fig02_el_gate.py:91` calls it instead of the `max(sup)` shortcut.

The decisive check is not that the tests pass but that they **would fail if the implementation
regressed**. Two mutants were injected and reverted (working tree verified clean afterwards):

| mutant | result |
| --- | --- |
| restore the old shortcut `max(sup) < 0.50` | `3 failed, 9 passed` — **caught** |
| always return `True` (parks everything) | `2 failed, 10 passed` — **caught** |

Both directions are therefore genuinely bound, as the remediation instruction required.
`tests/test_emergencia_viz.py` has 12 cases including the case that separates the two predicates
(`test_el_atajo_daba_un_falso_negativo_y_el_predicado_no`), the second disjunct in isolation, the
"para todo `n`" quantifier, and an absent representation raising rather than silently returning
`False`.

**4.3 Warning 3 — CLOSED without rewriting the record.** `git diff ec51f44 752cf04 --
emergencia/HOJA_DE_RUTA.md` shows the §16 and §18 hunks as `+8` lines each with **zero
deletions**: the historical sentences at `:662` and `:747` are intact and each now carries a
blockquote pointing to the `Delta_A` / `Delta_B` distinction of §22.4 and the `0.0008` bound.
The only deleted lines in the whole diff belong to §22.4/§22.5 and the stale control token — the
material this commit is supposed to update.

**4.4 Regression — clean.** Full battery `python3 -m pytest tests/ -q`: **341 passed** (329
pre-existing + 12 new), no failures. `git diff --stat ec51f44 752cf04 --
emergencia/viz/output/` shows exactly one PNG changed (`fig04`, the footnote); `fig02.png` is
byte-identical, which is the correct outcome — the predicate change is logical, not visual.
Re-running `hacer_figuras.py` reproduces all six byte-identically. Everything report 033 closed
still holds: `0.50` drawn (`fig02_el_gate.py:99`), sealed terminals reproduced, `fig06` count
self-checked, SHA-256 guardrail firing (covered by `test_el_guardarrail_sha256_salta`).

## 5. dev/validation separation & ground-truth leakage

Unchanged and re-checked. `752cf04` adds no RNG call and no write path; the new test file is
read-only over `emergencia/resultados/` and `tmp_path`. The reserved seed band
`[2000000, 2999999]` (`docs/program_closure_note_2026-07-30.md:136`) is untouched. Ground truth
still appears only as the ANOVA response.

## 6. Claim-boundary check

No over-claim introduced; the two negations in `hacer_figuras.py:11` and `README.md:5` are
unchanged. §22.6 describes the remediation without inflating it, and states plainly that on the
sealed sample the two predicates agree `3/3` so **no terminal changed** — which is the honest
framing of a fix that is about future validity, not about today's result.

**Finding 1 — WARN. The figure's drawn justification still states the invalid implication that
the code no longer commits.** `emergencia/viz/fig02_el_gate.py:130-135` prints inside the panel:

```text
HEIGHT_WIDTH: sup IC95 = 0.484 < 0.50  =>  APARCADO FUERTE.
COUNT_VOLUME: 0.582 > 0.50  =>  no aparcado, y aun así lejos del gate.
```

and `:150-151` returns the keys `"sup IC95 HEIGHT_WIDTH (< 0.50 = aparcado)"` /
`"sup IC95 COUNT_VOLUME (> 0.50 = no aparcado)"`. The first implication is sound —
`max(sup) < 0.50` implies the contract's condition. **The second is not**: `max(sup) > 0.50` does
not entail "no aparcada" under `:152-157`, since a representation with one side below `0.50` for
every `n` would still be parked. That is precisely the unsound inference report 033 flagged, now
surviving as the *stated reason* in the image and in the printed diagnostics, even though the
code beneath computes the correct predicate and would abort on disagreement.

The drawn conclusion is not wrong for this data (the literal predicate confirms both terminals,
and the guardrail makes a figure with a wrong conclusion unproducible), so this is a labelling
defect, not a false result. But a caption that teaches an invalid inference is the same class of
defect this chain has been closing since report 032, and the fix is one line.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | WARN | `fig02`'s in-panel text and returned keys justify the terminals by `sup ≷ 0.50`; the "`0.582 > 0.50` ⇒ no aparcado" half is not a valid inference under the contract, though the conclusion holds here and the code uses the correct predicate | `emergencia/viz/fig02_el_gate.py:130-135`, `:150-151` vs `P1a_contrato_representaciones_alternativas_d2.md:152-157` |
| 2 | OK | Warning 1 closed: `\|Delta_B\| < 0.0008` at all three sites; worst case `0.000747`, margin `5.29e-05`; interval relabelled a point evaluation | `viz/README.md:126`, `HOJA_DE_RUTA.md:1167`, `fig04_anatomia_del_error.py:171`; §4.1 |
| 3 | OK | Warning 2 closed in code: `aparcada_fuerte` implements both disjuncts and both quantifiers, column mapping correct; `fig02` calls it | `emergencia/viz/datos.py` `aparcada_fuerte`; `fig02_el_gate.py:91`; contract `:152-157` |
| 4 | OK | The tests genuinely bind the predicate: shortcut mutant → `3 failed`, always-parked mutant → `2 failed`; tree restored clean | §4.2; `tests/test_emergencia_viz.py` (12 cases) |
| 5 | OK | Warning 3 closed without rewriting: §16/§18 hunks are `+8/-0`, historical text intact, notes point to §22.4 | `git diff ec51f44 752cf04 -- emergencia/HOJA_DE_RUTA.md`; `:662`, `:747` |
| 6 | OK | No regression: 341 tests pass; only `fig04.png` changed; all six figures reproduce byte-identically; `fig02.png` unchanged as expected | §4.4 |
| 7 | OK | Seal `6e2c3888…` intact, no new mechanical finding, seed band untouched, ground truth scoring-only, no over-claim | §2, §3, §5, §6 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=1

## 8. Verdict

One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error). Must match the counts in §7.
AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS

The three warnings of report 033 are closed. The bound is now sustainable with a stated margin;
the parking predicate is the contract's, verbatim, and mutation testing confirms the test suite
would catch a regression in either direction; §16 and §18 are annotated without a single line of
historical record removed. No regression anywhere — 341 tests pass and only the one expected PNG
changed.

One warning remains, and it is the residue of the warning just fixed: the code stopped committing
the unsound inference but the caption still prints it. Recommended remediation — **not applied;
the user's call**:

1. In `fig02_el_gate.py:130-135`, justify the two terminals by the predicate the code actually
   evaluates — e.g. state `HEIGHT_WIDTH` parked / `COUNT_VOLUME` not parked *por la regla
   `:152-157`*, keeping `sup IC95` as the reported quantity rather than as the stated reason —
   and rename the two returned keys accordingly.
2. Regenerate `fig02.png` (it will change this time) and re-verify byte-identity.

This is a caption-level fix over an otherwise clean state. Whether it is worth another commit
before pushing, or is better folded into the next change, is a judgement for the user; nothing in
the current tree is scientifically wrong.
