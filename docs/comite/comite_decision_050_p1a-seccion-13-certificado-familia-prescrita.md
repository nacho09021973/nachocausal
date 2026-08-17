# Comité Decision 050 — p1a-seccion-13-certificado-familia-prescrita

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Adjudicate §13 of `emergencia/P1a_puerta_teorica_en_Minkowski.md` (HEAD `649505d`, branch
`emergencia/p1a-canal-sigma-m`): the "prescribed family" uniqueness certificate claiming
`Pr(S) >= e^{-o(n)}` for even `n`.

Primary charge to the falsifier, priority over everything else: **is the mathematics of §13
correct?** The two load-bearing lemmas are Lemma 13.7 (the planted quadruple sits at
`u_-=u_+=v_-=v_+=1/2` of the free landscape *exactly*) and Lemma 13.11 (the trichotomy of rivals;
is the case split exhaustive?). Break both with explicit small-even-`n` counterexamples if
possible.

Secondary: (1) is replacing dyadic peeling with a single global bound sound? (2) does Lemma
13.10's union over index rectangles really neutralise the selection-induced dependence
`CLAUDE.md` warns about? (3) does the result justify its entropic cost, given that Advertencia
13.16 shows the target it was built to serve (`P_{2,n} -> 0`) is true-and-empty? (4) given Braun
(`d>=3`) and Madsen (`d>2`) exclude `d=2`, does further 1+1D investment make sense, or does the
3+1D gate come first?

**Independence context, declared to every role:** §13 and audit 031 were both written by the
chair in this same session. Roles were instructed to treat the text as suspect by default and not
to accept a verification merely because the text asserts it was performed.

## 2. Verified state

Facts checked **this session**, each with its command / file:line.

- **Seal intact.** `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching
  `docs/preregistration_003.md:9` and `docs/preregistration_002.md:8`. Independently re-run by the
  pre-registration warden with the same result. §13 touches no sealed path.
- **Git.** Branch `emergencia/p1a-canal-sigma-m`, HEAD `649505d`, working tree clean
  (`git status --porcelain` empty), 0 ahead / 0 behind `origin` — i.e. **already pushed**.
- **Prior audit.** `docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md`,
  `AUDIT_VERDICT=AUDIT_FAIL`. Its single ERROR (contradictory live flag values) was remediated in
  `649505d`; chair verified 6 lines now carry the `[SUPERSEDED — ver §13.7]` prefix
  (`P1a_puerta_teorica_en_Minkowski.md:908-913`). Its findings 13 and 14 (`NOT VERIFIED`) were the
  object of this committee. **Finding 14 is now resolved** (see §7); **finding 13 is resolved
  adversely** (see §5, §8).
- **Sealed numbers reproduced.** Audit 031 §4 re-ran `emergencia/p1a_count_volume_canal_sigma_m_d2.py`
  and reproduced the six-stratum table of `P1a_count_volume_canal_sigma_m_d2.md:109-114` bit for
  bit. The mathematician and the falsifier independently re-derived the Advertencia 13.16 columns
  (`19.724621/7014 = 2.812e-3`; `29.117250/7014 = 4.151e-3`; `T_emp=0.6774`; `rho_max=0.5680`).
- **Two remediation residues confirmed by the chair after the falsifier flagged them**
  (`grep`, this session): `:1486` states `| discrepancia global uniforme | PROVED |` while the flag
  block at `:1499` states `GLOBAL_DISCREPANCY_LEMMA = PROVED_MODULO_UNARCHIVED_HOEFFDING`; and
  `:1490` bundles a deductive result and a three-point empirical observation under one `PROVED`
  cell, still quoting the superseded rounding `0.68-0.72`. The falsifier's related claim that
  `:903` contains a contradictory *flag assertion* is **not** upheld — `:903` is explanatory prose
  inside the supersession note — but that prose does contain a now-stale value
  (`SUBEXPONENTIAL_LOWER_BOUND_ON_PR_S = PROVED`, superseded by `PROVED_EVEN_N_SKETCH_ODD_N`).
- **Committee composition deviation, recorded.** The configured falsifier model (Fable 5) was
  unavailable mid-session ("monthly spend limit"); the falsifier role was re-dispatched on Opus.
  The committee's own independence design was therefore **not executed as specified**. The
  substitute falsifier was told of the substitution and recorded it in its own brief.

## 3. Dossier

Files and references supplied to the committee:

- `emergencia/P1a_puerta_teorica_en_Minkowski.md` — §13 (line ~916 to EOF) and §12 (~550-915, the
  superseded empty-frame route whose §12.2/§12.3 geometry §13 reuses).
- `emergencia/P1a_count_volume_experimento_condicionado_d2.md:47-79` (domain `Q_3`, event `S`),
  `:162` (closed-interval convention).
- `emergencia/P1a_contrato_comparacion_selectores_balanceados_d2.md:34-58` (three frozen selectors,
  no tie-break).
- `emergencia/P1a_resultados_comparacion_selectores_balanceados_d2.md:73-77` (measured `p_unique`),
  `:128-145` (the `MIN_ONLY` → `MIN_COVERAGE_LEX` bridge).
- `emergencia/P1a_count_volume_lema_kl_d2.md:321-600` (`P_1`/`P_2`, eq. 7.10, 7.15).
- `emergencia/P1a_count_volume_canal_sigma_m_d2.md:60-114` (Lema 3; sealed six-stratum table).
- `emergencia/p1a_enumeracion_simulacion.py:173-199`; `emergencia/p1a_comparar_selectores_d2.py:243-310`.
- `emergencia/P1a_contrato_enumeracion_y_monte_carlo_d2.md` (the frozen local enumeration contract).
- `docs/bibliography_claims.md` §1.1, §1.3, §2.5bis; `docs/manuscript_limits_draft.md` §3.1, §6.1.
- `docs/auditor/auditor_report_031_p1a-seccion-13-certificado-familia-prescrita.md`.
- `docs/preregistration.md`, `_002`, `_003`, `_001_addendum`; `Makefile`; `CLAUDE.md`.
- `biblioteca/emergencia/2507.01907v1_Braun_*.pdf`; `biblioteca/emergencia/2607.05840v1_Madsen_*.pdf`;
  `biblioteca/2503.01719v2.pdf` (Müller); `biblioteca/derived-md/Towards black-hole horizons and
  geodesic focusing in causal sets.md`; `biblioteca/derived-md/The causal set approach to quantum
  gravity.md`; `biblioteca/emergencia/readme_emergencia.md`.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

**Proposed artefact(s)**

- `emergencia/p1a_verificacion_familia_prescrita_d2.py` — a single deterministic, argument-free-by-default script following the `emergencia/p1a_*_d2.py` naming already in use. Its shape should copy `emergencia/p1a_count_volume_canal_sigma_m_d2.py:4-5`, whose own docstring is the precedent for a *non-writing* verifier: "No genera aleatoriedad, no remuestrea, no escribe en `resultados/`". Print to stdout only; emit no CSV/JSON into `emergencia/resultados/`.
- Companion note `emergencia/P1a_verificacion_familia_prescrita_d2.md` (contract-before-run, in the style of `emergencia/P1a_contrato_enumeracion_y_monte_carlo_d2.md:31-56`) fixing the (n, ρ) grid, the predicates, and the PASS/FAIL semantics **before** the numbers are read.
- No file under `nachocausal/`, `tests/`, `certifier/`, `results/` or `docs/preregistration*` is touched.

**Spec of the smallest genuine check** (described, not written):

1. `build_F_B(n, rho) -> (prescribed: dict row->col, free_rows, free_cols, planted)` implementing Def. 13.1 verbatim (`emergencia/P1a_puerta_teorica_en_Minkowski.md:982-1006`), with ρ a **free parameter**, not `floor(mu_n(n-1))` — see the risk section.
2. For each (n, ρ) in the grid, enumerate all `N!` bijections free_rows → free_cols (`itertools.permutations`, deterministic order, no RNG at all — the run has no seed).
3. Per bijection, call the already-committed `emergencia/p1a_enumeracion_simulacion.py:173-199` `interval_count_matrix` (closed-interval convention, which is exactly the convention §13.2 declares load-bearing at `:1180`) and `emergencia/p1a_comparar_selectores_d2.py:255` `evaluate_selectors(...)['MIN_ONLY']`.
4. Assert, exhaustively: (a) `K == L` for every bijection (Lemma 13.5, `:1073`); (b) free-row/free-col counts per half `== N/2` and prescribed counts per half `== rho+1` (Lemma 13.7, `:1125-1140`); (c) the deterministic core of Lemma 13.8 (`:1167`) — for **every** rival with `b=b_0, c=c_0`, `min(K,L)(q) < min(K,L)(q_0)` strictly; (d) Lemma 13.9's `P_-(q), P_+(q) <= rho-1` (`:1204`); (e) classify every rival into exactly one of the three cases of Lemma 13.11 (`:1306-1315`) and assert the partition is total and disjoint; (f) record whether MIN_ONLY is UNIQUE and equals the planted quadruple, and dump every counterexample with its trichotomy case.

**Feasibility already established (this session, read-only, no files written).** I ran the probe. Anchors: `make verify-seal` → `6e2c...bfefd4`, HEAD `649505d`, numpy `1.26.4`, python `3.12.3`.

```
n=12 rho=3 N=4 perms=24     MIN_ONLY_unique=24     planted=24     K==L always: True
n=12 rho=2 N=6 perms=720    MIN_ONLY_unique=720    planted=720    K==L always: True
n=14 rho=3 N=6 perms=720    MIN_ONLY_unique=720    planted=720    K==L always: True
n=14 rho=2 N=8 perms=40320  MIN_ONLY_unique=40273  planted=40273  K==L always: True
n=16 rho=4 N=6 perms=720    MIN_ONLY_unique=720    planted=720    K==L always: True
Lemma 13.8 core (b=b0,c=c0 rivals), n=14 rho=2, all 40320 bijections: 0 violations
```

So the check is *cheap* (seconds to minutes; `N! <= 10!` is the practical ceiling), it is *non-vacuous*, and it already produced a **47/40320 residue at n=14, ρ=2 where MIN_ONLY is TIE, i.e. `F_B ⊄ S` at that n** (all with `primary_score = 3 = K0`, the admissibility floor at `p1a_enumeracion_simulacion.py:32`). That residue is not a refutation — see below — but it is exactly the kind of object §13's prose never exhibits.

**What such a check CAN establish**
- Lemma 13.5 (`K=L`) and Lemma 13.7's free-row/column arithmetic are *finite, n-free identities of the construction*; verifying them exhaustively at several even n is strong evidence, and a single failure would be a hard refutation.
- Lemmas 13.8 and 13.9 are labelled "**determinista sobre `F_B`**" (`:1167`, `:1199`), invoking no `G_n` and no asymptotics. Their deterministic cores must therefore hold at **every** n where `F_B` is well defined. A counterexample at n=12 would falsify a `PROVED` label outright, with no asymptotic escape hatch.
- Lemma 13.11's trichotomy is a *combinatorial partition* of rivals. Totality and disjointness are exactly checkable at finite n.

**What it CANNOT establish**
- Nothing about `Pr(S) >= e^{-o(n)}`. That is asymptotic; no finite n bears on it. NO_RECONSTRUCTION_CLAIM stands untouched either way.
- Prop. 13.12's cases 2 and 3 (`:1341-1353`) are *quantitative asymptotic* separations (`rho - 1 > 2 eta_n`, `N/8 - o(N) >> rho + 2 eta_n`). At the reachable n these are **false by construction**: with `Lambda_n = L log n`, `L > 8`, at n=14, N=8 one gets `eta_n = sqrt(N Λ_n) ≈ 13 > N`, so `G_n` is the whole space and the check is silently testing the *strictly stronger* claim `F_B ⊆ S`. The 47 ties are consistent with this and must be reported as such, not as a refutation.
- The odd case (Def. 13.2, `SKETCH` at `:1035`) is out of scope; the charge is even n.

**Environment & seal**
- Sealed env: pure numpy pinned `numpy==1.26.4` (`nachocausal/thresholds.py:18`, `PINNED_NUMPY`; enforced by `assert_environment()` at `:22-33`). The proposed script imports **only** `emergencia.*`, which does not call `assert_environment()` — but the run should still be executed under the pinned numpy so results are comparable with the committed `emergencia/resultados/` corpus.
- Seal SHA to re-verify **before and after**: `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching `docs/preregistration_003.md:9`. Confirmed unchanged this session.
- Package-diff-clean: `git status --porcelain` empty at `649505d`; re-run after the check and require `nachocausal/`, `tests/`, `certifier/`, `results/`, `docs/preregistration*` all absent from the diff. `make test` and `make dry-run` (`Makefile:9,12`) are **not** invoked; the check has no code path into them. RESPECT_SEAL_FREEZE and NO_THRESHOLD_LOOSENING are structurally untouchable here because the only sealed constant read is `K0 = 3` (`p1a_enumeracion_simulacion.py:32`), read-only.

**Provenance capture** (a run must record, to stdout, in the manner of `p1a_enumeracion_simulacion.py:538-545`)
- `git rev-parse HEAD` (`649505d…`) and `git status --porcelain` (must be empty);
- `thresholds.py` sha256 before and after;
- `platform.python_version()`, `numpy.__version__`, `platform.platform()`;
- **seed band: none.** This run is seedless by design — full enumeration, no RNG. That is a feature: it removes NO_GROUND_TRUTH_LEAKAGE and dev/validation-seed questions entirely. The script should assert no `numpy.random` / `random` import.
- the exact (n, ρ) grid and per-cell `N!` counts, and a sha256 of the printed report body so the stdout can be quoted verbatim in a follow-up audit.

**Run mechanics**
- Single foreground invocation, `python -m emergencia.p1a_verificacion_familia_prescrita_d2`, no flags, no `--out`. Runtime at the proposed grid is minutes; no background job, no `nohup`, nothing to babysit.
- Clean abort for a guard: the script writes nothing, so `Ctrl-C` or a non-zero exit leaves the tree byte-identical. The abort test is `git status --porcelain` still empty. Exit code non-zero on any assertion failure — no `|| true` (the `Makefile:41-43` comment makes swallowing failures itself an audit finding).
- **Reversible pre-flight**: everything above. **Committing step**: only the later act of adding the script + its report to the repo and re-labelling any `PROVED` flag in `§13.7` (`:1470-1485`). Those are separate and must not ride along in the same action. NO_POST_HOC_TUNING: the (n, ρ) grid and the PASS/FAIL predicates must be frozen in the companion `.md` *before* the run, because the temptation to drop n=14, ρ=2 after seeing its 47 ties is exactly the failure mode.
- The frozen enumeration contract `P1a_contrato_enumeracion_y_monte_carlo_d2.md:47-49` fixes `EXACT_N = (6,7,8,9)` over **all `n!` permutations**. This proposed run enumerates `N!` bijections of a *conditioned* family at n=12–16 — a different object. It therefore does **not** reuse and does **not** amend that contract; it needs its own, and the note must say so explicitly to avoid a future auditor reading it as contract drift.

**Reproducibility risks / ambiguities**

- **Def. 13.1 has an unstated well-definedness side condition.** Injectivity of the prescription requires `q_1 + rho - 1 <= s - 1` (else `Q^-` collides with `pi(s)=s`) and likewise `q_3 + rho - 1 <= n - 1`. Verified by direct construction: at n=12, ρ=4 the prescription collides (`Q^- = {4,5,6}` vs `pi(6)=6`). The text at `:982-1006` never states this; it is harmless asymptotically since `rho/n -> 0` (Lemma 13.3, `:1053`), but any verifier must either enforce it or silently produce a non-permutation. This is a genuine gap in a `PROVED` definition, anchored.
- **ρ cannot be taken from the formula at reachable n.** `mu_n = C(Λ_n/n)^{1/3}` with `Λ_n = L log n`, `L > 8` (`:963-970`) gives `mu_n > 1/2` for every n a computer can enumerate, so `rho = floor(mu_n(n-1))` exceeds `s` and `F_B` is empty. The check must treat ρ as free and *declare* that it is testing the construction's combinatorial skeleton, not the asymptotic parameterisation. [Anchored by the collision computation above; the mismatch itself is `[UNVERIFIED]` as a *claim about §13's intent* — the text never says whether small-n ρ is meant to be free.]
- **`G_n` is vacuous at reachable n** (`eta_n = sqrt(N Λ_n) > N` for N ≤ 10), so item (c) of the charge — "unique MIN_ONLY maximiser on `F_B ∩ G_n`" — degenerates to "on `F_B`". Failures there are uninformative about Prop. 13.12; only *successes* and the deterministic lemmas carry weight. This asymmetry must be stated in the contract before the run, or the 47-tie residue will be misread in both directions.
- **Machinery reuse is real and clean.** `interval_count_matrix` (`p1a_enumeracion_simulacion.py:173-199`) and `evaluate_selectors` (`p1a_comparar_selectores_d2.py:255-310`) are both committed, deterministic, and import-safe; I invoked both this session with no side effects. Importing `p1a_comparar_selectores_d2` transitively imports `p1a_estabilidad_d2` (`:28-29`) — confirmed side-effect-free on import, but the verifier should import `p1a_enumeracion_simulacion` directly where possible to shrink the dependency surface.
- **Independence caveat**: §13 and audit 031 share an author (chair, this session). The proposed check is the first artefact in this chain whose output does not pass through that author's prose — provided the contract is frozen first. If the same session both writes the contract and reads the output, the independence gain is partial, not full. [UNVERIFIED as to whether a separate session is procedurally available.]
- **`make verify-comite` / `verify-audit` gates** (`Makefile:46-64`) validate briefs/reports, not `emergencia/` notes; the companion `.md` will not be gate-checked by anything. That is a known blind spot in the tooling, not a defect of this proposal.

### Mathematician brief

**Computability**

- The whole of §13 is decidable on the order relation alone. `Q_3(C)`, `S_lex` and the abstaining gate are defined purely from `prec_C` and closed-interval cardinalities (`emergencia/P1a_count_volume_experimento_condicionado_d2.md:47-62`); the gate abstains (`UNDEFINED`) on `Q_3=∅` or on any tie, so `S` is an order-only event over the full realisation, not over a candidate pair (`:63-65`). The domain gate `m_-,m_+ >= 3` is likewise order-only.
- `C` is a **total** order only after projection; as a poset it is the 2-dimensional permutation poset (`x prec y` iff both ranks increase), which is why "row/column" language is legitimate. Every object §13 manipulates (`K`, `L`, blocks, prescribed points, `u,v`) is a function of `pi`, hence of the isomorphism class of `C`. Nothing embedding-dependent enters — this is `order-only` in the sanctioned sense of `CLAUDE.md:12-18` ("blind-to-embedding, NOT count-free").
- The closed convention is load-bearing and is real: `emergencia/p1a_enumeracion_simulacion.py:172-199` (*"closed-interval cardinalities … inclusive axis-aligned rectangle"*), matching `P1a_count_volume_experimento_condicionado_d2.md:162`. I confirm the text's claim at `:1157-1161`: under a half-open convention, replacing `a_0` would not delete `a_0` from the count and Lemma 13.8 would degrade from `<` to `<=`.

**Order observable**

- The carrier is `m = n_C(a,b) = |[a,b]_C|`, an Alexandrov-interval cardinality. §13 works with the split `count(block) = P(block) + free(block)`, `E[free|F_B] = N·u·v` exactly (hypergeometric, Lemma 13.6, `:1090-1105`). This carries the signal because the *continuum* score of §12.2 is `F = min(x_1y_1, x_2y_2) = s_xs_y/4 + pq - |T|/2` (Lemma 12.5, `:610-628`), maximised at `x=y=1/2` with `F=1/4`; Lemma 13.7 is the assertion that the planted quadruple realises that maximiser **exactly** in free coordinates.

**Verdict on Lemma 13.7 (even n): SURVIVES the attack.** I could not break it. Exhaustive check of the exact counts over every `(n,rho)` with `n` even in `[20,4000]` and `2 <= rho <= n/4`: **998 984 pairs tested, 0 failures** — free rows and free columns per half equal `N/2 = s-rho-1` exactly, hence `u_-=u_+=v_-=v_+=1/2` and `E[K]=E[L]=N/4+rho+1`. Lemma 13.5 (`K=L`) also survives: 0 failures in 8000 random even-`n` permutations, and it is an identity for *every* permutation, as the text says. One **unstated side condition**: the construction is only well defined for `rho <= floor(n/4)`; the first column collision (`Q^+` hitting column `n`) occurs at exactly `rho = floor(n/4)+1` (checked at `n=100,1000,4000`). Asymptotically harmless, but Def. 13.1 (`:963-1005`) does not state it.

**Verdict on Lemma 13.11 (trichotomy): exhaustive, but the labels around it are wrong.** Under the reading `B_n = {s-rho+1,…,s+rho}` the case split by `row(b)` is exhaustive and each conclusion follows. Two defects: (a) "**una y solo una**" is false — the cases overlap (a `b` below the band can also satisfy `min(u_-v_-,u_+v_+) <= 1/8`); only exhaustiveness is used, so this is cosmetic. (b) The `B_n` used here is *not* the `B_n` defined at `:977`. See caveats.

**Relevant invariants**

- Ordering fraction `r = 2R/n(n-1)`, dimension-only for faithful embeddings — Myrheim 1978, restated in Surya LRR 2019 eq. (14), `biblioteca/derived-md/The causal set approach to quantum gravity.md:1006-1011` (PDF p. 26).
- Myrheim–Meyer estimator `R/n^2 = f_0(d) = Γ(d+1)Γ(d/2)/4Γ(3d/2)`, eq. (18), same file `:1040-1052`; "in the large `n` limit this is half of Myrheim's ordering fraction".
- Interval abundances `N_d` (Glaser–Surya), same file `:1908,1938` — §13's `m` is a *single selected* member of that family, not an ensemble average, which is exactly the selection-induced-dependence hazard flagged at `CLAUDE.md:29`.
- Longest chain / height and `C_k` do not appear in §13; the certificate is purely a two-block interval-count statement.

**Analytic / continuum target**

- The correct continuum benchmark is the Alexandrov-volume law `m-2 | A ~ Binomial(n-2, A)`, `A = ell(a,b)^2` (`P1a_count_volume_experimento_condicionado_d2.md:158-165`), i.e. Bombelli et al. 1987's "number ≈ volume" (`docs/bibliography_claims.md:175`; Surya derived-md `:409-410`). §13 does not target this directly; its target is the §12.2 product landscape whose maximum is `1/4`, and Lemma 13.7 hits it exactly. That is the right target and it is met.
- Dimensional context: HKMM requires `d>2` and "the conformal-isometry conclusion is explicitly not claimed for d=2" (`docs/bibliography_claims.md:60-61`); Braun assumes `d>=3` verbatim (`:126-131`); Madsen's rate holds the covariance term subdominant only "for `d>2`" (`:292-294`).

**Caveats**

- **[CONFIRMED BREAK] Lemma 13.4 (`PROVED`) is false for roughly half of all `(C,n)`.** Def. 13.1 sets `B_n = {i : |x_i-1/2| <= mu_n}` (`:977`) but then prescribes only `{s-rho+1,…,s+rho}`. These differ whenever `frac(mu_n(n-1)) >= 1/2`: **295 mismatches out of 600** `(C,n)` pairs scanned (`C∈{0.8,1.0,1.2}`, `L=8.1`, `n` up to 2·10^5). Concrete: `C=1, n=6000` gives `rho=1363`, inequality-band `{1637,…,4364}` vs prescribed `{1638,…,4363}`. Rows `s-rho` and `s+rho+1` satisfy the inequality but are **free**, so the proof step at `:1060` ("tiene índice de fila en `B_n`, luego es una fila prescrita") fails, and the central square is non-empty with probability ≈ **0.917** conditional on `F_B` at that `n` (2 free rows × 1500 free central columns / `N=3272`). Asymptotically the failure probability is `Θ(mu_n)=Θ((log n/n)^{1/3})` — vanishing, but 13.4 asserts a *deterministic* identity "sin ningún evento probabilístico". Fix: define the band by index set and shrink the square to half-side `(rho-1/2)/(n-1)`. Blast radius is contained: 13.4 feeds only Lemma 13.8(iii), and Prop. 13.12 routes through the trichotomy, using only 13.8(i),(ii),(iv), which need no `delta <= mu_n`. So the top-line certificate survives, but `PRESCRIBED_BAND_GEOMETRY = PROVED` and the `PROVED` on 13.4/13.8 are unearned.
- **[CONFIRMED BREAK, load-bearing] Prop. 13.12 case 2 (`:1341-1345`) is a non-sequitur, wrong by Θ(ρ) — the size of the entire margin.** "El bloque que pierde una escalera tiene `P<=2`, luego `min(K,L)(q) <= N/4 + 2 + eta_n`". The bound `N·u·v <= N/4` comes from `min(u_-v_-,u_+v_+) <= 1/4`, which applies to the **minimising** block; `P<=2` applies to the **staircase-losing** block. They need not be the same block. Explicit `F_B`-compatible counterexample (`n=4000, rho=320, N=3358`): `a=a_0`, `b=(1680, 3999)` — row `s-rho` free, column `n-1` free. The past block loses the entire lower staircase (`P_-=1`) yet `u_-=0.5000, v_-=1.0000`, so its mean is `N·u_-v_- + P_- = 1680.00` against the claimed `N/4+2 = 841.50`: **violated by 838.5 = Θ(N)**. Restricting to rivals where the losing block *is* the min, the violation is still `Θ(rho)`.
- **[CONFIRMED] The conclusion of Prop. 13.12 survives, but with half the claimed margin.** Exhaustive search over *all realisable* rivals (`a=a_0`, `d=d_0`, which maximises both blocks; `b,c` over every point realisable under `F_B`; 2-D suffix-max, `O(n^2)`), `n=4000`: planted is the strict maximiser of the exact mean landscape with gap `5.50, 10.51, 20.51, 40.52, 80.54, 160.60` for `rho = 10,20,40,80,160,320` — i.e. **gap/ρ → 0.500**, not `rho-1`. The argmax rival is precisely the case-2 configuration that breaks the text's inequality (`b` just below the band, column past the centre). A correct proof must combine (i) `f_-f_+ <= 1/16`, (ii) the budget `P_- + P_+ <= 2rho+2` (blocks are point-disjoint, and the planted saturates it), and (iii) the geometric fact that a block containing both staircases has `v >= 1/2-o(1)`, forcing the other block to `v <= 1/4+o(1)`. **None of these three steps is in the text.**
- **[CONFIRMED] Consequence for `OPEN` 4 and for scope.** `:1544` says "`C` sólo está restringida por `rho-1 > 2 eta_n`". The measured margin `rho/2` makes the true constraint `rho > 4 eta_n`. Combined with the well-definedness ceiling `rho <= n/4`, the smallest `n` at which the certificate's own inequality is non-vacuous moves from `≈4.4e3` to `≈2.1e4` (C-free), and under the actual parametrisation `rho = C n^{2/3}Λ^{1/3}` with `C=1, L=8.1`, from `n≈4.6e3` to **`n≈2.6e5`**. The sealed experiment runs at `n∈{64,96,128}`. Legitimate for an asymptotic claim, but the certificate is astronomically far from the measured regime and no text should suggest otherwise.
- **[CONFIRMED, minor] Lemma 13.9's stated inequality (`:1204`) and Prop. 13.12's opening bound (`:1334`) are false as written.** The rival `q=(a_0, c_0, c, d_0)` with `row(c) > s+rho` (e.g. `c=(s+rho+1, s+2)`, `delta ≈ mu_n < 1/4`) has past block `[a_0,c_0]` containing `a_0, b_0, c_0` and the whole lower staircase: `P_- = rho+2 > rho+1`. Lemma 13.9 is rescued only under the reading "band point = staircase point only", which contradicts Lemma 13.11's four-type classification that counts `b_0,c_0` as band points. Harmless to the chain (the case analysis does not use `:1334`), but it is a false statement inside a `PROVED` proof.
- **[CONFIRMED, minor] Cor. 13.14 exponent inconsistency.** It states `Pr(G_n|F_B) = 1 - O(N^{4-L})` while Lemma 13.10 proves `1 - 4n^{4-2L}`. Weaker direction, harmless, but inconsistent inside `PROVED`.
- **Secondary (1) — dropping dyadic peeling: SOUND.** The regime where a single global bound would be too weak (`delta` small, drift `N delta^2 < eta_n`) is handled *deterministically* by `K=L` plus the closed convention (13.8 (i),(ii),(iv)), not by discrepancy. Every stochastic case carries a gap of `Θ(rho)` or `Θ(N)`, both `>> eta_n = O(sqrt(n log n))`; I confirm `rho/eta_n = Θ(n^{1/6}(log n)^{-1/6})` as claimed at `:1349`. No multiscale profile is needed.
- **Secondary (2) — union over index rectangles: SOUND, and it genuinely neutralises selection-induced dependence.** The family `{I×J}` is deterministic given `F_B` (free rows in an index interval form an interval in the induced order), has `<= N^4` members, and the free part of every realised block is a member. `G_n` is therefore an event about `pi` alone; applying it to random blocks is legitimate, and the fact that `a,b` are themselves points of `pi` introduces no bias because the bound is a uniform sup. This is the right fix for the `CLAUDE.md:29` hazard. Residual: step (b) is `[UNVERIFIED]` by the text's own admission (Hoeffding 1963 §6 not in `biblioteca/`); the inequality used, `Pr(|X-EX|>=t) <= 2exp(-2t^2/N)` for hypergeometric `X`, is standard, and the offered substitute (Joag-Dev–Proschan 1983) is also unarchived. The flag `GLOBAL_DISCREPANCY_LEMMA = PROVED_MODULO_UNARCHIVED_HOEFFDING` is honest and should stay.
- **Secondary (3) — entropic cost vs Advertencia 13.16: NOT justified.** I reproduced 13.16's table against the sealed source (`P1a_count_volume_canal_sigma_m_d2.md:109-114`): `SSW 19.724621 → 19.72`, `SST/N = 29.117250/7014 = 4.151e-3 → 4.15e-3`, `T_emp 0.6774`, `rho_max 0.5680` — faithful. The warning is correct and decisive: `T_n = 1-rho_max^2` is stuck in `[0.6773, 0.7175]`. `Pr(S) >= e^{-o(n)}` is a divisor for *upper* bounds; the open question (`liminf T_n > 0`) needs a *lower* bound on conditional variance, requiring mass and separation, which §13 supplies not at all. Obs. 13.15 further shows only `e^{-c(eps)n}` unconditional bounds survive the division. So the certificate's only known consumer does not exist and would be vacuous if it did — the text says this itself at `:1414-1420` and `:1466-1469`. The entropic investment is not repaid.
- **Secondary (4) — further 1+1D investment: hard to justify on this route.** Three independent results exclude `d=2` (`docs/bibliography_claims.md:60-61, :126-131, :292-294`). §13 is not a reconstruction claim, so `NO_RECONSTRUCTION_CLAIM` is not at risk; but `OPEN` 5 (`:1553`) is correct that the machinery — rows, columns, rank prescription, block flow conservation — **is** the `d=2` permutation structure and has no stated transfer. Marginal value of more §13-style work is low; `OPEN` 1 is orthogonal to it.
- **Recommendation.** `PRESCRIBED_BAND_UNIQUENESS_CERTIFICATE` and `SUBEXPONENTIAL_LOWER_BOUND_ON_PR_S` should be downgraded from `PROVED_EVEN_N_SKETCH_ODD_N` to `SKETCH_EVEN_N` until Prop. 13.12 case 2 is rewritten with the product/budget/geometry argument, and `PRESCRIBED_BAND_GEOMETRY` from `PROVED` until the `B_n` definitional hole is closed. `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` should remain `NO`: this brief is one adversarial read, not an audit, and it found two unearned `PROVED` labels in the two lemmas the chair nominated as load-bearing — while confirming that Lemma 13.7's arithmetic itself is exactly right.

### Mathematical logic brief

**Formal status**

- **Genuinely proved (I re-derived each independently):**
  - *Lemma 13.3* (`:1033`). `Pr(F_B)=1/(n)_{r_n}` is exact ((n−r)!/n!), and `log Pr(F_B) = −(1+o(1)) r_n log n = −Θ(n^{2/3}(log n)^{4/3})` with `r_n≈2μ_n n = 2C n^{2/3}Λ^{1/3}`. Arithmetic checks; `= e^{−o(n)}` ✓.
  - *Lemma 13.5* (`:1073`). `K=|[a₀,b₀]| = #(L→L)`, `L=|[c₀,d₀]| = #(H→H)`, and `#(L→L)=#(H→H)` holds for **every** permutation with `|L|=|H|=s`. This is a theorem, not an asymptotic, and it is correct. It is also *the* load-bearing fact: without exact `K=L`, Lemma 13.8's strict inequality collapses to `≤` and `S` fails by tie (`:1190-1195`, correctly self-diagnosed).
  - *Lemma 13.6* (`:1090`). `E[#{i∈A:π(i)∈D}|F_B]=|A||D|/N` exact; `u_-+u_+≤1`, `v_-+v_+≤1` from disjointness of row/column ranges ✓.
  - *Lemma 13.7, even n* (`:1125`). I recomputed the prescription of Def. 13.1 line by line: prescribed rows in `{1..s}` = `{1}∪B_n^-` = `ρ+1`; in `{s+1..n}` = `{n}∪B_n^+` = `ρ+1`; prescribed columns in `{1..s}` = `{1,s}∪Q^-` = `ρ+1`; in `{s+1..n}` = `{s+1,n}∪Q^+` = `ρ+1`. Hence free rows/cols per half `= s−ρ−1 = N/2`, so `u_-=u_+=v_-=v_+=1/2` **exactly**, and `max min(u_-v_-,u_+v_+)=1/4` (AM–GM under the two sum constraints). `E[K|F_B]=E[L|F_B]=(ρ+1)+N/4` ✓; consistency cross-check: `(ρ+1)+(ρ+1)=2ρ+2=r_n`, i.e. every prescribed point lies in exactly one planted block. **The centrepiece of §13 is correct.**
  - *Lemma 13.10* (`:1238`). Structure is sound. `X=|π(I)∩J|` hypergeometric ✓; `2exp(−2t²/N)` is a *valid weakening* of Hoeffding's `2exp(−2t²/|I|)` since `|I|≤N` ✓; `t=√(NΛ_n)` ⇒ `2n^{−2L}` ✓; union over `≤N⁴≤n⁴` deterministic index rectangles ⇒ `4n^{4−2L}` (the extra factor 2 is unexplained but is an over-count, hence harmless).
  - *Advertencia 13.16, mathematical half* (`:1416`). The identity `T_n = 1−ρ_max²` is proved at `P1a_count_volume_canal_sigma_m_d2.md:65-73` (Cauchy–Schwarz + tower + total variance) ✓, and the six sealed rows reproduce (`19.7246/29.1173 = 0.6774` ✓).

- **Labelled `PROVED` but actually SKETCH / incomplete:** Lemma 13.4, Lemma 13.8 (scope), Lemma 13.11 (exclusivity), **Proposition 13.12 Case 2** (the substantive one), and hence Corollary 13.14 inherits.
- **Correctly labelled:** Def. 13.2 `SKETCH`; `GLOBAL_DISCREPANCY_LEMMA = PROVED_MODULO_UNARCHIVED_HOEFFDING`; `P2_STATUS = OPEN`; `NORMALISED_CHANNEL_STATUS = OPEN`; `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO`.
- **Physical interpretation, not theorem:** the empirical half of Adv. 13.16 rests on three `n` values in six strata; tagging the composite statement `PROVED` (`:1490`) is a type error, though it errs *against* over-claiming.

**Quantifier / dependency order**

- The order is: fix `L>8`, fix `C>0` (`:965-970`) → `μ_n, ρ_n, B_n, F_B, q_0` are then **deterministic functions of n** → `π` is drawn → `G_n` is evaluated on the residual bijection. Nothing in the construction looks at the realised `π`. **No NO_POST_HOC_TUNING and no NO_GROUND_TRUTH_LEAKAGE exposure**; `C` is left genuinely free (`OPEN` 4, `:1545`).
- **Lemma 13.10's quantifier order is valid.** The union is over the deterministic class of index rectangles (`≤N⁴`), producing a single event `G_n` on which *all* rectangles obey the bound; the random blocks of a realised quadruple are then instances of a universally quantified statement, not new union terms. This is the standard uniform-class device and it correctly avoids the selection-induced dependence `CLAUDE.md` warns about.
- **`Pr(G_n|F_B)=1−o(1)` without division is genuine, not the §12.7 defect in disguise.** The distinction is a real one about the *type* of the conditioning event: `F_B` is a cylinder set fixing `π` on a deterministic row set to deterministic values, so the residual law is *exactly* uniform on bijections of `N` elements (Lemma 13.3); `E_n^0` of §12 is defined by the *values* of the free rows, which destroys uniformity and forced the illegitimate division (`:861-867`). Lemma 13.10 is stated directly for a uniform bijection of `N` elements, so `Pr(G_n|F_B)` **is** its conclusion under the conditional law. No division occurs anywhere. **This is the strongest and most defensible claim in §13, and I confirm it.**
- **Omitted quantifier:** Cor. 13.14's display (`:1373-1378`) carries no `∃n₀ ∀n≥n₀`, yet Prop. 13.12 Cases 2 and 3 hold only "para todo `n` grande" (`:1350`). The correct statement is `∀C>0 ∀L>8 ∃n₀ ∀ even n≥n₀`.

**Equivalence claims**

- `K=L` (Lemma 13.5) is a genuine **equality**, proved for all `π`, used two-sidedly ✓.
- The bridge `MIN_ONLY unique ⇒ MIN_COVERAGE_LEX unique & same quadruple` (Cor. 13.13, `:1355`) is **one-way**, and §13 only uses that direction ✓. Its justification at `P1a_resultados_comparacion_selectores_balanceados_d2.md:138-141` is a valid deterministic argument, not an empirical regularity — the counts `2138…3429` are corroboration, not the proof. The contract's warning that `MIN_COVERAGE_LEX` is *not* a tie-break after `MIN_ONLY` (`contrato…:57-58`) is respected.
- `S` is used with the sealed semantics (`experimento_condicionado_d2.md:53-65`): uniqueness of the *quadruple*, `UNDEFINED` on ties. Lemma 13.8's insistence on **strict** inequality is therefore necessary and correctly identified as such ✓.
- (7.10) is cited faithfully as an iff (`lema_kl_d2.md:473-477`) ✓. §13.6 correctly declines to claim the `Pr(S) ⇒ P_{2,n}` link exists.

**Type / object discipline**

- Clean throughout: `B_n` is a set of *row indices*, `F_B` an *event* (cylinder set), `G_n` an *event on the residual bijection*, `q_0` a deterministic *quadruple of lattice points*, `u,v` *fractions relative to N* (not areas). The insistence at `:1118-1123` that the band correction "no es un error, es un cambio de coordenadas" is the correct type-level observation.
- One genuine category slip: Prop. 13.12 (`:1333-1336`) argues with `E[min(K,L)(q)|F_B]` (an expectation of a minimum) and then "adds `η_n`" from Lemma 13.10, which concentrates each *block count* pathwise, not the min. The intended argument is pathwise-per-block and is fine; the written one mixes a moment with a uniform deviation bound.

**Caveats**

- **[CONFIRMED — the one real hole] Prop. 13.12 Case 2's bound is false as written.** `:1341-1347` asserts "el bloque que pierde una escalera tiene `P ≤ 2`, luego `min(K,L)(q) ≤ N/4 + 2 + η_n`". This silently uses `u v ≤ 1/4` **for that specific block**, which is not implied by Lemma 13.6 — only `min(u_-v_-,u_+v_+) ≤ 1/4` is. Concrete violation: `a=a_0`, `b` a free point at row `≈ s−ρ−5` and column `≈ 0.99n`: `u_-=1/2`, `v_-≈0.99`, so the past block's count is `≈0.495N ≫ N/4+2+η_n`. The *conclusion* survives here (the future block has `v_+≈0.01`), but only via an argument the text does not make. The repair is **non-uniform across sub-cases**: it needs a joint argument coupling the `(u,v)` geometry to the prescribed-point content `P` of the *other* block. I did not verify every sub-case. **Verdict: Prop. 13.12 is `SKETCH`, not `PROVED`.**
- **[CONFIRMED] Prop. 13.12 mis-cites Lemma 13.9.** `:1334` uses "`P(q) ≤ ρ+1` (Lema 13.9)" unconditionally, but Lemma 13.9 (`:1199-1216`) bounds only *band-staircase* points and only for `δ<1/4`. A rival block can contain `a_0,b_0,c_0` plus both staircases, i.e. `P` up to `2ρ+1`. Case 3 survives with the weaker `r_n` bound; Case 2 does not.
- **[CONFIRMED, computationally] Internal contradiction in the definition of `B_n`.** `:977-980` defines `B_n = {i : |x_i−1/2| ≤ μ_n}` while Def. 13.1 `:1000` asserts `|B_n|=2ρ` exactly. For `n=2s` the geometric band has `2·floor(M+1/2)` rows, `M=μ_n(n−1)`, which is `2ρ+2` whenever `frac(M)≥1/2`. Sampled 100 even `n∈[1000,2·10⁵]` at `C∈{0.5,1,2}`, `L=9`: mismatch in **46–57%** of cases. Consequence: rows `s−ρ` and `s+ρ+1` are then geometrically in the central band but **free**, so Lemma 13.4 (`:1049`, tagged `PROVED: vaciado determinista`) is *not* deterministic. Repairable by defining `B_n` as the prescribed set and shrinking the square; the final bound would still be `(1−o(1))Pr(F_B)`. But as written, two `PROVED · determinista` labels are literally false.
- **[CONFIRMED] Lemma 13.8 is applied outside its stated hypothesis.** Lemma 13.8 (`:1167`) is quantified over rivals with `δ ≤ μ_n`; Prop. 13.12 Case 1 (`:1338`) invokes it for **arbitrary** `δ`. The proof content covers this (steps (i),(ii),(iv) use only that `a_0`/`d_0` are global extrema plus the closed convention), so the fix is to restate 13.8 conditionally on `{b=b_0,c=c_0}`.
- **[CONFIRMED] Lemma 13.11's "una y solo una" is false.** The proof establishes only "at least one"; cases 2 and 3 plainly co-occur. Only exhaustiveness is used, so this is harmless — but it is an over-stated `PROVED`. **Exhaustiveness itself I verify as correct** for even `n`: the case split on `row(b)` covers every admissible rival; no gap found.
- **[CONFIRMED] Exponent inconsistency between Lemma 13.10 and Cor. 13.14** (`1−4n^{4−2L}` vs `1−O(N^{4−L})`). Numerically inert, but a `PROVED` corollary should not restate its own lemma with a different exponent.
- **[CONFIRMED] Table/flag mismatch.** The §13.7 table row reads `discrepancia global uniforme | PROVED` (`:1486`) while the flag block reads `PROVED_MODULO_UNARCHIVED_HOEFFDING` (`:1499`). The flag is the honest one. The `[UNVERIFIED]` marker on Hoeffding (1963) §6 at `:1261-1269` is correctly placed and correctly scoped.
- **[CONFIRMED, favourable] §13.6 and Adv. 13.16 do not over-claim.** `:1385-1414` explicitly denies the `Pr(S) ⇒ P_{2,n}` link, and `:1462-1468` states that a rarity certificate is a tool for *upper* bounds and cannot lower-bound a conditional variance. Obs. 13.15's scale accounting is arithmetically correct. No RESPECT_SEAL_FREEZE or NO_RECONSTRUCTION_CLAIM exposure: `git show --stat 649505d` touches one markdown file only.
- **Bottom line.** The architecture of §13 is sound and its central innovation genuinely evades the §12.7 defect. Lemmas 13.3, 13.5, 13.6, 13.7 (even `n`) and 13.10 I independently confirm. But **Prop. 13.12 is not proved as written**, and Lemma 13.4's determinism fails on a definitional off-by-one. Honest flags today: `SKETCH_EVEN_N`, not `PROVED_EVEN_N_SKETCH_ODD_N`. `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED` may move from `NO` to `PARTIAL` on the strength of this reading, but not to `YES`.

### Physicist brief

- **Coordinates & patch:** §13 lives entirely in flat 1+1D Minkowski, not Schwarzschild (`:1-10`). The frozen coordinates are **null (light-cone) coordinates on the unit causal diamond**: `(U_i,V_i) iid Uniform([0,1]^2) | N=n`, `ds^2 = du dv`, `ell(x,y)=sqrt((U_y-U_x)(V_y-V_x))` (`P1a_count_volume_lema_kl_d2.md:31-38`). §13's `x_i=(i-1)/(n-1)` is the **rank** coordinate — an order-isomorphic reparametrisation of the null coordinates by their own empirical CDFs. That is legitimate (monotone on each null axis, hence causal-order-preserving) and is what makes the "band" a *rank* band, not a metric band. The `Q^-/Q^+` "quartile" blocks are quartiles of rank, corresponding to metric null positions only up to `O(n^{-1/2})` order-statistic fluctuations. Finiteness forfeits: no asymptotic/global structure (so no event horizon, a global-future construct — cf. `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:77`), no absolute scale (`CLAUDE.md`), and no boundary-free interior (§13 actively exploits the diamond's tips: `a_0=(1,1)` global minimum, `d_0=(n,n)` global maximum, `:1170-1186`).
- **Physical meaning of the signal:** `M = |[a,b]_C|` is the **discrete volume** of a causal diamond; `ell` is its **proper time** normalised to the enclosing diamond. In 1+1D `V ∝ τ²`, so the estimator inverts volume to duration as `COUNT_VOLUME = sqrt((m-2)/(n-2))` (`P1a_count_volume_canal_sigma_m_d2.md:60`) — the *Order + Number ≈ Geometry* premise specialised to `d=2`. The physical ceiling is quantitative: Poisson fluctuation `δm ~ √m` gives `δτ/τ ~ (1/2)m^{-1/2}`, i.e. the channel cannot resolve `ell` below the discreteness scale `n^{-1/2}`.
- **Sprinkling domain:** the **unit causal diamond of 1+1D Minkowski**, `n` iid uniform points **conditioned on `N=n`**, not a free-intensity Poisson process (`p1a_enumeracion_simulacion.py:5`; `P1a_count_volume_lema_kl_d2.md:33`). Levels `n ∈ {64,96,128}` in the sealed channel. Fixed-`N` conditioning is not a deviation from the literature — Braun uses the same channel verbatim — but it forfeits absolute scale, exact Poisson independence, and any single-realisation guarantee. §13 adds a **further** conditioning of its own.
- **Claim boundary:** §13 claims only `Pr(S) >= e^{-o(n)}` for even `n` in flat 1+1D Minkowski. It does **not** claim metric reconstruction, horizon localisation, or anything about Schwarzschild, and is not a statement about typical sprinklings. `NO_RECONSTRUCTION_CLAIM` holds. `P1a_count_volume_lema_kl_d2.md:586-588` already fences the whole `σ(M)` line. I found no over-claim in §13; its self-labelling is appropriately conservative.

**Charge (a) — is a planted-configuration lower bound physically meaningful?** *It is a legitimate technical device with essentially no physical content, and it is also enormously slack.*

1. **The planted event is not a sprinkling.** `F_B` prescribes `r_n = Θ(n^{2/3}(log n)^{1/3})` row images, producing `Pr(F_B) = exp[-Θ(n^{2/3}(log n)^{4/3})]`. Physically it demands that a macroscopic sub-population lie on two exact rank-staircases at `v ≈ 1/4` and `v ≈ 3/4`. Conditioning on it produces an ensemble that is **not** a Poisson sprinkling of any Lorentzian region — it is a sprinkling of `N=n-r_n` points plus a hand-placed lattice. Nothing about Minkowski causal structure is being probed on `F_B`.
2. **Planting is a standard and sound probabilistic device**, used correctly in the one respect that matters: the residual law on `F_B` is *exactly* uniform, so there is no illegitimate division. I have no physics objection to the mechanism; my objection is to reading it as saying anything about typical causal sets.
3. **The bound is ~90 orders of magnitude weaker than the measured truth.** `Pr(S)` for `MIN_COVERAGE_LEX` is measured at **0.5922 / 0.6528 / 0.6966** for `n = 64/96/128` and *increasing* (`P1a_resultados_comparacion_selectores_balanceados_d2.md:73-77`). The certificate's bound at `n=128` is `≈10^{-91}` for `C=1`. **Physical verdict: no physical content; correct as mathematics; near-zero decision weight.**

**Charge (b) — is Advertencia 13.16's "true and empty" reframing physically right?** *Yes, and it is the most physically valuable paragraph in §13.* The physics is the discreteness scale: both `ell` and `M` are measured inside a *fixed* unit diamond while the discreteness length `n^{-1/2} → 0`, so everything absolute shrinks together. The total spread of `ell` and the spread remaining after conditioning on `M` are **both sub-discreteness**. A constant estimator already achieves absolute error `→ 0`; therefore `P_{1,n}+P_{2,n} → 0` is a statement about the diamond shrinking, not about `M` informing `ell`. The scale-free quantity is `T_n = 1 - ρ_max²`, sitting at **[0.6773, 0.7175]** with no downward trend. `CLAUDE.md` already states that conditioning on `N=n` removes absolute scale, so any decisive quantity in this channel *must* be a ratio. I confirm Advertencia 13.16 as physically correct, and note it makes §13's own certificate largely moot. §13.7 concedes exactly this (`:1524-1529`).

One honesty flag against the chair's own text: Advertencia 13.16 carries the label `PROVED`. The *identity* `T = 1 - ρ_max²` is proved; the *empirical* claim that numerator and denominator decay at the same rate rests on three `n` values in one sealed sample and is not a proof of `liminf T_n > 0`. The prose draws the distinction correctly; the flag is stronger than the evidence for the part that matters.

**Charge (c) — what weight can a 1+1D result carry, and should a 3+1D gate precede?** The three exclusions are real and structurally identical, **not** three independent facts: HKMM `d>2`, Braun `d≥3` — inherited *from Malament*, i.e. the same fact — and Madsen "for `d > 2`". They rest on **one** structural fact: in `d=2` the conformal group is infinite-dimensional. My assessment splits sharply:

- For the **identifiability/`σ(M)` line** (this decision's subject), the `d=2` exclusion bites hard. A *negative* 1+1D result does **not** transfer upward as a no-go — it could be a `d=2` conformal artefact, and the repo already fences it. A *positive* result is largely pre-empted by Braun. Physical weight of either outcome: informative about *this scalar channel in this patch*, and nothing else.
- For the **horizon-localisation line** (the project's declared target), the `d=2` restriction is *physically motivated rather than a defect*: Eichhorn–Gamito–Stokes state that "the salient features of the causal structure of Schwarzschild spacetime are found in the `(t,r)`-slices as a consequence of spherical symmetry", and they sprinkle the induced 2D metric rather than slicing a 4D sprinkling (`biblioteca/derived-md/Towards black-hole horizons…md:128,130-135`). Causal-structure questions in a spherically symmetric spacetime genuinely live on the `(t,r)` slice; metric-reconstruction theorems do not.

**Recommendation:** the 3+1D gate should precede further investment in the **`P_2` / prescribed-family branch specifically** — §13's machinery *is* the permutation representation, i.e. order-dimension 2, and has no `d≥3` analogue (`:1549-1553`). Spending further on a branch that (i) serves a target Adv. 13.16 showed to be empty, (ii) is 90 orders slack against measured `Pr(S)`, and (iii) provably cannot transfer, is poor allocation. The 3+1D gate should **not** be imposed on the horizon line, which has direct 1+1D external precedent and a spherical-symmetry justification.

**Caveats:**
- The rank-vs-metric distinction is handled correctly in the text, but I found no explicit statement that the `Q^-/Q^+` quartiles are *rank* quartiles whose metric positions fluctuate by `O(n^{-1/2})`. Presentational gap, not a demonstrable error. `[UNVERIFIED]` as a defect.
- My decay-exponent fits on the sealed table are three-point arithmetic with no error bars; do not treat them as measurements. The *ratio* `T_emp ∈ [0.6773, 0.7175]` is the sealed number and needs no fit.
- `GLOBAL_DISCREPANCY_LEMMA = PROVED_MODULO_UNARCHIVED_HOEFFDING` is honest; Hoeffding §6 is not in `biblioteca/` and I did not verify it.
- The odd case is `SKETCH`. The sealed strata are `n = 64, 96, 128` — all even — so this affects no executed result, but the certificate is not a statement about all `n`.
- `NO_GROUND_TRUTH_LEAKAGE` is not violated by the planting — `F_B` is an analytic conditioning device in a proof, never an input to an estimator. I record that it *would* be a leakage violation if any future executed code sampled from `F_B` and scored on it.

## 5. Falsifier attack

> **Composition note (chair).** The configured falsifier model (Fable 5) was unavailable
> mid-session due to a monthly spend limit. This section was produced by a substitute falsifier
> running on Opus, told of the substitution. The committee's independence design was therefore not
> executed as specified.

**Both wave-1 breaks independently RE-DERIVED, not taken on trust. Both are real. The top-line certificate SURVIVES in substance; its *proof* does not. Three further defects wave 1 missed, one of which makes §13 untestable at any n a human will ever run.**

- **Concrete failure modes:**

  **(A) CONFIRMED — Lemma 13.4 `PROVED: vaciado determinista` is false, and it propagates further than wave 1 said.** `:977` defines `B_n={i:|x_i-1/2|<=mu_n}`; `:982-1000` prescribes only `{s-rho+1,…,s+rho}`. With `x_i=(i-1)/(n-1)`, `n=2s`, `M:=mu_n(n-1)`, the geometric band is `[s+1/2-M, s+1/2+M]`, so `B_n={s-rho,…,s+rho+1}` (2ρ+2 rows) exactly when `frac(M)>=1/2`. My own sweep (independent of the mathematician's): **83/179 valid (C,n) pairs mismatch, 46.4%**, e.g. `C=0.5,n=800,rho=168`: band `[232,569]`, prescribed `[233,568]`. Rows `s-rho`, `s+rho+1` are geometrically in-band and **free**. The proof line at `:1053` is therefore false, and `Pr(central square non-empty | F_B) = Θ(rho/N) = Θ(mu_n)` — small, but **not zero**. Wave 1 stopped at Lemma 13.4/13.8. It also breaks **Lemma 13.11's** premise (`:1306`, "todo punto con índice de fila en `B_n` es de uno de cuatro tipos"), which is the sole support of Prop. 13.12's case split. *Damage assessment (mine):* the leaked rows fall into Case 2 anyway, so the trichotomy's **conclusion** holds. Clean repair: prescribe `B_n` itself (2ρ+2 rows, ρ+1 columns per quartile block) — Lemma 13.7's exact `u=v=1/2` survives that change unchanged. **Break real, statement repairable, label unearned as written.**

  **(B) CONFIRMED — Prop. 13.12 Case 2 (`:1344`) is wrong by Θ(rho), and I reproduced it arithmetically.** The step needs `u v <= 1/4` for the *staircase-losing* block; Lemma 13.6 yields only `min(u_-v_-,u_+v_+)<=1/4` — for a block the case analysis does **not** get to choose. Exact reproduction at `n=4000, rho=320, N=3358`: `b=(1680,3999)`, `a=a_0` gives `u_-=0.5, v_-=1.033`, `E[K]=1711.0` against the claimed cap `N/4+2=841.5`. **The claimed inequality is violated by a factor >2.**
  I then ran my own exhaustive maximisation over *realisable* rivals (`a=a_0,d=d_0` optimal since they are the global extremes; `K` monotone ↑ in b, `L` monotone ↓ in c, so a 2-D prefix-max is exact):
  ```
  n= 2000 rho=200 planted=600.50 best_rival=499.87 gap/rho=0.503 gap/(2eta)=0.152
  n= 4000 rho=320 planted=1160.50 best_rival=999.90 gap/rho=0.502 gap/(2eta)=0.160
  n= 8000 rho=520 planted=2260.50 best_rival=1999.93 gap/rho=0.501 gap/(2eta)=0.174
  n=16000 rho=830 planted=4415.50 best_rival=3999.94 gap/rho=0.501 gap/(2eta)=0.186
  ```
  The worst rival at n=4000 is `b=(1679,2321), c=(1680,2322)` — b two rows *below* the band (Case 2), trading `u_-v_-=0.2975 > 1/4` for the lost staircase while the kept block trades area back for `P_+≈rho+1`. **This is exactly the mechanism the text's proof does not model.** So: the planted *is* still the strict maximiser, but the true margin is **rho/2, not rho−1**.
  *Repairable?* Yes, and I supply the missing step wave 1 said was absent: with `f=u_lv_l`, `g=(1-u_l)(1-v_l)`, AM-GM gives `g <= (1-sqrt f)^2`, so `f=1/4+eps ⇒ g <= 1/4-eps+eps²`. Combined with `P_l<=2` and `P_k<=rho+1` this closes Case 2 rigorously. **Break real, conclusion survives, proof as written is a non-sequitur.**

  **(C) NEW — `n_0` is astronomical, unstated, and C-dependent; the certificate is unfalsifiable at every reachable n.** With the *corrected* Case-2 margin the criterion becomes `rho > 4 eta_n`, not `rho-1 > 2 eta_n` (`:1545`). Crossover:
  ```
  corrected (rho>4eta):  C=0.3 → n_0~1.2e9 | C=0.5 → 4.0e7 | C=1.0 → 3.6e5 | C=2.0 → 5.7e4
  text's    (rho-1>2eta): C=0.3 → n_0~1.4e7 | C=0.5 → 4.7e5 | C=1.0 → 5.4e3 | C=2.0 → 5.7e4
  ```
  Correcting break (B) moves `n_0` by up to **two orders of magnitude**. `Corolario 13.14` (`:1368`) carries no `∃n_0` quantifier at all.

  **(D) NEW — Def. 13.1 is not merely missing a "side condition"; it is *ill-defined* over a huge range.** `Q^+ = {q_3+1,…,q_3+rho-1}` requires `rho < n/4`. Sweep of the smallest `n` beyond which Def. 13.1 is well-defined *for all larger n*: **C=0.5 → n≥418; C=1.0 → n≥4878; C=2.0 → n≥49826.** My first natural parameter pick (C=1, L=9, n=4000) produced `rho=1060 > n/4`, `Q^+` running to column 4059 > n=4000, and *colliding* prescribed columns (`|pres_cols| = 2060 ≠ 2122 = r_n`), silently corrupting `N`. A `PROVED` definition that constructs out-of-range indices is not `PROVED`.

  **(E) NEW — Lemma 13.9's displayed inequality (`:1204`) is false, and Prop. 13.12 cites it for a bound it does not state.** Take `q=(a_0, b=c_0, c, d_0)` with `c` just above `c_0`: `delta = O(1/n) < 1/4`, and the past block contains the ρ−1 low-staircase points **plus** `b_0` **plus** `c_0` — `P_-(q)=rho+1 > rho-1`. Worse: Prop. 13.12 (`:1334`) asserts "`P(q) <= rho+1` (Lema 13.9)" — a *different* bound from the lemma's, and for `delta>=1/4` even `rho+1` is false in general (a single block can swallow *both* staircases: `P ≈ 2rho+2`). Case 3 survives only because the block it selects is the small-`uv` one, which provably contains at most one staircase — an argument **nowhere in the text**.

  **(F) Case 3 (`:1350`) — I attacked it and it HOLDS, unlike Case 2.** Structural reason: Case 3 identifies the block by *small `uv`* and then applies `min(K,L) <= count_j` for that block — logically valid. Case 2 identifies the block by *staircase loss* and then needs `uv<=1/4` for that same block — invalid. Two unstated but true sub-lemmas are used: `u_- <= 1/2` when `b` is low-staircase and `u_+ <= 1/2` when `b` is high-staircase. Gap `N/8` swamps `rho + 2eta`. **Not a break.**

  **(G) Cor. 13.13's bridge to `S`: I attacked it and it HOLDS.** Prop. 13.12 gives a unique `S_min` maximiser; every competitor has strictly smaller first component, so the lexicographic second component can neither displace it nor create a tie — Lemma 12.4 (`:595-600`), corroborated at `P1a_resultados_..._d2.md:128-145`. The contract confirms both selectors run on the same frozen `Q_3(C)`. The closed-interval convention is verified literally at `p1a_enumeracion_simulacion.py:173-178`. **No break here.** `F_B ∩ G_n ⊆ S` *is* established modulo (A)+(B)+(D).

  **(H) Cor. 13.14 exponent inconsistency (`:1368`).** Three different exponents in one corollary labelled `PROVED`. Harmless numerically, fatal to the label.

- **Ground-truth leakage:** **None found.** §13 is written entirely in rank/permutation coordinates of the observable poset; `ell` never enters a definition, a boundary, a band, or a prescription. Adv. 13.16 uses `ell` only to *score* against the already-sealed six strata, and I reproduced its arithmetic exactly. One residual hazard, not a violation: `§13.8 OPEN 4` declares `C` constrained *only* by `rho-1 > 2 eta_n`, now known false (finding C); leaving `C` free-floating with an `n_0` that moves 100× under a proof correction is an open surface for later constant-fitting. Freeze `C` and `L` now. — Dossier item `sd(ell) = (0.50 ± 0.02) n^{-1/2}` attributed to the sealed table: **I could not locate it**; `[UNVERIFIED]` — do not carry it into the brief.

- **Freeze violations:** No sealed-path violation. Two live problems: (1) `:1485` sets the discrepancy row to bare `PROVED` while `:1499` sets `PROVED_MODULO_UNARCHIVED_HOEFFDING` — a flag-value contradiction **inside the file audit 031 was supposed to have remediated**, still live and pushed at `649505d`. Same defect class that produced `AUDIT_FAIL`; the remediation is incomplete. (2) The warden is right that a now-*confirmed*-unearned `PROVED` on Prop. 13.12 in a pushed file violates `CLAUDE.md:33-34`. No seed burn; no threshold loosening detected.

- **Verdict coercion:** None inside §13 — abstention semantics preserved verbatim (`:572-577`, `p1a_comparar_selectores_d2.py:280-306`), no tie-break introduced. **One reporting asymmetry to correct in the brief:** the engineer's "47 ties ⇒ `F_B ⊄ S`" at n=14 is being read as evidence against §13. It is not evidence at all. At n=14, `eta_n = 13.8 > N = 8`, so `G_n` is vacuous; and break (A) is present there too. The probe tests a statement §13 never makes (`F_B ⊆ S`) at an `n` ~10⁸ below `n_0`. Reporting it as a §13 failure would be an asymmetry in the *other* direction. Likewise the physicist's "10⁻⁹¹ vs measured 0.6966" is not a contradiction (it is a lower bound) — but it is the honest headline: **the certificate has zero empirical content at every reachable n.**

- **Premature / over-broad claims:** No reconstruction claim, no asymptotic-horizon claim, no 3+1D claim — §13.8 point 5 explicitly disclaims transfer. §13.6 and Adv. 13.16 are, if anything, *under*-claimed and are the section's real content. Two residual over-claims: (i) the §13.7 row at `:1494` imports a 3-size empirical observation into a `PROVED` scope cell — split the row; (ii) `PRESCRIBED_BAND_GEOMETRY = PROVED` is flatly contradicted by findings (A) and (D).

- **Independent-falsification gate:** **NOT satisfied for §13's mathematics prior to this committee, and only partially satisfied now.** §13 and audit 031 share a single author in a single session — `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` is the correct self-report and must stay `NO` for anything that would count as a discharged audit. This wave supplies three independent adversarial readings converging on the *same two* breaks by *three different* constructions, which is genuine corroboration. But: (a) I am a substitute for the configured falsifier, so the committee's independence design was not executed as specified — record it; (b) every check in this session, including mine, is a *numerical* check of *mean-field* landscapes, not a proof audit — no one has verified the repaired Case-2 argument I sketched, and I am its author. Do not let my AM-GM repair enter the manuscript as `PROVED` on my say-so.

- **Minimal falsification test:** Already executed. Enumerate all realisable rivals in the exact mean landscape induced by `F_B` and compare `min(K,L)` against the planted, with `b,c` restricted to `P ∪ (free row × free col)`, `a=a_0`, `d=d_0`, 2-D prefix-max over `b ≺ c`. **Outcome:** at `n ∈ {2000,4000,8000,16000}` the planted is the strict maximiser (Prop. 13.12's *conclusion* holds) but the margin is `0.501–0.503 · rho`, **not** `rho-1`; the claimed Case-2 cap is violated by up to `rho/2`; and `gap/(2·eta_n) = 0.152 → 0.186`, i.e. **below 1 at every n tested**, so the discrepancy budget does not close until `n_0 ~ 5.7e4–1.2e9` depending on `C`. This single test confirms break (B), refutes the text's constant, and exposes finding (C). It should be committed as a deterministic script *before* any flag change, so the constant `1/2` is on the record and cannot later be re-fitted.

**Bottom line for the decision.** The top-line `Pr(S) >= e^{-o(n)}` **survives** — but only because two of its supporting lemmas are false-as-written in ways that happen to be repairable, and the repairs are not in the manuscript. §13 currently claims `PROVED` for a chain containing one ill-defined definition, one false deterministic lemma, one false displayed inequality, one non-sequitur, and internal flag contradictions.

**Flag values I would set:**

```text
PRESCRIBED_BAND_UNIQUENESS_CERTIFICATE = SKETCH_EVEN_N_GAP_IN_PROP_13_12_CASE_2
PRESCRIBED_BAND_GEOMETRY               = SKETCH_BAND_OFF_BY_ONE_AND_UNSTATED_RHO_LT_N_OVER_4
SUBEXPONENTIAL_LOWER_BOUND_ON_PR_S     = SKETCH_EVEN_N
GLOBAL_DISCREPANCY_LEMMA               = PROVED_MODULO_UNARCHIVED_HOEFFDING  (unchanged; fix table row :1485)
ABSOLUTE_RISK_IS_NOT_RECOVERABILITY    = PROVED                             (unchanged; split :1494 row)
PRESCRIBED_FAMILY_N0                   = UNSTATED_C_DEPENDENT_GE_5E4        (new)
PRESCRIBED_FAMILY_EMPIRICALLY_TESTABLE = NO                                 (new)
P2_STATUS = OPEN ; NORMALISED_CHANNEL_STATUS = OPEN                         (unchanged — correct)
MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO_TWO_BREAKS_CONFIRMED_BY_ADVERSARIAL_READ
```
Per-lemma rows: Lemma 13.4 `PROVED → FALSE_AS_WRITTEN`; Lemma 13.9 `PROVED → FALSE_AS_WRITTEN`; Prop. 13.12 `PROVED → SKETCH`; Lemma 13.11 `PROVED → PROVED_MODULO_13.4` (and drop "una y solo una"); Cor. 13.13 `PROVED` may stand *conditionally on* Prop. 13.12; Cor. 13.14 fix the exponent and add `∃n_0`; Def. 13.1 add `rho_n < floor(n/4)`.

## 6. Pre-registration verdict

- **Verdict: PASS** (§13 as committed text) **with a BLOCK on the proposed follow-up as currently specified** (the brute-force verification may not proceed until a contract is frozen in writing).

- **Freeze status:** No threshold governs §13 at all — it is a "BORRADOR ANALÍTICO · SIN EJECUCIÓN" (`:925`) that "no modifica ningún gate congelado" (`:926`). The only frozen artefacts in scope are `docs/preregistration_002.md` (seal `:8`), `docs/preregistration_003.md` (seal `:9`), and the narrow local freeze `emergencia/P1a_contrato_enumeracion_y_monte_carlo_d2.md` (`CONTRATO CONGELADO v1.0`, `:3-9`), which governs only the `F_cov,3` selector at `EXACT_N=(6,7,8,9)` and `MC_N=(6,…,64)` (`:49,77`) — it neither mentions nor authorizes anything about `F_B`, `G_n`, or ρ (`grep -n "F_B\|G_n"` → empty). Thresholds for the proposed step are **not** frozen in writing.

- **Seal integrity:** Confirmed unchanged. `make verify-seal` → `6e2c3888…bfefd4` (independently re-run), matching `docs/preregistration_002.md:8` and `docs/preregistration_003.md:9`. §13 and the proposed check touch neither `nachocausal/thresholds.py` nor any sealed script.

- **Seed discipline:** N/A to §13 itself. For the *proposed* follow-up: the reproducibility engineer already ran an ad hoc probe with **no pre-declared n/ρ grid and no pre-declared pass/fail rule** — and this probe is not committed to the repo (no matching file under `emergencia/*.py`, no `git status` trace). It does not touch `RESERVED_002` (band `2_000_000-2_999_999`, `docs/preregistration_002.md:16-27`) — it is a separate line — but it is also not covered by the frozen enumeration contract.

- **Reporting rule:** For §13 as committed: satisfied at the document level — `PROVED`/`SKETCH`/`OPEN` are used per-item (`:1470-1491`) and `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` is itself reported (`:1493`) rather than suppressed. **For the unearned `PROVED` on Prop. 13.12 specifically: the reporting rule is currently violated in the pushed file** until corrected.

- **Forbidden moves present?** No post-hoc tuning, no threshold loosening, no ground-truth leakage in §13 or audit 031. **Reconstruction over-claim: none** — OPEN item 5 explicitly declines 3+1D transfer; Adv. 13.16 blocks the absolute-risk→recoverability inference. **Post-hoc hazard: present, for the *proposed follow-up only*.** **A knowingly-unearned `PROVED` left live in a pushed file: present and unremediated.**

- **Reasons:**
  - §13's own status banner and flag table already practice the honesty mandate at the document level (`:925-926`, `:1470-1493`).
  - `emergencia/P1a_contrato_enumeracion_y_monte_carlo_d2.md` is a real in-force local freeze, but scoped to a different object (`F_cov,3`) and a different n-grid; it provides **no** cover for a §13 verification run.
  - `docs/auditor/auditor_report_031_…md` finding 1 shows the flag-discipline failure mode is not hypothetical in this file — it has already happened once and was remediated in `649505d`; the falsifier has now found the remediation incomplete.

**(ii) Is the unearned `PROVED` on Prop. 13.12, left in a pushed file, a reporting-rule violation?** Yes. The founding rule is "Every claim carries verifiable backing… or is marked `[UNVERIFIED]`" (`CLAUDE.md:33-34`). Audit 031 itself, in the very commit that is HEAD, already downgraded Def. 13.2 from `PROVED` to `SKETCH` on discovering its count wasn't line-by-line checkable — establishing the repo's own remediation precedent for exactly this situation. Leaving `Proposición 13.12 (PROVED)` (`:1330`) and the `unicidad sobre F_B ∩ G_n | PROVED` row (`:1487`) live, in a pushed branch, after this committee has confirmed the break, is a live false claim in the repository — a `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` disclaimer does not cure a specific, now-confirmed-wrong `PROVED` on a specific proposition.

**(iii) Does the pre-contract probe create a post-hoc hazard?** Yes, structurally — not because the probe was run maliciously, but because any contract written *now* is written by people who already know 47/40320 ties turned up at n=14, ρ=2. That knowledge can silently steer which n's to include, whether n=14 is "too small", what tie rate disqualifies. Before the verification proceeds, in writing and before any further n/ρ value is examined: the **n-grid** on a principled basis; the **ρ construction** with no run-time discretion; the operational meaning of a **"tie"**; the **pass/fail/inconclusive criterion**, stated so precisely that a result contrary to the already-known n=14 finding could occur; **explicit disclosure in the contract text that n=14, ρ=2 was already probed and gave 47 ties**, so the freeze is not silently retroactive; and a "report alike" clause matching `preregistration_002.md:64-68`.

**(iv) Does `emergencia/` fall under the existing pre-registrations?** Partially governed, unevenly. It inherits the founding rules verbatim (`CLAUDE.md:31-35`, repo-wide) and has produced its own local frozen contracts in the same style. But it is **not** covered by the numbered `docs/preregistration*.md` sequence — those are scoped to the sealed v2 estimator and `RESERVED_002`/`RESERVED_003`. So §13 and its follow-up sit in a line with local freeze *discipline* but **no specific pre-registration for the brute-force verification**; it must get one, modelled on the existing `emergencia/*contrato*.md` pattern, before execution. The absence of `docs/preregistration_00X` coverage is not an absence of governance — it is a gap to be closed by a new, emergencia-local, written-before-results contract, not a licence to run first and register later.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| Braun 2507.01907, p.2, "we assume all spacetimes have the same dimension d ∈ N no less than 3" | dossier §1.3 | CONFIRMED — verbatim at PDF p.2 |
| Braun 2507.01907, p.4, "the random support of a PPP conditioned on k elements" | dossier §1.3 | CONFIRMED — verbatim at PDF p.4 |
| Braun 2507.01907, Thm 1.4 (laws agree for every k ∈ N; concludes smooth isometry) | dossier §1.3 | CONFIRMED — exact statement at p.4 |
| Braun 2507.01907, absence of estimator/rate/finite-n risk bound | dossier §1.3 | CONFIRMED — no occurrence of "estimator", "finite-n", "risk bound" or "rate" anywhere in the paper |
| Braun's d≥3 restriction inherited from Malament, not an independent technique gap | dossier §1.3 | CONFIRMED — proof of Thm 1.4 invokes Theorem 2.13 ("Malament's theorem") directly |
| Madsen 2607.05840, Thm 4.18 eq.(39) error and Cor 5.6 eq.(48) probability | dossier §2.5bis | CONFIRMED — matching exactly |
| Madsen 2607.05840, covariance term subdominant "for d > 2" | dossier §2.5bis | CONFIRMED — verbatim in the proof of Thm 4.18 |
| Madsen 2607.05840, F2 tolerance eq. (4) | dossier §2.5bis | CONFIRMED — exact form |
| Madsen 2607.05840, footnote 1 p.4: (F3)'s relation to (F1)–(F2) left OPEN | dossier §2.5bis | CONFIRMED — verbatim |
| Madsen 2607.05840, Remark 5.5(b): boundary layer does not shrink as ρ→∞ | dossier §2.5bis | CONFIRMED — verbatim |
| Madsen 2607.05840, Remark 5.4: no almost-sure statement for infinite-volume M | dossier §2.5bis | CONFIRMED |
| Madsen 2607.05840, §6.2: Müller proved the direct finite-set Hauptvermutung FALSE | dossier §2.5bis | CONFIRMED — near-verbatim |
| Müller 2503.01719 primary source | dossier §2.5bis (cited *through* Madsen) | CONFIRMED (substance), with a nuance — see Notes |
| Hoeffding (1963) §6 absent from `biblioteca/`; step marked `[UNVERIFIED]` | §13.5 | CONFIRMED absent — no file matching "hoeffding" anywhere in `biblioteca/`; no local source supplies an equivalent hypergeometric Chernoff bound. `[UNVERIFIED]` correctly stands and **cannot be discharged locally** |
| Eichhorn–Gamito–Stokes 2605.06813: (t,r)-slices by spherical symmetry; sprinkle induced 2D metric | Physicist | CONFIRMED — derived-md lines 128, 135, verbatim |
| Surya LRR 2019 eq. (14) ordering fraction, eq. (18) Myrheim–Meyer | Mathematician | CONFIRMED — derived-md lines 1006-1009 and 1045-1051 |

- **Notes**: One substantive nuance on the Müller primary-source check, not a defect but worth recording: Müller's actual Theorem 2 (`biblioteca/2503.01719v2.pdf`, p.3–4) does not literally exhibit "a" finite causal set with two simultaneous order-preserving embeddings into named distinct manifolds; it is a *probabilistic* statement — for any distance-bound D it constructs a pair (X, Y) with equal volume, same boundary, `d⁻(X,Y) > D` (hence non-isometric), such that the L¹-distance between the induced distributions over order-isomorphism classes of random K-point samples is `< ε`. The proof shows a specific order type `q` has probability `> ε` of arising from both X and Y, which *does* imply the existence of realizations of `q` order-embeddable in both — so Madsen's gloss is a faithful paraphrase of the substance, not a misstatement, but it elides that the construction is via positive-probability events under a sampling measure rather than a single deterministic exhibited object. Recommend §2.5bis flag this as "paraphrase confirmed; mechanism is probabilistic, not a bare deterministic counterexample". This does not change the `PARTIAL` verdict. **Audit-031 finding 14 is resolved**: all of §1.3 and §2.5bis's citations check out against the local PDFs verbatim or near-verbatim.

## 8. Synthesis

**Unanimous, and it matters: the centrepiece of §13 is correct.** Lemma 13.7 — the claim the chair
nominated as load-bearing — survived three independent attacks by three different methods: an
exhaustive sweep of 998 984 `(n,ρ)` pairs with **0 failures** (mathematician), a line-by-line
re-derivation of Def. 13.1's prescription counts (logician), and the falsifier's own construction.
Lemmas 13.3, 13.5 (`K=L` for *every* permutation), 13.6 and the structure of 13.10 are likewise
independently confirmed. Lemma 13.11's case split is **exhaustive**, which is the property the
argument actually uses.

**Unanimous, and it also matters: §13's central architectural claim is genuine.** The logician's
verdict, unprompted, is that `Pr(G_n|F_B)=1−o(1)` *without division* is "the strongest and most
defensible claim in §13" and that it genuinely evades the §12.7 defect, because `F_B` is a
cylinder set fixing `π` on a deterministic row set (residual law exactly uniform) whereas §12's
`E_n^0` was defined by the *values* of free rows (uniformity destroyed). The mathematician and
logician independently confirm that the union over deterministic index rectangles is the correct
fix for the selection-induced-dependence hazard `CLAUDE.md` names.

**Also unanimous: the proof, as written, is not proved.** Three roles independently produced three
*different* counterexamples to the same step — Prop. 13.12 Case 2 (`:1344`) silently applies
`u·v ≤ 1/4` to the *staircase-losing* block when Lemma 13.6 licenses it only for the *minimising*
block. The mathematician's exhaustive maximisation and the falsifier's independent re-run agree the
true margin is `ρ/2`, not `ρ−1` — the text over-states its own drift by a factor 2 and derives it
from a false inequality. Independently, three sweeps (295/600, 46–57%, 83/179) confirm Lemma 13.4's
"vaciado determinista" is false on roughly half of all `(C,n)` because `B_n` is defined by an
inequality (`:977`) but prescribed as an index set (`:1000`).

**Both breaks are repairable and the top-line conclusion survives.** The planted quadruple remains
the strict maximiser at every `n` tested. But the repairs are **not in the manuscript**, and the
falsifier — who supplied one — explicitly asks that it not be entered as `PROVED` on its say-so.

**Three findings beyond the charge, and the third is the decision-relevant one.**

1. *(falsifier, new)* Def. 13.1 is not merely missing a side condition; it is **ill-defined** for
   `ρ ≥ n/4`. The falsifier's first natural parameter pick (`C=1, L=9, n=4000`) silently produced
   colliding prescribed columns and a corrupted `N`.
2. *(falsifier, new)* With the corrected margin the criterion becomes `ρ > 4η_n`, moving `n_0` by up
   to two orders of magnitude: `n_0 ≈ 5.7e4` (C=2) to `1.2e9` (C=0.3). `Cor. 13.14` carries no
   `∃n_0` quantifier at all. **The certificate is unfalsifiable at every `n` a computer will run.**
3. *(physicist)* Measured `Pr(S)` for `MIN_COVERAGE_LEX` is **0.5922 / 0.6528 / 0.6966** at
   `n=64/96/128` and **increasing** (`P1a_resultados_comparacion_selectores_balanceados_d2.md:73-77`),
   against a certificate bound of `≈10^{-91}` at `n=128`. §13 proves, by heroic combinatorics, a
   lower bound on a quantity already measured to be `Θ(1)` and rising. This is not a contradiction —
   it is a lower bound — but it is the honest headline: **the certificate has zero empirical content
   at every reachable `n`, and its only known consumer (`P_{2,n} → 0`) was shown by Advertencia
   13.16 to be true-and-empty.**

**Open disagreements, not hidden.**

- **Interpretation of the n=14 residue.** The reproducibility engineer surfaces 47/40320 ties at
  `n=14, ρ=2` as "`F_B ⊄ S` at that n". The falsifier rules this **not evidence at all**: `η_n =
  13.8 > N = 8` there, so `G_n` is vacuous, break (A) is present, and the probe tests a statement
  §13 never makes at an `n` ~10⁸ below `n_0`. **The chair adopts the falsifier's reading**, and
  records that reporting the residue as a §13 failure would be a reporting asymmetry in the
  opposite direction.
- **Whether `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED` may move.** Mathematician: keep `NO`.
  Logician: may move to `PARTIAL`. Falsifier: `NO_TWO_BREAKS_CONFIRMED_BY_ADVERSARIAL_READ`.
  **Chair's ruling: it stays `NO`**, annotated with this brief's number. Two reasons: the configured
  falsifier model was unavailable and the role was substituted, so the committee's own independence
  design was not executed as specified; and every check in this session, including the adversarial
  ones, is a *numerical* check of *mean-field* landscapes, not a proof audit.
- **Scope of the 3+1D gate — this corrects an earlier chair statement in the originating session.**
  The physicist draws a distinction the chair did not: the three `d=2` exclusions (HKMM, Braun,
  Madsen) rest on **one** structural fact, not three, and while that fact bites hard on the
  identifiability/`σ(M)` line, the `d=2` restriction is **physically motivated** for the
  horizon-localisation line — Eichhorn–Gamito–Stokes state that Schwarzschild's salient causal
  features live in the `(t,r)`-slices by spherical symmetry, and they sprinkle the induced 2D metric
  rather than slicing a 4D sprinkling (`biblioteca/derived-md/Towards black-hole horizons…md:128,
  130-135`, CONFIRMED in §7). **The 3+1D gate should therefore apply to the prescribed-family /
  `P_2` branch, not to the horizon line.**
- **Warden**: `PASS` on §13 as committed text; `BLOCK` on the proposed brute-force follow-up until a
  contract is frozen. The warden further holds that leaving a now-confirmed-unearned `PROVED` on
  Prop. 13.12 live in a pushed file is a live founding-rule violation (`CLAUDE.md:33-34`).

**Recommended direction.** Downgrade the labels to match what is actually established, write the
missing repairs in as explicit `SKETCH`, record `n_0` and the ill-definedness bound, and **stop
investing in this branch**. Ranked alternatives: (1) downgrade + repair + stop — recommended;
(2) downgrade + repair + attempt a full proof of the repaired Case 2 — defensible only if the
certificate acquires a consumer, which Advertencia 13.16 says it has not; (3) proceed to the
brute-force verification — blocked by the warden until a contract is frozen, and of limited value
since `G_n` is vacuous at every enumerable `n`; (4) leave the flags as they are — rejected, it is a
live false claim in a pushed file.

## 9. Next-step spec

**Reversible (may be done now if the user asks).**

- **R1 — Label correction in `emergencia/P1a_puerta_teorica_en_Minkowski.md` §13.** Apply the
  falsifier's flag table from §5 verbatim: `PRESCRIBED_BAND_UNIQUENESS_CERTIFICATE` and
  `SUBEXPONENTIAL_LOWER_BOUND_ON_PR_S` → `SKETCH_EVEN_N…`; `PRESCRIBED_BAND_GEOMETRY` → `SKETCH…`;
  new `PRESCRIBED_FAMILY_N0` and `PRESCRIBED_FAMILY_EMPIRICALLY_TESTABLE = NO`;
  `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` retained with a pointer to this brief.
  Per-lemma: 13.4 → `FALSE_AS_WRITTEN`; 13.9 → `FALSE_AS_WRITTEN`; 13.12 → `SKETCH`; 13.11 →
  `PROVED_MODULO_13.4` and drop "una y solo una"; 13.13 conditional on 13.12; Def. 13.1 add
  `ρ_n < ⌊n/4⌋`; Cor. 13.14 fix the exponent and add `∃n_0`.
- **R2 — Fix the two remediation residues** the falsifier found and the chair confirmed: the `:1486`
  table row vs the `:1499` flag, and the `:1490` row that bundles a deductive identity with a
  three-point empirical observation under one `PROVED` cell (split it; the identity is proved,
  `liminf T_n > 0` is `OPEN`). Also correct the stale value in the supersession prose at `:903`.
- **R3 — Write the repairs in as explicit `SKETCH`, attributed.** The falsifier's AM-GM step
  (`g ≤ (1−√f)²`) plus the budget `P_-+P_+ ≤ 2ρ+2` and the geometric step; the `B_n` fix (define by
  index set, shrink the square); the restatement of Lemma 13.8 conditional on `{b=b_0,c=c_0}`.
  **Must not be labelled `PROVED`** — the falsifier is the author of the repair and explicitly
  declines to have it entered on its say-so.
- **R4 — Record `n_0` explicitly** in §13.8 with the falsifier's table, and state that the
  certificate is not empirically testable at any enumerable `n`.

**Committing (only on explicit user authorisation).**

- **C1 — Commit and push R1–R4.** One commit, message stating it is a downgrade following comité 050.
- **C2 — The brute-force verification.** **BLOCKED by the warden** until an `emergencia/`-local
  contract is frozen in writing that pre-declares: the n-grid on a principled basis; the ρ
  construction with no run-time discretion; the operational meaning of a tie; the
  pass/fail/inconclusive criterion, stated so a result contrary to the already-known `n=14` finding
  could occur; **explicit disclosure that `n=14, ρ=2` was already probed and gave 47 ties**; and a
  "report alike" clause matching `docs/preregistration_002.md:64-68`. The committee notes this check
  has limited value (`G_n` vacuous at every enumerable `n`) and does not recommend prioritising it.

**Falsifier's minimal falsification test — already executed, result binding.** Enumerate all
realisable rivals in the exact mean landscape induced by `F_B`; `a=a_0`, `d=d_0`; `b,c` over
`P ∪ (free row × free col)`; 2-D prefix-max over `b ≺ c`. Outcome at `n ∈ {2000,4000,8000,16000}`:
planted is the strict maximiser, margin `0.501–0.503·ρ` (**not** `ρ−1`), Case-2 cap violated by up
to `ρ/2`, and `gap/(2η_n) = 0.152 → 0.186` — **below 1 at every n tested**. The falsifier asks that
this be committed as a deterministic script *before* any flag change, so the constant `1/2` is on
the record and cannot later be re-fitted. The committee endorses that sequencing.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

**Decisión del PI, 2026-08-05.** La recomendación de fondo del comité (`no seguir invirtiendo en
esta rama`) se **acepta**; la forma `REVISE_AND_RECONVENE` se **agota aquí**: no se reconvoca.

- **R1–R4: ya aplicadas** en `2aafb77` (bajada a `SKETCH`, residuos de remediación corregidos,
  reparaciones escritas y atribuidas, `n_0` y `PRESCRIBED_FAMILY_EMPIRICALLY_TESTABLE = NO`).
- **C1 (commit/push de R1–R4): autorizado y ejecutado** (`2aafb77`, ya empujado).
- **C2 (verificación por fuerza bruta): NO se ejecuta.** No se congela el contrato que el warden
  exigía; la rama se cierra antes de necesitarlo.
- **Reparación del certificado (Def. 13.1, Lemas 13.4, 13.9, caso 2 de la Prop. 13.12): NO se
  prioriza.** Motivo del PI, más fuerte que el estado de la demostración: aun parcheado, el
  resultado sería estratégicamente vacío en el régimen que importa (`n ≈ 64–128`). Una cota de
  `Pr(S)` que solo empieza a funcionar en `n_0 ~ 1e5–1e9` no aporta nada utilizable.
- **Lo que sí se conserva** de la ruta B: el **mecanismo plantado** (prescribir una familia y
  colocar la cuádrupla en el máximo exacto del paisaje libre) es una idea combinatoria válida y
  queda en el registro como tal.
- **Objetivo absoluto `P_{2,n} -> 0`: descartado por vacuidad**, no por dificultad — el colapso
  conjunto de numerador y denominador (Adv. 13.16) lo liquida como demostración de recuperación.
- **Única pregunta con sustancia: `liminf T_n > 0`** (punto 1 de la lista `OPEN`). El `~0.70`
  está observado exclusivamente en `n ∈ {64,96,128}`: es evidencia numérica finita,
  **no** un teorema ni evidencia hasta `n=16000`. Esta corrección documental queda
  autorizada por la firma del PI de 2026-08-17.
- **Redirección.** El esfuerzo no continúa aquí ni en más fuerza bruta computacional. Ver
  `emergencia/HOJA_DE_RUTA.md` §19 y `emergencia/P1a_puerta_teorica_en_Minkowski.md` §13.9.

```text
COMMITTEE_050_SIGNOFF = ACCEPTED_WITH_OVERRIDE_NO_RECONVENE
COMMITTEE_050_C2_BRUTE_FORCE = DECLINED_BY_PI
```
