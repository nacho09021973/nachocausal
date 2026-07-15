# OP-2.1 — Dev pre-registration: reference positive certifier

**Status:** `DEV_PREREGISTRATION / FROZEN_ON_COMMIT / NO_SCIENTIFIC_CLAIM`
**Authorized by:** `docs/comite/comite_decision_034_op21-certifier-opening.md` §9 (R1), PI
sign-off §11 (2026-07-15). Scope forks resolved by PI: top-level `certifier/` package (D3);
PR011 quarantined bench-only.
**Governing theory contract:** `research_program/work_packages/op13_positive_evidence_protocol.md`
(§3 fixed-sample Hoeffding certificate; §5 multiplicity; §6 generator error; §7
`SEQUENTIAL_STOPPING=FORBIDDEN`).

This document freezes, **before any Monte Carlo draw is executed by `certifier/` code**, the
synthetic laws, seeds, budgets, terminal precedence, return-state semantics, mutation-detection
power requirement and one-shot rule for the OP-2.1 reference bench. It is a *tool-verification*
pre-registration: nothing here is a physical experiment, a witness selection, or a scientific
confirmation. `POSITIVE_CERTIFIER_REFERENCE_PASS` licenses no physical, recovery or 3+1D claim
(op13:163-174, :207-208; plan:336,674).

## 1. Artefacts and location

- `certifier/` — new top-level package, **outside** `nachocausal/`. No pre-existing
  `nachocausal/*.py` file is edited (integrity snapshot: §8).
  - `certifier/kernel.py` — pure, stateless fixed-sample Hoeffding kernel (op13 §3).
  - `certifier/ledger.py` — manifest/ledger layer: frozen cell list, α-budget ledger, one-shot
    certification per cell, structural rejection of sequential use.
  - `certifier/bench.py` — reference bench: runs the frozen cells, computes exact reference
    miscoverage, evaluates the criteria of §5, emits exactly one terminal by the chain of §6.
  - `certifier/tests/test_op21_reference_certifier.py` — pytest suite (marker `op21_certifier`).
- Bench tests live under `certifier/tests/`, **not** under `tests/`, so the canonical `make test`
  (`pytest tests/`, `Makefile:9-10`) is untouched. This honours the binding constraint of
  decision 034 §9 R3 ("never inside canonical `make test`"); the letter of R3 named `tests/` with
  a marker, but with no pytest config file in the repo a marker cannot exclude a file from
  `pytest tests/`, so the directory split is the faithful implementation. A new Makefile target
  `op21-bench` (`python -m pytest -q certifier/tests`) is the only Makefile change.
- Docstring rule: every `certifier/` module states "Not part of the prereg-002 evaluation path."
  `certifier/` never imports `nachocausal.validate`, `nachocausal.estimator`,
  `nachocausal.generator`, `nachocausal.gate`, `nachocausal.scoring` or `nachocausal.c1_selector`
  (bench-enforced, §5 G6). Importing `nachocausal.thresholds` is allowed **read-only** for
  `assert_environment()` and seed-band constants.

## 2. Interface and return states (kernel)

```text
hoeffding_radius(m, alpha) = sqrt(log(4/alpha) / (2*m))            # op13:59-62

certify_tv_lower(stream_p, stream_q, alpha, eps_p, eps_q, precision_budget=None)
  -> Certificate(state, tv_lower, r_p, r_q, mu_p, mu_q, m_p, m_q, alpha, eps_p, eps_q)
```

- Input type firewall: `stream_p`, `stream_q` are 1-D float arrays with every value in `[0,1]`
  and finite; scalars only otherwise. The kernel accepts **no** poset, no `past_matrix`, no
  coordinates, no labels, no callables. Out-of-domain input raises `DomainError` (guard must be
  demonstrably able to fail: §5 G1). Per decision 034 D1 (strict reading), this proves
  *module-level* geometry-blindness only; it is never citable as end-to-end no-leakage.
- `TV_lower = max(0, |mu_p - mu_q| - r_p - r_q - eps_p - eps_q)` (op13:68-76).
- Distinct return states (decision 034 §9 R1; op13:122-133):
  - `BOUND_POSITIVE` — valid certificate, `tv_lower > 0`;
  - `ZERO_BOUND` — **valid vacuous certificate**, `tv_lower = 0`; not an abstention;
  - `ABSTAIN_PRECISION` — `precision_budget` declared and `r_p + r_q + eps_p + eps_q >
    precision_budget`; no bound reported;
  - `ABSTAIN_GENERATOR_ERROR` — `eps_p` or `eps_q` is `None` / not a finite float `>= 0`;
    **mandatory** abstention; no bound reported. The kernel never silently assumes `eps = 0`.

## 3. Ledger layer (what a stateless call cannot own)

`CertificationLedger(alpha_total)`:

- `register_cell(cell_id, m_p, m_q, alpha_j, eps_p, eps_q, precision_budget=None)` — consumes
  `alpha_j` from the budget; registering past `sum alpha_j <= alpha_total` raises
  `LedgerOverdraft` (op13:44,110-120). The cell list is closed with `freeze()`; registering after
  freeze raises.
- `certify_cell(cell_id, stream_p, stream_q)` — exactly once per cell; a second call raises
  `SequentialUseError`. Streams must have exactly the registered lengths `m_p, m_q`; a shorter or
  longer stream raises. There is **no** append/update/incremental entry point in the public API
  (op13:141-151, `SEQUENTIAL_STOPPING=FORBIDDEN`; the Howard et al. confidence sequence,
  arXiv:1810.08240, is NOT instantiated under OP-2.1).
- `manifest()` — op13:135-139 fields: commit SHA, numpy version, `uname`, RNG derivation rule,
  per-cell `(m_p, m_q, alpha_j, eps_p, eps_q)`, sha256 of each stream's bytes, kernel source
  hash, start/end timestamps.

## 4. Frozen bench design

### 4.1 Seed policy — new dedicated band

```text
SYNTH_MC_BAND = [3_000_000, 3_999_999]
```

- Disjoint from: dev sprinkling pool `EXPLORE_POOL = 1_000_000..1_000_039`
  (`docs/preregistration_002.md:18`); `DEV_SEEDS` 8-tuple (`nachocausal/thresholds.py:57`); the
  reserved virgin validation band `[2_000_000, 2_999_999]`
  (`docs/preregistration_002.md:14-30`, `nachocausal/thresholds.py:66-75`); and the burned
  prereg-001 set (`<= 65537`, `thresholds.py:63`). Verified unreserved this session:
  `grep -rn "3_000_000" nachocausal docs dev tests research_program` matches only the exclusive
  upper bound `arange(2_000_000, 3_000_000)` of the virgin draw.
- Derivation rule (frozen): the k-th declared cell (0-based, order of §4.2) uses
  `numpy.random.default_rng(3_000_000 + 1000*k)` for its P-stream and
  `default_rng(3_000_000 + 1000*k + 500)` for its Q-stream. The reproducibility re-run (§5 C3)
  reuses the SAME seeds (bit-exactness is the property under test). No other RNG source is
  permitted anywhere in `certifier/`.
- Sprinkling generators (`nachocausal.generator`) are never called: no causal-set sprinkling
  occurs in this bench.

### 4.2 Cells (all frozen; bench budget `alpha_total_bench = 0.50`)

Coverage/validity replications per cell: `N_REP = 200_000`. All laws are synthetic with
closed-form TV; witness streams are the raw draws (identity witness, values in `[0,1]`).

| cell_id | intended P vs Q | generated (tilde) | m_p=m_q | alpha_j | eps_p, eps_q | TV(P,Q) exact | purpose |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CELL-B1 | Bern(0.50) vs Bern(0.80) | same as intended | 200 | 0.01 | 0, 0 | 0.30 | positive-separation coverage |
| CELL-B0 | Bern(0.50) vs Bern(0.50) | same as intended | 200 | 0.01 | 0, 0 | 0.00 | null pair; false-positive rate |
| CELL-CAL | Bern(0.50) vs Bern(0.50) | same as intended | 50 | 0.25 | 0, 0 | 0.00 | calibration cell; mutant-A power |
| CELL-EPS | P = Q = Bern(0.50) | tilde_P=Bern(0.65), tilde_Q=Bern(0.35) | 200 | 0.10 | 0.15, 0.15 | 0.00 | ε-load-bearing cell; mutant-B power |
| CELL-U | Uniform[0,0.5] vs Uniform[0.5,1] | same as intended | 200 | 0.05 | 0, 0 | 1.00 | continuous laws; bound strictly below TV |
| CELL-PR011 | PR011 poset laws, τ=0.95 vs τ=1.05, n=4, grid_m=12 | same (enumeration-exact) | 200 | 0.04 | 0, 0 | `enum.enumerate_tv(4, 0.95, 1.05, grid_m=12).tv` | quarantined integration bench |

Notes.

- CELL-EPS: `TV(Bern(0.5), Bern(0.65)) = 0.15` exactly, so `eps = 0.15` is a **true certified
  bound**, not a declaration of convenience (op13:122-133). Intended TV is 0; any
  `tv_lower > 0` is a miscoverage event.
- CELL-U streams: P-draws `0.5*U`, Q-draws `0.5 + 0.5*U`, `U ~ Uniform[0,1)`. TV = 1 (disjoint
  supports); `|E_P f − E_Q f| = 0.5` with the identity witness — verifies the bound stays a
  *lower* bound strictly below TV.
- CELL-PR011 (quarantine, decision 034 D-PR011): poset laws are taken **read-only** from
  `dev/pr011_tv_certification_enumeration.py` (`build_diamond_family` → `copula_grid` →
  `poset_law_from_grid` → `normalize_law`), the same path exercised by
  `tests/test_pr011_tv_certification_enumeration.py`. The bench witness is
  `f_bench(poset) = |relations| / 6` (relation count of the `frozenset[(i,j)]` signature over
  `C(4,2) = 6` pairs) — **BENCH_ONLY_NON_PROMOTABLE**: `f_bench` is not a witness candidate, can
  never seed OP-2.2, and appears in no promotion, feature, orientation, frontier or abstention
  decision (op13:98-104). Sampling: `rng.choice` over the law's poset keys with the cell's frozen
  seeds. Validity check only (miscoverage ≤ alpha_j band); no physical statement of any kind.
  PR011 is not re-executed as confirmation (plan:326).

### 4.3 Exact reference miscoverage (the falsifier's power fix)

For each Bernoulli cell the bench computes, deterministically (math.comb / lgamma over the
`(m_p+1) x (m_q+1)` binomial support — no sampling, no scipy), the **exact miscoverage
probability of the correct kernel**:

```text
p0(cell) = P( max(0, |X/m_p − Y/m_q| − r_p − r_q − eps_p − eps_q) > TV(P,Q) ),
           X ~ Bin(m_p, tilde_p), Y ~ Bin(m_q, tilde_q) independent.
```

`p0` is computed with the frozen radius formula written in this document (§2), independently of
the kernel implementation under test.

## 5. Frozen criteria (all must be evaluated; PASS requires all of C1–C6 and G1–G6)

Coverage / calibration:

- **C1 (validity, per cell):** empirical miscoverage count over `N_REP` must satisfy
  `count <= N_REP * alpha_j` for every cell. (Hoeffding guarantees per-cell miscoverage
  `<= alpha_j`; the exact `p0` is far below `alpha_j`, so this band cannot mask an
  anti-conservative bug — C2 carries that power.)
- **C2 (calibration, per Bernoulli cell):**
  `count <= N_REP * p0 + max(5 * sqrt(N_REP * p0 * (1-p0)), 6)` with `p0` from §4.3. One-sided; a
  conservative implementation (count below band) is not a failure. The `max(., 6)` floor covers
  Poisson discreteness in cells with `N_REP * p0 < 1` and does not weaken mutant power (CELL-CAL
  band ≈ 240 vs mutant expectation ≈ 800).
- **C3 (reproducibility):** the entire bench runs twice with identical seeds; the sha256 of the
  canonical JSON report (sorted keys, repr floats) must be identical. Mismatch →
  `REFERENCE_REPRODUCIBILITY_FAIL`.
- **C4 (mutation power, binding — decision 034 falsifier test):** the same bench run against
  each mutant kernel MUST emit `REFERENCE_COVERAGE_FAIL`:
  - MUT-A: radius uses `log(2/alpha)` instead of `log(4/alpha)` (anti-conservative). Detection
    channel: C2 on CELL-CAL (exact `p0` ratio ≈ 4.6, `N_REP * p0 ≈ 175`, mutant expectation
    ≈ 800 ≫ band).
  - MUT-B: `eps` terms silently dropped. Detection channel: C1 on CELL-EPS (mutant miscoverage
    ≈ 0.86 ≫ `alpha_j = 0.10`).
  If either mutant PASSES the bench, the bench is decoration (`CLAUDE.md` founding rule) and **no
  OP-2.1 terminal may issue**; the prereg must be revised (v2) before any further run.
- **C5 (abstention semantics):** deterministic checks — `eps=None` → `ABSTAIN_GENERATOR_ERROR`;
  `precision_budget` smaller than `r_p+r_q+eps_p+eps_q` → `ABSTAIN_PRECISION`; a valid zero
  bound → `ZERO_BOUND` and never reported as an abstention. Each state is distinct in the report.
- **C6 (lower-bound sanity):** in every CELL-U replication, `tv_lower < 1.0` (= TV); and in every
  cell, `tv_lower >= 0`.

Guards (each must be demonstrably able to fail — the test suite includes a failing-input case for
every guard):

- **G1** `[0,1]`-domain guard raises on out-of-domain / non-finite input.
- **G2** numpy pin via `nachocausal.thresholds.assert_environment()` at bench start.
- **G3** seed-band guard: every RNG seed used is in `SYNTH_MC_BAND` and derived by the §4.1 rule;
  anything else raises.
- **G4** ledger overdraft (`sum alpha_j > alpha_total`) raises; post-freeze registration raises.
- **G5** sequential rejection: second `certify_cell` on the same cell raises; wrong-length stream
  raises; the public API exposes no incremental entry point (asserted by introspection).
- **G6** import firewall: `certifier/` modules do not import the sealed evaluation path
  (`nachocausal.validate|estimator|generator|gate|scoring|c1_selector`); asserted by reading the
  module sources in the test.

## 6. Terminal precedence chain (frozen; decision 034 §9 R1)

```text
POSITIVE_CERTIFIER_INVALID
  > REFERENCE_REPRODUCIBILITY_FAIL
  > REFERENCE_COVERAGE_FAIL
  > REFERENCE_PRECISION_ABSTAIN
  > POSITIVE_CERTIFIER_REFERENCE_PASS
```

- `POSITIVE_CERTIFIER_INVALID`: any guard G1–G6 found violated at bench time, ledger integrity
  broken, or manifest incomplete (op13:135-139).
- `REFERENCE_REPRODUCIBILITY_FAIL`: C3 fails.
- `REFERENCE_COVERAGE_FAIL`: C1, C2, C4 or C6 fails.
- `REFERENCE_PRECISION_ABSTAIN`: C5's abstention paths unreachable within declared resources
  (`N_REP` not computable on this machine), reported honestly instead of shrinking the bench.
- `POSITIVE_CERTIFIER_REFERENCE_PASS`: everything above holds.

The first applicable terminal is the only published terminal; other true conditions are recorded
as secondary diagnostics (mirrors op13:190-208). PASS, FAIL and ABSTAIN are reported alike
(plan:646-663): a FAIL terminal is committed and published with the same discipline as a PASS.

## 7. One-shot rule

- Exactly **one** terminal-issuing bench run is authorized, executed only after this document is
  committed (freeze) and R2/R3 code is complete, and followed by an `/auditor` pass before the
  terminal is recorded as the OP-2.1 outcome (decision 034 §9 R5–R6).
- Debug iterations before the terminal run are unrestricted dev work but may not be cited.
- If the terminal run fails or the mutation check exposes the bench, repairs reopen this prereg
  as `v2` (new commit, changes listed) — never a silent re-run ("reparar método; no cambiar
  target", plan:646-663).

## 8. Integrity snapshot (R4)

- Baseline recorded this session before any `certifier/` file existed: sha256 of all 11
  pre-existing `nachocausal/*.py` + `nachocausal/scoring/*.py`; `thresholds.py` =
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (= live seal,
  `make verify-seal` verified this session).
- After every OP-2.1 commit: re-run `make verify-seal` (must equal `6e2c3888…`) and re-hash the
  11 files (must all match the baseline). `git status` must show only: this file, `certifier/`
  contents, the `op21-bench` Makefile target, and the decision-034 brief.

## 9. What this pre-registration does NOT authorize

No physical confirmation; no witness selection or promotion (OP-2.2 closed); no PR012/PR013
action; no touching `thresholds.py`, prereg-002/003 or the seal; no validation/confirmatory seed;
no 3+1D code; no sequential stopping; no `n_star` measurement (OP-2.3 closed)
(plan:667-678; decision 034 §9 binding rules).
