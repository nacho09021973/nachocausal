# Auditoría 1 de reingreso físico — transporte de canal S1/S2 al benchmark Schwarzschild

```text
ESTADO: AUDIT_ONLY
FECHA: 2026-08-28
GOBERNANZA: docs/program_physical_reentry_2026-08-28.md
            docs/program_s2_authorization_2026-08-28.md
NO_REVOCA: docs/program_closure_note_2026-07-30.md
NATURALEZA: lectura de registro existente.
            Cero semillas, cero simulacion, cero instrumentos.
NO_COMMIT: este fichero no se commitea en este run
```

Este documento no modifica S1/S2, el mapa corto
`docs/physical_reentry_map_2026-08-28.md`, ni ningún otro fichero.
No demuestra un puente nuevo.

## 1. INPUT_STATE

```text
git branch --show-current  -> emergencia/p1a-canal-sigma-m
git rev-parse HEAD         -> 7e9c8fa9c43553e80308a695e7df2c328d20dccf
git status --short         -> ?? docs/physical_reentry_audit_001_2026-08-28.md
@{u}                       -> origin/emergencia/p1a-canal-sigma-m
git rev-parse @{u}         -> c0780566d8f42d605e5c3d7dfc59f9327a1425be
HEAD vs origin             -> ahead 1 (7e9c8fa = reingreso opcion 1 + mapa corto)
ANCLA_S1                   -> 2219f21dea2cbd82ba9d959a6d55e1cf87a0bcf6
ANCLA_S2                   -> c0780566d8f42d605e5c3d7dfc59f9327a1425be
SELLO                      -> 6e2c38881234cef48e859096b46f261cfa83ea8a2f6c955cc1dbc42537bfefd4
```

El único estado no commiteado de entrada es este borrador de auditoría,
preexistente y no rastreado; se reutiliza en lugar de crear un segundo fichero.
Los ficheros de decisión de reingreso ya commitados
(`docs/program_physical_reentry_2026-08-28.md`,
`docs/physical_reentry_map_2026-08-28.md`) no se editan.

## 2. FISHER_BRANCH_FROZEN_STATE

Fuentes: `research_program/work_packages/wp6_d2_geometric_tangent_classification.md`
(S1, ancla `2219f21`);
`research_program/work_packages/wp6_d2_geometric_fisher_retention.md`
(S2, ancla `c078056`);
`docs/program_s2_authorization_2026-08-28.md`.

```text
GEOMETRIC_TANGENT_CLASSIFICATION = PROVED
S2_GEOMETRIC_FISHER_RETENTION = PROVED_BY_ASSEMBLY
STOP_AFTER_S2 = SI
S3_NOT_OPENED
S4_NOT_OPENED
NO_HORIZON_CLAIM
NO_PRIORITY_CLAIM
FISHER_BRANCH_ROLE = STRUCTURAL_TOOL
```

No se reabre finite-rank, sector asimétrico, bilinear genérico, rate
improvement, S3, 2+1 ni 3+1.

## 3. EXPERIMENT_F

Fuente: S1 §1 y §5; S2 §1; WP6 dicotomía §§1–2; hoja de ruta §2.2 Convención B.

1. **Punto base geométrico.** Diamante de Minkowski `1+1`, métrica plana
   `g_0`. El punto `epsilon=0` es plano.
   (S1 `:71-87`; lectura `docs/s1_closure_reading_2026-08-28.md` §1)
2. **Dominio.** `D=[0,1]^2`.
   (S1 `:75-78`)
3. **Coordenadas.** Nulas normalizadas `(u,v)` con orden producto
   `(u,v) ≼ (u',v') ⇔ u≤u' y v≤v'`.
   (S1 `:75-78`)
4. **Medida/sprinkling.** Volumen normalizado `mu_0=du dv` en el nulo;
   `mu_epsilon = q_epsilon du dv` con
   `q_epsilon = e^{2 epsilon psi}/Z(epsilon)`.
   (S1 `:82-87`, `:127-128` de S1; S2 `:65-67`)
5. **Condicionamiento a `N`.** Poisson condicionado a `N` puntos = `N` iid
   de `mu_epsilon` (lema de condicionamiento,
   `docs/manuscript_limits_draft.md:294-298`, citado en WP6 dicotomía §1).
6. **Parámetro local.** `epsilon` en `epsilon=0`; generador `psi in C(D)`.
   Clase S2: `psi = alpha(u)+beta(v)+lambda f(u)f(v)`, `lambda != 0`,
   `int f=0`, `int f^2>0`.
   (S2 `:56-85`)
7. **Representación antes del cociente.** Permutación de rangos `Pi_N`
   del realizador `(U,V)`. Depende del realizador. No es order-only.
   (S2 `:69-70`; S1 §5.2)
8. **Estadístico.** Score
   `S_{N,psi}(pi)=2 lambda sum_i a_{i,N} a_{pi(i),N}`,
   `a_{i,N}=E[f(U_{(i)})]`.
   (S1 Teorema 6; S2 `:3.2`)
9. **Canal.** `Pi_N -> [P_{Pi_N}]`.
   (S2 `:72-73`; Teorema 5 WP6 modular)
10. **Fisher comparado.** `I_N^{[P]}/I_N^Pi -> 1` (Teorema 8 / (11.6)).
11. **PIT.** `T=(F_U, F_V)` creciente por coordenadas; isomorfismo de orden
    del orden producto; la ley de `Pi_N` es la de la cópula.
    (WP6 dicotomía Lema A `:54-74`; S1 §5.1)
12. **Caja nula.** El PIT y la densidad de cópula `c_epsilon(x,y)` sobre
    el cuadrado completo usan que el soporte es `I × J`.
    (S1 (3.4)–(3.5); WP6 dicotomía `:24-48`)
13. **Equivalencias marginales.** `ker P = A = {alpha(u)+beta(v)}` =
    direcciones planas (Proposición B). El canal de rangos no las ve.
    (S1 Prop. 9.1; WP6 dicotomía §3)

## 4. EXPERIMENT_H

Fuente: `docs/preregistration.md`; addendum 001; freeze v2; prereg-002;
resultado 002. No se rellenan campos no documentados.

1. **Métrica.** Schwarzschild 1+1 en Eddington–Finkelstein. En el
   manuscrito de límites, forma
   `g_tau = -(1-tau/r) dv^2 + 2 dv dr`, `det g = -1`.
   (`docs/preregistration.md:61-62`;
   `docs/manuscript_limits_draft.md:235-245`)
2. **Dominio físico.** Caja alta:
   `t_edge=6.0`, `r_edge=1.2`, `r_center=0.7`, área 7.2,
   `r ∈ [0.1, 1.3]`.
   (`docs/preregistration_001_addendum.md:39`;
   `docs/estimator_v2_freeze.md:110-111`)
3. **Sistema de coordenadas.** EF `(t*, r)` en el generador sellado; el
   manuscrito escribe el mismo chart ingoing como `(v,r)`. Sprinkling uniforme
   en esas coordenadas porque `det g = -1`.
   (`nachocausal/generator.py:10-12, 91-127`;
   `docs/manuscript_limits_draft.md:235-249`)
4. **Fronteras del patch.** `t_edge=6` (suelo del domain gate
   `T_EDGE_MIN=6`); corte radial `[0.1, 1.3]` que incluye `r_S=0.5` y
   una pared interior `r=0.1`.
   (`docs/estimator_v2_freeze.md:62-66, 110-111`;
   addendum `:39-40`)
5. **Sprinkling.** Poisson de volumen natural, sin densificación radial.
   (`docs/preregistration.md:8-10, 62-63`)
6. **`N`.** Intensidades congeladas `{1500, 3000, 6000, 12000}`; primario
   12000. El resultado reporta `N̄` (p.ej. 12052), no un `n` fijado.
   Poisson **no** condicionado a cardinalidad exacta.
   (`docs/preregistration_001_addendum.md:44-45`;
   `docs/preregistration_002_result.md:42`)
7. **Información del estimador.** Poset anonimizado `(C, ≤)` y `|C|`.
   (`docs/preregistration.md:10-11, 63`)
8. **Ground truth solamente.** Embedding, `M`, `r`, etiquetas. El
   embedding puntúa, no define.
   (`docs/preregistration.md:32-33`; `CLAUDE.md:39`)
9. **Observable.** v2: `O(i)=|future(i)|` sobre minimales; umbral
   2-means; gate `τ(n)`; bracket `[r_lo, r_hi]`.
   (`docs/estimator_v2_seal.md:16-17`;
   `docs/preregistration_002.md:43-47`)
10. **Objeto que se puntúa.** Bracket de `r` de minimales low-O vs
    high-O contra `r_S=2M=0.5` oculto.
    (`docs/preregistration_001_addendum.md:64-73`)
11. **“Horizon-associated boundary”.** Frontera order-only asociada al
    horizonte **en un parche finito**. El addendum prohíbe la lectura
    asintótica `r_h → 2M`.
    (`docs/preregistration_001_addendum.md:75-84`;
    `docs/preregistration_002_result.md:64-75`)
12. **Claim demostrado / no demostrado.**
    Demostrado (PASS, primario 12000): bimodalidad vs MINK de la misma
    nube, localización del bracket con `|dr|/(2M)=0.064 ≤ θ_loc`,
    estabilidad, fp=0, order-only.
    (`docs/preregistration_002_result.md:18-61`)
    No demostrado: horizonte de eventos global (Teorema 3.2);
    reconstrucción métrica; 3+1; que la señal sea trapping y no
    truncación de singularidad (C3-early `REJECTED_HAYWARD`).
    (`docs/manuscript_limits_draft.md: teorema 3.2`;
    `docs/comite/comite_decision_042_c1-c5-localizer-line-closure.md:48-53`)

Square-box (`docs/new_geometry_future_observables_addendum.md`) **no es
H**. Terminal `BH_MINK_DISPERSION_DIFFERENCE_DETECTED`. No localiza
horizonte (`:21-38, 187-196`). Se trata en la matriz como transferencia, no como
el experimento H.

## 5. TRANSPORT_MATRIX

Categorías: `A = EXACTLY_TRANSPORTS`,
`B = REQUIRES_NEW_MATHEMATICAL_BRIDGE`,
`C = BENCHMARK_SPECIFIC_NOT_INHERITED_FROM_S1_S2`.

| Pieza | Cat. | Cita |
|---|---|---|
| Orden causal 1+1 en nulas globales = producto | A | wp4 floor `:115-124` (`(Ũ,v)` double-null, orden producto en `r>0`) |
| Existencia de coordenadas nulas para Schwarzschild 1+1 | A | wp4 floor `:79-81`, `:115-124`; manuscript_limits `:246-248` |
| Rectangularidad `I × J` del **parche H** en nulas | B | wp4 Prop. 2 `:83-92`: soporte `S_tau` con intervalo en `Ũ` **dependiente de `v`**; no es caja. Diamante `D_tau` sí es caja (`:126-130`) y **no es H** |
| Condicionamiento a `N` | B | El estrato H dado `N=n` sí es iid por el Lema 2.1 (`manuscript_limits:294-298`), pero el protocolo/result H observa la mezcla Poisson con `N` variable (`002 result:38-45`); transportar S2 estrato a estrato al resultado no condicionado exige un puente |
| Medida de sprinkling | C | H: Lebesgue `dv dr` para todo `tau` (wp4 `:77-79`). F: `q_epsilon` conforme sobre caja nula |
| PIT | B | F: PIT sobre caja nula, Lema A. H: Prop. 2, soporte no rectangular ⇒ PIT de S1 no aplica literalmente |
| Cópula sobre `[0,1]^2` completo | B | S1 (3.4). Marginales uniformes ≠ soporte rectangular completo (consigna 4.4) |
| Parámetro / tangente `h_psi` | B | F: `epsilon` en Minkowski. H: BH vs MINK (misma nube) y scoring de `r_S`; no hay familia `g_epsilon` escrita para H |
| Permutación de rangos `Pi_N` | A | A `N=n` fijo y sin empates, el chart global `(Ũ,v)` tiene orden producto (wp4 `:115-124`), por lo que ordenar por `Ũ` y registrar rangos de `v` da exactamente `Pi_n` como en S1 `:382-390`; es representación latente, no input del estimador |
| Cociente a poset no etiquetado | A | El poset inducido por ese orden producto es exactamente `[P_{Pi_n}]`; H observa el poset anonimizado y `|C|` (`preregistration:8-11, 61-67`), igual que el lado posterior del canal S2 (`S2:69-73`) |
| Información Fisher S2 | B | QMD/Fisher no están habilitados para H. WP4 Prop. 2 `:83-92` afirma no regularidad, pero está rotulada **sketch**; `manuscript_limits` Prop. 3.4 `:552-558` repite el claim como `[PROVED] (sketch in annex)` sin completar la cota Hellinger. `MOVING_SUPPORT_QMD_STATUS = OPEN` en esta auditoría |
| Observable `O=\|future\|` | C | estimator_v2_seal `:16-17`. No entra en Teorema 8 (S2 `:4`, claim ceiling) |
| Localización de boundary | C | addendum `:64-73`; 002 result `:49-51`. No hay lema que la ligue a `I^{[P]}/I^Pi` |
| Interpretación como horizonte | C | addendum `:75-84` (no `r_h→2M`); Teorema 3.2; Hayward C3-early |
| Transferencia al square-box | C | addendum new_geometry `:8-43`: `BH_MINK_DISPERSION_DIFFERENCE_DETECTED`, no localización |
| Transferencia 2+1 / 3+1 | C | R4 §6; S2 autorización STOP_AFTER_S2; Teorema 3.1 TV=0 de escala |

Ninguna fila A convierte H en F. Las primeras dos son propiedades geométricas;
las otras dos identifican exactamente el **esqueleto finito del canal** a `n`
fijo. No identifican su ley paramétrica con la de S2 ni transportan Fisher.

## 6. DOMAIN_AUDIT

F1. En coordenadas nulas `(Ũ, v)` documentadas, la imagen del rectángulo
EF `B=[0,T]×[r_a,r_b]` es

```text
S_tau = { (Ũ, v) : v in [0,T],
          Ũ in -e^{-v/(2 tau)} [W_tau(r_b), W_tau(r_a)] }
```

(`wp4_fisher_localization_floor.md:83-85`). El intervalo de `Ũ` depende
de `v`. **No es una caja cartesiana `I × J`.** La fórmula también depende
de `tau`, pero eso no basta por sí solo para concluir que la diferencia
Hellinger sea de primer orden.

El argumento S1/S2 que usa la caja: dominio `D=[0,1]^2` (S1 `:75-78`);
cámara `C_pi` de rangos en el cuadrado (S1 §5); densidad de cópula (3.4)
sobre el cuadrado completo; QMD en `epsilon=0` con soporte fijo.

El diamante de límites `D_tau` **sí** es caja nula
(`wp4_fisher_localization_floor.md:126-130`). Ese parche no es el
benchmark sellado.

**Conclusión de dominio.** Aplicar S1/S2 *literalmente* a H queda
bloqueado por la forma del soporte. Eso basta para F1.

**Microauditoría QMD.** WP4 Prop. 2 (`:83-92`) contiene el mecanismo
específico propuesto —borde a velocidad no nula, densidad inferior positiva
y franja de área `asymp |delta|`—, pero el propio enunciado lo marca
`sketch`. No hay en el anexo ni en sus chequeos simbólicos una derivación
para los extremos sellados que establezca esas tres premisas y la cota
`H^2(p_tau,p_{tau+delta}) >= c_1|delta|`. Prop. 3.4 del manuscrito
(`:552-558`) repite el resultado y remite al mismo bosquejo; no añade prueba.

```text
MOVING_SUPPORT_QMD_STATUS = OPEN
```

Por tanto, esta auditoría no promueve `moving support => QMD fails`. Sí
registra que la familia H no satisface **ya demostradas** las hipótesis de
soporte fijo y QMD de S1/S2.

## 7. CONDITIONING_AND_MEASURE_AUDIT

- **Cambio de coordenadas.** `(v,r) → (Ũ,v)` está escrito (wp4 §§3–4).
  Preserva el orden y permite la representación por rangos, pero no es una
  equivalencia con el experimento **regular de S2**: empuja la ley uniforme de
  `B` a `S_tau` no rectangular. La fórmula `h_tau` de wp4 `:132-136` es para
  el diamante y no se usa como si cubriera H.
- **Jacobiano/volumen.** En EF, `det g=-1` ⇒ `dvol=dv dr` independiente
  de `tau` (wp4 `:77-79`). En nulas, la geometría reaparece en la
  densidad y en el soporte. Eso es F5: la transformación cambia el
  experimento estadístico.
- **Cardinalidad.** F condiciona a `N=n`. H es Poisson de intensidad y `N`
  es aleatorio (`N̄` en 002 result `:38-45`). El Lema 2.1 sí da, al
  condicionar H a un valor observado `N=n`, `n` puntos iid de volumen
  normalizado (`manuscript_limits:294-298`). Lo no demostrado es que el
  resultado Fisher estratificado se recomponga en el experimento Poisson
  order+number que evaluó prereg-002.
- **Truncación.** H incluye `r=0.1` (cercanía a singularidad) y paredes
  de caja. F no tiene singularidad.

## 8. PIT_COPULA_AUDIT

El PIT de Lema A se prueba para una caja nula con densidad positiva y
marginales estrictamente crecientes (dicotomía §2). En ese caso
`T=(F,G)` es un homeomorfismo de la caja sobre el cuadrado completo.

Sobre `S_tau`, los rangos siguen definidos y las transformaciones marginales
pueden uniformar las marginales, pero la medida resultante no llena
automáticamente `[0,1]^2` con soporte producto y densidad positiva.
Marginales uniformes ≠ soporte rectangular completo.

No hay en el registro un teorema que convierta la ley de H, tras PIT, en
el experimento de cópula de S1. F1 implica que el PIT de S1 no se
instancia.

## 9. PHYSICAL_PARAMETER_AUDIT

H no define un parámetro local diferenciable. En el protocolo varían:

- presencia de Schwarzschild vs MINK **con la misma nube**
  (addendum `:41`; prereg `:34-35`);
- y, al puntuar, la posición de minimales relativa a `r_S` fijo
  (`r_S=0.5`).

La intensidad toma cuatro valores, pero `M=0.25`, `r_S=0.5` y el patch se
mantienen fijos (`thresholds.py:35-48`).

```text
LOCAL_PHYSICAL_PARAMETER = NOT_DOCUMENTED
```

No existe familia diferenciable de H cuyo score en un punto base se
identifique con un tangente `h_psi` de S1.

```text
PHYSICAL_TANGENT_BRIDGE = OPEN
```

Además, sobre la caja EF no está legitimado aplicar Fisher S2: la QMD de la
familia no está probada y su negación sólo está bosquejada (WP4 Prop. 2;
manuscript_limits Prop. 3.4).

## 10. FISHER_VS_LOCALISATION_AUDIT

Teorema 8 compara `I^{[P]}` con `I^Pi` para el score de rangos de la
clase rank-one en F. El estimador H usa `O=|future|` y un bracket en
`r`.

Ningún documento leído demuestra una implicación

```text
I^{[P]}/I^Pi -> 1   =>   localizacion del bracket de O
```

```text
FISHER_TO_LOCALISATION_BRIDGE = OPEN
```

Alta Fisher no implica localización. El PASS de 002 no es un dato de
Fisher. El suelo 3.8 es un minimax sobre la **familia diamante** (parche
B), no un rendimiento de `O` sobre H.

## 11. FALSIFIERS

**F1 — dominio.** Activado. `S_tau` no es caja. S1/S2 literal no aplica
a H. Esto no decide por sí solo QMD para otra representación común.

**F2 — parámetro.** Activado. No hay familia `g_epsilon` de H
identificada con `psi`. `PHYSICAL_TANGENT_BRIDGE = OPEN`.

**F3 — canal observado.** No destruye el esqueleto del canal: a `N=n` fijo,
H admite la misma representación latente `Pi_n -> [P_{Pi_n}]`. H observa el
lado cocientado y `|C|`, no `Pi_n`, exactamente como exige su contrato. La
diferencia decisiva está en la ley Poisson/soporte y en el score, no en el
mapa finito de cociente.

**F4 — Fisher vs localización.** Activado. Puente abierto. PASS 002 y
Teorema 8 son objetos distintos.

**F5 — coordenadas.** Activado. El paso a nulas cambia soporte y densidad;
no cuenta por sí solo como puente. Su efecto exacto sobre QMD permanece
`OPEN` en esta auditoría.

## 12. FIRST_PHYSICAL_OBSTACLE

```text
FIRST_PHYSICAL_OBSTACLE = DOMAIN_BRIDGE
```

**Por qué va primero.** S1/S2 está definido sobre un soporte producto fijo
`I × J`, con densidad positiva y QMD en el punto base. El parche H, en las
nulas ya escritas, no tiene ese soporte; la familia de soportes depende de
`tau`, pero el claim más fuerte de pérdida de QMD no está cerrado. La
representación `Pi_n -> [P]` sobrevive, pero no se ha construido ni probado
un likelihood regular equivalente al de S1. Sin `DOMAIN_BRIDGE` no existe
aún un experimento regular demostrado sobre el cual identificar el tangente
físico; el puente Fisher→localización viene después.

El diamante `D_tau` (parche B) resuelve la rectangularidad **para otro
experimento**, no para H. Sustituir H por B sería un cambio de
experimento físico, no un transporte.

Obligación exacta, una frase:

> Probar un transporte paramétricamente común desde la familia del rectángulo EF sellado —incluida su ley Poisson descompuesta en estratos `N=n`— a una familia de soporte nulo fijo, densidad positiva y QMD que preserve la ley del canal `Pi_n -> [P_{Pi_n}]`, o probar que tal transporte no existe.

Ese mapa **no está** en el repositorio. Prop. 2 muestra que el
candidato obvio (push-forward a `(Ũ,v)`) no produce la caja; su afirmación
adicional `H^2 >= c_1|delta|` permanece como bosquejo no cerrado.

## 13. SCIENTIFIC_VERDICT

```text
PHYSICAL_REENTRY = PARTIAL_TRANSPORT_WITH_EXACT_FIRST_OBLIGATION
```

Hay transporte exacto parcial: orden producto en nulas globales y, por
estratos `N=n`, la representación `Pi_n -> [P_{Pi_n}]`. Eso no convierte la
**ley paramétrica de H** en el **experimento regular F**. La consigna 4 lo
excluye explícitamente: ser 1+1 conforme-plano no es el puente estadístico.

Adversarial: no se elige `EXACT_TRANSPORT`. La obligación parcial no es
“probar que H es caja” —el registro ya prueba que no lo es—, sino resolver
si existe una equivalencia estadística regular distinta del push-forward
obvio, con todas las preservaciones escritas en la frase de §12.

## 14. PROHIBITED_INFERENCES

```text
NO_S2_EQUALS_SEALED_BENCHMARK
NO_NULL_DIAMOND_IS_THE_BENCHMARK
NO_FISHER_IMPLIES_LOCALISATION
NO_DISPERSION_IS_LOCALISATION
NO_CONFORMAL_FLATNESS_IS_THE_BRIDGE
NO_HORIZON_CLAIM_FROM_FISHER
NO_2PLUS1
NO_3PLUS1
NO_FORCED_BRIDGE
```

Square-box: diferencia de dispersiones, no localización de horizonte.

## 15. NEXT_GATE

```text
NEXT_RUN_AUTHORIZED = NO
NEXT_PHYSICAL_DECISION = PENDING_PI
```

Tras F1, siguen abiertas y **no se toman**: (a) un puente matemático de
dominio (teorema nuevo, autorización nueva); (b) volver al observable
de horizonte como otro gate, sin Fisher como programa.

Este run no autoriza el siguiente cálculo.

## 16. POST-AUDIT DOMAIN-BRIDGE RESOLUTION — 2026-08-28

Tras la instrucción explícita del PI registrada en
`docs/program_domain_bridge_authorization_2026-08-28.md`, la primera
obligación exacta se resolvió analíticamente en
`research_program/work_packages/wp6_domain_bridge_fixed_ef_box.md`.

Las velocidades de los extremos son no nulas casi en todo `v`, la diferencia
simétrica de soportes tiene área `Theta(|delta|)` y la densidad transportada
tiene una cota inferior positiva localmente uniforme en `tau`. Por tanto:

```text
H^2(p_tau,p_{tau+delta}) >= c_tau |delta|
MOVING_SUPPORT_QMD_STATUS = PROVED_NON_QMD_FOR_POINT_EXPERIMENT
COMMON_POINT_ISOMORPHISM = REFUTED
FINITE_CHANNEL_REGULARITY = OPEN
DOMAIN_BRIDGE = OPEN_AT_FINITE_CHANNEL
NEXT_RUN_AUTHORIZED = NO
```

El resultado negativo es invariante bajo cualquier isomorfismo estadístico
común e independiente del parámetro. No afirma no-QMD después del canal de
permutaciones o posets no etiquetados, ni abre el puente Fisher→localización.
