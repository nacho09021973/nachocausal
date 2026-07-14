# Auditor Report 010 — pr011-ladder-closure-n6-n8

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

**Trigger:** pre-`/comite` foundation. The user asked to close the PR011 ladder (`n=6,7,8`); the
next step is a `/comite` session to scope PR012, which builds directly on this closure. Per the
comité skill's own discipline ("do not deliberate a PROCEED atop an unaudited result"), this
closure is audited before PR012 deliberation begins.

**Target:** commit `d8ce482` ("Certify PR011 viability at n=6,7,8; close frozen ladder"), branch
`main`, pushed to `origin/main`. Artifacts: `data/reports/pr011_tv_certification_n{6,7,8}.csv` +
`.sha256`. Doc updates: `research_program/synthesis/pr011_mass_distinguishability_viability.md`,
`research_program/README.md`, `docs/plan_avanzado_14_julio_2026.md`,
`tests/test_pr011_tv_certification_enumeration.py`.

**Out of scope:** PR012 scope itself (that is the forward-looking `/comite` question this audit
feeds); the sealed empirical estimator path (prereg-001/002/003); blind mass-estimation.

## 2. Mechanical audit

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: [34 files, incl.
      auditor_report_001..009, comite_decision_001..022, hoja_de_ruta_*, preregistration_002/003]
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

Exit code: `0`. The `n6/n7/n8` WARN lines are the same heuristic class already carried by
`n4`/`n5` since `auditor_report_009` — the script matches a generator reference by grep, not by
prose; it does not detect the `certify --n N` invocations documented in the spec and status plan.
Not a new class of finding; count increased by 6 (3 CSV + 3 sha256) for a reason already accepted.

## 3. Seal & freeze integrity

- `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
  (unchanged from `auditor_report_009`).
- `git show d8ce482 -- dev/pr011_tv_certification_enumeration.py` → **empty diff**. The generator
  script itself was not modified in the ladder-closure commit; only `data/reports/`, three
  synthesis/status docs, and the test file changed.
- `nachocausal/thresholds.py` is untouched by this commit (not in `git show d8ce482 --stat`
  output) — confirms the PR011/PR012 identifiability track has no path into the sealed empirical
  estimator, consistent with spec §9 ("no changes to `nachocausal/thresholds.py` or sealed
  estimator").

## 4. Reproducibility of published numbers

**Generator:** `python3 dev/pr011_tv_certification_enumeration.py certify --n {6,7,8}`.

Fresh in-process re-run this session (`enum.certify(n)` for `n in (6,7,8)`, no artifact write,
independent of the committed CSVs):

```
6 HELLINGER_FALLBACK 0.006917848843 PAIR_DISTINGUISHABLE_AT_TRACTABLE_N
7 HELLINGER_FALLBACK 0.00807082365  PAIR_DISTINGUISHABLE_AT_TRACTABLE_N
8 HELLINGER_FALLBACK 0.009223798457 PAIR_DISTINGUISHABLE_AT_TRACTABLE_N
```

Bit-for-bit identical to the committed CSV `epsilon_certified_upper` values — the method is
deterministic (fixed anchor, fixed grid, no RNG) and reproduces exactly on a fresh process.

**Artifact hash chain**, independently recomputed (`sha256sum` on the committed CSV bytes) and
compared against both the committed `.sha256` sidecar and the hardcoded
`COMMITTED_CERT_SHA256_N{6,7,8}` constants added to
`tests/test_pr011_tv_certification_enumeration.py`:

| `n` | `sha256sum` (recomputed) | sidecar | test constant | match |
|---|---|---|---|---|
| 6 | `351888f6…7565` | `351888f6…7565` | `351888f6…7565` | **YES** |
| 7 | `29ab38ee…35a7` | `29ab38ee…35a7` | `29ab38ee…35a7` | **YES** |
| 8 | `2910319b…f565` | `2910319b…f565` | `2910319b…f565` | **YES** |

**Doc-to-CSV cross-check** — every `epsilon_certified_upper` value quoted in
`pr011_mass_distinguishability_viability.md` §13, `research_program/README.md` §1.2, and
`docs/plan_avanzado_14_julio_2026.md`'s ε table was diffed against column 5 of the corresponding
CSV row for `n=4..8`. All five values match verbatim (`0.004611899229`, `0.005764874036`,
`0.006917848843`, `0.008070823650`/`0.00807082365`, `0.009223798457`) — no rounding or
transcription drift. `terminal` is `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` in all five rows,
matching every doc claim.

**Test suite:** `python3 -m pytest tests/test_pr011_tv_certification_enumeration.py -q` → **16
passed** (10 pre-existing + the parametrized artifact test now covering `n=4..8` — 6 was 2
parametrizations, now 5).

## 5. dev/validation separation & ground-truth leakage

- Channel is order-only, conditioned on `N=n`; no sprinkled seeds from the sealed validation
  path; no hidden-embedding coordinate enters the estimator (the certification operates on the
  frozen copula/geometry anchor only, per spec §3).
- No new numeric anchor was introduced for `n=6,7,8` — same frozen pair `(τ₀=0.95, τ₁=1.05)`,
  same geometry `G_◊`, same `HELLINGER_M=100` as `n=4,5`. Nothing was selected after seeing an
  `n=6,7,8` result; the ladder `{4,5,6,7,8}` was frozen at spec-freeze time (`6662a3b`), before
  any of these three certifications ran.
- `grep -rn "PR009\|PR010"` on the generator script and spec: every hit is an explicit exclusion
  statement ("no PR009/PR010 inputs", "PR010 closed", G0b gate) — confirms separation, not usage.

## 6. Claim-boundary check

- **OK:** all three new terminals are `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` at named `(n, τ₀,
  τ₁)` only — a viability certification, not a performance claim, not mass estimation, not
  metric reconstruction.
- **OK:** `ε` remains an upper bound via Hellinger/Le Cam + `n`-fold data-processing (same
  inequality chain as `n=4,5`, audited in `auditor_report_009`) — not exact poset TV.
- **OK:** the new spec text ("`ε` grows linearly in `n` by construction; nominal enumeration TV
  annotations are diagnostics only, not certified bounds") is itself accurate — the primary-grid
  `raw_mass_sum` at `n=8` is `0.000964`, far under the `RAW_MASS_SUM_TARGET=0.99` needed for a
  tier-1 primary-enumeration close, so the doc correctly attributes the terminal to the fallback
  route only, not to the nominal annotation.
- **WARN (carried forward from `auditor_report_009`):** the primary route (§6.1 preferred
  enumeration) still never closes tier-1 at any tractable grid across the whole ladder — every
  rung, `n=4` through `n=8`, rests on the `HELLINGER_FALLBACK`, not the nominally preferred
  method. This is disclosed in the spec (§13, "Frozen ladder … closed … primary grid enumeration
  with convergence audit" listed first but never satisfied) but is a standing methodological
  caveat worth restating for whoever scopes PR012, since PR012 inherits the same primary-route
  limitation if it reuses this generator.

## 7. Findings

| # | Severity | Finding | Anchor |
|---|---|---|---|
| 1 | OK | `certify --n {6,7,8}` reproduces `epsilon_certified_upper` bit-for-bit on a fresh process | §4 in-process re-run |
| 2 | OK | CSV↔sha256-sidecar↔test-constant hash chain verified independently for `n=6,7,8` | §4 table |
| 3 | OK | Generator script (`dev/pr011_tv_certification_enumeration.py`) unmodified in the closure commit — no code changed alongside the new artifacts | `git show d8ce482 -- dev/pr011_tv_certification_enumeration.py` (empty diff) |
| 4 | OK | Seal `6e2c3888…` unchanged; `nachocausal/thresholds.py` untouched by this commit | §3 |
| 5 | OK | All ε values and terminals quoted in the three updated docs match the CSVs verbatim | §4 doc-to-CSV cross-check |
| 6 | OK | 16/16 tests pass, including new `n=6,7,8` parametrized artifact-hash test | pytest output |
| 7 | OK | No PR009/PR010 input path; ladder frozen before any of the three new results were seen | §5 |
| 8 | WARN | Primary-route enumeration (§6.1 preferred method) still never closes tier-1 at any `n` in the ladder — every rung rests on the fallback | §6 |
| 9 | WARN | `audit.sh` heuristic flags 6 new "no generator reference" WARNs for the `n6/n7/n8` artifacts — same pre-accepted class as `n4/n5`, not a new issue | §2 |

AUDIT_ERRORS=0
AUDIT_WARNINGS=2

## 8. Verdict

The `n=6,7,8` ladder closure is **reproducible bit-for-bit**, its artifact hash chain is
internally consistent, no code path changed alongside the new certifications, the seal is intact,
and every number quoted in the three updated docs matches its source CSV exactly. The two
warnings are both carried forward from the already-accepted `n=4,5` posture (fallback-only route;
heuristic no-generator-reference grep) and introduce no new risk. This closure is sound ground
for a `/comite` session to scope PR012.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
