---
name: program-status-reentry-marker
description: Estado vivo del programa — cerrado 2026-07-30 (deóntico) y REABIERTO ACOTADO 2026-07-31 sólo para R1 (paper de límites) y R2 (derivar λ⁶); caja de 6 semanas. Punto de reentrada — LEER PRIMERO antes de proponer cualquier paso
metadata: 
  node_type: memory
  type: project
  originSessionId: ba8e0f66-5e67-49f8-a0fa-d7165b974d41
  modified: 2026-08-19T08:02:47.601Z
---

Sustituye al marcador de pausa del 2026-07-19 (pausa → cierre → reapertura acotada).

**Cierre 2026-07-30.** `docs/program_closure_note_2026-07-30.md`, base
`docs/comite/comite_decision_049_program-closure-adjudication.md §11`, firmado por el PI, tag
`program-closed-2026-07-30` en `bcd4633`. Es **deóntico, no alético**: retira autorización para
ampliar el programa bajo su objetivo fuerte; NO afirma que no exista camino legítimo.

**Reapertura acotada 2026-07-31 (decisión del PI, confirmada por él el 2026-08-01).**
`docs/program_reopening_note_2026-07-31.md` — **vive sólo en la rama
`reopen/r1-r2-limits-writeup`, NO está en `main`** (a 2026-08-01). Estado
`REOPENED_BOUNDED / WRITE_UP_ONLY_PLUS_ONE_DERIVATION`. No revoca el cierre; restaura autorización
para **dos ítems y nada más**:
- **R1** — llevar `docs/manuscript_limits_draft.md` (~1.280 líneas, Teoremas 3.8 suelo de
  localización order-only N1 y 3.9, correcciones `R-A1`–`R-B2` aplicadas) a PDF sometible. Es
  redacción, no investigación.
- **R2** — derivar analíticamente el exponente `λ⁶` de `wp4_fisher_localization_floor.md §5a`
  (ley empírica `κ ~ λ⁶`, exponente 5.9–6.0; vía plausible: expansión near-horizon/Rindler).
  Día 1 (`91a84ac`): exponente derivado y cross-checked, **prefactor aún abierto**.

**Cajas de tiempo (duras, sin prórroga):** R1+R2 seis semanas desde 2026-07-31 → ~2026-09-11.
R2 tiene tope propio de dos semanas → ~2026-08-14; si no sale, se marca abierto y se pasa a R1.
**R2 no puede bloquear R1** (§4.4 de la nota).

**Why:** el cierre acota la prohibición al objetivo de reconstrucción de horizonte; R2 se autoriza
porque es un **límite sobre** la localización cerca del horizonte —dirección opuesta— y su diana
numérica ya existe. El PI declaró esa tensión en la propia nota en vez de disimularla.

**How to apply:**
- Perímetro fijo R1/R2. Nada entra sin nueva nota firmada. Todo hallazgo fuera de perímetro va
  fechado a `docs/backlog_hallazgos.md`, nunca al trabajo en curso.
- **Sigue cerrado:** reconstrucción de horizonte 1+1D/3+1D en cualquier reformulación; PR004;
  localizadores C1–C6; anclas de presente; ladder-braiding; diagnósticos de rescate; `Q_trap` v2
  (`UNADJUDICATED_AT_CLOSURE`, no se reconvoca); nuevos observables/WP fuera de R2; simulaciones;
  validaciones.
- **Semillas: ninguna.** La banda virgen `[2.000.000–2.999.999]` no se toca.
- **Lenguaje de novedad absoluta: prohibido** (cláusula 2 del cierre). `NOVELTY_CERTIFIED = NO`;
  `PRIOR_FOR_N1 = NOT_FOUND_BY_EITHER_READER` **no** es un certificado.
- Reapertura **append-only**: sello, terminales, pruebas e historial no se alteran.
  `nachonumero` pinea `nachocausal@bcd4633` vía `verify_herencia.py` — **ese commit no se toca**.
- Cifras publicadas (`V ≈ 1.4717`, `I ≈ 5.415e-4`, `κ ≈ 7.97e-4`, `δ_τ/ℓ ≈ 35.4`) deben ser salida
  literal de `wp4_kappa_numeric_reference.py` re-ejecutado, con error de cuadratura declarado y no
  presentado como exacto — ver [[numbers-must-come-from-committed-script]].

**Actualización 2026-08-16 (rama `research/f2-f3-chain-distance`).** R2 cerrado como **abierto**:
exponente derivado y cross-checked, **prefactor `OPEN / [UNVERIFIED]`**; caja vencida el
2026-08-14, pasa a R1 (commit `44b0d75`, ítem C-3 del foro-001). Nueva nota firmada
`docs/scope_note_2026-08-16_foro001_falsification_test.md` que levanta la prohibición de ampliar
`n` **sólo** para el test `FORO001-F1` (el `R-1` del foro-001; ojo con la colisión de nombres
`R-1` vs `R1`). Ejecutado (`7b5deec`): 560 de 112.911.876 tuplas falsifican los tres disyuntos → se emitió
`REFUTED` y **se retractó el mismo día** (`0afc16c`,
`docs/c1_correction_2026-08-16_realizability.md`): los 560 emparejan filas/columnas prohibidas por
la prescripción `F_n` (el testigo usa `(11,11)` cuando `F_n` fija `11→7`). Restringido a las
11.639.124 cadenas realizables, sólo 40 de las 1504 no vacuas sobreviven y las 40 caen en
`loss_case` → `COMPATIBLE_FAILURES=0`. **`C1` sigue `INCONCLUSIVE`**, con evidencia positiva
acotada. **Lección:** el test sellado (y el predicado que firmamos a partir de él) cuantifica
sobre cuádruplas **abstractas**, que es el dominio equivocado — precomprometer un predicado no lo
hace correcto. El test sellado no se tocó y sigue pasando (su `n=12` es vacuo, 245025/245025). **`C-1` adjudicado** el mismo día
(`docs/c1_adjudication_2026-08-16_ef4_token_degradation.md`, commits `4c22025`+`c9a891d`):
`EF4_CORRECTED_PRESCRIBED_FAMILY = SKETCH_GEOMETRIC_CORE_REFUTED_AS_STATED`,
`EF4_Q2_ASYMPTOTIC = PROVED_DEDUCTIVE_NO_EXECUTABLE_BACKING_CONDITIONAL_ON_REFUTED_TRICHOTOMY`,
`MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED` restituido — **corregidos** por la retractación:
vigentes son `EF4_CORRECTED_PRESCRIBED_FAMILY = SKETCH_PENDING_INDEPENDENT_AUDIT_COMITE_050`,
`EF4_Q2_ASYMPTOTIC = PROVED_DEDUCTIVE_NO_EXECUTABLE_BACKING`,
`GEOMETRIC_TRICHOTOMY_EF4_3_ABSTRACT_DOMAIN = REFUTED_AT_N24`,
`GEOMETRIC_TRICHOTOMY_EF4_3_ON_F_N = NOT_REFUTED_AT_N24`. La degradación **sobrevive por el motivo
procedimental** (orden vigente del comité 050, nunca levantada), no por el sustantivo. Ningún
token sube. **Reserva clave (backed, `0f1db5e`):** las escaleras del test tienen `rho-1` puntos, así
que a `rho=2` la **contención parcial es imposible para todo `n`** — y la contención parcial es lo
que ejercita los topes de `loss_case`. Luego el `COMPATIBLE_FAILURES=0` de `n=24` no toca el núcleo
del análisis de casos. Sumado a `n=12` vacuo, `n=30` (`rho=2`) y `n=34` (`rho=3`, 0 casos
parciales), **la lógica de escaleras nunca se ha ejercitado**. Los datos de `n=30`/`n=34` están en
`docs/backlog_hallazgos.md` como **`[UNVERIFIED]`** (no salieron de script commiteado). Siguiente
paso propuesto y **no autorizado**: localizar el menor `(n,rho)` no vacuo con un caso compatible de
contención parcial y barrer allí; exige nota firmada por §4 de la nota de alcance.
`C-5` sigue en pie: PR #4 no sale de draft.

**C6 cambió de estado — la nota vieja decía BLOCKED y ya no es cierto.** Entre 2026-07-21 y el
cierre, C6 se cerró y se promovió a **teorema de manuscrito** (`141cccc` cierra el resto uniforme,
`861d5e5` lo promueve), con teorema de separación *dimension-free* a fixed-n y auditoría de
prioridad sobre C6/Teorema 3.9. Aun así, la **línea de localizadores sigue clausurada** por §3 de
la nota de reapertura: C6 es resultado escrito, no vía viva.

**Cadena NC (rama `agent/nc2d-selected-second-moment`, 2026-08-17/18).** Serie de notas de
alcance firmadas una a una por el PI (`docs/program_reopening_note_2026-08-1{6,7,8}_*`), cada una
con terminal precomprometido y un único documento científico en `emergencia/`: NC-0 (auditoría) →
NC-1 (preflight asintótico) → NC-2A (`b_n(m)` escala interior, PROVED) → NC-2B (ley seleccionada
existe, PROVED) → NC-2C (masa interior uniforme + `Pr(S)>=½n^(-(2n^(4/5)+4))`, PROVED) → NC-2D
(segundo momento seleccionado: `Var(sqrt(K L)|S)<=2800 n^(9/5)log n`, PARCIAL) → **NC-2E**
(2026-08-18, `NC2E_PARTIAL_RELATIVE_VARIANCE_REDUCTION`). Objetivo vivo `NC2E-O3`:
`Var_{nu_n}(sqrt(K_h L_h))<=C_q n` (⇒ `Var(ell_h|S)=O(1/n)` ⇒ `liminf T_n^h>0` en el canal
`sigma(M_h)`, fixed-n, d=2). NC-2E probó
`Var <= 10^6 n[log(n!/|S_n|)+4log n]` y **redujo todo el problema a una sola obligación**:
`sum_{pi in S_n}(R+Delta_n)^2 <= (C/n)|S_n|` (discrepancia rectangular media cuadrática bajo la
medida seleccionada). Techo calculado: la familia «cola incondicional ÷ Pr(S)» no baja de
`n log n` ni con `Pr(S)=1`, así que **mejorar `Pr(S)` no cierra O3 por sí solo**. `NC2E_O3 = OPEN`.
**`NC-2F`** (2026-08-18, autorizado por instrucción general del PI «vamos con 1», no por firma
conforme a borrador — **conviene refrendo**): (a) `rho=ceil(20 sqrt(n log n))` en la familia
prescrita de NC-2C §4.1 pasa las cinco desigualdades de margen ⇒
`Pr(S) >= ½ n^(-(40 sqrt(n log n)+5))` ⇒ **exponente de varianza 9/5 → 3/2**
(`Var(q|S) <= 4.2e7 n^(3/2)(log n)^(3/2)`, `Var(ell|S) <= 4.3e7 (log n)^(3/2)/sqrt(n)`);
(b) cota **incondicional** autocontenida `E[Delta_n^2] <= 4.2e4/n` (reducción a esquinas +
proceso empírico iid + encadenamiento diádico + Doob), que cierra el objeto (B) de NC-2E.
Consecuencia **condicional** (hipótesis NO demostrada): si `Pr(S) >= c > 0` entonces `NC2E.1` con
`C_q = 3.4e9/c`, para `n>=10^40`. Ojo: `Pr(S)>=c` está **abierta en ambos sentidos** — sólo hay
cota inferior que decae, ninguna cota superior incondicional en el repo. **La obligación que queda
para cerrar O3 por la ruta del Thm 8.1 de NC-2E es selectiva y afecta a LOS DOS términos**:
`sum_{pi in S_n} (R + Delta_n)^2 <= (C/n)|S_n|`. NC-2F(b) aporta **una mitad** (el término
`Delta_n`, sólo incondicionalmente); `R` está igual desde NC-2E Lema 6.1, y su única cota
*relativa* (Lema 6.3) da `O((log n)^1.5/sqrt n)`, insuficiente. **No contabilizar lo que falta
usando sólo `Delta_n`** — ese error se commiteó el 2026-08-18 y lo cazó el foro-002.
NC-2C/2D/2E no se modifican (append-only).

**Auditoría adversarial foro-002** (`docs/foro/foro_decision_002_nc2fb-auditoria-adversarial.md`,
`REVISE_AND_RECONVENE`): el Teorema 1.1 de NC-2F(b) PASA con recómputo independiente; se
corrigieron una desigualdad publicada falsa (razón de la cola `0.7270292`, no `<0.72`), la omisión
de `R`, y la falta de etiqueta CONDICIONAL en el Cor 8.1. **BLOCK del guardián** contra declarar
«cerrada de forma definitiva la parte incondicional»: ese objeto no está definido en el repo
(`grep -rl "parte incondicional"` → 0 ficheros), ningún criterio se fijó antes, y la práctica
del repo son 11 reaperturas acotadas tras un cierre. Si se cierra, con cláusula de reapertura.

**Actualización 2026-08-21 — ledger del teorema normalizado (`cc6f216`, rama
`agent/nc2fb-lemma-2-1-lean`).** Nota **firmada** por el PI:
`docs/status_note_2026-08-21_normalized_theorem_ledger.md`. Corrige una atribución errónea que
circulaba en deliberación: **`V_n^h>0` NO es resultado de NC-2B**. Lo que NC-2B Thm 3.1 prueba
para todo `n>=6` es `Pr_n(S)>=1/n!>0`, es decir la **existencia del condicionamiento**
(`D_h ⊇ {n>=6}`). La positividad del denominador es de **NC-0 ronda 4 §10.3**
(`emergencia/P1a_count_volume_canal_sigma_m_d2.md:368`), donde el objeto se llama `B_n^h` y es
**literalmente** `Var(ell|n,h,S)` = el `V_n^h` de NC-1 = el `Var(ell_h|n,h,S)` de NC-2B/2D: un
único objeto con tres nombres. La conjunción de ambos cierra `V_n^h>0` para toda la cola, luego
`T_n^h` está bien definido para todo `n>=6` y ambos lados. `DENOMINATOR_POSITIVITY =
PROVED_ALL_N_GE_6_BOTH_SIDES`: **deja de ser deuda, no volver a abrirla por parecido de
notación.** Hereda la dependencia del lema de soporte `2<=K,L<=n-4`
(`emergencia/P1a_count_volume_lema_kl_d2.md:84`) — **cambiar el selector la invalida sin aviso**.

**Frente vivo reducido a tres, todas de escala y ninguna de no-degeneración:**
- `DENOMINATOR_SCALE_COUNTS_PROXY` — `NC2E-O3`, `Var_{nu_n}(q_{n,h})<=C_q n`;
- `DENOMINATOR_SCALE_REAL_OBJECT` — `Var(ell_h|n,h,S)=O(1/n)`. **NC-2E los lista por separado**
  (`emergencia/P1a_count_volume_selected_variance_clt_scale_d2.md:794-795`): no colapsarlos en un
  solo token, porque el puente entre ellos es justo lo que falta;
- `SELECTION_MASS_UNIFORM` — `Pr_n(S)>=c>0`, `OPEN_NOT_REFUTED`. `1/n!` **no** sirve aquí: basta
  para definir el condicionamiento y no para la hipótesis del Cor 8.1 de NC-2F(b).

Puente entre las dos primeras: `sum_{pi in S_n}(R+Delta_n)^2 <= (C/n)|S_n|`, con **sólo la mitad
`Delta_n` suministrada y sólo incondicionalmente**. **Advertencia metodológica congelada en §4 de
la nota:** el objetivo no puede degenerar en una cota absoluta de `E[Delta_n^2]`; hay que
demostrar que el control **sobrevive al condicionamiento** y tiene la escala correcta respecto de
`Var(ell|n,h,S)`.

Objeto principal, sin ambigüedad (§2 de la nota):
`T_n^h = inf_f E[(ell-f(M))^2|n,h,S] / Var(ell|n,h,S)`, ínfimo alcanzado en
`f*(M)=E[ell|M,n,h,S]` por proyección ortogonal en `L^2`. `liminf T_n^h>0` significa
exactamente: **todo predictor basado sólo en `M` conserva asintóticamente una fracción `c_h>0`
del riesgo de Bayes normalizado**. No es reconstrucción, no es insuficiencia para toda pérdida,
no es información mutua. Enunciado objetivo registrado (NO probado): *uniform asymptotic
`L^2`-insufficiency of the count-volume channel for `ell`*. `NOVELTY_CERTIFIED = NO`;
`BRAUN_OVERLAP = COMPLEMENTARY_NOT_EQUIVALENT` (Braun asume `d>=3`, matrices etiquetadas, sin
estimador ni tasa).

Relacionado: [[prereg002-pass-artifact-gap]] (el PASS sellado de 1+1D sigue siendo el activo
positivo), [[pr003-fase3-lecam]], [[estimator-v2-exploration]], [[memoria-claude-sync]].
