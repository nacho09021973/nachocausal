# Auditor Report 026 — wp4-annex-c-variance-addendum-precommit

> Produced by `/auditor`. Backward-looking integrity audit: every published number, the seal, the
> dev/validation separation, and the claim boundary are checked against reality. The auditor
> REPORTS; it never edits the repo, never loosens a threshold, never re-runs a committing step.
> A weaker real result beats a strong fabricated one. Sibling skill: `/comite` (forward-looking
> deliberation).

## 1. Scope & target

Repo root `/home/adnac/nachocausal`, branch `main`, HEAD `90e3aad`, with three **modified,
uncommitted** files. Trigger: **precommit audit** of the §4b addendum (`zeta_1` and the `fixed_n`
variance) to WP4 Annex C.

Targets (all `M` in `git status --short`):

- `research_program/work_packages/wp4_comparable_pair_separation_checks.py` — new
  `h1_zeta1`, `var_S_n`, `_sample_D`, `S_n_moments_mc`, and checks `[10]`–`[13]`.
- `research_program/work_packages/wp4_comparable_pair_separation.md` — new §4b (Props C7, C8,
  Theorem C9, the §6.4 constant-level requirement), revised §5 items 3–4, revised §6 labels,
  headline addendum.
- `research_program/bibliography/ficha_se_busca_tv_order_only.md` — §2.2 points 3–4 revised.

Scope hint asked for: literal-output provenance of new numbers (with an independent re-check of two
rounded values the author says were already fixed); whether §5 item 3's closure is overstated;
honesty of Theorem C9's `[PROVED]`/`[NUMERICAL]` split; correctness and labelling of the
`zeta_1*Ibar >= kappa^2 dv^2/54` requirement including its `[UNVERIFIED]` reasoning; preservation of
"Forma L remains OPEN on channel items 1–2"; seal and separation untouched.

## 2. Mechanical audit

`bash .claude/skills/auditor/audit.sh`, exit code **0**, tail (full listing byte-identical to
reports 024 §2 and 025 §2):

```text
WARN: committed data file with no generator reference: data/reports/present_anchor_sanity_pilot.csv
WARN: committed data file with no generator reference: evidence/new_geometry_20260719/mink_control_metrics.csv
----------------------------------------
Auditor: 0 error(s), 23 warning(s)
```

Baseline unchanged: **0 errors, 23 warnings**, all pre-existing `data/reports/` and `evidence/`
generator-reference items, none attributable to this target (which adds no data file).

## 3. Seal & freeze integrity

| Item | Value | Anchor |
| --- | --- | --- |
| Live seal | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `make verify-seal` |
| Frozen record | `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` | `docs/preregistration_002.md:8` |
| Drift | **none** | — |

`nachocausal/thresholds.py` absent from `git status --short`. **OK.**

## 4. Reproducibility of published numbers

Script re-run twice: exit `0` both times, captures **byte-identical** (`diff -q`) — the new
Monte-Carlo in check `[12]` (`S_n_moments_mc`, seeds `4242+n`) is deterministic. Runtime ~9 s.

**Provenance sweep.** Every numeric literal with ≥3 decimals required to appear verbatim in a fresh
stdout capture:

- `wp4_comparable_pair_separation.md`: **25 literals, 0 unbacked.** The two rounded values the
  author reports fixing (`7.8e-16`, `9.1e-15`) are indeed gone; the note now carries
  `|diff| = 7.77e-16` and `9.10e-15`, matching check `[10]` exactly. Independently re-verified.
- `ficha_se_busca_tv_order_only.md`: 11 literals, 9 not in this script's output. **Not a finding.**
  `git diff | grep '^+'` shows **none** of the nine occurs in an added line — all are pre-existing —
  and each has its own provenance: `0.009223798457` is anchored with its exact generating command at
  `docs/plan_avanzado_14_julio_2026.md:55`
  (`python3 dev/pr011_tv_certification_enumeration.py certify --n 8`) and appears in
  `auditor_report_011` and `auditor_report_012`; `0.0125`, `0.025`, `0.0133` are PR012 ladder values
  cited to PR012 §4; the remaining five (`0902.0306`, `1104.1039`, `2503.01719`, `2507.01907`,
  `2607.05840`) are arXiv identifiers, not computed quantities.

**Individually confirmed against stdout:** `0.02733369969886`, `0.02777783467369`, `7.77e-16`,
`9.10e-15`, `0.000265`, `0.999852`, `9.754357e-03`, `2.399599e-07`, and the three MC sigmas
`0.73`, `0.31`, `0.14`. **OK.**

**Finding 2 (WARN) — three convergence ratios are rounded, not literal.** §4b states the
`zeta_1 - 1/36` halving ratios as "`2.17, 2.97, 3.44, 3.70, 3.85 -> 4`"
(`wp4_comparable_pair_separation.md:258-259`). Check `[11]` prints `2.1747, 2.9662, 3.4352, 3.7023,
3.8468`. `2.17` and `3.70` are truncations (and so appear verbatim), but `2.97`, `3.44` and `3.85`
are 2-decimal **roundings** and appear nowhere in the output. Distinct from report 024's finding 4
in one important respect: these roundings are correct and do **not** flatter the claim (the claim is
"ratio → 4"; rounding `2.9662` to `2.97` neither strengthens nor weakens it). Reported for
consistency with the standard applied in report 024, at the low end of WARN.

**Independent verification of the mathematics** (not a re-reading of the script's self-checks):

- *`zeta_1 -> 1/36`, second derivation.* Direct moments of `h_1 = uw + (1-u)(1-w)` on the unit
  square give `E[h_1] = 1/2`, `E[h_1^2] = 5/18`, hence `zeta_1 = 5/18 - 1/4 = 1/36` exactly. This
  route does not use the note's `h_1 = 1/2 + 2ab` substitution, so it is a genuine cross-check of
  Theorem C9's limit. **Confirmed.**
- *Hoeffding coefficient counting.* Brute-force enumeration of ordered pairs-of-pairs at
  `n = 4, 5, 8, 20` gives `24, 60, 336, 6840` sharing exactly one index, matching
  `C(n,2)*2(n-2)` in every case, with the disjoint class contributing `0` by independence. The
  formula `Var(S_n) = C(n,2)[2(n-2) zeta_1 + zeta_2]` is **confirmed** independently of the MC.
- *The §6.4 requirement.* Re-derived from scratch: minimising `B t - 1 + A/t^2` over `t > 0` gives
  critical `t = 2^{1/3} A^{1/3} / B^{1/3}` and minimum `3·2^{1/3} A^{1/3} B^{2/3}/2 - 1`, so
  non-negativity is `A B^2 >= 4/27`; substituting `A = 32 zeta_1/(kappa^2 dv^2)`, `B^2 = Ibar/4`
  yields `8 Ibar zeta_1/(dv^2 kappa^2) >= 4/27`, i.e. **`zeta_1 * Ibar >= kappa^2 dv^2 / 54`**.
  Matches the note exactly. **Confirmed.**
- *Proposition C8's corner claim.* Evaluated directly: `h_1(p) = 1.0` and `h_1(q) = 1.0` exactly,
  against `0.5497` at an interior point. **Confirmed.**

## 5. dev/validation separation & ground-truth leakage

- **Import surface unchanged** — `numpy`, `sympy`, `scipy.special.lambertw` only
  (`..._checks.py:32-34`). The new functions add no dependency.
- **No sealed-path contact.** Grep for `nachocausal|thresholds|seed_band` returns exactly one hit,
  the docstring disclaimer at line 11. No write path; no file produced.
- **The new Monte Carlo is not a bench run.** `S_n_moments_mc` samples continuum points to check a
  variance formula; it builds no causal set through the sealed generator, evaluates no estimator,
  consumes no reserved seed band (its seeds are literals `4242+n`, outside any prereg band), and
  its output is never persisted. It is quadrature verification, and the note says so.
- **Ground-truth leakage.** Still no hidden embedding and no observable — nothing for the rule to
  bind on. The orbit test (check `[6]`) still passes to `< 1e-15`.
- **Pause discipline.** Calculation only, per `docs/hoja_de_ruta_24_jul_2026.md` §2.1 and
  `docs/hoja_de_ruta_25_jul_2026.md` §3.1 (which pre-identified exactly this step). No roadmap §3/§4
  "No hacer" item breached. **OK.**

## 6. Claim-boundary check

**§5 item 3's closure is justified and not overstated.** Its three components each hold: `zeta_1 > 0`
rests on Proposition C8, whose proof is valid and whose corner values verify exactly; the `1/36`
limit is exact and independently re-derived; the finite-`n` variance formula is standard, verified by
brute-force combinatorics *and* by MC at `0.73`/`0.31`/`0.14` sigma. The note correctly keeps
`zeta_1`'s *value* at `[NUMERICAL]` (quadrature) while the limit is `[PROVED]`
(`...separation.md:288-290`). No overstatement.

**Theorem C9's label split is honest.** `[PROVED]` for the limit, `[NUMERICAL]` for the `O(dv^2)`
order — correct, since the order rests only on the ratio table converging to 4. The note also
volunteers that this is "one order better than `p` itself" (`:259-260`), which is accurate
(`p`'s correction is `O(dv)`).

**The `zeta_1*Ibar` requirement is correctly derived and correctly labelled.** It is stated as a
*requirement* derived from two bounds, explicitly flagged one-way ("violation would refute the
chain; satisfaction proves nothing", `:277-278`), explicitly "stated, not executed", and the
supporting `Ibar ~ C dv^2` argument is explicitly `[UNVERIFIED — reasoning, not computed]`
(`:281`). All three labels are the right ones.

**No over-claim toward reconstruction / 3+1D / asymptotic horizon.** Re-scan finds only disclaimers.
The seal, prereg-002 and the C1–C6 ledger remain explicitly untouched.

**Finding 1 (WARN, headline) — the note UNDER-claims: a `fixed_n` Forma L now follows, and §6's
`[OPEN]` label is wrong for that channel.** This is the one material defect found.

§5 item 2 (`...separation.md:317-320`) states that in `fixed_n` "a de-Poissonisation step is then
needed, and Reitzner–Schulte supply none. `[OPEN]`", and §6 labels "Forma L for candidate 7.1 —
`[OPEN]`". But de-Poissonisation is required only to import Reitzner–Schulte's *CLT*; it is **not**
required for the two-moment Chebyshev route, which ficha §6.3 explicitly offers and which needs
nothing the note has not already established. Concretely, at fixed `n`:

- `Delta_mu = C(n,2)|Delta_p|` exactly, `Delta_p != 0` by Corollary C6 (`[PROVED]`, small `dv`);
- `Var(S_n) = C(n,2)[2(n-2) zeta_1 + zeta_2] <= C(n,2)(2n-3)/4`, using only the **trivial** bounds
  `zeta_1 <= 1/4`, `zeta_2 <= 1/4` (both `h_1` and `f` take values in `[0,1]`) — §4b's exact
  `zeta_1` is not even needed;
- `S_n` is a function of the unlabelled poset, so data processing gives
  `TV(Q^n_tau, Q^n_tau') >= TV(L(S_n))`;
- Chebyshev at the midpoint therefore yields
  `TV(Q^n_tau, Q^n_tau') >= 1 - 4(2n-3)/(n(n-1) Delta_p^2) -> 1` as `n -> infinity` for a fixed pair.

This audit verified the inequality numerically: for `r_p=3, r_q=0.5, tau=1.0, tau'=1.2`, it gives
`TV >= 0.542689` at `n = 1.16e8` and `TV >= 0.954269` at `n = 1.16e9` (`dv = 4`), and
`TV >= 0.550001` / `0.955000` at `n = 1.36e9` / `1.36e10` (`dv = 0.02`). No CLT, no
Reitzner–Schulte, no de-Poissonisation is used anywhere.

`fixed_n`/`n -> infinity` is a **declared admissible regime** — ficha §1.3 mode 3, which the ficha
itself says "elimina el confusor de §1.2", i.e. precisely the obstruction of §5 item 1. And ficha
§3's Forma L asks only for `f_lambda -> 1` in a declared regime; it sets no requirement on the
constant. So on the note's own mathematics, Forma L (strong form) **is** obtained in the `fixed_n`
channel for this family, and the `[OPEN]` label is incorrect there.

Graded WARN, not ERROR: nothing asserted is false, no number is unbacked, and the error is in the
conservative direction — the opposite of the failure mode this skill exists to catch. But it is not
harmless. Status labels are how this repo routes effort, and a wrongly pessimistic one misroutes it
just as a wrongly optimistic one would: `docs/hoja_de_ruta_25_jul_2026.md` §3.2 currently ranks
"des-Poissonización" as the second priority and describes it as a blocker, which on this analysis it
is not. Two honest caveats belong in any restatement: the constant is enormous (`n ~ 10^8`–`10^10`
for the pairs computed, because `Delta_p` is small), and `Corollary C6`'s `dv_0` is non-effective,
so the `[PROVED]` version is asymptotic in `dv` while the named-pair version rests on `[NUMERICAL]`
`Delta_p`.

## 7. Findings

| # | Severity | Finding | Anchor (file:line / command) |
| --- | --- | --- | --- |
| 1 | WARN | Note under-claims: the `fixed_n` Chebyshev route gives Forma L (`f -> 1`) using only `Delta_p != 0` + trivial `zeta <= 1/4`, needing no CLT or de-Poissonisation; §5 item 2 presents de-Poissonisation as a blocker and §6 labels Forma L `[OPEN]`, both wrong for that channel | `...separation.md:317-320`, `:331`; ficha §1.3 mode 3, §3; audit's independent `TV >= 0.954269 @ n=1.16e9` computation |
| 2 | WARN | Three of five convergence ratios in §4b are 2-decimal roundings, not literal output (`2.9662 -> 2.97`, `3.4352 -> 3.44`, `3.8468 -> 3.85`); unlike report 024 finding 4, they do not flatter the claim | `...separation.md:258-259` vs check `[11]` |
| 3 | WARN ×23 | Pre-existing mechanical baseline (`data/reports/`, `evidence/` generator references) — **not attributable to this target** | `bash .claude/skills/auditor/audit.sh` (§2) |
| 4 | OK | The two previously-rounded values are genuinely fixed; note now carries literal `7.77e-16`, `9.10e-15` | `...separation.md:247-248` vs check `[10]` |
| 5 | OK | Provenance sweep: 25/25 note literals backed verbatim | `grep -F` over fresh capture |
| 6 | OK | The ficha's 9 script-unbacked literals are all pre-existing (absent from added lines) with their own generators/citations | `git diff`; `docs/plan_avanzado_14_julio_2026.md:55` |
| 7 | OK | Script deterministic incl. the new MC; exit 0 twice, captures byte-identical | `diff -q` over two captures |
| 8 | OK | `zeta_1 -> 1/36` independently re-derived by direct moments (`E[h_1^2] = 5/18`) | audit cross-check |
| 9 | OK | `Var(S_n)` coefficient `C(n,2)*2(n-2)` confirmed by brute-force enumeration at `n = 4, 5, 8, 20` | audit cross-check |
| 10 | OK | `zeta_1*Ibar >= kappa^2 dv^2/54` re-derived from scratch; matches the note exactly | audit cross-check |
| 11 | OK | Prop C8 corner claim exact: `h_1(p) = h_1(q) = 1.0` vs `0.5497` interior | audit cross-check |
| 12 | OK | §5 item 3's closure justified, not overstated; `zeta_1`'s value correctly left `[NUMERICAL]` | `...separation.md:288-290` |
| 13 | OK | Theorem C9's `[PROVED]` limit / `[NUMERICAL]` order split is honest | `...separation.md:255-260`, `:288-290` |
| 14 | OK | §6.4 requirement correctly labelled stated-not-executed, one-way, with `[UNVERIFIED]` reasoning flagged | `...separation.md:277-281` |
| 15 | OK | Seal unchanged and matching the frozen record | `make verify-seal`; `docs/preregistration_002.md:8` |
| 16 | OK | No new dependency, no sealed-path contact, no seed-band use, no persisted output from the new MC | `..._checks.py:32-34`; grep |
| 17 | OK | No over-claim toward reconstruction, 3+1D or asymptotic horizon; prereg-002 and the C1–C6 ledger untouched | re-scan of the note |

AUDIT_ERRORS=0
AUDIT_WARNINGS=25

## 8. Verdict

The §4b addendum is sound and, unusually, the only material defect runs the *other* way: the note
proves more than it claims. Every substantive number is literal script output, determinism holds
including the new Monte Carlo, and the four mathematical claims this audit could re-derive
independently — `zeta_1 -> 1/36`, the Hoeffding coefficient, the `zeta_1*Ibar` requirement, and
Proposition C8's corner values — all reproduce exactly. The `[PROVED]`/`[NUMERICAL]`/`[UNVERIFIED]`
labels on Theorem C9 and on the §6.4 requirement are correctly assigned.

Recommendation to the PI, in order:

1. **Act on finding 1 before the ficha is cited further.** Restate §5 item 2 to distinguish "blocks
   the Reitzner–Schulte CLT route" from "blocks Forma L", and re-label the `fixed_n` channel — with
   the two caveats named in §6 (enormous constant; non-effective `dv_0`). Then re-prioritise
   `docs/hoja_de_ruta_25_jul_2026.md` §3, whose item 2 is premised on de-Poissonisation being a
   blocker. Because this would change a Forma L status, it is a **`/comite` matter, not a text
   edit**: ficha §2.4 and roadmap §2.4 both route status changes of this weight through the
   committee, and `/comite` may legitimately conclude that an `n ~ 10^9` constant makes the result
   `PROVED_BUT_VACUOUS_IN_PRACTICE` and worth a weaker label than a bare `[PROVED]`.
2. Fix finding 2 (quote the printed ratios).

Findings 1 and 2 are text/labelling, not mathematics: no result needs recomputing. This audit is a
suitable foundation for the `/comite` that recommendation 1 requires.

AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS
