# Nota de estado — ledger del teorema normalizado `T_n^h`

```text
ESTADO: FIRMADA — NOTA DE ESTADO DOCUMENTAL / NO ES REAPERTURA NI CIERRE
FECHA: 2026-08-21
FECHA_FIRMA: 2026-08-21
COMMIT_DE_VERIFICACION_DE_ANCLAS: e7cac71
NATURALEZA: REGISTRO — NO DEONTICO, NO ALETICO SOBRE OBJETOS NUEVOS
RESULTADO_NUEVO: NINGUNO
NO_MODIFICA: PR #7, sello, semillas, codigo, ni los tokens publicados de NC-0..NC-2F
SEMILLAS: ninguna
DATOS: ninguno
CODIGO: ninguno
```

## 1. Por qué existe esta nota

Tres cosas estaban dispersas y una estaba mal atribuida.

1. El **objeto principal** `T_n^h` aparece definido en cuatro ficheros con tres
   notaciones para un mismo denominador:
   `B_n^h` (`emergencia/P1a_count_volume_canal_sigma_m_d2.md:364`),
   `V_n^h` sobre `ell` (`emergencia/P1a_count_volume_preflight_asintotico_d2.md:24`),
   y `V_n^h` sobre `ell_h`
   (`docs/program_reopening_note_2026-08-17_nc2b_selected_law_DRAFT.md:53`;
   `emergencia/P1a_count_volume_selected_second_moment_d2.md:91`).
2. La **positividad del denominador** venía arrastrándose **en la deliberación**
   como deuda abierta por asociación de notación. El terminal de `NC-2F(b)` ya no la
   lista —correctamente, por omisión—, pero la omisión no es un registro: esta nota
   la convierte en token explícito para que no se reabra por inercia.
3. El **techo de afirmación** del posible resultado publicable no estaba escrito en
   ningún sitio en su forma exacta, sólo aludido.

Esta nota fija las tres. No demuestra nada nuevo: su §3 es una conjunción de dos
resultados ya registrados, y su §5 es un enunciado objetivo, no un teorema probado.

## 2. Objeto principal, sin ambigüedad

Para `h in {PAST,FUTURE}` sea

\[
D_h=\{n\ge6:\Pr_n(S)>0\},
\]

y para `n in D_h`, con todas las esperanzas y varianzas condicionadas a `(n,h,S)`:

\[
A_n^h=\mathbb E[\operatorname{Var}(\ell\mid M,n,h,S)\mid n,h,S],
\qquad
V_n^h=\operatorname{Var}(\ell\mid n,h,S).
\]

El objeto principal es el **riesgo de Bayes normalizado del canal `sigma(M)`**:

\[
T_n^h=
\inf_{\substack{f\ \text{medible}\\ f(M)\in L^2}}
\frac{\mathbb E[(\ell-f(M))^2\mid n,h,S]}{\operatorname{Var}(\ell\mid n,h,S)}.
\]

Por proyección ortogonal en `L^2` el ínfimo se alcanza en
`f^*(M)=E[ell|M,n,h,S]`, luego

\[
T_n^h=\frac{A_n^h}{V_n^h}.
\tag{2.1}
\]

El ínfimo está bien puesto: `ell=sqrt(XY)` con `X,Y` Beta toma valores en `[0,1]`
(`emergencia/P1a_count_volume_canal_sigma_m_d2.md:369`), luego `ell in L^2` de la ley
condicionada; y el denominador no se anula por §3.

(2.1) es una identidad, no una aproximación: coincide literalmente con la
definición operativa usada en `emergencia/P1a_count_volume_canal_sigma_m_d2.md:362-365`
y en `emergencia/P1a_count_volume_preflight_asintotico_d2.md:22-26`.

**Lectura exacta del objetivo.** `liminf_n T_n^h>0` significa: existe `c_h>0` tal
que, asintóticamente, **todo predictor basado únicamente en `M` conserva al menos
una fracción `c_h` del riesgo de Bayes normalizado**. No es reconstrucción del
espaciotiempo, no es insuficiencia para todas las pérdidas, y no es una afirmación
sobre información mutua.

## 3. Microcomprobación documental — positividad del denominador

### 3.1 Los dos registros no son el mismo

Lo que `NC-2B` probó para `n>=6` **no** es `V_n^h>0`:

- `emergencia/P1a_count_volume_selected_law_asymptotics_d2.md:66-69` — Teorema 3.1:
  `Pr_n(S)>=1/n!>0` para todo `n>=6`, por exhibición de una permutación testigo
  (identidad si `n` es par; `(2,3,...,n,1)` si es impar).
- Token: `NC2B_O1_EVENTUAL_SELECTION = PROVED_FOR_ALL_N_GE_6` (`:111`).

Es decir, `NC-2B(O1)` cierra `D_h ⊇ {n>=6}` — la **existencia del
condicionamiento** en toda la cola —, no la positividad de la varianza. El propio
techo de `NC-2B` lo dice: «Queda demostrado exclusivamente que el condicionamiento
existe para todo `n>=6`» (`:236`).

### 3.2 La positividad es de `NC-0`, ronda 4

- `emergencia/P1a_count_volume_canal_sigma_m_d2.md:364` define
  `B_n^h = Var(ell|n,h,S)`. Es **literalmente** el mismo objeto que `V_n^h`: mismo
  condicionamiento `(n,h,S)`, mismo target `ell`, mismo denominador. El renombre a
  `V_n^h` ocurre en el preflight `NC-1`
  (`emergencia/P1a_count_volume_preflight_asintotico_d2.md:24`), y el subíndice
  `ell_h` de `NC-2B` (`docs/program_reopening_note_2026-08-17_nc2b_selected_law_DRAFT.md:53`)
  es sólo etiquetado de lado. Los tres nombres denotan un único objeto.
- `emergencia/P1a_count_volume_canal_sigma_m_d2.md:368-372` prueba: el soporte
  seleccionado cumple `2<=K,L<=n-4`; condicionado a cada forma, `ell=sqrt(XY)` con
  Betas propias no degeneradas, luego `Var(ell|K,L,n,h,S)>0`; por tanto `A_n^h>0` y,
  por varianza total, `B_n^h>=A_n^h>0`.
- El mismo pasaje acota su alcance: «no da una cota uniforme, una tasa inferior ni
  demuestra que `D_h` contenga todos los enteros suficientemente grandes» (`:372-374`).
  La positividad es **puntual en `D_h`**.

### 3.3 Proposición 3.1 (conjunción, sin contenido nuevo)

> Para todo `n>=6` y ambos lados `h`, `V_n^h>0`; en consecuencia `T_n^h` está bien
> definido en toda la cola `n>=6`.

*Demostración.* `NC-2B` Thm 3.1 da `n in D_h` para todo `n>=6`
(`emergencia/P1a_count_volume_selected_law_asymptotics_d2.md:66-69`). `NC-0` §10.3 da `B_n^h>0` para todo
`n in D_h` (`emergencia/P1a_count_volume_canal_sigma_m_d2.md:368-372`). `B_n^h = V_n^h` por §3.2. `QED`

Esto es una conjunción de dos hechos registrados, no un resultado nuevo. Concuerda
con el terminal vigente de `NC-0`, que ya declara «el cociente está bien definido en
su dominio» (`emergencia/P1a_count_volume_canal_sigma_m_d2.md:497-501`).

### 3.4 Dependencias y advertencias

- La positividad hereda la dependencia del **lema de soporte** `2<=K,L<=n-4`,
  demostrado en `emergencia/P1a_count_volume_lema_kl_d2.md:76-84` y registrado como
  `P1_ACTUAL_SELECTED_DOMAIN` (`:620`). **Cualquier cambio del selector la invalida
  sin aviso.**
- El `FAIL_MATERIAL` de la ronda 4 de `NC-0` fue por la sobreextensión de `T_emp`
  hasta `n=16000`, y no tocó §10.3; la ronda 5 cerró con
  `NC0_AUDIT_ROUND_5 = PASS_AFTER_DOCUMENTARY_REMEDIATION`
  (`emergencia/P1a_count_volume_canal_sigma_m_d2.md:505`).
- Toda esta cadena es **prosa auditada, no Lean**. Lo formalizado en la rama
  `agent/nc2fb-lemma-2-1-lean` es el Lema 2.1 de `NC-2F(b)` y su andamiaje de rangos
  (commits `ac14798..e7cac71`), no §10.3 de `NC-0`.

## 4. Lo que la positividad **no** cierra

La positividad no toca ninguna de las deudas abiertas, que son de **escala**, no de
no-degeneración. Ni se siguen de `V_n^h>0` ni lo implican:

| Deuda | Enunciado | Ancla |
|---|---|---|
| Masa de selección uniforme | `Pr_n(S)>=c>0` con `c` independiente de `n` | `emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md:485-486`, token `:517` |
| Escala del denominador, proxy de conteos (`NC2E-O3`) | `Var_{nu_n}(q_{n,h})<=C_q n`, con `q_{n,h}=sqrt(K_h L_h)` | `emergencia/P1a_count_volume_selected_variance_clt_scale_d2.md:33`, `:65-66`, token `:833` |
| Escala del denominador, objeto real | `Var(ell_h|n,h,S)=O(1/n)` | `emergencia/P1a_count_volume_selected_variance_clt_scale_d2.md:795`; `emergencia/P1a_count_volume_selected_law_asymptotics_d2.md:240` |
| Masa interior (`NC2B-O2`) | `Pr(M in I_n|n,h,S)>=p>0` | `emergencia/P1a_count_volume_selected_law_asymptotics_d2.md:257` |

Las dos filas de escala son objetivos distintos y ambos abiertos: `NC-2E` los lista
por separado (`:794-795`). El puente entre ellas es la obligación relativa
`RELATIVE_SUM_OF_(R+Delta_n)^2_OVER_S_n`, de la que `NC-2F(b)` suministra
**sólo el término `Delta_n`, y sólo incondicionalmente**
(`emergencia/P1a_count_volume_rectangular_discrepancy_l2_d2.md:518-519`).

`Pr_n(S)>=1/n!` es **incomparablemente más débil** que `Pr_n(S)>=c>0`: la primera
basta para definir el condicionamiento, la segunda es la hipótesis del Corolario 8.1
de `NC-2F(b)` y sigue `OPEN_NOT_REFUTED`.

**Consecuencia metodológica.** El objetivo no puede convertirse en una cota absoluta
de `E[Delta_n^2]`. Hay que demostrar que ese control **sobrevive al
condicionamiento** y tiene la escala correcta respecto de `Var(ell|n,h,S)`. Ésa es
exactamente la diferencia entre un buen lema técnico y el posible teorema
científicamente interesante.

## 5. Enunciado del posible resultado publicable

Se registra el objetivo **como enunciado**, no como teorema probado:

> **Uniform asymptotic `L^2`-insufficiency of the count–volume channel for `ell`.**
>
> Existen `c>0` y `n_0<infinity` tales que para todo `n>=n_0` y todo
> `h in {PAST,FUTURE}`:
> \[
> \inf_f
> \frac{\mathbb E[(\ell-f(M))^2\mid n,h,S]}{\operatorname{Var}(\ell\mid n,h,S)}
> \ge c.
> \]

Si se cerrase para `PAST` y `FUTURE` por separado, al ser sólo dos orientaciones
basta tomar el mínimo de las dos constantes positivas para obtener la versión
uniforme en `h`.

**Alcance de la afirmación, si alguna vez se probase.** Vale para el canal
count–volume y sólo para él; para el target `ell` y sólo para él; bajo pérdida
cuadrática y sólo bajo ella; y en el modelo condicionado por `(n,h,S)`. No dice
nada sobre canales enriquecidos, poset completo, horizontes, escala absoluta ni
`d>=3`.

**Solapamiento con Braun.** Complementario, no equivalente: Braun (arXiv:2507.01907)
asume `d>=3` heredado de Malament, trabaja con matrices etiquetadas, y no contiene
estimador, tasa ni cota de riesgo a `n` finito
(`docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md:375-379`;
`research_program/work_packages/wp4_fisher_localization_floor.md:500-514`). Un
resultado negativo en `d=2` **no** transfiere hacia arriba como no-go, y el
repositorio ya lo cerca (`docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md:262-264`).

**Estatuto bibliográfico.** La búsqueda dirigida que no encontró un teorema
equivalente se realizó en deliberación y **no dejó registro de comandos en el
repositorio**: se marca `[UNVERIFIED]` como registro bibliográfico. De la ausencia
de comprobación no se sigue novedad. `NOVELTY_CERTIFIED = NO`.

## 6. Techo de afirmación de esta nota

Se afirma exclusivamente: (a) la identidad de objetos de §2 y §3.2; (b) la
Proposición 3.1, que es conjunción de dos registros previos; (c) el inventario de
deudas de §4. No se demuestra ni se refuta `liminf T_n^h>0`, ninguna de las tres
deudas de §4, ni ningún enunciado de §5. No se usaron datos sellados,
simulaciones, semillas ni código nuevo, y no se consultaron los tamaños
`n in {64,96,128}`.

## 7. Terminal

```text
NORMALIZED_THEOREM_LEDGER_TERMINAL = LEDGER_RECORDED_NO_NEW_RESULT

DENOMINATOR_POSITIVITY
= PROVED_ALL_N_GE_6_BOTH_SIDES
  [NC-0 §10.3  emergencia/P1a_count_volume_canal_sigma_m_d2.md:368
   + NC-2B Thm 3.1  emergencia/P1a_count_volume_selected_law_asymptotics_d2.md:66]

DENOMINATOR_OBJECT_IDENTITY
= B_n^h == V_n^h == Var(ell_h|n,h,S)   [SINGLE_OBJECT_THREE_NAMES]

DENOMINATOR_POSITIVITY_DEPENDS_ON
= SELECTED_SUPPORT_2_LE_K_L_LE_N_MINUS_4  (emergencia/P1a_count_volume_lema_kl_d2.md:84)

DENOMINATOR_SCALE_COUNTS_PROXY
= OPEN   (NC2E-O3: Var_{nu_n}(q_{n,h}) <= C_q n)

DENOMINATOR_SCALE_REAL_OBJECT
= OPEN   (Var(ell_h|n,h,S) = O(1/n))

BRIDGE_BETWEEN_THE_TWO
= RELATIVE_SUM_OF_(R+Delta_n)^2_OVER_S_n  [HALF_SUPPLIED: DELTA_TERM_UNCONDITIONAL_ONLY]

SELECTION_MASS_UNIFORM
= OPEN_NOT_REFUTED  (Pr_n(S) >= c > 0; probado solo Pr_n(S) >= 1/n!)

INTERIOR_MASS
= OPEN_RELATIVE_COUNTING_PROBLEM  (NC2B-O2)

BRAUN_OVERLAP
= COMPLEMENTARY_NOT_EQUIVALENT

CLAIM_SCOPE
= COUNT_VOLUME_CHANNEL_ONLY
  + TARGET_ELL
  + SQUARED_ERROR
  + CONDITIONAL_MODEL

EQUIVALENT_THEOREM_FOUND
= NO_IN_TARGETED_SEARCH  [UNVERIFIED — sin registro de comandos en el repositorio]

NOVELTY_CERTIFIED
= NO

NORMALIZED_THEOREM
= OPEN_AT_NC-2F(B)

FORMALIZED_IN_LEAN
= NC2F_B_LEMMA_2_1_ONLY  (rama agent/nc2fb-lemma-2-1-lean, ac14798..e7cac71)

NEW_DATA = NO
NEW_SEEDS = NO
NEW_CODE = NO
GATES_REOPENED = NONE
```

## 8. Firma

```text
FIRMADO_POR: Ignacio Martín (PI)
FECHA_FIRMA: 2026-08-21
DECISION: LEDGER_RATIFICADO_CONFORME_AL_BORRADOR
AUTHORISED_SCOPE: registro documental de §§2-5 y terminal de §7; ninguna ejecución
LITERAL_SIGNOFF: "firmo , commit y push"
```

Esta firma ratifica el **registro**, no promueve ningún enunciado abierto. Las
deudas de §4 siguen exactamente donde estaban y cualquier ataque a ellas requiere
nota de alcance y firma nuevas.
