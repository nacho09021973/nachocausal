# Auditor Report 003 — bibliography-claims-vs-biblioteca

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo `nachocausal` at `HEAD=0d73114c05f0c3fd7dee8b4ea33f418d01695e3d` (branch `main`), the commit
that added `docs/bibliography_claims.md` (807 lines) atop `110e4af` (the RelationalHorizon
orientation-fix commit). Trigger: user-requested, narrow-scope audit of
`docs/bibliography_claims.md` against the local `biblioteca/` tree, per the closing note of
`0d73114`'s own recommendation. Requested checks only: (1) cited page/line ranges, (2)
PDF hash/identity, (3) declared reading status (read vs. not-read) per entry. Explicitly
out of scope this run: Brightwell–Gregory, promotion of any `R`-candidate. Step 1's mechanical
audit still runs at full-repo scope regardless (see `/auditor` discipline) — its output is
reported verbatim below even though it is unrelated to the bibliography.

## 2. Mechanical audit

Verbatim output of `bash .claude/skills/auditor/audit.sh` (exit code 1):

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: docs/auditor/auditor_report_001_pr003-c1-freeze-foundation.md,docs/auditor/auditor_report_002_pr003-c1-revised-draft.md,docs/comite/comite_decision_001_pr003-bare-relocalisation-next-step.md,docs/comite/comite_decision_002_pr003-extended-horizon-ideas-and-density-robustness.md,docs/comite/comite_decision_003_pr003-silver-bullet-synthesis.md,docs/comite/comite_decision_004_pr003-c1-freeze-readiness.md,docs/comite/comite_decision_005_pr003-intrinsic-observable-identifiability.md,docs/comite/comite_decision_006_pr003-relational-horizon-candidate-adjudication.md,docs/comite/comite_decision_007_pr003-bl-localization-lemma-l1-regrade.md,docs/comite/comite_decision_009_c1-relational-closure-preflight.md,docs/comite/comite_decision_010_c1-completion-truncation-nonidentifiability.md,docs/comite/comite_decision_011_patch-ensemble-architecture.md,docs/hoja_de_ruta_25_jun_2026.md,docs/hoja_de_ruta_27_jun_2026.md,docs/preregistration_002.md,docs/preregistration_003.md,docs/preregistration_003_draft.md
ERROR: 1 tracked file(s) are also gitignored (committed despite being declared uncommitted):
    dev/bl_localization_l1a.log
----------------------------------------
Auditor: 1 error(s), 0 warning(s)
```

This ERROR is a pre-existing repo-hygiene defect unrelated to `docs/bibliography_claims.md` or
`biblioteca/`. It is not part of the requested narrow scope, but per `/auditor`'s own discipline
Step 1 is not scoped and its output cannot be suppressed — see §7 row 1 and §8.

## 3. Seal & freeze integrity

`make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`.
Matches the frozen SHA named verbatim in `docs/preregistration_003.md:9` (same 64-hex-digit
string, not just the truncated `6e2c3888…` short-form used elsewhere). Live instrument matches
the current prereg's binding record. Not otherwise touched by this run — no bibliography claim
depends on the seal.

## 4. Reproducibility of published numbers

Out of scope for this run (no numeric benchmark results live in `docs/bibliography_claims.md`;
its content is bibliographic claims, not pipeline output). Not audited here.

## 5. dev/validation separation & ground-truth leakage

Out of scope for this run. `docs/bibliography_claims.md` is a literature dossier; it does not
touch the sealed estimator, `dev/`, or the hidden embedding. No leakage path found or looked for
beyond what §2's mechanical scan already covers.

## 6. Claim-boundary check

`docs/bibliography_claims.md` itself is scrupulous about scope — e.g. §1.1 explicitly flags the
d=2 exclusion of HKMM as "a load-bearing gap, not a technicality" (`docs/bibliography_claims.md:68-71`),
and §3.4.2/§4 repeatedly mark diagnostics as *candidate/complementary*, not this project's own
sealed result. No over-claim beyond finite-patch 1+1D localisation found in the file.

## 7. Findings — verified against `biblioteca/`

**Method.** Read the full 807-line dossier. For every `file:line` anchor into
`biblioteca/derived-md/*.md`, every claimed page range into a PDF read via `pdftotext`, every
claimed file existence/hash, and every "acquired/read" status claim, checked the underlying file
directly (`sed -n`, `pdftotext -layout`, `md5sum`, `wc -l`, `ls`). ~30 independent anchors were
spot-checked across 8 distinct source documents (Surya 2019 review, Sorkin Dice08, Dhital 2023
thesis, Yazdi entanglement-entropy paper, Barton et al. 2019 horizon-molecules, Dou–Sorkin 2003,
Eichhorn–Gamito–Stokes 2026 ladders paper, Dushnik–Miller 1941, Bombelli 1987 PhD). **Every single
quoted sentence, equation, numeric value (including uncertainties like `0.185±0.007`,
`−0.039±0.011`, `−0.33±0.01`), and cited line number matched the source file exactly** — no
fabricated or misattributed citation was found anywhere in the sample. The claimed
byte-identity of `dushnik_miller-partially_ordered_sets.pdf` and `ordenes dimension 010.pdf`
(md5 `dc17be5441...`) is confirmed exactly. The claimed "scanner-only, no text layer" status of
`ordenes dimension 003.pdf`/`009.pdf` is consistent with `pdftotext` output (only page-break
bytes, no text). This is an unusually well-grounded dossier.

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | ERROR | `dev/bl_localization_l1a.log` is tracked in git despite matching a `.gitignore` pattern — the exact "quietly commit the exploration sandbox" failure mode this skill exists to catch. Unrelated to the bibliography scope but real and unresolved. | `bash .claude/skills/auditor/audit.sh` output, §2 above; `git ls-files dev/bl_localization_l1a.log` |
| 2 | WARN | `biblioteca/parcial_Set_Trotter.pdf` — W.T. Trotter, "Combinatorial Problems in Dimension Theory for Partially Ordered Sets," Colloques Internationaux C.N.R.S. N°260 (Orsay, 1976) — is present, OCR-legible (`pdftotext` extracts full French/English abstract + body text cleanly), and directly on-topic for §5 (poset order-dimension combinatorics, the exact gap §5.3 discusses). It is **not mentioned anywhere in `docs/bibliography_claims.md`**, including §5.2 (identified-but-unread sources), §5.4 (supplementary background, inventoried-not-mined), or §5.5's acquisition table, which explicitly asserts "Still genuinely missing after this pass: only item 2 (Trotter's 1992 book) has no local substitute confirmed." File mtime (`2026-07-02 16:53:00`) coincides with the session's other `[re-graded 2026-07-02 audit]` edits, suggesting it was acquired but never entered into the dossier. Read in full this session: it does **not** state or prove realizer-uniqueness-up-to-swap (grepped negative for "uniqu", "realizer", "conjugate", "automorph" — confirms §5.3's `UNSUPPORTED_GAP` verdict is still correct on the merits), but the dossier's own completeness self-assessment in §5.5 is factually inaccurate as written — this readable, on-topic local file is missing from its own inventory. | `biblioteca/parcial_Set_Trotter.pdf` (not referenced in `docs/bibliography_claims.md`); cf. `docs/bibliography_claims.md:804-807` (§5.5 completeness claim) |
| 3 | OK | ~30 sampled `file:line` citations into `biblioteca/derived-md/*.md` and page citations into `pdftotext`-read PDFs, spanning §1.1–§1.2, §2.3–§2.7, §3.1.1–§3.4.2, §4.1–§4.3, §5.1 — all verified verbatim against source. | see method note above |
| 4 | OK | PDF identity/hash claims (`dushnik_miller-partially_ordered_sets.pdf` ≡ `ordenes dimension 010.pdf`, md5 `dc17be5441edfbaaacf794924fb87c8c`) and the `ordenes dimension 003/009.pdf` "no text layer" claim — both confirmed. | `md5sum`, `pdftotext` byte-count check |
| 5 | OK | All 12 PDFs the dossier names as locally present (`0302009v1.pdf`, `1909.08620v1.pdf`, `2301.06480v1.pdf`, `2307.04150v1.pdf`, `1710.09467v2.pdf`, `1802.09326v3.pdf`, `0809.1828v1.pdf`, plus the Dushnik–Miller/Kelly–Trotter/Trotter-handbook trio) exist at the claimed paths. §5.5's "text layer confirmed readable" claims for items 9–10 (`2301.06480v1.pdf`, `2307.04150v1.pdf`) verified by direct `pdftotext`. | `ls`, `pdftotext` |

AUDIT_ERRORS=1
AUDIT_WARNINGS=1

## 8. Verdict

The single ERROR (row 1) is a pre-existing, scope-unrelated repo-hygiene defect that Step 1 of
`/auditor` always surfaces regardless of the requested scope — it is not softened here. Within
the requested scope itself (bibliography vs. `biblioteca/`), the dossier's sourcing is
exceptionally solid: every sampled citation checks out exactly, and the one substantive finding
(row 2) is a completeness gap in the dossier's own bookkeeping, not a fabricated or
misrepresented claim.

AUDIT_VERDICT=AUDIT_FAIL
