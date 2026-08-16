# Adjudicación de C-1 (foro-001) — degradación de los tokens de EF-4

> **CORREGIDA EN PARTE — 2026-08-16, mismo día**, por
> `docs/c1_correction_2026-08-16_realizability.md`. El **motivo sustantivo** de §1.2 —la
> refutación de la tricotomía en `n=24`— **se retira**: los contraejemplos no son realizables bajo
> `F_n`. El **motivo procedimental** de §1.1 (la orden vigente del comité 050) **se mantiene
> intacto**, y con él la degradación de `EF4_CORRECTED_PRESCRIBED_FAMILY` fuera de `PROVED`.
> Los valores de token vigentes son los de la corrección §3, no los de §2 de este documento.

```text
ESTADO: C1_ADJUDICATED / TOKENS_DEGRADED
FECHA: 2026-08-16
BASE: docs/foro/foro_decision_001_ef4-falsacion-adversarial.md §10 (C-1)
BASE: docs/comite/comite_decision_050_p1a-seccion-13-certificado-familia-prescrita.md:485,496-497
EVIDENCIA NUEVA: dev/EF4_TRICHOTOMY_N24_RESULT.md (FORO001-F1, commit 7b5deec)
SELLO: intacto — no se toca
SEMILLAS: ninguna
```

## 1. Por qué se abre

C-1 estaba `NOT_AUTORISED` desde la firma del 2026-08-15
(`foro_decision_001:635`). Se abre ahora por autorización del PI (§6), con dos motivos
independientes acumulados:

1. **Procedimental (el motivo original de C-1).** El comité 050 ordenó explícitamente que la
   reparación del Caso 2 de la Prop. 13.12 **no** se etiquetara `PROVED` —"Do not let my AM-GM
   repair enter the manuscript as `PROVED` on my say-so" (`comite_050:325`)— y que
   `MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO` se **conservara** con puntero a ese
   informe (`comite_050:485`). Ningún comité posterior levantó la condición: `docs/comite/`
   termina en 050. El token no se conservó degradado: **desapareció**, y la afirmación subyacente
   se promovió a `PROVED`. Ésa es exactamente la modalidad de fallo que 050 se anticipó a impedir.

2. **Sustantivo (nuevo, del 2026-08-16).** `FORO001-F1` refuta la tricotomía de EF-4.3 en `n=24`:
   560 de 112.911.876 tuplas falsifican `fixed_inner`, `small_product` y `loss_case` a la vez, con
   cross-check escalar independiente de las 560 y de las 1.504 tuplas no vacuas. La tricotomía era
   el núcleo geométrico que hacía funcionar la familia prescrita, y su único test —`n=12`— es
   vacuo (`245025/245025`), de modo que nunca la había puesto a prueba.

## 2. Tokens degradados

Valores vigentes a partir de esta nota. Sustituyen a los de `docs/backlog_hallazgos.md:1531-1533`,
que se conservan **in situ** como registro histórico con marcador adjunto.

```text
EF4_CORRECTED_PRESCRIBED_FAMILY = SKETCH_GEOMETRIC_CORE_REFUTED_AS_STATED
EF4_Q2_ASYMPTOTIC = PROVED_DEDUCTIVE_NO_EXECUTABLE_BACKING_CONDITIONAL_ON_REFUTED_TRICHOTOMY
MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED = NO_TWO_BREAKS_CONFIRMED_BY_COMITE_050
GEOMETRIC_TRICHOTOMY_EF4_3 = REFUTED_AT_N24
```

Justificación por token:

- **`EF4_CORRECTED_PRESCRIBED_FAMILY`.** No puede llevar `PROVED` por (1) —orden vigente del 050—
  y ahora tampoco por (2). Baja a `SKETCH`, con la calificación explícita de que su núcleo
  geométrico está refutado *tal como está enunciado*. Lo que sigue con respaldo ejecutable es la
  parte aritmética: construcción entera, inyectividad y medio-balance, verificadas en
  `n ∈ {10⁵,10⁶,10⁷}`. Eso no se toca y no se degrada.
- **`EF4_Q2_ASYMPTOTIC`.** El foro ya había establecido que tiene **cero** respaldo ejecutable
  (C9): deducción en prosa desde (EF4.19)+(EF3.9). Se le añade la condicionalidad heredada: la
  inserción pasa por la familia prescrita, cuyo núcleo geométrico acaba de caer.
- **`MATHEMATICAL_CORRECTNESS_INDEPENDENTLY_AUDITED`.** Se restituye con el valor literal que ya
  figura en `emergencia/P1a_puerta_teorica_en_Minkowski.md:1608`, con puntero al 050.
- **`GEOMETRIC_TRICHOTOMY_EF4_3`.** Token nuevo, emitido por un resultado ejecutable propio
  (`dev/ef4_trichotomy_exhaustiveness_n24.py`), no por lectura.

## 3. Lo que esta nota NO hace

- **No sube ningún token.** La regla precomprometida del foro —"no se sube ningún token sin
  auditoría independiente registrada; el autor de una reparación no firma su propia promoción"—
  se refiere a promociones. Aquí sólo se baja.
- **No declara muerto EF-4.** `FORO001-F1` enumera cuádruplas **abstractas**; que 560 de ellas
  escapen a la tricotomía no establece por sí solo que las configuraciones refutadas sean
  alcanzables por el argumento real. Lo que queda establecido es que **la tricotomía no es una
  partición exhaustiva de casos**, y por tanto el certificado no está probado por esa vía.
  Si sobrevive con un análisis de casos reparado es `OPEN`.
- **No adjudica los tokens vecinos.** `EF4_UNIQUE_SELECTION_ENTROPY`,
  `EF4_TERMINAL = FIBER_CONCENTRATION` y el `Gate EF-4: PASS` de
  `docs/backlog_hallazgos.md:1537` quedan marcados como **afectados y no adjudicados**: su
  dependencia del núcleo refutado no se ha leído en esta sesión. No se degradan aquí porque
  degradar sin lectura es tan poco fundado como promover sin auditoría.
- **No reabre la línea EF-0..EF-8**, que sigue en `docs/backlog_hallazgos.md` como hallazgo fuera
  de perímetro. Esto es saneamiento del registro, no investigación.
- **No toca** el sello, `prereg-001/002/003`, ni el manuscrito de límites (`R1`), que no dependen
  de EF-4.

## 4. C-5 sigue en pie

PR #4 **no sale de draft**. La precondición del foro era "no sacar PR #4 de draft hasta que C-1
esté hecho"; C-1 está hecho, pero lo que C-1 ha destapado es una refutación, no un visto bueno.
Sacar de draft requiere su propia decisión.

## 5. Trabajo abierto que esto deja

1. Leer si `EF4_UNIQUE_SELECTION_ENTROPY` y el `Gate EF-4: PASS` heredan la rotura (§3, tercer
   punto).
2. Delimitar qué parte de EF-4 sobrevive con un análisis de casos reparado, o registrarlo como
   cerrado en negativo.
3. Comprobar si la familia de contraejemplos persiste para `n > 24`. Observación **no verificada**:
   `threshold = 1/8 + rho/free_count → 1/8` cuando `n` crece, mientras la partición equilibrada se
   mantiene en `0.25`, de modo que el hueco se ensancha. Sólo se ha ejecutado `n=24`; extender
   requiere otra nota firmada.

Ninguno de los tres bloquea `R1`, cuya caja vence el 2026-09-11.

## 6. Firma

```text
ADJUDICATED_BY_PI: Ignacio
DATE: 2026-08-16
AUTHORISED_SCOPE: C-1 del foro-001 — degradar los tokens enumerados en §2 y anotar el registro
NOT_AUTHORISED: C-5 (PR #4 sigue en draft); reabrir EF-0..EF-8; ampliar n más allá de 24;
  degradar o promover cualquier token no listado en §2
```
