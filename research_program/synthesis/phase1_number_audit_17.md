# Fase 1 · Paso 1.7 — Number and identifier audit

> **STATUS: AUDIT_PASS_WITH_DECLARED_CAVEATS / NOT_A_VALIDATION_RERUN /
> DOES_NOT_TOUCH_SEAL.**
>
> Sweep of numeric claims and hard identifiers in the limits manuscript after PI
> review OK (2026-07-28). Policy: every published number is either the literal
> output of a committed deterministic artifact, a frozen threshold/hash, or marked
> non-numeric/ asymptotic / `[UNVERIFIED]`.
>
> FECHA: 2026-07-28 · Manuscript: `docs/manuscript_limits_draft.md`
> HEAD de referencia al auditar: `018fc62` (pre-polish); post-polish commit follows.

## 1. Policy

| Class | Allowed without `[UNVERIFIED]` | Action if missing generator |
|---|---|---|
| A. Seal / commit / hash | Verified in repo files | Fail audit if wrong |
| B. Frozen thresholds / seeds | From prereg-002 / thresholds.py | Cite file |
| C. Validation table numbers | From `preregistration_002_result.md` + MATCH re-verification | Transcribe only |
| D. Asymptotic rates / exact 0 | Theorems (`TV=0`, \(n^{-1/2}\)) | Math, not ensemble |
| E. Heuristic or ungenerated | Must say NUMERICAL / OPEN / omit | Do not invent |

No new `validate.run()` was executed for this audit.

## 2. Class A — seals and commits

| Identifier | Location in manuscript | Verification |
|---|---|---|
| `thresholds.py` SHA256 `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | §4.1 | Matches `docs/preregistration_002.md` L7–8 and CLAUDE/seal discipline |
| Commit `573cfcb` (historical blind run) | §4.2 provenance | Cited as historical package commit in `preregistration_002_result.md` L20 |
| numpy 1.26.4 | §4.2 | Same result file L22 |
| Estimator-v2 seal chain `2f4c4a99` / freezes | §4.1 (by reference) | prereg-002 provenance chain |

**Verdict:** OK. Seal not modified.

## 3. Class B — frozen thresholds and protocol constants

| Quantity | Value | Source |
|---|---|---|
| Primary intensity \(\lambda\) | 12000 | prereg-002 |
| \(p_{\mathrm{perm}}\) threshold | \(\le 10^{-4}\) | prereg-002 frozen analysis |
| Coverage floor | \(\ge 0.5\) | prereg-002 (deliberately weak) |
| FP fraction threshold | \(\le 0.05\) | prereg-002 |
| Domain \(t_{\mathrm{edge}}\) | 6 | prereg-002 / estimator-v2 freeze |
| Validation seed count | 20 | prereg-002 held-out draw |
| Virgin seed band | \([2\cdot 10^6,\,3\cdot 10^6)\) | prereg-002 |
| `VALIDATION_DRAW_SEED` | 20260622 | prereg-002 |

**Verdict:** OK — protocol constants, not free parameters.

## 4. Class C — validation table (primary endpoint)

All from `docs/preregistration_002_result.md` (transcribed; MATCH under
`prereg002_reverification_result.md` per comité 016):

| Quantity | Value in manuscript | Status |
|---|---|---|
| \(p_{\mathrm{perm}}\) primary | \(9.54\times 10^{-7}\) | TRANSCRIBED_MATCH |
| med \(\lvert dr\rvert/(2M)\) | 0.064 | TRANSCRIBED_MATCH |
| \(\theta_{\mathrm{loc}}\) | 0.098 | TRANSCRIBED_MATCH |
| coverage | 0.95 | TRANSCRIBED_MATCH |
| \(r\)-std | 0.008 | TRANSCRIBED_MATCH |
| \(\theta_{\mathrm{stab}}\) | 0.049 | TRANSCRIBED_MATCH |
| LOO fp primary | 0.00 | TRANSCRIBED_MATCH |
| BH abstention | 0.00 | TRANSCRIBED_MATCH |
| MINK abstention range | 0.90–1.00 | TRANSCRIBED_MATCH (levels) |
| Non-primary \(\lambda=6000\) fp | 0.10 | TRANSCRIBED caveat; not in PASS rule |
| Mean \(N\) at primary | “order \(1.2\times 10^4\)” | Consistent with table \(\bar N=12052\); manuscript uses order-of-magnitude wording OK |

**Primary raw artifact:** LOST; epistemic tag already in §4 title/status.  
**Verdict:** OK under declared caveats. No silent re-generation.

## 5. Class D — mathematical / exact (not ensemble)

| Claim | Status |
|---|---|
| \(\mathrm{TV}=0\) on dilation/co-scaling orbit | Theorem; not a float |
| Floor order \(n^{-1/2}\) / \(1/\sqrt{n\bar I}\) | Theorem bound; \(\bar I\) finite not numerically required |
| \(R_\tau=-2\tau/r^3\) | Symbolic; annex + symbolic_checks script |
| Kruskal factor \(16M^2\) | Closed-form proof annex Prop 1 |
| Hellinger/TV inequalities | Standard + project two-point note |

**Verdict:** OK.

## 6. Class E — intentionally non-numeric or open

| Item | Manuscript treatment | Audit |
|---|---|---|
| Numerical \(\bar I\), \(\bar\kappa\sim 35\ell\), \(\lambda^6\) scalings | Not asserted as proved numbers in §3; annex marks NUMERICAL | OK — not smuggled into manuscript claims |
| Ordering-fraction Chebyshev cardinalities | Omitted (comité 045 C3–C4 open) | OK |
| arXiv IDs in §6 / references | From filtered/verified set (`tarea_grok_2.md`) | OK — do not add unaudited IDs |
| “First in literature” for Thm 3.8 | Forbidden; hedge only | OK |

## 7. Structural polish 1.6b (related)

| Issue | Fix |
|---|---|
| Duplicate Lemma 0 / channel paragraph in §3 | §3 now points to Lemma 2.1–2.2 in §2 |
| FWP Lemma 0/1 naming in proofs | Renamed to Lemma 2.1 / 2.2 in proof sketches |

## 8. Audit verdict

```text
AUDIT_PASS_WITH_DECLARED_CAVEATS
```

- No fabricated numbers found.
- Validation floats are transcriptions with MATCH re-verification and lost primary raw.
- Seal hash unchanged.
- Open numerical work remains labeled open/NUMERICAL outside proved claims.

**PI review:** accepted manuscript structure/content 2026-07-28 (user confirmation).  
**Not discharged:** Paso D item 5 (external novelty reader); arXiv release.

## 9. Residual actions (non-blocking for internal draft)

1. Optional: cite exact line `12052` instead of “order \(1.2\times 10^4\)” for \(\bar N\) if desired for pedantry.
2. Before arXiv: re-run `make verify-seal`; re-verify all Class C numbers against MATCH artifact files in one auditor pass.
3. Expand reference list from `biblioteca/` without new unaudited arXiv IDs.
