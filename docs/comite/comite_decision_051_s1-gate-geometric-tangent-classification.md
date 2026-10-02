# Comité Decision 051 — s1-gate-geometric-tangent-classification

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Auditoría adversarial de PUERTA S1→S2. ¿Debe autorizarse el commit de
`research_program/work_packages/wp6_d2_geometric_tangent_classification.md` (untracked, 1172
líneas, rama `emergencia/p1a-canal-sigma-m`), que proclama
`GEOMETRIC_TANGENT_CLASSIFICATION = PROVED`?

`docs/hoja_de_ruta_septiembre_2026.md` §3 (`:206-208`, «Esta fase sólo se abre si S1 termina
`PROVED`») convierte ese token en **puerta lógica que autoriza la fase S2**, no en una mejora
documental. Por eso se audita antes del commit.

El PI encargó falsar específicamente cinco puntos:

1. §9.1-9.2 — identidad `P = (I-M_u)(I-M_v)`, idempotencia, y `ker P = A`, `ran P = R`,
   `A ⊕ R = C(D)`, `A ∩ R = {0}`.
2. §9.4 Teorema 6 — el «iff» completo, incluyendo el caso degenerado `lambda = 0`, y si
   `int f^2 > 0` se usa o sólo se arrastra.
3. §9.5 Proposición 9.4 — suficiencia de la absoluta continuidad, y si «la única equivalencia
   marginal que sobrevive es `ker P`» es teorema o salto.
4. §11.3 (H3) — uniformidad de la convergencia cerca de los extremos `i=1`, `i=N`.
5. §5 y §3.2 — si el paso cópula → score condicionado introduce una dependencia oculta de
   `epsilon` por el PIT.

Veredicto de puerta requerido: `GATE_PASS` / `GATE_PASS_WITH_CONDITIONS` / `GATE_FAIL`.

## 2. Verified state

Hechos comprobados **en esta sesión** por el chair, cada uno con su comando o `file:line`.

- **Sello intacto.** `make verify-seal` →
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`. Coincide con
  `docs/preregistration_002.md:7-8` y `docs/hoja_de_ruta_24_jul_2026.md:83`.
  `docs/estimator_v2_seal.md:7` (`2f4c4a99…`) y `docs/preregistration_001_addendum.md:121`
  (`ad02cb57…`) son registros de congelación anteriores, **no** el sello vivo; no hay discrepancia.
- **Árbol limpio salvo el artefacto.** `git status --short` → única entrada
  `?? research_program/work_packages/wp6_d2_geometric_tangent_classification.md`. Cero ficheros
  rastreados modificados. Ningún instrumento sellado tocado.
- **Cabeza de rama.** `git log --oneline -3` → `99cec0d add September roadmap for geometric
  tangent bridge` / `4bcbfc5 document unlabeled 2D poset Fisher theorem` / `236b182 prove
  asymptotic Fisher efficiency for unlabeled 2D posets`.
- **Anclas de reutilización declaradas en §0, todas resueltas.**
  `wp6_d2_null_copula_dichotomy.md` §§1-2 (`:22`, `:54`);
  `wp4_ibar_direct_score_derivation.md` §§5-6 (`:252`, `:282`);
  `wp6_d2_modular_fiber_score.md` §7 (`:825`), con el Teorema 5 en §7.6 (`:1090`).
- **Cero superficie ejecutable.** El artefacto no publica ningún número producido por script, no
  consume semillas, no ejecuta simulación. Es prueba matemática en texto.
- **Brecha de perímetro, verificada por el chair y confirmada después por dos roles.**
  `docs/program_reopening_note_2026-07-31.md:83` fija «Perímetro fijo: R1 y R2. Nada entra sin una
  nueva nota firmada». La última nota firmada es R3
  (`docs/program_reopening_note_2026-08-05_R3.md:38-43`), cuyo ámbito autorizado es puente E +
  redacción + auditoría de novedad. **No existe nota R4** (`ls docs/program_reopening_note_*`
  devuelve sólo las dos). `docs/backlog_hallazgos.md`, destino obligado de todo hallazgo fuera de
  perímetro por la regla §6.2 de la nota del 07-31, **no existe**.
- **Tokens contradictorios ya en el árbol.**
  `research_program/work_packages/wp6_d2_modular_fiber_score.md:20` y `:1263` dicen
  `GEOMETRIC_TANGENT_CLASSIFICATION = OPEN`; `README.md:95` dice
  `NEXT_TARGET = GEOMETRIC_TANGENT_CLASSIFICATION`.
- **Falta cabecera de gobernanza.** El hermano `wp6_d2_null_copula_dichotomy.md:3-9` lleva bloque
  `ESTADO / ALCANCE / NATURALEZA / GOBERNANZA / FECHA`. El artefacto auditado no lleva ninguno.
- **Alcance del `/auditor`.** El chair no invocó la skill `/auditor` completa y ejecutó en su lugar
  su sustancia aplicable a este artefacto: sello, higiene de árbol, y resolución de cada cita
  reutilizada. Motivo declarado: no hay números publicados, scripts, ni bandas de semillas que
  auditar. **Esta decisión de alcance es del chair y el PI puede revocarla.** `[UNVERIFIED]` queda
  todo lo que un `/auditor` completo habría cubierto y esto no cubre.

## 3. Dossier

- `research_program/work_packages/wp6_d2_geometric_tangent_classification.md` — el artefacto
  auditado (untracked, 1172 líneas).
- `docs/hoja_de_ruta_septiembre_2026.md` — §2.1-2.5 (obligaciones, falsificadores, veredictos
  permitidos) y §3 (fase S2).
- `research_program/work_packages/wp6_d2_modular_fiber_score.md` §7 — Teorema 5 congelado.
- `research_program/work_packages/wp6_d2_null_copula_dichotomy.md` — Lema A, Proposición B,
  Teorema C, Teorema D, obstrucción `b`.
- `research_program/work_packages/wp4_ibar_direct_score_derivation.md` — §§5-6 (score a rangos
  fijos), `:300-312` (ANOVA / doble centrado), `:395-420` (Lema 9.1).
- `docs/program_reopening_note_2026-07-31.md`, `docs/program_reopening_note_2026-08-05_R3.md`.
- `docs/preregistration.md`, `docs/preregistration_001_addendum.md`,
  `docs/preregistration_002.md`, `docs/estimator_v2_seal.md`.
- `CLAUDE.md`, `README.md`, `research_program/README.md`, `Makefile`, `audit.sh`.
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`.

## 4. Expert briefs (wave 1 — blind, parallel)

Los cuatro expertos trabajaron en paralelo y ciegos entre sí. Sus secciones se reproducen tal como
las devolvieron.

### Reproducibility engineer brief

**Role verdict: GATE_PASS_WITH_CONDITIONS** (documentary commit only; the `PROVED` token must not be committed in gate-triggering form until conditions C1–C6 are met). If the PI declines C1, this becomes GATE_FAIL on governance, not on mathematics.

- **Proposed artefact(s):**
  - `research_program/work_packages/wp6_d2_geometric_tangent_classification.md` — the single untracked file (`git status --short` returns only this entry). Placement is in tension with `research_program/README.md:3-5` ("REVISABLE, no congelado… no convierte ninguna conjetura conceptual en resultado") and `:10-12`, which reserve `docs/` for "claims, preregistros, **cierres de fase**, auditorías y documentos con valor de registro". A phase-gate document is a *cierre de fase*. Precedent is mixed: `wp6_d2_modular_fiber_score.md` also lives in `work_packages/` and declares `ASYMPTOTIC_..._PROVED` (`:1261`).
  - Required companion artefact (missing): a signed perimeter note `docs/program_reopening_note_2026-08-2x_R4.md`. See C1.
  - Required companion edit (missing): the stale token in `research_program/work_packages/wp6_d2_modular_fiber_score.md:20` and `:1263` (`GEOMETRIC_TANGENT_CLASSIFICATION = OPEN`) and `README.md:95` (`NEXT_TARGET = GEOMETRIC_TANGENT_CLASSIFICATION`).

- **Environment & seal:** the artefact is pure text — **no environment is exercised, no interpreter, no numpy, no Minz clone**. `NACHOCAUSAL_MINZ_PATH` / `~/cs-horizon-reuse-check/venv_minz` (`CLAUDE.md:48-50`) and the pinned `numpy==1.26.4` (`Makefile:2-3`) are *not* touched. The chair-run `make verify-seal` (`Makefile:22-24`) returned `6e2c3888…bfefd4`, matching `docs/preregistration_002.md:7-8` and `docs/hoja_de_ruta_24_jul_2026.md:83`; `nachocausal/thresholds.py` is not in the diff, so the seal is provably invariant under this commit. The historical hashes in `docs/estimator_v2_seal.md:7` (`2f4c4a99…`) and `docs/preregistration_001_addendum.md:121` (`ad02cb57…`) are prior freeze records, not the live seal — `audit.sh:60-73` only requires the **live** hash to appear somewhere in `docs/`, which it does. `make audit` checks 4 and 5 (`audit.sh:78-101`) are indifferent to a new `.md`, so `make audit` must still exit 0 after the commit. Package-diff-clean check: N/A, no packages invoked; the correct analogue is a **tree-diff-clean check** — the commit must contain exactly one added file and zero modifications.

- **Provenance capture:** since there is no run, the record must be carried *inside the document*, and it currently is not. `grep -n '2026|FECHA|GOBERNANZA|NATURALEZA'` on the artefact returns **nothing** — the document has no date, no governance line, no seal-state line. Contrast the sibling gate document `research_program/work_packages/wp6_d2_null_copula_dichotomy.md:3-9`, which carries `ESTADO / ALCANCE / NATURALEZA: deductivo… Cero semillas, cero simulación, sello intacto / GOBERNANZA: requiere nota firmada — ver docs/program_reopening_note_2026-08-05_R3.md / FECHA`. Required header fields: commit parent (`99cec0d`), branch (`emergencia/p1a-canal-sigma-m`), `FECHA: 2026-08-28`, `NATURALEZA: deductivo — cero semillas, cero simulación, cero ejecución`, `SELLO: 6e2c3888… intacto`, `SEMILLAS: banda virgen sin quemar`, `GOBERNANZA: <nota R4>`, `GATE_AUDIT: <veredicto del comité>`. No pip freeze / uname / seed band / timestamp is applicable because no process runs.

- **Run mechanics:** reversible pre-flight (read-only w.r.t. sealed state, safe to repeat): `make verify-seal` → expect `6e2c3888…`; `make audit` → expect exit 0; `make test` (`Makefile:11-12`) → expect green, purely as a null-effect witness. Committing step: a **single foreground invocation**, `git add <the one path> && git commit`, no background job, no `git push`. A guard aborts cleanly by simply not staging: the file is untracked, so abort = no-op, and post-commit reversal is `git revert` on an unpushed branch. Explicitly **not** authorised and **not** needed: `make dry-run`, `make gate`, `make op21-terminal` — none of these bear on a text artefact, and `op21-terminal` is a single-authorised terminal run (`Makefile:37-38`) that must not be perturbed.

- **Reproducibility risks / ambiguities:**
  - **C1 — perimeter governance gap (blocking).** `docs/program_reopening_note_2026-07-31.md:83`: *"Perímetro fijo: R1 y R2. Nada entra sin una nueva nota firmada."* The last signed note is R3, whose `AUTHORISED_SCOPE` is the **closed list of §2** (`docs/program_reopening_note_2026-08-05_R3.md:38-43`, signature block `:100-110`) — bridge E, write-up, novelty audit. The geometric-tangent / Fisher-efficiency frontier is not in that list. `ls docs/` shows **no R4 note**. Yet three artefacts of this frontier were committed on 2026-08-28 (`236b182`, `4bcbfc5`, `99cec0d`) and none carries a `GOBERNANZA:` line, unlike `wp6_d2_null_copula_dichotomy.md:7`. Under the repo's own rule 6.2 (`:84`) an out-of-perimeter finding goes dated to `docs/backlog_hallazgos.md` — **which does not exist** (`ls` fails). Condition: the PI signs an R4 note authorising this frontier, or the gate token is withheld.
  - **C2 — contradictory machine-readable state.** Committing `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` while `wp6_d2_modular_fiber_score.md:20`/`:1263` still say `= OPEN` puts two contradictory values of the same key in the tracked tree with no pointer between them. Condition: update both, or add an explicit `SUPERSEDED_BY:` line.
  - **C3 — grep-collision hazard on the gate string.** `docs/hoja_de_ruta_septiembre_2026.md:198` fixes `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` as the *exact* verdict token, and §3 (`:206`) makes it the S2 opener. The artefact emits that exact string inside fenced blocks (§0 and §12) next to `GATE_AUDIT = PENDING`. Any downstream reader or agent keying on the string alone concludes S2 is open. Condition: until the gate audit signs off, emit `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED_PENDING_GATE_AUDIT` (a string that cannot match the roadmap trigger), and keep `S2_NOT_OPENED` adjacent.
  - **C4 — §10 contradicts its own independence claim.** The heading and the sentence "**Verificación directa, sin invocar §3**" are falsified four paragraphs later by "Sustituyendo en (3.4)", and (3.4) is defined in §3.2. The check is independent of the *derived* result (3.5), not of §3. Condition: reword to "sin invocar (3.5)", and state that (3.4) is the standard copula-density change of variables. (The substantive O(ε²) step is sound and reader-checkable: `q_0 ≡ 1` has zero spatial gradient, so the O(ε) quantile shift enters only multiplied by ε — the same mechanism as §3.2, and structurally the same as `wp4_ibar_direct_score_derivation.md:295-300`, where the quantile velocities `a1, a2` multiply *spatial* derivatives of `g`.)
  - **C5 — two mis-citations, both repairable, neither a math failure.** (i) §11.5 attributes `I_N^Π = E[(ℓ̇_N^Π)²]` to "§7.5 del WP6 modular"; it is equation (7.4) in **§7.4** (`wp6_d2_modular_fiber_score.md:1027-1032`). Only the `L_N` definition is in §7.5 (`:1052-1056`). (ii) The proof of Theorem 6, branch (c)⇒(a), invokes Lema 9.2 to get `P(λ f⊗f) = λ f⊗f`, but Lema 9.2 is stated under `f ≠ 0` **and `λ ≠ 0`** (artefact §9.3), so it does not cover the degenerate `λ = 0`. The correct citation is point 4 of Proposition 9.1 (`R ⊂ ran P`, `Pφ = φ`), which holds for every λ. Relatedly, `∫f² > 0` appears in the hypotheses of Theorem 6 but is never used in its proof — it is load-bearing only in §11 (H3). Condition: re-point the citation and either drop `∫f² > 0` from Theorem 6 or mark it as carried forward for §11.
  - **C6 — non-effective constant inherited, caveat dropped.** (11.6) reuses `C_A` from `wp6_d2_modular_fiber_score.md:1041-1046`, where it is explicitly an **unpublished external constant** ("sin inventar una constante que la fuente no publica", Bouvel–Chauve–Mishna–Rossin) valid only for `N ≥ N_A`. The artefact correctly says "no inventada aquí" but omits the `N ≥ N_A` domain restriction. So (11.6) is asymptotic and non-effective; it can never be numerically checked by a reader. Condition: carry the `N ≥ N_A` caveat.
  - **Inherited defect, flagged not blocking.** `wp6_d2_modular_fiber_score.md:1233-1248` asserts a *computational* result (exhaustive rational arithmetic over `S_N`, `1 ≤ N ≤ 8`, "los 40 casos dieron igualdad", 40320 permutations) with **no committed generator** — commit `236b182` added only the `.md`, and `git ls-files` shows no such script. That is precisely the "committed result with no generator" pattern founding rule 1 targets, and `audit.sh:87-101` misses it because it only scans data files, not numbers asserted in prose. It is not load-bearing (`:1252-1254` says the check "no interviene en la prueba"). The artefact under audit **does not repeat this defect**: a grep for `verific|script|python|numpy|seed|simulaci|semilla` returns only its own negative claims ("sin simulación", "ninguna semilla"). This is the artefact's strongest reproducibility property and should be preserved.
  - **No executable check is required to settle any of the five attack points.** All five are pure analysis over closed forms. I hand-verified the two that are arithmetically checkable: (11.5), `Σ_{i=1}^{m-1}(i − m/2)² = (m−1)m(m−2)/12` with `m = N+1`, giving `(N−1)/(12(N+1)) → 1/12` — correct; and (11.4), whose stated bound `(N+1)/N[ω_g(1/(N+1)) + ‖g‖_∞/(N+1)] + (1/N)∫g` is exactly what the right-endpoint sum minus the `i = N+1` term plus the `(N+1)/N` reweighting produces — correct. On attack point 4, `Var(U_(i)) = i(N+1−i)/((N+1)²(N+2))` is maximised at `i = (N+1)/2`, so the bound `≤ 1/(4(N+2))` is **uniform in i**, Chebyshev applies uniformly, and `δ_N = (N+2)^{−1/4}` gives `‖f‖_∞/(2√(N+2))` uniformly including `i = 1, N`; the argument uses only the uniform variance bound and the uniform continuity of `f`, never the shape of the Beta, so end-point asymmetry is irrelevant. `(11.1)` is reproduced verbatim from `wp6_d2_modular_fiber_score.md:1168-1176` — real citation, says what is claimed. Theorem 5's three hypotheses (`:1092-1099`) match (H1)/(H2)/(H3) exactly.
  - **Optional, explicitly NOT a condition:** if the committee wants belt-and-braces on §10 and (11.5), the precedent shape is `wp6_d2_modular_fiber_score.md` §7.8 — **exact rational arithmetic, zero RNG, zero seeds, no sealed instrument**, run in `dev/` outside `make test`, with the script committed alongside (correcting the §7.8 omission). This is a falsifier, not evidence: it cannot upgrade `PROVED`, and it must not be made a gate precondition, because the underlying identities are already reader-checkable by hand.
  - **Commit hygiene is otherwise sound:** one untracked file, zero tracked modifications, no sealed instrument touched, branch is the working branch named in `docs/hoja_de_ruta_septiembre_2026.md:12`, no seeds consumed, no roadmap edit (the §6.3 normalisation correction is proposed as a diff and explicitly **not applied** — correct, and in any case the roadmap self-declares "Plan REVISABLE, no congelado", `:3`, so no freeze is at stake). `RESPECT_SEAL_FREEZE`, `NO_GROUND_TRUTH_LEAKAGE`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING` are all untouched by this commit. `NO_RECONSTRUCTION_CLAIM`: the artefact contains no novelty or reconstruction language (grep for `first|novel|breakthrough|primera vez` returns nothing) and keeps `NO_UNIVERSALITY_CLAIM` / `PRIORITY = PROVISIONAL_NOT_SEALED`, consistent with R3 §5's absolute-novelty prohibition.

### Mathematician brief

- **Computability:** On the order relation alone the decidable object at fixed cardinality is the isomorphism class `[P_N]` of the induced poset. In a null-coordinate box the causal relation is exactly the product order (`wp6_d2_null_copula_dichotomy.md:47-49`), so the sprinkled causet is a.s. a strict 2-dimensional order, i.e. a permutation poset (ties have probability 0 because `q_eps = e^{2 eps psi}/Z > 0` is continuous, `…geometric_tangent_classification.md:120-124`). Two levels must be kept apart and the audited document does keep them apart only implicitly: `Pi_N` (the rank permutation) is **not** order-only — it presupposes a chosen realizer (the `U`-linear-order and the `V`-linear-order); the order-only datum is `[P_{Pi_N}]`. The document's chain lives at `Pi_N` level from §5 to §11.4 and only re-enters the order-only world at §11.5 via the frozen channel `Pi_N -> [P_{Pi_N}]` (`…geometric_tangent_classification.md:1115-1132`). That channel is genuinely computable from order alone: the event `A_N` is `[P]`-measurable because the modular tree of the incomparability graph is determined by the poset up to isomorphism (`…wp6_d2_modular_fiber_score.md:1049-1051`), and the fiber is `{pi, pi^{-1}}` only on `A_N` (`…modular_fiber_score.md:817`), consistent with the exhaustive `n=4` enumeration showing fibers of size 3 off that event (`…null_copula_dichotomy.md:186-210`). No `tau(n)` / domain gate is engaged here: §0 and §12 declare zero seeds, zero simulation, and the seal is untouched, which the chair's `git status` confirms.

- **Order observable:** the step relies on the conditional score `S_{N,psi}(pi) = E_0[sum_k h_psi(U_k,V_k) | Pi_N = pi]` (`…geometric_tangent_classification.md:386-394`), which for `h_psi = kappa f⊗f` factorises exactly as `kappa sum_i a_{i,N} a_{pi(i),N}` with `a_{i,N} = E[f(U_{(i)})]` (eq. 5.3, `:422-428`). The factorisation is order-theoretically correct: under the uniform null the rank permutation is independent of the order-statistic vectors and the two order-statistic vectors are independent of each other, and the chamber `Pi_N = pi` pairs `U_{(i)}` with `V_{(pi(i))}` (`:400-412`) — classical, but asserted without citation. Why it carries geometric signal: `h_psi = 2 P psi` with `P = (I-M_u)(I-M_v)` (`:624-629`), and `ker P = A` = the separable directions, which by Proposición B are exactly the flat ones (`…null_copula_dichotomy.md:84-95`); at first order `R ∝ Omega^{-1} d_u d_v log Omega` (`…null_copula_dichotomy.md:98-102`) kills `A` and sees exactly `P psi`. So `P` is precisely the linearised curvature content, and the frozen witness `f(u)=u-1/2` (`…geometric_tangent_classification.md:526-546`) is the constant-linearised-curvature direction (`d_u d_v (lambda f⊗f) = lambda f'f' = lambda`). This is curvature, **not** horizon: roadmap §3.2 explicitly forbids a horizon claim at S2 (`docs/hoja_de_ruta_septiembre_2026.md:243`), and the document correctly makes none.

- **Relevant invariants:** the invariants actually used are (i) the isomorphism class `[P]` and, through it, the modular/substitution decomposition of the incomparability (permutation) graph — the only invariant carrying the zero-conditional-variance result (`…modular_fiber_score.md:788-812`, Corolario 6.7); (ii) pattern densities of size `n` (permuton densities), which are the linearised content of `S_{N,psi}` and the object of Teorema D (`…null_copula_dichotomy.md:146-158`, HKMMRS 2013 + Grübel 2024). Ordering fraction / longest chain / `C_k` interval abundances are **not** used here; the `2D poset ↔ permutation, flat ↔ uniform` correspondence is logged in-repo as prior art / CST folklore (Myrheim; BDJ) with the random-2D-order literature (Winkler *Random orders*; Brightwell *Models of random partial orders*; Brightwell–Luczak arXiv:1510.05612 §2) at `…null_copula_dichotomy.md:388, 396-397, 410`. Nothing in §9-§11 claims novelty over those, correctly.

- **Analytic / continuum target:** the continuum benchmark is the 1+1 conformal family `g_eps = e^{2 eps psi} g_0 / Z(eps)` on a null-coordinate box, whose volume measure is `(Omega/2) dU dV` so that the sprinkling density *is* the conformal factor without exponents (`…null_copula_dichotomy.md:30-38`) — this is what makes the reduction of §1.1 exact rather than approximate. The reduction to `[0,1]^2` is order-theoretically legitimate: the rank map `T=(F,G)` is a separate-coordinate increasing homeomorphism, hence an order isomorphism for the product order, so labelled poset and permutation laws are unchanged (Lema A, `…null_copula_dichotomy.md:54-78`). The gauge fixing `mu_0 = du dv` is performed at `eps = 0` (the reference metric), so it cannot be tuned by the perturbation — freeze-clean. The target endpoint is `I_N^{[P]}/I_N^{Pi} -> 1` at rate `N^{-1/2}` (roadmap `…hoja_de_ruta_septiembre_2026.md:66-71`; frozen Teorema 5 `…modular_fiber_score.md:1129-1136`). Physical relevance of the 1+1 target is anchored: EGS note that the induced (1+1) Schwarzschild metric has constant determinant in `(t,r)`/`(t*,r)` hence constant sprinkling density (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:135`) — the non-uniformity that the order sees appears only after passing to null coordinates, which is exactly the frame this document works in.

- **Caveats:**
  - **PI point 5 (mine) — no missing cross term, and it is already anchored.** The general fixed-rank score with the quantile-motion terms *explicit* is already in the repo: `s_tau(x,y) = d_tau g + a1(w) d_w g + a2(v) d_v g` with `d_tau g = D - E[D|w] - E[D|v] + E[D]` labelled "(ANOVA) doble centrado" (`research_program/work_packages/wp4_ibar_direct_score_derivation.md:300-312`). At the null `q_0 ≡ 1`, so `d_w g = d_v g = 0` and only the double-centred term survives — a third independent derivation of (3.5). The `O(eps)` quantile shift multiplies an `O(eps)` spatial log-gradient, hence `O(eps^2)`, exactly as asserted at `…geometric_tangent_classification.md:861-864`.
  - **PIT `eps`-dependence is harmless, for the reason the document gives.** The identity `law(Pi_N | q_eps) = law(Pi_N | c_eps)` holds *for each `eps` separately* because `F_{U,eps}, F_{V,eps}` are strictly increasing (`q_eps > 0`), so it can be differentiated in `eps` (`…geometric_tangent_classification.md:359-362`, reusing Lema A `…null_copula_dichotomy.md:54-78` — that reuse claim is real, I verified §§1-2 provide both the fixed-`N` conditioning lemma, itself citing `docs/manuscript_limits_draft.md:273`, and the order-preserving PIT). Rank invariance is complete. **No falsification found on point 5.**
  - **Rigor gap, repairable in one line (condition).** §3.2 (`:279-283`) applies a chain rule through `d_u log q_0` although §1.1 (`:79-84`) assumes only `psi ∈ C(D)`. The step survives — `(eps,u,v) ↦ 2 eps psi(u,v) - log Z(eps)` is jointly differentiable at `(0,x,y)` with vanishing spatial part by uniform continuity of `psi` — but the document does not say so. Require either that sentence or `psi ∈ C^1`.
  - **`I_N^{[P]}` is used but never defined (condition).** Eq. (11.6) writes `1 - I_N^{[P]}/I_N^{Pi}` (`:1120-1128`), whereas the frozen theorem only defines `q_N = 1 - L_N/I_N^{Pi}` (`…modular_fiber_score.md:1111`); `I_N^{[P]}` appears nowhere in that file. The identity `I^{[P]} = I^{Pi} - L_N` is true (law of total variance, plus `d_eps log p_eps([P])|_0 = E_0[S | [P]]` by differentiating a finite fiber sum) but is proved in neither document. It is an **inherited** gap — the roadmap states the frozen theorem in the same `I^{[P]}` form (`…hoja_de_ruta_septiembre_2026.md:66-71`) — so it is not created here, but the gate should not launder it: require the one-line lemma stated once and cited.
  - **§9.5 over-reach (condition).** "la **única** equivalencia marginal que sobrevive sobre el generador es `ker P`" (`:782-784`, repeated in §12 `:1150-1152`) is proved only at the level of the copula tangent (`P psi = P psi' ⟺ psi - psi' ∈ A`, immediate from Prop 9.1). Upgrading it to the *observable* requires injectivity of `h ↦ (S_{N,·})_{N≥1}`, which is nowhere established: at `Pi` level it is the linearisation of Teorema D, itself only `PROVED_MODULO_FUENTES_VERIFICADAS` (`…null_copula_dichotomy.md:140`), and at `[P]` level the even obstruction `b` is explicitly **OPEN** (`…null_copula_dichotomy.md:230-263`). Reword to "at the level of `h_psi`" or mark `[UNVERIFIED]`.
  - **Proposición 9.4 is true and its hypotheses are stronger than needed.** Absolute continuity does suffice (`phi' chi' = 1` a.e. → by Fubini fix a good `v`, `chi'(v) ≠ 0`, so `phi' ≡ a` a.e., and AC gives `phi(u) = au`, `a = 1`), `:775-780`. In fact measure preservation on rectangles forces `phi^{-1}(s)·chi^{-1}(t) = st`, and `t=1` gives `phi = id` with no AC at all. No failure; the result is robust.
  - **Teorema 6 cites the wrong lemma in the degenerate case (condition).** The step `(c)⇒(a)` invokes Lema 9.2 (`:736-738`), whose hypotheses are `lambda ≠ 0` and `f ≠ 0` (`:678`); for `lambda = 0` those fail. The needed fact is Prop 9.1 point 4 (`int f = 0 ⇒ f⊗f ∈ R ⇒ P(f⊗f) = f⊗f`), which is unconditional. Swap the citation. Separately: `int f^2 > 0` is **not** used in the equivalence (a)⟺(b)⟺(c) — it is dragged; it becomes load-bearing only in §9.5(ii) (faithful coordinate) and in Teorema 7 (H3 limit `c > 0`). Say so.
  - **PI point 4 (H3 near the extremes) survives.** `Var(U_{(i)}) ≤ 1/(4(N+2))` is uniform in `i` because `i(N+1-i) ≤ ((N+1)/2)^2`, and Chebyshev is distribution-free, so the asymmetry of `Beta(i, N+1-i)` at `i=1, N` is irrelevant; `delta_N = (N+2)^{-1/4}` gives the stated `‖f‖_inf/(2 sqrt(N+2))` uniformly in `i` (`:988-1012`). I re-derived (11.4): `(1/N)sum_{i≤N} g(p_i) - int g = ((N+1)/N)(S - int g) + (1/N)int g - g(1)/N`, whose modulus is bounded by the document's right-hand side; `g = f^2 ≥ 0` makes the un-absolute-valued `int g` term legitimate. **No falsification found on point 4.**
  - **PI point 1 survives.** `M_u M_v = M_v M_u = bar psi·1`, idempotence, `P^2 = P`, `ker P = A`, `ran P = R`, `A ∩ R = {0}`, `A ⊕ R = C(D)` all check out; everything is continuous on a compact square so Fubini and the integral interchanges are unproblematic. **No falsification found on point 1.**
  - **Novelty hygiene (condition, S3-facing).** Prop 9.1 / Teorema 6 are the classical two-way ANOVA (Hoeffding) decomposition of `C([0,1]^2)`; the repo already uses that name for the identical object at `…wp4_ibar_direct_score_derivation.md:305-308`, while §9 presents it under fresh theorem numbers with no cross-reference. Add the cross-reference and the ANOVA/Hoeffding label so the S3 priority audit does not inherit an inflated novelty surface.
  - **Minor:** (11.6) drops the frozen theorem's `N ≥ N_A` restriction attached to `Pr(B_N) ≤ C_A/N` (`…modular_fiber_score.md:1036-1045`); the substitution `M_* → ‖f‖_inf` is a valid weakening since `M_* ≤ ‖f‖_inf` and the bound increases in `M`; Lema 11.1 correctly excludes `lambda = 0` (`:1115`), where `q_N` is `0/0`. Also: for members of the class with merely continuous `f`, the pointwise linearised curvature `lambda f'(u)f'(v)` does not exist, so the *geometric* reading of Teorema 6 needs `f ∈ C^1` — which is what roadmap §2.2 asked for ("`f` suave", `…hoja_de_ruta_septiembre_2026.md:152`) and what both witnesses satisfy.
  - **Verdict from this seat: `GATE_PASS_WITH_CONDITIONS`.** The order-theoretic content of S1 is sound; I found no falsification on PI points 1, 4 or 5, and points 2 and 3 yield defects of citation and of wording, not of substance. Conditions, all textual and none requiring new mathematics: (1) add the continuity justification for the §3.2 chain rule (or assume `psi ∈ C^1`); (2) state and prove once the identity `I_N^{[P]} = I_N^{Pi} - L_N`, or restate (11.6) in the frozen `q_N` notation; (3) restrict the §9.5/§12 uniqueness claim to the `h_psi` level, citing the open `b` obstruction at `[P]` level; (4) in Teorema 6 cite Prop 9.1(4) instead of Lema 9.2 and state where `int f^2 > 0` is actually used; (5) add one explicit sentence that `Pi_N` is realizer-dependent and that only (11.6) is order-only, with the citation for rank ⊥ order-statistic independence; (6) cross-reference `wp4_ibar_direct_score_derivation.md:300-312` and name Prop 9.1 as the ANOVA/Hoeffding decomposition; (7) carry `N ≥ N_A` into (11.6). S2 must stay closed until these land: nothing here authorises seeds, simulation, the asymmetric `f⊗g` sector, or any horizon statement.

### Mathematical logic brief

**Formal status**

- **Machine-checked: none.** `formal/HorizonFormal/` covers posets, ideals, cofinal chains, ends, accessibility only (`formal/HorizonFormal/README.md:34-40`); `grep -rli "copula\|fisher\|score\|permut" formal/` returns **no hits**, and `grep -rn sorry formal/` returns nothing. So `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` is a **prose-proof** token with zero formal-artefact backing. The token block (`...classification.md:1158-1172`) should not be read as carrying the same warrant as the Lean track.
- **Definitions** (not results): §1.1 normalisation `mu_0 = du dv` and `Z(eps)` (lines 61-95); the four-level notation of §1.2 (134-140); `A`, `R` (641-649); `P` (624-628).
- **Proved theorems (I verified line by line, all correct):** Prop 9.1 (654-671) — all six items valid, no continuity/measurability/Fubini failure anywhere, since every integrand is continuous on a compact; Theorem 6 (700-742) — the *statement* is true, see defects below in the *proof*; §10 closed-form falsifier (836-890) — I re-did the algebra, `2xy - x - y + 1/2 = 2(x-1/2)(y-1/2)` holds and no O(eps) cross term is lost, because `Q_U Q_V = xy + O(eps)` enters already multiplied by `eps` (line 863-864 is sound); Theorem 7 H1/H2/H3 (951-1047) — Chebyshev bound `omega_f(delta) + ||f||_inf/(2(N+2)delta^2)` is uniform in `i` **including i=1,N** because `Var(U_(i)) <= 1/(4(N+2))` is an `i`-free bound, `delta_N=(N+2)^{-1/4}` is legitimate for all `i`, and the Riemann bookkeeping (11.4) with the `i=N+1` cut is arithmetically correct; (11.5) I re-derived `(m-1)m(m-2)/12` and `(N-1)/(12(N+1))` — exact.
- **True statement with a defective proof:** Prop 9.4 (770-780). It is true and in fact provable *without* absolute continuity (restrict measure preservation to rectangles `A x [0,1]`: `lambda(phi^{-1}A) = lambda(A)` for all Borel `A`, then `A=[0,t]` gives `phi^{-1}(t)=t`). The written proof instead asserts an uncited a.e. Jacobian identity and then misnames the key step: "fijando `v` en un punto de Lebesgue" is the wrong notion — what is needed is Fubini plus a `v_0` at which `chi'(v_0)` exists **and lies in (0, inf)** (guaranteed only because AC gives `int chi' = 1`). Repairable, but as written it is a gap.
- **Rhetorical claim, not a theorem:** lines 782-787, "la **única** equivalencia marginal que sobrevive sobre el generador es la aditiva `ker P = A`". See quantifier section.
- **Conditional corollary mislabelled as out of scope:** (11.6) at 1120-1132.
- **Correctly demoted:** §9.6 asymmetric sector (791-803) — the algebra genuinely does transfer (`P(f (x) g) = f (x) g` needs `int f = int g = 0`, both hypothesised), and it is explicitly not promoted. Compliant.

**Quantifier / dependency order**

- The load-bearing order is: `f` and `lambda` are chosen **before** `psi`; `N` and `pi` come last. Theorem 6 quantifies `for all lambda in R, for all f (with int f = 0, int f^2 > 0), for all psi: (a)<=>(b)<=>(c)` — this order is respected and no post-hoc freedom enters, because nothing in §9 depends on `N` or on data.
- **Degenerate `lambda = 0` is inside the quantifier range and breaks two citations.** Lemma 9.2 (678-689) explicitly requires `lambda != 0` and `f != 0`. Theorem 6's proof invokes it twice — `(c)=>(a)` at line 737 and, via the same identity, `(a)=>(c)` at 739-740 — with `lambda` ranging over all of `R`. At `lambda = 0` the lemma's hypotheses fail. The conclusion still holds trivially (`P0 = 0`), so this is a **citation defect, not a false step**, and the minimal repair is one line: replace "por el Lema 9.2" with "por el punto 4 de la Proposición 9.1, ya que `int f = 0` implica `(f (x) f)_U = (f (x) f)_V = 0`" — which needs neither `lambda != 0` nor `f != 0`.
- **`int f^2 > 0` is carried, never used in Theorem 6.** I checked every step of 734-742: the equivalence holds verbatim even for `f == 0`. It *is* genuinely used downstream — §9.5(ii) normalisation (763), H3's non-degenerate limit `c > 0` (948), and the denominator of (11.6) (1125). So it is not decoration, but it makes Theorem 6 formally weaker than what is proved, and the theorem is **not vacuous** in any degenerate case.
- `lambda != 0` **is** correctly guarded where it matters for the Fisher conclusion (line 1115 and Lemma 11.1 at 1107-1108). Good discipline.
- (5.2)'s legitimacy depends on an ordering fact the document states only implicitly: the chamber `C_pi` (line 380) is defined by ranks in **copula coordinates** and is therefore `eps`-independent, so no moving-domain boundary term arises. That is the right structure (compare the explicit fixed-domain reparametrisation `wp4_ibar_direct_score_derivation.md:200-216`), but it should be said out loud.

**Equivalence claims**

- **Genuinely bilateral and proved:** `(a) <=> (b)` (it is `h_psi = 2 P psi` plus `2 != 0`); `(a) <=> (c)` (modulo the `lambda=0` citation repair); Prop 9.1's five set identities; Lemma 9.2's `iff` (within its stated hypotheses `lambda != 0`, `f != 0` — correctly guarded there). Corollary 9.3 is a correct contrapositive.
- **One-way / unproved:** §9.5(ii) (762-766). "`lambda` queda unívocamente determinado y `f` salvo el signo global" is asserted with no proof; it is true for `lambda != 0` (uniqueness of a rank-one symmetric kernel with `||f||_{L^2}=1`), and it is **false at `lambda = 0`**, where every `f` yields the same class `A`. The sentence "`(lambda,[f])` es una coordenada fiel de la clase" therefore fails on a non-empty part of the quantifier range it inherits from Theorem 6.
- **Semantic, not proved:** lines 782-787. Prop 9.4 quantifies only over *separated, strictly increasing, AC, measure-preserving* maps. It does not cover the swap `(u,v) |-> (v,u)`, which preserves `du dv` **and** the componentwise order of `D` (`...classification.md:62-65`) and acts non-trivially on `A` (`alpha(u)+beta(v) |-> alpha(v)+beta(u)`); nor the reflection `(u,v) |-> (1-u,1-v)`, a `mu_0`-preserving order anti-automorphism. Neither disturbs the *symmetric* rank-one sector, but both falsify the literal word "única" over any unrestricted reading. The deeper defect is that "equivalencias marginales pertinentes" (imported from `docs/hoja_de_ruta_septiembre_2026.md:2.2`) is **never defined**, so the universal claim has no quantification domain. What *is* proved and is exactly what the gate needs is the fibre statement: `{psi : h_psi = h}` is precisely a coset of `A` (Prop 9.1 + Theorem 6). That should replace the sentence.
- (11.6) substitutes `||f||_inf` for the frozen `M_*` of Theorem 5 (`wp6_d2_modular_fiber_score.md:1092-1120`). This is a valid *weakening* (the bound is increasing in `M_*` and `M_* <= ||f||_inf` by H1) but the monotonicity is never stated. `c = int f^2` matches exactly. Hypothesis match with the frozen theorem is otherwise clean: Theorem 5 requires a **deterministic** triangular array, and `a_{i,N} = E[f(U_(i))]` is deterministic; H2 must be *exact* (it feeds (7.4)), and §11.2 delivers exactness, not asymptotics.

**Type / object discipline**

- The four-level separation (§1.2, 134-145) is the document's strongest formal feature and it holds throughout: `psi` (generator, a function), `dot g_0` (a tensor), `t_psi`/`h_psi` (log-density tangents, functions), `S_{N,psi}` (a function on `S_N`). The §6 audit of the two `lambda` conventions is a **type error found and correctly diagnosed**, not a mathematical error, and the fix is proposed, not applied (line 519-520) — correct freeze discipline.
- **Category slip, minor:** line 616-619 writes `M_u M_v = M_v M_u = barpsi . 1`, equating an *operator* with a *function*. Should be `(M_u M_v)psi = barpsi . 1` for all `psi`. The underlying commutation is true as operators (I checked both compositions on arbitrary `psi in C(D)`), so `P^2 = P` at line 632 stands.
- "proyector de rango infinito" (633-634) and "cerrada" (744) are true but unproved in situ; both follow from `||P|| < inf` (kernel and range of a bounded projection are closed) and from `f (x) g in R` for all centred `f,g`.
- Sets vs classes: `A` and `R` are genuine closed subspaces, `lambda f (x) f + A` a genuine affine coset — no ideal/quotient confusion anywhere. The physical objects (metric, sprinkling) are kept strictly upstream of §9; §9-§11 are pure real analysis. `NO_RECONSTRUCTION_CLAIM` and `NO_UNIVERSALITY_CLAIM` are respected in the text I read.

**Caveats**

- **[C1 — must fix before the gate]** Theorem 6's proof applies Lemma 9.2 outside its own hypotheses at `lambda = 0` (`...classification.md:678` vs `:737` and `:739-740`). Replace the citation with point 4 of Prop 9.1, or add the parenthetical "para `lambda=0` ambos miembros se anulan y la afirmación es trivial". Statement survives unchanged; only the proof text changes.
- **[C2 — must fix]** §9.5(ii) (`:762-766`) must be restricted to `lambda != 0`, and the uniqueness of `(lambda,[f])` must be proved (one line from rank-one kernel uniqueness) or downgraded to a remark. As written it is false on part of Theorem 6's quantifier range.
- **[C3 — must fix]** Replace lines `:782-787` with the proved fibre statement (`{psi : h_psi = h} = psi_0 + A`), and restrict the "única equivalencia" wording to the class Prop 9.4 actually quantifies over. The swap `(u,v)|->(v,u)` is a `mu_0`-preserving order automorphism outside that class; the current sentence is an unquantified rhetorical jump, not a theorem.
- **[C4 — should fix]** Prop 9.4's proof (`:775-780`): cite the AC change-of-variables that yields `phi'chi' = 1` a.e., and replace "punto de Lebesgue" with "por Fubini, elíjase `v_0` tal que la identidad valga para c.t. `u` y `chi'(v_0) in (0,inf)`". Preferable: substitute the rectangle argument, which proves the same proposition without AC.
- **[C5 — should fix]** §5.2's justification "La acotación de `h_psi` permite derivar bajo la integral" (`:380-381`) bounds the derivative *at* `eps=0`, not uniformly on a neighbourhood, which is what dominated differentiation requires. This falls below the repo's own established standard for exactly this manoeuvre (`wp4_ibar_direct_score_derivation.md:395-420`, Lema 9.1, a four-step compactness argument the PI demanded in a prior round). Add: `c_eps` and `partial_eps c_eps` are jointly continuous on `[-eps_0,eps_0] x D` (compact), hence uniformly bounded; `C_pi` is `eps`-independent. Also state explicitly that `q_eps = e^{2 eps psi}/Z > 0` for **all** `eps`, which is what makes the PIT strictly increasing and the rank-invariance argument of `:359-362` complete — the `eps`-dependence of the PIT is harmless because laws are compared at equal `eps`. I find no hidden `eps`-dependence leak here.
- **[C6 — scope, must be resolved by the chair]** (11.6) at `:1120-1132` **is** the S2 target of `docs/hoja_de_ruta_septiembre_2026.md:3.1` (`I^{[P]}/I^Pi -> 1` for the S1 class), in rate form, conditional on frozen Theorem 5 and on the §7.5 projection identity — while `:1154` and the token `S2_NOT_OPENED` assert the opposite. Either relabel (11.6) as "corolario condicional; no es el entregable modular de §3.3" or drop the token. As a logician I flag this as an inconsistency between the proved content and the declared scope, and it is precisely the class of thing a gate audit exists to catch.
- **[C7 — record]** The roadmap requires `f` *suave* (`hoja_de_ruta_septiembre_2026.md:2.2`); the document proves everything for `f in C[0,1]` only. This is a strict generalisation (harmless, in fact better), but the gate would then authorise a **larger** class than the roadmap named. Record the deviation explicitly rather than let it pass silently.
- **[UNVERIFIED]** I did not re-verify the internals of frozen Theorem 5, of `(7.4)`/`(7.6)`, or of the score-projection identity `I^{[P]} = I^Pi - L_N` of `wp6_d2_modular_fiber_score.md` §7.5; §11.5 cites them without re-proof, which `hoja_de_ruta_septiembre_2026.md:3.3` permits ("citarlas con hipótesis verificadas una por una") — but the hypothesis-by-hypothesis verification of §7.5 is *asserted* at `:1110-1113`, not exhibited.
- **My recommendation: GATE_PASS_WITH_CONDITIONS**, conditions C1-C6 (C7 as a recorded note). I found **no false theorem** in §§9-11: every statement I checked is true, and the two genuinely broken sentences (`:766` faithfulness at `lambda=0`; `:782-787` "única equivalencia") are *auxiliary commentary*, not load-bearing for Theorem 6 or Theorem 7. But `PROVED` here is a logical gate authorising S2, so a proof that cites a lemma outside its hypotheses and an undefined universal quantifier must not cross it unrepaired. No condition requires new computation, new seeds, or touching any sealed instrument.

### Physicist brief

- **Coordinates & patch:** The audited step must use — and does use — flat null coordinates on a **Minkowski** causal diamond, reduced to `D=[0,1]^2` with `(u,v)⪯(u',v') ⟺ u≤u', v≤v'` (`research_program/work_packages/wp6_d2_geometric_tangent_classification.md:57-66`). The reduction is **legitimate and loses nothing at the level of order**: in `d=2` a null-coordinate box induces exactly the product order (`research_program/work_packages/wp6_d2_null_copula_dichotomy.md:41-43`), and the rank map `T=(F,G)` is an increasing homeomorphism in each coordinate separately, hence an order isomorphism, so the labelled poset is literally unchanged (`wp6_d2_null_copula_dichotomy.md:52-60`). What is discarded — the two marginals — is exactly the *separable* content of the conformal factor, and separable ⟺ **flat** (`wp6_d2_null_copula_dichotomy.md:82-100`); so the discarded directions carry zero scalar curvature. This is **not** the coordinate system of the sealed benchmark, which is 1+1D Schwarzschild in Eddington–Finkelstein `(t*,r)` with `det g = -1` (`docs/preregistration.md:61-62`) on a *finite* tall box `t_edge=6.0, r_edge=1.2, r_center=0.7`, area 7.2, `r_S=2M=0.5` (`docs/preregistration_001_addendum.md:39-40`). Finiteness there forfeits any asymptotic event-horizon claim: at fixed `t_edge` the exterior mode of `O` is limited by box size, not by the horizon, and the project has already frozen `NO r_h → 2M asymptotic claim` (`docs/preregistration_001_addendum.md:74-84`). The audited document forfeits *more*: it has no `ρ`, no `ℓ=ρ^{-1/2}`, no `2M`, so it cannot speak to `θ_loc = 2ℓ_λ/(2M)` at all.
- **Physical meaning of the signal:** In the sealed benchmark the order-only observable tracks `r=2M` because timelike chains starting inside the horizon must reach `r=0` in finite proper time and therefore **terminate**, while chains starting outside are limited only by the box — producing a sharp transition in longest-chain length at the horizon and a **bimodal** distribution over minimal elements, extractable without any reference to coordinates (Eichhorn–Gamito–Stokes, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-193`, `:463`). The sealed instrument uses the cardinality variant `O(i)=|future(i)|` (`docs/preregistration_002.md:44-45`), which the same paper flags as more boundary-sensitive (`:193`). **The audited document contains none of this.** Its observable is a first-order Fisher score `S_{N,ψ}(π)` about the *flat* null point `ε=0`; singularity-truncated futures are a global/boundary effect, not a first-order conformal tangent, so the two observables are physically disjoint objects. Nothing in WP6-D2 supports or weakens the horizon benchmark.
- **Sprinkling domain:** Declared region `D=[0,1]^2` with reference measure `μ_0 = du dv := dvol_{g_0}/V_0`; **Poisson sprinkling conditioned to `N` points**, hence `N` iid draws from `μ_ε = q_ε du dv`, `q_ε = e^{2εψ}/Z(ε)` (`wp6_d2_geometric_tangent_classification.md:107-124`), reusing the conditioning lemma of `wp6_d2_null_copula_dichotomy.md` §§1-2 (itself citing `docs/manuscript_limits_draft.md:273`). **No intensity, no `ρ`, no `N` levels, no seeds, no simulation** — verified: the only occurrences of "simulación"/"semilla" are the negations at `:18`, `:1140`, `:1155`. Forfeited by construction: absolute scale (the `1/Z(ε)` normalisation plus conditioning on `N` removes exactly the global-scale information, consistent with `CLAUDE.md:24-26`), Poisson number fluctuations, and any statement about the discreteness scale.
- **Claim boundary:** The verdict I can support claims **only** that, for conformal deformations of a *flat* 1+1 diamond, the copula tangent is `h_ψ = 2𝒫ψ` and the rank-one-symmetric class is exactly the coset `ψ = α(u)+β(v)+λ f(u)f(v)` with `∫f=0` (`:698-745`). It does **NOT** claim: metric reconstruction; sufficiency w.r.t. continuous coordinates; anything about Schwarzschild, `r=2M`, trapped regions or horizons; anything in 2+1 or 3+1; any universality over generic conformal tangents. Roadmap §3.2 already forbids exactly these (`docs/hoja_de_ruta_septiembre_2026.md:240-248`), which is the correct ceiling. The regular-black-hole caveat from the anchor paper is orthogonal but must stay on record: the longest-chain diagnostic **fails** for regular (e.g. Hayward) black holes, because timelike curves can be continued for arbitrarily long proper time inside the horizon, so no partition of the causet is expected (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:195`); the benchmark's signal is a *geodesic-incompleteness* signal, not a horizon signal per se.
- **Caveats:**
  - The `d=2` volume identity is **correct**: for a 2×2 metric `det(m g_0) = m² det g_0`, so `√|det|` scales by `m` and `dvol_{m g_0} = m dvol_{g_0}` (`:98-105`). Consequently `vol_{g_ε}(D) = V_0` exactly. Note this is `m^{d/2}` in general — the clean linear form is a `d=2`-only fact and does not survive a 2+1 extension.
  - The "conventional factor in front of `du dv`" is handled correctly (`:74-77`): with `g = -Ω dU dV` one has `g_{UV} = -Ω/2`, `det g = -Ω²/4`, `dvol = (Ω/2) dU dV` (`wp6_d2_null_copula_dichotomy.md:26-30`); that constant is a *global* factor and cancels identically in `μ_0 = dvol_{g_0}/V_0`. No hidden physics.
  - **The `α+β` directions are not "just gauge" — they are exactly the flat directions, and this is the strongest available defence of the construction, yet the document never says it.** `R = 0 ⟺ ∂_U∂_V log Ω = 0 ⟺ log Ω = α(U)+β(V)` (`wp6_d2_null_copula_dichotomy.md:96-100`), and that same set is exactly the orbit of `G = Diff⁺(I)×Diff⁺(I)`, infinite-dimensional (`:124-129`). So `ker 𝒫 = 𝒜` discards zero curvature content. Instead, `:83-84` says only "additional geometric regularity to define curvature does not intervene in this substep". **Condition:** cite `wp6_d2_null_copula_dichotomy.md` §3 in §1.1/§9.2 so the kernel is identified as *flat*, not merely as *marginal*.
  - `∂_u∂_v ψ = λ f'(u) f'(v)` for the classified class, so the retained content is a **rank-one linearised curvature profile**; `∫f=0` (Lemma 9.2, `:676-694`) is then the physical solubility condition on that profile, not a normalisation. *[This differentiation is my own, from the anchored formula at `wp6_d2_null_copula_dichotomy.md:97` with `log Ω = 2εψ + const`; not stated in the audited file — treat the phrasing as [UNVERIFIED] until the document derives it.]*
  - **Over-claim risk in wording:** `:1151` calls the class "infinito-dimensional". True of the coset `λ f⊗f + 𝒜`, but the *gauge-invariant, curvature-carrying* content is one rank-one mode, faithfully coordinatised by `(λ,[f])` (`:770-780`). A reader can take "infinite-dimensional" as breadth. **Condition:** qualify as "infinite-dimensional as a coset; rank-one modulo the flat kernel".
  - **The document is Minkowski-pure and says so implicitly but never explicitly.** Zero hits for `schwarzschild|horizon|curvatur` (other than a Riemann *sum* at `:1028-1029`). In a repo whose headline is 1+1D Schwarzschild horizon recovery (`CLAUDE.md:7-8`), the §0 token block carries `NO_UNIVERSALITY_CLAIM` and `S2_NOT_OPENED` but **no `NO_HORIZON_CLAIM`**. **Condition (my principal one):** add `MINKOWSKI_DIAMOND_PERTURBATIVE`/`NO_HORIZON_CLAIM` to the §0 and §12 token blocks, mirroring roadmap `:246` and `:498`.
  - **Conformal flatness cuts both ways.** In `d=2` every metric is conformally flat, so `ψ` *is* the whole local geometry — classifying `ψ` genuinely classifies the geometry, which makes the result more meaningful than a generic conformal sub-sector. But that same fact is why the invisibility group is infinite-dimensional in `d=2` and finite-dimensional (Liouville) for `d>2`, which is precisely the reason HKMM/Braun/Madsen exclude `d=2` (`wp6_d2_null_copula_dichotomy.md:130-133`). The result must never be advertised as generic causal-set geometry.
  - **The factor-2 mismatch is physically real, not bookkeeping.** It descends from the `d=2` coincidence that the conformal factor *is* the sprinkling density with no extra exponent (`wp6_d2_null_copula_dichotomy.md:32-34`). Convention B (`:453-520`) is the right choice. But the document emits `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` against roadmap §2.2, which still states Convention A (`docs/hoja_de_ruta_septiembre_2026.md:138-142`) — i.e. it satisfies the gate criterion under a redefinition it proposes itself. Refusing to unilaterally edit the roadmap is the honest move (`:519-520`), but **the discrepancy must be resolved in writing by the PI before the token is read as clearing §2.2**.
  - **The proposed S2 target is physically well-posed and is narrower than the mathematics, not broader.** `I_N^{[P]}/I_N^{Π} → 1` compares *unlabelled poset vs rank permutation* — the labelling quotient — and says nothing about how much the permutation retains of `ψ`. Since `ker 𝒫 = 𝒜` is exactly invisible at every `n` (Theorem C, `wp6_d2_null_copula_dichotomy.md:105-120`), the geometry→permutation channel already has an infinite-dimensional kernel. Roadmap §3.2's qualifier "*disponible en la permutación de rangos*" (`:236-239`) is **load-bearing** and must survive verbatim into any README/abstract; without it the sentence becomes "the poset retains the geometry", which is false.
  - **Scope-creep vector to watch:** the copula machinery requires the patch to be a *null-coordinate rectangle* with `Ω>0` continuous (`wp6_d2_null_copula_dichotomy.md:22-24`). The sealed benchmark region is a rectangle in `(t*,r)`, **not** in `(U,V)`. So this formalism does not currently apply to the sealed domain, and no bridge between the two should be asserted without a separate derivation. Gate authorises S2 only (`docs/hoja_de_ruta_septiembre_2026.md:208`); S4-S7 (`:298`, `:378`) remain closed, and `ASYMMETRIC_RANK_ONE_SECTOR = CLASSIFIED_BUT_NOT_PROMOTED` (`:789-803`) must be preserved verbatim.
  - **Physics-seat verdict: `GATE_PASS_WITH_CONDITIONS`** — coordinates, volume identity, convention handling and sprinkling domain are correct; the four conditions above (flat-kernel citation, `NO_HORIZON_CLAIM` token, "rank-one modulo kernel" qualifier, written resolution of the factor-2 convention against roadmap §2.2) are text-level and touch no sealed instrument, no seed and no threshold. Seal `6e2c3888…` matches `docs/preregistration_002.md:7-8` and must remain untouched by this commit.

## 5. Falsifier attack

> Nota del chair: el falsador recibió los cuatro informes de la ola 1 en un fichero de trabajo
> (`wave1_briefs.md`, en el scratchpad de la sesión, no versionado). Sus referencias del tipo
> `wave1_briefs :74` apuntan a ese fichero; el contenido citado es el reproducido íntegro en §4.

### Falsifier attack

- **Concrete failure modes:**
  1. **Teorema 6's proof is not actually a proof of what it states, as written.** `research_program/work_packages/wp6_d2_geometric_tangent_classification.md:698-753` quantifies `lambda in R` (all reals, including 0), then its `(c)=>(a)` step invokes "Lema 9.2" (`:698-704`, stated for `f != 0`, `lambda != 0`) to cover the *entire* range. At `lambda=0` the cited lemma's hypotheses fail — the citation is outside its own domain. Both the logician and mathematician briefs independently found this (wave1_briefs `:74`, `:50`), and both call it "repairable in one line," but as *literally committed*, the token `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` (`:39`, `:1162`) certifies a theorem whose written proof has a genuine hole in part of its own stated quantifier range. A "PUERTA LOGICA" gate should not be crossed by a proof text with an unrepaired logical gap, however trivial the repair.
  2. **A load-bearing sentence in §9.5 is asserted false on part of the theorem's own domain.** "`lambda` queda unívocamente determinado y `f` … es una coordenada fiel de la clase" (`:9.5(ii)`, ~`:770-775`) is FALSE at `lambda=0`, where every `f` gives the identical class `A` (logician, wave1_briefs `:82`). This is not a stylistic nit — it is presented as part of the "gauge exacto" that closes S1's obligation (roadmap §2.2's "estable bajo las equivalencias marginales pertinentes"). A document that contains a demonstrably false universal claim inside the very section meant to nail down uniqueness cannot be waved through as "PROVED" without that sentence being corrected first.
  3. **The "única equivalencia" claim in §9.5 is also false as literally written**, refuted by two explicit counterexamples the logician supplies: the coordinate swap `(u,v)->(v,u)` and the reflection `(u,v)->(1-u,1-v)`, both `mu_0`-preserving order automorphisms/anti-automorphisms outside the class Proposición 9.4 quantifies over (wave1_briefs `:83`, `:97`). The document's own §9.5 text (`:786-789`) uses the word "única" unqualified. This is the second literally-false universal sentence in the same short section that the gate is supposed to authorize on the strength of.
  4. **Teorema 6 is, in its true content, close to a restatement of "the fibre of a linear projection is a coset of its kernel."** §9.1-9.2 build `P = (I-M_u)(I-M_v)` and prove `ker P = A`, `ran P = R`, `C(D) = A ⊕ R` — a completely standard double-centering / two-way-ANOVA(Hoeffding) decomposition that the repo itself already uses under a different name (`wp4_ibar_direct_score_derivation.md:305-308`, flagged uncredited by the mathematician, wave1_briefs `:53`). Lema 9.2 is a one-line computation (`int f(u)f(v') dv' = f(u)\int f`). Teorema 6 then combines these two elementary facts into "the preimage of `lambda f⊗f` under `P` is `lambda f⊗f + A`" — which *is* exactly "coset of the kernel," dressed with a theorem number. **Adjudication: the mathematical content is genuinely elementary linear algebra; it is not vacuous (Corolario 9.3, the non-solubility direction, has real content, and identifying `ker P` with the flat/gauge directions is a real geometric fact, per physicist wave1_briefs `:116`), but calling it "PROVED" and treating it as a "puerta lógica" for a new research phase substantially inflates its epistemic weight.** A committee should not authorize a phase transition on the rhetorical strength of a "Teorema" label when the underlying content is a textbook decomposition applied to a case chosen precisely because it is guaranteed to be tractable.
  5. **The S1/S2 boundary is not real — S2's target is already substantively present inside the S1 document.** The logician's C6 (wave1_briefs `:100`) states plainly: `(11.6)` — inside the audited S1 document — already IS the S2 rate target of roadmap §3.1 ("`I_N^{[P]}/I_N^{Pi} -> 1`"), conditional only on the already-frozen Theorem 5 and the §7.5 identity, while the token block simultaneously asserts `S2_NOT_OPENED` (`:35` region) and roadmap §3.1 says S2 "sólo se abre si S1 termina PROVED" (`docs/hoja_de_ruta_septiembre_2026.md:208`). This means the committee is being asked to authorize opening a phase whose "first complete theorem" has effectively already been assembled inside the phase being closed — the gate is decorative in the direction that matters (it doesn't stop S2's content from existing pre-authorization), while being treated as load-bearing in the direction that matters to governance (it is used to justify why S2 can now start). This is the single most dangerous convergence-blind-spot: all four wave-1 experts flagged pieces of it (C3, C6) but none drew the conclusion that the gate itself may be theater around a fait accompli.

- **Ground-truth leakage:** None found via the literal channel (no simulation, no seeds, no embedding lookup — `wp6_d2_geometric_tangent_classification.md` is pure closed-form analysis, confirmed independently by three of four wave-1 briefs and by direct inspection of §10). The closer-to-real hazard is a *methodological* analogue of leakage, not a data one: the target subclass (rank-one symmetric, `int f=0`) was chosen in roadmap §2.2 specifically so that it slots into the **already-proved** frozen Theorem 5 (H1/H2/H3), i.e., the geometric class was picked to fit a pre-existing statistical result rather than derived independently and then found to satisfy it by surprise. This is not ground-truth leakage in the benchmark sense (no hidden embedding is consulted), but it is target-selection circularity: success was close to guaranteed by construction before any derivation began, which should temper how much evidential weight "PROVED" is allowed to carry toward "the geometry-to-causet program is on track."

- **Freeze violations:** No sealed instrument, threshold, or seed is touched (confirmed: `make verify-seal` hash matches `docs/preregistration_002.md:7-8`; no `nachocausal/thresholds.py` diff). However: (a) the document self-certifies under a **convention it proposes itself** — the physicist brief (wave1_briefs `:121`) documents that the factor-2/normalization convention used to reach `PROVED` (Convention B) differs from roadmap §2.2's still-unedited Convention A, so the document satisfies "its own gate criterion under a redefinition it proposes itself" without the PI having signed off on that redefinition in writing. Silently declaring victory against a self-redefined target, rather than the frozen target, is the mathematical-proof analogue of threshold loosening and must not be waved through as a mere documentation nit. (b) The document's own token block sets `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` (`:39`) in the same breath as `GATE_AUDIT = PENDING` (`:37`) — pre-committing the headline verdict before the audit that is supposed to determine it, which anchors every downstream reader (including, evidently, all four wave-1 experts, none of whom proposed REFUTED or INCONCLUSIVE despite finding two literally-false sentences and a citation-outside-hypotheses defect inside the reviewed material).

- **Verdict coercion:** No PASS/FAIL is silently collapsed to OUT_OF_DOMAIN or vice versa in this document. But there is a subtler coercion: **four independently-blind reviewers, faced with a proof containing (i) a citation invoked outside its hypotheses, (ii) one false universal claim, (iii) a second false universal claim, and (iv) an undefined quantifier domain ("equivalencias marginales pertinentes" never defined per the logician, wave1_briefs `:83`), all converged on GATE_PASS_WITH_CONDITIONS rather than GATE_FAIL or INCONCLUSIVE.** That degree of convergence toward "pass, with a laundry list of textual fixes" when the underlying artefact contains actual false statements (not just gaps) is itself worth flagging as evidence of anchoring on the author's own `PROVED` token rather than a from-scratch verdict. A defensible alternative reading is: a document containing two false universal sentences and a proof step outside its cited lemma's hypotheses should not be labelled "PROVED" at all until repaired — the correct token today is `OPEN_WITH_EXACT_OBLIGATION` (a verdict the roadmap itself explicitly permits, `docs/hoja_de_ruta_septiembre_2026.md` §2.5), not `PROVED` with a promise to fix it later.

- **Premature / over-broad claims:** No horizon, Schwarzschild, r=2M, or 3+1D language appears in the audited document (correctly, per the physicist's zero-hits check), and no token block asserts a horizon claim. But the *silence* is itself a gap the physicist correctly flags: the section-0 and section-12 token blocks carry `NO_UNIVERSALITY_CLAIM` and `S2_NOT_OPENED` but no `NO_HORIZON_CLAIM` (wave1_briefs `:119`), in a repository whose headline claim is horizon recoverability — an omission that becomes dangerous exactly at the moment this token starts being read by downstream agents as "S2 authorized." Separately, and more structurally: the entire copula/rank-permutation machinery here operates on null-coordinate `(U,V)` rectangles in flat Minkowski, while the sealed benchmark's domain is Eddington-Finkelstein `(t*,r)` around a Schwarzschild horizon (`docs/preregistration.md:61-62`) — the physicist notes explicitly that "this formalism does not currently apply to the sealed domain, and no bridge should be asserted without a separate derivation" (wave1_briefs `:123`). Practically: even a fully successful S2 (Fisher-efficiency ratio → 1 for the rank-one symmetric conformal subclass of a flat diamond) says nothing directly transferable to the horizon benchmark without a wholly separate, not-yet-attempted coordinate bridge — which means the S1→S2 gate, even if cleanly passed, licenses further work on a line that may never reconnect to nachocausal's actual falsifiable claim. This risk is under-weighted in all four wave-1 briefs, which treat "claim ceiling correctly stated" (roadmap §3.2) as sufficient, without asking whether the S2 target is even the right target for the program's stated goal.

- **Independent-falsification gate:** Partially satisfied, not cleanly. Four blind wave-1 reviewers did re-check the algebra line by line and did find real defects (citation-outside-hypotheses, two false universal sentences, a Prop 9.4 proof gap, a chain-rule justification gap) — this is legitimate, non-trivial verification work, not rubber-stamping. But it is verification of a given derivation, not independent re-derivation from the axioms without sight of the target formula — a materially weaker form of independence than, e.g., a Lean/Alloy formalization (confirmed absent: `grep -rli "copula|fisher|score|permut" formal/` returns nothing, wave1_briefs `:63`). More seriously for *this specific gate*: the dossier states the chair "independently verified" the governance facts (seal hash, R3 scope, missing R4 note) but the mathematical content of sections 9-12 was checked only by the same pipeline of agents that operates within the same repository and session context as whoever drafted those sections — there is no evidence of an external, human, or differently-sourced check of the mathematics itself, and critically **no signed R4 note from the PI** exists to supply the one form of independence the project's own governance explicitly requires before new mathematical territory is admitted (`docs/program_reopening_note_2026-07-31.md:83`: "Nada entra sin una nueva nota firmada"; last signed note is R3, whose closed-list authorized scope is bridge E + write-up + novelty audit, `docs/program_reopening_note_2026-08-05_R3.md` §2, and does not include the Fisher-efficiency/geometric-tangent frontier). Confirmed directly: `ls docs/` contains only `program_reopening_note_2026-07-31.md` and `program_reopening_note_2026-08-05_R3.md` — no R4; `docs/backlog_hallazgos.md` does not exist; and the audited document itself carries no `GOBERNANZA:` line, unlike its sibling `wp6_d2_null_copula_dichotomy.md:7` which explicitly cites the R3 note as its governance anchor. **This alone is sufficient for GATE_FAIL, independent of the mathematics**: the repo's own perimeter rule was not followed, the one prior work package that did follow it (R3, for a materially similar frontier) sets a clean, directly-applicable precedent for what compliance looks like, and this document does not meet it.

- **Minimal falsification test:** No executable/simulation check is needed or appropriate — the artefact is pure closed-form analysis and running anything (`make dry-run`, `make gate`, `make op21-terminal`, or any script) would itself be an unauthorized action against a document with no `GOBERNANZA:` line. The correct minimal check is **textual, not executable**: verify that the repaired Teorema 6 proof (citing Prop 9.1 point 4 instead of Lema 9.2 for `lambda=0`) and the corrected §9.5 statements (restricted to `lambda != 0`, with the swap/reflection counterexamples acknowledged) are present in the committed text before the `PROVED` token is read as final — i.e., re-diff the document against the four independently-identified defects (C1/C2/C3 across the reproducibility, mathematician and logician briefs converge on the *same* lambda=0 citation error) and confirm zero remain. If a machine-checkable step is wanted at low cost and without opening S2, the one genuinely informative one is: formalize Teorema 6's four-way equivalence, *including the `lambda=0` branch*, as a small Lean lemma in `formal/HorizonFormal/` — this is the cheapest test that would mechanically expose whether the "PROVED" token survives a domain that currently is not literally covered by its own cited proof.

**Overall falsifier verdict: GATE_FAIL.** On governance alone (missing signed R4 note under the project's own explicit perimeter rule, absent `GOBERNANZA:` header, no `docs/backlog_hallazgos.md` entry) the commit should not be authorized as written. Independent of governance, the mathematics is not cleanly "PROVED": two literally false universal sentences in §9.5 and one lemma cited outside its own hypotheses in Teorema 6's proof are load-bearing defects, not decoration, and a "puerta lógica" that authorizes a new research phase should not be crossed on a document whose own central classification theorem contains an unrepaired citation-outside-hypotheses gap and whose gauge/uniqueness section asserts falsehoods. The correct token, if any is committed at all, is `GEOMETRIC_TANGENT_CLASSIFICATION = OPEN_WITH_EXACT_OBLIGATION` (a verdict the roadmap itself permits) pending both the signed R4 note and the textual repairs C1-C3 identified convergently by the reproducibility, mathematician, and logician seats.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: **BLOCK**

- Freeze status: Not applicable in the classical sealed-threshold sense — this is a pure-mathematics documentary artefact, no thresholds to freeze. But the roadmap's *own* pre-condition for entering this proof attempt is not satisfied: `docs/hoja_de_ruta_septiembre_2026.md:3` self-declares "**Plan REVISABLE, no congelado**. No es una pre-registración... no autoriza... cambios en instrumentos sellados." A document that is explicitly *not* a pre-registration cannot function as the frozen criterion that gates S1→S2 in `docs/hoja_de_ruta_septiembre_2026.md`§3 (`:206-208`, "Esta fase sólo se abre si S1 termina `PROVED`"). §2.2 (`:136-155`) fixes Convention A (`h_psi=lambda f(u)f(v)`) as *the* target subclass **before** any proof was attempted — that is the one thing in this roadmap that functions like a frozen criterion, revisable-plan disclaimer notwithstanding, because it was written down before the classification work began. The submitted document (`wp6_d2_geometric_tangent_classification.md:435-520`) proves the classification under a *different*, self-introduced Convention B (`𝒫ψ=λf(u)f(v)` ⇒ `h_ψ=2λff`), explicitly documents the mismatch (`:490-504`, `ROADMAP_NORMALIZATION_MISMATCH = CONFIRMED`), proposes but does **not** apply a diff to §2.2 to reconcile it (`:509-520`: "No se modifica la hoja de ruta en esta fase: la corrección queda propuesta, no aplicada"), and then declares `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` (`:39`, `:1162`) anyway. Proving under a criterion the same document quietly swaps in, then claiming the swap is cost-free because "el mismatch no es un error matemático" (`:490`), is a change to the success criterion made *after* seeing that the original criterion (Convention A) does not fall out cleanly from the score derivation. That is textbook post-hoc criterion adjustment, even though it is unusually transparent about doing so. Transparency mitigates the intent charge; it does not satisfy the freeze requirement. The self-declared "REVISABLE, no congelado" status (`:3`) cuts *against* letting this PROVED stand as a gate — a plan that admits it is not frozen cannot simultaneously mint a token (`PROVED`) that this same roadmap's §3 treats as an irrevocable logical gate opening S2.

- Seal integrity: Confirmed intact and untouched. `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` matches `docs/preregistration_002.md:7-8`. The document under audit runs no code, touches no sealed instrument (`nachocausal/thresholds.py`, `nachocausal/gate.py`), and consumes zero seeds. On the narrow question "does committing this file corrupt the sealed empirical pipeline" — no. This is not the axis on which the document should be blocked.

- Seed discipline: Not engaged. The document is pure derivation/algebra; it makes no reference to `EXPLORE_POOL = 1_000_000..1_000_039` or the virgin validation band `[2_000_000, 2_999_999]` (`docs/preregistration_002.md:14-16`). No seed-band violation to report here.

- Reporting rule: **Cannot yet be confirmed satisfied**, and this is the crux of the BLOCK. The reporting-symmetry rule that underlies every seal in this repo is: PASS, FAIL and INCONCLUSIVE must be reportable with equal ease, and no result may be declared success by silently moving the finish line. Here the document had three roadmap-sanctioned outputs available — `PROVED`, `REFUTED`, `OPEN_WITH_EXACT_OBLIGATION` (`docs/hoja_de_ruta_septiembre_2026.md:197-201`) — and instead of returning `OPEN_WITH_EXACT_OBLIGATION` against the literal §2.2 criterion (which is what a document that finds a live normalization gap and does not close it against the frozen target would owe), it manufactures a fourth, non-roadmap status track (`S1_CANDIDATE_COMPLETE_AWAITING_GATE_AUDIT`, `GATE_AUDIT = PENDING` at `:36-37`/`:1159-1160`) that sits *outside* §2.5's exactly-three-token contract while simultaneously publishing `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` in the very same status block (`:39`, `:1162`) — the literal token §3 reads to auto-open S2. `FACTOR_TWO_INDEPENDENT_CHECK = PASS` and `ASYMMETRIC_RANK_ONE_SECTOR = CLASSIFIED_BUT_NOT_PROMOTED` (`:893`, `:802`, `:1163`, `:1166`) are likewise invented tokens with no home in §2.5. Extra internal bookkeeping tokens are not inherently forbidden — but inventing a *parallel gate variable* (`GATE_AUDIT`) that the author intends as the real gate, while leaving the *roadmap's own* gate variable (`GEOMETRIC_TANGENT_CLASSIFICATION`) sitting at the value that mechanically triggers §3, is exactly the failure mode the three-token contract exists to prevent: it lets a document simultaneously claim "I have not really said PROVED yet" and "I have said PROVED" depending on which reader (human vs. section-3 trigger-logic) is asked. A file's on-disk status block cannot be read as pending by one convention and gate-triggering by another.

- Forbidden moves present?
  - **Post-hoc criterion redefinition**: yes — Convention A → Convention B swap after the classification was derived, undisclosed in the roadmap prior to this document (`:435-520`). Mitigated by candor, not eliminated.
  - **Ground-truth leakage**: no — no empirical data, no hidden embedding, no seeds involved.
  - **Re-run after peeking**: not applicable — no runs.
  - **Threshold loosening**: not applicable in the numeric-seal sense, but structurally analogous: the roadmap's §2.2 target was loosened to whatever the derivation actually produced.
  - **Reconstruction over-claim**: not found in the document's own claim-ceiling language (`§3.2` of the roadmap, `:233-248`, is respected in spirit by the WP's explicit non-claims at `:21-23`); no violation here.
  - **Governance/perimeter violation (structural, adjacent to freeze discipline)**: `docs/program_reopening_note_2026-07-31.md:83` ("Perímetro fijo: R1 y R2. Nada entra sin una nueva nota firmada") and its heir `docs/program_reopening_note_2026-08-05_R3.md` authorize exactly three items (R1 manuscript, R2 λ⁶ derivation, R3 null-copula bridge E). None of the three 2026-08-28 commits (`236b182` wp6_d2_modular_fiber_score.md, `4bcbfc5` README update, `99cec0d` this September roadmap) nor the untracked geometric-tangent file falls under R1/R2/R3's closed lists. **The perimeter breach precedes this commit** — it was already committed to history by the same author (`Ignacio <adnacho@gmail.com>`, matching the PI) three times on 2026-08-28 without a signed R4 note, and `docs/backlog_hallazgos.md` (the required destination for out-of-perimeter findings per rule §6.2 of the 07-31 note) does not exist. Committing the untracked file compounds an already-open governance gap rather than creating a new one in isolation, but a pre-registration warden cannot certify PASS on a step whose immediate ancestry already violates the repo's own written perimeter rule, self-authored by the same PI or not.

- Reasons:
  - `docs/hoja_de_ruta_septiembre_2026.md:3` — roadmap is explicitly non-frozen ("no es una pre-registración"), so it cannot simultaneously serve as the frozen success criterion that gates S2 per its own §3.
  - `docs/hoja_de_ruta_septiembre_2026.md:136-155` (§2.2, Convention A) vs. `wp6_d2_geometric_tangent_classification.md:435-520` (§6, Convention B) — proof delivered against a substituted criterion, mismatch declared but not reconciled in the roadmap, `PROVED` issued anyway.
  - `wp6_d2_geometric_tangent_classification.md:36-44` and `:1159-1166` — status block emits tokens (`S1_CANDIDATE_COMPLETE_AWAITING_GATE_AUDIT`, `GATE_AUDIT`, `FACTOR_TWO_INDEPENDENT_CHECK`, `ASYMMETRIC_RANK_ONE_SECTOR`) outside the closed three-token contract of `docs/hoja_de_ruta_septiembre_2026.md:195-204`, while still publishing the literal gate-triggering token `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED`.
  - `docs/program_reopening_note_2026-07-31.md:83` and `docs/program_reopening_note_2026-08-05_R3.md` (closed scope R1/R2/R3) — this work package and its two 2026-08-28 predecessor commits (`236b182`, `4bcbfc5`, `99cec0d`) fall outside all three authorized items; no R4 note exists; `docs/backlog_hallazgos.md` does not exist despite being the mandated destination for out-of-perimeter findings.
  - `make verify-seal` output this session (`6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`) matches `docs/preregistration_002.md:7-8` — seal axis alone is clean; BLOCK is on freeze/reporting/perimeter grounds, not on seal corruption.
  - Recommended remedy for a future PASS: (1) obtain a signed R4 note before this or any successor commit lands, or explicitly retro-ratify the three 2026-08-28 commits and route the true out-of-perimeter status to a `docs/backlog_hallazgos.md` entry; (2) either amend roadmap §2.2 to Convention B *before* re-asserting `PROVED` (making the criterion change auditable and dated prior to the result, not folded into the same commit as the result), or downgrade the WP's own verdict to `OPEN_WITH_EXACT_OBLIGATION` against the literal, unamended §2.2; (3) collapse the invented `GATE_AUDIT`/`S1_CANDIDATE_COMPLETE_AWAITING_GATE_AUDIT` machinery into one of the three roadmap-legal tokens so the file cannot be read two ways.

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| `wp6_d2_modular_fiber_score.md:1027-1032` — eq (7.4) `I_N^Π = E[(score)²]` is in §7.4, not §7.5 | Reproducibility engineer (C5i) | CONFIRMED — verified verbatim: (7.4) sits in "### 7.4 Cuarto momento del score Fisher"; §7.5 ("Combinación con el evento excepcional") contains only `L_N`, `C_A`, `N_A`, no `I_N^Π` definition |
| `wp6_d2_geometric_tangent_classification.md:1110` cites "§7.5 del WP6 modular" for `I_N^Π=E[(score)²]` | Reproducibility engineer / mathematician / logician | CONFIRMED mis-citation — Lema 11.1's proof literally says "Por §7.5 del WP6 modular, `I_N^Pi=E[(dot ell_N^Pi)^2]`", which is factually eq. (7.4) in §7.4 |
| `wp6_d2_modular_fiber_score.md` §7.5, `L_N` definition and `C_A`, `N>=N_A` restriction (lines 1034-1046, 1055-1085) | Reproducibility engineer, causet mathematician | CONFIRMED — `L_N:=E[Var(score∣[P])]` at line 1055; `C_A`, `N_A` bound `Pr(B_N)<=C_A/N` for `N>=N_A` at lines 1040-1046, propagated into (7.6) with the domain restriction stated |
| Theorem 5 (§7.6, lines 1090-1136) and its three hypotheses (M_* sup, Σa=0, (1/N)Σa²→c>0) | Reproducibility engineer, causet mathematician, logician | CONFIRMED — verbatim match; boxed statement at 1132-1136 exactly as described |
| `I_N^{[P]}` never defined in `wp6_d2_modular_fiber_score.md`, only used undefined in audited doc's (11.6) | Causet mathematician, logician | CONFIRMED — exhaustive grep of the frozen file finds zero occurrences of `I_N^{[P]}`; only `L_N` and `q_N=1-L_N/I_N^Π` are defined there; `wp6_d2_geometric_tangent_classification.md:1122` uses `I_N^{[P]}` with no definition supplied in either file |
| `wp6_d2_geometric_tangent_classification.md` drops `N>=N_A` in (11.6) | Reproducibility engineer (C6) | CONFIRMED — `grep -n "N_A"` on the audited file returns nothing |
| `wp6_d2_null_copula_dichotomy.md:54-78` Lema A (invariancia por rangos) | Causet mathematician | CONFIRMED — matches verbatim (order isomorphism `T=(F,G)`, `Q_n(Ω)=Q_n(C_Ω)`) |
| `wp6_d2_null_copula_dichotomy.md:80-102` Proposición B (separable ⟺ plano) | Physicist, mathematician | CONFIRMED — states exactly `Ω(U,V)=a(U)b(V) ⟺ (B,g)` plana, plus the independent curvature cross-check `R=0 ⟺ ∂_U∂_V log Ω=0 ⟺` separable, exactly as cited |
| `wp6_d2_null_copula_dichotomy.md:104-134` Teorema C (invisibilidad exacta a todo n) | Reproducibility engineer, mathematician | CONFIRMED — verbatim statement and proof match; orbit corollary present |
| `wp6_d2_null_copula_dichotomy.md:140` Teorema D status `PROVED_MODULO_FUENTES_VERIFICADAS` | Reproducibility engineer, logician | CONFIRMED — line 140 exact match; final status block (line 492) gives the equivalent finer label `PROVED_MODULO_HKMMRS_2013_Y_GRUBEL_2024` |
| `wp6_d2_null_copula_dichotomy.md:~230-263` obstruction `b`, marked OPEN | Causet mathematician | CONFIRMED — `b` is the unique even direction of the n=4 kernel (lines 230-263); overall bridge status is `PUENTE E OPEN` (line 4) / `PUENTE_E_PRIMA_INYECTIVIDAD_EN_PI = OPEN_PERO_ENTORNO_DE_PI_EXCLUIDO` (line 495) |
| `wp4_ibar_direct_score_derivation.md:300-312` fixed-rank score with explicit quantile-motion terms, "(ANOVA) doble centrado" | Causet mathematician | CONFIRMED (near-verbatim) — lines 300-312 give `s_tau = ∂_tau g + a1(w)∂_w g + a2(v)∂_v g` with `∂_tau g = D − E[D∣w] − E[D∣v] + E[D]`; label is split across lines 305 ("(ANOVA)") and 308 ("(doble centrado)") rather than one fused phrase, but the object and label are both present |
| `wp4_ibar_direct_score_derivation.md:395-420` Lema 9.1, four-step compactness argument | Logician | CONFIRMED — §9(b) lines 412-429 is explicitly a 4-step argument, and the text itself states it "cierra el hueco señalado explícitamente por el PI" |
| `wp6_d2_geometric_tangent_classification.md` §5.2, "La acotación de h_psi permite derivar bajo la integral" (single-sentence justification, contrasted with wp4's 4-step standard) | Logician (C5) | CONFIRMED — line 380-381 is exactly this one sentence, with no uniform-neighborhood argument, unlike wp4's Lema 9.1 |
| `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:135` constant determinant in (t,r) | Physicist | CONFIRMED verbatim |
| same file, lines 181-193, 463: bimodal distribution / longest-chain diagnostic | Physicist | CONFIRMED verbatim (both longest-chain and cardinality-of-future readings explicitly called "bimodal"; line 463 gives the general EGS-style statement) |
| same file, line 195: diagnostic fails for regular (Hayward) black holes | Physicist | CONFIRMED verbatim ("such a definition would no longer work for regular black holes... e.g., of the Hayward type") |
| `docs/preregistration.md:61-62` Eddington-Finkelstein, det g = -1 | Physicist | CONFIRMED — line 61 exact match |
| `docs/preregistration_001_addendum.md:39-40` r_S = 2M = 0.5, finite box | Physicist | CONFIRMED — line 40 exact match (table row); box geometry given in the preceding row |
| Bombelli conjecture quote via Brightwell–Luczak arXiv:1510.05612 §2 (`wp6_d2_null_copula_dichotomy.md:406-419`) | Mathematician (novelty triage) | UNCONFIRMED as a `biblioteca/` artefact — Brightwell–Luczak's paper itself is **not present** in `biblioteca/` (only cited secondhand inside `Libro_basico.md:1424` and `The causal set approach to quantum gravity.md:3438`); cannot independently verify the "literal" quote from repo holdings alone |
| Bombelli conjecture, primary quote (`wp6_d2_null_copula_dichotomy.md:421-428`) from `gr-qc0002053_Bombelli...pdf` | Mathematician | CONFIRMED — the (iii) statement is verbatim in the PDF (lines 404-408 of extracted text) |
| Winkler, *Random orders*, Order 1 (1985) 317-335 (`wp6_d2_null_copula_dichotomy.md:472-476`) | Mathematician (novelty triage) | UNVERIFIED / NOT IN BIBLIOTECA — no PDF or derived-md of this paper exists in `biblioteca/`; a *different* Winkler paper ("Random orders of dimension 2", Order 7, 1991) is cited secondhand in `Libro_basico.md:1585`, confirming the author/topic are real CST folklore, but the specific 1985 paper cannot be checked against primary text in the repo |
| Winkler *Random orders* / Brightwell *Models of random partial orders* / Bollobás–Brightwell as novelty-audit target (`wp6_d2_null_copula_dichotomy.md:388, 396-397`) | Causet mathematician | CONFIRMED absent from biblioteca, and the document **itself already flags this**: `wp6_d2_null_copula_dichotomy.md:401` reads `[UNVERIFIED: ninguno leído; no están en biblioteca/.]` — so no false claim of verification is made here; Brightwell's "Models of random partial orders" is independently confirmed to be a real, existing paper via a secondhand bibliography hit in `Rideout_Sorkin_1999...md:626` |
| HKMMRS 2013 (*Limits of permutation sequences*) and Grübel 2024 (*Ranks, copulas, and permutons*), used to prove Teorema D | Mathematician / logician | UNVERIFIED — neither paper (nor any bibliography mention of them) exists anywhere in `biblioteca/`, unlike the Winkler/Brightwell case, and here the document does **not** attach an `[UNVERIFIED]` tag to them, instead stating "fuentes verificadas por el PI, 2026-08-05" as if closed; this asymmetry (flagged-vs-unflagged absence from biblioteca) should be recorded as a gap in the gate's evidentiary trail, though it does not itself falsify Teorema D |
| Kelly–Trotter 1982 / Trotter as prior art for realizer-uniqueness, later dismissed (`wp6_d2_null_copula_dichotomy.md:333`) | Causet mathematician | CONFIRMED as an existing, real citation — "D. Kelly and W.T. Trotter, Dimension theory for ordered sets, in Ordered Sets, ed. I. Rival, Reidel 1982" appears verbatim in `biblioteca/derived-md/Bombelli_1987_PhD.md:2169` and `Manifoldlike_Causal_Sets_eGrove_ETD.md:1280`; the paper itself is not in `biblioteca/` as a standalone document, only cited secondhand |
| `wp6_d2_modular_fiber_score.md:20`, `:1263` `GEOMETRIC_TANGENT_CLASSIFICATION = OPEN` (stale token, C2) | Reproducibility engineer | CONFIRMED verbatim at both line numbers |
| Missing FECHA/GOBERNANZA/NATURALEZA/SELLO header in `wp6_d2_geometric_tangent_classification.md` | Reproducibility engineer | CONFIRMED — no such fields found anywhere in the file, unlike the sibling `wp6_d2_null_copula_dichotomy.md:3-9` header block, which is present and matches as cited |
| ANOVA/Hoeffding decomposition of `C([0,1]^2)` as the content of Prop 9.1/Teorema 6 — novelty-hygiene claim | Causet mathematician, logician | CONFIRMED that the identical decomposition object (double-centred residual, `D − E[D∣w] − E[D∣v] + E[D]`) is already present and explicitly named "(ANOVA)"/"doble centrado" in `wp4_ibar_direct_score_derivation.md:305-308`, with no cross-reference added in the audited document's §9. Additionally: searches of all of `biblioteca/` (including the scanned, non-OCR'd van der Vaart–Wellner volume `[Aad_van_der_Vaart,_Jon_Wellner].pdf`, which could not be full-text-searched) turned up **no** dedicated primary source on "Hoeffding decomposition"/"ANOVA decomposition of copulas"/"copula tangent" — this is textbook material (Hoeffding 1948 U-statistics decomposition / Hájek projection) that is standard in the statistics literature at large but is not separately anchored inside `biblioteca/`; the *in-repo* precedent (`wp4_ibar_direct_score_derivation.md:300-312`) is the only anchor available, and it independently corroborates that the audited document's "Proposición 9.1 / Teorema 6" is a re-derivation of a known object under a fresh name |

- Notes: All five priority items (1–4, 6) check out exactly as the four Wave-1 experts described — every `path:line` citation resolves, and the content matches, including two real defects the panel converged on independently: (a) the mis-citation of eq. (7.4) as "§7.5" in `wp6_d2_geometric_tangent_classification.md:1110`, and (b) the undefined `I_N^{[P]}` used in boxed equation (11.6) with no definition anywhere in `wp6_d2_modular_fiber_score.md`. The literature-of-random-2D-orders item (5) is more mixed: Winkler's 1985 "Random orders" paper and the Kelly–Trotter 1982 chapter are real, attested citations (confirmed via secondhand bibliography hits inside other `biblioteca/` documents — Libro_basico.md, Bombelli_1987_PhD.md, Manifoldlike_Causal_Sets_eGrove_ETD.md, Rideout_Sorkin_1999...md) but **none of Winkler, Brightwell "Models of random partial orders", Brightwell–Luczak arXiv:1510.05612, HKMMRS 2013, or Grübel 2024 exist as primary-source files inside `biblioteca/`** — only as bibliography-list mentions in other papers, or (for Brightwell–Luczak and Bombelli) as text the document claims to have read outside the repo this session. Crucially, the audited document is honest about this for the Winkler/Brightwell/Bollobás–Brightwell novelty-triage citations (self-tags `[UNVERIFIED: ninguno leído; no están en biblioteca/.]` at line 401) but is **not** equally honest for HKMMRS 2013 and Grübel 2024, which underwrite the load-bearing Teorema D and are stated as "fuentes verificadas por el PI" with no `[UNVERIFIED]` flag despite being just as absent from `biblioteca/` — this double standard in citation hygiene should be surfaced to the gate, though it does not by itself overturn Teorema D. On the central novelty question: the core mathematical engine of the audited document — Prop 9.1 / Teorema 6's classification of a rank-one bilinear perturbation of `C([0,1]^2)` as exactly `ker P = A` (the additive/separable subspace) — is confirmed by both the causet mathematician and the logician, and independently corroborated here, to be the classical two-way ANOVA (Hoeffding) decomposition applied to a copula tangent; the *identical* double-centred object already exists in this repository under the label "(ANOVA) doble centrado" at `wp4_ibar_direct_score_derivation.md:300-312`, with no cross-reference from the audited document. This should be recorded verbatim for the S3 priority/novelty audit so it does not inherit an inflated novelty surface: the S1→S2 gate's central classification result is standard statistical mathematics (Hoeffding/ANOVA decomposition + rank-one kernel identification), not a new theorem, even though its application to causal-set copula tangents and the resulting Fisher-efficiency corollary (§11, chained to the frozen Theorem 5) may be new.

## 8. Synthesis

### 8.1 Recuento de veredictos por asiento

| Asiento | Veredicto |
| --- | --- |
| Ingeniero de reproducibilidad | `GATE_PASS_WITH_CONDITIONS` (C1 declinada ⇒ `GATE_FAIL` por gobernanza) |
| Matemático de causal sets | `GATE_PASS_WITH_CONDITIONS` (7 condiciones textuales) |
| Lógico matemático | `GATE_PASS_WITH_CONDITIONS` (C1-C6, C7 como nota) |
| Físico | `GATE_PASS_WITH_CONDITIONS` (4 condiciones textuales) |
| Falsador | **`GATE_FAIL`** |
| Guardián de pre-registración | **`BLOCK`** |
| Verificador de literatura | Sin veredicto de puerta; todas las citas prioritarias CONFIRMED, dos defectos confirmados, un problema de higiene de novedad |

Un `BLOCK` de pre-registración en §6 impide por invariante fundacional cualquier veredicto PROCEED
en §10, y el validador del brief lo comprueba mecánicamente. La dirección recomendada es, por
tanto, **revisar y reconvocar**, no proceder.

### 8.2 Qué NO se ha roto

Conviene fijarlo antes de la lista de defectos, porque es el resultado positivo de la auditoría y
es sólido: **ninguno de los siete asientos encontró un teorema falso.** Las cinco dianas del PI se
resuelven así:

- **Diana 1 (proyector `P`, núcleo, rango, suma directa): SOBREVIVE.** Verificada punto por punto
  e independientemente por el lógico y por el matemático de causal sets. No hay fallo de
  continuidad, medibilidad ni intercambio de integrales: todo integrando es continuo sobre un
  compacto.
- **Diana 4 (H3 en los extremos `i=1,N`): SOBREVIVE, y por una razón limpia.** La cota
  `Var(U_(i)) ≤ 1/(4(N+2))` es **libre de `i`** (máximo en `i=(N+1)/2`), y Chebyshev es
  distribution-free, de modo que la asimetría de la Beta en los extremos es irrelevante: la prueba
  nunca usa la forma de la Beta. `δ_N=(N+2)^{-1/4}` es legítima para todo `i`. Tres asientos
  re-derivaron (11.4) y (11.5) a mano y coinciden.
- **Diana 5 (dependencia oculta de `epsilon` por el PIT): SOBREVIVE, y hay una tercera derivación
  independiente en el repo.** La cámara `C_pi` está definida por rangos en coordenadas de cópula y
  es por tanto `epsilon`-independiente; no hay término de frontera móvil. El desplazamiento `O(ε)`
  del cuantil multiplica un gradiente espacial `O(ε)`, luego contribuye `O(ε²)`. Además
  `wp4_ibar_direct_score_derivation.md:300-312` ya contiene el score a rangos fijos con los
  términos de movimiento de cuantiles explícitos, y en el nulo se reduce exactamente al doble
  centrado — una confirmación independiente de (3.5) que el documento no citaba.
- **Dianas 2 y 3: NO sobreviven como están escritas**, pero los defectos son de **citación y de
  redacción**, no de sustancia. Ver §8.3.

### 8.3 Los defectos reales, ordenados por gravedad

**Nivel 1 — gobernanza (bloqueante, y sólo el PI puede resolverlo).**
`docs/program_reopening_note_2026-07-31.md:83` exige nota firmada para todo lo que entre en el
perímetro. La última es R3, cuyo ámbito cerrado (puente E, redacción, auditoría de novedad) **no
incluye** esta frontera. No existe R4. `docs/backlog_hallazgos.md` no existe. El hermano
`wp6_d2_null_copula_dichotomy.md:7` sí lleva línea `GOBERNANZA:` y este documento no. Hallazgo
adicional, y es el más incómodo: **la brecha precede a este commit** — los tres commits del
2026-08-28 (`236b182`, `4bcbfc5`, `99cec0d`) ya cayeron fuera de R1/R2/R3 sin nota firmada. Este
commit agravaría una brecha ya abierta, no la crearía.

**Nivel 2 — el token `PROVED` no puede emitirse hoy, por tres razones convergentes.**

1. *Auto-satisfacción del criterio.* La hoja de ruta §2.2 fija la Convención A antes de empezar;
   el documento prueba bajo Convención B, declara el mismatch, propone el diff y **no lo aplica**,
   y emite `PROVED` igualmente. Guardián y físico coinciden: es el análogo, en una prueba, de
   aflojar un umbral. La candidez lo atenúa; no lo elimina.
2. *Variable de puerta paralela.* `S1_CANDIDATE_COMPLETE_AWAITING_GATE_AUDIT` y
   `GATE_AUDIT = PENDING` conviven con `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED`, que es el
   literal que la §3 lee para abrir S2. El fichero se lee como pendiente o como puerta abierta
   según quién lo lea. **Estos tokens los introdujo el chair a petición del PI en la sesión previa;
   estaban mal planteados.**
3. *Anclaje del panel.* El falsador señala que los cuatro expertos ciegos leyeron un documento que
   ya contenía su propio `PROVED`, y ninguno propuso REFUTED ni INCONCLUSIVE pese a encontrar dos
   frases universales falsas. El chair acepta la crítica: poner el veredicto dentro del artefacto
   auditado fue un defecto de diseño de la propia auditoría.

**Nivel 3 — reparaciones textuales, todas mecánicas, ninguna requiere matemática nueva.** Ver la
lista consolidada T1-T21 en §9.2.

**Nivel 4 — higiene de novedad, de cara a S3.** El núcleo de la Proposición 9.1 y del Teorema 6 es
la descomposición ANOVA / Hoeffding clásica de `C([0,1]^2)`, y el repo **ya usa ese objeto con ese
nombre** en `wp4_ibar_direct_score_derivation.md:305-308`. El verificador de literatura confirma
que no hay fuente primaria dedicada en `biblioteca/`. Debe constar en acta que el resultado central
de la puerta es matemática estándar, sin que eso lo desacredite: lo posiblemente nuevo es su
aplicación a tangentes de cópula de causal sets y el corolario Fisher encadenado al Teorema 5.

### 8.4 Desacuerdos abiertos (no se ocultan)

1. **Cuatro asientos contra dos.** Los expertos dicen `GATE_PASS_WITH_CONDITIONS`; falsador y
   guardián dicen `GATE_FAIL` / `BLOCK`. No es reconciliable por votación: el invariante
   fundacional da prioridad al `BLOCK`. El chair señala además que los cuatro expertos condicionan
   su PASS a que las condiciones se cumplan **antes** del commit, lo que en la práctica los acerca
   mucho más al falsador de lo que sugiere la etiqueta.
2. **Orden de los commits: el PI contra el guardián.** El PI (mensaje de esta sesión) quiere
   proof-commit primero y corrección del roadmap después, para que la genealogía muestre que el
   teorema no salió de retocar el plan. El guardián exige lo contrario: el cambio de criterio debe
   quedar fechado **antes** del resultado. **Ambos protegen algo real y distinto.** El chair
   propone en §9.3 una secuencia de tres commits que satisface a los dos; la elección es del PI.
3. **Qué token emitir mientras tanto: ingeniero contra guardián.** El ingeniero propone
   `PROVED_PENDING_GATE_AUDIT` (una cadena que no dispara el trigger); el guardián dice que
   inventar tokens es precisamente el problema. **Se reconcilian:** `OPEN_WITH_EXACT_OBLIGATION` es
   legal según §2.5, no dispara la §3, y expresa exactamente la situación. El chair lo recomienda.
4. **Disidencia del chair frente al falsador, en dos puntos.**
   - *«Circularidad de selección de diana».* Es cierto que la subclase se eligió para encajar en el
     Teorema 5 ya probado, pero eso está **declarado** en la hoja de ruta §2.2, que pide
     literalmente identificar una subclase que alimente el teorema congelado. Modera cuánto peso
     evidencial puede cargar el `PROVED`; no es un defecto oculto.
   - *«La puerta es teatro porque (11.6) ya es S2».* (11.6) es un corolario **por citación** del
     Teorema 5 congelado aplicado a la clase; el entregable de S2 según §3 es el teorema
     geometría→causet completo, que no está escrito. Pero la premisa del falsador sí se sostiene:
     emitir (11.6) junto a `S2_NOT_OPENED` es incoherente, y se corrige reetiquetando (T10).
5. **Conflicto de interés del chair, declarado.** El mismo agente redactó §§9-12 del artefacto
   auditado, construyó el dossier y preside este comité. Los siete asientos son ciegos entre sí y
   verificaron el texto de forma independiente, pero **no hay verificación externa, humana ni de
   fuente distinta, de la matemática**. El falsador lo señala y el chair lo suscribe: la puerta
   independiente que la gobernanza del propio proyecto exige es la nota firmada del PI, que no
   existe. `[UNVERIFIED]` queda todo lo que un lector humano externo habría cubierto.
6. **Ubicación del artefacto.** El ingeniero señala tensión entre `research_program/README.md:10-12`
   (que reserva `docs/` para cierres de fase) y la ubicación en `work_packages/`. El precedente es
   mixto: el hermano congelado vive también en `work_packages/`. El chair no lo eleva a condición.

### 8.5 Alternativas ordenadas

1. **Recomendada — reparar, degradar el token y reconvocar.** Aplicar T1-T19, emitir
   `OPEN_WITH_EXACT_OBLIGATION` con la obligación exacta escrita, y no tocar S2. El PI decide
   entonces la gobernanza (G1) y la convención (G2). Coste: bajo. Preserva íntegro el trabajo
   matemático, que no está en cuestión.
2. **Aceptable — no comprometer nada y abrir primero la gobernanza.** Firmar R4 (o fechar el
   hallazgo en `docs/backlog_hallazgos.md`) antes de tocar el artefacto. Más limpio
   metodológicamente, más lento.
3. **Desaconsejada — comprometer `PROVED` hoy con las condiciones como deuda.** Cruza una puerta
   lógica con dos frases universales falsas en el texto y sin nota firmada. Es exactamente lo que
   la regla fundacional «un guardarraíl que no puede fallar es decoración» existe para impedir.
4. **Rechazada — abrir S2.** Ningún asiento la apoya y las restricciones duras la prohíben.

## 9. Next-step spec

### 9.1 Pasos reversibles (pueden ejecutarse ya, si el PI lo pide)

- `make verify-seal` → debe seguir dando `6e2c3888…bfefd4`.
- `make audit` → debe salir 0.
- `make test` → verde, sólo como testigo de efecto nulo.
- Aplicar las reparaciones textuales T1-T19 al fichero **untracked**, que sigue sin comprometerse y
  por tanto es enteramente reversible.
- **No autorizados y no necesarios:** `make dry-run`, `make gate`, `make op21-terminal`. Ninguna
  simulación, ninguna semilla, ningún script nuevo. La prueba mínima de falsación es **textual**,
  no ejecutable (ver §9.4).

### 9.2 Condiciones consolidadas (deduplicadas de los siete asientos)

**Gobernanza — sólo el PI, no delegable:**
- **G1.** Firmar una nota R4 que autorice esta frontera, o bien declararla fuera de perímetro y
  fecharla en `docs/backlog_hallazgos.md` (que hay que crear). Decidir además si los tres commits
  del 2026-08-28 se ratifican retroactivamente.
- **G2.** Resolver por escrito la convención: enmendar la hoja de ruta §2.2 a Convención B, con
  fecha **anterior** a cualquier reafirmación de `PROVED`.

**Reparaciones textuales del artefacto — mecánicas, sin matemática nueva:**
- **T1.** Teorema 6, rama (c)⇒(a): citar Proposición 9.1(4), no el Lema 9.2 (cubre `λ=0`).
- **T2.** §9.5(ii): restringir a `λ≠0` y probar la fidelidad de `(λ,[f])` o degradarla a remark.
- **T3.** §9.5 y §12: sustituir «única equivalencia» por el enunciado de fibra probado
  (`{ψ : h_ψ = h} = ψ₀ + A`) y reconocer el swap `(u,v)↦(v,u)` y la reflexión.
- **T4.** Proposición 9.4: sustituir «punto de Lebesgue» por Fubini con `χ'(v₀) ∈ (0,∞)`, o usar el
  argumento de rectángulos, que prueba lo mismo sin absoluta continuidad.
- **T5.** §5.2: argumento de dominación uniforme en un entorno de `ε=0`, no sólo en `ε=0`; y
  declarar `q_ε > 0` para todo `ε`.
- **T6.** §3.2: justificar la regla de la cadena por continuidad uniforme, o asumir `ψ ∈ C¹`.
- **T7.** §10: «sin invocar (3.5)», no «sin invocar §3».
- **T8.** §11.5: citar (7.4)/§7.4 para `I_N^Π`, y §7.5 sólo para `L_N`.
- **T9.** (11.6): definir `I_N^{[P]}`, enunciar y probar una vez `I^{[P]} = I^Π − L_N`, arrastrar
  `N ≥ N_A`, y declarar la monotonía `M_* ≤ ‖f‖_∞`.
- **T10.** Reetiquetar (11.6) como corolario condicional, no entregable de S2.
- **T11.** §9.1: corregir el desliz de categoría `M_u M_v = ψ̄·1` (operador vs función).
- **T12.** Declarar que `Π_N` depende del realizador y que sólo (11.6) es order-only; citar la
  independencia rango ⊥ estadísticos de orden.
- **T13.** Referencia cruzada a `wp4_ibar_direct_score_derivation.md:300-312` y nombrar la
  Proposición 9.1 como descomposición ANOVA / Hoeffding.
- **T14.** Citar `wp6_d2_null_copula_dichotomy.md` §3 para identificar `ker P` como las direcciones
  **planas**, no meramente marginales.
- **T15.** Añadir `NO_HORIZON_CLAIM` y `MINKOWSKI_DIAMOND_PERTURBATIVE` a los bloques de estado.
- **T16.** Matizar «infinito-dimensional» → «infinito-dimensional como coset; rank-one módulo el
  núcleo plano».
- **T17.** Añadir cabecera de gobernanza (`FECHA`, `NATURALEZA`, `SELLO`, `SEMILLAS`, `GOBERNANZA`,
  `GATE_AUDIT`), replicando `wp6_d2_null_copula_dichotomy.md:3-9`.
- **T18.** Registrar la desviación `f ∈ C[0,1]` frente al «`f` suave» de §2.2, y que la lectura
  geométrica (`∂_u∂_v ψ = λ f'f'`) requiere `f ∈ C¹`.
- **T19.** Bloques de estado: sustituir `GEOMETRIC_TANGENT_CLASSIFICATION = PROVED` y los tokens de
  puerta inventados por `GEOMETRIC_TANGENT_CLASSIFICATION = OPEN_WITH_EXACT_OBLIGATION`, con la
  obligación exacta escrita (= G1 + G2 + T1-T3), manteniendo `S2_NOT_OPENED`.

**Higiene del árbol — commit acompañante, no el mismo:**
- **T20.** Actualizar `wp6_d2_modular_fiber_score.md:20`, `:1263` y `README.md:95`, o añadir
  `SUPERSEDED_BY:`, para que no queden dos valores contradictorios de la misma clave.

**Hallazgo en OTRO documento — fuera del alcance de este commit, se registra:**
- **T21.** `wp6_d2_null_copula_dichotomy.md` marca `[UNVERIFIED]` las citas Winkler/Brightwell pero
  **no** HKMMRS 2013 ni Grübel 2024, que sostienen el Teorema D y están igual de ausentes de
  `biblioteca/`. Doble rasero de higiene de citación. No falsifica el Teorema D.

### 9.3 Secuencia de commits propuesta (reconcilia al PI y al guardián)

El PI quiere que la prueba quede preservada **antes** de tocar el plan; el guardián exige que el
cambio de criterio quede fechado **antes** del `PROVED`. Ambas cosas se cumplen a la vez si el
token viaja por separado del texto:

```text
99cec0d  roadmap original
   |
   +-- (1) commit del WP con T1-T19 aplicadas
   |        GEOMETRIC_TANGENT_CLASSIFICATION = OPEN_WITH_EXACT_OBLIGATION
   |        (la prueba queda preservada primero, y es ella la que detecta el mismatch)
   |
   +-- (2) commit de higiene del árbol (T20)
   |
   +-- (3) commit del roadmap: §2.2 a Convención B (G2)
   |
   +-- (4) commit mínimo que sube el token a PROVED  [requiere G1 firmada]
```

Ningún paso de esta secuencia está autorizado por este comité: los cuatro son **committing steps**
y requieren autorización explícita del PI, y el (4) requiere además la nota R4 firmada.

### 9.4 Prueba mínima de falsación (pre-comprometida)

**No ejecutable, y deliberadamente.** El artefacto es análisis en forma cerrada; ejecutar cualquier
cosa contra un documento sin línea `GOBERNANZA:` sería en sí mismo una acción no autorizada. La
prueba mínima es un **re-diff textual**: comprobar que T1, T2 y T3 están presentes en el texto
comprometido y que no queda ninguna instancia de (a) el Lema 9.2 citado con `λ` recorriendo todo
`R`, (b) la afirmación de fidelidad de `(λ,[f])` sin restringir a `λ≠0`, ni (c) la palabra «única»
sin dominio de cuantificación. Si el PI quiere una comprobación mecánica de bajo coste y sin abrir
S2, la única genuinamente informativa es formalizar la equivalencia del Teorema 6 **incluyendo la
rama `λ=0`** como un lema Lean en `formal/HorizonFormal/`; hoy `formal/` no contiene nada de
cópulas, scores ni permutaciones.

### 9.5 Regla vinculante pre-comprometida

Si tras aplicar T1-T19 el PI decide **no** firmar G1, el veredicto de puerta queda en `GATE_FAIL`
por gobernanza y el artefacto no se compromete, o se compromete con
`OPEN_WITH_EXACT_OBLIGATION` y una entrada fechada en `docs/backlog_hallazgos.md`. En ningún caso
se abre S2. `PASS`, `FAIL` e `INCONCLUSIVE` se reportan por igual.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

Veredicto de puerta traducido a la escala pedida por el PI: **`GATE_FAIL` por gobernanza**
(G1 ausente) **y `GATE_PASS_WITH_CONDITIONS` en lo matemático** (T1-T19, ninguna de las cuales
requiere matemática nueva). Ningún teorema de §§9-11 resulta falso. Lo que no puede emitirse hoy es
el **token**, no la matemática.

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
