# Comité Decision 048 — Adjudicación científica del target Q_FMOTS para Fase 3 B2

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Adjudicación científica única del 29 de julio de 2026 sobre el target propuesto para Fase 3 B2:
¿es admisible \(Q_{\mathrm{FMOTS}}\) (funcional binario intrínseco de existencia MOTS cuasi-local,
definido en `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md` §2)
como primer target formal para B2, con una ruta no trivial —con regularidad y canal explícitos—
para construir un par conforme estilo Müller que cambie \(Q_{\mathrm{FMOTS}}\) manteniendo próximas
las leyes de posets a cardinalidad fija?

**Alcance vinculante fijado por el PI para esta sesión:** evaluar únicamente si el target merece
adopción formal. No construir el par testigo explícito \((g_0,g_1)\). No escribir código ni
ejecutar simulaciones. No fijar ni reservar semillas. No modificar el contrato de preapertura para
declarar el target adoptado — la adopción formal es un acto separado que el PI ejecuta después de
leer esta acta. El PR #1 permanece en `DRAFT`; esta acción no toca git.

## 2. Verified state

Hechos comprobados en esta sesión, con su comando/ruta:

- `git status --short` → vacío (árbol de trabajo limpio).
- `git rev-parse HEAD` = `2a8851fd844f56387eda61efec2e4c6a26ab2d67` (rama
  `agent/phase2-b2-documentation`); `git rev-parse origin/main` =
  `29f84357ae7c5e6b8eb4d2afc1ce75949c3b190f`.
- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`,
  coincidente con `docs/preregistration_002.md:7-12` (sin cambios desde el acta 047).
- `gh pr view 1` → PR #1 (`agent/phase2-b2-documentation` → `main`) `OPEN`, `DRAFT`; esta
  adjudicación no toca git.
- `ls docs/comite/` → el acta más alta existente es 047; el siguiente número es 048.
- Blob SHA del contrato adjudicado (`git rev-parse HEAD:research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md`)
  = `c7512a7f0bfb8757a5db2a78a20720bf0a8b882d`. Todo lo que sigue adjudica exactamente ese blob; una
  edición posterior del contrato re-escopa lo que G1–G9 calificaron aquí.
- Blob SHA del acta 047 (`git rev-parse HEAD:docs/comite/comite_decision_047_phase2-b2-documentation-publication.md`)
  = `ce0e08e76f33466489d7e110e81944cb95764e73`.
- El PDF primario de Müller (arXiv:2503.01719v2, "On the Hauptvermutung of Causal Set Theory")
  **existe localmente** en `biblioteca/2503.01719v2.pdf`, aunque no hay resumen en
  `biblioteca/derived-md/`. Fue leído directamente por el verificador de literatura y por el
  falsificador en esta sesión (ver §7, §5).
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`
  confirmado presente y legible; líneas clave: L201 (definición MOTS), L221-225 (\(\Theta_{\rm
  out}(r)=0\) en \(r=2M\) en Schwarzschild), L227 (el propio artículo, en su montaje 1+1D, **no
  tiene superficies espaciales de codimensión dos y no puede computar \(\Theta_\pm\)** — usa
  escaleras como proxy), L564-570 (\(\Theta_{\rm int}&lt;0\), \(\Theta_{\rm ext}&gt;0\)).
- Trabajo del día 2026-07-29 (fecha de la sesión).

## 3. Dossier

Fuentes principales suministradas al comité:

- `CLAUDE.md` (reglas fundacionales)
- `docs/preregistration.md`, `docs/preregistration_002.md`, `docs/preregistration_002_result.md`
- `docs/comite/comite_decision_047_phase2-b2-documentation-publication.md` (texto completo)
- `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md` (texto completo —
  el contrato bajo adjudicación)
- `research_program/bibliography/phase2_novelty_and_item5.md`
- `docs/manuscript_limits_draft.md`
- `formal/HorizonFormal/` (incl. `HorizonFormal/Horizon.lean`, el precedente
  `relationalHorizonOld_eq_empty`)
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`
  (Eichhorn–Gamito–Stokes, arXiv:2605.06813)
- `biblioteca/2503.01719v2.pdf` (Müller, fuente primaria — leída directamente esta sesión)
- `biblioteca/derived-md/The causal set approach to quantum gravity.md` (Surya)
- `biblioteca/derived-md/Discrete geometry of a small causal diamond.md` (Roy et al.)

Guardarraíles vigentes (contrato §11): `TARGET_ADOPTION=PENDING_SCIENTIFIC_ADJUDICATION`,
`WITNESS_CONSTRUCTION`/`CODE`/`SIMULATION`/`SEEDS`/`THRESHOLDS` todos `NOT_AUTHORIZED`,
`SEALED_PATH=UNTOUCHED`. Esta acta solo puede recomendar; no tiene autoridad para voltear ese
bloque.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): Exactly one documentary artefact — `docs/comite/comite_decision_048_<slug>.md` (048 is the correct next index: highest existing is `docs/comite/comite_decision_047_phase2-b2-documentation-publication.md`, per the chair's `ls` of `docs/comite/`). It must carry the 14 headings plus `### Mathematical logic brief` enforced by `.claude/skills/comite/check_comite_brief.py:15-33` and one `COMMITTEE_DECISION_VERDICT=` token from the four in `:36-42`. The contract's §8 deliverables (ficha Q, ten-line candidate proposition, g₀/g₁ table, TV chain, source ledger, falsifier attack, single §9 terminal — `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:225-240`) should live **inside** 048 as an appendix, not as a new `research_program/work_packages/phase3_b2_*.md` file: a standalone "ficha Q" file reads as an adopted target ficha and would misrepresent `TARGET_NOT_ADOPTED` (`contract:3-9`). **No edit to the contract file itself.** Flipping `TARGET_ADOPTION` at `contract:295` *is* the act of adoption and belongs to the PI, not to this brief (`contract:302` `COMMIT_OR_PUSH = NOT_AUTHORIZED_BY_THIS_DOCUMENT`).
- Environment & seal: No Python environment is exercised. The sealed contract `numpy==1.26.4` (`requirements.txt:7`) is enforced at runtime by `thresholds.assert_environment()` (`nachocausal/thresholds.py:21`), called **only** from `nachocausal/dry_run.py:19` and `nachocausal/validate.py:157` — neither entry point may be invoked, so `make dry-run` (`Makefile:11-12`) and `make test` (`Makefile:8-9`) are out of scope and irrelevant to a documentary act. `make gate` needs the external Minz clone (`Makefile:2-3`; `CLAUDE.md:26-29`, `~/cs-horizon-reuse-check/venv_minz`) and is likewise irrelevant. Re-verify the seal with `make verify-seal` (`Makefile:14-16`, pure `hashlib`, read-only) and require `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching `docs/preregistration_002.md:7-9` — once before drafting and once after, so 048 records a same-session before/after pair. Package-diff-clean: `git diff --name-only` and `git diff --cached --name-only` must show **zero** paths under `nachocausal/`, `tests/`, `scripts/`, `certifier/`, `results/`, `requirements*.txt`, `Makefile`; since the tree is verified clean (chair DOSSIER `git status --short` empty), the only expected delta is the one untracked 048 file. `make audit` (`Makefile:52-53` → `.claude/skills/auditor/audit.sh:58-69`) must stay green — it independently asserts the live seal SHA is recorded in a `docs/` freeze file.
- Provenance capture: 048 §2 must record: `HEAD=2a8851fd844f56387eda61efec2e4c6a26ab2d67`, branch `agent/phase2-b2-documentation`, `origin/main=29f84357ae7c5e6b8eb4d2afc1ce75949c3b190f`, PR #1 state OPEN+DRAFT, `git status --short` empty, `make verify-seal` output before/after, work date 2026-07-29, the chosen §9 terminal and the verdict token. **One extra item is load-bearing and currently missing from the DOSSIER:** the blob SHA of the adjudicated contract (`git rev-parse HEAD:research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md`). Without it a later edit to the contract silently re-scopes what G1–G9 were scored against. Deliberately **not** captured: `pip freeze`, `uname`, seed band, RNG state — no code runs, and inventing such fields would be provenance theatre. `SEEDS = NOT_AUTHORIZED` (`contract:299`); the frozen validation band `[2_000_000,2_999_999]` and its one-time blind draw stay untouched at `docs/preregistration_002.md:14-33`; this act burns nothing.
- Run mechanics: No run. The only permitted executions are read-only verifiers, all foreground and idempotent: `make verify-seal`, `make verify-comite`, `make audit`, and `git status/diff/rev-parse/log`. Reversible pre-flight = writing 048 as an **untracked** file (abort = delete it; tree returns to the verified-clean state with no git operation at all). Committing step = `git add docs/comite/comite_decision_048_*.md` + commit + push onto the open draft PR #1 — this is **not** authorized: decision 047's sign-off covers only its explicit 25-path manifest (`comite_decision_047:205-230,249-253`), and `contract:302` withholds commit/push. Adding 048 to PR #1 also mutates a branch already under review; prefer leaving 048 uncommitted pending a fresh, explicit PI sign-off rather than silently extending that PR. Clean abort triggers: seal SHA mismatch, `BRIEF_CHECK=FAIL`, any off-scope path in the diff, or any pressure to edit `contract:289-303`.
- Reproducibility risks / ambiguities:
  - **Correction to the DOSSIER, and it matters for G8.** The DOSSIER states no local Müller source exists; that is true only of `biblioteca/derived-md/` (no match for `muller|müller|hauptver`). The **primary PDF is present and readable**: `/home/ignac/nachocausal/biblioteca/2503.01719v2.pdf` (348057 bytes, ~10 pages). G8 demands a *literal* comparison with Müller Thm 2–3 (`contract:220`); it is therefore closable this session from primary text via a read-only PDF read, and a brief that instead recycles the secondhand numbers in `comite_decision_047:156` should mark them `[UNVERIFIED]`. Reading a PDF modifies nothing.
  - **No machine gate exists for B2 terminals.** `check_comite_brief.py` contains no `B2_` token (grep: zero hits); it validates headings, placeholders, verdict string and the BLOCK/PROCEED invariant only (`:15-90`). So `BRIEF_CHECK=PASS` on 048 is *not* evidence that the §9 terminal is well-formed or that its precedence order (`contract:246-255`) was respected. That must be checked by human reading; asserting otherwise would be a guardrail-that-cannot-fail.
  - **Nothing about G5/G6 is reproducible today, by design.** `Q_FMOTS` is a functional of the latent 3+1 completion, not of the observed poset (`contract:43-69`); no number, no artefact, no rerun attaches to target separation or the TV chain. Any attempt to "sanity-check" G5/G6 numerically would be a `SIMULATION = NOT_AUTHORIZED` violation (`contract:296-299`).
  - **No reusable environment exists for a future B2 step.** Every executable path in the repo is the finite 1+1 EF sealed instrument (`docs/preregistration_002.md:35-57`); `formal/HorizonFormal/` stops below the Lorentzian/sprinkling layer (`comite_decision_047:93,96`). A future authorized witness/numerics step would need its **own** dev pre-registration and its own env pin, and must follow the OP-2.1 precedent of living outside the canonical suite (`Makefile:26-34`: `op21-bench`/`op21-terminal` are deliberately excluded from `make test` so the sealed suite's semantics and runtime never change). It must never be run in the sealed venv or against `nachocausal/thresholds.py`.
  - **Terminology drift risk.** If 048 issues `B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION`, that authorizes proof work only (`contract:257-259`). A commit message or PR body reading "B2 opened" would over-claim; commit wording, if ever authorized, must retain `TARGET_NOT_ADOPTED` until the PI acts.
  - `[UNVERIFIED]` — I did not run `make verify-seal`, `make verify-comite`, or `make audit` in this session; the seal SHA above is the chair's pasted output, and the post-drafting seal re-check does not yet exist.

### Mathematician brief
- Computability: The B2 observation is the isomorphism class of an unlabeled finite **partial** order at fixed \(N=n\), not a total order (Surya §2, `biblioteca/derived-md/The causal set approach to quantum gravity.md:566-571`; contract `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:123-133`). Unlabeled posets on \(n\) elements form a **finite** set, so \(P_{i,n}\) is a law on a finite space with no measure-theoretic subtlety. **\(Q_{\mathrm{FMOTS}}\) does not need to be computable, or even measurable, as a function of \(g\)**: the two-point argument evaluates it at exactly two fixed metrics — a genuine well-posedness relief for a latent existence functional quantified over an infinite-dimensional surface class. What §4.1-4.2 silently requires and never states: measurability of the sample→poset map, i.e. the causal relation on \(U\times U\) is measurable; holds for continuous Lorentzian \(g\) on compact causally convex \(U\) but must be an explicit hypothesis of the regularity class `[UNVERIFIED for the exact class §3 will fix]`. estimator-v2's \(\tau(n)\)/`T_EDGE_MIN` gates are sealed-1+1-only and must not be imported; contract correctly declares `THRESHOLDS = NOT_APPLICABLE`.
- Order observable: By Hawking–Malament, causal structure fixes the metric up to a local conformal factor, recovered by counting (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:81-83`). For \(g_\omega=e^{2\omega}g_0\) the causal relation is **literally identical**, giving one common parameter-independent measurable map sample→poset, so the first §4.2 inequality is exact data processing. The residual channel reduces to a closed-form \(\mathrm{TV}(\mu_0,\mu_1)\) integral over \(\omega\). Corollaries: (a) exact \(\mathrm{TV}=0\iff\omega\) constant \(\Rightarrow\) homothety \(\Rightarrow\theta_\pm\) rescale by \(e^{-\omega}\), signs preserved, \(Q\) unchanged — **exact TV=0 is provably unavailable for a Q-separating conformal pair**, vindicating the \(\varepsilon_n\)-only claim with a reason; (b) the channel is blind exactly along the direction \(Q_{\mathrm{FMOTS}}\) lives in, which is why the target is well-matched to this route.
- Relevant invariants: ordering fraction, \(C_k\), longest chain, future cardinality — B2 must select **none** of them; a two-point bound at full-poset level dominates all by data processing, and picking an invariant would drift toward the forbidden C1-C6 localizer line.
- Analytic/continuum target, gate by gate:
  - **G1: achievable but not as currently written.** Normalization of \(\ell_\pm\) is the lesser problem (\(\{\theta_+=0,\theta_-&lt;0\}\) is invariant under \(\ell_\pm\mapsto f\ell_\pm\)). The real hazard is "exterior" — a compact \(U\) has no asymptotic end, so "outward" is not determined by \((g,U)\) alone. Two repairs: (i) drop orientation, use orientation-free "marginally future-trapped" form (both \(\theta_+&lt;0,\theta_-&lt;0\)) `[UNVERIFIED against biblioteca; standard MOTS theory]`; (ii) declare "outer" = side meeting \(\partial U\) (intrinsic but boundary-dependent, reopens falsifier attack 4). **Recommends (i).** Absent an explicit repair, `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL` is the correct reading.
  - **G3: passes by type** — image is \(\{0,1\}\), no `Min(C)`→region map. Attainable conclusion is a testing floor (risk\(\ge(1-\mathrm{TV})/2\)), not a localization rate — must never be narrated as a rate.
  - **G5: yes on existence half, unproved on the harder half.** Q(g0,U)=0 is a non-existence theorem over the whole \(S_{\rm adm}\) class — the genuinely hard half. Quantitative warning recorded pre-construction: MOTS condition and conformal correction both scale as 1/length; flipping the sign forces \(\|\omega\|_\infty=O(1)\); small TV must come entirely from small support volume, forcing \(\|\partial^2\omega\|\sim\rho^{-2}\sim(n/V)^{1/2}\to\infty\) as \(n\) grows — structural conformal scale-covariance `[UNVERIFIED heuristic, not proof]`.
  - **G8: substantive non-redundancy argument available, on secondhand evidence only** (no local derived-md for 2503.01719 at the time of this brief). Taking repo's own characterization at face value: Müller's geometries are flat slabs/cylinders; flat spacetime carries no closed marginally trapped surface, so \(Q_{\mathrm{FMOTS}}=0\) on both sides of every Müller pair. **[See §5 falsifier attack and §7 literature verdict: this claim is confirmed only for Theorem 3 and is false for Theorem 2, whose proof uses an arbitrary Cauchy slab and a small-support conformal perturbation — essentially the same mechanism B2 proposes.]**
- Caveats: measurability of causal relation must be explicit §3 hypothesis; exact TV=0 unattainable for Q-separating pair but converse must not be assumed (Hauptvermutung-type question); G1 fails only through "exterior"; non-existence half of G5 gets no help from conformal mechanism; \(Q\) is quasi-local to \(U\) (feature — makes \(Q\neq T_{EH}\) — but must be written into ficha); G8 could not be fully closed without reading the primary PDF.
- **Recommendation from this seat (advisory only):** `RECOMMEND_ADMISSIBLE_WITH_CONDITIONS` — support `B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION` only if (1) §2.1 amended to orientation-free form closing G1/G7 without external label, and (2) the \(\|\omega\|_\infty=O(1)\)/\(\rho^{-2}\) regularity scaling is pre-declared now. Failing (1), correct terminal is `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`. **Note: this recommendation's G8 premise was subsequently overturned by primary-source reading — see §5, §7.**

### Mathematical logic brief
- Formal status: \(Q_{\mathrm{FMOTS}}\) is a **definition schema, not a closed definition** — parametric in \(S_{\rm adm}\) (contract flags this itself, §2.2), plus a second free parameter: outward labelling and null-normal normalization (contract §2.1 refuses to inherit implicitly). Current object is really \(Q_{\mathrm{FMOTS}}[S_{\rm adm},\text{orientation},\text{normalisation}]\). Conformal family and TV chain are self-labelled proof routes, not proofs. **Zero mechanised (Lean) support** — the library deliberately stops below the Schwarzschild/sprinkling layer. **Directly relevant precedent from this repo's own Lean track:** a plausible relational-horizon definition was provably empty for every \(R\) in every preorder until its orientation was corrected (`formal/HorizonFormal/HorizonFormal/Horizon.lean:120-125`), accepted only once a non-emptiness witness was exhibited. The identical failure mode is open for \(Q_{\mathrm{FMOTS}}\): an orientation/quantifier slip in \(S_{\rm adm}\) can make the inner \(\exists S\) vacuous (\(Q\equiv0\)) or universal (\(Q\equiv1\)), making G5 unreachable by construction.
- Quantifier/dependency order: fix \(U\), orientation, \(S_{\rm adm}\)+normalization, \(k\)+regularity budget, boundary data, equivalence group, sampling channel, fixed-\(n\)/range — THEN \(g_0,g_1\), THEN prove separation, THEN TV bound. **The unblocked inversion created by adopting now:** with \(S_{\rm adm}\) still free at adoption time, the statement degenerates from "\(\forall S_{\rm adm}\text{-fixed}\ \exists(g_0,g_1)\)" to "\(\exists S_{\rm adm}\ \exists(g_0,g_1)\)" — i.e. the class may be chosen after seeing which pair separates. This is falsifier attack 1 ("etiqueta externa") re-entering through the quantifier prefix.
- Equivalence claims: TV chain is one-way data processing only, correctly stated. **G2 (\(Q\neq T_{EH}\)) is currently an asserted type distinction, not a proved separation** — but is provable conditionally: \(T_{EH}\) is proved non-measurable w.r.t. finite causally convex patch data by Theorem 3.2 (`docs/manuscript_limits_draft.md:455-483`), which doesn't prohibit quasi-local proxies. Separation reduces to a locality requirement on \(S_{\rm adm}\): if \(S_{\rm adm}(g,U)\) depends only on \(g|_U\), \(Q\) is a functional of \(g|_U\) while \(T_{EH}\) provably is not — Theorem 3.2's completion pair IS the witness. **So G2 collapses into G1, it is not independently blocking, and it stays conditional/inactionable until \(S_{\rm adm}\) is actually closed.** G3 passes by codomain typing; residual hazard is a constructive proof of \(\exists S\) carrying a witness surface that a downstream rule could extract, re-importing localisation (falsifier attack 8; the safeguard is not written into any gate).
- Type/object discipline: typing is clean where written. One gap: "intrinsic and diffeomorphism-invariant" is stated as a prohibition rather than the positive condition it must be — naturality/equivariance: \(\forall\varphi,\ S_{\rm adm}(\varphi^*g,U)=\varphi^{-1}(S_{\rm adm}(g,\varphi(U)))\). That form is checkable; the prohibition form is not.
- Caveats: \(S_{\rm adm}\) is the single load-bearing undischarged degree of freedom — G2 and G7 both reduce to it, so the adjudication has effectively one open question, not four. Adopting now with \(S_{\rm adm}\)/orientation/normalisation open creates a definitional post-hoc degree of freedom a later witness-pair choice could exploit. \(\theta_+=0,\theta_-&lt;0\) stated without its transformation law; any restatement is `[UNVERIFIED]`. Degenerate sub-case that must be stated explicitly: constant \(\omega\) gives exact TV=0 but plausibly leaves \(\theta_+\) zero-set invariant (G5 fails) — witness must be non-constant small-support \(\omega\), should be written into the proposition, not left implicit. Second redundancy risk beyond Müller: the project's OWN proved exact-equality dilation orbit (Theorem 3.1) — §5's redundancy terminal only covers Müller.
- **Recommendation from this seat:** \(Q_{\mathrm{FMOTS}}\) is **well-typed and admissible in form but not yet a closed definition**; recommend adoption ONLY if \(S_{\rm adm}\) is closed in-session in the equivariance form above, otherwise emit the typed block, `B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION` withheld. Adoption should additionally be conditioned on the repo's own Lean-track standard: exhibit \(\exists(g,U):Q=1\) AND \(\exists(g,U):Q=0\) before the class is used.

### Physicist brief
- Coordinates & patch: \(Q_{\mathrm{FMOTS}}\) must use **no coordinates at all** — its main physical virtue, and the point where the sealed positive and B2 must not be conflated. Sealed 1+1 positive lives in ingoing EF \((v,r)\) on a finite box with sealed `T_EDGE_MIN=6`; its finiteness forfeits any \(\mathscr I^+\)-defined event-horizon claim. \(Q_{\mathrm{FMOTS}}\) instead lives on a compact, causally convex 3+1 patch \(U\) with intrinsic \(S_{\rm adm}(g,U)\); nothing transfers from 1+1. Residual coordinate leak is not \((v,r)\) but the choice of "outer": \(\theta_+\) vs \(\theta_-\) is not intrinsic without a designated outward null normal, and in asymptotically flat GR "outer" is fixed by reference to infinity — which compact \(U\) lacks. Contract already routes this to `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL` (G1/G7); not yet closed. [Notes existence of orientation-symmetric fallback — closed trapped surface, \(\theta_+&lt;0\) AND \(\theta_-&lt;0\) — without endorsing a target substitution, which is the PI's act.]
- Physical meaning of the signal: two different mechanisms must be kept apart. Sealed 1+1 observable's signal is singularity truncation. **\(Q_{\mathrm{FMOTS}}\) has no discrete mechanism at all** — Boolean functional of latent continuum geometry, not an estimator on the poset. Its GR content is correct: Schwarzschild \(\Theta_{\rm in}=-2/r&lt;0\) everywhere, \(\Theta_{\rm out}=r^{-1}(1-2M/r)\) vanishes at \(r=2M\), MOTS locus = event/Killing horizon. Contract's \(\theta_+=0,\theta_-&lt;0\) is sharper than the source paper's own looser "apparent horizon=MOTS" prose and its refusal to inherit terminology/normalisation implicitly improves on the source.
- Sprinkling domain: B2's fixed-\(n\) conditioning **deliberately deletes the counting channel** — causal-set kinematics normally recovers the conformal factor by counting (\(V=n\cdot V_{\rm Planck}\)); by normalising \(\mu_i\) and conditioning on \(n\), B2 removes precisely that mechanism. This is a physics fact, not bookkeeping: if \(\mathrm{Vol}_{g_0}(U)\neq\mathrm{Vol}_{g_1}(U)\), a fixed-density Poisson ensemble would discriminate the pair through \(N\) alone, so the fixed-\(n\) conditioning is doing real work and must be declared. Permitted regime is only fixed-\(n\)/announced-finite-range with possibly \(n\)-dependent pair — no intensity/asymptotic guarantee on offer.
- Claim boundary: adopting \(Q_{\mathrm{FMOTS}}\) would claim only that a quasi-local, binary, diffeomorphism-invariant MOTS-existence functional on a compact 3+1 patch is a well-posed continuum target for a two-point argument at fixed \(n\). Would NOT claim MOTS reconstructibility, localisation, \(Q=T_{EH}\), anything asymptotic, or 1+1 transfer. Critically: **the 3+1 side has no empirical support in the causal-set literature to inherit** — EGS has no spatial two-surfaces in 1+1D and cannot compute \(\Theta_\pm\) at all; B2 must stand on continuum GR + probability alone, needs an explicit non-evidential-inheritance statement.
- Caveats: conformal route is physically the right knob (Hawking–Malament) — contract's "route not proof" honesty is adequate and endorsed. \(\theta_\pm\) conformal transformation law itself is not anchored in `biblioteca/` — `[UNVERIFIED from memory]`. **Independent dimensional-analysis finding (converges with mathematician's):** scaling tension between "flips \(\theta_+\)" and "small TV" forces amplitude \(a=O(1)\), TV smallness must come from shrinking support with \(|\partial\omega|\to\infty\) `[UNVERIFIED heuristic]`; the uniform regularity budget is therefore load-bearing, not a formality. Proving \(Q(g_0,U)=0\) is the physically hard half. Regular-black-hole caveat from decision 047 actually SUPPORTS \(Q_{\mathrm{FMOTS}}\) (θ± are local, need no singularity) — but must never be presented as the natural continuation of the sealed 1+1 positive. G9 risk is the inverse of the one named: danger is importing the sealed result's CREDIBILITY, not its ceiling — adoption should carry an explicit non-inheritance clause. Did not independently re-read the Müller PDF at brief-writing time; **subsequently done by the literature verifier and falsifier, see §5, §7.**
- **Physicist recommendation:** target is physically well-posed enough to merit formal adoption, conditional on closing (i) intrinsic outward-orientation/\(S_{\rm adm}\) (G1/G7), (ii) an anchored \(\theta_\pm\) conformal transformation law, (iii) an explicit uniform regularity budget with \(n\)-dependence and counting-channel forfeiture written into the claim ceiling (G4/G9). Advisory only; adoption is the PI's act.

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes:
  1. **The Wave-1 non-redundancy case for G8 is factually wrong on the primary source, verified page-by-page.** The mathematician's G8 argument ("Müller's geometries are flat slabs/cylinders; flat spacetime carries no closed marginally trapped surface, so \(Q_{\mathrm{FMOTS}}=0\) on both sides of every Müller pair") describes only Theorem 3 (`biblioteca/2503.01719v2.pdf` p.5: flat normalized cylinders). **Theorem 2's witness pair is NOT flat**: its proof reads, verbatim, "We modify the Lorentzian metric in a sufficiently thin neighborhood of \(c\) by a **conformal factor** \(u\)..." (`biblioteca/2503.01719v2.pdf` p.4). Müller's Theorem 2 mechanism is *literally* B2's proposed mechanism — a small-support conformal perturbation of an arbitrary (unit-volume, matched-boundary) Cauchy slab — and his channel (\(C_K(X)\), permutation-invariant order-law at fixed \(K\), \(\|C_K(X)-C_K(Y)\|_1&lt;\varepsilon\)) is *literally* B2's channel. The contract's §5 table row distinguishing "perturbación geométrica de soporte pequeño" (Müller) from "candidato conforme de soporte pequeño" (B2) manufactures a mechanism difference that does not exist. The only residual novelty is the *target* (binary MOTS existence vs. Lorentzian distance) plus the two-point minimax framing — which may survive as bounded instantiation, but `B2_REDUNDANT_WITH_MULLER` outranks `B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION` in §9 precedence and must be re-adjudicated against Theorem 2's actual mechanism, not against a flatness claim that is false for Theorem 2.
  2. **The "convergent G1 fix" is a target substitution, not a repair — and the two proposers do not even state the same object or the same lemma.** The mathematician's repair (i) is "marginally future-trapped (both \(\theta_+&lt;0\) and \(\theta_-&lt;0\))" — internally imprecise ("marginally" with two strict inequalities is a *trapped* surface, not marginal) and `[UNVERIFIED against biblioteca]`. The physicist's fallback is explicitly flagged as "a target substitution, which is the PI's act." Their load-bearing conformal transformation laws **contradict each other**: \(\tilde\theta_\pm=e^{-\omega}(\theta_\pm+2\ell_\pm\partial\omega)\) (mathematician) vs. \(\tilde\theta_\pm=e^{-2\omega}(\theta_\pm+2\ell_\pm\partial\omega)\) (physicist) — different conformal weights, both `[UNVERIFIED]`, neither anchored in `biblioteca`. Convergence of two heuristics is being mistaken for verification. A trapped-surface target also quietly changes the benchmark from horizon-locus to trapped-*region* detection.
  3. **The decision question conjoins two claims and only one is even arguably closable.** Admissibility of \(Q_{\mathrm{FMOTS}}\) is one thing; "existe una ruta no trivial" is another. The convergent scaling heuristic (\(\|\omega\|_\infty=O(1)\), \(\partial^2\omega\sim\rho^{-2}\sim(n/V)^{1/2}\to\infty\)) means a nontrivial testing floor at cardinality \(n\) needs \(\mathrm{TV}(\mu_0,\mu_1)\lesssim1/n\), hence support \(\sim V/n\), hence curvature growing like \(n^{1/2}\) — "fixed-\(n\)" relabels rather than evades this. If the heuristic stands, `B2_BLOCKED_REGULARITY_DEGENERATES` or the §10 clean-stop condition is the live terminal, not admissibility-plus-route.
  4. **G2 "closed by Theorem 3.2" is conditional on an object that does not exist yet.** The logician's collapse of G2 into G1 requires \(S_{\rm adm}(g,U)\) to depend only on \(g|_U\); Theorem 3.2 is a promise about the undefined \(S_{\rm adm}\). Reporting G2 as closed today would score a gate against a phantom.
- Ground-truth leakage: In B2 the latent completion \((g,U)\) plays the ground-truth role. The open \(S_{\rm adm}\)/orientation/normalization slot is the contract's own attack 1 ("etiqueta externa") left unlocked: with \(S_{\rm adm}\) free at adoption, the quantifier prefix degenerates to \(\exists S_{\rm adm}\ \exists(g_0,g_1)\) — the class can be chosen after seeing which pair separates. The mathematician's repair (ii) ("outer" = side meeting \(\partial U\)) re-imports a boundary label and reopens attack 4 by his own admission. Any adoption text that leaves \(S_{\rm adm}\) to be "closed later during witness construction" is a leakage channel with a governance stamp on it.
- Freeze violations: No sealed-path or seed violation is possible in this documentary act (seal verified at `6e2c3888...`). The freeze risk is **definitional**: adopting "Q_FMOTS as in §2.1 plus an unwritten orientation-free amendment" freezes nothing — the adjudicated definition and the adopted definition would differ. The only clean paths are recording the *complete closed definition verbatim inside decision 048* with the contract blob SHA, or emitting `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`. Failing to pre-declare the \(\rho^{-2}\) scaling obstruction now, then "discovering" an \(n\)-dependent regularity budget after a witness is in hand, is post-hoc tuning at the definitional layer.
- Verdict coercion: §9 contains **no** `ADMISSIBLE_WITH_CONDITIONS` terminal, and §7 says failing *any* gate blocks construction. Three advisory "admissible with conditions" recommendations must not be summed into `B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION` with the conditions demoted to caveats: conditions unmet = gate open = typed block. `B2_REDUNDANT_WITH_MULLER` sits immediately above ADMISSIBLE in precedence, and G8 (failure mode 1) is the gate Wave 1 closed on materially wrong secondhand evidence. Deferring G8 "to the witness phase" would be a silent coercion of an unresolved gate into PASS.
- Premature / over-broad claims: adoption must not imply route-existence; no regularity budget under which the route is non-degenerate has been exhibited. The attainable conclusion is a testing floor, never a localization rate. No credibility transfer from the sealed 1+1 positive; no "natural continuation" narrative; no 3+1 empirical inheritance. "Primer target formal" must not shade into "B2 opened" — the ADMISSIBLE terminal authorizes proof work only.
- Independent-falsification gate: **Not satisfied for the three load-bearing sub-claims.** (i) The orientation-free reformulation: proposed by mathematician and physicist, verified by neither, and they state inconsistent transformation laws — two proposers do not make one verifier. (ii) The scaling obstruction: two independent derivations, but both self-labelled heuristics; convergence is corroboration, not proof. (iii) G8: no Wave-1 seat read the primary PDF before writing; this falsifier brief performed the first primary-source read and it *overturns* the Wave-1 flatness characterization for Theorem 2.
- Minimal falsification test: Read-only, executable now: `pdftotext biblioteca/2503.01719v2.pdf - | grep -n -B2 -A3 "conformal factor"` → returns Müller's Theorem 2 proof sentence, confirming the conformal mechanism. **Pass condition for adoption:** any future G8 closure must quote this sentence and argue non-redundancy against *Theorem 2's* conformal mechanism explicitly (novelty resting on the target/minimax framing alone, stated as bounded instantiation); any G8 closure resting on "Müller's geometries are flat" is falsified on primary text. Secondary check: the adopted text must contain exactly one \(\theta_\pm\) transformation law with a named primary source, since the two Wave-1 candidate laws are mutually inconsistent and both unverified.

**Bottom line from this seat (recommendation only):** \(Q_{\mathrm{FMOTS}}\) *as written* fails G1
today; the "convergent fix" is an unadopted target substitution with contradictory supporting
lemmas; G8's Wave-1 closure argument is falsified on the primary PDF for Theorem 2; and the
route-existence conjunct is unestablished against a convergent-but-heuristic degeneracy
obstruction. Adoption is defensible only in the narrow form: closed definition frozen verbatim +
blob-SHA pin + G8 re-argued against Theorem 2's conformal mechanism + scaling obstruction
pre-declared + both Q=1/Q=0 witnesses exhibited before the class is used. Anything less is an
abstain being dressed as a PASS.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: PASS (narrow scope — this PASS covers only the coherence of running this documentary,
  recommend-only adjudication act; it is not a PASS on adopting the target)
- Freeze status: the gates G1-G9 and the §9 terminal list were fixed in writing before this session
  (`phase3_b2_witness_pair_preopening_contract.md:207-223,242-255`), authored under acta 047 prior
  to today's adjudication. No gate criterion is being written or reinterpreted post-hoc. The sealed
  numeric estimator freeze (`docs/preregistration_002.md`) is a separate, untouched track; B2
  correctly marks it `THRESHOLDS = NOT_APPLICABLE`.
- Seal integrity: `SEALED_PATH = UNTOUCHED`; `make verify-seal` → `6e2c3888...`, matching
  `docs/preregistration_002.md:7-9`. Nothing in this adjudication touches the sealed 1+1D estimator
  path.
- Seed discipline: `SEEDS = NOT_AUTHORIZED`; this is a documentary/mathematical governance act
  only — no dev pool or virgin validation band is touched or referenced.
- Reporting rule: contract §9 requires the session to land on exactly one of eight named
  terminals, in strict precedence order, reported alike whether it blocks or admits. **Binding
  requirement:** the terminal actually recorded must reflect the state of G1 honestly. Since
  neither Wave-1 mathematician nor logician found G1 (intrinsic exterior-orientation of
  \(S_{\rm adm}\)) closed as currently *written* in contract §2.1 — and no PI edit to that text has
  occurred in this read-only session — the faithful terminal per §9's own precedence list is
  `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`, not `B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION`,
  unless and until the PI amends §2.1.
- Forbidden moves present? One live risk, correctly self-flagged inside the dossier, not yet
  committed: **definitional post-hoc tuning.** Freezing "\(Q_{\mathrm{FMOTS}}\) is the target"
  while its own admission criterion (which surface class counts) is still open would let a later
  witness-pair construction retroactively pick the definition that makes separation work — the
  target-adoption analogue of loosening a threshold before its own gate closes. No forbidden move
  has actually occurred in the dossier itself: both mathematical Wave-1 seats correctly gate their
  support on this point being closed first. The hazard is procedural: rounding their *conditional*
  recommendations up to a plain "adopt" in this synthesis would itself be the forbidden move.
- Scope-authorization check: acta 047 §11 explicitly withholds authorization for adopting
  \(Q_{\mathrm{FMOTS}}\), witness construction, code, simulation, seeds, thresholds, sealed
  execution, or novelty/reconstruction language. This session, per the PI's explicit scope limit,
  stays inside that bound.
- Reasons:
  - Gates were pre-written before this adjudication; freeze discipline intact for the governance
    criteria in play (`comite_decision_047.md:245`).
  - Sealed numeric path unchanged and re-verified; B2 correctly marks thresholds not applicable.
  - No seeds, code, or simulation touched; virgin validation band untouched.
  - Both convergent mathematical Wave-1 seats find G1 currently open in the artifact as written,
    which under §9's precedence currently reads as `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`.
  - Adopting the target while G1 (into which G2/G7 collapse) is unresolved is structurally
    equivalent to loosening a threshold before its gate closes.
  - Acta 047's own sign-off bounds this session to recommend-only; treating conditional Wave-1
    recommendations as adoption would exceed that bound.

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Müller 2503.01719v2, Thm 2 (∀ε∈(0,1) ∀D>0 ∃X,Y unit-volume Cauchy slabs, \(d^-(X,Y)>D\), \(\|C_K(X)-C_K(Y)\|_1<\varepsilon\)) | Mathematician, Physicist (also decision_047, phase2_novelty_and_item5.md V8) | CONFIRMED — read primary PDF p.3-4 directly |
| Müller 2503.01719v2, Thm 3 (flat normalized cylinders \(C(T)\); \(E\ge1-4\pi K^2T^{-1/n}\)) | Mathematician, Physicist | CONFIRMED — read primary PDF p.5; statement explicitly restricted to flat geometries |
| "Müller's example geometries are flat slabs/cylinders" (premise of the G8 non-redundancy argument) | Mathematician | **UNCONFIRMED for Thm 2 / CONFIRMED for Thm 3 only** — see Notes |
| EGS, MOTS definition | derived-md L201 | CONFIRMED |
| EGS, \(\Theta_{\rm out}(r)=0\) at \(r=2M\) Schwarzschild | derived-md L221-227 | CONFIRMED |
| EGS, "no spatial two-surfaces… cannot compute the expansions" in 1+1D | derived-md L227 | CONFIRMED |
| EGS, regular-black-hole robustness of apparent-horizon concept | derived-md L199, L467 | CONFIRMED |
| Surya, Myrheim-Meyer ordering fraction | background | CONFIRMED |
| Roy et al., \(k\)-chain label invariance | background | CONFIRMED |
| `manuscript_limits_draft.md` Thm 3.2 (\(T_{EH}\) not measurable on finite causally convex patch) | Mathematical logician | CONFIRMED — lines 455-489 |
| `Horizon.lean:120-125`, `relationalHorizonOld_eq_empty` tombstone | Mathematical logician | CONFIRMED — lines 100-139 |

- Notes: The load-bearing correction for Gate G8: Müller's Theorem 2 proof begins with an
  **arbitrary Cauchy slab** \(X\) — no flatness assumed or used in the statement or proof; \(Y\) is
  obtained only by a local conformal perturbation in a thin neighborhood of a maximizing curve.
  The "all \(C_S\) are flat" language appears **only** in Theorem 3. Consequently the mathematician's
  G8 non-redundancy argument is secure only against Theorem 3's pairs; against Theorem 2's pairs it
  is not automatically true, since \(X\) can be a genuine black-hole patch supporting a MOTS. The
  θ±-conformal-transformation-law claims used by mathematician/physicist remain genuinely
  UNVERIFIED — no `biblioteca` source states it explicitly; their own `[UNVERIFIED]` tags stand and
  should not be upgraded.

## 8. Synthesis

**Consenso.** Los siete roles convergen en un único punto de bloqueo cargante: la clase de
superficies admisibles \(S_{\rm adm}(g,U)\) y su orientación "exterior" (§2.1-2.2 del contrato) no
están cerradas como intrínsecas y difeomorfismo-invariantes. El matemático y el lógico formal
llegaron, sin verse, a la misma conclusión — que este es el único gate realmente cargante, del que
G2 y G7 son corolarios — y el matemático y el físico propusieron, también sin verse, la misma
familia de reparación (forma libre de orientación tipo "marginally future-trapped"). El
falsificador correctamente advierte que esta convergencia es corroboración heurística, no
verificación: las dos leyes de transformación conforme de \(\theta_\pm\) que sostienen esa
reparación son **mutuamente inconsistentes** (\(e^{-\omega}\) vs \(e^{-2\omega}\)) y ninguna está
anclada en `biblioteca/`.

**Hallazgo que cambia el estado del acta.** El verificador de literatura leyó por primera vez el
PDF primario de Müller (`biblioteca/2503.01719v2.pdf`, disponible localmente aunque sin resumen en
`derived-md/`) y encontró que el argumento de no-redundancia de G8 usado en Wave 1 — "las
geometrías de Müller son planas, por tanto no admiten MOTS, por tanto Müller no puede separar este
target" — es **correcto solo para el Teorema 3** y **falso para el Teorema 2**, cuyo mecanismo
(perturbación conforme de soporte pequeño sobre un slab de Cauchy arbitrario, canal de leyes de
orden a \(K\) fija) es esencialmente idéntico al mecanismo que B2 propone. El falsificador
confirmó independientemente esta lectura. Esto reabre `B2_REDUNDANT_WITH_MULLER` como pregunta
activa, no cerrada, y ese terminal antecede en precedencia a la admisión.

**Segundo hallazgo convergente.** El matemático y el físico, de forma independiente, derivaron el
mismo argumento de escala heurístico: forzar el cambio de signo de \(\theta_+\) requiere amplitud
\(\|\omega\|_\infty=O(1)\) (no arbitrariamente pequeña), de modo que la cercanía TV solo puede venir
de encoger el soporte, lo que hace crecer la curvatura como \(\sim\sqrt n\). Ninguno lo prueba; ambos
lo marcan `[UNVERIFIED]`. Es una advertencia estructural pre-declarada, no un resultado, y determina
que el único régimen honesto es `FIXED_n_OR_ANNOUNCED_FINITE_n_RANGE` con degradación de
regularidad explícita — nunca una familia uniforme en \(n\).

**Caveats vinculantes.**

- Ninguna de las tres recomendaciones "ADMISIBLE CON CONDICIONES" de Wave 1 puede redondearse a una
  adopción llana: el contrato §9 no tiene terminal intermedio, y condiciones no cumplidas equivalen
  a gate abierto.
- El custodio de prerregistro y el falsificador coinciden: el terminal fiel, tal como está escrito
  hoy el contrato, es `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL` — no
  `B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION`.
- Adoptar el target ahora, con \(S_{\rm adm}\)/orientación/normalización abiertas, crearía
  exactamente el grado de libertad post-hoc que el propio contrato tipifica como ataque 1
  ("etiqueta externa").
- G8 debe re-adjudicarse explícitamente contra el mecanismo del Teorema 2 de Müller (no contra el
  Teorema 3) antes de que pueda cerrarse.
- Nada de esto refuta la idea de B2 en general: los siete roles coinciden en que el objeto es
  **matemática y físicamente razonable** y que el camino conforme es la elección correcta — el
  bloqueo es de cierre definicional y de comparación con literatura, no de viabilidad conceptual.

**Desacuerdos abiertos.** Ninguno sobre el fondo: los siete roles concuerdan en que hoy no
corresponde emitir `B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION`. La única diferencia de énfasis
es táctica — el matemático y el físico ven la reparación de orientación como "casi cerrada" (falta
solo anclar una fuente primaria), mientras el lógico y el falsificador la ven como una sustitución
de target no verificada. No es una contradicción: ambos leen el mismo hecho (dos leyes de
transformación conflictivas, ninguna anclada) con distinto optimismo sobre cuánto trabajo falta.

## 9. Next-step spec

### Reversible / verificación — ya completado en esta sesión

1. Verificar sello (`make verify-seal`), estado de git y del PR #1, blob SHA del contrato
   adjudicado.
2. Leer el contrato de preapertura y el acta 047 completos.
3. Obtener revisión independiente de siete roles (dos oleadas) y registrar los desacuerdos.
4. Leer el PDF primario de Müller y confirmar/corregir las citas de segunda mano.

### Pendiente antes de poder re-adjudicar `ADOPT` — trabajo documental/matemático, sin código

Ninguno de estos pasos requiere par testigo, código, simulación ni semillas; son cierre
definicional y de literatura, dentro del alcance que el PI ya autorizó explorar:

1. Cerrar \(S_{\rm adm}(g,U)\) con una única definición intrínseca y verificada — o bien derivar
   /anclar a fuente primaria la ley de transformación conforme correcta de \(\theta_\pm\) y elegir
   **una** convención (no dos conflictivas), o adoptar explícitamente la forma libre de orientación
   ("trapped surface", \(\theta_+&lt;0\) y \(\theta_-&lt;0\)) como una **sustitución de target**
   reconocida como tal, con su propio recorrido de G1-G9.
2. Re-argumentar G8 específicamente contra el mecanismo del Teorema 2 de Müller (perturbación
   conforme sobre slab de Cauchy arbitrario), no contra el Teorema 3; declarar honestamente si B2
   sobrevive como instanciación acotada o si dispara `B2_REDUNDANT_WITH_MULLER`.
3. Pre-declarar la degradación de regularidad (\(\rho\to0\), amplitud \(O(1)\), curvatura
   \(\sim\sqrt n\)) explícitamente en el techo de reclamo (G4/G9), en vez de descubrirla después de
   construir un testigo.
4. No tratar G2 como cerrado hasta que \(S_{\rm adm}\) esté cerrado (es condicional, colapsa en G1).
5. Exhibir — o justificar explícitamente por qué se difiere — un ejemplo con \(Q=1\) y otro con
   \(Q=0\), siguiendo el propio estándar de no-vacuidad de la pista Lean del repositorio, antes de
   tratar la clase como utilizable.

### Falsificador mínimo (ya ejecutado, para que conste)

`pdftotext biblioteca/2503.01719v2.pdf - | grep -n -B2 -A3 "conformal factor"` — confirma el
mecanismo conforme del Teorema 2 de Müller; cualquier cierre futuro de G8 debe citar esta frase y
argumentar contra ella explícitamente.

### Committing / outward-facing

Ninguno. Esta acta no autoriza, ni recomienda, ningún commit, push, edición del contrato, ni la
construcción del par testigo. `TARGET_ADOPTION` permanece `PENDING_SCIENTIFIC_ADJUDICATION` en el
contrato hasta que el PI decida.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

_(left blank for the user — decision, date, and any overriding notes)_
