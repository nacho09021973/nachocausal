# Fase 3 B2 — decisión terminal sobre \(Q_{\mathrm{FMOTS}}\) y disposición de la línea

> **STATUS: DIRECTOR_DECISION_UNDER_PI_DELEGATION / WORK_DATE_2026-07-29 / NOT_A_COMITE_ACTA /
> EMITS_CONTRACT_S9_TERMINAL / DOES_NOT_ADOPT_ANY_TARGET / WITNESS_PAIR_NOT_CONSTRUCTED /
> NO_CODE / NO_SIMULATION / NO_SEEDS / SEALED_PATH_UNTOUCHED / COMITE_NOT_RECONVENED_THIS_SESSION.**

## 0. Autoridad y alcance

El PI delegó en esta sesión (2026-07-29) la decisión completa sobre el estado de Fase 3 B2, con
instrucción explícita de decidir y ejecutar de principio a fin ("actúa como director científico con
plena autonomía… Decide tú completamente qué conviene hacer ahora… Ejecuta tu decisión de principio
a fin usando la estructura existente y dejando evidencia verificable"). Esta delegación cubre los
actos que los documentos anteriores reservaban al PI (emisión del terminal §9, disposición del
target, versionado); los guardarraíles científicos del proyecto (`CLAUDE.md`, sello, separación
dev/validación) no son delegables y permanecen intactos.

Este documento hace exactamente cuatro cosas: (1) deja constancia del versionado del expediente
pendiente; (2) emite el terminal único del contrato §9 para \(Q_{\mathrm{FMOTS}}(g,U)\);
(3) dispone el fork \(Q_{\mathrm{end}}\); (4) ordena la preparación de un contrato de preapertura
v2 para un target sustituto, sin adoptarlo. No adopta ningún target, no construye pares testigo,
no escribe código, no ejecuta simulaciones, no reserva semillas, no toca el sello y no reconvoca
al comité en esta sesión.

## 1. Estado verificado (esta sesión)

- `make verify-seal` → `thresholds.py sha256: 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`,
  coincidente con `docs/preregistration_002.md:7-12`. Verificado antes de redactar este documento.
- Rama `agent/phase3-b2-decision-048`; HEAD previo a esta sesión =
  `5924b6b74d0e77b86e9334446110657d957cf7ca`; `origin/main` =
  `29f84357ae7c5e6b8eb4d2afc1ce75949c3b190f`. PR #1 (`agent/phase2-b2-documentation` → `main`)
  sigue `OPEN`, `DRAFT`, sin tocar.
- Blob SHA del contrato v1 en HEAD
  (`git rev-parse HEAD:research_program/work_packages/phase3_b2_witness_pair_preopening_contract.md`)
  = `c7512a7f0bfb8757a5db2a78a20720bf0a8b882d` — **idéntico al blob adjudicado por la Decisión 048**
  (`docs/comite/comite_decision_048_q-fmots-target-adjudication.md:37-39`). El contrato no ha sido
  editado entre la adjudicación y esta decisión; los gates G1–G9 calificados por el comité y el
  terminal emitido abajo se refieren al mismo texto.
- Blob SHA del acta 048 = `a9e2074b404a723d39016bb7e8107f314e99becf`; de la revisión de condiciones
  = `16257002b9796f8360e515d01ac63c123c308e11` (commit `5924b6b`); del expediente de extremo
  asintótico = `6c3228beff9f38f4169d261e6284863bb2313cdd` (commit `edd6bb6`, versionado como primer
  acto de esta decisión).

## 2. Terminal emitido para \(Q_{\mathrm{FMOTS}}(g,U)\)

```text
TERMINAL = B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL
CLASSIFICATION = FATAL_FOR_CURRENT_TARGET, NOT_UNIVERSAL_NO_GO
ADJUDICATED_CONTRACT_BLOB = c7512a7f0bfb8757a5db2a78a20720bf0a8b882d
```

### Fundamento

1. **La regla ya estaba escrita.** El contrato §2.2
   (`phase3_b2_witness_pair_preopening_contract.md:71-77`) tipifica exactamente este modo de fallo:
   "Si esto no puede hacerse sin importar una etiqueta externa, se emite
   `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`". La Decisión 048 §6 (custodio de prerregistro)
   registró como requisito vinculante que, con G1 abierto y sin enmienda del §2.1, "el terminal
   fiel per la propia lista de precedencia de §9 es `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`",
   y el falsificador (§5) coincidió. Emitir este terminal no es una decisión de frontera nueva:
   es ejecutar la regla de precedencia que el comité dejó registrada, ahora con evidencia más
   fuerte que la que el comité tenía.

2. **La evidencia posterior a 048 convirtió "abierto" en "obstruido".**
   - La vía "borde de región compacta \(\Omega\)" — única candidata identificada que proveía el
     dato transversal necesario — quedó `REFUTED` por el test falsificador \(S^3\)
     (`phase3_b2_decision048_conditions_review.md`, Condición 1): una isometría propia y ortócrona
     \(\psi\) de \((g,U)\) deja \(S\) invariante como conjunto e intercambia las dos presentaciones
     admisibles, de modo que \((g,U)\) solo no fija la coorientación cuando la topología de
     \(\Sigma\) no privilegia un lado.
   - El atajo "libre de orientación" no evita el problema, lo reubica (mismo documento, hallazgo
     negativo): distinguir un MOTS exterior genuino de una configuración interior con papeles
     cambiados requiere datos transversales que no viven en \((g,S)\) puntualmente.
   - La mejor reparación restante — restricción a extremo asintótico único — recibió veredicto
     `REQUIRES_TARGET_CHANGE` (`phase3_b2_asymptotic_end_restriction_review.md` §4): hecha precisa,
     colapsa en la Ruta A (información exterior a \(U\): define \(Q_{\mathrm{end}}(N,g,U;e)\), otro
     target con otra firma) o en la Ruta B (la componente distinguida de \(\partial U\) que ya se
     había descartado como "etiqueta hacia el borde artificial de observación").

3. **Precedencia.** `B2_BLOCKED_TARGET_NOT_INTRINSIC` antecede en la lista §9, pero el contrato
   §2.2 asigna explícitamente este modo de fallo concreto (cierre de \(S_{\rm adm}\) imposible sin
   etiqueta externa) al terminal `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`; se sigue la tipificación
   del propio contrato, que es la más específica.

### Qué cierra y qué no cierra

Per contrato §10: "Un bloqueo documentado de este target no refuta B2 en general y no prueba
identificabilidad. Solo cierra esta instanciación." Concretamente:

- **Cierra:** \(Q_{\mathrm{FMOTS}}(g,U)\) tal como está definido en el contrato §2.1 (blob
  `c7512a7f…`), con "exterior" pendiente de selector intrínseco, deja de ser candidato a adopción.
  Las cinco condiciones de la Decisión 048 §9 quedan sin efecto respecto de este target (su tabla
  de estado final: 1 `OPEN`-obstruida, 2 `CLOSED` con caveat permanente, 3 `OPEN`, 4 `OPEN`,
  5 `PARTIAL` — ver `phase3_b2_decision048_conditions_review.md`, síntesis).
- **No cierra:** la rama B2 (dos-puntos sobre target continuo cuasi-local), la técnica conforme,
  los Lemas 1–2 (normalización irrelevante; covariancia por difeomorfismos — reutilizables tal
  cual), la relación con Müller Thm 2 (Condición 2, cerrada con caveat permanente de
  "instanciación acotada, no método nuevo", que se hereda a cualquier target sucesor), ni la
  posibilidad de que exista alguna definición intrínseca de "exterior" no considerada — no se
  probó un no-go universal y este documento no lo afirma.

### Valor científico del bloqueo (registro, no claim)

La obstrucción documentada tiene la misma forma que el tema central del programa de consolidación:
la estructura orientada de horizonte ("cuál lado es exterior") no queda fijada por los datos
declarados del parche compacto — requiere datos transversales, de borde o de extensión ambiente.
Es complementaria (por analogía estructural, no por corolario — ver
`phase3_b2_asymptotic_end_restriction_review.md` §3) al Teorema 3.2 del manuscrito
(`docs/manuscript_limits_draft.md:455-483`, no-medibilidad de \(T_{\rm EH}\) en parche finito).
Se registra como **candidato a sección/observación del track de consolidación** (manuscrito de
límites o synthesis del research program); su incorporación al manuscrito es un acto editorial
separado, no ejecutado aquí.

## 3. Disposición del fork \(Q_{\mathrm{end}}(N,g,U;e)\)

```text
Q_END_DISPOSITION = COHERENT_NOT_PURSUED
```

La Ruta A es matemáticamente coherente y la más limpia de las tres candidatas evaluadas
(`phase3_b2_asymptotic_end_restriction_review.md` §4), pero no se adopta ni se prepara contrato
para ella, por dos razones:

1. **Renuncia a la promesa central de B2.** El contrato §2.3 define el valor del target por
   contraste con \(T_{\rm EH}\): evaluable desde el parche declarado. \(Q_{\mathrm{end}}\) requiere
   la extensión ambiente \(N\) y su extremo como datos declarados no derivables de \((g,U)\) —
   el mismo *tipo* de obstrucción por información exterior al parche que motivó evitar
   \(T_{\rm EH}\) (analogía estructural, no equivalencia). Adoptarlo debilitaría el punto del
   benchmark en lugar de responderlo.
2. **Existe una alternativa que conserva la promesa.** El target sustituto de §4 es cuasi-local
   en sentido estricto (funcional de \((g,U)\) solo) y esquiva la obstrucción por construcción.
   Mientras esa vía no se agote, \(Q_{\mathrm{end}}\) es dominado.

El expediente queda versionado (`edd6bb6`) como registro de que la vía existe, es coherente, y
podría retomarse con contrato propio si la vía simétrica fallara en su adjudicación.

## 4. Disposición de la línea B2 — target sustituto y contrato v2

```text
B2_LINE = CONTINUES_UNDER_SUBSTITUTED_TARGET_CANDIDATE
CANDIDATE = Q_trap (existencia de superficie atrapada cerrada, forma simétrica)
CONTRACT_V2 = research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md
TARGET_ADOPTION = PENDING_SCIENTIFIC_ADJUDICATION (comité futuro, sesión independiente)
```

Se ordena la preparación (en esta misma sesión, como documento separado) del contrato de
preapertura v2 para

\[
Q_{\mathrm{trap}}(g,U)
=
\mathbf 1\!\left\{
\exists S\in\mathcal S_{\mathrm{adm}}(g,U):
\theta(\ell^{(1)}_S)<0\ \wedge\ \theta(\ell^{(2)}_S)<0
\right\},
\]

donde \(\ell^{(1)},\ell^{(2)}\) son las dos direcciones nulas futuras normales a \(S\), **sin
elegir cuál es exterior**. Razones de la elección, frente a las alternativas consideradas:

1. **La obstrucción probada no le aplica, por construcción.** La condición definitoria es
   invariante bajo el intercambio \(\ell^{(1)}\leftrightarrow\ell^{(2)}\): no existe selector de
   coorientación que fijar, luego el test falsificador \(S^3\) (que refuta selectores, no
   condiciones simétricas) no lo alcanza. Por el Lema 1 la condición es independiente de la
   normalización; por el Lema 2, difeomorfismo-invariante. Ambos lemas se reutilizan sin cambio.
2. **Mejor que la variante marginal simétrica.** La forma marginal (\(\theta^{(i)}\equiv0,\
   \theta^{(j)}<0\)) ya fue examinada y hereda el problema semántico interior/exterior
   (`phase3_b2_decision048_conditions_review.md`, hallazgo negativo). La forma estrictamente
   atrapada no distingue — ni necesita distinguir — orientaciones; además es una condición
   abierta (desigualdades estrictas), mejor adaptada a una construcción perturbativa que una
   igualdad exacta \(\theta\equiv0\).
3. **Pedigrí físico.** "Superficie atrapada cerrada" es la hipótesis clásica de los teoremas de
   singularidad (Penrose), definida en la literatura estándar sin referencia a infinito ni a
   orientación exterior. `[UNVERIFIED against biblioteca — la biblioteca del proyecto es de
   conjuntos causales, no de relatividad matemática; el anclaje primario es obligación del
   contrato v2, no de este documento.]`
4. **Precio declarado, no escondido.** \(Q_{\mathrm{trap}}\) detecta presencia de región atrapada
   en el parche, no "el horizonte exterior": pierde la semántica orientada de FMOTS. En
   Schwarzschild las esferas redondas con \(r<2M\) son atrapadas
   (\(\Theta_{\rm out}<0\) para \(r<2M\), \(\Theta_{\rm in}=-2/r<0\) —
   `biblioteca/derived-md/Towards black-hole horizons and geodesic focusing in causal sets.md:221-225`),
   así que en el caso de referencia el target sí co-localiza con la región interior al horizonte;
   pero un parche cosmológico puede tener superficies atrapadas sin agujero negro, y ese riesgo de
   dilución semántica queda pre-declarado como ataque falsador en el contrato v2.

**Gobernanza de la adjudicación:** siguiendo el precedente v1 (contrato en acta 047 → adjudicación
en acta 048, sesiones separadas), el contrato v2 se redacta ahora pero **no se adjudica en esta
sesión**. El modo de fallo documentado en 048 (Wave 1 cerró G8 sobre evidencia secundaria sin leer
la fuente primaria; la maduración independiente importa) desaconseja que la misma sesión que
redacta un contrato lo adjudique. `NOT_READY_TO_RECONVENE` queda **superado, no contradicho**: se
mantenía respecto de re-adjudicar `ADOPT` para \(Q_{\mathrm{FMOTS}}\) — pregunta que este terminal
extingue — y la reconvocatoria futura tendrá una pregunta nueva y bien planteada (admisibilidad de
\(Q_{\mathrm{trap}}\) bajo el contrato v2).

## 5. Estado de autorización tras esta decisión

```text
PHASE_3_BRANCH = B2
Q_FMOTS_TERMINAL = B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL (emitido, §2)
Q_END = COHERENT_NOT_PURSUED
CANDIDATE_V2 = Q_trap — TARGET_ADOPTION = PENDING_SCIENTIFIC_ADJUDICATION
WITNESS_CONSTRUCTION = NOT_AUTHORIZED
CODE = NOT_AUTHORIZED
SIMULATION = NOT_AUTHORIZED
SEEDS = NOT_AUTHORIZED
THRESHOLDS = NOT_APPLICABLE
SEALED_PATH = UNTOUCHED (verify-seal 6e2c3888… antes y después de esta sesión)
COMITE_RECONVENE = REQUIRED_BEFORE_V2_ADOPTION (sesión independiente, dossier = contrato v2)
COMMIT_AND_PUSH = AUTHORIZED_BY_PI_DELEGATION_2026_07_29 (rama agent/phase3-b2-decision-048)
```
