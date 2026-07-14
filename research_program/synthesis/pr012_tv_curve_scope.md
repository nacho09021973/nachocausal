# PR012 — Certified TV(τ0,τ1) vs Δτ curve at fixed n (draft scope)

**Status:** `DRAFT_SCOPE` — **not** `FROZEN`. Nothing in this document authorizes execution or
publication of a curve artifact. See §9 for what is and is not discharged.

## 0. Provenance note (read this before anything else)

This scope was set by a **direct PI scoping directive** (session of 2026-07-14, following
`docs/comite/comite_decision_023_pr012-scope-adjudication.md`), not by a second full `/comite`
session. The committee's `RECOMMEND_REVISE_AND_RECONVENE` verdict identified three open items
before any PR012 spec could be drafted; the PI reviewed the chair's synthesis of those items and
directed this exact scope directly: *"la idea de la curva TV(τ0,τ1) vs Δτ a n fijo (dentro de la
escalera tratable {4..8}), usar la cota correcta (BC^n) en vez de la actual, así como tener en
cuenta los puntos 1, 2 y 3."* This is a legitimate way to discharge G1 under this project's own
rule ("the committee proposes, the user authorises") — but it is **not** the same evidentiary
weight as a fresh multi-agent adversarial review, and this document says so plainly rather than
implying comité 023 itself endorsed this exact draft. A `/auditor` pass on this freeze text (G2a)
is still recommended before anything here is marked `FROZEN`.

## 1. Decision question

For the frozen family `G_◊` (PR011 §3) and channel `N=n` (PR011 §4), at a **fixed**, already
tractable `n`, how does the certified upper bound on `TV(P_n(τ0),P_n(τ1))` behave as a function of
`Δτ = τ1 - τ0`, holding `τ_center = (τ0+τ1)/2 = 1.0` fixed? This is candidate (a) of
`comite_decision_023` §8 — explicitly **not** an extension of the `n`-ladder (candidate b, shown
self-limiting: see §5 below) and **not** a switch to a Poisson-`ρ` channel (candidate c, a
different observable, out of scope here).

## 2. Resolution of the three items comité 023 left open

### 2.1 Item 1 — Theorem A's converse

**Resolved, already in the repo.** `research_program/models/first_witness_pair_candidates.md` §4
("Attempt C"), in the course of explaining why a horizon-existence witness pair fails, states and
uses as an established fact: *"For null-box models..., equal copulas mean the normalized measures
`Ω dU dV` agree after increasing reparametrizations of `U` and `V`... i.e. an isometry up to a
global constant scale... same copula implies isometric up to global scale — and an isometry
cannot turn a horizon-free patch into a horizon-containing one. ... the `TV=0` equivalence class
of a completion is exactly its scale orbit."* This **is** the converse PR012 needs: two patches
that are not related by a pure dilation `Φ_s` (i.e., not in the same scale orbit) cannot have
equal copulas, hence cannot have `TV=0`. PR012's `G_◊` pairs are never scale-related (fixed
absolute corners, only `τ` varies — PR011 §5's sanity check, re-verified per-point by
`dev/pr012_tv_curve_certification.py::assert_not_scale_related`), so every curve point is
genuinely `TV>0`, not merely "an upper bound below 1 by luck."

**Caveat, stated plainly:** this rigidity argument is presented in prose in a document about a
*different*, failed attempt (Attempt C), not given its own theorem number or a fully spelled-out
proof in the excerpt read this session. It is used there as established fact to derive a FAILED
verdict, which is internally consistent evidence that the repo's own authors treat it as solid —
but a future `/auditor` or `/comite` pass should consider promoting it to a properly labeled,
separately proved lemma (e.g. "Lemma: 2D copula rigidity") rather than PR012 continuing to lean on
an unlabeled paragraph. Not blocking for this draft; flagged for the eventual freeze pass.

### 2.2 Item 2 — Δτ_floor from an error model

**Resolved — and revised from the chair's initial estimate.** Two distinct floors exist (module
docstring, `dev/pr012_tv_curve_certification.py`):

- A deep floating-point/quadrature floor, `DELTA_TAU_FLOOR = 1e-9`, derived by comparing the
  measured `H²(Δτ)` against the proved Fisher/QMD asymptotic `(Δτ²/4)·Ībar`
  (`wp4_fisher_localization_floor.md`) across eleven decades of `Δτ`; the two track each other to
  within a stable ~2% (a genuine higher-order Taylor residual) until `Δτ≈1e-13`, where the ratio
  explodes. `1e-9` carries a >10,000x safety margin below that measured breakpoint.
- A much coarser, **already-frozen** floor that actually binds first in practice: PR011's own
  `verify_hellinger_stability` (`HELLINGER_H2_REL_TOL=1e-3`, comparing `M=100` vs `M=72` grid
  quadratures) rejects the two smallest points of §3's Δτ-ladder (`Δτ=0.0125, 0.025`) — see §4.
  This is not a new PR012 threshold; it is PR011's frozen instability guard doing its job.

Both floors are enforced; no curve point is certified below either. Points the coarser gate
rejects are reported as an explicit `GRID_RESOLUTION_ABSTAIN` row (§4), never silently dropped,
per the falsifier's requirement (`comite_decision_023` §5).

### 2.3 Item 3 — which object each point certifies

Every certified curve point (§4) reports, side by side, in one CSV row: the corrected certified
upper bound (`epsilon_certified_upper`, method `HELLINGER_FALLBACK_TENSORIZED`), the **superseded,
loose** bound for comparison (`epsilon_naive_linear_for_comparison` — never the certified value,
kept only as an audit trail against PR011's already-published numbers), and the §7-style
consequence (`minimax_error_floor = (1-ε)/2`) computed automatically, not left for a reader to
derive by hand as happened with PR011's original terminal-naming problem
(`auditor_report_011`). No row is ever labeled with a bare terminal name unaccompanied by its
numeric consequence.

## 3. Method: corrected tensorization (supersedes PR011's naive bound for any future work)

PR011's `HELLINGER_FALLBACK` computed `ε = ⌈n · TV_copula⌉`, an `n`-fold union/data-processing
bound — always valid, but generically loose, and loose by a **provable, non-negligible** factor
even at PR011's own tractable `n`: for the frozen `H²` this small,

```
TV_tensorized(n) / TV_naive(n) = 1/√n   (exact, to the precision this H² admits)
```

verified numerically at `n=4..8`: the ratio matches `1/√n` to 3-4 significant figures in each
case (`tests/test_pr012_tv_curve_certification.py::test_tensorized_bound_is_root_n_tighter...`).
At `n=8`, the corrected bound is **0.003261**, vs. PR011's published **0.009223798457** — a
~2.83x tightening, not a rounding-level correction. **This does not change any of PR011's five
published artifacts** (those remain as certified, under the method frozen at the time); it means
any *future* certification, including this one, should use the tensorized form:

```
BC = 1 - H²/2                         (Bhattacharyya coefficient, single copula sample)
BC_n = BC^n                            (exact tensorization under independence)
H²_n = 2(1 - BC_n)
TV_n <= sqrt(H²_n) · sqrt(1 - H²_n/4)  (same Le Cam step PR011 already uses, on the exact H²_n)
```

implemented in `dev/pr012_tv_curve_certification.py::bhattacharyya_tv_upper`.

## 4. Frozen numeric anchor

| Symbol | Value | Source |
|---|---|---|
| Geometry `G_◊`, corners, family range | reused verbatim from PR011 §3.1 | `dev/pr012_tv_curve_certification.py` imports, does not redefine, PR011's `R_P,V_P,R_Q,V_Q,TAU_FAMILY` |
| Channel | `N=n` conditioned, reused from PR011 §4 | same |
| `n` (fixed, not extended) | `8` | largest, most-audited rung of the already-closed PR011 ladder |
| `τ_center` | `1.0` | midpoint of `[0.8,1.2]` |
| `Δτ` ladder (frozen before any point computed) | `(0.0125, 0.025, 0.05, 0.1, 0.2, 0.4)` | fractions `{1/32,1/16,1/8,1/4,1/2,1}` of the full family span `0.4`; includes PR011's own `Δτ=0.1` as a cross-check |
| `DELTA_TAU_FLOOR` (hard, deep) | `1e-9` | §2.2 |
| `HELLINGER_H2_REL_TOL` (inherited, binds first) | `1e-3` | PR011 §6.1, unmodified |
| Method | `HELLINGER_FALLBACK_TENSORIZED` | §3 |

**Dry-run preview** (`python3 dev/pr012_tv_curve_certification.py curve --dry-run`, no artifact
written, reproduced this session):

| `Δτ` | `ε_certified` (tensorized) | `ε_naive` (superseded, for comparison) | minimax floor `(1-ε)/2` | terminal |
|---|---|---|---|---|
| 0.0125 | — | — | — | `GRID_RESOLUTION_ABSTAIN` |
| 0.025 | — | — | — | `GRID_RESOLUTION_ABSTAIN` |
| 0.05 | 0.001629425461 | 0.004608713846 | 0.499185 | `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` |
| 0.1 | 0.003261097632 | 0.009223798457 | 0.498369 | `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` |
| 0.2 | 0.006542987366 | 0.018506536254 | 0.496729 | `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` |
| 0.4 | 0.013307085972 | 0.037639580996 | 0.493346 | `PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` |

Note the naive column at `Δτ=0.1` reproduces PR011's published `n=8` value
(`0.009223798457`) exactly — a live consistency check that this module correctly reuses PR011's
frozen anchor rather than drifting from it.

**Reading the table honestly (per §2.3):** every minimax floor is still ≈0.49-0.50 — i.e., even
at the widest frozen Δτ (0.4, the full family span), an order-only estimator at `n=8` errs on `τ`
almost as often as a coin flip. This curve does not show PR011's pair becoming "easy" to
distinguish; it shows *how little* the certified bound moves across the entire frozen family, and
that the previously-used naive method overstated the difficulty by a `√n`-scale factor throughout.

## 5. Why not extend `n` instead (candidate b, rejected)

Discussed at length with the PI this session, reproduced here for the record. The naive bound
becomes vacuous (`ε≥1`, uninformative) around `n≈868`; the corrected tensorized bound is far
better behaved but still requires `n` on the order of `10⁵`–`10⁷` before approaching `TV≈1` for
this pair's `H²`. Both regimes are far outside anything the primary exact-enumeration route could
ever reach (already fails to converge at `n=8`) or that a certifiable method (excluding raw
simulation, per PR011 §6) could touch. Fixing `n=8` and varying `Δτ` instead stays inside the
already-audited, already-tractable regime and asks a question actually answerable with existing
tools.

## 6. Claim boundary

Same as PR011's (§2.2): not a recoverability benchmark, not absolute-unit mass estimation
(Theorem A still blocks that channel), not metric reconstruction, not a 3+1D result. Additionally,
per `auditor_report_011`'s lesson: **no curve point's terminal name may be read in isolation** —
`PAIR_DISTINGUISHABLE_AT_TRACTABLE_N` names only "a non-degenerate upper bound `ε<1` was
certified," never "this pair is easy to tell apart." Every published row carries its minimax-floor
consequence alongside the terminal for exactly this reason.

## 7. Reused artifacts / new artifacts

- Reused, unmodified: `dev/pr011_tv_certification_enumeration.py` (`build_diamond_family`,
  `certified_tv_upper`, `terminal_for_epsilon`, `verify_hellinger_stability`, frozen constants).
- New: `dev/pr012_tv_curve_certification.py` (`sanity`, `curve --dry-run`, `curve`); would publish
  a single `data/reports/pr012_tv_curve_n8.csv` + `.sha256` (one file for the whole curve, not
  one-per-point — addresses the reproducibility engineer's flagged artifact-shape gap from
  `comite_decision_023`).
- New: `tests/test_pr012_tv_curve_certification.py`, 16 tests, all passing; full PR011+PR012
  suite (34 tests) green; `make verify-seal` unchanged (`6e2c3888…`) throughout.

## 8. Gates

| Gate | Requirement | Status |
|---|---|---|
| G0a | Spec document freeze | **DRAFT** — this document, not yet frozen |
| G1 | `/comite` on numeric anchor | Discharged via direct PI scoping directive (§0), not a fresh multi-agent session — flagged, not hidden |
| G2a | `/auditor` on freeze text | **OPEN** — recommended before `FROZEN` |
| G2b | `/auditor` on any reported `ε`/terminal, pre-publication | **OPEN** — the dry-run numbers above are a preview, not a certification; publishing `data/reports/pr012_tv_curve_n8.csv` is a committing step requiring explicit authorization, same as PR011 §10 |
| G3 | Tsybakov/Le Cam literature check if cited | inherits PR011's OPEN status, never triggered |

**Nothing here authorizes running `curve` without `--dry-run`, or calling `publish_curve()`.**

## 9. What remains open

- G2a/G2b `/auditor` passes before freeze/publication.
- The Theorem-A-converse rigidity argument (§2.1) deserves promotion to a named, separately proved
  lemma rather than continuing to rest on an unlabeled paragraph in a different section's writeup.
- Whether `n=8` is the right fixed anchor, vs. presenting the same curve at each of PR011's five
  already-certified `n` values, is a presentation choice not yet decided.
