# Comité Decision 047 — Publicación del cierre Fase 2, migración histórica y preapertura B2

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action, never tunes a frozen threshold post-hoc, and never makes a
> reconstruction claim. Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`,
> `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

¿Debe aceptarse como internamente coherente y publicarse ahora en GitHub el paquete documental
completo —adjudicación de respuestas Tier A/B y correcciones acotadas del manuscript, migración al
esquema vigente de las decisiones históricas 012–014 y 039–043, y contrato de preapertura de Fase 3
B2— manteniendo explícitamente sin abrir la adopción del target B2, la construcción de pares
testigo, el código, las simulaciones y las semillas?

## 2. Verified state

Hechos comprobados en esta sesión:

- Instrucción explícita del PI el 2026-07-28: `COMITEA Y PUSHEA`. La publicación queda condicionada
  a un veredicto no bloqueante y a todos los gates finales.
- Estado de partida:
  `HEAD=origin/main=29f84357ae7c5e6b8eb4d2afc1ce75949c3b190f`, rama `main`, divergencia
  `origin/main...HEAD = 0 0`.
- Superficie antes de esta acta: 23 rutas trackeadas modificadas, todas documentales/README, más
  `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md` como archivo nuevo.
  `git diff --name-status` no mostró cambios en código, tests, scripts, dependencias, datos,
  resultados ni umbrales.
- `make verify-seal`:
  `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`,
  coincidente con `docs/preregistration_002.md:7-12`.
- `make test`: `270 passed in 370.35s (0:06:10)`, exit 0.
- `make verify-comite`: 46/46 briefs previos con `BRIEF_CHECK=PASS`.
- `make verify-audit`: 29/29 informes con `AUDIT_CHECK=PASS`.
- `make audit`: 0 errores y 23 warnings de archivos de datos ya committeados; este paquete no
  modifica ninguna de esas rutas.
- `git diff --check`: PASS.
- `git check-ignore -v` confirmó que los dos borradores y las dos respuestas PDF bajo `email/`
  coinciden con `.gitignore:30`; no forman parte de la superficie pública.
- El conector autenticado de GitHub confirmó `nacho09021973/nachocausal`, rama por defecto `main`,
  visibilidad pública y permisos admin/push. `gh auth status` informó token CLI inválido; por tanto
  `gh` no se usará como evidencia. La prueba operativa será `git push --dry-run`, push HTTPS,
  igualdad por `git ls-remote`, y PR borrador mediante el conector.

## 3. Dossier

Fuentes principales:

- `CLAUDE.md:7-16`
- `docs/preregistration.md:25-78`
- `docs/preregistration_002.md:1-74`
- `docs/preregistration_002_result.md:1-80`
- `research_program/bibliography/phase2_novelty_and_item5.md:3-25,199-279,317-331`
- `docs/manuscript_limits_draft.md:3-23,189-200,363-603,964-1013`
- `docs/comite/comite_decision_012_c1-admissible-completion-class.md:396-469`
- `docs/comite/comite_decision_013_c1-bce-review.md:606-678`
- `docs/comite/comite_decision_014_q-reference-rule-disposition.md:1080-1150`
- `docs/comite/comite_decision_039_c4-neighbor-graph-adjudication.md:432-502`
- `docs/comite/comite_decision_040_c5-search-space-adjudication.md:341-409`
- `docs/comite/comite_decision_041_c5-1-matrix-to-block-map-adjudication.md:348-416`
- `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md:293-362`
- `docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md:589-660`
- `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:1-303`
- `tarea_grok_2.md:3-6,357-384`
- Surya, *The causal set approach to quantum gravity*, §§2, 4.1, 4.3.
- Roy et al., *Discrete geometry of a small causal diamond*, §2.
- Eichhorn–Gamito–Stokes, *Towards black-hole horizons and geodesic focusing in causal sets*,
  §§III, IV, VI.
- Müller, *On the Hauptvermutung of Causal Set Theory*, Theorems 2–3.

## 4. Expert briefs

### Reproducibility engineer brief
- Proposed artefact(s): One documentation-only commit on `agent/phase2-b2-documentation`, comprising exactly the 23 tracked paths in the current `git diff --name-only` output, new `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md`, and this new `docs/comite/comite_decision_047_*.md`; then one draft PR to `main`. Stage an explicit 25-path manifest—never `git add -A`. Exclude `email/`: `.gitignore:26-30` declares it local-only, and current `git check-ignore -v` maps both drafts and both response PDFs to `.gitignore:30`.
- Environment & seal: This publication authorizes no scientific execution, so it must not invoke `make dry-run`, validation, B2 witness construction, simulations, or seeds (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:289-302`). Preserve the sealed numpy contract `numpy==1.26.4` (`docs/preregistration_002.md:20-33`; `docs/estimator_v2_seal.md:61-66`) and re-anchor `make verify-seal` at `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (chair DOSSIER; `docs/preregistration_002.md:7-12`). Require a package-diff-clean check over `nachocausal/`, `tests/`, `scripts/`, `Makefile`, and dependency files; the current `git diff --name-only` output contains documentation/README paths only. The running `make test` remains pending and must not be reported as PASS without its completed output `[UNVERIFIED]`.
- Provenance capture: Record source `HEAD=29f84357ae7c5e6b8eb4d2afc1ce75949c3b190f`, pre-publication `origin/main` match and `0 0` divergence (current `git rev-parse`/`git rev-list` outputs), branch name, exact staged name-status, resulting commit SHA, seal SHA, completed gate outputs, publication timestamp, draft-PR URL, and remote branch SHA. `pip freeze`, `uname`, and seed-band capture are not new publication artefacts because no executable B2 run is authorized; the existing validation seed provenance remains frozen in `docs/preregistration_002.md:14-33`.
- Run mechanics: Use one foreground, fail-closed publication sequence: create the branch; stage only the explicit manifest; inspect `git diff --cached --name-status` and `git diff --cached --check`; require `verify-seal`, `verify-comite`, `verify-audit`, `audit`, and the already-running `make test` to complete acceptably; commit once; run `git push --dry-run --set-upstream origin agent/phase2-b2-documentation`; only then perform the HTTPS push; verify with `git ls-remote` that remote SHA equals local `HEAD`; create the draft PR through the authenticated connector; finally require a clean local tree. Abort before push on any off-manifest path, visible `email/` artefact, failed gate, test failure, dry-run authentication failure, or SHA mismatch. `Makefile:9-17,38-56` anchors the local gates.
- Reproducibility risks / ambiguities: The current full test result is pending `[UNVERIFIED]`; working-tree drift between committee review and staging can change the reviewed surface, so cached name-status must equal the 25-path manifest; `email/` contains intentionally private source material and must remain ignored (`.gitignore:26-30`; `research_program/bibliography/phase2_novelty_and_item5.md:23-25,199-222`); the B2 document can be misread as target adoption unless its `TARGET_NOT_ADOPTED` and `*_NOT_AUTHORIZED` status is preserved (`phase3_b2_witness_pair_preopening_contract.md:3-9,289-302`); `gh auth status` is invalid (chair DOSSIER), but this is conditionally non-blocking because Git HTTPS push and connector-based draft-PR creation are separate authenticated paths—the exact-branch `git push --dry-run` remains the mandatory proof before publication; remote/local SHA equality and a clean final tree are not established until after the actual push `[UNVERIFIED]`.

### Mathematician brief
- **Computability:** The B2 observation is the isomorphism class of an unlabeled finite **partial** order at fixed \(N=n\), not a total-order assumption (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:123-133`; Surya, *The causal set approach to quantum gravity*, §2, `biblioteca/derived-md/The causal set approach to quantum gravity.md:566-571`). Every relabeling-invariant statistic of that finite poset is decidable in principle. \(Q_{\mathrm{FMOTS}}\), however, is a target on the latent geometric completion, not claimed to be directly computable from the order (`phase3_b2_witness_pair_preopening_contract.md:43-69`). The existing \(\tau(n)\) abstention and `T_EDGE_MIN` domain gates belong exclusively to estimator-v2 (`docs/estimator_v2_freeze.md:48-70`) and must not be imported into B2; B2 correctly specifies no threshold, simulation, code, or seeds (`phase3_b2_witness_pair_preopening_contract.md:289-302`).
- **Order observable:** B2 properly works at the strongest available observation—the complete unlabeled poset—and then invokes data processing under one common sample-to-poset map (`phase3_b2_witness_pair_preopening_contract.md:121-153`). For \(g_\omega=e^{2\omega}g_0\) on the same \(U\), the contract identifies conformal preservation of causal cones as a route requiring proof rather than as an achieved result (`phase3_b2_witness_pair_preopening_contract.md:88-117`); conditional on that common causal relation, the map is parameter-independent and the TV chain is mathematically appropriate. This is separate from the manuscript’s sealed positive observable \(O_{\min}(i)=|\operatorname{future}(i)|\) (`docs/estimator_v2_freeze.md:34-38`), whose finite-patch signal comes from singularity-truncated futures and the resulting bimodality (Eichhorn–Gamito–Stokes, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-195`).
- **Relevant invariants:** Ordering fraction \(r=2R/[n(n-1)]\) is an order invariant tied to dimension in Minkowski sprinklings (Myrheim 1978; Surya §4.1, `biblioteca/derived-md/The causal set approach to quantum gravity.md:986-1011`); \(C_k\) counts \(k\)-chains and is label-invariant (`biblioteca/derived-md/Discrete geometry of a small causal diamond.md:54-65`); longest-chain length is the standard order proxy for timelike distance (Surya §4.3, `biblioteca/derived-md/The causal set approach to quantum gravity.md:1221-1246`); future cardinality is likewise order-only but more boundary-sensitive (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:188-195`). None must be selected as B2’s estimator: a two-point lower bound at the full-poset level applies to every downstream invariant.
- **Analytic / continuum target:** The provisional target is the binary, dimensionless, quasi-local existence functional \(Q_{\mathrm{FMOTS}}\), explicitly distinct from a global event horizon and from a region localizer (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:43-86`). Its continuum semantics are compatible with the standard MOTS condition: outgoing expansion zero and ingoing expansion negative; in Schwarzschild, \(\Theta_{\rm out}=r^{-1}(1-2M/r)\) vanishes at \(r=2M\) (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:199-225`). The required benchmark is an explicit regular pair with \(Q(g_0,U)\neq Q(g_1,U)\) and \(\operatorname{TV}(P_{0,n},P_{1,n})\le\varepsilon_n\), followed by the scoped two-point bound (`phase3_b2_witness_pair_preopening_contract.md:261-274`). The Müller comparison is correctly ceiling-preserving: Theorem 3 is acknowledged as the closest quantitative precursor, and B2 must terminate as redundant if its hypotheses, target, and regime coincide (`phase3_b2_witness_pair_preopening_contract.md:170-186`; `research_program/bibliography/phase2_novelty_and_item5.md:233-279`).
- **Caveats:**
  - The intrinsic, diffeomorphism-invariant definition of \(\mathcal S_{\mathrm{adm}}(g,U)\) is unresolved and is correctly a blocking gate; an externally marked surface would invalidate the target (`phase3_b2_witness_pair_preopening_contract.md:71-77,207-223`).
  - No conformal expansion law, regular matched family, target separation, or small-TV witness has yet been proved; the contract explicitly labels these as obligations and provides fail-closed terminals (`phase3_b2_witness_pair_preopening_contract.md:100-117,188-223,242-259`).
  - The Tier adjudication supports only a bounded family-specific instantiation, not priority: Müller’s quantitative precursor is acknowledged, standard QMD/Hellinger/Le Cam machinery is background, and absolute-priority wording is forbidden (`research_program/bibliography/phase2_novelty_and_item5.md:231-279,301-313`; `docs/manuscript_limits_draft.md:194-200,964-974,1000-1013`).
  - The historical schema migration is mathematically non-destructive: original findings are preserved and `ANNULLED=NO`; decision 042 remains the active C1–C5 closure and 043 remains active only as revised by 044 (`docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md:293-303,350-362`; `docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md:589-599,647-660`).
  - **Recommendation from this seat:** `RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP` for publication of the documentation package only. This does not adopt \(Q_{\mathrm{FMOTS}}\), open witness construction, or authorize code/simulations/seeds (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:289-302`; `tarea_grok_2.md:357-378`). Publication remains conditional on the running full `make test` acquiring an anchored PASS; at present that result is `[UNVERIFIED]`.

### Mathematical logic brief
- Formal status: The Tier A/B material is a procedural adjudication recorded by tier, hash and bounded consequences—not a theorem and not a novelty certificate (`research_program/bibliography/phase2_novelty_and_item5.md:199-222,231-279,317-331`). The manuscript separately labels Theorems 3.1 and 3.8 as proved measure/statistics results and Theorem 3.2 as a proved definitional non-functionality result, with their stated scopes (`docs/manuscript_limits_draft.md:363-453,455-494,540-603`); none is a Lean theorem, because the Lean library deliberately stops at posets, ideals and the relational-horizon interface below the Schwarzschild/sprinkling layer (`formal/HorizonFormal/README.md:3-8`). The B2 expression for \(Q_{\mathrm{FMOTS}}\) is only a provisional definition whose domain component \(\mathcal S_{\mathrm{adm}}(g,U)\) remains open; the conformal family, target separation and MOTS transformation claim are a proposed proof route/open hypotheses, while G1–G9 and the ordered terminals are governance definitions (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:3-9,41-77,88-117,207-223,242-259`). The migrated acts add only disposition metadata and schema correspondences: 012–014 are superseded for forward planning, 039–041 absorbed as historical precursors, 042 remains governing, and 043 remains active as revised by 044; all say `HISTORICAL_FINDINGS=PRESERVED`, `ANNULLED=NO`, and `SCHEMA_MIGRATION_ONLY=YES` (`docs/comite/comite_decision_012_c1-admissible-completion-class.md:396-408`; `docs/comite/comite_decision_013_c1-bce-review.md:606-616`; `docs/comite/comite_decision_014_q-reference-rule-disposition.md:1080-1090`; `docs/comite/comite_decision_039_c4-neighbor-graph-adjudication.md:432-442`; `docs/comite/comite_decision_040_c5-search-space-adjudication.md:341-351`; `docs/comite/comite_decision_041_c5-1-matrix-to-block-map-adjudication.md:348-358`; `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md:293-303`; `docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md:589-599`).
- Quantifier / dependency order: B2 must first fix \(U\), time/outward orientation, the intrinsic and diffeomorphism-invariant rule defining \(\mathcal S_{\mathrm{adm}}\), \(k\), a uniform regularity budget, common boundary data, equivalences, sampling channel and either a fixed \(n\) or announced finite range; only then may it select \(g_0,g_1\), prove \(Q(g_0,U)\ne Q(g_1,U)\), and bound the induced laws (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:71-77,88-110,119-168,211-223`). If the bump depends on \(n\), that dependence and any derivative/curvature deterioration must occur in the theorem statement rather than be chosen after inspecting a witness (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:155-168`). Target adoption precedes witness construction, and witness construction precedes any code, simulation, seeds or thresholds; all remain explicitly unauthorized (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:225-240,289-302`; `tarea_grok_2.md:357-378`).
- Equivalence claims: The proved equalities in the manuscript are the exact fixed-\(n\) equality of poset laws along the stated dilation orbit and its scoped 3+1 analogue, not an equivalence classification of all geometries (`docs/manuscript_limits_draft.md:365-431`). B2 asserts no equality yet: \(\operatorname{TV}(P_{0,n},P_{1,n})\le\operatorname{TV}(\mu_0^{\otimes n},\mu_1^{\otimes n})\) is explicitly one-way data processing, and a point-level upper bound neither proves equality nor gives a converse/visibility result (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:135-153`). `Q_{\mathrm{FMOTS}}\neq T_{\mathrm{EH}}` is presently a type/definition distinction—binary quasi-local existence functional versus global horizon set—not a proved equivalence or inequivalence theorem about physical content (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:64-86,211-220`). “Superseded” and “absorbed” are temporal governance relations, not logical negations of the historical verdicts; the appendices explicitly avoid retroactive expert attribution (`docs/comite/comite_decision_012_c1-admissible-completion-class.md:398-407,423-437`; `docs/comite/comite_decision_039_c4-neighbor-graph-adjudication.md:434-441,456-470`).
- Type / object discipline: \(Q_{\mathrm{FMOTS}}\) is a Boolean functional of latent geometric data \((g,U)\); it is neither a surface, a region-valued localizer, nor an estimator on the observed poset (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:43-69,79-86`). \(\mathcal S_{\mathrm{adm}}(g,U)\) is a metric-dependent class of embedded codimension-two surfaces and cannot be replaced by a hidden marked surface or coordinate-defined label (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:45-77`). \(P_{i,n}\) is a probability law on isomorphism classes of unlabeled finite posets, distinct from a sampled poset and from the product point law (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:119-153`). Existing Lean objects—reference subsets, lower closures and sets of crossing pairs—do not supply a bridge to 3+1 Lorentzian surfaces or \(Q_{\mathrm{FMOTS}}\): the formal source explicitly disclaims event-horizon, Schwarzschild and sprinkling claims (`formal/HorizonFormal/HorizonFormal/Horizon.lean:3-31,38-78`), and the hypothesis audit classifies the pregeometric horizon only as `DEFINITION_FORMALISED`, with physical interpretation open (`dev/LEAN_HYPOTHESIS_AUDIT.md:219-239`).
- Caveats:
  - No formal-logical blocker prevents publishing this package as documentation provided the publication decision does not promote the B2 candidate into an adopted target or theorem; the contract itself states `TARGET_ADOPTION=PENDING_SCIENTIFIC_ADJUDICATION` and leaves construction, code, simulation and seeds unauthorized (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:289-302`).
  - The public repository can authenticate the two local responses only by their recorded hashes; it intentionally cannot reconstruct their identities or full contents, so “neither reader found a prior” remains a recorded adjudication rather than independently replayable public evidence and must retain `NOVELTY_CERTIFIED=NO` (`research_program/bibliography/phase2_novelty_and_item5.md:212-222,248-252`).
  - The manuscript’s Theorem 3.2 remains a prose definitional/existence argument, not a mechanized theorem; its conclusion is scoped to admissible completion pairs agreeing near a common causally convex patch and differing in their global continuation (`docs/manuscript_limits_draft.md:455-483`).
  - A full-suite `make test` PASS is not established by the supplied dossier while the run is pending and must not be asserted in the publication decision until its completed output exists `[UNVERIFIED]`.

### Physicist brief
- Coordinates & patch: The manuscript positive must remain in the finite \(1{+}1\) Schwarzschild model using ingoing Eddington–Finkelstein coordinates \((v,r)\), with \(g_\tau=-(1-\tau/r)dv^2+2\,dv\,dr\), \(\det g=-1\), and \(r=\tau=2M\) as the hidden scoring locus; the sealed endpoint is the finite domain `t_edge=6` (`docs/manuscript_limits_draft.md:216-245`; `docs/preregistration_002.md:37-56`). Finiteness forfeits any claim about the event horizon defined through future null infinity (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:171-179`; `docs/manuscript_limits_draft.md:204-208`). B2 is deliberately different: it requires a compact causally convex \(3{+}1\) patch \(U\) and an intrinsic codimension-two surface class, with no transfer of the \(1{+}1\) EF localizer (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:43-77,100-110`).
- Physical meaning of the signal: For the sealed positive, \(O(i)=|\mathrm{future}(i)|\) is order-only (`docs/manuscript_limits_draft.md:686-698`). In singular Schwarzschild, futures from interior minimal elements are shortened by termination at \(r=0\), whereas exterior futures extend to the finite box boundary; this produces the observed/expected bimodality, with the continuum transition aligned with \(r=2M\), but future cardinality is explicitly boundary-sensitive (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-193`). Hence the manuscript correctly calls it a horizon-associated in-patch score, not an intrinsic horizon reconstruction (`docs/manuscript_limits_draft.md:765-780`). B2’s provisional \(Q_{\mathrm{FMOTS}}\) is instead a latent binary existence/classification target, \(\theta_+=0,\theta_-<0\), not a region locator or estimator (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:45-69,79-86`); its physical motivation is that in \(3{+}1\) Schwarzschild \(\Theta_{\rm out}\) changes sign and vanishes at \(r=2M\), while \(\Theta_{\rm in}<0\) (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:217-227`).
- Sprinkling domain: The existing positive uses genuine natural-volume Poisson sprinkling with no densification in the finite \(1{+}1\) EF domain; the estimator receives only the anonymized poset and cardinality (`docs/preregistration.md:59-67`). Its declared levels are \(\lambda=1500,3000,6000,12000\), with \(12000\) primary and `t_edge=6` (`docs/preregistration_002_result.md:38-60`). B2 instead conditions on \(N=n\): \(n\) i.i.d. points from normalized volume on compact \(U\), followed by a parameter-independent sample-to-unlabeled-poset map with coordinates and embedding labels forgotten (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:119-153`). Consequently B2 forfeits cardinality/intensity information and currently promises only a fixed-\(n\) or explicitly finite-\(n\)-range lower-bound route, not a Poisson-count or asymptotic guarantee (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:155-168`).
- Claim boundary: The package is physically coherent for documentary publication because it now distinguishes the continuous \(1{+}1\) family parameter from a horizon detector, keeps the validated signal bounded to finite-patch recoverability, and leaves the \(3{+}1\) B2 target unopened (`docs/manuscript_limits_draft.md:605-621,665-674`; `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:289-302`). This verdict does **not** claim metric reconstruction, an asymptotic/global event horizon, transfer of the \(1{+}1\) positive to \(3{+}1\), adoption of \(Q_{\mathrm{FMOTS}}\), existence of a witness pair, or authorization of code, simulation, thresholds, or seeds (`docs/preregistration_002_result.md:63-75`; `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:3-9,257-259`).
- Caveats:
  - The singularity-truncated-future mechanism is not robust to geodesically complete regular black holes: the cited paper expects the interior/exterior partition diagnostic to fail there, although apparent-horizon/geodesic-expansion concepts may remain meaningful (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:193-201,463-469`).
  - A \(1{+}1\) sprinkling has no spatial two-surfaces on which to compute the \(3{+}1\) null expansions; B2 must therefore prove its own \(3{+}1\) target statement rather than inherit the ladder or future-volume interpretation (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:221-234`; `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:102-110`).
  - \(\mathcal S_{\mathrm{adm}}\), exterior orientation, normalization of null normals, and boundary conditions remain unresolved; any hidden marked surface or boundary-created MOTS blocks target adoption (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:59-77,188-205`).
  - The conformal route is only a proof strategy: preservation of causal cones does not itself establish a change in \(Q_{\mathrm{FMOTS}}\), controlled regularity, or small total variation of normalized-volume poset laws (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:88-117,135-168`).
  - The external review closes its procedural item but supplies no novelty certificate; Müller Theorem 3 remains the closest quantitative precursor and absolute-priority language stays forbidden (`research_program/bibliography/phase2_novelty_and_item5.md:231-279`; `docs/manuscript_limits_draft.md:1002-1013`).

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes: (1) `.gitignore` is not a privacy boundary: `email/` can still be force-added or its recipient-identifying/full-response text copied into a tracked document; only the two hashes and bounded adjudication are admissible publicly (`.gitignore:26-30`; `research_program/bibliography/phase2_novelty_and_item5.md:196-222`). (2) The migrated 012–014 and 039–043 acquire current-schema expert headings, PASS/PROCEED tokens and “User sign-off”, which can be misquoted as contemporaneous expert deliberation even though the appendices say schema-only, preserve history and prohibit retrospective attribution; the current verdict tokens must never be cited as the original verdict (`docs/comite/comite_decision_012_c1-admissible-completion-class.md:396-408,423-469`; `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md:293-303,317-362`; `docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md:589-599,614-660`). (3) “not found by either reader” can become an illicit novelty certificate in a commit/PR summary; the controlling text instead says `NOVELTY_CERTIFIED=NO`, forbids absolute-priority wording, identifies Müller Theorem 3 as the closest precursor and calls the method standard (`research_program/bibliography/phase2_novelty_and_item5.md:231-279,301-313`). (4) Publishing a document headed “target candidato recomendado” can be mistaken for adopting \(Q_{\mathrm{FMOTS}}\); publication is coherent only while `TARGET_NOT_ADOPTED`, `TARGET_ADOPTION=PENDING_SCIENTIFIC_ADJUDICATION` and all construction/code/simulation/seed prohibitions survive verbatim (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:3-9,41-77,289-302`). (5) Connector permission does not prove Git HTTPS authentication or that `origin` names the confirmed repository `[UNVERIFIED]`; an invalid `gh` token, wrong remote/branch, non-draft PR, PR creation before branch publication, or local/remote SHA mismatch defeats publication despite a local commit. The required proof remains exact-branch dry-run, actual push, `git ls-remote` equality and only then draft-PR creation (chair DOSSIER; reproducibility brief).
- Ground-truth leakage: The documentary patch does not authorize use of the hidden embedding, and the sealed benchmark still permits it only for scoring after an order-only freeze (`CLAUDE.md:14-18`; `docs/preregistration.md:25-35`). B2 nevertheless contains a latent-leakage route if \(\mathcal S_{\mathrm{adm}}\), exterior orientation, the witness bump or the claimed target separation is chosen using a marked surface, hidden coordinates or inspected geometric labels; the contract correctly makes that a blocking terminal, which publication must not soften (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:71-77,121-153,188-223`).
- Freeze violations: None is established in the reviewed documentation: the seal check passed at `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, the chair’s completed `make test` returned `270 passed in 370.35s`, exit 0, and the surface contains no changed code, thresholds, seeds or results (chair DOSSIER). Publication must still abort if its mechanics invoke `validate.run()`, B2 witness execution, simulations, fresh seeds, threshold selection or any sealed-file change; the blind run remains single-use and all PASS/FAIL/INCONCLUSIVE/OUT_OF_DOMAIN outcomes must be reported without rerun or loosening (`docs/preregistration_002.md:35-68`; `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:289-302`).
- Verdict coercion: The migration risks coercing historical nuanced outcomes into the checker-compatible PASS/PROCEED token appended in 2026; `SCHEMA_MIGRATION_ONLY=YES`, `HISTORICAL_FINDINGS=PRESERVED`, `ANNULLED=NO` and each original terminal must govern interpretation (`docs/comite/comite_decision_012_c1-admissible-completion-class.md:396-408,457-474`; `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md:293-303,350-367`). For B2, every typed block, redundancy terminal and `B2_TARGET_ADMISSIBLE_FOR_WITNESS_CONSTRUCTION` must be publishable alike; “admissible” authorizes only a later mathematical proof, while a push/authentication failure is an operational abort—not scientific FAIL or evidence against B2 (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:242-259,276-287`).
- Premature / over-broad claims: The package may publish only a procedural Tier adjudication, bounded manuscript corrections, historical-schema metadata and a preopening contract. It does not certify novelty, adopt \(Q_{\mathrm{FMOTS}}\), prove a witness pair, reconstruct a metric/event horizon, establish an asymptotic or 3+1 result, or transfer the finite 1+1 localizer to B2 (`research_program/bibliography/phase2_novelty_and_item5.md:248-279,301-313`; `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:64-86,155-186,257-259,289-302`; `docs/preregistration.md:69-72`). Commit and PR wording must retain that ceiling.
- Independent-falsification gate: The content has now received separate Wave-1 expert review and this independent Wave-2 attack, so its author is not its sole conceptual verifier; the completed full test removes the previously unverified test blocker (chair DOSSIER). The gate is nevertheless only conditional until the chair independently verifies the exact staged bytes, final committee brief, dry-run target, pushed remote SHA and draft-PR state; none of those post-staging/publication facts yet exists `[UNVERIFIED]` (`docs/preregistration.md:74-78`; reproducibility brief).
- Minimal falsification test: Immediately before commit, run `git diff --cached --name-status` and require byte-for-byte equality with the committee-approved explicit 25-path manifest—23 reviewed tracked documentation paths, the new B2 contract and decision 047—with no `email/`, code, data, result, threshold, dependency or other off-manifest path; any discrepancy aborts before commit or push (`.gitignore:26-30`; chair DOSSIER; reproducibility brief).

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: PASS
- Freeze status: N/A for this documentation-only publication and B2 preopening: it introduces no threshold, freeze, code, simulation or scientific execution (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:3-9,289-302`). The pre-existing estimator-v2 thresholds and verdict aggregation remain immutable as written (`docs/preregistration_002.md:35-57`).
- Seal integrity: The proposed publication does not run or alter the sealed validation path; the chair verified `make verify-seal` → PASS at the prereg-002 SHA256 `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, exactly matching `docs/preregistration_002.md:7-12`. B2 explicitly records `SEALED_PATH = UNTOUCHED` (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:289-302`).
- Seed discipline: No seed band is used or reserved by this publication; B2 states `SEEDS = NOT_AUTHORIZED` (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:289-300`). The historical prereg-002 validation band `[2_000_000,2_999_999]`, its one-time blind draw, and its disjoint exploration pool are documented at `docs/preregistration_002.md:14-33`; this documentary step burns no additional seed.
- Reporting rule: The existing binding rule reports PASS, FAIL, INCONCLUSIVE and OUT_OF_DOMAIN alike and forbids tuning, fresh-seed reruns after peeking, and threshold loosening (`docs/preregistration_002.md:59-68`). B2 has no empirical verdict to report and cannot open witness construction, simulation, code or seeds through this publication (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:242-259,289-302`).
- Forbidden moves present? None in the reviewed publication scope: no post-hoc tuning, threshold loosening, ground-truth leakage, re-run after peeking, or reconstruction over-claim. The package preserves the finite-patch recoverability ceiling (`docs/preregistration_002_result.md:63-75`) and explicitly keeps B2 target adoption and scientific execution unopened (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:3-9,289-302`).
- Reasons:
  - PASS authorizes only documentary publication; it does not adopt \(Q_{\mathrm{FMOTS}}\), construct a witness, or authorize code, simulations, seeds, thresholds or a B2 scientific claim (`research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md:225-240,257-259,289-302`).
  - The sealed estimator contract remains one-way and unchanged; its historical result retains the bounded `NO_RECONSTRUCTION_CLAIM` interpretation (`docs/preregistration_002.md:59-68`; `docs/preregistration_002_result.md:63-75`).
  - The chair’s completed `make test` result is `270 passed in 370.35s`, exit 0; together with the supplied seal PASS, this removes the Wave-1 pending-test condition (Committee 047 dossier, “Verified state supplied by the chair”).

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Surya, *The causal set approach to quantum gravity*, §2, Poisson sprinkling and induced partial order | Mathematician | CONFIRMED |
| Surya, *The causal set approach to quantum gravity*, §4.1, Eq. (14), Myrheim–Meyer ordering fraction | Mathematician | CONFIRMED |
| Surya, *The causal set approach to quantum gravity*, §4.3, Eqs. (21)–(22), longest-chain timelike-distance proxy | Mathematician | CONFIRMED |
| Roy et al., *Discrete geometry of a small causal diamond*, §2, definition and label invariance of \(k\)-chain abundances | Mathematician | CONFIRMED |
| Eichhorn–Gamito–Stokes, *Towards black-hole horizons and geodesic focusing in causal sets*, §III, Fig. 3 | Mathematician; Physicist | CONFIRMED |
| Eichhorn–Gamito–Stokes, *Towards black-hole horizons and geodesic focusing in causal sets*, §IV, Eqs. (10)–(12) | Mathematician; Physicist | CONFIRMED |
| Eichhorn–Gamito–Stokes, *Towards black-hole horizons and geodesic focusing in causal sets*, §VI | Physicist | CONFIRMED |
| Müller, *On the Hauptvermutung of Causal Set Theory*, Theorem 2 | Mathematician; Physicist | CONFIRMED |
| Müller, *On the Hauptvermutung of Causal Set Theory*, Theorem 3 and its proof | Mathematician; Physicist | CONFIRMED |
| `phase2_novelty_and_item5.md` §§3.4–3.6 and `manuscript_limits_draft.md` §§1.6, 6.2, 6.5 | Mathematician; Mathematical logic; Physicist | CONFIRMED |

- Notes: Surya confirms that sprinkling induces a finite partial order, not a total-order assumption; the ordering fraction and longest-chain statements are correctly scoped to their embedding/ensemble regimes. Eichhorn–Gamito–Stokes confirms the finite-patch, singularity-truncated bimodality and boundary sensitivity, the failure of that diagnostic for geodesically complete regular black holes, the Schwarzschild expansions \(\Theta_{\rm in}=-2/r\) and \(\Theta_{\rm out}=r^{-1}(1-2M/r)\), and the absence of spatial two-surfaces in the paper’s \(1+1\)-dimensional setting. Müller’s Theorem 2 gives arbitrarily close fixed-\(K\) order laws for unit-volume slabs with arbitrarily large \(d^{-}\) separation; Theorem 3 gives the explicit concentration bound \(E\ge 1-4\pi K^2T^{-1/n}\) for normalized flat cylinders while temporal diameters separate. Thus “closest quantitative precursor” is supported, but Müller does not formulate QMD, Fisher information, Le Cam risk, or a local minimax floor. The public package repeatedly records `NOT_A_NOVELTY_CERTIFICATE`, `NOVELTY_CERTIFIED=NO`, identifies Müller Theorem 3, treats the post-QMD machinery as standard, and forbids absolute-priority language. The narrower statement that neither reader found a prior remains a hash-anchored adjudication whose underlying responses are intentionally absent from the public tracked tree; it is not independently replayable from the public package.

## 8. Synthesis

**Consenso.** Los siete roles convergen en que el paquete es coherente y puede publicarse como
documentación. La segunda oleada confirma la literatura citada y el custodio emite `PASS`.
La suite completa, pendiente durante algunos briefs de Wave 1, terminó después con
`270 passed in 370.35s`, eliminando esa condición.

La publicación tiene un alcance único:

1. registrar la adjudicación procedural de ambas respuestas externas sin nombres ni textos
   íntegros y sin convertir “prior no encontrado” en certificado de novedad;
2. aplicar al manuscript las correcciones acotadas ya enumeradas;
3. migrar el esquema de ocho actas sin anularlas, borrar su contenido ni presentar los nuevos
   tokens como sus veredictos contemporáneos originales;
4. publicar B2 únicamente como contrato de preapertura.

**Caveats vinculantes.**

- `email/` permanece completamente fuera del índice. El hash no autoriza publicar el documento.
- Los tokens de compatibilidad añadidos a 012–014 y 039–043 son metadatos de migración; sus bloques
  originales siguen gobernando la interpretación histórica.
- `Q_FMOTS` no está adoptado. \(\mathcal S_{\mathrm{adm}}\), la familia regular, la transformación
  conforme, la separación del target y la cota TV siguen abiertos.
- El commit y el PR no usarán lenguaje de prioridad, reconstrucción, resultado 3+1 ni apertura
  científica de B2.
- La autenticación CLI inválida no se oculta; el push solo procede si el dry-run HTTPS funciona y
  la rama remota termina con el mismo SHA local. El PR debe ser borrador.

**Desacuerdos abiertos.** No hay desacuerdo sobre publicar. Sí hay una diferencia de énfasis:
matemática considera admisible el marco B2 como pregunta, mientras lógica, física y falsificador
subrayan que el target aún no está definido de forma cerrada. No es una contradicción: el objeto
que se publica es precisamente un contrato fail-closed, no una adopción del target.

## 9. Next-step spec

### Reversible / verificación — completado

1. Verificar sello, suite, checker de comité, informes de auditoría, auditor general y
   `git diff --check`.
2. Verificar que `email/` está ignorado y que no hay código, datos, resultados, dependencias ni
   umbrales en la superficie.
3. Obtener revisión independiente de siete roles y registrar los desacuerdos.

### Committing / outward-facing — autorizado por la instrucción del PI

1. Crear `agent/phase2-b2-documentation` desde
   `29f84357ae7c5e6b8eb4d2afc1ce75949c3b190f`.
2. Stagear **solo** este manifest de 25 rutas:
   - `README.md`
   - `docs/comite/comite_decision_012_c1-admissible-completion-class.md`
   - `docs/comite/comite_decision_013_c1-bce-review.md`
   - `docs/comite/comite_decision_014_q-reference-rule-disposition.md`
   - `docs/comite/comite_decision_039_c4-neighbor-graph-adjudication.md`
   - `docs/comite/comite_decision_040_c5-search-space-adjudication.md`
   - `docs/comite/comite_decision_041_c5-1-matrix-to-block-map-adjudication.md`
   - `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md`
   - `docs/comite/comite_decision_043_c6-internal-alexandrov-waist-screen-adjudication.md`
   - `docs/comite/comite_decision_047_phase2-b2-documentation-publication.md`
   - `docs/manuscript_limits_draft.md`
   - `research_program/bibliography/README.md`
   - `research_program/bibliography/external_adversarial_review_package_n1_n5.md`
   - `research_program/bibliography/external_reader_candidates_n1_n5.md`
   - `research_program/bibliography/phase2_novelty_and_item5.md`
   - `research_program/bibliography/wp5_paso_d_independent_novelty_review.md`
   - `research_program/synthesis/phase1_limits_paper_outline.md`
   - `research_program/synthesis/phase1_section1_2_abstract_draft.md`
   - `research_program/synthesis/phase1_section3_nonidentifiability_draft.md`
   - `research_program/synthesis/phase1_section6_7_8_draft.md`
   - `research_program/work_packages/README.md`
   - `research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md`
   - `research_program/work_packages/wp4_fisher_localization_floor.md`
   - `research_program/work_packages/wp5_shape_scanner_design.md`
   - `tarea_grok_2.md`
3. Falsificador mínimo: exigir igualdad exacta entre `git diff --cached --name-status` y el
   manifest; cualquier ruta extra aborta antes del commit.
4. Repetir `git diff --cached --check`, `make verify-seal`, `make verify-comite`,
   `make verify-audit` y `make audit`.
5. Commit único: `docs: close external review and prepare Phase 3 B2`.
6. `git push --dry-run --set-upstream origin agent/phase2-b2-documentation`; si falla, parar.
7. Push real, luego `git ls-remote` y exigir SHA remoto = `HEAD`.
8. Crear PR **borrador** hacia `main` mediante el conector, con wording:
   cierre procedural, manuscript acotado, migración histórica y preapertura B2; no certificado
   de novedad ni apertura científica.
9. Verificar árbol limpio y registrar rama, commit, SHA remoto y URL del PR.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

- **2026-07-28 — PI/user:** instrucción explícita `COMITEA Y PUSHEA`.
- Interpretación vinculante: autoriza la secuencia de publicación de §9 si y solo si los gates,
  el manifest exacto, el dry-run y la igualdad de SHA pasan.
- No autoriza adopción de `Q_FMOTS`, construcción de testigo, código, simulaciones, semillas,
  umbrales, ejecución sellada ni lenguaje de novedad/reconstrucción.
