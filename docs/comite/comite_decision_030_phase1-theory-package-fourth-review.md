# Comite Decision 030 — Phase 1 theory package fourth review

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action, never tunes a frozen threshold post-hoc, and never makes a
> reconstruction claim. Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`,
> `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Do exact blobs OP-1.1 `7ce617c1d72d12296124fc7f1d82eac29ac5db108f3b61eb4dcda42954d0910b`,
OP-1.2 `c9a8d1346ff237d3a96ad92d063ed14062caeafb18aa1c7f8251256fcff8372b`, and OP-1.3
`570b9bc67aedeb42c9e6b56bb5c3c9eca47a8d16616d758bb97745d792d80757` close decision 029
section 9 and qualify as `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`?

## 2. Verified state

- `HEAD=origin/main=496985dbecd464a57267e607b7d3b48c323b510b` when checked by the chair.
- Decision 029 records the PI authorization at
  `docs/comite/comite_decision_029_phase1-theory-package-third-review.md:201-209`.
- `sha256sum` returned the three hashes in section 1 and decision-029 hash
  `634d6404af5700989528904f4353500f39f5b40ad1188f1430dc89d53870451b`.
- The three static falsification checks in decision 029 for `iota_P=id`, element-wise `ABSTAIN`
  counted as error, and joint reporting of `A_side`/`A_trapping` returned exit code 0.
- Static whitespace checks emitted no errors.
- The displayed Kruskal coefficient is at
  `research_program/synthesis/op11_spherical_dual_target.md:24-29`; `rg` finds no adjacent or
  source-list marker that identifies that exact normalization as `UNVERIFIED` or `UNCONFIRMED`
  (`research_program/synthesis/op11_spherical_dual_target.md:332-340`).
- No `/auditor`, code, simulation, test, commit or push was run. Seal and executable environment
  remain `[UNVERIFIED_THIS_SESSION]` and are not used for this documentary verdict.

## 3. Dossier

- `research_program/synthesis/op11_spherical_dual_target.md`;
- `research_program/synthesis/op12_tv_zero_3p1.md`;
- `research_program/work_packages/op13_positive_evidence_protocol.md`;
- `docs/comite/comite_decision_029_phase1-theory-package-third-review.md`;
- `docs/claim_grammar.md`;
- `docs/plan_operativo_15_julio_2026.md`;
- `biblioteca/derived-md/Bombelli_1987_PhD.md`;
- `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md`;
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`;
- `biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md`;
- `biblioteca/derived-md/The causal set approach to quantum gravity.md`.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): No adoptar todavía los tres blobs como `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`. Las dos correcciones principales de OP-1.1 sí están materializadas: `iota_P=id` y naturalidad (`research_program/synthesis/op11_spherical_dual_target.md:185-195`), y scoring fail-closed de `ABSTAIN` con tasas separadas (`research_program/synthesis/op11_spherical_dual_target.md:255-275`). Sin embargo, sigue abierta una condición explícita de decision 029 §9.
- Environment & seal: Paquete propuesto: OP11 `7ce617c1d72d12296124fc7f1d82eac29ac5db108f3b61eb4dcda42954d0910b`, OP12 `c9a8d1346ff237d3a96ad92d063ed14062caeafb18aa1c7f8251256fcff8372b`, OP13 `570b9bc67aedeb42c9e6b56bb5c3c9eca47a8d16616d758bb97745d792d80757`, sobre HEAD `496985d` `[UNVERIFIED_THIS_ROLE: hashes y HEAD suministrados por chair]`. Al ser artefactos teóricos Markdown, el sello reproducible es base commit más hashes exactos; no existe entorno de ejecución autorizado (`research_program/work_packages/op13_positive_evidence_protocol.md:1-9`).
- Provenance capture: Los tres documentos registran decisiones 027-029 y sign-off del PI (`research_program/synthesis/op11_spherical_dual_target.md:9-13`, `research_program/synthesis/op12_tv_zero_3p1.md:5-9`, `research_program/work_packages/op13_positive_evidence_protocol.md:5-9`). Decision 029 exige además confirmar que la normalización métrica exacta esté honestamente respaldada o marcada como no verificada (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:194-195`). OP-1.1 muestra el coeficiente `32 M^3/r` (`research_program/synthesis/op11_spherical_dual_target.md:24-29`), pero su sección de fuentes no marca explícitamente esa normalización como no verificada ni aporta una verificación primaria identificable (`research_program/synthesis/op11_spherical_dual_target.md:332-340`).
- Run mechanics: No procede auditor, código, simulación, tests, seeds, commit ni push. La mecánica reproducible inmediata es obtener autorización para corregir únicamente el estado de fuente de la normalización, recalcular el hash de OP11 y reconvocar comité sobre los tres blobs exactos, conforme al patrón de decision 029 (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:181-195`). El paquete mantiene correctamente `NO_RECOVERY_RESULT` (`research_program/synthesis/op11_spherical_dual_target.md:3-20,329-330`) y `NO_EXECUTION_AUTHORIZED` (`research_program/work_packages/op13_positive_evidence_protocol.md:3,222-229`).
- Reproducibility risks / ambiguities: Riesgo bloqueante: la ausencia del marcador explícito permite que lectores distintos interpreten la constante métrica como verificada o meramente convencional, incumpliendo el cierre fail-closed exigido por decision 029. Persisten además fuentes declaradas no verificadas en OP11, OP12 y OP13 (`research_program/synthesis/op11_spherical_dual_target.md:334-339`, `research_program/synthesis/op12_tv_zero_3p1.md:182-191`, `research_program/work_packages/op13_positive_evidence_protocol.md:231-236`), pero estas son transparentes y no bloquean por sí solas la adopción tras corregir el punto anterior.

### Mathematician brief
- Computability: En cada representante finito `P=(S(P),prec_P)`, OP-1.1 define ahora `P^op` sobre el mismo portador, `iota_P=id`, su ley involutiva y naturalidad bajo cualquier relabeling (`research_program/synthesis/op11_spherical_dual_target.md:182-195`). Esto elimina la elección no canónica anterior y coincide con la definición estándar del dual como el mismo conjunto con flechas invertidas (Bombelli, Eq. 2.1.3, `biblioteca/derived-md/Bombelli_1987_PhD.md:402-407`). Las acciones sobre subconjuntos, etiquetas y abstención quedan así totalmente computables y bien tipadas (`research_program/synthesis/op11_spherical_dual_target.md:205-234`).
- Order observable: El contrato sigue siendo estrictamente order-only: las salidas se construyen sobre el representante y son naturales/equivariantes bajo relabeling, mientras coordenadas, `r`, expansiones y etiquetas continuas solo aparecen en scoring (`research_program/synthesis/op11_spherical_dual_target.md:191-237`). No se define todavía un localizador concreto. OP-1.3 únicamente prueba para un testigo congelado `f:Omega->[0,1]` la cota `TV(P,Q)>=|E_Pf-E_Qf|`, y mantiene `TARGET_WITNESS_MISMATCH` cuando separación no implica localización (`research_program/work_packages/op13_positive_evidence_protocol.md:11-33,162-173`).
- Relevant invariants: Dualidad, cardinalidad, ordering fraction, abundancias `C_k` y altura son invariantes finitos order-only; sus interpretaciones geométricas permanecen ensemble-scoped (`biblioteca/derived-md/The causal set approach to quantum gravity.md:1001-1015,1054-1082,1092-1118,1151-1152,1221-1246`). Las pérdidas puntuales ya son funciones totales de las predicciones y del scoring ground truth: cada `ABSTAIN` cuenta como error, permanece en el denominador de su clase, y se reportan separadamente `A_side` y `A_trapping` (`research_program/synthesis/op11_spherical_dual_target.md:239-275`). Una clase o denominador vacío produce `LOSS_UNSCORABLE`; por tanto no existe vía de mejorar la pérdida absteniéndose o eliminando clases difíciles (`research_program/synthesis/op11_spherical_dual_target.md:266-275,295-318`).
- Analytic / continuum target: La identificación `iota_P=id` es compatible con la ley generativa `Law_K(Dg)=d_#Law_K(g)` porque la primera relaciona elementos del mismo representante discreto, mientras `D` acopla puntos de los dos modelos y revierte el orden mediante la convención temporal congelada (`research_program/synthesis/op11_spherical_dual_target.md:80-100,168-203`). Los targets `h_M`, `c_g` y `Chi` permanecen separados y transforman con la paridad dual correcta (`research_program/synthesis/op11_spherical_dual_target.md:123-166`). OP-1.2 conserva sin cambios su lema de acoplamiento módulo nulos, la degeneración `fixed_n` en la órbita coescalada y la separación Poisson con `rho` conocida (`research_program/synthesis/op12_tv_zero_3p1.md:23-79,81-122`). OP-1.3 conserva el certificado Hoeffding condicional sobre leyes generadas tipadas separadamente y errores TV deterministas (`research_program/work_packages/op13_positive_evidence_protocol.md:35-80`).
- Caveats: **Recomendación: `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** Las dos correcciones autorizadas en decisión 029 §9 están incorporadas literalmente y cierran los defectos de tipo/scoring anteriores (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:171-195`; `research_program/synthesis/op11_spherical_dual_target.md:182-195,255-275`). No detecto otro bloqueo matemático antes de auditoría. La normalización exacta del coeficiente Kruskal sigue sin estar verificada por la fuente local y no debe promocionarse bibliográficamente; no afecta a la involución discreta ni a los argumentos de causalidad conforme y escalado empleados aquí (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:123-144`). La ausencia de testigo, generador y pérdidas numéricamente congeladas sigue bloqueando implementación y recovery, no la adopción del esquema documental (`research_program/synthesis/op11_spherical_dual_target.md:322-330`; `research_program/work_packages/op13_positive_evidence_protocol.md:222-228`).

### Mathematical logic brief
- Formal status: OP-1.1 now contains total definitions of the dual model, representative duality, support identification, output involutions, scoring losses and terminal order; `DUAL_FAMILY_CLOSED` is a documentary theorem following from those definitions, not an estimator-existence or recovery theorem (`research_program/synthesis/op11_spherical_dual_target.md:68-100`, `:168-203`, `:205-293`, `:320-330`). OP-1.2 proves a one-way coupling lemma, fixed-`n` equality on the scoped co-scaled mass orbit and a known-`rho` Poisson iff; its general converse and asymptotic claims remain open (`research_program/synthesis/op12_tv_zero_3p1.md:23-79`, `:104-122`, `:139-180`). OP-1.3 proves only a conditional fixed-sample certificate schema; concrete generators, witnesses and scientific runs remain unauthorized (`research_program/work_packages/op13_positive_evidence_protocol.md:11-80`, `:140-160`, `:222-228`).
- Quantifier / dependency order: OP-1.1 fixes patch, temporal orientation, positive measure and ambient causal relation before the observed channels and law pushforward (`research_program/synthesis/op11_spherical_dual_target.md:31-100`, `:168-203`). For every concrete representative it then defines `P^op` on the same carrier and `iota_P=id` before using either in output equations (`research_program/synthesis/op11_spherical_dual_target.md:182-203`, `:205-234`). OP-1.2 places the `mu_g tensor mu_g` almost-everywhere quantifier before finite-sample coupling, fixes sector and `lambda` before varying mass, and restricts only `ell_eff` to `n>=1` while retaining the law theorem for all `n>=0` (`research_program/synthesis/op12_tv_zero_3p1.md:23-44`, `:46-79`, `:81-102`). OP-1.3 freezes laws, witness, iid sample sizes, multiplicity and deterministic generator-error bounds before confirmation and keeps adaptive development provenance separate (`research_program/work_packages/op13_positive_evidence_protocol.md:35-77`, `:82-107`, `:121-138`).
- Equivalence claims: The identities `T^-=-D_*T^+` and `x prec^+ y iff D(y) prec^- D(x)` now supply the exact hypotheses used by `Law_K(Dg)=d_#Law_K(g)` (`research_program/synthesis/op11_spherical_dual_target.md:80-100`, `:168-203`). Representative duality is an involution because it reverses the relation on the unchanged carrier; `iota_{P^op} o iota_P=id` follows from both maps being identities, and the stated naturality square is well-typed for every relabeling isomorphism (`research_program/synthesis/op11_spherical_dual_target.md:182-195`). OP-1.2 correctly uses only the forward measure-causal implication, scopes fixed-`n` equality to fixed sector/`lambda`, and scopes `TV=0 iff M=M'` to fixed known `rho>0` (`research_program/synthesis/op12_tv_zero_3p1.md:23-44`, `:46-79`, `:104-122`). OP-1.3's Hoeffding and union-bound calculation plus deterministic tilde-to-intended TV transport supports the stated simultaneous lower bound (`research_program/work_packages/op13_positive_evidence_protocol.md:35-77`).
- Type / object discipline: Decision 029's remaining defects are closed. `iota_P` is no longer free: its carrier, value, involution law and relabeling naturality are explicit, without embedding correspondence (`research_program/synthesis/op11_spherical_dual_target.md:182-203`). `nu` and the lifted set action are total; `H_hat=empty` is a scored set prediction while `H_hat=ABSTAIN` is a separate sum value (`research_program/synthesis/op11_spherical_dual_target.md:205-234`, `:277-290`). Element-wise `ABSTAIN` is now counted as error, retained in each class denominator and reported separately through `A_side` and `A_trapping`; empty denominators emit `LOSS_UNSCORABLE` (`research_program/synthesis/op11_spherical_dual_target.md:239-275`). OP-1.1 and OP-1.3 retain deterministic total terminal precedence (`research_program/synthesis/op11_spherical_dual_target.md:295-318`; `research_program/work_packages/op13_positive_evidence_protocol.md:175-228`).
- Caveats:
  - **Recommendation: `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** The exact OP-1.1 blob closes both corrections authorized by decision 029 §9, and the current OP-1.2/OP-1.3 contents preserve their scoped and conditional claims. None licenses recovery, implementation or execution (`research_program/synthesis/op11_spherical_dual_target.md:320-330`; `research_program/synthesis/op12_tv_zero_3p1.md:167-180`; `research_program/work_packages/op13_positive_evidence_protocol.md:203-228`).
  - Final `PHASE_1_THEORY_READY` still requires audit of these exact hashes; committee adoption is only the pending-audit state (`docs/plan_operativo_15_julio_2026.md:293-304`).
  - The assertion that OP-1.2 and OP-1.3 changed only in provenance cannot be reconstructed byte-for-byte from current untracked blobs alone `[UNVERIFIED]`. Their full current mathematical contents were reviewed here, so the recommendation applies to the exact present hashes rather than relying on that delta claim.
  - The exact Kruskal metric normalization and absent primary snapshots remain literature-verification matters, not logical consequences proved by these drafts; their unavailable sources remain explicitly marked `[UNVERIFIED_*]` (`research_program/synthesis/op11_spherical_dual_target.md:332-340`; `research_program/synthesis/op12_tv_zero_3p1.md:182-192`; `research_program/work_packages/op13_positive_evidence_protocol.md:231-239`).
  - Decision 029 authorizes only the two documentary corrections, provenance-line updates and reconvening; auditor, code, simulations, tests, commit and push remain unauthorized until a proceed decision (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:171-209`).

### Physicist brief
- Coordinates & patch: La relación `-UV=(r/2M-1)e^{r/2M}`, el patch con `S^2` completo y la involución `D(U,V,omega)=(-V,-U,omega)` describen coherentemente los sectores `I∪II` y `I∪IV`; `D` conserva `UV`, `r` y el locus `r=2M` (`research_program/synthesis/op11_spherical_dual_target.md:24-66`). Con la convención estándar de línea de elemento, la transformación desde coordenadas nulas de Schwarzschild produce `-(32M^3/r)e^{-r/2M}dU dV`.
- Physical meaning of the signal: El target es la frontera puntual donde cambia el signo de la expansión nula exterior; en Schwarzschild, `Theta_in<0` y `Theta_out=(1/r)(1-2M/r)`, por lo que el locus marginal es `r=2M` (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:197-225`). La dualidad conserva localización y lado, pero invierte trapping y carácter BH/WH (`research_program/synthesis/op11_spherical_dual_target.md:123-166`). Definir `P^op` sobre el mismo portador solamente formaliza la inversión temporal causal estándar (`biblioteca/derived-md/Bombelli_1987_PhD.md:402-407`); las nuevas reglas de `ABSTAIN` modifican únicamente scoring y denominadores (`research_program/synthesis/op11_spherical_dual_target.md:255-275`), no el target físico.
- Sprinkling domain: El experimento usa la medida positiva de volumen y la causalidad ambiente de Schwarzschild maximal restringida a pares del patch, no causalidad interna al patch (`research_program/synthesis/op11_spherical_dual_target.md:68-100`). Los canales `fixed_n` y Poisson order+number están separados (`research_program/synthesis/op11_spherical_dual_target.md:168-180`). La fuente local confirma la construcción general de sprinkling por medida de volumen y relaciones causales (`biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md:53-60`).
- Claim boundary: Las revisiones de mismo portador y `ABSTAIN` cierran materialmente las dos correcciones enumeradas en decision 029 (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:153-162,173-179`) y no introducen recovery, convergencia ni reconstructor (`research_program/synthesis/op11_spherical_dual_target.md:320-330`). No obstante, los blobs exactos todavía no satisfacen completamente la condición adicional de decision 029 §9 sobre la normalización métrica (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:194-195`); por ello no recomiendo aún `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.
- Caveats: La fuente local imprime `16M^3/r` y trata explícitamente el sector bidimensional (`biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562,3628-3633`), así que no respalda literalmente la fórmula 3+1 con coeficiente 32. La discrepancia puede ser convencional: para `ds^2=-32A dU dV`, los componentes son `g_{UV}=g_{VU}=-16A` y la densidad radial de volumen es `16A`, coincidente con el factor usado en el apéndice (`biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:3633-3663`). Pero la fuente no declara esa convención `[UNVERIFIED]`. OP-1.1 muestra 32 (`research_program/synthesis/op11_spherical_dual_target.md:24-29`) sin derivación, fuente literal ni marcador específico `UNVERIFIED`; sus marcadores actuales se aplican a otras referencias (`research_program/synthesis/op11_spherical_dual_target.md:332-340`). Hace falta marcar explícitamente la normalización como no verificada o añadir la derivación y convención antes de adopción.

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes: Las dos correcciones centrales pasan la reinspección: `iota_P=id`, involución y naturalidad están definidas (`research_program/synthesis/op11_spherical_dual_target.md:182-203`), y todo `ABSTAIN` puntual cuenta como error, permanece en denominador y tiene tasas separadas (`research_program/synthesis/op11_spherical_dual_target.md:255-275`). Pero decision 029 impuso además confirmar que la normalización Kruskal estuviera respaldada o marcada como no verificada (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:194-195`). OP-1.1 muestra `32M^3/r` sin marcador específico ni derivación (`research_program/synthesis/op11_spherical_dual_target.md:24-29,332-340`). La fuente local imprime 16 y es explícitamente bidimensional (`biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562,3628-3633`). Aunque una convención de términos cruzados puede explicar el factor dos, el apéndice solo lo sugiere mediante su densidad de volumen 16 (`biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:3633-3663`); no declara la convención. Por tanto el cuarto requisito semántico de §9 sigue abierto y bloquea la adopción de estos hashes.
- Ground-truth leakage: No encuentro una fuga introducida por las revisiones. Coordenadas, `r`, `M`, expansiones y etiquetas quedan prohibidas para construcción, selección, orientación y abstención (`research_program/synthesis/op11_spherical_dual_target.md:227-237`); `h_M`, `c_g` y la banda `B_H` se usan solo en scoring (`research_program/synthesis/op11_spherical_dual_target.md:239-281`). La identificación por mismo portador es combinatoria y natural bajo relabeling, no una correspondencia de embedding (`research_program/synthesis/op11_spherical_dual_target.md:182-203`).
- Freeze violations: No se han ejecutado runs ni consumido seeds `[UNVERIFIED: estado suministrado por chair]`. Sin embargo, aceptar los hashes actuales y relegar el marcador ausente al auditor alteraría el gate congelado de decision 029: esa decisión ordena reconvocar comité después de cerrar sus condiciones y prohíbe auditor/código/simulaciones/tests hasta un proceed verdict (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:181-195`). La corrección documental exige nuevo hash de OP11 y otra adjudicación exacta; no puede incorporarse silenciosamente durante auditoría.
- Verdict coercion: La revisión elimina la vía de abstenerse para mejorar artificialmente `L_side` o `L_trapping`: abstención equivale a error y se informa aparte (`research_program/synthesis/op11_spherical_dual_target.md:255-275`). `H_hat=empty` se puntúa, `H_hat=ABSTAIN` emite terminal separado y `A_H` se reporta (`research_program/synthesis/op11_spherical_dual_target.md:217-225,277-290`). Los denominadores vacíos producen `LOSS_UNSCORABLE`, no PASS/FAIL (`research_program/synthesis/op11_spherical_dual_target.md:274-275,295-318`). No detecto coerción de resultado en las correcciones.
- Premature / over-broad claims: El terminal se limita correctamente a clausura dual documental y niega existencia de estimador, selector, convergencia y recovery 3+1D (`research_program/synthesis/op11_spherical_dual_target.md:320-330`). El sobrealcance residual es de procedencia física: presentar una normalización exacta 3+1 sin derivación ni estado explícito, cuando el único anclaje local inspeccionado muestra una expresión 2D con factor 16. Su corrección física probable no sustituye la trazabilidad exigida.
- Independent-falsification gate: No está satisfecho para adopción. Existe revisión multirrol, por lo que el autor no es el único verificador, pero los tres checks del chair cubren únicamente `iota_P` y `ABSTAIN`; decision 029 incluye una condición adicional no capturada por ellos (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:186-195`). Veredicto falsificador: `BLOCK / REVISE_AND_RECONVENE`, con cambio mínimo de estado de fuente o derivación explícita y recálculo del hash OP11.
- Minimal falsification test: `rg -n '(32 M\^3/r).*(UNVERIFIED|UNCONFIRMED)|(UNVERIFIED|UNCONFIRMED).*(32 M\^3/r|coeficiente Kruskal|normalizaci[oó]n)' research_program/synthesis/op11_spherical_dual_target.md` debe encontrar el marcador o derivación de estado junto a la normalización; en el blob inspeccionado no encuentra ninguno, exponiendo el incumplimiento de decision 029 §9 (`research_program/synthesis/op11_spherical_dual_target.md:24-29,332-340`).

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: BLOCK
- Freeze status: No numerical threshold, concrete witness, generator, seed band or confirmatory grid is frozen by these theory drafts. OP-1.1 leaves numerical loss choices for a later pre-inference freeze (`research_program/synthesis/op11_spherical_dual_target.md:239-253`), and OP-1.3 requires the complete laws, witness hash, sample sizes, alpha budget, deterministic generator-error bounds and manifest before confirmation (`research_program/work_packages/op13_positive_evidence_protocol.md:35-77`, `:121-138`). The exact package must not be hash-adopted while the source status of its displayed metric normalization remains ambiguous.
- Seal integrity: No sealed path was run or modified. The live `nachocausal/thresholds.py` SHA256 remains `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching the operative prereg-002 seal (`docs/preregistration_002.md:7-12`). OP-1.1 remains `NO_IMPLEMENTATION / NO_RECOVERY_RESULT`, and OP-1.3 remains `NO_EXECUTION_AUTHORIZED` (`research_program/synthesis/op11_spherical_dual_target.md:1-20`; `research_program/work_packages/op13_positive_evidence_protocol.md:1-9`).
- Seed discipline: No development, validation or reserved seed is consumed. OP-1.3 correctly requires development/confirmation separation, complete search provenance, disjoint seed derivation and a complete manifest before any confirmatory seed is used (`research_program/work_packages/op13_positive_evidence_protocol.md:82-107`, `:133-138`).
- Reporting rule: Report `BLOCK / SOURCE_STATUS_INCOMPLETE`; do not record `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING` or combine the author terminals into `PHASE_1_THEORY_READY`. Decision 029 forbids `/auditor` until a reconvened committee returns a proceed verdict (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:171-195`). Audit is therefore not the next authorized step.
- Forbidden moves present? No post-hoc tuning, threshold loosening, seed reuse, validation rerun, ground-truth leakage, reconstruction claim, code execution, test, commit or push occurred. Adopting the current hashes would nevertheless violate the anchoring mandate by freezing an exact formula whose verification status is not declared.
- Reasons:
  - The `iota_P` blocker is closed: `P^op` uses the same carrier, `iota_P=id`, the involution law is explicit and naturality under relabeling is frozen without embedding correspondence (`research_program/synthesis/op11_spherical_dual_target.md:182-203`).
  - The element-wise abstention blocker is closed: every `ABSTAIN` counts as error, remains in its class denominator, and `A_side` plus `A_trapping` are reported separately; empty denominators emit `LOSS_UNSCORABLE` (`research_program/synthesis/op11_spherical_dual_target.md:255-275`).
  - Decision 029 imposed an additional explicit condition: the exact metric normalization had to be honestly sourced or marked unverified before committee adoption (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:194-195`).
  - OP-1.1 still displays `ds^2=-(32 M^3/r) exp(-r/(2M)) dU dV + r^2 dOmega_2^2` without an adjacent derivation or `[UNVERIFIED]` marker (`research_program/synthesis/op11_spherical_dual_target.md:23-29`). Its source section marks Ashtekar-Krishnan unverified but does not identify or qualify a source for that coefficient (`research_program/synthesis/op11_spherical_dual_target.md:332-340`).
  - The local source discussed by committee 029 did not literally verify the displayed coefficient, and the decision preserved its status as `UNCONFIRMED` (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:164-169`). Silence in the revised blob is therefore not an honest closure of the condition.
  - The remaining repair is documentary and narrow: either add a checked derivation/source for the convention or mark the exact normalization `[UNVERIFIED]`, recompute OP-1.1's hash and reconvene. Decision 029's current sign-off authorized only the two listed corrections plus provenance-line updates, so any additional source-status edit requires explicit authorization (`docs/comite/comite_decision_029_phase1-theory-package-third-review.md:201-209`).

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Kruskal relation, Eq. (3.9), `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2556-2562` | OP-1.1: `-UV=(r/(2M)-1)e^{r/(2M)}`, so `UV` determines `r` and `D(U,V)=(-V,-U)` preserves `r` | CONFIRMED |
| Kruskal metric, Eq. (3.8), `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2555` | OP-1.1: exact line-element coefficient `-(32M^3/r)e^{-r/(2M)}dU dV` | UNCONFIRMED |
| Two-dimensional Kruskal volume, Appendix A, `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:3628-3663` | Physicist: the printed `16` versus OP-1.1's `32` can arise from whether `dU dV` denotes one metric component or the symmetrized cross term | UNCONFIRMED |
| OP-1.1 source list, `research_program/synthesis/op11_spherical_dual_target.md:332-340` | Reproducibility / Physicist: current source markers explicitly support or mark unverified the exact Kruskal normalization at `research_program/synthesis/op11_spherical_dual_target.md:24-29` | UNCONFIRMED |
| Bombelli, Eq. (2.1.3), `biblioteca/derived-md/Bombelli_1987_PhD.md:402-407` | Mathematician / Physicist: order duality is time reversal on the same underlying set, with every arrow reversed | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:171-195` | Claim boundary: event-horizon identification is global; the longest-chain/future-cardinality diagnostic depends on singularity and patch boundary | CONFIRMED |
| Eichhorn–Gamito–Stokes, §IV, Eqs. (10)-(12), `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:197-225` | OP-1.1: trapped surfaces have two negative future expansions; `Theta_in=-2/r`, `Theta_out=(1/r)(1-2M/r)`, and the Schwarzschild marginal locus is `r=2M` | CONFIRMED |
| Eichhorn–Gamito–Stokes, conclusions, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:459-469` | Physicist: the longest-chain diagnostic does not apply to geodesically complete black holes; ladder expansion additionally requires ensemble convergence | CONFIRMED |
| He–Rideout, sprinkling definition, `biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md:53-60` | OP-1.1/OP-1.2: sprinkling samples the positive volume measure, uses Poisson counts and orders elements by continuum causal relations | CONFIRMED |
| Surya review, ordering fraction, `C_k` and longest chain, `biblioteca/derived-md/The causal set approach to quantum gravity.md:1001-1015,1052-1083,1092-1118,1150-1152,1221-1246` | Mathematician: these are order invariants, while their continuum interpretations are ensemble-scoped and do not establish manifoldlikeness individually | CONFIRMED |
| Surya review, HKMM Theorem 1, `biblioteca/derived-md/The causal set approach to quantum gravity.md:329-350` | OP-1.2: HKMM assumes a chronological/causal bijection and cannot derive it from equality of sampled finite-poset laws | CONFIRMED |
| Janson arXiv:0902.0306; Hoeffding JASA 58 (1963); Howard et al. arXiv:1810.08240; Ashtekar–Krishnan arXiv:gr-qc/0407042 | OP-1.1–OP-1.3 load-bearing or limiting citations without local snapshots | UNVERIFIED |

- Notes: La discrepancia `16/32` es compatible con una diferencia de notación: si `ds²=2g_{UV}dU dV`, entonces `g_{UV}=-16A` produce el coeficiente combinado `-32A` y densidad bidimensional `sqrt(|det g|)=16A`, coincidente con el Apéndice A (`biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:3630-3663`). Pero la fuente no declara su convención de producto simétrico; por ello no confirma literalmente el `32` de OP-1.1. Además, la lista de fuentes actual no cita esa fuente ni añade un marcador específico `[UNVERIFIED_*]` para la normalización (`research_program/synthesis/op11_spherical_dual_target.md:332-340`). En consecuencia, la condición bibliográfica de decisión 029 sigue abierta en los blobs actuales: debe añadirse la derivación/convenio explícito o marcar la normalización como no verificada. La definición `iota_P=id`, su naturalidad y las reglas de `ABSTAIN` son contratos internos (`research_program/synthesis/op11_spherical_dual_target.md:182-195,255-275`); Bombelli respalda el mismo portador, pero la literatura no sustituye su tipado ni adjudica las pérdidas.

## 8. Synthesis

The two corrections explicitly authorized by decision 029 are closed. The mathematician and
logician recommend adoption pending audit. Reproducibility and physics block because decision 029
also required the exact Kruskal normalization to be honestly sourced or marked unverified. Both
wave-2 controls reproduce that source-status defect, and the pre-registration warden returns
`BLOCK`; therefore the exact hashes cannot proceed to audit.

This is not a mathematical or physical rejection of the conventional coefficient. The local source
prints a factor 16 in a two-dimensional presentation; a symmetrized-cross-term convention can
plausibly explain the factor two, but that convention is not explicit in the source. The fail-closed
repair is therefore a source-status statement, not a silent derivation or a change to the metric:

```text
[UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT]
```

It must state that the `32M^3/r` coefficient is retained as the declared convention, that the local
snapshot does not literally verify it, and that no theorem in OP-1.1--OP-1.3 depends on choosing 32
rather than the corresponding component convention 16 beyond an overall positive normalization.

## 9. Next-step spec

**Reversible step requiring PI sign-off:** make one source-status correction in OP-1.1 and only
mechanical provenance-line updates elsewhere:

1. add an adjacent note after the displayed Kruskal convention and a matching source-list entry
   carrying `[UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT]`;
2. do not alter the formula, patch, measure, target, losses, theorem statements or terminals;
3. add decision 030 to the authorization provenance of OP-1.1--OP-1.3, recompute all three hashes,
   and reconvene `/comite` on those exact blobs.

Do not run `/auditor`, code, simulations, tests, seeds, commit or push. Minimal falsification test:

```text
rg -q 'UNVERIFIED_EXACT_KRUSKAL_NORMALIZATION_LOCAL_SNAPSHOT' \
  research_program/synthesis/op11_spherical_dual_target.md
```

The next committee must verify that this marker is adjacent to the formula and represented in the
source list, and that no scientific content changed.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

Signed: Nacho / PI

Date: 2026-07-15

Decision: authorize the single source-status correction in committee decision 030 section 9,
including provenance-line updates only, reconvene on the revised hashes, and do not run auditor,
code, simulations, tests, commit, or push.
