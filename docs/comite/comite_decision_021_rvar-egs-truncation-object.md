# Comité Decision 021 — rvar-egs-truncation-object

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Comité 020 §9 paso 6 (autorizado por el PI, 2026-07-05): convocar una NUEVA pregunta de comité
para definir el objeto de truncación-por-singularidad de Schwarzschild order-only que el PI firmó
como dirección de re-scope en comité 020 §11.3, tras el cierre de Part F
(BLOCKED_BY_MEASURED_DEGENERACY, `docs/rvar_partF_disposition.md`, commit `896ec3e`) y el re-scope
de Parte E (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_3.md`, commit `c92cb40`).

Pregunta a adjudicar: ¿cuál es el objeto candidato correcto para una localización order-only de la
truncación por singularidad de Schwarzschild en el patch finito 1+1D, con (a) un observable
GRADUADO (no un flag binario EMPTY/nonempty — esa vía quedó RECHAZADA unánimemente en comité 020
§8 por ser un artefacto de aspect-ratio de la caja), (b) un nulo MINK no degenerado (la dirección
apuntada por el propio comité 020 es la bimodalidad de cardinalidad-de-futuro / cadena-más-larga de
EGS, EGS PDF p.11-12), y (c) libre de los defectos que mataron el R-VAR anterior: sin artefacto de
esquina en el argmax, sin fuga de ground-truth en ninguna clave auxiliar de ordenamiento, y con el
caveat EGS de "no funcionaría para agujeros negros regulares" (EGS PDF p.12) incorporado
explícitamente al texto del claim, no como amenaza externa?

Debe fijar, antes de cualquier implementación: objeto candidato preciso; nulo MINK y por qué es
no-degenerado (con evidencia, no solo argumento); control de artefacto de frontera/caja; claims
prohibidos (`NO_RECONSTRUCTION_CLAIM`, no horizonte-evento, alcance 1+1D); condición de cierre
negativo explícita (si el objeto falla su propio Gate 0/calibración, R-VAR se cierra como resultado
negativo documentado — criterio ya fijado por el PI en comité 020 §11.3); y la condición mínima
que autorizaría pasar a implementación (spec + Gate 0 propio, freeze ∀-antes-que-∃ sobre semillas
no vistas — EXPLORE_POOL/VALIDATION_SEEDS intactos).

No autorizado por esta convocatoria: ninguna ejecución, ningún draw de
EXPLORE_POOL/VALIDATION_SEEDS, ningún cómputo. Es puramente definición de objeto + condiciones de
freeze.

## 2. Verified state

Facts checked **this session** (2026-07-05), each with its command/file:line.

- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` = `docs/preregistration_002.md:8`. MATCH.
- `git log --oneline -6`: HEAD=`c92cb40` (Part E re-scope v2.3), `896ec3e` (Part F disposition),
  `5014a39` (cross-key probe, leakage confirmed branch (a)), `4a408a8` (adjudication record
  commit), `6347459` (structure probe), `014d364` (feasibility blocker).
- `git status --short`: only pre-existing, unrelated working-tree items (`M INSTRUCCIONES.md`,
  untracked Alloy/image files) — nothing R-VAR related uncommitted.
- Seed bands (`nachocausal/thresholds.py:47-74`, `dev/explore_seeds.py`): `DEV_SEEDS =
  (20240617, 13, 101, 7, 42, 99, 2718, 31415)`; `EXPLORE_POOL = 1_000_000..1_000_039` (dev-only);
  `VALIDATION_SEEDS` = 20 seeds in `[2_076_703, 2_983_811]`, drawn once from the reserved virgin
  band `[2_000_000, 2_999_999]`, already burned for prereg-002 PASS, untouched by anything R-VAR.
- Geometry (`nachocausal/thresholds.py:36-43`): `T_EDGE=6.0`, `R_EDGE=1.2`, `R_CENTER=0.7`,
  `R_S=0.5` (=2M), `BOX_AREA=7.2`, sprinkling domain `r∈[0.1,1.3]`. **r=0 is NOT in the sprinkled
  patch** (falsifier finding, §5). `INTENSITIES=(1500,3000,6000,12000)`, primary `12000`,
  `ENSEMBLE=20`, `SAME_CLOUD=True`.
- No longest-chain or future-cardinality-restricted-to-`Min(C)` primitive currently exists in
  `nachocausal/*.py` (`grep -rn "longest.chain\|future.*card" nachocausal/*.py` → no hits outside
  comments) — any such object is new `dev/` work.
- Prior art: prereg-001's original primary observable was future-HEIGHT (longest future chain),
  REPLACED by future-VOLUME (`O_min(i)=|future(i)|`, column-sum of `C`) after a measured coverage
  FAIL in blind validation (`docs/estimator_v2_freeze.md:34-37,119`).
- `NON_CORROBORATION` precedent (comité 017 §8, `docs/comite/comite_decision_017_r-var-v2-reconvene.md:173,332`):
  "since d⁺ and O_min read the same future-truncation imprint, any future BH-patch agreement
  between R-VAR and the sealed estimator... may never be cited as independent corroboration of the
  prereg-002 PASS."
- Comité 020 full disposition record: `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md`
  — §4 physicist brief (old R-VAR argmax was a corner artifact, `|D*|≈N−few, B∈{3..8}` independent
  of N); §8 synthesis (unanimous rejection of the binary dichotomy; signed direction = graded
  observable + non-degenerate MINK null); §9 step 6 (this convocation).
- Part F disposition: `docs/rvar_partF_disposition.md` (commit `896ec3e`) —
  `PARTF_STATUS=BLOCKED_BY_MEASURED_DEGENERACY`, never executed.
- Part E re-scope: `dev/PR003_R_VAR_SELECTOR_SPEC_V2_3.md` (commit `c92cb40`) — polynomiality
  bounded to interval-certified orders; interval-DP DISQUALIFIED for ground-truth leakage
  (kind-dependent sort key, cross-key probe `5014a39`, branch (a)).
- Structure probe: `dev/PR003_RVAR_STRUCTURE_PROBE_REPORT.md`, `dev/rvar_structure_probe_result.json`
  (commit `6347459`) — MINK `𝒜(C)=∅` certified 12/12 draws (dev seeds 20240617/13/101, 4
  intensities); BH 100% partial-interval minimals, K=116-436; interval property 0 violations 24/24
  under ingoing sort `p=t+r` (MINK `u=t-r`), outgoing sort `q=t-r*` FAILS in BH (5000+ violations).
  **These three dev draws already exist and are already consumed** — a fresh measurement reusing
  them draws zero new seeds (falsifier's minimal test, §5).
- EGS paper (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`),
  the candidate-object source, **all citations independently verified this session by the
  literature-verifier seat (§7)**: line 226 (longest-chain-from-minimal, interior bounded by
  finite proper time to r=0); line 237 (Fig.3: upper=longest-chain-by-r, lower=cardinality-of-
  future-by-r, 400 sprinklings n=10³); line 239-245 (sharp transition, bimodal, "without reference
  to coordinates"); line 247 (cardinality-of-future variant explicitly scoped to a **causal
  diamond**, "varies between n and √n already for Minkowski" — literature-verifier CONFIRMED this
  is textually a diamond, not a box, statement); line 249 (regular-BH caveat, PDF p.12, confirmed
  by page-marker bracketing, correcting an earlier committee's p.11 mis-cite); line 616 (§VI
  restatement).
- Bombelli 1987 PhD order-dim-2 claim: substance CONFIRMED, but literature-verifier found comité
  020 §7's page citation (PDF pp.61-63) is WRONG — the actual passage is at PDF file-page 67 /
  printed p.62 (§2.4), and the `derived-md` OCR fails to extract it at any location (verifiable
  only against the raw PDF). Recorded for the project's citation-hygiene record; does not change
  the underlying mathematical claim (still CONFIRMED in the primary source).
- "Future-cardinality" is CONFIRMED project house terminology, not EGS's literal wording (EGS says
  "cardinality of the future of minimal points/elements") — analogous to the prior "C_k"/d⁺
  Benincasa–Dowker bridge-terminology finding (comité 020 §7). Use "cardinality of the future"
  going forward to avoid terminology drift.
- Binding guardrail tokens (unchanged, must persist into any new object): `NO_RECONSTRUCTION_CLAIM`,
  `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`,
  `NON_CORROBORATION` (comité 017 §8).

## 3. Dossier

- `docs/comite/comite_decision_020_rvar-partF-degeneracy-disposition.md` (full, esp. §4 physicist
  brief and §8 synthesis)
- `docs/rvar_partF_disposition.md` (commit `896ec3e`)
- `dev/PR003_R_VAR_SELECTOR_SPEC_V2_3.md` (commit `c92cb40`)
- `dev/PR003_RVAR_STRUCTURE_PROBE_REPORT.md` + `dev/rvar_structure_probe_result.json` (commit
  `6347459`)
- `dev/rvar_crosskey_probe_result.json` (commit `5014a39`)
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md` (EGS,
  arXiv:2605.06813) — lines 226, 237, 239-245, 247, 249, 616
- `biblioteca/derived-md/Bombelli_1987_PhD.md` — order-dim-2 (citation location corrected, §2/§7)
- `nachocausal/generator.py`, `nachocausal/thresholds.py`
- `docs/estimator_v2_freeze.md` (sealed `O_min` definition, clause A)
- `docs/preregistration_001_result.md` (future-HEIGHT precedent)

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):** This convocation authorises *definition + freeze conditions only* (no
  code, no run), so the concrete artefact is a **spec document**, not a measurement. Following the
  established dev naming lineage (`dev/PR003_R_VAR_SELECTOR_SPEC_V2_3.md`, `c92cb40`;
  `dev/PR003_RVAR_STRUCTURE_PROBE_REPORT.md`, `6347459`), the object should be fixed in a new
  committed dev spec, e.g. `dev/PR003_RVAR_EGS_OBJECT_SPEC_V1.md`, stating: (i) the candidate
  object — EGS "longest chain from each minimal element" as a **graded, r-sortable diagnostic over
  `Min(C)` only** (EGS md line 226, 239–245), explicitly NOT the future-cardinality variant as
  primary (see risk 1); (ii) its self-contained Gate 0 (witness-poset table + brute-force
  cross-check, the format already used in `dev/gate0_tier0_result.json`); (iii) the frozen
  non-degeneracy null and boundary-artefact control. When/if implementation is later authorised,
  the run script and result belong at `dev/measure_pr003_rvar_egs_object.py` →
  `dev/rvar_egs_object_result.json`, mirroring the existing `measure_pr003_rvar_structure_probe.py`
  → `rvar_structure_probe_result.json` pair. All artefacts live under `dev/`; none touch
  `nachocausal/` (sealed).
- **Environment & seal:** `numpy==1.26.4` hard-pinned (`nachocausal/thresholds.py:21-30`
  `assert_environment()`). Re-verify `make verify-seal` before any run, byte-match `6e2c3888...`
  against `docs/preregistration_002.md:8`. The EGS object is a new dev diagnostic and must not
  re-hash or re-freeze `thresholds.py`.
- **Provenance capture:** Existing probe JSONs (`dev/rvar_structure_probe_result.json`,
  `dev/rvar_crosskey_probe_result.json`) omit git commit, numpy version, uname, timestamp — a live
  gap. The new spec's capture contract must mandate all of these plus explicit seed-band
  declaration and a CLAIM-INERT `scope` string.
- **Run mechanics:** Deliverable authorised now is spec + Gate 0 on paper/dev only —
  single-invocation, reversible, consumes no reserved seeds. Committing step (μ/table on unseen
  seeds) stays gated behind the object's own Gate 0. Front-load seal verify → numpy assert →
  seed-band assert → Gate 0; failing any aborts before a single draw.
- **Reproducibility risks / ambiguities:**
  - **Risk 1 — variant choice affects reproducibility of the null.** EGS flags the future-
    cardinality variant as boundary-sensitive (line 247) and warns the longest-chain partition
    "would no longer work for regular black holes" (line 249). Spec must fix longest-chain-from-
    minimals as PRIMARY, future-cardinality as labelled SECONDARY, regular-BH caveat in claim text.
  - **Risk 2 — NON_CORROBORATION inheritance.** Future-cardinality-of-minimals is literally the
    sealed `O_min(i)=|future(i)|` restricted to `i∈Min(C)`; comité 017 §8 forbids citing agreement
    as independent corroboration.
  - **Risk 3 — future-HEIGHT precedent.** The longest-chain object is chain-based, same family as
    prereg-001's REPLACED future-HEIGHT. Spec must record why a `Min(C)`-localised partition
    variant does not inherit that coverage failure — otherwise not reproducibly distinguishable
    from a known-failed statistic.
  - **Risk 4 — sort-key determinism/GT-leakage.** The interval property is sort-key-dependent
    (ingoing passes, outgoing fails in BH); any r-sorting/tie-break must be order-only, frozen,
    kind-blind. The leak-free sort rule is not yet defined — `[partly UNVERIFIED]`.
  - **Risk 5 — provenance gap is a live defect** in current JSONs; must be closed in the spec's
    capture contract, not left to the implementer.

### Mathematician brief

- **Computability.** `Min(C)` (row/column predicate on `C`) and height `L(i)` (longest-path DP
  over the Hasse DAG, topological order, `O(N·|relations|)`) are both order-only, polynomial,
  permutation-invariant. Order-dim-2 (Bombelli 1987, confirmed comité 020 §7 — location corrected
  §7 below) makes `Min(C)` and heights recoverable "without reference to coordinates" (EGS line
  245). A domain/abstaining gate `τ(n)` is mandatory: must ABSTAIN (`OUT_OF_DOMAIN`) when a
  frozen-before-validation separation certificate fails.
- **Order observable.** Graded distribution `{L(i): i∈Min(C)}`, expected bimodal (interior bounded
  by finite-proper-time-to-singularity; exterior box-limited). Structurally distinct from killed
  `𝒜(C)` down-set object — does not inherit the `|D*|≈N−few, B∈{3..8}` corner artifact (comité 020
  §4).
- **Relevant invariants.** Height/longest-chain (EGS Fig.3 upper, line 237) is load-bearing;
  future-volume (Fig.3 lower, line 247) is secondary — literally sealed `O_min` restricted to
  `Min(C)` ⇒ `NON_CORROBORATION` binds; also more boundary-sensitive per EGS. Recommendation:
  height `L` primary, future-cardinality secondary/diagnostic with explicit `NON_CORROBORATION`
  caveat.
- **Analytic / continuum target.** Sharp transition in `L` at `r=r_S=0.5`; interior
  `L·ℓ→τ_max(r)<∞`, exterior upper mode set by `T_EDGE=6.0`. Localisation target, NOT
  reconstruction, NOT asymptotic event-horizon.
- **Caveats.**
  - future-HEIGHT was prereg-001's ORIGINAL primary and FAILED blind validation on coverage; a
    height-based candidate MUST justify why a partition diagnostic over `Min(C)` escapes that
    failure mode — it does not automatically. [anchored]
  - MINK non-degeneracy must be SHOWN, not argued. EGS's "n vs √n already in Minkowski" evidence
    (line 247) is for a **causal diamond**, not our TALL RECTANGLE (`T_EDGE=6.0, R_EDGE=1.2`) — it
    does not transfer. Empirical non-degeneracy on THIS geometry is `[UNVERIFIED]` and is precisely
    what a future Gate 0 must certify.
  - Whether `T_EDGE=6.0` is "large enough timelike extent" for a clean valley is `[UNVERIFIED]`.
  - Boundary/corner control: the partition count must SCALE WITH `n_min` (comité 020 §4 criterion),
    certified per-draw before any threshold freeze.
  - Regular-BH caveat (line 249, PDF p.12) MUST be written into the claim text itself.
  - `NO_GROUND_TRUTH_LEAKAGE`: heights use only `≺`; no hidden-kind-dependent sort key.

### Mathematical logic brief

- **Formal status.** Candidate is a function `f: Min(C)→ℕ`, two variants: (i) height of longest
  chain from `i`, (ii) `|future(i)|` restricted to `Min(C)`. Neither exists yet in
  `nachocausal/*.py`. EGS bimodality is an EXPECTATION/empirical observation over 400 sprinklings
  at n≈10³ (lines 237, 239, 245), NOT a proven theorem — treat "bimodal ⇒ partition" as a
  conjecture under test. MINK `𝒜(C)=∅` 12/12 was an empirical certification of the REJECTED
  degenerate null, not a template to reuse.
- **Quantifier/dependency order.** Freeze must be `∀-before-∃`: object `f`, kind-blind sort key,
  MINK null, boundary control, mode-separation threshold ALL fixed before ANY `VALIDATION_SEEDS`
  draw. Post-hoc traps: EGS's "box with large enough timelike extent" (line 245) is a free
  parameter — the box is ALREADY frozen (`T_EDGE=6.0`) and must not be re-tuned per-draw. The
  interior/exterior cut must be a pre-registered rule, frozen before reveal. The sort-key must be
  kind-blind and fixed a priori — the outgoing key fails in BH (5000+ violations), so key-by-
  hidden-kind is leakage (cross-key probe `5014a39` branch (a) precedent).
- **Equivalence claims.** "Inside horizon ⟺ f(i) bounded" is NOT a proved iff — only the interior
  arm has a mechanism; the exterior arm is "in practice" box-limited, not intrinsically unbounded —
  do not cite as biconditional. Variant (ii) is literally `⊆` sealed `O_min` restricted to
  `Min(C)` — `NON_CORROBORATION` binds, must be written into the claim not inherited silently.
  Variant (i) is the same functional class as superseded future-HEIGHT — must state why a
  `Min(C)`-localisation diagnostic escapes the coverage failure. The graded object must NOT
  collapse back to the rejected binary dichotomy.
- **Type/object discipline.** `Min(C)` is a set/antichain; `future(i)` a principal filter; variant
  (ii) is filter-cardinality, variant (i) is filter-height — distinct functionals, conflating them
  is a category error (exactly the future-VOLUME≠future-HEIGHT distinction). "The partition" is a
  derived 2-class quotient induced by a threshold on `f`, NOT an intrinsic order-theoretic set —
  "the horizon" is an embedding/physical object, never an order invariant; ground-truth `r` may
  score only, never enter `f` or the sort key.
- **Caveats.**
  - The regular-BH exclusion is itself only an EGS expectation ("we expect... likely", line 249,
    PDF p.12), not proved — embed as a stated scope limit, not a derived theorem.
  - Variant (ii)'s non-degenerate-MINK evidence is for a **causal diamond** (line 247); our
    geometry is a **box** — mark non-degeneracy of OUR MINK null `[UNVERIFIED]` until a dev-seed
    (EXPLORE_POOL only) measurement.
  - EGS's Fig.3 evidence is at n≈10³ vs our primary intensity 12000 — comparable order but our
    frozen `T_EDGE=6.0` may sit in a regime where the transition is not yet sharp — `[UNVERIFIED]`,
    live risk.
  - Minimal condition to authorise implementation: a committed spec fixing (a) which functional
    variant, (b) the a-priori kind-blind sort key, (c) the frozen mode-cut rule, (d) the
    `NON_CORROBORATION` statement, and (e) an own Gate 0 on EXPLORE_POOL only — with `∀-before-∃`
    freeze and `VALIDATION_SEEDS` intact. No execution, no draw, no computation is authorised by
    this convocation.

### Physicist brief

- **Coordinates & patch.** Must use the ingoing EF branch (`generator.py`, `t_in=r_j-r_i`),
  consistent with the structure-probe finding (ingoing `p=t+r` passes the interval property,
  outgoing `q=t-r*` fails in BH, 5000+ violations, `6347459`). The finite patch is the frozen tall
  box. What finiteness forfeits: the true event horizon needs infinite proper-length timelike
  curves to 𝒥⁺ (EGS p.10-11); in a finite box, the exterior longest chain is "in practice only
  limited by... size" (line 239) — the object is a SINGULARITY-TRUNCATION CUT inside a finite
  patch, NOT an asymptotic event horizon.
- **Physical meaning of the signal.** Interior minimals: bounded longest chain (every interior
  timelike curve reaches r=0 in finite proper time — singularity-truncated future, lines
  226-239). Exterior: box-limited only. Sharp transition at r=2M; bimodal, order-only partition
  (lines 239-245). The graded observable is longest-chain length per minimal element — NOT the
  rejected binary flag. This is the physically correct read of the r=2M imprint: a graded
  truncation depth, not a box-aspect-ratio corner artifact.
- **Sprinkling domain.** Frozen tall box, Poisson sprinkling, frozen intensities `(1500, 3000,
  6000, 12000)`, primary 12000, `ENSEMBLE=20`, `SAME_CLOUD=True`. Forfeited: exterior mode is a
  box-size feature, not an intrinsic scale; boundary/corner sensitivity (comité 020 §4's
  corner-artifact finding on the OLD object) means the NEW object must carry an explicit boundary/
  corner control before implementation. EGS flags the future-cardinality variant as MORE
  boundary-sensitive than longest-chain (line 247) — argues for longest-chain-over-`Min(C)` as
  PRIMARY.
- **Claim boundary.** Claims order-only localisation of the Schwarzschild singularity-truncation
  cut in a finite 1+1D patch, expressed as a graded, bimodal partition of minimal elements. Does
  NOT claim metric reconstruction (`NO_RECONSTRUCTION_CLAIM`), NOT an event-horizon/asymptotic-𝒥⁺
  result, NOT 3+1D. The regular-black-hole caveat is PART OF THE CLAIM TEXT, not an external
  threat (EGS line 249, PDF p.12) — the diagnostic keys specifically on the *singular* Schwarzschild
  interior; this limitation is stated as a scope condition, not concealed.
- **Caveats.**
  - Future-HEIGHT inheritance risk — same family as prereg-001's REPLACED observable; must justify
    escape, cannot be assumed.
  - `NON_CORROBORATION` binding for the future-cardinality variant (literally sealed `O_min`
    restricted to `Min(C)`); the longest-chain variant is a DIFFERENT statistic (height not
    volume) and preferable partly for this reason, but the relationship must still be stated. **[The
    falsifier, §5, rejects this carve-out — see synthesis §8.]**
  - MINK non-degeneracy has TEXTUAL evidence, not just argument: EGS states "n vs √n already for
    Minkowski" in a causal diamond (line 247) — physically, MINK has no singularity hence no
    interior-truncation mode, so MINK longest-chain/cardinality distribution is expected box-
    limited/UNIMODAL rather than BH's bimodal — that CONTRAST is the signal. **[Live, unresolved
    tension with mathematician/logician — flagged explicitly for the falsifier and resolved against
    the physicist's reading in §8.]**
  - No primitive exists yet — new `dev/` work, CLAIM-INERT until Gate 0.
  - Negative-closure honesty: if the object fails its own Gate 0/calibration, R-VAR closes as a
    documented negative result (criterion fixed by the PI, comité 020 §11.3) — reported alike to a
    PASS, no coercion.

## 5. Falsifier attack

- **Concrete failure modes:**
  1. **The MINK null may be quasi-degenerate, not "non-degenerate," on THIS box — and the repo's
     own data points that way.** The structure probe certifies `unrelated_min_max_pairs = 0` in
     12/12 MINK draws: every minimal precedes every maximal. In a box where light crosses the
     spatial width in `Δt=R_EDGE=1.2 ≪ T_EDGE=6`, every minimal's future is nearly the whole set
     and every minimal's longest chain runs to the top slice. Both variants (`L(i)` and
     `|future(i)|` over `Min(C)`) are therefore expected to concentrate in a narrow spike — NOT
     EGS's "varies between n and √n" regime, which is explicitly a **causal diamond** statement
     (literature-verifier CONFIRMED §7). A near-deterministic null makes quantile/valley
     calibration ill-posed for the same structural reason `rate_empty≈1` made μ ill-posed —
     degeneracy one level up, dressed as gradedness. **This resolves the wave-1 tension in the
     mathematician/logician's favor**, and with a track record: the physicist seat's geometric
     prediction on this exact box already inverted once before (comité 020 §4, "Why comité-019's
     prediction inverted"). Non-degeneracy on this geometry is `[UNVERIFIED]` until measured; the
     spec must define "non-degenerate" quantitatively (minimum null spread relative to the
     discreteness floor, cf. `POOLED_SD_FLOOR`) so the criterion can FAIL.
  2. **"Singularity truncation" is literally false for this patch: r=0 is not in the box.** The
     sprinkling domain is `r∈[0.1,1.3]`. Interior chains terminate at the frozen inner excision
     edge `r=0.1`, not at the singularity. The interior mode is therefore an inner-boundary-
     truncation mode that *proxies* singularity truncation. The claim text must say "truncation at
     the inner excision boundary as proxy for singularity truncation" or it over-claims; and the
     lower tail is populated by proximity to the same inner-top corner that produced the OLD
     object's corner artifact. The mandated corner control must be the pre-registered scaling law:
     interior-mode occupancy ≈ `n_min·(0.4/1.2)` and **grows with `n_min` across the four frozen
     intensities** (n_min 13-21 at 1500 → ≈64-73 at 12000). A constant-count lower mode = corner
     artifact = negative closure.
  3. **The future-HEIGHT ghost is unexorcised.** Variant (i) is the same functional class as
     prereg-001's observable, which FAILED blind validation and was REPLACED. Every wave-1 brief
     says "must justify escape"; **none supplies the justification.** The plausible escape (a
     per-minimal *partition* task tolerates height's variance better than a *point-localisation*
     task did) is an unproven conjecture and must be written into the spec as such, with a
     coverage-analogue failure clause.
  4. **Statistical power ceiling: the whole observable lives on ~64-73 samples per draw.** Support
     is `Min(C)`, `n_min≈64-73` at primary intensity, ~1/3 interior (~21-24 points in the lower
     mode). Bimodality/dip tests at `n≈70` are weak; `ENSEMBLE=20` helps only if pooling across
     seeds is pre-specified. Underpowered ⇒ chronic INCONCLUSIVE ⇒ coercion pressure (below). The
     spec must state the pooling rule and a power argument, or pre-accept that
     `OUT_OF_DOMAIN`/`INCONCLUSIVE` is a likely and *honorable* endpoint.
  5. **EGS's transition sharpness is conditioned on "large enough timelike extent"** at n≈10³ in
     *their* patches; whether the frozen `T_EDGE=6.0` sits in the sharp regime for our patch is
     `[UNVERIFIED]`. If not, the only compliant outcome is negative closure — not a bigger box.
  6. **`NON_CORROBORATION` is imprint-based, not statistic-based — the physicist's carve-out for
     variant (i) fails.** Comité 017's clause reads "d⁺ and O_min read the same **future-truncation
     imprint**" — not "the same functional." Longest-chain-from-minimals reads that same imprint
     (chains truncate because futures truncate). **BOTH variants must carry the `NON_CORROBORATION`
     label**; any spec that exempts variant (i) because "height ≠ volume" is laundering
     corroboration through a functional relabel.

- **Ground-truth leakage:**
  - Every ordering key currently in the repo is coordinate-derived (`p=t+r`, `u=t−r`, `r`,
    `q=t−r*`), and key choice already leaked kind once (cross-key probe branch (a), commit
    `5014a39`). Height `L(i)` needs no sort key to *compute* — the spec must say exactly that and
    **ban import of any interval-DP key machinery** into this object; any tie-break, binning, or
    presentation order that touches `t`, `r`, `t±r`, `r*` is leakage. "r-sortable diagnostic" is a
    red flag: r-sorting is Fig.3 *presentation using ground truth* (EGS: "the same information
    could of course be extracted without reference to coordinates") — allowed for scoring plots
    only, never in the observable, the valley rule, or the domain gate.
  - Valley-cut contamination: the interior/exterior threshold rule must be frozen from order-only
    quantities; every dev look at r-labelled histograms during rule design must be recorded
    (`dev/dip_check.py`, `dev/dip_diag.py` already exist for this purpose).
  - Embedding may score the final partition (fraction of lower-mode minimals with `r<r_S`) — score
    only; a scoring miss falsifies, never triggers redesign of `f`.

- **Freeze violations:**
  - Geometry re-tuning is the #1 smuggle path: EGS invites "increase the timelike extent";
    `T_EDGE=6.0` is frozen. Any clause permitting box enlargement after a weak valley is
    `NO_POST_HOC_TUNING` + de-facto `NO_THRESHOLD_LOOSENING`. If `T_EDGE=6.0` is insufficient:
    negative closure, full stop.
  - Primary-variant selection by outcome: primary=longest-chain, secondary=future-cardinality must
    be fixed in this convocation's output, before any dev histogram of either is drawn; the spec
    must forbid post-hoc promotion of the secondary if the primary fails (that would repeat the
    future-HEIGHT→future-VOLUME move, which last time cost a burned validation band).
  - Gate 0 acceptance criteria must be committed before the Gate 0 runs (comité 020 precedent:
    criteria written after seeing production behavior are tailored criteria).
  - No draw is authorized by this convocation; the spec text itself must not embed any number
    derived from an unauthorized peek. Provenance gap (probe JSONs lack commit/env/timestamp) must
    be closed in the spec.

- **Verdict coercion:**
  - Graded→binary relapse: a threshold on `f` yields a 2-class output; if reported as "horizon
    found/not found" the committee has rebuilt the unanimously rejected EMPTY/nonempty flag one
    level up. The reportable object must be the distribution + pre-frozen separation statistic,
    with a three-valued outcome (LOCALISED / NOT-LOCALISED / `OUT_OF_DOMAIN`-INCONCLUSIVE), reported
    with identical prominence.
  - Underpowered-INCONCLUSIVE laundering: with ~70 samples/draw, weak-valley results are likely;
    the spec must pre-commit the number of dev draws allowed before freeze and the exact
    `OUT_OF_DOMAIN` certificate, stating OOD is neither FAIL nor PASS.

- **Premature / over-broad claims:** metric reconstruction; event horizon/asymptotic 𝒥⁺; apparent
  horizon (EGS's distinct ladder diagnostic); 3+1D; horizon-generic detection (the regular-BH
  caveat is itself only an EGS *expectation*, state as scope limit not theorem); "singularity
  localisation" without the r=0.1-excision-proxy caveat (failure mode 2); any corroboration of the
  prereg-002 PASS from either variant (failure mode 6); "recovery of horizon structure" phrasing
  that drops the recoverability-benchmark framing.

- **Independent-falsification gate:** Partially satisfied at the committee level (this wave-2 seat
  is adversarial to wave-1), but structurally unsatisfied downstream: the same chair/PI pipeline
  will author the spec, its Gate 0, and its acceptance criteria. Mitigation must be mechanical:
  Gate-0 criteria and the non-degeneracy criterion committed (hash-fixed) *before* the Gate-0 run,
  brute-force cross-check included; negative-closure condition signed now so closing negative
  requires no discretion later. The physicist's necessity argument for MINK non-degeneracy must be
  recorded as a *prediction to be tested*, never a substitute for the test.

- **Minimal falsification test:** One dev-only, seed-band-neutral measurement (future
  authorization; nothing runs under this convocation): on the three **already-consumed** dev
  draws (seeds 20240617/13/101 — the exact draws in `dev/rvar_structure_probe_result.json`, zero
  new seed consumption), compute order-only `{L(i): i∈Min(C)}` and `{|future(i)|: i∈Min(C)}` for
  MINK and BH at all four frozen intensities, and report (a) MINK null coefficient of variation vs
  a pre-stated floor and unimodality, and (b) BH lower-mode occupancy vs `n_min` across
  intensities (scaling ⇒ horizon-cut candidate; constant ⇒ corner artifact redux). This single
  check attacks the two worst failure modes simultaneously and every branch is informative. If (a)
  fails, the object dies before any spec is implemented — the negative closure the PI signed for
  in comité 020 §11.3.

## 6. Pre-registration verdict

- **Verdict: PASS** (scoped strictly to the convocation as authorized: definition of the
  candidate object + freeze conditions; zero execution, zero seed draw, zero code).
- **Freeze status:** Not yet applicable to a new threshold — correctly so; this convocation is
  pre-freeze by design. Authorization chain is git-anchored: comité 020 §9 step 6 and §11 sign-off
  item 3. The box constants this object would sort against are already frozen and untouched
  (`T_EDGE=6.0, R_EDGE=1.2, R_S=0.5`, `thresholds.py:36-40`).
- **Seal integrity:** No sealed path is run. `make verify-seal` MATCH confirmed against
  `docs/preregistration_002.md:8`. Nothing proposes touching `nachocausal/thresholds.py`; all new
  artefacts scoped to `dev/` only.
- **Seed discipline:** No seeds drawn by this convocation. `DEV_SEEDS`, `EXPLORE_POOL` (dev-only),
  `VALIDATION_SEEDS` (burned for prereg-002, untouched by R-VAR) all confirmed disjoint and
  undisturbed. Wave-1's proposed future Gate 0 is explicitly scoped to dev/toy posets and
  `DEV_SEEDS`, never `EXPLORE_POOL`/`VALIDATION_SEEDS`.
- **Reporting rule:** Negative-closure is explicit and pre-committed: "If that object fails its own
  Gate 0 / calibration, R-VAR closes as a documented negative result" (comité 020 §11.3 item 3).
  `NON_CORROBORATION` and `rate_empty`-analogue CLAIM-INERT persist verbatim into any redesigned
  object per comité 020 §9 binding rules.
- **Forbidden moves present?** None found in the convocation as scoped. No post-hoc tuning (object
  criteria fixed before implementation, ∀-before-∃); no threshold loosening; no ground-truth
  leakage in the definition as stated (though the falsifier, §5, finds the *implementation risk* is
  live and must be closed by spec text, not assumed away); no re-run after peeking (nothing has
  run); no reconstruction over-claim (claim scoped to finite-patch 1+1D localisation); no silent
  `OOD→PASS` coercion (the `PARTF_STATUS` third-state precedent is the template to inherit).
- **Reasons:**
  - The requested output (object, MINK null + why non-degenerate, boundary control, forbidden
    claims, negative-closure condition, Gate-0 admission bar) matches exactly the six items comité
    020 §9 step 6 pre-specified as required before any implementation.
  - **Live risk flagged for the record, not a violation yet:** EGS's non-degeneracy evidence (PDF
    p.12, causal diamond) does not transfer to our tall box by citation alone (literature-verifier
    §7 confirms the textual distinction is real). The eventual spec's Gate 0 must *measure* MINK
    non-degeneracy on `DEV_SEEDS` before any `VALIDATION_SEEDS` draw is authorized; asserting
    non-degeneracy from the EGS quote alone (the physicist brief's reading) would be argument, not
    evidence, and must not substitute for measurement — the single point wave-1 seats disagree on,
    resolved by measurement (falsifier's minimal test), not by vote.
  - The regular-BH caveat (EGS PDF p.12) is correctly required by all four wave-1 briefs to sit in
    the claim text itself.
  - The corner-artifact failure mode that killed the prior R-VAR object is a property of the
    min-cut/`𝒜(C)` construction, not of a height/cardinality-over-`Min(C)` functional by
    assumption — but this remains to be *demonstrated* empirically at Gate 0, not merely argued
    structurally (falsifier failure mode 2 sharpens this: the scaling-with-`n_min` test is the
    actual demonstration required).
  - Bombelli 1987 order-dim-2 and the EGS bimodality claim are correctly treated as literature
    background/conjecture-under-test, not proof.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| EGS md:226 — longest-chain diagnostic on minimal elements, interior curves bounded by finite proper time to r=0 | Physicist, Mathematician | CONFIRMED (verbatim match) |
| EGS md:237 (Fig.3 caption) — upper panel longest-chain-by-r, lower panel cardinality-of-future-by-r, "400 sprinklings of average size n=10³" | Wave-1 | CONFIRMED (verbatim match) |
| EGS md:239-245 — sharp transition at horizon; bimodal distribution "without reference to coordinates" | Wave-1 | CONFIRMED (verbatim match, incl. "the same information could of course be extracted without reference to coordinates") |
| EGS md:247 — cardinality-of-future bimodal but boundary-sensitive; **causal diamond** example giving n to √n spread already in Minkowski | Mathematician, Logician | CONFIRMED — text literally says "if we sprinkle into a **causal diamond**...", distinct from a tall box/rectangle. The distinction wave-1 drew (causal diamond ≠ nachocausal's frozen tall-box geometry) is textually well-founded: EGS's non-degeneracy caveat is scoped to a diamond boundary, not a box, so it does not automatically transfer without separate justification |
| EGS md:249 — regular-BH caveat ("would no longer work for regular black holes... likely does not allow a partition... through these diagnostics") | Physicist | CONFIRMED, and comité 020's page correction (PDF p.12, not p.11) is independently re-verified via the PDF-page markers bracketing the line |
| EGS md:616 — §VI Conclusions restatement of the longest-chain interior/exterior diagnostic | Wave-1 | CONFIRMED (verbatim match), correctly distinct from the original Fig.3 discussion |
| Bombelli 1987 PhD — 1+1D Minkowski causal order is order-dimension-2 via null coordinates u=x⁰+x¹, v=x⁰−x¹ | Mathematician (inherited from comité 020 §7) | CONFIRMED in substance, but **citation-location correction**: the lemma is at PDF file-page 67 / printed p.62 (§2.4), not "PDF pp.61-63" as comité 020 §7 stated — those pages cover an unrelated density discussion. The `derived-md` fails to OCR-extract the passage at any location; verifiable only against the raw PDF |
| "future-cardinality" / "future cardinality" as EGS terminology | Wave-1 (multiple) | UNCONFIRMED as literal EGS wording — zero hits in derived-md. EGS's actual phrase is "the cardinality of the future of minimal points/elements." Project-coined shorthand, analogous to the prior "C_k"/d⁺ Benincasa–Dowker bridge-terminology finding |

- **Notes:** (1) All direct EGS citations (items 1-6) are verbatim-confirmed. (2) The
  causal-diamond vs. tall-box distinction is real and load-bearing exactly as wave-1's
  mathematician/logician argued — this is the textual anchor for the falsifier's failure mode 1.
  (3) The Bombelli citation page should be corrected in the project record going forward (PDF
  file-page 67/printed p.62, not pp.61-63); the underlying mathematical claim remains correct. (4)
  "Future-cardinality" should be replaced with "cardinality of the future" in spec text to avoid
  terminology drift, matching the project's existing C_k/d⁺ hygiene practice.

## 8. Synthesis

**Direction: converges on a candidate object, but with a materially different confidence profile
than wave-1's initial framing** — the falsifier's attack, corroborated by the literature verifier's
independent confirmation of the causal-diamond/tall-box distinction, demotes "non-degenerate MINK
null" from a near-settled premise to a **live, measurable, currently-unresolved risk** that could
kill the object exactly as `𝒜(C)`'s degeneracy killed Part F.

**Candidate object (adopted):** a graded, order-only function `f: Min(C)→ℕ`, with
**longest-chain-from-minimal height `L(i)`** as the PRIMARY statistic (EGS md:226,239-245,616) and
**cardinality-of-the-future restricted to `Min(C)`** as a labelled SECONDARY/diagnostic variant
(EGS md:247) — never the reverse, and never promoted post-hoc if the primary underperforms
(falsifier, freeze violations). Both variants are computable from `≺` alone with no auxiliary sort
key (mathematician; falsifier ground-truth-leakage section) — this is a structural improvement
over the disqualified interval-DP, which required an unspecified order-only key derivation that
does not yet exist.

**Non-degenerate MINK null: NOT YET ESTABLISHED, condition (b) of the decision question is
open.** Wave-1's physicist read EGS's causal-diamond evidence as transferring by physical necessity
(no singularity in MINK ⇒ unimodal contrast IS the signal); wave-1's mathematician and logician
both independently flagged this as `[UNVERIFIED]` on our box geometry. The falsifier resolves this
tension **against** the physicist's reading, with a mechanism: this project's own tall-box aspect
ratio (`R_EDGE=1.2 ≪ T_EDGE=6`) is exactly the geometry that made every MINK minimal precede every
MINK maximal (12/12, `𝒜(C)=∅` certified) — the same mechanism plausibly concentrates both `L(i)`
and `|future(i)|` into a narrow MINK spike, which is degeneracy dressed as gradedness, not a fix.
The literature verifier's independent confirmation that EGS's non-degeneracy quote is scoped to a
**causal diamond**, not a box, removes the citation as evidence for our geometry. **This is not
disqualifying on its own — it is exactly the kind of thing a cheap dev-seed measurement resolves,
and the three dev draws needed for it already exist and are already consumed (zero new seed
cost).**

**Boundary/corner-artifact control: adopted as a falsifiable scaling law, not a description.**
The prior object's `B∈{3..8}` independent of N was retrospectively diagnosed as a corner artifact.
For this object, the pre-registered test is that BH lower-mode (interior) occupancy must **scale
with `n_min`** across the four frozen intensities (`n_min≈13-21` at 1500 → `≈64-73` at 12000); a
constant count is a corner-artifact verdict, not a horizon-cut verdict, and triggers negative
closure exactly as a failed Gate 0 would.

**`NON_CORROBORATION` scope: BROADENED per the falsifier, overruling wave-1's narrower reading.**
Wave-1 (mathematician, logician, physicist) all scoped `NON_CORROBORATION` to the future-
cardinality variant only, on the reasoning that it is literally `⊆` the sealed `O_min`. The
falsifier correctly reads comité 017 §8's actual language — "the same future-truncation imprint,"
not "the same functional" — and finds this binds height too (chains truncate because futures
truncate; both read the same underlying mechanism). **Adopted: `NON_CORROBORATION` applies to
BOTH variants**, permanently, per any future spec text.

**Claim-boundary additions, all adopted:** (i) the regular-BH caveat (EGS PDF p.12) sits inside the
claim text as a stated scope condition, not a theorem, not an external threat (physicist,
logician); (ii) a new, previously-unflagged caveat from the falsifier: **the interior truncation
this object measures is truncation at the frozen inner excision edge `r=0.1`, not at the physical
singularity `r=0`** (`r∈[0.1,1.3]`, `thresholds.py`), since `r=0` is outside the sprinkled patch —
any claim text must say "excision-boundary-proxy for singularity truncation," not "singularity
truncation," or it over-claims by omission; (iii) the future-HEIGHT precedent (prereg-001's
coverage FAIL) is flagged by every wave-1 seat but justified by none — the spec text must record
the proposed escape (partition-task vs. point-localisation-task) explicitly as an **unproven
conjecture with its own failure clause**, not settled reasoning.

**Statistical power is a genuine, previously-unraised constraint.** `n_min≈64-73` per draw with
~1/3 in the interior mode (~21-24 points) is thin for bimodality/dip testing; `ENSEMBLE=20` only
helps if a pooling rule is pre-specified. The spec must either state the pooling rule and a power
argument, or explicitly accept `OUT_OF_DOMAIN`/INCONCLUSIVE as a likely, honorable, non-coerced
outcome — never quietly re-interpreted as failure-of-signal or fished for by drawing more dev
seeds until a valley appears.

**Open disagreements, none hidden:** (i) physicist vs. mathematician/logician on whether MINK
non-degeneracy needs measurement or follows from physical necessity — resolved in favor of
measurement (falsifier + literature verifier), not by majority; (ii) wave-1's narrow
`NON_CORROBORATION` scoping (future-cardinality only) vs. the falsifier's broader reading (both
variants) — resolved in favor of the broader reading, since it tracks comité 017's actual wording;
(iii) whether the corner-artifact risk is structurally absent from a height/cardinality functional
(wave-1's implicit assumption) vs. must be independently demonstrated per-object (falsifier) —
resolved in favor of demonstration, via the adopted scaling-with-`n_min` test.

## 9. Next-step spec

**Reversible steps (may be run now if the user asks; dev seeds only, zero NEW seed consumption,
no EXPLORE_POOL, no VALIDATION_SEEDS, no seal contact):**

1. **Falsifier's minimal falsification test (adopted as mandatory first move, before any spec
   text is treated as final):** on the three already-consumed dev draws (seeds 20240617/13/101,
   the exact draws already in `dev/rvar_structure_probe_result.json` — zero new seed
   consumption), compute order-only `{L(i): i∈Min(C)}` and `{|future(i)|: i∈Min(C)}` for MINK and
   BH at all four frozen intensities. Report: (a) MINK null coefficient of variation vs. a
   pre-stated non-degeneracy floor, and unimodality; (b) BH interior-mode occupancy vs. `n_min`
   across the four intensities (scaling ⇒ candidate survives; constant ⇒ corner-artifact verdict,
   negative closure). Write-up goes to `dev/`, CLAIM-INERT, with full provenance (commit, numpy
   version, uname, timestamp — closing the reproducibility engineer's Risk 5).
2. Draft (not commit) the candidate-object spec text (`dev/PR003_RVAR_EGS_OBJECT_SPEC_V1.md`) for
   committee/PI review, incorporating: primary=height/secondary=cardinality-of-future;
   `NON_CORROBORATION` on both; excision-boundary-proxy caveat; regular-BH caveat in claim text;
   future-HEIGHT-escape stated as unproven conjecture with its own failure clause; the
   scaling-with-`n_min` boundary-artifact test as a hard Gate-0 criterion; a stated power/pooling
   rule or an explicit acceptance of likely `OUT_OF_DOMAIN`.

**Committing steps (each requires explicit user authorisation; sequenced, only after step 1's
result is known):**

3. **Spec-commit:** commit `dev/PR003_RVAR_EGS_OBJECT_SPEC_V1.md` once step 1's result is folded
   in — if step 1 fails (degenerate MINK null or non-scaling BH occupancy), this step becomes a
   **negative-result commit** instead (R-VAR closes, per the PI's criterion, comité 020 §11.3),
   never a redesign-and-retry on the same dev seeds (that would be post-hoc object tuning).
4. **Fresh Gate 0** for the adopted object (Tier 0 hand-checkable witness + Tier 1 ≥100 sprinkled
   posets, both kinds, brute-force cross-check, zero discrepancy) — criteria committed *before*
   running, on `EXPLORE_POOL` only, mirroring the existing `measure_pr003_rvar_gate0.py`/`_tier1.py`
   pattern. Must independently exercise: the excision-boundary edge case, the abstention path when
   `n_min` is too small for a valley, and the kind-blind property of `L`/`future`-cardinality
   (no coordinate ever enters the computation, only presentation).
5. **If Gate 0 passes:** freeze the object's full spec (functional choice, non-degeneracy
   threshold, mode-cut rule, `τ(n)`-analogue domain gate, `NON_CORROBORATION` statement verbatim)
   `∀-before-∃` on unseen seeds — `EXPLORE_POOL`/`VALIDATION_SEEDS` intact until that freeze names
   its own held-out band, drawn exactly once, via a pre-registered draw rule (mirroring
   `VALIDATION_DRAW_SEED`, `thresholds.py:57`).
6. **If Gate 0 or the non-degeneracy/scaling checks fail at any point:** R-VAR closes as a
   documented negative result (PI's criterion, comité 020 §11.3), reported with the same
   prominence as a PASS would be — no re-seed, no threshold loosening, no silent quiet retirement.

**Binding rules pre-committed:** `NO_RECONSTRUCTION_CLAIM` (claim stays "order-only localisation
of a singularity-excision-boundary-proxy truncation in a finite 1+1D patch," never event-horizon,
never 3+1D); `NO_POST_HOC_TUNING`/`NO_THRESHOLD_LOOSENING` (T_EDGE/R_EDGE/intensities untouched;
primary/secondary variant choice frozen before any dev histogram; box may not be enlarged after a
weak valley); `NO_GROUND_TRUTH_LEAKAGE` (no coordinate, no hidden-kind label enters `f`, the sort,
or the mode-cut rule — coordinates score only, in a separate, clearly labelled diagnostic step);
`RESPECT_SEAL_FREEZE` (seal verified unchanged this session; nothing touches `nachocausal/`);
`NON_CORROBORATION` extended to BOTH variants (falsifier's broadened reading, §8) and persists
verbatim into any further redesign; three-valued reporting (LOCALISED / NOT-LOCALISED /
`OUT_OF_DOMAIN`-INCONCLUSIVE) with identical prominence, no graded→binary relapse in reporting.
**Falsifier's minimal falsification test (§5, step 1 above) is mandatory before treating the
candidate-object spec as anything more than a draft.**

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
