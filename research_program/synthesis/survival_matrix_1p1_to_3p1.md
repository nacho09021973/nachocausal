# Matriz de supervivencia 1+1D -> 3+1D

**Unidad:** `OP-0.1`

**Estado:** `AUDIT_PENDING / DOCUMENT_ONLY / NO_NEW_SCIENCE`

**Snapshot de fuentes:** `726c8c1` (2026-07-15)

## 1. Alcance y regla de lectura

Esta matriz audita que tecnologia de PR011/PR012 puede financiar trabajo 3+1D. No demuestra
transferencia dimensional, no define el target 3+1D y no autoriza codigo, simulaciones,
publicacion de PR012 ni cambios en artefactos congelados.

Cada fila contiene:

- una clasificacion de supervivencia;
- un anclaje `file:line` o el literal `NO_ESPECIFICABLE`;
- un terminal negativo que puede bloquear la fila.

Clasificaciones:

- `SURVIVES_AS_PROTOCOL`: sobrevive una regla metodologica, no un teorema dimensional;
- `SURVIVES_CONDITIONALLY`: solo sobrevive si se prueba la condicion declarada;
- `DOES_NOT_TRANSFER`: el constructo depende de 1+1D o responde otra pregunta;
- `NO_ESPECIFICABLE`: las fuentes cerradas abajo no contienen una especificacion auditable.

`NO_ESPECIFICABLE` significa ausencia en este corpus cerrado, no una afirmacion sobre toda la
literatura:

1. `research_program/synthesis/pr011_mass_distinguishability_viability.md`;
2. `research_program/synthesis/pr012_tv_curve_scope.md`;
3. `research_program/models/first_witness_pair_candidates.md`;
4. `research_program/work_packages/wp4_two_point_theorem.md`;
5. `dev/PR003_C1_RELATIONAL_SPEC.md`.

La busqueda negativa se limita a los ejes congelados en el plan: target, dualidad, canal/escala,
patch, limites, salida/perdida, alternativas, direccion de garantia y abstencion. Por tanto, una
fila `NO_ESPECIFICABLE` debe abrir trabajo teorico; nunca cuenta como transferencia tacita.

## 2. Resumen ejecutivo

| Constructo | Veredicto de transferencia | Consecuencia WP5 |
|---|---|---|
| Familia `G_diamond` | `SURVIVES_AS_PROTOCOL` como patron de familia compacta y congelada; la geometria 1+1D no viaja | Definir una familia 3+1D nueva antes de generar datos |
| Canal `N=n` | `SURVIVES_AS_PROTOCOL` como experimento condicionado; no equivale a `order+number` | Mantener separados `fixed_n` y Poisson con `rho` conocida |
| Target escalar `tau` | `DOES_NOT_TRANSFER` como proxy/localizador de horizonte | Especificar primero target set-valued o perdida geometrica 3+1D |
| Certificador Hellinger | `SURVIVES_CONDITIONALLY` como cota superior por data processing; la reduccion por copula es 2D | No usarlo como evidencia positiva ni asumir un mapa de puntos a posets 3+1D ya certificado |
| Escalera `n=4,...,8` | `SURVIVES_AS_PROTOCOL` solo como patron fail-closed; los valores no viajan | Disenar una escalera 3+1D por presupuesto y resolucion propios |
| Curva PR012 en `Delta tau` | `SURVIVES_AS_PROTOCOL` como sensibilidad a separacion parametrica y abstencion | No confundirla con `n_star(Delta tau)` ni con convergencia |
| Interfaz `H[C;R]` y selector de `R` | `SURVIVES_CONDITIONALLY` como tipo relacional; el selector actual falla estructuralmente | Resolver target y selector antes de cualquier probe 3+1D |

## 3. Familia `G_diamond`

| Eje | Estado 1+1D y disposicion 3+1D | Anclaje | Terminal negativo |
|---|---|---|---|
| Target | PR011 asocia la familia al escalar `tau=2M`, y excluye expresamente un target set-valued. La familia no especifica el proxy 3+1D. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:78-98` | `TARGET_NOT_SPECIFIABLE` |
| Orientacion/dualidad | Usa coordenadas EF ingoing, pero no define accion sobre `G union G^op` ni salidas BH/WH. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:78-92` | `DUAL_CLOSURE_FAIL` |
| Canal/escala | La familia se observa como poset no etiquetado y PR011 condiciona despues a `N=n`; `rho` no entra en esa ley. Sobrevive solo si el canal 3+1D se congela aparte. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:91-92`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:106-114` | `CHANNEL_AMBIGUOUS` |
| Patch | El patch es un diamante finito definido por esquinas EF y cruza el horizonte. Sobrevive el requisito de congelar el patch, no estas esquinas ni esta dimension. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:85-90` | `PATCH_CONTRACT_FAIL` |
| Limite continuo | PR011 declara una familia compacta y ningun limite de densidad o extension; no hay dos leyes de limite. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:100-119`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:169` | `LIMIT_NOT_TESTABLE` |
| Salida/perdida | La salida del canal es la clase de isomorfismo del poset, pero la familia no define salida geometrica ni perdida 3+1D. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:91-98` | `TARGET_WITNESS_MISMATCH` |
| Alternativas | Solo excluye cajas Kruskal y pares relacionados por escala; no congela nulas sin horizonte ni alternativas adversariales 3+1D. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:94-98` | `ADVERSARIAL_CLASS_MISSING` |
| Garantia | La familia por si sola no garantiza separacion; PR011 le aplica una cota superior TV. No sobrevive como garantia positiva. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:194-212` | `GUARANTEE_DIRECTION_MISSING` |
| Abstencion | La construccion exige diamante no vacio y geometria sana, pero no define abstencion de un reconstructor. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:85-90`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:253-265` | `ABSTENTION_NOT_DEFINED` |

**Veredicto:** `SURVIVES_AS_PROTOCOL`. Sobrevive congelar una familia regular, compacta y
auditable. `G_diamond` no es la familia 3+1D candidata.

## 4. Canal condicionado `N=n`

| Eje | Estado 1+1D y disposicion 3+1D | Anclaje | Terminal negativo |
|---|---|---|---|
| Target | El canal transporta un poset de cardinalidad fija; no determina que target se estima. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:138-158` | `TARGET_NOT_SPECIFIABLE` |
| Orientacion/dualidad | Condicionar en cardinalidad no rompe ni resuelve la dualidad temporal. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:138-150` | `DUAL_CLOSURE_FAIL` |
| Canal/escala | Esta completamente especificado como ley sobre posets no etiquetados a igual `n`; cierra la fuga Poisson. No es el canal `order+number` con `rho` fisica conocida. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:138-150`; `research_program/models/first_witness_pair_candidates.md:23-31` | `CHANNEL_AMBIGUOUS` |
| Patch | Normaliza la medida dentro de cada patch y por ello elimina la informacion de volumen total; cualquier uso 3+1D debe declarar esa perdida. | `research_program/models/first_witness_pair_candidates.md:23-31`; `research_program/models/first_witness_pair_candidates.md:77-84` | `PATCH_CONTRACT_FAIL` |
| Limite continuo | PR011 trabaja en `n` fijo y no prueba asintotica en `n`; densidad y extension siguen sin ley. | `research_program/work_packages/wp4_two_point_theorem.md:170-181` | `LIMIT_NOT_TESTABLE` |
| Salida/perdida | La salida observable es el poset no etiquetado; no hay perdida geometrica asociada al canal. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:138-158` | `TARGET_WITNESS_MISMATCH` |
| Alternativas | Toda pareja adversarial debe igualar la ley de `N` o declarar condicionamiento. Esta disciplina si sobrevive. | `research_program/work_packages/wp4_two_point_theorem.md:149-157` | `ADVERSARIAL_CLASS_MISSING` |
| Garantia | El canal no da una direccion de garantia; admite cotas superiores e inferiores que deben declararse por separado. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:194-212` | `GUARANTEE_DIRECTION_MISSING` |
| Abstencion | La cardinalidad fija no define cuando un estimador debe abstenerse. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:138-150` | `ABSTENTION_NOT_DEFINED` |

**Veredicto:** `SURVIVES_AS_PROTOCOL`. Es un experimento estadistico legitimo, pero responde una
pregunta distinta del canal Poisson donde `N` informa sobre `rho V`.

## 5. Target escalar `tau`

| Eje | Estado 1+1D y disposicion 3+1D | Anclaje | Terminal negativo |
|---|---|---|---|
| Target | Esta definido como `T(tau)=tau=2M` dentro de `G_diamond`; no es una frontera ni una region atrapada discreta. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:152-158`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:96-98` | `TARGET_NOT_SPECIFIABLE` |
| Orientacion/dualidad | Un escalar de masa no porta caracter BH/WH ni ley anti-equivariante. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:152-158` | `DUAL_CLOSURE_FAIL` |
| Canal/escala | A `N=n`, `tau` solo se interpreta dentro de la carta congelada; la escala absoluta queda bloqueada por la orbita de dilatacion. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:65-74`; `research_program/models/first_witness_pair_candidates.md:62-105` | `CHANNEL_AMBIGUOUS` |
| Patch | Las esquinas fijas hacen variar la forma relativa al variar `tau`; el target no define como extender el patch. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:85-98`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:121-134` | `PATCH_CONTRACT_FAIL` |
| Limite continuo | PR011 solo certifica dos valores y una escalera finita; no hay consistencia en densidad ni extension. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:160-169`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:303-310` | `LIMIT_NOT_TESTABLE` |
| Salida/perdida | PR011 deriva riesgo metrico escalar en `tau`; eso no puntua fidelidad de un conjunto-frontera. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:228-251` | `TARGET_WITNESS_MISMATCH` |
| Alternativas | El par `(0.95,1.05)` prueba sensibilidad local dentro de una sola familia, no especificidad frente a no-horizonte o adversarios. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:121-134` | `ADVERSARIAL_CLASS_MISSING` |
| Garantia | La cota superior pequena produce un suelo minimax grande: certifica dificultad, no recuperacion positiva. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:230-247`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:352-359` | `GUARANTEE_DIRECTION_MISSING` |
| Abstencion | PR011 tiene terminales de certificacion, pero no una abstencion de reconstructor escalar o geometrico. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:253-265` | `ABSTENTION_NOT_DEFINED` |

**Veredicto:** `DOES_NOT_TRANSFER` como localizador. Puede sobrevivir como parametro de simulacion y
scoring, nunca como sustituto del target intrinseco 3+1D.

## 6. Certificador Hellinger

| Eje | Estado 1+1D y disposicion 3+1D | Anclaje | Terminal negativo |
|---|---|---|---|
| Target | Acota distancia entre leyes; no construye el objeto estimado. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:194-205` | `TARGET_NOT_SPECIFIABLE` |
| Orientacion/dualidad | Es agnostico a dualidad salvo que las dos leyes y el estadistico se cierren bajo ella. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:194-205` | `DUAL_CLOSURE_FAIL` |
| Canal/escala | Es valido para el canal declarado; la reduccion concreta pasa por densidades de copula 2D y data processing. Esa implementacion no se presume en 3+1D. | `research_program/models/first_witness_pair_candidates.md:33-49`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:203-205` | `CHANNEL_AMBIGUOUS` |
| Patch | Compara leyes inducidas por patches ya definidos; no certifica que la truncacion sea inocua. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:194-205` | `PATCH_CONTRACT_FAIL` |
| Limite continuo | Tensoriza para productos independientes, pero la asintotica en densidad requiere una secuencia de modelos y no esta probada. | `research_program/work_packages/wp4_two_point_theorem.md:170-181` | `LIMIT_NOT_TESTABLE` |
| Salida/perdida | Produce `epsilon` y consecuencias minimax, no una salida geometrica. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:228-251` | `TARGET_WITNESS_MISMATCH` |
| Alternativas | Solo compara el par nombrado; no crea ni valida una clase adversarial. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:194-212` | `ADVERSARIAL_CLASS_MISSING` |
| Garantia | Direccion explicita: `TV <= epsilon`. PR011 declara que una cota inferior sola no cierra su pregunta. No es evidencia positiva de recuperacion. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:194-212` | `GUARANTEE_DIRECTION_MISSING` |
| Abstencion | Tiene fallos numericos y certificacion incompleta; PR012 materializa `GRID_RESOLUTION_ABSTAIN`. Esta regla fail-closed si sobrevive. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:214-226`; `research_program/synthesis/pr012_tv_curve_scope.md:54-71` | `ABSTENTION_NOT_DEFINED` |

**Veredicto:** `SURVIVES_CONDITIONALLY`. Sobrevive la desigualdad estadistica y la disciplina de
errores; no sobreviven automaticamente la copula 2D, el mapa de data processing ni la direccion
positiva que necesita recoverability.

## 7. Escalera `n=4,...,8`

| Eje | Estado 1+1D y disposicion 3+1D | Anclaje | Terminal negativo |
|---|---|---|---|
| Target | La escalera no define target; solo evalua el par escalar congelado. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:121-134`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:160-169` | `TARGET_NOT_SPECIFIABLE` |
| Orientacion/dualidad | No contiene prueba dual ni convencion temporal. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:160-169` | `DUAL_CLOSURE_FAIL` |
| Canal/escala | Todos los peldaños pertenecen al mismo canal `N=n`; variar `n` entre leyes no se autoriza sin formulacion conjunta. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:147-150`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:160-169` | `CHANNEL_AMBIGUOUS` |
| Patch | Mantiene fija la regla de familia, pero no varia extension del patch. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:85-114` | `PATCH_CONTRACT_FAIL` |
| Limite continuo | Cinco puntos tractables no establecen ley asintotica; el propio teorema separa `n` fijo de densidad creciente. | `research_program/work_packages/wp4_two_point_theorem.md:170-181`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:347-350` | `LIMIT_NOT_TESTABLE` |
| Salida/perdida | Registra `epsilon`, `n` y metodo, no salida de horizonte. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:253-265` | `TARGET_WITNESS_MISMATCH` |
| Alternativas | Repite un unico par de masas; no escala una clase adversarial. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:121-134` | `ADVERSARIAL_CLASS_MISSING` |
| Garantia | Toda la escalera certifica cotas superiores pequenas y suelos minimax cercanos a moneda al aire; no mide el encendido positivo. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:337-359` | `GUARANTEE_DIRECTION_MISSING` |
| Abstencion | El protocolo permite parar o emitir inviabilidad por techo computacional. Sobrevive el patron, no el presupuesto numerico. | `research_program/synthesis/pr011_mass_distinguishability_viability.md:160-169`; `research_program/synthesis/pr011_mass_distinguishability_viability.md:222-226` | `ABSTENTION_NOT_DEFINED` |

**Veredicto:** `SURVIVES_AS_PROTOCOL`. Los valores `{4,...,8}` no financian una escalera 3+1D; si
financian el patron de presupuesto previo, parada y terminal explicito.

## 8. Curva PR012 en `Delta tau`

| Eje | Estado 1+1D y disposicion 3+1D | Anclaje | Terminal negativo |
|---|---|---|---|
| Target | Varia separacion del target escalar a `n=8`; no localiza una frontera. | `research_program/synthesis/pr012_tv_curve_scope.md:20-27`; `research_program/synthesis/pr012_tv_curve_scope.md:110-121` | `TARGET_NOT_SPECIFIABLE` |
| Orientacion/dualidad | No contiene familia dual-cerrada ni salida de caracter. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr012_tv_curve_scope.md:20-27` | `DUAL_CLOSURE_FAIL` |
| Canal/escala | Congela `N=n`, `n=8`, y excluye explicitamente el canal Poisson-`rho`. Esta separacion de canales sobrevive. | `research_program/synthesis/pr012_tv_curve_scope.md:20-27`; `research_program/synthesis/pr012_tv_curve_scope.md:110-121` | `CHANNEL_AMBIGUOUS` |
| Patch | Reutiliza sin variar las esquinas de PR011; no estudia extension. | `research_program/synthesis/pr012_tv_curve_scope.md:110-121` | `PATCH_CONTRACT_FAIL` |
| Limite continuo | Es curva en `Delta tau` a `n` fijo, no `n_star(Delta tau)`, limite de densidad ni limite de patch. | `research_program/synthesis/pr012_tv_curve_scope.md:20-27`; `research_program/synthesis/pr012_tv_curve_scope.md:145-154` | `LIMIT_NOT_TESTABLE` |
| Salida/perdida | Cada fila produce cota superior y suelo minimax, no un estimador ni perdida geometrica. | `research_program/synthesis/pr012_tv_curve_scope.md:73-82`; `research_program/synthesis/pr012_tv_curve_scope.md:126-143` | `TARGET_WITNESS_MISMATCH` |
| Alternativas | Recorre pares dentro de `G_diamond`; no incluye nulas sin horizonte ni alternativas disenadas. `NO_ESPECIFICABLE`. | `research_program/synthesis/pr012_tv_curve_scope.md:110-121` | `ADVERSARIAL_CLASS_MISSING` |
| Garantia | Corrige la tensorizacion pero mantiene `TV <= epsilon`; los suelos ~0.49 certifican dificultad. | `research_program/synthesis/pr012_tv_curve_scope.md:84-108`; `research_program/synthesis/pr012_tv_curve_scope.md:139-143` | `GUARANTEE_DIRECTION_MISSING` |
| Abstencion | Define `GRID_RESOLUTION_ABSTAIN` para puntos que fallan estabilidad y prohibe publicacion sin gates. Este patron sobrevive. | `research_program/synthesis/pr012_tv_curve_scope.md:54-71`; `research_program/synthesis/pr012_tv_curve_scope.md:176-190` | `ABSTENTION_NOT_DEFINED` |

**Veredicto:** `SURVIVES_AS_PROTOCOL`. La curva es un diagnostico de sensibilidad parametrica y un
precedente de abstencion; no sustituye la ley de encendido `n_star(Delta tau)`.

## 9. Interfaz `H[C;R]` y selector de `R`

| Eje | Estado 1+1D y disposicion 3+1D | Anclaje | Terminal negativo |
|---|---|---|---|
| Target | `H[C;R]` es una interfaz relacional finita, expresamente no un horizonte de eventos; no se ha especificado su limite hacia atrapamiento puntual 3+1D. | `dev/PR003_C1_RELATIONAL_SPEC.md:10-37`; `dev/PR003_C1_RELATIONAL_SPEC.md:174-182` | `TARGET_NOT_SPECIFIABLE` |
| Orientacion/dualidad | La orientacion local fue corregida a links `A_R -> B_R`, pero no hay clausura `G union G^op` ni ley anti-equivariante del caracter. | `dev/PR003_C1_RELATIONAL_SPEC.md:18-28`; `dev/PR003_C1_RELATIONAL_SPEC.md:209-219` | `DUAL_CLOSURE_FAIL` |
| Canal/escala | La entrada es solo el poset finito; no usa `N` como estimador de volumen ni declara `rho`. | `dev/PR003_C1_RELATIONAL_SPEC.md:10-16`; `dev/PR003_C1_RELATIONAL_SPEC.md:143-156` | `CHANNEL_AMBIGUOUS` |
| Patch | El riesgo de pared de muestreo y el control bulk siguen abiertos; por tanto la dependencia del patch no esta controlada. | `dev/PR003_C1_RELATIONAL_SPEC.md:39-57`; `dev/PR003_C1_RELATIONAL_SPEC.md:174-180` | `PATCH_CONTRACT_FAIL` |
| Limite continuo | No hay ley de densidad ni extension y la interpretacion fisica sigue abierta. `NO_ESPECIFICABLE`. | `dev/PR003_C1_RELATIONAL_SPEC.md:174-182` | `LIMIT_NOT_TESTABLE` |
| Salida/perdida | La salida estructurada `(R, interface)` es order-only y relabel-equivariant; no existe perdida geometrica 3+1D congelada. | `dev/PR003_C1_RELATIONAL_SPEC.md:143-172` | `TARGET_WITNESS_MISMATCH` |
| Alternativas | `BULK_CONTROL` esta abierto y no existe clase adversarial de pared/truncacion/inhomogeneidad congelada. | `dev/PR003_C1_RELATIONAL_SPEC.md:174-180`; `dev/PR003_C1_RELATIONAL_SPEC.md:129-139` | `ADVERSARIAL_CLASS_MISSING` |
| Garantia | No hay cota superior ni inferior TV asociada al selector; no puede actuar aun como testigo positivo. `NO_ESPECIFICABLE`. | `dev/PR003_C1_RELATIONAL_SPEC.md:174-207` | `GUARANTEE_DIRECTION_MISSING` |
| Abstencion | `H` vacio devuelve `NO_INTERFACE`; ademas, el selector `R=Max(C)` esta demostrado degenerado en todo poset finito. Sobrevive la abstencion, no el selector. | `dev/PR003_C1_RELATIONAL_SPEC.md:69-74`; `dev/PR003_C1_RELATIONAL_SPEC.md:184-207` | `ABSTENTION_NOT_DEFINED` |

**Veredicto:** `SURVIVES_CONDITIONALLY`. Sobreviven el tipo de salida relacional, la equivariancia
por relabeling y `NO_INTERFACE`. No sobrevive `R=Max(C)`; cualquier reemplazo requiere nueva
revision antes de datos.

## 10. Bloqueos que pasan a Fase 1

La matriz no bloquea por falta de anclajes: bloquea de forma informativa la transferencia de los
siguientes contenidos no especificados:

1. target intrinseco 3+1D y perdida geometrica compatible con patch;
2. clausura dual de la familia y ley de transformacion de localizacion/caracter;
3. clase `TV=0` de la familia 3+1D en cada canal;
4. testigo order-only que produzca una cota inferior TV con cobertura declarada;
5. leyes separadas de densidad y extension de patch;
6. clase de alternativas nulas y adversariales;
7. selector de `R` no degenerado o abandono explicito de esa interfaz.

Estos siete bloqueos corresponden a OP-1.1--OP-1.5. Ninguno autoriza implementacion 3+1D.

## 11. Puerta WP5 y terminal OP-0.1

La contribucion 1+1D que sobrevive es metodologica: contratos de canal, pares nombrados, direccion
de garantia, presupuesto fail-closed, abstencion y salidas order-only. Los objetos geometricos y
los numeros de PR011/PR012 no se promueven a 3+1D.

```text
WP5_RELEVANCE = PASS_FOR_TRANSFER_AUDIT_ONLY
OP_0_1_AUTHOR_TERMINAL = SURVIVAL_MATRIX_COMPLETE
OP_0_1_GATE = AUDIT_PENDING
```

El terminal efectivo sera uno de:

- `SURVIVAL_MATRIX_COMPLETE`, si `/auditor` confirma todas las celdas;
- `SURVIVAL_MATRIX_BLOCKED(<celda>)`, si falta un anclaje o un `NO_ESPECIFICABLE` honesto;
- `SURVIVAL_MATRIX_AUDIT_FAIL`, si el informe no pasa su checker o detecta sobreclaim.
