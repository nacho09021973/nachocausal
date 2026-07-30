# Comité Decision 049 — Adjudicación de la nota de cierre del programa `nachocausal`

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Decisión de frontera: cierre formal del programa `nachocausal`. El PI redactó una "Nota de cierre
del programa nachocausal" (`ESTADO: PROGRAM_CLOSED / REPOSITORY_ARCHIVE_RECOMMENDED /
NO_FURTHER_RESEARCH_AUTHORIZED / NO_PUBLIC_NOVELTY_CLAIM / PRESERVE_AS_SCIENTIFIC_RECORD`, fecha 30
jul 2026) y pidió explícitamente que el comité decidiera si se firma ese cierre ("que sea el
comité quien decida el funeral"). Texto completo de la nota (verbatim, tal como se entregó al
comité):

> # Nota de cierre del programa `nachocausal`
>
> **ESTADO: PROGRAM_CLOSED / REPOSITORY_ARCHIVE_RECOMMENDED / NO_FURTHER_RESEARCH_AUTHORIZED /
> NO_PUBLIC_NOVELTY_CLAIM / PRESERVE_AS_SCIENTIFIC_RECORD.**
>
> Fecha: 30 de julio de 2026.
>
> ## Decisión
>
> Se cierra el programa activo de investigación de `nachocausal`. La pregunta que motivó el
> repositorio era si la información causal *order-only* de un conjunto causal finito podía
> sostener una reconstrucción o localización físicamente significativa de estructura de horizonte
> de Schwarzschild, con vocación de transferencia a 3+1 dimensiones. El trabajo realizado no ha
> establecido ese resultado. Tampoco ha establecido una contribución central que sea, a la vez,
> suficientemente original, físicamente útil y proporcionada al esfuerzo necesario para continuar
> el programa.
>
> ## Balance científico
>
> El repositorio contiene matemática correcta e internamente auditada, resultados negativos y
> experimentos reproducibles dentro de sus contratos: cegueras exactas del canal condicionado,
> límites de recuperabilidad, obstrucciones a ciertas definiciones globales y una validación
> acotada en un modelo Schwarzschild 1+1. Eso no equivale a haber reconstruido un horizonte, ni a
> disponer de un observable útil para 3+1, ni a haber certificado una colección de resultados
> novedosos frente a la literatura: el lema de amplificación estadística independiente de la
> dimensión es una especialización reutilizable de maquinaria estándar; la separación mediante
> fracción de orden en la familia concreta es débil, asintótica y condicionada a parámetros y a un
> régimen small-lapse no certificado numéricamente; los terminales C1–C6 documentan el fracaso de
> una clase de candidatos, no un no-go universal; el resultado positivo 1+1 localiza una frontera
> asociada al horizonte dentro de un parche controlado y no transfiere por sí mismo a 3+1; el
> horizonte de eventos global no es un funcional de un parche finito y la escala absoluta es
> invisible en el canal fixed-n estudiado. La conclusión honesta: "El objetivo fuerte del programa
> no se alcanzó, y los resultados supervivientes no justifican seguir ampliando el repositorio en
> busca de una contribución que rescate retrospectivamente ese objetivo."
>
> ## Alcance del cierre
>
> 1. no se abren nuevos observables, work packages, simulaciones, auditorías de rescate ni
>    reformulaciones del target dentro de este programa; 2. no se reclama novedad pública para los
>    resultados cuya prioridad no fue certificada; 3. los manuscritos y notas existentes se
>    conservan como registro de lo probado, lo refutado y lo que quedó abierto; 4. no se alteran
>    resultados sellados, terminales, pruebas ni historial; 5. tras registrar y sincronizar este
>    cierre, se recomienda archivar el repositorio en modo de solo lectura.
>
> ## Resumen público
>
> `nachocausal` estudió qué puede recuperarse de la geometría de Schwarzschild a partir de orden
> causal finito sin coordenadas. Produjo resultados acotados de identificabilidad y
> no-identificabilidad, pero no obtuvo una reconstrucción de horizonte 3+1 ni una contribución
> central de utilidad física suficiente. El programa queda cerrado y el repositorio se conserva
> como registro reproducible de ese resultado.

## 2. Verified state

Hechos comprobados en esta sesión, con su comando/ruta:

- `git status --short` → vacío (árbol de trabajo limpio).
- `git rev-parse HEAD` = `be958b6c7d25bf0ae617d0cac3c99bd39f09666b`, rama
  `agent/phase3-b2-decision-048`, 1 commit por delante de `origin/agent/phase3-b2-decision-048`.
- `git rev-list --count main..HEAD` = 16 (rama de trabajo 16 commits por delante de `main`); ramas
  no fusionadas adicionales: `origin/formula` (+2), `origin/agent/phase2-b2-documentation` (+1).
- `git tag | wc -l` = 0 — el repositorio no tiene ninguna etiqueta.
- `make verify-seal` → `thresholds.py sha256:
  6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` — coincide con
  `docs/preregistration_002.md:8` y `docs/estimator_v2_seal.md:7-9`. Intacto, sin cambios.
- `ls docs/comite/` → la más alta preexistente es `comite_decision_048_q-fmots-target-adjudication.md`;
  este documento es correctamente `049`.
- Producido y comiteado en esta misma sesión (cadena `192abf2..be958b6`):
  `docs/hoja_de_ruta_30_jul_2026.md`;
  `research_program/bibliography/wp4_dimension_free_order_statistic_priority_audit.md`
  (`PRIORITY_GATE=PRECURSOR_ONLY`, `STANDARD_COROLLARY`, sin reclamo de novedad);
  `research_program/bibliography/wp4_dimension_free_order_statistic_separation.md` (recalibrado);
  `research_program/bibliography/c6_theorem39_priority_audit.md`
  (`NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH / PRIORITY_NOT_YET_CERTIFIED`; hueco de grafos
  geométricos/modelos latentes declarado abierto, no agotado); `dev/explore_p_tau_shape.py`
  (verificación numérica independiente, reutiliza funciones ya auditadas).
- Esa verificación numérica dio, para el diamante concreto `r_p=3.0, r_q=0.5`, `dv=0.05`, `τ∈[0.62,1.8]`:
  `Δp` observado ≈ 1.554×10⁻³; `Δp` de la cota inferior demostrada ≈ 8.849×10⁻⁴; por bisección
  exacta sobre la fórmula literal del Teorema 3.9(2), `n≈6,629,533` (hueco observado) / `n≈20,431,728`
  (cota probada) para `TV≥0.5`. **Advertencia de la oleada 1 (mayoritaria):** estas cifras son la
  inversión de una cota de Chebyshev de **peor caso** (usa `ζ₁,ζ₂≤1/4`); el propio proyecto probó
  `ζ₁=1/36+O(dv²)` (`wp4_comparable_pair_separation.md` Thm C9), lo que reduciría el `n` requerido en
  un factor ≈9 por el mismo argumento, y una escala tipo CLT lo situaría en el mismo orden que el
  `N≈12000` de la corrida sellada §4. Esa corrección **no se ejecutó** en esta sesión —
  `[UNVERIFIED]` como salida de código— pero la dirección del argumento es robusta. **No debe
  usarse la cifra de millones como prueba de futilidad física sin esta salvedad.**
- `docs/manuscript_limits_draft.md` §7.2: `ABANDONED_AS_PROGRAM_NORTH` ya cierra, como acto de
  gobernanza, los localizadores de región 3+1D order-only (justificado por Thm 3.1–3.2 + no
  transferencia + el ledger). §7.3 lista como `OPEN`: B2 (pares adversariales, "preferred scientific
  sequel", línea 1179), B1 (order+number, separación de masa, línea 1178), la auditoría de
  prioridad de Thm 3.9 (residual bibliográfico) y la constante de escala crítica / `dv₀` certificado.
  §8: "Further scientific work, if any, should open a new contract (order+number; non-horizon
  targets; adversarial pairs...)".
- Rama viva sin adjudicar, no nombrada en la nota de cierre:
  `research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md` (commit
  `b48d98f`), cabecera `TARGET_NOT_ADOPTED / ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION`. Sucede
  al v1 (`phase3_b2_witness_pair_preopening_contract.md`, terminal
  `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`, emitido por `phase3_b2_qfmots_terminal_decision.md`,
  una decisión de director bajo delegación del PI, **no** un acta de comité). El acta previa
  `comite_decision_048_q-fmots-target-adjudication.md:318` dio veredicto
  `RECOMMEND_REVISE_AND_RECONVENE` sobre el target *predecesor*; la mitad "revise" se ejecutó
  (se redactó v2), la mitad "reconvene" nunca se ejecutó.
- `README.md` (líneas ~17–33): prioridad en 3 niveles — (1) Schwarzschild 3+1D order-only es "the
  destination of this program, not an optional extension"; (2) 1+1D es "structural foundation...
  1+1D does **not** resolve 3+1D"; (3) "close verifiable units before expanding scope."
- Precedente: `comite_decision_046` cerró la rama de *localizadores de región* (C1–C6 + Page–Shoom,
  7 fracasos) vía proceso de comité completo — más estrecho en alcance que un cierre de programa
  completo.
- `research_program/bibliography/phase2_novelty_and_item5.md`: lectores externos Tier A/B
  (2026-07-28) adjudicaron Thm 3.8 con `NOVELTY_CERTIFIED = NO`; `ITEM_5_DISCHARGED = YES`.

## 3. Dossier

Ficheros y referencias suministrados al comité:

- `docs/manuscript_limits_draft.md` (§1–§8, en particular §3.3 Thm 3.8–3.10, §7 cerrado/abierto/
  abandonado, §8 conclusiones).
- `research_program/bibliography/c6_theorem39_priority_audit.md` y
  `wp4_dimension_free_order_statistic_priority_audit.md`.
- `research_program/work_packages/wp4_comparable_pair_separation.md` y `_checks.py`.
- `dev/explore_p_tau_shape.py`.
- `research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md`,
  `phase3_b2_witness_pair_preopening_contract.md`, `phase3_b2_qfmots_terminal_decision.md`.
- `docs/comite/comite_decision_048_q-fmots-target-adjudication.md`,
  `docs/comite/comite_decision_046_weyl-level-sheet-page-shoom-adjudication.md`.
- `docs/preregistration.md`, `docs/preregistration_001_addendum.md`, `docs/preregistration_002.md`
  y su resultado, `docs/estimator_v2_seal.md`.
- `README.md`, `CLAUDE.md`.
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`
  (Eichhorn–Gamito–Stokes, arXiv:2605.06813 en la nomenclatura del proyecto).
- `biblioteca/derived-md/The causal set approach to quantum gravity.md` (Surya, LRR 2019).
- `biblioteca/derived-md/Bombelli_1987_PhD.md`.
- `biblioteca/Discrete geometry of a small causal diamond.pdf` (Roy–Sinha–Surya, arXiv:1212.0631).

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):**
  1. `docs/comite/comite_decision_049_program-closure-adjudication.md` — the acta of this committee, which is the only artefact that makes the closure *adjudicated* rather than declared. It must satisfy the machine gate `.claude/skills/comite/check_comite_brief.py` (14 required headings + `### Mathematical logic brief` for n≥009, no unfilled double-brace template residue, one `COMMITTEE_DECISION_VERDICT=` line from the 4-value vocabulary at `check_comite_brief.py:37-45`), verified by `make verify-comite` (`Makefile`, target `verify-comite`, which propagates non-zero by design).
  2. The PI note itself, filed under the existing closure precedent naming, e.g. `docs/program_closure_note_2026-07-30.md`, and — per that precedent (`docs/rvar_closure_negative_result.md:11-25`, "## Status token") — carrying its status as a **typed token block**, not only as prose in a blockquote. The current draft's `ESTADO:` line is prose; the R-VAR closure and the B2 terminal (`research_program/work_packages/phase3_b2_qfmots_terminal_decision.md:3-5`) both use typed, greppable tokens. Provenance-wise this matters: a future reader (or `git grep`) must be able to recover the closure state mechanically.
  3. Optionally a final integrity pass `docs/auditor/auditor_report_031_program-closure-precommit.md` (numbering after `docs/auditor/auditor_report_030_...`), gated by `make verify-audit` / `make audit`.
  4. An **annotated git tag** on the final commit. `git tag | wc -l` → `0`: this repository currently has **no tags at all**. Archiving read-only without a tag leaves the "final state" identified only by a branch head, which is a weaker pointer than the project's own standards elsewhere.

- **Environment & seal:** the closure act touches **no** sealed code path, so the sealed environment is only a *witness*, not a dependency. Re-verify and record, pre- and post-commit:
  - `make verify-seal` → must print `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, the frozen prereg-002 value at `docs/preregistration_002.md:8`; the instrument seal beneath it is `2f4c4a99…` (`docs/estimator_v2_seal.md:7-9`, commit `22b7660`). The DOSSIER records this match this session — seal **intact and untouched**, consistent with closure clause 4 ("no se alteran resultados sellados").
  - Sealed env is pure `numpy==1.26.4`, hard-pinned in `requirements.txt` with `thresholds.assert_environment` (`nachocausal/thresholds.py:21`) hard-failing on any other version. The GPU/dev stack (`requirements-gpu.txt`, CuPy + numpy 2.x) is explicitly a *separate* venv and never bit-identical to the sealed CPU instrument.
  - Package-diff-clean: `git status --short` → empty (DOSSIER), i.e. no `M nachocausal/`. The invariant the closure must record is exactly the one prereg-003 drafts already use: seal equal before and after, **no modification under `nachocausal/`** (`docs/preregistration_003_draft.md:158`).
  - The external Minz clone + `~/cs-horizon-reuse-check/venv_minz` (`CLAUDE.md:29`) is **not on the closure path** — no numerical run is proposed. Its evidence is already frozen in `nachocausal/fixtures/gate_evidence.json`, so archiving does not orphan the gate claim.

- **Provenance capture:** the closure note / acta must record, as literal command output:
  - commit `be958b6c7d25bf0ae617d0cac3c99bd39f09666b`, branch `agent/phase3-b2-decision-048`, `git status --short` empty;
  - `make verify-seal` output verbatim (pre and post);
  - `python -c "import numpy,sys; print(numpy.__version__, sys.version)"` + `pip freeze` of the sealed venv, and `uname -a` — the closure is the last moment at which the environment that produced every number is still live and interrogable; after archiving it cannot be re-captured from the repo;
  - `make test` / `make verify-comite` / `make verify-audit` / `make audit` exit statuses (read-only, non-committing);
  - **seed band, stated as unspent**: the reserved virgin band `[2_000_000, 2_999_999]` (`docs/estimator_v2_seal.md:56-57`). A closure record must state that no seed was drawn in this session and that the band is left **UNBURNED**. This is the provenance fact that makes the closure honest rather than merely final: nothing was spent to reach it.
  - timestamps: session date 2026-07-30 and the committer dates of the closure commits.
  - I did **not** execute `make test`, `make audit` or `make verify-comite` (read-only mandate); their current pass/fail state is `[UNVERIFIED]` and must be captured by the chair before the committing step.

- **Run mechanics:** a single foreground documentary session; no background jobs, no code execution, no seeds, no MC. Clean sequence with the abort points a guard can actually use:
  - **Reversible pre-flight** (all abortable with zero trace): read-only verification (`git status`, `make verify-seal`, `make test`, `make audit`), drafting the acta and the closure note in the working tree *uncommitted*, then `python .claude/skills/comite/check_comite_brief.py docs/comite/comite_decision_049_*.md`. Any non-zero exit → stop, fix, re-run; nothing has been committed.
  - **Committing step** — and here the layering matters, because these are *not* equally reversible:
    1. `git commit` of acta + closure note — appended history, revertible by a further commit;
    2. merge into `main` + `git push` — publishes; revertible only by revert-commit, i.e. the record of having closed is permanent;
    3. `git tag -a` on the final commit — the intended immutable pointer;
    4. **GitHub archive toggle** — the only *administrative* act; it is technically un-archivable, but it is the point after which no guard, gate or `make` target in this repo can run in CI or accept a push. It must be strictly last, after (1)–(3), and after every provenance capture above, because post-archive you cannot add the forgotten `pip freeze`.
  - Abort semantics: the Makefile deliberately carries no `|| true` on the integrity targets (`Makefile`, comment above `audit:`), so a failing gate genuinely blocks. Recommended hard aborts: seal SHA ≠ `6e2c3888…`; `git status --short` non-empty outside the two closure artefacts; `verify-comite` FAIL; any diff under `nachocausal/`.

- **Reproducibility risks / ambiguities:**
  - **The default branch does not contain the record.** `git rev-list --count main..HEAD` → **16**; `main` is 16 commits behind the closure head, and `origin/formula` (2 ahead of `main`) and `origin/agent/phase2-b2-documentation` (1 ahead) are also unmerged. Archiving now freezes a default branch that lacks today's priority audits, the C6 work and the closure note itself. The closure note's own clause 5 ("tras registrar y **sincronizar** este cierre") is therefore not yet satisfiable: signing must be conditioned on merge-to-`main` + push of all three branches (or an explicit typed disposition abandoning the two side branches).
  - **No immutable final pointer exists.** `git tag | wc -l` → `0`. Recommend an annotated tag (e.g. `program-closed-2026-07-30`) recording seal SHA + HEAD in its message, created before the archive toggle.
  - **Half the reproduction surface is git-ignored.** `.gitignore` excludes `results/`, `dev_ensemble_raw/`, `biblioteca/` and `email/`. Post-archive, every published number must be regenerable from committed scripts + fixtures alone; `results/` is ignored while "the committed verdict record lives in `docs/`" (`.gitignore` comment). This is by design, but the closure note should state it explicitly so a future reader does not mistake absent raw data for lost data.
  - **External, non-vendored dependency.** The Minz admissibility gate depends on the third-party clone `github.com/c-minz/Python-causets` (`requirements.txt` note; `CLAUDE.md:29`). After archiving we control neither its availability nor its content; mitigation is that `nachocausal/fixtures/gate_evidence.json` is committed. The Lean track pins its toolchain in `formal/HorizonFormal/lean-toolchain` / `lake-manifest.json`; whether `lake build` currently succeeds is `[UNVERIFIED]` — worth capturing before archive, since it is unrecoverable afterwards.
  - **Verdict-vocabulary mismatch.** `check_comite_brief.py:37-45` admits only `RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`, `RECOMMEND_PROCEED_WITH_CAVEATS`, `RECOMMEND_REVISE_AND_RECONVENE`, `RECOMMEND_DO_NOT_PROCEED`. None of these names "close the program". Whichever is used, the acta must define in-text what the token means for a closure act, or `make verify-comite` will pass a brief whose verdict string is semantically ambiguous to a future reader — a decoration-grade guardrail in exactly the sense `CLAUDE.md` forbids.
  - **A live, unadjudicated contract would be archived mid-flight.** `research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md` carries `TARGET_NOT_ADOPTED / ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION`, and `docs/manuscript_limits_draft.md` §7.3 lists the Fase 3 B2 adversarial-pair sequel as legitimately OPEN. The closure note names neither. Provenance-wise, archiving leaves a document in the tree whose own contract demands an act the closure forbids: irreconcilable for any future reader. A clean closure must emit an explicit typed disposition for Q_trap v2 (e.g. `CLOSED_UNADJUDICATED`), not silence — this is a documentary requirement, not a request to reopen the work.
  - The closure changes no threshold, burns no seed, touches no sealed byte: `RESPECT_SEAL_FREEZE`, `NO_THRESHOLD_LOOSENING`, `NO_POST_HOC_TUNING` and `NO_GROUND_TRUTH_LEAKAGE` are not at risk from the act itself. The reproducibility risk is entirely one of **completeness of the record at the moment of freezing**, not of integrity.

### Mathematician brief

- **Computability:** Everything the program actually ran is decidable in polynomial time from the order relation alone, on a **finite partial order** (irreflexive, transitive, locally finite — no total order anywhere; the observable is defined on antichain-rich sprinkled posets). (i) The sealed estimator-v2 observable is `O(i)=|future(i)|` = column sum of the boolean past matrix over minimal elements, `nachocausal/estimator.py:113-131` — O(n²), permutation-invariant, provably order-only ("the only input is an N×N boolean order matrix… no coordinate array in scope", `estimator.py:43-44`). (ii) The retained height oracle `estimate_O` is single-source longest path by topological DP on the DAG, `estimator.py:26-44` — polynomial on a DAG, and the audited poset-integrity anchor. (iii) The **τ(n) abstaining gate** is data-independent by construction: `abstains(improvement, n) ⇔ improvement < τ(n)`, `nachocausal/gate.py:53-57`, with τ(n) read from a frozen uniform-null MC table (α=0.01→p99, seed 20260621, 40000 reps, n=2..128, `docs/estimator_v2_seal.md:19-22`); `n<2 ⇒ abstain` (a 2-partition is undefined). (iv) The **domain gate** `t_edge<6 ⇒ OUT_OF_DOMAIN` is a config precondition, "never a physical FAIL" (`docs/estimator_v2_seal.md:24`, `docs/preregistration_002.md:48,57`). Both gates are order-/config-level and touch no embedding — the `NO_GROUND_TRUTH_LEAKAGE` requirement holds at the level of the code, not merely of the prose. Seal `6e2c3888…` verified untouched per DOSSIER. **Important scoping point for the closure question:** the B2 target `Q_trap` is *not* a computability question at all — it is a functional of the latent geometry \((g,U)\), and B2 asks only for a two-point **TV lower bound** (a testing floor), never for a poset algorithm (`phase3_b2_trapped_surface_preopening_contract.md:145-152`, §4). So "C1–C6 failed to compute a locator" is logically disjoint from "no witness pair exists", and cannot be used to close the latter.

- **Order observable:** Two, and they must not be conflated. (1) *Sealed / empirical:* truncated future volume \(|\mathrm{fut}(i)|\) on minimal elements — the finite-n, coordinate-free stand-in for the Eichhorn–Gamito–Stokes longest-chain-from-minimal-elements diagnostic, whose horizon signal is stated there explicitly: "For minimal elements inside the horizon, the length of the longest chain is limited, because each timelike curve inside the horizon must reach r=0 within a finite amount of proper time… we observe a sharp transition… exactly at the location of the horizon… the same information could of course be extracted without reference to coordinates" (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-191`). (2) *Proved / theoretical:* Theorem 3.9's statistic \(S_n\) = number of comparable unordered pairs, i.e. exactly the Myrheim **ordering fraction** up to normalisation, \(r = 2R/(n(n-1))\) (Surya, *Living Reviews in Relativity* 22:5 (2019), Eq. (14), `biblioteca/derived-md/The causal set approach to quantum gravity.md:1006-1012`; Myrheim 1978; Bombelli 1987 PhD §2.5, `biblioteca/derived-md/Bombelli_1987_PhD.md:904`). Closed form of its signal (`docs/manuscript_limits_draft.md:605-660`): \(p(\tau)=\tfrac12+\kappa(r_p,r_q)\,\tau\,dv+R(\tau,dv)\), \(|\partial_\tau R|\le C_1 dv^2\), with \(\kappa(r_p,r_q)=\frac{(r_p^2-r_q^2)-2r_pr_q\log(r_p/r_q)}{12r_pr_q(r_p-r_q)^2}>0\), giving \(|p(\tau')-p(\tau)|\ge \frac{\kappa\,dv}{2}|\tau'-\tau|\) and \(\mathrm{TV}(Q^n_\tau,Q^n_{\tau'})\ge 1-\frac{4(2n-3)}{n(n-1)|p(\tau')-p(\tau)|^2}\).

- **Relevant invariants:** ordering fraction / comparable-pair count \(R\) (Surya LRR Eq. 14; Myrheim–Meyer estimator Eq. 17–18, `…quantum gravity.md:1030-1052`); longest chain / height from minimal elements (EGS §III, `…causal sets.md:181-191`); future volume \(|J^+(e)\cap U|\); Fisher information \(I(\tau)\) and the dilation-invariant combination \(\kappa_{\dim}=V\!\cdot\!I\) (`docs/manuscript_limits_draft.md:~760`, annex §5a). Note the ordering fraction is Surya's canonical example of an **O-Hauptvermutung** pairing (order invariant ↔ manifold invariant, `…quantum gravity.md:1081-1086`) — Theorem 3.9 is a legitimate member of that tradition, and Roy–Sinha–Surya 2013 (`biblioteca/Discrete geometry of a small causal diamond.pdf`) is its technique-level precursor per `research_program/bibliography/c6_theorem39_priority_audit.md:150-260`.

- **Analytic / continuum target:** For the sealed 1+1 track, the continuum benchmark is the EGS bimodal split of minimal elements at \(r/r_S=1\) (`…causal sets.md:150,188-191`), and the note's non-transfer claim is corroborated *by the same source*: "a regular black-hole spacetime… when considered in 3+1 dimensions, likely does not allow a partition of the corresponding causal set through these diagnostics" (`…causal sets.md:195`). For B2/`Q_trap` the continuum target is the classical trapped-surface condition \(\Theta(\ell^{(1)})<0 \wedge \Theta(\ell^{(2)})<0\), with the Schwarzschild instantiation \(\Theta_{\rm in}=-2/r,\ \Theta_{\rm out}=r^{-1}(1-2M/r)\) and \(\Theta_{\rm out}<0\) for \(r<2M\) (`…causal sets.md:201-203, 221-225`). For Theorems 3.8–3.9 the target is the minimax boundary exponent \(n^{-1/2}\), matched in the \(o/\omega\) sense (Cor. 3.10, `docs/manuscript_limits_draft.md:697-712`) — the constant is *not* determined.

- **Caveats:**
  - **The strong-goal closure is mathematically supported, and was already closed.** Thm 3.1 (`PROVED_NON_IDENTIFIABILITY`, TV=0 on the dilation orbit at fixed n) and Thm 3.2 (`T_EH` not \(\mathcal D(P)\)-measurable for a finite causally convex patch, `docs/manuscript_limits_draft.md:455-470`) are genuine structural obstructions, and §7.2 already records `ABANDONED_AS_PROGRAM_NORTH` for order-only 3+1 region-locators as a **governance** closure (`:1157-1169`). Nothing in the note over-reaches on this point.
  - **The note's "no further path" reading is NOT supported by the record.** The same manuscript §7.3 (`:1171-1181`) lists items typed `OPEN` and headed "**legitimate next science**", including B2 as the "**preferred scientific sequel**" (`:1179`). Closure point 1 ("no se abren nuevos observables, work packages… ni reformulaciones") silently overrides a live `OPEN` typing. That is a governance act, not a mathematical exhaustion, and the note should say so in those words or it becomes an unanchored claim in its own record.
  - **`Q_trap` is not inside the abandoned class, and is being terminated unadjudicated.** §7.2's scope is *region-locators*; `Q_trap` is explicitly binary, non-localizing, and intrinsic (G3, `phase3_b2_trapped_surface_preopening_contract.md:2.1, §7`), and it seeks a **negative** result (a testing floor) — the category in which this program has actually succeeded (Thms 3.1/3.2/3.8). Its Lema 0 (symmetry of the conjunction under \(\ell^{(1)}\!\leftrightarrow\!\ell^{(2)}\) plus \(\theta_{f\ell}=f\theta_\ell\), \(f>0\)) is a correct one-line proof and *does* immunize it against the exact obstruction that killed v1 (`B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`). No committee has ever ruled on it: 048 returned `RECOMMEND_REVISE_AND_RECONVENE` on the *predecessor* target, and the v1 terminal came from a PI-delegated session, not a comité acta. Signing the note as written retires a live, well-posed mathematical avenue by fiat.
  - **Partial discharge available for a `Q_trap` gap the contract marked open.** `…contract.md:2.2(2)` carries `[UNVERIFIED against biblioteca — no hay texto de relatividad matemática en biblioteca/]` for the trapped-surface definition. That is now partially false: EGS states the definition directly ("On a trapped surface, the expansions of both congruences of future-directed null geodesics (ingoing and outgoing ones) are negative everywhere", `…causal sets.md:201`) and gives the Schwarzschild expansions at `:221-225`. The Minkowski non-existence half (`Q_trap=0`) remains genuinely unanchored in `biblioteca/`. This lowers, not raises, the cost of adjudicating B2.
  - **Do not cite the dev figure "n ≈ 6.6M" as evidence of futility.** It is the output of the *literal* Theorem 3.9(2) Chebyshev bound, which uses the worst-case \(\zeta_1,\zeta_2\le 1/4\) and \(\mathrm{Var}(S_n)\le\binom n2\frac{2n-3}{4}\) (`docs/manuscript_limits_draft.md:660-690`). Bombelli 1987 already notes the true scale is CLT-governed, fluctuations \(\sim\sqrt{N_{\rm rel}}\) (`Bombelli_1987_PhD.md:978`), and the manuscript's own §7.3 types "Critical-scale constant, constant efficiency of \(S_n\), and a numerically certified \(dv_0\)" as `OPEN` (`:1181`). The true sample complexity is therefore **unknown and plausibly orders of magnitude smaller** `[UNVERIFIED — requires deterministic quadrature of \(\zeta_1(\tau),\zeta_2(\tau)\), which no committed artifact has performed]`. Using a deliberately loose bound as a closure argument would be a reasoning error in the permanent record.
  - **Two wording inaccuracies in the note's balance sheet.** (a) "la separación mediante fracción de orden… es débil, **asintótica**" — Theorem 3.9(2) is a **fixed-n** statement, labeled `PROVED_FIXED_N_SEPARATION`, holding "for every \(n\ge2\) and every fixed pair" (`:635-650`); "weak" and "parameter-conditioned" are fair (\(dv<dv_0\) uncertified; \(\kappa\to0\) as \(r_p/r_q\to1\), confirmed numerically per DOSSIER), "asymptotic" is not. (b) The note omits that Cor. 3.10 *matches* Thm 3.8's \(n^{-1/2}\) floor in the \(o/\omega\) sense — i.e. the 1+1 τ-identifiability sub-line is exponent-sharp and genuinely has nothing left but constants. Fixing (a) and (b) makes the note *stronger* on the 1+1 line and correspondingly makes the unadjudicated B2 branch the only real casualty.
  - **The 1+1 positive result carries no horizon semantics, and the note is right to say so.** In 1+1 Schwarzschild \(R_\tau=-2\tau/r^3\), so \(\tau\) is simultaneously horizon radius and the family's only curvature amplitude; discriminating \(\tau\) is discrimination of a continuous geometric parameter, and the manuscript **forbids** naming Thm 3.9 a "horizon detector bound" (mandatory physics caveat, `docs/manuscript_limits_draft.md:~740`). `NO_RECONSTRUCTION_CLAIM` is respected by the note.
  - **Recommendation from this role:** the mathematics supports closing the *reconstruction* program; it does not support "no further legitimate order-theoretic path exists". I would sign only a note that (i) preserves §7.3 `OPEN` items as open rather than deleting them, (ii) types B2/`Q_trap` explicitly as `CLOSED_BY_GOVERNANCE / NOT_ADJUDICATED / NO_MATHEMATICAL_OBSTRUCTION_ESTABLISHED`, and (iii) drops or footnotes any futility inference from the Chebyshev-derived \(n\). Absent (i)–(iii), my vote is *revise before signing* — not because the closure is wrong, but because as worded it asserts an exhaustion the record does not anchor, which is precisely the failure mode the first founding rule exists to prevent.

### Mathematical logic brief

- **Formal status:**
  - **Proved (Lean, machine-checked, `sorry`-free):** the `formal/HorizonFormal/` layer — 1014 lines across 7 modules, `grep -rn "sorry\|axiom\|admit\|native_decide"` returns zero hits. Its content is order-theoretic only and *by design* below the physics layer (`formal/HorizonFormal/README.md`: "deliberately starts below the Schwarzschild/GKP/sprinkling layer"). It contains no statement the closure note is closing. Notably it contains a falsifiable pair: the tombstone `relationalHorizonOld_eq_empty` (`formal/HorizonFormal/HorizonFormal/Horizon.lean:120`) and the non-emptiness witness `relationalHorizon_nonempty_witness` (`:246`) — an instance of a guardrail that *can* fail, per `CLAUDE.md`.
  - **Proved theorems (paper-level, typed):** Thm 3.1, 3.2, 3.8 `PROVED_NON_IDENTIFIABILITY`; Thm 3.9/Cor 3.10 `PROVED_FIXED_N_SEPARATION` (`docs/manuscript_limits_draft.md:1148-1155`). These are genuine non-existence results, but each with an explicit restrictor (fixed \(n\); stated dilation/co-scaling orbits; *finite causally convex* patch; the regular EF diamond family).
  - **Empirical / conditional:** §4 sealed PASS `VALIDATED (caveated artifact status)`; §5 `EMPIRICAL_FAILURE_OF_CLASS_L`. The closure note correctly types the latter — "los terminales C1–C6 documentan el fracaso de una clase de candidatos, no un no-go universal" — which is the honest reading and matches `manuscript:1155`.
  - **Governance act, not theorem:** `ABANDONED_AS_PROGRAM_NORTH` (`manuscript:1157-1170`) is *self-labelled* "a **governance** closure". The closure note is the same species, one scope level up.
  - **Not proved, and not claimed to be:** the note's central sentence — "tampoco ha establecido una contribución central que sea, a la vez, suficientemente original, físicamente útil y proporcionada" — is a **judgment over an inventory**, not a theorem. Correctly modalized in the note's own summary ("continuar ya no está científicamente justificado **con la evidencia disponible**") — evidential, not alethic. That modalisation is the note's single most important logical feature and must be preserved.
  - **Open, and closed by fiat rather than resolved:** `RESIDUAL_GAP_OPEN: random_geometric_graphs / latent_space_models` (`research_program/bibliography/c6_theorem39_priority_audit.md:300-310`); `PRIORITY_NOT_YET_CERTIFIED`; pointwise \(I(\tau)>0\) (`manuscript:1174`); certified \(dv_0\) (`manuscript:1181`).

- **Quantifier / dependency order:**
  - The note's core proposition is \(\neg\exists C\,[\mathrm{Original}(C)\wedge\mathrm{Useful}(C)\wedge\mathrm{Proportionate}(C)]\). The three conjuncts do **not** range over the same domain: `Original` and `Useful` are predicates of *existing* results; `Proportionate` is explicitly indexed to "el esfuerzo necesario **para continuar**" — a predicate over *unexecuted future work*. A finite inventory of past results can discharge the first two conjuncts over that inventory; it cannot discharge a conjunct quantified over the unexplored branch. **The universal is therefore an unexplored-search-space statement, not a proved non-existence.**
  - The note's own bullet 3 ("no un no-go universal") concedes exactly this and thereby blocks its own strong reading — consistent, but it means the closure must not be read as \(\neg\exists\) path.
  - **Dependency order defect (the sharpest one):** `comite_decision_048_q-fmots-target-adjudication.md:318` issued `COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE`. The *revise* half was executed (`phase3_b2_trapped_surface_preopening_contract.md`, `TARGET_NOT_ADOPTED / ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION`, `:3-9`). The *reconvene* half never ran. Decision 049 would adjudicate a strict superset while the deferred subset question is still outstanding. A superset decision may legitimately **moot** a subset one, but the note must say it is *mooting*, not *answering*, 048.
  - The B2 contract's own stopping rule is a conditional whose antecedent is unsatisfied: "Un bloqueo documentado de este target no refuta B2 en general… la decisión de cerrar B2 entera sería entonces un acto separado del PI" (`:235-237`). There is no documented block of \(Q_{\mathrm{trap}}\) — no adjudication was held. So B2 would be closed in state `UNADJUDICATED`, not `BLOCKED`. That is within PI authority (the contract does not condition PI closure on a block), but the two states are logically distinct and the record must not conflate them.
  - **Post-hoc degrees of freedom:** the decision rule "original ∧ useful ∧ proportionate" was never pre-registered as a continuation gate; it is chosen after seeing the corpus. Structurally this is a post-hoc rule. Its *direction* is protective — it can only manufacture a STOP, never a PASS — so `NO_POST_HOC_TUNING` is not violated in its guarding sense, and `make verify-seal` (`6e2c3888…`) confirms `RESPECT_SEAL_FREEZE` is untouched. But the rule should be typed as **PI prerogative**, not as a derived scientific conclusion. By contrast, §7.2's abandonment *was* pre-frozen (`phase0_program_north_decision.md`, R1), so the note's 3+1D component inherits a legitimate pre-declared basis; the broader components do not.
  - **Scope-widening hazard:** `docs/hoja_de_ruta_30_jul_2026.md:325-328` says "La **única** cuestión científica abierta que queda… es la prioridad específica de C6 geométrico". That "única" is scoped to the bibliographic-audit track. `manuscript:1171-1182` lists seven open items and B2 is live. If the closure note inherits the roadmap's "única" at program scope, that is an illicit widening of a restricted quantifier.

- **Equivalence claims:**
  - **Genuine proved biconditionals/equalities** (order-theoretic, Lean): `ChainEventuallyLe_iff_generated_subset`, `CofinalChainEquivalent_iff_generated_eq`, `isPrincipalIdeal_mapOrderIso_iff`, `accessesIdeal_iff_mem`, `relationalHorizonOld_eq_empty`. Also Thm 3.1's \(\mathrm{TV}=0\) is a true *equality* — exact indistinguishability, symmetric, hence the strongest object in the corpus.
  - **One-way only:** Theorem 3.9(2) is a lower bound \(\mathrm{TV}\ge 1-4(2n-3)/(n(n-1)|\Delta p|^{2})\). The dossier's inversions (\(n\approx 6.63\times10^{6}\) at the observed gap; \(n\approx 2.04\times10^{7}\) at the proved bound) are **sufficient** \(n\), not **necessary** \(n\). The closure note is safe here because it states no number; the committee brief must likewise not report these as "elements required" — that would read a one-way bound as an equivalence.
  - **Semantic, not proved:** the note's typing of the separation as "asintótica" is in tension with the manuscript's own token `PROVED_FIXED_N_SEPARATION` (`manuscript:1152`). The theorem is fixed-\(n\) consistent for each fixed pair; only its *practical* \(n\) is astronomical. "Débil y condicionada a parámetros" is anchored; "asintótica" is a mis-typing of the theorem's logical form and should be reworded (e.g. "fixed-\(n\) but with a separation constant so small that useful \(n\) is astronomical").
  - **Not an equivalence at all:** "cerrar el programa" \(\not\equiv\) "no existe camino legítimo". These are different speech acts — deontic (withdrawal of authorisation) vs alethic (non-existence). The note mostly keeps them apart, but the token `NO_FURTHER_RESEARCH_AUTHORIZED` sits adjacent to prose "ha llegado a su término", which reads alethic. Recommend the deontic reading be made explicit in the token block.
  - **Correctly discharged by renunciation:** closure §2 ("no se reclama novedad pública para los resultados cuya prioridad no fue certificada") disposes of `RESIDUAL_GAP_OPEN` by renouncing the dependent claim rather than by claiming the gap is closed. That is logically clean and exactly right — \(\neg\mathrm{Claim}(\text{novelty})\) makes the open priority question inert for the record, and it respects `c6_theorem39_priority_audit.md:292-298`'s prohibited formulations.

- **Type / object discipline:**
  - The Lean layer's objects are typed with no category slippage: `Order.Ideal P`, cofinal-chain **quotient classes** via `cofinalChainSetoid` / `nonterminalCofinalChainSetoid`, and — critically — `RelationalHorizon R : Set (P × P)`, a set of **covering pairs (links)**, not a set of points and not a continuum hypersurface. `RelationalPast` / `RelationalBlackRegion` are relative to a chosen reference \(R\), and `Horizon.lean:29-32` states plainly that the one-way no-escape property "does not by itself establish… any physical horizon claim; all of that burden lies with the (still open) selection rule for `R`." No `NO_RECONSTRUCTION_CLAIM` exposure from the formal layer.
  - **One category imprecision in the closure note.** `manuscript:118-140` (§1.4) enforces a permanent trichotomy — (1) global event horizon, (2) singularity-truncation cut, (3) quasi-local proxy — with silent substitution typed `TELEOLOGY_CLAIM_FAIL`. The note's opening question is posed over "estructura de horizonte de Schwarzschild", an **untyped disjunction spanning all three**. Its balance bullets do disambiguate (bullet 5 names "horizonte de eventos **global**"; bullet 4 says "una frontera **asociada al** horizonte dentro de un parche" — correctly weak). But the untyped top-line lets a reader infer that the proved results on object (1) close object (3), which they do not: `manuscript:1179` lists "Witness-pair or rate no-go for a *named* quasi-local proxy \(Q\neq T_{\mathrm{EH}}\)" as `OPEN`, and \(Q_{\mathrm{trap}}\) is exactly an object-(3) candidate. **This is the same conflation the closure would otherwise be committing at the branch level.**
  - Correct object handling elsewhere: "el horizonte de eventos global no es un funcional de un parche finito" is the precise statement of Thm 3.2 (a claim about a *functional*, not about a set), and "la escala absoluta es invisible en el canal fixed-n" correctly indexes the channel.

- **Caveats:**
  - The closure's universal is **unproven, not false**. What is proved is a set of restricted non-existence theorems (Thm 3.1, 3.2 — `manuscript:1149-1150`) plus a self-declared non-universal empirical ledger (`manuscript:1155`, note bullet 3). Neither entails \(\neg\exists\) legitimate path. Signing must therefore be an **executive/deontic** act, not endorsement of a non-existence claim.
  - The note is materially **incomplete as a record**: it never names `research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md` (`:3-9`, `TARGET_NOT_ADOPTED / ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION`), which `manuscript:1179` designates the "preferred scientific sequel". Closure §3 ("lo que quedó abierto") arguably covers it generically, but a program closure that leaves a *pending typed adjudication* unnamed under-documents its own scope. Minimal fix: name B2/\(Q_{\mathrm{trap}}\) explicitly and type it `UNADJUDICATED_AT_CLOSURE`, distinct from the v1 terminal `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`.
  - `comite_decision_048…:318` = `RECOMMEND_REVISE_AND_RECONVENE` has an undischarged consequent. The closure note should state that 048's reconvene directive is **mooted by executive closure**, not satisfied.
  - The v1 terminal came from a PI-delegated director session, not a comité acta (per DOSSIER); precedent 046 shows track-level closures went through comité. A *program*-level closure resting partly on a non-comité terminal has weaker procedural provenance than the narrower precedent it exceeds in scope. `[UNVERIFIED]` — I did not read `phase3_b2_qfmots_terminal_decision.md` this session; taken from the DOSSIER.
  - "Asintótica" (bullet 2) mis-types `PROVED_FIXED_N_SEPARATION` (`manuscript:1152`). Reword; do not let a closure note weaken a theorem's logical form beyond what the theorem says — that is over-claiming in the negative direction and is as much a record error as over-claiming positively.
  - The \(n\approx 6.6\times10^{6}\) / \(2.0\times10^{7}\) figures are **sufficiency** inversions of a one-way TV bound. Do not restate them as necessary sample sizes anywhere in 049.
  - `NO_FURTHER_RESEARCH_AUTHORIZED` and `PRESERVE_AS_SCIENTIFIC_RECORD` are mutually consistent only under the deontic reading; add one sentence making that explicit so the archived record cannot later be cited as "the program proved no path exists".
  - No guardrail-token violation detected on the logical side: seal verified untouched (`6e2c3888…`), no threshold moved, no ground truth used to define anything, no reconstruction claimed — the note's operative claims are all negative or bounded. `NO_POST_HOC_TUNING` is unviolated *in direction*, though the continuation criterion itself is post hoc and should be labelled a PI prerogative rather than a derived result.

### Physicist brief

- **Coordinates & patch:** Two *different* 1+1D Schwarzschild patch families are in play and the closure note conflates their fates. (i) **Thm 3.8/3.9 family:** ingoing Eddington–Finkelstein chart, `g_τ = -(1-τ/r)dv² + 2 dv dr`, `det g = -1` so the sprinkling measure is flat Lebesgue in `(v,r)` (`docs/manuscript_limits_draft.md:214-227`; `research_program/work_packages/wp4_comparable_pair_separation.md` §2, Fact C0); patch is the causal diamond `D_τ = J⁺_τ(p) ∩ J⁻_τ(q)` with fixed corners `0 < r_q < τ₀ ≤ τ₁ < r_p`, `dv := v_q - v_p`, which in the exact null chart `(Ũ, v)` (`Ũ := -e^{-v/2τ}ω_τ(r)`, `ω_τ(r) = e^{r/τ}(r/τ-1)`) is a coordinate box **straddling the horizon** `Ũ = 0`, with `min_{D_τ} r = r_q > 0` (singularity avoided). (ii) **Sealed §4 family:** a *fixed EF coordinate rectangle*, `t_edge = 6.0`, `r ∈ [0.1, 1.3]`, `r_S = 2M = 0.5` (`nachocausal/thresholds.py:37-42`). Prop 3.4 (`docs/manuscript_limits_draft.md:517-518`) records that the fixed EF box is **non-regular** (no QMD), so the §4 arena is deliberately *not* the arena where Thms 3.8–3.9 hold. Finiteness forfeits, irrecoverably, any asymptotic-horizon claim: the event horizon is `∂J⁻(𝒥⁺)`, and EGS state plainly that "*to define an event horizon in a causal set, an infinite sprinkling is required*" (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:173`) — the physical content of Thm 3.2.
- **Physical meaning of the signal:** The §4 observable `O(i) = |future(i)|` is EGS's own second diagnostic: interior minimal elements have truncated futures because every interior timelike curve reaches `r = 0` in finite proper time, giving a **bimodal** distribution of future-cardinality sorted by `r/r_S` (EGS lines 181, 186 Fig. 3 lower panel, 191, 193). Two physics caveats bind here. First, EGS explicitly warn that this cardinality version "*may be affected more strongly by the choice of boundary… if we sprinkle into a causal diamond, the cardinality of the future of the minimal elements varies between n and √n already for Minkowski*" (line 193) and prescribe "*box boundaries with large ratio of timelike to spacelike extent*" (line 390) — which the project honours (6.0 : 1.2 = 5:1, `thresholds.py:37-38`). Second, the project's box has `r_min = 0.1 > 0`, so the singularity is **outside** the domain: truncation there is by the wall/ceiling, not by `r=0`. What licenses the physical reading is the box-matched Minkowski control on the *identical point cloud*, differing only in causality (`SAME_CLOUD = True`, `thresholds.py:52-55`), with abstention 0.90–1.00 on Minkowski vs 0.00 on Schwarzschild — truncation artifacts are common-mode and cancel; the residual is attributable to BH causal structure. Separately, Thm 3.9's `p(τ)` is **not** a horizon detector: the manuscript's own mandatory caveat (`manuscript_limits_draft.md:725-731`) notes `R_τ = -2τ/r³`, so `τ` is simultaneously the horizon radius and the *only* curvature amplitude of the family, "*there is no threshold structure that activates because the diamond crosses r = τ*."
- **Sprinkling domain:** Declared region = the frozen tall EF box above; Poisson process w.r.t. `vol_g` (constant density since `√-g = 1`, so coordinate-uniform = covariant — the same identity EGS use, their line 135); intensities `(1500, 3000, 6000, 12000)`, primary `λ = 12000` (`thresholds.py:45-46`), i.e. `ρ ≈ 12000/7.2 ≈ 1.67e3`, `ℓ = ρ^{-1/2} ≈ 0.0245`, `ℓ/(2M) ≈ 0.049` — matching the frozen `θ_stab = 0.049` discreteness anchor. Forfeited by construction: absolute scale (Thm 3.1, fixed-`n` channel), the global EH (Thm 3.2), and any 3+1D transfer. Not forfeited: the `order+number` channel, where `N ~ Poisson(ρV)` makes absolute scale a *Number* observable (`manuscript_limits_draft.md:438-441`; `op12_tv_zero_3p1.md` §5: `TV = 0 iff M = M'`).
- **Claim boundary:** The verdict claims **localisation of a horizon-associated in-patch boundary score**, in units of `2M`, against pre-frozen thresholds, in one finite 1+1D EF patch, under one observable and one protocol — `VALIDATED` with `PRIMARY_ARTIFACT_LOST; TRANSCRIPTION_REVERIFIED; BLINDNESS_DOCUMENTARY_ONLY`. It does **not** claim: metric reconstruction, global-EH reconstruction (Thm 3.2), absolute `M` (Thm 3.1), 3+1D or Kerr, or that `τ`-discrimination is "horizon detection" (`:725-731`). The paper's regular-black-hole caveat is EGS's: for Hayward-type regular BHs, interior timelike curves can also be continued for arbitrarily long proper time, so "*a regular black-hole spacetime… likely does not allow a partition of the corresponding causal set through these diagnostics*" (EGS line 195) — i.e. the chain-length/future-cardinality mechanism the §4 observable rides on is **singularity-dependent**, not horizon-intrinsic. That is a real ceiling on the physical generality of the 1+1D positive and independently supports the closure note's refusal of a reconstruction claim.

**Caveats:**
- **The "physically very weak" diagnosis is materially mischaracterised, in three anchored respects.** (a) The `n ≈ 6.6e6` figure is the inversion of Thm 3.9(2)'s **Chebyshev bound with worst-case variance** `ζ₁, ζ₂ ≤ 1/4` (`manuscript_limits_draft.md:670-690`). But the project itself *proved* the true value: `ζ₁ = 1/36 + O(dv²)` (Thm C9, `wp4_comparable_pair_separation.md:406-407`). Substituting the proved `ζ₁` into the same Chebyshev step reduces the required `n` by a factor of exactly 9, to `≈ 7.4e5`; and since `S_n` is an asymptotically normal U-statistic with `ζ₁ > 0` (Prop C8), the *CLT-level* requirement for a one-sd separation is `n ≈ 1/(9Δp²) ≈ 4.6e4` — the same order as the sealed §4 run's `N ≈ 1.2e4`. [Hand arithmetic from dossier-reported `Δp = 1.554e-3` plus the cited proved identities; **not executed this session — treat the three numbers as `[UNVERIFIED]` as code output**, but the *direction and the factor-of-9* follow directly from replacing `1/4` by `1/36`.] The dossier's 6.6e6–2.0e7 is an artefact of proof technique, not a physical requirement.
- **(b) The `n` figure is a statement about `dv = 0.05`, not about the family.** `Δp ∝ κ·τ·dv` ⟹ `n ∝ dv^{-2}`. `dv` is the *advanced-time lapse* of the diamond and is a free design parameter; the only thing blocking a larger `dv` is that `dv₀` is **not numerically certified** (`manuscript_limits_draft.md:718-722`, §7.3 row "numerically certified `dv₀`"). Raising `dv` by 10× would drop `n` by 100×. So "needs millions of elements" is a proof-regime statement, and the honest label is *uncertified small-lapse regime*, which the closure note in fact already says — it then over-reads that into "physically weak."
- **(c) `κ → 0` as `r_p/r_q → 1` is geometrically forced, not a defect.** With `r_p = r_q(1+e)`, `κ = [(r_p²-r_q²) - 2r_p r_q log(r_p/r_q)] / [12 r_p r_q (r_p-r_q)²] ≈ e/(36 r_q²)` [hand expansion, `[UNVERIFIED]` as executed]. The family's own admissibility constraint is `r_q < τ₀ ≤ τ₁ < r_p`, so as `r_p/r_q → 1` the admissible `τ`-window collapses to zero: the diamond loses the radial room to straddle the horizon at all. A signal that vanishes when the patch stops straddling `r = τ` is behaving *correctly*. Note also `κ ≈ 1/(12 r_p r_q) → 0` in the opposite limit `r_p/r_q → ∞`, so `κ` is non-monotone with an interior maximum; the tested `(3.0, 0.5)` gives `κ ≈ 0.030`, within an O(1) factor of the achievable optimum — i.e. the tested diamond is close to the *best* case for this family, and reshaping buys nothing. The dossier names only one limit and reads it as generic decay.
- **What the closure note gets physically right, and I endorse:** in 1+1D there are no spatial two-surfaces, so expansion/trapped-surface targets are *dimensionally ill-posed* — EGS say so for their own setup: "*we do not have spatial two-surfaces available, because we are considering (1+1)-dimensional sprinklings. Therefore, we cannot compute the expansions*" (line 227), corroborated in `research_program/work_packages/phase3_b2_decision048_conditions_review.md:41,59`. This is a strong physical argument against the unadjudicated `Q_trap` v2 (`phase3_b2_trapped_surface_preopening_contract.md`) as a 1+1D avenue, independent of any statistics. Combined with the `τ ≡ horizon radius ≡ curvature amplitude` degeneracy (`:725-731`) and the singularity-dependence of the chain-length mechanism (EGS:195), I agree that **no horizon-*specific* 1+1D order-only observable is likely to be definable at all** — the 1+1D arena cannot separate "horizon" from "curvature scale."
- **But `order+number` with known `ρ` is a physically distinct, unexhausted channel, and the closure note does not name it.** It is not a re-run of a closed question: Thm 3.1's `TV = 0` is *expressly* fixed-`n`, and `op12_tv_zero_3p1.md` §5 shows the obstruction is **lifted** in `order+number` (`TV = 0 iff M = M'`), because the Poisson mean `ρ·M⁴·μ₁` differs. The manuscript lists it as "Open as **new program**… (Fase 3 B1)" (`manuscript_limits_draft.md` §7.3) and §8 closes with "*Further scientific work, if any, should open a new contract (order+number; …)*" (`:1231-1234`). Physically the reason is clean: `N` restores the absolute length scale that order alone provably cannot carry (Bombelli 1987 — recovery only up to a global conformal factor; the "Order + Number" slogan, `manuscript_limits_draft.md:442-448`). A blanket `NO_FURTHER_RESEARCH_AUTHORIZED` therefore closes, without physical argument, the one channel the program's own manuscript identifies as physically open. Caveat on its value: `order+number` recovers *scale*, not *horizon* — it would be a mass/scale-identifiability program, not a horizon program, so closing the *horizon* program while noting `order+number` as a separate future contract is a defensible reading; closing it silently is not.
- **Scope note on my own competence here:** I assess coordinates, patch, and physical meaning. Whether the governance act of full-program closure is warranted given `README.md:17-33`'s tier-1 3+1D destination, and whether an unadjudicated live contract (`phase3_b2_trapped_surface_preopening_contract.md`, `ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION`) may be closed by a note that never names it, are governance questions outside this brief. My physics input to them: the 1+1D `Q_trap` target is dimensionally ill-posed (EGS:227) and I would not defend it on physical grounds regardless of how the governance question resolves.
- I did not run any code, did not touch the seal, and read only committed artefacts. The seal SHA and git state are taken from the chair's DOSSIER as pasted; I did not re-verify them. `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE` all upheld in this brief.

## 5. Falsifier attack

### Falsifier attack

- Concrete failure modes:
  1. **Non-existence smuggled in as inventory.** The note's load-bearing sentence — "Tampoco ha establecido una contribución central que sea, a la vez, suficientemente original, físicamente útil y proporcionada al esfuerzo necesario para continuar" — conjoins two predicates over the existing record with one ("proporcionada") quantified over *unexecuted* future work. The record itself contradicts a non-existence reading: `docs/manuscript_limits_draft.md:1179` types Fase 3 B2 `OPEN` ("preferred scientific sequel"), `:1181` types the critical-scale constant / efficiency of Sₙ / certified dv₀ `OPEN`, and §8 (`:1232`) explicitly directs that further work "should open a **new** contract (order+number; non-horizon targets; adversarial pairs...)". A blanket `NO_FURTHER_RESEARCH_AUTHORIZED` that does not name and argue against the order+number channel (Fase 3 B1, which lifts the Thm 3.1 scale obstruction per the physicist brief) closes a physically distinct, unexhausted channel by silence. Only a deontic reading ("authorisation withdrawn") is supported; the note as drafted permits an alethic reading ("no path exists"), which the record refutes.
  2. **Live contract archived mid-flight, unnamed.** `research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md:4-6` carries `TARGET_NOT_ADOPTED / ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION`. The closure note never names it. `docs/comite/comite_decision_048_q-fmots-target-adjudication.md:318` = `RECOMMEND_REVISE_AND_RECONVENE`: the revise half executed, the reconvene half never ran. Signing closure as drafted adjudicates a strict superset of a question the committee itself deferred — without saying so.
  3. **The record is mis-stated by the note that claims to preserve it.** The note calls the separation "asintótica"; `docs/manuscript_limits_draft.md:175,322` type Thm 3.9 `PROVED_FIXED_N_SEPARATION` (fixed-n). A closure acta whose stated purpose is `PRESERVE_AS_SCIENTIFIC_RECORD` must not archive a mischaracterisation of that record as its final word.
  4. **The effort denominator is unanchored.** Any "proporcionada al esfuerzo" judgment leaning on the dev figure n≈6.6M inherits a worst-case Chebyshev bound (ζ≤1/4); substituting the project's own proved ζ₁=1/36 cuts it ~9×, and CLT-level scaling lands near the sealed run's N≈12000 (physicist brief; [UNVERIFIED] this session, direction of the factor-9 follows from the algebra). The closure's proportionality conjunct may be wrong by orders of magnitude in the note's favour.
  5. **Attack on keeping open (the other direction).** Refusing to close has its own failure mode and it is not hypothetical here: 7 region-locator candidates already failed and were closed by full comité process (`comite_decision_046`), the region-localizer north is `ABANDONED_AS_PROGRAM_NORTH` (§7.2), the physicist brief argues Q_trap is dimensionally ill-posed in 1+1D (no spatial two-surfaces, EGS line 227), and the "true sample complexity is much smaller" argument is itself [UNVERIFIED]. An open-ended program with an unburned virgin seed band [2,000,000–2,999,999] is a standing temptation to burn seeds chasing a diminishing effect or to re-litigate 042/046. The falsifiable middle: closure of *authorisation* is defensible today; closure of *possibility* is not — and "keep everything open" is not the alternative, "adjudicate the one deferred item, then close" is.

- Ground-truth leakage: **None.** The closure is a documentary act: no new observable, estimator, or boundary is defined, so there is no channel for the hidden embedding to guide anything. `make verify-seal` reproduces the frozen sha256 (`6e2c3888…`, matches `docs/preregistration_002.md`); working tree clean at `be958b6c`. Residual record-integrity (not leakage) risk: archiving with `main` 16 commits behind and two unmerged branches (`origin/formula` +2, `origin/agent/phase2-b2-documentation` +1) plus zero tags would freeze a public archive that differs from the adjudicated state — the note's "sincronizar" step must complete *before* archive, verifiably.

- Freeze violations: none inherent in the note. Two smuggling paths to bar explicitly in the acta: (i) the pre-archive "sync" must be merge-only — no re-execution of any committing step, no re-running sealed validation "one last time to confirm"; (ii) the virgin seed band must be archived documented as **UNBURNED**, not burned for a farewell confirmation run. Today's `dev/explore_p_tau_shape.py` is dev-side and reuses audited functions — no violation.

- Verdict coercion: three instances, all in the note's favour:
  1. Q_trap's state is abstain-like (`ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION`); closure as drafted silently collapses it into effectively-FAIL. It must be typed `CLOSED_BY_GOVERNANCE_WITHOUT_ADJUDICATION`, and the acta must state it is *mooting*, not *answering*, 048.
  2. "No suficientemente original" collapses an INCONCLUSIVE into a negative: today's `research_program/bibliography/c6_theorem39_priority_audit.md` returned `NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH / PRIORITY_NOT_YET_CERTIFIED` with the residual gap declared open. `NO_PUBLIC_NOVELTY_CLAIM` (conservative abstention) is correct; "not original" (asserted negative) is not what the audit says.
  3. None of the four tokens in `.claude/skills/comite/check_comite_brief.py:35-42` means "close the program". Whichever is emitted (presumably `RECOMMEND_DO_NOT_PROCEED`) is a scoped-step verdict being repurposed for a program-level act and must be glossed in-text, or the acta itself commits a token-semantics coercion.

- Premature / over-broad claims: the note is commendably conservative in the positive direction (no reconstruction, no asymptotic horizon, no 3+1D claim — consistent with `NO_RECONSTRUCTION_CLAIM`). The over-broad risk is **negative** over-claim: (i) the alethic "no path exists" reading (failure mode 1); (ii) the physicist's "no horizon-specific 1+1D order-only observable is likely definable at all" is a plausibility argument and must not enter the acta as established; (iii) C1–C6 remain "fracaso de una clase de candidatos, no un no-go universal" — the note says this correctly and the acta must not harden it.

- Independent-falsification gate: **Partially satisfied, with one propagated defect.** The PI drafted the note and the comité independently adjudicates it — gate formally met for the closure act. But the B2 v1 terminal the closure implicitly leans on (`phase3_b2_qfmots_terminal_decision.md:3-5`: `DIRECTOR_DECISION_UNDER_PI_DELEGATION / NOT_A_COMITE_ACTA / COMITE_NOT_RECONVENED_THIS_SESSION`) was authored and verified in the same delegated session. If the acta treats that terminal as comité-adjudicated, the author-sole-verifier defect propagates into the closure. The acta must cite it with its actual provenance label.

- Minimal falsification test: `grep -c -e "phase3_b2_trapped_surface_preopening_contract" -e "Q_trap" -e "048" <closure-note-file>` — expected result on the note as drafted: **0**. A zero confirms the worst failure concretely: a program-level closure that adjudicates a superset of comité decision 048's deferred question without once naming the live contract, the deferred target, or the acta that deferred it. If the note is revised to name and type them (`UNADJUDICATED_AT_CLOSURE` / mooting-not-answering), the check passes and my principal objection to signing falls away.

**Bottom line:** the closure is signable only as a deontic act with four amendments (name and type the live B2 contract; fix "asintótica" → fixed-n; replace "not original" with `PRIORITY_NOT_YET_CERTIFIED`; drop or bound any effort-magnitude inference). Unamended, it over-claims non-existence and coerces two abstentions into negatives. Refusing to close outright is the worse error: it re-opens governance-closed tracks on an [UNVERIFIED] sample-complexity hope with a virgin seed band exposed. `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: **BLOCK**
- Freeze status: The relevant freezes for *this* act are two: (a) the estimator-v2 validation contract — `docs/preregistration_002.md:1-9` ("Status: FROZEN pre-registration... After this commit nothing here may be tuned on a result") and `docs/preregistration_001_addendum.md:1-8` (thresholds fixed "before any validation seed is generated or analysed") — both already discharged by the reported PASS (`docs/preregistration_002_result.md:1,18`), and the closure note's clause 4 ("no se alteran resultados sellados, terminales, pruebas ni historial") correctly does not reopen either. (b) A second, distinct procedural freeze this closure act actually touches: `research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md:1-13`, whose own header states adjudication of Q_trap "**no puede ocurrir en la sesión que redactó este documento**" and requires a future independent `/comite` session (`contract:11-13`), and `docs/comite/comite_decision_048_q-fmots-target-adjudication.md:318` (`COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE`), whose "revise" half executed (v2 drafted) but whose "reconvene" half never ran. That is itself a written procedural commitment, and it is not frozen-satisfied before this closure act — it is precisely what this act would moot without discharging.
- Seal integrity: Confirmed unchanged. `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching `docs/preregistration_002.md:8` verbatim; `git status --short` empty; `git diff` shows no threshold/code delta this session (`dev/explore_p_tau_shape.py` is a numeric check only, per dossier). The proposed step does not re-run, re-derive, or re-interpret the sealed path.
- Seed discipline: dev pool `EXPLORE_POOL = 1_000_000..1_000_039` (`docs/preregistration_002.md:18`) stays disjoint from the reserved virgin validation band `[2_000_000, 2_999_999]` (`docs/preregistration_002.md:16-17`); the 20 seeds actually scored are listed at `docs/preregistration_002.md:25-27` and the remainder of that band was never touched. Nothing in the closure note or today's committed artifacts burns any seed. Consistent with the reproducibility engineer's finding: the note should say explicitly, in-text, that this band remains reserved/unburned going forward — this is a documentation gap, not yet a violation, but it must be closed before signature.
- Reporting rule: The one already-adjudicated result (`docs/preregistration_002_result.md`) was reported "regardless of value" per `docs/preregistration_002.md:64-68`, and remains so under this closure — compliant. However, the closure note's own verdict-reporting act is deficient on the committee's binding format: none of the four tokens enforced by `.claude/skills/comite/check_comite_brief.py:34-41` (`RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP`, `RECOMMEND_PROCEED_WITH_CAVEATS`, `RECOMMEND_REVISE_AND_RECONVENE`, `RECOMMEND_DO_NOT_PROCEED`) semantically denotes "close the program archive." Whichever is emitted must be glossed in-text as meaning program closure, or the committee's own reporting contract is violated by a silent semantic substitution — a form of the same discipline that forbids silently coercing an ambiguous outcome into a convenient label.
- Forbidden moves present? One live concern, not yet a committed violation: **quasi post-hoc reinterpretation of a pending adjudication.** Retiring `phase3_b2_trapped_surface_preopening_contract.md` under `NO_FURTHER_RESEARCH_AUTHORIZED` without ever running the independent session its own header (`contract:11-13`) and 048's `RECONVENE` half (`comite_decision_048...md:318`) require would finalize, by omission, a target-adjudication question that the program's own governance document says only a dedicated future session may adjudicate. That is the deontic analogue of "re-labeling an unrun test as decided" — not a threshold loosening, but a scope-of-authority overreach if signed as-is. No `NO_RECONSTRUCTION_CLAIM`, `NO_GROUND_TRUTH_LEAKAGE`, or `NO_THRESHOLD_LOOSENING` violation found on the sealed-validation axis proper.
- Reasons:
  - `docs/manuscript_limits_draft.md:1157-1163` (`§7.2 ABANDONED_AS_PROGRAM_NORTH`) is scoped narrowly to "further order-only region-locators aimed at Schwarzschild 3+1 horizon structure" — it is *already* a governance closure, and the note may correctly cite it, but it does not cover B1 (order+number), the Thm 3.9 bibliographic residual, or B2 adversarial pairs, all of which `§7.3` (`:1171-1181`) and `§8` (`:1231-1234`, "Further scientific work, if any, should open a new contract (order+number; non-horizon targets; adversarial pairs for named quasi-local proxies)") list as `OPEN`/legitimate. A blanket `NO_FURTHER_RESEARCH_AUTHORIZED` that does not name and separately address these standing `OPEN` items reinterprets a narrow, already-written governance closure as a broader one — that is scope creep against a frozen document, even though no threshold number is touched.
  - `docs/comite/comite_decision_048_q-fmots-target-adjudication.md:318` issued `RECOMMEND_REVISE_AND_RECONVENE`, not `RECOMMEND_DO_NOT_PROCEED`; a program-closure act is a strict superset of the deferred "reconvene" question and cannot silently supersede it without at minimum typing the state explicitly as `UNADJUDICATED_AT_CLOSURE` (per the mathematical-logic brief) rather than folding it into an undifferentiated "no further research" blanket.
  - `research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md:3-6` is self-typed `TARGET_NOT_ADOPTED / ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION` — a live, self-declared procedural gate. A closure note that retires it without running that gate is the one action in this dossier most analogous to "committing a step whose own governing document requires a review process that was never run."
  - Seal/seed/threshold discipline proper (`docs/preregistration_002.md`, `docs/preregistration_001_addendum.md`) is fully intact and is **not** what blocks this verdict — it is clean.
  - Path to PASS (matches wave-1 consensus, esp. mathematician and logician briefs): revise the note to (i) explicitly name and separately dispose of `phase3_b2_trapped_surface_preopening_contract.md`, typing it `UNADJUDICATED_AT_CLOSURE` / `CLOSED_BY_GOVERNANCE — NOT_ADJUDICATED — NO_MATHEMATICAL_OBSTRUCTION_ESTABLISHED` distinct from the v1 terminal `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`, (ii) preserve `§7.3` items (B1, B2, Thm 3.9 audit, dv0 constant) as open rather than foreclosed, (iii) drop the n≈6.6M figure as evidence of futility (`[UNVERIFIED]` per physicist/mathematician briefs — it is a Chebyshev worst-case artifact, not a proved bound using the project's own proved ζ1=1/36), (iv) gloss whichever `COMMITTEE_DECISION_VERDICT` token is used as meaning program closure, and (v) state in-text that the reserved band `[2,000,000-2,999,999]` remains unburned beyond the 20 already-scored seeds. With those five amendments this act would respect every standing freeze and could PASS as a documentary governance act.

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Eichhorn-Gamito-Stokes, "Towards black-hole horizons and geodesic focusing in causal sets," lines 181-182: "For minimal elements inside the horizon, the length of the longest chain is limited, because each timelike curve inside the horizon must reach r=0 within a finite [amount of proper time]" | Physicist + Mathematician | CONFIRMED |
| Same file, line 193: "the cardinality of the future of the minimal elements varies between n and √n already for Minkowski spacetime" | Physicist + Mathematician | CONFIRMED |
| Same file, line 227: "we do not have spatial two-surfaces available, because we are considering (1+1)-dimensional sprinklings. Therefore, we cannot compute the expansions" | Physicist | CONFIRMED |
| Same file, line 195: regular-black-hole caveat, "a regular black-hole spacetime... likely does not allow a partition of the corresponding causal set through these diagnostics" | Physicist | CONFIRMED (quote is accurate; note the source qualifies this specifically for the Hayward-type example "when considered in 3+1 dimensions" — the expert's paraphrase drops that qualifier but does not misrepresent the claim) |
| Same file, lines 221-225: Θ_in = -2/r, Θ_out = r⁻¹(1-2M/r), Θ_out<0 for r<2M | Physicist | CONFIRMED |
| Surya, *Living Reviews in Relativity* 22:5 (2019), `biblioteca/derived-md/The causal set approach to quantum gravity.md` lines 1006-1009 (ordering fraction r = 2R/n(n-1), eq. 14) and lines 1080-1083 (O-Hauptvermutung: order invariant = ordering fraction r, manifold invariant = dimension d) | Mathematician | CONFIRMED |
| Bombelli 1987 PhD, `biblioteca/derived-md/Bombelli_1987_PhD.md` line 904 (ordering fraction f(n), §2.5 "Expected total number of relations") | Mathematician | CONFIRMED |
| Same file, line 978 (fluctuations ~ √N_rel via central limit theorem, ordering-fraction reliability discussion) | Mathematician | CONFIRMED |
| Same file, lines 500-502 ("up to a global scale factor," Minkowski causal structure recovers affine/metric structure up to dilatation, attributed to Zeeman's theorem) | Mathematician | CONFIRMED |
| `research_program/bibliography/c6_theorem39_priority_audit.md` lines 150-193 (§4.4): classifies Roy-Sinha-Surya 2013 (arXiv:1212.0631) as `DIRECT_PRECURSOR` of the **technique** only, explicitly `NO_MATCH` for the small-lapse instantiation of Thm 3.9's κ(r_p,r_q) | Mathematician/dossier | CONFIRMED |
| Same file, lines 156-162: notes the local derived-md header carries a "March 21, 2024" OCR/metadata artifact from the `marker-pdf` pipeline, and gives the corrected date as arXiv:1212.0631 / Phys. Rev. D 87, 044046 (21 Feb 2013) | Mathematician/dossier | CONFIRMED |
| `docs/manuscript_limits_draft.md` §7.3, line 1179: "Witness-pair or rate no-go for a named quasi-local proxy Q≠T_EH \| OPEN \| Fase 3 B2 (adversarial pairs)—preferred scientific sequel" | Cross-check (multiple wave-1 briefs) | CONFIRMED — exact row text matches |
| Same file, line 1178: "Order+number with known ρ: separation of absolute mass \| Open as new program \| OP-1.2 §5: Poisson means differ when M differs; not developed here (Fase 3 B1)" | Cross-check (multiple wave-1 briefs) | CONFIRMED — exact row text matches |

- Notes: All 8 citation groups check out at or within a few lines of the locations given, and each quoted/paraphrased claim is substantively supported by the source text. The only imprecision found is in citation #3/item 3: the expert's brief states the regular-black-hole caveat as a general statement, while the source text (`Towards black-hole horizons...md` line 195) attaches it specifically to the Hayward-type example "when considered in 3+1 dimensions" — this is a minor loss of qualifier in paraphrase, not a misrepresentation, since the paper's broader discussion (lines 164-169, 199) does treat regular black holes generically as the motivating case. No citation was found to be fabricated, absent, or contradicted by its source.

## 8. Synthesis

**All seven roles converge, independently, on the same structural finding**: the closure note's
scientific balance sheet (mathematics correct, results negative/bounded, 1+1D reconstruction goal
genuinely not reached) is **sound and well-anchored**, but its **governance scope is one step too
wide**. It retires, by omission, exactly one live thing: the B2 `Q_trap` v2 contract
(`research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md`, commit
`b48d98f`), which:

1. is explicitly self-typed `TARGET_NOT_ADOPTED / ADJUDICATION_REQUIRED_IN_INDEPENDENT_SESSION`
   — a written procedural commitment to a future comité session that has never been convened;
2. is the direct, undischarged residue of `comite_decision_048`'s
   `RECOMMEND_REVISE_AND_RECONVENE` verdict (the "revise" half ran, the "reconvene" half did not);
3. is explicitly named by the manuscript itself (`§7.3`, line 1179) as the "preferred scientific
   sequel" — not a marginal or already-rejected idea;
4. is, per the physicist brief, probably **not viable** on 1+1D physical grounds (no spatial
   two-surfaces to define expansions) — but "probably not viable, unadjudicated" is a different,
   weaker state than "closed", and the note does not distinguish them.

**No role disputes** the following, and the committee treats them as settled premises of this
acta:

- The sealed §4 PASS, Theorems 3.1/3.2/3.8/3.9, and the C1–C6 ledger are correctly characterized
  by the note (with two small wording defects noted below) and none is reopened by this act.
- §7.2's `ABANDONED_AS_PROGRAM_NORTH` (order-only 3+1D region-locators) was already a valid
  governance closure and the note may lean on it without objection.
- The seal, seeds, and thresholds are untouched; this act carries no `NO_GROUND_TRUTH_LEAKAGE` or
  `RESPECT_SEAL_FREEZE` risk in itself.
- The B1 (order+number) channel is a physically and logically distinct, unexhausted avenue that
  the manuscript's own §8 names as the legitimate next contract *if* anyone chooses to open it —
  the closure note should not be read as foreclosing it, and should say so rather than leave it to
  inference.

**One open disagreement to surface, not hide**: the mathematician and physicist independently flag
that the "n ≈ 6.6M–2.0×10⁷ elements needed" figure — introduced in this session's own numerical
exploration, not by the PI's note — is a worst-case Chebyshev artifact, and that substituting the
project's own *proved* `ζ₁ = 1/36` would very plausibly cut it by an order of magnitude or more.
This is `[UNVERIFIED]` as executed code (the committee did not run it), so the committee does
**not** rule on whether the effect is "weak" or "merely expensive to prove tightly" — it rules only
that **this specific number must not be cited as a settled measure of physical futility** in
whatever record follows this acta.

**Ranked alternatives:**
1. **(Recommended.)** Revise the closure note per §9 below, re-present for a lightweight signature
   check (not a full re-convene — the substance was already adjudicated here), then sign and
   proceed with archival.
2. Sign the note exactly as drafted. **Not recommended**: this would retire `Q_trap` v2's
   self-declared review gate by silence, which the pre-registration warden types as a scope-of-
   authority overreach (`BLOCK`) rather than a scientific error.
3. Do not close; keep the program open indefinitely pending a Q_trap adjudication. **Not
   recommended**: the falsifier and physicist both note this has its own failure mode (an
   unburned virgin seed band as standing temptation; an all-but-certainly-nonviable 1+1D avenue
   given no spatial two-surfaces) and is disproportionate to one unresolved item.

## 9. Next-step spec

**Reversible steps (documentary only; the PI may ask for these now):**

1. Revise the closure note text to add, verbatim or equivalent:
   - A named, typed disposition for `phase3_b2_trapped_surface_preopening_contract.md`:
     `UNADJUDICATED_AT_CLOSURE — CLOSED_BY_GOVERNANCE, NOT_BY_MATHEMATICAL_OBSTRUCTION`, stating
     explicitly that this act **moots**, rather than **answers**, `comite_decision_048`'s deferred
     "reconvene" question, and (optionally, since the physics brief already argues it) that the
     committee's physics assessment is that a 1+1D trapped-surface target is likely dimensionally
     ill-posed regardless — but this is offered as color, not as the ground for closing it.
   - Reword "la separación mediante fracción de orden... es débil, asintótica" → "...es débil (en
     el sentido de una constante \(\kappa\) pequeña y un régimen `dv` no certificado
     numéricamente), y consistente `PROVED_FIXED_N_SEPARATION` — no asintótica."
   - Replace any reading of "no ha certificado... resultados novedosos" that could be parsed as
     "not original" with the literal audit tokens: `PRIORITY_NOT_YET_CERTIFIED` /
     `NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH` (i.e. abstention, not a negative finding).
   - Drop, or footnote as `[PROOF-TECHNIQUE ARTIFACT, NOT A PHYSICAL BOUND]`, any use of the
     "millions of elements" figure as evidence of physical futility.
   - Add one sentence making explicit that `NO_FURTHER_RESEARCH_AUTHORIZED` is a **deontic**
     withdrawal of authorisation under present evidence, not an **alethic** claim that no
     legitimate path exists — and that the `order+number`/B1 channel remains a separate,
     unaddressed-by-this-note possibility for any future PI decision.
   - State that the reserved virgin seed band `[2,000,000–2,999,999]` remains unburned.
2. `git tag -a` the final pre-archive commit with a message recording the seal SHA and HEAD.
3. Merge / synchronize `main`, `origin/formula`, and `origin/agent/phase2-b2-documentation` (or
   issue an explicit typed disposition abandoning the ones not merged), so that the archived
   default branch actually contains the adjudicated record.
4. Optionally run `make test` / `make audit` / `make verify-comite` once, read-only, to capture
   their exit status in the closure record before the environment becomes unreachable post-archive.

**Committing steps (only on explicit PI authorisation, in this order):**

1. Commit the revised closure note + this acta.
2. Push to `origin` (all synchronized branches).
3. Create the annotated tag.
4. Toggle the GitHub repository to archived/read-only. This is the only step in the whole sequence
   that is administratively irreversible in practice (technically un-archivable, but after this
   no gate, guard, or CI target in this repo can run) — it must be strictly last.

**Falsifier's minimal check, pre-committed:** before any of the above commits, run
`grep -c -e "phase3_b2_trapped_surface_preopening_contract" -e "Q_trap" -e "comite_decision_048" <revised-closure-note>`
— must be **non-zero**. A zero result means the revision did not actually name the live contract
and the note must not be signed.

**Binding rules carried forward unchanged:** `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`,
`NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`. No new seed is drawn,
no threshold is touched, no sealed byte is modified by this closure act at any step above.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

**Gloss (program-closure act, per the reproducibility engineer's and warden's flagged token-
semantics gap):** for this program-level closure question, `RECOMMEND_REVISE_AND_RECONVENE` means
— *the scientific substance of the closure is sound and does not require a full second committee
session to re-litigate; what is required is a scoped textual revision (§9) naming and typing the
one unadjudicated live branch, after which the PI may sign the revised note directly without a new
`/comite` convocation, since the substantive adjudication has already been done here.* This is
consistent with the pre-registration warden's `BLOCK` (§6): the warden blocks the note *as
currently drafted*, not the underlying closure decision, and specifies the exact path to PASS
(§6, "Path to PASS", five amendments — all folded into §9 above).

## 11. User sign-off

**Decision:** SIGNED — PI authorises the program closure.
**Date:** 2026-07-30.
**Basis:** the five amendments specified in §9 were incorporated into the revised closure note
(`docs/program_closure_note_2026-07-30.md`), discharging the pre-registration warden's `BLOCK`
(§6) without a second committee session, per this acta's own §10 gloss. `Q_trap` v2 is signed off
as `UNADJUDICATED_AT_CLOSURE` (not adjudicated, not blocked mathematically); the `order+number`
(B1) channel is explicitly left outside this closure's scope, not foreclosed by it.
**Overriding notes:** none. No amendment to §9's next-step spec.
