# PR011 — Mass distinguishability viability (theoretical–computational unit)

**Status:** `FROZEN_VIABILITY_SPEC`

**Freeze record:**

- G1: `docs/comite/comite_decision_022_pr011-viability-freeze-readiness.md` (user sign-off
  2026-07-14: spec freeze authorized)
- G2a (freeze text): `docs/auditor/auditor_report_007_pr011-viability-freeze-text.md`
  (`AUDIT_PASS_WITH_WARNINGS`, 2026-07-14)
- G2b (pre-execution `ε`): `docs/auditor/auditor_report_008_pr011-g2b-pre-execution-epsilon.md`
  (`AUDIT_PASS_WITH_WARNINGS`, 2026-07-14)

**G2b tier-1 (2026-07-14):** `HELLINGER_FALLBACK` certification on frozen ladder —
`n=4`: `ε ≤ 0.004611899229`; `n=5`: `ε ≤ 0.005764874036` (both `< 1`); terminal
`PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` at each certified `n` (§13).

**Normative status:** This is a **viability specification**, not a preregistration, not a blind
validation run, and not authorization to execute production science. It does not modify PR010,
the sealed path, or any frozen preregistration. **G0a:** this spec document is frozen as
`FROZEN_VIABILITY_SPEC`. **G0b:** PR010 closed (`PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`,
2026-07-14). **G2b** discharged: provisional audit (`auditor_report_008`); tier-1 closure via
`HELLINGER_FALLBACK` (`auditor_report_009`, 2026-07-14) — see §13.

**Series placement:** PR011 is **not** an observable/recoverability protocol (unlike PR008–PR010).
It is the first **theoretical–computational viability** unit in the identifiability track (WP4). It
answers whether a fully frozen 1+1D Schwarzschild family, at fixed cardinality, admits **certified
statistical distinguishability** between two preselected masses — and hence whether minimax
estimation of `τ = R_H = 2M` is **non-vacuous** at tractable `n`.

**Anchors:**

- Program synthesis: `research_program/synthesis/geometric_indeterminacy_decision.md`
- Two-point theorem (PROVED): `research_program/work_packages/wp4_two_point_theorem.md`
- Diamond family (regularity PROVED): `research_program/work_packages/wp4_fisher_localization_floor.md` §4–5
- Scale degeneracy (TV = 0): `research_program/models/first_witness_pair_candidates.md` §2 (Theorem A)
- Evidence tiers: `research_program/work_packages/wp3b_identifiability_criteria.md` §7

## 1. Decision question (frozen when PR011 opens)

In a **fully frozen** 1+1D Schwarzschild causal-diamond family `G_◊` (§3), with observation channel
**order-only conditioned on `N = n`**, and target `T(τ) = τ = 2M`:

> For a pair of masses `(M_0, M_1)` chosen **before** any PR011 computation from a declared
> theory-only rule (§5), can one **certify** an upper bound
> `TV( P_n(τ_0), P_n(τ_1) ) ≤ ε` with `ε < 1` at some **tractable** `n` in the frozen ladder
> (§4.4)?

Equivalently: is binary distinguishability **non-degenerate**, and is scalar estimation of `τ`
**not** killed by the scale orbit (`TV = 0`)?

This is **viability**, not performance of any estimator.

## 2. What PR011 is and is not

### 2.1 PR011 is

- A **freeze** of one admissible geometry class (diamond EF family) and one observation channel.
- A **certification attempt** on `TV` (or exact `TV`) between two fixed parameter values.
- A **gate** for later work: if viability fails (`TV = 0` or certification infeasible), a mass-
  estimation prereg must not open; if viability passes, a separate certification/scaling prereg may
  be proposed.

### 2.2 PR011 is not

- A recoverability benchmark (`prereg-002` style).
- An operational floor on the sealed estimator (`prereg-003` (★)).
- A new observable design (PR009/PR010 lineage).
- A classifier accuracy study, histogram overlap, or seed ensemble without a TV bound.
- A claim that failure to distinguish implies physical indeterminacy without an **upper** bound
  on `TV`.
- Estimation of `R_H` in **absolute units** independent of the frozen coordinate chart (Theorem A
  blocks that channel; target is `τ` **within** `G_◊`).

## 3. Frozen geometry class `G_◊` (to be locked at PR011 freeze)

**Family of record:** causal diamonds in ingoing Eddington–Finkelstein `(v, r)` with metric

```math
g_\tau = -\left(1 - \frac{\tau}{r}\right) dv^2 + 2\,dr\,dv,
\qquad \tau = 2M = R_H,
```

**Construction** (from `wp4_fisher_localization_floor.md` §4; parameters frozen at PR011 open):

1. Fix corners `p = (v_p, r_p)` (exterior) and `q = (v_q, r_q)` (interior) with
   `0 < r_q < \tau_0 \leq \tau_1 < r_p` and `v_p < v_q`.
2. For each `\tau \in [\tau_0, \tau_1]`, patch `D_\tau = J^+_\tau(p) \cap J^-_\tau(q)` (nonempty
   diamond straddling `\tilde U = 0`).
3. Sprinkling: Poisson intensity `\rho` w.r.t. `dv\,dr` on `D_\tau` (`\det g = -1`).
4. Observed object: isomorphism class of the induced unlabeled poset.

**Explicit exclusions (binding):**

- No fixed Kruskal box (Prop. 1 degeneracy, `I \equiv 0`).
- No patches related by scale diffeomorphism `\Phi_s` across the compared pair (Theorem A, `TV = 0`).
- No set-valued horizon target in PR011 (scalar `τ` only).

### 3.1 Numeric anchor (filled — source: shape **A moderate**)

**Provenance:** `wp4_fisher_localization_floor.md` §5a; reproduced numerically in
`research_program/work_packages/wp4_kappa_numeric_reference.py` (lines 136–137, shape label
`A moderate`). Geometry sanity: `dev/pr011_freeze_sanity_check.py` → `PR011_FREEZE_SANITY=PASS`.

| Symbol | Frozen value | Notes |
|---|---|---|
| `v_p, r_p` | `(0.0,\ 2.0)` | exterior corner `p` |
| `v_q, r_q` | `(1.0,\ 0.5)` | interior corner `q` |
| `[\tau_0^{\mathrm{fam}}, \tau_1^{\mathrm{fam}}]` | `[0.8,\ 1.2]` | compact parameter range for `G_◊` |
| `V(\tau=1)` | `≈ 1.471720` | diamond area at reference (`det g = -1`); kappa script |
| `\kappa(\tau=1)` | `≈ 7.97\times 10^{-4}` | `V \cdot I`; informational cross-check only |
| `\rho` | **not used** | channel is `N=n` conditioned; law = normalized volume on `D_\tau` |
| `n` ladder | `{4, 5, 6, 7, 8}` | attempt in ascending order; stop early if infeasible |

**Constraint verification** (all `\tau` in family range and certification pair):

- `r_q < \tau < r_p` for `\tau \in \{0.8, 0.95, 1.0, 1.05, 1.2\}`;
- `\tilde U_p < 0 < \tilde U_q` (horizon straddle) at each checked `\tau`.

### 3.2 Certification pair derived from §5 (pre-committed numerics)

| Quantity | Value |
|---|---|
| `\tau_{\mathrm{center}}` | `1.0` (midpoint of `[0.8, 1.2]`) |
| `\delta_\tau^{\mathrm{commit}}` | `(1.2 - 0.8)/4 = 0.1` |
| `\tau_0` (cert) | `0.95` |
| `\tau_1` (cert) | `1.05` |
| `M_0` | `0.475` |
| `M_1` | `0.525` |
| `\Delta\tau` | `0.1` |
| `\Delta M` | `0.05` |

Pair rule name: `MIDPOINT_QUARTER_SPAN` — separation fixed in parameter space, not from data.

## 4. Observation channel and laws

### 4.1 Channel (Family C, order-only)

- Input: unlabeled poset `C_n` on `n` elements.
- **Conditioned law:** `P_n(\tau) := \mathrm{Law}(C_n \mid N = n)` under sprinkling on `D_\tau`.
- Sample space: isomorphism classes of `n`-element posets (`\Omega_n`).

Lemma 0 (`first_witness_pair_candidates.md`): given `N = n`, points are i.i.d. from normalized
volume on `D_\tau`; poset is a function of the induced causal order.

### 4.2 Cardinality discipline

Both compared models use the **same** `n`. Poisson cardinality leak is closed by conditioning.
Do **not** compare laws on different `n` without an explicit joint formulation.

### 4.3 Target

```math
T(\tau) = \tau = 2M.
```

Report masses only as `M = \tau/2` after `\tau` is certified; no absolute-unit claim outside `G_◊`.

### 4.4 Tractable `n` ladder (frozen)

```text
n ∈ {4, 5, 6, 7, 8}
```

**Attempt order:** `4 → 5 → 6 → 7 → 8`. Stop at the first `n` where §6 primary method closes with
`ε < 1`, or emit `INFEASIBLE_AT_TRACTABLE_N` if none succeed.

No production-scale simulation in PR011.

## 5. Mass-pair selection rule (theory-only, pre-committed)

The pair `(M_0, M_1)` must be chosen **without** reading:

- PR009 internal outputs;
- PR010 coverage artifacts;
- any sealed validation seed result;
- any dev ensemble tuned to maximize or minimize separation.

**Frozen rule:** `MIDPOINT_QUARTER_SPAN`

1. Family range `[\tau_0^{\mathrm{fam}}, \tau_1^{\mathrm{fam}}] = [0.8, 1.2]`.
2. `\tau_{\mathrm{center}} = (\tau_0^{\mathrm{fam}} + \tau_1^{\mathrm{fam}})/2 = 1.0`.
3. `\delta_\tau^{\mathrm{commit}} = (\tau_1^{\mathrm{fam}} - \tau_0^{\mathrm{fam}})/4 = 0.1`.
4. Certification pair: `\tau_0 = \tau_{\mathrm{center}} - \delta/2 = 0.95`,
   `\tau_1 = \tau_{\mathrm{center}} + \delta/2 = 1.05`; masses `M_i = \tau_i/2`.

Numeric values in §3.2. **Not** chosen to minimize TV post-hoc.

**Sanity check (mandatory before certification):** confirm the two patches `D_{\tau_0}` and
`D_{\tau_1}` are **not** scale-related by `\Phi_s`. In the diamond family they are not if corners
are fixed and only `\tau` varies — unlike Theorem A.

## 6. Certification methods (acceptable for PR011)

PR011 succeeds only with a **certified upper bound** `ε` on `TV(P_n(\tau_0), P_n(\tau_1))`
(WP3b §7 tier 1–4). Acceptable routes, in preferred order:

1. **Exact enumeration** on `\Omega_n` for small `n`: compute masses `p_{\tau}(c)`, sum
   `\frac12 \sum_c |p_{\tau_0}(c) - p_{\tau_1}(c)|` with certified rounding error.
2. **Explicit coupling** on a common latent space: construct a coupling of `n` sprinklings whose
   poset laws marginalize correctly; bound `\Pr(\text{posets differ}) \leq \varepsilon`.
3. **KL / Hellinger chain** from copula densities `c_\tau` (diamond Lemma R): bound
   `H^2(c_{\tau_0}, c_{\tau_1})` or `KL`, then `TV` via `wp4_two_point_theorem.md` Obs. 5.3.
   Data processing to posets requires Lemma 1 (poset is function of copula sample).

**Explicitly insufficient for PR011 closure:**

- Simulation without certified approximation theorem linking simulated law to `P_n(\tau)`.
- Classifier accuracy, AUC, or histogram overlap without TV bound.
- Lower bound on TV only (falsifies small-ε claims; does not establish viability alone unless
  combined with upper bound showing `ε < 1`).

### 6.1 Numerical error budget (frozen)

| Route | Budget | Failure |
|---|---|---|
| **Primary — enumeration** | exact rational masses where feasible; else float sum with per-term `1e-15` and reported `TV` rounded **up** at `1e-12` | gap `> 1e-12` on any checked `n` |
| **Fallback — copula Hellinger** | grid `N=100`, unit-square `M=18`; symmetric `\delta` scan `{0.04, 0.02, 0.01}`; require `I` stability `< 0.1%` (kappa script protocol) | instability or gap `> 1e-6` on `V` cross-check |
| **Surrogate law** | not permitted in PR011 unless a new approximation theorem is frozen | default `CERTIFICATION_INCOMPLETE` |

**Primary method (frozen):** exact enumeration on `\Omega_n`, starting at `n=4`.

**Compute ceiling (soft):** if exact enumeration of `\Omega_n` is not completed within **one
foreground hour** on one CPU core at a given `n`, skip to next `n` or emit
`INFEASIBLE_AT_TRACTABLE_N` — no distributed search, no GPU.

## 7. Interpretation machinery (pre-registered consequences)

If a certified bound `TV(P_n(\tau_0), P_n(\tau_1)) \leq \varepsilon` with `\varepsilon < 1` is
obtained, the two-point theorem (`wp4_two_point_theorem.md` §3) implies:

```math
\max_i P_{\tau_i}\!\left(\text{any order-only estimator errs on } \tau \right)
\geq \frac{1 - \varepsilon}{2}.
```

For metric risk on `T(\tau) = \tau` (`geometric_indeterminacy_decision.md` §6.2):

```math
\mathcal R_n^* \geq \frac{\Delta\tau}{4}(1 - \varepsilon),
\qquad \Delta\tau = |\tau_1 - \tau_0|.
```

If `\varepsilon` is **small**, masses are **hard** to distinguish (large minimax floor). If
`\varepsilon` is **close to 1**, they are **easier**. PR011 viability requires `\varepsilon < 1`
(non-degeneracy), not `\varepsilon \approx 0`.

**Cross-check with Fisher annex:** for the same family, a proved **lower** floor
`\delta\tau \sim \ell / \sqrt{\kappa}` may apply (`wp4_fisher_localization_floor.md` §5a). PR011
does not re-prove that floor; it **certifies the actual TV** at named `(n, \tau_0, \tau_1)`.

## 8. Terminals (precedence at close)

Emit **exactly one** primary terminal:

| Terminal | Meaning |
|---|---|
| `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` | Certified `TV \leq \varepsilon < 1` at some frozen `(n, \tau_0, \tau_1)` |
| `PAIR_INDISTINGUISHABLE_TV_ZERO` | Proved `TV = 0` (scale degeneracy or bad freeze) — **valid negative result** |
| `CERTIFICATION_INCOMPLETE` | Methods exhausted; no certified upper bound; **not** a mass-estimation go |
| `INVALID_FREEZE` | Family violates §3 exclusions (e.g. Kruskal box smuggled in) |
| `INFEASIBLE_AT_TRACTABLE_N` | Tractable `n` ladder too small for any method in §6 |

Secondary annotations (non-terminal): `ε` value, `n` used, method tier (enumeration / coupling / KL).

**No terminal** implies authorization for a blind mass-estimation experiment.

## 9. Deliverables (no scientific execution in this draft)

When PR011 is authorized after freeze:

1. **Freeze record** — numeric corners, `\tau` range, `n` ladder, pair rule, error budget.
2. **Certification report** — `TV` bound or exact value, method, error budget audit trail.
3. **Interpretation note** — map to §7; state regime A/B per `geometric_indeterminacy_decision.md`
   §12 if a scaling ladder is included (optional extension, not required for viability).
4. **Provenance header** — commit, seal SHA (`make verify-seal`), explicit “no sealed validation /
   no PR009–PR010 inputs”.

**Implementation locus (not authorized until G0–G2 + user sign-off):**

- `dev/pr011_freeze_sanity_check.py` — geometry-only checks (**exists**, PASS at anchor);
- `dev/pr011_tv_certification_enumeration.py` — `falsifier`, `probe`, `certify` (§6.1 fallback);
- `data/reports/pr011_tv_certification_n4.csv`, `pr011_tv_certification_n5.csv` — tier-1
  certification (2026-07-14);
- no changes to `nachocausal/thresholds.py` or sealed estimator.

## 10. Gates (split per comité 022 §8)

| Gate | Requirement | Status |
|---|---|---|
| **G0a** | Spec document freeze (`FROZEN_VIABILITY_SPEC`) | **DISCHARGED** (comité 022 + user sign-off) |
| **G0b** | PR010 closed under its own rules — required for **TV certification execution** | **DISCHARGED** (`PR010_DESIGN_INFEASIBLE_REFERENCE_COVERAGE`, 2026-07-14) |
| **G1** | `/comite` on numeric anchor §3.1, §5, §6.1 | **DISCHARGED** (comité 022) |
| **G2a** | `/auditor` on freeze text (claim boundary, anchor numbers) | **DISCHARGED** (`auditor_report_007`, `AUDIT_PASS_WITH_WARNINGS`) |
| **G2b** | `/auditor` on any reported `ε` or viability terminal (pre-execution) | **DISCHARGED** (`auditor_report_008`–`009`; tier-1 `ε` certified) |
| **G3** | Tsybakov/Le Cam in `biblioteca/` if external memo cites them | **OPEN** |

Spec freeze does **not** authorize running TV certification or emitting a viability terminal.
Tier-1 `ε` at `n=4` closed via `HELLINGER_FALLBACK` (2026-07-14). Ladder `n > 4` and blind
mass-estimation remain separate authorization units.

## 11. Relation to later units (out of scope for PR011)

| Later unit | Opens if PR011 terminal is |
|---|---|
| PR012 (or named certification scaling) | `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` — extend `n`, `\rho` ladder with prereg |
| Mass-estimation prereg | Same + certified TV curve vs `\Delta\tau` |
| Set-valued horizon extension | Only after scalar `τ` viability and separate spec |

## 12. Freeze checklist

| Item | Status |
|---|---|
| Diamond corners `(0,2)`, `(1,0.5)` | **FILLED** §3.1 |
| Family range `[0.8, 1.2]` | **FILLED** §3.1 |
| Certification pair `(0.95, 1.05)` / masses `(0.475, 0.525)` | **FILLED** §3.2 |
| Pair rule `MIDPOINT_QUARTER_SPAN` | **FILLED** §5 |
| `n` ladder, primary method, error budget | **FILLED** §4.4, §6.1 |
| Spec freeze (G0a) | **DISCHARGED** |
| PR010 closed (G0b) | **DISCHARGED** |
| `/comite` (G1) | **DISCHARGED** |
| `/auditor` freeze text (G2a) | **DISCHARGED** |
| `/auditor` pre-execution `ε` (G2b) | **DISCHARGED** (`auditor_report_008`) |
| Tier-1 `ε` at `n=4` (`HELLINGER_FALLBACK`) | **CLOSED** (2026-07-14) |
| Tier-1 `ε` at `n=5` (`HELLINGER_FALLBACK`) | **CLOSED** (2026-07-14) |
| Viability terminal `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` | **EMITTED** at `n=4`, `n=5` |
| Ladder `n ∈ {6,7,8}` / mass-estimation prereg | **OPEN** |

Nothing in §3–§6 was selected using PR009 or PR010 scientific outputs.

## 13. Current status

```text
PAIR_DISTINGUISHABLE_AT_TRACTABLE_N — method=HELLINGER_FALLBACK — hellinger_M=100
n=4  epsilon_certified_upper = 0.004611899229  primary_nominal_tv ≈ 0.001440 (grid_m=12)
n=5  epsilon_certified_upper = 0.005764874036  primary_nominal_tv ≈ 0.001888 (grid_m=8)
H2 = 1.329351347556e-06  (cross-check M=72, rel_gap < 0.1%)
```

Artifacts: `data/reports/pr011_tv_certification_n4.csv`, `pr011_tv_certification_n5.csv` (+ `.sha256`).
Generator: `python3 dev/pr011_tv_certification_enumeration.py certify --n N`.
Audits: `auditor_report_008`–`009`.