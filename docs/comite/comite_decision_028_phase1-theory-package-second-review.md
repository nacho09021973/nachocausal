# Comite Decision 028 — Phase 1 theory package second review

> Produced by `/comite`. The committee PROPOSES; the user AUTHORISES. No code, simulation,
> scientific run, commit or push is authorized. Guardrails: `NO_RECONSTRUCTION_CLAIM`,
> `NO_POST_HOC_TUNING`, `NO_THRESHOLD_LOOSENING`, `NO_GROUND_TRUTH_LEAKAGE`,
> `RESPECT_SEAL_FREEZE`.

## 1. Decision question

Do the exact revised OP-1.1, OP-1.2 and OP-1.3 blobs close decision 027 and qualify for
`THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`?

## 2. Verified state

- `HEAD=origin/main=496985dbecd464a57267e607b7d3b48c323b510b`.
- Decision 027 is signed by Nacho / PI on 2026-07-15 and authorizes its eight reversible
  corrections and reconvening, with no code or simulation.
- Candidate hashes:
  - OP-1.1: `c6a7e58d390dc48e2f5ce95108956c3271af76888e682fb8465d2df11388af48`;
  - OP-1.2: `d22299e6c842343574ef679df1e291e4d9f565c65d0fb6155d062e3d9390f863`;
  - OP-1.3: `fccc00a2f6344745932a04e5c44bde72b37e11552953dd61b7dd55e374f75b80`.
- Whitespace, anchors and decision-027 minimal falsification checks pass. Obsolete symbols are
  absent. Only documentary files are untracked.
- No generator, test, simulation, seed, data, threshold or sealed path ran or changed.

## 3. Dossier

- `docs/comite/comite_decision_027_phase1-theory-package-first-review.md`
- `research_program/synthesis/op11_spherical_dual_target.md`
- `research_program/synthesis/op12_tv_zero_3p1.md`
- `research_program/work_packages/op13_positive_evidence_protocol.md`
- `docs/claim_grammar.md`
- `docs/plan_operativo_15_julio_2026.md:179-304`
- Local primary/derived sources named in the three candidates.

## 4. Expert briefs (wave 1 — blind, parallel)

### Reproducibility engineer brief
- Proposed artefact(s): Tratar los tres blobs revisados como un paquete indivisible: `research_program/synthesis/op11_spherical_dual_target.md` (`c6a7e58d390dc48e2f5ce95108956c3271af76888e682fb8465d2df11388af48`), `research_program/synthesis/op12_tv_zero_3p1.md` (`d22299e6c842343574ef679df1e291e4d9f565c65d0fb6155d062e3d9390f863`) y `research_program/work_packages/op13_positive_evidence_protocol.md` (`fccc00a2f6344745932a04e5c44bde72b37e11552953dd61b7dd55e374f75b80`). La decision reconvocada debe registrar los tres hashes y `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`; el siguiente artefacto correcto es un unico informe `/auditor` sobre exactamente ese paquete. No procede crear codigo, datos ni preregistro: OP-1.1 sigue siendo `NO_IMPLEMENTATION / NO_RECOVERY_RESULT` (`op11_spherical_dual_target.md:12-17`) y OP-1.3 conserva `IMPLEMENTATION_READINESS=PENDING_GENERATOR_AND_WITNESS_SPEC` (`op13_positive_evidence_protocol.md:199-206`).
- Environment & seal: El paso documental no necesita un entorno cientifico nuevo. `/auditor` debe revalidar el seal `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`, ejecutar los checkers documentales y confirmar que no cambiaron `nachocausal/`, tests, datos, resultados, thresholds, seeds ni preregistros. `make verify-seal`, `make test`, `make verify-comite` y `make verify-audit` son los preflights pertinentes (`Makefile:9-17`, `:24-47`); `make dry-run`, `make gate` y `validate.run()` siguen fuera de alcance (`Makefile:12-22`; `docs/preregistration_002.md:59-68`). El pin historico `numpy==1.26.4` no se hereda como entorno 3+1D; una implementacion futura requerira lock propio.
- Provenance capture: La decision y auditoria deben fijar `HEAD=origin/main=496985dbecd464a57267e607b7d3b48c323b510b`, los tres SHA256 completos, el hash del brief reconvocado, el seal, el estado exacto del arbol y timestamp UTC. Los ocho cambios estan trazados a la decision firmada 027 (`op11_spherical_dual_target.md:9-10`; `op12_tv_zero_3p1.md:5-6`; `op13_positive_evidence_protocol.md:5-6`). Para una futura confirmacion, OP-1.3 ya exige hashes de codigo/generador/testigo, entorno y RNG, derivacion de seeds, bandas disjuntas, celdas, tamanos, alpha, errores del generador, rejilla, separacion, umbral y timestamps; un manifest incompleto aborta antes de consumir seeds (`op13_positive_evidence_protocol.md:131-135`).
- Run mechanics: La unica mecanica autorizable ahora es: decision de comite sobre hashes exactos, auditoria read-only del mismo paquete y, solo si pasa, promocion documental de los tres terminales al gate de Fase 1. No hay proceso background ni paso confirmatorio. Para la futura spec, el preflight debe resolver `EXACT_GENERATOR` o cotas deterministas de error, verificar manifest e independencia IID, y abortar antes de seeds si falla (`op13_positive_evidence_protocol.md:34-74`, `:118-135`). La ejecucion confirmatoria sera una unica muestra fija; parada secuencial permanece prohibida y una interrupcion prevalece sobre cualquier resultado cientifico (`op13_positive_evidence_protocol.md:137-157`, `:172-201`).
- Reproducibility risks / ambiguities: **Recomendacion: `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** Los ocho blockers de decision 027 estan cerrados al nivel documental: modelo/medida/causalidad (`op11_spherical_dual_target.md:65-92`), campo puntual frente a caracter sectorial (`:130-153`, `:183-221`), perdida `L_H` y abstenciones (`:207-253`), medida producto y `ell_eff` (`op12_tv_zero_3p1.md:20-37`, `:78-98`), leyes intended/generated e IID (`op13_positive_evidence_protocol.md:32-74`), seleccion sin embedding y provenance (`:79-104`), manifest/interrupcion y `Delta_alt` (`:131-157`, `:172-201`) y fuentes ausentes marcadas explicitamente como no verificadas (`op11_spherical_dual_target.md:267-275`; `op12_tv_zero_3p1.md:178-188`; `op13_positive_evidence_protocol.md:208-216`). Los riesgos restantes no bloquean la auditoria teorica, pero si cualquier implementacion: las fuentes primarias locales continuan sin verificar, no existe generador/testigo concreto, no hay environment lock ni seed bands congeladas, y `EXACT_GENERATOR`/`BOUNDED_GENERATOR_ERROR` aun no estan satisfechos. `/auditor` es por tanto el proximo paso correcto; no debe convertir esos pendientes en evidencia de recovery, permitir ejecucion ni retirar `NO_RECONSTRUCTION_CLAIM`.

### Mathematician brief
- Computability: Sobre un poset finito, que es un orden parcial, son decidibles `P^op`, autodualidad, clases de isomorfismo, futuros/pasados, alturas y cualquier salida/testigo efectivamente especificado. OP-1.1 tipa ahora representantes, orden ambiente, salidas equivariantes y gates de dominio (`research_program/synthesis/op11_spherical_dual_target.md:65-92,159-205,231-253`). No reutiliza el `tau(n)` historico; las abstenciones pertinentes son `LOSS_UNSCORABLE`, `CHARACTER_ABSTAIN_SELF_DUAL` y `ESTIMATOR_ABSTAIN_NO_INTERFACE`.
- Order observable: El paquete sigue sin proponer un localizador concreto. OP-1.1 define `y_hat_P`, `H_hat`, `c_hat_P` y `Chi_hat`, pero prohibe embedding en su construccion (`op11_spherical_dual_target.md:183-226`). OP-1.2 compara leyes del suborden inducido no etiquetado. OP-1.3 certifica cualquier `f:Omega->[0,1]` congelado, separando seleccion order-only y scoring geometrico (`research_program/work_packages/op13_positive_evidence_protocol.md:8-30,79-104,159-170`). Por tanto, el terminal posible es un contrato teorico, no existencia de reconstructor.
- Relevant invariants: Ordering fraction, abundancias `C_k`, longest-chain y future-volume son invariantes order-only, pero sus correspondencias geometricas son ensemble-scoped y ninguna es por si sola un localizador de trapping (`biblioteca/derived-md/The causal set approach to quantum gravity.md:1001-1015,1054-1082,1092-1118,1151-1152,1221-1246`). El paquete evita correctamente heredar el future-volume/longest-chain singularity-truncation proxy como expansion 3+1D (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-230`; `op13_positive_evidence_protocol.md:159-170`).
- Analytic / continuum target: La separacion entre campo puntual `c_g`, caracter sectorial `Chi(g)` y localizacion `h_M=0` corrige el bloqueo anterior (`op11_spherical_dual_target.md:114-157`). `L_H` puntua una banda embedding-only, declara denominadores y emite abstencion para clases vacias (`op11_spherical_dual_target.md:207-229,245-253`). El lema de OP-1.2 cuantifica ahora la equivalencia causal bajo `mu_g tensor mu_g`, de modo que la union finita de pares excepcionales es nula (`research_program/synthesis/op12_tv_zero_3p1.md:20-41`). La orbita coescalada con `lambda` y sector fijos prueba igualdad de todas las leyes `fixed_n`, mientras `ell_eff` queda explicitamente como unidad condicional de scoring (`op12_tv_zero_3p1.md:43-98`). Las leyes intended/generated y el descuento de sus errores TV estan correctamente separados en OP-1.3 (`op13_positive_evidence_protocol.md:32-77,118-135`).
- Caveats: **REVISE_BEFORE_ADOPTION.** Los ocho bloqueos de decision 027 estan sustancialmente incorporados, pero quedan dos defectos de tipo en el blob exacto. Primero, `g^-=D_*(g^+)` no fija inequivocamente la orientacion: debe escribirse `T^-=-D_*T^+` y, por tanto, `x prec^+ y iff Dy prec^- Dx`; la frase posterior sobre “pullback ... con signo invertido” no basta para demostrar `Law(Dg)=d_#Law(g)` (`op11_spherical_dual_target.md:65-103,159-181`). Segundo, las ecuaciones `c_hat(P^op)=-c_hat(P)` y `Chi_hat(P^op)=-Chi_hat(P)` aplican negacion a `ABSTAIN`, operacion no definida en sus codominios (`op11_spherical_dual_target.md:183-202`). Debe congelarse una involucion de salida que intercambie `+1/-1` y fije `0` y `ABSTAIN`; eso hace ademas bien tipada la abstencion autodual. Como ajuste menor, `ell_eff(n;g)` debe restringirse a `n>=1` (`op12_tv_zero_3p1.md:92-98`). OP-1.3 si cierra intended/generated, IID, provenance, manifest, interrupcion y `TARGET_WITNESS_MISMATCH` como esquema condicional (`op13_positive_evidence_protocol.md:32-77,79-135,137-205`). Recomendacion: corregir esas dos ecuaciones de OP-1.1 y el dominio de `ell_eff`; hasta entonces los blobs exactos no califican para `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.

### Mathematical logic brief
- Formal status: OP-1.1 now gives typed definitions of the model, positive measure, ambient causal restriction, pointwise trapping field, sector character, outputs and losses; `DUAL_FAMILY_CLOSED` is a paper-level documentary theorem, not estimator existence or a Lean theorem (`research_program/synthesis/op11_spherical_dual_target.md:65-92`, `:114-157`, `:183-229`, `:255-265`). OP-1.2 proves a sufficient coupling lemma and two scoped consequences: equality of every fixed-`n` law along the mass-scaling orbit and `TV=0 iff M=M'` in `order+number` with fixed known `rho>0`; the general converse and asymptotic equivalence remain open (`research_program/synthesis/op12_tv_zero_3p1.md:20-76`, `:100-118`, `:135-176`). OP-1.3 proves a conditional fixed-sample certificate schema; it does not instantiate a generator, witness, sequential boundary or scientific result (`research_program/work_packages/op13_positive_evidence_protocol.md:8-77`, `:137-157`, `:199-206`).
- Quantifier / dependency order: OP-1.1 fixes patch, time orientation, positive sampling measure and ambient causal relation before defining either observed channel or scoring (`research_program/synthesis/op11_spherical_dual_target.md:28-92`, `:159-181`). OP-1.2 now quantifies causal preservation under `mu_g tensor mu_g` on conull representatives before coupling any finite iid sample; sector and `lambda` are fixed before mass varies (`research_program/synthesis/op12_tv_zero_3p1.md:20-41`, `:43-76`). OP-1.3 correctly chooses intended/generated laws, witness hash, iid sample sizes, alpha allocation and deterministic generator-TV bounds before confirmation; adaptive selection is confined to development and requires complete search provenance without embedding-guided promotion (`research_program/work_packages/op13_positive_evidence_protocol.md:32-74`, `:79-104`, `:118-135`).
- Equivalence claims: `D^2=id` and closure are definitional; dual-law covariance follows conditionally from the stated isometry, positive-measure pushforward and reversal of the frozen ambient causal relation (`research_program/synthesis/op11_spherical_dual_target.md:54-92`, `:159-181`). OP-1.2 uses only the forward coupling implication and explicitly rejects its general converse (`research_program/synthesis/op12_tv_zero_3p1.md:20-41`). Its fixed-`n` equality is scoped to fixed sector and co-scaled `lambda`, while the Poisson iff is scoped to fixed `lambda`, sector and known `rho>0`; neither is exported to arbitrary 3+1D geometries (`research_program/synthesis/op12_tv_zero_3p1.md:43-76`, `:100-118`, `:135-176`). OP-1.3's Hoeffding radii give failure at most `alpha_j/2` per two-sided mean interval, hence at most `alpha_j` per cell and `alpha_total` jointly; subtracting the two deterministic generator-TV errors validly transports the generated-law expectation gap to a lower bound for `TV(P_j,Q_j)` (`research_program/work_packages/op13_positive_evidence_protocol.md:32-74`).
- Type / object discipline: The eight prior type blockers are closed. OP-1.1 separates the positive measure from the oriented four-form and ambient causality from internal-patch causality (`research_program/synthesis/op11_spherical_dual_target.md:65-92`); separates pointwise `c_g`/`c_hat_P` from scalar `Chi`/`Chi_hat` (`:130-153`, `:183-202`); and defines an element-band loss for `H_hat` with empty-class and empty-interface terminals (`:207-229`). OP-1.2 uses a bimeasurable mod-null map, product-measure quantification, `ell_eff` as scoring-only rather than observed density, and forbids sector character on the dual quotient (`research_program/synthesis/op12_tv_zero_3p1.md:20-41`, `:78-98`, `:120-133`). OP-1.3 distinguishes intended laws, generated laws, iid samples and their respective expectations before applying coverage (`research_program/work_packages/op13_positive_evidence_protocol.md:32-74`).
- Caveats:
  - **Recommendation: `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING`.** The revised hashes close decision 027's eight blockers and the three author terminals are deserved at their explicitly narrow documentary/conditional level. Final `PHASE_1_THEORY_READY` still requires the independent bibliography/mathematics, committee and auditor gates required by the plan (`docs/plan_operativo_15_julio_2026.md:293-304`).
  - `POSITIVE_EVIDENCE_PROTOCOL_PROVED` denotes only the conditional fixed-sample schema; the document correctly leaves every concrete generator/witness choice unauthorized and `IMPLEMENTATION_READINESS` pending (`research_program/work_packages/op13_positive_evidence_protocol.md:186-206`).
  - Before implementation, define the lifted sign operation on abstention explicitly, e.g. `-ABSTAIN=ABSTAIN`, or restrict the dual equations to non-abstaining outputs; unary minus is currently written over codomains containing `ABSTAIN` without that convention (`research_program/synthesis/op11_spherical_dual_target.md:183-202`). This does not invalidate `DUAL_FAMILY_CLOSED`, which claims no estimator exists.
  - The auditor should verify terminal completeness: OP-1.1 defines `TARGET_NOT_SPECIFIABLE` outside its displayed precedence chain, and OP-1.3 explicitly orders manifest/interruption above scientific terminals but does not present a total order over every contract failure (`research_program/synthesis/op11_spherical_dual_target.md:231-253`; `research_program/work_packages/op13_positive_evidence_protocol.md:172-197`). These are reporting refinements, not failures of the three proved author terminals.
  - Missing local primary snapshots are now marked `[UNVERIFIED_*]` rather than silently treated as proved sources (`research_program/synthesis/op11_spherical_dual_target.md:267-275`; `research_program/synthesis/op12_tv_zero_3p1.md:178-188`; `research_program/work_packages/op13_positive_evidence_protocol.md:208-216`). No 3+1D recovery, reconstruction or execution claim follows.

### Physicist brief
- Coordinates & patch: OP-1.1 usa correctamente Kruskal adimensional `(U,V,omega)` con `-UV=(r/2M-1)e^{r/2M}` y la metrica Schwarzschild 3+1D (`research_program/synthesis/op11_spherical_dual_target.md:21-26`; convencion local compatible en `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562`). El patch BH mantiene `V>0`, cruza `U=0`, contiene `S^2` completas y satisface `UV<=1-epsilon_s`; excluye singularidad, bifurcation sphere y regiones asintoticas (`op11_spherical_dual_target.md:28-63`). La causalidad ambiente de Schwarzschild maximal restringida a pares del patch queda ahora congelada, diferenciandola correctamente de causalidad interna al patch (`op11_spherical_dual_target.md:65-75`). La finitud impide cualquier claim de horizonte de eventos global o convergencia asintotica.
- Physical meaning of the signal: Para una esfera de simetria, `theta_k=(2/r)k(r)` es la expansion correcta porque su area es proporcional a `r^2`; su signo no depende de reescalar positivamente el normal nulo (`op11_spherical_dual_target.md:94-112`). En Schwarzschild, la expansion outgoing cambia de signo en `r=2M`, mientras la ingoing permanece negativa en el sector BH (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:197-225`). Por ello `h_M`, `y_g` y el campo `c_g` son targets de scoring fisicamente coherentes dentro de la familia esferica congelada (`op11_spherical_dual_target.md:114-157`). La separacion entre campo puntual `c_g` y etiqueta sectorial `Chi(g)` corrige el error anterior. `L_H` puntua localizacion a resolucion finita mediante una shell, no hits exactos sobre una superficie de medida cero; sus denominadores y abstenciones de clase vacia estan especificados (`op11_spherical_dual_target.md:207-229`).
- Sprinkling domain: Los dos experimentos estan bien separados: IID de la medida positiva normalizada en `fixed_n`, y PPP de intensidad `rho mu_g` con `rho` conocida en `order+number` (`op11_spherical_dual_target.md:159-181`). La distincion entre medida positiva `mu=|dVol|` y 4-forma orientada esta ahora correcta: `D` preserva la primera y revierte la segunda (`op11_spherical_dual_target.md:65-92`). No hay niveles de `n`, intensidad, generador ni predicado causal implementado; por tanto el documento solo define leyes continuas y no autoriza sprinkling, simulacion ni consumo de seeds.
- Claim boundary: El paquete puede afirmar unicamente cierre documental de una familia Schwarzschild maximal esferica, degeneracion fixed-n en la orbita coescalada y un esquema condicional de evidencia positiva. No demuestra que exista `H_hat`, `c_hat` o `Chi_hat`, ni recovery 3+1D, reconstruccion metrica o horizonte global (`op11_spherical_dual_target.md:255-265`; `research_program/synthesis/op12_tv_zero_3p1.md:135-176`; `research_program/work_packages/op13_positive_evidence_protocol.md:159-205`). El diagnostico longest-chain/future-cardinality de EGS depende de singularidad y borde y no se transfiere a agujeros negros regulares (`biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-199`, `:463-469`). El target por expansiones puede motivar trabajo futuro regular, pero este contrato esta restringido a Schwarzschild maximal: `NO_RECONSTRUCTION_CLAIM`.
- Caveats: **Recomendacion: `REVISE_BEFORE_AUDIT` con dos correcciones tipograficas-fisicas obligatorias.** La objecion sobre orientacion es valida. Si `T^+` representa el futuro BH y se quiere que `D` revierta la relacion causal, debe escribirse literalmente `T^-=-D_*T^+` y `x prec^+ y iff D(y) prec^- D(x)`. La notacion actual `g^-=D_*(g^+)` sugiere el pushforward ordinario `T^-=D_*T^+`, que haria a `D` time-orientation preserving y transportaria el orden sin dualizarlo; la prosa posterior no elimina esa ambiguedad (`op11_spherical_dual_target.md:65-103`, `:173-180`). Ademas, las ecuaciones `c_hat(P^op)=-c_hat(P)` y `Chi_hat(P^op)=-Chi_hat(P)` aplican signo a codominios que incluyen `ABSTAIN`; debe definirse una involucion `nu` con `nu(-1)=+1`, `nu(+1)=-1`, `nu(0)=0` y `nu(ABSTAIN)=ABSTAIN`, y usarla en ambas salidas (`op11_spherical_dual_target.md:183-202`). Con esas dos reparaciones, medida, patch, expansiones, tipos `c/Chi` y `L_H` quedan fisicamente aptos para reconvocatoria y posterior auditoria.

## 5. Falsifier attack

### Falsifier attack
- Concrete failure modes: **BLOCK** sobre los tres hashes actuales. OP-1.1 no define literalmente `T^-=-D_*T^+` ni `x prec^+ y iff D(y) prec^- D(x)`; por tanto, la igualdad de leyes bajo dualizacion no queda derivada de una convencion inequivoca. Ademas, `-ABSTAIN` no esta definido en los contratos de `c_hat` y `Chi_hat`; hace falta una involucion total `nu` que fije `0` y `ABSTAIN`. OP-1.2 usa `ell_eff=(mu(K)/n)^(1/4)` dentro de una discusion que incluye `n=0`; la escala solo existe para `n>=1`.
- Ground-truth leakage: OP-1.3 cierra razonablemente la fuga de embedding, pero permitir que la seleccion consuma la identidad del generador permite optimizar un separador supervisado entre alternativas. Eso es admisible para una cota inferior de TV, no convierte al testigo en localizador de horizonte. Cualquier promocion posterior debe conservar obligatoriamente `TARGET_WITNESS_MISMATCH` cuando el testigo no tenga interpretacion de atrapamiento order-only (`research_program/work_packages/op13_positive_evidence_protocol.md:79-104`, `:159-170`).
- Freeze violations: no hay todavia ejecucion ni freeze roto, pero tampoco estan congelados los hiperparametros cientificos del futuro ensayo: banda `delta_H`, familia de testigos, regla de abstencion, presupuesto de seleccion y multiplicidad. Los textos solo autorizan una especificacion candidata, no una corrida.
- Verdict coercion: OP-1.1 tipa `H_hat` como subconjunto, pero transforma automaticamente `H_hat=empty` en abstencion antes de puntuar. Asi, prediccion vacia y abstencion etiquetada son indistinguibles y un estimador siempre vacio puede evitar un falso negativo. Debe usarse un tipo suma `P(S) union {ABSTAIN}` y reportar la tasa de abstencion. Ademas, las precedencias no forman un orden total: `TARGET_NOT_SPECIFIABLE` queda fuera de la cadena de OP-1.1, y OP-1.3 no ordena deterministamente fallos simultaneos como `ADAPTIVE_SELECTION_UNCONTROLLED`, `FAILED_DEVELOPMENT_PROVENANCE` y `GENERATOR_ERROR_NOT_BOUNDED`.
- Premature / over-broad claims: OP-1.2 esta correctamente restringido a la familia y sector congelados; OP-1.3 declara un teorema condicional y no recuperacion. El unico exceso actual es tratar la dualidad de leyes de OP-1.1 como cerrada antes de fijar las ecuaciones de orientacion y hacer total la accion sobre las salidas.
- Independent-falsification gate: **NOT SATISFIED**. Los bloqueos de orientacion, involucion total y dominio `n>=1` son reproducibles directamente en los blobs auditados. Antes de ejecucion anadiria tambien la separacion tipada entre interfaz vacia y abstencion, y una prioridad total de terminales.
- Minimal falsification test: el agente devolvio un test contra paths `research_program/theory/*` que no existen. El chair sustituye esos anchors por los paths reales en section 9; el hallazgo sustantivo permanece reproducible.

## 6. Pre-registration verdict

### Pre-registration verdict
- Verdict: BLOCK
- Freeze status: No numerical threshold, concrete family instance, witness, seed band or confirmatory grid is frozen by these theory drafts. OP-1.1 explicitly defers candidate-loss parameters to a later pre-inference freeze (`research_program/synthesis/op11_spherical_dual_target.md:207-229`), and OP-1.3 requires the complete laws, witness hash, sample sizes, alpha budget and deterministic generator-error bounds before confirmation (`research_program/work_packages/op13_positive_evidence_protocol.md:32-74`, `:118-135`). The three exact blobs remain revisable theory candidates, not an implementation preregistration.
- Seal integrity: No sealed validation path is run or modified. OP-1.1 and OP-1.2 remain theory drafts, while OP-1.3 explicitly states `NO_EXECUTION_AUTHORIZED` (`research_program/synthesis/op11_spherical_dual_target.md:1-17`; `research_program/synthesis/op12_tv_zero_3p1.md:1-18`; `research_program/work_packages/op13_positive_evidence_protocol.md:1-6`). The operative 1+1D seal remains `6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4` (`docs/preregistration_002.md:7-12`).
- Seed discipline: No seed is consumed. OP-1.3 requires development/confirmation separation, a single independent confirmatory evaluation, complete development provenance and an exhaustive pre-run manifest before any confirmatory seed is touched (`research_program/work_packages/op13_positive_evidence_protocol.md:79-104`, `:131-135`).
- Reporting rule: Report `BLOCK / REVISE_BEFORE_AUDIT`; do not promote the package to `THEORY_COMMITTEE_ADOPTED_AUDIT_PENDING` or combine its author terminals into `PHASE_1_THEORY_READY`. Decision 027 forbids `/auditor` until the reconvened committee returns a proceed verdict and leaves commit, push and scientific execution unauthorized (`docs/comite/comite_decision_027_phase1-theory-package-first-review.md:148-164`, `:170-177`).
- Forbidden moves present? No post-hoc tuning, threshold loosening, seed reuse, validation rerun, ground-truth leakage or reconstruction claim occurred. Sending the known ill-typed dual-output contract to audit as committee-adopted would prematurely freeze ambiguities that can affect abstention and BH/WH reporting.
- Reasons:
  - The time-orientation transport is described partly as `g^-=D_*(g^+)` and partly as a pullback with an additional sign, but no single typed identity such as `T^-=-D_*T^+` is frozen (`research_program/synthesis/op11_spherical_dual_target.md:65-92`, `:94-103`). The corresponding causal reversal is asserted in prose without the pointwise iff defining `prec^-` from `prec^+`, yet that reversal is used to claim the observed-law pushforward (`research_program/synthesis/op11_spherical_dual_target.md:159-181`).
  - Both `c_hat` and `Chi_hat` have codomains containing `ABSTAIN`, while their dual equations apply unary minus to the whole output. Since `-ABSTAIN` is undefined, the equations are not total functions on their declared codomains; define the lifted involution explicitly or condition the equations on non-abstention (`research_program/synthesis/op11_spherical_dual_target.md:183-202`).
  - `CHARACTER_ABSTAIN_SELF_DUAL` relies precisely on that missing lifted action. Until it is typed, a self-dual realization has no formally defined route from anti-equivariance to abstention (`research_program/synthesis/op11_spherical_dual_target.md:231-253`).
  - OP-1.2 quantifies fixed-`n` equality for every `n>=0`, but later defines `ell_eff(n;g)=(mu_g(K_g)/n)^(1/4)`, which is undefined at `n=0`. Restrict the scoring-scale statement to `n>=1`; this does not alter the valid all-`n` law equality (`research_program/synthesis/op12_tv_zero_3p1.md:8-15`, `:67-98`).
  - OP-1.1 also emits `TARGET_NOT_SPECIFIABLE` without placing it in the displayed terminal precedence. The revised contract should locate it before any scoring or scientific terminal so angular-target failure cannot be coerced into another outcome (`research_program/synthesis/op11_spherical_dual_target.md:231-253`).
  - These are documentary type and reporting repairs only. The fixed-sample Hoeffding transport from generated laws to intended laws is now correctly specified and does not require new data (`research_program/work_packages/op13_positive_evidence_protocol.md:32-74`); it is not a reason to touch the seal or consume seeds.

## 7. Literature verdict

### Literature verdict
| Citation | Claimed by | Status |
| --- | --- | --- |
| Bombelli, *Space-time as a causal set*, §2.1, Eq. (2.1.3), `biblioteca/derived-md/Bombelli_1987_PhD.md:402-407` | OP-1.1 — causal-set time reversal is order duality, with every arrow reversed | CONFIRMED |
| Kruskal metric and implicit radius relation, Eqs. (3.8)-(3.9), `biblioteca/derived-md/Causal Sets, a Possible Interpretation.md:2550-2562` | OP-1.1 — `UV` determines `r`; `D(U,V)=(-V,-U)` preserves `UV`, `r` and the metric coefficient | CONFIRMED |
| Bombelli Eq. (2.1.3) plus the temporally oriented model in `research_program/synthesis/op11_spherical_dual_target.md:65-103` | Committee objection — an anti-time-orienting `D` requires `T^-=-D_*T^+` and then `x prec^+ y iff D(y) prec^- D(x)` | CONFIRMED |
| Current notation `g^-=D_*(g^+)` and dual-law claim, `research_program/synthesis/op11_spherical_dual_target.md:77-92`, `:173-180` | OP-1.1 — the present typed tuple already establishes order reversal and `Law_K(Dg)=d_#Law_K(g)` without an additional sign convention | UNCONFIRMED |
| Direct Jacobian of `D(U,V,omega)=(-V,-U,omega)` together with the Kruskal metric above | OP-1.1 — `D` preserves the positive measure `|dVol|` but reverses the signed four-form | CONFIRMED |
| Eichhorn-Gamito-Stokes, §IV, Eqs. (10)-(12), `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:197-230` | OP-1.1 — trapped spheres have both future expansions negative; Schwarzschild outgoing expansion vanishes and changes sign at `r=2M` | CONFIRMED |
| Eichhorn-Gamito-Stokes, Eq. (12), plus time reversal | OP-1.1 — the WH field is anti-trapped and satisfies `c_{Dg}(Dx)=-c_g(x)` | UNCONFIRMED |
| Eichhorn-Gamito-Stokes, §§III-IV and conclusions, `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:181-230`, `:463-480` | OP-1.1 — longest-chain/future-cardinality is singularity/boundary dependent; 1+1D lacks true two-surface expansion; regular BHs require a different diagnostic | CONFIRMED |
| Kruskal metric above and four-dimensional conformal scaling | OP-1.2 — with dimensionless patch fixed, `g_{M'}=a^2g_M`, positive volume scales as `a^4`, and normalized fixed-`n` laws coincide | CONFIRMED |
| He-Rideout, sprinkling definition and Poisson count, `biblioteca/derived-md/A Causal Set Black Hole_ arXiv0811.4235.md:50-60` | OP-1.2 — known `rho` and volume proportional to `M^4` distinguish unequal masses through the marginal law of `N` | CONFIRMED |
| Surya, HKMM theorem, `biblioteca/derived-md/The causal set approach to quantum gravity.md:329-352` | OP-1.2 — HKMM assumes a causal/chronological bijection and does not derive it from equality of sampled-poset laws | CONFIRMED |
| Janson, arXiv:0902.0306 | OP-1.2 — finite-poset-law equality yields only weak kernel equivalences, not the strong continuum converse | UNVERIFIED |
| Hoeffding, JASA 58 (1963) | OP-1.3 — `sqrt(log(4/alpha_j)/(2m))` gives two-sided failure `alpha_j/2` per mean and the stated Bonferroni coverage | UNVERIFIED |
| Howard et al., arXiv:1810.08240 | OP-1.3 — optional stopping requires a time-uniform confidence sequence | UNVERIFIED |
| Ashtekar-Krishnan, arXiv:gr-qc/0407042 | OP-1.1 — quasi-local horizon target via null expansions | UNVERIFIED |

- Notes: La formulacion fisica correcta es `T^-=-D_*T^+`. Con `T^-=D_*T^+`, `D` transportaria curvas futuras a curvas futuras y preservaria el orden; con el signo menos, las transporta a curvas pasadas y produce exactamente el orden opuesto confirmado por Bombelli. El borrador expresa la inversion en prosa (`op11_spherical_dual_target.md:98-103`), pero `g^-=D_*(g^+)` (`:82`) conserva la lectura estandar incompatible; por ello `Law_K(Dg)=d_#Law_K(g)` queda sobreafirmado hasta escribir literalmente el signo y la equivalencia causal. La ley WH de signos es una deduccion valida una vez fijada esa orientacion, pero EGS no la demuestra directamente. Asimismo, la literatura no puede dar significado a `-ABSTAIN`; las ecuaciones duales deben usar una involucion que intercambie `+1/-1` y fije `0/ABSTAIN` (`op11_spherical_dual_target.md:183-202`). La formula Hoeffding es algebraicamente consistente con la desigualdad estandar: `2 exp(-2mr^2)=alpha_j/2` por media y la union de dos medias cuesta `alpha_j`; permanece `UNVERIFIED` bibliograficamente porque no hay snapshot local, tal como declara el borrador. No detecto otro overclaim de medida, trapping o scaling. Recomendacion: `REVISE_BEFORE_AUDIT` unicamente para cerrar orientacion/orden y la involucion de outputs; las fuentes ausentes estan honestamente marcadas como no verificadas.

## 8. Synthesis

The package remains blocked before audit. Reproducibility and logic consider decision 027's eight
items substantially closed, but the mathematician, physicist, falsifier, preregistration warden and
literature verifier agree that the dual-law claim is not yet fully typed. This dissent is
load-bearing and cannot be hidden.

The remaining mandatory corrections are:

1. replace the ambiguous tuple transport with `T^-=-D_*T^+` and freeze
   `x prec^+ y iff D(y) prec^- D(x)`;
2. define a total involution `nu` on `{ -1,0,+1,ABSTAIN }` that swaps signs and fixes `0,ABSTAIN`,
   then use `nu` in both dual output equations;
3. type `H_hat` as `P(S) union {ABSTAIN}` so an empty prediction is scored rather than silently
   converted to abstention, and record abstention rate separately;
4. restrict `ell_eff(n;g)` to `n>=1` without changing the all-`n` equality theorem;
5. put `TARGET_NOT_SPECIFIABLE` into OP-1.1's displayed precedence and give OP-1.3 a deterministic
   precedence for simultaneous contract failures.

These are documentary type/reporting repairs. OP-1.2's scoped TV result and OP-1.3's conditional
certificate survive. No source, seal or scientific run needs to change.

## 9. Next-step spec

**Reversible step requiring PI sign-off:** apply only the five corrections in section 8, recompute
the three hashes and reconvene `/comite`. Do not run `/auditor` until a proceed verdict. Do not add
code, tests, simulations, data, concrete witnesses, thresholds or seeds.

Correct-path minimal falsification test:

```text
rg -q 'T\^-.*=.*-D_\*T\^\+' research_program/synthesis/op11_spherical_dual_target.md
rg -q 'nu(ABSTAIN).*ABSTAIN' research_program/synthesis/op11_spherical_dual_target.md
rg -q 'n>=1' research_program/synthesis/op12_tv_zero_3p1.md
```

The next committee must also verify empty prediction versus abstention and total terminal
precedence. Commit, push and scientific execution remain unauthorized.

## 10. Verdict

COMMITTEE_DECISION_VERDICT=RECOMMEND_REVISE_AND_RECONVENE

## 11. User sign-off

Signed: Nacho / PI

Date: 2026-07-15

Decision: authorize the five reversible corrections in committee decision 028 section 8,
reconvene on the revised hashes, and do not run auditor, code, or simulations.
