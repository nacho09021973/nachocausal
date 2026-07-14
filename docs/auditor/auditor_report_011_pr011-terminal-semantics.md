# Auditor Report 011 — pr011-terminal-semantics

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

**Trigger:** `/comite` session `docs/comite/comite_decision_023_pr012-scope-adjudication.md`
(verdict `RECOMMEND_REVISE_AND_RECONVENE`) surfaced two findings via its falsifier wave that no
prior audit (`auditor_report_008/009/010`) caught: (1) a dead-code defect in `certify()`'s
terminal-selection logic; (2) an open question of whether `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N`
over-claims, since PR011's own §7 states small `ε` means masses are *hard* to distinguish. The
chair then ran the falsifier's proposed minimal test live, confirming both findings
simultaneously. This audit follows up: is this real, does it affect how the five already-published
certifications (`n=4..8`) should be read, and does any committed prose over-claim.

**Target:** `dev/pr011_tv_certification_enumeration.py` (`certify()`), the terminal vocabulary in
`research_program/synthesis/pr011_mass_distinguishability_viability.md` §7–§8 and §13,
`research_program/README.md` §1.2, and `docs/plan_avanzado_14_julio_2026.md`.

**Out of scope:** PR012 scoping itself (already covered by `comite_decision_023`); the sealed
empirical estimator (Track A, untouched throughout).

## 2. Mechanical audit

```
Auditor — auditing: /home/ignac/nachocausal
----------------------------------------
ok:   seal nachocausal/thresholds.py SHA256 6e2c3888… is recorded in: [34 files, incl.
      auditor_report_001..010, comite_decision_001..023, hoja_de_ruta_*, preregistration_002/003]
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

Exit code: `0`. Unchanged from `auditor_report_010`; this mechanical pass does not detect the
semantic/logic issue this audit targets — that requires reading the code and prose directly (§3–§6).

## 3. Seal & freeze integrity

- `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
  (unchanged; confirms this audit's findings are about interpretation and code logic, not seal
  drift or Track-A contamination).

## 4. Reproducibility of published numbers

**The five certified `ε` values themselves are not in question** — `auditor_report_010` already
independently reproduced them bit-for-bit and verified their hash chain; nothing in this audit
contradicts that. What is checked here is whether the *code path* that assigns a terminal to a
given `ε`, and the *prose* that describes what a terminal means, are both sound.

**4.1 — Confirmed dead-code defect (ERROR).**

`dev/pr011_tv_certification_enumeration.py:327` and `:359` (primary and fallback branches of
`certify()`, both duplicate the same pattern):

```python
terminal = (
    TERMINAL_DISTINGUISHABLE
    if epsilon < 1.0
    else TERMINAL_INDISTINGUISHABLE
    if epsilon <= 0.0
    else TERMINAL_INCOMPLETE
)
```

`certified_tv_upper()` never returns a negative value (floors at `0.0`), so the only way to reach
`epsilon <= 0.0` is `epsilon == 0.0` — and `epsilon == 0.0` also satisfies `epsilon < 1.0`, which
is checked **first**. The `TERMINAL_INDISTINGUISHABLE` branch (`PAIR_INDISTINGUISHABLE_TV_ZERO`,
spec §8: **"valid negative result"**) is therefore **unreachable** for any input, by construction
of the `if/elif` order alone — not a rare edge case, a structural defect present since this code
was first committed (`873573f`, per the working tree; not re-derived from git blame this
session, `[UNVERIFIED — line-level blame not run]`, but the logic is unchanged across all
`certify`-touching commits `873573f`→`1fbbc6b`→`9a5e3df`→`d8ce482` per the diffs already verified
empty-for-the-generator in `auditor_report_010`).

**Live re-execution this session** (chair, in `dev/`, no seal contact, no repo write):

```
$ python3 -c "from dev.pr011_tv_certification_enumeration import certify; \
  r = certify(4, 0.95, 0.95 + 1e-9); print(r.terminal, r.epsilon_certified_upper, r.method)"
PAIR_DISTINGUISHABLE_AT_TRACTABLE_N 5e-11 HELLINGER_FALLBACK
```

For a pair separated by `Δτ=1e-9` — numerically and physically indistinguishable — the generator
reports `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` with `ε=5e-11`, **not** a `RuntimeError` from grid
instability (`H²` stability check passed cleanly, `~1.51e-22` on both `M=100` and `M=72` grids)
and **not** `PAIR_INDISTINGUISHABLE_TV_ZERO`. The dead branch is confirmed live, not just by static
reading.

**4.2 — Does this affect the five already-published certifications? No, not their numeric
validity — but yes, their interpretation.**

The five certified pairs all use the fixed pair `(τ0=0.95, τ1=1.05)`, `Δτ=0.1`, far from the
`Δτ→0` regime that triggered the dead branch above; none of them could have hit
`epsilon<=0.0` regardless (all five `ε` are strictly positive and would report
`TERMINAL_DISTINGUISHABLE` correctly under either branch ordering). **The dead-code defect does
not corrupt any published number.**

What *is* a real interpretive problem, independently confirmed by direct computation this
session: PR011's own §7 (`pr011_mass_distinguishability_viability.md:245-247`) states, in the
spec's own words, "If `ε` is **small**, masses are **hard** to distinguish (large minimax
floor)," and gives the formula `max_i P(any order-only estimator errs on τ) ≥ (1-ε)/2`. Applying
that formula to all five certified `ε` values:

| `n` | `ε_certified_upper` | minimax error floor `(1-ε)/2` |
|---|---|---|
| 4 | 0.004611899229 | **0.497694** |
| 5 | 0.005764874036 | **0.497118** |
| 6 | 0.006917848843 | **0.496541** |
| 7 | 0.008070823650 | **0.495965** |
| 8 | 0.009223798457 | **0.495388** |

Every certified rung of the ladder implies a minimax error floor between **49.5% and 49.8%** —
i.e., by the spec's own §7 machinery, any order-only estimator errs on `τ` roughly **as often as
a coin flip** at every `n` in `{4,...,8}`. This is the mathematically correct reading of "small
`ε`, hard to distinguish." Yet the terminal name emitted at every one of these five rungs is
`PAIR_DISTINGUISHABLE_AT_TRACTABLE_N`, and prose describing the closure reads, verbatim:

- `pr011_mass_distinguishability_viability.md:347`: "Frozen ladder `n ∈ {4,…,8}` **closed**
  (2026-07-14): every rung **certified distinguishable** with `ε < 1`."
- `research_program/README.md:72`: "PR011 **certificó** `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` en
  toda la escalera congelada `n ∈ {4,…,8}`... (`ε ≤ 0.00461`, ...; todos `< 1`)."

Both lines were **added or edited this session** (chair's own edits, ladder-closure commit
`d8ce482`), and both read naturally as "we established these masses are distinguishable," which
is the opposite of what the spec's own §7 formula computes from the same numbers. `§7` itself is
careful and correct ("PR011 viability requires `ε<1` (non-degeneracy), not `ε≈0`" —
`:246-247`); the defect is that this careful framing is not carried into §13's status summary or
into the downstream README, where the terminal *name* alone is left to do the talking, and the
terminal name is, on the numbers actually certified, misleading.

## 5. dev/validation separation & ground-truth leakage

Not implicated — this audit is about internal logical/terminological consistency of Track B's own
declared machinery, not about the sealed estimator or the hidden embedding. No leakage path found.

## 6. Claim-boundary check

- **ERROR-adjacent (code, §4.1):** the generator cannot emit one of its own five declared
  terminals (`PAIR_INDISTINGUISHABLE_TV_ZERO`) for any input — a structural asymmetry in the
  verdict space itself, not merely a documentation wording issue. This is the kind of "guardrail
  that cannot fail" `CLAUDE.md`'s first founding rule warns against: a generator that can only
  ever report the "distinguishable" family of terminals (`DISTINGUISHABLE`, `INCOMPLETE`) can
  never produce the negative result its own spec names as valid, no matter what pair is fed to it.
- **WARN (prose, §4.2):** `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N`, as named and as described in
  `§13`/`README.md:72`, reads as a positive distinguishability claim; the numbers it is attached to
  (minimax error floor ≈49.5-49.8%) support closer to the opposite reading under the spec's own
  §7 formula. This is not a 1+1D-vs-3+1D scope overclaim (`NO_RECONSTRUCTION_CLAIM` is not
  implicated — nothing here claims metric reconstruction or asymptotic horizon), but it is a
  statistical-confidence overclaim risk: a reader encountering only the terminal name and the
  §13/README prose, without working through §7's formula themselves, would reasonably conclude
  PR011 "successfully distinguishes" the two masses, when the certified numbers say the opposite
  — that at every tractable `n` tried so far, distinguishing them is almost exactly as hard as
  guessing.
- **OK:** the numeric `ε` values themselves remain correct, reproducible, and hash-verified
  (`auditor_report_010`); this finding is entirely about naming/interpretation layered on top of
  sound numbers, not about the numbers.
- **OK:** no claim in the audited text asserts metric reconstruction, an asymptotic/global event
  horizon, or a 3+1D result — the 1+1D finite-patch scope boundary itself remains intact.

## 7. Findings

| # | Severity | Finding | Anchor |
|---|---|---|---|
| 1 | ERROR | `certify()`'s terminal-selection `if/elif` chain makes `TERMINAL_INDISTINGUISHABLE` unreachable for any input — confirmed by live re-execution, not just static reading | `dev/pr011_tv_certification_enumeration.py:327,359`; live run `certify(4,0.95,0.95+1e-9)` → `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N`, `ε=5e-11` |
| 2 | WARN | All five published terminals are named/described as "distinguishable," but applying the spec's own §7 formula to the same five `ε` values yields a minimax error floor of 49.5-49.8% at every `n` — the numbers support "almost exactly as hard as a coin flip," not a positive distinguishability claim | `pr011_mass_distinguishability_viability.md:245-247` (formula) vs `:347` and `README.md:72` (prose); table in §4.2 above |
| 3 | OK | The five certified `ε` values themselves are correct, reproducible, and hash-verified — this audit's findings are about terminal semantics/code logic layered on top, not about the underlying numbers | `auditor_report_010` (prior, independently reproduced) |
| 4 | OK | Seal unchanged, Track A untouched, no ground-truth leakage, no 1+1D/3+1D scope overclaim | §3, §5, §6 |
| 5 | OK (carried forward, not double-counted) | `audit.sh` mechanical pass unchanged from `auditor_report_010` — same 22 pre-accepted heuristic warnings, no new mechanical finding | §2 |

AUDIT_ERRORS=1
AUDIT_WARNINGS=1

## 8. Verdict

The falsifier's finding from `comite_decision_023` is **confirmed real on both counts**: (1) a
genuine, reproducible code defect makes one of PR011's five declared terminals structurally
unreachable, and (2) the terminal name and its surrounding prose, including text added this
session, read as a positive distinguishability claim that the spec's own §7 formula — applied to
the same five certified `ε` values — actually contradicts (minimax error floor ≈49.5-49.8% at
every certified `n`). Neither finding corrupts the underlying `ε` numbers or crosses the
1+1D-finite-patch claim boundary, but the code defect is a structural asymmetry in the verdict
space (an ERROR by this project's own "guardrail that cannot fail is decoration" standard), and
the prose is at minimum misleading as currently worded. Both should be fixed — the code via a
corrected branch order (or an explicit justification if unreachability is somehow intended, which
nothing in the spec suggests), and the prose via language that states the certified upper bound
and its §7 consequence together, not the terminal name alone. Per this skill's own discipline, a
`/comite` session may not recommend `PROCEED` for PR012 (or any further unit) on top of this
`AUDIT_FAIL` until both are resolved — consistent with `comite_decision_023`'s own
`RECOMMEND_REVISE_AND_RECONVENE` verdict, reached independently before this audit ran.

AUDIT_VERDICT=AUDIT_FAIL
