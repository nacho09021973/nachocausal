# Comité Decision 045 — Estado lógico del candidato 7.1 (`S_n`) en el canal `fixed_n`

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Adjudicar **exclusivamente** el estado lógico del candidato 7.1 de
`research_program/bibliography/ficha_se_busca_tv_order_only.md` §7.1 — el conteo de pares
comparables `S_n` — en el canal `fixed_n` (§1.3 modo 3). Siete preguntas obligatorias:

1. ¿Es correcta en `fixed_n` la cadena
   `Delta_p != 0` ⇒ diferencia de medias `Theta(n^2)` + `Var(S_n) = O(n^3)` ⇒
   `TV(Q^n_tau, Q^n_tau') -> 1`?
2. ¿Se necesita la CLT de Reitzner–Schulte, des-Poissonización, o un ajuste empírico del exponente?
3. ¿Debe la ficha dejar de marcar **toda** Forma L como `[OPEN]` en `fixed_n`?
4. ¿Qué etiqueta precisa separa existencia asintótica de utilidad finita? (evaluar al menos
   `[PROVED — FIXED_N ASYMPTOTIC SEPARATION; NON-EFFECTIVE]` +
   `[OPEN — FINITE_N EFFICIENCY / CONSTANT-LEVEL INFORMATION EFFICIENCY]`)
5. ¿Cómo debe modificarse la hoja de ruta? (retirar des-Poissonización como bloqueo de `fixed_n`;
   conservarla donde siga siendo necesaria; priorizar prefactor/eficiencia constante; **no** abrir
   observable nuevo ni ejecución nueva)
6. ¿Queda el exponente `1/2` demostrado por la matemática existente?
7. Valorar: «El exponente raíz-n no parece ser el cuello de botella. Bajo la cota Fisher de WP4, es
   la tasa regular esperable y posiblemente óptima. El problema visible está en el prefactor o en la
   pérdida de información al comprimir el poset completo al único estadístico `S_n`» — marcando qué
   es demostrado, qué es inferencia y qué sigue abierto.

**Restricción de sesión impuesta por el PI y honrada:** un solo paso y un solo fichero (esta acta).
No se editan la ficha, la hoja de ruta, el Anexo C ni ningún otro documento. No se crea código,
script, test, CSV ni notebook. No se ejecutan sprinklings, semillas ni Monte-Carlo. No se toca
sello, preregistro ni contrato congelado. No se commitea ni se hace push.

## 2. Verified state

Hechos comprobados **esta sesión**, cada uno con su comando / `file:line`. Lo no comprobado se marca
`[UNVERIFIED]`.

- **Working tree.** `git status --short` →
  ` M research_program/bibliography/ficha_se_busca_tv_order_only.md`,
  ` M research_program/work_packages/wp4_comparable_pair_separation.md`,
  ` M research_program/work_packages/wp4_comparable_pair_separation_checks.py`,
  `?? docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md`.
  `HEAD = 90e3aad` («docs: WP4 Anexo C — p(tau) != p(tau') probado para la familia diamante (ficha
  v4)»). Rama `main`.
- **Sello.** `make verify-seal` → `thresholds.py sha256:`
  `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, **bit-idéntico** al récord
  congelado en `docs/preregistration_002.md:8`. Sin drift. `nachocausal/thresholds.py` **ausente**
  de `git status --short`. `RESPECT_SEAL_FREEZE` honrado; ningún path sellado se ejecuta en esta
  sesión.
- **Auditoría previa (routing).** `/auditor` ya corrió sobre este objeto:
  `docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md`,
  `AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS`, `AUDIT_ERRORS=0`, `AUDIT_WARNINGS=25` (23 son la línea
  base preexistente del repo). Su **Finding 1** — «the note UNDER-claims: a `fixed_n` Forma L now
  follows, and §6's `[OPEN]` label is wrong for that channel» (`:145-182`) — es exactamente lo que
  este comité adjudica. **Gap de routing registrado:** ese informe sigue `??` (untracked, sin
  commitear); la *secuencia* del routing se honra, el *registro* aún no es durable.
- **Regla de routing vigente, anclada.** `docs/hoja_de_ruta_24_jul_2026.md:66-70` (§2, ítem 4):
  «Cualquier resultado que emerja de (1)-(3) que parezca cerrar una Forma L/U/D debe pasar por
  `/auditor` antes de tocarse el estado `[PROVED]`/`[OPEN]` de la ficha, y por `/comite` antes de
  promoverse a una decisión que afecte al programa». Repetida en
  `docs/hoja_de_ruta_25_jul_2026.md:96-98`.
- **Anclaje decisivo para la adjudicación del «No hacer».** `docs/hoja_de_ruta_24_jul_2026.md:52-57`
  (§2, ítem 1) dice literalmente: «Si `p(theta) != p(theta')` se confirma, **la cadena de Forma L
  para 7.1 queda cerrada salvo redacción**». La hoja del 25 jul §4 (`:102-103`) lo revierte a «No
  presentar el candidato 7.1 como Forma L. Ni «casi»». El comité está restaurando la previsión del
  24 jul, **restringida al canal `fixed_n`** — no innovando contra un plan.
- **Estado del programa.** `PROGRAMA_EN_PAUSA_LIMPIA` (`docs/marcador_reentrada_2026-07-19.md:3`);
  línea de localizadores C1–C6 cerrada (C6 = `BLOCKED_NO_STABLE_CODIM2`, comités 043/044);
  recomendación viva: consolidar (paper), no abrir C7. Nada de esta acta la toca.
- **Documentos objeto — estatus autodeclarado, verificado.** La ficha es `BORRADOR / EXPLORACION`
  (`:3`); el Anexo C es «Working draft, REVISABLE, not frozen» (`:3-9`); la hoja del 25 jul es
  «Plan REVISABLE, no congelado» (`:3-4`). **Ninguno es un objeto congelado.**
- **Mis-anclas confirmadas por dos roles independientes.** `auditor_report_026:225-227` enruta por
  «ficha §2.4 and roadmap §2.4»: la ficha **no tiene §2.4** (sus encabezados saltan de `## 2.2` a
  `## 3.`) y la hoja del 25 jul tampoco; la ancla real es `docs/hoja_de_ruta_24_jul_2026.md:66-70`
  (§2 **ítem** 4). Defecto de anclaje, no de contenido.
- **`[UNVERIFIED]` declarado.** El presidente **no** ejecutó
  `wp4_comparable_pair_separation_checks.py` en esta sesión (restricción del PI). Todos los
  literales numéricos citados provienen del texto commiteado/working-tree del Anexo C y del informe
  026; su procedencia fue auditada en el informe 026 §4 (25/25 literales de la nota respaldados
  verbatim), **excepto** los `n ~ 10^8`–`10^10`, que se tratan como no respaldados (§8).

## 3. Dossier

Ficheros y referencias suministrados al comité:

- `research_program/work_packages/wp4_comparable_pair_separation.md` (Anexo C; §2 setup EF, §3
  reducción, §4 Teo C4 / Lema C5 / Cor C6 + los dos pasos argumentados-no-escritos, §4b adenda de
  varianza (Props C7/C8, Teo C9, requisito §6.4), §5 ítems 1–4, §6 etiquetas)
- `research_program/work_packages/wp4_comparable_pair_separation_checks.py` (checks `[1]`–`[13]`)
- `research_program/bibliography/ficha_se_busca_tv_order_only.md` (§1.2 canal, §1.3 tres modos, §2,
  §2.1(A)(B), §2.2, §3 Formas L/U/D, §4 test de órbita, §5 asimetría/data processing, §6.3 Chebyshev,
  §6.4 chequeo de consistencia, §7.1, §8 vocabulario de estados, §9.1/§9.2)
- `research_program/work_packages/wp4_fisher_localization_floor.md` (§4 familia diamante, §5 cota
  superior y sus hipótesis, §5a Prop 6, Lema R, Props 1–5)
- `research_program/models/first_witness_pair_candidates.md` (FWP Lema 0 condicionamiento, Lema 1
  cópula, Teorema A, §4 rigidez)
- `research_program/synthesis/op12_tv_zero_3p1.md`, `research_program/synthesis/pr012_tv_curve_scope.md`
- `docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md` (disparador),
  `auditor_report_024/025` (precedente `AUDIT_FAIL` por número sin generador)
- `docs/hoja_de_ruta_24_jul_2026.md`, `docs/hoja_de_ruta_25_jul_2026.md`, `docs/roadmap.md`
- `docs/preregistration.md`, `docs/preregistration_001_addendum.md`, `docs/preregistration_002.md`,
  `docs/estimator_v2_seal.md`, `docs/estimator_v2_freeze.md`, `docs/marcador_reentrada_2026-07-19.md`
- `dev/explore_seeds.py` (`EXPLORE_POOL`, banda virgen reservada), `nachocausal/thresholds.py`
  (`DEV_SEEDS`), `requirements.txt`
- `formal/HorizonFormal/` (cobertura formal real), `CLAUDE.md`, `README.md`
- `biblioteca/1104.1039v3.pdf` (Reitzner–Schulte 2013), `biblioteca/0902.0306v1.pdf` (Janson 2011),
  `biblioteca/2507.01907v1.pdf` (Braun 2025), `biblioteca/Tsybakov_Nonparametric_Estimation.pdf`,
  `biblioteca/Asymptotic Statistics.pdf`, `biblioteca/derived-md/` (Bombelli 1987 PhD; *Discrete
  geometry of a small causal diamond*; Eichhorn–Gamito–Stokes, *Towards black-hole horizons and
  geodesic focusing in causal sets*)
- `docs/comite/comite_decision_042/043/044` (estilo de casa, vocabulario de etiquetas, cierre C1–C6)

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief

- **Proposed artefact(s):**
  - *For the documentary step itself: no new artefact and no run are needed.* The label change lives entirely in the two files already modified in the working tree (`research_program/bibliography/ficha_se_busca_tv_order_only.md`, `research_program/work_packages/wp4_comparable_pair_separation.md`) plus these minutes. **Condition:** the restatement must publish **zero new numeric literals**. The `n ~ 10^8`–`10^10` figures in DOSSIER §D exist in exactly one place in the repo — the auditor's own ad-hoc cross-check at `docs/auditor/auditor_report_026_...md:164-165` (`TV >= 0.542689 @ n=1.16e8`, `0.954269 @ n=1.16e9`, `0.550001/0.955000 @ n=1.36e9/1.36e10`) — and `grep -rn` over the repo (excluding `biblioteca/`) finds them nowhere else. They have **no generator, committed or uncommitted**. Publishing them in the ficha/note as-is would reproduce the exact defect that produced `AUDIT_VERDICT=AUDIT_FAIL`, `AUDIT_ERRORS=1` in `docs/auditor/auditor_report_024_...md:97,:211,:247` ("three load-bearing numbers have no committed generator").
  - *If the PI later authorises a generator* (a separate session): one appended block **check [14]** inside the existing `research_program/work_packages/wp4_comparable_pair_separation_checks.py`. No new file, no new module, no `CANDIDATE_7` directory (`docs/hoja_de_ruta_25_jul_2026.md` §4). This mirrors the remediation pattern that closed report 024 → `docs/auditor/auditor_report_025_...md` (finding 1 closed by adding printing block `[4b]` to the same script; see `..._checks.py:375` in HEAD).
  - Spec for check [14] (description only, not code): pure-deterministic, no RNG, no new imports beyond `numpy`/`sympy` already at `..._checks.py:32-34`, no file writes. It must emit, for the diamond of record `r_p=3.0, r_q=0.5, tau=1.0 vs tau'=1.2` at `dv ∈ {4, 0.02}`: (i) `Delta_p` from the existing `p_comparable` quadrature; (ii) the trivial-bound Chebyshev threshold `n*(eps)` solving `1 - 4(2n-3)/(n(n-1) Delta_p^2) = eps` for `eps ∈ {0.5, 0.95}`, using only `zeta_1, zeta_2 <= 1/4`; (iii) the same threshold with the exact `zeta_1` from `h1_zeta1`, to exhibit the ~9× prefactor gap between the trivial and exact variance; (iv) an explicit reprint of the caveat that `Ibar` is still uncomputed, so check `[13]` remains *stated, not executed*. It must `assert` the bound is monotone in `n` and lies in `[0,1]` so it exits non-zero on drift, as `[12]` already does (`assert abs(v_mc - v_f) < 4*se`, `..._checks.py:481`).

- **Environment & seal:**
  - Sealed numeric env = `requirements.txt:7` `numpy==1.26.4` (hard pin; `thresholds.assert_environment` hard-fails otherwise). Live venv introspected this session (`.venv/bin/python -c "import numpy,sympy,scipy"`): `numpy 1.26.4`, `sympy 1.14.0`, `scipy 1.17.1` — consistent with the pin and with the ranges `scipy>=1.11,<2` (`requirements.txt:15`), `sympy>=1.12,<2` (`:16`).
  - Seal SHA to re-verify with `make verify-seal`: `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, identical to the frozen record at `docs/preregistration_002.md:8` (chair verified this session; no drift). A documentary label change must leave it byte-identical — re-run `make verify-seal` after the commit as the cheapest no-drift assertion.
  - Package-diff-clean: the checks script is **off the sealed path** by construction — its docstring (`..._checks.py:10-14`) states it imports nothing from `nachocausal/`, and `grep -rn "wp4_comparable" tests/ Makefile scripts/` returns nothing, so it is not in `make test` and cannot perturb the sealed regression suite. `RESPECT_SEAL_FREEZE` holds.

- **Provenance capture:** any commit that publishes this label change must record: HEAD before/after (currently `90e3aad`); `make verify-seal` output verbatim; `python -m pip freeze` or at minimum the numpy/sympy/scipy triple above (**the note's existing literals were produced under sympy 1.14.0 and that is recorded nowhere in the repo**); `uname -srm`; the fixed-seed inventory of the script (`seed=20260725` in `p_monte_carlo`, `seed=4242+n` in `S_n_moments_mc`) — **neither touches `EXPLORE_POOL = 1_000_000..1_000_039` nor the reserved virgin band `[2_000_000, 2_999_999]` of `docs/preregistration_002.md:18`, so no virgin seed is burned**; the byte-identical double-run evidence (`diff -q` over two stdout captures, ~9 s runtime, already established in report 026 §4); and the timestamp of the stdout capture the note's literals were transcribed from.

- **Run mechanics:** for the documentary step, **no invocation at all** — the reversible pre-flight is everything up to `git add`, and the single committing step is the commit that flips the `[OPEN]` labels. If check [14] is later authorised: one foreground invocation, `.venv/bin/python research_program/work_packages/wp4_comparable_pair_separation_checks.py`, stdout captured whole; never backgrounded (it is short and its value is the full transcript). Clean abort = the script's own `assert`s propagate a non-zero exit before anything is transcribed; nothing is written to disk by the script, so an abort leaves zero residue. Publication order is load-bearing and non-negotiable: **script committed first, note/ficha literals second** — never the reverse.

- **Reproducibility risks / ambiguities:**
  - **The §4b generator is itself uncommitted right now.** `git diff --stat` shows `..._checks.py | 141 ++++`, and `git show HEAD:...checks.py | grep "\[10\]\|\[11\]\|\[12\]\|\[13\]"` returns nothing — only `[4b]` exists in HEAD. So every §4b literal (`zeta_1`, the `Var_MC` vs `Var_formula` table, the `Ibar` requirement) is currently backed by a **working-tree-only** script. Auditor 026 is correctly styled *precommit*; the standing rule binds at publication, so the script must land in the same commit as the note. Until it does, the mathematical chain's steps 3-5 are unbacked in the committed repo.
  - **Chain step 7 (the Chebyshev/trivial-bound route to `TV -> 1`) has no generator of any kind.** Steps 1, 3-5 map onto emitted checks (`[7]`,`[8]`,`[9]`; `[10]`,`[11]`,`[12]`); step 7 maps onto nothing. Check `[13]` prints the §6.4 *consistency* inequality (`..._checks.py:485-499`), not the TV lower bound. This is the single most important reproducibility fact for the adjudication: the new statement is a **new derivation**, and its algebra is fine (`8*sigma^2/Delta_mu^2` with `sigma^2 <= C(n,2)(2n-3)/4` and `Delta_mu = C(n,2)Delta_p` reduces exactly to `4(2n-3)/(n(n-1)Delta_p^2)`, matching ficha §6.3), but **no committed deterministic script emits it**.
  - **The `dv = 4` thresholds are `[NUMERICAL]`, not proved-chain, numbers.** Corollary C6 is asymptotic in `dv` with non-effective `dv_0`, and the note itself records that at `dv = 4` `p` *decreases* in `tau`, outside the asymptotic regime (`wp4_comparable_pair_separation.md:335-337`). Any published `n*` at `dv = 4` inherits that label and must carry it.
  - **Stale module docstring.** `..._checks.py:18-30` lists "Checks, in order" only through `[9]`, while `main()` emits `[4b]` and `[10]`-`[13]`. Minor, but it is the file's own provenance index and should be updated in the same commit; a future auditor reading the docstring would under-count the emitted checks.
  - **`Ibar` is still uncomputed**, so ficha §6.4 stays one-way and unexecuted (`..._checks.py:497-499`). No wording in the restatement may imply the consistency check passed. `[UNVERIFIED]` for these corners.
  - **sympy/scipy are range-pinned, not hard-pinned** (`requirements.txt:15-16`). The symbolic outputs of `[1]`-`[3]`, `[7]`, `[8]` are the ones most exposed to a minor-version change in `sympy`'s simplification; the exact producing versions are unrecorded. Low probability, cheap to eliminate by recording the triple in the note's run header.
  - **The auditor's cross-check numbers are not reproducible from this repo.** Report 026's independent computations (brute-force `Var` enumeration at `n=4,5,8,20`; `E[h_1^2]=5/18`; the `n*` values) live only as prose in the report. That is acceptable *for an audit* (it is exactly the independence that gives them value), but it means they cannot be cited as repo-anchored results — precedent: report 024 finding 5, where a non-reproducible `78` had to be explicitly demoted to "recorded as history, not as a result" (`docs/auditor/auditor_report_025_...md`, §4).
  - `NO_POST_HOC_TUNING` / `NO_THRESHOLD_LOOSENING` / `NO_GROUND_TRUTH_LEAKAGE`: nothing here touches a threshold, a seed band, an estimator or the hidden embedding; the statistic's scale-blindness is still actively tested by check `[6]` (`< 1e-15`). No exposure identified.

### Mathematician brief

- **Computability:** Everything the `fixed_n` chain uses is decidable on the order relation alone. The observed object is a finite **partial** (not total) order — the induced causet — and `S_n := #{unordered pairs (x,y) : x ≺ y or y ≺ x}` is literally the cardinality of the relation, i.e. `|≺|` read off the adjacency matrix: `O(n²)` from the relation, `O(1)` if the relation is stored as a count. No transitive closure, no link/covering computation, no embedding, no dimension estimate is required. In the null-box setting the poset is a **2-dimensional order** (intersection of the two null-coordinate linear orders, `first_witness_pair_candidates.md:33-49`, Lemma 1), so `S_n = C(n,2) − inv(π)` for the rank permutation `π` and is computable in `O(n log n)` **given a realizer**; from the abstract poset a realizer costs `O(n²)`. Cardinality `n` is itself readable from the poset (`ficha:61-68`), so conditioning on `N = n` is an operation the order-only observer can actually perform — the `fixed_n` channel is *not* ground-truth leakage. There is **no abstain/domain gate** here because no estimator and no localiser is being built: the object is binary two-point discrimination `D_τ` vs `D_τ'`. The only domain restriction is model-side admissibility `0 < r_q < τ_0 ≤ τ, τ' ≤ τ_1 < r_p` plus `dv < dv_0` (`wp4_comparable_pair_separation.md:192-203`). Caveat that belongs in the efficiency ledger: at `n ~ 10⁸–10¹⁰` the relation has `~10¹⁶–10²⁰` entries; `S_n` is *decidable* but not *computable in practice* at the cardinality the bound needs.

- **Order observable:** `S_n` = number of relations of the induced poset; equivalently `S_n / C(n,2)` is **Myrheim's ordering fraction**. Closed form of its mean: `E_τ[S_n] = C(n,2) p(τ)` exactly, with `p(τ) = P(two i.i.d. points of D_τ are comparable) = (1 + τ_K(c_τ))/2`, `τ_K` = Kendall's tau of the copula (`wp4_comparable_pair_separation.md:146-154`). It carries the signal because in a null box comparability **is** rank-concordance, so `p` is exactly a copula functional; the diamond's copula moves with `τ` at first order in the null lapse, `p(τ) = 1/2 + κ(r_p,r_q) τ dv + O(dv²)`, `κ > 0` (`:158-190`). Being a copula functional it is provably blind to the Theorem-A scale orbit (`ficha §4`; check [6], `< 1e-15`) — it cannot manufacture a spurious separation there.

- **Relevant invariants:** (i) **Ordering fraction** `f(N) := N_rel / C(N,2)` — defined and attributed to Myrheim in `biblioteca/derived-md/Bombelli_1987_PhD.md:904` ("the expected number of related pairs of elements … over the total number of pairs"), the oldest order-only invariant in the field; our `p` is exactly its expectation. (ii) **Myrheim–Meyer dimension**, the standard consumer of the ordering fraction (`biblioteca/derived-md/Discrete geometry of a small causal diamond.md:117`, "f₀(n) is one-half of Myrheim's ordering fraction"; `:54`, Meyer's `⟨C_k⟩`). (iii) **Chain abundances `C_k`** and (iv) longest chain / height — the natural next-order invariants (ficha §7.2–7.4), *not* used here. Relevant contrast: Eichhorn–Gamito–Stokes work with **links, ladders and local diagnostics** (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:77`, `:100`, `:152`), i.e. local/covering structure, whereas `S_n` is a **global order-2 average** — a different and strictly coarser handle.

- **Analytic / continuum target:** The benchmark is the Myrheim–Meyer flat value in `d = 2`: for a 1+1D Minkowski Alexandrov interval the ordering fraction is exactly `1/2` (independent uniform null coordinates ⇒ `P(concordant) = 2·(1/2)² = 1/2`, i.e. `τ_K = 0`; consistent with `Bombelli_1987_PhD.md:904`'s table and with `Discrete geometry…:117`). So `p − 1/2 = τ_K/2` is precisely the departure of the diamond's copula from independence, and Annex C's `p = 1/2 + κ τ dv + O(dv²)` says the leading departure is linear in the null lapse and **linear in the horizon parameter `τ`**. That is the whole continuum content: the observable approaches the Minkowski benchmark as the diamond degenerates (`dv → 0`), and its first-order deviation is the signal. It is *not* a horizon localiser and *not* a curvature/action estimator.

- **Independent re-derivation** (by hand, no code run):
  - **(a) CONFIRMED.** Let `μ_τ < μ_τ'`, `Δμ = μ_τ' − μ_τ`, `A = {S_n ≤ (μ_τ+μ_τ')/2}`. Two-sided Chebyshev at radius `Δμ/2` gives `Q_τ(Aᶜ) ≤ 4σ_τ²/Δμ²` and `Q_τ'(A) ≤ 4σ_τ'²/Δμ²`, so `TV ≥ Q_τ(A) − Q_τ'(A) ≥ 1 − 4(σ_τ² + σ_τ'²)/Δμ²`. The bound uses **`σ_τ² + σ_τ'²`**; ficha §6.3's `1 − 8σ²/Δμ²` (`ficha:430-434`) is the same statement with `σ² := max(σ_τ², σ_τ')²`, so the two agree and ficha §6.3 is correct as written. Substituting `Δμ = C(n,2)|Δ_p|` and `σ² ≤ C(n,2)(2n−3)/4` for both: `4·2·C(n,2)(2n−3)/4 / (C(n,2)²Δ_p²) = 2(2n−3)/(C(n,2)Δ_p²) = 4(2n−3)/(n(n−1)Δ_p²)`. The stated `fixed_n` form is **exactly right**. Constants checked: the asymptotic form is `8/(nΔ_p²)`; with `Δ_p = 1.143e−4` (`dv = 0.02`) and target deficit `0.45` I get `n = 1.361e9`, and with `Δ_p = 3.8755e−4` (`dv = 4`) and deficit `0.457311` I get `n = 1.165e8` — both reproduce the dossier's `1.36e9` and `1.16e8` to three digits. I also re-derived `κ(3, 0.5) = [(9 − 0.25) − 3·ln 6] / (18·6.25) = 3.374722/112.5 = 0.0299975`, giving leading `Δ_p = κ·dv·δ = 1.19990e−4` at `dv = 0.02, δ = 0.2`, matching `wp4_comparable_pair_separation.md:351` (`+1.199901e-04`) to six digits. **One correction to ficha §6.3:** its third bullet (`ficha:439-440`) says that without atom control "ni siquiera el paso Chebyshev es citable con TV". That is **wrong** as applied here — `TV(μ,ν) = sup_A|μ(A) − ν(A)| ≥ μ(A) − ν(A)` holds for any `A`, atoms or not. Anti-concentration is needed only for the *Gaussian-comparison* route, never for the two-moment route. This removes an apparent internal blocker.
  - **(b) CONFIRMED.** `h_1` and `f` both take values in `[0,1]`, so `ζ_2 = Var(f) = p(1−p) ≤ 1/4` (Bernoulli) and `ζ_1 = Var(h_1) ≤ 1/4` (Popoviciu on `[0,1]`). Both are **universal**, model-free, and require none of Annex C's quadrature. Then `Var(S_n) ≤ C(n,2)[2(n−2)/4 + 1/4] = C(n,2)(2n−3)/4`. ✓ Note the price: with the *actual* `ζ_1 ≈ 1/36` (`:252-266`) the same chain gives `n` smaller by a factor `≈ 9` (`~1.3e7` instead of `1.16e8` at `dv = 4`) — a free order-of-magnitude already sitting in §4b, though `ζ_1`'s value is `[NUMERICAL]` except its `dv → 0` limit.
  - **(c) CONFIRMED.** An order isomorphism is a bijection preserving `≺` in both directions, hence maps comparable pairs bijectively onto comparable pairs: `S_n` is a genuine isomorphism invariant, so it factors as `S_n = T ∘ Φ` and `L_τ(S_n) = T_# Q^n_τ`. Data processing for TV under any measurable map gives `TV(Q^n_τ, Q^n_τ') ≥ TV(L_τ(S_n), L_τ'(S_n))` — **the direction claimed**, and exactly the display at `ficha:399-405`. `n` is preserved by `Φ` (`ficha:61-68`), so `S_n` is well-defined on the iso class. Ties have probability zero (continuous positive copula density, FWP Lemma 1 `:45-49`), so the trichotomy `x ≺ y / y ≺ x / spacelike` is a.s. clean and `E[S_n] = C(n,2)p` is exact.
  - **(d) CONFIRMED, and the `fixed_n` route is self-contained.** By FWP Lemma 0 (`:23-31`) conditioning on `N = n` makes the `n` points **i.i.d.** from the normalised volume measure — so `S_n = Σ_{i<j} f(X_i,X_j)` is a genuine order-2 U-statistic on i.i.d. points, **not** a Poisson functional. Hand variance count: same pair → `C(n,2)` terms of `Var(f) = ζ_2`; pairs sharing exactly one index → `C(n,2)·2(n−2)` terms of `Cov(f_{ij}, f_{ik}) = E[h_1(X_i)²] − p² = Var(h_1) = ζ_1`; disjoint pairs → covariance `0` by independence. Hence `Var(S_n) = C(n,2)[2(n−2)ζ_1 + ζ_2]` exactly, matching `wp4_comparable_pair_separation.md:219-222` and the auditor's brute-force enumeration at `n = 4,5,8,20` (`auditor_report_026:94-97`). Reitzner–Schulte, Malliavin–Stein and de-Poissonisation are **not used anywhere** in this chain. The only external ingredients are Chebyshev's inequality and the variational definition of TV. (A textbook citation for the Hoeffding decomposition — Hoeffding 1948 / van der Vaart 1998 Ch. 12 — is `[UNVERIFIED, standard]`: I found no local copy; `biblioteca/Asymptotic Statistics.pdf` is Höpfner, not van der Vaart. Nothing is load-bearing on it, since the identity is elementary and re-derived above.)
  - **(e) CONFIRMED — the `1/2` is a theorem, not a fit.** `Δμ = C(n,2)|Δ_p| = Θ(n²)` exactly. `sd = sqrt(C(n,2)[2(n−2)ζ_1 + ζ_2]) = Θ(n^{3/2})` **provided `ζ_1 > 0`**, which is Proposition C8 (`:242-250`, proved: `h_1(p) = h_1(q) = 1` but `h_1 < 1` in the interior, `h_1` continuous on a compact ⇒ non-constant). So the ratio is `Θ(√n)`, with the *upper* bound `ζ_1 ≤ 1/4` supplying `TV → 1` and the *lower* bound `ζ_1 > 0` supplying the matching `O(√n)`. No Monte-Carlo number enters; the MC at `n = 5,10,20` only cross-checks the exact variance identity. Worth recording against `biblioteca/`: `Bombelli_1987_PhD.md:978` estimates the fluctuation of `N_rel` heuristically as `√N_rel ~ n` "since it is a sum of a large number of variables … the central limit theorem tells us that the fluctuations will be of the order of √N_rel". That heuristic treats relations as independent and is **off by a factor `√n`**: the non-degenerate first Hoeffding projection makes the true sd `Θ(n^{3/2})`, not `Θ(n)`. The `√n` (rather than `n`) signal-to-noise ratio is precisely the cost of that dependence.
  - **(f) CONFIRMED that `n^{−1/2}` is the optimal *rate*, REFUTED as a claim about the constant.** I read WP4 §5. Its bound `TV(Q^n_τ, Q^n_{τ+δ}) ≤ (|δ|/2)√(n·Ībar)` (`wp4_fisher_localization_floor.md:266-287`) rests on `H²(c_τ, c_{τ+δ}) ≤ (δ²/4)Ībar` at `:159`, which is the **integrated Cauchy–Schwarz bound along the parameter path**, *not* the QMD Taylor expansion at `:155`. It is therefore **non-asymptotic and valid for every `δ` with both `τ, τ+δ ∈ [τ_0, τ_1]`** — no small-`δ` restriction. Hypotheses, precisely: the §4 diamond family with fixed EF corners and `0 < r_q < τ_0 ≤ τ_1 < r_p`; Lemma R's regularity on the closed box (`:135-149`, score bounded uniformly ⇒ `Ībar = sup I < ∞`, Prop 4); the diamond is a null box so FWP Lemma 1 applies; both models conditioned on `N = n`. Since `TV(Q^n)` is by definition the supremum of `|E_τ φ − E_τ' φ|` over all (randomised) functions of the poset, this upper bound binds **every** order-only procedure. Consequently at `δ = c·n^{−1/2}` we get `TV ≤ (c/2)√Ībar`, which is `< 1` and can be made arbitrarily small — so **no order-only procedure separates at `δ = o(n^{−1/2})`**, and `S_n`, which succeeds whenever `δ√n ≫ √(32ζ_1)/(κ dv)`, is rate-optimal. Both thresholds live at `t := δ√n = O(1)`, exactly as Annex C `:271-282` says. What is **not** proved: optimality of the *constant*. `Ībar` is proved finite but never computed for these corners, so the ratio `[√(64ζ_1)/(κ dv)] / [1/√Ībar]` — the efficiency of `S_n` against the full poset — is unknown.
  - **(g) One real degeneracy found, and it is not hypothetical.** `Δ_p(dv) := p_{1.2}(dv) − p_{1.0}(dv)` is `+1.142952e−04` at `dv = 0.02` and `−3.875520e−04` at `dv = 4` (`wp4_comparable_pair_separation.md:351-352`, and §5(ii) `:338-340` explicitly notes `p` decreasing in `τ` at `dv = 4`). `p` is continuous in `dv` (integrals of analytic integrands over analytically varying domains, §4 argued step (i)). Therefore by the intermediate value theorem **there exists `dv* ∈ (0.02, 4)` with `Δ_p(dv*) = 0` exactly** — at which `S_n` is *exactly blind at the mean level* and the entire two-moment chain is vacuous, no matter how large `n` is. This is precisely the "exact cancellation" the PI asked about, it is guaranteed (not merely possible), and it is the sharpest reason the result must be labelled as holding only for `dv < dv_0` and never extrapolated in `dv`. Both endpoint values are `[NUMERICAL]`, but they sit 10–11 orders above quadrature noise (`:354-356`), so the sign change is not an artefact. Secondary, benign items: the bound is vacuous unless `n(n−1)Δ_p² > 4(2n−3)`, i.e. roughly `n > 8/Δ_p²`; `ζ_1 → 1/36 > 0` and `ζ_2 → 1/4`, so no variance degeneracy; integrality/atoms of `S_n` are harmless (see (a)).
  - **(h) CONFIRMED doubly non-effective, but the two non-effectivities have a single root.** Required cardinality: `n*(dv, δ) ≈ 8 / (ε κ² dv² δ²)` (hand-derived from (a) with `Δ_p ≈ κ dv δ`), so `n* ∝ dv^{−2} δ^{−2}` — verified numerically above against both dossier rows. Corollary C6's `dv_0` is non-effective (`:210-212`, no remainder bound computed), so the guaranteed regime is `dv` small, which is exactly where `n*` blows up: the theorem is *guaranteed* precisely where it is *most expensive*. That said, the two are not independent obstructions — a single missing ingredient (an explicit `O(dv²)` remainder bound, uniform in `τ`, i.e. the two steps §4 flags as "argued rather than written out", `:174-183`) would make `dv_0` **and** `n*(dv,δ)` effective simultaneously. Does it matter for the label? It does not damage the asymptotic-in-`n` statement (for each fixed admissible `dv < dv_0`, `TV → 1` as `n → ∞`), so `[PROVED — FIXED_N ASYMPTOTIC SEPARATION; NON-EFFECTIVE]` is honest — but "NON-EFFECTIVE" must be glossed as covering **both** senses, and the label must state that at the *named* pairs (`dv = 4`, `dv = 0.02`) the input `Δ_p ≠ 0` is `[NUMERICAL]`, not `[PROVED]`. The `δ^{−2}` half of the blow-up is **not** a pathology: it is the ordinary parametric `n ~ δ^{−2}` scaling and matches WP4 §5's floor exactly.
  - **Adjudication of the decision question.** **Q1 — YES, the chain is correct in `fixed_n`**, with one wording repair: what the chain needs is `Var(S_n) = O(n³)` (from `ζ ≤ 1/4` alone); `Var(S_n) = Θ(n³)` is true (Prop C8) but is used only for the matching `Θ(√n)` claim in (e). **Q2 — NO.** No Reitzner–Schulte, no de-Poissonisation, no CLT, no empirically fitted exponent. `Var(S_n)` here is a fixed-`n` i.i.d. U-statistic identity, and the Poisson channel is never entered. **Q3 — YES, partially.** The blanket `[OPEN]` at `wp4_comparable_pair_separation.md:381-382` and the presentation of de-Poissonisation as a Forma L blocker at `:317-320` are wrong for the `fixed_n` channel of candidate 7.1 on the WP4 §4 diamond family with `dv < dv_0`. They stay right everywhere else: other families (`[OPEN por par]`), candidates 7.2–7.4, the unconditioned Poisson channel, and Formas U and D. Also `ficha:147-151` ("no existe en el repo ninguna técnica para acotar `TV(Q)` por debajo") becomes false and must be **narrowed, not deleted** — the technique that exists is exactly the one ficha §5 `:399-405` already anticipated: order-only statistic + data processing + Chebyshev. **Q4 — the proposed label split is the right one**, provided the `[PROVED]` half is stated with its full quantifier structure and both non-effectivities (see (h)) and the `dv*` blindness of (g). I would name the second item `[OPEN — FINITE_N EFFICIENCY / CONSTANT-LEVEL INFORMATION EFFICIENCY]` and note it now has a *single scalar target* (below). **Q5 — roadmap:** drop de-Poissonisation as a `fixed_n` blocker; keep it exactly where it is still load-bearing (importing Reitzner–Schulte's CLT, i.e. the Poisson channel and any *distributional* upgrade of Chebyshev); promote to first priority the one number that closes both open questions at once — the `dv`-scaling of `Ībar` for these corners, since §6.4's unexecuted test (`ζ_1·Ībar ≥ κ²dv²/54`, `:271-287`) and the efficiency ratio of (f) are the **same** constant. Open no new observable and authorise no run; the analytic step is the written-out `O(dv²)` remainder bound. **Q6 — YES**, the `1/2` exponent is already proved by 1948-vintage mathematics (Hoeffding's variance decomposition, re-derived by hand in (d)) plus Chebyshev; nothing in this repo's `fixed_n` chain is new probability theory. **Q7 — grading the PI's sentence:** *"the root-n exponent is not the bottleneck"* — **PROVED**, in the precise sense that WP4 §5's non-asymptotic upper bound forbids any order-only procedure from beating `δ ~ n^{−1/2}` (see (f)). *"under the WP4 Fisher bound it is the expected and possibly optimal regular rate"* — the *rate* optimality is **PROVED**; "possibly optimal" as a statement about the **constant** is **INFERENCE**, and it is currently unquantifiable because `Ībar` is uncomputed. *"the visible problem is the prefactor"* — **INFERENCE**, but well-founded: I confirm the prefactor is the binding term (`n ≈ 8/(εκ²dv²δ²)`), and I confirm a factor-9 improvement is free from `ζ_1 ≈ 1/36`, plus a further constant-factor gain available from Cantelli or a CLT. *"or the information lost in compressing the whole poset to the single statistic `S_n`"* — **OPEN**, and now sharply statable: because `p = (1+τ_K)/2`, `S_n` compresses the entire copula to **one scalar** (Kendall's tau), whereas the full poset law determines the copula essentially completely (Janson Thm 7.1 via `ficha:159-187`). The compression loss is therefore infinite-dimensional in principle and its cost in TV is exactly the unquantified constant ratio of (f).

- **Caveats:**
  - The result adjudicated is **binary discrimination** between `D_τ` and `D_τ'` by a function of the poset. It is **not** horizon localisation, **not** metric reconstruction, **not** an estimator, **not** asymptotic-horizon, **not** 3+1D. `NO_RECONSTRUCTION_CLAIM` holds. Annex C `:336-342` already says so; any restatement must repeat it verbatim.
  - **Guaranteed exact blindness at some `dv* ∈ (0.02, 4)`** by IVT on the sign change at `wp4_comparable_pair_separation.md:351-352`. The statement must never be phrased as "`S_n` separates the diamond family"; only "for `dv < dv_0`". [anchored; endpoint values `[NUMERICAL]`]
  - `dv_0` is non-effective (`:210-212`) and the two steps underwriting Theorem C4 — analyticity of `p` in `dv` at `0⁺`, and uniformity in `τ` of the `O(dv²)` remainder — are **argued, not written out** (`:174-183`). The `[PROVED]` label inherits both gaps. Writing out the remainder bound is the single highest-value analytic step and makes the whole statement effective.
  - `ζ_1`'s numerical value is `[NUMERICAL]` (quadrature); only the `dv → 0` limit `1/36` is `[PROVED]` (`:372-377`). The Chebyshev chain does **not** depend on it — it uses only `ζ ≤ 1/4` — so this gap does not touch the `[PROVED]` claim, only the factor-9 sharpening.
  - `Ībar` for the diamond of record is **proved finite but never computed** (`wp4_fisher_localization_floor.md:151-159` proves finiteness; §5a has only `[NUMERICAL]` `V·Ībar` for one reference shape). Until it exists, ficha §6.4's mandatory consistency check (`:271-287`) is **stated, not executed**, and the optimality claim stops at the rate. One-way test: violation refutes, satisfaction proves nothing.
  - ficha §6.3's anti-concentration bullet (`ficha:439-440`) misstates the requirement for the Chebyshev step; it should be scoped to the Gaussian-comparison route only. [anchored, re-derived in (a)]
  - Computability at the required cardinality: `S_n` is `O(n²)` from the relation (or `O(n log n)` from a realizer), but `n ~ 10⁸–10¹⁰` puts both the relation and the sprinkling far outside anything runnable. This belongs in the EFFICIENCY column, and it is an additional, independent reason `[PROVED]` must not be read as "usable". `RESPECT_SEAL_FREEZE`, `NO_POST_HOC_TUNING`: nothing here authorises a run, a seed, or a threshold.
  - A textbook citation for the Hoeffding decomposition is `[UNVERIFIED, standard]` — no verified local copy (`biblioteca/Asymptotic Statistics.pdf` is Höpfner, not van der Vaart 1998). No claim depends on it: the identity is re-derived by hand in (d) and independently confirmed combinatorially at `auditor_report_026:94-97`.

### Mathematical logic brief

- **Formal status:**
  - **DEFINITIONS (no content to adjudicate):** `p(tau)` as comparability probability (`ficha:463-464`; note the §2.1(B) variant is *half* of it, `ficha:236-241`, `wp4_comparable_pair_separation.md:49-54`); `S_n` as comparable-pair count; `Q^n_tau := Phi_# P^n_tau`; the channel `fixed_n` (`ficha:56-59`, FWP Lemma 0 at `first_witness_pair_candidates.md:23`).
  - **PROVED, unconditionally:** `E_tau[S_n] = C(n,2) p(tau)` (exact, iid); `Var(S_n) = C(n,2)[2(n-2)zeta_1 + zeta_2]` (Hoeffding, independently re-derived by the auditor, `auditor_report_026...:94-97`); `zeta_1, zeta_2 <= 1/4` (trivial, kernel in `[0,1]`); `zeta_1 > 0` (Prop C8, `...separation.md:242-250`); data-processing `TV(Q^n) >= TV(L(S_n))` (`ficha:400-402`); the midpoint-Chebyshev inequality `TV >= 1 - 8 sigma^2/Delta_mu^2` (`ficha:429-434`); the WP4 §5 upper bound / localisation floor (`wp4_fisher_localization_floor.md:266-292`).
  - **THEOREM WITH ONE ADMITTED GAP:** `Delta_p != 0` for a *fixed* pair at small `dv` — Theorem C4 + Lemma C5 (`...separation.md:158-190`), inheriting only step **(i)** (analyticity of `p` in `dv` at `0^+`, `:175-178`), with `dv_0` non-effective (`:210-212`).
  - **THEOREM WITH TWO ADMITTED GAPS:** Corollary C6 in its *uniform* form (`:192-203`) — additionally step **(ii)**, uniformity in `tau` of the `O(dv^2)` remainder (`:179-183`).
  - **`[NUMERICAL]`:** the values `Delta_p = +1.142952e-04` (`dv=0.02`) and `-3.875520e-04` (`dv=4`) (`:349-352`); `zeta_1`'s value; the `O(dv^2)` order in Thm C9; every `n ~ 10^8`–`10^10` figure derived from them.
  - **STATED-NOT-EXECUTED (a potential defeater, not a premise):** `zeta_1 * Ibar >= kappa^2 dv^2/54` (`:268-287`).
  - **NO FORMAL BACKING ANYWHERE.** `formal/HorizonFormal/` exists and is `sorry`-free, but covers only posets/ideals/ends/accessibility/relational-horizon (`formal/HorizonFormal/HorizonFormal/*.lean`). Nothing probabilistic, no TV, no `S_n`, no copula. The new label may borrow **zero** credibility from `formal/`.

- **Quantifier / dependency order:**
  - **(a)** Corollary C6 as written places `dv_0` **before** `tau, tau'` ("there is `dv_0 > 0` — depending on those four numbers only — such that for all `0 < dv < dv_0`, the map `tau -> p(tau)` is strictly increasing on `[tau_0, tau_1]`", `:192-199`). That is the *strong* order, and its justification is exactly admitted step (ii) (`:179-183`) — the proof of C6 leans on it in one clause (`:201-203`). **But the `fixed_n` claim does not need it.** The claim under adjudication compares **two fixed** values `tau, tau'`, so Theorem C4 applied pointwise at each, with `dv_0 := min(dv_0(tau), dv_0(tau'))`, suffices. The honest sentence is therefore the *weak* order:
    `∀ admissible (r_p,r_q) ∀ tau != tau' in (r_q,r_p) ∃ dv_0 > 0 (non-effective) ∀ dv in (0,dv_0) ∀ eps>0 ∃ n_0 ∀ n >= n_0 : TV(Q^n_tau, Q^n_tau') >= 1 - eps.`
    Recommend the committee adopt exactly this sentence and **not** the uniform-over-compact version.
  - **(b)** Consequence: the `fixed_n` result is a **theorem with ONE admitted gap** (step (i)), not two. It is not a bare theorem and must not carry a bare `[PROVED]`; it is also not "conditional" in the hypothesis sense — nothing is assumed, one step of the proof is unwritten. Repo precedent for exactly this is `[PROVED (leading order)]` with the gaps named (`...separation.md:367-369`).
  - **Two non-effectivities, not one.** `dv_0` is non-effective (`:210-212`); and since no effective lower bound on `|Delta_p|` exists, the downstream `n_0 = O(1/Delta_p^2)` is non-effective **as a function of the inputs** too. A single unqualified word "NON-EFFECTIVE" does not carry both.
  - **(c) The quantifier trap is real and must be blocked in writing.** Two logically distinct statements: **S1** (existential-asymptotic, PROVED mod gap (i)): `∃ dv_0 ∀ dv < dv_0 : Delta_p != 0`. **S2** (concrete instance, `[NUMERICAL]`): at `r_p=3, r_q=0.5, tau=1.0, tau'=1.2, dv in {0.02, 4}`, `Delta_p` has the tabulated value. S1 supplies **no** `n`; every `n ~ 10^9` number descends from S2. Worse: at `dv = 4` the note itself proves the regime is outside the theorem — `p` there *decreases* in `tau`, sign-opposite to Theorem C4 (`:337-340`). So `TV >= 0.954269 @ n=1.16e9 (dv=4)` is a **purely numerical** claim about a point where the proved statement demonstrably does not apply. Conflating S1 and S2 would be the single most likely mis-citation of this label.
  - **Dependency graph of the new result (surprisingly thin):** `{Theorem C4 + Lemma C5}` → `Delta_p != 0`; `+ E S_n` exact; `+ zeta_1,zeta_2 <= 1/4` (trivial); `+ DPI`; `+ Chebyshev`. It does **not** depend on Prop C8, Thm C9, the value of `zeta_1`, Reitzner–Schulte, de-Poissonisation, or any fitted exponent. §4b is needed only for the *rate-sharpness* and *prefactor* discussion, not for Forma L. Therefore the new label does **not** inherit `zeta_1`'s `[NUMERICAL]` status.
  - **(g)** The `fixed_n` result is **logically independent** of the §6.4 check: both the Chebyshev lower bound and the WP4 §5 upper bound are independently `[PROVED]`. The check is therefore **not a hypothesis but a live defeater**: `zeta_1 * Ibar >= kappa^2 dv^2/54` is entailed by the conjunction of two proved theorems, so an executed violation would prove that one of the two proofs is wrong (candidates: Annex C's Chebyshev constants, or WP4 §5, which is itself an *a fortiori* point-level bound and explicitly "can therefore be loose for posets", `wp4_fisher_localization_floor.md:288-292`). It must appear in the label as a standing falsification hook, phrased as defeater-not-premise. It is unexecutable today because `Ibar` for these corners is unknown (`...separation.md:328-334`).
  - **Post-hoc degrees of freedom to watch:** `dv` is currently chosen *after* seeing `Delta_p` (two values reported, one inside and one outside the proved regime). Any future "pick the `dv` that gives the nicest `n`" is post-hoc tuning. Freeze `dv` in the text now. `NO_POST_HOC_TUNING`.

- **Equivalence claims:**
  - `p = (1 + tau_K(c_tau))/2` — a genuine **equality** (`:147-154`), and it is what makes the ficha §4 orbit test pass *by construction*, not by numerical luck. The `<1e-15` check [6] is confirmation, not proof; the proof is "`p` is a copula functional". Correctly one-directional as used (blindness to the Theorem-A orbit is a *necessary* condition passed, never evidence for Forma L).
  - `Delta_p != 0 ⟺ Forma L` is **false in both directions** as an equivalence and is not claimed: `⟸` is not asserted; `⟹` holds only after the variance + Chebyshev + DPI steps, exactly the ficha §9.2 second-bullet guardrail (`ficha:576`) — an isolated mean difference is not Forma L. The dossier's chain items 5→6 ("`Var = Theta(n^3)` vs gap `Theta(n^2 Delta_p)` ⟹ signal/sd `Theta(sqrt n)`") is **not** an inference to TV; only item 7 is. State it that way or the guardrail is being walked past.
  - "Injectivity of `tau -> c_tau` (WP4 Prop 5) ⟹ injectivity of `tau -> p(tau)`" — correctly identified as **invalid** and never used (`...separation.md:45-47`, `ficha:216-217`). Good.
  - **Rate-optimality is a two-sided claim and both sides are proved.** Achievability at `delta ~ n^{-1/2}` (Chebyshev + exact moments; the matching `Var = Theta(n^3)` direction needs Prop C8, PROVED); impossibility below `delta ~ 2/sqrt(n Ibar)` for **every** order-only estimator (`wp4_fisher_localization_floor.md:266-277`, conditional on `Ibar < infinity`, PROVED for this family by Lemma R/Prop 4). So the exponent match is a proved equality of *exponents* — not of constants.
  - `[UNVERIFIED]` in the ficha and never load-bearing here: Tsybakov §2.4 as the citation for the standard TV inequalities (`ficha:432`, `:550`). The Chebyshev step is one line and does not need the citation, but the ficha should say so rather than lean on an unverified reference.

- **Type / object discipline:**
  - **(d) The types are correct and the DPI direction is correct.** `Q^n_tau` is a law on `Iso_n`, the finite set of isomorphism classes of `n`-element posets; `TV` there is the discrete TV. `S_n` is the comparable-pair count, an **isomorphism invariant**, so it factors as `S_n = g ∘ Phi` with `g : Iso_n -> {0,...,C(n,2)}` well-defined on the quotient. Hence `L_tau(S_n) = g_# Q^n_tau` and DPI gives `TV(g_#Q, g_#Q') <= TV(Q, Q')`, i.e. `TV(Q^n_tau,Q^n_tau') >= TV(L(S_n))` — the **lower**-bounding direction, exactly as `ficha:400-402` prescribes and the opposite of the error `ficha:578-579` forbids. **No category mistake here.** The a.s.-no-ties premise (needed for the induced relation to be a strict partial order and for `p = 2P(X ≺ Y)`) is used and holds for the continuous sampling measure (`...separation.md:132-134`, Fact C0 at `:64-66`).
  - **Two live type hazards, both in the ficha, both cosmetic-but-committing:** (1) the factor-2 convention clash between §2.1(B) `p = ∫∫1[x≺y]` and §7.1 `p = P(comparable)` is *declared* (`ficha:236-241`) but **not fixed**; every Chebyshev constant moves by 4 if the two are mixed. Do not publish a label on top of an unfixed convention clash. (2) `ficha:463-471` mixes channels inside one numbered item: `E S_n = C(n,2) p` is `fixed_n`, `Var_theta S = Theta(lambda^3)` is unconditioned Poisson. Split them.
  - **A guardrail sentence that is over-broad and would, read literally, block this very chain:** `ficha:439-440` says that without atom control "ni siquiera el paso Chebyshev es citable con TV". That is **wrong as stated** — the midpoint-test bound `TV >= |P_tau(A) - P_tau'(A)|` with `A = {S_n < mid}` needs no anti-concentration whatsoever. Atoms genuinely block only the *Gaussian-comparison* route (`ficha:435-438`), where TV between an integer law and a Gaussian is 1. Narrow that bullet to the normal-approximation route.
  - **(e) What `TV -> 1` licenses, exactly:** the existence, for each **pre-specified** pair `(D_tau, D_tau')` in the WP4 §4 family and each small enough `dv`, of a sequence of order-only tests — threshold `S_n` at the midpoint — whose type-I + type-II error tends to 0 as `n -> infinity` in `fixed_n`. Equivalently: the two order-only laws are asymptotically mutually singular. **That is the entire content.**
    It does **not** license: a confidence set for `tau`; an estimator or localiser (converting pointwise pairwise tests into estimation needs uniform testing errors over a net — not available, and capped at `n^{-1/2}` anyway by WP4 §5); any statement about a pair *not* fixed in advance (that is the uniform form, which needs admitted step (ii)); "horizon localisation" — the horizon is fixed by construction inside each of the two models, and nothing is located *within* a given causal set; metric reconstruction; anything 3+1D, asymptotic, or bearing on the closed C1–C6 line. `NO_RECONSTRUCTION_CLAIM`.

- **Label adjudication (f):**
  - `[PROVED — FIXED_N ASYMPTOTIC SEPARATION; NON-EFFECTIVE]` **overstates in three ways and is ambiguous in two**: bare `[PROVED]` where the repo's own precedent for this exact chain is `[PROVED (leading order)]` with gaps named (`...separation.md:367-369`); "SEPARATION" does not distinguish separation-of-means from separation-in-TV (the §9.2 trap); it is silent on two-fixed-hypotheses-only; and "NON-EFFECTIVE" is un-typed — it names neither which object (`dv_0`) nor the second non-effectivity (`n_0`). Recommended replacement:

    `[PROVED (leading order in dv; Annex C §4 step (i) argued, not written) — TWO-POINT TEST CONSISTENCY, fixed_n CHANNEL, WP4 §4 DIAMOND FAMILY ONLY: for each fixed admissible (r_p, r_q, tau != tau') there EXISTS a NON-EFFECTIVE dv_0 > 0 such that for all 0 < dv < dv_0, TV(Q^n_tau, Q^n_tau') -> 1 as n -> infinity. NON-EFFECTIVE TWICE: dv_0, and n_0(dv, tau, tau'). NO UNIFORMITY IN (tau, tau') CLAIMED (that form would additionally need Annex C §4 step (ii)). Concrete-instance values of Delta_p and every finite n are [NUMERICAL], one of them (dv = 4) outside the proved regime. NOT AN ESTIMATOR, NOT LOCALISATION, NOT RECONSTRUCTION.]`

    Short table token: `FORMA_L_FUERTE_fixed_n = PROVED_LEADING_ORDER / NON_EFFECTIVE_x2 / TWO_POINT_ONLY / DIAMOND_FAMILY_ONLY`.
  - On the two §4 gaps in the label: **step (i) must appear** (it is inherited). **Step (ii) must not** — it is not used by the two-point form — but the label must *explicitly disclaim the uniform form*, otherwise a reader will silently upgrade the quantifier order and re-import gap (ii) without noticing.
  - `[OPEN — FINITE_N EFFICIENCY / CONSTANT-LEVEL INFORMATION EFFICIENCY]` **understates what is closed** (it leaves the reader thinking the `n^{-1/2}` exponent might be the problem, when exponent-optimality is proved on both sides) and **imports an undefined term** ("efficiency" has an estimator-theoretic meaning the repo has not defined and, per roadmap §4, must not open). Recommended replacement:

    `[OPEN — CONSTANT LEVEL ONLY. The exponent is settled: delta ~ n^{-1/2} is achieved by S_n (exact moments + Prop C8) and is unimprovable by ANY order-only procedure on this family (WP4 §5, PROVED, conditional on Ibar < infinity). What is open is the CONSTANT: (i) the true prefactor of TV(Q^n) — the Chebyshev route is provably conservative (factor 8 and the trivial zeta <= 1/4); (ii) the constant-level information loss of the compression Iso_n -> S_n; (iii) the ONE-WAY consistency check zeta_1 * Ibar >= kappa^2 dv^2 / 54, STATED AND UNEXECUTED (Ibar unknown for these corners), whose violation would refute one of the two PROVED bounds. No new observable, no CANDIDATE_7, no estimator.]`
  - **Answers to the decision question, compactly.** (1) The chain is **correct in `fixed_n`**, with one wording correction: `signal/sd -> infinity` is not itself a TV statement; the TV step is Chebyshev + DPI, and it needs only the *trivial* variance upper bound. (2) It needs **no** Reitzner–Schulte CLT, **no** de-Poissonisation, **no** fitted exponent; the `n = 5,10,20` Monte Carlo checks the exact variance formula only. (3) **Yes** — the blanket `[OPEN]` for Forma L in `fixed_n` (`...separation.md:381-382`, `ficha:273-281`) is logically wrong and should be replaced by the two labels above; `[OPEN]` remains correct for the *unconditioned Poisson* channel (item 1, the `N` confounder) and for all other families (`[OPEN por par]`). (4) The precise separator is the pair of labels above: existence-asymptotic vs constant-level. (5) Roadmap: **drop** "des-Poissonización" as a `fixed_n` blocker (`docs/hoja_de_ruta_25_jul_2026.md:86-88`) and re-scope it to "needed only to import the Reitzner–Schulte CLT, i.e. only in the Poisson channel and only for sharper constants"; **promote** the constant question — concretely `Ibar` for these corners, which is the one number that both executes the §6.4 defeater and quantifies the prefactor; **keep** every "No hacer" item at `:100-113` in force. (6) The `1/2` exponent is **already proved by existing repo mathematics**, both directions, for this family — nothing new is required. (7) The submitted sentence: *"root-n is not the bottleneck"* = **PROVED**; *"under the WP4 Fisher bound it is the expected regular rate"* = **PROVED**; *"possibly optimal"* = **understatement, the exponent-optimality is proved, only constant-optimality is open**; *"the visible problem is the prefactor"* = **INFERENCE**, and only about the prefactor *of this bound* (the true prefactor of `TV(Q^n)` is unknown, and the `10^8`–`10^10` figures are `[NUMERICAL]`); *"or the information lost in compressing to `S_n`"* = **OPEN, and not a genuine alternative** — since both `S_n` and the full channel scale as `n^{-1/2}`, any compression loss is confined to the constant, so the disjunction collapses into a single constant-level question, which is exactly the unexecuted §6.4 check.

- **Caveats:**
  - `formal/HorizonFormal/` is `sorry`-free but covers only order-theoretic ideals/ends/accessibility (`formal/HorizonFormal/HorizonFormal/{Posets,Ideals,Ends,Accessibility,Horizon,CofinalChains,ChainEnds}.lean`). **Zero** formal coverage of `S_n`, TV, copulas or `fixed_n`. The label must not be read as formally verified.
  - `auditor_report_026...:225-227` routes the change through "ficha §2.4 and roadmap §2.4"; **the ficha has no §2.4** — `grep -n "2\.4"` on the ficha returns only Tsybakov citations at `:432` and `:550`. The live routing rule is `docs/hoja_de_ruta_25_jul_2026.md:97-99` (and roadmap 24 jul §2.4). Minor mis-anchor in an otherwise sound report; fix before the report is cited.
  - The ficha's anti-concentration guardrail (`ficha:439-440`) is over-broad as written and, taken literally, would forbid the very Chebyshev step being adjudicated. Narrow it to the Gaussian-comparison route in the same edit as the label change, or the ficha will be self-contradictory.
  - The §2.1(B)/§7.1 factor-2 convention clash (`ficha:236-241`) is declared but unfixed; it moves Chebyshev constants by 4 if mixed. Fix in the same edit.
  - `dv = 4` is provably outside the regime of Theorem C4 (the sign of `dp/dtau` flips, `...separation.md:337-340`). Any future citation of `TV >= 0.954269 @ n = 1.16e9` must carry that fact, or it will read as a proved consequence of C6 when it is not.
  - The §6.4 defeater is unexecutable until `Ibar` is computed for these corners; computing it is a calculation of the same genre as Annex C, but authorising it is the warden's call, not mine. `RESPECT_SEAL_FREEZE`, `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`.
  - `[UNVERIFIED]` — I did not execute any script; all numerical values above are quoted from `...separation.md` §6/§4b and `auditor_report_026...` §4/§6 as committed text. My contributions are the quantifier analysis and the dependency graph, both derivable from the quoted statements alone.

### Physicist brief

Repo root for all paths below: `/home/adnac/nachocausal` (HEAD `90e3aad`).

- **Coordinates & patch:** The step lives entirely in ingoing Eddington–Finkelstein `(v, r)` with `g_tau = -(1 - tau/r) dv^2 + 2 dv dr` (`research_program/work_packages/wp4_comparable_pair_separation.md:60-62`; `research_program/work_packages/wp4_fisher_localization_floor.md:75-78`). `tau` **is** the horizon radius `r_s = 2M`, i.e. the mass parameter — the horizon is exactly the null ray `Utilde = 0`, and no outgoing ray crosses it (`wp4_comparable_pair_separation.md:76-80`). What "vary `tau` at fixed corners" means physically: `p = (v_p, r_p)` and `q = (v_q, r_q)` are held at **fixed areal radius and fixed ingoing-null label**, so changing `tau` compares two different black-hole masses seen at the *same* areal radii and the same null lapse `dv`. Because the corners do **not** scale with `tau`, this is the *reshaping* direction: the dimensionless ratios `r_p/tau`, `r_q/tau`, `dv/tau` all move, and all of the information sits there — `V(tau)*I(tau)` is exactly dilation-invariant, a pure shape functional (`wp4_fisher_localization_floor.md:325-332`, Proposition 6). The complementary direction, corners co-scaled with `tau`, is Theorem A and carries **`TV = 0` exactly for every `n`** (`research_program/models/first_witness_pair_candidates.md:83-96`). So even in the best case this family localises the horizon **relative to the fixed corners, in units set by the corners**; absolute `r_s` is provably unrecoverable. The patch `D_tau := J^+_tau(p) ∩ J^-_tau(q)` is compact with `min r = r_q > 0` (`wp4_fisher_localization_floor.md:99-103`) — the singularity is excluded by construction and there is no `J^+`. Finiteness therefore forfeits the event horizon outright: EGS state that "to define an event horizon in a causal set, an infinite sprinkling is required" (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:173`). Nothing here is an asymptotic-horizon claim, and nothing here is 3+1D.

- **Physical meaning of the signal:** `p(tau) = (1 + tau_K(c_tau))/2` with `tau_K` Kendall's tau; in a null box comparability *is* rank concordance, so `p` is exactly a copula functional and is provably blind to the Theorem-A scale orbit (verified `< 1e-15`, check [6]; `wp4_comparable_pair_separation.md:148-156`). `p = 1/2` is the 1+1D Minkowski interval value, so `p - 1/2` measures departure of the diamond's null-coordinate copula from independence. **My verdict on (c): this is a curvature/shape signature, not a horizon-locus signature.** Three anchored reasons. (i) The leading coefficient is `kappa(r_p, r_q) * tau * dv` and `kappa` is **proved positive for all `0 < r_q < r_p`, with no condition on `tau` whatsoever** (Lemma C5, `wp4_comparable_pair_separation.md:186-192`) — there is no threshold structure at `r = tau`, no sign change, nothing that fires *because* the diamond straddles the horizon. (ii) In this family `tau` is simultaneously the horizon radius and the *sole* curvature amplitude, `R_tau = -2 tau / r^3` (`wp4_fisher_localization_floor.md:174-180`); in 1+1D Schwarzschild there is only one dimensionful invariant, so "discriminating horizon radius" and "discriminating average curvature of the patch" are literally the same act. Calling the result horizon information is a naming convention, not an extra physical fact. (iii) The deformation is a boundary/shape effect — the ficha itself lists "forma del patch y borde entran vía la cópula" as a confounder of candidate 7.1 (`research_program/bibliography/ficha_se_busca_tv_order_only.md:481-484`). The straddling condition `r_q < tau < r_p` is needed only for `D_tau` to be a nondegenerate null box (`wp4_fisher_localization_floor.md:97-99`), not to generate `Delta_p`.

- **Sprinkling domain:** Declared region `D_tau` in the `(v, r)` chart; Poisson sprinkling of the volume measure, conditioned to `N = n`, whereupon the `n` points are i.i.d. from `vol/V` (FWP Lemma 0, `first_witness_pair_candidates.md:22-27`). **(b)** `det g_tau = -1` identically ⇒ `sqrt(-det g) = 1` ⇒ the sampling measure is flat Lebesgue `dv dr` (Fact C0, `wp4_comparable_pair_separation.md:64-68`). This is independently corroborated by EGS, who note the induced 1+1D metric has constant determinant "implying a constant sprinkling density … also if we use `(t*, r)` coordinates" (`derived-md/Towards black-hole horizons…:135`). What it buys: sprinkling is trivially implementable, and *all* `tau`-dependence is pushed into the region shape and the causal order — exactly the order-only purity the programme wants. What it hides: flatness of the *measure* is a 1+1D + EF-chart artifact and says nothing about the geometry (`R_tau = -2tau/r^3` is unchanged); the causal order is emphatically **not** Minkowski (rays obey `d rho/dD = (rho - tau)/(2 rho)`, `wp4_comparable_pair_separation.md:72-74`); and it does not survive to 3+1D. **(d)** `n ~ 10^8`–`10^10` is the fixed cardinality inside the *fixed* diamond, so it fixes the discreteness scale via `ell = sqrt(V/n)`. With `V(1.0) = 11.501608349297` and `n = 1.16e9` this is `ell ≈ 1.0e-4 * tau`; with `V = 0.049967998677` and `n = 1.36e10`, `ell ≈ 1.9e-6 * tau` `[UNVERIFIED — hand arithmetic this session, no script run]`. Physically that means the discreteness scale must be `10^4`–`10^6` times finer than the horizon radius: if `ell` is Planckian the hole is a `~10^4 ell_P` object (not an astrophysical black hole), and if `r_s` is astrophysical then `ell ~ 0.3 m` for a solar mass — not a fundamental discreteness scale in either reading. Computationally it is out of reach by a wide margin: the sealed bench's frozen intensity ladder is `{1500, 3000, 6000, 12000}` (`docs/preregistration_001_addendum.md:44`), so `n ~ 10^9` is `~10^5` times the largest level ever run here, and EGS themselves work at `n = 10^3` (`derived-md/Towards black-hole horizons…:186`). `S_n` also ranges over `C(n,2) ~ 5*10^17` pairs. **(f)** Conditioning on `N = n` genuinely removes the volume channel, formally and physically. Formally: under Lemma 0 the sample law is `vol/V`, in which `V` is divided out; `Q^n_tau` depends on `tau` only through the copula `c_tau` (FWP Lemma 1(2), `first_witness_pair_candidates.md:29-47`), and a copula is invariant under per-coordinate increasing reparametrisation, so `V(tau)` is **not a function of the fixed-`n` poset law at all** — there is no residual for it to leak through. Physically: the observer is handed exactly `n` elements in both worlds; total volume is a global scale, and the pure-scale direction is precisely the Theorem-A orbit to which `p` is blind to `< 1e-15`. The residual `Delta_p = kappa * tau * dv + O(dv^2)` is dilation-invariant (`kappa` homogeneous of degree `-2`, `wp4_comparable_pair_separation.md:194-198`), i.e. it is shape, not size. I confirm no residual geometric-volume leakage survives conditioning. Forfeited by this choice: the honest `fixed_n` channel *discards* the real Poisson `N` fluctuation that a physical sprinkling would carry, so the result is strictly weaker than what a real bench would see — which is the correct direction to err.

- **Claim boundary:** `TV(Q^n_tau, Q^n_tau') -> 1` says exactly: given `n` elements and only the unlabelled order, a threshold test on `S_n` eventually separates the **two fixed completions `D_1.0` and `D_1.2`**. It is **NOT horizon localisation** — no locus `r = 2M` is produced, no element or subset of the causet is labelled "horizon", no `r`-coordinate is emitted. It is **NOT reconstruction** — Theorem A shows the entire dilation orbit is a single poset law at every `n`, so absolute `r_s` is provably unrecoverable. It is **NOT estimation of `tau`** — the family's own floor forbids any order-only estimator from doing better than `~ell/sqrt(kappa_bar)`, numerically `~35 ell` for one moderate reference shape and degrading as `~ell/lambda^3` toward thin near-horizon diamonds (`wp4_fisher_localization_floor.md:363-386`). It is **NOT 3+1D and NOT an asymptotic/event-horizon statement** (`derived-md/Towards black-hole horizons…:173`; op12's 3+1D analogue of exactly this "patches no coescalados con `M`" is listed as **open**, `research_program/synthesis/op12_tv_zero_3p1.md:151-160`). **(e), the 1+1D cost:** the ficha records that `d = 2` is excluded from Braun-type identifiability because HKMM rigidity fails there (`ficha_se_busca_tv_order_only.md:545`). Concretely this costs the leverage step: in 1+1D order alone fixes only the conformal class, which is locally trivial, so geometry enters the poset *only* through the volume element — and `fixed_n` deliberately quotients the volume out. Everything therefore rests on the shape of one compact region in null coordinates. No continuum rigidity theorem can promote "the two poset laws differ" to "the two spacetimes are distinguished as geometries", and there is no route from here to 3+1D.
  - **(1) Chain correct in `fixed_n`? YES, with one caveat.** `E_tau[S_n] = C(n,2) p(tau)` and `Var(S_n) = C(n,2)[2(n-2) zeta_1 + zeta_2]` are the *i.i.d./binomial* U-statistic moments, native to `fixed_n` by Lemma 0 — no Poisson object appears. `S_n` is an order-isomorphism invariant, so data processing gives `TV(Q^n) >= TV(law S_n)` in the right direction, and Chebyshev with `zeta_1, zeta_2 <= 1/4` (automatic: `h_1, f` take values in `[0,1]`) yields the stated bound; I reproduce `8 sigma^2/Delta_mu^2 = 4(2n-3)/(n(n-1) Delta_p^2)` by hand `[UNVERIFIED — arithmetic, no script]`. **Caveat:** `Delta_p != 0` is `[PROVED]` only for `dv < dv_0` with `dv_0` non-effective (Corollary C6, `wp4_comparable_pair_separation.md:200-212`), and at the *named* `dv = 4` and `dv = 0.02` it is `[NUMERICAL]`. So the honest statement is "for all sufficiently small (unquantified) `dv`, `TV -> 1`", plus a numerical inequality at two named `dv`. Neither is "at `dv = 0.02`, PROVED".
  - **(2) Needs Reitzner–Schulte / de-Poissonisation / a fitted exponent? NO to all three.** Chebyshev needs two moments, both exact in `fixed_n`. RS lives in the unconditioned Poisson channel where `V(tau) != V(tau')` contaminates via the marginal `N` (`ficha:61-68`, `wp4_comparable_pair_separation.md` §5 item 1) — dropping it is a *purification*, not a loss. No exponent was fitted; the MC at `n = 5, 10, 20` only validates the exact variance identity (auditor 026 §4).
  - **(3) Should the ficha stop labelling all of Forma L `[OPEN]` in `fixed_n`? YES, narrowly.** Ficha §3 Forma L (strong) asks only for `f_lambda -> 1` in a declared §1.3 regime with no requirement on the constant (`ficha:300-308`); mode 3 (`fixed_n`, `n -> infinity`) is declared, and physically it *is* the continuum limit `rho -> infinity` at fixed patch, the programme-relevant regime (`ficha:71-76`). It must remain `[OPEN]` for every other family (`[OPEN por par]`), in the Poisson channel, and for any effective/finite-`n` reading.
  - **(4) Label I recommend:** two fields, never one. `FORMA_L_FUERTE [PROVED — asintótico, constantes no efectivas]` scoped to *canal `fixed_n`, familia diamante WP4 §4, par `(1.0, 1.2)`, régimen `dv < dv_0` no efectivo*; and separately `EFICIENCIA/UTILIDAD_A_n_FINITO [OPEN]` with the anchored gap `n_* ~ 10^9` vs sealed-bench `N <= 12000`.
  - **(5) Roadmap:** drop de-Poissonisation as a `fixed_n` blocker (it was never on this path); keep it *only* if someone ever wants the Poisson-channel or `S/C(N,2)` variant — which ficha §1.2/§9.2 already disallow as contaminated, so it arguably drops entirely. Promote to top priority the single missing number `Ibar` for **these** corners: it is a deterministic quadrature of an object already defined and already implemented for another shape (`wp4_kappa_numeric_reference.py`), it closes ficha §6.4's one-way check `zeta_1 * Ibar >= kappa^2 dv^2/54`, and it is the only way to quantify the compression loss. **No new observable, no `CANDIDATE_7`, no bench run, no seeds** — consistent with `docs/hoja_de_ruta_25_jul_2026.md:100-122`.
  - **(6) Is the `1/2` exponent proved? Split it.** (a) Signal/sd `= Theta(n^{1/2})` for `S_n`: **PROVED**, given the exact variance identity plus `zeta_1 > 0` strictly (Prop C8). (b) `delta ~ n^{-1/2}` as a *floor* on any order-only estimator: **PROVED** (`wp4_fisher_localization_floor.md:266-290`). (c) `n^{-1/2}` as an *attained estimation rate*: **NOT proved** — `S_n` supplies a two-point test, not an estimator, and building one is forbidden. (d) The `O(dv^2)` exponent of `zeta_1 - 1/36` is `[NUMERICAL]` only (ratios `2.17 … 3.85 -> 4`), but it is not on the `TV -> 1` path.
  - **(7) On the PI's sentence.** **Proved:** the exponent is not the bottleneck — `S_n`'s `sqrt(n)` matches the family's proved floor scale, both thresholds sitting at `delta ~ n^{-1/2}` (`wp4_comparable_pair_separation.md` §5 item 3). **Inference (mine, `[UNVERIFIED — hand arithmetic]`):** the `10^9` decomposes into two very unequal parts. Chebyshev slack: a standard i.i.d. U-statistic CLT (Hoeffding-type; non-degeneracy is exactly Prop C8's `zeta_1 > 0`) would need `Delta_mu/sigma ≈ 3.92` for `TV ≈ 0.95`, i.e. `n ≈ (0.92/Delta_p)^2 ≈ 6*10^6` at `dv = 4` — roughly `200x` better than `1.16e9`, and this route is already written in the ficha (`ficha:432-438`, the normal-approximation bullet), needing no new observable. Compression loss: setting WP4 §5's *upper* bound `(delta/2) sqrt(n Ibar) ≈ 1` with the reference-shape `Ibar ≈ 5.4e-4` gives a necessary `n >~ 2*10^5` for **any** statistic, so `S_n` would sit within `~30x` in `n` (`~5x` in `delta`) of the information-theoretic minimum — but that `Ibar` belongs to a **different diamond** (`r_p=2, r_q=0.5, v_q-v_p=1`), so this figure is illustrative only and collapses the moment `Ibar` for the diamond of record is computed. **Stays open:** `Ibar` for these corners; effective `dv_0`; whether the full poset beats `S_n` by `O(1)` or by orders (this is literally ficha §3's Forma D question, `ficha:321-338`); and whether any `n` here is physically or computationally meaningful. **Word to strike:** "possibly optimal" unqualified — the floor is a **two-point** bound, not minimax (the annex corrects that wording itself, `wp4_fisher_localization_floor.md:487-489`), it is an *upper* bound on `TV` and hence "can therefore be loose for posets" by the authors' own admission (`wp4_fisher_localization_floor.md:293-297`). It forbids doing better; it never certifies that `sqrt(n)` is attainable. The defensible phrasing is "rate-optimal among regular procedures on this named family".

- **Caveats:**
  - The signal is not horizon-specific: `kappa > 0` holds for every `0 < r_q < r_p` with no `tau`-threshold (`wp4_comparable_pair_separation.md:186-192`). Nothing in the derivation detects the locus `r = tau`. `NO_RECONSTRUCTION_CLAIM`.
  - `p` is not globally monotone in `tau`: at `dv = 4` it **decreases** (`0.548382340298801` vs `0.547994788251956`, `wp4_comparable_pair_separation.md:334-337`). The theorem is asymptotic in `dv`; no physical "more mass ⇒ more comparable pairs" reading is licensed.
  - The two named `Delta_p` values are `[NUMERICAL]` at working precision, not proved; `dv_0` is non-effective (`wp4_comparable_pair_separation.md:214-217`). This is the weakest link in the chain and must be labelled as such.
  - Two steps of Theorem C4 are argued, not written: analyticity of `p` in `dv` at `0^+`, and uniformity in `tau` of the `O(dv^2)` remainder (`wp4_comparable_pair_separation.md:169-178`). The second is the one Corollary C6 actually leans on.
  - `n ~ 10^9`–`10^10` implies `ell ~ 10^{-4}`–`10^{-6}` of the horizon radius and exceeds the sealed bench's largest level (`12000`, `docs/preregistration_001_addendum.md:44`) by `~10^5`. `[UNVERIFIED — ell figures are hand arithmetic this session.]` The result is asymptotic existence, not a runnable experiment.
  - `Ibar` for the diamond of record is missing, so ficha §6.4's one-way consistency check is derived but **unexecuted** (`wp4_comparable_pair_separation.md:290-300`). Until it runs, the chain has not been tested against the proved upper bound at the level of constants — and a violation would refute it.
  - The `~35 ell` reference floor and the `kappa_bar ~ lambda^6` reshaping degradation are `[NUMERICAL]` for **one** shape, not this one (`wp4_fisher_localization_floor.md:363-386`). Do not transport them to the diamond of record.
  - Nothing in this step touches the seal, the hidden embedding, or any bench artifact — see the ground-truth bullet below.
  - **(g) Ground truth / hidden embedding: NO, categorically.** This is a continuum calculation — symbolic algebra, deterministic quadrature, one seeded MC that only cross-checks the quadrature. There is no estimator, no sprinkling of the bench geometry, no seed band, no threshold, no validation artifact, and nothing imports from `nachocausal/` (`wp4_comparable_pair_separation.md:3-8`). Seal verified unchanged this session (`6e2c8838…` = `docs/preregistration_002.md:8`). What would change the answer: (i) implementing `S_n` as an observable and scoring it against sprinkled causets; (ii) using any embedding coordinate — including `r_p, r_q, tau` themselves — inside a decision rule rather than inside a proof; (iii) tuning `dv`, the corners, or `n` after seeing any separation number. All three are exactly what `docs/hoja_de_ruta_25_jul_2026.md:100-112` forbids. `RESPECT_SEAL_FREEZE`, `NO_GROUND_TRUTH_LEAKAGE`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`.

## 5. Falsifier attack

- Concrete failure modes:
  1. **The mathematics survives attack; the packaging does not.** I attacked each link: midpoint-Chebyshev (`docs/auditor/auditor_report_026_...md:155-161`) re-derives to exactly `1 - 4(2n-3)/(n(n-1)Delta_p^2)` — algebra correct, only `Var = O(n^3)` (Popoviciu `zeta_1, zeta_2 <= 1/4`) is used, so the chain does not inherit `zeta_1`'s `[NUMERICAL]` status; DPI direction correct (`ficha:399-405`); no Reitzner–Schulte / de-Poissonisation anywhere (`fixed_n` is a genuine iid U-statistic, FWP Lemma 0); the `1/2` exponent is Hoeffding-vintage theorem, not a fit. **Q1 YES (with the `O` not `Theta` wording repair), Q2 NO×3, Q6 YES.** The attackable surface is entirely in the label and the literals, below.
  2. **The load-bearing `n ~ 10^8–10^10` literals are irreproducible prose.** They exist only in the auditor's own report (`auditor_report_026:164-166`); HEAD's checks script contains none of checks `[10]-[13]` (`git show HEAD:...checks.py | grep '\[10\]...'` → 0 hits) and even the working-tree `[13]` prints the §6.4 inequality, not the TV bound. Publishing them reproduces verbatim the defect that produced `AUDIT_FAIL` in report 024 (numbers with no committed generator).
  3. **The flagship instance sits outside the proved regime.** `TV >= 0.954269 @ n=1.16e9` is at `dv=4`, where the note itself proves `p` decreases in `tau` — sign-opposite to Theorem C4 (`...separation.md:338-340, 351-352`). Citing it as an instance of the theorem is the single most likely mis-citation.
  4. **Mathematician's finding (g) is CORRECT and I extend it to a live falsification.** `Delta_p` is `+1.143e-4` at `dv=0.02` and `-3.876e-4` at `dv=4` (`...separation.md:349-352`), `p` continuous in `dv` (ratio of analytic integrals, `Vhat(0) != 0`, `:167-176`), so IVT guarantees `dv* in (0.02,4)` with `Delta_p(dv*)=0`: the two-moment chain is vacuous there for every `n`. This does **not** break the small-`dv` theorem (Theorem C4 gives `Delta_p = kappa*(tau'-tau)*dv + O(dv^2)`, `kappa>0`, hence no zero below `dv_0`) — it **bounds scope** and forbids any `dv`-extrapolation. But it **falsifies ficha:483-485 as written**: "el estadístico nunca es ciego ahí" is FALSE for the family at large; blindness at `dv*` is guaranteed, not hypothetical. That sentence must be scoped to `dv < dv_0` in the same commit as any upgrade.
  5. **The bare proposed label over-claims.** `[PROVED — FIXED_N ASYMPTOTIC SEPARATION; NON-EFFECTIVE]` hides: gap (i) (analyticity, "argued rather than written out", `...separation.md:174-183`); doubly non-effective (`dv_0` AND `n_0`, with `n* ∝ dv^{-2}delta^{-2}` — guaranteed exactly where most expensive); two-point-only, diamond-family-only. Repo precedent demands `[PROVED (leading order)]` with gaps named (`:367-369`). The logician's replacement label is the only publishable form.
  6. **Internal contradictions must fall with the upgrade or the ficha self-refutes:** `ficha:439-440` ("sin control de átomos ni siquiera el paso Chebyshev es citable con TV") literally blocks this very chain and is wrong — `TV >= mu(A)-nu(A)` needs no atom control; `ficha:147-151` ("no existe ninguna técnica para acotar TV(Q) por debajo") becomes false and must be narrowed, not deleted; the §2.1(B)/§7.1 factor-2 convention clash (`ficha:236-241`) moves every Chebyshev constant by 4 if mixed and is declared-not-fixed.
  7. Minor but real: `auditor_report_026:225` routes through "ficha §2.4", which does not exist; live rule is `docs/hoja_de_ruta_25_jul_2026.md:97-99`.
- Ground-truth leakage: **None found.** Pure continuum quadrature/symbolic calculation; `...checks.py:11` "imports nothing from `nachocausal/`", confirmed by import inspection (`:32-34`: numpy/sympy/scipy only); `fixed_n` conditioning provably quotients out `V(tau)` (copula invariance, FWP Lemma 1), so the hidden embedding neither defines nor scores anything here. Seal intact (`make verify-seal` = `docs/preregistration_002.md:8`).
- Freeze violations: no thresholds touched, no virgin seed burned (seeds `20260725`, `4242+n` outside `[2_000_000, 2_999_999]`), script off the sealed path. Two smuggling routes to block: (i) `dv in {0.02, 4}` was chosen after seeing `Delta_p` — one value inside, one outside the proved regime; freeze the quoted `dv` in the text NOW or the pair reads as post-hoc selection; (ii) publication order — committing the label before checks `[10]-[13]` land in the same commit would publish literals with no generator (`NO_POST_HOC_TUNING`, report-024 precedent).
- Verdict coercion: the §6.4 check `zeta_1*Ibar >= kappa^2 dv^2/54` is one-way ("satisfaction proves nothing", `...separation.md:330-335`) and unexecuted (`Ibar` missing); the label must carry it as a **standing defeater**, not a satisfied premise, and must never let its future satisfaction be read as PASS. The sealed benchmark verdicts are untouched; no abstain is coerced. Watch one asymmetry: `[PROVED asymptotic]` next to `[OPEN finite-n]` invites readers to collapse the pair into "works"; the label must state NON-EFFECTIVE TWICE explicitly.
- Premature / over-broad claims: this is a **two-point test-consistency** statement on one named diamond family — NOT an estimator, NOT a confidence set, NOT horizon localisation (physicist: no threshold structure at `r = tau`; `kappa>0` for all `0<r_q<r_p`; it is a curvature/shape signature — `ficha:481-484` lists shape/boundary as confounders), NOT reconstruction, NOT 3+1D, NOT asymptotic-horizon (EGS: event horizon needs infinite sprinkling). `n ~ 10^9` is `~10^5×` the frozen intensity ladder max (`docs/preregistration_001_addendum.md:44`). "Possibly optimal" must be struck: rate-optimality is proved (WP4 §5 floor, non-asymptotic via `wp4_fisher_localization_floor.md:159`), constant-optimality is not, and the floor "can be loose for posets" by its own admission (`:293-297`). `NO_RECONSTRUCTION_CLAIM`.
- Attack on the status quo: **Yes, leaving `[OPEN]` is itself a defect, and a serious one.** `...separation.md:381-382` labels Forma L for 7.1 `[OPEN]` with §5 items 1–2 as "live blockers"; item 2 (de-Poissonisation) was **never on the `fixed_n` path** — the chain uses only Hoeffding + Chebyshev on iid points. Consequence: roadmap priority 2 (`hoja_de_ruta_25_jul_2026.md:86-87`) commissions a literature hunt for a transfer theorem that is not needed, and `ficha:147-151` keeps a now-false "no technique exists" claim in circulation, actively suppressing the repo's first proved TV-lower-bound instance. A knowingly-wrong pessimistic label corrupts the ledger exactly as an optimistic one does. **Which failure is worse here:** the bare upgrade label is worse than the status quo (this repo's founding threat model is fake positives, and the mis-citation surface in items 2–5 is large); but the status quo is worse than the **logician's tightened label**, which dominates both. Refusing any upgrade is therefore the second-worst option, not the safe one.
- Independent-falsification gate: **Satisfied for the chain, FAILED for the literals.** The chain has three independent verifications (WP4 author; auditor 026 ad-hoc; causet mathematician by hand this session). The `n ~ 10^9` figures have exactly one source — the auditor, who is thus author and sole verifier of numbers with no committed generator; they may not be published until a deterministic script emits them.
- Minimal falsification test: ONE committed deterministic check (future session, not now — describe only): extend `..._checks.py` with a check `[14]` that (a) recomputes `Delta_p(dv)` by the existing quadrature on a fixed grid over `[0.02, 4]` and brackets the sign change, emitting an interval for `dv*` (executes the IVT blindness point, exposing failure mode 4 and any published `dv` sitting near it), and (b) prints `1 - 4(2n-3)/(n(n-1)Delta_p^2)` at the exact `n` values to be quoted, making every TV literal script-emitted (kills failure modes 2–3). If any quoted literal fails to reproduce, the upgrade is falsified as packaged; if `dv*` brackets near a quoted `dv`, the scoping is falsified. `RESPECT_SEAL_FREEZE` — the check touches no seeds, thresholds, or validation artifacts.

## 6. Pre-registration verdict

- **Verdict: PASS** (the documentary re-label is permitted to proceed to `/comite` adjudication; it does not itself touch anything frozen)

- **Freeze status:** All thresholds for prereg-002 are frozen in writing at `docs/preregistration_002.md:1-9` ("FROZEN pre-registration... After this commit nothing here may be tuned on a result") with seal SHA `6e2c3888…bfefd4` fixed before any validation seed was seen (validation seeds drawn blind `docs/preregistration_002.md:14-27`, one-way rule `:61-68`). **(a) Confirmed no FROZEN object is touched**: `git status --short` this session shows only `research_program/bibliography/ficha_se_busca_tv_order_only.md`, `research_program/work_packages/wp4_comparable_pair_separation.md`, `wp4_comparable_pair_separation_checks.py` (all self-declared non-frozen: ficha `:1` "BORRADOR/EXPLORACION", wp4 note `:1-9` "Working draft, REVISABLE, not frozen") plus untracked `docs/auditor/auditor_report_026_...md`. `nachocausal/thresholds.py` is absent from `git status --short` (verified directly: `git status --short -- nachocausal/thresholds.py` → no output) and its live SHA still matches `docs/preregistration_002.md:8` (`make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, confirmed by me independently and by the auditor §3). `docs/preregistration.md`, `docs/preregistration_002.md`, `docs/estimator_v2_seal.md`/`_freeze.md` are untouched (not in `git status --short`). No prereg-003 exists. Nothing under discussion is a prereg document, a threshold, or the seal — it is a status label (`[OPEN]`→scoped `[PROVED]`) on two exploratory documents that are explicitly not frozen.

- **Seal integrity:** Unaffected — the sealed path is not run. Seal SHA `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` matches `docs/preregistration_002.md:8` with no drift (confirmed independently and by auditor_report_026 §3). `grep -rn "wp4_comparable" tests/ Makefile scripts/` (reproducibility engineer, cited) returns nothing — the WP4 script has no contact with the sealed path; its imports are `numpy`, `sympy`, `scipy.special.lambertw` only (`wp4_comparable_pair_separation_checks.py`, per auditor §5).

- **Seed discipline:** PASS. The two literals in question are `20260725` (`wp4_comparable_pair_separation_checks.py:86`, `p_monte_carlo`'s fixed-seed quadrature cross-check) and `4242+n` (`:473`, `S_n_moments_mc`'s seeded variance-formula check). I confirmed directly: `DEV_SEEDS = (20240617, 13, 101, 7, 42, 99, 2718, 31415)` (`nachocausal/thresholds.py:57`); `EXPLORE_POOL = 1_000_000..1_000_039` (`dev/explore_seeds.py:24`); the reserved virgin band is `[2_000_000, 2_999_999]` (`dev/explore_seeds.py:29`, `docs/preregistration_002.md:16-17`). Neither `20260725` nor any `4242+n` for plausible small `n` (5, 10, 20 per the note) falls in `DEV_SEEDS`, `EXPLORE_POOL`, or the reserved band — they are ordinary Python literals for a continuum quadrature/MC cross-check that "builds no causal set through the sealed generator, evaluates no estimator, consumes no reserved seed band" (auditor_report_026 §5). No virgin seed burned.

- **Reporting rule:** The founding symmetric rule is `docs/preregistration.md:55-57` ("Unmet principled thresholds are informative… not a licence to loosen") and `docs/preregistration_002.md:64-68` ("the outcome — PASS, FAIL, INCONCLUSIVE, or OUT_OF_DOMAIN — is recorded and reported regardless of which it is… An unmet principled threshold is informative, never a licence to retune"). Nothing in either founding text distinguishes over- from under-claiming — the discipline is "report the true status," full stop. Per (g): **yes, symmetric, and binding equally here.** The audit (`auditor_report_026_...md:145-146`, "Finding 1 (WARN, headline) — the note UNDER-claims") found the *opposite* failure mode from what this skill exists to catch, and its own verdict text (`:174-176`) says an incorrectly pessimistic label "misroutes [effort] just as a wrongly optimistic one would." Refusing to correct a verified under-claim is not neutral caution; it is itself a departure from the "report alike" rule, just in the safe-looking direction. This does not license skipping `/comite` (routing still binds, see below) — it means the eventual correction, once routed, is *owed*, not merely optional.

- **Forbidden moves present?** None confirmed; two require adjudication (flagged, not blocking):
  - Post-hoc tuning / threshold loosening / ground-truth leakage / re-run after peeking: none present — no threshold changes, no embedding, no bench run (auditor §5, §6).
  - Reconstruction over-claim: none — the proposed change is scoped to `fixed_n` two-point TV, explicitly not extended to reconstruction, 3+1D, or asymptotic-horizon claims (wp4:336-342 "Also not claimed"; ficha and wp4 both self-limit to the diamond family).
  - **(b) Pause discipline not violated.** `docs/marcador_reentrada_2026-07-19.md:3` states `PROGRAMA_EN_PAUSA_LIMPIA`; its only pre-identified next step is the OP-2.2 falsifier run, "no autorizada" (`:24-36`) — unrelated to this proposal. The pause permits documentary/bibliographic work explicitly: `docs/hoja_de_ruta_24_jul_2026.md:16-19` calls such work "bibliografía y matemática de búsqueda, no una reapertura del programa," and `docs/hoja_de_ruta_25_jul_2026.md:118-120` (auditor_report_026 §5, citing hoja-24 §2.1 and hoja-25 §3.1) confirms this exact step was "Calculation only… No roadmap §3/§4 'No hacer' item breached." A label correction on an already-permitted calculation is the same class of act, not an escalation.
  - **(c) Routing partially honoured, one gap flagged.** `docs/hoja_de_ruta_24_jul_2026.md` §2 item 4 requires `/auditor` before touching `[PROVED]`/`[OPEN]` states and `/comite` before a programme-affecting decision; `docs/hoja_de_ruta_25_jul_2026.md:96-98` repeats it verbatim. `/auditor` ran and returned `AUDIT_PASS_WITH_WARNINGS`, `AUDIT_ERRORS=0` (`auditor_report_026_...md:206-207,233`), and its own recommendation (`:220-227`) explicitly names this a `/comite` matter. **But** `docs/auditor/auditor_report_026_...md` is itself `??` in `git status --short` — uncommitted and untracked. The routing *sequence* (auditor before committee) is honoured; the routing *record* is not yet durable. I flag this: the committee should not treat the audit as load-bearing history until it is committed — a `/comite` PASS should not be the thing that first causes the audit report to be committed as a fait accompli; commit it on its own footing.
  - **(d) Adjudicated: the "No hacer" item is not binding here, and is not actually violated by the literal proposal.** `docs/hoja_de_ruta_25_jul_2026.md` §4 first bullet (`:102-103`): "No presentar el candidato 7.1 como Forma L. Ni «casi». Los cuatro puntos de §2 son bloqueos, no detalles de redacción." Three things distinguish this from a frozen pre-registration and from a real violation: (1) **Self-declared status.** The document's own header (`:1-2`) says "**Plan REVISABLE, no congelado.** No es pre-registración, no fija umbrales, no autoriza ejecuciones... por sí mismo" — a roadmap "No hacer" is a *plan*, revisable by construction, unlike `docs/preregistration.md` / `_002.md`, which are `FROZEN` and state nothing here may be tuned on a result (`preregistration_002.md:3-5`). A frozen pre-registration may never be revised on a result because doing so would let the result choose its own bar — that hazard is structurally absent from a roadmap item whose entire premise is "these four points are blockers," when new mathematics shows two of those four points (point 3, variance, now `CERRADO 2026-07-25` per ficha `:282-286`; point 2, de-Poissonisation, now shown by the auditor's own re-derivation not to be needed on the Chebyshev/`fixed_n` route, `auditor_report_026:148-172`) were wrong on the roadmap author's own subsequent mathematics. (2) **The bullet's own scope.** It forbids "presenting 7.1 as Forma L. Not even 'almost'." The proposal on the table does *not* do that — it proposes a *scoped* label change for one channel (`fixed_n`) with two named caveats (enormous constant, non-effective `dv_0`), explicitly not a blanket "Forma L achieved" claim, and explicitly not touching the blanket ficha-wide `[OPEN]` framing for other pairs/families (wp4:336-342, ficha `[OPEN por par]` for OP-1.1/1.2 unchanged). (3) **The bullet is reasoning from now-superseded premises**, not a decision made in awareness of the closure. A roadmap "No hacer" is binding as *process discipline* (don't skip audit/committee, don't silently rewrite the record) — it is not binding as an unrevisable *substantive conclusion* once its own stated premises (§2's "four blocking points") have been shown, by the same author's later, audited work, to be partly mistaken. Verdict: the roadmap item's *procedural* command (route any such change through `/auditor` then `/comite`, don't just edit) is respected by this proposal; its *substantive* premise is exactly what `/comite` is being asked to reassess, which is the correct venue for revising a REVISABLE plan — not a violation of it.
  - **(e)** answered above — PASS.
  - **(f) Post-hoc `dv`-selection hazard: live, and must be pre-committed now, before any restated label is published.** `dv` currently appears at two values in the record: `0.02` (inside the proved asymptotic regime, `p` increasing in `tau` per Theorem C4) and `4` (outside it, where wp4:338-340 states plainly "the numerics show `p` *decreasing* in `tau`... The theorem is asymptotic"). Because both values are already computed and sitting side by side (wp4 §6 table, `:349-352`), there is a genuine hazard of *choosing* which `dv` to foreground in any restated Forma-L label after the fact — e.g., quietly favoring `dv=0.02` because it match the theorem's sign, or quietly favoring `dv=4` because its `Delta_p` is numerically larger. The logician's flag (echoed in the dossier) is correct and I endorse it as a pre-commitment: **any restatement must fix, in writing, before further computation, which `dv` (or which explicit rule for choosing one) is being asserted for the `fixed_n` closure, and must report both values' status (one inside the proved regime, one outside it) rather than foregrounding one silently.** This is not yet a violation — no restated document has been published — but it is a specific, concrete guard that the committee decision must impose as a condition, not leave implicit. Additionally the mathematician's finding that `dv* in (0.02, 4)` exists with `Delta_p(dv*) = 0` exactly (guaranteed blind cancellation) sharpens this: the eventual write-up must state that `S_n` is provably blind at that value, closing off any temptation to imply the separation holds "generically" in `dv`.

- **Reasons:**
  - `docs/preregistration_002.md:3-5` — frozen prereg definition; nothing this session touches it.
  - `git status --short` (verified this session) — thresholds.py absent; only two `REVISABLE` docs + one script modified, one untracked audit report.
  - `make verify-seal` → `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` = `docs/preregistration_002.md:8`, no drift.
  - `nachocausal/thresholds.py:57` (`DEV_SEEDS`), `dev/explore_seeds.py:24,29` (`EXPLORE_POOL`, reserved band) vs. literals `20260725`/`4242+n` in `wp4_comparable_pair_separation_checks.py:86,473` — disjoint, no burn.
  - `docs/marcador_reentrada_2026-07-19.md:3,24-36` — pause permits exactly this class of documentary/calculation step, not this specific one.
  - `docs/hoja_de_ruta_24_jul_2026.md` §2 item 4, `docs/hoja_de_ruta_25_jul_2026.md:96-98` — routing rule honoured in sequence (`/auditor` ran, names `/comite` next) but its own artifact (`docs/auditor/auditor_report_026_...md`) is uncommitted/untracked.
  - `docs/hoja_de_ruta_25_jul_2026.md:1-2` ("Plan REVISABLE, no congelado") vs. `docs/preregistration_002.md:3-5` ("FROZEN… nothing here may be tuned") — the categorical distinction that resolves (d).
  - `wp4_comparable_pair_separation.md:338-340`, `:349-352` — the `dv=0.02` vs `dv=4` sign-reversal, anchoring the post-hoc-selection hazard in (f).
  - `docs/preregistration.md:55-57`, `docs/preregistration_002.md:64-68` — founding "report alike" rule, symmetric by its own text, applied to the audit's under-claim finding in (g).
  - Reproducibility engineer's finding (this dossier, confirmed by me: `git show HEAD:...checks.py` has checks up to `[9]` + `[4b]` only; working tree adds `[10]`–`[13]`) — the §4b generator backing chain steps 3-5 is itself still uncommitted, an independent reason any restated label must be script-first, literals-second, and must not be finalized until that script is committed alongside it.

Procedural bottom line for the warden's role: this session PASSES on freeze/seal/seed/reporting-symmetry grounds; the substantive label change is not itself forbidden by any frozen object or by the pause; but it must not be committed as text until (i) the auditor report is itself committed, (ii) the `dv` pre-commitment in (f) is written down, and (iii) the §4b generator (checks `[10]`-`[13]`) is committed alongside any restated claim — script-first, literals-second, per the reproducibility engineer.

## 7. Literature verdict

| Citation | Claimed by | Status |
| --- | --- | --- |
| `Bombelli_1987_PhD.md:904` (ordering fraction, attrib. Myrheim) | MATHEMATICIAN | CONFIRMED |
| `Bombelli_1987_PhD.md:978` (CLT heuristic, `sqrt(N_rel)`) | MATHEMATICIAN | CONFIRMED |
| `Discrete geometry of a small causal diamond.md:117` (f₀(n) = ½ ordering fraction) + `:54` (Meyer's ⟨Cₖ⟩) | MATHEMATICIAN | CONFIRMED |
| `Towards black-hole horizons...md:173` ("infinite sprinkling required" for event horizon) | PHYSICIST | CONFIRMED |
| `Towards black-hole horizons...md:135` (constant det. ⇒ constant density, incl. (t*,r)) | PHYSICIST | CONFIRMED |
| `Towards black-hole horizons...md:186` (EGS at n=10³) | PHYSICIST | CONFIRMED |
| `Towards black-hole horizons...md:77,100,152` (links/local diagnostics vs global S_n) | MATHEMATICIAN | CONFIRMED (minor caveat, see notes) |
| Reitzner–Schulte 2013, `1104.1039v3.pdf`, Lemma 3.5, Thm 4.7/5.2 (Poisson-only, no de-Poissonisation) | (negative claim, WP4/ficha) | CONFIRMED |
| Janson 2011, `0902.0306v1.pdf`, Theorem 7.1 (equiv. incl. "same law all finite n"; twin-free hypothesis for (viii)/(ix)) | MATHEMATICIAN | CONFIRMED |
| van der Vaart 1998 Ch.12 / Hoeffding 1948 (Hoeffding decomposition) | MATHEMATICIAN | UNVERIFIED (correctly flagged) |
| Tsybakov 2009 §2.4, `ficha_se_busca_tv_order_only.md:432,550` | (ficha, `[UNVERIFIED]`) | CONFIRMED as correctly-labelled UNVERIFIED (local copy of Tsybakov's book *does* exist, but §2.4 content not cross-checked against the specific TV inequality claim) |
| Popoviciu's inequality (`Var(X)<=1/4`) | MATHEMATICIAN | CONFIRMED (no local source needed/exists, correctly unsourced) |
| Braun 2025, `ficha_se_busca_tv_order_only.md:545` + Remark 3.10 | PHYSICIST | CONFIRMED |
| `auditor_report_026...md:225-227` (mis-anchor "ficha §2.4 and roadmap §2.4") | LOGICIAN | CONFIRMED |

- **Bombelli 1987 (`derived-md/Bombelli_1987_PhD.md:904`)**: line 904 reads verbatim (OCR'd) "Myrheim [16] showed that, if we call *f(n)* := (N,.1) / (~) the 'ordering fraction', i.e., the expected number of related pairs of elements N,,I in the causal set over the total number of pairs." Attribution to Myrheim [16] is explicit and correct.
- **Bombelli 1987 (`:978`)**: line 978 reads "...*Nre1* will not fluctuate much, since it is a sum of a large number of variables, each associated with the existence of a relation between two elements of *P*, and the central limit theorem tells us that the fluctuations will be of the arder [order] of ,/N;;i [√N_rel]." This is exactly the heuristic independence-style argument the mathematician describes (treating N_rel as an approximately-independent sum and invoking CLT for its own square-root scaling) — Bombelli does not derive this via a proper (non-degenerate) Hoeffding-projection variance calculation, consistent with the mathematician's off-by-√n claim (which itself is the mathematician's own derivation, not sourced to Bombelli — correctly so).
- **Discrete geometry of a small causal diamond (`:54`, `:117`)**: line 54 attributes ⟨C_k⟩ to "Meyer's work [8]"; line 117 reads "Indeed, f0(n) is one-half of Myrheim's ordering fraction" followed immediately by the definition `f(C) ≡ R(N choose 2)^-1 ≈ 2R/N²` (eq. 12) — both citations verbatim-confirmed.
- **Towards black-hole horizons (`:173`)**: verbatim "Thus, to define an event horizon in a causal set, an infinite sprinkling is required." — exact match, footnote 3 immediately follows discussing the only alternative (Penrose-diagram sprinkling), reinforcing the boundary-of-claim point.
- **Towards black-hole horizons (`:135`)**: verbatim "The induced metric on the (1+1)-dimensional submanifold spanned by (t, r) has a constant determinant, implying a constant sprinkling density. This remains true, also if we use (t∗, r) coordinates, as we do below." — exact match.
- **Towards black-hole horizons (`:186`)**: Fig. 3 caption states "The data points for both plots were collected in 400 sprinklings of average size n = 10^3." — confirms EGS (Eichhorn–Gamito/Gomes–Stokes, i.e. this very paper's authors) used n~10³, supporting the physicist's "n~10⁹ is far out of reach" framing.
- **Towards black-hole horizons (`:77,100,152`)**: line 77 mentions "a local diagnostic that approximates a global concept"; line 100 defines the link (`≺*`, nearest-neighbor relation); line 152 discusses determining links via transitive reduction. These substantiate "local diagnostics" and "links" but none of the three specific lines mentions "ladders" verbatim (ladders are introduced later, in Sec. IV.A, not shown at these three anchors) — a minor imprecision in the citation bundle, not a misrepresentation, since the broader document does treat ladders as local (link-chain-based) diagnostics contrasted with global observables like S_n.
- **Reitzner–Schulte 2013 (`1104.1039v3.pdf`)**: Confirmed as Ann. Probab. 41(6), "Central Limit Theorems for U-statistics of Poisson Point Processes," Reitzner & Schulte. Lemma 3.5 (kernels/variance of Wiener–Itô chaos expansion), Theorem 4.7 (Wasserstein CLT bound) and Theorem 5.2 (rate `C_f λ^{-1/2}`) all exist exactly as cited, and the entire apparatus (Malliavin/Wiener–Itô, intensity `λ`) is for a Poisson process, never a fixed/binomial sample. Critically, the paper itself states explicitly (p.23, discussing the binomial-approximation remark): "it seems to be difficult to prove one result by the other, especially with keeping rates of convergence" — i.e., Reitzner–Schulte supply **no** de-Poissonisation bridge to the classical (fixed-`n`) U-statistic CLT. This is a strong, direct textual confirmation of the committee's central negative claim: Reitzner–Schulte is not needed (and does not help) for the `fixed_n` channel.
- **Janson 2011 (`0902.0306v1.pdf`)**: Theorem 7.1 verbatim confirms (iv) "The random posets P(n,W1) and P(n,W2) have the same distribution for every finite n" as one of the equivalent conditions to Π1 = Π2, and confirms that (viii) requires "If further W2 is almost twinfree" and (ix) requires "If both W1 and W2 are almost twinfree" — exactly the extra hypothesis structure the mathematician describes. Fully confirmed.
- **van der Vaart 1998 Ch.12 / Hoeffding 1948**: The file `biblioteca/Asymptotic Statistics.pdf` is confirmed to be **Reinhard Höpfner's** "Asymptotic Statistics" (De Gruyter, 2014), *not* van der Vaart's 1998 book of the same title — the mathematician's correction is CONFIRMED. Additionally, `biblioteca/[Aad_van_der_Vaart,_Jon_Wellner].pdf` is a different van der Vaart book, "Weak Convergence and Empirical Processes" (Springer, 1996, with Wellner) — a scanned, non-OCR'd, image-only PDF (no extractable text; verified by direct page-image reading) that is *also* not van der Vaart's "Asymptotic Statistics" (1998). Grep of Höpfner's book for "Hoeffding"/"U-statistic" returned nothing. So: no local source covers the classical Hoeffding decomposition / U-statistics under either candidate PDF — the `[UNVERIFIED, standard]` tag is fully justified, and the additional claim "biblioteca's Asymptotic Statistics.pdf is Höpfner, not van der Vaart" is CONFIRMED.
- **Tsybakov 2009 §2.4**: A local copy `biblioteca/Tsybakov_Nonparametric_Estimation.pdf` (Tsybakov, "Introduction to Nonparametric Estimation," Springer) exists and does contain a genuine "§2.4 Distances between probability measures" (confirmed via TOC and in-text headers, incl. "2.4.1 Inequalities for distances," "2.4.2 Bounds based on distances"). The ficha's own tag is `[UNVERIFIED]` "sin copia local verificada" (no local copy verified) at the time of writing — this tag is technically now stale/overcautious since the PDF *does* exist locally, but the ficha never claims the file is absent, only that the specific citation wasn't cross-verified; no misrepresentation.
- **Popoviciu's inequality**: No file matching "Popoviciu" found anywhere in `biblioteca/` or `research_program/`; consistent with the mathematician's note that this is elementary and needs no citation.
- **Braun 2025 (`2507.01907v1.pdf`)**: ficha line 545 verbatim-matches (checked exact text). Remark 3.10 (p.15, verbatim) confirms: "Bombelli's conjecture ... suggests that the conclusion from Theorem 1.4 ... is true with permutations," and explicitly frames it as unresolved ("There are two challenges that need to be understood before applying our argument to Bombelli's conjecture"). The paper itself (line 69, Sec. 1.1) states the HKMM/Braun rigidity applies to dimension "d ∈ N no less than 3." The "d=2 excluida ... FWP Lemma 1" clause in the same ficha cell is a repo-internal citation (not to Braun) — `research_program/models/first_witness_pair_candidates.md:33` Lemma 1 ("copula reduction; null-box patches") is a 1+1D (d=2) result showing the poset law collapses to depend only on the copula, i.e., exactly the failure-of-rigidity-in-2D phenomenon the ficha cell alludes to. Confirmed as correctly anchored (though the two halves of that cell cite two different sources — Braun for the labelled/Bombelli-conjecture part, FWP internal Lemma 1 for the d=2-exclusion part — which is accurate but could read as a single citation if not read carefully).
- **Auditor report mis-anchor (`docs/auditor/auditor_report_026_wp4-annex-c-variance-addendum-precommit.md:225`)**: verbatim text found: "...ficha §2.4 and roadmap §2.4 both route status changes of this weight through the committee..." Checked `research_program/bibliography/ficha_se_busca_tv_order_only.md` heading structure: sections run `## 2. ...`, `## 2.1 ...`, `## 2.2 ...`, then jump directly to `## 3. ...` — there is **no `## 2.4`** heading anywhere in the ficha (the only "2.4" occurrences in that file are references *to* Tsybakov's book §2.4, at lines 432 and 550, not the ficha's own numbering). Checked `docs/hoja_de_ruta_25_jul_2026.md` heading structure: `## 0`, `## 1`, `## 2`, `## 3`, `## 4`, `## 5` — likewise no `§2.4` subsection. The LOGICIAN's finding is CONFIRMED: both anchors in the auditor report are non-existent section numbers.

## 8. Synthesis

### 8.0 Lo que el comité NO hace

Este acta **no edita** la ficha, el Anexo C, la hoja de ruta ni ningún otro fichero; no crea código
ni ejecuta nada; no commitea. Es el único fichero producido en esta sesión, conforme a la
restricción del PI. Los cambios de §9 requieren autorización explícita en una sesión posterior.

### 8.1 Consenso unánime (7/7 roles)

- **Q1 — La cadena es CORRECTA en `fixed_n`.** Verificada por tres rutas independientes: el autor
  del Anexo C, el auditor (informe 026 §6, cómputo ad-hoc propio), y el matemático de este comité
  **a mano, término a término** (§4, ítems (a)–(d)), reproduciendo `κ(3,0.5) = 0.0299975` y los
  umbrales `n = 1.361e9` / `1.165e8` a tres cifras. **Reparación de redacción obligatoria:** lo que
  la cadena necesita es `Var(S_n) = O(n^3)` (sólo `zeta <= 1/4`), no `Theta(n^3)`; y el cociente
  señal/desviación `-> infinito` **no es por sí mismo** un enunciado sobre TV — el paso a TV es
  Chebyshev + data processing. Redactarlo de otro modo camina justo por encima del guardarraíl de
  ficha §9.2, segundo guión.
- **Q2 — NO se necesita nada de eso.** Ni CLT de Reitzner–Schulte, ni des-Poissonización, ni CLT
  alguna, ni ajuste empírico de exponente. Por FWP Lema 0 los `n` puntos son i.i.d., luego `S_n` es
  un U-estadístico de orden 2 **binomial**, no un funcional de Poisson: los dos momentos son
  identidades exactas. El único insumo externo es la desigualdad de Chebyshev y la definición
  variacional de TV. **Confirmación textual decisiva** (§7): Reitzner–Schulte *dicen ellos mismos*
  (p.23) que «it seems to be difficult to prove one result by the other, especially with keeping
  rates of convergence» — no aportan puente de des-Poissonización. La des-Poissonización nunca
  estuvo en la ruta `fixed_n`.
- **Q3 — SÍ, en sentido estricto y acotado.** El `[OPEN]` en bloque de
  `wp4_comparable_pair_separation.md:381-382` y la presentación de la des-Poissonización como
  bloqueo (`:317-320`, ficha §2.2 punto 2) son **incorrectos para el canal `fixed_n`** de la familia
  diamante de WP4 §4 con `dv < dv_0`. Siguen siendo correctos en todo lo demás: canal Poisson sin
  condicionar, otras familias (`[OPEN por par]`), candidatos 7.2–7.4, y Formas U y D.
- **Q6 — SÍ, el exponente `1/2` está demostrado**, y por matemática de 1948 (descomposición de
  Hoeffding) más Chebyshev. No hay probabilidad nueva en la cadena `fixed_n`. No se ajustó ningún
  exponente: los Monte-Carlo a `n = 5, 10, 20` sólo verifican la fórmula exacta de varianza.
- **Delimitación física, unánime.** Discriminación binaria entre dos completions fijas mediante una
  función del poset. **NO** localización del horizonte, **NO** reconstrucción, **NO** estimación de
  `tau`, **NO** 3+1D, **NO** horizonte asintótico. `NO_RECONSTRUCTION_CLAIM`.
- **Sin fuga de ground truth, sin violación del sello, sin semilla virgen quemada.** Cálculo en el
  continuo; nada importa de `nachocausal/`; sello sin drift.

### 8.2 Respuesta a la pregunta estructural del PI

El PI pidió separar **estructura** de **eficiencia**. El comité lo hace así, y añade un matiz que el
PI no anticipó:

- **Cuestión estructural — CERRADA en sentido positivo, pero SÓLO dentro del régimen de C6.** Para
  `dv < dv_0` no hay cancelación exacta: `Delta_p = kappa*tau*dv*delta + O(dv^2)` con `kappa > 0`
  probado, y `Var(S_n)` no degenera (`zeta_1 > 0`, Prop C8).
- **Pero la cancelación exacta EXISTE fuera de ese régimen, y está garantizada, no es hipotética.**
  Hallazgo nuevo de este comité (matemático §4(g), confirmado y extendido por el falsador §5.4): como
  `Delta_p(0.02) = +1.142952e-04` y `Delta_p(4) = -3.875520e-04` con `p` continua en `dv`, **por el
  teorema del valor intermedio existe `dv* ∈ (0.02, 4)` con `Delta_p(dv*) = 0` exactamente**. En ese
  lapso `S_n` es **exactamente ciego a nivel de medias** y toda la cadena de dos momentos es vacua
  para **cualquier** `n`. Esto no rompe el teorema (Teo C4 excluye ceros por debajo de `dv_0`): lo
  **acota**, y prohíbe toda extrapolación en `dv`.
- **Consecuencia documental:** `ficha:483-485` — «La rama "si `p(theta) = p(theta')` el candidato es
  ciego para ese par" queda **descartada** para la familia diamante: `kappa > 0` estrictamente, luego
  el estadístico **nunca es ciego** ahí» — es **FALSA tal como está escrita**. Debe acotarse a
  `dv < dv_0`. **Este comité, por tanto, sube una etiqueta y BAJA otra.** No es una sesión de
  promoción.
- **Cuestión de eficiencia — ABIERTA, y ahora con un blanco escalar único.** Ver §8.4.

### 8.3 Q4 — Etiquetas: el comité RECHAZA la formulación propuesta por el PI

El PI propuso evaluar `[PROVED — FIXED_N ASYMPTOTIC SEPARATION; NON-EFFECTIVE]` +
`[OPEN — FINITE_N EFFICIENCY / CONSTANT-LEVEL INFORMATION EFFICIENCY]`. El comité **no las adopta**:
el lógico las declara sobre-afirmantes en tres puntos y ambiguas en dos (§4); el falsador dictamina
que **la etiqueta escueta propuesta es PEOR que el statu quo** (§5, «Attack on the status quo»). El
comité adopta la reformulación del lógico, con la estructura de dos campos del físico. **Etiquetas
recomendadas, literales:**

**Etiqueta 1 — sustituye el `[OPEN]` en bloque, SÓLO en el canal `fixed_n`:**

```text
FORMA_L_FUERTE_fixed_n
  = PROVED_LEADING_ORDER / NON_EFFECTIVE_x2 / TWO_POINT_ONLY / DIAMOND_FAMILY_ONLY

[PROVED (orden dominante en dv; el paso (i) de Anexo C §4 — analiticidad de p en dv en 0^+ —
 queda argumentado, NO escrito) — CONSISTENCIA DE TEST A DOS PUNTOS, canal fixed_n,
 familia diamante WP4 §4 ÚNICAMENTE]

Enunciado exacto (orden de cuantificadores DÉBIL, el único que se afirma):
  para todo (r_p, r_q) admisible y todo par FIJO tau != tau' en (r_q, r_p),
  EXISTE dv_0 > 0 NO EFECTIVO tal que para todo 0 < dv < dv_0:
  TV(Q^n_tau, Q^n_tau') -> 1 cuando n -> infinito.

NO EFECTIVO DOS VECES: dv_0, y n_0(dv, tau, tau').
SIN UNIFORMIDAD en (tau, tau'): esa forma exigiría además el paso (ii) de §4, que NO se afirma.
Todo valor concreto de Delta_p y todo n finito son [NUMERICAL]; uno de ellos (dv = 4) cae
  demostrablemente FUERA del régimen probado (allí p DECRECE en tau).
NO es estimador, NO es localización, NO es reconstrucción, NO es 3+1D.
DEFEATER VIVO (no premisa): zeta_1 * Ibar >= kappa^2 dv^2 / 54, enunciado y NO ejecutado.
```

**Etiqueta 2 — cuestión nueva que sustituye a la propuesta por el PI:**

```text
EFICIENCIA_CONSTANTE_fixed_n = OPEN_CONSTANT_LEVEL_ONLY

[OPEN — SÓLO A NIVEL DE CONSTANTES]
El EXPONENTE está cerrado por ambos lados: delta ~ n^{-1/2} lo alcanza S_n (momentos exactos
+ Prop C8) y NINGÚN procedimiento order-only lo mejora sobre esta familia (WP4 §5, [PROVED],
condicional a Ibar < infinito). Lo abierto es la CONSTANTE:
 (i) el prefactor verdadero de TV(Q^n) — la ruta Chebyshev es demostrablemente conservadora
     (factor 8, más el zeta <= 1/4 trivial que ya cuesta un factor ~9 frente a zeta_1 ~ 1/36);
 (ii) la pérdida de información constante de la compresión Iso_n -> S_n;
 (iii) el chequeo de UNA SOLA DIRECCIÓN zeta_1*Ibar >= kappa^2 dv^2/54, ENUNCIADO Y NO EJECUTADO
     (Ibar desconocido para estas esquinas), cuya violación refutaría una de las dos cotas [PROVED].
NI observable nuevo, NI CANDIDATE_7, NI estimador.
```

**Etiqueta 3 — corrección a la baja descubierta por este comité:**

```text
S_N_BLINDNESS_AT_dv_star = PROVED_EXISTS (dv* no localizado)

ficha §7.1 punto 5 — «el estadístico nunca es ciego ahí» — [REFUTED as written].
Por el teorema del valor intermedio existe dv* in (0.02, 4) con Delta_p(dv*) = 0 exactamente:
S_n es EXACTAMENTE ciego a nivel de medias en ese lapso, para todo n.
La frase debe acotarse a dv < dv_0.
```

**Etiquetas explícitamente rechazadas y por qué:**

- `[PROVED — FIXED_N ASYMPTOTIC SEPARATION; NON-EFFECTIVE]` (propuesta del PI) — «SEPARATION» no
  distingue separación de medias de separación en TV (la trampa de §9.2); `[PROVED]` escueto
  contradice el precedente propio del repo (`...separation.md:367-369` usa
  `[PROVED (leading order)]` con los huecos nombrados); «NON-EFFECTIVE» sin tipar no lleva las **dos**
  no-efectividades; y no dice «sólo dos puntos, sólo esta familia».
- `PROVED_BUT_VACUOUS_IN_PRACTICE` (sugerida por `auditor_report_026:227`) — **el comité la rechaza
  por sobre-afirmar en la dirección pesimista.** «Vacuo en la práctica» es una afirmación sobre
  `TV(Q^n)` verdadero, que es **desconocido**. Lo enorme es la **cota de Chebyshev**, no
  necesariamente la TV: el físico estima `[UNVERIFIED — aritmética a mano]` que una CLT estándar de
  U-estadísticos bajaría a `n ~ 6e6` (factor ~200) y que el mínimo teórico-informativo podría estar
  en `n ~ 2e5` para una forma de referencia distinta. Llamarlo vacuo sería exactamente el mismo tipo
  de error que llamarlo viable.
- **«Viabilidad matemática demostrada»** — prohibida, como pidió el PI, y el comité **confirma que la
  prohibición está justificada**: la convergencia asintótica en un régimen no efectivo, con un
  defeater sin ejecutar y una ceguera exacta garantizada fuera del régimen, no es viabilidad.

### 8.4 Q7 — Graduación de la afirmación sometida, término a término

| Fragmento | Estado | Anclaje |
|---|---|---|
| «El exponente raíz-n no parece ser el cuello de botella» | **DEMOSTRADO** | La cota de WP4 §5 es **no asintótica** (descansa en Cauchy–Schwarz integrado, `wp4_fisher_localization_floor.md:159`, no en el desarrollo QMD) y acota `TV(Q^n)`, que por definición es el supremo sobre **toda** función del poset: ningún procedimiento order-only separa a `delta = o(n^{-1/2})` |
| «Bajo la cota Fisher de WP4, es la tasa regular esperable» | **DEMOSTRADO** | Ambos umbrales viven en `t := delta*sqrt(n) = O(1)` (`...separation.md:271-282`) |
| «y posiblemente óptima» | **SUBESTIMA en tasa, INFERENCIA en constante** | La optimalidad **de exponente** está probada por ambos lados, no es «posible». La optimalidad **de constante** no lo está y hoy es incuantificable (`Ibar` sin calcular). **El físico exige tachar «possibly optimal» sin cualificar**: el suelo es una cota **a dos puntos**, no minimax (`wp4_fisher_localization_floor.md:487-489`), y es una cota *superior* de TV que «can therefore be loose for posets» por admisión propia (`:293-297`). Redacción defendible: «rate-optimal among regular procedures on this named family» |
| «El problema visible está en el prefactor» | **INFERENCIA bien fundada** | `n* ≈ 8/(eps*kappa^2*dv^2*delta^2)`: el prefactor es el término que ata. Un factor ~9 es **gratis** usando `zeta_1 ≈ 1/36` en vez de `zeta_1 <= 1/4`; más ganancia con Cantelli o una CLT. Pero el prefactor **verdadero** de `TV(Q^n)` sigue desconocido |
| «o en la pérdida de información al comprimir el poset completo al único estadístico `S_n`» | **ABIERTA — y NO es una alternativa genuina** | Como ambos, `S_n` y el canal completo, escalan `n^{-1/2}`, cualquier pérdida por compresión está **confinada a la constante**: la disyunción colapsa en **una sola** pregunta de constante, que es exactamente el chequeo §6.4 sin ejecutar. Cuantitativamente la compresión es severa — `p = (1+tau_K)/2` reduce toda la cópula a **un escalar** (tau de Kendall), mientras que la ley del poset completo determina la cópula esencialmente por entero (Janson Teo 7.1, `CONFIRMED` en §7) |

### 8.5 Desacuerdos abiertos (no ocultados)

1. **Redacción de la etiqueta — resuelto por el presidente a favor del lógico.** El PI propone una
   forma corta; el lógico una larga y tipada; el físico dos campos; el auditor sugiere
   `PROVED_BUT_VACUOUS_IN_PRACTICE`; el falsador ordena las opciones como *etiqueta ajustada del
   lógico* > *statu quo `[OPEN]`* > *etiqueta escueta del PI*. **El presidente adopta la del lógico
   con la estructura de dos campos del físico** (§8.3), y rechaza explícitamente
   `PROVED_BUT_VACUOUS_IN_PRACTICE` por sobre-afirmar en dirección pesimista.
2. **Significado físico — disidencia del físico, registrada y adoptada como límite.** El físico es el
   único que sostiene que la señal es una **firma de curvatura/forma, no del locus del horizonte**:
   `kappa > 0` vale para **todo** `0 < r_q < r_p` **sin ninguna condición sobre `tau``, luego nada en
   la derivación se dispara *porque* el diamante cruce el horizonte; y en 1+1D Schwarzschild `tau` es
   a la vez radio del horizonte y **única** amplitud de curvatura (`R_tau = -2tau/r^3`), de modo que
   «discriminar el horizonte» y «discriminar la curvatura media del parche» son literalmente el mismo
   acto. Ningún otro rol lo contradice. **El comité lo adopta:** ninguna redacción futura puede
   llamar a esto «información de horizonte» sin declarar que es una convención de nombre.
3. **Utilidad de la des-Poissonización — divergencia menor.** El matemático la conserva «donde sigue
   siendo portante» (importar la CLT de Reitzner–Schulte, i.e. canal Poisson y mejoras
   *distribucionales* de Chebyshev). El físico observa que ficha §1.2/§9.2 ya prohíben el canal
   Poisson por contaminado, «so it arguably drops entirely». **El presidente adopta la posición del
   matemático** (retenerla, degradada de bloqueo a herramienta opcional para constantes), porque
   eliminarla del todo cerraría por decreto una vía que nadie ha refutado.
4. **Suficiencia de la cadena vs. suficiencia del paquete — el eje real.** Matemático, lógico, físico
   y falsador coinciden en que **la matemática se sostiene**. El ingeniero de reproducibilidad y el
   falsador coinciden en que **los literales no**: el paso 7 de la cadena no tiene generador alguno,
   los `n ~ 10^8`–`10^10` existen sólo en prosa del auditor, y el generador de §4b (checks
   `[10]`–`[13]`) **sigue sin commitear**. Esto no bloquea el veredicto; **condiciona la ejecución**
   (§9, condición C2).

### 8.6 Prohibición explícita de lectura (vinculante para cualquier cita futura)

**Este resultado NO es, y no puede citarse como:**

- localización del horizonte — no se produce ningún locus `r = 2M`, ningún elemento o subconjunto del
  causet queda etiquetado «horizonte», no se emite ninguna coordenada `r`;
- reconstrucción geométrica o métrica — el Teorema A prueba que toda la órbita de dilatación es
  **una sola** ley de poset a todo `n`, luego `r_s` absoluto es demostrablemente irrecuperable;
- estimación de `tau` ni conjunto de confianza para `tau` — es un test entre **dos hipótesis fijadas
  de antemano**; convertir tests puntuales en estimación exigiría error uniforme sobre una red, que
  no existe aquí y que además está topado por WP4 §5;
- un enunciado sobre 3+1D, sobre el horizonte asintótico (EGS: «to define an event horizon in a
  causal set, an infinite sprinkling is required», `CONFIRMED` en §7), ni sobre la línea C1–C6
  cerrada, prereg-002, o cualquier artefacto sellado;
- un resultado **ejecutable**: `n ~ 10^9` implica `ell ~ 10^{-4}`–`10^{-6}` del radio del horizonte y
  supera en `~10^5` el mayor nivel de la escalera congelada `{1500, 3000, 6000, 12000}`
  (`docs/preregistration_001_addendum.md:44`); `S_n` recorrería `C(n,2) ~ 5e17` pares.

**Contenido exacto y completo del enunciado:** para cada par `(D_tau, D_tau')` **fijado de antemano**
en la familia de WP4 §4 y cada `dv` suficientemente pequeño, existe una sucesión de tests order-only
—umbral sobre `S_n` en el punto medio— cuyo error de tipo I + tipo II tiende a 0 cuando `n -> infinito`
en `fixed_n`. Equivalentemente: las dos leyes order-only son asintóticamente mutuamente singulares.
**Eso es todo.**

## 9. Next-step spec

### 9.1 Paso ejecutado en esta sesión (irreversible sólo como escritura de acta)

Único fichero producido: este acta. Nada más se ha tocado. `git status --short` al cierre se reporta
al PI.

### 9.2 Condiciones vinculantes (pre-comprometidas AHORA, antes de ver ningún número nuevo)

Ninguna edición documental de §9.3 puede ejecutarse hasta que las cuatro se cumplan.

- **C1 — El informe de auditoría 026 se commitea por su propio pie, PRIMERO y por separado.** Hoy es
  `??` (untracked). El routing exige `/auditor` antes de tocar estados; su registro debe ser durable
  **antes** de que el acta lo use como base, y no como efecto colateral de la edición que autoriza.
  (Warden §6(c).)
- **C2 — Script primero, literales después. Sin excepción.** El generador de §4b (checks
  `[10]`–`[13]`) sigue **sin commitear** (`git show HEAD:...checks.py` sólo tiene hasta `[9]` y
  `[4b]`). Además, el **paso 7 de la cadena no tiene generador alguno**, y los `n ~ 10^8`–`10^10`
  existen únicamente en la prosa de `auditor_report_026:164-166`. **Regla:** ninguna cifra `n*` ni
  ninguna cota TV puede publicarse en la ficha o el Anexo C hasta que un script determinista
  commiteado la emita verbatim. Precedente vinculante: `auditor_report_024` = `AUDIT_FAIL` por
  exactamente este defecto. Si el PI no autoriza el generador, la reetiquetación debe hacerse
  **publicando cero literales numéricos nuevos** — es posible: la Etiqueta 1 no contiene ninguno.
- **C3 — `dv` se congela por escrito ANTES de cualquier cómputo posterior.** El registro contiene dos
  valores (`0.02` dentro del régimen probado, `4` demostrablemente fuera). Debe fijarse en el texto
  qué `dv` (o qué regla explícita) se afirma, y **reportar el estado de ambos**, no destacar uno en
  silencio. Elegir después el que dé el mejor `n` sería `NO_POST_HOC_TUNING` puro.
- **C4 — Las tres etiquetas de §8.3 se adoptan como bloque, o ninguna.** En particular la Etiqueta 3
  (corrección a la baja de `ficha:483-485`) **no** es opcional: subir una etiqueta sin bajar la otra
  sería precisamente el sesgo que este comité existe para impedir.

### 9.3 Cambios documentales autorizados para un paso posterior (REVERSIBLES, requieren orden del PI)

Ninguno se ejecuta hoy. Todos son ediciones de texto en documentos autodeclarados no congelados.

1. `research_program/work_packages/wp4_comparable_pair_separation.md`
   - §5 ítem 2: reescribir para distinguir «bloquea la ruta CLT de Reitzner–Schulte» de «bloquea la
     Forma L». La des-Poissonización **nunca estuvo** en la ruta `fixed_n`.
   - §6, línea de estado de Forma L (`:381-382`): sustituir el `[OPEN]` en bloque por **Etiqueta 1**
     + **Etiqueta 2**, conservando `[OPEN]` para canal Poisson, otras familias, y Formas U/D.
   - §4b / §5 ítem 4: mantener el defeater §6.4 como **defeater**, nunca como premisa satisfecha.
   - Actualizar el docstring obsoleto del script (`..._checks.py:18-30`, lista sólo hasta `[9]`).
   - Corregir los tres ratios redondeados de `:258-259` (finding 2 del informe 026).
2. `research_program/bibliography/ficha_se_busca_tv_order_only.md`
   - §2.2 punto 2 y §7.1 punto 3: retirar la des-Poissonización como bloqueo de `fixed_n`.
   - §7.1 punto 5: aplicar **Etiqueta 3** (acotar «nunca es ciego» a `dv < dv_0`).
   - §2, viñeta «el hueco central» (`:147-151`): **NARROW, no borrar** — «no existe ninguna técnica
     para acotar `TV(Q)` por debajo» es ahora falso; la técnica es la que la propia §5 (`:399-405`)
     anticipaba: estadístico order-only + data processing + Chebyshev.
   - §6.3, tercera viñeta (`:439-440`): acotar la exigencia de anti-concentración **sólo** a la ruta
     de comparación gaussiana. Tal como está, leída literalmente, **bloquea la propia cadena que se
     adjudica** — la ficha sería auto-contradictoria.
   - §2.1(B)/§7.1: **arreglar** el choque de convención del factor 2 (declarado en `:236-241`, sin
     arreglar). Mueve toda constante de Chebyshev por 4 si se mezclan. **No publicar una etiqueta
     encima de un choque de convención sin resolver.**
   - §7.1 punto 3 (`:463-471`): separar el canal `fixed_n` (`E S_n = C(n,2)p`) del Poisson
     (`Var = Theta(lambda^3)`); hoy están mezclados en un mismo ítem.
   - Fila de Reitzner–Schulte en §8: registrar la cita textual de p.23 («difficult to prove one
     result by the other… keeping rates of convergence») como confirmación de que no hay puente.
3. `docs/hoja_de_ruta_25_jul_2026.md`
   - §3 ítem 2: de «des-Poissonización, bloqueo, prioridad 2» a «necesaria **sólo** para importar la
     CLT de Reitzner–Schulte, i.e. sólo en el canal Poisson y sólo para constantes más finas».
   - §3: promover a **prioridad 1** el único número que cierra las dos cuestiones abiertas a la vez —
     `Ibar` para **estas** esquinas, y/o su escala en `dv`. Es el mismo objeto que (a) ejecuta el
     defeater §6.4 y (b) cuantifica el prefactor y la pérdida por compresión.
   - §4 primera viñeta: reescribir como «no presentar 7.1 como Forma L **sin acotar canal, familia,
     par y régimen `dv`**», que es lo que su premisa quería proteger.
   - Registrar que `docs/hoja_de_ruta_24_jul_2026.md:52-57` ya había previsto este desenlace («la
     cadena de Forma L para 7.1 queda cerrada salvo redacción»).
4. `docs/auditor/auditor_report_026_...md`: corregir la mis-ancla «ficha §2.4 / roadmap §2.4»
   (§7 `CONFIRMED`: la ficha no tiene §2.4). La regla viva es
   `docs/hoja_de_ruta_24_jul_2026.md:66-70` (§2, **ítem** 4).

### 9.4 Paso analítico recomendado (NO autorizado aquí; un cálculo, no una ejecución)

**Prioridad 1 — `Ibar` para las esquinas del diamante de registro.** Un único escalar que cierra
tres cosas a la vez: ejecuta el defeater `zeta_1*Ibar >= kappa^2 dv^2/54`, cuantifica el prefactor, y
da la primera medida real de la pérdida por compresión `Iso_n -> S_n`. Cuadratura determinista de un
objeto ya definido en WP4.

**Prioridad 2 — escribir la cota de resto `O(dv^2)`, uniforme en `tau`.** Es el **único** ingrediente
que faltaba: cierra el paso (i) argumentado-no-escrito **y** hace efectivos `dv_0` **y**
`n_0(dv, delta)` **simultáneamente**. Convertiría la Etiqueta 1 en `[PROVED]` sin cualificar y con
constantes.

**Explícitamente NO autorizado y NO recomendado:** abrir un observable nuevo, abrir `CANDIDATE_7`,
implementar `S_n` como estimador, ejecutar el banco sellado, consumir semillas, o tocar cualquier
umbral. La recomendación viva del marcador de reentrada (**consolidar, no observable nuevo**) sigue
intacta y nada de esta acta la toca.

### 9.5 Test mínimo de falsación (del falsador; describir, NO ejecutar hoy)

Un único check determinista `[14]` añadido al script existente, en sesión futura y previa
autorización: (a) recomputar `Delta_p(dv)` por la cuadratura existente sobre una malla fija en
`[0.02, 4]` y **acotar el cambio de signo**, emitiendo un intervalo para `dv*` — esto **ejecuta** el
punto de ceguera del TVI y expone cualquier `dv` publicado que caiga cerca; (b) imprimir
`1 - 4(2n-3)/(n(n-1)Delta_p^2)` en los `n` exactos que se vayan a citar, dejando todo literal TV
emitido por script. **Si algún literal citado no reproduce, la subida de etiqueta queda falsada como
paquete; si `dv*` acota cerca de un `dv` publicado, el acotamiento queda falsado.** Sin semillas, sin
umbrales, sin artefactos de validación.

## 10. Verdict
COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_CAVEATS

## 11. User sign-off
_(left blank for the user — decision, date, and any overriding notes)_
