# Comite Decision 031 — Phase 1 theory package audit gate

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action, never tunes a frozen threshold post-hoc, and never makes a
> reconstruction claim. Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`,
> `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Do exact blobs OP-1.1 `6d024df0376d701b6c26c061d2c565942ebd3ab19a687f2c480551cae84f3024`,
OP-1.2 `0bfb9eeddc9ad14354956a99e522c1ca5b0ed05e7838d31be84c4fe63ac1663f`, and OP-1.3
`60e874813c44ebe31bbed40cde507c18fe8e8e686447d76ca96452553d64fb1b` close decision 030
section 9 and qualify as `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`?

## 2. Verified state

- `HEAD=origin/main=496985dbecd464a57267e607b7d3b48c323b510b` when checked by the chair.
- `sha256sum` returned the three hashes in section 1 and signed decision-030 hash
  `5622c0f5da1ef674de25f8b98d0f6a906743013350ee155aecac695993b44927`.
- Before this brief, `git status --short --branch` showed seven untracked documentary files: four
  committee decisions and the three candidate documents. No tracked code or data change appeared.
- Decision 030 records PI authorization at
  `docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md:175-183`.
- The exact normalization marker occurs adjacent to the formula and in the source list
  (`research_program/synthesis/op11_spherical_dual_target.md:25-37,340-345`).
- Static whitespace checks emitted no errors. The marker-presence check returned exit code 0.
- No `/auditor`, code, simulation, test, commit or push was run. Seal and executable environment
  remain `[UNVERIFIED_THIS_SESSION]`; this verdict is documentary and exact-hash scoped.

## 3. Dossier

- `research_program/synthesis/op11_spherical_dual_target.md`;
- `research_program/synthesis/op12_tv_zero_3p1.md`;
- `research_program/work_packages/op13_positive_evidence_protocol.md`;
- `docs/comite/comite_decision_027_phase1-theory-package-first-review.md` through
  `docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md`;
- `docs/claim_grammar.md`;
- `docs/plan_operativo_15_julio_2026.md`;
- local citations listed in the three candidate documents and reviewed below.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): **PROCEED — `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** OP11 `6d024df0376d701b6c26c061d2c565942ebd3ab19a687f2c480551cae84f3024`, OP12 `0bfb9eeddc9ad14354956a99e522c1ca5b0ed05e7838d31be84c4fe63ac1663f` y OP13 `60e874813c44ebe31bbed40cde507c18fe8e8e686447d76ca96452553d64fb1b` fueron recalculados y coinciden exactamente con los blobs sometidos.
- Environment & seal: HEAD y `origin/main` coinciden en `496985dbecd464a57267e607b7d3b48c323b510b`; los siete documentos de decisiones/candidatos permanecen untracked `[VERIFIED_THIS_ROLE]`. El sello reproducible del paquete es base commit más los tres SHA256 exactos. No existe entorno científico ejecutado ni autorizado; OP13 mantiene `NO_EXECUTION_AUTHORIZED` (`research_program/work_packages/op13_positive_evidence_protocol.md:1-10,223-230`).
- Provenance capture: Decision 030 autorizó únicamente marcador adyacente, entrada correspondiente en fuentes y actualizaciones mecánicas de procedencia (`docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md:150-169,175-183`). OP11 incorpora el marcador junto a la fórmula (`research_program/synthesis/op11_spherical_dual_target.md:25-37`) y en fuentes (`research_program/synthesis/op11_spherical_dual_target.md:340-345`); OP11-OP13 registran decision 030 y sign-off (`research_program/synthesis/op11_spherical_dual_target.md:9-14`, `research_program/synthesis/op12_tv_zero_3p1.md:5-10`, `research_program/work_packages/op13_positive_evidence_protocol.md:5-10`).
- Run mechanics: La adopción solo habilita la auditoría posterior de estos hashes exactos; no habilita código, simulaciones, tests, seeds ni recovery. OP11 mantiene explícitamente que no existe reconstructor, selector ni convergencia probada (`research_program/synthesis/op11_spherical_dual_target.md:328-338`), y OP13 deja generador y testigo concretos para una spec futura (`research_program/work_packages/op13_positive_evidence_protocol.md:223-230`).
- Reproducibility risks / ambiguities: La historia byte a byte entre los candidatos anteriores y estos archivos untracked no puede reconstruirse desde Git `[UNVERIFIED]`; el dictamen se aplica al contenido íntegro de los hashes actuales. La auditoría debe verificar el paquete exacto, la superficie exclusivamente documental y la conservación literal del estado `UNVERIFIED`, sin convertirlo en validación física de la constante (`research_program/synthesis/op11_spherical_dual_target.md:32-37,342-345`). No queda un bloqueo reproducible previo a auditoría.

### Mathematician brief
- Computability: `P^op` permanece definido sobre el mismo portador, con `iota_P=id`, involución y naturalidad bajo todo relabeling (`research_program/synthesis/op11_spherical_dual_target.md:190-203`). Las salidas duales siguen siendo funciones totales sobre representantes equivariantes (`research_program/synthesis/op11_spherical_dual_target.md:213-242`).
- Order observable: El nuevo marcador solo declara el estado bibliográfico del coeficiente Kruskal; no modifica orden, patch, medida, targets ni salidas (`research_program/synthesis/op11_spherical_dual_target.md:25-37`; `docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md:150-169`). El paquete continúa sin afirmar un localizador concreto; OP-1.3 certifica únicamente un testigo order-only preespecificado y distingue separación de recoverability (`research_program/work_packages/op13_positive_evidence_protocol.md:12-34,163-174`).
- Relevant invariants: El bloqueo de abstención permanece cerrado: cada `ABSTAIN` por elemento cuenta como error, permanece en el denominador, genera tasas separadas `A_side`/`A_trapping`, y cualquier denominador vacío produce `LOSS_UNSCORABLE` (`research_program/synthesis/op11_spherical_dual_target.md:263-283`). La dualidad del mismo portador concuerda con la definición estándar del dual como inversión de flechas sin cambiar el conjunto (Bombelli, Eq. 2.1.3, `biblioteca/derived-md/Bombelli_1987_PhD.md:402-407`).
- Analytic / continuum target: El marcador conserva `32M^3/r` como convención declarada y reconoce que el snapshot local no la verifica literalmente (`research_program/synthesis/op11_spherical_dual_target.md:25-37,340-345`). Esto no altera la clausura bajo `D`: la prueba usa preservación de `UV`, medida y reversión del orden para obtener `Law_K(Dg)=d_#Law_K(g)` (`research_program/synthesis/op11_spherical_dual_target.md:88-108,190-211`). Tampoco altera OP-1.2: el argumento `TV=0` depende del coescalado `g_{M'}=a^2g_M`, del volumen `a^4` y de la medida normalizada, no de verificar externamente esa constante convencional (`research_program/synthesis/op12_tv_zero_3p1.md:47-80`). La cota inferior de OP-1.3 es puramente probabilística y permanece idéntica (`research_program/work_packages/op13_positive_evidence_protocol.md:24-80`).
- Caveats: **Recomendación: `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** La corrección única autorizada por decisión 030 §9 aparece adyacente a la fórmula y en la lista de fuentes, sin cambiar los resultados matemáticos (`docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md:150-169`; `research_program/synthesis/op11_spherical_dual_target.md:25-37,340-345`). `iota_P` y el scoring fail-closed de `ABSTAIN` siguen completamente tipados; no detecto otro bloqueo matemático. La auditoría debe preservar el estado `UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT`, y ninguna adopción autoriza reconstructor, recovery o ejecución (`research_program/synthesis/op11_spherical_dual_target.md:328-338`; `research_program/work_packages/op13_positive_evidence_protocol.md:223-229`).

### Mathematical logic brief
- Formal status: **PROCEED**. The submitted exact blobs qualify as `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`: decision 030’s sole remaining blocker is closed by the adjacent normalization marker and matching source entry, while the coefficient remains a declared convention and theorem-independence is explicit (`research_program/synthesis/op11_spherical_dual_target.md:23-37,340-345`). Decision-030 provenance appears in all three blobs (`research_program/synthesis/op11_spherical_dual_target.md:9-14`; `research_program/synthesis/op12_tv_zero_3p1.md:5-10`; `research_program/work_packages/op13_positive_evidence_protocol.md:5-10`).
- Quantifier / dependency order: OP-1.2 correctly separates fixed `n`, all `n>=0`, and asymptotic equivalence; its scaling conclusion is restricted to fixed `lambda` and temporal sector, while `ell_eff` is defined only for `n>=1` and only as a scoring scale (`research_program/synthesis/op12_tv_zero_3p1.md:12-22,47-103`). OP-1.3 freezes laws, witness, multiplicity, sample sizes and generator-error bounds before confirmatory sampling, and forbids uninstantiated sequential stopping (`research_program/work_packages/op13_positive_evidence_protocol.md:35-80,122-161`).
- Equivalence claims: The coupling lemma is sufficient rather than reciprocal and carries the required conull, bimeasurable and almost-every-pair hypotheses (`research_program/synthesis/op12_tv_zero_3p1.md:24-45`). Fixed-`n` mass degeneracy, known-density Poisson identifiability and BH/WH dual pushforward are stated on their proper restricted domains; general TV-zero classification and oriented BH/WH equality remain open (`research_program/synthesis/op12_tv_zero_3p1.md:47-80,105-138,140-180`).
- Type / object discipline: Order duality uses the same carrier, a total involutive `iota_P=id`, relabeling naturality and a law-level pushforward without embedding correspondence (`research_program/synthesis/op11_spherical_dual_target.md:190-211`). Output codomains distinguish the empty interface from `ABSTAIN`; `nu` is total, elementwise abstentions count as errors and remain in denominators, and terminal precedence is total (`research_program/synthesis/op11_spherical_dual_target.md:213-301,303-326`). The positive-evidence theorem distinguishes intended from generated laws and certifies only the bounded-witness lower bound with simultaneous coverage (`research_program/work_packages/op13_positive_evidence_protocol.md:11-80,176-230`).
- Caveats: The Kruskal normalization remains explicitly unverified rather than proved, which is now honest and non-load-bearing (`research_program/synthesis/op11_spherical_dual_target.md:32-37,342-345`). The author terminals establish only dual-family closure, a scoped TV-zero class and a conditional statistical protocol; they do not establish an estimator, selector, convergence, single-instance reconstruction or 3+1D recoverability (`research_program/synthesis/op11_spherical_dual_target.md:328-338`; `research_program/synthesis/op12_tv_zero_3p1.md:168-181`; `research_program/work_packages/op13_positive_evidence_protocol.md:205-230`). Final readiness remains blocked on exact-hash audit; committee adoption alone is not `PHASE_1_THEORY_READY`.

### Physicist brief
- Coordinates & patch: La fórmula permanece `ds^2=-(32M^3/r)e^{-r/2M}dU dV+r^2dOmega_2^2`, con la misma relación implícita para `r`, patch angular completo e involución `D(U,V,omega)=(-V,-U,omega)` (`research_program/synthesis/op11_spherical_dual_target.md:23-74`). El nuevo texto no modifica la métrica: declara 32 como convención y marca explícitamente que el snapshot local no la verifica literalmente (`research_program/synthesis/op11_spherical_dual_target.md:25-37`).
- Physical meaning of the signal: El target continúa siendo `r=2M`, frontera entre esferas atrapadas/no atrapadas, con localización dual-invariante y carácter BH/WH anti-invariante (`research_program/synthesis/op11_spherical_dual_target.md:123-174`). El marcador bibliográfico no altera expansiones, orientación, target ni scoring.
- Sprinkling domain: La afirmación de independencia es físicamente razonable para los teoremas declarados. Interpretar 32 como coeficiente combinado y 16 como componente simétrico describe el mismo tensor. Incluso la clasificación de escala de OP12 usa normalización de volumen en `fixed_n` y únicamente la ley `mu_M(K)=M^4mu_1(K)` en Poisson (`research_program/synthesis/op12_tv_zero_3p1.md:47-80,105-123`); esas conclusiones no dependen del convenio de escritura del término cruzado. La causalidad ambiente y la medida positiva permanecen congeladas (`research_program/synthesis/op11_spherical_dual_target.md:76-108`).
- Claim boundary: **PROCEED — `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** Decision 030 exigía marcador adyacente, entrada correspondiente en fuentes y ningún cambio científico (`docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md:150-169`). Ambos marcadores están presentes y dicen exactamente que el snapshot no verifica literalmente 32 (`research_program/synthesis/op11_spherical_dual_target.md:32-37,340-345`). El paquete no reclama estimador, convergencia ni recovery 3+1D (`research_program/synthesis/op11_spherical_dual_target.md:328-338`), y OP13 separa explícitamente evidencia TV de localización (`research_program/work_packages/op13_positive_evidence_protocol.md:163-174,223-230`).
- Caveats: La fuente local sigue mostrando 16 en una presentación bidimensional y no explicita la convención del producto cruzado (`biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562,3628-3663`). Por tanto la adopción no verifica físicamente el coeficiente 32; únicamente conserva honestamente su estado no verificado. Si 16 se interpretara como una métrica alternativa y no como notación de componentes, la equivalencia física requeriría una derivación separada. Esa ambigüedad queda correctamente fuera del claim actual y debe permanecer visible durante auditoría.

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes: No encuentro un bloqueo load-bearing. Los SHA256 recalculados coinciden exactamente con OP11 `6d024df...`, OP12 `0bfb9eed...` y OP13 `60e87481...` `[VERIFIED_THIS_ROLE]`. El marcador aparece inmediatamente después de la fórmula (`research_program/synthesis/op11_spherical_dual_target.md:25-37`) y vuelve a aparecer en la entrada de fuente que reconoce que el snapshot no verifica literalmente 32 (`research_program/synthesis/op11_spherical_dual_target.md:340-345`). El riesgo residual es semántico: 16 solo es equivalente si significa componente simétrico; como métrica radial realmente distinta requeriría otra prueba. El texto evita esa promoción al fijar 32 como convención y conservar `UNVERIFIED`.
- Ground-truth leakage: No aparece una ruta nueva. Embedding, `r`, `M` y expansiones están prohibidos en construcción, selección, orientación y abstención (`research_program/synthesis/op11_spherical_dual_target.md:235-245`). La dualidad usa el mismo portador y naturalidad bajo relabeling, no correspondencias continuas (`research_program/synthesis/op11_spherical_dual_target.md:190-211`).
- Freeze violations: No se autoriza ejecución ni elección retrospectiva. Decision 030 permitió únicamente marcador, fuente y procedencia (`docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md:150-169,175-183`), y OP13 mantiene toda elección concreta para una spec futura (`research_program/work_packages/op13_positive_evidence_protocol.md:223-230`). La delta byte a byte frente a los blobs anteriores no es reconstruible desde archivos untracked `[UNVERIFIED]`, pero la adopción queda sellada sobre los hashes actuales y no hereda resultados.
- Verdict coercion: El contrato anterior permanece cerrado: `ABSTAIN` puntual cuenta como error, no abandona denominadores y genera tasas separadas (`research_program/synthesis/op11_spherical_dual_target.md:263-283`). Predicción vacía y abstención de interfaz siguen siendo objetos distintos; los casos no puntuables conservan terminal propio (`research_program/synthesis/op11_spherical_dual_target.md:213-242,285-326`).
- Premature / over-broad claims: No hay recovery encubierto. OP11 niega estimador, selector y convergencia (`research_program/synthesis/op11_spherical_dual_target.md:328-338`); OP13 declara que separación TV no implica localización (`research_program/work_packages/op13_positive_evidence_protocol.md:163-174`). La constante Kruskal no se presenta como verificada por la fuente local. La independencia de los teoremas es razonable bajo la distinción coeficiente combinado/componente simétrico y no autoriza tratar 16 como una geometría alternativa (`research_program/synthesis/op11_spherical_dual_target.md:32-37`).
- Independent-falsification gate: **SATISFIED — PROCEED a `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** La condición exacta de decision 030 está cerrada y sobreviven `iota_P=id`, involución y naturalidad (`research_program/synthesis/op11_spherical_dual_target.md:190-203`), junto con el scoring fail-closed. La auditoría de hashes sigue siendo necesaria; este gate no equivale a `PHASE_1_THEORY_READY`.
- Minimal falsification test: `rg -n 'ds\^2 = -\(32 M\^3/r\)|UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT|iota_P = id|ABSTAIN.*cuenta como error' research_program/synthesis/op11_spherical_dual_target.md` debe mostrar la fórmula, dos apariciones del marcador, `iota_P=id` y la política fail-closed; cualquier ausencia bloquea auditoría (`research_program/synthesis/op11_spherical_dual_target.md:29-37,195,274,342-345`).

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: PASS
- Freeze status: This PASS applies only to freezing the three exact documentary blobs as `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`; their SHA256 values are recorded in the decision question and verified state (`docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md:10-28`). No witness, generator, numerical loss threshold or confirmatory grid is frozen or executable yet; those require a later pre-run specification (`research_program/synthesis/op11_spherical_dual_target.md:247-261`; `research_program/work_packages/op13_positive_evidence_protocol.md:35-46,135-139,223-230`).
- Seal integrity: The proposed step does not run or alter the sealed estimator path. The operative prereg-002 reference remains `thresholds.py` SHA256 `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (`docs/preregistration_002.md:1-12`); no seal verification or scientific execution is part of this adoption (`research_program/work_packages/op13_positive_evidence_protocol.md:1-10,223-230`).
- Seed discipline: No seed band is consumed. The legacy prereg-002 virgin and burned bands remain separate (`docs/preregistration_002.md:14-33`); any future OP-1.3 confirmation must freeze development provenance, use independent confirmatory replicas and register disjoint seed derivation before consumption (`research_program/work_packages/op13_positive_evidence_protocol.md:83-108,135-139`).
- Reporting rule: `PASS` means only committee adoption pending exact-hash audit, not `PHASE_1_THEORY_READY`, run authorization or scientific success. Future OP-1.3 reports the first applicable terminal under its frozen total precedence and cannot promote the conditional author theorem into a scientific PASS (`research_program/work_packages/op13_positive_evidence_protocol.md:176-230`).
- Forbidden moves present? None. The package prohibits embedding information during inference, scores elementwise `ABSTAIN` as error, and keeps empty prediction distinct from abstention (`research_program/synthesis/op11_spherical_dual_target.md:213-245,263-301`). It makes no estimator, convergence or 3+1D recovery claim (`research_program/synthesis/op11_spherical_dual_target.md:328-338`; `research_program/work_packages/op13_positive_evidence_protocol.md:163-174,223-230`).
- Reasons:
  - Decision 030’s authorized source-status repair is present both adjacent to the formula and in the source list, retaining the coefficient as an explicitly unverified convention (`docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md:150-169`; `research_program/synthesis/op11_spherical_dual_target.md:25-37,340-345`).
  - The same-carrier dual is frozen with `iota_P=id`, involution and relabeling naturality (`research_program/synthesis/op11_spherical_dual_target.md:190-203`).
  - Every elementwise `ABSTAIN` remains an error in its class denominator, separate abstention rates are mandatory, and empty denominators fail closed (`research_program/synthesis/op11_spherical_dual_target.md:263-298`).
  - Audit of these exact hashes remains the next gate; this PASS authorizes no code, simulations, tests, seeds, commit, push or reconstruction claim (`docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md:132-148,163-169`).

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Kruskal relation, Eq. (3.9), `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2556-2562` | OP-1.1: `-UV=(r/(2M)-1)e^{r/(2M)}`; `UV` determines `r` and is preserved by `D=(-V,-U)` | CONFIRMED |
| Kruskal metric, Eq. (3.8), `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2555` | OP-1.1: exact combined coefficient `32M^3/r` | UNCONFIRMED |
| Kruskal volume, Appendix A, `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:3628-3663` | OP-1.1 marker: the snapshot prints `16M^3/r` in a two-dimensional presentation and does not state the cross-term convention resolving `16/32` | CONFIRMED |
| OP-1.1 formula marker and source entry, `research_program/synthesis/op11_spherical_dual_target.md:25-37,340-345` | Decision 030: retain `32` as declared convention while marking its exact local verification unavailable | CONFIRMED |
| Bombelli, Eq. (2.1.3), `biblioteca/derived-md/Bombelli_1987_PhD.md:402-407` | OP-1.1: order duality reverses arrows on the same underlying set | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:171-195` | Claim boundary: event horizons are global; longest-chain/future-cardinality diagnostics depend on singularity and patch boundary | CONFIRMED |
| Eichhorn–Gamito–Stokes, §IV, Eqs. (10)-(12), `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:197-225` | OP-1.1: trapped surfaces have negative future expansions and Schwarzschild has marginal locus `r=2M` | CONFIRMED |
| Eichhorn–Gamito–Stokes, conclusions, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:459-469` | Regular-BH caveat and ensemble requirement for ladder diagnostics | CONFIRMED |
| He–Rideout, sprinkling definition, `biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md:53-60` | OP-1.1/OP-1.2: volume-measure sprinkling, Poisson counts and continuum-induced causal order | CONFIRMED |
| Surya review, `biblioteca/derived-md/The causal set approach to quantum gravity.md:329-350,1001-1015,1052-1083,1092-1118,1150-1152,1221-1246` | OP-1.2 / mathematician: HKMM assumes a causal bijection; ordering fraction, `C_k` and longest chain are order invariants with ensemble-scoped continuum meaning | CONFIRMED |
| Janson; Hoeffding; Howard et al.; Ashtekar–Krishnan | Cited claims without local snapshots | UNVERIFIED |

- Notes: El marcador actual representa honestamente la evidencia: no afirma que `32` esté verificado, identifica el `16` impreso, explica que la convención cruzada no está declarada y repite el estado en fuentes (`research_program/synthesis/op11_spherical_dual_target.md:32-37,342-345`). La compatibilidad `16/32` sigue siendo plausible, no confirmada; la adopción no debe elevarla a hecho bibliográfico. **El bloqueo de fuente queda cerrado para `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`**, porque decisión 030 exigía transparencia de estado, no demostrar la constante (`docs/comite/comite_decision_030_phase1-theory-package-fourth-review.md:150-169`). `iota_P`, naturalidad y scoring de `ABSTAIN` son contratos internos, no hechos adjudicables por estas citas.

## 8. Synthesis

All seven roles support the scoped transition. Decision 030's single source-status correction is
present, earlier type and abstention blockers remain closed, the falsifier reports no load-bearing
failure, and the pre-registration warden returns `PASS` for documentary adoption only.

The three exact hashes are therefore adopted as:

```text
PHASE_1_THEORY_PACKAGE = THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING
```

This is not `PHASE_1_THEORY_READY`. It proves no estimator exists, no selector is chosen, no
convergence or recovery is established, no implementation is ready, and no scientific execution is
authorized. The Kruskal coefficient remains explicitly unverified by the local snapshot.

## 9. Next-step spec

**Scoped reversible step requiring PI sign-off:** run `/auditor` in strictly read-only mode on the
three exact hashes in section 1 plus decisions 027--031 and the Phase-1 plan/claim grammar. The audit
must verify:

1. exact SHA256 identity and documentary-only surface;
2. authorization provenance through decision 030 and this committee adoption;
3. closure of all blockers from decisions 027--030;
4. exact claim boundaries, open hypotheses and source-status markers;
5. that author terminals are not promoted to `PHASE_1_THEORY_READY` or recovery;
6. that no code, simulations, tests, seeds, commit or push are run.

The auditor should emit a new `docs/auditor/auditor_report_NNN_*` with a binary verdict. On
`AUDIT_PASS`, return to `/comite` for the Phase-1 closure/next-work decision; on `AUDIT_FAIL`, repair
only findings explicitly authorized by the PI and re-audit new hashes. Commit and push remain
unauthorized.

Minimal falsification check for the auditor:

```text
rg -n 'ds\^2 = -\(32 M\^3/r\)|UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT|iota_P = id|ABSTAIN.*cuenta como error' \
  research_program/synthesis/op11_spherical_dual_target.md
```

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_PROCEED_WITH_SCOPED_NEXT_STEP

## 11. User sign-off

Signed: Nacho / PI

Date: 2026-07-15

Decision: authorize the scoped strictly read-only audit in committee decision 031 section 9 on
the exact adopted hashes; do not run scientific code, simulations, tests, seeds, commit, or push;
return to committee after the binary audit verdict.
