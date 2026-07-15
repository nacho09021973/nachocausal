# Comite Decision 029 — Phase 1 theory package third review

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. The committee never executes
> a one-way or outward-facing action (the blind validation run, a commit/push, anything
> irreversible), never tunes a frozen threshold post-hoc, and never makes a reconstruction claim.
> Guardrails: `NO_RECONSTRUCTION_CLAIM`, `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`,
> `NO_GROUND_TRUTH_LEAKAGE`, `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Do the revised exact blobs

- OP-1.1 `0dfe4bea3fe7b078ac828a8974e14bb733e4dda8f6d678c6661a95f6c0b01386`;
- OP-1.2 `dbc8bd3465265541bf75dc71b798c6a7c09337663ba63a8dec7d23b2b6995fdf`;
- OP-1.3 `7914804d2448b7b40487b17876e8326cf1901c8e625e5c12ad459289c2bcca79`

close all five corrections in committee decision 028 section 8 and qualify as
`THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`, without a recovery or execution claim?

## 2. Verified state

Facts checked this session:

- `git rev-parse HEAD` and `git rev-parse origin/main` both returned
  `496985dbecd464a57267e607b7d3b48c323b510b`.
- `git status --short --branch` returned `main...origin/main` plus exactly five untracked Phase-1
  documents: decisions 027/028 and the three OP-1 candidates. No tracked code or data change was
  reported.
- `sha256sum` returned the three candidate hashes in section 1 and decision-028 hash
  `34415bd8ff690d29f8327e5c3f3a064484183cabe80ac53b01427844c243d59a`.
- Decision 028 records the PI authorization at
  `docs/comite/comite_decision_028_phase1-theory-package-second-review.md:165-172`.
- The three literal tests frozen by decision 028 for `T^-=-D_*T^+`, `nu(ABSTAIN)=ABSTAIN` and
  `n>=1` returned exit code 0.
- `python .claude/skills/comite/check_comite_brief.py` on decision 028 returned
  `BRIEF_CHECK=PASS`; five static `git diff --no-index --check` calls emitted no whitespace error.
- `rg -n "iota_P|ABSTAIN|L_side|L_trapping"` shows that `iota_P` occurs only where it is used,
  not where it is defined, and that only `A_H` has an abstention-rate rule
  (`research_program/synthesis/op11_spherical_dual_target.md:197-250`).
- Per the signed instruction, no `/auditor`, code, simulation, commit or push was run. Seal and
  executable-environment state are therefore `[UNVERIFIED_THIS_SESSION]` and are not inputs to a
  proceed verdict.

## 3. Dossier

Files and references supplied to the committee:

- `research_program/synthesis/op11_spherical_dual_target.md`;
- `research_program/synthesis/op12_tv_zero_3p1.md`;
- `research_program/work_packages/op13_positive_evidence_protocol.md`;
- `docs/comite/comite_decision_027_phase1-theory-package-first-review.md`;
- `docs/comite/comite_decision_028_phase1-theory-package-second-review.md`;
- `docs/plan_operativo_15_julio_2026.md`;
- `docs/claim_grammar.md`;
- `biblioteca/derived-md/Bombelli_1987_PhD.md`;
- `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md`;
- `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md`;
- `biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md`;
- `biblioteca/derived-md/The causal set approach to quantum gravity.md`.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): Tratar como paquete indivisible los blobs exactos `research_program/synthesis/op11_spherical_dual_target.md` (`0dfe4bea3fe7b078ac828a8974e14bb733e4dda8f6d678c6661a95f6c0b01386`), `research_program/synthesis/op12_tv_zero_3p1.md` (`dbc8bd3465265541bf75dc71b798c6a7c09337663ba63a8dec7d23b2b6995fdf`) y `research_program/work_packages/op13_positive_evidence_protocol.md` (`7914804d2448b7b40487b17876e8326cf1901c8e625e5c12ad459289c2bcca79`). El brief reconvocado debe registrar esos tres hashes y `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`; `/auditor` debe evaluar exactamente los mismos blobs, junto con la trazabilidad de decisiones 027/028. No procede crear código, datos o preregistro: OP-1.1 declara `NO_IMPLEMENTATION / NO_RECOVERY_RESULT` (`op11_spherical_dual_target.md:14-19`) y OP-1.3 mantiene `NO_EXECUTION_AUTHORIZED` e `IMPLEMENTATION_READINESS=PENDING_GENERATOR_AND_WITNESS_SPEC` (`op13_positive_evidence_protocol.md:1-8`, `:221-228`).
- Environment & seal: El gate es documental y no requiere entorno 3+1D. El próximo `/auditor` debe revalidar el seal `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, confirmar que el diff sigue limitado a documentos y ejecutar únicamente los preflights de integridad aplicables: `make verify-seal`, `make test`, `make verify-comite` y luego `make verify-audit` (`Makefile:9-17`, `:24-47`). `make dry-run`, `make gate` y `validate.run()` pertenecen al camino sellado 1+1D y siguen prohibidos en esta fase (`Makefile:12-22`; `docs/preregistration_002.md:59-68`). Ningún pin, seed o entorno 1+1D se convierte por herencia en contrato 3+1D.
- Provenance capture: La decisión debe fijar `HEAD=origin/main=496985dbecd464a57267e607b7d3b48c323b510b`, los tres SHA256 completos, hash del nuevo brief, hash del seal, lista exacta de los cinco documentos untracked y timestamp UTC. La autorización de las cinco reparaciones está firmada en `docs/comite/comite_decision_028_phase1-theory-package-second-review.md:129-172`, y los candidatos enlazan expresamente decisiones 027/028 (`op11_spherical_dual_target.md:9-12`; `op12_tv_zero_3p1.md:5-8`; `op13_positive_evidence_protocol.md:5-8`). Al estar todavía untracked, cualquier cambio de byte exige nuevos hashes, nueva decisión o rechazo del auditor; no puede auditarse “el path” sin verificar el blob.
- Run mechanics: Ahora solo corresponde la secuencia reversible `committee hash lock -> auditoría del mismo paquete -> terminal documental`; no hay proceso background, generación, consumo de seeds ni resultado científico. Las cinco correcciones están materializadas: orientación/orden exactos (`op11_spherical_dual_target.md:79-100`), involución total y tipo suma para `H_hat` (`:191-220`), predicción vacía puntuada y abstención reportada (`:241-254`), `ell_eff` restringida a `n>=1` (`op12_tv_zero_3p1.md:80-101`) y precedencias deterministas (`op11_spherical_dual_target.md:259-282`; `op13_positive_evidence_protocol.md:174-219`). Una ejecución futura deberá empezar por el manifest y los gates de generador antes de seeds (`op13_positive_evidence_protocol.md:120-137`) y conservar muestra fija/optional-stopping prohibido (`:139-159`).
- Reproducibility risks / ambiguities: **Recomendación: `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** Las cinco correcciones de decisión 028 están cerradas al nivel documental y `/auditor` es el siguiente paso correcto. Persisten únicamente bloqueos de implementación, no de auditoría teórica: no existen generador/testigo concretos, environment lock, bandas de seeds ni cotas de error instanciadas (`op13_positive_evidence_protocol.md:120-137`, `:221-228`); las fuentes primarias ausentes continúan marcadas explícitamente como no verificadas (`op11_spherical_dual_target.md:296-304`; `op12_tv_zero_3p1.md:181-191`; `op13_positive_evidence_protocol.md:230-238`). La futura spec deberá además crear un terminal positivo de **corrida** distinto de `POSITIVE_EVIDENCE_PROTOCOL_PROVED`, que el texto reserva al esquema matemático (`op13_positive_evidence_protocol.md:188-206`), y precisar cómo computan/reportan `ABSTAIN` las pérdidas element-wise `L_side` y `L_trapping`; hoy son pérdidas candidatas aún por congelar (`op11_spherical_dual_target.md:225-254`). Ningún punto autoriza recovery, simulación, commit/push ni retirada de `NO_RECONSTRUCTION_CLAIM`.

### Mathematician brief
- Computability: En un poset finito, `P^op`, autodualidad, futuros/pasados, alturas, cardinalidad y cualquier testigo acotado efectivamente especificado son computables sobre el orden parcial. OP-1.1 distingue ahora predicción vacía de abstención y hace total `nu` (`research_program/synthesis/op11_spherical_dual_target.md:193-220`); sin embargo, las cuatro ecuaciones duales usan `iota_P` e `iota_P^{-1}` sin definir esa identificación en ningún punto del documento (`research_program/synthesis/op11_spherical_dual_target.md:203-220`). Sobre representantes concretos puede repararse declarando `P^op` sobre el mismo portador e `iota_P=id`, con naturalidad bajo relabeling; sobre clases no etiquetadas no existe una identificación de elementos canónica sin esa convención.
- Order observable: El paquete no afirma un observable localizador concreto. OP-1.1 solo tipa futuras salidas order-only y prohíbe embedding en construcción, selección y abstención (`research_program/synthesis/op11_spherical_dual_target.md:191-245`); OP-1.3 admite un testigo congelado `f:Omega->[0,1]` y prueba `TV(P,Q)>=|E_Pf-E_Qf|`, pero exige `TARGET_WITNESS_MISMATCH` si `f` únicamente separa generadores (`research_program/work_packages/op13_positive_evidence_protocol.md:10-32,161-172`). La cota Hoeffding simultánea, incluido el transporte desde leyes generadas a pretendidas mediante errores TV deterministas, es matemáticamente correcta como esquema condicional (`research_program/work_packages/op13_positive_evidence_protocol.md:34-76`).
- Relevant invariants: Las leyes `fixed_n` dependen de la clase de isomorfismo del suborden inducido; `order+number` añade `N`. Dualidad, cardinalidad, ordering fraction, abundancias de intervalos y altura son invariantes order-only, aunque ninguna constituye aquí un localizador de trapping (`biblioteca/derived-md/The causal set approach to quantum gravity.md:1001-1015,1054-1082,1092-1118,1221-1246`; `research_program/work_packages/op13_positive_evidence_protocol.md:161-172`). `H_hat` está correctamente tipado como `P(S(P)) union {ABSTAIN}`: `empty` conserva falsos negativos y `A_H` reporta abstención separadamente (`research_program/synthesis/op11_spherical_dual_target.md:197-210,241-254`). En cambio, `y_hat_P` y `c_hat_P` admiten abstención por elemento, pero `L_side` y `L_trapping` no especifican si esos valores cuentan como error, se excluyen o generan terminal, ni exigen tasas de abstención análogas (`research_program/synthesis/op11_spherical_dual_target.md:197-200,225-239,247-254`).
- Analytic / continuum target: La familia dual ya está correctamente tipada: `T^-=-D_*T^+` y `x prec^+ y iff D(y) prec^- D(x)` hacen que el muestreo transportado produzca el orden opuesto, mientras la medida positiva se preserva (`research_program/synthesis/op11_spherical_dual_target.md:67-100,167-189`). El target separa localización `h_M=0`, campo puntual `c_g` y carácter sectorial `Chi`, con las transformaciones duales correspondientes (`research_program/synthesis/op11_spherical_dual_target.md:122-165`). El lema de OP-1.2 es válido: una biyección bimedible medida-causal módulo nulos acopla todos los pares de cualquier muestra finita (`research_program/synthesis/op12_tv_zero_3p1.md:22-43`). La igualdad `fixed_n` queda correctamente restringida a Schwarzschild, sector y `lambda` fijos; el coescalado `g->a^2g`, `mu->a^4mu` elimina `M` tras normalización, mientras el canal Poisson con `rho>0` conocida distingue masas por su marginal de `N` (`research_program/synthesis/op12_tv_zero_3p1.md:45-78,103-121`). `ell_eff` ya está restringida a `n>=1` sin alterar el teorema para todo `n>=0` (`research_program/synthesis/op12_tv_zero_3p1.md:80-101`).
- Caveats: **REVISE_BEFORE_AUDIT.** Las cinco reparaciones literales de la decisión 028 están incorporadas (`docs/comite/comite_decision_028_phase1-theory-package-second-review.md:129-159`), y no queda un bloqueo en la familia dual, el lema `TV=0`, el escalado o la cota testigo. Persiste, no obstante, un defecto de tipo en el contrato dual: `iota_P` es un símbolo libre; debe definirse y demostrar su compatibilidad con relabeling antes de adoptar los blobs exactos. También debe congelarse una regla fail-closed para las abstenciones element-wise de `y_hat_P` y `c_hat_P`, o eliminarlas de esos codominios; de otro modo las pérdidas balanceadas pueden depender de una coerción no especificada (`research_program/synthesis/op11_spherical_dual_target.md:193-239`). Estas son reparaciones documentales mínimas. La ausencia de generador y testigo concretos no bloquea el teorema condicional, pero mantiene correctamente `IMPLEMENTATION_READINESS=PENDING_GENERATOR_AND_WITNESS_SPEC` y excluye cualquier claim de recovery o ejecución (`research_program/work_packages/op13_positive_evidence_protocol.md:203-228`).

### Mathematical logic brief
- Formal status: OP-1.1 contains typed definitions of the dual Schwarzschild family, continuum targets, output types, losses and terminal order; its author terminal is the documentary theorem `DUAL_FAMILY_CLOSED`, not estimator existence, convergence or recovery (`research_program/synthesis/op11_spherical_dual_target.md:67-100`, `:122-165`, `:191-257`, `:259-294`). OP-1.2 proves a sufficient coupling lemma, fixed-`n` equality on the co-scaled mass orbit and a scoped known-`rho` Poisson iff; the general converse, varying-patch class and asymptotic equivalence remain open (`research_program/synthesis/op12_tv_zero_3p1.md:22-78`, `:103-121`, `:138-179`). OP-1.3 proves a conditional fixed-sample certificate schema; concrete generators, witnesses and any sequential extension remain uninstantiated and unauthorized (`research_program/work_packages/op13_positive_evidence_protocol.md:10-79`, `:139-159`, `:221-228`). No statement is presented as a Lean theorem.
- Quantifier / dependency order: OP-1.1 now fixes the patch, positive measure, time orientation and ambient causal relation before deriving the dual observed law (`research_program/synthesis/op11_spherical_dual_target.md:30-100`, `:167-189`). OP-1.2 quantifies causal preservation under `mu_g tensor mu_g` on conull representatives before coupling each finite iid sample, and fixes sector plus `lambda` before varying mass (`research_program/synthesis/op12_tv_zero_3p1.md:22-43`, `:45-78`). Its all-`n>=0` law theorem is correctly separated from the scoring-only domain `ell_eff`, now restricted to `n>=1` (`research_program/synthesis/op12_tv_zero_3p1.md:10-17`, `:80-101`). OP-1.3 freezes intended/generated laws, witness hash, iid sample sizes, multiplicity budget and deterministic generator-error bounds before confirmation; adaptive development cannot inspect embedding-derived quantities for promotion and requires full provenance (`research_program/work_packages/op13_positive_evidence_protocol.md:34-76`, `:81-106`, `:120-137`).
- Equivalence claims: The dual model is now defined componentwise by `T^-=-D_*T^+` and `x prec^+ y iff D(y) prec^- D(x)`, so `D^2=id`, family closure and `Law_K(Dg)=d_#Law_K(g)` have the required orientation/order hypotheses explicitly in scope (`research_program/synthesis/op11_spherical_dual_target.md:79-100`, `:167-189`). OP-1.2 uses only the forward measure-causal coupling implication and explicitly declines its converse (`research_program/synthesis/op12_tv_zero_3p1.md:22-43`). Its fixed-`n` equality is only for fixed sector and `lambda`; its `TV=0 iff M=M'` is only for fixed known `rho>0`, sector and `lambda`; neither is exported to arbitrary 3+1D geometry (`research_program/synthesis/op12_tv_zero_3p1.md:45-78`, `:103-121`, `:138-179`). OP-1.3's Hoeffding radii plus union bounds yield simultaneous coverage at least `1-alpha_total`, and the deterministic tilde-to-intended TV bounds justify subtracting `epsilon_Pj+epsilon_Qj` (`research_program/work_packages/op13_positive_evidence_protocol.md:34-76`).
- Type / object discipline: Decision 028's type blockers are closed. The physical pointwise field `c_g` and scalar sector target `Chi(g)` have matching discrete outputs (`research_program/synthesis/op11_spherical_dual_target.md:138-161`, `:191-220`). `nu` is a total involution fixing `0` and `ABSTAIN`, and the lifted set action distinguishes an empty prediction from the separate abstention summand (`research_program/synthesis/op11_spherical_dual_target.md:196-220`). `L_H` scores empty predictions, abstains only on the sum value `ABSTAIN`, reports abstention rate separately and fails closed on empty scoring classes (`research_program/synthesis/op11_spherical_dual_target.md:225-257`). OP-1.1 and OP-1.3 now give total deterministic precedence orders, including `TARGET_NOT_SPECIFIABLE`, simultaneous provenance/generator failures and the distinction between contract terminals and scientific outcomes (`research_program/synthesis/op11_spherical_dual_target.md:259-282`; `research_program/work_packages/op13_positive_evidence_protocol.md:174-228`).
- Caveats:
  - **Recommendation: `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** The exact blobs close decision 028 §8's five corrections and, transitively, decision 027's earlier blockers. Their author terminals are logically deserved at the narrow documentary/conditional levels stated; none licenses implementation, recovery or execution (`research_program/synthesis/op11_spherical_dual_target.md:284-294`; `research_program/synthesis/op12_tv_zero_3p1.md:166-179`; `research_program/work_packages/op13_positive_evidence_protocol.md:203-228`).
  - Final `PHASE_1_THEORY_READY` remains unavailable until the identical hashes pass the required independent mathematical/bibliographic, committee and auditor gates (`docs/plan_operativo_15_julio_2026.md:293-304`).
  - `POSITIVE_EVIDENCE_PROTOCOL_PROVED` must remain interpreted as the conditional certificate theorem, never as a future scientific PASS; the draft states this distinction and leaves `IMPLEMENTATION_READINESS=PENDING_GENERATOR_AND_WITNESS_SPEC` (`research_program/work_packages/op13_positive_evidence_protocol.md:188-228`).
  - Primary sources absent from the local library remain explicitly marked `[UNVERIFIED_*]`; audit must preserve that status rather than upgrading the paper-level derivations by citation alone (`research_program/synthesis/op11_spherical_dual_target.md:296-304`; `research_program/synthesis/op12_tv_zero_3p1.md:181-191`; `research_program/work_packages/op13_positive_evidence_protocol.md:230-238`).
  - Decision 028 authorizes only the five documentary corrections and reconvening, with auditor, code and simulations still prohibited until the committee issues the proceed state (`docs/comite/comite_decision_028_phase1-theory-package-second-review.md:144-172`).

### Physicist brief
- Coordinates & patch: OP-1.1 usa Kruskal adimensional `(U,V,omega)` con `-UV=(r/(2M)-1)e^{r/(2M)}` y la métrica Schwarzschild 3+1D (`research_program/synthesis/op11_spherical_dual_target.md:21-28`; convención Kruskal local en `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562`). El patch BH mantiene `V>0`, cruza `U=0`, contiene las esferas `S^2` completas y satisface `UV<=1-epsilon_s`; por ello incluye un corte de `H^+` pero excluye singularidad, bifurcation sphere e infinito nulo (`op11_spherical_dual_target.md:30-65`). Su imagen por `D(U,V,omega)=(-V,-U,omega)` contiene el corte dual de `H^-`. La causalidad está fijada como el suborden inducido por Schwarzschild maximal, no por curvas obligadas a permanecer en el patch (`op11_spherical_dual_target.md:67-77`).
- Physical meaning of the signal: La orientación ya está correctamente tipada: `T^-=-D_*T^+` y `x prec^+ y iff D(y) prec^- D(x)` hacen que `D` envíe curvas futuras BH a curvas pasadas WH y produzca el poset dual (`op11_spherical_dual_target.md:79-100`; la identificación time-reversal/order-duality aparece en `biblioteca/derived-md/Bombelli_1987_PhD.md:402-407`). Para esferas de simetría, `theta_k=(2/r)k(r)`, de modo que el signo es independiente de una normalización nula positiva (`op11_spherical_dual_target.md:102-120`). EGS obtiene `Theta_in=-2/r` y `Theta_out=(1/r)(1-2M/r)`, confirmando el cambio de signo en `r=2M` (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:197-225`). Por tanto `h_M`, el lado `y_g`, el campo puntual `c_g` y el carácter sectorial separado `Chi(g)` son targets físicamente coherentes dentro de esta familia (`op11_spherical_dual_target.md:122-165`). La involución `nu` hace total la acción dual sobre signos y abstención (`op11_spherical_dual_target.md:191-220`).
- Sprinkling domain: El modelo distingue correctamente la medida positiva `mu=|dVol|` de la 4-forma orientada: `D_#mu^+=mu^-`, mientras `D^*dVol_oriented=-dVol_oriented` (`op11_spherical_dual_target.md:67-100`). Los canales son experimentos distintos: IID de `mu_g/mu_g(K_g)` en `fixed_n` y PPP de intensidad conocida `rho mu_g` en `order+number` (`op11_spherical_dual_target.md:167-189`), coherente con la definición de sprinkling/Poisson en `biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md:50-60`). Con `lambda` y sector fijos, la métrica coescala como `M^2`, la medida como `M^4` y la ley normalized fixed-n permanece idéntica; con `rho` conocida, la marginal Poisson de `N` separa masas distintas (`research_program/synthesis/op12_tv_zero_3p1.md:45-78`, `:103-121`). `ell_eff` está correctamente restringida a `n>=1` y declarada escala de scoring, no densidad física observada (`op12_tv_zero_3p1.md:80-101`).
- Claim boundary: `L_H` puntúa una banda de resolución `delta_H`, no hits exactos sobre la superficie de medida cero; la predicción vacía se puntúa, `ABSTAIN` es un valor distinto y su frecuencia se reporta (`op11_spherical_dual_target.md:225-257`). Esto define un contrato de scoring, no un localizador existente. OP-1.2 solo clasifica la órbita Schwarzschild exacta, coescalada, con `lambda` y sector fijos; deja abiertas perturbaciones, patches no coescalados, BH/WH orientados y asintóticos (`op12_tv_zero_3p1.md:123-179`). OP-1.3 separa explícitamente evidencia TV de recoverability física (`research_program/work_packages/op13_positive_evidence_protocol.md:161-172`). Nada demuestra recovery 3+1D, reconstrucción métrica, convergencia de horizonte global, dinámica cuántica o ejecutabilidad: `NO_RECONSTRUCTION_CLAIM`.
- Caveats: **Recomendación: `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** Las cinco correcciones físicas/tipadas de decisión 028 están cerradas: orientación y causalidad dual, involución total, predicción vacía frente a abstención, dominio de `ell_eff` y precedencias (`op11_spherical_dual_target.md:79-100`, `:191-220`, `:241-282`; `op12_tv_zero_3p1.md:94-101`; `op13_positive_evidence_protocol.md:188-219`). La auditoría es el siguiente gate, no una simulación. Persisten límites explícitos: no hay generador, intensidad, niveles `n`, testigo ni pérdidas congeladas para una inferencia concreta (`op11_spherical_dual_target.md:225-239`; `op13_positive_evidence_protocol.md:221-228`). La extensión a agujeros negros regulares o geometrías dinámicas sigue abierta; EGS advierte que el diagnóstico de cadenas/futuros depende de incompletitud y borde y falla para BH regulares (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-199`, `:463-469`). Las fuentes primarias locales ausentes permanecen correctamente marcadas `[UNVERIFIED_*]` (`op11_spherical_dual_target.md:296-304`; `op12_tv_zero_3p1.md:181-191`).

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes: `DECISION=REVISE_BEFORE_AUDIT`. La objeción sobre `iota_P` es válida: OP-1.1 usa `iota_P`, su inversa y el lift `iota_*^A` sin definir la identificación de soportes ni su naturalidad bajo relabeling (`research_program/synthesis/op11_spherical_dual_target.md:191-220`). En un representante concreto puede cerrarse declarando `P^op=(S(P),prec^op)`, `iota_P=id_{S(P)}` e `iota_{sigma.P} o sigma = sigma o iota_P`; sobre la clase no etiquetada no existe por sí sola una correspondencia canónica de elementos. También es válida la objeción de scoring: `y_hat_P` y `c_hat_P` admiten `ABSTAIN` por elemento, pero `L_side` y `L_trapping` no dicen si ese valor cuenta como error, se excluye del denominador o activa un terminal (`op11_spherical_dual_target.md:193-200`, `:225-254`). Un estimador que se abstenga exactamente en elementos difíciles puede obtener pérdidas arbitrariamente distintas según la coerción elegida. Las cinco reparaciones literales de decisión 028 sí están presentes (`docs/comite/comite_decision_028_phase1-theory-package-second-review.md:129-159`), pero estos dos defectos impiden que target/salida/pérdida/abstención sea todavía un contrato total.
- Ground-truth leakage: OP-1.3 prohíbe correctamente que embedding guíe selección del testigo (`research_program/work_packages/op13_positive_evidence_protocol.md:90-106`). Sin embargo, una `iota_P` no definida podría implementarse usando etiquetas de embedding o correspondencias coordenadas entre sprinklings duales, aunque la inferencia debe ser order-only. Debe fijarse como identificación puramente combinatoria del mismo portador antes de datos. Asimismo, la regla sobre `ABSTAIN` debe ser independiente de `h_M`, `c_g` y la banda geométrica; esas cantidades solo pueden entrar en scoring (`op11_spherical_dual_target.md:222-245`).
- Freeze violations: No se ha roto ningún seal ni consumido seeds. El problema es prospectivo: los hashes congelan símbolos cuya semántica permanece abierta. Elegir después `iota_P`, excluir abstenciones element-wise o contarlas como errores cambiaría el observable y la pérdida sin modificar los targets físicos. Esas reglas deben incorporarse documentalmente, generar nuevos hashes y volver a comité; decisión 028 autoriza reconvocatoria documental pero mantiene auditor, código y simulación prohibidos hasta proceed (`docs/comite/comite_decision_028_phase1-theory-package-second-review.md:144-172`).
- Verdict coercion: `H_hat` ya distingue correctamente `empty` de `ABSTAIN` y reporta `A_H` (`op11_spherical_dual_target.md:197-210`, `:241-254`). No existe el análogo para `y_hat_P` o `c_hat_P`. Si se eliminan del denominador sus elementos abstaining, un estimador siempre abstaining puede ocultar error; si se cuentan como error, debe decirse; si activan terminal, debe fijarse precedencia y tasa. `LOSS_UNSCORABLE` solo cubre clases de scoring vacías, no esta elección (`op11_spherical_dual_target.md:259-282`). Esta ambigüedad permite coercionar abstención a aparente performance.
- Premature / over-broad claims: La clausura física de la familia, la órbita `TV=0` acotada y el certificado Hoeffding condicional sobreviven (`op11_spherical_dual_target.md:79-100`, `:284-294`; `research_program/synthesis/op12_tv_zero_3p1.md:45-78`, `:166-179`; `research_program/work_packages/op13_positive_evidence_protocol.md:34-76`, `:221-228`). No hay claim explícito de recovery o ejecución. Pero promover el paquete completo a contrato de Fase 1 sería prematuro porque el plan exige salida, pérdida y abstención especificadas antes del gate (`docs/plan_operativo_15_julio_2026.md:202-215`, `:293-304`). `NO_RECONSTRUCTION_CLAIM` permanece obligatorio.
- Independent-falsification gate: No está satisfecho. El desacuerdo de ola 1 es sustantivo y este ataque reproduce ambos defectos directamente en el blob exacto. El autor no es el único verificador, pero `/auditor` no debe recibir un paquete cuyo contrato dual y scoring todavía admiten dos interpretaciones incompatibles.
- Minimal falsification test: Ejecutar `bash -c 'rg -q "iota_P *= *id" research_program/synthesis/op11_spherical_dual_target.md && rg -q "ABSTAIN.*(cuenta como error|activa.*terminal)" research_program/synthesis/op11_spherical_dual_target.md && rg -q "A_(side|trapping)" research_program/synthesis/op11_spherical_dual_target.md'`; debe devolver código distinto de cero sobre el blob actual. La reparación mínima debe definir la identificación natural y una política fail-closed más tasa de abstención para ambas salidas element-wise.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: BLOCK
- Freeze status: No numerical threshold, concrete witness, generator, seed band or confirmatory grid is frozen by these theory drafts. OP-1.1 explicitly leaves its candidate losses for a later pre-inference freeze (`research_program/synthesis/op11_spherical_dual_target.md:225-239`), while OP-1.3 requires all laws, witness hashes, sample sizes, alpha allocations, deterministic generator-error bounds and manifest fields before confirmation (`research_program/work_packages/op13_positive_evidence_protocol.md:34-76`, `:120-137`). Before theory adoption, however, the support identification and element-wise abstention semantics must be fixed in writing because they define the observable/scoring contract rather than a future numerical threshold.
- Seal integrity: No sealed path was run or modified. The live `nachocausal/thresholds.py` SHA256 remains `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, matching the operative prereg-002 seal (`docs/preregistration_002.md:7-12`). OP-1.1 remains `NO_IMPLEMENTATION / NO_RECOVERY_RESULT`, and OP-1.3 remains `NO_EXECUTION_AUTHORIZED` (`research_program/synthesis/op11_spherical_dual_target.md:1-19`; `research_program/work_packages/op13_positive_evidence_protocol.md:1-8`).
- Seed discipline: No development, validation or reserved seed is consumed. OP-1.3 correctly requires independent confirmation after development, forbids reuse without a uniform bound and requires complete search and seed provenance before promotion (`research_program/work_packages/op13_positive_evidence_protocol.md:81-106`, `:133-137`).
- Reporting rule: Report `BLOCK / REVISE_BEFORE_AUDIT`; do not record `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING` or combine the author terminals into `PHASE_1_THEORY_READY`. Decision 028 forbids `/auditor` until the reconvened committee returns a proceed verdict (`docs/comite/comite_decision_028_phase1-theory-package-second-review.md:144-159`). Element-wise abstentions must not be silently removed from denominators, counted as correct, or coerced into an ordinary scientific error without a predeclared rule (`docs/claim_grammar.md:369-384`).
- Forbidden moves present? No post-hoc tuning, threshold loosening, seed reuse, validation rerun, ground-truth leakage, reconstruction claim, code execution, commit or push occurred. Adopting the current blobs would nevertheless permit post hoc choice of the element correspondence and abstention scoring convention.
- Reasons:
  - `iota_P` and `iota_P^{-1}` are free symbols in every representative-level dual-output equation; OP-1.1 never defines their domain, value, involution law or relabeling naturality (`research_program/synthesis/op11_spherical_dual_target.md:203-220`). The adopted grammar requires this support bijection and `iota_{P^op} o iota_P=id` to be frozen before duality is claimed (`docs/claim_grammar.md:141-152`). Since `P^op` is intended on the same carrier, the minimal repair is to declare `iota_P=id_{S(P)}` and its relabeling compatibility, or define an equally explicit natural family.
  - `y_hat_P` and `c_hat_P` permit `ABSTAIN` separately for each element, but `L_side` and `L_trapping` merely say “error balanceado” and do not state whether abstaining elements count as errors, are excluded with changed denominators, or activate a higher-precedence terminal (`research_program/synthesis/op11_spherical_dual_target.md:191-220`, `:225-239`).
  - The detailed empty-versus-abstain rule and reported rate `A_H` apply only to set-valued `H_hat`; they do not close element-wise abstention for `y_hat` or `c_hat` (`research_program/synthesis/op11_spherical_dual_target.md:241-254`). The Phase-1 specification expressly requires target, output, loss and abstention to be jointly specified (`docs/plan_operativo_15_julio_2026.md:202-208`).
  - OP-1.1's displayed precedence contains no dedicated element-wise abstention terminal, and `LOSS_UNSCORABLE` is defined for empty scoring classes rather than voluntary per-element abstention (`research_program/synthesis/op11_spherical_dual_target.md:259-282`). A fail-closed repair must either remove `ABSTAIN` from those pointwise codomains or define rates, loss treatment and terminal precedence.
  - Decision 028's five named corrections are otherwise present: typed time reversal/order, total `nu`, empty set versus `H_hat=ABSTAIN`, `ell_eff` restricted to `n>=1`, and deterministic terminal chains (`research_program/synthesis/op11_spherical_dual_target.md:79-100`, `:191-220`, `:241-282`; `research_program/synthesis/op12_tv_zero_3p1.md:80-101`; `research_program/work_packages/op13_positive_evidence_protocol.md:174-228`). The required revision is therefore narrow and documentary; OP-1.2's scoped theorem and OP-1.3's conditional certificate need no scientific rerun.

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Kruskal relation, `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562`, Eqs. (3.8)-(3.9) | Physicist / OP-1.1: `UV` determines `r`; the horizon is `UV=0`; `D(U,V)=(-V,-U)` preserves `UV` and `r` | CONFIRMED |
| Same Kruskal source, `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562` | OP-1.1: exact displayed 3+1 metric coefficient `-(32M^3/r)e^{-r/2M}dU dV` | UNCONFIRMED |
| Bombelli, *Space-time as a causal set*, Eq. (2.1.3), `biblioteca/derived-md/Bombelli_1987_PhD.md:402-407` | Mathematician / Physicist: causal-set time reversal is order duality on the same underlying set, with every arrow reversed | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:171-180` | Claim boundary: an event horizon is global and its direct causal-set definition requires an infinite sprinkling | CONFIRMED |
| Eichhorn–Gamito–Stokes, §IV, Eqs. (10)-(12), `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:197-225` | Physicist / OP-1.1: trapped surfaces have two negative future null expansions; in Schwarzschild `Theta_in=-2/r`, `Theta_out=(1/r)(1-2M/r)`, with marginal locus `r=2M` | CONFIRMED |
| Eichhorn–Gamito–Stokes, Eq. (11), `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:214-225` | OP-1.1: for symmetry spheres, expansion is logarithmic area change and hence `theta_k=(2/r)k(r)` | CONFIRMED |
| Eichhorn–Gamito–Stokes, §III and conclusions, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-195,463-465` | Physicist: longest-chain/future-cardinality separation relies on geodesic incompleteness and patch boundaries and does not transfer to regular/geodesically complete black holes | CONFIRMED |
| He–Rideout causal-set sprinkling discussion, `biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md:53-60` | Physicist / OP-1.2: sprinkling uses the volume measure, Poisson counts, and continuum causal relations; at density `rho`, the count mean is `rho Vol` | CONFIRMED |
| Surya review, Eq. (14), `biblioteca/derived-md/The causal set approach to quantum gravity.md:1001-1015,1054-1082` | Mathematician: ordering fraction is order-only, but its geometric interpretation is ensemble-scoped and one matching invariant does not establish manifoldlikeness | CONFIRMED |
| Surya review, Eqs. (19), (21), `biblioteca/derived-md/The causal set approach to quantum gravity.md:1092-1118,1151-1152,1221-1246` | Mathematician: `C_k` abundances and longest-chain height are order invariants; longest-chain continuum correspondence has substantial finite-density fluctuations and is ensemble-based | CONFIRMED |
| Surya review, HKMM Theorem 1, `biblioteca/derived-md/The causal set approach to quantum gravity.md:329-350` | OP-1.2: HKMM assumes a chronological/causal bijection and yields conformal equivalence; it does not derive that bijection from equality of finite sampled-poset laws | CONFIRMED |
| Janson, arXiv:0902.0306 | OP-1.2: equality of all finite-poset laws implies only weak kernel equivalence, not the claimed strong continuum converse | UNVERIFIED |
| Hoeffding, JASA 58 (1963) | OP-1.3: the stated fixed-sample radii and simultaneous coverage | UNVERIFIED |
| Howard et al., arXiv:1810.08240 | OP-1.3: optional stopping requires a time-uniform confidence sequence | UNVERIFIED |
| Ashtekar–Krishnan, arXiv:gr-qc/0407042 | OP-1.1: quasi-local horizon target formulated through null expansions | UNVERIFIED |

- Notes: La relación implícita de Kruskal está confirmada, pero la fuente local imprime `16M^3/r` en su término radial y no muestra el término angular 3+1D (`biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562`); por ello no verifica literalmente la normalización `32M^3/r` de OP-1.1. La preservación de `UV` por `D=(-V,-U)` es una deducción algebraica inmediata; la elección `T^-=-D_*T^+` y la equivalencia causal puntual son definiciones internas del modelo, no resultados citados. Bombelli sí confirma que el dual usa el mismo portador, lo que permite definir `iota_P=id`, pero no subsana que `iota_P` esté sin definir en el contrato actual (`research_program/synthesis/op11_spherical_dual_target.md:203-220`). Del mismo modo, el tratamiento de `ABSTAIN` en `L_side` y `L_trapping` es una objeción interna de tipos/scoring (`research_program/synthesis/op11_spherical_dual_target.md:197-200,225-254`), no una cuestión resoluble por literatura. Las fórmulas de Hoeffding son algebraicamente compatibles con la desigualdad estándar, pero permanecen bibliográficamente `UNVERIFIED` porque no existe snapshot local; lo mismo aplica a Janson, Howard et al. y Ashtekar–Krishnan.

## 8. Synthesis

The five corrections explicitly authorized by decision 028 are present. Reproducibility,
mathematical logic and physics recommend adoption pending audit; the causal-set mathematician
dissents. Wave-2 falsification reproduces that dissent, and the pre-registration warden returns
`BLOCK`. That disagreement is load-bearing.

Two documentary defects remain in OP-1.1:

1. `iota_P` is a free symbol in the dual-output contract. Defining the dual on the same carrier and
   freezing `iota_P=id_{S(P)}`, its involution law and naturality under relabeling closes the
   representative-versus-isomorphism-class ambiguity without embedding information.
2. `y_hat_P` and `c_hat_P` allow element-wise `ABSTAIN`, but `L_side` and `L_trapping` do not say
   how it is scored or reported. The contract must adopt one fail-closed convention and expose
   separate `A_side` and `A_trapping` rates. The recommended convention is to count each
   element-wise abstention as an error in the corresponding balanced loss while also reporting
   its rate; this prevents denominator gaming and needs no new terminal.

OP-1.2's scoped TV=0 classification and OP-1.3's conditional positive-evidence theorem survive
unchanged. The future implementation spec should create a scientific-run positive terminal distinct
from the author theorem `POSITIVE_EVIDENCE_PROTOCOL_PROVED`, but that is not a blocker for this
theory package. Literature confirms the load-bearing physical claims except the exact displayed
Kruskal metric coefficient, whose present local source is `UNCONFIRMED`; its source status must not
be upgraded without primary verification.

## 9. Next-step spec

**Reversible step requiring PI sign-off:** apply only these two corrections to OP-1.1:

1. define `P^op=(S(P),prec^op)` on the same carrier, set `iota_P=id_{S(P)}`, require
   `iota_{P^op} o iota_P=id` and freeze relabeling naturality;
2. define element-wise `ABSTAIN` as an error for `L_side` and `L_trapping`, report
   `A_side` and `A_trapping` separately, and state that abstaining elements never leave the loss
   denominator.

Then recompute all three candidate hashes and reconvene `/comite` on those exact blobs. OP-1.2 and
OP-1.3 should change only if their authorization provenance lines must name this decision. Do not
run `/auditor`, code, simulations, tests, seeds, commit or push until a proceed verdict and separate
authorization.

Minimal falsification test:

```text
rg -q 'iota_P *= *id' research_program/synthesis/op11_spherical_dual_target.md
rg -q 'ABSTAIN.*cuenta como error' research_program/synthesis/op11_spherical_dual_target.md
rg -q 'A_side.*A_trapping' research_program/synthesis/op11_spherical_dual_target.md
```

The revised committee must also confirm that exact metric normalization remains honestly sourced
or marked unverified and that no output/scoring convention uses embedding information.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

Signed: Nacho / PI

Date: 2026-07-15

Decision: authorize the two reversible corrections in committee decision 029 section 9,
including provenance-line updates only, reconvene on the revised hashes, and do not run auditor,
code, simulations, tests, commit, or push.
