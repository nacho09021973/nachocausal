# Nota de cierre del programa `nachocausal`

> **ESTADO: PROGRAM_CLOSED / REPOSITORY_ARCHIVE_RECOMMENDED /
> NO_FURTHER_RESEARCH_AUTHORIZED / NO_PUBLIC_NOVELTY_CLAIM /
> PRESERVE_AS_SCIENTIFIC_RECORD / CLOSURE_IS_DEONTIC_NOT_ALETHIC.**
>
> Fecha: 30 de julio de 2026.
>
> Revisada tras `docs/comite/comite_decision_049_program-closure-adjudication.md`
> (veredicto `RECOMMEND_REVISE_AND_RECONVENE`, custodio de pre-registración `BLOCK`
> sobre el borrador original). Las cinco enmiendas exigidas en el acta 049 §9 están
> incorporadas abajo; el comité no exigió una segunda convocatoria — la sustancia ya
> quedó adjudicada en esa sesión.

## Decisión

Se cierra el programa activo de investigación de `nachocausal`.

La pregunta que motivó el repositorio era si la información causal *order-only* de
un conjunto causal finito podía sostener una reconstrucción o localización
físicamente significativa de estructura de horizonte de Schwarzschild, con
vocación de transferencia a 3+1 dimensiones.

El trabajo realizado no ha establecido ese resultado. Tampoco ha establecido una
contribución central que sea, a la vez, suficientemente original, físicamente útil
y proporcionada al esfuerzo necesario para continuar el programa **con la
evidencia disponible hoy**.

**Naturaleza del acto (enmienda 5).** Este cierre es un acto **deóntico**: retira la
autorización para seguir ampliando el programa bajo su objetivo fuerte original. No
es, y no debe leerse como, un acto **alético**: no afirma que esté probado que no
existe ningún camino científico legítimo. La distinción importa porque el registro
mismo contiene elementos que una lectura alética contradiría (ver "Lo que este
cierre no adjudica", más abajo).

## Balance científico

El repositorio contiene matemática correcta e internamente auditada, resultados
negativos y experimentos reproducibles dentro de sus contratos. Entre ellos hay
cegueras exactas del canal condicionado, límites de recuperabilidad, obstrucciones
a ciertas definiciones globales y una validación acotada en un modelo
Schwarzschild 1+1.

Eso no equivale a haber reconstruido un horizonte, ni a disponer de un observable
útil para 3+1, ni a haber certificado una colección de resultados novedosos
frente a la literatura:

- el lema de amplificación estadística independiente de la dimensión es una
  especialización reutilizable de maquinaria estándar (`PRECURSOR_ONLY` /
  `STANDARD_COROLLARY`, `research_program/bibliography/wp4_dimension_free_order_statistic_priority_audit.md`);
- la separación mediante fracción de orden en la familia concreta (Teorema 3.9) es
  **fixed-n, no asintótica** (`PROVED_FIXED_N_SEPARATION`) — la corrección precisa
  es: la constante \(\kappa(r_p,r_q)\) es pequeña, el régimen `dv` está condicionado
  a un umbral \(dv_0\) no certificado numéricamente, y su prioridad bibliográfica
  sigue **sin certificar** (`PRIORITY_NOT_YET_CERTIFIED` /
  `NO_EXACT_PRECEDENT_FOUND_IN_SCOPED_SEARCH`,
  `research_program/bibliography/c6_theorem39_priority_audit.md`) — esto es
  abstención documentada, no un hallazgo de "no original" *(enmiendas 2 y 3)*;
  **nota sobre magnitud (enmienda 4):** una exploración numérica de esta misma
  sesión estimó que, con la cota de Chebyshev de peor caso del Teorema 3.9(2), se
  necesitarían del orden de \(10^6\)–\(10^7\) elementos para una separación
  TV≥0.5 en el diamante de prueba. Esa cifra es un **artefacto de la técnica de
  prueba** (usa \(\zeta_1,\zeta_2\le1/4\)), no una medida establecida de utilidad
  física: sustituyendo el valor ya probado \(\zeta_1=1/36\) del propio proyecto
  la reduciría sustancialmente, plausiblemente en un orden de magnitud o más
  (`docs/comite/comite_decision_049_program-closure-adjudication.md` §4,
  brief del físico y del matemático). **Esta cifra no debe citarse como prueba de
  debilidad física del resultado**, ni aquí ni en ningún documento futuro;
- los terminales C1–C6 documentan el fracaso de una clase de candidatos, no un
  no-go universal;
- el resultado positivo 1+1 localiza una frontera asociada al horizonte dentro
  de un parche controlado, con las cautelas documentales registradas, y no
  transfiere por sí mismo a 3+1;
- el horizonte de eventos global no es un funcional de un parche finito y la
  escala absoluta es invisible en el canal fixed-n estudiado.

La conclusión honesta no es «todo era falso» ni «no se aprendió nada». Es esta:

> El objetivo fuerte del programa no se alcanzó, y los resultados supervivientes
> no justifican seguir ampliando el repositorio en busca de una contribución que
> rescate retrospectivamente ese objetivo.

## Lo que este cierre NO adjudica (enmienda 1)

Este cierre retira la autorización para continuar, pero **no adjudica** dos
elementos vivos que el registro mismo deja pendientes, y los nombra explícitamente
para que no queden retirados por silencio:

1. **`Q_trap` v2** (`research_program/work_packages/phase3_b2_trapped_surface_preopening_contract.md`,
   commit `b48d98f`). Estado explícito de este cierre:

   ```text
   Q_TRAP_V2_DISPOSITION = UNADJUDICATED_AT_CLOSURE
   CLOSED_BY_GOVERNANCE — NOT_BY_MATHEMATICAL_OBSTRUCTION
   MOOTS_NOT_ANSWERS = comite_decision_048 (RECOMMEND_REVISE_AND_RECONVENE,
     mitad "revise" ejecutada, mitad "reconvene" nunca convocada)
   ```

   Ningún comité ha adjudicado nunca `Q_trap`; el acta 048 solo se pronunció sobre
   el target *predecesor* (`Q_FMOTS`). El terminal `B2_TARGET_BLOCKED_EXTERNAL_SURFACE_LABEL`
   de `Q_FMOTS` vino de una sesión de director bajo delegación del PI, no de un acta
   de comité. Este cierre da por **mooteada** (no respondida) la pregunta que 048
   dejó pendiente, apoyado en la valoración física del comité 049 (`Q_trap` es
   probablemente inviable en 1+1D por carencia de superficies espaciales de
   codimensión dos para definir expansiones — `docs/comite/comite_decision_049_program-closure-adjudication.md`
   §4, brief del físico) — pero esa valoración es un juicio de plausibilidad, no
   una prueba, y se registra como tal.

2. **`order+number` con \(\rho\) conocida** (Fase 3 B1, `docs/manuscript_limits_draft.md`
   §7.3/§8). Este canal es física y lógicamente distinto del programa de
   reconstrucción de horizonte que aquí se cierra: el Teorema 3.1 (\(\mathrm{TV}=0\))
   es expresamente un resultado de canal *fixed-n*, y ese obstáculo se levanta en
   `order+number` porque el número restaura la escala absoluta que el orden solo no
   puede portar. Este cierre **no** se pronuncia sobre B1; queda fuera de su
   alcance, no cerrado por él. Abrirlo, si alguien lo decide, sería un contrato
   nuevo y separado.

## Alcance del cierre

A partir de esta nota:

1. no se abren nuevos observables, work packages, simulaciones, auditorías de
   rescate ni reformulaciones del target **dentro del objetivo de reconstrucción
   de horizonte 1+1D/3+1D que este programa perseguía** — esto incluye no
   reconvocar la adjudicación pendiente de `Q_trap` v2 bajo esta autorización;
   el canal `order+number` (B1) queda expresamente fuera de esta cláusula, por lo
   dicho arriba;
2. no se reclama novedad pública para los resultados cuya prioridad no fue
   certificada (`PRIORITY_NOT_YET_CERTIFIED`, no "no originales");
3. los manuscritos y notas existentes se conservan como registro de lo probado,
   lo refutado y lo que quedó abierto, no como anuncio de una reconstrucción;
4. no se alteran resultados sellados, terminales, pruebas ni historial. Sello
   verificado intacto en el momento de este cierre:
   `thresholds.py sha256 = 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4`
   (coincide con `docs/preregistration_002.md`). La banda de semillas virgen
   reservada `[2,000,000–2,999,999]` permanece **sin quemar** más allá de las 20
   semillas ya anotadas en `docs/preregistration_002.md`;
5. tras registrar y sincronizar este cierre, se recomienda archivar el repositorio
   en modo de solo lectura.

Archivar no significa declarar inútil cada cálculo. Significa aceptar que el
programa, como programa de reconstrucción de horizonte order-only, ha llegado a
su término y que continuar ya no está científicamente justificado con la evidencia
disponible — bajo la lectura deóntica de esta sección, no bajo una afirmación de
inexistencia de todo camino posible.

## Resumen público

`nachocausal` estudió qué puede recuperarse de la geometría de Schwarzschild a
partir de orden causal finito sin coordenadas. Produjo resultados acotados de
identificabilidad y no-identificabilidad, pero no obtuvo una reconstrucción de
horizonte 3+1 ni una contribución central de utilidad física suficiente. El
programa queda cerrado y el repositorio se conserva como registro reproducible de
ese resultado. Un candidato de continuación (`Q_trap` v2) y un canal físicamente
distinto (`order+number`) quedan explícitamente sin adjudicar, no descartados.

## Firma

```text
SIGNED_AND_AUTHORIZED_BY_PI: 2026-07-30
BASIS: docs/comite/comite_decision_049_program-closure-adjudication.md §11
```
