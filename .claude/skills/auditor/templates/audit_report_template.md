# Auditor Report {{NNN}} — {{SLUG}}

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target
What was audited (repo root, branch, commit) and the trigger (routine check, pre-`/comite`
foundation, specific claim under suspicion).
{{SCOPE}}

## 2. Mechanical audit
Verbatim output of `bash .claude/skills/auditor/audit.sh`, plus its exit code.
{{MECHANICAL_AUDIT}}

## 3. Seal & freeze integrity
Live `make verify-seal` SHA vs the recorded frozen SHA (`docs/preregistration_*`, the
`docs/estimator_v2_seal.md` chain). Confirm the live instrument is the one a freeze record names;
flag any drift. Each line carries its command / file:line.
{{SEAL_INTEGRITY}}

## 4. Reproducibility of published numbers
Every numeric claim in `README.md` / `docs/` traced to the committed deterministic script + seed
band + commit that produces it. "If a value does not survive its generator, it is not real."
Mark any number with no committed generator.
{{REPRODUCIBILITY}}

## 5. dev/validation separation & ground-truth leakage
Is the exploration sandbox kept out of the sealed path? Is the hidden embedding used only to
score, never to define/guide the observable or the boundary? Any path by which dev tuning or
ground truth could leak into a committing result.
{{SEPARATION}}

## 6. Claim-boundary check
Does any text over-claim beyond finite-patch 1+1D *localisation* — metric reconstruction,
asymptotic event horizon, 3+1D, a PASS coerced from an abstain/OUT_OF_DOMAIN? Cite the offending
line.
{{CLAIM_BOUNDARY}}

## 7. Findings
| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | ERROR / WARN / OK | … | … |

AUDIT_ERRORS={{N_ERRORS}}
AUDIT_WARNINGS={{N_WARNINGS}}

## 8. Verdict
One of: `AUDIT_PASS` (no errors, no warnings), `AUDIT_PASS_WITH_WARNINGS` (no errors, ≥1 warning),
`AUDIT_FAIL` (≥1 error). Must match the counts in §7.
AUDIT_VERDICT={{VERDICT}}
