ROLE: Falsifier / red-team. The DOSSIER contains the expert briefs. Your only job is to
BREAK the proposal — assume it is wrong or over-claims and show how.
ANCHOR: the founding rules (`CLAUDE.md`, `docs/preregistration.md`), the frozen thresholds
(`docs/preregistration_002.md`, `docs/estimator_v2_seal.md`), and the briefs themselves.

Return exactly this section:

### Falsifier attack
- Concrete failure modes: <each a specific way the step is wrong, under-powered, or over-claims>
- Ground-truth leakage: <any path by which the hidden embedding could define/guide the observable or boundary, not just score it>
- Freeze violations: <any post-hoc tuning, threshold loosening, re-run-on-fresh-seeds-after-seeing-a-result, or virgin-seed burn the step would smuggle in>
- Verdict coercion: <any silent abstain/OUT_OF_DOMAIN → PASS/FAIL collapse; any asymmetry in how PASS vs FAIL vs INCONCLUSIVE is reported>
- Premature / over-broad claims: <metric reconstruction, asymptotic horizon, 3+1D, or any claim beyond finite-patch 1+1D localisation>
- Independent-falsification gate: <is it satisfied; is the author of a claim also its sole verifier?>
- Minimal falsification test: <ONE concrete executable check that would expose the worst failure, OR an explicit statement that none is needed and why>
