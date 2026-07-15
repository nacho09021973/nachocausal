# Comite Decision 032 — Phase 1 theory closure handoff

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action, never tunes a frozen threshold post-hoc, and never makes a
> reconstruction claim. Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`,
> `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Does auditor report 015 (`AUDIT_PASS_WITH_WARNINGS`, zero errors and 22 legacy repo-wide warnings
outside the Phase-1 package) justify declaring `PHASE_1_THEORY_READY` and recommending an atomic
documentary commit/push, while OP-2.1 remains separately unauthorized?

## 2. Verified state

- The exact candidate hashes remain OP-1.1
  `6d024df0376d701b6c26c061d2c565942ebd3ab19a687f2c480551cae84f3024`, OP-1.2
  `0bfb9eeddc9ad14354956a99e522c1ca5b0ed05e7838d31be84c4fe63ac1663f`, and OP-1.3
  `60e874813c44ebe31bbed40cde507c18fe8e8e686447d76ca96452553d64fb1b`.
- Auditor report 015 has hash `4abd0bd0e40eb3d010d766cda7071303bc76790971943d6e8899868272ecaf00`,
  `AUDIT_ERRORS=0`, `AUDIT_WARNINGS=22`, and `AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS`
  (`docs/auditor/auditor_report_015_phase1-theory-package.md:124-141`).
- The three author terminals satisfy the conjunction written in
  `docs/plan_operativo_15_julio_2026.md:293-304`.
- Independent falsification found two citations in decision 031 that point to an ephemeral
  external dossier rather than a repository path
  (`docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md:86,95`).
- `rg` over decisions 027--031, audit 015 and OP-1.1--OP-1.3 found no other ephemeral external
  path citation.
- No scientific code, simulation, test, seed, commit or push was run.

Durability normalization: committee agents cited their temporary wave dossier while deliberating.
This brief replaces those citations in the pasted role text with the repo-local evidence they were
intended to reference; no substantive verdict or reasoning is changed.

## 3. Dossier

- `docs/plan_operativo_15_julio_2026.md`;
- `docs/auditor/auditor_report_015_phase1-theory-package.md`;
- `docs/comite/comite_decision_027_phase1-theory-package-first-review.md` through
  `docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md`;
- OP-1.1, OP-1.2 and OP-1.3 at the hashes in section 2;
- the local literature sources and explicit source-status markers audited in report 015.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): **PROCEED — declarar `PHASE_1_THEORY_READY` y recomendar un commit documental atómico antes de OP-2.1.** El gate exige `DUAL_FAMILY_CLOSED`, `TV_ZERO_CLASS_SCOPED_TO_CANDIDATE_FAMILY` y `POSITIVE_EVIDENCE_PROTOCOL_PROVED`, más revisión primaria, matemática, comité y auditor (`docs/plan_operativo_15_julio_2026.md:293-304`). Auditor 015 confirma esos terminales, hashes y límites con `AUDIT_ERRORS=0` (`docs/auditor/auditor_report_015_phase1-theory-package.md:124-141`).
- Environment & seal: Base `HEAD=origin/main=496985dbecd464a57267e607b7d3b48c323b510b`; los tres SHA256 auditados constan en el informe (`docs/auditor/auditor_report_015_phase1-theory-package.md:9-24`). El sello vivo coincide con prereg-002 y ningún test, simulación o validación científica fue ejecutado (`docs/auditor/auditor_report_015_phase1-theory-package.md:67-74`).
- Provenance capture: La superficie atómica propuesta contiene exactamente decisions 027--032, auditor report 015, OP-1.1, OP-1.2 y OP-1.3. Ningún código, dato, plan ya rastreado ni artefacto sellado debe entrar (`docs/auditor/auditor_report_015_phase1-theory-package.md:92-108`).
- Run mechanics: Tras firmar decision 032, verificar la lista staged contra esos diez paths, confirmar nuevamente los tres hashes, crear un único commit documental y hacer push de `main`. Solo después de push exitoso y worktree limpio puede abrirse OP-2.1; la Fase 2 depende del protocolo OP-1.3 probado (`docs/plan_operativo_15_julio_2026.md:308-320`). Esta recomendación no autoriza todavía ejecución científica.
- Reproducibility risks / ambiguities: Los 22 warnings son hallazgos heurísticos repo-wide sobre datos legacy, ajenos al paquete, con exit code 0; deben conservarse literalmente en auditor 015 y no reinterpretarse como cero warnings (`docs/auditor/auditor_report_015_phase1-theory-package.md:32-65,124-141`). Las fuentes primarias ausentes permanecen marcadas como no verificadas y los claims siguen acotados (`docs/auditor/auditor_report_015_phase1-theory-package.md:76-90,110-122`). No bloquean este gate documental, pero cualquier cambio posterior en hashes, terminales o marcadores exige nueva auditoría.

### Mathematician brief
- Computability: **PROCEED.** El gate del plan exige `DUAL_FAMILY_CLOSED`, una clasificación `TV=0` general o acotada, y `POSITIVE_EVIDENCE_PROTOCOL_PROVED` (`docs/plan_operativo_15_julio_2026.md:293-304`). Los tres terminales exactos están presentes (`research_program/synthesis/op11_spherical_dual_target.md:328-338`; `research_program/synthesis/op12_tv_zero_3p1.md:168-180`; `research_program/work_packages/op13_positive_evidence_protocol.md:223-230`), y auditor report 015 verificó sus hashes con `AUDIT_ERRORS=0` y `AUDIT_VERDICT=AUDIT_PASS_WITH_WARNINGS` (`docs/auditor/auditor_report_015_phase1-theory-package.md:9-24,124-141`).
- Order observable: OP-1.1 cierra únicamente la familia y el contrato de salidas order-only: dualización sobre el mismo portador, naturalidad bajo relabeling y outputs totales (`research_program/synthesis/op11_spherical_dual_target.md:190-245`). OP-1.3 prueba el esquema de cota inferior para cualquier testigo preespecificado `f:Omega->[0,1]`, separando leyes pretendidas/generadas y cobertura simultánea (`research_program/work_packages/op13_positive_evidence_protocol.md:12-80`). Ninguno demuestra que exista un localizador.
- Relevant invariants: La igualdad `fixed_n` en OP-1.2 sigue limitada a la órbita Schwarzschild coescalada con `lambda` y sector fijos; con `rho` conocida, la marginal Poisson distingue masas (`research_program/synthesis/op12_tv_zero_3p1.md:47-80,105-123`). OP-2.1 puede usar únicamente streams acotados y leyes sintéticas de TV conocida para validar cobertura, reproducibilidad, multiplicidad y abstención, sin consumir información geométrica (`docs/plan_operativo_15_julio_2026.md:313-336`).
- Analytic / continuum target: `DUAL_FAMILY_CLOSED` deriva de la involución temporal, medida positiva y reversión puntual del orden (`research_program/synthesis/op11_spherical_dual_target.md:88-108,190-211`). `TV_ZERO_CLASS_SCOPED_TO_CANDIDATE_FAMILY` deriva del acoplamiento medida-causal y coescalado `g->a^2g`, `mu->a^4mu` (`research_program/synthesis/op12_tv_zero_3p1.md:24-80`). `POSITIVE_EVIDENCE_PROTOCOL_PROVED` es un teorema estadístico condicional, no un certificado ejecutado (`research_program/work_packages/op13_positive_evidence_protocol.md:12-80,205-230`). Las 22 advertencias del auditor pertenecen a datos históricos fuera del paquete y no invalidan esos objetos; permanecen contabilizadas (`docs/auditor/auditor_report_015_phase1-theory-package.md:36-65,76-90`).
- Caveats: El conjunto de evidencias justifica `PHASE_1_THEORY_READY` al nivel documental definido por el plan. Antes de abrir trabajo de Fase 2 debe existir un commit durable que incluya decisions 027--031, los tres blobs exactos y auditor report 015; el propio audit registró esa superficie como Markdown aún no durable (`docs/auditor/auditor_report_015_phase1-theory-package.md:92-108`). Después, la única transición justificada es OP-2.1 con alcance genérico y autorización separada; no OP-2.2, preregistro ni corrida física (`docs/plan_operativo_15_julio_2026.md:308-347`). Permanecen abiertos el selector `R`, un testigo/localizador concreto, convergencia, variación de patch, geometrías no Schwarzschild, separación BH/WH orientada, generador certificado y cualquier claim de recovery (`research_program/synthesis/op11_spherical_dual_target.md:328-338`; `research_program/synthesis/op12_tv_zero_3p1.md:155-180`; `research_program/work_packages/op13_positive_evidence_protocol.md:122-174,223-230`).

### Mathematical logic brief
- Formal status: **PROCEED.** Report 015 satisfies the plan's `/auditor` prerequisite: the exact candidate hashes are bound in scope, all three author terminals are verified, and the audit has zero errors (`docs/auditor/auditor_report_015_phase1-theory-package.md:9-24,124-141`). Therefore the conjunction defining `PHASE_1_THEORY_READY` is satisfied at theory-document level (`docs/plan_operativo_15_julio_2026.md:293-304`).
- Quantifier / dependency order: The gate requires `DUAL_FAMILY_CLOSED`, either permitted TV-zero terminal, and `POSITIVE_EVIDENCE_PROTOCOL_PROVED`; the exact documents provide respectively `DUAL_FAMILY_CLOSED`, `TV_ZERO_CLASS_SCOPED_TO_CANDIDATE_FAMILY`, and `POSITIVE_EVIDENCE_PROTOCOL_PROVED` (`research_program/synthesis/op11_spherical_dual_target.md:328-338`; `research_program/synthesis/op12_tv_zero_3p1.md:168-181`; `research_program/work_packages/op13_positive_evidence_protocol.md:223-230`). Committee adoption preceded the authorized audit, so the dependency order is respected (`docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md:122-148,163-169`).
- Equivalence claims: `AUDIT_PASS_WITH_WARNINGS` is the auditor's canonical zero-error pass variant when warnings exist, not a failure or coerced clean pass (`.claude/skills/auditor/SKILL.md:27-31,69-75`). Decision 031's shorthand `AUDIT_PASS` branch is therefore satisfied semantically by report 015's `0 errors / 22 warnings`; the warnings remain recorded and concern older out-of-scope data, not the Phase-1 package (`docs/auditor/auditor_report_015_phase1-theory-package.md:59-65,89-90,136-141`).
- Type / object discipline: `PHASE_1_THEORY_READY` is a theory-gate terminal, not implementation readiness, estimator existence or recovery. OP-1.1 denies estimator, selector, convergence and 3+1D recovery; OP-1.3 leaves implementation pending a generator/witness specification (`research_program/synthesis/op11_spherical_dual_target.md:337-338`; `research_program/work_packages/op13_positive_evidence_protocol.md:205-230`). The audit independently found no reconstruction, executed recovery or implementation claim (`docs/auditor/auditor_report_015_phase1-theory-package.md:110-122`).
- Caveats: The 22 legacy warnings remain unresolved and cannot be restated as repo-wide cleanliness; they simply do not negate this exact package gate (`docs/auditor/auditor_report_015_phase1-theory-package.md:64-65,124-141`). An atomic documentary commit and push may be proposed next, but both remain unauthorized until a new explicit PI sign-off: decision 031 authorized only the read-only audit and expressly withheld commit/push (`docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md:145-148,161-169`).

### Physicist brief
- Coordinates & patch: **PROCEED — declarar el gate documental `PHASE_1_THEORY_READY`.** OP-1.1 fija únicamente Schwarzschild maximal esférico, patch finito con `S^2` completo, causalidad ambiente y clausura BH/WH bajo `D`; no identifica el horizonte de eventos de una continuación arbitraria (`research_program/synthesis/op11_spherical_dual_target.md:16-21,39-108`). Auditor 015 no encontró alteraciones de código, datos ni geometría sellada (`docs/auditor/auditor_report_015_phase1-theory-package.md:92-108`).
- Physical meaning of the signal: El resultado físico cerrado es un target continuo de trapping puntual en la familia congelada: localización en `r=2M`, lado dual-invariante y carácter BH/WH anti-invariante. No es todavía un observable causal-set construido (`research_program/synthesis/op11_spherical_dual_target.md:123-174,328-338`). Esto satisface `DUAL_FAMILY_CLOSED`, no una detección experimental.
- Sprinkling domain: OP-1.2 limita `TV=0` a sector y forma de patch fijos, separa `fixed_n` de Poisson con densidad conocida y deja abiertos patches variables, geometrías no esféricas y la recíproca general (`research_program/synthesis/op12_tv_zero_3p1.md:47-80,105-138,139-181`). OP-1.3 prueba solo el esquema estadístico condicional y deja generador/testigo concretos pendientes (`research_program/work_packages/op13_positive_evidence_protocol.md:163-174,223-230`). OP-2.1 debe requerir autorización separada; el gate teórico no autoriza sprinklings, simulaciones ni seeds.
- Claim boundary: Auditor 015 verificó los hashes exactos, `AUDIT_ERRORS=0`, ausencia de claim de reconstrucción/convergencia/recovery y conservación de los terminales acotados (`docs/auditor/auditor_report_015_phase1-theory-package.md:110-141`). Los 22 warnings pertenecen a datos legacy fuera del paquete y son físicamente no bloqueantes, aunque deben conservarse (`docs/auditor/auditor_report_015_phase1-theory-package.md:32-65,124-141`). Recomiendo commit/push documental atómico únicamente tras decision 032 y sign-off posterior del PI.
- Caveats: La normalización Kruskal exacta permanece explícitamente no verificada por el snapshot local, adyacente a la fórmula y repetida en fuentes (`research_program/synthesis/op11_spherical_dual_target.md:25-37,340-345`); `PHASE_1_THEORY_READY` no debe promocionarla a hecho bibliográfico. Siguen abiertos el reconstructor `H_hat`, selector `R(C)`, convergencia en densidad/tamaño de patch, recoverability individual, separación BH/WH orientada y extensión fuera de Schwarzschild esférico (`research_program/synthesis/op11_spherical_dual_target.md:328-338`; `research_program/synthesis/op12_tv_zero_3p1.md:139-181`). Estas aperturas delimitan Fase 2; no bloquean el gate documental de Fase 1.

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes: **BLOCK del handoff/commit atómico propuesto.** La conjunción de terminales del gate está presente (`docs/plan_operativo_15_julio_2026.md:293-304`), pero decision 031 contiene dos anclajes a un dossier temporal efímero, ausente de la superficie documental propuesta (`docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md:86,95`). Un commit durable con referencias no reproducibles contradice la captura de procedencia y el auditor no detectó este defecto pese a incluir decisions 027--031 en alcance (`docs/auditor/auditor_report_015_phase1-theory-package.md:21-24,124-134`).
- Ground-truth leakage: No encuentro fuga nueva. Auditor 015 confirmó separación de scoring, dualidad combinatoria y prohibición de embedding en selección/inferencia (`docs/auditor/auditor_report_015_phase1-theory-package.md:92-108`).
- Freeze violations: No hubo ejecución científica ni consumo de seeds (`docs/auditor/auditor_report_015_phase1-theory-package.md:67-74`). Sin embargo, reparar decision 031 después del audit cambia un documento incluido en su alcance exacto; no puede editarse silenciosamente antes del commit. Debe autorizarse el reemplazo mínimo de ambos anclajes por referencias repo-locales y repetir la auditoría documental sobre la nueva superficie.
- Verdict coercion: Los 22 warnings no bloquean por sí mismos: `AUDIT_PASS_WITH_WARNINGS` corresponde a cero errores y uno o más warnings (`.claude/skills/auditor/SKILL.md:74-75`). Pero deben conservarse como 22 warnings legacy, nunca resumirse como "repo limpio" (`docs/auditor/auditor_report_015_phase1-theory-package.md:59-65,124-141`). El bloqueo encontrado es independiente de ellos.
- Premature / over-broad claims: `PHASE_1_THEORY_READY` solo puede significar cierre del gate teórico. OP-1.1 sigue negando estimador, selector, convergencia y recovery, mientras OP-1.3 mantiene implementación pendiente (`research_program/synthesis/op11_spherical_dual_target.md:328-338`; `research_program/work_packages/op13_positive_evidence_protocol.md:223-230`). OP-2.1 continúa requiriendo autorización separada (`docs/plan_operativo_15_julio_2026.md:308-322`).
- Independent-falsification gate: **NOT SATISFIED para commit/push ni handoff durable.** Los hashes científicos y terminales pasan, y los warnings son no bloqueantes; falla la portabilidad de procedencia del paquete exacto. Reemplazo mínimo recomendado: en decision 031, sustituir los dos anclajes efímeros por sus equivalentes internos de secciones 1-2 y 8-9, recalcular cualquier hash afectado y reauditar antes de decision final, commit o push.
- Minimal falsification test: buscar citas a directorios temporales en `docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md` devuelve los anclajes efímeros en líneas 86 y 95; el gate durable exige salida vacía antes de staging.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: PASS
- Freeze status: `PHASE_1_THEORY_READY` may be declared for the exact audited theory package: the required three terminals and review gates are satisfied (`docs/plan_operativo_15_julio_2026.md:293-304`; `docs/auditor/auditor_report_015_phase1-theory-package.md:124-141`). This freezes no witness, generator, numerical threshold or confirmatory grid; OP-1.3 leaves those to a future specification (`research_program/work_packages/op13_positive_evidence_protocol.md:223-230`).
- Seal integrity: Auditor 015 verified the live prereg-002 seal as `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`; the Phase-1 surface is documentary and does not alter the sealed estimator (`docs/auditor/auditor_report_015_phase1-theory-package.md:67-74,92-108`). The proposed atomic commit must contain exactly decisions 027--032, auditor report 015 and OP-1.1 through OP-1.3, with no code, data, tracked plan or sealed artifact (`docs/auditor/auditor_report_015_phase1-theory-package.md:92-108`).
- Seed discipline: No development, validation or reserved seed is consumed. OP-2.1 remains unauthorized; opening it requires a separate scoped decision despite Phase 2 depending on the proved OP-1.3 protocol (`docs/plan_operativo_15_julio_2026.md:308-336`).
- Reporting rule: Publish `PHASE_1_THEORY_READY` only as the documentary theory gate. Preserve `AUDIT_ERRORS=0`, `AUDIT_WARNINGS=22` and `AUDIT_PASS_WITH_WARNINGS` literally; do not rewrite the result as a warning-free audit (`docs/auditor/auditor_report_015_phase1-theory-package.md:124-141`). The status implies neither implementation readiness nor recovery (`docs/auditor/auditor_report_015_phase1-theory-package.md:110-122`).
- Forbidden moves present? None in the proposed transition. Commit and push remain forbidden until decision 032 receives explicit PI sign-off; decision 031 authorized only the audit and expressly withheld both actions (`docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md:145-148,161-169`). OP-2.1 scientific work, tests, simulations and seeds remain outside this authorization.
- Reasons:
  - The three exact hashes and all earlier blockers were verified with zero audit errors (`docs/auditor/auditor_report_015_phase1-theory-package.md:9-24,124-141`).
  - The 22 warnings concern older repo-wide data outside the package and remain counted; they do not invalidate this documentary gate (`docs/auditor/auditor_report_015_phase1-theory-package.md:59-65,89-90`).
  - The exact atomic surface is decisions 027--032, auditor report 015 and OP-1.1 through OP-1.3; any additional path or changed candidate hash requires renewed review/audit (`docs/auditor/auditor_report_015_phase1-theory-package.md:92-108`).
  - OP-1.1 denies estimator, selector, convergence and recovery, while OP-1.3 keeps implementation pending a concrete generator/witness spec (`research_program/synthesis/op11_spherical_dual_target.md:328-338`; `research_program/work_packages/op13_positive_evidence_protocol.md:223-230`).

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Kruskal relation, `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2556-2562` | OP-1.1: `UV` determines `r` and is preserved by `D=(-V,-U)` | CONFIRMED |
| Exact combined Kruskal coefficient `32M^3/r`, compared with `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2555,3628-3663` | OP-1.1 metric convention | UNCONFIRMED |
| Explicit normalization marker, `research_program/synthesis/op11_spherical_dual_target.md:340-345` | OP-1.1: the local snapshot does not literally verify `32M^3/r` | CONFIRMED |
| Bombelli, Eq. (2.1.3), `biblioteca/derived-md/Bombelli_1987_PhD.md:402-407` | Same-carrier order duality and arrow reversal | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III–IV, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:171-230,459-469` | Global event-horizon caveat, boundary dependence, null expansions and Schwarzschild marginal locus `r=2M` | CONFIRMED |
| He–Rideout, `biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md:53-60` | Volume-measure sprinkling, Poisson count and continuum-induced causal order | CONFIRMED |
| Surya review, `biblioteca/derived-md/The causal set approach to quantum gravity.md:329-350,1001-1015,1052-1083,1092-1118,1150-1152,1221-1246` | HKMM scope and ensemble-qualified order invariants | CONFIRMED |
| Ashtekar–Krishnan; HKM/Malament primaries; Janson; Hoeffding; Howard et al. | References lacking local primary snapshots | UNVERIFIED |
| Auditor report 015 source-status check, `docs/auditor/auditor_report_015_phase1-theory-package.md:76-90,110-122` | Missing and unconfirmed sources remain marked rather than promoted | CONFIRMED |

- Notes: Auditor report 015 preserves every material source limitation and explicitly records that no executed certificate or empirical result is being cited (`docs/auditor/auditor_report_015_phase1-theory-package.md:76-90`). The unavailable Janson converse is not used; OP-1.2 explicitly declines that converse (`research_program/synthesis/op12_tv_zero_3p1.md:24-45,155-166`). Hoeffding supports a theorem derived in-text, while Howard is reserved for a forbidden future sequential extension (`research_program/work_packages/op13_positive_evidence_protocol.md:24-80,141-151,232-240`). Therefore no citation blocker prevents `PHASE_1_THEORY_READY` or an atomic documentary commit of the exact audited package. The commit must retain `UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT` and all other markers verbatim; it cannot present `32` or absent primaries as verified. The 22 audit warnings concern legacy data outside this package and are not literature findings (`docs/auditor/auditor_report_015_phase1-theory-package.md:124-141`).

## 8. Synthesis

The theory-gate conjunction is substantively satisfied: all four wave-1 roles, the pre-registration
warden and literature verifier agree that the three author terminals plus the zero-error audit
support `PHASE_1_THEORY_READY` as a documentary status. The 22 warnings are preserved and do not
belong to this package.

However, the falsifier found a portability defect in decision 031 that auditor report 015 missed:
two role-brief citations point to an ephemeral external dossier. Because decision 031 was inside the
audited surface, editing those citations changes an audited blob. The committee cannot recommend
commit/push on the current package and cannot silently treat report 015 as auditing the corrected
document.

The scientific hashes and author terminals remain valid and must not change. The closure status is:

```text
PHASE_1_THEORY_READY = SUBSTANTIVELY_SATISFIED_PROVENANCE_REAUDIT_PENDING
```

## 9. Next-step spec

**Reversible documentary repair requiring PI sign-off:** perform only the following:

1. in decision 031 lines 86 and 95, replace the two ephemeral dossier citations with repo-local
   anchors to decision 031 sections 1--2 and 8--9 plus auditor report 015 section 1 as appropriate;
2. do not change any candidate, terminal, verdict, warning count, scientific statement or source
   status;
3. recompute decision 031's hash and run a new strictly read-only scoped audit over decisions
   027--032, audit 015, OP-1.1--OP-1.3 and the unchanged three scientific hashes;
4. the new auditor must explicitly check that no durable document relies on an external temporary
   path and must emit report 016 with a binary verdict;
5. return to `/comite` after that verdict. Commit, push and OP-2.1 remain unauthorized.

Minimal falsification check after repair:

```text
rg -n '/t[m]p/' \
  docs/comite/comite_decision_031_phase1-theory-package-audit-gate.md
```

The command must return no matches. No scientific code, simulation, test or seed may run.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

Signed: Nacho / PI

Date: 2026-07-15

Decision: authorize only the two repo-local citation replacements in committee decision 032
section 9, record this sign-off, run the new strictly read-only scoped audit as report 016, and
return to committee after its binary verdict; do not change the three scientific hashes or run
scientific code, simulations, tests, seeds, commit, or push.
