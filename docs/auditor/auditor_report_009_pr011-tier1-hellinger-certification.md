# Auditor Report 009 — pr011-tier1-hellinger-certification

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

**Trigger:** User authorization to close tier-1 `ε` via §6.1 `HELLINGER_FALLBACK` and re-pass G2b
after `auditor_report_008`.

**Target:** `dev/pr011_tv_certification_enumeration.py certify`, artifact pair
`data/reports/pr011_tv_certification_n4.csv` + `.sha256`, terminal
`PAIR_DISTINGUISHABLE_AT_TRACTABLE_N`.

**Commit audited:** working tree at certification run (post-`1b220da` implementation edits).

**Out of scope:** `n > 4` ladder; blind mass-estimation prereg; sealed validation.

## 2. Mechanical audit

Re-run `bash .claude/skills/auditor/audit.sh` after artifact commit expected to list
`pr011_tv_certification_n4.csv` with generator reference in
`dev/pr011_tv_certification_enumeration.py` (this session: generator exists pre-commit).

Exit code at audit time (pre-artifact commit): `0`, 12 legacy CSV warnings unchanged.

## 3. Seal & freeze integrity

- `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (unchanged).
- No `nachocausal/` modifications in certification path.

## 4. Reproducibility of published numbers

**Generator:** `python3 dev/pr011_tv_certification_enumeration.py certify`

**This session (wall ~342 s including primary probe M=24):**

```
PR011_CERTIFICATION=OK
method=HELLINGER_FALLBACK
epsilon_certified_upper=0.004611899229
PR011_VIABILITY_TERMINAL=PAIR_DISTINGUISHABLE_AT_TRACTABLE_N
hellinger_M=100 H2=1.329351347556e-06
hellinger_H2_crosscheck=1.328434182296e-06
primary_nominal_tv=0.001440222659206 grid_m=12 raw_mass_sum=0.328075
```

**Artifact SHA256:** `5b53df73cdb02cba1198e02fb332d69d0ca3377a033cb767075d7855b6a475a0`

**Harness:** `PYTHONPATH=. pytest tests/test_pr011_tv_certification_enumeration.py` → 10 passed.

**Method audit:**

| Check | Result |
|---|---|
| Primary enumeration tier-1 at M≤32 | **FAIL** (`raw_mass_sum` ≤ 0.59; renormalization required) |
| Hellinger M=72 vs M=100 stability | **PASS** (rel_gap ≈ 0.069% < 0.1% budget) |
| `ε_certified = 4 × Le_Cam_upper(H²) < 1` | **PASS** (0.00461…) |
| Nominal enumeration TV (annotation) | 0.00144 < ε_certified (consistent upper bound) |

**Implementation note:** frozen spec table cites fallback grid `M=18`; execution uses `M=100`
with `M=72` cross-check per `N=100` anchor in §6.1 and convergence evidence (this session:
`M=18` vs `M=100` rel_gap ≈ 1.6%). Documented in spec §13.

## 5. dev/validation separation & ground-truth leakage

- Order-only channel; no sealed seeds; no embedding in estimator.
- Pair `(0.95, 1.05)` theory-anchored; no PR009/PR010 inputs.
- Certification is a **viability** unit, not blind validation.

## 6. Claim-boundary check

- **OK:** Terminal is `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` at **named** `(n=4, τ₀, τ₁)` only —
  not a performance claim, not metric reconstruction.
- **OK:** `ε` is an **upper bound** via Hellinger/Le Cam + data-processing/product bound — not
  exact poset TV.
- **WARN:** Primary route §6.1 enumeration remains **non-tier-1** at tractable grids; terminal
  rests on **fallback** route, not preferred enumeration.

## 7. Findings

| # | Severity | Finding | Anchor |
|---|---|---|---|
| 1 | OK | `certify` reproduces terminal + ε; artifact pair written | §4 stdout; CSV |
| 2 | OK | `ε_certified < 1` — non-degenerate viability at n=4 | `epsilon_certified_upper=0.004611899229` |
| 3 | OK | Hellinger grid stability M=72/M=100 within 0.1% | §4 method table |
| 4 | OK | Tests 10/10; falsifier unchanged | pytest |
| 5 | WARN | Terminal via **fallback**, not primary enumeration | spec §6; `method=HELLINGER_FALLBACK` |
| 6 | WARN | Execution grid M=100 refines frozen table M=18 | spec §6.1 vs `HELLINGER_M=100` in script |

AUDIT_ERRORS=0
AUDIT_WARNINGS=2

## 8. Verdict

Tier-1 certification at `n=4` is **reproducible** and **claim-safe** as an upper-bound viability
result. G2b **tier-1 closure** is authorized for `(n=4, τ₀=0.95, τ₁=1.05)` with terminal
`PAIR_DISTINGUISHABLE_AT_TRACTABLE_N`. Ladder extension and mass-estimation remain out of scope.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS